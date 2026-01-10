---
title: Que se passe-t-il lorsque vous gélez un prototype en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-03T07:34:33.000Z'
originalURL: https://freecodecamp.org/news/what-happens-when-you-freeze-a-prototype
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/DSC03702.JPG
tags:
- name: JavaScript
  slug: javascript
seo_title: Que se passe-t-il lorsque vous gélez un prototype en JavaScript
seo_desc: 'By Cristian Salcescu

  Have you wondered what happens when you freeze the prototype of an object? Let''s
  find out together.

  Objects

  In JavaScript, objects are dynamic collections of properties with a “hidden” property.
  We start by creating such an objec...'
---

Par Cristian Salcescu

Vous êtes-vous déjà demandé ce qui se passe lorsque vous gélez le prototype d'un objet ? Découvrons-le ensemble.

## Objets

En JavaScript, les objets sont des collections dynamiques de propriétés avec une propriété "cachée". Nous commençons par créer un tel objet en utilisant la syntaxe littérale des objets.

```js
const counter = {
  count: 0,
  
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }  
}

console.log(counter.increment())
```

`counter` est un objet avec un champ et deux méthodes qui opèrent sur celui-ci.

## Prototypes

Les objets peuvent hériter de propriétés à partir de prototypes. En fait, l'objet `counter` hérite déjà de l'objet `Object.prototype`.

Par exemple, nous pouvons appeler la méthode `toString()` sur l'objet `counter` même si nous ne l'avons pas définie.

```js
counter.toString();
```

La meilleure façon de travailler avec les prototypes est d'extraire les méthodes dans le prototype et ensuite de les partager entre tous les objets ayant le même comportement. Faisons cela en utilisant [Object.create()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create).

```js
const counterPrototype = {
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }
}

const counter = Object.create(counterPrototype);
counter.count = 0;
console.log(counter.increment())
//1
```

La méthode `Object.create()` crée un nouvel objet, en utilisant un objet existant comme prototype du nouvel objet. `counter` a `counterPrototype` comme prototype.

Le système de prototypes est flexible mais présente certains inconvénients. Toutes les propriétés sont publiques et peuvent être modifiées.

Par exemple, nous pouvons redéfinir l'implémentation de l'objet `increment()` dans l'objet `counter`.

```js
const counter = Object.create(counterPrototype);
counter.count = 0;

counter.increment = function(){
  console.log('increment')
}

console.log(counter.increment());
//"increment"
```

## Geler les prototypes

Voyons ce qui se passe si nous gelons le prototype. Geler un objet ne nous permet pas d'ajouter, de supprimer ou de modifier ses propriétés.

```js
const counterPrototype = Object.freeze({
  increment(){
    this.count += 1;
    return this.count;
  },
  
  decrement(){
    this.count -= 1;
    return this.count
  }
});

counterPrototype.increment = function(){
  console.log('increment')
}
//Impossible d'assigner à la propriété en lecture seule 'increment' de l'objet '#'
```

La méthode `Object.freeze()` gèle un objet. Un objet gelé ne peut plus être modifié. Nous ne pouvons pas ajouter, éditer ou supprimer de propriétés.

Regardons maintenant ce qui se passe lorsque nous essayons de modifier la méthode dans l'objet `counter` héritant de `counterPrototype`.

```js
const counter = Object.create(counterPrototype);
counter.count = 0;

counter.increment = function(){
  console.log('increment')
}
//Impossible d'assigner à la propriété en lecture seule 'increment' de l'objet

console.log(counter.increment());
//1
```

Comme vous pouvez le voir, maintenant que le prototype est gelé, nous ne sommes pas en mesure de modifier la méthode `increment()` dans l'objet `counter`.

## Récapitulatif

Les objets ont une propriété cachée qui fait référence à leur prototype.

Le prototype est généralement utilisé pour conserver les méthodes qui sont partagées entre différents objets.

Geler le prototype ne nous permet pas de modifier ces propriétés dans les objets héritant de ce prototype. Les autres propriétés peuvent être modifiées.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs livres sur la programmation fonctionnelle**](https://bookauthority.org/books/best-functional-programming-books) par BookAuthority !

Pour en savoir plus sur l'application des techniques de programmation fonctionnelle à React, consultez **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2).