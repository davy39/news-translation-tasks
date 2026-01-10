---
title: Que signifie le fait qu'un code soit « facile à comprendre » ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-30T14:52:14.000Z'
originalURL: https://freecodecamp.org/news/what-does-it-mean-when-code-is-easy-to-reason-about-4e6f63eb386f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ksdpItuqJJshToI3D39RaQ.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Que signifie le fait qu'un code soit « facile à comprendre » ?
seo_desc: 'By Preethi Kasireddy

  You’ve probably heard the expression “easy to reason about” enough times to make
  your ears bleed.

  The first time I heard this expression, I had no idea what the person meant by it.

  Does it mean functions that are easy to understa...'
---

Par Preethi Kasireddy

Vous avez probablement entendu l'expression « facile à comprendre » suffisamment de fois pour en avoir les oreilles qui saignent.

La première fois que j'ai entendu cette expression, je n'avais aucune idée de ce que la personne voulait dire par là.

_Est-ce que cela signifie des fonctions faciles à comprendre ?_

_Est-ce que cela signifie des fonctions qui fonctionnent correctement ?_

_Est-ce que cela signifie des fonctions faciles à analyser ?_

Après un certain temps, j'avais entendu « facile à comprendre » dans tant de contextes que je pensais que c'était juste un autre mot à la mode semi-sans signification pour les développeurs.

…Mais est-ce vraiment sans signification ?

La vérité est que l'expression a bel et bien une signification importante. Elle capture une idée assez complexe, ce qui rend son décodage un peu délicat. Difficile ou non, avoir une compréhension de haut niveau de ce à quoi ressemble un code « facile à comprendre » nous aide absolument à écrire de meilleurs programmes.

À cette fin, cet article sera dédié à la dissection de l'expression « facile à comprendre » telle qu'elle se rapporte aux conversations techniques que nous avons en tant que développeurs.

### Comprendre le comportement de votre programme

Une fois que vous avez écrit un morceau de code, vous voulez généralement aussi comprendre le comportement du programme, comment il interagit avec d'autres parties du programme, et les propriétés qu'il présente.

Par exemple, prenons le morceau de code ci-dessous. Cela devrait multiplier un tableau de nombres par 3.

Comment pouvons-nous tester qu'il fonctionne comme prévu ? Une façon logique est de passer un tas de tableaux en entrée et de s'assurer qu'il retourne toujours le tableau avec chaque élément multiplié par 3.

Cela semble bon jusqu'à présent. Nous avons testé que la fonction fait ce que nous voulons qu'elle fasse.

Mais comment savons-nous qu'elle ne fait pas ce que nous **_ne voulons pas_** qu'elle fasse ? Par exemple, avec une inspection minutieuse, nous pouvons voir que la fonction mute le tableau original.

Est-ce ce que nous voulions ? Et si nous avions besoin de références à la fois au tableau original et au tableau résultant ? Trop tard, je suppose.

Ensuite, voyons ce qui se passe si nous passons le même tableau plusieurs fois différentes — retourne-t-il toujours le même résultat pour une entrée donnée ?

Oh oh. Il semble que lorsque nous avons passé le tableau **[1, 2, 3]** à la fonction la première fois, il a retourné **[3, 6, 9]**, mais plus tard il a retourné **[ 49, 98, 147 ]**. Ce sont des résultats très différents.

C'est parce que la fonction **multiplyByThree** dépend d'une variable externe **multiplier**. Donc, si l'état externe du programme fait que la variable **multiplier** change entre les appels à la fonction **multiplyByThree**, le comportement de la fonction change même si nous passons le même tableau à la fonction.

Eeek. Cela ne semble plus si bien. Creusons un peu plus.

Jusqu'à présent, nous avons testé des entrées de tableau parfaites. Maintenant, que se passe-t-il si nous faisons ceci :

Qu'est-ce que c'est que ça ?!?

