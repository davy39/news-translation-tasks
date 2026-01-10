---
title: Comment optimiser les requêtes de recherche dans MongoDB
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-01-10T21:12:23.000Z'
originalURL: https://freecodecamp.org/news/optimize-search-queries-in-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/mongosearch.jpg
tags:
- name: MongoDB
  slug: mongodb
- name: search
  slug: search
seo_title: Comment optimiser les requêtes de recherche dans MongoDB
seo_desc: 'Searching through a database to extract relevant data can be quite cumbersome
  if you don''t have – or know how to use – the right tools.

  MongoDB is a non-relational, no-SQL database that differs from relational SQL-based
  databases such as PostgresSQL,...'
---

Rechercher dans une base de données pour extraire des données pertinentes peut être assez fastidieux si vous n'avez pas – ou ne savez pas utiliser – les bons outils.

MongoDB est une base de données non relationnelle, no-SQL qui diffère des bases de données SQL relationnelles telles que PostgresSQL, MySQL.

Ces bases de données SQL utilisent des lignes et des colonnes conventionnelles pour afficher les données, tandis que MongoDB utilise des collections. En raison de cette distinction primaire, il est important pour vous de comprendre certains termes spécifiques à MongoDB.

L'inspiration pour ce tutoriel est venue d'un projet personnel. Je devais implémenter une fonctionnalité qui nécessitait une opération de requête complexe dans MongoDB. En parcourant la documentation MongoDB concernant ce problème, je me suis encore plus confus et je n'ai pas réussi à comprendre.

Après avoir consulté plusieurs sites web et livres, j'ai finalement réussi à le faire. Donc, dans ce tutoriel, mon objectif est de simplifier les opérations de recherche complexes dans MongoDB pour vous, en tant qu'utilisateur plus récent de MongoDB.

J'espère que cet article répond à vos questions brûlantes et vous aide à naviguer dans les opérations de requête MongoDB.

Avant de commencer, voici quelques prérequis importants pour ce tutoriel :

* Connaissance de base de Node.js
* Connaissance de base de MongoDB
* Connaissance des commandes MongoDB
* Connaissance de Postman

## Qu'est-ce que les requêtes MongoDB ?

Les requêtes sont des commandes que vous utilisez pour obtenir des données d'une base de données MongoDB. Elles fonctionnent de manière similaire au système de requête SQL, mais elles opèrent différemment en termes de syntaxe.

Une requête SQL conventionnelle ressemble à ceci :

```
"SELECT * FROM db.Users" (SQL) vs "db.collection.find()" (MONGO DB)

```

Cette commande vous permet d'obtenir toutes les données stockées dans la base de données Users.

De nombreux opérateurs de requête peuvent être utilisés sur une collection de base de données MongoDB pour obtenir des informations pertinentes. Mais je vais éclairer davantage quelques-uns pertinents dans ce tutoriel.

### Exemples de requêtes MongoDB

Maintenant, je vais expliquer certains des opérateurs de requête disponibles dans MongoDB. Vous pouvez exécuter les exemples de code fournis ci-dessous dans l'interface de ligne de commande MongoDB pour voir comment ils fonctionnent.

`Find()` : Cet opérateur retourne tous les documents d'une collection. Vous pouvez tester cela en exécutant ;

```
Db.collection.find()

```

Dans ce cas, remplacez `collection` par le nom réel de la collection que vous souhaitez rechercher.

`findOne()` : cet opérateur de requête retourne le premier document d'une collection qui correspond au filtre attaché à l'opérateur.

```
Db.collection.findOne()

```

`Aggregate()` : Cet opérateur compile les résultats de divers documents dans une collection donnée. Vous pouvez le combiner avec d'autres opérateurs de requête pour organiser les résultats et regrouper diverses données efficacement.

Vous verrez un exemple de la façon d'utiliser cet opérateur avec les opérateurs de requête limit et sort.

`limit()` : Cet opérateur limite le nombre total de résultats de recherche attendus au nombre spécifié.

```
db.collection.aggregate([{ $limit: 6 }]);
```

Ce code ci-dessus limite le nombre total de données agrégées à seulement 6.

`Sort()` : Cet opérateur trie les résultats de la requête de recherche dans l'ordre croissant ou décroissant.

```
db.collection.aggregate([
  { $sort: { fieldName: 1 } } // Remplacez 'fieldName' par le nom réel du champ et utilisez 1 pour l'ordre croissant ou -1 pour l'ordre décroissant
]);

```

Vous pouvez tester ces opérateurs de requête dans une application web standard. Il existe de nombreux outils de programmation disponibles pour développer des applications, mais dans ce tutoriel, nous utiliserons Node.js car il est moins complexe à utiliser et facilement compatible avec l'application de base de données MongoDB.

## Comment implémenter des requêtes de recherche dans MongoDB en utilisant Node.js

Node.js est un langage backend basé sur JavaScript, et ce sera notre langage de prédilection pour l'utilisation de MongoDB dans ce tutoriel.

