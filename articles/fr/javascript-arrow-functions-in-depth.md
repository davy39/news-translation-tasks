---
title: Comment utiliser les fonctions fléchées JavaScript – Expliqué en détail
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-11-30T19:26:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-arrow-functions-in-depth
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/How-to-get-file-extension-with-PHP.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les fonctions fléchées JavaScript – Expliqué en détail
seo_desc: 'Hello everyone! In this article, I’m going to explain one of the most useful
  features in JavaScript: the arrow function.

  I’ll compare the arrow function with the regular function syntax, I''ll show you
  how to convert a regular function into an arrow f...'
---

Bonjour à tous ! Dans cet article, je vais expliquer l'une des fonctionnalités les plus utiles en JavaScript : la fonction fléchée.

Je vais comparer la fonction fléchée avec la syntaxe de fonction régulière, je vous montrerai comment convertir facilement une fonction régulière en une fonction fléchée, et je discuterai pourquoi la syntaxe de fonction fléchée est recommandée par rapport à la fonction régulière.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que la syntaxe des fonctions fléchées ?](#heading-quest-ce-que-la-syntaxe-des-fonctions-flechees)
2. [Comment convertir une fonction régulière en une fonction fléchée facilement](#heading-comment-convertir-une-fonction-reguliere-en-une-fonction-flechee-facilement)
3. [Pourquoi les fonctions fléchées sont recommandées par rapport aux fonctions régulières](#heading-pourquoi-les-fonctions-flechees-sont-recommandees-par-rapport-aux-fonctions-regulieres)
4. [Les fonctions fléchées sont meilleures pour les fonctions courtes](#heading-les-fonctions-flechees-sont-meilleures-pour-les-fonctions-courtes)
5. [Les fonctions fléchées ont une instruction de retour implicite](#heading-les-fonctions-flechees-ont-une-instruction-de-retour-implicite)
6. [Les fonctions fléchées n'ont pas de liaison `this`](#heading-les-fonctions-flechees-nont-pas-de-liaison-this)
7. [Quand ne pas utiliser les fonctions fléchées ?](#heading-quand-ne-pas-utiliser-les-fonctions-flechees)
8. [Conclusion](#heading-conclusion)

Commençons !

## Qu'est-ce que la syntaxe des fonctions fléchées ?

Lorsque vous devez créer une fonction en JavaScript, la méthode principale consiste à utiliser le mot-clé `function` suivi du nom de la fonction comme montré ci-dessous :

```js
function greetings(name) {
  console.log(`Hello, ${name}!`);
}

greetings('John'); // Hello, John!
```

La syntaxe des fonctions fléchées vous permet de créer une expression de fonction qui produit le même résultat que le code ci-dessus.

Voici la fonction `greetings()` à nouveau, mais en utilisant la syntaxe des fonctions fléchées :

```js
const greetings = name => {
  console.log(`Hello, ${name}!`);
};

greetings('John'); // Hello, John!
```

Lorsque vous déclarez une fonction avec la syntaxe des fonctions fléchées, vous devez assigner la déclaration à une variable afin que la fonction ait un nom.

En gros, la syntaxe des fonctions fléchées ressemble à ceci :

```js
const myFunction = (param1, param2, ...) => {
  // corps de la fonction
}
```

Dans le code ci-dessus, `myFunction` est la variable qui contient la fonction. Vous pouvez appeler la fonction en tant que `myFunction()` plus tard dans votre code.

`(param1, param2, ...)` sont les paramètres de la fonction. Vous pouvez définir autant de paramètres que nécessaire pour la fonction.

Ensuite, vous avez la flèche `=>` pour indiquer le début de la fonction. Après cela, vous pouvez écrire des accolades `{}` pour indiquer le corps de la fonction, ou les supprimer si vous avez une fonction sur une seule ligne. Plus d'informations à ce sujet plus tard.

Au début, la fonction fléchée peut sembler étrange car vous êtes habitué à voir le mot-clé `function`. Mais à mesure que vous commencez à utiliser la syntaxe fléchée, vous verrez qu'elle est très pratique et plus facile à écrire.

Permettez-moi de vous montrer une manière facile de convertir une fonction régulière en une fonction fléchée ensuite.

## Comment convertir une fonction régulière en une fonction fléchée facilement

Vous pouvez suivre ces **trois étapes faciles** pour convertir une fonction régulière en une fonction fléchée :

1. Remplacez le mot-clé `function` par le mot-clé de variable `const`
2. Ajoutez le symbole `=` après le nom de la fonction et avant les parenthèses
3. Ajoutez le symbole `=>` après les parenthèses

Habituellement, une fonction n'est jamais modifiée après la déclaration, donc nous utilisons le mot-clé `const` au lieu de `let`.

Le code ci-dessous devrait vous aider à visualiser les étapes :

```js
function greetings(name) {
  return `Hello, ${name}!`;
}

// étape 1 : remplacer function par const
const greetings(name) {
  return `Hello, ${name}!`;
}

// étape 2 : ajouter = après le nom de la fonction
const greetings = (name) {
  return `Hello, ${name}!`;
}

// étape 3 : ajouter => après les parenthèses
const greetings = (name) => {
  return `Hello, ${name}!`;
}
```

Les trois étapes ci-dessus suffisent pour convertir toute ancienne syntaxe de fonction JavaScript en la nouvelle syntaxe de fonction fléchée.

Lorsque vous avez une fonction sur une seule ligne, il y a une quatrième étape optionnelle pour supprimer les accolades et le mot-clé `return` comme suit :

```js
// de ceci
const greetings = (name) => {
  return `Hello, ${name}!`;
};

// à ceci
const greetings = (name) => `Hello, ${name}!`;
```

Lorsque vous avez exactement un paramètre, vous pouvez également supprimer les parenthèses :

```js
// de ceci
const greetings = (name) => `Hello, ${name}!`;

// à ceci
const greetings = name => `Hello, ${name}!`;
```

Mais les deux dernières étapes sont optionnelles. Seules les trois premières étapes sont nécessaires pour convertir toute fonction JavaScript créée en utilisant le mot-clé `function` en la syntaxe de fonction fléchée.

## Pourquoi les fonctions fléchées sont recommandées par rapport aux fonctions régulières

La syntaxe des fonctions fléchées offre des améliorations à la manière dont vous écrivez une fonction en JavaScript, telles que :

* Vous pouvez écrire des fonctions courtes de manière plus directe
* Pour les fonctions sur une seule ligne, l'instruction `return` peut être implicite
* Le mot-clé `this` n'est pas lié à la fonction.

Voyons comment ces améliorations fonctionnent avec des exemples pratiques ensuite.

### Les fonctions fléchées sont meilleures pour les fonctions courtes

Supposons que vous avez une fonction sur une seule ligne qui imprime une chaîne dans la console. En utilisant le mot-clé `function`, voici comment vous écrirez la fonction :

```js
function greetings(name) {
  console.log(`Hello, ${name}!`);
}
```

Si vous utilisez la syntaxe des fonctions fléchées, vous pouvez omettre les accolades, créant une fonction sur une seule ligne comme montré ci-dessous :

```js
const greetings = (name) => console.log(`Hello, ${name}!`);
```

Encore plus, vous pouvez supprimer les parenthèses qui entourent les paramètres de la fonction lorsque vous avez exactement un paramètre :

```js
const greetings = name => console.log(`Hello, ${name}!`);
```

Si votre fonction n'a pas de paramètre, alors vous devez passer des parenthèses vides entre l'assignation et la syntaxe de la flèche comme montré ci-dessous :

```js
const greetings = () => console.log(`Hello, World!`);
```

Lorsque vous utilisez la syntaxe des fonctions fléchées, les accolades sont requises uniquement lorsque votre fonction fait plus d'une seule ligne. Par exemple :

```js
const greetings = () => {
  console.log('Hello World!');
  console.log('How are you?');
};
```

Lorsque vous utilisez le mot-clé `function` régulier, vous ne pouvez pas omettre les accolades peu importe quoi.

Les fonctions fléchées sont également idéales pour les situations où vous n'avez pas besoin de nommer la fonction, comme les rappels :

```js
const myArray = [1, 2, 3];

// De ceci :
myArray.forEach(function (item) {
  console.log(item);
});

// À ceci :
myArray.forEach(item => console.log(item));
```

Ou lorsque vous devez créer une Expression de Fonction Invocable Immédiatement (IIFE) :

```js
// De ceci :
(function () {
  console.log('Hello World');
})();

// À ceci :
(() => console.log('Hello World'))();
```

Comme vous pouvez le voir, l'utilisation de la syntaxe des fonctions fléchées rend votre code beaucoup plus propre et concis.

### Les fonctions fléchées ont une instruction de retour implicite

Lorsque vous avez une fonction fléchée sur une seule ligne, l'instruction de retour sera ajoutée implicitement par JavaScript. Cela signifie que vous ne devez pas ajouter le mot-clé `return` explicitement.

Pour vous montrer ce que je veux dire, supposons que vous avez une fonction qui additionne deux nombres comme suit :

```js
function sum(a, b) {
  return a + b;
}
```

Lorsque vous écrivez la fonction ci-dessus en utilisant la syntaxe des fonctions fléchées, vous devez supprimer les accolades et le mot-clé `return` :

```js
const sum = (a, b) => a + b;
```

Si vous n'avez pas supprimé le mot-clé `return`, alors JavaScript lancera une erreur, disant qu'une accolade ouvrante `{` est attendue.

Lorsque vous utilisez des fonctions fléchées, n'écrivez l'instruction `return` explicitement que lorsque vous avez des instructions sur plusieurs lignes :

```js
const sum = (a, b) => {
  const result = a + b;
  return result;
};
```

Lorsque vous supprimez les accolades, n'oubliez pas de supprimer le mot-clé `return` si vous l'utilisez.

### Les fonctions fléchées n'ont pas de liaison `this`

Une différence significative entre la fonction fléchée et la syntaxe de fonction régulière réside dans la manière dont elles gèrent le mot-clé `this`.

Dans une fonction régulière, le mot-clé `this` fait référence à l'objet à partir duquel vous **appelez** la fonction. Dans une fonction fléchée, le mot-clé `this` fait référence à l'objet à partir duquel vous **définissez** la fonction.

Pour vous montrer ce que je veux dire, supposons que vous avez une `personne` avec les propriétés et méthodes suivantes :

```js
const person = {
  name: 'Nathan',
  skills: ['HTML', 'CSS', 'JavaScript'],

  showSkills() {
    this.skills.forEach(function (skill) {
      console.log(`${this.name} is skilled in ${skill}`);
    });
  },
};

person.showSkills();
```

Si vous exécutez le code ci-dessus, le résultat de l'appel de la méthode `showSkills()` serait :

```txt
undefined is skilled in HTML
undefined is skilled in CSS
undefined is skilled in JavaScript
```

Ici, le mot-clé `this` fait référence à l'objet global `Window` car nous avons appelé la méthode `showSkills()` en dehors de l'objet `person`.

Dans l'objet global, la propriété `name` est `undefined`. Maintenant, réécrivons la fonction de rappel en utilisant la syntaxe fléchée :

```js
const person = {
  name: 'Nathan',
  skills: ['HTML', 'CSS', 'JavaScript'],

  showSkills() {
    this.skills.forEach(skill => {
      console.log(`${this.name} is skilled in ${skill}`);
    });
  },
};

person.showSkills();
```

Exécutez le code à nouveau, et le résultat serait :

```txt
Nathan is skilled in HTML
Nathan is skilled in CSS
Nathan is skilled in JavaScript
```

Ici, le mot-clé `this` fait référence à l'objet à partir duquel la fonction fléchée est définie, qui est l'objet `person`.

Ce comportement est ce qui fait que les gens préfèrent les fonctions fléchées, car il est plus logique que `this` fasse référence à l'objet à partir duquel vous définissez cette fonction plutôt qu'à partir duquel vous l'appelez.

## Quand ne pas utiliser les fonctions fléchées ?

Les fonctions fléchées sont généralement préférées aux fonctions standard, mais il existe quelques situations où vous ne devriez pas utiliser la fonction fléchée.

L'une de ces situations est lorsque vous définissez une méthode d'objet. Revenons à notre exemple d'objet `person` ci-dessus, supposons que vous écrivez la méthode `showSkills()` comme une fonction fléchée comme ceci :

```js
const person = {
  name: 'Nathan',
  skills: ['HTML', 'CSS', 'JavaScript'],

  showSkills: () => {
    this.skills.forEach(skill => {
      console.log(`${this.name} is skilled in ${skill}`);
    });
  },
};

person.showSkills();
```

L'exécution du code ci-dessus provoquera une erreur :

```txt
TypeError: Cannot read properties of undefined (reading 'forEach')
```

À l'intérieur d'un objet, le mot-clé `this` fait référence à l'objet courant **uniquement** lorsque vous déclarez la méthode en utilisant la syntaxe standard (`methodName()` ou `methodName: function(){ }`)

Lorsque vous déclarez une méthode d'objet en utilisant la fonction fléchée, le mot-clé `this` fait référence à l'objet global, et la propriété `skills` est `undefined` là-bas. Ne jamais utiliser la fonction fléchée lors de la déclaration d'une méthode.

## Conclusion

Et c'est tout sur les fonctions fléchées. Maintenant, vous avez appris les différences entre les fonctions fléchées et les fonctions régulières, comment convertir une fonction régulière en une fonction fléchée, ainsi que quand les fonctions fléchées sont recommandées (et non recommandées !).

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !