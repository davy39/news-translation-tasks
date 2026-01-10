---
title: Les meilleures structures de données à connaître pour votre prochain entretien
  de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T22:29:48.000Z'
originalURL: https://freecodecamp.org/news/the-top-data-structures-you-should-know-for-your-next-coding-interview-36af0831f5e3
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/1_s6hhrgR5_tXpO_j7uKaHMw-1.png
tags:
- name: Data Science
  slug: data-science
- name: interview
  slug: interview
- name: Java
  slug: java
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Les meilleures structures de données à connaître pour votre prochain entretien
  de codage
seo_desc: 'By Fahim ul Haq

  Niklaus Wirth, a Swiss computer scientist, wrote a book in 1976 titled Algorithms
  + Data Structures = Programs.

  40+ years later, that equation still holds true. That’s why software engineering
  candidates have to demonstrate their unde...'
---

Par Fahim ul Haq

Niklaus Wirth, un informaticien suisse, a écrit un livre en 1976 intitulé *Algorithmes + Structures de données = Programmes*.

Plus de 40 ans plus tard, cette équation est toujours valable. C'est pourquoi les candidats en génie logiciel doivent démontrer leur compréhension des structures de données ainsi que leurs applications.

Presque tous les problèmes nécessitent que le candidat démontre une compréhension approfondie des structures de données. Peu importe que vous veniez de sortir de l'université (ou d'un bootcamp de codage), ou que vous ayez des décennies d'expérience.

Parfois, les questions d'entretien mentionnent explicitement une structure de données, par exemple, "étant donné un arbre binaire". D'autres fois, c'est implicite, comme "nous voulons suivre le nombre de livres associés à chaque auteur".

Apprendre les structures de données est essentiel même si vous essayez simplement de vous améliorer dans votre travail actuel. Commençons par comprendre les bases.

### Qu'est-ce qu'une structure de données ?

Simplement, une structure de données est un conteneur qui stocke des données selon une disposition spécifique. Cette "disposition" permet à une structure de données d'être efficace pour certaines opérations et inefficace pour d'autres. Votre objectif est de comprendre les structures de données afin de pouvoir choisir celle qui est la plus optimale pour le problème à résoudre.

#### **Pourquoi avons-nous besoin des structures de données ?**

Comme les structures de données sont utilisées pour stocker des données de manière organisée, et puisque les données sont l'entité la plus cruciale en informatique, la véritable valeur des structures de données est claire.

Peu importe le problème que vous résolvez, d'une manière ou d'une autre, vous devez traiter des données — qu'il s'agisse du salaire d'un employé, des prix des actions, d'une liste de courses, ou même d'un simple annuaire téléphonique.

Selon différents scénarios, les données doivent être stockées dans un format spécifique. Nous avons un certain nombre de structures de données qui couvrent notre besoin de stocker des données dans différents formats.

### Structures de données couramment utilisées

Listons d'abord les structures de données les plus couramment utilisées, puis nous les couvrirons une par une :

1. Tableaux
2. Piles
3. Files d'attente
4. Listes chaînées
5. Arbres
6. Graphes
7. Tries (ce sont effectivement des arbres, mais il est bon de les mentionner séparément).
8. Tables de hachage

### Tableaux

Un tableau est la structure de données la plus simple et la plus largement utilisée. D'autres structures de données comme les piles et les files d'attente sont dérivées des tableaux.

Voici une image d'un simple tableau de taille 4, contenant les éléments (1, 2, 3 et 4).

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-81.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/06/B4CncYOv-dN76B45UXdVrfat45MvgQ9b8atv.png)

Chaque élément de données se voit attribuer une valeur numérique positive appelée **Index**_,_ qui correspond à la position de cet élément dans le tableau. La majorité des langages définissent l'index de départ du tableau comme 0.

Les deux types de tableaux sont les suivants :

* Tableaux unidimensionnels (comme montré ci-dessus)
* Tableaux multidimensionnels (tableaux dans des tableaux)

#### Opérations de base sur les tableaux

* Insertion — Insère un élément à un index donné
* Obtenir — Retourne l'élément à un index donné
* Suppression — Supprime un élément à un index donné
* Taille — Obtient le nombre total d'éléments dans un tableau

#### Questions d'entretien courantes sur les tableaux

* Trouver le deuxième élément minimum d'un tableau
* Premiers entiers non répétitifs dans un tableau
* Fusionner deux tableaux triés
* Réorganiser les valeurs positives et négatives dans un tableau

### **Piles**

Nous sommes tous familiers avec la fameuse option **Annuler**, présente dans presque toutes les applications. Vous êtes-vous déjà demandé comment elle fonctionne ? L'idée : vous stockez les états précédents de votre travail (qui sont limités à un nombre spécifique) dans la mémoire dans un ordre tel que le dernier apparaît en premier. Cela ne peut pas être fait simplement en utilisant des tableaux. C'est là que la Pile s'avère utile.

