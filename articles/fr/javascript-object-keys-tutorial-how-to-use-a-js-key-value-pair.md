---
title: Tutoriel sur les clés d'objets JavaScript – Comment utiliser une paire clé-valeur
  JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-11T18:35:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-object-keys-tutorial-how-to-use-a-js-key-value-pair
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/objects.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Tutoriel sur les clés d'objets JavaScript – Comment utiliser une paire
  clé-valeur JS
seo_desc: "By Amy Haddad\nYou can group related data together into a single data structure\
  \ by using a JavaScript object, like this:\nconst desk = {\n   height: \"4 feet\"\
  ,\n   weight: \"30 pounds\",\n   color: \"brown\",\n   material: \"wood\",\n };\n\
  \nAn object contains proper..."
---

Par Amy Haddad

Vous pouvez regrouper des données liées ensemble dans une seule structure de données en utilisant un objet JavaScript, comme ceci :

```JavaScript
const desk = {
   height: "4 feet",
   weight: "30 pounds",
   color: "brown",
   material: "wood",
};
```

Un objet contient des propriétés, ou paires clé-valeur. L'objet `desk` ci-dessus a quatre propriétés. Chaque propriété a un nom, qui est aussi appelé une clé, et une valeur correspondante. 

Par exemple, la clé `height` a la valeur `"4 feet"`. Ensemble, la clé et la valeur constituent une seule propriété. 

```JavaScript
height: "4 feet",
```

L'objet `desk` contient des données sur un bureau. En fait, c'est une raison pour laquelle vous utiliseriez un objet JavaScript : pour stocker des données. Il est également simple de récupérer les données que vous stockez dans un objet. Ces aspects rendent les objets très utiles. 

Cet article vous permettra de démarrer avec les objets JavaScript :

* comment créer un objet 
* comment stocker des données dans un objet
* et récupérer des données à partir de celui-ci.

Commençons par créer un objet.

# Comment créer un objet en JavaScript

Je vais créer un objet appelé `pizza` ci-dessous, et ajouter des paires clé-valeur à celui-ci. 

```javaScript
const pizza = {
   topping: "cheese",
   sauce: "marinara",
   size: "small"
};
```

Les clés sont à gauche du deux-points `:` et les valeurs sont à droite de celui-ci. Chaque paire clé-valeur est une `propriété`. Il y a trois propriétés dans cet exemple :

* La clé **topping** a une valeur **"cheese"**.
* La clé **sauce** a une valeur **"marinara"**.
* La clé **size** a une valeur **"small"**.

Chaque propriété est séparée par une virgule. Toutes les propriétés sont enveloppées dans des accolades. 

C'est la syntaxe de base de l'objet. Mais il y a quelques règles à garder à l'esprit lors de la création d'objets JavaScript.

### Clés d'objet en JavaScript

Chaque clé dans votre objet JavaScript doit être une chaîne de caractères, un symbole ou un nombre.

Examinez de près l'exemple ci-dessous. Les noms de clés **`1`** et **`2`** sont en fait convertis en chaînes de caractères.

```javaScript 
const shoppingCart = {
   1: "apple",
   2: "oranges"
};
```

C'est une différence qui devient claire lorsque vous imprimez l'objet.

```javaScript 
console.log(shoppingCart);
//Résultat: { '1': 'apple', '2': 'oranges' }
```

Il y a une autre règle à garder à l'esprit concernant les noms de clés : si votre nom de clé contient des espaces, vous devez l'envelopper dans des guillemets.

Regardez l'objet `programmer` ci-dessous. Remarquez le dernier nom de clé, `"current project name"`. Ce nom de clé contient des espaces, donc je l'ai enveloppé dans des guillemets.

```javaScript
const programmer = {
   firstname: "Phil",
   age: 21,
   backendDeveloper: true,
   languages: ["Python", "JavaScript", "Java", "C++"],
   "current project name": "The Amazing App"
};
```

### Valeurs d'objet en JavaScript

Une valeur, en revanche, peut être de n'importe quel type de données, y compris un tableau, un nombre ou un booléen. Les valeurs dans l'exemple ci-dessus contiennent ces types : chaîne de caractères, entier, booléen et un tableau.

Vous pouvez même utiliser une fonction comme valeur, auquel cas elle est connue sous le nom de méthode. `sounds()`, dans l'objet ci-dessous, est un exemple. 

```javaScript 
const animal = {
   type: "cat",
   name: "kitty",
   sounds() { console.log("meow meow") }
};
```

Maintenant, disons que vous voulez ajouter ou supprimer une paire clé-valeur. Ou vous voulez simplement récupérer la valeur d'un objet.

Vous pouvez faire ces choses en utilisant la notation par point ou par crochets, que nous allons aborder ensuite.

# Comment la notation par point et la notation par crochets fonctionnent en JavaScript

