---
title: Apprendre les opérateurs JavaScript – Logiques, Comparaison, Ternaires, et
  Plus d'Opérateurs JS Avec Exemples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-14T15:44:58.000Z'
originalURL: https://freecodecamp.org/news/javascript-operators
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/JS-EVERY-OPERATOR.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: Apprendre les opérateurs JavaScript – Logiques, Comparaison, Ternaires,
  et Plus d'Opérateurs JS Avec Exemples
seo_desc: 'JavaScript has many operators that you can use to perform operations on
  values and variables (also called operands)

  Based on the types of operations these JS operators perform, we can divide them
  up into seven groups:


  Arithmetic Operators

  Assignment...'
---

JavaScript dispose de nombreux opérateurs que vous pouvez utiliser pour effectuer des opérations sur des valeurs et des variables (également appelées opérandes)

En fonction des types d'opérations que ces opérateurs JS effectuent, nous pouvons les diviser en sept groupes :

1. [Opérateurs arithmétiques](#heading-operateurs-arithmetiques)
2. [Opérateurs d'affectation](#heading-operateurs-daffectation)
3. [Opérateurs de comparaison](#heading-operateurs-de-comparaison)
4. [Opérateurs logiques](#heading-operateurs-logiques)
5. [Opérateurs ternaires](#heading-operateur-ternaire)
6. [L'opérateur `typeof`](#heading-loperateur-typeof)
7. [Opérateurs bit à bit](#heading-operateurs-bit-a-bit)

Dans ce manuel, vous allez apprendre comment ces opérateurs fonctionnent avec des exemples. Commençons par les opérateurs arithmétiques.

## Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés pour effectuer des opérations mathématiques comme l'addition et la soustraction.

Ces opérateurs sont fréquemment utilisés avec des types de données numériques, ils sont donc similaires à une calculatrice. L'exemple suivant montre comment vous pouvez utiliser l'opérateur `+` pour additionner deux variables ensemble :

```js
let x = 3;
let y = 8;

console.log(x + y); // 11
```

Ici, les deux variables `x` et `y` sont additionnées ensemble en utilisant l'opérateur plus `+`. Nous avons également utilisé la méthode `console.log()` pour imprimer le résultat de l'opération à l'écran.

Vous pouvez utiliser des opérateurs directement sur des valeurs sans les assigner à une variable aussi :

```js
console.log(2 + 1); // 3
console.log(4 + 1); // 5
```

En JavaScript, nous avons 8 opérateurs arithmétiques au total. Ils sont :

1. Addition `+`
2. Soustraction `-`
3. Multiplication `*`
4. Division `/`
5. Reste `%`
6. Exponentiation `**`
7. Incrément `++`
8. Décrément `--`

Voyons comment ces opérateurs fonctionnent un par un.

### 1. Opérateur d'addition

L'opérateur d'addition `+` est utilisé pour additionner deux ou plusieurs nombres ensemble. Vous avez vu comment cet opérateur fonctionne précédemment, mais voici un autre exemple :

```js
console.log(7 + 2); // 9
console.log(2.3 + 1.5); // 3.8
```

Vous pouvez utiliser l'opérateur d'addition sur des nombres entiers et flottants.

### 2. Opérateur de soustraction

L'opérateur de soustraction est marqué par le signe moins `-` et vous pouvez l'utiliser pour soustraire l'opérande de droite de l'opérande de gauche.

Par exemple, voici comment soustraire 3 de 5 :

```js
let x = 5;
let y = 3;

console.log(x - y); // 2
```

### 3. Opérateur de multiplication

L'opérateur de multiplication est marqué par le symbole astérisque `*`, et vous l'utilisez pour multiplier la valeur de gauche par la valeur de droite de l'opérateur.

```js
console.log(5 * 2); // 10
console.log(3 * 3); // 9
```

### 4. Opérateur de division

L'opérateur de division `/` est utilisé pour diviser l'opérande de gauche par l'opérande de droite. Voici quelques exemples d'utilisation de l'opérateur :

```js
console.log(10 / 2); // 5
console.log(9 / 3); // 3
```

### 5. Opérateur de reste

L'opérateur de reste `%` est également connu sous le nom d'opérateur modulo. Cet opérateur est utilisé pour calculer le reste après qu'une division a été effectuée.

Un exemple pratique devrait rendre cet opérateur plus facile à comprendre, alors voyons-en un :

```js
console.log(10 % 3);
```

Le nombre 10 ne peut pas être divisé par 3 parfaitement. Le résultat de la division est 3 avec un reste de 1. L'opérateur de reste retourne simplement ce reste.

Si l'opérande de gauche peut être divisé sans reste, alors l'opérateur retourne 0.

Cet opérateur est couramment utilisé lorsque vous voulez vérifier si un nombre est pair ou impair. Si un nombre est pair, le diviser par 2 donnera un reste de 0, et s'il est impair, le reste sera 1.

```js
console.log(1 % 2); // 1
console.log(2 % 2); // 0
console.log(3 % 2); // 1
console.log(4 % 2); // 0
```

### 6. Opérateur d'exponentiation

L'opérateur d'exponentiation est marqué par deux astérisques `**`. C'est l'un des nouveaux opérateurs JavaScript et vous pouvez l'utiliser pour calculer la puissance d'un nombre (basé sur son exposant).

Par exemple, voici comment calculer 10 à la puissance de 3 :

```js
console.log(10 ** 3); // 1000
```

Ici, le nombre 10 est multiplié par lui-même 3 fois (10 * 10 * 10)

L'opérateur d'exponentiation vous donne un moyen facile de trouver la puissance d'un nombre spécifique.

### 7. Opérateur d'incrément

L'opérateur d'incrément `++` est utilisé pour augmenter la valeur d'un nombre de un. Par exemple :

```js
let x = 5;

x++;

console.log(x); // 6
```

Cet opérateur vous donne un moyen plus rapide d'augmenter une valeur de variable de un. Sans l'opérateur, voici comment vous incrémentez une variable :

```js
let x = 5;

x = x + 1;

console.log(x); // 6
```

L'utilisation de l'opérateur d'incrément vous permet de raccourcir la deuxième ligne. Vous pouvez placer cet opérateur avant ou après la variable que vous souhaitez incrémenter :

```js
let x = 5;

// Placez l'opérateur après la variable (postfix)
x++;

// Placez l'opérateur avant la variable (prefix)
++x;
```

Les deux placements montrés ci-dessus sont valides. La différence entre le préfixe (avant) et le postfixe (après) est que la position du préfixe exécutera l'opérateur après que cette ligne de code ait été exécutée.

Considérez l'exemple suivant :

```js
let x = 5;
let y = 5;

console.log(x++); // 5
console.log(x); // 6

console.log(++y); // 6
console.log(y); // 6
```

Ici, vous pouvez voir que placer l'opérateur d'incrément après la variable imprimera la variable comme si elle n'avait pas été incrémentée.

Lorsque vous placez l'opérateur avant la variable, alors le nombre sera incrémenté avant d'appeler la méthode `console.log()`.

### 8. Opérateur de décrément

L'opérateur de décrément `--` est utilisé pour diminuer la valeur d'un nombre de un. C'est l'opposé de l'opérateur d'incrément :

```js
let x = 5;

x--;

console.log(x); // 4
```

Veuillez noter que vous ne pouvez utiliser les opérateurs d'incrément et de décrément que sur une variable. Une erreur se produit lorsque vous essayez d'utiliser ces opérateurs directement sur une valeur numérique :

```js
console.log(5--);
```

**Sortie :**

```txt
Uncaught SyntaxError: Invalid left-hand side expression in postfix operation
```

Vous ne pouvez pas utiliser l'opérateur d'incrément ou de décrément sur un nombre directement.

### Résumé des opérateurs arithmétiques

Maintenant que vous avez appris les 8 types d'opérateurs arithmétiques. Excellent ! Gardez à l'esprit que vous pouvez mélanger ces opérateurs pour effectuer des équations mathématiques complexes.

Par exemple, vous pouvez effectuer une addition et une multiplication sur un ensemble de nombres :

```js
console.log(5 + 2 * 3); // 11
```

L'ordre des opérations en JavaScript est le même qu'en mathématiques. La multiplication, la division et l'exponentiation ont une priorité plus élevée que l'addition ou la soustraction (rappelez-vous l'acronyme PEMDAS ? Parenthèses, exposants, multiplication et division, addition et soustraction – voici votre ordre des opérations).

Vous pouvez utiliser des parenthèses `()` pour changer l'ordre des opérations. Enveloppez l'opération que vous voulez exécuter en premier comme suit :

```js
console.log((5 + 2) * 3); // 21
```

Lorsque vous utilisez des opérateurs d'incrément ou de décrément avec d'autres opérateurs, vous devez placer les opérateurs en position de préfixe comme suit :

```js
let x = 5;
console.log(2 + ++x); // 2 + 6 = 8
```

C'est parce qu'un opérateur d'incrément ou de décrément postfixé ne sera pas exécuté avec d'autres opérations sur la même ligne, comme je l'ai expliqué précédemment.

Faisons quelques exercices. Pouvez-vous deviner le résultat de ces opérations ?

```js
console.log(5 * 3 - 2);
console.log((3 * 6) % 2);
console.log(5 + 7 - 1);
console.log((4 + 9) * 4);

let x = 5;
console.log(++x);
console.log(x++ / 3);
```

Et c'est tout pour les opérateurs arithmétiques. Vous avez fait un travail merveilleux en apprenant ces opérateurs.

Prenons une courte pause de cinq minutes avant de passer au type d'opérateurs suivant.

## Opérateurs d'affectation

Le deuxième groupe d'opérateurs que nous allons explorer est les opérateurs d'affectation.

Les opérateurs d'affectation sont utilisés pour assigner une valeur spécifique à une variable. L'opérateur d'affectation de base est marqué par le symbole égal `=`, et vous avez déjà vu cet opérateur en action auparavant :

```js
let x = 5;
```

Après l'opérateur d'affectation de base, il y a 5 autres opérateurs d'affectation qui combinent des opérations mathématiques avec l'affectation. Ces opérateurs sont utiles pour rendre votre code propre et court.

Par exemple, supposons que vous voulez incrémenter la variable `x` de 2. Voici comment vous le faites avec l'opérateur d'affectation de base :

```js
let x = 5;

x = x + 2;
```

Il n'y a rien de mal avec le code ci-dessus, mais vous pouvez utiliser l'affectation d'addition `+=` pour réécrire la deuxième ligne comme suit :

```js
let x = 5;

x += 2;
```

Il y a 7 types d'opérateurs d'affectation que vous pouvez utiliser en JavaScript :

| Nom                      | Exemple d'opération | Signification      |
| ------------------------- | ----------------- | ------------ |
| Affectation                | `x = y`           | `x = y`      |
| Affectation d'addition       | `x += y`          | `x = x + y`  |
| Affectation de soustraction    | `x -= y`          | `x = x - y`  |
| Affectation de multiplication | `x *= y`          | `x = x * y`  |
| Affectation de division       | `x /= y `         | `x = x / y`  |
| Affectation de reste      | `x %= y`          | `x = x % y`  |
| Affectation d'exponentiation | `x **= y`         | `x = x ** y` |

Les opérateurs arithmétiques que vous avez appris dans la section précédente peuvent être combinés avec l'opérateur d'affectation sauf les opérateurs d'incrément et de décrément.

Faisons un petit exercice. Pouvez-vous deviner les résultats de ces affectations ?

```js
let x = 3;

x += 2 * 3;
console.log(x);

x -= 3;
console.log(x);

x %= 2;
console.log(x);
```

Maintenant que vous avez appris les opérateurs d'affectation. Continuons et apprenons les opérateurs de comparaison.

## Opérateurs de comparaison

Comme le nom l'indique, les opérateurs de comparaison sont utilisés pour comparer une valeur ou une variable avec autre chose. Les opérateurs de cette catégorie retournent toujours une valeur booléenne : soit `true` soit `false`.

Par exemple, supposons que vous voulez comparer si la valeur d'une variable est supérieure à 1. Voici comment vous le faites :

```js
let x = 5;

console.log(x > 1); // true
console.log(x > 7); // false
```

L'opérateur supérieur à `>` vérifie si la valeur de l'opérande de gauche est supérieure à la valeur de l'opérande de droite.

Il y a 8 types d'opérateurs de comparaison disponibles en JavaScript :

| Nom                  | Exemple d'opération | Signification                                                                          |
| --------------------- | ----------------- | -------------------------------------------------------------------------------- |
| Égal                 | `x == y`          | Retourne `true` si les opérandes sont égaux                                         |
| Non égal             | `x != y`          | Retourne `true` si les opérandes ne sont pas égaux                                     |
| Strictement égal          | `x === y`         | Retourne `true` si les opérandes sont égaux et ont le même type                  |
| Strictement non égal      | `x !== y`         | Retourne `true` si les opérandes ne sont pas égaux, ou ont des types différents            |
| Supérieur à          | `x > y`           | Retourne `true` si l'opérande de gauche est supérieur à l'opérande de droite             |
| Supérieur ou égal à | `x >= y`          | Retourne `true` si l'opérande de gauche est supérieur ou égal à l'opérande de droite |
| Inférieur à             | `x < y `          | Retourne `true` si l'opérande de gauche est inférieur à l'opérande de droite                |
| Inférieur ou égal à    | `x <= y`          | Retourne `true` si l'opérande de gauche est inférieur ou égal à l'opérande de droite    |

Voici quelques exemples d'utilisation des opérateurs de comparaison :

```js
console.log(9 == 9); // true

console.log(9 != 20); // true

console.log(2 > 10); // false

console.log(2 < 10); // true

console.log(5 >= 10); // false

console.log(10 <= 10); // true
```

Les opérateurs de comparaison sont divisés en deux types : les opérateurs relationnels et les opérateurs d'égalité.

Les opérateurs relationnels comparent la valeur d'un opérande par rapport au deuxième opérande (supérieur à, inférieur à)

Les opérateurs d'égalité vérifient si la valeur de gauche est égale à la valeur de droite. Ils peuvent également être utilisés pour comparer des chaînes de caractères comme ceci :

```js
console.log("ABC" == "ABC"); // true

console.log("ABC" == "abc"); // false

console.log("Z" != "A"); // true
```

Les comparaisons de chaînes sont sensibles à la casse, comme le montre l'exemple ci-dessus.

JavaScript dispose également de deux versions des opérateurs d'égalité : lâche et stricte.

En mode strict, JavaScript comparera les valeurs sans effectuer de coercition de type. Pour activer le mode strict, vous devez ajouter un symbole égal `=` supplémentaire à l'opération comme suit :

```js
console.log("9" == 9); // true
// strictement égal
console.log("9" === 9); // false

console.log("1" != 1); // false
// strictement non égal
console.log("1" !== 1); // true
```

Puisque la coercition de type peut entraîner un comportement indésirable, vous devriez utiliser les opérateurs d'égalité stricte chaque fois que vous effectuez une comparaison d'égalité.

## Opérateurs logiques

Les opérateurs logiques sont utilisés pour vérifier si une ou plusieurs expressions résultent en `true` ou `false`.

Il y a trois opérateurs logiques disponibles en JavaScript :

| Nom        | Exemple d'opération | Signification                                                         |
| ----------- | ----------------- | --------------------------------------------------------------- | --- | --------------------------------------------------------------------- |
| ET logique | `x && y`          | Retourne `true` si tous les opérandes sont `true`, sinon retourne `false` |
| OU logique  | `x || y`  | Retourne `true` si l'un des opérandes est `true`, sinon retourne `false` |
| NON logique | `!x`              | Inverse le résultat : retourne `true` si `false` et vice versa    |

Ces opérateurs ne peuvent retourner que des valeurs booléennes. Par exemple, vous pouvez déterminer si '7 est supérieur à 2' et '5 est supérieur à 4' :

```js
console.log(7 > 2 && 5 > 4); // true
```

Ces opérateurs logiques suivent les lois de la logique mathématique :

1. `&&` opérateur ET – si une expression retourne `false`, le résultat est `false`
2. `||` opérateur OU – si une expression retourne `true`, le résultat est `true`
3. `!` opérateur NON – nie l'expression, retournant l'inverse.

Faisons un petit exercice. Essayez d'exécuter ces instructions sur votre ordinateur. Pouvez-vous deviner les résultats ?

```js
console.log(true && false);

console.log(false || false);

console.log(!true);
```

Ces opérateurs logiques seront utiles lorsque vous devrez affirmer qu'une exigence spécifique est remplie dans votre code.

Disons qu'une `vieHeureuse` nécessite un travail avec un `revenuEleve` et une `equipeSoutenante` :

```js
let revenuEleve = true;
let equipeSoutenante = true;
let vieHeureuse = revenuEleve && equipeSoutenante;

console.log(vieHeureuse); // true
```

Sur la base des exigences, vous pouvez utiliser l'opérateur ET logique pour vérifier si vous avez les deux exigences. Lorsque l'une des exigences est `false`, alors `vieHeureuse` est également `false`.

## Opérateur ternaire

L'opérateur ternaire (également appelé opérateur conditionnel) est le seul opérateur JavaScript qui nécessite 3 opérandes pour fonctionner.

Imaginons que vous devez implémenter une logique spécifique dans votre code. Supposons que vous ouvrez un magasin pour vendre des fruits. Vous donnez une réduction de 3 $ lorsque le total des achats est de 20 $ ou plus. Sinon, vous donnez une réduction de 1 $.

Vous pouvez implémenter la logique en utilisant une instruction `if..else` comme suit :

```js
let totalAchat = 15;

let reduction;

if (totalAchat >= 20) {
  reduction = 3;
} else {
  reduction = 1;
}
```

Le code ci-dessus fonctionne bien, mais vous pouvez utiliser l'opérateur ternaire pour rendre le code plus court et plus concis comme suit :

```js
let totalAchat = 15;

let reduction = totalAchat >= 20 ? 3 : 1;
```

La syntaxe de l'opérateur ternaire est `condition ? expression1 : expression2`.

Vous devez écrire la `condition` à évaluer suivie d'un point d'interrogation `?`.

À côté du point d'interrogation, vous écrivez l'expression à exécuter lorsque la condition est évaluée à `true`, suivie d'un symbole deux-points `:`. Vous pouvez appeler cela `expression1`.

À côté du symbole deux-points, vous écrivez l'expression à exécuter lorsque la condition est évaluée à `false`. C'est `expression2`.

Comme le montre l'exemple ci-dessus, l'opérateur ternaire peut être utilisé comme une alternative à l'instruction `if..else`.

## L'opérateur `typeof`

L'opérateur `typeof` est le seul opérateur qui n'est pas représenté par des symboles. Cet opérateur est utilisé pour vérifier le type de données de la valeur que vous avez placée du côté droit de l'opérateur.

Voici quelques exemples d'utilisation de l'opérateur :

```js
let x = 5;
console.log(typeof x) //  'number'

console.log(typeof "Nathan") // 'string'

console.log(typeof true) // 'boolean'

console.log(typeof null) // 'object'

console.log(typeof [1, 2, 3]) // 'object'

console.log(typeof {}) // 'object'

console.log(typeof undefined) // 'undefined'
```

L'opérateur `typeof` retourne le type des données sous forme de chaîne. Le type 'number' représente à la fois les types entier et flottant, les types string et boolean représentent leurs types respectifs.

Les tableaux, les objets et la valeur `null` sont de type object, tandis que `undefined` a son propre type.

## Opérateurs bit à bit

Les opérateurs bit à bit sont des opérateurs qui traitent leurs opérandes comme un ensemble de chiffres binaires, mais retournent le résultat de l'opération sous forme de valeur décimale.

Ces opérateurs sont rarement utilisés dans le développement web, vous pouvez donc sauter cette partie si vous ne voulez apprendre que des choses pratiques. Mais si vous êtes intéressé à savoir comment ils fonctionnent, alors laissez-moi vous montrer un exemple.

Un ordinateur utilise un système de nombres binaires pour stocker des nombres décimaux en mémoire. Le système binaire n'utilise que deux nombres, 0 et 1, pour représenter toute la gamme de nombres décimaux que nous, humains, connaissons.

Par exemple, le nombre décimal 1 est représenté par le nombre binaire 00000001, et le nombre décimal 2 est représenté par 00000010.

Je ne vais pas entrer dans les détails sur la façon de convertir un nombre décimal en un nombre binaire car c'est trop long à inclure dans ce guide. Le point principal est que les opérateurs bit à bit fonctionnent sur ces nombres binaires.

Si vous voulez trouver le nombre binaire à partir d'un nombre décimal spécifique, vous pouvez chercher sur Google le "convertisseur décimal en binaire".

Il y a 7 types d'opérateurs bit à bit en JavaScript :

1. ET `&`
2. OU `|`
3. XOR `^`
4. NON `~`
5. Déplacement à gauche `<<`
6. Déplacement à droite `>>`
7. Déplacement à droite avec remplissage de zéros `>>>`

Voyons comment ils fonctionnent.

### 1. Opérateur bit à bit ET

L'opérateur bit à bit ET `&` retourne un 1 lorsque le nombre 1 se chevauche dans les deux opérandes. Les nombres décimaux 1 et 2 n'ont pas de chevauchement de 1, donc l'utilisation de cet opérateur sur les nombres retourne 0 :

```js
// 1 = 00000001
// 2 = 00000010
// ------------
//     00000000 = 0

console.log(1 & 2); // 0
```

### 2. Opérateur bit à bit OU

D'autre part, l'opérateur bit à bit OU `|` retourne tous les 1 dans les deux nombres décimaux.

```js
// 1 = 00000001
// 2 = 00000010
// ------------
//     00000011 = 3

console.log(1 | 2); // 3
```

Le nombre binaire 00000011 représente le nombre décimal 3, donc l'opérateur OU ci-dessus retourne 3.

### Opérateur bit à bit XOR

Le XOR bit à bit `^` recherche les différences entre deux nombres binaires. Lorsque les bits correspondants sont les mêmes, il retourne 0 :

5 = 00000101

```js
// 5 = 00000101
// 7 = 00000111
// ------------
//     00000010 = 2

console.log(5 ^ 7); // 2
```

### Opérateur bit à bit NON

L'opérateur bit à bit NON `~` inverse les bits d'un nombre décimal de sorte que 0 devient 1 et 1 devient 0 :

```js
// 5 = 00000101
// ------------
//     11111010 = -6

console.log(~5); // -6
```

### Opérateur de déplacement à gauche bit à bit

Le déplacement à gauche bit à bit `<<` décale la position du bit en ajoutant des zéros à droite.

Les bits excédentaires sont ensuite supprimés, modifiant le nombre décimal représenté par les bits. Voir l'exemple suivant :

```js
console.log(5 << 2);

// 5 = 00000101
// ------------ << Déplacement à gauche de 2
//     00010100 = 20
```

L'opérande de droite est le nombre de zéros que vous allez ajouter à l'opérande de gauche.

### Opérateur de déplacement à droite bit à bit

Le déplacement à droite bit à bit `>>` décale la position des bits en ajoutant des zéros à gauche. C'est l'inverse de l'opérateur de déplacement à gauche :

```js
console.log(5 >> 2); // 1

// 5 = 00000101
// ------------ >> Déplacement à droite de 2
//     00000001 = 1
```

### Opérateur de déplacement à droite bit à bit avec remplissage de zéros

Également connu sous le nom d'opérateur de déplacement à droite non signé, l'opérateur de déplacement à droite avec remplissage de zéros `>>>` est utilisé pour décaler la position des bits vers la droite, tout en changeant le bit de signe en `0`.

Cet opérateur transforme tout nombre négatif en un nombre positif, vous pouvez donc voir comment il fonctionne lorsque vous passez un nombre négatif comme opérande de gauche :

```js
console.log(-70 >> 1); // -35
console.log(-70 >>> 1); // 2147483613

console.log(5 >> 1); // 2
console.log(5 >>> 1); // 2
```

Dans l'exemple ci-dessus, vous pouvez voir que les opérateurs `>>` et `>>>` retournent des résultats différents. L'opérateur de déplacement à droite avec remplissage de zéros n'a aucun effet lorsque vous l'utilisez sur un nombre positif.

Maintenant que vous avez appris comment fonctionnent les opérateurs bit à bit. Si vous pensez qu'ils sont déroutants, alors vous n'êtes pas seul ! Heureusement, ces opérateurs sont rarement utilisés lors du développement d'applications web.

Vous n'avez pas besoin de les apprendre en profondeur. Il suffit de savoir ce qu'ils sont.

## Conclusion

Dans ce tutoriel, vous avez appris les 7 types d'opérateurs JavaScript : les opérateurs arithmétiques, d'affectation, de comparaison, logiques, ternaires, typeof et bit à bit.

Ces opérateurs peuvent être utilisés pour manipuler des valeurs et des variables afin d'obtenir un résultat souhaité.

Félicitations pour avoir terminé ce guide !

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !