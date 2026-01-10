---
title: '[object, object] en JavaScript – Signification en JS'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-25T14:30:52.000Z'
originalURL: https://freecodecamp.org/news/object-object-in-javascript-meaning-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/clement-helardot-95YRwf6CNw8-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: '[object, object] en JavaScript – Signification en JS'
seo_desc: "When working with objects in JavaScript, you may have come across the [object,\
  \ object] output. While this may seem irrelevant, it's not necessarily an error.\
  \ \n[object, object] is the string representation of a JavaScript object data type.\
  \ You'll unde..."
---

Lorsque vous travaillez avec des objets en JavaScript, vous avez peut-être rencontré la sortie `[object, object]`. Bien que cela puisse sembler sans importance, ce n'est pas nécessairement une erreur. 

`[object, object]` est la représentation sous forme de chaîne de caractères du type de données objet en JavaScript. Vous comprendrez mieux au fur et à mesure que nous avancerons dans cet article.

Il existe deux principaux contextes où vous rencontrerez une telle sortie :

* Lorsque vous essayez d'afficher un objet en utilisant la méthode `alert()` (le plus courant). 
* Lorsque vous utilisez la méthode `toString()` sur un objet. 

Examinons quelques exemples. 

## Que se passe-t-il si vous affichez un objet en JavaScript ?

Dans cette section, vous verrez ce qui se passe lorsque vous utilisez la méthode `alert()` pour afficher un objet en JavaScript. Voici un exemple de code :

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

alert(student)
```

Dans le code ci-dessus, nous avons créé un objet appelé `student`. Après avoir utilisé la méthode `alert()` pour afficher l'objet dans le navigateur, nous avons obtenu la sortie suivante : 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--301-.png)

Comme vous pouvez le voir sur l'image ci-dessus, au lieu d'avoir l'objet et ses propriétés affichés, `[object, object]` a été affiché. 

Cela se produit parce que lorsque vous utilisez la méthode `alert()` pour afficher un objet en JavaScript, vous obtenez le format de chaîne affiché. 

Pour corriger cela, vous pouvez utiliser la méthode `JSON.stringify()` pour transformer l'objet en une chaîne qui peut être affichée dans le navigateur en utilisant la méthode `alert()`. Voici un exemple :

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

alert(JSON.stringify(student));
```

Lorsque vous exécutez le code ci-dessus, vous devriez voir l'objet et ses propriétés affichés – similaire à l'image ci-dessous. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--303-.png)

## Que se passe-t-il lorsque vous utilisez la méthode `toString()` sur un objet en JavaScript ?

La méthode `toString()` en JavaScript retourne le format de chaîne d'un objet. Cette section vous aidera à comprendre ce qui s'est passé sous le capot dans la dernière section.

Lorsque vous utilisez la méthode `toString()` sur un objet en JavaScript, vous obtenez la représentation sous forme de chaîne – `[object, object]` – retournée. 

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

console.log(student.toString());
// [object Object]
```

Comme vous pouvez le voir dans le code ci-dessus, nous avons utilisé la méthode `toString()` sur un objet appelé `student` : `student.toString()`. 

Lorsque nous avons enregistré cela dans la console, nous avons obtenu `[object, object]`. 

Cet effet est exactement ce qui se passe lorsque vous affichez un objet dans le navigateur en utilisant la méthode `alert()` (comme nous l'avons vu dans la dernière section).

## Résumé

Dans cet article, nous avons parlé de la sortie étrange `[object, object]` en JavaScript. 

Nous avons compris que cette sortie est la représentation sous forme de chaîne du type de données objet en JavaScript. 

Vous êtes susceptible de voir une telle sortie lorsque vous essayez d'afficher un objet dans le navigateur en utilisant la méthode `alert()`, ou lorsque vous utilisez la méthode `toString()` sur un objet. 

Nous avons également passé en revue quelques exemples de code et images pour démontrer comment vous pouvez voir `[object, object]` en JavaScript.

Bon codage !