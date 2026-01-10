---
title: Comment créer un fil d'actualité photo avec .NET et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:41:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-photo-feed-using-net-and-pusher-5c2dae1ee889
coverImage: https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment créer un fil d'actualité photo avec .NET et Pusher
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time photo feed using .NET and Pusher.


  We will build a mini system that allows people to upload their images/photographs
  for everyone to view in real-time. It’s like a mini-Instagram without the comment,...'
---

Par Ogundipe Samuel

Aujourd'hui, nous allons créer un fil d'actualité photo en temps réel en utilisant .NET et Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif)

Nous allons construire un mini système qui permet aux gens de télécharger leurs images/photographies pour que tout le monde puisse les voir en temps réel. C'est comme un mini-Instagram sans les aspects commentaires, likes et vues.

Ça a l'air cool ? C'est parti.

Pour suivre ce tutoriel, assurez-vous d'être familier avec les bases de :

### Création d'un compte et d'une application Pusher

Pusher est un service hébergé qui rend super facile l'ajout de données et de fonctionnalités en temps réel aux applications web et mobiles.

Pusher agit comme une couche en temps réel entre vos serveurs et vos clients. Pusher maintient des connexions persistantes avec les clients (via Websockets si possible et en revenant à une connectivité basée sur HTTP) afin que, dès que vos serveurs ont de nouvelles données qu'ils veulent pousser vers les clients, ils puissent le faire via Pusher.

Nous allons enregistrer une nouvelle application sur le tableau de bord. Les seules options obligatoires sont le nom de l'application et le cluster. Un cluster représente l'emplacement physique du serveur Pusher qui gérera les requêtes de votre application. Sélectionnez également `jQuery` comme technologie front-end et `ASP.NET` comme technologie back-end pour ce tutoriel. Pour d'autres projets, vous pouvez choisir selon vos besoins.

Ensuite, copiez votre App ID, Key et Secret depuis la section `App Keys`, car nous en aurons besoin plus tard.

### Configuration du projet Asp.Net dans Visual Studio

La prochaine chose que nous devons faire est de créer une nouvelle application Asp.Net MVC. Pour ce faire, nous allons :

* Ouvrir Visual Studio et sélectionner un nouveau projet depuis la barre latérale
* Sous les modèles, sélectionner `Visual C#`
* Ensuite, sélectionner web
* Dans la section centrale, sélectionner `ASP.NET MVC Web Application`

Pour ce tutoriel, j'ai nommé le projet : `Real-time-photo-feed`.

Maintenant, nous sommes presque prêts. La prochaine étape sera d'installer la bibliothèque officielle `Pusher` pour .Net en utilisant le `NuGet Package`.

Pour ce faire, nous allons dans outils, via le menu de la barre supérieure, cliquer sur `NuGet Package Manager`. Dans le menu déroulant, nous sélectionnons `Package Manager Console`.

Nous verrons la `Package Manager Console` en bas de notre Visual Studio. Ensuite, installons le package en exécutant :

Alternativement, nous pouvons également installer la bibliothèque `Pusher` en utilisant l'interface utilisateur `NuGet Package Manager`. Pour ce faire, dans l'`Explorateur de solutions`, cliquez avec le bouton droit sur `References` ou un projet et sélectionnez `Manage NuGet Packages`. L'onglet Parcourir affiche les packages disponibles par popularité. Recherchez le package `Pusher` en tapant `PusherServer` dans la boîte de recherche en haut à droite. Sélectionnez le package Pusher pour afficher les informations du package à droite et activer le bouton `Install`.

### Conception de notre application

Maintenant que notre environnement est configuré et prêt, plongeons dans l'écriture de code.

Par défaut, Visual Studio crée trois contrôleurs pour nous. Cependant, nous utiliserons le `HomeController` pour la logique de l'application. La première chose que nous voulons faire est de définir un modèle qui stocke la liste des images que nous avons dans la base de données.

Dans le dossier `models`, créons un fichier nommé `PhotoFeed.cs` et ajoutons le contenu suivant :

Dans le bloc de code ci-dessus, nous avons déclaré un modèle appelé `PhotoFeed` avec trois propriétés principales :

* Id : Il s'agit de la clé primaire de la table du modèle
* Comment : La description de l'image
* Imagepath : Le chemin vers l'image stockée

Maintenant que nous avons défini notre modèle, référençons-le dans notre contexte de base de données par défaut appelé `ApplicationDbContext`. Pour ce faire, ouvrons le fichier `models\IdentityModels.cs`, puis localisons la classe appelée `ApplicationDbContext` et ajoutons ce qui suit après la fonction create :

Dans le bloc de code ci-dessus, la classe `DBSet` représente un ensemble d'entités utilisé pour les opérations de lecture, de mise à jour et de suppression. L'entité que nous utiliserons pour effectuer des opérations CRUD est le modèle `PhotoFeed` que nous avons créé précédemment, et nous lui avons donné le nom `FeedModel`.

### Connexion de notre base de données

Bien que notre modèle soit configuré, nous devons encore attacher une base de données à notre application. Pour ce faire, sélectionnez l'Explorateur de serveurs sur le côté gauche de notre Visual Studio, cliquez avec le bouton droit sur Connexions de données et ajoutez une base de données.

