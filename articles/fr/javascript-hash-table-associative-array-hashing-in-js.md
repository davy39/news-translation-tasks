---
title: Table de hachage JavaScript – Le hachage de tableaux associatifs en JS
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-05-11T15:24:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-hash-table-associative-array-hashing-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/JavaScript-Hash-Table.png
tags:
- name: data structures
  slug: data-structures
- name: Hash tables
  slug: hash-tables
- name: JavaScript
  slug: javascript
seo_title: Table de hachage JavaScript – Le hachage de tableaux associatifs en JS
seo_desc: 'Hash Tables are a data structure that allow you to create a list of paired
  values. You can then retrieve a certain value by using the key for that value, which
  you put into the table beforehand.

  A Hash Table transforms a key into an integer index usi...'
---

Les tables de hachage (Hash Tables) sont une structure de données qui vous permet de créer une liste de valeurs appariées. Vous pouvez ensuite récupérer une certaine valeur en utilisant la clé correspondante, que vous avez préalablement insérée dans la table.

Une table de hachage transforme une clé en un index entier à l'aide d'une fonction de hachage, et cet index déterminera l'emplacement où stocker la paire clé/valeur en mémoire :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/g983.jpg)
_Table de hachage pour le stockage d'annuaires téléphoniques (de [Wikipedia](https://en.wikipedia.org/wiki/Hash_table))_

On utilise couramment une table de hachage en raison de la rapidité de ses opérations de recherche, d'insertion et de suppression :

||Complexité temporelle de la table de hachage en notation Grand O||
|:-------------------:|:-------:|:----------:|
|       Algorithme     | Moyenne | Pire cas |
|         Espace       |   O(n)  |    O(n)    |
|         Recherche    |   O(1)  |    O(n)    |
|         Insertion    |   O(1)  |    O(n)    |
|         Suppression  |   O(1)  |    O(n)    |

<small>Source : [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)</small>

Ce tutoriel vous aidera à comprendre l'implémentation des tables de hachage en JavaScript ainsi que la manière dont vous pouvez construire votre propre classe `HashTable`. 

Tout d'abord, examinons les classes `Object` et `Map` de JavaScript.

## Comment utiliser les tables de hachage avec les classes Object et Map en JavaScript

L'exemple le plus courant de table de hachage en JavaScript est le type de données `Object`, où vous pouvez coupler la valeur d'une propriété de l'objet avec une clé de propriété.

Dans l'exemple suivant, la clé `Nathan` est couplée à la valeur du numéro de téléphone `"555-0182"` et la clé `Jane` est couplée à la valeur `"315-0322"` :

```js
let obj = {
  Nathan: "555-0182",
  Jane: "315-0322"
}
```

Mais le type `Object` de JavaScript est une implémentation particulière de table de hachage pour deux raisons :

* Il possède des propriétés ajoutées par la classe `Object`. Les clés que vous saisissez peuvent entrer en conflit et écraser les propriétés par défaut héritées de la classe.
* La taille de la table de hachage n'est pas suivie. Vous devez compter manuellement le nombre de propriétés définies par le programmeur au lieu de celles héritées du prototype.

Par exemple, le prototype `Object` possède la méthode `hasOwnProperty()` qui vous permet de vérifier si une propriété n'est pas héritée :

```js
const obj = {};
obj.name = "Nathan";

console.log(obj.hasOwnProperty("name")); // true
```

JavaScript ne bloque pas une tentative d'écrasement de la méthode `hasOwnProperty()`, ce qui peut provoquer une erreur comme celle-ci :

```js
const obj = {};
obj.name = "Nathan";
obj.hasOwnProperty = true;

console.log(obj.hasOwnProperty("name")); 
// Erreur : obj.hasOwnProperty n'est pas une fonction
```

Pour remédier à ces lacunes, JavaScript a créé une autre implémentation de la structure de données de table de hachage appelée `Map`.

Tout comme `Object`, `Map` vous permet de stocker des paires clé-valeur à l'intérieur de la structure de données. Voici un exemple de `Map` en action :

```js
const collection = new Map();

collection.set("Nathan", "555-0182");
collection.set("Jane", "555-0182");

console.log(collection.get("Nathan")); // 555-0182
console.log(collection.size); // 2
```

Contrairement au type `Object`, `Map` vous oblige à utiliser les méthodes `set()` et `get()` pour définir et récupérer les paires clé-valeur que vous souhaitez ajouter à la structure de données. 

Vous ne pouvez pas non plus écraser les propriétés héritées de `Map`. Par exemple, le code suivant tente d'écraser la valeur de la propriété `size` par `false` :

