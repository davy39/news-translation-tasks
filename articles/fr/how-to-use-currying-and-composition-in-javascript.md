---
title: Comment utiliser le currying et la composition en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-18T22:06:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-currying-and-composition-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/lydia-tallent-SkY-jiMGYfA-unsplash.jpg
tags:
- name: composition
  slug: composition
- name: currying
  slug: currying
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser le currying et la composition en JavaScript
seo_desc: 'By Tobias Parent

  A great conversation I had this evening got me thinking about and revisiting a concept
  I''ve toyed with before – currying. But this time, I''d like to explore it with
  you all!

  The concept of currying is not a new one, but it is very us...'
---

Par Tobias Parent

Une excellente conversation que j'ai eue ce soir m'a fait réfléchir et revisiter un concept avec lequel j'ai joué auparavant – le currying. Mais cette fois, j'aimerais l'explorer avec vous tous !

Le concept de currying n'est pas nouveau, mais il est très utile. Il est également fondamental pour la programmation fonctionnelle, et est une sorte de porte d'entrée pour penser aux fonctions de manière plus modulaire.

Et l'idée de composition, de combiner des fonctions pour en créer de plus grandes, plus complexes, plus utiles, peut sembler assez intuitive, mais est également un composant clé de la programmation fonctionnelle.

Lorsque nous commençons à les combiner, alors des choses amusantes peuvent se produire. Voyons comment cela pourrait fonctionner.

## Curry, quelqu'un ?

Les fonctions curryfiées font à peu près la même chose que toute autre fonction, mais la manière de les aborder est un peu différente.

Supposons que nous voulions une fonction qui pourrait vérifier la distance entre deux points : `{x1, y1}` et `{x2, y2}`, par exemple. La formule pour cela est un peu mathématique, mais rien que nous ne puissions gérer :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/distance-formula.svg)
_La formule pour la distance entre deux points, qui est une application du théorème de Pythagore._

Ordinativement, l'appel de notre fonction pourrait ressembler à ceci :

```js
const distance = (start, end) => Math.sqrt( Math.pow(end.x-start.x, 2) + Math.pow(end.y-start.y, 2) );

console.log( distance( {x:2, y:2}, {x:11, y:8} );
// logs 10.816653826391969
```

Maintenant, curryfier une fonction, c'est la forcer à prendre un seul paramètre à la fois. Donc plutôt que de l'appeler comme `distance( start, end )`, nous l'appellerions comme ceci : `distance(start)(end)`. Chaque paramètre est passé individuellement, et chaque appel de fonction retourne une autre fonction, jusqu'à ce que tous les paramètres aient été fournis.

Il pourrait être plus facile de montrer que d'expliquer, alors regardons la fonction de distance ci-dessus comme une fonction curryfiée :

```js
const distance = function(start){
  // nous avons une portée fermée ici, mais nous allons retourner une fonction qui
  //  peut y accéder - créant effectivement une "fermeture".
  return function(end){
    // maintenant, dans cette fonction, nous avons tout ce dont nous avons besoin. nous pouvons faire
    //  le calcul et retourner le résultat.
    return Math.sqrt( Math.pow(end.x-start.x, 2) + Math.pow(end.y-start.y, 2) );
  }
}

console.log( distance({x:2, y:2})({x:11, y:8});
// logs 10.816653826391969 encore
```

Cela semble être un travail énorme pour obtenir le même résultat ! Nous _pouvons_ le raccourcir un peu, en utilisant les fonctions fléchées ES6 :

```js
const distancewithCurrying = 
        (start) => 
          (end) => Math.sqrt( Math.pow(end.x-start.x, 2) +
                              Math.pow(end.y-start.y, 2) );
```

Mais encore une fois, cela semble être beaucoup de remue-ménage pour aucun gain réel, à moins que nous commençons à penser à nos fonctions de manière plus abstraite.

