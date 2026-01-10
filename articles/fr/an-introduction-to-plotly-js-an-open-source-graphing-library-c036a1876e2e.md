---
title: Une introduction à plotly.js — une bibliothèque open source de graphiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-01T14:18:22.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-plotly-js-an-open-source-graphing-library-c036a1876e2e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mTCZLjLHGCC6GDIB
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
seo_title: Une introduction à plotly.js — une bibliothèque open source de graphiques
seo_desc: 'By Praveen Dubey

  Plotly.js is a library ideally suited for JavaScript applications which make use
  of graphs and charts. There are a few reasons to consider using it for your next
  data visualization project:


  Plotly.js uses both D3.js (SVG) and WebGL ...'
---

Par Praveen Dubey

[Plotly.js](https://plot.ly/javascript/) est une bibliothèque idéale pour les applications JavaScript qui utilisent des graphiques et des diagrammes. Voici quelques raisons d'envisager de l'utiliser pour votre prochain projet de visualisation de données :

1. Plotly.js utilise à la fois D3.js (SVG) et WebGL pour le rendu graphique
2. Plotly.js est un « bundle tout-en-un » avec les modules d3.js et stack.gl
3. Il fonctionne avec le schéma JSON
4. Plotly.js prend en charge les graphiques de base, statistiques, scientifiques, financiers et cartographiques.

De plus, plus de 9000 étoiles sur son dépôt open source [Github](https://github.com/plotly/plotly.js/) est un fort indicateur de sa croissance communautaire.

![Image](https://cdn-media-1.freecodecamp.org/images/ArP420b0zklSCgGCTzeyKvaYoY2w7Gprg2cl)

### Utilisation et exemples

Examinons l'installation et quelques exemples pour une meilleure compréhension pratique.

Tout d'abord, incluez le fichier depuis son CDN.

```
<head><!-- Inclure Plotly.js --><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>
```

Ensuite, traçons un petit graphique qui montre les nombres et leurs carrés :

![Image](https://cdn-media-1.freecodecamp.org/images/8-4CeZ8PRoQlphhbuB4YsSNgIiFSAydCc95p)

Le code pour générer ce graphique est ci-dessous :

```
<head>   <!-- Inclure Plotly.js -->   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>
```

```
<body>  <div id="myDiv">      <!-- Le graphique Plotly sera dessiné à l'intérieur de cette DIV -->  </div>
```

```
<script>    var trace = {        x: [1, 2, 3, 4, 5, 6, 7, 8],        y: [1, 4, 9, 16, 25, 36, 49, 64],        mode: 'line'    };
```

```
var data = [ trace ];   Plotly.newPlot('myDiv', data);
```

```
</script></body>
```

La configuration de base peut être faite avec une inclusion de fichier, un élément DOM et un script pour le traçage.

Après l'inclusion de la bibliothèque Plotly.js dans `<head>`, nous avons défini une `<div>` vide pour tracer le graphique.

`Plotly.new()` dessine un nouveau graphique dans l'élément `<div>`, écrasant tout graphique existant, et dans ce cas, nous avons utilisé `myDiv`. L'entrée sera un élément `<div>` et des données.

Remarquez l'inclusion de `mode` dans la variable trace. Il peut s'agir de n'importe quelle combinaison de `"lines"`, `"markers"`, `"text"` joints avec un `"+"` OU `"none"`.

Les exemples incluent `"lines"`, `"markers"`, `"lines+markers"`, `"lines+markers+text"`, `"none"`.

Ici, nous avons utilisé `markers`. Remarquez que vous n'obtenez que des points marqués dans les coordonnées du graphique et ne voyez pas la ligne connectée à travers tous les points.

![Image](https://cdn-media-1.freecodecamp.org/images/skE3C2oFFvsWkp5D5QvTIV70X-s1EaymGKqT)

Tracez maintenant plusieurs lignes simplement en ajoutant des valeurs à la variable `data` :

```
<head>   <!-- Inclure Plotly.js -->   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>  <div id="myDiv">  <!-- Le graphique Plotly sera dessiné à l'intérieur de cette DIV --></div>  <script>    var trace1 = {        x: [1, 2, 3, 4],        y: [10, 15, 13, 17],        mode: 'lines',        type: 'scatter'      };
```

```
var trace2 = {        x: [2, 3, 4, 5],        y: [16, 5, 11, 9],        mode: 'marker',        type: 'scatter'      };
```

```
var trace3 = {        x: [1, 2, 3, 4],        y: [12, 9, 15, 12],        mode: 'lines+markers',        type: 'scatter'      };
```

```
var data = [trace1, trace2, trace3];
```

```
Plotly.newPlot('myDiv', data);  </script></body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/BNEF4V1CZUdARRqq7GB-aY6YADM6sfvu9Vmk)

La légende d'un graphique est liée aux données affichées graphiquement dans la zone de traçage du graphique.

Pour l'instant, nous n'avons aucune étiquette, et la légende ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1-mwt2h2WtfUAD4Ypmnq2FH2a19mKuuHOZj6)

Mettons-les à jour en utilisant des options telles que `text`, `textfont`, `textposition` pour la personnalisation de nos étiquettes de données. Celles-ci doivent être passées avec chaque ensemble de données.

```
<head>   <!-- Inclure Plotly.js -->   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>
```

```
<body>  <div id="myDiv"><!-- Le graphique Plotly sera dessiné à l'intérieur de cette DIV --></div>  <script>    var trace1 = {          x: [1, 2, 3, 4, 5],          y: [100, 60, 30, 60, 10],          mode: 'lines+markers+text',          type: 'scatter',          name: 'Beta',          text: ['Mobile A', 'Mobile B', 'Mobile C', 'Mobile D', 'Mobile E'],          textposition: 'top center',          textfont: {          family:  'Raleway, sans-serif'        },        marker: { size: 12 }      };
```

```
var trace2 = {        x: [1.5, 2.5, 3.5, 4.5, 5.5],        y: [100, 10, 70, 150, 40],        mode: 'lines+markers+text',        type: 'scatter',        name: 'Alpha',        text: ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],        textfont : {          family:'Times New Roman'        },        textposition: 'bottom center',        marker: { size: 12 }      };
```

```
var data = [ trace1, trace2 ];
```

```
var layout = {        xaxis: {          range: [ 0.75, 5.25 ]        },        yaxis: {          range: [0, 200]        },        legend: {          y: 0.5,          yref: 'paper',          font: {            family: 'Arial, sans-serif',            size: 20,            color: 'black',          }        },        title:'Data Labels on the Plot'      };
```

```
Plotly.newPlot('myDiv', data, layout);  </script></body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/yQhTyjFJODkEToXG0hSK0jXn-eZCHw6ahMQR)

La disposition des autres attributs visuels tels que le titre et les annotations sera définie dans un objet généralement appelé `layout`.

Jusqu'à présent, nous avons vu quelques exemples de lignes, traçons rapidement un graphique à barres en utilisant `'bar'` comme type.

```
var data = [{  x: ['Company X', 'Company Y', 'Company Z'],  y: [200, 140, 230],  type: 'bar'}];
```

```
Plotly.newPlot('myDiv', data);
```

![Image](https://cdn-media-1.freecodecamp.org/images/j3DWpaP1s82rWL3D8asq9sTIb8J8hWOBmfDx)

Vous pouvez également changer le `type` dans les données montrées ci-dessus pour les produits et les mobiles en changeant `scatter` en `bar`.

```
var trace = {        x: [1.5, 2.5, 3.5, 4.5, 5.5],        y: [100, 10, 70, 150, 40],        mode: 'lines+markers+text',        type: 'bar',        name: 'Alpha',        text: ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],        textfont : {          family:'Times New Roman'        },        textposition: 'top',        marker: { size: 12 }      };
```

Voici un exemple qui change l'opacité de la barre :

```
var trace2 = {          x: ['Alpha', 'Beta', 'Gamma'],          y: [100, 200, 500],          type: 'bar',          name: 'Opacity Example',          marker: {            color: 'rgb(204,204,204)',            opacity: 0.5          }};
```

![Image](https://cdn-media-1.freecodecamp.org/images/0JPQtSoN1U2J064PhuXtYWF1vn8oS-QSCNS8)

Nous avons créé quelques graphiques de dispersion de base et parlé de quelques options qui peuvent être facilement ajustées pour obtenir différentes variations du même graphique.

Continuons en traçant un ensemble de données de météorites en utilisant seulement quelques lignes de code.

J'utilise un ensemble de données provenant du [github de bcdunbar](https://raw.githubusercontent.com/bcdunbar/datasets/master/meteorites_subset.csv) et vais essayer de décomposer tout le processus en plusieurs étapes.

Commençons.

#### Étape 1. Configuration initiale

Ajoutez plotly.js dans votre fichier HTML. Cela inclut le fichier JavaScript, l'élément `div` vide et l'espace réservé pour les scripts.

```
<html><head>  <!-- Inclure le fichier Plotly.js depuis le CDN -->  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body><!-- La DIV sera utilisée pour les graphiques --><div id="mapDiv"></div>  <script>  // Code JS pour le graphique  </script></div></body></html>
```

#### Étape 2. Ensemble de données

Puisque notre ensemble de données est au format CSV, nous pouvons utiliser `Plotly.d3.csv`. Il lit interne les données CSV à partir d'un appel AJAX.

Code wrapper pour le traçage :

```
Plotly.d3.csv('https://raw.githubusercontent.com/bcdunbar/datasets/master/meteorites_subset.csv', function(err, rows){
```

```
Plotly.plot('mapDiv', data, layout);
```

```
});
```

#### Étape 3. Jeton d'accès

Obtenez le jeton d'accès Mapbox que nous utiliserons depuis [ici](https://www.mapbox.com/help/how-access-tokens-work/).

`Plotly.plot` a besoin de deux choses principales : `data` et `layout` qui définissent quel type de données sera utilisé et comment il doit être tracé à l'écran.

#### Étape 4. Disposition de la carte

```
var layout = {  title: 'Démonstration de l\'atterrissage de météorites en utilisant Plotly.js',  font: { color: 'white'  },  dragmode: 'zoom',   mapbox: {    center: {  lat: 38.03697222,   lon: -90.70916722    },     style: 'light',     zoom: 2  },   paper_bgcolor: '#191A1A',   plot_bgcolor: '#191A1A',   showlegend: true,  annotations: [{  x: 0,  y: 0,    text: 'NASA',    showarrow: false  }]};
```

Remarquez que nous utilisons `mapbox` pour définir toutes les configurations de la carte, y compris le centre, le niveau de zoom, la couleur et les légendes.

Ajoutez ensuite le jeton que nous avons créé à l'étape 3 en utilisant :

```
Plotly.setPlotConfig({    mapboxAccessToken: 'votre jeton ici'});
```

#### Étape 5. Traiter les données

La dernière chose dont nous avons besoin est d'ajouter notre objet de données à partir du CSV source :

```
var classArray = unpack(rows, 'class');  var classes = [...new Set(classArray)];
```

```
function unpack(rows, key) {    return rows.map(function(row) { return row[key]; });  }
```

```
var data = classes.map(function(classes) {    var rowsFiltered = rows.filter(function(row) {        return (row.class === classes);    });    return {       type: 'scattermapbox',       name: classes,       lat: unpack(rowsFiltered, 'reclat'),       lon: unpack(rowsFiltered, 'reclong')    };  });
```

Maintenant, nous avons les données, la disposition, le jeton et la carte... Voici le résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/VTZuxKBMMrdzclSRmMJqJFmG86RZKxIShFd-)

Ceci était une démonstration de traçage avec une approche étape par étape pour tracer un ensemble de données de carte en utilisant plotly.js. Vous pouvez trouver de nombreux exemples dans la [documentation Plotly](https://plot.ly/javascript/) pour commencer.

J'espère que cela vous a donné une bonne introduction à Plotly js.

**Assurez-vous de laisser vos commentaires ci-dessous**, et le code pour cela peut être trouvé sur mon [Github](https://github.com/edubey/plotly-demo).