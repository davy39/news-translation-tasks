---
title: Pourquoi ai-je écrit cet article ?
date: '2021-05-21T15:33:45.000Z'
author: Tapas Adhikary
authorURL: https://www.freecodecamp.org/news/author/atapas/
originalURL: https://freecodecamp.org/news/the-javascript-array-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/JavaScript-Array-Handbook-Book-Cover--1-.png
tags:
- name: arrays
  slug: arrays
- name: beginners guide
  slug: beginners-guide
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_desc: "In programming, an array is a collection of elements or items. Arrays store\
  \ data as elements and retrieve them back when you need them. \nThe array data structure\
  \ is widely used in all programming languages that support it.\nIn this handbook,\
  \ I'll teac..."
---


En programmation, un `array` (tableau) est une collection d'éléments ou d'articles. Les tableaux stockent des données sous forme d'éléments et les récupèrent lorsque vous en avez besoin.

<!-- more -->

La structure de données de type tableau est largement utilisée dans tous les langages de programmation qui la supportent.

Dans ce manuel, je vais vous apprendre tout ce qu'il faut savoir sur les tableaux en JavaScript. Vous en apprendrez davantage sur la gestion de données complexes, la déstructuration, les méthodes de tableau les plus couramment utilisées, et bien plus encore.

# Pourquoi ai-je écrit cet article ?

Il existe déjà de nombreux excellents articles sur les tableaux JavaScript sur Internet. Alors pourquoi en écrire un de plus sur le même sujet ? Quelle est la motivation ?

Eh bien, au fil des années d'interaction avec mes mentorés, j'ai réalisé que la plupart des débutants ont besoin d'un tutoriel qui couvre les tableaux de manière approfondie, du début à la fin, avec des exemples.

J'ai donc décidé de créer un tel article, regorgeant d'exemples concrets. Si vous êtes débutant en JavaScript, j'espère que vous le trouverez très utile.

Mais même en tant que développeur expérimenté, ce manuel peut s'avérer pratique pour vous aider à rafraîchir vos connaissances au besoin. J'apprends également tout à nouveau en écrivant à ce sujet. Alors, plongeons dans le vif du sujet.

# Qu'est-ce qu'un tableau en JavaScript ?

Une paire de `square brackets []` (crochets) représente un tableau en JavaScript. Tous les éléments du tableau sont séparés par une `comma(,)` (virgule).

En JavaScript, les tableaux peuvent être une collection d'éléments de n'importe quel type. Cela signifie que vous pouvez créer un tableau avec des éléments de type String, Boolean, Number, Objects, et même d'autres Arrays.

Voici un exemple d'un tableau avec quatre éléments : de type Number, Boolean, String et Object.

```
const mixedTypedArray = [100, true, 'freeCodeCamp', {}];
```

La position d'un élément dans le tableau est connue sous le nom d' `index`. En JavaScript, l'index d'un tableau commence à `0`, et il augmente de un pour chaque élément.

Ainsi, par exemple, dans le tableau ci-dessus, l'élément 100 est à l' `index 0`, true est à l' `index 1`, 'freeCodeCamp' est à l' `index 2`, et ainsi de suite.

Le nombre d'éléments dans le tableau détermine sa longueur (`length`). Par exemple, la longueur du tableau ci-dessus est de quatre.

Il est intéressant de noter que les tableaux JavaScript n'ont pas une longueur fixe. Vous pouvez modifier la longueur à tout moment en assignant une valeur numérique positive. Nous en apprendrons plus à ce sujet dans un instant.

# Comment créer un tableau en JavaScript

Vous pouvez créer un tableau de plusieurs manières en JavaScript. La façon la plus simple est d'assigner une valeur de tableau à une variable.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
```

Vous pouvez également utiliser le constructeur `Array` pour créer un tableau.

```
const salad = new Array('🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑');
```

> Remarque : `new Array(2)` créera un tableau d'une longueur de deux dont aucun des éléments n'est défini. Cependant, `new Array(1,2)` créera un tableau d'une longueur de deux contenant les éléments 1 et 2.

Il existe d'autres méthodes comme `Array.of()` et `Array.from()`, et l'opérateur `spread` ( `...`) vous aide également à créer des tableaux. Nous les aborderons plus tard dans cet article.

## Comment obtenir des éléments d'un tableau en JS

Vous pouvez accéder aux éléments d'un tableau et les récupérer en utilisant leur index. Vous devez utiliser la syntaxe des `square bracket` (crochets) pour accéder aux éléments du tableau.

```
const element = array[index];
```

Selon vos cas d'utilisation, vous pouvez choisir d'accéder aux éléments du tableau un par un ou dans une boucle.

Lorsque vous accédez aux éléments en utilisant l'index comme ceci :

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
salad[0]; // '🍅'
salad[2]; // '🥦'
salad[5]; // '🥕'
```

