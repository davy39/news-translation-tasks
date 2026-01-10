---
title: Les fonctions fléchées de JavaScript expliquées en descendant un toboggan
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T22:23:35.000Z'
originalURL: https://freecodecamp.org/news/javascripts-arrow-functions-explained-by-going-down-a-slide-2eb8ee3c45e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HVh2O4VIKLxLoPH9CjZztA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Les fonctions fléchées de JavaScript expliquées en descendant un toboggan
seo_desc: 'By Kevin Kononenko

  If you have ever gone down a water slide, then you can understand arrow functions.


  If you have been using JavaScript for a few years, you are probably familiar with
  this syntax:

  function addTen(num){  return num + 10;});

  console.l...'
---

Par Kevin Kononenko

#### Si vous êtes déjà descendu d'un toboggan aquatique, alors vous pouvez comprendre les fonctions fléchées.

![Image](https://cdn-media-1.freecodecamp.org/images/Au60r4itPIeaPi5dHkcuwlKSk37qb2FjvroV)

Si vous utilisez JavaScript depuis quelques années, vous êtes probablement familier avec cette syntaxe :

```
function addTen(num){  return num + 10;});
```

```
console.log(addTen(2));//12
```

Cette syntaxe de fonction était populaire en ES5, ou ECMAScript 5.

Il y a un avantage majeur à cette syntaxe : elle inclut le mot function, donc il est évident que vous écrivez une fonction !

Une fonction prend clairement de 0 à plusieurs arguments et exécute un ensemble spécifique d'instructions chaque fois qu'elle est appelée.

Mais ensuite, le monde de JavaScript a fait un bond en avant avec ES6 en 2015.

Maintenant, la même fonction que ci-dessus serait écrite comme ceci :

```
let addTen = (num) => num + 10;
```

```
console.log(addTen(2));//12
```

Maintenant, il n'y a plus de mot-clé _function_, et plus d'instruction return ! Les fonctions en ES6 sont beaucoup plus concises.

Donc, puisque ces indices évidents ont été supprimés, vous pourriez avoir un peu de mal à comprendre les différentes parties des fonctions fléchées.

Heureusement, comme vous le verrez bientôt avec quelques animations, les fonctions fléchées sont assez faciles à comprendre une fois que vous apprenez à visualiser la flèche « => » d'une nouvelle manière.

Voici donc comment les fonctions fléchées sont comme un toboggan aquatique. Pour bien comprendre ce tutoriel, il pourrait être utile de connaître les [fonctions map](https://blog.codeanalogies.com/2018/02/20/javascript-map-method-explained-by-going-on-a-hike/) et la [portée des variables](https://blog.codeanalogies.com/2017/11/22/how-javascript-variable-scoping-is-just-like-multiple-levels-of-government/).

### Fonctions fléchées visualisées

Explorons un peu plus en profondeur la fonction addTen.

```
let addTen = (num) => num + 10;
```

```
console.log(addTen(2));//12
```

Cette fonction va transformer un paramètre et retourner ce paramètre avec 10 ajouté.

La transformation se fait avec cette subtile flèche « => ».

J'aime transformer cette flèche en toboggan dans mon esprit pour montrer ce qui se passe réellement. Voici ce que je veux dire :

![Image](https://cdn-media-1.freecodecamp.org/images/Ps5SxrF558e8ywvcBoSFDzNQUKwussni3Ci-)

Le signe égal est comme le toboggan et la flèche est comme la zone d'atterrissage.

Les fonctions fléchées suivent ce modèle :

(parameters) => {statements}

Ajoutons donc ces éléments au diagramme avec notre exemple de fonction addTen.

![Image](https://cdn-media-1.freecodecamp.org/images/fXH4R-oTUpaYcc8kWG3nhLRuBmL5LlirC1o-)

La dernière chose que nous devons montrer est comment le paramètre, qui est 10 dans ce cas, descend le toboggan et devient disponible dans les instructions de la fonction. Voici à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/eS7jMV7kl-h6mChbh1VVJ9Rq5HbDk6ArTM6R)

C'est tout ! Assez simple.

Maintenant, regardons un exemple où il y a deux paramètres différents. Voici notre nouvelle fonction :

```
let multiply = (num1, num2) => {return num1 * num2};
```

```
console.log(multiply(2, 10));//20
```

Dans ce cas, nous multiplions simplement les deux paramètres ensemble. Les deux descendent le toboggan ensemble. Comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/dsHfwfhAlIBdb3jU7erDG0lSf-6dvWv6DAxr)

Il y a un autre exemple que vous devriez connaître : combiner la méthode map() avec les fonctions fléchées.

La méthode map() va envoyer chaque élément d'un tableau dans la fonction fléchée, dans l'ordre.

Passons par un exemple : imaginez que vous avez un tableau de nombres, et que vous voulez obtenir la racine carrée de chacun.

Voici le code.

```
let nums = [1, 4, 9];
```

```
let squares = nums.map((num) => {  return Math.sqrt(num);});
```

```
console.log (squares)// [1, 2, 3]
```

Vous devez connaître un peu la méthode map pour comprendre celle-ci. Mais vous remarquerez probablement la syntaxe concise encore une fois — la méthode map() est beaucoup plus courte que d'écrire une boucle for().

Voici ce qui se passe dans ce code :

![Image](https://cdn-media-1.freecodecamp.org/images/NiM1EAFP57EsIPOVr-Q5bQUD7AgCkHgK7b5B)

1. Il y a trois éléments dans le tableau _nums_, donc le paramètre _num_ descend le toboggan 3 fois.
2. La méthode Math.sqrt() prend la racine carrée du nombre à chaque fois.
3. Le résultat est stocké dans le tableau _squares_ à chaque fois.

### La différence entre les fonctions fléchées et les fonctions traditionnelles

Vous vous demandez peut-être... est-ce simplement une différence de syntaxe ?

En fait, il y a une différence importante dans la façon dont les fonctions ES5 traditionnelles et les fonctions ES6 fonctionnent.

Le grand changement est que les fonctions fléchées n'ont pas leur propre portée. Par conséquent, si vous essayez d'utiliser le mot-clé _this_, vous serez surpris lorsqu'il ne se référera pas à la portée de la fonction fléchée.

Pour revenir à notre analogie du toboggan, cela signifie que _this_ est le même en haut et en bas du toboggan. Si nous utilisions des fonctions ES5, alors _this_ serait différent en haut et en bas du toboggan.

Pour reconnaître rapidement cela dans le code, il suffit de chercher le mot-clé _function_. Si vous le voyez, cela signifie qu'une nouvelle portée est créée. Sinon, supposez que vous utilisez la portée de la fonction englobante.

### Avez-vous apprécié ce tutoriel visuel ?

Si vous avez apprécié ce tutoriel, donnez-lui un "clap" ! Ou, si vous souhaitez lire plus de tutoriels visuels sur HTML, CSS et JavaScript, consultez le [site principal CodeAnalogies](http://codeanalogies.com/) pour 50+ tutoriels.