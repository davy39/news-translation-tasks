---
title: Les meilleurs exemples React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-20T17:43:00.000Z'
originalURL: https://freecodecamp.org/news/react-examples-reactjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f29740569d1a4ca4119.jpg
tags:
- name: React
  slug: react
seo_title: Les meilleurs exemples React
seo_desc: 'React (also known as React.js) is one of the most popular JavaScript front
  end development libraries. Here is a collection of React syntax and usage that you
  can use as a handy guide or reference.

  React Component Example

  Components are reusable in Re...'
---

React (également connu sous le nom de React.js) est l'une des bibliothèques de développement front-end JavaScript les plus populaires. Voici une collection de syntaxe et d'utilisation de React que vous pouvez utiliser comme guide ou référence pratique.

## **Exemple de composant React**

Les composants sont réutilisables dans React.js. Vous pouvez injecter des valeurs dans les props comme indiqué ci-dessous :

```jsx
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}

const element = <Welcome name="Faisal Arkan" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

`name="Faisal Arkan"` donnera une valeur à `{props.name}` depuis `function Welcome(props)` et retournera un composant qui a la valeur donnée par `name="Faisal Arkan"`. Après cela, React rendra l'élément en HTML.

### **Autres façons de déclarer des composants**

Il existe de nombreuses façons de déclarer des composants lors de l'utilisation de React.js. Il existe deux types de composants, les composants **sans état** et les composants **avec état**. 

### **Avec état**

#### **Composants de type Classe**

```jsx
class Cat extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      humor: 'heureux'
    }
  }
  render() {
    return(
      <div>
        <h1>{this.props.name}</h1>
        <p>
          {this.props.color}
        </p>
      </div>
    );
  }
}
```

### **Composants sans état**

#### **Composants fonctionnels (Fonction fléchée ES6)**

```jsx
const Cat = props => {
  return (  
    <div>
      <h1>{props.name}</h1>
      <p>{props.color}</p>
    </div>;
  );
};
```

#### **Composants avec retour implicite**

```jsx
const Cat = props => 
  <div>
    <h1>{props.name}</h1>
    <p>{props.color}</p>
  </div>;
```

# **Exemple de Fragment React**

Les fragments sont un moyen de rendre plusieurs éléments sans utiliser d'élément conteneur. Lorsque vous essayez de rendre des éléments sans balise englobante en JSX, vous verrez le message d'erreur `Les éléments JSX adjacents doivent être enveloppés dans une balise englobante`. Cela est dû au fait que lorsque JSX est transpilé, il crée des éléments avec leurs noms de balises correspondants et ne sait pas quel nom de balise utiliser si plusieurs éléments sont trouvés. 

Dans le passé, une solution fréquente à ce problème était d'utiliser une div conteneur pour résoudre ce problème. Cependant, la version 16 de React a introduit l'ajout de `Fragment`, ce qui rend cela inutile.

`Fragment` agit comme un conteneur sans ajouter de divs inutiles au DOM. Vous pouvez l'utiliser directement depuis l'import React, ou le déstructurer :

```jsx
import React from 'react';

class MyComponent extends React.Component {
  render(){
    return (
      <React.Fragment>
        <div>Je suis un élément !</div>
        <button>Je suis un autre élément</button>
      </React.Fragment>
    );
  }
}

export default MyComponent;
```

```jsx
// Déstructuré
import React, { Component, Fragment } from 'react';

class MyComponent extends Component {
  render(){
    return (
      <Fragment>
        <div>Je suis un élément !</div>
        <button>Je suis un autre élément</button>
      </Fragment>
    );
  }
}

