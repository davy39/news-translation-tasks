---
title: Tutoriel sur la boucle For en JS – Comment itérer sur un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T19:32:45.000Z'
originalURL: https://freecodecamp.org/news/javascript-loop-tutorial-how-to-iterate-over-an-array-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b53740569d1a4ca2b1a.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: Tutoriel sur la boucle For en JS – Comment itérer sur un tableau en JavaScript
seo_desc: "By Marty Jacobs\nThis article will provide you with a solid understanding\
  \ of exactly how to iterate over an Array data structure in JavaScript. \nWhether\
  \ you are just beginning to learn JavaScript or are here for a refresher, there\
  \ will be value for yo..."
---

Par Marty Jacobs

Cet article vous permettra de comprendre précisément comment itérer sur une structure de données de type Array (tableau) en JavaScript.

Que vous commenciez tout juste à apprendre le JavaScript ou que vous soyez ici pour un rappel, vous y trouverez de la valeur dans les deux cas. Cet article vous guidera à travers l'un des concepts les plus utilisés en JavaScript.

### Qu'est-ce qu'un tableau ?

```js
let cars = ["Tesla", "Ferrari", "Lamborghini", "Audi"];
```

Ci-dessus se trouve un tableau JavaScript utilisé pour stocker plusieurs valeurs. C'est l'une des formes les plus simples d'un tableau. Il contient 4 « éléments » à l'intérieur du tableau, tous des strings. Et comme vous pouvez le voir, chaque élément est séparé par une virgule.

Cet exemple de tableau contient différentes marques de voitures et peut être référencé avec la variable `cars`.

Il existe plusieurs façons d'itérer sur ce tableau. JavaScript est incroyablement riche en fonctionnalités, nous avons donc le luxe de choisir la meilleure façon de résoudre notre problème.

Voici comment nous allons aborder l'itération sur les tableaux en JavaScript :

1. Mettre en avant 5 méthodes courantes pour itérer sur un tableau
2. Donner un aperçu de chaque méthode itérative
3. Fournir du code que vous pourrez également utiliser pour tester !

## La boucle For traditionnelle

### Qu'est-ce qu'une boucle For ?

Voici une définition simple d'une [boucle for](https://en.wikipedia.org/wiki/For_loop) :

