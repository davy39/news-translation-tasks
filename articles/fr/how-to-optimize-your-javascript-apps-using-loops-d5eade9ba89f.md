---
title: Comment optimiser vos applications JavaScript en utilisant des boucles
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-04-15T16:57:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-your-javascript-apps-using-loops-d5eade9ba89f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lTVOyrPN6uiYJKCVmuBxtQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment optimiser vos applications JavaScript en utilisant des boucles
seo_desc: 'Everyone wants high-performance apps — so in this post, we’ll learn how
  to achieve that goal.

  One of the easiest and most neglected things you can do to boost the performance
  of your JavaScript applications is to learn how to write properly high perf...'
---

Tout le monde veut des applications haute performance — alors dans cet article, nous allons apprendre comment atteindre cet objectif.

L'une des choses les plus faciles et les plus négligées que vous pouvez faire pour améliorer la performance de vos applications JavaScript est d'apprendre à écrire des instructions de boucle performantes. L'idée de cet article est de vous aider dans cette démarche.

> *Nous verrons les principaux types de boucles utilisées en JavaScript et comment nous pouvons les écrire de manière performante.*

Commençons !

### Performance des boucles

En matière de performance des boucles, le débat porte toujours sur la boucle à utiliser. Quelle est la plus rapide et la plus performante ? La vérité est que, parmi les quatre types de boucles fournies par JavaScript, une seule est significativement plus lente que les autres — la boucle `for-in`. *Le choix du type de boucle doit être basé sur vos besoins plutôt que sur des préoccupations de performance*.

Il y a deux facteurs principaux qui contribuent à la performance des boucles — **le travail effectué par itération** et **le nombre d'itérations**.

Dans les sections suivantes, nous verrons comment, en les réduisant, nous pouvons avoir un impact global positif sur la performance des boucles.

### Boucle For

ECMA-262 (la spécification qui définit la syntaxe de base et le comportement de JavaScript), dans sa troisième édition, définit quatre types de boucles. La première est la boucle `for` standard, qui partage sa syntaxe avec d'autres langages de type C :

```js
for (var i = 0; i < 10; i++){    // corps de la boucle}
```

Il s'agit probablement de la structure de boucle JavaScript la plus couramment utilisée. Pour comprendre comment nous pouvons optimiser son fonctionnement, nous devons la disséquer un peu.

#### Dissection

La boucle `for` se compose de quatre parties : initialisation, condition de pré-test, corps de la boucle et post-exécution. Voici comment elle fonctionne : d'abord, le code d'initialisation est exécuté (var i = 0 ;). Ensuite, la condition de pré-test (i < 10 ;). Si la condition de pré-test est évaluée à `true`, alors le corps de la boucle est exécuté. Après cela, le code de post-exécution (i++) est exécuté.

#### Optimisations

La première étape pour optimiser la quantité de travail dans une boucle consiste à minimiser le nombre de recherches de membres d'objets et d'éléments de tableau.

Vous pouvez également augmenter la performance des boucles en inversant leur ordre. En JavaScript, inverser une boucle entraîne une légère amélioration des performances, à condition que vous éliminiez les opérations supplémentaires.

Les deux affirmations ci-dessus sont également valables pour les deux autres boucles plus rapides (`while` et `do-while`).

```js
// boucle originale
for (var i = 0; i < items.length; i++){
    process(items[i]);
}
// minimiser les recherches de propriétés
for (var i = 0, len = items.length; i < len; i++){
    process(items[i]);
}
// minimiser les recherches de propriétés et inverser
for (var i = items.length; i--; ){
    process(items[i]);
}
```

### Boucle While

Le deuxième type de boucle est la boucle `while`. Il s'agit d'une simple boucle de pré-test, composée d'une condition de pré-test et d'un corps de boucle.

```js
var i = 0;
while(i < 10){
    // corps de la boucle
    i++;
}
```

#### Dissection

Si la condition de pré-test est évaluée à `true`, le corps de la boucle est exécuté. Sinon, il est ignoré. Chaque boucle `while` peut être remplacée par une boucle `for` et vice versa.

#### Optimisations

```js
// boucle originale
var j = 0;
while (j < items.length){
    process(items[j++]);
}
// minimiser les recherches de propriétés
var j = 0,
    count = items.length;
while (j < count){
    process(items[j++]);
}
// minimiser les recherches de propriétés et inverser
var j = items.length;
while (j--){
    process(items[j]);
}
```

### Boucle Do-While

`do-while` est le troisième type de boucle et c'est la seule boucle de post-test en JavaScript. Elle est composée d'un corps de boucle et d'une condition de post-test :

```js
var i = 0;
do {
    // corps de la boucle
} while (i++ < 10);
```

#### Dissection

Dans ce type de boucle, le corps de la boucle est toujours exécuté au moins une fois. Ensuite, la condition de post-test est évaluée, et si elle est `true`, un autre cycle de boucle est exécuté.

#### Optimisations

```js
// boucle originale
var k = 0;
do {
    process(items[k++]);
} while (k < items.length);
// minimiser les recherches de propriétés
var k = 0,
    num = items.length;
do {
    process(items[k++]);
} while (k < num);
// minimiser les recherches de propriétés et inverser
var k = items.length - 1;
do {
    process(items[k]);
} while (k--);
```

### Boucle For-In

Le quatrième et dernier type de boucle s'appelle la boucle `for-in`. Elle a un but très spécial — **énumérer les propriétés nommées de tout objet JavaScript.** Voici à quoi elle ressemble :

```js
for (var prop in object){
    // corps de la boucle
}
```

#### Dissection

Elle n'est similaire à la boucle `for` *standard* que par son nom. La façon dont elle fonctionne est totalement différente. Et cette différence la rend beaucoup plus lente que les trois autres boucles, qui ont des caractéristiques de performance équivalentes telles qu'il n'est pas utile d'essayer de déterminer laquelle est la plus rapide.

À chaque exécution de la boucle, la variable `prop` contient le nom d'une autre propriété, qui est une *chaîne de caractères*, de l'`object`. Elle s'exécutera jusqu'à ce que toutes les propriétés aient été retournées. Il s'agira des propriétés de l'objet lui-même, ainsi que de celles héritées via sa chaîne de prototypes.

#### **Notes**

**Vous ne devriez jamais utiliser « `for-in` » pour itérer sur les membres d'un tableau.**

Chaque itération de cette boucle entraîne une recherche de propriété soit sur l'instance, soit sur le prototype, ce qui rend la boucle `for-in` beaucoup plus lente que les autres boucles. Pour le même nombre d'itérations, elle pourrait être sept fois plus lente que les autres.

### Conclusion

* Les boucles `for`, `while` et `do-while` ont toutes des caractéristiques de performance similaires, et donc aucun type de boucle n'est significativement plus rapide ou plus lent que les autres.

* Évitez la boucle `for-in` sauf si vous devez itérer sur un nombre de propriétés d'objet inconnues.

* Les meilleures façons d'améliorer la performance des boucles sont de **réduire la quantité de travail effectué par itération et de réduire le nombre d'itérations de boucle**.

J'espère que cela vous a été utile, comme cela l'a été pour moi !

Merci d'avoir lu.

### Ressources

« [High Performance JavaScript](https://www.amazon.com/High-Performance-JavaScript-Application-Interfaces/dp/059680279X) » — Nicholas C. Zakas

Lisez plus de mes articles sur [mihail-gaberov.eu](https://mihail-gaberov.eu/optimizing-javascript-apps-loops/).