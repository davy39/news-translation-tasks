---
title: Tout ce que vous devez savoir sur les structures de données en arbre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-05T20:58:27.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WeWOBZy6N7cXkq4inS7FVA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Tout ce que vous devez savoir sur les structures de données en arbre
seo_desc: 'By TK

  When you first learn to code, it’s common to learn arrays as the “main data structure.”

  Eventually, you will learn about hash tables too. If you are pursuing a Computer
  Science degree, you have to take a class on data structure. You will also l...'
---

Par TK

Lorsque vous commencez à apprendre à coder, il est courant d'apprendre les tableaux comme la « principale structure de données ».

Eventuellement, vous apprendrez également les `tables de hachage`. Si vous poursuivez un diplôme en informatique, vous devez suivre un cours sur les structures de données. Vous apprendrez également les `listes chaînées`, les `files d'attente` et les `piles`. Ces structures de données sont appelées structures de données « linéaires » car elles ont toutes un début logique et une fin logique.

Lorsque nous commençons à apprendre les `arbres` et les `graphes`, cela peut devenir vraiment confus. Nous ne stockons pas les données de manière linéaire. Les deux structures de données stockent les données de manière spécifique.

Cet article est là pour vous aider à mieux comprendre la structure de données en arbre et à clarifier toute confusion que vous pourriez avoir à ce sujet.

Dans cet article, nous apprendrons :

* Qu'est-ce qu'un arbre
* Des exemples d'arbres
* Sa terminologie et son fonctionnement
* Comment implémenter des structures d'arbres en code.

Commençons ce voyage d'apprentissage. :)

### Définition

Lorsque l'on commence la programmation, il est courant de mieux comprendre les structures de données linéaires que les structures de données comme les arbres et les graphes.

Les arbres sont bien connus comme une structure de données non linéaire. Ils ne stockent pas les données de manière linéaire. Ils organisent les données de manière hiérarchique.

### Plongeons dans des exemples de la vie réelle !

Que veux-je dire lorsque je dis de manière hiérarchique ?

Imaginez un arbre généalogique avec des relations de toutes les générations : grands-parents, parents, enfants, frères et sœurs, etc. Nous organisons couramment les arbres généalogiques de manière hiérarchique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MasdC5DmucEU2abIXQe45Q.jpeg)
_Mon arbre généalogique_

Le dessin ci-dessus est mon arbre généalogique. `Tossico, Akikazu, Hitomi` et `Takemi` sont mes grands-parents.

`Toshiaki` et `Juliana` sont mes parents.

`TK, Yuji, Bruno` et `Kaio` sont les enfants de mes parents (moi et mes frères).

La structure d'une organisation est un autre exemple de hiérarchie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GsBCmW5E1GuJ3MpH3Zz0Ew.jpeg)
_La structure d'une entreprise est un exemple de hiérarchie_

En HTML, le Document Object Model (DOM) fonctionne comme un arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dLXUdR4NuIZG8GJdu_Cinw.jpeg)
_Document Object Model (DOM)_

La balise `HTML` contient d'autres balises. Nous avons une balise `head` et une balise `body`. Ces balises contiennent des éléments spécifiques. La balise `head` a des balises `meta` et `title`. La balise `body` a des éléments qui s'affichent dans l'interface utilisateur, par exemple, `h1`, `a`, `li`, etc.

### Une définition technique

Un `arbre` est une collection d'entités appelées `nœuds`. Les nœuds sont connectés par des `arêtes`. Chaque `nœud` contient une `valeur` ou des `données`, et il peut ou non avoir un `nœud enfant`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3WN7tIQ-kNBQmY9MgvTuOA.jpeg)

Le `premier nœud` de l'`arbre` est appelé la `racine`. Si ce `nœud racine` est connecté à un autre `nœud`, la `racine` est alors un `nœud parent` et le `nœud` connecté est un `enfant`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9AtR3bhhlMJxQlaUVEQgrw.jpeg)

Tous les `nœuds d'arbre` sont connectés par des liens appelés `arêtes`. C'est une partie importante des `arbres`, car elle gère la relation entre les `nœuds`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j5qKwIxKcEjoxy88EOc1Rg.jpeg)

