---
title: JavaScript Split – Comment diviser une chaîne en un tableau en JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-06-16T21:19:08.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-how-to-split-a-string-into-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/freeCodeCamp-Cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Split – Comment diviser une chaîne en un tableau en JS
seo_desc: "In general, a string represents a sequence of characters in a programming\
  \ language. \nLet's look at an example of a string created using a sequence of characters,\
  \ \"Yes, You Can DO It!\". In JavaScript, we can create a string in a couple of\
  \ ways:\n\nUsing..."
---

En général, une `string` représente une séquence de caractères dans un langage de programmation. 

Prenons un exemple de chaîne créée à partir d'une séquence de caractères, "Yes, You Can DO It!". En JavaScript, nous pouvons créer une chaîne de plusieurs manières :

* En utilisant le littéral de chaîne comme primitif

```js
const msg = "Yes, You Can DO It!";
```

* En utilisant le constructeur `String()` comme objet

```js
const msg = new String("Yes, You Can DO It!");
```

Un fait intéressant concernant les chaînes en JavaScript est que nous pouvons accéder aux caractères d'une chaîne en utilisant leur index. L'index du premier caractère est 0, et il s'incrémente de 1. Ainsi, nous pouvons accéder à chacun des caractères d'une chaîne comme ceci :

```js
let str = "Yes, You Can Do It!";

console.log(str[0]); // Y
console.log(str[1]); // e
console.log(str[2]); // s
console.log(str[3]); // ,

console.log(str[10]); // a
```

L'image ci-dessous représente la même chose :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/split.png)
_Accéder aux caractères d'une chaîne par l'index_

Outre sa capacité à accéder aux caractères d'une chaîne par leurs index, JavaScript fournit également de nombreuses méthodes utilitaires pour accéder aux caractères, extraire une partie d'une chaîne et la manipuler. 

Dans cet article, nous allons apprendre une méthode de chaîne pratique appelée `split()`. J'espère que vous apprécierez sa lecture.

# La méthode split() en JavaScript

La méthode `split()` divise une chaîne en deux ou plusieurs sous-chaînes en fonction d'un `séparateur` (ou diviseur). Le séparateur peut être un caractère unique, une autre chaîne ou une expression régulière. 

Après avoir divisé la chaîne en plusieurs sous-chaînes, la méthode `split()` les place dans un tableau et le retourne. Elle ne modifie pas la chaîne originale.

Comprenons comment cela fonctionne avec un exemple. Voici une chaîne créée à l'aide de littéraux de chaîne :

```js
let message = 'I am a Happy Go lucky Guy';

```

Nous pouvons appeler la méthode `split()` sur la chaîne `message`. Divisons la chaîne en fonction du caractère espace (`' '`). Ici, le caractère espace agit comme un séparateur ou diviseur.

```js
// Diviser en utilisant un caractère espace
let arr = message.split(' ');

// Le tableau
console.log(arr); // ["I", "am", "a", "Happy", "Go", "lucky", "Guy"]


// Accéder à chacun des éléments du tableau.
console.log(arr[0]); // "I"
console.log(arr[1]); // "am"
console.log(arr[2]); // "a"
console.log(arr[3]); // "Happy"
console.log(arr[4]); // "Go",
console.log(arr[5]); // "lucky"
console.log(arr[6]); // "Guy"


```

Le but principal de la méthode `split()` est d'obtenir les parties qui vous intéressent dans une chaîne pour les utiliser dans d'autres cas d'utilisation.

## Comment diviser une chaîne par chaque caractère

Vous pouvez diviser une chaîne par chaque caractère en utilisant une chaîne vide ('') comme séparateur. Dans l'exemple ci-dessous, nous divisons le même message en utilisant une chaîne vide. Le résultat de la division sera un tableau contenant tous les caractères de la chaîne du message.

```js
console.log(message.split('')); // ["I", " ", "a", "m", " ", "a", " ", "H", "a", "p", "p", "y", " ", "G", "o", " ", "l", "u", "c", "k", "y", " ", "G", "u", "y"]
```

