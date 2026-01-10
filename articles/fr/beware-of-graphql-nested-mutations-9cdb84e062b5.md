---
title: Attention aux mutations imbriquées de GraphQL !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T17:51:21.000Z'
originalURL: https://freecodecamp.org/news/beware-of-graphql-nested-mutations-9cdb84e062b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6bCUDbvVF5Ccaavkye2Tjw.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Attention aux mutations imbriquées de GraphQL !
seo_desc: 'By Jeff M Lowery

  “I have a cunning plan…”

  Once upon a time, I hit upon the notion of organizing GraphQL mutations by nesting
  operations in a return type. The idea was that these operations would then mutate
  the parent entity.

  The basic idea was this:...'
---

Par Jeff M Lowery

_J'ai un plan astucieux..._

Il était une fois, j'ai eu l'idée d'[organiser les mutations GraphQL](https://www.freecodecamp.org/news/organizing-graphql-mutations-653306699f3d/) en imbriquant les opérations dans un type de retour. L'idée était que ces opérations muteraient ensuite l'entité parente.

L'idée de base était la suivante :

```
input AddBookInput {
            ISBN: String!
            title: String!
        }
        
input RemoveBookInput {
            bookId: Int!
        }
        
input UpdateBookInput {
          ISBN: String!
          title: String!
      }
      
type AuthorOps {
          addBook(input: AddBookInput!): Int
          removeBook(input: RemoveBookInput! ): Boolean
          updateBook(input: UpdateBookInput!): Book
      }
      
type Mutation {
        Author(id: Int!): AuthorOps
      }
```

Et j'ai utilisé cette technique quelques fois sans problème, mais j'ai eu de la chance. Où est le problème ?