```js
const collection = new Map();

collection.set("Nathan", "555-0182");
collection["size"] = false;

console.log(collection.get("size")); // undefined
console.log(collection.size); // 1
```

Comme vous pouvez le voir dans le code ci-dessus, vous ne pouvez pas ajouter une nouvelle entrée à l'objet `Map` sans utiliser la méthode `set()`.

La structure de données `Map` est également itérable, ce qui signifie que vous pouvez boucler sur les données comme suit :

```js
const myMap = new Map();

myMap.set("Nathan", "555-0182");
myMap.set("Jane", "315-0322");

for (let [key, value] of myMap) {
  console.log(`${key} = ${value}`);
}
```

Maintenant que vous avez appris comment JavaScript implémente les tables de hachage sous la forme des structures de données `Object` et `Map`, voyons comment vous pouvez créer votre propre implémentation de table de hachage.

## Comment implémenter une structure de données de table de hachage en JavaScript

Bien que JavaScript dispose déjà de deux implémentations de tables de hachage, écrire votre propre implémentation est l'une des questions d'entretien JavaScript les plus courantes.

Vous pouvez implémenter une table de hachage en JavaScript en trois étapes :

* Créer une classe `HashTable` avec les propriétés initiales `table` et `size`
* Ajouter une fonction `hash()` pour transformer les clés en indices
* Ajouter les méthodes `set()` et `get()` pour ajouter et récupérer des paires clé/valeur de la table.

D'accord, commençons par créer la classe `HashTable`. Le code ci-dessous créera une `table` de compartiments (buckets) d'une taille de `127` :

```js
class HashTable {
  constructor() {
    this.table = new Array(127);
    this.size = 0;
  }
}
```

Toutes vos paires clé/valeur seront stockées à l'intérieur de la propriété `table`.

### Comment écrire la méthode hash()

Ensuite, vous devez créer la méthode `hash()` qui acceptera une valeur `key` et la transformera en un index. 

Une façon simple de créer le hachage serait de sommer le code ASCII des caractères de la clé en utilisant la méthode `charCodeAt()` comme suit. Notez que la méthode est nommée avec un `_` pour indiquer qu'il s'agit d'une méthode privée :

```js
_hash(key) {
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash += key.charCodeAt(i);
  }
  return hash;
}
```

Mais comme la classe `HashTable` ne possède que 127 compartiments, cela signifie que la méthode `_hash()` doit renvoyer un nombre compris entre `0 et 127`.

Pour garantir que la valeur de hachage ne dépasse pas la taille des compartiments, vous devez utiliser l'opérateur modulo comme indiqué ci-dessous :

```js
_hash(key) {
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash += key.charCodeAt(i);
  }
  return hash % this.table.length;
}
```

 Maintenant que vous avez terminé la méthode `_hash()`, il est temps d'écrire les méthodes `set()` et `get()`.

### Comment écrire la méthode set()

Pour définir la paire clé/valeur dans votre table de hachage, vous devez écrire une méthode `set()` qui accepte `(key, value)` comme paramètres :

* La méthode `set()` appellera la méthode `_hash()` pour obtenir la valeur de l'index (`index`). 
* La paire `[key, value]` sera assignée à la `table` à l'index spécifié.
* Ensuite, la propriété `size` sera incrémentée de un.

```js
set(key, value) {
  const index = this._hash(key);
  this.table[index] = [key, value];
  this.size++;
}
```

Maintenant que la méthode `set()` est terminée, écrivons la méthode `get()` pour récupérer une valeur par sa clé.

### Comment écrire la méthode get()

Pour obtenir une certaine valeur de la table de hachage, vous devez écrire une méthode `get()` qui accepte une valeur `key` comme paramètre :

* La méthode appellera la méthode `_hash()` pour récupérer à nouveau l'index de la table.
* Elle renverra la valeur stockée à `table[index]`.

```js
get(key) {
  const index = this._hash(key);
  return this.table[index];
}
```

De cette façon, la méthode `get()` renverra soit la paire clé/valeur, soit `undefined` lorsqu'aucune paire clé/valeur n'est stockée à l'index spécifié.

Jusqu'ici, tout va bien. Ajoutons ensuite une autre méthode pour supprimer une paire clé/valeur de la table de hachage.

### Comment écrire la méthode remove()

Pour supprimer une paire clé/valeur de la table de hachage, vous devez écrire une méthode `remove()` qui accepte une valeur `key` comme paramètre :

* Récupérer le bon `index` en utilisant la méthode `_hash()`.
* Vérifier si `table[index]` a une valeur truthy et si la propriété `length` est supérieure à zéro. Assigner la valeur `undefined` au bon `index` et décrémenter la propriété `size` de un si c'est le cas.
* Sinon, renvoyer simplement `false`.

