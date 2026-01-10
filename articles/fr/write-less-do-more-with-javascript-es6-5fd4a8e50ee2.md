---
title: JavaScript ES6 — écrire moins, faire plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T17:53:40.000Z'
originalURL: https://freecodecamp.org/news/write-less-do-more-with-javascript-es6-5fd4a8e50ee2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_g2EvGpJlt4YKcvsNsta7g.png
tags:
- name: ES6
  slug: es6
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: JavaScript ES6 — écrire moins, faire plus
seo_desc: 'By Said Hayani

  JavaScript ES6 brings new syntax and new awesome features to make your code more
  modern and more readable. It allows you to write less code and do more. ES6 introduces
  us to many great features like arrow functions, template strings, c...'
---

Par Said Hayani

JavaScript ES6 apporte une nouvelle syntaxe et de nouvelles fonctionnalités géniales pour rendre votre code plus moderne et plus lisible. Il vous permet d'écrire moins de code et de faire plus. ES6 nous introduit à de nombreuses fonctionnalités géniales comme les fonctions fléchées, les chaînes de caractères de modèle, la destruction de classe, les Modules… et plus encore. Jetons un coup d'œil.

### const et let

`const` est un nouveau mot-clé dans ES6 pour déclarer des variables. `const` est plus puissant que `var`. Une fois utilisé, la variable ne peut pas être réassignée. En d'autres termes, c'est une **variable immutable** sauf lorsqu'elle est utilisée avec des objets.

Cela est vraiment utile pour cibler les sélecteurs. Par exemple, lorsque nous avons un seul bouton qui déclenche un événement, ou lorsque vous voulez sélectionner un élément HTML en JavaScript, utilisez `const` au lieu de `var`. Cela est dû au fait que `var` est "hoisted". Il est toujours préférable d'utiliser `const` lorsque vous ne voulez pas réassigner la variable.

![Image](https://cdn-media-1.freecodecamp.org/images/e4r4Zg1XTz395qj9A5hOpHMK0mzH0zwxitK9)

Dans le code ci-dessus, `const` ne changera pas et ne peut pas être réassignée. Si vous essayez de lui donner une nouvelle valeur, cela vous retournera une erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/kM-LHiezWRHQa0aakmKyPrgd53riDwKnrSUa)

`let` peut être réassigné et prendre une nouvelle valeur. Il crée une **variable mutable**.

`let` est le même que `const` en ce sens que les deux sont bloqués dans leur portée. Cela signifie que la variable est uniquement disponible dans sa portée.

### Fonctions fléchées

La fonction fléchée est vraiment géniale et rend votre code plus lisible, plus structuré et ressemble à du code moderne. Au lieu d'utiliser ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/CAtsmTIStmCZaK-7ej4vvuHzY-aqfNhRhevc)

Utilisez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/jaJg1ODAb7FcbQbWaQ8FwegEmTD4IsTtx7Of)

Comme vous le voyez, la fonction fléchée semble plus lisible et propre ! Vous n'aurez plus besoin d'utiliser l'ancienne syntaxe.

De plus, vous pouvez utiliser la fonction fléchée avec les fonctions intégrées `map`, `filter` et `reduce`.