> F4A1 Veuillez noter que la division d'une chaîne vide ('') en utilisant une chaîne vide comme séparateur retourne un tableau vide. Vous pourriez obtenir cette question lors de vos prochains entretiens d'embauche !

```js
''.split(''); // retourne []
```

## Comment diviser une chaîne en un seul tableau

Vous pouvez invoquer la méthode `split()` sur une chaîne sans séparateur/diviseur. Cela signifie simplement que la méthode `split()` n'a aucun argument qui lui est passé. 

Lorsque vous invoquez la méthode `split()` sur une chaîne sans séparateur, elle retourne un tableau contenant la chaîne entière.

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split()); // retourne ["I am a Happy Go lucky Guy"]
```

> F4A1 Notez à nouveau que l'appel de la méthode `split()` sur une chaîne vide ('') sans séparateur retournera un tableau avec une chaîne vide. Elle ne retourne pas un tableau vide.

Voici deux exemples pour que vous puissiez voir la différence :

```js
// Retourne un tableau vide
''.split(''); // retourne []

// Retourne un tableau avec une chaîne vide
''.split() // retourne [""]
```

## Comment diviser une chaîne en utilisant un caractère non correspondant

Habituellement, nous utilisons un séparateur qui fait partie de la chaîne que nous essayons de diviser. Il peut y avoir des cas où vous avez passé un séparateur qui ne fait pas partie de la chaîne ou qui ne correspond à aucune partie de celle-ci. Dans ce cas, la méthode `split()` retourne un tableau avec la chaîne entière comme élément.

Dans l'exemple ci-dessous, la chaîne de message ne contient pas de caractère virgule (,). Essayons de diviser la chaîne en utilisant la virgule (,) comme séparateur.

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split(',')); // ["I am a Happy Go lucky Guy"]
```

> F4A1 Vous devez être conscient de cela, car cela pourrait vous aider à déboguer un problème dû à une erreur triviale comme le passage du mauvais séparateur dans la méthode `split()`.

# Comment diviser avec une limite

Si vous pensiez que la méthode `split()` ne prend que le séparateur comme paramètre optionnel, laissez-moi vous dire qu'il y en a un autre. Vous pouvez également passer la `limite` comme paramètre optionnel à la méthode `split()`.

```js
string.split(séparateur, limite);
```

Comme l'indique le nom, le paramètre `limite` limite le nombre de divisions. Cela signifie que le tableau résultant ne contiendra que le nombre d'éléments spécifié par le paramètre de limite.

Dans l'exemple ci-dessous, nous divisons une chaîne en utilisant un espace (' ') comme séparateur. Nous passons également le nombre `4` comme limite. La méthode `split()` retourne un tableau avec seulement quatre éléments, en ignorant le reste.

```js
let message = 'I am a Happy Go lucky Guy';
console.log(message.split(' ', 4)); // ["I", "am", "a", "Happy"] 
```

# Comment diviser en utilisant Regex

Nous pouvons également passer une expression régulière (regex) comme séparateur/diviseur à la méthode `split()`. Considérons cette chaîne à diviser :

```js
let message = 'The sky is blue. Grass is green! Do you know the color of the Cloud?';
```

Divisons cette chaîne au niveau du point (.), du point d'exclamation (!) et du point d'interrogation (?). Nous pouvons écrire une regex qui identifie lorsque ces caractères se produisent. Ensuite, nous passons la regex à la méthode `split()` et l'invoquons sur la chaîne ci-dessus.

```js
let sentences = message.split(/[.,!,?]/);
console.log(sentences);
```

La sortie ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-102.png)
_Division en utilisant une expression régulière_

Vous pouvez utiliser le paramètre `limite` pour limiter la sortie aux trois premiers éléments seulement, comme ceci :

```js
sentences = message.split(/[.,!,?]/, 3);
console.log(sentences);
```

La sortie ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-103.png)
_Division en utilisant une expression régulière et une valeur de limite_

> F4A1 Si vous souhaitez capturer les caractères utilisés dans les expressions régulières dans le tableau de sortie, vous devez modifier légèrement la regex. Utilisez des parenthèses pour capturer les caractères correspondants. La regex mise à jour sera `/([.,!,?])/`.

