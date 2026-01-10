---
title: Un guide pour débutants sur les graphes — De Google Maps aux échiquiers
subtitle: ''
author: Tilda Udufo
co_authors: []
series: null
date: '2025-06-02T15:50:01.512Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-graphs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748879365710/23d7601e-cde0-489b-a843-97190e58e5c9.png
tags:
- name: Graph
  slug: graph
- name: Python
  slug: python
- name: data structures
  slug: data-structures
- name: DFS
  slug: dfs
- name: BFS
  slug: bfs
seo_title: Un guide pour débutants sur les graphes — De Google Maps aux échiquiers
seo_desc: Most of us use Google Maps without thinking twice. You open the app, check
  which route has the least traffic, and hit start. Then somewhere along the way –
  maybe you miss a turn (I do that often) – and Maps calmly recalculates your route,
  showing you...
---

La plupart d'entre nous utilisons Google Maps sans y réfléchir à deux fois. Vous ouvrez l'application, vérifiez quel itinéraire a le moins de trafic, et vous appuyez sur démarrer. Ensuite, quelque part en chemin — peut-être que vous ratez un tournant (je fais souvent cela) — et Maps recalcule calmement votre itinéraire, vous montrant un nouveau chemin qui vous mène toujours à votre destination.

Derrière ce reroutage fluide se cache un graphe — non pas un graphique, mais une structure de **nœuds** (lieux) et d'**arêtes** (routes) qui permet à Google Maps de calculer le chemin le plus court, le plus rapide ou le moins encombré du point A au point B.

Une fois que vous commencez à les remarquer, vous réaliserez que les graphes sont partout. Si vous avez déjà utilisé :

* **Google Maps** pour aller d'une ville à une autre,

* **LinkedIn** pour voir comment vous êtes connecté à quelqu'un,

* ou **Git** pour visualiser les branches et les fusions...

...vous avez interagi avec un graphe.

Les graphes sont partout, dans la façon dont nous planifions les itinéraires, recommandons des amis, gérons les dépendances de projets, et même prédisons les mouvements possibles d'un cavalier sur un échiquier. Mais pour les utiliser efficacement, nous devons d'abord comprendre comment ils sont structurés et pourquoi ils sont si utiles.

Dans cet article, vous apprendrez :

* Ce qu'est un graphe et comment il est utilisé dans les systèmes du monde réel

* Les différents types de graphes et comment ils sont représentés en code

* Comment parcourir les graphes en utilisant des algorithmes de recherche

* Et enfin, comment le mouvement d'un cavalier aux échecs peut être modélisé en utilisant des graphes, et résolu en utilisant des techniques de parcours

Commençons par décomposer ce dont les graphes sont faits et pourquoi ils apparaissent dans tant de choses que vous utilisez déjà.

## Table des matières

