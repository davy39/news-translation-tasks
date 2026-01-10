---
title: Tutoriel JavaScript sur les chaînes de caractères – Méthodes de chaîne en JS
subtitle: ''
author: Dario Di Cillo
co_authors: []
series: null
date: '2023-03-10T19:14:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-tutorial-string-methods-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/belen-garrido-n642zkjBAEY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript sur les chaînes de caractères – Méthodes de chaîne
  en JS
seo_desc: "A string is a sequence of characters intended to represent text. Strings\
  \ can contain any kind of character, like letters, numbers, or special characters.\
  \ \nThey are a very useful data type and you will be probably working with them\
  \ frequently. So it's..."
---

Une chaîne de caractères est une séquence de caractères destinée à représenter du texte. Les chaînes de caractères peuvent contenir tout type de caractère, comme des lettres, des chiffres ou des caractères spéciaux. 

Elles sont un type de données très utile et vous travaillerez probablement fréquemment avec elles. Il est donc important de savoir comment les manipuler efficacement.

Dans cet article, vous apprendrez :

* Les bases des chaînes de caractères en JavaScript
* Les méthodes de chaîne de caractères courantes en JavaScript

Commençons.

## Les bases des chaînes de caractères en JavaScript

Voici une définition simple d'une [chaîne de caractères](https://www.freecodecamp.org/news/what-is-a-string-in-javascript/) :

> En JavaScript, une chaîne de caractères est un type de données représentant une séquence de caractères qui peut consister en des lettres, des chiffres, des symboles, des mots ou des phrases.