# Comment remplacer des caractères dans une chaîne en utilisant la méthode Split()

Vous pouvez résoudre de nombreux problèmes intéressants en utilisant la méthode `split()` combinée avec d'autres méthodes de chaîne et de tableau. Voyons-en un ici. Il pourrait s'agir d'un cas d'utilisation courant pour remplacer toutes les occurrences d'un caractère dans la chaîne par un autre caractère. 

Par exemple, vous pouvez vouloir créer l'`id` d'un élément HTML à partir d'une valeur de nom. La valeur du nom peut contenir un espace (' '), mais en HTML, la valeur de l'id ne doit pas contenir d'espaces. Nous pouvons faire cela de la manière suivante :

```js
let name = 'Tapas Adhikary';
let subs = name.split(' ');
console.log(subs); // ["Tapas", "Adhikary"]

let joined = subs.join('-');
console.log(joined); // Tapas-Adhikary
```

Considérons que le nom contient le prénom (Tapas) et le nom de famille (Adhikary) séparés par un espace. Ici, nous divisons d'abord le nom en utilisant le séparateur d'espace. Il retourne un tableau contenant le prénom et le nom de famille comme éléments, c'est-à-dire `['Tapas', 'Adhikary']`.

Ensuite, nous utilisons la méthode de tableau appelée `join()` pour joindre les éléments du tableau en utilisant le caractère `-`. La méthode `join()` retourne une chaîne en joignant les éléments en utilisant un caractère passé comme paramètre. Ainsi, nous obtenons la sortie finale comme `Tapas-Adhikary`.

# ES6 : Comment diviser avec la destructuration de tableau

ECMAScript2015 (ES6) a introduit une manière plus innovante d'extraire un élément d'un tableau et de l'assigner à une variable. Cette syntaxe intelligente est connue sous le nom de `Destructuration de tableau`. Nous pouvons l'utiliser avec la méthode `split()` pour assigner facilement la sortie à une variable avec moins de code.

```js
let name = 'Tapas Adhikary';
let [firstName, lastName] = name.split(' ');
console.log(firstName, lastName);
```

Ici, nous divisons le nom en utilisant le caractère espace comme séparateur. Ensuite, nous assignons les valeurs retournées du tableau à quelques variables (le `firstName` et `lastName`) en utilisant la syntaxe de destructuration de tableau.

# Avant de terminer...

F44B Voulez-vous coder et apprendre avec moi ? Vous pouvez trouver le même contenu ici dans cette vidéo YouTube. Ouvrez simplement votre éditeur de code préféré et commencez.

%[https://www.youtube.com/watch?v=xbHFdstSpvc]

J'espère que vous avez trouvé cet article instructif et qu'il vous aide à comprendre plus clairement la méthode `split()` des chaînes JavaScript. Veuillez pratiquer les exemples plusieurs fois pour bien les maîtriser. Vous pouvez trouver tous les [exemples de code dans mon dépôt GitHub](https://github.com/atapas/js-handbook-examples/blob/master/string/split/index.js).

Restez en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre.

Vous pourriez également aimer ces articles :

* [Le manuel des tableaux JavaScript – Méthodes de tableau JS expliquées avec des exemples](https://www.freecodecamp.org/news/the-javascript-array-handbook/)
* [10 astuces DevTools pour vous aider avec CSS et la conception UX](https://blog.greenroots.info/10-devtools-tricks-to-help-you-with-css-and-ux-design-ckpp7mtnu04u6whs143e7huwx)
* [Un guide pratique de la destructuration d'objets en JavaScript](https://blog.greenroots.info/a-practical-guide-to-object-destructuring-in-javascript-cknx6tb2l06yvg1s1425rh54f)
* [10 faits HTML triviaux mais puissants que vous devez connaître](https://blog.greenroots.info/10-trivial-yet-powerful-html-facts-you-must-know-ckmx0d7q30346c1s125iydcsa)
* [10 astuces VS Code emmet pour vous rendre plus productif](https://blog.greenroots.info/10-vs-code-emmet-tips-to-make-you-more-productive-ckknjvxal028f1qs18w20e94t)