---
title: Comment utiliser les collections JavaScript – Map et Set
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-10-05T16:59:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-collections-map-and-set
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cover-5.png
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les collections JavaScript – Map et Set
seo_desc: 'In JavaScript, objects are used to store multiple values as a complex data
  structure.

  An object is created with curly braces {…} and a list of properties. A property
  is a key-value pair where the key must be a string and the value can be of any type....'
---

En JavaScript, les `objets` sont utilisés pour stocker plusieurs valeurs sous forme de structure de données complexe.

Un objet est créé avec des accolades `{…}` et une liste de propriétés. Une propriété est une paire clé-valeur où la `clé` doit être une chaîne de caractères et la `valeur` peut être de n'importe quel type.

D'autre part, les `tableaux` sont une collection ordonnée qui peut contenir des données de n'importe quel type. En JavaScript, les tableaux sont créés avec des crochets `[...]` et permettent des éléments en double.

Jusqu'à ES6 (ECMAScript 2015), les `objets` et les `tableaux` JavaScript étaient les structures de données les plus importantes pour gérer les collections de données. La communauté des développeurs n'avait pas beaucoup de choix en dehors de cela. Même ainsi, une combinaison d'objets et de tableaux était capable de gérer les données dans de nombreux scénarios.

Cependant, il y avait quelques lacunes,

* Les clés d'objet ne peuvent être que de type `chaîne`.
* Les objets ne maintiennent pas l'ordre des éléments insérés.
* Les objets manquent de certaines méthodes utiles, ce qui les rend difficiles à utiliser dans certaines situations. Par exemple, vous ne pouvez pas calculer facilement la taille (`length`) d'un objet. De plus, l'énumération d'un objet n'est pas si simple.
* Les tableaux sont des collections d'éléments qui permettent les doublons. La prise en charge des tableaux qui n'ont que des éléments distincts nécessite une logique et un code supplémentaires.

Avec l'introduction d'ES6, nous avons obtenu deux nouvelles structures de données qui répondent aux lacunes mentionnées ci-dessus : `Map` et `Set`. Dans cet article, nous allons examiner les deux de près et comprendre comment les utiliser dans différentes situations.

## Map en JavaScript

`Map` est une collection de paires clé-valeur où la clé peut être de n'importe quel type. `Map` se souvient de l'ordre original dans lequel les éléments ont été ajoutés, ce qui signifie que les données peuvent être récupérées dans le même ordre où elles ont été insérées.

En d'autres termes, `Map` a des caractéristiques à la fois de `Object` et de `Array` :

* Comme un objet, il prend en charge la structure de paire clé-valeur.
* Comme un tableau, il se souvient de l'ordre d'insertion.

### **Comment créer et initialiser une Map en JavaScript**

Une nouvelle `Map` peut être créée comme ceci :

```js
const map = new Map();
```

Ce qui retourne une `Map` vide :

```shell
Map(0) {}
```

Une autre façon de créer une `Map` est avec des valeurs initiales. Voici comment créer une `Map` avec trois paires clé-valeur :

```js
const freeCodeCampBlog = new Map([
  ['name', 'freeCodeCamp'],
  ['type', 'blog'],
  ['writer', 'Tapas Adhikary'],
]);
```

Ce qui retourne une `Map` avec trois éléments :

```shell
Map(3) {"name" => "freeCodeCamp", "type" => "blog", "writer" => "Tapas Adhikary"}
```

### **Comment ajouter des valeurs à une Map en JavaScript**

Pour ajouter une valeur à une Map, utilisez la méthode `set(key, value)`.

La méthode `set(key, value)` prend deux paramètres, `key` et `value`, où la clé et la valeur peuvent être de n'importe quel type, un primitif (`boolean`, `string`, `number`, etc.) ou un objet :

```js
// créer une map
const map = new Map();

// Ajouter des valeurs à la map
map.set('name', 'freeCodeCamp');
map.set('type', 'blog');
map.set('writer', 'Tapas Adhikary');
```

Sortie :

```shell
Map(3) {"name" => "freeCodeCamp", "type" => "blog", "writer" => "Tapas Adhikary"}
```

Veuillez noter que si vous utilisez la même clé pour ajouter une valeur à une `Map` plusieurs fois, elle remplacera toujours la valeur précédente :

```js
// Ajouter un écrivain différent
map.set('writer', 'Someone else!');
```

Donc la sortie serait :

```shell
Map(3) 
{"name" => "freeCodeCamp", "type" => "blog", "writer" => "Someone else!"}
```

### **Comment obtenir des valeurs d'une Map en JavaScript**

Pour obtenir une valeur d'une `Map`, utilisez la méthode `get(key)` :

```js
map.get('name'); // retourne freeCodeCamp
```

### **Tout sur les clés de Map en JavaScript**

