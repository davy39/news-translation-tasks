---
title: JavaScript Concaténer des Chaînes – Comment Fonctionne la Concaténation de
  Chaînes en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-05-07T17:14:16.908Z'
originalURL: https://freecodecamp.org/news/how-js-string-concatenation-works
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/mfB1B1s4sMc/upload/138f5daa340578a0ba2da07274b59252.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Strings
  slug: strings
seo_title: JavaScript Concaténer des Chaînes – Comment Fonctionne la Concaténation
  de Chaînes en JS
seo_desc: 'When coding in JavaScript, you may need to combine multiple strings to
  create a new, longer string. This operation is known as concatenation.

  In this article, you will learn five ways to concatenate strings in JavaScript.

  How to Concatenate Strings i...'
---

Lorsque vous codez en JavaScript, vous pouvez avoir besoin de combiner plusieurs chaînes pour créer une nouvelle chaîne plus longue. Cette opération est connue sous le nom de concaténation.

Dans cet article, vous apprendrez cinq façons de concaténer des chaînes en JavaScript.

## Comment Concaténer des Chaînes en JavaScript en Utilisant l'Opérateur `+`

L'opérateur `+` n'est pas utilisé uniquement pour effectuer des additions, mais aussi pour concaténer des chaînes.

Prenons l'exemple suivant :

```jsx
let greeting = "Hello";
let name = "John";

let result = greeting + name;

console.log(result); // Sortie : HelloJohn
```

Dans le code ci-dessus, j'ai créé deux variables nommées `greeting` et `name`, et j'ai stocké les valeurs de chaîne `Hello` et `John`, respectivement.

J'ai également créé une autre variable nommée `result` et j'ai stocké le résultat de la concaténation de `greeting` et `name` en utilisant l'opérateur `+`.

Enfin, j'ai utilisé `console.log()` pour afficher le `result` dans la console.

Si vous regardez attentivement la sortie, `HelloJohn`, vous remarquerez qu'il n'y a pas d'espace entre `Hello` et `John`. Le résultat de la jonction des deux chaînes, `Hello` et `John`, sera une nouvelle chaîne unique, `HelloJohn`.

Lorsque vous concaténez des chaînes avec l'opérateur `+`, vous devez vous souvenir d'ajouter des espaces entre les chaînes, sinon vous obtiendrez une sortie inattendue :

```jsx
let greeting = "Hello";
let name = "John";

let result = greeting + " " + name;

console.log(result); // Sortie : Hello John
```

Ainsi, bien que l'opérateur `+` soit une approche pratique pour la concaténation de chaînes de base en JavaScript, vous devez être attentif à la séparation manuelle des chaînes, ce qui peut entraîner des erreurs lors de la réalisation de concaténations de chaînes plus complexes.

## Comment Concaténer des Chaînes en JavaScript en Utilisant l'Opérateur `+=`

L'opérateur `+=` est utilisé lorsque vous souhaitez ajouter une chaîne à une chaîne existante.

Prenons l'exemple suivant :

```javascript
let name = "John ";

name += "Doe";

console.log(name); // Sortie : John Doe
```

Dans l'exemple ci-dessus, j'ai créé une variable `name` et j'ai stocké la valeur de chaîne `John` avec un espace à la fin. Notez que lorsque vous utilisez l'opérateur `+=`, vous devez ajouter des espaces pour séparer les chaînes, similaire à l'utilisation de l'opérateur `+`.

Ensuite, j'ai ajouté la chaîne `Doe` à la variable `name`. Après cette opération, la variable `name` contiendra la chaîne `John Doe`.

L'opérateur `+=` prend la valeur originale de la variable `name`, `John`, ajoute la valeur `Doe` et assigne le résultat à la variable.

Vous pouvez considérer la ligne `name += "Doe";` comme une abréviation pour `name = name + "Doe"`.

## Comment Concaténer des Chaînes en JavaScript en Utilisant les Littéraux de Gabarit

Comme vous l'avez vu précédemment, l'opérateur `+` est pratique pour la concaténation de chaînes de base. Cependant, le code peut devenir difficile à lire ou entraîner des erreurs lors de la réalisation de concaténations de chaînes plus complexes.

Les littéraux de gabarit offrent une alternative plus lisible et facilitent le travail avec les chaînes.