Vous pouvez utiliser la longueur d'un tableau pour le parcourir à rebours et accéder aux éléments.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
const len = salad.length;
salad[len - 1]; // '🥑'
salad[len - 3]; // '🌽'
```

Vous pouvez également parcourir le tableau en utilisant une boucle `for` classique, une boucle `forEach`, ou toute autre boucle.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];

for(let i=0; i<salad.length; i++) {
  console.log(`Element at index ${i} is ${salad[i]}`);
}
```

Et voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-30.png)

## Comment ajouter des éléments à un tableau en JS

Utilisez la méthode `push()` pour insérer un élément dans un tableau. La méthode `push()` ajoute un élément à la fin du tableau. Et si nous ajoutions des cacahuètes à la salade, comme ceci :

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
salad.push('🥜');
```

Maintenant, le tableau salad est :

\["🍅", "🍄", "🥦", "🥒", "🌽", "🥕", "🥑", "🥜"\]

Notez que la méthode `push()` ajoute un élément à la fin du tableau. Si vous souhaitez ajouter un élément au début du tableau, vous devrez utiliser la méthode `unshift()`.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
salad.unshift('🥜');
```

Maintenant, le tableau salad est :

\["🥜", "🍅", "🍄", "🥦", "🥒", "🌽", "🥕", "🥑"\]

## Comment supprimer des éléments d'un tableau en JS

Le moyen le plus simple de supprimer un seul élément d'un tableau est d'utiliser la méthode `pop()`. Chaque fois que vous appelez la méthode `pop()`, elle supprime un élément à la fin du tableau. Ensuite, elle renvoie l'élément supprimé et modifie le tableau d'origine.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
salad.pop(); // 🥑

console.log(salad); // ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕']
```

Utilisez la méthode `shift()` pour supprimer un élément au début d'un tableau. Comme la méthode `pop()`, `shift()` renvoie l'élément supprimé et modifie le tableau d'origine.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
salad.shift(); // 🍅

console.log(salad); // ['🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
```

## Comment copier et cloner un tableau en JS

Vous pouvez copier et cloner un tableau dans un nouveau tableau en utilisant la méthode `slice()`. Notez que la méthode `slice()` ne modifie pas le tableau d'origine. Au lieu de cela, elle crée une nouvelle copie superficielle (shallow copy) du tableau d'origine.

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];
const saladCopy = salad.slice();

console.log(saladCopy); // ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑']

salad === saladCopy; // returns false
```

Alternativement, vous pouvez utiliser l'opérateur `spread` pour créer une copie du tableau. Nous en apprendrons plus à ce sujet bientôt.

## Comment déterminer si une valeur est un tableau en JS

Vous pouvez déterminer si une valeur est un tableau en utilisant la méthode `Array.isArray(value)`. La méthode renvoie true si la valeur passée est un tableau.

```
Array.isArray(['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑']); // returns true
Array.isArray('🍅'); // returns false
Array.isArray({ 'tomato': '🍅'}); // returns false
Array.isArray([]); // returns true
```

# Déstructuration de tableau en JavaScript

Avec l'ECMAScript 6 (ES6), nous disposons d'une nouvelle syntaxe pour extraire plusieurs propriétés d'un tableau et les assigner à des variables en une seule fois. C'est très pratique pour garder votre code propre et concis. Cette nouvelle syntaxe est appelée syntaxe de déstructuration.

Voici un exemple d'extraction des valeurs d'un tableau en utilisant la syntaxe de déstructuration :

```
let [tomato, mushroom, carrot] = ['🍅', '🍄', '🥕'];
```

Vous pouvez maintenant utiliser les variables dans votre code :

```
console.log(tomato, mushroom, carrot); // Output, 🍅 🍄 🥕
```

Pour faire la même chose sans la déstructuration, cela ressemblerait à ceci :

```
let vegetables = ['🍅', '🍄', '🥕'];
let tomato = vegetables[0];
let mushroom= vegetables[1];
let carrot= vegetables[2];
```

Ainsi, la syntaxe de déstructuration vous évite d'écrire beaucoup de code. Cela vous donne un gain de productivité massif.

## Comment assigner une valeur par défaut à une variable

Vous pouvez assigner une valeur par défaut en utilisant la déstructuration lorsqu'il n'y a pas de valeur ou que l'élément du tableau est `undefined`.

Dans l'exemple ci-dessous, nous assignons une valeur par défaut pour la variable mushroom.

```
let [tomato , mushroom = '🍄'] = ['🍅'];
console.log(tomato); // '🍅'
console.log(mushroom ); // '🍄'
```

## Comment ignorer une valeur dans un tableau

Avec la déstructuration, vous pouvez ignorer un élément du tableau lors de la correspondance avec une variable. Par exemple, vous pourriez ne pas être intéressé par tous les éléments d'un tableau. Dans ce cas, ignorer une valeur s'avère pratique.

Dans l'exemple ci-dessous, nous ignorons l'élément mushroom. Notez l'espace dans la déclaration de variable sur le côté gauche de l'expression.

```
let [tomato, , carrot] = ['🍅', '🍄', '🥕'];

