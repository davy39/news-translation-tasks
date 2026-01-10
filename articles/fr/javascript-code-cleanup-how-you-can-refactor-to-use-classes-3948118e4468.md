---
title: 'Nettoyage du code JavaScript : comment refactoriser pour utiliser des Classes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T19:31:37.000Z'
originalURL: https://freecodecamp.org/news/javascript-code-cleanup-how-you-can-refactor-to-use-classes-3948118e4468
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vBiTug8cUn6ARgwJeSZv1Q.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Nettoyage du code JavaScript : comment refactoriser pour utiliser des
  Classes'
seo_desc: 'By Amber Wilkie

  In smaller React projects, keeping all of your component methods in the components
  themselves works well. In medium-sized projects, you may find yourself wishing you
  could get those methods out of your components and into a “helper”. ...'
---

Par Amber Wilkie

Dans les petits projets React, le fait de garder toutes vos méthodes de composant dans les composants eux-mêmes fonctionne bien. Dans les projets de taille moyenne, vous pourriez vous surprendre à souhaiter sortir ces méthodes de vos composants et les placer dans un « helper ». Ici, je vais vous montrer comment utiliser une Classe (au lieu d'exporter des fonctions et variables individuelles) pour organiser votre code.

**Note** : Je travaille avec React, donc c'est l'exemple que nous allons discuter ici.

### Refactorisation typique

Dans une refactorisation typique, vous prenez une fonction du composant et la déplacez vers un autre helper.

De :

```js
const MyComponent = () => {
  const someFunction = () => 'Hey, I am text'
  return (
    <div>
      {someFunction()}
    </div>
  )
}
```

À :

```js
import { someFunction } from 'functionHelper.js'
const MyComponent = () => {
  return (
    <div>
      {someFunction()}
    </div>
  )
}
```

et

```
export const someFunction = () => 'Hey, I am text'
```

Cet exemple est vraiment simpliste, mais vous voyez où nous allons :

1. Prenez vos fonctions et copiez-les dans un fichier séparé
2. Importez-les et appelez-les normalement.

Quand les choses se compliquent, cependant, vous devrez passer un tas de choses à ces fonctions — des objets, des fonctions pour manipuler l'état, et ainsi de suite. Aujourd'hui, je suis tombée sur un problème où je voulais extraire trois fonctions d'un composant et elles nécessitaient toutes les mêmes entrées (une `resource` et une fonction pour mettre à jour la `resource`). Il doit y avoir une meilleure façon...

### Refactorisation avec une classe

J'ai fait une grande démonstration pour cet article. Vous pouvez voir le code [sur Github](https://github.com/AmberWilkie/class-demo). Le commit initial montre toutes les fonctionnalités à l'intérieur du composant principal (`App.js`) et les commits suivants refactorisent le code pour utiliser une classe.

![Image](https://cdn-media-1.freecodecamp.org/images/gYagZlg9McGFcj763-OOKtIBZjjiGEoOLbjZ)

Vous pouvez exécuter cela vous-même et en faire ce que vous voulez. N'oubliez pas de faire `yarn install`.

Nous commençons avec un composant qui « récupère » un objet (en imitant la façon dont nous pourrions le faire à partir d'une API) avec certains attributs : repeat (nombre de boîtes), side (hauteur et largeur), text, color. Nous avons ensuite plusieurs façons de manipuler la vue — changer la couleur, mettre à jour le texte, et ainsi de suite. Après chaque changement, nous affichons un message.

Par exemple, voici notre méthode pour changer la largeur et la hauteur :

```js
changeSide = side => {
  const obj = {...this.state.obj, side}
  this.fetchObject(obj);
  this.setState({ message: `You changed the sides to ${side} pixels!` });
}
```

Nous pourrions avoir un certain nombre d'autres méthodes qui nécessitent des actions similaires — ou peut-être des méthodes très différentes. Nous pourrions commencer à penser à extraire ce code vers un helper. Ensuite, nous créerions une méthode différente pour appeler l'action `setState` et nous devrions la passer, ainsi que `this.fetchObject`, l'objet dans l'état, et le `side` que nous recevons en tant qu'argument de la méthode. Si nous avons plusieurs méthodes similaires, cela fait beaucoup de passage de paramètres et peut-être que ce n'est pas vraiment utile (ou lisible).

Au lieu de cela, nous pouvons utiliser une classe, complète avec une méthode constructeur :

```js
export default class ObjectManipulator {
  constructor( { object, fetchObject, markResettable, updateMessage, updateStateValue } ) {
    this.fetchObject = fetchObject;
    this.markResettable = markResettable;
    this.updateMessage = updateMessage;
    this.updateStateValue = updateStateValue;
  }

  changeSide = ( object, side ) => {
    const newObject = { ...object, side };
    this.fetchObject(newObject);
    this.updateMessage(`You changed the sides to ${side} pixels!`);
    this.markResettable();
    this.updateStateValue('side', side);
  };
};
```

Cela nous permet de créer un objet dont les fonctions peuvent être appelées à l'intérieur de notre composant principal :

```js
const manipulator = new ObjectManipulator({
  object,
  fetchObject: this.fetchObject,
  markResettable: this.markResettable,
  updateMessage: this.updateMessage,
  updateStateValue: this.updateStateValue,
});
```

Cela crée un objet `manipulator` — une instance de notre classe `ObjectManipulator`. Lorsque nous appelons `manipulator.changeSide(object, '800')`, cela exécutera la méthode `changeSide` que nous avons définie ci-dessus. Il n'est pas nécessaire de passer `updateMessage` ou l'une des autres méthodes — nous les récupérons à partir du constructeur, lorsque nous avons créé l'instance.

Vous pouvez imaginer que cela devient vraiment utile si nous avons beaucoup de ces méthodes à gérer. Dans mon cas, je devais appeler `.then(res => myFunction(res))` après tout ce que j'essayais d'extraire. Définir `myFunction` sur l'instance de la classe au lieu de la passer à chaque fonction m'a fait économiser beaucoup de code.

### Garder tout organisé

Cette méthode d'organisation peut être vraiment utile pour garder tout à sa place. Par exemple, j'ai un tableau de couleurs que je parcours pour obtenir les boutons de couleur que vous voyez dans l'exemple. En déplaçant cette constante dans `ObjectManipulator`, je peux m'assurer qu'elle n'entre pas en conflit avec d'autres `colors` dans le reste de mon application :

```js
export default class ObjectManipulator {
  [...]

  colors = ['blue', 'red', 'orange', 'aquamarine', 'green', 'gray', 'magenta'];
};
```

Je peux utiliser `manipulator.colors` pour obtenir les bonnes couleurs pour cette page, alors qu'il pourrait y avoir une constante globale `colors` utilisée pour autre chose.

### Références

[La bonne vieille documentation Mozilla sur les Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)