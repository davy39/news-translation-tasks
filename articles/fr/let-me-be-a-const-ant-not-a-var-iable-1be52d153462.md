---
title: Laissez-moi être une 'const'(ante), pas une 'var'(iable) !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-28T13:51:49.000Z'
originalURL: https://freecodecamp.org/news/let-me-be-a-const-ant-not-a-var-iable-1be52d153462
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d-yr1HCiJN05bS1m4ooS0w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Laissez-moi être une 'const'(ante), pas une 'var'(iable) !
seo_desc: 'By Srishti Gupta

  var, let and const are the keywords which are used to declare variables in JavaScript.
  var comes under the ECMAScript 5th edition (aka ES5) whereas let and const fall
  under the category of ECMAScript 6th edition (aka ES6 and ES2015)....'
---

Par Srishti Gupta

`var`, `let` et `const` sont les mots-clés utilisés pour déclarer des variables en JavaScript. `var` fait partie de la 5ème édition d'ECMAScript (aka ES5) tandis que `let` et `const` relèvent de la 6ème édition d'ECMAScript (aka ES6 et ES2015).

Puisque JavaScript ne dispose pas de vérification de type, chacun de ces mots-clés peut être utilisé pour déclarer une variable de n'importe quel type (type de données) en JavaScript.

_Bien que les trois mots-clés soient utilisés à la même fin, ils sont différents._

### 'let' vs. 'const' :

#### **Changement de valeur dans le futur**

> Les variables déclarées avec le mot-clé `let` peuvent changer leurs valeurs dans le futur.

Considérez l'exemple donné ci-dessous :

```
let iChange = 11;iChange = 12;
```

```
console.log(iChange);
```

**Sortie :**

```
12
```

À la première ligne, la variable `iChange` est déclarée avec le mot-clé `let` et est initialisée avec la valeur 11. Lorsque vous passez à la ligne suivante, la variable `iChange` se voit attribuer une nouvelle valeur, qui est 12. Changer les valeurs des variables déclarées avec le mot-clé `let` est autorisé. Lorsque, à la dernière ligne, vous essayez d'imprimer la valeur de la variable `iChange`, vous obtenez correctement la valeur mise à jour 12.

> Les variables déclarées avec le mot-clé `const` ne peuvent pas changer leurs valeurs dans le futur. C'est pourquoi vous devez toujours initialiser les variables déclarées avec le mot-clé `const`.

```
const PI = 3.14;PI = 22/7;
```

```
console.log(PI);
```

**Sortie :**

```
Uncaught TypeError: Assignment to constant variable
```

Ici, la variable `PI` est déclarée avec le mot-clé `const` et est initialisée avec la valeur `3.14` à la première ligne. Lorsque vous passez à la ligne suivante, la variable `PI` est mise à jour avec une nouvelle valeur `22/7`. Changer les valeurs des variables déclarées avec le mot-clé `const` n'est pas autorisé. C'est pourquoi la deuxième ligne génère l'erreur montrée dans la sortie parce que vous essayez d'attribuer une nouvelle valeur à une variable constante. Par conséquent, rappelez-vous que les variables déclarées avec le mot-clé `const` sont en lecture seule et ne peuvent pas être réassignées à une autre valeur.

Comme mentionné précédemment, il est obligatoire d'initialiser une constante lors de sa déclaration. Voyons l'instruction de code suivante :

```
const PI;
```

**Sortie :**

```
Uncaught SyntaxError: Missing initializer in const declaration
```

Vous savez que vous ne pouvez pas mettre à jour une constante dans le futur. Si vous n'initialisez pas une constante lors de sa déclaration, vous ne pourrez jamais lui attribuer une valeur ! C'est pourquoi vous obtenez une `SyntaxError` lorsque vous laissez une constante non initialisée.

Que pensez-vous de la sortie du code donné ci-dessous ?

```
const passengerBus = {wheels: 8, passengers: 40}passengerBus.passengers = 50;
```

```
console.log(passengerBus);
```

Pensez-vous qu'une erreur sera générée ? Vérifions la sortie. La voici.

**Sortie :**

```
{ wheels: 8, passengers: 50 }
```

