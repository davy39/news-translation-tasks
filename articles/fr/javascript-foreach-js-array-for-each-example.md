---
title: JavaScript forEach() – Exemple de boucle JS Array For Each
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-16T14:52:20.000Z'
originalURL: https://freecodecamp.org/news/javascript-foreach-js-array-for-each-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template.png
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: JavaScript forEach() – Exemple de boucle JS Array For Each
seo_desc: 'When working with arrays, there will be times when you need to loop or
  iterate through the array''s values in order to either output or manipulate them.

  These arrays can hold any datatype, including objects, numbers, strings, and many
  others.

  In this ...'
---

Lorsque vous travaillez avec des tableaux, il y aura des moments où vous devrez parcourir ou itérer à travers les valeurs du tableau afin de les afficher ou de les manipuler.

Ces tableaux peuvent contenir n'importe quel type de données, y compris des objets, des nombres, des chaînes de caractères et bien d'autres.

Dans cet article, nous allons voir comment utiliser la méthode de tableau JavaScript `forEach()` pour parcourir tous les types de tableaux, ainsi que ses différences avec la méthode de boucle for.

Il existe de nombreuses méthodes d'itération en JavaScript, y compris la méthode `forEach()`, et elles remplissent presque toutes la même fonction avec des différences mineures. Il vous appartient entièrement d'utiliser ou non une méthode de boucle spécifique, mais il est important que nous comprenions chacune d'elles et leur fonctionnement.

## JavaScript forEach()

La méthode de tableau `forEach()` parcourt n'importe quel tableau, exécutant une fonction fournie une fois pour chaque élément de tableau dans l'ordre croissant des indices. Cette fonction est appelée fonction de rappel.

> **Note :** Les tableaux sont des collections d'éléments qui peuvent être de n'importe quel type de données.

### Syntaxe et paramètres d'une boucle forEach()

Voici les manières standard d'écrire la boucle forEach :

```js
array.forEach(callbackFunction);
array.forEach(callbackFunction, thisValue);
```

La fonction de rappel peut accepter jusqu'à trois arguments différents, bien que tous ne soient pas obligatoires. Voici quelques exemples de boucles `forEach()` qui utilisent à la fois la fonction normale et la méthode ES6 pour déclarer la fonction de rappel :

```js
// En utilisant uniquement l'élément courant
array.forEach((currentElement) => { /* ... */ })
array.forEach(function(currentElement) { /* ... */ })

// En utilisant uniquement l'élément courant et l'index
array.forEach((currentElement, index) => { /* ... */ })
array.forEach(function(currentElement, index) { /* ... */ })

// En utilisant uniquement l'élément courant, l'index et le tableau
array.forEach((currentElement, index, array) => { /* ... */ })
array.forEach(function(currentElement, index, array){ /* ... */ })

// En utilisant tous les paramètres avec thisValue (valeur de this dans le rappel) 
array.forEach((currentElement, index, array) => { /* ... */ }, thisValue)
array.forEach(function(currentElement, index, array) { /* ... */ }, thisValue)
```

La syntaxe ci-dessus peut sembler confuse, mais c'est la syntaxe générale pour écrire une boucle forEach en fonction de la valeur que vous souhaitez utiliser. Passons en revue tous les paramètres que nous avons utilisés :

* `callbackFunction` : La fonction de rappel est une fonction qui est exécutée une seule fois pour chaque élément et peut accepter les arguments suivants pour être utilisés dans la fonction de rappel :

1. `currentElement` : L'élément courant, comme son nom l'indique, est l'élément du tableau qui est traité au moment où la boucle se produit. C'est le seul argument nécessaire.

2. `index` : L'index est un argument optionnel qui porte l'index de l'élément courant.

3. `array` : Le tableau est un argument optionnel qui retourne le tableau qui a été passé à la méthode `forEach()`.

* `thisValue` : Il s'agit d'un paramètre optionnel qui spécifie la valeur qui sera utilisée dans la fonction de rappel.

