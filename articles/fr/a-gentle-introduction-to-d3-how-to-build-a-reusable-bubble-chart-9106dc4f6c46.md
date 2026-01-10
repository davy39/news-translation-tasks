---
title: 'Une introduction en douceur à D3 : comment construire un graphique à bulles
  réutilisable'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-11T19:20:44.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ywul1VdNkWbdFz3x5iVYCA.jpeg
tags:
- name: D3
  slug: d3
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: 'Une introduction en douceur à D3 : comment construire un graphique à bulles
  réutilisable'
seo_desc: 'By Déborah Mesquita

  Getting Started with D3


  When I started to learn D3, nothing made sense to me. Things only became more clear
  when I started to learn about reusable charts.

  In this article, I’ll show you how to create a reusable bubble chart and g...'
---

Par Débora Mesquita

#### Introduction à D3

![Image](https://cdn-media-1.freecodecamp.org/images/b1f4Gb2hEkCUMp9X0hyUcsXKVAMuRPFHYuvk)

Lorsque j'ai commencé à apprendre D3, rien n'avait de sens pour moi. Les choses ne sont devenues plus claires que lorsque j'ai commencé à apprendre les graphiques réutilisables.

Dans cet article, je vais vous montrer comment créer un graphique à bulles réutilisable et vous donner une introduction en douceur à D3. Le jeu de données que nous allons utiliser est composé de [stories publiées sur freeCodeCamp en janvier 2017](https://github.com/dmesquita/reusable_bubble_chart/blob/master/medium_january.csv).

![Image](https://cdn-media-1.freecodecamp.org/images/ST0umvE7-OejTYSovrDQQZQzVPbXqKGhtUnL)
_C'est le graphique que vous allez construire_

### À propos de D3

[D3](https://d3js.org/) est une bibliothèque JavaScript pour la visualisation de données. Elle donne vie aux données en utilisant HTML, SVG et CSS.

Nous avons souvent besoin de réutiliser un graphique dans un autre projet, ou même de partager le graphique avec d'autres. Pour cela, Mike Bostock (le créateur de D3) a proposé un modèle appelé [reusable charts](https://bost.ocks.org/mike/chart/). Nous allons utiliser son approche avec quelques petites modifications, comme présenté par Pablo Navarro Castillo dans le livre [Mastering D3.js](http://pnavarrc.github.io/book/).

Nous utilisons ici la version **4.6.0** de D3.

### ? Graphiques réutilisables

Les graphiques suivant le modèle de graphique réutilisable ont deux caractéristiques :

* **Configurabilité.** Nous voulons modifier l'apparence et le comportement du graphique sans avoir à modifier le code lui-même.
* **Capacité à être construit de manière indépendante.** Nous voulons que chaque élément du graphique associé à un point de données de notre jeu de données soit indépendant. Cela a à voir avec la manière dont D3 associe les instances de données aux éléments du DOM. Cela deviendra plus clair dans un instant.

> « En résumé : implémentez les graphiques comme des **closures avec des méthodes getter-setter. » —** [Mike Bostock](https://bost.ocks.org/mike/chart/)

### Le graphique à bulles

Vous devez d'abord définir quels éléments du graphique peuvent être personnalisés :

* La taille du graphique
* Le jeu de données d'entrée

#### Définir la taille du graphique

Commençons par créer une fonction pour encapsuler toutes les variables du graphique et définir les valeurs par défaut. Cette structure est appelée une closure.

```
// bubble_graph.js
```

```
var bubbleChart = function () {    var width = 600,    height = 400;    function chart(selection){        // vous allez arriver ici    }    return chart;}
```

Vous voulez créer des graphiques de différentes tailles sans avoir à changer le code. Pour cela, vous allez créer des graphiques comme suit :

```
// bubble_graph.html
```

```
var chart = bubbleChart().width(300).height(200);
```

Pour cela, vous allez maintenant définir des accesseurs pour les variables de largeur et de hauteur.

```
// bubble_graph.js
```

```
var bubbleChart = function () {    var width = 600    height = 400;
```

```
    function chart(selection){        // nous allons arriver ici    }    chart.width = function(value) {        if (!arguments.length) { return width; }        width = value;        return chart;    }
```

```
    chart.height = function(value) {        if (!arguments.length) { return height; }        height = value;        return chart;    }    return chart;}
```

Si vous appelez `bubbleChart()` (sans attributs de largeur ou de hauteur), le graphique est créé avec les valeurs de largeur et de hauteur par défaut que vous avez définies à l'intérieur de la closure. Si appelé sans arguments, la méthode retourne la valeur de la variable.

```
// bubble_graph.html
```

```
var chart = bubbleChart();bubbleChart().width(); // retourne 600
```

Vous vous demandez peut-être pourquoi les méthodes retournent la fonction chart. Il s'agit d'un modèle JavaScript utilisé pour simplifier le code. Cela s'appelle le chaînage de méthodes. Avec ce modèle, vous pouvez créer de nouveaux objets comme ceci :

```
// bubble_graph.html
```

```
var chart = bubbleChart().width(600).height(400);
```

au lieu de :

```
// bubble_graph.html
```

```
var chart = bubbleChart(); chart.setWidth(600); chart.setHeight(400);
```

#### Joindre les données à notre graphique

Maintenant, apprenons à joindre les données aux éléments du graphique. Voici comment le graphique est structuré : la div avec le graphique a un élément SVG, et chaque point de données correspond à un cercle dans le graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/KDQtSripZjkfZlWAGwt1RMOhoOEtuZy6BvbV)

```
// bubble_graph.html, après l'appel de la fonction bubbleChart()
```

```
<svg width="600" height="400">;    <circle></circle> // une histoire des données    <circle></circle> // une autre histoire des données    ...</svg>
```

#### ? d3.data()

La fonction `d3.selection.**data**([data[,key]])` retourne une nouvelle sélection qui représente un élément lié avec succès aux données. Pour cela, vous devez d'abord charger les données à partir du fichier .csv. Vous allez utiliser la fonction `d3.**csv**(_url_[[, _row_], _callback_])`.

```
// bubble_graph.html
```

```
d3.csv('file.csv', function(error, our_data) {    var data = our_data; // ici vous pouvez faire ce que vous voulez avec les données}
```

```
// medium_january.csv|                title                 |   category   | hearts ||--------------------------------------|--------------|--------|| Nobody wants to use software         | Development  |  2700  |  | Lossless Web Navigation with Trails  |    Design    |  688   |   | The Rise of the Data Engineer        | Data Science |  862   |
```

#### ? d3-selection

Vous allez utiliser les fonctions **d3-select()** et **data()** pour passer nos données au graphique.

> Les sélections permettent une transformation puissante des données du document object model (DOM) : définir les [attributs](https://github.com/d3/d3-selection/blob/master/README.md#selection_attr), [styles](https://github.com/d3/d3-selection/blob/master/README.md#selection_style), [propriétés](https://github.com/d3/d3-selection/blob/master/README.md#selection_property), le contenu [HTML](https://github.com/d3/d3-selection/blob/master/README.md#selection_html) ou [texte](https://github.com/d3/d3-selection/blob/master/README.md#selection_text), et plus encore. — [Documentation D3](https://github.com/d3/d3-selection/)

```
// bubble_graph.html
```

```
<div class="chart-example" id="chart"><svg></svg></div>
```

```
d3.csv('medium_january.csv', function(error, our_data) {    if (error) {        console.error('Erreur lors de la récupération ou de l'analyse des données.');        throw error;    }
```

```
    var chart = bubbleChart().width(600).height(400);    d3.select('#chart').data(our_data).call(chart);
```

```
 });
```

Un autre sélecteur important est **d3.selectAll()**. Supposons que vous avez la structure suivante :

```
<body>    <div></div>    <div></div>    <div></div></body>
```

`d3.select("body").selectAll("div")` sélectionne toutes ces divs pour nous.

#### ?? d3.enter()

Et maintenant, vous allez apprendre une fonction importante de D3 : **d3.enter()**. Supposons que vous avez une balise body vide et un tableau avec des données. Vous voulez parcourir chaque élément du tableau et créer une nouvelle div pour chaque élément. Vous pouvez faire cela avec le code suivant :

```
<!-- avant --><body> // vide</body>
```

```
----// script js
```

```
var our_data = [1, 2, 3]var div = d3.select("body") .selectAll("div") .data(our_data) .enter() .append("div");---
```

```
<!-- après --><body>    <div></div>    <div></div>    <div></div></body>
```

Pourquoi avez-vous besoin de `selectAll("div")` si les divs n'existent même pas encore ? Parce qu'en D3, au lieu de dire **comment** faire quelque chose, nous disons **ce que** nous voulons.

Dans ce cas, vous voulez associer chaque div à un élément du tableau. C'est ce que vous dites avec le `selectAll("div")`.

```
var div = d3.select("body") .selectAll("div") // ici vous dites 'hey d3, chaque élément de données      du tableau qui suit sera lié à une div' .data(our_data) .enter().append("div");
```

La fonction `enter()` retourne la sélection avec les données liées à l'élément du tableau. Vous ajoutez ensuite cette sélection au DOM avec le `.append("div")`.

#### ? d3.forceSimulation()

Vous avez besoin de quelque chose pour simuler la physique des cercles. Pour cela, vous allez utiliser `d3.forceSimulation([nodes])`. Vous devez également indiquer quel type de force changera la position ou la vitesse des nœuds.

Dans notre cas, nous allons utiliser `d3.forceManyBody()`.

```
// bubble_chart.js
```

```
var simulation = d3.forceSimulation(data) .force("charge", d3.forceManyBody().strength([-50])) .force("x", d3.forceX()) .force("y", d3.forceY()) .on("tick", ticked);
```

Une valeur de force positive fait que les nœuds s'attirent les uns les autres, tandis qu'une valeur de force négative fait qu'ils se repoussent.

![Image](https://cdn-media-1.freecodecamp.org/images/wMJSa903Hk1t5odK27XEEl0vhpYS8eq6odq5)
_L'effet strength()_

Nous ne voulons pas que les nœuds se répandent dans tout l'espace SVG, alors nous utilisons `d3.forceX(0)` et `d3.forceY(0)`. Cela "tire" les cercles vers la position 0. Allez-y et essayez de supprimer cela du code pour voir ce qui se passe.

Lorsque vous actualisez la page, vous pouvez voir que les cercles s'ajustent jusqu'à ce qu'ils se stabilisent enfin. La fonction `ticked()` met à jour les positions des cercles. La fonction `d3.forceManyBody()` continue de mettre à jour les positions x et y de chaque nœud, et la fonction `ticked()` met à jour le DOM avec ces valeurs (les attributs cx et cy).

```
// bubble_graph.js
```

```
function ticked(e) {    node.attr("cx", function(d) { return d.x; })        .attr("cy", function(d) { return d.y; });    // 'node' est chaque cercle du graphique à bulles
```

```
 }
```

Voici le code avec tout ensemble :

```
var simulation = d3.forceSimulation(data)     .force("charge", d3.forceManyBody().strength([-50]))     .force("x", d3.forceX())     .force("y", d3.forceY())     .on("tick", ticked); 
```

```
function ticked(e) {     node.attr("cx", function(d) { return d.x; })         .attr("cy", function(d) { return d.y; }); }
```

En résumé, toute cette simulation donne à chaque cercle une position x et y.

#### ? d3.scales

Voici la partie la plus excitante : l'ajout des cercles. Vous vous souvenez de la fonction **enter()** ? Vous allez l'utiliser maintenant. Dans notre graphique, le rayon de chaque cercle est proportionnel au nombre de recommandations de chaque histoire. Pour cela, vous allez utiliser une échelle linéaire : **d3.scaleLinear()**

Pour utiliser les échelles, vous devez définir deux choses :

* **Domaine** : les valeurs minimale et maximale des données d'entrée (dans notre cas, le nombre minimal et maximal de recommandations). Pour obtenir les valeurs minimale et maximale, vous allez utiliser les fonctions **d3.min()** et **d3.max()**.
* **Plage** : les valeurs minimale et maximale de sortie de l'échelle. Dans notre cas, nous voulons que le plus petit rayon soit de taille 5 et le plus grand rayon de taille 18.

```
// bubble_graph.js
```

```
var scaleRadius = d3.scaleLinear()            .domain([d3.min(data, function(d) { return +d.views; }),                     d3.max(data, function(d) { return +d.views; })])            .range([5,18]);
```

Et puis vous créez enfin les cercles :

```
// bubble_graph.js
```

```
var node = svg.selectAll("circle")   .data(data)   .enter()   .append("circle")   .attr('r', function(d) { return scaleRadius(d.views)})});
```

Pour colorer les cercles, vous allez utiliser une échelle catégorielle : **d3.scaleOrdinal()**. Cette échelle retourne des valeurs discrètes.

Notre jeu de données a 3 catégories : Design, Development et Data Science. Vous allez mapper chacune de ces catégories à une couleur. `d3.schemeCategory10` nous donne une liste de 10 couleurs, ce qui est suffisant pour nous.

```
// bubble_graph.js
```

```
var colorCircles = d3.scaleOrdinal(d3.schemeCategory10);var node = svg.selectAll("circle")    .data(data)    .enter()    .append("circle")    .attr('r', function(d) { return scaleRadius(d.views)})    .style("fill", function(d) { return colorCircles(d.category)});
```

Vous voulez que les cercles soient dessinés au milieu du SVG, alors vous allez déplacer chaque cercle vers le milieu (la moitié de la largeur et la moitié de la hauteur). Allez-y et supprimez cela du code pour voir ce qui se passe.

```
// bubble_graph.js
```

```
var node = svg.selectAll("circle") .data(data) .enter() .append("circle") .attr('r', function(d) { return scaleRadius(d.views)}) .style("fill", function(d) {return colorCircles(d.category)}) .attr('transform', 'translate(' + [width / 2, height / 2] + ')');
```

Maintenant, vous allez ajouter des infobulles au graphique. Elles doivent apparaître chaque fois que nous plaçons la souris sur les cercles.

```
var tooltip = selection .append("div") .style("position", "absolute") .style("visibility", "hidden") .style("color", "white") .style("padding", "8px") .style("background-color", "#626D71") .style("border-radius", "6px") .style("text-align", "center") .style("font-family", "monospace") .style("width", "400px") .text("");
```

```
var node = svg.selectAll("circle") .data(data) .enter() .append("circle") .attr('r', function(d) { return scaleRadius(d.views)}) .style("fill", function(d) {return colorCircles(d.category)}) .attr('transform', 'translate(' + [width / 2, height / 2] + ')') .on("mouseover", function(d){     tooltip.html(d.category +"<br>"+ d.title+"<br>"+d.views);      return tooltip.style("visibility", "visible");}) .on("mousemove", function(){   return tooltip.style("top", (d3.event.pageY-       10)+"px").style("left",(d3.event.pageX+10)+"px");}) .on("mouseout", function(){return tooltip.style("visibility", "hidden");});
```

Le `mousemove` suit le curseur lorsque la souris bouge. `d3.event.pageX` et `d3.event.pageY` retournent les coordonnées de la souris.

Et c'est tout ! Vous pouvez voir le code final [ici](https://github.com/dmesquita/reusable_bubble_chart).

Vous pouvez jouer avec le graphique à bulles [ici](https://bl.ocks.org/dmesquita/37d8efdb3d854db8469af4679b8f984a).

Avez-vous trouvé cet article utile ? Je fais de mon mieux pour écrire un article approfondi chaque mois, vous pouvez [recevoir un email lorsque j'en publie un nouveau](https://goo.gl/forms/SLrJDrGtxgAoILkt1).

Des questions ou des suggestions ? Laissez-les dans les commentaires. Merci d'avoir lu ! 😊

_Merci spécial à [John Carmichael](https://www.freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46/undefined) et [Alexandre Cisneiros](https://www.freecodecamp.org/news/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46/undefined)._