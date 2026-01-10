---
title: Comment comprendre la récursivité en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-10T21:09:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-recursion-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98be740569d1a4ca1bcc.jpg
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
- name: Tutorial
  slug: tutorial
seo_title: Comment comprendre la récursivité en JavaScript
seo_desc: "By Joel P. Mugalu\n\n\"To understand recursion, one must first understand\
  \ recursion\" - Unknown\n\nIf you're like me then you probably didn't understood\
  \ recursion the first time you read about it. \nFor me, it was because\n\nrecursion\
  \ is a hard concept in its..."
---

Par Joel P. Mugalu

> "Pour comprendre la récursivité, il faut d'abord comprendre la récursivité" - Inconnu

Si vous êtes comme moi, vous n'avez probablement pas compris la récursivité la première fois que vous en avez lu.

Pour moi, c'était parce que

1. la récursivité est un concept difficile en soi, et
2. certains des tutoriels et articles que j'ai lus n'étaient pas très clairs.

Pour une raison quelconque, la plupart des articles qui expliquaient la récursivité utilisaient l'exemple des nombres factoriels et de la suite de Fibonacci. Cela signifiait que je devais d'abord comprendre comment fonctionnaient les nombres de Fibonacci, puis les relier à la récursivité.

Mais nous allons prendre une route différente dans cet article.

## Qu'est-ce que la récursivité ?

En termes les plus basiques, la récursivité est lorsqu'une fonction continue de s'appeler elle-même jusqu'à ce qu'elle n'ait plus besoin de le faire.

Quoi ? Oui, la fonction continue de s'appeler elle-même mais avec une entrée plus petite à chaque fois.

Imaginez la récursivité comme une course de circuit. C'est comme courir sur la même piste encore et encore, mais les tours deviennent de plus en plus petits à chaque fois. Finalement, vous allez courir le dernier et plus petit tour, et la course sera terminée.

Même chose avec la récursivité : la fonction continue de s'appeler elle-même avec une entrée plus petite et finalement elle s'arrête.

Mais la fonction ne décide pas toute seule quand s'arrêter. Nous lui disons quand s'arrêter. Nous donnons à la fonction une condition connue sous le nom de **cas de base**.

Le cas de base est la condition qui indique à la fonction quand arrêter de s'appeler elle-même. C'est comme dire à la fonction quel sera le dernier tour de la course pour qu'elle arrête de courir après ce tour.

## Exemples de récursivité

D'accord, c'est ça la récursivité. Regardons quelques exemples pour comprendre comment fonctionne la récursivité.

Vous souvenez-vous de la première fois où vous avez appris les boucles ? Le premier exemple que vous avez probablement fait était un programme de compte à rebours. Faisons cela.

Tout d'abord, comprenons ce que nous voulons que notre programme fasse. Compter à rebours à partir d'un nombre donné jusqu'au plus petit nombre, en soustrayant 1 à chaque fois.

Étant donné le nombre 5, nous nous attendons à ce que la sortie soit quelque chose comme :

```javascript
// 5
// 4
// 3
// 2
// 1

```

D'accord, comment pouvons-nous coder ce programme avec la récursivité ?

```javascript
let countDown = number => {
    // cas de base
    if (number === 0) {
        return;
    }
    console.log(number);
    return countDown(number - 1);
};
console.log(countDown(5)) // 5, 4, 3, 2, 1

```

Alors, que se passe-t-il exactement ici ?

Si vous avez remarqué, la première chose que nous avons faite a été de définir le cas de base. Pourquoi ? Parce que la fonction doit d'abord savoir quand elle va arrêter de s'appeler elle-même.

Vous ne courriez jamais une course sans d'abord savoir quelle est la longueur de la course, n'est-ce pas ?

Si vous ne dites pas à la fonction quand s'arrêter, alors quelque chose appelé stackoverflow va se produire. La pile va se remplir de fonctions qui sont appelées mais ne retournent pas ou ne sont pas retirées de la pile.

La partie récursive se produit réellement à la ligne 7. Là, nous disons à la fonction de continuer à se retourner elle-même mais en réduisant l'entrée de un à chaque fois.

Donc, en effet, voici ce qui se passe :

```javascript
// L'entrée actuelle est 5
// Est-ce que 5 est égal à 0 ?
// Non, d'accord, alors affichons 5 dans la console.
// Elle s'appelle elle-même à nouveau avec number - 1 OU 5 - 1 ;
// L'entrée actuelle est 4
// Est-ce que 4 est égal à 0 ?
// Non, d'accord, alors affichons 4 dans la console
// Répète jusqu'à ce que l'entrée soit 0, donc la fonction arrête de s'appeler elle-même.

```