> Les objets (y compris les tableaux et les fonctions) déclarés avec le mot-clé `_const_` sont mutables.

Jusqu'à présent, vous avez appris que les variables déclarées avec le mot-clé `const` ne peuvent pas se voir attribuer une autre valeur. Bien que cela soit vrai, il y a une autre facette de l'histoire. Sans aucun doute, vous ne pouvez pas attribuer une nouvelle valeur à une constante, mais vous pouvez manipuler la valeur existante si c'est un objet ou un tableau.

Dans le code donné ci-dessus, vous ne changez pas toute la valeur attribuée à la constante `passengerBus`, mais vous manipulez une propriété à l'intérieur. Vous pouvez ajouter/supprimer/mettre à jour une propriété à l'intérieur d'un objet déclaré avec le mot-clé `const`.

Il en va de même pour les tableaux. Vous pouvez ajouter/supprimer/mettre à jour un élément à l'intérieur d'un tableau déclaré avec un mot-clé `const`.

```
const android = ['Marshmallow', 'Noughat', 'Oreo'];arr[3] = 'Pie'; // ajout d'une nouvelle version
```

```
console.log(android);
```

**Sortie :**

```
['Marshmallow', 'Noughat', 'Oreo', 'Pie']
```

Maintenant, considérant que les mots-clés `let` et `const` appartiennent à la même catégorie, les points suivants énumèrent les différences entre les variables déclarées avec les mots-clés `let`/`const` et les variables déclarées avec le mot-clé `var` :

### 'let' (ou 'const') vs. 'var' :

#### **Portée**

> Les variables déclarées avec les mots-clés `let`/`const` sont **limitées au bloc**.

Considérez l'exemple suivant :

```
function foo() {   for (let i = 0; i < 3; i++) {      console.log(i); // instruction 1   }   console.log(`All eyes here please: ${i}`); // instruction 2}
```

```
foo();
```

**Sortie :**

```
012Uncaught ReferenceError: i is not defined
```

La variable _i_ est déclarée avec le mot-clé `let` à l'intérieur du bloc for-loop. Cela signifie que lorsque le bloc for-loop se termine, la variable _i_ perd sa portée et n'est plus accessible en dehors des accolades du bloc for-loop. Ainsi, lorsque vous essayez d'accéder à la variable _i_ et d'imprimer sa valeur à l'instruction 2, vous obtenez une `ReferenceError: i is not defined`, comme montré dans la sortie.

Considérez un autre exemple de déclaration d'une variable avec le mot-clé `const` :

```
function placeOrder(status) {   if (status) {      const message = "Order placed successfully!";      console.log(message); // instruction 1   }   console.log(message); // instruction 2}
```

```
placeOrder(true);
```

**Sortie :**

```
Order placed successfullyUncaught ReferenceError: message is not defined
```

La variable `message` est déclarée avec le mot-clé `const` à l'intérieur du bloc if. Cela signifie que lorsque le bloc if se termine, la variable `message` perd sa portée et n'est plus accessible en dehors des accolades du bloc if. C'est pourquoi, lorsque vous essayez d'accéder à la variable `message` et d'imprimer sa valeur à l'instruction 2, vous obtenez une `ReferenceError: message is not defined`, comme montré dans la sortie.

> Les variables déclarées avec le mot-clé `var` sont **limitées à la fonction**.

Considérez l'exemple que nous avons discuté précédemment où, au lieu d'utiliser `let`, vous utilisez le mot-clé `var` pour déclarer la variable _i_ :

```
function foo() {   for (var i = 0; i < 3; i++) {      console.log(i); // instruction 1   }   console.log(`All eyes here please: ${i}`); // instruction 2}
```

```
foo();
```

**Sortie :**

```
012All eyes here please: 3
```

