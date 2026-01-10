---
title: Pourquoi les Applications Web Progressives sont l'Avenir du Développement Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T18:20:16.000Z'
originalURL: https://freecodecamp.org/news/why-progressive-web-apps-are-the-future-of-web-development-13db7dd5f640
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oc4pOoEeR_QMrCA6LkF5Kw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: development
  slug: development
- name: PWA
  slug: pwa
- name: web
  slug: web
- name: Web Development
  slug: web-development
seo_title: Pourquoi les Applications Web Progressives sont l'Avenir du Développement
  Web
seo_desc: 'By Tushar Agrawal


  “The key is to embrace disruption and change early. Don’t react to it decades later.
  You can’t fight innovation.” — Ryan Kavanaugh


  Lately, there’s been a lot of buzz around PWAs with many claiming it to be future
  of web developmen...'
---

Par Tushar Agrawal

> « La clé est d'embrasser la disruption et le changement tôt. Ne réagissez pas des décennies plus tard. Vous ne pouvez pas lutter contre l'innovation. » — Ryan Kavanaugh

Récemment, il y a eu beaucoup de buzz autour des PWAs, beaucoup affirmant qu'elles représentent l'avenir du développement web, surtout en termes d'appareils mobiles. À sa base, une Application Web Progressive (PWA) est simplement une application web qui utilise des techniques web modernes pour offrir une expérience similaire à une application native aux utilisateurs. Ce sont des applications web avec une amélioration progressive pour implémenter des fonctionnalités comme le cache, la synchronisation en arrière-plan et les notifications push.

Même si les [PWAs](https://developers.google.com/web/progressive-web-apps/) existent depuis plus de deux ans maintenant, la réponse est assez décevante. Peu de grands acteurs ont adopté cette philosophie, mais la plupart ne l'ont pas vraiment embrassée. Chrome et Mozilla sont peut-être les meilleurs navigateurs pour tester vos PWAs, car Apple n'a pas encore adopté cette technologie.

### PWA — Est-ce vraiment bien ?

D'un côté, nous avons des applications natives qui sont sans aucun doute rapides et efficaces dans la plupart des cas. De l'autre, il y a des sites web qui sont plutôt lents et, avec les problèmes de connectivité, cela ne fait qu'empirer.

Le projet Accelerated Mobile Pages ([AMP](https://www.ampproject.org/)), dirigé par Twitter et Google, a été lancé en 2016 pour résoudre uniquement ces problèmes de connexion lente. Les PWAs fonctionnent sans faille dans tous les scénarios possibles. Avec une bonne connexion, il n'y a jamais de problème. Le problème survient lorsque nous n'avons pas de connexion et que nous sommes accueillis par une page d'erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0DOKUYA7bHE9COGpJw5q0Q.png)

Mais cela peut devenir très ennuyeux si nous avons une connexion lente. La page semble se charger et tout ce que nous voyons est un écran blanc. Nous attendons, attendons et attendons, mais la page ne semble jamais se charger. C'est là que la PWA vient à notre secours. Le meilleur aspect des PWAs — vous obtenez la meilleure expérience utilisateur possible, même avec une connectivité lente ou sans connectivité (oui, vous avez bien lu...).

### Pourquoi il est logique d'utiliser une PWA

Selon une étude, un utilisateur moyen passe 80 % de son temps total sur les applications sur seulement trois de ses applications (pour moi, c'est Chrome, Quora et Medium).

Les autres applications restent inactives la plupart du temps, consommant une précieuse partie de la mémoire. De plus, il coûte environ dix fois plus cher de développer une application plutôt que de créer un site web pour la même chose. Le coût peut être beaucoup plus élevé si vous prévoyez de développer et de maintenir des bases de code séparées pour différentes plateformes comme Android, iOS et le web.

### Fonctionnalités des applications natives que les PWAs peuvent utiliser

* Notifications push
* Plein écran
* Fonctionnement hors ligne
* Écran de démarrage pris en charge, donnant une sensation plus proche d'une application

Les PWAs peuvent utiliser beaucoup plus de fonctionnalités de ce type. Les points ci-dessus ne sont là que pour vous donner une idée de ce dont les PWAs sont capables. Cependant, il existe certaines fonctionnalités traditionnelles dont seules les applications natives bénéficient pour l'instant.

### Fonctionnalités des applications natives que les PWAs ne peuvent pas utiliser pour l'instant

* Pas d'accès ou accès très restreint aux différents capteurs matériels
* Alarmes
* Accès au répertoire téléphonique
* Modification des paramètres système

Les PWAs évoluent assez rapidement et nous pouvons espérer voir ces fonctionnalités entrer en action très bientôt.

### Deux composants majeurs d'une PWA

**Manifest de l'application**
C'est un fichier JSON qui définit une icône d'application, comment lancer l'application (autonome, plein écran, dans le navigateur, etc.), et toute information connexe. Il est situé à la racine de votre application. Un lien vers ce fichier est requis sur chaque page qui doit être rendue.

Il est ajouté dans la section head de la page HTML :
```html
<link rel="manifest" href="/manifest.json">
```

**Service Worker**
Le service worker est l'endroit où la plupart de la magie se produit. Ce n'est rien d'autre que du code JavaScript qui agit comme des proxys programmables, uniquement responsables de l'interception et de la réponse aux requêtes réseau. Puisqu'il agit comme un proxy et peut être facilement programmable, l'application doit être servie via HTTPS pour garder les données sécurisées.

Il est important de noter que le service worker met en cache la réponse réelle, y compris tous les en-têtes HTTP, plutôt que simplement les données de réponse. Cela signifie que votre application peut simplement effectuer des requêtes réseau et traiter la réponse sans aucun code spécifique pour gérer le cache.

### Comment commencer ?

Le meilleur aspect pour commencer est que c'est beaucoup plus facile que cela en a l'air. En fait, il est tout à fait possible de prendre un site existant et de le convertir en PWA. Je vous suggère vivement de regarder ceci si vous avez l'intention de développer une PWA.

#### Merci d'avoir lu ! Si vous avez aimé, soutenez en applaudissant et en partageant l'article.