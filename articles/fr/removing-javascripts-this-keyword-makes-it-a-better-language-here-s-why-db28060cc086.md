---
title: Supprimer le mot-clé 'this' de JavaScript rend le langage meilleur. Voici pourquoi.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T21:55:27.000Z'
originalURL: https://freecodecamp.org/news/removing-javascripts-this-keyword-makes-it-a-better-language-here-s-why-db28060cc086
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLIXa6jWWjxfB-6AYjm2Hg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Supprimer le mot-clé 'this' de JavaScript rend le langage meilleur. Voici
  pourquoi.
seo_desc: 'By Cristian Salcescu

  Read Functional Architecture with React and Redux and learn how to build apps in
  function style.

  this is of course the source of much confusion in JavaScript. The reason being that
  this depends on how the function was invoked, no...'
---

Par Cristian Salcescu

Lisez [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) et apprenez à construire des applications en style fonctionnel.

`this` est bien sûr la source de beaucoup de confusion en JavaScript. La raison étant que `this` dépend de la manière dont la fonction a été invoquée, et non de l'endroit où la fonction a été définie.

JavaScript sans `this` ressemble à un meilleur langage de programmation fonctionnelle.

### this perdant le contexte

Les méthodes sont des fonctions qui sont stockées dans des objets. Pour qu'une fonction sache sur quel objet travailler, `this` est utilisé. `this` représente le contexte de la fonction.

`this` perd le contexte dans de nombreuses situations. Il perd le contexte à l'intérieur des fonctions imbriquées, il perd le contexte dans les rappels.

Prenons le cas d'un objet timer. L'objet timer attend que l'appel précédent se termine avant d'effectuer un nouvel appel. Il implémente le modèle setTimeout récursif. [Dans l'exemple suivant](https://jsfiddle.net/cristi_salcescu/h3pbc42u/), dans les fonctions imbriquées et les rappels, `this` perd le contexte :

```js
class Timer {
 constructor(callback, interval){
    this.callback = callback;
    this.interval = interval;
    this.timerId = 0;
  }
  
 executeAndStartTimer(){
   this.callback().then(function startNewTimer(){
       this.timerId =  
       setTimeout(this.executeAndStartTimer, this.interval);
   });
 }
    
 start(){
   if(this.timerId === 0){
     this.executeAndStartTimer();
   }
 }
 stop(){
   if(this.timerId !== 0){
     clearTimeout(this.timerId);
     this.timerId = 0;
   }
 }
}

const timer = new Timer(getTodos, 2000);
timer.start();
function getTodos(){
  console.log("call");
  return fetch("https://jsonplaceholder.typicode.com/todos");
}
```

`this` perd le contexte lorsque la méthode est utilisée comme gestionnaire d'événements. Prenons le cas d'un composant React qui construit une requête de recherche. Dans les deux méthodes, utilisées comme gestionnaires d'événements, `this` perd le contexte :

```js
class SearchForm extends React.Component {
  handleChange(event) {
    const newQuery = Object.freeze({ text: event.target.value });
    this.setState(newQuery);
  }
  search() {
    const newQuery = Object.freeze({ text: this.state.text });
    if (this.props.onSearch) this.props.onSearch(newQuery);
  }
  render() {
    return (
      <form>
      <input onChange={this.handleChange} value={this.state.text} />
      <button onClick={this.search} type="button">Search</button>
      </form>
    );
  }
}
```

Il existe de nombreuses solutions à ces problèmes : la méthode `bind()`, le modèle that/self, la fonction fléchée.

Pour plus d'informations sur la façon de corriger les problèmes liés à `this`, consultez [Que faire lorsque 'this' perd le contexte](https://medium.freecodecamp.org/what-to-do-when-this-loses-context-f09664af076f).

### this n'a pas d'encapsulation

`this` crée des problèmes de sécurité. Tous les membres déclarés sur `this` sont publics.

```js
class Timer {
 constructor(callback, interval){
    this.timerId = "secret";
  }
}

const timer = new Timer();
timer.timerId; //secret
```

### Pas de this, pas de prototypes personnalisés

Et si, au lieu d'essayer de corriger `this` perdant le contexte et les problèmes de sécurité, nous nous en débarrassions complètement ?

Supprimer `this` a un ensemble d'implications.

Pas de `this` signifie essentiellement pas de `class`, pas de constructeur de fonction, pas de `new`, pas de `Object.create()`.

Supprimer `this` signifie pas de prototypes personnalisés en général.

### Un meilleur langage

JavaScript est à la fois un langage de programmation fonctionnelle et un langage basé sur les prototypes. Si nous nous débarrassons de `this`, il nous reste JavaScript comme langage de programmation fonctionnelle. C'est encore mieux.

En même temps, sans `this`, JavaScript offre une nouvelle façon unique de faire de la programmation orientée objet sans classes ni héritage.

### Programmation orientée objet sans this

La question est de savoir comment construire des objets sans `this`.

Il y aura deux types d'objets :

* objets de données pures
* objets de comportement

#### Objets de données pures

Les objets de données pures contiennent uniquement des données et n'ont pas de comportement.

Tout champ calculé sera rempli à la création.

Les objets de données pures doivent être immuables. Nous devons les `Object.freeze()` à la création.

#### Objets de comportement

Les objets de comportement seront des collections de fermetures partageant le même état privé.

[Créons](https://jsfiddle.net/cristi_salcescu/8z7mLkca/) l'objet Timer dans une approche sans `this`.

```js
function Timer(callback, interval){
  let timerId;
  function executeAndStartTimer(){
    callback().then(function makeNewCall(){
      timerId = setTimeout(executeAndStartTimer, interval);
    });
  }
  function stop(){
    if(timerId){
      clearTimeout(timerId);
      timerId = 0;
    }
  }
  function start(){
    if(!timerId){
      executeAndStartTimer();
    }
  }
  return Object.freeze({
    start,
    stop
  });  
}

const timer = Timer(getTodos, 2000);
timer.start();
```

L'objet `timer` a deux méthodes publiques : `start` et `stop`. Tout le reste est privé. Il n'y a pas de problèmes de perte de contexte de `this` car il n'y a pas de `this`.

Pour plus d'informations sur pourquoi favoriser une approche sans `this` lors de la construction d'objets de comportement, consultez [Class vs Factory function: exploring the way forward](https://medium.freecodecamp.org/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15).

#### Mémoire

Le système de prototypes est meilleur pour la conservation de la mémoire. Toutes les méthodes sont créées une seule fois dans l'objet prototype et partagées par toutes les instances.

Le coût mémoire de la construction d'objets de comportement utilisant des fermetures est notable lors de la création de milliers du même objet. Dans une application, nous avons quelques objets de comportement. Si nous prenons par exemple un objet de comportement de magasin, il n'y aura qu'une seule instance de celui-ci dans l'application, donc il n'y a pas de coût mémoire supplémentaire lors de l'utilisation de fermetures pour le construire.

Dans une application, il peut y avoir des centaines ou des milliers d'objets de données pures. Les objets de données pures n'utilisent pas de fermetures, donc pas de coût mémoire.

### Composants sans this

`this` peut être requis par de nombreux frameworks de composants, comme React ou Vue par exemple.

Dans React, nous pouvons créer des composants fonctionnels sans état, sans `this`, en tant que fonctions pures.

```js
function ListItem({ todo }){
  return (
    <li>
      <div>{ todo.title}</div>
      <div>{ todo.userName }</div>
    </li>
  );
}
```

Nous pouvons également créer des composants avec état sans `this` avec [React Hooks](https://reactjs.org/docs/hooks-overview.html). [Regardez l'exemple suivant](https://codesandbox.io/s/31v5w58wo1) :

```js
import React, { useState } from "react";
function SearchForm({ onSearch }) {
  const [query, setQuery] = useState({ text: "" });
  function handleChange(event) {
    const newQuery = Object.freeze({ text: event.target.value });
    setQuery(newQuery);
  }
  function search() {
    const newQuery = Object.freeze({ text: query.text });
    if (onSearch) onSearch(newQuery);
  }
  return (
    <form>
      <input type="text" onChange={handleChange} />
      <button onClick={search} type="button">Search</button>
    </form>
  );
};
```

### Suppression des arguments

Si nous nous débarrassons de `this`, nous devrions également nous débarrasser de `arguments` car ils ont le même comportement de liaison dynamique.

Se débarrasser de `arguments` est assez simple. Nous utilisons simplement la nouvelle syntaxe des paramètres rest. Cette fois, le paramètre rest est un objet de tableau :

```js
function addNumber(total, value){
  return total + value;
}

function sum(...args){
  return args.reduce(addNumber, 0);
}

sum(1,2,3); //6
```

### Conclusion

La meilleure façon d'éviter les problèmes liés à `this` est de ne pas utiliser `this` du tout.

JavaScript sans `this` peut être un meilleur langage de programmation fonctionnelle.

Nous pouvons construire des objets encapsulés, sans utiliser `this`, comme des collections de fermetures.

Avec React Hooks, nous pouvons créer des composants avec état sans `this`.

Cela dit, `this` ne peut pas être supprimé de JavaScript sans casser toutes les applications existantes. Cependant, quelque chose peut être fait. Nous pouvons écrire notre propre code sans `this` et le laisser être utilisé dans les bibliothèques.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour plus d'informations sur l'application des techniques de programmation fonctionnelle dans React, consultez** **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)