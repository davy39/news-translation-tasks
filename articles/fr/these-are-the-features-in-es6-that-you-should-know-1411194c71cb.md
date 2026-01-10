---
title: Voici les fonctionnalités d'ES6 que vous devriez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T21:37:34.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-features-in-es6-that-you-should-know-1411194c71cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yZbFWrCpWZnlps21EJ0avQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Voici les fonctionnalités d'ES6 que vous devriez connaître
seo_desc: 'By Cristian Salcescu

  ES6 brings more features to the JavaScript language. Some new syntax allows you
  to write code in a more expressive way, some features complete the functional programming
  toolbox, and some features are questionable.

  let and const

  ...'
---

Par Cristian Salcescu

ES6 apporte plus de fonctionnalités au langage JavaScript. Certaines nouvelles syntaxes vous permettent d'écrire du code de manière plus expressive, certaines fonctionnalités complètent la boîte à outils de programmation fonctionnelle, et certaines fonctionnalités sont discutables.

### let et const

Il existe deux façons de déclarer une variable (`let` et `const`) plus une qui est devenue obsolète (`var`).

## let

`let` déclare et initialise optionnellement une variable dans la portée actuelle. La portée actuelle peut être un module, une fonction ou un bloc. La valeur d'une variable non initialisée est `undefined`.

La portée définit la durée de vie et la visibilité d'une variable. Les variables ne sont pas visibles en dehors de la portée dans laquelle elles sont déclarées.

Considérez le code suivant qui met en évidence la portée de bloc de `let` :

```javascript
let x = 1;
{ 
  let x = 2;
}
console.log(x); //1
```

En revanche, la déclaration `var` n'avait pas de portée de bloc :

```javascript
var x = 1;
{ 
  var x = 2;
}
console.log(x); //2
```

L'instruction de boucle `for`, avec la déclaration `let`, crée une nouvelle variable locale à la portée de bloc, pour chaque itération. La boucle suivante crée cinq fermetures sur cinq variables `i` différentes.

```javascript
(function run(){
  for(let i=0; i<5; i++){
    setTimeout(function log(){
      console.log(i); //0 1 2 3 4
    }, 100);
  }
})();
```

Écrire le même code avec `var` créera cinq fermetures, sur la même variable, donc toutes les fermetures afficheront la dernière valeur de `i`.

La fonction `log()` est une fermeture. Pour plus d'informations sur les fermetures, consultez [Découvrez la puissance des fermetures en JavaScript](https://medium.freecodecamp.org/discover-the-power-of-closures-in-javascript-5c472a7765d7).

## const

`const` déclare une variable qui ne peut pas être réassignée. Elle devient une constante uniquement lorsque la valeur assignée est immutable.

Une valeur immutable est une valeur qui, une fois créée, ne peut pas être modifiée. Les valeurs primitives sont immutables, les objets sont mutables.

`const` gèle la variable, `Object.freeze()` gèle l'objet.

L'initialisation de la variable `const` est obligatoire.

## Modules

Avant les modules, une variable déclarée en dehors de toute fonction était une variable globale.

Avec les modules, une variable déclarée en dehors de toute fonction est masquée et non disponible pour les autres modules, sauf si elle est explicitement exportée.

L'exportation rend une fonction ou un objet disponible pour d'autres modules. Dans l'exemple suivant, j'export des fonctions depuis différents modules :

```js
//module "./TodoStore.js"
export default function TodoStore(){}

//module "./UserStore.js"
export default function UserStore(){}
```

L'importation rend une fonction ou un objet, depuis d'autres modules, disponible pour le module actuel.

```js
import TodoStore from "./TodoStore";
import UserStore from "./UserStore";

const todoStore = TodoStore();
const userStore = UserStore();
```

## Spread/Rest

L'opérateur `...` peut être l'opérateur de spread ou le paramètre rest, selon l'endroit où il est utilisé. Considérez l'exemple suivant :

