---
title: "L'algorithme de Dijkstra \x13 Expliqu\x0E avec un exemple de pseudocode"
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-12-01T20:57:53.000Z'
originalURL: https://freecodecamp.org/news/dijkstras-algorithm-explained-with-a-pseudocode-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/michael-dziedzic-vLmo8kAVVt4-unsplash--2-.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: "L'algorithme de Dijkstra \x13 Expliqu\x0E avec un exemple de pseudocode"
seo_desc: 'You can use algorithms in programming to solve specific problems through
  a set of precise instructions or procedures.

  Dijkstra''s algorithm is one of many graph algorithms you''ll come across. It is
  used to find the shortest path from a fixed node to a...'
---

Vous pouvez utiliser des algorithmes en programmation pour rsoudre des problmes spcifiques  travers un ensemble d'instructions ou de procdures prcises.

L'algorithme de Dijkstra est l'un des nombreux algorithmes de graphes que vous rencontrerez. Il est utilis pour trouver le chemin le plus court d'un nud fixe vers tous les autres nuds d'un graphe.

Il existe diffrentes reprsentations de l'algorithme de Dijkstra. Vous pouvez soit trouver le chemin le plus court entre deux nuds, soit le chemin le plus court d'un nud fixe vers le reste des nuds d'un graphe.

Dans cet article, vous apprendrez comment fonctionne l'algorithme de Dijkstra  l'aide de guides visuels.

## Comment fonctionne l'algorithme de Dijkstra ?

Avant de plonger dans des exemples visuels plus dtaills, vous devez comprendre comment fonctionne l'algorithme de Dijkstra.

Bien que l'explication thorique puisse sembler un peu abstraite, elle vous aidera  mieux comprendre l'aspect pratique.

Dans un graphe donn contenant diffrents nuds, nous devons obtenir le chemin le plus court d'un nud donn vers le reste des nuds.

Ces nuds peuvent reprsenter n'importe quel objet comme les noms de villes, des lettres, et ainsi de suite.

Entre chaque nud se trouve un nombre dsignant la distance entre deux nuds, comme vous pouvez le voir sur l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nodes-1.png)

Nous travaillons gnralement avec deux tableaux  un pour les nuds visits et un autre pour les nuds non visits. Vous en apprendrez plus sur les tableaux dans la section suivante.

Lorsque qu'un nud est visit, l'algorithme calcule combien de temps il a fallu pour atteindre le nud et stocke la distance. Si un chemin plus court vers un nud est trouv, la valeur initiale attribue  la distance est mise  jour.

Notez qu'un nud ne peut pas tre visit deux fois.

L'algorithme s'excute de manire rcursive jusqu' ce que tous les nuds aient t visits.

## Exemple de l'algorithme de Dijkstra

Dans cette section, nous allons examiner un exemple pratique qui montre comment fonctionne l'algorithme de Dijkstra.

Voici le graphe avec lequel nous allons travailler :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nodes.png)

Nous allons utiliser le tableau ci-dessous pour indiquer les nuds visits et leur distance par rapport au nud fixe :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |   |
| B |       |
| C |  |
| D |   |
| E |       |

Nuds visits = []  
Nuds non visits = [A,B,C,D,E]

Ci-dessus, nous avons un tableau montrant chaque nud et la distance la plus courte depuis ce nud jusqu'au nud fixe. Nous n'avons pas encore choisi le nud fixe.

Notez que la distance pour chaque nud dans le tableau est actuellement dsigne comme infinie (). Cela est dû au fait que nous ne connaissons pas encore la distance la plus courte.

Nous avons galement deux tableaux  visits et non visits. Chaque fois qu'un nud est visit, il est ajout au tableau des nuds visits.

Commenons !

Pour simplifier les choses, je vais dcomposer le processus en itrations. Vous verrez ce qui se passe  chaque tape  l'aide de diagrammes.

### Itration #1

La premire itration peut sembler confuse, mais c'est tout  fait normal. Une fois que nous commencerons  rpter le processus  chaque itration, vous aurez une image plus claire de comment l'algorithme fonctionne.

##### **9tape #1 - Choisir un nud non visit**

Nous allons choisir **A** comme nud fixe. Nous allons donc trouver la distance la plus courte de **A** vers tous les autres nuds du graphe.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node1-1.png)

