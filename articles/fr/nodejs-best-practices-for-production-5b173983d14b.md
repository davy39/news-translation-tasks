---
title: 'NodeJS : Meilleures pratiques pour la production'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T10:18:21.000Z'
originalURL: https://freecodecamp.org/news/nodejs-best-practices-for-production-5b173983d14b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7wN5t9ILU0fpnhbMX2vtng.jpeg
tags:
- name: Design
  slug: design
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'NodeJS : Meilleures pratiques pour la production'
seo_desc: 'By Saurabh Rayakwar

  This is an attempt to enlist the most important practices for developing and deploying
  on NodeJs.

  I have been working on this technology for a while myself. I realize its huge potential
  and place in the development process. With t...'
---

Par Saurabh Rayakwar

Ceci est une tentative de lister les pratiques les plus importantes pour le développement et le déploiement sur NodeJs.

Je travaille sur cette technologie depuis un certain temps. Je réalise son énorme potentiel et sa place dans le processus de développement. Avec une forte concurrence de langages comme Python et Golang, NodeJS a prouvé son utilité dans des cas d'utilisation appropriés.

Avant de plonger dans les meilleures pratiques ?, je voudrais faire une brève introduction à ce qu'est un modèle de microservice. Puis poursuivre la conversation à partir de là.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7wN5t9ILU0fpnhbMX2vtng.jpeg)

#### Alors, que sont les microservices ?

Les microservices - également connus sous le nom d'architecture de microservices - est un style architectural qui structure une application comme une collection de services qui sont :

* Hautement maintenables et testables
* Faiblement couplés
* Déployables indépendamment
* Organisés autour des capacités métier.

L'architecture de microservices permet la livraison/déploiement continu de grandes applications complexes. Elle permet également à une organisation de faire évoluer sa stack technologique.

#### Comment décider si vous avez besoin de microservices

Initialement, lorsque vous commencez à travailler sur votre MVP, vous n'aurez peut-être pas besoin d'utiliser des microservices. La mise à l'échelle sur l'axe Y ne sera peut-être pas votre agenda pour le moment. Mais lorsque le produit commence à mûrir et parfois trop tôt où vous devez gérer la mise à l'échelle, la décomposition en modules fonctionnels a plus de sens car le business lui-même se décompose. Ce sera le bon moment pour commencer à examiner le modèle d'architecture de microservices.

