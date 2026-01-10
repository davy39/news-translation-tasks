---
title: La programmation fonctionnelle en JavaScript expliquée en anglais simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T16:45:41.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-javascript-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/blog1.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
seo_title: La programmation fonctionnelle en JavaScript expliquée en anglais simple
seo_desc: 'By Joel P. Mugalu

  One of the hardest things you have to do in programming is control complexity. Without
  careful consideration, a program''s size and complexity can grow to the point where
  it confuses even the creator of the program.

  In fact, as one a...'
---

Par Joel P. Mugalu

L'une des choses les plus difficiles que vous ayez à faire en programmation est de contrôler la complexité. Sans une considération minutieuse, la taille et la complexité d'un programme peuvent croître au point de confondre même le créateur du programme.

En fait, comme un auteur l'a dit :

> "L'art de la programmation est la compétence de contrôler la complexité" - Marijn Haverbeke

Dans cet article, nous allons décomposer un concept majeur de la programmation. Ce concept de programmation peut vous aider à garder la complexité sous contrôle et à écrire de meilleurs programmes.

À la fin de cet article, vous saurez ce qu'est la programmation fonctionnelle, les types de fonctions qui existent, les principes de la programmation fonctionnelle, et vous aurez une compréhension plus approfondie des fonctions d'ordre supérieur.

Je suppose que vous avez déjà des connaissances préexistantes sur les bases des fonctions. Les concepts fondamentaux des fonctions ne seront pas couverts dans cet article.

Si vous voulez une révision rapide des fonctions en JavaScript, alors j'ai écrit un article détaillé [ici](https://dev.to/codingknite/javascript-functions-broken-down-4fgh).

## Qu'est-ce que la programmation fonctionnelle ?

La programmation fonctionnelle est un paradigme de programmation ou un style de programmation qui repose fortement sur l'utilisation de fonctions pures et isolées.

Comme vous l'avez peut-être deviné d'après le nom, l'utilisation de fonctions est le principal composant de la programmation fonctionnelle. Mais, le simple fait d'utiliser des fonctions ne se traduit pas par de la programmation fonctionnelle.

En programmation fonctionnelle, nous utilisons des fonctions pures, qui sont des fonctions qui n'ont pas d'effets secondaires. Je vais expliquer ce que tout cela signifie.

Avant de plonger plus profondément dans l'article, comprenons certains des termes et types de fonctions qui existent.

## Types de fonctions

Il existe quatre principaux types de fonctions.

### Fonctions de première classe

En JavaScript, toutes les fonctions sont des fonctions de première classe. Cela signifie qu'elles peuvent être traitées comme n'importe quelle autre variable.

Les fonctions de première classe sont des fonctions qui peuvent être assignées comme valeurs à des variables, retournées par d'autres fonctions, et passées comme arguments à d'autres fonctions.

Considérez cet exemple de fonction passée à une variable :

```javascript
const helloWorld = () => {
	console.log("Hello, World"); // Hello, World
};
helloWorld();

```

### Fonctions de rappel

Les fonctions de rappel sont des fonctions qui sont passées à d'autres fonctions comme arguments et sont appelées par la fonction dans laquelle elles sont passées.

Simplement, les fonctions de rappel sont des fonctions que nous écrivons comme arguments dans d'autres fonctions. Nous ne pouvons pas invoquer les fonctions de rappel. Elles sont invoquées lorsque la fonction principale dans laquelle elles ont été passées comme arguments est appelée.

Regardons un exemple :

```javascript
const testValue = (value, test) => {
    if (test(value)) {
        return `${value} a passé le test`;
    } else 
        return `${value} n'a pas passé le test`;
};
const checkString = testValue('Twitter',  string  =>  typeof  string === 'string');
checkString; // Twitter a passé le test

