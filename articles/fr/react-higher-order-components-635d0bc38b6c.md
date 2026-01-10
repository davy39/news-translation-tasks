---
title: Comment utiliser les composants d'ordre supérieur de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-09T03:51:22.000Z'
originalURL: https://freecodecamp.org/news/react-higher-order-components-635d0bc38b6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jnqXL4Q-iW0qxodFDTxyFQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les composants d'ordre supérieur de React
seo_desc: 'By Adam Recvlohe

  When React first hit the scene, it brought with it a new way of developing front-end
  architectures. It was regarded as the “View” in Model-View-Controller.

  Over time, core contributors to the React ecosystem have latched onto the con...'
---

Par Adam Recvlohe

Lorsque React est apparu pour la première fois, il a apporté avec lui une nouvelle façon de développer des architectures front-end. Il était considéré comme la "Vue" dans Modèle-Vue-Contrôleur.

Avec le temps, les contributeurs principaux de l'écosystème React se sont attachés au modèle conteneur/présentation.

Dans cet article, vous en apprendrez davantage sur le modèle conteneur/présentation et sur la manière de l'utiliser pour créer des composants React.

Avant d'aller plus loin, clarifions quelques termes techniques :

* Un conteneur est un composant qui récupère et/ou transforme des données.
* Un composant de présentation présente/affiche les données qui lui sont passées via ses props. Rien de plus.
* Un conteneur agit comme un composant d'ordre supérieur. La composition de composants d'ordre supérieur ensemble vous permet de séparer ces deux couches. Cela vous empêche de mélanger votre couche de présentation avec une logique inutile.

Si vous le souhaitez, vous pouvez suivre ce tutoriel en utilisant ESNextbin.

Après avoir navigué vers cette page, en haut, vous devriez voir trois onglets : **CODE**, **HTML** et **PACKAGE**. Cliquez sur **PACKAGE**. Après être passé à cet onglet, ajoutez _react_ et _react-dom_ comme _dependencies_.

```
{ "name": "esnextbin-sketch", "version": "0.0.0", "dependencies": {   "react" : "latest",   "react-dom": "latest" }}
```

Maintenant, cliquez sur l'onglet **CODE**, puis importez _react_ et **render** depuis _react-dom_.

```
import { default as React } from 'react'
import { render } from 'react-dom'
```

Maintenant, créons un composant fonctionnel sans état qui rend 'Bonjour, le monde !'

```
const Presentational = () => <div>Bonjour, le monde !</div>
```

Ensuite, vous devez simplement monter ce composant dans le DOM en utilisant _render_.

```
render(<Presentational />, document.querySelector('#root'))
```

Vous n'avez pas encore créé l'élément **root** dans le **HTML**, alors faisons cela maintenant. Tout ce que vous faites est d'ajouter une _div_ avec l'_id_ **root**.

```
<!doctype html><html><head> <meta charset="utf-8"> <title>ESNextbin Sketch</title> <! — put additional styles and scripts here →</head><body> // Notice something different <div id='root'></div></body></html>
```

Maintenant, le moment de vérité. Cliquez sur **EXECUTE** dans le coin supérieur droit de la page. Vous devriez voir _Bonjour, le monde !_ à l'écran.

Vous avez maintenant un composant de présentation. Mais vous avez également besoin d'un composant conteneur pour récupérer vos données.

Créons un composant conteneur au-dessus du composant de présentation. Pour créer le conteneur, vous utiliserez le composant de classe de React. Pour cette raison, vous devrez l'importer en haut de la page.

```
import { default as React, Component } from 'react'
```

À ce stade, vous pouvez vous atteler à la création du composant conteneur.

```
class Container extends Component {  state = {   data: [] }  componentDidMount() {   fetch('https://fcctop100.herokuapp.com/api/fccusers/top/alltime')   .then(response => response.json())   .then(data => this.setState({ data })) }  render() {   return <Presentational data={this.state.data} /> }}
```

En haut, vous avez l'état qui est un tableau vide. Vous utilisez une méthode de cycle de vie appelée _componentDidMount_ où vous allez récupérer les données.

Lorsque la réponse revient, vous mettez ensuite à jour l'état avec les données. Les données sont ensuite passées en tant que prop au composant de présentation. Cela signifie que vous devrez également mettre à jour votre composant de présentation.

```
const Presentational = ({ data }) =>   <div>{JSON.stringify(data)}</div>
```

Ici, j'utilise la déstructuration pour extraire **data** de l'objet props. Sinon, cela ressemblerait à ceci :

```
const Presentational = props =>   <div>{JSON.stringify(props.data)}</div>
```

Ces changements vous obligent à mettre à jour le composant qui est monté. Vous devez maintenant rendre le composant conteneur.

```
render(<Container />, document.querySelector('#root'))
```

Lorsque vous cliquez sur **EXECUTE**, vous devriez voir une grande quantité de données déborder sur votre écran. Oh là là !

Ce que vous avez fait ici, c'est abstraire le composant conteneur et tout ce qu'il fait. Mais ce n'est pas flexible. Vous devez placer votre composant de présentation à l'intérieur du conteneur. Y a-t-il une autre façon de faire cela qui soit plus flexible ? Entrez dans le composant d'ordre supérieur.

Un composant d'ordre supérieur est une fonction qui prend un composant et retourne un nouveau composant. À quoi cela ressemblerait-il en pratique. Créons une fonction qui prend un composant et retourne un nouveau composant avec les données de l'API FCC. Vous allez mettre à jour le composant conteneur pour faire cela.

