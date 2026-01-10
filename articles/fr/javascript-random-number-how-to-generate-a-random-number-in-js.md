---
title: Nombre aléatoire en JavaScript – Comment générer un nombre aléatoire en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-03T19:29:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-random-number-how-to-generate-a-random-number-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-josh-sorenson-1714208.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Nombre aléatoire en JavaScript – Comment générer un nombre aléatoire en
  JS
seo_desc: 'When working with a JavaScript program, there may be times when you will
  need to generate a random number.

  For example, you may want to generate a random number when developing a JavaScript
  game, such as a number guessing game.

  JavaScript has many bu...'
---

Lorsque vous travaillez avec un programme JavaScript, il peut arriver que vous ayez besoin de générer un nombre aléatoire.

Par exemple, vous pouvez vouloir générer un nombre aléatoire lors du développement d'un jeu JavaScript, comme un jeu de devinettes de nombres.

JavaScript dispose de nombreuses méthodes intégrées pour travailler avec des nombres et effectuer des calculs mathématiques. L'une de ces méthodes est la méthode `Math.random()`.

Dans cet article, vous apprendrez à utiliser la méthode `Math.random()` pour récupérer des nombres aléatoires.

Voici ce que nous allons couvrir :

1. [Introduction à l'objet `Math`](#introduction-a-l-objet-math)
2. [Analyse de la syntaxe de `Math.random()`](#syntaxe)
   1. [Comment générer un nombre décimal aléatoire avec un `max` spécifié](#max)
   2. [Comment générer un nombre décimal aléatoire avec une plage `min` et `max` spécifiée](#plage)
   3. [Comment générer un nombre entier aléatoire avec un `max` spécifié](#entier-max)
   4. [Comment générer un nombre entier aléatoire avec un `max` inclus](#max-inclus)
   5. [Comment générer un nombre entier aléatoire avec une plage `min` et `max` inclusive](#plage-inclusive)

## Comment utiliser Math en JavaScript - Introduction à l'objet `Math` <a name="introduction-a-l-objet-math"></a>

JavaScript dispose de l'objet statique intégré `Math`, qui vous permet d'effectuer des calculs et des opérations mathématiques.

L'objet `Math` dispose de quelques méthodes intégrées qui rendent l'exécution de ces opérations beaucoup plus précise.

La syntaxe générale des méthodes de l'objet `Math` est la suivante :

```
Math.methodName(number);
```

Certaines des méthodes les plus populaires sont :

- `Math.round()`
- `Math.ceil()`
- `Math.floor()`
- `Math.random()`

Passons en revue quelques exemples de mise en œuvre de ces méthodes.

Si vous souhaitez arrondir un nombre à l'entier le plus proche, utilisez la méthode `Math.round()` :

```js
console.log(Math.round(6.2)); // 6

console.log(Math.round(6.3)); // 6

console.log(Math.round(6.5)); // 7

console.log(Math.round(6.8)); // 7
```

Si vous souhaitez arrondir un nombre **vers le haut** à l'entier le plus proche, utilisez la méthode `Math.ceil()` :

```js
console.log(Math.ceil(6.2));  // 7

console.log(Math.ceil(6.3));  // 7

console.log(Math.ceil(6.5));  // 7

console.log(Math.ceil(6.8));  // 7
```

Si vous souhaitez arrondir un nombre **vers le bas** à l'entier le plus proche, utilisez la méthode `Math.floor()` :

```js
console.log(Math.floor(6.2));  // 6

console.log(Math.floor(6.3));  // 6

console.log(Math.floor(6.5));  // 6

console.log(Math.floor(6.8)); // 6
```

Si vous souhaitez générer un nombre **aléatoire**, utilisez la méthode `Math.random()` :

```js
console.log(Math.random());

// Vous n'obtiendrez pas la même sortie

// première exécution du programme :
// 0.4928793139100267 

// deuxième exécution du programme :
// 0.5420802533292215

// troisième exécution du programme :
// 0.5479835477696466
```

## Qu'est-ce que la méthode `Math.random()` en JavaScript ? - Analyse de la syntaxe <a name="syntaxe"></a>

La syntaxe de la méthode `Math.random()` est la suivante :

```js
Math.random();
```

La méthode ne prend aucun paramètre.

Par défaut, la méthode retourne une valeur qui est un nombre **décimal aléatoire (ou à virgule flottante)** entre `0` et `1`. 

Une chose à noter est que `0` est inclus, tandis que `1` ne l'est *pas*. 

Ainsi, elle retournera une valeur supérieure ou égale à `0` et toujours inférieure à et jamais égale à `1`.

### Comment générer un nombre décimal aléatoire avec une limite `max` spécifiée en utilisant `Math.random()` en JavaScript <a name="max"></a>

Comme vous l'avez vu jusqu'à présent, par défaut, les nombres générés par `Math.random()` sont petits. 

Que faire si vous souhaitez générer un nombre décimal aléatoire qui commence à partir de, et inclut, `0` et est également *supérieur* à `1` ? Pour cela, vous spécifiez un nombre **max**.

Plus précisément, vous devrez multiplier ce nombre `max` par le nombre aléatoire de `Math.random()`.

Par exemple, si vous souhaitez générer un nombre aléatoire entre `0` et `10`, vous feriez ce qui suit :

```js
console.log(Math.random() * 10);

// Vous n'obtiendrez pas la même sortie
//9.495628210218175
```

Dans l'exemple ci-dessus, j'ai multiplié le nombre `max` (`10`), qui servira de limite, par le nombre résultant de `Math.random()`.

Gardez à l'esprit que dans ce cas, le nombre aléatoire sera entre `0` et `10` - cela signifie supérieur ou égal à `0` et inférieur à et jamais égal à `10`.

### Comment générer un nombre décimal aléatoire avec une plage `min` et `max` spécifiée en utilisant `Math.random()` en JavaScript <a name="plage"></a>

Que faire si vous souhaitez générer un nombre décimal aléatoire entre une plage de nombres que vous spécifiez ? 

Vous avez vu dans la section précédente comment spécifier un `max`, mais que faire si vous *ne voulez pas* que la plage commence à `0` (qui est la plage de départ par défaut) ? Pour cela, vous pouvez également spécifier un `min`.

La syntaxe générale pour générer un nombre décimal entre deux valeurs (ou plage) ressemble à ceci :

```
Math.random() * (max - min) + min;
```

Prenons l'exemple suivant :

```js
// spécifiez un minimum - où la plage commencera
let min = 20.4;

// spécifiez un maximum - où la plage se terminera
let max = 29.8;
```

J'ai créé deux variables, `min` et `max` - où `min` sera le plus petit nombre et `max` le plus grand nombre dans la plage.

Ensuite, je génère un nombre aléatoire dans cette plage en utilisant la syntaxe que vous avez vue précédemment :

```js
let min = 20.4;
let max = 29.8;

let randomNum = Math.random() * (max - min) + min;

console.log(randomNum);

// Vous n'obtiendrez pas la même sortie
// 23.309418058783486
```

Une chose à noter ici est que `min` est inclus, donc le nombre aléatoire sera supérieur ou égal à `20.4`, tandis que `max` ne l'est *pas*, donc le résultat sera toujours un nombre inférieur à et jamais égal à `29.8`.

### Comment générer un nombre entier aléatoire avec une limite `max` spécifiée en utilisant `Math.random()` en JavaScript <a name="entier-max"></a>

Jusqu'à présent, vous avez vu comment générer des nombres *décimaux* aléatoires. 

Cela dit, il existe un moyen de générer des nombres *entiers* aléatoires en utilisant `Math.random()`. 

Vous devrez passer le résultat du calcul `Math.random()` à la méthode `Math.floor()` que vous avez vue précédemment.

La syntaxe générale pour cela est la suivante :

```
Math.floor(Math.random());
```

La méthode `Math.floor()` arrondira le nombre décimal aléatoire à l'entier (ou nombre entier) le plus proche.

En plus de cela, vous pouvez spécifier un nombre `max`. 

Ainsi, par exemple, si vous vouliez générer un nombre aléatoire entre `0` et `10`, vous feriez ce qui suit :

```js
console.log(Math.floor(Math.random() * 10));

// Vous n'obtiendrez pas la même sortie
// 0
```

Dans cet exemple, j'ai multiplié le nombre `max` (qui est `10` dans ce cas) par le résultat de `Math.random()` et j'ai passé le résultat de ce calcul à `Math.floor()`.

Une chose à noter ici est que le nombre aléatoire sera entre `0` inclus et `10` exclus. Ainsi, les nombres peuvent être supérieurs ou égaux à `0` et inférieurs à et jamais égaux à `10`.

### Comment générer un nombre entier aléatoire avec une limite `max` inclusive spécifiée en utilisant `Math.random()` en JavaScript <a name="max-inclus"></a>

Dans l'exemple de la section précédente, j'ai généré un nombre aléatoire entre les nombres `0` (inclus) et `10` (exclus).

Jusqu'à présent, vous avez vu que vous ne pouvez pas générer un nombre aléatoire égal au `max` spécifié.

Que faire si vous souhaitez générer un nombre aléatoire qui inclut le max spécifié ?

La solution à cela est d'ajouter `1` pendant le calcul.

Reprenons donc le code de la section précédente :

```js
console.log(Math.floor(Math.random() * 10));
```

Vous réécrirez maintenant le code comme suit :

```js
console.log(Math.floor(Math.random() * 10) + 1);

// Vous n'obtiendrez pas la même sortie
// 10
```

Une chose à noter ici est que ce code générera un nombre entier aléatoire entre `1` (et non `0`) et `10` - incluant `10`.

### Comment générer un nombre entier aléatoire avec une plage `min` et `max` inclusive spécifiée en utilisant `Math.random()` en JavaScript <a name="plage-inclusive"></a>

Jusqu'à présent, vous avez vu comment générer un nombre entier aléatoire avec un `max` inclus que vous spécifiez.

Comme vous l'avez vu dans l'exemple ci-dessus, le code pour rendre le nombre `max` inclus utilisait le nombre `1` comme nombre de départ et non `0`.

Cela dit, il existe un moyen pour vous de spécifier une plage inclusive de nombres. Pour cela, vous devez spécifier un `min` et un `max`.

Dans une section précédente, vous avez vu comment générer un nombre aléatoire entre une plage spécifiée, et le code est similaire. Le seul changement est que vous passez le résultat à la méthode `Math.floor()` pour arrondir le nombre décimal à l'entier le plus proche.

Ainsi, le code général est le suivant :

```
Math.floor(Math.random() * (max - min) + min);
```

Pour rendre cette plage *inclusive*, vous feriez ce qui suit :

```
console.log(Math.floor(Math.random() * (max - min + 1)) + min);
```

Ainsi, pour générer un nombre aléatoire entre les nombres `0` (inclus) *et* `10` (inclus), vous écririez ce qui suit :

```js
let min = 0;
let max = 10;

console.log(Math.floor(Math.random() * (max - min + 1)) + min);

// Vous n'obtiendrez pas la même sortie
// 0
```

## Conclusion

Et voilà ! Vous savez maintenant comment fonctionne la méthode `Math.random()` et quelques façons de l'utiliser.

Pour en savoir plus sur JavaScript, rendez-vous sur la [Certification Algorithmes et Structures de Données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien pensé et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances.

Merci d'avoir lu !