Les `feuilles` sont les derniers `nœuds` d'un `arbre`. Ce sont des nœuds sans enfants. Comme les vrais arbres, nous avons la `racine`, les `branches`, et enfin les `feuilles`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*c9_5uMUsIy4Q3OA7Q8bJiw.jpeg)

D'autres concepts importants à comprendre sont la `hauteur` et la `profondeur`.

La `hauteur` d'un `arbre` est la longueur du chemin le plus long jusqu'à une `feuille`.

La `profondeur` d'un `nœud` est la longueur du chemin jusqu'à sa `racine`.

### Résumé de la terminologie

* **Racine** est le `nœud` le plus haut de l'`arbre`
* **Arête** est le lien entre deux `nœuds`
* **Enfant** est un `nœud` qui a un `nœud parent`
* **Parent** est un `nœud` qui a une `arête` vers un `nœud enfant`
* **Feuille** est un `nœud` qui n'a pas de `nœud enfant` dans l'`arbre`
* **Hauteur** est la longueur du chemin le plus long jusqu'à une `feuille`
* **Profondeur** est la longueur du chemin jusqu'à sa `racine`

### Arbres binaires

Maintenant, nous allons discuter d'un type spécifique d'`arbre`. Nous l'appelons l'`arbre binaire`.

> « En informatique, un arbre binaire est une structure de données arborescente dans laquelle chaque nœud a au plus deux enfants, qui sont appelés l'enfant gauche et l'enfant droit. » — [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree)

Alors, regardons un exemple d'`arbre binaire`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ofbwuz4inpf2OlB-l9gtHw.jpeg)

### Codons un arbre binaire

La première chose à garder à l'esprit lorsque nous implémentons un `arbre binaire` est qu'il s'agit d'une collection de `nœuds`. Chaque `nœud` a trois attributs : `valeur`, `enfant_gauche` et `enfant_droit`.

Comment implémentons-nous un simple `arbre binaire` qui s'initialise avec ces trois propriétés ?

Regardons cela.

```py
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
```

Voici notre classe `arbre binaire`.

Lorsque nous instancions un objet, nous passons la `valeur` (les données du nœud) en tant que paramètre. Regardez `left_child` et `right_child`. Les deux sont définis sur `None`.

Pourquoi ?

Parce que lorsque nous créons notre `nœud`, il n'a pas d'enfants. Nous avons juste les `données du nœud`.

Testons cela :

```py
tree = BinaryTree('a')
print(tree.value) # a
print(tree.left_child) # None
print(tree.right_child) # None
```

C'est tout.

Nous pouvons passer la `chaîne` 'a' comme `valeur` à notre `nœud d'arbre binaire`. Si nous imprimons la `valeur`, `left_child` et `right_child`, nous pouvons voir les valeurs.

Passons à la partie insertion. Que devons-nous faire ici ?

Nous allons implémenter une méthode pour insérer un nouveau `nœud` à `droite` et à `gauche`.

Voici les règles :

* Si le `nœud` actuel n'a pas d'`enfant gauche`, nous créons simplement un nouveau `nœud` et le définissons comme `enfant gauche` du nœud actuel.
* S'il a un `enfant gauche`, nous créons un nouveau nœud et le plaçons à la place de l'`enfant gauche` actuel. Allouez cet `enfant gauche` au `enfant gauche` du nouveau nœud.

Dessinons cela. :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ofbwuz4inpf2OlB-l9gtHw.jpeg)

Voici le code :

```py
def insert_left(self, value):
    if self.left_child == None:
        self.left_child = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left_child = self.left_child
        self.left_child = new_node
```

Encore une fois, si le nœud actuel n'a pas d'`enfant gauche`, nous créons simplement un nouveau nœud et le définissons comme `enfant gauche` du nœud actuel. Sinon, nous créons un nouveau nœud et le plaçons à la place de l'`enfant gauche` actuel. Allouez cet `enfant gauche` au `enfant gauche` du nouveau nœud.

Et nous faisons la même chose pour insérer un `nœud enfant droit`.

```py
def insert_right(self, value):
    if self.right_child == None:
        self.right_child = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.right_child = self.right_child
        self.right_child = new_node
```

Terminé. :)

Mais pas entièrement. Nous devons encore le tester.

Construisons l'`arbre` suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*V_EUgNXVc8Wy9H1-JoqT3g.jpeg)

Pour résumer l'illustration de cet arbre :

* Le `nœud` `a` sera la `racine` de notre `arbre binaire`
* L'`enfant gauche` de `a` est le `nœud` `b`
* L'`enfant droit` de `a` est le `nœud` `c`
* L'`enfant droit` de `b` est le `nœud` `d` (`nœud` `b` n'a pas d'`enfant gauche`)
* L'`enfant gauche` de `c` est le `nœud` `e`
* L'`enfant droit` de `c` est le `nœud` `f`
* Les `nœuds` `e` et `f` n'ont pas d'enfants

Voici le code pour l'`arbre` :

```py
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f
```

L'insertion est terminée.

Maintenant, nous devons penser au parcours de l'`arbre`.

Nous avons **deux options** ici : **Recherche en profondeur (DFS)** et **Recherche en largeur (BFS)**.

* **DFS** « est un algorithme pour parcourir ou rechercher une structure de données arborescente. On commence à la racine et explore aussi loin que possible le long de chaque branche avant de revenir en arrière. » — [Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
* **BFS** « est un algorithme pour parcourir ou rechercher une structure de données arborescente. Il commence à la racine de l'arbre et explore les nœuds voisins en premier, avant de passer aux voisins du niveau suivant. » — [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)

Alors, plongeons dans chaque type de parcours d'arbre.

#### Recherche en profondeur (DFS)

**DFS** explore un chemin jusqu'à une feuille avant de **revenir en arrière** et d'explorer un autre chemin. Regardons un exemple avec ce type de parcours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-sCuUx3R9e1ougu2pGdThg.jpeg)

Le résultat pour cet algorithme sera 1–2–3–4–5–6–7.

Pourquoi ?

Décomposons cela.

1. Commencez à la `racine` (1). Imprimez-la.

2. Allez à l'`enfant gauche` (2). Imprimez-le.

3. Puis allez à l'`enfant gauche` (3). Imprimez-le. (Ce `nœud` n'a pas d'enfants)

4. Revenez en arrière et allez à l'`enfant droit` (4). Imprimez-le. (Ce `nœud` n'a pas d'enfants)

5. Revenez en arrière au `nœud` `racine` et allez à l'`enfant droit` (5). Imprimez-le.

6. Allez à l'`enfant gauche` (6). Imprimez-le. (Ce `nœud` n'a pas d'enfants)

7. Revenez en arrière et allez à l'`enfant droit` (7). Imprimez-le. (Ce `nœud` n'a pas d'enfants)

8. Terminé.

Lorsque nous allons profondément jusqu'à la feuille et revenons en arrière, cela s'appelle l'algorithme **DFS**.

Maintenant que nous sommes familiers avec cet algorithme de parcours, nous discuterons des types de **DFS** : `pré-ordre`, `in-ordre` et `post-ordre`.

#### Pré-ordre

C'est exactement ce que nous avons fait dans l'exemple ci-dessus.

1. Imprimez la valeur du `nœud`.
2. Allez à l'`enfant gauche` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant gauche`.
3. Allez à l'`enfant droit` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant droit`.

```py
def pre_order(self):
    print(self.value)

    if self.left_child:
        self.left_child.pre_order()

    if self.right_child:
        self.right_child.pre_order()
```

#### In-ordre

![Image](https://cdn-media-1.freecodecamp.org/images/1*-sCuUx3R9e1ougu2pGdThg.jpeg)

Le résultat de l'algorithme in-ordre pour cet exemple d'`arbre` est 3–2–4–1–6–5–7.

Le gauche d'abord, le milieu ensuite, et le droit en dernier.

Maintenant, codons cela.

```py
def in_order(self):
    if self.left_child:
        self.left_child.in_order()

    print(self.value)

    if self.right_child:
        self.right_child.in_order()
```

1. Allez à l'`enfant gauche` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant gauche`.
2. Imprimez la valeur du `nœud`
3. Allez à l'`enfant droit` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant droit`.

#### Post-ordre

![Image](https://cdn-media-1.freecodecamp.org/images/1*-sCuUx3R9e1ougu2pGdThg.jpeg)

Le résultat de l'algorithme `post-ordre` pour cet exemple d'`arbre` est 3–4–2–6–7–5–1.

Le gauche d'abord, le droit ensuite, et le milieu en dernier.

Codons cela.

```
def post_order(self):
    if self.left_child:
        self.left_child.post_order()

    if self.right_child:
        self.right_child.post_order()

    print(self.value)
```

1. Allez à l'`enfant gauche` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant gauche`.
2. Allez à l'`enfant droit` et imprimez-le. Cela est fait si, et seulement si, il a un `enfant droit`.
3. Imprimez la valeur du `nœud`

#### Recherche en largeur (BFS)

L'algorithme **BFS** parcourt l'`arbre` niveau par niveau et profondeur par profondeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNxp_NkRZLCeak85rreebA.jpeg)

Voici un exemple qui aide à mieux expliquer cet algorithme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-sCuUx3R9e1ougu2pGdThg.jpeg)

