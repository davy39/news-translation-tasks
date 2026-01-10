---
title: Le Guide Ultime de Flexbox — Apprendre par l'Exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-12T04:53:49.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-flexbox-learning-through-examples-8c90248d4676
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9vcCT6S_dFJqR6yed6Vmqw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: flexbox
  slug: flexbox
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: Le Guide Ultime de Flexbox — Apprendre par l'Exemple
seo_desc: 'By Emmanuel Ohans


  _Note — this is a long read, so if you want, you can download this article and read
  it offline [here](https://payhip.com/b/YVGf" rel="noopener" target="blank" title=").

  What’s the best way to understand Flexbox? Learn the fundament...'
---

Par Emmanuel Ohans

![Image](https://cdn-media-1.freecodecamp.org/images/DDLwRS3Jad5brv0RIH2r5K2YxqcvAa1vBThw)
_Note — cet article est long, donc si vous le souhaitez, vous pouvez le télécharger et le lire hors ligne [ici](https://payhip.com/b/YVGf" rel="noopener" target="_blank" title=")._

Quelle est la meilleure façon de comprendre **Flexbox** ? Apprendre les bases, puis construire beaucoup de choses. Et c'est exactement ce que nous allons faire dans cet article.

### Quelques points à noter

* Cet article a été écrit pour les développeurs intermédiaires et suppose que vous connaissez déjà un peu Flexbox. Mais...
* Si vous connaissez un peu CSS mais ne connaissez pas du tout Flexbox, [j'ai écrit un guide complet ici (article gratuit, 46 minutes de lecture)](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af).
* Et si vous ne connaissez pas très bien CSS, je vous recommande de suivre mon [Introduction (pratique) complète à CSS (cours payant avec 74 leçons)](http://bit.ly/learn_css).
* Vous n'avez pas à suivre les exemples de cet article dans l'ordre indiqué ici.
* Flexbox n'est qu'une technique de mise en page. Les projets du monde réel nécessitent plus que des mises en page.
* Lorsque vous voyez une notation telle que `div.ohans`, elle fait référence à une div avec un nom de classe `ohans`.

### Exemple 1 : Comment Créer une Galerie Photo avec Flexbox

Faire en sorte que les photos s'affichent en lignes et en colonnes avec Flexbox est plus facile que ce que la plupart des gens pensent.

Considérons un balisage simple, comme ceci :

```
<main class="gallery">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg">  <img src="/sample.jpg"></main>
```

Nous avons 10 images dans un `main.gallery`.

Supposons que le `main.gallery` a été stylisé pour couvrir l'écran disponible.

```
.gallery {   min-height: 100vh}
```

#### Une Note Rapide sur les Images

Par défaut, les images sont des éléments `inline-block`. Elles ont une largeur et une hauteur. Elles resteront sur une ligne sauf si elles sont contraintes par la taille, comme lorsque les images sont trop grandes pour tenir sur une ligne.

#### Le Point de Départ

En mettant tout ensemble, le résultat de tout le balisage et le style ci-dessus est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/s2ntfDqrLewl66sGtavdhgQybTyD2JX520r2)
_10 images avec leurs déclarations de largeur et de hauteur intactes. Elles passent à la ligne suivante lorsque c'est approprié. De gentils garçons ;)_

Maintenant, introduisons Flexbox :

```
.gallery {    display: flex }
```

À ce stade, le comportement par défaut des images a changé. Elles passent d'éléments `inline-block` à des `flex-items`.

En raison du contexte Flexbox initié dans `.gallery`, les images seront maintenant écrasées sur une seule ligne. De plus, elles s'étireront le long de la verticale comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/sEzCWC3d-xoorKjDGf8TMdq6-ZxtOFMQjIST)
_Les images s'étirent maintenant le long de la verticale et sont écrasées sur une seule ligne. Rien n'est plus laid :(_

Ceci est le résultat du comportement par défaut de Flexbox :

1. Écraser tous les éléments enfants sur une seule ligne. Ne pas envelopper les éléments.

Ce n'est pas bon pour une galerie, donc nous changeons ce comportement comme suit :

```
.gallery {    flex-wrap: wrap}
```

Cela enveloppera maintenant les éléments et les brisera sur plusieurs lignes lorsque c'est approprié.

![Image](https://cdn-media-1.freecodecamp.org/images/JGAnqvkIeN-q8vh1beADx0XUrUE6SEZkGQFp)
_Avec la valeur d'enveloppement modifiée, les images passent maintenant à la ligne suivante_

2. Les images passent maintenant à la ligne suivante. Mais elles s'**étirent** toujours le long de la verticale. Nous ne voulons certainement **pas** ce comportement car il déforme les images.

Le comportement `stretch` est dû à la valeur par défaut `align-items` sur les conteneurs `flex`.

```
align-items: stretch
```

Changeons cela :

```
.gallery {  ...  align-items: flex-start}
```

Cela empêchera les images de s'étirer. Elles prendront leurs valeurs de `width` et `height` par défaut.

Elles s'aligneront également au début de l'axe vertical comme vu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/02VgeT3SyoxuWFwkqyD1pzEjFzUjMH160mn0)
_Nous avons maintenant des images qui ne sont pas déformées. C'est à peu près là où nous avons commencé avant d'introduire Flexbox._

Nous avons maintenant notre galerie alimentée par Flexbox.

#### L'Avantage d'Utiliser Flexbox

À ce stade, il n'y a pas beaucoup d'avantages à utiliser Flexbox. Nous avons le même aspect que nous avions avant d'initier le modèle **Flexbox**.

Outre l'obtention d'une galerie réactive gratuitement, les autres avantages de l'utilisation de Flexbox proviennent des options d'alignement qu'il apporte.

Rappelez-vous que le conteneur flex, `.gallery` assume les valeurs de propriétés suivantes : `flex-direction: row`, `justify-content: flex-start` et `align-items: flex-start`.

La disposition de la galerie peut être changée en un instant en modifiant les valeurs par défaut comme montré ci-dessous :

```
.gallery {   ...   justify-content:center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/etSBjIv9EwausQZC8PCe3tdHj0JovaLXkNvs)
_Les images sont maintenant parfaitement centrées le long de l'horizontale._

Comme vu dans l'image ci-dessus, cela alignera les images au centre, le long de l'horizontale :

```
.gallery {   ...   justify-content:center;   align-items: center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/jSx35Bma2fYhAISiEg0B3TcZanxoy0hPOb8D)
_Allant plus loin, nous avons les images parfaitement alignées au centre (horizontalement et verticalement)_

Comme vu dans l'image ci-dessus, cela aligne les images à la fois horizontalement et verticalement au centre de `.gallery`.

Avec Flexbox viennent beaucoup d'options d'alignement. N'hésitez pas à jouer avec d'autres options d'alignement comme vous le jugez approprié.

Vous pouvez voir la galerie Flexbox réelle dans ce [CodePen](https://codepen.io/ohansemmanuel/full/dzgLLw/).

### Exemple 2 : Comment Construire des Cartes avec Flexbox

Les cartes sont devenues populaires sur Internet. Google, Twitter, Pinterest, et il semble que tout le monde passe aux cartes.

Une carte est un modèle de conception d'interface utilisateur qui regroupe des informations connexes dans un conteneur de taille flexible. Elle ressemble visuellement à une carte à jouer.

Il y a de nombreuses bonnes utilisations pour les cartes. Une utilisation courante est la célèbre grille de tarification.

![Image](https://cdn-media-1.freecodecamp.org/images/wjb-g2V7hV6IvRbGaDHYmAePhTjwR5ZeekkX)
_maquette de grille de tarification exemple_

Construisons-en une.

#### Le Balisage

Chaque carte assumera un balisage comme ci-dessous :

```
<section class="card">  <header>  </header>
```

```
  <ul>    <li></li>    <li></li>    <li></li>  </ul>  <button></button></section>
```

Il y aura au moins 3 cartes. Enveloppez les cartes dans un `div.cards`.

```
<div class="cards"></div>
```

Maintenant, nous avons un élément parent.

Pour cet exemple, l'élément parent a été configuré pour remplir toute la fenêtre.

```
.cards {   min-height: 100vh}
```

#### Configurer Flexbox

Le bloc de code suivant initiéra un contexte de formatage Flexbox dans `.cards`.

```
.cards {  display: flex;  flex-wrap: wrap}
```

Si vous vous souvenez du dernier exemple, `flex-wrap` permettra aux `flex-items` de passer à une autre ligne.

Cela se produit lorsque les éléments enfants ne peuvent pas tenir dans l'élément parent. Cela est dû à la largeur calculée plus grande des éléments enfants combinés.

Allez-y et donnez à `.card` une largeur initiale.

En utilisant Flexbox :

```
.card {  flex: 0 0 250px}
```

Cela définira les valeurs `flex-grow` et `flex-shrink` à `0`. La valeur `flex-basis` sera définie à `250px`.

À ce stade, les cartes seront alignées au début de la page. Elles s'étireront également le long de la verticale.

![Image](https://cdn-media-1.freecodecamp.org/images/dkco2Y-Dru2WyMonIq51riqbYtjVr2Zn3E4T)
_cartes alignées au début de la page_

Dans certains cas, cela peut être idéal pour votre cas d'utilisation. Mais pour la plupart des cas, ce ne sera pas le cas.

#### Le Comportement par Défaut des Conteneurs Flex

Le résultat ci-dessus est dû au comportement par défaut des conteneurs flex.

Les cartes commencent au début de la page en haut à gauche car `justify-content` est défini sur la valeur `flex-start`.

De plus, les cartes s'étirent pour remplir toute la hauteur de l'élément parent car `align-items` est défini sur `stretch` par défaut.

#### Modifier les Valeurs par Défaut

Nous pouvons obtenir des résultats assez impressionnants en changeant les valeurs par défaut que Flexbox offre.

Voir ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/hq7D1wJINa5-DC77TMt4e517xOAG6C46yKZ3)
_align-items: flex-start; justify-content: center_

![Image](https://cdn-media-1.freecodecamp.org/images/R8-ShSWPknA8m7CBl1UNMj4qdbhycAIp1D9r)
_align-items: flex-end; justify-content: center_

![Image](https://cdn-media-1.freecodecamp.org/images/B9jkLQHZp7Cze2rEPkE8mzUfBDRWuf5nXFYP)
_align-items: center; justify-content: center_

Pour voir le projet final, consultez ce [CodePen](https://codepen.io/ohansemmanuel/full/Ljqdpa/).

### Exemple 3 : Comment Construire des Grilles avec Flexbox

Des frameworks CSS entiers sont construits sur le concept qui sera discuté dans cet exemple. C'est un sujet assez important.

#### Qu'est-ce qu'une Grille ?

Une grille est une série de lignes directrices verticales et horizontales droites qui se croisent, utilisées pour structurer le contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/06AK1XPmRT2w0zMezFzS2W50a8-xxwmujZEb)
_une série de lignes directrices droites (verticales, horizontales) qui se croisent_

Si vous êtes familier avec des frameworks CSS tels que Bootstrap, alors vous avez certainement utilisé des grilles auparavant.

Votre expérience peut varier, mais nous considérerons différents types de grilles dans cet exemple.

Commençons par le premier, les **grilles de base**.

#### Grilles de Base

![Image](https://cdn-media-1.freecodecamp.org/images/emC8Q5HRNl1dVcCGxvvheVNZYpQ0Ce05-MMc)
_Un ensemble de grilles de base ayant chacune des colonnes également espacées_

Ce sont des grilles avec les caractéristiques suivantes :

* Les cellules de la grille doivent être espacées de manière égale et s'étendre pour remplir toute la ligne.
* Les cellules de la grille doivent avoir la même hauteur.

Il est facile d'y parvenir avec Flexbox. Considérez le balisage ci-dessous :

```
<div class="row">  <div class="row_cell">1</div></div>
```

Chaque `.row` sera son propre conteneur flex.

Chaque élément dans `.row` devient alors un élément flex. Tous les éléments flex se distribuent uniformément sur la ligne.

Par conception, il ne devrait pas importer si nous avons 3 éléments enfants

```
<div class="row">  <div class="row_cell">1/3</div>  <div class="row_cell">1/3</div>  <div class="row_cell">1/3</div></div>
```

Ou 6 éléments enfants

```
<div class="row">  <div class="row_cell">1/6</div>  <div class="row_cell">1/6</div>  <div class="row_cell">1/6</div>  <div class="row_cell">1/6</div>  <div class="row_cell">1/6</div>  <div class="row_cell">1/6</div></div>
```

Ou 12 éléments

```
<div class="row">  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div>  <div class="row_cell">1/12</div></div>
```

#### La Solution

Il y a juste deux étapes pour faire cela.

1. Initiate a Flexbox formatting context:

```
.row {   display: flex;}
```

2. Have each `flex-item` expand to fit the entire row in equal proportions:

```
.row_cell {   flex: 1}
```

Et c'est tout.

#### La Solution Expliquée.

```
flex: 1
```

`flex` est un nom de propriété raccourci pour définir trois propriétés Flexbox distinctes, les propriétés `flex-grow`, `flex-shrink` et `flex-basis`, dans l'ordre indiqué.

`flex: 1` n'a que la valeur `1` définie. Cette valeur est attribuée à la propriété `flex-grow`.

Les propriétés `flex-shrink` et `flex-basis` seront définies à `1` et `0`.

```
flex: 1  === flex: 1 1 0
```

#### Cellules de Grille avec des Tailles Spécifiques

Parfois, ce que vous voulez n'est pas une ligne de grille de cellules égales.

Vous pouvez vouloir des cellules qui sont le double des autres cellules, ou n'importe quelle fraction d'ailleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/CKD3-ZUoxNAOJ-bp-cUZ0XcxnnMB1OvvA2yX)
_grille de cellules de ligne qui sont 2x ou 3x les autres cellules._

La solution est assez simple.

À ces cellules de grille spécifiques, ajoutez une classe modificatrice comme suit :

```
.row_cell--2 {   flex: 2}
```

Ayez la classe incluse dans le balisage. Voir le premier enfant `div` dans le balisage ci-dessous :

```
<div class="row">  <div class="row_cell row_cell--2">2x</div>  <div class="row_cell">1/3</div>  <div class="row_cell">1/3</div></div>
```

La cellule avec la classe `.row__cell--2` sera 2 fois les cellules par défaut.

Pour une cellule qui prend 3 fois l'espace disponible :

`.row_cell--3 {`  
 `flex: 3`  
`}`

#### Cellules de Grille avec des Alignements Spécifiques

Grâce à Flexbox, chaque cellule n'a pas à être liée à une certaine valeur d'alignement. Vous pouvez spécifier l'alignement spécifique pour n'importe quelle cellule.

Pour ce faire, utilisez des classes modificatrices comme ceci :

```
.row_cell--top {  align-self: flex-start}
```

Cela alignera la cellule spécifique en haut de la `row`.

![Image](https://cdn-media-1.freecodecamp.org/images/rSpBVp7JoobnRoc0-Vsb6CjfzyKxO9c5pUwq)
_l'application de la classe .row_cell — top alignera la cellule spécifique en haut de la `row`_

Vous devez également avoir ajouté la classe à la cellule spécifique dans le balisage. Voir le premier enfant `div` dans le balisage ci-dessous :

```
<div class="row">  <div class="row_cell row_cell--top"></div>  <div class="row_cell"></div>  <div class="row_cell"></div></div>
```

Voici les autres options d'alignement disponibles :

```
.row_cell--bottom {  align-self: flex-end}
```

![Image](https://cdn-media-1.freecodecamp.org/images/V76ETVyzFX4E7HLQ3MLr03LSH6GkYnvjEzNa)
_l'application de la classe .row_cell — bottom alignera la cellule spécifique en bas de la `row`_

```
.row_cell--center {  align-self: center}
```

![Image](https://cdn-media-1.freecodecamp.org/images/N-KfRijROiUyGtSj6RTAZmZjNZZ5A3Djf2NA)
_l'application de la classe .row_cell — center alignera la cellule spécifique au centre de la `row`_

#### Alignement Global dans les Lignes

Comme les cellules spécifiques peuvent être alignées, les éléments enfants **entiers** dans la ligne peuvent l'être aussi.

Pour ce faire, utilisez une classe modificatrice comme suit :

```
.row--top {   align-items: flex-start}
```

![Image](https://cdn-media-1.freecodecamp.org/images/le3bablkysAG-j-JEQQdHyBvvjiCbIfZP2Bs)
_une ligne avec les trois cellules alignées en haut de la ligne._

Il est important de noter que la classe modificatrice, `.row--top` doit être ajoutée à la `row` ou au conteneur parent `flex-container`.

```
<div class="row row--top">  <div class="row_cell"></div>  <div class="row_cell"></div>  <div class="row_cell"></div></div>
```

Les autres options d'alignement peuvent être vues ci-dessous :

```
.row--center {   align-items: center}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NVv3xZxxaIbyPHDJTxp5LdcG-Be0wolyXiCb)
_une ligne avec les trois cellules alignées au centre de la ligne._

```
.row--bottom {   align-items: flex-end}
```

![Image](https://cdn-media-1.freecodecamp.org/images/OsI1AJj-F4BMIJQAMN82bY6MXqTxvwmZkw3J)
_une ligne avec les trois cellules alignées au centre de la ligne._

#### Grilles Imbriquées

Sans faire quoi que ce soit de particulier, ces `rows` peuvent être imbriquées les unes dans les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/2eyhYZJlDdZXJkiLuwGYSoB83KKPxnfgfjCg)
_Une ligne avec deux cellules, l'une 2x l'autre. Dans la cellule plus grande, une ligne de trois cellules centrées a été imbriquée._

Vous pouvez voir les grilles finales [créées ici](https://codepen.io/ohansemmanuel/full/xLBLLG/).

#### Encore Plus de Grilles

Bien que vous puissiez vous amuser à construire des grilles avec Flexbox, des grilles verticales et des configurations encore plus complexes, utilisez le meilleur outil pour le travail. Apprenez, maîtrisez et utilisez la [Mise en Page de Grille CSS](https://medium.com/flexbox-and-grids/how-to-efficiently-master-the-css-grid-in-a-jiffy-585d0c213577). C'est la solution CSS ultime pour les grilles.

### Exemple 4 : Comment Construire des Mises en Page de Sites Web avec Flexbox

La communauté désapprouve généralement l'utilisation de Flexbox pour des mises en page web complètes.

Bien que je sois d'accord avec cela, je pense également que dans certains cas, vous pouvez vous en tirer.

Le conseil le plus important que je puisse donner ici serait :

> **_Utilisez Flexbox là où cela a du sens_**

Je vais expliquer cette déclaration dans l'exemple suivant.

#### La Mise en Page du Saint Graal

Quelle meilleure mise en page de site web construire que l'infâme « **saint graal** » ?

![Image](https://cdn-media-1.freecodecamp.org/images/9HvLwuqluns72rMdkVL4SMf5pyPQMxFb9mSi)
_La mise en page du saint graal — en-tête, pied de page et 3 autres conteneurs de contenu._

Il y a 2 façons d'essayer de construire cette mise en page avec Flexbox.

La première consiste à avoir la mise en page construite avec Flexbox. Placez l'`header`, le `footer`, le `nav`, l'`article` et l'`aside` tous dans un seul `flex-container`.

Commençons par cela.

#### Le Balisage

Considérez le balisage de base ci-dessous :

```
<body>  <header>Header</header>  <main>    <article>Article</article>    <nav>Nav</nav>    <aside>Aside</aside>  </main>  <footer>Footer</footer></body>
```

Parmi d'autres, il y a une règle particulière à laquelle le saint graal adhère. Cette règle a inspiré le balisage ci-dessus :

La colonne centrale, `article`, doit apparaître en premier dans le balisage, avant les deux barres latérales, `nav` et `aside`.

![Image](https://cdn-media-1.freecodecamp.org/images/YDZbT2gN-JVcBRbvAkXYasm3Hqo-Q7VtxbU9)
_"<article></article>" apparaît en premier dans le balisage, mais est centré dans la mise en page._

#### Initiate the Flexbox Formatting Context

```
body {   display: flex}
```

Because the child elements should stack from top to bottom, the default direction of the Flexbox must be changed.

```
body { ... flex-direction: column}
```

**1**. `header` and `footer` should have a fixed width.

```
header,footer {  width: 20vh /*you can use pixels e.g. 200px*/}
```

**2.**`main` must be made to fill the available remaining space within the `flex-container`

```
main {   flex: 1}
```

Assuming you didn’t forget, `flex: 1` is equivalent to `flex-grow: 1` , `flex-shrink: 1` and `flex-basis: 0`

![Image](https://cdn-media-1.freecodecamp.org/images/eBj3j7v59T5PYdH8sBCadGevCVyOlPfuMIqR)
_This will cause `main` to “grow” and contain the available remaining space._

At this point, we need to take care of the contents within `main` which are `article`, `nav` and `aside`.

Set up `main` as a `flex-container` :

```
main {  display: flex}
```

Have the `nav` and `aside` take up fixed widths:

```
nav,aside {  width: 20vw}
```

Ensure that `article` takes up the remaining available space:

```
article {   flex: 1}
```

![Image](https://cdn-media-1.freecodecamp.org/images/3--f-KqkBdvx8jv6n9mhmA354cP7OvgS4Ayz)
_`"article"` now takes up the remaining available space_

There’s just one more thing to do now.

Re-order the `flex-items` so `nav` is displayed first:

```
nav {  order: -1}
```

![Image](https://cdn-media-1.freecodecamp.org/images/rN1l8s8aO44ecL8RBUIG824WpUNHBIyl5iLo)
_The final result. [https://codepen.io/ohansemmanuel/full/brzJZz/](https://codepen.io/ohansemmanuel/full/brzJZz/" rel="noopener" target="_blank" title=")_

The `order` property is used to re-order the position of `flex-items`.

All `flex-items` within a container will be displayed in **increasing** `order` values. The `flex-item` with the lowest `order` values appear first.

All `flex-items` have a default `order` value of `0`.

#### The Holy Grail Layout (another solution)

The previous solution used a `flex-container` as the overall container. The layout is heavily dependent on Flexbox.

Let’s see a more “sane” approach. Take a look at the supposed final result again:

![Image](https://cdn-media-1.freecodecamp.org/images/UIy61i1OzIjdddu2W5i9NvL74JXjY5sclt8i)
_The holy grail layout_

`header` and `footer` could be treated as block elements. Without any intervention, they will fill up the width of their containing element, and stack from top to bottom.

```
<body>  <header>Header</header>  <main>    <article>Article</article>    <nav>Nav</nav>    <aside>Aside</aside>  </main>  <footer>Footer</footer></body>
```

With this approach, the only `flex-container` needed would be `main`.

The singular challenge with this approach is that you have to compute the height of `main` yourself. `main` should fill the available space besides the space taken up by the `header` and `footer`.

```
main {  height: calc(100vh - 40vh);}
```

Consider the code block above. It uses the CSS `calc` function to compute the height of `main`.

Whatever your mileage, the height of `main` must be equal to `calc(100vh — height of header — height of footer )`.

As in the previous solution, you must have given `header` and `footer` a fixed height. Then go ahead and treat `main` the same way as in the previous solution.

You may view the [actual results here](https://codepen.io/ohansemmanuel/full/brzybZ/).

#### 2 column website layouts

Two column layouts are pretty common. They are also easily achieved using Flexbox.

![Image](https://cdn-media-1.freecodecamp.org/images/Mk-G8NgfEsSoMlzbafucKr5IUHOiSAcr4cEp)
_2 column layout with a sidebar and main content area._

Consider the markup below:

```
<body>  <aside>sidebar</aside>  <main>main</main></body>
```

Initiate the Flexbox formatting context:

```
body {  display: flex;}
```

Give `aside` a fixed width:

```
aside {   width: 20vw}
```

Finally, ensure that `main` fills up the remaining available space:

```
main {  flex: 1}
```

That’s pretty much all there is to it.

### Example 5: Media Objects with Flexbox

Media Objects are everywhere. From tweets to Facebook posts, they seem to be the go to choice for most UI designs.

![Image](https://cdn-media-1.freecodecamp.org/images/hoOVQQcGFJ-EivoJRCqOTXynRzq88ye3zzE6)
_Sample Tweet and Facebook post_

Consider the markup below:

```
<div class="media">  <img class="media-object" src="/pic.jpg">  <div class="media-body">    <h3 class="media-heading"> Header </h3>    <p></p>  </div></div>
```

As you have guessed, `.media` will establish the Flexbox formatting context:

```
.media {   display: flex}
```

By default, the `flex-items` of a `container` are stretched along the vertical to fill the available height within the `flex-container`.

Make sure the `.media-body` takes up all the remaining available space:

```
.media-body {   flex: 1}
```

![Image](https://cdn-media-1.freecodecamp.org/images/zJRJJ8NeVDHI1FNdnsKF5mpeRXjabOb-zVk9)
_The box on the left stretches to fit the available screen. The media body takes up the remaining horizontal space within the media object (white)_

Let’s fix the stretched box.

```
.media {  ...  align-items: flex-start}
```

![Image](https://cdn-media-1.freecodecamp.org/images/hkcBJNNimRRArL6iPiDoFN3UdSJSHdRazWlw)
_The flex items are now aligned to the start of the media object. The image now takes it default’s size. No weird stretching :)_

And that’s it.

#### A flipped Media Object

![Image](https://cdn-media-1.freecodecamp.org/images/GL7OTu019Ov2HtElcXKhObmhreC86yEDpKK0)
_A flipped media object has the image on the other side (right) of the media object_

You do not have the change the `html` source order to create a flipped media object.

Just re-order the `flex-item`s like so:

```
.media-object {   order: 1}
```

This will have the image displayed after the `.media-body` and `media-heading`

#### A Nested Media Object

You may even go on to nest the Media object. Without changing any of the CSS styles we have written.

```
<div class="media">  <img class="media-object" src="/pic.jpg">  <div class="media-body">    <h3 class="media-heading"> Header </h3>    <p></p>        <!--nested-->    <div class="media">    <img class="media-object" src="/pic.jpg">    <div class="media-body">        <h3 class="media-heading"> Header </h3>        <p></p>    </div>    </div><!--end nested-->  </div> </div>
```

It works!

![Image](https://cdn-media-1.freecodecamp.org/images/cH3o4d2UTkqB1qWCqymnvLjyGpmJ3mmEq-Ro)
_Media objects nested within media objects._

#### A Unicode Media Object

It appears we are not restricted to just images.

Without changing any of the CSS styles written, you can have a unicode represent the image.

```
<div class="media">  <div class="media-object">?</div>  <div class="media-body">    <h3 class="media-heading"> Header </h3>    <p></p>  </div></div>
```

I have snugged in an emoji there.

![Image](https://cdn-media-1.freecodecamp.org/images/i5nrdZwTbOz3vGgZZUAwyqaG9GZEzWJSmh8i)
_Media object with emoji support._

Taking away the `img` and replacing it with a `div` containing the desired unicode yields the output above.You may grab some more emoji unicodes [here](https://emojipedia.org).

#### An HTML Entity Media Object

You may have also use [html entities](https://www.w3schools.com/html/html_entities.asp) as seen below.

```
<div class="media">  <div class="media-object">F4F1</div>  <div class="media-body">    <h3 class="media-heading"> Header </h3>    <p></p>  </div></div>
```

The html entity used in this example is `F4F1` and you may see the result below.

![Image](https://cdn-media-1.freecodecamp.org/images/ssilgIfm3znqoCXzkmUXSnOuvziC5MauRQ0h)
_html entity, F4F1_

You can view the result of these examples in this [CodePen](https://codepen.io/ohansemmanuel/full/jLJbGL/).

### Example 6: How to Build Form Elements with Flexbox

It is difficult to find any website that does not have a form or two these days.

![Image](https://cdn-media-1.freecodecamp.org/images/h8nCEyfprhm-MuBBUjW-vpd7W2LY6L2tdmYg)
_form inputs appended and prepended with other elements_

Consider the markup below:

```
<form class="form">  <input class="form__field">  <button class="form__item">F4F1</button></form><form class="form">  <span class="form__item">F4F1</span>  <input class="form__field"></form><form class="form">  <span class="form__item">F4F1</span>  <input class="form__field">  <button class="form__item">F4F1</button></form>
```

This example shows the combination of aligning input fields with buttons or spans of text. The solution again is quite easy with Flexbox.

Initiate the Flexbox formatting context:

```
.form {  display: flex}
```

Ensure the input field takes up the available space:

```
.form__field {   flex: 1}
```

Finally, you may style the appended or prepended texts and buttons whichever way you seem fit.

```
.form__item {  ... }
```

You may view the complete result of this example in this [CodePen](https://codepen.io/ohansemmanuel/full/ZJPmNj/).

### Example 7: How to Build a Mobile App Layout with Flexbox

In this example, I will walk you the process the mobile app layout below:

![Image](https://cdn-media-1.freecodecamp.org/images/FDxWh9vQBhjQ2L6pSyb2w4QuqJvIjjuXElFF)
_The mobile app layout we will build with Flexbox_

However, this example is different.

I will explain the process of building the mobile layout in pseudo code, and you’ll go ahead to build it.

This will be a form of practice to get your hands **wet**.

#### Step 1

Strip the layout off the iPhone, and we have this:

![Image](https://cdn-media-1.freecodecamp.org/images/cH4ifH1HxdWH9M7IpSEphw9dz7op6WJ7KM8v)
_The barebones layout_

#### Step 2

Define the containing body as a `flex-container`

![Image](https://cdn-media-1.freecodecamp.org/images/gGlfDGRg8mSHNpD-PqZGNI9JnIzTCQiSOWrb)
_Initiate the Flexbox formatting context as a flex container._

#### Step 3

By default, the `flex-direction` of a `flex-container` is set to `row`. In this case, change it to `column` .

![Image](https://cdn-media-1.freecodecamp.org/images/C1KEFWls3---EMGS2nEiLh8pXnk6a2YOH7x0)
_Change the default flex direction to have 3 child elements aka `flex-items`_

#### Step 4

Give Item 1 and 3 fixed heights such as `height: 50px.`

#### Step 5

Item 2 must have a height that fills up the available space. Use `flex-grow` or the `flex` shorthand `flex: 1.`

#### Step 6

Finally, treat each block of content as a Media Object as seen in an earlier example.

![Image](https://cdn-media-1.freecodecamp.org/images/ZD4lqIbYDidmyyCu-lGXi9QXpKjaX7eOUScN)
_Treat the blocks of content as media objects._

Follow the six steps above to successfully build the mobile app layout successfully.

### Want to become Pro?

Download my free CSS Grid cheat sheet, and also get two quality interactive Flexbox courses for free!

![Image](https://cdn-media-1.freecodecamp.org/images/Hisu3Q2Yz70DyjZSPfJ3Dr0gnZ9eB38g152g)
_[Get the Free CSS Grid Cheat sheet + Two Quality Flexbox Courses for free!](http://eepurl.com/dcNiP1" rel="noopener" target="_blank" title=")_

[Get them now](http://eepurl.com/dcNiP1)