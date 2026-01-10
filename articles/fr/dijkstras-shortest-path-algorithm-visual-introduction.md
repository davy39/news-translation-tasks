---
title: Algorithme du Plus Court Chemin de Dijkstra - Une Introduction Détaillée et
  Visuelle
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-09-28T15:07:55.000Z'
originalURL: https://freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Algorithm-Image-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Algorithme du Plus Court Chemin de Dijkstra - Une Introduction Détaillée
  et Visuelle
seo_desc: "Welcome! If you've always wanted to learn and understand Dijkstra's algorithm,\
  \ then this article is for you. You will see how it works behind the scenes with\
  \ a step-by-step graphical explanation. \nYou will learn:\n\nBasic Graph Concepts\
  \ (a quick review..."
---

**Bienvenue !** Si vous avez toujours voulu apprendre et comprendre l'algorithme de Dijkstra, alors cet article est fait pour vous. Vous verrez comment il fonctionne en coulisses avec une explication graphique étape par étape. 

**Vous apprendrez :**

* Les concepts de base des graphes (un rapide rappel).
* À quoi sert l'algorithme de Dijkstra.
* Comment il fonctionne en coulisses avec un exemple étape par étape.

**Commençons. ✨** 

## 📌 Introduction aux Graphes

Commençons par une brève introduction aux graphes. 

### Concepts de Base

Les graphes sont des structures de données utilisées pour représenter les "connexions" entre des paires d'éléments. 

* Ces éléments sont appelés **nœuds**. Ils représentent des objets, des personnes ou des entités de la vie réelle. 
* Les connexions entre les nœuds sont appelées **arêtes**.

Voici une représentation graphique d'un graphe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-123.png)

Les **nœuds** sont représentés par des cercles colorés et les **arêtes** par des lignes qui relient ces cercles. 

**💡 Astuce :** Deux nœuds sont connectés s'il existe une arête entre eux. 

### Applications

Les graphes sont directement applicables à des scénarios réels. Par exemple, nous pourrions utiliser des graphes pour modéliser un réseau de transport où les nœuds représenteraient des installations qui envoient ou reçoivent des produits et les arêtes représenteraient des routes ou des chemins qui les relient (voir ci-dessous). 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-121.png)
_Réseau représenté avec un graphe_

### Types de Graphes

Les graphes peuvent être :

* **Non orientés :** si pour chaque paire de nœuds connectés, vous pouvez aller d'un nœud à l'autre dans les deux directions.
* **Orientés :** si pour chaque paire de nœuds connectés, vous ne pouvez aller que d'un nœud à un autre dans une direction spécifique. Nous utilisons des flèches au lieu de simples lignes pour représenter les arêtes orientées.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-124.png)

**💡 Astuce :** dans cet article, nous travaillerons avec des graphes **non orientés**. 

### Graphes Pondérés

Un **graphe pondéré** est un graphe dont les arêtes ont un "poids" ou un "coût". Le poids d'une arête peut représenter une distance, un temps, ou toute autre chose qui modélise la "connexion" entre la paire de nœuds qu'elle relie.

Par exemple, dans le graphe pondéré ci-dessous, vous pouvez voir un nombre bleu à côté de chaque arête. Ce nombre est utilisé pour représenter le poids de l'arête correspondante.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-126.png)



**💡 Astuce :** Ces poids sont essentiels pour l'algorithme de Dijkstra. Vous verrez pourquoi dans un instant.

## 📌 Introduction à l'Algorithme de Dijkstra

Maintenant que vous connaissez les concepts de base des graphes, commençons à plonger dans cet algorithme incroyable. 

* Objectif et Cas d'Utilisation
* Histoire
* Bases de l'Algorithme
* Exigences

### Objectif et Cas d'Utilisation

