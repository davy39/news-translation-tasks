---
title: String to Number en JavaScript – Convertir une chaîne en nombre en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-30T16:38:26.000Z'
originalURL: https://freecodecamp.org/news/string-to-number-in-javascript-convert-a-string-to-an-int-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-pixabay-459653.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: String to Number en JavaScript – Convertir une chaîne en nombre en JS
seo_desc: "When you're programming, you'll often need to switch between data types.\
  \ For example, you may need to convert a string into a number. \nThe ability to\
  \ convert one data type to another gives you great flexibility when working with\
  \ information.\nJavaScri..."
---

Lorsque vous programmez, vous devrez souvent basculer entre différents types de données. Par exemple, vous devrez peut-être convertir une chaîne de caractères en nombre.

La capacité de convertir un type de données en un autre vous offre une grande flexibilité lorsque vous travaillez avec des informations.

JavaScript dispose de différentes méthodes intégrées pour convertir ou transtyper une chaîne de caractères en nombre.

Dans cet article, vous apprendrez certaines des méthodes JavaScript intégrées disponibles pour convertir des chaînes en nombres, ainsi qu'une introduction (ou un rappel !) aux bases du fonctionnement des chaînes et des nombres en JavaScript.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une chaîne de caractères en JavaScript ?](#questcequunechaine)
2. [Qu'est-ce qu'un nombre en JavaScript ?](#questcequunnombre)
3. [Comment vérifier le type de données d'une valeur en JavaScript ?](#typeof)
4. [Comment convertir une chaîne en nombre en utilisant la fonction `parseInt()`](#parseint)
5. [Comment convertir une chaîne en nombre en utilisant la fonction `parseFloat()`](#parsefloat)
6. [Comment convertir une chaîne en nombre en utilisant la fonction `Number()`](#number)
7. [Comment convertir une chaîne en nombre en utilisant les fonctions `Math`](#mathfunctions)
8. [Comment convertir une chaîne en nombre en multipliant et en divisant par `1`](#multiplication)
9. [Comment convertir une chaîne en nombre en utilisant l'opérateur unaire `+`](#unary)

## Qu'est-ce qu'une chaîne de caractères en JavaScript ? <a name="questcequunechaine"></a>

Les chaînes de caractères sont un moyen efficace de communiquer par le texte, comme le stockage et la manipulation de texte. Elles sont l'un des types de données les plus fondamentaux dans tous les langages de programmation.

Les chaînes de caractères en JavaScript sont un type de données primitif. Cela signifie qu'elles sont intégrées au langage par défaut.

Une chaîne de caractères est une séquence ordonnée de zéro ou plusieurs valeurs de caractères. Plus précisément, il s'agit d'une séquence d'un ou plusieurs caractères qui peuvent être des lettres, des nombres ou des symboles (comme des signes de ponctuation).

Généralement, vous pouvez savoir si une valeur de données est une chaîne de caractères si elle est entourée de guillemets, simples ou doubles.

Plus précisément, il existe trois façons de créer une chaîne de caractères en JavaScript :

- En utilisant des guillemets simples.
- En utilisant des guillemets doubles.
- En utilisant des backticks.

Voici comment créer une chaîne de caractères en utilisant des guillemets simples :

```js
// chaîne créée en utilisant des guillemets simples ('')
let phrasePreferee = 'Bonjour le monde !';
```

Voici comment créer une chaîne de caractères en utilisant des guillemets doubles :

```js
// chaîne créée en utilisant des guillemets doubles ("")
let phrasePreferee = "Bonjour le monde !";
```

Et voici comment créer une chaîne de caractères en utilisant des backticks :

```js
// chaîne créée en utilisant des backticks (``)
let phrasePreferee = `Bonjour le monde !`;
```

La dernière façon de créer des chaînes de caractères en JavaScript est également connue sous le nom de template literal.

## Qu'est-ce qu'un nombre en JavaScript ? <a name="questcequunnombre"></a>

Les nombres vous permettent de représenter des valeurs numériques et d'effectuer des opérations et des calculs mathématiques.

Les nombres en JavaScript sont un type de données primitif – tout comme les chaînes de caractères.

Contrairement à d'autres langages de programmation, vous n'avez pas besoin de spécifier le type de nombre que vous souhaitez créer. Par exemple, vous n'avez pas besoin de mentionner si le nombre sera un entier ou un flottant.

En JavaScript, il existe plusieurs types de nombres différents (positifs et négatifs) intégrés au langage :

- Entiers. Un entier est une valeur numérique qui n'inclut pas de partie décimale - également connu sous le nom de nombre rond ou entier.
- Flottants. Un flottant est un nombre avec une décimale et au moins un chiffre suivant le point décimal.
- Nombres exponentiels sont des nombres qui peuvent être des entiers ou des flottants et sont suivis d'un `e`. Le `e` indique la multiplication d'un nombre par `10` élevé à une puissance donnée.
- Nombres binaires (également connus sous le nom de nombres en base 2). Le binaire est un système numérique composé de seulement deux nombres : `0` et `1`. Il utilise 8 bits pour représenter un octet. Le nombre commence par un `0` suivi d'un `b` suivi d'un nombre de 8 bits.
- Nombres octaux (également connus sous le nom de nombres en base 8). Un nombre octal commence par un `0` suivi de chiffres octaux allant de `0 - 7`.
- Nombres hexadécimaux (également connus sous le nom de nombres en base 16). Un nombre hexadécimal commence par un `0` suivi d'un `x` ou `X`. Après cela, il peut y avoir une combinaison de chiffres hexadécimaux allant de `0 - 9` et de lettres allant de `A - F` (ou `a - f`). Les lettres `A - F` sont associées aux valeurs `10 -15`.

```js
// entier
let num = 47;

// flottant
let num = 47.32;

// exponentiel - pour représenter de grands nombres
let num = 477e2;  // égal à multiplier 477 par 10 à la puissance de 2 (ou 100) ce qui donne 47700

// exponentiel - pour représenter de petits nombres
let num = 477e-2;  // égal à diviser 477 par 10 à la puissance de 2 (ou 100) ce qui donne 4.77

// binaire
let num = 0b1111;    // représente 15

// octal
let num = 023; // représente 19

// hexadécimal
let num = 0xFF; // représente 255
```

Une chose à garder à l'esprit est que les nombres *ne devraient pas* être entourés de guillemets - cela les transformera automatiquement en chaîne de caractères.

```js
// ceci est une chaîne de caractères et non un nombre !
let num = '7';
```

## Comment vérifier le type de données d'une valeur en JavaScript ? <a name="typeof"></a>

Pour éviter toute erreur et double-vérifier le type de données d'une valeur en JavaScript, utilisez l'opérateur `typeof`.

Plus tôt, j'ai mentionné que les nombres entourés de guillemets sont des chaînes de caractères.

Vous pouvez vérifier cela par vous-même en faisant ce qui suit :

```js
let num = '7';
console.log(typeof num)

// string
```

## Comment convertir une chaîne en nombre en utilisant la fonction `parseInt()` <a name="parseint"></a>

La syntaxe générale de la fonction `parseInt()` est la suivante :

```js
parseInt(string, radix)
```

La fonction `parseInt()` prend deux arguments : une chaîne de caractères comme premier argument et un radix comme second argument optionnel.

La chaîne de caractères est la valeur qui doit être convertie en nombre.

Le radix spécifie le système de numération mathématique que vous souhaitez utiliser et la base du nombre qui sera retourné – que le nombre sera un nombre en base 2 (ou binaire), base 8 (ou octal), base 10 (décimal), ou base 16 (ou hexadécimal).

Si le radix n'est pas inclus, alors il est `10` (valeur décimale) par défaut.

```js
let num = '7';

let strToNum = parseInt(num, 10);

console.log(strToNum);
console.log(typeof strToNum);

// 7
// number
```

Que se passe-t-il si la chaîne contient des lettres et des nombres ? Elle retournera uniquement les nombres de la chaîne :

```js
let num = '7 chats 7';

let strToNum = parseInt(num, 10);

console.log(strToNum);
console.log(typeof strToNum);

// 7
// number
```

Lorsque `parseInt()` rencontre un caractère non numérique, il l'ignore ainsi que tous les caractères qui suivent, même s'il y a plus de nombres plus loin.

Une chose à garder à l'esprit est que si la chaîne ne *commence pas* par un nombre, alors `NaN` (qui signifie `Not a Number`) sera retourné à la place.

```js
let num = 'h7';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// NaN
```

La fonction `parseInt()` commence à la position `0` de la chaîne et détermine si le caractère à cette position peut être converti en nombre. Si ce n'est pas le cas, la fonction retourne `NaN` à la place, même si la chaîne contient des nombres plus tard.

Que se passe-t-il si vous avez une chaîne qui contient un flottant ? La fonction `parseInt()` l'arrondira et retournera un nombre entier :

```js
let num = '7.77';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// retourne 7 au lieu de 7.77
```

Si c'est le cas et que vous souhaitez effectuer une conversion littérale, il est préférable d'utiliser la fonction `parseFloat()` à la place.

## Comment convertir une chaîne en nombre en utilisant la fonction `parseFloat()` <a name="parsefloat"></a>

La syntaxe générale de la fonction `parseFloat()` est la suivante :

```js
parseFloat(string)
```

La syntaxe et les comportements de la fonction `parseFloat()` sont similaires à ceux de la fonction `parseInt()`. La principale différence est que `parseFloat()` ne prend qu'un seul argument et n'accepte pas de radix comme argument.

La fonction `parseFloat()` accepte une chaîne de caractères comme seul argument et retourne un flottant – un nombre avec un point décimal.

Utilisez la fonction `parseFloat()` lorsque vous souhaitez conserver la partie décimale et pas seulement la partie entière d'un nombre.

En reprenant le même exemple de la section précédente, voici comment vous le réécririez en utilisant `parseFloat()` :

```js
let num = '7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// 7.77
```

Tout comme `parseInt()`, la fonction `parseFloat()` ne retournera que le premier nombre et ignorera tout caractère non numérique :

```js
let num = '7.77 chats 7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// 7.77
```

Et tout comme `parseInt()` encore une fois, si le premier caractère n'est pas un nombre valide, la fonction `parseFloat()` retournera `NaN` au lieu d'un nombre car elle ne peut pas le convertir en nombre :

```js
let num = 'h7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// NaN
```

## Comment convertir une chaîne en nombre en utilisant la fonction `Number()` <a name="number"></a>

La syntaxe générale de la fonction `Number()` est la suivante :

```js
Number(string)
```

La différence entre la fonction `Number()` et les fonctions `parseInt()` et `parseFloat()` est que la fonction `Number()` essaie de convertir toute la chaîne en nombre d'un seul coup. Les méthodes de parsing convertissent une chaîne en nombre morceau par morceau, et elles parcourent les caractères qui composent la chaîne individuellement et un par un.

Prenons l'exemple suivant que vous avez vu plus tôt et qui utilisait `parseInt()` :

```js
let num = '7 chats 7';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// 7
```

Dès que `parseInt()` rencontre un caractère non numérique, il met fin à la conversion.

Voici comment le même exemple fonctionne avec la fonction `Number()` :

```js
let num = '7 chats 7';

let strToNum = Number(num);

console.log(strToNum);

// NaN
```

Puisque `Number()` tente de convertir et de transtyper toute la chaîne en nombre d'un seul coup, il retourne `NaN` car il rencontre des caractères non numériques et est donc incapable de convertir en nombre.

La fonction `Number()` est un excellent choix lorsque vous souhaitez que la conversion échoue si la chaîne contient des caractères non numériques.

Une autre chose à noter est que la fonction `Number()` ne retourne pas un nombre entier lorsqu'elle rencontre un nombre décimal, contrairement à la fonction `parseInt()` que vous avez vue plus tôt.

```js
let num = '7.77';

let strToNum = Number(num);

console.log(strToNum);

// 7.77
```

## Comment convertir une chaîne en nombre en utilisant les fonctions `Math` <a name="mathfunctions"></a>

L'objet `Math` est un objet JavaScript intégré. Et vous pouvez utiliser certaines de ses méthodes, telles que `Math.round()`, `Math.floor()`, et `Math.ceil()`, pour convertir des chaînes en nombres.

Une chose à garder à l'esprit lorsque vous utilisez les méthodes Math pour la conversion de type est que lorsque vous travaillez avec des flottants, elles les transformeront en entier, et le flottant perdra sa partie décimale.

Les méthodes convertiront la chaîne en l'entier équivalent le plus proche.

La fonction `Math.round()` convertit une chaîne en nombre et l'arrondit au nombre entier le plus proche :

```js
let num = '7.5';

let strToNum = Math.round(num);

console.log(strToNum);

// 8
```

Si la valeur de `num` est égale à `7.4`, j'obtiendrai le résultat suivant :

```js
let num = '7.4';

let strToNum = Math.round(num);

console.log(strToNum);

// 7
```

Si la chaîne contient des caractères non numériques, `Math.round()` retourne `NaN`.

```js
let num = '7.5a';

let strToNum = Math.round(num);

console.log(strToNum);

// NaN
```

La fonction `Math.floor()` convertit une chaîne en nombre et l'arrondit *vers le bas* au nombre entier le plus proche :

```js
let num = '7.87';

let strToNum = Math.floor(num);

console.log(strToNum);

// 7
```

Si la chaîne contient des caractères non numériques, `Math.floor()` retourne `NaN`. La façon dont cette fonction fonctionne est qu'elle essaie de convertir toute la chaîne en nombre puis évalue le résultat, ce qui signifie que la chaîne doit être une chaîne valide pour qu'elle fonctionne :

```js
let num = '7.87a';

let strToNum = Math.floor(num);

console.log(strToNum);

// NaN
```

La fonction `Math.ceil()` est l'opposé de `Math.floor()` puisqu'elle convertit une chaîne en nombre et l'arrondit *vers le haut* au nombre entier le plus proche :

```js
let num = '7.87';

let strToNum = Math.ceil(num);

console.log(strToNum);

// 8
```

De manière similaire aux exemples précédents, la fonction `Math.ceil()` retournera `NaN` lorsqu'elle rencontrera une valeur non numérique dans la chaîne :

```js
let num = '7.87a';

let strToNum = Math.ceil(num);

console.log(strToNum);

// NaN
```

## Comment convertir une chaîne en nombre en multipliant et en divisant par `1` <a name="multiplication"></a>

Multiplier par `1` est l'une des façons les plus rapides de convertir une chaîne en nombre :

```js
let convertirChaineEnNombre = "7" * 1;

console.log(convertirChaineEnNombre);
console.log(typeof convertirChaineEnNombre);

// 7
// number
```

Et si vous souhaitez effectuer une conversion de type sur un flottant, multiplier par `1` conserve la place décimale :

```js
let convertirChaineEnNombre = "7.1" * 1;

console.log(convertirChaineEnNombre);
console.log(typeof convertirChaineEnNombre);

// 7.1
// number
```

Si la chaîne contient des caractères non numériques, elle retournera `NaN` :

```js
let convertirChaineEnNombre = "7a" * 1;

console.log(convertirChaineEnNombre);

// NaN
```

Cette façon de convertir des chaînes en entiers fonctionne également en divisant une chaîne par `1` :

```js
let convertirChaineEnNombre = "7" / 1

console.log(convertirChaineEnNombre);
console.log(typeof(convertirChaineEnNombre));

// 7
// number
```

À ce stade, il est également utile de mentionner ce qui se passe lorsque vous essayez d'ajouter `1` à une chaîne pour la convertir en entier. Si vous essayiez de faire cela, voici le résultat que vous obtiendriez :

```js
let convertirChaineEnNombre = "7" + 1;

console.log(convertirChaineEnNombre);
console.log(typeof convertirChaineEnNombre);

// 71
// string
```

Dans l'exemple ci-dessus, `1` a été concaténé avec la chaîne `"7"`, ce qui signifie qu'il a été placé côte à côte avec la chaîne.


## Comment convertir une chaîne en nombre en utilisant l'opérateur unaire `+` <a name="unary"></a>

L'utilisation de l'opérateur unaire `+` est également l'une des façons les plus rapides de convertir une chaîne en nombre.

Vous placez l'opérateur plus, `+`, avant la chaîne, et il convertit la chaîne en entier :


```js
let convertirChaineEnNombre = +"7";

console.log(convertirChaineEnNombre);
console.log(typeof convertirChaineEnNombre);

// 7
// number
```

.. ou un flottant :

```js
let convertirChaineEnNombre = +"7.77";

console.log(convertirChaineEnNombre);

// 7.77
```

De manière similaire aux autres façons que vous avez vues pour convertir une chaîne en nombre, toute la chaîne doit contenir uniquement des caractères numériques pour que l'opérateur unaire `+` fonctionne. Si la chaîne ne représente pas un nombre, alors elle retournera `NaN` :

```js
let convertirChaineEnNombre = +"7a";

console.log(convertirChaineEnNombre);

// NaN
```


## Conclusion

Et voilà ! Vous savez maintenant certaines des façons de convertir une chaîne en nombre en JavaScript.

Pour en savoir plus sur JavaScript, rendez-vous sur la certification [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien pensé et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances.

Merci d'avoir lu !