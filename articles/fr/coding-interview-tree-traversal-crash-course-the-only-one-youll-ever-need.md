---
title: Cours accéléré sur le parcours d'arbres pour les entretiens de codage – Le
  seul dont vous aurez jamais besoin
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-08-16T23:49:03.000Z'
originalURL: https://freecodecamp.org/news/coding-interview-tree-traversal-crash-course-the-only-one-youll-ever-need
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/tree-thumb.png
tags:
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Trees
  slug: trees
seo_title: Cours accéléré sur le parcours d'arbres pour les entretiens de codage –
  Le seul dont vous aurez jamais besoin
seo_desc: 'Are you preparing for coding interviews? I designed a crash course series
  to help you out.

  I''m Lynn, a software engineer and a recent graduate from the University of Chicago.
  This is the second course in my Coding Interview Crash Course Series. Feel ...'
---

Vous préparez-vous pour des entretiens de codage ? J'ai conçu une série de cours accélérés pour vous aider.

Je m'appelle Lynn, je suis ingénieure logicielle et récente diplômée de l'Université de Chicago. Ceci est le deuxième cours de ma série de cours accélérés sur les entretiens de codage. N'hésitez pas à consulter [ma chaîne YouTube, Lynn's DevLab](https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw), pour rester informé de cette série.

Ce cours accéléré porte sur le parcours d'arbres. Si vous voulez plonger directement dans le sujet, [vous pouvez trouver le cours ici](https://youtu.be/uaeCfsCcYWo) (et lié en bas de cet article). Si vous voulez plus d'informations, continuez votre lecture. 😊

## À qui s'adresse le cours et quels sont les algorithmes de parcours d'arbres ? 🌳

