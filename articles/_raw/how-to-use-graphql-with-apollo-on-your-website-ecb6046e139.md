---
title: How to Use GraphQL with Apollo on Your Website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-21T16:00:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-graphql-with-apollo-on-your-website-ecb6046e139
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DQ22UoX0M8_mdFj3rkc5sQ@2x.png
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondrej Polesny

  In my previous article, I explained why it makes sense to decouple the front-end
  part of a website from its back-end services. I introduced GraphQL, Apollo and other
  tools that enable such abstraction and make maintenance of product...'
---

By Ondrej Polesny

In my [previous article](http://bit.ly/2TW60L6), I explained why it makes sense to decouple the front-end part of a website from its back-end services. I introduced GraphQL, Apollo and other tools that enable such abstraction and make maintenance of production websites a nice experience.

In this article, I will show you a boilerplate that already has all these tools set up and saves you a lot of time when starting the development.

[Check out the live demo of the boilerplate](http://bit.ly/2GGHIB5)

# Boilerplate to Speed Up the Start

Let’s start with the tools I used:

* Node.js — runtime
* Express — web application framework
* Apollo server — middleware service with GraphQL support
* Apollo client — GraphQL client
* Kentico Cloud tools — headless CMS
* Pug — template engine

# Schema and Resolvers Code

The first step in building the site is to create or generate a schema. I already mentioned in the previous article that I am using [Content-as-a-Service platform Kentico Cloud](http://bit.ly/2QzUALM) for content storage. The content that is stored there is already structured within defined model structures. Therefore I can quickly generate the schema using the [schema generator](http://bit.ly/2SqEAju):

kc-generate-gql-schema — projectId {projectID} — createModule

But it’s also possible to define all the models manually in the following syntax.

const TYPE_DEFINITION = `  
    
  type SystemInfo {  
    id: String!  
    name: String!  
    codename: String!  
    language: String!  
    type: String!  
    lastModified: String!  
  }  
    
  interface ContentItem {  
    system: SystemInfo!  
  }  
  ...  
  type FactAboutUsContentType implements ContentItem {  
    system: SystemInfo!  
    description: RichTextElement  
    title: TextElement  
    image: AssetElement  
  }  
  ...`module.exports = {  
  TYPE_DEFINITION  
}

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/types.js)_.)_

The model generator lists all the system types including links, texts, datetime fields, images and others (`SystemInfo` above), followed by the data models of each of the custom content models (`FactAboutUsContentType`). We will need to use the type definition as a module, hence the last argument `createModule`.

The next step is to create GraphQL queries and resolvers. As the content API is read-only, the queries are quite simple and limited to fetch all items or items grouped by type:

const queryTypes = `  
  type Query {  
    items: [ContentItem],  
    itemsByType(type: String!, limit: Int, depth: Int, order: String): [ContentItem]  
  }  
`;

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js)_.)_

And right after the definition, we can create a resolver for the headless CMS API:

const deliveryClient = new DeliveryClient(deliveryConfig);  
const resolvers = {  
  ...  
  Query: {  
    items: async () => {  
      const response = await deliveryClient.items()  
        .getPromise();  
      return response.items;  
    },  
    itemsByType: async (_, { type, limit, depth, order }) => {  
      const query = deliveryClient.items()  
        .type(type);  
      limit && query.limitParameter(limit);  
      depth && query.depthParameter(depth);  
      order && query.orderParameter(order);  
      const response = await query.getPromise();  
      return response.items;  
    }  
  },  
};

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js)_.)_

Did you notice that the queries always return generic type `ContentItem` even though there are more specific types like `FactAboutUsContentType` that inherit `ContentItem` defined? If you did, great job! Defining a specific query for every single type would be inefficient (there would be so many of them). Therefore both our queries return `ContentItem` data. But how do we ensure the right models are returned at runtime?

Every content item that comes from the headless CMS contains information about its type. You can see the string property `Type` in the definition of `SystemInfo` data model above.

{  
  "system": {  
    "type": "fact_about_us"  
    ...  
  }  
...  
}