Donc, nous parcourons niveau par niveau. Dans cet exemple, le résultat est 1–2–5–3–4–6–7.

* Niveau/Profondeur 0 : seul `nœud` avec la valeur 1
* Niveau/Profondeur 1 : `nœuds` avec les valeurs 2 et 5
* Niveau/Profondeur 2 : `nœuds` avec les valeurs 3, 4, 6 et 7

Maintenant, codons cela.

```py
def bfs(self):
    queue = Queue()
    queue.put(self)

    while not queue.empty():
        current_node = queue.get()
        print(current_node.value)

        if current_node.left_child:
            queue.put(current_node.left_child)

        if current_node.right_child:
            queue.put(current_node.right_child)
```

Pour implémenter un algorithme **BFS**, nous utilisons la structure de données `file d'attente` pour aider.

Comment cela fonctionne-t-il ?

Voici l'explication.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A4yGfEoiqcZ-COvAfr2CWQ.jpeg)

1. Ajoutez d'abord le `nœud` `racine` dans la `file d'attente` avec la méthode `put`.
2. Itérez tant que la `file d'attente` n'est pas vide.
3. Obtenez le premier `nœud` dans la `file d'attente`, puis imprimez sa valeur.
4. Ajoutez les `enfants` `gauche` et `droit` dans la `file d'attente` (si le `nœud` actuel a des `enfants`).
5. Terminé. Nous imprimerons la valeur de chaque `nœud`, niveau par niveau, avec notre aide `file d'attente`.

### Arbre de recherche binaire

> « Un arbre de recherche binaire est parfois appelé arbre binaire ordonné ou trié, et il maintient ses valeurs dans l'ordre trié, de sorte que la recherche et d'autres opérations peuvent utiliser le principe de la recherche binaire » — [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)

Une propriété importante d'un `arbre de recherche binaire` est que la valeur d'un `nœud` d'un `arbre de recherche binaire` est plus grande que la valeur de la descendance de son `enfant gauche`, mais plus petite que la valeur de la descendance de son `enfant droit`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mslH9VtVUN9Hs983XxUN5A.jpeg)

Voici une décomposition de l'illustration ci-dessus :

* **A** est inversé. Le `sous-arbre` 7–5–8–6 doit être du côté droit, et le `sous-arbre` 2–1–3 doit être du côté gauche.
* **B** est la seule option correcte. Il satisfait la propriété de l'`arbre de recherche binaire`.
* **C** a un problème : le `nœud` avec la valeur 4. Il doit être du côté gauche de la `racine` car il est plus petit que 5.

### Codons un arbre de recherche binaire !

Maintenant, il est temps de coder !

Que verrons-nous ici ? Nous allons insérer de nouveaux nœuds, rechercher une valeur, supprimer des nœuds et équilibrer l'`arbre`.

Commençons.

#### Insertion : ajout de nouveaux nœuds à notre arbre

Imaginez que nous avons un `arbre` vide et que nous voulons ajouter de nouveaux `nœuds` avec les valeurs suivantes dans cet ordre : 50, 76, 21, 4, 32, 100, 64, 52.

La première chose que nous devons savoir est si 50 est la `racine` de notre arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fxSlTwgQSN_DlzfEmcxqQg.jpeg)

Nous pouvons maintenant commencer à insérer `nœud` par `nœud`.

