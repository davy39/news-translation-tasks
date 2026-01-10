---
title: 'Les tableaux PHP en pratique : comment reconstruire le projet de cartes d''équipe
  de football avec PHP et MongoDB'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2024-06-18T20:58:07.000Z'
originalURL: https://freecodecamp.org/news/php-arrays-how-to-rebuild-the-football-team-cards-with-php-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/PHP-Arrays-in-Practice-Cover.png
tags:
- name: arrays
  slug: arrays
- name: handbook
  slug: handbook
- name: MongoDB
  slug: mongodb
- name: PHP
  slug: php
seo_title: 'Les tableaux PHP en pratique : comment reconstruire le projet de cartes
  d''équipe de football avec PHP et MongoDB'
seo_desc: 'This is the second part of my PHP array handbook. You can find the first
  part here, where I cover array basics.

  In the first part, you learned about arrays, how to create arrays, array functions,
  and how to loop through arrays.

  This second part will ...'
---

Ceci est la deuxième partie de mon manuel sur les tableaux PHP. Vous pouvez [trouver la première partie ici](https://www.freecodecamp.org/news/php-array-handbook/), où je couvre les bases des tableaux.

Dans la première partie, vous avez appris les tableaux, comment créer des tableaux, les fonctions de tableau et comment parcourir les tableaux.

Cette deuxième partie vous apprendra à utiliser PHP et MongoDB pour reconstruire le projet de cartes d'équipe de football du programme JavaScript mis à jour de freeCodeCamp.

Les données de l'équipe de football seront stockées dans une base de données MongoDB Atlas. Nous les récupérerons sous forme de tableau et les afficherons en fonction des joueurs sélectionnés (gardiens de but, défenseurs, milieux de terrain et attaquants).

Cela vous aidera à construire sur ce que vous avez appris sur le parcours des tableaux. Après tout, à de nombreuses occasions, vous parcourrez ce que vous obtenez d'une base de données ou d'une API, pas nécessairement des tableaux codés en dur.

Afin de ne pas vous choquer en passant directement des tableaux aux bases de données, nous commencerons par ce que sont les données et les bases de données, puis nous passerons à l'apprentissage de :

* Bases de données relationnelles vs non relationnelles

* Comment utiliser MongoDB Atlas

* Comment installer MongoDB pour PHP sur un Mac

* Comment configurer MongoDB Atlas

* Comment construire une application CRUD avec PHP et MongoDB Atlas

* Et enfin, comment reconstruire le projet de cartes d'équipe de football avec PHP et MongoDB Atlas

## Prérequis

Pour tirer le meilleur parti de ce guide, je vous suggère d'avoir une connaissance de base des éléments suivants :

* Fondamentaux de PHP (variables, tableaux, fonctions, boucles)

* HTML et CSS

* Événements JavaScript

* Ligne de commande

* Composer

* Comment configurer un environnement de développement PHP avec VS Code

* Bases de données

* MongoDB Atlas

* Git et GitHub

## Table des matières

* [Qu'est-ce que les données et les bases de données ?](#heading-quest-ce-que-les-donnees-et-les-bases-de-donnees)

* [Bases de données relationnelles vs non relationnelles](#heading-bases-de-donnees-relationnelles-vs-non-relationnelles)

  * [MongoDB Atlas – Un exemple de base de données non relationnelle](#heading-mongodb-atlas-un-exemple-de-base-de-donnees-non-relationnelle)

* [Comment installer MongoDB pour PHP](#heading-comment-installer-mongodb-pour-php)

  * [Étape 1 : Installer l'extension MongoDB avec PECL (Bibliothèque communautaire d'extensions PHP)](#heading-etape-1-installer-lextension-mongodb-avec-pecl-bibliotheque-communautaire-dextensions-php)

  * [Étape 2 : Modifier le fichier `php.ini` pour inclure l'extension MongoDB](#heading-etape-2-modifier-le-fichier-phpini-pour-inclure-lextension-mongodb)

  * [Étape 3 : Vérifier l'installation de l'extension MongoDB](#heading-etape-3-verifier-linstallation-de-lextension-mongodb)

  * [Étape 4 : Configurer un cluster MongoDB Atlas](#heading-etape-4-configurer-un-cluster-mongodb-atlas)

  * [Étape 5 : Installer la bibliothèque PHP MongoDB](#heading-etape-5-installer-la-bibliotheque-php-mongodb)

* [Opérations CRUD utilisant PHP et MongoDB](#heading-operations-crud-utilisant-php-et-mongodb)

  * [Étape 1 : Installer la bibliothèque MongoDB et le package Dotenv](#heading-etape-1-installer-la-bibliotheque-mongodb-et-le-package-dotenv)

  * [Étape 2 : Créer un fichier `.env` pour vos informations d'identification URI MongoDB Atlas](#heading-etape-2-creer-un-fichier-env-pour-vos-informations-didentification-uri-mongodb-atlas)

  * [Étape 3 : Créer un fichier de connexion à la base de données](#heading-etape-3-creer-un-fichier-de-connexion-a-la-base-de-donnees)

  * [Étape 4 : La partie `READ` du CRUD](#heading-etape-4-la-partie-read-du-crud)

  * [Étape 5 : La partie `CREATE` du CRUD](#heading-etape-5-la-partie-create-du-crud)

  * [Étape 6 : La partie `UPDATE` du CRUD](#heading-etape-6-la-partie-update-du-crud)

  * [Étape 7 : La partie `DELETE` du CRUD](#heading-etape-7-la-partie-delete-du-crud)

* [Projet : Comment utiliser PHP pour reconstruire le projet de cartes d'équipe de football du programme JavaScript mis à jour](#heading-projet-comment-utiliser-php-pour-reconstruire-le-projet-de-cartes-dequipe-de-football-du-programme-javascript-mis-a-jour)

  * [Étape 1 : Configurer MongoDB Atlas](#heading-etape-1-configurer-mongodb-atlas)

  * [Étape 2 : Installer les dépendances du projet avec Composer](#heading-etape-2-installer-les-dependances-du-projet-avec-composer)

  * [Étape 3 : Créer les fichiers du projet](#heading-etape-3-creer-les-fichiers-du-projet)

  * [Étape 4 : Envelopper la balise `select` dans un élément `form`](#heading-etape-4-envelopper-la-balise-select-dans-un-element-form)

  * [Étape 5 : Créer la logique pour récupérer les footballeurs de la collection `footballers`](#heading-etape-5-creer-la-logique-pour-recuperer-les-footballeurs-de-la-collection-footballers)

  * [Étape 6 : Créer la logique pour filtrer les footballeurs en fonction de leur position](#heading-etape-6-creer-la-logique-pour-filtrer-les-footballeurs-en-fonction-de-leur-position)

  * [Étape 7 : Afficher les joueurs sur la page en fonction de la position sélectionnée](#heading-etape-7-afficher-les-joueurs-sur-la-page-en-fonction-de-la-position-selectionnee)

* [Conclusion](#heading-conclusion)

## Qu'est-ce que les données et les bases de données ?

Les données sont au cœur de presque tout dans le monde moderne. Les personnes que vous voyez sur les réseaux sociaux et autres sites web, le contenu qu'elles publient, les commentaires qu'elles ajoutent aux publications, et de nombreuses autres activités en ligne produisent toutes beaucoup de données. Même les dossiers des patients dans un hôpital ou la paie d'une entreprise hébergée sur un serveur local sont des données. Les données n'ont pas besoin d'être sur Internet.

Pour gérer et utiliser efficacement les données pour la croissance, vous avez besoin d'une **base de données**. Une **base de données** est une collection structurée de données qui vous aide à stocker, récupérer et manipuler ces données de manière efficace.

Les bases de données se présentent sous deux types principaux – les bases de données relationnelles et non relationnelles. Nous allons discuter des différences entre elles ensuite.

Les bases de données relationnelles et non relationnelles sont gérées avec ce qu'on appelle des systèmes de gestion de bases de données (SGBD). Un SGBD est une interface entre l'utilisateur et la base de données qui vous permet de créer, lire, mettre à jour et supprimer des données dans la base de données.

## Bases de données relationnelles vs non relationnelles

### Qu'est-ce que les bases de données relationnelles ?

Les **bases de données relationnelles** organisent les données dans des tables composées de lignes et de colonnes. Chaque table représente une entité spécifique, telle que des clients ou des produits. Les colonnes définissent les attributs de ces entités, comme le nom du client ou le nom du produit.

Le modèle relationnel utilise le langage de requête structuré (SQL) pour interroger et gérer les données. Les relations entre les tables sont établies par des clés primaires et étrangères pour assurer l'intégrité des données et réduire la redondance.

Les bases de données relationnelles sont connues pour leur robustesse, leur cohérence et leur support pour les requêtes complexes. Elles sont bien adaptées pour les applications qui nécessitent des transactions multi-lignes, comme les systèmes financiers, les logiciels de planification des ressources d'entreprise (ERP) et les systèmes de gestion de la relation client (CRM).

Des exemples de bases de données relationnelles sont MySQL, PostgreSQL et Microsoft SQL Server.

### Qu'est-ce que les bases de données non relationnelles ?

Les **bases de données non relationnelles** stockent et gèrent les données dans des formats flexibles et sans schéma, comme des paires clé-valeur, des documents, des colonnes larges ou des graphes. Elles sont également connues sous le nom de bases de données NoSQL car elles n'utilisent pas SQL comme les bases de données relationnelles.

Les bases de données non relationnelles sont conçues pour évoluer horizontalement, ce qui les rend idéales pour le traitement de données à grande échelle et les applications web en temps réel.

Les bases de données non relationnelles sont faciles à utiliser, évolutives et performantes en même temps. En raison de cela, elles sacrifient souvent un certain degré de cohérence en faveur de la disponibilité et de la tolérance aux partitions.

Les cas d'utilisation courants incluent l'analyse en temps réel, les applications web en temps réel et les applications nécessitant une ingestion de données à haute vitesse.

### MongoDB Atlas – Un exemple de base de données non relationnelle

MongoDB Atlas est une base de données non relationnelle qui stocke les données dans un format orienté document similaire à JSON appelé BSON (Binary JSON). BSON étend le modèle JSON pour fournir des types de données supplémentaires et pour être efficace pour l'encodage et le décodage dans divers langages de programmation.

MongoDB Atlas offre la flexibilité et l'évolutivité de MongoDB, avec les avantages du déploiement automatisé, des sauvegardes et de la surveillance. Il permet aux développeurs de se concentrer sur la construction d'applications sans se soucier de la gestion de la base de données.

MongoDB Atlas prend également en charge des fonctionnalités avancées telles que le partitionnement des données, la réplication et la distribution mondiale. Cela en fait un choix puissant pour les applications modernes nécessitant flexibilité et performance.

## Comment installer MongoDB pour PHP

Avant de pouvoir installer MongoDB pour PHP, assurez-vous d'avoir PHP lui-même installé correctement.

Sur un Mac, vous pouvez installer PHP avec homebrew en exécutant `brew install PHP`. En plus de cela, assurez-vous d'avoir Apache installé en exécutant `brew install httpd` et démarrez-le en exécutant `brew services start httpd`.

Vous pouvez suivre les étapes ci-dessous pour installer MongoDB pour PHP sur un Mac.

### Étape 1 : Installer l'extension MongoDB avec PECL (Bibliothèque communautaire d'extensions PHP)

Installez l'extension MongoDB pour PHP en exécutant `pecl install mongodb`.

### Étape 2 : Modifier le fichier `php.ini` pour inclure l'extension MongoDB

L'installation de l'extension MongoDB devrait automatiquement ajouter les configurations nécessaires au fichier `php.ini`. Mais si ce n'est pas le cas, localisez le fichier `php.ini` en exécutant la commande suivante :

```bash
$ php --ini
Configuration File (php.ini) Path: /usr/local/etc/php/8.3
```

Après cela, collez ce qui suit à la fin du fichier `php.ini` et enregistrez-le :

```bash
extension=mongodb.so
```

Après avoir fait cela, redémarrez Apache en exécutant `brew services restart httpd`.

### Étape 3 : Vérifier l'installation de l'extension MongoDB

Exécutez la commande suivante pour voir si l'extension PHP a été installée avec succès :

```bash
php -i | grep mongo
```

Vous devriez voir quelque chose comme ceci dans le terminal :

![Screenshot-2024-05-24-at-09.21.50](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.21.50.png align="left")

Consultez [la documentation MongoDB PHP](https://www.mongodb.com/docs/languages/php/) pour plus d'informations sur l'utilisation de MongoDB avec PHP et des frameworks comme Laravel et Symfony.

### Étape 4 : Configurer un cluster MongoDB Atlas

Pour tester l'extension PHP que vous venez d'installer, vous avez besoin d'une base de données MongoDB. Atlas facilite cela pour vous car le travail lourd est géré dans le cloud.

#### 1. Connectez-vous à votre compte MongoDB

Rendez-vous sur https://cloud.mongodb.com/ et connectez-vous à votre compte. Si vous n'avez pas de compte, **vous pouvez en créer un gratuitement**.

#### 2. Créer un projet

Si vous avez des projets existants, créez un nouveau projet en cliquant sur la flèche à droite du projet actuellement ouvert et en sélectionnant "Nouveau projet".

![Screenshot-2024-05-24-at-09.34.05](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.34.05.png align="left")

Donnez un nom à votre projet et cliquez sur le bouton "Suivant".

![Screenshot-2024-05-24-at-09.37.13](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.37.13.png align="left")

Cliquez sur "Créer un projet" pour enfin créer le projet.

![Screenshot-2024-05-24-at-09.38.29](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.38.29.png align="left")

#### 3. Créer un cluster

Après avoir créé un projet, vous devriez être invité à créer un cluster. Si ce n'est pas le cas, assurez-vous d'être dans l'onglet Vue d'ensemble. À partir de là, cliquez sur le grand bouton "Créer" :

![create-giant-1](https://www.freecodecamp.org/news/content/images/2024/06/create-giant-1.png align="left")

Sélectionnez le niveau gratuit "MO", donnez un nom à votre cluster et cliquez sur le bouton "Créer un déploiement".

![Screenshot-2024-05-24-at-09.44.11](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.44.11.png align="left")

J'ai donné au cluster le nom `movie-list`.

Gardez simplement à l'esprit que, à mesure que votre base de données grandit, vous devrez peut-être passer à l'un des niveaux payants.

#### 4. Créer un utilisateur de base de données

Immédiatement après avoir créé votre cluster, vous serez invité à créer un utilisateur de base de données. Remplissez le nom d'utilisateur et le mot de passe de votre utilisateur de base de données et cliquez sur le bouton "Créer un utilisateur de base de données". Ensuite, cliquez sur "Choisir une méthode de connexion".

![Screenshot-2024-05-24-at-09.50.54](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.50.54.png align="left")

Assurez-vous de saisir un mot de passe que vous pouvez retenir ou de l'enregistrer dans un gestionnaire de mots de passe.

#### 5. Choisir une méthode de connexion

Vous verrez plusieurs méthodes que vous pouvez utiliser pour vous connecter au cluster une fois que vous aurez cliqué sur le bouton "Choisir une méthode de connexion".

![Screenshot-2024-05-24-at-09.56.37](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.56.37.png align="left")

Sélectionnez Pilotes dans la liste.

![Screenshot-2024-05-24-at-09.58.02](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-09.58.02.png align="left")

Choisissez PHP dans la liste et sélectionnez PHP Lib 1.9 + MongoDB 1.10 ou une version ultérieure comme version à utiliser. Ensuite, copiez la chaîne de connexion et cliquez sur le bouton "Terminé".

![Screenshot-2024-05-24-at-10.02.55](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.02.55.png align="left")

#### 6. Choisir l'accès réseau

Rendez-vous dans l'onglet "Accès réseau" et sélectionnez "Ajouter une adresse IP", cliquez sur "AUTORISER L'ACCÈS DE N'IMPORTE OÙ", puis cliquez sur le bouton "Confirmer". Vous pouvez modifier cela plus tard en fonction de l'endroit où votre application est déployée.

![Screenshot-2024-05-24-at-10.05.03](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.05.03.png align="left")

Retournez à l'onglet "Base de données" et cliquez sur le bouton "Parcourir les collections".

![Screenshot-2024-05-24-at-10.07.48](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.07.48.png align="left")

Sélectionnez "Charger un jeu de données d'exemple" afin de ne pas avoir à ajouter vos propres données – au moins pour l'instant.

![Screenshot-2024-05-24-at-10.24.54](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.24.54.png align="left")

Vous devriez maintenant voir les bases de données suivantes :

![Screenshot-2024-05-24-at-10.28.04](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.28.04.png align="left")

Pour tester que votre extension MongoDB pour PHP fonctionne, vous pouvez interroger n'importe quelle donnée dans ces bases de données. Mais d'abord, vous devez installer la bibliothèque PHP MongoDB avec `composer`. `composer` vous permet de gérer les dépendances de votre projet PHP.

### Étape 5 : Installer la bibliothèque PHP MongoDB

Si vous n'avez pas `composer` installé, installez-le avec homebrew en exécutant `brew install composer`.

Après cela, créez un dossier et ouvrez-le avec votre éditeur de texte. Si votre éditeur de texte dispose d'un terminal intégré, ouvrez-le et exécutez la commande suivante :

```bash
composer require mongodb/mongodb
```

Si l'installation est réussie, vous verrez un dossier `vendor`, ainsi que les fichiers `composer.json` et `composer.lock` à la racine de votre projet. Vous verrez également ce qui suit dans le terminal :

![Screenshot-2024-05-24-at-10.36.29](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.36.29.png align="left")

Maintenant, vous devez interroger n'importe quelle donnée dans votre base de données atlas et les afficher.

Créez un fichier `index.php` et collez ce qui suit à l'intérieur :

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';

// Votre chaîne de connexion
$client = new MongoDB\Client(
 'mongodb+srv://username:<password>@movie-list.s6r7qkr.mongodb.net/?retryWrites=true&w=majority&appName=movie-list'
);

$movies = $client->selectCollection('sample_mflix', 'movies');
$document = $movies->findOne(['title' => 'Wild and Woolly']);

echo '<pre>';
print_r($document);
```

Le code ci-dessus vous permet de vous connecter à la base de données `movies` dans la collection `sample_mflix` avec la fonction `selectCollection()` et d'interroger un film intitulé "Wild and Bolly" dans celle-ci.

**Note** : Assurez-vous de remplacer la chaîne de connexion existante par la vôtre. Vous l'avez copiée dans l'élément 5 de l'étape 4. Assurez-vous également de remplacer `<password>` par le mot de passe de votre utilisateur de base de données.

Après cela, exécutez votre application PHP (avec `php -S localhost:8000` sur Mac dans le terminal). Si tout est configuré correctement, vous devriez voir ce qui suit dans le navigateur :

![Screenshot-2024-05-24-at-10.54.05](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-24-at-10.54.05.png align="left")

**Note** : J'ai les données bien formatées car j'ai installé l'extension Chrome PHP View. Elle imprime tout ce que vous avez à l'intérieur de la fonction `print_r()` comme cela.

## Opérations CRUD utilisant PHP et MongoDB

Avec MongoDB Atlas pour la gestion de la base de données et la persistance de l'UI, et PHP pour la logique côté serveur, vous pouvez construire une application qui implémente des opérations CRUD complètes – créer, lire, mettre à jour et supprimer.

L'application CRUD particulière que nous construisons est une liste de films. Assurez-vous donc de configurer une base de données Atlas pour celle-ci, comme nous l'avons déjà couvert dans ce guide.

Maintenant, voyons comment vous pouvez construire une application CRUD de liste de films.

### Étape 1 : Installer la bibliothèque MongoDB et le package Dotenv

Assurez-vous d'avoir une extension MongoDB et un package Dotenv pour vous aider à gérer vos variables `.env` en exécutant les commandes suivantes :

```bash
composer require mongodb/mongodb
composer require vlucas/phpdotenv
```

### Étape 2 : Créer un fichier `.env` pour vos informations d'identification URI MongoDB Atlas

Créez un fichier `.env` et ajoutez ce qui suit à l'intérieur :

```md
MDB_URI="Votre chaîne de connexion MongoDB Atlas"
```

### Étape 3 : Créer un fichier de connexion à la base de données

Créez un fichier `mongo_atlas_setup.php` pour la connexion à la base de données à la racine et collez ce qui suit à l'intérieur :

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$client = new MongoDB\Client($_ENV['MDB_URI']);

function getMongoClient()
{
 global $client;
 return $client;
}

function getMongoCollection($database, $collection)
{
 $client = getMongoClient();
 return $client->selectCollection($database, $collection);
}
```

Avec le code ci-dessus, nous :

* chargeons les dépendances requises pour le projet

* chargeons la variable d'environnement

* utilisons une fonction pour obtenir la base de données et la collection que nous voulons à l'intérieur

Importer le fichier et appeler le `getMongoCollection` dans celui-ci avec la base de données et la collection à l'intérieur vous permettra de vous connecter à la base de données et à la collection.

### Étape 4 : La partie `READ` du CRUD

Dans la racine à nouveau, créez un fichier `index.php` qui prendra en charge la partie READ du CRUD. Collez ce qui suit dans le fichier :

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/mongo_atlas_setup.php';

$movies_list = getMongoCollection('movie_list', 'movies');
$movies = $movies_list->find([], ['sort' => ['_id' => -1]]);
?>

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Movie List CRUD App</title>
 <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 p-10">

 <div class="max-w-4xl mx-auto bg-white p-6 rounded shadow">
   <h1 class="text-3xl font-bold mb-4 text-center">Movie List CRUD App</h1>

   <?php include 'create.php' ?>

   <div class="space-y-4">
     <?php foreach ($movies as $movie) : ?>
       <div class="p-4 border rounded shadow-sm bg-gray-50">
         <h2 class="text-2xl font-semibold"><?= $movie['movie_title'] ?></h2>
         <p class="text-gray-700">Year: <?= $movie['movie_year'] ?></p>
         <div class="mt-2">
           <a href="update.php?id=<?= $movie['_id'] ?>" class="bg-yellow-500 text-white py-1 px-3 rounded">Update</a>
           <a href="delete.php?id=<?= $movie['_id'] ?>" onclick="return confirm('Are you sure you want to delete this movie?')" class="bg-red-500 text-white py-1 px-3 rounded">Delete</a>
         </div>
       </div>
     <?php endforeach ?>
   </div>
 </div>

</body>

</html>
```

Remarquez qu'il y a les liens Update et Delete vers des fichiers `update.php` et `delete.php` avec l'id du film cliqué. De cette façon, nous saurons quel film est cliqué afin de le mettre à jour ou de le supprimer. Il y a aussi une instruction include pour un fichier `create.php`.

Pour l'instant, vous pouvez créer les fichiers `create.php`, `update.php` et `delete.php` à la racine.

À ce stade, vous ne verrez encore rien dans l'UI car vous devez gérer la fonctionnalité de création.

### Étape 5 : La partie `CREATE` du CRUD

Créez un fichier `create.php` à la racine (si vous ne l'avez pas déjà fait) et collez ce qui suit à l'intérieur :

```php
<?php
require_once __DIR__ . '/mongo_atlas_setup.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $movies = getMongoCollection('movie_list', 'movies');
 $newMovie = [
   'movie_title' => $_POST['movie-title'],
   'movie_year' => (int)$_POST['movie-year'],
 ];
 $result = $movies->insertOne($newMovie);
 if ($result->getInsertedCount() === 1) {
   // echo "Movie created successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to create movie";
 }
}
?>

<form method="POST" action="create.php" class="space-y-4 mb-6">
 <div>
   <label class="block text-gray-700">Movie Title</label>
   <input type="text" name="movie-title" required class="w-full p-2 border rounded max-w-md">
 </div>
 <div>
   <label class="block text-gray-700">Movie Year</label>
   <input type="text" name="movie-year" required class="w-full p-2 border rounded max-w-md">
 </div>
 <button type="submit" class="bg-green-500 text-white py-2 px-4 rounded">Create</button>
</form>
```

Le code ci-dessus contient le formulaire et les éléments d'entrée pour créer un film. Nous utilisons ensuite les attributs de nom dans ces éléments d'entrée pour créer la requête `POST` qui nous permettra de créer un film et de l'enregistrer dans la collection `movies` d'une base de données `movie_list`.

### Étape 6 : La partie `UPDATE` du CRUD

Pour gérer la mise à jour, nous devons créer un fichier séparé et faire quelque chose de similaire à la création de film. L'exception est que nous allons utiliser le champ id (`_id`) pour déterminer si le film existe et ensuite le mettre à jour au lieu d'en créer un nouveau.

Pour ce faire, créez un fichier `update.php` (si vous ne l'avez pas déjà fait) à la racine et collez ce qui suit à l'intérieur :

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/mongo_atlas_setup.php';

use MongoDB\BSON\ObjectId;

$movies_list = getMongoCollection('movie_list', 'movies');
$title = '';
$year = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $filter = ['_id' => new ObjectId($_POST['id'])];
 
 $update = ['$set' => [
   'movie_title' => $_POST['movie-title'],
   'movie_year' => (int)$_POST['movie-year'],
 ]];
 
 $result = $movies_list->updateOne($filter, $update);
 
 if ($result->getModifiedCount() === 1) {
   // echo "Movie updated successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to update movie.";
 }
} else {
 if (isset($_GET['id'])) {
   $id = $_GET['id'];
   $movie = $movies_list->findOne(['_id' => new ObjectId($id)]);
   if ($movie) {
     $title = $movie['movie_title'];
     $year = $movie['movie_year'];
   } else {
     echo "Movie not found.";
     exit;
   }
 } else {
   echo "No movie ID provided.";
   exit;
 }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <script src="https://cdn.tailwindcss.com"></script>
 <title>Update Movie </title>
</head>

<body class="bg-gray-100 p-10">

 <div class="max-w-4xl mx-auto bg-white p-6 rounded shadow">
   <h1 class="text-3xl font-bold mb-4">Update <?= $title ?> </h1>

   <form method="POST" action="update.php" class="space-y-4">
     <input type="hidden" name="id" value="<?php echo $id; ?>">

     <div>
       <label class="block text-gray-700">Title</label>
       <input type="text" name="movie-title" value="<?= htmlspecialchars($title); ?>" required class="w-full p-2 border rounded" />
     </div>

     <div>
       <label class="block text-gray-700">Release Year</label>
       <input type="number" name="movie-year" value="<?= htmlspecialchars($year); ?>" required class="w-full p-2 border rounded" />
     </div>

     <button class=" bg-green-500 text-white py-2 px-4 rounded" type="submit">Update</button>
   </form>

   <div class="mt-4">
     <a href="index.php" class="bg-gray-500 text-white py-2 px-4 rounded">Back to List</a>
   </div>
 </div>

</body>

</html>
```

### Étape 7 : La partie `DELETE` du CRUD

Pour gérer la fonctionnalité de suppression, nous pouvons obtenir le film et utiliser la fonction `deleteOne` fournie par MongoDB pour le supprimer. Une fois la suppression effectuée, nous utiliserons à nouveau la fonction `header()` pour rediriger vers la page d'accueil.

Collez le code suivant dans votre fichier `delete.php` :

```php
<?php
require_once __DIR__ . '/mongo_atlas_setup.php';

use MongoDB\BSON\ObjectId;

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
 $movies = getMongoCollection('movie_list', 'movies');
 $filter = ['_id' => new ObjectId($_GET['id'])];
 $result = $movies->deleteOne($filter);
 if ($result->getDeletedCount() === 1) {
   // echo "Movie deleted successfully!";
   header('Location: ' . '/');
 } else {
   echo "Failed to delete movie.";
 }
} else {
 echo "No movie provided.";
}
?>
```

Voici à quoi devrait ressembler l'application CRUD maintenant :

![CRUD-gif](https://www.freecodecamp.org/news/content/images/2024/06/CRUD-gif.gif align="left")

Tout le code se trouve dans ce [dépôt GitHub](https://github.com/Ksound22/crud-app-for-php-fcc-article)

## Projet : Comment utiliser PHP pour reconstruire le projet de cartes d'équipe de football du programme JavaScript mis à jour

Avant de commencer à suivre les étapes pour construire le projet, récupérez le code de départ du projet dans [la branche de démarrage de ce dépôt GitHub](https://github.com/Ksound22/football-team-cards-php-rebuild).

Vous pouvez également consulter [le projet de cartes d'équipe de football](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-modern-javascript-methods-by-building-football-team-cards/step-1) pour savoir ce que nous essayons d'accomplir.

### Étape 1 : Configurer MongoDB Atlas

Connectez-vous à votre compte MongoDB Atlas et créez une base de données `football-team-cards`. N'hésitez pas à la créer dans un projet existant ou un nouveau si vous le souhaitez. Dans la base de données `football-team-cards`, créez une collection `footballers`.

Dans la collection `footballers`, cliquez sur le bouton "INSERT DOCUMENT".

![Screenshot-2024-06-09-at-14.33.15](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.33.15.png align="left")

Ensuite, collez le contenu du fichier `footballers.json` dans la branche de démarrage du dépôt GitHub du projet et cliquez sur "Done".

![Screenshot-2024-06-09-at-14.42.47](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.42.47.png align="left")

Après cela, votre collection `footballers` devrait ressembler à ceci :

![Screenshot-2024-06-09-at-14.44.59](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-14.44.59.png align="left")

### Étape 2 : Installer les dépendances du projet avec Composer

Créez un dossier `football-team-cards-php` sur votre ordinateur et ouvrez-le avec votre éditeur de texte préféré. Ouvrez le même dossier dans votre terminal et exécutez les commandes suivantes :

```bash
composer require vlucas/phpdotenv 
composer require mongodb/mongodb
```

### Étape 3 : Créer les fichiers du projet

À l'intérieur du dossier `football-team-cards-php`, créez les fichiers suivants :

* `.env`

* `mongo_atlas_php_setup.php`

* `index.php`

* `styles.css`

Dans le fichier `.env`, vous devriez avoir l'URI MongoDB Atlas :

```bash
MDB_URI="Votre chaîne de connexion MongoDB Atlas"
```

Dans le fichier `mongo_atlas_php_setup.php`, vous devriez vous connecter à la base de données avec ce code :

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


function getMongoClient()
{
 return new MongoDB\Client($_ENV['MDB_URI']);
}


function getMongoCollection($database, $collection)
{
 $client = getMongoClient();
 return $client->selectCollection($database, $collection);
}
```

Dans le code ci-dessus, nous chargeons les variables d'environnement et utilisons une fonction `getMongCollection` pour connecter la base de données. Assurez-vous de remplacer la chaîne de connexion par la vôtre.

Maintenant, chaque fois que vous voulez vous connecter à une base de données, requérez le fichier, puis passez les noms de la base de données et de la collection à la fonction `getMongoCollection`.

Copiez le contenu des fichiers `index.html` et `styles.css` dans la branche de démarrage du dépôt GitHub du projet et collez-les dans vos fichiers `index.php` et `styles.css`.

### Étape 4 : Envelopper la balise `select` dans un élément `form`

Remplacez la balise `select` existante par ce qui suit :

```html
<form method="POST" action="">
     <label class="options-label" for="players">Filter Teammates:</label>
     <select name="position" id="players" onchange="this.form.submit()">
       <option value="all">All Players</option>
       <option value="nickname">Nicknames</option>
       <option value="forward">Position Forward</option>
       <option value="midfielder">Position Midfielder</option>
       <option value="defender">Position Defender</option>
       <option value="goalkeeper">Position Goalkeeper</option>
     </select>
</form>
```

Cela vous permettra de faire une requête `POST` avec l'attribut `name` défini sur `position`. Et avec l'attribut `onchange` de `this.form.submit()`, vous pourrez récupérer les footballeurs en fonction de l'une des options sélectionnées. Plus d'informations à ce sujet plus tard.

### Étape 5 : Créer la logique pour récupérer les footballeurs de la collection `footballers`

```php
require_once __DIR__ . '/mongo_atlas_php_setup.php';

$position = isset($_POST['position']) ? $_POST['position'] : 'all';

$collection = getMongoCollection('football-team-cards', 'footballers');
$team = $collection->findOne(['team' => 'Argentina']);
$players = $team['players']->getArrayCopy();
```

Avec le code ci-dessus, nous :

* importons le fichier de connexion à la base de données

* vérifions les données `POST` avec le nom sur la balise `select` et définissons une valeur par défaut de `all` (la première option dans l'élément select)

* obtenons la base de données et la collection à l'intérieur

* utilisons la méthode `findOne` de MongoDB pour obtenir l'équipe

* et récupérons les données sous forme de tableau avec `getArraCopy()` afin de pouvoir les parcourir

À ce stade, vous pouvez imprimer la variable `$players` avec `print_r()` ou `var_dump()` pour voir à quoi elle ressemble. De mon côté, cela ressemble à ceci lorsque j'ai exécuté l'application avec `php -S localhost:4000` :

![Screenshot-2024-06-09-at-16.24.47](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-at-16.24.47.png align="left")

### Étape 6 : Créer la logique pour filtrer les footballeurs en fonction de leur position

Rappelons que nous devons afficher les joueurs en fonction de leur position (gardiens de but, défenseurs, milieux de terrain ou attaquants). Pour ce faire, nous pouvons utiliser le code ci-dessous :

```php
$filteredPlayers = $players;


if ($position !== 'all') {
 if ($position === 'nickname') {
   $filteredPlayers = array_filter($players, function ($player) {
     return !empty($player['nickname']);
   });
 } else {
   $filteredPlayers = array_filter($players, function ($player) use ($position) {
     return $player['position'] === $position;
   });
 }
}
```

Au début, nous initialisons `$filteredPlayers` à tous les joueurs. Si la position sélectionnée n'est pas `all`, nous filtrons les joueurs en fonction du `nickname`. Et si la position sélectionnée n'est pas `nickname`, nous filtrons les joueurs pour n'inclure que ceux dont la position correspond à la position sélectionnée.

### Étape 7 : Afficher les joueurs sur la page en fonction de la position sélectionnée

Maintenant, tout ce que nous devons faire est de définir la valeur de chaque option (tous les joueurs, gardiens de but, défenseurs, milieux de terrain, attaquants) à `selected` si cette option est sélectionnée. Après cela, nous devons utiliser une boucle `foreach` pour effectuer l'affichage approprié.

Voici une façon de définir la valeur de chaque `option` à `selected` :

```php
<option value="all" <?= $position === 'all' ? 'selected' : '' ?>>All Players</option>
       <option value="nickname" <?= $position === 'nickname' ? 'selected' : '' ?>>Nicknames</option>
       <option value="forward" <?= $position === 'forward' ? 'selected' : '' ?>>Forwards</option>
       <option value="midfielder" <?= $position === 'midfielder' ? 'selected' : '' ?>>Midfielders</option>
       <option value="defender" <?= $position === 'defender' ? 'selected' : '' ?>>Defenders</option>
       <option value="goalkeeper" <?= $position === 'goalkeeper' ? 'selected' : '' ?>>Goalkeepers</option>
```

Et voici comment vous pouvez utiliser la boucle `foreach` pour enfin afficher les joueurs sélectionnés :

```php
<div class="cards" id="player-cards">
     <?php if (empty($filteredPlayers)) : ?>
       <p>No players found for the selected position.</p>
     <?php else : ?>
       <?php foreach ($filteredPlayers as $players) : ?>
         <div class="player-card">
           <h2><?= $players['name'] . ($players['isCaptain'] ? ' (Captain)' : '') ?></h2>
           <p>Position: <?= $players['position'] ?></p>
           <p>Number: <?= $players['number'] ?></p>
           <p>Nickname: <?= !empty($players['nickname']) ? $players['nickname'] : 'N/A' ?></p>
         </div>
       <?php endforeach ?>
     <?php endif ?>
   </div>
```

Maintenant, tout fonctionne comme prévu :

![football-team-cards](https://www.freecodecamp.org/news/content/images/2024/06/football-team-cards.gif align="left")

Vous pouvez récupérer le code final du projet dans la branche principale de ce [dépôt GitHub](https://github.com/Ksound22/football-team-cards-php-rebuild).

## Conclusion

Reconstruire le projet de cartes d'équipe de football avec PHP et MongoDB Atlas montre à quel point il peut être puissant et flexible de combiner le scripting côté serveur avec une base de données NoSQL basée sur le cloud.

Le projet met non seulement en évidence la manière dont PHP et MongoDB Atlas fonctionnent ensemble en douceur, mais il montre également les avantages de l'utilisation d'une base de données basée sur le cloud comme Atlas. Atlas offre une évolutivité, une haute disponibilité et une gestion facile, ce qui en fait un excellent choix pour les applications web modernes.

Quelle que soit l'application pilotée par les données que vous créez, ces techniques que nous avons utilisées ici pour construire le projet et l'application CRUD initiale peuvent vous aider.

Bonne programmation !