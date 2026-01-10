---
title: Comment Construire Un Design De Blog Responsive Avec Bulma CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:56:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-blog-design-with-bulma-css-c2257a17c16b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnvTa_zYybCdqG0dKQLq4Q.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment Construire Un Design De Blog Responsive Avec Bulma CSS
seo_desc: 'By ZAYDEK


  Ooooooh

  How To Build A ? Responsive Blog Design With Bulma CSS

  ?‍‍ Thanks, Bulma!

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers...'
---

Par ZAYDEK

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ZQC1eAhNoto4nw_R3PZvw.gif)

#### Ooooooh

# Comment Construire Un Design De Blog Responsive Avec Bulma CSS

#### 🙏 Merci, Bulma !

Avant de commencer l'article, je souhaite partager que je développe un produit et que j'aimerais recueillir des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de le consulter ! Et maintenant, revenons à notre programme habituel.

### Bonjour internet !

Je suis ici pour vous convaincre que construire des sites web n'a pas à être difficile. De plus, en quelques minutes, nous, simples mortels, allons apprendre à créer un design de blog à la fois beau et responsive en utilisant Bulma.

#### **Bulma ?!** [Bulma](https://bulma.io/) est un framework CSS et l'œuvre de [@jgthms](https://jgthms.com/). 💡

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQHwKzcZaWbWrew33_bV4A.png)

#### J'ai également enseigné un cours complet et gratuit sur Bulma CSS sur Scrimba.com, où nous construisons ces designs 🎨. [Cliquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/gbulma) ✨

