---
title: Voici ce que j'aurais aimé savoir avant de commencer à utiliser Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:45:18.000Z'
originalURL: https://freecodecamp.org/news/heres-what-i-wish-i-knew-before-i-started-using-firebase-9110d393e193
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXiKiz-wuXiCUboQDAG5Cw.png
tags:
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Voici ce que j'aurais aimé savoir avant de commencer à utiliser Firebase
seo_desc: 'By Nikhil Sridhar

  A list of advantages and drawbacks you should consider before choosing Cloud Firestore
  as your database


  Over the last few years, Firebase has grown as an increasingly popular backend solution.
  Especially after the release of Cloud ...'
---

Par Nikhil Sridhar

#### Une liste d'avantages et d'inconvénients à considérer avant de choisir Cloud Firestore comme base de données

![Image](https://cdn-media-1.freecodecamp.org/images/dfT6Nj8mXMG8y0qJgCA1F5r3GeGqwHoMLppn)

Au cours des dernières années, Firebase est devenu une solution backend de plus en plus populaire. Surtout après la sortie de Cloud Firestore. Firestore est une base de données cloud flexible avec des requêtes expressives et des mises à jour en temps réel. Après avoir développé ma première application avec Cloud Firestore, j'ai organisé une liste d'avantages et d'inconvénients. Cette liste vous aidera à choisir si Firestore est la base de données qu'il vous faut.

Avant de commencer, il est impératif que vous compreniez le modèle de données de Cloud Firestore. Firestore stocke les données dans des documents, organisés en collections. _Chaque_ **_document_** _contient un ensemble de paires clé-valeur_. Cloud Firestore est optimisé pour stocker de grandes collections de petits documents. _Tous les documents doivent être stockés dans des_ **_collections_**. Les documents peuvent contenir des sous-collections et des objets imbriqués. _Les deux peuvent inclure des champs primitifs comme des chaînes de caractères ou des objets complexes comme des listes_.

Maintenant que vous comprenez les bases, voici une liste d'éléments dans Cloud Firestore qui peuvent faire ou défaire votre application.

### Avantages #1 : Transactions et Écritures par Lots

La gestion des erreurs peut être l'une des tâches les plus fastidieuses lorsqu'il s'agit de lire et d'écrire dans une base de données. Dans certaines situations, si une erreur se produit lors de la lecture ou de l'écriture à un endroit de la base de données, vous pourriez vouloir annuler toute l'opération. C'est là que les écritures par lots et les transactions entrent en jeu.

**Les écritures par lots sont un ensemble d'opérations d'écriture effectuées de manière atomique. Dans un ensemble d'opérations atomiques, soit toutes les opérations réussissent, soit aucune d'entre elles.** Si votre application réussit à écrire des données dans un document mais échoue à écrire des données dans un autre document, aucune des écritures n'est effectuée. Une erreur est lancée.

**Les transactions fonctionnent de manière similaire. Elles sont plus puissantes, car elles vous permettent de lire et d'écrire dans des documents de manière atomique.**

Les écritures par lots et les transactions peuvent être mieux expliquées à travers un exemple. Le plus simple étant l'ajout d'amis sur une plateforme de médias sociaux. Lorsque l'utilisateur A ajoute l'utilisateur B comme ami, vous voulez écrire des données dans le document de l'utilisateur A et dans le document de l'utilisateur B pour signifier qu'ils sont amis. Cependant, si l'écriture dans le document de l'utilisateur A ou de l'utilisateur B échoue, vous voulez annuler tout changement et lancer une erreur. Les écritures par lots et les transactions simplifient ce processus avec seulement quelques lignes de code.

### Avantages #2 : Invites

![Image](https://cdn-media-1.freecodecamp.org/images/KKJeFis8M7Z0fjdCH1PK0P0Yg49jKs9V8oa3)

Firebase Invites est peut-être **la technique d'intégration la plus puissante**, surtout si votre application fonctionne sur plusieurs plateformes (iOS, Android, etc.). Elle vous permet de **demander à l'utilisateur actuel s'il souhaite inviter ses amis à utiliser votre application.** Cependant, ce qui est encore plus intéressant, c'est que Firebase vous permet de créer un utilisateur temporaire pour l'utilisateur invité afin de fournir à l'utilisateur actuel la meilleure expérience client.

Par exemple, supposons que vous développez une application similaire à Venmo. Cette application permet aux utilisateurs de suivre les dépenses et de régler les comptes. L'utilisateur A souhaite payer l'utilisateur B, qui n'a pas encore de compte. En utilisant Firebase Invites, vous pourriez permettre à l'utilisateur A d'inviter l'utilisateur B. Ensuite, configurer un compte temporaire pour l'utilisateur A afin de suivre les dépenses jusqu'à ce que l'utilisateur B accepte l'invitation et crée son propre compte. Invites fournit des recommandations d'applications par **email et SMS.** C'est un excellent moyen d'acquérir de nouveaux utilisateurs et de rendre les utilisateurs actuels plus heureux que jamais.

### Avantages #3 : Liens Dynamiques

Firebase Dynamic Links permet la meilleure expérience possible d'intégration des utilisateurs. **Ces liens fonctionnent sur plusieurs plateformes. Ils vous permettent de fournir une expérience personnalisée au sein d'une application une fois qu'un utilisateur ouvre un certain lien.** Dynamic Links est mieux utilisé lorsqu'il est intégré avec Firebase Invites.

Prenons l'exemple de l'avantage précédent. L'utilisateur B, qui a été invité à votre application par l'utilisateur A, décide maintenant qu'il veut créer un compte pour voir les dettes qu'il doit à l'utilisateur A. Lorsque l'utilisateur B reçoit l'invitation par email et clique sur le lien dynamique, il sera dirigé vers l'AppStore où il téléchargera votre application. Ensuite, lorsqu'il ouvrira l'application et commencera à s'inscrire, son email sera déjà rempli grâce aux **informations transmises par le lien dynamique**.

### Inconvénient #1 : Requêtes par Sous-collection

L'une des plus grandes déceptions de Cloud Firestore est **l'impossibilité de requêter des documents par leurs sous-collections**. Par exemple, supposons que vous avez la structure de données suivante :

**collection** d'utilisateurs -> **document utilisateur** -> **collection** d'amis -> **document ami** -> données concernant cet ami (nom, email, etc.)

Dans cette structure, il serait impossible de récupérer tous les utilisateurs qui ont un ami avec un nom et un email spécifiques. Firebase prévoit éventuellement de proposer une solution. Pour l'instant, il semble que **la seule solution soit de remplacer les sous-collections par des tableaux** dans lesquels les documents peuvent être requêtés.

Bien que cette solution puisse sembler suffisante, elle ne l'est pas. À mesure que votre application grandit, les tableaux peuvent également grandir, **affectant significativement les performances de lecture et d'écriture des documents**.

### Inconvénient #2 : Requêtes par Localisation

![Image](https://cdn-media-1.freecodecamp.org/images/yPBPQPtjssORw63qBsL2qKBZjII3XSXTmMe8)

Selon la fonctionnalité de votre application, cela pourrait être le plus grand défaut de tous. Bien que Cloud Firestore fournisse un type de données de localisation, **il ne vous permet pas de requêter tous les documents dans un rayon donné autour d'une localisation.**

Considérons que vous développez une application identique à Uber. Lorsque un utilisateur se connecte à l'application, vous voulez récupérer toutes les voitures dans un certain rayon autour de la localisation actuelle de l'utilisateur pour alerter l'utilisateur s'il y a des conducteurs à proximité. Cette tâche est impossible sans l'aide de bibliothèques tierces.

Heureusement, si vous utilisez la base de données en temps réel, Firebase recommande maintenant d'utiliser la bibliothèque [GeoFire](https://github.com/googlearchive/geofire) pour requêter des documents par localisation. Cependant, si vous prévoyez d'utiliser Cloud Firestore, il n'y a pas de solution recommandée.

Bien qu'il existe quelques bibliothèques qui ont tenté de résoudre ce problème comme [GeoFirestore](https://github.com/imperiumlabs/GeoFirestore), Firebase n'a pas encore vérifié leur fiabilité.

### Inconvénient #3 : Recherche en Texte Intégral

Ce problème est sûr d'affecter quiconque utilise Cloud Firestore, car **il ne permet pas de requêter des documents par "texte incomplet"**. Ce problème peut être mieux illustré par un exemple.

Supposons que votre application permet aux utilisateurs de s'ajouter comme amis. Un utilisateur tape "Al" dans une tentative de rechercher son ami "Alex". **Vous voulez récupérer tous les utilisateurs de la base de données dont le nom contient le texte "Al" pour aider l'utilisateur à affiner sa recherche. Cette tâche n'est pas possible** avec Cloud Firestore seul. **Algolia, un service tiers, est requis pour implémenter la recherche en texte intégral**. Tous les documents doivent être téléchargés vers Algolia sous forme d'enregistrements. Ces enregistrements peuvent ensuite être requêtés par texte incomplet.

Pour plus de conseils, restez à l'écoute et suivez-moi. Si vous avez aimé cet article, n'hésitez pas à appuyer longuement sur ce bouton d'applaudissements.