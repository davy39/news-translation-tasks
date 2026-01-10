---
title: 'Fonctions d''ordre supérieur : ce qu''elles sont, et un exemple avec React'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T16:58:06.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-what-they-are-and-a-react-example-1d2579faf101
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x4AH7NNM6KIASH0-9dOKOg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Fonctions d''ordre supérieur : ce qu''elles sont, et un exemple avec React'
seo_desc: 'By Amber Wilkie

  Tech Jargon series


  There are so many phrases that get thrown around at tech meetups and conferences,
  assuming that everyone is already down with the lingo. I’m often not down with the
  lingo. It’s common for developers to act astonish...'
---

Par Amber Wilkie

#### Série Jargon Technique

![Image](https://cdn-media-1.freecodecamp.org/images/54ciU297spnDIrc59mWwUo7S7XHaCjkFzKbs)

Il y a tant de phrases qui sont lancées lors des rencontres et conférences technologiques, en supposant que tout le monde maîtrise déjà le jargon. Je ne maîtrise souvent pas ce jargon. Il est courant que les développeurs fassent semblant d'être surpris que je manque d'une connaissance.

La vérité est que je ne connais souvent tout simplement pas le bon terme pour cela. En tant qu'êtres humains, mais surtout en tant que développeurs, nous aimons écarter ceux qui ne "parlent pas le langage", donc cette série vise à obtenir une compréhension solide des concepts de programmation que l'on "devrait connaître".

Mon premier sujet pour cette série est les Fonctions d'Ordre Supérieur. J'étais à une rencontre technologique l'autre jour, et nous discutions de React et de la difficulté pour les nouveaux venus à React de se plonger dans le code. J'ai mentionné que les composants d'ordre supérieur (HOCs) peuvent être difficiles à comprendre. Une réponse a été qu'ils sont très similaires aux fonctions d'ordre supérieur, n'est-ce pas ? Et j'ai dit : "Je ne sais pas ce que c'est." Lorsque j'ai demandé un exemple, on m'a répondu "map". J'ai fait une blague sur le fait que je n'avais aucune idée de ce qu'est "map" et nous avons continué.

Mais toujours : _qu'est-ce qu'une fonction d'ordre supérieur ?_

(Note : tous les exemples donnés sont en Javascript, mais ce concept s'applique à tous les langages de programmation.)

### Fonctions d'ordre supérieur : une définition

**Une fonction d'ordre supérieur est une fonction qui soit a) prend une fonction comme argument ou b) retourne une fonction.**

Si une fonction ne fait aucune de ces deux choses, c'est une **fonction de premier ordre**.

### Map

Commençons par l'exemple qui m'a été donné : `map`.

```
[1, 2, 3].map(num => num * 2)> [2, 4, 6]
```

La fonction `map` est appelée sur un tableau et prend une fonction de "rappel". Elle applique la fonction à chacun des éléments du tableau, retournant un nouveau tableau. `[1, 2, 3]` est notre tableau et `num => num * 2` est notre fonction. Un rappel est l'argument de fonction passé à notre fonction d'ordre supérieur.

Cette fonction d'ordre supérieur est intégrée au langage, prototypée sur Array (`Array.prototype.map`).

D'autres exemples de fonctions d'ordre supérieur prototypées sur Array sont `filter`, `reduce`, et `some`.

### Exemple personnalisé

Alors écrivons notre propre fonction d'ordre supérieur.

#### Fonction passée

```
const myFunc = age => age * 2
```

#### Fonction d'ordre supérieur

Maintenant, nous écrivons une fonction qui _prend en entrée_ une fonction.

```
const hof = (customFunc, age) => customFunc(age + 5) 
```

Nous allons passer un nombre à `hof`, qui ajoutera 5 puis appellera notre fonction passée, qui le doublera. Si nous passons 10, nous passons 15 à notre première fonction, qui le double ensuite pour obtenir 30.

![Image](https://cdn-media-1.freecodecamp.org/images/aKsJnW5DCylTlQKXyu9UyJw8bBCyPowmj7DP)
_Notre fonction d'ordre supérieur ultra-simple s'exécutant dans le terminal_

### Exemple personnalisé avec des "composants" React

Comme je l'ai noté ci-dessus, ce sujet est venu en référence aux composants de React. Comme un composant React est une fonction, lorsque nous le passons à une autre fonction, nous créons notre propre fonction d'ordre supérieur, que React appelle "composants d'ordre supérieur". Si vous utilisez des composants avec état (et étendez le `Component` de React), vous utilisez déjà des HOCs.

#### Composant sans état

```
const details = ({ name, randomNum }) =>
  `${name}, ${randomNum}`
```

Nous avons une fonction, appelée `details`, dans laquelle nous passons `props`. Nous les déstructurons à leur arrivée et les assignons à des variables locales `name` et `randomNum`. Il s'agit de la syntaxe ES6 — si elle vous semble étrangère, cherchez-la sur Google (vous allez l'adorer).

Il s'agit d'une **fonction de premier ordre** — elle prend un argument (un objet `props`) et retourne un littéral de gabarit.

#### Composant d'ordre supérieur

```
const hoc = (component, props) => {
  const randomNum = Math.floor(Math.random() * 100)
  return component({ ...props, randomNum })
}
```

Il s'agit d'une **fonction d'ordre supérieur** — elle prend en entrée une fonction (le `component`, qu'elle appelle ensuite, en passant des props supplémentaires). Il s'agit d'un exemple extrêmement basique de ce que fait chaque composant React sans état.

![Image](https://cdn-media-1.freecodecamp.org/images/2YbPxStADhhj3jspS8lc4-qDi4l1MbZONtZb)
_Notre "composant" super-basique s'exécutant dans la console_

Vous pouvez employer ce modèle pour abstraire le code qui est partagé parmi de nombreux composants dans votre application.

Vous vous demandez si vous pouvez imbriquer des fonctions d'ordre supérieur ? Vous pouvez ! Mais soyez prudent. Les abstractions devraient rendre le code _plus facile à lire et à utiliser_. Il est facile de se retrouver dans une situation où votre code est si obscur que personne ne peut comprendre comment faire quoi que ce soit.

### Références

* [Higher-order-function](https://en.wikipedia.org/wiki/Higher-order_function), Wikipedia
* [Higher-order functions](https://eloquentjavascript.net/05_higher_order.html), Eloquent Javascript (chapitre 5)
* `[Array.prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/prototype)` [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/prototype).