---
title: Comment fonctionnent les clés React et les choses amusantes que vous pouvez
  faire avec elles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T12:41:01.000Z'
originalURL: https://freecodecamp.org/news/react-fun-with-keys-68f4c8c36f3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NfrC9urk9a69PqAioUrvaw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment fonctionnent les clés React et les choses amusantes que vous pouvez
  faire avec elles
seo_desc: 'By Christoph Michel

  React uses the key attribute during its reconciliation phase to decide which elements
  can be reused for the next render. They are important for dynamic lists. React will
  compare the keys of the new element with the previous keys a...'
---

Par Christoph Michel

React utilise l'attribut `key` pendant [sa phase de réconciliation](https://reactjs.org/docs/reconciliation.html) pour décider quels [éléments](https://reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html) peuvent être réutilisés pour le prochain rendu. Ils sont importants pour les listes dynamiques. React comparera les clés du nouvel élément avec les clés précédentes et 1) montera les composants ayant une nouvelle clé 2) démontera les composants dont les clés ne sont plus utilisées.

De nombreux développeurs React ont entendu le conseil général selon lequel vous [ne devriez pas utiliser `index` comme clé](https://medium.com/@robinpokorny/index-as-a-key-is-an-anti-pattern-e0349aece318). Mais que peut-il se passer exactement lorsque vous utilisez les `key`s de manière incorrecte ? Que pouvons-nous faire d'autre lorsque nous jouons avec les clés ?

Pour mieux comprendre, considérons [l'exemple](https://codesandbox.io/s/7ko97vnv80) de rendu d'une liste de `input`. Lorsque vous cliquez sur un bouton, nous allons insérer un nouvel élément avec le texte `Front` **au début** de la liste.

```
import React from "react";import { render } from "react-dom";class Item extends React.PureComponent {  state = {    text: this.props.text  };  onChange = event => {    this.setState({      text: event.target.value    });  };  componentDidMount() {    console.log("Monté ", this.props.text);  }  componentWillUnmount() {    console.log("Démontage ", this.props.text);  }  render() {    console.log("rerendu ", this.props.text);    const { text } = this.state;    return (      <li>        <input value={text} onChange={this.onChange} />      </li>    );  }}class App extends React.Component {  state = {    items: [      {        text: "First",        id: 1      },      {        text: "Second",        id: 2      }    ]  };  addItem = () => {    const items = [{ text: "Front", id: Date.now() }, ...this.state.items];    this.setState({ items });  };  render() {    return (      <div>        <ul>          {this.state.items.map((item, index) => (            <Item {...item} key={index} />          ))}        </ul>        <button onClick={this.addItem}>Ajouter un élément</button>      </div>    );  }}render(<App />, document.getElementById("root"));
```

Si vous utilisez `index` comme clé, voici ce qui se passe :

[**CodeSandbox**](https://codesandbox.io/embed/7ko97vnv80)  
[_CodeSandbox est un éditeur en ligne conçu pour les applications web._codesandbox.io](https://codesandbox.io/embed/7ko97vnv80)

![Image](https://cdn-media-1.freecodecamp.org/images/AG7Wjs11dx4F6d7F4lkLf6zFs622uFqOTLlt)

Et si un autre `Item` avec le texte `Second` au lieu de `Front` est inséré **à la fin** de la liste ? Voici ce qui se passe :

1. `Item est un composant non contrôlé` : Le texte que l'utilisateur écrit dans son champ `input` est stocké en tant qu'`state`
2. Un nouvel élément de données `{ text: "Front" }` est inséré au début des données de la liste.
3. La liste est réaffichée avec la valeur **index** comme `key`. Ainsi, les composants précédents sont réutilisés pour les deux premiers **éléments de données** et reçoivent les bonnes props `Front` et `First`, mais l'état n'est pas mis à jour dans `Item`. C'est pourquoi les deux premières instances de composant conservent le même texte.
4. Une nouvelle instance de composant est créée pour `key: 2` car aucune clé correspondante précédente n'est trouvée. Elle est remplie avec les `props` du dernier **élément de données de la liste** qui est `Second`.

![Image](https://cdn-media-1.freecodecamp.org/images/5wLO4ksFCdVvKeDvMDshS8FrUWoiSFOvxI6l)

Un autre point intéressant est les appels `render` qui se produisent. Item est un `PureComponent`, donc il ne se met à jour que lorsque la prop `text` (ou state) change :

```
rerendu  Frontrerendu  Firstrerendu  SecondMonté  Second
```

**Tous** les composants sont réaffichés. Cela se produit parce que l'élément avec `key: 0` est réutilisé pour le premier élément de données et reçoit ses `props`, mais le premier élément de données est maintenant le nouvel objet `Front`, déclenchant un `render`. Il en va de même pour les autres composants, car les anciens éléments de données sont maintenant tous décalés d'une place.

Alors, quelle est la solution ? La solution est simple : nous donnons à chaque élément de données de liste un `id` unique une fois **lors de la création** (pas à chaque rendu !). Toutes les instances de composants seront appariées avec leur élément de données correspondant. Ils reçoivent les mêmes `props` qu'avant, et cela évite un autre `render`.

Ignorons pour l'instant les avantages de performance qui découlent de l'utilisation d'`id`s dans les listes dynamiques. L'exemple montre que **les bugs introduits par les clés ne se produisent que jamais avec des composants _non contrôlés_**, des composants qui conservent un **état interne**.

Si nous réécrivons `Item` comme un composant contrôlé, en déplaçant l'état hors de celui-ci, le bug disparaît.

Pourquoi ? Encore une fois, parce que le bug était **la réutilisation d'un composant pour un élément de données différent**. Par conséquent, l'état interne reflétait toujours **l'état de l'élément de données précédent**, mais les **props d'un autre**. En rendant le composant contrôlé, en supprimant complètement son état, nous n'avons plus cette divergence. (Mais il y a toujours le problème des réaffichages inutiles.)

#### Abuser des clés pour corriger des composants tiers défectueux

React n'a besoin de `key`s que lors de la correspondance de plusieurs éléments, donc définir une clé sur un enfant unique n'est pas nécessaire. Mais il peut encore être utile de définir une clé sur un composant enfant unique.

Si vous changez la clé, React jettera tout le composant (le démontera), et montera une nouvelle instance de composant à sa place. Pourquoi cela pourrait-il être utile ?

Encore une fois, nous revenons aux **composants non contrôlés**. Parfois, vous utilisez un composant tiers et vous ne pouvez pas modifier son code pour le rendre contrôlé. Si un composant a un état interne et qu'il est implémenté de manière incorrecte (par exemple, l'état est dérivé uniquement **une fois** dans le constructeur, mais `getDerivedStateFromProps` / `componentWillReceiveProps` n'est pas implémenté pour **refléter les changements récurrents de `props` dans son état interne**), la boîte à outils standard de React ne peut pas vous aider ici. Il n'y a pas de `forceRemount`.

Cependant, nous pouvons simplement définir une nouvelle `key` sur ce composant pour obtenir le comportement souhaité d'initialisation complète d'un nouveau composant. L'ancien composant sera démonté, et un nouveau sera monté avec les nouvelles `props` initialisant l'`state`.

#### TL;DR :

Utiliser `index` comme clé peut :

1. entraîner des réaffichages inutiles
2. introduire des bugs lorsque les éléments de liste sont des **composants non contrôlés** mais utilisent toujours `props`

La propriété `key` peut être utilisée pour forcer un remontage complet d'un composant, ce qui peut parfois être utile.

Publié à l'origine sur [cmichel.io](https://cmichel.io/react-fun-with-keys/)

![Image](https://cdn-media-1.freecodecamp.org/images/ZpVxptp2LfM-Ia7ksRx3CnJ-dCuVnoxUBGGN)