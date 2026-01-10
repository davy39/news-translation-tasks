---
title: Opérateur Rest vs Spread en JavaScript – Quelle est la différence ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-09-15T22:27:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-rest-vs-spread-operators
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/javascript-rest-vs-spread-operators-codesweetly-1.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Opérateur Rest vs Spread en JavaScript – Quelle est la différence ?
seo_desc: 'JavaScript uses three dots (...) for both the rest and spread operators.
  But these two operators are not the same.

  The main difference between rest and spread is that the rest operator puts the rest
  of some specific user-supplied values into a JavaSc...'
---

JavaScript utilise trois points (`...`) pour les opérateurs rest et spread. Mais ces deux opérateurs ne sont pas identiques.

La principale différence entre rest et spread est que l'opérateur rest place le reste de certaines valeurs spécifiques fournies par l'utilisateur dans un tableau JavaScript. Mais la syntaxe spread étend les itérables en éléments individuels.

Par exemple, considérons ce code qui utilise rest pour encapsuler certaines valeurs dans un tableau :

```js
// Utiliser rest pour encapsuler le reste des valeurs spécifiques fournies par l'utilisateur dans un tableau :
function myBio(firstName, lastName, ...otherInfo) { 
  return otherInfo;
}

// Invoquer la fonction myBio tout en passant cinq arguments à ses paramètres :
myBio("Oluwatobi", "Sofela", "CodeSweetly", "Développeur Web", "Homme");

// L'invocation ci-dessus retournera :
["CodeSweetly", "Développeur Web", "Homme"]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-t3kcyw?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé le paramètre rest `...otherInfo` pour mettre `"CodeSweetly"`, `"Développeur Web"`, et `"Homme"` dans un tableau.

Maintenant, considérons cet exemple d'opérateur spread :

```js
// Définir une fonction avec trois paramètres :
function myBio(firstName, lastName, company) { 
  return `${firstName} ${lastName} dirige ${company}`;
}

// Utiliser spread pour étendre les éléments d'un tableau en arguments individuels :
myBio(...["Oluwatobi", "Sofela", "CodeSweetly"]);

// L'invocation ci-dessus retournera :
"Oluwatobi Sofela dirige CodeSweetly"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ppjslx?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé l'opérateur spread (`...`) pour étendre le contenu de `["Oluwatobi", "Sofela", "CodeSweetly"]` à travers les paramètres de `myBio()`.

Ne vous inquiétez pas si vous ne comprenez pas encore les opérateurs rest ou spread. Cet article est là pour vous aider !

Dans les sections suivantes, nous discuterons du fonctionnement de rest et spread en JavaScript.

Alors, sans plus attendre, commençons par l'opérateur rest.

## Qu'est-ce que l'opérateur Rest exactement ?

L'**opérateur rest** est utilisé pour mettre le reste de certaines valeurs spécifiques fournies par l'utilisateur dans un tableau JavaScript.

Ainsi, par exemple, voici la syntaxe rest :

```js
...yourValues
```

Les trois points (`...`) dans l'extrait ci-dessus symbolisent l'opérateur rest.

Le texte après l'opérateur rest référence les valeurs que vous souhaitez encapsuler dans un tableau. Vous ne pouvez l'utiliser que devant le dernier paramètre dans une définition de fonction.

Pour mieux comprendre la syntaxe, voyons comment rest fonctionne avec les fonctions JavaScript.

### Comment fonctionne l'opérateur Rest dans une fonction ?

Dans les fonctions JavaScript, rest est utilisé comme préfixe du dernier paramètre de la fonction.

**Voici un exemple :**

```js
// Définir une fonction avec deux paramètres réguliers et un paramètre rest :
function myBio(firstName, lastName, ...otherInfo) { 
  return otherInfo;
}
```

L'opérateur rest (`...`) indique à l'ordinateur d'ajouter toutes les valeurs `otherInfo` (arguments) fournies par l'utilisateur dans un tableau. Ensuite, il assigne ce tableau au paramètre `otherInfo`.

Ainsi, nous appelons `...otherInfo` un paramètre rest.