* 76 est plus grand que 50, donc insérez 76 du côté droit.
* 21 est plus petit que 50, donc insérez 21 du côté gauche.
* 4 est plus petit que 50. Le `nœud` avec la valeur 50 a un `enfant gauche` 21. Puisque 4 est plus petit que 21, insérez-le du côté gauche de ce `nœud`.
* 32 est plus petit que 50. Le `nœud` avec la valeur 50 a un `enfant gauche` 21. Puisque 32 est plus grand que 21, insérez 32 du côté droit de ce `nœud`.
* 100 est plus grand que 50. Le `nœud` avec la valeur 50 a un `enfant droit` 76. Puisque 100 est plus grand que 76, insérez 100 du côté droit de ce `nœud`.
* 64 est plus grand que 50. Le `nœud` avec la valeur 50 a un `enfant droit` 76. Puisque 64 est plus petit que 76, insérez 64 du côté gauche de ce `nœud`.
* 52 est plus grand que 50. Le `nœud` avec la valeur 50 a un `enfant droit` 76. Puisque 52 est plus petit que 76, le `nœud` avec la valeur 76 a un `enfant gauche` 64. 52 est plus petit que 64, donc insérez 54 du côté gauche de ce `nœud`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LlLDNx7wgJfH6VAGnyAbIQ.jpeg)

Remarquez-vous un motif ici ?

Décomposons cela.

1. La valeur du nouveau `nœud` est-elle plus grande ou plus petite que le `nœud` actuel ?
2. Si la valeur du nouveau `nœud` est plus grande que le `nœud` actuel, allez au `sous-arbre` droit. Si le `nœud` actuel n'a pas d'`enfant droit`, insérez-le là, sinon revenez à l'étape #1.
3. Si la valeur du nouveau `nœud` est plus petite que le `nœud` actuel, allez au `sous-arbre` gauche. Si le `nœud` actuel n'a pas d'`enfant gauche`, insérez-le là, sinon revenez à l'étape #1.
4. Nous n'avons pas traité les cas spéciaux ici. Lorsque la valeur d'un nouveau `nœud` est égale à la valeur actuelle du `nœud`, utilisez la règle numéro 3. Considérez l'insertion de valeurs égales du côté gauche du `sous-arbre`.

Maintenant, codons cela.

```py
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)
```

Cela semble très simple.

La partie puissante de cet algorithme est la partie récursive, qui se trouve aux lignes 9 et 13. Ces deux lignes de code appellent la méthode `insert_node`, et l'utilisent pour ses `enfants` `gauche` et `droit`, respectivement. Les lignes 11 et 15 sont celles qui effectuent l'insertion pour chaque `enfant`.

#### Recherchons la valeur du nœud... Ou pas...

L'algorithme que nous allons construire maintenant concerne les recherches. Pour une valeur donnée (nombre entier), nous dirons si notre `arbre de recherche binaire` contient ou non cette valeur.

Un élément important à noter est la manière dont nous avons défini l'algorithme d'**insertion de l'arbre**. D'abord, nous avons notre `nœud` `racine`. Tous les `nœuds` du `sous-arbre` gauche auront des valeurs plus petites que le `nœud` `racine`. Et tous les `nœuds` du `sous-arbre` droit auront des valeurs plus grandes que le `nœud` `racine`.

Regardons un exemple.

Imaginez que nous avons cet `arbre`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LlLDNx7wgJfH6VAGnyAbIQ.jpeg)

Maintenant, nous voulons savoir si nous avons un nœud basé sur la valeur 52.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NwvTrpKiJWb1u2yAY-nnAA.jpeg)

Décomposons cela.

1. Nous commençons avec le `nœud` `racine` comme notre `nœud` actuel. La valeur donnée est-elle plus petite que la valeur du `nœud` actuel ? Si oui, alors nous la rechercherons dans le `sous-arbre` gauche.
2. La valeur donnée est-elle plus grande que la valeur du `nœud` actuel ? Si oui, alors nous la rechercherons dans le `sous-arbre` droit.
3. Si les règles #1 et #2 sont toutes deux fausses, nous pouvons comparer la valeur du `nœud` actuel et la valeur donnée si elles sont égales. Si la comparaison retourne `vrai`, alors nous pouvons dire : « Oui ! Notre `arbre` a la valeur donnée », sinon, nous disons : « Non, il ne l'a pas. »

Maintenant, codons cela.

```py
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value
```

Décomposons le code :