Les littéraux de gabarit utilisent des backticks (\`) pour encadrer une chaîne au lieu de guillemets simples ou doubles. À l'intérieur des backticks, vous pouvez insérer des variables ou des expressions directement dans des chaînes en utilisant `${}`.

Reprenons le code pour concaténer des chaînes en utilisant l'opérateur `+` :

```javascript
let greeting = "Hello";
let name = "John";

let result = greeting + " " + name;

console.log(result); // Sortie : Hello John
```

Voici comment vous réécririez le code en utilisant des littéraux de gabarit :

```javascript
let greeting = "Hello";
let name = "John";

let result = `${greeting} ${name}`;

console.log(result); // Sortie : Hello John
```

Les `${greeting}` et `${name}` sont comme des espaces réservés qui sont remplacés par les valeurs réelles des variables. `${greeting}` intègre la valeur de la variable `greeting` dans la chaîne, et `${name}` intègre la valeur de la variable `name`.

Bien que les deux exemples de code produisent la même sortie, le code utilisant les littéraux de gabarit est plus lisible et concis par rapport au code utilisant l'opérateur `+`.

## Comment Concaténer des Chaînes en JavaScript en Utilisant la Méthode `concat()`

Vous pouvez également utiliser la méthode intégrée `concat()` pour concaténer deux ou plusieurs chaînes en JavaScript.

La syntaxe générale de la méthode `concat()` ressemble à quelque chose comme ceci :

```javascript
string.concat(string1, string2, ..., stringN)
```

Vous pouvez appeler la méthode `concat()` sur une chaîne et passer la ou les chaînes que vous souhaitez concaténer en tant qu'arguments à l'intérieur des parenthèses. Lorsque vous passez plusieurs chaînes en tant qu'arguments, vous séparez chaque chaîne par une virgule.

Notez que la méthode `concat()` ne modifie pas la chaîne originale. Au lieu de cela, elle retourne une nouvelle chaîne concaténée.

Voyons un exemple de la méthode `concat()` en action :

```javascript
let greeting = "Hello";
let name = "John";

let result = greeting.concat(name);

console.log(result); 
console.log(greeting);

// Sortie : 

// Hello John
// Hello
```

Dans le code ci-dessus, la méthode `concat()` est appelée sur la variable de chaîne initiale `name`, et la variable de chaîne `greeting` est passée en tant qu'argument.

Cela crée une nouvelle chaîne, `Hello John`, où `name` est ajouté à la fin de `greeting`. La chaîne dans la variable `greeting` ne change pas.

## Comment Concaténer des Chaînes en JavaScript en Utilisant la Méthode `join()`

Enfin, vous pouvez concaténer des chaînes en utilisant la méthode intégrée `join()`.

La syntaxe générale de la méthode `join()` ressemble à quelque chose comme ceci :

```javascript
array.join(separator);
```

La méthode `join()` est utile lorsque vous travaillez avec des tableaux de chaînes, car elle combine tous les éléments du tableau en une seule chaîne séparée par un séparateur que vous spécifiez. Lorsque vous ne spécifiez pas de séparateur, une virgule est utilisée par défaut.

Prenons l'exemple suivant :

```javascript
let programmingLanguages = ["JavaScript", "Java", "Python"];

let result = programmingLanguages.join(", ");

console.log(result); // Sortie : JavaScript, Java, Python
```

Dans l'exemple ci-dessus, j'ai d'abord créé un tableau appelé `programmingLanguages` contenant trois chaînes : `JavaScript`, `Java` et `Python`.

Ensuite, j'ai appelé la méthode `join()` sur `programmingLanguages` pour concaténer tous les éléments du tableau en une seule chaîne et j'ai utilisé une virgule suivie d'un espace, `,` , comme séparateur. Puis, j'ai stocké le résultat dans une nouvelle variable appelée `result`.

Les éléments du tableau `JavaScript`, `Java` et `Python` sont joints ensemble avec une virgule et un espace entre chaque élément, résultant en la chaîne `JavaScript, Java, Python`.

## Conclusion

Dans cet article, vous avez appris cinq façons de concaténer des chaînes en JavaScript.

Pour résumer :

* L'opérateur `+` est utile pour effectuer une concaténation de chaînes de base, mais il peut devenir moins lisible lors de la réalisation de concaténations plus complexes.

* L'opérateur `+=` est pratique lorsque vous souhaitez ajouter une chaîne à une chaîne existante et modifier la chaîne originale.

* Les littéraux de gabarit vous permettent d'intégrer des variables directement dans une chaîne et fournissent une syntaxe lisible et concise.

* La méthode `concat()` est utile lorsque vous souhaitez concaténer des chaînes mais ne souhaitez pas modifier les chaînes existantes.

* La méthode `join()` vous permet de concaténer un tableau de chaînes en une seule chaîne, avec un séparateur optionnel entre chaque élément du tableau.

Merci d'avoir lu, et bon codage !