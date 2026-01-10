---
title: Qu'est-ce qu'une fonction de rappel en JavaScript ? Exemple de tutoriel JS
  Callbacks
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-09T00:32:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-callback-function-in-javascript-js-callbacks-example-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-pixabay-39656.jpg
tags:
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'une fonction de rappel en JavaScript ? Exemple de tutoriel
  JS Callbacks
seo_desc: 'In JavaScript there are higher order methods and functions that accept
  a function as an argument. These functions used as arguments for other functions
  are called callback functions.

  What is a callback in JavaScript?

  A callback is a function passed a...'
---

En JavaScript, il existe des méthodes et des fonctions d'ordre supérieur qui acceptent une fonction comme argument. Ces fonctions utilisées comme arguments pour d'autres fonctions sont appelées fonctions de rappel.

## Qu'est-ce qu'un rappel en JavaScript ?

Un rappel est une fonction passée comme argument d'une autre fonction.

Cela signifie que la fonction parente est généralement conçue pour utiliser n'importe quel type de fonction. Mais la fonction de rappel, en revanche, est destinée à être utilisée dans un cas spécifique (ou un nombre restreint de cas) dans lequel la fonction parente est utilisée.

## Comment créer une fonction de rappel en JavaScript ?

Vous créez une fonction de rappel comme n'importe quelle autre fonction en JavaScript :

```javascript
function callbackFunction() {
    
}
```

La différence entre une fonction de rappel et toute autre fonction réside dans la manière dont elle est utilisée.

Une fonction de rappel est spécifiquement conçue pour être utilisée comme argument d'une autre fonction.

```javascript
function anyFunction(fun) {
    // ...
    fun(a, b, c);
    //...
}

anyFunction(callbackFunction);
```

Ainsi, pour créer une `callbackFunction`, vous devez savoir comment la fonction parente utilise la fonction de rappel, quels arguments elle passe et dans quel ordre elle les passe.

### Quel est un exemple de fonction de rappel ?

Nous allons maintenant écrire notre propre fonction de rappel, car c'est quelque chose que vous devrez faire de nombreuses fois. Alors, commençons !

Une fonction d'ordre supérieur déjà intégrée dans le langage JavaScript est la méthode `every`.

La méthode `every` est une méthode de tableau et utilise un rappel pour vérifier que tous les éléments du tableau passent un certain test.

En consultant la [documentation sur la méthode `every`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every), vous pouvez voir que le rappel reçoit trois arguments : un élément du tableau, l'index de cet élément et le tableau entier.

Ainsi, la signature de la fonction de rappel serait quelque chose comme ceci :

```javascript
function callbackFunction(element, index, array) {
    // faire quelque chose
}
```

Les fonctions de rappel peuvent être aussi simples ou aussi complexes que nécessaire. Pour créer un exemple, nous avons besoin d'un contexte.

### Comment écrire une fonction de rappel en JavaScript

Supposons que vous travaillez avec des tableaux de chaînes de caractères. Vous devez vérifier si le tableau ne contient que des chaînes qui sont exactement de trois caractères de long, en majuscules, contiennent toutes des lettres différentes et qu'elles ne se répètent pas à l'intérieur du tableau.

C'est un cas assez complexe, mais peut-être devrez-vous éventuellement faire quelque chose de similaire ou de complexité égale, donc c'est une bonne pratique.

Vous pouvez aborder une condition à la fois lorsque vous construisez une fonction avec autant de choses à vérifier.

La première condition est que l'élément est une chaîne, alors ajoutons-la :

```javascript
function callbackFunction(element, index, array) {
    
    // vérifier que l'élément est une chaîne
	const isNotString = typeof element !== "string";
    // si ce n'est pas le cas, terminer la fonction
    if (isNotString) {return;}
    
}
```

Ensuite, les chaînes doivent être toutes en majuscules, ne contenir que des lettres et faire 3 caractères de long.

Vous pourriez vérifier ces trois conditions séparément, ou vous pouvez les vérifier ensemble avec une expression régulière qui vérifie exactement ces trois choses.

Une telle expression régulière ressemblerait à ceci : `/^[A-Z]{3}$/`.

Voyons quelles sont les parties de cette expression régulière :

* Les caractères `^` au début et `$` à la fin sont des ancres. Ceux-ci indiquent que la chaîne doit commencer et se terminer exactement de cette manière. Et si vous utilisez les deux, ils restreignent une chaîne à contenir uniquement et exactement le motif de l'expression régulière.
* `[A-Z]` est une classe de caractères qui correspond à n'importe quel caractère de `A` à `Z`, donc toutes les lettres majuscules.
* `{3}` est un compteur. Cela indique que la chose précédente doit être correspondante exactement trois fois consécutives.

L'expression régulière expliquée ci-dessus est l'équivalent de cette expression régulière : `/^[A-Z][A-Z][A-Z]$/`.

Dans ce cas, au lieu du compteur `{3}`, nous avons écrit la classe `[A-Z]` trois fois.

