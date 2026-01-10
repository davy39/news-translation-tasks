---
title: 'Introduction aux mutations dans GraphQL : ce qu''elles sont et comment les
  utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T17:57:04.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-mutations-in-graphql-what-they-are-and-how-to-use-them-e959735abd8d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-z0QCz9YmonRiRBq
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Introduction aux mutations dans GraphQL : ce qu''elles sont et comment
  les utiliser'
seo_desc: 'By Aditya Sridhar

  This blog post is a continuation of my previous blog post on GraphQL Basics. Click
  Here to check out the GraphQL Basics post.

  It is necessary to read the GraphQL Basics post to make the best use of this article.

  What is a mutation i...'
---

Par Aditya Sridhar

Cet article est la suite de mon précédent article sur les bases de GraphQL. [Cliquez ici](https://medium.freecodecamp.org/an-introduction-to-graphql-how-it-works-and-how-to-use-it-91162ecd72d0) pour consulter l'article sur les bases de GraphQL.

Il est nécessaire de lire l'article sur les bases de GraphQL pour tirer le meilleur parti de cet article.

### Qu'est-ce qu'une mutation dans GraphQL ?

Chaque fois que vous souhaitez écrire des données sur le serveur, les mutations sont utilisées.

### En quoi la mutation et la requête sont-elles différentes ?

**Query** est utilisé lorsque vous souhaitez lire des données depuis le serveur. **Mutation** est utilisé lorsque vous souhaitez écrire des données sur le serveur.

Mais attendez. Ne puis-je pas aller dans le resolver dans **query** et effectuer une opération d'écriture ?

Bien qu'il soit possible d'effectuer une opération d'écriture dans une **query**, cela ne devrait pas être fait. Il est nécessaire de séparer les opérations de lecture et d'écriture, et donc les **mutations** sont nécessaires.

### Code

[Cliquez ici](https://github.com/aditya-sridhar/graphql-with-nodejs) pour obtenir le code de mon précédent article. Nous allons ajouter la logique de mutation à ce code dans cet article.

### Ajouter une mutation de film

Créons une mutation qui peut être utilisée pour ajouter un nouveau film.

Créez un nouveau fichier appelé **mutation.js**. Copiez le code suivant dans **mutation.js** :

```js
const { GraphQLObjectType
} = require('graphql');
const _ = require('lodash');

const {movieType} = require('./types.js');
const {inputMovieType} = require('./inputtypes.js');
let {movies} = require('./data.js');

const mutationType = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        addMovie: {
            type: movieType,
            args: {
                input: { type: inputMovieType }
            },
            resolve: function (source, args) {

                let movie = {
                    id: args.input.id, 
                    name: args.input.name, 
                    year: args.input.year, 
                    directorId: args.input.directorId};

                movies.push(movie);

                return _.find(movies, { id: args.input.id });
            }
        }
    }
});

exports.mutationType = mutationType;
```

Vous remarquerez qu'une mutation ressemble beaucoup à une requête. La principale différence est que le nom du **GraphQLObjectType** est **Mutation**.

Ici, nous avons ajouté une mutation appelée **addMovie** qui a un type de retour de **movieType** ( _movieType_ a été couvert dans le [précédent](https://adityasridhar.com/posts/what-is-graphql-and-how-to-use-it) blog ).

Dans les args, nous mentionnons que nous avons besoin d'un paramètre appelé **input** qui est de type **inputMovieType**

Alors, qu'est-ce que **inputMovieType** ici ?

### Types d'entrée

Il est possible que plusieurs mutations nécessitent les mêmes arguments d'entrée. Il est donc bon de créer des **Input Types** et de réutiliser les Input Types pour toutes ces mutations.

Ici, nous créons un type d'entrée pour le film appelé **inputMovieType**.

Nous pouvons voir que **inputMovieType** provient du fichier **inputtypes.js**. Créons cela maintenant.

Créez un nouveau fichier appelé **inputtypes.js**.

Copiez le code suivant dans inputtypes.js :

```js
const {
    GraphQLInputObjectType,
    GraphQLID,
    GraphQLString,
    GraphQLInt
} = require('graphql');

inputMovieType = new GraphQLInputObjectType({
    name: 'MovieInput',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        year: { type: GraphQLInt },
        directorId: { type: GraphQLID }

    }
});

exports.inputMovieType = inputMovieType;
```

Nous pouvons voir qu'un Input Type ressemble exactement à n'importe quel autre Type dans GraphQL. **GraphQLInputObjectType** est utilisé pour créer un Input Type, tandis que **GraphQLObjectType** est utilisé pour créer des Types normaux.

### Fonction de résolution d'une mutation

La fonction de résolution d'une mutation est l'endroit où l'opération d'écriture réelle se produit.

Dans une application réelle, cela peut être une opération d'écriture de base de données.

Pour cet exemple, nous ajoutons simplement les données au tableau de films puis nous retournons le film ajouté.

```js
resolve: function (source, args) {

                let movie = {
                    id: args.input.id, 
                    name: args.input.name, 
                    year: args.input.year, 
                    directorId: args.input.directorId};

                movies.push(movie);

                return _.find(movies, { id: args.input.id });
            }
```

Le code ci-dessus dans resolve effectue les actions suivantes :

* Obtient les paramètres du film d'entrée depuis l'arg **input**.
* Ajoute le nouveau film au tableau de films
* Retourne le nouveau film qui a été ajouté en le récupérant depuis le tableau de films

### Ajouter une mutation de réalisateur

Créons une mutation qui peut être utilisée pour ajouter un nouveau réalisateur.

Cela serait la même chose que l'ajout de la mutation Movie.

**inputtypes.js** avec la mutation Director ajoutée :

```js
const {
    GraphQLInputObjectType,
    GraphQLID,
    GraphQLString,
    GraphQLInt
} = require('graphql');

inputMovieType = new GraphQLInputObjectType({
    name: 'MovieInput',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        year: { type: GraphQLInt },
        directorId: { type: GraphQLID }

    }
});

inputDirectorType = new GraphQLInputObjectType({
    name: 'DirectorInput',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        age: { type: GraphQLInt }

    }
});

exports.inputMovieType = inputMovieType;
exports.inputDirectorType = inputDirectorType;
```

**mutation.js** après avoir ajouté la mutation **addDirector** :

```js
const { GraphQLObjectType
} = require('graphql');
const _ = require('lodash');

const {movieType,directorType} = require('./types.js');
const {inputMovieType,inputDirectorType} = require('./inputtypes.js');
let {movies,directors} = require('./data.js');

const mutationType = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        addMovie: {
            type: movieType,
            args: {
                input: { type: inputMovieType }
            },
            resolve: function (source, args) {

                let movie = {
                    id: args.input.id, 
                    name: args.input.name, 
                    year: args.input.year, 
                    directorId: args.input.directorId};

                movies.push(movie);

                return _.find(movies, { id: args.input.id });
            }
        },
        addDirector: {
            type: directorType,
            args: {
                input: { type: inputDirectorType }
            },
            resolve: function (source, args) {
                let director = {
                    id: args.input.id, 
                    name: args.input.name, 
                    age: args.input.age};

                directors.push(director);

                return _.find(directors, { id: args.input.id });
            }
        }
    }
});

exports.mutationType = mutationType;
```

### Activer les mutations

Jusqu'à présent, nous avons défini les points de terminaison de mutation et leurs fonctionnalités. Mais nous n'avons pas encore activé les mutations.

Pour les activer, les mutations doivent être ajoutées au schéma.

La mutation est ajoutée en utilisant le code suivant dans **server.js** :

```js
// Définir le Schéma
const schema = new GraphQLSchema(
    { 
        query: queryType,
        mutation: mutationType 
    }
);
```

Code complet dans **server.js** après avoir ajouté la mutation :

```js
// obtenir toutes les bibliothèques nécessaires
const express = require('express');
const graphqlHTTP = require('express-graphql');
const {GraphQLSchema} = require('graphql');

const {queryType} = require('./query.js');
const {mutationType} = require('./mutation.js');

// configurer le numéro de port et l'application express
const port = 5000;
const app = express();

 // Définir le Schéma
const schema = new GraphQLSchema(
    { 
        query: queryType,
        mutation: mutationType 
    }
);

// Configurer le serveur GraphQL nodejs 
app.use('/graphql', graphqlHTTP({
    schema: schema,
    graphiql: true,
}));

app.listen(port);
console.log(`Serveur GraphQL en cours d'exécution sur localhost:${port}`);
```

### Code

Le code complet pour cet article peut être trouvé dans [ce dépôt git](https://github.com/aditya-sridhar/graphql-mutations-with-nodejs).

### Tester les points de terminaison de mutation

Exécutez l'application en utilisant la commande suivante :

```bash
node server.js
```

Ouvrez votre navigateur web et allez à l'URL suivante **localhost:5000/graphql**

### Tester le point de terminaison de mutation addMovie

Entrée :

```js
mutation {
	addMovie(input: {id: 4,name: "Film 4", year: 2020,directorId:4}){
    id,
    name,
	year,
    directorId
  }
  
}
```

Sortie :

```js
{
  "data": {
    "addMovie": {
      "id": "4",
      "name": "Film 4",
      "year": 2020,
      "directorId": "4"
    }
  }
}
```

Entrée :

```js
mutation {
	addMovie(input: {id: 5,name: "Film 5", year: 2021,directorId:4}){
    id,
    name,
	year,
    directorId
  }
  
}
```

Sortie :

```js
{
  "data": {
    "addMovie": {
      "id": "5",
      "name": "Film 5",
      "year": 2021,
      "directorId": "4"
    }
  }
}
```

### Tester le point de terminaison de mutation addDirector

Entrée :

```js
mutation {
	addDirector(input: {id: 4,name: "Réalisateur 4", age: 30}){
    id,
    name,
	age,
    movies{
      id,
      name,
      year
    }
  }
  
}
```

Sortie :

```js
{
  "data": {
    "addDirector": {
      "id": "4",
      "name": "Réalisateur 4",
      "age": 30,
      "movies": [
        {
          "id": "4",
          "name": "Film 4",
          "year": 2020
        },
        {
          "id": "5",
          "name": "Film 5",
          "year": 2021
        }
      ]
    }
  }
}
```

### Félicitations 🎉

Vous savez maintenant ce que sont les Mutations dans GraphQL !

Vous pouvez consulter la [documentation](https://graphql.github.io/learn/) pour en savoir plus sur GraphQL.

### À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

Lisez plus de mes articles sur mon blog à l'adresse [adityasridhar.com](https://adityasridhar.com/posts/what-is-a-mutation-in-graphql-and-how-to-use-it).