export default MyComponent;
```

La version 16.2 de React a simplifié ce processus, permettant aux balises JSX vides d'être interprétées comme des Fragments :

```jsx
return (
  <>
    <div>Je suis un élément !</div>
    <button>Je suis un autre élément</button>
  </>
);
```

# Exemple de JSX React

### JSX

JSX signifie JavaScript XML.

JSX est une expression qui utilise des instructions HTML valides dans JavaScript. Vous pouvez assigner cette expression à une variable et l'utiliser ailleurs. Vous pouvez combiner d'autres expressions JavaScript valides et JSX dans ces instructions HTML en les plaçant entre accolades (`{}`). Babel compile ensuite JSX en un objet de type `React.createElement()`.

### **Expressions sur une seule ligne et sur plusieurs lignes**

Les expressions sur une seule ligne sont simples à utiliser.

```jsx
const one = <h1>Bonjour le monde !</h1>;
```

Lorsque vous devez utiliser plusieurs lignes dans une seule expression JSX, écrivez le code dans une seule parenthèse.

```jsx
const two = (
  <ul>
    <li>Une fois</li>
    <li>Deux fois</li>
  </ul>
);
```

### **Utilisation de balises HTML uniquement**

```jsx
const greet = <h1>Bonjour le monde !</h1>;
```

### **Combinaison d'expressions JavaScript avec des balises HTML**

Nous pouvons utiliser des variables JavaScript entre accolades.

```jsx
const who = "Quincy Larson";
const greet = <h1>Bonjour {who} !</h1>;
```

Nous pouvons également appeler d'autres fonctions JavaScript entre accolades.

```jsx
function who() {
  return "Monde";
}
const greet = <h1>Bonjour {who()} !</h1>;
```

### **Une seule balise parente est autorisée**

Une expression JSX doit avoir une seule balise parente. Nous pouvons ajouter plusieurs balises imbriquées dans l'élément parent uniquement.

```jsx
// Ceci est valide.
const tags = (
  <ul>
    <li>Une fois</li>
    <li>Deux fois</li>
  </ul>
);