Le programme semblait bien en surface — lorsque nous prenons quelques minutes pour l'évaluer, cependant, c'était une autre histoire.

Nous avons vu qu'il retourne parfois une erreur, parfois la même chose que vous avez passée, et seulement occasionnellement le résultat attendu. De plus, il a quelques effets secondaires non intentionnels (mutation du tableau original) et ne semble pas être cohérent dans ce qu'il retourne pour une entrée donnée (puisqu'il dépend de l'état externe).

Maintenant, regardons une fonction **multiplyByThree** légèrement différente :

Tout comme ci-dessus, nous pouvons tester la correction.

Cela semble bon jusqu'à présent.

Testons aussi pour voir s'il fait ce que nous ne voulons pas qu'il fasse. Est-ce qu'il mute le tableau original ?

Non. Le tableau original est intact !

Est-ce qu'il retourne la même sortie pour une entrée donnée ?

Oui ! Puisque la variable **multiplier** est maintenant dans la portée de la fonction, même si nous déclarons une variable **multiplier** en double dans la portée globale, cela n'affectera pas le résultat.

Est-ce qu'il retourne la même chose si nous passons un tas de différents types d'arguments ?

Oui ! Maintenant, la fonction se comporte de manière plus prévisible — elle retourne soit une erreur, soit un nouveau tableau résultant.

À ce stade, à quel point sommes-nous confiants que cette fonction fait exactement ce que nous voulons qu'elle fasse ? Avons-nous couvert tous les cas limites ? Essayons quelques autres :

Zut. Il semble que notre fonction ait encore besoin d'un peu de travail. Lorsque le tableau lui-même contient des éléments inattendus, comme **undefined** ou des chaînes de caractères, nous voyons à nouveau un comportement étrange.

Essayons de le corriger en ajoutant une autre vérification dans notre boucle for pour vérifier les éléments de tableau invalides :

Avec cette nouvelle fonction, pourquoi ne pas essayer à nouveau ces deux cas limites :

Super. Maintenant, il retourne également une erreur si l'un des éléments du tableau n'est pas un nombre au lieu d'une sortie aléatoire et bizarre.

### Enfin, une définition

En passant par les étapes ci-dessus, nous avons lentement construit une fonction qui est facile à comprendre parce qu'elle possède ces qualités clés :