```js
const numbers = [1, 2, 3];
const arr = ['a', 'b', 'c', ...numbers];

console.log(arr);
["a", "b", "c", 1, 2, 3]
```

Ceci est l'opérateur de spread. Maintenant, regardez l'exemple suivant :

```js
function process(x,y, ...arr){
  console.log(arr)
}
process(1,2,3,4,5);
//[3, 4, 5]

function processArray(...arr){
  console.log(arr)
}
processArray(1,2,3,4,5);
//[1, 2, 3, 4, 5]
```

Ceci est le paramètre rest.

### arguments

Avec le paramètre rest, nous pouvons remplacer le pseudo-paramètre `arguments`. Le paramètre rest est un tableau, `arguments` n'en est pas un.

```js
function addNumber(total, value){
  return total + value;
}

function sum(...args){
  return args.reduce(addNumber, 0);
}

sum(1,2,3); //6
```

### Clonage

L'opérateur de spread rend le clonage des objets et des tableaux plus simple et plus expressif.

L'opérateur de propriété de spread d'objet sera disponible dans le cadre d'ES2018.

```js
const book = { title: "JavaScript: The Good Parts" };

//clone avec Object.assign()
const clone = Object.assign({}, book);

//clone avec l'opérateur de spread
const clone = { ...book };

const arr = [1, 2 ,3];

//clone avec slice
const cloneArr = arr.slice();

//clone avec l'opérateur de spread
const cloneArr = [ ...arr ];
```

### Concaténation

Dans l'exemple suivant, l'opérateur de spread est utilisé pour concaténer des tableaux :

```js
const part1 = [1, 2, 3];
const part2 = [4, 5, 6];

const arr = part1.concat(part2);

const arr = [...part1, ...part2];
```

### Fusion d'objets

L'opérateur de spread, comme `Object.assign()`, peut être utilisé pour copier des propriétés d'un ou plusieurs objets vers un objet vide et combiner leurs propriétés.

```js
const authorGateway = { 
  getAuthors : function() {},
  editAuthor: function() {}
};

const bookGateway = { 
  getBooks : function() {},
  editBook: function() {}
};

//copie avec Object.assign()
const gateway = Object.assign({},
      authorGateway, 
      bookGateway);
      
//copie avec l'opérateur de spread
const gateway = {
   ...authorGateway,
   ...bookGateway
};
```

## Raccourcis de propriétés

Considérez le code suivant :

```js
function BookGateway(){
  function getBooks() {}
  function editBook() {}
  
  return {
    getBooks: getBooks,
    editBook: editBook
  }
}
```

Avec les raccourcis de propriétés, lorsque le nom de la propriété et le nom de la variable utilisée comme valeur sont les mêmes, nous pouvons simplement écrire la clé une fois.

```js
function BookGateway(){
  function getBooks() {}
  function editBook() {}
  
  return {
    getBooks,
    editBook
  }
}
```

Voici un autre exemple :

```js
const todoStore = TodoStore();
const userStore = UserStore();
    
const stores = {
  todoStore,
  userStore
};
```

## Affectation par décomposition

Considérez le code suivant :

```js
function TodoStore(args){
  const helper = args.helper;
  const dataAccess = args.dataAccess;
  const userStore = args.userStore;
}
```

Avec la syntaxe d'affectation par décomposition, cela peut s'écrire comme ceci :

```js
function TodoStore(args){
   const { 
      helper, 
      dataAccess, 
      userStore } = args;
}
```

ou encore mieux, avec la syntaxe de décomposition dans la liste des paramètres :

```js
function TodoStore({ helper, dataAccess, userStore }){}
```

Voici l'appel de fonction :

```js
TodoStore({ 
  helper: {}, 
  dataAccess: {}, 
  userStore: {} 
});
```

## Paramètres par défaut

Les fonctions peuvent avoir des paramètres par défaut. Regardez l'exemple suivant :

```js
function log(message, mode = "Info"){
  console.log(mode + ": " + message);
}

log("An info");
//Info: An info

log("An error", "Error");
//Error: An error
```

