---
title: Algorithmes gloutons expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-19T18:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-greedy-algorithm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f2e740569d1a4ca413c.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Algorithmes gloutons expliqués avec des exemples
seo_desc: 'What is a greedy algorithm?

  You may have heard about a lot of algorithmic design techniques while sifting through
  some of the articles here. Some of them are:


  Brute Force

  Divide and Conquer

  Greedy Programming

  Dynamic Programming to name a few. In th...'
---

## Qu'est-ce qu'un algorithme glouton ?

Vous avez peut-être entendu parler de nombreuses techniques de conception algorithmique en parcourant certains des articles ici. Certaines d'entre elles sont :

* Force brute
* Diviser pour régner
* Programmation gloutonne
* Programmation dynamique, pour n'en citer que quelques-unes. Dans cet article, vous apprendrez ce qu'est un algorithme glouton et comment vous pouvez utiliser cette technique pour résoudre de nombreux problèmes de programmation qui, autrement, ne semblent pas triviaux.

Imaginez que vous partiez en randonnée et que votre objectif est d'atteindre le pic le plus haut possible. Vous avez déjà la carte avant de commencer, mais il y a des milliers de chemins possibles indiqués sur la carte. Vous êtes trop paresseux et n'avez tout simplement pas le temps d'évaluer chacun d'eux. Oubliez la carte ! Vous avez commencé la randonnée avec une stratégie simple : être glouton et myope. Prenez simplement les chemins qui montent le plus. Cela semble être une bonne stratégie pour la randonnée. Mais est-ce toujours la meilleure ?

Après la fin du voyage et que tout votre corps est endolori et fatigué, vous regardez la carte de randonnée pour la première fois. Oh mon dieu ! Il y a une rivière boueuse que j'aurais dû traverser, au lieu de continuer à marcher vers le haut. Cela signifie qu'un algorithme glouton choisit le meilleur choix immédiat et ne reconsidère jamais ses choix. En termes d'optimisation d'une solution, cela signifie simplement que la solution gloutonne essaiera de trouver des solutions optimales locales - qui peuvent être nombreuses - et pourrait manquer une solution optimale globale.

## Définition formelle

Supposons que vous avez une fonction objectif qui doit être optimisée (soit maximisée, soit minimisée) à un point donné. Un algorithme glouton fait des choix gloutons à chaque étape pour s'assurer que la fonction objectif est optimisée. L'algorithme glouton n'a qu'une seule chance de calculer la solution optimale de sorte qu'il ne revient jamais en arrière et ne reverse pas la décision.

### Les algorithmes gloutons ont certains avantages et inconvénients :

* Il est assez facile de concevoir un algorithme glouton (ou même plusieurs algorithmes gloutons) pour un problème. L'analyse du temps d'exécution pour les algorithmes gloutons sera généralement beaucoup plus facile que pour d'autres techniques (comme Diviser pour régner). Pour la technique Diviser pour régner, il n'est pas clair si la technique est rapide ou lente. Cela est dû au fait qu'à chaque niveau de récursion, la taille des sous-problèmes diminue et le nombre de sous-problèmes augmente.
* La partie difficile est que pour les algorithmes gloutons, vous devez travailler beaucoup plus dur pour comprendre les problèmes de correction. Même avec l'algorithme correct, il est difficile de prouver pourquoi il est correct. Prouver qu'un algorithme glouton est correct relève plus de l'art que de la science. Cela implique beaucoup de créativité. Habituellement, concevoir un algorithme peut sembler trivial, mais prouver qu'il est réellement correct est un problème tout à fait différent.

## Problème de planification d'intervalles

Plongeons dans un problème intéressant que vous pouvez rencontrer dans presque toutes les industries ou tous les domaines de la vie. Certaines instances du problème sont les suivantes :

