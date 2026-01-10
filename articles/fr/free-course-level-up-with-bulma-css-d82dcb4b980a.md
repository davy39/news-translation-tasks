---
title: 'Cours Gratuit : Passez au Niveau Supérieur ? Avec Bulma CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-11T15:24:26.000Z'
originalURL: https://freecodecamp.org/news/free-course-level-up-with-bulma-css-d82dcb4b980a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4urWdQBOzdIhWfSmcaSfhg.png
tags:
- name: Bulma
  slug: bulma
- name: CSS
  slug: css
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Cours Gratuit : Passez au Niveau Supérieur ? Avec Bulma CSS'
seo_desc: 'By ZAYDEK

  KAMEHAMEHAAAA ?

  Free Course: Level Up ? With Bulma CSS

  The best CSS framework since Bootstrap

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web...'
---

Par ZAYDEK

#### KAMEHAMEHAAAA ?

# Cours Gratuit : Passez au Niveau Supérieur ? Avec Bulma CSS

#### Le meilleur framework CSS depuis Bootstrap

Avant de commencer l'article, je souhaite partager que je développe un produit et j'aimerais recueillir des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Veuillez y jeter un coup d'œil — merci ! Et maintenant, revenons à notre programmation habituelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4urWdQBOzdIhWfSmcaSfhg.png)
_L'originale Bulma. [→](http://dragonball.wikia.com/wiki/Bulma" rel="noopener" target="_blank" title=")_

### Rencontrez Bulma CSS ! Cours gratuit ? i[ci](https://scrimba.com/g/gbulma)

En plus d'être le deuxième personnage le plus ancien de Dragon Ball Z, [Bulma](https://bulma.io/) est un framework CSS moderne basé sur Flexbox créé par Jeremy Thomas [@jgthms](https://jgthms.com/). Et Bulma gagne rapidement en adoption avec [150K+ téléchargements](https://github.com/jgthms/bulma/) par mois et [26K+ étoiles](https://github.com/jgthms/bulma) sur GitHub. OK… dites-moi en plus. ?

