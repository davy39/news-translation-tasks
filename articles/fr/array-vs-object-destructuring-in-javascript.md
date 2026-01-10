---
title: Destructuration de tableau vs objet en JavaScript – Quelle est la différence
  ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-11-10T16:24:16.000Z'
originalURL: https://freecodecamp.org/news/array-vs-object-destructuring-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/extract-777603_1920-Image-by-Oscar-Castillo-from-Pixabay.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Destructuration de tableau vs objet en JavaScript – Quelle est la différence
  ?
seo_desc: 'The destructuring assignment in JavaScript provides a neat and DRY way
  to extract values from your arrays and objects.

  This article aims to show you exactly how array and object destructuring assignments
  work in JavaScript.

  So, without any further ad...'
---

L'affectation par destructuration en JavaScript offre une manière propre et DRY d'extraire des valeurs de vos tableaux et objets.

Cet article vise à vous montrer exactement comment fonctionnent les affectations par destructuration de tableaux et d'objets en JavaScript.

Alors, sans plus attendre, commençons par la destructuration de tableaux.

## Qu'est-ce que la destructuration de tableaux ?

La **destructuration de tableaux** est une technique unique qui permet d'extraire proprement les valeurs d'un tableau dans de nouvelles variables.

Par exemple, sans utiliser la technique d'affectation par destructuration de tableaux, vous copieriez les valeurs d'un tableau dans une nouvelle variable comme suit :

```js
const profile = ["Oluwatobi", "Sofela", "codesweetly.com"];

const firstName = profile[0];
const lastName = profile[1];
const website = profile[2];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-mrqjsu?file=script.js)

Remarquez que l'extrait ci-dessus contient beaucoup de code répété, ce qui n'est pas une manière DRY (**D**on't **R**epeat **Y**ourself) de coder.

Voyons maintenant comment la destructuration de tableaux rend les choses plus propres et DRY.

```js
const profile = ["Oluwatobi", "Sofela", "codesweetly.com"];

const [firstName, lastName, website] = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-uxrjek?file=script.js)