Ajoutons cela au code.

```javascript
function callbackFunction(element, index, array) {
    
    // vérifier que l'élément est une chaîne
    const isNotString = typeof element !== "string";
    // si ce n'est pas le cas, terminer la fonction
    if (isNotString) {
        return;
    }
    
    // vérifier que la chaîne fait 3 caractères de long et ne contient que des lettres majuscules
    const isItThreeUpperCaseLetters = /^[A-Z]{3}$/.test(element);
    // sinon, terminer la fonction
    if (!isItThreeUpperCaseLetters) {
        return;
    }
    
}
```

Si vous n'aimez pas les expressions régulières, vous pouvez lire [ci-dessous](#heading-installation) comment effectuer les mêmes vérifications sans utiliser d'expression régulière.

Ensuite, nous devons vérifier si les caractères sont tous différents.

Il y a trois caractères que vous pouvez utiliser : `element[0] !== element[1] && element[0] !== element[2] && element[1] !== element[2]`.

Mais vous pouvez aussi faire cela avec une boucle – en fait une double boucle.

```javascript
// avec la boucle externe, vous obtenez j, le premier index à comparer
for (let j = 0; j++; j < element.length) {
    // avec la boucle interne, vous obtenez k, le second index à comparer
    for (let k = j+1; k++; k < element.length) {
        // vous comparez l'élément à l'index j avec l'élément à l'index k
        if (element[j] === element[k]) {
            // s'ils sont égaux, retourner pour arrêter la fonction
            return;
        }
    }
}
```

La boucle fonctionnera avec n'importe quelle longueur, et vous n'avez pas besoin de la réécrire pour différentes situations.

Est-ce exactement la même chose que d'écrire les trois comparaisons ? Suivons la boucle pour vérifier.

À la première itération, nous avons `j=0`, et `k=1`, donc la première comparaison est `element[0] === element[1]`. Ensuite, `k` augmente, donc c'est `j=0` et `k=2`, donc c'est `element[0] === element[2]`.

À ce stade, la boucle interne s'arrête, et la boucle externe (celle avec `j`) passe à l'itération suivante. Cette fois, `j=1`, et la boucle interne commence à `k=j+1` donc à `k=2` – la comparaison ici est `element[1] === element[2]`.

La boucle interne a terminé de boucler, la boucle externe passe de `j=1` à `j=2`, la boucle interne ne démarre pas car `k = j+1 = 3` ne passe pas la condition `k < element.length` de la boucle.

```javascript
function callbackFunction(element, index, array) {
    
    
    // vérifier que l'élément est une chaîne
    const isNotString = typeof element !== "string";
    // si ce n'est pas le cas, terminer la fonction
    if (isNotString) {
        return;
    }
    
    
    // vérifier que la chaîne fait 3 caractères de long et ne contient que des lettres majuscules
    const isItThreeUpperCaseLetters = /^[A-Z]{3}$/.test(element);
    // sinon, terminer la fonction
    if (!isItThreeUpperCaseLetters) {
        return;
    }
    
    
    // vérifier si tous les caractères sont différents
    const allDifferentCharacters = element[0] !== element[1] && element[0] !== element[2] && element[1] !== element[2];
    // si ce n'est pas le cas, retourner pour arrêter la fonction
    if (!allDifferentCharacters) {
        return;
    }
    
    
    
}
```

Ensuite, la dernière chose que nous devons vérifier est que les chaînes ne sont pas répétées à l'intérieur du tableau.

Nous pouvons utiliser `indexOf` pour vérifier que l'élément actuel est la première apparition de `element` à l'intérieur du tableau.

Nous devrions référencer le tableau pour cela. Et nous l'avons – c'est l'un des arguments passés dans le rappel, le paramètre `array`.

Si c'est la première apparition de la chaîne dans le tableau, la sortie de `indexOf` sera la même que `index`.

Si `array.indexOf(element) === index` est `true`, cela signifie que `element` est présent dans le tableau pour la première fois à `index`. Si c'est `false`, une chaîne identique est présente plus tôt dans le tableau.

Ajoutons cette vérification à la fonction. Et si la chaîne a survécu à toutes les vérifications, alors la fonction peut retourner `true` à la fin.

```javascript
function callbackFunction(element, index, array) {
    
    
    // vérifier que l'élément est une chaîne
    const isNotString = typeof element !== "string";
    // si ce n'est pas le cas, terminer la fonction
    if (isNotString) {
        return;
    }
    
    
    // vérifier que la chaîne fait 3 caractères de long et ne contient que des lettres majuscules
    const isItThreeUpperCaseLetters = /^[A-Z]{3}$/.test(element);
    // sinon, terminer la fonction
    if (!isItThreeUpperCaseLetters) {
        return;
    }
    
    
    // vérifier si tous les caractères sont différents
    const allDifferentCharacters = element[0] !== element[1] && element[0] !== element[2] && element[1] !== element[2];
    // si ce n'est pas le cas, retourner pour arrêter la fonction
    if (!allDifferentCharacters) {
        return;
    }
    
    
    // vérifier si c'est la première apparition de l'élément à l'intérieur du tableau
    const isItFirstAppearence = array.indexOf(element) === index;
    // si ce n'est pas le cas, retourner pour arrêter la fonction
    if (!isItFirstAppearence) {
        return;
    }
    
    
    return true;
}
```

