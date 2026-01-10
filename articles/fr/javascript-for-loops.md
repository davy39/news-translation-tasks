---
title: Boucle For en JavaScript – Expliqué avec des Exemples
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-05-27T16:32:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-for-loops
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/for-loops.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: Boucle For en JavaScript – Expliqué avec des Exemples
seo_desc: 'Loops are a programming concept that we constantly encounter and implement
  as JavaScript developers.

  And many developers are familiar with loops, but not everyone understands how they
  work and why or when they should use a specific type of loop.

  In t...'
---

Les boucles sont un concept de programmation que nous rencontrons et implémentons constamment en tant que développeurs JavaScript.

Et de nombreux développeurs sont familiers avec les boucles, mais tout le monde ne comprend pas comment elles fonctionnent et pourquoi ou quand ils devraient utiliser un type spécifique de boucle.

Dans cet article, nous allons apprendre ce que sont les boucles for, comment elles fonctionnent et pourquoi nous les utilisons. Nous garderons également à l'esprit qu'il existe plusieurs types de boucles, chacune remplissant une fonction spécifique même si elles peuvent presque toutes remplir la même fonction commune.

## Qu'est-ce que les Boucles ?

Les boucles sont des programmes informatiques qui exécutent un ensemble d'instructions ou un bloc de code un certain nombre de fois sans avoir à le réécrire jusqu'à ce qu'une certaine condition soit remplie. En d'autres termes, les boucles permettent à votre code d'exécuter une ou plusieurs instructions autant de fois que souhaité.

Encore une fois, il existe de nombreux types de boucles, mais nous ne regarderons que la boucle for dans cet article.

Presque tous les langages de programmation de haut niveau, y compris JavaScript, ont une boucle for. Nous allons seulement regarder JavaScript dans cet article, et nous examinerons sa syntaxe et quelques exemples.

### Boucles For en JavaScript

La boucle for est une instruction itérative que vous utilisez pour vérifier certaines conditions puis exécuter répétitivement un bloc de code tant que ces conditions sont remplies.

