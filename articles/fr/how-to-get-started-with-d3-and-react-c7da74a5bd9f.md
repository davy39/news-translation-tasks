---
title: Comment commencer avec D3 et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-13T17:13:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-d3-and-react-c7da74a5bd9f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AEjU4WgW-clHPyokVbdcVg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment commencer avec D3 et React
seo_desc: 'By Magdalena Stenius

  Data Driven Documents (D3.js) is a JavaScript library used to create visualizations
  of data using HTML, CSS, and SVG. It does this by binding data to the DOM (Document
  Object Model) and its elements and allowing them to transform...'
---

Par Magdalena Stenius

Data Driven Documents (D3.js) est une bibliothèque JavaScript utilisée pour créer des visualisations de données en utilisant HTML, CSS et SVG. Elle le fait en liant les données au DOM (Document Object Model) et à ses éléments, et en permettant leur transformation lorsque les données changent.

Par exemple, supposons que nous voulons créer un graphique en secteurs des quantités de livres dans chaque genre dans une bibliothèque. Nous avons des données que nous mettons à jour chaque fois qu'un bibliothécaire entre un nouveau livre. Nous les stockons dans l'état de l'application, dans une variable appelée « books ».

```js
const [books, setBooks] = useState(initialBooks)
const initialBooks = [
    {
        name: "Harry Potter à l'école des sorciers",
        author: "J. K. Rowling",
        genre: "fantasy"
    },{
        name: "La pédagogie de la liberté",
        author: "Bell hooks",
        genre: "non-fiction"
    },{
        name: "Harry Potter et la Chambre des Secrets",
        author: "J. K. Rowling",
        genre: "fantasy"
    },{
        name: "Gilgamesh",
        author: "Derrek Hines",
        genre: "poetry"
    }
]
```

Actuellement, nous pourrions créer un graphique qui a 50% de fantasy, 25% de non-fiction et 25% de poésie. Lorsque le bibliothécaire ajoute un nouveau livre à la base de données, les données changent et votre graphique se modifie. Supposons que nous ajoutons « 50 plats vegans ».

```js
setBooks(books.concat(
    {
        name: "50 plats vegans",
        author: "Antti Leppänen",
        genre: "non-fiction"
    }
))
```

Lorsque ces données changent, notre graphique D3 met à jour le DOM pour correspondre aux nouvelles données. Nous avons maintenant 40% de fantasy, 40% de non-fiction et 20% de poésie. D3 facilite la manipulation du DOM du site web. Cela signifie que vous pouvez l'utiliser pour créer, mettre à jour et supprimer des éléments dans la structure de la page.

