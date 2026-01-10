---
title: Un aperçu des outils de discussion modernes, et pourquoi nous avons décidé
  d'en construire notre propre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-05-14T05:50:28.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-modern-discussion-tools-and-why-we-decided-to-build-our-own-54bd98c48b15
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WsjchoXvv2f1TMEt.png
tags: []
seo_title: Un aperçu des outils de discussion modernes, et pourquoi nous avons décidé
  d'en construire notre propre
seo_desc: 'By freeCodeCamp

  Our chat rooms are a fun place to hang out, make friends, and get fast help. But
  knew early on that our campers wanted a less synchronous place to discuss articles
  and share their projects.

  We needed a modern discussion tool, with upv...'
---

Par freeCodeCamp

Nos salles de chat sont un endroit amusant pour se détendre, se faire des amis et obtenir de l'aide rapidement. Mais nous savions dès le début que nos campers voulaient un endroit moins synchrone pour discuter des articles et partager leurs projets.

Nous avions besoin d'un outil de discussion moderne, avec des fonctionnalités de vote, de commentaire, de discussion en fil et de recherche, qui pouvait être davantage indexé par les moteurs de recherche.

Puisque nous sommes des [Programmeurs Pragmatiques](http://amzn.to/1wWvhrz), et que nous avons fait de notre mieux pour éviter le syndrome [Not Invented Here](http://en.wikipedia.org/wiki/Not_invented_here). Nous avons résolu de donner à chaque produit sur le marché une chance équitable. Nous avons donc d'abord essayé les solutions suivantes:

### Reddit Subreddits

![Image](https://cdn-media-1.freecodecamp.org/images/0*WsjchoXvv2f1TMEt.png)

Avantages:

* Vous pouvez créer un subreddit et le configurer en moins d'une heure.
* Les subreddits sont gratuits, fiables et gérés par Reddit.
* Les subreddits servent de mécanisme de découverte. D'autres utilisateurs de Reddit peuvent tomber sur votre subreddit.

Inconvénients:

* Les pages de Reddit sont remplies de boutons et de publicités distractifs, attirant constamment l'attention de vos utilisateurs loin de votre contenu.
* Il nécessite une connexion et un mot de passe Reddit, et une session active.
* Reddit obtient les backlinks, pas vous.

### Discourse

![Image](https://cdn-media-1.freecodecamp.org/images/0*uIVjFdgz56BiBCwc.png)

Avantages:

* Discourse dispose de nombreuses fonctionnalités et d'un puissant panneau d'administration.
* Discourse sauvegarde automatiquement les images et les sauvegardes de base de données nocturnes vers AWS S3.
* Vous pouvez déployer Discourse sur AWS et le configurer en quelques heures en utilisant [Bitnami](https://bitnami.com/stack/discourse).

Inconvénients:

* Vous devez connaître Ruby on Rails pour personnaliser et maintenir une instance Discourse.
* Discourse veut que vous fassiez les choses à sa manière. Par exemple, vous ne pouvez pas désactiver ses raccourcis clavier.
* Discourse est lent. Même sur une petite instance EC2 (~700$/an), et l'application rampait, peu importe le nombre de personnes qui l'utilisaient.

### NodeBB

![Image](https://cdn-media-1.freecodecamp.org/images/0*uGKWapOh-Wasqb64.png)

Avantages:

* NodeBB est écrit en NodeJS, et en conséquence, il est rapide.
* NodeBB a été conçu pour fonctionner avec Redis, et cela se voit dans la conception du schéma. Le support MongoDB semble "ajouté après coup".
* NodeBB s'améliore chaque jour grâce à une communauté de développement active.

Inconvénients:

* Nous n'avons pas réussi à le faire fonctionner sur Heroku avec MongoDB, et nous n'avons pas trouvé de documentation expliquant comment nous pourrions le faire.
* NodeBB fait beaucoup de choses, mais aucune d'entre elles particulièrement bien.

### Telesc.pe

![Image](https://cdn-media-1.freecodecamp.org/images/0*QYSJ-xVz80oEYZxF.png)

Avantages:

* Telesc.pe est presque identique en fonctionnalité à Hacker News et Reddit

Inconvénients:

* Vous devez utiliser Meteor.js pour le personnaliser et le maintenir.
* La dernière fois que nous avons essayé, Telesc.pe n'était pas capable de fonctionner sur Heroku, malgré les buildpacks qui étaient censés permettre aux applications Meteor de fonctionner sur Heroku.

### Camper News

![Image](https://cdn-media-1.freecodecamp.org/images/0*AjPoNK4x2a7WRCR-.png)

Après avoir essayé toutes ces solutions et les avoir trouvées suboptimales pour nos campers, nous avons décidé d'abandonner et d'en construire une nous-mêmes. Avantages:

* Les campers peuvent commencer à publier immédiatement sans avoir à quitter Free Code Camp ou à créer des connexions et des mots de passe supplémentaires.
* Les publications des campers renvoient à leurs portefeuilles Free Code Camp, augmentant leur profil au sein de la communauté.
* Chaque soumission devient un artefact recherchable que les campers peuvent trouver et utiliser à l'avenir.

Nous pouvons observer le comportement global, effectuer des tests A/B, et utiliser les données collectées pour rendre Free Code Camp un meilleur endroit pour apprendre à coder.

Nous sommes restés aussi proches que possible des conventions qui fonctionnent sur Reddit, Product Hunt et Hacker News.

Camper News continuera à évoluer à mesure que nous recevrons des retours de nos campers. Il est déjà open-source, mais nous pourrions aller plus loin et demander à certains de nos campers de le factoriser en une application autonome.

[Découvrez Camper News ici](http://www.freecodecamp.com/stories/hot). Nous avons hâte de lire vos articles.

_Initialement publié sur [blog.freecodecamp.com](http://blog.freecodecamp.com/2015/03/an-overview-of-modern-discussion-tools-and-why-we-decided-to-build-our-own.html) le 10 mars 2015._