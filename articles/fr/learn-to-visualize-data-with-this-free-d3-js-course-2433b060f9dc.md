---
title: Apprenez D3 dans ce cours gratuit de visualisation de données en 10 parties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-12T19:41:06.000Z'
originalURL: https://freecodecamp.org/news/learn-to-visualize-data-with-this-free-d3-js-course-2433b060f9dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rzZYWcWSMdmryHhB6Oq1ig.png
tags:
- name: D3.js
  slug: d3js
- name: Data Science
  slug: data-science
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
seo_title: Apprenez D3 dans ce cours gratuit de visualisation de données en 10 parties
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  D3.js is a JavaScript library which allows you to bring data to life using HTML,
  SVG, and CSS. Learning it will give you superpowers when it comes to extracting
  value from data, as you’ll basic...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*sDp-GORp42nSv5xEuddOcw.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gd3js_launch_article)_

D3.js est une bibliothèque JavaScript qui vous permet de donner vie aux données en utilisant HTML, SVG et CSS. L'apprendre vous donnera des superpouvoirs lorsqu'il s'agira d'extraire de la valeur des données, car vous serez essentiellement en mesure de créer n'importe quelle visualisation à laquelle vous pouvez penser.

Cependant, ce n'est pas la bibliothèque la plus facile à apprendre, donc commencer peut être un peu délicat. C'est pourquoi nous nous sommes associés avec le développeur web et instructeur [Sohaib Nehal](https://medium.com/u/4f68c487d7cf) et avons créé un [cours complet gratuit sur le sujet.](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_launch_article) Tout au long du cours, Sohaib vous donnera une introduction en douceur à cette bibliothèque puissante.

Jetons un coup d'œil à la manière dont il est structuré !

### Le contenu

Le cours se compose de 10 screencasts qui durent au total moins d'une heure. Il commence par les concepts les plus basiques, comme la sélection, la manipulation, le chargement de données, et plus encore. Cela pose les bases pour les diverses visualisations que vous apprendrez à créer tout au long du reste du cours.

#### #1 : Introduction au cours

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTASftirCvIEkkzu09ZNcw.png)

Comme d'habitude avec les cours Scrimba, il commence par un rapide aperçu du contenu du cours, ainsi qu'une introduction à D3.js et à l'instructeur.

#### #2 : Sélection et manipulation

![Image](https://cdn-media-1.freecodecamp.org/images/1*H-7cY_zluQqHuYdvNMbFGw.png)

La première chose que vous devez apprendre est comment sélectionner et manipuler des éléments du DOM avec D3.js. La bibliothèque est en fait assez puissante en termes de manipulation du DOM, donc vous pourriez théoriquement l'utiliser comme [remplacement pour jQuery.](https://blog.webkid.io/replacing-jquery-with-d3/)

#### #3 : Chargement et liaison de données

![Image](https://cdn-media-1.freecodecamp.org/images/1*5sEb4D4exhT8YZnpts-T9w.png)

Puisque vous allez créer des visualisations, il est important d'apprendre comment charger des données et aussi comment les lier au DOM. Donc, dans cette leçon, vous apprendrez cela.

#### #4 : Création d'un simple graphique à barres

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jm03LA1t_o3-GKjt84MLrA.png)

Dans la troisième leçon, vous apprendrez à construire votre toute première visualisation : un simple graphique à barres. La raison pour laquelle nous vous introduisons à la construction de choses si tôt est que c'est beaucoup plus amusant de créer des visualisations que de simplement parler de théorie. Donc, nous pensons que vous apprécierez cette leçon.

#### #5 : Création de labels

![Image](https://cdn-media-1.freecodecamp.org/images/1*sDp-GORp42nSv5xEuddOcw.png)

L'étape suivante consiste à ajouter des labels au graphique à barres, comme vous voudriez souvent le faire dans la vie réelle. Il s'agit d'une leçon courte et simple. Ici, je vous recommande de jouer avec les positions des labels, car c'est un moyen simple et amusant d'interagir avec le code.

#### #6 : Échelles

Les échelles sont un concept critique dans D3. Elles vous permettent de mapper vos données à d'autres plages pertinentes, par exemple, la quantité d'espace dont vous disposez. Donc, dans cette leçon, vous apprendrez la méthode `scaleLinear()` :

```js
var yScale = d3.scaleLinear()  
    .domain(\[0, d3.max(dataset)\])  
    .range(\[0, svgHeight\]);

```

#### #7 : Axes

![Image](https://cdn-media-1.freecodecamp.org/images/1*nag8GxIZpnUrvtfM9HaYNg.png)

Les axes sont une partie intégrante de tout graphique, et D3 vous fournit quelques méthodes simples pour les créer. Cette leçon s'appuie sur la précédente, car elle tire parti des échelles lors de la création des axes. Elle vous prépare également à comprendre le graphique en ligne super cool que vous apprendrez dans le dernier screencast du cours.

#### #8 : Création d'éléments SVG

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZdi_TA96EMc0B8I-Tt6Cg.png)

Même si vous avez déjà créé des éléments SVG précédemment dans le cours, c'est un concept si important qu'il mérite sa propre leçon. Dans celle-ci, vous apprendrez les éléments `<rect>`, `<circle>` et `<line>`.

#### #9 : Création d'un graphique en secteurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*JvNCACLTK_o7Q1D2AlMVuw.png)

Les graphiques en secteurs sont pratiques dans de nombreux cas, donc dans cette leçon, vous apprendrez à en créer un. D3 fournit une API simple pour cela, donc cela ne devrait pas être difficile pour vous à ce stade.

#### #10 : Création d'un graphique en ligne

![Image](https://cdn-media-1.freecodecamp.org/images/1*NSDd3qCL8-xYDsTnOMQ5KA.png)

Enfin, vous apprendrez à créer un graphique en ligne pour visualiser le prix du Bitcoin. Pour obtenir les données, vous utiliserez une API externe. Ce projet rassemblera également de nombreux concepts que vous avez appris tout au long du cours, donc c'est une excellente visualisation pour terminer.

Et c'est tout ! Après avoir suivi ces dix leçons, vous devriez être bien préparé pour commencer à utiliser D3.js dans votre travail ou pour des projets personnels.

Si vous atteignez ce point, nous apprécierions vraiment que vous donniez un coup de projecteur à [Sohaib](https://medium.com/u/4f68c487d7cf) sur [Twitter](https://twitter.com/Sohaib_Nehal) !

### Le format Scrimba

Avant de partir, jetons également un rapide coup d'œil à la technologie derrière le cours. Il est construit en utilisant [Scrimba](http://scrimba.com), un outil de screencast de codage interactif. Un "scrim" ressemble à une vidéo normale, cependant, il est entièrement interactif. Cela signifie que vous pouvez modifier le code à l'intérieur du screencast.

Voici un gif qui explique le concept :

![Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos changements](https://cdn-media-1.freecodecamp.org/images/1*4PWxbgV--7ZHlB-YVqavJg.gif)

Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos changements

C'est génial lorsque vous sentez que vous devez expérimenter avec le code afin de bien le comprendre, ou lorsque vous voulez simplement copier un morceau de code.

Alors, qu'attendez-vous ? [Rendez-vous sur Scrimba et suivez le cours gratuit dès aujourd'hui !](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_launch_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_launch_article) si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gd3js_launch_article)_