console.log(tomato); // '🍅'
console.log(carrot); // '🥕'
```

## Déstructuration de tableaux imbriqués en JS

En JavaScript, les tableaux peuvent être imbriqués. Cela signifie qu'un tableau peut avoir un autre tableau comme élément. L'imbrication de tableaux peut aller à n'importe quelle profondeur.

Par exemple, créons un tableau imbriqué pour les fruits. Il contient quelques fruits et un tableau de légumes.

```
let fruits = ['🍈', '🍍', '🍌', '🍉', ['🍅', '🍄', '🥕']];
```

Comment accéderiez-vous à '🥕' à partir du tableau ci-dessus ? Encore une fois, vous pourriez le faire sans déstructuration, comme ceci :

```
const veg = fruits[4]; // returns the array ['🍅', '🍄', '🥕']
const carrot = veg[2]; // returns '🥕'
```

Alternativement, vous pourriez utiliser cette syntaxe raccourcie :

```
fruits[4][2]; // returns '🥕'
```

Vous pouvez également y accéder en utilisant la syntaxe de déstructuration, comme ceci :

```
let [,,,,[,,carrot]] = ['🍈', '🍍', '🍌', '🍉', ['🍅', '🍄', '🥕']];
```

# Comment utiliser la syntaxe Spread et le paramètre Rest en JavaScript

Depuis ES6, nous pouvons utiliser `...` (oui, trois points consécutifs) comme syntaxe spread et paramètre rest dans la déstructuration de tableau.

-   Pour le paramètre rest, le `...` apparaît sur le côté gauche de la syntaxe de déstructuration.
-   Pour la syntaxe spread, le `...` apparaît sur le côté droit de la syntaxe de déstructuration.

## Comment utiliser le paramètre Rest en JS

Avec le `Rest Parameter`, nous pouvons extraire les éléments restants d'un tableau dans un nouveau tableau. Le paramètre rest doit être la dernière variable de la syntaxe de déstructuration.

Dans l'exemple ci-dessous, nous avons fait correspondre les deux premiers éléments du tableau aux variables tomato et mushroom. Les éléments restants sont mis en correspondance avec la variable `rest` en utilisant le `...`. La variable `rest` est un nouveau tableau contenant les éléments restants.

```
const [tomato, mushroom, ...rest] = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];

console.log(tomato); // '🍅'
console.log(mushroom); // '🍄'
console.log(rest); // ["🥦", "🥒", "🌽", "🥕", "🥑"]
```

## Comment utiliser l'opérateur Spread en JS

Avec l'opérateur spread, nous pouvons créer un clone/une copie d'un tableau existant comme ceci :

```
const salad = ['🍅', '🍄', '🥦', '🥒', '🌽', '🥕', '🥑'];

const saladCloned = [...salad];
console.log(saladCloned); // ["🍅", "🍄", "🥦", "🥒", "🌽", "🥕", "🥑"]

