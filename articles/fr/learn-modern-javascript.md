---
title: JavaScript Moderne – Imports, Exports, Let, Const et Promesses en ES6+
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-12-07T22:47:10.000Z'
originalURL: https://freecodecamp.org/news/learn-modern-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fcb4bbce6787e098393a6fd.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: Web Development
  slug: web-development
seo_title: JavaScript Moderne – Imports, Exports, Let, Const et Promesses en ES6+
seo_desc: 'Over the past few years, there have been many updates to the JavaScript
  language. And these updates are very useful if you want to improve your coding.

  ​Keeping abreast of the newest developments in the language is really important.
  It can help you g...'
---

Au cours des dernières années, de nombreuses mises à jour ont été apportées au langage JavaScript. Et ces mises à jour sont très utiles si vous souhaitez améliorer votre codage.

💡 Rester à jour des derniers développements du langage est vraiment important. Cela peut vous aider à obtenir un emploi mieux rémunéré, à rester à jour avec les dernières tendances, à améliorer la qualité de votre code et à exceller dans votre travail actuel.

Et vous devez absolument connaître les dernières fonctionnalités si vous essayez d'apprendre une bibliothèque JavaScript comme React ou un framework comme Angular ou Vue.

Récemment, de nombreuses additions utiles ont été apportées à JavaScript comme l'**opérateur de coalescence nulle**, le **chaînage optionnel**, les **Promesses**, **async/await**, la **destructuration ES6**, et bien plus encore.

Aujourd'hui, nous allons donc examiner certains de ces concepts que tout développeur JavaScript devrait connaître.

Commençons et plongeons dans les choses que vous devez savoir sur JS.

## Let et const en JavaScript

Avant ES6, JavaScript utilisait le mot-clé `var` qui n'utilisait que la portée de fonction et globale. Il n'y avait pas de portée au niveau du bloc.

Avec l'ajout de `let` et `const`, JavaScript a ajouté la portée de bloc.

### Comment utiliser let en JavaScript

Lorsque nous déclarons une variable en utilisant le mot-clé `let`, nous pouvons **assigner** une nouvelle valeur à cette variable plus tard, mais nous ne pouvons pas la **re-déclarer** avec le même nom.

```js
// Code ES5
var value = 10;
console.log(value); // 10

var value = "hello";
console.log(value); // hello

var value = 30;
console.log(value); // 30

```

Comme vous pouvez le voir ci-dessus, nous avons re-déclaré la variable `value` en utilisant le mot-clé `var` plusieurs fois.

Avant ES6, nous pouvions re-déclarer une variable qui avait déjà été déclarée auparavant si elle n'était pas utilisée de manière significative et causait plutôt de la confusion.

Mais que se passe-t-il si nous avions déjà une variable déclarée avec le même nom ailleurs et que nous la re-déclarions sans nous en rendre compte ? Alors nous pourrions écraser la valeur de la variable, causant des problèmes difficiles à déboguer.

Donc, lorsque vous utilisez le mot-clé `let`, vous obtiendrez une erreur lorsque vous essayez de re-déclarer la variable avec le même nom – ce qui est une bonne chose.

```js
// Code ES6
let value = 10;
console.log(value); // 10

let value = "hello"; // Uncaught SyntaxError: Identifier 'value' has already been declared

```

Mais le code suivant est valide :

```js
// Code ES6
let value = 10;
console.log(value); // 10

value = "hello";
console.log(value); // hello

```

Nous n'obtenons pas d'erreur dans le code ci-dessus car nous **réassignons** une nouvelle valeur à la variable `value`. Mais nous ne **re-déclarons** pas `value` à nouveau.

Maintenant, regardez le code ci-dessous :

```js
// Code ES5
var isValid = true;
if(isValid) {
  var number = 10;
  console.log('inside:', number); // inside: 10
}
console.log('outside:', number); // outside: 10

```

Comme vous pouvez le voir dans ce code, lorsque nous déclarons une variable avec le mot-clé `var`, elle est disponible en dehors du bloc `if` également.

Maintenant, regardez le code ci-dessous :

```js
// Code ES6
let isValid = true;
if(isValid) {
  let number = 10;
  console.log('inside:', number); // inside: 10
}

console.log('outside:', number); // Uncaught ReferenceError: number is not defined

```

Comme vous pouvez le voir, la variable `number` lorsqu'elle est déclarée en utilisant le mot-clé `let` n'est accessible qu'à l'intérieur du bloc `if`. En dehors du bloc, elle n'est pas disponible, donc nous avons obtenu une erreur de référence lorsque nous avons essayé d'y accéder en dehors du bloc `if`.

