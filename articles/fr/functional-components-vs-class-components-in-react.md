---
title: Composants Fonctionnels vs Composants de Classe dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-17T00:16:00.000Z'
originalURL: https://freecodecamp.org/news/functional-components-vs-class-components-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ea8740569d1a4ca3e61.jpg
tags:
- name: React
  slug: react
seo_title: Composants Fonctionnels vs Composants de Classe dans React
seo_desc: 'There are mainly two components in React:


  Functional Components

  Class Components


  Functional Components


  Functional components are basic JavaScript functions. These are typically arrow
  functions but can also be created with the regular function keyw...'
---

Il existe principalement deux types de composants dans React :

* Composants Fonctionnels
* Composants de Classe

## **Composants Fonctionnels**

* Les composants fonctionnels sont des fonctions JavaScript basiques. Ce sont généralement des fonctions fléchées, mais elles peuvent également être créées avec le mot-clé `function` classique.
* Parfois appelés composants "bêtes" ou "sans état", car ils acceptent simplement des données et les affichent sous une certaine forme ; c'est-à-dire qu'ils sont principalement responsables du rendu de l'interface utilisateur.
* Les méthodes du cycle de vie de React (par exemple, `componentDidMount`) ne peuvent pas être utilisées dans les composants fonctionnels.
* Il n'y a pas de méthode de rendu utilisée dans les composants fonctionnels.
* Ils sont principalement responsables de l'UI et sont généralement uniquement présentationnels (par exemple, un composant Button).
* Les composants fonctionnels peuvent accepter et utiliser des props.
* Les composants fonctionnels doivent être privilégiés si vous n'avez pas besoin d'utiliser l'état de React.

```js
import React from "react";

const Person = props => (
  <div>
    <h1>Bonjour, {props.name}</h1>
  </div>
);

export default Person;
```

## **Composants de Classe**

* Les composants de classe utilisent la syntaxe de classe ES6 et étendent la classe `Component` de React.
* Parfois appelés composants "intelligents" ou "avec état", car ils tendent à implémenter la logique et l'état.
* Les méthodes du cycle de vie de React peuvent être utilisées à l'intérieur des composants de classe (par exemple, `componentDidMount`).
* Vous passez les props aux composants de classe et y accédez avec `this.props`

```js
import React, { Component } from "react";

class Person extends Component {
  constructor(props){
    super(props);
    this.state = {
      myState: true;
    }
  }
  
  render() {
    return (
      <div>
        <h1>Bonjour Person</h1>
      </div>
    );
  }
}

export default Person;
```

## **Plus d'Informations**

* [Composants React](https://reactjs.org/docs/components-and-props.html)
* [Composants fonctionnels vs composants de classe](https://react.christmas/16)
* [Composants Fonctionnels avec État vs sans État dans React](https://code.tutsplus.com/tutorials/stateful-vs-stateless-functional-components-in-react--cms-29541)
* [État et Cycle de Vie](https://reactjs.org/docs/state-and-lifecycle.html)