**Note :** Les [arguments](https://www.codesweetly.com/javascript-arguments) sont des valeurs optionnelles que vous pouvez passer à un paramètre de fonction via un invocateur.

**Voici un autre exemple :**

```js
// Définir une fonction avec deux paramètres réguliers et un paramètre rest :
function myBio(firstName, lastName, ...otherInfo) { 
  return otherInfo;
}

// Invoquer la fonction myBio tout en passant cinq arguments à ses paramètres :
myBio("Oluwatobi", "Sofela", "CodeSweetly", "Développeur Web", "Homme");

// L'invocation ci-dessus retournera :
["CodeSweetly", "Développeur Web", "Homme"]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-t3kcyw?file=script.js)

Dans l'extrait ci-dessus, notez que l'invocation de `myBio` a passé cinq arguments à la fonction.

En d'autres termes, `"Oluwatobi"` et `"Sofela"` ont été assignés aux paramètres `firstName` et `lastName`.

En même temps, l'opérateur rest a ajouté les arguments restants (`"CodeSweetly"`, `"Développeur Web"`, et `"Homme"`) dans un tableau et a assigné ce tableau au paramètre `otherInfo`.

Par conséquent, la fonction `myBio()` a correctement retourné `["CodeSweetly", "Développeur Web", "Homme"]` comme contenu du paramètre rest `otherInfo`.

### Attention ! Vous ne pouvez pas utiliser « use strict » à l'intérieur d'une fonction contenant un paramètre Rest

Gardez à l'esprit que vous ne pouvez pas utiliser la directive `"use strict"` à l'intérieur d'une fonction contenant un paramètre rest, un paramètre par défaut, ou un [paramètre de destructuration](https://www.codesweetly.com/destructuring-object#how-to-use-a-destructuring-object-to-copy-values-from-properties-to-a-functions-parameters). Sinon, l'ordinateur générera une [erreur de syntaxe](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Strict_Non_Simple_Params).

Par exemple, considérons cet exemple ci-dessous :

```js
// Définir une fonction avec un paramètre rest :
function printMyName(...value) {
  "use strict";
  return value;
}

// La définition ci-dessus retournera :
"Uncaught SyntaxError: Illegal 'use strict' directive in function with non-simple parameter list"
```

[**Essayez-le sur CodeSandbox**](https://codesandbox.io/s/you-cannot-use-use-strict-inside-a-function-containing-a-spread-parameter-cvis3)

`printMyName()` a retourné une erreur de syntaxe parce que nous avons utilisé la directive `"use strict"` à l'intérieur d'une fonction avec un paramètre rest.

Mais supposons que vous avez besoin que votre fonction soit en mode strict tout en utilisant le paramètre rest. Dans un tel cas, vous pouvez écrire la directive `"use strict"` à l'extérieur de la fonction.

**Voici un exemple :**

```js
// Définir une directive "use strict" à l'extérieur de votre fonction :
"use strict";

// Définir une fonction avec un paramètre rest :
function printMyName(...value) {
  return value;
}

// Invoquer la fonction printMyName tout en passant deux arguments à ses paramètres :
printMyName("Oluwatobi", "Sofela");

// L'invocation ci-dessus retournera :
["Oluwatobi", "Sofela"]
```

[**Essayez-le sur CodeSandbox**](https://codesandbox.io/s/you-can-use-use-strict-outside-a-function-containing-a-spread-parameter-spbmh)

**Note :** Placez la directive `"use strict"` à l'extérieur de votre fonction uniquement si cela ne pose pas de problème que l'ensemble du script ou [la portée englobante](https://www.codesweetly.com/javascript-lexical-scope) soit en mode strict.

Maintenant que nous savons comment rest fonctionne dans une fonction, nous pouvons parler de son fonctionnement dans une [affectation par destructuration](https://www.codesweetly.com/destructuring-array).

### Comment l'opérateur Rest fonctionne dans une affectation par destructuration

L'opérateur rest est généralement utilisé comme préfixe de la dernière variable de l'affectation par destructuration.

**Voici un exemple :**

```js
// Définir un tableau de destructuration avec deux variables régulières et une variable rest :
const [firstName, lastName, ...otherInfo] = [
  "Oluwatobi", "Sofela", "CodeSweetly", "Développeur Web", "Homme"
];

// Invoquer la variable otherInfo :
console.log(otherInfo); 

// L'invocation ci-dessus retournera :
["CodeSweetly", "Développeur Web", "Homme"]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-tckdt8?file=script.js)

