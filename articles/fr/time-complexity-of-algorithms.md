---
title: Une introduction à la complexité temporelle des algorithmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-10T10:32:28.000Z'
originalURL: https://freecodecamp.org/news/time-complexity-of-algorithms
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/aron-visuals-322314-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: efficiency
  slug: efficiency
seo_title: Une introduction à la complexité temporelle des algorithmes
seo_desc: 'By Aditya

  In computer science, analysis of algorithms is a very crucial part. It is important
  to find the most efficient algorithm for solving a problem. It is possible to have
  many algorithms to solve a problem, but the challenge here is to choose t...'
---

Par Aditya

En informatique, l'analyse des algorithmes est une partie très cruciale. Il est important de trouver l'algorithme le plus efficace pour résoudre un problème. Il est possible d'avoir de nombreux algorithmes pour résoudre un problème, mais le défi ici est de choisir le plus efficace.

Maintenant, la question est, comment pouvons-nous reconnaître l'algorithme le plus efficace si nous avons un ensemble de différents algorithmes ? Ici, le concept de complexité spatiale et temporelle des algorithmes entre en jeu. La complexité spatiale et temporelle agit comme une échelle de mesure pour les algorithmes. Nous comparons les algorithmes sur la base de leur complexité spatiale (quantité de mémoire) et temporelle (nombre d'opérations).

La quantité totale de mémoire de l'ordinateur utilisée par un algorithme lorsqu'il est exécuté est la complexité spatiale de cet algorithme. Nous ne discuterons pas de la complexité spatiale dans cet article (pour rendre cet article un peu plus petit).

## Complexité temporelle

Ainsi, la complexité temporelle est le nombre d'opérations qu'un algorithme effectue pour accomplir sa tâche (en considérant que chaque opération prend la même quantité de temps). L'algorithme qui effectue la tâche en le plus petit nombre d'opérations est considéré comme le plus efficace en termes de complexité temporelle. Cependant, la complexité spatiale et temporelle est également affectée par des facteurs tels que votre système d'exploitation et votre matériel, mais nous ne les incluons pas dans cette discussion.

Pour comprendre la complexité temporelle, nous allons prendre un exemple dans lequel nous comparerons deux algorithmes différents utilisés pour résoudre un problème particulier.

