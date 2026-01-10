---
title: JavaScript String to Boolean – Comment analyser un booléen en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-30T22:14:10.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-to-boolean
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/string-to-boolean.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript String to Boolean – Comment analyser un booléen en JS
seo_desc: 'When you''re manipulating data, receiving values from forms, and dealing
  with data in other ways, these values may take the incorrect datatype.

  Assume you want your value to be a boolean with either true or false, but it is
  stored as a string – "true"...'
---

Lorsque vous manipulez des données, recevez des valeurs de formulaires et traitez des données de différentes manières, ces valeurs peuvent avoir le mauvais type de données.

Supposons que vous souhaitez que votre valeur soit un booléen avec soit `true` soit `false`, mais qu'elle est stockée sous forme de chaîne de caractères – "true" ou "false". Il devient difficile de l'utiliser pour votre objectif prévu, vous devez donc d'abord convertir ces valeurs de chaîne de caractères en valeurs booléennes réelles.

Dans cet article, vous apprendrez comment convertir une chaîne de caractères en une valeur booléenne en utilisant différentes méthodes en JavaScript. Si vous êtes pressé, voici comment vous pouvez le faire :

```js
// Utilisation de l'opérateur d'identité
console.log((boolString === "true")); // true / false

// Utilisation de Regex
console.log((/true/).test(boolString)); // true
```

Si vous n'êtes pas pressé, comprenons chacune des méthodes et bien plus encore.

## Comment analyser une chaîne de caractères en booléen avec l'opérateur d'identité (`===`)

L'opérateur strict est un autre nom pour l'opérateur d'identité. Il ne retournera `true` que si les deux valeurs comparées sont identiques. Cela implique que leur casse de lettres – et tout le reste – doit également être le même. Sinon, il retournera `false`.

Dans ce cas, vous souhaitez convertir une chaîne de caractères en booléen, ce qui signifie que vous la comparerez à la chaîne "true". Si les deux valeurs sont identiques, il retournera la valeur booléenne `true`, sinon, il retournera la valeur booléenne `false`.

```js
let boolString = "true"; 
let boolValue = (boolString === "true"); 
console.log(boolValue); // true
```

Il s'agit d'un opérateur d'égalité stricte et il sera strict avec la comparaison de la casse des lettres :

```js
let boolString = "True"; 
let boolValue = (boolString === "true"); 
console.log(boolValue); // false
```

Vous pouvez corriger cela en utilisant la méthode `toLowerCase()`, afin qu'elle convertisse d'abord la valeur de la chaîne de caractères en casse de lettres qui correspond à votre comparaison, puis qu'elle compare.

```js
let boolString = "True"; 
let boolValue = (boolString.toLowerCase() === "true"); 
console.log(boolValue); // true
```

Une autre méthode très similaire à l'opérateur d'identité est la méthode regex, où vous pouvez tester si deux valeurs correspondent.

## Comment analyser une chaîne de caractères en booléen avec Regex

Regex signifie Expressions Régulières. C'est un vaste sujet de programmation et vous pouvez utiliser regex comme un motif pour faire correspondre et tester des combinaisons de caractères de chaîne.

Un guide très simple sur regex vous dira que l'expression est placée entre deux barres obliques (`/`). Par exemple, si vous souhaitez tester la valeur de chaîne "true", vous feriez ceci :

```js
let boolString = "true"; 
let boolValue = (/true/).test(boolString);
console.log(boolValue); // true
```

Cela est également sensible à la casse :

```js
let boolString = "True"; 
let boolValue = (/true/).test(boolString);
console.log(boolValue); // false
```

Vous devrez ajouter le drapeau `i` à la fin de l'expression régulière pour permettre une correspondance insensible à la casse.

```js
let boolString = "True"; 
let boolValue = (/true/i).test(boolString);
console.log(boolValue); // true
```

## Comment analyser une chaîne de caractères en booléen avec l'opérateur Double NOT (`!!`)

Vous devriez également savoir comment utiliser l'opérateur NOT simple, que vous pouvez utiliser pour inverser un résultat.

Lorsque vous ajoutez l'opérateur NOT simple devant une chaîne de caractères, il retournera soit `true` soit `false`. Si c'est une chaîne vide, il retournera `true`, sinon, `false` :

```js
let stringValue1 = !'true';
let stringValue2 = !'';

console.log(stringValue1); // false
console.log(stringValue2); // true
```

Ce n'est pas ce que vous voulez. Plutôt, vous souhaitez convertir une chaîne de caractères en booléen, ce qui signifie que lorsque la chaîne est vide, elle devrait retourner `false`, et dans tous les autres cas, elle devrait retourner `true`.

C'est alors que vous pouvez utiliser l'opérateur logique double NOT. Vous l'utilisez pour inverser le résultat de l'opérateur NOT simple :

```js
let stringValue1 = !!'true';
let stringValue2 = !!'';

console.log(stringValue1); // true
console.log(stringValue2); // false
```

Vous utilisez cette méthode pour convertir **toute valeur de chaîne** en booléen. Lorsqu'elle est vide, elle retourne `false`. Sinon, elle retourne `true`.

Un inconvénient de cette méthode est que vous ne pouvez pas convertir une chaîne de `"false"` en une valeur booléenne de `false`. Elle ne retournera `false` que lorsqu'il s'agit d'une chaîne vide.

## Comment analyser une chaîne de caractères en booléen avec un wrapper Boolean

L'objet Boolean de JavaScript représente une valeur booléenne. Cette méthode fonctionne exactement comme l'opérateur double NOT.

```js
// Syntaxe
Boolean()
```

Lorsque vous passez une valeur de chaîne dans l'objet Boolean, il évaluera à `true`, mais lorsque vous passez une chaîne vide, il évaluera à `false`.

```js
let stringValue1 = Boolean('true');
let stringValue2 = Boolean('');

console.log(stringValue1); // true
console.log(stringValue2); // false
```

La seule limitation avec cette méthode est que si vous ajoutez un espace entre les guillemets pour représenter une chaîne, il retournera `true` — ce qui signifie qu'il la considère comme une chaîne.

```js
let stringValue = Boolean(' ');

console.log(stringValue); // true
```

**Note :** Lorsque vous convertissez une chaîne de `"false"`, vous vous attendez à ce qu'elle retourne une valeur booléenne de `false`. Mais cela retournera `true` car il ne retourne `false` que lorsqu'il s'agit d'une chaîne vide.

## Conclusion

Dans cet article, vous avez appris comment convertir une valeur de chaîne en booléen. La meilleure approche qui couvre tous les scénarios est l'opérateur d'égalité d'identité, tandis que l'objet Boolean et le double NOT logique ont une meilleure syntaxe.

Amusez-vous bien à coder !