---
title: How to use Apollo’s brand new Query components to manage local state
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2018-06-04T07:52:49.000Z'
originalURL: https://freecodecamp.org/news/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CMxI-q0DAMtcF-VGs10G0Q.jpeg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Note: This article deals with utilizing Apollo’s brand new Query and Mutation
  components, instead of the HOCs. For those that have read the original article here,
  be aware that the two articles are very similar.

  Introduction

  One of Web Development’s ...'
---

Note: This article deals with utilizing Apollo’s brand new Query and Mutation components, instead of the HOCs. For those that have read the original article [here](https://itnext.io/managing-local-state-with-apollo-client-3be522258645), be aware that the two articles are very similar.

### Introduction

One of Web Development’s biggest strengths — and weaknesses — is its approach to modularity. A key programming mantra is to choose something (a function, a package) to do a single job and to do it well. The downside to this approach is that a single project can involve juggling dozens of separate technologies and concepts, each focusing on something specific.

So choosing Apollo Client to handle my local state as well as my remote data seems like a no brainer. Why deal with Redux’s boilerplate and idioms when I’ve already got Apollo/GraphQL set up to get data from my backend?

While this article is going to deal with setting up Apollo to handle local state, it’s not going to be an introduction to the tech. (This legit [howtographql](https://www.howtographql.com/) tutorial is a good start for that).

Note: The finished repo can be found [here](https://github.com/andrico1234/apollo-local-state-starter). You can pore through the code if you get stuck or feel confused.

### Getting set up

We’ll start by cloning the corresponding repo from [here](https://github.com/andrico1234/apollo-state-blog-repo). This repo contains a simple react website, with a sidebar, header, and a body. It’s pretty static in nature, no dynamic content (…yet). By the end of this tutorial, we’ll have Apollo managing the state of the website. Clicking an item in the sidebar will change the state of the website, which in turn updates the header to display the new data.

If you check `package.json` you’ll see that we’ve only got the basics, plus some additional packages pertaining to our parcel setup.

After cloning the repo, run your standard commands in your command line interface.

```
> yarn
> yarn dev
```

To install all of your packages and to whip up a local server, go to localhost:1234 and you’ll hopefully see the demo website in all of its glory. It’s static right now, so clicking around won’t do a thing.

What we want to do first and foremost is to get Apollo in our project, so install these packages. `apollo-client` lets us configure our instance of Apollo, and `react-apollo` is the driver that allows us to integrate it into our React application. Due to an issue with parcel (I think) we’ll also need to install `graphql`.

```
> yarn add apollo-client react-apollo graphql
```

Create a new directory `src/apollo`, crack open an `index.js` file, and add the following:

```js
import ApolloClient from ‘apollo-client’;
export const client = new ApolloClient({});
```

This initializes our Apollo Client, which we will then use to wrap our React application by adding the following inside of our `src/index.js` file.

```js
import { ApolloProvider } from ‘react-apollo’;
import { client } from ‘./apollo’;

const WrappedApp = (
  <ApolloProvider client={client} >
    <App />
  </ApolloProvider>
);

ReactDOM.render(WrappedApp, document.getElementById(‘root’));
// Don’t be a sap. Wrap your app.
```

We now have Apollo ready to use in our app. Everything builds when we restart our dev server, but we get an error when we try and access it in the browser. The console will tell us that we need to specify the link and cache properties for our Apollo client, so let’s do that.

```
> yarn add apollo-link apollo-cache-inmemory apollo-link-state
```

The previous line adds the new Apollo dependencies to our application while the following code resolves the console errors we were getting. So go back to `apollo/index.js` and update it so the file looks like this:

```js
import ApolloClient from ‘apollo-client’;
import { InMemoryCache } from ‘apollo-cache-inmemory’;
import { ApolloLink } from ‘apollo-link’;
import { withClientState } from ‘apollo-link-state’;

const cache = new InMemoryCache();
const stateLink = withClientState({
  cache
});

export const client = new ApolloClient({
  cache,
  link: ApolloLink.from([
    stateLink,
  ]),
})
```

Let’s create an instance of our cache. The cache is Apollo’s normalized data store that stores the results of the query in a flattened data structure. We will read from the cache when we make our GraphQL query, and we’ll write to the cache when we make our mutation resolver.

You can see we’ve also added `link` to our client object. The `ApolloLink.from()`method lets us modularly configure how our queries are sent over HTTP. We can use this to handle errors and authorization, and to provide access to our backend. We’re not going to be doing any of this in the tutorial, but we will set up our client state here. So we create `const stateLink` above and pass in our cache. We’ll add our default state and resolvers here later.

Going back to the browser, you’ll see our lovely static site displaying in all of its magnificence. Let’s add some default state to our project and fire off our first query.

Inside of the Apollo directory, create a new directory called `defaults` and add an `index.js` inside of it. The file will contain the following:

```js
export default {
  apolloClientDemo: {
    __typename: ‘ApolloClientDemo’,
    currentPageName: ‘Apollo Demo’,
  }
}
```

We create an object which acts as the default state of our site. apolloClientDemo is the name of the data structure we want to access when we make our queries. The `__typename` is the mandatory identifier that our cache uses, and the currentPageName is the specific item of data that our header will use to — you guessed it — display the current page name.

We’ll need to add this to our `apollo/index.js` file:

```js
import defaults from ‘./defaults’;

const stateLink = withClientState({
  cache,
  defaults,
});
```

Let’s clear this up a little bit. `import` and `default` are both keywords associated with importing modules, but coincidentally the name of the object we’re exporting from `./defaults` is also called `defaults` (so don’t be thinking that I’m using `import/export` wrong). Treat this import line as if it was just any regular ol’ named import.

With that out of the way, let’s go make a query!

### How to make a query

Add the following package to your project:

```
> yarn add graphql-tag
```

and create a new directory `src/graphql`. In there, create two new files: `index.js` and `getPageName.js`. The GraphQL directory will house all the queries and mutations. We’ll create our query in `getPageName.js` by writing the following:

```js
import gql from ‘graphql-tag’;

export const getPageNameQuery = gql`
  query {
    apolloClientDemo @client {
      currentPageName
    }
  }
`;

export const getPageNameOptions = ({
  props: ({ data: { apolloClientDemo } }) => ({
    apolloClientDemo
  })
});
```

So we’re exporting two variables, the query and the options. If you’ve used GraphQL before, then the query will look familiar. We’re querying against the apolloClientDemo data structure, retrieving back nothing more than the currentPageName. You’ll notice that we’ve added the `@client` directive to our query. This tells Apollo to query our local state instead of sending the request to the backend.

Below you’ll see that we’re exporting some options. This is simply defining how we want the data to look when we map the results to the props. We’re destructuring the GraphQL response and sending it to our view so it looks like this:

```js
props: {
  currentPageName: ‘Apollo Demo’,
}
// and not this
props: {
  data: {
    apolloClientDemo: {
      currentPageName: ‘Apollo Demo’,
    }
  }
}
```

Go to the `graphql/index.js` file and export the query as follows:

```js
export { getPageNameQuery, getPageNameOptions } from ‘./getPageName’;

```

Again, while this isn’t completely necessary for a small demo/project, this file is handy should your application grow larger. Having your queries exported from a single centralized location keeps everything organized and scalable.

Add to your Header.js:

```js
import React from 'react';
import { Query } from 'react-apollo';
import { getPageNameQuery } from '../graphql';

const Header = () => (
    <Query query={getPageNameQuery}>
        {({ loading, error, data }) => {
            if (error) return <h1>Error...</h1>;
            if (loading || !data) return <h1>Loading...</h1>;

            return <h1>{data.apolloClientDemo.currentPageName}</h1>
        }}
    </Query>
);

export default Header;
```

This is our first use of Apollo’s new Query Component, which was added in 2.1. We import `Query` from `react-apollo` and use it to wrap the rest of our component. We then pass the getPageNameQuery as a value in the query prop. When our component renders, it fires off the query and gives the rest of the component access to the data, which we destructure to gain access to loading, errors, and data.

The Query Component uses the render props pattern to give the rest of our component access to the information returned from the query. If you’ve used the React Context API in 16.3, then you’ve seen this syntax before. Otherwise it’s worth checking out the official React docs [here](https://reactjs.org/docs/render-props.html), as the Render Props pattern is becoming increasingly popular.

In our component, we do a few checks to see if there were any errors when firing the query or if we’re still waiting for data to be returned. If either of these scenarios are true, we return the corresponding HTML. If the query was fired correctly, the component will dynamically display the title of the current page. As we haven’t added our mutation yet, it will only display the default value. But you can change whatever’s in the default state and the website will reflect that.

Now all that’s left to do is mutate the data in the Apollo cache by clicking on the sidebar item.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OHpQBcsRCsX5Wk_b.)
_A refreshing image to break up the text. [Jeff Sheldon](https://unsplash.com/@ugmonk?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Mutations

Things get a little more complicated when dealing with mutations. We no longer just retrieve data from the Apollo store, but we update it too. The architecture of mutation is as follows:

**> U**ser clicks sidebar item

**> Se**nds variable to mutation

**> Fi**res mutation with variable

**> G**ets sent to the instance of Apollo

**> Fi**nds corresponding resolver

**> Appl**ies logic to the Apollo store

**> Se**nds data back to header

If that’s difficult to remember, then use this handy mnemonic created using a mnemonic generator: Urban Senile Fauns Groped Faithless Aslan Solemnly. (easy…)

Start by creating a file `graphql/updatePageName.js`.

```js
import gql from ‘graphql-tag’;

export const updatePageName = gql`
  mutation updatePageName($name: String!) {
    updatePageName(name: $name) @client {
      currentPageName
    }
  }
`;
```

and export it just like we did with the query.

```js
export { updatePageNameMutation } from ‘./updatePageName’;

```

You’ll notice a few differences regarding the mutation. First off we’ve changed the keyword from query to mutation. This lets GraphQL know the type of action we’re performing. We’re also defining the name of the query and adding types to the variables we’re passing in. Inside here we’re specifying the name of the resolver we’ll be using to carry out the changes. We’re also passing through the variable and adding the `@client` directive.

Unlike the query, we can’t just add the mutation to our view and expect anything to happen. We’ll have to go back to our Apollo directory and add our resolvers. So go ahead and create a new directory `apollo/resolvers`, and files `index.js` and `updatePageName.js`. Inside of `updatePageName.js`add the following:

```js
import gql from ‘graphql-tag’;

export default (_, { name }, { cache }) => {
  const query = gql`
    query GetPageName {
      apolloClientDemo @client {
        currentPageName
      }
    }
  `;
  
  const previousState = cache.readQuery({ query });
  
  const data = {
    apolloClientDemo: {
      …previousState.apolloClientDemo,
      currentPageName: name,
    },
  };
  
  cache.writeQuery({
    query,
    data,
  });
  
  return null;
};
```

There are a lot of interesting things going on in this file. Fortunately, it’s all very logical and doesn’t add many new concepts to what we’ve seen before.

So by default, when a resolver gets called, Apollo passes in all of the variables and the cache. The first argument is a simple ‘_’ because we don’t need to use it. The second argument is the variables object, and the final argument is the cache.

Before we can make changes to the Apollo store, we’ll need to retrieve it. So we make a simple request to get the current content from the store and assign it to previousState. Inside of the data variable, we create a new object with the new information we want to add to the store, which we then write to. You can see that we’ve spread the previous state inside of this object. This is so that only the data we explicitly want to change gets updated. Everything else remains as it is. This prevents Apollo from needlessly updating components whose data hasn’t changed.

Note: while this isn’t completely necessary for this example, it’s super useful when queries and mutations handle larger amounts of data, so I’ve kept it in for the sake of scalability.

Meanwhile in the `resolvers/index.js` file…

```js
import updatePageName from ‘updatePageName’;

export default {
  Mutation: {
    updatePageName,
  }
};
```

This is the shape of object that Apollo expects when we pass in our resolvers in to stateLink back in `apollo/index.js`:

```js
import resolvers from ‘./resolvers’;

const stateLink from = withClientState({
  cache,
  defaults,
  resolvers,
});
```

All that’s left to do is add the mutation to our sidebar component.

```js
// previous imports
import { Mutation } from ‘react-apollo’;
import { updatePageNameMutation } from ‘../graphql’;

class Sidebar extends React.Component {
  render() {
    return (
      <Mutation mutation={updatePageNameMutation}>
        {updatePageName => (
          // outer div elements
          <li className=“sidebar-item” onClick={() => updatePageName({ variables: { name: ‘React’} })}>React</li>
          // other list items and outer div elements
        )}
      </Mutation>
    );
  }
}

export default Sidebar;
```

Like our resolver file, there’s a lot going on in this file — but it’s new. We import our `Mutation` component from `react-apollo`, wrap it around our component, and pass the `updatePageNameMutation` inside of the `mutation` prop.

The component now has access to the `updatePageName` method which fires the mutation whenever it’s called. We do this by adding the method as a handler to the `<`li>’s onClick property. The method expects to receive on object containing the variables as a parameter, so pass in the name you want to update the header to. If everything works, you should be able to run your dev server and click the sidebar items, which should then change our header.

### Wrapping up

Hooray! Hopefully everything worked out. If you got stuck, then check out the repo [here](https://github.com/andrico1234/apollo-local-state-starter). It contains all of the finished code. If you’re thinking of using local state management in your next React app, then you can fork this repo and continue from there. If you’re interested in having this article/topic spoken about at a meetup or conference, then send a message my way!

There’s a lot more I wanted to cover in this tutorial, such as async resolvers (think Redux thunk), type checking/creating a schema, and a mutation update. So who knows… maybe I’ll drop another article sometime soon.

I really hope that this tutorial was useful for you. I’d like to shout out [Sara Vieira’s youtube tutorial too](https://www.youtube.com/watch?v=2RvRcnD8wHY), as it helped me get my head around Apollo Client. If I haven’t done my job well enough by leaving you scratching your head, then follow the link. And finally, feel free to hit me up on social media, I’m a big music and tech fan so talk geek to me.

#### Thanks for reading!

If you’re interested in hosting me at a conference, meetup or as a speaking guest for any engagement then you can DM me on [twitter](https://twitter.com/andricokaroulla?lang=en)!

#### You can check out my other articles below:

[_How to use Apollo’s brand new Query components to manage local state_](https://medium.com/@andricokaroulla/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7)

[_Add a touch of Suspense to your web app with React.lazy()_](http://Add a touch of Suspense to your web app with React.lazy())

[_No need to wait for the holidays, start Decorating now_](https://codeburst.io/no-need-to-wait-for-the-holidays-start-decorating-now-67b9dabd60d7)

[_Managing local state with Apollo and Higher Order Components_](https://itnext.io/managing-local-state-with-apollo-client-3be522258645)

[_The React Conference drinking game_](https://medium.com/@andricokaroulla/the-react-conference-drinking-game-7a996bfbef3)

[_Develop and Deploy your own React monorepo app in under 2 hours, using Lerna, Travis and Now_](https://codeburst.io/develop-and-deploy-your-own-react-monorepo-app-in-under-2-hours-using-lerna-travis-and-now-2b140d647238)

