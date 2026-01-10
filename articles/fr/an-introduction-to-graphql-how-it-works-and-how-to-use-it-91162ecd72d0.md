---
title: 'Une introduction à GraphQL : comment ça marche et comment l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T17:03:26.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-graphql-how-it-works-and-how-to-use-it-91162ecd72d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*472sv1dYbnObNwS2
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
seo_title: 'Une introduction à GraphQL : comment ça marche et comment l''utiliser'
seo_desc: 'By Aditya Sridhar

  GraphQL is a query language for API’s. It shows what are the different types of
  data provided by the server and then the client can pick exactly what it wants.

  Also in GraphQL you can get multiple server resources in one call rather...'
---

Par Aditya Sridhar

GraphQL est un langage de requête pour les API. Il montre quels sont les différents types de données fournies par le serveur, puis le client peut choisir exactement ce qu'il veut.

Avec GraphQL, vous pouvez également obtenir plusieurs ressources du serveur en un seul appel, plutôt que de faire plusieurs appels à une API REST.

Vous pouvez consulter [https://graphql.org/](https://graphql.org/) pour la liste complète des avantages.

Le problème est que, jusqu'à ce que vous voyiez GraphQL en action, il est difficile de comprendre ses avantages. Alors, commençons à utiliser GraphQL.

Nous allons utiliser GraphQL avec NodeJS dans cet article.

### Prérequis

Installez NodeJS depuis ici : [https://nodejs.org/en/](https://nodejs.org/en/).

### Comment utiliser GraphQL avec NodeJS

GraphQL peut être utilisé avec plusieurs langages. Ici, nous allons nous concentrer sur l'utilisation de GraphQL avec JavaScript en utilisant NodeJS.

Créez un dossier appelé **graphql-with-nodejs**. Allez dans le dossier du projet et exécutez `npm init` pour créer le projet NodeJS. La commande pour cela est donnée ci-dessous.

```bash
cd graphql-with-nodejs
npm init
```

### Installer les dépendances

Installez Express en utilisant la commande suivante :

```bash
npm install express
```

Installez GraphQL en utilisant la commande suivante. Nous allons installer GraphQL et GraphQL pour Express.

```bash
npm install express-graphql graphql
```

### Code NodeJS

Créez un fichier appelé **server.js** dans le projet et copiez le code suivant dedans :

```js
const express = require('express');
const port = 5000;
const app = express();

app.get('/hello', (req,res) => {
    res.send("hello");
   }
);

app.listen(port);
console.log(`Server Running at localhost:${port}`);
```

Le code ci-dessus a un seul point de terminaison HTTP GET appelé **/hello**.

Le point de terminaison est créé en utilisant Express.

Maintenant, modifions ce code pour activer GraphQL.

### Activation de GraphQL dans le code

GraphQL aura une seule URL de point de terminaison appelée **/graphql** qui gérera toutes les requêtes.

Copiez le code suivant dans **server.js** :

```js
//obtenir toutes les bibliothèques nécessaires
const express = require('express');
const graphqlHTTP = require('express-graphql');
const {GraphQLSchema} = require('graphql');

const {queryType} = require('./query.js');

//configuration du numéro de port et de l'application express
const port = 5000;
const app = express();

 // Définir le Schéma
const schema = new GraphQLSchema({ query: queryType });

//Configurer le serveur GraphQL nodejs
app.use('/graphql', graphqlHTTP({
    schema: schema,
    graphiql: true,
}));

app.listen(port);
console.log(`Serveur GraphQL en cours d'exécution sur localhost:${port}`);
```

Passons en revue ce code maintenant.

**graphqlHTTP** nous permet de configurer un serveur GraphQL à l'URL **/graphql**. Il sait comment gérer la requête qui arrive.

Cette configuration est effectuée dans les lignes de code suivantes :

```js
app.use('/graphql', graphqlHTTP({
    schema: schema,
    graphiql: true,
}));
```

Explorons maintenant les paramètres à l'intérieur de graphqlHTTP.

### graphiql

graphiql est une interface utilisateur Web avec laquelle vous pouvez tester les points de terminaison GraphQL. Nous allons le définir sur true pour qu'il soit plus facile de tester les différents points de terminaison GraphQL que nous créons.

### schéma

GraphQL n'a qu'un seul point de terminaison externe **/graphql**. Ce point de terminaison peut avoir plusieurs autres points de terminaison faisant diverses choses. Ces points de terminaison seraient spécifiés dans le schéma.

Le schéma ferait des choses comme :

* Spécifier les points de terminaison
* Indiquer les champs d'entrée et de sortie pour le point de terminaison
* Indiquer quelle action doit être effectuée lorsqu'un point de terminaison est atteint, etc.

Le schéma est défini comme suit dans le code :

```js
const schema = new GraphQLSchema({ query: queryType });
```

Le schéma peut contenir des types **query** ainsi que **mutation**. Cet article se concentrera uniquement sur le type de requête.

### requête

Vous pouvez voir dans le schéma que la **requête** a été définie sur **queryType**.

Nous importons queryType depuis le fichier **query.js** en utilisant la commande suivante :

```js
const {queryType} = require('./query.js');
```

**query.js** est un fichier personnalisé que nous allons créer bientôt.

**query** est l'endroit où nous spécifions les points de terminaison en lecture seule dans un schéma.

Créez un fichier appelé **query.js** dans le projet et copiez le code suivant dedans.

```js
const { GraphQLObjectType,
    GraphQLString
} = require('graphql');


//Définir la requête
const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        hello: {
            type: GraphQLString,

            resolve: function () {
                return "Hello World";
            }
        }
    }
});

