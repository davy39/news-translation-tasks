---
title: Comment travailler avec le modèle général de mise à jour de D3.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T17:03:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-d3-jss-general-update-pattern-8adce8d55418
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qyybxSDlom1vFlZ4LwppTg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: Comment travailler avec le modèle général de mise à jour de D3.js
seo_desc: 'By Wen Tjun Chan

  A guided tour on implementing visualization modules with dynamic datasets

  It is common to remove the existing Scalable Vector Graphics (SVG) element by calling
  d3.select(''#chart'').remove(), before rendering a new chart.

  However, ther...'
---

Par Wen Tjun Chan

#### Un guide pour implémenter des modules de visualisation avec des ensembles de données dynamiques

Il est courant de supprimer l'élément Scalable Vector Graphics (SVG) existant en appelant `d3.select('#chart').remove()`, avant de rendre un nouveau graphique.

Cependant, il peut y avoir des scénarios où vous devez produire des visualisations dynamiques à partir de sources telles que des API externes. Cet article vous montrera comment faire cela en utilisant D3.js.

D3.js gère les données dynamiques en adoptant le modèle général de mise à jour. Cela est communément décrit comme une jointure de données, suivie d'opérations sur les sélections enter, update et exit. Maîtriser ces méthodes de sélection vous permettra de produire des transitions fluides entre les états, vous permettant de raconter des histoires significatives avec des données.

### Pour commencer

#### Prérequis

Nous allons construire un graphique qui illustre le mouvement de quelques Exchange-Traded Funds (ETFs) au cours du second semestre 2018. Le graphique se compose des outils suivants :

1. [Graphique en ligne des prix de clôture](https://www.investopedia.com/terms/l/linechart.asp)

2. [Graphique en barres du volume d'échange](https://www.investopedia.com/terms/v/volumeoftrade.asp)

3. Moyenne mobile simple sur 50 jours

4. [Bandes de Bollinger](https://www.investopedia.com/terms/b/bollingerbands.asp) (moyenne mobile simple sur 20 jours, avec un écart-type fixé à 2.0)

5. Graphique Open-High-Low-Close ([OHLC](https://www.investopedia.com/terms/o/ohlcchart.asp))

6. [Chandeliers](https://www.investopedia.com/terms/c/candlestick.asp)

Ces outils sont couramment utilisés dans l'analyse technique des actions, des matières premières et d'autres titres. Par exemple, les traders peuvent utiliser les Bandes de Bollinger et les Chandeliers pour dériver des motifs qui représentent des signaux d'achat ou de vente.

Voici à quoi ressemblera le graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*v3ebquZIF6E5DUL5rbbpdQ.gif align="left")

*Alimenté par D3.js. Observez comment le graphique répond aux interactions de l'utilisateur, et aux changements de données ou d'état.*

Cet article vise à vous équiper des théories fondamentales des jointures de données et du modèle enter-update-exit afin de vous permettre de visualiser facilement des ensembles de données dynamiques. De plus, nous aborderons [selection.join](https://github.com/d3/d3-selection/blob/master/README.md#selection_join), qui est introduit dans la version v5.8.0 de D3.js.

### Le modèle général de mise à jour

L'essentiel du modèle général de mise à jour est la sélection des éléments du Document Object Model (DOM), suivie de la liaison des données à ces éléments. Ces éléments sont ensuite créés, mis à jour ou supprimés, pour représenter les données nécessaires.

#### Jointure de nouvelles données

La jointure de données est la mise en correspondance de `n` éléments dans l'ensemble de données avec `n` nœuds sélectionnés du Document Object Model (DOM), spécifiant l'action requise sur le DOM à mesure que les données changent.

Nous utilisons la méthode `data()` pour mapper chaque point de données à un élément correspondant dans la sélection DOM. De plus, il est bon de maintenir la [constance de l'objet](https://bost.ocks.org/mike/constancy/) en spécifiant une clé comme identifiant unique dans chaque point de données. Examinons l'exemple suivant, qui est la première étape vers le rendu des barres de volume d'échange :

```js
const bars = d3
  .select('#volume-series')
  .selectAll('.vol')
  .data(this.currentData, d => d['date']);
```

La ligne de code ci-dessus sélectionne tous les éléments avec la classe `vol`, suivie de la mise en correspondance du tableau `this.currentData` avec la sélection des éléments DOM en utilisant la méthode `data()`.

Le deuxième argument optionnel de `data()` prend un point de données comme entrée et retourne la propriété `date` comme clé sélectionnée pour chaque point de données.

#### Sélection Enter/Update

`.enter()` retourne une sélection enter qui représente les éléments qui doivent être ajoutés lorsque le tableau joint est plus long que la sélection. Cela est suivi par l'appel de `.append()`, qui crée ou met à jour des éléments sur le DOM. Nous pouvons implémenter cela de la manière suivante :

```js
bars
  .enter()
  .append('rect')
  .attr('class', 'vol')
  .merge(bars)
  .transition()
  .duration(750)
  .attr('x', d => this.xScale(d['date']))
  .attr('y', d => yVolumeScale(d['volume']))
  .attr('fill', (d, i) => {
    if (i === 0) {
      return '#03a678';
    } else {
      // barre verte si le prix augmente pendant cette période, et rouge lorsque le prix baisse
      return this.currentData[i - 1].close > d.close
        ? '#c0392b'
        : '#03a678';
    }
  })
  .attr('width', 1)
  .attr('height', d => this.height - yVolumeScale(d['volume']));
```

`.merge()` fusionne les sélections update et enter, avant d'appliquer les chaînes de méthodes suivantes pour créer des animations entre les transitions, et pour mettre à jour leurs attributs associés. Le bloc de code ci-dessus vous permet d'effectuer les actions suivantes sur les éléments DOM sélectionnés :

1. La sélection update, qui se compose de points de données représentés par les éléments `<rect>` sur le graphique, aura leurs attributs mis à jour en conséquence.

2. La création d'éléments `<rect>` avec la classe `vol`, avec les attributs ci-dessus définis dans chaque élément car la sélection enter se compose de points de données qui ne sont pas représentés sur le graphique.

#### Sélection Exit

Supprimez les éléments de notre ensemble de données en suivant les étapes simples ci-dessous :bars.exit().remove();

`.exit()` retourne une sélection exit, qui spécifie les points de données qui doivent être supprimés. La méthode `.remove()` supprime ensuite la sélection du DOM.

Voici comment les barres de la série de volume répondront aux changements de données :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dEZBCu-p5hRGZNJGMCtG4Q.gif align="left")

*Remarquez comment les barres changent lorsque nous passons d'un ensemble de données à un autre.*

Notez comment le DOM et les attributs respectifs de chaque élément `<rect>` sont mis à jour lorsque nous sélectionnons un ensemble de données différent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XI_7a6kYRLT__mvLEPD0qA.gif align="left")

*Observez les changements dans le DOM via les outils de développement Chrome intégrés.*

### Selection.join (à partir de la v5.8.0)

L'introduction de `selection.join` dans la v5.8.0 de D3.js a simplifié l'ensemble du processus de jointure de données. Des fonctions séparées sont maintenant passées pour gérer enter, update et exit, qui à leur tour retournent les sélections enter et update fusionnées.

```js
selection.join(
    enter => // enter.. ,
    update => // update.. ,
    exit => // exit.. 
  )
  // permet des opérations enchaînées sur les sélections retournées
```

Dans le cas des barres de la série de volume, l'application de `selection.join` entraînera les modifications suivantes dans notre code :

```js
// sélection, suivie de la mise à jour de la jointure de données
const bars = d3
  .select('#volume-series')
  .selectAll('.vol')
  .data(this.currentData, d => d['date']);
bars.join(
  enter =>
    enter
      .append('rect')
      .attr('class', 'vol')
      .attr('x', d => this.xScale(d['date']))
      .attr('y', d => yVolumeScale(d['volume']))
      .attr('fill', (d, i) => {
        if (i === 0) {
          return '#03a678';
        } else {
          return this.currentData[i - 1].close > d.close
            ? '#c0392b'
            : '#03a678';
        }
      })
      .attr('width', 1)
      .attr('height', d => this.height - yVolumeScale(d['volume'])),
  update =>
    update
      .transition()
      .duration(750)
      .attr('x', d => this.xScale(d['date']))
      .attr('y', d => yVolumeScale(d['volume']))
      .attr('fill', (d, i) => {
        if (i === 0) {
          return '#03a678';
        } else {
          return this.currentData[i - 1].close > d.close
            ? '#c0392b'
            : '#03a678';
        }
      })
      .attr('width', 1)
      .attr('height', d => this.height - yVolumeScale(d['volume']))
);
```

Notez également que nous avons apporté quelques modifications à l'animation des barres. Au lieu de passer la méthode `transition()` aux sélections enter et update fusionnées, elle est maintenant utilisée dans la sélection update de sorte que les transitions ne seront appliquées que lorsque l'ensemble de données a changé.

Les sélections enter et update retournées sont ensuite fusionnées et retournées par `selection.join`.

#### Bandes de Bollinger

De même, nous pouvons appliquer `selection.join` sur le rendu des Bandes de Bollinger. Avant de rendre les Bandes, nous devons calculer les propriétés suivantes de chaque point de données :

1. Moyenne mobile simple sur 20 jours.

2. Les bandes supérieure et inférieure, qui ont un écart-type de 2.0 au-dessus et en dessous de la moyenne mobile simple sur 20 jours, respectivement.

Voici la formule pour calculer l'écart-type :

![Image](https://cdn-media-1.freecodecamp.org/images/0*aVvmssYG1cPl2aDB align="left")

*Crédits :* [*Khan Academy*](https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step)

Maintenant, nous allons traduire la formule ci-dessus en code JavaScript :

```js
calculateBollingerBands(data, numberOfPricePoints) {
  let sumSquaredDifference = 0;
  return data.map((row, index, total) => {
    const start = Math.max(0, index - numberOfPricePoints);
    const end = index; 
    
    // diviser la somme par subset.length pour obtenir la moyenne mobile
    const subset = total.slice(start, end + 1);
    const sum = subset.reduce((a, b) => {
      return a + b['close'];
    }, 0);
    const sumSquaredDifference = subset.reduce((a, b) => {
      const average = sum / subset.length;
      const dfferenceFromMean = b['close'] - average;
      const squaredDifferenceFromMean = Math.pow(dfferenceFromMean, 2);
      return a + squaredDifferenceFromMean;
    }, 0);
    const variance = sumSquaredDifference / subset.length;
  return {
      date: row['date'],
      average: sum / subset.length,
      standardDeviation: Math.sqrt(variance),
      upperBand: sum / subset.length + Math.sqrt(variance) * 2,
      lowerBand: sum / subset.length - Math.sqrt(variance) * 2
    };
  });
}
.
.
// calcule la moyenne mobile simple et l'écart-type sur 20 jours
this.bollingerBandsData = this.calculateBollingerBands(validData, 19);
```

Une explication rapide du calcul de l'écart-type et des valeurs des Bandes de Bollinger sur le bloc de code ci-dessus est la suivante :

Pour chaque itération,

1. Calculez la moyenne du prix de clôture.

2. Trouvez la différence entre la valeur moyenne et le prix de clôture pour ce point de données.

3. Élevez au carré le résultat de chaque différence.

4. Trouvez la somme des différences au carré.

5. Calculez la moyenne des différences au carré pour obtenir la variance.

6. Obtenez la racine carrée de la variance pour obtenir l'écart-type pour chaque point de données.

7. Multipliez l'écart-type par 2. Calculez les valeurs des bandes supérieure et inférieure en ajoutant ou en soustrayant la moyenne avec la valeur multipliée.

Avec les points de données définis, nous pouvons ensuite utiliser `selection.join` pour rendre les Bandes de Bollinger :

```js
// code non montré : rendu des bandes supérieure et inférieure
.
.
// graphique en aire des bandes de Bollinger
const area = d3
  .area()
  .x(d => this.xScale(d['date']))
  .y0(d => this.yScale(d['upperBand']))
  .y1(d => this.yScale(d['lowerBand']));
const areaSelect = d3
  .select('#chart')
  .select('svg')
  .select('g')
  .selectAll('.band-area')
  .data([this.bollingerBandsData]);
areaSelect.join(
  enter =>
    enter
      .append('path')
      .style('fill', 'darkgrey')
      .style('opacity', 0.2)
      .style('pointer-events', 'none')
      .attr('class', 'band-area')
      .attr('clip-path', 'url(#clip)')
      .attr('d', area),
  update =>
    update
      .transition()
      .duration(750)
      .attr('d', area)
);
```

Cela rend le graphique en aire qui désigne la zone remplie par les Bandes de Bollinger. Dans la fonction de mise à jour, nous pouvons utiliser la méthode `selection.transition()` pour fournir des transitions animées sur la sélection de mise à jour.

#### Chandeliers

Le graphique en chandeliers affiche les prix haut, bas, ouvert et fermé d'une action pour une période spécifique. Chaque chandelier représente un point de données. Le vert représente lorsque l'action clôture plus haut tandis que le rouge représente lorsque l'action clôture à une valeur plus basse.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GGsqZeYDGuZzrvGd align="left")

*Crédits :* [*Investopedia*](https://www.investopedia.com/terms/c/candlestick.asp)

Contrairement aux Bandes de Bollinger, il n'est pas nécessaire de calculs supplémentaires, car les prix sont disponibles dans l'ensemble de données existant.

```js
const bodyWidth = 5;
const candlesticksLine = d3
  .line()
  .x(d => d['x'])
  .y(d => d['y']);
const candlesticksSelection = d3
  .select('#chart')
  .select('g')
  .selectAll('.candlesticks')
  .data(this.currentData, d => d['volume']);
candlesticksSelection.join(enter => {
  const candlesticksEnter = enter
    .append('g')
    .attr('class', 'candlesticks')
    .append('g')
    .attr('class', 'bars')
    .classed('up-day', d => d['close'] > d['open'])
    .classed('down-day', d => d['close'] <= d['open']);
```

Dans la fonction enter, chaque chandelier est rendu en fonction de ses propriétés individuelles.

Tout d'abord, chaque élément de groupe de chandeliers se voit attribuer une classe `up-day` si le prix de clôture est supérieur au prix d'ouverture, et `down-day` si le prix de clôture est inférieur ou égal au prix d'ouverture.

```js
candlesticksEnter
    .append('path')
    .classed('high-low', true)
    .attr('d', d => {
      return candlesticksLine([
        { x: this.xScale(d['date']), y: this.yScale(d['high']) },
        { x: this.xScale(d['date']), y: this.yScale(d['low']) }
      ]);
    });
```

Ensuite, nous ajoutons l'élément `path`, qui représente le prix le plus haut et le plus bas de ce jour, à la sélection ci-dessus.

```js
  candlesticksEnter
    .append('rect')
    .attr('x', d => this.xScale(d.date) - bodyWidth / 2)
    .attr('y', d => {
      return d['close'] > d['open']
        ? this.yScale(d.close)
        : this.yScale(d.open);
    })
    .attr('width', bodyWidth)
    .attr('height', d => {
      return d['close'] > d['open']
        ? this.yScale(d.open) - this.yScale(d.close)
        : this.yScale(d.close) - this.yScale(d.open);
    });
});
```

Cela est suivi par l'ajout de l'élément `rect` à la sélection. La hauteur de chaque élément `rect` est directement proportionnelle à sa plage de jour, dérivée en soustrayant le prix d'ouverture du prix de clôture.

Dans nos feuilles de style, nous définirons les propriétés CSS suivantes pour nos classes rendant les chandeliers rouges ou verts :

```js
.bars.up-day path {
 stroke: #03a678;
}
.bars.down-day path {
 stroke: #c0392b;
}
.bars.up-day rect {
 fill: #03a678;
}
.bars.down-day rect {
 fill: #c0392b;
}
```

Cela entraîne le rendu des Bandes de Bollinger et des chandeliers :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TOj5vW_eVXLlscri0zbY4A.gif align="left")

*Il est courant pour les traders d'utiliser à la fois les Bandes de Bollinger et les chandeliers pour l'analyse technique.*

La nouvelle syntaxe s'est avérée plus simple et plus intuitive que d'appeler explicitement `selection.enter`, `selection.append`, `selection.merge` et `selection.remove`.

Notez que pour ceux qui développent avec la v5.8.0 de D3.js et au-delà, il a été [recommandé](https://bl.ocks.org/mbostock/3808218) par Mike Bostock que ces utilisateurs commencent à utiliser `selection.join` en raison des avantages ci-dessus.

### Conclusion

Le potentiel de D3.js est illimité et les illustrations ci-dessus ne sont que la partie émergée de l'iceberg. De nombreux utilisateurs satisfaits ont créé des visualisations bien plus complexes et sophistiquées que celle montrée ci-dessus. Cette [liste d'API gratuites](https://github.com/toddmotto/public-apis) pourrait vous intéresser si vous souhaitez vous lancer dans vos propres projets de visualisation de données.

N'hésitez pas à consulter le [code source](https://github.com/wentjun/d3-historical-prices-data-joins) et la [démonstration complète](https://wentjun.com/d3-historical-prices-data-joins/) de ce projet.

Merci beaucoup d'avoir lu cet article. Si vous avez des questions ou des suggestions, n'hésitez pas à les laisser dans les commentaires ci-dessous !

*Nouveau dans D3.js ? Vous pouvez vous référer à cet* [*article*](https://medium.freecodecamp.org/how-to-build-historical-price-charts-with-d3-js-72214aaf6ba3) *sur les bases de l'implémentation des composants de graphique courants.*

*Un merci spécial à Debbie Leong pour avoir révisé cet article.*

Références supplémentaires :

1. [Documentation de l'API D3.js](https://github.com/d3/d3/blob/master/API.md)

2. [Démonstration interactive de selection.join](https://beta.observablehq.com/@d3/selection-join)