Mais si une variable `number` existe en dehors du bloc `if`, alors cela fonctionnera comme montré ci-dessous :

```js
// Code ES6
let isValid = true;
let number = 20;

if(isValid) {
  let number = 10;
  console.log('inside:', number); // inside: 10
}

console.log('outside:', number); // outside: 20

```

Ici, nous avons deux variables `number` dans une portée séparée. Donc en dehors du bloc `if`, la valeur de `number` sera 20.

Regardez le code ci-dessous :

```js
// Code ES5
for(var i = 0; i < 10; i++){
 console.log(i);
}
console.log('outside:', i); // 10

```

Lorsque nous utilisons le mot-clé `var`, `i` est disponible même en dehors de la boucle `for`.

```js
// Code ES6
for(let i = 0; i < 10; i++){
 console.log(i);
}

console.log('outside:', i); // Uncaught ReferenceError: i is not defined

```

Mais lorsque nous utilisons le mot-clé `let`, il n'est pas disponible en dehors de la boucle.

Donc, comme vous pouvez le voir à partir des exemples de code ci-dessus, l'utilisation de `let` rend la variable disponible uniquement à l'intérieur de ce bloc et elle n'est pas accessible en dehors du bloc.

Nous pouvons également créer un bloc par une paire d'accolades comme ceci :

```js
let i = 10;
{
 let i = 20;
 console.log('inside:', i); // inside: 20
 i = 30;
 console.log('i again:', i); // i again: 30
}

console.log('outside:', i); // outside: 10

```

Si vous vous souvenez, j'ai dit que nous ne pouvons pas re-déclarer une variable basée sur `let` dans le même bloc, mais nous pouvons la re-déclarer dans un autre bloc. Comme vous pouvez le voir dans le code ci-dessus, nous avons re-déclaré `i` et assigné une nouvelle valeur de `20` à l'intérieur du bloc. Une fois déclarée, cette valeur de variable sera disponible uniquement dans ce bloc.

En dehors du bloc, lorsque nous avons imprimé cette variable, nous avons obtenu `10` au lieu de la valeur précédemment assignée de `30` car en dehors du bloc, la variable `i` intérieure n'existe pas.

Si nous n'avons pas la variable `i` déclarée à l'extérieur, alors nous obtiendrons une erreur comme vous pouvez le voir dans le code ci-dessous :

```js
{
 let i = 20;
 console.log('inside:', i); // inside: 20
 i = 30;
 console.log('i again:', i); // i again: 30
}

console.log('outside:', i); // Uncaught ReferenceError: i is not defined

```

### Comment utiliser const en JavaScript

Le mot-clé `const` fonctionne exactement de la même manière que le mot-clé `let` dans sa fonctionnalité de portée de bloc. Donc, voyons comment ils diffèrent l'un de l'autre.

Lorsque nous déclarons une variable comme `const`, elle est considérée comme une variable constante dont la valeur ne changera jamais.

Dans le cas de `let`, nous sommes capables d'assigner une nouvelle valeur à cette variable plus tard comme ceci :

```js
let number = 10;
number = 20;

console.log(number); // 20

```

Mais nous ne pouvons pas faire cela dans le cas de `const` :

```js
const number = 10;
number = 20; // Uncaught TypeError: Assignment to constant variable.

```

Nous ne pouvons même pas **re-déclarer** une variable `const`.

```js
const number = 20;
console.log(number); // 20

const number = 10; // Uncaught SyntaxError: Identifier 'number' has already been declared

```

Maintenant, regardez le code ci-dessous :

```js
const arr = [1, 2, 3, 4];

arr.push(5);

console.log(arr); // [1, 2, 3, 4, 5]

```

Nous avons dit que la variable `const` est constante et que sa valeur ne changera jamais – mais nous avons changé le tableau constant ci-dessus. Alors, comment cela a-t-il du sens ?

> Note : Les tableaux sont des types de référence et non des types primitifs en JavaScript

Donc, ce qui est réellement stocké dans `arr` n'est pas le tableau réel mais seulement la référence (adresse) de l'emplacement mémoire où le tableau réel est stocké.

Donc, en faisant `arr.push(5);` nous ne changeons pas réellement la référence où `arr` pointe, mais nous changeons les valeurs stockées à cette référence.

Il en va de même pour les objets :

```js
const obj = {
 name: 'David',
 age: 30
};

obj.age = 40;

console.log(obj); // { name: 'David', age: 40 }

```

Ici aussi, nous ne changeons pas la référence de l'endroit où `obj` pointe, mais nous changeons les valeurs stockées à cette référence.