L'opérateur rest (`...`) indique à l'ordinateur d'ajouter le reste des valeurs fournies par l'utilisateur dans un tableau. Ensuite, il assigne ce tableau à la variable `otherInfo`.

Ainsi, vous pouvez appeler `...otherInfo` une variable rest.

**Voici un autre exemple :**

```js
// Définir un objet de destructuration avec deux variables régulières et une variable rest :
const { firstName, lastName, ...otherInfo } = {
  firstName: "Oluwatobi",
  lastName: "Sofela", 
  companyName: "CodeSweetly",
  profession: "Développeur Web",
  gender: "Homme"
}

// Invoquer la variable otherInfo :
console.log(otherInfo);

// L'invocation ci-dessus retournera :
{companyName: "CodeSweetly", profession: "Développeur Web", gender: "Homme"}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-fmr3dr?file=script.js)

Dans l'extrait ci-dessus, notez que l'opérateur rest a assigné un objet de propriétés — et non un tableau — à la variable `otherInfo`.

En d'autres termes, chaque fois que vous utilisez rest dans un [objet de destructuration](https://www.codesweetly.com/destructuring-object), l'opérateur rest produira un objet de propriétés.

Cependant, si vous utilisez rest dans un [tableau de destructuration](https://www.codesweetly.com/destructuring-array) ou une fonction, l'opérateur produira un littéral de tableau.

Avant de conclure notre discussion sur rest, vous devez être conscient de certaines différences entre les [arguments](https://www.codesweetly.com/javascript-arguments) JavaScript et le paramètre rest. Alors, parlons-en ci-dessous.

### Arguments vs Paramètres Rest : Quelle est la différence ?

Voici quelques-unes des différences entre les arguments JavaScript et le paramètre rest :

#### Différence 1 : L'objet `arguments` est un objet de type tableau — pas un vrai tableau !

Gardez à l'esprit que l'objet arguments JavaScript n'est pas un vrai tableau. Au lieu de cela, il s'agit d'un objet de type [tableau](https://www.codesweetly.com/javascript-arguments#what-is-an-arraylike-object) qui ne possède pas les fonctionnalités complètes d'un tableau JavaScript régulier.

Le paramètre rest, cependant, est un vrai objet tableau. Ainsi, vous pouvez utiliser toutes les méthodes de tableau sur celui-ci.

Par exemple, vous pouvez appeler la méthode `sort()`, `map()`, `forEach()`, ou `pop()` sur un paramètre rest. Mais vous ne pouvez pas faire de même sur l'objet arguments.

#### Différence 2 : Vous ne pouvez pas utiliser l'objet `arguments` dans une fonction fléchée

L'objet `arguments` n'est pas disponible dans une fonction fléchée, donc vous ne pouvez pas l'utiliser là. Mais vous pouvez utiliser le paramètre rest dans toutes les fonctions — y compris la fonction fléchée.

#### Différence 3 : Laissez rest être votre préférence

Il est préférable d'utiliser les paramètres rest au lieu de l'objet `arguments` — surtout lorsque vous écrivez du code compatible ES6.

Maintenant que nous savons comment fonctionne rest, discutons de l'opérateur `spread` afin que nous puissions voir les différences.

## Qu'est-ce que l'opérateur Spread et comment fonctionne `spread` en JavaScript ?

L'**opérateur spread** (`...`) vous aide à étendre les itérables en éléments individuels.

La syntaxe spread fonctionne dans les littéraux de tableau, les appels de fonction et les objets de propriétés initialisés pour étendre les valeurs des [objets itérables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#Iterables) en éléments séparés. Ainsi, il fait effectivement l'inverse de l'opérateur rest.

**Note :** Un opérateur spread est efficace uniquement lorsqu'il est utilisé dans des littéraux de tableau, des appels de fonction ou des objets de propriétés initialisés.

Alors, que signifie exactement cela ? Voyons avec quelques exemples.

### Exemple de Spread 1 : Comment Spread fonctionne dans un littéral de tableau

```js
const myName = ["Sofela", "is", "my"];
const aboutMe = ["Oluwatobi", ...myName, "name."];

console.log(aboutMe);