1. N'a pas d'effets secondaires non intentionnels
2. Ne dépend pas ou n'affecte pas l'état externe
3. Étant donné le même argument, elle retournera toujours la même sortie correspondante (également connu sous le nom de « [transparence référentielle](https://en.wikipedia.org/wiki/Referential_transparency) »).

### Façons de garantir ces propriétés

Il existe de nombreuses façons différentes de garantir que notre code est facile à comprendre. Examinons-en quelques-unes :

#### **Tests unitaires**

Tout d'abord, nous pouvons écrire des tests unitaires pour isoler des morceaux de code et vérifier qu'ils fonctionnent comme prévu :

Des tests unitaires comme ceux-ci nous aident à vérifier que notre code se comporte correctement et nous donnent une documentation vivante sur le fonctionnement des petites parties du système global. Le bémol avec les tests unitaires est que, sauf si vous êtes très réfléchis et minutieux, il est incroyablement facile de manquer des cas limites problématiques.

Par exemple, nous n'aurions jamais découvert que le tableau original est muté à moins que nous n'ayons pensé à le tester. Donc notre code n'est aussi robuste que nos tests.

#### **Types**

En plus des tests, nous pouvons également utiliser des types pour faciliter la compréhension du code. Par exemple, si nous utilisions un vérificateur de types statique pour JavaScript comme [Flow](https://flowtype.org/), nous pourrions nous assurer que le tableau d'entrée est toujours un tableau de nombres :

Les types nous obligent à déclarer explicitement que le tableau d'entrée est un tableau de nombres. Ils aident à créer des restrictions sur notre code qui empêchent de nombreux types d'erreurs d'exécution comme nous l'avons vu précédemment. Dans notre cas, nous n'avons plus à penser à vérifier que chaque élément du tableau est un nombre — c'est une garantie qui nous est donnée avec les types.

#### **Immuabilité**

Enfin, une autre chose que nous pouvons faire est d'utiliser des données immuables. Les données immuables signifient simplement que les données ne peuvent pas être modifiées une fois qu'elles sont créées. Cela aide à éviter les effets secondaires non intentionnels.

Dans notre exemple précédent, par exemple, si le tableau d'entrée était immuable, cela aurait empêché le comportement imprévisible où le tableau original est muté. Et si le **multiplier** était immuable, cela empêcherait les situations où une autre partie du programme peut muter notre multiplier.

Certaines des façons dont nous pouvons tirer parti de l'immuabilité sont d'utiliser un langage de programmation fonctionnelle qui garantit intrinsèquement l'immuabilité ou d'utiliser une bibliothèque externe, comme [Immutable.js](https://facebook.github.io/immutable-js/), qui impose l'immuabilité sur un langage existant.

En tant qu'exploration amusante, j'utiliserai [Elm](http://elm-lang.org/), un langage de programmation fonctionnelle typé, pour démontrer comment l'immuabilité nous aide :

Ce petit extrait fait la même chose que notre fonction JavaScript **multiplyByThree** précédente, sauf qu'il est maintenant en [Elm](http://elm-lang.org/). Puisque Elm est un langage typé, vous verrez à la ligne 6 que nous définissons les types d'entrée et de sortie pour la fonction **multiplyByThree** comme étant tous deux une liste de nombres. La fonction elle-même utilise l'opération de base **map** pour générer le tableau résultant.

Maintenant que nous avons défini notre fonction en Elm, faisons une dernière série des mêmes tests que nous avons faits pour notre fonction **multiplyByThree** précédente :

Comme vous pouvez le voir, le résultat est celui que nous attendions et le **originalArray** n'a pas été muté.

Maintenant, essayons de tromper Elm et essayons de muter le multiplier :

Aha ! Elm vous empêche de faire cela. Il lance une erreur très amicale.

Et si nous passions une chaîne de caractères comme argument, au lieu d'un tableau de nombres ?

Il semble qu'Elm ait également attrapé cela. Parce que nous avons déclaré l'argument comme une Liste de nombres, nous ne pouvons pas passer autre chose qu'une Liste de nombres même si nous essayions !

Nous avons un peu triché dans cet exemple en utilisant un langage de programmation fonctionnelle qui a à la fois des types et de l'immuabilité. Le point que je voulais prouver est qu'avec ces deux fonctionnalités, nous n'avons plus à penser à ajouter manuellement des vérifications pour tous les cas limites afin d'obtenir les trois propriétés dont nous avons discuté. Les types et l'immuabilité garantissent cela pour nous, et à leur tour, nous pouvons raisonner sur notre code plus facilement 💡

### Maintenant, c'est à vous de raisonner sur votre code

Je vous mets au défi de prendre un moment la prochaine fois que vous entendez quelqu'un dire, _« XYZ rend le code facile à comprendre »_ ou _« ABC rend le code difficile à comprendre »_. Remplacez ce mot à la mode par les propriétés mentionnées ci-dessus, et essayez de comprendre ce que la personne veut dire. Quelles propriétés le morceau de code possède-t-il qui le rendent facile à comprendre ?

Personnellement, faire cet exercice m'a aidé à penser de manière critique sur le code et, à son tour, m'a motivé à penser à la façon d'écrire des programmes qui sont plus faciles à comprendre. J'espère qu'il en sera de même pour vous aussi !

J'aimerais entendre vos réflexions sur d'autres propriétés que j'aurais pu manquer et que vous pensez être importantes. Veuillez laisser vos commentaires dans les commentaires !