![Image](https://cdn-media-1.freecodecamp.org/images/2G7fWO8OuCNbdMXa7wiRxoncLZshsRxZ0WYR)

La fonction map avec les flèches semble plus claire et lisible que `map` dans ES5. Avec ES6, vous pouvez écrire un code plus court et plus intelligent. Vous pouvez utiliser la même chose avec `filter` et `reduce`.

### Littéraux de modèle

Les littéraux de modèle ou chaînes de caractères de modèle sont assez cool. Nous n'avons pas à utiliser l'opérateur plus (+) pour concaténer des chaînes de caractères, ou lorsque nous voulons utiliser une variable à l'intérieur d'une chaîne de caractères.

L'ancienne syntaxe :

![Image](https://cdn-media-1.freecodecamp.org/images/pyiP612uJAXA9gvXK0fnmxc9tb6J0WRSB3Nj)

Avec la nouvelle syntaxe ES6 :

![Image](https://cdn-media-1.freecodecamp.org/images/O1aAY7ehL3Vtvej0YXuZVXbN3LjHX2-WXzOG)

Si simple ! C'est une réelle énorme différence entre l'ancienne syntaxe et ES6. Lorsque vous jouez avec des chaînes de caractères, la chaîne de caractères littérale dans ES6 semble plus organisée et bien structurée que dans ES5.

### **Paramètres par défaut**

Lorsque je travaille en PHP, j'utilise généralement des paramètres par défaut. Ceux-ci vous permettent de définir un paramètre à l'avance.

Ainsi, lorsque vous oubliez d'écrire le paramètre, il ne retournera pas une erreur indéfinie car le paramètre est déjà défini par défaut. Donc, lorsque vous exécutez votre fonction avec un paramètre manquant, elle prendra la valeur du paramètre par défaut `t`, et elle ne retournera pas d'erreur !

Regardez cet exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/qFmJ6F0gOBdVl4kJ7sFhIqHaGIZx6iehhoML)

La fonction ci-dessus retourne indéfini, car nous avons oublié de lui donner le deuxième paramètre `age`.

Mais si nous utilisons le paramètre par défaut, il ne retournera pas indéfini, et il utilisera sa valeur lorsque nous oublions d'assigner un paramètre !

![Image](https://cdn-media-1.freecodecamp.org/images/-RczdieWIpZVTLYih1PD4ZJdq2UeurbiMBHu)

Comme vous le voyez, la fonction retourne une valeur même si nous avons manqué le deuxième paramètre. Maintenant, avec le paramètre par défaut, nous pouvons gérer l'erreur à l'avance.

### Destruction de tableau et d'objet

La destruction facilite l'assignation des valeurs d'un tableau ou d'un objet à la nouvelle variable.

L'ancienne syntaxe :

![Image](https://cdn-media-1.freecodecamp.org/images/rsZwpm7Ah7OyThsTpkBsaRUsCwjQBSGCGEfG)

Avec la syntaxe ES6 :

![Image](https://cdn-media-1.freecodecamp.org/images/rrKo0LFQOblpaAIlywUGrtD8keMqwywZ5MXR)

Avec ES5, nous devons assigner chaque valeur à chaque variable. Avec ES6, nous mettons simplement nos valeurs entre accolades pour obtenir n'importe quelle propriété de l'objet.

Note : si vous assigner une variable qui n'est pas identique au nom de la propriété, elle retournera indéfini. Par exemple, si le nom de la propriété est `name` et que nous l'assignons à une variable `username`, elle retournera indéfini.

Nous devons toujours nommer la variable de la même manière que le nom de la propriété. Mais dans le cas où nous voulons renommer la variable, nous pouvons utiliser le deux-points `:` à la place.

![Image](https://cdn-media-1.freecodecamp.org/images/zLZ3XTvYSXB3UiRg2W05YXGcHa6GJGqEQJLa)

Pour le tableau, nous utilisons la même syntaxe que pour l'objet. Nous devons simplement remplacer les accolades par des crochets.

![Image](https://cdn-media-1.freecodecamp.org/images/JUcyaqc4T9qdXgQbYCqfbi10THAatzHh64ts)

### Import et export

L'utilisation de `import` et `export` dans votre application JavaScript la rend plus puissante. Ils vous permettent de créer des composants séparés et réutilisables.

Si vous êtes familier avec un framework MVC JavaScript, vous verrez qu'ils utilisent `import` et `export` pour gérer les composants la plupart du temps. Alors, comment fonctionnent-ils vraiment ?

C'est simple ! `export` vous permet d'exporter un module pour être utilisé dans un autre composant JavaScript. Nous utilisons `import` pour importer ce module afin de l'utiliser dans notre composant.

Par exemple, nous avons deux fichiers. Le premier s'appelle `detailComponent.js` et le second s'appelle `homeComponent.js`.

Dans `detailComponent.js`, nous allons exporter la fonction `detail`.

![Image](https://cdn-media-1.freecodecamp.org/images/3K3KNLMTvnsVpk2EEx100lAURNgW7fXzBauC)

Et si nous voulons utiliser cette fonction dans `homeComponent.js`, nous utiliserons simplement `import`.

![Image](https://cdn-media-1.freecodecamp.org/images/IB6KSO6rK-574uNXuX5tDUIly6NkqIsT7cpZ)

Si nous voulons importer plus d'un module, nous les mettons simplement entre accolades.

![Image](https://cdn-media-1.freecodecamp.org/images/yeJzCdTfkuZEd-PL9oLX7DWO-cukNHKrLt-5)

C'est cool, n'est-ce pas ?!

### **Promesses**

Les promesses sont une nouvelle fonctionnalité de ES6. C'est une méthode pour écrire du code asynchrone. Elle peut être utilisée lorsque, par exemple, nous voulons récupérer des données à partir d'une API, ou lorsque nous avons une fonction qui prend du temps à être exécutée. Les promesses facilitent la résolution du problème, alors créons notre première promesse !

![Image](https://cdn-media-1.freecodecamp.org/images/zVsFm1MnCkDU9oPLEmfRhLJiA0dyH1nKCa7C)

Si vous consignez votre console, elle retournera une promesse. Donc, si nous voulons exécuter une fonction après que les données soient récupérées, nous utiliserons une promesse. La promesse prend deux paramètres : `resolve` et `reject` pour gérer une erreur attendue.

Note : la fonction fetch retourne une promesse elle-même !

```
const url='https://jsonplaceholder.typicode.com/posts';
```

```
const getData=(url)=>{
  return fetch(url);
}
```

```
getData(url).then(data=> data.json()).then(result=> console.log(result));
```

Maintenant, si vous consignez votre console, elle retournera un tableau de données.

### Paramètre de repos et opérateur de propagation

[Le paramètre de repos](https://developer.mozilla.org/ar/docs/Web/JavaScript/Reference/Functions/rest_parameters) est utilisé pour obtenir l'argument d'un tableau et retourner un nouveau tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/ZGyyj2ByWBRUpEw841VQRKGXPX6KV4aeyRyf)

![Image](https://cdn-media-1.freecodecamp.org/images/SEt08SKlukqs7SSkDBoRHt-0dc9s2zrEpBDr)

L'opérateur de propagation a la même syntaxe que le paramètre de repos, mais l'opérateur de propagation prend le tableau lui-même et non seulement les arguments. Nous pouvons utiliser le paramètre de propagation pour obtenir les valeurs d'un tableau, au lieu d'utiliser une boucle for ou toute autre méthode.

```js
const arr=['said',20,'JavaScript enthusiast','Hi','Said','How are you?'];

const Func=(...anArray)=>{
  return anArray;
}

console.log(Func(arr));

//output  ["said", 20, "JavaScript enthusiast", "Hi", "Said", "How are you?"
```

### Classes

Les classes sont le cœur de la programmation orientée objet (POO). Elles rendent votre code plus sécurisé et encapsulé. L'utilisation de classes donne à votre code une belle structure et le maintient orienté.

![Image](https://cdn-media-1.freecodecamp.org/images/2EGxzbm25W2EtzYv67c-N49DAqTMw01iZ2Ok)

Pour créer une classe, utilisez le mot-clé `class` suivi du nom de la classe avec deux accolades.

![Image](https://cdn-media-1.freecodecamp.org/images/0K889E--nHdRPGY1nCVvUzCtAWGkDe8vPfCa)

Maintenant, nous pouvons accéder aux méthodes et propriétés de la `class` en utilisant le mot-clé `new`.

```js
class myClass{
    constructor(name,age){
    this.name=name;
    this.age=age;
}
}
const Home= new myClass("said",20);
console.log(Home.name)//  said
```

Pour hériter d'une autre classe, utilisez le mot-clé `extends` suivi du nom de la classe dont vous voulez hériter.

![Image](https://cdn-media-1.freecodecamp.org/images/rTlJ5DgmaUL1ZCoy1EEKxCt4TK2ihUeWVd-M)

Vous pouvez en apprendre plus sur les Classes [ici](https://developer.mozilla.org/ar/docs/Web/JavaScript/Reference/Classes).

ES6 a d'autres fonctionnalités incroyables — vous pouvez les explorer [ici](http://es6-features.org).

### Conclusion

J'espère que vous avez trouvé cet article utile, et j'espère avoir pu vous introduire à certaines des fonctionnalités de ES6. Si c'est le cas, abonnez-vous à cette [liste de diffusion](http://eepurl.com/dk9OJL) pour en apprendre plus sur les sujets Front-end. Merci pour votre temps.

> Au fait, j'ai récemment travaillé avec un groupe solide d'ingénieurs logiciels pour l'une de mes applications mobiles. L'organisation était géniale, et le produit a été livré très rapidement, beaucoup plus vite que d'autres entreprises et freelances avec lesquels j'ai travaillé, et je pense que je peux honnêtement les recommander pour d'autres projets. Envoyez-moi un email si vous voulez entrer en contact — [said@devsdata.com](mailto:said@devsdata.com).