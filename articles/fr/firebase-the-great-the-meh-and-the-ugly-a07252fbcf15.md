---
title: 'Firebase : le bon, le moyen et le mauvais'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-13T04:25:56.000Z'
originalURL: https://freecodecamp.org/news/firebase-the-great-the-meh-and-the-ugly-a07252fbcf15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AoarrKQjCE0zVJkxl9za8Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Firebase : le bon, le moyen et le mauvais'
seo_desc: 'By Pier Bover

  We jumped right into Firebase when Google announced it at Google I/O in May 2016.

  We were starting a single-page React application that needed to work on mobile via
  Cordova, and desktop via Electron. So Firebase seemed like a magical so...'
---

Par Pier Bover

Nous nous sommes lancés dans Firebase lorsque Google l'a annoncé lors de la Google I/O en mai 2016.

Nous commencions une application React en une seule page qui devait fonctionner sur mobile via Cordova, et sur desktop via Electron. Firebase semblait donc être une solution magique pour nous.

Maintenant, après 7 mois de travail avec Firebase presque quotidiennement, je suis prêt à partager notre expérience avec lui.

### Le Bon

#### Données en temps réel

Oui, c'est génial. Avec un peu de configuration et quelques sorcelleries de liaison de données, vous pouvez connecter vos vues avec vos données et elles changent magiquement lorsque les données changent.

Dans notre expérience, les performances étaient constamment excellentes, bien que Firebase soit conçu pour des millions d'utilisateurs, donc nous n'avons même pas effleuré la surface de la bête.

Nos utilisateurs sont toujours impressionnés par la rapidité avec laquelle tout fonctionne.

#### Hébergement statique surpuissant

L'hébergement Firebase est livré avec un CDN gratuit et SSL — tout fonctionnant sur la plateforme Google Cloud. Cela signifie que vous ne devriez avoir aucun problème à servir des fichiers à un nombre quelconque d'utilisateurs dans le monde entier.

Si vous cherchez un hébergement sans configuration pour votre prochaine application en une seule page ou votre site web statique, je considérerais vraiment Firebase comme une option, même si vous n'utilisez aucun des autres services de Google.

#### Super pouvoirs

Firebase vous fournit également un certain nombre de services et de SDK qui sont super faciles à intégrer tels que :

* Authentification OAuth
* Stockage de fichiers
* Sauvegardes de base de données
* Mise à l'échelle automatique
* CLI pour le déploiement et autres tâches
* Niveau gratuit

### Le Moyen

#### La console

Elle est belle et permet de faire un certain nombre de choses, mais elle n'est pas _si_ utile.

Le gestionnaire de base de données est en réalité un éditeur JSON glorifié. Super pour ce qu'il est, mais ce n'est pas la solution complète à laquelle je m'attendais. Si vous venez de WorkBench, Postico, Mongotron, ou même PHPMyAdmin, cela vous semblera un joli jouet.

Un autre aspect très limitant de la console est le manque de journaux détaillés ou d'analyses. Considérant qu'il s'agit de _Google-obsédé-par-les-données_, cela semble bizarre. Bien sûr, vous obtenez un joli graphique pour l'utilisation de la base de données, mais il n'y a aucun moyen de savoir combien de fois un fichier a été téléchargé depuis le stockage à moins que vous ne mettiez en place une solution vous-même.

#### Serverless ?

Firebase est un hébergement statique + API, rien de plus. Cette limitation n'est pas la fin du monde. Vous pouvez facilement résoudre ce problème en utilisant un serveur Node.js comme un autre client de Firebase, ce dont vous aurez probablement besoin pour de nombreuses tâches courantes telles que la création de miniatures, l'envoi d'e-mails à vos utilisateurs, etc.

Apparemment, il sera possible d'utiliser [Google Cloud Functions](https://cloud.google.com/functions/) (toujours en Alpha) avec Firebase, mais qui sait quand. Peut-être que cela sera annoncé lors de la Google I/O 2017.