D'accord, cela avait du sens. Essayons un autre exemple.

Vous savez comment nous pouvons dire qu'un nombre est pair en utilisant l'opérateur de reste (%) ? Donc, si un nombre % 2 == 0, alors ce nombre est pair, ou si un nombre % 3 == 0, alors ce nombre est impair.

Eh bien, il s'avère qu'il y a une autre méthode.

Si nous soustrayons continuellement deux d'un nombre jusqu'à ce que le plus petit nombre soit soit 0 soit 1, alors nous pouvons dire si le nombre est pair ou impair.

Essayons cela avec la récursivité. Donc, étant donné le nombre 6, notre programme devrait retourner **'Pair'** parce que 6-2-2-2 = 0. Étant donné 7, notre programme devrait retourner **'Impair'** parce que 7-2-2-2 = 1.

Voyons cela en code.

```javascript
let oddOrEven = (number) => {
    if (number === 0) {
        return 'Pair';
    } else if (number === 1) {
        return 'Impair';
    } else {
        return oddOrEven(number - 2);
    }
};
console.log(oddOrEven(20)) // Pair
console.log(oddOrEven(75)) // Impair
console.log(oddOrEven(98)) // Pair
console.log(oddOrEven(113)) // Impair

```

Encore une fois, la première étape était de dire à la fonction quand arrêter de s'appeler elle-même. Ensuite, nous lui avons dit quoi faire lorsqu'elle s'appelle elle-même.

La récursivité est essentiellement diviser pour régner. Nous continuons à diviser le problème en le rendant plus petit à chaque fois.

## Récursivité vs Boucles

En termes de vitesse, une boucle s'exécute beaucoup plus rapidement qu'une fonction récursive. Il est également plus facile d'écrire une boucle qu'une fonction récursive. Et en termes de lisibilité, il est plus facile de savoir ce qui se passe avec une boucle qu'avec une fonction récursive.

Mais les fonctions récursives sont très élégantes.

Alors, quel est le meilleur choix ? Efficacité ou vitesse ?

Voici une citation du livre Eloquent JavaScript.

> S'inquiéter de l'efficacité peut être une distraction. C'est encore un autre facteur qui complique la conception du programme, et lorsque vous faites quelque chose qui est déjà difficile, cette chose supplémentaire à laquelle il faut penser peut être paralysante. Par conséquent, commencez toujours par écrire quelque chose qui est correct et facile à comprendre. Si vous êtes inquiet que ce soit trop lent—ce qui n'est généralement pas le cas puisque la plupart du code n'est simplement pas exécuté assez souvent pour prendre une quantité significative de temps—vous pouvez mesurer ensuite et l'améliorer si nécessaire.

À ce stade, vous vous demandez peut-être pourquoi au monde vous choisiriez d'écrire une fonction récursive plutôt qu'une boucle. Je veux dire, les boucles sont beaucoup plus faciles, non ?

Eh bien, c'est vrai – mais il y a certains problèmes qui sont plus faciles à résoudre avec la récursivité. Si vous souhaitez explorer un tel problème, alors envisagez de lire le [chapitre 3](https://eloquentjavascript.net/03_functions.html) d'Eloquent JavaScript.

Maintenant que vous avez découvert une nouvelle super puissance, mettons-la à profit.

Effectuez les exercices suivants en utilisant la récursivité. Si vous pensez pouvoir en faire plus, alors vous pouvez résoudre les célèbres problèmes de factorielle et de suite de Fibonacci.

## Exercices

Si vous souhaitez vous challenger davantage, alors envisagez de résoudre ces problèmes récursifs.

1. Écrivez un programme qui inverse une chaîne de caractères en utilisant la récursivité. Étant donné la chaîne "freeCodeCamp", votre programme devrait retourner "pmaCedoCeerf".
2. Écrivez un programme qui retourne le nombre de fois qu'un caractère apparaît dans une chaîne. Votre programme devrait recevoir une chaîne et le caractère. Il devrait ensuite retourner le nombre de fois que le caractère apparaît dans la chaîne. Étant donné la chaîne "JavaScript" et un caractère "a", votre programme devrait retourner 2.

**Indice** : Essayez de déterminer quand vous voulez que la fonction arrête de s'appeler elle-même et comment retourner une version plus petite du problème à chaque fois que la fonction s'appelle elle-même.

C'est tout pour cet article. J'espère qu'il vous a aidé à mieux comprendre la récursivité.

 _Si vous avez aimé cet article, vous pouvez me suivre sur [Twitter](https://twitter.com/joeepm)._