## Littéraux de gabarits

Les gabarits sont définis avec le caractère ```. Avec les gabarits, le message de journalisation précédent peut s'écrire comme ceci :

```js
function log(message, mode= "Info"){
  console.log(`${mode}: ${message}`);
}
```

Les gabarits peuvent être définis sur plusieurs lignes. Cependant, une meilleure option est de garder les longs messages texte comme ressources, dans une base de données par exemple.

Voir ci-dessous une fonction qui génère un HTML qui s'étend sur plusieurs lignes :

```js
function createTodoItemHtml(todo){
  return `<li>
    <div>${todo.title}</div>
    <div>${todo.userName}</div>
  </li>`;
}
```

## Appels en position de queue

> _Une fonction récursive est récursive en position de queue lorsque l'appel récursif est la dernière chose que fait la fonction._

Les fonctions récursives en position de queue performantes mieux que les fonctions récursives non en position de queue. L'appel récursif en position de queue optimisé ne crée pas un nouveau cadre de pile pour chaque appel de fonction, mais utilise plutôt un seul cadre de pile.

ES6 apporte l'optimisation des appels en position de queue en mode strict.

[La fonction suivante](https://jsfiddle.net/cristi_salcescu/4t2j3uho/) devrait bénéficier de l'optimisation des appels en position de queue.

```js
function print(from, to) 
{ 
  const n = from;
  if (n > to)  return;
  
  console.log(n);
    
  //la dernière instruction est l'appel récursif 
  print(n + 1, to); 
}

print(1, 10);
```

Note : l'optimisation des appels en position de queue n'est pas encore supportée par les principaux navigateurs.

## Promesses

_Une promesse est une référence à un appel asynchrone. Elle peut être résolue ou échouer quelque part dans le futur._

Les promesses sont plus faciles à combiner. [Comme vous le voyez dans l'exemple suivant](https://jsfiddle.net/cristi_salcescu/eqyhq2e3/), il est facile d'appeler une fonction lorsque toutes les promesses sont résolues, ou lorsque la première promesse est résolue.

```js
function getTodos() { return fetch("/todos"); }
function getUsers() { return fetch("/users"); }
function getAlbums(){ return fetch("/albums"); }

const getPromises = [
  getTodos(), 
  getUsers(), 
  getAlbums()
];

Promise.all(getPromises).then(doSomethingWhenAll);
Promise.race(getPromises).then(doSomethingWhenOne);

function doSomethingWhenAll(){}
function doSomethingWhenOne(){}
```

La fonction `fetch()`, partie de l'API Fetch, retourne une promesse.

`Promise.all()` retourne une promesse qui se résout lorsque toutes les promesses d'entrée sont résolues. `Promise.race()` retourne une promesse qui se résout ou est rejetée lorsque l'une des promesses d'entrée est résolue ou rejetée.

Une promesse peut être dans l'un des trois états : en attente, résolue ou rejetée. La promesse restera en attente jusqu'à ce qu'elle soit résolue ou rejetée.

Les promesses supportent un système de chaînage qui vous permet de passer des données à travers un ensemble de fonctions. [Dans l'exemple suivant](https://jsfiddle.net/cristi_salcescu/kgxnay46/), le résultat de `getTodos()` est passé en entrée à `toJson()`, puis son résultat est passé en entrée à `getTopPriority()`, et ensuite son résultat est passé en entrée à la fonction `renderTodos()`. Lorsque une erreur est lancée ou qu'une promesse est rejetée, `handleError` est appelé.

```js
getTodos()
  .then(toJson)
  .then(getTopPriority)
  .then(renderTodos)
  .catch(handleError);

