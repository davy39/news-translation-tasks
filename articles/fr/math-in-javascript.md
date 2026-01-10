---
title: Fonctions Mathématiques JavaScript Expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T18:25:00.000Z'
originalURL: https://freecodecamp.org/news/math-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc6740569d1a4ca398d.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: Fonctions Mathématiques JavaScript Expliquées
seo_desc: 'Math

  Math is one of JavaScript''s global or standard built-in objects, and can be used
  anywhere you can use JavaScript. It contains useful constants like π and Euler’s
  constant and functions such as floor(), round(), and ceil().

  In this article, we''ll...'
---

## **Math**

`Math` est l'un des objets globaux ou intégrés standard de JavaScript, et peut être utilisé partout où vous pouvez utiliser JavaScript. Il contient des constantes utiles comme π et la constante d'Euler, ainsi que des fonctions telles que `floor()`, `round()` et `ceil()`.

Dans cet article, nous examinerons des exemples de nombreuses de ces fonctions. Mais d'abord, apprenons-en plus sur l'objet `Math`.

### **Exemple**

L'exemple suivant montre comment utiliser l'objet `Math` pour écrire une fonction qui calcule l'aire d'un cercle :

```javascript
function calculateCircleArea(radius) {
  return Math.PI * Math.pow(radius, 2);
}

calculateCircleArea(1); // 3.141592653589793
```

## **Math Max**

`Math.max()` est une fonction qui retourne la valeur la plus grande d'une liste de valeurs numériques passées en paramètres. Si une valeur non numérique est passée en paramètre, `Math.max()` retournera `NaN`.

Un tableau de valeurs numériques peut être passé comme un seul paramètre à `Math.max()` en utilisant soit `spread (...)` soit `apply`. Cependant, l'une ou l'autre de ces méthodes peut échouer lorsque le nombre de valeurs du tableau devient trop élevé.

### **Syntaxe**

```js
Math.max(value1, value2, value3, ...);
```

### **Paramètres**

Nombres, ou tableau limité de nombres.

### **Valeur de retour**

La plus grande des valeurs numériques données, ou `NaN` si une valeur donnée est non numérique.

### **Exemples**

_Nombres en tant que paramètres_

```js
Math.max(4, 13, 27, 0, -5); // retourne 27
```

_Paramètre invalide_

```js
Math.max(4, 13, 27, 'eight', -5); // retourne NaN
```

_Tableau en tant que paramètre, utilisant Spread(5)_

```js
let numbers = [4, 13, 27, 0, -5];

Math.max(...numbers); // retourne 27
```

_Tableau en tant que paramètre, utilisant Apply_

```js
let numbers = [4, 13, 27, 0, -5];

Math.max.apply(null, numbers); // retourne 27
```

## Math Min

La fonction Math.min() retourne la plus petite valeur parmi zéro ou plusieurs nombres.

Vous pouvez lui passer n'importe quel nombre d'arguments.

```javascript
Math.min(7, 2, 9, -6);
// retourne -6
```

## Math PI

`Math.PI` est une propriété statique de l'objet Math et est définie comme le rapport entre la circonférence d'un cercle et son diamètre. Pi est approximativement 3,14149, et est souvent représenté par la lettre grecque π.

## **Exemples**

```js
Math.PI \\ 3.141592653589793
```

#### **Plus d'informations :**

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI)

## **Math Pow**

`Math.pow()` retourne la valeur d'un nombre élevé à la puissance d'un autre nombre.

#### **Syntaxe**

`Math.pow(base, exponent)`, où `base` est le nombre de base et `exponent` est le nombre par lequel élever la `base`.

`pow()` est une méthode statique de `Math`, donc elle est toujours appelée comme `Math.pow()` plutôt que comme une méthode sur un autre objet.

#### **Exemples**

```js
Math.pow(5, 2); // 25
Math.pow(7, 4); // 2401
Math.pow(9, 0.5); // 3
Math.pow(-8, 2); // 64
Math.pow(-4, 3); // -64
```

