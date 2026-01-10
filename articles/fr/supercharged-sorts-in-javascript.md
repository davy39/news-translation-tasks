---
title: Comment utiliser les tris suralimentés en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-23T16:14:34.000Z'
originalURL: https://freecodecamp.org/news/supercharged-sorts-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6054e9bf687d62084bf682b9.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les tris suralimentés en JavaScript
seo_desc: 'By Tobias Parent

  I was asked a great question recently about filtering and sorting arrays. At first,
  it seemed trivial:


  If I have an array of objects, and I want to be able to filter() by multiple properties,
  can I do that?


  And the answer is, of co...'
---

Par Tobias Parent

On m'a posé une excellente question récemment sur le filtrage et le tri des tableaux. Au début, cela semblait trivial :

> Si j'ai un tableau d'objets, et que je veux pouvoir utiliser `filter()` sur plusieurs propriétés, est-ce possible ?

Et la réponse est, bien sûr, oui. Absolument. La manière dont `Array.filter()` fonctionne en JavaScript, c'est qu'il est chaînable. Cela signifie que lorsque la première fonction `.filter()` retourne, elle peut être directement alimentée dans un deuxième `.filter()`, et ainsi de suite pour autant de filtres que vous le souhaitez.

Mais si nous voulons _trier_ par plus d'une propriété, cela semble un peu plus compliqué. Après tout, si nous trions par une propriété, puis par une seconde, nous avons perdu la première.

Et si nous utilisions quelque chose comme `.reduce()` à la place ? Nous pourrions l'utiliser pour réduire le tableau à un objet dont les propriétés sont les premières valeurs de tri, puis définir chacune de ces propriétés à un tableau d'éléments _contenant_ ces valeurs, et les trier !

Et juste comme ça, nous sommes dans le terrier du lapin. Il doit y avoir une manière plus facile.

Comme il se trouve, il y en a une. C'est le bon vieux `Array.sort()` encore une fois.

## Deuxième couplet, même que le premier

Voici par où nous devons commencer : pensez aux valeurs que `Array.sort()` attend que sa fonction de rappel retourne, étant donné un rappel avec `(a, b)` comme paramètres :

* Si la valeur retournée est inférieure à zéro, `a` restera avant `b` dans l'ordre de tri.
* Si la valeur retournée est supérieure à zéro, `b` échangera sa place avec `a` dans l'ordre de tri.
* _Si la valeur retournée est égale à zéro, `a` et `b` ont le même poids, et restent donc inchangés._

Maintenant, une autre chose à noter : dans ces trois cas, nous avons trois valeurs : 0, -1, et 1. Voici comment JavaScript les coercera, en tant que valeurs Booléennes (vrai/faux) :

```js
Boolean(-1) === true; 
Boolean(1) === true; 
// Mais :
Boolean(0) === false;
```

Maintenant, comment cela nous aide-t-il ? Nous avons ici de grandes informations : premièrement, si un tri est effectué entre deux propriétés, et que les propriétés sont les mêmes, la comparaison devrait retourner 0 ou un Booléen `false`. Comme zéro est le seul nombre à être coercé en une valeur fausse, toute valeur égale donnera une comparaison fausse.

Deuxièmement, nous pouvons utiliser ce `true` ou `false` pour déterminer si nous devons creuser plus profondément.

Voici la dernière page, pour ceux qui voient déjà où cela nous mène :

```js
return <la valeur du premier comparateur, si elle est coercée en un Booléen vrai> 
    || <la valeur d'un second>;
```

## Attendez, quoi ?

Lol Oui. Qu'est-ce qui vient de se passer ? Que retournons-nous exactement là ?

L'utilisation du OU en ligne, `||`, indique à l'instruction return d'évaluer la valeur à retourner. Est-ce que le premier comparateur est Booléen `true` ? Si ce n'est pas le cas, alors parcourez l'arbre `||` jusqu'à la première comparaison qui le fait, ou si aucune ne le fait, retournez le résultat de cette dernière comparaison.