salad === saladCloned // false
```

# Cas d'utilisation de la déstructuration en JavaScript

Examinons quelques cas d'utilisation intéressants de la déstructuration de tableau, de l'opérateur spread et du paramètre rest.

## Comment échanger des valeurs avec la déstructuration

Nous pouvons facilement échanger la valeur de deux variables en utilisant la syntaxe de déstructuration de tableau.

```
let first = '😔';
let second = '🙂';
[first, second] = [second, first];

console.log(first);  // '🙂'
console.log(second); // '😔'
```

## Comment fusionner des tableaux

Nous pouvons fusionner deux tableaux et créer un nouveau tableau avec tous les éléments des deux tableaux. Prenons deux tableaux — l'un avec quelques smileys et l'autre avec quelques légumes.

```
const emotion = ['🙂', '😔'];
const veggies = ['🥦', '🥒', '🌽', '🥕'];
```

Maintenant, nous allons les fusionner pour créer un nouveau tableau.

```
const emotionalVeggies = [...emotion, ...veggies];
console.log(emotionalVeggies); // ["🙂", "😔", "🥦", "🥒", "🌽", "🥕"]
```

# Méthodes de tableau JavaScript

Jusqu'à présent, nous avons vu quelques propriétés et méthodes de tableau. Faisons un récapitulatif rapide de celles que nous avons examinées :

-   `push()` – Insérer un élément à la fin du tableau.
-   `unshift()` – Insérer un élément au début du tableau.
-   `pop()` – Supprimer un élément à la fin du tableau.
-   `shift()` – Supprimer un élément au début du tableau.
-   `slice()` – Créer une copie superficielle d'un tableau.
-   `Array.isArray()` – Déterminer si une valeur est un tableau.
-   `length` – Déterminer la taille d'un tableau.

Nous allons maintenant découvrir d'autres méthodes importantes des tableaux JS avec des exemples.

## Comment créer, supprimer, mettre à jour et accéder aux tableaux en JavaScript

Dans cette section, nous allons découvrir les méthodes que vous pouvez utiliser pour créer un nouveau tableau, supprimer des éléments pour vider le tableau, accéder aux éléments, et bien plus encore.

### La méthode de tableau `concat()`

La méthode `concat()` fusionne un ou plusieurs tableaux et renvoie un tableau fusionné. C'est une méthode immuable. Cela signifie qu'elle ne modifie pas (ne mute pas) les tableaux existants.

Fusionnons deux tableaux.

```
const first = [1, 2, 3];
const second = [4, 5, 6];

const merged = first.concat(second);

console.log(merged); // [1, 2, 3, 4, 5, 6]
console.log(first); // [1, 2, 3]
console.log(second); // [4, 5, 6]
```

En utilisant la méthode `concat()`, nous pouvons fusionner plus de deux tableaux. Nous pouvons fusionner n'importe quel nombre de tableaux avec cette syntaxe :

```
array.concat(arr1, arr2,..,..,..,arrN);
```

Voici un exemple :

```
const first = [1, 2, 3];
const second = [4, 5, 6];
const third = [7, 8, 9];

const merged = first.concat(second, third);

console.log(merged); // [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### La méthode de tableau `join()`

La méthode `join()` joint tous les éléments du tableau en utilisant un séparateur et renvoie une chaîne de caractères. Le séparateur par défaut utilisé pour la jonction est la `comma(,)` (virgule).

```
const emotions = ['🙂', '😍', '🙄', '😟'];

const joined = emotions.join();
console.log(joined); // "🙂,😍,🙄,😟"
```

Vous pouvez passer le séparateur de votre choix pour joindre les éléments. Voici un exemple de jonction d'éléments avec un séparateur personnalisé :

```
const joined = emotions.join('<=>');
console.log(joined); // "🙂<=>😍<=>🙄<=>😟"
```

L'appel de la méthode `join()` sur un tableau vide renvoie une chaîne vide :

```
[].join() // returns ""
```

### La méthode de tableau `fill()`

La méthode `fill()` remplit un tableau avec une valeur statique. Vous pouvez changer tous les éléments en une valeur statique ou changer quelques éléments sélectionnés. Notez que la méthode `fill()` modifie le tableau d'origine.

```
const colors = ['red', 'blue', 'green'];

colors.fill('pink');
console.log(colors); // ["pink", "pink", "pink"]
```

Voici un exemple où nous ne modifions que les deux derniers éléments du tableau en utilisant la méthode `fill()` :

```
const colors = ['red', 'blue', 'green'];

colors.fill('pink', 1,3); // ["red", "pink", "pink"]
```

