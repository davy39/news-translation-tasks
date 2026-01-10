---
title: Organiser les Mutations GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T17:38:27.000Z'
originalURL: https://freecodecamp.org/news/organizing-graphql-mutations-653306699f3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OYjAHBzgbgDRDFJeIrzr0Q.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Organiser les Mutations GraphQL
seo_desc: 'By Jeff M Lowery

  Cleaning up the CRUD.

  Update (5/7/2018): Anders Ringqvist (comments) spotted an issue report that can
  cause problems when using this approach. Please see my follow up post.

  —

  The Great Divide in GraphQL schemas runs between Queries a...'
---

Par Jeff M Lowery

Nettoyer le CRUD.

**_Mise à jour (5/7/2018) :_** Anders Ringqvist (commentaires) a repéré [un rapport de problème](https://github.com/graphql/graphql-js/issues/221) qui **peut causer des problèmes** lors de l'utilisation de cette approche. Veuillez consulter [mon article de suivi](https://www.freecodecamp.org/news/beware-of-graphql-nested-mutations-9cdb84e062b5/).

—

Le Grand Fossé dans les schémas GraphQL sépare les [Requêtes et les Mutations](http://graphql.org/learn/queries/). Une méthode de requête lit les données d'une source de données, telle qu'une base de données SQL, un système de fichiers ou même un service distant. Alors que les requêtes peuvent être exécutées simultanément, les mutations ne le peuvent pas.

Les mutations doivent être exécutées séquentiellement car la prochaine opération de mutation peut dépendre des données stockées ou mises à jour par la mutation précédente. Par exemple, un enregistrement doit être créé avant de pouvoir être mis à jour. Par conséquent, les mutations doivent être exécutées séquentiellement. C'est pourquoi les requêtes et les mutations ont leur propre espace de noms dans GraphQL.

Les requêtes sont le « R » dans CRUD (Create, Read, Update, & Delete). Le code de cet article s'appuie sur un [exemple Launchpad](https://launchpad.graphql.com/1jzxrj179). Dans le code Launchpad, il y a une requête définie qui retournera les Posts d'un Auteur, donné un ID d'auteur. J'ai déjà étendu cet exemple une fois dans mon article sur [le test des interfaces GraphQL](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364). Dans cet article, j'ai ajouté des Livres au mélange, et ici je vais étendre cette idée.

### Posts d'Auteur

Les mutations sont le CUD dans CRUD. L'exemple Launchpad lié ci-dessus a une mutation `**upvotePost**` qui augmente le compte de votes (une opération de mise à jour) pour un Post.

```js
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
```

Pour implémenter également le vote négatif, je crée simplement une mutation `**downvotePost**` similaire :

```js
Mutation: {
...

  downvotePost: (_, { postId }) => {
      const post = find(posts, { id: postId });
      if (!post) {
        throw new Error(`Couldn't find post with id ${postId}`);
      }
      post.votes -= 1;
      return post;
    },
  },
```

Ce n'est pas exactement une façon [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) de faire les choses. Le corps de la logique pourrait être placé dans une fonction externe unique avec un paramètre pour incrémenter le vote positif ou négatif.

De plus, je voudrais me débarrasser des noms `upvotePost` et `downvotePost` et plutôt m'appuyer sur un contexte, comme `**Post.upvote()**` et `**Post.downvote()**`. Cela peut être fait en faisant retourner à la méthode Mutation un ensemble d'opérations qui affectent un Post donné.

`PostOps` est un type défini comme :

```js
type PostOps {
          upvote(postId: Int!): Post
          downvote(postId: Int!): Post
      }
```

Le nom `**Post**` a été éliminé du nom verbe-nom de la méthode car il est redondant. Le code du resolver fonctionne dans un contexte Post, via `PostOps` :

```js
const voteHandler = (postId, updown) => {
    return new Promise((resolve, reject) => {
        const post = posts.find(p => p.id === postId);
        if (!post) {
            reject(`Couldn't find post with id ${postId}`);
        }
        post.votes += updown;
        resolve(post);
    })
};

const PostOps =
    ({
        upvote: ({
            postId
        }) => voteHandler(postId, 1),
        downvote: ({
            postId
        }) => voteHandler(postId, -1)
    });
```

Vous remarquerez que j'utilise une nouvelle Promise dans le resolver, bien que techniquement ce ne soit pas nécessaire pour cet exemple. Néanmoins, la plupart des applications récupèrent les données de manière asynchrone, donc... force de l'habitude ?

Maintenant, au lieu d'appeler une méthode de mutation directement au niveau racine, elle est appelée dans le contexte d'un `Post` :

```js
mutation upvote {
  Post {
    upvote(postId: 3) {
      votes
    }
  }
}
```

Et cela retourne :

```json
{
  "data": {
    "Post": {
      "upvote": {
        "votes": 2
      }
    }
  }
}
```

Jusqu'à présent, tout va bien. Les méthodes pourraient être encore plus DRY en déplaçant l'argument `**postId**` au niveau supérieur :

```js
extend type Mutation {
        Post
(postId: Int!): PostOps
}

