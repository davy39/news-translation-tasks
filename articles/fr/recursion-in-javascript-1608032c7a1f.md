---
title: Récursion en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-07-25T13:11:16.000Z'
originalURL: https://freecodecamp.org/news/recursion-in-javascript-1608032c7a1f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb9c2740569d1a4caf44e.jpg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Récursion en JavaScript
seo_desc: 'By Kevin Ennis

  I’m just gonna get this out of the way right up front, because people get really
  angry otherwise:

  Consider this post as a series of learning exercises. These examples are designed
  to make you think — and, if I’m doing it right, maybe e...'
---

Par Kevin Ennis

Je vais simplement mettre cela au clair tout de suite, car les gens se mettent vraiment en colère sinon :

Considérez cet article comme une série d'exercices d'apprentissage. Ces exemples sont conçus pour vous faire réfléchir — et, si je fais bien les choses, peut-être élargir un peu votre compréhension de la programmation fonctionnelle.

### Hey, mon pote. J'ai entendu dire que tu aimais la récursion, alors j'ai mis un « Hey, mon pote. J'ai entendu dire que tu aimais la récursion, alors j'ai mis un « Hey, mon pote...

Définie de manière lâche, la récursion est le processus qui consiste à prendre un gros problème et à le subdiviser en plusieurs instances plus petites du même problème.

En pratique, cela signifie généralement écrire une fonction qui s'appelle _elle-même_. Probablement l'exemple le plus classique de ce concept est la fonction **factorielle**.

Vous vous souvenez peut-être des cours de maths que la factorielle d'un nombre **n** est le produit de tous les entiers positifs inférieurs ou égaux à **n**. En d'autres termes, la factorielle de **5** est **5 x 4 x 3 x 2 x 1**. La notation mathématique pour cela est **5!**.

Une chose intéressante que vous avez peut-être remarquée à propos de ce motif : **5!** est en fait juste **5 x 4!**. Et **4!** est juste **4 x 3!**. Et ainsi de suite jusqu'à ce que vous arriviez à **1**.

Voici comment nous écririons cela en JavaScript :

```javascript
function factorial(n) {
  if (n === 1) {
    return 1;
  }
  
  return n * factorial(n - 1);
}
```

Si cela semble confus, je vous encourage à parcourir mentalement le code en utilisant l'exemple de **factorial( 3 )**.

Voici un peu d'aide, au cas où vous en auriez besoin :

1. **factorial( 3 )** est **3 x factorial( 2 )**.
2. **factorial( 2 )** est **2 x factorial( 1 )**.
3. **factorial( 1 )** remplit notre condition **if**, donc c'est juste **1**.

Ce qui se passe vraiment ici, c'est que vous remontez la pile d'appels, descendez jusqu'à **1**, puis déroulez la pile. En déroulant la pile d'appels, vous multipliez chaque résultat. **1 x 2 x 3** est **6**, et c'est votre valeur de retour.

### **Inverser une chaîne de caractères**

Un de mes collègues m'a récemment parlé d'une question de tableau blanc qu'on lui avait posée lors d'un entretien, et j'ai pensé que c'était un problème plutôt amusant.

> Écrivez une fonction qui accepte une chaîne de caractères et l'inverse. De manière récursive.

Si vous êtes du genre ambitieux, je vous encourage à prendre quelques minutes et à essayer de résoudre ce problème par vous-même. Gardez à l'esprit le principe de base de la récursion, qui est de prendre un gros problème et de le décomposer en instances plus petites de lui-même.

Si vous êtes bloqué (ou si vous êtes du genre décidément _peu ambitieux_), voici ma solution :

```javascript
function reverse(str) {
  if (str.length === 1) {
    return str;
  }
  
  return reverse(str.slice(1)) + str[0];
}
```

Encore une fois, je vais donner un exemple de parcours rapide au cas où vous seriez bloqué. Nous utiliserons **reverse('bar')** comme point de départ.

1. **reverse('bar')** est **reverse('ar') + 'b'**
2. **reverse('ar')** est **reverse('r') + 'a'**
3. **reverse('r')** remplit notre condition **if**, donc c'est juste **'r'**

Lorsque la pile d'appels se déroule, nous obtenons **'r' + 'a' + 'b'**.

### Écrire une fonction Map récursive

Pour notre dernier exemple, nous allons écrire une fonction **map()**. Nous voulons pouvoir l'utiliser comme ceci :

```javascript
map([ 'a', 'b', 'c' ], function(v) {
  return v.toUpperCase();
});
// => [ 'A', 'B', 'C' ]
```

Encore une fois, je vous _encourage fortement_ à prendre quelques minutes et à essayer cela par vous-même. Voici quelques indices et rappels :

1. **map()** doit toujours retourner un _nouveau_ tableau.
2. Décomposez le problème en morceaux plus petits.
3. Souvenez-vous de l'exemple **reverse()**.

Oh, bien. Vous êtes de retour. Comment cela s'est-il passé ?

Je plaisante, c'est un blog et je ne peux pas vous entendre. lol.

En tout cas, voici comment je l'ai fait :

```javascript
function map(arr, fn) {
  if (arr.length === 0) {
    return arr;
  }
  
  const [ head, ...tail ] = arr;
  
  return [ fn(head) ].concat(map(tail, fn));
}
```

Alors, passons en revue cela en utilisant l'exemple que j'ai donné précédemment :

1. Appelez **map()** en utilisant le tableau **[ 'a', 'b', 'c' ]**
2. Créez un _nouveau_ tableau qui contient le résultat de l'appel **fn('a')**
3. Retournez **[ 'A' ].concat( map([ 'b', 'c' ]) )**
4. Répétez les étapes 1 à 3 avec **[ 'b', 'c' ]**
5. Répétez les étapes 1 à 3 pour **[ 'c' ]**
6. Finalement, nous appelons **map()** avec un tableau vide, ce qui met fin à la récursion.

**NOTE :**  
Vous ne devriez jamais, jamais, jamais faire cela dans une application réelle. Vous allez faire exploser la pile avec de grands tableaux, et surtout, vous créez une **énorme** quantité de déchets en instanciant autant de nouveaux objets. Utilisez **Array#map** dans le code de production.

### Conclusion

Espérons que j'ai fait un travail décent pour expliquer tout cela. Si vous avez encore un peu de mal à comprendre la récursion, le meilleur conseil que je puisse donner est de commencer par des exemples simples et de tracer mentalement la pile d'appels. Essayez quelque chose comme **reverse('abc')** et parcourez-le, étape par étape. Finalement, cela deviendra clair.

— -

Suivez-moi sur [Twitter](http://twitter.com/kevincennis) ou [Medium](https://medium.com/@kevincennis/) pour plus de publications. J'essaie d'écrire une fois par jour pendant les 30 prochains jours.

Et si vous êtes dans la région de Boston et que vous voulez venir travailler sur des problèmes fous, intéressants et difficiles avec moi chez [Starry](https://starry.com), envoyez-moi un [email](mailto:kennis84@gmail.com). Je recrute.