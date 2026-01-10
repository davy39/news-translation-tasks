---
title: Comment manipuler les chaînes de caractères en JavaScript – Avec des exemples
  de code
subtitle: ''
author: Eric Hu
co_authors: []
series: null
date: '2024-05-24T21:46:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-manipulate-strings-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/js-string.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment manipuler les chaînes de caractères en JavaScript – Avec des exemples
  de code
seo_desc: 'String manipulation is a common task for programmers, whether it is extracting
  information from the string, converting letter cases, joining strings, or trimming
  extra white spaces.

  This tutorial covers various methods and techniques for manipulating...'
---

La manipulation de chaînes de caractères est une tâche courante pour les programmeurs, qu'il s'agisse d'extraire des informations d'une chaîne, de convertir les cas de lettres, de joindre des chaînes ou de supprimer les espaces blancs supplémentaires.

Ce tutoriel couvre diverses méthodes et techniques pour manipuler des chaînes de caractères en utilisant JavaScript, vous offrant un guide complet sur la façon de travailler avec des chaînes dans vos applications JavaScript.

## **Comment extraire un caractère d'une chaîne en JavaScript**

Commençons par parler de la façon d'extraire un seul caractère d'une chaîne. JavaScript offre trois méthodes différentes à cet effet : `charAt()`, `at()` et `charCodeAt()`.

### Comment utiliser `charAt(index)`

La méthode `charAt()` accepte un index et retourne le caractère à cet index.

```javascript
const str = "Hello World!";

console.log(str.charAt(0));
console.log(str.charAt(8));
console.log(str.charAt(16));
```

```text
H
r


```

Si l'index est hors de portée, `charAt()` retournera une chaîne vide (`""`).

### Comment utiliser `at(index)`

La méthode `at()` a été ajoutée à JavaScript avec ES2022, et elle est très similaire à `charAt()`. Vous lui passez un index, et la méthode retourne le caractère à cet index.

```javascript
const str = "Hello World!";

console.log(str.at(0));
console.log(str.at(8));
console.log(str.at(16));
```

```text
H
r
undefined
```

Lorsque l'index est hors de portée, `at()` retournera `undefined` au lieu d'une chaîne vide.

Une autre différence est que `at()` permet un indexage négatif, ce qui signifie que l'index `-1` retourne le dernier caractère de la chaîne, `-2` retourne l'avant-dernier caractère, et ainsi de suite.

```javascript
const str = "Hello World!";

console.log(str.at(-1));
console.log(str.at(-2));
```

```text
!
d
```

Avant `at()`, la seule façon de faire cela était via la propriété `length`.

```javascript
const str = "Hello World!";

console.log(str.charAt(str.length - 1)); // Le dernier caractère
console.log(str.charAt(str.length - 2)); // L'avant-dernier caractère
```

```text
!
d
```

### Comment utiliser `charCodeAt(index)`

