---
title: Comment implémenter une PWA et Barba.js dans des bornes internet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T18:12:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-pwa-and-barba-js-into-internet-kiosks-854d4895fd04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7QocFarKH2FtHu64nQA-JA.jpeg
tags:
- name: Android
  slug: android
- name: JavaScript
  slug: javascript
- name: PWA
  slug: pwa
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment implémenter une PWA et Barba.js dans des bornes internet
seo_desc: 'By Nino Mihovilić

  The project we’ll describe here is an interactive internet kiosk that’s used as
  an extension for the LikeUs mobile application. LikeUs is a mobile app that makes
  it easy for users to choose a place to go out, have coffee or listen t...'
---

Par Nino Mihovilić

Le projet que nous allons décrire ici est une borne internet interactive utilisée comme extension pour l'application mobile [LikeUs](https://likeus.hr/). LikeUs est une application mobile qui permet aux utilisateurs de choisir facilement un endroit pour sortir, prendre un café ou écouter un concert. Comme la rue Tkalčićeva à Zagreb est un lieu où de nombreux jeunes se retrouvent, nous avons décidé que c'était l'endroit idéal pour promouvoir l'application LikeUs hors ligne.

#### Implémentation du mode borne

L'un des premiers défis auxquels nous avons été confrontés était l'implémentation du mode navigateur borne sur notre appareil. Il s'agissait d'une Android Box et nous avons utilisé Chrome comme navigateur web pour exécuter l'application. Le mode navigateur borne est un mode dans lequel vous exécutez l'application en plein écran et sans aucune interface utilisateur du navigateur ou, dans notre cas, sans aucune interface utilisateur Android.

L'objectif est d'empêcher les utilisateurs d'exécuter autre chose que le contenu basé sur le navigateur. Comme il existe des centaines d'applications en mode borne, nous avons décidé d'utiliser l'une des applications disponibles plutôt que d'en construire une à partir de zéro.

