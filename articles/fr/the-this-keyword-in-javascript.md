---
title: Comment utiliser le mot-clé "this" en JavaScript
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-01-31T23:40:14.000Z'
originalURL: https://freecodecamp.org/news/the-this-keyword-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/brad-_Js9c6w_FDk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser le mot-clé "this" en JavaScript
seo_desc: 'Hey everyone! In this article we''re going to talk about the THIS keyword
  in Javascript.

  This used to be a concept that confused me a little bit, so I''ll try to break it
  down for you so you can understand its uses and in what situations can it be usef...'
---

Salut à tous ! Dans cet article, nous allons parler du mot-clé THIS en JavaScript.

Cela a déjà été un concept qui m'a un peu confus, alors je vais essayer de le décomposer pour vous afin que vous puissiez comprendre ses utilisations et dans quelles situations il peut être utile. C'est parti !

# Table des matières

* [Qu'est-ce que le mot-clé THIS](#heading-quest-ce-que-le-mot-cle-this)
    
* [Appeler THIS seul](#heading-appeler-this-seul)
    
* [THIS dans une méthode d'objet](#heading-this-dans-une-methode-dobjet)
    
* [THIS dans une fonction](#heading-this-dans-une-fonction)
    
    * [Une note sur les fonctions fléchées](#heading-une-note-sur-les-fonctions-flechees)
        
    * [Une note sur le mode strict](#heading-une-note-sur-le-mode-strict)
        
* [THIS dans un événement](#heading-this-dans-un-evenement)
    
* [Méthodes THIS (call, apply et bind)](#heading-methodes-this-call-apply-et-bind)
    
    * [Call](#call)
        
    * [Apply](#apply)
        
    * [Bind](#bind)
        
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que le mot-clé THIS ?

D'accord, alors commençons par définir ce qu'est le mot-clé `this`. En JavaScript, le mot-clé `this` fait toujours référence à un **objet**. Le problème est que l'objet auquel il fait référence variera en fonction de la manière et de l'endroit où `this` est appelé.

Et il existe plusieurs façons d'utiliser le mot-clé `this`, alors voyons les cas les plus courants et comment il se comporte dans chacun d'eux.

Un commentaire important est que `this` n'est pas une variable – c'est un mot-clé, donc sa valeur ne peut pas être modifiée ou réassignée.

# Comment appeler `this` seul

Si nous appelons `this` seul, c'est-à-dire pas dans une fonction, un objet, ou autre chose, il fera référence à l'objet global window.

Si vous l'imprimez comme `console.log('this seul', this);` vous obtiendrez ceci dans votre console : `[object Window]`.

Ou ceci si vous l'expandez :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-367.png align="left")

*Résultat développé de l'appel de* `this` seul

# Comment appeler `this` dans une méthode d'objet

Mais si nous appelons `this` dans une méthode d'objet, comme dans l'exemple suivant :

```plaintext
const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    getThis : function() {
      return this;
    }
};

console.log('this dans une méthode d\'objet', person.getThis());
```

Nous verrons que `this` ne fait plus référence à l'objet lui-même :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-368.png align="left")

*Résultat de l'appel de* `this` dans une méthode d'objet

Et étant donné cela, nous pouvons utiliser `this` pour accéder à d'autres propriétés et méthodes du même objet :

```javascript
const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    getFullName : function() {
      return this.firstName + ' ' + this.lastName;  // Corrigé pour utiliser `this.firstName`
    }
};

console.log('this dans une méthode d\'objet', person.getFullName());
```

# Comment appeler `this` dans une fonction

Si nous appelons `this` dans une fonction comme dans l'exemple suivant :

```javascript
function test() {
    console.log('this dans une fonction', this);
}

test()
```

`this` fera maintenant référence à l'objet général window, et nous obtiendrons ceci dans notre console : `[object Window]`.

## Une note sur les fonctions fléchées

Dans les fonctions fléchées, JavaScript définit `this` de manière lexicale. Cela signifie que la fonction fléchée ne crée pas son propre [contexte d'exécution](https://www.javascripttutorial.net/javascript-execution-context/) mais hérite de `this` de la fonction externe où la fonction fléchée est définie.

Dans la plupart des cas, cela signifie que `this` fera référence à l'objet window également :

```javascript
const show = () => this

console.log('this dans une fonction fléchée', show())
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-374.png align="left")

Il est important de noter cela car, par exemple, si nous essayons d'implémenter une fonction fléchée comme méthode d'objet, nous ne pourrons pas accéder à l'objet via le mot-clé `this` :

```javascript
const person = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: () => this.name + ' ' + this.surname
}

console.log(person.sayName());
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-375.png align="left")

## Une note sur le mode strict

Lorsque vous utilisez le [mode strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode), l'appel de `this` dans une fonction retournera `undefined`.

```javascript
"use strict";

function show() {
    console.log(this);
}

show();
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-370.png align="left")

En tant que commentaire supplémentaire, si vous n'êtes pas familier avec le mode strict, selon la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) :

> Le mode strict de JavaScript est un moyen d'opter pour une variante restreinte de JavaScript, optant ainsi implicitement hors du "[mode sloppy](https://developer.mozilla.org/en-US/docs/Glossary/Sloppy_mode)". Le mode strict n'est pas seulement un sous-ensemble : il a intentionnellement des sémantiques différentes du code normal.

Le mode strict apporte plusieurs changements à la sémantique régulière de JavaScript :

* Élimine certaines erreurs silencieuses de JavaScript en les transformant en erreurs lancées.
    
* Corrige les erreurs qui rendent difficile pour les moteurs JavaScript d'effectuer des optimisations : le code en mode strict peut parfois être exécuté plus rapidement que le code identique qui n'est pas en mode strict.
    
* Interdit certaines syntaxes susceptibles d'être définies dans les futures versions d'ECMAScript.
    

# Comment utiliser `this` dans un écouteur d'événement

Lorsque vous utilisez `this` dans un écouteur d'événement, `this` fera référence à l'élément DOM qui a déclenché l'événement.

```javascript
document.getElementById('testBtn').addEventListener('click', function() {
    console.log('this dans un événement', this);
})
```

Dans notre cas, nous avons ajouté l'écouteur d'événement à un élément bouton : `<button id="testBtn">TEST</button>`

Et après avoir cliqué dessus, nous obtenons ce qui suit dans notre console :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-369.png align="left")

# Méthodes `this` (call, apply et bind)

Pour compliquer un peu le sujet, JavaScript fournit trois méthodes natives qui peuvent être utilisées pour manipuler le comportement du mot-clé `this`. Ces méthodes sont `call`, `apply` et `bind`. Voyons comment elles fonctionnent.

## Comment utiliser la méthode Call

Avec `call`, nous pouvons invoquer une méthode en passant un objet propriétaire comme argument. En d'autres termes, nous pouvons appeler une méthode en indiquant à quel objet le mot-clé `this` fera référence.

Voyons un exemple :

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function() {
        return this.name + " " + this.surname;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.call(person2));
```

Ici, nous avons deux objets person. Chacun avec ses propriétés `name` et `surname`, et l'objet `person1` a une méthode `sayName`.

Ensuite, nous appelons la méthode `sayName` de `person1` de la manière suivante : `person1.sayName.call(person2)`.

En faisant cela, nous indiquons que lorsque la méthode `sayName` s'exécute, le mot-clé `this` ne fera pas référence à l'objet qui "possède" la méthode (`person1`) mais à l'objet que nous avons passé en paramètre (`person2`). Par conséquent, nous obtenons ceci dans notre console :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-376.png align="left")

Gardez à l'esprit que si la méthode donnée accepte des arguments, nous pouvons également les passer lorsque nous l'invoquons avec `call` :

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function(city, country) {
        return this.name + " " + this.surname + ", " + city + ", " + country;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.call(person2, "DF", "Mexico"));
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-377.png align="left")

## Comment utiliser la méthode Apply

La méthode `apply` fonctionne de manière très similaire à `call`. La seule différence entre elles est que `call` accepte les paramètres sous forme de liste séparée par des virgules (comme dans le dernier exemple que nous avons vu), et `apply` les accepte sous forme de tableau.

Donc, si nous voulons reproduire le même exemple en utilisant `apply`, nous devrions le faire comme ceci :

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function(city, country) {
        return this.name + " " + this.surname + ", " + city + ", " + country;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.apply(person2, ["DF", "Mexico"]));
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-378.png align="left")

## Comment utiliser la méthode Bind

Comme `call` et `apply`, la méthode `bind` indique l'objet auquel le mot-clé `this` fera référence lorsque la méthode donnée s'exécute.

Mais la différence avec `bind` est qu'elle retournera une **nouvelle fonction**, sans l'exécuter. Alors qu'avec `call` et `apply`, la fonction s'exécute immédiatement, en utilisant `bind`, nous devons l'exécuter séparément.

Voyons cela dans un exemple :

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function() {
        return this.name + " " + this.surname
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

const sayPerson2Name = person1.sayName.bind(person2)

console.log(sayPerson2Name())
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-381.png align="left")

# Conclusion

Eh bien, à tous, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/01/baby-yoda-bye-bye-icegif.gif align="left")