// L'invocation ci-dessus retournera :
[ "Oluwatobi", "Sofela", "is", "my", "name." ]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-rd1npd?file=script.js)

L'extrait ci-dessus a utilisé spread (`...`) pour copier le tableau `myName` dans `aboutMe`.

**Note :**

* Les modifications apportées à `myName` ne se refléteront pas dans `aboutMe` car toutes les valeurs à l'intérieur de `myName` sont des [primitives](https://www.codesweetly.com/web-tech-glossary#primitive-data-js). Par conséquent, l'opérateur spread a simplement copié et collé le contenu de `myName` dans `aboutMe` sans créer de référence vers le tableau original.
* Comme mentionné par [@nombrekeff](https://dev.to/oluwatobiss/spread-operator-how-spread-works-in-javascript-4fdn#comment-node-767546) dans un commentaire [ici](https://dev.to/oluwatobiss/spread-operator-how-spread-works-in-javascript-4fdn), l'opérateur spread ne fait que des copies superficielles. Donc, gardez à l'esprit que si `myName` contenait une valeur [non primitive](https://www.codesweetly.com/web-tech-glossary#non-primitive-data-js), l'ordinateur aurait créé une référence entre `myName` et `aboutMe`. Voir [info 3](#heading-info-3-beware-of-how-spread-works-when-used-on-objects-containing-non-primitives) pour plus d'informations sur le fonctionnement de l'opérateur spread avec les valeurs primitives et non primitives.
* Supposons que nous n'avons pas utilisé la syntaxe spread pour dupliquer le contenu de `myName`. Par exemple, si nous avions écrit `const aboutMe = ["Oluwatobi", myName, "name."]`. Dans un tel cas, l'ordinateur aurait assigné une référence à `myName`. Ainsi, tout changement apporté au tableau original se refléterait dans le duplicata.

### Exemple de Spread 2 : Comment utiliser Spread pour convertir une chaîne en éléments de tableau individuels

```js
const myName = "Oluwatobi Sofela";

console.log([...myName]);

// L'invocation ci-dessus retournera :
[ "O", "l", "u", "w", "a", "t", "o", "b", "i", " ", "S", "o", "f", "e", "l", "a" ]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-axvtye?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé la syntaxe spread (`...`) dans un littéral de tableau (`[...]`) pour étendre la valeur de chaîne de `myName` en éléments individuels.

Ainsi, `"Oluwatobi Sofela"` a été étendu en `[ "O", "l", "u", "w", "a", "t", "o", "b", "i", " ", "S", "o", "f", "e", "l", "a" ]`.

### Exemple de Spread 3 : Comment l'opérateur Spread fonctionne dans un appel de fonction

```js
const numbers = [1, 3, 5, 7];

function addNumbers(a, b, c, d) {
  return a + b + c + d;
}

console.log(addNumbers(...numbers));

// L'invocation ci-dessus retournera :
16
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-nrn8f3?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé la syntaxe spread pour étendre le contenu du tableau `numbers` à travers les paramètres de `addNumbers()`.

Supposons que le tableau `numbers` avait plus de quatre éléments. Dans un tel cas, l'ordinateur n'utiliserait que les quatre premiers éléments comme arguments de `addNumbers()` et ignorerait le reste.

**Voici un exemple :**

```js
const numbers = [1, 3, 5, 7, 10, 200, 90, 59];

function addNumbers(a, b, c, d) {
  return a + b + c + d;
}

console.log(addNumbers(...numbers));

// L'invocation ci-dessus retournera :
16
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ef3ncm?file=script.js)

**Voici un autre exemple :**

```js
const myName = "Oluwatobi Sofela";

function spellName(a, b, c) {
  return a + b + c;
}

console.log(spellName(...myName));      // retourne : "Olu"

console.log(spellName(...myName[3]));   // retourne : "wundefinedundefined"

console.log(spellName([...myName]));    // retourne : "O,l,u,w,a,t,o,b,i, ,S,o,f,e,l,aundefinedundefined"

console.log(spellName({...myName}));    // retourne : "[object Object]undefinedundefined"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-pkrxjd?file=script.js)

### Exemple de Spread 4 : Comment Spread fonctionne dans un littéral d'objet

```js
const myNames = ["Oluwatobi", "Sofela"];
const bio = { ...myNames, runs: "codesweetly.com" };

console.log(bio);

// L'invocation ci-dessus retournera :
{ 0: "Oluwatobi", 1: "Sofela", runs: "codesweetly.com" }
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-qnmxsu?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé spread à l'intérieur de l'objet `bio` pour étendre les valeurs de `myNames` en propriétés individuelles.

### Ce qu'il faut savoir sur l'opérateur Spread

Gardez ces trois informations essentielles à l'esprit chaque fois que vous choisissez d'utiliser l'opérateur spread.

#### Info 1 : Les opérateurs spread ne peuvent pas étendre les valeurs des littéraux d'objet

Puisqu'un objet de propriétés n'est pas un objet itérable, vous ne pouvez pas utiliser l'opérateur spread pour étendre ses valeurs.

Cependant, vous pouvez utiliser l'opérateur spread pour cloner des propriétés d'un objet à un autre.

**Voici un exemple :**

```js
const myName = { firstName: "Oluwatobi", lastName: "Sofela" };
const bio = { ...myName, website: "codesweetly.com" };

console.log(bio);

// L'invocation ci-dessus retournera :
{ firstName: "Oluwatobi", lastName: "Sofela", website: "codesweetly.com" };
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-psnsa8?file=script.js)