Les clés `Map` peuvent être de n'importe quel type, un primitif ou un objet. C'est l'une des principales différences entre `Map` et les objets JavaScript réguliers où la clé ne peut être qu'une chaîne :

```js
// créer une Map
const funMap = new Map();

funMap.set(360, 'Mon numéro de maison'); // nombre comme clé
funMap.set(true, 'J'écris des blogs !'); // booléen comme clé

let obj = {'name': 'tapas'}
funMap.set(obj, true); // objet comme clé

console.log(funMap);
```

Voici la sortie :

```shell
Map(3) 
{
  360 => "Mon numéro de maison", 
  true => "J'écris des blogs !", 
  {…} => true
}
```

Un objet JavaScript régulier traite toujours la clé comme une chaîne. Même lorsque vous lui passez un primitif ou un objet, il convertit interne la clé en chaîne :

```js
// Créer un objet vide
const funObj = {};

// ajouter une propriété. Notez, passer la clé comme un nombre.
funObj[360] = 'Mon numéro de maison';

// Il retourne true car le nombre 360 a été converti en chaîne '360' en interne !
console.log(funObj[360] === funObj['360']);
```

### **Propriétés et méthodes de Map en JavaScript**

La `Map` de JavaScript a des propriétés et méthodes intégrées qui la rendent facile à utiliser. En voici quelques-unes courantes :

* Utilisez la propriété `size` pour savoir combien d'éléments se trouvent dans une `Map` :
* Recherchez un élément avec la méthode `has(key)` :
* Supprimez un élément avec la méthode `delete(key)` :
* Utilisez la méthode `clear()` pour supprimer tous les éléments de la `Map` en une seule fois :

```js
console.log('la taille de la map est', map.size);
```

```js
// retourne true, si la map a un élément avec la clé, 'John'
console.log(map.has('John')); 


// retourne false, si la map n'a pas d'élément avec la clé, 'Tapas'
console.log(map.has('Tapas')); 
```

```js
map.delete('Sam'); // supprime l'élément avec la clé, 'Sam'.
```

```js
// Effacer la map en supprimant tous les éléments
map.clear(); 

map.size // Il retournera, 0

```

### **MapIterator : keys(), values(), et entries() en JavaScript**

Les méthodes `keys()`, `values()` et `entries()` retournent un `MapIterator`, ce qui est excellent car vous pouvez utiliser une boucle `for-of` ou `forEach` directement dessus.

Tout d'abord, créez une `Map` simple :

```js
const ageMap = new Map([
  ['Jack', 20],
  ['Alan', 34],
  ['Bill', 10],
  ['Sam', 9]
]);
```

* Obtenez toutes les clés :
* Obtenez toutes les valeurs :
* Obtenez toutes les entrées (paires clé-valeur) :

```js
console.log(ageMap.keys());

// Sortie :

// MapIterator {"Jack", "Alan", "Bill", "Sam"}
```

```js
console.log(ageMap.values());

// Sortie

// MapIterator {20, 34, 10, 9}
```

```js
console.log(ageMap.entries());

// Sortie

// MapIterator {"Jack" => 20, "Alan" => 34, "Bill" => 10, "Sam" => 9}
```

### **Comment itérer sur une Map en JavaScript**

Vous pouvez utiliser soit la boucle `forEach` ou `for-of` pour itérer sur une `Map` :

```js
// avec forEach
ageMap.forEach((value, key) => {
   console.log(`${key} a ${value} ans !`);
});

// avec for-of
for(const [key, value] of ageMap) {
  console.log(`${key} a ${value} ans !`);
}
```

La sortie sera la même dans les deux cas :

```shell
Jack a 20 ans !
Alan a 34 ans !
Bill a 10 ans !
Sam a 9 ans !
```

### **Comment convertir un Objet en Map en JavaScript**

Vous pouvez rencontrer une situation où vous devez convertir un `objet` en une structure de type `Map`. Vous pouvez utiliser la méthode `entries` de `Object` pour cela :

```js
const address = {
  'Tapas': 'Bangalore',
  'James': 'Huston',
  'Selva': 'Srilanka'
};

const addressMap = new Map(Object.entries(address));
```

### **Comment convertir une Map en Objet en JavaScript**

Si vous voulez faire l'inverse, vous pouvez utiliser la méthode `fromEntries` :

```js
Object.fromEntries(map)
```

### **Comment convertir une Map en Tableau en JavaScript**

Il existe plusieurs façons de convertir une map en tableau :

* En utilisant `Array.from(map)` :
* En utilisant l'opérateur de propagation :

```js
const map = new Map();
map.set('milk', 200);
map.set("tea", 300);
map.set('coffee', 500);

console.log(Array.from(map));
```

```js
console.log([...map]);
```

### **Map vs. Object : Quand les utiliser ?**

