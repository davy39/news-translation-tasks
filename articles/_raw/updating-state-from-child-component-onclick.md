---
title: Updating State From Child Component Onclick
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
seo_title: null
seo_desc: 'How to update the state of a parent component from a child component is
  one of the most commonly asked React questions.

  Imagine you''re trying to write a simple recipe box application, and this is your
  code so far:

  import React from "react";

  import Re...'
---

How to update the state of a parent component from a child component is one of the most commonly asked React questions.

Imagine you're trying to write a simple recipe box application, and this is your code so far:

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

Eventually you want `handleChange` to capture what the user enters and update specific recipes.

But when you try to run your app, you see a lot of errors in the terminal and dev console. Let's take a closer look at what's going on.

## Fixing errors

First in `handleSubmit`, `setState` should be `this.setState`:

```jsx
handleSubmit() {
  const newRecipe = this.state.recipelist[0].recipe;
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

You're already prop drilling, or passing things from the parent `RecipeBox` component to its child `EditList` properly. But when someone enters text into the input box and clicks "Submit", the state isn't updated the way you expect.

## How to update the state from a child component

Here you're running into issues because you're trying to update the state of a nested array (`recipeList[0].recipe: newRecipe`). That won't work in React.

Instead, you need to create a copy of the full `recipeList` array, modify the value of `recipe` for the element you want to update in the copied array, and assign the modified array back to `this.state.recipeList`.

First, use the spread syntax to create a copy of `this.state.recipeList`:

```jsx
handleSubmit() {
  const recipeList = [...this.state.recipeList];
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

Then update the recipe for the element you want to update. Let's do the first element as a proof of concept:

```jsx
handleSubmit() {
  const recipeList = [...this.state.recipeList];
  recipeList[0].recipe = this.state.input;
  this.setState({
    recipeList[0].recipe: newRecipe
  });
}
```

Finally, update the current `recipeList` with your new copy. Also, set `input` to an empty string so the textbox is empty after users click "Submit":

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