L'extrait ci-dessus a utilisé l'opérateur spread pour cloner le contenu de `myName` dans l'objet `bio`.

**Note :**

* L'opérateur spread peut étendre uniquement les valeurs des objets itérables.
* Un objet est itérable uniquement s'il (ou un objet dans sa chaîne de prototypes) possède une propriété avec une clé [@@iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol).
* [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/@@iterator), [TypedArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/@@iterator), [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/@@iterator), [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/@@iterator), et [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/@@iterator) sont tous des types itérables intégrés car ils possèdent la propriété `@@iterator` par défaut.
* Un objet de propriétés n'est pas un type de données itérable car il ne possède pas la propriété `@@iterator` par défaut.
* Vous pouvez [rendre un objet de propriétés itérable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator#user-defined_iterables) en ajoutant `@@iterator` à celui-ci.

#### Info 2 : L'opérateur spread ne clone pas les propriétés identiques

Supposons que vous avez utilisé l'opérateur spread pour cloner des propriétés de l'objet A dans l'objet B. Et supposons que l'objet B contient des propriétés identiques à celles de l'objet A. Dans un tel cas, les versions de B remplaceront celles à l'intérieur de A.

**Voici un exemple :**

```js
const myName = { firstName: "Tobi", lastName: "Sofela" };
const bio = { ...myName, firstName: "Oluwatobi", website: "codesweetly.com" };

console.log(bio);

// L'invocation ci-dessus retournera :
{ firstName: "Oluwatobi", lastName: "Sofela", website: "codesweetly.com" };
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-gjhjue?file=script.js)

Observez que l'opérateur spread n'a pas copié la propriété `firstName` de `myName` dans l'objet `bio` car `bio` contient déjà une propriété `firstName`.

#### Info 3 : Méfiez-vous de la façon dont spread fonctionne lorsqu'il est utilisé sur des objets contenant des non-primitives !

Supposons que vous avez utilisé l'opérateur spread sur un objet (ou un tableau) contenant uniquement des valeurs primitives. L'ordinateur ne créera aucune référence entre l'objet original et le duplicata.

Par exemple, considérons ce code ci-dessous :

```js
const myName = ["Sofela", "is", "my"];
const aboutMe = ["Oluwatobi", ...myName, "name."];

console.log(aboutMe);

// L'invocation ci-dessus retournera :
["Oluwatobi", "Sofela", "is", "my", "name."]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-rd1npd?file=script.js)

Observez que chaque élément de `myName` est une valeur primitive. Par conséquent, lorsque nous avons utilisé l'opérateur spread pour cloner `myName` dans `aboutMe`, l'ordinateur n'a créé aucune référence entre les deux tableaux.

Ainsi, toute modification que vous apportez à `myName` ne se reflétera pas dans `aboutMe`, et vice versa.

Par exemple, ajoutons plus de contenu à `myName` :

```js
myName.push("real");
```

Maintenant, vérifions l'état actuel de `myName` et `aboutMe` :