Donc le code ci-dessus fonctionnera, mais le code ci-dessous ne fonctionnera pas.

```js
const obj = { name: 'David', age: 30 };
const obj1 = { name: 'Mike', age: 40 };
obj = obj1; // Uncaught TypeError: Assignment to constant variable.

```

Le code ci-dessus ne fonctionne pas car nous essayons de changer la référence que la variable `const` pointe.

Donc, le point clé à retenir lors de l'utilisation de const est que, lorsque nous déclarons une variable comme une constante en utilisant const, nous ne pouvons pas la redéfinir. Nous ne pouvons pas non plus réassigner cette variable, mais nous pouvons changer les valeurs stockées à cet emplacement si la variable est de type référence.

Donc le code ci-dessous est invalide car nous réassignons une nouvelle valeur.

```js
const arr = [1, 2, 3, 4];
arr = [10, 20, 30]; // Uncaught TypeError: Assignment to constant variable.

```

Mais notez que nous pouvons changer les valeurs à l'intérieur du tableau, comme nous l'avons vu précédemment.

Le code suivant de redéfinition d'une variable `const` est également invalide.

```js
const name = "David";
const name = "Raj"; // Uncaught SyntaxError: Identifier 'name' has already been declared

```

### Résumé de let et const

* Les mots-clés `let` et `const` ajoutent la portée de bloc en JavaScript.
* Lorsque nous déclarons une variable comme `let`, nous ne pouvons pas `redéfinir` ou `re-déclarer` une autre variable let avec le même nom dans la même portée (fonction ou portée de bloc), mais nous pouvons `réassigner` une valeur.
* Lorsque nous déclarons une variable comme `const`, nous ne pouvons pas `redéfinir` ou `re-déclarer` une autre variable `const` avec le même nom dans la même portée (fonction ou portée de bloc). Mais nous pouvons changer les valeurs stockées dans cette variable si la variable est d'un type de référence comme un tableau ou un objet.

D'accord, passons au prochain grand sujet : les promesses.

## Promesses en JavaScript

Les promesses sont l'une des parties les plus importantes mais aussi les plus confuses et difficiles à comprendre de JavaScript. Et la plupart des nouveaux développeurs, ainsi que les plus expérimentés, ont du mal à les comprendre.

Les promesses ont été ajoutées dans ES6 comme une implémentation native.

Alors, qu'est-ce qu'une promesse ? Une promesse représente une opération asynchrone à compléter dans le futur.

Auparavant, avant ES6, il n'y avait aucun moyen d'attendre que quelque chose effectue une opération.

Par exemple, lorsque nous voulions faire un appel d'API, il n'y avait aucun moyen d'attendre que les résultats reviennent avant ES6.

Pour cela, nous utilisions des bibliothèques externes comme Jquery ou Ajax qui avaient leur propre implémentation des promesses. Mais il n'y avait pas de promesse implémentée par le navigateur.

Mais maintenant, en utilisant les promesses dans ES6, nous pouvons faire un appel d'API nous-mêmes et attendre qu'il soit terminé pour effectuer une opération.

### Comment créer une promesse

Pour créer une promesse, nous devons utiliser la fonction constructeur `Promise` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 
});

```

Le constructeur `Promise` prend une fonction comme argument et cette fonction reçoit en interne `resolve` et `reject` comme paramètres.

Les paramètres `resolve` et `reject` sont en fait des fonctions que nous pouvons appeler en fonction du résultat de l'opération asynchrone.

Une `Promise` passe par trois états :

* En attente
* Remplie
* Rejetée

Lorsque nous créons une promesse, elle est dans un état en attente. Lorsque nous appelons la fonction `resolve`, elle passe dans un état rempli et si nous appelons `reject`, elle passera dans l'état rejeté.

Pour simuler l'opération de longue durée ou asynchrone, nous utiliserons la fonction `setTimeout`.

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

```

Ici, nous avons créé une promesse qui se résoudra à la somme de `4` et `5` après un délai de 2000 ms (2 secondes).

Pour obtenir le résultat de l'exécution réussie de la promesse, nous devons enregistrer un rappel en utilisant `.then` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

promise.then(function(result) {
 console.log(result); // 9
});

```

Donc, chaque fois que nous appelons `resolve`, la promesse retournera la valeur passée à la fonction `resolve` que nous pouvons collecter en utilisant le gestionnaire `.then`.

Si l'opération n'est pas réussie, alors nous appelons la fonction `reject` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
});

```

Ici, si la `sum` n'est pas un nombre, alors nous appelons la fonction `reject` avec le message d'erreur. Sinon, nous appelons la fonction `resolve`.

Si vous exécutez le code ci-dessus, vous verrez la sortie suivante :