Dans ce cas, le premier argument de la méthode `fill()` est la valeur avec laquelle nous effectuons le changement. Le deuxième argument est l'index de début pour le changement. Il commence à `0`. Le dernier argument sert à déterminer où arrêter le remplissage. Sa valeur maximale peut être `colors.length`.

Veuillez consulter ce fil Twitter pour une utilisation pratique de la méthode `fill()`.

> [][1]

De plus, vous pourriez trouver ce projet de démonstration utile : [https://github.com/atapas/array-fill-color-cards][2].

### La méthode de tableau `includes()`

Vous pouvez déterminer la présence d'un élément dans un tableau en utilisant la méthode `includes()`. Si l'élément est trouvé, la méthode renvoie `true`, et `false` sinon.

```
const names = ['tom', 'alex', 'bob', 'john'];

names.includes('tom'); // returns true
names.includes('july'); // returns false
```

### La méthode de tableau `indexOf()`

Vous pourriez vouloir connaître la position de l'index d'un élément dans un tableau. Vous pouvez utiliser la méthode `indexOf()` pour l'obtenir. Elle renvoie l'index de la première occurrence d'un élément dans le tableau. Si un élément n'est pas trouvé, la méthode `indexOf()` renvoie `-1`.

```
const names = ['tom', 'alex', 'bob', 'john'];

names.indexOf('alex'); // returns 1
names.indexOf('rob'); // returns -1
```

Il existe une autre méthode `lastIndexOf()` qui vous aide à trouver l'index de la dernière occurrence d'un élément dans le tableau. Comme `indexOf()`, `lastIndexOf()` renvoie également `-1` si l'élément n'est pas trouvé.

```
const names = ['tom', 'alex', 'bob', 'tom'];

names.indexOf('tom'); // returns 0
names.lastIndexOf('tom'); // returns 3
```

### La méthode de tableau `reverse()`

Comme son nom l'indique, la méthode `reverse()` inverse les positions des éléments dans le tableau de sorte que le dernier élément passe à la première position et le premier à la dernière.

```
const names = ['tom', 'alex', 'bob'];

names.reverse(); // returns ["bob", "alex", "tom"]
```

La méthode `reverse()` modifie le tableau d'origine.

### La méthode de tableau `sort()`

La méthode `sort()` est probablement l'une des méthodes de tableau les plus souvent utilisées. La méthode `sort()` par défaut convertit les types d'éléments en chaînes de caractères, puis les trie. L'ordre de tri par défaut est croissant. La méthode `sort()` modifie le tableau d'origine.

```
const names = ['tom', 'alex', 'bob'];

names.sort(); // returns ["alex", "bob", "tom"]
```

La méthode `sort()` accepte une fonction de comparaison optionnelle comme argument. Vous pouvez écrire une fonction de comparaison et la passer à la méthode `sort()` pour outrepasser le comportement de tri par défaut.

Prenons maintenant un tableau de nombres et trions-les par ordre croissant et décroissant en utilisant une fonction de comparaison :

```
const numbers = [23, 5, 100, 56, 9, 13, 37, 10, 1]
```

Tout d'abord, nous allons appeler la méthode `sort()` par défaut et voir le résultat :

```
numbers.sort();
```

Maintenant, le tableau trié est \[1, 10, 100, 13, 23, 37, 5, 56, 9\]. Eh bien, ce n'est pas le résultat que nous attendions. Mais cela arrive parce que la méthode `sort()` par défaut convertit les éléments en chaîne de caractères, puis les compare en fonction des valeurs des unités de code `UTF-16`.

Pour résoudre ce problème, écrivons une fonction de comparaison. En voici une pour l'ordre croissant :

```
function ascendingComp(a, b){
  return (a-b);
}
```

Maintenant, passez-la à la méthode `sort()` :

```
numbers.sort(ascendingComp); // retruns [1, 5, 9, 10, 13, 23, 37, 56, 100]

/* 

Nous pourrions aussi coder cela comme ceci :

numbers.sort(function(a, b) {
  return (a-b);
});

Ou, avec une fonction fléchée :

numbers.sort((a, b) => (a-b));

*/
```

Pour l'ordre décroissant, faites ceci :

```
numbers.sort((a, b) => (b-a));
```

Consultez ce dépôt GitHub pour plus d'exemples de tri et de conseils : [https://github.com/atapas/js-array-sorting][3]

### La méthode de tableau `splice()`

La méthode `splice()` vous aide à ajouter, mettre à jour et supprimer des éléments dans un tableau. Cette méthode peut être un peu déroutante au début, mais une fois que vous saurez comment l'utiliser correctement, vous la maîtriserez.

Le but principal de la méthode `splice()` est de supprimer des éléments d'un tableau. Elle renvoie un tableau des éléments supprimés et modifie le tableau d'origine. Mais vous pouvez également l'utiliser pour ajouter et remplacer des éléments.

Pour ajouter un élément en utilisant la méthode `splice()`, nous devons passer la position où nous voulons ajouter, le nombre d'éléments à supprimer à partir de cette position, et l'élément à ajouter.

Dans l'exemple ci-dessous, nous ajoutons un élément `zack` à l'index `1` sans supprimer aucun élément.

```
const names = ['tom', 'alex', 'bob'];

names.splice(1, 0, 'zack');

console.log(names); // ["tom", "zack", "alex", "bob"]
```

Jetez un œil à l'exemple suivant. Ici, nous supprimons un élément à partir de l' `index 2` (le 3ème élément) et ajoutons un nouvel élément, `zack`. La méthode `splice()` renvoie un tableau avec l'élément supprimé, `bob`.

```
const names = ['tom', 'alex', 'bob'];

const deleted = names.splice(2, 1, 'zack');

console.log(deleted); // ["bob"]
console.log(names); // ["tom", "alex", "zack"]
```

Consultez ce fil Twitter pour apprendre comment la méthode `splice()` vous aide à vider un tableau.

> [][4]

## Méthodes de tableau statiques en JavaScript

En JavaScript, les tableaux ont trois méthodes statiques. Nous avons déjà discuté de `Array.isArray()`. Abordons maintenant les deux autres.

### La méthode de tableau `Array.from()`

Prenons un simple extrait de code HTML contenant une div et quelques éléments de liste :

```
<div id="main">
  <ul>
    <ol type="1">
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
      <li>...</li>
    </ol>
  </ul> 
</div>
```

Nous allons maintenant interroger le DOM en utilisant la méthode `getElementsByTagName()`.

```
document.getElementsByTagName('li');
```

Elle renvoie une `HTMLCollection` qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/htmlCollec.png) _HTMLCollection est un objet de type tableau (Array-Like Object)_

