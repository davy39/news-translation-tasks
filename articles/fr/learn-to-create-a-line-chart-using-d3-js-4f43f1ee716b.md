---
title: Apprendre à créer un graphique en ligne avec D3.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T03:17:56.000Z'
originalURL: https://freecodecamp.org/news/learn-to-create-a-line-chart-using-d3-js-4f43f1ee716b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x-3p2C-nd9_RbXOZG0Dx0A.png
tags:
- name: D3.js
  slug: d3js
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre à créer un graphique en ligne avec D3.js
seo_desc: 'By Sohaib Nehal

  Use the power of D3.js to draw beautiful representations of your data.


  Learn D3.js for free on Scrimba

  D3.js is an open source JavaScript library used to create beautiful data representations
  which we can view in any modern browser. ...'
---

Par Sohaib Nehal

#### Utilisez la puissance de D3.js pour dessiner de belles représentations de vos données.

![Image](https://cdn-media-1.freecodecamp.org/images/EUZuijdvOc8orJ9PUi3raR9Lm0LktF18luAT)
_Apprenez D3.js gratuitement sur Scrimba_

D3.js est une bibliothèque JavaScript open source utilisée pour créer de belles représentations de données que nous pouvons visualiser dans n'importe quel navigateur moderne. En utilisant D3.js, nous pouvons créer divers types de graphiques et de diagrammes à partir de nos données.

Dans ce tutoriel, nous allons créer un graphique en ligne affichant l'indice des prix du Bitcoin des six derniers mois. Nous allons récupérer des données depuis une API externe et rendre un graphique en ligne avec des labels et un axe à l'intérieur du DOM.

**Nous avons également créé un cours gratuit sur D3.js sur Scrimba. [Découvrez-le ici.](https://scrimba.com/g/gd3js)**

#### Installation

Tout d'abord, nous allons importer la bibliothèque D3.js directement depuis le CDN à l'intérieur de notre HTML.

```
<html>  <head>    <link rel="stylesheet" href="index.css">  </head>  <body>    <svg></svg>    <script src="https://d3js.org/d3.v4.min.js"></script>  </body></html>
```

Nous avons également ajouté une balise `<svg>`</svg> à l'intérieur de notre HTML pour créer le graphique en ligne à l'intérieur de celle-ci en utilisant D3.js

Passons maintenant à l'écriture de notre code JavaScript. Tout d'abord, nous voulons charger nos données de l'indice des prix du Bitcoin depuis une API externe une fois que le DOM a été chargé.

#### **Récupérer les données**

```
var api = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-31&end=2018-04-01';
```

```
document.addEventListener("DOMContentLoaded", function(event) {   fetch(api)     .then(function(response) { return response.json(); })     .then(function(data) {          //FAIRE QUELQUE CHOSE AVEC LES DONNÉES       })});
```

Dans le code ci-dessus, nous utilisons la méthode `fetch` pour obtenir les données depuis une API externe. Nous les analysons ensuite en utilisant la méthode `.json()`.

Nous voulons maintenant convertir ces données en paires clé/valeur afin qu'elles soient au format `date:prix`. Pour cela, nous allons envoyer nos données à une autre fonction qui les analysera et les retournera dans le format souhaité.

#### **Analyser les données**

```
.....then(function(data) {          var parsedData = parseData(data) })
```

```
function parseData(data) {   var arr = [];   for (var i in data.bpi) {      arr.push(         {            date: new Date(i), //date            value: +data.bpi[i] //convertir la chaîne en nombre         });   }   return arr;}
```

Nous passons nos données à une fonction `parseData` qui retourne un autre tableau d'objets. Chaque objet contient une date et le prix du bitcoin à cette date particulière.

Une fois que nous avons les données dans le format requis, nous allons envoyer ces données à la fonction `drawChart` dans laquelle tout le code restant sera écrit en utilisant D3.js pour rendre le graphique en ligne.

```
.....then(function(data) {    var parsedData = parseData(data);   drawChart(parsedData);})
```

#### Sélectionner l'élément SVG

Dans la fonction `drawChart`, nous sélectionnons d'abord notre élément SVG et lui fournissons un peu de style.

```
function drawChart(data) {
```

```
   var svgWidth = 600, svgHeight = 400;   var margin = { top: 20, right: 20, bottom: 30, left: 50 };   var width = svgWidth - margin.left - margin.right;   var height = svgHeight - margin.top - margin.bottom;
```

```
   var svg = d3.select('svg')     .attr("width", svgWidth)     .attr("height", svgHeight);...
```

Dans le code ci-dessus, nous définissons la largeur et la hauteur du conteneur SVG en le sélectionnant d'abord avec la méthode `select()` puis en utilisant la méthode `attr()` pour assigner les attributs.

Nous avons également défini des marges et utilisons leurs valeurs pour calculer les attributs de largeur et de hauteur du conteneur SVG. Ces valeurs de marge nous aideront plus tard à positionner et afficher correctement notre graphique.

En utilisant CSS, nous avons donné des bordures à notre conteneur SVG :

```
<style>    .line-chart    {        border: 1px solid lightgray;    }</style>
```

Jusqu'à présent, nous n'avons rien à l'intérieur de notre DOM :

![Image](https://cdn-media-1.freecodecamp.org/images/amoiuppE703baUzbP-qvjHoeM8I0S4HgucSw)

Ensuite, nous allons créer un élément de groupe pour contenir notre graphique en ligne, l'axe et les labels.

#### **Créer et transformer l'élément de groupe**

```
...var g = svg.append("g")   .attr("transform",       "translate(" + margin.left + "," + margin.top + ")"   );
```

Le regroupement des éléments aide à organiser des éléments similaires ou liés ensemble. Ici, après avoir rendu un élément de groupe, nous lui fournissons une transformation.

D3 nous donne diverses options pour transformer nos éléments. Dans le code ci-dessus, nous utilisons la propriété `translate` pour repositionner notre élément de groupe avec des marges sur sa gauche et son haut.

#### **Ajouter des échelles**

Maintenant, nous voulons ajouter des échelles à notre graphique.

```
var x = d3.scaleTime().rangeRound([0, width]);
```

```
var y = d3.scaleLinear().rangeRound([height, 0]);
```

Comme nous le savons, nos données se composent de dates et de la valeur du Bitcoin à ces dates. Par conséquent, nous pouvons supposer que l'axe des x contiendra les dates et l'axe des y contiendra les valeurs. C'est ainsi que nous pouvons voir la variation dans le graphique en ligne par rapport au temps.

Et donc, dans l'extrait de code ci-dessus, nous avons créé une échelle de type temps sur l'axe des x et de type linéaire sur l'axe des y. Nous fournissons également à ces échelles les plages selon la largeur et la hauteur de notre conteneur SVG.

#### Créer une ligne

Passons maintenant à la définition de notre ligne en utilisant la méthode `d3.line`. Nous allons définir les attributs x et y de la ligne en passant des fonctions anonymes et en retournant l'objet date et la valeur du bitcoin pour ce jour particulier.

```
var line = d3.line()   .x(function(d) { return x(d.date)})   .y(function(d) { return y(d.value)})   x.domain(d3.extent(data, function(d) { return d.date }));   y.domain(d3.extent(data, function(d) { return d.value }));
```

#### Ajouter des axes

Nous allons maintenant ajouter nos axes gauche et inférieur à l'intérieur de notre élément de groupe pour le graphique en ligne. L'axe de gauche représentera la valeur du bitcoin tandis que l'axe du bas affichera la date correspondante.

```
g.append("g")   .attr("transform", "translate(0," + height + ")")   .call(d3.axisBottom(x))   .select(".domain")   .remove();
```

Dans le code ci-dessus, nous ajoutons un élément de groupe à l'intérieur de notre groupe principal et le translatons tout en bas de notre conteneur. Ensuite, nous passons la méthode `d3.axisBottom` dans la fonction call où `d3.axisBottom` prend le paramètre de `x` qui est défini dans la section **Ajouter des échelles**.

```
g.append("g")   .call(d3.axisLeft(y))   .append("text")   .attr("fill", "#000")   .attr("transform", "rotate(-90)")   .attr("y", 6)   .attr("dy", "0.71em")   .attr("text-anchor", "end")   .text("Prix ($)");
```

Similaire à l'axe du bas, nous ajoutons un autre élément de groupe et appelons ensuite la méthode `d3.axisLeft` qui prend le paramètre de `y`. Ensuite, nous stylisons également notre axe en lui assignant différents attributs et une étiquette.

Si nous sauvegardons et actualisons la page, nous pouvons voir nos axes rendus à l'intérieur du DOM :

![Image](https://cdn-media-1.freecodecamp.org/images/Os96ExJTGVVQuHqS-q3zqToG-pfBg5CztO6H)
_Axes gauche et inférieur_

#### Ajouter un chemin

Dans la dernière étape, nous allons ajouter un chemin à l'intérieur de notre élément de groupe principal. Ce chemin dessinerait en fait le graphique en ligne selon les valeurs des données.

Nous passons notre ensemble de données en utilisant la méthode `datum` puis définissons les attributs de couleur de remplissage, de couleur de trait et de largeur. À la fin, nous définissons l'attribut de `d` qui donne en fait des instructions au chemin SVG sur l'endroit où connecter les points du chemin.

```
g.append("path").datum(data).attr("fill", "none").attr("stroke", "steelblue").attr("stroke-linejoin", "round").attr("stroke-linecap", "round").attr("stroke-width", 1.5).attr("d", line);
```

Voici le résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/I0yynRDidWlR6HOGbpdSs2aMS6cZJfUNysNt)
_Graphique en ligne_

#### Conclusion

Félicitations ! Nous avons réussi à créer le graphique en ligne en utilisant D3.js. Vous pouvez consulter la documentation officielle de [D3.js](https://github.com/d3/d3/wiki) pour en savoir plus sur les différents graphiques et diagrammes que vous pouvez créer.

Si vous êtes intéressé à en apprendre davantage sur D3.js, assurez-vous de [consulter notre cours gratuit sur Scrimba.](https://scrimba.com/g/gd3js)

_Je suis Sohaib Nehal. Je suis un développeur d'applications web Full-Stack. Vous pouvez me joindre à sohaib.nehal@ymail.com ou sur Twitter @Sohaib_Nehal. Merci :-)_