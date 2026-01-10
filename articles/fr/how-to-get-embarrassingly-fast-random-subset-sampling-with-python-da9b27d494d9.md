---
title: Comment obtenir un échantillonnage de sous-ensembles aléatoires extrêmement
  rapide avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T09:48:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-embarrassingly-fast-random-subset-sampling-with-python-da9b27d494d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NZyHwP7xOOY7nNodbLbF3g.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment obtenir un échantillonnage de sous-ensembles aléatoires extrêmement
  rapide avec Python
seo_desc: 'By Kirill Dubovikov

  Imagine that you are developing a machine learning model to classify articles. You
  have managed to get an unreasonably large text file which contains millions of identifiers
  of similar articles that belong to the same class. You a...'
---

Par Kirill Dubovikov

Imaginez que vous développez un modèle de machine learning pour classer des articles. Vous avez réussi à obtenir un fichier texte démesurément grand qui contient des millions d'identifiants d'articles similaires appartenant à la même classe. Vous n'êtes pas sûr que les identifiants proches les uns des autres soient indépendants.

Par exemple, un parseur pourrait écrire les identifiants d'articles d'un seul site ensemble. Maintenant, vous souhaitez obtenir un grand nombre d'échantillons aléatoires à partir d'un tableau de plusieurs millions d'éléments pour créer un ensemble de données d'entraînement ou compter certaines statistiques empiriques. Cette situation peut se présenter en pratique plus fréquemment que vous ne le pensez.

Grâce à Binder, vous pouvez [**jouer avec le code en ligne**](https://beta.mybinder.org/v2/gh/kdubovikov/fastsampling/master) sans rien installer localement. Ou vous pouvez cloner le [dépôt Github](https://github.com/kdubovikov/fastsampling). Veuillez noter que tous les benchmarks peuvent différer d'une machine à l'autre.

Eh bien, quel est le problème ? Utilisons [numpy](http://www.numpy.org) !

Sur Macbook Pro, ce code s'exécute en **environ 1,4 s par boucle**. Si vous souhaitez obtenir 100 000 échantillons, cela prendra environ un jour et demi. Aïe !

#### Accélérer ❄️

Que s'est-il passé ? Pour générer un échantillon aléatoire, numpy.random.choice permute le tableau **chaque fois que nous l'appelons**. Lorsque la taille de notre échantillon n'est qu'une fraction de la longueur totale du tableau, nous n'avons pas besoin de mélanger le tableau chaque fois que nous voulons prendre un échantillon. Mélangeons-le une fois et prenons des échantillons à partir du début du tableau mélangé.

Lorsque nous arrivons au dernier élément, nous devons le mélanger à nouveau. Cette optimisation a également un effet secondaire très agréable : nous aurons moins de collisions (échantillons répétitifs).

Il est maintenant temps de coder cela :

Cette fois, nous obtenons 21,1 µs ± 979 ns par boucle, ce qui est plus rapide de plusieurs ordres de grandeur.

#### Encore plus rapide ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*JXF21j3Z9zt16aysLEb-Tw.jpeg)

Pouvons-nous le faire encore plus vite ? Oui, mais nous devons passer au natif. [Cython](http://cython.org) traduit le code de type Python en code natif optimisé C ou C++ qui peut être compilé et utilisé comme un module Python familier et convivial par la suite.

Vous pouvez utiliser Cython dans les notebooks Jupyter en chargeant l'extension Cython avec `%load_ext Cython`, et en utilisant la magie `%%cython` comme première instruction dans une cellule avec du code Cython.

Presque tout le code Python est un code Cython valide. Mais pour en tirer le meilleur parti, nous devons utiliser les extensions fournies par Cython :

* Nous annotons statiquement tous les types pour les signatures de fonctions et la définition de variables afin d'utiliser des variables natives C au lieu d'objets Python lents lorsque cela est possible
* Nous utilisons le mot-clé `cdef` pour les fonctions qui n'ont pas besoin d'être exportées comme une API Python. Les appels `cdef` sont beaucoup plus rapides.
* Nous désactivons l'indexation négative et la vérification des limites de tableau avec `@cython.wraparound` et `@cython.boundscheck` pour obtenir plus de vitesse

Ce léger refactoring est suffisant pour obtenir une accélération raisonnable (2x sur mon ordinateur portable) par rapport à la version Python.

Je suis obligé de dire que Cython est bien plus qu'un traducteur Python-C optimisé. Avec cet outil génial, vous pouvez également :

* Surmonter les limitations du [GIL](https://www.google.ru/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=0ahUKEwjQlqzs6eDWAhXhCJoKHW0mD0cQFghFMAU&url=https%3A%2F%2Fwiki.python.org%2Fmoin%2FGlobalInterpreterLock&usg=AOvVaw20YulOZd6sYn-anu5E4rz4)
* [Paralléliser votre code](http://cython.readthedocs.io/en/latest/src/userguide/parallelism.html) avec des wrappers OpenMP de haut niveau (avec des threads, pas des processus !)
* Utiliser des tableaux rapides via [memoryviews](http://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html)
* Exposer des tampons de mémoire brute au code Python via [Buffer Protocol](http://cython.readthedocs.io/en/latest/src/userguide/buffer.html)

#### Qu'en est-il des collisions ? ?

Les collisions d'échantillonnage se produisent lorsque nous obtenons un élément répétitif lors de l'échantillonnage du tableau. Pour simplifier, supposons que le tableau ne contient pas de doublons.

Nous allons comparer les deux algorithmes en termes de collisions. Nous pouvons collecter un grand nombre d'échantillons à partir du même tableau pour chacun des algorithmes, puis compter le nombre total de collisions.

Lorsque nous répétons ce processus plusieurs fois et enregistrons les résultats, nous collectons en fait un échantillon aléatoire de comptes de collisions pour les deux algorithmes.

Ayant ces échantillons à portée de main, nous pouvons appliquer des statistiques pour les comparer. Dans ce cas, nous utiliserons un test t (vous pouvez en lire plus sur la distribution t dans mon [article précédent](https://medium.freecodecamp.org/the-t-distribution-a-key-statistical-concept-discovered-by-a-beer-brewery-dbfdc693184) et plus sur le test t [ici](http://www.statisticshowto.com/probability-and-statistics/t-test/)).

La valeur p que nous obtenons est 0, ce qui signifie que le résultat que nous avons obtenu est significatif.

Faisons un graphique et voyons la différence :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZquEFfe47SUXzzPBCFx0w.jpeg)

Comme vous pouvez le voir, nous obtenons des nombres de collisions beaucoup plus bas en bonus.

#### Conclusion

Merci beaucoup d'avoir lu jusqu'à la fin ! Donnez-moi quelques applaudissements ? si vous avez trouvé ce matériel utile — cela aidera à faire passer le mot.