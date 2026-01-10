---
title: 'GraphQL déclaratif : écrivez moins de code et accomplissez plus avec graphql-tools'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-21T05:50:31.000Z'
originalURL: https://freecodecamp.org/news/declarative-graphql-with-graphql-tools-cd1645f94fc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-AdNar_hX9-ougYftbv3qg.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'GraphQL déclaratif : écrivez moins de code et accomplissez plus avec graphql-tools'
seo_desc: 'By Jeff M Lowery

  I’ve been working with GraphQL for a few months now, but only recently began using
  Apollo’s graphql-tools library. After learning a few idioms, I am able to mock up
  a functional API quickly. This is largely due to its low-code, decla...'
---

Par Jeff M Lowery

Je travaille avec GraphQL depuis quelques mois, mais j'ai seulement commencé à utiliser récemment la bibliothèque graphql-tools d'Apollo. Après avoir appris quelques idiomes, je suis en mesure de créer rapidement une API fonctionnelle. Cela est largement dû à son approche déclarative et low-code pour les définitions de types.

### Commencer avec leur exemple

Apollo dispose d'un site web interactif [LaunchPad](https://launchpad.graphql.com/), similaire à ceux couverts dans ma [série Swagger](https://medium.com/@jefflowery/staggered-by-swagger-82acf85f3c3b). Il y a plusieurs exemples de schémas que vous pouvez utiliser, et pour cet article, j'utiliserai leur [schéma Posts et Auteurs](https://launchpad.graphql.com/1jzxrj179). Vous pouvez télécharger ou forker le code.

Je vais réorganiser les dossiers du projet. Pour ce post, je vais le télécharger et le stocker sur Github, afin de pouvoir créer des branches et modifier le code à chaque étape. En cours de route, je lierai les branches à ce post.

#### Les bases

* **déclarer les types de schéma**

Dans le Launchpad, vous verrez un modèle littéral `typeDefs` :

```js
const typeDefs = `
  type Author {
    id: Int!
    firstName: String
    lastName: String
    posts: [Post] # la liste des Posts par cet auteur
  }

type Post {
    id: Int!
    title: String
    author: Author
    votes: Int
  }

# le schéma permet la requête suivante :
  type Query {
    posts: [Post]
    author(id: Int!): Author
  }

# ce schéma permet la mutation suivante :
  type Mutation {
    upvotePost (
      postId: Int!
    ): Post
  }
`;
```

Il y a deux **entités** définies, `Author` et `Post`. En outre, il y a deux types "magiques" : `Query` et `Mutation`. Le type Query définit les `accesseurs` racine. Dans ce cas, il y a un accesseur pour récupérer tous les `Posts`, et un autre pour récupérer un seul `Author` par `ID`.

Notez qu'il n'y a aucun moyen de demander directement une liste d'auteurs ou un seul post. Il est possible d'ajouter de telles requêtes plus tard.

* **déclarer les résolveurs**

Les résolveurs fournissent la logique nécessaire pour supporter le schéma. Ils sont écrits sous forme d'un objet JavaScript avec des clés qui correspondent aux types définis dans le schéma. Le `resolver` montré ci-dessous fonctionne avec des données statiques, que je vais couvrir dans un instant.

```js
const resolvers = {
  Query: {
    posts: () => posts,
    author: (_, { id }) => find(authors, { id: id }),
  },
  Mutation: {
    upvotePost: (_, { postId }) => {
      const post = find(posts, { id: postId });
      if (!post) {
        throw new Error(`Couldn't find post with id ${postId}`);
      }
      post.votes += 1;
      return post;
    },
  },
  Author: {
    posts: (author) => filter(posts, { authorId: author.id }),
  },
  Post: {
    author: (post) => find(authors, { id: post.authorId }),
  },
};
```

Pour lier `schema` et `resolver` ensemble, nous allons créer une instance de schéma exécutable :

```js
export const schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});
```

* **la source de données**

Pour cet exemple simple, les données proviennent de deux tableaux d'objets définis comme constantes : `**authors**` et `**posts**` :

```js
const authors = [
  { id: 1, firstName: 'Tom', lastName: 'Coleman' },
  { id: 2, firstName: 'Sashko', lastName: 'Stubailo' },
  { id: 3, firstName: 'Mikhail', lastName: 'Novikov' },
];