```js
remove(key) {
  const index = this._hash(key);

  if (this.table[index] && this.table[index].length) {
    this.table[index] = undefined;
    this.size--;
    return true;
  } else {
    return false;
  }
}
```

Grâce à cela, vous disposez maintenant d'une méthode `remove()` fonctionnelle. Voyons si la classe `HashTable` fonctionne correctement.

## Comment tester l'implémentation de la table de hachage

Il est temps de tester l'implémentation de la table de hachage. Voici à nouveau le code complet de l'implémentation de la table de hachage :

```js
class HashTable {
  constructor() {
    this.table = new Array(127);
    this.size = 0;
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash += key.charCodeAt(i);
    }
    return hash % this.table.length;
  }

  set(key, value) {
    const index = this._hash(key);
    this.table[index] = [key, value];
    this.size++;
  }

  get(key) {
    const target = this._hash(key);
    return this.table[target];
  }

  remove(key) {
    const index = this._hash(key);

    if (this.table[index] && this.table[index].length) {
      this.table[index] = [];
      this.size--;
      return true;
    } else {
      return false;
    }
  }
}
```

Pour tester la classe `HashTable`, je vais créer une nouvelle instance de la classe et définir quelques paires clé/valeur comme indiqué ci-dessous. Les paires clé/valeur ci-dessous sont simplement des valeurs numériques arbitraires associées à des noms de pays sans signification particulière :

```js
const ht = new HashTable();
ht.set("Canada", 300);
ht.set("France", 100);
ht.set("Spain", 110);
```

Ensuite, essayons de les récupérer en utilisant la méthode `get()` :

```js
console.log(ht.get("Canada")); // [ 'Canada', 300 ]
console.log(ht.get("France")); // [ 'France', 100 ]
console.log(ht.get("Spain")); // [ 'Spain', 110 ]
```

Enfin, essayons de supprimer l'une de ces valeurs avec la méthode `remove()` :

```js
console.log(ht.remove("Spain")); // true
console.log(ht.get("Spain")); // undefined
```

Très bien, toutes les méthodes fonctionnent comme prévu. Essayons une autre insertion avec une nouvelle instance de `HashTable` et récupérons ces valeurs :

```js
const ht = new HashTable();

ht.set("Spain", 110);
ht.set("ǻ", 192);

console.log(ht.get("Spain")); // [ 'ǻ', 192 ]
console.log(ht.get("ǻ")); // [ 'ǻ', 192 ]
```

Oups ! On dirait que nous avons un problème ici. 😨

## Comment gérer les collisions d'index

Parfois, la fonction de hachage d'une table de hachage peut renvoyer le même numéro d'index. Dans le cas de test ci-dessus, la chaîne `"Spain"` et `"ǻ"` **renvoient toutes deux la même valeur de hachage** car le nombre `507` est la somme de leurs deux codes ASCII.

La même valeur de hachage provoquera une _collision_ d'index, écrasant l'entrée précédente par la nouvelle.

Actuellement, les données stockées dans notre implémentation de table de hachage ressemblent à ceci :

```js
[
    [ "Spain", 110],
    [ "France", 100]
]
```

Pour gérer la collision des numéros d'index, vous devez stocker la paire clé/valeur dans un second tableau afin que le résultat final ressemble à ceci :

```js
[
    [
        [ "Spain", 110 ],
        [ "ǻ", 192 ]
    ],
    [
        ["France", 100]
    ],
]
```

Pour créer ce second tableau, vous devez mettre à jour la méthode `set()` afin qu'elle :

* Regarde dans `table[index]` et boucle sur les valeurs du tableau.
* Si la clé de l'un des tableaux est égale à la `key` passée à la méthode, remplace la valeur à l'index `1` et arrête toute exécution ultérieure avec l'instruction `return`.
* Si aucune clé correspondante n'est trouvée, ajoute un nouveau tableau de clé et de valeur au second tableau.
* Sinon, initialise un nouveau tableau et ajoute la paire clé/valeur à l'index spécifié.
* Chaque fois qu'une méthode `push()` est appelée, incrémente la propriété `size` de un.

Le code complet de la méthode `set()` sera le suivant :

```js
set(key, value) {
  const index = this._hash(key);
  if (this.table[index]) {
    for (let i = 0; i < this.table[index].length; i++) {
      // Trouver la paire clé/valeur dans la chaîne
      if (this.table[index][i][0] === key) {
        this.table[index][i][1] = value;
        return;
      }
    }
    // non trouvé, ajouter une nouvelle paire clé/valeur
    this.table[index].push([key, value]);
  } else {
    this.table[index] = [];
    this.table[index].push([key, value]);
  }
  this.size++;
}
```