Un livre que je recommande vivement est celui de Chris Richardson ici : [http://bit.ly/2EmJDYt](http://bit.ly/2EmJDYt).

Les microservices sont le plus souvent considérés lors du remplacement d'une application monolithique qui était assez courante jusqu'à récemment, lorsque des solutions de conteneurisation comme Docker ont commencé à dominer le monde DevOps. Mais nous en parlerons plus tard.

Il serait injuste de continuer sans mentionner le Domain Driven Design (DDD). C'est une stratégie très populaire pour décomposer votre produit en modules fonctionnels. Par conséquent, il est très utile pour créer des microservices.

#### Alors, qu'est-ce qu'un domaine selon le DDD ?

Chaque problème que vous essayez de résoudre est un domaine.

Chaque domaine est subdivisé en contextes délimités mutuellement exclusifs. Ces contextes ne sont rien d'autre que des zones séparées de ce problème particulier.

Dans un modèle de microservice, chaque contexte délimité correspond à un microservice. Les modèles DDD vous aident à comprendre la complexité du domaine. Pour le modèle de domaine de chaque Contexte Délimité, vous identifiez et définissez les entités, les objets de valeur et les agrégats qui modélisent votre domaine.

Selon la complexité de votre logiciel, vous pouvez choisir les principes du DDD ou effectuer une approche plus simple.

Le but est d'atteindre un modèle de domaine hautement cohésif et faiblement couplé. Pour cela, suivez cette approche :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RSnJbXxdqGt-uAoumCmHzA.jpeg)

C'était une brève introduction au DDD. Pour en savoir plus, je vous recommande vivement de lire l'excellent livre d'Eric Evans [http://bit.ly/2Eoy17l](http://bit.ly/2Eoy17l).

Passons à la suite.

J'espère que vous tenez le coup avec moi. ?

À partir de là, je vais parler davantage des pratiques spécifiques à NodeJS. Et ce que je veux dire, c'est que les microservices et le DDD vous aident à évaluer le vrai potentiel de NodeJS néanmoins. Il est complet en lui-même. Comment ? Nous allons voir.

#### Quel modèle de conception utiliser avec NodeJs

![Image](https://cdn-media-1.freecodecamp.org/images/1*waWi1Kb0zt6GptBNVQ6ikQ.jpeg)

Les modèles de conception concernent la conception de logiciels en utilisant certaines normes connues d'un certain nombre de développeurs.

Il existe divers modèles de conception que nous pouvons utiliser. Je voudrais présenter et/ou rappeler aux développeurs qui connaissent déjà un modèle appelé le Repository Pattern.

Ce modèle facilite la séparation de la logique MVC tout en facilitant la gestion de la définition du modèle et de l'interaction du modèle avec le reste de la logique.

Il se compose de :

1. **Controller** : Il ne gère que la requête et la réponse et les attributs associés. Il n'aura aucune logique métier ou définition de modèle ou associations de modèle. (nom du dossier : controllers)
2. **Service** : Il contient la logique métier pour votre microservice. Le contrôle passe du contrôleur à un service. Il y a une relation 1:1 entre un contrôleur et son service et une relation 1:plusieurs entre le service et les repositories. (nom du dossier : services)
3. **Repository** : Il interagit avec les modèles qui font partie du dossier de modèles. Toute requête à la base de données via la couche de modèle sera formée ici. Il n'aura aucune logique métier. (nom du dossier : repositories)
4. **Model** : Il contient la définition du modèle, les associations, les fonctions virtuelles (par exemple, dans mongoose)
5. **Utilities** : Cela contiendra des classes/fonctions d'assistance qui peuvent être utilisées comme services. Par exemple : une utilité Redis qui contient toutes les fonctions nécessaires pour interagir avec Redis. (nom du dossier : utilities)
6. **Test case** : Cela inclura des cas de test unitaires contre les méthodes du contrôleur pour assurer une couverture de code maximale. (nom du dossier : spec)

Pour en savoir plus, vous pouvez vous référer à ce lien : [http://bit.ly/2TrSyRS](http://bit.ly/2TrSyRS)

#### D'accord, parlez-moi des modules de cluster

Une seule instance de Node.js s'exécute dans un seul thread. Pour tirer parti des systèmes multi-cœurs, l'utilisateur voudra parfois lancer un cluster de processus Node.js pour gérer la charge.

Le module cluster permet une création facile de processus enfants qui partagent tous les ports du serveur.

> Veuillez noter qu'il est idéal d'utiliser un processus par conteneur lors de l'utilisation de la conteneurisation Docker pour le déploiement via des microservices. Par conséquent, les modules de cluster ne sont pas utiles lors de l'utilisation de la dockerisation.

#### Comment gérer le flux de contrôle dans NodeJS

Lors de l'utilisation de callbacks ou de promesses, les bibliothèques suivantes pourraient être utiles :

1. Async ([https://www.npmjs.com/package/async](https://www.npmjs.com/package/async))
2. Vasync (avec un meilleur suivi des opérations) [https://www.npmjs.com/package/vasync](https://www.npmjs.com/package/vasync)
3. Bluebird (gère les promesses, par exemple, Promise.all, etc.) [https://www.npmjs.com/package/bluebird](https://www.npmjs.com/package/bluebird)

#### Et les boucles ?

* Boucle en série : exécuter chaque étape une par une dans l'ordre

* Boucle retardée : boucle avec un délai d'attente

* Boucle parallèle : collecter toutes les promesses dans une boucle et exécuter en parallèle

#### Et quels sont quelques outils de linting utiles ?

Les outils de linting analysent votre code statiquement (sans l'exécuter). Ils identifient les bugs potentiels ou les modèles dangereux. Des modèles comme l'utilisation de variables non déclarées, ou des instructions "case" à l'intérieur d'un switch sans instruction "break".

L'activation du mode strict sur votre base de code avec 'use strict' peut aider votre code à échouer rapidement si le parseur JavaScript peut identifier une fuite globale ou un comportement similaire.

Des exemples de linters sont Javascript lint et JS lint.

#### D'accord, comment gérons-nous la journalisation ?

Certains packages npm couramment utilisés sont :

* Winston (https://www.npmjs.com/package/winston)
* Bunyan (https://www.npmjs.com/package/bunyan)

Format de journalisation possible :

Pour les systèmes distribués comme les microservices, vous souhaiterez explorer le traçage distribué en utilisant ZipKin, etc.

> Une note sur les packages NPM : Vous ne devriez utiliser un package que s'il résout un problème pour vous que vous ne pouvez pas résoudre vous-même. Effectuez régulièrement des audits npm pour trouver des problèmes critiques avec vos dépendances npm.

#### Gestion des exceptions non capturées

Par défaut, Node.js gère ces exceptions en imprimant la trace de la pile sur stderr et en quittant avec le code 1, remplaçant tout code process.exitCode précédemment défini.

Remarque : L'ajout d'un gestionnaire pour l'événement 'uncaughtException' remplace ce comportement par défaut.

Alternativement, modifiez le process.exitCode dans le gestionnaire 'uncaughtException', ce qui entraînera la sortie du processus avec le code de sortie fourni. Sinon, en présence d'un tel gestionnaire, le processus se terminera avec 0.

process.exit(0) – terminaison réussie   
process.exit(1) – terminaison non réussie

#### Gestion des rejets non gérés

Les promesses sont omniprésentes dans le code Node.js et parfois enchaînées à une très longue liste de fonctions qui retournent des promesses, et ainsi de suite.

Ne pas utiliser un gestionnaire de rejet .catch() approprié provoquera l'émission d'un événement unhandledRejection. Si ce n'est pas correctement capturé et inspecté, vous pourriez vous priver de votre seule chance de détecter et éventuellement de corriger le problème.

#### Conseil supplémentaire :

#### console.time() et console.timeEnd()

L'objet console dispose des méthodes time() et timeEnd() qui aident à analyser les performances de parties de votre code.

Ce n'est pas une solution pour la production, mais elle peut être utilisée lorsque vous n'avez pas de meilleurs outils.

**Merci beaucoup pour votre temps.**  
**[Inscrivez-vous à ma newsletter](https://forms.gle/SWVTMcdgnqdecD3t9)**

D'autres articles merveilleux sur des sujets similaires :

1. [https://microservices.io](https://microservices.io) ?
2. [https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)