`Map` a des caractéristiques à la fois de `object` et de `array`. Cependant, `Map` ressemble plus à un `object` qu'à un `array` en raison de la nature du stockage des données au format `clé-valeur`.

La similarité avec les objets s'arrête ici. Comme vous l'avez vu, `Map` est différent à bien des égards. Alors, lequel devez-vous utiliser, et quand ? Comment décider ?

Utilisez `Map` lorsque :

* Vos besoins ne sont pas si simples. Vous pouvez vouloir créer des clés qui ne sont pas des chaînes. Stocker un objet comme clé est une approche très puissante. `Map` vous donne cette capacité par défaut.
* Vous avez besoin d'une structure de données où les éléments peuvent être ordonnés. Les objets réguliers ne maintiennent pas l'ordre de leurs entrées.
* Vous cherchez de la flexibilité sans dépendre d'une bibliothèque externe comme lodash. Vous pourriez finir par utiliser une bibliothèque comme lodash car nous ne trouvons pas de méthodes comme has(), values(), delete(), ou une propriété comme size avec un objet régulier. Map facilite cela en fournissant toutes ces méthodes par défaut.

Utilisez un objet lorsque :

* Vous n'avez aucun des besoins listés ci-dessus.
* Vous dépendez de `JSON.parse()` car une `Map` ne peut pas être analysée avec.

## Set en JavaScript

Un `Set` est une collection d'éléments uniques qui peuvent être de n'importe quel type. `Set` est également une collection ordonnée d'éléments, ce qui signifie que les éléments seront récupérés dans le même ordre où ils ont été insérés.

Un `Set` en JavaScript se comporte de la même manière qu'un ensemble mathématique.

### Comment créer et initialiser un Set en JavaScript

Un nouveau `Set` peut être créé comme ceci :

```js
const set = new Set();
console.log(set);
```

Et la sortie sera un `Set` vide :

```shell
Set(0) {}
```

Voici comment créer un `Set` avec quelques valeurs initiales :

```js
const fruteSet = new Set(['🍉', '🍎', '🍈', '🍏']);
console.log(fruteSet);
```

Sortie :

```shell
Set(4) {"🍉", "🍎", "🍈", "🍏"}
```

### **Propriétés et méthodes de Set en JavaScript**

`Set` a des méthodes pour ajouter un élément, supprimer des éléments, vérifier si un élément existe et pour le vider complètement :

* Utilisez la propriété `size` pour connaître la taille du `Set`. Elle retourne le nombre d'éléments qu'il contient :
* Utilisez la méthode `add(element)` pour ajouter un élément au `Set` :

```js
set.size
```

```js
// Créer un set - saladSet
const saladSet = new Set();

// Ajouter quelques légumes
saladSet.add('🍅'); // tomate
saladSet.add('🥑'); // avocat
saladSet.add('🥕'); // carotte
saladSet.add('🥒'); // concombre

console.log(saladSet);


// Sortie

// Set(4) {"🍅", "🥑", "🥕", "🥒"}
```

J'adore les concombres ! Et si on en ajoutait un autre ?

Oh non, je ne peux pas – `Set` est une collection d'éléments _uniques_ :

```js
saladSet.add('🥒');
console.log(saladSet);
```

La sortie est la même qu'avant – rien n'a été ajouté au `saladSet`.

* Utilisez la méthode `has(element)` pour rechercher si nous avons une carotte (🥕) ou un brocoli (🥦) dans le `Set` :
* Utilisez la méthode `delete(element)` pour supprimer l'avocat(🥑) du `Set` :

```js
// La salade a une 🥕, donc retourne true
console.log('La salade a-t-elle une carotte ?', saladSet.has('🥕'));

// La salade n'a pas de 🥦, donc retourne false
console.log('La salade a-t-elle du brocoli ?', saladSet.has('🥦'));
```

```js
saladSet.delete('🥑');
console.log('Je n'aime pas 🥑, retirez de la salade :', saladSet);
```

Notre salade `Set` est maintenant comme suit :

```shell
Set(3) {"🍅", "🥕", "🥒"}
```

* Utilisez la méthode `clear()` pour supprimer tous les éléments d'un `Set` :

```js
saladSet.clear();
```

### **Comment itérer sur un Set** en JavaScript

`Set` a une méthode appelée `values()` qui retourne un `SetIterator` pour obtenir toutes ses valeurs :

```js
// Créer un Set
const houseNos = new Set([360, 567, 101]);

// Obtenir le SetIterator en utilisant la méthode `values()`
console.log(houseNos.values());
```

Sortie :

```js
SetIterator {360, 567, 101}
```

Nous pouvons utiliser une boucle `forEach` ou `for-of` pour récupérer les valeurs.

