---
title: Comment effacer les valeurs de saisie d'un formulaire dynamique dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-clear-input-values-of-dynamic-form-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a92740569d1a4ca2665.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
- name: toothbrush
  slug: toothbrush
seo_title: Comment effacer les valeurs de saisie d'un formulaire dynamique dans React
seo_desc: 'There''s a lot to consider when working on a React application, especially
  when they involve forms. Even if you''re able to create a submit button and update
  your app''s state the way you want, clearing the forms can be difficult.

  Say your application h...'
---

Il y a beaucoup de choses à considérer lors du développement d'une application React, surtout lorsqu'elles impliquent des formulaires. Même si vous êtes capable de créer un bouton de soumission et de mettre à jour l'état de votre application comme vous le souhaitez, effacer les formulaires peut être difficile.

Disons que votre application a des formulaires dynamiques comme ceci :

```jsx
import React from "react";
import ReactDOM from "react-dom";
import Cart from "./Cart";

import "./styles.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Items: [
        {
          name: "item1",
          description: "item1",
          group: "groupA",
          dtype: "str"
        },
        {
          name: "item2",
          description: "item2",
          group: "groupA",
          dtype: "str"
        },
        {
          name: "item3",
          description: "item3",
          group: "groupB",
          dtype: "str"
        },
        {
          name: "item4",
          description: "item4",
          group: "groupB",
          dtype: "str"
        }
      ],
      itemvalues: [{}]
    };
    this.onChangeText = this.onChangeText.bind(this);
    this.handleReset = this.handleReset.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.findFieldIndex = this.findFieldIndex.bind(this);
    this.trimText = this.trimText.bind(this);
  }

  onChangeText = e => {
    const valuesCopy = [...this.state.itemvalues];
    //debugger;

    // obtenir la valeur de data-group
    const itemvalue = e.target.dataset.group;

    if (!valuesCopy[0][itemvalue]) {
      valuesCopy[0][itemvalue] = [];
    }

    const itemvalues = valuesCopy[0][itemvalue];
    const index = this.findFieldIndex(itemvalues, e.target.name);

    if (index < 0) {
      valuesCopy[0][itemvalue] = [
        ...itemvalues,
        { [e.target.name]: e.target.value.split(",").map(this.trimText) }
      ];
    } else {
      // mettre à jour la valeur
      valuesCopy[0][itemvalue][index][e.target.name] = e.target.value
        .split(",")
        .map(this.trimText);
    }

    // console.log(itemsCopy);

    this.setState({ itemvalues: valuesCopy });
  };
  findFieldIndex = (array, name) => {
    return array.findIndex(item => item[name] !== undefined);
  };
  trimText(str) {
    return str.trim();
  }

  handleReset = () => {
    this.setState({
      itemvalues: [{}]
    });
  };

  handleSubmit = () => {
    console.log(this.state.itemvalues);
  };

  render() {
    return (
      <Cart
        Items={this.state.Items}
        handleSubmit={this.handleSubmit}
        handleReset={this.handleReset}
        onChangeText={this.onChangeText}
      />
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
```

```jsx
import React from "react";
import Form from "./Form";

const Cart = props => {
  return (
    <div>
      <Form Items={props.Items} onChangeText={props.onChangeText} />

      <button onClick={props.handleSubmit}>Submit</button>
      <button onClick={props.handleReset}>Reset</button>
    </div>
  );
};

export default Cart;
```

```jsx
import React from "react";

const Form = props => {
  return (
    <div>
      {props.Items.map((item, index) => (
        <input
          name={item.name}
          placeholder={item.description}
          data-type={item.dtype}
          data-group={item.group}
          onChange={e => props.onChangeText(e)}
          key={index}
        />
      ))}
    </div>
  );
};
export default Form;
```

Et des cases de saisie simples sont rendues sur la page :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-56.png)

Lorsque l'utilisateur entre du texte dans l'une des cases de saisie, il est enregistré dans l'état de l'application en groupes comme ceci :

```
Itemvalues:
  0:
    groupA: 
            item1: itemvalue1
            item2: itemvalue2
    groupB: 
            item3: itemvalue3
            item4: itemvalue4
```

C'est assez compliqué, mais vous avez réussi à le faire fonctionner.

Dans `handleReset`, vous êtes capable de réinitialiser `itemvalues` à un état nul lorsque le bouton "Reset" est pressé :

```js
handleReset = () => {
  this.setState({
    itemvalues: [{}]
  });
};
```

Mais le problème est que le texte n'est pas effacé de toutes les cases de saisie :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-16-21-32.gif)

Vous avez déjà géré le stockage du texte réel dans l'état, voici donc une méthode simple pour effacer le texte de toutes les cases de saisie.

## Comment effacer les valeurs de toutes les saisies

Au début de `handleReset`, utilisez `document.querySelectorAll('input')` pour sélectionner tous les éléments de saisie sur la page :

```js
handleReset = () => {
  document.querySelectorAll('input');
  this.setState({
    itemvalues: [{}]
  });
};
```

`document.querySelectorAll('input')` retourne une `NodeList`, qui est un peu différente d'un tableau, donc vous ne pouvez pas utiliser de méthodes de tableau utiles dessus.

Pour la transformer en tableau, passez `document.querySelectorAll('input')` à `Array.from()` :

```js
handleReset = () => {
  Array.from(document.querySelectorAll('input'));
  this.setState({
    itemvalues: [{}]
  });
};
```

Maintenant, tout ce que vous avez à faire est de parcourir chaque saisie et de définir son attribut `value` à une chaîne vide. La méthode `forEach` est un bon candidat pour cela :

```js
handleReset = () => {
  Array.from(document.querySelectorAll("input")).forEach(
    input => (input.value = "")
  );
  this.setState({
    itemvalues: [{}]
  });
};
```

Maintenant, lorsque l'utilisateur appuie sur le bouton "Reset", la valeur de chaque saisie est également effacée :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-16-21-42.gif)