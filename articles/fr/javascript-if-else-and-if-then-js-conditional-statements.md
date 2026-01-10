---
title: JavaScript If-Else et If-Then – Instructions conditionnelles JS
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-09T23:21:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-if-else-and-if-then-js-conditional-statements
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/walling-e_MdMMKrgdY-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript If-Else et If-Then – Instructions conditionnelles JS
seo_desc: "There will be times where you will want to write commands that handle different\
  \ decisions in your code. \nFor example, if you are coding a bot, you can have it\
  \ respond with different messages based on a set of commands it receives. \nIn this\
  \ article, I..."
---

Il y aura des moments où vous voudrez écrire des commandes qui gèrent différentes décisions dans votre code. 

Par exemple, si vous codez un bot, vous pouvez le faire répondre avec différents messages en fonction d'un ensemble de commandes qu'il reçoit. 

Dans cet article, je vais expliquer ce qu'est une instruction `if...else` et fournir des exemples de code. Nous examinerons également l'opérateur conditionnel (ternaire) que vous pouvez utiliser comme raccourci pour l'instruction `if...else`. 

## Qu'est-ce qu'une instruction if...else en JavaScript ?

Le `if...else` est un type d'instruction conditionnelle qui exécutera un bloc de code lorsque la condition dans l'instruction `if` est `truthy`. Si la condition est `falsy`, alors le bloc `else` sera exécuté. 

Les valeurs `truthy` et `falsy` sont converties en `true` ou `false` dans les instructions `if`.

```js
if (condition est vraie) {
   // code est exécuté
} else {
   // code est exécuté
}
```

Toute valeur qui n'est pas définie comme `falsy` serait considérée comme `truthy` en JavaScript. 

Voici une liste des valeurs `falsy` :

* false
* 0 (zéro)
* -0 (zéro négatif)
* 0n (BigInt zéro)
* `""`, `''`, ```` (chaîne vide)
* null
* undefined
* NaN (not a number)

## Exemples d'instructions if...else en JavaScript

Dans cet exemple, la condition pour l'instruction `if` est `true`, donc le message imprimé dans la console serait "Nick est un adulte."

```js
const age = 18;

if (age >= 18) {
  console.log("Nick est un adulte.");
} else {
  console.log("Nick est un enfant.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.18.12-AM.png)

Mais si je change la variable `age` pour qu'elle soit inférieure à 18, alors la condition serait `false` et le code exécuterait le bloc `else` à la place. 

```js
const age = 12;

