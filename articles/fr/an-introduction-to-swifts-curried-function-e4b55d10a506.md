---
title: Une introduction au currying de fonctions en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T05:01:42.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-swifts-curried-function-e4b55d10a506
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kx8jzRIUN8lytiKmR8ALPA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction au currying de fonctions en Swift
seo_desc: 'By Boudhayan Biswas

  When you hear the word “curry”, the very first thing that probably passes through
  your mind is a great part of Indian cuisine. Indian people use a very complex combination
  of spices to prepare the dish. They put all the ingredient...'
---

Par Boudhayan Biswas

Lorsque vous entendez le mot « **curry** », la première chose qui vous vient probablement à l'esprit est un grand plat de la cuisine indienne. Les Indiens utilisent une combinaison très complexe d'épices pour préparer le plat. Ils mettent tous les ingrédients un par un pour faire un bon curry.

Le principal truc est donc de mettre tous les ingrédients un par un. De même, en programmation, le **currying** est la technique qui consiste à convertir une fonction prenant plusieurs arguments en une fonction prenant un argument à la fois, puis retournant une fonction.

Mais dans n'importe quel langage de programmation, nous pouvons facilement déclarer une fonction prenant plusieurs arguments à la fois, et la plupart des programmeurs y sont habitués. Alors pourquoi utiliser le currying ?

Outre le fait de rendre votre nourriture exceptionnelle, il est utilisé pour permettre l'enchaînement d'opérations sur un ensemble de données particulier. Ainsi, au lieu d'écrire des algorithmes complexes avec quelques boucles imbriquées, vous pouvez accomplir la même chose avec quelques commandes simples.

Il utilise la réutilisabilité du code, et moins vous avez de code à écrire, moins vous aurez d'erreurs ! Vous pouvez présenter le currying / le dé-currying comme un moyen d'énoncer l'élimination et l'introduction de règles pour et dans la logique constructive. Cela fournit une connexion à une motivation plus élégante de son existence.

Les programmeurs ont la possibilité de déclarer chaque fonction de deux manières équivalentes. Dans le currying, une fonction prend un seul argument et retourne une fonction. Ensuite, la fonction retournée prend un argument et retourne le résultat final.

Dans l'esprit de chaque programmeur, il peut y avoir une question : pourquoi prendre la direction la plus compliquée, c'est-à-dire d'abord écrire une fonction qui retourne une fonction, puis appeler à nouveau la deuxième fonction ?

Regardons d'abord le style le plus populaire de définition d'une fonction :

```swift
func multiply1(_ x: Int, _ y: Int) -> Int {
  return x*y
}
```

La fonction ci-dessus prend deux arguments et retourne leur résultat de multiplication.

Nous pouvons maintenant définir la même fonction d'une manière différente :

```
func multiply2(_ x: Int) -> (Int) -> Int {
  return { $0 * x }
}
```

La différence entre ces deux fonctions réside dans leur style d'appel :

```
multiply1(3, 4) // retourne 12
```

```
multiply2(3)(4) // retourne 12
```

Dans la première fonction, nous passons les deux arguments en même temps. Dans la deuxième fonction, nous passons le premier argument (qui retourne lui-même une fonction), puis nous passons le deuxième argument.

En fait, les deux fonctions font la même chose ici. Ces deux exemples montrent comment nous pouvons toujours transformer une fonction prenant plusieurs arguments à la fois en une série de fonctions prenant un argument à la fois. C'est le processus du **currying**. Ainsi, la fonction **_multiply2_** est la version curryfiée de **_multiply1_**. 

Nous pouvons représenter la deuxième fonction comme une chaîne de fonctions comme ceci :

```
//Avantage : 1
```

```
multiply2(3)(multiply2(4)(multiply2(5)(6))) // retourne 360
```

```
//Avantage : 2
```

```
let multiplier = multiply2(2)
```

```
let integerList = 1...100
```

```
let x = integerList.map(multiplier) // retourne [2, 4, 6, 8, 10, 12 ...]
```

Ce sont quelques-uns des avantages de la fonction curryfiée. Vous pouvez toujours enchaîner les opérations avec quelques étapes simples. Génial, non ?

Regardons un autre exemple :

Maintenant, créons une **MorningWalk** pour dimanche et ajoutons 100 pas.

Donc, ici, nous appelons la méthode d'instance **_addSteps()_** sur l'instance elle-même.

Mais nous pouvons aussi faire la même chose de manière curryfiée comme ceci :

Cela fait la même chose que ce que nous avons fait ci-dessus. D'abord, nous attribuons les méthodes **_addSteps_** et **_minusSteps_** à deux variables différentes. À ce stade, nous n'appelons aucune fonction. Nous avons simplement fait des références aux fonctions, comme des pointeurs de fonction. À l'étape suivante, nous appelons réellement les fonctions qui sont stockées dans **_stepIncreaser_** et **_stepDecreaser_**. 

Maintenant, **_stepIncreaser_** prend un seul argument qui est l'instance **MorningWalk**, et retourne une fonction dont le type est **_(Int) ->_** (). Ainsi, la fonction retournée prend un argument de type Int et ne retourne rien. Ici, la fonction retournée et la fonction **_addSteps()_** ont le même type de signature de méthode. Le même concept s'applique à **_stepDecreaser_**. 

Ainsi, enfin, nous pouvons dire qu'une méthode d'instance en Swift est aussi une méthode de type. Elle prend une instance de la classe comme argument et retourne une fonction, qui prendra ensuite d'autres arguments et retournera/mettra à jour le résultat final.

Nous pouvons appeler les méthodes ci-dessus comme ceci aussi :

#### Conclusion

Dans cet article, nous avions une fonction avec plus d'un argument. Nous l'avons transformée en une fonction qui prenait toujours un seul argument à la fois, résultant en une autre fonction, jusqu'à ce qu'il n'y ait plus d'argument. Cela nous a ensuite donné le résultat final. Nous pouvons donc dire que les fonctions ne sont rien de plus que des valeurs ordinaires qui peuvent être produites et retournées par d'autres fonctions.

Maintenant, vous avez quelque chose de nouveau et d'intéressant à essayer dans vos tâches de programmation quotidiennes !