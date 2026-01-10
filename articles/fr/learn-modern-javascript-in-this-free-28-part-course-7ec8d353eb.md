---
title: Apprenez ES6 dans ce cours Scrimba gratuit en 28 parties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T16:09:50.000Z'
originalURL: https://freecodecamp.org/news/learn-modern-javascript-in-this-free-28-part-course-7ec8d353eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bBlPwnLZ3hoVAUbxoczzqQ.png
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Apprenez ES6 dans ce cours Scrimba gratuit en 28 parties
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  As a part of our collaboration with freeCodeCamp, their eminent instructor Beau
  Carnes has turned their entire ES6 curriculum into an interactive Scrimba course
  which you can watch today.

  As yo...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/dIB4enxTUgFHbooVsnQOkXnoQLJqvnYlQIpe)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

Dans le cadre de notre collaboration avec freeCodeCamp, leur éminent instructeur [Beau Carnes](https://twitter.com/carnesbeau?lang=en) a transformé l'ensemble du programme ES6 en un cours interactif Scrimba [que vous pouvez regarder dès aujourd'hui.](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

Comme vous le savez peut-être, ES6 est simplement une façon de décrire les nouvelles fonctionnalités de JavaScript qui n'ont pas été pleinement et largement acceptées avant 2017. Aujourd'hui, presque tout JavaScript est écrit en utilisant les fonctionnalités ES6, donc ce cours vous prépare à devenir un développeur JavaScript moderne.

Dans cet article, je vais lister les chapitres et vous donner une ou deux phrases à leur sujet. Ainsi, vous devriez pouvoir juger rapidement si ce cours vous semble intéressant.

Si c'est le cas, assurez-vous de [vous rendre sur Scrimba pour le regarder !](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

### 1. Introduction

Dans la première capture d'écran, Beau vous donne une rapide introduction au cours et à lui-même et parle un peu d'ES6. Il vous montre également comment vous pouvez trouver le programme si vous souhaitez le parcourir sur [le site de freeCodeCamp](https://freecodecamp.org) également.

### 2. Explorer les différences entre les mots-clés var et let

Le premier sujet est les variables. Dans ES5, nous ne pouvions déclarer des variables qu'avec `var`, mais à partir d'ES6, nous pouvons maintenant utiliser `let` et `const`.

Comment `let` et `var` sont-ils différents ? `let` ne vous permet pas de déclarer une variable deux fois.

```js
var catName = "Quincy";  
var catName = "Beau";  
// Fonctionne bien !

let dogName = "Quincy";  
let dogName = "Beau";  
// Erreur : TypeError: unknown: Déclaration en double "dogName"

```

### 3. Comparer les portées des mots-clés var et let

Une autre différence majeure entre `var` et `let` est leur portée ([guide de freeCodeCamp sur la portée](https://guide.freecodecamp.org/javascript/scopes/)).

Lorsque vous déclarez une variable avec `var`, elle est déclarée globalement ou localement si elle est à l'intérieur d'une fonction.

Lorsque vous la déclarez avec `let`, elle serait limitée à une instruction ou une portée d'expression de bloc.

Beau vous montre deux exemples.

![Cliquez sur une image pour accéder au Scrimba cast](https://cdn-media-1.freecodecamp.org/images/1*laCp2HN4_bQD3BBf0QLkDw.png)

![Cliquez sur une image pour accéder au Scrimba cast](https://cdn-media-1.freecodecamp.org/images/1*2qchOXyzuS8lMoVgYuRd2Q.png)
_[Cliquez ici pour accéder au Scrimba cast](https://scrimba.com/p/p7v3gCd/cLez8TE?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

### 4. Déclarer une variable en lecture seule avec le mot-clé const

`const` est un moyen d'assigner une variable en lecture seule qui ne peut pas être réassignée.

```js
const fcc = "freeCodeCamp";  
const sentence = fcc + " est cool !";  
sentence = fcc + " est incroyable !";  
// Erreur : SyntaxError: unknown: "sentence" est en lecture seule

```

### 5. Muter un tableau déclaré avec const

Vous devez être prudent avec `const`, car il est toujours possible de muter les tableaux assignés avec.

```js
const myArray = [5, 7, 2];

myArray[0] = 2;  
myArray[1] = 7;  
myArray[2] = 5;

console.log(myArray);   
// [2, 7, 5]

```

Même chose pour les objets.

### 6. Empêcher la mutation des objets

Afin d'éviter la mutation des objets et des tableaux, vous pouvez utiliser `Object.freeze()` :

```js
const MATH_CONSTANTS = {  
  PI: 3.14  
};

Object.freeze(MATH_CONSTANTS);  
MATH_CONSTANTS.PI = 99;

// TypeError: Impossible d'assigner à la propriété en lecture seule 'PI' de l'objet '#<Object>'

```

Si vous souhaitez geler les tableaux, vous pouvez également utiliser `Object.freeze()` et passer votre tableau, mais cela pourrait ne pas fonctionner sur certains anciens navigateurs.

### 7. Utiliser les fonctions fléchées pour écrire des fonctions anonymes concises

ES6 introduit également une manière plus courte d'écrire des fonctions anonymes.

```js
// Fonction anonyme ES5  
var magic = function() {  
  return new Date();  
};

// Une fonction fléchée ES6 plus courte  
var magic = () => {  
  return new Date();  
};

// Et nous pouvons la raccourcir encore plus  
var magic = () => new Date();

```

### 8. Écrire des fonctions fléchées avec des paramètres

Passer des paramètres aux fonctions fléchées est également facile.

```js
var myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [3, 4, 5]));  
// [1, 2, 3, 4, 5]

```

### 9. Écrire des fonctions fléchées d'ordre supérieur

Les fonctions fléchées brillent lorsqu'elles sont utilisées avec des fonctions d'ordre supérieur, comme `map()`, `filter()`, `reduce()`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-4.png)
_[Cliquez ici pour accéder au Scrimba cast](https://scrimba.com/p/p7v3gCd/ck4L6T9?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

### 10. Définir des paramètres par défaut pour vos fonctions

Si certains de nos paramètres de fonction peuvent être définis à une valeur par défaut, voici comment vous pouvez le faire en ES6 :

```js
// Si le paramètre value n'est pas passé, il sera assigné à 1.   
function increment(number, value = 1) {  
  return number + value;  
};

console.log(increment(5, 2)); // 7  
console.log(increment(5)); // 6

```

### 11. Utiliser l'opérateur Rest avec les paramètres de fonction

L'opérateur Rest vous permet de créer une fonction qui prend un nombre variable d'arguments.

```js
function sum(...args) {  
  return args.reduce((a, b) => a + b);  
};

console.log(sum(1, 2, 3)); // 6  
console.log(sum(1, 2, 3, 4)); // 10

```

### 12. Utiliser l'opérateur Spread pour évaluer les tableaux en place

L'opérateur _spread_ ressemble exactement à l'opérateur _rest_ et ressemble à ceci : `...`, mais il développe un tableau déjà existant en parties individuelles.

```js
const monthsOriginal = ['JAN', 'FEB', 'MAR'];

let monthsNew = [...monthsOriginal];  
monthsOriginal[0] = 'potato';

console.log(monthsOriginal); // ['potato', 'FEB', 'MAR']  
console.log(monthsNew); // ['JAN', 'FEB', 'MAR']

```

### 13. Utiliser l'assignation par décomposition pour assigner des variables à partir d'objets

La décomposition est une syntaxe spéciale pour assigner proprement des valeurs prises directement d'un objet à une nouvelle variable.

```js
// Objet que nous voulons décomposer  
var voxel = {x: 3.6, y: 7.4, z: 6.54 };

// C'est comment nous le ferions en ES5  
var a = voxel.x; // a = 3.6  
var b = voxel.y; // b = 7.4  
var c = voxel.z; // c = 6.54

// Une manière plus courte en ES6  
const { x : a, y : b, z : c } = voxel;   
// a = 3.6, b = 7.4, c = 6.54

```

### 14. Utiliser l'assignation par décomposition pour assigner des variables à partir d'objets imbriqués

Vous pouvez utiliser la décomposition pour obtenir des valeurs même à partir d'objets imbriqués :

```js
const LOCAL_FORECAST = {  
  today: { min: 72, max: 83 },  
  tomorrow: { min: 73.3, max: 84.6 }  
};

function getMaxOfTmrw(forecast) {  
  "use strict";

// nous obtenons l'objet tomorrow à partir de la prévision  
  // et ensuite nous créons maxOfTomorrow avec la valeur de max  
  const { tomorrow : { max : maxOfTomorrow }} = forecast;

return maxOfTomorrow;  
}  
console.log(getMaxOfTmrw(LOCAL_FORECAST));  
// 84.6

```

### 15. Utiliser l'assignation par décomposition pour assigner des variables à partir de tableaux

Vous vous demandez si la décomposition peut être utilisée avec des tableaux ? Absolument ! Il y a une différence importante cependant. Lors de la décomposition de tableaux, vous ne pouvez pas spécifier une valeur que vous souhaitez aller dans une variable spécifique et elles vont toutes dans l'ordre.

```js
const [z, x, , y] = [1, 2, 3, 4, 5, 6];

// z = 1;  
// x = 2;   
// Passer 3  
// y = 4;

```

### 16. Utiliser l'assignation par décomposition avec l'opérateur Rest pour réassigner des éléments de tableau

Combinons maintenant l'opérateur rest avec la décomposition pour supercharger nos compétences ES6.

```js
const list = [1,2,3,4,5,6,7,8,9,10];

// Créer a et b à partir des deux premiers membres  
// Mettre le reste dans une variable appelée newList  
const [ a, b, ...newList] = list;

// a = 1;  
// b = 2;  
// newList = [3,4,5,6,7,8,9,10];

```

### 17. Utiliser l'assignation par décomposition pour passer un objet en tant que paramètres d'une fonction

Nous pouvons créer des fonctions plus lisibles.

```js
const stats = {  
  max: 56.78,  
  standard_deviation: 4.34,  
  median: 34.54,  
  mode: 23.87,  
  min: -0.75,  
  average: 35.85  
};

// ES5  
function half(stats) {  
  return (stats.max + stats.min) / 2.0;  
};

// ES6 utilisant la décomposition  
function half({max, min}) {  
  return (max + min) / 2.0;  
};

console.log(half(stats));   
// 28.015

```

### 18. Créer des chaînes de caractères en utilisant les littéraux de gabarit

Les littéraux de gabarit nous aident à créer des chaînes de caractères complexes. Ils utilisent une syntaxe spéciale de ```` et `${}` où vous pouvez combiner du texte de gabarit avec des variables ensemble. Par exemple ``Bonjour, mon nom est ${myNameVariable} et j'adore ES6 !``

```js
const person = {  
  name: "Zodiac Hasbro",  
  age: 56  
};

// Littéral de gabarit avec multi-ligne et interpolation de chaîne

const greeting = `Bonjour, mon nom est ${person.name}!   
J'ai ${person.age} ans.`;

console.log(greeting);

```

### 19. Écrire des déclarations d'objets littéraux concises en utilisant des champs simples

ES6 a ajouté la prise en charge de la définition facile des littéraux d'objets.

```js
// retourne un nouvel objet à partir des paramètres passés  
const createPerson = (name, age, gender) => ({  
  name: name,  
  age: age,   
  gender: gender  
});

console.log(createPerson("Zodiac Hasbro", 56, "male"));

// { name: "Zodiac Hasbro", age: 56, gender: "male" }

```

### 20. Écrire des fonctions déclaratives concises avec ES6

Les objets en JavaScript peuvent contenir des fonctions.

```js

const ES5_Bicycle = {  
  gear: 2,  
  setGear: function(newGear) {  
    "use strict";  
    this.gear = newGear;  
  }  
};

const ES6_Bicycle = {  
  gear: 2,  
  setGear(newGear) {  
    "use strict";  
    this.gear = newGear;  
  }  
};

ES6_Bicycle.setGear(3);

console.log(ES6Bicycle.gear); // 3

```

### 21. Utiliser la syntaxe de classe pour définir une fonction constructeur

ES6 fournit une syntaxe pour créer des objets en utilisant le mot-clé `class` :

```js

var ES5_SpaceShuttle = function(targetPlanet){  
  this.targetPlanet = targetPlanet;  
}

class ES6_SpaceShuttle {  
  constructor(targetPlanet){  
    this.targetPlanet = targetPlanet;  
  }  
}

var zeus = new ES6_SpaceShuttle('Jupiter');

console.log(zeus.targetPlanet); // 'Jupiter'

```

### 22. Utiliser les getters et setters pour contrôler l'accès à un objet

Avec un objet, vous souhaitez souvent obtenir les valeurs des propriétés et définir une valeur de propriété dans un objet. Ceux-ci sont appelés _getters_ et _setters_. Ils existent pour cacher un certain code sous-jacent, car il ne devrait pas être une préoccupation pour quiconque utilise la classe.

```js

class Thermostat {  
  // Nous créons Thermostat en utilisant la température en Fahrenheit.  
  constructor(temp) {  
    // _temp est une variable privée qui n'est pas destinée   
    // à être accessible depuis l'extérieur de la classe.  
    this._temp = 5/9 * (temp - 32);  
  }

// getter pour _temp  
  get temperature(){  
    return this._temp;  
  }

// setter pour _temp  
  // nous pouvons mettre à jour la température en utilisant Celsius.  
  set temperature(updatedTemp){  
    this._temp = updatedTemp;  
  }  
}

// Créer Thermostat en utilisant la valeur Fahrenheit  
const thermos = new Thermostat(76);  
let temp = thermos.temperature;

// Nous pouvons mettre à jour la valeur en utilisant Celsius  
thermos.temperature = 26;  
temp = thermos.temperature;  
console.log(temp) // 26

```

### 23. Comprendre les différences entre import et require

Dans le passé, nous ne pouvions utiliser que `require` pour importer des fonctions et du code depuis d'autres fichiers. Dans ES6, nous pouvons utiliser `import` :

```js

// dans le fichier string_function.js  
export const capitalizeString = str => str.toUpperCase()

// dans le fichier index.js  
import { capitalizeString } from "./string_function"

const cap = capitalizeString("hello!");

console.log(cap); // "HELLO!"

```

### 24. Utiliser export pour réutiliser un bloc de code

Vous exporteriez normalement des fonctions et des variables dans certains fichiers afin de pouvoir les importer dans d'autres fichiers et maintenant nous pouvons réutiliser le code !

```js

const capitalizeString = (string) => {  
  return string.charAt(0).toUpperCase() + string.slice(1);  
}

// Export nommé  
export { capitalizeString };

// Export nommé sur la même ligne  
export const foo = "bar";  
export const bar = "foo";

```

### 25. Utiliser * pour importer tout depuis un fichier

Si un fichier exporte plusieurs choses différentes, vous pouvez soit les importer individuellement, soit utiliser `*` pour importer tout depuis un fichier.

Voici comment vous importeriez toutes les variables depuis le fichier de l'exercice précédent.

```js

import * as capitalizeStrings from "capitalize_strings";

```

### 26. Créer une exportation de secours avec export default

Nous avons examiné les exportations nommées dans les chapitres précédents et parfois il peut y avoir une seule fonction ou une variable que nous voulons exporter depuis un fichier — `export default`, souvent utilisé comme exportation de secours également.

```js

// Dans le fichier math_functions.js

export default function subtract(x,y) {  
  return x - y;  
}

```

### 27. Importer une exportation par défaut

Si vous souhaitez importer la fonction `export default` de l'exercice précédent, voici comment vous pourriez le faire.

Notez l'absence de `{}` autour de la fonction `subtract`. Les exportations par défaut n'en ont pas besoin.

```js

// Dans le fichier index.js  
import subtract from "math_functions";

subtract(7,4); // retourne 3;

```

### 28. Conclusion sur JavaScript ES6

Si vous êtes arrivé jusqu'ici : félicitations ! La plupart des gens qui commencent des cours ne les terminent jamais, donc vous pouvez être fier de vous.

Si vous cherchez votre prochain défi, vous devriez consulter le cours de Beau sur [Regex ici !](https://scrimba.com/g/gregularexpressions?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*wkctXSR70cUrFBAyiqK1Qw.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gregularexpressions?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

Bonne chance ! :)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_