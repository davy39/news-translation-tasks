---
title: Une introduction facile à la portée lexicale en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T18:26:21.000Z'
originalURL: https://freecodecamp.org/news/lexical-scoping-in-javascript-e876cd221b74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LoVCoRxQBamxz5xRTYaXeA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction facile à la portée lexicale en JavaScript
seo_desc: 'By Michael McMillan

  Lexical scoping is a topic that frightens many programmers. One of the best explanations
  of lexical scoping can be found in Kyle Simpson’s book You Don’t Know JS: Scope
  and Closures. However, even his explanation is lacking becaus...'
---

Par Michael McMillan

La portée lexicale est un sujet qui effraie de nombreux programmeurs. L'une des meilleures explications de la portée lexicale peut être trouvée dans le livre de Kyle Simpson [You Don't Know JS: Scope and Closures](https://www.amazon.com/You-Dont-Know-JS-Closures/dp/1449335586). Cependant, même son explication est incomplète car il n'utilise pas d'exemple réel.

L'un des meilleurs exemples réels de la façon dont la portée lexicale fonctionne, et pourquoi elle est importante, peut être trouvé dans le célèbre manuel, "The Structure and Interpretation of Computer Programs" (SICP) de Harold Abelson et Gerald Jay Sussman. Voici un lien vers une version PDF du livre : [SICP](https://web.mit.edu/alexmv/6.037/sicp.pdf).

SICP utilise Scheme, un dialecte de Lisp, et est considéré comme l'un des meilleurs textes d'introduction à l'informatique jamais écrits. Dans cet article, j'aimerais revisiter leur exemple de portée lexicale en utilisant JavaScript comme langage de programmation.

#### Notre exemple

L'exemple utilisé par Abelson et Sussman est le calcul des racines carrées en utilisant la méthode de Newton. La méthode de Newton fonctionne en déterminant des approximations successives pour la racine carrée d'un nombre jusqu'à ce que l'approximation atteigne une limite de tolérance acceptable. Travaillons à travers un exemple, comme le font Abelson et Sussman dans SICP.

L'exemple qu'ils utilisent est la recherche de la racine carrée de 2. Vous commencez par faire une supposition de la racine carrée de 2, disons 1. Vous améliorez cette supposition en divisant le nombre original par la supposition, puis en faisant la moyenne de ce quotient et de la supposition actuelle pour obtenir la supposition suivante. Vous arrêtez lorsque vous atteignez un niveau d'approximation acceptable. Abelson et Sussman utilisent la valeur 0,001. Voici un aperçu des premières étapes du calcul :

```
Racine carrée à trouver : 2Première supposition : 1Quotient : 2 / 1 = 2Moyenne : (2+1) / 2 = 1.5Supposition suivante : 1.5Quotient : 1.5 / 2 = 1.3333Moyenne : (1.3333 + 1.5) / 2 = 1.4167Supposition suivante : 1.4167Quotient : 1.4167 / 2 = 1.4118Moyenne : (1.4167 + 1.4118) / 2 = 1.4142
```

Et ainsi de suite jusqu'à ce que la supposition atteigne notre limite d'approximation, qui pour cet algorithme est 0,001.

### Une fonction JavaScript pour la méthode de Newton

Après cette démonstration de la méthode, les auteurs décrivent une procédure générale pour résoudre ce problème en Scheme. Plutôt que de vous montrer le code Scheme, je vais l'écrire en JavaScript :

```
function sqrt_iter(guess, x) {  if (isGoodEnough(guess, x)) {    return guess;  }    else {    return sqrt_iter(improve(guess, x), x);  }}
```

Ensuite, nous devons développer plusieurs autres fonctions, y compris isGoodEnough() et improve(), ainsi que quelques autres fonctions auxiliaires. Nous commencerons par improve(). Voici la définition :

```
function improve(guess, x) {  return average(guess, (x / guess));}
```

Cette fonction utilise une fonction auxiliaire average(). Voici cette définition :

```
function average(x, y) {  return (x+y) / 2;}
```

Maintenant, nous sommes prêts à définir la fonction isGoodEnough(). Cette fonction sert à déterminer quand notre supposition est suffisamment proche de notre tolérance d'approximation (0,001). Voici la définition de isGoodEnough() :

```
function isGoodEnough(guess, x) {  return (Math.abs(square(guess) - x)) < 0.001;}
```

Cette fonction utilise une fonction square(), qui est facile à définir :

```
function square(x) {  return x * x;}
```

Maintenant, il nous faut une fonction pour démarrer les choses :

```
function sqrt(x) {  return sqrt_iter(1.0, x);}
```

Cette fonction utilise 1.0 comme supposition de départ, ce qui est généralement très bien.

Maintenant, nous sommes prêts à tester nos fonctions pour voir si elles fonctionnent. Nous les chargeons dans une console JS et calculons quelques racines carrées :

```
> .load sqrt_iter.js> sqrt(3)1.7321428571428572> sqrt(9)3.00009155413138> sqrt(94 + 87)13.453624188555612> sqrt(144)12.000000012408687
```

Les fonctions semblent bien fonctionner. Cependant, il y a une meilleure idée qui se cache ici. Ces fonctions sont toutes écrites indépendamment, même si elles sont destinées à travailler en conjonction les unes avec les autres. Nous n'allons probablement pas utiliser la fonction isGoodEnough() avec un autre ensemble de fonctions, ou seule. De plus, la seule fonction qui compte pour l'utilisateur est la fonction sqrt(), puisque c'est celle qui est appelée pour trouver une racine carrée.

### La portée de bloc cache les fonctions auxiliaires

La solution ici est d'utiliser la portée de bloc pour définir toutes les fonctions auxiliaires nécessaires dans le bloc de la fonction sqrt(). Nous allons supprimer square() et average() de la définition, car ces fonctions pourraient être utiles dans d'autres définitions de fonctions et ne sont pas aussi limitées à l'utilisation dans un algorithme qui implémente la méthode de Newton. Voici la définition de la fonction sqrt() maintenant avec les autres fonctions auxiliaires définies dans la portée de sqrt() :

```
function sqrt(x) {  function improve(guess, x) {    return average(guess, (x / guess));  }  function isGoodEnough(guess, x) {    return (Math.abs(square(guess) - x)) > 0.001;  }  function sqrt_iter(guess, x) {    if (isGoodEnough(guess, x)) {      return guess;    }    else {      return sqrt_iter(improve(guess, x), x);    }  }  return sqrt_iter(1.0, x);}
```

Nous pouvons maintenant charger ce programme dans notre console et calculer quelques racines carrées :

```
> .load sqrt_iter.js> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> sqrt(3.14159)1.772581833543688> sqrt(144)12.000000012408687
```

Remarquez que vous ne pouvez pas appeler l'une des fonctions auxiliaires depuis l'extérieur de la fonction sqrt() :

```
> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> improve(1,2)ReferenceError: improve is not defined> isGoodEnough(1.414, 2)ReferenceError: isGoodEnough is not defined
```

Puisque les définitions de ces fonctions (improve() et isGoodEnough()) ont été déplacées à l'intérieur de la portée de sqrt(), elles ne peuvent pas être accessibles à un niveau supérieur. Bien sûr, vous pouvez déplacer l'une des définitions de fonctions auxiliaires en dehors de la fonction sqrt() pour y avoir accès globalement comme nous l'avons fait avec average() et square().

Nous avons grandement amélioré notre implémentation de la méthode de Newton, mais il y a encore une chose que nous pouvons faire pour améliorer notre fonction sqrt() en la simplifiant encore plus en tirant parti de la portée lexicale.

### Améliorer la clarté avec la portée lexicale

Le concept derrière la portée lexicale est que lorsqu'une variable est liée à un environnement, d'autres procédures (fonctions) qui sont définies dans cet environnement ont accès à la valeur de cette variable. Cela signifie que dans la fonction sqrt(), le paramètre x est lié à cette fonction, ce qui signifie que toute autre fonction définie dans le corps de sqrt() peut accéder à x.

Sachant cela, nous pouvons simplifier encore plus la définition de sqrt() en supprimant toutes les références à x dans les définitions de fonctions puisque x est maintenant une variable libre et accessible par toutes. Voici notre nouvelle définition de sqrt() :

```
function sqrt(x) {  function isGoodEnough(guess) {    return (Math.abs(square(guess) - x)) > 0.001;  }  function improve(guess) {    return average(guess, (x / guess));  }  function sqrt_iter(guess) {    if (isGoodEnough(guess)) {      return guess;    }    else {      return sqrt_iter(improve(guess));    }  }  return sqrt_iter(1.0);}
```

Les seules références au paramètre x sont dans les calculs où la valeur de x est nécessaire. Chargeons cette nouvelle définition dans la console et testons-la :

```
> .load sqrt_iter.js> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> sqrt(123+37)12.649110680047308> sqrt(144)12.000000012408687
```

La portée lexicale et la structure de bloc sont des caractéristiques importantes de JavaScript et nous permettent de construire des programmes plus faciles à comprendre et à gérer. Cela est particulièrement important lorsque nous commençons à construire des programmes plus grands et plus complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/S2PRBM-GSiBQBuXWf1q614LInt0MBmr9rTuN)