Vous voyez, comme par magie, nous avons nettoyé notre code en plaçant les trois nouvelles variables (c'est-à-dire `firstName`, `lastName` et `website`) dans un objet tableau (`[...]`). Ensuite, nous leur avons assigné les valeurs du tableau `profile`.

En d'autres termes, nous avons instructé l'ordinateur d'extraire les valeurs du tableau `profile` dans les variables du côté gauche de l'[opérateur d'affectation](https://www.codesweetly.com/javascript-expression#types-of-expressions-in-javascript).

Par conséquent, JavaScript analysera le tableau `profile` et copiera sa première valeur (`"Oluwatobi"`) dans la première variable du tableau de destructuration (`firstName`).

De même, l'ordinateur extraira la deuxième valeur du tableau `profile` (`"Sofela"`) dans la deuxième variable du tableau de destructuration (`lastName`).

Enfin, JavaScript copiera la troisième valeur du tableau `profile` (`"codesweetly.com"`) dans la troisième variable du tableau de destructuration (`website`).

Remarquez que l'extrait ci-dessus a destructuré le tableau `profile` en le référençant. Cependant, vous pouvez également faire une destructuration directe d'un tableau. Voyons comment.

### Comment faire une destructuration directe de tableau

JavaScript permet de destructurer un tableau directement comme suit :

```js
const [firstName, lastName, website] = [
  "Oluwatobi", 
  "Sofela", 
  "codesweetly.com"
];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-rndtx5?file=script.js)

Supposons que vous préférez séparer vos déclarations de variables de leurs affectations. Dans ce cas, JavaScript vous couvre. Voyons comment.

### Comment utiliser la destructuration de tableau tout en séparant les déclarations de variables de leurs affectations

Lorsque vous utilisez la destructuration de tableau, JavaScript vous permet de séparer vos déclarations de variables de leurs affectations.

**Voici un exemple :**

```js
let firstName, lastName, website;

[firstName, lastName, website] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-nm1ng3?file=script.js)

Que faire si vous voulez que `"Oluwatobi"` soit assigné à la variable `firstName` et que le reste des éléments du tableau soit assigné à une autre variable ? Comment faire cela ? Découvrons-le ci-dessous.

### Comment utiliser la destructuration de tableau pour assigner le reste d'un littéral de tableau à une variable

JavaScript permet d'utiliser l'[opérateur rest](https://www.codesweetly.com/javascript-rest-operator) dans un tableau de destructuration pour assigner le reste d'un tableau régulier à une variable.

**Voici un exemple :**

```js
const [firstName, ...otherInfo] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(firstName); // "Oluwatobi"
console.log(otherInfo); // ["Sofela", "codesweetly.com"]
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-w15axc?file=script.js)

**Note :** Utilisez toujours l'opérateur rest comme dernier élément de votre tableau de destructuration pour éviter d'obtenir une `SyntaxError`.

Maintenant, que faire si vous voulez uniquement extraire `"codesweetly.com"` ? Discutons de la technique que vous pouvez utiliser ci-dessous.

### Comment utiliser la destructuration de tableau pour extraire des valeurs à n'importe quel index

Voici comment vous pouvez utiliser la destructuration de tableau pour extraire des valeurs à n'importe quelle position d'index d'un tableau régulier :

```js
const [, , website] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-311nkt?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé des virgules pour sauter les variables aux première et deuxième positions d'index du tableau de destructuration.

En faisant cela, nous avons pu lier la variable `website` à la valeur du troisième index du tableau régulier du côté droit de l'opérateur d'affectation (c'est-à-dire `"codesweetly.com"`).

Parfois, cependant, la valeur que vous souhaitez extraire d'un tableau est `undefined`. Dans ce cas, JavaScript fournit un moyen de définir des valeurs par défaut dans le tableau de destructuration. Apprenons-en plus à ce sujet ci-dessous.

### Comment les valeurs par défaut fonctionnent dans une affectation par destructuration de tableau

Définir une valeur par défaut peut être utile lorsque la valeur que vous souhaitez extraire d'un tableau n'existe pas (ou est définie sur `undefined`).

Voici comment vous pouvez en définir une à l'intérieur d'un tableau de destructuration :

```js
const [firstName = "Tobi", website = "CodeSweetly"] = ["Oluwatobi"];

console.log(firstName); // "Oluwatobi"
console.log(website); // "CodeSweetly"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-r38k67?file=script.js)

Dans l'extrait ci-dessus, nous avons défini `"Tobi"` et `"CodeSweetly"` comme valeurs par défaut des variables `firstName` et `website`.

Par conséquent, dans notre tentative d'extraire la première valeur d'index du tableau du côté droit, l'ordinateur a utilisé la valeur par défaut `"CodeSweetly"`—parce qu'il n'existe qu'une valeur d'index zéro dans `["Oluwatobi"]`.

Alors, que faire si vous devez échanger la valeur de `firstName` avec celle de `website` ? Encore une fois, vous pouvez utiliser la destructuration de tableau pour accomplir cela. Voyons comment.

### Comment utiliser la destructuration de tableau pour échanger les valeurs de variables

Vous pouvez utiliser l'affectation par destructuration de tableau pour échanger les valeurs de deux ou plusieurs variables différentes.

**Voici un exemple :**

```js
let firstName = "Oluwatobi";
let website = "CodeSweetly";

[firstName, website] = [website, firstName];

console.log(firstName); // "CodeSweetly"
console.log(website); // "Oluwatobi"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-fu7phn?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé la destructuration directe de tableau pour réaffecter les variables `firstName` et `website` avec les valeurs du littéral de tableau du côté droit de l'opérateur d'affectation.

Ainsi, la valeur de `firstName` changera de `"Oluwatobi"` à `"CodeSweetly"`. Tandis que le contenu de `website` changera de `"CodeSweetly"` à `"Oluwatobi"`.

Gardez à l'esprit que vous pouvez également utiliser la destructuration de tableau pour extraire des valeurs d'un tableau régulier vers les paramètres d'une fonction. Parlons-en plus ci-dessous.

### Comment utiliser la destructuration de tableau pour extraire des valeurs d'un tableau vers les paramètres d'une fonction

Voici comment vous pouvez utiliser la destructuration de tableau pour extraire les valeurs d'un tableau vers les paramètres d'une fonction :

```js
// Définir un tableau avec deux éléments :
const profile = ["Oluwatobi", "Sofela"];

// Définir une fonction avec un tableau de destructuration contenant deux paramètres :
function getUserBio([firstName, lastName]) {
  return `My name is ${firstName} ${lastName}.`;
}

// Invoquer getUserBio en passant le tableau profile comme argument :
getUserBio(profile);

// L'invocation ci-dessus retournera :
"My name is Oluwatobi Sofela."
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ckdkjb?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé un paramètre de destructuration de tableau pour extraire les valeurs du tableau `profile` dans les paramètres `firstName` et `lastName` de `getUserBio`.

**Note :** Un paramètre de destructuration de tableau est typiquement appelé un _paramètre de destructuration_.

**Voici un autre exemple :**

```js
// Définir un tableau avec deux valeurs de chaîne et un tableau imbriqué :
const profile = ["codesweetly.com", "Male", ["Oluwatobi", "Sofela"]];

// Définir une fonction avec deux tableaux de destructuration contenant chacun un paramètre :
function getUserBio([website, , [userName]]) {
  return `${userName} runs ${website}`;
}

// Invoquer getUserBio en passant le tableau profile comme argument :
getUserBio(profile);

// L'invocation ci-dessus retournera :
"Oluwatobi runs codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-gvzqak?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé deux paramètres de destructuration de tableau pour extraire les valeurs du tableau `profile` dans les paramètres `website` et `userName` de `getUserBio`.

Il arrive que vous deviez invoquer une fonction contenant un paramètre de destructuration sans passer d'argument. Dans ce cas, vous devrez utiliser une technique qui empêche le navigateur de lancer une `TypeError`.

Apprenons cette technique ci-dessous.

### Comment invoquer une fonction contenant des paramètres de destructuration de tableau sans fournir d'argument

Considérez la fonction ci-dessous :

```js
function getUserBio([firstName]) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Maintenant, invoquons la fonction `getUserBio` sans passer d'argument à son paramètre de destructuration :

```js
getUserBio();
```

[**Essayez-le sur CodeSandBox**](https://codesandbox.io/s/wrong-way-to-invoke-a-function-containing-an-array-destructuring-parameter-vtdrl)

Après avoir invoqué la fonction `getUserBio` ci-dessus, le navigateur lancera une erreur similaire à `TypeError: undefined is not iterable`.

Le message `TypeError` se produit parce que les fonctions contenant un paramètre de destructuration s'attendent à ce que vous fournissiez au moins un argument.

Ainsi, vous pouvez éviter de tels messages d'erreur en assignant un argument par défaut au paramètre de destructuration.

**Voici un exemple :**

```js
function getUserBio([firstName] = []) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Remarquez dans l'extrait ci-dessus que nous avons assigné un tableau vide comme argument par défaut du paramètre de destructuration.

Ainsi, invoquons maintenant la fonction `getUserBio` sans passer d'argument à son paramètre de destructuration :

```js
getUserBio();
```

La fonction produira :

```js
"Do something else that does not need the destructuring parameter."
"My name is undefined."
```

[**Essayez-le sur CodeSandBox**](https://codesandbox.io/s/the-correct-way-to-invoke-a-function-containing-an-array-destructuring-parameter-voo50?file=/src/index.js)

Gardez à l'esprit que vous n'avez pas à utiliser un tableau vide comme argument par défaut du paramètre de destructuration. Vous pouvez utiliser toute autre valeur qui n'est pas `null` ou `undefined`.

Maintenant que nous savons comment fonctionne la destructuration de tableaux, discutons de la destructuration d'objets afin de voir les différences.

## Qu'est-ce que la destructuration d'objets en JavaScript ?

La **destructuration d'objets** est une technique unique qui permet d'extraire proprement les valeurs d'un objet dans de nouvelles variables.

Par exemple, sans utiliser la technique d'affectation par destructuration d'objets, nous extrairions les valeurs d'un objet dans une nouvelle variable comme suit :

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const firstName = profile.firstName;
const lastName = profile.lastName;
const website = profile.website;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-3tyjgy?file=script.js)

Remarquez que l'extrait ci-dessus contient beaucoup de code répété, ce qui n'est pas une manière DRY (**D**on't **R**epeat **Y**ourself) de coder.

Voyons maintenant comment l'affectation par destructuration d'objets rend les choses plus propres et DRY.

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName: firstName, lastName: lastName, website: website } = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-begth4?file=script.js)

Vous voyez, comme par magie, nous avons nettoyé notre code en plaçant les trois nouvelles variables dans un objet de propriétés (`{...}`) et en leur assignant les valeurs de l'objet `profile`.

En d'autres termes, nous avons instructé l'ordinateur d'extraire les valeurs de l'objet `profile` dans les variables du côté gauche de l'[opérateur d'affectation](https://www.codesweetly.com/javascript-expression#types-of-expressions-in-javascript).

Par conséquent, JavaScript analysera l'objet `profile` et copiera sa première valeur (`"Oluwatobi"`) dans la première variable de l'objet de destructuration (`firstName`).

De même, l'ordinateur extraira la deuxième valeur de l'objet `profile` (`"Sofela"`) dans la deuxième variable de l'objet de destructuration (`lastName`).

Enfin, JavaScript copiera la troisième valeur de l'objet `profile` (`"codesweetly.com"`) dans la troisième variable de l'objet de destructuration (`website`).

Gardez à l'esprit que dans `{ firstName: firstName, lastName: lastName, website: website }`, les clés sont des références aux propriétés de l'objet `profile`—tandis que les valeurs des clés représentent les nouvelles variables.

![Anatomie d'une affectation par destructuration d'objet JavaScript](https://www.freecodecamp.org/news/content/images/2021/11/destructuring-object-anatomy-codesweetly.png)
_L'anatomie d'une affectation par destructuration d'objet JavaScript_

Alternativement, vous pouvez utiliser la syntaxe abrégée pour rendre votre code plus facile à lire.

**Voici un exemple :**

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName, lastName, website } = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-4nhtlt?file=script.js)

Dans l'extrait ci-dessus, nous avons raccourci `{ firstName: firstName, age: age, gender: gender }` en `{ firstName, age, gender }`. Vous pouvez en apprendre plus sur la technique abrégée [ici](https://alligator.io/js/object-property-shorthand-es6/).

Observez que les extraits ci-dessus ont illustré comment assigner la valeur d'un objet à une variable lorsque la propriété de l'objet et la variable ont le même nom.

Cependant, vous pouvez également assigner la valeur d'une propriété à une variable de nom différent. Voyons comment.

### Comment utiliser la destructuration d'objets lorsque le nom de la propriété diffère de celui de la variable

JavaScript permet d'utiliser la destructuration d'objets pour extraire la valeur d'une propriété dans une variable même si les noms de la propriété et de la variable sont différents.

**Voici un exemple :**

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName: forename, lastName: surname, website: onlineSite } = profile;