if (age >= 18) {
  console.log("Nick est un adulte.");
} else {
  console.log("Nick est un enfant.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.17.07-AM.png)

## Exemples de conditions multiples (instructions if...else if...else) en JavaScript

Il y aura des moments où vous voudrez tester plusieurs conditions. C'est là que le bloc `else if` intervient. 

```js
if (condition 1 est vraie) {
   // code est exécuté
} else if (condition 2 est vraie) {
  // code est exécuté
} else {
   // code est exécuté
}
```

Lorsque l'instruction `if` est `false`, l'ordinateur passera à l'instruction `else if`. Si celle-ci est également `false`, alors il passera au bloc `else`. 

Dans cet exemple, le bloc `else if` serait exécuté parce qu'Alice a entre 18 et 21 ans. 

```js
const age = 18;

if (age < 18) {
  console.log("Alice a moins de 18 ans.");
} else if (age >= 18 && age <= 21) {
  console.log("Alice a entre 18 et 21 ans.");
} else {
  console.log("Alice a plus de 21 ans.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.33.33-AM.png)

## Quand utiliser les instructions switch plutôt que les instructions if...else ? 

Il y a des moments en JavaScript où vous [pourriez envisager d'utiliser une instruction `switch`](https://www.freecodecamp.org/news/javascript-switch-case-js-switch-statement-example/) au lieu d'une instruction `if else`.

Les instructions `switch` peuvent avoir une syntaxe plus propre que les instructions `if else` compliquées.

Regardez l'exemple ci-dessous – au lieu d'utiliser cette longue instruction `if else`, vous pourriez choisir d'utiliser une instruction `switch` plus facile à lire.

```js
const pet = "dog";

if (pet === "lizard") {
  console.log("J'ai un lézard");
} else if (pet === "dog") {
  console.log("J'ai un chien");
} else if (pet === "cat") {
  console.log("J'ai un chat");
} else if (pet === "snake") {
  console.log("J'ai un serpent");
} else if (pet === "parrot") {
  console.log("J'ai un perroquet");
} else {
  console.log("Je n'ai pas d'animal de compagnie");
}
```

```js
const pet = "dog";
 
switch (pet) {
  case "lizard":
    console.log("J'ai un lézard");
    break;
  case "dog":
    console.log("J'ai un chien");
    break;
  case "cat":
    console.log("J'ai un chat");
    break;
  case "snake":
    console.log("J'ai un serpent");
    break;
  case "parrot":
    console.log("J'ai un perroquet");
    break;
  default:
    console.log("Je n'ai pas d'animal de compagnie");
    break;
}
```

Les instructions `switch` ne seront pas appropriées à utiliser dans toutes les situations. Mais si vous trouvez que les instructions `if else` sont longues et compliquées, alors une instruction `switch` pourrait être une option alternative. 

## L'opérateur logique AND (&&) et les instructions if...else en JavaScript

Dans l'opérateur logique AND (`&&`), si les deux conditions sont `true`, alors le bloc `if` sera exécuté. Si l'une ou les deux conditions sont `false`, alors le bloc `else` sera exécuté. 

Dans cet exemple, puisque l'âge est supérieur à 16 et que la variable `ownsCar` est `true`, le bloc `if` sera exécuté. Le message imprimé dans la console sera "Jerry est assez âgé pour conduire et a sa propre voiture."

```js
const age = 17;
const ownsCar = true;

if (age >= 16 && ownsCar) {
  console.log("Jerry est assez âgé pour conduire et a sa propre voiture.");
} else {
  console.log("Jerry ne conduit pas.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.22.49-AM.png)

Si je change la variable `age` pour qu'elle soit inférieure à 16, alors les deux conditions ne sont plus `true` et le bloc `else` serait exécuté à la place. 

```js
const age = 13;
const ownsCar = true;

if (age >= 16 && ownsCar) {
  console.log("Jerry est assez âgé pour conduire et a sa propre voiture.");
} else {
  console.log("Jerry ne conduit pas.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.20.19-AM.png)

## L'opérateur logique OR (||) et les instructions if...else en JavaScript

Dans l'opérateur logique OR (`||`), si l'une ou les deux conditions sont `true`, alors le code à l'intérieur de l'instruction `if` sera exécuté. 

Dans cet exemple, même si la variable `isSale` est définie sur `false`, le code à l'intérieur du bloc `if` sera toujours exécuté parce que la variable `boyfriendIsPaying` est définie sur `true`. 

```js
const boyfriendIsPaying = true;
const isSale = false;

if (boyfriendIsPaying || isSale) {
  console.log("Jesse ira faire du shopping.");
} else {
  console.log("Jesse n'ira pas faire du shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.40.36-AM.png)

Si je devais changer la valeur de la variable `boyfriendIsPaying` en `false`, alors le bloc `else` serait exécuté parce que les deux conditions sont `false`. 

```js
const boyfriendIsPaying = false;
const isSale = false;

if (boyfriendIsPaying || isSale) {
  console.log("Jesse ira faire du shopping.");
} else {
  console.log("Jesse n'ira pas faire du shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.42.12-AM.png)

## L'opérateur logique NOT (!) et les instructions if...else en JavaScript

L'opérateur logique NOT (`!`) prendra quelque chose qui est `true` et le rendra `false`. Il prendra également quelque chose qui est `false` et le rendra `true`.

Nous pouvons modifier l'exemple précédent pour utiliser l'opérateur `!` afin de rendre la variable `boyfriendIsPaying` `false`. Puisque les deux conditions sont `false`, le bloc `else` serait exécuté. 

```js
const boyfriendIsPaying = true;
const isSale = false;

if (!boyfriendIsPaying || isSale) {
  console.log("Jesse ira faire du shopping.");
} else {
  console.log("Jesse n'ira pas faire du shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-5.02.04-AM.png)

## Opérateur conditionnel (ternaire) en JavaScript

Si vous avez une courte instruction `if else`, alors vous pourriez choisir d'utiliser l'opérateur ternaire. Le mot ternaire signifie quelque chose composé de trois parties.

Voici la syntaxe de base pour un opérateur ternaire :

```js
condition ? si condition est vraie : si condition est fausse

```

La condition va avant le `?` et si elle est `true`, alors le code entre le `?` et le `:` serait exécuté. Si la condition est `false`, alors le code après le `:` serait exécuté. 

Dans cet exemple, puisque l'âge est supérieur à 18, alors le message dans la console serait "Peut voter". 

```js
const age = 32;
const citizen = age >= 18 ? "Peut voter" : "Ne peut pas voter";
console.log(citizen);

```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-5.25.14-AM.png)

Voici à quoi ressemblerait le code en utilisant une instruction `if else` :

```js
const age = 32;
let citizen;

if (age >= 18) {
  citizen = "Peut voter";
} else {
  citizen = "Ne peut pas voter";
}

console.log(citizen);
```

## Conclusion

Les instructions `if else` exécuteront un bloc de code lorsque la condition dans l'instruction `if` est `truthy`. Si la condition est `falsy`, alors le bloc `else` sera exécuté. 

Il y aura des moments où vous voudrez tester plusieurs conditions et vous pourrez utiliser une instruction `if...else if...else`. 

Si vous trouvez que l'instruction `if else` est longue et compliquée, alors une instruction `switch` pourrait être une option alternative. 

L'utilisation d'opérateurs logiques pour tester plusieurs conditions peut remplacer les instructions `if else` imbriquées. 

L'opérateur ternaire peut être utilisé pour écrire un code plus court pour une simple instruction `if else`.