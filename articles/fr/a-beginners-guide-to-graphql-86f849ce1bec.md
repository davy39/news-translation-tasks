---
title: Un guide du débutant pour GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T18:31:55.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-graphql-86f849ce1bec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sbPjm_cUHedMps6Kdy2F-A.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Un guide du débutant pour GraphQL
seo_desc: 'By Leonardo Maldonado

  One of the most commonly discussed terms today is the API. A lot of people don’t
  know exactly what an API is. Basically, API stands for Application Programming Interface.
  It is, as the name says, an interface with which people —...'
---

Par Leonardo Maldonado

L'un des termes les plus discutés aujourd'hui est l'API. Beaucoup de gens ne savent pas exactement ce qu'est une API. Basiquement, API signifie **Interface de Programmation d'Application**. C'est, comme son nom l'indique, une interface avec laquelle les gens — développeurs, utilisateurs, consommateurs — peuvent interagir avec des données.

Vous pouvez penser à une API comme à un barman. Vous demandez au barman une boisson, et il vous donne ce que vous vouliez. Simple. Alors, pourquoi est-ce un problème ?

Depuis le début du web moderne, construire des APIs n'a pas été aussi difficile que cela en a l'air. Mais apprendre et comprendre les APIs l'était. Les développeurs forment la majorité des personnes qui utiliseront votre API pour construire quelque chose ou simplement consommer des données. Donc votre API devrait être aussi propre et intuitive que possible. Une API bien conçue est très facile à utiliser et à apprendre. Elle est également intuitive, un bon point à garder à l'esprit lorsque vous commencez à concevoir votre API.

Nous avons utilisé REST pour construire des APIs depuis longtemps. Avec cela viennent certains problèmes. Lorsque vous construisez une API en utilisant la conception REST, vous rencontrerez des problèmes comme :

1) vous aurez beaucoup de points de terminaison

2) il sera beaucoup plus difficile pour les développeurs d'apprendre et de comprendre votre API

3) il y a sur- et sous-récupération d'informations

Pour résoudre ces problèmes, Facebook a créé GraphQL. Aujourd'hui, je pense que GraphQL est la meilleure façon de construire des APIs. Cet article vous expliquera pourquoi vous devriez commencer à l'apprendre aujourd'hui.

Dans cet article, vous allez apprendre comment fonctionne GraphQL. Je vais vous montrer comment créer une API très bien conçue, efficace et puissante en utilisant GraphQL.

Vous avez probablement déjà entendu parler de GraphQL, car beaucoup de gens et d'entreprises l'utilisent. Puisque GraphQL est open-source, sa communauté a énormément grandi.

Maintenant, il est temps pour vous de commencer à apprendre en pratique comment fonctionne GraphQL et tout sur sa magie.

### Qu'est-ce que GraphQL ?