function toJson(response){}
function getTopPriority(todos){}
function renderTodos(todos){}
function handleError(error){}
```

Dans l'exemple précédent, `.then()` gère le scénario de succès et `.catch()` gère le scénario d'erreur. Si une erreur survient à une étape quelconque, le contrôle de la chaîne saute au gestionnaire de rejet le plus proche en aval de la chaîne.

`Promise.resolve()` retourne une promesse résolue. `Promise.reject()` retourne une promesse rejetée.

## Classe

La classe est une syntaxe sucrée pour créer des objets avec un prototype personnalisé. Elle a une meilleure syntaxe que la précédente, le constructeur de fonction. [Consultez l'exemple suivant](https://jsfiddle.net/cristi_salcescu/aLg8t632/) :

```js
class Service {
  doSomething(){ console.log("doSomething"); }
}

let service = new Service();
console.log(service.__proto__ === Service.prototype);
```

Toutes les méthodes définies dans la classe `Service` seront ajoutées à l'objet `Service.prototype`. Les instances de la classe `Service` auront le même objet prototype (`Service.prototype`). Toutes les instances délégueront les appels de méthode à l'objet `Service.prototype`. Les méthodes sont définies une fois sur `Service.prototype` puis héritées par toutes les instances.

### Héritage

« Les classes peuvent hériter d'autres classes ». Ci-dessous un [exemple d'héritage](https://jsfiddle.net/cristi_salcescu/1xo96yt8/) où la classe `SpecialService` « hérite » de la classe `Service` :

```js
class Service {
  doSomething(){ console.log("doSomething"); }
}

class SpecialService extends Service {
  doSomethingElse(){ console.log("doSomethingElse"); }  
}

let specialService = new SpecialService();
specialService.doSomething();
specialService.doSomethingElse();
```

Toutes les méthodes définies dans la classe `SpecialService` seront ajoutées à l'objet `SpecialService.prototype`. Toutes les instances délégueront les appels de méthode à l'objet `SpecialService.prototype`. Si la méthode n'est pas trouvée dans `SpecialService.prototype`, elle sera recherchée dans l'objet `Service.prototype`. Si elle n'est toujours pas trouvée, elle sera recherchée dans `Object.prototype`.

### La classe peut devenir une mauvaise fonctionnalité

Même si elles semblent encapsulées, tous les membres d'une classe sont publics. Vous devez toujours gérer les problèmes de perte de contexte de `this`. L'API publique est mutable.

`class` peut devenir une mauvaise fonctionnalité si vous négligez le côté fonctionnel de JavaScript. `class` peut donner l'impression d'un langage basé sur les classes alors que JavaScript est à la fois un langage de programmation fonctionnelle et un langage basé sur les prototypes.

Des objets encapsulés peuvent être créés avec des fonctions d'usine. Considérez l'exemple suivant :

```js
function Service() {
  function doSomething(){ console.log("doSomething"); }
  
  return Object.freeze({
     doSomething
  });
}
```

Cette fois, tous les membres sont privés par défaut. L'API publique est immutable. Il n'est pas nécessaire de gérer les problèmes de perte de contexte de `this`.

`class` peut être utilisé comme une exception si requis par le framework de composants. Cela a été le cas avec React, mais ce n'est plus le cas avec [React Hooks](https://reactjs.org/docs/hooks-overview.html).

Pour plus d'informations sur pourquoi privilégier les fonctions d'usine, consultez [Class vs Factory function: exploring the way forward](https://medium.freecodecamp.org/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15).

### Fonctions fléchées

Les fonctions fléchées peuvent créer des fonctions anonymes à la volée. Elles peuvent être utilisées pour créer de petits callbacks, avec une syntaxe plus courte.

Prenons une collection de tâches. Une tâche a un `id`, un `title`, et une propriété booléenne `completed`. Maintenant, considérons le code suivant qui sélectionne uniquement le `title` de la collection :

```js
const titles = todos.map(todo => todo.title);
```

ou l'exemple suivant sélectionnant uniquement les `todos` qui ne sont pas complétés :

```js
const filteredTodos = todos.filter(todo => !todo.completed);
```

### this

Les fonctions fléchées n'ont pas leur propre `this` et `arguments`. Par conséquent, vous pouvez voir la fonction fléchée utilisée pour corriger les problèmes de perte de contexte de `this`. Je pense que la meilleure façon d'éviter ce problème est de ne pas utiliser `this` du tout.

### Les fonctions fléchées peuvent devenir une mauvaise fonctionnalité

Les fonctions fléchées peuvent devenir une mauvaise fonctionnalité lorsqu'elles sont utilisées au détriment des fonctions nommées. Cela créera des problèmes de lisibilité et de maintenabilité. Regardez le code suivant écrit uniquement avec des fonctions fléchées anonymes :

```js
const newTodos = todos.filter(todo => 
       !todo.completed && todo.type === "RE")
    .map(todo => ({
       title : todo.title,
       userName : users[todo.userId].name
    }))
    .sort((todo1, todo2) =>  
      todo1.userName.localeCompare(todo2.userName));