La notation par point et la notation par crochets sont deux façons d'accéder et d'utiliser les propriétés d'un objet. Vous allez probablement utiliser plus souvent la notation par point, alors commençons par celle-ci.

### Comment ajouter une paire clé-valeur avec la notation par point en JavaScript

Je vais créer un objet `book` vide ci-dessous.

```JavaScript
const book = {};
```

Pour ajouter une paire clé-valeur en utilisant la notation par point, utilisez la syntaxe :

 `objectName.keyName = value`

Voici le code pour ajouter la clé (author) et la valeur ("Jane Smith") à l'objet `book` : 

```JavaScript
book.author = "Jane Smith";
```

Voici une décomposition du code ci-dessus :

* `book` est le nom de l'objet
* `.` (point)
* `author` est le nom de la clé 
* `=` (égal)
* `"Jane Smith"` est la valeur

Lorsque j'imprime l'objet book, je verrai la nouvelle paire clé-valeur ajoutée.

```javaScript 
console.log(book);
//Résultat: { author: 'Jane Smith' }
```

Je vais ajouter une autre paire clé-valeur à l'objet `book`.

```JavaScript
book.publicationYear = 2006;
```

L'objet `book` a maintenant deux propriétés.

```javaScript 
console.log(book);
//Résultat: { author: 'Jane Smith', publicationYear: 2006 }
```

### Comment accéder aux données dans un objet JavaScript en utilisant la notation par point

Vous pouvez également utiliser la notation par point sur une clé pour _accéder_ à la valeur associée. 

Considérez cet objet `basketballPlayer`.

```javaScript
const basketballPlayer = {
   name: "James",
   averagePointsPerGame: 20,
   height: "6 feet, 2 inches",
   position: "shooting guard"
};
```

Disons que vous voulez récupérer la valeur "shooting guard". Voici la syntaxe à utiliser : 

`objectName.keyName`

Utilisons cette syntaxe pour obtenir et imprimer la valeur "shooting guard".

```javaScript
console.log(basketballPlayer.position);
//Résultat: shooting guard
```

Voici une décomposition du code ci-dessus :

* `basketballPlayer` est le nom de l'objet
* `.` (point)
* `position` est le nom de la clé

Voici un autre exemple.

```javaScript
console.log(basketballPlayer.name);
//Résultat: James
```

### Comment supprimer une paire clé-valeur en JavaScript

Pour supprimer une paire clé-valeur, utilisez l'opérateur `delete`. Voici la syntaxe : 

`delete objectName.keyName`

Donc, pour supprimer la clé `height` et sa valeur de l'objet `basketballPlayer`, vous écriviez ce code : 

```JavaScript
delete basketballPlayer.height;
```

En conséquence, l'objet `basketballPlayer` a maintenant trois paires clé-valeur.

```javaScript
console.log(basketballPlayer);
//Résultat: { name: 'James', averagePointsPerGame: 20, position: 'shooting guard' }
```

Vous allez probablement utiliser souvent la notation par point, bien qu'il y ait certaines exigences à connaître.

Lorsque vous utilisez la notation par point, les noms de clés ne peuvent pas contenir d'espaces, de traits d'union ou commencer par un nombre.

Par exemple, disons que j'essaie d'ajouter une clé qui contient des espaces en utilisant la notation par point. Je vais obtenir une erreur.

```javaScript
basketballPlayer.shooting percentage = "75%";
//Résulte en une erreur
```

Donc, la notation par point ne fonctionnera pas dans toutes les situations. C'est pourquoi il y a une autre option : la notation par crochets.

### Comment ajouter une paire clé-valeur en utilisant la notation par crochets en JavaScript

Tout comme la notation par point, vous pouvez utiliser la notation par crochets pour ajouter une paire clé-valeur à un objet. 

La notation par crochets offre plus de flexibilité que la notation par point. C'est parce que les noms de clés _peuvent_ inclure des espaces et des traits d'union, et ils peuvent commencer par des nombres.

Je vais créer un objet `employee` ci-dessous.

```JavaScript
const employee = {};
```

Maintenant, je veux ajouter une paire clé-valeur en utilisant la notation par crochets. Voici la syntaxe : 

`objectName["keyName"] = value`

Donc, voici comment j'ajouterais la clé (occupation) et la valeur (sales) à l'objet employee : 

```JavaScript
employee["occupation"] = "sales";
```

Voici une décomposition du code ci-dessus :

* `employee` est le nom de l'objet
* `"occupation"` est le nom de la clé 
* `=` (égal)
* `"sales"` est la valeur

Voici plusieurs autres exemples qui utilisent la flexibilité de la notation par crochets pour ajouter une variété de paires clé-valeur.

```javaScript
//Ajouter un nom de clé en plusieurs mots
employee["travels frequently"] = true;
 
//Ajouter un nom de clé qui commence par un nombre et inclut un trait d'union
employee["1st-territory"] = "Chicago";
 
//Ajouter un nom de clé qui commence par un nombre
employee["25"] = "total customers";
```

Lorsque j'imprime l'objet `employee`, il ressemble à ceci :

```javaScript
{
  '25': 'total customers',
  occupation: 'sales',
  'travels frequently': true,
  '1st-territory': 'Chicago'
}
```

Avec cette information en tête, nous pouvons ajouter la clé "shooting percentage" à l'objet `basketballPlayer` de ci-dessus.

```javaScript
const basketballPlayer = {
   name: "James",
   averagePointsPerGame: 20,
   height: "6 feet, 2 inches",
   position: "shooting guard"
};
```

Vous vous souvenez peut-être que la notation par point nous a laissé avec une erreur lorsque nous avons essayé d'ajouter une clé qui incluait des espaces.

```javaScript
basketballPlayer.shooting percentage = "75%";
//Résulte en une erreur
```

Mais la notation par crochets nous laisse sans erreur, comme vous pouvez le voir ici :

```javaScript
basketballPlayer["shooting percentage"] = "75%";
```

Voici le résultat lorsque j'imprime l'objet :

```javaScript 
{
  name: 'James',
  averagePointsPerGame: 20,
  height: '6 feet, 2 inches',
  position: 'shooting guard',
  'shooting percentage': '75%'
}
```

### Comment accéder aux données dans un objet JavaScript en utilisant la notation par crochets

Vous pouvez également utiliser la notation par crochets sur une clé pour _accéder_ à la valeur associée.

Rappelons l'objet `animal` du début de l'article.

```JavaScript
const animal = {
   type: "cat",
   name: "kitty",
   sounds() { console.log("meow meow") }
};
```

Obtenons la valeur associée à la clé, `name`. Pour ce faire, enveloppez le nom de la clé dans des guillemets et mettez-le entre crochets. Voici la syntaxe : 

`objectName["keyName"]`

Voici le code que vous écriviez avec la notation par crochets : `animal["name"];`.	

Voici une décomposition du code ci-dessus :

* `animal` est le nom de l'objet
* `["name"]` est le nom de la clé enfermé dans des crochets

Voici un autre exemple.

```javaScript
console.log(animal["sounds"]());

//Résultat: 
meow meow
undefined
```

Notez que `sounds()` est une méthode, c'est pourquoi j'ai ajouté les parenthèses à la fin pour l'invoquer.

Voici comment vous invoqueriez une méthode en utilisant la notation par point.

```javaScript
console.log(animal.sounds());

//Résultat: 
meow meow
undefined
```

# Méthodes d'objet JavaScript

Vous savez comment accéder à des propriétés spécifiques. Mais que faire si vous voulez _toutes_ les clés ou _toutes_ les valeurs d'un objet ?

Il y a deux méthodes qui vous donneront les informations dont vous avez besoin.

```JavaScript
const runner = {
   name: "Jessica",
   age: 20,
   milesPerWeek: 40,
   race: "marathon"
};
```

Utilisez la méthode `Object.keys()` pour récupérer tous les noms de clés d'un objet.

Voici la syntaxe :

`Object.keys(objectName)`

Nous pouvons utiliser cette méthode sur l'objet `runner` ci-dessus.

```JavaScript
Object.keys(runner);
```

Si vous imprimez le résultat, vous obtiendrez un tableau des clés de l'objet.

```JavaScript
console.log(Object.keys(runner));
//Résultat: [ 'name', 'age', 'milesPerWeek', 'race' ]
```

De même, vous pouvez utiliser la méthode `Object.values()` pour obtenir toutes les valeurs d'un objet. Voici la syntaxe : 

`Object.values(objectName)`

Maintenant, nous allons obtenir toutes les valeurs de l'objet `runner`.

```JavaScript
console.log(Object.values(runner));
//Résultat: [ 'Jessica', 20, 40, 'marathon' ]
```

Nous avons couvert beaucoup de terrain. Voici un résumé des idées clés :

**Objets :**

* Utilisez des objets pour stocker des données sous forme de propriétés (paires clé-valeur).
* Les noms de clés doivent être des chaînes de caractères, des symboles ou des nombres.
* Les valeurs peuvent être de n'importe quel type.

**Accéder aux propriétés d'un objet :**

* Notation par point : `objectName.keyName`
* Notation par crochets : `objectName["keyName"]`

**Supprimer une propriété :**

* `delete objectName.keyName`  


Il y a beaucoup de choses que vous pouvez faire avec des objets. Et maintenant vous avez quelques bases pour tirer parti de ce type de données puissant de JavaScript.  


_Je parle de l'apprentissage de la programmation, et des meilleures façons de s'y prendre sur [amymhaddad.com](http://amymhaddad.com/)._ Je tweete également sur la programmation, l'apprentissage et la productivité : [@amymhaddad](https://twitter.com/amymhaddad).