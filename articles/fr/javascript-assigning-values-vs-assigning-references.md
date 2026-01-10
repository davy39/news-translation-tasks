---
title: Valeurs primitives JavaScript vs valeurs de référence – Expliqué avec des exemples
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-04-18T16:31:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-assigning-values-vs-assigning-references
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-pedro-figueras-681447.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Valeurs primitives JavaScript vs valeurs de référence – Expliqué avec des
  exemples
seo_desc: 'Hi everyone! In JavaScript, variables can hold two types of data: primitive
  values and reference values. Understanding the difference between these two types
  of data is crucial for writing efficient and bug-free code.

  In this short article, we will e...'
---

Bonjour à tous ! En JavaScript, les variables peuvent contenir deux types de données : les valeurs primitives et les valeurs de référence. Comprendre la différence entre ces deux types de données est crucial pour écrire un code efficace et sans bogues.

Dans cet article court, nous allons explorer la différence entre les valeurs et les références en JavaScript.

# Table des matières

* [Qu'est-ce que les valeurs primitives ?](#heading-quest-ce-que-les-valeurs-primitives)
    
* [Qu'est-ce que les valeurs de référence ?](#heading-quest-ce-que-les-valeurs-de-reference)
    
* [Comment passer des valeurs et des références en arguments de fonction](#heading-comment-passer-des-valeurs-et-des-references-en-arguments-de-fonction)
    
* [Comment créer des copies d'objets, de tableaux et de fonctions](#heading-comment-creer-des-copies-dobjets-de-tableaux-et-de-fonctions)
    
    * [Copies superficielles vs copies profondes](#heading-copies-superficielles-vs-copies-profondes)
        
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que les valeurs primitives ?

Les valeurs primitives sont des données qui sont stockées directement dans une variable. Cela inclut les nombres, les booléens, les chaînes de caractères, null et undefined.

Lorsque nous assignons une valeur primitive à une variable, une copie de cette valeur est créée et stockée en mémoire. Toute modification apportée à la variable n'affecte pas la valeur originale.

Par exemple :

```javascript
let x = 5;
let y = x;
y = 10;
console.log(x); // Sortie : 5
console.log(y); // Sortie : 10
```

Dans l'exemple ci-dessus, la variable `y` reçoit une copie de la valeur de `x`. Lorsque nous changeons la valeur de `y`, cela n'affecte pas la valeur de `x`. Cela est dû au fait que `x` et `y` sont des variables distinctes avec des emplacements mémoire séparés.

# Qu'est-ce que les valeurs de référence ?

Les valeurs de référence, en revanche, sont des objets qui sont stockés en mémoire et accessibles par une référence. Cela inclut les tableaux, les objets et les fonctions.

Lorsque nous assignons une valeur de référence à une variable, une référence à la valeur originale est créée et stockée en mémoire. Toute modification apportée à la variable affecte la valeur originale.

Par exemple :

```javascript
let array1 = [1, 2, 3];
let array2 = array1;
array2.push(4);
console.log(array1); // Sortie : [1, 2, 3, 4]
console.log(array2); // Sortie : [1, 2, 3, 4]
```

Dans l'exemple ci-dessus, la variable `array2` reçoit une référence au tableau original `array1`. Lorsque nous ajoutons une valeur à `array2`, cela affecte également `array1` car les deux variables référencent le même emplacement mémoire.

# Comment passer des valeurs et des références en arguments de fonction

Lorsque nous passons une valeur primitive en argument à une fonction, une copie de cette valeur est créée et passée à la fonction. Toute modification apportée à la variable à l'intérieur de la fonction n'affecte pas la valeur originale.

Par exemple :

```javascript
function addOne(x) {
    x++;
    return x;
}

let number = 5;
console.log(addOne(number)); // Sortie : 6
console.log(number); // Sortie : 5
```

Dans l'exemple ci-dessus, la fonction `addOne` reçoit une copie de la valeur de `number`. Lorsque nous incrémentons la valeur de `x` à l'intérieur de la fonction, cela n'affecte pas la valeur de `number`.

Lorsque nous passons une valeur de référence en argument à une fonction, une référence à la valeur originale est passée. Toute modification apportée à la variable à l'intérieur de la fonction affecte la valeur originale.

Par exemple :

```javascript
function addToArray(array) {
    array.push(4);
    return array;
}

let myArray = [1, 2, 3];
console.log(addToArray(myArray)); // Sortie : [1, 2, 3, 4]
console.log(myArray); // Sortie : [1, 2, 3, 4]
```

Dans l'exemple ci-dessus, la fonction `addToArray` reçoit une référence au tableau original `myArray`. Lorsque nous ajoutons une valeur à `array` à l'intérieur de la fonction, cela affecte également `myArray` car les deux variables référencent le même emplacement mémoire.

# Comment créer des copies d'objets, de tableaux et de fonctions

Créer une copie d'un objet, d'un tableau ou d'une fonction peut être utile lorsque vous souhaitez modifier les données sans affecter l'original. Il existe plusieurs façons de créer une copie d'un objet en JavaScript.

Une façon de créer une copie superficielle d'un objet est d'utiliser la syntaxe de propagation d'objet, introduite dans ECMAScript 2018. La syntaxe est simple et ressemble à ceci :

```javascript
const originalObj = { name: "John", age: 30 };
const copyObj = { ...originalObj };
```

Dans cet exemple, `copyObj` est un nouvel objet avec les mêmes propriétés que `originalObj`. Cependant, la modification de `copyObj` n'affectera pas `originalObj`.

Pour les tableaux, la méthode `slice()` peut être utilisée pour créer une copie superficielle d'un tableau. Voici un exemple :

```javascript
const originalArr = [1, 2, 3, 4];
const copyArr = originalArr.slice();
```

Dans cet exemple, `copyArr` est un nouveau tableau avec les mêmes valeurs que `originalArr`.

En ce qui concerne la création d'une copie d'une fonction, les choses se compliquent un peu. Une approche consiste à créer une nouvelle fonction qui appelle simplement la fonction originale avec les mêmes arguments. Voici un exemple :

```javascript
function originalFunc(arg1, arg2) {
    // corps de la fonction ici
}
const copyFunc = function(...args) {
    return originalFunc.apply(this, args);
};
```

Dans cet exemple, `copyFunc` est une nouvelle fonction qui appelle `originalFunc` avec les mêmes arguments. Mais gardez à l'esprit que cela ne crée qu'une copie superficielle de la fonction. Toute fonction ou objet utilisé dans `originalFunc` référencera toujours les valeurs originales.

Comme vous pouvez le voir, la création de copies d'objets, de tableaux et de fonctions peut être une technique utile en programmation JavaScript. L'utilisation de la méthode appropriée pour le type de données avec lequel vous travaillez aidera à garantir que votre code se comporte comme prévu et soit plus maintenable à long terme.

## Copies superficielles vs copies profondes

En JavaScript, il existe deux façons de copier des objets et des tableaux : la copie superficielle et la copie profonde. Comprendre la différence entre ces deux types de copies est important, car cela peut affecter le comportement de votre code.

Une copie superficielle crée un nouvel objet ou tableau, mais elle ne copie que les références aux propriétés de l'objet ou du tableau original.

En d'autres termes, le nouvel objet ou tableau a les mêmes valeurs pour ses propriétés que l'original, mais les propriétés elles-mêmes référencent toujours les mêmes valeurs en mémoire. Cela signifie que toute modification apportée aux propriétés du nouvel objet ou tableau affectera également l'objet ou le tableau original, et vice versa.

Voici un exemple de copie superficielle d'un tableau :

```javascript
const originalArr = [1, 2, 3, [4, 5]];
const shallowCopyArr = [...originalArr];

shallowCopyArr[0] = 10;
shallowCopyArr[3][0] = 40;

console.log(originalArr); // [1, 2, 3, [40, 5]]
console.log(shallowCopyArr); // [10, 2, 3, [40, 5]]
```

Dans cet exemple, l'opérateur de propagation est utilisé pour créer une copie superficielle de `originalArr`. Ensuite, le premier élément de `shallowCopyArr` est changé en `10`, ce qui n'affecte pas `originalArr`. Mais lorsque le premier élément du tableau imbriqué dans `shallowCopyArr` est changé en `40`, il change également dans `originalArr`, car les deux tableaux partagent une référence au même tableau imbriqué.

Une copie profonde, en revanche, crée un nouvel objet ou tableau. Elle copie également les valeurs des propriétés de l'objet ou du tableau original, plutôt que simplement les références. Cela signifie que toute modification apportée au nouvel objet ou tableau n'affectera pas l'objet ou le tableau original, et vice versa.

Voici un exemple de copie profonde d'un tableau :

```javascript
const originalArr = [1, 2, 3, [4, 5]];
const deepCopyArr = JSON.parse(JSON.stringify(originalArr));

deepCopyArr[0] = 10;
deepCopyArr[3][0] = 40;

console.log(originalArr); // [1, 2, 3, [4, 5]]
console.log(deepCopyArr); // [10, 2, 3, [40, 5]]
```

Dans cet exemple, `JSON.stringify()` est utilisé pour convertir `originalArr` en une chaîne, puis `JSON.parse()` est utilisé pour convertir la chaîne en un tableau. Cela crée un nouveau tableau avec les mêmes valeurs que `originalArr`, mais le nouveau tableau est complètement indépendant du tableau original.

En conclusion, la principale différence entre une copie superficielle et une copie profonde en JavaScript est que la nouvelle copie ne copie que les références aux propriétés de l'objet ou du tableau original, ou si elle copie également les valeurs des propriétés.

Lors de la copie de types de données complexes comme les objets et les tableaux, il est important d'utiliser le type de copie approprié en fonction de votre cas d'utilisation.

# Conclusion

En résumé, comprendre la différence entre les valeurs et les références en JavaScript est essentiel pour écrire un code efficace et sans bogues. En étant conscient de la manière dont les données sont stockées et manipulées, vous pouvez éviter les comportements inattendus et améliorer les performances de vos applications.

Rappelez-vous que les types primitifs sont passés par valeur, tandis que les objets et les tableaux sont passés par référence. Gardez cela à l'esprit lorsque vous travaillez avec des fonctions et que vous assigner des variables.

Enfin, il est intéressant de noter qu'ECMAScript 6 a introduit un nouveau mot-clé appelé `let` qui se comporte plus comme les langages de programmation traditionnels en ce qui concerne l'assignation de variables. `let` vous permet de déclarer une variable avec une portée de bloc, ce qui signifie qu'elle n'est accessible que dans le bloc de code dans lequel elle est déclarée. Cela peut aider à prévenir la confusion avec les références et les valeurs, car la portée de la variable est limitée.

En conclusion, bien que les valeurs et les références puissent sembler un détail mineur dans le grand schéma de la programmation JavaScript, elles peuvent avoir un impact significatif sur le comportement et l'efficacité de votre code. En comprenant les différences et en utilisant les techniques appropriées pour votre situation particulière, vous pouvez écrire un code plus propre, plus efficace et moins sujet aux erreurs.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/04/monsters-inc-sully.gif align="left")