![Error without catch](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/error_no_catch.png)

Comme vous pouvez le voir, nous obtenons un message d'erreur non capturé ainsi que le message que nous avons spécifié car l'appel de la fonction `reject` génère une erreur. Mais nous n'avons pas ajouté de gestionnaire d'erreur pour capturer cette erreur.

Pour capturer l'erreur, nous devons enregistrer un autre rappel en utilisant `.catch` comme ceci :

```js
promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

Vous verrez la sortie suivante :

![Error with catch](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/error_catch.png)

Comme vous pouvez le voir, nous avons ajouté le gestionnaire `.catch`, donc nous n'obtenons aucune erreur non capturée mais nous enregistrons simplement l'erreur dans la console.

Cela évite également l'arrêt brutal de votre application.

Il est donc toujours recommandé d'ajouter le gestionnaire `.catch` à chaque promesse afin que votre application ne s'arrête pas de fonctionner à cause de l'erreur.

### Chaînage de promesses

Nous pouvons ajouter plusieurs gestionnaires `.then` à une seule promesse comme ceci :

```js
promise.then(function(result) {
 console.log('first .then handler');
 return result;
}).then(function(result) {
 console.log('second .then handler');
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

Lorsque nous avons plusieurs gestionnaires `.then` ajoutés, la valeur de retour du gestionnaire `.then` précédent est automatiquement passée au gestionnaire `.then` suivant.

![Promise Chaining](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/promise_chaining.png)

Comme vous pouvez le voir, l'addition de `4 + 5` résout une promesse et nous obtenons cette somme dans le premier gestionnaire `.then`. Là, nous imprimons une instruction de journalisation et retournons cette somme au gestionnaire `.then` suivant.

Et à l'intérieur du gestionnaire `.then` suivant, nous ajoutons une instruction de journalisation et ensuite nous imprimons le résultat que nous avons obtenu du gestionnaire `.then` précédent.

Cette façon d'ajouter plusieurs gestionnaires `.then` est connue sous le nom de chaînage de promesses.

### Comment retarder l'exécution d'une promesse en JavaScript

Souvent, nous ne voulons pas créer de promesse immédiatement mais nous voulons en créer une après qu'une opération soit terminée.

Pour y parvenir, nous pouvons envelopper la promesse dans une fonction et retourner cette promesse à partir de cette fonction comme ceci :

```js
function createPromise() {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = 4 + 5;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

```

De cette manière, nous pouvons utiliser les paramètres de la fonction à l'intérieur de la promesse, rendant la fonction vraiment dynamique.

```js
function createPromise(a, b) {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = a + b;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

createPromise(1,8)
 .then(function(output) {
  console.log(output); // 9
});

// OU

createPromise(10,24)
 .then(function(output) {
  console.log(output); // 34
});

```

![Output](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/general_function.png)

**Note :** Lorsque nous créons une promesse, elle sera soit résolue soit rejetée mais pas les deux en même temps. Donc nous ne pouvons pas ajouter deux appels de fonction `resolve` ou `reject` dans la même promesse.

De plus, nous pouvons passer seulement une seule valeur à la fonction `resolve` ou `reject`.

Si vous voulez passer plusieurs valeurs à une fonction `resolve`, passez-les sous forme d'objet comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve({
   a: 4,
   b: 5,
   sum
  });
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

![Resolving object](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/65fba14b45b22228f49107634d440903eb0c8dbd/object_resolve.png)

### Comment utiliser les fonctions fléchées en JavaScript

Dans tous les exemples de code ci-dessus, nous avons utilisé la syntaxe de fonction ES5 régulière lors de la création de promesses. Mais il est courant d'utiliser la syntaxe des fonctions fléchées au lieu de la syntaxe de fonction ES5 comme ceci :

```js
const promise = new Promise((resolve, reject) => {
 setTimeout(() => {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then((result) => {
 console.log(result);
});

```

Vous pouvez utiliser soit la syntaxe de fonction ES5 ou ES6 selon vos préférences et besoins.

## Syntaxe d'import et d'export ES6

Avant l'arrivée d'ES6, nous utilisions plusieurs balises `script` dans un seul fichier HTML pour importer différents fichiers JavaScript comme ceci :

```js
<script type="text/javascript" src="home.js"></script>
<script type="text/javascript" src="profile.js"></script>
<script type="text/javascript" src="user.js"></script>

```

Donc, si nous avions une variable avec le même nom dans différents fichiers JavaScript, cela créerait un conflit de nommage et la valeur à laquelle vous vous attendiez ne serait pas la valeur réelle obtenue.