```

`testValue` est une fonction qui accepte une valeur et une fonction de rappel `test` qui retourne "value a passé le test" si la valeur retourne vrai lorsqu'elle est passée dans la fonction de rappel.

Dans ce cas, la fonction de rappel est le deuxième argument que nous avons passé à la fonction `testValue`. Elle est invoquée lorsque la fonction `testValue` est appelée.

### Fonctions d'ordre supérieur

Les fonctions d'ordre supérieur sont des fonctions qui reçoivent d'autres fonctions comme arguments ou retournent une fonction.

Dans cet article, je vais élaborer davantage sur les fonctions d'ordre supérieur et pourquoi elles sont une disposition si puissante. Pour l'instant, tout ce que vous devez savoir, c'est que ces types de fonctions reçoivent d'autres fonctions comme arguments ou retournent des fonctions.

### Fonctions asynchrones

Les fonctions asynchrones sont des fonctions qui n'ont pas de nom et ne peuvent pas être réutilisées. Ces fonctions sont normalement écrites lorsque nous devons effectuer quelque chose une fois et en un seul endroit.

Un exemple parfait de fonction asynchrone est ce que nous avons écrit plus tôt dans l'article.

```javascript
const checkString = testValue('Twitter',  value  =>  typeof  value === 'string');
checkString;

// Voir le précédent extrait de code
```

`checkString` est une variable dont la valeur est une fonction. Nous passons deux arguments à cette fonction. 

`'Twitter'` est le premier argument et le second est une fonction asynchrone. Cette fonction n'a pas de nom et n'a qu'une seule tâche : vérifier si la valeur donnée est une chaîne de caractères.

![Principles Meme](https://memegenerator.net/img/instances/81322055.jpg)

## Principes de la programmation fonctionnelle

Plus tôt dans l'article, j'ai fait allusion au fait que le simple fait d'utiliser des fonctions ne se traduit pas par de la programmation fonctionnelle.

Il y a certains principes que nous devons comprendre si nos programmes doivent qualifier pour la norme de programmation fonctionnelle. Regardons ceux-ci.

### Éviter les mutations et les effets secondaires.

Le premier principe de la programmation fonctionnelle est d'éviter de changer les choses. Une fonction ne devrait pas changer quoi que ce soit comme une variable globale.

Cela est très important car les changements entraînent souvent des bugs. Si une fonction change une variable globale, par exemple, cela pourrait entraîner un comportement inattendu dans tous les endroits où cette variable est utilisée.

Le deuxième principe est qu'une fonction doit être pure, ce qui signifie qu'elle n'a pas d'effets secondaires. En programmation fonctionnelle, les changements qui sont faits sont appelés mutations, et les résultats sont appelés effets secondaires.

Une fonction pure ne fait ni l'un ni l'autre. Une fonction pure aura toujours la même sortie pour la même entrée.

Si une fonction dépend d'une variable globale, cette variable doit être passée à la fonction comme argument. Cela nous permet d'obtenir la même sortie pour la même entrée.

Voici un exemple :

```javascript
const legalAgeInTheUS = 21;
const checkLegalStatus = (age, legalAge) => {
    return age >= legalAge ? 'En âge légal.' : 'Pas en âge légal.';
};
const johnStatus = checkLegalStatus(18, legalAgeInTheUS);
johnStatus; // Pas en âge légal
legalAgeInTheUS; // 21