console.log(forename); // "Oluwatobi"
console.log(surname); // "Sofela"
console.log(onlineSite); // "codesweetly.com"
console.log(website); // "ReferenceError: website is not defined"
```

**[Essayez-le sur CodeSandBox](https://codesandbox.io/s/how-to-use-object-destructuring-when-the-propertys-name-differs-from-that-of-the-variable-ppohh?file=/src/index.js)**

Dans l'extrait ci-dessus, l'ordinateur a réussi à extraire les valeurs de l'objet `profile` dans les variables nommées `forename`, `surname` et `onlineSite`—même si les propriétés et les variables ont des noms différents.

**Note :** `const { firstName: forename } = profile` est équivalent à `const forename = profile.firstName`.

**Voici un autre exemple :**

```js
const profile = {
  lastName: { familyName: "Sofela" }
};

const { lastName: { familyName: surname } } = profile;

console.log(surname); // "Sofela"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-nbnqcl?file=script.js)

Dans l'extrait ci-dessus, l'ordinateur a réussi à extraire la valeur de l'objet `profile` dans la variable `surname`—même si la propriété et la variable ont des noms différents.

**Note :** `const { lastName: { familyName: surname } } = profile` est équivalent à `const surname = profile.lastName.familyName`.

Remarquez que jusqu'à présent, nous avons destructuré l'objet `profile` en le référençant. Cependant, vous pouvez également faire une destructuration directe d'un objet. Voyons comment.

