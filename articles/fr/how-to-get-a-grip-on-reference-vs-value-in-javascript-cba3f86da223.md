---
title: Comment comprendre la référence vs la valeur en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T22:17:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-grip-on-reference-vs-value-in-javascript-cba3f86da223
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Hl0yMUBL8UBmsNBwbVMJJg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment comprendre la référence vs la valeur en JavaScript
seo_desc: 'By Marina Ferreira

  This article discusses how the various JavaScript data types behave when they’re
  assigned to a variable. Depending on the data type, memory is allocated differently
  to store it. It may reserve a new space to store a copy of the val...'
---

Par Marina Ferreira

Cet article discute comment les différents types de données JavaScript se comportent lorsqu'ils sont assignés à une variable. Selon le type de données, la mémoire est allouée différemment pour le stocker. Elle peut réserver un nouvel espace pour stocker une copie de la valeur, ou elle peut ne pas créer de copie du tout et simplement pointer vers la valeur existante (référence).

Voici mes notes prises en suivant le cours [Javascript30](https://javascript30.com) de [Wes Bos](https://wesbos.com/).

#### Nombres, Chaînes de caractères et Booléens

En JavaScript, les types primitifs tels que `undefined`, `null`, `string`, `number`, `boolean` et `symbol` sont passés par valeur.

```
let name = 'Marina';
let name2 = name;
```

```
console.log({name, name2}); // { name: 'Marina', name2: 'Marina' }
```

```
name = 'Vinicius';
```

```
console.log({name, name2}); // { name: 'Vinicius', name2: 'Marina' }
```

![Image](https://cdn-media-1.freecodecamp.org/images/WOKvO0CDlVUun7pqwGOyN4g64IqolhrWjuA0)
_Passé par valeur._

Lorsque la variable `name` est assignée, un espace en mémoire avec une adresse de `0x001` est réservé pour stocker cette valeur. La variable `name` pointe alors vers cette adresse. La variable `name2` est ensuite définie pour être égale à `name`. Un nouvel espace en mémoire, avec une nouvelle adresse `0x002` est alloué et stocke une copie de la valeur stockée à l'adresse vers laquelle `name` pointe.

Ainsi, chaque fois que nous voulons modifier la valeur de `name`, la valeur stockée par `name2` ne sera pas changée, puisque c'est une copie, stockée dans un emplacement différent.

#### Objets et Tableaux

Les objets en JavaScript sont passés par référence. Lorsque plus d'une variable est définie pour stocker soit un `object`, `array` ou `function`, ces variables pointeront vers le même espace alloué en mémoire.

```
const animals = ['Cat', 'Dog', 'Horse', 'Snake'];
```

```
let animals2 = animals;
console.log({animals, animals2}); // { animals: ['Cat', 'Dog', 'Horse', 'Snake'], animals2: ['Cat', 'Dog', 'Horse', 'Snake'] }
```

```
animals2[3] = 'Wale';
console.log(animals, animals2); // { animals: ['Cat', 'Dog', 'Horse', 'Wale'], animals2: ['Cat', 'Dog', 'Horse', 'Wale'] }
```

![Image](https://cdn-media-1.freecodecamp.org/images/8UmMLgC2-3bI2PYI8km77Jk9P1EPUV5CdGk6)
_Passé par référence._

Lorsque `animals` est défini pour stocker un tableau, la mémoire est allouée et une adresse est associée à cette variable. Ensuite, `animals2` est défini pour être égal à `animals`. Puisque `animals` stocke un tableau, au lieu de créer une copie de ce tableau et une nouvelle adresse en mémoire, `animals2` est simplement pointé vers le même objet à l'adresse existante. Ainsi, tout changement apporté à `animals2` se réfléchira sur `animals`, car ils pointent vers le même emplacement.

Vous verrez le même comportement pour les objets :

```
const person = {  name: 'Marina',  age: 29};
```

```
let femme = person;
femme.age = 18;
```

```
console.log({person, femme}); // { person: { name: 'Marina', age: 18 }, femme: { name: 'Marina', age: 18 } }
```

### Copie d'Objets et de Tableaux

Puisqu'une simple assignation ne suffit pas pour produire une copie d'un objet, cela peut être réalisé par d'autres approches :

#### Tableaux

**slice()**

```
let animals2 = animals.slice();
animals2[3] = 'Shark';
```

**concat()**

```
let animals3 = [].concat(animals);
animals3[3] = 'Tiger';
```

**spread (ES6)**

```
let animals4 = [...animals];
animals4[3] = 'Lion';
```

Les changements n'affecteront que l'objet modifié :

```
console.log({animals, animals2, animals3, animals4}); // { animals: ['Cat', 'Dog', 'Horse', 'Snake'], animals2: ['Cat', 'Dog', 'Horse', 'Shark'], animals3: ['Cat', 'Dog', 'Horse', 'Tiger'], animals4: ['Cat', 'Dog', 'Horse', 'Lion'] }
```

#### Objets

**assign()**

```
let human = Object.assign({}, person, { age: 20 });
```

```
console.log(person, human); // { person: { name: 'Marina', age: 29 }, human: { name: 'Marina', age: 20 } }
```

**Clone Profond**

Il est important de noter que ces méthodes ne sont profondes que d'un niveau. Pour les clones profonds, il existe une méthode déconseillée. Utilisez-la avec précaution.

```
let femme3 = JSON.parse(JSON.stringify(person));
femme3.name = 'Leslie';
```

```
console.log(person, femme3); // { person: { name: 'Marina', age: 29 }, femme3: { name: 'Leslie', age: 29 } }
```

### Références

* WesBos - [Javascript 30](https://javascript30.com)
* You Don't Know JS: Scope & Closures par Kyle Simpson

_Publié à l'origine sur [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/javascript30/reference-vs-copy/).