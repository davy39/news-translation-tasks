---
title: Méthodes du cycle de vie des composants React – Expliquées avec des exemples
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-05-25T14:28:35.000Z'
originalURL: https://freecodecamp.org/news/react-component-lifecycle-methods
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-23-10-50-48.png
tags:
- name: components
  slug: components
- name: lifecycle methods
  slug: lifecycle-methods
- name: React
  slug: react
seo_title: Méthodes du cycle de vie des composants React – Expliquées avec des exemples
seo_desc: In React, components have a lifecycle that consists of different phases.
  Each phase has a set of lifecycle methods that are called at specific points in
  the component's lifecycle. These methods allow you to control the component's behavior
  and perfor...
---

Dans React, les composants ont un cycle de vie qui se compose de différentes phases. Chaque phase possède un ensemble de méthodes de cycle de vie qui sont appelées à des points spécifiques du cycle de vie du composant. Ces méthodes permettent de contrôler le comportement du composant et d'effectuer des actions spécifiques à différentes étapes de son cycle de vie.

Le cycle de vie d'un composant comporte trois phases principales : la phase de montage, la phase de mise à jour et la phase de démontage.

La phase de montage commence lorsque le composant est créé et inséré dans le DOM. La phase de mise à jour se produit lorsque l'état ou les props d'un composant changent. Et la phase de démontage se produit lorsque le composant est retiré du DOM.

## Phase de montage du composant

La phase de montage fait référence à la période où un composant est créé et inséré dans le DOM.

Au cours de cette phase, plusieurs méthodes de cycle de vie sont invoquées par React pour permettre au développeur de configurer le composant, d'initialiser l'état ou les écouteurs d'événements nécessaires, et d'effectuer d'autres tâches d'initialisation.

La phase de montage comporte trois méthodes principales de cycle de vie qui sont appelées dans l'ordre :

### La méthode de cycle de vie `constructor()`

La méthode `constructor()` est appelée lorsque le composant est créé pour la première fois. Elle est utilisée pour initialiser l'état du composant et lier les méthodes à l'instance du composant. Voici un exemple :

```
import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  }

  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.handleClick}>Incrémenter</button>
      </div>
    );
  }
}

export default Counter;

```

Dans cet exemple, la méthode `constructor()` définit l'état initial du composant avec un objet ayant une propriété `count` définie à `0`, et lie la méthode `handleClick` à l'instance du composant. La méthode `handleClick` incrémente la propriété d'état `count` lorsque le bouton est cliqué.

### La méthode de cycle de vie `render()`

La méthode `render()` est responsable de la génération de la représentation du DOM virtuel du composant en fonction de ses props et de son état actuels. Elle est appelée chaque fois que le composant doit être réaffiché, soit parce que ses props ou son état ont changé, soit parce qu'un composant parent a été réaffiché.

Dans l'exemple ci-dessus dans la partie constructeur :

```jsx
render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={this.handleClick}>Incrémenter</button>
      </div>
    );
  }
}

```

La méthode `render` affiche la valeur actuelle du compte et un bouton. Lorsque le bouton est cliqué, la méthode `handleClick` est invoquée. Cela déclenche une mise à jour de l'état, provoquant un réaffichage, et le compte mis à jour est affiché.

### La méthode de cycle de vie `getDerivedStateFromProps()`

`getDerivedStateFromProps()` est une méthode de cycle de vie disponible dans React 16.3 et les versions ultérieures qui est invoquée pendant la phase de montage et de mise à jour d'un composant.

Pendant la phase de montage, `getDerivedStateFromProps()` est appelée après le constructeur et avant `render()`. Cette méthode est appelée pour chaque cycle de rendu et offre l'opportunité de mettre à jour l'état du composant en fonction des changements de props avant le rendu initial.

La signature de `getDerivedStateFromProps()` est la suivante :

```
static getDerivedStateFromProps(props, state)
```

Elle prend deux paramètres :

`props` : Les props mises à jour pour le composant.

`state` : L'état actuel du composant.

La méthode doit retourner un objet qui représente l'état mis à jour du composant, ou `null` si aucune mise à jour de l'état n'est nécessaire.