Si vous souhaitez suivre cet exemple, vous pouvez utiliser [Create React App](https://github.com/facebook/create-react-app) pour créer une simple application web React. Si React vous est encore inconnu, vous pouvez [consulter ce tutoriel](https://reactjs.org/tutorial/tutorial.html) de la documentation React.

1. Créez une nouvelle application, appelée my-d3-app `npx create-react-app my-d3-app`. Changez de répertoire dans le dossier créé en utilisant `cd my-d3-app`.
2. Installez D3 en exécutant `npm install d3 --save`.
3. Importez D3 dans App.js en ajoutant `import * as d3 from 'd3'`. Vous devez utiliser import * (« importer tout ») puisque D3 n'a pas de module exporté par défaut.

#### Sélection des éléments du DOM

D3 facilite la manipulation du DOM. Par exemple, essayons de changer tous les éléments `<p>` pour qu'ils aient un style en ligne définissant la couleur en bleu.

`d3.selectAll("p").style("color", "blue")`

La méthode `.selectAll()` nous permet de sélectionner tous les éléments d'un type spécifique. Nous pouvons également utiliser `.select()` pour sélectionner des nœuds individuels.

La bibliothèque React manipule également le DOM. Cela signifie que nous devons faire un petit effort supplémentaire pour qu'elle fonctionne avec D3. Heureusement, React a déjà une solution pour permettre le ciblage et la mise à jour des éléments du DOM. Pour ce faire, React utilise des références.

Créons un élément `<div>` et ajoutons une référence à celui-ci, puis utilisons la référence pour le sélectionner avec D3.

```js
d3.select(this.refs.myDiv).style("background-color", "blue")
render(<div ref="myDiv"></div>)
```

#### Ajout d'éléments au DOM

Une fois que vous avez sélectionné l'élément que vous souhaitez manipuler, vous pouvez commencer à ajouter plus d'éléments à celui-ci. Par exemple, imaginons que nous avons un `<ol ref="myList">`. Nous pouvons utiliser D3 pour ajouter un nouvel élément de liste, contenant le texte « bananes ».

```js
d3.select(this.refs.myList)
    .append("li")
    .text("bananas")
```

#### Utilisation des données pour créer

Vous pouvez rendre D3 conscient de vos données en sélectionnant des éléments du DOM et en attachant les données à ceux-ci en utilisant `.data()`. D3 a une méthode appelée `.enter()`, qui est souvent utilisée pour travailler avec des données. Elle signifie que ces éléments de données doivent être ajoutés au DOM. Le contrepartie de enter, `.exit()`, est utilisée pour signifier les éléments qui n'existent plus dans les données mais existent dans le DOM. Nous pouvons l'utiliser pour supprimer ces éléments avec remove, comme dans `.exit().remove()`.

Prenons un exemple.

```js
import React, { component } from 'react'
import * as d3 from 'd3'
class App extends Component {
    const temperatureData = [ 8, 5, 13, 9, 12 ]
    d3.select(this.refs.temperatures)
        .selectAll("h2")
        .data(temperatureData)
        .enter()
            .append("h2")
            .text("New Temperature")
 
    render(<div ref="temperatures"></div>)
}
export default App
```

Cela se lit comme suit : « D3, sélectionne l'élément avec la référence 'temperatures'. Ensuite, attache temperatureData à ses éléments `<h2>`. Pour les parties des données qui ne sont pas encore représentées dans le DOM, ajoute un nouvel élément `<h2>` avec le texte 'New Temperature'. »

Attendez, maintenant il dit « New Temperature » encore et encore ! Que faire si nous voulons afficher la valeur réelle du point de données ?

#### Propriétés en tant que fonctions

Dans D3, les styles, les attributs et autres propriétés des éléments peuvent être définis en utilisant des fonctions. Refactorisons le code ci-dessus pour utiliser une fonction qui définit les textes des éléments `<h2>` à la valeur du point de données qu'ils représentent.

```js
d3.select(this.refs.temperatures)
    .selectAll("h2")
    .data(temperatureData)
    .enter()
        .append("h2")
        .text((datapoint) => datapoint + " degrees")
```

Nous pouvons utiliser une fonction fléchée pour prendre la valeur du point de données et retourner la valeur ajoutée à « degrees ». Les fonctions dans les propriétés nous permettent de nous montrer créatifs avec les éléments. Dans cet exemple de la [documentation D3](https://d3js.org/), un paragraphe reçoit une couleur aléatoire en utilisant une fonction pour définir la propriété de style de l'élément.

```js
d3.selectAll("p")
    .style("color", function() {
        return "hsl(" + Math.random() * 360 + ",100%,50%)";
    }
);
```

Vous pouvez également utiliser des conditionnelles, comme dans n'importe quelle fonction. Supposons que nous voulons définir le style d'un élément de notre liste de températures en fonction des données.

```js
d3.select(this.refs.temperatures)
    .selectAll("h2")
    .data(temperatureData)
    .enter()
        .append("h2")
        .text((datapoint) => `${datapoint} degrees`)
        .style((datapoint) => {
            if (datapoint > 10) {
                return "red"
            } else { return "blue" }     
        }) 
```

Cependant, ajouter des styles en ligne est une tâche fastidieuse, et nous aimerions utiliser des classes et des identifiants à la place afin de pouvoir définir les styles dans notre CSS. Pour définir des attributs comme les classes et les identifiants, nous utilisons `.attr()`. Le code ci-dessus pourrait être refactorisé en `.attr("class", (datapoint) => { datapoint > 10 ? "highTemperature" : "lowTemperature" }`.

#### Animation avec des transitions

Enfin, D3 facilite l'animation des transitions. Nous pourrions changer la couleur du texte en rouge.

```js
d3.select(this.ref.descr)
    .transition()
    .style("background-color", "red");
render(<p ref="descr"></p>)
```

Nous pouvons modifier l'animation pour qu'elle se produise après 1 seconde en utilisant `.duration(1000)`. Nous pouvons également utiliser des fonctions avec des transitions. Par exemple, nous pouvons faire en sorte que nos éléments apparaissent dans une transition décalée. L'exemple suivant de la documentation D3 fait apparaître des cercles un à la fois, en utilisant une fonction `delay()` qui prend `dataPoint` et `iteration` comme paramètres, et retourne l'itération multipliée par 10. L'itération fait référence à la position du point de données dans la liste des données.

```js
d3.selectAll("circle").transition()
    .duration(750)
    .delay(function(dataPoint, iteration) => iteration * 10)
    .attr("r", (dataPoint) => Math.sqrt(d * scale))
```

#### Notre premier graphique

Créons un nouveau composant. Créez un nouveau fichier, appelé `BarChart.js`. Modifiez App.js pour qu'il ressemble à ceci.

```js
import React from React
import BarChart from './BarChart'
const App = () => {
    return ( <BarChart /> )
}
```

Collez le code suivant dans `BarChart.js`. Appelez `npm start` pour démarrer l'application.

```js
import React, { Component } from 'react'
import * as d3 from 'd3'
class BarChart extends Component {
    componentDidMount() {
        const data = [ 2, 4, 2, 6, 8 ]
        this.drawBarChart(data)
    }
    drawBarChart(data)  {}
    render() { return <div ref="canvas"></div> }
}
export default BarChart
```

Nous avons un ensemble de données factices, que nous passons à la fonction de dessin en tant que paramètre. À partir de maintenant, nous travaillerons à l'intérieur de `drawBarChart()`. Tout d'abord, sélectionnez le `div` avec la référence `canvas`. À l'intérieur de `drawBarChart()`, nous ajoutons un élément `svg` à l'intérieur du `div` que nous avons référencé. Nous définissons le `svg` pour qu'il ait une largeur de 600, une hauteur de 400 et une bordure noire. Vous devriez voir cette boîte vide apparaître sur la page.

```js
const svgCanvas = d3.select(this.refs.canvas)
    .append("svg")
    .attr("width", 600)
    .attr("height", 400)
    .style("border", "1px solid black")
```

![Image](https://cdn-media-1.freecodecamp.org/images/4SGaco4vI2i7aFkKQsgwwIOYIXRaLXbHrysJ)
_Un élément SVG vide avec une bordure noire._

Ensuite, nous avons besoin de quelques barres sur notre graphique à barres. Nous sélectionnons tous les éléments `rect`, ou rectangles, du `svg`. Ensuite, nous ajoutons les données aux rectangles et utilisons enter pour entrer dans les données. Pour chaque donnée dans l'élément, nous ajoutons un rectangle avec une largeur de 40 et la hauteur de la valeur du point de données multipliée par 20.

```js
svgCanvas.selectAll("rect")
    .data(data).enter()
         .append("rect")
         .attr("width", 40)
         .attr("height", (datapoint) => datapoint * 20)
         .attr("fill", "orange")
```

![Image](https://cdn-media-1.freecodecamp.org/images/Ihtl3uCAtOkuHQdndzg7YyLabgnG2JWzF35T)
_Après avoir ajouté les rectangles avec les données au SVG._

Attendez, pourquoi semble-t-il que nous n'avons qu'un seul rectangle ? Puisque nous n'avons pas spécifié où sur le `svg` le rectangle devrait apparaître, ils se sont tous empilés à 0, 0. Ajoutons les positions x et y. Refactorisons également le code pour garder la largeur du canevas, la hauteur et l'échelle des barres dans des variables.

```js
drawBarChart(data) {
const canvasHeight = 400
const canvasWidth = 600
const scale = 20
const svgCanvas = d3.select(this.refs.canvas)
    .append("svg")
    .attr("width", canvasWidth)
    .attr("height", canvasHeight)
    .style("border", "1px solid black")
svgCanvas.selectAll("rect")
    .data(data).enter()
        .append("rect")
        .attr("width", 40)
        .attr("height", (datapoint) => datapoint * scale)
        .attr("fill", "orange")
        .attr("x", (datapoint, iteration) => iteration * 45)
        .attr("y", (datapoint) => canvasHeight - datapoint * scale)
}
```

Maintenant, nous définissons la position x à l'itération multipliée par 45, ce qui est 5 de plus que la largeur de la colonne, laissant un petit espace entre les colonnes. La position y est un peu plus délicate. Nous la définissons à la hauteur du canevas moins la hauteur de la barre, qui est la valeur du point de données multipliée par 20. Maintenant, notre graphique ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/JwFsJSO0BpGCxlEq6GWWnVruQvzGiLJb26sC)
_Après avoir défini les positions x et y des rectangles._

Pour donner à nos barres une touche finale, ajoutons les valeurs des points de données aux barres. Nous ajoutons quelques éléments de texte au `svg` et définissons leur attribut x à 10 unités de plus que le point de départ de chaque barre. Nous définissons l'attribut y à 10 unités de moins que le point de départ de la barre.

```js
svgCanvas.selectAll("text")
    .data(data).enter()
        .append("text")
        .attr("x", (dataPoint, i) => i * 45 + 10)
        .attr("y", (dataPoint, i) => canvasHeight - dataPoint * scale - 10)
        .text(dataPoint => dataPoint)
```

![Image](https://cdn-media-1.freecodecamp.org/images/As7X63uSvkE7VEzy56P2toGboiIqFbTEPf5O)
_Ajout d'étiquettes de texte à nos barres._

Maintenant, les textes se trouvent juste au-dessus des barres. Vous pouvez continuer à travailler avec le graphique, ajouter des styles (en utilisant `.attr("class", "bar")`) et ajouter un fichier CSS. Vous pouvez également ajouter un axe au graphique et ajouter une info-bulle lors du survol de la barre.

**Soyez créatif et amusez-vous !**

Travailler avec D3 peut sembler difficile au début. Une fois que vous avez maîtrisé les bases, cela devient un outil puissant pour exprimer et visualiser des données. Je recommande d'utiliser D3 plutôt que de choisir une bibliothèque de graphiques prête à l'emploi, car elle permet des pièces plus personnelles et modifiables.

Enfin, apprendre D3 est également un bon moyen de devenir fluide dans la traversée et la manipulation du DOM. Comprendre le DOM est souvent une qualité que les recruteurs recherchent chez les développeurs front-end.

#### Ressources :

[Tutoriels D3](https://github.com/d3/d3/wiki/Tutorials) suggérés par D3

[Tutoriel React de la documentation React](https://reactjs.org/tutorial/tutorial.html)