#### Et si nous n'avions pas utilisé d'expression régulière ?

Dans le code ci-dessus, pour vérifier trois choses différentes, nous avons utilisé une expression régulière : `/^[A-Z]{3}$/`.

Mais si vous ne voulez pas travailler avec les regex, vous pouvez utiliser la propriété `length` pour vérifier si une chaîne est d'une longueur exactement certaine. Dans ce cas, `element.length === 3` pour vérifier que la chaîne est exactement de trois caractères de long.

Ensuite, la chaîne doit être entièrement en majuscules et ne contenir que des lettres.

Vous pouvez utiliser `charCodeAt` pour cela. Cette méthode retourne le code ASCII d'un caractère, et sachant que les lettres majuscules ont des codes ASCII de 65 à 90, vous pouvez vérifier qu'il n'y a que des lettres majuscules.

Il y a trois nombres à vérifier : `element.charCodeAt(0)`, `element.charCodeAt(1)`, et `element.charCodeAt(2)`. Ils doivent tous être compris entre 65 et 90. Ce ne sont que trois caractères, mais nous pouvons toujours utiliser une boucle.

Donc, cela serait comme ci-dessous :

```javascript
for (let i = 0; i++; i < element.length) {
    // trouver le code ASCII du caractère
    const code = element.charCodeAt(i);
    // vérifier s'il est en dehors de la plage
    if (code < 65 || code > 90) {
        // si c'est le cas, retourner pour arrêter la fonction
        return;
    }
}
```

Ajoutons cela à la fonction :

```javascript
function callbackFunction(element, index, array) {
    
    // vérifier que l'élément est une chaîne
    const isNotString = typeof element !== "string";
    // si ce n'est pas le cas, terminer la fonction
    if (isNotString) {return;}
    
    // vérifier que l'élément a une longueur de chaîne
    const hasLengthThree = element.length === 3;
    // s'il a une longueur différente, terminer la fonction
    if (!hasLengthThree) {return;}
    
    // boucler sur les caractères
	for (let i = 0; i++; i < element.length) {
        // trouver le code ASCII du caractère
        const code = element.charCodeAt(i);
        // vérifier s'il est en dehors de la plage
        if (code < 65 || code > 90) {
            // s'il est en dehors de la plage, retourner et arrêter la fonction
            return;
        }
    } 
}
```

Si vous êtes arrivé ici depuis le lien ci-dessus, vous pouvez y retourner pour continuer à lire comment terminer la fonction, sinon, veuillez continuer jusqu'à la fin.

### Comment utiliser la fonction de rappel d'exemple

Nous avons écrit la fonction de rappel. Alors, comment l'utiliser ?

```javascript
anArray.every(callbackFunction);
```

Vous pouvez également utiliser la méthode `every` à l'intérieur d'un rappel – peut-être le rappel d'une [méthode `filter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).

À mesure qu'un programme devient plus complexe, il utilisera probablement proportionnellement plus de fonctions de rappel.

## Pourquoi utilisons-nous des fonctions de rappel en JavaScript ?

Les fonctions de rappel sont une fonctionnalité pratique de JavaScript. Cela signifie que nous pouvons avoir une fonction générale qui fait quelque chose (comme `every` qui vérifie si chaque élément d'un tableau correspond à une certaine condition, `filter`, qui supprime les éléments qui ne correspondent pas à une certaine condition, `replace`, une méthode de chaîne qui accepte un rappel pour décrire comment remplacer des parties d'une chaîne, et ainsi de suite) et une fonction de rappel pour ajouter des spécificités de ce comportement pour la situation spécifique.

* `filter` dans cette situation supprimera les éléments spécifiés par le rappel.
* `every` vérifiera que tous les éléments dans cette situation sont tels que spécifiés par la fonction de rappel.
* `replace` remplacera des parties de la chaîne dans la situation dans laquelle elle est utilisée telle que spécifiée par le rappel.

Les fonctions d'ordre supérieur ajoutent un niveau d'abstraction au code. Nous ne savons pas (et n'avons pas besoin de savoir) comment `every` vérifie chaque élément du tableau et vérifie qu'ils passent tous les tests spécifiés par le rappel. Nous devons seulement savoir que la méthode accepte une fonction de rappel pour cela.

## Conclusion

Les rappels sont des fonctions qui sont passées comme arguments d'autres fonctions. Vous avez vu un exemple de comment en créer une, et quelques considérations sur pourquoi elles sont utiles.

Merci d'avoir lu !