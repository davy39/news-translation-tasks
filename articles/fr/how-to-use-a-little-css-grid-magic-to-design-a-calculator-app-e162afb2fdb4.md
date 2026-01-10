---
title: Comment utiliser un peu de magie CSS Grid pour concevoir une application calculatrice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T18:26:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-little-css-grid-magic-to-design-a-calculator-app-e162afb2fdb4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_tl8E-Ui_n4f3W_bTk_AnQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser un peu de magie CSS Grid pour concevoir une application
  calculatrice
seo_desc: 'By Deepika Gunda

  This article is a quick intro to CSS Grid. We will be making a calculator using
  it.

  This article is good for developers who have a basic understanding of CSS and for
  those who want to learn the newer tools CSS offers to style pages.

  ...'
---

Par Deepika Gunda

Cet article est une rapide introduction à CSS Grid. Nous allons créer une calculatrice en l'utilisant.

Cet article est destiné aux développeurs qui ont une compréhension basique de CSS et à ceux qui veulent apprendre les nouveaux outils que CSS offre pour styliser les pages.

J'ai aimé les modèles de zones CSS Grid dès le début ! Les exemples sur le web peuvent sembler compliqués, mais faites-moi confiance, une tentative d'utilisation et vous les aimerez et les utiliserez dans beaucoup de vos projets.

Cette idée est venue après avoir voulu créer quelque chose de similaire à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/2-LP4hidt5n59CzI0AYjN1-gtAZvbSdooSy7)
_Calculatrice_

Notez que les boutons =, 0 et AC sont deux fois plus grands que les boutons normaux. Au début, j'ai pensé à utiliser l'élément HTML table et colspan et rowspan pour faire cela. Mais ensuite, je me suis demandé si nous pouvions le faire en utilisant CSS Flexbox. Après avoir échoué à placer =, 0 et . dans la même ligne, j'ai commencé à réaliser le besoin de CSS Grid.

Le code complet pour cela est disponible ici : [CSS-Grid-Calculator](https://github.com/deepikagunda/CSS-Grid-Calculator).

### Qu'est-ce que CSS Grid ?

> Le module de mise en page CSS Grid offre un système de mise en page basé sur une grille, avec des lignes et des colonnes, ce qui facilite la conception de pages web sans avoir à utiliser des flottements et des positionnements. _— de mon favori w3schools.com_

Je suppose donc que la mise en page principale et le contenu de type tableau ressemblent à des grilles, nous pouvons donc utiliser CSS Grid pour les styliser.

### Première chose à faire pour créer une grille

Nous devons utiliser display:grid sur tout conteneur qui doit être une grille. Dans le cas où c'est toute la page principale du site web, nous pouvons le faire comme ceci :

```
<html>
```

```
<style> #main{       display:grid;     }
```

```
</style>
```

```
<body><div id="main"></div>
```

```
</body></html>
```

### Qu'est-ce qui suit ?

Supposons que vous voulez créer un site web qui a une barre de navigation, une barre latérale droite, une barre latérale gauche et une partie centrale pour le contenu. Typiquement, vous voudriez que la barre de navigation et les barres latérales aient une largeur et une hauteur fixes en termes de pourcentages de la fenêtre d'affichage et que la partie contenu s'étende dans l'espace restant.

Alors, comment faisons-nous cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/o0hK11X4FJa-2at1HoQGrIh274V1CSKBjzwa)
_Mise en page d'un site web typique._

```
<style>#main{ display:grid; grid-template-columns: 20vw auto 20vw; grid-template-rows: 15vh auto; grid-template-areas:"header header header"                     "leftSB content rightSB";
```

```
}#header{ grid-area:header;}#leftSB{  grid-area:leftSB;}#rightSB{  grid-area:rightSB;}#content{grid-area:content;}
```

```
</style><body> <div id="main">   <div id="header>header</div>   <div id="rightSB">right sidebar</div>   <div id="leftSB">left sidebar</div>   <div id="content">content</div> </div>
```

```
</body>
```

Voici ce qui réalise la mise en page dont nous avions besoin.

### Explication détaillée

Dans l'image ci-dessus, vous pouvez voir que nous devons simplement créer des divs simples qui contiennent notre en-tête, nos barres latérales et notre contenu et les ajouter à la racine.

Dans la section style, nous avons ajouté « display:grid » pour le conteneur principal.

Ensuite, nous pouvons voir que globalement nous avons besoin de 2 lignes et 3 colonnes. C'est pourquoi nous avons ajouté la ligne

```
grid-template-columns: 20vw auto 20vw;
```

Nous lui disons que nous avons besoin de 3 colonnes, et que la première colonne doit occuper 20 % de la largeur de la vue, que la colonne suivante est auto (c'est-à-dire tout l'espace disponible à prendre par cette colonne), et que la dernière colonne est à nouveau 20 % de la largeur de la vue.

```
grid-template-rows: 15vh auto;
```

Nous disons ici que nous avons besoin de deux lignes au total. La première ligne sera utilisée pour un en-tête et elle sera de 15 % de la hauteur de la fenêtre d'affichage, et l'espace restant est nécessaire pour la deuxième ligne.

Maintenant vient grid-template-areas. Ici, nous définissons en noms simples ce qui occupera la grille. Supposons que nous voulons que l'en-tête prenne toute la première ligne et qu'il n'y ait pas de divisions. Alors nous utilisons ce qui suit :

```
grid-template-areas:"header header header"
```

Parce que nous avons 3 colonnes, nous devons mentionner header 3 fois. En utilisant le même nom, le résultat sera une région d'en-tête unifiée.

