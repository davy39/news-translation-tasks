---
title: React - Changer le CSS en ligne conditionnellement en fonction de l'état du
  composant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/react-change-inline-css-conditionally-based-on-component-state
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a95740569d1a4ca267a.jpg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: React - Changer le CSS en ligne conditionnellement en fonction de l'état
  du composant
seo_desc: 'If you''re having trouble with freeCodeCamp''s Change Inline CSS Conditionally
  Based on Component State challenge, you''re probably not alone.

  In this challenge, you need to add code to change some inline CSS conditionally
  based on the state of a React ...'
---

Si vous avez des difficultés avec le défi de freeCodeCamp [Change Inline CSS Conditionally Based on Component State](https://www.freecodecamp.org/learn/front-end-libraries/react/change-inline-css-conditionally-based-on-component-state), vous n'êtes probablement pas seul.

Dans ce défi, vous devez ajouter du code pour changer certains CSS en ligne conditionnellement en fonction de l'état d'un composant React.

Lorsque vous accédez pour la première fois au défi, voici le code que vous verrez :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line

    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

Remarquez qu'un objet de style en ligne, `inputStyle`, a déjà été déclaré avec un style par défaut.

Votre objectif dans ce défi est de mettre à jour `inputStyle` afin que la bordure de l'entrée soit `3px solid red` lorsqu'il y a plus de 15 caractères dans l'entrée. Notez que le texte dans la zone de saisie est enregistré dans l'état du composant sous `input` :

```jsx
...
this.state = {
  input: ''
};
...
```

## Presque, mais pas tout à fait

Imaginez que, après avoir lu la description et les instructions, vous arrivez à ceci :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

Mais lorsque vous essayez de soumettre cela, cela ne passe pas tous les tests. Examinons de plus près ce qui se passe.

## Solutions

### Utilisation d'une instruction `if`

Déclarer `char` est correct, mais examinez de plus près la condition `if` :

```jsx
if(this.state.input > char) {
  inputStyle = {
    border:'3px solid red'
  }
}  
```

Rappelez-vous que `this.state.input` est la valeur de la zone de saisie et est une chaîne de caractères. Par exemple, cela pourrait être "testing testing 1, 2, 3".

Si vous entrez "testing testing 1, 2, 3" dans la zone de texte et affichez `this.state.input` dans la console :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    console.log(this.state.input);
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

Vous verrez `testing testing 1, 2, 3` dans la console.

De plus, si vous affichez `this.state.input > char` dans la console, vous verrez qu'il évalue à `false` :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    console.log(this.state.input > char);
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

En termes simples, vous ne pouvez pas comparer directement une chaîne de caractères (`this.state.input`) à `char`, qui est un nombre.

Au lieu de cela, appelez `.length` sur `this.state.input` pour obtenir la longueur de la chaîne et comparez cela à `count` :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    if(this.state.input.length > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

Puisque la longueur de la chaîne "testing testing 1, 2, 3" est de 23 caractères (y compris les espaces et les virgules), la bordure de la zone de saisie deviendra rouge :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-53.png)

### Utilisation d'un opérateur ternaire

Un [opérateur ternaire ou conditionnel](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) est comme une instruction `if...else` sur une ligne, et peut aider à raccourcir considérablement votre code.

Revenez à votre solution et supprimez tout sauf la variable `char` :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line

    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

Prenez maintenant la condition que vous avez utilisée dans votre instruction `if` précédente et utilisez-la comme première partie de la condition ternaire : `this.state.input.length > char ?  :  ;`

Tout ce qui se trouve entre `?` et `:` indique ce qui se passe si l'instruction précédente est vraie. Vous pouvez simplement copier le code qui se trouvait à l'intérieur de votre instruction `if` auparavant : `this.state.input.length > char ? inputStyle = { border:'3px solid red' } :  ;`

Maintenant, vous devez gérer la partie `else` de l'opérateur ternaire, qui est tout ce qui se trouve entre `:` et `;`.

Bien que vous n'ayez pas utilisé d'instruction `else` dans votre première solution, vous avez effectivement utilisé `inputStyle` tel quel. Utilisez donc `inputStyle` de la manière dont il est déclaré plus tôt dans votre code : `this.state.input.length > char ? inputStyle = { border:'3px solid red' } : inputStyle;`

Votre solution complète devrait ressembler à ceci :

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    this.state.input.length > char ? inputStyle = { border:'3px solid red' } : inputStyle;
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

Et c'est tout — vous devriez pouvoir passer le défi ! Maintenant, allez de l'avant et stylez conditionnellement les composants React à votre guise.