ES6 a résolu ce problème avec le concept de modules.

Chaque fichier JavaScript que nous écrivons en ES6 est connu sous le nom de module. Les variables et fonctions que nous déclarons dans chaque fichier ne sont pas disponibles pour les autres fichiers jusqu'à ce que nous les exportions spécifiquement de ce fichier et les importions dans un autre fichier.

Donc, les fonctions et variables définies dans le fichier sont privées pour chaque fichier et ne peuvent pas être accessibles en dehors du fichier jusqu'à ce que nous les exportions.

Il existe deux types d'exports :

* Exports nommés : Il peut y avoir plusieurs exports nommés dans un seul fichier
* Exports par défaut : Il ne peut y avoir qu'un seul export par défaut dans un seul fichier

### Exports nommés en JavaScript

Pour exporter une seule valeur en tant qu'export nommé, nous l'exportons comme ceci :

```js
export const temp = "This is some dummy text";

```

Si nous avons plusieurs choses à exporter, nous pouvons écrire une instruction d'export sur une ligne séparée au lieu de devant la déclaration de variable. Nous spécifions les choses à exporter entre accolades.

```js
const temp1 = "This is some dummy text1";
const temp2 = "This is some dummy text2";

export { temp1, temp2 };

```

Notez que la syntaxe d'export n'est pas une syntaxe d'objet littéral. Donc en ES6, pour exporter quelque chose, nous ne pouvons pas utiliser des paires clé-valeur comme ceci :

```js
 // Cette syntaxe d'export est invalide en ES6

export { key1: value1, key2: value2 }

```

Pour importer les choses que nous avons exportées en tant qu'export nommé, nous utilisons la syntaxe suivante :

```js
import { temp1, temp2 } from './filename';

```

Notez que lors de l'importation de quelque chose depuis le fichier, nous n'avons pas besoin d'ajouter l'extension `.js` au nom du fichier car elle est considérée par défaut.

```js
// import depuis le fichier functions.js du répertoire courant 
import { temp1, temp2 } from './functions';

// import depuis le fichier functions.js du parent du répertoire courant
import { temp1 } from '../functions';

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/hardcore-pond-q4cjx](https://codesandbox.io/s/hardcore-pond-q4cjx)

**Une chose à noter est que le nom utilisé lors de l'exportation doit correspondre au nom que nous utilisons lors de l'importation.**

Donc si vous exportez comme ceci :

```js
// constants.js
export const PI = 3.14159;

```

Alors lors de l'importation, vous devez utiliser le même nom que celui utilisé lors de l'exportation :

```js
import { PI } from './constants';

```

Vous ne pouvez pas utiliser un autre nom comme ceci :

```js
import { PiValue } from './constants'; // Cela générera une erreur

```

Mais si vous avez déjà la variable avec le même nom que la variable exportée, vous pouvez utiliser la syntaxe de renommage lors de l'importation comme ceci :

```js
import { PI as PIValue } from './constants';

```

Ici, nous avons renommé `PI` en `PIValue` et donc nous ne pouvons pas utiliser le nom de variable `PI` maintenant. Au lieu de cela, nous devons utiliser la variable `PIValue` pour obtenir la valeur exportée de `PI`.

Nous pouvons également utiliser la syntaxe de renommage au moment de l'exportation :

```js
// constants.js
const PI = 3.14159; 

export { PI as PIValue };

```

Alors lors de l'importation, nous devons utiliser `PIValue` comme ceci :

```js
import { PIValue } from './constants';

```

Pour exporter quelque chose en tant qu'export nommé, nous devons d'abord le déclarer.

```js
export 'hello'; // cela entraînera une erreur
export const greeting = 'hello'; // cela fonctionnera
export { name: 'David' }; // Cela entraînera une erreur
export const object = { name: 'David' }; // Cela fonctionnera

```

**L'ordre dans lequel nous importons les exports nommés multiples n'est pas important.**

Regardez le fichier `validations.js` ci-dessous :

```js
// utils/validations.js

const isValidEmail = function(email) {
  if (/^[^@ ]+@[^@ ]+\.[^@ \.]{2,}$/.test(email)) {
    return "email is valid";
  } else {
    return "email is invalid";
  }
};

const isValidPhone = function(phone) {
  if (/^[\\(]\d{3}[\\)]\s\d{3}-\d{4}$/.test(phone)) {
    return "phone number is valid";
  } else {
    return "phone number is invalid";
  }
};

function isEmpty(value) { 
  if (/^\s*$/.test(value)) {
    return "string is empty or contains only spaces";
  } else {
    return "string is not empty and does not contain spaces";
  } 
}

