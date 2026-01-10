---
title: Algorithmes de recherche binaire expliqués en utilisant C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-13T23:36:33.000Z'
originalURL: https://freecodecamp.org/news/what-is-binary-search-algorithm-c-d4b554418ac4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j1pc-U3OlcABlHUk9FAB0w.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: c programming
  slug: c-programming
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Algorithmes de recherche binaire expliqués en utilisant C++
seo_desc: 'By Pablo E. Cortez

  Binary search is one of those algorithms that you’ll come across on every (good)
  introductory computer science class. It’s an efficient algorithm for finding an
  item in an ordered list. For the sake of this example we’ll just assum...'
---

Par Pablo E. Cortez

La recherche binaire est l'un de ces algorithmes que vous rencontrerez dans chaque (bon) cours d'introduction à l'informatique. C'est un algorithme efficace pour trouver un élément dans une liste **ordonnée**. Pour simplifier, nous supposerons que cette liste est un tableau.

Les objectifs de la recherche binaire sont les suivants :

* pouvoir éliminer la moitié du tableau à chaque itération
* minimiser le nombre d'éléments que nous devons parcourir
* nous laisser avec une seule valeur finale

Prenons par exemple le tableau d'entiers suivant :

```
int array[] = {     1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71 };
```

Supposons que nous essayons de trouver la valeur d'index du nombre 7 dans ce tableau. Il y a 17 éléments au total et les valeurs d'index vont de 0 à 16.

Nous pouvons voir que la valeur d'index de 7 est 4, car c'est le cinquième élément du tableau.

Mais quelle serait la meilleure façon pour l'ordinateur de trouver la valeur d'index du nombre que nous cherchons ?

Tout d'abord, nous stockons les valeurs `min` et `max`, telles que `0` et `16`.

```
int min = 0;int max = 16;
```

Maintenant, nous devons faire une supposition. La chose la plus intelligente à faire serait de supposer une valeur d'index au milieu du tableau.

Avec la valeur d'index de 0 à 16 dans ce tableau, la valeur d'index médiane de ce tableau serait 8. Cela contient le nombre 14.

`// Cela arrondira à l'entier inférieur si le quotient n'est pas un entier`  
`int guess = (min + max) / 2;`

Notre supposition est maintenant égale à 8, qui est 14 dans le tableau, puisque `array[8]` est égal à `14`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8cG_3FmI_F0LXrZVuwvN9g.png)
_(Wikimedia Commons.) La première supposition est à la valeur d'index 8, qui stocke le nombre 14._

Si le nombre que nous cherchions était 14, nous aurions terminé !

Étant donné que ce n'est pas le cas, nous allons maintenant éliminer la moitié du tableau. Ce sont tous les nombres après 14, ou la valeur d'index 8, puisque nous savons que 14 est supérieur à 7, et notre supposition est trop élevée.

Après la première itération, notre recherche se limite maintenant à : `1, 3, 4, 6, 7, 8, 10, 13`

Nous n'avons pas besoin de supposer dans la dernière moitié du tableau original, car nous savons que toutes ces valeurs sont trop grandes. C'est pourquoi il est important que nous appliquions la recherche binaire à une liste **ordonnée**.

Puisque notre supposition initiale de 14 était supérieure à 7, nous la diminuons maintenant de 1 et stockons cela dans `max` :

```
max = guess - 1; // max est maintenant égal à 7, qui est 13 dans le tableau
```

Maintenant, la recherche ressemble à ceci :

```
                      1, 3, 4, 6, 7, 8, 10, 13
```

```
min = 0max = 7guess = 3 
```

Parce que notre supposition était trop basse, nous éliminons la moitié inférieure du tableau en augmentant le `min`, contrairement à ce que nous avons fait précédemment pour `max` :

```
min = guess + 1; // min est maintenant 4
```

À l'itération suivante, il nous reste :

```
                             7, 8, 10, 13min = 4max = 7guess = 5
```

Puisque la valeur d'index 5 retourne 8, nous sommes maintenant un au-dessus de notre cible. Nous répétons le processus à nouveau, et il nous reste :

```
                                  7min = 4max = 4guess = 4
```

Et il nous reste une seule valeur, 4, comme index du nombre cible que nous cherchions, qui était 7.

Le but de la recherche binaire est de se débarrasser de la moitié du tableau à chaque itération. Ainsi, nous ne travaillons que sur les valeurs pour lesquelles il est logique de continuer à supposer.

Le pseudo-code pour cet algorithme ressemblerait à ceci :

1. Soit `min = 0`, et soit `max = n` où `n` est la valeur d'index la plus élevée possible
2. Trouver la moyenne de `min` et `max`, arrondir à l'entier inférieur. C'est notre `guess`
3. Si nous avons deviné le nombre, arrêter, nous l'avons trouvé !
4. Si `guess` est trop bas, définir `min` égal à un de plus que `guess`
5. Si `guess` est trop élevé, définir `max` égal à un de moins que `guess`
6. Retourner à l'étape deux.

Voici une solution, écrite en C++ :