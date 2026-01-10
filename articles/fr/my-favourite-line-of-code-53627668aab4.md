---
title: Ma ligne de code préférée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T21:33:49.000Z'
originalURL: https://freecodecamp.org/news/my-favourite-line-of-code-53627668aab4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CbW_xpWGV31N6TZM4zZH2w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Ma ligne de code préférée
seo_desc: 'By Sam Williams

  Every developer has their favourite patterns, functions or bits of code. This is
  mine and I use it every day.

  What is it?

  This little function takes a promise and returns an array of the error and the result
  of the promise. It’s super...'
---

Par Sam Williams

Chaque développeur a ses motifs, fonctions ou morceaux de code préférés. Voici le mien et je l'utilise tous les jours.

### Qu'est-ce que c'est ?

Cette petite fonction prend une promesse et retourne un tableau contenant l'erreur et le résultat de la promesse. C'est super simple mais peut être utilisé pour des choses incroyables.

### Que peut-elle faire ?

#### Gestion propre des erreurs avec async / await

C'est la principale raison pour laquelle j'utilise cette méthode tous les jours. Au travail, nous essayons d'écrire tout le code en utilisant la syntaxe `async` / `await` pour une meilleure lisibilité et maintenabilité à l'avenir. Le problème est que l'attente d'une promesse ne vous indique pas si la promesse a réussi ou échoué.

```js
let unimportantPromiseTask = () => {
    Math.random() > 0.5 ? 
        Promise.reject('random fail') : 
        Promise.resolve('random pass');
};

let data = await unimportantPromiseTask();
```

Si cette promesse réussit, alors `data = 'random pass'`, mais si elle échoue, il y a un rejet de promesse non géré et data n'est jamais assigné. Cela peut ne pas être ce à quoi vous vous attendriez en lisant le code.

Passer la promesse à cette fonction `handle` retourne un résultat très explicite que tout le monde peut facilement comprendre en le lisant.

```js
let [err, res] = await handle(unimportantPromiseTask());
```

Vous pouvez ensuite faire ce que vous voulez avec l'erreur et le résultat. Voici un motif courant que nous utilisons souvent ensuite :

```js
if (err || (res && !res.data)) { 
    // gestion des erreurs
    return {err: 'il y a eu une erreur'}
}
// continuer avec la réponse réussie
```

La principale raison pour laquelle nous utilisons cela plutôt que d'envelopper la promesse attendue dans un bloc `try / catch` est que nous trouvons cela plus facile à lire.

#### Arrêter les rejets de promesse non gérés

Cette fonction peut être utilisée pour gérer les promesses (d'où le nom). Parce que la fonction enchaîne `.catch` à la promesse, si elle échoue, l'erreur est attrapée. Cela signifie que si vous appelez une promesse et que vous ne vous souciez pas de savoir si elle réussit ou échoue, passez-la simplement dans `handle` !

```js
unimportantPromiseTask(); // 50% de chance d'erreur
handle(unimportantPromiseTask()); // n'échoue jamais
```

Sans passer la promesse dans la fonction `handle`, il y a une chance qu'elle échoue. Cela devient de plus en plus important car les futures versions de Node vont terminer le processus lorsqu'un _rejet de promesse non géré_ est rencontré.

Les autres façons de gérer les rejets de promesse consistent à envelopper la fonction dans un try catch, ou simplement à enchaîner un `.catch` à la promesse. Bien que ces deux méthodes soient très valides, l'utilisation de `handle` lorsque nous le pouvons rend notre code plus cohérent.

Merci d'avoir lu ce rapide article sur ma ligne de code préférée. Si vous avez une ligne de code préférée, faites-le moi savoir dans les commentaires, ce qu'elle est et pourquoi !