Il est important de noter que `getDerivedStateFromProps()` est une méthode statique, ce qui signifie qu'elle n'a pas accès au mot-clé `this` et ne peut pas interagir avec les méthodes ou propriétés de l'instance du composant.

```
import React from 'react';
import ReactDOM from 'react-dom';
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritefood: "rice"};
  }
  componentDidMount() {
    setTimeout(() => {
      this.setState({favoritefood: "pizza"})
    }, 1000)
  }
  static getDerivedStateFromProps(props, state) {
    return {favoritefood: props.favfod };
  }
   render() {
    return (
      <h1>Mon aliment préféré est {this.state.favoritefood}</h1>
    );
  }
}
ReactDOM.render(<Header />, document.getElementById('root')); 
```

Ceci est un composant React nommé Header qui affiche un élément `<h1>` avec une chaîne qui inclut la valeur de `this.state.favoritefood`.

Le composant a un constructeur qui définit l'état initial de `favoritefood` à "rice".

La méthode `componentDidMount()` est également définie, qui est appelée lorsque le composant est monté dans le DOM. Dans cette méthode, il y a une fonction `setTimeout()` qui met à jour l'état de `favoritefood` à "pizza" après 1 seconde (1000 millisecondes).

Le composant a également une méthode statique `getDerivedStateFromProps()` qui prend `props` et `state` comme arguments et retourne un objet avec une clé `favoritefood` et une valeur `props.favfod`. Cette méthode est appelée pendant la phase de montage et de mise à jour du composant et est utilisée pour dériver l'état des props.

Enfin, la méthode `render()` du composant retourne l'élément `<h1>` avec la valeur de `this.state.favoritefood`. Lorsque le composant est rendu en utilisant `ReactDOM.render()`, il est monté sur l'élément avec un ID de "root".

### La méthode de cycle de vie `componentDidMount()`

La méthode `componentDidMount()` est appelée une fois que le composant a été monté dans le DOM. Elle est généralement utilisée pour configurer les écouteurs d'événements ou les temporisateurs nécessaires, effectuer les appels API ou la récupération de données nécessaires, et effectuer d'autres tâches d'initialisation qui nécessitent l'accès à l'API DOM du navigateur.

Voici un exemple :

```
import React from 'react';
import ReactDOM from 'react-dom';
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritefood: "rice"};
  }
  componentDidMount() {
    setTimeout(() => {
      this.setState({favoritefood: "pizza"})
    }, 1000)
  }
  render() {
    return (
      <h1>Mon aliment préféré est {this.state.favoritefood}</h1>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('root')); 
```

Ce code définit un composant React appelé `Header` qui étend la classe `React.Component`. Le composant a un constructeur qui initialise l'état du composant avec une propriété appelée `favoritefood` définie sur la chaîne "rice".