* Vous avez un ensemble de N plannings de cours pour une seule journée à l'université. Le planning pour un cours spécifique est de la forme (s_time, f_time) où s_time représente l'heure de début de ce cours et de même f_time représente l'heure de fin. Étant donné une liste de N plannings de cours, nous devons sélectionner le nombre maximum de cours à organiser pendant la journée de sorte que **aucun des cours ne se chevauche, c'est-à-dire que si les cours Li et Lj sont inclus dans notre sélection, alors l'heure de début de j >= l'heure de fin de i ou vice versa**.
* Votre ami travaille comme conseiller de camp et il est responsable de l'organisation d'activités pour un groupe de campeurs. L'un de ses plans est le suivant : un mini-triathlon où chaque concurrent doit nager 20 longueurs de piscine, puis faire 10 miles à vélo, puis courir 3 miles.
* Le plan est d'envoyer les concurrents de manière échelonnée, selon la règle suivante : les concurrents doivent utiliser la piscine un à la fois. En d'autres termes, un concurrent nage d'abord les 20 longueurs, sort et commence à faire du vélo.
* Dès que cette première personne est sortie de la piscine, un deuxième concurrent commence à nager les 20 longueurs ; dès qu'il ou elle est sorti et commence à faire du vélo, un troisième concurrent commence à nager, et ainsi de suite.
* Chaque concurrent a un temps de natation prévu, un temps de vélo prévu et un temps de course prévu. Votre ami veut décider d'un planning pour le triathlon : un ordre dans lequel séquencer les départs des concurrents.
* Supposons que le temps de completion d'un planning est le moment le plus précoce auquel tous les concurrents auront terminé les trois épreuves du triathlon, en supposant que les projections de temps sont exactes. Quel est le meilleur ordre pour envoyer les gens, si l'on veut que toute la compétition soit terminée le plus rapidement possible ? Plus précisément, donnez un algorithme efficace qui produit un planning dont le temps de completion est le plus petit possible.

### Le problème de planification des cours

Examinons les différentes approches pour résoudre ce problème.

**Heure de début la plus précoce** c'est-à-dire sélectionner l'intervalle qui a l'heure de début la plus précoce. Regardez l'exemple suivant qui brise cette solution. Cette solution a échoué car il pourrait y avoir un intervalle qui commence très tôt mais qui est très long. Cela signifie que la prochaine stratégie que nous pourrions essayer serait de regarder les intervalles plus petits en premier.

![Heure de début la plus précoce](https://algorithmsandme.files.wordpress.com/2015/03/f268b-jobs.png?w=840)

**Intervalle le plus court en premier** c'est-à-dire que vous finissez par sélectionner les cours dans l'ordre de leur intervalle global qui n'est rien d'autre que leur `heure de fin - heure de début`. Encore une fois, cette solution n'est pas correcte. Regardez le cas suivant.

![Intervalle le plus court en premier](https://cdn-media-1.freecodecamp.org/imgr/4bz2N.png)

Vous pouvez clairement voir que le cours avec l'intervalle le plus court est celui du milieu, mais ce n'est pas la solution optimale ici. Regardons une autre solution pour ce problème en tirant des enseignements de cette solution.

**Intervalle le moins conflictuel en premier** c'est-à-dire que vous devez regarder les intervalles qui causent le moins de conflits. Encore une fois, nous avons un exemple où cette approche échoue à trouver une solution optimale.

![Intervalle le moins conflictuel en premier](https://cdn-media-1.freecodecamp.org/imgr/5LZ9V.png)

Le diagramme nous montre que l'intervalle le moins conflictuel est celui du milieu avec seulement 2 conflits. Après cela, nous ne pouvons choisir que les deux intervalles aux extrémités avec 3 conflits chacun. Mais la solution optimale est de choisir les 4 intervalles au niveau le plus élevé.

**Heure de fin la plus précoce en premier**. C'est l'approche qui nous donne toujours la solution la plus optimale à ce problème. Nous avons tiré de nombreux enseignements des approches précédentes et avons finalement abouti à cette approche. Nous trions les intervalles selon l'ordre croissant de leurs heures de fin et ensuite nous commençons à sélectionner les intervalles dès le début. Regardez le pseudo-code suivant pour plus de clarté.

```
function interval_scheduling_problem(requests)
    schedule \gets \{\}
    while requests is not yet empty
        choose a request i_r \in requests that has the lowest finishing time
        schedule \gets schedule \cup \{i_r\}
        delete all requests in requests that are not compatible with i_r
    end
    return schedule
end

```

## Quand utilisons-nous les algorithmes gloutons

Les algorithmes gloutons peuvent vous aider à trouver des solutions à de nombreux problèmes apparemment difficiles. Le seul problème avec eux est que vous pourriez trouver la solution correcte mais que vous ne pourriez pas vérifier si c'est la bonne. Tous les problèmes gloutons partagent une propriété commune selon laquelle un optimum local peut finalement conduire à un minimum global sans reconsidérer l'ensemble des choix déjà considérés.

Les algorithmes gloutons nous aident à résoudre de nombreux types de problèmes différents, comme :

## Problème du plus court chemin :

%[https://www.youtube.com/watch?v=gdmfOwyQlcI]

## Problème de l'arbre couvrant minimal dans un graphe

%[https://www.youtube.com/watch?v=4ZlRH0eK-qQ]



## Problème de codage de Huffman

%[https://www.youtube.com/watch?v=dM6us854Jk0]

## Problème des K centres

%[https://www.youtube.com/watch?v=dpYZojRuJEI]