---
title: Explication des types TypeScript – Un modèle mental pour vous aider à penser
  en types
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T11:05:00.000Z'
originalURL: https://freecodecamp.org/news/a-mental-model-to-think-in-typescript-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/cover.jpg
tags:
- name: compilers
  slug: compilers
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: programming languages
  slug: programming-languages
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Explication des types TypeScript – Un modèle mental pour vous aider à penser
  en types
seo_desc: 'By TK

  One day I came across this tweet from Lari Mazza:


  As a software engineer who learned Python, Ruby, JavaScript, and Clojure first,
  when I tried C++ it was a horror movie. I couldn''t do much, and it was so counterproductive
  and frustrating. Mayb...'
---

Par TK

Un jour, je suis tombé sur ce [tweet](https://twitter.com/larimaza/status/1275747670989176833) de Lari Mazza :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/typescript.png)

En tant qu'ingénieur logiciel ayant appris Python, Ruby, JavaScript et Clojure en premier, lorsque j'ai essayé C++, c'était un film d'horreur. Je ne pouvais pas faire grand-chose, et c'était si contre-productif et frustrant. Peut-être parce que je faisais tout de travers et que je ne comprenais pas les types de la bonne manière.

Mais même si j'avais tant de problèmes, j'ai pu implémenter un tas d'[algorithmes et de structures de données](https://github.com/leandrotk/algorithms).

Maintenant que j'utilise de plus en plus TypeScript dans mon travail quotidien et [mes projets parallèles](https://github.com/leandrotk/laziness), je me sens plus préparé à affronter les types. En fait, pas affronter, mais les utiliser en ma faveur.

Ce post est ma tentative d'aider les développeurs à penser davantage en types et à comprendre ce modèle mental.

## Penser en types JavaScript

Si vous êtes ici, vous avez probablement entendu dire que TypeScript est un sur-ensemble de JavaScript. Si ce n'est pas le cas, tant mieux, vous venez d'apprendre quelque chose de nouveau aujourd'hui. YAY !

TypeScript est un sur-ensemble car tout code JavaScript est valide en TypeScript, syntaxiquement parlant. Il peut ou non compiler en fonction de la configuration du compilateur TypeScript. Mais en termes de syntaxe, cela fonctionne très bien.

C'est pourquoi vous pouvez migrer JavaScript vers TypeScript progressivement en remplaçant simplement l'extension `.js` par `.ts`. Tout sera sans déclarations de type (le type `any`), mais c'est une autre histoire.

De plus, si vous codez en JavaScript - ou dans tout autre langage de programmation - vous pensez probablement en types :

* "Hmm, c'est une liste d'entiers, donc je vais devoir filtrer uniquement les nombres pairs et retourner une nouvelle liste"
* "C'est un objet, mais je dois juste obtenir cette valeur de chaîne à partir de la propriété X"
* "Cette fonction reçoit deux paramètres. A et B sont tous deux des entiers et je veux les additionner"

Oui, vous voyez l'idée. Nous pensons en types. Mais ils sont juste dans nos têtes. Nous pensons constamment à eux parce que nous devons savoir comment gérer, analyser ou modifier les données. Nous devons savoir quelles méthodes nous sommes autorisés à utiliser dans ce type d'objet.

Pour donner un exemple plus concret, imaginez que vous voulez additionner le prix de tous les produits. Un objet produit ressemble à ceci :

```typescript
const product = {
  title: 'Some product',
  price: 100.00,
};
```

Mais maintenant avec une liste de produits :

```typescript
const products = [
  {
    title: 'Product 1',
    price: 100.00,
  },
  {
    title: 'Product 2',
    price: 25.00,
  },
  {
    title: 'Product 3',
    price: 300.00,
  }
];
```

Ok ! Maintenant nous voulons une fonction pour additionner tous les prix des produits.

```typescript
function sumAllPrices(products) {
  return products.reduce((sum, product) => sum + product.price, 0);
};

sumAllPrices(products); // 425
```

Il suffit de recevoir les produits en tant qu'argument et de réduire tous les prix des produits. JavaScript fonctionne très bien. Mais en construisant cette fonction, vous commencez à penser aux données et à la manière de les gérer correctement.

La première partie : les produits en tant qu'argument. Ici, vous pensez simplement : "eh bien, nous recevons une liste de certains objets". Oui, dans nos têtes, les produits sont une liste. C'est pourquoi nous pouvons penser à utiliser la méthode `reduce`. C'est une méthode du prototype `Array`.

Ensuite, nous pouvons penser à l'objet en détail. Nous savons que l'objet produit a une propriété `price`. Et cette propriété est un nombre. C'est pourquoi nous pouvons faire `product.price` et additionner avec l'accumulateur.

Récapitulons :

* `products` est une liste d'objets.
* En tant que liste, nous pouvons utiliser la méthode `reduce`, car cette méthode est un membre du prototype `Array`.
* L'objet `produce` a certaines propriétés. L'une d'entre elles est `price`, qui est un nombre.
* En tant que propriété numérique, nous pouvons l'utiliser pour additionner avec l'accumulateur reduce.
* Nous voulions retourner un nombre, la somme de tous les prix des produits.

Nous pensons toujours aux types de données, nous devons simplement ajouter les annotations de type pour les rendre plus explicites et demander de l'aide au compilateur. Notre mémoire est limitée et les compilateurs sont là pour nous aider, nous les humains.

Le système de types ne rendra pas seulement nos données plus cohérentes, mais il peut également fournir une autocomplétion pour les types de données. Il connaît les types, donc il peut montrer les membres pour les données. Nous examinerons cette idée plus tard. Ici, je voulais juste montrer que nous pensons en types dans nos têtes.

## Types Simples & Utilisations Simples

Nous sommes donc prêts à utiliser certains langages de programmation fortement typés comme TypeScript. Nous devons simplement ajouter explicitement des annotations de type à nos structures de données. C'est simple, non ?

Mais parfois, ce n'est pas si facile (habituellement, ce n'est pas facile lorsque vous venez de langages à typage dynamique. Vous vous sentez improductif. Cela ressemble à une bataille contre les types). L'idée ici est de rendre cette courbe d'apprentissage plus douce et plus amusante.

Ici, nous verrons de nombreux exemples sur la façon d'utiliser les types en TypeScript. Nous commencerons par des exemples faciles et simples et les rendrons progressivement plus complexes tout en concevant le modèle mental pour penser en types.