* Les lignes 8 et 9 relèvent de la règle #1.
* Les lignes 10 et 11 relèvent de la règle #2.
* La ligne 13 relève de la règle #3.

Comment le testons-nous ?

Créons notre `arbre de recherche binaire` en initialisant le `nœud` `racine` avec la valeur 15.

```py
bst = BinarySearchTree(15)
```

Et maintenant, nous allons insérer de nombreux nouveaux `nœuds`.

```py
bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)
```

Pour chaque `nœud` inséré, nous testerons si notre méthode `find_node` fonctionne vraiment.

```py
print(bst.find_node(15)) # True
print(bst.find_node(10)) # True
print(bst.find_node(8)) # True
print(bst.find_node(12)) # True
print(bst.find_node(20)) # True
print(bst.find_node(17)) # True
print(bst.find_node(25)) # True
print(bst.find_node(19)) # True
```

Oui, cela fonctionne pour ces valeurs données ! Testons pour une valeur qui n'existe pas dans notre `arbre de recherche binaire`.

```py
print(bst.find_node(0)) # False
```

Oh oui.

Notre recherche est terminée.

#### Suppression : suppression et organisation

La suppression est un algorithme plus complexe car nous devons gérer différents cas. Pour une valeur donnée, nous devons supprimer le `nœud` avec cette valeur. Imaginez les scénarios suivants pour ce `nœud` : il n'a pas d'`enfants`, a un seul `enfant`, ou a deux `enfants`.

* **Scénario #1** : Un `nœud` sans `enfants` (`nœud` `feuille`).

```py
#        |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (SUPPRIMER 20) --->   |30|   |70|
#   /    \                                \
# |20|   |40|                             |40|
```

Si le `nœud` que nous voulons supprimer n'a pas d'enfants, nous le supprimons simplement. L'algorithme n'a pas besoin de réorganiser l'`arbre`.

* **Scénario #2** : Un `nœud` avec un seul enfant (`enfant` `gauche` ou `droit`).

```py
#        |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (SUPPRIMER 30) --->   |20|   |70|
#   /            
# |20|
```

Dans ce cas, notre algorithme doit faire en sorte que le parent du `nœud` pointe vers le `nœud` enfant. Si le `nœud` est l'`enfant gauche`, nous faisons en sorte que le parent de l'`enfant gauche` pointe vers l'`enfant`. Si le `nœud` est l'`enfant droit` de son parent, nous faisons en sorte que le parent de l'`enfant droit` pointe vers l'`enfant`.

* **Scénario #3** : Un `nœud` avec deux enfants.

```py
#        |50|                              |50|
#      /      \                           /    \
#    |30|     |70|   (SUPPRIMER 30) --->   |40|   |70|
#   /    \                             /
# |20|   |40|                        |20|
```

Lorsque le `nœud` a 2 enfants, nous devons trouver le `nœud` avec la valeur minimale, en commençant par l'`enfant droit` du `nœud`. Nous placerons ce `nœud` avec la valeur minimale à la place du `nœud` que nous voulons supprimer.

Il est temps de coder.

```py
def remove_node(self, value, parent):
    if value < self.value and self.left_child:
        return self.left_child.remove_node(value, self)
    elif value < self.value:
        return False
    elif value > self.value and self.right_child:
        return self.right_child.remove_node(value, self)
    elif value > self.value:
        return False
    else:
        if self.left_child is None and self.right_child is None and self == parent.left_child:
            parent.left_child = None
            self.clear_node()
        elif self.left_child is None and self.right_child is None and self == parent.right_child:
            parent.right_child = None
            self.clear_node()
        elif self.left_child and self.right_child is None and self == parent.left_child:
            parent.left_child = self.left_child
            self.clear_node()
        elif self.left_child and self.right_child is None and self == parent.right_child:
            parent.right_child = self.left_child
            self.clear_node()
        elif self.right_child and self.left_child is None and self == parent.left_child:
            parent.left_child = self.right_child
            self.clear_node()
        elif self.right_child and self.left_child is None and self == parent.right_child:
            parent.right_child = self.right_child
            self.clear_node()
        else:
            self.value = self.right_child.find_minimum_value()
            self.right_child.remove_node(self.value, self)

        return True
```

