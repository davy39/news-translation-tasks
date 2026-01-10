---
title: Apprendre le CSS – Guide d'étude sur la conception Web réactive
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-11-07T18:24:20.000Z'
originalURL: https://freecodecamp.org/news/learn-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/kobu-agency-ipARHaxETRk-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: freeCodeCamp.org
  slug: freecodecamp
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre le CSS – Guide d'étude sur la conception Web réactive
seo_desc: 'Cascading Style Sheets (CSS) represents the design for a web page. But
  when you are learning this information for the first time, it can be hard to keep
  track of all of the different CSS properties.

  In this article, I have created a study guide for t...'
---

Les feuilles de style en cascade (CSS) représentent le design d'une page web. Mais lorsque vous apprenez ces informations pour la première fois, il peut être difficile de suivre toutes les différentes propriétés CSS.

Dans cet article, j'ai créé un guide d'étude pour l'ensemble du programme de certification de freeCodeCamp [Apprendre les bases du CSS en construisant un menu de café](https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-basic-css-by-building-a-cafe-menu). Ce guide d'étude est rempli d'informations supplémentaires, d'articles et de vidéos pour vous aider à mieux comprendre les concepts.

N'hésitez pas à vous référer à ce guide tout au long de la certification. La première partie du projet passe en revue les éléments HTML puis aborde le CSS.

Voici la liste complète des sujets abordés. Cliquez sur l'un des liens ci-dessous pour en savoir plus sur le sujet.

## Table des matières