### Comment faire une destructuration directe d'objet

JavaScript permet la destructuration directe d'un objet de propriétés comme suit :

```js
const { firstName, lastName, website } = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-vspaeg?file=script.js)

Supposons que vous préférez séparer vos déclarations de variables de leurs affectations. Dans ce cas, JavaScript vous couvre. Voyons comment.

### Comment utiliser la destructuration d'objets tout en séparant les déclarations de variables de leurs affectations

Lorsque vous utilisez la destructuration d'objets, JavaScript vous permet de séparer vos déclarations de variables de leurs affectations.

**Voici un exemple :**

```js
// Déclarer trois variables :
let firstName, lastName, website;

// Extraire les valeurs vers les trois variables ci-dessus :
({ firstName, lastName, website } = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
});

// Invoquer les trois variables :
console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-3fmanq?file=script.js)

**Note :**

* Assurez-vous d'encadrer l'affectation par destructuration d'objet dans des parenthèses. En faisant cela, l'ordinateur saura que la destructuration d'objet est un littéral d'objet, et non un bloc.
* Placez un point-virgule (`;`) après les parenthèses d'une affectation par destructuration d'objet. En faisant cela, vous empêcherez l'ordinateur d'interpréter les parenthèses comme un invocateur de fonction qui pourrait se trouver sur la ligne précédente.