const posts = [
  { id: 1, authorId: 1, title: 'Introduction to GraphQL', votes: 2 },
  { id: 2, authorId: 2, title: 'Welcome to Meteor', votes: 3 },
  { id: 3, authorId: 2, title: 'Advanced GraphQL', votes: 1 },
  { id: 4, authorId: 3, title: 'Launchpad is Cool', votes: 7 },
];
```

* **le serveur**

Vous pouvez servir le schéma exécutable via **graphql_express**, **apollo_graphql_express**, ou **graphql-server-express**. Nous voyons cela dans cet exemple.

Les parties importantes sont :

```js
import { graphqlExpress, graphiqlExpress } from 'graphql-server-express';
import { schema, rootValue, context } from './schema';

const PORT = 3000;
const server = express();

server.use('/graphql', bodyParser.json(), graphqlExpress(request => ({
  schema,
  rootValue,
  context: context(request.headers, process.env),
})));

server.use('/graphiql', graphiqlExpress({
  endpointURL: '/graphql',
}));

server.listen(PORT, () => {
  console.log(`GraphQL Server is now running on 
http://localhost:${PORT}/graphql`);
  console.log(`View GraphiQL at 
http://localhost:${PORT}/graphiql`);
});
```

Notez qu'il y a deux morceaux de middleware GraphQL utilisés :

* **graphqlExpress**  
le serveur GraphQL qui gère les requêtes et les réponses
* **graphiqlExpress**  
le service web interactif GraphQL qui permet des requêtes interactives via une interface HTML

### Réorganisation

> Pour les grandes applications, nous suggérons de diviser votre code de serveur GraphQL en 4 composants : Schema, Resolvers, Models et Connectors, chacun gérant une partie spécifique du travail. ([http://dev.apollodata.com/tools/graphql-tools/](http://dev.apollodata.com/tools/graphql-tools/))

Placer chaque type de composant dans son propre fichier a du sens. Je vais encore mieux faire et placer chaque ensemble de composants dans son propre dossier de "domaine".

#### Pourquoi des domaines ?

Les domaines sont un moyen pratique de diviser un grand système en zones d'opération. Au sein de chaque domaine, il peut y avoir des sous-domaines. En général, les sous-domaines ont un contexte délimité. Au sein d'un contexte délimité, les noms d'entités, les propriétés et les processus ont une signification précise.

Je trouve que les contextes délimités sont utiles lors de l'analyse, surtout lorsque je parle à des experts du domaine.

Le problème est que les types GraphQL occupent un seul espace de noms, donc des conflits de nommage peuvent exister. Plus sur cela plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1nxilNJ_g7fiIOf2T_o_9w.png)

J'appellerai ce domaine **authorposts**, et je mettrai les composants associés dans le dossier `authorposts`. Dans celui-ci, je vais créer un fichier pour chaque `datasource`, `resolvers` et schema. Ajoutons également un fichier `index.js` pour simplifier l'importation. Les fichiers de schéma et de serveur d'origine resteront dans le dossier racine, mais le code de `schema.js` sera squelettique. Les méthodes `**find**` et `**filter**` importées de **lodash** seront remplacées par des méthodes natives ES6 synonymes. Le code source résultant est [ici](https://github.com/JeffML/graphql_authors/tree/reorg).

Le fichier de schéma principal est devenu plus simple. Il fournit une structure squelettique pour une extension supplémentaire par les schémas dans nos domaines.

```js
import {
    makeExecutableSchema
} from 'graphql-tools';

import {
    schema as authorpostsSchema,
    resolvers as authorpostsResolvers
} from './authorposts';