Now we know that the content item is of type `fact_about_us` which corresponds to generated data model `FactAboutUsContentType`. Therefore we need to translate the type name to pascal case and ensure that GraphQL uses the right data model. We can ensure this using a special resolver for the generic data model:

...  
const resolvers = {  
  ContentItem: {  
    __resolveType(item, _context, _info) {  
    // fact_about_us -> FactAboutUs  
    const type = convertSnakeCaseToPascalCase(item);  
    // FactAboutUs -> FactAboutUsContentType  
    return type + 'ContentType';  
  }  
},  
...

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js)_.)_

And add a simple function to translate the type name to the data model name:

...  
// fact_about_us -> FactAboutUs  
const convertSnakeCaseToPascalCase = (item) => {  
  return item.system.type  
    .split('_')  
    .map((str) => str.slice(0, 1).toUpperCase() + str.slice(1, str.length))  
    .join('');  
  }  
...

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js)_.)_

You see that for the implementation of the resolver you need to know the target service API, or in this case the specifics of the SDK. The developer working on the front-end only needs to know the GraphQL schema regardless of the services you use.

# Putting It All Together

To bring our data models, queries and resolvers to life, we need to create the Apollo server instance in the main `app.js` file and connect it with Express and our GraphQL schema definitions:

const { TYPE_DEFINITION } = require('./graphQL/types');  
const { queryTypes, resolvers } = require('./graphQL/queries');  
const app = express();  
const apolloServer = new ApolloServer({  
  introspection: true,  
  playground: true,  
  typeDefs: [  
    TYPE_DEFINITION,  
    queryTypes  
  ],  
  resolvers  
});  
apolloServer.applyMiddleware({  
  app,  
  path: graphQLPath  
});

_(See the whole file on_ [_GitHub_](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/app.js)_.)_

In this code, we are telling Apollo which schema to use. The definitions are provided in the `typeDefs` array and correspond to previously created queries and resolvers.

The rest of the code in `app.js` (omitted here, but you may take a look at the [whole file on GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/app.js)) is related to Pug templating and routing engine. Pug enables building pages and routes in MVC structure, so it’s easy and straightforward. Take a look at the `routes/index.js` file ([file on GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/routes/index.js)) that contains the definition of the only route in the boilerplate project:

...  
router.get('/', async function (_req, res, _next) {  
  const result = await apolloClient.query({  
    query: gql`  
    {  
      itemsByType(type: "article", limit: 3, depth: 0, order: "elements.post_date") {  
        ... on ArticleContentType {  
          title {  
            value  
          }  
          summary {  
            value  
          }  
          teaser_image {  
            assets {  
              name  
              url  
            }  
          }  
        }  
      }  
    }`  
  });  
  res.render('index', {  
    articles: result.data.itemsByType,  
    ...  
  });  
});module.exports = router;

Yes! Finally, a GraphQL query. You see it requests all articles ordered by `post_date` and specifies which data fields should be provided in the response (`title`, `summary`, `teaser_image`).

Note here that in the query we need to specify which data model we are expecting because not all children of `ContentItem` must contain requested fields (for example `summary` or `teaser_image`). By `… on ArticleContentType` we are basically creating a `switch` case that will return defined fields (`title`, `summary` and `teaser_image`) if the returned content item is of type `ArticleContentType`.

The Apollo Client sends this request to the Apollo Server which forwards it to the Kentico Cloud resolver. The resolver translates the GraphQL query into the REST API. The content takes the same way back to Pug which renders the page according to template in `views/index.pug`.

How does it all work together? Take a look at the [live demo](http://bit.ly/2GGHIB5).

# Spare Some Time for a Beer

All the tools I’ve used and shown you are easy to put together, but why reinvent the wheel? When you want to start implementing a website using Apollo and React or any other JavaScript framework, remember this boilerplate to save yourself some time and effort. If you find anything missing or wish to enhance it, feel free to [raise an issue](http://bit.ly/2ByzwiJ) or [add it directly](http://bit.ly/2TGTmPW) to the code base.

Do you have experience using Apollo and GraphQL to separate concerns? Would you recommend it to others? Let me know in comments.

