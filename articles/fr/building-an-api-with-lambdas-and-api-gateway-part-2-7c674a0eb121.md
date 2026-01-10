---
title: Comment intégrer DynamoDB dans votre API en utilisant AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T20:38:49.000Z'
originalURL: https://freecodecamp.org/news/building-an-api-with-lambdas-and-api-gateway-part-2-7c674a0eb121
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DpwCOdwJh84BzmZCuJPLmA.png
tags:
- name: Amazon
  slug: amazon
- name: AWS
  slug: aws
- name: lambda
  slug: lambda
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment intégrer DynamoDB dans votre API en utilisant AWS Lambda
seo_desc: 'By Sam Williams

  In the first part of this tutorial, we created an API which passed requests through
  to a Lambda which returned the top tv show or movie for that genre. Now we’re going
  to use DynamoDB to allow users to vote for their favourite genre.

  ...'
---

Par Sam Williams

Dans la [première partie de ce tutoriel](https://medium.freecodecamp.org/building-an-api-with-lambdas-and-api-gateway-11254e23b703), nous avons créé une API qui transmettait les requêtes à une Lambda qui retournait le meilleur film ou série télévisée pour ce genre. Maintenant, nous allons utiliser DynamoDB pour permettre aux utilisateurs de voter pour leur genre préféré.

Si vous n'avez pas lu la première partie de cette série, alors [consultez-la ici](https://medium.freecodecamp.org/building-an-api-with-lambdas-and-api-gateway-11254e23b703) !

### DynamoDB

DynamoDB est une base de données non relationnelle créée par Amazon que nous pouvons utiliser pour stocker les votes des utilisateurs. C'est aussi génial, car nous pouvons y accéder facilement en utilisant le **aws-sdk** qui est préinstallé dans les Lambdas.

La première chose que nous devons faire est de créer une table pour stocker les votes des films. Naviguez vers DynamoDB dans AWS et cliquez sur « Créer une table ».

![Image](https://cdn-media-1.freecodecamp.org/images/gw6O3QWWUiAy784JH5lWIm1K2SVgfq7dNFT9)

![Image](https://cdn-media-1.freecodecamp.org/images/HyNfOnvaam0CEq7vhE-YBZZ9lWcdHDBtJEZT)

Sur la page suivante, nous nommerons notre table et fournirons une clé primaire. La clé primaire doit être unique afin que nous n'ayons pas deux enregistrements avec la même clé. Nous pouvons appeler la table « movie-api » et définir la clé primaire sur « movie-genre », car chaque film ne doit apparaître qu'une fois dans chaque genre.

Nous avons maintenant configuré tout ce dont nous avons besoin dans DynamoDB, donc nous pouvons revenir à notre code.

### Ajout d'un gestionnaire Dynamo

L'obtention et la mise à jour des données dans une table Dynamo se font en utilisant le `documentClient` sur **aws-sdk**, mais la structure des requêtes est très spécifique. Pour nous faciliter la vie, nous pouvons créer un gestionnaire Dynamo pour faire tout le formatage.

Commencez par créer un nouveau fichier appelé « dynamo.js » dans la Lambda « movieAPI ». Dans ce fichier, nous commençons par importer **aws-sdk** et créer notre `documentClient`.

```
const AWS = require('aws-sdk');
```

```
let documentClient = new AWS.DynamoDB.DocumentClient({    'region': 'eu-west-1'});
```

Nous voulons maintenant créer et exporter une classe qui a trois méthodes : un `get`, un `write`, et un `update`.

```
module.exports = class DB {    get(key, value, table) {}    write(ID, data, table) {}    async increment(ID, table) {}}
```

Nous commencerons par créer notre méthode `get`. La première chose que nous devons faire est de vérifier que nous avons une `key`, une `value` et une `table` valides.

```
if (!table) throw 'table nécessaire';if (typeof key !== 'string') throw `key n'était pas une chaîne et était ${JSON.stringify(key)} sur la table ${table}`;if (typeof value !== 'string') throw `value n'était pas une chaîne et était ${JSON.stringify(value)} sur la table ${table}`;
```

Parce que nous voulons que cette méthode soit basée sur des promesses, nous devons retourner une `new Promise`.

```
return new Promise((resolve, reject) => {})
```

Pour obtenir des données de Dynamo, nous devons passer un ensemble de paramètres au client de document. Ces paramètres doivent inclure `TableName` et `Key`.

```
let params = {    TableName: table,    Key: {[key]: value}};
```

Nous passons ces **params** à `documentClient` et ensuite `reject` s'il y a une erreur ou `resolve` s'il n'y en a pas.

```
documentClient.get(params, function(err, data) {    if (err) {        console.log(`Il y a eu une erreur lors de la récupération des données pour ${key} ${value} sur la table ${table}`, err);        return reject(err);    }    return resolve(data.Item);});
```

Un processus similaire est fait pour la méthode `write`. Nous vérifions que les **paramètres** sont valides, créons les **paramètres**, et les passons à `documentClient`.

```
return new Promise((resolve, reject) => {    if (typeof ID !== 'string') throw `l'id doit être une chaîne et non ${ID}`;    if (!data) throw "les données sont nécessaires";    if (!table) throw 'le nom de la table est nécessaire';
```

```
    let params = {        TableName: table,        Item: { ...data, ID: ID }    };
```

```
    documentClient.put(params, function(err, result) {        if (err) {            console.log("Erreur dans writeForCall lors de l'écriture des messages dans dynamo :", err);            console.log(params);            return reject(err);        }        console.log('a écrit des données dans la table ', table)        return resolve({ ...result.Attributes, ...params.Item });    });});
```

La méthode `increment` est beaucoup plus facile. Pour incrémenter, nous essayons d'obtenir les données pour cette clé, augmentons le compte de un, puis l'écrivons à nouveau dans la base de données. Si nous ne pouvons pas obtenir les données, ou s'il n'y a pas de compte sur les données, alors nous supposons que nous devons définir le compte à 0.

```
async increment(ID, table) {    if (!table) throw 'table nécessaire';    if (!ID) throw 'ID nécessaire';    let data;    try {        data = await this.get('movie-genre', ID, table);        if (!data.count) throw 'aucun compte dans les données'    } catch (err) {            data = { "movie-genre": ID, count: 0 };    };    let newData = { ...data, count: data.count + 1 };    return this.write(ID, newData, table);}
```

### Modification de notre Lambda

Maintenant que nous avons un moyen facile d'obtenir, d'écrire et de mettre à jour notre table Dynamo, nous pouvons l'utiliser pour permettre à nos utilisateurs de voter. Dans « index.js », nous devons d'abord importer notre nouvelle classe Dynamo et créer une instance de celle-ci.

```
const DB = require('./dynamo');const Dynamo = new DB();
```

Maintenant, à l'intérieur de notre `putMovie`, nous pouvons ajouter la logique pour permettre aux utilisateurs de voter. Les deux choses que nous devons obtenir sont `movie` du corps et `genre` des paramètres de chemin. Nous les combinons ensuite pour créer notre ID `movie-genre`. Cela est ensuite passé à `Dynamo.increment` avec un nom de table de `movie-api` et notre `putMovie` est complet.

```
const putMovie = async event => {    let { movie } = JSON.parse(event.body);    let genre = event.pathParameters.genre;    let ID = `${movie}-${genre}`;    return Dynamo.increment(ID, 'movie-api')}
```

Pour que cela fonctionne lorsque nous recevons la requête `Put`, nous devons légèrement modifier notre fonction de gestionnaire de base.

```
if (event.httpMethod === 'PUT') {    let response = await putMovie(event)    return done(response);}
```

Parce que nous avons ajouté **AWS** à notre Lambda, nous devons exécuter `npm init` puis `npm install --save aws-sdk` dans le dossier Lambda. Cela peut être fait localement et téléchargé, ou fait en utilisant Cloud9.

### Ajout de la méthode API Gateway

Avec la nouvelle fonction, nous pouvons ajouter une nouvelle méthode à notre API. Dans API Gateway, nous pouvons sélectionner notre « movieAPI » puis sélectionner « /movies/{genre} ». Cliquez sur « Actions » -> « Créer une méthode » et choisissez d'ajouter une méthode « PUT ».

![Image](https://cdn-media-1.freecodecamp.org/images/nkKXDo9fZIwCBmib5CuBVhOuPYgt5kCxuF7b)

Ce « PUT » peut être dirigé vers notre « movieAPI », et cocher « Utiliser l'intégration Lambda Proxy ». Une fois sauvegardé, nous pouvons le tester. Sur la méthode, nous pouvons cliquer sur « TEST » et entrer un genre et un corps contenant un film. Lorsque nous cliquons sur « TEST », nous obtenons une réponse contenant le film et le nouveau compte. Comme il s'agit du premier vote, le compte sera de 1.

![Image](https://cdn-media-1.freecodecamp.org/images/22fOgFeE-f4fu84NrhXqW3NDtfYjCpiDfMCO)

![Image](https://cdn-media-1.freecodecamp.org/images/Z6vdhExeuNJFJQCoAZZcHdndLzjRy3hmxu0I)

![Image](https://cdn-media-1.freecodecamp.org/images/mLrC1ijul84nx3VvTJsjo6RFIZCjQqHIHQ7e)

L'exécution du test une deuxième fois incrémentera maintenant les votes pour ce film de un.

![Image](https://cdn-media-1.freecodecamp.org/images/ZriL39b1A9v2MyEFt4Zlk7oat5jHGVrT6DZj)

### Modification de la méthode _GET_

Maintenant que nous avons un nouveau système de vote, nous pouvons mettre à jour notre « GET » pour utiliser ces nouvelles données. Nous devons obtenir tous les films qui sont dans le genre demandé et les lister par ordre de votes.

Nous devons d'abord créer une nouvelle méthode dynamo. Cette méthode scannera chacune des entrées et sélectionnera celles qui correspondent à nos critères.

```
scan(key, value, table) {    return new Promise((resolve, reject) => {        let params = {             TableName: table,             FilterExpression: `${key} = :value`,             ExpressionAttributeValues: { ':value': value }         };         documentClient.scan(params, function(err, data) {             if (err) reject(err);             resolve(data);         });    });}
```

Nous pouvons maintenant modifier notre fonction `getMovie` pour utiliser cette nouvelle méthode Dynamo. Nous devons passer le genre, le film sélectionné et le compte actuel.

```
const getMovie = async event => {    let genre = event.pathParameters.genre;    let data = await Dynamo.scan('genre', genre, 'movie-api');    let result = data.Items.sort((a,b) => b.count - a.count);    result = result.map(({count, ID, genre})=> { return {count, ID, genre}});    return data;}
```

La dernière chose à faire est d'ajouter un `await` avant notre fonction `getMovie` pour qu'elle gère le scan de la base de données asynchrone.

```
let response = await getMovie(event);
```

#### Test

Lorsque nous appelons ce nouveau point de terminaison « GET », nous recevons une liste ordonnée de tous les films dans la base de données.

```
[  {    "count": 2,    "ID": "Desperado (1995)-action",    "genre": "action"  },  {    "count": 1,    "ID": "Team America (2004)-action",    "genre": "action"  }]
```

### Résumé

Nous avons maintenant construit une API qui peut gérer les requêtes « GET » et « PUT », stocker et récupérer des données d'une base de données Dynamo. Vous pouvez également réutiliser une grande partie du code de la classe Dynamo pour d'autres API qui fonctionnent avec Dynamo.

### Vous voulez vous entraîner ?

Si vous avez aimé cela, pourquoi ne pas essayer de mettre en place un système similaire pour les émissions de télévision ? Si vous le faites, faites-moi savoir comment cela se passe !

Vous pouvez également améliorer cette API en vous assurant que `Desperado (1995)` et `desperado (1995)` comptent pour le même film, ou en n'autorisant qu'un certain format de titre de film.

Si vous avez aimé cela, alors assurez-vous de l'applaudir et de vous abonner pour plus de tutoriels et de guides Amazon. **À la prochaine et continuez à coder !**

![Image](https://cdn-media-1.freecodecamp.org/images/SClwEaQxE4CUJ6oJviWTugWNaGOAH4Xxqohh)