* [DOCTYPE et éléments HTML](#heading-doctype-et-elements-html) - Étape 1
* [Éléments Head et Title](#heading-head-et-title-elements) - Étape 2
* [Attribut Meta charset](#heading-meta-charset-attribute) - Étapes 3,17
* [Élement Body](#heading-body-element) - Étape 4
* [Éléments de titre](#heading-heading-elements) - Étapes 6,9,10, 47
* [Élement Paragraph](#heading-paragraph-element) - Étapes 7, 30, 31, 49, 65
* [Élement Header](#heading-header-element) - Étape 7
* [Élement Main](#heading-main-element) - Étape 5
* [Éléments Section](#heading-section-elements) - Étapes 8, 9, 46
* [Élement Style](#heading-style-element) - Étape 10
* [Propriété text-align en CSS](#heading-text-align-property-in-css) - Étapes 11, 12, 33, 35
* [Regroupement des sélecteurs CSS](#heading-grouping-css-selectors) - Étapes 13, 51
* [Liaison de feuilles de style externes](#heading-linking-external-stylesheets) - Étape 16
* [Balise meta Viewport](#heading-viewport-meta-tag) - Étape 18
* [Propriété background-color](#heading-background-color-property) - Étapes 18, 19, 23, 68
* [Élement Div](#heading-div-element) - Étape 20
* [Propriété CSS `width`](#heading-css-width-property) - Étapes 21, 24, 38, 39, 41, 45
* [Commentaires CSS](#heading-css-comments) - Étapes 22, 77
* [Propriété Margin](#heading-margin-property) - Étapes 25, 73, 75, 84, 85, 86, 91
* [Sélecteurs de classe](#heading-class-selectors) - Étapes 26, 27, 32, 34, 36, 42, 44, 50, 61, 76, 87
* [Propriété `background-image`](#heading-background-image-property) - Étape 28
* [Élement Article](#heading-article-element) - Étapes 29, 31, 48, 52
* [Valeurs block, inline et inline-block](#heading-block-inline-et-inline-block-values) - Étapes 37, 89
* [Padding](#heading-padding) - Étapes 53 - 55, 72
* [Propriété `max-width`](#heading-max-width-property) - Étape 56
* [font-family](#heading-font-family-property) - Étape 57 - 59
* [Propriété `font-style`](#heading-font-style-property) - Étape 60
* [Propriété `font-size`](#heading-font-size-property) - Étapes 62, 74, 78
* [Éléments Footer](#heading-footer-elements) - Étape 63
* [Éléments Anchor](#heading-anchor-elements) - Étape 64
* [Élement hr](#heading-hr-element) - Étapes 66, 71
* [Propriété Height](#heading-height-property) - Étapes 67, 70
* [Propriété `border-color`](#heading-border-color-property) - Étape 69
* [Propriété Color](#heading-color-property) - Étapes 79, 83
* [Pseudo-classes](#heading-pseudo-classes) - Étapes 80, 81, 82
* [Éléments Image](#heading-image-elements) - Étapes 88, 90
* [Ressources supplémentaires pour HTML et CSS](#heading-additional-resources-for-html-and-css)

## DOCTYPE et éléments HTML

La première ligne de votre code HTML doit être la déclaration `DOCTYPE`. Un `DOCTYPE` indique au navigateur quelle version de HTML la page est écrite.

Voici la déclaration `DOCTYPE` pour HTML 5 :

```html
<!DOCTYPE html>
```

Si vous oubliez d'inclure cette ligne de code dans votre fichier, certaines des balises HTML 5 comme `<article>`, `<footer>`, et `<header>` peuvent ne pas être supportées par le navigateur.

L'élément `html` est l'élément racine où tous les autres éléments vont à l'intérieur.

```html
<!DOCTYPE html>
<html lang="en">
  <!--Tous les autres éléments vont ici-->
</html>
```

L'attribut `lang` à l'intérieur de la balise `<html>` d'ouverture définit la langue de la page. Il est également bon de l'inclure pour des raisons d'accessibilité, car les lecteurs d'écran sauront comment prononcer correctement le texte.

```html
<html lang="en">
```

## Éléments Head et Title

Les balises `<head>` contiennent des informations qui sont traitées par les machines. À l'intérieur des balises `<head>`, vous imbriquerez des métadonnées qui sont des données décrivant le document à la machine.

```html
<head>
  <!--les métadonnées importantes vont ici-->
  <!--l'élément title va également ici-->
</head>
```

La balise `<title>` est le titre de la page web. Ce texte est affiché dans la barre de titre du navigateur.

```html
    <title>HTML 5 Boilerplate</title>

```

![Screen-Shot-2021-07-30-at-4.15.25-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-30-at-4.15.25-AM.png)

Voici un exemple de ce à quoi ressemble un `head` sur une vraie page web. Aucune de ces informations n'est affichée sur la page web elle-même.

```html
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
```

Pour une description détaillée de chaque balise meta listée, vous pouvez lire cet [article sur un HTML5 Boilerplate](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/).

## Attribut Meta charset

UTF-8 est l'encodage de caractères standard que vous devez utiliser dans vos pages web. Cela sera généralement la première balise `<meta>` affichée dans l'élément `<head>`.

```html
 <meta charset="UTF-8">
```

Selon le [World Wide Web Consortium](https://www.w3.org/International/questions/qa-choosing-encodings),

> Un encodage basé sur Unicode tel que UTF-8 peut supporter de nombreuses langues et peut accommoder des pages et des formulaires dans n'importe quel mélange de ces langues. Son utilisation élimine également le besoin de logique côté serveur pour déterminer individuellement l'encodage des caractères pour chaque page servie ou chaque soumission de formulaire entrant.

## Élément Body

L'élément body contient tout le contenu de la page web. Cela inclut les titres, les paragraphes, les images, les liens, et plus encore.

```html
<html>
  <head>
    <title>Apprenons à propos de l'élément body</title>
  </head>
  <body>
    <!--le contenu de la page web va ici-->
  </body>
</html>

```

## Éléments de titre

Les éléments de titre HTML représentent le titre principal et les sous-titres d'une page web.

L'élément `h1` représente le titre le plus important et ne doit être utilisé qu'une seule fois par page web.

```html
<h1>Je représente le titre principal d'une page web</h1>
```

L'élément `h2` représente le deuxième titre le plus important sur la page.

```html
<h2>Je suis le deuxième élément de titre le plus important</h2>
```

Il y a un total de six éléments de titre de section :

```html
<h1>Je suis l'élément de titre le plus important</h1>
<h2>Je suis le deuxième élément de titre le plus important</h2>
<h3>Je suis le troisième élément de titre le plus important</h3>
<h4>Je suis le quatrième élément de titre le plus important</h4>
<h5>Je suis le cinquième élément de titre le plus important</h5>
<h6>Je suis l'élément de titre le moins important</h6>
```

Voici à quoi cela ressemble rendu sur la page.

![Screen-Shot-2022-06-18-at-9.19.27-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.19.27-PM.png)

Pour en savoir plus sur les éléments de titre, vous pouvez lire cette [explication détaillée des éléments de titre DevDocs](https://devdocs.io/html/element/heading_elements).

## Élément Paragraph

Les éléments de paragraphe représentent les paragraphes sur une page web.

```html
<p>J'adore apprendre avec freeCodeCamp. Ils ont des milliers d'articles et de vidéos gratuits pour m'aider à apprendre à coder.</p>
```

Voici à quoi cela ressemble rendu sur la page :

![Screen-Shot-2022-06-18-at-9.55.21-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.55.21-PM.png)

Pour en savoir plus sur les éléments de paragraphe, vous pouvez lire cette [explication détaillée de l'élément `p` DevDocs](https://devdocs.io/html/element/p).

## Élément Header

L'élément `header` contient le contenu introductif de la page web. Cela peut inclure des éléments comme un `nav`, `h1` ou un logo de site web.

```html
<header>
  <img src="link-for-logo" alt="description pour le faux logo va ici">
  <nav>
    <ul>
      <li><a href="/">Accueil</a></li>
      <li><a href="#bio">Bio</a></li>
      <li><a href="#projects">Projets</a></li>
    </ul>
  </nav>
</header>
```

## Élément Main

L'élément `main` est utilisé pour regrouper tout le contenu principal de la page web.

```html
<h1>Ce que freeCodeCamp a à offrir</h1>
<main>
  <p>Le programme principal de freeCodeCamp enseigne le développement full stack JavaScript et Python. Il y a des centaines de leçons à parcourir pour vous préparer à un emploi de développeur de niveau débutant.</p>

  <p>freeCodeCamp a des milliers d'articles gratuits sur leur publication d'actualités. Ils ont également des centaines de vidéos sur leur chaîne YouTube.</p>
</main>
```

Voici à quoi ressemble le code rendu sur la page.

![Screen-Shot-2022-06-18-at-10.34.18-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-10.34.18-PM.png)

Pour en savoir plus sur l'élément `main`, vous pouvez lire cette [explication détaillée de l'élément `main` DevDocs](https://devdocs.io/html/element/main).

## Éléments Section

L'élément `section` est utilisé pour regrouper des sections de contenu dans le document HTML.

Voici un exemple de l'élément `section` :

```html
<h1>Apprenons à propos des éléments de section</h1>
<section>
  <h2>Définition</h2>
  <p>L'élément de section est utilisé pour regrouper des sections de contenu dans le document HTML.</p>
</section>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Screen-Shot-2022-06-25-at-9.34.22-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-9.34.22-PM.png)

Pour en savoir plus sur les éléments `section`, vous pouvez lire cette [explication détaillée de l'élément `section` DevDocs](https://devdocs.io/html/element/section).

## Élément Style

L'élément `style` contient le style de la page web. Cela est connu sous le nom de CSS interne.

L'élément `style` va à l'intérieur des balises `head`.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <style>
    /*Les styles iront ici*/
  </style>
</head>

<body>
  <!--le contenu du site web va ici-->
</body>

</html>
```

Pour en savoir plus, vous pouvez lire cette explication utile de [DevDocs sur l'élément `style`](https://devdocs.io/html/element/style).

## Propriété `text-align` en CSS

Lorsque vous travaillez avec des balises de titre ou de paragraphe, le style par défaut en HTML positionnera le texte sur le côté gauche de la page.

Dans cet exemple, nous avons un `<h1>` qui est placé sur le côté gauche supérieur de la page.

```html
<h1>Apprenons à centrer le texte</h1>
```

![Screen-Shot-2022-04-24-at-11.41.12-AM](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.41.12-AM.png)

Si nous voulions centrer horizontalement ce texte sur la page, alors nous pouvons utiliser la propriété `text-align`.

```css
h1 {
  text-align: center;
}
```

![Screen-Shot-2022-04-24-at-11.42.48-AM](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.42.48-AM.png)

Pour en savoir plus, vous pouvez lire cet article utile sur le centrage du texte : [Text Align en CSS – Comment aligner le texte au centre avec HTML](https://www.freecodecamp.org/news/text-align-in-css-how-to-align-text-in-center-with-html/).

## Regroupement des sélecteurs CSS

Si vous avez plusieurs sélecteurs CSS avec les mêmes styles, alors vous pouvez les regrouper ensemble comme ceci :

```css
h1, h2, h3 {
    text-align: center;
}

```

Remarquez comment les `h1`, `h2` et `h3` sont séparés par des virgules. Le regroupement de plusieurs sélecteurs CSS ensemble nettoie votre CSS et supprime la répétition.

Vous pouvez [lire plus sur les combinateurs CSS ici](https://www.freecodecamp.org/news/css-combinators-to-select-elements/).

## Liaison de feuilles de style externes

L'élément `link` est utilisé dans la plupart des cas pour lier une feuille de style externe au document HTML. L'utilisation de CSS externe est préférée dans la plupart des cas pour aider à garder votre HTML et CSS dans des documents séparés pour une meilleure lisibilité.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
  </body>
</html>
```

`rel="stylesheet"` définit la relation entre le fichier HTML et la feuille de style externe.

Pour en savoir plus, vous pouvez lire cet [exemple DevDocs sur les éléments `link`](https://devdocs.io/html/element/link).

## Balise meta Viewport

Cette balise rend la largeur de la page égale à la largeur de l'écran de l'appareil. Si vous avez un appareil mobile qui fait 600px de large, alors la fenêtre du navigateur fera également 600px de large.

L'initial-scale contrôle le niveau de zoom. La valeur de 1 pour l'initial-scale empêche le zoom par défaut des navigateurs.

```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Propriété background-color

Vous pouvez changer la couleur de fond d'un élément HTML en utilisant la propriété CSS `background-color`.

Disons que nous avons ce balisage HTML.

```html
<h1>Apprenons à propos de la propriété background-color</h1>
<p>Nous apprenons à propos des couleurs de fond</p>
```

Je voulais changer la couleur de fond du blanc par défaut en rose. Nous pouvons cibler le sélecteur `body` et utiliser `background-color: pink;`

```css
body {
  background-color: pink;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-02-at-10.57.53-PM.png)

Pour en savoir plus, vous pouvez lire cet article utile : [CSS Background Color – Comment changer la couleur de fond en HTML](https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/).

## Élément Div

L'élément `div` HTML est utilisé pour regrouper plusieurs éléments HTML et représente un conteneur générique. Cet élément n'a aucune signification sémantique et est principalement utilisé à des fins de style.

```html
<div>
  <h1>Apprenons à propos des divs</h1>
  <p>les éléments div sont des conteneurs génériques pour regrouper des éléments</p>
</div>
```

Pour en savoir plus, vous pouvez lire cet article utile : [HTML Div – Qu'est-ce qu'une balise Div et comment la styliser avec CSS](https://www.freecodecamp.org/news/html-div-what-is-a-div-tag-and-how-to-style-it-with-css/).

## Propriété CSS width

La propriété `width` définira la largeur de l'élément HTML.

Dans cet exemple, je veux définir la largeur de ce `div` à 200px.

```css
div {
  width: 200px;
}
```

Pour en savoir plus, vous pouvez lire cette explication utile de [DevDocs](https://devdocs.io/css/width) sur la propriété width.

## Commentaires CSS

Si vous devez commenter du code ou laisser des messages pour vous-même ou d'autres développeurs, vous pouvez utiliser des commentaires.

Voici la syntaxe de base pour un commentaire en CSS :

```css
/* ceci est un commentaire en CSS */
```

Tout ce qui est à l'intérieur de cette balise de commentaire ne sera pas rendu sur la page web.

Dans cet exemple, nous avons un peu de balisage HTML.

```html
<h1>Commentaires CSS</h1>
<p class="red-text">Ceci est un texte de démonstration</p>
```

Pour le CSS, j'ai changé la couleur du texte en rouge et augmenté la taille de la police.

```css
.red-text {
  font-size: 1.2rem;
  color: red;
}

```

Voici le résultat actuel :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-09-at-9.33.31-PM.png)

Si je commente la couleur du texte rouge, alors le texte redeviendra noir.

```css
.red-text {
  font-size: 1.2rem;
  /* color: red; */
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-09-at-9.34.30-PM.png)

## Propriété Margin

La propriété `margin` représente l'espace autour de l'élément HTML. Il existe quatre propriétés de marge différentes :

* `margin-left`
* `margin-right`
* `margin-top`
* `margin-bottom`

Dans ce premier exemple, nous avons deux éléments `div` qui représentent des boîtes bleue et rouge.

```html
<div class="blue-box"></div>
<div class="red-box"></div>
```

```css
.blue-box,
.red-box {
  width: 200px;
  height: 200px;
}

.blue-box {
  background-color: blue;
}

.red-box {
  background-color: red;
}
```

Voici à quoi ressemble le résultat rendu sur la page :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-09-at-10.26.01-PM.png)

Si nous voulons créer un espace entre les boîtes rouge et bleue, nous pouvons utiliser la propriété `margin`. Je vais ajouter un `margin-bottom: 20px;` à la boîte bleue pour créer de l'espace.

```css
.blue-box {
  background-color: blue;
  margin-bottom: 20px;
}
```

Voici à quoi ressemble le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-09-at-10.27.39-PM.png)

Nous pouvons également centrer les deux boîtes en définissant les propriétés `margin-left` et `margin-right` sur `auto`.

```css
.blue-box,
.red-box {
  width: 200px;
  height: 200px;
  margin-left: auto;
  margin-right: auto;
}
```

Voici le résultat :

%[https://codepen.io/jessica-wilkins/pen/yLKJyjV?editors=1100]

Dans cet exemple suivant, nous avons une boîte verte, une boîte bleue et du texte sur la page. Nous pouvons utiliser les propriétés `margin-left`, `margin-right`, `margin-top` et `margin-bottom` pour créer des espaces entre le texte et les boîtes.

```html
<h1 class="text">Propriété de raccourci de marge</h1>
<div class="green-box"></div>
<p class="text">Les marges créent de l'espace autour des éléments HTML</p>
<div class="blue-box"></div>
<p class="text">CSS est amusant</p>
```

```css
.text {
  text-align: center;
}
.blue-box,
.green-box {
  width: 200px;
  height: 200px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px;
}

.blue-box {
  background-color: blue;
}

.green-box {
  background-color: green;
}

```

Voici le résultat :

%[https://codepen.io/jessica-wilkins/pen/gOeMbjN?editors=1100]

Pour les boîtes bleue et verte, nous pouvons nettoyer notre code ici et placer tous ces styles de `margin` en une seule ligne.

```css
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px;
```

La propriété de raccourci `margin` est utilisée pour définir la marge pour tous les côtés de l'élément. Si deux valeurs sont présentes, alors la première valeur représente les marges supérieure et inférieure tandis que la deuxième valeur représente les marges gauche et droite.

```css
  margin: 20px auto;
```

Pour en savoir plus sur la propriété de raccourci `margin`, vous pouvez lire cette [explication utile de DevDocs](https://devdocs.io/css/margin).

## Sélecteurs de classe

Si vous vouliez qu'un groupe d'éléments HTML partage les mêmes styles, alors vous utiliseriez l'attribut `class`.

Voici un exemple de la façon d'appliquer une classe à un élément HTML.

```html
<h1 class="title">Blog de Jessica Wilkins</h1>
```

Ensuite, dans votre CSS, vous pouvez cibler cette classe et ajouter des styles.

Voici un exemple de transformation de ce texte en rouge, en utilisant CSS. Notez que vous devez précéder le nom de la classe d'un `.` qui indique à l'ordinateur que vous souhaitez utiliser un sélecteur de classe.

```css
.title {
  color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-8.14.24-PM.png)

## Propriété background-image

La propriété `background-image` est utilisée pour définir l'image de fond d'un élément HTML.

Dans cet exemple, nous allons appliquer une image de fond de lasagnes à l'élément `body`.

```css
body {
  background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg");
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-8.38.43-PM.png)

La raison pour laquelle cette image se répète à l'écran est que c'est le comportement par défaut de la propriété `background-image`. Vous pourriez utiliser `background-repeat: no-repeat;` pour changer ce comportement par défaut.

## Élément Article

L'élément `article` est un élément HTML sémantique qui est utilisé pour un contenu indépendant et autonome.

```html
<article>
  <h2>Entrée de blog #3</h2>
  le contenu va ici...
</article>
```

## Valeurs block, inline et inline-block

La propriété `display` est utilisée pour appliquer des caractéristiques de bloc ou en ligne à un élément. Les éléments de niveau bloc occupent tout l'espace horizontal sur la page tandis que les éléments en ligne n'occupent que l'espace horizontal pour cet élément.

Les éléments en ligne ne fonctionneront pas avec les propriétés de largeur et de hauteur. Les valeurs de marge gauche et droite fonctionneront pour les éléments en ligne mais pas les valeurs supérieure et inférieure.

Vous pouvez avoir plusieurs éléments en ligne affichés dans une rangée tandis que vous ne pouvez avoir qu'un seul élément de niveau bloc par rangée. Voici un exemple de plusieurs éléments en ligne dans une rangée :

```html
<a href="">ceci est le lien 1</a>
<a href="">ceci est le lien 2</a>
<a href="">ceci est le lien 3</a>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-9.37.55-PM.png)

Vous pouvez utiliser la valeur `display:block;` sur ces éléments d'ancrage pour changer leur comportement par défaut et le définir sur des caractéristiques de bloc.

```css
a {
  display: block;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-12.40.45-AM.png)

Cet exemple suivant est pour plusieurs éléments de niveau bloc. Remarquez comment chacun de ces `divs` occupe tout l'espace horizontal sur la page et qu'ils ne sont pas affichés les uns à côté des autres.

```html
<div class="box red"></div>
<div class="box green"></div>
<div class="box blue"></div>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-9.42.27-PM.png)

Cette dernière valeur s'appelle `inline-block` qui traitera les éléments comme en ligne mais aura également des caractéristiques des éléments de niveau bloc.

Voici un exemple de deux éléments de paragraphe qui sont des éléments de niveau bloc par défaut.

```html
<p>Ceci est le paragraphe 1.</p>
<p>Ceci est le paragraphe 2.</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-9.47.44-PM.png)

Je peux définir la largeur, la marge, le remplissage et la `background-color` pour ces éléments `p`.

```css
p {
  background-color: #89cff0;
  width: 100px;
  margin: 20px;
  padding: 15px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-9.52.04-PM.png)

Nous pouvons ajouter `display: inline-block;` pour placer les éléments de paragraphe les uns à côté des autres.

```css
p {
  background-color: #89cff0;
  width: 100px;
  margin: 20px;
  padding: 15px;
  display: inline-block;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-9.53.52-PM.png)

## Padding

En CSS, vous pouvez ajouter un padding pour créer de l'espace autour du contenu de l'élément.

Dans cet exemple, nous avons un élément de paragraphe avec un fond rose qui n'utilise pas de padding.

```html
<p>Ceci est un exemple sans padding</p>
```

```css
p {
  background-color: pink;
  width: 100px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-11.44.34-PM.png)

Remarquez comment le texte est collé contre la bordure de l'élément `p`. C'est parce que nous n'avons pas ajouté de padding.

Si nous voulons créer de l'espace autour de ce texte, alors nous pouvons utiliser le padding. Ajoutons 10px de padding sur tous les côtés du texte.

```css
p {
  background-color: pink;
  width: 100px;
  padding: 10px;
}
```


![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-11.57.14-PM.png)

Si nous voulions ajouter du padding uniquement sur les côtés gauche et droit, alors nous pouvons utiliser les propriétés `padding-left` et `padding-right`.

```css
p {
  background-color: pink;
  width: 100px;
  padding-left: 10px;
  padding-right: 10px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-11.57.40-PM.png)

Nous pouvons également le modifier pour qu'il n'y ait de l'espace qu'autour du haut et du bas du texte.

```css
p {
  background-color: pink;
  width: 100px;
  padding-top: 10px;
  padding-bottom: 10px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-11.58.03-PM.png)

Similaire à la propriété `margin`, vous pouvez utiliser une notation raccourcie pour appliquer différents types de padding aux côtés supérieur, gauche, droit et inférieur.

Dans cet exemple, nous allons ajouter 10px de padding au haut et au bas du texte et ajouter 15px de padding aux côtés gauche et droit du texte.

Sans la propriété raccourcie, le code ressemblerait à ceci :

```css
p {
  background-color: pink;
  width: 100px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
}

```

Mais nous pouvons utiliser la notation raccourcie pour obtenir le même résultat. Le premier nombre dans la propriété padding représente le haut et le bas tandis que le deuxième nombre représente la gauche et la droite.

```css
p {
  background-color: pink;
  width: 100px;
  padding: 10px 15px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-05-at-11.58.42-PM.png)

Pour en savoir plus sur la notation raccourcie de padding, vous pouvez lire cette explication utile de [DevDocs](https://devdocs.io/css/padding).

## Propriété `max-width`

La propriété `max-width` est utile lorsque vous souhaitez définir une largeur maximale pour un élément.

Dans cet exemple, nous avons un conteneur rouge avec une `width` définie à 70 % de la largeur de la fenêtre.

```html
<div class="red-container"></div>
```

```css
.red-container {
  width: 70%;
  height: 40px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.11.27-AM.png)

Nous pouvons utiliser la propriété `max-width` pour définir une largeur maximale de 1000px à ce conteneur rouge.

```css
.red-container {
  width: 70%;
  max-width: 1000px;
  height: 40px;
  background-color: red;
}

```

Maintenant, lorsque la fenêtre est plus large que 1000px, la largeur ne sera plus définie à 70 % de la fenêtre. Au lieu de cela, elle restera à la largeur maximale de 1000px.

## Propriété `font-family`

En design, une `font-family` représente une collection de polices qui partagent des caractéristiques de design similaires. Voici quelques exemples de familles de polices :

```
Times, Times New Roman, serif	
Comic Sans MS, Comic Sans, cursive	

```

En CSS, vous pouvez utiliser la propriété `font-family` pour appliquer un ensemble de polices à des éléments donnés.

```html
<h1>Apprenons à propos des familles de polices</h1>
<p>Ceci est un exemple sur la façon d'utiliser la propriété CSS font-family</p>
```

```css
body {
  font-family: Comic Sans MS, Comic Sans, cursive;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.28.01-AM.png)

Le navigateur sélectionnera la première police de la liste et l'affichera si elle est disponible. Si cette police n'est pas disponible, alors il passera à la police suivante de la liste.

Il est bon de fournir une police de repli dans le cas où les autres polices de la liste ne sont pas disponibles pour le navigateur. Dans notre exemple, `cursive` serait considérée comme la police de repli si Comic Sans MS et Comic Sans n'étaient pas disponibles.

## Propriété `font-style`

La propriété `font-style` est utilisée pour définir le texte en style de police normal, italique ou oblique.

Voici un exemple de définition du texte en italique `font-style`.

```html
<h1>Cet exemple concerne la propriété font-style</h1>
```

```css
h1 {
  font-style: italic;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.36.57-AM.png)

Il est important de ne pas utiliser l'[élément HTML `i` (Texte Idiomatique)](https://www.freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag/) pour styliser le texte en italique. En ce qui concerne le style du texte, vous devez toujours utiliser la propriété `font-style`.

## Propriété `font-size`

La propriété `font-size` est utilisée pour changer les tailles de police des éléments HTML comme les titres et les paragraphes. Voici quelques valeurs courantes que vous pouvez utiliser avec la propriété `font-size` :

* xx-small, x-small, small, medium, large, x-large, xx-large, xxx-large
* smaller, larger
* px, em, rem
* pourcentages (par exemple, font-size: 60%;)

Dans cet exemple, nous allons définir la `font-size` pour cet élément de paragraphe à 20px.

```html
<p>Cet exemple concerne la propriété font-size</p>
```

```css
p {
  font-size: 20px;
}

```

## **Éléments Footer**

L'élément `footer` est situé en bas du document HTML et contient des informations comme les droits d'auteur, ou des liens vers d'autres informations liées à la page.

Voici un exemple de base :

```html
<footer>
  <p>
9 2022 Jessica Wilkins</p>
</footer>
```

Pour en savoir plus sur l'élément `footer`, vous pouvez lire cette [explication de DevDocs de l'élément `footer`](https://devdocs.io/html/element/footer).

## **Éléments Anchor**

Un élément d'ancrage représente un lien sur la page web.

Voici la syntaxe de base :

```html
<a href="link-where-you-want-to-go">le texte d'ancrage va ici</a>
```

Voici à quoi cela ressemble rendu sur la page :

![Screen-Shot-2022-06-25-at-5.10.07-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.10.07-PM.png)

Vous utilisez l'attribut `href` pour indiquer à l'hyperlien où aller.

```html
href="link-where-you-want-to-go"
```

Le texte d'ancrage est ce qui est affiché à l'écran pour les utilisateurs.

Voici un exemple de balise d'ancrage qui lie à freeCodeCamp :

```html
<a href="https://www.freecodecamp.org/">freeCodeCamp</a>
```

Voici à quoi cela ressemble rendu sur la page.

![Screen-Shot-2022-06-25-at-5.41.36-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.41.36-PM.png)

Pour en savoir plus sur les éléments d'ancrage HTML, je suggère de lire ces articles utiles :

* [La balise HTML <a> – Exemple de code de balise d'ancrage](https://www.freecodecamp.org/news/the-html-a-tag-anchor-tag-example-code/)
* [Balise HTML <a> – Exemple de lien d'ancrage HREF](https://www.freecodecamp.org/news/html-a-tag-anchor-link-href-example/)

## Élément `hr`

L'élément `hr` (Règle Horizontale) est utilisé pour créer des ruptures entre les éléments de paragraphe.

Voici un exemple de la façon d'utiliser l'élément `hr` entre deux éléments de paragraphe. Les éléments `hr` sont auto-fermants.

```html
<p>Ceci est le paragraphe 1</p>
<hr>
<p>Ceci est le paragraphe 2</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.02.23-AM.png)

Vous pouvez styliser l'élément `hr` en changeant sa bordure et sa couleur.

```css
hr {
  border: 5px solid red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.05.39-AM.png)

## Propriété Height

La propriété `height` en CSS est utilisée pour définir la hauteur d'un élément HTML. Voici un exemple où nous avons un conteneur bleu avec une hauteur de 50px.

```html
<div class="blue-container"></div>
```

```css
.blue-container {
  background-color: blue;
  width: 30px;
  height: 50px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.11.44-AM.png)

Pour en savoir plus sur la propriété `height`, vous pouvez lire cette explication utile de [DevDocs](https://devdocs.io/css/height).

## Propriété `border-color`

La propriété `border-color` est utilisée pour définir la couleur de la bordure d'un élément.

Dans cet exemple, nous allons créer deux éléments de paragraphe avec différentes couleurs de bordure. La première étape consiste à définir les largeurs et le style de la bordure.

```html
<p class="para1">Ceci est le paragraphe un avec une bordure verte</p>
<p class="para2">Ceci est le paragraphe deux avec une bordure bleue</p>
```

```css
p {
  border-style: solid;
  border-width: 3px;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.21.11-AM.png)

Ensuite, nous pouvons définir le premier paragraphe pour avoir une couleur de bordure verte et le deuxième paragraphe pour avoir une couleur de bordure bleue.

```css
.para1 {
  border-color: green;
}

.para2 {
  border-color: blue;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.22.36-AM.png)

Nous pouvons réécrire notre exemple pour utiliser la notation raccourcie de bordure afin d'appliquer la largeur, la couleur et le style de la bordure en même temps.

```css
.para1 {
  border: 3px solid green;
}

.para2 {
  border: 3px solid blue;
}

```

## Propriété Color

Vous pouvez changer la couleur du texte en utilisant la propriété `color`. Voici un exemple pour changer le texte du paragraphe en bleu :

```html
<p>Ceci est un exemple pour la propriété color</p>
```

```css
p {
  color:blue;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-1.30.47-AM.png)

## Pseudo-classes

Les pseudo-classes sont des mots-clés spéciaux que vous pouvez ajouter aux sélecteurs CSS pour montrer l'état spécifique d'un élément HTML.

Dans ce premier exemple, nous allons créer un bouton bleu qui change pour une teinte plus foncée de bleu lorsque l'utilisateur passe la souris dessus. Nous pouvons utiliser la pseudo-classe `:hover` pour obtenir ce résultat.

```html
<button>Connexion</button>
```

```css
button {
  border: none;
  padding: 10px;
  font-size: 20px;
  color: white;
  background-color: #0e3386;
  cursor: pointer;
}

button:hover {
  background-color: #041e42;
}

```

%[https://codepen.io/jessica-wilkins/pen/ExRgXod]

Dans cet exemple suivant, nous allons utiliser des pseudo-classes CSS pour styliser les différents états d'un lien.

La pseudo-classe `:link` est utilisée pour montrer l'état initial du lien.

```css
a:link {
  color: #0066b2;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-2.01.56-AM.png)

La pseudo-classe `:hover` est utilisée pour montrer quand un utilisateur passe la souris sur un lien.

```css
a:hover {
  color: #13274f;
}
```

La pseudo-classe `:visited` est utilisée pour montrer quand un utilisateur clique sur ce lien et visite le site.

```css
a:visited {
  color: #5a4fcf;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-2.11.03-AM.png)

Vous pouvez jouer avec cet exemple CodePen pour voir les différents états des liens.

%[https://codepen.io/jessica-wilkins/pen/RwJGgyP?editors=1100#_=_]

Si vous voulez en savoir plus sur les pseudo-classes, alors vous pouvez lire cet [article utile](https://www.freecodecamp.org/news/explained-css-pseudo-classes-cef3c3177361/).

## **Éléments Image**

Les éléments `img` sont utilisés pour ajouter des images à la page web.

L'attribut `src` représente l'emplacement de l'image et l'attribut `alt` est le texte descriptif de l'image.

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="assiette de lasagnes">
```

Voici à quoi ressemble le code rendu sur la page :

![Screen-Shot-2022-06-18-at-11.41.23-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-11.41.23-PM.png)

Pour en savoir plus sur l'élément `img`, vous pouvez lire ce [tutoriel sur l'élément `img`](https://www.freecodecamp.org/news/img-html-image-tag-tutorial/).

## Ressources supplémentaires pour HTML et CSS

Merci d'avoir lu ! Voici quelques ressources supplémentaires pour vous familiariser avec CSS :

* [Tutoriel CSS – Cours complet pour débutants](https://www.youtube.com/watch?v=OXGznpKZ_sA)
* [Tutoriel CSS - De zéro à héros (Cours complet)](https://www.youtube.com/watch?v=1Rs2ND1ryYc)
* [Apprendre HTML & CSS – Cours complet pour débutants](https://www.youtube.com/watch?v=a_iQb1lnAEQ)
* [Introduction à la conception Web réactive - Tutoriel HTML & CSS](https://www.youtube.com/watch?v=srvUrASNj0s)
* [Tutoriel HTML et CSS - Créer un site Web pour débutants](https://www.youtube.com/watch?v=kMT54MPz9oE)