Avec l'algorithme de Dijkstra, vous pouvez trouver le plus court chemin entre des nœuds dans un graphe. En particulier, vous pouvez **trouver le plus court chemin d'un nœud (appelé "nœud source") à tous les autres nœuds du graphe**, produisant ainsi un arbre de plus courts chemins. 

Cet algorithme est utilisé dans les dispositifs GPS pour trouver le plus court chemin entre l'emplacement actuel et la destination. Il a de nombreuses applications dans l'industrie, notamment dans les domaines qui nécessitent la modélisation de réseaux.

### Histoire

Cet algorithme a été créé et publié par [Dr. Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra), un brillant informaticien et ingénieur logiciel néerlandais. 

En 1959, il a publié un article de 3 pages intitulé "A note on two problems in connexion with graphs" où il expliquait son nouvel algorithme.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-112.png)
_[ETH Zurich](https://commons.wikimedia.org/wiki/File:Edsger_Dijkstra_1994.jpg">Dr. Edsger Dijkstra</a> à <a href="https://en.wikipedia.org/wiki/ETH_Zurich) en 1994 (image par Andreas F. Borchert)_

Lors d'une interview en 2001, le Dr. Dijkstra a révélé comment et pourquoi il avait conçu l'algorithme :

> Quel est le chemin le plus court pour voyager de Rotterdam à Groningen ? C'est l'algorithme du plus court chemin, que j'ai conçu en environ 20 minutes. Un matin, je faisais des courses à Amsterdam avec ma jeune fiancée, et fatigués, nous nous sommes assis sur la terrasse d'un café pour boire une tasse de café et je réfléchissais simplement à savoir si je pouvais faire cela, et j'ai alors conçu l'algorithme du plus court chemin. Comme je l'ai dit, c'était une invention de 20 minutes. En fait, il a été publié en 1959, trois ans plus tard. La publication est toujours assez belle. L'une des raisons pour lesquelles elle est si belle est que je l'ai conçue sans crayon ni papier. Sans crayon ni papier, vous êtes presque forcé d'éviter toutes les complexités évitables. Finalement, cet algorithme est devenu, à ma grande surprise, l'une des pierres angulaires de ma renommée. — Comme cité dans l'article [Edsger W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) de [An interview with Edsger W. Dijkstra](https://dl.acm.org/doi/pdf/10.1145/1787234.1787249).

✨ **Incroyable, n'est-ce pas ?** En seulement 20 minutes, le Dr. Dijkstra a conçu l'un des algorithmes les plus célèbres de l'histoire de l'informatique. 

### Bases de l'Algorithme de Dijkstra

* L'algorithme de Dijkstra commence essentiellement au nœud que vous choisissez (le nœud source) et analyse le graphe pour trouver le plus court chemin entre ce nœud et tous les autres nœuds du graphe. 
* L'algorithme garde une trace de la distance actuellement connue la plus courte de chaque nœud au nœud source et met à jour ces valeurs s'il trouve un chemin plus court.
* Une fois que l'algorithme a trouvé le plus court chemin entre le nœud source et un autre nœud, ce nœud est marqué comme "visité" et ajouté au chemin. 
* Le processus continue jusqu'à ce que tous les nœuds du graphe aient été ajoutés au chemin. De cette manière, nous avons un chemin qui relie le nœud source à tous les autres nœuds en suivant le chemin le plus court possible pour atteindre chaque nœud.

### Exigences

L'algorithme de Dijkstra ne peut fonctionner qu'avec des graphes dont les poids sont **positifs**. Cela est dû au fait que, pendant le processus, les poids des arêtes doivent être additionnés pour trouver le plus court chemin. 

S'il y a un poids négatif dans le graphe, alors l'algorithme ne fonctionnera pas correctement. Une fois qu'un nœud a été marqué comme "visité", le chemin actuel vers ce nœud est marqué comme le plus court chemin pour atteindre ce nœud. Et les poids négatifs peuvent altérer cela si le poids total peut être décrémenté après que cette étape a eu lieu.

## 📌 Exemple de l'Algorithme de Dijkstra

Maintenant que vous en savez plus sur cet algorithme, voyons comment il fonctionne en coulisses avec un exemple étape par étape.

Nous avons ce graphe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-76.png)

