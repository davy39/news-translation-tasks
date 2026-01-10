---
title: Comment écrire de meilleurs composants React
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-01-20T19:07:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/modern_way-1.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment écrire de meilleurs composants React
seo_desc: 'Many features were added to JavaScript in ES6. And these changes help developers
  write code that is short and easy to understand and maintain.

  When you use create-react-app to create a React App, you already have support for
  these changes. This is be...'
---

De nombreuses fonctionnalités ont été ajoutées à JavaScript dans ES6. Et ces changements aident les développeurs à écrire du code qui est court et facile à comprendre et à maintenir.

Lorsque vous utilisez [create-react-app](https://github.com/facebook/create-react-app) pour créer une application React, vous avez déjà le support pour ces changements. Cela est dû au fait qu'il utilise Babel.js pour convertir le code ES6+ en code ES5 que tous les navigateurs comprennent.

Dans cet article, nous allons explorer diverses façons d'écrire du code React plus court, plus simple et plus facile à comprendre. Alors, commençons.

Jetez un coup d'œil à la démonstration Code Sandbox ci-dessous :

%[https://codesandbox.io/s/quirky-chebyshev-zff8p]

Ici, nous avons deux zones de texte d'entrée qui prennent les entrées des utilisateurs, et deux boutons qui calculent l'addition et la soustraction des nombres fournis en entrée.

## Éviter de lier manuellement les gestionnaires d'événements

Comme vous le savez dans React, lorsque nous attachons un gestionnaire d'événements comme `onClick` ou `onChange` ou tout autre gestionnaire d'événements comme ceci :

```js
<input
  ...
  onChange={this.onFirstInputChange}
/>

```

alors, la fonction de gestionnaire (onFirstInputChange) ne conserve pas la liaison de `this`.

Ce n'est pas un problème avec React, mais c'est ainsi que fonctionnent les gestionnaires d'événements JavaScript.

Nous devons donc utiliser la méthode `.bind` pour lier correctement `this` comme ceci :

```js
constructor(props) {
  // du code
  this.onFirstInputChange = this.onFirstInputChange.bind(this);
  this.onSecondInputChange = this.onSecondInputChange.bind(this);
  this.handleAdd = this.handleAdd.bind(this);
  this.handleSubtract = this.handleSubtract.bind(this);
}

```

Les lignes de code ci-dessus maintiendront la liaison de `this` de la classe correctement à l'intérieur des fonctions de gestionnaire.

Mais ajouter un nouveau code de liaison pour chaque nouveau gestionnaire d'événements est fastidieux. Heureusement, nous pouvons le corriger en utilisant la syntaxe des propriétés de classe.

L'utilisation des propriétés de classe nous permet de définir des propriétés directement à l'intérieur de la classe.

Create-react-app utilise en interne le plugin `@babel/babel-plugin-transform-class-properties` pour Babel version >= 7 et le plugin `babel/plugin-proposal-class-properties` pour Babel version <7, donc vous n'avez pas à le configurer manuellement.

Pour l'utiliser, nous devons convertir les fonctions de gestionnaire d'événements en syntaxe de fonction fléchée.

```js
onFirstInputChange(event) {
  const value = event.target.value;
  this.setState({
    number1: value
  });
}

```

Le code ci-dessus peut être écrit comme suit :

```js
onFirstInputChange = (event) => {
  const value = event.target.value;
  this.setState({
    number1: value
  });
}

```

De manière similaire, nous pouvons convertir les trois autres fonctions :

```js
onSecondInputChange = (event) => {
 // votre code
}

handleAdd = (event) => {
 // votre code
}

handleSubtract = (event) => {
 // votre code
}

```

De plus, il n'est pas nécessaire de lier les gestionnaires d'événements dans le constructeur. Nous pouvons donc supprimer ce code. Maintenant, le constructeur ressemblera à ceci :

```js
constructor(props) {
  super(props);

  this.state = {
    number1: "",
    number2: "",
    result: "",
    errorMsg: ""
  };
}

```

Nous pouvons le simplifier encore davantage. La syntaxe des propriétés de classe nous permet de déclarer n'importe quelle variable directement à l'intérieur de la classe, donc nous pouvons complètement supprimer le constructeur et déclarer l'état comme une partie de la classe, comme montré ci-dessous :

```js
export default class App extends React.Component {
  state = {
    number1: "",
    number2: "",
    result: "",
    errorMsg: ""
  };

  render() { }
}

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/trusting-dust-ukvx2](https://codesandbox.io/s/trusting-dust-ukvx2)

Si vous consultez la démonstration Code Sandbox ci-dessus, vous verrez que la fonctionnalité fonctionne toujours comme avant.

Mais l'utilisation des propriétés de classe rend le code beaucoup plus simple et facile à comprendre.

De nos jours, vous trouverez du code React écrit comme ceci.

## Utiliser une seule méthode de gestionnaire d'événements

Si vous inspectez le code ci-dessus, vous verrez que pour chaque champ de saisie, nous avons une fonction de gestionnaire d'événements séparée, `onFirstInputChange` et `onSecondInputChange`.

Si le nombre de champs de saisie augmente, le nombre de fonctions de gestionnaire d'événements augmente également, ce qui n'est pas bon.

Par exemple, si vous créez une page d'inscription, il y aura de nombreux champs de saisie. Donc, créer une fonction de gestionnaire séparée pour chaque champ de saisie n'est pas réalisable.

Changeons cela.

Pour créer un seul gestionnaire d'événements qui gérera tous les champs de saisie, nous devons donner un nom unique à chaque champ de saisie qui correspond exactement aux noms des variables d'état correspondantes.

Nous avons déjà cette configuration. Les noms `number1` et `number2` que nous avons donnés aux champs de saisie sont également définis dans l'état. Donc, changeons la méthode de gestionnaire des deux champs de saisie en `onInputChange` comme ceci :

```js
<input
  type="text"
  name="number1"
  placeholder="Entrez un nombre"
  onChange={this.onInputChange}
/>

<input
  type="text"
  name="number2"
  placeholder="Entrez un nombre"
  onChange={this.onInputChange}
/>

```

et ajoutez un nouveau gestionnaire d'événements `onInputChange` comme ceci :

```js
onInputChange = (event) => {
  const name = event.target.name;
  const value = event.target.value;
  this.setState({
    [name]: value
  });
};

```

Ici, lors de la définition de l'état, nous définissons le nom de l'état dynamique avec la valeur dynamique. Donc, lorsque nous changeons la valeur du champ de saisie `number1`, `event.target.name` sera `number1` et `event.target.value` sera la valeur saisie par l'utilisateur.

Et lorsque nous changeons la valeur du champ de saisie `number2`, `event.target.name` sera `number2` et `event.target.value` sera la valeur saisie par l'utilisateur.

Ici, nous utilisons la syntaxe de clé dynamique ES6 pour mettre à jour la valeur correspondante de l'état.

Maintenant, vous pouvez supprimer les méthodes de gestionnaire d'événements `onFirstInputChange` et `onSecondInputChange`. Nous n'en avons plus besoin.

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/withered-feather-8gsyc](https://codesandbox.io/s/withered-feather-8gsyc)

## Utiliser une seule méthode de calcul

Maintenant, refactorisons les méthodes `handleAdd` et `handleSubtract`.

Nous utilisons deux méthodes séparées qui ont presque le même code, ce qui crée une duplication de code. Nous pouvons corriger cela en créant une seule méthode et en passant un paramètre à la fonction pour identifier l'opération d'addition ou de soustraction.

```js
// changez le code ci-dessous :
<button type="button" className="btn" onClick={this.handleAdd}>
  Ajouter
</button>

<button type="button" className="btn" onClick={this.handleSubtract}>
  Soustraire
</button>

// en ce code :
<button type="button" className="btn" onClick={() => this.handleOperation('add')}>
  Ajouter
</button>

<button type="button" className="btn" onClick={() => this.handleOperation('subtract')}>
  Soustraire
</button>

```

Ici, nous avons ajouté une nouvelle méthode en ligne pour le gestionnaire `onClick` où nous appelons manuellement une nouvelle méthode `handleOperation` en passant le nom de l'opération.

Maintenant, ajoutez une nouvelle méthode `handleOperation` comme ceci :

```js
handleOperation = (operation) => {
  const number1 = parseInt(this.state.number1, 10);
  const number2 = parseInt(this.state.number2, 10);

  let result;
  if (operation === "add") {
    result = number1 + number2;
  } else if (operation === "subtract") {
    result = number1 - number2;
  }

  if (isNaN(result)) {
    this.setState({
      errorMsg: "Veuillez entrer des nombres valides."
    });
  } else {
    this.setState({
      errorMsg: "",
      result: result
    });
  }
};

```

et supprimez les méthodes `handleAdd` et `handleSubtract` précédemment ajoutées.

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/hardcore-brattain-zv09d](https://codesandbox.io/s/hardcore-brattain-zv09d)

## Utiliser la syntaxe de déstructuration ES6

À l'intérieur de la méthode `onInputChange`, nous avons du code comme ceci :

```js
const name = event.target.name;
const value = event.target.value;

```

Nous pouvons utiliser la syntaxe de déstructuration ES6 pour le simplifier comme ceci :

```js
const { name, value } = event.target;

```

Ici, nous extrayons les propriétés `name` et `value` de l'objet `event.target` et créons des variables locales `name` et `value` pour stocker ces valeurs.

Maintenant, à l'intérieur de la méthode `handleOperation`, au lieu de faire référence à l'état chaque fois que nous utilisons `this.state.number1` et `this.state.number2`, nous pouvons séparer ces variables au préalable.

```js
// changez le code ci-dessous :

const number1 = parseInt(this.state.number1, 10);
const number2 = parseInt(this.state.number2, 10);

// en ce code :

let { number1, number2 } = this.state;
number1 = parseInt(number1, 10);
number2 = parseInt(number2, 10);

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/exciting-austin-ldncl](https://codesandbox.io/s/exciting-austin-ldncl)

## Utiliser la syntaxe littérale d'objet améliorée

Si vous vérifiez l'appel de la fonction `setState` à l'intérieur de la fonction `handleOperation`, cela ressemble à ceci :

```js
this.setState({
  errorMsg: "",
  result: result
});

```

Nous pouvons utiliser la syntaxe littérale d'objet améliorée pour simplifier ce code.

Si le nom de la propriété correspond exactement au nom de la variable comme `result: result`, alors nous pouvons sauter la mention de la partie après le deux-points. Donc l'appel de la fonction `setState` ci-dessus peut être simplifié comme ceci :

```js
this.setState({
  errorMsg: "",
  result
});

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/affectionate-johnson-j50ks](https://codesandbox.io/s/affectionate-johnson-j50ks)

## Convertir les composants de classe en React Hooks

À partir de la version 16.8.0 de React, React a ajouté un moyen d'utiliser l'état et les méthodes de cycle de vie à l'intérieur des composants fonctionnels en utilisant les React Hooks.

L'utilisation des React Hooks nous permet d'écrire un code qui est beaucoup plus court et facile à maintenir et à comprendre. Donc, convertissons le code ci-dessus pour utiliser la syntaxe des React Hooks.

Si vous êtes nouveau dans les React Hooks, consultez mon article [introduction aux react hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54).

Déclarons d'abord un composant App comme un composant fonctionnel :

```js
const App = () => {

};

export default App;

```

Pour déclarer l'état, nous devons utiliser le hook `useState`, donc importez-le en haut du fichier. Ensuite, créez 3 appels `useState`, un pour stocker les nombres ensemble sous forme d'objet. Nous pouvons les mettre à jour ensemble en utilisant une seule fonction de gestionnaire et deux autres appels `useState` pour stocker le résultat et le message d'erreur.

```js
import React, { useState } from "react";

const App = () => {
  const [state, setState] = useState({
    number1: "",
    number2: ""
  });
  const [result, setResult] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
};

export default App;

```

Changez la méthode de gestionnaire `onInputChange` en ceci :

```js
const onInputChange = () => {
  const { name, value } = event.target;

  setState((prevState) => {
    return {
      ...prevState,
      [name]: value
    };
  });
};

```

Ici, nous utilisons la syntaxe de mise à jour pour définir l'état car, lorsque nous travaillons avec les React Hooks, l'état n'est pas fusionné automatiquement lors de la mise à jour d'un objet.

Nous étalons donc d'abord toutes les propriétés de l'état, puis nous ajoutons la nouvelle valeur de l'état.

Changez la méthode `handleOperation` en ceci :

```js
const handleOperation = (operation) => {
  let { number1, number2 } = state;
  number1 = parseInt(number1, 10);
  number2 = parseInt(number2, 10);

  let result;
  if (operation === "add") {
    result = number1 + number2;
  } else if (operation === "subtract") {
    result = number1 - number2;
  }

  if (isNaN(result)) {
    setErrorMsg("Veuillez entrer des nombres valides.");
  } else {
    setErrorMsg("");
    setResult(result);
  }
};

```

Maintenant, retournez le même JSX retourné par la méthode de rendu du composant de classe, mais supprimez toutes les références à `this` et `this.state` du JSX.

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/musing-breeze-ec7px?file=/src/App.js](https://codesandbox.io/s/musing-breeze-ec7px?file=/src/App.js)

## Retour implicite des objets

Maintenant, nous avons optimisé notre code pour utiliser les fonctionnalités modernes d'ES6 et évité les duplications de code. Il y a une autre chose que nous pouvons faire pour simplifier l'appel de la fonction `setState`.

Si vous vérifiez l'appel actuel de la fonction `setState` à l'intérieur du gestionnaire `onInputChange`, cela ressemble à ceci :

```js
setState((prevState) => {
  return {
    ...prevState,
    [name]: value
  };
});

```

Dans une fonction fléchée, si nous avons du code comme ceci :

```js
const add = (a, b) => {
 return a + b;
}

```

Alors nous pouvons le simplifier comme montré ci-dessous :

```js
const add = (a, b) => a + b;

```

Cela fonctionne car s'il y a une seule instruction dans le corps de la fonction fléchée, alors nous pouvons sauter les accolades et le mot-clé return. Cela est connu comme un retour implicite.

Donc, si nous retournons un objet d'une fonction fléchée comme ceci :

```js
const getUser = () => {
 return {
  name: 'David,
  age: 35
 }
}

```

Alors nous **ne pouvons pas** le simplifier comme ceci :

```js
const getUser = () => {
  name: 'David,
  age: 35
}

```

Cela est dû au fait que les accolades ouvrantes indiquent le début de la fonction, donc le code ci-dessus est invalide. Pour le faire fonctionner, nous pouvons envelopper l'objet dans des parenthèses comme ceci :

```js
const getUser = () => ({
  name: 'David,
  age: 35
})

```

Le code ci-dessus est le même que le code ci-dessous :

```js
const getUser = () => {
 return {
  name: 'David,
  age: 35
 }
}

```

Nous pouvons donc utiliser la même technique pour simplifier notre appel de fonction `setState`.

```js
setState((prevState) => {
  return {
    ...prevState,
    [name]: value
  };
});

// le code ci-dessus peut être simplifié comme :

setState((prevState) => ({
  ...prevState,
  [name]: value
}));

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/sharp-dream-l90gf?file=/src/App.js](https://codesandbox.io/s/sharp-dream-l90gf?file=/src/App.js)

Cette technique d'enveloppement de code dans des parenthèses est utilisée dans React :

* Pour définir un composant fonctionnel :

```js
const User = () => (
   <div>
    <h1>Bienvenue, Utilisateur</h1>
    <p>Vous êtes connecté avec succès.</p>
   </div>
);

```

* À l'intérieur de la fonction mapStateToProps dans react-redux :

```js
const mapStateToProps = (state, props) => ({ 
   users: state.users,
   details: state.details
});

```

* Fonctions de création d'actions Redux :

```js
const addUser = (user) => ({
  type: 'ADD_USER',
  user
});

```

et dans de nombreux autres endroits.

## Un conseil supplémentaire pour vous aider à écrire de meilleurs composants React

Si nous avons un composant comme ceci :

```js
const User = (props) => (
   <div>
    <h1>Bienvenue, Utilisateur</h1>
    <p>Vous êtes connecté avec succès.</p>
   </div>
);

```

et que nous voulons ensuite logger les props dans la console juste pour les tester ou les déboguer, au lieu de convertir le code en ce code :

```js
const User = (props) => {
 console.log(props);
 return (
   <div>
    <h1>Bienvenue, Utilisateur</h1>
    <p>Vous êtes connecté avec succès.</p>
   </div>
 );
}

```

vous pouvez utiliser l'opérateur OR logique (`||`) comme ceci :

```js
const User = (props) => console.log(props) || (
   <div>
    <h1>Bienvenue, Utilisateur</h1>
    <p>Vous êtes connecté avec succès.</p>
   </div>
);

```

Comment cela fonctionne-t-il ?

La fonction `console.log` imprime simplement la valeur qui lui est passée, mais elle ne retourne rien – elle sera donc évaluée comme undefined `||` (...).

Et parce que l'opérateur `||` retourne la première valeur truthy, le code après `||` sera également exécuté.

### Merci d'avoir lu !

Vous pouvez tout apprendre sur les fonctionnalités ES6+ en détail dans mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).

Vous pouvez également consulter mon cours gratuit [Introduction à React Router](https://yogeshchavan.podia.com/react-router-introduction).

**Abonnez-vous à ma [newsletter hebdomadaire](https://yogeshchavan.dev/) pour rejoindre plus de 1000 autres abonnés et recevoir des conseils, astuces, articles et offres de réduction directement dans votre boîte de réception.**