Comme en JavaScript, TypeScript possède également des types de données de base comme `number`, `string`, `boolean`, `null`, etc. Vous pouvez trouver tous les types de données de base dans la [Documentation TypeScript](https://www.typescriptlang.org/docs/handbook/basic-types.html).

Avec ces unités de données, nous pouvons rendre nos programmes plus utiles. Pour être plus pratique, prenons un exemple simple. Une fonction `sum`.

Comment cela fonctionne-t-il en JavaScript ?

```typescript
function sum(a, b) {
  return a + b;
}
```

Tout est correct ? Bien.

Maintenant, utilisons-la :

```typescript
sum(1, 2); // 3
sum(2, 2); // 4
sum(0, 'string'); // '0string'   WTF !
```

Les deux premiers appels sont ce que nous attendons dans notre système. Mais JavaScript est très flexible, il nous permet de fournir n'importe quelle valeur à cette fonction.

Le dernier appel est bizarre. Nous pouvons appeler avec une chaîne, mais cela retournera un résultat inattendu. Cela ne casse pas en développement, mais cela entraînera un comportement étrange à l'exécution.

Que voulons-nous ? Nous voulons ajouter certaines contraintes à la fonction. Elle ne pourra recevoir que des nombres. De cette façon, nous réduisons la possibilité d'avoir des comportements inattendus. Et le type de retour de la fonction est également un nombre.

```typescript
function sum(a: number, b: number): number {
  return a + b;
}
```

Génial ! C'était très simple. Appelons à nouveau.

```typescript
sum(1, 2); // 3
sum(2, 2); // 4
sum(0, 'string'); // Argument of type '"string"' is not assignable to parameter of type 'number'.
```

En annotant notre fonction, nous fournissons des informations au compilateur pour voir si tout est correct. Il suivra les contraintes que nous avons ajoutées à la fonction.

Ainsi, les deux premiers appels sont les mêmes qu'en JavaScript. Il retournera le calcul correct. Mais dans le dernier, nous avons une erreur à la compilation. C'est important. L'erreur se produit maintenant à la compilation et nous empêche d'envoyer du code incorrect en production. Il indique que le type `string` ne fait pas partie de l'ensemble des valeurs dans l'univers du type `number`.

Pour les types de base, nous devons simplement ajouter un deux-points suivi de la définition du type.

```typescript
const isTypescript: boolean = true;
const age: number = 24;
const username: string = 'tk';
```

Maintenant, augmentons le défi. Vous souvenez-vous du code de l'objet produit que nous avons écrit en JavaScript ? Implémentons-le à nouveau, mais maintenant avec l'état d'esprit TypeScript.

Juste pour rappeler de quoi nous parlons :

```typescript
const product = {
  title: 'Some product',
  price: 100.00,
};
```

C'est la valeur du produit. Il a un `title` de type `string` et le `price` de type `number`. Pour l'instant, c'est tout ce que nous devons savoir.

Le type de l'objet serait quelque chose comme ceci :

```typescript
{ title: string, price: number }
```

Et nous utilisons ce type pour annoter notre fonction :

```typescript
const product: { title: string, price: number } = {
  title: 'Some product',
  price: 100.00,
};
```

Avec ce type, le compilateur saura comment gérer les données incohérentes :

```typescript
const wrongProduct: { title: string, price: number } = {
  title: 100.00, // Type 'number' is not assignable to type 'string'.
  price: 'Some product', // Type 'string' is not assignable to type 'number'.
};
```

Ici, cela se décompose en deux propriétés différentes :

* Le `title` est une `string` et ne doit pas recevoir un `number`.
* Le `price` est un `number` et ne doit pas recevoir une `string`.

Le compilateur nous aide à attraper des erreurs de type comme celle-ci.

Nous pourrions améliorer cette annotation de type en utilisant un concept appelé `Type Aliases`. C'est une façon de créer un nouveau nom pour un type spécifique.

Dans notre cas, le type de produit pourrait être :

```typescript
type Product = {
  title: string;
  price: number;
};

const product: Product = {
  title: 'Some product',
  price: 100.00,
};
```

C'est mieux pour visualiser le type, ajouter de la sémantique, et peut-être le réutiliser dans notre système.

Maintenant que nous avons ce type de produit, nous pouvons l'utiliser pour typer la liste des produits. La syntaxe ressemble à ceci : `MyType[]`. Dans notre cas, `Product[]`.

```typescript
const products: Product[] = [
  {
    title: 'Product 1',
    price: 100.00,
  },
  {
    title: 'Product 2',
    price: 25.00,
  },
  {
    title: 'Product 3',
    price: 300.00,
  }
];
```

Maintenant, la fonction `sumAllPrices`. Elle recevra le produit et retournera un nombre, la somme de tous les prix des produits.

```typescript
function sumAllPrices(products: Product[]): number {
  return products.reduce((sum, product) => sum + product.price, 0);
};
```

C'est très intéressant. Comme nous avons typé le produit, lorsque nous écrivons `product.`, il montrera les propriétés possibles que nous pouvons utiliser. Dans le cas du type de produit, il montrera les propriétés `price` et `title`.

```typescript
sumAllPrices(products); // 425
sumAllPrices([]); // 0
sumAllPrices([{ title: 'Test', willFail: true }]); // Type '{ title: string; willFail: true; }' is not assignable to type 'Product'.
```

Passer les `products` donnera le résultat `425`. Une liste vide donnera le résultat `0`. Et si nous passons un objet avec une structure différente - TypeScript a un système de types structurel et nous approfondirons ce sujet plus tard - le compilateur lancera une erreur de type indiquant que la structure ne fait pas partie du type `Product`.

## Typage Structurel

Le typage structurel est un type de compatibilité de types. C'est une façon de comprendre la compatibilité entre les types en fonction de leur structure : caractéristiques, membres, propriétés. Certains langages ont une compatibilité de types basée sur les noms des types, et cela s'appelle le typage nominal.

Par exemple, en Java, même si différents types ont la même structure, cela lancera une erreur de compilation car nous utilisons un type différent pour instancier et définir une nouvelle instance.

```typescript
class Person {
  String name;
}

class Client {
  String name;
}

Client c = new Person();  // compiler throws an error
Client c = new Client();  // OK!
```

Dans les systèmes de types nominaux, la partie pertinente d'un type est le nom, pas la structure.

TypeScript, en revanche, vérifie la compatibilité structurelle pour autoriser ou non des données spécifiques. Son système de types est basé sur le typage structurel.

Le même code d'implémentation qui plante en Java fonctionnerait en TypeScript.

```typescript
class Person {
  name: string;
}

class Client {
  name: string;
}

const c1: Client = new Person(); // OK!
const c2: Client = new Client(); // OK!
```

Nous voulons utiliser le type `Client`, qui a la propriété `name`, pour pointer vers le type `Person`. Il a également le type de propriété. Donc TypeScript comprendra que les deux types ont la même forme.

Mais ce n'est pas seulement pour les classes, cela fonctionne pour tout autre "objet".

```typescript
const c3: Client = {
  name: 'TK'
};
```

Ce code compile également car nous avons la même structure ici. Le système de types TypeScript ne se soucie pas de savoir s'il s'agit d'une classe ou d'un littéral d'objet, s'il a les mêmes membres, il sera flexible et compilera.

Mais maintenant, nous allons ajouter un troisième type : le `Customer`.

```typescript
class Customer {
  name: string;
  age: number;
};
```

Il n'a pas seulement la propriété `name`, mais aussi `age`. Que se passerait-il si nous instancions une instance `Client` dans une constante de type `Customer` ?

```typescript
const c4: Customer = new Client();
```

Le compilateur n'acceptera pas cela. Nous voulons utiliser `Customer`, qui a `name` et `age`. Mais nous instancions `Client` qui n'a que la propriété `name`. Donc il n'a pas la même forme. Cela provoquera une erreur :

```bash
Property 'age' is missing in type 'Client' but required in type 'Customer'.
```

L'inverse fonctionnerait car nous voulons `Client`, et `Customer` a toutes les propriétés (`name`) de `Client`.

```typescript
const c5: Client = new Customer();
```

Cela fonctionne très bien !

Nous pourrions continuer avec les énumérations, les littéraux d'objets et tout autre type, mais l'idée ici est de comprendre que la structure du type est la partie pertinente.

## Runtime et Compile time

C'est un sujet beaucoup plus complexe dans la théorie des langages de programmation, mais je voulais donner quelques exemples pour distinguer le runtime du compile time.

En gros, le runtime est le temps d'exécution d'un programme. Imaginez votre backend recevant des données d'une page de formulaire frontend, traitant ces données et les sauvegardant. Ou lorsque votre frontend demande des données à un serveur pour rendre une liste de ~~Pokemons~~ produits.

Le compile time est essentiellement lorsque le compilateur exécute des opérations dans le code source pour satisfaire les exigences du langage de programmation. Il peut inclure la vérification de type comme une opération, par exemple.

Les erreurs de compilation en TypeScript, par exemple, sont très liées au code que nous avons écrit auparavant :

* Lorsque le type manque de propriété : `Property 'age' is missing in type 'Client' but required in type 'Customer'.`
* Lorsque le type ne correspond pas : `Type '{ title: string; willFail: true; }' is not assignable to type 'Product'.`

Regardons quelques exemples pour mieux comprendre.

Je veux écrire une fonction pour obtenir l'index d'une partie du langage de programmation passé.

```typescript
function getIndexOf(language, part) {
  return language.indexOf(part);
}
```

Elle reçoit le `language` et la `part` que nous allons chercher pour obtenir l'index.

```typescript
getIndexOf('Typescript', 'script'); // 4
getIndexOf(42, 'script'); // Uncaught TypeError: language.indexOf is not a function at getIndexOf
```

Lorsque vous passez une chaîne, cela fonctionne bien. Mais en passant un nombre, nous obtenons une erreur de runtime `Uncaught TypeError`. Parce qu'un nombre n'a pas de fonction `indexOf`, donc nous ne pouvons pas vraiment l'utiliser.

Mais si nous donnons des informations de type au compilateur, à la compilation, il lancera une erreur avant d'exécuter le code.

```typescript
function getIndexOf(language: string, part: string): number {
  return language.indexOf(part);
}
```

Maintenant, notre programme sait qu'il devra recevoir deux chaînes et retourner un nombre. Le compilateur peut utiliser ces informations pour lancer des erreurs lorsque nous obtenons une erreur de type... avant le runtime.

```typescript
getIndexOf('Typescript', 'script'); // 4
getIndexOf(42, 'script'); // Argument of type '42' is not assignable to parameter of type 'string'.
```

Peut-être que pour les petits projets (ou les petites fonctions comme les nôtres), nous ne voyons pas vraiment beaucoup d'avantages.

Dans ce cas, nous savons que nous devons passer une chaîne, donc nous ne passerons pas de nombre à la fonction. Mais lorsque la base de code grandit ou que vous avez beaucoup de personnes ajoutant du code et plus de complexité, il est clair pour moi qu'un système de types peut nous aider beaucoup à obtenir des erreurs à la compilation avant d'envoyer du code en production.

Au début, nous avons besoin de toute la courbe d'apprentissage pour comprendre les types et tous les modèles mentaux, mais après un certain temps, vous serez plus habitué aux annotations de type et finirez par devenir ami avec le compilateur. Ce serait un _helper_, pas un _yeller_.

Alors que nous apprenons la différence de base entre le compile time et le runtime, je pense qu'il est bon de différencier les types des valeurs.

Tous les exemples que je vais montrer ici peuvent être copiés et exécutés dans le [TypeScript Playground](https://www.typescriptlang.org/play) pour comprendre le compilateur et le résultat du processus de compilation (aka le _"JavaScript"_).

En TypeScript, nous avons deux univers différents : l'espace des valeurs et l'espace des types. L'espace des types est où les types sont définis et utilisés pour permettre au compilateur de faire toute la magie. Et l'espace des valeurs est les valeurs dans nos programmes comme les variables, les constantes, les fonctions, les littéraux de valeurs, et les choses que nous avons au runtime.

Il est bon d'avoir une compréhension de ce concept car en TypeScript nous ne pouvons pas utiliser la vérification de type au runtime. Il a une séparation très claire entre la vérification de type et le processus de compilation.

TypeScript a le processus de vérification de type des types de code source et voit si tout est correct et cohérent. Et puis il peut compiler en JavaScript.

Comme ces deux parties sont séparées, nous ne pouvons pas utiliser la vérification de type au runtime. Seulement en "compile time". Si vous essayez d'utiliser un type comme une valeur, il lancera une erreur : `only refers to a type, but is being used as a value here`.

Regardons des exemples de cette idée.

Imaginez que nous voulons écrire une fonction appelée `purchase` où nous recevons un mode de paiement et en fonction de ce mode, nous voulons effectuer une action. Nous avons une carte de crédit et une carte de débit. Définissons-les ici :

```typescript
type CreditCard = {
  number: number;
  cardholder: string;
  expirationDate: Date;
  secutiryCode: number;
};

type DebitCard = {
  number: number;
  cardholder: string;
  expirationDate: Date;
  secutiryCode: number;
};

type PaymentMethod = CreditCard | DebitCard;
```

Ces types sont dans l'_espace des types_, donc cela ne fonctionne qu'à la compilation. Après la vérification de type de cette fonction, le compilateur supprime tous les types.

Si vous ajoutez ces types dans le TypeScript Playground, la sortie sera uniquement une définition stricte `"use strict";`.

L'idée ici est de vraiment comprendre que les types vivent dans l'_espace des types_ et ne seront pas disponibles au runtime. Donc dans notre fonction, il ne sera pas possible de faire ceci :

```typescript
const purchase = (paymentMethod: PaymentMethod) => {
  if (paymentMethod instanceof CreditCard) {
    // purchase with credit card
  } else {
    // purchase with debit card
  }
}
```

Dans le compilateur, il lance une erreur : `'CreditCard' only refers to a type, but is being used as a value here.`.

Le compilateur connaît la différence entre les deux espaces et que le type `CreditCard` vit dans l'_espace des types_.

Le playground est un outil très cool pour voir la sortie de votre code TypeScript. Si vous créez un nouvel objet de carte de crédit comme ceci :

```typescript
const creditCard: CreditCard = {
  number: 2093,
  cardholder: 'TK',
  expirationDate: new Date(),
  secutiryCode: 101
};
```

Le compilateur vérifiera le type et fera toute la magie puis transpilera le code TypeScript en JavaScript. Et nous avons ceci :

```typescript
const creditCard = {
    number: 2093,
    cardholder: 'TK',
    expirationDate: new Date(,
    secutiryCode: 101
};
```

Le même objet, mais maintenant seulement avec la valeur et sans le type.

## Contraintes & Rétrécissement de Type

Lorsque nous restreignons ce que nous pouvons faire, il est plus facile de comprendre ce que nous pouvons faire.

Nous utilisons les types comme des contraintes pour limiter les bugs dans votre programme. Pour comprendre ce concept, je vole un exemple de la conférence de Lauren Tan sur les systèmes de types.

```typescript
const half = x => x / 2;
```

Combien de façons cette fonction peut-elle échouer ? Imaginez un certain nombre d'entrées possibles :

```typescript
[
  null,
  undefined,
  0,
  '0',
  'TK',
  { username: 'tk' },
  [42, 3.14],
  (a, b) => a + b,
]
```

Et quels sont les résultats pour l'entrée :

```typescript
half(null); // 0
half(undefined); // NaN
half(0); // 0
half('0'); // 0
half('TK'); // NaN
half({ username: 'tk' }); // NaN
half([42, 3.14]); // NaN
half((a, b) => a + b); // NaN
```

Nous avons ici des résultats différents et inattendus. Ici, il est clair que nous voulons un nombre en tant que fonction `half`, faire le calcul, et c'est tout ! Mais parfois nous ne contrôlons pas l'entrée ou la base de code est grande, ou nouvelle/peu familière, et nous sommes capables de faire ces petites erreurs.

L'idée d'ajouter des contraintes à notre code est de réduire les possibilités d'une gamme de types. Dans ce cas, nous voulons limiter le type d'entrée à un type `number`. C'est le seul type qui nous intéresse pour faire le calcul de la moitié. Avec le rétrécissement de type, nous donnons à nouveau des informations de type au compilateur.

```typescript
const half = (x: number) => x / 2;
```

Et avec cette nouvelle information, si nous appelons la fonction avec les cas de test à nouveau, nous avons des résultats différents :

```typescript
half(null); // Argument of type 'null' is not assignable to parameter of type 'number'.
half(undefined); // Argument of type 'undefined' is not assignable to parameter of type 'number'.(
half(0); // 0
half('0'); // Argument of type '"0"' is not assignable to parameter of type 'number'.
half('TK'); // Argument of type '"TK"' is not assignable to parameter of type 'number'.
half({ username: 'tk' }); // Argument of type '{ username: string; }' is not assignable to parameter of type 'number'.
half([42, 3.14]); // Argument of type 'number[]' is not assignable to parameter of type 'number'.
half((a, b) => a + b); // Argument of type '(a: any, b: any) => any' is not assignable to parameter of type 'number'.
```

En gros, le compilateur nous dira que seul le type nombre, dans ce cas, la valeur `0`, est une entrée valide, il compilera et permettra d'exécuter le code. Nous réduisons le type d'entrée et n'autorisons que la valeur que nous voulons vraiment pour cette fonction.

Mais il existe d'autres moyens de réduire les types en TypeScript. Imaginez que nous avons une fonction qui reçoit un paramètre qui peut être soit une chaîne, soit un nombre.

```typescript
type StringOrNumber = string | number;

function stringOrNumber(value: StringOrNumber) {}
```

Dans le corps de la fonction, le compilateur ne saura pas quelles méthodes ou propriétés nous pouvons utiliser pour ce type. Est-ce une chaîne ou un nombre ? Nous ne connaissons la valeur qu'à l'exécution. Mais nous pouvons réduire le type en utilisant le `typeof` :

```typescript
function stringOrNumber(value: StringOrNumber) {
  if (typeof value === 'string') {
    // value.
		// votre ide vous montrera les méthodes possibles du type string
		// (parameter) value: string
    value
  }

  if (typeof value === 'number') {
    // value.
		// votre ide vous montrera les méthodes possibles du type number
		// (parameter) value: number
    value
  }
}
```

Avec une instruction `if` et le `typeof`, nous pouvons donner plus d'informations au compilateur. Maintenant, il connaîtra le type spécifique pour chaque corps de `if`.

L'IDE sait quoi montrer pour le type spécifique. À l'exécution, lorsque la valeur est une chaîne, elle ira à la première instruction `if`, et le compilateur déduira que le type est une chaîne : `(parameter) value: string`.

Lorsque la valeur est un nombre, elle ira à la deuxième instruction `if` et le compilateur déduira qu'un type est un nombre : `(parameter) value: number`.

L'instruction `if` peut être une aide pour le compilateur.

Un autre exemple est lorsque nous avons une propriété optionnelle dans un objet, mais dans une fonction, nous devons retourner une valeur basée sur cette valeur optionnelle.

Imaginez que nous avons ce type :

```typescript
type User = {
  name: string;
  address: {
    street: string;
    complement?: string;
  }
};
```

C'est un type `User` simple. Concentrons-nous sur la propriété `complement`. Elle est optionnelle (regardez de plus près le symbole `?`), ce qui signifie qu'elle peut être une `string` ou `undefined`.

Maintenant, nous voulons construire une fonction pour recevoir l'utilisateur et obtenir la longueur du complément d'adresse. Qu'en est-il de ceci ?

```typescript
function getComplementLength(user: User): number {
  return user.address.complement.length;
	// (property) complement?: string | undefined
  // Object is possibly 'undefined'.
}
```

Comme nous l'avons vu précédemment, le `complement` peut être une `string` ou `undefined`. `undefined` n'a pas vraiment de propriété appelée `length` :

```typescript
Uncaught TypeError: Cannot read property 'length' of undefined
```

Nous pourrions faire quelque chose comme :

```typescript
function getComplementLength(user: User) {
  return user.address.complement?.length;
}
```

Si le `complement` a une valeur de chaîne, nous pouvons appeler `length`, sinon, il retournera `undefined`.

Donc cette fonction a deux types de retour possibles : `number | undefined`. Mais nous voulons nous assurer que nous ne retournons que `number`. Nous utilisons donc une condition `if` ou ternaire pour réduire le type. Il n'appellera `.length` que lorsqu'il a une valeur réelle (ou lorsqu'il n'est pas `undefined`).

```typescript
function getComplementLength(user: User): number {
  return user.address.complement
    ? user.address.complement.length
    : 0;
}
```

Si c'est `undefined`, nous retournons la longueur minimale : `0`. Maintenant, nous pouvons utiliser la fonction avec le bon type de conception avec et sans le complément. Sans erreurs de compilation et d'exécution.

```typescript
getComplementLength({
  name: 'TK',
  address: {
    street: 'Shinjuku Avenue'
  }
}); // 0

getComplementLength({
  name: 'TK',
  address: {
    street: 'Shinjuku Avenue',
    complement: 'A complement'
  }
}); // 12
```

Nous obtiendrons `0` du premier appel de fonction et `12` du deuxième appel.

Avec ce concept `if`, nous pouvons également utiliser d'autres helpers pour faire la même chose. Nous pourrions utiliser l'opérateur `in` pour vérifier une propriété d'un objet, un `Array.isArray` pour vérifier un tableau, ou le `instanceof` pour tout autre type de classe.

Nous pourrions également utiliser des concepts plus avancés comme une fonction d'assertion ou des gardes de type, mais je laisserai ces concepts pour de futurs articles.

Une chose que je veux approfondir dans ce sujet _Contraintes_ est l'immuabilité.

En JavaScript et TypeScript, nous avons l'idée d'objets mutables. Si vous définissez une valeur dans une variable, nous pouvons la réassigner avec une autre valeur plus tard.

```typescript
let email = 'harry.potter@mail.com';
email // 'harry.potter@mail.com'
email = 'hermione.granger@mail.com';
email // 'hermione.granger@mail.com'
```

Maintenant, imaginez que vous avez une liste de nombres. Et vous voulez utiliser une fonction pour additionner tous ses nombres. La fonction ressemble à ceci :

```typescript
function sumNumbers(numbers: number[]) {
  let sum = 0;
  let num = numbers.pop();

  while (num !== undefined) {
    sum += num;
    num = numbers.pop();
  }

  return sum;
}
```

Vous appelez la fonction en passant votre liste et obtenez le résultat. Cela fonctionne très bien.

```typescript
const list = [1, 2, 3, 4];
sumNumbers(list); // 10
```

Mais qu'est-il arrivé à votre liste ? La fonction l'a-t-elle entièrement mutée ?

```typescript
list; // []
```

Si nous utilisons la liste, elle est vide maintenant. Le `pop` dans la fonction `sumNumbers` est une fonction "mutate". Elle obtient les références et supprime l'élément de celles-ci. Ce n'est pas une copie, c'est la référence réelle.

À l'exécution, nous pouvons utiliser d'autres fonctions ou méthodes pour faire la même chose : utiliser reduce, faire une boucle for sans avoir besoin de `pop` des éléments du tableau.

Mais en utilisant TypeScript, nous pouvons fournir de l'immuabilité à la compilation. Si vous n'utilisez pas de types, il est possible d'utiliser une assertion de type `as const`. Imaginez ceci :

```typescript
const author = {
  name: 'Walter Isaacson',
  email: 'walter.isaacson@mail.com',
  books: [
    {
      title: 'Leonardo Da Vinci',
      price: 50.00,
    }
  ]
};

author.books.push({
  title: 'Steve Jobs',
  price: 10.00
});
```

Juste un objet auteur et ensuite nous ajoutons un nouveau livre à cet auteur. La méthode `push` met à jour la référence du tableau de livres. C'est une méthode "mutate". Voyons si vous utilisez l'assertion const `as const` :

```typescript
const author = {
  name: 'Walter Isaacson',
  email: 'walter.isaacson@mail.com',
  books: [
    {
      title: 'Leonardo Da Vinci',
      price: 50.00,
    }
  ]
} as const;

author.books.push({
  title: 'Steve Jobs',
  price: 10.00
});
// Property 'push' does not exist on type
// 'readonly [{ readonly title: "Leonardo Da Vinci"; readonly price: 50; }]'
```

Le compilateur ne compilera pas. Il obtient une erreur sur l'objet de l'auteur. Il est maintenant en lecture seule, et en tant qu'objet en lecture seule, il n'a pas de méthode appelée `push` (ou toute méthode "mutate").

Nous avons ajouté une contrainte à l'objet de l'auteur. Avant, c'était un type spécifique (avec toutes les méthodes "mutate"), et maintenant nous avons réduit le type pour qu'il soit presque le même, mais sans les méthodes "mutate". Rétrécissement de type.

Pour continuer, ajoutons des types à cet objet. Le `book` et l'`author` :

```typescript
type Book = {
  title: string;
  price: number;
};

type Author = {
  name: string;
  email: string;
  books: Book[];
};
```

Ajoutez le type à l'objet author :

```typescript
const author: Author = {
  name: 'Walter Isaacson',
  email: 'walter.isaacson@mail.com',
  books: [
    {
      title: 'Leonardo Da Vinci',
      price: 50.00,
    }
  ]
};
```

Ajoutez le type à un nouvel objet book :

```typescript
const book: Book = {
  title: 'Steve Jobs',
  price: 30
};
```

Et maintenant nous pouvons ajouter le nouveau livre à l'auteur :

```typescript
author.name = 'TK';
author.books.push(book);
```

Cela fonctionne très bien !

Je veux montrer une autre façon d'ajouter de l'immuabilité à la compilation. TypeScript a un type utilitaire appelé `Readonly`.

Vous pouvez ajouter le `readonly` pour chaque propriété dans un objet. Quelque chose comme ceci :

```typescript
type Book = {
  readonly title: string;
  readonly price: number;
};
```

Mais cela peut être très répétitif. Donc nous pouvons utiliser l'utilitaire `Readonly` pour ajouter le `readonly` à toutes les propriétés d'un objet :

```typescript
type Book = Readonly<{
  title: string;
  price: number;
}>;
```

Une chose à garder à l'esprit est qu'il n'ajoute pas le readonly pour les propriétés imbriquées. Par exemple, si nous ajoutons le `Readonly` au type `Author`, il n'ajoutera pas le `readonly` au type `Book` également.

```typescript
type Author = Readonly<{
  name: string;
  email: string;
  books: Book[];
}>;
```

Toutes les propriétés de l'auteur ne peuvent pas être réassignées, mais vous pouvez muter la liste `books` ici (`push`, `pop`, ...) car le `Book[]` n'est pas en lecture seule. Voyons cela.

```typescript
const author: Author = {
  name: 'Walter Isaacson',
  email: 'walter.isaacson@mail.com',
  books: [
    {
      title: 'Leonardo Da Vinci',
      price: 50.00,
    }
  ]
};

const book: Book = {
  title: 'Steve Jobs',
  price: 30
};

author.books.push(book);
author.books;
/* =>
 *
 * [
 *   {
 *     title: 'Leonardo Da Vinci',
 *     price: 50.00,
 *   },
 *   {
 *    title: 'Steve Jobs',
 *    price: 30
 *   }
 * ]
 *
 */
```

Le `push` fonctionnera très bien.

Alors, comment pouvons-nous imposer un readonly aux `books` ? Nous devons nous assurer que le tableau est un type readonly. Nous pouvons utiliser le `Readonly`, ou utiliser un autre utilitaire de TypeScript appelé `ReadonlyArray`. Voyons les deux façons de le faire.

Avec `Readonly` :

```typescript
type Author = Readonly<{
  name: string;
  email: string;
  books: Readonly<Book[]>;
}>;
```

Avec `ReadonlyArray` :

```typescript
type Author = Readonly<{
  name: string;
  email: string;
  books: ReadonlyArray<Book>;
}>;
```

Pour moi, les deux fonctionnent très bien ! Mais à mon avis, `ReadonlyArray` est plus sémantique et je le trouve également moins verbeux (ce n'est pas que le `Readonly` avec un tableau soit verbeux).

Que se passe-t-il si nous essayons de muter l'objet author maintenant ?

```typescript
author.name = 'TK'; // Cannot assign to 'name' because it is a read-only property.
author.books.push(book); // Property 'push' does not exist on type 'readonly [{ readonly title: "Leonardo Da Vinci"; readonly price: 50; }]'.
```

Génial ! Maintenant, nous pouvons attraper les opérations mutables à la compilation. C'est une façon d'utiliser le concept d'ajout de contraintes à nos types pour s'assurer qu'ils ne font que ce qui est vraiment nécessaire.

## Sémantique & Lisibilité

Au début, j'ai senti que TypeScript pouvait être très verbeux à cause des types et rendre le code beaucoup plus complexe qu'il ne devrait l'être. Et c'est effectivement le cas. Strive for simplicity est l'objectif et c'est difficile en même temps.

Cette idée est très liée au code propre et à la manière dont nous pouvons écrire du code pour qu'il soit lisible par les humains et maintenable. TypeScript ne fait pas exception. Dans la plupart des cas, nous n'avons pas besoin de types super complexes. Laissez les types simples faire le travail.

Une autre chose que je trouve très utile est la sémantique des types.

Imaginez que vous devez ajouter une chaîne à la `sessionStorage` pour la sauvegarder dans le navigateur. Votre fonction ressemble à ceci :

```typescript
function saveMyString(value: string): any {
  sessionStorage.myString = value;
}
```

Vous ajoutez une annotation de type à l'entrée de chaîne et comme vous ne connaissez pas le type de retour, vous ajoutez probablement un type `any`.

Mais quelle est la vraie signification derrière ce type de retour ? Est-ce qu'il retourne quelque chose ?

Il sauvegarde simplement la chaîne dans la `sessionStorage`. Il ne retourne rien. Le type `void` était ce que vous cherchiez. Comme le dit la documentation TypeScript : `l'absence d'avoir un type du tout`.

```typescript
function saveMyString(value: string): void {
  sessionStorage.myString = value;
}
```

Génial, la signification du type est correcte maintenant. La justesse est très importante dans un système de types. C'est une façon de modéliser nos données, mais aussi d'aider à maintenir les systèmes pour les développeurs futurs. Même si le développeur est ... vous !

Auparavant, nous parlions de code verbeux. Et nous pouvons améliorer beaucoup de notre code en utilisant l'inférence de type TypeScript.

Pour certains codes, nous n'avons pas besoin d'ajouter explicitement une annotation de type. Le compilateur TypeScript comprendra et l'inférera implicitement. Par exemple :

```typescript
const num: number = 1;
```

Ce code est redondant. Nous pouvons simplement laisser le compilateur l'inférer comme ceci :

```typescript
const num = 1;
```

Dans notre exemple précédent, nous avons ajouté l'annotation `void` à la fonction `saveMyString`. Mais comme la fonction ne retourne aucune valeur, le compilateur inférera que le type de retour est `void` implicitement.

Lorsque j'ai appris cela, je me suis dit. Mais l'un des plus grands avantages de l'utilisation de TypeScript (ou de tout autre système de types / langage à typage statique) est les types en tant que documentation. Si nous laissons le compilateur inférer la plupart des types, nous n'aurons pas la documentation que nous voulons.

Mais si vous survolez le code TypeScript dans votre éditeur (au moins VS Code fonctionne comme ça), vous pouvez voir les informations de type et la documentation pertinente.

Regardons d'autres exemples de code redondant et rendons le code moins verbeux et laissons le compilateur travailler pour nous.

```typescript
function sum(a: number, b: number): number {
  return a + b;
};
```

Nous n'avons pas besoin du type de retour `number`, car le compilateur sait qu'un `number` + un autre `number` est égal à un type `number`, et c'est le type de retour. Cela peut être :

```typescript
function sum(a: number, b: number) {
  return a + b;
};
```

Code implicite, mais avec documentation, et le compilateur fait le travail.

L'inférence de type fonctionne également pour les méthodes :

```typescript
function squareAll(numbers: number[]): number[] {
  return numbers.map(number => number * number);
};
```

Cette fonction prend une liste de nombres et rend chaque nombre une valeur au carré. Le type de retour est `number[]`, même si le résultat d'un map est toujours une liste, et comme nous avons une liste de nombres, ce sera toujours une liste de nombres. Donc nous laissons le compilateur inférer cela aussi :

```typescript
function squareAll(numbers: number[]) {
  return numbers.map(number => number * number);
};
```

Cela fonctionne de la même manière pour les objets aussi.

```typescript
const person: { name: string, age: number } = {
  name: 'TK',
  age: 24
};
```

Un objet personne avec un nom de chaîne et un âge de nombre. Mais comme nous attribuons ces valeurs, le compilateur peut inférer ces types.

```typescript
const person = {
  name: 'TK',
  age: 24
};
```

Si vous survolez la `person`, vous obtenez ceci :

```typescript
const person: {
  name: string;
  age: number;
}
```

Les types sont documentés ici.

Un autre avantage de l'inférence de type est que nous pouvons facilement refactoriser notre code. C'est un exemple simple, mais bon pour illustrer le processus de refactoring. Reprenons la fonction `sum`.

```typescript
function sum(a: number, b: number): number {
  return a + b;
};
```

Au lieu de retourner le nombre de somme, nous voulons retourner `"Sum: {a + b}"`. Donc pour `a = 1` et `b = 2`, nous avons la chaîne résultante comme `"Sum: 3"`.

```typescript
function sum(a: number, b: number): string {
  return `Sum: ${a + b}`;
};

sum(1, 2); // Sum: 3
```

Génial ! Mais maintenant, laissons le compilateur inférer cela.

```typescript
// function sum(a: number, b: number): number
function sum(a: number, b: number) {
  return a + b;
};

// function sum(a: number, b: number): string
function sum(a: number, b: number) {
  return `Sum: ${a + b}`;
};
```

Nous devons simplement modifier la valeur de retour et l'inférence de type fonctionnera. Pas besoin de penser au type de retour. C'est un petit exemple, mais pour des fonctions plus complexes, cela fonctionnerait aussi.

En revenant à la partie lisibilité, nous pouvons utiliser `Enum`. Un utilitaire qui définit un ensemble de constantes nommées. C'est une façon de donner plus de sens aux données dans votre application.

Dans votre application node ou une application frontend, vous effectuez probablement des requêtes pour demander des données. Vous utilisez couramment un objet fetch pour effectuer une requête et parfois vous devez passer les en-têtes d'acceptation.

```typescript
fetch('/pokemons', {
  headers: {
    Accept: 'application/json'
  }
});

fetch('/harry-potter/spells', {
  headers: {
    Accept: 'application/json'
  }
});
```

C'est bien, mais nous pouvons également utiliser une énumération pour séparer cette chaîne d'acceptation dans une constante et la réutiliser.

```typescript
enum MediaTypes {
  JSON = 'application/json'
}

fetch('/pokemons', {
  headers: {
    Accept: MediaTypes.JSON
  }
});

fetch('/harry-potter/spells', {
  headers: {
    Accept: MediaTypes.JSON
  }
});
```

Et nous sommes en mesure d'ajouter plus de données liées aux `MediaTypes` comme `PDF` :

```typescript
enum MediaTypes {
  JSON = 'application/json',
  PDF = 'application/pdf'
}
```

Avec `Enum`, nous pouvons encapsuler des données dans un bloc de code significatif.

Récemment, j'implémentais un composant "state" React. C'est essentiellement un composant qui rend un état vide ou un état d'erreur basé sur la réponse de la requête.

L'UI pour les états vide et d'erreur étaient très similaires. Seuls le titre et le texte de description et l'icône d'image étaient différents. Donc je me suis dit : "J'ai deux façons en tête pour implémenter cela : faire la logique en dehors du composant et passer toutes les informations nécessaires ou passer un 'type d'état' et laisser le composant rendre l'icône et les messages corrects."

Donc j'ai construit une énumération :

```typescript
export enum StateTypes {
  Empty = 'Empty',
  Error = 'Error'
};
```

Et je pouvais simplement passer ces données au composant en tant que `type` :

```typescript
import ComponentState, { StateTypes } from './ComponentState';

<ComponentState type={StateTypes.Empty} />
<ComponentState type={StateTypes.Error} />
```

Dans le composant, il avait un objet d'état avec toutes les informations liées au `title`, `description`, et `icon`.

```typescript
const stateInfo = {
  Empty: {
    title: messages.emptyTitle,
    description: messages.emptyDescription,
    icon: EmptyIcon,
  },
  Error: {
    title: messages.errorTitle,
    description: messages.errorDescription,
    icon: ErrorIcon,
  },
};
```

Donc je pouvais simplement recevoir le type basé sur l'énumération et utiliser cet objet `stateInfo` avec le composant `State` de notre système de design :

```typescript
export const ComponentState = ({ type }) => (
  <State
    title={stateInfo[type].title}
    subtitle={stateInfo[type].subtitle}
    icon={stateInfo[type].icon}
  />
);
```

C'est une façon d'utiliser une énumération pour encapsuler des données importantes dans un bloc de code significatif dans votre application.

Une autre fonctionnalité intéressante de TypeScript est les propriétés optionnelles. Lorsque nous avons des propriétés d'un objet qui peuvent être une valeur réelle ou indéfinie, nous utilisons une propriété optionnelle pour indiquer explicitement que la propriété peut être présente ou non. La syntaxe pour cela est un simple opérateur `?` dans la propriété de l'objet. Imaginez cette fonction :

```typescript
function sumAll(a: number, b: number, c: number) {
  return a + b + c;
}
```

Mais maintenant la valeur `c` est optionnelle :

```typescript
function sumAll(a: number, b: number, c?: number) {
  return a + b + c;
}
```

Nous ajoutons le `?` après `c`. Mais maintenant nous avons une erreur de compilateur disant :

```typescript
(parameter) c: number | undefined
Object is possibly 'undefined'.
```

Nous ne pouvons pas additionner une valeur `undefined` (en fait, en JavaScript nous pouvons, mais nous recevons une valeur `NaN`).

Nous devons nous assurer que `c` existe. Rétrécissement de type !

```typescript
function sumAll(a: number, b: number, c?: number) {
  if (c) {
    return a + b + c;
  }

  return a + b;
}
```

Si `c` existe, ce sera un `number` et nous pouvons tout additionner. Sinon, additionnez uniquement les valeurs `a` et `b`.

Une partie intéressante de cette propriété optionnelle est qu'elle est `undefined` et non `null`. C'est pourquoi nous faisons cela, nous obtenons une erreur de compilation :

```typescript
let number = null;
sumAll(1, 2, number);
// Argument of type 'null' is not assignable to parameter of type 'number | undefined'.
```

Comme l'opérateur `?` ne gère pas la valeur `null`, choisissez d'utiliser le type `undefined` dans votre application et vous pouvez toujours utiliser la propriété optionnelle et rendre les types cohérents. Nous pouvons l'utiliser comme ceci :

```typescript
let value: number | undefined;
sumAll(1, 2, value); // 3
```

Si vous ajoutez une valeur par défaut au paramètre, vous n'aurez pas besoin de l'opérateur `?`. En fait, le compilateur dira que le `Parameter cannot have question mark and initializer`.

```typescript
function sumAll(a: number, b: number, c: number = 3) {
  return a + b + c;
}
```

Les propriétés optionnelles ne fonctionnent pas seulement sur les variables et les paramètres, mais aussi dans les objets.

Une réponse d'API est un bon exemple de définition de type et de propriété optionnelle ensemble. Dans les réponses d'API, les données peuvent être optionnelles. Parfois l'API envoie, parfois elle n'a pas de valeur.

La façon dont nous modélisons nos types est vraiment importante pour une application. Si une propriété optionnelle est définie comme un type requis, nous pouvons faire en sorte que notre application se casse à l'exécution. Mais si nous concevons les types correctement, nous avons les erreurs possibles à la compilation.

Imaginez que nous récupérons des données utilisateur et que c'est ainsi que nous avons modélisé le type de réponse :

```typescript
type UserResponse = {
  name: string;
  email: string;
  username: string;
  age: number;
  isActive: boolean;
};
```

Mais en réalité, l'email est optionnel pour l'utilisateur. Le point de terminaison de l'API pourrait retourner ou non. Mais le type `UserResponse` que nous avons construit le traite comme une propriété requise.

Après avoir récupéré les données de l'utilisateur, nous voulons voir si l'email de l'utilisateur correspond à un domaine spécifique.

```typescript
function matchDomain(email: string) {
  return email.endsWith(domain);
}
```

Comme la propriété `email` est requise dans le type `UserResponse`, le paramètre `email` sera également requis dans la fonction `matchDomain`.

C'est le runtime que nous pouvons obtenir si l'`email` est `undefined` :

```typescript
// Uncaught TypeError: Cannot read property 'endsWith' of undefined
```

Mais que se passerait-il si nous modélisions correctement le `UserResponse` ?

```typescript
type UserResponse = {
  name: string;
  email?: string;
  username: string;
  age: number;
  isActive: boolean;
};
```

Maintenant, l'`email` est éventuellement `undefined` et c'est explicite.

Mais si nous gardons la fonction `matchDomain` de la même manière, nous obtenons une erreur de compilation :

```typescript
// Argument of type 'undefined' is not assignable to parameter of type 'string'.
```

Et c'est génial ! Maintenant, nous pouvons corriger le paramètre `email` dans cette fonction en utilisant l'opérateur `?` :

```typescript
function matchDomain(email?: string) {
  return email.endsWith('email.com');
}
```

Mais maintenant, nous obtenons une erreur de compilation lors de l'exécution de `email.endsWith`, car il pourrait être `undefined` aussi :

```typescript
// (parameter) email: string | undefined
// Object is possibly 'undefined'.
```

Rétrécissement de type ! Nous utilisons un bloc if pour retourner un `false` lorsque l'`email` est `undefined`. Et exécuter la méthode `endsWith` uniquement si l'`email` est vraiment une chaîne :

```typescript
function matchDomain(email?: string) {
  if (!email) return false;
  return email.endsWith('email.com');
}
```

C'est plutôt bien lorsque nous pouvons obtenir des erreurs de runtime à la compilation. Mieux vaut coder que déboguer après avoir mis en production, n'est-ce pas ?

## Composition de types

La composition de types est très utile lorsque l'on essaie de réutiliser des types existants pour de nouveaux endroits de la base de code. Nous n'avons pas besoin de réécrire de nouveaux types, nous pouvons créer un nouveau type en composant des types existants.

Un exemple de composition que je dois toujours gérer en utilisant Redux ou le hook `useReducer` de React est l'idée de "réducteurs". Un réducteur peut toujours recevoir un certain nombre d'actions différentes.

Dans ce contexte, les actions sont des objets avec au moins une propriété `type`. Cela ressemble à ceci :

```typescript
enum ActionTypes {
  FETCH = 'FETCH'
}

type FetchAction = {
  type: typeof ActionTypes.FETCH;
};

const fetchAction: FetchAction = {
  type: ActionTypes.FETCH
};
```

Une `fetchAction` a un type `FetchAction` qui a une propriété type qui est un typeof `FETCH`.

Mais un réducteur peut recevoir d'autres actions aussi. Par exemple, une action de soumission :

```typescript
enum ActionTypes {
  FETCH = 'FETCH',
  SUBMIT = 'SUBMIT'
}

type SubmitAction = {
  type: typeof ActionTypes.SUBMIT;
};

const submitAction: SubmitAction = {
  type: ActionTypes.SUBMIT
};
```

Pour un conteneur spécifique, nous pouvons composer toutes ces actions en un seul type et l'utiliser pour le type de paramètre du réducteur.

Cela ressemblerait à ceci :

```typescript
type Actions = FetchAction | SubmitAction;

function reducer(state, action: Actions) {
  switch (action.type) {
    case ActionTypes.FETCH:
    // fetching action
    case ActionTypes.SUBMIT:
    // submiting action
  }
}
```

Toutes les actions possibles sont le type `Actions`. Et nous utilisons un type d'union pour "joindre" tous les types d'actions. L'action dans le réducteur peut avoir le `FetchAction` ou le `SubmitAction`.

En tant que Potterhead, je ne pouvais pas manquer un exemple de Harry Potter. Je veux construire une fonction simple pour choisir une Maison de Poudlard en fonction du trait de caractère de la personne. Commençons d'abord par les maisons.

```typescript
type House = {
  name: string;
  traits: string[];
}

const gryffindor: House = {
  name: 'Gryffindor',
  traits: ['courage', 'bravery']
};

const slytherin: House = {
  name: 'Slytherin',
  traits: ['ambition', 'leadership']
};

const ravenclaw: House = {
  name: 'Ravenclaw',
  traits: ['intelligence', 'learning']
};

const hufflepuff: House = {
  name: 'Hufflepuff',
  traits: ['hard work', 'patience']
};

const houses: House[] = [
  gryffindor,
  slytherin,
  ravenclaw,
  hufflepuff
];
```

Je veux garder cela simple, donc le type `House` n'a que le `name` et les `traits`, une liste de traits possibles des personnes liées à la maison.

Et puis, je crée chaque maison et les ajoute toutes à la liste `houses`.

Génial ! Maintenant, je vais construire le type `Person`. Une personne peut être une sorcière ou un moldu.

```typescript
type Witch = {
  name: string;
  trait: string;
	magicFamily: string;
}

type Muggle = {
  name: string;
	trait: string;
  email: string;
}
```

Et c'est la partie où nous combinons ces deux types différents en utilisant le type d'union :

```typescript
type Person = Muggle | Witch;
```

En utilisant le type d'intersection, le type `Person` a toutes les propriétés de `Muggle` ou toutes celles de `Witch`.

Donc maintenant, si je crée un `Muggle`, j'ai besoin du nom, du trait et de l'email :

```typescript
const hermione: Muggle = {
  name: 'Hermione Granger',
	trait: 'bravery',
  email: 'hermione@mail.com'
};
```

Si je crée une `Witch`, j'ai besoin du nom, du trait et du nom de la famille magique :

```typescript
const harry: Witch = {
  name: 'Harry Potter',
  trait: 'courage',
  magicFamily: 'Potter'
};
```

Et si je crée une `Person`, j'ai besoin au moins des propriétés `name` et `trait` de `Muggle` et `Witch` :

```typescript
const tk: Person = {
  name: 'TK',
  email: 'tk@mail.com',
  trait: 'learning',
  magicFamily: 'Kinoshita'
};
```

Le `chooseHouse` est très simple. Nous passons simplement les maisons et la personne. En fonction du trait de la personne, la fonction retournera la maison choisie :

```typescript
function chooseHouse(houses: House[], person: Person) {
  return houses.find((house) => house.traits.includes(person.trait))
}
```

Et en appliquant toutes les personnes que nous avons créées :

```typescript
chooseHouse(houses, harry); // { name: 'Gryffindor', traits: ['courage', 'bravery'] }
chooseHouse(houses, hermione); // { name: 'Gryffindor', traits: ['courage', 'bravery'] }
chooseHouse(houses, tk); // { name: 'Ravenclaw', traits: ['intelligence', 'learning'] }
```

Bien !

Le type d'intersection est un peu différent, mais il peut également être utilisé pour combiner des types existants.

Lorsque j'implémentais une application web pour [appliquer mes études sur l'UX](https://github.com/leandrotk/ux-studies), j'ai dû créer un type de prop pour le composant Image.

J'avais le type `ImageUrl` du type de produit :

```typescript
type ImageUrl = {
  imageUrl: string;
};
```

Et le `ImageAttr` pour représenter tous les attributs de l'image :

```typescript
type ImageAttr = {
  imageAlt: string;
  width?: string
};
```

Mais les props attendaient toutes ces informations dans le composant. Type d'intersection à la rescousse !

```typescript
type ImageProps = ImageUrl & ImageAttr;
```

Simple comme cela. Donc maintenant, le composant a besoin de toutes ces propriétés. Le type ressemble à ceci :

```typescript
type ImageProps = {
  imageUrl: string;
  imageAlt: string;
  width?: string
};
```

Et nous pouvons utiliser ce type de cette manière :

```typescript
const imageProps: ImageProps = {
  imageUrl: 'www.image.com',
  imageAlt: 'an image',
};

const imagePropsWithWidth: ImageProps = {
  imageUrl: 'www.image.com',
  imageAlt: 'an image',
  width: '100%'
};
```

Bien ! Un autre concept pour réutiliser et composer des types.

Je trouve également le type `Pick` très intéressant et utile. Nous avons d'autres [types intéressants](https://leandrotk.github.io/tk/2020/05/typescript-learnings-interesting-types/index.html) que nous pourrions écrire ici, mais l'idée ici est de comprendre que nous pouvons composer des types et qu'il n'y a pas de limite à la réutilisation des types. Si vous êtes intéressé à étudier d'autres types, jetez un coup d'œil à cet article que j'ai écrit : [TypeScript Learnings: Interesting Types](https://leandrotk.github.io/tk/2020/05/typescript-learnings-interesting-types/index.html).

## Outillage

Lorsque vous exécutez `npm install typescript`, vous n'obtenez pas seulement le compilateur, vous obtenez l'API de service de langage, un serveur autonome appelé tsserver que les éditeurs peuvent exécuter pour fournir une autocomplétion, un aller à, et d'autres fonctionnalités intéressantes.

Ces fonctionnalités sont ce que certaines personnes de l'équipe TypeScript appellent des outils de productivité pour les développeurs comme les erreurs intelligentes lors de la vérification des types et IntelliSense (complétion de code, info au survol, information de signature). Nous avons examiné ces fonctionnalités tout au long de l'article, mais je veux faire un sujet spécial pour en parler.

Le vérificateur de types TypeScript est puissant dans le sens où il peut inférer des types et fournir des informations sur certains problèmes possibles. Exemple : Il a inféré que la ville est une chaîne. Et le `uppercase` est utilisé de la mauvaise manière. Comme il sait que c'est une chaîne, il essaie également de trouver une méthode possible que l'ingénieur recherche.

```typescript
const city = 'Tokyo';
city.toUppercase();
// Property 'toUppercase' does not exist on type
// 'string'. Did you mean 'toUpperCase'?
```

Dans ce cas, le compilateur est vraiment intelligent, car il trouve exactement ce que nous voulions.

Cela fonctionne également pour les objets :

```typescript
const people = [
  { name: 'TK', age: 24 },
  { name: 'Kaio', age: 12 },
  { name: 'Kazumi', age: 31 },
];

for (const person of people) {
  console.log(person.agi);
  // Property 'agi' does not exist on type '{ name: string; age: number; }'
}
```

Avec les types statiques, l'outillage peut fournir une excellente expérience de développement avec la complétion de code, l'info au survol pour montrer les types définis, et les informations de signature pour les méthodes et autres données.

Si vous tapez : `'TK'.`, l'éditeur affichera toutes les méthodes possibles pour l'objet chaîne. Le compilateur sait que c'est une chaîne. Et il connaît les méthodes du prototype `String`. Mais il fournit également la signature de la méthode. C'est très intéressant car nous n'avons pas nécessairement besoin d'aller dans la documentation. La "documentation" est déjà dans notre éditeur de code.

C'est une expérience géniale lors du codage.

La définition de type "au survol" est une autre chose que nous avons vue plus tôt dans cet article. Laissez le compilateur inférer les types implicitement et vous ne perdrez pas la documentation de type. En utilisant le survol sur l'objet, l'IDE ou l'éditeur sera toujours en mesure d'afficher la définition de type.

Une autre chose intéressante est que TypeScript ne signalera pas seulement ce qui pourrait mal se passer à l'exécution, mais il aide également à trouver du code qui ne fait pas ce que vous avez l'intention de faire.

Imaginez que nous avons une fonction pour ouvrir un snackbar s'il est encore fermé. Il vérifierait l'état du snackbar. S'il est fermé, appelez simplement une autre fonction pour l'ouvrir.

```typescript
const buildSnackbar = (status: SnackbarStatus) => {
  if (status.isClosed) {
    openSnackbar();
  }
};
```

Et les informations de type pour ce snackbar sont :

```typescript
type SnackbarStatus = {
  isClosed: boolean;
};
```

Que se passe-t-il si j'appelle cette fonction comme ceci :

```typescript
buildSnackbar({ isclosed: true });
```

Cela ne cassera pas à l'exécution, car l'objet `status` n'a pas d'attribut `isClosed` et l'objet `undefined` est une valeur `falsy`, donc il ignorera la condition if et n'appellera pas la fonction `openSnackbar`. Pas d'erreur à l'exécution. Mais probablement, cela se comportera différemment de ce qui était attendu.

En TypeScript, le compilateur donnera quelques indices pour le faire fonctionner correctement. D'abord, il montrera cette erreur :

```typescript
// Argument of type '{ isclosed: boolean; }' is not assignable to
// parameter of type 'SnackbarStatus'.
```

`isclosed` avec un `C` minuscule n'est pas assignable au type. Il n'est pas défini là. C'est le premier indice pour vous faire corriger votre code.

Le second est encore mieux :

```typescript
// Object literal may only specify known properties,
// but 'isclosed' does not exist in type 'SnackbarStatus'.
// Did you mean to write 'isClosed'?
```

Il dit exactement ce que vous devez probablement faire : renommer `isclosed` en `isClosed`.

Nous pourrions parler de beaucoup de choses sur l'outillage, mais je pense que c'est la partie principale.

Ma suggestion pour en apprendre davantage sur cela est de simplement coder en TypeScript et "avoir une conversation" avec le compilateur. Lisez les erreurs. Jouez avec le survol. Voyez l'autocomplétion. Comprenez les signatures de méthode. C'est vraiment une façon productive de coder.

## Conseils & Apprentissages

Alors que l'article touche à sa fin, je veux simplement ajouter quelques réflexions finales, apprentissages et conseils pour vous aider dans votre parcours d'apprentissage de TypeScript ou simplement dans son application dans vos projets.

* Lisez vraiment l'erreur de type : cela vous aidera à mieux comprendre le problème et les types.
* `strictNullChecks` et `noImplicitAny` peuvent être très utiles pour trouver des bugs. Activez cela dès que possible dans votre projet. Utilisez `strictNullChecks` pour prévenir les erreurs de runtime du type "undefined is not an object". Utilisez `noImplicitAny` pour typer le code source afin de donner plus d'informations de type au compilateur.
* Ensemble avec les configurations du compilateur, je recommande toujours d'être très précis sur vos types. Principalement avec les valeurs qui n'apparaissent qu'à l'exécution comme une réponse d'API. La justesse est importante pour attraper autant de bugs que possible à la compilation.
* Comprenez la différence entre le runtime et le compile time : les types n'affectent que le compile time. Il exécute le vérificateur de type puis compile en JavaScript. Le code source JavaScript n'utilise aucune référence de type ou opération de type.
* Apprenez les types utilitaires. Nous avons parlé plus spécifiquement du `Readonly` dans l'immuabilité à la compilation, mais TypeScript a une boîte d'outils comme `Required`, `Pick`, et bien d'autres.
* Si possible, préférez laisser le compilateur inférer les types pour vous. La plupart des types et des types de retour sont redondants. Le compilateur TypeScript est très intelligent dans ce domaine. Si ce n'est pas possible, vous pouvez toujours ajouter des annotations de type. Et laissez les assertions de type comme dernière option.
* Alors que vous écrivez du code, jetez un coup d'œil à l'outillage. La conception de l'outillage fourni dans un IDE est incroyable. L'IntelliSense et la vérification de type fournissent une expérience vraiment bonne.

Cet article a été publié à l'origine sur [le blog de TK](https://leandrotk.github.io/tk/2020/07/a-mental-model-to-think-in-typescript/index.html). Et vous pouvez trouver plus de contenu comme celui-ci sur mon blog à l'adresse [https://leandrotk.github.io/tk](https://leandrotk.github.io/tk/).

Vous pouvez également me suivre sur [Twitter](https://twitter.com/leandrotk_) et [GitHub](https://github.com/leandrotk).

# Ressources

J'ai compilé (jeu de mots très intentionnel !) un tas de ressources pour vous aider à en apprendre davantage sur les langages de programmation, les systèmes de types et le modèle mental de type.

De plus, si vous avez trouvé les exemples de cet article utiles, je les ai tous ajoutés à ce dépôt : [Thinking in Types](https://github.com/leandrotk/thinking-in-types). Vous pouvez donc les fork et jouer avec.

### Systèmes de Types

* [Type Compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
* [Type Systems: Structural vs. Nominal typing explained](https://medium.com/@thejameskyle/type-systems-structural-vs-nominal-typing-explained-56511dd969f4)
* [Learning TypeScript: Structural vs nominal typing systems](https://yakovfain.com/2018/07/11/learning-typescript-structural-vs-nominal-typing-system/)
* [Constraints Liberate, Liberties Constrain — Runar Bjarnason](https://www.youtube.com/watch?v=GqmsQeSzMdw&feature=youtu.be)
* [Type Narrowing in TypeScript](https://www.no.lol/2019-12-27-type-narrowing/)
* [TypeScript: narrowing types via type guards and assertion functions](https://2ality.com/2020/06/type-guards-assertion-functions-typescript.html)
* [TypeScript Learnings: Interesting Types](https://leandrotk.github.io/tk/2020/05/typescript-learnings-interesting-types/index.html)

### Outillage & Expérience Développeur

* [Advanced TypeScript tooling at scale](https://www.youtube.com/watch?v=fnTEZk-oECM)
* [Type Systems & Props Design](https://www.youtube.com/watch?v=4C4wCGcsiT0)
* [Anders Hejlsberg on Modern Compiler Construction](https://www.youtube.com/watch?v=wSdV1M7n4gQ)
* [TypeScript Compiler explained by the Author Anders Hejlsberg](https://www.youtube.com/watch?v=f6TCB61fDwY)

### Compile time vs Runtime

* [Compile time vs Runtime](https://stackoverflow.com/questions/846103/runtime-vs-compile-time)
* [Compile error vs Runtime error](https://stackoverflow.com/questions/9471837/what-is-the-difference-between-run-time-error-and-compiler-error)
* [Value space and Type space](https://stackoverflow.com/a/51132333/3159162)
* [A playground tool to play with TypeScript and see the JavaScript output](https://www.typescriptlang.org/play)

### Best Practices

* [TypeScript Best Practices](https://engineering.zalando.com/posts/2019/02/typescript-best-practices.html)
* [Do's and Don'ts for General Types](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)

### Books

* [Programming with Types Book](https://www.goodreads.com/book/show/48920810-programming-with-types)
* [Effective TypeScript: 62 Specific Ways to Improve Your TypeScript Book](https://www.goodreads.com/book/show/48570456-effective-typescript)
* [Thinking with Types](https://thinkingwithtypes.com/)