* [Qu'est-ce qu'un graphe ?](#heading-quest-ce-quun-graphe)

* [Types de graphes](#heading-types-de-graphes)

* [Comment les graphes sont représentés](#heading-comment-les-graphes-sont-representes)

* [Parcours de graphes](#heading-parcours-de-graphes)

* [Les périples du cavalier : Un problème de graphe du monde réel](#heading-les-periples-du-cavalier-un-probleme-de-graphe-du-monde-reel)

* [Conclusion](#heading-conclusion)

### **Prérequis**

Cet article est adapté aux débutants, et aucune connaissance préalable des graphes n'est requise. Pour suivre les exemples de code, il est utile d'avoir :

* Une certaine familiarité avec les structures de données comme les piles et les files d'attente.

* J'utilise Python pour les extraits de code, mais si vous avez travaillé avec un autre langage, vous devriez pouvoir suivre facilement.

## Qu'est-ce qu'un graphe ?

À sa base, un graphe est une collection de **nœuds** (également appelés sommets) et d'**arêtes** — des connexions qui relient ces nœuds ensemble.

Si cela semble simple, c'est parce que c'est le cas. La puissance des graphes n'est pas dans leur complexité, mais dans leur flexibilité. Vous pouvez les utiliser pour représenter presque tout : des personnes, des villes, des pages web, des tâches, des mouvements de jeu, et les relations entre eux.

Décomposons cela :

### Nœuds (Sommets)

Chaque nœud est un point dans le graphe. Il peut représenter :

* Un lieu (comme une ville sur une carte)

* Une personne (dans un réseau social)

* Une page (par exemple, sur le web)

* Une case (comme une case sur un échiquier)

### Arêtes

Une arête est une connexion entre deux nœuds. Elle pourrait représenter :

* Une route entre deux villes

* Une amitié entre deux utilisateurs

* Un hyperlien entre deux pages web

* Un mouvement de cavalier légal entre deux cases

Les arêtes peuvent avoir une direction (à sens unique ou à double sens), un poids (comme la distance ou le coût), ou être simples et non pondérées.

### Visualisateur de graphes

Voici un graphe simple :

![Graphe avec 7 nœuds circulaires étiquetés de 0 à 6. Des lignes relient diverses paires de nœuds, formant une structure en réseau. Chaque nœud est connecté à un ou plusieurs autres.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748363812251/59a945ea-eae0-4792-98bb-3f1d8477dde9.png align="center")

Dans cette image :

* Les cercles représentent les nœuds (également appelés sommets)

* Les lignes qui les relient sont des arêtes, qui montrent que deux nœuds sont liés ou connectés d'une certaine manière

Chaque nœud est connecté à un ou plusieurs autres nœuds, formant un réseau de relations.

## Types de graphes

Maintenant que nous avons vu à quoi ressemble un graphe, parlons des différentes façons dont les graphes peuvent se comporter.

Les graphes peuvent varier en **direction**, **poids** et **structure**. Comprendre ces types nous aide à choisir le bon modèle de graphe pour le problème que nous essayons de résoudre.

### Graphes orientés

Dans un graphe orienté (également connu sous le nom de **digraphe**), les connexions entre les nœuds se déplacent dans une direction spécifique. Pensez à une rue à sens unique — si vous pouvez conduire du point A au point B, cela ne signifie pas nécessairement que vous pouvez revenir par le même chemin.

Un bon exemple de cela est X (Twitter). Si vous suivez quelqu'un sur X, cela ne signifie pas automatiquement qu'il vous suit en retour. Votre "suivi" est une connexion à sens unique, une arête dirigée de vous vers lui.

Ce type de graphe est particulièrement utile dans les situations où les relations ne sont pas mutuelles. Sur Internet, les liens entre les pages web se comportent de la même manière. La page A peut lier à la page B, mais la page B peut ne pas lier en retour. De même, dans les systèmes de flux de travail ou les pipelines de tâches, chaque étape s'écoule dans la suivante dans un ordre spécifique, et vous ne revenez généralement pas en arrière — l'étape 1 mène à l'étape 2, et ainsi de suite.

![Un graphe orienté avec six nœuds bleus (0–5) et des arêtes les reliant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748365204873/4926ff56-af90-438d-8281-8423ffa1bfad.png align="center")

### Graphes non orientés

Un graphe non orienté représente des relations qui fonctionnent dans les deux sens. Si une connexion existe entre le nœud A et le nœud B, vous pouvez voyager dans les deux directions.

Un exemple courant est une amitié sur Facebook. Si vous êtes ami avec quelqu'un, la connexion est mutuelle par défaut. Il n'aurait pas de sens d'être "demi-amis".

Les graphes non orientés sont utiles lorsque la relation elle-même est mutuelle et symétrique, comme les appareils partagés sur un réseau ou les systèmes routiers où le trafic est autorisé dans les deux sens.

La différence clé ici est que les arêtes sont simplement des lignes, pas des flèches — elles n'impliquent pas de flux ou de hiérarchie, juste une connexion.

![Un graphe non orienté avec six nœuds rouges (0–5) et des arêtes les reliant de manière symétrique, montrant des relations bidirectionnelles sans flèches.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748365067259/af75d2bc-91ee-459a-8277-d0b53a039bd3.png align="center")

### Graphes pondérés

Un graphe pondéré est un graphe où chaque connexion (arête) porte des informations supplémentaires, généralement un nombre représentant la distance, le coût, le temps ou l'importance.

Considérez comment vous utilisez Google Maps pour aller d'un endroit à un autre. L'application ne cherche pas n'importe quel itinéraire, elle cherche celui qui prend le **moins de temps**, parcourt la **distance la plus courte**, ou utilise le **moins de carburant**. Tous ceux-ci sont des poids.

Dans un graphe comme celui-ci, deux villes peuvent être connectées, mais une route peut prendre 5 minutes tandis qu'une autre en prend 20, donc l'arête entre ces villes n'est pas seulement une ligne — c'est une ligne avec une valeur.

Cette structure nous permet de prendre des décisions plus intelligentes. Nous pouvons poser des questions comme :

* Quel est le moyen le moins cher d'atteindre une destination ?

* Quel itinéraire évite le plus de trafic ?

* Quel est l'itinéraire le plus rapide du nœud A au nœud Z ?

Si les graphes orientés et non orientés décrivent qui est connecté à qui, les graphes pondérés nous aident à comprendre à quel point ces connexions sont fortes, éloignées ou coûteuses.

![Un graphe non orienté pondéré avec neuf nœuds violets (0–8) et des arêtes étiquetées montrant des poids. Les valeurs des arêtes varient (par exemple, 3, 5, 10), modélisant un graphe pondéré.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748365667877/bfa51c1c-e17d-4db9-aaf9-5d25d1825af0.png align="center")

### Graphes non pondérés

Dans un graphe non pondéré, toutes les arêtes sont traitées de manière égale. Une connexion existe ou n'existe pas — il n'y a pas de valeur ou de coût supplémentaire attaché.

Pensez à un groupe d'amis où vous vous souciez seulement de savoir si deux personnes se connaissent. Vous n'essayez pas de mesurer à quel point elles sont proches ou à quelle fréquence elles parlent, vous voulez simplement cartographier la présence ou l'absence d'une relation.

Les graphes non pondérés sont utiles pour modéliser des systèmes où l'existence d'une connexion est plus importante que toute nuance de sa force. Ceux-ci sont parfaits pour représenter des relations de base, des états de jeu de société, ou des arbres de décision où chaque chemin est considéré comme également probable ou précieux.

En bref, les graphes non pondérés concernent le "oui/non", pas le "combien".

![Un graphe non pondéré avec des nœuds orange (0–8). Les nœuds sont connectés sans flèches, formant une disposition circulaire lâche.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748365816756/761186c7-befb-4dc9-8059-787aac271e05.png align="center")

### Graphes cycliques

Un graphe cyclique est un graphe où il est possible de revenir à l'endroit où vous avez commencé. Vous pouvez traverser une série de connexions et finir par revenir au même nœud.

Si vous avez déjà regardé une carte de ville ou utilisé un système de transport public avec des itinéraires circulaires, vous avez vu un cycle en action. Vous pouvez commencer à une station, prendre le train à travers plusieurs arrêts, et finalement revenir à l'endroit où vous avez commencé, sans jamais retracer vos étapes exactes.

Les graphes cycliques sont particulièrement utiles dans les simulations, les jeux ou les systèmes du monde réel où les boucles font partie de la conception, comme les circuits de contrôle ou les flux de travail répétés. Ils sont un choix naturel pour tout scénario où la répétition ou les chemins de retour comptent.

Mais ils peuvent aussi introduire de la complexité, surtout dans les algorithmes qui ne sont pas conçus pour gérer les cycles. Reconnaître si votre graphe contient des cycles est souvent une première étape importante dans le choix de la bonne méthode de parcours.

![Un graphe cyclique avec huit nœuds verts (0–7).](https://cdn.hashnode.com/res/hashnode/image/upload/v1748366079943/bf3b7675-cee8-442a-a680-e52e9ee85612.png align="center")

### Graphes acycliques

Un graphe acyclique est l'opposé d'un graphe cyclique — il n'y a pas de boucles. Une fois que vous commencez à vous déplacer dans le graphe, vous ne pouvez pas revenir à un nœud que vous avez déjà visité en suivant la direction des arêtes. Ils peuvent être des graphes orientés ou non orientés.

Pensez aux systèmes de gestion des tâches où certaines tâches dépendent d'autres. Vous ne pouvez pas compléter la tâche C jusqu'à ce que vous ayez terminé la tâche B, et vous ne pouvez pas commencer B jusqu'à ce que A soit fait. Il y a un ordre naturel, et pas de retour en arrière.

Les graphes acycliques sont courants dans :

* Les systèmes de planification

* Les organigrammes

* Les systèmes de progression de tutoriels (comme un chapitre débloquant le suivant)

![Un graphe acyclique avec huit nœuds rouges (0–7).](https://cdn.hashnode.com/res/hashnode/image/upload/v1748366703312/412cece1-85f2-4251-a422-776d56f115e7.png align="center")

### Graphes acycliques orientés

Un graphe acyclique orienté ou DAG est un type de graphe acyclique où chaque arête a une direction, et vous ne pouvez pas former de cycles. C'est comme une carte routière où toutes les routes pointent vers l'avant et ne bouclent jamais.

Cette structure est incroyablement courante en informatique, surtout lorsque vous devez suivre la progression, les dépendances ou l'historique.

Dans Git, par exemple, chaque commit pointe vers un ou plusieurs commits parents, formant un graphe orienté de changements. Mais comme les commits ne peuvent pas "revisiter" un état antérieur, la structure reste acyclique.

Dans les gestionnaires de paquets, une bibliothèque peut dépendre d'autres, mais vous ne pouvez pas avoir de boucle. Supposons que la bibliothèque A dépend de B, qui dépend de C, qui dépend à nouveau de A — cela briserait tout. Un DAG garantit que les dépendances avancent, pas en cercles.

![Un graphe acyclique orienté (DAG) avec huit nœuds bleus (0–7).](https://cdn.hashnode.com/res/hashnode/image/upload/v1748366537100/1110ebc4-33eb-4036-9ead-4a6178e02474.png align="center")

## Comment les graphes sont représentés

Jusqu'à présent, nous avons exploré les graphes en tant que concepts et visuels avec divers types et comportements. Mais lorsqu'il est temps de travailler avec des graphes en code, nous avons besoin d'un moyen de représenter ces connexions dans un format structuré.

Il existe deux façons courantes de représenter un graphe :

* **Liste d'adjacence**

* **Matrice d'adjacence**

Chacune a ses forces, et celle que vous utilisez dépend du type de graphe et des opérations que vous devez effectuer.

### Liste d'adjacence

Une liste d'adjacence stocke un graphe sous forme de collection de nœuds, où chaque nœud est mappé à une liste de ses voisins (nœuds auxquels il est connecté). Une liste d'adjacence est l'une des façons les plus intuitives de représenter un graphe. Mais la manière dont vous écrivez cette liste dépend du type de graphe avec lequel vous travaillez.

**Pour un graphe non orienté**, la connexion fonctionne dans les deux sens, donc chaque arête est écrite deux fois — une fois pour chaque nœud.

**Pour un graphe orienté**, chaque connexion ne circule que dans un sens, donc vous ne l'écrivez qu'une fois, dans la direction qu'elle indique.

![Un diagramme de graphe non orienté avec six nœuds étiquetés A à F, montré à côté de sa représentation en liste d'adjacence. Dans le graphe : les nœuds sont connectés par des lignes droites représentant des arêtes non orientées. La liste d'adjacence montre chaque nœud et ses voisins : A est connecté à E, F et C. B est connecté à E et F. C est connecté à A, D et E. D est connecté à C. E est connecté à A, B, C et F. F est connecté à A, B et E](https://cdn.hashnode.com/res/hashnode/image/upload/v1748375989397/6589e103-8589-4529-9ede-98d298567c39.png align="center")

**Avantages :**

* Économique en mémoire pour les graphes clairsemés (c'est-à-dire que tous les nœuds ne sont pas connectés)

* Facile à ajouter ou supprimer des nœuds et des arêtes

* Rapide pour obtenir les voisins d'un nœud — il suffit de lire sa liste

**Inconvénients :**

* Recherche d'arêtes plus lente : Pour vérifier si deux nœuds sont connectés, vous devez scanner une liste

* Peut être inefficace pour les graphes denses où la plupart des nœuds sont connectés à de nombreux autres

* Le tri des voisins ou l'accès à ceux-ci par index est moins pratique

### Matrice d'adjacence

Une matrice d'adjacence utilise un tableau 2D (ou une grille) pour représenter les connexions entre les nœuds. Chaque ligne et colonne correspond à un nœud, et la cellule à l'intersection vous indique s'il y a une connexion.

* Une valeur de `1` signifie qu'il y a une arête entre les deux nœuds.

* Une valeur de `0` signifie qu'une arête n'existe pas entre deux nœuds.

**Pour un graphe non orienté**, une arête entre `i` et `j` signifie que la connexion fonctionne dans les deux sens. Donc si `(i, j)` est `1`, `(j, i)` est aussi `1`. Cela rend la matrice symétrique, c'est-à-dire `(i, j) == (j, i)`.

**Pour un graphe orienté**, une arête du nœud `i` au nœud `j` est à la position `(i, j)`. Mais cela n'implique pas qu'il y a une arête de `j` à `i`. Donc en général, `(i, j) ≠ (j, i)`.

![Un diagramme montrant un graphe orienté et sa matrice d'adjacence correspondante. La matrice d'adjacence est un tableau 6x6 étiqueté avec les nœuds A à F. Une cellule avec une valeur de 1 indique une arête dirigée du nœud de la ligne au nœud de la colonne. Le nœud A a des arêtes sortantes vers C, E et F ; le nœud B pointe vers E et F ; le nœud C se connecte à D et E ; le nœud E se connecte à F. Les nœuds D et F n'ont pas d'arêtes sortantes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748378013560/6ecd11fc-bede-4dda-b01e-6f6d65f3bcb6.png align="center")

**Avantages :**

* Recherche instantanée d'arêtes entre deux nœuds en temps `O(1)`.

* Simple à implémenter et souvent utilisé dans les graphes denses à faible nombre de nœuds.

**Inconvénients :**

* Complexité spatiale élevée — même si le graphe a peu d'arêtes, la matrice occupe toujours un espace `O(V²)`.

* Inefficace pour les graphes clairsemés, où de nombreuses cellules sont inutilisées.

* Trouver les voisins nécessite de scanner une ligne entière, ce qui prend un temps `O(V)`.

## Parcours de graphes

Une fois que vous avez construit un graphe en utilisant des listes ou des matrices d'adjacence, la question suivante est : comment l'explorer ?

Le parcours de graphe est le processus de visite de chaque nœud (et de ses voisins) dans un graphe dans un ordre spécifique. C'est une technique fondamentale en informatique, utilisée dans tout, du crawl web aux suggestions d'amis sur les réseaux sociaux.

Le parcours est utilisé lorsque :

* Vous voulez rechercher une valeur ou un nœud spécifique.

* Vous voulez visiter tous les nœuds, par exemple, pour analyser la connectivité.

* Vous voulez résoudre des énigmes, comme des labyrinthes ou des problèmes de routage.

Il existe deux façons principales de parcourir un graphe : **Recherche en profondeur d'abord (DFS)** et **Recherche en largeur d'abord (BFS)**. Parcourons ce graphe en utilisant les deux méthodes :

![Un graphe non orienté avec des nœuds étiquetés (A–E)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748378930021/c8c46f1e-493d-4790-a48b-5059359bd3a4.png align="center")

### Recherche en largeur d'abord (BFS)

BFS commence par un nœud et explore tous ses voisins immédiats avant de passer aux voisins de ces voisins.

Il est couramment utilisé dans :

* Trouver le chemin le plus court (dans les graphes non pondérés)

* Parcours par niveau

* Simulations de diffusion de réseau

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        # le nœud n'a pas été visité
        if node not in visited:
            print(node)  # Visite le nœud
            visited.add(node)
            for neighbor in graph[node]:  # Regarde chaque voisin du nœud actuel
                if neighbor not in visited:     
                    queue.append(neighbor)  

# Graphe non orienté
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'E'],
    'E': ['D']
}

bfs(graph, 'A')
```

Voici la sortie du code ci-dessus :

```bash
A
B
C
D
E
```

#### Ce que fait ce code :

**Étape 1 : Choisir un point de départ**  
Choisissez le nœud où vous voulez commencer le parcours. Ajoutez-le à une file d'attente.

**Étape 2 : Visiter le nœud au début de la file d'attente**  
Prenez le premier nœud de la file d'attente (c'est votre nœud actuel) et marquez-le comme visité. Faites quelque chose avec lui, comme imprimer sa valeur.

**Étape 3 : Ajouter ses voisins à la file d'attente**  
Regardez tous les nœuds directement connectés au nœud actuel (ses voisins). Pour chaque voisin, s'il n'a pas encore été visité, ajoutez-le à la fin de la file d'attente.

**Étape 4 : Répéter jusqu'à ce que la file d'attente soit vide**  
Retournez à l'étape 2. Continuez à visiter le nœud au début de la file d'attente et mettez en file ses voisins non visités jusqu'à ce qu'il ne reste plus de nœuds dans la file d'attente.

### Recherche en profondeur d'abord (DFS)

DFS plonge profondément dans un chemin du graphe avant de revenir en arrière et d'explorer d'autres branches.

Il est utile pour :

* Détection de cycles

* Tri topologique

* Résolution d'énigmes comme les labyrinthes (où le chemin le plus court n'a pas d'importance)

```python
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)  # Visite le nœud
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


# Exemple de graphe (identique au précédent)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'E'],
    'E': ['D']
}

dfs(graph, 'A')
```

Voici la sortie du code ci-dessus :

```bash
A
C
D
E
B
```

#### Tout comme BFS, nous :

* Suivons les nœuds visités avec un ensemble

* Utilisons une boucle pour traiter chaque nœud

* Visitons les voisins un par un

**Mais voici la différence importante** : DFS utilise une **pile**, donc il va *profondément* dans un chemin jusqu'à ce qu'il ne puisse plus aller plus loin, puis il revient en arrière et explore le chemin suivant. Cela le rend idéal pour des tâches comme résoudre des labyrinthes ou explorer toutes les possibilités dans un arbre de décision.

### **Conclusion sur le parcours de graphes**

Comprendre comment parcourir un graphe est fondamental pour résoudre de nombreux problèmes du monde réel, de la cartographie des itinéraires à l'analyse des réseaux sociaux. Que vous utilisiez BFS pour trouver le chemin le plus court ou DFS pour explorer des relations profondes, choisir la bonne méthode de parcours dépend du problème que vous essayez de résoudre.

## Les périples du cavalier : Un problème de graphe du monde réel

Pour donner vie aux graphes, commençons par un exemple simple.

Imaginez que vous jouez aux échecs, et que votre cavalier est coincé dans un coin de l'échiquier. Supposons que vous voulez le déplacer vers une case spécifique pour défendre votre reine. Quel est le nombre minimum de mouvements qu'il faudra pour y arriver ?

C'est un problème classique de graphe.

Chaque case de l'échiquier peut être représentée comme un nœud. Si un cavalier peut légalement se déplacer d'une case à une autre, il y a une arête entre elles. Les règles de mouvement du cavalier — ces sauts en forme de L — définissent les arêtes du graphe. Donc, si vous y réfléchissez, vous naviguez dans un graphe, essayant de trouver le chemin le plus court d'un nœud (case de départ) à un autre (case cible).

Décomposons cela.

### Modélisation de l'échiquier comme un graphe

* L'échiquier est une grille de 8x8.

* Chaque case est un nœud, identifié par ses coordonnées `(x, y)` où `0 ≤ x < 8` et `0 ≤ y < 8`.

* Un cavalier a un maximum de **8 mouvements possibles** depuis n'importe quelle position (certains peuvent être hors limites).

* L'objectif est de construire un graphe où chaque nœud se connecte à tous les mouvements de cavalier valides depuis cette case.

![Un échiquier étiqueté avec des paires de coordonnées le long des bords inférieur et gauche. Un cavalier est positionné en (4, 0). L'axe x s'étend de (0, 0) à (0, 7) en bas, et l'axe y s'étend de (0, 0) à (7, 0) sur le côté gauche. Le plateau montre visuellement comment les cases sont représentées comme des paires de coordonnées dans une grille.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748383043887/83609e20-d41d-47d1-ba19-25887a96abcc.jpeg align="center")

### BFS ou DFS ? Choisir le bon outil

Il existe deux méthodes de parcours dont nous avons discuté précédemment, la recherche en largeur d'abord (BFS) et la recherche en profondeur d'abord (DFS). Alors, laquelle devons-nous utiliser pour résoudre le problème des périples du cavalier ?

Réfléchissons à ce qui se passerait si nous utilisions DFS.

DFS va aussi profondément que possible le long d'un chemin avant de revenir en arrière. Donc, si vous utilisez DFS pour déplacer le cavalier, il pourrait suivre une longue séquence sinueuse de mouvements valides qui mène finalement à la destination, disons en 7 mouvements.

Mais cela ne signifie pas que c'est le chemin le plus court. Le chemin optimal aurait pu atteindre la cible en seulement 3 ou 4 mouvements, mais DFS ne le trouverait pas à moins qu'il n'explore exactement ce chemin en premier.

Ce qui est pire, DFS ne garantit pas que vous trouverez le chemin le plus court à moins de rechercher exhaustivement chaque possibilité et de les comparer, ce qui est lent et inefficace pour ce type de problème.

Maintenant, voici pourquoi BFS est mieux adapté.

BFS explore toutes les positions que le cavalier peut atteindre en 1 mouvement, puis toutes les positions accessibles en 2 mouvements, puis 3 mouvements, et ainsi de suite. Dès qu'il trouve la case de destination, vous pouvez être sûr qu'il y est arrivé en utilisant le moins de pas possible, car il explore tous les chemins plus courts avant les plus longs.

En bref :

* DFS pourrait atteindre la destination éventuellement, mais pas efficacement, et pas nécessairement via le chemin le plus court.

* BFS garantit que le chemin qu'il retourne est le plus court en termes de nombre de mouvements.

C'est pourquoi, pour des problèmes comme celui-ci, où le nombre minimum d'étapes est l'objectif, BFS est l'approche à privilégier.

### Implémentation des périples du cavalier avec BFS

Pour modéliser le parcours du cavalier sur l'échiquier, nous utiliserons une classe appelée `Square`. Cette classe nous aidera à suivre :

* La position actuelle du cavalier sur l'échiquier (`x_coord`, `y_coord`)

* Une référence à sa case parente, afin que nous puissions reconstruire le chemin le plus court une fois la destination atteinte

* Suivre tous les mouvements suivants valides (ses `children`), qui représentent les cases vers lesquelles le cavalier peut légalement se déplacer depuis la position actuelle

Voici la classe initiale :

```python
from collections import deque

# Classe pour représenter une case sur l'échiquier
class Square:
    def __init__(self, x_coord, y_coord, parent=None):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.parent = parent
        self.children = []
```

Cette configuration est utile car nous construisons un arbre de chemins : chaque mouvement crée un nœud enfant, et nous pouvons retracer notre chemin jusqu'au point de départ en utilisant le `parent`.

#### Comment un cavalier se déplace-t-il ?

Un cavalier aux échecs se déplace en forme de "**L**", deux pas dans une direction et un pas perpendiculaire à celle-ci. Si le cavalier est au centre d'un échiquier de 8x8, il peut faire jusqu'à 8 mouvements légaux. Ces mouvements peuvent être visualisés comme des arêtes reliant une case (nœud) à d'autres.

![Un échiquier avec un cavalier placé sur e5. Des lignes en pointillés et des points rouges indiquent les huit mouvements en forme de L possibles que le cavalier peut faire depuis cette position. Chaque point rouge marque une case de destination valide selon le motif de mouvement du cavalier.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748425100670/fbccffb8-4cc0-46eb-b67d-b206bd528bd6.jpeg align="center")

Voici comment nous pouvons représenter et générer ces mouvements :

```python
from collections import deque

# Classe pour représenter une case sur l'échiquier
class Square:
    def __init__(self, x_coord, y_coord, parent=None):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.parent = parent
        self.children = []

    def generate_legal_moves(self):
        # Tous les 8 mouvements possibles du cavalier (en forme de L)
        row_moves = [-2, -1, 1, 2, 2, 1, -1, -2]
        col_moves = [1, 2, 2, 1, -1, -2, -2, -1]

        for dx, dy in zip(row_moves, col_moves):
            nx, ny = self.x_coord + dx, self.y_coord + dy

            # N'ajouter que les positions valides sur l'échiquier (0–7 pour un échiquier de 8x8)
            if 0 <= nx < 8 and 0 <= ny < 8:
                self.children.append(Square(nx, ny, self))
```

#### Trouver le chemin le plus court

Maintenant que nous avons la classe `Square` et les mouvements possibles du cavalier, nous devons implémenter BFS pour trouver le chemin le plus court d'une case de départ à une case de destination.

```python
# Fonction BFS pour trouver le chemin le plus court de la case de départ à la case de fin
def knight_travails(start_coords, end_coords):
    # Initialiser la file d'attente BFS avec la case de départ
    start_x, start_y = start_coords
    queue = deque([Square(start_x, start_y)])
    # Ensemble pour suivre les positions visitées et éviter les revisites
    visited = set()
    end_coords = tuple(end_coords)

    while queue:
        current = queue.popleft()
        coords = (current.x_coord, current.y_coord)

        # Si cette case est la cible, nous avons trouvé le chemin le plus court
        if coords == end_coords:
            return current

        # Passer si cette position a déjà été visitée
        if coords in visited:
            continue

        visited.add(coords)

        # Générer tous les mouvements de cavalier légaux depuis la case actuelle
        current.generate_legal_moves()
        # Ajouter les enfants à la file d'attente
        queue.extend(current.children)

def construct_path(start, end):
    # Exécuter BFS pour obtenir la case finale
    end_square = knight_travails(start, end)
    path = []

    # Retracer depuis la case de fin jusqu'au début en utilisant les liens parent
    while end_square:
        path.append((end_square.x_coord, end_square.y_coord))
        end_square = end_square.parent

    # Inverser le chemin pour le montrer du début à la fin
    return path[::-1]
```

Une fois que vous avez implémenté les fonctions ci-dessus, vous pouvez imprimer la sortie comme ceci :

```python
print(construct_path([3, 4], [0, 1]))
```

Cela retourne la séquence la plus courte de mouvements que le cavalier doit effectuer pour voyager de `[3, 4]` à `[0, 1]`. Exemple de sortie :

```python
[(3, 4), (2, 2), (0, 1)]
```

Chaque tuple représente une case sur l'échiquier que le cavalier visite. C'est le chemin le plus court que le cavalier peut prendre (de la case de départ à la case de fin) — et grâce au fonctionnement de BFS, nous savons avec certitude qu'aucun chemin plus court n'existe. Cette garantie d'optimalité est ce qui fait de la recherche en largeur d'abord un choix parfait ici.

## Conclusion

Des échiquiers aux cartes routières et aux itinéraires aériens, les graphes sont partout. Ils alimentent silencieusement une grande partie de la technologie sur laquelle nous comptons quotidiennement. Que vous réserviez un vol, naviguiez dans une ville ou obteniez une recommandation sur votre application préférée, les graphes sont souvent à l'œuvre en coulisses.

Ils vous permettent de modéliser et de résoudre des problèmes complexes du monde réel en connectant des entités et en explorant leurs relations. Donc, la prochaine fois que votre Google Maps vous reroute, souvenez-vous : les graphes sont le mécanisme derrière cette magie. Une fois que vous commencez à reconnaître les graphes, vous commencez à voir la structure cachée derrière les applications, les systèmes et même les jeux que vous utilisez tous les jours.