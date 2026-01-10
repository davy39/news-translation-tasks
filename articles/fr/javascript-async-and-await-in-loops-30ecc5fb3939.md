---
title: JavaScript async et await dans les boucles
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-05-21T23:04:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-async-and-await-in-loops-30ecc5fb3939
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p2upvpYKRT0-qtTP61LOYg.gif
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript async et await dans les boucles
seo_desc: 'Basic async and await is simple. Things get a bit more complicated when
  you try to use await in loops.

  In this article, I want to share some gotchas to watch out for if you intend to
  use await in loops.

  Before you begin

  I''m going to assume you know h...'
---

Les bases de `async` et `await` sont simples. Les choses deviennent un peu plus compliquées lorsque vous essayez d'utiliser `await` dans des boucles.

Dans cet article, je souhaite partager quelques pièges à éviter si vous prévoyez d'utiliser `await` dans des boucles.

### **Avant de commencer**

Je vais supposer que vous savez comment utiliser `async` et `await`. Si ce n'est pas le cas, lisez l'[article précédent](https://zellwk.com/blog/async-await) pour vous familiariser avant de continuer.

### **Préparer un exemple**

Pour cet article, disons que vous voulez obtenir le nombre de fruits dans un panier de fruits.

```
const fruitBasket = {
  apple: 27,
  grape: 0,
  pear: 14
};
```

Vous voulez obtenir le nombre de chaque fruit dans le panier de fruits. Pour obtenir le nombre d'un fruit, vous pouvez utiliser une fonction `getNumFruit`.

```
const getNumFruit = fruit => {
  return fruitBasket[fruit];
};

const numApples = getNumFruit("apple");
console.log(numApples); // 27
```

Maintenant, disons que `fruitBasket` se trouve sur un serveur distant. L'accès prend une seconde. Nous pouvons simuler ce délai d'une seconde avec un timeout. (Veuillez vous référer à l'[article précédent](https://zellwk.com/blog/async-await) si vous avez des problèmes à comprendre le code de timeout).

```
const sleep = ms => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const getNumFruit = fruit => {
  return sleep(1000).then(v => fruitBasket[fruit]);
};

getNumFruit("apple").then(num => console.log(num)); // 27
```

Enfin, disons que vous voulez utiliser `await` et `getNumFruit` pour obtenir le nombre de chaque fruit dans une fonction asynchrone.

```
const control = async _ => {
  console.log("Start");
  
  const numApples = await getNumFruit("apple");
  console.log(numApples);
  
  const numGrapes = await getNumFruit("grape");
  console.log(numGrapes);
  
  const numPears = await getNumFruit("pear");
  console.log(numPears);
  
  console.log("End");
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/n5Qv0F00AiCZqsRsu7NPh3S3HFp-ZWXYTwuH)
_La console affiche 'Start'. Une seconde plus tard, elle affiche 27. Une autre seconde plus tard, elle affiche 0. Une seconde de plus, elle affiche 14, et 'End'_

Avec cela, nous pouvons commencer à examiner `await` dans les boucles.

### **Await dans une boucle for**

Disons que nous avons un tableau de fruits que nous voulons obtenir du panier de fruits.

```
const fruitsToGet = ["apple", "grape", "pear"];
```

Nous allons parcourir ce tableau.

```
const forLoop = async _ => {
  console.log("Start");
  
  for (let index = 0; index < fruitsToGet.length; index++) {
    // Obtenir le nombre de chaque fruit
  }
  
  console.log("End");
};
```

Dans la boucle for, nous allons utiliser `getNumFruit` pour obtenir le nombre de chaque fruit. Nous allons également afficher le nombre dans la console.

Puisque `getNumFruit` retourne une promesse, nous pouvons `await` la valeur résolue avant de la logger.

```
const forLoop = async _ => {
  console.log("Start");
  
  for (let index = 0; index < fruitsToGet.length; index++) {
    const fruit = fruitsToGet[index];
    const numFruit = await getNumFruit(fruit);
    console.log(numFruit);
  }
  
  console.log("End");
};
```

Lorsque vous utilisez `await`, vous vous attendez à ce que JavaScript pause l'exécution jusqu'à ce que la promesse attendue soit résolue. Cela signifie que les `await` dans une boucle for doivent être exécutés en série.

Le résultat est celui auquel vous vous attendez.

```
"Start";
"Apple: 27";
"Grape: 0";
"Pear: 14";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/sU0OzGuNuH5BwMoYmNcmNLfQzcexW0m7e08K)
_La console affiche 'Start'. Une seconde plus tard, elle affiche 27. Une autre seconde plus tard, elle affiche 0. Une seconde de plus, elle affiche 14, et 'End'_

Ce comportement fonctionne avec la plupart des boucles (comme les boucles `while` et `for-of`)...

Mais cela ne fonctionnera pas avec les boucles qui nécessitent un callback. Des exemples de telles boucles qui nécessitent un fallback incluent `forEach`, `map`, `filter`, et `reduce`. Nous allons voir comment `await` affecte `forEach`, `map`, et `filter` dans les prochaines sections.

### **Await dans une boucle forEach**

Nous allons faire la même chose que dans l'exemple de la boucle for. Tout d'abord, parcourons le tableau de fruits.

```
const forEachLoop = _ => {
  console.log("Start");
  
  fruitsToGet.forEach(fruit => {
    // Envoyer une promesse pour chaque fruit
  });
  
  console.log("End");
};
```

Ensuite, nous allons essayer d'obtenir le nombre de fruits avec `getNumFruit`. (Remarquez le mot-clé `async` dans la fonction de callback. Nous avons besoin de ce mot-clé `async` parce que `await` est dans la fonction de callback).

```
const forEachLoop = _ => {
  console.log("Start");
  
  fruitsToGet.forEach(async fruit => {
    const numFruit = await getNumFruit(fruit);
    console.log(numFruit);
  });
  
  console.log("End");
};
```

Vous pourriez vous attendre à ce que la console ressemble à ceci :

```
"Start";
"27";
"0";
"14";
"End";
```

Mais le résultat réel est différent. JavaScript procède à l'appel de `console.log('End')` avant que les promesses dans la boucle forEach ne soient résolues.

La console log dans cet ordre :

```
'Start'
'End'
'27'
'0'
'14'
```

![Image](https://cdn-media-1.freecodecamp.org/images/DwUgo9TAK8PXNLIAv3-27UZMSrEkfNx778hS)
_La console log 'Start' et 'End' immédiatement. Une seconde plus tard, elle log 27, 0, et 14._

JavaScript fait cela parce que `forEach` n'est pas conscient des promesses. Il ne peut pas supporter `async` et `await`. Vous __ne pouvez pas__ utiliser `await` dans `forEach`.

### **Await avec map**

Si vous utilisez `await` dans un `map`, `map` retournera toujours un tableau de promesses. Cela est dû au fait que les fonctions asynchrones retournent toujours des promesses.

```
const mapLoop = async _ => {
  console.log("Start");
  
  const numFruits = await fruitsToGet.map(async fruit => {
    const numFruit = await getNumFruit(fruit);
    return numFruit;
  });
  
  console.log(numFruits);

  console.log("End");
};

"Start";
"[Promise, Promise, Promise]";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/JD3o7BUxILoFP-hVwv5920JtHJPB8l6IrMNs)
_La console log 'Start', '[Promise, Promise, Promise]', et 'End' immédiatement_

Puisque `map` retourne toujours des promesses (si vous utilisez `await`), vous devez attendre que le tableau de promesses soit résolu. Vous pouvez faire cela avec `await Promise.all(arrayOfPromises)`.

```
const mapLoop = async _ => {
  console.log("Start");
  
  const promises = fruitsToGet.map(async fruit => {
    const numFruit = await getNumFruit(fruit);
    return numFruit;
  });
  
  const numFruits = await Promise.all(promises);
  console.log(numFruits);
  
  console.log("End");
};
```

Voici ce que vous obtenez :

```
"Start";
"[27, 0, 14]";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/Clz579WsPZ0Tv4iiA5rN1960VP0xx4x66dAz)
_La console log 'Start'. Une seconde plus tard, elle log '[27, 0, 14]' et 'End'_

Vous pouvez manipuler la valeur que vous retournez dans vos promesses si vous le souhaitez. Les valeurs résolues seront les valeurs que vous retournez.

```
const mapLoop = async _ => {
  // …
  const promises = fruitsToGet.map(async fruit => {
    const numFruit = await getNumFruit(fruit);
    // Ajoute des fruits avant de retourner
    return numFruit + 100;
  });
  // …
};

"Start";
"[127, 100, 114]";
"End";
```

### **Await avec filter**

Lorsque vous utilisez `filter`, vous voulez filtrer un tableau avec un résultat spécifique. Disons que vous voulez créer un tableau avec plus de 20 fruits.

Si vous utilisez `filter` normalement (sans await), vous l'utiliserez comme ceci :

```
// Filtrer s'il n'y a pas d'await
const filterLoop = _ => {
  console.log('Start')
  
  const moreThan20 = await fruitsToGet.filter(fruit => {
    const numFruit = fruitBasket[fruit]
    return numFruit > 20
  })
  
  console.log(moreThan20)
  console.log('End')
}
```

Vous vous attendriez à ce que `moreThan20` ne contienne que des pommes parce qu'il y a 27 pommes, mais il y a 0 raisins et 14 poires.

```
"Start"["apple"];
("End");
```

`await` dans `filter` ne fonctionne pas de la même manière. En fait, cela ne fonctionne pas du tout. Vous obtenez le tableau non filtré en retour...

```
const filterLoop = _ => {
  console.log('Start')
  
  const moreThan20 = await fruitsToGet.filter(async fruit => {
    const numFruit = getNumFruit(fruit)
    return numFruit > 20
  })
  
  console.log(moreThan20)
  console.log('End')
}

"Start"[("apple", "grape", "pear")];
("End");
```

![Image](https://cdn-media-1.freecodecamp.org/images/xI8y6n2kvda8pz9i7f5ffVu92gs7ISj7My9M)
_La console log 'Start', '[apple, grape, pear]', et 'End' immédiatement_

Voici pourquoi cela se produit.

Lorsque vous utilisez `await` dans un callback `filter`, le callback retourne toujours une promesse. Puisque les promesses sont toujours truthy, chaque élément du tableau passe le filtre. Écrire `await` dans un `filter` revient à écrire ce code :

```
// Tout passe le filtre...
const filtered = array.filter(true);
```

Il y a trois étapes pour utiliser `await` et `filter` correctement :

1. Utilisez `map` pour retourner un tableau de promesses

2. `await` le tableau de promesses

3. `filter` les valeurs résolues

```
const filterLoop = async _ => {
  console.log("Start");
  
  const promises = await fruitsToGet.map(fruit => getNumFruit(fruit));
  const numFruits = await Promise.all(promises);
  
  const moreThan20 = fruitsToGet.filter((fruit, index) => {
    const numFruit = numFruits[index];
    return numFruit > 20;
  });
  
  console.log(moreThan20);
  console.log("End");
};

Start["apple"];
End;
```

![Image](https://cdn-media-1.freecodecamp.org/images/KbvkmmX4K77pSq29OVj8jhK0KNdyCYQsH1Sn)
_La console affiche 'Start'. Une seconde plus tard, la console log '[apple]' et 'End'_

### **Await avec reduce**

Pour ce cas, disons que vous voulez connaître le nombre total de fruits dans le panier de fruits. Normalement, vous pouvez utiliser `reduce` pour parcourir un tableau et faire la somme des nombres.

```
// Réduire s'il n'y a pas d'await
const reduceLoop = _ => {
  console.log("Start");
  
  const sum = fruitsToGet.reduce((sum, fruit) => {
    const numFruit = fruitBasket[fruit];
    return sum + numFruit;
  }, 0);
  
  console.log(sum);
  console.log("End");
};
```

Vous obtiendrez un total de 41 fruits. (27 + 0 + 14 = 41).

```
"Start";
"41";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/1cHrIKZU2x4bt0Cl6NmnrNA9eYed0-3n4SIq)
_La console log 'Start', '41', et 'End' immédiatement_

Lorsque vous utilisez `await` avec reduce, les résultats deviennent extrêmement désordonnés.

```
// Réduire si nous attendons getNumFruit
const reduceLoop = async _ => {
  console.log("Start");
  
  const sum = await fruitsToGet.reduce(async (sum, fruit) => {
    const numFruit = await getNumFruit(fruit);
    return sum + numFruit;
  }, 0);
  
  console.log(sum);
  console.log("End");
};

"Start";
"[object Promise]14";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/vziO1ieaUzFZNE1p3FlaOBJLEQtAL21CYDKw)
_La console log 'Start'. Une seconde plus tard, elle log '[object Promise]14' et 'End'_

Quoi ?! `[object Promise]14` ?!

Disséquer cela est intéressant.

* Dans la première itération, `sum` est `0`. `numFruit` est 27 (la valeur résolue de `getNumFruit('apple')`). `0 + 27` est 27.
* Dans la deuxième itération, `sum` est une promesse. (Pourquoi ? Parce que les fonctions asynchrones retournent toujours des promesses !) `numFruit` est 0. Une promesse ne peut pas être ajoutée à un objet normalement, donc JavaScript la convertit en chaîne `[object Promise]`. `[object Promise] + 0` est `[object Promise]0`
* Dans la troisième itération, `sum` est également une promesse. `numFruit` est `14`. `[object Promise] + 14` est `[object Promise]14`.

Mystère résolu !

Cela signifie que vous pouvez utiliser `await` dans un callback `reduce`, mais vous devez vous souvenir d'attendre l'accumulateur en premier !

```
const reduceLoop = async _ => {
  console.log("Start");
  
  const sum = await fruitsToGet.reduce(async (promisedSum, fruit) => {
    const sum = await promisedSum;
    const numFruit = await getNumFruit(fruit);
    return sum + numFruit;
  }, 0);
  
  console.log(sum);
  console.log("End");
};

"Start";
"41";
"End";
```

![Image](https://cdn-media-1.freecodecamp.org/images/a3ZEbODMdVmob-31Qh0qfFugbLJoNZudoPwM)
_La console log 'Start'. Trois secondes plus tard, elle log '41' et 'End'_

Mais... comme vous pouvez le voir dans le gif, cela prend assez longtemps pour `await` tout. Cela se produit parce que `reduceLoop` doit attendre que `promisedSum` soit complété pour chaque itération.

Il y a un moyen d'accélérer la boucle reduce. (J'ai découvert cela grâce à [Tim Oxley](https://twitter.com/timkevinoxley). Si vous `await getNumFruits(`) en premier avant `await promisedSum`, le `reduceLoop` ne prend qu'une seconde pour se terminer :

```
const reduceLoop = async _ => {
  console.log("Start");
  
  const sum = await fruitsToGet.reduce(async (promisedSum, fruit) => {
    // Le travail intensif vient en premier.
    // Cela déclenche toutes les trois promesses getNumFruit avant d'attendre la prochaine itération de la boucle.
    const numFruit = await getNumFruit(fruit);
    const sum = await promisedSum;
    return sum + numFruit;
  }, 0);
  
  console.log(sum);
  console.log("End");
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/Vm9olChpCbbEgBmub6OuOS2r0QD5SwwW9y9i)
_La console log 'Start'. Une seconde plus tard, elle log '41' et 'End'_

Cela fonctionne parce que `reduce` peut déclencher toutes les trois promesses `getNumFruit` avant d'attendre la prochaine itération de la boucle. Cependant, cette méthode est légèrement déroutante puisque vous devez être prudent avec l'ordre dans lequel vous `await` les choses.

La manière la plus simple (et la plus efficace) d'utiliser `await` dans reduce est de :

1. Utiliser `map` pour retourner un tableau de promesses

2. `await` le tableau de promesses

3. `reduce` les valeurs résolues

```
const reduceLoop = async _ => {
  console.log("Start");
  
  const promises = fruitsToGet.map(getNumFruit);
  const numFruits = await Promise.all(promises);
  const sum = numFruits.reduce((sum, fruit) => sum + fruit);
  
  console.log(sum);
  console.log("End");
};
```

Cette version est simple à lire et à comprendre, et prend une seconde pour calculer le nombre total de fruits.

![Image](https://cdn-media-1.freecodecamp.org/images/rAN2FodB3Ff8FmQvMLy4R3mii1Kt41jRszkE)
_La console log 'Start'. Une seconde plus tard, elle log '41' et 'End'_

### **Points clés à retenir**

1. Si vous voulez exécuter des appels `await` en série, utilisez une boucle `for` (ou toute boucle sans callback).

2. N'utilisez jamais `await` avec `forEach`. Utilisez une boucle `for` (ou toute boucle sans callback) à la place.

3. N'utilisez pas `await` à l'intérieur de `filter` et `reduce`. Attendez toujours un tableau de promesses avec `map`, puis filtrez ou réduisez en conséquence.

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/async-await-in-loops/)_._   
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.