#### 

## **Math Sqrt**

La fonction `Math.sqrt()` retourne la racine carrée d'un nombre.

Si un nombre négatif est entré, `NaN` est retourné.

`sqrt()` est une méthode statique de `Math`, donc elle est toujours appelée comme `Math.sqrt()` plutôt que comme une méthode sur un autre objet.

#### **Syntaxe**

`Math.sqrt(x)`, où `x` est un nombre.

#### **Exemples**

```js
Math.sqrt(25); // 5
Math.sqrt(169); // 13
Math.sqrt(3); // 1.732050807568
Math.sqrt(1); // 1
Math.sqrt(-5); // NaN
```

#### 

## **Math Trunc**

`Math.trunc()` est une méthode de l'objet standard Math qui retourne uniquement la partie entière d'un nombre donné en supprimant simplement les unités fractionnaires. Cela entraîne un arrondi global vers zéro. Toute entrée qui n'est pas un nombre entraînera une sortie de NaN.

Attention : Cette méthode est une fonctionnalité ECMAScript 2015 (ES6) et n'est donc pas prise en charge par les anciens navigateurs.

### **Exemples**

```javascript
Math.trunc(0.1)   //  0
Math.trunc(1.3)   //  1
Math.trunc(-0.9)  // -0
Math.trunc(-1.5)  // -1
Math.trunc('foo') // NaN
```

## Math Ceil

La méthode `Math.ceil()` est une méthode de l'objet standard Math qui arrondit un nombre donné vers le haut à l'entier suivant. Notez que pour les nombres négatifs, cela signifie que le nombre sera arrondi « vers 0 » au lieu du nombre de valeur absolue plus grande (voir exemples).

### **Exemples**

```javascript
Math.ceil(0.1)  //  1
Math.ceil(1.3)  //  2
Math.ceil(-0.9) // -0
Math.ceil(-1.5) // -1
```

## Math Floor

`Math.floor()` est une méthode de l'objet standard Math qui arrondit un nombre donné vers le bas à l'entier suivant. Notez que pour les nombres négatifs, cela signifie que le nombre sera arrondi « loin de 0 » au lieu du nombre de valeur absolue plus petite, car `Math.floor()` retourne le plus grand entier inférieur ou égal au nombre donné.

### **Exemples**

```javascript
Math.floor(0.9)  //  0
Math.floor(1.3)  //  1
Math.floor(0.5)  //  0
Math.floor(-0.9) // -1
Math.floor(-1.3) // -2
```

### Une application de math.floor : Comment créer une machine à sous JavaScript

Pour cet exercice, nous devons générer trois nombres aléatoires en utilisant une formule spécifique et non la formule générale. `Math.floor(Math.random() * (3 - 1 + 1)) + 1;`

```text
slotOne = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
slotTwo = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
slotThree = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
```

### Un autre exemple : Trouver le reste

### Exemple

```text
5 % 2 = 1 car
Math.floor(5 / 2) = 2 (Quotient)
2 * 2 = 4
5 - 4 = 1 (Reste)
```

### Utilisation

En mathématiques, un nombre peut être vérifié comme pair ou impair en vérifiant le reste de la division du nombre par 2.

```text
17 % 2 = 1 (17 est impair)
48 % 2 = 0 (48 est pair)
```

**Note** Ne le confondez pas avec le _modulus_, `%` ne fonctionne pas bien avec les nombres négatifs.

## Plus d'articles liés aux mathématiques :

* [Convertir une horloge am/pm en heure 24 heures](https://guide.freecodecamp.org/mathematics/converting-am-pm-to-24-hour-clock/)
* [La règle de Simpson](https://www.freecodecamp.org/news/simpsons-rule/)
* [Qu'est-ce qu'un hexagone ?](https://guide.freecodecamp.org/mathematics/hexagon/)