exports.queryType = queryType;
```

### Explication de la requête

queryType est créé en tant que **GraphQLObjectType** et reçoit le nom **Query**.

**fields** est l'endroit où nous spécifions les différents points de terminaison.

Ici, nous ajoutons donc un point de terminaison appelé **hello**.

**hello** a un **type** de **GraphQLString**, ce qui signifie que ce point de terminaison a un type de retour String. Le type est **GraphQLString** au lieu de **String** puisque c'est un schéma GraphQL. Donc, utiliser directement String ne fonctionnera pas.

La fonction **resolve** indique l'action à effectuer lorsque le point de terminaison est appelé. Ici, l'action consiste à retourner une chaîne "Hello World".

Enfin, nous exportons le querytype en utilisant `exports.queryType = queryType`. Cela garantit que nous pouvons l'importer dans **server.js**.

### Exécution de l'application

Exécutez l'application en utilisant la commande suivante :

```bash
node server.js
```

L'application s'exécute sur **localhost:5000/graphql**.

Vous pouvez tester l'application en allant sur localhost:5000/graphql.

Cette URL exécute l'interface utilisateur Web Graphiql comme montré dans l'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/MIEYIUgUDC85-MYLKOU5kddtUiGduNKCTDSk)

L'entrée est donnée à gauche et la sortie est affichée à droite.

Donnez l'entrée suivante

```js
{
  hello
}
```

Cela donnera la sortie suivante

```js
{
  "data": {
    "hello": "Hello World"
  }
}
```

### Félicitations 🎉

Vous avez créé votre premier point de terminaison GraphQL.

### Ajout de plus de points de terminaison

Nous allons créer 2 nouveaux points de terminaison :

* **movie** : Ce point de terminaison retournera un film, étant donné l'ID du film
* **director** : Ce point de terminaison retournera un réalisateur étant donné l'ID du réalisateur. Il retournera également tous les films réalisés par ce réalisateur.

### Ajout de données

Habituellement, une application lira les données à partir d'une base de données. Mais pour ce tutoriel, nous allons coder en dur les données dans le code lui-même pour simplifier.

Créez un fichier appelé **data.js** et ajoutez le code suivant.

```js
//Coder en dur certaines données pour les films et les réalisateurs
let movies = [{
    id: 1,
    name: "Film 1",
    year: 2018,
    directorId: 1
},
{
    id: 2,
    name: "Film 2",
    year: 2017,
    directorId: 1
},
{
    id: 3,
    name: "Film 3",
    year: 2016,
    directorId: 3
}
];