Les chaînes de caractères sont utilisées pour représenter du texte. Donc, essentiellement, tout ce qui est un [caractère Unicode](https://unicode.org/charts/).

Procédez et voyez quelque chose de pratique.

### Comment créer des chaînes de caractères en JavaScript

En JavaScript, vous pouvez créer des chaînes de caractères en enveloppant le texte dans des guillemets simples (`'`), des guillemets doubles (`"`) ou des backticks (```).

```js
// Une chaîne de caractères créée en utilisant des guillemets simples
let string1 = 'Je suis une chaîne de caractères très cool ! 😎';

// Une chaîne de caractères créée en utilisant des guillemets doubles
let string2 = "Je suis une chaîne de caractères très cool ! 😎";

// Une chaîne de caractères créée en utilisant des backticks, également connue sous le nom de template literal
let string3 = `Je suis une chaîne de caractères très cool ! 😎`;
```

Les chaînes de caractères créées de cette manière, comme dans l'exemple ci-dessus, sont traitées de manière égale. Vous pouvez facilement les comparer pour le prouver :

```js
string1 === string2; // true

string1 === string3; // true

string2 === string3; // true
```

Les chaînes de caractères créées en utilisant des backticks sont également connues sous le nom de _template literals_ et possèdent des fonctionnalités spéciales que nous discuterons dans un instant.

Une chaîne de caractères créée en utilisant des guillemets simples, des guillemets doubles ou des backticks est générée comme une **valeur primitive**, similaire aux nombres et aux valeurs booléennes. Les données primitives sont **immuables**, ce qui signifie qu'elles ne peuvent pas être changées. De plus, elles n'ont aucune méthode ou propriété.

Pour votre information, il existe une autre façon de créer des chaînes de caractères en JavaScript, qui est via le constructeur [`String()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String). Le constructeur `String()` génère une chaîne de caractères comme un **objet** (quand il est appelé avec `new`). Si appelé comme une fonction (`str2` dans l'exemple ci-dessous), la valeur est [coercée](https://www.freecodecamp.org/news/coercion-and-type-conversion-in-javascript/) en une chaîne de caractères primitive.

```js
let str1 = new String('Quoi suis-je ?');
typeof str1; // 'object'

let str2 = String('Quoi suis-je ?');
typeof str2; // 'string'

let str3 = "Quoi suis-je ?";
typeof str3; // 'string'

str1 === str2; // false
str1 === str3; // false
str2 === str3; // true
```

L'opérateur `typeof` retourne une chaîne de caractères indiquant le type de données de l'opérande. Cette fois, bien que `str1` et `str2` puissent sembler égaux, leur comparaison retourne `false`, puisque ce sont des valeurs complètement différentes.

Note : À partir de maintenant, je discuterai exclusivement des chaînes de caractères primitives.

## Manipulation de base des chaînes de caractères en JavaScript

### Indexation des chaînes de caractères

Vous pouvez accéder à chaque caractère à l'intérieur d'une chaîne de caractères par son index numérique – en commençant par zéro – en utilisant la notation entre crochets :

```js
let str = 'larch';
str[0]; // 'l'
str[1]; // 'a'
str[2]; // 'r'
str[3]; // 'c'
str[4]; // 'h'
```

De plus, vous pouvez utiliser la méthode `charAt()` pour obtenir un caractère spécifique à l'intérieur de la chaîne de caractères :

```js
str.charAt(0); // 'l'
```

Bien que vous puissiez utiliser la notation entre crochets pour changer les données _non-primitives_, par exemple, les tableaux :

```js
let arr = ['birch', 'larch', 'oak'];
typeof arr; // 'object'
arr[2] = 'scots pine';
console.log(arr); // ['birch', 'larch', 'scots pine']
```

Vous **ne pouvez pas muter** une chaîne de caractères, puisque c'est une valeur _primitive_ :

```js
let str = 'larch';
typeof str; // 'string'
str[0] = 'm'; // Cela pourrait lancer une erreur si vous êtes en mode strict
console.log(str); // 'larch'
```

La valeur de notre variable `str` est toujours `'larch'` et vous ne pouvez rien faire pour la muter. Cette particularité des valeurs primitives ne signifie pas que vous ne pouvez pas faire en sorte que la variable `str` pointe vers une autre valeur par réaffectation :

```js
let str = 'larch';
str = 'march'; // Réaffectation de str à une autre valeur
console.log(str); // 'march'

```

Juste une note – certains des exemples suivants utiliseront des lignes de ces chansons :

* _Always Look on the Bright Side of Life_, paroles de Eric Idle
* _The Trek_ par Primus
* _The Trees_ par Rush

### La propriété `length`

Vous obtenez le nombre de caractères contenus dans une chaîne de caractères en utilisant la propriété `length` :

```js
let sentence = 'Always look on the bright side of life';
sentence.length; // 38
```

La propriété `length` retourne le nombre de caractères dont la chaîne de caractères est composée, y compris les espaces blancs. Donc le dernier caractère de notre phrase aura l'index 37 (la valeur retournée par length -1, parce que l'indexation commence à 0).

### Concaténation de chaînes de caractères

Vous pouvez concaténer (ou joindre) deux ou plusieurs chaînes de caractères en utilisant l'opérateur de concaténation, `+`. Consultez l'exemple suivant :

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
let c = a + ' ' + b;
console.log(c); // 'When candles are out, all cats are grey.'
```

Notez que j'ai ajouté une chaîne de caractères supplémentaire entre `a` et `b` pour donner à la phrase finale l'espacement correct.

Vous pouvez faire une chose similaire en utilisant l'opérateur d'addition et d'affectation `+=` :

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
console.log(a += ' '); // 'When candles are out, '
console.log(a += b); // 'When candles are out, all cats are grey.'
```

En faisant cela, la variable `a` est assignée à sa valeur plus la valeur du côté droit de l'opérateur (`+=`). Maintenant, `a` contient toute la phrase, tandis que dans l'exemple précédent la phrase complète était stockée dans une autre variable, `c`.

Si vous essayez de concaténer un nombre à une chaîne de caractères, ce nombre sera coercé en une valeur de chaîne de caractères. Par exemple :

```js
console.log('The ' + 3 + ' Musketeers'); // 'The 3 Musketeers'
```

### Comparaison de chaînes de caractères

Vous pouvez comparer des chaînes de caractères en fonction de leur ordre alphabétique et de leur longueur en utilisant des opérateurs de comparaison arithmétique. La valeur retournée est un booléen. 

Dans l'exemple ci-dessous, nous comparons deux chaînes de caractères selon leur ordre alphabétique :

```js
'Berry' < 'Copper'; // true
// parce que 'B' vient avant 'C'

'Berry' < 'Bingo'; // true
// parce que les premiers caractères sont les mêmes et 'e' vient avant 'i'

'berry' < 'Copper'; // false
// parce que la comparaison est sensible à la casse et les lettres majuscules viennent en premier
```

La comparaison est effectuée lettre par lettre, en commençant par la première. Et elle est en fait basée sur l'ordre Unicode. C'est pourquoi _C_ vient avant _b_ – les lettres majuscules sont placées avant les lettres minuscules dans la table Unicode.

Pour la même raison, `'$' < '&'` évalue `true` – _$_ vient avant _&_ dans la table Unicode.

Après la comparaison lettre par lettre, si chaque caractère équivaut à son homologue dans l'autre chaîne de caractères, et que les chaînes de caractères ont la même longueur, elles sont égales. Sinon, la chaîne de caractères la plus longue est la plus grande. 

Dans l'exemple ci-dessous, `quote` manque le point d'exclamation final, donc `quoteMark` est plus grand :

```js
let quote = 'All generalizations are dangerous, even this one';
let quoteMark = 'All generalizations are dangerous, even this one!';
quote < quoteMark; // true
```

Si vous devez comparer les longueurs de deux chaînes de caractères, vous utilisez simplement la propriété length :

```js
quote.length < quoteMark.length; // true
```

### Template literals

Auparavant, nous avons dit que les template literals (chaînes de caractères créées avec des backticks, ```) ont quelques fonctionnalités spéciales. L'une est la capacité d'afficher le texte sur plusieurs lignes, facile comme bonjour.

```js
const chorus = `Ne perdons pas courage, camarades
C'est par-dessus cette colline
Le paradis est juste par-dessus cette colline`;

console.log(chorus);
// Ne perdons pas courage, camarades
// C'est par-dessus cette colline
// Le paradis est juste par-dessus cette colline
```

Le texte affiché reflète l'espacement utilisé pour écrire la chaîne de caractères. Cela n'aurait pas été le cas pour d'autres chaînes de caractères littérales, qui nécessitent l'utilisation d'un caractère de nouvelle ligne, `\n`, afin d'avoir le texte arrangé de manière multiligne. Par exemple :

```js
const verse = "Il y a de l'agitation dans la forêt\nDes problèmes avec les arbres";

console.log(verse);
// Il y a de l'agitation dans la forêt
// Des problèmes avec les arbres
```

Si vous voulez inclure une variable à l'intérieur d'une chaîne de caractères créée avec des guillemets simples ou doubles, vous devez utiliser la concaténation, comme vu précédemment.

```js
const dog1 = 'Bach';
const dog2 = 'Bingo';

console.log('Mes deux chiens s'appellent ' + dog1 + ' et ' + dog2 + '.');
// Mes deux chiens s'appellent Bach et Bingo.
```

Mais les template literals fournissent une fonctionnalité appelée **[interpolation de chaîne de caractères](https://www.freecodecamp.org/news/javascript-string-format-how-to-use-string-interpolation-in-js/)**, qui simplifie la lisibilité et rend le code plus fluide. 

Voici l'exemple précédent réécrit avec des template literals :

```js
const dog1 = 'Bach';
const dog2 = 'Bingo';

console.log(`Mes deux chiens s'appellent ${dog1} et ${dog2}.`);
// Mes deux chiens s'appellent Bach et Bingo.
```

En bref, vous assemblez la chaîne de caractères en substituant le contenu des placeholders, `${}`, qui est ajouté au texte.

Dans l'exemple ci-dessus, chaque placeholder contient une variable, mais les placeholders peuvent contenir n'importe quelle expression dont la valeur sera convertie en une chaîne de caractères, construisant la chaîne de caractères finale.

## Méthodes de chaîne de caractères courantes en JavaScript

Comme nous l'avons dit précédemment, les données primitives n'ont pas de méthodes et de propriétés. Hé, qu'en est-il de la propriété `length` que nous avons utilisée avant ? Et de la méthode `charAt()` ? Et qu'en est-il de cette section ?!

Les données primitives n'ont effectivement pas de méthodes ou de propriétés. Mais lorsque vous appelez une méthode sur une chaîne de caractères, ou accédez à une propriété, JavaScript génère un objet wrapper sous le capot. En fin de compte, les méthodes et propriétés effectuent leur travail sur cet objet wrapper. Après l'utilisation, l'objet wrapper est supprimé.

Donc, il s'avère que nous avons quelque chose à discuter dans cette section. Voici quelques-unes des méthodes de chaîne de caractères les plus courantes en JavaScript avec des exemples.

### La méthode `concat()`

L'effet de la méthode `concat()` est très similaire à l'utilisation des opérateurs `+` et `+=`. Elle concatène une ou plusieurs chaînes de caractères passées en arguments à la chaîne de caractères sur laquelle la méthode est appelée, retournant la chaîne de caractères concaténée.

Réécrivons l'exemple de la section [concaténation](#heading-concatenation) :

```js
let a = 'When candles are out,';
let b = 'all cats are grey.';
let c = a.concat(' ', b);
console.log(c); // 'When candles are out, all cats are grey.'
```

### Les méthodes `toLowerCase()` et `toUpperCase()`

Parfois, vous pourriez avoir besoin de manipuler la casse des lettres de chaînes de caractères spécifiques pour les comparer correctement, stocker des entrées avec une certaine uniformité, ou pour d'autres raisons.

Comme leurs noms peuvent le suggérer, `toLowerCase()` et `toUpperCase()` convertissent une chaîne de caractères en lettres minuscules et majuscules, respectivement. Ces méthodes ne changent pas la chaîne de caractères originale.

```js
let sentence = 'Always look on the bright side of life';

console.log(sentence.toLowerCase());
// always look on the bright side of life

console.log(sentence.toUpperCase());
// ALWAYS LOOK ON THE BRIGHT SIDE OF LIFE
```

### La méthode `includes()`

La méthode `includes()` vérifie si une chaîne de caractères spécifiée, passée en argument, est présente à l'intérieur d'une autre chaîne de caractères. La recherche est sensible à la casse et la valeur retournée est un booléen.

De plus, vous pouvez spécifier un deuxième argument indiquant l'index auquel commencer la recherche de la chaîne de caractères spécifiée.

```js
let sentence = 'Always look on the bright side of life';
sentence.includes('look up'); // false 
sentence.includes('look on'); // true
sentence.includes('look on', 8); // false
```

### Les méthodes `indexOf()`

La méthode `indexOf()` recherche une sous-chaîne et retourne la première occurrence de la sous-chaîne à l'intérieur de la chaîne de caractères appelante. Elle prend un paramètre optionnel, indiquant un index spécifique pour commencer la recherche. Par exemple :

```js
let sentence = 'Always look on the bright side of life';

sentence.indexOf('l'); // 1
sentence.indexOf('l', 2); // 7
sentence.indexOf('l', 8); // 34
sentence.indexOf('L'); // -1
```

`indexOf()` retourne l'index de la première occurrence de la sous-chaîne. Si la sous-chaîne n'est pas trouvée, elle retourne `-1`. Gardez à l'esprit que la recherche est sensible à la casse. C'est pourquoi `sentence.indexOf('L')` dans l'exemple ci-dessus retourne `-1`.

### Les méthodes `startsWith()` et `endsWith()`

La méthode `startsWith()` vérifie si une chaîne de caractères commence par une séquence spécifique de caractères et retourne une valeur booléenne. La recherche est sensible à la casse.

La méthode prend un argument optionnel indiquant la position à laquelle commencer la recherche de la chaîne de caractères spécifiée.

```js
let dish = 'Lemon curry';
dish.startsWith('Lem'); // true
dish.startsWith('lem'); // false
dish.toLowerCase().startsWith('lem'); // true
dish.startsWith('cu'); // false
dish.startsWith('cu', 6); // true
```

De même, la méthode `endsWith()` vérifie si une chaîne de caractères se termine par une séquence spécifique de caractères, retournant une valeur booléenne. Dans ce cas également, la recherche est sensible à la casse.

L'argument optionnel indique la position de fin attendue de la sous-chaîne spécifiée (l'index du caractère final attendu + 1).

```js
let dish = 'Lemon curry';
dish.endsWith('ry'); // true
dish.endsWith('on', 5); // true
```

### Les méthodes `slice()` et `substring()`

Les méthodes `slice()` et `substring()` extraient une portion d'une chaîne de caractères, la retournant comme une nouvelle chaîne de caractères. Elles ne changent pas le contenu de la chaîne de caractères originale.

Le premier argument passé à chaque méthode est l'index du premier caractère à inclure dans la chaîne de caractères à extraire. Le deuxième argument est l'index du premier caractère à exclure. Par exemple :

```js
let sentence = 'Always look on the bright side of life';

sentence.slice(7); // 'look on the bright side of life'
sentence.substring(7); // 'look on the bright side of life'
sentence.slice(0, 6); // 'Always'
sentence.substring(0, 6); // 'Always'
```

Ces deux méthodes sont presque identiques, sauf pour quelques différences. L'une d'elles est que si le premier index passé à `substring()` est supérieur au deuxième index, les deux arguments sont échangés afin qu'une chaîne de caractères soit toujours retournée. Dans le même scénario, la méthode `slice()` retourne une chaîne de caractères vide à la place :

```js
let sentence = 'Always look on the bright side of life';

sentence.substring(11, 7); // 'look'
sentence.slice(11, 7); // ''
```

### La méthode `split()`

La méthode `split()` prend un argument séparateur et divise une chaîne de caractères, selon l'occurrence du caractère séparateur à l'intérieur de la chaîne de caractères. Ensuite, elle retourne un tableau de chaînes de caractères.

Elle prend également un argument optionnel, indiquant le nombre maximum d'éléments à mettre à l'intérieur du tableau. Par exemple :

```js
let sentence = 'Always look on the bright side of life';

sentence.split(' '); // ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
sentence.split(' ', 5); // ['Always', 'look', 'on', 'the', 'bright']
```

### La méthode `match()`

La méthode `match()` recherche un motif spécifique – passé sous forme d'expression régulière – à l'intérieur d'une chaîne de caractères, et retourne un tableau contenant les résultats correspondants. Par exemple :

```js
const tongueTwister = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
const regex1 = /(w|c)o*(ul)?d/g;
const regex2 = /wool/g;
tongueTwister.match(regex1);
// ['wood', 'would', 'wood', 'wood', 'could', 'wood']
tongueTwister.match(regex2);
// null

```

Si vous avez seulement besoin de savoir si un motif est présent ou non à l'intérieur d'une chaîne de caractères, vous devriez utiliser `test()`.

### La méthode `test()`

La méthode `test()` recherche un motif spécifique – passé sous forme d'expression régulière – à l'intérieur d'une chaîne de caractères, et retourne un booléen. La syntaxe est inversée par rapport à `match()`. 

En considérant l'exemple précédent, l'utilisation de la méthode `test()` ressemblerait à ceci :

```js
const tongueTwister = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
const regex1 = /(w|c)o*(ul)?d/g;
const regex2 = /wool/g;
regex1.test(tongueTwister); // true
regex2.test(tongueTwister); // false

```

## Conclusion

Une chaîne de caractères est une séquence de caractères qui représente du texte. En JavaScript, les chaînes de caractères sont des données primitives. Vous pouvez les créer en enveloppant le texte dans des guillemets simples, des guillemets doubles ou des backticks.

Les template literals vous permettent d'écrire un code plus propre grâce à l'interpolation de chaînes de caractères, et lorsque vous avez besoin de chaînes de caractères multilignes.

Les chaînes de caractères sont partout, donc vous devrez savoir comment les manipuler efficacement. Dans ce tutoriel, vous avez appris les méthodes de chaîne de caractères les plus courantes que vous utiliserez pour travailler avec les chaînes de caractères. Mais il y en a beaucoup d'autres à découvrir !

Bonne apprentissage :)