const baseSchema = [
    `
    type Query {
        domain: String
    }
    type Mutation {
        domain: String
    }
    schema {
        query: Query,
        mutation: Mutation
    }`
]

// Mettre le schéma ensemble dans un tableau de chaînes de schéma et une carte de résolveurs, comme makeExecutableSchema l'attend
const schema = [...baseSchema, ...authorpostsSchema]

const options = {
    typeDefs: schema,
    resolvers: {...authorPostResolvers}
}

const executableSchema = makeExecutableSchema(options);

export default executableSchema;
```

Un schéma de `domain` est importé aux lignes 7-8, et le schéma `base` aux lignes 11-23. Vous noterez qu'il y a une propriété **domain**. Cela est arbitraire mais GraphQL, ou graphql-tools, insiste pour qu'une propriété soit définie.

Le schéma complet est construit à la ligne 26, et une instance `executableSchema` est créée étant donné le `schema` et les `resolvers` définis jusqu'à présent aux lignes 28-33. C'est ce qui est importé par le code **server.js**, qui est largement inchangé par rapport à l'original.

Il y a une astuce pour diviser un schéma de cette manière. Jetons un coup d'œil :

```js
import {
    authors,
    posts
} from './dataSource';

const rootResolvers = {
    Query: {
        posts: () => posts,
        author: (_, {
            id
        }) => authors.find(a => a.id === id)
    },
    Mutation: {
        upvotePost: (_, {
            postId
        }) => {
            const post = posts.find(p => p.id === postId);
            if (!post) {
                throw new Error(`Couldn't find post with id ${postId}`);
            }
            post.votes += 1;
            return post;
        }
    },
    Author: {
        posts: (author) => posts.filter(p => p.authorId === author.id)
    },
    Post: {
        author: (post) => authors.find(a => a.id === post.authorId)
    }
};


export default rootResolvers;
```

```js
const typeDefs = [
    `
  type Author {
    id: Int!
    firstName: String
    lastName: String
    posts: [Post] # la liste des Posts par cet auteur
  }
  type Post {
    id: Int!
    title: String
    author: Author
    votes: Int
  }
  # le schéma permet la requête suivante :
  extend type Query {
    posts: [Post]
    author(id: Int!): Author
  }
  # ce schéma permet la mutation suivante :
  extend type Mutation {
    upvotePost (
      postId: Int!
    ): Post
  }
`
];


export default typeDefs;
```

La première liste, `authorpostResolvers.js`, est principalement un copier-coller du code source `schema.js` original de l'exemple d'Apollo. Pourtant, dans le code `authorpostSchema.js`, nous **étendons** les définitions `Query` et `Mutator` qui sont déclarées dans le schéma de base. Si vous n'utilisez pas le mot-clé **extend**, le constructeur de schéma exécutable se plaindra de deux définitions **Query**.

#### Continuation...

C'est un bon début pour organiser plusieurs schémas, un pour chaque domaine d'intérêt (tant que vous êtes conscient de l'espace de noms global pour les types), mais un schéma complet, même pour un seul domaine, peut devenir énorme. Heureusement, vous pouvez décomposer chaque schéma encore plus, jusqu'au [niveau de l'entité](https://github.com/JeffML/graphql_authors/tree/reorg2), si nécessaire.

Voici une structure de répertoire modifiée, et les listes des nouveaux contenus :

![Image](https://cdn-media-1.freecodecamp.org/images/1*b4rGOYcGju6U50IzxDUf9g.png)

```js
export default `
  type Author {
    id: Int!
    firstName: String
    lastName: String
    posts: [Post] # la liste des Posts par cet auteur
}`
```

```js
export default `
type Post {
  id: Int!
  title: String
  author: Author
  votes: Int
}`
```

```js
import Author from './components/author'
import Post from './components/post'

const typeDefs =
    `
  # le schéma permet la requête suivante :
  extend type Query {
    posts: [Post]
    author(id: Int!): Author
  }
  # ce schéma permet la mutation suivante :
  extend type Mutation {
    upvotePost (
      postId: Int!
    ): Post
  }
`;

