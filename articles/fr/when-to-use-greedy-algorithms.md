---
title: Quand utiliser les algorithmes gloutons – Et quand les éviter [Avec des exemples
  de problèmes]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-05T18:11:05.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-greedy-algorithms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ff481f37af2371468bb79ba.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Quand utiliser les algorithmes gloutons – Et quand les éviter [Avec des
  exemples de problèmes]
seo_desc: "By Jose J. Rodríguez\nGreedy algorithms try to find the optimal solution\
  \ by taking the best available choice at every step. \nFor example, you can greedily\
  \ approach your life. You can always take the path that maximizes your happiness\
  \ today. But that d..."
---

Par Jose J. Rodríguez

Les algorithmes gloutons tentent de trouver la solution optimale en prenant le meilleur choix disponible à chaque étape. 

Par exemple, vous pouvez aborder votre vie de manière gloutonne. Vous pouvez toujours prendre le chemin qui maximise votre bonheur aujourd'hui. Mais cela ne signifie pas que vous serez plus heureux demain.

De même, il existe des problèmes pour lesquels les algorithmes gloutons ne donnent pas la meilleure solution. En fait, ils pourraient donner la pire solution possible. 

Mais il y a d'autres cas où nous pouvons obtenir une solution suffisamment bonne en utilisant une stratégie gloutonne.

Dans cet article, je vais écrire sur les algorithmes gloutons et l'utilisation de cette stratégie même lorsqu'elle ne garantit pas que vous trouverez une solution optimale.

La première section est une introduction aux algorithmes gloutons et aux problèmes bien connus qui sont résolubles en utilisant cette stratégie. Ensuite, je parlerai des problèmes pour lesquels la stratégie gloutonne est une très mauvaise option. Et enfin, je vous montrerai un exemple d'une bonne approximation grâce à un algorithme glouton.

> **Note** : La plupart des algorithmes et problèmes dont je discute dans cet article incluent des graphes. Il serait bon que vous soyez familier avec les graphes pour tirer le meilleur parti de cet article.

## Comment fonctionnent les algorithmes gloutons

Les algorithmes gloutons choisissent toujours la meilleure option disponible. 

En général, ils sont moins coûteux en calcul que d'autres familles d'algorithmes comme la programmation dynamique ou la force brute. Cela est dû au fait qu'ils n'explorent pas trop l'espace des solutions. Et, pour la même raison, ils ne trouvent pas la meilleure solution à de nombreux problèmes.

Mais il y a beaucoup de problèmes qui sont résolubles avec une stratégie gloutonne, et dans ces cas, cette stratégie est précisément la meilleure façon de procéder.

L'un des algorithmes gloutons les plus populaires est l'algorithme de Dijkstra qui trouve le chemin avec le coût minimum d'un sommet à un autre dans un graphe. 

Cet algorithme trouve un tel chemin en allant toujours vers le sommet le plus proche. C'est pourquoi nous disons que c'est un algorithme glouton.

Voici le pseudocode de l'algorithme. Je désigne par ```G``` le graphe et par ```s``` le nœud source. 

```pseudocode
Dijkstra(G, s):
    distances <- liste de longueur égale au nombre de nœuds du graphe, initialement tous ses éléments sont égaux à l'infini

    distances[s] = 0

    queue = l'ensemble des sommets de G

    while queue is not empty:

          u <- sommet dans queue avec min distances[u]

          remove u from queue

          for each neighbor v of u:
              temp = distances[u] + value(u,v)

              if temp < distances[v]:
                   distances[v] = temp
     return distances
```

Après avoir exécuté cet algorithme, nous obtenons une liste de ```distances``` telle que ```distances[u]``` est le coût minimum pour aller du nœud ```s``` au nœud ```u```.

Cet algorithme est garanti de fonctionner uniquement si le graphe n'a pas d'arêtes avec des coûts négatifs. Un coût négatif dans une arête peut faire en sorte que la stratégie gloutonne choisisse un chemin qui n'est pas optimal.

Un autre exemple utilisé pour introduire les concepts de la stratégie gloutonne est le problème du sac à dos fractionnaire.

Dans ce problème, nous avons une collection d'objets. Chaque objet a un poids ```Wi``` supérieur à zéro, et un profit ```Pi``` également supérieur à zéro. 

Nous avons un sac à dos avec une capacité ```W``` et nous voulons le remplir de manière à obtenir le profit maximum. Bien sûr, nous ne pouvons pas dépasser la capacité du sac à dos.

Dans la version fractionnaire du problème du sac à dos, nous pouvons prendre soit l'objet entier, soit seulement une fraction de celui-ci. Lorsque nous prenons une fraction ```0 <= X <= 1``` du i-ème objet, nous obtenons un profit égal à ```X*Pi``` et nous devons ajouter ```X*Wi``` au sac. 

Nous pouvons résoudre ce problème en utilisant une stratégie gloutonne. Je ne vais pas discuter de la solution ici. Si vous ne la connaissez pas, je vous recommande d'essayer de la résoudre par vous-même et de chercher ensuite la solution en ligne.

Le nombre de problèmes que nous pouvons résoudre en utilisant des algorithmes gloutons est énorme. Mais le nombre de problèmes que nous ne pouvons pas résoudre de cette manière est encore plus grand. La section suivante traite de ces derniers problèmes - ceux que nous ne devrions pas résoudre de cette manière.

## Quand être glouton est la pire des options

Dans la section précédente, nous avons vu deux exemples de problèmes qui sont résolubles en utilisant une stratégie gloutonne. C'est génial car ces algorithmes sont assez rapides.

