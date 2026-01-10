---
title: 'Applications haute performance : Multiplexage, Débounce, Polices système et
  autres astuces'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-22T17:36:58.000Z'
originalURL: https://freecodecamp.org/news/high-performance-apps-multiplexing-debouncing-system-fonts-and-other-tricks-37c6fd3d7b2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y9Wf1Py9tQd3nc4l0AFsCQ.png
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
seo_title: 'Applications haute performance : Multiplexage, Débounce, Polices système
  et autres astuces'
seo_desc: 'By Atila Fassina

  Here are some performance tips for your client-side application that you can start
  using immediately.

  These will boost your app’s perceived performance significantly. And most of them
  only require quick tweaks to your app.

  Preload yo...'
---

Par Atila Fassina

Voici quelques conseils de performance pour votre application côté client que vous pouvez commencer à utiliser immédiatement.

Cela améliorera significativement la [performance perçue](https://en.wikipedia.org/wiki/Perceived_performance) de votre application. Et la plupart d'entre eux ne nécessitent que des ajustements rapides à votre application.

### Préchargez vos ressources

`rel="preload"` est un moyen de laisser votre navigateur savoir qu'une ressource spécifique est importante. Ainsi, votre navigateur récupérera la ressource aussi rapidement que possible. Ensuite, il la stockera localement jusqu'à ce qu'il trouve la référence attendue dans le DOM.

Voici quelques exemples d'utilisation d'un `link` avec cet attribut :

L'attribut `as` est obligatoire ici, car il indique au navigateur le type de fichier qu'il récupère. Ainsi, il peut interpréter la demande et ajouter les en-têtes appropriés. Sinon, votre demande aurait le `mime/type` incorrect, donc votre navigateur ne pourrait pas le parser.

Au fait, `mime/type` est la déclaration de type de fichier que les développeurs utilisent sur le web. Cela ressemble aux extensions de fichier sur votre système d'exploitation de bureau. Si vous avez le `mime/type` incorrect, le navigateur ne saura pas comment parser le fichier.

Les fichiers de police sont un peu plus délicats à précharger. Voici quelques points à garder à l'esprit :

* `crossorigin` — Le [W3C](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium) exige que les requêtes de police soient anonymes. En résumé, cela signifie que même lorsque la requête provient du même domaine, elle sera traitée comme une requête cross-origin.
* `type` — Cela spécifie le format que le navigateur doit utiliser lors de la récupération de la police.

De plus, assurez-vous d'ajouter uniquement le premier format à votre déclaration `font-face`. Le préchargement de plusieurs formats de police est contraire aux bonnes pratiques, offre une mauvaise expérience utilisateur et gaspille la bande passante de vos utilisateurs.

Vous pouvez [en savoir plus sur le préchargement ici](https://caniuse.com/#search=preload).

### Utilisez des polices spécifiques au système d'exploitation

En utilisant des polices système, il est possible d'émuler l'apparence et la convivialité du système d'exploitation de vos utilisateurs. Ainsi, votre application a plus de chances de ressembler à une application native, tout en évitant à l'utilisateur de télécharger davantage de ressources.

Analysons de plus près chacune de ces déclarations :

* _apple-system_ : comme son nom l'indique, ces polices ciblent les systèmes liés à OSX/iOS
* _system-ui_ : ces polices ciblent la police système, quel que soit le système
* _BlinkMacSystemFont_ : la police de Chrome sur MacOS
* _Segoe UI_ : Windows/Windows Phone
* _Roboto_ : Android

Cette solution est largement utilisée même si de nombreux développeurs ne la connaissent pas encore. Par exemple, au moment de la rédaction de cet article, elle est utilisée chez :

* GitHub
* Wordpress
* Bootstrap
* Medium
* Ghost
* Zeit

Et probablement d'autres que je ne connais pas encore.

### Débounce et throttle les appels à votre serveur

Certains événements se déclenchent beaucoup plus de fois que nous ne le souhaitons. Par exemple : resize, scroll, keypress/keydown/keyup, ou change.

Resize et scroll, par exemple, se déclenchent à _chaque_ pixel. Cela représente beaucoup de bruit si vous souhaitez simplement ajuster certains éléments sur un breakpoint, ou ajouter une classe à un en-tête lorsque l'utilisateur fait défiler la page.

Si vous avez un autocomplete, par exemple, vous ne voulez pas qu'il se déclenche à chaque pression de touche. Dans la plupart des cas, il serait bon de commencer l'autocomplétion après le 3ème caractère. Surtout si vous prévoyez de récupérer des informations pour cela.

**Debounce** retarde votre déclencheur jusqu'à ce que l'événement cesse de se déclencher pendant une durée donnée (généralement 500 millisecondes).

**Throttle** retarde votre déclencheur s'il tente de se déclencher plus souvent qu'un intervalle donné (généralement 250 millisecondes).

### Utilisez async/defer

Vous vous souvenez de la bonne vieille fonction `window.onload` ? Ou de déplacer tous les scripts en bas de votre HTML ? Eh bien, `async` et `defer` sont là pour vous offrir de meilleures options.

**Async** téléchargera votre script pendant le parsing du HTML. Il l'exécutera de manière asynchrone (si possible) — indépendamment de l'endroit où il est déclaré.

**Defer** téléchargera également votre script pendant le parsing du HTML, bien qu'il n'essayera d'exécuter votre script qu'après que le parseur ait terminé. De plus, déclarer plusieurs scripts différés garantit qu'ils seront exécutés dans l'ordre de déclaration.

```
<script async src="./my-async-script.js"></script><script defer src="./my-deferred-script.js"></script>
```

### data:uri et <svg>

Lors de l'ajout d'icônes ou de petits fichiers image, une technique intéressante consiste à utiliser `data-uri`. Une URL `data` est généralement encodée en `base64` et offre un moyen facile d'intégrer des fichiers directement dans votre DOM. De manière similaire, vous pouvez ajouter `<svg>` en tant que balisage. Ainsi, votre image SVG sera analysée et rendue par le navigateur.

Notez que l'utilisation de `<svg>` au lieu de l'intégrer en tant qu'`<img>` ou icon-font apporte d'autres fonctionnalités qui vont au-delà du cadre de cet article.

Ajouter les fichiers directement dans votre balisage au lieu de les référencer vous évite une requête HTTP à chaque fois. Cela est utile lorsque votre fichier est si petit qu'il ne vaut pas la peine de faire un aller-retour vers le serveur. Surtout sur les réseaux mobiles, car les [handshakes](https://en.wikipedia.org/wiki/Handshaking) peuvent être assez coûteux.

### Utilisez le Multiplexage

Si votre serveur fonctionne déjà avec HTTP2, l'intégration de fichiers peut ne pas en valoir la peine. Cela est dû au fait que HTTP2 dispose d'une fonctionnalité appelée **Multiplexage**.

Cela signifie que votre navigateur peut envoyer plusieurs requêtes et recevoir plusieurs réponses "_regroupées_" dans une seule connexion TCP. Ainsi, la charge de travail associée aux recherches DNS et aux [handshakes](https://en.wikipedia.org/wiki/Handshaking) est économisée pour les fichiers provenant du même serveur.

De plus, HTTP2 vous offre également le **Server Push**. Cela signifie qu'il est possible d'envoyer des fichiers même avant que l'utilisateur ne les demande. Cela augmente significativement la performance perçue.

J'espère que ces conseils vous aideront à améliorer la performance perçue de votre application. Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements ?. Vous pouvez également me donner votre avis sur T[witter.](https://twitter.com/atilafassina)

### Lectures complémentaires

#### Sur rel=preload :

* [SmashingMagazine — Preload What is it Good for](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/)
* [Zach Letherman — Preload](https://www.zachleat.com/web/preload/)

#### Sur les polices système :

* [Bitsofcode — The New System Font Stack?](https://bitsofco.de/the-new-system-font-stack/)
* [Normalize.css — issue#665](https://github.com/necolas/normalize.css/issues/665)