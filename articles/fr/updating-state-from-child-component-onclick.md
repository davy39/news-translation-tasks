---
title: Mettre à jour l'état depuis un composant enfant au clic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/updating-state-from-child-component-onclick
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a94740569d1a4ca2673.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
- name: toothbrush
  slug: toothbrush
seo_title: Mettre à jour l'état depuis un composant enfant au clic
seo_desc: 'How to update the state of a parent component from a child component is
  one of the most commonly asked React questions.

  Imagine you''re trying to write a simple recipe box application, and this is your
  code so far:

  import React from "react";

  import Re...'
---

Comment mettre à jour l'état d'un composant parent depuis un composant enfant est l'une des questions les plus fréquemment posées sur React.

Imaginez que vous essayez d'écrire une application simple de boîte à recettes, et voici votre code jusqu'à présent :

```jsx
import React from "react";
import ReactDOM from "react-dom";

import RecipeBox from "./RecipeBox";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <RecipeBox />
  </React.StrictMode>,
  rootElement
);
```

```jsx
import React from "react";

export default class RecipeBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: "",
      recipeList: [
        {
          recipe: "Tacos",
          directions: "make tacos",
          ingredients: ["meat"]
        },
        {
          recipe: "pizza",
          directions: "bake",
          ingredients: ["dough"]
        }
      ]
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      input: event.target.value
    });
  }

  handleSubmit() {
    const newRecipe = this.state.recipelist[0].recipe;
    setState({
      recipeList[0].recipe: newRecipe
    });
  }

  render() {
    const ITEMS = this.state.recipeList.map(({ directions }) => (
      <li>{directions}</li>
    ));
    return (
      <div>
        <EditList
          input={this.state.input}
          handleChange={this.handleChange}
          onSubmit={this.handleSubmit}
        />
        <ul>{ITEMS}</ul>
      </div>
    );
  }
}

class EditList extends React.Component {
  render() {
    return (
      <div>
        <input
          type='text'
          value={this.props.input}
          onChange={this.props.handleChange}
        />
        <button onClick={this.props.onSubmit}>Submit</button>
      </div>
    );
  }
}
```

Finalement, vous voulez que `handleChange` capture ce que l'utilisateur saisit et met à jour des recettes spécifiques.

Mais lorsque vous essayez d'exécuter votre application, vous voyez beaucoup d'erreurs dans le terminal et la console de développement. Examinons de plus près ce qui se passe.

## Correction des erreurs

D'abord dans `handleSubmit`, `setState` devrait être `this.setState` :

```jsx
handleSubmit() {
  const newRecipe = this.state.recipelist[0].recipe;
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

Vous faites déjà du "prop drilling", ou passez des éléments du composant parent `RecipeBox` à son enfant `EditList` correctement. Mais lorsque quelqu'un saisit du texte dans la zone de saisie et clique sur "Submit", l'état n'est pas mis à jour comme vous l'attendez.

## Comment mettre à jour l'état depuis un composant enfant

Ici, vous rencontrez des problèmes parce que vous essayez de mettre à jour l'état d'un tableau imbriqué (`recipeList[0].recipe: newRecipe`). Cela ne fonctionnera pas dans React.

Au lieu de cela, vous devez créer une copie du tableau complet `recipeList`, modifier la valeur de `recipe` pour l'élément que vous souhaitez mettre à jour dans le tableau copié, et assigner le tableau modifié à `this.state.recipeList`.

D'abord, utilisez la syntaxe de décomposition pour créer une copie de `this.state.recipeList` :

```jsx
handleSubmit() {
  const recipeList = [...this.state.recipeList];
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

Ensuite, mettez à jour la recette pour l'élément que vous souhaitez modifier. Faisons le premier élément comme preuve de concept :

```jsx
handleSubmit() {
  const recipeList = [...this.state.recipeList];
  recipeList[0].recipe = this.state.input;
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

Enfin, mettez à jour le `recipeList` actuel avec votre nouvelle copie. De plus, définissez `input` sur une chaîne vide pour que la zone de texte soit vide après que les utilisateurs aient cliqué sur "Submit" :

```jsx
handleSubmit() {
  const recipeList = [...this.state.recipeList];
  recipeList[0].recipe = this.state.input;
  this.setState({
    recipeList,
    input: ""
  });
}
```