> « En informatique, une **boucle for** (ou simplement **boucle for**) est une [instruction](https://en.wikipedia.org/wiki/Statement_(programming)) de [contrôle de flux](https://en.wikipedia.org/wiki/Control_flow) permettant de spécifier une [itération](https://en.wikipedia.org/wiki/Iteration), **ce qui permet au code d'être [exécuté](https://en.wikipedia.org/wiki/Execution_(computers)) de manière répétée.** »

Une boucle for est un moyen d'exécuter du code de manière répétée. Au lieu de taper `console.log("salut")` cinq fois, vous pourriez l'envelopper dans une boucle for.

Dans ce premier exemple, nous allons apprendre à itérer sur le tableau `cars` que vous avez vu plus haut, et à afficher chaque élément. L'itérateur, ou compteur, commencera au premier index « Tesla » et se terminera au dernier « Audi ». Il parcourt le tableau et affiche un élément à la fois.

```js
let cars = ["Tesla", "Ferrari", "Lamborghini", "Audi"];

for(let i = 0; i < cars.length; i++) {
  console.log(cars[i]);
}
```

**Sortie :**

```
Tesla
Ferrari
Lamborghini
Audi
```

En plongeant dans le code, nous passons trois options à la boucle for :

* la variable d'itérateur - `let i = 0;`
* où l'itérateur doit s'arrêter - `i < cars.length`
* de combien incrémenter l'itérateur à chaque boucle - `i++`

Cette boucle nous fait démarrer à `0`, augmente la variable de un à chaque boucle et s'arrête lorsque nous atteignons le dernier élément du tableau.

_Le principal avantage de la boucle for traditionnelle est que vous avez plus de contrôle._

Il est possible d'accéder à différents éléments au sein du tableau, ou d'itérer à travers le tableau d'une manière sophistiquée pour résoudre un problème complexe. Par exemple, sauter un élément sur deux dans le tableau peut être fait assez facilement avec la boucle for traditionnelle.

## La méthode forEach

### Qu'est-ce que la méthode forEach ?

La méthode `forEach` est utilisée pour exécuter une fonction pour chaque élément de votre tableau. Cette méthode est un excellent choix si la longueur du tableau est « inconnue » ou susceptible de changer. Cette méthode ne peut être utilisée qu'avec les Arrays, les Sets et les Maps.

```js
const amounts = [65, 44, 12, 4];
let doubledAmounts = [];

amounts.forEach(item => {
  doubledAmounts.push(item * 2);
})

console.log(doubledAmounts);
```

Le plus grand avantage d'une boucle `forEach` est de pouvoir accéder à chaque élément, même si votre tableau est susceptible de s'agrandir. C'est une solution évolutive pour de nombreux cas d'utilisation et elle est plus facile à lire et à comprendre qu'une boucle for traditionnelle car nous savons que nous allons itérer sur chaque élément exactement une fois.

## La boucle While

### Qu'est-ce qu'une boucle While ?

Voici une définition simple d'une boucle While :

> « Une **boucle while** est une instruction de contrôle de flux qui permet d'exécuter du code de manière répétée en fonction d'une condition [booléenne](https://en.wikipedia.org/wiki/Boolean_datatype) donnée. La boucle _while_ peut être considérée comme une instruction if répétitive. »

Une boucle `while` est un moyen d'exécuter du code de manière répétée pour vérifier si une condition est vraie ou fausse. Ainsi, au lieu d'utiliser une boucle for avec une instruction if imbriquée, nous pouvons utiliser une boucle while. Ou, si nous ne sommes pas en mesure de trouver la longueur du tableau, les boucles while sont un excellent choix.

The boucle while est souvent contrôlée par un compteur. Dans l'exemple ci-dessous, nous montrons une boucle while de base itérant à travers un tableau. La clé est d'avoir le contrôle sur la boucle while que vous créez.

**Exemple de boucle While (Bon) :**

```js
let i = 0 

while (i < 5) { 
  console.log(i); 
  i++; 
}
```

**Sortie** :

```
0
1
2
3
4
```

L'instruction if de la boucle while est `i < 5`, ou dit à haute voix, « i est inférieur à 5 ». La variable `i` est incrémentée à chaque fois que la boucle s'exécute.

En termes simples, cela signifie que 1 est ajouté à la variable `i` chaque fois que la boucle effectue une itération complète. Lors de la première itération, `i` est égal à 0, et nous affichons « 0 » dans la console.

_Le plus grand risque lié à l'utilisation d'une boucle while est d'écrire une condition qui n'est jamais remplie._

Cela se produit fréquemment dans des scénarios réels, où quelqu'un écrit une boucle while mais oublie de tester sa boucle, ce qui introduit une [boucle infinie](https://en.wikipedia.org/wiki/Infinite_loop) dans la base de code.

Une boucle infinie se produit lorsque la condition n'est jamais remplie et que la boucle continue de s'exécuter éternellement. Cela entraîne souvent des changements critiques, qui provoquent ensuite le plantage et l'arrêt de l'application logicielle entière.

**Attention : n'exécutez pas ce code.**

**Exemple de boucle infinie (Mauvais) :**

```js
let i = 0 

while (i < 5) { 
  console.log(i); 
}
```

**Sortie :**

Les résultats peuvent varier.

## La boucle Do While

### Qu'est-ce qu'une boucle do while ?

Voici une définition simple d'une boucle Do-While :

> « une **boucle do while** est une instruction de contrôle de flux qui exécute un bloc de code **au moins une fois**, puis exécute le bloc de manière répétée, ou non, en fonction d'une condition booléenne donnée à la fin du bloc. »

Une boucle do-while est presque identique à une boucle while, mais il y a une différence clé. La boucle do-while garantit de toujours exécuter le bloc de code au moins une fois avant que l'instruction if ne soit vérifiée.

Je la considère souvent comme une boucle while inversée, et je ne les utilise presque jamais. Cependant, elles s'avèrent utiles dans certains scénarios très spécifiques.

**Exemple de boucle Do-While (Bon) :**

```js
let i = 0; 

do { 
  console.log(i); 
  i++; 
} while (i < 5);
```

**Sortie** :

```
0
1
2
3
4
```

_Le plus grand risque lié à l'utilisation d'une boucle do-while est d'écrire une condition qui n'est jamais remplie. (Idem que pour une boucle While.)_

**Attention : n'exécutez pas ce code.**

**Exemple de boucle infinie (Mauvais) :**

```js
let i = 0; 

do { 
  console.log(i); 
} while (i < 5);
```

**Sortie** :

Les résultats peuvent varier.

Vous voulez faire passer vos connaissances en JavaScript au niveau supérieur ? Apprenez-en plus sur `map`, qui est identique à `forEach`, mais avec un bonus !! ✨

## Exemple BONUS (Itération avec map)

### Qu'est-ce que map ?

Voici une définition simple de map :

> « Dans de nombreux [langages de programmation](https://en.wikipedia.org/wiki/Programming_language), **map** est le nom d'une [fonction d'ordre supérieur](https://en.wikipedia.org/wiki/Higher-order_function) qui applique une [fonction donnée](https://en.wikipedia.org/wiki/Procedural_parameter) à chaque élément d'un [foncteur](https://en.wikipedia.org/wiki/Functor_(disambiguation)), par exemple une [liste](https://en.wikipedia.org/wiki/List_(computing)), en renvoyant une liste de résultats dans le même ordre. Elle est souvent appelée _apply-to-all_ lorsqu'elle est considérée sous une [forme fonctionnelle](https://en.wikipedia.org/wiki/Functional_form). »

Comment ça marche ? La fonction `map` en JavaScript applique une fonction à _chaque élément_ du tableau. Veuillez prendre un moment pour relire cette phrase.

Ensuite, la fonction `map` renvoie un nouveau tableau avec les résultats de l'application d'une fonction à chaque élément du tableau.

**Exemple de map :**

```js
const array = [1, 1, 1, 1];

// passer une fonction à map
const results = array.map(x => x * 2);

console.log(results);
```

**Sortie** :

```
[2,2,2,2]
```

Nous avons appliqué la fonction `map` au tableau contenant quatre 1. La fonction `map` a ensuite multiplié chaque élément par 2, c'est-à-dire `x * 2`, et a renvoyé un nouveau tableau. Le nouveau tableau a ensuite été stocké dans la variable `results`.

En regardant notre sortie, nous pouvons voir que cela a fonctionné avec succès. Chaque élément du tableau a été multiplié par 2. Cette méthode peut être utilisée en remplacement d'une boucle dans certains cas, et elle est incroyablement puissante.

## Conclusion

Bravo ! Vous avez appris cinq façons différentes d'itérer sur un tableau en JavaScript. Ce sont les briques fondamentales qui vous prépareront au succès dans votre parcours de programmation JavaScript.

Vous avez également été exposé à un concept avancé, `map`, qui est souvent utilisé dans les applications logicielles à grande échelle.

Alors, je vous laisse sur ceci : comment allez-vous utiliser les tableaux dans vos projets ? Et quelle méthode d'itération avez-vous trouvée la plus intéressante ?

**_Merci de m'avoir lu !_**

Si vous avez aimé mon article, n'hésitez pas à me suivre et/ou à m'envoyer un message !

**[Twitter](https://twitter.com/MartyJacobsDev) • [Medium](https://medium.com/@majikarpp) • [Github](https://github.com/majikarp)**