type PostOps {
          upvote: Post
          downvote: Post
      }
```

Les resolvers `PostOp` resteraient inchangés : ils prennent toujours un paramètre `postId`, mais ce paramètre est passé de `Post` à `PostOps`. Le prochain exemple expliquera comment cela fonctionne en détail.

### Auteurs et Livres

Les Auteurs dans mon application non seulement écrivent des Posts, mais certains ont également écrit des Livres. Je souhaite effectuer des opérations classiques de Création, Mise à jour et Suppression sur la liste des livres écrits. Les `AuthorOps` sont alors :

```js
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
```

Dans GraphQL, [les Mutations prennent leurs propres types d'Input](http://graphql.org/graphql-js/mutations-and-input-types/) comme paramètres. Cela est généralement nécessaire pour les entités qui ont des IDs auto-générés. Dans le type Query, l'ID de l'Auteur peut être requis, mais dans le type AuthorInput, il ne l'est pas et ne peut pas l'être (l'ID est généré).

Dans ce cas, l'ISBN est l'ID du Livre non généré, donc il est inclus dans `CreateBookInput`. Les Livres ont également un Auteur. D'où cela va-t-il venir ? Il s'avère que `authorId` est passé au resolver `addBook` à partir du contexte à partir duquel l'opération de création est appelée, à savoir `AuthorOps` :

```js
extend type Mutation {
        Post: PostOps
        Author(id: Int!): AuthorOps
      }
```

Le resolver pour `AuthorOps` ressemble à :

```js
const addBook = (book, authorId) => {
    console.log("addBook", book, authorId)
    return new Promise((resolve, reject) => {
        book.authorId = authorId
        books.push(book)
        resolve(books.length)
    })
}

const removeBook = (book, authorId) => {
    return new Promise((resolve, reject) => {
        books = books.filter(b => b.ISBN !== book.ISBN && b.authorId === authorId);
        resolve(books.length)
    })
}

const updateBook = (book, authorId) => {
    return new Promise((resolve, reject) => {
        let old = books.find(b => b.ISBN === book.ISBN && b.authorId === authorId);
        if (!old) {
            reject(`Book with ISBN = ${book.ISBN} not found`)
            return
        }
        resolve(Object.assign(old, book))
    })
}

const AuthorOps = (authorId) => ({
    addBook: ({
        input
    }) => addBook(input, authorId),
    removeBook: ({
        input
    }) => removeBook(input, authorId),
    updateBook: ({
        input
    }) => updateBook(input, authorId)
})
```

Maintenant, créons un livre et mettons-le à jour :

```js
mutation addAndUpdateBook {
  Author(id: 4) {
    
addBook(input: {ISBN: "922-12312455", title: "Flimwitz le Magnifique"})
  }
  Author(id: 4) {
    
updateBook(input: {ISBN: "922-12312455", title: "Flumwitz le Magnifique"}) {
      authorId
      title
    }
  }
}
```

La réponse est :

```json
{
  "data": {
    "Author": {
      "addBook": 4,
      "updateBook": {
        "authorId": 4,
        "title": "Flumwitz le Magnifique"
      }
    }
  }
}
```

#### Et « Book » ?

Vous avez peut-être remarqué qu'il y a en fait un sous-contexte en jeu. Remarquez que nous avons des mutations nommées `**addBook**`, `**updateBook**`, `**removeBook**`. Je pourrais refléter cela dans le schéma :

```js
type AuthorOps {
     Book: BookOps
}

type BookOps {
     add(input: AddBookInput!): Int
     remove(input: RemoveBookInput! ): Boolean
     update(input: UpdateBookInput!): Book
}
```

Rien ne vous empêche d'ajouter des contextes aussi profonds que vous le souhaitez, mais sachez que les résultats retournés sont imbriqués plus profondément à chaque fois que cette technique est utilisée :

```json
>>> RESPONSE >>>
{
  "data": {
    "Author": {
       "Book": {

          "add": 4,
          "update": {
             "authorId": 4,
             "title": "Flumwitz le Magnifique"
          }
        }
     }
  }
}
```

Cela est assez similaire à la structure que les requêtes GraphQL retournent, mais pour les opérations de mutation, les hiérarchies profondes peuvent être gênantes : vous devez « creuser profondément » pour savoir si votre opération de mutation a réussi. Dans certains cas, une réponse plus plate peut être meilleure. Néanmoins, une organisation peu profonde des mutations dans quelques contextes de haut niveau semble meilleure que rien.

Le code source fonctionnel pour cet article peut être trouvé [sur mon compte Github](https://github.com/JeffML/graphql-crud2).