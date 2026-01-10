---
title: 'Modèles de liaison React : 5 approches pour gérer `this`'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-17T19:33:44.000Z'
originalURL: https://freecodecamp.org/news/react-binding-patterns-5-approaches-for-handling-this-92c651b5af56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Brf51FVp5subpavq4ax8ow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: 'Modèles de liaison React : 5 approches pour gérer `this`'
seo_desc: 'By Cory House

  JavaScript’s this keyword behavior has confused developers for ages.

  There are at least five ways to handle the this context in React. Let’s consider
  the merits of each approach.

  1. Use React.createClass

  If you use React.createClass, Re...'
---

Par Cory House

Le comportement du mot-clé **this** en JavaScript a confus les développeurs depuis des années.

Il existe au moins cinq façons de gérer le contexte **this** dans React. Examinons les mérites de chaque approche.

#### 1. Utiliser React.createClass

Si vous utilisez [React.createClass](https://facebook.github.io/react/docs/top-level-api.html#react.createclass), [React lie automatiquement toutes les fonctions à **this**](https://facebook.github.io/react/docs/tutorial.html#events). Ainsi, le mot-clé **this** est lié à l'instance de votre composant automatiquement :

```
// Cela fonctionne magiquement avec React.createClass
// car `this` est lié pour vous.
onChange={this.handleChange}
```

Cependant, avec l'avènement des classes ES6, cette approche non standard pour créer des classes n'est pas l'avenir de React. En fait, [createClass sera probablement extrait du cœur de React dans une future version](https://facebook.github.io/react/blog/#other-use-cases).

#### 2. Lier dans le Render

Les autres approches supposent que vous déclarez des composants React via des classes ES6. Si vous utilisez une classe ES6, React ne lie plus automatiquement. Une façon de résoudre cela est d'appeler bind dans render :

```
onChange={this.handleChange.bind(this)}
```

Cette approche est concise et claire, cependant, il y a des implications de performance puisque la fonction est réallouée à chaque rendu. Cela semble important, mais **les implications de performance de cette approche sont peu susceptibles d'être perceptibles dans la plupart des applications.** Ainsi, écarter cette option dès le départ pour des raisons de performance est une optimisation prématurée. Cela dit, [voici un exemple où l'impact de performance de cette approche était significatif](https://medium.com/@esamatti/react-js-pure-render-performance-anti-pattern-fb88c101332f#.hv3l5i8vb).

En résumé, si vous rencontrez des problèmes de performance, [évitez d'utiliser bind ou des fonctions fléchées dans render](https://facebook.github.io/react/docs/reusable-components.html#no-autobinding).

#### 3. Utiliser une fonction fléchée dans le Render

Cette approche est similaire à la #2. Vous pouvez éviter de changer le contexte **this** en utilisant une fonction fléchée dans render :

```
onChange={e => this.handleChange(e)}
```

Cette approche a le même impact potentiel sur la performance que la #2.

Les approches alternatives ci-dessous valent la peine d'être considérées car elles offrent une meilleure performance pour un coût supplémentaire minime.

#### 4. Lier dans le Constructeur

Une façon d'éviter de lier dans render est de lier dans le constructeur (l'autre approche est discutée dans la #5 ci-dessous).

```js
constructor(props) {
  super(props);
  this.handleChange = this.handleChange.bind(this);
}
```

C'est l'approche [actuellement recommandée dans la documentation React](https://facebook.github.io/react/docs/reusable-components.html#es6-classes) pour "une meilleure performance dans votre application". C'est aussi l'approche que j'utilise dans "[Building Applications with React and Redux in ES6](https://app.pluralsight.com/courses/react-redux-react-router-es6)" sur Pluralsight.

Cependant, dans la plupart des applications, les implications de performance des approches #2 et #3 ne seront pas perceptibles, donc les avantages de lisibilité et de maintenance des approches #2 et #3 peuvent l'emporter sur les préoccupations de performance dans de nombreuses applications.

Mais si vous êtes prêt à utiliser des fonctionnalités de stage-2, la dernière option ci-dessous est probablement votre meilleur choix.

#### 5. Utiliser une fonction fléchée dans une propriété de classe

Cette technique repose sur la [fonctionnalité proposée des propriétés de classe](https://github.com/jeffmo/es-class-public-fields). Pour utiliser cette approche, vous devez activer [transform-class-properties](http://babeljs.io/docs/plugins/transform-class-properties) ou [activer stage-2 dans Babel](http://babeljs.io/docs/plugins/preset-stage-2/).

```js
handleChange = () => {
  // appelez cette fonction depuis render
  // et this.whatever ici fonctionne bien.
};
```

Cette approche présente plusieurs avantages :

1. Les fonctions fléchées [adoptent la liaison **this** de la portée englobante](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20%26%20object%20prototypes/ch2.md#lexical-this) (en d'autres termes, elles ne changent pas la signification de **this**), donc tout fonctionne automatiquement.
2. Elle évite les problèmes de performance des approches #2 et #3.
3. Elle évite la répétition de l'approche #4.
4. Il est simple de refactoriser depuis le style ES5 createClass vers ce style en convertissant les fonctions pertinentes en fonctions fléchées. En fait, il existe un [moyen entièrement automatisé de gérer cela](https://github.com/reactjs/react-codemod#class) en utilisant un codemod.

#### Résumé

Ce diagramme résume la décision.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YJI4x0i0lJA110oRvjwNBw.png)

Voici des exemples complets et fonctionnels des 5 approches :

```js
// Approche 1 : Utiliser React.createClass
var HelloWorld = React.createClass({
  getInitialState() {
    return { message: 'Bonjour' };
  },

  logMessage() {
    // cela fonctionne magiquement car React.createClass lie automatiquement.
    console.log(this.state.message);
  },

  render() {
    return (
      <input type="button" value="Log" onClick={this.logMessage} />
    );
  }
});

// Approche 2 : Lier dans le Render
class HelloWorld extends React.Component {
  constructor(props) {
    super(props);
    this.state = { message: 'Bonjour' };
  }

  logMessage() {
    // Cela fonctionne grâce au bind dans render ci-dessous.
    console.log(this.state.message);
  }

  render() {
    return (
      <input type="button" value="Log" onClick={this.logMessage.bind(this)} />
    );
  }
}

// Approche 3 : Utiliser une fonction fléchée dans le Render
class HelloWorld extends React.Component {
  constructor(props) {
    super(props);
    this.state = { message: 'Bonjour' };
  }

  logMessage() {
    // Cela fonctionne grâce à la fonction fléchée dans render ci-dessous.
    console.log(this.state.message);
  }

  render() {
    return (
      <input type="button" value="Log" onClick={() => this.logMessage()} />
    );
  }
}

// Approche 4 : Lier dans le Constructeur
class HelloWorld extends React.Component {
  constructor(props) {
    super(props);
    this.state = { message: 'Bonjour' };
    this.logMessage = this.logMessage.bind(this);
  }

  logMessage() {
    // Cela fonctionne grâce au bind dans le constructeur ci-dessus.
    console.log(this.state.message);
  }

  render() {
    return (
      <input type="button" value="Log" onClick={this.logMessage} />
    );
  }
}

// Approche 5 : Fonction fléchée dans une propriété de classe
class HelloWorld extends React.Component {
  // Notez que state est une propriété,
  // donc aucun constructeur n'est nécessaire dans ce cas.
  state = {
    message: 'Bonjour'
  };

  logMessage = () => {
    // Cela fonctionne car les fonctions fléchées adoptent la liaison this de la portée englobante.
    console.log(this.state.message);
  };

  render() {
    return (
      <input type="button" value="Log" onClick={this.logMessage} />
    );
  }
}
```

Alors, que préfèrent les gens ? Voici le sondage :

%[https://twitter.com/housecor/status/766257218312282113]

Avez-vous d'autres façons de gérer cela ? N'hésitez pas à commenter.

Un énorme merci à [@dan_abramov](https://twitter.com/dan_abramov), [@kentcdodds](http://www.twitter.com/kentcdodds), et [@dmosher](http://www.twitter.com/dmosher) pour leurs précieux conseils et révisions !

**_Cory House_** est l'auteur de "[Building Applications with React and Redux in ES6](https://app.pluralsight.com/courses/react-redux-react-router-es6)", "[Building Applications with React and Flux](https://www.pluralsight.com/courses/react-flux-building-applications)", "[Clean Code: Writing Code for Humans](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK1pXx89nJAhUujoMKHeuWAEUQFggcMAA&url=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwriting-clean-code-humans&usg=AFQjCNEBfkBoN-IgCn_1jFUqWDAUIxcmAw&sig2=Ub9Wup4k4mrw_ffPgYu3tA)" et de plusieurs autres cours sur Pluralsight. Il est Architecte Logiciel chez VinSolutions, MVP Microsoft, et [forme des développeurs logiciels à l'international](http://www.bitnative.com/training/) sur des pratiques logicielles comme le développement front-end et le code propre.