Ensuite, mettez à jour la méthode `get()` afin qu'elle vérifie également le tableau de second niveau avec une boucle `for` et renvoie la bonne paire clé/valeur :

```js
get(key) {
  const target = this._hash(key);
  if (this.table[target]) {
    for (let i = 0; i < this.table.length; i++) {
      if (this.table[target][i][0] === key) {
        return this.table[target][i][1];
      }
    }
  }
  return undefined;
}
```

Enfin, vous devez mettre à jour la méthode `remove()` afin qu'elle boucle sur le tableau de second niveau et supprime le tableau avec la bonne valeur de `key` en utilisant la méthode `splice()` :

```js
remove(key) {
  const index = this._hash(key);

  if (this.table[index] && this.table[index].length) {
    for (let i = 0; i < this.table.length; i++) {
      if (this.table[index][i][0] === key) {
        this.table[index].splice(i, 1);
        this.size--;
        return true;
      }
    }
  } else {
    return false;
  }
}
```

Grâce à cela, votre classe `HashTable` pourra éviter toute collision de numéros d'index et stocker la paire clé/valeur à l'intérieur du tableau de second niveau.

En bonus, ajoutons une méthode `display()` qui affichera toutes les paires clé/valeur stockées dans la table de hachage. Il vous suffit d'utiliser la méthode `forEach()` pour itérer sur la table et d'utiliser `map()` pour transformer les valeurs en une chaîne de caractères comme indiqué ci-dessous :

```js
display() {
  this.table.forEach((values, index) => {
    const chainedValues = values.map(
      ([key, value]) => `[ ${key}: ${value} ]`
    );
    console.log(`${index}: ${chainedValues}`);
  });
}
```

Voici à nouveau le code complet de la classe `HashTable` avec l'évitement de collision appliqué pour votre référence :

```js
class HashTable {
  constructor() {
    this.table = new Array(127);
    this.size = 0;
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash += key.charCodeAt(i);
    }
    return hash % this.table.length;
  }

  set(key, value) {
    const index = this._hash(key);
    if (this.table[index]) {
      for (let i = 0; i < this.table[index].length; i++) {
        if (this.table[index][i][0] === key) {
          this.table[index][i][1] = value;
          return;
        }
      }
      this.table[index].push([key, value]);
    } else {
      this.table[index] = [];
      this.table[index].push([key, value]);
    }
    this.size++;
  }

  get(key) {
    const index = this._hash(key);
    if (this.table[index]) {
      for (let i = 0; i < this.table.length; i++) {
        if (this.table[index][i][0] === key) {
          return this.table[index][i][1];
        }
      }
    }
    return undefined;
  }

  remove(key) {
    const index = this._hash(key);

    if (this.table[index] && this.table[index].length) {
      for (let i = 0; i < this.table.length; i++) {
        if (this.table[index][i][0] === key) {
          this.table[index].splice(i, 1);
          this.size--;
          return true;
        }
      }
    } else {
      return false;
    }
  }

  display() {
    this.table.forEach((values, index) => {
      const chainedValues = values.map(
        ([key, value]) => `[ ${key}: ${value} ]`
      );
      console.log(`${index}: ${chainedValues}`);
    });
  }
}
```

Vous pouvez tester l'implémentation en créant une nouvelle instance de `HashTable` et en effectuant quelques insertions et suppressions :

```js
const ht = new HashTable();

ht.set("France", 111);
ht.set("Spain", 150);
ht.set("ǻ", 192);

ht.display();
// 83: [ France: 111 ]
// 126: [ Spain: 150 ],[ ǻ: 192 ]

console.log(ht.size); // 3
ht.remove("Spain");
ht.display();
// 83: [ France: 111 ]
// 126: [ ǻ: 192 ]
```

Désormais, il n'y a plus de collision au sein de l'instance `HashTable`. Beau travail !

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est une table de hachage et comment JavaScript l'utilise pour créer les structures de données `Object` et `Map`.

Vous avez également appris à implémenter votre propre classe `HashTable` ainsi qu'à empêcher la collision des indices de clé de la table de hachage en utilisant la technique du chaînage.

En utilisant une structure de données de table de hachage, vous serez en mesure de créer un tableau associatif avec des opérations de recherche, d'insertion et de suppression rapides. 😉

Si vous avez apprécié cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il propose un guide progressif et bienveillant qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous aurez réellement l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !