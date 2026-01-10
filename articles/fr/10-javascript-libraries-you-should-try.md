---
title: 10 bibliothèques JavaScript géniales que vous devriez essayer
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2021-01-03T17:32:00.000Z'
originalURL: https://freecodecamp.org/news/10-javascript-libraries-you-should-try
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9999740569d1a4ca20a6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: Productivity
  slug: productivity
seo_title: 10 bibliothèques JavaScript géniales que vous devriez essayer
seo_desc: 'JavaScript is one of the most popular languages on the web. Even though
  it was initially developed just for web pages, it has seen exponential growth in
  the past two decades.

  Now, JavaScript is capable of doing almost anything and works on several pl...'
---

JavaScript est l'un des langages les plus populaires sur le web. Bien qu'il ait été initialement développé uniquement pour les pages web, il a connu une croissance exponentielle au cours des deux dernières décennies.

Aujourd'hui, JavaScript est capable de faire presque n'importe quoi et fonctionne sur plusieurs plateformes et appareils, y compris l'IoT. Et avec le récent lancement de SpaceX Dragon, JavaScript est même dans l'espace.

L'une des raisons de sa popularité est la disponibilité d'un grand nombre de frameworks et de bibliothèques. Elles rendent le développement beaucoup plus facile par rapport au développement traditionnel en Vanilla JS.

Il existe des bibliothèques pour presque tout, et de nouvelles apparaissent presque tous les jours. Mais avec tant de bibliothèques parmi lesquelles choisir, il devient difficile de suivre chacune d'elles et de savoir comment elle peut être adaptée spécifiquement à vos besoins.

Dans cet article, nous allons discuter de 10 des bibliothèques JS les plus populaires que vous pouvez utiliser pour construire votre prochain projet.

# [Leaflet](https://leafletjs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-17.png align="left")

*Leaflet*

Je pense que Leaflet est la meilleure bibliothèque open source pour ajouter des cartes interactives adaptées aux mobiles à votre application.

Sa petite taille (39 ko) en fait une excellente alternative à considérer par rapport à d'autres bibliothèques de cartes. Avec une efficacité multiplateforme et une API bien documentée, elle a tout ce dont vous avez besoin pour vous faire tomber amoureux.

Voici un exemple de code qui crée une carte Leaflet :

```javascript
var map = new L.Map("map", {
    center: new L.LatLng(40.7401, -73.9891),
    zoom: 12,
    layers: new L.TileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png")
});
```

