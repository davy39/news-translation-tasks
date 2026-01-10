---
title: Introduction à l'opérateur de décomposition et au paramètre rest en JavaScript
  (ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T16:53:29.000Z'
originalURL: https://freecodecamp.org/news/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lC-MTayAodosjbtLk8zL1A.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Introduction à l'opérateur de décomposition et au paramètre rest en JavaScript
  (ES6)
seo_desc: 'By Joanna Gaudyn

  Both the spread operator and the rest parameter are written as three consecutive
  dots (…). Do they have anything else in common?


  _[source](https://unsplash.com/photos/8AJuvX4hzws" rel="noopener" target="blank"
  title=")

  The spread op...'
---

Par Joanna Gaudyn

#### L'opérateur de décomposition et le paramètre rest s'écrivent tous deux sous la forme de trois points consécutifs (…). Ont-ils autre chose en commun ?

![Image](https://cdn-media-1.freecodecamp.org/images/xVf5V7-nilHXYj2WtcgAgE8QNW-DY6I23NS5)
_[source](https://unsplash.com/photos/8AJuvX4hzws" rel="noopener" target="_blank" title=")_

### L'opérateur de décomposition (…)

L'opérateur de décomposition a été introduit dans ES6. Il vous permet de développer des [objets itérables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#Iterators) en plusieurs éléments. Que signifie-t-il vraiment ? Vérifions quelques exemples.

```
const movies = ["Leon", "Love Actually", "Lord of the Rings"];console.log(...movies);
```

Affiche :

> Leon Love Actually Lord of the Rings

```
const numbers = new Set([1, 4, 5, 7]);console.log(...numbers);
```

Affiche :

> 1 4 5 7

Vous avez peut-être remarqué que le tableau du premier exemple et le set du second ont été développés en leurs éléments individuels (respectivement des chaînes de caractères et des chiffres). Comment cela peut-il être utile, pourriez-vous demander.

L'utilisation la plus courante est probablement la combinaison de tableaux. Si vous avez déjà dû faire cela avant l'opérateur de décomposition, vous avez probablement utilisé la méthode `concat()`.

```
const shapes = ["triangle", "square", "circle"];const objects = ["pencil", "notebook", "eraser"];const chaos = shapes.concat(objects);console.log(chaos);
```

Affiche :

> ["triangle", "square", "circle", "pencil", "notebook", "eraser"]

Ce n'est pas trop mal, mais ce que l'opérateur de décomposition offre est un raccourci, qui rend votre code bien plus lisible également :

```
const chaos = [...shapes, ...objects];console.log(chaos);
```

Affiche :

> ["triangle", "square", "circle", "pencil", "notebook", "eraser"]

Voici ce que nous obtiendrions si nous essayions de faire la même chose _sans_ l'opérateur de décomposition :

```
const chaos = [shapes, objects];console.log(chaos);
```

Affiche :

> [Array(3), Array(3)]

Que s'est-il passé ici ? Au lieu de combiner les tableaux, nous avons obtenu un tableau `chaos` avec le tableau `shapes` à l'index 0 et le tableau `objects` à l'index 1.

![Image](https://cdn-media-1.freecodecamp.org/images/FWmzdtMxBzeGEB1G5byEABuOfQOA6QkCu82f)
_[source](https://unsplash.com/photos/DJpJDdeCrag" rel="noopener" target="_blank" title=")_

### Le paramètre rest (…)

Vous pouvez considérer le paramètre rest comme l'opposé de l'opérateur de décomposition. Tout comme l'opérateur de décomposition vous permet de développer un tableau en ses éléments individuels, le paramètre rest vous permet de regrouper des éléments dans un tableau.

#### Assigner les valeurs d'un tableau à des variables

Regardons l'exemple suivant :

```
const movie = ["Life of Brian", 8.1, 1979, "Graham Chapman", "John Cleese", "Michael Palin"];const [title, rating, year, ...actors] = movie;console.log(title, rating, year, actors);
```

Affiche :

> "Life of Brian", 8.1, 1979, ["Graham Chapman", "John Cleese", "Michael Palin"]

Le paramètre rest nous a permis de prendre les valeurs du tableau `movie` et de les assigner à plusieurs variables individuelles en utilisant la [décomposition](https://medium.com/@aska.gaudyn/destructuring-in-javascript-es6-ee963292623a). Ainsi, `title`, `rating` et `year` se voient assigner les trois premières valeurs du tableau, mais c'est avec `actors` que la vraie magie opère. Grâce au paramètre rest, `actors` se voit assigner les valeurs restantes du tableau `movie`, sous forme de tableau.

#### Fonctions variadiques

Les fonctions variadiques sont des fonctions qui prennent un nombre indéfini d'arguments. Un bon exemple est la fonction `sum()` : nous ne pouvons pas savoir à l'avance combien d'arguments lui seront passés :

```
sum(1, 2);sum(494, 373, 29, 2, 50067);sum(-17, 8, 325900);
```

Dans les versions antérieures de JavaScript, ce type de fonction était géré en utilisant l'[objet arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments), qui est un objet de type tableau, disponible en tant que variable locale dans chaque fonction. Il contient toutes les valeurs des arguments passés à une fonction. Voyons comment la fonction `sum()` pourrait être implémentée :

```
function sum() {  let total = 0;    for(const argument of arguments) {    total += argument;  }  return total;}
```

Cela fonctionne, mais c'est loin d'être parfait :

* Si vous regardez la définition de la fonction `sum()`, elle n'a aucun paramètre. Cela peut être assez trompeur.
* Cela peut être difficile à comprendre si vous n'êtes pas familier avec l'objet arguments (comme dans : d'où viennent les `arguments` ?!)

Voici comment nous écririons la même fonction avec le paramètre rest :

```
function sum(...nums) {  let total = 0;    for(const num of nums) {    total += num;  }  return total;}
```

Notez que la boucle `for...in` a été remplacée par la boucle `[for...of](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)`. Nous avons rendu notre code plus lisible et concis en même temps.

Alléluia ES6 !

Commencez-vous tout juste votre voyage dans la programmation ? Voici quelques articles qui pourraient également vous intéresser :

* [Un bootcamp de codage est-il fait pour vous ?](https://medium.freecodecamp.org/is-a-coding-bootcamp-something-for-you-974c3b5bd3b2)
* [Le changement de carrière est-il vraiment possible ?](https://medium.com/datadriveninvestor/is-career-change-really-possible-c29c9a0d791c)
* [Pourquoi Ruby est un excellent langage pour commencer la programmation](https://medium.com/@aska.gaudyn/why-ruby-is-a-great-language-to-start-programming-with-2f17e0c2907a)