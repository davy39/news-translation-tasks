---
title: Comment vérifier si une chaîne contient une sous-chaîne en JavaScript
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-10-07T18:00:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-string-contains-a-substring-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-tranmautritam-251225.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier si une chaîne contient une sous-chaîne en JavaScript
seo_desc: 'When you''re working with a JavaScript program, you might need to check
  whether a string contains a substring. A substring is a string inside another string.

  Specifically, you might need to check whether a word contains a specific character
  or a speci...'
---

Lorsque vous travaillez avec un programme JavaScript, vous pourriez avoir besoin de vérifier si une chaîne contient une sous-chaîne. Une sous-chaîne est une chaîne de caractères située à l'intérieur d'une autre chaîne.

Plus précisément, vous pourriez avoir besoin de vérifier si un mot contient un caractère spécifique ou un ensemble spécifique de caractères.

Heureusement, il existe quelques moyens rapides d'y parvenir avec JavaScript.

Dans cet article, vous apprendrez deux manières différentes de vérifier si une chaîne contient une sous-chaîne en utilisant des méthodes JavaScript.

Plus précisément, vous apprendrez :
- Comment utiliser la méthode JavaScript intégrée `includes()`.
- Comment utiliser la méthode JavaScript intégrée `indexOf()`.

Voici ce que nous allons couvrir plus en détail :