```

[Maintenant, consultez la même logique](https://jsfiddle.net/cristi_salcescu/pm7n2ab5/) refactorisée en fonctions pures avec des noms révélant l'intention et décidez laquelle est plus facile à comprendre :

```js
const newTodos = todos.filter(isTopPriority)
  .map(partial(toTodoView, users))
  .sort(ascByUserName);

function isTopPriority(todo){
  return !todo.completed && todo.type === "RE";
}
  
function toTodoView(users, todo){
  return {
    title : todo.title,
    userName : users[todo.userId].name
  }
}

function ascByUserName(todo1, todo2){
  return todo1.userName.localeCompare(todo2.userName);
}
```

De plus, les fonctions fléchées anonymes apparaîtront comme `(anonymous)` dans la pile d'appels.

Pour plus d'informations sur pourquoi privilégier les fonctions nommées, consultez [How to make your code better with intention-revealing function names](https://medium.freecodecamp.org/how-to-make-your-code-better-with-intention-revealing-function-names-6c8b5271693e).

Moins de code ne signifie pas nécessairement plus lisible. [Regardez l'exemple suivant](https://jsfiddle.net/cristi_salcescu/wc8be2gn/) et voyez quelle version est plus facile à comprendre pour vous :

```js
//avec fonction fléchée
const prop = key => obj => obj[key];

//avec le mot-clé function
function prop(key){
   return function(obj){
      return obj[key];
   }
}
```

Faites attention lorsque vous retournez un objet. Dans l'exemple suivant, `getSampleTodo()` retourne `undefined`.

```js
const getSampleTodo = () => { title : "A sample todo" };

getSampleTodo();
//undefined
```

## Générateurs

Je pense que le générateur ES6 est une fonctionnalité inutile qui complique le code.

Le générateur ES6 crée un objet qui a la méthode `next()`. La méthode `next()` crée un objet qui a la propriété `value`. Les générateurs ES6 favorisent l'utilisation de boucles. [Regardez le code ci-dessous](https://jsfiddle.net/cristi_salcescu/edq7vfwm/) :

```js
function* sequence(){
  let count = 0;
  while(true) {
    count += 1;
    yield count;
  }
}

const generator = sequence();
generator.next().value;//1
generator.next().value;//2
generator.next().value;//3
```

Le même générateur peut être simplement implémenté avec une fermeture.

```js
function sequence(){
  let count = 0;
  return function(){
    count += 1;
    return count;
  }
}

const generator = sequence();
generator();//1
generator();//2
generator();//3
```

Pour plus d'exemples avec des générateurs fonctionnels, consultez [Let’s experiment with functional generators and the pipeline operator in JavaScript](https://medium.freecodecamp.org/lets-experiment-with-functional-generators-and-the-pipeline-operator-in-javascript-520364f97448).

# Conclusion

`let` et `const` déclarent et initialisent des variables.

Les modules encapsulent la fonctionnalité et n'exposent qu'une petite partie.

L'opérateur de spread, le paramètre rest et les raccourcis de propriétés rendent les choses plus faciles à exprimer.

Les promesses et la récursion en position de queue complètent la boîte à outils de programmation fonctionnelle.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour plus d'informations sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)