1. **Premièrement** : Notez les paramètres `value` et `parent`. Nous voulons trouver le `nœud` qui a cette `valeur`, et le `parent` du `nœud` est important pour la suppression du `nœud`.
2. **Deuxièmement** : Notez la valeur de retour. Notre algorithme retournera une valeur booléenne. Il retourne `True` s'il trouve le `nœud` et le supprime. Sinon, il retournera `False`.
3. **De la ligne 2 à la ligne 9** : Nous commençons à rechercher le `nœud` qui a la `valeur` que nous cherchons. Si la `valeur` est plus petite que la `valeur du nœud actuel`, nous allons au `sous-arbre` gauche, de manière récursive (si, et seulement si, le `nœud` actuel a un `enfant gauche`). Si la `valeur` est plus grande, allez au `sous-arbre` droit, de manière récursive.
4. **Ligne 10** : Nous commençons à penser à l'algorithme de `suppression`.
5. **De la ligne 11 à la ligne 13** : Nous couvrons le `nœud` sans `enfants`, et il est l'`enfant gauche` de son `parent`. Nous supprimons le `nœud` en définissant l'`enfant gauche` du `parent` sur `None`.
6. **Lignes 14 et 15** : Nous couvrons le `nœud` sans `enfants`, et il est l'`enfant droit` de son `parent`. Nous supprimons le `nœud` en définissant l'`enfant droit` du `parent` sur `None`.
7. **Méthode clear_node** : Je montrerai le code `clear_node` ci-dessous. Il définit les `enfants` `gauche` et `droit` du nœud, et sa `valeur` sur `None`.
8. **De la ligne 16 à la ligne 18** : Nous couvrons le `nœud` avec un seul `enfant` (`enfant gauche`), et il est l'`enfant gauche` de son `parent`. Nous définissons l'`enfant gauche` du `parent` sur l'`enfant gauche` du `nœud` (le seul enfant qu'il a).
9. **De la ligne 19 à la ligne 21** : Nous couvrons le `nœud` avec un seul `enfant` (`enfant gauche`), et il est l'`enfant droit` de son `parent`. Nous définissons l'`enfant droit` du `parent` sur l'`enfant gauche` du `nœud` (le seul enfant qu'il a).
10. **De la ligne 22 à la ligne 24** : Nous couvrons le `nœud` avec un seul `enfant` (`enfant droit`), et il est l'`enfant gauche` de son `parent`. Nous définissons l'`enfant gauche` du `parent` sur l'`enfant droit` du `nœud` (le seul enfant qu'il a).
11. **De la ligne 25 à la ligne 27** : Nous couvrons le `nœud` avec un seul `enfant` (`enfant droit`), et il est l'`enfant droit` de son `parent`. Nous définissons l'`enfant droit` du `parent` sur l'`enfant droit` du `nœud` (le seul enfant qu'il a).
12. **De la ligne 28 à la ligne 30** : Nous couvrons le `nœud` avec les deux `enfants` `gauche` et `droit`. Nous obtenons le `nœud` avec la plus petite `valeur` (le code est montré ci-dessous) et le définissons comme `valeur` du `nœud` actuel. Terminez en supprimant le plus petit `nœud`.
13. **Ligne 32** : Si nous trouvons le `nœud` que nous cherchons, il doit retourner `True`. De la ligne 11 à la ligne 31, nous gérons ce cas. Donc, retournez simplement `True` et c'est tout.

* Pour utiliser la méthode `clear_node` : définissez la valeur `None` pour les trois attributs — (`valeur`, `enfant_gauche` et `enfant_droit`)

```py
def clear_node(self):
    self.value = None
    self.left_child = None
    self.right_child = None
```

* Pour utiliser la méthode `find_minimum_value` : allez tout en bas à gauche. Si nous ne pouvons plus trouver de nœuds, nous avons trouvé le plus petit.

```py
def find_minimum_value(self):
    if self.left_child:
        return self.left_child.find_minimum_value()
    else:
        return self.value
```

Maintenant, testons cela.

Nous utiliserons cet `arbre` pour tester notre algorithme `remove_node`.

```py
#        |15|
#      /      \
#    |10|     |20|
#   /    \    /    \
# |8|   |12| |17| |25|
#              \
#              |19|
```

Supprimons le `nœud` avec la `valeur` 8. C'est un `nœud` sans enfant.

