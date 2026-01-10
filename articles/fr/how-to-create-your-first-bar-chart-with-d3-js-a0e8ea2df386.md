---
title: Apprendre à créer un graphique à barres avec D3 - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T20:41:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-bar-chart-with-d3-js-a0e8ea2df386
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4gyftwYFlIenlKtILaiqbw.png
tags:
- name: coding
  slug: coding
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
seo_title: Apprendre à créer un graphique à barres avec D3 - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen


  _Want to learn D3 properly? Check out our free course as well._

  D3.js is the most popular JavaScript library for creating visual representations
  of your data. However, it’s a bit tricky to learn, so I think it’s important to
  sta...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/8dC3-aSGvqDWCs-25l0ny4Un8uV7ujrgEEoG)
_Voulez-vous apprendre D3 correctement ? Consultez également [notre cours gratuit](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gd3js_bar_chart_article)._

[D3.js](https://d3js.org/) est la bibliothèque JavaScript la plus populaire pour créer des représentations visuelles de vos données. Cependant, elle est un peu difficile à apprendre, donc je pense qu'il est important de commencer en douceur.

Dans ce tutoriel, vous apprendrez à créer votre tout premier graphique à barres avec D3. Cela vous donnera une introduction aux concepts les plus importants, tout en vous amusant à construire quelque chose.

**Nous avons également créé un cours gratuit sur D3.js sur Scrimba.** **[Découvrez-le ici.](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_bar_chart_article)**

Maintenant, commençons.

#### L'installation

Nous utiliserons la configuration la plus simple possible, en important simplement la bibliothèque D3 depuis un CDN.

```html
<html>  
  <head>  
    <link rel="stylesheet" href="index.css">  
  </head>  
  <body>  
    <svg></svg>  
    <script src="https://d3js.org/d3.v4.min.js"></script>  
    <script></script>  
  </body>  
</html>

```

Nous écrirons notre code D3 dans la balise script. Deuxièmement, nous avons ajouté un élément `<svg>` au DOM. Si vous souhaitez jouer avec le code tout en lisant ce tutoriel, consultez [ce terrain de jeu Scrimba](https://scrimba.com/c/cyKgGCL?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_bar_chart_article), qui contient la version finale du code.

La première chose que nous allons faire est de sélectionner cet élément et de le styliser un peu.

```js
var svgWidth = 500;  
var svgHeight = 300;

var svg = d3.select('svg')  
    .attr("width", svgWidth)  
    .attr("height", svgHeight)  
    .attr("class", "bar-chart");

```

Nous lui donnons une largeur et une hauteur, plus une classe `.bar-chart`. Dans notre CSS, nous avons stylisé la classe comme ceci :

```css
.bar-chart {  
    background-color: #C7D9D9;  
}

```

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pe1Psj8v6GbOqP9tlGnJkQ.png)

Maintenant, nous avons un beau conteneur SVG où nous pouvons dessiner notre graphique à barres. Le code pour le faire est un peu complexe, alors regardons d'abord l'ensemble puis passons en revue chaque étape :

```js
var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];

var barPadding = 5;  
var barWidth = (svgWidth / dataset.length);

var barChart = svg.selectAll("rect")  
    .data(dataset)  
    .enter()  
    .append("rect")  
    .attr("y", function(d) {  
        return svgHeight - d  
    })  
    .attr("height", function(d) {  
        return d;  
    })  
    .attr("width", barWidth - barPadding)  
    .attr("transform", function (d, i) {  
         var translate = [barWidth * i, 0];  
         return "translate("+ translate +")";  
    });

```

#### selectAll()

La première chose que nous faisons peut sembler un peu étrange, nous faisons `.selectAll("rect")`, cependant, nous n'avons pas encore créé d'éléments `<rect>`. Donc cette méthode retourne une sélection vide (un tableau vide). Cependant, nous allons bientôt créer des éléments `<rect>` en utilisant `enter().append()`.

Cela peut sembler un peu confus. Mais expliquer comment `selectAll()` fonctionne en combinaison avec `enter().append()` est hors du cadre de ce tutoriel. Si vous voulez comprendre cela correctement, lisez [cet article](http://knowledgestockpile.blogspot.no/2012/01/understanding-selectall-data-enter.html) très attentivement.

#### data()

Nous enchaînons ensuite la méthode `data()` et passons notre jeu de données. Les données finiront par dicter la hauteur de chaque barre.

#### enter()

L'étape suivante consiste à enchaîner la méthode `enter()`. La méthode `enter()` examine à la fois le jeu de données que vous avez passé à `data()` **et** la sélection que nous avons faite avec `selectAll('rect')`, puis elle essaie de trouver des "correspondances". Elle crée ainsi une correspondance entre vos données et le DOM.

Mais souvenez-vous, la méthode `selectAll('rect')` a retourné une sélection **vide**, car il n'y a pas encore d'éléments `<rect>` dans le DOM. Cependant, le jeu de données contient neuf éléments. Il n'y a donc pas de "correspondances".

La méthode `enter()` vous permet ensuite de créer un nouvel élément `<rect>` dans le DOM pour chaque élément du jeu de données qui n'a pas encore d'élément `<rect>` correspondant.

#### append()

À la ligne suivante, nous ajoutons un élément `<rect>` pour chacun des éléments. Comme cette méthode suit `enter()`, elle sera en fait exécutée neuf fois, une pour chaque point de données qui manque d'un `<rect>` correspondant dans le DOM.

#### attr()

L'étape suivante consiste à décider de la forme de chacun des rectangles (nos barres). Nous devons lui donner quatre attributs : **hauteur, largeur, position x** et **position y**. Nous utiliserons la méthode `attr()` pour tous ceux-ci.

Commençons par la position y :

```js
.attr("y", function(d) {  
    return svgHeight - d  
})

```

Le premier paramètre dicte quel attribut nous voulons ajouter : dans ce cas, la coordonnée y de la barre. Dans le second, nous avons accès à une fonction de rappel dans laquelle nous allons retourner la valeur que nous voulons que notre attribut ait.

Ici, nous avons accès au point de données à cette étape du processus d'itération (souvenez-vous, cette méthode est invoquée une fois par élément dans le tableau `dataset`). Le point de données est stocké dans l'argument `d`. Nous allons ensuite soustraire le point de données donné, `d`, de la hauteur de notre conteneur SVG.

Les coordonnées X et Y sont toujours calculées à partir du coin supérieur gauche. Donc lorsque nous soustrayons la hauteur du conteneur avec la valeur `d`, nous obtenons la coordonnée y pour le haut de la barre.

Pour que la barre s'étire de ce point vers le bas jusqu'au bas du conteneur SVG, nous devons lui donner une hauteur équivalente à la valeur du point de données :

```js
.attr("height", function(d) {  
    return d;  
})

```

L'étape suivante consiste à lui donner une largeur :

.attr("width", barWidth - barPadding)

Ici, nous passons simplement une expression simple plutôt qu'une fonction de rappel, car nous n'avons pas besoin d'accéder au point de données. Nous prenons simplement comme base la variable `barWidth` que nous avons créée plus haut, qui est la largeur totale du conteneur divisée par le nombre de barres. Afin d'obtenir un petit espace entre chacune des barres, nous allons également soustraire le padding, que nous avons défini comme 5.

La dernière étape consiste à définir les coordonnées x. Cette expression est un peu plus complexe :

```js
.attr("transform", function (d, i) {  
    var xCoordinate = barWidth * i;  
    return "translate("+ xCoordinate +")";  
});

```

Ici, nous profitons tout d'abord d'un deuxième paramètre dans le rappel, `i`. Il s'agit de l'index de l'élément donné dans le tableau.

Pour définir la coordonnée de chacune des barres, nous allons simplement multiplier l'index par la variable `barWidth`. Nous allons ensuite retourner une valeur de chaîne qui décrit la transformation pour l'axe des x, par exemple `"translate(100)"`. Cela pousserait la barre de 100 pixels vers la droite.

Et voilà, vous avez votre tout premier graphique à barres en D3.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4gyftwYFlIenlKtILaiqbw.png)

Si vous êtes intéressé à en apprendre davantage sur D3.js, assurez-vous de [consulter notre cours gratuit sur Scrimba](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_bar_chart_article).

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gd3js_bar_chart_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gd3js_bar_chart_article)_