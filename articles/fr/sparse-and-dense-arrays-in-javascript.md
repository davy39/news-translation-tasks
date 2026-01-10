---
title: Tableaux clairsemés vs tableaux denses en JavaScript — Expliqué avec des exemples
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-03-08T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/sparse-and-dense-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/UwzSmIVOo.jpeg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tableaux clairsemés vs tableaux denses en JavaScript — Expliqué avec des
  exemples
seo_desc: 'I had a really interesting bug recently that, at first glance, completely
  stumped me.I saw I had an array that was empty. But the length was 31.

  Wait, what?

  What are dense arrays?

  Dense arrays are the most well known type of Array. They are the "norm...'
---

J'ai eu un bug vraiment intéressant récemment qui, à première vue, m'a complètement déconcerté. 
J'ai vu que j'avais un tableau qui était vide. Mais la longueur était de 31.

Attendez, quoi ?

## Qu'est-ce que les tableaux denses ?

Les tableaux denses sont le type de `Array` le plus connu. Ce sont les tableaux "normaux" avec lesquels la plupart des gens sont familiers.

Un tableau dense est un tableau où les éléments sont tous séquentiels en commençant à l'index 0.

Dans ce cas, la propriété length d'un tableau spécifie avec précision le nombre d'éléments dans le tableau.

```javascript
let array = [1, 2, 3, 4, 5]  
array.length // Retourne 5

```

## Qu'est-ce que les tableaux clairsemés ?

Un tableau clairsemé est un tableau dans lequel les éléments ne sont pas séquentiels, et ils ne commencent pas toujours à 0.

Ce sont essentiellement des `Array` avec des "trous", ou des écarts dans la séquence de leurs indices.

Un exemple serait :

```javascript
let array = [];
array[100] = "Des trous existent maintenant";
array.length // 101, mais seulement 1 élément
```

Normalement, la propriété length d'un `Array` retourne avec précision le nombre d'éléments dans le tableau, mais dans les tableaux clairsemés, ce n'est pas le cas. Si le tableau est clairsemé, la valeur de la propriété length est supérieure au nombre d'éléments.

# Pourquoi les `Array` peuvent-ils être clairsemés ?

Les `Array` sous le capot en JavaScript sont des `Object`. Leurs clés sont des nombres, et leurs valeurs sont les éléments.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599682873904/ByiIRL0vT.png)

```javascript
let array = [];
array[20] = {};
array[100] = {};
array[19] = {};
alert(array.length); // Affiche 101

```

La propriété `length` d'un `Array` prend l'index du dernier élément et ajoute un. Donc si vous avez un tableau avec des trous entre l'index 0 et 100, et un élément à l'index 101, le `length` retournera 101, car c'est le dernier index + 1.

Ce qui précède se produit indépendamment du nombre d'éléments dans le `Array`.

La spécification détaille spécifiquement ce comportement si vous [souhaitez en lire plus sur la spécification ECMAScript ici.](http://www.ecma-international.org/ecma-262/5.1/#sec-15.4.5.2)

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599597131632/RiZ59nGj3.png)

# Comment obtenir un tableau clairsemé ?

Vous avez déjà vu quelques méthodes, mais il y en a d'autres :

## Utiliser l'objet `Array`

```javascript
let array = new Array(10); // tableau initialisé sans éléments
array.length // 10

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-53.png)

## Insérer une clé/valeur à un certain index

```javascript
array[1000] = 0; // L'assignation ajoute un élément 
array.length // Mais .length retourne 1001

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-54.png)

## Utiliser l'opérateur `delete`

```javascript
let array = [1, 2, 3, 4, 5]
delete array[0]
array.length // .length retourne 5

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-55.png)

## Initialiser un `Array` avec des trous

```javascript
[,,,,] // Vous avez créé un tableau avec rien que des trous
[1,2,3,4,,5] // Oh non, vous avez mal tapé une virgule et entré un trou entre 4 et 5 !

```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-56.png)

## Différences d'implémentation entre navigateurs

Le navigateur que vous utilisez (ainsi que la version) représente les trous des tableaux clairsemés différemment.

Chrome affiche cela de la meilleure manière (à mon avis) et montre `empty`.  


![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599687555328/dX4b8NGcj.png)

La dernière version de Firefox (80.0.1 au moment de l'écriture) l'affiche comme suit :  


![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599598536385/vfQk4COPj.png)

## Conclusion

La solution finale du bug que j'ai introduit au début est de simplement vérifier que l'élément n'est pas falsy avant de l'utiliser. Quelque chose comme :

```javascript
let array = [,,,,]
for(let i = 0; i < array.length; i++){
    if (array[i]) {
        console.log(array[i])
    }
}

```

Parce que les trous sont falsy, cela n'exécutera pas la logique que vous essayez sur les trous que vous avez dans le `Array`.

Alors pourquoi mon navigateur l'a-t-il montré comme vide ?

J'utilisais Safari et il n'a rien montré pour les trous. J'ai donc enregistré la longueur du `Array` qui était de 31, et quand j'ai enregistré le contenu, il m'a juste montré un tableau vide ! Plutôt déconcertant à première vue.