let directors = [{
    id: 1,
    name: "Réalisateur 1",
    age: 20
},
{
    id: 2,
    name: "Réalisateur 2",
    age: 30
},
{
    id: 3,
    name: "Réalisateur 3",
    age: 40
}
];

exports.movies = movies;
exports.directors = directors;
```

Ce fichier contient les données des films et des réalisateurs. Nous utiliserons les données de ce fichier pour nos points de terminaison.

### Ajout du point de terminaison movie à la requête

Les nouveaux points de terminaison seront ajoutés à queryType dans le fichier query.js.

Le code pour le point de terminaison movie est montré ci-dessous :

```js
movie: {
            type: movieType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(movies, { id: args.id });
            }
        }
```

Le type de retour de ce point de terminaison est **movieType** qui sera défini bientôt.

Le paramètre **args** est utilisé pour indiquer l'entrée du point de terminaison movie. L'entrée de ce point de terminaison est **id** qui est de type **GraphQLInt.**

La fonction **resolve** retourne le film correspondant à l'id, à partir de la liste des films. **find** est une fonction de la bibliothèque **lodash** utilisée pour trouver un élément dans une liste.

Le code complet pour **query.js** est montré ci-dessous :

```js
const { GraphQLObjectType,
    GraphQLString,
    GraphQLInt
} = require('graphql');
const _ = require('lodash');

const {movieType} = require('./types.js');
let {movies} = require('./data.js');


//Définir la requête
const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        hello: {
            type: GraphQLString,

            resolve: function () {
                return "Hello World";
            }
        },

        movie: {
            type: movieType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(movies, { id: args.id });
            }
        }
    }
});

exports.queryType = queryType;
```

À partir du code ci-dessus, nous pouvons voir que **movieType** est en fait défini dans **types.js.**

### Ajout du type personnalisé movieType

Créez un fichier appelé **types.js**.

Ajoutez le code suivant dans types.js

```js
const {
    GraphQLObjectType,
    GraphQLID,
    GraphQLString,
    GraphQLInt
} = require('graphql');

// Définir le type Film
movieType = new GraphQLObjectType({
    name: 'Movie',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        year: { type: GraphQLInt },
        directorId: { type: GraphQLID }

    }
});

exports.movieType = movieType;
```

On peut voir que **movieType** est créé en tant que **GraphQLObjectType.**

Il a 4 champs : **id, name, year et directorId**. Les types pour chacun de ces champs sont également spécifiés lors de leur ajout.

Ces champs proviennent directement des données. Dans ce cas, ils proviendront de la liste **movies**.

### Ajout de la requête et du type pour le point de terminaison director

Comme pour movie, le point de terminaison director peut également être ajouté.

Dans **query.js**, le point de terminaison director peut être ajouté comme suit :

```js
director: {
            type: directorType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(directors, { id: args.id });
            }
        }
