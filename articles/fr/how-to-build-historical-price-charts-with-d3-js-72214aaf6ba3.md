---
title: Comment créer des graphiques de prix historiques avec D3.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T17:15:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-historical-price-charts-with-d3-js-72214aaf6ba3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4xr6-FwevPj7MIL756bDwA.png
tags:
- name: data visualization
  slug: data-visualization
- name: fintech
  slug: fintech
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer des graphiques de prix historiques avec D3.js
seo_desc: 'By Wen Tjun Chan

  A step by step approach towards visualizing financial datasets

  It is a challenge to communicate data and display these visualizations on multiple
  devices and platforms.


  “Data is just like crude. It’s valuable, but if unrefined it ca...'
---

Par Wen Tjun Chan

#### Une approche étape par étape pour visualiser des ensembles de données financières

Il est difficile de communiquer des données et d'afficher ces visualisations sur plusieurs appareils et plateformes.

> « Les données sont comme le pétrole brut. Elles sont précieuses, mais si elles ne sont pas raffinées, elles ne peuvent pas vraiment être utilisées. » - [Michael Palmer](https://ana.blogs.com/maestros/2006/11/data_is_the_new.html)

D3 (Data-Driven Documents) résout ce dilemme ancestral. Il offre aux développeurs et analystes la possibilité de créer des visualisations personnalisées pour le Web avec une liberté totale. D3.js nous permet de lier des données au DOM (Document Object Model). Ensuite, appliquer des transformations basées sur les données pour créer des visualisations raffinées des données.

Dans ce tutoriel, nous comprendrons comment faire fonctionner la bibliothèque D3.js pour nous.

#### Mise en route

Nous allons construire un graphique qui illustre le mouvement d'un instrument financier sur une période de temps. Cette visualisation ressemble aux graphiques de prix fournis par [Yahoo Finance](https://finance.yahoo.com). Nous allons décomposer les différents composants nécessaires pour rendre un graphique de prix interactif qui suit une action particulière [stock](https://sg.finance.yahoo.com/quote/VIG/chart?p=VIG).

Composants requis :

1. Chargement et analyse des données
2. Élément SVG
3. Axes X et Y
4. Graphique en ligne du prix de clôture
5. Courbe de la moyenne mobile simple avec quelques calculs
6. Graphique en barres de la série de volumes
7. Légende et réticule au survol de la souris

#### Chargement et analyse des données

```js
const loadData = d3.json('sample-data.json').then(data => {
  const chartResultsData = data['chart']['result'][0];
  const quoteData = chartResultsData['indicators']['quote'][0];
  return chartResultsData['timestamp'].map((time, index) => ({
    date: new Date(time * 1000),
    high: quoteData['high'][index],
    low: quoteData['low'][index],
    open: quoteData['open'][index],
    close: quoteData['close'][index],
    volume: quoteData['volume'][index]
  }));
});
```

Tout d'abord, nous allons utiliser le module [fetch](https://github.com/d3/d3-fetch) pour charger nos données d'exemple. D3-fetch prend également en charge d'autres formats tels que les fichiers TSV et CSV. Les données seront ensuite traitées pour retourner un tableau d'objets. Chaque objet contient l'horodatage de la transaction, le prix le plus haut, le prix le plus bas, le prix d'ouverture, le prix de clôture et le volume de transaction.

```css
body {
  background: #00151c;
}
#chart {
  background: #0e3040;
  color: #67809f;
}
```

Ajoutez les propriétés CSS de base ci-dessus pour personnaliser le style de votre graphique pour un attrait visuel maximal.

#### Ajout de l'élément SVG

```js
const initialiseChart = data => {
  const margin = { top: 50, right: 50, bottom: 50, left: 50 };
  const width = window.innerWidth - margin.left - margin.right;
  const height = window.innerHeight - margin.top - margin.bottom; 
  // ajouter SVG à la page
  const svg = d3
    .select('#chart')
    .append('svg')
    .attr('width', width + margin['left'] + margin['right'])
    .attr('height', height + margin['top'] + margin['bottom'])
    .call(responsivefy)
    .append('g')
    .attr('transform', `translate(${margin['left']},  ${margin['top']})`);
```

Par la suite, nous pouvons utiliser la méthode `append()` pour ajouter l'élément SVG à l'élément `<div>` avec l'id `chart`. Ensuite, nous utilisons la méthode `attr()` pour assigner la largeur et la hauteur de l'élément SVG. Nous appelons ensuite la méthode `responsivefy()` (originalement écrite par [Brendan Sudol](https://brendansudol.com/writing/responsive-d3)). Cela permet à l'élément SVG d'avoir des capacités réactives en écoutant les événements de redimensionnement de la fenêtre.

N'oubliez pas d'ajouter l'élément de groupe SVG à l'élément SVG ci-dessus avant de le traduire en utilisant les valeurs de la constante `margin`.

#### Rendu des axes X et Y

Avant de rendre le composant des axes, nous devons définir notre domaine et notre plage, qui seront ensuite utilisés pour créer nos échelles pour les axes.

```js
// trouver la plage de données
const xMin = d3.min(data, d => {
  return d['date'];
});
const xMax = d3.max(data, d => {
  return d['date'];
});
const yMin = d3.min(data, d => {
  return d['close'];
});
const yMax = d3.max(data, d => {
  return d['close'];
});
// échelles pour les graphiques
const xScale = d3
  .scaleTime()
  .domain([xMin, xMax])
  .range([0, width]);
const yScale = d3
  .scaleLinear()
  .domain([yMin - 5, yMax])
  .range([height, 0]);
```

Les axes x et y pour le graphique en ligne du prix de clôture sont constitués de la date de transaction et du prix de clôture, respectivement. Par conséquent, nous devons définir les valeurs x et y minimales et maximales, en utilisant `d3.max()` et `d3.min()`. Nous pouvons ensuite utiliser `scaleTime()` et `scaleLinear()` de [D3-scale](https://github.com/d3/d3-scale) pour créer l'échelle de temps sur l'axe x et l'échelle linéaire sur l'axe y, respectivement. La plage des échelles est définie par la largeur et la hauteur de notre élément SVG.

```js
// créer le composant des axes
svg
  .append('g')
  .attr('id', 'xAxis')
  .attr('transform', `translate(0, ${height})`)
  .call(d3.axisBottom(xScale));
svg
  .append('g')
  .attr('id', 'yAxis')
  .attr('transform', `translate(${width}, 0)`)
  .call(d3.axisRight(yScale));
```

Après cette étape, nous devons ajouter le premier élément `g` à l'élément SVG, qui appelle la méthode `d3.axisBottom()`, en prenant `xScale` comme paramètre pour générer l'axe x. L'axe x est ensuite traduit en bas de la zone du graphique. De même, l'axe y est généré en ajoutant l'élément `g`, en appelant `d3.axisRight()` avec `yScale` comme paramètre, avant de traduire l'axe y à droite de la zone du graphique.

#### Rendu du graphique en ligne du prix de clôture

```
// génère le graphique en ligne du prix de clôture lorsqu'il est appelé
const line = d3
  .line()
  .x(d => {
    return xScale(d['date']);
  })
  .y(d => {
    return yScale(d['close']);
  });
// Ajouter le chemin et lier les données
svg
 .append('path')
 .data([data])
 .style('fill', 'none')
 .attr('id', 'priceChart')
 .attr('stroke', 'steelblue')
 .attr('stroke-width', '1.5')
 .attr('d', line);
```

Maintenant, nous pouvons ajouter l'élément `[path](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths)` à l'intérieur de notre élément SVG principal, suivi du passage de notre jeu de données analysé, `data`. Nous définissons l'attribut `d` avec notre fonction auxiliaire, `line`, qui appelle la méthode `d3.line()`. Les attributs `x` et `y` de la ligne acceptent les fonctions anonymes et retournent la date et le prix de clôture, respectivement.

À ce stade, voici à quoi votre graphique devrait ressembler :

![Image](https://cdn-media-1.freecodecamp.org/images/fnbftLMqi8MQnIy8ZZBrqsKN8fXYVfodvgQ2)
_Point de contrôle #1 : Graphique en ligne du prix de clôture, avec les axes X et Y._

#### Rendu de la courbe de la moyenne mobile simple

Au lieu de nous fier uniquement au prix de clôture comme seul indicateur technique, nous utilisons la [Moyenne Mobile Simple](https://www.investopedia.com/terms/s/sma.asp). Cette moyenne identifie les tendances à la hausse et à la baisse pour le titre particulier.

```
const movingAverage = (data, numberOfPricePoints) => {
  return data.map((row, index, total) => {
    const start = Math.max(0, index - numberOfPricePoints);
    const end = index;
    const subset = total.slice(start, end + 1);
    const sum = subset.reduce((a, b) => {
      return a + b['close'];
    }, 0);
    return {
      date: row['date'],
      average: sum / subset.length
    };
  });
};
```

Nous définissons notre fonction auxiliaire, `movingAverage`, pour calculer la moyenne mobile simple. Cette fonction accepte deux paramètres, à savoir le jeu de données et le nombre de points de prix, ou périodes. Elle retourne ensuite un tableau d'objets, chaque objet contenant la date et la moyenne pour chaque point de données.

```js
// calcule la moyenne mobile simple sur 50 jours
const movingAverageData = movingAverage(data, 49);
// génère la courbe de la moyenne mobile lorsqu'elle est appelée
const movingAverageLine = d3
 .line()
 .x(d => {
  return xScale(d['date']);
 })
 .y(d => {
  return yScale(d['average']);
 })
  .curve(d3.curveBasis);
svg
  .append('path')
  .data([movingAverageData])
  .style('fill', 'none')
  .attr('id', 'movingAverageLine')
  .attr('stroke', '#FF8900')
  .attr('d', movingAverageLine);
```

Dans notre contexte actuel, `movingAverage()` calcule la moyenne mobile simple sur une période de 50 jours. Similaire au graphique en ligne du prix de clôture, nous ajoutons l'élément `path` à l'intérieur de notre élément SVG principal, suivi du passage de notre jeu de données de la moyenne mobile, et en définissant l'attribut `d` avec notre fonction auxiliaire, `movingAverageLine`. La seule différence avec ce qui précède est que nous avons passé `d3.curveBasis` à `d3.line().curve()` afin d'obtenir une courbe.

Cela donne la courbe de la moyenne mobile simple superposée à notre graphique actuel :

![Image](https://cdn-media-1.freecodecamp.org/images/XhcAf6lV84KJ5fOpcZ6reXZ4ovtPqA9Y07dM)
_Point de contrôle #2 : Courbe orange, qui représente la moyenne mobile simple. Cela nous donne une meilleure idée du mouvement des prix._

#### Rendu du graphique en barres de la série de volumes

Pour ce composant, nous allons rendre le [volume](https://commodity.com/technical-analysis/volume/) des transactions sous la forme d'un graphique en barres codé par couleur occupant le même élément SVG. Les barres sont vertes lorsque l'action clôture plus haut que le prix de clôture de la veille. Elles sont rouges lorsque l'action clôture plus bas que le prix de clôture de la veille. Cela illustre le volume échangé pour chaque date de transaction. Cela peut ensuite être utilisé avec le graphique ci-dessus pour analyser les mouvements de prix.

```js
/* Barres de la série de volumes */
const volData = data.filter(d => d['volume'] !== null && d['volume'] !== 0);
const yMinVolume = d3.min(volData, d => {
  return Math.min(d['volume']);
});
const yMaxVolume = d3.max(volData, d => {
  return Math.max(d['volume']);
});
const yVolumeScale = d3
  .scaleLinear()
  .domain([yMinVolume, yMaxVolume])
  .range([height, 0]);
```

Les axes x et y pour le graphique en barres de la série de volumes sont constitués de la date de transaction et du volume, respectivement. Ainsi, nous devons redéfinir les valeurs y minimales et maximales et utiliser `scaleLinear()` sur l'axe y. La plage de ces échelles est définie par la largeur et la hauteur de notre élément SVG. Nous allons réutiliser `xScale` puisque l'axe x du graphique en barres correspond de manière similaire à la date de transaction.

```js
svg
  .selectAll()
  .data(volData)
  .enter()
  .append('rect')
  .attr('x', d => {
    return xScale(d['date']);
  })
  .attr('y', d => {
    return yVolumeScale(d['volume']);
  })
  .attr('fill', (d, i) => {
    if (i === 0) {
      return '#03a678';
    } else {  
      return volData[i - 1].close > d.close ? '#c0392b' : '#03a678'; 
    }
  })
  .attr('width', 1)
  .attr('height', d => {
    return height - yVolumeScale(d['volume']);
  });
```

Cette section repose sur votre compréhension du fonctionnement de la méthode `selectAll()` avec les méthodes `enter()` et `append()`. Vous pouvez lire [ceci](https://bost.ocks.org/mike/join/) (écrit par [Mike Bostock](https://bost.ocks.org/mike/) lui-même) si vous n'êtes pas familier avec ces méthodes. Cela peut être important car ces méthodes sont utilisées dans le cadre du modèle [enter-update-exit](https://bost.ocks.org/mike/join/), que je pourrais aborder dans un tutoriel ultérieur.

Pour rendre les barres, nous allons d'abord utiliser `.selectAll()` pour retourner une sélection vide, ou un tableau vide. Ensuite, nous passons `volData` pour définir la hauteur de chaque barre. La méthode `enter()` compare le jeu de données `volData` avec la sélection de `selectAll()`, qui est actuellement vide. Actuellement, le DOM ne contient aucun élément `<rect>`. Ainsi, la méthode `append()` accepte un argument 'rect', qui crée un nouvel élément `<rect>` dans le DOM pour chaque objet unique dans volData.

Voici une ventilation des attributs des barres. Nous allons utiliser les attributs suivants : `x`, `y`, `fill`, `width`, et `height`.

```
.attr('x', d => {
  return xScale(d['date']);
})
.attr('y', d => {
  return yVolumeScale(d['volume']);
})
```

La première méthode `attr()` définit la coordonnée x. Elle accepte une fonction anonyme qui retourne la date. De même, la deuxième méthode `attr()` définit la coordonnée y. Elle accepte une fonction anonyme qui retourne le volume. Ceux-ci définiront la position de chaque barre.

```
.attr('width', 1)
.attr('height', d => {
  return height - yVolumeScale(d['volume']);
});
```

Nous attribuons une largeur de 1 pixel à chaque barre. Pour faire en sorte que la barre s'étire du haut (définie par `y`) à l'axe x, il suffit de déduire la hauteur avec la valeur `y`.

```
.attr('fill', (d, i) => {
  if (i === 0) {
    return '#03a678';
  } else {  
    return volData[i - 1].close > d.close ? '#c0392b' : '#03a678'; 
  }
})
```

Rappelez-vous la manière dont les barres seront codées par couleur ? Nous allons utiliser l'attribut `fill` pour définir les couleurs de chaque barre. Pour les actions qui ont clôturé plus haut que le prix de clôture de la veille, la barre sera verte. Sinon, la barre sera rouge.

Voici à quoi votre graphique actuel devrait ressembler :

![Image](https://cdn-media-1.freecodecamp.org/images/f3q6i4i1wTbBzHe4TXuLTR3Blcg4YbOYUsCW)
_Point de contrôle #3 : Graphique de la série de volumes, représenté par des barres rouges et vertes._

#### Rendu du réticule et de la légende pour l'interactivité

Nous avons atteint la dernière étape de ce tutoriel, où nous allons générer un réticule au survol de la souris qui affiche des lignes de chute. Le survol des différents points du graphique fera en sorte que les légendes soient mises à jour. Cela nous fournit les informations complètes (prix d'ouverture, prix de clôture, prix le plus haut, prix le plus bas et volume) pour chaque date de transaction.

La section suivante est référencée de [l'excellent exemple de Micah Stubbs](https://bl.ocks.org/micahstubbs/e4f5c830c264d26621b80b754219ae1b).

```js
// rend les réticules x et y
const focus = svg
  .append('g')
  .attr('class', 'focus')
  .style('display', 'none');
focus.append('circle').attr('r', 4.5);
focus.append('line').classed('x', true);
focus.append('line').classed('y', true);
svg
  .append('rect')
  .attr('class', 'overlay')
  .attr('width', width)
  .attr('height', height)
  .on('mouseover', () => focus.style('display', null))
  .on('mouseout', () => focus.style('display', 'none'))
  .on('mousemove', generateCrosshair);
d3.select('.overlay').style('fill', 'none');
d3.select('.overlay').style('pointer-events', 'all');
d3.selectAll('.focus line').style('fill', 'none');
d3.selectAll('.focus line').style('stroke', '#67809f');
d3.selectAll('.focus line').style('stroke-width', '1.5px');
d3.selectAll('.focus line').style('stroke-dasharray', '3 3');
```

Le réticule se compose d'un cercle translucide avec des lignes de chute composées de tirets. Le bloc de code ci-dessus fournit le style des éléments individuels. Au survol de la souris, il générera le réticule en fonction de la fonction ci-dessous.

```js
const bisectDate = d3.bisector(d => d.date).left;
function generateCrosshair() {
  // retourne la valeur correspondante du domaine
  const correspondingDate = xScale.invert(d3.mouse(this)[0]);
  // obtient le point d'insertion
  const i = bisectDate(data, correspondingDate, 1);
  const d0 = data[i - 1];
  const d1 = data[i];
  const currentPoint = correspondingDate - d0['date'] > d1['date'] - correspondingDate ? d1 : d0;
  
  focus.attr('transform',`translate(${xScale(currentPoint['date'])},     ${yScale(currentPoint['close'])})`);
focus
  .select('line.x')
  .attr('x1', 0)
  .attr('x2', width - xScale(currentPoint['date']))
  .attr('y1', 0)
  .attr('y2', 0);
focus
  .select('line.y')
  .attr('x1', 0)
  .attr('x2', 0)
  .attr('y1', 0)
  .attr('y2', height - yScale(currentPoint['close']));
 updateLegends(currentPoint);
}
```

Nous pouvons ensuite utiliser la méthode [d3.bisector()](https://github.com/d3/d3-array#bisect) pour localiser le point d'insertion, qui mettra en évidence le point de données le plus proche sur le graphique en ligne du prix de clôture. Après avoir déterminé le `currentPoint`, les lignes de chute seront mises à jour. La méthode `updateLegends()` utilise le `currentPoint` comme paramètre.

```
const updateLegends = currentData => {  d3.selectAll('.lineLegend').remove();
```

```
const updateLegends = currentData => {
  d3.selectAll('.lineLegend').remove();
  const legendKeys = Object.keys(data[0]);
  const lineLegend = svg
    .selectAll('.lineLegend')
    .data(legendKeys)
    .enter()
    .append('g')
    .attr('class', 'lineLegend')
    .attr('transform', (d, i) => {
      return `translate(0, ${i * 20})`;
    });
  lineLegend
    .append('text')
    .text(d => {
      if (d === 'date') {
        return `${d}: ${currentData[d].toLocaleDateString()}`;
      } else if ( d === 'high' || d === 'low' || d === 'open' || d === 'close') {
        return `${d}: ${currentData[d].toFixed(2)}`;
      } else {
        return `${d}: ${currentData[d]}`;
      }
    })
    .style('fill', 'white')
    .attr('transform', 'translate(15,9)');
  };
```

La méthode `updateLegends()` met à jour la légende en affichant la date, le prix d'ouverture, le prix de clôture, le prix le plus haut, le prix le plus bas et le volume du point sélectionné au survol de la souris sur le graphique en ligne de clôture. Similaire aux graphiques en barres de volume, nous allons utiliser la méthode `selectAll()` avec les méthodes `enter()` et `append()`.

Pour rendre les légendes, nous allons utiliser `.selectAll('.lineLegend')` pour sélectionner les légendes, suivi de l'appel de la méthode `remove()` pour les supprimer. Ensuite, nous passons les clés des légendes, `legendKeys`, qui seront utilisées pour définir la hauteur de chaque barre. La méthode `enter()` est appelée, qui compare le jeu de données `volData` et la sélection de `selectAll()`, qui est actuellement vide. Actuellement, le DOM ne contient aucun élément `<rect>`. Ainsi, la méthode `append()` accepte un argument 'rect', qui crée un nouvel élément `<rect>` dans le DOM pour chaque objet unique dans volData.

Ensuite, ajoutez les légendes avec leurs propriétés respectives. Nous traitons davantage les valeurs en convertissant les prix à 2 décimales. Nous définissons également l'objet date à la [locale par défaut](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString) pour la lisibilité.

Ce sera le résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/TdHsr5qhwh-KFRJHOeGi0RfqtYS8XD4QbCjG)
_Point de contrôle #4 : Survolez n'importe quelle partie du graphique !_

#### Réflexions finales

Félicitations ! Vous avez atteint la fin de ce tutoriel. Comme démontré ci-dessus, D3.js est simple mais dynamique. Il vous permet de créer des visualisations personnalisées pour tous vos ensembles de données. Dans les semaines à venir, je publierai la deuxième partie de cette série qui approfondira le modèle enter-update-exit de D3.js. En attendant, vous pouvez consulter la [documentation de l'API](https://github.com/d3/d3/wiki), [plus de tutoriels](https://github.com/d3/d3/wiki/Tutorials), et [d'autres visualisations intéressantes construites avec D3.js](https://github.com/d3/d3/wiki/Gallery).

N'hésitez pas à consulter le [code source](https://github.com/wentjun/d3-historical-price-chart-basic) ainsi que la [démonstration complète](https://wentjun.com/d3-historical-price-chart-basic/) de ce tutoriel. Merci, et j'espère que vous avez appris quelque chose de nouveau aujourd'hui !

_Un merci spécial à Debbie Leong pour la révision de cet article._