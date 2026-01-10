---
title: Une introduction rapide à la composition de fonctions en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-12T20:42:35.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-function-composition-in-swift-17f5c9999cee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_o81YbJg_qxXhHaZFWiWhQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Une introduction rapide à la composition de fonctions en Swift
seo_desc: 'By Boudhayan Biswas

  Programmers come across functions every day. A function represents a special type
  of relationship: every input value that the function takes is associated with some
  output value. So in a more generic way, a function is a rule whic...'
---

Par Boudhayan Biswas

Les programmeurs rencontrent des fonctions tous les jours. Une fonction représente un type spécial de relation : chaque valeur d'entrée que la fonction prend est associée à une certaine valeur de sortie. Donc, de manière plus générique, une fonction est une règle qui mappe certaines valeurs d'entrée à une valeur de sortie.

L'idée de base derrière la composition de fonctions est d'appliquer une fonction au résultat d'une autre fonction. C'est donc un concept mathématique de combinaison de fonctions en une seule fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QDF5FSC7IE8GxFd-Y5DbrQ.jpeg)
_Composition de Fonctions_

#### Pour commencer

Discutons-en avec le concept mathématique. Dans le diagramme ci-dessus, « f » et « g » sont deux fonctions. Nous pouvons représenter les fonctions comme suit :

```
f: A -> Bg: B -> C
```

Si nous faisons la composition de ces deux fonctions, alors nous pouvons la représenter comme « g o f » (vous pouvez dire g de f).

```
(g o f): A -> C tel que (g o f)(a) = g(f(a)) pour tout a dans A
```

Essayons d'explorer cela plus en détail avec un exemple simple :

```
Soit f(a) = 2a + 3 & g(a) = 3a + 5, alors la composition de fonctions
```

```
(g o f)(a) = g(f(a)) = 3(f(a)) + 5 = 3(2a + 3) + 5 = 6a + 14
```

Ce concept n'est pas seulement applicable en mathématiques — nous pouvons également l'appliquer dans les langages de programmation. Ces langages sont appelés langages de programmation fonctionnelle. Comprendre ce concept améliore la lisibilité de votre code et le rend plus facile à comprendre pour les autres programmeurs.

#### Introduction à Swift en tant que langage de programmation fonctionnelle

Maintenant, la bonne nouvelle est que Swift est également un langage de programmation fonctionnelle. En programmation Swift, une fonction a le rôle le plus important, donc vous interagirez avec elles quotidiennement. Une fonction Swift peut retourner une valeur, puis nous pouvons utiliser la valeur retournée comme entrée dans une autre fonction. C'est une pratique de programmation courante.

#### Implémentation de la composition de fonctions en Swift

Supposons que nous avons un tableau d'entiers, et nous voulons que la sortie soit un tableau au carré d'entiers pairs uniques. Donc, pour cela, nous implémenterions normalement des fonctions comme ci-dessous :

Ce code nous donne la sortie correcte, mais comme vous pouvez le voir, la lisibilité du code n'est pas excellente. De plus, l'ordre d'appel des fonctions semble être l'inverse de ce que nous voulons, et cela pourrait créer de la confusion pour certains nouveaux programmeurs. Ce bloc de code est difficile à analyser.

C'est là que la composition de fonctions vient à notre secours pour résoudre tous les problèmes ci-dessus. Nous pouvons réaliser la composition de fonctions en tirant parti des génériques, des fermetures et de l'opérateur infixe.

Donc, voyons ce qui se passe dans le bloc de code ci-dessus :

1. Nous avons déclaré un opérateur infixe personnalisé « >>> ». Il a une associativité à gauche et un ordre de priorité comme l'opérateur +.
2. Nous avons déclaré une fonction dont le nom est le même que celui de l'opérateur infixe. La fonction utilise trois génériques T, U, V et elle prend deux fermetures comme paramètres d'entrée.
3. Le paramètre de gauche est une fermeture, et il prend une entrée de type T et retourne une sortie de type U.
4. Le paramètre de droite est également une fermeture, et il prend une entrée de type U et retourne la sortie de type V.
5. Maintenant, la fonction >>> retourne une fonction ou une fermeture, qui a le type (T) → V. La fermeture de sortie prend une entrée de type T et retourne la sortie de type V. Ici, la sortie du paramètre de gauche est l'entrée du paramètre de droite.

```
left :  (T) -> U right: (U) -> V
```

```
Type de sortie : (T) -> V
```

Si vous comprenez la représentation mathématique de la composition de fonctions, alors vous pouvez voir qu'elle est exactement la même que l'implémentation de Swift.

6. Dans le corps de la fonction, il retourne le résultat du paramètre de droite sur le paramètre de gauche.

Maintenant, si nous voulons le même résultat (un tableau au carré d'entiers pairs uniques), nous pouvons le faire avec la composition de fonctions.

C'est une chaîne de fonctions qui retourne le même résultat. L'ordre des fonctions semble maintenant similaire à ce qu'un être humain pourrait penser. Il a une meilleure lisibilité et est plus facile à comprendre pour tout le monde.

Merci d'avoir lu !