Rappelez-vous, les fonctions ne peuvent retourner qu'une seule chose. Bien que nous puissions fournir n'importe quel nombre de paramètres, nous ne recevrons qu'une seule valeur, qu'il s'agisse d'un nombre, d'un tableau, d'un objet ou d'une fonction. Nous ne recevons qu'une seule chose en retour. Et maintenant, avec une fonction curryfiée, nous avons une fonction qui ne peut recevoir qu'une seule chose. Il peut y avoir une connexion là.

Comme il se trouve, la puissance des fonctions curryfiées réside dans la capacité à les combiner et à les _composer_.

Considérons notre formule de distance – que se passerait-il si nous écrivions un jeu "capture le drapeau", et qu'il serait utile de calculer rapidement et facilement la distance de chaque joueur par rapport au drapeau. Nous pourrions avoir un tableau de joueurs, chacun contenant une localisation `{x, y}`. Avec un tableau de valeurs `{x,y}`, une fonction réutilisable pourrait être très pratique. Jouons avec cette idée pendant une minute :

```js
const players = [
  {
    name: 'Alice',
    color: 'aliceblue',
    position: { x: 3, y: 5}
  },{
    name: 'Benji',
    color: 'goldenrod',
    position: { x: -4, y: -4}
  },{
    name: 'Clarissa',
    color: 'firebrick',
    position: { x: -2, y: 8}
  }
];
const flag = { x:0, y:0};

```

Voici notre configuration : nous avons un emplacement de départ, `flag`, et nous avons un tableau de joueurs. Nous avons deux fonctions différentes définies pour calculer la différence, voyons la différence :

```js
// Étant donné cela, voyons si nous pouvons trouver un moyen de mapper 
//  ces distances ! Faisons-le d'abord avec la première
//  formule de distance.
const distances = players.map( player => distance(flag, player.position) );
/***
 * distances == [
 *   5.830951894845301, 
 *   5.656854249492381, 
 *   8.246211251235321
 * ]
 ***/

// en utilisant une fonction curryfiée, nous pouvons créer une fonction qui contient déjà
//  notre point de départ.
const distanceFromFlag = distanceWithCurrying(flag);
// Maintenant, nous pouvons mapper nos joueurs pour extraire leur position, et
//  mapper à nouveau avec cette formule de distance :
const curriedDistances = players.map(player=>player.position)
                                .map(distanceFromFlag)
/***
 * curriedDistances == [
 *   5.830951894845301, 
 *   5.656854249492381, 
 *   8.246211251235321
 * ]
 ***/
```

Ici, nous avons utilisé notre fonction `distanceCurried` pour appliquer un paramètre, le point de départ. Cela a retourné une fonction qui prend un autre paramètre, le point d'arrivée. En mappant les joueurs, nous pouvons créer un nouveau tableau avec _seulement_ les données dont nous avons besoin, et ensuite passer ces données dans notre fonction curryfiée !

C'est un outil puissant, et il peut prendre un certain temps pour s'y habituer. Mais en créant des fonctions curryfiées et en les composant avec d'autres fonctions, nous pouvons créer des fonctions très complexes à partir de parties plus petites et plus simples.

## Comment composer des fonctions curryfiées

Pouvoir mapper des fonctions curryfiées est très utile, mais vous trouverez également d'autres grandes utilisations pour elles. C'est le début de la "Programmation Fonctionnelle" : écrire de petites fonctions pures qui fonctionnent correctement comme ces bits atomiques et ensuite les combiner comme des blocs de construction.

Voyons comment nous pourrions prendre des fonctions curryfiées, et les composer en de plus grandes. Cette prochaine exploration abordera les fonctions de filtrage.

D'abord, un peu de travail préparatoire. `Array.prototype.filter()`, la fonction de filtrage ES6, nous permet de définir une fonction de rappel, une qui prend une valeur d'entrée ou des valeurs et retourne un vrai ou faux basé sur cela. Voici un exemple :

```js
// un tableau source,
const ages = [11, 14, 26, 9, 41, 24, 108];
// une fonction de filtrage. Prend une entrée, et retourne vrai/faux à partir de celle-ci.
function isEven(num){
  if(num%2===0){
    return true;
  } else {
    return false;
  }
}
// ou, en style ES6 :
const isEven = (num) => num%2===0 ? true : false;
// et appliqué :
console.log( ages.filter(isEven) );
// [14, 26, 24, 108]
```