Avec Bulma, nous pouvons créer des sites web magnifiques et réactifs avec facilité. Jeremy a conçu Bulma comme un ensemble réutilisable de [Sass](http://placeholder) pour démarrer de nouveaux projets. Vous ne connaissez pas _Sass_ ? Sass *compile* en CSS. Et une fois que [Flexbox](https://en.wikipedia.org/wiki/CSS_flex-box_layout) a été standardisé, Jeremy l'a utilisé pour alimenter ce que nous connaissons maintenant sous le nom de Bulma.

Dans cet article, je détaille *comment* Bulma fonctionne et *ce* que nous pouvons construire avec.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YUa4liSlBUoldpJGt0ovtg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*4NZIFhHJqCZPErX-b1hxJQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ejl2VJMpj-2sKbSMN4cgyw.png)
_Voulez-vous apprendre à *construire* ce graphique 3D ? [Faites-le-moi savoir !](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")_

### J'ai également enseigné Bulma CSS sur Scrimba, où nous construisons ces sites web. C'est gratuit — [cliquez ici pour vous inscrire](https://scrimba.com/g/gbulma) ! ?

#### [Scrimba.com](https://scrimba.com/g/gbulma) est une plateforme pour le développement front-end, où les sites web sont enregistrés en tant qu'événements — pas des vidéos — et peuvent être modifiés. ?

### Comment fonctionne Bulma ?

Bulma est [4,5K lignes](https://github.com/jgthms/bulma/tree/master/sass) de Sass et [9,5K lignes](https://github.com/jgthms/bulma/blob/master/css/bulma.css) lorsqu'il est compilé en CSS. Mais que fait tout ce code ? Bulma traite 90 % des motifs courants des sites web, comme les [colonnes](https://bulma.io/documentation/columns/), les [formulaires](https://bulma.io/documentation/form/), les [composants](https://bulma.io/documentation/components/), les [modificateurs](https://bulma.io/documentation/modifiers/), les [dispositions](https://bulma.io/documentation/layout/) et les [éléments](https://bulma.io/documentation/elements/). Le code est *également* réactif et peut être davantage thématisé et personnalisé.

Bulma ne résout pas tous les problèmes, mais peut être *beaucoup* plus productif que de coder manuellement en Sass ou CSS. Et parce que Bulma compile en CSS, il est adaptable aux frameworks et bibliothèques JavaScript comme Angular, React et Vue. En bref, Bulma fonctionne *comme* Bootstrap mais sans [JavaScript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript).

Contrairement à Bootstrap, Bulma repose sur CSS — pas JavaScript. Mais comme Bootstrap, il est livré avec sa propre [réinitialisation CSS](https://github.com/jgthms/bulma/blob/master/sass/base/minireset.sass). Maintenant, examinons comment Bulma fonctionne à partir des premiers principes. Je suppose que vous êtes [familier avec HTML/CSS](https://medium.freecodecamp.org/how-to-design-and-develop-a-beautiful-blog-from-scratch-a0cd1af46845) mais pas plus, donc voici à quoi ressemble le CSS classique :

**Note :** Bien que ceci ne soit pas Bulma, cela démontre *comment* Bulma fonctionne.

```
<!DOCTYPE html><html>  <head>    …    <style>
```

```
p {  line-height: 2;}
```

```
    </style>  </head>  <body>    <p>      Il y a bien longtemps, dans une galaxie lointaine, très lointaine…    </p>  </body></html>
```

Ici, nous avons défini un `p` dans notre HTML, et dans notre CSS, nous avons défini tous les `p` comme ayant des lignes doubles, par exemple `line-height: 2`. Attendez — que se passe-t-il si nous ne voulons pas que tous les `p` soient doubles ? Ou si nous voulons que certains, mais pas *tous*, soient doubles ? Alors nous pouvons opter pour CSS en utilisant des classes :

```
<!DOCTYPE html><html>  <head>    …    <style>
```

```
.double-spaced {  line-height: 2;}
```

```
    </style>  </head>  <body>    <p class="double-spaced">      Il y a bien longtemps, dans une galaxie lointaine, très lointaine…    </p>  </body></html>
```

Nous avons donc défini une classe nommée `double-spaced` que nous choisissons d'utiliser plutôt que de faire hériter les éléments de CSS, comme dans le premier exemple. Et cela est plus sensé car cela rend plus difficile la surcharge de notre CSS plus tard. Cependant, nous pouvons aller encore plus loin pour rendre cela plus difficile, et nous pouvons rendre notre classe conditionnelle :

```
<!DOCTYPE html><html>  <head>    …    <style>
```

```
p.double-spaced {  line-height: 2;}
```

```
    </style>  </head>  <body>    <p class="double-spaced">      Il y a bien longtemps, dans une galaxie lointaine, très lointaine…    </p>  </body></html>
```

Et maintenant, `double-spaced` nécessite la présence d'un élément `p`. C'est du **CSS conditionnel**, et nous pouvons aller encore plus loin ! Nous pouvons utiliser uniquement des classes, par exemple `class-1.class-2` pour créer des **classes conditionnelles**. C'est l'une des techniques que Bulma utilise pour créer des contrats HTML/CSS.

> _*AHEM* Écrivons-nous simplement du CSS dans notre HTML maintenant… ?_

> (◔ ‸ ◔)

La différence ici est que Bulma met l'accent sur les motifs courants en utilisant la sémantique — pas des règles CSS un-à-un. Cela signifie que nous utilisons Bulma pour décrire des relations — pas des règles — et donc c'est plus puissant. De plus, la [nouvelle documentation](https://bulma.io/documentation/) de Bulma est incroyable et élimine beaucoup de conjectures en CSS.

En plus des classes conditionnelles, Bulma définit de nombreux contrats HTML/CSS, ce qui conduit à un CSS plus flexible et à un code plus idiomatique. Et c'est génial pour partager du code entre les équipes. Ces contrats détaillent la relation des classes les unes avec les autres. Voici un exemple simple d'un contrat HTML/CSS :

```
<section class="section">  <div class="container">    ...  </div></section>
```

Avec suffisamment de classes bien conçues et de contrats, nous pouvons créer toutes sortes de sites web magnifiques et réactifs soutenus par Bulma. [Consultez l'expo !](https://bulma.io/expo/) ✨ Maintenant, avant de nous emballer, commençons par un « Hello World » puis la diapositive suivante — [ce n'est pas une diapositive, c'est un site web](https://www.youtube.com/watch?v=EVekNsgUqn4).

![Image](https://cdn-media-1.freecodecamp.org/images/1*LN_Rupiz74q5b-yAfxgRQw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2hcqN-nehso7LlXNRNl7hQ.png)
_Cliquez sur l'un ou l'autre pour ouvrir dans le bac à sable interactif de Scrimba. ?_

Et dans un avenir proche, je publierai deux ✉️ autres articles détaillant comment nous pouvons construire un [beau blog](https://twitter.com/username_ZAYDEK/status/994209963558944769) et une [page de lancement Tesla](https://twitter.com/username_ZAYDEK/status/994209997373423617) avec Bulma ! Pour les mises à jour, suivez-moi sur [Medium](https://medium.com/@ZAYDEK) ✍️ et [Twitter](https://twitter.com/username_ZAYDEK). ? Je les enseigne cependant dans le cours interactif gratuit de Scrimba. C[liquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/gbulma) ?

Et sans plus tarder…

### « Hello World »

![Image](https://cdn-media-1.freecodecamp.org/images/1*LN_Rupiz74q5b-yAfxgRQw.png)
_Un *peu* zoommé. ? Cliquez pour ouvrir dans le bac à sable interactif de Scrimba. ?_

Maintenant que nous comprenons comment Bulma fonctionne, apprenons comment faire un « Hello World » :

```
<!DOCTYPE html><html>  <head>    <meta charset="utf-8">    <meta        name="viewport" content="width=device-width,        initial-scale=1">    <title>Bonjour Bulma !</title>    <link rel="stylesheet" href="https://…/bulma.min.css">    <script defer src="https://…/all.js"></script>  </head>  <body>    <section class="section">      <div class="container">        <h1 class="title">          Hello World        </h1>        <p class="subtitle">          Mon premier site web avec <strong>Bulma</strong> !        </p>      </div>    </section>  </body></html>
```

Revenez — ne soyez pas effrayé ! ? Tous les sites web Bulma commencent à partir de c[e modèle.](https://bulma.io/documentation/overview/start/) Concentrons-nous d'abord sur l'élément h`ead` ; le l`ink` pointant vers b`ulma.min.css` charge Bulma, et le s`cript` pointant vers a`ll.js` charge les i[cônes Font Awesome.](https://fontawesome.com/) N**ote :** Bulma prend en charge toutes les bibliothèques d'icônes.

Et Bulma préfère utiliser les [éléments HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5), par exemple `section` plutôt que `div` lorsque c'est approprié. C'est plus lisible et idiomatique. Attendez — que se passe-t-il si le navigateur du client est obsolète et ne reconnaît donc pas les éléments HTML5 ? Bulma s'en occupe aussi !

```
/* bulma.css#L312 */
```

```
article,aside,figure,footer,header,hgroup,section {  display: block;}
```

Merci Bulma ! ? Cela garantit que les éléments HTML5 sont rendus comme des éléments de bloc malgré le navigateur du client. OK — passons en revue le b`ody` :

```
<section class="section">  <div class="container">    <h1 class="title">      Hello World    </h1>    <p class="subtitle">      Mon premier site web avec <strong>Bulma</strong> !    </p>  </div></section>
```

Quand j'ai appris Bulma pour la première fois, j'ai (╯°□°）╯︵ ┻━┻ parce que c'est si concis. Mais une fois que je me suis calmé, j'ai commencé à reconnaître un motif émergent : la forme de l'arbre de notre site web. Et c'est beaucoup plus simple que je ne le pensais :

```
   .section       |  .container     /   \.title  .subtitle   /       \ ...       ...
```

_Ahhhh._ Où `.section` définit le début d'un nouveau contenu, `.container` est une classe d'enveloppe pour le contenu (comme du texte) et est utilisée pour le design réactif. Et `.title` et `.subtitle` sont pour l'esthétique. Ayant fait cela, Bulma s'est occupé de dizaines de détails comme les meilleures pratiques _et_ le design réactif. ??

### Au-delà de « Hello World » ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*2hcqN-nehso7LlXNRNl7hQ.png)
_Cliquez pour ouvrir dans le bac à sable interactif de Scrimba. ?_

Pensez à Bulma comme à des pièces de Lego avec des modificateurs, comme des variantes de couleur. Et ainsi, composer ce site web nécessite seulement quelques pièces et modificateurs, tels que `.columns`, `.media`, `.icon` — c'est tout. Bien que le code *soit* plus complexe, c'est parce que c'est du code. La composition du site web est ce qui est simple :

```
         .column            |         .media          /   \.media-left  .media-content        /       \    .icon      .content      /           \    ...           ...
```

Ce qui précède est à quoi ressemble un colonne Bulma sous forme d'arbre. Et en code :

```
…<div class="column">  <article class="media notification is-info">    <figure class="media-left">      <span class="icon is-medium">        <i class="fab fa-2x fa-css3-alt"></i>      </span>    </figure>    <div class="media-content">      <div class="content">        <h1 class="title is-size-4">          Bulma        </h1>        <p class="is-size-5">          <strong>Bulma</strong> est un framework CSS moderne...        </p>      </div>    </div>  </article></div>…
```

**Note** : Les modificateurs tels que `.notification`, `.is-info`, `.is-medium`, etc., aident à personnaliser notre site web. Certains modificateurs sont conditionnels et nécessitent une autre classe, et certains sont à usage général. Vous pouvez en apprendre plus sur eux [ici](https://bulma.io/documentation/modifiers/). Et pour un bac à sable interactif du site web complet, [cliquez ici](https://scrimba.com/c/cyr3dT3). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*AeG2UlfaWGBM7VVT0BZVmQ.png)
_Cliquez pour ouvrir dans le bac à sable interactif de Scrimba. ?_

> **Bulma est fascinant ! Nous pouvons concevoir des sites web magnifiques et réactifs en utilisant la sémantique — sans écrire de CSS.**

### Réflexions finales ?

Ce que j'aime le plus chez Bulma, c'est que c'est un moyen de comprendre comment son créateur pense sans avoir à lui demander. Comment faire X ? [Cherchez-le !](https://github.com/jgthms/bulma/) **C'est une idée puissante — que nous pouvons regarder dans l'esprit d'un guru CSS pour des réponses, plutôt que de bricoler des solutions non idéales nous-mêmes.**

**Merci d'avoir lu !** J'étais réticent à apprendre Bulma au début, mais j'ai fini par apprécier à quel point il peut être puissant et idiomatique. J'ai donc décidé que Bulma ne devait pas passer inaperçu, car concevoir et développer des sites web peut souvent être *beaucoup* plus difficile que prévu. Encore une fois — **merci d'avoir lu !** _???_

### _Vous aimez cela ? Il y en a deux autres — cliquez [ici](https://medium.freecodecamp.org/how-to-build-a-responsive-blog-design-with-bulma-css-c2257a17c16b) et [ici](https://medium.freecodecamp.org/how-to-build-a-responsive-tesla-launch-page-with-bulma-css-2bf484057349) !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*jYb2etzcRa1YfBSm_JYjGQ.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*lzMU40hG75TH-k1oNlSfdQ.gif)
_Voulez-vous apprendre à *construire* ce graphique 3D ? [Faites-le-moi savoir !](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")_

#### _Envisagez de soutenir [jgthms](https://jgthms.com/) sur [Patreon](https://www.patreon.com/jgthms) ! Il est déterminé à faire de Bulma son gagne-pain et son engagement à temps plein. ??_