Nous allons donner  **A** une distance de 0 car c'est le nud initial. Le tableau ressemblerait donc  ceci :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |       |
| C |  |
| D |   |
| E |       |

##### **9tape #2 - Trouver la distance depuis le nud actuel**

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node1a-3.png)

La prochaine chose  faire aprs avoir choisi un nud est de trouver la distance de celui-ci aux nuds non visits autour de lui.

Les deux nuds non visits directement relis  **A** sont **B** et **C**.

Pour obtenir la distance de **A**  **B** :

0 + 4 = 4

0 9tant la valeur du nud actuel (**A**), et 4 9tant la distance entre **A** et **B** dans le graphe.

Pour obtenir la distance de **A**  **C** :

0 + 2 = 2

##### **9tape #3 - Mettre  jour le tableau avec les distances connues**

Dans la dernire tape, nous avons obtenu 4 et 2 comme valeurs de **B** et **C** respectivement. Nous allons donc mettre  jour le tableau avec ces valeurs :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    4   |
| C | 2 |
| D |   |
| E |       |

##### **9tape #4 - Mettre  jour les tableaux**

 ce stade, la premire itration est termine. Nous allons dplacer le nud **A** vers le tableau des nuds visits :

Nuds visits = [A]  
Nuds non visits = [B,C,D,E]

Avant de passer  l'itration suivante, vous devez savoir ce qui suit :

* Une fois qu'un nud a t visit, il ne peut pas tre reli au nud actuel. Rfrez-vous  l'9tape #2 dans l'itration ci-dessus et  l'9tape #2 dans l'itration suivante.
* Un nud ne peut pas tre visit deux fois.
* Vous ne pouvez mettre  jour la distance la plus courte connue que si vous obtenez une valeur plus petite que la distance enregistre.

### Itration #2

##### **9tape #1 - Choisir un nud non visit**

Nous avons quatre nuds non visits  [B,C,D,E]. Alors, comment savoir quel nud choisir pour la prochaine itration ?

Eh bien, nous choisissons le nud avec la plus petite distance connue enregistre dans le tableau. Voici le tableau :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    4   |
| C | 2 |
| D |   |
| E |       |

Nous allons donc choisir le nud **C**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node2-2.png)

##### **9tape #2 - Trouver la distance depuis le nud actuel**

Pour trouver la distance du nud actuel au nud fixe, nous devons considrer les nuds relis au nud actuel.

Les nuds relis au nud actuel sont **A** et **B**.

Mais **A** a t visit dans l'itration prcdente, il ne sera donc pas reli au nud actuel. C'est--dire :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node2a-1.png)

D'aprs le diagramme ci-dessus,

* La couleur verte dsigne le nud actuel.
* La couleur bleue dsigne les nuds visits. Nous ne pouvons pas nous y relier ou les visiter  nouveau.
* La couleur rouge montre le lien des nuds non visits au nud actuel.

Pour trouver la distance de **C**  **B** :

2 + 1 = 3

2 ci-dessus est la distance enregistre pour le nud **C** tandis que 1 est la distance entre **C** et **B** dans le graphe.

##### **9tape #3 - Mettre  jour le tableau avec les distances connues**

Dans la dernire tape, nous avons obtenu la valeur de **B**  3. Dans la premire itration, elle 9tait de 4.

Nous allons mettre  jour la distance dans le tableau  3.

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |   |
| E |       |

Donc, **A** --> **B** = 4 (Premire itration).

**A** --> **C** --> **B** = 3 (Deuxime itration).

L'algorithme nous a aids  trouver le chemin le plus court vers **B** depuis **A**.

##### **9tape #4 - Mettre  jour les tableaux**

Nous avons termin avec le dernier nud visit. Ajoutons-le au tableau des nuds visits :

Nuds visits = [A,C]  
Nuds non visits = [B,D,E]

### Itration #3

##### **9tape #1 - Choisir un nud non visit**

Il nous reste trois nuds non visits  [B,D,E]. D'aprs le tableau, **B** a la plus petite distance connue.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node3-2.png)

Pour raffirmer ce qui se passe dans le diagramme ci-dessus :

* La couleur verte dsigne le nud actuel.
* La couleur bleue dsigne les nuds visits. Nous ne pouvons pas nous y relier ou les visiter  nouveau.
* La couleur rouge montre le lien des nuds non visits au nud actuel.

