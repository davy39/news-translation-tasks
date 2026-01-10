---
title: Comment générer un nombre aléatoire dans une certaine plage en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-06T16:21:25.000Z'
originalURL: https://freecodecamp.org/news/generate-random-number-within-a-range-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/9.-random-number.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment générer un nombre aléatoire dans une certaine plage en JavaScript
seo_desc: 'By Dillion Megida

  Let''s say you want to generate a random number between 10 and 15 – how do you do
  that in JavaScript? I''ll show you how with examples in this article.

  In JavaScript, there''s the random method of the Math object which returns random
  n...'
---

Par Dillion Megida

Disons que vous voulez générer un nombre aléatoire entre 10 et 15 – comment faites-vous cela en JavaScript ? Je vais vous montrer comment faire avec des exemples dans cet article.

En JavaScript, il y a la méthode `random` de l'objet `Math` qui retourne des nombres aléatoires. Mais cela a une limitation de plage. Alors voyons comment nous pouvons tirer parti de cette méthode pour résoudre différentes plages.

J'ai créé une version vidéo de cet article que vous pouvez [utiliser pour compléter votre apprentissage ici](https://www.youtube.com/watch?v=oUZVKzXVJaE).

## Comment utiliser `Math.random` en JavaScript

La méthode `random` retourne un nombre flottant aléatoire entre `0` et `1`. Voici un exemple de code :

```js
Math.random()
// 0.26636355538480383

Math.random()
// 0.6272624945940997

Math.random()
// 0.05992852707853347
```

D'après les résultats, vous pouvez voir trois nombres aléatoires entre 0 et 1. Maintenant, résolvons pour d'autres plages.

## Comment obtenir des nombres aléatoires dans une plage en JavaScript

Nous aurons une fonction que nous pouvons utiliser pour différentes plages :

```js
function getRandom(min, max) {
  // code ici
}
```

Cette fonction prend les arguments `min` (paramètre le plus bas de la plage) et `max` (paramètre le plus haut de la plage). Maintenant, utilisons cette plage et `Math.random` pour obtenir un nombre aléatoire :

```js
function getRandom(min, max) {
  const floatRandom = Math.random()

  const difference = max - min

  // aléatoire entre 0 et la différence
  const random = Math.round(difference * floatRandom)

  const randomWithinRange = random + min

  return randomWithinRange
}
```

Voici ce qui se passe dans la fonction :

* d'abord, nous obtenons un nombre flottant aléatoire en utilisant `Math.random()`
* ensuite, nous trouvons la différence entre la plage la plus haute et la plus basse
* ensuite, nous évaluons un nombre aléatoire entre 0 et la différence entre les plages

Pour obtenir ce nombre aléatoire, nous multiplions la différence par le nombre aléatoire que nous avons obtenu de `Math.random` et nous appliquons `Math.round` sur le résultat pour arrondir le nombre à l'entier le plus proche.

Donc, par exemple, si `Math.random` retourne **0.3** et que la différence entre les plages est **5**, en les multipliant ensemble, cela donne **1.5**. Ensuite, en utilisant `Math.round`, cela donne **2** qui est entre 0 et 5 (la différence).

Un autre exemple : si `Math.random` retourne **0.9** et que la différence entre les plages spécifiées est **8**, en les multipliant ensemble, cela donne **7.2**. Ensuite, en utilisant `Math.round`, cela donne **7** qui est entre 0 et 8 (la différence).

Maintenant que nous avons un nombre aléatoire entre 0 et la différence, nous pouvons ajouter ce nombre aléatoire à la plage minimale. En faisant cela, nous obtenons un résultat qui est dans la plage minimale et maximale.

Nous attribuons ce résultat à `randomWithinRange` et le retournons depuis la fonction. Maintenant, voyons la fonction en utilisation :

```js
console.log(getRandom(10, 15))
// 14

console.log(getRandom(10, 15))
// 11

console.log(getRandom(10, 15))
// 12

console.log(getRandom(10, 15))
// 15
```

Ici, nous utilisons un `min` de **10** et un `max` de **15**. Les quatre fois où nous appelons la fonction avec ces arguments, vous pouvez voir les résultats qui sont des nombres aléatoires entre la plage fournie.

Regardons un autre exemple de la fonction en utilisation :

```js
console.log(getRandom(180, 450))
// 215

console.log(getRandom(180, 450))
// 386

console.log(getRandom(180, 450))
// 333

console.log(getRandom(180, 450))
// 442
```

Ici, nous utilisons un `min` de **180** et un `max` de **450**. Encore une fois, vous pouvez voir comment les résultats des nombres aléatoires de notre fonction.

## Conclusion

Si vous devez jamais générer un nombre aléatoire dans une plage spécifique, j'espère que cet article vous a montré comment faire.

Dans cet article, j'ai expliqué la limitation de plage de `Math.random` qui retourne un nombre aléatoire entre 0 et 1. Et je vous ai également montré comment tirer parti de cette méthode mathématique pour créer une fonction réutilisable pour générer des nombres aléatoires dans n'importe quelle plage de votre choix.

Merci de partager cet article si vous le trouvez utile.