Vous tirerez le meilleur parti de ce cours si vous connaissez déjà un peu la structure de données **Arbre**. Consultez [ces](https://www.freecodecamp.org/news/binary-data-structures-an-intro-to-trees-and-heaps-in-javascript-962ab536cb42/) [tutoriels](https://www.freecodecamp.org/news/the-codeless-guide-to-tree-data-structures/) si vous avez besoin d'un rappel.

Nous aborderons les algorithmes de parcours pour les **Arbres Binaires** et les **Arbres N-aires** (dans lesquels chaque nœud parent a un nombre arbitraire d'enfants).

Si vous avez déjà entendu parler des Arbres Binaires de Recherche (ABR), c'est un type spécial d'Arbre Binaire, donc les techniques que nous allons apprendre ici s'appliquent également.

Les arbres sont un sujet d'entretien favori parmi les grandes entreprises technologiques comme Google, Microsoft et Facebook, alors étudions ce sujet !

Nous apprendrons quatre techniques de parcours et résoudreons leurs problèmes LeetCode correspondants de manière pratique.

Les quatre techniques sont :

* **Pré-ordre (Recherche en Profondeur, DFS)**

* **Post-ordre**

* **In-ordre**

* **Par niveau (Recherche en Largeur, BFS).**

## Plan du cours

Cette vidéo de cours dure au total 30 minutes et comprend :

* Une description de haut niveau des quatre techniques de parcours : **pré-ordre, post-ordre, in-ordre et par niveau**

* Les implémentations **récursives** de pré-ordre, post-ordre et in-ordre (Note : cela ne s'applique pas au parcours par niveau)

* Les implémentations **itératives** de pré-ordre, post-ordre, in-ordre et par niveau

* Une extension des modèles des **Arbres Binaires** aux **Arbres N-aires**

Plongeons dans chacune des quatre techniques ci-dessous.

## Démonstration du parcours d'arbres à l'aide d'un exemple d'arbre

Nous utiliserons l'arbre suivant pour démontrer le résultat des quatre techniques de parcours.

Notez que cet arbre est un simple Arbre Binaire, pas un Arbre Binaire de Recherche (ABR). Un ABR est un type spécial d'Arbre Binaire, donc nos techniques s'appliquent également. De plus, le **parcours in-ordre** devient particulièrement intéressant lorsque nous travaillons avec un ABR, comme nous le verrons ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-16-at-2.48.44-PM.png align="left")

*Un exemple d'Arbre Binaire. Notez qu'il ne s'agit pas d'un Arbre Binaire de Recherche (ABR).*

Étant donné cet arbre, le résultat du parcours des quatre techniques est le suivant :

* Pré-ordre : 1, 2, 4, 5, 3

* Post-ordre : 4, 5, 2, 3, 1

* In-ordre : 4, 2, 5, 1, 3

* Par niveau : 1, 2, 3, 4, 5

### Parcours en pré-ordre

Le parcours en pré-ordre est également connu sous le nom de **Recherche en Profondeur (DFS)** si nous analysons l'arbre comme un graphe et prenons le nœud racine de l'arbre comme notre nœud de départ dans la recherche.

Comme dans l'exemple ci-dessus, nous allons tout droit jusqu'au nœud le plus à gauche avant de visiter tout autre nœud qui est un enfant gauche d'un nœud parent.

Le parcours en pré-ordre nous permet d'explorer les racines avant les feuilles et est donc idéal pour des tâches comme la copie d'un arbre.

### Parcours en post-ordre

Le parcours en post-ordre fait l'inverse du parcours en pré-ordre, nous permettant d'explorer les feuilles avant les racines.

### Parcours en in-ordre

Le parcours en in-ordre est particulièrement utile pour aplatir un arbre en une représentation de tableau.

Pour un Arbre Binaire de Recherche comme ci-dessous, le parcours en in-ordre produit un tableau dans un ordre trié, non décroissant : -4, 3, 2, 5, 18.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-16-at-2.51.44-PM.png align="left")

*Exemple d'Arbre Binaire de Recherche*

### Parcours par niveau

Le parcours par niveau est également connu sous le nom de **Recherche en Largeur (BFS)** si nous considérons l'arbre comme un graphe et commençons notre recherche à partir du nœud racine de l'arbre.

Nous visitons chaque nœud du niveau actuel (profondeur) avant de passer à ceux du niveau suivant. Effectivement, nous visitons le voisin immédiat de (à un pas de) notre nœud actuel avant de visiter les voisins qui sont plus éloignés.

## Comment implémenter ces quatre techniques

Nous utiliserons la définition suivante pour un nœud d'un Arbre Binaire :

```python
# Définition pour un nœud d'arbre binaire.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

### Implémentation récursive

Les implémentations récursives sont les plus simples. La chose la plus importante à retenir est l'ordre dans lequel nous concaténons les résultats des deux appels récursifs (un sur le sous-arbre gauche et un sur le sous-arbre droit) avec la valeur du nœud actuel.

```pgsql
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

### Implémentation itérative

Comparées aux implémentations récursives, les implémentations itératives sont non triviales. La plupart nécessitent que nous utilisions soit une pile soit une file d'attente pour suivre les nœuds que nous devons visiter.

```python
def preorder(self, root):
    if not root:
        return []
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        # notez que nous ajoutons l'enfant droit avant l'enfant gauche
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ret
```

```python
def postorder(self, root):
    if not root:
        return []
    from collections import deque
    ret = deque()
    stack = [root]
    while stack:
        node = stack.pop()
        ret.appendleft(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret
```

L'implémentation pour le parcours in-ordre semble assez différente de pré-ordre et post-ordre :

```python
def inorder(self, root):
    if not root:
        return []
    ret = []
    stack = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ret.append(root.val)
        root = root.right
    return ret
```

Enfin, nous avons le parcours par niveau, où nous allons produire le résultat sous la forme `[[nœuds du premier niveau], [nœuds du deuxième niveau], [nœuds du troisième niveau], ...]`.

```python
def levelorder(self, root):
    if not root:
        return []
    ret = []
    from collections import deque
    queue = deque([root])
    while queue:
        ret_row = []
        # taille fixe pour le niveau actuel
        for _ in range(len(queue)):
            node = queue.popleft()
            ret_row.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.append(ret_row)
    return ret
```

### Arbres N-aires

Nous étendons maintenant nos modèles de la gestion des Arbres Binaires à la gestion des Arbres N-aires. Nous utilisons la définition suivante pour le nœud d'un Arbre N-aire :

```python
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
```

Pour étendre nos implémentations itératives afin de gérer les Arbres N-aires, tout ce que nous devons faire est de nous assurer que nous ajoutons les nœuds enfants que nous allons visiter dans un ordre correct.

Rappelons que dans le parcours en pré-ordre, nous avons ajouté l'enfant droit avant l'enfant gauche. Donc, lorsque nous ajoutons les enfants d'un nœud d'un Arbre N-aire, nous devons inverser la liste des enfants.

```python
def preorder(self, root):
    if not root:
        return []
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        # inverser la liste des enfants
        for child in node.children[::-1]:
            stack.append(child)
    return ret
```

Pour les autres techniques de parcours, puisque nous ajoutons les enfants de gauche à droite, nous pouvons itérer sur la liste des enfants normalement :

```python
def postorder(self, root):
    if not root:
        return []
    from collections import deque
    ret = deque()
    stack = [root]
    while stack:
        node = stack.pop()
        ret.appendleft(node.val)
        for child in node.children:
            stack.append(child)
    return ret
```

```python
def levelorder(self, root):
    if not root:
        return []
    ret = []
    from collections import deque
    queue = deque([root])
    while queue:
        ret_row = []
        # taille fixe pour le niveau actuel
        for _ in range(len(queue)):
            node = queue.popleft()
            ret_row.append(node.val)
            for child in node.children:
                queue.append(child)
        ret.append(ret_row)
    return ret
```

Et maintenant, nous pouvons appliquer nos modèles de parcours d'arbres aux arbres qui ont un nombre arbitraire d'enfants à chaque nœud.

## Conclusion

Dans ce cours accéléré sur le parcours d'arbres, nous avons appris quatre techniques : pré-ordre, post-ordre, in-ordre et par niveau. Nous avons discuté de leurs différences et des tâches pour lesquelles elles sont les mieux adaptées.

Nous les avons également implémentées à la fois de manière récursive et itérative. Enfin, mais non des moindres, nous avons étendu les techniques pour traiter non seulement les Arbres Binaires, mais aussi les Arbres N-aires.

J'espère que vous vous sentez maintenant plus confiant concernant les questions d'entretien sur le parcours d'arbres. C'est également une belle transition vers le sujet de mon prochain cours accéléré sur le parcours de graphes.

Avec la connaissance du parcours en pré-ordre et du parcours par niveau, DFS et BFS ne seront pas complètement nouveaux pour vous 🤓 Je parlerai même de la façon dont j'ai appliqué le parcours de graphes lors du développement d'un algorithme pour [mon jeu de match-three, Clicky Galaxy](https://github.com/RuolinZheng08/unity-clicky-galaxy), alors restez à l'écoute !

## Ressources

Regardez le cours ici :

%[https://youtu.be/uaeCfsCcYWo]

Accédez au modèle de code sur mon GitHub :

%[https://gist.github.com/RuolinZheng08/f6e55b09eb096fe5fe630249cd859b07]

Consultez toute la série de cours accélérés :

%[https://youtube.com/playlist?list=PLKcjA7XxXuvSsE-_heuBxIvzWcx4IKfXD]

Et enfin, n'hésitez pas à vous abonner à ma chaîne YouTube pour plus de contenu comme celui-ci :)

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]