export default [typeDefs, Author, Post];
```

Nous pouvons atteindre la granularité en définissant deux fichiers de composants, puis en les important dans un schéma de domaine.

Vous n'avez pas à faire un composant par fichier. Mais vous devez vous assurer que le schéma exporte ces composants avec le schéma lui-même comme montré à la ligne 20 de **schema.js**. Sinon, vous risquez de manquer une dépendance plus loin dans la chaîne d'inclusion.

#### Plusieurs schémas et résolveurs

Ajouter un nouveau schéma pour un nouveau domaine est simple. Créez un nouveau dossier de domaine et ajoutez des fichiers dataSource, resolvers, schema et index.js. Vous pouvez également ajouter un dossier de composants optionnel avec des définitions de types de composants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*57--cwAN6mBbUxUFfXkSpA.png)

```js
const myLittleTypes = [{
    id: 1,
    description: 'This is good',
}, {
    id: 2,
    description: 'This is better',
}, {
    id: 3,
    description: 'This is the best!',
}];

export {
    myLittleTypes
};
```

```js
export default `
  type MyLittleType {
    id: Int!
    description: String
}`
```

```js
import {
    myLittleTypes
} from './dataSource';

const rootResolvers = {
    Query: {
        myLittleType: (_, {
            id
        }) => myLittleTypes.find(t => t.id === id)
    },
};


export default rootResolvers;
```

```js
import MyLittleType from './components/myLittleType'

const typeDefs =
    `
  # le schéma permet la requête suivante :
  extend type Query {
    myLittleType(id: Int!): MyLittleType
  }
`;

export default [typeDefs, MyLittleType];
```

Enfin, le fichier schema.js racine doit combiner les schémas et les résolveurs des deux domaines :

```js
//...
import {
    schema as myLittleTypoSchema,
    resolvers as myLittleTypeResolvers
} from './myLittleDomain';

import {
    merge
} from 'lodash';
//...
const schema = [...baseSchema, ...authorpostsSchema, ...myLittleTypoSchema]

const options = {
    typeDefs: schema,
    resolvers: merge(authorpostsResolvers, myLittleTypeResolvers)
}
```

Notez que j'ai dû inclure `**lodash**` **merge** ici en raison du besoin d'une fusion profonde des deux imports de **resolvers**.

### Gérer les collisions de noms

Si vous travaillez sur un grand projet, vous rencontrerez des collisions de noms de types. Vous pourriez penser qu'un Account dans un domaine signifierait la même chose qu'un Account dans un autre. Pourtant, même s'ils signifient des choses plus ou moins similaires, les propriétés et les relations seront probablement différentes. Donc, techniquement, ils ne sont pas du même type.

Au moment de la rédaction de cet article, GraphQL utilise un seul espace de noms pour les types.

Comment contourner cela ? Facebook utilise apparemment une [convention de nommage](https://github.com/facebook/graphql/issues/163#issuecomment-241607229) pour leurs 10 000 types. Aussi maladroit que cela puisse sembler, cela fonctionne pour eux.

La pile Apollo graphql-tools semble détecter les doublons de noms de types. Vous devriez donc être couvert.

Il y a une discussion en cours sur [l'opportunité](https://github.com/facebook/graphql/issues/163#issuecomment-230163416) d'inclure des espaces de noms dans GraphQL. Ce n'est pas une décision simple. Je me souviens des complexités causées par l'introduction des [espaces de noms XML](https://www.w3.org/TR/REC-xml-names/) il y a 10 ans.

### Où aller à partir de là ?

Ce post ne fait qu'effleurer la surface de la manière dont on pourrait organiser un grand ensemble de schémas GraphQL. Le prochain post portera sur la simulation des résolveurs GraphQL, et sur la manière dont il est possible de mélanger des valeurs réelles et simulées dans les réponses aux requêtes.