Un exemple réel de Pile pourrait être une pile de livres placés verticalement. Pour obtenir le livre qui se trouve quelque part au milieu, vous devrez retirer tous les livres placés au-dessus. C'est ainsi que fonctionne la méthode LIFO (Last In First Out).

Voici une image d'une pile contenant trois éléments de données (1, 2 et 3), où 3 est en haut et sera retiré en premier :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/BP-lD2OxkMbIQI2iZD-jxgIPlANlsMTqwnLP.png)

Opérations de base d'une pile :

* Push — Insère un élément en haut
* Pop — Retourne l'élément du haut après l'avoir retiré de la pile
* isEmpty — Retourne vrai si la pile est vide
* Top — Retourne l'élément du haut sans le retirer de la pile

#### Questions d'entretien courantes sur les piles

* Évaluer une expression postfixe en utilisant une pile
* Trier les valeurs dans une pile
* Vérifier les parenthèses équilibrées dans une expression

### **Files d'attente**

Similaire à la Pile, la File d'attente est une autre structure de données linéaire qui stocke les éléments de manière séquentielle. La seule différence significative entre la Pile et la File d'attente est qu'au lieu d'utiliser la méthode LIFO, la File d'attente implémente la méthode FIFO, qui signifie Premier entré, Premier sorti.

Un exemple parfait de File d'attente dans la vie réelle : une file de personnes attendant à un guichet de billets. Si une nouvelle personne arrive, elle rejoindra la file à la fin, pas au début — et la personne se tenant à l'avant sera la première à obtenir le billet et donc à quitter la file.

Voici une image d'une File d'attente contenant quatre éléments de données (1, 2, 3 et 4), où 1 est en haut et sera retiré en premier :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/C2riLJTPBVpSI-3o5Cx9IrQ16LZi1kLrqYXo.png)

#### Opérations de base d'une File d'attente

* Enqueue() — Insère un élément à la fin de la file d'attente
* Dequeue() — Retire un élément du début de la file d'attente
* isEmpty() — Retourne vrai si la file d'attente est vide
* Top() — Retourne le premier élément de la file d'attente

#### Questions d'entretien courantes sur les Files d'attente

* Implémenter une pile en utilisant une file d'attente
* Inverser les k premiers éléments d'une file d'attente
* Générer des nombres binaires de 1 à n en utilisant une file d'attente

### **Liste chaînée**

Une liste chaînée est une autre importante structure de données linéaire qui peut sembler similaire aux tableaux au premier abord mais diffère dans l'allocation mémoire, la structure interne et la manière dont les opérations de base d'insertion et de suppression sont effectuées.

Une liste chaînée est comme une chaîne de nœuds, où chaque nœud contient des informations comme des données et un pointeur vers le nœud suivant dans la chaîne. Il y a un pointeur de tête, qui pointe vers le premier élément de la liste chaînée, et si la liste est vide, il pointe simplement vers null ou rien.

Les listes chaînées sont utilisées pour implémenter des systèmes de fichiers, des tables de hachage et des listes d'adjacence.

Voici une représentation visuelle de la structure interne d'une liste chaînée :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/ezrkbpSyblh3famnGsgIHiRvHV9CKODu0tPw.png)

Les types de listes chaînées sont les suivants :

* Liste chaînée simple (Unidirectionnelle)
* Liste chaînée double (Bidirectionnelle)

#### _Opérations de base d'une Liste chaînée :_

* _InsertAtEnd_ — Insère un élément donné à la fin de la liste chaînée
* _InsertAtHead_ — Insère un élément donné au début/tête de la liste chaînée
* _Delete_ — Supprime un élément donné de la liste chaînée
* _DeleteAtHead_ — Supprime le premier élément de la liste chaînée
* _Search_ — Retourne l'élément donné d'une liste chaînée
* _isEmpty_ — Retourne vrai si la liste chaînée est vide

#### Questions d'entretien courantes sur les Listes chaînées

* Inverser une liste chaînée
* Détecter une boucle dans une liste chaînée
* Retourner le Nème nœud à partir de la fin dans une liste chaînée
* Supprimer les doublons d'une liste chaînée

### **Graphes**

Un graphe est un ensemble de nœuds qui sont connectés les uns aux autres sous forme de réseau. Les nœuds sont également appelés sommets. Une **paire(x,y)** est appelée une **arête**_,_ qui indique que le sommet **x** est connecté au sommet **y**. Une arête peut contenir un poids/coût, montrant combien il en coûte pour traverser du sommet x au sommet y_._

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0MsvzasAr6vS6bnvozjRAa5iBnEDKn9Cty0D.png)

Types de Graphes :

* Graphe non orienté
* Graphe orienté

Dans un langage de programmation, les graphes peuvent être représentés sous deux formes :

* Matrice d'adjacence
* Liste d'adjacence

Algorithmes de parcours de graphe courants :