Le problème est la recherche. Nous devons rechercher un élément dans un tableau (dans ce problème, nous allons supposer que le tableau est trié par ordre croissant). Pour résoudre ce problème, nous avons deux algorithmes :

	1. [Recherche linéaire.](https://www.hackerearth.com/practice/algorithms/searching/linear-search/tutorial/)

	2. [Recherche binaire.](https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/)

Disons que le tableau contient dix éléments, et nous devons trouver le nombre dix dans le tableau.

```javascript
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const search_digit = 10;
```

L'algorithme de **recherche linéaire** comparera chaque élément du tableau au **search_digit**. Lorsqu'il trouve le **search_digit** dans le tableau, il retournera **true**.

Maintenant, comptons le nombre d'opérations qu'il effectue. Ici, la réponse est 10 (puisqu'il compare chaque élément du tableau). Ainsi, la recherche linéaire utilise dix opérations pour trouver l'élément donné (ce sont le nombre maximum d'opérations pour ce tableau ; dans le cas de la recherche linéaire, cela est également connu comme le [pire cas](https://www.geeksforgeeks.org/analysis-of-algorithms-set-2-asymptotic-analysis/) d'un algorithme).

En général, la recherche linéaire prendra **n** nombre d'opérations dans son pire cas (où **n** est la taille du tableau).

Examinons l'algorithme de **recherche binaire** pour ce cas.

La recherche binaire peut être facilement comprise par cet exemple :

<html>
    <body>
        <img src='https://s3.amazonaws.com/learneroo-images/main/binarySearch.png'/>
        <p>Source : <a href='https://www.learneroo.com/modules/71/nodes/399'>Learneroo</a></p>
    </body>
</html>

Si nous essayons d'appliquer cette logique à notre problème, nous comparerons d'abord **search_digit** avec l'élément du milieu du tableau, c'est-à-dire 5. Maintenant, puisque 5 est inférieur à 10, nous commencerons à chercher le **search_digit** dans les éléments du tableau supérieurs à 5, de la même manière jusqu'à ce que nous obtenions l'élément souhaité 10.

Maintenant, essayez de compter le nombre d'opérations que la recherche binaire a prises pour trouver l'élément souhaité. Elle a pris environ quatre opérations. Maintenant, c'était le pire cas pour la recherche binaire. Cela montre qu'il existe une relation [logarithmique](https://www.khanacademy.org/math/algebra2/exponential-and-logarithmic-functions/introduction-to-logarithms/a/intro-to-logarithms) entre le nombre d'opérations effectuées et la taille totale du tableau.

nombre d'opérations = log(10) = 4 (approx)
*pour la base 2*

Nous pouvons généraliser ce résultat pour la recherche binaire comme suit :

Pour un tableau de taille **n**, le nombre d'opérations effectuées par la recherche binaire est : **log(n)**

## La notation Big O

Dans les déclarations ci-dessus, nous avons vu que pour un tableau de taille **n**, la recherche linéaire effectuera **n** opérations pour compléter la recherche. D'autre part, la recherche binaire a effectué **log(n)** nombre d'opérations (les deux pour leurs pires cas). Nous pouvons représenter cela sous forme de graphique (**axe x** : nombre d'éléments, **axe y** : nombre d'opérations).

<html>
    <body>
        <img src="https://www.techtud.com/sites/default/files/public/user_files/tud39880/linearSearch%20vs%20binary%20search%20diagram_0.jpg"/>
        <p>Source : <a href='https://www.techtud.com/computer-science-and-information-technology/algorithms/searching/binary-search' target='_blank'>Techtud</a></p>
    </body>
</html>

Il est assez clair d'après la figure que le taux auquel la complexité augmente pour la recherche linéaire est beaucoup plus rapide que pour la recherche binaire.

Lorsque nous analysons un algorithme, nous utilisons une notation pour représenter sa complexité temporelle et cette notation est la notation Big O.

Par exemple : la complexité temporelle pour la recherche linéaire peut être représentée comme **O(n)** et **O(log n)** pour la recherche binaire (où, **n** et **log(n)** sont le nombre d'opérations).

Les notations de complexité temporelle ou Big O pour certains algorithmes populaires sont listées ci-dessous :

1. Recherche binaire : O(log n)
2. Recherche linéaire : O(n)
3. Tri rapide : O(n * log n)
4. Tri par sélection : O(n * n)
5. Problème du voyageur de commerce : O(n!)

## Conclusion

J'apprécie vraiment vos efforts si vous lisez toujours cet article. Maintenant, vous devez vous demander - pourquoi est-il si important de comprendre la complexité temporelle ?

Nous savons que pour un petit nombre d'éléments (disons 10), la différence entre le nombre d'opérations effectuées par la recherche binaire et la recherche linéaire n'est pas si grande. Mais dans le monde réel, la plupart du temps, nous traitons des problèmes qui ont de grandes quantités de données.

Par exemple, si nous avons 4 milliards d'éléments à rechercher, alors, dans son pire cas, la recherche linéaire prendra 4 milliards d'opérations pour accomplir sa tâche. La recherche binaire accomplira cette tâche en seulement 32 opérations. C'est une grande différence. Maintenant, supposons que si une opération prend 1 ms pour se compléter, alors la recherche binaire prendra seulement 32 ms tandis que la recherche linéaire prendra 4 milliards de ms (soit environ 46 jours). C'est une différence significative.

C'est la raison pour laquelle l'étude de la complexité temporelle devient importante lorsqu'il s'agit d'une telle grande quantité de données.

## Ressources

[Grokking Algorithms- par Aditya Y Bhargava](https://www.manning.com/books/grokking-algorithms)

[Introduction à la notation Big O et à la complexité temporelle- par CS Dojo](https://youtu.be/D6xkbGLQesk)