Le composant a également une méthode de cycle de vie `componentDidMount`, qui est appelée par React après que le composant a été monté (c'est-à-dire inséré dans le DOM). Dans cette méthode, une fonction `setTimeout` est utilisée pour retarder l'exécution d'une fonction qui met à jour la propriété d'état `favoritefood` à "pizza" d'une seconde.

Enfin, le composant a une méthode `render` qui retourne une expression JSX contenant un élément `h1` avec le texte "Mon aliment préféré est" et la valeur actuelle de la propriété d'état `favoritefood`.

## Phase de mise à jour du composant

Cette phase se produit lorsque les props ou l'état d'un composant changent, et que le composant doit être mis à jour dans le DOM.

### La méthode de cycle de vie `shouldComponentUpdate()`

La méthode `shouldComponentUpdate()` est appelée avant qu'un composant ne soit mis à jour. Elle prend deux arguments : `nextProps` et `nextState`. Cette méthode retourne une valeur booléenne qui détermine si le composant doit être mis à jour ou non. Si cette méthode retourne true, le composant sera mis à jour, et si elle retourne false, le composant ne sera pas mis à jour.

Voici un exemple de l'utilisation de `shouldComponentUpdate()` :

```
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class Header extends Component {
  constructor(props) {
    super(props);
    this.state = { favoriteFood: 'rice' };
  }

  shouldComponentUpdate(nextProps, nextState) {
    // Ne réafficher que si l'état favoriteFood a changé
    return this.state.favoriteFood !== nextState.favoriteFood;
  }

  changeFood = () => {
    this.setState({ favoriteFood: 'Pizza' });
  }

  render() {
    return (
      <div>
        <h1>Mon aliment préféré est {this.state.favoriteFood}</h1>
        <button type="button" onClick={this.changeFood}>Changer l'aliment</button>
      </div>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('root'));

```

Le code ci-dessus définit un composant `Header` qui affiche l'aliment préféré de l'utilisateur et permet à l'utilisateur de le changer en cliquant sur un bouton. La méthode `shouldComponentUpdate()` est implémentée pour ne réafficher le composant que si l'état `favoriteFood` a changé, ce qui est un bon moyen d'optimiser les performances.

Le code utilise la syntaxe ES6 pour définir la classe de composant et ses méthodes, et importe `Component` de `React` pour créer la classe. La fonction `ReactDOM.render()` est utilisée pour rendre le composant Header dans le DOM.

### La méthode de cycle de vie `componentWillUpdate()`

`componentWillUpdate()` est une méthode de cycle de vie dans React qui est appelée juste avant le début du cycle de mise à jour d'un composant. Elle reçoit les prochains props et état comme arguments et permet d'effectuer les actions nécessaires avant que le composant ne se mette à jour.

Mais cette méthode n'est pas recommandée pour mettre à jour l'état, car elle peut provoquer une boucle infinie de rendu. Elle est principalement utilisée pour des tâches telles que les appels API, la mise à jour du DOM, ou la préparation du composant à recevoir de nouvelles données. `componentWillUpdate()` est souvent utilisée en conjonction avec `componentDidUpdate()` pour gérer les mises à jour des composants.

```
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class MyComponent extends Component {
  state = {
    count: 0,
  };

  handleClick = () => {
    this.setState({ count: this.state.count + 1 });
  };

  componentWillUpdate(nextProps, nextState) {
    if (nextState.count !== this.state.count) {
      console.log(`Le compte est sur le point de passer de ${this.state.count} à ${nextState.count}.`);
    }
  }

  render() {
    return (
      <div>
        <h1>Compte : {this.state.count}</h1>
        <button type="button" onClick={this.handleClick}>
          Incrémenter
        </button>
      </div>
    );
  }
}

const rootElement = document.getElementById('root');
ReactDOM.render(<MyComponent />, rootElement);

```

Dans cet exemple, la méthode `componentWillUpdate` est appelée chaque fois que le composant est sur le point de se mettre à jour. Dans cette méthode, nous pouvons accéder aux arguments `nextProps` et `nextState` pour vérifier s'il y a des changements dans l'état ou les props du composant. S'il y a des changements, nous pouvons effectuer certaines actions ou enregistrer des messages avant que la mise à jour ne se produise.

### La méthode de cycle de vie `componentDidUpdate`

La méthode `componentDidUpdate()` est une méthode de cycle de vie dans React qui est appelée après qu'un composant a été mis à jour et réaffiché. Elle est utile pour effectuer des effets secondaires ou des opérations supplémentaires lorsque les props ou l'état du composant ont changé.

Voici un exemple de l'utilisation de la méthode `componentDidUpdate()` :

```jsx
import React, { Component } from 'react';

class ExampleComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.count !== this.state.count) {
      console.log('Le compte a été mis à jour :', this.state.count);
    }
  }

  handleClick() {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  }

  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={() => this.handleClick()}>Incrémenter</button>
      </div>
    );
  }
}

export default ExampleComponent;

```

Dans cet exemple, la méthode `componentDidUpdate()` est utilisée pour enregistrer un message dans la console chaque fois que l'état `count` a été mis à jour. Elle compare l'état précédent (`prevState.count`) avec l'état actuel (`this.state.count`) pour vérifier s'il y a eu un changement.

Chaque fois que la méthode `handleClick()` est appelée, l'état `count` est incrémenté, déclenchant un réaffichage du composant. Après le réaffichage, `componentDidUpdate()` est appelée, et elle enregistre la valeur mise à jour du compte dans la console.

Il est important d'inclure une vérification conditionnelle à l'intérieur de `componentDidUpdate()` pour éviter les boucles infinies. Si vous souhaitez mettre à jour l'état en fonction d'un changement de prop, assurez-vous de comparer la prop précédente (`prevProps`) avec la prop actuelle (`this.props`) avant de mettre à jour l'état.

Rappelez-vous que `componentDidUpdate()` n'est pas appelée pendant le rendu initial du composant, seulement lors des mises à jour ultérieures.

> À partir de React 16.3, la méthode `componentDidUpdate()` peut recevoir deux arguments supplémentaires : `prevProps` et `prevState`. Ces arguments fournissent l'accès aux valeurs précédentes des props et de l'état, ce qui peut être utile pour effectuer des comparaisons.
>   
> Mais si vous utilisez une version plus récente de React, vous pouvez utiliser le hook `useEffect()` avec un tableau de dépendances pour obtenir une fonctionnalité similaire.

### La méthode de cycle de vie `getSnapshotBeforeUpdate`

La méthode `getSnapshotBeforeUpdate()` est appelée juste avant que l'interface utilisateur du composant ne soit mise à jour. Elle permet au composant de capturer certaines informations sur l'état actuel de l'interface utilisateur, telles que la position de défilement avant qu'elle ne change. Cette méthode retourne une valeur qui est passée en tant que troisième paramètre à la méthode `componentDidUpdate()`.

Voici un exemple de l'utilisation de `getSnapshotBeforeUpdate()` pour capturer la position de défilement d'un composant avant qu'il ne se mette à jour :

```
import React from 'react';
import ReactDOM from 'react-dom';

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {favoritefood: "rice"};
  }
  componentDidMount() {
    setTimeout(() => {
      this.setState({favoritefood: "pizza"})
    }, 1000)
  }
  getSnapshotBeforeUpdate(prevProps, prevState) {
    document.getElementById("div1").innerHTML =
    "Avant la mise à jour, le préféré était " + prevState.favoritefood;
  }
  componentDidUpdate() {
    document.getElementById("div2").innerHTML =
    "L'aliment préféré mis à jour est " + this.state.favoritefood;
  }
  render() {
    return (
      <div>
        <h1>Mon aliment préféré est {this.state.favoritefood}</h1>
        <div id="div1"></div>
        <div id="div2"></div>
      </div>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('root'));




```

Ceci est un composant React appelé `Header` qui affiche un titre et un bouton qui, lorsqu'il est cliqué, montre l'aliment préféré de l'utilisateur. Le composant a également un état qui suit l'aliment préféré et s'il doit être affiché ou non.

La méthode `constructor` définit l'état initial du composant, y compris l'aliment préféré par défaut "rice" et la variable d'état `showFavFood` à `false`.

La méthode `componentDidMount` est appelée après que le composant a été monté dans le DOM. Dans ce cas, elle définit un délai qui changera l'aliment préféré en "pizza" après une seconde.

La méthode `getSnapshotBeforeUpdate` est appelée juste avant que le composant ne soit mis à jour. Elle vérifie si la variable d'état `favoriteFood` a changé depuis la dernière mise à jour et retourne un objet avec l'aliment préféré précédent si c'est le cas. Sinon, elle retourne `null`.

La méthode `componentDidUpdate` est appelée après que le composant a été mis à jour. Elle reçoit les props précédents, l'état précédent et le snapshot comme arguments. Dans ce cas, elle vérifie si le snapshot n'est pas null et enregistre l'aliment préféré précédent dans la console.

Dans la méthode `render`, le composant affiche un titre qui affiche la variable d'état `favoriteFood` actuelle. Lorsque le bouton est cliqué, la variable d'état `showFavFood` est définie à `true` et un paragraphe est affiché qui affiche la variable d'état `favoriteFood` actuelle.

Enfin, la fonction `ReactDOM.render` est appelée pour afficher le composant Header à l'intérieur d'un élément HTML avec l'ID "root".

## Phase de démontage du composant

La phase de démontage fait référence à l'étape du cycle de vie où un composant est retiré du DOM (Document Object Model) et n'est plus rendu ou accessible.

Au cours de cette phase, React effectue une série d'opérations de nettoyage pour s'assurer que le composant et ses ressources associées sont correctement supprimées.

La phase de démontage est la dernière étape du cycle de vie d'un composant React et se produit lorsque le composant est retiré de l'arbre DOM.

Cela peut se produire pour diverses raisons, telles que lorsque le composant n'est plus nécessaire, que le composant parent est réaffiché sans inclure le composant enfant, ou lorsque l'application navigue vers une page ou une vue différente.

### La méthode de cycle de vie `componentWillUnmount()`

Au cours de la phase de démontage, React appelle les méthodes de cycle de vie suivantes dans l'ordre :

* `componentWillUnmount()` : Cette méthode est appelée juste avant que le composant ne soit retiré du DOM. Elle permet d'effectuer tout nettoyage nécessaire, tel que l'annulation des temporisateurs, la suppression des écouteurs d'événements, ou le vidage des structures de données qui ont été configurées pendant la phase de montage.
* Après que `componentWillUnmount()` soit appelée, le composant est retiré du DOM et tout son état et ses props sont détruits.

Il est important de noter qu'une fois qu'un composant est démonté, il ne peut pas être remonté. Si vous devez rendre le composant à nouveau, vous devrez créer une nouvelle instance de celui-ci.

Voici un exemple de l'utilisation de la méthode `componentWillUnmount()` pour effectuer le nettoyage :

```
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class MyComponent extends Component {
  state = {
    showChild: true,
  };

  handleDelete = () => {
    this.setState({ showChild: false });
  };

  render() {
    const { showChild } = this.state;

    return (
      <div>
        {showChild && <Child />}
        <button type="button" onClick={this.handleDelete}>
          Supprimer l'en-tête
        </button>
      </div>
    );
  }
}

class Child extends Component {
  componentWillUnmount() {
    alert('Le composant nommé Child est sur le point d'être démonté.');
  }

  render() {
    return <h1>Bonjour le monde !</h1>;
  }
}

const rootElement = document.getElementById('root');
ReactDOM.render(<MyComponent />, rootElement);

```

Ceci est un composant React qui affiche un `MyComponent` avec un composant `Child` qui sera rendu conditionnellement en fonction de la valeur de l'état `showChild`.

Lorsque l'utilisateur clique sur le bouton "Supprimer l'en-tête", la fonction `handleDelete` sera appelée, ce qui mettra à jour l'état `showChild` à `false`. Cela provoque le démontage du composant `Child` et déclenche la méthode de cycle de vie `componentWillUnmount`, qui affichera un message d'alerte.

La classe `MyComponent` étend la classe `Component` fournie par React et définit une variable d'état `showChild` avec une valeur initiale de `true`. Elle définit également une fonction `handleDelete` qui sera appelée lorsque l'utilisateur clique sur le bouton "Supprimer l'en-tête". Cette fonction met à jour l'état `showChild` à `false`.

Dans la méthode de rendu de `MyComponent`, l'état `showChild` est utilisé pour rendre conditionnellement le composant `Child` en utilisant l'opérateur logique `&&`. Si `showChild` est `true`, le composant `Child` sera rendu. Sinon, il ne sera pas rendu.

La classe `Child` étend la classe `Component` et définit une méthode `componentWillUnmount` qui sera appelée juste avant que le composant ne soit démonté. Dans ce cas, elle affiche un message d'alerte.

Enfin, la méthode `ReactDOM.render` est appelée pour rendre le composant `MyComponent` à l'intérieur de l'élément avec l'ID "root" dans le document HTML.

## Conclusion

En résumé, les composants React ont un cycle de vie composé de trois phases : le montage, la mise à jour et le démontage. Chaque phase possède des méthodes de cycle de vie spécifiques qui sont appelées à différents points du cycle de vie du composant.

La compréhension de ces méthodes de cycle de vie peut aider les développeurs à contrôler le comportement du composant et à effectuer des actions spécifiques à différentes étapes de son cycle de vie.