---
title: Mémoisation, Récursion et Boucles For en Python Expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-11T17:48:27.000Z'
originalURL: https://freecodecamp.org/news/python-memoization-recursion-for-loop
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/martin-shreder-5Xwaj9gaR0g-unsplash.jpg
tags:
- name: Python
  slug: python
- name: Recursion
  slug: recursion
seo_title: Mémoisation, Récursion et Boucles For en Python Expliquées
seo_desc: 'By Diva Dugar


  There''s more than one way to do things. There''s always different points of views
  and styles of pitching. ~Tim Hudson


  In this article, we will use three different techniques in Python to code a basic
  Fibonacci program which will give t...'
---

Par Diva Dugar

> _Il y a plus d'une façon de faire les choses. Il y a toujours différents points de vue et styles de présentation. ~_**_Tim Hudson_**

Dans cet article, nous allons utiliser trois techniques différentes en Python pour coder un programme Fibonacci de base qui donnera la somme de la séquence comme résultat. La séquence Fibonacci est 0,1,1,2,3,5,8...

Comme vous l'avez peut-être remarqué, nous additionnons les premier et deuxième nombres, 0 et 1, pour obtenir le troisième nombre de la séquence (1) -> 0+1=1. Ensuite, nous additionnons les deuxième et troisième nombres, 1+1=2, pour obtenir le 4ème nombre de la séquence... et ainsi de suite.

Vous pouvez implémenter ce code dans Jupyter, Colab ou tout IDE ou éditeur de texte avec lequel vous êtes à l'aise.

## Comment Coder la Séquence Fibonacci en Utilisant une Boucle For en Python

Ici, j'ai écrit un programme Fibonacci de base en utilisant une boucle for en Python. La logique derrière cela est simple et nous en avons déjà discuté ci-dessus.

La complexité temporelle est O(N) et la complexité spatiale est O(1) ou constante. Mais, c'est en réalité plus compliqué que ce que cette complexité implique.

> "Si votre nombre est inférieur à _N < 94_, et que vous utilisez un entier 64 bits, alors l'algorithme agit comme une complexité linéaire. Cependant, pour _N > 94_, il commence à se comporter comme un algorithme de complexité quadratique." ~ [Michael Veksler](https://qr.ae/pNxAka)

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_1.png)
_Impersion d'un résultat Fibonacci en utilisant une boucle For_

Je vais exécuter cela avec le module `%timeit` de Python. Cela évite un certain nombre de pièges courants pour mesurer les temps d'exécution. Vous pouvez voir plus d'utilisations [ici](https://docs.python.org/3/library/timeit.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_R_1.png)
_Cela a pris 675 nanoSec par boucle pour 10_

## Comment Coder la Séquence Fibonacci avec la Récursion en Python

Ici, nous allons implémenter la séquence en utilisant la récursion. Les fonctions récursives tendent à s'appeler elles-mêmes en répétition jusqu'à ce qu'elles atteignent le cas de base. Ainsi, la récursion crée une structure d'arbre.

Si nous prenons une série Fibonacci de 5, voici l'arbre qui sera créé par la récursion.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_R2_1.png)

La complexité spatiale est O(N) et la complexité temporelle est O(2^N) parce que le nœud racine a 2 enfants et 4 petits-enfants. Et, comme vous pouvez le voir, chaque nœud a 2 enfants.

Maintenant, la profondeur est N, ce qui signifie que nous devons faire cela N fois. De plus, vous avez peut-être remarqué que le sous-arbre droit est plus petit que le sous-arbre gauche, donc le temps d'exécution réel est environ O(1.6^_N_).

Le cas de base : _Fibonacci(2)_ = _Fib(1)_ + _Fib(0)_ = _1 + 0 = 1_

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Recur_op_2.png)
_Impersion du résultat Fibonacci en utilisant la récursion_

L'exemple récursif de Fibonacci est définitivement plus rapide que la boucle for.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Recur_R_2.png)

## Comment Coder la Séquence Fibonacci en Utilisant la Mémoisation en Python

La mémoisation est une technique qui peut améliorer significativement les performances d'une fonction récursive en réduisant la responsabilité computationnelle.

Elle [stocke les résultats des appels de fonctions coûteuses dans un tableau](https://en.wikipedia.org/wiki/Memoization) ou un dictionnaire et retourne les résultats mis en cache lorsque la même entrée est appelée.

Vous pouvez voir l'arbre ci-dessus pour référence, et comment certaines entrées continuent à être recalculées à chaque appel.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Memo_op_3.png)
_Impersion du résultat Fibonacci en utilisant la mémoisation_

La complexité temporelle est O(nlogn).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Memo_R_3.png)

## Quelle est la meilleure méthode : la récursion, les boucles for ou la mémoisation ?

Maintenant, ces techniques ne sont pas censées être meilleures les unes que les autres. Vous devez simplement savoir quand utiliser laquelle. Ce qui dépend, bien sûr, de vos exigences.

L'itération sera plus rapide que la récursion parce que la récursion doit gérer le cadre de la pile d'appels récursifs. Mais, si la récursion est écrite dans un langage qui optimise l'appel terminal, alors elle élimine le surcoût et est presque au même niveau que les boucles for.

Enfin, la mémoisation est meilleure chaque fois que l'espace d'état est clairsemé, c'est-à-dire que tous les sous-problèmes plus petits n'ont pas besoin d'être résolus, mais seulement quelques-uns.

_Merci d'avoir lu ! Si vous avez aimé cet article, vous pouvez **[lire mes autres articles ici](https://medium.com/@divadugar).** Vous pouvez **montrer votre appréciation pour cet article** en le partageant. Vous pouvez également **[me connecter sur LinkedIn](https://www.linkedin.com/in/divadugar).**