![Image](https://paper-attachments.dropbox.com/s_3315FAFA14C012362B87C753E4A1C2D25C00228882CEE2A5B63A9FDA99BA4B77_1653509464069_for+loop+flowchart+1.jpg align="left")

*Organigramme de la boucle for*

### Syntaxe d'une boucle for

```javascript
for (initialExpression; condition; updateExpression) {
    // corps de la boucle for : instruction
}
```

Le bloc de code ci-dessus est la syntaxe standard utilisée par la boucle for. Examinons chaque paramètre pour voir ce qu'il signifie et ce qu'il fait :

* `initialExpression` : Cela est utilisé pour définir la valeur d'une variable de compteur, et elle n'est évaluée qu'une seule fois, avant le début de la boucle. Selon la portée, ces variables de compteur sont généralement déclarées avec les mots-clés `var` ou `let`.
    
* `condition` : Il s'agit d'une expression d'évaluation constante qui détermine si la boucle doit être exécutée. En termes simples, si cette condition retourne vrai, le bloc de code de la boucle for est exécuté. Si elle retourne faux, la boucle for est terminée.
    
* `updateExpression` : Cela est couramment utilisé pour mettre à jour ou incrémenter la variable de compteur `initialExpression`. En d'autres termes, lorsque la condition est vraie, elle met à jour la valeur de `initialExpression`.
    

En résumé, la boucle for fait en sorte que la variable `initialExpression`, qui est définie à une valeur de départ, augmente ou diminue en réponse à `updateExpression` tant que la condition est remplie. Enfin, l'instruction sera toujours exécutée si la condition est évaluée à vrai.

## Exemples de Boucles For en JavaScript

À ce stade, nous comprenons maintenant ce que sont les boucles, alors regardons quelques exemples et voyons comment nous pouvons utiliser les boucles.

### Comment Afficher du Texte Plusieurs Fois

Commençons par afficher du texte plusieurs fois jusqu'à ce que notre condition soit remplie.

```javascript
for (var i = 0; i < 3; i++) {
  let name = "John Doe";
  console.log("Hi, my name is " + name);
}
```

**Sortie :**

```bash
"Hi, my name is John Doe"
"Hi, my name is John Doe"
"Hi, my name is John Doe"
```

Voici comment le programme a traité cette boucle :

| Itération | Variable | Condition : i < 3 | Action & mise à jour de la variable |
| --- | --- | --- | --- |
| 1ère | i = 0 | vrai | Hi, my name is John Doe est imprimé. |
| 2ème | i = 1 | vrai | Hi, my name is John Doe est imprimé. |
| 3ème | i = 2 | vrai | Hi, my name is John Doe est imprimé. |
| 4ème | i=3 | faux | La boucle est terminée. |

**Note :** La boucle est terminée parce que 3 n'est pas inférieur à 3, donc elle a retourné `false`.

### Comment Afficher une Séquence de Nombres avec une Boucle For

Cette fois-ci, affichons une séquence de nombres en affichant la valeur de l'itération.

```javascript
for (let i = 2; i <= 5; i++) {
    console.log(i);  // impression de la valeur de i
}
```

**Sortie :**

```bash
2
3
4
5
```

Voici comment le programme a traité cette boucle :

| Itération | Variable | Condition : i <= 5 | Action & mise à jour de la variable |
| --- | --- | --- | --- |
| 1ère | i = 2 | vrai | 2 est imprimé. |
| 2ème | i = 3 | vrai | 3 est imprimé. |
| 3ème | i = 4 | vrai | 4 est imprimé. |
| 5ème | i = 5 | vrai | 5 est imprimé. |
| 6ème | i = 6 | faux | La boucle est terminée. |

**Note :** La boucle est terminée parce que 6 n'est pas inférieur ou égal à 5, donc la condition retourne faux.

### Comment Afficher une Séquence de Nombres Pairs

Affichons maintenant une séquence de nombres pairs uniquement en affichant la valeur de l'itération :

```javascript
for (let i = 2; i <= 10; i+=2) {
    console.log(i);  // impression de la valeur de i
}
```

**Sortie :**

```bash
2
4
6
8
10
```

Voici comment le programme a traité cette boucle :

| Itération | Variable | Condition : i <= 10 | Action & mise à jour de la variable |
| --- | --- | --- | --- |
| 1ère | i = 2 | vrai | 2 est imprimé. |
| 2ème | i = 4 | vrai | 4 est imprimé. |
| 3ème | i = 6 | vrai | 6 est imprimé. |
| 5ème | i = 8 | vrai | 8 est imprimé. |
| 6ème | i = 10 | vrai | 10 est imprimé. |
| 7ème | i = 12 | faux | La boucle est terminée. |

Supposons que nous voulons obtenir les nombres impairs. Tout ce que nous avons à faire est de changer `initialExpression` pour qu'il soit égal à `1` ou à n'importe quel nombre impair que nous souhaitons commencer comme vu ci-dessous

```javascript
for (let i = 1; i <= 10; i+=2) {
    console.log(i);  // impression de la valeur de i
}
```

### Comment Interrompre une Opération de Boucle For

Jusqu'à présent, nous avons vu comment créer une boucle for, mais il est également important de mentionner que nous pouvons sortir d'une boucle en utilisant `break`. L'instruction break est utilisée pour terminer la boucle immédiatement lorsqu'elle est rencontrée.

```javascript
for (let i = 1; i <= 10; i++) {    
    if (i == 5) {
        break;
    }
    console.log(i);
}
```

**Sortie :**

```bash
1
2
3
4
```

### Comment Afficher la Somme des Nombres Naturels

Faisons maintenant une boucle de 1 à 10 puis additionnons ces nombres ensemble au fur et à mesure que l'itération augmente :

```javascript
let sum = 0;

for (let i = 1; i <= 10; i++) {
    sum += i;  // Cela revient à : sum = sum + i
}

console.log('La somme de 1 à 10 est : ', sum); // "La somme de 1 à 10 est :  55"
```

**Note :** Nous ajoutons `console.log()` en dehors de la boucle, donc il ne nous donne que la sortie finale lorsque la boucle est terminée.

Nous pouvons également décider d'utiliser des variables pour définir le nombre maximum de notre condition de cette manière :

```javascript
let sum = 0;
let n = 10;

for (let i = 1; i <= n; i++) {
    sum += i;  // cela revient à : sum = sum + i
}

console.log('La somme de 1 à 10 est : ', sum); // "La somme de 1 à 10 est :  55"
```

### Comment Effectuer des Boucles Infini avec une Boucle For

Cela peut bloquer votre système, car il continue à s'exécuter jusqu'à ce que la mémoire soit pleine, puisque la condition est toujours évaluée à vrai.

```javascript
for(let i = 1; i > 0; i++) {
    // bloc de code
}
```

### Comment Parcourir un Tableau pour Vérifier les Nombres Pairs et Impairs

La plupart du temps, vous travaillerez avec des tableaux, alors voyons comment nous pouvons parcourir un tableau de nombres pour afficher tous les nombres pairs et impairs :

```javascript
var numbers = [1, 4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var evenNumbers = [];
var oddNumbers = [];

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 != 1) {
        evenNumbers.push(numbers[i]);
    } else {
        oddNumbers.push(numbers[i]);
    }
}

console.log("Les nombres pairs sont : " + evenNumbers); // "Les nombres pairs sont : 4,44,64,24,32,74,22"
console.log("Les nombres impairs sont : " + oddNumbers); // "Les nombres impairs sont : 1,55,55,19,17,23"
```

### Comment Parcourir un Tableau de Nombres pour Obtenir le Nombre Maximum et Minimum

Enfin, avant de conclure cet article, voyons comment obtenir le nombre maximum et minimum à partir d'un tableau avec une boucle for :

**Maximum :**

```javascript
var numbers = [1, 4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var max = 0;

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
        max = numbers[i];
    }
}

console.log(max); // 74
```

**Minimum :**

```javascript
var numbers = [4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var min = numbers[0];

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] < min) {
        min = numbers[i];
    }
}

console.log(min); // 4
```

## Conclusion

Dans cet article, nous avons appris ce qu'est une boucle JavaScript et nous avons examiné quelques exemples.

Il est important de comprendre qu'il existe de nombreux autres types de boucles, y compris la boucle while, qui est mieux utilisée lorsque vous ne connaissez pas le nombre d'itérations. Sinon, utilisez toujours la boucle for lorsque vous connaissez le nombre d'itérations.