```

### Abstraction

Les abstractions cachent les détails et nous permettent de parler des problèmes à un niveau plus élevé sans décrire tous les détails de mise en œuvre du problème.

Nous utilisons des abstractions dans presque tous les aspects de notre vie, surtout dans la parole.

Par exemple, au lieu de dire _"Je vais échanger de l'argent contre une machine qui, une fois branchée, affiche des images mobiles accompagnées de son"_, vous êtes plus susceptible de dire _"Je vais acheter une télévision"_.

Dans ce cas, **acheter** et **télévision** sont des abstractions. Ces formes d'abstractions rendent la parole beaucoup plus facile et réduisent les chances de dire la mauvaise chose.

Mais vous serez d'accord avec moi que avant d'utiliser des termes abstraits comme **acheter**, vous devez d'abord comprendre le sens du terme et le problème qu'il abstrait.

Les fonctions nous permettent d'atteindre quelque chose de similaire. Nous pouvons créer des fonctions pour des tâches que nous sommes susceptibles de répéter encore et encore. Les fonctions nous permettent de créer nos propres abstractions.

En plus de créer nos propres abstractions, certaines fonctions ont déjà été créées pour nous pour abstraire les tâches que nous sommes susceptibles de faire encore et encore.

Nous allons donc examiner certaines de ces fonctions d'ordre supérieur qui existent déjà pour abstraire les tâches répétitives.

### Filtrer les tableaux

Lorsque nous travaillons avec des structures de données comme les tableaux, nous sommes susceptibles de nous retrouver dans une situation où nous ne sommes intéressés que par certains éléments du tableau.

Pour obtenir ces éléments, nous pouvons facilement créer une fonction pour effectuer la tâche :

```javascript
function filterArray(array, test) {
    const filteredArray = [];
    for (let item of array) {
        if (test(item)) {
            filteredArray.push(item);
        }
    }
    return filteredArray;
};
const mixedArray = [1, true, null, "Hello", undefined, "World", false];
const onlyStrings = filterArray(mixedArray, item => typeof item === 'string');
onlyStrings; // ['Hello', 'World']

```

`filterArray` est une fonction qui accepte un tableau et une fonction de rappel. Elle parcourt le tableau et ajoute les éléments qui passent le test dans la fonction de rappel dans un tableau appelé `filteredArray`.

En utilisant cette fonction, nous sommes capables de filtrer un tableau et de retourner les éléments qui nous intéressent, comme dans le cas de `mixedArray`.

Imaginez si nous avions 10 programmes différents et dans chaque programme nous devions filtrer un tableau. Tôt ou tard, il deviendrait extrêmement fastidieux de réécrire la même fonction encore et encore.

Heureusement, quelqu'un a déjà pensé à cela. Les tableaux ont une méthode standard `filter`. Elle retourne un nouveau tableau avec les éléments du tableau qu'elle reçoit qui passent le test que nous fournissons.

```javascript
const mixedArray = [1, true, null, "Hello", undefined, "World", false];
const stringArray = mixedArray.filter(item => typeof item === 'string')
stringArray; // ['Hello', 'World']

```

En utilisant la méthode de filtrage standard, nous avons pu obtenir les mêmes résultats que lorsque nous avons défini notre propre fonction dans l'exemple précédent. Donc, la méthode de filtrage est une abstraction de la première fonction que nous avons écrite.

### Transformer les éléments de tableau avec Map

Imaginez un autre scénario où nous avons un tableau d'éléments mais nous aimerions effectuer une certaine opération sur tous les éléments. Nous pouvons écrire une fonction pour le faire pour nous :

```javascript
function transformArray(array, test) {
    const transformedArray = [];
    for (let item of array) {
        transformedArray.push(test(item));
    }
    return transformedArray;
};
const ages = [12, 15, 21, 19, 32];
const doubleAges = transformArray(ages, age => age * 2);
doubleAges; // [24, 30, 42, 38, 64];

```

Tout simplement, nous avons créé une fonction qui parcourt n'importe quel tableau donné et transforme tous les éléments du tableau en fonction de la fonction de rappel que nous fournissons.

Mais encore une fois, cela deviendrait fastidieux si nous devions réécrire la fonction dans 20 programmes différents.

Encore une fois, quelqu'un a pensé à cela pour nous, et heureusement, les tableaux ont une méthode standard appelée `map` qui fait exactement la même chose. Elle applique la fonction de rappel sur tous les éléments du tableau donné et retourne un nouveau tableau.

```javascript
const ages = [12, 15, 21, 19, 32];
const doubleAges = ages.map(age => age * 2);
doubleAges; // [24, 30, 42, 38, 64];