1. [Analyse de la syntaxe de la méthode `includes()` en JavaScript](#syntaxe-includes)
    1. [Comment vérifier si une chaîne contient une sous-chaîne spécifique en utilisant la méthode `includes()`](#exemple-includes)
2. [Analyse de la syntaxe de la méthode `indexOf()` en JavaScript](#syntaxe-index)
    1. [Comment vérifier si une chaîne contient une sous-chaîne spécifique en utilisant la méthode `indexOf()`](#exemple-index)
 3. [Comment effectuer une vérification insensible à la casse avec les méthodes `includes()` et `indexOf()`](#insensible)

## Qu'est-ce que la méthode `includes()` en JavaScript ? Analyse de la syntaxe de la méthode `includes()` <a name="syntaxe-includes"></a>

La méthode JavaScript `includes()` a été introduite avec l'ES6, et c'est le moyen le plus courant et le plus moderne de vérifier si une chaîne contient un caractère spécifique ou une série de caractères.

La syntaxe générale de la méthode `includes()` ressemble à ceci :

```
string.includes(substring, index);
```

Décomposons-la :

- `string` est le mot dans lequel vous voulez effectuer la recherche.
- `includes()` est la méthode que vous appelez sur le mot dans lequel vous voulez chercher, qui dans ce cas est `string`.
- La méthode `includes()` accepte deux arguments : l'un est obligatoire, l'autre est optionnel.
- Le premier argument accepté par la méthode `includes()` est `substring`, et il est *obligatoire*. `substring` est le caractère ou la série de caractères dont vous vérifiez l'existence au sein de `string`.
- Le second argument accepté par la méthode `includes()` est `index`, et il est *optionnel*. `index` fait référence à la position à partir de laquelle la recherche de `substring` commencera — la valeur par défaut est `0` car l'indexation dans les langages de programmation commence à `0`.

La valeur de retour est un booléen. Une valeur booléenne peut être soit `true` (vrai), soit `false` (faux) selon que la sous-chaîne est présente ou non dans la chaîne.

Une chose à garder à l'esprit est que la méthode `includes()` est **sensible à la casse**.

### Comment vérifier si une chaîne contient une sous-chaîne spécifique en JavaScript en utilisant la méthode `includes()` <a name="exemple-includes"></a>

Voyons un exemple du fonctionnement de la méthode `includes()`.

Tout d'abord, j'ai créé une variable qui contient la chaîne `"Hello, World"` — c'est la chaîne dans laquelle je veux chercher :

```js
let string= "Hello, World";
```

Ensuite, j'ai créé une variable avec la sous-chaîne `"Hello"` — c'est la sous-chaîne que je veux rechercher dans la chaîne d'origine :

```js
let string= "Hello, World";
let substring = "Hello";
```

Ensuite, je vais vérifier si `substring` est présent dans `string` en utilisant la méthode `includes()` et afficher le résultat dans la console :

```js
let string= "Hello, World";
let substring = "Hello";

console.log(string.includes(substring));

// sortie
// true
```

La valeur de retour est `true`, ce qui signifie que `Hello` est présent dans la variable `string`.

Comme mentionné dans la section précédente, la méthode `includes()` est sensible à la casse.

Voyez ce qui se passe quand je change la valeur de `substring` de `"Hello"` à `"hello"` :

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.includes(substring));

// sortie
// false
```

La valeur de retour, dans ce cas, est `false`, car il n'y a pas de sous-chaîne `hello` avec un `h` minuscule. Gardez donc cela à l'esprit lorsque vous travaillez avec la méthode `includes()` : elle différencie les majuscules des minuscules.

Maintenant, voyons comment utiliser la méthode `includes()` avec le second argument, `index`.

Pour rappel, le second argument spécifie la position à partir de laquelle vous souhaitez commencer la recherche de la sous-chaîne.

Reprenons la même variable `string` des exemples précédents :

```js
let string= "Hello, World";
```

Je vais changer la valeur de la variable `substring` en `"H"` :

```js
let string= "Hello, World";
let substring = "H";
```

Et je vais spécifier que la recherche de la sous-chaîne commence à la position `0` :

```js
let string= "Hello, World";
let substring = "H";

console.log(string.includes(substring,0));

// sortie
// true
```

La valeur de retour est `true` car la sous-chaîne `H` se trouve à la position d'index `0` dans la chaîne `"Hello, World"`.

N'oubliez pas que la première lettre d'une chaîne a une position de `0`, la deuxième une position de `1`, et ainsi de suite.

## Qu'est-ce que la méthode `indexOf()` en JavaScript ? Analyse de la syntaxe de la méthode `indexOf()` <a name="syntaxe-index"></a>

Tout comme la méthode `includes()`, la méthode JavaScript `indexOf()` vérifie si une chaîne inclut une sous-chaîne.

La syntaxe générale de la méthode `indexOf()` ressemble à ceci :

```
string.indexOf(substring, index);
```

Décomposons-la :

- `string` est le mot dans lequel vous voulez effectuer la recherche.
- `indexOf()` est la méthode que vous appelez sur le mot dans lequel vous voulez chercher, dans ce cas, `string`.
- La méthode `indexOf()` prend deux arguments : l'un est obligatoire, l'autre est optionnel.
- Le premier argument de la méthode `indexOf()` est `substring`, et il est *obligatoire*. `substring` est le caractère ou la série de caractères que vous recherchez.
- Le second argument de la méthode `indexOf()` est `index`, et il est *optionnel*. `index` fait référence à la position à partir de laquelle la recherche de `substring` commencera. La valeur par défaut est `0` car l'indexation dans les langages de programmation commence à `0`.

La différence entre les deux méthodes réside dans leur valeur de retour.

La méthode `includes()` renvoie une valeur booléenne (une valeur qui est soit `true`, soit `false`), tandis que la méthode `indexOf()` renvoie un nombre.

Ce nombre sera la position de l'index de départ où la sous-chaîne que vous recherchez est trouvée dans la chaîne. La valeur de retour sera `-1` si la sous-chaîne n'est pas trouvée dans la chaîne.

Et tout comme la méthode `includes()`, la méthode `indexOf()` est **sensible à la casse**.

### Comment vérifier si une chaîne contient une sous-chaîne spécifique en JavaScript en utilisant la méthode `indexOf()` <a name="exemple-index"></a>

Utilisons le même exemple que précédemment pour voir comment fonctionne la méthode `indexOf()`.

```js
let string= "Hello, World";
let substring = "H";
```

Voici la variable `string` avec la chaîne d'origine, et la variable `substring` avec la sous-chaîne que vous recherchez.

```js
let string= "Hello, World";
let substring = "H";

console.log(string.indexOf(substring));

// sortie
// 0
```

La sortie est `0`, qui est la position de départ de la sous-chaîne que vous recherchez.

Dans ce cas, la valeur que vous recherchiez était un seul caractère.

Changeons la valeur de `substring` de `"H"` à `"Hello"` :

```js
let string= "Hello, World";
let substring = "Hello";

console.log(string.indexOf(substring));

// sortie
// 0
```

La valeur de retour est à nouveau `0` puisque `indexOf()` renvoie la position de *départ* de la sous-chaîne que vous recherchez. Comme le premier caractère de la sous-chaîne est situé à la position `0`, `indexOf()` renvoie `0`.

Maintenant, changeons la valeur de `substring` de `"Hello"` à `"hello"` avec un `h` minuscule :

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.indexOf(substring));

// sortie
// -1
```

La valeur de retour est `-1`. Comme mentionné précédemment, `indexOf()` est sensible à la casse, il ne peut donc pas trouver la sous-chaîne `hello` avec un `h` minuscule. Et lorsque `indexOf()` ne trouve pas la sous-chaîne donnée, il renvoie `-1`.

Enfin, vous pouvez spécifier la valeur d'index à partir de laquelle vous souhaitez commencer votre recherche en passant le second argument accepté par `indexOf()`.

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.indexOf(substring,1));

// sortie
// -1
```

Supposons que vous vouliez commencer votre recherche à partir de la position `1`. La valeur de retour est `-1` puisque la position de départ de la sous-chaîne que vous recherchez est `0`. Une correspondance exacte n'est pas trouvée à partir de la position `1`, donc `indexOf()` renvoie `-1`.

## Comment effectuer une vérification insensible à la casse avec les méthodes `includes()` et `indexOf()` <a name="insensible"></a>

Jusqu'à présent, vous avez vu que les méthodes `includes()` et `indexOf()` sont sensibles à la casse.

Mais que se passe-t-il lorsque vous voulez effectuer une vérification insensible à la casse ?

Pour effectuer une vérification insensible à la casse et voir si une sous-chaîne est présente dans une chaîne, vous devrez convertir à la fois la chaîne d'origine et la sous-chaîne en minuscules à l'aide de la méthode JavaScript `toLowerCase()` avant d'appeler l'une des deux méthodes.

Voici comment vous feriez cela en utilisant la méthode `includes()` :

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.toLowerCase().includes(substring.toLowerCase()));

// sortie
// true
```

Par défaut, la valeur de retour aurait été `false` car la chaîne d'origine contient un `H` majuscule, alors que la sous-chaîne contient un `h` minuscule. Après avoir converti les deux chaînes en minuscules, vous n'avez plus à vous soucier de la capitalisation de la chaîne d'origine et de la sous-chaîne que vous recherchez.

Et voici comment vous feriez la même chose en utilisant la méthode `indexOf()` :

```js
let string= "Hello, World";
let substring = "hello";

console.log(string.toLowerCase().indexOf(substring.toLowerCase()));

// sortie
// 0
```

Par défaut, la valeur de retour aurait été `-1` car la chaîne d'origine et la sous-chaîne que vous recherchez ont des casses différentes.

Après avoir utilisé la méthode `toLowerCase()`, la méthode `indexOf()` renvoie la position de départ de la sous-chaîne.

## Conclusion

Et voilà ! Vous savez maintenant comment vérifier si une chaîne contient une sous-chaîne en JavaScript.

Pour en savoir plus sur JavaScript, rendez-vous sur la [Certification JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien conçu et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances.

Merci de m'avoir lu !