Mais, comme je l'ai dit, l'algorithme de Dijkstra ne fonctionne pas dans les graphes avec des arêtes négatives. 

Et le problème est encore plus grand. Je peux toujours construire un graphe avec des arêtes négatives de manière à ce que la solution de Dijkstra soit aussi mauvaise que je le souhaite ! Considérez l'exemple suivant qui a été extrait de [Stackoverflow](https://stackoverflow.com/questions/6799172/negative-weights-using-dijkstras-algorithm/6799344#6799344)


![rmowk.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1606581688656/MrsI2Usdb.png)

L'algorithme de Dijkstra échoue à trouver la distance entre ```A``` et ```C```. Il trouve ```d(A, C) = 0``` alors qu'elle devrait être -200. Et si nous diminuons la valeur de l'arête ```D -> B```, nous obtiendrons une distance qui sera encore plus éloignée de la distance minimale réelle.

De même, lorsque nous ne pouvons pas diviser les objets dans le problème du sac à dos (le problème du sac à dos 0-1), la solution que nous obtenons en utilisant une stratégie gloutonne peut être également très mauvaise. Nous pouvons toujours construire une entrée pour le problème qui fait en sorte que l'algorithme glouton échoue gravement.

Un autre exemple est le problème du voyageur de commerce (TSP). Étant donné une liste de villes et les distances entre chaque paire de villes, quel est le trajet le plus court possible qui visite chaque ville exactement une fois et revient à la ville d'origine ?

Nous pouvons aborder le problème de manière gloutonne en allant toujours vers la ville la plus proche possible. Nous sélectionnons n'importe quelle ville comme première et appliquons cette stratégie.

Comme dans les exemples précédents, nous pouvons toujours construire une disposition des villes de manière à ce que la stratégie gloutonne trouve la pire solution possible.

Dans cette section, nous avons vu qu'une stratégie gloutonne pourrait nous mener à la catastrophe. Mais il existe des problèmes pour lesquels une telle approche peut approximer la solution optimale assez bien.

## Quand être glouton n'est pas si grave

Nous avons vu qu'une stratégie gloutonne peut devenir aussi mauvaise que nous le voulons pour certains problèmes. Cela signifie que nous ne pouvons pas l'utiliser pour obtenir la solution optimale ni même une bonne approximation de celle-ci.

Mais il existe des exemples où les algorithmes gloutons nous fournissent de très bonnes approximations ! Dans ces cas, l'approche gloutonne est très utile car elle tend à être moins coûteuse et plus facile à implémenter.

Le couverture de sommets d'un graphe est l'ensemble minimum de sommets tel que chaque arête du graphe a au moins l'une de ses extrémités dans l'ensemble.

C'est un problème très difficile. En fait, il n'existe aucune solution efficace et exacte pour celui-ci. Mais la bonne nouvelle est que nous pouvons faire une bonne approximation avec un algorithme glouton.

Nous sélectionnons n'importe quelle arête ```<u, v>``` du graphe, et ajoutons ```u``` et ```v``` à l'ensemble. Ensuite, nous supprimons toutes les arêtes qui ont ```u``` ou ```v``` comme l'une de leurs extrémités, et nous répétons le processus précédent tant que le graphe restant a des arêtes.

Voici le pseudocode de l'algorithme précédent :

```pseudocode
vertexCover(G):
    VertexCover <- {} // ensemble vide
    E' <- arêtes de G

    while E' is not empty:
          VertexCover <- VertexCover U {u,v} où <u,v> est dans E'
          E' = E' - {<u, v> U arêtes incidentes à u, v}

     return VertexCover
```

Comme vous pouvez le voir, c'est un algorithme simple et relativement rapide. Mais le meilleur, c'est que la solution sera toujours inférieure ou égale à deux fois la solution optimale ! Nous n'obtiendrons jamais un ensemble qui est plus grand que deux fois la plus petite couverture de sommets, peu importe comment le graphe d'entrée a été construit.

Je ne vais pas inclure la démonstration de cette affirmation dans cet article, mais vous pouvez la prouver en remarquant que pour chaque arête ```<u, v>``` que nous ajoutons à la couverture de sommets, soit ```u``` soit ```v``` est dans la solution optimale (c'est-à-dire, dans la plus petite couverture de sommets).

De nombreux informaticiens travaillent pour trouver plus de ces approximations. Il y a plus d'exemples, mais je vais m'arrêter ici. 

C'est un domaine de recherche intéressant et très actif en informatique et en mathématiques appliquées. Avec ces approximations, nous pouvons obtenir de très bonnes solutions pour des problèmes très difficiles en implémentant des algorithmes assez simples.

## Conclusions

Dans cet article, je vous ai donné une introduction superficielle aux algorithmes gloutons. Nous avons vu des exemples de problèmes qui peuvent être résolus en utilisant la stratégie gloutonne. Ensuite, j'ai parlé de certains problèmes pour lesquels la stratégie gloutonne est une mauvaise option. Et enfin, nous avons vu un exemple d'un algorithme glouton qui vous donnera une solution approximative à un problème difficile.

Parfois, nous pouvons résoudre un problème en utilisant une approche gloutonne, mais il est difficile de trouver la bonne stratégie. Et démontrer la justesse des algorithmes gloutons (pour des solutions exactes ou approximatives) peut être très difficile. Donc, il y a beaucoup de choses que nous pouvons discuter sur les algorithmes gloutons !

Si vous avez aimé cet article et que vous voulez que je continue à produire ce type de contenu, faites-le moi savoir en le partageant et en me taguant. Vous pouvez également me suivre sur Twitter pour plus de contenu lié à l'informatique.