```

### Réduire les tableaux avec Reduce

Voici un autre scénario : Vous avez un tableau de nombres, mais vous aimeriez calculer la somme de tous ces nombres et la retourner. Bien sûr, vous pouvez écrire une fonction pour le faire pour vous.

```javascript
function reduceArray(array, test, start) {
    let sum = start;
    for (let item of array) {
        sum = test(sum, item)
    }
    return sum;
}
let numbers = [5, 10, 20];
let doubleNumbers = reduceArray(numbers, (a, b) => a + b, 0);
doubleNumbers; // 35

```

Similaire aux exemples précédents que nous venons de voir, les tableaux ont une méthode standard `reduce` qui a la même logique que la fonction que nous venons d'écrire ci-dessus.

La méthode reduce est utilisée pour réduire un tableau à une seule valeur basée sur la fonction de rappel que nous fournissons. Elle prend également un deuxième argument optionnel qui spécifie où nous voulons que l'opération dans le rappel commence.

La fonction de rappel que nous fournissons dans la fonction reduce a deux paramètres. Le premier paramètre est le premier élément du tableau par défaut. Sinon, c'est le deuxième argument que nous fournissons dans la méthode reduce. Le deuxième paramètre est l'élément actuel du tableau.

```javascript
let numbers = [5, 10, 20];
let doubleNumbers = numbers.reduce((a, b) => a + b, 10);
doubleNumbers;  // 45

// L'exemple ci-dessus utilise la méthode reduce pour additionner tous les éléments du tableau à partir de 10.
```

## Autres méthodes utiles de tableau

### Array.some()

Tous les tableaux ont la méthode `some` qui accepte une fonction de rappel. Elle retourne `true` si **n'importe quel** élément du tableau passe le test donné dans la fonction de rappel. Sinon, elle retourne `false` :

```javascript
const numbers = [12, 34, 75, 23, 16, 63]
console.log(numbers.some(item => item < 100)) // true
```

### Array.every()

La méthode every est l'opposé de la méthode some. Elle accepte également une fonction de rappel et retourne `true` si **tous** les éléments du tableau passent le test donné dans la fonction de rappel. Sinon, elle retourne `false` :

```javascript
const numbers = [12, 34, 75, 23, 16, 63]
console.log(numbers.every(item => item < 100)) // true
```

### Array.concat()

La méthode `concat`, abréviation de concatenate, est une méthode standard de tableau qui concatène ou joint deux tableaux et retourne un nouveau tableau :

```javascript
const array1 = ['one', 'two', 'three'];
const array2 = ['four', 'five', 'six'];
const array3 = array1.concat(array2);
array3; // [ 'one', 'two', 'three', 'four', 'five', 'six' ]
```

### Array.slice()

La méthode `slice` est une méthode de tableau qui copie les éléments d'un tableau à partir d'un index donné et retourne un nouveau tableau avec les éléments copiés. La méthode `slice` accepte deux arguments.

Le premier argument reçoit l'index à partir duquel commencer la copie. Le deuxième argument reçoit l'index à partir duquel arrêter la copie. Elle retourne un nouveau tableau avec les éléments copiés de l'index de départ (exclusif) à l'index final (inclusif).

Notez cependant que la méthode slice n'utilise pas l'indexation zéro. Donc l'index du premier élément du tableau est 1 et non 0 :

```javascript
const numbers = [1,2,3,4,5,7,8];
console.log(theArray.slice(1, 4)); // [ 2, 3, 4 ]

```

## Conclusion

J'espère que vous avez apprécié la lecture de cet article et appris quelque chose de nouveau en même temps. 

Il existe de nombreuses méthodes de tableau et de chaîne que je n'ai pas mentionnées dans l'article. Si vous le souhaitez, prenez le temps de faire quelques recherches sur ces méthodes.

_Si vous souhaitez entrer en contact avec moi ou simplement dire bonjour, n'hésitez pas à le faire via [Twitter](http://twitter.com/joeepm). Je partage également des conseils et des ressources intéressants pour les développeurs._ ?