* Recherche en largeur d'abord
* Recherche en profondeur d'abord

#### Questions d'entretien courantes sur les Graphes

* Implémenter la Recherche en largeur et en profondeur d'abord
* Vérifier si un graphe est un arbre ou non
* Compter le nombre d'arêtes dans un graphe
* Trouver le chemin le plus court entre deux sommets

### **Arbres**

Un arbre est une structure de données hiérarchique composée de sommets (nœuds) et d'arêtes qui les relient. Les arbres sont similaires aux graphes, mais le point clé qui différencie un arbre d'un graphe est qu'un cycle ne peut pas exister dans un arbre.

Les arbres sont largement utilisés en Intelligence Artificielle et dans des algorithmes complexes pour fournir un mécanisme de stockage efficace pour la résolution de problèmes.

Voici une image d'un arbre simple, et les terminologies de base utilisées dans la structure de données arborescente :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/VPUnmQO8rMoLGMqMe24EnoJ3uS72JZdMt48w.png)

Les types d'arbres sont les suivants :

* Arbre N-aire
* Arbre équilibré
* Arbre binaire
* Arbre de recherche binaire
* Arbre AVL
* Arbre Rouge-Noir
* Arbre 2-3

Parmi ceux-ci, l'Arbre binaire et l'Arbre de recherche binaire sont les arbres les plus couramment utilisés.

#### Questions d'entretien courantes sur les Arbres

* Trouver la hauteur d'un arbre binaire
* Trouver la k-ième valeur maximale dans un arbre de recherche binaire
* Trouver les nœuds à une distance "k" de la racine
* Trouver les ancêtres d'un nœud donné dans un arbre binaire

### Trie

Trie, également connu sous le nom d'Arbres de préfixes, est une structure de données de type arbre qui s'avère assez efficace pour résoudre les problèmes liés aux chaînes de caractères. Il offre une récupération rapide et est principalement utilisé pour rechercher des mots dans un dictionnaire, fournir des suggestions automatiques dans un moteur de recherche, et même pour le routage IP.

Voici une illustration de la manière dont trois mots top, thus et their sont stockés dans un Trie :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/lSNi21Wr4P6eMKDwLMQ5rijHhA-lBlovlc40-1.png)

Les mots sont stockés de haut en bas, où les nœuds de couleur verte p, s et r indiquent la fin de top, thus et their respectivement.

Questions d'entretien courantes sur les Tries :

* Compter le nombre total de mots dans un Trie
* Imprimer tous les mots stockés dans un Trie
* Trier les éléments d'un tableau en utilisant un Trie
* Former des mots à partir d'un dictionnaire en utilisant un Trie
* Construire un dictionnaire T9

### **Table de hachage**

Le hachage est un processus utilisé pour identifier de manière unique des objets et stocker chaque objet à un index unique pré-calculé appelé sa clé. Ainsi, l'objet est stocké sous la forme d'une paire clé-valeur, et la collection de tels éléments est appelée un dictionnaire. Chaque objet peut être recherché en utilisant cette clé. Il existe différentes structures de données basées sur le hachage, mais la structure de données la plus couramment utilisée est la **table de hachage**.

Les tables de hachage sont généralement implémentées en utilisant des tableaux.

La performance de la structure de données de hachage dépend de ces trois facteurs :

* Fonction de hachage
* Taille de la table de hachage
* Méthode de gestion des collisions

Voici une illustration de la manière dont le hachage est mappé dans un tableau. L'index de ce tableau est calculé à travers une fonction de hachage.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zV3x2Pxt0JFt7UjokTKNx24HFmM3t-6phDV2.png)

#### Questions d'entretien courantes sur le hachage

* Trouver les paires symétriques dans un tableau
* Tracer le chemin complet d'un voyage
* Vérifier si un tableau est un sous-ensemble d'un autre tableau
* Vérifier si les tableaux donnés sont disjoints

Les huit structures de données ci-dessus sont celles que vous devez absolument connaître avant de vous présenter à un entretien de codage.

*Si vous cherchez des ressources sur les structures de données pour les entretiens de codage, consultez les cours interactifs et basés sur des défis : [Structures de données pour les entretiens de codage](https://www.educative.io/d/data_structures) ([Python](https://www.educative.io/collection/5642554087309312/5634727314718720), [Java](https://www.educative.io/collection/5642554087309312/5724822843686912), ou [JavaScript](https://www.educative.io/collection/5642554087309312/5663204961157120)).*

*Pour des questions plus avancées, consultez [Coderust 3.0 : Préparation plus rapide aux entretiens de codage avec des défis interactifs et des visualisations](https://www.educative.io/collection/5642554087309312/5679846214598656).*

Si vous vous préparez pour des entretiens en génie logiciel, voici un [guide complet pour se préparer aux entretiens de codage](https://medium.com/educative/3-month-coding-interview-bootcamp-904422926ce8).

Bonne chance et bon apprentissage ! :)