C'est donc comme un tableau. Essayons maintenant d'itérer dessus en utilisant `forEach` :

```
document.getElementsByTagName('li').forEach(() => {
 // Faire quelque chose ici..
})
```

Devinez quel est le résultat ? C'est une erreur comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/htmlcolc_error.png) _Erreur lors de l'utilisation de forEach sur l'objet de type tableau_

Mais pourquoi ? Parce que la `HTMLCollection` n'est pas un tableau. C'est un objet de type tableau (`Array-Like`). Vous ne pouvez donc pas itérer dessus en utilisant `forEach`.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/htmlCollec_object.png) _Le proto est Object_

C'est ici que vous devriez utiliser la méthode `Array.from()`. Elle convertit un objet de type tableau en un véritable tableau afin que vous puissiez effectuer toutes les opérations de tableau dessus.

```
const collection = Array.from(document.getElementsByTagName('li'))
```

Ici, `collection` est un tableau :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/collection.png) _Le proto est Array_

### La méthode de tableau `Array.of()`

La méthode `Array.of()` crée un nouveau tableau en utilisant n'importe quel nombre d'éléments de n'importe quel type.

```
Array.of(2, false, 'test', {'name': 'Alex'})
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-49.png) _Sortie de la méthode Array.of()_

## Méthodes d'itération de tableau en JavaScript

Nous allons maintenant découvrir les méthodes d'itération de tableau. Ce sont des méthodes très utiles pour parcourir un tableau et effectuer des calculs, prendre des décisions, filtrer des éléments, et plus encore.

Jusqu'à présent, nous n'avons pas vu d'exemple de tableau d'objets. Dans cette section, nous utiliserons le tableau d'objets suivant pour expliquer et démontrer les méthodes ci-dessous.

Ce tableau contient les informations de certains étudiants inscrits à divers cours payants :

```
let students = [
   {
      'id': 001,
      'f_name': 'Alex',
      'l_name': 'B',
      'gender': 'M',
      'married': false,
      'age': 22,
      'paid': 250,  
      'courses': ['JavaScript', 'React']
   },
   {
      'id': 002,
      'f_name': 'Ibrahim',
      'l_name': 'M',
      'gender': 'M',
      'married': true,
      'age': 32,
      'paid': 150,  
      'courses': ['JavaScript', 'PWA']
   },
   {
      'id': 003,
      'f_name': 'Rubi',
      'l_name': 'S',
      'gender': 'F',
      'married': false,
      'age': 27,
      'paid': 350,  
      'courses': ['Blogging', 'React', 'UX']
   },
   {
      'id': 004,
      'f_name': 'Zack',
      'l_name': 'F',
      'gender': 'M',
      'married': true,
      'age': 36,
      'paid': 250,  
      'courses': ['Git', 'React', 'Branding']
   } 
];
```

Très bien, commençons. Toutes les méthodes d'itération de tableau prennent une fonction comme argument. Vous devez spécifier la logique à itérer et à appliquer dans cette fonction.

### La méthode de tableau `filter()`

La méthode `filter()` crée un nouveau tableau avec tous les éléments qui satisfont à la condition mentionnée dans la fonction. Trouvons l'étudiant qui est une femme. La condition de filtrage doit donc être que le genre soit égal à 'F'.

```
const femaleStudents = students.filter((element, index) => {
  return element.gender === 'F';
})

