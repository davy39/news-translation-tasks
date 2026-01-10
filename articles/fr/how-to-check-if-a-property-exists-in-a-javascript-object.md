---
title: Comment vérifier si une propriété existe dans un objet JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-25T17:53:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-property-exists-in-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/kevin-canlas-cFFEeHNZEqw-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment vérifier si une propriété existe dans un objet JavaScript
seo_desc: "When you are working with objects in JavaScript, you might need to check\
  \ if a specific property exists or not. \nIn this article, I will show you three\
  \ ways to check if a property exists in a JavaScript object. \nHow to Use the hasOwnProperty()\
  \ Method ..."
---

Lorsque vous travaillez avec des objets en JavaScript, vous pourriez avoir besoin de vérifier si une propriété spécifique existe ou non. 

Dans cet article, je vais vous montrer trois façons de vérifier si une propriété existe dans un objet JavaScript. 

## Comment utiliser la méthode `hasOwnProperty()` en JavaScript

La méthode `hasOwnProperty()` vérifie si un objet contient une propriété directe et retourne vrai ou faux selon qu'elle existe ou non. 

Voici la syntaxe de base :

```js
obj.hasOwnProperty(prop)
```

Dans ce premier exemple, nous avons un objet appelé `developer` avec trois propriétés :

```js
const developer = {
  name: "Jessica Wilkins",
  country: "United States",
  isEmployed: true
};
```

Si nous voulions vérifier si la propriété `isEmployed` existe dans l'objet `developer`, nous pouvons utiliser la méthode `hasOwnProperty()`, comme ceci :

```js
developer.hasOwnProperty("isEmployed")
```

Cela retournerait vrai car la propriété appelée `isEmployed` est une propriété directe de l'objet `developer`. 

Mais que se passerait-il si nous essayions de vérifier une propriété appelée `isPrototypeOf` ?

```js
developer.hasOwnProperty("isPrototypeOf")
```

Cela retournerait faux car il n'y a pas de propriété directe appelée `isPrototypeOf` sur l'objet `developer`. Mais que veux-je dire par propriété directe ? 

Chaque fois que vous créez un objet en JavaScript, il y a une propriété intégrée appelée prototype et sa valeur est un autre objet. Cet objet aura son propre prototype, et cela est connu sous le nom de chaîne de prototypes. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-23-at-6.47.02-PM.png)

Notre objet `developer` a accès à ces autres propriétés, comme `toString`, et c'est ce qu'on appelle une propriété héritée. 

La méthode `hasOwnProperty()` ne retournera vrai que pour les propriétés directes et non pour les propriétés héritées de la chaîne de prototypes. 

## Comment utiliser l'opérateur `in`

Contrairement à la méthode `hasOwnProperty()`, l'opérateur `in` retournera vrai pour les propriétés directes et héritées qui existent dans l'objet. 

Voici la syntaxe de base :

```js
property in object
```

Nous pouvons modifier notre exemple précédent pour vérifier si la propriété `country` existe dans l'objet `developer` en utilisant l'opérateur `in`.

```js
"country" in developer
```

Cela retournerait vrai car la propriété `country` est une propriété directe dans l'objet `developer`. 

Nous pouvons également vérifier si la propriété `toString` existe sur l'objet `developer` ou dans la chaîne de prototypes. 

```js
"toString" in developer
```

Cela retournerait vrai car la propriété `toString` existe dans la chaîne de prototypes car elle a été héritée de l'objet prototype. 

## Comment vérifier si une propriété existe dans un objet en utilisant `undefined`

Si j'essaie d'accéder à un nom de propriété dans un objet qui n'existe pas, alors j'obtiendrai undefined. 

Par exemple, si j'essaie `developer.age`, la valeur de retour serait undefined car l'objet `developer` n'a pas ce nom de propriété. 

Nous pouvons vérifier si une propriété existe dans l'objet en vérifiant si `property !== undefined`.

Dans cet exemple, cela retournerait vrai car la propriété `name` existe dans l'objet `developer`. 

```js
developer.name !== undefined
```

## Conclusion

Si vous devez vérifier si une propriété existe dans un objet JavaScript, il existe trois façons courantes de le faire. 

La méthode `hasOwnProperty()` vérifie si un objet contient une propriété directe et retourne vrai ou faux selon qu'elle existe ou non. La méthode `hasOwnProperty()` ne retournera vrai que pour les propriétés directes et non pour les propriétés héritées de la chaîne de prototypes. 

Contrairement à la méthode `hasOwnProperty()`, l'opérateur `in` retournera vrai pour les propriétés directes et héritées qui existent dans l'objet ou sa chaîne de prototypes. 

Enfin, nous pouvons voir si une propriété existe dans l'objet en vérifiant si `property !== undefined`.

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours de développeur.