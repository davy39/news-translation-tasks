---
title: Le manuel des classes JavaScript – Guide complet sur les champs de classe et
  le mot-clé Super
date: '2024-05-20T20:05:18.000Z'
author: Oluwatobi Sofela
authorURL: https://www.freecodecamp.org/news/author/oluwatobiss/
originalURL: https://freecodecamp.org/news/javascript-class-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/JavaScript-Class-Handbook-Cover.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
seo_desc: 'Classes let you privatize your data while providing users indirect access
  to it. It is an excellent way to prevent direct access to your constructor’s data.

  This handbook aims to show you exactly how classes work in JavaScript. We will also
  discuss c...'
---


Les classes vous permettent de privatiser vos données tout en offrant aux utilisateurs un accès indirect à celles-ci. C'est un excellent moyen d'empêcher l'accès direct aux données de votre constructeur.

<!-- more -->

Ce manuel vise à vous montrer exactement comment fonctionnent les classes en JavaScript. Nous aborderons également les champs de classe et le mot-clé `super`.

## Table des matières

1.  [Qu'est-ce qu'une classe JavaScript ?][1]
2.  [Pourquoi utiliser les classes en JavaScript ?][2]
3.  [Syntaxe d'une classe JavaScript][3]
    -   [Qu'est-ce que le mot-clé `class` ?][4]
    -   [Qu'est-ce qu'un nom de classe ?][5]
    -   [Qu'est-ce qu'un bloc de code ?][6]
    -   [Qu'est-ce qu'un corps de classe ?][7]
4.  [Qu'est-ce qu'un champ de classe JavaScript ?][8]
    -   [Comment créer des champs de classe en JavaScript][9]
    -   [Comment créer des champs de classe avec des noms calculés][10]
    -   [Comment créer des méthodes de champ de classe régulières][11]
    -   [Comment créer des méthodes de champ de classe raccourcies][12]
    -   [Méthodes de champ de classe régulières vs raccourcies : quelle est la différence ?][13]
    -   [Qu'est-ce qu'une méthode prototypale définie par l'utilisateur dans les classes JavaScript ?][14]
    -   [Qu'est-ce qu'une méthode `constructor` dans les classes JavaScript ?][15]
    -   [Types de champs de classe][16]
    -   [Qu'est-ce qu'un champ de classe public dans les classes JavaScript ?][17]
    -   [Qu'est-ce qu'un champ de classe privé dans les classes JavaScript ?][18]
    -   [Qu'est-ce qu'un champ de classe statique dans les classes JavaScript ?][19]
5.  [Types de classes JavaScript][20]
    -   [Qu'est-ce qu'une déclaration de classe JavaScript ?][21]
    -   [Qu'est-ce qu'une expression de classe JavaScript ?][22]
    -   [Qu'est-ce qu'une classe dérivée en JavaScript ?][23]
6.  [Qu'est-ce que le mot-clé `super` en JavaScript ?][24]
    -   [Comment utiliser le mot-clé `super` comme appelant de fonction][25]
    -   [Comment utiliser le mot-clé `super` comme accesseur de propriété][26]
    -   [Mot-clé `super` vs `this` : quelle est la différence ?][27]
7.  [Composants d'une classe JavaScript][28]
8.  [Comment une classe JavaScript aide-t-elle à l'encapsulation ?][29]
9.  [Choses importantes à savoir sur les classes JavaScript][30]
    -   [1. Déclarez votre classe avant d'y accéder][31]
    -   [2. Les classes sont des fonctions][32]
    -   [3. Les classes sont strictes][33]
    -   [4. Évitez le mot-clé `return` dans la méthode `constructor` de votre classe][34]
    -   [5. L'évaluation d'une classe commence de la clause `extends` vers ses valeurs][35]
10.  [Aperçu][36]

Commençons par les bases.

## Qu'est-ce qu'une classe JavaScript ?

Une classe JavaScript est un [constructeur d'objet][37] que le [mot-clé `new`][38] utilise pour créer une nouvelle instance d'objet.

Voici un exemple :

```
// Définir une classe JavaScript :
class Name {}

// Créer une instance d'objet à partir de la classe Name :
const yourName = new Name();

// Vérifier le contenu de yourName :
yourName;

// L'appel ci-dessus retournera un objet vide :
{ }
```

[**Essayer de le modifier**][39]

Le fragment de code ci-dessus utilise le mot-clé `new` pour créer une nouvelle instance d'objet à partir du constructeur `class`.

**Note :** L'appel d'une classe JavaScript nécessite le mot-clé `new`. Sinon, les navigateurs lèveront une `TypeError`.

## Pourquoi utiliser les classes en JavaScript ?

Les classes permettent de créer un modèle pour concevoir des objets ayant accès à des données privées via des méthodes publiques.

En d'autres termes, les classes vous aident à [encapsuler][40] vos données tout en offrant aux utilisateurs un accès indirect au fonctionnement interne d'une instance. Cela vous permet de fournir aux utilisateurs une interface propre et conviviale, indépendante des implémentations internes d'un objet.

Par exemple, [`Date`][41] est une classe JavaScript qui vous permet d'accéder à ses données de date via ses méthodes publiques, telles que `getDate()`, `setDate()` et `getFullYear()`.

## Syntaxe d'une classe JavaScript

```
class NameOfClass {
  // corps de la classe
}
```

Une classe est composée de quatre composants :

1.  Un mot-clé `class`
2.  Le nom de la classe
3.  Un bloc de code (`{...}`)
4.  Le corps de la classe

Analysons chaque composant.

### Qu'est-ce que le mot-clé `class` ?

Nous utilisons le mot-clé `class` pour déclarer aux navigateurs qu'un morceau de code spécifique est une classe JavaScript — et non une classe mathématique ou une autre classe générique.

### Qu'est-ce qu'un nom de classe ?

Un nom de classe vous permet de créer un identifiant pour votre classe, que vous pouvez utiliser pour la référencer.

**Note :** Les développeurs utilisent généralement une majuscule pour commencer le nom d'une classe. Cette convention aide à différencier un constructeur des autres fonctions.

### Qu'est-ce qu'un bloc de code ?

Un bloc est une paire d'accolades (`{...}`) utilisée pour regrouper plusieurs instructions.

Voici un exemple :

```
{
  var bestColor = "White";
}
```

Le bloc dans le fragment ci-dessus contient une [instruction JavaScript][42].

Voici un autre exemple :

```
if (new Date().getHours() < 18) {
  const hourNow = new Date().getHours();
  const minutesNow = new Date().getMinutes();
  const secondsNow = new Date().getSeconds();
  console.log(`Check your plans now. The time is ${hourNow}:${minutesNow}:${secondsNow}.`);
}
```

Le bloc de code de la condition `if` regroupe quatre instructions JavaScript.

Maintenant, considérez ce fragment :

```
class Time {
  hourNow = new Date().getHours();
  minutesNow = new Date().getMinutes();
  secondsNow = new Date().getSeconds();
}

if (new Date().getHours() < 18) {
   const currentTime = new Time();
   console.log(`Check your plans now. The time is ${currentTime.hourNow}:${currentTime.minutesNow}:${currentTime.secondsNow}.`);
}
```

Le bloc de code de la classe `Time` regroupe trois instructions JavaScript, tandis que le bloc de code de la condition `if` en regroupe deux.

Notez les points suivants :

-   `hourNow`, `minutesNow` et `secondsNow` sont les champs de classe (propriétés).
-   Le fragment ci-dessus utilise le mot-clé `new` pour construire un nouvel objet à partir de la classe `Time`. Par conséquent, l'objet `currentTime` est une instance de la classe constructeur `Time`.

### Qu'est-ce qu'un corps de classe ?

Un corps de classe est l'endroit où vous placez une séquence d'instructions.

Voici la syntaxe :

```
class NameOfClass {
  // corps de la classe
}
```

**Note :** Le corps d'une classe n'héberge que des champs de classe. Mais qu'est-ce qu'un champ de classe exactement ? Découvrons-le.

## Qu'est-ce qu'un champ de classe JavaScript ?

Un champ de classe est une propriété définie directement dans le corps d'une classe — et non à l'intérieur de l'une des [méthodes][43] de la classe.

### Comment créer des champs de classe en JavaScript

Vous pouvez créer un champ de classe en utilisant un signe égal (`=`) — et non deux points (`:`) — pour assigner une valeur à une propriété.

Voici un exemple :

```
// Définir une classe JavaScript :
class Name {
  // Créer deux champs de classe :
  firstName = "Oluwatobi";
  lastName = "Sofela";
}

// Créer une nouvelle instance d'objet :
const fullName = new Name();

console.log(fullName.firstName + " " + fullName.lastName);
```

[**Essayer de le modifier**][44]

La classe `Name` dans le fragment ci-dessus possède deux champs de classe (`firstName` et `lastName`).

Notez les points suivants :

-   Les champs de classe JavaScript valent `undefined` par défaut si vous ne fournissez aucune valeur.
-   Les champs de classe sont comme les [propriétés][45] d'objet régulières dont vous pouvez [calculer][46] les noms. Voyons comment.

### Comment créer des champs de classe avec des noms calculés

Vous pouvez calculer (évaluer) le nom d'un champ de classe en plaçant une expression entre crochets comme ceci :

```
// Initialiser une variable num avec un nombre :
let num = 0;

// Assigner une valeur de chaîne à une variable enSuites :
const enSuites = "East";

// Définir une classe Room et calculer chacun des noms de ses champs de classe :
class Room {
  [enSuites + ++num] = num;
  [enSuites + ++num] = num;
  [enSuites + ++num] = num;
}

// Créer une instance d'objet ensuiteRooms :
const ensuiteRooms = new Room();

// Vérifier le contenu de ensuiteRooms :
console.log(ensuiteRooms);

// L'appel ci-dessus retournera :
{East1: 1, East2: 2, East3: 3}
```

[**Essayer de le modifier**][47]

Nous avons utilisé la syntaxe `[enSuites + ++num]` dans le fragment ci-dessus pour calculer les noms des champs de classe.

En d'autres termes, JavaScript a évalué l'expression `enSuites + ++num` et a utilisé le résultat comme nom pour chaque champ de classe.

**Note :** Vous pouvez également définir des champs de classe comme des méthodes JavaScript régulières. Parlons-en davantage maintenant.

### Comment créer des méthodes de champ de classe régulières

Vous pouvez créer une méthode de champ de classe régulière en utilisant un signe égal (`=`) pour assigner une fonction à une propriété.

Voici un exemple :

```
// Définir une classe JavaScript :
class Time {
  // Créer deux méthodes de champ de classe régulières :
  hourNow = function() {
    return new Date().getHours();
  }
  minutesNow = function() {
    return new Date().getMinutes();
  }
}

// Créer une nouvelle instance d'objet :
const currentTime = new Time();

console.log(`The time is ${currentTime.hourNow()}:${currentTime.minutesNow()}.`);
```

[**Essayer de le modifier**][48]

Les méthodes `hourNow` et `minutesNow` dans le fragment ci-dessus sont des méthodes de champ de classe car ce sont des propriétés contenant des fonctions JavaScript régulières.

JavaScript vous permet d'utiliser une syntaxe raccourcie pour simplifier les méthodes de votre classe. Voyons comment.

### Comment créer des méthodes de champ de classe raccourcies

La méthode de champ de classe raccourcie est un moyen concis de définir des méthodes JavaScript dans le corps de vos classes.

Voici un exemple :

```
// Définir une classe JavaScript :
class Time {
  // Créer deux méthodes de champ de classe raccourcies : 
  hourNow() {
    return new Date().getHours();
  }
  minutesNow() {
    return new Date().getMinutes();
  }
}

// Créer une nouvelle instance d'objet :
const currentTime = new Time();

console.log(`The time is ${currentTime.hourNow()}:${currentTime.minutesNow()}.`);
```

[**Essayer de le modifier**][49]

Bien que vous puissiez utiliser les méthodes régulières et raccourcies de manière interchangeable dans le corps de votre classe, vous devez connaître une différence significative entre les deux syntaxes. Discutons-en maintenant.

### Méthodes de champ de classe régulières vs raccourcies : quelle est la différence ?

La principale différence entre les méthodes de champ de classe régulières et raccourcies est la suivante :

-   Les méthodes régulières sont des [propriétés d'instance][50], tandis que les méthodes raccourcies sont des [propriétés prototypales][51].

En d'autres termes, JavaScript traite les méthodes régulières et raccourcies différemment comme suit :

-   **Méthode régulière :** JavaScript ajoute la méthode à l'[instance d'objet][52] que vous construisez avec le mot-clé `new`. Par conséquent, les méthodes régulières sont des propriétés de l'instance d'objet.
-   **Méthode raccourcie :** JavaScript ajoute la méthode à la [propriété `prototype`][53] de la classe. Par conséquent, les méthodes raccourcies sont des propriétés prototypales d'une instance d'objet.

Voici un exemple :

```
// Définir une classe JavaScript :
class Time {
  // Créer une méthode régulière :
  hourNow = function() {
    return new Date().getHours();
  }
  // Créer une méthode raccourcie :
  minutesNow() {
    return new Date().getMinutes();
  }
}

// Créer une nouvelle instance d'objet :
const currentTime = new Time();

// Vérifier le contenu de currentTime :
console.log(currentTime);

// L'appel ci-dessus retournera :
{ hourNow: hourNow() }
```

[**Essayer de le modifier**][54]

L'instance d'objet `currentTime` ne contient que la propriété `hourNow` car les méthodes régulières sont des propriétés d'instance que le mot-clé `new` a assignées à l'objet qu'il construit à partir de sa classe constructeur.

D'un autre côté, les méthodes raccourcies sont des méthodes prototypales que JavaScript ajoute à la propriété `prototype` de la classe que vous avez définie.

Par conséquent, vous pouvez accéder à la méthode `minuteNow` via l'[héritage prototypal][55] de sa classe comme ceci :

```
// Définir une classe JavaScript :
class Time {
  // Créer une méthode régulière :
  hourNow = function() {
    return new Date().getHours();
  }
  // Créer une méthode raccourcie :
  minutesNow() {
    return new Date().getMinutes();
  }
}

// Vérifier le contenu du prototype de Time :
console.log(Time.prototype);

// L'appel ci-dessus retournera :
{...}:
  constructor: class Time {}
  minutesNow: function minutesNow()
  [[Prototype]]: Object {...}
```

[**Essayer de le modifier**][56]

Vous pouvez voir que la propriété `prototype` de `Time` contient la méthode `minutesNow`, dont toutes les instances d'objet hériteront automatiquement.

Voici un exemple :

```
// Définir une classe JavaScript :
class Time {
  // Créer une méthode raccourcie :
  minutesNow() {
    return new Date().getMinutes();
  }
}

// Créer une instance d'objet à partir de la classe Time :
const currentTime = new Time();

// Vérifier le contenu de currentTime :
console.log(currentTime);

// L'appel ci-dessus retournera un objet vide :
{ }

// Appeler la méthode minutesNow de currentTime :
console.log(currentTime.minutesNow());
```

[**Essayer de le modifier**][57]

Le code `currentTime.minutesNow()` a retourné une valeur valide car `currentTime` a hérité de la méthode `minuteNow()` de la propriété `prototype` de son constructeur.

**Note :** Une classe JavaScript possède deux types de méthodes prototypales :

-   Les méthodes définies par l'utilisateur
-   Les méthodes constructeurs

Analysons ces deux types maintenant.

### Qu'est-ce qu'une méthode prototypale définie par l'utilisateur dans les classes JavaScript ?

Une méthode prototypale définie par l'utilisateur est la méthode raccourcie que vous créez vous-même dans le corps de votre classe JavaScript.

Voici un exemple :

```
// Définir une classe JavaScript :
class Name {
  // Créer une méthode raccourcie :
  firstName(name) {
    return name;
  }
}

// Créer une instance d'objet à partir de la classe Name :
const myName = new Name().firstName("Oluwatobi");

// Afficher le contenu de myName dans la console :
console.log(myName);

// L'appel ci-dessus retournera :
"Oluwatobi"
```

[**Essayer de le modifier**][58]

La méthode `firstName()` est une méthode définie par l'utilisateur car nous l'avons créée nous-mêmes dans le corps de la classe `Name`.

## Qu'est-ce qu'une méthode `constructor` dans les classes JavaScript ?

Un `constructor()` est la méthode prototypale par défaut intégrée à chaque classe JavaScript.

La création d'une méthode `constructor` est facultative. Cependant, si vous n'en créez pas, JavaScript en ajoutera automatiquement une vide.

La méthode `constructor` reçoit automatiquement les [arguments][59] que vous passez à la classe. C'est donc l'endroit idéal pour définir les champs de classe qui dépendent des arguments de l'[appelant de la classe][60].

Voici un exemple :

```
// Définir une classe JavaScript :
class Name {
  // Utiliser la méthode constructor intégrée :
  constructor(name) {
    this.name = name;
  }
}

// Créer une instance d'objet à partir de la classe Name :
const myName = new Name("Oluwatobi");

// Afficher le contenu de myName dans la console :
console.log(myName);

// L'appel ci-dessus retournera :
{ name: "Oluwatobi" }
```

[**Essayer de le modifier**][61]

La classe `Name` ci-dessus possède une méthode `constructor` avec une [propriété d'instance][62] dans son bloc de code.

**Astuce :** Le mot-clé `this` d'une méthode `constructor()` fait référence à l'instance d'objet de la classe.

JavaScript exécute la méthode `constructor` avant toute autre méthode définie par l'utilisateur. C'est donc le meilleur endroit pour définir tout code que vous souhaitez exécuter avant les autres méthodes dans le corps de la classe. Par exemple, considérez le code ci-dessous :

```
// Définir une classe JavaScript :
class CarColor {
  // Utiliser la méthode constructor intégrée :
  constructor(color) {
    this.carColor = `${color} car`;
  }
  // Créer une méthode raccourcie :
  revealColor() {
    console.log(`I have a ${this.carColor}`);
  }
}

// Créer une instance d'objet à partir de la classe CarColor :
const myCarColor = new CarColor("white");

// Appeler la méthode prototypale revealColor de myCarColor :
myCarColor.revealColor();

// L'appel ci-dessus retournera :
"I have a white car"
```

[**Essayer de le modifier**][63]

Le fragment ci-dessus a automatiquement appelé la méthode `constructor` lors de la création de l'instance d'objet de `myCarColor`.

Par conséquent, l'ordinateur a traité les instructions du `constructor` avant d'exécuter le code `myCarColor.revealColor()`.

Notez les points suivants :

-   Vous ne pouvez utiliser que la technique du [raccourci de méthode JavaScript][64] pour définir un `constructor`. Sinon, les navigateurs lèveront une `Uncaught SyntaxError`.
-   Une classe ne peut avoir qu'une seule méthode `constructor`. Sinon, les navigateurs lèveront une `Uncaught SyntaxError`.

Maintenant que nous savons comment créer des champs de classe, nous pouvons discuter des types disponibles.

## Types de champs de classe

Les trois types de champs de classe sont :

-   Champs de classe publics
-   Champs de classe privés
-   Champs de classe statiques

Analysons chaque type.

### Qu'est-ce qu'un champ de classe public dans les classes JavaScript ?

Un champ de classe public est une propriété à laquelle une instance d'objet a accès.

**Astuce :** Bien que vous puissiez définir plusieurs champs de classe publics avec le même nom, le dernier champ écrasera les précédents.

#### Exemple : Comment créer des champs de classe publics

```
// Définir une classe JavaScript :
class Name {
  // Créer deux champs de classe publics :
  myName = "Oluwatobi";
  updateMyName(name) {
    this.myName = name;
  }
}

// Créer une nouvelle instance d'objet :
const author = new Name();

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
"Oluwatobi"

// Utiliser la propriété de la variable author pour modifier la valeur de myName :
author.myName = "Sofela";

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
"Sofela"

// Utiliser la méthode de la variable author pour mettre à jour la valeur de myName :
author.updateMyName("CodeSweetly");

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
"CodeSweetly"
```

[**Essayer de le modifier**][65]

La classe `Name` dans le fragment ci-dessus contient des champs de classe publics car vous pouvez utiliser les instances d'objet de la classe pour accéder aux deux propriétés et les modifier.

Si vous définissez plusieurs champs de classe publics avec le même nom, la dernière propriété écrasera les précédentes.

#### Exemple : Le dernier champ de classe public écrase les précédents portant le même nom

```
// Définir une classe JavaScript :
class Name {
  // Créer trois champs de classe publics :
  myName = "Oluwatobi";
  myName = "Sofela";
  myName = "CodeSweetly";
}

// Créer une nouvelle instance d'objet :
const author = new Name();

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
"CodeSweetly"
```

[**Essayer de le modifier**][66]

Le fragment ci-dessus a retourné `"CodeSweetly"` car le dernier champ de classe public `myName` écrase ceux déclarés précédemment.

### Qu'est-ce qu'un champ de classe privé dans les classes JavaScript ?

Un champ de classe privé est une propriété que vous ne pouvez accéder et modifier qu'à l'intérieur du corps de la classe.

Vous pouvez préfixer un champ de classe avec le symbole dièse (`#`) pour en faire une propriété privée.

**Astuce :** Les noms des champs de classe privés doivent être uniques. Vous ne pouvez pas redéclarer un champ privé dans la même classe. Sinon, le navigateur lèvera une `Uncaught SyntaxError`.

#### Exemple : Comment créer des champs de classe privés

```
// Définir une classe JavaScript :
class Name {
  // Créer un champ de classe privé :
  #myName = "Oluwatobi";
}

// Créer une nouvelle instance d'objet :
const author = new Name();

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
undefined
```

[**Essayer de le modifier**][67]

Le fragment ci-dessus a retourné `undefined` car `myName` est un champ de classe privé qui ne peut être lu et modifié que depuis l'intérieur du corps de la classe.

Par conséquent, vous devez utiliser un code interne pour accéder à `myName`.

#### Exemple : Comment accéder aux champs de classe privés

```
// Définir une classe JavaScript :
class Name {
  // Créer un champ de classe privé :
  #myName = "Oluwatobi";

  // Créer un champ de classe public :
  fullName = `${this.#myName} Sofela`;

  // Créer un autre champ de classe public :
  showMyName() {
    return this.#myName;
  }
}

// Créer une nouvelle instance d'objet :
const author = new Name();

// Vérifier la valeur actuelle de fullName :
author.fullName;

// L'appel ci-dessus retournera :
"Oluwatobi Sofela"

// Vérifier la valeur actuelle de myName :
author.showMyName();

// L'appel ci-dessus retournera :
"Oluwatobi"
```

[**Essayer de le modifier**][68]

**Note :**

-   Une méthode `constructor()` ne peut être que publique. Les navigateurs lèveront une `Uncaught SyntaxError` si vous la définissez comme un champ de classe privé.
-   Vous ne pouvez pas créer de champs de classe privés plus tard (en dehors du corps de la classe). Par exemple, écrire `author.#wifeName = "Sarah"` lèvera une `Uncaught SyntaxError`.
-   Les champs de classe privés rendent l'encapsulation des données possible dans les classes JavaScript.

### Qu'est-ce qu'un champ de classe statique dans les classes JavaScript ?

Un champ de classe statique est une propriété à laquelle vous ne pouvez accéder et que vous ne pouvez modifier que directement depuis la classe elle-même.

En d'autres termes, JavaScript interprète les champs statiques comme les propriétés propres d'une classe — et non comme des propriétés d'[instance][69] ou [prototypales][70].

Par conséquent, l'instance d'une classe ou l'objet `prototype` ne peut pas accéder aux champs de classe statiques.

**Astuce :**

-   Bien que vous puissiez définir plusieurs champs de classe statiques avec le même nom, le dernier champ écrasera les précédents.
-   JavaScript n'ajoute pas les champs statiques à la propriété `prototype`. Ils restent dans le corps de la classe en tant que propriétés propres. Ils sont donc idéaux pour les propriétés que vous souhaitez éviter de répliquer sur les objets instances de la classe.

Nous préfixons un champ de classe avec le mot-clé `static` pour en faire une propriété statique.

#### Exemple : Comment créer des champs de classe statiques

```
// Définir une classe JavaScript :
class Name {
  // Créer un champ de classe statique :
  static myName = "Oluwatobi";
}

// Créer une nouvelle instance d'objet :
const author = new Name();

// Vérifier la valeur actuelle de myName :
author.myName;

// L'appel ci-dessus retournera :
undefined
```

[**Essayer de le modifier**][71]

Le fragment ci-dessus a retourné `undefined` car `myName` est un champ de classe statique qui ne peut être lu et modifié que depuis la classe elle-même, et non via son instance.

En d'autres termes, vous devez appeler `myName` sur la classe elle-même pour le lire ou le modifier.

#### Exemple : Comment accéder aux champs de classe statiques

```
// Définir une classe JavaScript :
class Name {
  // Créer un champ de classe statique :
  static myName = "Oluwatobi";
}

// Vérifier la valeur actuelle de myName :
Name.myName;

// L'appel ci-dessus retournera :
"Oluwatobi"
```

[**Essayer de le modifier**][72]

Si vous définissez plusieurs champs de classe statiques avec le même nom, la dernière propriété écrasera les précédentes.

#### Exemple : Le dernier champ de classe statique écrase les précédents portant le même nom

```
// Définir une classe JavaScript :
class Name {
  // Créer des champs de classe statiques :
  static myName = "Oluwatobi";
  static myName = "Sofela";
  static myName = "CodeSweetly";
}

// Vérifier la valeur actuelle de myName :
Name.myName;

// L'appel ci-dessus retournera :
"CodeSweetly"
```

[**Essayer de le modifier**][73]

Le fragment ci-dessus a retourné `"CodeSweetly"` car le dernier champ de classe statique `myName` écrase ceux déclarés précédemment.

Maintenant que nous connaissons les composants d'une classe JavaScript, nous pouvons discuter de ses types.

## Types de classes JavaScript

Les trois types de classes JavaScript sont :

-   Déclaration de classe
-   Expression de classe
-   Classe dérivée

Analysons chaque type.

### Qu'est-ce qu'une déclaration de classe JavaScript ?

Une déclaration de classe est une classe créée sans l'assigner à une [variable][74].

Nous appelons parfois la déclaration de classe une « définition de classe » ou une « instruction de classe ».

Voici un exemple :

```
class Numbers {}
```

La classe ci-dessus est une déclaration de classe car nous l'avons définie sans la stocker dans une variable.

### Qu'est-ce qu'une expression de classe JavaScript ?

Une expression de classe est une classe que vous créez et assignez à une variable.

Voici un exemple :

```
const myClassExpr = class Numbers {};
```

La classe ci-dessus est une expression de classe nommée que nous avons assignée à la variable `myClassExpr`.

**Note :** Vous ne pouvez utiliser le nom d'une expression de classe qu'à l'intérieur du corps de la classe. En d'autres termes, JavaScript vous permet d'utiliser `myClassExpr` et `Numbers` de manière interchangeable à l'intérieur du corps de la classe. Cependant, seul `myClassExpr` est appelable en dehors de la classe. Sinon, les navigateurs lèveront une `ReferenceError`.

Vous pouvez également écrire le fragment ci-dessus sous forme d'expression de classe anonyme comme ceci :

```
const myClassExpr = class {};
```

La classe ci-dessus est une expression de fonction anonyme assignée à la variable `myClassExpr`.

**Astuce :**

-   Une classe anonyme est une classe sans nom.
-   Une classe nommée est une classe avec un nom.

Discutons maintenant des classes dérivées.

### Qu'est-ce qu'une classe dérivée en JavaScript ?

Une classe dérivée est une classe qui étend les fonctionnalités [publiques][75] et [statiques][76] d'une classe existante.

En d'autres termes, une classe dérivée est l'enfant d'une classe parente.

**Important :** Une classe dérivée _ne peut pas_ accéder aux [fonctionnalités privées][77] de sa classe parente.

#### Syntaxe d'une classe dérivée

Nous utilisons le mot-clé `extends` pour créer une classe dérivée.

**Astuce :** Le mot-clé `extends` en JavaScript fait d'une classe l'enfant d'un autre constructeur. En d'autres termes, le mot-clé `extends` assigne un constructeur (classe ou fonction) comme [dunder proto][78] d'une classe spécifiée.

Voici la syntaxe :

```
class DerivedClass extends BaseClass {
  // corps de la classe dérivée
}
```

-   Une classe dérivée est parfois appelée classe enfant.
-   Une classe de base est parfois appelée classe parente.
-   Vous pouvez étendre n'importe quel constructeur (classe ou fonction) qui répond aux critères suivants :
    -   Vous pouvez utiliser le mot-clé `new` pour créer une instance d'objet à partir de celui-ci.
    -   Il possède une propriété [`prototype`][79].
    -   La valeur de sa propriété `prototype` est un [objet][80] ou `null`.

Une fois que vous étendez une classe enfant à une classe parente, la classe dérivée héritera de tous les champs de classe publics et statiques de sa classe de base.

#### Exemple : Comment utiliser les fonctionnalités d'une classe de base dans une classe dérivée

```
// Créer une nouvelle classe :
class Name {
  // Créer un champ de classe public :
  myName = "Oluwatobi";
}

// Créer une classe dérivée :
class Bio extends Name { }

// Créer une nouvelle instance d'objet :
const myBio = new Bio();

// Vérifier la valeur actuelle de myBio :
myBio;

// L'appel ci-dessus retournera :
{ myName: "Oluwatobi" }
```

[**Essayer de le modifier**][81]

La classe `Bio` a hérité de la propriété de son parent car nous avons utilisé le mot-clé `extends` pour assigner la classe `Name` comme dunder proto de la classe dérivée.

**Note :** Un champ de classe d'une classe dérivée remplacera la propriété de sa classe parente portant le même nom. Par exemple, considérez le code suivant :

```
// Créer une nouvelle classe :
class Name {
  myName = "Oluwatobi";
}

// Créer une classe dérivée :
class Bio extends Name {
  myName = "Sofela";
}

// Créer une nouvelle instance d'objet :
const myBio = new Bio();

// Vérifier la valeur actuelle de myBio :
myBio;

// L'appel ci-dessus retournera :
{ myName: "Sofela" }
```

[**Essayer de le modifier**][82]

JavaScript vous permet également d'utiliser le mot-clé `super` pour accéder aux champs de classe statiques ou prototypaux d'une classe parente à partir de classes dérivées. Discutons-en davantage maintenant.

## Qu'est-ce que le mot-clé `super` en JavaScript ?

Le mot-clé `super` recherche une propriété statique ou prototypale spécifiée dans une classe parente ou un objet littéral.

Par exemple, considérez le fragment suivant :

```
// Créer une nouvelle classe :
class Name {
  constructor() {
    console.log("Oluwatobi is my Name");
  }
}

// Créer une classe enfant :
class Bio extends Name {
  constructor() {
    // Utiliser super pour accéder au constructeur du parent :
    super();
  }
}

// Appeler la classe constructeur Bio :
new Bio();

// L'appel ci-dessus retournera :
"Oluwatobi is my Name."
{}
```

[**Essayer de le modifier**][83]

L'appel de fonction `super()` dans le fragment ci-dessus indique à l'ordinateur de trouver un `constructor` dans la chaîne de prototypes de la classe parente.

Vous pouvez utiliser le mot-clé `super` comme « appelant de fonction » ou « accesseur de propriété ». Voyons comment.

### Comment utiliser le mot-clé `super` comme appelant de fonction

L'appelant de fonction `super()` trouve et appelle la méthode `constructor()` de la classe parente.

En d'autres termes, `super()` vous permet d'accéder au `constructor` d'une classe parente à partir du `constructor` d'une classe dérivée.

#### Syntaxe du mot-clé `super` comme appelant de fonction

```
super(argument1, …, argumentN);
```

**Note :** Un appelant de fonction `super()` n'est valide que dans la méthode `constructor()` d'une classe dérivée.

#### Exemple : Comment utiliser l'appelant de fonction `super()`

```
// Créer une nouvelle classe :
class Name {
  constructor(name) {
    this.name = name;
  }
}

// Créer une classe dérivée :
class Bio extends Name {
  constructor(firstName) {
    // Utiliser super pour accéder au constructeur du parent :
    super(firstName);
  }
}

// Créer une nouvelle instance d'objet :
const myBio = new Bio("Oluwatobi");

// Vérifier la valeur actuelle de myBio :
myBio;

// L'appel ci-dessus retournera :
{ name: "Oluwatobi" }
```

[**Essayer de le modifier**][84]

L'appel de fonction `super()` dans le fragment ci-dessus indique à l'ordinateur de trouver et d'appeler le `constructor()` de la classe parente.

En d'autres termes, l'appel de fonction `super()` recherche un `constructor` dans la chaîne de prototypes de `Name`.

**Notez les points suivants :**

-   L'appel de `super()` permet à JavaScript d'utiliser le `constructor` de la classe parente pour initialiser `this`. Ainsi, un appel de fonction `super()` est similaire à l'écriture de `this = new ParentClass()`.
-   JavaScript vous oblige à appeler `super()` avant d'utiliser le [mot-clé][85] `this`. Sinon, le navigateur lèvera une `ReferenceError`. En d'autres termes, le `constructor` d'une classe dérivée ne peut pas accéder à un mot-clé `this` non initialisé.

#### Exemple : Que se passe-t-il si vous accédez à `this` avant `super` dans le `constructor` d'une classe dérivée ?

```
// Créer une nouvelle classe :
class Name {
  constructor(name) {
    this.name = name;
  }
}

// Créer une classe dérivée :
class Bio extends Name {
  constructor(firstName) {
    this.lastName = "Sofela"; // Utiliser le mot-clé this avant super provoquera une ReferenceError :
    super(firstName);
  }
}

// Créer une nouvelle instance d'objet :
const myBio = new Bio("Oluwatobi");
```

[**Essayer de le modifier**][86]

Le fragment ci-dessus lève une `Uncaught ReferenceError` car le `constructor` d'une classe dérivée ne peut pas accéder au mot-clé `this` avant l'appelant de fonction `super()`.

#### Exemple : Que se passe-t-il si vous utilisez uniquement le mot-clé `this` dans le `constructor` d'une classe dérivée ?

```
// Créer une nouvelle classe :
class Name {
  createName() {
    return "Sofela";
  }
}

// Créer une classe dérivée :
class Bio extends Name {
  constructor() {
    this.firstName = "Oluwatobi"; // Utiliser le mot-clé this avant super provoquera une ReferenceError :
  }
}

// Créer une nouvelle instance d'objet :
const myBio = new Bio();
```

[**Essayer de le modifier**][87]

Le fragment ci-dessus lève une `Uncaught ReferenceError` car le `constructor` d'une classe dérivée ne peut pas accéder au mot-clé `this` avant l'appelant de fonction `super()`.

Maintenant que nous savons comment utiliser le mot-clé `super` comme appelant de fonction, nous pouvons discuter de son utilisation comme accesseur de propriété.

### Comment utiliser le mot-clé `super` comme accesseur de propriété

Vous pouvez utiliser le mot-clé `super` comme accesseur de propriété dans vos classes JavaScript et vos objets littéraux.

-   **Utilisation dans une classe :** Le mot-clé `super` recherche dans le parent d'une classe un champ de classe statique ou prototypal spécifié. En d'autres termes, `super` vous permet d'accéder aux propriétés statiques ou prototypales d'une classe parente à partir d'une classe enfant.
-   **Utilisation dans un objet littéral :** Le mot-clé `super` recherche dans le parent d'un objet une propriété prototypale spécifiée. En d'autres termes, `super` vous permet d'accéder aux propriétés prototypales de l'objet parent à partir d'un objet enfant.

#### Syntaxe du mot-clé `super` comme accesseur de propriété en notation pointée

```
super.parentClassOrObjectProperty;
```

#### Exemple : Utiliser la notation pointée du mot-clé `super` pour accéder au champ statique de la classe parente

```
// Créer une nouvelle classe :
class Name {
  // Créer un champ de classe statique :
  static myName = "Oluwatobi";
}

// Créer une classe dérivée :
class Bio extends Name {
  // Créer une propriété statique à partir du champ de classe statique du parent :
  static firstName = super.myName;
}

// Vérifier la valeur actuelle de firstName :
Bio.firstName;

// L'appel ci-dessus retournera :
"Oluwatobi"
```

[**Essayer de le modifier**][88]

Nous avons utilisé le mot-clé `super` dans le fragment ci-dessus pour accéder au champ de classe statique de la classe parente.

**Note :** Préfixer l'instruction `firstName` avec un mot-clé `static` fait en sorte que `super` trouve une [propriété statique][89] `myName` dans la classe parente.

Si vous omettez le mot-clé `static`, `super` recherchera une [propriété prototypale][90] `myName` dans la classe parente.

#### Exemple : Utiliser la notation pointée du mot-clé `super` pour accéder au champ prototypal de la classe parente

```
// Créer une nouvelle classe :
class Time {
  // Créer une méthode prototypale :
  hourNow() {
    return new Date().getHours();
  }

  // Créer une seconde méthode prototypale :
  minutesNow() {
    return new Date().getMinutes();
  }
}

// Créer une classe dérivée :
class Moment extends Time {
  // Créer une propriété d'instance en utilisant les méthodes prototypales de la classe parente :
  currentMoment = `The time is ${super.hourNow()}:${super.minutesNow()}.`
}

// Créer une nouvelle instance d'objet :
const momentNow = new Moment();

// Vérifier la valeur actuelle de momentNow :
console.log(momentNow);
```

[**Essayer de le modifier**][91]

Nous avons utilisé le mot-clé `super` dans le fragment ci-dessus pour accéder aux champs de classe prototypaux de la classe parente.

#### Exemple : Utiliser la notation pointée du mot-clé `super` pour accéder à une propriété prototypale d'un objet parent

```
// Créer un nouvel objet :
const website = {
  // Créer une méthode :
  showName() {
    return "CodeSweetly";
  }
}

// Créer un autre objet :
const company = {
  // Créer une méthode :
  showCompany() {
    return super.showName();
  }
}

// Changer le dunder proto de company vers l'objet website :
Object.setPrototypeOf(company, website);

// Appeler la méthode showCompany :
company.showCompany()

// L'appel ci-dessus retournera :
"CodeSweetly"
```

[**Essayer de le modifier**][92]

Nous avons utilisé le mot-clé `super` dans le fragment ci-dessus pour accéder à la méthode `showName()` de l'objet parent.

**Note :** Le code `Object.setPrototypeOf()` change la [propriété `[[Prototype]]`][93] de company vers l'objet website. Par conséquent, la [chaîne de prototypes][94] de l'objet `company` ressemblera à ceci :

```
{ showCompany: showCompany() } ---> { showName: showName() } ---> Object.prototype ---> null
```

Vous pouvez également utiliser le mot-clé `super` comme accesseur de propriété en notation entre crochets pour rechercher une propriété statique ou prototypale spécifiée dans une classe parente ou un objet littéral.

#### Syntaxe du mot-clé `super` comme accesseur de propriété en notation entre crochets

```
super[expresssion];
```

#### Exemple : Utiliser la notation entre crochets du mot-clé `super` pour accéder au champ statique d'une classe parente

```
// Créer une nouvelle classe :
class Name {
  // Créer un champ de classe statique :
  static myName = "Oluwatobi";
}

// Créer une classe dérivée :
class Bio extends Name {
  // Créer une propriété statique à partir du champ de classe statique du parent :
  static firstName = super["myName"];
}

// Vérifier la valeur actuelle de firstName :
Bio.firstName;

// L'appel ci-dessus retournera :
"Oluwatobi"
```

[**Essayer de le modifier**][95]

Nous avons utilisé le mot-clé `super` dans le fragment ci-dessus pour accéder au champ de classe statique de la classe parente.

**Note :** `super` ne peut pas accéder au champ de classe d'instance d'une classe parente car JavaScript définit une propriété d'instance sur l'instance d'objet, et non sur la classe elle-même ou sa chaîne de prototypes. (`super` ne recherche que les propriétés statiques ou prototypales d'un parent.)

#### Exemple : Utiliser le mot-clé `super` pour accéder au champ d'instance de la classe parente

```
// Créer une nouvelle classe :
class Name {
  // Créer un champ de classe d'instance :
  myName = "Oluwatobi";
}

// Créer une classe dérivée :
class Bio extends Name {
  // Créer une propriété d'instance à partir du champ de classe d'instance du parent :
  firstName = super.myName;
}

// Créer une nouvelle instance d'objet :
const myBio = new Bio();

// Vérifier la valeur actuelle de myBio :
myBio;

// L'appel ci-dessus retournera :
{ myName: "Oluwatobi", firstName: undefined }
```

[**Essayer de le modifier**][96]

La valeur de la propriété `firstName` est `undefined` car `super` n'a pas pu trouver de champ `myName` prototypal sur la classe parente.

**Note :** Les mots-clés `super` et [`this`](https://codesweetly.com/javascript-this-keyword) vous permettent de rechercher une propriété spécifiée dans la chaîne de prototypes d'un objet. Mais ils fonctionnent de manières différentes. Discutons de leurs différences maintenant.

### `super` vs mot-clé `this` : quelle est la différence ?

La différence entre les mots-clés `super` et `this` est la suivante :

-   `super` recherche une propriété prototypale spécifiée dans la chaîne de prototypes d'une classe parente.
-   `this` recherche une propriété prototypale spécifiée en partant des propriétés propres de l'instance d'objet d'une classe jusqu'à sa chaîne de prototypes.

En d'autres termes, `super` commence sa recherche à partir de la propriété `prototype` de la classe parente. Mais `this` cherche du scope local d'une instance d'objet jusqu'à sa chaîne de prototypes.

Par exemple, considérez le code suivant :

```
// Créer une nouvelle classe :
class ParentClass {
  // Créer une méthode prototypale :
  showId() {
    return "I am a parent.";
  }
}

// Créer une classe dérivée :
class ChildClass extends ParentClass {
  // Créer une méthode prototypale :
  showId() {
    return "I am a child.";
  }
  // Créer une autre méthode prototypale :
  getId() {
    console.log(super.showId());
    console.log(this.showId());
  }
}

// Créer une nouvelle instance d'objet :
const instanceObject = new ChildClass();

// Appeler la méthode getId() de instanceObject :
instanceObject.getId();

// L'appel ci-dessus retournera :
"I am a parent."
"I am a child."
```

[**Essayer de le modifier**][97]

Voici comment `super` et `this` ont effectué leurs recherches :

|  | super | this |
| --- | --- | --- |
| 1. | Trouve `showId()` dans la chaîne de prototypes de `ParentClass`, en commençant par `ParentClass.prototype`. _Trouvé._ | Trouve `showId()` dans les propriétés propres de `instanceObject`. _Rien trouvé._ |
| 2. | (Supposons que `showId()` ne soit pas dans `ParentClass.prototype`. Dans ce cas, `super` continuerait sa recherche dans `Object.prototype`.) | Trouve `showId()` dans la chaîne de prototypes de `instanceObject`, en commençant par `ChildClass.prototype`. _Trouvé._ |
| 3. |  | (Supposons que `showId()` ne soit pas dans `ChildClass.prototype`. Dans ce cas, `this` continuerait sa recherche dans `ParentClass.prototype`.) |
| 4. |  | (Supposons que `showId()` ne soit pas dans `ChildClass.prototype` ni `ParentClass.prototype`. Dans ce cas, `this` continuerait sa recherche dans `Object.prototype`.) |

Vous pouvez voir que `super` raccourcit les étapes nécessaires pour trouver une méthode prototypale.

Maintenant que nous savons comment utiliser les trois types de classes JavaScript, examinons les composants principaux d'un seul tenant.

## Composants d'une classe JavaScript

Les principales caractéristiques d'une classe JavaScript sont les suivantes :

1.  Un mot-clé `class`
2.  Le nom de la classe
3.  La clause `extends`
4.  Un bloc de code (`{...}`)
5.  Le corps de la classe
6.  Une méthode `constructor`
7.  L'appelant de fonction `super()`
8.  L'accesseur de propriété `super`
9.  Champs de classe d'instance
10.  Champs de classe prototypaux
11.  Champs de classe privés
12.  Champs de classe statiques
13.  Blocs d'initialisation statiques

Voyons ces caractéristiques dans une déclaration de classe.

```
class ChildClass extends ParentClass {
  constructor(parameter) {
    super(parameter);
  }
  instanceClassField = "Value can be any valid JavaScript data type";
  prototypalClassField() {
    // corps de prototypalClassField
  }
  #privateClassField = "Value can be any valid JavaScript data type";
  static classField = "Value can be any valid JavaScript data type";
  static classFieldWithSuperValue = super.parentProperty;
  static #privateClassField = "Value can be any valid JavaScript data type";
  static {
    // Corps du bloc d'initialisation statique
  }
}
```

L'équivalent en fonction constructeur du fragment ci-dessus ressemble à ceci :

```
function ChildClass() {
  this.instanceClassField = "Value can be any valid JavaScript data type";
}

Object.setPrototypeOf(ChildClass, ParentClass);

ChildClass.prototype.prototypalClassField = function () {
  // corps de prototypalClassField
}

ChildClass.staticClassField = "Value can be any valid JavaScript data type";

ChildClass.staticClassFieldWithSuperValue = Object.getPrototypeOf(ChildClass).parentProperty;

(function () {
  // Corps du bloc d'initialisation statique
})();
```

**Note :** Vous ne pouvez actuellement pas créer de champs privés dans les fonctions constructeurs. C'est l'une des dernières fonctionnalités introduites par JavaScript dans les classes.

## Comment une classe JavaScript aide-t-elle à l'encapsulation ?

Les classes vous permettent d'empêcher le code externe d'interagir avec les champs de classe internes. Au lieu de cela, le code externe utiliserait des méthodes publiques pour opérer sur les implémentations internes de la classe.

Par exemple, considérez le code suivant :

```
// Créer une nouvelle classe :
class Name {
  // Créer une donnée de champ de classe privée :
  #myName = "Oluwatobi";

  // Créer une méthode disponible publiquement :
  showMyName() {
    return this.#myName;
  }

  // Créer une autre méthode disponible publiquement :
  updateMyName(value) {
    this.#myName = value;
  }
}

// Créer une nouvelle instance d'objet :
const bio = new Name();

// Vérifier la valeur des données de l'instance :
bio.myName;

// L'appel ci-dessus retournera :
undefined
```

[**Essayer de le modifier**][98]

Le fragment ci-dessus a [encapsulé][99] les données de `Name` car il a défini `myName` comme une fonctionnalité privée et a fourni deux méthodes publiques pour que les utilisateurs puissent lire et mettre à jour l'implémentation interne de la classe.

Par conséquent, l'objet instance `bio` ne sait rien des données internes de la classe et ne peut pas interagir directement avec elles.

Chaque fois que les utilisateurs ont besoin d'accéder aux données encapsulées, ils utilisent les méthodes publiquement disponibles comme ceci :

```
// Vérifier la valeur des données de l'instance :
bio.showMyName();

// L'appel ci-dessus retournera :
"Oluwatobi"

// Mettre à jour la valeur des données de l'instance :
bio.updateMyName("Sofela");

// Vérifier la valeur des données de l'instance :
bio.showMyName();

// L'appel ci-dessus retournera :
"Sofela"
```

[**Essayer de le modifier**][100]

Encapsuler vos données est un excellent moyen de garder votre classe propre. Cela empêche un refactoring interne mineur de casser le code des utilisateurs.

Par exemple, considérez le code suivant :

```
// Créer une nouvelle classe :
class Name {
  // Créer une donnée de champ de classe publique :
  myName = "Oluwatobi";
}

// Créer une nouvelle instance d'objet :
const bio = new Name();

// Vérifier la valeur des données de l'instance :
bio.myName;

// L'appel ci-dessus retournera :
"Oluwatobi"

// Mettre à jour la valeur des données de l'instance :
bio.myName = "Sofela";

// Vérifier la valeur des données de l'instance :
bio.myName;

// L'appel ci-dessus retournera :
"Sofela"
```

Comme le fragment ci-dessus n'a pas encapsulé les données de la classe, le refactoring du nom du champ de classe casserait le code des utilisateurs.

Voici un exemple :

```
class Name {
  // Mettre à jour le nom de la donnée de myName vers myFirstName :
  myFirstName = "Oluwatobi";
}

// Créer une nouvelle instance d'objet :
const bio = new Name();

// Vérifier la valeur des données de l'instance :
bio.myName;

// L'appel ci-dessus retournera :
undefined
```

Le fragment ci-dessus a retourné `undefined` car le refactoring de l'implémentation interne de la classe a cassé le code `bio.myName` de l'utilisateur. Pour que l'application fonctionne correctement, l'utilisateur doit mettre à jour chaque instance du code (ce qui peut être fastidieux pour les grands projets).

Cependant, l'encapsulation empêche un tel refactoring de casser le code de l'utilisateur.

Voici un exemple :

```
class Name {
  // Mettre à jour le nom de la donnée de myName vers myFirstName :
  #myFirstName = "Oluwatobi";

  // Créer une méthode disponible publiquement :
  showMyName() {
    return this.#myFirstName;
  }

  // Créer une autre méthode disponible publiquement :
  updateMyName(value) {
    this.#myFirstName = value;
  }
}

// Créer une nouvelle instance d'objet :
const bio = new Name();

// Vérifier la valeur des données de l'instance :
bio.showMyName();

// L'appel ci-dessus retournera :
"Oluwatobi"

// Mettre à jour la valeur des données de l'instance :
bio.updateMyName("Sofela");

// Vérifier la valeur des données de l'instance :
bio.showMyName();

// L'appel ci-dessus retournera :
"Sofela"
```

Vous pouvez voir que le refactoring de l'implémentation interne de la classe n'a pas cassé le code de l'utilisateur. C'est toute la beauté de l'encapsulation !

L'encapsulation vous permet de fournir aux utilisateurs une interface indépendante des données sous-jacentes de la classe. Par conséquent, vous minimisez la probabilité que le code des utilisateurs se casse lorsque vous modifiez les implémentations internes.

## Choses importantes à savoir sur les classes JavaScript

Voici cinq faits essentiels à retenir lors de l'utilisation des classes JavaScript.

### 1. Déclarez votre classe avant d'y accéder

Les classes sont comme les fonctions constructeurs mais ont le même comportement de [zone morte temporelle][101] que les variables `const` et `let`.

En d'autres termes, JavaScript n'effectue pas de [hoisting][102] sur les déclarations de classe. Par conséquent, vous devez d'abord déclarer votre classe avant de pouvoir y accéder. Sinon, l'ordinateur lèvera une `Uncaught ReferenceError`.

Voici un exemple :

```
// Créer une instance d'objet à partir de la classe Name :
const name = new Name();

// Définir la classe Name :
class Name {}
```

[**Essayer de le modifier**][103]

Le fragment ci-dessus lève une `Uncaught ReferenceError` car JavaScript ne pratique pas le hoisting sur les classes. Ainsi, appeler `Name()` avant sa définition est invalide.

### 2. Les classes sont des fonctions

Le `typeof` d'une classe est une fonction car, sous le capot, le mot-clé `class` crée une nouvelle [fonction][104].

Par exemple, considérez le code suivant :

```
// Définir une classe JavaScript :
class Bio {
  // Définir deux champs de classe d'instance :
  firstName = "Oluwatobi";
  lastName = "Sofela";
  // Créer une méthode prototypale :
  showBio() {
    return `${ firstName } ${ lastName } runs CodeSweetly.`;
  }
}

// Créer une nouvelle instance d'objet :
const aboutMe = new Bio();

// Vérifier quel type de donnée est la classe Bio :
typeof Bio;

// L'appel ci-dessus retournera :
"function"
```

[**Essayer de le modifier**][105]

L'ordinateur traite le fragment ci-dessus comme suit :

1.  Créer une nouvelle fonction nommée `Bio`.
2.  Ajouter les propriétés d'instance de la classe au mot-clé `this` de la fonction nouvellement créée.
3.  Ajouter les propriétés prototypales de la classe à la propriété `prototype` de la fonction nouvellement créée.

### 3. Les classes sont strictes

JavaScript exécute les classes en mode strict. Suivez donc les règles de syntaxe stricte lorsque vous utilisez des classes. Sinon, votre code lèvera des erreurs — dont certaines seront des erreurs silencieuses difficiles à déboguer.

### 4. Évitez le mot-clé `return` dans la méthode `constructor` de votre classe

Supposons que le `constructor` de votre classe retourne une [valeur non primitive][106]. Dans ce cas, JavaScript ignorera les valeurs de tous les mots-clés `this` et assignera la valeur non primitive à l'expression du mot-clé `new`.

En d'autres termes, l'[objet retourné par un `constructor` l'emporte][107] sur son mot-clé `this`.

Par exemple, considérez le code suivant :

```
// Créer une nouvelle classe :
class Name {
  constructor() {
    this.firstName = "Oluwatobi";
    this.lastName = "Sofela";
    return { companyName: "CodeSweetly" };
  }
}

// Créer une nouvelle instance d'objet :
const myName = new Name();

// Vérifier la valeur actuelle de myName :
myName;

// L'appel ci-dessus retournera :
{ companyName: "CodeSweetly" }

// Vérifier la valeur actuelle de firstName :
myName.firstName;

// L'appel ci-dessus retournera :
undefined

// Vérifier la valeur actuelle de lastName :
myName.lastName;

// L'appel ci-dessus retournera :
undefined
```

[**Essayer de le modifier**][108]

L'expression du mot-clé `new` n'a retourné que `{ companyName: "CodeSweetly" }` car JavaScript ignore les mots-clés `this` de la méthode `constructor` chaque fois que vous utilisez un opérateur `return` pour produire un objet.

### 5. L'évaluation d'une classe commence de la clause `extends` vers ses valeurs

JavaScript évalue votre classe selon l'ordre suivant :

#### 1. Clause `extends`

Si vous déclarez une clause `extends`, l'ordinateur l'évaluera en premier.

**Note :** Les navigateurs lèveront une `TypeError` si la clause `extends` ne s'évalue pas en une fonction constructeur ou `null`.

#### 2. Extraire le `constructor` de la classe

JavaScript extrait le `constructor` de la classe.

**Note :** Supposons que vous n'ayez pas défini de méthode `constructor`. Dans ce cas, l'ordinateur utilisera celle par défaut.

#### 3. Analyser les noms de propriétés de la classe

L'ordinateur analyse les noms des champs de classe (pas leurs valeurs) selon leur ordre de déclaration.

#### 4. Analyser les méthodes et les accesseurs de propriété de la classe

JavaScript analyse les méthodes et les accesseurs de propriété de la classe selon leur ordre de déclaration en faisant ce qui suit :

-   Ajouter les méthodes prototypales et les accesseurs de propriété à la propriété `prototype` de la classe.
-   Analyser les méthodes statiques et les accesseurs de propriété comme des propriétés propres de la classe, que vous pouvez appeler sur la classe elle-même.
-   Analyser les méthodes d'instance privées et les accesseurs de propriété comme des propriétés privées de l'objet instance de la classe.

#### 5. Analyser les valeurs de propriétés de la classe

L'ordinateur analyse les valeurs des champs de classe selon leur ordre de déclaration en faisant ce qui suit :

-   Sauvegarder l'expression d'initialisation de chaque champ d'instance pour des évaluations ultérieures. JavaScript évaluera l'expression d'initialisation pendant les périodes suivantes :
    -   Lorsque le mot-clé `new` crée un objet instance.
    -   Pendant le traitement du `constructor` de la classe parente.
    -   Avant que l'appel de fonction `super()` ne retourne.
-   Définir le mot-clé `this` de chaque champ statique sur la classe elle-même et créer la propriété statique sur la classe.
-   Évaluer les [blocs d'initialisation statiques][109] de la classe et définir leur mot-clé `this` sur la classe elle-même.

**Note :**

-   Ce n'est qu'après que JavaScript a analysé les valeurs de propriété d'une classe que celle-ci est entièrement initialisée et disponible en tant que fonction constructeur.
-   Toute tentative d'accéder à la classe enfant avant son initialisation complète retournerait une `ReferenceError`.

## Aperçu

Dans cet article, nous avons discuté de ce qu'est un objet classe JavaScript. Nous avons également utilisé des exemples pour aborder les champs de classe, le mot-clé `super` et l'encapsulation des données.

Merci de m'avoir lu !

### Et voici une ressource utile sur React.JS :

J'ai écrit un livre sur la [création de packages NPM][110] !

C'est un guide accessible aux débutants pour maîtriser l'art de créer, tester et publier des bibliothèques NPM dans l'écosystème React et JavaScript.

Il utilise un projet scalable pour expliquer les fondamentaux de la construction et de la gestion de packages NPM de zéro.

[![Le livre sur la création de packages NPM ReactJS est maintenant disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2024/01/creating-npm-package-reactjs-book-codesweetly.png)][111]

[1]: #heading-qu-est-ce-qu-une-classe-javascript
[2]: #heading-pourquoi-utiliser-les-classes-en-javascript
[3]: #heading-syntaxe-d-une-classe-javascript
[4]: #heading-qu-est-ce-que-le-mot-cle-class
[5]: #heading-qu-est-ce-qu-un-nom-de-classe
[6]: #heading-qu-est-ce-qu-un-bloc-de-code
[7]: #heading-qu-est-ce-qu-un-corps-de-classe
[8]: #heading-qu-est-ce-qu-un-champ-de-classe-javascript
[9]: #heading-comment-creer-des-champs-de-classe-en-javascript
[10]: #heading-comment-creer-des-champs-de-classe-avec-des-noms-calcules
[11]: #heading-comment-creer-des-methodes-de-champ-de-classe-regulieres
[12]: #heading-comment-creer-des-methodes-de-champ-de-classe-raccourcies
[13]: #heading-methodes-de-champ-de-classe-regulieres-vs-raccourcies-quelle-est-la-difference
[14]: #heading-qu-est-ce-qu-une-methode-prototypale-definie-par-l-utilisateur-dans-les-classes-javascript
[15]: #heading-qu-est-ce-qu-une-methode-constructor-dans-les-classes-javascript
[16]: #heading-types-de-champs-de-classe
[17]: #heading-qu-est-ce-qu-un-champ-de-classe-public-dans-les-classes-javascript
[18]: #heading-qu-est-ce-qu-un-champ-de-classe-prive-dans-les-classes-javascript
[19]: #heading-qu-est-ce-qu-un-champ-de-classe-statique-dans-les-classes-javascript
[20]: #heading-types-de-classes-javascript
[21]: #heading-qu-est-ce-qu-une-declaration-de-classe-javascript
[22]: #heading-qu-est-ce-qu-une-expression-de-classe-javascript
[23]: #heading-qu-est-ce-qu-une-classe-derivee-en-javascript
[24]: #heading-qu-est-ce-que-le-mot-cle-super-en-javascript
[25]: #heading-comment-utiliser-le-mot-cle-super-comme-appelant-de-fonction
[26]: #heading-comment-utiliser-le-mot-cle-super-comme-accesseur-de-propriete
[27]: #heading-super-vs-this-quelle-est-la-difference
[28]: #heading-composants-d-une-classe-javascript
[29]: #heading-comment-une-classe-javascript-aide-t-elle-a-l-encapsulation
[30]: #heading-choses-importantes-a-savoir-sur-les-classes-javascript
[31]: #heading-1-declarez-votre-classe-avant-d-y-acceder
[32]: #heading-2-les-classes-sont-des-fonctions
[33]: #heading-3-les-classes-sont-strictes
[34]: #heading-4-evitez-le-mot-cle-return-dans-la-methode-constructor-de-votre-classe
[35]: #heading-5-l-evaluation-d-une-classe-commence-de-la-clause-extends-vers-ses-valeurs
[36]: #heading-apercu
[37]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/Object
[38]: https://codesweetly.com/javascript-new-keyword
[39]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-gtfmeb
[40]: https://codesweetly.com/encapsulation-in-javascript
[41]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
[42]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements
[43]: https://codesweetly.com/method-in-javascript
[44]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-bxe9or
[45]: https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript
[46]: https://codesweetly.com/javascript-properties-object#computed-property-names-in-javascript
[47]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-b9jwfx
[48]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-fro6pz
[49]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-j6kpwy
[50]: https://codesweetly.com/web-tech-terms-i#instance-property-in-javascript
[51]: https://codesweetly.com/web-tech-terms-p#prototypal-property-in-javascript
[52]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object
[53]: https://codesweetly.com/default-function-properties-in-javascript#what-is-the-default-prototype-property-in-javascript-functions
[54]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-xgekwn
[55]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain
[56]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-tfz2hb
[57]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-gzhxdi
[58]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-pqgqew
[59]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments
[60]: https://codesweetly.com/declaration-initialization-invocation-in-programming#what-does-invocation-mean
[61]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-stxiye
[62]: https://codesweetly.com/web-tech-terms-i#instance-property-in-javascript
[63]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-vkvnuv
[64]: https://codesweetly.com/method-in-javascript#shorthand-for-javascript-methods
[65]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-88zwpt
[66]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-4gefar
[67]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-mkabvf
[68]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-7acrhs
[69]: https://codesweetly.com/web-tech-terms-i#instance-property-in-javascript
[70]: https://codesweetly.com/web-tech-terms-p#prototypal-property-in-javascript
[71]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-dcx7ck
[72]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-cvbm6x
[73]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-field/js-wtvny3
[74]: https://codesweetly.com/javascript-variable
[75]: #heading-qu-est-ce-qu-un-champ-de-classe-public-dans-les-classes-javascript
[76]: #heading-qu-est-ce-qu-un-champ-de-classe-statique-dans-les-classes-javascript
[77]: #heading-qu-est-ce-qu-un-champ-de-classe-prive-dans-les-classes-javascript
[78]: https://codesweetly.com/default-function-properties-in-javascript#what-is-the-default-prototype-property-in-javascript-functions-1
[79]: https://codesweetly.com/default-function-properties-in-javascript#what-is-the-default-prototype-property-in-javascript-functions
[80]: https://codesweetly.com/javascript-properties-object
[81]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-jivp9r
[82]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-kxiztt
[83]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-qcdu2a
[84]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-cdc4ks
[85]: https://www.freecodecamp.org/news/the-this-keyword-in-javascript/
[86]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-zyd4dm
[87]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-sgc2tx
[88]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-cr3jfd
[89]: https://codesweetly.com/web-tech-terms-s#static-class-field-in-javascript
[90]: https://codesweetly.com/web-tech-terms-p#prototypal-property-in-javascript
[91]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-fr9bvs
[92]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-mxdvkm
[93]: https://codesweetly.com/default-function-properties-in-javascript#what-is-the-default-prototype-property-in-javascript-functions-1
[94]: https://codesweetly.com/default-function-properties-in-javascript#the-javascript-prototype-chain-diagram
[95]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-vpw14s
[96]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-kqsqqe
[97]: https://codesweetly.com/try-it-sdk/javascript/operators/super-keyword/js-v2st2a
[98]: https://codesweetly.com/try-it-sdk/javascript/encapsulation/js-q7uqv4
[99]: https://codesweetly.com/web-tech-terms-e#encapsulation
[100]: https://codesweetly.com/try-it-sdk/javascript/encapsulation/js-3vq4es
[101]: https://codesweetly.com/javascript-temporal-dead-zone#how-does-vars-tdz-differ-from-let-and-const-variables
[102]: https://www.freecodecamp.org/news/what-is-hoisting-in-javascript-3/
[103]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-74u2wt
[104]: https://codesweetly.com/javascript-function-object
[105]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-spwwdy
[106]: https://codesweetly.com/javascript-non-primitive-data-type
[107]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_properties#returning_overriding_object
[108]: https://codesweetly.com/try-it-sdk/javascript/function/class/class-explained/js-vgwrmg
[109]: https://codesweetly.com/web-tech-terms-s#static-initialization-blocks
[110]: https://amzn.to/48NjBdY
[111]: https://amzn.to/48NjBdY