Maintenant, cette fonction de filtrage, `isEven`, est écrite de manière très spécifique : elle prend une valeur (ou des valeurs, si nous voulons inclure l'index du tableau par exemple), effectue une sorte de hoojinkery interne, et retourne un vrai ou faux. À chaque fois.

C'est l'essence d'une "fonction de rappel de filtre", bien qu'elle ne soit pas exclusive aux filtres – `Array.prototype.every` et `Array.prototype.some` utilisent le même style. Un rappel est testé contre chaque membre d'un tableau, et le rappel prend une certaine valeur et retourne vrai ou faux.

Créons quelques fonctions de filtrage plus utiles, mais cette fois un peu plus avancées. Dans ce cas, nous pourrions vouloir "abstraire" nos fonctions un peu, nous permettant de les rendre plus réutilisables.

Par exemple, des fonctions utiles pourraient être `isEqualTo` ou `isGreaterThan`. Celles-ci sont plus avancées en ce sens qu'elles nécessitent _deux_ valeurs : une à définir comme un terme d'une comparaison (appelons-la un `comparateur`), et une provenant du tableau _étant_ comparé (nous l'appellerons la `valeur`). Voici un peu plus de code :

```js
// nous écrivons une fonction qui prend une valeur...
function isEqualTo(comparator){
  // et cette fonction *retourne* une fonction qui prend une seconde valeur
  return function(value){
    // et nous comparons simplement ces deux valeurs.
    return value === comparator;
  }
}
// encore, en ES6 :
const isEqualTo = (comparator) => (value) => value === comparator;
```

À partir de ce point, je vais m'en tenir à la version ES6, sauf s'il y a une raison particulièrement difficile d'étendre le code à la version classique. Continuons :

```js
const isEqualTo = (comparator) => (value) => value === comparator;
const isGreaterThan = (comparator) => (value) => value > comparator;

// et en application :
const isSeven = isEqualTo(7);
const isOfLegalMajority = isGreaterThan(18);

```

Donc, les deux premières fonctions sont nos fonctions curryfiées. Elles attendent un seul paramètre, et retournent une fonction qui à son tour attend également un seul paramètre.

Sur la base de ces deux fonctions à paramètre unique, nous faisons une simple comparaison. Les deux suivantes, `isSeven` et `isOfLegalMajority`, sont simplement des implémentations de ces deux fonctions.

Jusqu'à présent, nous n'avons pas obtenu de complexité ou d'implication, et nous pouvons rester petits pour quelques autres :

```js
// fonction pour simplement inverser une valeur : true <=> false
const isNot = (value) => !value;

const isNotEqual = (comparator) => (value) => isNot( isEqual(comparator)(value) );
const isLessThanOrEqualTo = (comparator) => (value) => isNot( isGreaterThan(comparator)(value) );
```

Ici, nous avons une fonction utilitaire qui inverse simplement la _véracité_ d'une valeur, `isNot`. En utilisant cela, nous pouvons commencer à composer des pièces plus grandes : nous prenons notre comparateur et notre valeur, nous les passons à travers la fonction `isEqual`, et ensuite nous `isNot` cette valeur pour dire `isNotEqual`.

C'est le début de la composition, et soyons justes – cela semble absolument ridicule. Quel usage possible y aurait-il à écrire tout cela pour obtenir ceci :

```js
// tous les blocs de construction...
const isGreaterThan = (comparator) => (value) => value > comparator;
const isNot = (value) => !value;
const isLessThanOrEqualTo = (comparator) => (value) => isNot( isGreaterThan(comparator)(value) );

// simplement pour obtenir ceci ?
const isTooYoungToRetire = isLessThanOrEqualTo(65)

// et en implémentation :
const ages = [31, 24, 86, 57, 67, 19, 93, 75, 63];
console.log(ages.filter(isTooYoungToRetire)

// est-ce plus propre que :
console.log(ages.filter( num => num <= 65 ) )
```

"Le résultat final est assez similaire dans ce cas, donc cela ne nous économise pas vraiment quelque chose. En fait, étant donné la configuration dans ces trois premières fonctions, cela a pris **beaucoup** plus de travail que de simplement faire une comparaison !"

Et c'est vrai. Je ne vais pas argumenter contre cela. Mais ce n'est que voir une petite partie d'un puzzle beaucoup plus grand.

* Premièrement, nous écrivons du code qui est beaucoup plus _auto-documenté_. En utilisant des noms de fonctions expressifs, nous sommes capables de voir d'un coup d'œil que nous filtrons `ages` pour les valeurs `isTooYoungToRetire`. Nous ne voyons pas les mathématiques, nous voyons la description.
* Deuxièmement, en utilisant de très petites fonctions atomiques, nous sommes capables de tester chaque pièce en isolation, en nous assurant qu'elle fonctionne exactement de la même manière à chaque fois. Plus tard, lorsque nous réutilisons ces petites fonctions, nous pouvons être confiants qu'elles fonctionneront – nous libérant de tester chaque petit morceau lorsque la complexité de notre fonction augmente.
* Troisièmement, en créant des fonctions abstraites, nous pourrions trouver des applications pour elles dans d'autres projets plus tard. Construire une bibliothèque de composants fonctionnels est un atout très puissant, et je recommande fortement de la cultiver.

Avec tout cela dit, nous pouvons également prendre ces fonctions plus petites et commencer à les combiner en pièces de plus en plus grandes. Essayons cela maintenant : ayant à la fois un `isGreaterThan` et `isLessThan`, nous pouvons écrire une belle fonction `isInRange` !

```js
const isInRange = (minComparator) 
                 => (maxComparator)
                   => (value) => isGreaterThan(minComparator)(value)
                              && isLessThan(maxComparator)(value)

const isTwentySomething = isInRange(19)(30);
```

C'est génial – nous avons maintenant un moyen de tester plusieurs conditions en une seule fois. Mais en regardant cela, cela ne semble pas très auto-documenté. Le `&&` au milieu n'est pas terrible, mais nous pouvons faire mieux.

Peut-être si nous écrivions _une autre_ fonction, que nous pourrions appeler `and()`. La fonction `and` peut prendre n'importe quel nombre de conditions, et les tester contre une valeur donnée. Cela serait utile, et extensible.

```js
const and = (conditions) = 
             (value) => conditions.every(condition => condition(value) )

const isInRange = (min)
                 =>(max) 
                  => and([isGreaterThan(min), isLessThan(max) ])
```

Ainsi, la fonction `and` prend n'importe quel nombre de fonctions de filtrage, et ne retourne vrai que si elles sont toutes vraies contre une valeur donnée. Cette fonction `isInRange` dans la dernière fait exactement la même chose que la précédente, mais elle semble beaucoup plus lisible, et auto-documentée.

De plus, elle nous permettra de combiner n'importe quel nombre de fonctions : supposons que nous voulions obtenir des nombres pairs entre 20 et 40, nous combinerions simplement notre fonction `isEven` de tout en haut avec notre fonction `isInRange` en utilisant un `and`, et cela fonctionne simplement.

## Récapitulatif

En utilisant des fonctions curryfiées, nous sommes capables de composer des fonctions ensemble de manière propre. Nous pouvons connecter la sortie d'une fonction directement à l'entrée de la suivante, car les deux prennent un seul paramètre.

En utilisant la composition, nous pouvons combiner des fonctions plus petites ou des fonctions curryfiées en structures beaucoup plus grandes et plus compliquées, avec la confiance que les plus petites parties fonctionnent comme prévu.

C'est beaucoup à digérer, et c'est un concept profond. Mais si vous prenez le temps et explorez cela davantage, je pense que vous commencerez à voir des applications que nous n'avons même pas abordées, et vous pourriez écrire le prochain article comme celui-ci au lieu de moi !