L'algorithme générera le plus court chemin du nœud `0` à tous les autres nœuds du graphe. 

**💡 Astuce :** Pour ce graphe, nous supposerons que le poids des arêtes représente la distance entre deux nœuds. 

Nous aurons le plus court chemin du nœud `0` au nœud `1`, du nœud `0` au nœud `2`, du nœud `0` au nœud `3`, et ainsi de suite pour chaque nœud du graphe. 

Initialement, nous avons cette liste de distances (voir la liste ci-dessous) :

* La distance du nœud source à lui-même est `0`. Pour cet exemple, le nœud source sera le nœud `0`, mais il peut être n'importe quel nœud que vous choisissez.
* La distance du nœud source à tous les autres nœuds n'a pas encore été déterminée, donc nous utilisons le symbole de l'infini pour représenter cela initialement.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-77.png)

Nous avons également cette liste (voir ci-dessous) pour garder une trace des nœuds qui n'ont pas encore été visités (nœuds qui n'ont pas été inclus dans le chemin) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-78.png)

**💡 Astuce :** N'oubliez pas que l'algorithme est terminé une fois que tous les nœuds ont été ajoutés au chemin.

Puisque nous choisissons de commencer au nœud `0`, nous pouvons marquer ce nœud comme visité. De manière équivalente, nous le rayons de la liste des nœuds non visités et ajoutons une bordure rouge au nœud correspondant dans le diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-87.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-83.png)

Maintenant, nous devons commencer à vérifier la distance du nœud `0` à ses nœuds adjacents. Comme vous pouvez le voir, ce sont les nœuds `1` et `2` (voir les arêtes rouges) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-89.png)

**💡 Astuce :** Cela ne signifie pas que nous ajoutons immédiatement les deux nœuds adjacents au plus court chemin. Avant d'ajouter un nœud à ce chemin, nous devons vérifier si nous avons trouvé le plus court chemin pour l'atteindre. Nous faisons simplement un processus d'examen initial pour voir les options disponibles.

Nous devons mettre à jour les distances du nœud `0` au nœud `1` et au nœud `2` avec les poids des arêtes qui les relient au nœud `0` (le nœud source). Ces poids sont respectivement 2 et 6 :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-90.png)

Après avoir mis à jour les distances des nœuds adjacents, nous devons :

* Sélectionner le nœud qui est le plus proche du nœud source en fonction des distances actuellement connues.
* Le marquer comme visité.
* L'ajouter au chemin. 

Si nous vérifions la liste des distances, nous pouvons voir que le nœud `1` a la distance la plus courte au nœud source (une distance de 2), donc nous l'ajoutons au chemin. 

Dans le diagramme, nous pouvons représenter cela avec une arête rouge :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-94.png)

Nous le marquons avec un carré rouge dans la liste pour représenter qu'il a été "visité" et que nous avons trouvé le plus court chemin vers ce nœud :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-92.png)

Nous le rayons de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-93.png)

Maintenant, nous devons analyser les nouveaux nœuds adjacents pour trouver le plus court chemin pour les atteindre. Nous n'analyserons que les nœuds qui sont adjacents aux nœuds qui font déjà partie du plus court chemin (le chemin marqué avec des arêtes rouges).

Le nœud `3` et le nœud `2` sont tous deux adjacents à des nœuds qui sont déjà dans le chemin car ils sont directement connectés au nœud `1` et au nœud `0`, respectivement, comme vous pouvez le voir ci-dessous. Ce sont les nœuds que nous analyserons à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-94.png)

