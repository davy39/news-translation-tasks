---
title: 'Apprendre CSS Grid en recréant des mises en page familières : Airbnb, YouTube
  et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-11T19:24:05.000Z'
originalURL: https://freecodecamp.org/news/learning-css-grid-through-recreating-airbnb-youtube-and-more-399c71377eaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XspBwNvWJWup4WKKuMKMBQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Apprendre CSS Grid en recréant des mises en page familières : Airbnb,
  YouTube et plus'
seo_desc: 'By Cameron Jenkinson

  I learn best by example and I’m guessing you have arrived here because you do as
  well. I’ve found learning the features of CSS Grid much easier by re-creating the
  layouts of products and websites I’m familiar with.

  For each layou...'
---

Par Cameron Jenkinson

J'apprends mieux par l'exemple et je suppose que vous êtes arrivé ici parce que vous aussi. J'ai trouvé l'apprentissage des fonctionnalités de CSS Grid beaucoup plus facile en recréant les mises en page de produits et de sites web que je connais.

Pour chaque mise en page, j'ai utilisé une seule vue principale comme base pour comprendre comment elle serait construite en utilisant CSS Grid.

**À noter :** J'ai omis la plupart des détails complexes sur la façon dont la mise en page est gérée (animations, données, etc.) afin que l'accent soit mis sur l'exploration de la mise en page et le fonctionnement des fonctionnalités de la grille. Donc, veuillez garder à l'esprit que les mises en page peuvent ne pas se comporter exactement comme elles le font officiellement.

Mon objectif pour cet article est de servir de point de référence et de guide pour démarrer des mises en page similaires avec relativement peu de code (ce qui est pourquoi CSS Grid est bon dans ce qu'il fait).

Je prévois d'ajouter des mises en page supplémentaires à ce post au fil du temps.

Dernière mise à jour : **11 décembre 2017**

Mises en page actuelles :

1. Page d'accueil d'Airbnb
2. Page d'accueil de YouTube
3. Vue d'accueil de Pinterest

À venir :

* Soundcloud
* Bloomberg
* Huffington Post

### CSS Grids

Qu'est-ce que CSS Grid ?

> **_CSS Grid Layout_** _excelle dans la division d'une page en régions principales, ou dans la définition de la relation en termes de taille, de position et de couche, entre les parties d'un contrôle construit à partir de primitives HTML._

> _Comme les tableaux, la mise en page de la grille permet à un auteur d'aligner des éléments en colonnes et en lignes. Cependant, de nombreuses autres mises en page sont soit possibles, soit plus faciles avec CSS Grid qu'elles ne l'étaient avec les tableaux. Par exemple, les éléments enfants d'un conteneur de grille pourraient se positionner de manière à ce qu'ils se chevauchent et se superposent, similaire aux éléments positionnés CSS. — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)_

En bref, CSS Grid fournit un ensemble de contrôles et d'outils de mise en page que les implémentations existantes de mises en page basées sur des colonnes et des lignes créées à partir de l'utilisation de largeurs et de propriétés de flottement.

CSS Grid est également plus que cela. Il peut mettre à jour dynamiquement les propriétés en fonction des règles que vous définissez (comme : « lorsque le navigateur a cette largeur, faites ceci »). Par conséquent, je crois que c'est l'avenir des approches de mise en page front-end.

Pour ceux qui sont nouveaux dans le concept de la grille elle-même : une grille est un ensemble de lignes (pensez à un ancien cahier de maths) où elle a des lignes horizontales et verticales qui permettent de définir le placement des éléments.

### Terminologie de la grille :

#### Conteneur de grille

Le conteneur de grille est le parent qui contiendra tous les éléments placés sur la grille. Il définit l'état initial des lignes de la grille (verticales et horizontales).

Pour créer une grille CSS, il suffit d'ajouter `display: grid;` à l'enveloppe ou au conteneur avec lequel vous travaillez dans votre document.

#### Élément de grille

Tous les enfants du conteneur de grille sont référencés comme des éléments de grille.

#### Ligne de grille

Les lignes de grille représentent les colonnes verticales (lignes de grille de colonne) et horizontales (lignes de grille de rangée).

Il existe deux propriétés `grid-template-columns` et `grid-template-rows` qui sont utilisées pour définir les lignes de grille de la mise en page.

`grid-template-columns` définit le placement des colonnes et `grid-template-rows` définit le placement des rangées.

#### Cellule de grille

Il s'agit de la plus petite zone au sein de la mise en page de la grille, qui est l'espace défini par quatre lignes de grille.

#### Zone de grille

Une zone de grille est une zone de conteneur nommée spécifique qui contient des cellules de grille définies par des lignes de grille.

### Apprendre CSS Grid par l'exemple

### 1. [Airbnb](https://www.airbnb.co.uk/s/homes)

#### Mise en page du document :

```
<div class="wrapper">  <header class="header">Airbnb</header>      <article class="content">      	<div class="panel">  		<img src="#" />  		<span>Nom de la maison</span>  	</div>        <!-- Reste des éléments de la maison ... -->      </article>    <aside class="sidebar">Barre latérale - Carte</aside>  </div>
```

#### Grille principale :

```
.wrapper {  margin: 0 auto;  display: grid;  grid-template-columns: 65% 35%;  grid-gap: 16px;}
```

La classe `wrapper` définit le conteneur de grille, celui qui contient les blocs de document principaux (`article` qui est la zone où les éléments de la maison sont contenus, `aside` qui est la carte de la barre latérale).

Après que la propriété `display: grid` a été définie, la mise en page a été définie comme une grille où nous pouvons utiliser `grid-template-columns` pour déclarer la `track-size` des colonnes en utilisant des pourcentages.

La `track-size` peut être une longueur, un pourcentage, ou une fraction de l'espace libre dans la grille (en utilisant l'unité `fr`).