Maintenant, nous allons écrire du code pour rechercher des documents en utilisant le framework backend Node.js Express.

Mongoose servira de connexion entre MongoDB et Node. Mais avant de nous plonger dedans, qu'est-ce que Mongoose ?

### Qu'est-ce que Mongoose ?

Mongoose est un outil populaire de mapping objet-relationnel (ORM) qui aide à établir une connexion efficace entre la base de données (MongoDB) et le langage de programmation orienté objet (Node.js/JavaScript).

Il fournit des fonctionnalités étendues telles que la modélisation des données, le développement de schémas, l'authentification des modèles et la gestion des données, ce qui simplifie les interactions entre l'API web et la base de données.

Vous pouvez également l'utiliser pour interagir avec d'autres bases de données telles que Redis, MySQL et Postgres.

Maintenant, installons Mongoose.

```
npm install mongoose

```

Pour le connecter à MongoDB dans une application Node.js, utilisez le code suivant :

```
const mongoose = require("mongoose");

mongoose.connect('mongodb://localhost/location', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  autoIndex: true
})
  .then(() => {
    console.log("Connecté à MongoDB");
  })
  .catch((err) => {
    console.error(err);
  });

```

Ce code initie une connexion avec la base de données MongoDB et maintient la connexion pour permettre l'échange de données avec l'application backend.

## Comment rechercher dans des documents dans MongoDB

Dans cette section, nous allons améliorer notre requête de recherche en appliquant certaines des opérations MongoDB que nous avons apprises dans les sections précédentes. Nous allons obtenir des livres dans une base de données en fonction du paramètre `findOne` que nous avons brièvement mentionné précédemment.

Tout d'abord, utilisons l'opérateur `Find()` comme ceci :

```
router.get("/", async (req, res) => {
  try {
    const books = await Book.find();
    res.status(200).json(books);
  } catch (err) {
    res.status(500).json(err);
  }
});

```

Le code ci-dessus demande tous les livres de la base de données. S'il est exécuté avec succès, il retourne un code de statut 200 avec tous les livres de la collection au format JSON. S'il échoue, il retourne un code d'erreur.

Comment nous pouvons appliquer l'opérateur `Limit()` comme ceci :

```
router.get("/", async (req, res) => {
  try {
    let limitedBooks = await Book.find().limit(6);
    res.status(200).json(limitedBooks);
  } catch (err) {
    res.status(500).json(err);
  }
});

```

Ce code est assez similaire au code ci-dessus. Mais il a un opérateur de limite supplémentaire attaché qui limite la réponse attendue aux six premiers livres de la base de données.

Et enfin, nous allons appliquer l'opérateur `FindOne()` :

```
router.get("/", async (req, res) => {
  try {
    let myBook = await Book.findOne({ Author: "Man" });
    res.status(200).json(myBook);
  } catch (err) {
    res.status(500).json(err);
  }
});

```

Dans le code ci-dessus, nous avons essayé de trouver le premier livre écrit par quelqu'un appelé "Man". Si cela trouve avec succès ce document, il retournera un code de succès 200 et le format JSON de cette collection de livres dans la base de données, sinon il retournera un code d'erreur.

## Comment rechercher entre des textes dans MongoDB

Rechercher entre des textes implique une approche plus complexe pour rechercher dans une base de données MongoDB.

Cela implique de rechercher des textes et des phrases dans l'ensemble de la base de données, puis d'afficher les informations des objets contenant ces textes recherchés.

Il est couramment utilisé dans les opérations de recherche complexes afin d'inclure uniquement les informations qui sont regroupées en fonction du prix, des auteurs, de l'adresse, de l'âge ou de toute autre variable commune pertinente.

Alors maintenant, implémentons un opérateur de requête de recherche spécial MongoDB. Nous utiliserons cet opérateur pour rechercher entre des textes et retourner les résultats appropriés.

Le code pour cela est affiché ci-dessous :

```
let myBook = await Book.find({
  "$or": [
    { Author: { $regex: req.params.key } },
    { Title: { $regex: req.params.key } },
  ]
});

```

Ce code ci-dessus utilise le format regex pour aider à localiser des phrases dans la base de données et les retourne. Regex fonctionne sur le principe de correspondance d'un ensemble de chaînes avec des motifs similaires. Cela aide à fournir une réponse plus rapide à nos requêtes de recherche et ne retourne que les documents similaires à notre recherche.

## Conclusion

Avec cela, nous arrivons à la fin du tutoriel. Nous espérons que vous avez appris l'essentiel sur les requêtes de recherche MongoDB et comment exploiter divers opérateurs de recherche pour obtenir les meilleurs résultats possibles de votre base de données.

N'hésitez pas à laisser des commentaires et des questions et à consulter mes autres articles [ici](https://www.freecodecamp.org/news/author/oluwatobi/). Jusqu'à la prochaine fois, continuez à coder.