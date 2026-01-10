---
title: Les nouveautés de JavaScript ES2019
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T17:20:45.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-javascript-es2019-8af4390d8494
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eK0RbuEJK9WzmA272g41Qg.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Les nouveautés de JavaScript ES2019
seo_desc: 'By Vali Shah

  Many of us know that there is a standard procedure for Javascript’s latest releases
  and a committee behind that. In this post, I will explain about who makes the final
  call on any new specification, what is the procedure for it, and what...'
---

Par Vali Shah

Beaucoup d'entre nous savent qu'il existe une procédure standard pour les dernières versions de JavaScript et un comité derrière cela. Dans cet article, je vais expliquer qui prend la décision finale sur toute nouvelle spécification, quelle est la procédure pour cela, et quelles sont les nouveautés de **ES2019.**

La spécification du langage qui guide JavaScript s'appelle **ECMAScript.** Il y a une équipe derrière cela appelée Technical Committee 39 **[TC39]** qui examine chaque spécification avant de l'adopter**.**

Chaque changement passe par un processus avec des étapes de maturité.

* **Étape 0:** Idées/Ébauche
* **Étape 1:** Propositions
* **Étape 2:** Brouillons
* **Étape 3:** Candidats
* **Étape 4:** Terminé/Approuvé

Une fonctionnalité qui atteint **l'Étape 4** fera très probablement partie de la spécification du langage.

Plongeons dans les choses qui ont été nouvellement ajoutées à la spécification sous ES2019.

#### Array.prototype.{flat,flatMap}

`Array.prototype.flat()` propose d'aplatir les tableaux de manière récursive jusqu'à la profondeur spécifiée et retourne un nouveau tableau.

**Syntaxe**: `Array.prototype.flat(depth)`   
**depth —** Valeur par défaut **1**, Utilisez `Infinity` pour aplatir tous les tableaux imbriqués.

```js
const numbers = [1, 2, [3, 4, [5, 6]]];
// Considère la profondeur par défaut de 1
numbers.flat(); 
> [1, 2, 3, 4, [5, 6]]
// Avec une profondeur de 2
numbers.flat(2); 
> [1, 2, 3, 4, 5, 6]
// Exécute deux opérations flat
numbers.flat().flat(); 
> [1, 2, 3, 4, 5, 6]
// Aplatit de manière récursive jusqu'à ce que le tableau ne contienne plus de tableaux imbriqués
numbers.flat(Infinity)
> [1, 2, 3, 4, 5, 6]
```

`Array.prototype.flatMap()` mappe chaque élément en utilisant une fonction de mappage et aplatit le résultat dans un nouveau tableau. C'est identique à l'opération map suivie d'un `flat` de profondeur **1.**

**Syntaxe:** `Array.prototype.flatMap(callback)`   
**callback:** `function` qui produit un élément du nouveau tableau.

```js
const numbers = [1, 2, 3];
numbers.map(x => [x * 2]);
> [[2], [4], [6]]
numbers.flatMap(x => [x * 2]);
> [2, 4, 6]
```

#### Object.fromEntries

`Object.fromEntries` effectue l'inverse de `Object.entries`. Il transforme une liste de paires clé-valeur en un objet.

**Syntaxe:** `Object.fromEntries(iterable)`   
**iterable:** Un itérable comme `Array` ou `Map` ou des objets implémentant le [protocole itérable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol)

```js
const records = [['name','Mathew'], ['age', 32]];
const obj = Object.fromEntries(records);
> { name: 'Mathew', age: 32}
Object.entries(obj);
> [['name','Mathew'], ['age', 32]];
```

#### String.prototype.{trimStart, trimEnd}

`trimStart()` supprime les espaces au début d'une chaîne et `trimEnd()` supprime les espaces à la fin d'une chaîne.

```js
const greeting = ` Hello Javascript! `;
greeting.length;
> 19
greeting = greeting.trimStart();
> 'Hello Javascript! '
greeting.length;
> 18
greeting = 'Hello World!   ';
greeting.length;
> 15
greeting = greeting.trimEnd();
> 'Hello World!'
greeting.length;
> 12
```

#### Optional Catch Binding

Avant la nouvelle spécification, il était nécessaire d'avoir une variable d'exception liée à une clause `catch`. ES2019 l'a rendu optionnel.

```js
// Avant
try {
   ...
} catch(error) {
   ...
}
// Après
try {
   ...
} catch {
   ...
}
```

Cette fonctionnalité est utile lorsque vous souhaitez ignorer complètement l'erreur. **La meilleure pratique est de considérer la gestion d'une erreur.**

Il existe des cas où vous connaissez l'erreur possible qui pourrait se déclencher lors des opérations. Vous pouvez ignorer le traitement du bloc catch.

#### JSON ⊂ ECMAScript

Les symboles de séparateur de ligne (U+2028) et de séparateur de paragraphe (U+2029) sont désormais autorisés dans les littéraux de chaîne. Auparavant, ceux-ci étaient traités comme des terminateurs de ligne et entraînaient des exceptions `SyntaxError`.

```js
// Produit une chaîne invalide avant ES2019
eval('"\u2028"');
// Valide dans ES2019
eval('"\u2028"');
```

#### Well-formed JSON.stringify

Au lieu de points de code de substitution non appariés résultant en des unités de code **UTF-16** uniques, ES10 les représente avec des séquences d'échappement JSON.

```js
JSON.stringify('\uD800');
> '""'
JSON.stringify('\uD800');
> '"\\ud800"'
```

#### Function.prototype.toString

`.toString()` retourne désormais des tranches exactes du texte du code source, y compris les espaces blancs et les commentaires.

```js
function /* un commentaire */ foo () {}
// Auparavant:
foo.toString();
> 'function foo() {}'
             ^ aucun commentaire
                ^ aucun espace
// Maintenant:
foo.toString();
> 'function /* commentaire */ foo () {}'
```

#### Symbol.prototype.description

Propriété en lecture seule qui retourne la description optionnelle d'un objet `Symbol`:

```js
Symbol('desc').toString();
> "Symbol(desc)"
Symbol('desc').description;  
> "desc"
Symbol('').description;      
> ""
Symbol().description;
> undefined
```

### Conclusion

**TC39** conserve toutes les spécifications à venir qui sont à l'étape >1 du processus [ici](https://github.com/tc39/proposals). En tant que [développeur](https://www.microverse.org/), il est important de suivre ce qui se passe. Il y a beaucoup plus de choses passionnantes à venir comme les méthodes et champs statiques et privés dans les classes, Legacy RegE**x, etc. Découvrez toutes les nouvelles choses qui sont en phase de proposition [ici](https://github.com/tc39/proposals).

`**code** = **ca**fé + **dé**veloppeur`

Voici quelques autres sujets intéressants:

* [**Un aperçu rapide des Symboles JavaScript**](https://medium.freecodecamp.org/how-did-i-miss-javascript-symbols-c1f1c0e1874a)
* [**Comment adopter une stratégie de branchement git**](https://medium.freecodecamp.org/adopt-a-git-branching-strategy-ac729ff4f838)
* [**Une introduction à Git Merge et Git Rebase: Ce qu'ils font et quand les utiliser**](https://medium.freecodecamp.org/an-introduction-to-git-merge-and-rebase-what-they-are-and-how-to-use-them-131b863785f)