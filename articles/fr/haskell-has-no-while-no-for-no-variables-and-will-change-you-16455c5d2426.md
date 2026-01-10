---
title: Comment un langage de programmation purement fonctionnel peut changer votre
  vie.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T16:34:37.000Z'
originalURL: https://freecodecamp.org/news/haskell-has-no-while-no-for-no-variables-and-will-change-you-16455c5d2426
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KtsVK65nfJz8MohWwdEHWQ.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment un langage de programmation purement fonctionnel peut changer votre
  vie.
seo_desc: 'By Andrea Zanin

  I believe everyone should learn Haskell, even if you won’t use it in your work.
  It’s beautiful, and it changes the way you think.

  Haskell who?

  Introductions first: what is Haskell? Haskell is a lazy, purely functional programming
  lang...'
---

Par Andrea Zanin

Je crois que tout le monde devrait apprendre Haskell, même si vous ne l'utiliserez pas dans votre travail. C'est magnifique, et cela change votre façon de penser.

#### Haskell qui ?

Commençons par les présentations : qu'est-ce que Haskell ? Haskell est un langage de programmation paresseux et purement fonctionnel.

Qu'est-ce que cela signifie ?

Eh bien, paresseux signifie que Haskell n'exécutera pas vos commandes immédiatement, mais attendra jusqu'à ce que vous ayez besoin du résultat. Au début, cela peut sembler étrange, mais cela permet quelques fonctionnalités assez intéressantes — comme les listes infinies :

```
evenNumbers = [0, 2..]
```

Ce snippet déclarera un tableau contenant tous les nombres pairs. Mais comme nous l'avons dit, Haskell est paresseux, donc il ne calculera rien jusqu'à ce qu'il soit forcé de le faire.

```
take 10 evenNumbers
```

Le code retourne les 10 premiers éléments de evenNumbers, donc Haskell ne calculera que ceux-ci.

**Bonus** : comme vous pouvez le voir, en Haskell, vous appelez une fonction sans parenthèses. Vous entrez simplement le nom de la fonction suivi des arguments (comme dans le terminal, si vous voulez).

Nous avons également dit que Haskell est purement fonctionnel. Cela signifie que, en général, les fonctions n'ont pas d'effets secondaires. Ce sont des boîtes noires qui prennent des entrées et produisent des sorties sans affecter le programme d'une autre manière.

**Bonus** : Cela rend les tests beaucoup plus faciles, car vous n'avez pas un état mystérieux qui va casser votre fonction. Tout ce dont votre fonction a besoin est passé en argument et peut être testé.

#### Math, récursion, et Haskell entrent dans un bar

J'ajouterais également que Haskell ressemble vraiment aux maths. Je vais m'expliquer avec un exemple : la suite de Fibonacci.

![Image](https://cdn-media-1.freecodecamp.org/images/HZdgRtDDXfrZrDZK7aH-TY7gtgA2CsZSmUe-)
_Suite de Fibonacci telle que définie en maths et en Haskell. La version Haskell n'est pas du tout optimisée_

Comme vous pouvez le voir, les définitions sont très similaires. Trop similaires, pourriez-vous dire.

Alors, où sont les boucles ?

Vous n'en avez pas besoin ! Ces quatre lignes suffisent en Haskell pour calculer la suite de Fibonacci. C'est presque trivial. C'est une définition récursive, ce qui signifie que la fonction s'appelle elle-même. Pour faciliter la compréhension, voici un exemple de fonction récursive :

```
factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial x = x * factorial (x-1)
```

Voici ce que fait l'ordinateur lors du calcul de l'appel _factorial 5_ :

```
factorial 5 = 5 * factorial 4
factorial 4 = 4 * factorial 3
factorial 3 = 3 * factorial 2
factorial 2 = 2 * factorial 1
factorial 1 = 1 * factorial 0
factorial 0 = 1
```

```
factorial 1 = 1 * 1 = 1
factorial 2 = 2 * 1 = 2
factorial 3 = 3 * 2 = 6
factorial 4 = 4 * 6 = 24
factorial 5 = 5 * 24 = 120
```

Vous pourriez penser que cette approche est inefficace, mais ce n'est pas vrai. Avec un peu de soin, vous pouvez atteindre une vitesse similaire à celle du C, parfois même légèrement meilleure (voir [ce fil stackoverflow](https://goo.gl/qbUhR5) pour plus d'informations).

#### _Attendez ! Avez-vous dit pas de variables ?_

Oui, Haskell n'a pas de variables — juste des constantes. Eh bien, en théorie, Haskell a des variables. Mais vous les utilisez rarement.

Comment est-ce possible ? Vous ne pouvez pas coder sans variables, c'est fou !

Eh bien, la plupart des langages sont impératifs. Cela signifie que la plupart du code va vers expliquer à l'ordinateur comment exécuter une tâche. Haskell, en revanche, est déclaratif. Donc la plupart de votre code va dans la définition du résultat que vous voulez (constantes ≈ définitions). Ensuite, le compilateur trouvera comment le faire.

Comme nous l'avons déjà découvert, les fonctions en Haskell sont pures. Il n'y a pas d'état à modifier, et pas besoin de variables. Vous passez des données à travers diverses fonctions et récupérez le résultat final.

#### Système de types (non, je ne vais pas entrer dans le débat statique vs dynamique)

En apprenant le système de types de Haskell, la première chose qui m'a laissé bouche bée était les types de données algébriques. À première vue, ils ressemblent un peu aux énumérations.

```
data Hand = Left | Right
```

Nous venons de définir un type de données Hand qui peut prendre la valeur Left ou Right. Mais voyons un exemple un peu plus complexe :

```
data BinTree = Empty          | Leaf Int          | Node BinTree BinTree
```

Nous définissons un arbre binaire, en utilisant un type récursif. Les définitions de types peuvent être récursives !

#### D'accord, je comprends : Haskell est génial

* Mais où puis-je en apprendre plus ? Ma suggestion personnelle est le grand livre gratuit [Learn You a Haskell for Great Good](https://goo.gl/JxQy3h)
* Mais je veux quelque chose qui peut m'aider à trouver un emploi ! Beaucoup des grandes fonctionnalités de Haskell peuvent également être utilisées en JavaScript (bien que avec une syntaxe légèrement plus complexe et des bibliothèques supplémentaires). Pour en savoir plus, consultez mon [Introduction Pratique à la Programmation Fonctionnelle en JS](https://goo.gl/3CvMF7).