```js
console.log(myName); // ["Sofela", "is", "my", "real"]

console.log(aboutMe); // ["Oluwatobi", "Sofela", "is", "my", "name."]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ujs6ny?file=script.js)

Remarquez que le contenu mis à jour de `myName` ne s'est pas reflété dans `aboutMe` — car spread n'a créé aucune référence entre le tableau original et le duplicata.

##### Que se passe-t-il si `myName` contient des éléments non primitifs ?

Supposons que `myName` contenait des non-primitives. Dans ce cas, spread créera une référence entre la non-primitive originale et la clonée.

**Voici un exemple :**

```js
const myName = [["Sofela", "is", "my"]];
const aboutMe = ["Oluwatobi", ...myName, "name."];

console.log(aboutMe);

// L'invocation ci-dessus retournera :
[ "Oluwatobi", ["Sofela", "is", "my"], "name." ]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ombp5w?file=script.js)

Observez que `myName` contient une valeur non primitive.

Par conséquent, l'utilisation de l'opérateur spread pour cloner le contenu de `myName` dans `aboutMe` a amené l'ordinateur à créer une référence entre les deux tableaux.

Ainsi, toute modification que vous apportez à la copie de `myName` se reflétera dans la version de `aboutMe`, et vice versa.

Par exemple, ajoutons plus de contenu à `myName` :

```js
myName[0].push("real");
```

Maintenant, vérifions l'état actuel de `myName` et `aboutMe` :

```js
console.log(myName); // [["Sofela", "is", "my", "real"]]

console.log(aboutMe); // ["Oluwatobi", ["Sofela", "is", "my", "real"], "name."]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-qpyy8n?file=script.js)

Remarquez que le contenu mis à jour de `myName` est reflété dans `aboutMe` — car spread a créé une référence entre le tableau original et le duplicata.

**Voici un autre exemple :**

```js
const myName = { firstName: "Oluwatobi", lastName: "Sofela" };
const bio = { ...myName };

myName.firstName = "Tobi";

console.log(myName); // { firstName: "Tobi", lastName: "Sofela" }

console.log(bio); // { firstName: "Oluwatobi", lastName: "Sofela" }
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-tbmtgm?file=script.js)

Dans l'extrait ci-dessus, la mise à jour de `myName` ne s'est pas reflétée dans `bio` car nous avons utilisé l'opérateur spread sur un objet qui ne contient que des valeurs primitives.

**Note :** Un développeur appellerait `myName` un **objet superficiel** car il ne contient que des éléments primitifs.

**Voici un exemple supplémentaire :**

```js
const myName = { 
  fullName: { firstName: "Oluwatobi", lastName: "Sofela" }
};

const bio = { ...myName };

myName.fullName.firstName = "Tobi";

console.log(myName); // { fullName: { firstName: "Tobi", lastName: "Sofela" } }

console.log(bio); // { fullName: { firstName: "Tobi", lastName: "Sofela" } }
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-9uce9g?file=script.js)

Dans l'extrait ci-dessus, la mise à jour de `myName` est reflétée dans `bio` car nous avons utilisé l'opérateur spread sur un objet qui contient une valeur non primitive.

**Note :**

* Nous appelons `myName` un **objet profond** car il contient un élément non primitif.
* Vous faites une **copie superficielle** lorsque vous créez des références lors du clonage d'un objet dans un autre. Par exemple, `...myName` produit une copie superficielle de l'objet `myName` car toute modification que vous apportez à l'un se reflétera dans l'autre.
* Vous faites une **copie profonde** lorsque vous clonez des objets sans créer de références. Par exemple, je pourrais faire une copie profonde de `myName` dans `bio` en faisant `const bio = JSON.parse(JSON.stringify(myName))`. En faisant cela, l'ordinateur clonera `myName` dans `bio` sans créer de référence.
* Vous pouvez rompre la référence entre les deux objets en remplaçant l'objet `fullName` à l'intérieur de `myName` ou `bio` par un nouvel objet. Par exemple, faire `myName.fullName = { firstName: "Tobi", lastName: "Sofela" }` déconnecterait le pointeur entre `myName` et `bio`.

## Conclusion

Cet article a discuté des différences entre les opérateurs rest et spread. Nous avons également utilisé des exemples pour voir comment chaque opérateur fonctionne.

Merci d'avoir lu !