// Ceci n'est pas valide.
const tags = (
  <h1>Bonjour le monde !</h1>
  <h3>Voici ma liste spéciale :</h3>
  <ul>
    <li>Une fois</li>
    <li>Deux fois</li>
  </ul>
);
```

## Exemple d'état React

L'état est l'endroit d'où proviennent les données.

Nous devons toujours essayer de rendre notre état aussi simple que possible et minimiser le nombre de composants avec état. Si nous avons, par exemple, dix composants qui ont besoin de données de l'état, nous devons créer un composant conteneur qui conservera l'état pour tous.

L'état est essentiellement comme un objet global qui est disponible partout dans un composant.

Exemple d'un composant de classe avec état :

```javascript
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
      
    // Nous déclarons l'état comme indiqué ci-dessous
    
    this.state = {                           
      x: "Ceci est x de l'état",    
      y: "Ceci est y de l'état"
    }
  }
  render() {
    return (
      <div>
        <h1>{this.state.x}</h1>
        <h2>{this.state.y}</h2>
      </div>
    );
  }
}
export default App;
```

Un autre exemple :

```javascript
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    
    // Nous déclarons l'état comme indiqué ci-dessous
    this.state = {                           
      x: "Ceci est x de l'état",    
      y: "Ceci est y de l'état"
    }
  }

  render() {
    let x1 = this.state.x;
    let y1 = this.state.y;

    return (
      <div>
        <h1>{x1}</h1>
        <h2>{y1}</h2>
      </div>
    );
  }
}
export default App;
```

## **Mise à jour de l'état**

Vous pouvez changer les données stockées dans l'état de votre application en utilisant la méthode `setState` sur votre composant.

```js
this.setState({ value: 1 });
```

Gardez à l'esprit que `setState` est asynchrone, vous devez donc être prudent lorsque vous utilisez l'état actuel pour définir un nouvel état. Un bon exemple de cela serait si vous voulez incrémenter une valeur dans votre état.

#### **La mauvaise façon**

```js
this.setState({ value: this.state.value + 1 });
```

Cela peut entraîner un comportement inattendu dans votre application si le code ci-dessus est appelé plusieurs fois dans le même cycle de mise à jour. Pour éviter cela, vous pouvez passer une fonction de rappel de mise à jour à `setState` au lieu d'un objet.

#### **La bonne façon**

```js
this.setState(prevState => ({ value: prevState.value + 1 }));
```

## **Mise à jour de l'état**

Vous pouvez changer les données stockées dans l'état de votre application en utilisant la méthode `setState` sur votre composant.

```js
this.setState({value: 1});
```

Gardez à l'esprit que `setState` peut être asynchrone, vous devez donc être prudent lorsque vous utilisez l'état actuel pour définir un nouvel état. Un bon exemple de cela serait si vous voulez incrémenter une valeur dans votre état.

##### **La mauvaise façon**

```js
this.setState({value: this.state.value + 1});
```

Cela peut entraîner un comportement inattendu dans votre application si le code ci-dessus est appelé plusieurs fois dans le même cycle de mise à jour. Pour éviter cela, vous pouvez passer une fonction de rappel de mise à jour à `setState` au lieu d'un objet.

##### **La bonne façon**

```js
this.setState(prevState => ({value: prevState.value + 1}));
```

##### **La façon plus propre**

```text
this.setState(({ value }) => ({ value: value + 1 }));
```

Lorsque seul un nombre limité de champs dans l'objet d'état est requis, la déstructuration d'objet peut être utilisée pour un code plus propre.

### Exemple d'état React VS Props

Lorsque nous commençons à travailler avec des composants React, nous entendons fréquemment deux termes. Ce sont `state` et `props`. Donc, dans cet article, nous allons explorer ce que sont ces termes et comment ils diffèrent.

## **État :**

* L'état est quelque chose qu'un composant possède. Il appartient à ce composant particulier où il est défini. Par exemple, l'âge d'une personne est un état de cette personne.
* L'état est mutable. Mais il ne peut être changé que par le composant qui le possède. Comme je peux seulement changer mon âge, pas quelqu'un d'autre.
* Vous pouvez changer un état en utilisant `this.setState()`

Voir l'exemple ci-dessous pour avoir une idée de l'état :

#### **Person.js**

```javascript
  import React from 'react';

  class Person extends React.Component{
    constructor(props) {
      super(props);
      this.state = {
        age:0
      this.incrementAge = this.incrementAge.bind(this)
    }

    incrementAge(){
      this.setState({
        age:this.state.age + 1;
      });
    }

    render(){
      return(
        <div>
          <label>Mon âge est : {this.state.age}</label>
          <button onClick={this.incrementAge}>Faites-moi vieillir !!<button>
        </div>
      );
    }
  }

  export default Person;
```

Dans l'exemple ci-dessus, `age` est l'état du composant `Person`.

## **Props :**

* Les props sont similaires aux arguments de méthode. Ils sont passés à un composant où ce composant est utilisé.
* Les props sont immuables. Ils sont en lecture seule.

Voir l'exemple ci-dessous pour avoir une idée des Props :

#### **Person.js**

```javascript
  import React from 'react';

  class Person extends React.Component{
    render(){
      return(
        <div>
          <label>Je suis une personne {this.props.character}.</label>
        </div>
      );
    }
  }

  export default Person;

  const person = <Person character = "good"></Person>
```

Dans l'exemple ci-dessus, `const person = <Person character = "good"></Person>` nous passons la prop `character = "good"` au composant `Person`.

Cela donne le résultat « Je suis une bonne personne », en fait je le suis.

Il y a beaucoup plus à apprendre sur l'état et les props. Beaucoup de choses peuvent être apprises en plongeant réellement dans la programmation. Alors, mettez les mains dans le cambouis en codant.

## **Exemple de composant d'ordre supérieur React**

Dans React, un **composant d'ordre supérieur** (HOC) est une fonction qui prend un composant et retourne un nouveau composant. Les programmeurs utilisent les HOC pour atteindre la **réutilisation de la logique des composants**. 

Si vous avez utilisé `connect` de Redux, vous avez déjà travaillé avec des composants d'ordre supérieur.

L'idée principale est :

```jsx
const EnhancedComponent = enhance(WrappedComponent);
```

Où :

* `enhance` est le composant d'ordre supérieur ;
* `WrappedComponent` est le composant que vous souhaitez améliorer ; et
* `EnhancedComponent` est le nouveau composant créé.

Cela pourrait être le corps du HOC `enhance` :

```jsx
function enhance(WrappedComponent) {
  return class extends React.Component {
    render() {
      const extraProp = 'Ceci est une prop injectée !';
      return (
        <div className="Wrapper">
          <WrappedComponent
            {...this.props}
            extraProp={extraProp}
          />
        </div>
      );
    }
  }
} 
```

Dans ce cas, `enhance` retourne une **classe anonyme** qui étend `React.Component`. Ce nouveau composant fait trois choses simples :

* Rendre le `WrappedComponent` dans un élément `div` ;
* Passer ses propres props au `WrappedComponent` ; et
* Injecter une prop supplémentaire au `WrappedComponent`.

Les HOC sont simplement un modèle qui utilise la puissance de la nature compositionnelle de React. **Ils ajoutent des fonctionnalités à un composant**. Il y a beaucoup plus de choses que vous pouvez faire avec eux !