Dans Leaflet, nous devons fournir une couche de tuiles puisqu'il n'y en a pas par défaut. Mais cela signifie également que vous pouvez choisir parmi une large gamme de couches, à la fois gratuites et premium. Vous pouvez explorer diverses couches de tuiles gratuites [ici](https://leaflet-extras.github.io/leaflet-providers/preview/).

Lisez la [Documentation](https://leafletjs.com/reference-1.6.0.html) ou suivez les [Tutoriels](https://leafletjs.com/examples.html) pour en savoir plus.

# [fullPage.js](https://alvarotrigo.com/fullPage/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-1--1.gif align="left")

Cette bibliothèque open-source vous aide à créer des sites web à défilement plein écran comme vous pouvez le voir dans le GIF ci-dessus. Elle est facile à utiliser et offre de nombreuses options de personnalisation, il n'est donc pas surprenant qu'elle soit utilisée par des milliers de développeurs et qu'elle ait plus de 30k étoiles sur GitHub.

Voici une démonstration Codepen avec laquelle vous pouvez jouer :

%[https://codepen.io/lelouchb/pen/WNrLvLG]

Vous pouvez même l'utiliser avec des frameworks populaires tels que :

* [react-fullpage](https://alvarotrigo.com/react-fullpage/)

* [vue-fullpage](https://alvarotrigo.com/vue-fullpage/)

* [angular-fullpage](https://alvarotrigo.com/angular-fullpage/)

Je suis tombé sur cette bibliothèque il y a environ un an et depuis lors, elle est devenue l'une de mes préférées. C'est l'une des rares bibliothèques que vous pouvez utiliser dans presque tous les projets. Si vous n'avez pas encore commencé à l'utiliser, essayez-la, vous ne serez pas déçu.

# [anime.js](https://animejs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/anime.gif align="left")

*anime.js*

L'une des meilleures bibliothèques d'animation, Anime.js est flexible et simple à utiliser. C'est l'outil parfait pour vous aider à ajouter des animations vraiment cool à votre projet.

Anime.js fonctionne bien avec les propriétés CSS, SVG, les attributs DOM et les objets JavaScript, et peut être facilement intégré dans vos applications.

En tant que développeur, il est important d'avoir un bon portfolio. La première impression que les gens ont de votre portfolio aide à décider s'ils vont vous embaucher ou non. Et quel meilleur outil que cette bibliothèque pour donner vie à votre portfolio. Non seulement elle améliorera votre site web, mais elle aidera également à montrer des compétences réelles.

Consultez ce Codepen pour en savoir plus :

%[https://codepen.io/lelouchb/pen/XWXoboE]

Vous pouvez également jeter un coup d'œil à tous les autres projets cool sur [Codepen](https://codepen.io/collection/XLebem) ou [Lire la Documentation ici](https://animejs.com/documentation/).

# [Screenfull.js](https://github.com/sindresorhus/screenfull.js)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-29.png align="left")

*screenfull.js*

Je suis tombé sur cette bibliothèque en cherchant un moyen d'implémenter une fonctionnalité de plein écran dans mon projet.

Si vous souhaitez également avoir une fonctionnalité de plein écran, je vous recommande d'utiliser cette bibliothèque plutôt que l'[API Fullscreen](https://developer.mozilla.org/en/DOM/Using_full-screen_mode) en raison de son efficacité multi-navigateurs (bien qu'elle soit construite par-dessus celle-ci).

Elle est si petite que vous ne la remarquerez même pas – environ 0,7 ko compressé.

Essayez la [Démonstration](https://sindresorhus.com/screenfull.js) ou lisez la [Documentation](https://github.com/sindresorhus/screenfull.js) pour en savoir plus.

# [Moment.js](https://momentjs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-18.png align="left")

*Moment.js*

Travailler avec les dates et les heures peut être un énorme casse-tête, surtout avec les appels API, les différents fuseaux horaires, les langues locales, etc. Moment.js peut vous aider à résoudre tous ces problèmes, qu'il s'agisse de manipuler, valider, analyser ou formater des dates ou des heures.

Il existe de nombreuses méthodes cool qui sont vraiment utiles pour vos projets. Par exemple, j'ai utilisé la méthode `.fromNow()` dans l'un de mes projets de blog pour montrer l'heure à laquelle l'article a été publié.

```javascript
const moment = require('moment');

relativeTimeOfPost = moment([2019, 07, 13]).fromNow();
// il y a un an
```

Bien que je ne l'utilise pas très souvent, je suis un fan de son support pour l'internationalisation. Par exemple, nous pouvons personnaliser le résultat ci-dessus en utilisant la méthode `.locale()`.

```javascript
// Français
moment.locale('fr');
relativeTimeOfPostInFrench = moment([2019, 07, 13]).fromNow();
// il y a un an

// Espagnol
moment.locale('es');
relativeTimeOfPostInSpanish = moment([2019, 07, 13]).fromNow();
// hace un año
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif.gif align="left")

*Page d'accueil de Moment.js*

Lisez la [Documentation ici](https://momentjs.com/).

**Mise à jour septembre 2020 :** Moment.js est passé en mode maintenance. Lisez plus à ce sujet [ici](https://momentjs.com/docs/#/-project-status/). Vous pourriez vouloir explorer des alternatives telles que [Day.js](https://day.js.org/) ou [date-fns](https://date-fns.org/).

# [Hammer.js](http://hammerjs.github.io/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-2.gif align="left")

Hammer.js est une bibliothèque JavaScript légère qui vous permet d'ajouter des gestes multi-touch à vos applications web.

Je recommande cette bibliothèque pour ajouter un peu de fun à vos composants. Voici un exemple avec lequel jouer. Exécutez simplement le pen et tapez ou cliquez sur la div grise.

%[https://codepen.io/lelouchb/pen/abdPOPj]

Elle peut reconnaître les gestes faits par le toucher, la souris et les pointerEvents. Pour les utilisateurs de jQuery, je recommande d'utiliser le [plugin jQuery](http://hammerjs.github.io/jquery-plugin/).

```javascript
$(element).hammer(options).bind("pan", myPanHandler);
```

Lisez la [Documentation ici](http://hammerjs.github.io/getting-started/).

# [Masonry](https://masonry.desandro.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-20.png align="left")

*Masonry*

Masonry est une bibliothèque de mise en page de grille JavaScript. Elle est super géniale et je l'utilise pour beaucoup de mes projets. Elle peut prendre vos éléments de grille simples et les placer en fonction de l'espace vertical disponible, un peu comme la façon dont les entrepreneurs ajustent les pierres ou les blocs dans un mur.

Vous pouvez utiliser cette bibliothèque pour montrer vos projets sous un jour différent. Utilisez-la avec des cartes, des images, des modales, etc.

Voici un exemple simple pour vous montrer la magie en action. Eh bien, pas exactement de la magie, mais comment la mise en page change lorsque vous **zoomez** sur la page web.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-crop.gif align="left")

Et voici le code pour ce qui précède :

```javascript
var elem = document.querySelector('.grid');
var msnry = new Masonry( elem, {
  itemSelector: '.grid-item',
  columnWidth: 400
});

var msnry = new Masonry( '.grid');
```

Voici une démonstration cool sur Codepen :

%[https://codepen.io/lelouchb/pen/qBbLdLQ]

Consultez ces projets

* [https://halcyon-theme.tumblr.com/](https://halcyon-theme.tumblr.com/)

* [https://tympanus.net/Development/GridLoadingEffects/index.html](https://tympanus.net/Development/GridLoadingEffects/index.html)

* [https://www.erikjo.com/work](https://www.erikjo.com/work)

# [D3.js](https://d3js.org/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-30.png align="left")

Si vous êtes un développeur obsédé par les données, cette bibliothèque est faite pour vous. Je n'ai pas encore trouvé de bibliothèque qui manipule les données aussi efficacement et aussi magnifiquement que D3. Avec plus de 92k étoiles sur GitHub, D3 est la bibliothèque de visualisation de données préférée de nombreux développeurs.

J'ai récemment utilisé D3 pour visualiser les données COVID-19 avec React et le [Dépôt de données CSSE de Johns Hopkins sur GitHub](https://github.com/CSSEGISandData/COVID-19). C'était un projet vraiment intéressant, et si vous pensez faire quelque chose de similaire, je vous suggère d'essayer D3.js.

Lisez plus à ce sujet [ici](https://github.com/d3/d3/wiki).

# [slick](https://kenwheeler.github.io/slick/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-23.png align="left")

*slick*

Slick est entièrement réactif, compatible avec le balayage, en boucle infinie, et plus encore. Comme mentionné sur la page d'accueil, c'est vraiment le dernier carrousel dont vous aurez jamais besoin.

J'utilise cette bibliothèque depuis un certain temps, et elle m'a fait gagner beaucoup de temps. Avec seulement quelques lignes de code, vous pouvez ajouter tant de fonctionnalités à votre carrousel.

```js
$('.autoplay').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-2-.gif align="left")

*Lecture automatique*

Consultez les démonstrations [ici](https://kenwheeler.github.io/slick/).

# [Popper.js](https://popper.js.org/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-25.png align="left")

*Popper.js*

Popper.js est une bibliothèque JavaScript légère (~3 ko) sans dépendances qui fournit un moteur de positionnement fiable et extensible que vous pouvez utiliser pour vous assurer que tous vos éléments popper sont positionnés au bon endroit.

Il peut ne pas sembler important de passer du temps à configurer les éléments popper, mais ce sont ces petites choses qui vous distinguent en tant que développeur. Et avec une taille si petite, elle ne prend pas beaucoup de place.

Lisez la [Documentation ici](https://popper.js.org/docs/v2/).

# Conclusion

En tant que développeur, avoir et utiliser les bonnes bibliothèques JavaScript est important. Cela vous rendra plus productif et rendra le développement beaucoup plus facile et rapide. En fin de compte, c'est à vous de choisir quelle bibliothèque préférer en fonction de vos besoins.

Ce sont 10 bibliothèques JavaScript que vous pouvez essayer et commencer à utiliser dans vos projets dès aujourd'hui. Quelles autres bibliothèques JavaScript cool utilisez-vous ? Souhaitez-vous un autre article comme celui-ci ? [Tweetez](https://twitter.com/noharashutosh) et faites-le moi savoir.