##### **9tape #2 - Trouver la distance depuis le nud actuel**

Les nuds relis au nud actuel sont **D** et **E**.

**B** (le nud actuel) a une valeur de 3. Par consquent,

Pour le nud **D**, 3 + 3 = 6.

Pour le nud **E**, 3 + 2 = 5.

##### **9tape #3 - Mettre  jour le tableau avec les distances connues**

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

##### **9tape #4 - Mettre  jour les tableaux**

Nuds visits = [A,C,B]  
Nuds non visits = [D,E]

### Itration #4

##### **9tape #1 - Choisir un nud non visit**

Comme pour les autres itrations, nous allons choisir le nud non visit avec la plus petite distance connue. C'est **E**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node4-1.png)

##### **9tape #2 - Trouver la distance depuis le nud actuel**

D'aprs notre tableau, **E** a une valeur de 5.

Pour **D** dans l'itration actuelle,

5 + 5 = 10.

La valeur obtenue pour **D** ici est 10, ce qui est suprieur  la valeur enregistre de 6 dans l'itration prcdente. Pour cette raison, nous ne mettrons pas  jour le tableau.

##### **9tape #3 - Mettre  jour le tableau avec les distances connues**

Notre tableau reste le meme :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

##### **9tape #4 - Mettre  jour les tableaux**

Nuds visits = [A,C,B,E]  
Nuds non visits = [D]

### Itration #5

##### **9tape #1 - Choisir un nud non visit**

Il nous reste actuellement un nud dans le tableau des non visits  **D**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node5-1.png)

##### **9tape #2 - Trouver la distance depuis le nud actuel**

L'algorithme est arriv  la dernire itration. Cela est dû au fait que tous les nuds relis au nud actuel ont dj t visits, nous ne pouvons donc pas nous y relier.

##### **9tape #3 - Mettre  jour le tableau avec les distances connues**

Notre tableau reste le meme :

| Nud   | Distance la plus courte depuis le nud fixe |
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

 ce stade, nous avons mis  jour le tableau avec la distance la plus courte du nud fixe vers tous les autres nuds du graphe.

##### **9tape #4 - Mettre  jour les tableaux**

Nuds visits = [A,C,B,E,D]  
Nuds non visits = []

Comme on peut le voir ci-dessus, il ne nous reste plus de nuds  visiter. En utilisant l'algorithme de Dijkstra, nous avons trouv la distance la plus courte du nud fixe aux autres nuds du graphe.

## Exemple de pseudocode de l'algorithme de Dijkstra

L'exemple de pseudocode dans cette section a t obtenu depuis [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). Le voici :

```txt
 1  function Dijkstra(Graphe, source):
 2      
 3      pour chaque sommet v dans Graphe.Sommets:
 4          dist[v]  INFINI
 5          prev[v]  NON_DEFINI
 6          ajouter v  Q
 7      dist[source]  0
 8      
 9      tant que Q n'est pas vide:
10          u  sommet dans Q avec dist[u] minimale
11          retirer u de Q
12          
13          pour chaque voisin v de u toujours dans Q:
14              alt  dist[u] + Graphe.Aretes(u, v)
15              si alt < dist[v]:
16                  dist[v]  alt
17                  prev[v]  u
18
19      retourner dist[], prev[]
```

## Applications de l'algorithme de Dijkstra

Voici quelques-unes des applications courantes de l'algorithme de Dijkstra :

* Dans les cartes pour obtenir la distance la plus courte entre des lieux. Un exemple est Google Maps.
* Dans les tlcommunications pour dterminer le taux de transmission.
* Dans la conception robotique pour dterminer le chemin le plus court pour les robots automatiss.

## Rsum

Dans cet article, nous avons parl de l'algorithme de Dijkstra. Il est utilis pour trouver la distance la plus courte d'un nud fixe vers tous les autres nuds d'un graphe.

Nous avons commen par donner un bref rsum de comment l'algorithme fonctionne.

Nous avons ensuite examin un exemple qui a expliqu plus en dtail l'algorithme de Dijkstra en tapes  l'aide de guides visuels.

Nous avons conclu avec un exemple de pseudocode et quelques-unes des applications de l'algorithme de Dijkstra.

Bon codage !