Puisque nous avons déjà la distance du nœud source au nœud `2` notée dans notre liste, nous n'avons pas besoin de mettre à jour la distance cette fois. Nous devons seulement mettre à jour la distance du nœud source au nouveau nœud adjacent (nœud `3`) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-98.png)

Cette distance est **7**. Voyons pourquoi.

Pour trouver la distance du nœud source à un autre nœud (dans ce cas, le nœud `3`), nous additionnons les poids de toutes les arêtes qui forment le plus court chemin pour atteindre ce nœud :

* **Pour le nœud `3` :** la distance totale est **7** car nous additionnons les poids des arêtes qui forment le chemin `0 -> 1 -> 3` (2 pour l'arête `0 -> 1` et 5 pour l'arête `1 -> 3`).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-94.png)

Maintenant que nous avons la distance aux nœuds adjacents, nous devons choisir quel nœud sera ajouté au chemin. Nous devons sélectionner le nœud **non visité** avec la distance la plus courte (actuellement connue) au nœud source. 

D'après la liste des distances, nous pouvons immédiatement détecter que c'est le nœud `2` avec une distance de **6** :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-98.png)

Nous l'ajoutons au chemin graphiquement avec une bordure rouge autour du nœud et une arête rouge :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-96.png)

Nous le marquons également comme visité en ajoutant un petit carré rouge dans la liste des distances et en le rayant de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-99.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-100.png)

Maintenant, nous devons répéter le processus pour trouver le plus court chemin du nœud source au nouveau nœud adjacent, qui est le nœud `3`. 

Vous pouvez voir que nous avons deux chemins possibles `0 -> 1 -> 3` ou `0 -> 2 -> 3`. Voyons comment nous pouvons décider lequel est le plus court chemin. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-96.png)

Le nœud `3` a déjà une distance dans la liste qui a été enregistrée précédemment (**7**, voir la liste ci-dessous). Cette distance était le résultat d'une étape précédente, où nous avons additionné les poids 5 et 2 des deux arêtes que nous devions traverser pour suivre le chemin `0 -> 1 -> 3`.

Mais maintenant nous avons une autre alternative. Si nous choisissons de suivre le chemin `0 -> 2 -> 3`, nous devrions suivre deux arêtes `0 -> 2` et `2 -> 3` avec des poids **6** et **8**, respectivement, ce qui représente une distance totale de **14**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-101.png)

Clairement, la première (existante) distance est plus courte (7 vs. 14), donc nous choisirons de garder le chemin original `0 -> 1 -> 3`. **Nous ne mettons à jour la distance que si le nouveau chemin est plus court.**

Par conséquent, nous ajoutons ce nœud au chemin en utilisant la première alternative : `0 -> 1 -> 3`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-104.png)

Nous marquons ce nœud comme visité et le rayons de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-103.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-106.png)

Maintenant, nous répétons le processus à nouveau. 

Nous devons vérifier les nouveaux nœuds adjacents que nous n'avons pas encore visités. Cette fois, ces nœuds sont le nœud `4` et le nœud `5` puisqu'ils sont adjacents au nœud `3`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-104.png)

Nous mettons à jour les distances de ces nœuds au nœud source, en essayant toujours de trouver un chemin plus court, si possible :

* **Pour le nœud `4` :** la distance est **17** depuis le chemin `0 -> 1 -> 3 -> 4`.
* **Pour le nœud `5` :** la distance est **22** depuis le chemin `0 -> 1 -> 3 -> 5`.

**💡 Astuce :** Remarquez que nous ne pouvons considérer que l'extension du plus court chemin (marqué en rouge). Nous ne pouvons pas considérer les chemins qui nous mèneraient à travers des arêtes qui n'ont pas été ajoutées au plus court chemin (par exemple, nous ne pouvons pas former un chemin qui passe par l'arête `2 -> 3`). 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-105.png)

Nous devons choisir quel nœud non visité sera marqué comme visité maintenant. Dans ce cas, c'est le nœud `4` car il a la distance la plus courte dans la liste des distances. Nous l'ajoutons graphiquement dans le diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-108.png)

