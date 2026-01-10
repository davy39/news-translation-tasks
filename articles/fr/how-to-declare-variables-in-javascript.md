---
title: Comment déclarer des variables en JavaScript – var, let et const expliqués
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2023-11-07T22:16:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-variables-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: Comment déclarer des variables en JavaScript – var, let et const expliqués
seo_desc: 'Declaring variables is something you''ll do all the time in JavaScript.
  And if you know the variable declaration process inside and out, you''ll have the
  confidence to start writing great JS code.

  Through this article, you will learn how to declare and...'
---

Déclarer des variables est une opération que vous effectuerez constamment en JavaScript. Et si vous maîtrisez parfaitement le processus de déclaration des variables, vous aurez la confiance nécessaire pour commencer à écrire du code JS de qualité.

À travers cet article, vous apprendrez à déclarer et à muter des variables en utilisant `var`, `let` et `const`, et vous comprendrez mieux les différences entre eux.

Je vais expliquer chaque concept en deux parties :

* Avant ES6 (l'instruction `var`)
* Après ES6 (les instructions `let` et `const`)

Plongeons dans ces différentes façons de déclarer des variables en JavaScript afin que vous sachiez comment elles fonctionnent et quand utiliser chacune d'elles.

## Comment déclarer des variables en JavaScript

Lorsque vous déclarez des variables dans votre application, l'interpréteur les déplace en haut de leur portée et alloue des emplacements en mémoire avant le début de l'exécution. Ce processus est appelé **Hoisting**.

### 1. Comment déclarer des variables avec `var` en JavaScript :

Lorsque vous déclarez une variable avec `var`, elle est hissée et initialisée en mémoire comme `undefined` avant l'exécution du code. Ainsi, vous pouvez accéder à la variable avant de la déclarer, mais elle retourne `undefined`. Cela s'appelle parfois **Declaration hoisting**.

Lorsque l'exécution commence et atteint la ligne où la variable est déclarée, elle remplace la valeur en mémoire par la valeur de la variable.

```javascript
console.log(strawberry); // undefined

var strawberry = '\ud83c\udf53';

console.log(strawberry); // \ud83c\udf53

```

Sous le capot, le code ci-dessus se comporte comme ceci :

```javascript
var strawberry;

console.log(strawberry); // undefined

strawberry = '\ud83c\udf53';

console.log(strawberry); // \ud83c\udf53

```

Ainsi, nous pouvons utiliser la variable `strawberry` avant la déclaration, mais elle retourne `undefined`.

Avec ce comportement, le programme s'exécute sans erreurs. Mais dans certains cas, cela peut conduire à des résultats inattendus. Nous sommes humains, et un jour chargé, vous pourriez essayer d'accéder à une variable avant de la déclarer. Dans un programme complexe, il peut être difficile de déterminer d'où provient un étrange `undefined`.

### 2. Comment déclarer des variables avec `let` et `const` en JavaScript :

Lorsque vous déclarez une variable avec `let` ou `const`, elle est également hissée mais elle est allouée en mémoire comme **non initialisée** dans la [zone morte temporelle](https://www.freecodecamp.org/news/what-is-the-temporal-dead-zone/). Vous ne pouvez pas accéder aux variables dans la zone morte temporelle avant de les avoir déclarées. Ainsi, si vous essayez d'accéder à une variable avant de la déclarer, le programme lève une `ReferenceError`.

Lorsque le programme atteint la ligne où la variable est déclarée, il l'initialise avec cette valeur.

```javascript
console.log(cherry); // ReferenceError

const cherry = "\ud83c\udf52";

console.log(cherry); // \ud83c\udf52

```

Si vous essayez d'exécuter cet extrait de code, vous verrez une erreur similaire à celle-ci car nous avons essayé d'accéder à une variable dans la zone morte temporelle.

![ReferenceError: Cannot access 'cherry' before initialization](https://www.freecodecamp.org/news/content/images/2023/10/error-1.png)
_"ReferenceError: Cannot access 'cherry' before initialization"_

C'est un comportement plus prévisible que celui de l'instruction `var`.

### Qu'ont donc en commun `var`, `let` et `const` ?

Dans les deux sections précédentes, vous avez appris le processus de déclaration de `var`, `let` et `const`. Dans cette section, nous examinerons les concepts communs.

* Vous pouvez déclarer une variable avec `let` et `var` sans valeur. Dans ce cas, la valeur par défaut sera `undefined`.

```javascript
var tomato;
let potato;

console.log(tomato); // undefined
console.log(potato); // undefined

```

Ce comportement n'est pas valide pour `const` car une valeur initiale est requise pour celui-ci. Si aucune valeur initiale n'est présente, le programme lève une `SyntaxError`.

```javascript
const avocado; // SyntaxError
```

Pour le code ci-dessus, une erreur est levée comme celle-ci :

!["SyntaxError: Missing initializer in const declaration"](https://www.freecodecamp.org/news/content/images/2023/11/image-4.png)
_SyntaxError: Missing initializer in const declaration_

* Vous pouvez déclarer une chaîne de variables en utilisant la même instruction. Placez l'instruction au début et séparez chaque variable par une virgule. Cela est valide pour `var`, `let` et `const`.

```javascript
let number1 = 2, number2 = 23, number3 = 99;

console.log(number1); // 2
console.log(number2); // 23
console.log(number3); // 99

```

De nos jours, pour déclarer des variables, vous voudrez utiliser les instructions ES6 `let` et `const`. Vous pouvez considérer `var` comme la méthode héritée pour le faire.

Ma recommandation est :

* Utilisez `const` par défaut.
* Utilisez `let` si la variable changera dans le futur.
* N'utilisez pas `var` s'il n'y a pas de cas d'utilisation particulier.

## Variables JavaScript et Portée

Selon [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Scope) :

> La **portée** est le contexte d'exécution actuel dans lequel les valeurs et les expressions sont "visibles" ou peuvent être référencées.

En termes de variables, la portée est l'endroit où certaines variables sont disponibles. Nous pouvons accéder aux variables qui ont été déclarées dans une portée parente dans une portée enfant, mais cela ne fonctionne pas dans l'autre sens.

### Portée Globale

La **Portée Globale** est la portée principale qui couvre toutes les portées dans un script. Les variables déclarées dans la portée globale sont disponibles dans toutes les portées.

```javascript
// Portée Globale

const grapes = "\ud83c\udf47";

// Portée Fonctionnelle
function logGrapes() {
  console.log(grapes); // \ud83c\udf47

  // Portée de Bloc dans une Portée Fonctionnelle
  {
    console.log(grapes); // \ud83c\udf47
  }
}

// Portée de Bloc
{
  console.log(grapes); // \ud83c\udf47
}

```

Dans l'exemple ci-dessus, nous pouvons accéder à la variable `grapes` depuis toutes les portées enfants car elle est déclarée dans la portée globale.

### Portée Fonctionnelle

La **portée fonctionnelle** est la portée créée avec une déclaration de fonction. Les variables déclarées dans une portée fonctionnelle ne sont disponibles que dans cette portée et ne peuvent pas être accessibles en dehors de celle-ci. Le comportement de `var`, `let` et `const` est le même dans ce cas.

Voici un exemple :

```javascript
// Portée Globale

// Portée Fonctionnelle
function createVariables() {
  var apple = "\ud83c\udf4e";
  const cherry = "\ud83c\udf52";
  let strawberry = "\ud83c\udf53";
}

console.log(apple); // ReferenceError
console.log(cherry); // ReferenceError
console.log(strawberry); // ReferenceError

```

Dans l'exemple ci-dessus, les trois variables ne sont accessibles que dans la portée fonctionnelle de la fonction `createVariables`. Si vous essayez d'y accéder en dehors de la portée fonctionnelle, le programme lève une `ReferenceError`.

### Portée de Bloc

La **portée de bloc** est la portée créée avec une paire d'accolades. La portée de bloc n'est valide que pour `let` et `const`, et non pour `var`. Lorsque vous déclarez une variable avec `var`, elle est déplacée vers la portée globale ou la portée fonctionnelle la plus proche si elle existe.

```javascript
// Portée de Bloc
{
  const banana = "\ud83c\udf4c";

  // Portée de Bloc dans une Portée de Bloc
  {
    console.log(banana); // \ud83c\udf4c

    var carrot = "\ud83e\udd55";
    let lemon = "\ud83c\udf4b";
  }

  console.log(carrot); // \ud83e\udd55
  console.log(lemon); // ReferenceError
}

```

Dans l'exemple ci-dessus :

* Nous pouvons accéder à la variable `banana` que nous avons déclarée avec `const` dans la portée parente dans la portée enfant.
* Nous pouvons accéder à la variable `carrot` déclarée avec `var` dans la portée enfant dans la portée parente car le programme la déplace vers la portée globale.
* Nous ne pouvons pas accéder à la variable `lemon` déclarée avec `let` dans la portée enfant dans la portée parente car elle ne peut pas être accessible en dehors de la portée dans laquelle elle est déclarée. Si nous essayons de le faire, le programme lève une `ReferenceError`.

## Comment muter des variables en JavaScript

Dans cette section, nous parlerons des instructions `var` et `let` ensemble, puis nous discuterons du comportement de l'instruction `const`. Cela est dû au fait que les variables déclarées avec `var` et `let` sont mutables (c'est-à-dire qu'elles peuvent être modifiées), tandis que les variables déclarées avec `const` sont immuables.

### 1. Mutation dans les instructions `var` et `let`

Comme je l'ai dit, les variables déclarées avec `var` et `let` sont mutables, ce qui signifie que vous pouvez leur attribuer de nouvelles valeurs. Voici ce que je veux dire :

```javascript
var pepper = "\ud83c\udf36\ufe0f";
let apple = "\ud83c\udf4f";

pepper = "\ud83e\uded1";
apple = "\ud83c\udf4e";

console.log(pepper); // \ud83e\uded1
console.log(apple); // \ud83c\udf4e

```

Dans l'exemple ci-dessus, nous avons muté les variables `pepper` et `apple`, et de nouvelles valeurs leur ont été attribuées.

### 2. Mutation dans l'instruction `const`

Les variables déclarées avec `const` sont immuables. Vous ne pouvez donc pas leur attribuer de nouvelles valeurs une fois que vous les avez déclarées.

```javascript
const strawberry = "\ud83c\udf53";

strawberry = "\ud83c\udf49"; // TypeError

```

Si vous essayez d'exécuter l'extrait de code ci-dessus, le programme lève une erreur comme celle-ci :

![TypeError: Assignment to constant variable.](https://www.freecodecamp.org/news/content/images/2023/10/error-3.png)
_"TypeError: Assignment to constant variable."_

Les objets sont une exception à l'immuabilité de l'instruction `const` car ils ont des propriétés et des méthodes, contrairement aux [primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive).

Vous ne pouvez pas les muter via une affectation, mais vous pouvez les muter via leurs méthodes et l'affectation de propriétés. Voici un exemple :

```javascript
const fruits = ["\ud83c\udf4e", "\ud83c\udf50"];
const fruitEmojiMap = {
  apple: "\ud83c\udf4e",
  pear: "\ud83c\udf50",
};

fruits[2] = "\ud83c\udf52"; // [ '\ud83c\udf4e', '\ud83c\udf50', '\ud83c\udf52' ]
fruits.push("\ud83c\udf4c"); // [ '\ud83c\udf4e', '\ud83c\udf50', '\ud83c\udf52', '\ud83c\udf4c' ]

fruitEmojiMap.cherry = "\ud83c\udf52"; // { apple: '\ud83c\udf4e', pear: '\ud83c\udf50', cherry: '\ud83c\udf52' }

```

Dans l'exemple de code ci-dessus,

* Nous avons ajouté deux nouveaux fruits au tableau `fruits` via l'affectation de propriétés, et utilisé la méthode `push` de l'objet `Array`.
* Nous avons ajouté un nouveau fruit à l'objet `fruitEmojiMap` via l'affectation de propriétés.

Une petite note : vous pouvez utiliser la méthode `[Object.freeze()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)` pour obtenir une immuabilité complète des objets.

## Comment redéclarer des variables en JavaScript

Redéclarer une variable avec le même nom dans la même portée est probablement quelque chose que vous ne voulez pas faire intentionnellement, et je n'ai jamais trouvé de cas d'utilisation réel pour cela.

Mais étrangement, nous pouvons redéclarer des variables déclarées avec `var` en utilisant le même nom dans la même portée. C'est une autre caractéristique sujette aux erreurs de l'instruction `var`. Heureusement, ce comportement a été modifié avec les instructions `let` et `const`.

### **1.** Comment redéclarer des variables avec `var`

Vous pouvez redéclarer une variable déclarée avec `var` dans la même portée ou dans des portées parent-enfant. La variable sera affectée dans la portée globale, ou dans la portée fonctionnelle si elle est déclarée dans une fonction.

Ainsi, même si vous redéclarez une variable dans la portée enfant, la variable changera dans toutes les portées où cette variable est disponible.

```javascript
// Portée Globale
var pepper = "\ud83c\udf36\ufe0f";

console.log(pepper); // \ud83c\udf36\ufe0f

// Portée de Bloc
{
  var pepper = "\ud83e\udd66";

  console.log(pepper); // \ud83e\udd66
}

console.log(pepper); // \ud83e\udd66

```

Dans l'exemple ci-dessus, nous avons déclaré une nouvelle variable `pepper` dans la portée de bloc et lui avons attribué une valeur différente. Cela affecte la variable dans la portée globale et nous perdons l'accès à la variable précédente.

Ce comportement tend à causer de gros problèmes. Parce que quelqu'un travaillant sur la même base de code peut déclarer involontairement une variable en utilisant le même nom utilisé auparavant.

Le processus est un peu différent si vous faites la redéclaration dans une fonction. La variable en dehors de la fonction reste la même et la variable à l'intérieur de la fonction ne peut pas l'affecter. Comme je l'ai dit, les variables déclarées avec `var` dans une fonction sont dans la portée fonctionnelle et n'affectent pas l'extérieur.

```javascript
// Portée Globale
var onion = "\ud83e\uddc5";

// Portée Fonctionnelle
function redeclareOnion() {
  var onion = "\ud83e\uddc4";

  console.log(onion); // \ud83e\uddc4
}

console.log(onion); // \ud83e\uddc5

```

Dans l'exemple ci-dessus, même si nous avons déclaré une nouvelle variable en utilisant le même nom que la variable `onion` à l'intérieur d'une fonction, la variable `onion` déclarée dans la portée globale est restée la même.

### 2. Comment redéclarer des variables avec `let` et `const`

Vous ne pouvez pas redéclarer des variables déclarées avec `let` ou `const` dans la même portée. Si vous essayez de le faire, le programme lève une `SyntaxError`.

```javascript
let eggplant = "\ud83c\udf46";

let eggplant = "\ud83e\udd54"; // SyntaxError

```

Dans l'exemple ci-dessus, nous avons essayé de redéclarer la variable `eggplant` dans la même portée, et le programme a levé l'erreur suivante :

![SyntaxError: Identifier 'eggplant' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-17.png)
_"SyntaxError: Identifier 'eggplant' has already been declared"_

Mais vous pouvez redéclarer des variables en utilisant `let` et `const` dans des portées enfants. Parce que les variables déclarées avec `let` et `const` sont dans la portée de bloc et n'affectent pas les portées parent.

```javascript
// Portée Globale
const carrot = "\ud83e\udd55";

// Portée de Bloc
{
  const carrot = "\ud83c\udf52";

  console.log(carrot); // \ud83c\udf52
}

console.log(carrot); // \ud83e\udd55

```

Dans l'exemple ci-dessus, nous avons déclaré deux variables `carrot`. La première est dans la portée globale et la seconde est dans la portée de bloc avec une valeur différente. La variable dans la portée globale reste la même et la variable dans la portée de bloc est une nouvelle variable autonome.

L'inconvénient est que nous avons perdu l'accès à la variable `carrot` déclarée dans la portée globale, dans la portée de bloc. Si nous avons besoin de cette variable à l'avenir, nous ne pouvons pas y accéder.

Ainsi, la plupart du temps, il est préférable de déclarer une variable avec un nom unique.

### 3. Comment redéclarer des variables en mélangeant les instructions

En bref, vous ne devriez pas mélanger les instructions. Cette section est destinée à vous donner des informations plutôt qu'à vous montrer comment le processus est réalisé.

Vous ne pouvez pas créer de variables en mélangeant des instructions utilisant le même nom dans la même portée. Si vous essayez, le programme lève une `SyntaxError`.

```javascript
const banana = "\ud83c\udf4c";

var banana = "\ud83c\udf4b"; // SyntaxError

```

Dans l'exemple ci-dessus, nous avons essayé de redéclarer la variable `banana` déclarée avec `const` avec `var`, mais le programme a levé une erreur similaire à celle ci-dessous :

![SyntaxError: Identifier 'banana' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-16.png)
_"SyntaxError: Identifier 'banana' has already been declared"_

De plus, vous ne pouvez pas déclarer une variable avec `var` en utilisant le même nom qu'une variable déjà déclarée dans une portée parente en utilisant `let` ou `const`. Comme je l'ai dit, `var` est dans la portée globale et affecte la variable déclarée dans les portées parent, sauf si elle est à l'intérieur d'une fonction.

```javascript
// Portée Globale
let pineapple = "\ud83c\udf4d";

// Portée Fonctionnelle
function declarePineapple() {
  var pineapple = "\ud83c\udf4f"; // C'est correct
}

// Portée de Bloc
{
  var pineapple = "\ud83c\udf4e"; // SyntaxError
}

```

Dans l'exemple ci-dessus, nous avons essayé de redéclarer la variable `pineapple` à deux endroits :

* Dans la fonction, ce que nous avons fait avec succès.
* Mais dans la portée de bloc enfant, le programme a levé l'erreur suivante :

![SyntaxError: Identifier 'pineapple' has already been declared](https://www.freecodecamp.org/news/content/images/2023/11/image-19.png)
_"SyntaxError: Identifier 'pineapple' has already been declared"_

## Conclusion

De nos jours, `let` et `const` sont les choix par défaut pour la déclaration de variables en JavaScript. Mais vous pourriez encore rencontrer l'instruction `var`, surtout dans les anciennes applications. Vous devrez donc savoir comment la gérer.

Dans ce guide, vous avez appris les différences entre `var`, `let` et `const`. Nous avons également parlé du hoisting et de la portée dans la déclaration de variables.

À la prochaine !

### Restez en contact

Vous pouvez me suivre sur [Twitter](https://twitter.com/femincan), et vous pouvez lire plus de tutoriels comme celui-ci [sur mon blog ici](https://femincan.dev).