```

**directorType** peut être ajouté comme suit dans **types.js** :

```js
//Définir le type Réalisateur
directorType = new GraphQLObjectType({
    name: 'Director',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        age: { type: GraphQLInt },
        movies: {
            type: new GraphQLList(movieType),
            resolve(source, args) {
                return _.filter(movies, { directorId: source.id });
            }

        }

    }
});
```

Attendez une minute. Le **directorType** est légèrement différent de **movieType**. Pourquoi ?

Pourquoi y a-t-il une fonction resolve à l'intérieur de **directorType** ? Auparavant, nous avons vu que les fonctions resolve étaient présentes uniquement dans la **query…**

### La nature spéciale de directorType

Lorsque le point de terminaison **director** est appelé, nous devons retourner les détails du réalisateur, ainsi que tous les films que le réalisateur a réalisés.

Les 3 premiers champs **id, name, age** dans **directorType** sont simples et proviennent directement des données (liste **directors**).

Le quatrième champ, **movies**, doit contenir la liste des films de ce réalisateur.

Pour cela, nous indiquons que le type du champ **movies** est une **GraphQLList de movieType** (Liste de films).

Mais comment allons-nous trouver tous les films réalisés par ce réalisateur ?

Pour cela, nous avons une fonction **resolve** à l'intérieur du champ movies. Les entrées de cette fonction resolve sont **source** et **args**.

source contiendra les détails de l'objet parent.

Supposons que les champs **id =1, name = "Random" et age = 20** pour un réalisateur. Alors **source.id =1, source.name = "Random" et source.age = 20**

Donc dans cet exemple, la fonction resolve trouve tous les films où directorId correspond à l'Id du réalisateur requis.

### Code

L'ensemble du code pour cette application est disponible dans ce [dépôt GitHub](https://github.com/aditya-sridhar/graphql-with-nodejs)

### Test de l'application

Maintenant, testons l'application pour différents scénarios.

Exécutez l'application en utilisant `node server.js`.

Allez sur **localhost:5000/graphql** et essayez les entrées suivantes.

### movie

Entrée :

```js
{
  movie(id: 1) {
    name
  }
}
```

Sortie :

```js
{
  "data": {
    "movie": {
      "name": "Film 1"
    }
  }
}
```

D'après ce qui précède, nous pouvons voir que le client peut demander exactement ce qu'il veut et GraphQL garantira que seuls ces paramètres sont renvoyés. Ici, seul le champ **name** est demandé et seul celui-ci est renvoyé par le serveur.

Dans `movie(id: 1)`, id est le paramètre d'entrée. Nous demandons au serveur de renvoyer le film dont l'id est 1.

Entrée :

```js
{
  movie(id: 3) {
    name
    id
    year
  }
}
```

Sortie :

```js
{
  "data": {
    "movie": {
      "name": "Film 3",
      "id": "3",
      "year": 2016
    }
  }
}
```

Dans l'exemple ci-dessus, les champs **name, id et year** sont demandés. Donc le serveur renvoie tous ces champs.

### director

Entrée :

```js
{
  director(id: 1) {
    name
    id,
    age
  }
}
```

Sortie :

```js
{
  "data": {
    "director": {
      "name": "Réalisateur 1",
      "id": "1",
      "age": 20
    }
  }
}
```

Entrée :

```js
{
  director(id: 1) {
    name
    id,
    age,
    movies{
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
    "director": {
      "name": "Réalisateur 1",
      "id": "1",
      "age": 20,
      "movies": [
        {
          "name": "Film 1",
          "year": 2018
        },
        {
          "name": "Film 2",
          "year": 2017
        }
      ]
    }
  }
}
```

Dans l'exemple ci-dessus, nous voyons la puissance de GraphQL. Nous indiquons que nous voulons un réalisateur avec l'id 1. Nous indiquons également que nous voulons tous les films de ce réalisateur. Les champs du réalisateur et des films sont personnalisables et le client peut demander exactement ce qu'il veut.

De même, cela peut être étendu à d'autres champs et types. Par exemple, nous pourrions exécuter une requête comme **Trouver un réalisateur avec l'id 1. Pour ce réalisateur, trouver tous les films. Pour chaque film, trouver les acteurs. Pour chaque acteur, obtenir les 5 films les mieux notés** et ainsi de suite. Pour cette requête, nous devons spécifier la relation entre les types. Une fois que nous avons fait cela, le client peut interroger n'importe quelle relation qu'il souhaite.

### Félicitations 🎉

Vous connaissez maintenant les concepts de base de GraphQL.

Vous pouvez consulter la [documentation](https://graphql.github.io/learn/) pour en savoir plus sur GraphQL

### À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site Web : [https://adityasridhar.com/](https://adityasridhar.com/)

Lisez plus de mes articles sur mon blog à l'adresse [adityasridhar.com.](https://adityasridhar.com/)