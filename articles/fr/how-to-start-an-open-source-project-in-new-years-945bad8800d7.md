---
title: Comment démarrer un projet Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T21:42:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-an-open-source-project-in-new-years-945bad8800d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*skkIJz5B4nwZya06X4Q61w.jpeg
tags:
- name: open source
  slug: open-source
- name: project management
  slug: project-management
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: Comment démarrer un projet Open Source
seo_desc: 'By Dmitriy Strukov

  My name is Dima and I’m Ruby developer. Today I want to share my experience creating
  an open source solution. I will talk about what steps the project should take, how
  to choose the right functionality for the first release, and wh...'
---

Par Dmitriy Strukov

Je m'appelle Dima et je suis développeur Ruby. Aujourd'hui, je souhaite partager mon expérience de création d'une solution open source. Je vais parler des étapes que le projet doit suivre, comment choisir les bonnes fonctionnalités pour la première version, et quelles erreurs j'ai personnellement rencontrées lors de la création de mon projet open source.

Il y a six mois, j'ai eu l'idée qu'il serait bon de créer un projet open source. Au lieu de tâches de test pour l'entretien, il me suffirait d'envoyer un lien vers le dépôt. La perspective d'aider mes collègues avec la solution à leurs problèmes quotidiens m'a inspiré.

J'ai toujours détesté les gems pour créer des panneaux d'administration. Tout mouvement supplémentaire nécessite de redéfinir la classe, et pour changer les champs, vous devez apporter des modifications aux fichiers. Après réflexion et discussion avec des collègues, j'ai décidé de créer une nouvelle bibliothèque qui serait flexible et ne nécessiterait ni tableaux de bord ni fichiers de configuration.

### Déterminer les objectifs

Chaque projet open source résout un problème spécifique. Parlez avec des collègues, des chats, des forums, et partagez votre idée. Tout cela vous aide dans les premières étapes à comprendre des choses importantes, comme quelles solutions existent déjà, et à entendre des critiques. Parlez avec des personnes qui ont déjà des projets open source. Elles peuvent vous donner des conseils très précieux, alors n'ayez pas peur de demander et de prendre l'initiative.

Un conseil important que j'ai reçu à ce stade est de porter attention en premier lieu à la documentation du projet. Vous pouvez avoir un très bon projet, mais personne ne prendra le temps de comprendre comment il fonctionne.

L'aspect le plus important, sans lequel les étapes suivantes sont impossibles, est la motivation. L'idée du projet doit vous inspirer en premier lieu. Le plus souvent, les gens s'habituent aux outils avec lesquels ils travaillent et tombent dans une zone de confort, donc les opinions externes peuvent être ambiguës.

### Planification

Le choix d'un certain gestionnaire de tâches est une question de goût. Il devrait avoir une image claire des tâches et des étapes de votre projet.

Divisez les tâches en sous-tâches. Idéalement, si une tâche ne prend pas plus de 3 à 4 heures, il est important de profiter de la mise en œuvre de petites tâches. Cela aidera à éviter l'épuisement et la perte de motivation.

J'utilise [pivotal tracker](http://pivotaltracker.com/). Le principal avantage est une version gratuite pour les projets open source où vous pouvez trier les tâches par type (fonctionnalité, bug, chore, release), et les regrouper en versions et déterminer des délais.

### Documentation

Chaque projet open source doit contenir ces éléments :

* README
* Licence Open Source
* Directives de contribution
* Changelog

Le fichier README n'explique pas seulement comment utiliser votre projet, mais aussi le but de votre projet. Si vous ne savez pas comment écrire correctement un fichier README, vous pouvez regarder d'autres projets open source connus ou utiliser un [modèle](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).

La licence garantit que d'autres peuvent utiliser, copier et modifier le code source du projet. Vous devez ajouter ce fichier à chaque dépôt avec votre projet open source. MIT et Apache 2.0 GPLv3 sont les licences les plus populaires pour les projets open source. Si vous n'êtes pas sûr de ce qu'il faut choisir, vous pouvez utiliser ce service pratique [service](https://choosealicense.com/).

Le fichier CONTRIBUTING aidera d'autres développeurs à contribuer au projet. Aux premières étapes du projet, il n'est pas nécessaire de porter une attention particulière à ce fichier. Vous pouvez utiliser le modèle déjà préparé d'un autre projet.

Le Changelog contient une liste soutenue, chronologiquement ordonnée, des changements significatifs pour chaque version. Comme pour le fichier CONTRIBUTING, je ne conseille pas de porter une attention particulière à cela à un stade précoce.

### Versioning

Pour suivre les changements importants pour les utilisateurs et les contributeurs, il existe une [version sémantique](https://semver.org/). Le numéro de version contient des nombres et suit le modèle suivant X.Y.Z.

* X version majeure
* Y version mineure
* Z version de correctif

### Intégration continue / Livraison continue

Pour exécuter automatiquement les tests et les builds, j'utilise [Travis CI](https://travis-ci.org/). Il est également bon d'ajouter des badges pour afficher l'assemblage réussi de la build dans l'assistant, la couverture de test ([Codecov](https://codecov.io/)), et la documentation ([Inch CI](https://inch-ci.org/)).

![Image](https://cdn-media-1.freecodecamp.org/images/GOv6LmGVzeTtbenyF6xAowGpn9QSBHNRr9oB)

Après chaque nouveau commit ou merge dans le master, j'ai automatiquement un déploiement sur [Heroku](http://heroku.com/) (très pratique intégration avec GitHub). Tous les outils sont absolument gratuits pour un projet open source.

### Mes erreurs

Pour analyser la phase initiale, j'avais une idée, mais il n'y avait pas de plan clair. J'ai décidé que je voulais faire cela sans avoir une idée claire de combien de temps cela prendrait ou une représentation spécifique des fonctions qui seraient dans la première version de la bibliothèque. J'avais juste beaucoup de désir et un manque de plan clair.

De plus, après avoir lu l'histoire d'autres projets (pas seulement open source), j'ai remarqué qu'à un stade précoce, certains plans sont trop optimistes. Ils nécessitent une réévaluation de leurs forces et capacités. Mais il n'est pas facile de trouver du temps chaque jour pour écrire une nouvelle fonctionnalité dans le projet. La plupart des tâches ont finalement dû être éliminées, laissant le minimum nécessaire pour le [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product).

À l'heure actuelle, mon projet [simple-admin](https://github.com/evil-raccoon/simple_admin) est en version alpha. Les plans futurs incluent la création d'une version séparée de la bibliothèque pour [Hanami](http://hanamirb.org/).