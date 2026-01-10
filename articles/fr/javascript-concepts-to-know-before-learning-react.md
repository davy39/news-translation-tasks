---
title: Concepts JavaScript à connaître avant d'apprendre React
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2023-04-20T00:30:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-to-know-before-learning-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Seven-JavaScript-Concepts-to-master-before-React--2-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Concepts JavaScript à connaître avant d'apprendre React
seo_desc: 'A lot of web developers use React as their go-to library for building UI
  components for their websites. React is one of the most popular frameworks for web
  development and it is written entirely in JavaScript.

  Since React was written in JavaScript, i...'
---

Beaucoup de développeurs web utilisent React comme leur bibliothèque de prédilection pour construire des composants d'interface utilisateur pour leurs sites web. React est l'un des frameworks les plus populaires pour le développement web et il est entièrement écrit en JavaScript.

Puisque React a été écrit en JavaScript, il utilise beaucoup de concepts JavaScript qui ont été introduits avant et dans la version ES6 de JavaScript. Il est important pour quiconque souhaite apprendre React de comprendre ces concepts.

Dans cet article, je vais expliquer avec des exemples détaillés les sept concepts JavaScript les plus importants qu'un développeur doit connaître avant d'apprendre React.

Avant de commencer à lire cet article, vérifiez les prérequis.

## Prérequis

Pour suivre cet article, vous devez avoir quelques connaissances de base en :

* JavaScript, et

