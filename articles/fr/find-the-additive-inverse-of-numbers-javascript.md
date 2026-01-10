---
title: Comment trouver l'inverse additif de chaque nombre en JavaScript [Défi CodeWars
  Résolu]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T20:20:50.000Z'
originalURL: https://freecodecamp.org/news/find-the-additive-inverse-of-numbers-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/volkan-olmez-aG-pvyMsbis-unsplash.jpg
tags:
- name: coding challenge
  slug: coding-challenge
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: Comment trouver l'inverse additif de chaque nombre en JavaScript [Défi
  CodeWars Résolu]
seo_desc: "By Madison Kanna\nIn this tutorial, we'll go over how to solve the CodeWars\
  \ invert values problem in JavaScript. \nInstead of just diving into the code, we'll\
  \ first read through the problem and make sure we understand it. Next we'll write\
  \ pseudocode th..."
---

Par Madison Kanna

Dans ce tutoriel, nous allons voir comment résoudre le problème CodeWars [invert values](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/javascript) en JavaScript. 

Au lieu de plonger directement dans le code, nous allons d'abord lire le problème et nous assurer de bien le comprendre. Ensuite, nous écrivons un pseudocode que nous utiliserons comme guide pour résoudre le problème. Enfin, nous écrivons le code lui-même. 

Commençons !

## D'abord, lire le problème

Voici la description du problème :

**Étant donné un ensemble de nombres, retourner l'inverse additif de chacun. Chaque nombre positif devient négatif, et les nombres négatifs deviennent positifs.**

**Vous pouvez supposer que toutes les valeurs sont des entiers. Ne pas muter le tableau/liste d'entrée.**

Pour résoudre ce problème, nous devons d'abord nous assurer de bien le comprendre. Passons en revue quelques questions que nous pouvons nous poser pour nous aider à comprendre ce problème.

## Quelles sont les entrées ?

Quelles sont les entrées possibles pour ce problème ? Que recevra cette fonction ?

La description du problème dit : "_étant donné un ensemble de nombres_". Cela nous indique que nos entrées sont un ensemble de nombres. 

Le problème nous dit également de supposer que tous ces nombres seront des entiers. 

Enfin, d'après les exemples donnés par le problème, nous pouvons voir que l'ensemble de nombres sera à l'intérieur d'un tableau :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-58.png)

En rassemblant ces informations, nous pouvons dire que notre entrée sera un tableau d'entiers.

## Quelles sont les sorties ?

Ensuite, nous pouvons nous demander, quelles sont les sorties ? Que retournera cette fonction ?

Nous pouvons voir, d'après l'exemple du problème, que notre sortie est un tableau avec chaque nombre changé en son inverse additif. 

Maintenant, nous connaissons les entrées et la sortie. Ensuite, nous passerons en revue quelques exemples du problème.

## Quels sont quelques exemples d'entrées et de sorties ?

Nous avons déjà des exemples d'entrées et de sorties à partir du problème ci-dessus, mais parfois il peut être utile d'en écrire quelques-uns par soi-même pour mieux comprendre ce que le problème demande. Voici un exemple d'entrée et de sortie :

```javascript
//entrée
[2, 3, -4]

//sortie
[-2, -3, 4]
```

Maintenant, nous connaissons nos entrées et sorties, et nous avons quelques exemples. 

Nous sommes prêts à passer à l'écriture de notre pseudocode, la dernière étape avant de coder notre solution. Le pseudocode est une description en langage simple des étapes d'un algorithme. Le pseudocode nous aidera à créer un plan pour résoudre ce défi. 

Pour écrire notre pseudocode, décomposons d'abord le problème étape par étape.

## Comment décomposer le problème

Nous devons pouvoir examiner et faire quelque chose à chaque nombre dans le tableau d'entrée. Nous voulons également retourner un nouveau tableau avec chaque nombre modifié. 

Pour ce faire, nous pouvons utiliser la méthode `map` en JavaScript, qui retourne un nouveau tableau rempli avec les résultats de l'appel d'une fonction fournie sur chaque élément du tableau appelant.

Nous allons écrire cela en pseudocode comme notre première étape : 

```javascript
//étape un : parcourir chaque nombre dans le tableau en utilisant la méthode map
```

Pour chaque nombre dans le tableau, nous voulons le changer en son inverse additif. Nous devons comprendre ce que cela signifie, alors clarifions la définition de l'inverse additif :

En mathématiques, l'**inverse additif** d'un nombre a est le nombre qui, lorsqu'il est ajouté à a, donne zéro. Voici quelques exemples :

L'inverse additif de -10 est +10, car -10 + 10 = 0

L'inverse additif de -2 est +2, car -2 + 2 = 0

Pour obtenir l'inverse additif d'un nombre, nous pouvons le multiplier par -1. Nous pouvons tester cela avec quelques exemples :

`10 * -1 = -10`

`-2 * -1 = 2`

Nous savons maintenant que si nous multiplions chaque nombre par -1, nous obtiendrons l'inverse additif de ce nombre. Nous pouvons ajouter cela à notre pseudocode :

```
/* 
étape un : parcourir chaque nombre dans le tableau en utilisant la méthode map
étape deux : multiplier chaque nombre par -1
*/

```

Enfin, nous devons retourner notre nouveau tableau. 

```
/* 
étape un : parcourir chaque nombre dans le tableau en utilisant la méthode map
étape deux : multiplier chaque nombre par -1
étape trois : retourner le nouveau tableau
*/

```

## Comment coder la solution

Maintenant que nous avons écrit notre pseudocode, nous pouvons coder notre solution en l'utilisant comme guide.

```
function invert(array) {
   return array.map(num =>   {
     return num * -1
   })
}
```

Lorsque nous testons notre solution sur CodeWars, cela fonctionne ! Nous créons notre fonction, `invert`, qui accepte un tableau de nombres. Nous parcourons notre tableau avec map, et pour chaque nombre, nous le multiplions par -1. Ensuite, nous retournons notre nouveau tableau.

Nous pouvons voir qu'il passe tous les tests. Si nous voulons rendre notre solution un peu plus propre, nous pouvons faire un retour implicite et supprimer les accolades intérieures et le mot-clé `return` intérieur. 

```
function invert(array) {
   return array.map(num => num * -1)
}
```

C'est tout ! Nous avons maintenant terminé notre problème d'inversion de valeurs. Nous nous sommes assurés de bien comprendre le problème, nous avons écrit les étapes pour le résoudre en pseudocode, puis nous avons codé la solution.

Pour voir les autres solutions à ce problème, vous pouvez les consulter [ici](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/solutions/javascript). 

### **Merci d'avoir lu !**

Si vous avez aimé cet article, inscrivez-vous à [ma liste de diffusion](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f) où j'envoie mes derniers articles et annonce les réunions de mon club de lecture de codage.

Si vous avez des commentaires ou des questions sur cet article, n'hésitez pas à me tweeter @[madisonkanna](https://twitter.com/Madisonkanna).