Après quelques recherches, nous avons décidé d'utiliser l'application [Kiosk Browser Lockdown](https://www.android-kiosk.com/). Elle possède toutes les fonctionnalités que nous recherchions :

* Verrouillage de l'appareil sur une seule URL
* Masquage des options de la barre d'outils
* Masquage de l'écran des notifications
* Masquage de l'interface utilisateur Android

L'étape suivante a été de tester la PWA dans l'environnement Android et dans l'application Kiosk Browser. C'est alors que nous avons découvert que les choses ne se passeraient pas aussi facilement que prévu !

Le premier problème que nous avons rencontré était du côté frontend : le site web final semblait être une version mise à l'échelle du design initial, et cela était dû à certaines limitations d'écran et à un environnement de rendu différent. Comme la date limite approchait, nous n'avions pas assez de temps pour ajuster chaque élément en CSS pour correspondre aux contours du design initial, nous avons donc décidé de réduire l'échelle de l'ensemble du document.

C'était une approche raisonnable compte tenu de toutes les entrées que nous avions. Devoir tout tester une fois de plus était un gros inconvénient, mais nous devions être sûrs que tout fonctionnerait dans ce contexte.

Le deuxième problème était que les scripts externes comme Google Maps ne se chargeaient pas dans l'application Kiosk Browser avec la PWA, nous avons donc fait un petit ajustement. Nous avons démarré l'application Kiosk Browser, qui a supprimé l'interface utilisateur Android, puis nous avons quitté l'application Kiosk Browser et démarré la PWA en dehors de l'application Kiosk Browser. De cette manière, nous avons réussi à supprimer l'interface Android avec tous les scripts externes se chargeant comme prévu.

![Image](https://cdn-media-1.freecodecamp.org/images/HpUfeFTjyE05czMLe-X7GgCVO0uacIPiAjrE)

#### Développement d'une application web progressive

Après avoir examiné le brief et les spécifications du projet, la première chose qui nous est venue à l'esprit était... nous devrions faire une PWA (Progressive Web App). Une Progressive Web App est une application qui offre des capacités et des fonctionnalités similaires à celles des applications mobiles natives :

* Les service workers permettent aux applications d'afficher du contenu presque instantanément et de manière fiable car ils mettent en cache chaque requête
* Il est possible d'ajouter l'application à l'écran d'accueil comme une application native normale
* Les notifications push peuvent être implémentées pour des usages multiples
* L'application est rapide et fluide
* Elle utilise HTTPS et est facile à implémenter.

Après avoir évalué les demandes du client, toutes les fonctionnalités de la PWA répondaient à nos exigences.

Nos exigences étaient :

* Construire une application qui pourrait être utilisée sur un écran interactif
* L'application devrait utiliser une API existante que nous avons construite pour notre application mobile LikeUs
* L'appareil utilisé serait une Android Box
* L'accès à Internet serait restreint car l'application serait connectée à un réseau public (cela changerait plus tard)
* L'application devrait avoir une section supplémentaire pour les bannières et un système de gestion des bannières

Nous pourrions construire une application web avec notre API existante sans avoir à implémenter des fonctionnalités supplémentaires, et nous pourrions également construire un CMS (système de gestion de contenu) simple pour la gestion des bannières et des notifications push pour le rechargement du contenu. Comme l'accès à Internet serait restreint et instable, nous pourrions utiliser la fonctionnalité PWA pour mettre en cache les pages et les servir même lorsque l'application est hors ligne.

Assurez-vous de consulter ce [tutoriel approfondi](https://medium.com/@jewbre/service-workers-6a5c13c9a123) et cette explication sur les Service Workers.

#### Ajustement du système de gestion des bannières

L'application est divisée en deux sections. La section supérieure est la section des bannières, et la partie inférieure est la section principale divisée en onglets.

Nous avons deux types de bannières : des vidéos YouTube et des images. Comme les bannières peuvent être changées, nous devions développer un CMS. Nous avons développé un CMS simple dans lequel le client peut entrer des vidéos YouTube et des images dans un slider.

Le problème que nous avons rencontré ici était le rafraîchissement de l'application pour recharger le nouveau contenu des bannières. Vous voyez, parce que l'application utilisait Barba.js, elle ne se rafraîchissait jamais. Pour la faire fonctionner, nous avons utilisé une fonctionnalité cool de notre PWA : les notifications push. Les notifications push sont une fonctionnalité qui utilise l'API Notifications et l'API Push pour envoyer des messages du serveur au client.

Comment les notifications push ont-elles aidé à résoudre notre problème de rechargement de contenu ? La solution est assez simple et directe. Lorsque l'utilisateur change le contenu des bannières dans le CMS, nous envoyons une notification push à la PWA, puis la PWA se rafraîchit deux fois. La PWA doit être rafraîchie deux fois pour supprimer le cache et recharger le nouveau contenu.

#### Gestion des obstacles externes

Les bornes internet sont souvent placées dans des environnements extérieurs où la connexion internet est parfois instable et lente. Lorsque la connexion internet est publique et dans une rue assez fréquentée, vous rencontrez de nombreux problèmes lors de l'utilisation de la communication en temps réel et des API externes.

Une approche "bricolage" courante consiste à prolonger le temps de délai et à espérer que tout fonctionne bien. Même si ce n'est pas la méthode préférée, elle peut servir de solution de secours si tout le reste échoue.

Google Maps était l'une des API externes qui nous a causé beaucoup de maux de tête. Nous devions recharger et ajouter de nouvelles épingles, mais sur une connexion lente, cela était parfois impossible.

![Image](https://cdn-media-1.freecodecamp.org/images/hyvg705AuzUl8rybWXHDDk9stgbs7vsnTmec)

#### Équilibre entre contenu fixe et dynamique

L'optimisation ne s'applique pas seulement dans le domaine des techniques de cache avancées et des réseaux de diffusion de contenu. Un placement intelligent de la mise en page et la compréhension des éléments qui peuvent être "poussés hors" du flux de rechargement de la page peuvent réduire le nombre de requêtes et accélérer l'ensemble du flux de navigation.

Le contenu publicitaire dans la borne était hébergé sur YouTube : il s'agissait d'un slider vidéo qui se répétait sur toutes les pages. En dessous, nous avions le contenu principal avec une navigation en ligne. Lors de la sélection de différents éléments de navigation, le comportement par défaut du navigateur était de recharger l'ensemble de la page, y compris cette zone publicitaire fixe. C'est un cauchemar en termes de performance, surtout lorsqu'il y a des scripts externes tels que l'API YouTube.

La question ici est : comment recharger uniquement une partie spécifique de la page ? Eh bien, il n'y aura pas de rechargement du navigateur et la seule chose qui peut être faite est de changer le contenu en arrière-plan sans quitter la page.

En raison de l'analyse implémentée, nous devions mettre à jour l'URL en conséquence. Nous l'avons fait en utilisant la technologie PJAX (Push State Ajax). Cette technologie permet le préchargement du contenu et l'échange de nœuds DOM cibles en arrière-plan.

Pour éviter le scintillement du contenu, créez une simple transition en fondu qui se déclenche lorsque le contenu change. Comme il est chronophage de gérer manuellement tous les états de l'échange de contenu, nous avons utilisé une bibliothèque externe appelée Barba.js. Cette bibliothèque permet une gestion avancée des transitions et est compatible avec tous les frameworks d'animation.

![Image](https://cdn-media-1.freecodecamp.org/images/yzC0x5NH-VvltNXi-nOOXA871NO2gcJnlcQy)

Barba.js dispose d'un cache d'état interne qui peut être utilisé pour tirer parti du cache du navigateur et optimiser le temps de chargement. Le cache Barba est un objet Javascript global où chaque valeur est une Promesse qui doit être résolue.

#### Implémentation de l'analyse et des pages virtuelles

Nous voulions mesurer l'interaction des utilisateurs et les vues de pages. Parce que nous utilisons Barba.js, il s'agit essentiellement d'une application monopage sans rechargement de pages, donc l'astuce pour mesurer les vues de pages dans ce type d'application est d'utiliser des pages virtuelles. Ce sont des hits de pages envoyés à Google Analytics, sans recharger réellement la page.

La première étape consiste à inclure le code du [Google Tag Manager](https://developers.google.com/tag-manager/quickstart), puis à envoyer réellement des pages virtuelles à la couche de données. Nous pouvons le faire avec le snippet suivant :

```
dataLayer.push({ 'event': 'VirtualPageview', 'virtualPageURL': currentUrl, 'virtualPageTitle': title });
```

Ce snippet doit être appelé sur chaque nouvelle page. À chaque interaction de l'utilisateur qui ouvre une nouvelle "page", nous appelons ce snippet qui envoie l'URL de la page et le titre de la page à Google Analytics. De cette manière, nous pouvons suivre les vues de pages dans les applications monopages qui utilisent Barba.js ou toute autre technologie PJAX.

![Image](https://cdn-media-1.freecodecamp.org/images/pkJtXRjiySB4CfjP6v8gC1ujMJZFTSGe2qjI)

#### Conclusion

Lorsque vous travaillez dans un environnement spécifique, parfois la solution "par le livre" n'est pas votre seule solution. Il y a généralement une opportunité d'innover et d'utiliser certains outils et bibliothèques courants dans un environnement pas si standard avec un ensemble spécifique de défis.

_Publié à l'origine sur [www.bornfight.com](https://www.bornfight.com/blog/how-to-implement-pwa-and-barba-js-into-internet-kiosks/)._