---
title: Qu'est-ce que les objets en JavaScript ?
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-02-08T19:23:29.000Z'
originalURL: https://freecodecamp.org/news/objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Your-paragraph-text.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que les objets en JavaScript ?
seo_desc: 'Objects are important data structures in JavaScript. This is partly because
  arrays are objects in JavaScript, and you''ll use them all the time.

  Objects are super important for grouping data and functionalities, so you can do
  a lot with an object in J...'
---

Les objets sont des structures de données importantes en JavaScript. Cela est en partie dû au fait que les tableaux sont des objets en JavaScript, et vous les utiliserez tout le temps.

Les objets sont super importants pour regrouper des données et des fonctionnalités, donc vous pouvez faire beaucoup de choses avec un objet en JavaScript. Le nœud DOM, et tout nœud DOM créé avec `createElement` sont des exemples d'objet en JavaScript.

Dans cet article, nous allons couvrir tout ce qui suit sur les objets :

* [Qu'est-ce qu'un objet JavaScript ?](#heading-questce-quun-objet-javascript)
* [Comment créer un objet en JavaScript](#heading-comment-creer-un-objet-en-javascript)
* [Comment ajouter des propriétés dans un objet](#heading-comment-ajouter-des-proprietes-dans-un-objet)
* [Pourquoi le mot-clé `let` plutôt que la notation par point ?](#heading-pourquoi-le-mot-cle-let-plutot-que-la-notation-par-point)
* [Comment modifier des propriétés dans un objet](#heading-comment-modifier-des-proprietes-dans-un-objet)
* [Comment supprimer des propriétés dans un objet](#heading-comment-supprimer-des-proprietes-dans-un-objet)
* [Comment utiliser des clés spéciales dans les objets](#heading-comment-utiliser-des-cles-speciales-dans-les-objets)
* [Comment accéder aux propriétés avec des crochets](#heading-comment-acceder-aux-proprietes-avec-des-crochets)
* [Comment définir dynamiquement des propriétés](#heading-comment-definir-dynamiquement-des-proprietes)
* [Syntaxe abrégée des méthodes](#heading-syntaxe-abregée-des-methodes)
* [Avantages de l'utilisation des méthodes courtes d'objet par rapport aux méthodes régulières.](#heading-avantages-de-lutilisation-des-methodes-courtes-dobjet-par-rapport-aux-methodes-regulieres)
* [Opérateur de propagation d'objet](#heading-operateur-de-propagation-dobjet)
* [Destructuration d'objet](#heading-destructuration-dobjet)
* [Comment utiliser le mot-clé `this` en JavaScript](https://www.freecodecamp.org/news/p/f8c8e52f-7c90-4e0c-b2ac-0bb498e15fb3/How%20to%20Use%20the%20this%20Keyword%20in%20JavaScript)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un objet JavaScript ?

Les objets dans la vie quotidienne ont des propriétés et des actions "méthodes". Prenons, par exemple, un ventilateur. C'est un objet avec des propriétés telles que la marque, la couleur ou le modèle, et des actions qu'il peut effectuer telles que refroidir les pièces et contrôler l'humidité.

Comme expliqué ci-dessus, les objets en JavaScript sont des structures de données principales qui comprennent des propriétés et des méthodes. Alors que les méthodes sont des fonctions/actions qu'un objet peut effectuer (comme conduire et refroidir les pièces avec des objets de la vie réelle comme les voitures et les ventilateurs), les propriétés sont des caractéristiques d'un objet telles que son nom et sa valeur.

Les objets vous permettent de regrouper des données liées ensemble et de diviser le code en morceaux logiques. En JavaScript, nous avons des valeurs primitives et des valeurs de référence. Number, Boolean, Null, Undefined, String et Symbol sont des valeurs primitives, tandis que les objets comme les nœuds DOM, les tableaux, etc., sont des valeurs de référence.

Dans la vie réelle et en JavaScript, vous pouvez utiliser des objets de différentes manières selon leurs propriétés et méthodes. Nous allons en apprendre davantage sur les objets JavaScript maintenant.

## Comment créer un objet en JavaScript

Nous utiliserons le code ci-dessous comme exemple :

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

Dans le code ci-dessus, nous avons un objet `person` que nous avons créé avec des accolades. L'objet a des paires clé-valeur. Vous pouvez stocker des paires clé-valeur dans un objet JavaScript, en associant chaque clé à une valeur unique.

Ces paires clé-valeur vous permettent de récupérer des valeurs en utilisant les clés associées. Par exemple, l'objet ci-dessus représente une personne avec des propriétés comme "name", "age", "friends", et une fonction "greet". Chaque propriété devient une paire clé-valeur avec le nom de la propriété comme clé et la valeur de la propriété comme valeur. Les propriétés et les méthodes sont créées à l'intérieur de l'objet.

Pour créer une clé dans un objet, vous n'avez pas besoin d'un mot-clé let ou const. Parce que les objets sont dynamiques, vous pouvez ajouter ou changer des propriétés sans déclarer de variable. Au lieu de cela, vous commencez avec votre nom préféré, un deux-points, puis votre valeur.

Nous avons créé un tableau de `friends` à l'intérieur de l'objet pour montrer que nous pouvons avoir un objet à l'intérieur d'un objet. Nous avons créé une méthode (qui est une fonction) à l'intérieur d'un objet avec `greet` comme clé.

### Comment ajouter des propriétés dans un objet

Il existe deux approches principales pour ajouter des propriétés à un objet en JavaScript. La première consiste à créer un tout nouvel objet.

```javascript
let person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
 person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  },
  isAdmin:true
}
```

Avec le code ci-dessus, nous avons créé le premier objet person en utilisant le mot-clé `let`, ce qui nous permet de le réassigner à une nouvelle valeur. Nous avons ensuite ajouté la propriété "isAdmin" à l'objet person. Si vous exécutez `console.log(person)`, vous verrez que "isAdmin" fait maintenant partie des propriétés de l'objet.

La deuxième approche consiste à ajouter des propriétés en utilisant la notation par point.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
```

Avec la notation par point, vous pouvez accéder à des propriétés qu'un objet n'a pas encore ajoutées. Par exemple, si l'objet person n'a pas de propriété "isAdmin", y accéder retournera "undefined".

Vous pouvez ajouter la propriété "isAdmin" à l'objet person en utilisant la notation par point, et vous pouvez également écraser n'importe quelle propriété en lui assignant une nouvelle valeur. Cette approche est plus courte et plus simple par rapport à d'autres méthodes.

### Pourquoi le mot-clé `let` plutôt que la notation par point ?

Le choix entre l'utilisation du mot-clé `let` et la notation par point dépend de savoir si vous devez créer une nouvelle référence d'objet ou modifier une référence existante.

Vous utiliseriez le mot-clé `let` pour créer un nouvel objet lorsque vous devez créer une nouvelle référence à un objet, séparée de toute référence existante à des objets similaires.

D'autre part, vous utiliseriez la notation par point pour ajouter ou modifier des propriétés sur une référence d'objet existante. Cela est utile lorsque vous souhaitez apporter des modifications à un objet sans créer une nouvelle référence.

### Comment modifier des propriétés dans un objet

Vous pouvez également utiliser la notation par point pour modifier des propriétés dans un objet. Le code ci-dessous montre que la propriété `name` avec la valeur associée `kamal` sera changée en `lawal` lorsqu'elle est modifiée en utilisant la notation par point.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
person.name = 'lawal';
console.log(person);
```

### Comment supprimer des propriétés dans un objet

Il est très simple de supprimer une propriété dans un objet. JavaScript a un mot-clé spécial appelé "**delete**" qui vous permet de supprimer les propriétés que vous souhaitez.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
delete person.friends;
console.log(person);
```

La propriété `friends` sera supprimée de l'objet avec le code ci-dessus.

### Comment utiliser des clés spéciales dans les objets

Vous pouvez utiliser n'importe quoi comme nom de clé que vous pouvez utiliser comme nom de variable. Mais tous les noms de clé ne peuvent pas servir de nom de variable car les clés sont plus flexibles que les variables.

```javascript
let person = {
 name:'kamal',
 age:37,
}
```

Supposons que vous souhaitiez utiliser "last name" comme clé au lieu de "name". La syntaxe JavaScript ne permet pas deux mots séparés dans cette convention de nommage.

Mais vous pouvez surmonter cela en utilisant une clé spéciale dans un objet. JavaScript convertit automatiquement toute clé que vous entrez en une chaîne, même la clé "age". Par conséquent, les objets en JavaScript sont un dictionnaire de clés de chaîne et de valeurs de n'importe quel type.

```javascript
let person = {
  last name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

Pour utiliser "last name" comme clé dans le code ci-dessus, vous devez informer JavaScript que c'est une clé en l'enfermant dans des guillemets, simples ou doubles. Utiliser un nom qui peut également être utilisé comme variable est recommandé au lieu de cette méthode d'exception pour définir une clé.

```javascript
let person = {
  'last name':'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

Utiliser des guillemets simples pour entourer "last name" et l'utiliser comme nom de clé est un code JavaScript valide et fonctionnera correctement.

### Comment accéder aux propriétés avec des crochets

Pour ajouter et modifier des propriétés dans un objet, vous pouvez utiliser la méthode de notation d'objet. Cependant, il existe une autre méthode en JavaScript pour accéder aux propriétés d'objet, connue sous le nom de notation par crochets, qui vous permet d'accéder à une propriété créée par une **clé spéciale** en JavaScript.

```javascript
let person = {
  'last name':'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
}
// console.log(person.last name); n'est pas valide en JavaScript
```

Vous ne pouvez pas accéder au nom de clé 'last name' en utilisant la méthode de notation par point, mais vous pouvez utiliser la notation par crochets, qui est disponible pour n'importe quel objet.

```javascript
console.log(person['last name']);
```

Le code ci-dessus affichera la valeur de la clé last name qui est `kamal`. Cependant, il est crucial d'enfermer votre clé dans des guillemets simples ou doubles.

### Comment définir dynamiquement des propriétés

Vous pouvez activer une autre fonctionnalité dynamique avec des crochets et des objets en JavaScript. Cela fonctionne lorsque vous devez définir une nouvelle propriété, surtout lorsque vous ne connaissez pas le nom de la propriété.

Par exemple, vous ne connaîtrez pas les entrées spécifiques de l'utilisateur à l'avance. Mais vous devrez ajouter la propriété avec ce nom à l'objet.

```javascript
const userName ='level';

let person = {
 'first name':'kamal',
  age:30,
  [userName]: 'see',
}
console.log(person);
```

En n'enfermant pas le **userName** dans un crochet, la propriété avec le nom userName sera ajoutée au lieu de la valeur stockée à l'intérieur. Ajouter un crochet au **userName** recherchera et prendra la valeur stockée dans la variable comme nom de clé et l'ajoutera à un objet person.

### Syntaxe abrégée des méthodes

Il existe une syntaxe alternative que vous pouvez utiliser pour définir une méthode de manière plus efficace. Traditionnellement, pour créer une méthode dans un objet, vous avez besoin d'une clé et d'une valeur, où vous créez la valeur comme une méthode en utilisant le mot-clé function.

```javascript
let person = {
  name:'jamaldeen',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ],
  speek:function(){
    return this.hobbies
  }
}
console.log(person.speak());
```

Dans le code ci-dessus, la méthode est créée avec un mot-clé function après un deux-points. Alternativement, vous pourriez faire ceci :

```javascript
let person = {
  name:'jamaldeen',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ],
  speek(){
    return this.hobbies
  }
}
console.log(person.speak());
```

En JavaScript, la création d'une méthode avec des méthodes courtes d'objet est une notation abrégée. Omettre le mot-clé "function" et le deux-points (:) avant le corps de la fonction est autorisé en utilisant les méthodes courtes.

Cela est dû au fait qu'avec la syntaxe des méthodes courtes, la propriété est automatiquement définie comme méthode, ce qui rend le mot-clé "function" inutile.

Le code reste fonctionnel car le moteur JavaScript reconnaît la syntaxe abrégée et l'interprète comme une définition de fonction régulière.

### Avantages de l'utilisation des méthodes courtes d'objet par rapport aux méthodes régulières.

Certains des avantages de l'utilisation des méthodes courtes d'objet par rapport aux méthodes régulières sont les suivants :

1. Concis : Contrairement aux méthodes régulières, les méthodes courtes d'objet vous permettent d'écrire un code plus compact et lisible.
2. Performance améliorée : Bien que la performance des méthodes courtes d'objet et des méthodes régulières soit similaire, la syntaxe plus courte facilite l'écriture et la maintenance de votre code.
3. Réutilisabilité : Vous pouvez facilement réutiliser les méthodes courtes d'objet dans d'autres objets.
4. Meilleure organisation : Avec les méthodes courtes d'objet, vous pouvez facilement regrouper des méthodes liées au sein d'un objet et garder votre code organisé.

Bien que l'utilisation des méthodes courtes d'objet soit bonne, l'utilisation de méthodes régulières peut encore être plus appropriée. Il est important de choisir la bonne approche en fonction de vos exigences particulières.

### Opérateur de propagation d'objet

L'opérateur de propagation d'objet est une syntaxe populaire et puissante en JavaScript. L'opérateur de propagation prend toutes les paires clé-valeur d'un objet et copie le nom de la clé et la valeur dans un nouvel objet.

Un objet est une valeur de référence, et si vous voulez une copie de l'objet sans pointer vers la même propriété en mémoire, l'opérateur de propagation est la réponse.

```javascript
let person = {
  name:'kamal',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ]
}
console.log(person);
const person2 ={...person};
console.log(person2.age);
```

La syntaxe de l'opérateur de propagation d'objet se place entre les crochets d'ouverture et de fermeture. Ensuite, il doit y avoir trois points et l'objet que vous souhaitez propager dans cet objet.

### Destructuration d'objet

La destructuration d'objet est une fonctionnalité importante en JavaScript qui vous permet d'extraire des valeurs d'un objet et de les assigner à des variables individuelles.

Pour effectuer une destructuration d'objet, vous utilisez un motif de destructuration du côté gauche d'une instruction d'assignation, et l'objet dont vous souhaitez extraire les valeurs du côté droit. Par exemple :

```javascript
const person = { name: 'lawal', age: 39 };
const { person, age } = person;
console.log(name); // 'lawal'
console.log(age); // 39

```

L'instruction `const` utilise la destructuration d'objet pour extraire les propriétés `name` et `age` de l'objet `person` et les assigner à deux variables séparées. C'est une manière concise et efficace d'extraire des valeurs d'un objet, surtout lorsque vous traitez avec des objets complexes.

La destructuration d'objet vous permet également de fournir des valeurs par défaut, au cas où la propriété que vous souhaitez extraire n'existe pas dans l'objet. Vous pouvez également renommer les variables extraites en utilisant un alias, ce qui vous donne un meilleur contrôle sur la structure et le nommage des valeurs extraites.

## Comment utiliser le mot-clé `this` en JavaScript

Qu'est-ce que le mot-clé `this` ? `this` est un mot-clé spécifique en JavaScript qui est le plus important lorsqu'il est utilisé à l'intérieur d'une fonction dans un objet. Mais vous pouvez l'utiliser n'importe où dans votre code en dehors du corps de la fonction d'un objet.

`this` est un mot-clé puissant utilisé pour référencer l'objet courant dans lequel il est utilisé.

```javascript
let person = {
  name:'kamal',
  age:30,
  greet:function(){
    return `My name is ${this.name}, and my age is ${this.age} years old`;
  },
}
console.log(person.greet());
// My name is kamal, and my age is 30 years old.
```

Le code ci-dessus démontre que le mot-clé "this" fait référence à l'objet contenant la fonction, dans ce cas l'objet "person", et le résultat affiche la sortie de la fonction "greet".

Quelle que soit sa position au sein d'un objet, le mot-clé `this` fait toujours référence à l'entité qui a exécuté la fonction dans le code. L'utilisation de `this` dans différents contextes au sein du code peut produire des résultats distincts. Par exemple :

```javascript
let person = {
  name:'kamal',
  age:30,
  greet:function(){
    return `My name is ${this.name}, and my age is ${this.age} years old`;
  },
}
console.log(this);
```

La sortie du code montre que le mot-clé `this` lorsqu'il est journalisé dans la console affichera un objet window.

## Conclusion

Dans ce tutoriel, nous avons appris ce qu'est un objet JavaScript, comment créer un objet et comment modifier/supprimer des propriétés dans un objet.

Nous avons brièvement parlé de l'importance de l'opérateur de propagation et de la destructuration d'objet dans les objets JavaScript ainsi que du mot-clé populaire `this` et de son utilisation dans les objets JavaScript.