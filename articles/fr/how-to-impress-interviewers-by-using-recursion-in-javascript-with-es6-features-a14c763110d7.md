---
title: Comment impressionner les recruteurs en utilisant la récursivité en JavaScript
  avec les fonctionnalités ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-impress-interviewers-by-using-recursion-in-javascript-with-es6-features-a14c763110d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*krm8DV5lopMRYxuH0DevlQ.jpeg
tags:
- name: ES6
  slug: es6
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment impressionner les recruteurs en utilisant la récursivité en JavaScript
  avec les fonctionnalités ES6
seo_desc: 'By Hugo Di Francesco

  There’s nothing as flashy and useful for JavaScript interviews than recursion.

  If you just want to be impressive with recursion in JavaScript, here are some semi
  real-world (technical test type) examples.

  The short definition of ...'
---

Par Hugo Di Francesco

Rien n'est aussi impressionnant et utile pour les entretiens JavaScript que la récursivité.

Si vous voulez simplement impressionner avec la récursivité en JavaScript, voici quelques exemples semi-réalistes (du type test technique).

La définition courte d'une solution récursive à un problème (en informatique) est : n'utilisez pas l'itération. Cela signifie généralement qu'une fonction doit s'appeler elle-même avec une instance plus petite du même problème. Elle le fait jusqu'à ce qu'elle atteigne un cas trivial (généralement défini dans le problème).

Ainsi, la récursivité est composée de quelques étapes.

Dans cet article, nous discuterons de :

* ? Récursivité pour envelopper des requêtes HTTP séquentielles
* ? Compter le nombre de caractères