```
grid-template-areas:"header header header"                     "leftSB content rightSB";
```

C'est la grille complète des zones de modèle, qui utilise des noms simples pour définir chaque partie de notre grille 2 * 3.

Maintenant que nous avons défini le modèle de grille, nous allons assigner les divs à ces zones. Nous avons donc utilisé les IDs des divs et assigné le nom de la zone de modèle en utilisant grid-area.

```
#header{ grid-area:header;}#leftSB{  grid-area:leftSB;}
```

C'est tout, nous avons maintenant défini comment ces divs doivent être positionnés sur toutes les tailles de fenêtre d'affichage sans utiliser de flottements ou de largeurs sur des éléments individuels et aussi sans utiliser bootstrap, etc.

N'est-ce pas incroyable ? Voyez ce que nous avons créé en ces quelques lignes en action [ici](https://codepen.io/deepikag/pen/xmLLoE).

### Qu'est-ce qui suit ?

Nous pouvons maintenant travailler sur nos divs pour ajouter des barres latérales, des barres de navigation, etc. Je vais laisser cet exemple ici et maintenant passer à un design de calculatrice un peu plus compliqué en utilisant CSS Grid.

### Définition des composants

Nous avons une section d'affichage de la formule, la section d'affichage actuelle en haut. Le reste ce sont les boutons 0-9, le bouton AC (effacer), et les boutons opérateurs + - * / et =.

Alors, créons des boutons et des divs pour tous les composants et gardons-les dans un conteneur.

```
<body> <div id="root">  <label id="display"> 0</label>  <label id="cdisplay" >0</label>  <button id="clear">AC </button>  <button id="divide">/</button>  <button id="multiply">*</button>  <button id="seven">7</button>  <button id="eight">8</button>  <button id="nine">9</button>  <button id="minus">-</button>  <button id="four">4</button>  <button id="five">5</button>  <button id="six">6</button>  <button id="plus">+</button>  <button id="one">1</button>  <button id="two">2</button>  <button id="three">3</button>  <button id="zero">0</button>  <button id="dot">.</button>  <button id="equal">=</button>   </div> </body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/bUBziyLxRCKEstFELl6blf-mhaiKNqritLd-)
_Notre calculatrice finale_

Regardons l'image de la calculatrice. Vous pouvez voir que nous avons 4 colonnes et 7 lignes. Alors définissons notre grille :

```
#root{ padding:5px; background-color:black; width:240px; height:280px;
```

```
   display:grid;   grid-template-columns: 1fr 1fr 1fr 1fr;   grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;   grid-gap:0.1px;
```

```
   grid-template-areas:    "display display display display"   "cdisplay cdisplay cdisplay cdisplay"   "clear clear divide multiply"   "seven eight nine minus"   "four five six plus"   "one two three equal"   "zero zero dot equal"; }
```

Décomposons cela...

```
display:grid;   grid-template-columns: 1fr 1fr 1fr 1fr;   grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
```

Ici, nous avons dit que nous avons 4 colonnes et 7 lignes et que chaque partie de la grille est de la même taille. Notez que les colonnes et les lignes du modèle utilisent 1fr. Fr est une unité fractionnaire et **1fr** est pour 1 partie de l'espace disponible.

J'ai donné à la div racine une largeur de 240 px et une hauteur de 280 px. Donc 1 fr est approximativement 60px de large * 40 px de haut.

```
grid-template-areas:    "display display display display"   "cdisplay cdisplay cdisplay cdisplay"   "clear clear divide multiply"   "seven eight nine minus"   "four five six plus"   "one two three equal"   "zero zero dot equal"; }
```

Ici, nous avons défini les zones de modèle de grille.

Les zones de modèle de grille sont un ensemble de chaînes de lignes * colonnes. Vous devez ajouter autant de chaînes qu'il y a de lignes dans votre grille. Dans chaque chaîne de ligne, vous devez mentionner ce que chaque colonne contiendra. Le nombre d'éléments dans chaque chaîne doit correspondre au nombre de colonnes.

Notez comment l'affichage occupe toute la première ligne. Il est donc ajouté 4 fois dans la première chaîne de ligne.

cdisplay, c'est-à-dire l'affichage actuel, occupe la deuxième ligne et est défini de manière similaire à l'affichage.

Ensuite viennent les boutons. Le bouton clear est dans la 3ème ligne et les première et deuxième colonnes mises ensemble. C'est pourquoi il est mentionné deux fois dans la chaîne de ligne 3.

Et ainsi de suite...

Maintenant que le travail principal est terminé, nous devons assigner ces zones de grille aux divs.

```
#display{   grid-area:display; }#cdisplay{   grid-area:cdisplay; }#clear {   grid-area:clear; }#divide {   grid-area:divide; } #multiply {   grid-area:multiply; }
```

J'ai montré comment les zones de grille sont assignées pour 4 divs.

L'exemple complet peut être trouvé [ici](https://codepen.io/deepikag/pen/GPvMgd) où nous avons ajouté un peu plus de style.

#### Conclusion

Comme mentionné précédemment, ceci n'est qu'une introduction à CSS Grid et plus spécifiquement aux zones de modèle CSS Grid. J'espère que cet exemple vous fera penser à CSS Grid lorsque vous regarderez des sites web à partir de maintenant et j'espère que vous les utiliserez dans le futur.

Si vous avez aimé mon article, applaudissez. C'est assez encourageant pour moi.

Si vous deviez faire la même tâche, comment l'aborderiez-vous ? Faites-le moi savoir dans les commentaires.