```
const container = Presentational =>  class extends Component {  state = {   data: [] }  componentDidMount() {   fetch('https://fcctop100.herokuapp.com/api/fccusers/top/alltime')   .then(response => response.json())   .then(data => this.setState({ data })) }  render() {   return <Presentational data={this.state.data} /> }}
```

Rien de trop différent ici. Il y a cependant une étape supplémentaire que vous devez effectuer. Vous devez composer ce conteneur et ce composant de présentation ensemble. Je ne fais qu'appeler le conteneur avec le composant de présentation comme argument. Cela est ajouté juste en dessous de votre composant de présentation.

```
const HigherOrderComponent = container(Presentational)
```

Maintenant, tout ce que vous avez à faire est de rendre le composant d'ordre supérieur.

```
render(<HigherOrderComponent />, document.querySelector('#root'))
```

Vous voyez ce que vous avez fait là ? Maintenant, vous pouvez utiliser le conteneur avec n'importe quel composant, pas seulement le composant de présentation !

Allons un peu plus loin. Appelons une autre fonction qui indique au composant conteneur quelles données récupérer. Je pense que cela rendrait le conteneur encore plus flexible.

Le nouveau conteneur ressemblera à quelque chose comme ceci :

```
const container = endpoint => Presentational =>  class extends Component {  state = {   data: [] }  componentDidMount() {   fetch(endpoint)     .then(response => response.json())     .then(data => this.setState({ data })) }  render() {   return <Presentational data={this.state.data} /> }}
```

Maintenant, vous devrez mettre à jour le composant d'ordre supérieur pour gérer le nouvel appel à l'endpoint.

```
const HigherOrderComponent = container(  'https://fcctop100.herokuapp.com/api/fccusers/top/alltime')(Presentational)
```

Si cela vous semble un peu étrange, vous avez bon œil. Et si vous pouviez abstraire cela encore plus loin ? Entrez _recompose_ !

Faisons une pause pour un moment et couvrons l'idée de compose. Pour comprendre compose, vous devez comprendre le mapping.

Le mapping en programmation informatique est lorsque vous prenez une valeur et la transformez en une autre valeur. Ce qui est essentiellement chaque fonction jamais créée ! Laissez-moi vous donner un exemple pour bonne mesure.

```
function double(x) {   return x * 2}
```

```
const doubled = double(2)
```

Maintenant, disons que je veux faire une autre transformation, par exemple triple. Comment ferais-je cela ?

```
function triple(x) {   return x * 3 }
```

```
function double(x) {   return x * 2}
```

```
const messedAroundAndGotATripleDouble = triple(double(2))
```

Assez simple, n'est-ce pas ? Et si je voulais faire une autre transformation, et une autre, et une autre. Cela deviendrait assez long. Avec l'aide d'une fonction compose, vous pouvez rendre le code non seulement plus lisible mais aussi plus composable.

```
function compose(f, g) {   return function(x) {     return f(g(x))  }}
```

```
function triple(x) {   return x * 3 }
```

```
function double(x) {   return x * 2}
```

```
const tripleThenDouble = compose(triple, double)
```

```
const messedAroundAndGotATripleDouble = tripleThenDouble(2)
```

C'est un exemple simple, mais il montre comment vous pouvez faire de nombreuses transformations sur la même valeur initiale.

Maintenant, imaginez que la valeur initiale est le composant de présentation tandis que le conteneur est l'une des fonctions qui transforme la valeur initiale. L'esprit soufflé !

Pour commencer à utiliser _recompose_, vous devez intégrer la bibliothèque _recompose_. Sous **PACKAGES**, ajoutons la bibliothèque _recompose_.

```
{ "name": "esnextbin-sketch", "version": "0.0.0", "dependencies": {   "react": "15.3.2",   "react-dom": "15.3.2",   "recompose": "latest",   "babel-runtime": "6.11.6" }}
```

Revenons au **CODE** et importons **compose** depuis _recompose_.

```
import { compose } from 'recompose'
```

Ensuite, vous pouvez utiliser compose pour abstraire davantage le composant d'ordre supérieur.

```
const HigherOrderComponent = compose( container(  'https://fcctop100.herokuapp.com/api/fccusers/top/alltime' ))
```

Et vous pouvez être plus déclaratif sur ce que fait l'ensemble du composant.

```
const FetchAndDisplayFCCData = HigherOrderComponent(Presentational)
```

```
render(<FetchAndDisplayFCCData />, document.querySelector('#root'))
```

Cela vous a enfin permis de créer des composants qui sont polyvalents et flexibles. Vous pouvez même tester vos composants de présentation séparément des composants d'ordre supérieur. Les composants d'ordre supérieur FTW !

Pour le plaisir, mettons à jour le composant de présentation pour qu'il rende une liste d'éléments au lieu d'un gros bloc de données.

```
const Presentational = ({ data }) =>  <ul>   {data.map((v, k) =>      <li key={k}>       {v.username}     </li>   )} </ul>
```

Ouf ! C'était beaucoup. Si vous voulez voir le produit final, jetez un œil au gist que j'ai créé [ici](https://gist.github.com/arecvlohe/c5005643ea4fcb9637ccd9f60b98d305).

Pour plus d'informations, visitez la grande bibliothèque utilitaire React d'Andrew Clark appelée _recompose_ pour en savoir plus !

[**acdlite/recompose**](https://github.com/acdlite/recompose)  
[_recompose - A React utility belt for function components and higher-order components._github.com](https://github.com/acdlite/recompose)