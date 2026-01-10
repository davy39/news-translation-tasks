---
title: Tutoriel sur les Tableaux JavaScript – Méthodes de Tableaux en JS
subtitle: ''
author: Dario Di Cillo
co_authors: []
series: null
date: '2023-03-27T19:45:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-tutorial-array-methods-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/tom-wilson-Em2hPK55o8g-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tutoriel sur les Tableaux JavaScript – Méthodes de Tableaux en JS
seo_desc: 'Arrays are data structures that are extremely useful and versatile. They''re
  present in many programming languages, and they allow you to store multiple values
  in a single variable.

  In this tutorial, we will explore how arrays work in JavaScript, thei...'
---

Les tableaux (arrays) sont des structures de données extrêmement utiles et polyvalentes. Ils sont présents dans de nombreux langages de programmation et vous permettent de stocker plusieurs valeurs dans une seule variable.

Dans ce tutoriel, nous explorerons le fonctionnement des tableaux en JavaScript, leurs caractéristiques et comment les manipuler à l'aide des méthodes de tableaux les plus courantes.

## Table des matières

1. [Comment créer un tableau en JavaScript](#heading-comment-creer-un-tableau-en-javascript)
2. [Indexation des tableaux](#heading-indexation-des-tableaux)
3. [Comment utiliser la propriété `length`](#heading-comment-utiliser-la-propriete-length)
4. [Tableaux multidimensionnels](#heading-tableaux-multidimensionnels)
5. [Tableaux creux](#heading-tableaux-creux)
6. [Comment comparer des tableaux en JavaScript](#heading-comment-comparer-des-tableaux-en-javascript)
7. [L'opérateur Spread vs le paramètre Rest](#heading-loperateur-spread-vs-le-parametre-rest)
8. [Affectation par décomposition](#heading-affectation-par-decomposition)
9. [Comment ajouter et supprimer des éléments d'un tableau](#heading-comment-ajouter-et-supprimer-des-elements-dun-tableau)
10. [Comment combiner des tableaux](#heading-comment-combiner-des-tableaux)
11. [Comment convertir un tableau en chaîne de caractères](#heading-comment-convertir-un-tableau-en-chaine-de-caracteres)
12. [Comment comparer des tableaux](#heading-comment-comparer-des-tableaux)
13. [Comment copier un tableau](#heading-comment-copier-un-tableau)
14. [Comment rechercher dans un tableau](#heading-comment-rechercher-dans-un-tableau)
15. [Comment vérifier si les éléments d'un tableau remplissent une condition](#heading-comment-verifier-si-les-elements-dun-tableau-remplissent-une-condition)
16. [Comment trier un tableau](#heading-comment-trier-un-tableau)
17. [Comment effectuer une opération sur chaque élément d'un tableau](#heading-comment-effectuer-une-operation-sur-chaque-element-dun-tableau)
18. [Conclusion](#heading-conclusion)

# Une introduction aux tableaux en JS

En JavaScript, un tableau est un **objet** constitué d'un groupe d'éléments ayant un **ordre** spécifique. Les tableaux peuvent contenir des valeurs de types de données **mixtes** et leur **taille** n'est **pas fixe**.

## Comment créer un tableau en JavaScript

Vous pouvez créer un tableau en utilisant une **syntaxe littérale** – en spécifiant son contenu entre crochets, chaque élément étant séparé par une virgule.

Créons un tableau de chaînes de caractères, appelé `nobleGases` :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];

console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

Alternativement, vous pouvez utiliser le **constructeur** `Array()`, en passant les éléments à mettre dans le tableau comme arguments.

```js
let nobleGases = Array('He', 'Ne', 'Ar', 'Kr', 'Xn');

console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

## Indexation des tableaux

Chaque élément à l'intérieur d'un tableau est identifié par son **index** numérique ou sa position – commençant à zéro (pas 1) en JavaScript, comme dans de nombreux langages de programmation. Nous pouvons accéder aux éléments via la **notation entre crochets**, en spécifiant l'index à l'intérieur des crochets.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[0]; // 'He'
nobleGases[1]; // 'Ne'
nobleGases[2]; // 'Ar'
nobleGases[3]; // 'Kr'
nobleGases[4]; // 'Xn'
nobleGases[5]; // undefined
```

Lorsque vous essayez d'accéder à une valeur en dehors de la plage d'index, vous obtenez `undefined` comme valeur de retour. Comme vous pouvez le voir, dans l'exemple ci-dessus, aucune valeur n'est stockée à l'index 5.

Les tableaux JavaScript ne sont **pas de taille fixe**. Ils peuvent s'agrandir et se réduire en fonction de leur contenu. Vous pouvez facilement le vérifier en essayant d'assigner une valeur à `nobleGases[5]` :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[5] = 'Rn';
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Maintenant, `nobleGases` contient une valeur de plus, comme vous pouvez le voir dans la sortie.

## Comment utiliser la propriété `length`

Vous pouvez vérifier le nombre d'éléments contenus dans un tableau en utilisant la propriété `length`, via la **notation par points** :

```js
nobleGases.length; // 6
```

La longueur du tableau sera la valeur de l'index du dernier élément du tableau + 1, puisque l'indexation commence à zéro.

## Tableaux multidimensionnels

Les tableaux JavaScript peuvent contenir n'importe quelle valeur autorisée, y compris d'autres tableaux. Un tableau à l'intérieur d'un autre tableau est appelé un tableau **imbriqué**. Cette situation crée la possibilité d'avoir de nombreux objets de tableau imbriqués à différentes profondeurs. Voici un exemple de tableau à trois dimensions :

```js
let elements = [[['H', 'Li', 'Na'], ['Be', 'Mg']], [['B', 'Al'], ['C', 'Si']]];
```

Vous pouvez accéder aux différents éléments en répétant la syntaxe des crochets avec les index correspondant aux éléments qui vous intéressent, pour aller de plus en plus profondément. Comme ceci :

```js
console.log(elements[0]); // [['H', 'Li', 'Na'], ['Be', 'Mg']]

console.log(elements[0][0]); // ['H', 'Li', 'Na']

console.log(elements[0][0][0]); // 'H'
```

## Tableaux creux

Les tableaux creux (sparse arrays) sont des tableaux contenant des **emplacements** **vides**. Par exemple, si vous tapez deux virgules consécutives par erreur lors de la création d'un tableau, vous obtiendrez un tableau creux :

```js
let firstGroup = ['H', 'Li', 'Na',, 'K', 'Rb', 'Cs'];
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs']

```

Comme vous pouvez le voir, entre `'Na'` et `'K'`, il y a une valeur `empty`. Cela peut être affiché de différentes manières, selon l'environnement de codage. Mais ce n'est pas la même chose qu'avoir une valeur `undefined`.

Les tableaux creux peuvent également être créés en modifiant directement la propriété `length` ou par affectation à un index supérieur à la longueur :

```js
// Augmenter la propriété length
firstGroup.length = 11;
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs', empty × 4]

// Assigner un élément à un index supérieur à la longueur
firstGroup[15] = 'Fr';
console.log(firstGroup);
// ['H', 'Li', 'Na', empty, 'K', 'Rb', 'Cs', empty × 8, 'Fr']
```

Selon l'opération effectuée sur un tableau creux, les emplacements vides [peuvent agir comme `undefined` ou être ignorés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots).

## Comment comparer des tableaux en JavaScript

Les tableaux JavaScript sont des objets, et si vous essayez de comparer deux objets, la comparaison s'effectue en considérant leurs **références** – et non leurs **valeurs** réelles.

Cela signifie que vous pourriez essayer de comparer deux tableaux contenant les mêmes éléments – et qui sont donc apparemment égaux – comme ceci :

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = ['flour', 'water', 'yeast', 'salt'];

dough1 === dough2; // false
```

Mais, selon JavaScript, ils ne sont pas égaux. Et même la comparaison de deux tableaux vides, quelle que soit la manière dont ils sont créés, renverrait le même résultat :

```js
[] === []; // false
Array() === Array(); // false
```

Comme je l'ai mentionné, cela se produit parce que les **références d'objets sont comparées**, et non leur contenu réel. Et chaque fois que vous créez un nouvel objet tableau, il aura une référence différente en mémoire.

La seule façon pour que cette comparaison soit évaluée à `true` est de faire pointer les deux tableaux vers la même référence. Par exemple :

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = dough1;

dough1 === dough2; // true
```

Dans le code ci-dessus, `let dough2 = dough1` ne signifie pas que vous faites une copie de `dough1`. Cela signifie que la variable `dough2` pointera exactement vers la même référence que `dough1`. Ils sont le même objet tableau.

Cela dit, si vous voulez comparer deux tableaux, vous devrez adopter une stratégie différente. Une bonne approche consisterait à parcourir le tableau et à comparer chaque élément un par un. Vous pouvez le faire avec une boucle `for` et quelques instructions conditionnelles :

```js
const compareArr = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    } 
    for (let i = 0; i < arr1.length; i++) {
    	if (arr1[i] !== arr2[i]) {
            return false
        }
    }
    return true
};
```

Dans l'extrait de code ci-dessus, vous pouvez voir une fonction pour vérifier si les deux tableaux sont égaux.

* La première étape consiste à vérifier si les tableaux ont la même longueur. Si la longueur est différente, ils ne peuvent certainement pas être égaux :

```js
if (arr1.length !== arr2.length) {
        return false
    }
```

* Ensuite, une boucle `for` parcourt le tableau et une instruction `if` vérifie si chaque élément du premier tableau est différent de l'élément à l'index correspondant dans le second tableau :

```js
for (let i = 0; i < arr1.length; i++) {
    	if (arr1[i] !== arr2[i]) {
            return false
        }
    }
```

* Si aucune différence n'est détectée, les tableaux sont égaux et la fonction retourne `true`.

Voici le résultat de la comparaison des deux tableaux du début de cette section avec notre fonction :

```js
let dough1 = ['flour', 'water', 'yeast', 'salt'];
let dough2 = ['flour', 'water', 'yeast', 'salt'];

compareArr(dough1, dough2); // true
```

Notez que nous ne pouvons appliquer cette fonction qu'à un tableau contenant des valeurs **primitives**. Si un tableau contient des objets, vous devriez chercher la solution qui convient à votre problème spécifique et approfondir la vérification.

Par exemple, si vous savez que vos tableaux sont imbriqués, comme ceux-ci :

```js
let metal1 = [['Li', 'Na', 'K'], ['Be', 'Mg', 'Ca']];
let metal2 = [['Li', 'Na', 'K'], ['Be', 'Mg', 'Ca']];
```

Une solution possible serait la suivante :

```js
const compareNested = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    } for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            if (arr1[i][j] !== arr2[i][j]) {
                return false
            }
        }
    }
    return true
};

compareNested(metal1, metal2); // true
```

Par rapport à la fonction précédente, nous avons ajouté une boucle `for` supplémentaire. C'est suffisant pour comparer les éléments à l'intérieur des tableaux internes.

Si vous avez besoin de comparer deux tableaux d'objets :

```js
let albums1 = [
    {artist: 'Frank Zappa', title: 'Over-Nite Sensation', year: 1973},
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: 1975}
];
let albums2 = [
    {artist: 'Frank Zappa', title: 'Over-Nite Sensation', year: 1973},
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: undefined},
];
```

Vous pouvez faire quelque chose comme ceci :

```js
const compareArrObj = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false
    }
    for (let i = 0; i < arr1.length; i++) {
        if (Object.keys(arr1[i]).length !== Object.keys(arr2[i]).length) {
            return false
        }
        for (let prop in arr1[i]) {
            if (arr1[i][prop] !== arr2[i][prop]) {
                return false
            }
        }
    }
    return true
};
```

* Encore une fois, la première étape consiste à vérifier si les tableaux ont la même longueur. Si la longueur est différente, ils ne peuvent pas être égaux.
* Une boucle `for` parcourt le tableau et une instruction `if` vérifie si chaque objet du premier tableau a une longueur différente de l'objet à l'index correspondant dans le second tableau :

```js
for (let i = 0; i < arr1.length; i++) {
        if (Object.keys(arr1[i]).length !== Object.keys(arr2[i]).length) {
            return false
        }
//...
}
```

* Ensuite, une boucle `for`...`in` parcourt les propriétés du i-ème objet du premier tableau. Et une instruction `if` vérifie si la valeur de chaque clé est différente de la valeur de la clé correspondante dans le i-ème objet de l'autre tableau :

```js
for (let prop in arr1[i]) {
            if (arr1[i][prop] !== arr2[i][prop]) {
                return false
            }
        }
```

À la fin, le résultat serait :

```js
compareArrObj(albums1, albums2); // false
```

Parce que la valeur de `year` dans le troisième objet de `albums2` est différente. Si nous la changeons, le résultat sera `true` :

```js
albums2[2]['year'] = 1975;

compareArrObj(albums1, albums2); // true
```

## L'opérateur Spread vs le paramètre Rest

L'opérateur spread et le paramètre rest ont une syntaxe similaire (`...`) mais ils effectuent des opérations fondamentalement différentes.

L'opérateur **spread** vous permet d'**étendre** un tableau – plus généralement un objet itérable – en ses éléments. Le paramètre **rest** vous permet de collecter un nombre indéfini d'arguments dans **un seul tableau**.

### Comment utiliser l'opérateur Spread

Plus loin dans cet article, nous verrons quelques méthodes pour copier un tableau ou fusionner différents tableaux. Mais utiliser l'opérateur spread est une alternative valable pour faire les mêmes choses.

Dans l'exemple ci-dessous, les tableaux `alkali` et `alkEarth` sont fusionnés en un seul tableau à l'aide de la syntaxe spread. Pour ce faire, vous devez lister les tableaux que vous souhaitez fusionner entre crochets, en faisant précéder chacun d'eux de trois points.

```js
let alkali = ['Li', 'Na', 'K'];
let alkEarth = ['Be', 'Mg', 'Ca'];

// Fusionner deux tableaux avec l'opérateur spread
let metals = [...alkali, ...alkEarth];
console.log(metals); // ['Li', 'Na', 'K', 'Be', 'Mg', 'Ca']
```

De plus, vous pouvez utiliser la même syntaxe avec un seul tableau, pour créer une copie d'un tableau :

```js
// Copier un tableau avec l'opérateur spread
let metalsCopy = [...metals];
console.log(metalsCopy); // ['Li', 'Na', 'K', 'Be', 'Mg', 'Ca']

```

### Comment utiliser le paramètre Rest

Le paramètre rest vous permet de collecter un nombre indéfini d'éléments dans un seul tableau. Le paramètre rest doit être le dernier dans une séquence de paramètres de fonction. De plus, une fonction ne peut avoir qu'un seul paramètre rest.

```js
function f1(first, second, third, ...others) {
	console.log(first);
    console.log(second);
    console.log(third);
    console.log(others);
};

f1('He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'); 
// He
// Ne
// Ar
// ['Kr', 'Xn', 'Rn']
```

Dans l'exemple ci-dessus, la fonction `f1` est appelée avec six arguments de type chaîne de caractères. Et les arguments après le troisième sont rassemblés à l'intérieur du tableau `others` en utilisant la syntaxe rest.

En général, les arguments passés à une fonction sont collectés dans l'objet `arguments`, qui est un objet semblable à un tableau (array-like) et ne prend pas en charge les méthodes itératives que nous verrons dans la section suivante de cet article.

Ainsi, le paramètre rest offre un moyen d'accéder facilement aux arguments passés à une fonction sous forme de tableau, au lieu d'utiliser l'objet `arguments` :

```js
function f2(...args) {
	console.log(args);
    // vous pouvez utiliser une méthode itérative sur le tableau args
};

f2('He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn');
// ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Dans l'exemple ci-dessus, nous avons simplement affiché le tableau `args`, mais l'avantage ici est de pouvoir implémenter une méthode itérative sur celui-ci.

## Affectation par décomposition

La syntaxe de décomposition (destructuring) offre un moyen simple d'assigner des valeurs en les déballant d'un objet tableau. Voyons un exemple pratique :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
let [firstRow, secondRow,,FourthRow] = nobleGases;
console.log(firstRow); // 'He'
console.log(secondRow); // 'Ne'
console.log(FourthRow); // 'Kr'
// 'Ar' est ignoré à cause de la virgule supplémentaire
```

Les variables situées à gauche de l'opérateur d'affectation reçoivent la valeur des éléments correspondants du tableau situé à droite. Vous pouvez ignorer des éléments du tableau et passer aux suivants en tapant plus d'une virgule entre chaque nom de variable.

# Méthodes de tableaux courantes en JS

En JavaScript, les tableaux sont des **objets** et possèdent des **propriétés** et des **méthodes**.

Dans cette section, nous aborderons certaines des méthodes de tableaux les plus courantes que vous devez connaître pour travailler efficacement avec les tableaux en JavaScript.

## Comment ajouter et supprimer des éléments d'un tableau

Dans cette section, vous verrez les moyens les plus courants d'ajouter et de supprimer des éléments d'un tableau en JavaScript. Toutes les méthodes suivantes **mutent** (modifient) le tableau original.

### Comment utiliser la méthode `push()`

Reprenons l'exemple de la section sur l'indexation :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases[5] = 'Rn';
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Nous avons assigné `Rn` à l'index `5` du tableau `nobleGases` en utilisant la notation entre crochets. Au final, nous avons simplement ajouté `Rn` à la fin de ce tableau.

Vous pouvez obtenir le même résultat en utilisant la méthode `push()`, et vous n'avez pas besoin de connaître la longueur du tableau pour cela. Vous utilisez la notation par points pour appeler `push()`, en indiquant le ou les éléments à ajouter entre parenthèses. Comme ceci :

```js
// Syntaxe
array.push(element1, /* … ,*/ elementN)
```

L'élément spécifié sera ajouté à la **fin** du tableau, retournant la nouvelle longueur du tableau. Par exemple :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];
nobleGases.push('Rn'); // 6
// push() retourne la longueur du tableau modifié
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Vous pouvez ajouter plusieurs éléments avec `push()`, en indiquant leurs valeurs séparées par une virgule :

```js
let halogens = ['F', 'Cl'];
console.log(halogens); // ['F', 'Cl']

halogens.push('Br', 'I', 'At'); // 5
// push() retourne la longueur du tableau modifié
console.log(halogens); // ['F', 'Cl', 'Br', 'I', 'At']
```

### Comment utiliser la méthode `unshift()`

Similaire à `push()`, la méthode `unshift()` ajoute un ou plusieurs éléments au **début** d'un tableau et retourne la longueur du tableau modifié.

```js
// Syntaxe
array.unshift(element1, /* … ,*/ elementN)
```

Par exemple :

```js
let halogens = ['F', 'Cl'];
console.log(halogens); // ['F', 'Cl']

halogens.unshift('Br', 'I', 'At'); // 5
// unshift() retourne la longueur du tableau modifié
console.log(halogens); // ['Br', 'I', 'At', 'F', 'Cl']
```

### Comment utiliser la méthode `pop()`

Si vous avez besoin de supprimer le **dernier** élément d'un tableau, vous pouvez utiliser la méthode `pop()`.

```js
// Syntaxe
array.pop()
```

Elle supprime uniquement le dernier élément et le retourne.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.pop(); // 'Rn'
// pop() retourne l'élément supprimé
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn']
```

### Comment utiliser la méthode `shift()`

De même, la méthode `shift()` supprime le **premier** élément d'un tableau et le retourne.

```js
// Syntaxe
array.shift()
```

Voici un exemple :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.shift(); // 'He'
// shift() retourne l'élément supprimé
console.log(nobleGases); // ['Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

### Comment utiliser la méthode `splice()`

Si vous devez supprimer un ou plusieurs éléments d'une position spécifique d'un tableau, vous pouvez utiliser la méthode `splice()`.

```js
// Syntaxe
array.splice(start, count)
```

Le premier paramètre de `splice()` est l'**index de départ**, tandis que le second est le **nombre d'éléments à supprimer** du tableau.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']

nobleGases.splice(1, 3); // ['Ne', 'Ar', 'Kr']
// splice() retourne un tableau contenant les éléments supprimés
console.log(nobleGases); // ['He', 'Xn', 'Rn']
```

Ainsi, `.splice(1, 3)` signifie "commencer à l'index = `1` et supprimer `3` éléments". La méthode retourne un tableau contenant les éléments supprimés du tableau original.

Si le second argument n'est pas fourni, les éléments sont supprimés jusqu'à la fin.

En utilisant `splice()`, vous pouvez également ajouter des éléments.

```js
// Syntaxe
array.splice(start, count, addition1, /* … ,*/ additionN)
```

Si vous spécifiez des arguments supplémentaires – après l'index de départ et le nombre d'éléments à supprimer – ceux-ci seront insérés à la position indiquée. Par exemple :

```js
let nobleGases = ['He', 'Ne', 'Cl', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Cl', 'Rn']

nobleGases.splice(2, 1, 'Ar', 'Kr', 'Xn'); // ['Cl']
// splice() retourne un tableau contenant les éléments supprimés
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

Ici, `.splice(2, 1, 'Ar', 'Kr', 'Xn')` signifie "commencer à l'index = `2`, supprimer `1` élément et ajouter les chaînes `'Ar'`, `'Kr'`, `'Xn'`". Le tableau retourné par la méthode contient l'élément `'Cl'`, qui était à l'index = `2` dans le tableau d'origine.

Si vous n'avez pas besoin de supprimer d'éléments du tableau, vous pouvez simplement utiliser zéro comme second argument. Les éléments seront ajoutés en commençant à l'index spécifié, sans supprimer aucun élément :

```js
let nobleGases = ['He', 'Ne', 'Rn'];
console.log(nobleGases); // ['He', 'Ne', 'Rn']

nobleGases.splice(2, 0, 'Ar', 'Kr', 'Xn'); // []
// splice() retourne un tableau contenant les éléments supprimés
console.log(nobleGases); // ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn']
```

## Comment combiner des tableaux

### Comment utiliser la méthode `concat()`

Si vous avez besoin de combiner deux ou plusieurs tableaux – c'est-à-dire créer un seul tableau contenant chaque élément des tableaux que vous souhaitez fusionner – vous pouvez utiliser la méthode `concat()`. Cette méthode ne modifie pas les tableaux originaux et retourne un nouveau tableau.

Vous devez appeler `.concat()` sur le tableau qui doit venir en premier, en passant comme arguments les tableaux avec lesquels vous souhaitez le fusionner. L'ordre sera reflété dans le tableau résultant.

```js
// Syntaxe
array1.concat(array2, /* … ,*/ arrayN)
```

Voici un exemple de combinaison de deux et trois tableaux :

```js
let alkali = ['Li', 'Na', 'K'];
let moreAlkali = ['Rb', 'Cs', 'Fr'];
let alkEarth = ['Be', 'Mg', 'Ca'];

alkali.concat(moreAlkali);
// ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']

alkali.concat(moreAlkali, alkEarth);
// ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca']
```

### Comment utiliser la méthode `push()` et l'opérateur Spread

Si cela ne vous dérange pas de modifier le tableau d'origine, vous pouvez combiner un appel à `.push()` avec la syntaxe spread (`...`) pour ajouter tous les éléments d'un ou plusieurs tableaux au tableau d'origine. Par exemple :

```js
let alkali = ['Li', 'Na', 'K'];
let moreAlkali = ['Rb', 'Cs', 'Fr'];
let alkEarth = ['Be', 'Mg', 'Ca'];

alkali.push(...moreAlkali); // 6
console.log(alkali); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
```

Vous ne pouvez pas utiliser `push()` sans la syntaxe spread dans ses arguments, à moins que vous ne vouliez imbriquer l'intégralité du tableau `moreAlkali` comme dernier élément de `alkali`. Dans ce cas, le résultat serait `['Li', 'Na', 'K', ['Rb', 'Cs', 'Fr']]` – un tableau composé de 4 éléments, le dernier étant lui-même un tableau.

Notez que, comme nous l'avons vu précédemment, l'opérateur spread seul vous permet de fusionner deux ou plusieurs tableaux sans provoquer de mutation. Dans la continuité de l'exemple précédent :

```js
let metals = [...alkali, ...alkEarth];
console.log(metals); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca']
console.log(alkali); // ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
```

## Comment convertir un tableau en chaîne de caractères

Si vous devez convertir un tableau en chaîne de caractères, vous avez plusieurs options. Nous allons maintenant en voir quelques-unes. Notez que les méthodes suivantes ne mutent pas le tableau d'origine.

### Comment utiliser les méthodes `toString()` et `join()`

Ces méthodes vous permettent de convertir des tableaux en chaînes de caractères.

La méthode `toString()` est appelée sans paramètre et retourne une chaîne représentant le contenu du tableau.

```js
// Syntaxe
array.toString()
```

La méthode `join()` prend un séparateur comme argument, qui est utilisé pour séparer les éléments du tableau afin de former la chaîne.

```js
// Syntaxe
array.join(separator)
```

Voici un exemple :

```js
let animals = ['pig', 'dog', 'sheep'];

animals.toString(); // 'pig,dog,sheep'

animals.join(', '); // 'pig, dog, sheep'

animals.join(' '); // 'pig dog sheep'

animals.join(' * '); // 'pig * dog * sheep'
```

Ces deux méthodes présentent certaines limites. Si nous considérons le tableau de l'exemple suivant, nous pouvons observer quelques points intéressants :

```js
let arr = [1, 'two', null, undefined, true, {}];

arr.toString(); // '1,two,,,true,[object Object]'

arr.join(); // '1,two,,,true,[object Object]'
```

Premièrement, `null` et `undefined` donnent le même résultat sous forme de chaîne (une sous-chaîne vide).

Deuxièmement, la représentation sous forme de chaîne d'un objet est `[object Object]`. Par conséquent, si vous essayez de convertir un tableau contenant des objets en chaîne, vous devriez utiliser une autre méthode. Sinon, vous ne pourrez pas voir correctement le contenu des objets.

### Comment utiliser la méthode `JSON.stringify()`

Si vous souhaitez convertir un tableau contenant des objets en chaîne de caractères, la méthode `JSON.stringify()` est ce qu'il vous faut. Là où les méthodes précédentes échouent, `JSON.stringify()` vous permet de gérer correctement les objets.

```js
// Syntaxe
JSON.stringify(array)
```

Cette méthode prend une valeur JavaScript comme argument – dans ce cas, le tableau `albums` – et la convertit en une chaîne JSON.

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe', year: 1974},
    {artist: 'Frank Zappa', title: 'One Size Fits All', year: 1975}
];

JSON.stringify(albums);
//'[{"artist":"Frank Zappa","title":"Apostrophe","year":1974},{"artist":"Frank Zappa","title":"One Size Fits All","year":1975}]'
```

Comme vous pouvez le voir, les crochets sont conservés, il est donc souvent préférable d'utiliser cette méthode pour créer une chaîne à partir d'un tableau.

## Comment comparer des tableaux

Puisque les tableaux sont des objets, leur **comparaison est basée sur les références** et non sur les valeurs réelles.

Précédemment, nous avons vu quelques façons de comparer des tableaux en bouclant sur un tableau et en comparant chaque élément.

Une autre approche pour comparer les tableaux consiste à les convertir en chaînes de caractères avec l'une des méthodes précédentes, puis à comparer les représentations sous forme de chaînes des tableaux originaux.

C'est assez rapide et facile, mais cela peut parfois entraîner un comportement inattendu. Par exemple, lorsque des valeurs `null` et `undefined` sont comparées.

```js
let a = [1, null, 3];
let b = [1, undefined, 3];

a[1] === b[1]; // false

JSON.stringify(a) === JSON.stringify(b); // true

```

Vous pourriez penser que la comparaison entre la représentation sous forme de chaîne de `a` et `b` retournerait `false`, puisque `null` et `undefined` ne sont pas égaux. Mais en pratique, ils sont tous deux transformés en `null` par stringify.

Compte tenu de cet aspect, il est préférable d'utiliser une technique itérative.

### Comment utiliser la méthode `every()`

`every()` est une méthode itérative qui vérifie si tous les éléments du tableau passent une condition implémentée par une fonction de rappel (callback) et elle retourne `true` ou `false`.

```js
// Syntaxe
array.every((element, index, array) => {})
```

Parmi ses nombreuses utilisations, vous pouvez construire une fonction simple pour comparer des tableaux contenant des valeurs primitives avec `every()`, comme ceci :

```js
const compareEvery = (arr1, arr2) => {
    return arr1.length === arr2.length &&
    arr1.every((elem, index) => elem === arr2[index])
}
```

* Tout d'abord, les longueurs sont comparées. Si elles ne sont pas égales, les tableaux ne sont pas égaux non plus.
* Ensuite, `every()` est appelée sur le premier tableau. Le callback vérifie si chaque élément de `arr1` est égal à l'élément à l'index correspondant dans `arr2`.

```js
arr1.every((elem, index) => elem === arr2[index])
```

L'opérateur AND garantit que `true` n'est retourné que lorsque les deux conditions sont vraies.

Voici la fonction appliquée aux tableaux de tout à l'heure :

```js
let a = [1, null, 3];
let b = [1, undefined, 3];

compareEvery(a,b); // false

```

## Comment copier un tableau

Toutes les opérations courantes pour copier un tableau en JavaScript génèrent une **[copie superficielle (shallow copy)](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)** – au lieu d'une copie profonde (deep copy) – du tableau d'origine. Cela signifie qu'en modifiant la copie, vous pouvez également modifier le tableau d'origine. Nous verrons pourquoi cela se produit dans un instant.

### Comment utiliser la méthode `slice()`

La méthode `slice()` vous permet de copier un tableau entier – ou seulement une partie de celui-ci – sans le modifier.

```js
// Syntaxe
array.slice(start, end)
```

Comme paramètres, elle prend l'**index de départ** et l'**index final** (non inclus) à copier. Lorsqu'elle est appelée sans arguments, `slice()` crée un doublon de l'ensemble du tableau. Par exemple :

```js
let dough = ['flour', 'water', 'yeast', 'salt'];

let doughCopy = dough.slice();
console.log(doughCopy); // ['flour', 'water', 'yeast', 'salt']
```

Si vous essayez de modifier `doughCopy` d'une manière ou d'une autre, par exemple en assignant une nouvelle valeur à `doughCopy[1]`, vous verriez qu'aucun changement n'est reflété dans le tableau d'origine :

```js
doughCopy[1] = 'wine';
console.log(doughCopy); // ['flour', 'wine', 'yeast', 'salt']

console.log(dough); // ['flour', 'water', 'yeast', 'salt']
```

Cela se produit parce que le tableau est rempli de valeurs primitives. Cependant, l'histoire est bien différente si vous manipulez un tableau contenant des valeurs non primitives.

Considérons le tableau suivant, avec deux objets :

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];
```

Vous copiez le tableau en utilisant la méthode `slice()`, comme ceci :

```js
let albumsCopy = albums.slice();
```

Maintenant, `albumsCopy` représente une copie superficielle de `albums` et les éléments à l'intérieur de chaque tableau pointent vers les mêmes objets. En d'autres termes, `albums[0] === albumsCopy[0]` et `albums[1] === albumsCopy[1]` retournent tous deux `true` – rappelez-vous que cette comparaison implique les références d'objets – car il s'agit exactement des mêmes objets.

Si vous modifiez l'un d'eux en changeant la valeur d'une propriété, la modification affecte également l'autre tableau.

```js
albumsCopy[1]['title'] = 'Absolutely Free';
console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];

console.log(albums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];
```

Notez que si vous réassignez un élément à un objet différent – c'est-à-dire sans modifier l'un des objets existants – la modification n'affecte pas l'autre tableau :

```js
albumsCopy[1] = {artist: 'Captain Beefheart', title: 'Safe as Milk'};

console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Captain Beefheart', title: 'Safe as Milk'}
// ];

console.log(albums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'Absolutely Free'}
// ];
```

### Comment utiliser la méthode `map()`

La méthode `map()` génère un nouveau tableau contenant le résultat de l'appel d'une fonction de rappel sur chaque élément d'un tableau.

```js
// Syntaxe
array.map((element, index, array) => {})
```

La fonction prend en paramètres l'élément actuel, son index et le tableau sur lequel la méthode est appelée.

Vous pouvez utiliser `map()` pour copier un tableau en spécifiant une fonction qui retourne chaque élément du tableau :

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];

let mapAlbums = albums.map(element => element);
console.log(mapAlbums);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'One Size Fits All'}
// ];
```

### Comment créer une copie profonde

Si vous souhaitez créer un clone profond (deep copy) d'un tableau, vous pouvez convertir le tableau en une chaîne de caractères avec `JSON.stringify()` et passer sa valeur de retour à la méthode `JSON.parse()`.

```js
let albums = [
    {artist: 'Frank Zappa', title: 'Apostrophe'},
    {artist: 'Frank Zappa', title: 'One Size Fits All'}
];

let albumsCopy = JSON.parse(JSON.stringify(albums));
console.log(albumsCopy);
// [
//  {artist: 'Frank Zappa', title: 'Apostrophe'},
//  {artist: 'Frank Zappa', title: 'One Size Fits All'}
// ];
```

De cette façon, la copie sera complètement indépendante du tableau d'origine et vous ne risquerez pas de modification involontaire.

## Comment rechercher dans un tableau

Selon ce que vous recherchez, il existe plusieurs façons de fouiller dans un tableau. Explorons quelques méthodes pour effectuer une recherche par index et par valeur.

### Comment utiliser la méthode `includes()`

Si vous avez besoin de savoir si une valeur est incluse dans un tableau, vous pouvez appeler la méthode `includes()` sur celui-ci, en passant la valeur qui vous intéresse comme argument.

```js
// Syntaxe
array.includes(value, startingIndex)
```

Cette méthode retourne `true` si la valeur est trouvée. Sinon, `false`.

```js
let dMinor = ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'];

dMinor.includes('E'); // true
dMinor.includes('E', 2); // false
```

Elle accepte également un second paramètre, représentant l'index où commencer la recherche – la valeur par défaut est zéro.

### Comment utiliser la méthode `indexOf()`

Si vous avez besoin de connaître l'index auquel une valeur spécifique peut être trouvée dans un tableau, vous devriez utiliser la méthode `indexOf()`.

```js
// Syntaxe
array.indexOf(value, startingIndex)
```

Elle retourne uniquement le **premier index** auquel la valeur spécifiée est trouvée ; sinon, elle retourne -1. Le second paramètre est l'index à partir duquel commencer la recherche de la valeur – la valeur par défaut est zéro.

```js
let dMinor = ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'];

dMinor.indexOf('E'); // 1
dMinor.indexOf('E', 2); // -1
```

### Comment utiliser les méthodes `find()` et `findLast()`

`find()` et `findLast()` vous permettent de rechercher respectivement le **premier** et le **dernier** élément qui satisfait une certaine condition dans un tableau.

```js
// Syntaxe
array.find((element, index, array) => {})

array.findLast((element, index, array) => {})
```

Elles acceptent toutes deux une fonction de rappel, dont les paramètres sont l'élément actuel, son index et le tableau sur lequel la méthode est appelée.

`find()` et `findLast()` retournent le premier/dernier élément qui satisfait la fonction, ou `undefined` lorsqu'aucune valeur ne correspond à la condition spécifiée.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.find(el => el['track'].includes('Pigs'));
// {no: 1, track: 'Pigs on the Wing (Part One)'}

animals.findLast(el => el['track'].includes('Pigs'));
// {no: 5, track: 'Pigs on the Wing (Part Two)'}

animals.find(el => el['track'].includes('Horses'));
// undefined
```

Dans l'exemple ci-dessus, seuls le premier et le dernier objets contenant 'Pigs' sont trouvés. L'objet du milieu `{no: 3, track: 'Pigs (Three Different Ones)'}` ne peut pas être atteint par ces deux méthodes.

### Comment utiliser les méthodes `findIndex()` et `findLastIndex()`

Les méthodes `findIndex()` et `findLastIndex()` fonctionnent de manière similaire aux précédentes.

```js
// Syntaxe
array.findIndex((element, index, array) => {})

array.findLastIndex((element, index, array) => {})
```

Mais elles retournent l'**index** du premier et du dernier élément qui satisfait la condition fournie, respectivement, ou `-1` (et non `undefined`) lorsqu'aucune valeur ne correspond à la condition spécifiée.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.findIndex(el => el['track'].includes('Pigs')); // 0

animals.findLastIndex(el => el['track'].includes('Pigs')); // 4

animals.findIndex(el => el['track'].includes('Horses')); // -1
```

## Comment vérifier si les éléments d'un tableau remplissent une condition

### Comment utiliser les méthodes `every()` et `some()`

Parfois, vous voulez vérifier si les éléments d'un tableau satisfont à une condition spécifique. Nous avons déjà vu la méthode `every()` dans une section précédente. Elle parcourt le tableau et retourne `true` si tous les éléments remplissent la condition spécifiée. Sinon, elle retourne `false`.

```js
// Syntaxe
array.every((element, index, array) => {})

array.some((element, index, array) => {})
```

La méthode `some()` est très similaire. Elle itère à travers le tableau, testant si **certains** éléments – pas nécessairement tous – répondent aux exigences implémentées par une fonction de rappel.

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn'];

nobleGases.every(el => typeof el == 'string'); // true

nobleGases.some(el => el == 'Ar'); // true

nobleGases.some(el => el == 'Rn'); // false
```

Le dernier appel retourne `false` puisqu'aucun des éléments du tableau n'est égal à la chaîne `'Rn'`.

### Comment utiliser la méthode `filter()`

Cette méthode vous offre un moyen de filtrer les éléments du tableau qui satisfont à un certain critère.

```js
// Syntaxe
array.filter((element, index, array) => {})
```

`filter()` prend une fonction de rappel dont les paramètres sont l'élément actuel, son index et le tableau sur lequel la méthode est appelée.

Elle crée une copie superficielle du tableau d'origine contenant uniquement les valeurs pour lesquelles le rappel retourne une valeur véridique (truthy), et elle ignore les autres.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.filter(el => el['track'].includes('Pigs'));
// [
// {no: 1, track: 'Pigs on the Wing (Part One)'},
// {no: 3, track: 'Pigs (Three Different Ones)'},
// {no: 5, track: 'Pigs on the Wing (Part Two)'}
// ]
```

Ci-dessus, seuls les éléments incluant 'Pigs' sont insérés dans le tableau filtré.

## Comment trier un tableau

### Comment utiliser la méthode `sort()`

Si vous voulez trier un tableau, vous pouvez utiliser `sort()`. Cette méthode trie les éléments du tableau **sur place** (in place). Elle modifie le tableau sur lequel elle agit.

```js
// Syntaxe
array.sort()

array.sort((a, b) => {})
```

La procédure de tri par défaut évalue les valeurs des points de code Unicode et peut parfois conduire à des résultats inattendus. Pour cette raison, il est préférable de passer à `sort()` une fonction de rappel afin que les éléments puissent être triés selon la valeur de retour du callback.

Le tableau suivant résume le critère de tri à la base de `sort()`.

| Valeur de retour de la comparaison (a, b) | ordre |
|-|-|
| > 0 | [b, a] |
| < 0 | [a, b] |
| === 0 | ordre original |

Les éléments – représentés par les paramètres a et b – sont comparés deux par deux. Si la valeur de retour est positive, a est placé après b. Si elle est négative, b est placé après a. Tandis que si la valeur de retour est zéro, l'ordre d'origine est conservé.

Voici un exemple de tri d'un tableau de chaînes par ordre croissant et décroissant :

```js
let nobleGases = ['He', 'Ne', 'Ar', 'Kr', 'Xn', 'Rn'];

// tri en ordre croissant
nobleGases.sort((a, b) => {
   return a === b ? 0 : a > b ? 1 : -1; 
}); 
// ['Ar', 'He', 'Kr', 'Ne', 'Rn', 'Xn']

// tri en ordre décroissant
nobleGases.sort((a, b) => {
   return a === b ? 0 : a < b ? 1 : -1; 
});
// ['Xn', 'Rn', 'Ne', 'Kr', 'He', 'Ar']

 
```

La fonction de rappel est implémentée par un opérateur ternaire, afin de prendre en compte les trois issues possibles de la comparaison.

## Comment effectuer une opération sur chaque élément d'un tableau

### Comment utiliser la méthode `map()`

Précédemment, nous avons utilisé `map()` pour dupliquer un tableau. Mais en utilisant une fonction de rappel différente, vous pouvez effectuer de nombreuses opérations variées.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

let tracks = animals.map(el => el['track']);

console.log(tracks); // ['Pigs on the Wing (Part One)', 'Dogs', 'Pigs (Three Different Ones)', 'Sheep', 'Pigs on the Wing (Part Two)']
```

Dans l'exemple ci-dessus, nous avons utilisé `map()` pour créer un tableau peuplé des valeurs de la clé `track` de chaque objet du tableau `animals`.

### Comment utiliser la méthode `forEach()`

La méthode `forEach()` est similaire à `map()`. Elle exécute une fonction sur chaque élément du tableau, mais elle n'a pas de valeur de retour. Pour cette raison, un appel à `forEach()` ne peut être utilisé qu'à la fin d'une chaîne.

```js
// Syntaxe
array.forEach((element, index, array) => {})
```

Dans l'exemple ci-dessous, `forEach()` est utilisé pour supprimer la propriété `no` de chaque élément du tableau :

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

animals.forEach(el => delete el['no']); // retourne undefined

console.log(animals); 
// [
//   {track: 'Pigs on the Wing (Part One)'},
//   {track: 'Dogs'},
//   {track: 'Pigs (Three Different Ones)'},
//   {track: 'Sheep'},
//   {track: 'Pigs on the Wing (Part Two)'}
// ]
```

### Comment utiliser la méthode `reduce()`

La méthode `reduce()` accepte une fonction de rappel qui est exécutée sur chaque élément du tableau. Le rappel prend un accumulateur comme premier paramètre, suivi de l'élément actuel, de son index et du tableau sur lequel la méthode est appelée.

La valeur de retour de chaque itération est transmise à la suivante. De sorte que le tableau est réduit à une seule valeur. Le second paramètre de `reduce()` est la valeur de départ de l'accumulateur (`accumulator`). S'il n'est pas spécifié, `accumulator` prend la première valeur du tableau et l'itération commence à l'index 1.

```js
// Syntaxe
array.reduce((accumulator, element, index, array) => {}, initialValue)
```

Dans l'exemple ci-dessous, la méthode `reduce()` est utilisée pour compter le nombre de pistes qui incluent 'Pigs' dans le titre. La méthode parcourt le tableau et, lorsque la propriété track inclut 'Pigs', la valeur de count est incrémentée et transmise à l'itération suivante.

```js
let animals = [
    {no: 1, track: 'Pigs on the Wing (Part One)'},
    {no: 2, track: 'Dogs'},
    {no: 3, track: 'Pigs (Three Different Ones)'},
    {no: 4, track: 'Sheep'},
    {no: 5, track: 'Pigs on the Wing (Part Two)'}
];

let countPigs = animals.reduce((count, el) => {
	return el['track'].includes('Pigs') ? count + 1 : count
	}, 0);

console.log(countPigs); // 3

```

Dans ce cas, il est important de spécifier la valeur initiale à zéro. Sinon, la valeur initiale sera l'objet complet `{no: 1, track: 'Pigs on the Wing (Part One)'}`, ce qui conduira à un résultat inattendu.

## Conclusion

En JavaScript, les tableaux sont des structures de données qui contiennent plusieurs valeurs dans un ordre spécifique. Ils peuvent contenir des valeurs de différents types de données et sont redimensionnables.

Dans ce tutoriel, nous avons commencé par les bases des tableaux en JavaScript, puis nous avons abordé certaines des méthodes les plus courantes qui vous permettent de manipuler les tableaux.

Nous n'avons fait qu'effleurer la surface de ce vaste sujet, mais j'espère que c'est un bon point de départ pour vous.

Merci de m'avoir lu, et bon code !