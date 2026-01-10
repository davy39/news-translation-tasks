---
title: Comment supprimer une propriété d'un objet JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-21T17:48:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-property-from-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/remove-property-from-js-object.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment supprimer une propriété d'un objet JavaScript
seo_desc: "By Saransh Kataria\nThere are two ways to remove a property from a JavaScript\
  \ object. There's the mutable way of doing it using the delete operator, and the\
  \ immutable way of doing it using object restructuring. \nLet's go through each\
  \ of these methods ..."
---

Par Saransh Kataria

Il existe deux façons de supprimer une propriété d'un objet JavaScript. Il y a la méthode mutable utilisant l'opérateur delete, et la méthode immutable utilisant la restructuration d'objet. 

Passons en revue chacune de ces méthodes dans ce tutoriel.

## Supprimer une propriété d'un objet JS avec l'opérateur Delete

`delete` est une instruction JavaScript qui nous permet de supprimer une propriété d'un objet JavaScript. Il existe plusieurs façons de l'utiliser :

* `delete object.property;`
* `delete object['property'];`

L'opérateur supprime la propriété correspondante de l'objet.

```javascript
let blog = {name: 'Wisdom Geek', author: 'Saransh Kataria'};
const propToBeDeleted = 'author';
delete blog[propToBeDeleted];
console.log(blog); // {name: 'Wisdom Geek'}
```

L'opération de suppression modifie l'objet original. Cela signifie qu'il s'agit d'une opération mutable.

## Supprimer une propriété d'un objet JS avec la destructuration d'objet

En utilisant la restructuration d'objet et la syntaxe rest, nous pouvons destructurer l'objet avec la propriété à supprimer et créer une nouvelle copie de celui-ci. 

Après la destructuration, une nouvelle copie de l'objet est créée et assignée à une nouvelle variable sans la propriété que nous avons choisie de supprimer.

```javascript
const { property, ...remainingObject } = object;
```

Par exemple :

```javascript
let blog = {name: 'Wisdom Geek', author: 'Saransh Kataria'};
const { author, ...blogRest } = blog;
console.log(blogRest) // {name: 'Wisdom Geek'};
console.log(blog); // {name: 'Wisdom Geek', author: 'Saransh Kataria'}
```

Si nous voulons faire cela dynamiquement, nous pouvons faire ceci :

```javascript
const name = 'propertToBeRemoved';
const { [name]: removedProperty, ...remainingObject } = object;
```

Il est également possible de supprimer plusieurs propriétés en utilisant la même syntaxe.

## Conclusion

Et voilà les deux façons de supprimer une propriété d'un objet JavaScript. Si vous avez des questions, n'hésitez pas à me contacter !

_Lisez plus de mes articles sur : [https://www.wisdomgeek.com](https://www.wisdomgeek.com/)_