```
.content {  padding: 8px;  display: grid;  margin: 0 auto;  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)) ;  grid-auto-rows: minmax(264px, auto);  grid-gap: 16px;}
```

La grille principale contient un conteneur secondaire (une sous-grille) avec un nom de classe `.content`. Cela représente la zone de l'élément article qui contient tous les éléments de la maison.

La sous-grille est définie avec des colonnes ainsi que des rangées afin que tous les éléments puissent être dimensionnés pour s'adapter.

Il y a quelques nouvelles choses utilisées ici, alors décomposons chacune d'elles.

Lors de la définition des colonnes, nous avons utilisé `repeat(auto-fill, minmax(300px, 1fr));` comme :

`repeat()` évite essentiellement la répétition de la déclaration de la taille de la piste pour chaque colonne, mais cela devient plus intéressant lorsqu'il est utilisé avec `auto-fill`.

Lorsque `auto-fill` est donné comme le nombre de répétitions, si le conteneur de grille a une taille ou une taille maximale définie dans l'axe pertinent, alors le nombre de répétitions est le plus grand entier positif possible qui ne provoque pas le débordement de la grille de son conteneur de grille.

En utilisant `auto-fill` avec `repeat()`, nous avons dit à la grille de déterminer combien d'éléments elle peut contenir dans la taille du conteneur automatiquement sans que nous ayons à faire des calculs supplémentaires.

`minmax` définit une plage de taille supérieure ou égale à `min` et inférieure ou égale à `max`.

Si `max <` min, alors max est ignoré et `minmax(min, max)` est traité comme `min`. En tant que maximum, une valeur définit le facteur de flexibilité de la piste, elle est invalide en tant que minimum.

L'unité `fr` vous permet de définir la taille d'une piste comme une fraction de l'espace libre du conteneur de grille.

Par exemple, ce qui suit définira chaque élément à un tiers de la largeur du conteneur de grille :

`minmax` nous permet de spécifier la largeur à laquelle l'élément doit rester fixe lors du redimensionnement.

Avec les colonnes déclarées, nous passons aux rangées `grid-auto-rows: minmax(275px, auto);`

Nous avons utilisé `minmax` ici pour spécifier la hauteur maximale de chaque élément placé sur la sous-grille, dans ce cas, chaque maison sera de 275px.

En tant que maximum, il est identique à [max-content](https://drafts.csswg.org/css-grid/#valdef-grid-template-columns-max-content). En tant que minimum, il représente la plus grande taille minimale (telle que spécifiée par [min-width](https://drafts.csswg.org/css21/visudet.html#propdef-min-width)/[min-height](https://drafts.csswg.org/css21/visudet.html#propdef-min-height)) des éléments de grille occupant la piste de grille.

`auto` est utilisé au lieu de `1fr` dans la déclaration de colonne car nous voulons que la largeur de l'élément change automatiquement en fonction de la largeur de la colonne.

```
@media (max-width: 1100px) {  .wrapper {    grid-template-columns: 1fr;  }    .sidebar {    display: none;  }    .content {    width: 100%;    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr) ) ;    grid-auto-rows: minmax(300px, auto);  }  }
```

La chose géniale avec les grilles CSS dans cet exemple est que la mise en page n'a nécessité qu'une seule requête média pour créer une mise en page responsive simple.

Avant de me décider pour ce point de rupture, j'ai configuré des points de rupture individuels pour tablette, mobile, etc., mais j'ai trouvé que cela créait un changement saccadé dans la taille des éléments de la maison lors du redimensionnement dans le navigateur, alors je suis resté avec un seul qui offrait une expérience plus fluide.

La différence clé dans la mise en page au sein de la requête média est que la grille principale, qui contenait initialement deux colonnes définies par des pourcentages, a maintenant une colonne définie avec la taille de piste de `1fr` (j'ai également masqué la barre latérale comme dans le comportement en production).

Ensuite, pour chaque élément, les mêmes propriétés et méthodes sont utilisées, mais la différence clé est que j'ai augmenté la hauteur et la largeur des éléments (`360px, 300px`).

C'est tout pour la page d'accueil d'Airbnb, veuillez consulter l'exemple [CodePen](https://codepen.io/cameronjenkinson/full/zPGzLK/) ci-dessus pour voir comment cela fonctionne de manière responsive.

### 2. [YouTube](http://www.youtube.com/)

#### Mise en page du document :

```
<div class="wrapper">  <header class="header">Youtube</header>    <aside class="sidebar">Barre latérale</aside>      <article class="content">         <div class="panel">      <img class="panel-img" src="#">      <span class="panel-title">Titre de la vidéo</span>       <br>      <span class="panel-subtitle">346,112 vues</span>    </div>        <!--   Reste des éléments vidéo ... -->        </article>    </div>
```

#### Grille principale :

```
.wrapper {  margin: 0 auto;  display: grid;  grid-template-columns: 15% 85%;  grid-gap: 16px;}
```

La classe `wrapper` est utilisée à nouveau pour définir la grille principale. Il y a deux colonnes dans la grille principale qui sont associées aux balises `<article>` et `<aside>` du document.

J'ai utilisé des pourcentages pour définir la `track-size` des deux colonnes.

```
.content {  padding-right: 64px;  padding-left: 64px;  display: grid;  margin: 0 auto;  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));  grid-auto-rows: minmax(150px, auto);  grid-gap: 8px;}
```

Une autre sous-grille a été désignée en utilisant la propriété `.content` à nouveau où elle contiendra tous les éléments vidéo.

Veuillez consulter l'exemple Airbnb ci-dessus pour des explications supplémentaires sur les propriétés et méthodes ci-dessous.

Nous avons ensuite défini les colonnes de la grille en utilisant `repeat(auto-fill, minmax(200px, 1fr));` où chaque élément vidéo sera large de 300px et remplira automatiquement la colonne `1fr` en utilisant `auto-fill`.

Les rangées ont été définies en utilisant la méthode `minmax` `grid-auto-rows: minmax(150px, auto);` où chaque élément a une largeur maximale de 200px. Le `minmax` spécifie la hauteur maximale de chaque élément placé sur la sous-grille, dans ce cas, chaque maison aura une hauteur maximale de 150px.

```
@media (max-width: 1200px) {  .wrapper {    grid-template-columns: 2fr;  }    .sidebar {    display: none;  }     .content {    width: 100%;    grid-template-columns: repeat(auto-fill, minmax(200px, 2fr));    grid-auto-rows: minmax(150px, auto);  }}@media (max-width: 768px) {  .content {    padding-right: 48px;    padding-left: 48px;    grid-template-columns: repeat(3, minmax(200px, 3fr));    grid-auto-rows: minmax(150px, auto);  }}@media (max-width: 700px) {  .content {    padding-right: 116px;    padding-left: 116px;    grid-template-columns: repeat(2, minmax(200px, 2fr));    grid-auto-rows: minmax(150px, auto);  }}
```

Il y a trois points de rupture différents utilisés pour refléter le comportement de mise en page responsive de la page d'accueil de YouTube.

La différence clé dans la mise en page au sein de ceux-ci est que nous masquons la barre latérale et définissons différentes colonnes pour les éléments vidéo.

Pour les tablettes et en dessous, les quantités de colonnes sont définies à `3fr`, ce qui signifie qu'il y a 3 colonnes spécifiques dans lesquelles les vidéos peuvent s'adapter jusqu'à ce qu'elles atteignent le mobile où elles sont fixées à `2fr` deux colonnes.

À mesure que la mise en page se rétrécit, le remplissage autour des éléments vidéo (gauche, droite) augmente, garantissant que la taille des miniatures n'augmente pas.

Veuillez consulter l'exemple [CodePen](https://codepen.io/cameronjenkinson/full/YEpxEw/) ci-dessus pour voir comment cela fonctionne.

### 3. [Pinterest](https://www.pinterest.co.uk/)

#### Mise en page du document :

```
<div class="wrapper">  <header class="header">Pinterest</header>      <article class="content">        <div class="panel tall-panel">      <img class="panel-img" src="#" />    </div>        <!--   Reste des éléments épinglés ... -->       </article>    </div>
```

#### Grille principale :

```
.wrapper {  margin: 0 auto;  display: grid;  grid-template-columns: 1fr;  grid-gap: 16px;}
```

Dans la classe `wrapper`, nous définissons le conteneur de grille principal et une seule colonne avec la taille de piste définie à `1fr`.

```
.content {  padding-right: 40px;  padding-left: 40px;  display: grid;  margin: 0 auto;  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));  grid-auto-rows: minmax(200px, auto);  grid-gap: 16px;}
```

La grille secondaire contient tous les éléments épinglés, désignés par le nom de classe `.content` où nous avons défini les colonnes et les rangées.

Lors de la définition des colonnes, nous avons utilisé `repeat(auto-fill, minmax(240px, 1fr));`

Avec les colonnes déclarées, nous passons aux rangées `grid-auto-rows: minmax(200px, auto);`

Nous avons utilisé `minmax` ici pour spécifier la largeur maximale de chaque élément placé sur la sous-grille, dans ce cas, chaque maison sera de 200px.

`auto` est utilisé au lieu de `1fr` dans la déclaration de colonne car nous voulons que la largeur de l'élément change automatiquement en fonction de la largeur de la colonne.

```
@media (max-width: 1200px) {   .content {    padding-right: 72px;    padding-left: 72px;    width: 100%;    grid-template-columns: repeat(3, minmax(220px, 1fr) ) ;    grid-auto-rows: minmax(200px, auto);  }  }
```

Une simple requête média est utilisée pour créer une mise en page responsive où nous mettons à jour la classe `.content` avec un remplissage supplémentaire autour des épingles. Le détail clé sur la façon dont nous gérons les épingles à ce stade est de changer la valeur `auto-fill` dans la méthode repeat à `3`, ce qui indique à la grille que nous voulons pas moins de trois colonnes à ce viewport.

C'est tout pour Pinterest, une mise en page relativement simple comparée aux autres. Veuillez consulter l'exemple [CodePen](https://codepen.io/cameronjenkinson/full/EbNvYd/) ci-dessus pour voir comment cela fonctionne de manière responsive.

C'est tout pour l'instant, j'ajouterai des mises en page supplémentaires tout au long de l'année prochaine et j'espère approfondir la complexité des mises en page à chaque fois.

#### Pour aller plus loin :

* La plupart des apprentissages clés et la base de cet article proviennent de [gridbyexample](https://gridbyexample.com/) de Rachel Andrew
* [CSS-Ticks : Guide complet de la grille](https://css-tricks.com/snippets/css/complete-guide-grid/)
* [CSS Grid Garden](https://cssgridgarden.com/)
* [Documentation CSS Grid](https://drafts.csswg.org/css-grid/)
* Pour créer un système de grille à partir de zéro, consultez ce que [Stuart Robson a mis ensemble](https://24ways.org/2017/design-systems-and-css-grid/)

Publié à l'origine sur [cameronjjenkinson.com](http://cameronjjenkinson.com/exploring-css-through-familiar-layouts/).