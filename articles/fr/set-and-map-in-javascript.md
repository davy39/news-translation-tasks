---
title: Comment utiliser Set et Map en JavaScript
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-02-10T15:29:36.000Z'
originalURL: https://freecodecamp.org/news/set-and-map-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/kamaldeenlawal94@gmail.com--1-.jpg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser Set et Map en JavaScript
seo_desc: "There are three major iterables available in JavaScript: Arrays, Maps,\
  \ and Sets. \nIn this article, we will cover the following topics: \n\nWhat is an\
  \ Array?\nWhat is a Set?\nWhat is a Map?\nHow to Create a Seta. How to Create a\
  \ Set with a Value\nProperties..."
---

Il existe trois principaux itérables disponibles en JavaScript : les tableaux (Arrays), les Maps et les Sets. 

Dans cet article, nous aborderons les sujets suivants : 

* [Qu'est-ce qu'un tableau ?](#heading-quest-ce-quun-tableau)
* [Qu'est-ce qu'un Set ?](#heading-quest-ce-quun-set)
* [Qu'est-ce qu'une Map ?](#heading-quest-ce-quune-map)
* [Comment créer un Set](#heading-comment-creer-un-set)  
a. [Comment créer un Set avec une valeur](#heading-comment-creer-un-set-avec-une-valeur)
* [Propriétés et méthodes d'un Set](#heading-proprietes-et-methodes-dun-set)  
a. [Comment utiliser la méthode `add` dans un set](#heading-comment-utiliser-la-methode-add-dans-un-set)  
b. [Comment utiliser la méthode `has` dans un set](#heading-comment-utiliser-la-methode-has-dans-un-set)  
c. [Comment utiliser la méthode `delete` dans un set](#heading-comment-utiliser-la-methode-delete-dans-un-set)  
d. [Comment utiliser la méthode `clear` dans un set](#heading-comment-utiliser-la-methode-clear-dans-un-set)  
e. [Comment utiliser la méthode `entries` dans un set](#heading-comment-utiliser-la-methode-entries-dans-un-set)  
f. [Comment utiliser la méthode `values` dans un set](#heading-comment-utiliser-la-methode-values-dans-un-set)  
g. [Comment utiliser la propriété `size` dans un set](#heading-comment-utiliser-la-propriete-size-dans-un-set)  
h. [Comment utiliser `forEach` dans un set](#heading-comment-utiliser-foreach-dans-un-set)  
i. [Comment utiliser un set pour obtenir une valeur unique à partir d'un tableau](#heading-comment-utiliser-un-set-pour-obtenir-une-valeur-unique-a-partir-dun-tableau)
* [Comment créer une Map](#heading-comment-creer-une-map)
* [Propriétés et méthodes de Map](#heading-proprietes-et-methodes-de-map)  
a. [Comment obtenir des valeurs à partir de l'objet Map](#heading-comment-obtenir-des-valeurs-a-partir-de-lobjet-map)  
b. [Comment ajouter des données avec la méthode `set`](#heading-comment-ajouter-des-donnees-avec-la-methode-set)  
c. [Comment rechercher un élément avec la méthode `has`](#heading-comment-rechercher-un-element-avec-la-methode-has)  
d. [Comment supprimer un élément avec la méthode `delete`](#heading-comment-supprimer-un-element-avec-la-methode-delete)  
e. [Comment effacer tous les éléments avec la méthode `clear`](#heading-comment-effacer-tous-les-elements-avec-la-methode-clear)  
f. [Comment obtenir toutes les entrées dans une Map avec la méthode `entries`](#heading-comment-obtenir-toutes-les-entrees-dans-une-map-avec-la-methode-entries)  
g. [Comment obtenir toutes les clés dans une Map avec la méthode `keys`](#heading-comment-obtenir-toutes-les-cles-dans-une-map-avec-la-methode-keys)  
h. [Comment obtenir toutes les valeurs dans une Map avec la méthode `values`](#heading-comment-obtenir-toutes-les-valeurs-dans-une-map-avec-la-methode-values)  
i. [Comment énumérer sur une Map](#heading-comment-enumerer-sur-une-map)  
j. [Comment utiliser la propriété Size dans Map](#heading-comment-utiliser-la-propriete-size-dans-map)
* [Map vs Object – Quelle est la différence ?](#heading-map-vs-object-quelle-est-la-difference)
* [Avantages des Sets sur les tableaux](#heading-avantages-des-sets-sur-les-tableaux)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un tableau ?

Un **tableau** est l'itérable le plus important et le plus couramment utilisé parmi le trio. Nous l'utilisons pour stocker des listes et des données connectées de tout type et de toute longueur. 

Les tableaux disposent de nombreuses méthodes spéciales. Ils ont également un indexage basé sur zéro pour accéder aux éléments. Vous pouvez avoir des éléments en double dans un tableau, et l'ordre des éléments est garanti.

## Qu'est-ce qu'un Set ?

Un **set** est une structure de données utilisée pour stocker des données de toute longueur et de tout type. Les sets sont des itérables qui disposent de diverses méthodes spéciales différentes des tableaux. 

Certaines des caractéristiques des sets sont que l'ordre des éléments n'est pas garanti, vous ne pouvez pas accéder aux éléments par index, et vous ne pouvez pas avoir d'éléments en double. Les sets sont un excellent choix lorsque vous souhaitez stocker des données sans doublons.

## Qu'est-ce qu'une Map ?

Une **map** est une autre structure de données/conteneur utilisée pour stocker des paires clé-valeur de données de tout type et de toute longueur. 

Les maps sont similaires aux objets, mais avec les maps, vous pouvez utiliser n'importe quoi comme clé. Un objet, en revanche, prend des chaînes de caractères, des symboles et des nombres comme clés. 

Les maps sont des itérables et viennent avec diverses méthodes. Certaines des caractéristiques des maps sont que l'ordre est garanti, et les valeurs peuvent être dupliquées (mais pas les clés).

Maintenant, nous allons en apprendre davantage sur chacun de ces itérables afin que vous compreniez comment les utiliser.

## Comment créer un Set

Puisque nous utilisons les sets pour créer des valeurs uniques, un ID est un exemple parfait de quelque chose à créer avec un set. Nous pouvons créer un nouveau set comme ceci :

```javascript
const ids = new Set();
```

Pour créer un set, vous commencez par le mot-clé `new` suivi de `set`. Dans le code ci-dessus, nous avons créé un set d'IDs qui retourne un set vide.

```javascript
Set(0) {size: 0}
```

### Comment créer un Set avec une valeur

Vous initialisez le set avec un itérable en créant un set avec une certaine valeur initiale. Un itérable tel qu'un tableau, un set ou une nodelist peut être passé au set. L'exemple ci-dessous montre un set créé à partir d'un tableau de 4 éléments.

```javascript
const ids = new Set([3,6,9,7]);
console.log(ids);
```

Le résultat sera comme ceci :

```javascript
Set(4) {3,6,9,7}
```

D'après le résultat, le code retourne un set avec 4 éléments.

## Propriétés et méthodes d'un Set

Les **sets** ont plusieurs méthodes et une propriété que vous pouvez utiliser pour récupérer, ajouter, supprimer, vérifier et effacer tous les éléments du set. Nous parlerons de toutes ces méthodes et propriétés, et de la manière de les utiliser lors de la manipulation du set.

### Comment utiliser la méthode `add` dans un set

Nous utilisons la méthode `add` pour ajouter des éléments au set. Créez un set de fruits avec 4 éléments, cela fonctionne comme ceci :

```javascript
const fruits = new Set(['apple','mango']);
fruits.add('banana');
console.log(fruits)
```

D'après le code ci-dessus, la banane a été ajoutée au set à l'aide de la méthode add, ce qui nous donne ce résultat :

```javascript
Set(3) {'apple', 'mango', 'banana'}
```

Les sets stockent des éléments uniques, ce qui signifie que l'ajout d'une autre banane au set ne sera pas accepté.

### Comment utiliser la méthode `has` dans un set

Pour vérifier si un élément est contenu dans un set, vous utiliserez la méthode `has`. Dans le code ci-dessous, nous vérifierons si un set de fruits contenant divers éléments contient un élément spécifique `banana`.

```javascript
const fruits = new Set(['apple','mango']);
console.log(fruits.has('banana'));
```

Cette méthode retournera false, car l'élément recherché est la banane, qui n'est pas dans le set. Si elle avait été présente, nous aurions obtenu true en retour.

### Comment utiliser la méthode `delete` dans un set

Vous supprimez un élément d'un set en utilisant la méthode "delete". L'exemple ci-dessous montre la méthode "delete" utilisée sur un set de fruits contenant 3 éléments pour supprimer l'un des éléments.

```javascript
const fruits = new Set(['apple','mango', 'banana']);
fruits.delete('apple');
console.log(fruits);
```

Le code imprime un nouveau set de 2 éléments. Si vous essayez de supprimer un élément qui n'est pas dans le set, il l'ignore.

```javascript
Set(2) {'mango', 'banana'};
```

### Comment utiliser la méthode `clear` dans un set

La méthode clear est utilisée pour effacer tous les éléments du set. Avec un set de fruits contenant 3 éléments, nous utilisons la méthode delete pour supprimer l'un des éléments.

```javascript
const fruits = new Set(['apple','mango', 'banana']);
fruits.clear();
console.log(fruits);
```

Le code imprime un nouveau set de 0 éléments, car la méthode clear retournera un set sans aucun élément.

```javascript
Set(0) {size : 0};
```

### Comment utiliser la méthode `entries` dans un set

Vous pouvez récupérer tous les éléments d'un set en utilisant la méthode "entries", qui retourne un itérable. Vous pouvez ensuite utiliser une boucle for ou for-of pour parcourir les valeurs. 

L'exemple ci-dessous montre la création d'un set de fruits contenant 5 éléments, suivie de l'utilisation de la méthode "entries" pour parcourir tous les éléments du tableau.

```javascript
const fruits = new Set([100,160, 200,400,300]);
for( const fruit of fruits.entries()){
    console.log(fruit);
}
```

Il retourne un itérable de tableaux, chacun avec deux éléments.

```javascript
(2) {100, 100}
(2) {160, 160}
(2) {200, 200}
(2) {400, 400}
(2) {300, 300}
```

### Comment utiliser la méthode `values` dans un set

Vous récupérez les valeurs dans un set en utilisant la méthode "values", qui retourne un itérable. Vous pouvez ensuite utiliser une boucle for ou for-of pour parcourir les valeurs. 

L'exemple ci-dessous montre la création d'un set de fruits avec 4 éléments et l'utilisation de la méthode "values" pour parcourir les éléments avec une boucle for-of.

```javascript
const fruits = new Set([100,160, 200,300]);
for( const fruit of fruits.values()){
    console.log(fruit);
}
```

Il retourne un itérable, chacun avec une seule valeur :

```javascript
100
160
200
300
```

### Comment utiliser la propriété `size` dans un set

Vous utilisez la propriété `size` pour déterminer la taille du set en retournant le nombre d'éléments qu'il contient. Pour démontrer cela, nous allons créer un set de fruits qui contient 3 éléments.

```javascript
const fruits = new Set(['apple','mango','banana']);
console.log(fruits.size);
```

Le code ci-dessus retournera 3 comme taille du set de fruits.

```javascript
3
```

### Comment utiliser `forEach` dans un set

Vous pouvez facilement énumérer un set en utilisant "forEach". L'exemple ci-dessous montre la création d'un set de fruits avec certains éléments, suivie de l'utilisation de "forEach" pour imprimer chaque élément du set.

```javascript
const fruits = new Set([100,160, 200,400,300]);
fruits.forEach((fruit) => {
    console.log(fruit)
});
```

Le code imprime chaque élément du set comme ceci :

```javascript
100
160
200
400
300

```

### Comment utiliser un set pour obtenir une valeur unique à partir d'un tableau.

Vous pouvez supprimer les valeurs en double d'un tableau en utilisant un set. L'exemple ci-dessous montre la création d'un tableau de nombres dupliqués, suivie du passage du tableau dans un set pour obtenir tous les nombres uniques, sans doublons.

```javascript
const numbers = [1,2,4,1,6,8,2,5,9,2,0,9,7,6,3,4,6,7,8,4,2,1,5,8,9,0,2,4,5,3,2,6,8,9,6];

const numbers1 = new Set(numbers);
console.log(numbers1);
```

Le code ci-dessus montre un tableau de nombres avec différents nombres dupliqués. Le tableau a ensuite été passé au set de nombres et le résultat est montré ci-dessous.

```javascript
Set(10) {1,2,4,6,8,5,9,0,7,3};
```

Le code ci-dessus montre que le set a supprimé tous les nombres dupliqués et a maintenant une taille de 10.

Comme vous pouvez le voir, un set est une structure de données qui vous aide à gérer des valeurs uniques.

## Comment créer une Map

Vous créez une map en commençant par le mot-clé "new" suivi de "map". L'exemple ci-dessous montre la création d'une map d'un joueur, qui retourne une map vide. Vous pouvez créer une nouvelle map comme ceci :

```javascript
const player = new Map();
console.log(player);
```

Et elle retourne une map avec une valeur vide.

```javascript
Map(0) {size : 0}
```

Vous pouvez également créer une map en utilisant un constructeur initialisé avec un tableau de tableaux. Chaque tableau dans le tableau est une paire clé-valeur, et la clé peut être de n'importe quel type. L'exemple ci-dessous montre la création d'une map de deux tableaux en utilisant le constructeur.

```javascript
const player = new Map([['key','value'],['lawal','kamal']]);
console.log(player);
```

Le code ci-dessus retourne une map avec deux éléments :

```javascript
Map(2) { 'key' => 'value', 'lawal' => 'kamal'}
```

`key` et `lawal` sont les clés de la map, tandis que `value` et `kamal` sont les valeurs.

## Propriétés et méthodes de Map

**Map** a plusieurs méthodes et propriétés que nous pouvons utiliser pour récupérer, ajouter, supprimer, rechercher et effacer tous les éléments de la map. 

Nous parlerons de toutes ces méthodes et propriétés, et de la manière de les utiliser lors de la manipulation de la map.

### Comment obtenir des valeurs à partir de l'objet Map

Extraire des données d'une map est facile en utilisant la méthode get. Créons un objet player1 avec des propriétés de nom et d'âge. Ensuite, l'objet player1 sera utilisé comme clé dans la map. Cela fonctionne comme ceci :

```javascript
const player1 = { name: 'kamal', age: 30};

const playerData = new Map([[player1, [{date:'today',price :400}]]]);
 console.log(playerData);
```

Dans le code ci-dessus, vous pouvez voir que nous avons utilisé l'objet `player1` comme clé dans une Map dans playerData. En utilisant la méthode get, vous pouvez extraire des valeurs de player1 utilisé comme clé dans la Map.

```javascript
Map(1)
```

Elle retourne une map de taille 1. La map contient une clé qui est player1 que nous avons créé ci-dessus.

```javascript
key :{ name : 'kamal', age : 30}
```

Et elle retourne une valeur, qui était un tableau d'un seul objet contenant une date et un prix.

```javascript
0: {date:'today', price:400}
```

### Comment ajouter des données avec la méthode `set`

Vous pouvez ajouter des données à la Map après l'avoir créée à l'aide de la méthode set comme montré ci-dessous :

```javascript
const player = new Map();

player.set('kamal','lawal');

console.log(player);
```

Nous avons ajouté la paire clé-valeur `kamal` et `lawal` à une map vide avec la méthode set. La méthode set est l'endroit où vous définissez une paire clé-valeur. La clé doit être la première option et la valeur doit être la dernière. La clé et les valeurs peuvent être de n'importe quel type de données.

```javascript
Map(1) {'kamal' => 'lawal'}
```

### Comment rechercher un élément avec la méthode `has`

La méthode `has` retourne true si la map contient des clés qui correspondent au terme de recherche. Nous pouvons créer une map de `player` avec deux paires clé-valeur comme montré ci-dessous.

```javascript
const player = new Map([['key','value'],['small','medium']]);

console.log(player.has('small'));
```

Le code imprimera true car le terme de recherche (`small`) est présent dans la map en tant que clé.

```javascript
true

```

Mais il imprimera false si le terme de recherche (`medium`) est présent dans la map non pas en tant que clé mais en tant que valeur.

```javascript
const player = new Map([['key','value'],['small','medium']]);

console.log(player.has('medium'));

// la sortie sera false, le terme recherché (medium) n'est pas une clé mais une valeur
```

### **Comment supprimer un élément avec la méthode `delete`**

Nous utilisons la méthode delete pour supprimer un élément spécifique. Delete fonctionne si le terme recherché correspond à une clé dans un élément. Dans ce cas, nous supprimons `small`.

```javascript
const player = new Map([['key','value'],['small','medium']]);

player.delete('small');

console.log(player);

```

Le code supprimera la paire clé-valeur de `small` et `medium`. Mais, cela ne fonctionnera pas si le terme de recherche n'est pas une clé dans la map.

```javascript
const player = new Map([['key','value'],['small','medium']]);

player.delete('value');

console.log(player);
// Cela ne fonctionnera pas, car le terme de recherche est une valeur dans la map
```

### Comment effacer tous les éléments avec la méthode `clear`

Pour effacer tous les éléments d'une map, nous utiliserons la méthode clear.

```javascript
const player = new Map([['key','value'],['small','medium']]);
player.clear();

console.log(player);

```

Le code imprimera une map vide comme sortie.

```javascript
Map(0) { size : 0}
```

### Comment obtenir toutes les entrées dans une Map avec la méthode `entries`

La méthode entries est l'une des méthodes Map que vous pouvez utiliser avec des boucles for ou for-of directement car elle retourne `MapIterator`. 

#### Qu'est-ce qu'un MapIterator ?

Un MapIterator est un itérateur retourné par la méthode `entries()` d'un objet Map JavaScript. Il retourne un objet de type tableau de paires clé-valeur, chaque paire étant représentée comme un tableau contenant 2 éléments. Le `MapIterator` peut être utilisé dans une boucle `for...of` pour itérer sur toutes les paires clé-valeur dans un objet Map.

Avec `entries`, vous pouvez obtenir toutes les données, à la fois la clé et la valeur d'une map.

```javascript
const player = new Map([['key','value'],['small','medium'],['fruit','another']]);

console.log(player.entries());
```

Les valeurs de toutes les clés et valeurs seront enregistrées comme montré ci-dessous :

```javascript
MapIterator {'key' => 'value', 'small'=> 'medium', 'fruit' => 'another'}
```

### Comment obtenir toutes les clés dans une Map avec la méthode `keys`

Outre la méthode `entries`, la méthode `keys` retourne également un `MapIterator`. Avec la méthode keys, vous pouvez obtenir toutes les clés d'une map, et elle exécute également une boucle for ou for-of :

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

for(const player of players.keys()){
  console.log(player);
}
```

Cela imprimera toutes les clés de la map comme sortie, comme ceci :

```javascript
key
small
fruit
```

### Comment obtenir toutes les valeurs dans une Map avec la méthode `values`

La méthode `values` est la dernière méthode map qui retourne un `MapIterator` et vous pouvez exécuter une boucle for ou for-of directement dessus. C'est la méthode que vous devez utiliser lorsque l'obtention des seules valeurs dans la map est la priorité.

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

for(const player of players.values()){
  console.log(player);
}
```

La sortie du code ci-dessus sera celle-ci :

```javascript
value
medium
another
```

### Comment énumérer sur une Map

Pour une itération facile dans les maps, vous pouvez utiliser la méthode populaire `forEach` comme montré ci-dessous :

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

players.forEach((key, value) =>{
  const message = `I want to be remeembered as the best ${key} pair ${value}`;
    console.log(message)
})
```

Le code ci-dessus imprimera ceci comme sortie de l'itération :

```javascript
I want to be remembered as the best value pair key
I want to be remembered as the best medium pair small
I want to be remembered as the best another pair fruit

```

### Comment utiliser la propriété Size dans Map

Vous pouvez utiliser la propriété size pour déterminer la taille de la map en retournant le nombre d'éléments qu'elle contient.

```javascript
const player = new Map([['key', 'value'],['small','medium'],['fruit','another']]);

console.log(player.size);
```

Cela imprimera 3 comme taille de la map.

### Map vs Object – Quelle est la différence ?

Comme vous pouvez le voir, une map est similaire à un objet, ce qui soulève la question – quand devez-vous utiliser chacun ?

Quand utiliser une map :

1. Avec une map, vous pouvez utiliser n'importe quel type (et valeurs) comme clés.
2. La map offre de meilleures performances pour de grandes quantités de données.
3. Utilisez une map pour de meilleures performances lors de l'ajout et de la suppression fréquente de données.

Quand utiliser un objet :

1. Les objets ne peuvent utiliser que des nombres, des chaînes de caractères et des symboles comme clés.
2. Les objets sont parfaits pour des ensembles de données de petite à moyenne taille.
3. Les objets ont de meilleures performances et sont plus faciles à créer.

### Avantages des Sets sur les tableaux

Les tableaux et les sets sont tous deux des structures de données utilisées pour stocker des collections d'éléments. Mais les sets ont un léger avantage sur les tableaux grâce à :

* Unicité : Avec un set, les doublons sont supprimés pour réduire la taille de la structure de données (contrairement à un tableau qui stocke les doublons).
* Manipulation des collections : Il est facile de combiner un set avec d'autres sets pour effectuer diverses opérations comme les intersections, les unions et les différences.
* Performance : Grâce à l'implémentation utilisant des tables de hachage, le set offre des recherches plus rapides et des tests d'appartenance.

## Conclusion

Dans ce tutoriel, vous avez appris la relation entre les tableaux, les sets et les maps. 

Nous avons créé, modifié et supprimé des éléments dans les maps et les sets. Nous avons comparé les maps et les objets, et enfin, nous avons parlé des avantages des sets sur les tableaux.