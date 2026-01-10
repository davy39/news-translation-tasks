---
title: Un guide rapide sur MeteorJS – Qu'est-ce que c'est et qui devrait l'utiliser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T23:40:40.000Z'
originalURL: https://freecodecamp.org/news/what-is-meteorjs-and-who-should-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/meteor-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Meteor
  slug: meteor
seo_title: Un guide rapide sur MeteorJS – Qu'est-ce que c'est et qui devrait l'utiliser
seo_desc: 'By Yehuda Clinton

  MeteorJS is a do-it-all framework for making JavaScript applications. If you enjoy
  making websites in HTML, CSS, and JavaScript, then you can use those skills to make
  apps for your PC or phone.

  By default when you do “meteor create ...'
---

Par Yehuda Clinton

MeteorJS est un framework tout-en-un pour créer des applications JavaScript. Si vous aimez créer des sites web en HTML, CSS et JavaScript, alors vous pouvez utiliser ces compétences pour créer des apps pour votre PC ou votre téléphone.

Par défaut, lorsque vous exécutez « meteor create myapp & cd myapp & meteor run », il sert une page web HTML/JavaScript ainsi qu'un backend Node/MongoDB (qui n'est pas utilisé pour le moment).

Nodejs est simplement le nom du JavaScript qui réside sur le serveur. Mongodb est la base de données NoSQL (not-only-structured-query-language) utilisée par Meteor.

## Commençons une démonstration d'application mobile

Pour commencer, vous tapez « meteor add-platform android » puis « meteor run android ». Cela exécutera cette application sur votre téléphone [branchée](https://www.xda-developers.com/install-adb-windows-macos-linux/) (ou [dispositif virtuel](https://medium.com/androiddevelopers/developing-for-android-11-with-the-android-emulator-a9486af2d7ef)) en utilisant votre ordinateur comme serveur (si vous avez créé quelque chose dans le backend). Vous pouvez faire la même chose avec un iPhone en utilisant un Mac.

Les fichiers JS, HTML et CSS sont organisés de manière intuitive dans les répertoires 'server' et 'client'. Il s'agit du modèle de conception MVC (modèle vue contrôleur).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/mobile-1.png)

Les interfaces mobiles Android et iOS sont gérées par Apache Cordova. Vous ne le verrez pas dans une application web de base. Cependant, vous devez absolument en être conscient si vous utilisez des fonctions matérielles du téléphone.

La plateforme de base vous permet d'ajouter n'importe quel autre framework que vous souhaitez au backend ou au frontend. Tout, d'Angular, Express, React et Vue peut être installé sur Meteor.

Les frameworks CSS populaires comme Material-UI sont généralement utilisés pour faciliter le travail de conception. Cependant, vous n'avez pas besoin d'ajouter d'autre framework du tout. Meteor vient avec une excellente méthode [Publish/Subscribe](https://docs.meteor.com/api/pubsub.html), [Blaze handlebars](http://blazejs.org/) et des comptes utilisateurs, et bien plus encore.

## Au-delà de la démonstration

En plus des plugins disponibles avec "[meteor add](https://atmospherejs.com/)", vous avez également accès à tous les plugins npm et cordova. Vous pouvez utiliser "meteor npm install" pour y accéder.

Vous pouvez même ajouter une plateforme de bureau en utilisant [Meteor-desktop](https://github.com/sharekey/meteor-desktop/). Cela utilise le framework Electron. Vous pouvez ensuite créer des applications Windows, Mac et Linux. Espérons que cette fonctionnalité sera prise en charge nativement dans la version 2.0 de Meteor.

Il existe une communauté saine de développeurs Meteor dans différents forums depuis 2012. La documentation sur guide.meteor.com est plus complète et claire par rapport à la plupart des frameworks.

Bien que cela puisse sembler être le raccourci parfait pour un nouveau développeur, je vous met en garde : N'incluez pas de package ou de framework dans votre projet tant que vous n'êtes pas sûr de savoir comment il fonctionne.

Meteor est bon pour l'intégration, mais cela peut prendre un travail supplémentaire pour combiner différents packages. Ne vous contentez pas de chercher une liste de packages en espérant qu'ils fonctionneront tous ensemble parfaitement.

Meteor est un excellent outil pour un débutant cherchant à être introduit à l'étendue de la développement d'applications et au processus de création d'une application simple.

## **Production**

Meteor peut, bien sûr, créer des applications web et mobiles complètes pour la production. Il est utilisé par plusieurs entreprises de taille moyenne et grandes comme Ikea et Workpop.

Pour un développement et une optimisation faciles, vous pouvez utiliser l'hébergement [Galaxy](https://www.meteor.com/hosting). Galaxy vous aidera à passer en production sans aucune connaissance en administration système requise.

Si vous avez des connaissances et du temps, vous pouvez l'héberger sur votre propre serveur/VPC. Par exemple, une instance AWS Lightsail à 5 $ par mois peut héberger une application avec une centaine d'utilisateurs.

L'auto-hébergement et la construction fonctionnent de la même manière que vous avez commencé la démonstration Meteor. Cependant, au lieu de "meteor run", vous allez construire (meteor build) – votre backend en une application nodeJS standard, et votre mobile en une application [APK signée](https://medium.com/@yehudaclinton/how-to-make-an-android-app-with-meteorjs-62ae5b22623a) ou IOS.

Il y a eu des rumeurs au fil des ans selon lesquelles Meteor ne se met pas à l'échelle. Cela a été largement réfuté et peut être surmonté avec diverses techniques.

La sécurité de Meteor a les normes élevées typiques d'un projet open-source bien maintenu. Suivez attentivement le [guide de sécurité](https://guide.meteor.com/security.html) et méfiez-vous des [injections noSQL](https://medium.com/rangeforce/meteor-blind-nosql-injection-29211775cd01).

## Avantages de Meteor

* Une communauté diversifiée de contributeurs donne au framework une résilience et une longévité spéciales. La plupart des autres frameworks sont créés par une seule méga entreprise technologique. Cela pourrait signifier que le projet sera mis de côté s'ils ne voient pas de retour sur investissement. Avec Meteor, la direction de son développement suit de près ses utilisateurs.
* Il est multiplateforme. Google Flutter ne fonctionnera pas sur l'iPhone d'Apple. Meteor vous permet de faire toutes les implémentations de votre application en un seul endroit.
* Il est intégré aux gestionnaires MongoDB et il y a un support pour GraphQL.

## Inconvénients de Meteor

* Si les développeurs placent trop de confiance dans différents packages pré-construits, ils peuvent entrer en conflit les uns avec les autres.
* Si vous créez simplement une application web, il pourrait être plus simple d'utiliser Express.
* Vous ne pouvez pas faire fonctionner une application web mobile aussi efficacement qu'avec du natif.

En conclusion, Meteor est un framework efficace qui peut vous aider à réduire le temps de développement et à faciliter la maintenance des applications.

Si vous cherchez à en savoir plus sur la création d'applications en JavaScript, lisez ce nouveau [livre de Manning](https://www.manning.com/books/the-joy-of-javascript?utm_source=affiliate&utm_medium=affiliate&a_aid=bootstrap-it&a_bid=e5f7023c&chan=VPN) Publications.