Les exemples de cet article sont également disponibles sur [ObervableHQ](http://beta.observablehq.com/), qui est un outil super cool permettant de créer des notebooks JavaScript :

* [Récursivité pour envelopper des requêtes HTTP séquentielles](https://beta.observablehq.com/@hugodf/recursion-to-wrap-http-requests)
* [Compter le nombre de caractères](https://beta.observablehq.com/@hugodf/count-something-in-something-else)

# ? Récursivité pour envelopper des requêtes HTTP séquentielles

Supposons que vous deviez obtenir plusieurs pages d'une API REST et que vous soyez obligé d'utiliser le module HTTPS natif ([exemple ici](https://beta.observablehq.com/@hugodf/recursion-to-wrap-http-requests)). Dans cette situation, nous allons récupérer des commentaires depuis l'API Reddit.

Avec cette API :

* s'il y a plus de commentaires que ce qui peut tenir dans une réponse, elle retournera un champ `after` dans les données. Cela peut être utilisé comme paramètre de requête pour obtenir le prochain lot de commentaires
* s'il n'y a plus de commentaires, `after` sera falsy

Cela définit nos cas de terminaison et récursifs. Nous récupérons les données de l'API Reddit et ensuite soit :

* `after` est falsy → **cas de terminaison**, retourner les données
* `after` est défini → **cas récursif**, le passer pour récupérer la page suivante ainsi que les données retournées par l'appel actuel

Un des trucs utilisés ici est de passer un tableau `data` vide dans la fonction `recursiveCommentFetch` dès le premier passage. Cela nous permet de continuer à injecter de plus en plus de valeurs au fur et à mesure que nous passons par chaque appel récursif. Nous sommes capables de résoudre l'ensemble complet au cas de terminaison.

```js
const fetch = require('node-fetch');
const user = 'hugo__df';
function makeRedditCommentUrl(user, queryParams) {
  return `https://www.reddit.com/user/${user}/comments.json?${
    Object.entries(queryParams)
      .filter(([k, v]) => Boolean(v))
      .map(
        ([k, v]) => `${k}=${v}`
      ).join('&')
  }`;
}
function recursiveCommentFetch(user, data = [], { after, limit = 100 } = {}) {
  const url = makeRedditCommentUrl(user, { after, limit });
  return fetch(url)
    .then(res => res.json())
    .then(res => {
      const { after, children } = res.data;
      const newData = [...data, ...children];
      if (after) {
        // cas récursif, il y a un moyen de récupérer plus de commentaires
        return recurseCommentFetch(user, newData, { after });
      }
      // cas de base ou de terminaison
      return newData;
    });
}
recursiveCommentFetch(user)
  .then(comments => console.log(comments));
```

Je me suis familiarisé avec cette API en créant la visualisation suivante pour les contributions Reddit (dans le style du graphique de contributions de GitHub). [Voir ici](https://beta.observablehq.com/@hugodf/reddit-contributions-per-week-graph). La [version blog est également en ligne](https://accountableblogging.com/post-frequency).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/0_H5rcQi_HW8UZTipm.png)

# ? Compter le nombre de caractères

Lorsque la question est du type : « étant donné une entrée, retourner un objet contenant le nombre de fois où chaque caractère est présent dans l'entrée », vous utiliserez cette méthode.

Il y a une [démo en direct ici](https://beta.observablehq.com/@hugodf/count-something-in-something-else).

Le cas de terminaison et le cas récursif ne sont pas immédiatement évidents, donc il y a quelques sauts ici :

1. comprendre qu'une entrée peut être convertie en une chaîne, qui peut être `.split` en un tableau (c'est-à-dire que la plupart des entrées arbitraires peuvent être converties en un tableau).
2. savoir comment parcourir un tableau de manière récursive. C'est probablement l'une des choses les plus faciles/les plus courantes à parcourir de manière récursive. Mais cela prend quelques fois pour commencer à se sentir à l'aise de le faire.

Cela nous donne la situation suivante pour une fonction récursive :

* la liste/le tableau de caractères est vide → **cas de terminaison**, retourner la carte `characterToCount`
* la liste/le tableau de caractères n'est pas vide → **cas récursif**, mettre à jour `characterToCountMap` en incrémentant/initialisant l'entrée du caractère actuel. Appeler la fonction récursive avec la carte mise à jour et le reste de la liste/du tableau.

J'ai écrit un article plus complet : [**Récursivité en JavaScript avec ES6, déstructuration et rest/spread**](https://codewithhugo.com/recursion-in-javascript-with-es6-destructuring-and-rest/spread/), qui entre dans plus de détails (exemples et techniques) sur la façon dont nous pouvons parcourir des listes (tableaux) en JavaScript ES6. Il explique des choses comme la notation `[firstCharacter, ...rest]`.

```js
function recurseCountCharacters(
  [firstCharacter, ...rest],
  characterToCountMap = {}
) {
  const currentCharacterCount = characterToCountMap[firstCharacter] || 0;
  const newCharacterToCountMap = {
    ...characterToCountMap,
    [firstCharacter]: currentCharacterCount + 1
  };
  
  if (rest.length === 0) {
    // cas de base/terminaison
    // -> plus de caractères dans la chaîne
    return newCharacterToCountMap;
  }
  // cas récursif
  return recurseCountCharacters(rest, newCharacterToCountMap);
}
function countCharacters(input) {
  return recurseCountCharacters(String(input).split(''));  
}
console.log(countCharacters(1000000));
// { "0":6, "1": 1 }
console.log(countCharacters('some sentence'));
// { "s":2,"o":1,"m":1,"e":4," ":1,"n":2,"t":1,"c":1}
```

C'est ainsi que vous passez les entretiens en utilisant la récursivité ?, en tournant en rond autour de ces problèmes jouets.

Les solutions récursives aux problèmes d'entretien finissent par paraître plus cool et plus propres que les solutions itératives. Elles sont le bonbon pour les yeux des recruteurs.

Pour toute question, vous pouvez me joindre sur Twitter [@hugo__df](https://twitter.com/hugo__df).

Recevez tous les articles de la semaine avant tout le monde dans votre boîte mail : [Newsletter Code with Hugo](https://buttondown.email/hugo).