[Un lecteur m'a dirigé](https://medium.com/@anddoutoi/hey-jeff-bca074856669) vers [un problème](https://github.com/graphql/graphql-js/issues/221) sur le site GitHub de GraphQL où il était indiqué que l'ordre d'exécution des **mutations imbriquées** n'est pas garanti. Oh-oh. Dans le cas ci-dessus, je veux définitivement que la mutation **addBook**() se produise avant de tenter une opération **updateBook**() sur le même livre. Malheureusement, seules les mutations dites **racines** sont garanties de s'exécuter dans l'ordre.

### Une illustration du problème

Supposons que j'ai une file d'attente de messages où je veux que les messages soient stockés dans l'ordre où ils ont été reçus. Certains messages prennent plus de temps à traiter, donc j'utilise une mutation pour garantir que les messages sont traités séquentiellement :

```
type Query {
  noop: String!
}

type Mutation {
  message(id: ID!, wait: Int!): String!
}
```

Le resolver enregistre quand le message arrive, puis attend un temps donné avant de retourner le résultat de la mutation :

```js
const msg = (id, wait) => new Promise(resolve => {
  setTimeout(() => {
    
console.log({id, wait})
    let message = `response to message ${id}, wait is ${wait} seconds`;
    
resolve(message);
  }, wait)
})

const resolvers = {
  Mutation: {
    message: (_, {id, wait}) => msg(id, wait),
  }
}
```

Maintenant, pour l'essai. Je vais vouloir m'assurer que les messages de la console sont dans le même ordre que les requêtes de mutation. Voici la requête :

```js
mutation root {
  message1: message(id: 1, wait: 3000)
  message2: message(id: 2, wait: 1000)
  message3: message(id: 3, wait: 500)
  message4: message(id: 4, wait: 100)
}
```

La réponse est :

```json
{
  "data": {
    "message1": "response to message 1, wait is 3000 seconds",
    "message2": "response to message 2, wait is 1000 seconds",
    "message3": "response to message 3, wait is 500 seconds",
    "message4": "response to message 4, wait is 100 seconds"
  }
}
```

Et la console dit :

```
{ id: '1', wait: 3000 }
{ id: '2', wait: 1000 }
{ id: '3', wait: 500 }
{ id: '4', wait: 100 }
```

Super ! Les messages sont traités dans l'ordre où ils sont reçus, même si le deuxième et les messages suivants prennent moins de temps que le précédent. En d'autres termes, les mutations sont exécutées séquentiellement.

#### Le grain de sable

Maintenant, imbriquons ces opérations et voyons ce qui se passe. D'abord, je définis un type **MessageOps**, puis j'ajoute une mutation **Nested** :

```
const typeDefs = `
type Query {
  noop: String!
}

type MessageOps {
  message(id: ID!, wait: Int!): String!
}

type Mutation {
  message(id: ID!, wait: Int!): String!
  Nested: MessageOps
}`
```

Mes mutations passent maintenant par le resolver Nested, retournant MessageOps, que j'utilise ensuite pour exécuter ma mutation de message :

```
mutation nested {
  Nested {
    message1: message(id: 1, wait: 3000)
    message2: message(id: 2, wait: 1000)
    message3: message(id: 3, wait: 500)
    message4: message(id: 4, wait: 100)
  }
}
```

Assez similaire à ce que nous avions avant, et la réponse à la requête de mutation ressemble presque à la même :

```
{
  "data": {
    "Nested": {
      "message1": "response to message 1, wait is 3000 seconds",
      "message2": "response to message 2, wait is 1000 seconds",
      "message3": "response to message 3, wait is 500 seconds",
      "message4": "response to message 4, wait is 100 seconds"
    }
  }
}
```

La seule différence est que les réponses sont emballées dans un objet JSON Nested. Malheureusement, la console révèle une histoire de malheur :

```
{ id: '4', wait: 100 }
{ id: '3', wait: 500 }
{ id: '2', wait: 1000 }
{ id: '1', wait: 3000 }
```

Elle révèle que les messages sont traités hors séquence : les messages les plus rapides à traiter sont postés en premier.

D'accord. [Dans le code](https://github.com/JeffML/graphql-crud2) de mon article original, j'ai en fait fait quelque chose de plus proche de ce qui suit :

```
mutation nested2 {
  Nested {
    message1: message(id: 1, wait: 3000)
  }
  Nested {
    message2: message(id: 2, wait: 1000)
  }
  Nested {
    message3: message(id: 3, wait: 500)
  }
  Nested {
    message4: message(id: 4, wait: 100)
  }
}
```

Peut-être que cela fonctionne ? Chaque opération de mutation est dans sa propre mutation racine Nested, donc nous pourrions nous attendre à ce que les mutations Nested s'exécutent séquentiellement. La réponse est identique à celle d'avant :

```
{
  "data": {
    "Nested": {
      "message1": "response to message 1, wait is 3000 seconds",
      "message2": "response to message 2, wait is 1000 seconds",
      "message3": "response to message 3, wait is 500 seconds",
      "message4": "response to message 4, wait is 100 seconds"
    }
  }
}
```

Mais il en va de même pour le journal de la console :

```
{ id: '4', wait: 100 }
{ id: '3', wait: 500 }
{ id: '2', wait: 1000 }
{ id: '1', wait: 3000 }
```

#### Alors, que se passe-t-il ici ?

Le « problème » est que GraphQL exécute une mutation Nested, retournant un objet avec d'autres méthodes de mutation. Malheureusement, une fois que cet objet est retourné, GraphQL passe à la requête de mutation suivante, sans savoir qu'il y a d'autres opérations de mutation à effectuer dans la requête.

GraphQL est élégamment simple, mais la simplicité a un coût. Il est concevable que les mutations imbriquées puissent être supportées, par exemple en ajoutant un type **mutator** (son corollaire serait le type [**input**](https://graphql.org/graphql-js/mutations-and-input-types/)), que GraphQL traiterait comme une extension de l'opération de mutation. En l'état, il n'y a tout simplement pas assez d'informations dans la requête de mutation pour savoir que les opérations imbriquées sont également des mutateurs.

### Organiser les mutations GraphQL, partie 2

Vous pouvez toujours utiliser la technique pour des opérations qui ne sont pas séquentiellement dépendantes, mais c'est une hypothèse qui est susceptible d'être fragile et difficile à déboguer lorsqu'elle est violée. Peut-être que l'assemblage de schéma [stitching](https://www.apollographql.com/docs/graphql-tools/schema-stitching.html) ou [weaving](https://www.npmjs.com/package/graphql-weaver) offre une réponse. J'espère explorer ces approches dans un futur article.

L'application NodeJS complète utilisée pour cet article peut être trouvée [ici](https://github.com/JeffML/nested_mutations).