console.log(femaleStudents);
```

Le résultat est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-50.png)

C'est exact. L'étudiante nommée `Rubi` est la seule femme que nous ayons trouvée jusqu'à présent.

### La méthode de tableau `map()`

La méthode `map()` crée un nouveau tableau en itérant à travers les éléments et en appliquant la logique que nous avons fournie dans la fonction passée en argument. Nous allons créer un nouveau tableau des noms complets de tous les étudiants du tableau `students`.

```

const fullNames = students.map((element, index) => {
  return {'fullName': element['f_name'] + ' ' + element['l_name']}
});

console.log(fullNames);
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-51.png)

Ici, nous voyons un nouveau tableau avec les propriétés `fullName` calculées à partir des propriétés `f_name` et `l_name` de chaque objet étudiant.

### La méthode de tableau `reduce()`

La méthode `reduce()` applique une fonction réductrice sur chacun des éléments du tableau et renvoie une valeur de sortie unique. Nous allons appliquer une fonction réductrice sur le tableau `students` pour calculer le montant total payé par tous les étudiants.

```
const total = students.reduce(
   (accumulator, student, currentIndex, array) => {
      accumulator = accumulator + student.paid;
      return (accumulator);
   }, 
0);

console.log(total); // 1000
```

Dans le code ci-dessus,

-   Nous initialisons l' `accumulator` (accumulateur) à `0`.
-   Nous appliquons la méthode `reduce` sur chacun des objets étudiants. Nous accédons à la propriété `paid` et l'ajoutons à l'accumulateur.
-   Enfin, nous retournons l'accumulateur.

### La méthode de tableau `some()`

La méthode `some()` renvoie une valeur booléenne (true/false) selon qu'au moins un élément du tableau remplit la condition de la fonction. Voyons s'il y a des étudiants de moins de 30 ans.

```
let hasStudentBelow30 = students.some((element, index) => {
  return element.age < 30;
});

console.log(hasStudentBelow30); // true
```

Oui, nous voyons qu'il y a au moins un étudiant de moins de 30 ans.

### La méthode de tableau `find()`

En utilisant la méthode `some()`, nous avons vu qu'il y a un étudiant de moins de 30 ans. Découvrons qui est cet étudiant.

Pour ce faire, nous utiliserons la méthode `find()`. Elle renvoie le premier élément correspondant du tableau qui satisfait à la condition de la fonction.

Les tableaux ont une autre méthode apparentée, `findIndex()`, qui renvoie l'index de l'élément que nous trouvons en utilisant la méthode `find()`. Si aucun élément ne correspond à la condition, la méthode `findIndex()` renvoie `-1`.

Dans l'exemple ci-dessous, nous passons une fonction à la méthode `find()` qui vérifie l'âge de chaque étudiant. Elle renvoie l'étudiant correspondant lorsque la condition est remplie.

```
const student = students.find((element, index) => {
  return element.age < 30;
});

console.log(student);
```