export { isValidEmail, isValidPhone, isEmpty };

```

et dans `index.js`, nous utilisons ces fonctions comme montré ci-dessous :

```js
// index.js
import { isEmpty, isValidEmail } from "./utils/validations";

console.log("isEmpty:", isEmpty("abcd")); // isEmpty: string is not empty and does not contain spaces

console.log("isValidEmail:", isValidEmail("abc@11gmail.com")); // isValidEmail: email is valid

console.log("isValidEmail:", isValidEmail("ab@c@11gmail.com")); // isValidEmail: email is invalid

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/youthful-flower-xesus](https://codesandbox.io/s/youthful-flower-xesus)

Comme vous pouvez le voir, nous pouvons importer uniquement les choses exportées requises et dans n'importe quel ordre, donc nous n'avons pas besoin de vérifier dans quel ordre nous avons exporté dans un autre fichier. C'est la beauté des exports nommés.

### Exports par défaut en JavaScript

Comme je l'ai dit précédemment, il peut y avoir au plus un export par défaut dans un seul fichier.

Vous pouvez, cependant, combiner plusieurs exports nommés et un export par défaut dans un seul fichier.

Pour déclarer un export par défaut, nous ajoutons le mot-clé default devant le mot-clé export comme ceci :

```js
//constants.js
const name = 'David'; 
export default name;

```

Pour importer l'export par défaut, nous n'ajoutons pas les accolades comme nous l'avons fait dans l'export nommé comme ceci :

```js
import name from './constants';

```

Si nous avons plusieurs exports nommés et un export par défaut comme ceci :

```js
// constants.js
export const PI = 3.14159; 
export const AGE = 30;

const NAME = "David";
export default NAME;

```

Alors pour importer tout sur une seule ligne, nous devons utiliser la variable exportée par défaut avant l'accolade uniquement.

```js
// NAME est l'export par défaut et PI et AGE sont des exports nommés ici

import NAME, { PI, AGE } from './constants';

```

**Une spécialité de l'export par défaut est que nous pouvons changer le nom de la variable exportée lors de l'importation :**

```js
// constants.js
const AGE = 30;
export default AGE;

```

Et dans un autre fichier, nous pouvons utiliser un autre nom lors de l'importation

```js
import myAge from './constants'; 

console.log(myAge); // 30

```

Ici, nous avons changé le nom de la variable exportée par défaut de `AGE` à `myAge`.

Cela fonctionne car il ne peut y avoir qu'un seul export par défaut, donc vous pouvez le nommer comme vous le souhaitez.

Une autre chose à noter sur l'export par défaut est que le mot-clé export default ne peut pas venir avant la déclaration de variable comme ceci :

```js
// constants.js
export default const AGE = 30; // Cela est une erreur et ne fonctionnera pas

```

Donc nous devons utiliser le mot-clé export default sur une ligne séparée comme ceci :

```js
// constants.js 

const AGE = 30; 
export default AGE;

```

Nous pouvons, cependant, exporter par défaut sans déclarer la variable comme ceci :

```js
//constants.js
export default {
 name: "Billy",
 age: 40
};

```

et dans un autre fichier, l'utiliser comme ceci :

```js
import user from './constants';
console.log(user.name); // Billy 
console.log(user.age); // 40

```

Il existe une autre façon d'importer toutes les variables exportées dans un fichier en utilisant la syntaxe suivante :

```js
import * as constants from './constants';

```

Ici, nous importons tous les exports nommés et par défaut que nous avons dans `constants.js` et les stockons dans la variable `constants`. Donc, `constants` deviendra un objet maintenant.

```js
// constants.js
export const USERNAME = "David";
export default {
 name: "Billy",
 age: 40
};

```

Et dans un autre fichier, nous l'utilisons comme ci-dessous :

```js
// test.js

import * as constants from './constants';

console.log(constants.USERNAME); // David
console.log(constants.default); // { name: "Billy", age: 40 }
console.log(constants.default.age); // 40

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/green-hill-dj43b](https://codesandbox.io/s/green-hill-dj43b)

Si vous ne voulez pas exporter sur des lignes séparées pour les exports par défaut et nommés, vous pouvez les combiner comme montré ci-dessous :

```js
// constants.js
const PI = 3.14159; const AGE = 30;
const USERNAME = "David";
const USER = {
 name: "Billy",
 age: 40 
};

export { PI, AGE, USERNAME, USER as default };

```

Ici, nous exportons `USER` comme export par défaut et les autres comme exports nommés.

Dans un autre fichier, vous pouvez l'utiliser comme ceci :

```js
import USER, { PI, AGE, USERNAME } from "./constants";

```

Voici une démonstration Code Sandbox : [https://codesandbox.io/s/eloquent-northcutt-7btp1](https://codesandbox.io/s/eloquent-northcutt-7btp1)

### En résumé :

1. En ES6, les données déclarées dans un fichier ne sont pas accessibles à un autre fichier jusqu'à ce qu'elles soient exportées de ce fichier et importées dans un autre fichier.
2. Si nous avons une seule chose dans un fichier à exporter comme une déclaration de classe, nous utilisons l'export par défaut, sinon nous utilisons l'export nommé. Nous pouvons également combiner les exports par défaut et nommés dans un seul fichier.

## Paramètres par défaut en JavaScript

ES6 a ajouté une fonctionnalité très utile de fournir des paramètres par défaut lors de la définition des fonctions.

Supposons que nous avons une application, où une fois que l'utilisateur se connecte au système, nous lui montrons un message de bienvenue comme ceci :

```js
function showMessage(firstName) {
  return "Welcome back, " + firstName;
}
console.log(showMessage('John')); // Welcome back, John

```

Mais que se passe-t-il si nous n'avons pas le nom d'utilisateur dans notre base de données car il s'agissait d'un champ facultatif lors de l'inscription ? Alors nous pouvons montrer le message `Welcome Guest` à l'utilisateur après la connexion.

Donc, nous devons d'abord vérifier si le `firstName` est fourni et ensuite afficher le message correspondant. Avant ES6, nous aurions dû écrire du code comme ceci :

```js
function showMessage(firstName) {
  if(firstName) {
    return "Welcome back, " + firstName;
  } else {
    return "Welcome back, Guest";
  }
}

console.log(showMessage('John')); // Welcome back, John 
console.log(showMessage()); // Welcome back, Guest

```

Mais maintenant, en utilisant les paramètres de fonction par défaut d'ES6, nous pouvons écrire le code ci-dessus comme montré ci-dessous :

```js
function showMessage(firstName = 'Guest') {
   return "Welcome back, " + firstName;
}

console.log(showMessage('John')); // Welcome back, John 
console.log(showMessage()); // Welcome back, Guest

```

**Nous pouvons assigner n'importe quelle valeur comme valeur par défaut au paramètre de la fonction.**

```js
function display(a = 10, b = 20, c = b) { 
 console.log(a, b, c);
}

display(); // 10 20 20
display(40); // 40 20 20
display(1, 70); // 1 70 70
display(1, 30, 70); // 1 30 70

```

Comme vous pouvez le voir, nous avons assigné des valeurs uniques aux paramètres de fonction a et b, mais pour c, nous assignons la valeur de b. Donc, quelle que soit la valeur que nous avons fournie pour b sera également assignée à c s'il n'y a pas de valeur spécifique fournie pour c lors de l'appel de la fonction.

Dans le code ci-dessus, nous n'avons pas fourni tous les arguments à la fonction. Donc, les appels de fonction ci-dessus seront les mêmes que ci-dessous :

```js
display(); // est le même que display(undefined, undefined, undefined)
display(40); // est le même que display(40, undefined, undefined)
display(1, 70); // est le même que display(1, 70, undefined)

```

Donc, si l'argument passé est `undefined`, la valeur par défaut sera utilisée pour le paramètre correspondant.

**Nous pouvons également assigner des valeurs complexes ou calculées comme valeur par défaut.**

```js
const defaultUser = {
  name: 'Jane',
  location: 'NY',
  job: 'Software Developer'
};

const display = (user = defaultUser, age = 60 / 2 ) => { 
 console.log(user, age);
};
display();

/* output

{
  name: 'Jane',
  location: 'NY',
  job: 'Software Developer'
} 30 

*/

```

Maintenant, regardez le code ES5 ci-dessous :

```js
// Code ES5
function getUsers(page, results, gender, nationality) {
  var params = "";
  if(page === 0 || page) {
   params += `page=${page}&`; 
  }
  if(results) {
   params += `results=${results}&`;
  }
  if(gender) {
   params += `gender=${gender}&`;
  }
  if(nationality) {
   params += `nationality=${nationality}`;
  }

  fetch('https://randomuser.me/api/?' + params) 
   .then(function(response) {
     return response.json(); 
   })
   .then(function(result) { 
    console.log(result);
   }) 
   .catch(function(error) {
     console.log('error', error); 
   }); 
}

getUsers(0, 10, 'male', 'us');

```

Dans ce code, nous faisons un appel d'API à l'API [Random user](https://randomuser.me/) en passant divers paramètres optionnels dans la fonction `getUsers`.

Donc, avant de faire l'appel d'API, nous avons ajouté diverses conditions if pour vérifier si le paramètre est ajouté ou non, et en fonction de cela, nous construisons la chaîne de requête comme ceci : `https://randomuser.me/api/? page=0&results=10&gender=male&nationality=us`.

Mais au lieu d'ajouter autant de conditions if, nous pouvons utiliser les paramètres par défaut lors de la définition des paramètres de fonction comme montré ci-dessous :

```js
function getUsers(page = 0, results = 10, gender = 'male',nationality = 'us') {
 fetch(`https://randomuser.me/api/?page=${page}&results=${results}&gender=${gender}&nationality=${nationality}`)
 .then(function(response) { 
  return response.json();
 }) 
 .then(function(result) {
   console.log(result); 
 })
 .catch(function(error) { 
  console.log('error', error);
  }); 
}

