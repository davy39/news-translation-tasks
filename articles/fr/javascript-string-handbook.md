---
title: Le guide des chaînes de caractères en JavaScript – Comment manipuler les chaînes
  en JS
date: '2024-01-05T17:19:11.000Z'
author: Joan Ayebola
authorURL: https://www.freecodecamp.org/news/author/joanayebola/
originalURL: https://freecodecamp.org/news/javascript-string-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/The-JavaScript-String-Handbook-Version-2--1-.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: Strings
  slug: strings
- name: Web Development
  slug: web-development
seo_desc: Strings, in the context of JavaScript, are essential data types that represent
  sequences of characters. They are integral to web development, forming the foundation
  for handling and presenting textual information on websites. Whether it's displaying
  ...
---


Les chaînes de caractères (strings), dans le contexte de JavaScript, sont des types de données essentiels qui représentent des séquences de caractères. Elles sont font partie intégrante du développement web, formant la base de la manipulation et de la présentation des informations textuelles sur les sites web. Qu'il s'agisse d'afficher des noms d'utilisateurs, de gérer la saisie de formulaires ou de générer du contenu dynamique, les chaînes de caractères sont omniprésentes dans la programmation JavaScript.

<!-- more -->

La manipulation de chaînes est un aspect crucial de la programmation en JavaScript, permettant aux développeurs de transformer, d'analyser et de présenter les données de manière efficace. La capacité à manipuler les chaînes efficacement permet aux développeurs de concevoir des applications robustes et conviviales.

Cet article sert de guide pour naviguer dans le paysage complexe de la gestion des chaînes en JavaScript. En explorant les bases, les propriétés, les méthodes et les techniques avancées, vous acquerrez une compréhension approfondie de la manière de manier les chaînes efficacement. L'objectif est de vous doter des connaissances et des compétences nécessaires pour exploiter tout le potentiel des chaînes de caractères en JavaScript.

## Table des matières

1.  **[Que sont les chaînes de caractères en JavaScript ?][1]**
2.  **[Opérations de base sur les chaînes][2]**  
    – [Guillemets simples et doubles][3]
