---
title: Boucle For en JavaScript – Comment parcourir un tableau en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T23:14:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-loop-through-an-array-with-for-loop-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/1_9H5rmyp3MgrcA8i1emsJPg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: Boucle For en JavaScript – Comment parcourir un tableau en JS
seo_desc: 'By Dennis Temoye Charity

  A loop is an instruction in computer programming that allows an application to repeat
  a process until a specific condition is met.

  For example, say you want to run through a list of names and output each name on
  your screen. ...'
---

Par Dennis Temoye Charity

Une boucle est une instruction en programmation informatique qui permet à une application de répéter un processus jusqu'à ce qu'une condition spécifique soit remplie.

Par exemple, supposons que vous vouliez parcourir une liste de noms et afficher chaque nom sur votre écran. Si vous n'utilisiez pas de boucle, vous finiriez par répéter le code pour afficher chaque nom. Mais avec une boucle, vous pouvez afficher chaque nom individuellement sans répéter de code.

Cet article vous guidera à travers le processus de parcours d'un tableau en utilisant les cinq boucles les plus courantes en JavaScript.

## **Qu'est-ce qu'un tableau en JavaScript ?**

Un tableau en JavaScript est une variable que vous pouvez utiliser pour stocker plusieurs éléments. Il se présente généralement sous la forme de crochets contenant différents éléments, des chaînes de caractères et des entiers (ou les deux).

## **Qu'est-ce qu'une boucle en JavaScript ?**

Une boucle est une instruction conditionnelle utilisée pour exécuter une séquence d'instructions jusqu'à ce qu'une condition spécifiée soit remplie. On lui donne une instruction qui répète l'exécution d'un bloc de code et met fin à l'exécution une fois que la condition énoncée est remplie.

Parcourons ce tableau – `let name = ['Dennis', 'Precious', 'Evelyn']` – en utilisant l'une des boucles les plus couramment utilisées en JavaScript.

## **Comment parcourir un tableau avec une boucle For en JavaScript**

Une boucle `for` est une instruction qui répète l'exécution d'un bloc de code tant que la condition n'a pas été remplie et termine l'exécution lorsque la condition est remplie.

Parcourons maintenant un tableau en utilisant la méthode de la boucle `for`.

Je vous conseille de lire attentivement cet article pour ne pas manquer de détails essentiels en cours de route. Mais si vous êtes pressé de parcourir un tableau à l'aide de l'instruction `for`, vous pouvez consulter la syntaxe ci-dessous.

### **Explication rapide de la boucle for :**

C'est le chemin rapide pour parcourir un tableau à l'aide de l'instruction `for` avec un exemple.

Syntaxe :

```js
let name = ['Dennis', 'Precious', 'Evelyn'];
for (let i = 0; i < name.length; i++)
 {
     console.log(name[i]);
}
```

Et voici le résultat :

```js
Dennis
Precious
Evelyn
```

### **Comment fonctionnent les boucles for – plus en détail**

Ici, nous allons comprendre ce qu'est une boucle `for` et comment utiliser cette instruction pour parcourir un tableau avec un exemple.

Pour exécuter une instruction de boucle `for`, vous devez savoir qu'elle doit toujours comporter trois expressions primaires qui sont toujours séparées par un point-virgule.

Syntaxe :

```js
for (expression1; expression2; expression3)
 {
  // code à exécuter
}
```

* expression1 : C'est l'expression d'initialisation (`initialization`), que vous utilisez pour déclarer une variable de compteur de boucle `for` avec les mots-clés `var` ou `let`, comme `var i = 0` ou `let i = 0`.
* expression2 : C'est l'expression de condition (`condition`), qui renvoie soit true (vrai), soit false (faux). Elle détermine si la boucle `for` doit continuer l'exécution ou y mettre fin.

Rappelez-vous qu'une instruction de boucle `for` continue d'exécuter un bloc de code tant que la condition n'a pas été remplie ; elle ne termine la boucle que lorsque la condition est remplie.

* expression3 : C'est l'expression de mise à jour (`update`), qui est généralement utilisée pour incrémenter (`++i`) ou décrémenter (`--i`) la variable de compteur de la boucle `for` chaque fois que la condition de la boucle `for` a été remplie.

Maintenant que nous comprenons les expressions de l'instruction de boucle `for`, travaillons avec un exemple.

Syntaxe :

```js
const arrayName = ['Dennis', 'Precious', 'Evelyn']
for (let i = 0; i < arrayName.length; i++) {
	console.log(arrayName[i]);
}
```

Cette syntaxe ci-dessus parcourt le tableau `name` et affiche dans la console (`console.log()`) les chaînes de caractères du tableau tant que la condition n'a pas été remplie.

D'après la syntaxe ci-dessus :

* Nous avons d'abord initialisé la variable de compteur, `let i = 0;`.
* Ensuite, nous avons donné à la boucle une condition pour terminer la boucle une fois que la valeur de la variable de compteur (`i`) est inférieure à (`<`) la longueur du nom (`name.length;`).
* Vous utilisez le mot-clé `length` pour vérifier la longueur d'une chaîne.

Voici le résultat :

```js
Dennis
Precious
Evelyn
```

## **Conclusion**

Dans ce tutoriel, nous avons abordé les bases d'une boucle for en JavaScript ainsi que la définition d'un tableau. Nous avons également appris à utiliser l'instruction de boucle 'for' de JavaScript pour parcourir un tableau.

Merci de votre lecture.