Que faire si vous voulez que `"Oluwatobi"` soit assigné à la variable `firstName` et que le reste des valeurs de l'objet soit assigné à une autre variable ? Comment pouvez-vous faire cela ? Découvrons-le ci-dessous.

### Comment utiliser la destructuration d'objets pour assigner le reste d'un objet à une variable

JavaScript permet d'utiliser l'[opérateur rest](https://www.codesweetly.com/javascript-rest-operator/) dans un objet de destructuration pour assigner le reste d'un littéral d'objet à une variable.

**Voici un exemple :**

```js
const { firstName, ...otherInfo } = {
  firstName: "Oluwatobi",
  lastName: "Sofela",
  website: "codesweetly.com"
};

console.log(firstName); // "Oluwatobi"
console.log(otherInfo); // {lastName: "Sofela", website: "codesweetly.com"}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-hksus5?file=script.js)

**Note :** Utilisez toujours l'opérateur rest comme dernier élément de votre objet de destructuration pour éviter d'obtenir une `SyntaxError`.

Parfois, la valeur que vous souhaitez extraire d'un objet de propriétés est `undefined`. Dans ce cas, JavaScript fournit un moyen de définir des valeurs par défaut dans l'objet de destructuration. Apprenons-en plus à ce sujet ci-dessous.

### Comment les valeurs par défaut fonctionnent dans une affectation par destructuration d'objet

Définir une valeur par défaut peut être utile lorsque la valeur que vous souhaitez extraire d'un objet n'existe pas (ou est définie sur `undefined`).

Voici comment vous pouvez en définir une à l'intérieur d'un objet de destructuration de propriétés :

```js
const { firstName = "Tobi", website = "CodeSweetly" } = {
  firstName: "Oluwatobi"
};

console.log(firstName); // "Oluwatobi"
console.log(website); // "CodeSweetly"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-pnjh9a?file=script.js)

Dans l'extrait ci-dessus, nous avons défini `"Tobi"` et `"CodeSweetly"` comme valeurs par défaut des variables `firstName` et `website`.

Par conséquent, dans notre tentative d'extraire la valeur de la deuxième propriété de l'objet du côté droit, l'ordinateur a utilisé la valeur par défaut `"CodeSweetly"`—parce qu'il n'existe qu'une seule propriété dans `{firstName: "Oluwatobi"}`.

Alors, que faire si vous devez échanger la valeur de `firstName` avec celle de `website` ? Encore une fois, vous pouvez utiliser la destructuration d'objets pour accomplir cela. Voyons comment ci-dessous.

### Comment utiliser la destructuration d'objets pour échanger des valeurs

Vous pouvez utiliser l'affectation par destructuration d'objets pour échanger les valeurs de deux ou plusieurs variables différentes.

**Voici un exemple :**

```js
let firstName = "Oluwatobi";
let website = "CodeSweetly";

({ firstName, website } = {firstName: website, website: firstName});

console.log(firstName); // "CodeSweetly"
console.log(website); // "Oluwatobi"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-fmyerw?file=script.js)

L'extrait ci-dessus a utilisé la destructuration directe d'objet pour réaffecter les variables `firstName` et `website` avec les valeurs du littéral d'objet du côté droit de l'opérateur d'affectation.

Ainsi, la valeur de `firstName` changera de `"Oluwatobi"` à `"CodeSweetly"`. Tandis que le contenu de `website` changera de `"CodeSweetly"` à `"Oluwatobi"`.

Gardez à l'esprit que vous pouvez également utiliser la destructuration d'objets pour extraire des valeurs de propriétés vers les paramètres d'une fonction. Parlons-en plus ci-dessous.

### Comment utiliser la destructuration d'objets pour extraire des valeurs de propriétés vers les paramètres d'une fonction

Voici comment vous pouvez utiliser la destructuration d'objets pour copier la valeur d'une propriété vers les paramètres d'une fonction :

```js
// Définir un objet avec deux propriétés :
const profile = {
  firstName: "Oluwatobi",
  lastName: "Sofela",
};

// Définir une fonction avec un objet de destructuration contenant deux paramètres :
function getUserBio({ firstName, lastName }) {
  return `My name is ${firstName} ${lastName}.`;
}

// Invoquer getUserBio en passant l'objet profile comme argument :
getUserBio(profile);

// L'invocation ci-dessus retournera :
"My name is Oluwatobi Sofela."
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-aucght?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé un paramètre de destructuration d'objet pour copier les valeurs de l'objet `profile` dans les paramètres `firstName` et `lastName` de `getUserBio`.

**Note :** Un paramètre de destructuration d'objet est typiquement appelé un _paramètre de destructuration_.

**Voici un autre exemple :**

```js
// Définir un objet avec trois propriétés parent :
const profile = {
  website: "codesweetly.com",
  gender: "Male",
  fullName: {
    firstName: "Oluwatobi",
    lastName: "Sofela"
  }
};

// Définir une fonction avec deux objets de destructuration contenant chacun un paramètre :
function getUserBio({ website, fullName: { firstName: userName } }) {
  return `${userName} runs ${website}`;
}

// Invoquer getUserBio en passant l'objet profile comme argument :
getUserBio(profile);

// L'invocation ci-dessus retournera :
"Oluwatobi runs codesweetly.com"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-g2n2a6?file=script.js)

Dans l'extrait ci-dessus, nous avons utilisé deux paramètres de destructuration pour copier les valeurs de l'objet `profile` dans les paramètres `website` et `userName` de `getUserBio`.

**Note :** Si vous n'êtes pas clair sur le paramètre de destructuration ci-dessus, vous pouvez mieux le comprendre en révisant [cette section](#heading-comment-utiliser-la-destructuration-dobjets-lorsque-le-nom-de-la-propriete-differe-de-celui-de-la-variable).

Il arrive que vous deviez invoquer une fonction contenant un paramètre de destructuration sans passer d'argument. Dans ce cas, vous devrez utiliser une technique qui empêche le navigateur de lancer une `TypeError`.

Apprenons cette technique ci-dessous.

### Comment invoquer une fonction contenant des paramètres destructurés sans fournir d'argument

Considérez la fonction ci-dessous :

```js
function getUserBio({ firstName }) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Maintenant, invoquons la fonction `getUserBio` sans passer d'argument à son paramètre de destructuration :

```js
getUserBio();
```

[**Essayez-le sur CodeSandBox**](https://codesandbox.io/s/wrong-way-to-invoke-a-function-containing-an-object-destructuring-parameter-c1hdx?file=/src/index.js)

Après avoir invoqué la fonction `getUserBio` ci-dessus, le navigateur lancera une erreur similaire à `TypeError: (destructured parameter) is undefined`.

Le message `TypeError` se produit parce que les fonctions contenant un paramètre de destructuration s'attendent à ce que vous fournissiez au moins un argument.

Ainsi, vous pouvez éviter de tels messages d'erreur en assignant un argument par défaut au paramètre de destructuration.

**Voici un exemple :**

```js
function getUserBio({ firstName } = {}) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Remarquez que dans l'extrait ci-dessus, nous avons assigné un objet vide comme argument par défaut du paramètre de destructuration.

Ainsi, invoquons maintenant la fonction `getUserBio` sans passer d'argument à son paramètre de destructuration :

```js
getUserBio();
```

La fonction produira :

```js
"Do something else that does not need the destructuring parameter."
"My name is undefined."
```

**[Essayez-le sur CodeSandBox](https://codesandbox.io/s/the-correct-way-to-invoke-a-function-containing-an-object-destructuring-parameter-7kvum?file=/src/index.js)**

Gardez à l'esprit que vous n'avez pas à utiliser un objet vide comme argument par défaut du paramètre de destructuration. Vous pouvez utiliser toute autre valeur qui n'est pas `null` ou `undefined`.

## Conclusion

La destructuration de tableaux et d'objets fonctionne de manière similaire. La principale différence entre les deux affectations par destructuration est la suivante :

* La destructuration de tableaux extrait des valeurs d'un tableau. Mais la destructuration d'objets extrait des valeurs d'un objet JavaScript.

## Aperçu

Cet article a discuté de la manière dont la destructuration de tableaux et d'objets fonctionne en JavaScript. Nous avons également examiné la principale différence entre les deux affectations par destructuration.

Merci d'avoir lu !

### Et voici une ressource utile sur ReactJS :

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✔
* Il contient des extraits de code interactifs ✔
* Il contient des projets évolutifs ✔
* Il contient de nombreux exemples faciles à comprendre ✔

Le livre [React Explained Clearly](https://amzn.to/30iVPIG) est tout ce dont vous avez besoin pour comprendre ReactJS.

[Cliquez ici pour obtenir votre copie](https://amzn.to/30iVPIG)

[![Livre React Explained Clearly maintenant disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2021/11/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela-1.jpg)](https://amzn.to/30iVPIG)