getUsers();

```

Comme vous pouvez le voir, nous avons simplifié le code beaucoup. Donc, lorsque nous ne fournissons aucun argument à la fonction `getUsers`, elle prendra les valeurs par défaut et nous pouvons également fournir nos propres valeurs comme ceci :

```js
getUsers(1, 20, 'female', 'gb');

```

Donc, cela remplacera les paramètres par défaut de la fonction.

### null n'est pas égal à undefined

Mais vous devez être conscient d'une chose : `null` et `undefined` sont deux choses différentes lors de la définition des paramètres par défaut.

Regardez le code ci-dessous :

```js
function display(name = 'David', age = 35, location = 'NY'){
 console.log(name, age, location); 
}

display('David', 35); // David 35 NY
display('David', 35, undefined); // David 35 NY

```

Comme nous n'avons pas fourni la troisième valeur pour le paramètre location dans le premier appel à display, il sera `undefined` par défaut, donc la valeur par défaut de location sera utilisée dans les deux appels de fonction. Mais les appels de fonction suivants ne sont pas égaux.

```js
display('David', 35, undefined); // David 35 NY
display('David', 35, null); // David 35 null

```

Lorsque nous passons `null` comme argument, nous disons spécifiquement d'assigner une valeur `null` au paramètre `location`, ce qui n'est pas la même chose que `undefined`. Donc, il ne prendra pas la valeur par défaut de `NY`.

## Array.prototype.includes

ES7 a ajouté une nouvelle fonction qui vérifie si un élément est présent dans le tableau ou non et retourne une valeur booléenne de `true` ou `false`.

```js
// Code ES5

