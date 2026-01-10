---
title: Comment utiliser GraphQL avec Apollo sur votre site web
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
seo_title: Comment utiliser GraphQL avec Apollo sur votre site web
seo_desc: 'By Ondrej Polesny

  In my previous article, I explained why it makes sense to decouple the front-end
  part of a website from its back-end services. I introduced GraphQL, Apollo and other
  tools that enable such abstraction and make maintenance of product...'
---

Par Ondrej Polesny

Dans mon [article précédent](http://bit.ly/2TW60L6), j'ai expliqué pourquoi il est judicieux de découpler la partie front-end d'un site web de ses services back-end. J'ai présenté GraphQL, Apollo et d'autres outils qui permettent une telle abstraction et rendent la maintenance des sites web de production une expérience agréable.

Dans cet article, je vais vous montrer un modèle de base qui a déjà tous ces outils configurés et vous fait gagner beaucoup de temps lorsque vous commencez le développement.

[Consultez la démonstration en direct du modèle de base](http://bit.ly/2GGHIB5)

# Modèle de base pour accélérer le démarrage

Commençons par les outils que j'ai utilisés :

* Node.js — environnement d'exécution
* Express — framework d'application web
* Apollo server — service middleware avec support GraphQL
* Apollo client — client GraphQL
* Kentico Cloud tools — CMS headless
* Pug — moteur de template

# Code du schéma et des résolveurs

La première étape pour construire le site est de créer ou générer un schéma. J'ai déjà mentionné dans l'article précédent que j'utilise la [plateforme Content-as-a-Service Kentico Cloud](http://bit.ly/2QzUALM) pour le stockage de contenu. Le contenu qui y est stocké est déjà structuré dans des structures de modèle définies. Par conséquent, je peux rapidement générer le schéma en utilisant le [générateur de schéma](http://bit.ly/2SqEAju) :

kc-generate-gql-schema — projectId {projectID} — createModule

Mais il est également possible de définir tous les modèles manuellement dans la syntaxe suivante.

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

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/types.js).)_

Le générateur de modèle liste tous les types système, y compris les liens, les textes, les champs datetime, les images et autres (`SystemInfo` ci-dessus), suivis des modèles de données de chacun des modèles de contenu personnalisés (`FactAboutUsContentType`). Nous devrons utiliser la définition de type comme un module, d'où le dernier argument `createModule`.

L'étape suivante consiste à créer des requêtes et des résolveurs GraphQL. Comme l'API de contenu est en lecture seule, les requêtes sont assez simples et limitées à la récupération de tous les éléments ou d'éléments groupés par type :

const queryTypes = `  
  type Query {  
    items: [ContentItem],  
    itemsByType(type: String!, limit: Int, depth: Int, order: String): [ContentItem]  
  }  
`;

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js).)_

Et juste après la définition, nous pouvons créer un résolveur pour l'API du CMS headless :

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

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js).)_

Avez-vous remarqué que les requêtes renvoient toujours le type générique `ContentItem` même s'il existe des types plus spécifiques comme `FactAboutUsContentType` qui héritent de `ContentItem` défini ? Si c'est le cas, excellent travail ! Définir une requête spécifique pour chaque type serait inefficace (il y en aurait tellement). Par conséquent, nos deux requêtes renvoient des données `ContentItem`. Mais comment garantir que les bons modèles sont renvoyés à l'exécution ?

Chaque élément de contenu provenant du CMS headless contient des informations sur son type. Vous pouvez voir la propriété de chaîne `Type` dans la définition du modèle de données `SystemInfo` ci-dessus.

{  
  "system": {  
    "type": "fact_about_us"  
    ...  
  }  
...  
}

Maintenant, nous savons que l'élément de contenu est de type `fact_about_us` qui correspond au modèle de données généré `FactAboutUsContentType`. Par conséquent, nous devons traduire le nom du type en casse Pascal et nous assurer que GraphQL utilise le bon modèle de données. Nous pouvons garantir cela en utilisant un résolveur spécial pour le modèle de données générique :

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

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js).)_

Et ajouter une fonction simple pour traduire le nom du type en nom du modèle de données :

...  
// fact_about_us -> FactAboutUs  
const convertSnakeCaseToPascalCase = (item) => {  
  return item.system.type  
    .split('_')  
    .map((str) => str.slice(0, 1).toUpperCase() + str.slice(1, str.length))  
    .join('');  
  }  
...

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/graphQL/queries.js).)_

Vous voyez que pour l'implémentation du résolveur, vous devez connaître l'API du service cible, ou dans ce cas, les spécificités du SDK. Le développeur travaillant sur le front-end n'a besoin de connaître que le schéma GraphQL, indépendamment des services que vous utilisez.

# Mettre le tout ensemble

Pour donner vie à nos modèles de données, requêtes et résolveurs, nous devons créer l'instance du serveur Apollo dans le fichier principal `app.js` et la connecter avec Express et nos définitions de schéma GraphQL :

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

_(Voir le fichier complet sur [GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/app.js).)_

Dans ce code, nous indiquons à Apollo quel schéma utiliser. Les définitions sont fournies dans le tableau `typeDefs` et correspondent aux requêtes et résolveurs précédemment créés.

Le reste du code dans `app.js` (omis ici, mais vous pouvez consulter le [fichier complet sur GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/master/app.js)) est lié au moteur de templating et de routage Pug. Pug permet de construire des pages et des routes dans une structure MVC, ce qui est facile et direct. Consultez le fichier `routes/index.js` ([fichier sur GitHub](https://github.com/Kentico/cloud-boilerplate-express-apollo/blob/routes/index.js)) qui contient la définition de la seule route dans le projet de modèle de base :

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

Oui ! Enfin, une requête GraphQL. Vous voyez qu'elle demande tous les articles triés par `post_date` et spécifie quels champs de données doivent être fournis dans la réponse (`title`, `summary`, `teaser_image`).

Notez ici que dans la requête, nous devons spécifier quel modèle de données nous attendons car tous les enfants de `ContentItem` ne contiennent pas nécessairement les champs demandés (par exemple `summary` ou `teaser_image`). En utilisant `... on ArticleContentType`, nous créons essentiellement un cas `switch` qui retournera les champs définis (`title`, `summary` et `teaser_image`) si l'élément de contenu retourné est de type `ArticleContentType`.

Le client Apollo envoie cette requête au serveur Apollo qui la transmet au résolveur Kentico Cloud. Le résolveur traduit la requête GraphQL en API REST. Le contenu prend le même chemin de retour vers Pug qui rend la page selon le template dans `views/index.pug`.

Comment tout cela fonctionne-t-il ensemble ? Consultez la [démonstration en direct](http://bit.ly/2GGHIB5).

# Prenez un peu de temps pour une bière

Tous les outils que j'ai utilisés et montrés sont faciles à assembler, mais pourquoi réinventer la roue ? Lorsque vous souhaitez commencer à implémenter un site web en utilisant Apollo et React ou tout autre framework JavaScript, souvenez-vous de ce modèle de base pour vous faire gagner du temps et des efforts. Si vous trouvez quelque chose de manquant ou souhaitez l'améliorer, n'hésitez pas à [signaler un problème](http://bit.ly/2ByzwiJ) ou à [l'ajouter directement](http://bit.ly/2TGTmPW) à la base de code.

Avez-vous de l'expérience dans l'utilisation d'Apollo et de GraphQL pour séparer les préoccupations ? Le recommanderiez-vous aux autres ? Faites-le moi savoir dans les commentaires.