Il existe diverses bases de données qui sont légères et peuvent s'intégrer dans l'application que nous construisons, telles que :

* Base de données Microsoft Access
* Base de données Sqlite
* Serveur MSSQL
* Firebird
* VistaDb

Pour ce tutoriel, j'ai utilisé le Serveur MSSQL.

### Création de notre route d'index

Maintenant que notre modèle et notre base de données sont prêts à fonctionner, créons notre route d'index. Ouvrez le `HomeController` et remplacez-le par le code suivant :

Dans le bloc de code ci-dessus, nous avons défini notre fonction Index pour les requêtes `GET` et `POST`.

Avant de regarder nos fonctions de contrôleur `GET` et `POST`, nous remarquons qu'il y a une importation de notre contexte de base de données dans notre classe avec la ligne qui dit :

Cela permet d'accéder à notre modèle de base de données que nous avons défini en utilisant la classe `DbSet` dans notre classe `ApplicationDbContext`.

Dans la fonction `GET`, nous avons retourné la vue avec laquelle nous allons gérer l'ajout et la mise à jour en temps réel de notre flux.

Remarquez que dans la fonction `GET`, nous passons une variable dans la fonction de vue appelée `me`. Cette variable est une version **interrogeable** de notre modèle `BlogFeed`. Cela sera passé à la vue, qui sera ensuite bouclée et rendue.

Observez que la méthode `POST` est définie pour être asynchrone. Cela est dû au fait que la bibliothèque Pusher .NET utilise l'opérateur await pour attendre la réponse asynchrone des données envoyées à Pusher.

Dans cette fonction, nous ajoutons d'abord notre nouvelle image à la base de données, puis nous déclenchons un événement. Une fois l'événement émis, nous retournons une chaîne ok.

Cependant, veuillez noter que le code ci-dessus ne gérera aucune erreur si l'image a été enregistrée dans la base de données mais n'a pas été publiée en utilisant Pusher. Nous pourrions avoir besoin d'utiliser une instruction try et catch pour gérer les échecs de publication sur Pusher.

### Création de nos fichiers de vue

Ouvrons notre `Views\Home\Index.cshtml` et remplaçons le contenu par ce qui suit :

Dans le bloc de code ci-dessus, nous avons créé notre formulaire qui **comprend** trois éléments principaux, qui sont :

* Entrée de texte pour le commentaire de l'image.
* Entrée de fichier pour sélectionner l'image que nous voulons alimenter.
* Bouton pour enregistrer la nouvelle entrée dans la base de données.

Notez également que nous avons inclus certaines bibliothèques requises telles que :

* Bootstrap CSS
* Bibliothèque JavaScript jQuery
* Bibliothèque JavaScript Pusher

### Liaisons Pusher et extrait jQuery

Voici notre exemple d'extrait jQuery utilisé pour gérer le téléchargement de fichiers et les mises à jour en temps réel de Pusher.

Dans le bloc de code ci-dessus, nous remarquons que nous avons effectué deux activités principales, qui sont :

### Code de téléchargement d'image

Pour traiter le téléchargement d'images du côté client vers le serveur, les étapes suivantes ont été suivies :

* Nous avons attaché un écouteur d'événements à notre bouton d'entrée de fichier qui stocke notre image dans une variable appelée `files`.
* Nous avons défini une fonction appelée `feed_it` qui crée un nouveau `FormData`, puis ajoute notre image et sa description aux données du formulaire. Cette fonction fait ensuite une requête `AJAX POST` à notre route `index`.

### Abonnement aux ajouts de flux sur le serveur depuis d'autres clients

Après que l'image a été envoyée au serveur, une requête est envoyée à Pusher pour retourner un événement avec les nouvelles données que nous avons diffusées. Pour écouter ces événements en temps réel, nous avons :

* Initialisé un objet Pusher tout en passant notre clé d'application et notre cluster.
* Souscrit à notre canal appelé `a_channel`.
* Déclarer une liaison à notre événement appelé `an_event`. Dans la fonction de rappel de cette liaison, nous avons `pré-ajouté` les nouvelles données à notre liste de flux.

C'est tout ! Maintenant, une fois qu'une photo est téléchargée, elle est également diffusée et nous pouvons écouter en utilisant notre canal pour mettre à jour le flux en temps réel.

Voici une image de ce que nous avons construit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif)

### Conclusion

Dans cet article, nous avons couvert comment créer un fil d'actualité photo en temps réel en utilisant .NET et Pusher ainsi que la gestion des téléchargements de fichiers dans .NET.

La base de code de ce tutoriel est disponible dans un [dépôt GitHub public](https://github.com/samuelayo/ASP.NET-PHOTO-FEED). Vous pouvez le télécharger à des fins éducatives.

Avez-vous une meilleure façon de construire notre application, des réserves ou des commentaires ? Faites-le nous savoir dans les commentaires.

Cet article a été initialement publié sur le blog de Pusher [ici](https://blog.pusher.com/build-a-photo-feed-using-net-and-pusher/).

Cette version a été éditée pour plus de clarté et peut apparaître différente de l'article original.