En résumé, la méthode d'itération de tableau `forEach()` accepte une fonction de rappel qui contient des arguments pouvant être utilisés dans la fonction de rappel pour chaque élément de tableau, tels que l'élément de tableau, l'index de l'élément et le tableau entier.

## Exemples de forEach() en JavaScript

Avant de regarder d'autres exemples possibles, examinons tous les arguments que nous avons passés dans la fonction de rappel et à quoi ils pourraient servir.

### Comment utiliser l'argument `currentElement`

Supposons que nous avons un tableau de détails d'employés qui inclut leurs noms, âge, montant du salaire et devise :

```js
const staffsDetails = [
  { name: "Jam Josh", age: 44, salary: 4000, currency: "USD" },
  { name: "Justina Kap", age: 34, salary: 3000, currency: "USD" },
  { name: "Chris Colt", age: 37, salary: 3700, currency: "USD" },
  { name: "Jane Doe", age: 24, salary: 4200, currency: "USD" }
];
```

Si nous voulons afficher tous les noms individuellement avec quelques mots autour, nous pouvons utiliser la méthode `forEach()` comme suit :

```js
staffsDetails.forEach((staffDetail) => {
  let sentence = `I am ${staffDetail.name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

Sortie :

```bash
"I am Jam Josh a staff of Royal Suites."
"I am Justina Kap a staff of Royal Suites."
"I am Chris Colt a staff of Royal Suites."
"I am Jane Doe a staff of Royal Suites."
```

**Note :** Nous pourrions également déstructurer la valeur `currentElement` si c'est un objet contenant des paires clé/valeur de cette manière :

```js
staffsDetails.forEach(({ name }, index) => {
  let sentence = `I am ${name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

### Comment utiliser l'argument `index`

Nous pourrions également obtenir l'index de chaque élément de tableau en utilisant simplement l'argument d'index intégré de cette manière :

```js
staffsDetails.forEach((staffDetail, index) => {
  let sentence = `index ${index} : I am ${staffDetail.name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

Sortie :

```bash
"index 0 : I am Jam Josh a staff of Royal Suites."
"index 1 : I am Justina Kap a staff of Royal Suites."
"index 2 : I am Chris Colt a staff of Royal Suites."
"index 3 : I am Jane Doe a staff of Royal Suites."
```

### Comment utiliser l'argument `array`

L'argument `array` est le troisième argument qui contient le tableau original qui est en cours d'itération. Par exemple, nous pourrions essayer d'afficher la valeur dans notre console de cette manière :

```js
staffsDetails.forEach((staffDetail, index, array) => {
  console.log(array);
});
```

Cela afficherait le tableau entier 4 fois puisque nous avons 4 éléments et que l'itération s'exécute 4 fois. Faisons-le pour un tableau avec quelques valeurs afin que je puisse ajouter la sortie ici :

```js
let scores = [12, 55, 70];

scores.forEach((score, index, array) => {
  console.log(array);
});
```

Sortie :

```bash
[12,55,70]
[12,55,70]
[12,55,70]
```

Jusqu'à présent, nous avons utilisé tous les arguments de la fonction de rappel. Regardons quelques autres exemples pour bien comprendre son fonctionnement avant de faire une rapide comparaison avec la méthode de boucle for.

### Comment additionner toutes les valeurs dans un tableau de nombres avec `forEach()`

Supposons que nous avons un tableau de `scores`. Nous pourrions utiliser la méthode de tableau `forEach()` pour parcourir et aider à additionner ces nombres :

```js
const scores = [12, 55, 70, 47];

let total = 0;
scores.forEach((score) => {
  total += score;
});

console.log(total);
```

Rappelons que plus tôt, nous utilisions un tableau de détails du personnel. Maintenant, essayons d'additionner tous les salaires des membres du personnel pour voir comment cela fonctionne avec des objets :

```bash
let totalSalary = 0;
staffsDetails.forEach(({salary}) => {
  totalSalary += salary;
});

console.log(totalSalary + " USD"); // "14900 USD"
```

**Note :** Nous avons déstructuré l'objet `currentElement`.

### Comment utiliser des conditionnelles dans une fonction de rappel `forEach()`

Lorsque nous parcourons des tableaux, nous pouvons vouloir vérifier des conditions spécifiques, comme cela est couramment fait avec la méthode de boucle for. Nous pouvons passer ces conditions dans notre fonction de rappel ou toute autre opération que nous voulons exécuter sur chaque élément de tableau.

Par exemple, si nous voulons seulement afficher les noms des personnes dont les salaires sont supérieurs ou égaux à `4000` à partir du tableau de détails du personnel que nous avons déclaré précédemment, nous pouvons faire ce qui suit :

```js
staffsDetails.forEach(({name, salary}) => {
  if(salary >= 4000){
    console.log(name);
  }
});
```

Sortie :

```bash
"Jam Josh"
"Jane Doe"
```

## Comparaison de forEach() avec une boucle for

La boucle for est très similaire à la méthode forEach, mais chacune possède des caractéristiques qui leur sont propres, telles que :

### Sortir et continuer dans une boucle

Lorsque nous parcourons un tableau, nous pouvons vouloir soit sortir de la boucle, soit la continuer lorsqu'une certaine condition est remplie (ce qui signifie que nous sautons). Cela est possible avec les instructions `break` et `continue`, mais cela ne fonctionne pas avec la méthode `forEach()`, comme le montre l'exemple ci-dessous :

```js
const scores = [12, 55, 70, 47];

scores.forEach((score) => {
  console.log(score);

  if (score === 70) 
    break;
});
```

Cela générera une erreur de syntaxe `Illegal break statement`. Cela s'applique également à l'instruction continue qui générera également une erreur `Illegal continue statement: no surrounding iteration statement`.

```js
const scores = [12, 55, 70, 47];

scores.forEach((score) => {
  if (score === 70) 
    continue;
  
  console.log(score);
});
```

Mais heureusement, cela fonctionne parfaitement avec la méthode de boucle for :

```js
const scores = [12, 55, 70, 47];

for (i = 0; i < scores.length; i++) {
  console.log(scores[i]);

  if (scores[i] === 70) 
    break;
}
```

Sortie :

```bash
12
55
70
```

Et de même avec l'instruction `continue` :

```js
const scores = [12, 55, 70, 47];

for (i = 0; i < scores.length; i++) {
  if (scores[i] === 70) 
    continue;
  
  console.log(scores[i]);
}
```

Sortie :

```bash
12
55
47
```

### Tableau avec des éléments manquants

Une autre comparaison importante à faire est dans une situation où le tableau que nous parcourons a certaines valeurs/éléments de tableau manquants comme on le voit ci-dessous :

```js
const studentsScores = [70, , 12, 55, , 70, 47];
```

Cela pourrait être dû à une erreur de développeur ou autre chose, mais ces deux méthodes adoptent deux approches différentes pour parcourir ces types de tableaux. La boucle for retourne undefined là où il y a des valeurs manquantes, alors que la méthode `forEach()` les ignore.

**Boucle for**

```js
const studentsScores = [70, , 12, 55, , 70, 47];

for (i = 0; i < studentsScores.length; i++) {
  console.log(studentsScores[i]);
}
```

Sortie :

```bash
70
undefined
12
55
undefined
70
47
```

**forEach()**

```js
const studentsScores = [70, , 12, 55, , 70, 47];

studentsScores.forEach((stundentScore) => {
  console.log(stundentScore);
});
```

Sortie :

```bash
70
12
55
70
47
```

**Note :** Async/Await ne fonctionne pas avec la méthode de tableau `forEach()` mais fonctionne avec la méthode de boucle for.

## Conclusion

Dans cet article, nous avons appris à utiliser la méthode de tableau `forEach()`, qui nous permet de parcourir un tableau de n'importe quel type d'élément. Elle nous permet également d'écrire un code plus propre et plus lisible que la boucle for.