3.  **[Gabarits de chaînes (Template Literals)][4]**  
    – [Utilisation de base][5]  
    – [Chaînes multilignes][6]  
    – [Évaluation d'expressions][7]  
    – [Gabarits étiquetés (Tagged templates)][8]  
    – [Cas d'utilisation][9]
4.  **[Le constructeur String][10]**  
    – [Utiliser le constructeur String][11]  
    – [Objets String vs primitives string][12]  
    – [Convertir des objets String en primitives][13]  
    – [Cas d'utilisation rares][14]
5.  **[La méthode String.fromCharCode][15]**  
    – [Utilisation de base][16]  
    – [Créer des chaînes à partir de valeurs Unicode][17]  
    – [Cas d'utilisation][18]
6.  **[Concaténation][19]**  
    – [Utiliser l'opérateur +][20]  
    – [Utiliser la méthode concat][21]  
    – [Concaténer des variables et des chaînes][22]  
    – [Combiner `String.fromCharCode` avec la concaténation][23]
7.  **[Caractéristiques des chaînes][24]**  
    – [Immuabilité][25]  
    – [Séquence de caractères][26]
8.  **[Méthodes de manipulation de la casse][27]**  
    – [toUpperCase()][28]  
    – [toLowerCase()][29]
9.  **[Suppression des espaces blancs avec trim(), trimStart() et trimEnd()][30]**  
    – [trim()][31]  
    – [trimStart()][32]  
    – [trimEnd()][33]  
    – [Cas d'utilisation][34]
10.  **[Recherche dans les chaînes][35]**  
    – [indexOf() et lastIndexOf()][36]  
    – [Méthode includes() pour la présence de sous-chaînes][37]  
    – [Méthodes startsWith() et endsWith()][38]
11.  **[Extraction de sous-chaînes avec slice() et substring()][39]**  
    – [slice()][40]  
    – [substring()][41]
12.  **[Modification de chaînes][42]**  
    – [Remplacer des sous-chaînes avec la méthode replace()][43]  
    – [Diviser des chaînes avec split()][44]  
    – [Joindre des tableaux en une chaîne avec join()][45]
13.  **[Comparaison de chaînes][46]**  
    – [Vérifications d'égalité avec === et ==][47]  
    – [Comparaison de chaînes sensible à la locale avec localeCompare()][48]  
    – [Comparer des chaînes en utilisant `localeCompare()`][49]
14.  **[Expressions régulières et chaînes][50]**  
    – [Utiliser RegExp pour la correspondance et la manipulation de chaînes][51]  
    – [Méthodes de chaîne avec expressions régulières : match(), search(), replace()][52]
15.  **[Unicode et chaînes][53]**  
    – [Chaînes et Unicode en JavaScript][54]  
    – [Créer des chaînes Unicode][55]  
    – [Points de code Unicode][56]  
    – [Itération sur les points de code][57]
16.  **[Pièges courants avec les chaînes][58]**  
    – [Coercition entre chaîne et nombre][59]  
    – [Comportement inattendu avec les espaces blancs][60]  
    – [Gérer les caractères spéciaux][61]
17.  **[Études de cas et exemples][62]**  
    – [Validation des entrées utilisateur][63]  
    – [Formatage de noms][64]
18.  **[Conclusion][65]**

## Que sont les chaînes de caractères en JavaScript ?

En JavaScript, les chaînes de caractères sont des séquences de caractères entourées soit de guillemets simples, soit de guillemets doubles. Cette flexibilité permet aux développeurs de choisir le style de citation en fonction de leurs préférences ou des exigences contextuelles. Par exemple :

```
let greeting = "Hello, World!"; 
let message = "JavaScript is powerful.";
```

## Opérations de base sur les chaînes

La création de chaînes en JavaScript est une opération fondamentale, et il existe plusieurs façons d'y parvenir. Explorons les différentes méthodes de création de chaînes en JavaScript.

### Guillemets simples et doubles

En JavaScript, les chaînes peuvent être créées en utilisant soit des guillemets simples (`'`), soit des guillemets doubles (`"`). Les deux types de guillemets sont interchangeables, et le choix entre eux est souvent une question de préférence personnelle ou de respect des conventions de codage.

#### Guillemets simples

```
const singleQuotedString = 'Hello, World!';
```

#### Guillemets doubles

```
const doubleQuotedString = "Hello, World!";
```

Dans les exemples ci-dessus, `singleQuotedString` et `doubleQuotedString` représentent tous deux la même chaîne, `"Hello, World!"`. L'utilisation de guillemets simples ou doubles est largement un choix stylistique, et il n'y a aucune différence fonctionnelle entre eux en JavaScript.

#### Échapper les guillemets

Si vous devez inclure un caractère de guillemet à l'intérieur d'une chaîne qui est entourée par le même type de guillemet, vous pouvez utiliser la barre oblique inverse (`\`) comme caractère d'échappement :

```
const stringWithSingleQuotes = 'He said, \'Hello!\'';
const stringWithDoubleQuotes = "She said, \"Hi!\"";
```

Dans les exemples ci-dessus, la barre oblique inverse avant les guillemets simples ou doubles permet de les traiter comme un caractère littéral au sein de la chaîne.

#### Choisir entre guillemets simples et doubles

Le choix entre guillemets simples et doubles dépend souvent des préférences personnelles ou de l'équipe. Certains développeurs ou conventions de codage peuvent privilégier l'un par rapport à l'autre pour des raisons de cohérence au sein d'une base de code.

Bien que vous puissiez librement passer des guillemets simples aux guillemets doubles, même au sein du même projet, comme ceci :

```
const message1 = 'This is a message with single quotes.';
const message2 = "This is a message with double quotes.";
```

il est essentiel d'être cohérent dans votre utilisation tout au long de votre code pour maintenir la lisibilité et éviter la confusion :

```
// Utilisation cohérente des guillemets simples
const message1 = 'This is a message.';
const name = 'John';

// Utilisation cohérente des guillemets doubles
const message2 = "This is another message.";
const greeting = "Hello";
```

Que vous choisissiez des guillemets simples ou doubles, l'important est d'être cohérent dans votre utilisation pour garantir un code propre et lisible.

## Gabarits de chaînes (Template Literals)

Les gabarits de chaînes, introduits dans ECMAScript 6 (ES6), offrent une manière plus puissante et flexible de créer des chaînes en JavaScript. Ils proposent une syntaxe améliorée pour intégrer des variables et des expressions au sein des chaînes, rendant le code plus concis et lisible.

### Utilisation de base

```
const name = 'John';
const greeting = `Hello, ${name}!`;

console.log(greeting); // Output: Hello, John!
```

Dans cet exemple, la chaîne est définie à l'aide de backticks (`` `), et la variable `name` est intégrée dans la chaîne à l'aide de ``${}\`. Cette syntaxe vous permet d'inclure de manière transparente des variables et des expressions directement dans la chaîne.

### Chaînes multilignes

Les gabarits de chaînes prennent également en charge les chaînes multilignes, ce qui facilite la représentation de texte sur plusieurs lignes sans avoir recours à la concaténation ou à des caractères spéciaux :

```
const multilineString = `
  This is a multiline
  string using template literals.
`;

console.log(multilineString);

/*
Output:
  This is a multiline
  string using template literals.
*/
```

### Évaluation d'expressions

Les expressions à l'intérieur de `${}` sont évaluées, ce qui permet des expressions et des calculs plus complexes au sein de la chaîne :

```
const num1 = 5;
const num2 = 10;
const result = `The sum of ${num1} and ${num2} is ${num1 + num2}.`;

console.log(result); // Output: The sum of 5 and 10 is 15.
```

### Gabarits étiquetés (Tagged Templates)

Les gabarits de chaînes peuvent également être utilisés avec une fonction, appelée "fonction d'étiquetage", permettant un traitement plus avancé des chaînes. La fonction reçoit les parties de la chaîne et les valeurs comme des arguments séparés, permettant une manipulation personnalisée de la chaîne :

```
function customTag(strings, ...values) {
  const result = '';
  for (let i = 0; i < strings.length; i++) {
    result += strings[i];
    if (i < values.length) {
      result += values[i];
    }
  }
  return result;
}

const name = 'John';
const age = 30;
const taggedResult = customTag`My name is ${name} and I am ${age} years old.`;

console.log(taggedResult); // Output: My name is John and I am 30 years old.
```

### Cas d'utilisation

#### Création dynamique de chaînes

Les gabarits de chaînes sont particulièrement utiles lors de la création dynamique de chaînes basées sur des variables ou des expressions :

```
const product = 'Laptop';
const price = 1200;

const purchaseDetails = `You have purchased a ${product} for $${price}.`;
console.log(purchaseDetails);
// Output: You have purchased a Laptop for $1200.
```

#### Gabarits HTML

Les gabarits de chaînes sont couramment utilisés dans le développement frontend pour créer dynamiquement des templates HTML :

```
const itemName = 'Smartphone';
const itemDescription = 'The latest model with advanced features.';

const htmlTemplate = `
  <div class="item">
    <h2>${itemName}</h2>
    <p>${itemDescription}</p>
  </div>
`;
```

Les gabarits de chaînes offrent une manière plus élégante et expressive de travailler avec les chaînes, en particulier dans les scénarios impliquant du contenu dynamique ou des chaînes multilignes. Leur introduction a considérablement amélioré la lisibilité et la maintenabilité du code JavaScript.

## Le constructeur `String`

En JavaScript, le constructeur `String` est un moyen de créer un objet chaîne. Bien que la plupart des développeurs créent couramment des chaînes à l'aide de littéraux de chaîne (guillemets simples ou doubles) ou de gabarits de chaînes (backticks), le constructeur `String` offre une approche alternative pour créer des chaînes.

### Utiliser le constructeur `String`

```
const str = new String('This is a string');
console.log(str); // Output: This is a string
```

Dans cet exemple, la syntaxe `new String` est utilisée pour créer un objet chaîne avec la valeur `'This is a string'`. Cependant, il est important de noter que l'utilisation du constructeur `String` pour créer des chaînes est moins courante dans la programmation JavaScript quotidienne que l'utilisation de littéraux de chaîne.

### Objets String vs primitives string

Les chaînes créées à l'aide du constructeur `String` sont des instances de l'objet `String`, tandis que les chaînes créées avec des littéraux de chaîne sont des valeurs primitives. Cette distinction a des implications sur le comportement de ces chaînes :

```
const primitiveString = 'Hello, World!'; // primitive string
const objectString = new String('Hello, World!'); // string object

console.log(typeof primitiveString); // Output: string
console.log(typeof objectString);    // Output: object
```

Comme on le voit dans l'exemple ci-dessus, `primitiveString` est de type `string`, tandis que `objectString` est de type `object`. La plupart des opérations sur les chaînes sont conçues pour fonctionner avec des chaînes primitives, et dans la plupart des cas, l'utilisation de littéraux de chaîne est préférable.

### Convertir des objets String en primitives

Dans les situations où vous avez un objet chaîne mais que vous devez effectuer des opérations de chaîne qui fonctionnent avec des primitives, vous pouvez convertir l'objet en une chaîne primitive à l'aide de la méthode `valueOf` ou `toString` :

```
const objectString = new String('Hello, World!');
const primitiveString = objectString.valueOf();

console.log(typeof primitiveString); // Output: string
```

### Cas d'utilisation rares

Le constructeur `String` est rarement utilisé pour créer des chaînes dans le développement JavaScript typique. Les littéraux de chaîne et les gabarits de chaînes sont plus concis et largement acceptés dans la communauté. Cependant, le constructeur `String` peut avoir des cas d'utilisation de niche où vous devez travailler explicitement avec des objets chaînes :

```
const str1 = 'Hello';
const str2 = new String('Hello');

console.log(str1 === str2); // Output: false
```

Dans l'exemple ci-dessus, `str1` et `str2` peuvent avoir la même valeur, mais ils ne sont pas strictement égaux car `str2` est un objet chaîne.

En résumé, bien que le constructeur `String` offre une manière alternative de créer des chaînes en tant qu'objets, ce n'est pas la méthode préférée pour la création quotidienne de chaînes en JavaScript. L'utilisation de littéraux de chaîne est plus concise, lisible et s'aligne sur les pratiques de codage courantes.

## La méthode `String.fromCharCode`

La méthode `String.fromCharCode` en JavaScript est un moyen de créer une chaîne à partir d'une séquence de valeurs Unicode. Unicode est un système de codage de caractères standardisé qui attribue un numéro unique à chaque caractère, garantissant la cohérence entre les différentes plateformes et langages.

### Utilisation de base

```
const str = String.fromCharCode(72, 101, 108, 108, 111);
console.log(str); // Output: Hello
```

Dans cet exemple, les valeurs Unicode `72`, `101`, `108`, `108` et `111` correspondent respectivement aux caractères `H`, `e`, `l`, `l` et `o`. La méthode `String.fromCharCode` prend ces valeurs comme arguments et renvoie une chaîne composée des caractères correspondants.

### Créer des chaînes à partir de valeurs Unicode

Vous pouvez utiliser `String.fromCharCode` pour créer des chaînes à partir d'une série de valeurs Unicode. Par exemple, pour créer une chaîne représentant le mot `JavaScript` :

```
const jsString = String.fromCharCode(74, 97, 118, 97, 83, 99, 114, 105, 112, 116);
console.log(jsString); // Output: JavaScript
```

Cette méthode est moins couramment utilisée pour la création simple de chaînes, mais peut être utile dans des situations où vous disposez de valeurs Unicode spécifiques pour représenter des caractères.

### Cas d'utilisation :

#### Générer des chaînes avec des caractères spécifiques

```
const specialString = String.fromCharCode(9829, 9786, 8482);
console.log(specialString); // Output: ♥☺™
```

Cela peut être utile lorsque vous souhaitez inclure des symboles ou des caractères spéciaux dans vos chaînes.

#### Création dynamique de chaînes

```
const unicodeValues = [72, 105, 33];
const dynamicString = String.fromCharCode(...unicodeValues);
console.log(dynamicString); // Output: Hi!
```

L'utilisation de l'opérateur de décomposition (spread operator `...`) vous permet de passer un tableau de valeurs Unicode.

Bien que la méthode `String.fromCharCode` ne soit pas aussi couramment utilisée que d'autres méthodes de création de chaînes, elle offre une approche unique lors de la manipulation de codages de caractères spécifiques ou lorsque vous disposez d'une séquence de valeurs Unicode devant être convertie en chaîne. Comprendre ses cas d'utilisation peut enrichir votre boîte à outils pour la manipulation de chaînes en JavaScript.

## Concaténation

La concaténation est une opération fondamentale sur les chaînes en JavaScript qui consiste à combiner deux ou plusieurs chaînes en une seule. Ce processus vous permet de construire des chaînes plus longues en ajoutant ou en joignant des chaînes existantes. En JavaScript, la concaténation peut être réalisée à l'aide de l'opérateur `+` ou de la méthode `concat`.

### Utiliser l'opérateur `+`

L'opérateur `+` est le moyen le plus courant de concaténer des chaînes. Il fonctionne en combinant les caractères de deux chaînes pour créer une nouvelle chaîne :

```
const firstName = 'John';
const lastName = 'Doe';
const fullName = firstName + ' ' + lastName;
console.log(fullName); // Output: John Doe
```

Dans cet exemple, les chaînes `John` et `Doe` sont concaténées avec un espace entre elles pour former le nom complet `John Doe`.

Vous pouvez également concaténer plus de deux chaînes :

```
const greeting = 'Hello';
const target = 'World';
const message = greeting + ', ' + target + '!';
console.log(message); // Output: Hello, World!
```

### Utiliser la méthode `concat`

La méthode `concat` est une alternative pour concaténer des chaînes. C'est une méthode de chaîne qui peut être utilisée pour concaténer deux ou plusieurs chaînes :

```
const firstName = 'John';
const lastName = 'Doe';
const fullName = firstName.concat(' ', lastName);
console.log(fullName); // Output: John Doe
```

La méthode `concat` peut prendre plusieurs arguments, en les concaténant dans l'ordre où ils sont fournis :

```
const str1 = 'Hello';
const str2 = ' ';
const str3 = 'World';
const greeting = str1.concat(str2, str3, '!');
console.log(greeting); // Output: Hello World!
```

### Concaténer des variables et des chaînes

La concaténation est souvent utilisée lors de la combinaison de variables et de chaînes pour créer du contenu dynamique :

```
const userName = 'John';
const userGreeting = 'Welcome, ' + userName + '!';
console.log(userGreeting); // Output: Welcome, John!
```

C'est une technique puissante, en particulier dans les scénarios où vous devez construire des messages, afficher des sorties conviviales ou générer du contenu dynamique dans des applications web.

Il est important de noter que bien que la concaténation soit un moyen simple et efficace de combiner des chaînes, elle peut devenir moins performante lors de la gestion d'un grand nombre de concaténations. Dans de tels cas, d'autres approches, comme l'utilisation de gabarits de chaînes ou de jointures de tableaux, pourraient être plus performantes.

### Combiner `String.fromCharCode` avec la concaténation

Vous pouvez combiner `String.fromCharCode` avec la concaténation pour construire des chaînes plus complexes :

```
const str = String.fromCharCode(72, 101) + 'llo';
console.log(str); // Output: Hello
```

Dans cet exemple, les valeurs Unicode pour `H` et `e` sont combinées avec la chaîne `llo` à l'aide de l'opérateur `+`.

## Caractéristiques des chaînes

### Immuabilité

L'immuabilité des chaînes en JavaScript signifie qu'une fois qu'une chaîne est créée, son contenu ne peut plus être modifié. Les opérations telles que la concaténation ou le changement de casse créent de nouvelles chaînes, laissant la chaîne originale inchangée. Ce concept garantit la prévisibilité, simplifie le débogage et s'aligne sur les principes de la programmation fonctionnelle.

La modification directe des caractères d'une chaîne n'est pas autorisée, renforçant l'idée que les chaînes sont immuables. Bien que cette approche offre des avantages tels qu'un comportement de code clair et une facilité de débogage, il est essentiel de prendre en compte les implications potentielles sur l'utilisation de la mémoire :

```
// Création d'une chaîne originale
const originalString = 'Hello World!';

// La concaténation crée une nouvelle chaîne
const newString = originalString + ' Have a great day!';

// Le changement de casse crée une nouvelle chaîne
const upperCaseString = originalString.toUpperCase();

// L'extraction d'une sous-chaîne crée une nouvelle chaîne
const substring = originalString.slice(0, 5);

// Modification directe (qui n'est pas autorisée et entraînera une erreur)
// Décommenter la ligne ci-dessous provoquera une erreur.
// originalString[0] = 'J';

// Affichage des résultats
console.log('Original String:', originalString);
console.log('Concatenated String:', newString);
console.log('Uppercase String:', upperCaseString);
console.log('Substring:', substring);
```

Dans cet exemple, chaque opération (concaténation, changement de casse et extraction de sous-chaîne) crée une nouvelle chaîne sans modifier la chaîne originale. La tentative de modifier directement un caractère dans la chaîne originale entraîne une erreur, soulignant l'immuabilité des chaînes en JavaScript.

De plus, vous avez peut-être remarqué certaines méthodes de chaîne comme `toUpperCase()` et `slice()` dans les exemples ci-dessus. Vous en apprendrez davantage à leur sujet dans les sections suivantes.

### Séquence de caractères

Une séquence de caractères en JavaScript fait référence à une disposition linéaire de caractères individuels qui forment une chaîne. Une séquence de caractères peut inclure des lettres, des chiffres, des symboles et des espaces blancs. Chaque caractère de la séquence possède un index ou une position spécifique, commençant à `0` :

```
const greeting = 'Hello, World!';
```

Dans cet exemple, la chaîne `'Hello, World!'` est une séquence de caractères. Le premier caractère, `H`, est à l'index `0`, le deuxième caractère, `e`, est à l'index `1`, et ainsi de suite. La chaîne entière forme une séquence de caractères dans l'ordre où ils apparaissent.

## Méthodes de manipulation de la casse

### `toUpperCase()`

La méthode `toUpperCase()` transforme tous les caractères d'une chaîne en majuscules, offrant un moyen simple de standardiser la casse d'une chaîne :

```
const text = "Hello, World!";
const uppercased = text.toUpperCase(); // "HELLO, WORLD!"
```

### `toLowerCase()`

À l'inverse, la méthode `toLowerCase()` convertit tous les caractères d'une chaîne en minuscules :

```
const text = "Hello, World!";
const lowercased = text.toLowerCase(); // "hello, world!"
```

## Suppression des espaces blancs avec `trim()`, `trimStart()` et `trimEnd()`

En JavaScript, les chaînes contiennent souvent des espaces blancs au début ou à la fin (espaces, tabulations ou caractères de nouvelle ligne) qui peuvent devoir être supprimés. Les méthodes `trim()`, `trimStart()` et `trimEnd()` offrent des moyens pratiques de réaliser cette suppression d'espaces blancs.

### `trim()`

La méthode `trim()` supprime les espaces blancs aux deux extrémités d'une chaîne et renvoie le résultat :

```
const stringWithWhitespace = '   Hello, World!   ';
const trimmedString = stringWithWhitespace.trim();

console.log(trimmedString); // Output: 'Hello, World!'
```

Dans cet exemple, les espaces blancs au début et à la fin de `stringWithWhitespace` sont supprimés à l'aide de `trim()`.

### `trimStart()`

La méthode `trimStart()` (également connue sous le nom de `trimLeft()`) supprime les espaces blancs au début (start) d'une chaîne :

```
const stringWithLeadingWhitespace = '   Hello, World!';
const trimmedStartString = stringWithLeadingWhitespace.trimStart();

console.log(trimmedStartString); // Output: 'Hello, World!'
```

Ici, `trimStart()` supprime les espaces blancs au début de `stringWithLeadingWhitespace`.

### `trimEnd()`

La méthode `trimEnd()` (également connue sous le nom de `trimRight()`) supprime les espaces blancs à la fin d'une chaîne :

```
const stringWithTrailingWhitespace = 'Hello, World!   ';
const trimmedEndString = stringWithTrailingWhitespace.trimEnd();

console.log(trimmedEndString); // Output: 'Hello, World!'
```

Dans cet exemple, `trimEnd()` élimine les espaces blancs à la fin de `stringWithTrailingWhitespace`.

### Cas d'utilisation :

-   **Saisie utilisateur :** Lors du traitement de la saisie utilisateur, en particulier à partir de formulaires ou de champs de texte, le rognage est courant pour supprimer les espaces blancs accidentels au début ou à la fin.
-   **Nettoyage des données :** Le rognage des espaces blancs est bénéfique lors de la manipulation de jeux de données ou de sources de données externes pour garantir la cohérence des valeurs de chaînes.
-   **Comparaisons :** Le rognage peut être utile lors de la comparaison de chaînes, car les espaces blancs au début ou à la fin pourraient affecter les résultats de la comparaison.

**Note :** Ces méthodes ne modifient pas la chaîne originale. Au lieu de cela, elles renvoient une nouvelle chaîne avec les espaces blancs supprimés. Ceci est cohérent avec le concept d'immuabilité des chaînes JavaScript.

## Recherche dans les chaînes

### `indexOf()` et `lastIndexOf()`

La méthode `indexOf()` est utilisée pour trouver la première occurrence d'une sous-chaîne au sein d'une chaîne. Si la sous-chaîne n'est pas trouvée, elle renvoie `-1` :

```
const sentence = "JavaScript is powerful and versatile.";
const index = sentence.indexOf("is"); // 11
```

La méthode `lastIndexOf()` fonctionne de manière similaire mais commence la recherche à partir de la fin de la chaîne, permettant une recherche inversée.

### La méthode `includes()` pour la présence de sous-chaînes

La méthode `includes()` simplifie la tâche consistant à vérifier si une chaîne contient une sous-chaîne spécifique, en renvoyant une valeur booléenne :

```
const phrase = "To be or not to be";
const containsToBe = phrase.includes("to be"); // true
```

Cette méthode est particulièrement utile pour les vérifications conditionnelles.

### `startsWith()` et `endsWith()`

Pour les scénarios où il est nécessaire de déterminer si une chaîne commence ou se termine par une certaine sous-chaîne, les méthodes `startsWith()` et `endsWith()` sont utiles :

```
const filename = "document.txt";
const isDocument = filename.startsWith("document"); // true
const isTextFile = filename.endsWith(".txt"); // true
```

Ces méthodes sont couramment utilisées pour la validation du type de fichier et d'autres tâches similaires.

### Extraction de sous-chaînes avec slice() et substring() :

Les méthodes `slice()` et `substring()` en JavaScript sont couramment utilisées pour extraire des sous-chaînes à partir de chaînes, mais elles présentent quelques différences de syntaxe et de fonctionnalité.

### Méthode `slice()` :

La méthode `slice()` est un outil polyvalent pour extraire des sous-chaînes basées sur des indices spécifiés. Elle permet l'extraction de sous-chaînes à partir de n'importe quelle position dans la chaîne et prend en charge les indices négatifs. Voici la syntaxe :

```
string.slice(startIndex, endIndex);
```

-   `startIndex` : L'index auquel l'extraction commence.
-   `endIndex` : L'index avant lequel l'extraction se termine (le caractère à cet index n'est pas inclus).

#### Exemple avec des indices positifs et négatifs :

```
let str = "Hello, World!";
let sliced1 = str.slice(7);      // Extracts "World!"
let sliced2 = str.slice(-12, -1); // Extracts "ello, World"
```

Dans le premier exemple, `str.slice(7)` extrait la sous-chaîne commençant à l'index 7 jusqu'à la fin. Dans le second exemple, `str.slice(-12, -1)` extrait la sous-chaîne commençant à 12 positions de la fin jusqu'à 1 position de la fin.

### Méthode `substring()` :

La méthode `substring()` est similaire à `slice()` mais possède une syntaxe différente. Elle extrait une portion spécifiée d'une chaîne mais ne prend pas en charge les indices négatifs. Voici la syntaxe :

```
string.substring(startIndex, endIndex);
```

-   `startIndex` : L'index auquel l'extraction commence.
-   `endIndex` : L'index avant lequel l'extraction se termine (le caractère à cet index n'est pas inclus).

#### Exemple (pas d'indices négatifs) :

```
let str = "Hello, World!";
let subString = str.substring(7, 12); // Extracts "World"
```

Contrairement à `slice()`, la méthode `substring()` n'accepte pas les indices négatifs. Toute tentative d'utiliser des indices négatifs avec `substring()` les traitera comme s'ils étaient 0.

Bien que `slice()` et `substring()` puissent tous deux être utilisés pour l'extraction de sous-chaînes, `slice()` est plus polyvalent car il prend en charge les indices négatifs pour l'extraction à partir de la fin de la chaîne. `substring()`, en revanche, ne prend pas en charge les indices négatifs.

## Modification de chaînes

### Remplacer des sous-chaînes avec `replace()`

La méthode `replace()` est essentielle pour remplacer une sous-chaîne spécifiée par une autre chaîne. Ceci est particulièrement utile pour mettre à jour le contenu de manière dynamique :

```
const message = "Learning Java is fun!";
const updatedMessage = message.replace("Java", "JavaScript");
// "Learning JavaScript is fun!"
```

Cette méthode est couramment utilisée dans les scénarios où le contenu dynamique doit être mis à jour en fonction des interactions de l'utilisateur.

### Diviser des chaînes avec `split()`

Lorsqu'une chaîne doit être divisée en un tableau de sous-chaînes basées sur un séparateur spécifié, vous pouvez utiliser la méthode `split()` :

```
const sentence = "JavaScript is a powerful language.";
const words = sentence.split(" "); // ["JavaScript", "is", "a", "powerful", "language."]
```

Ceci est particulièrement utile lors de la manipulation de mots séparés par des espaces ou de données CSV (Valeurs Séparées par des Virgules).

### Joindre des tableaux en une chaîne avec `join()`

À l'inverse, la méthode `join()` concatène les éléments d'un tableau en une seule chaîne, en utilisant un délimiteur spécifié.

```
const fruits = ["Apple", "Banana", "Orange"];
const joinedString = fruits.join(", "); // "Apple, Banana, Orange"
```

Cette méthode est couramment utilisée lors de la conversion d'un tableau de valeurs en une représentation textuelle lisible.

## Comparaison de chaînes

### Vérifications d'égalité avec `===` et `==`

En JavaScript, la comparaison de chaînes implique l'utilisation des opérateurs `===` et `==`. L'opérateur `===` vérifie à la fois la valeur et le type, garantissant une vérification d'égalité stricte :

```
const numString = "5";
const num = 5;
const isEqualStrict = numString === num; // false
```

D'un autre côté, l'opérateur `==` vérifie l'égalité avec coercition de type :

```
const isEqualLoose = numString == num; // true
```

Il est généralement recommandé d'utiliser `===` pour des comparaisons plus prévisibles et explicites.

### Comparaison de chaînes sensible à la locale

JavaScript fournit la méthode `localeCompare()` pour les comparaisons de chaînes sensibles à la locale. Ceci est particulièrement pertinent lors de la gestion de l'internationalisation et de la localisation :

```
const string1 = "apple";
const string2 = "orange";
const result = string1.localeCompare(string2);
// The result is -1, indicating "apple" comes before "orange" in the dictionary.
```

`localeCompare()` prend en compte les règles linguistiques spécifiques pour le tri et la comparaison.

### Comparer des chaînes en utilisant `localeCompare()`

La méthode `localeCompare()` peut également être utilisée pour comparer des chaînes de manière sensible à la locale, en tenant compte de facteurs tels que les règles linguistiques spécifiques pour le tri.

```
const string1 = "apple";
const string2 = "orange";
const result = string1.localeCompare(string2);
// The result is -1, indicating "apple" comes before "orange" in a dictionary.
```

Cette méthode est utile dans les scénarios où des comparaisons linguistiques précises sont essentielles.

## Expressions régulières et chaînes

Les expressions régulières, souvent appelées regex ou RegExp, constituent un outil puissant pour la recherche de motifs (pattern matching) au sein des chaînes. Elles permettent des opérations de recherche et de manipulation sophistiquées basées sur des motifs spécifiés.

### Utiliser RegExp pour la correspondance et la manipulation de chaînes

Les expressions régulières peuvent être créées à l'aide du constructeur `RegExp` ou exprimées directement entre barres obliques (`/.../`). Elles offrent un large éventail d'options pour la correspondance de motifs, comme la recherche de caractères spécifiques, de groupes ou de plages.

### Méthodes de chaîne avec expressions régulières : `match()`, `search()`, `replace()`

#### `match()`

La méthode `match()` est utilisée pour récupérer les correspondances lorsqu'une chaîne correspond à une expression régulière. Elle renvoie un tableau de correspondances ou `null` si aucune correspondance n'est trouvée :

```
const sentence = "The cat and the hat";
const matches = sentence.match(/at/g); // ["at", "at"]
```

Dans cet exemple, l'expression régulière `/at/g` utilise le drapeau global, `g`, et recherche les occurrences de `at` dans la chaîne.

**Note :** Si le drapeau global (`g`) n'est pas utilisé dans l'expression régulière, `match()` ne renvoie que la première instance d'une correspondance.

#### `search()`

La méthode `search()` renvoie l'index de la première correspondance d'une expression régulière dans une chaîne. Si aucune correspondance n'est trouvée, elle renvoie `-1` :

```
const sentence = "The cat and the hat";
const index = sentence.search(/at/); // 7
```

Dans ce cas, l'expression régulière `/at/` recherche la première occurrence de `at` dans la chaîne.

#### `replace()`

La méthode `replace()` est utilisée pour remplacer les occurrences d'une sous-chaîne ou d'un motif par une autre chaîne. Les expressions régulières améliorent ses capacités, permettant des remplacements plus complexes :

```
const sentence = "The cat and the hat";
const updatedSentence = sentence.replace(/at/g, "og"); // "The cog and the hog"
```

Dans cet exemple, l'expression régulière `/at/g` est utilisée pour remplacer toutes les occurrences de `at` par `og`.

**Note :** Si le drapeau global (`g`) n'est pas utilisé dans l'expression régulière, `replace()` ne remplacera que la première instance d'une sous-chaîne ou d'un motif dans la chaîne originale.

## Unicode et chaînes

### Unicode en bref

Unicode est un système de codage de caractères standardisé qui attribue une valeur numérique unique (point de code) à chaque caractère, symbole ou glyphe dans presque tous les systèmes d'écriture utilisés à travers le monde. Il vise à fournir un codage universel englobant tous les systèmes d'écriture, permettant aux ordinateurs de représenter et de manipuler le texte de manière cohérente.

### Chaînes et Unicode en JavaScript

En JavaScript, les chaînes sont des séquences d'unités de code UTF-16, où chaque unité de code représente une valeur de 16 bits. Cela signifie que JavaScript utilise un sous-ensemble de la plage Unicode complète (qui va au-delà de la plage de 16 bits) pour représenter les caractères.

### Créer des chaînes Unicode

```
const unicodeString = 'Hello, \u{1F60A}'; // Using Unicode escape sequence
console.log(unicodeString); // Output: Hello, 😊
```

Dans l'exemple ci-dessus, la séquence d'échappement Unicode `\u{1F60A}` représente l'émoji visage souriant avec des yeux rieurs. JavaScript interprète cette séquence d'échappement et affiche le caractère Unicode correspondant.

### Points de code Unicode

JavaScript fournit des méthodes pour travailler directement avec les points de code Unicode. La méthode `codePointAt()` renvoie le point de code Unicode à un index spécifique dans une chaîne :

```
const greeting = 'Hello, World!';
const codePoint = greeting.codePointAt(7);
console.log(codePoint); // Output: 87 (the Unicode code point for 'W')
```

### Itération sur les points de code

La boucle `for...of` peut être utilisée pour itérer sur les caractères réels d'une chaîne, en tenant compte des paires de substitution pour les caractères situés en dehors du Plan Multilingue de Base (BMP) :

```
const astralString = '𝒜B'; // String with characters outside the BMP
for (let char of astralString) {
  console.log(char); // Output: 𝒜, B
}
```

Cette boucle itère correctement sur les deux caractères de la chaîne, même si `𝒜` est en dehors du BMP.

### Cas d'utilisation

-   **Support multilingue :** Unicode permet à JavaScript de gérer du texte dans diverses langues et systèmes d'écriture, permettant la création d'applications multilingues.
-   **Émojis et caractères spéciaux :** Unicode fournit un moyen standardisé de représenter les émojis, les symboles spéciaux et les caractères au-delà de l'alphabet latin de base.
-   **Échange de données :** Unicode est crucial pour l'échange de données entre systèmes et langages, garantissant une représentation et une interprétation cohérentes du texte.

Comprendre Unicode est essentiel pour travailler avec divers ensembles de caractères et de symboles dans les chaînes JavaScript, en particulier dans un environnement de programmation mondialisé et multilingue.

## Pièges courants avec les chaînes

### Coercition entre chaîne et nombre

Un piège courant est la coercition involontaire entre les chaînes et les nombres. JavaScript peut effectuer une conversion de type implicite, entraînant un comportement inattendu :

```
const num = 5;
const str = '10';

const result = num + str;
console.log(result); // Output: 510 (not 15!)
```

Pour éviter cela, assurez-vous de convertir explicitement les types si nécessaire :

```
const num = 5;
const str = '10';

const result = num + parseInt(str);
console.log(result); // Output: 15
```

### Comportement inattendu avec les espaces blancs

Les caractères d'espaces blancs, tels que les espaces et les tabulations, peuvent entraîner des résultats inattendus s'ils ne sont pas gérés correctement. Par exemple :

```
const word1 = 'Hello';
const word2 = ' World';

const result = word1 + word2;
console.log(result); // Output: Hello World (without a space in between)
```

Pour résoudre ce problème, rognez les espaces blancs à l'aide de la méthode `trim` :

```
const word1 = 'Hello';
const word2 = ' World';

const result = word1.trim() + word2.trim();
console.log(result); // Output: Hello World
```

### Gérer les caractères spéciaux

Les caractères spéciaux, comme les guillemets ou les barres obliques inverses, peuvent causer des problèmes lorsqu'ils sont inclus dans des chaînes :

```
const message = 'He said, 'JavaScript is powerful!'';
```

Pour gérer cela, échappez les caractères spéciaux à l'aide de barres obliques inverses :

```
const message = 'He said, \'JavaScript is powerful!\'';
```

## Études de cas et exemples

Explorons un scénario réel où la manipulation de chaînes est essentielle.

### Validation des entrées utilisateur

Supposons que vous construisiez un formulaire qui oblige un utilisateur à saisir son adresse e-mail. Pour valider la saisie, vous pouvez utiliser des méthodes de chaîne :

```
function validateEmail(email) {
  // Check if the email contains the @ symbol
  if (!email.includes('@')) {
    return false;
  }

  // Check if the email ends with a valid domain (e.g., .com, .org)
  const domain = email.split('@')[1];
  const validDomains = ['com', 'org', 'net'];
  if (!validDomains.includes(domain.split('.')[1])) {
    return false;
  }

  return true;
}

const userEmail = 'user@example.com';
if (validateEmail(userEmail)) {
  console.log('Email is valid!');
} else {
  console.log('Invalid email format.');
}
```

### Formatage de noms

Supposons que vous ayez une liste de noms au format "Prénom Nom" et que vous souhaitiez les afficher sous la forme "Nom, Prénom". Vous pouvez y parvenir grâce à la manipulation de chaînes :

```
function formatNames(names) {
  return names.map((name) => {
    const [first, last] = name.split(' ');
    return `${last}, ${first}`;
  });
}

const originalNames = ['John Doe', 'Jane Smith', 'Bob Johnson'];
const formattedNames = formatNames(originalNames);
console.log(formattedNames);
// Output: ['Doe, John', 'Smith, Jane', 'Johnson, Bob']
```

## Conclusion

Dans cet article, nous avons couvert les bases du travail avec les chaînes de caractères en JavaScript. Nous avons exploré les opérations fondamentales telles que la concaténation et la recherche de la longueur d'une chaîne. De plus, nous avons approfondi diverses méthodes de chaîne pour changer la casse, extraire des sous-chaînes, trouver des sous-chaînes, remplacer des sous-chaînes et diviser des chaînes.

Maîtriser la manipulation de chaînes nécessite de la pratique et de l'expérimentation. Au fur et à mesure que vous travaillerez sur davantage de projets, vous rencontrerez divers scénarios exigeant des solutions créatives impliquant des chaînes. N'hésitez pas à expérimenter différentes méthodes et approches pour améliorer vos compétences.

Une solide compréhension des méthodes de chaîne est cruciale pour écrire un code JavaScript propre, efficace et sans bogue. Alors que vous poursuivez votre parcours de programmation, rappelez-vous que les chaînes sont un élément fondamental de nombreuses applications, et la capacité à les manipuler efficacement contribuera de manière significative à votre succès en tant que développeur JavaScript. Continuez à coder, continuez à apprendre et profitez du monde de JavaScript !

[1]: #heading-que-sont-les-chaines-de-caracteres-en-javascript-
[2]: #heading-operations-de-base-sur-les-chaines
[3]: #heading-guillemets-simples-et-doubles
[4]: #heading-gabarits-de-chaines-template-literals
[5]: #heading-utilisation-de-base
[6]: #heading-chaines-multilignes
[7]: #heading-evaluation-d-expressions
[8]: #heading-gabarits-etiquetes-tagged-templates
[9]: #heading-cas-d-utilisation
[10]: #heading-le-constructeur-string
[11]: #heading-utiliser-le-constructeur-string
[12]: #heading-objets-string-vs-primitives-string
[13]: #heading-convertir-des-objets-string-en-primitives
[14]: #heading-cas-d-utilisation-rares
[15]: #heading-la-methode-string-fromcharcode
[16]: #heading-utilisation-de-base
[17]: #heading-creer-des-chaines-a-partir-de-valeurs-unicode
[18]: #heading-cas-d-utilisation
[19]: #heading-concatenation
[20]: #heading-utiliser-l-operateur-plus
[21]: #heading-utiliser-la-methode-concat
[22]: #heading-concatener-des-variables-et-des-chaines
[23]: #heading-combiner-string-fromcharcode-avec-la-concatenation
[24]: #heading-caracteristiques-des-chaines
[25]: #heading-immuabilite
[26]: #heading-sequence-de-caracteres
[27]: #heading-methodes-de-manipulation-de-la-casse
[28]: #heading-touppercase
[29]: #heading-tolowercase
[30]: #heading-suppression-des-espaces-blancs-avec-trim-trimstart-et-trimend
[31]: #heading-trim
[32]: #heading-trimstart
[33]: https://www.freecodecamp.org/news/p/e2ef5e41-04ae-40a6-b5a5-8915616f1bd3/trimend-
[34]: #heading-cas-d-utilisation
[35]: #heading-recherche-dans-les-chaines
[36]: #heading-indexof-et-lastindexof
[37]: #heading-methode-includes-pour-la-presence-de-sous-chaines
[38]: #heading-methodes-startswith-et-endswith
[39]: #heading-extraction-de-sous-chaines-avec-slice-et-substring-
[40]: #slice-
[41]: #substring-
[42]: #heading-modification-de-chaines
[43]: #heading-remplacer-des-sous-chaines-avec-la-methode-replace
[44]: #heading-diviser-des-chaines-avec-split
[45]: #heading-joindre-des-tableaux-en-une-chaine-avec-join
[46]: #heading-comparaison-de-chaines
[47]: #heading-verifications-d-egalite-avec-strict-et-abstrait
[48]: #heading-comparaison-de-chaines-sensible-a-la-locale-avec-localecompare
[49]: #heading-comparer-des-chaines-en-utilisant-localecompare
[50]: #heading-expressions-regulieres-et-chaines
[51]: #heading-utiliser-regexp-pour-la-correspondance-et-la-manipulation-de-chaines
[52]: #heading-methodes-de-chaine-avec-expressions-regulieres-match-search-replace
[53]: #heading-unicode-et-chaines
[54]: #heading-chaines-et-unicode-en-javascript
[55]: #heading-creer-des-chaines-unicode
[56]: #heading-points-de-code-unicode
[57]: #heading-iteration-sur-les-points-de-code
[58]: #heading-pieges-courants-avec-les-chaines
[59]: #heading-coercition-entre-chaine-et-nombre
[60]: #heading-comportement-inattendu-avec-les-espaces-blancs
[61]: #heading-gerer-les-caracteres-speciaux
[62]: #heading-etudes-de-cas-et-exemples
[63]: #heading-validation-des-entrees-utilisateur
[64]: #heading-formatage-de-noms
[65]: #heading-conclusion