Intéressant, JavaScript essaie de rendre `Set` compatible avec `Map`. C'est pourquoi nous trouvons deux des mêmes méthodes que `Map`, `keys()` et `entries()`.

Comme `Set` n'a pas de clés, la méthode `keys()` retourne un `SetIterator` pour récupérer ses valeurs :

```js
console.log(houseNos.keys());

// Sortie

// console.log(houseNos.keys());
```

Avec `Map`, la méthode `entries()` retourne un itérateur pour récupérer les paires clé-valeur. Encore une fois, il n'y a pas de clés dans un `Set`, donc `entries()` retourne un `SetIterator` pour récupérer les paires valeur-valeur :

```js
console.log(houseNos.entries());

// Sortie

// SetIterator {360 => 360, 567 => 567, 101 => 101}
```

### **Comment énumérer sur un Set en JavaScript**

Nous pouvons énumérer sur un Set en utilisant les boucles `forEach` et `for-of` :

```js
// avec forEach

houseNos.forEach((value) => {
   console.log(value);
});


// avec for-of

for(const value of houseNos) {
   console.log(value);
 }
```

La sortie des deux est :

```shell
360
567
101
```

### **Sets et Arrays en JavaScript**

Un tableau, comme un `Set`, vous permet d'ajouter et de supprimer des éléments. Mais `Set` est assez différent et n'est pas destiné à remplacer les tableaux.

La différence majeure entre un tableau et un `Set` est que les tableaux vous permettent d'avoir des éléments en double. De plus, certaines des opérations `Set` comme `delete()` sont plus rapides que les opérations de tableau comme `shift()` ou `splice()`.

Considérez `Set` comme une extension d'un tableau régulier, juste avec plus de muscles. La structure de données `Set` n'est pas un remplacement du `array`. Les deux peuvent résoudre des problèmes intéressants.

### **Comment convertir un Set en tableau en JavaScript**

Convertir un `Set` en tableau est simple :

```js
const arr = [...houseNos];
console.log(arr);
```

### **Valeurs uniques à partir d'un tableau en utilisant le Set en JavaScript**

Créer un `Set` est un moyen très facile de supprimer les valeurs en double d'un tableau :

```js
// Créer un tableau mixedFruit avec quelques fruits en double
const mixedFruit = ['🍉', '🍎', '🍉', '🍈', '🍏', '🍎', '🍈'];

// Passer le tableau pour créer un set de fruits uniques
const mixedFruitSet = new Set(mixedFruit);

console.log(mixedFruitSet);
```

Sortie :

```shell
Set(4) {"🍉", "🍎", "🍈", "🍏"}
```

### **Set et Object en JavaScript**

Un `Set` peut avoir des éléments de n'importe quel type, même des objets :

```js
// Créer un objet personne
const person = {
   'name': 'Alex',
   'age': 32
 };

// Créer un set et ajouter l'objet
const pSet = new Set();
pSet.add(person);
console.log(pSet);
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-113.png)

Pas de surprise ici – le `Set` contient un élément qui est un objet.

Changeons une propriété de l'objet et ajoutons-le à nouveau au set :

```js
// Changer le nom de la personne
person.name = 'Bob';

// Ajouter l'objet personne au set à nouveau
pSet.add(person);
console.log(pSet);
```

Que pensez-vous que sera la sortie ? Deux objets `person` ou seulement un ?

Voici la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-114.png)

`Set` est une collection d'éléments uniques. En changeant la propriété de l'objet, nous n'avons pas changé l'objet lui-même. Par conséquent, `Set` ne permettra pas les éléments en double.

`Set` est une excellente structure de données à utiliser en plus des tableaux JavaScript. Il n'a pas un énorme avantage sur les tableaux réguliers, cependant.

Utilisez `Set` lorsque vous devez maintenir un ensemble distinct de données pour effectuer des opérations d'ensemble comme `union`, `intersection`, `différence`, et ainsi de suite.

## **En résumé**

Voici un dépôt GitHub pour trouver tout le code source utilisé dans cet article. Si vous l'avez trouvé utile, veuillez montrer votre soutien en lui donnant une étoile : [https://github.com/atapas/js-collections-map-set](https://github.com/atapas/js-collections-map-set)

Vous aimerez peut-être aussi certains de mes autres articles :

* [Mes conseils et astuces JavaScript préférés](https://blog.greenroots.info/my-favorite-javascript-tips-and-tricks-ckd60i4cq011em8s16uobcelc)
* [Égalité et similarité en JavaScript avec ==, === et Object.is()](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis-ckdpt2ryk01vel9s186ft8cwl)

Si cet article était utile, veuillez le partager afin que d'autres puissent le lire également. Vous pouvez me mentionner sur Twitter ([@tapasadhikary](https://twitter.com/tapasadhikary)) avec des commentaires, ou n'hésitez pas à me suivre.