**( Edit Mars 2017**: Firebase vient d'annoncer [Google Cloud Functions pour Firebase](https://firebase.googleblog.com/2017/03/introducing-cloud-functions-for-firebase.html) )

(**Edit Mai 2018**: Consultez [mon avis sur Firebase Cloud Functions](https://medium.com/@Pier/firebase-cloud-functions-the-great-the-meh-and-the-ugly-c4562c6dc65d))

#### Définition des règles de sécurité

Firebase utilise un fichier JSON avec du code Javascript dans des chaînes pour définir des règles sur la base de données et le stockage.

```
{  "rules": {    "users": {      "$uid": {        ".write": "$uid === auth.uid"      }    }  }}
```

Ce n'est pas aussi mauvais que cela en a l'air puisque vous pouvez utiliser [Bolt](https://github.com/firebase/bolt) pour rendre ce processus moins douloureux. Cependant, même lorsque vous utilisez Bolt, une fois que vous allez au-delà de quelques dizaines de règles simples, ce fichier devient ingérable.

Des services comme [Dream Factory](https://www.dreamfactory.com/) et [Graph Cool](https://www.graph.cool/) vous donnent un outil approprié pour le faire sans perdre la tête.

#### Technologie propriétaire

Lorsque Facebook a décidé de fermer Parse, de nombreux projets se sont retrouvés dans une situation difficile. Je doute honnêtement que cela arrive à Firebase, mais je peux comprendre la réticence à coupler votre stack technologique avec une plateforme tiers en tant que service.

#### Aucune façon de développer localement

Si vous voyagez fréquemment ou vivez dans un pays avec une mauvaise connectivité, sachez que vous ne pouvez pas travailler avec une installation locale. Vous ne pouvez pas simplement utiliser Docker ou Node et démarrer votre API.

### Le Mauvais

#### SDK Javascript limité

Il y a un certain nombre de fonctionnalités dans Firebase qui ne sont implémentées que dans leurs SDK iOS et Android.

La plus flagrante est le manque de persistance hors ligne lors de l'utilisation de Javascript. Votre application web, hybride ou ReactNative continuera à fonctionner si l'appareil perd momentanément la connectivité. Mais une fois que vous fermez l'application ou l'onglet, vos données seront perdues. C'est à vous d'implémenter un cache avec persistance. Cela peut vraiment être une entreprise sérieuse, surtout sur mobile.

Le SDK Javascript n'a même pas de moyen de mettre en cache les données (je ne suis pas sûr pour iOS ou Android). Si vous chargez `/products` et que vous avez besoin de ces données plus tard, vous devrez les recharger à moins de maintenir manuellement une connexion en arrière-plan. Ce n'est pas difficile à implémenter, mais encore une fois, pourquoi Firebase ne fournit-il pas un moyen _magique_ de le faire ?

#### Aucune façon d'interroger vos données correctement

Vous pouvez faire un filtrage et une pagination très basiques, mais à part cela, vous êtes seul.

Vraiment ? Google fournit un service de données sans capacités de recherche ou de filtrage ?

Oui. Vraiment.

Si vous souhaitez implémenter une fonctionnalité de recherche, vous devrez soit télécharger toutes les données et le faire dans le client, utiliser un serveur comme je l'ai décrit précédemment, ou implémenter un service tiers comme [Elastic](https://www.elastic.co/).

Les développeurs de Firebase ont déclaré que c'était par conception, afin qu'ils puissent assurer des performances élevées. D'accord. Mais pourquoi ne pas nous laisser, utilisateurs, décider si nous pouvons nous permettre de payer le prix de la performance pour notre cas d'utilisation ?

Oui, et oubliez les jointures ou quoi que ce soit de sophistiqué avec vos données. Ce qui m'amène à...

#### Modélisation de données stupide

> Traiter les relations avec NoSQL est difficile, traiter les relations avec Firebase est une vraie galère. - [Baptiste Jamin](https://crisp.im/blog/author/baptiste/)

Ce qu'il a dit.

La base de données Firebase est essentiellement un seul énorme fichier JSON. Il n'y a aucun moyen de déclarer des relations _un à plusieurs_ ou _plusieurs à plusieurs_. En pratique, cela signifie que vous allez finir par dupliquer vos données partout.

Cela ne semble pas si mauvais au début. Après tout, il est pratique de mettre le nom de l'utilisateur dans un message de chat, non ?

```
{ "author":"Pepito Flores", "message":"I want a taco!", "time": 1484269756951}
```

Le problème survient lorsque vous devez réellement modifier le nom de Pepito, car vous devrez le modifier **partout** où vous l'avez utilisé et pas seulement dans `/users`.

Dire à vos utilisateurs qu'ils ne peuvent pas modifier leur nom n'est généralement pas une option viable, donc :

1. Votre code client pour écrire et modifier les données dans Firebase deviendra dans de nombreux cas ingérable.
2. Documenter où vous avez dupliqué vos données sera difficile, pour le moins.

De plus, comme de nombreuses bases de données NoSQL comme [MongoDB](https://docs.mongodb.com/manual/core/data-model-design/#data-modeling-referencing) ou [RethinkDB](https://www.rethinkdb.com/docs/table-joins/) ont trouvé des moyens de contourner ce problème, je trouve difficile de croire que Google ne peut pas résoudre cela avec au moins des performances raisonnables.

### TL;DR

Firebase est génial pour des projets simples ou pour développer de petites fonctionnalités qui nécessitent des données en temps réel. Par exemple, un chat ou un système de notification. Ce sont les démonstrations impressionnantes de 30 minutes que vous voyez sur YouTube. Cela fonctionne également très bien si vos données sont des flux de _choses_ avec une structure simple, comme un service pour un jeu multijoueur en ligne.

Tout ce qui a des exigences de données plus complexes devient difficile ou même impossible avec Firebase. Les requêtes de base de données régulières _courantes_ sont dans la plupart des cas plus précieuses que les données en temps réel, et aussi impressionnant que de voir les choses changer, vous n'en avez probablement pas besoin.

Comme pour tout, choisissez le bon outil pour le travail.

### Addendum : ce dont Firebase a besoin pour être génial

1. De vraies capacités de requête. Recherche, jointures, le tout.
2. Une sorte de références comme MongoDB ou RethinkDB.
3. Une vraie persistance hors ligne avec Javascript.
4. Donnez-moi _plus_ d'analyses.
5. Une API de cache.

![Image](https://cdn-media-1.freecodecamp.org/images/OsPFhH5ZqUDHJmO5x3-RALnjXyyOZETdlcGs)

C'est tout.

### Addendum 2 : plus d'informations

Si vous lisez ceci, vous évaluez peut-être Firebase en tant que développeur ou CTO. Voici quelques autres articles qui pourraient vous aider à décider si Firebase pourrait fonctionner pour vous, et s'il vaut la peine d'investir du temps de développement supplémentaire pour l'évaluation.

[**Firebase : Le Bon, le Mauvais et le Vilain - RaizException - Blog des Développeurs Raizlabs**](https://www.raizlabs.com/dev/2016/12/firebase-case-study/)  
[_Dans le cadre de notre travail en tant que développeurs de logiciels chez Raizlabs, nous évaluons constamment les derniers outils de développement utilisés..._www.raizlabs.com](https://www.raizlabs.com/dev/2016/12/firebase-case-study/)[**Raisons de ne pas utiliser Firebase**](https://crisp.im/blog/why-you-should-never-use-firebase-realtime-database/)  
[_La construction d'applications en temps réel est aujourd'hui standard. Chez Crisp, nous avons utilisé Firebase en production pendant 9 mois, en commençant par..._crisp.im](https://crisp.im/blog/why-you-should-never-use-firebase-realtime-database/)