Le résultat est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-52.png)

Comme nous le voyons, c'est Alex qui a 22 ans. Nous l'avons trouvé.

### La méthode de tableau `every()`

La méthode `every()` détecte si chaque élément du tableau satisfait à la condition passée dans la fonction. Vérifions si tous les étudiants se sont inscrits à au moins deux cours.

```
const atLeastTwoCourses = students.every((elements, index) => {
  return elements.courses.length >= 2;
});

console.log(atLeastTwoCourses); // true
```

Comme prévu, nous voyons que le résultat est `true`.

## Méthodes de tableau proposées

Depuis mai 2021, ECMAScript a une [méthode en proposition][5], la méthode `at()`.

### La méthode `at()`

La méthode `at()` proposée vous aiderait à accéder aux éléments d'un tableau en utilisant un numéro d'index négatif. Pour l'instant, ce n'est pas possible. Vous ne pouvez accéder aux éléments qu'à partir du début du tableau en utilisant un numéro d'index positif.

L'accès aux éléments à partir de la fin du tableau est possible en utilisant la valeur de la longueur. Avec l'inclusion de la méthode `at()`, vous seriez en mesure d'accéder aux éléments en utilisant des index positifs et négatifs avec une seule méthode.

```
const junkFoodILove = ['🥖', '🍔', '🍟', '🍕', '🌭', '🥪', '🌮', '🍿'];

junkFoodILove.at(0); // 🥖
junkFoodILove.at(3); // 🍕
junkFoodILove.at(-1); // 🍿
junkFoodILove.at(-5); // 🍕
junkFoodILove.at(-8); // 🥖
junkFoodILove.at(10); // undefined
```

Voici une démonstration rapide :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/demo-3.gif) _Démo de la méthode Javascript Array at()_

Vous pouvez utiliser [ce polyfill][6] pour obtenir la fonctionnalité de la méthode `at()` jusqu'à ce que cette méthode soit ajoutée au langage JavaScript. Veuillez consulter ce dépôt GitHub pour des exemples de la méthode `at()` : [https://github.com/atapas/js-array-at-method][7]

# Avant de terminer...

J'espère que vous avez trouvé cet article instructif et qu'il vous aide à comprendre les tableaux JavaScript plus clairement. Veuillez pratiquer les exemples plusieurs fois pour bien les maîtriser. Vous pouvez trouver tous les [exemples de code dans mon dépôt GitHub][8].

Restons en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)][9]. N'hésitez pas à me suivre.

Vous aimerez peut-être aussi ces articles :

-   [Pourquoi devez-vous connaître les objets de type tableau ?][10]
-   [5 conseils utiles sur la méthode sort des tableaux JavaScript][11]
-   [Façons de vider un tableau en JavaScript et les conséquences][12]
-   [Musclez votre JavaScript avec map, reduce, filter et d'autres itérateurs de tableau][13]
-   [Pourquoi devez-vous connaître la méthode Array at() en JavaScript ?][14]

[1]: https://twitter.com/tapasadhikary/status/1360185996768251904
[2]: https://github.com/atapas/array-fill-color-cards
[3]: https://github.com/atapas/js-array-sorting
[4]: https://twitter.com/tapasadhikary/status/1313112900085579776
[5]: https://tc39.es/proposal-relative-indexing-method/#sec-array-prototype-additions
[6]: https://github.com/es-shims/Array.prototype.at
[7]: https://github.com/atapas/js-array-at-method
[8]: https://github.com/atapas/js-handbook-examples#%EF%B8%8F-list-of-content
[9]: https://twitter.com/tapasadhikary
[10]: https://blog.greenroots.info/why-do-you-need-to-know-about-array-like-objects-ckgsynazh07er06s18ppn32n0
[11]: https://blog.greenroots.info/5-useful-tips-about-the-javascript-array-sort-method-ckfs2cifq00eju9s17dfy3jq8
[12]: https://blog.greenroots.info/ways-to-empty-an-array-in-javascript-and-the-consequences-cjwt45q9d002h2fs1kz5a77a2
[13]: https://blog.greenroots.info/build-your-javascript-muscles-with-map-reduce-filter-and-other-array-iterators-cjyo22miw000xzss1ydfqveib
[14]: https://blog.greenroots.info/why-do-you-need-to-know-about-the-javascript-array-at-method-ckoskkkee0ftmbws1ag0b4udt