La variable _i_ est déclarée avec le mot-clé `var` à l'intérieur du bloc for-loop. Parce que les variables déclarées avec le mot-clé `var` sont limitées à la fonction, la variable _i_ ne sort pas de la portée lorsque le bloc for-loop se termine et est accessible n'importe où à l'intérieur de la portée de la fonction `foo`. Ainsi, à l'instruction 2, lorsque vous essayez d'accéder à la variable _i_ et d'imprimer sa valeur, vous obtenez la sortie correcte comme `3` (valeur incrémentée de la variable _i_ après l'exécution de l'instruction d'incrément du for-loop) comme montré dans la sortie.

#### Redéclaration

> Les variables déclarées avec les mots-clés `_let_`/`_const_` **ne peuvent pas être redéclarées** dans la même portée.

Que pensez-vous de la sortie du code suivant ?

```
let avengers = 'Infinity War';let avengers = 'Endgame';
```

```
console.log(avengers);
```

**Sortie :**

```
Uncaught SyntaxError: Identifier 'avengers' has already been declared
```

Dans le code ci-dessus, vous avez déclaré une variable avec le nom `avengers` en utilisant le mot-clé `let` puis vous l'avez déclarée à nouveau à la ligne suivante. Ainsi, la deuxième ligne génère une `SyntaxError` comme mentionné dans la sortie.

> Les variables déclarées avec le mot-clé `var` **peuvent être redéclarées** dans la même portée.

Déclarons maintenant une variable déjà déclarée précédemment dans la même portée en utilisant le mot-clé `var`.

```
var avengers = 'Infinity War';var avengers = 'Endgame';
```

```
console.log(avengers);
```

**Sortie :**

```
Endgame
```

Comme le montre la sortie, vous pouvez redéclarer des variables ayant le même nom dans la même portée en utilisant le mot-clé `var`. La valeur contenue dans la variable sera la valeur finale que vous lui avez attribuée.

#### **Hoisting**

> Les variables déclarées avec les mots-clés `_let_`/`_const_` **ne sont PAS hoistées**.

C'est un point important qui est souvent oublié et que vous ne trouverez pas dans tous les articles. Pour comprendre ce que cela signifie, considérez l'exemple donné ci-dessous :

```
console.log(x);let x = 10;
```

**Sortie :**

```
Uncaught ReferenceError: x is not defined
```

Remarquez que à la première ligne dans le code donné ci-dessus, vous essayez d'accéder à une variable _x_, qui est déclarée et assignée à une valeur à la ligne suivante. Essentiellement, vous essayez d'accéder à une variable, qui n'a pas encore été allouée en mémoire (déclarée). Puisque la variable _x_ est déclarée avec le mot-clé `let` et que les variables déclarées avec les mots-clés `let`/`const` ne sont pas hoistées, cela génère une `ReferenceError: x is not defined`, comme montré dans la sortie.

> Les variables déclarées avec le mot-clé `var` sont **hoistées en haut de leur portée**.

```
console.log(x);var x = 10;
```

**Sortie :**

```
undefined
```

Toutes les déclarations sont déplacées en haut de la portée. Remarquez qu'à la première ligne, vous essayez d'accéder à une variable _x_, qui est déclarée et assignée à une valeur à la ligne suivante. Maintenant, puisque la variable _x_ est déclarée avec le mot-clé `var` et que les variables déclarées avec le mot-clé `var` sont hoistées en haut de leur portée en JavaScript, le code est converti en celui donné ci-dessous :

```
var x;console.log(x);x = 10;
```

Ici, la variable _x_ est déclarée à la ligne 1 et ne se voit pas attribuer de valeur. Toutes les variables en JavaScript sont initialisées avec la valeur par défaut `undefined`, si aucune autre valeur n'est explicitement attribuée par l'utilisateur. Ainsi, `x` se voit attribuer la valeur `undefined`, qui est ce qui est imprimé à la deuxième ligne (avant que x ne soit mis à jour à 10).

#### La grande question — Que préférer ?

ES6 (aka ES2015) est supporté par presque tous les navigateurs aujourd'hui. Si vous pouvez suivre cette syntaxe, il est recommandé d'utiliser les mots-clés `let` et `const` pour déclarer toutes les variables dans votre code.

Maintenant, lequel choisir parmi `let` et `const` ? Le titre dit tout.

![Image](https://cdn-media-1.freecodecamp.org/images/rj5mGjbr0EVJzlpIYxLgMluer6heMLZSsG0i)