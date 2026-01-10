---
title: Les opérateurs Spread et Rest en JavaScript – Expliqués avec des exemples de
  code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-08T23:27:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-spread-and-rest-operators
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-4-.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: Les opérateurs Spread et Rest en JavaScript – Expliqués avec des exemples
  de code
seo_desc: "In modern JavaScript, the spread and rest operators are indispensable tools\
  \ for simplifying array manipulation and function parameters. These operators provide\
  \ elegant solutions for tasks like array expansion and function arguments handling.\
  \ \nLet's d..."
---

En JavaScript moderne, les opérateurs spread et rest sont des outils indispensables pour simplifier la manipulation des tableaux et les paramètres de fonction. Ces opérateurs offrent des solutions élégantes pour des tâches comme l'expansion de tableaux et la gestion des arguments de fonction. 

Plongeons plus profondément dans leur fonctionnement afin que vous puissiez exploiter leur puissance.

Vous pouvez obtenir tout le code source depuis [ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/javascript-spread-and-rest-operator/index.js).

## Table des matières

* [L'opérateur Spread](#heading-loperateur-spread)
* [Avant l'opérateur Spread](#heading-avant-loperateur-spread)
* [Après l'opérateur Spread](#heading-apres-loperateur-spread)
* [Cas d'utilisation de l'opérateur Spread](#heading-cas-dutilisation-de-loperateur-spread)
* [L'opérateur Rest](#heading-loperateur-rest)
* [Avant l'opérateur Rest](#heading-avant-loperateur-rest)
* [Après l'opérateur Rest](#heading-apres-loperateur-rest)
* [Cas d'utilisation de l'opérateur Rest](#heading-cas-dutilisation-de-loperateur-rest)
* [Conclusion](#heading-conclusion)

## L'opérateur Spread

L'opérateur spread, représenté par trois points consécutifs (`...`), est principalement utilisé pour étendre les itérables comme les tableaux en éléments individuels. Cet opérateur nous permet de fusionner, copier ou passer efficacement des éléments de tableau à des fonctions sans avoir à itérer explicitement à travers eux.

Considérons le tableau suivant :

```javascript
const arr = [1, 2, 3];
console.log("Tableau original :", arr); // [1, 2, 3]
```

### Avant l'opérateur Spread

Traditionnellement, si nous voulions créer un nouveau tableau avec des éléments existants ajoutés à celui-ci, nous devions recourir à des approches fastidieuses comme celle-ci :

```javascript
const newArr = [5, 6, arr[0], arr[1], arr[2]];
console.log("Nouveau tableau (avant l'opérateur spread) :", newArr); // [5, 6, 1, 2, 3]
```

Cette méthode implique soit de coder en dur chaque élément, soit de parcourir manuellement le tableau, ce qui entraîne un code verbeux et sujet aux erreurs.

### Après l'opérateur Spread

Voici l'opérateur spread, offrant une alternative concise et intuitive :

```javascript
const newArr = [5, 6, ...arr];
console.log("Nouveau tableau (après l'opérateur spread) :", newArr); // [5, 6, 1, 2, 3]
```

Dans cet exemple, nous intégrons de manière transparente le contenu de `arr` dans `newArr` en utilisant l'opérateur spread. Aucun indexage ou boucle manuel n'est requis, ce qui rend le code plus lisible et maintenable.

### Cas d'utilisation de l'opérateur Spread

#### Combinaison de tableaux

L'opérateur spread offre une solution élégante pour combiner plusieurs tableaux en un seul. En étendant les éléments de chaque tableau dans un nouveau tableau, nous pouvons les concaténer sans effort.

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log("Tableau combiné :", combined); // [1, 2, 3, 4, 5, 6]
```

Cette approche élimine le besoin d'itération manuelle ou de méthodes de concaténation, ce qui donne un code concis et lisible.

#### Passage d'arguments à des fonctions

L'opérateur spread simplifie le processus de passage d'arguments de longueur variable à des fonctions. Au lieu de spécifier chaque argument individuellement, nous pouvons utiliser l'opérateur spread pour décompresser un tableau de valeurs en paramètres de fonction.

```javascript
function sum(a, b, c) {
    return a + b + c;
}

const nums = [1, 2, 3];
const result = sum(...nums);
console.log("Résultat de la somme :", result); // 6
```

Cette technique améliore la flexibilité des fonctions et réduit la redondance, surtout lorsqu'on traite des entrées dynamiques.

#### Copie de tableaux

L'opérateur spread offre une méthode concise pour copier des tableaux, garantissant que les modifications apportées au tableau copié n'affectent pas l'original. En étendant les éléments du tableau original dans un nouveau tableau, nous créons une copie distincte.

```javascript
const original = [1, 2, 3];
const copy = [...original];
console.log("Tableau copié :", copy); // [1, 2, 3]
```

Contrairement aux méthodes traditionnelles comme `slice()` ou `concat()`, l'opérateur spread fournit une approche plus intuitive et lisible pour la duplication de tableaux.

## L'opérateur Rest

Alors que l'opérateur spread étend les éléments, l'opérateur rest les condense en une seule entité au sein des paramètres de fonction ou de la destructuration de tableau. Il collecte les éléments restants dans une variable désignée, facilitant ainsi les définitions de fonction flexibles et la manipulation de tableaux.

### Avant l'opérateur Rest

Avant l'opérateur rest, extraire des éléments spécifiques d'un tableau tout en préservant le reste nécessitait une manipulation ou une boucle manuelle.

Considérons un scénario où nous voulons extraire le premier élément d'un tableau et collecter le reste dans un tableau séparé. Avant l'introduction de l'opérateur rest, la réalisation de cette tâche impliquait un code plus verbeux :

```javascript
const arr = [1, 2, 3, 4, 5];

const first = arr[0]; // Extraction du premier élément
const rest = arr.slice(1); // Collecte du reste des éléments

console.log("Premier élément :", first); // 1
console.log("Reste des éléments :", rest); // [2, 3, 4, 5]
```

Dans l'exemple ci-dessus, `first` capture le premier élément (`1`) en y accédant directement à l'index `0`, tandis que `rest` est obtenu en découpant le tableau à partir de l'index `1`. Cette approche manuelle est sujette aux erreurs et moins intuitive que l'utilisation de l'opérateur rest.

### Après l'opérateur Rest

Avec l'introduction de l'opérateur rest, l'extraction d'éléments spécifiques devient plus intuitive et concise.

```javascript
const [first, ...rest] = [1, 2, 3, 4, 5];
console.log("Premier élément :", first); // 1
console.log("Reste des éléments :", rest); // [2, 3, 4, 5]
```

Dans cet exemple, `first` capture le premier élément (`1`), tandis que `rest` encapsule les éléments restants (`[2, 3, 4, 5]`). L'opérateur rest nous permet de gérer des entrées de longueur variable avec facilité.

### Cas d'utilisation de l'opérateur Rest

#### Gestion des arguments de fonction de longueur variable

L'opérateur rest simplifie la gestion des arguments de longueur variable dans les fonctions. Il permet aux fonctions d'accepter un nombre indéfini d'arguments sans avoir à spécifier explicitement chacun d'eux.

```javascript
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log("Somme :", sum(1, 2, 3, 4, 5)); // Somme : 15
console.log("Somme :", sum(10, 20)); // Somme : 30
```

La syntaxe `...numbers` collecte tous les arguments passés dans un tableau nommé `numbers`, permettant des définitions de fonction flexibles.

#### Destructuration de tableau

L'opérateur rest est couramment utilisé dans la destructuration de tableau pour capturer les éléments restants dans une variable de tableau séparée.

```javascript
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log("Premier élément :", first); // Premier élément : 1
console.log("Deuxième élément :", second); // Deuxième élément : 2
console.log("Reste des éléments :", rest); // Reste des éléments : [3, 4, 5]
```

Cela permet un code plus concis et lisible lors de la manipulation de tableaux, surtout dans les scénarios où seuls les premiers éléments sont d'intérêt.

## Conclusion

C'est tout ! Ces opérateurs simplifient la manipulation des tableaux et la gestion des fonctions, rendant votre code plus efficace et lisible. 

Que ce soit pour des projets personnels ou des évaluations techniques, l'intégration des opérateurs spread et rest améliorera vos compétences en JavaScript et vos capacités de résolution de problèmes.

Si vous avez des commentaires, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/introvertedbot) ou [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/)