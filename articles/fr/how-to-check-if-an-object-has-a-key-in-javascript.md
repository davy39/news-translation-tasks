---
title: Clé JavaScript dans un Objet – Comment Vérifier si un Objet a une Clé en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-25T14:24:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-an-object-has-a-key-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--3-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Clé JavaScript dans un Objet – Comment Vérifier si un Objet a une Clé en
  JS
seo_desc: 'Objects in JavaScript are non-primitive data types that hold an unordered
  collection of key-value pairs.


  As you can see in the image above, the key is the property, and each object value
  must have a key.

  When interacting with objects, situations mig...'
---

Les objets en JavaScript sont des types de données non primitifs qui contiennent une collection non ordonnée de paires clé-valeur.

![](https://paper-attachments.dropbox.com/s_D8321C80F6574B261A5AA02D2476A50C8DDF61A6CC2583DCEE0E18EC365EF07B_1658417045591_Untitled+Diagram.jpg align="left")

Comme vous pouvez le voir sur l'image ci-dessus, la clé est la propriété, et chaque valeur d'objet doit avoir une clé.

Lors de l'interaction avec des objets, des situations peuvent survenir qui nécessitent de vérifier si une clé particulière existe. Il est important de noter que si vous savez qu'une clé existe, cela signifie automatiquement qu'une valeur existe. Cette valeur pourrait être n'importe quoi – même vide, null ou undefined.

Dans cet article, nous allons apprendre les différentes méthodes pour vérifier si une clé d'objet existe en JavaScript.

### Voici un Scrim Interactif sur Comment Vérifier si un Objet a une Clé en JavaScript

<iframe src="https://scrimba.com/scrim/cZ7y4nHv?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

Au cas où vous seriez pressé, voici les deux méthodes standard que nous pouvons utiliser pour vérifier :

```js
// Utilisation de l'opérateur in
'key' in object

// Utilisation de la méthode hasOwnProperty()
object.hasOwnProperty('key')
```

## Comment Vérifier si un Objet a une `clé` en JavaScript avec l'Opérateur `in`

Vous pouvez utiliser l'opérateur `in` de JavaScript pour vérifier si une propriété/clé spécifiée existe dans un objet. Il a une syntaxe simple et retourne `true` si la propriété/clé spécifiée existe dans l'objet spécifié ou dans sa chaîne de prototypes.

La syntaxe lors de l'utilisation de l'opérateur [`in`](https://www.freecodecamp.org/news/the-javascript-in-operator-explained-with-examples/) est :

```js
'key' in object
```

Supposons que nous avons un objet qui contient les détails d'un utilisateur :

```js
let user = {
  name: "John Doe",
  age: 40
};
```

Nous pouvons vérifier si une clé existe avec l'opérateur `in` comme vu ci-dessous :

```js
'name' in user; // Retourne true
'hobby' in user; // Retourne false
'age' in user; // Retourne true
```

Note : La valeur avant le mot-clé `in` doit être de type `string` ou `symbol`.

## Comment Vérifier si un Objet a une `clé` en JavaScript avec la Méthode `hasOwnProperty()`

Vous pouvez utiliser la méthode `hasOwnProperty()` de JavaScript pour vérifier si un objet spécifié a la propriété donnée comme sa propriété.

Cette méthode est assez similaire à l'opérateur `in`. Elle prend une `string` et retournera `true` si la `clé` existe dans l'objet et `false` sinon.

La syntaxe lors de l'utilisation de la méthode `hasOwnProperty()` est :

```js
object.hasOwnProperty('key')
```

Supposons que nous avons un objet qui contient les détails d'un utilisateur :

```js
let user = {
  name: "John Doe",
  age: 40
};
```

Nous pouvons vérifier si une clé existe avec l'opérateur `in` comme vu ci-dessous :

```js
user.hasOwnProperty('name'); // Retourne true
user.hasOwnProperty('hobby'); // Retourne false
user.hasOwnProperty('age'); // Retourne true
```

Note : La valeur que vous passez dans la méthode `hasOwnProperty()` doit être de type `string` ou `symbol`.

Maintenant que nous savons que ces méthodes existent, nous pouvons utiliser une condition pour vérifier et effectuer l'opération que nous souhaitons :

```js
if ("name" in user) {
  console.log("la clé existe sur l'objet");
}

// Ou

if (user.hasOwnProperty("name")) {
  console.log("la clé existe sur l'objet");
}
```

## Conclusion

Dans cet article, nous avons appris comment vérifier si un objet a une clé en utilisant les deux méthodes standard. La différence entre les deux méthodes est que `Object.hasOwnProperty()` recherche une clé dans un objet seul tandis que l'opérateur `in` recherche la clé dans l'objet et sa chaîne de prototypes.

Il existe d'autres méthodes que vous pouvez utiliser, mais à un moment donné, elles peuvent devenir trop élaborées et ne sont pas si faciles à comprendre. Elles peuvent également échouer lorsqu'elles sont testées contre certaines conditions.

Par exemple, nous pourrions utiliser le chaînage optionnel, donc si une clé spécifiée n'existe pas, elle retournera `undefined` :

```js
let user = {
  name: "John Doe",
  age: 40
};

console.log(user?.name); // Retourne John Doe
console.log(user?.hobby); // Retourne undefined
console.log(user?.age); // Retourne 40
```

Nous pourrions donc créer une condition qui, lorsqu'elle n'est pas égale à `undefined`, signifie que la clé existe :

```js
if (user?.hobby !== undefined) {
  console.log("La clé existe sur l'objet");
}
```

Comme nous l'avons dit plus tôt, ces méthodes échouent lorsqu'elles sont testées contre certaines conditions peu courantes. Par exemple, dans une situation où une clé particulière est définie sur "undefined", comme vu ci-dessous, la condition échoue :

```js
let user = {
  name: "John Doe",
  age: undefined
};

console.log(user?.age); // Retourne undefined
```

Un autre exemple où cela fonctionne mais devient élaboré est lorsque nous utilisons la méthode `Object.keys()` avec la méthode `some()`. Cela fonctionne mais n'est pas vraiment facile à comprendre :

```js
let user = {
  name: "John Doe",
  age: undefined
};

const checkIfKeyExist = (objectName, keyName) => {
    let keyExist = Object.keys(objectName).some(key => key === keyName);
    return keyExist;
};
  
console.log(checkIfKeyExist(user, 'name')); // Retourne true
```

Dans le code ci-dessus, nous avons récupéré toutes les clés sous forme de tableau puis appliqué la méthode `some()` pour tester si au moins un élément du tableau passe le test. Si c'est le cas, il retourne `true`, sinon `false`.

Bon codage !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.