const numbers = ["one", "two", "three", "four"];

console.log(numbers.indexOf("one") > -1); // true 
console.log(numbers.indexOf("five") > -1); // false
```

Le même code utilisant la méthode `includes` du tableau peut être écrit comme montré ci-dessous :

```js
// Code ES7

const numbers = ["one", "two", "three", "four"];

console.log(numbers.includes("one")); // true 
console.log(numbers.includes("five")); // false
```

Donc, l'utilisation de la méthode `includes` du tableau rend le code court et facile à comprendre.

La méthode `includes` est également pratique lors de la comparaison avec différentes valeurs.

Regardez le code ci-dessous :

```js
const day = "monday";

if(day === "monday" || day === "tuesday" || day === "wednesday") {
  // faire quelque chose
}
```

Le code ci-dessus utilisant la méthode `includes` peut être simplifié comme montré ci-dessous :

```js
const day = "monday";

if(["monday", "tuesday", "wednesday"].includes(day)) {
  // faire quelque chose
}
```

Donc, la méthode `includes` est très pratique lors de la vérification de valeurs dans un tableau.

## Points de conclusion

De nombreux changements ont été incorporés dans JavaScript à partir d'ES6. Et chaque développeur JavaScript, Angular, React ou Vue devrait en être conscient.

Les connaître fait de vous un meilleur développeur et peut même vous aider à obtenir un emploi mieux rémunéré. Et si vous apprenez des bibliothèques comme React et des frameworks comme Angular et Vue, vous voudrez certainement être familier avec ces nouvelles fonctionnalités.

## En savoir plus sur les fonctionnalités modernes de JavaScript

Vous pouvez tout apprendre sur les dernières fonctionnalités ajoutées dans JavaScript dans mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/). C'est le seul guide dont vous avez besoin pour apprendre les concepts modernes de JavaScript.

[<img src="https://modernjavascript.yogeshchavan.dev/book_cover.jpg">](https://modernjavascript.yogeshchavan.dev/)

Abonnez-vous à ma [newsletter hebdomadaire](https://bit.ly/2HwVEA2) pour rejoindre plus de 1000 autres abonnés et recevoir des conseils, astuces et articles incroyables directement dans votre boîte de réception.