Nous le marquons également comme "visité" en ajoutant un petit carré rouge dans la liste :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-107.png)

Et nous le rayons de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-109.png)

Et nous répétons le processus à nouveau. Nous vérifions les nœuds adjacents : le nœud `5` et le nœud `6`. Nous devons analyser chaque chemin possible que nous pouvons suivre pour les atteindre depuis les nœuds qui ont déjà été marqués comme visités et ajoutés au chemin.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-108.png)

**Pour le nœud `5` :**

* La première option est de suivre le chemin `0 -> 1 -> 3 -> 5`, qui a une distance de **22** depuis le nœud source (2 + 5 + 15). Cette distance a déjà été enregistrée dans la liste des distances lors d'une étape précédente.
* La deuxième option serait de suivre le chemin `0 -> 1 -> 3 -> 4 -> 5`, qui a une distance de **23** depuis le nœud source (2 + 5 + 10 + 6). 

Clairement, le premier chemin est plus court, donc nous le choisissons pour le nœud `5`.

**Pour le nœud `6` :**

* Le chemin disponible est `0 -> 1 -> 3 -> 4 -> 6`, qui a une distance de **19** depuis le nœud source (2 + 5 + 10 + 2).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-110.png)

Nous marquons le nœud avec la distance la plus courte (actuellement connue) comme visité. Dans ce cas, le nœud `6`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-140.png)

Et nous le rayons de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-111.png)

Maintenant, nous avons ce chemin (marqué en rouge) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-112.png)

Un seul nœud n'a pas encore été visité, le nœud `5`. Voyons comment nous pouvons l'inclure dans le chemin.

Il y a trois chemins différents que nous pouvons prendre pour atteindre le nœud `5` depuis les nœuds qui ont été ajoutés au chemin :

* **Option 1 :** `0 -> 1 -> 3 -> 5` avec une distance de **22** (2 + 5 + 15).
* **Option 2 :** `0 -> 1 -> 3 -> 4 -> 5` avec une distance de **23** (2 + 5 + 10 + 6).
* **Option 3 :** `0 -> 1 -> 3 -> 4 -> 6 -> 5` avec une distance de **25** (2 + 5 + 10 + 2 + 6).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-113.png)

Nous sélectionnons le plus court chemin : `0 -> 1 -> 3 -> 5` avec une distance de **22**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-115.png)

Nous marquons le nœud comme visité et le rayons de la liste des nœuds non visités :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-114.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-116.png)

**Et voilà !** Nous avons le résultat final avec le plus court chemin du nœud `0` à chaque nœud du graphe.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-115.png)

Dans le diagramme, les lignes rouges marquent les arêtes qui appartiennent au plus court chemin. Vous devez suivre ces arêtes pour suivre le plus court chemin pour atteindre un nœud donné dans le graphe en partant du nœud `0`. 

Par exemple, si vous voulez atteindre le nœud `6` en partant du nœud `0`, vous devez simplement suivre les arêtes rouges et vous suivrez automatiquement le plus court chemin `0 -> 1 -> 3 -> 4 -> 6`.

## 📌 En Résumé

* Les graphes sont utilisés pour modéliser les connexions entre des objets, des personnes ou des entités. Ils ont deux éléments principaux : les nœuds et les arêtes. Les nœuds représentent des objets et les arêtes représentent les connexions entre ces objets. 
* L'algorithme de Dijkstra trouve le plus court chemin entre un nœud donné (qui est appelé le "nœud source") et tous les autres nœuds d'un graphe. 
* Cet algorithme utilise les poids des arêtes pour trouver le chemin qui minimise la distance totale (poids) entre le nœud source et tous les autres nœuds. 

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous savez comment l'algorithme de Dijkstra fonctionne en coulisses. Suivez-moi sur Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN) et [découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/).