```py
print(bst.remove_node(8, None)) # True
bst.pre_order_traversal()

#     |15|
#   /      \
# |10|     |20|
#    \    /    \
#   |12| |17| |25|
#          \
#          |19|
```

Maintenant, supprimons le `nœud` avec la `valeur` 17. C'est un `nœud` avec un seul enfant.

```py
print(bst.remove_node(17, None)) # True
bst.pre_order_traversal()

#        |15|
#      /      \
#    |10|     |20|
#       \    /    \
#      |12| |19| |25|
```

Enfin, nous allons supprimer un `nœud` avec deux enfants. C'est la `racine` de notre `arbre`.

```py
print(bst.remove_node(15, None)) # True
bst.pre_order_traversal()

#        |19|
#      /      \
#    |10|     |20|
#        \        \
#        |12|     |25|
```

Les tests sont maintenant terminés. :)

### C'est tout pour l'instant !

Nous avons beaucoup appris ici.

Félicitations pour avoir terminé ce contenu dense. C'est vraiment difficile de comprendre un concept que nous ne connaissons pas. Mais vous l'avez fait. :)

C'est une étape de plus en avant dans mon voyage pour apprendre et maîtriser les algorithmes et les structures de données. Vous pouvez voir la documentation de mon voyage complet ici sur ma publication [**Renaissance Developer**](https://medium.com/the-renaissance-developer).

Amusez-vous, continuez à apprendre et à coder.

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺

### Ressources supplémentaires

* [Introduction à la structure de données en arbre par **mycodeschool**](https://www.youtube.com/watch?v=qH6yxkw0u78&index=25&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
* [Arbre par **Wikipedia**](https://en.wikipedia.org/wiki/Tree_(data_structure))
* [Comment ne pas être déconcerté par les arbres par la talentueuse Vaidehi Joshi](https://medium.com/basecs/how-to-not-be-stumped-by-trees-5f36208f68a7)
* [Introduction aux arbres, conférence par le professeur **Jonathan Cohen**](http://www.cs.jhu.edu/~cohen/CS226/Lectures/Trees.pdf)
* [Introduction aux arbres, conférence par le professeur **David Schmidt**](http://people.cs.ksu.edu/~schmidt/300s05/Lectures/Week7b.html)
* [Introduction aux arbres, conférence par le professeur **Victor Adamchik**](http://www.cs.cmu.edu/~clo/www/CMU/DataStructures/Lessons/lesson4_1.htm)
* [Arbres avec **Gayle Laakmann McDowell**](https://www.youtube.com/watch?v=oSWTXtMglKE)
* [Implémentation d'arbre binaire](https://github.com/leandrotk/algorithms/blob/master/computer_science/data_structures/binary_tree/binary_tree.py) et [Tests](https://github.com/leandrotk/algorithms/blob/master/computer_science/data_structures/binary_tree/test_binary_tree.py) par [**TK**](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/undefined)
* [Cours Coursera : Structures de données par **Université de Californie, San Diego**](https://www.coursera.org/learn/data-structures)
* [Cours Coursera : Structures de données et performance par **Université de Californie, San Diego**](https://www.coursera.org/learn/data-structures-optimizing-performance)
* [Concepts et implémentation d'arbre de recherche binaire par **Paul Programming**](https://www.youtube.com/playlist?list=PLTxllHdfUq4d-DE16EDkpeb8Z68DU7Z_Q)
* [Implémentation d'arbre de recherche binaire](https://github.com/leandrotk/algorithms/blob/master/computer_science/data_structures/binary_search_tree_without_node/binary_search_tree.py) et [Tests](https://github.com/leandrotk/algorithms/blob/master/computer_science/data_structures/binary_search_tree_without_node/test_binary_search_tree.py) par [**TK**](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/undefined)
* [Parcours d'arbre par **Wikipedia**](https://en.wikipedia.org/wiki/Tree_traversal)
* [Algorithme de suppression de nœud d'arbre de recherche binaire par **GeeksforGeeks**](http://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)
* [Algorithme de suppression de nœud d'arbre de recherche binaire](http://www.algolist.net/Data_structures/Binary_search_tree/Removal) par **Algolist**
* [Apprendre Python de zéro à héros](https://www.freecodecamp.org/news/learning-python-from-zero-to-hero-120ea540b567/)