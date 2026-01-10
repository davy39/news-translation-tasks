---
title: 10 étapes pour mieux planifier afin d'écrire moins de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-06-03T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/10-steps-to-plan-better-so-you-can-write-less-code-ece655e03608
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lO6S-555VY0QioGFss2SQw.jpeg
tags: []
seo_title: 10 étapes pour mieux planifier afin d'écrire moins de code
seo_desc: 'By freeCodeCamp

  An ounce of preparation is worth a pound of cure. That’s true in medicine, and that’s
  definitely true in software development.

  Here’s a structured 10-step workflow that will guide you through the app planning
  process, with the goal of...'
---

Par freeCodeCamp

Une once de préparation vaut une livre de remède. C'est vrai en médecine, et c'est définitivement vrai en développement logiciel.

Voici un workflow structuré en 10 étapes qui vous guidera à travers le processus de planification de l'application, avec pour objectif de vous éviter d'écrire beaucoup de code inutile.

Ensemble, nous allons planifier une simple application web de type "To-do" en une seule page. Nous allons également planifier un backend API pour une future application mobile.  
   
Voici les étapes que nous allons suivre pour planifier ce projet:

#### 1) Créer notre tableau Trello

[Trello](http://trello.com/) est un moyen amusant et gratuit de diviser votre processus de planification et de développement en petites tâches qui peuvent être suivies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U__BPzBi5pLsulZZXxnZsA.png)

* À faire  ce qui reste à faire
* En cours  tâches sur lesquelles les gens travaillent actuellement
* Fait  tâches terminées et prêtes pour les tests

#### 2) Créer nos user stories agiles

Voici quelques exemples de user stories. Ceux-ci guideront notre réflexion sur les fonctionnalités et la fonctionnalité de notre application. Notez qu'ils suivent tous une structure similaire : en tant que <personne> je peux <faire quelque chose>.

* en tant qu'utilisateur connecté, je peux voir la liste de mes tâches à faire.
* en tant qu'utilisateur connecté, je peux ajouter une nouvelle tâche.
* en tant qu'utilisateur connecté, je peux supprimer une tâche (uniquement mes tâches  pas celles des autres utilisateurs).
* en tant qu'utilisateur connecté, je peux compléter une tâche (uniquement mes tâches  pas celles des autres utilisateurs).
* en tant qu'utilisateur anonyme, je peux m'inscrire pour un nouveau compte, récupérer mon mot de passe ou me connecter à l'application avec un compte existant.

#### 3) Créer notre modèle de cas d'utilisation

Notre modèle de cas d'utilisation visualisera nos user stories et ajoutera des suggestions sur la manière de les implémenter.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Y2sQ8pcY1V4bS__w.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*8vNsghIvAKpeF6Pv.)

#### 4) Créer notre diagramme d'activité

Notre diagramme d'activité montrera les différents chemins que nos utilisateurs peuvent emprunter dans notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*o2dH3EQRpUEZfdh5.)

* Un utilisateur accède à notre application de tâches à faire.
* Si l'utilisateur n'est pas connecté, il verra notre page de connexion.
* S'il a déjà un compte, il peut se connecter.
* S'il a un compte, mais qu'il a oublié son mot de passe, il peut le récupérer.
* S'il n'a pas de compte, il peut en créer un.
* Les options "créer un compte" et "récupérer mon mot de passe" nécessiteront une validation par email. Un utilisateur ne peut se connecter à notre application qu'après avoir confirmé son adresse email.
* S'il est connecté, il verra sa liste de tâches à faire (celle-ci peut être vide s'il n'a pas encore ajouté de tâches).
* peut voir sa liste de tâches
* peut marquer une tâche de sa liste comme terminée
* peut rechercher dans sa liste de tâches
* peut supprimer une tâche de sa liste
* L'utilisateur peut quitter l'application à tout moment.

#### 5) Créer nos maquettes

Nos maquettes montrent à quoi notre application devrait ressembler. Il est beaucoup plus rapide d'itérer sur une maquette que sur du code fonctionnel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0Sqp2wF75fe2LCXl.)

#### 6) Choisir les bonnes technologies pour notre projet

Comme il s'agit d'une application en une seule page, nous allons nous appuyer fortement  ou dans ce cas exclusivement  sur JavaScript. Utilisons l'une des piles JavaScript les plus populaires : la pile [MEAN](http://meanjs.org/). Un grand avantage de la pile MEAN est que tous ses composants sont gratuits et open-source. Il existe également des tonnes de ressources disponibles pour apprendre la pile MEAN et pour la déboguer lorsque vous rencontrez inévitablement des erreurs.

Vous pouvez avoir un [environnement de développement MEAN](http://www.freecodecamp.com/challenges/waypoint-get-set-for-basejumps) en ligne dans le cloud en moins d'une heure, gratuitement.

Voici les composants que nous allons utiliser:

1. [MongoDB](http://mongodb.org/) pour notre base de données
2. [Node.js](http://nodejs.org/) et [Express.js](http://expressjs.com/) pour implémenter notre API
3. [AngularJS](http://angularjs.org/), ainsi que HTML et CSS (et Bootstrap) pour notre application côté client
4. [Mongoose](http://mongoosejs.com/) pour connecter notre application à MongoDB

#### 7) Concevoir notre schéma de base de données

Il vaut la peine de concevoir un schéma de base de données, même pour notre application simple.

Nous aurons deux collections : notre collection "Users" abritera nos données utilisateur, et notre collection "ToDo" abritera nos tâches à faire. Un utilisateur peut avoir zéro, un ou plusieurs tâches dans sa liste de tâches, nous aurons donc une relation de un-à-plusieurs (1:m) entre nos deux collections.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6TjyDpsRXJ6l4KfD.)

#### **8) Définir nos cas d'utilisation**

1. Que se passe-t-il avec les tâches liées à un utilisateur qui supprime son compte ? Lorsque l'utilisateur supprime son compte, les tâches liées à cet utilisateur doivent également être supprimées.
2. Aucune tâche ne peut être ajoutée sans être attachée à un utilisateur confirmé.
3. Une tâche ne peut être supprimée que par son propriétaire.
4. Aucun utilisateur ne peut être ajouté avec un nom d'utilisateur ou un mot de passe vide.
5. Aucune tâche ne peut être ajoutée avec une tâche vide.

Choses à garder à l'esprit:

1. Utilisez le middleware Mongoose pour supprimer les documents dépendants comme les tâches lorsqu'un utilisateur supprime son compte.
2. Utilisez les règles de validation Mongoose sur les modèles pour empêcher les champs vides d'être ajoutés à notre base de données.

#### 9) Concevoir et tester notre API

Je vous recommande de créer un compte et de commencer à jouer avec. Si vous liez votre compte [GitHub](http://github.com/) avec Apiary, vous pouvez vous assurer que votre documentation reste toujours à jour. Vous pourrez également tester vos données visuellement sans avoir besoin de frapper vos points de terminaison API. Si vous préférez tester votre API depuis la ligne de commande, [voici un exemple de la manière de le faire](http://docs.agendor.apiary.io/).

Plus tard, une fois que vous aurez implémenté votre API avec Node.js et Express.js, vous n'aurez qu'à définir votre URL dans Apiary. Ensuite, vous pourrez commencer à tester vos appels. Notre URL d'hébergement actuelle ([http://fcctodoapp.apiblueprint.org/](http://fcctodoapp.apiblueprint.org/)) sera remplacée par l'URL de votre API.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xO5pioP4hCYJ38Bu.)

#### 10) Commencer à écrire du code !

C'est la partie amusante, et cela prendra la majeure partie du temps de votre projet. Si vous avez besoin d'aide, rejoignez-nous et [apprenez à coder](http://freecodecamp.com/).

[_Bianca Mihal_](https://twitter.com/intent/user?screen_name=bubuslubu) _a initialement publié ceci_ _sur notre blog maintenant défunt en juin 2015._