La méthode `charCodeAt()` retourne le code [UTF-16](https://en.wikipedia.org/wiki/UTF-16) du caractère à l'index spécifié.

```javascript
const str = "Hello World!";

console.log(str.charCodeAt(0));
console.log(str.charCodeAt(4));
```

```text
72
111
```

## **Comment extraire une sous-chaîne en JavaScript**

Outre l'extraction d'un seul caractère, JavaScript permet également d'extraire une sous-chaîne en utilisant les méthodes `substring()` et `slice()`.

### Comment utiliser `substring(start, end)`

`substring()` extrait une sous-chaîne basée sur les index `start` (inclus) et `end` (exclus) fournis, et retourne la sous-chaîne sous forme de nouvelle chaîne.

```javascript
const str = "JavaScript";

console.log(str.substring(0, 4));
```

```text
Java
```

L'index `end` peut être omis, auquel cas la sous-chaîne sera extraite de `start` à la fin de la chaîne.

```javascript
const str = "JavaScript";

console.log(str.substring(4));
```

```text
Script
```

### Comment utiliser `slice(start, end)`

`slice()` est très similaire à `substring()`. Il extrait également une sous-chaîne basée sur les index `start` et `end` fournis, et retourne la sous-chaîne sous forme de nouvelle chaîne.

```javascript
const str = "JavaScript";

console.log(str.slice(0, 4));
```

```text
Java
```

L'index `end` peut également être omis.

```javascript
const str = "JavaScript";

console.log(str.slice(4));
```

```text
Script
```

La différence est que `slice()` accepte les index négatifs. Par exemple, l'exemple suivant extrait la sous-chaîne de l'index `-10` à `-6`.

```javascript
const str = "JavaScript";

console.log(str.slice(-10, -6));
```

```text
Java
```

## **Comment convertir une chaîne en majuscules ou minuscules en JavaScript**

Les méthodes `toUpperCase()` et `toLowerCase()` convertissent la chaîne en majuscules ou minuscules.

```javascript
const str = "JavaScript";

console.log(str.toUpperCase());
console.log(str.toLowerCase());
```

```text
JAVASCRIPT
javascript
```

## **Comment joindre deux chaînes ensemble en JavaScript**

La manière la plus simple de joindre deux chaînes ensemble est d'utiliser l'opérateur `+` :

```javascript
const str1 = "Hello";
const str2 = "World!";

const str3 = str1 + " " + str2;

console.log(str3);
```

```text
Hello World!
```

Alternativement, vous pouvez utiliser la méthode `concat()` :

```javascript
const str1 = "Hello";
const str2 = "World!";

const str3 = str1.concat(" ", str2);

console.log(str3);
```

```text
Hello World!
```

Ou vous pouvez utiliser des [littéraux de gabarit](https://www.freecodecamp.org/news/template-literals-in-javascript/) :

```javascript
const str1 = "Hello";
const str2 = "World!";

const str3 = `${str1} ${str2}`;

console.log(str3);
```

```text
Hello World!
```

## **Comment supprimer les espaces blancs supplémentaires d'une chaîne en JavaScript**

Lorsque vous travaillez avec des chaînes provenant de sources externes, telles que parsées à partir d'une page web ou reçues d'une entrée utilisateur, un problème courant que vous pourriez rencontrer est la présence d'espaces blancs au début et à la fin.

JavaScript offre trois méthodes différentes qui vous permettent de supprimer facilement les espaces blancs supplémentaires et de conserver uniquement les informations utiles.

La méthode `trimStart()` supprime les espaces blancs au début, y compris les espaces, les tabulations et les sauts de ligne. La méthode `trimEnd()` supprime les espaces blancs à la fin, et `trim()` supprime les espaces blancs des deux extrémités.

```javascript
const str = "  \n\tHello World!\t\n  ";

console.log(str.trimStart());
console.log(str.trimEnd());
console.log(str.trim());
```

```text
Hello World!


 Hello World!
Hello World!
```

## **Comment ajouter un remplissage à une chaîne en JavaScript**

Les méthodes `padStart()` et `padEnd()` peuvent être utilisées pour ajouter des caractères ou des sous-chaînes au début ou à la fin de la chaîne d'origine.

Les deux méthodes prennent deux arguments, `length` et une sous-chaîne. La sous-chaîne sera répétée plusieurs fois, jusqu'à ce que la chaîne résultante atteigne la longueur cible.

```javascript
const str = "123";

console.log(str.padStart(5, "0"));
console.log(str.padEnd(5, "0"));
```

```text
00123
12300
```

Si la sous-chaîne fait que la chaîne résultante dépasse la longueur cible, alors seule une partie de cette sous-chaîne sera utilisée.

```javascript
const str = "123";

console.log(str.padStart(8, "ok"));
```

```text
okoko123
```

Remarquez que la sous-chaîne `"ok"` est répétée deux fois, mais pour la troisième fois, elle fait que la chaîne résultante dépasse la limite de longueur, donc seul `"o"` est utilisé pour le remplissage final.

## **Comment répéter une chaîne en JavaScript**

`repeat()` retourne une nouvelle chaîne, avec le nombre spécifié de copies de la chaîne d'origine.

```javascript
const str = "123";

console.log(str.repeat(3));
```

```text
123123123
```

## **Comment diviser une chaîne en un tableau en JavaScript**

La méthode `split()` divise la chaîne en fonction du caractère donné, et retourne le résultat dans un tableau. Cette méthode est particulièrement utile lorsque vous devez extraire des informations d'une URL.

Par exemple, voici comment vous pouvez extraire le slug d'un article de blog :

```javascript
const url = "http://www.example.com/blog/example-article";

let arr = url.split("/");
console.log(arr);

let slug = arr[4];
console.log(slug);
```

```text
[ 'http:', '', 'www.example.com', 'blog', 'example-article' ]
example-article
```

## **Comment rechercher dans une chaîne en JavaScript**

Vous pouvez également rechercher un caractère ou une sous-chaîne en utilisant JavaScript.

### Comment utiliser `indexOf()` et `lastIndexOf()`

La méthode `indexOf()` retourne l'index de la **première** occurrence du caractère donné.

La méthode `lastIndexOf()` retourne l'index de la **dernière** occurrence du caractère donné.

```javascript
const str = "Hello World";

console.log(str.indexOf("l"));
console.log(str.lastIndexOf("l"));
```

```text
2
9
```

Les deux méthodes retourneront -1 si aucune correspondance n'est trouvée.

```javascript
const str = "Hello World";

console.log(str.indexOf("x"));
console.log(str.lastIndexOf("x"));
```

```text
-1
-1
```

### Comment utiliser `includes()`

La méthode `includes()` teste si la chaîne contient le caractère ou la sous-chaîne donnée. Elle retourne `true` si la sous-chaîne est trouvée, sinon `false` sera retourné.

```javascript
const str = "JavaScript";

console.log(str.includes("S"));
console.log(str.includes("Script"));
console.log(str.includes("script"));
```

```text
true
true
false
```

### Comment utiliser `startsWith()` et `endsWith()`

Comme leurs noms l'indiquent, ces deux méthodes testent si la sous-chaîne donnée est trouvée au début ou à la fin de la chaîne.

```javascript
const str = "JavaScript";

console.log(str.startsWith("Java"));
console.log(str.endsWith("Java"));

console.log(str.startsWith("Script"));
console.log(str.endsWith("Script"));
```

```text
true
false
false
true
```

## **Comment rechercher dans une chaîne en utilisant Regex en JavaScript**

Mais que faire si vous avez besoin de quelque chose de plus puissant ? Par exemple, les méthodes `indexOf()` et `lastIndexOf()` ne retournent que les première et dernière occurrences de la sous-chaîne, mais que faire si vous devez rechercher toutes les occurrences ?

Ou que faire si, au lieu d'une sous-chaîne, vous devez rechercher un motif, comme un numéro de téléphone ou une étiquette de prix ?

Cela peut être réalisé en combinant les méthodes de chaîne avec [Regex](https://www.thedevspace.io/course/javascript-regular-expressions), qui signifie expression régulière. C'est un outil de programmation qui permet de décrire des motifs dans une chaîne. Regex a une syntaxe très cryptique, mais peut être très utile parfois.

### Comment utiliser `search()`

La méthode `search()` fonctionne de manière similaire à `indexOf()` que nous venons de discuter. Elle retourne également la **première** occurrence de la sous-chaîne ou du motif correspondante, sauf que `search()` permet de passer une expression régulière.

L'exemple suivant, `/(?<=\$)\d\d?\d?\d?/`, recherche une étiquette de prix dans la chaîne, qui doit commencer par un signe dollar (`$`), et être suivie de 1 à 4 chiffres numériques.

```javascript
const str = "The laptop costs $1500. The tablet costs $1000.";

console.log(str.search("1500"));
console.log(str.search(/(?<=\$)\d\d?\d?\d?/));
console.log(str.search(/(?<=\$)\d\d?\d?\d?/g));
```

```text
18
18
18
```

Remarquez que le drapeau global (`g`) n'a aucun effet sur `search()`, et il retourne toujours la première occurrence de la correspondance.

### Comment utiliser `match()` et `matchAll()`

Comparé à `search()`, la méthode `match()` retourne beaucoup plus d'informations avec lesquelles vous pouvez travailler, comme la sous-chaîne réelle qui correspond au motif, l'index où la correspondance est trouvée, et plus encore.

```javascript
const str = "The laptop costs $1500. The tablet costs $1000.";

console.log(str.match(/(?<=\$)\d\d?\d?\d?/));
console.log(str.match(/(?<=\$)\d\d?\d?\d?/g));
```

```text
[
 '1500',
 index: 18,
 input: 'The laptop costs $1500. The tablet costs $1000.',
 groups: undefined
]
[ '1500', '1000' ]
```

En incluant un drapeau global, vous pouvez faire en sorte que `match()` retourne toutes les sous-chaînes correspondantes, au lieu de seulement la première.

Il existe également une méthode `matchAll()` qui vous oblige à utiliser le drapeau global. Sans lui, la méthode retournera une `TypeError`.

`matchAll()` retournera un [objet itérable](https://www.thedevspace.io/course/javascript-objects#iterating-over-an-object), que vous pouvez parcourir en utilisant une boucle `for of`.

```javascript
const str = "This laptop costs $1500. The tablet costs $1000.";

const prices = str.matchAll(/(?<=\$)\d\d\d\d/g);

for (let price of prices) {
  console.log(price);
}
```

```text
[
 '1500',
 index: 19,
 input: 'This laptop costs $1500. The tablet costs $1000.',
 groups: undefined
]
[
 '1000',
 index: 43,
 input: 'This laptop costs $1500. The tablet costs $1000.',
 groups: undefined
]
```

## **Comment remplacer un motif de chaîne en JavaScript**

Enfin, la méthode `replace()` permet de faire correspondre un motif, puis de remplacer les sous-chaînes correspondantes par une nouvelle chaîne. Par exemple :

```javascript
const str = "JavaScript javaScript Javascript";

console.log(str.replace(/JAVASCRIPT/i, "javascript"));
console.log(str.replace(/JAVASCRIPT/gi, "javascript"));
```

```text
javascript javaScript Javascript
javascript javascript javascript
```

Par défaut, `replace()` ne correspond et ne remplace que la première occurrence du motif, mais avec le drapeau global, vous pouvez remplacer tous les motifs correspondants.

## **Conclusion**

Dans ce tutoriel, nous avons exploré diverses méthodes que vous pouvez utiliser pour travailler avec des chaînes en JavaScript. Nous avons également couvert comment utiliser les expressions régulières pour faire correspondre des motifs de chaînes.

En résumé, voici les méthodes que nous avons discutées dans ce tutoriel :

* `charAt(index)` : Extrait le caractère à l'index spécifié d'une chaîne.
* `at(index)` : Récupère le caractère à l'index spécifié, supporte l'indexation négative.
* `charCodeAt(index)` : Retourne le code UTF-16 du caractère à l'index spécifié.
* `substring(start, end)` : Extrait une partie de la chaîne entre les index de début (inclus) et de fin (exclus).
* `slice(start, end)` : Similaire à `substring()`, extrait une partie de la chaîne entre les index de début (inclus) et de fin (exclus), mais supporte l'indexation négative.
* `toUpperCase()` : Convertit toutes les lettres de la chaîne en majuscules.
* `toLowerCase()` : Convertit toutes les lettres de la chaîne en minuscules.
* `concat()` : Joint deux chaînes ou plus ensemble.
* `trimStart()` : Supprime les espaces blancs au début d'une chaîne. Y compris les espaces, les tabulations et les nouvelles lignes.
* `trimEnd()` : Supprime les espaces blancs à la fin d'une chaîne.
* `trim()` : Supprime les espaces blancs des deux extrémités d'une chaîne.
* `padStart(length, substring)` : Remplit le début d'une chaîne avec une autre chaîne (plusieurs fois, si nécessaire) jusqu'à ce que la chaîne résultante atteigne la longueur donnée.
* `padEnd(length, substring)` : Remplit la fin de la chaîne avec une autre chaîne (plusieurs fois, si nécessaire) jusqu'à ce que la chaîne résultante atteigne la longueur donnée.
* `repeat(count)` : Retourne une nouvelle chaîne qui contient le nombre spécifié de copies de la chaîne d'origine.
* `split(separator)` : Divise la chaîne en un tableau de sous-chaînes, en utilisant le séparateur spécifié pour déterminer où faire la division.
* `indexOf(searchValue)` : Retourne l'index de la première occurrence de la sous-chaîne spécifiée. Retourne -1 si non trouvée.
* `lastIndexOf(searchValue)` : Retourne l'index de la dernière occurrence de la sous-chaîne spécifiée. Retourne -1 si non trouvée.
* `includes(searchValue)` : Détermine si la chaîne contient la sous-chaîne spécifiée, en retournant `true` ou `false`.
* `startsWith(searchValue)` : Vérifie si la chaîne commence par la sous-chaîne spécifiée.
* `endsWith(searchValue)` : Vérifie si la chaîne se termine par la sous-chaîne spécifiée.
* `search(regexp)` : Recherche un motif de chaîne, qui pourrait être défini par une Regex. Retourne l'index de la première occurrence de la correspondance ou -1 si non trouvée.
* `match(regexp)` : Recherche un motif de chaîne, qui est défini par une Regex. Si un drapeau global est inclus, il retournera toutes les occurrences du motif.
* `matchAll(regexp)` : Retourne un objet itérable contenant tous les résultats correspondant à une chaîne contre une expression régulière globale.
* `replace(regexp, newSubstr)` : Remplace les occurrences d'un motif (spécifié par une expression régulière) par une nouvelle sous-chaîne.

Si vous souhaitez en savoir plus sur JavaScript et le développement web, consultez mon nouveau cours sur [TheDevSpace.io](https://www.thedevspace.io/).