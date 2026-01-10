---
title: Un guide complet pour apprendre RxJava
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T22:15:55.000Z'
originalURL: https://freecodecamp.org/news/a-complete-roadmap-for-learning-rxjava-9316ee6aeda7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gaQI9yDYH86yIlrLE0tyaQ.png
tags:
- name: Android
  slug: android
- name: Computer Science
  slug: computer-science
- name: mobile app development
  slug: mobile-app-development
- name: rxjava
  slug: rxjava
- name: software development
  slug: software-development
seo_title: Un guide complet pour apprendre RxJava
seo_desc: 'By Ayusch Jain


  This article was originally posted here


  I wish someone had written an article like this when I started my learning journey
  with RxJava in 2017. I wish there had been a perfect book or some kind of an online
  school which taught me how...'
---

Par Ayusch Jain

> Cet article a été initialement publié [ici](https://ayusch.com/the-complete-rxjava-roadmap/)

Je souhaite que quelqu'un ait écrit un article comme celui-ci lorsque j'ai commencé mon parcours d'apprentissage avec RxJava en 2017. J'aurais aimé qu'il y ait un livre parfait ou une sorte d'[école en ligne](http://microverse.org) qui m'ait appris comment commencer avec Rx de la bonne manière.

Il y a eu tellement d'engouement récemment autour de **RxJava** et de la programmation réactive en général. Tout le monde semble la promouvoir, mais personne ne semble avoir une idée de la manière dont un programmeur novice qui commence avec RxJava devrait aborder ce parcours.

Tout cela a une raison ! RxJava a une courbe d'apprentissage abrupte et il n'y a pas une seule manière de la maîtriser. Certains préfèrent la documentation (qui est excellente, soit dit en passant), d'autres préfèrent les livres sur RxJava avec quelques exemples, tandis que certains fous (y compris moi *facepalm*) commettent l'erreur de plonger directement dans le code après avoir regardé une vidéo YouTube d'une conférence de Kaushik Gopal sur la manière de commencer avec RxJava et commencent à refactoriser leur code.

La dernière méthode est absolument dangereuse, et au lieu de résoudre vos problèmes avec Rx, vous finirez simplement par en créer de nouveaux. Je suggère donc que vous suiviez le guide donné ci-dessous pour commencer avec RxJava.

Bien que ce ne soit en aucun cas la seule manière de procéder, après avoir eu presque 1,5 ans d'expérience avec **RxJava** (et toujours en apprentissage), j'aurais aimé que quelqu'un m'ait dit ces choses lorsque je commençais mon parcours. Si vous suivez le guide donné religieusement, je peux vous assurer que vous aurez une base solide en RxJava sur laquelle vous pourrez ensuite construire pour libérer tout son potentiel.

J'ai divisé l'ensemble du guide en quatre phases :

* **La Découverte** : Dites bonjour au monde de la programmation réactive.
* **Le Désenchantement** : Le monde n'est pas tout soleil et arcs-en-ciel.
* **Eureka !**
* **Le ciel est la limite**

Alors, commençons sans plus tarder.

### Phase 1

#### La Découverte : Dites bonjour au monde de la programmation réactive

J'aurais aussi pu intituler cette phase « La Motivation », car c'est la toute première phase où vous avez entendu parler de **RxJava** par un ami ou quelqu'un sur LinkedIn en a posté à propos, ou vous êtes simplement tombé sur un morceau de code avec des Observables qui volent partout.

Quoi qu'il en soit, lorsque vous regardez pour la première fois un morceau de **routine RxJava** (même la plus simple), vous pourriez être intimidé par toutes les méthodes appelées les unes après les autres dans une seule chaîne. Mais vous remarquerez que le code semble plus propre que tout autre que vous ayez jamais vu. Et il accomplit des tâches d'une complexité inimaginable avec de simples chaînes de méthodes alors que vous avez été en train de former des AsynTask et de penser à plusieurs appels **Retrofit/Volley** dans votre tête.

Des tâches telles que faire plusieurs appels API les uns après les autres, faire des appels API et sauvegarder dans une base de données et retourner un succès ou un échec, etc., sont **accomplies en 20 à 25 lignes de code**. Vous serez intimidé mais en même temps enclin à découvrir ce qu'est cet outil et comment vous pouvez aussi commencer à écrire un code aussi propre.

**Alors, afin de vous lancer, voici une liste de choses que je vous demande de faire dans cette phase :**

Je suggère que vous **regardiez cette conférence de Kaushik Gopal** au moins deux fois (il m'a fallu 4 visionnages pour en saisir le contenu. J'avais la conférence téléchargée sur mon ordinateur) jusqu'au bout. Selon moi, c'est la référence absolue pour quiconque souhaite se lancer dans la programmation réactive.

Kaushik Gopal explique magnifiquement les nuances de RxJava et fournit des exemples concrets, avec une touche d'abstraction sur les aspects techniques absolus, facilement compréhensibles par tout débutant. Il divise toute routine RxJava en 4 constructions de base (même mon article sur RxJava : [**Comprendre les bases de RxJava**](https://disq.us/?url=https%3A%2F%2Fayusch.com%2Funderstanding-rxjava-basics%2F&key=7M4ry_gpESP38RXOsGVmaQ) est inspiré par sa conférence).

Bien sûr, lors de la première tentative, vous ne pourrez pas saisir exactement ce qu'est un observable et comment le modèle observateur fonctionne. C'est pourquoi je suggère que vous le regardiez au moins deux fois.

**Voici ce que vous devriez comprendre clairement à partir de cette conférence (au moins) :**

* Qu'est-ce qu'un Observable ?
* Qu'est-ce qu'un Subscriber ?
* Comment les Observables et les Subscribers fonctionnent-ils ensemble ?
* Qu'est-ce qu'un opérateur (pas la fonctionnalité spécifique, mais ce qu'un opérateur fait) ?

Regardez-la autant de fois que vous le souhaitez, mais vous devez être absolument clair sur les 4 questions ci-dessus une fois que vous avez terminé. Vous pouvez également vous référer au texte disponible en ligne avec cette vidéo. Ne passez pas à l'étape suivante tant que vous ne comprenez pas clairement les nuances ci-dessus, sinon vous finirez par être plus confus qu'avant.

Une fois que vous avez terminé, allez-y et regardez cette conférence de Christina Lee :

Regardez cette conférence une fois, mais je veux que vous vous concentriez particulièrement de **28:20 à 32:50**. Pendant ces 4 minutes, elle donne une explication absolument magnifique sur **ce que font les deux opérateurs les plus utilisés** dans toute routine RxJava, observeOn() et subscribeOn(), et comment ils sont utilisés ensemble, en utilisant un exemple.

Ces opérateurs sont inclus ensemble comme l'une des constructions principales, dans les **4 constructions de RxJava** expliquées par Kaushik Gopal. Et croyez-moi, ils sont vraiment importants dans votre parcours avec la programmation réactive et RxJava en général.

**Créez un projet dans Android Studio** (si vous êtes un développeur Android) ou dans l'IDE de votre choix et exécutez exactement le même code que celui fourni par Christina. Une fois que vous l'avez configuré, vous pouvez jouer en changeant l'ordre de observeOn et subscribeOn et voir comment ils se comportent. Essayez d'ajouter plusieurs instances de ceux-ci et voyez qui domine et quel est le résultat. Vous obtiendrez une bonne compréhension des fonctions de ces opérateurs une fois que vous aurez fait cet exercice.

> **À ne pas faire** : YouTube pourrait recommander plusieurs conférences sur RxJava par **Jake Wharton**, mais je vous suggère fortement de les ignorer pour l'instant. Ces conférences peuvent devenir vraiment intimidantes après un certain temps et vous risqueriez de décrocher quelque part au milieu et peut-être même d'abandonner complètement RxJava. Alors, éloignez-vous d'elles pour l'instant.

### Phase 2

#### Le Désenchantement : le monde n'est pas tout soleil et arcs-en-ciel

Cette phase pourrait aussi s'appeler « La Lutte ». C'est la phase où vous devez commencer à mettre les mains dans le cambouis en écrivant du code RxJava réel.

**Je vous suggère de commencer par faire quelques appels API avec RxJava et j'ai déjà publié un article à cet effet : [Réseautage avec l'architecture Retrofit-RxJava-MVP](https://ayusch.com/networking-with-retrofit-rxjava-mvp/)**

Comprenez ce qui se passe ici. Vous avez probablement déjà fait quelques appels API dans votre parcours de développement Android en utilisant Retrofit/Volley. Mais cet article expliquera comment les assembler correctement afin d'obtenir une séparation des préoccupations et de rendre votre code plus modulaire et finalement facile à comprendre et à mettre à l'échelle à un stade ultérieur.

Il inclut également l'utilisation du modèle MVP qui est vraiment simple, mais vous pouvez l'omettre si cela devient trop technique. **Concentrez-vous simplement sur la création de l'Adaptateur, l'interface de service API et la UserTask**. Soyez assuré que tout cela n'est que du simple code Android. Vous pouvez invoquer UserTask depuis n'importe où et obtenir le résultat dans un callback.

Une fois que vous avez fait cela, vous aurez une idée de ce que c'est que de travailler avec RxJava.

Ensuite, vous devriez développer une application vous-même qui implique du réseautage. Vous pourriez utiliser le service web fakeJson/faire un client Twitter/consommer une API Rotten Tomatoes, ou tout ce qui implique du réseautage. Vous découvrirez comment différents opérateurs tels que **Map** et **FlatMap** sont utiles pour transformer vos observables en quelque chose qui répond à vos besoins.

En faisant cela, vous commencerez à vous sentir plus à l'aise avec les routines RxJava et observerez que la plupart du code est le même dans ces applications. Bien sûr, il y aura différents opérateurs utilisés et une différence dans vos modèles. Mais l'idée générale est quelque peu similaire.

Maintenant, vous êtes prêt pour la **Phase 3** et pour ce moment Eureka ?

### Phase 3

#### Eureka !

C'est la phase où vous sortirez de votre zone de confort et commencerez à explorer ce que RxJava peut faire pour votre application **Android** plutôt que simplement du réseautage. C'est ici que vous apprendrez l'art de la gestion d'état avec RxJava et comment vous pouvez « Rxifier » presque tout dans votre code. Dans cette section, je vous pousserai à commencer la gestion d'état avec RxJava.

C'est aussi le moment où vous êtes prêt à regarder toutes les conférences de **Jake Wharton** sur RxJava. En fait, ce sera votre tâche dans cette phase, mais d'abord, comprenons ce qu'est la gestion d'état.

**Qu'est-ce que la gestion d'état ?**

Prenons un **exemple**. Supposons que vous avez une application simple de connexion/inscription où vous demandez à l'utilisateur son nom d'utilisateur et son mot de passe et, lorsqu'il clique sur un bouton, vous le connectez/le dirigez vers une page d'inscription.

Dès que l'utilisateur entre ses détails et clique sur le bouton de soumission, un chargeur est affiché pendant que l'application envoie les données à un service backend et attend la réponse. Nous pouvons dire que actuellement, notre application est dans un état « en cours ».

Lorsque le résultat est retourné, l'application revient à l'état « **Inactif** ».

Pour élargir davantage, parlons du bouton de soumission. Lorsque les champs de texte sont vides, c'est-à-dire que l'utilisateur n'a encore rien entré, alors le bouton doit être désactivé. Ainsi, « désactivé » devient un état du bouton. Lorsque l'utilisateur a entré les informations et que les champs sont validés, le bouton doit être dans l'état « activé ».

Ainsi, vous voyez, tout ce que vous voyez à l'écran existe dans un état particulier. De ce bouton à la barre de progression, tout est dans un état particulier.

**Tout va bien, mais que faire maintenant ?**

Voici ce que je veux que vous fassiez.

**Commencez** par regarder cette conférence sur la gestion d'état par Jake Wharton :

Cette conférence est destinée aux développeurs **avancés** et j'ai dû la regarder au moins 10 fois pour comprendre ce qui se passait. Mais regarder une vidéo seule ne fera pas de vous un pro de RxJava. Vous devrez gérer l'état de vos applications en utilisant RxJava.

Pour pratiquer la gestion d'état, je suggère de prendre une idée simple/un seul écran et de commencer à gérer son état avec RxJava. Par exemple, si votre application inclut un écran de connexion/inscription, vous pouvez effectuer sa gestion d'état en utilisant RxJava comme mentionné ci-dessus.

**Voici quelques idées pour vous :**

* **Développez une application de connexion/inscription**. Après que l'utilisateur se connecte, consommez l'API Rotten Tomatoes. Permettez une fonctionnalité de recherche afin que l'utilisateur puisse rechercher des films selon ses préférences. Dans tout cela, les barres de progression et les animations doivent être des états qui seraient gérés dans les flux RxJava. Rx serait également utilisé pour faire des appels API.
* **Consultez [ce](https://github.com/kaushikgopal/RxJava-Android-Samples) dépôt** de Kaushik Gopal qui inclut un exemple de validation de formulaire avec RxJava. Clonez-le et essayez de comprendre le code. Une fois que vous êtes à l'aise, commencez à l'implémenter vous-même. Pensez à tous les états que vous pourriez ajouter pour augmenter la complexité. Par exemple, une case à cocher pour révéler le mot de passe.

Vous obtiendrez définitivement votre moment Eureka dans cette phase où vous réaliserez le vaste potentiel de RxJava et comment vous pouvez potentiellement tout faire avec et rendre votre code plus propre.

### Phase 4

#### Le ciel est la limite

Je laisserai cette section vide pour vous. Maintenant, c'est à vous de me dire toutes les manières créatives dont vous avez utilisé **RxJava** dans votre code et comment RxJava a rendu votre vie plus facile qu'avant. Une chose que j'ai remarquée en commençant à écrire ces blogs est qu'ils m'ont définitivement aidé à devenir un meilleur développeur Android car je suis responsable de tout ce que je poste.

Dans cet article, j'ai partagé tout ce qui a fonctionné pour moi et ce que je pense fonctionnera pour vous. Si vous avez des suggestions, faites-le moi savoir dans la section des commentaires ci-dessous. Je vous exhorte à partager vos apprentissages avec tout le monde et à vous aider mutuellement à grandir et à devenir de meilleurs ingénieurs.

Vous avez aimé ce que vous avez lu ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp** et **LinkedIn**.

Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain) et [Instagram](https://www.instagram.com/androidville/) où je **réponds** aux questions liées au **développement mobile, surtout Android et Flutter**.

**Si vous souhaitez rester informé de tous les derniers articles, abonnez-vous à la newsletter hebdomadaire en entrant votre adresse e-mail dans le formulaire en haut à droite de cette page.**