* La console du navigateur (car c'est là que vous exécuterez votre code)

## Comment utiliser les instructions If et les opérateurs ternaires en JavaScript

En JavaScript, vous utilisez des instructions conditionnelles pour spécifier qu'un bloc de code doit être exécuté si certaines conditions sont vraies.

Les instructions conditionnelles sont utiles dans le rendu conditionnel des composants d'interface utilisateur dans React. Elles vous permettent de rendre votre interface utilisateur en fonction de certaines conditions.

### Instruction If ... Else

La première chose à savoir concernant les instructions conditionnelles est comment utiliser l'instruction if ... else.

Vous pouvez écrire du code qui ajoutera deux nombres si le second est supérieur au premier, et les soustraira si ce n'est pas le cas. Voici à quoi cela ressemblerait en utilisant une instruction if ... else :

```js
if (a < b) {            
    let output = a + b;        
} else {            
    let output = a - b;        
}
```

Dans une instruction if ... else, vous pouvez utiliser un else ... if au lieu d'écrire plusieurs if.

Le else if permet d'écrire plusieurs conditions ensemble. Il spécifie une nouvelle condition à tester, si la première condition est fausse.

```js
if (a < b)  {        
    let output = a + b;    
} else if (a > b) {
    let output = a - b;    
} else {        
    let output = a * b;    
}
```

Le code ci-dessus ajoute une instruction else if à l'exemple précédent. Le else if teste la condition a est supérieur à b, si la condition précédente est fausse.

### Opérateur Ternaire

Un opérateur ternaire est une manière plus concise d'écrire une instruction if ... else.

Il prend trois opérandes : une condition suivie d'un point d'interrogation (`?`), puis une expression à exécuter si la condition est vraie suivie de deux points (`:`), et enfin l'expression à exécuter si la condition est fausse.

Si vous souhaitez réécrire l'exemple if ... else ci-dessus en utilisant un opérateur ternaire, cela devrait ressembler à ceci :

```js
(a < b) ? a + b : a - b;
```

Le (a < b) est la condition, le ? évalue la condition, et si elle est vraie, il retourne a + b, tandis que si elle est fausse, il retourne a - b.

Cela fait cinq lignes de code de l'exemple précédent écrites en une seule ligne. Mais, si vous souhaitez inclure else if dans votre code d'opérateur ternaire, vous devrez écrire ceci :

```js
(a < b) ? a + b : (a > b) ? a - b : a * b;
```

Dans le code ci-dessus, le ? évalue la condition (a < b) et si elle est vraie, il retourne a + b. Mais, si elle est fausse, il évalue la deuxième condition (a > b) et si celle-ci est vraie, il retourne a - b, sinon il retourne a * b.

Une seule ligne aussi. Mais, pour éviter que cela ne devienne trop encombrant, vous pouvez le diviser en plusieurs lignes. Cela rendra votre code plus lisible.

Dans l'exemple ci-dessous, vous verrez comment vous pouvez diviser votre code en faisant en sorte que la condition et l'instruction de retour soient sur la même ligne.

```js
(a < b) ? a + b         
: (a > b) ? a - b         
: a * b;
```

## Comment fonctionne la destructuration en JavaScript

La destructuration en JavaScript consiste à déballer des valeurs de tableaux ou des propriétés d'objets et à les assigner à une variable.

Cela facilite l'extraction de données de tableaux et d'objets, et c'est applicable dans des concepts React comme useState.

### Destructuration de tableau

La destructuration de tableau est utilisée pour extraire des données d'un tableau.

Dans l'exemple ci-dessous, nous destructurons le tableau `newArray` de deux manières. Une manière consiste à déclarer un tableau contenant les variables que nous voulons assigner à nos valeurs de tableau et à l'assigner à la variable newArray. L'autre manière consiste à assigner le tableau de variables au tableau contenant les valeurs que nous voulons destructurer.

```js
let newArray = ["Musab", "I", "Handsome"];    
let [noun, pronoun, adjective] = newArray; 

// Ce qui précède peut également être réécrit comme ceci :  

let [noun, pronoun, adjective] = ["Musab", "I", "Handsome"];    

console.log(noun);    
console.log(pronoun);
```

Vous pouvez sauter une ou plusieurs valeurs en mettant des virgules à leur place.

```js
let newArray = [a, b, c, d, e];

let [firstLetter, , , ,lastLetter] = [a, b, c, d, e];
```

### Destructuration d'objet

La destructuration d'objet est similaire à la destructuration de tableau, mais dans les objets, nous ne destructurons que les clés/propriétés.

Dans l'exemple ci-dessous, l'objet "personObject" a été destructuré en déclarant un objet contenant les propriétés de personObject et en l'assignant à personObject.

```js
let personObject = {        
    name: "David",        
    age: 18,        
    height: "6ft 5in",        
    gender: "male",    
}    

let {name, age, height, gender} = personObject   
console.log(name, age, height, gender);
```

Maintenant, vous pouvez accéder aux valeurs de chacune des clés sans appeler l'objet.

Vous pouvez également assigner chacune des clés destructurées à de nouvelles variables.

```js
let personObject = {        
    name: "David",        
    age: 18,        
    height: "6ft 5in",        
    gender: "male",    
}    

let {name: personName, age: personAge, height: personHeight, gender: personGender} = personObject;

console.log(personName, personAge, personHeight, personGender);
```

## Comment utiliser les littéraux de gabarit en JavaScript

Les littéraux de gabarit sont enfermés dans des backticks tout comme les chaînes de caractères sont enfermées dans des guillemets. Ils vous permettent de stocker des chaînes de caractères multilignes et également d'interpoler des chaînes de caractères avec des expressions intégrées.

L'exemple ci-dessous montre un littéral de gabarit de base.

```js
let basic = `I write codes`
```

Vous pouvez écrire un littéral de gabarit qui stocke des chaînes de caractères multilignes comme ceci :

```js
let multiLine = `I write codes                     
		I debug codes`;
```

Vous pouvez utiliser le signe dollar et les accolades pour intégrer des expressions dans les littéraux de gabarit. Dans l'exemple ci-dessous, la fonction myName est intégrée dans la variable display avec un littéral de gabarit.

```js
function myName(Musab, Habeeb) {        
    alert("Musab Habeeb");    
}    

let display = `This displays my name ${myName()}`
```

## Comment utiliser les objets en JavaScript

Un objet vous permet de stocker des collections de données. Les données sont stockées dans une paire d'accolades dans un format clé-valeur.

Dans l'exemple ci-dessous, nous créons un objet nommé "myObject" et nous lui donnons trois clés avec leurs valeurs correspondantes.

```js
let myObject = {        
    name: Musab,        
    number: 12,        
    developer: [true, "David", 1]    
}
```

Vous pouvez accéder aux valeurs qui appartiennent à chaque clé dans un objet de deux manières :

* en utilisant la notation par point (c'est la plus couramment utilisée) ou

* en utilisant la notation par crochets

Dans l'exemple ci-dessous, nous accédons à la propriété name en utilisant la notation par crochets et à la propriété number en utilisant la notation par point.

```js
let myObject = {        
    name: "Musab",        
    number: 12,        
    developer: [true, "David", 1]    
}

console.log(myObject["name"]);
console.log(myObject.number);
```

Les clés d'objet doivent être sous forme de chaîne de caractères. Si ce n'est pas le cas, elles seront inaccessibles en utilisant la notation par point.

Dans l'exemple ci-dessous, en accédant à la propriété 3, vous obtiendrez une erreur de syntaxe.

```js
let numbers = {
    one: David,
    two: George,
    3: Peter
}

console.log(numbers.two);
console.log(numbers.3);
```

Vous devez toujours mettre une virgule à la fin de chaque valeur dans un objet sauf la dernière valeur de l'objet.

## Comment utiliser les tableaux et les méthodes de tableau en JavaScript

Les tableaux sont des types spéciaux d'objets qui stockent des données sous une forme ordonnée. Les méthodes de tableau sont des fonctions intégrées qui peuvent être appelées sur un tableau pour faire quelque chose sur ou avec le tableau.

Il existe de nombreuses méthodes de tableau, mais celles que vous utiliserez le plus dans React sont les méthodes map, filter et reduce.

### Méthode Map

Cette méthode itère à travers les éléments d'un tableau et appelle une fonction sur chaque élément du tableau. Cela retourne un nouveau tableau qui contient le résultat de chaque appel de fonction.

```js
let fruits = ["pawpaw", "orange", "banana"];   

let mappedFruits = fruits.map(item => item + "s");    

console.log(mappedFruits); // ["pawpaws", "oranges", "bananas"]
```

### Méthode Filter

Cette méthode retourne tous les éléments d'un tableau qui correspondent à une condition spécifique.

```js
let fruits = ["pawpaw", "orange", "banana", "grape"];
    
let filteredFruits = fruits.filter(fruit => fruit.length > 5);

console.log(filteredFruits);  // ["pawpaw", "orange", "banana"]
```

### Méthode Reduce

La méthode reduce itère sur tous les éléments d'un tableau et effectue une action à chaque itération. Le résultat de cette action est reporté à l'itération suivante pour être utilisé dans l'action suivante jusqu'à l'itération finale. Ensuite, le résultat final sera retourné.

Elle prend deux arguments, qui sont :

* une fonction et,

* un argument optionnel qui désigne la valeur à partir de laquelle la fonction commencera.

```js
let evenNumbers = [2, 4, 6, 8, 10]; 
    
evenNumbers.reduce((sum, current) => sum += current, 0);
```

## Comment utiliser les fonctions et les fonctions fléchées en JavaScript

### Fonctions

Une fonction est un bloc de code qui effectue une tâche particulière. Une fonction prend un argument, effectue une tâche en utilisant l'argument et retourne un résultat.

Les fonctions sont utilisées pour créer des composants fonctionnels dans React.

Pour déclarer une fonction, vous utiliserez le mot-clé "function" et le nom de la fonction comme ceci :

```js
function plusFour(a)  {        
    return a + 4;    
}
```

La fonction dans le code ci-dessus est nommée "plusFour" qui prend un argument "a", ajoute quatre à "a" et retourne le résultat.

Pour exécuter une fonction, vous appellerez la fonction en écrivant le nom de la fonction avec des parenthèses.

```js
// Nous allons appeler la fonction plusFour dans l'exemple précédent    
    
plusFour();
```

### Fonctions fléchées

Les fonctions fléchées sont une alternative pour écrire des fonctions. Elles sont plus compactes et contiennent également des limitations délibérées. Vous pouvez réécrire la fonction plusFour ci-dessus comme une fonction fléchée comme ceci :

```js
let plusFour = (a) => {        
    return a + 4;    
}
```

Puisque l'instruction return est juste une ligne, nous pouvons faire en sorte que la fonction fléchée soit sur une seule ligne :

```js
let plusFour = (a) => a + 4;
```

Les fonctions fléchées ne peuvent pas être utilisées comme méthodes, générateurs ou constructeurs tandis qu'une fonction régulière peut.

## Modules ES

Avant 2015, les variables JavaScript, tableaux, objets et fonctions créés dans un fichier ne pouvaient être accessibles que dans ce fichier.

Mais, avec l'introduction d'ES6 en 2015, les modules sont arrivés. Les modules vous permettent de réaliser des objets, tableaux, fonctions, etc., dans un fichier et de les utiliser dans un autre fichier.

Cela vous aide à maintenir la taille de votre fichier tandis que votre application continue de grandir.

Les modules sont ce qui fait fonctionner React comme un framework d'application monopage. Tous les autres fichiers sont sous forme de composants et sont importés quand et où ils sont nécessaires.

Il y a deux mots-clés que nous utilisons lorsque nous travaillons avec des modules :

* le mot-clé export

* le mot-clé import

Le mot-clé export vous permet de rendre le contenu du module disponible pour tous les autres fichiers JavaScript, tandis que le mot-clé import vous permet d'importer du contenu disponible d'un fichier JavaScript dans un autre fichier JavaScript.

Dans l'exemple ci-dessous, la fonction cook est exportée de son fichier.

```js
// nom du fichier : cook.js

function cook(ingredients, water, heat) {        
    let food = ingredients + water + heat;        
    return food;     
}    

export default cook;
```

Ensuite, dans l'exemple ci-dessous, la fonction cook est importée dans le fichier kitchen.js et appelée.

```js
// nom du fichier : kitchen.js

import cook from './cook';    
cook();
```

## Conclusion

Ces sept concepts JavaScript sont les plus importants à connaître si vous essayez d'apprendre React.

En apprenant ces concepts, il vous sera plus facile d'apprendre React car vous commencerez à voir leurs applications dans votre code React.

Vous devriez lire plus en profondeur sur ces concepts et également essayer de formuler des exemples de code les impliquant afin de mieux les comprendre.

Continuez à apprendre et continuez à vous améliorer.