Travaillons cela avec un exemple pratique (exécutez le code **[ici](https://tech.io/snippet/oJ0Ueod)** sur Tech.io). Considérons un tableau de quatre membres :

```js
const myArray = [
  {
    firstName: 'Bob',
    lastName: 'Francis', 
    age: 34,
    city: 'Holland', 
    state: 'Massachusetts', 
    country: 'USA', 
    online: true
  }, {
    firstName: 'Janet',
    lastName: 'Francis',
    age: 41,
    city: 'Holland',
    state: 'Massachusetts',
    country: 'USA',
    online: false 
  },{
    firstName: 'Alexia',
    lastName: 'Francis',
    age: 39,
    city: 'Paris',
    state: 'Ile de France',
    country: 'France',
    online: true,
  },{
    firstName: 'Lucille',
    lastName: 'Boure',
    age: 29,
    city: 'Paris',
    state: 'Ile de France',
    country: 'France',
    online: true,
  }
];
```

Nous avons ces quatre utilisateurs, et nous souhaitons les trier par leur nom de famille :

```js
const sortByLastName = function(a, b){
  return a.lastName.localeCompare(b.lastName)
};

console.log(myArray.sort(sortByLastName) );
```

Cette première ligne définit notre fonction de tri, que nous passerons dans `myArray.sort(...)`. La fonction `localeCompare()` est une fonction JavaScript pratique pour comparer une chaîne à une autre, en évitant les différences de casse, etc. Elle est conçue pour fonctionner avec `sort()`, retournant 1, 0, ou -1, selon la manière dont chaque paire d'enregistrements correspond.

Ainsi, le résultat de cette fonction de tri (et c'est un exemple assez trivial) trie le tableau par lastName :

```js
[
  {
    firstName: 'Lucille',
    lastName: 'Boure',
    // ... 
  },{
    firstName: 'Bob',
    lastName: 'Francis'
    //... 
  },{
    firstName: 'Janet',
    lastName: 'Francis',
    // ... 
  },{
    firstName: 'Alexia',
    lastName: 'Francis',
    // ... 
  }
]
```

Pas si impressionnant, vraiment – nous avons trié par nom de famille, mais qu'en est-il du nom ET du prénom ? Pouvez-nous faire cela ?

## Nous avons le pouvoir !

La réponse est, bien sûr, oui. Si vous avez lu jusqu'ici, il serait stupide de ma part de vous faire attendre et de ne pas vous donner une bonne réponse.

Le truc à retenir est, si la première comparaison retourne une valeur fausse (dans ce cas, `0`), alors nous pouvons passer à une seconde. Et, si nous voulons, une troisième ou quatrième ou...

Voici à quoi pourrait ressembler la fonction de comparaison, pour trier par `lastName`, puis par `firstName` :

```js
const sortByLastAndFirst = function(a, b){
  return (a.lastName.localeCompare(b.lastName) ) 
      || (a.firstName.localeCompare(b.firstName) )
};
```

Et voici un **[exécutable](https://tech.io/snippet/udV2Qfx)** de celui-ci. Les parenthèses dans ce retour sont simplement pour rendre les choses un peu plus lisibles, mais voici la logique en cours :

```
comparaison de a et b dans une fonction de tri, retour :

* si a.lastName vient avant ou après b.lastName,
  : retourner la valeur de cette comparaison.
  
* si a.lastName et b.lastName sont les mêmes, nous obtenons une valeur fausse, donc 
  : passer à la comparaison suivante, a.firstName et b.firstName
```

## Récapitulatif avant de continuer

À ce stade, nous savons que nous pouvons enchaîner les clauses de tri `return`. Et c'est puissant. Cela nous donne une certaine profondeur et rend nos tris un peu plus flexibles. Nous pouvons le rendre plus lisible et plus "plug-and-play", également.

Maintenant, je vais changer un peu les choses, j'utiliserai les _fonctions fléchées_ ES6 :

```js
// Mettons ensemble quelques blocs de construction plus petits...
const byLast = (a, b)=>a.last.localeCompare(b.last);
const byFirst = (a, b)=>a.first.localeCompare(b.first);

// Et ensuite nous pouvons les combiner (ou les composer) ! 
const byLastAndFirst = (a, b) => byLast(a, b) || byFirst(a, b);
```

Cela fait la même chose que celle que nous venons de faire, mais c'est un peu plus compréhensible. En lisant cette fonction `byLastAndFirst`, nous pouvons voir qu'elle trie par last, puis par first.

Mais c'est un peu pénible – devons-nous écrire le même code chaque fois ? Regardez `byLast` et `byFirst` dans ce dernier exemple. Ils sont les mêmes, à l'exception du nom de la propriété. Pouvez-nous le corriger pour ne pas avoir à écrire les mêmes fonctions encore et encore ?

## Troisième couplet, même que... peu importe.

Bien sûr ! Commençons par essayer de créer une fonction générique `sortByProp`. Celle-ci prendra un nom de propriété, et deux objets, et les comparera.

```js
const sortByProp = function(prop, a, b){
  if (typeof a[prop] === 'number')
    return a[prop]-b[prop];
    
  // else implicite - si nous sommes ici, alors nous n'avons pas retourné ci-dessus 
  // Ceci est simplifié, je n'attends qu'un nombre ou une chaîne.
  return a[prop].localeCompare(b[prop]); };
```

Pour que nous puissions l'utiliser dans notre fonction de tri comme comparateur :

```js
myArray.sort((a, b)=> sortByProp('lastName', a,b) 
                   || sortByProp('firstName', a, b) );
```

Et cela semble assez génial, n'est-ce pas ? Je veux dire, nous n'avons maintenant qu'une seule fonction, et nous pouvons comparer par n'importe quelle propriété. Et hey, elle inclut une vérification pour comparer les nombres vs les chaînes, pour la victoire !

Oui, mais cela me dérange. J'aime pouvoir prendre ces petites fonctions (les `byLast` et `byFirst`), et savoir qu'elles fonctionneront toujours avec `sort` – mais avec la signature de paramètre de notre `byProp(prop, a, b)`, nous ne pouvons pas utiliser cela ! Sort ne connaît pas notre fonction `prop`.

## Que doit faire un développeur ?

Eh bien, ce que nous faisons ici, c'est que nous écrivons une fonction qui retourne une fonction. Celles-ci sont connues sous le nom de **fonctions d'ordre supérieur**, et elles sont une fonctionnalité puissante de JavaScript.

Nous voulons créer une fonction (que nous appellerons toujours `sortByProp()`) à laquelle nous pouvons passer un nom de propriété. En retour, nous obtenons une fonction qui se souvient de notre nom de propriété dans sa portée interne, mais qui peut accepter la signature de paramètre `(a, b)` de la fonction de tri.

Ce que ce modèle fait, c'est créer une "fermeture". La propriété est passée dans la fonction externe en tant que paramètre, donc elle existe uniquement dans la portée de cette fonction externe.

Mais à l'intérieur de celle-ci, nous retournons une fonction qui peut référencer les valeurs qui s'y trouvent. Une fermeture a besoin de deux parties : une portée privée, et quelques méthodes d'accès à cette portée privée. C'est une technique puissante, et une que j'explorerai davantage à l'avenir.

Voici par où nous allons commencer : d'abord, nous devons redéfinir notre fonction `sortByProp`. Nous savons qu'elle doit prendre une propriété, et qu'elle doit retourner une fonction. De plus, cette fonction retournée devrait prendre les deux propriétés que `sort()` passera :

```js
const sortByProp = function(prop){
  return function(a,b){
    /* ici, nous aurons quelque chose qui se passe */ 
  } 
}
```

Maintenant, lorsque nous appelons celle-ci, nous obtiendrons une fonction en retour. Nous pouvons donc l'assigner à une variable afin de pouvoir l'appeler à nouveau plus tard :

```js
const byLast = sortByProp('lastName');
```

Dans cette ligne, nous avons capturé la fonction qui a été retournée, et l'avons stockée dans `byLast`. De plus, nous venons de créer une _fermeture_, une référence à une portée fermée qui stocke notre variable `prop`, et que nous pouvons utiliser plus tard, chaque fois que nous appelons notre fonction `byLast`.

Maintenant, nous devons revisiter cette fonction `sortByProp` et remplir ce qui se passe à l'intérieur. C'est la même chose que ce que nous avons fait dans la première fonction `sortByProp`, mais maintenant elle est enfermée avec une signature de fonction que nous pouvons utiliser :

```js
const sortByProp = function(prop){
  return function(a,b){
    if(typeof a[prop] === 'number')
      return a[prop]-b[prop];

    return a[prop].localeCompare(b[prop]); 
  } 
}
```

Et pour l'utiliser, nous pouvons simplement :

```js
const byLast = sortByProp('lastName'); 
const byFirst = sortByProp('firstName'); 
// nous pouvons maintenant combiner, ou "composer" ces deux : 
const byLastAndFirst = function(a, b){
  return byLast(a, b) 
      || byFirst(a, b); 
} 

console.log( myArray.sort(byLastAndFirst) );
```

Et notez que nous pouvons étendre cela à la profondeur que nous voulons :

```js
const byLast = sortByProp('lastName'); 
const byFirst = sortByProp('firstName'); 
const byCountry = sortByProp('country'); 
const byState = sortByProp('state'); 
const byCity = sortByProp('city'); 
const byAll = (a, b)=> byCountry(a, b) || byState(a, b) || byCity(a, b) || byLast(a, b) || byFirst(a, b); 

console.log(myArray.sort(byAll) );
```

Ce dernier exemple était profondément pénible. Et c'était fait exprès. Mon prochain article sera une alternative pour faire la même chose, sans avoir à coder manuellement toutes les comparaisons comme cela.

Pour ceux qui aiment voir le tableau complet, je m'attends pleinement à des questions sur une version ES6 de cette même fonction `sortByProp`, simplement parce qu'elles sont jolies. Et elles sont jolies, bien sûr, entre un retour implicite et le beau ternaire. La voici, et voici le **[Tech.io](https://tech.io/snippet/imU4elI)** pour celle-ci :

```js
const byProp = (prop) => (a, b) => typeof(a[prop])==='number'
             ? a[prop]-b[prop] 
             : a[prop].localeCompare(b[prop]);
```

Notez que cette version n'est ni meilleure ni pire que l'autre. Elle a l'air élégante, et elle tire parti de certaines fonctionnalités ES6, mais elle sacrifie la lisibilité. Un développeur junior pourrait regarder cela et lever les mains. S'il vous plaît, ne sacrifiez pas la maintenabilité pour l'ingéniosité.

Merci à tous d'avoir lu !