---
title: Comment déboguer les Progressive Web Apps à l'aide des outils de développement
  du navigateur
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2017-10-22T09:48:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-progressive-web-apps-using-browser-developer-tools-bad1cd3db784
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U3wBg7ofxcz0JPLMjjMd7A.png
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment déboguer les Progressive Web Apps à l'aide des outils de développement
  du navigateur
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  This tutorial explains what tools the Chrome and Firefox Dev Tools display that
  help you debug a Progressive Web App.


  There’s a lot to learn about this topic and the new browser APIs...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/hogzcxQxADPY1HvLDaMW3MsnsgrFaJJsyP4L)

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Ce tutoriel explique quels outils les DevTools de Chrome et Firefox affichent pour vous aider à déboguer une Progressive Web App.

> Il y a beaucoup à apprendre sur ce sujet et sur les nouvelles API des navigateurs. Je publie beaucoup de contenu connexe sur mon [blog sur le développement frontend](https://flaviocopes.com), ne le manquez pas ! ?

### Qu'est-ce qu'une Progressive Web App ?

Tout d'abord. Une [Progressive Web App](https://www.writesoftware.org/course/progressive-web-apps) (PWA) est une application qui peut fournir des **fonctionnalités supplémentaires** basées sur le support de l'appareil, telles que :

* La capacité de travailler hors ligne
* Les notifications push
* Une apparence et une rapidité d'application presque natives
* La mise en cache locale des ressources

Mais elle fonctionne toujours parfaitement comme un site web normal sur les appareils qui ne supportent pas les dernières technologies.

### Un bref aperçu des outils de développement Chrome

Commençons par Chrome. Une fois que vous [ouvrez les DevTools](https://developer.chrome.com/devtools#access), vous voyez plusieurs panneaux. Vous connaissez peut-être déjà bon nombre de ces panneaux, comme Console, Elements ou Network. Vous les utilisez quotidiennement lors de la création de sites web ou d'applications web.

Le panneau **Application** est récent, mais contient des outils familiers. À l'été 2016, l'onglet Resources a été renommé « Application ». Cela a regroupé toutes les fonctionnalités qui distinguent généralement les applications web des pages web. Nous l'examinerons en détail bientôt.

![Image](https://cdn-media-1.freecodecamp.org/images/5-zR5GMX85x-zBEP5OHvzxjktwhS17FPHHVa)

### Un exemple concret

Ce tutoriel propose une exploration de la Progressive Web App disponible sur [https://events.google.com/io2016/](https://events.google.com/io2016/). Vous pouvez ouvrir Chrome et suivre exactement les mêmes étapes détaillées ici, sans rien avoir à configurer localement.

### Simuler un appareil

Activons d'abord le **Device Mode** des DevTools de Chrome. Cela vous donne la possibilité d'émuler un appareil dans votre navigateur. Nous choisissons un appareil Android, car actuellement les PWA ne montrent leur plein potentiel que sur Android. Le fait que [Safari commence à travailler sur le support des Service Workers](https://webkit.org/status/#?search=service) semble être un pas dans la bonne direction pour le support d'iOS et de Safari Desktop.

![Image](https://cdn-media-1.freecodecamp.org/images/tBUVv5uQIKOI05L06U35IhT9Pgb8hYD3qjNC)

### Le panneau Application en détail

Le panneau Application regroupe de nombreux éléments clés pour les Progressive Web Apps.

#### Manifeste

Le manifeste débloque la possibilité d'offrir aux utilisateurs l'option **Ajouter à l'écran d'accueil**. Il fournit une série de détails sur la manière dont l'application doit se comporter une fois installée sur l'appareil. S'il y a un problème avec la façon dont vous avez défini le manifeste, il signalera l'erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/f9wqv2N27HqV-hhEBZyJmDq39DR186PFTjsE)

Vous y voyez le nom de l'application, un nom court pour l'écran d'accueil, un aperçu des icônes et quelques détails sur la présentation :

* **Start URL** : l'URL que l'appareil chargera lorsque l'utilisateur lancera l'application web depuis l'écran d'accueil. Vous pouvez ajouter un identifiant de campagne pour segmenter les accès PWA dans les analyses.
* **Theme color** : indique un thème pour votre site. Chrome l'utilise pour colorer certains éléments de l'interface utilisateur du navigateur, comme la barre d'adresse. Cela peut être personnalisé par page à l'aide de la balise méta `<meta name="theme-colo`r">, mais le spécifier dans le manifeste fournit une couleur de thème pour tout le site lorsque l'application est lancée depuis l'écran d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/au4cS0j1dhKt7ZCsS1g6R4Rstxpv1LXjjYp9)
_Exemple d'utilisation de l'option theme color dans le manifeste pour changer les couleurs de l'interface utilisateur du navigateur_

* **Background color** : spécifier la couleur d'arrière-plan de votre application web dans le manifeste permet au navigateur d'afficher cette couleur sur l'écran de chargement avant même que le CSS ne soit disponible. Cela produit une expérience plus agréable pour l'utilisateur. Dès que le CSS est disponible, cette valeur est écrasée par le style réel de l'application web.
* **Orientation** : spécifie l'orientation par défaut, et peut être n'importe quelle valeur parmi `any`, `natural`, `landscape`, `portrait` et d'autres options détaillées dans le [Screen Orientation API Working Draft](https://www.w3.org/TR/screen-orientation/#orientationlocktype-enum).
* **Display** : définit la manière dont l'application est présentée. Les valeurs valides sont `fullscreen` qui ouvre l'application sur toute la taille de l'écran. `standalone` affiche la barre d'état standard de l'appareil et le bouton de retour du système. `minimal-ui` fournit à l'utilisateur au moins les boutons de retour, d'avance et de rechargement. Et `browser` affiche l'interface utilisateur normale du navigateur, incluant la barre d'adresse.

En haut de l'onglet Manifest, cliquer sur le lien `manifest.json` nous amène au **panneau Sources**, avec le code source complet du manifeste.

![Image](https://cdn-media-1.freecodecamp.org/images/idtoNYUnbag4So8RRkoMHO2BgbVW8tb3U2Qr)
_Le code source du fichier manifest.json_

Le Manifeste vous permet de définir de nombreux autres champs. Je suggère de consulter directement le [Web App Manifest Working Draft](https://www.w3.org/TR/appmanifest) pour en savoir plus.

La dernière chose sur cet écran, qui est assez importante, est le lien **Add to home screen**. Sur Chrome Desktop, cela déclenche l'ajout de l'application à l'étagère. Sur mobile, cela invite à installer l'application (ajouter l'icône à l'écran d'accueil) :

![Image](https://cdn-media-1.freecodecamp.org/images/8X7qJMqXjTtE4QQu3avPdYFnDOxEo-aOBOfW)

#### Service Workers

Ensuite, dans la liste, il y a l'onglet Service Workers. Les [Service Workers](https://www.writesoftware.org/topic/service-workers) sont la technologie qui permet à une PWA de fonctionner hors ligne. Ils vous permettent d'intercepter les requêtes réseau et d'utiliser l'API Cache pour stocker des ressources localement.

![Image](https://cdn-media-1.freecodecamp.org/images/rvwow7ax0H1h632yCf955P3d9Rbb5GttHaxN)

Depuis cet écran, vous pouvez **forcer le mode hors ligne** dans l'onglet en cochant la case **Offline** :

![Image](https://cdn-media-1.freecodecamp.org/images/R7L76G4lK7aeCp6WZ256BE5c2lrUXo279kE7)
_Mode hors ligne forcé, reflété dans l'application_

Le mode hors ligne peut également être forcé dans l'écran Device Mode, en plus de la **limitation du réseau** (network throttling).

**Update on reload** est très utile lors du débogage. Les Service Workers sont installés sur l'appareil lorsqu'ils sont chargés pour la première fois. Ils ne sont pas mis à jour tant que le code du Service Worker ne change pas, ils ne sont donc pas comme des ressources ordinaires.

Mais même si vous mettez à jour le service worker, il ne sera pas utilisé par la page web tant que l'ancien service worker ne pourra pas être supprimé — c'est-à-dire jusqu'à ce que l'utilisateur ferme tous les onglets qui pointent vers l'application web. Cette case à cocher force la mise à jour.

**Bypass for network** vous permet de désactiver complètement la mise en cache activée par le Service Worker. Cela empêche l'application d'utiliser les ressources mises en cache lorsque vous voulez un accès direct depuis le réseau. Encore une fois, très utile lors du débogage.

**Show all** est une option qui permet un accès rapide à **tous** les Service Workers installés sur l'appareil.

Chaque Service Worker est listé avec un indicateur d'état que vous pouvez arrêter et redémarrer. En cliquant sur le nom du fichier, vous pouvez inspecter la source et vous y brancher à l'aide du débogueur JavaScript intégré :

![Image](https://cdn-media-1.freecodecamp.org/images/X0YJ2aNwXpkk8EjF5eA6XEG62ymk9PQf06fe)

Ce que vous utiliserez probablement le plus est la simulation des événements du cycle de vie du Service Worker. Vous pouvez forcer les événements suivants :

* **Update** forcera une mise à jour du Service Worker
* **Push** émule un événement push
* **Sync** émule un événement de synchronisation en arrière-plan, qui permet à l'utilisateur d'effectuer des actions hors ligne et de les communiquer au serveur une fois en ligne
* **Unregister** désinscrit le Service Worker, afin que vous puissiez repartir de zéro

#### Effacer le stockage

L'onglet Clear storage vous montre la taille totale du stockage utilisé par votre application web, l'espace qu'il vous reste, et vous permet de choisir précisément quel stockage effacer.

![Image](https://cdn-media-1.freecodecamp.org/images/bjIDgshhdrgVQqy8JmcdxtE1wGGMh1mvxJwX)

#### Stockage

L'onglet Storage contient des outils pour interagir avec les options de stockage habituelles comme **Local/Session Storage**, **IndexedDB** et **Cookies**. Ce n'est pas spécifique aux Service Workers, je n'entrerai donc pas dans les détails ici.

![Image](https://cdn-media-1.freecodecamp.org/images/YLnx1u4jSbBfcC-TFU55tiQBqoGnlJmZmpFG)

#### Cache

En ignorant l'onglet Application Cache — qui est une technologie obsolète — l'onglet **Cache Storage** est essentiel pour les Service Workers. Il affiche le contenu des ressources stockées à l'aide de l'API Cache, qui fait partie de la spécification des Service Workers. Il n'est pas limité à l'utilisation par les Service Workers.

La [démo Google Chrome Cache Storage](https://googlechrome.github.io/devtools-samples/whatsnew/m62/cache.html) est un bon moyen de voir ce qui se passe lorsque vous ajoutez un élément au cache.

![Image](https://cdn-media-1.freecodecamp.org/images/A5glHAb3TPHI-e9qHw31udOQ6I6fWNtP2JW9)

Au début, le cache n'est pas utilisé du tout :

![Image](https://cdn-media-1.freecodecamp.org/images/rdjTafv0pduYmCVRKMAZDqakUGtK5QCpLIxI)

Appuyer sur le bouton de cache **Create WNDT62** déclenche la création du cache :

![Image](https://cdn-media-1.freecodecamp.org/images/BZq0oaNAE7ESHywH2ZQdcvZ28kqt57Trru-O)

Ensuite, **Create RESOURCE_A** dans WNDT62 ajoute un élément dans le cache :

![Image](https://cdn-media-1.freecodecamp.org/images/TBaM47rVS2FihLDLYkCicNcEC8Hl63cN9etV)

Appuyer sur **Update RESOURCE_A** incrémente la valeur du corps, que nous pouvons inspecter en utilisant :

```
caches.open('WNDT62').then(function(cache) {  return cache.match('RESOURCE_A').then((res) => {    res.text().then(body => console.log(body));  })})
```

Chaque fois que vous appuyez sur Update RESOURCE_A, la valeur retournée est incrémentée.

Appuyer sur Delete WNDT62 supprime le cache, libère l'espace qui était occupé par les ressources et restaure l'état initial de l'application.

Lors du chargement de ressources mises en cache par les Service Workers à l'aide de l'API Cache, le panneau Network des DevTools indique qu'elles proviennent des Service Workers :

![Image](https://cdn-media-1.freecodecamp.org/images/OUqVR6214WW9L3EaPpuCwFfxZ-KxIYNXEH47)

### Et Firefox ?

Firefox offre un excellent support pour les Progressive Web Apps ainsi que pour les Service Workers. Mais ses outils de développement ne les affichent pas de manière aussi proéminente que les outils de développement de Chrome. Néanmoins, ils sont là, sous le menu `Outils |> Développement Web |> Service Workers`.

![Image](https://cdn-media-1.freecodecamp.org/images/NDBuI1PcF9xppqaDeiLFJsWh0x5JNiEFBWBr)

De là, vous pouvez désinscrire n'importe quel Service Worker et ouvrir le code du worker dans le débogueur pour n'importe quel type de worker (Web Workers également). Vous pouvez également déclencher un événement `push` de l'API Push pour déboguer les événements Push.

Vous ne pouvez pas simuler d'événements ou forcer la mise à jour ou le contournement des Service Workers comme dans Chrome. J'espère que cela sera possible bientôt dans Firefox pour une expérience de test plus facile.

Comme dans Chrome, lorsqu'une ressource est mise en cache par les Service Workers dans le panneau Network des outils de développement à l'aide de l'[API Cache](https://www.writesoftware.org/topic/cache-api), elle affiche `service worker` sous la colonne Transféré :

![Image](https://cdn-media-1.freecodecamp.org/images/7uf6oULpdGxR7FeGoCsrxJWyiv3pOg5Gjj5K)

### Conclusion

Les Progressive Web Apps sont l'un des tournants décisifs pour améliorer le Web sur mobile et offrir aux utilisateurs une bonne expérience en dehors des applications natives.

Les navigateurs, en particulier Chrome, fournissent de bons outils autour d'elles.

Google propose également [Lighthouse](https://developers.google.com/web/tools/lighthouse/) dans le cadre de ses outils de navigation, qui peut être installé séparément dans les DevTools de Chrome. Il fournit des vérifications automatiques pour s'assurer que votre application web est construite de manière optimale et inclut le support des Service Workers. Un outil incroyablement utile, ne le manquez pas.

Si vous avez apprécié cet article, n'hésitez pas à m'applaudir pour que plus de personnes le voient. Merci !

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)