[GraphQL](https://graphql.org) est un langage de requête open-source développé par Facebook. Il nous fournit un moyen plus efficace de concevoir, créer et consommer nos APIs. Basiquement, c'est le remplaçant de REST.

GraphQL a beaucoup de fonctionnalités, comme :

1. Vous écrivez les données que vous voulez, et vous obtenez exactement les données que vous voulez. **Plus de sur-récupération d'informations** comme nous en avions l'habitude avec REST.
2. Il nous donne un **point de terminaison unique**, plus de version 2 ou version 3 pour la même API.
3. GraphQL est **fortement typé**, et avec cela vous pouvez valider une requête dans le système de types GraphQL avant l'exécution. Cela nous aide à construire des APIs plus puissantes.

C'est une introduction basique à GraphQL — pourquoi il est si puissant et pourquoi il gagne en popularité ces jours-ci. Si vous voulez en apprendre plus, je vous recommande d'aller sur le [site web de GraphQL](https://graphql.org/) et de le vérifier.

### Pour commencer

L'objectif principal de cet article n'est pas d'apprendre à configurer un serveur GraphQL, donc nous n'allons pas approfondir cela pour l'instant. L'objectif est d'apprendre comment fonctionne GraphQL en pratique, donc nous allons utiliser un serveur GraphQL sans configuration appelé ☀️ [Graphpack](https://github.com/glennreyes/graphpack).

Pour démarrer notre projet, nous allons créer un nouveau dossier et vous pouvez le nommer comme vous le souhaitez. Je vais le nommer `graphql-server` :

Ouvrez votre terminal et tapez :

```
mkdir graphql-server
```

Maintenant, vous devriez avoir _npm_ ou _yarn_ installé sur votre machine. Si vous ne savez pas ce que c'est, _npm_ et _yarn_ sont des gestionnaires de paquets pour le langage de programmation JavaScript. Pour Node.js, le gestionnaire de paquets par défaut est _npm_.

À l'intérieur de votre dossier créé, tapez la commande suivante :

```
npm init -y
```

Ou si vous utilisez yarn :

```
yarn init
```

npm va créer un fichier `package.json` pour vous, et toutes les dépendances que vous avez installées et vos commandes seront là.

Donc maintenant, nous allons installer **la seule dépendance** que nous allons utiliser.

☀️[Graphpack](https://github.com/glennreyes/graphpack) vous permet de créer un serveur GraphQL **avec zéro configuration**. Puisque nous commençons avec GraphQL, cela va nous aider beaucoup à avancer et à en apprendre plus sans nous soucier de la configuration du serveur.

Dans votre terminal, à l'intérieur de votre dossier racine, installez-le comme ceci :

```
npm install --save-dev graphpack
```

Ou, si vous utilisez yarn, vous devriez faire comme ceci :

```
yarn add --dev graphpack
```

Après que Graphpack soit installé, allez dans nos scripts dans le fichier `package.json`, et mettez le code suivant là :

```js
"scripts": {
    "dev": "graphpack",
    "build": "graphpack build"
}
```

Nous allons créer un dossier appelé `src`, et ce sera le seul dossier dans notre serveur entier.

Créez un dossier appelé `src`, après cela, à l'intérieur de notre dossier, nous allons créer trois fichiers seulement.

À l'intérieur de notre dossier `src`, créez un fichier appelé `schema.graphql`. À l'intérieur de ce premier fichier, mettez le code suivant :

```js
type Query {
  hello: String
}
```

Dans ce fichier `schema.graphql`, nous allons avoir notre schéma GraphQL entier. Si vous ne savez pas ce que c'est, je vais expliquer plus tard — ne vous inquiétez pas.

Maintenant, à l'intérieur de notre dossier `src`, créez un deuxième fichier. Appelez-le `resolvers.js` et, à l'intérieur de ce deuxième fichier, mettez le code suivant :

```js
import { users } from "./db";

const resolvers = {
  Query: {
    hello: () => "Hello World!"
  }
};

export default resolvers;
```

Ce fichier `resolvers.js` va être le moyen par lequel nous fournissons les instructions pour transformer une opération GraphQL en données.

Et enfin, à l'intérieur de votre dossier `src`, créez un troisième fichier. Appelez ce fichier `db.js` et, à l'intérieur de ce troisième fichier, mettez le code suivant :

```js
export let users = [
  { id: 1, name: "John Doe", email: "john@gmail.com", age: 22 },
  { id: 2, name: "Jane Doe", email: "jane@gmail.com", age: 23 }
];
```

Dans ce tutoriel, nous n'utilisons pas une base de données réelle. Donc ce fichier `db.js` va simuler une base de données, juste à des fins d'apprentissage.

Maintenant, notre dossier `src` devrait ressembler à ceci :

```
src
  |--db.js
  |--resolvers.js
  |--schema.graphql
```

Maintenant, si vous exécutez la commande `npm run dev` ou, si vous utilisez yarn, `yarn dev`, vous devriez voir cette sortie dans votre terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FKJYY9qqg4PLBvziWPlhVg.png)

Vous pouvez maintenant aller sur `localhost:4000`. Cela signifie que nous sommes prêts à commencer à écrire nos premières requêtes, mutations et abonnements en GraphQL.

Vous voyez le GraphQL Playground, un IDE GraphQL puissant pour de meilleurs flux de travail de développement. Si vous voulez en apprendre plus sur GraphQL Playground, [cliquez ici](https://www.prisma.io/blog/introducing-graphql-playground-f1e0a018f05d/).

### Schéma

GraphQL a son propre type de langage qui est utilisé pour écrire des schémas. C'est une syntaxe de schéma lisible par l'homme appelée Schema Definition Language (SDL). Le SDL sera le même, peu importe la technologie que vous utilisez — vous pouvez utiliser cela avec n'importe quel langage ou framework que vous voulez.

Ce langage de schéma est très utile car il est simple de comprendre quels types votre API va avoir. Vous pouvez le comprendre juste en le regardant.

### Types

Les types sont l'une des fonctionnalités les plus importantes de GraphQL. Les types sont des objets personnalisés qui représentent à quoi votre API va ressembler. Par exemple, si vous construisez une application de médias sociaux, votre API devrait avoir des types tels que `Posts`, `Users`, `Likes`, `Groups`.

Les types ont des champs, et ces champs retournent un type spécifique de données. Par exemple, nous allons créer un type User, nous devrions avoir des champs `name`, `email`, et `age`. Les champs de type peuvent être n'importe quoi, et retournent toujours un type de données tel que Int, Float, String, Boolean, ID, une Liste de Types d'Objets, ou des Types d'Objets Personnalisés.

Donc maintenant pour écrire notre premier Type, allez dans votre fichier `schema.graphql` et remplacez le type Query qui s'y trouve par ce qui suit :

```js
type User {
  id: ID!
  name: String!
  email: String!
  age: Int
}
```

Chaque `User` va avoir un `ID`, donc nous lui avons donné un type `ID`. `User` va également avoir un `name` et un `email`, donc nous lui avons donné un type `String`, et un `age`, auquel nous avons donné un type `Int`. Pretty simple, right?

Mais, que signifient ces `!` à la fin de chaque ligne ? Le point d'exclamation signifie que les champs sont **non-nullables**, ce qui signifie que chaque champ doit retourner des données dans chaque requête. Le seul champ **nullable** que nous allons avoir dans notre type `User` sera `age`.

Dans GraphQL, vous allez traiter avec trois concepts principaux :

1. **queries** — la façon dont vous allez obtenir des données du serveur.
2. **mutations** — la façon dont vous allez modifier des données sur le serveur et obtenir des données mises à jour en retour (créer, mettre à jour, supprimer).
3. **subscriptions** — la façon dont vous allez maintenir une connexion en temps réel avec le serveur.

Je vais vous expliquer tout cela. Commençons par les Queries.

### Queries

Pour expliquer cela simplement, les queries en GraphQL sont la façon dont vous allez obtenir des données. L'une des choses les plus belles à propos des queries en GraphQL est que vous allez obtenir exactement les données que vous voulez. Ni plus, ni moins. Cela a un impact positif énorme sur notre API — plus de sur-récupération ou de sous-récupération d'informations comme nous en avions avec les APIs REST.

Nous allons créer notre premier type Query en GraphQL. Toutes nos queries vont se retrouver à l'intérieur de ce type. Donc pour commencer, nous allons dans notre `schema.graphql` et écrivons un nouveau type appelé `Query` :

```js
type Query {
  users: [User!]!
}
```

C'est très simple : la query `users` va nous retourner un tableau d'un ou plusieurs `Users`. Elle ne retournera pas null, car nous avons mis le `!`, ce qui signifie que c'est une query non-nullable. Elle devrait toujours retourner quelque chose.

Mais nous pourrions également retourner un utilisateur spécifique. Pour cela, nous allons créer une nouvelle query appelée `user`. À l'intérieur de notre type `Query`, mettez le code suivant :

```js
user(id: ID!): User!
```

Maintenant, notre type `Query` devrait ressembler à ceci :

```js
type Query {
  users: [User!]!
  user(id: ID!): User!
}
```

Comme vous le voyez, avec les queries en GraphQL, nous pouvons également passer des arguments. Dans ce cas, pour interroger un `user` spécifique, nous allons passer son `ID`.

Mais, vous vous demandez peut-être : comment GraphQL sait-il où obtenir les données ? C'est pourquoi nous devrions avoir un fichier `resolvers.js`. Ce fichier indique à GraphQL comment et où il va récupérer les données.

Tout d'abord, allez dans notre fichier `resolvers.js` et importez le `db.js` que nous venons de créer il y a quelques instants. Votre fichier `resolvers.js` devrait ressembler à ceci :

```js
import { users } from "./db";

const resolvers = {
  Query: {
    hello: () => "Hello World!"
  }
};

export default resolvers;
```

Maintenant, nous allons créer notre première Query. Allez dans votre fichier `resolvers.js` et remplacez la fonction `hello`. Maintenant, votre type Query devrait ressembler à ceci :

```js
import { users } from "./db";

const resolvers = {
  Query: {
    user: (parent, { id }, context, info) => {
      return users.find(user => user.id == id);
    },
    users: (parent, args, context, info) => {
      return users;
    }
  }
};

export default resolvers;
```

Maintenant, pour expliquer comment cela va fonctionner :

Chaque résolveur de query a quatre arguments. Dans la fonction `user`, nous allons passer `id` comme argument, puis retourner l'`user` spécifique qui correspond à l'`id` passé. Pretty simple.

Dans la fonction `users`, nous allons simplement retourner le tableau `users` qui existe déjà. Il nous retournera toujours tous nos utilisateurs.

Maintenant, nous allons tester si nos queries fonctionnent correctement. Allez sur `localhost:4000` et mettez le code suivant :

```js
query {
  users {
    id
    name
    email
    age
  }
}
```

Cela devrait vous retourner tous nos utilisateurs.

Ou, si vous voulez retourner un utilisateur spécifique :

```js
query {
  user(id: 1) {
    id
    name
    email
    age
  }
}
```

Maintenant, nous allons commencer à apprendre les **mutations**, l'une des fonctionnalités les plus importantes de GraphQL.

### Mutations

Dans GraphQL, les mutations sont la façon dont vous allez modifier des données sur le serveur et obtenir des données mises à jour en retour. Vous pouvez penser au CUD (Create, Update, Delete) de REST.

Nous allons créer notre premier type de mutation en GraphQL, et toutes nos mutations vont se retrouver à l'intérieur de ce type. Donc, pour commencer, allez dans notre `schema.graphql` et écrivez un nouveau type appelé `mutation` :

```js
type Mutation {
  createUser(id: ID!, name: String!, email: String!, age: Int): User!
  updateUser(id: ID!, name: String, email: String, age: Int): User!
  deleteUser(id: ID!): User!
}
```

Comme vous pouvez le voir, nous allons avoir trois mutations :

`createUser` : nous devons passer un `ID`, `name`, `email`, et `age`. Cela devrait nous retourner un nouvel utilisateur.

`updateUser` : nous devons passer un `ID`, et un nouveau `name`, `email`, ou `age`. Cela devrait nous retourner un nouvel utilisateur.

**deleteUser** : nous devons passer un `ID`. Cela devrait nous retourner un nouvel utilisateur.

Maintenant, allez dans notre fichier `resolvers.js` et **en dessous** de l'objet `Query`, créez un nouvel objet `mutation` comme ceci :

```js
Mutation: {
    createUser: (parent, { id, name, email, age }, context, info) => {
      const newUser = { id, name, email, age };

      users.push(newUser);

      return newUser;
    },
    updateUser: (parent, { id, name, email, age }, context, info) => {
      let newUser = users.find(user => user.id === id);

      newUser.name = name;
      newUser.email = email;
      newUser.age = age;

      return newUser;
    },
    deleteUser: (parent, { id }, context, info) => {
      const userIndex = users.findIndex(user => user.id === id);

      if (userIndex === -1) throw new Error("User not found.");

      const deletedUsers = users.splice(userIndex, 1);

      return deletedUsers[0];
    }
  }
```

Maintenant, notre fichier `resolvers.js` devrait ressembler à ceci :

```js
import { users } from "./db";

const resolvers = {
  Query: {
    user: (parent, { id }, context, info) => {
      return users.find(user => user.id == id);
    },
    users: (parent, args, context, info) => {
      return users;
    }
  },
  Mutation: {
    createUser: (parent, { id, name, email, age }, context, info) => {
      const newUser = { id, name, email, age };

      users.push(newUser);

      return newUser;
    },
    updateUser: (parent, { id, name, email, age }, context, info) => {
      let newUser = users.find(user => user.id === id);

      newUser.name = name;
      newUser.email = email;
      newUser.age = age;

      return newUser;
    },
    deleteUser: (parent, { id }, context, info) => {
      const userIndex = users.findIndex(user => user.id === id);

      if (userIndex === -1) throw new Error("User not found.");

      const deletedUsers = users.splice(userIndex, 1);

      return deletedUsers[0];
    }
  }
};

export default resolvers;
```

Maintenant, nous allons tester si nos mutations fonctionnent correctement. Allez sur `localhost:4000` et mettez le code suivant :

```js
mutation {
  createUser(id: 3, name: "Robert", email: "robert@gmail.com", age: 21) {
    id
    name
    email
    age
  }
}
```

Cela devrait vous retourner un nouvel utilisateur. Si vous voulez essayer de faire de nouvelles mutations, je vous recommande d'essayer par vous-même ! Essayez de supprimer cet utilisateur que vous avez créé pour voir si cela fonctionne correctement.

Enfin, nous allons commencer à apprendre les **subscriptions**, et pourquoi elles sont si puissantes.

### Subscriptions

Comme je l'ai dit avant, les subscriptions sont la façon dont vous allez maintenir une connexion en temps réel avec un serveur. Cela signifie que chaque fois qu'un événement se produit sur le serveur et chaque fois que cet événement est appelé, le serveur enverra les données correspondantes au client.

En travaillant avec des subscriptions, vous pouvez garder votre application à jour avec les dernières modifications entre différents utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NaIPy126r9Ie5NwjS3g-rg.png)

Une subscription basique ressemble à ceci :

```js
subscription {
  users {
    id
    name
    email
    age
  }
}
```

Vous allez dire que c'est très similaire à une query, et oui, c'est le cas. Mais cela fonctionne différemment.

Lorsque quelque chose est mis à jour sur le serveur, le serveur va exécuter la query GraphQL spécifiée dans la subscription, et envoyer un résultat nouvellement mis à jour au client.

Nous n'allons pas travailler avec les subscriptions dans cet article spécifique, mais si vous voulez en lire plus à leur sujet [cliquez ici](https://hackernoon.com/from-zero-to-graphql-subscriptions-416b9e0284f3).

### Conclusion

Comme vous l'avez vu, GraphQL est une nouvelle technologie qui est vraiment puissante. Elle nous donne un vrai pouvoir pour construire de meilleures APIs et bien conçues. C'est pourquoi je vous recommande de commencer à l'apprendre maintenant. Pour moi, elle remplacera éventuellement REST.

Merci d'avoir lu l'article.

[**Suivez-moi sur Twitter !**](https://twitter.com/leonardomso)   
[**Suivez-moi sur GitHub !**](https://github.com/leonardomso)

Je cherche une opportunité à distance, donc si vous en avez, j'adorerais en entendre parler, alors s'il vous plaît contactez-moi sur mon [**Twitter**](https://twitter.com/leonardomso) !