![Image](https://cdn-media-1.freecodecamp.org/images/1*MkSQUnosnWEuIIvoiUxadA.png)

#### [Scrimba.com](https://scrimba.com/g/gbulma) est une plateforme de nouvelle génération pour les développeurs front-end afin d'enregistrer et de partager leurs sites web sous forme de screencasts interactifs ! 🎥

### Bulma ? 🙇‍♂️

Bulma résout beaucoup de problèmes — vraiment beaucoup. Que vous ayez besoin d'un composant visuel ou que vous souhaitiez comprendre [comment un composant pourrait être codifié](https://github.com/jgthms/bulma/tree/master/sass), avec les meilleures pratiques et une [documentation de premier ordre](https://bulma.io/documentation/), Bulma est là pour aider ! 🤝💻

Bulma n'est même pas en version 1.0 et connaît une adoption majeure avec [150K+ téléchargements](https://github.com/jgthms/bulma/) par mois et [26K+ étoiles](https://github.com/jgthms/bulma) sur GitHub. Considérez Bulma comme un concurrent de Bootstrap, malgré le fait qu'il ne soit *que* du CSS. 😮 Regardez maman, pas de JavaScript !

### Comment fonctionne Bulma ?

Bulma utilise plusieurs techniques pour créer une interface cohérente pour les développeurs. Nous devons simplement nous soucier de décrire le design de notre site web en utilisant des classes sémantiques — et non des éléments — ou en d'autres termes, des [modèles idiomatiques](https://bulma.io/documentation/overview/start).

Ces modèles sémantiques peuvent être considérés comme des blocs de construction interconnectés que nous utilisons pour construire des sites web rapidement ! ⚠️ Ces composants sont également responsives dès leur conception, ce qui signifie que nous pouvons nous concentrer davantage sur notre contenu que sur le code.

#### Confus ? Commencez 🚀 [ici](https://medium.freecodecamp.org/free-course-level-up-with-bulma-css-d82dcb4b980a) pour apprendre d'abord les bases de Bulma.

### Et ce design 🎨 ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ZQC1eAhNoto4nw_R3PZvw.gif)
_Voulez-vous apprendre à créer ce graphique 3D en HTML et CSS ? 😲 [Faites-le moi savoir !](http://bit.do/subscribe-d82dcb4b980a) 💬_

Ce design peut être mieux compris comme étant composé de **trois parties** :

**✋ CSS Grid**  
**✍️ Composants Bulma**  
**📝 Contenu**

La spécification [**CSS Grid**](https://en.wikipedia.org/wiki/CSS_grid_layout) est la manière dont nous allons créer un design responsive personnalisé, où les **composants Bulma** nous fournissent des modèles et des sections utiles pour compartimenter notre contenu, et le **contenu** est... notre contenu, bien sûr ! 😊

### ✋ CSS Grid

Malgré le fait que [Bulma soit responsive](https://bulma.io/documentation/overview/responsiveness/) dès sa conception, nous allons plutôt opter pour CSS Grid afin de maintenir un contrôle complet sur le design responsive. Apeurés ? Ne le soyez pas ! Voici un secret ; ce n'est que 8 lignes de code lisible par l'homme ! 😉

![Image](https://cdn-media-1.freecodecamp.org/images/1*wqj11kB213Tv71KbL8GYVw.png)

Cela se passe comme suit : nous créons une classe `.grid` générale pour une utilisation courante, et pour des circonstances spécifiques, où nous voulons que notre contenu se démarque et soit plus large, nous créons une classe spéciale `.grid-xl` que nous pouvons utiliser au cas par cas :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eW7qDO0PdmJOUJvcLIgD8g.png)
_Wouah... c'est tout ? CSS Grid est magique ! 🎩✨_

Tout d'abord, nous créons un modèle de grille responsive à 5 colonnes avec les identifiants `xl` et `md`. Ensuite, nous disons à `.grid *` de couvrir la colonne `md`, par exemple la colonne de contenu, et à `.grid-xl` de couvrir les colonnes `xl`, par exemple toutes les colonnes. 🏗️

Maintenant, imaginez créer diverses classes `.grid-sm`, `.grid-lg`, etc., pour étendre différentes largeurs de caveat. Réfléchissez-y... ce n'est pas seulement concis ou cool, c'est du design responsive 100% moderne. Regardez maman, pas de media queries !

#### Confus ? Vous pouvez en apprendre davantage sur CSS Grid 🎓 [ici](https://scrimba.com/g/gR8PTE) avec Per !

### ✍️ Composants Bulma

Les [**composants Bulma**](https://bulma.io/documentation/) sont au cœur de notre design. Même si cela peut être amusant, nous n'avons pas à écrire du CSS *à partir de zéro* pour créer un design magnifique. Au lieu de cela, nous pouvons nous appuyer sur des frameworks réussis pour arbitrer les composants.

Maintenant, parce que Bulma peut être concis ou difficile à comprendre au premier abord, 💡 j'ai recréé le design en utilisant de l'art ASCII pour démontrer comment nous pourrions modéliser le design en utilisant différents composants Bulma :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WN-brZSHX68U0B8D_QeBJA.png)
_Et si nous pouvions écrire du code comme ceci... ??_

La vérité est que Bulma est plus concis, mais c'est compréhensible étant donné qu'il s'agit de HTML. Notez également que j'obfusque quelques détails pour mieux souligner comment Bulma fonctionne. Vous pouvez, cependant, [voir ce screencast interactif](https://scrimba.com/p/pV5eHk/cdkVWhq) pour voir le code complet. 😉

Jetez un second regard ; remarquez `.container (.grid)` et `.columns (.grid-xl)` ? Le premier, par exemple, se traduirait par `<div class="container grid">`. C'est *comment* nous pouvons interpoler notre grille avec les composants de Bulma !

Vous pouvez en apprendre davantage sur les composants de Bulma 📚 [ici](http://placeholder). Dans ce design de blog, nous avons utilisé [section](https://bulma.io/documentation/layout/section/), [container](https://bulma.io/documentation/layout/container/), [breadcrumb](https://bulma.io/documentation/components/breadcrumb/), [media](https://bulma.io/documentation/layout/media-object/), [image](https://bulma.io/documentation/elements/image/), [columns](https://bulma.io/documentation/columns/), et [content](https://bulma.io/documentation/elements/content/). Et, malgré le fait que je l'aie obfusqué, nous avons également utilisé des [modificateurs](https://bulma.io/documentation/modifiers/helpers/) ! 😎

#### **Considérez HTML comme du plastique, CSS comme de la peinture, et Bulma comme des LEGO. 🧱**

### 📝 Contenu

Comme promis, le dernier point est le **contenu** de notre site web, qui appartient à l'intérieur de notre composant `.content`. Rappelez-vous que j'ai dit que Bulma repose sur des classes opt-in ? Eh bien, 99% du temps, à l'intérieur de `.content`, Bulma applique du CSS à :

• Les paragraphes `p`  
• Les listes `ul`, `ol`, `dl`  
• Les titres `h1` à `h6`  
• Les citations `blockquote`  
• `em` et `strong`  
• Les tableaux `table`, `tr`, `th`, `td`  
• [etc.](https://bulma.io/documentation/elements/content/)

Et là où Bulma brille ✨ est que `.content` peut être associé à des modificateurs. Ceux-ci incluent `.is-small`, `.is-medium`, et `.is-large` pour changer la `font-size` des enfants de `.content` ! Vous pouvez en apprendre davantage sur `.content` [ici](https://bulma.io/documentation/elements/content/).

### Félicitations ! Merci d'avoir lu ! 6(^ω^)9

C'est un moment phénoménal comme aucun autre pour se lancer dans le développement front-end. Avec l'introduction des spécifications CSS comme [Flexbox](https://en.wikipedia.org/wiki/CSS_flex-box_layout) et [CSS Grid](https://en.wikipedia.org/wiki/CSS_grid_layout), et des frameworks comme [Bulma](https://bulma.io/), construire pour le web n'a jamais été aussi accessible !

#### Vous aimez cet article ?! Il y a un autre article tout comme celui-ci ! Cliquez 👆 [ici !](https://medium.freecodecamp.org/how-to-build-a-responsive-tesla-launch-page-with-bulma-css-2bf484057349)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zQKHJaZS8s5iXvBBYP3FOg.png)