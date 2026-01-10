---
title: 'Guide des questions d''entretien Python : comment coder une liste chaînée'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T21:50:34.000Z'
originalURL: https://freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y2zqUEPWCjkWCWVnxmy3GQ.jpeg
tags:
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Guide des questions d''entretien Python : comment coder une liste chaînée'
seo_desc: 'By Anthony Sistilli

  I always understood the core concept of Linked Lists, but I never put it into practice.

  It wasn’t until my very first Amazon interview years ago when I realized that I
  had no idea how the concept of Linked Lists translated into co...'
---

Par Anthony Sistilli

J'ai toujours compris le concept de base des listes chaînées, mais je ne l'ai jamais mis en pratique.

Ce n'est que lors de mon tout premier entretien chez Amazon il y a quelques années que j'ai réalisé que je n'avais aucune idée de la manière dont le concept des listes chaînées se traduisait en code.

![Image](https://cdn-media-1.freecodecamp.org/images/hTliWmiFIsrEJqgzgpkHffXflO3tkNIUa5-E)
_*Mon visage lors de mon tout premier entretien chez Amazon*_

Et c'est pourquoi j'écris ce guide !

Mon objectif est de vous aider à obtenir un emploi en tant qu'ingénieur logiciel.

Je souhaite aborder de nombreuses questions d'entretien sur les listes chaînées, et cet article est la première étape de ce processus. Alors, plongeons-nous dans le sujet.

### Qu'est-ce qu'une liste chaînée ?

Une liste chaînée est une structure de données qui se compose de nombreuses mini-structures de données appelées « Nœuds ». Les nœuds se lient ensemble pour former une liste.

![Image](https://cdn-media-1.freecodecamp.org/images/QUIARoltvUdLReB8VIoNcGFPkaAvGwDWOl8d)
_Une liste chaînée entière, composée de 3 nœuds liés ensemble._

#### Chaque nœud contient 2 attributs

1. Sa valeur. Cela peut être n'importe quoi : entiers, caractères, chaînes, objets, etc.
2. Un pointeur vers le nœud suivant dans la séquence.

#### Quelques définitions

**Le « Nœud de tête » :** Le nœud de tête est simplement le premier nœud de la liste chaînée. Comme nous pouvons le voir dans l'exemple ci-dessus, le nœud contenant « 5 » est le premier nœud, et donc la tête.

**Le « Nœud de queue » :** Le nœud de queue est le dernier nœud de la séquence. Puisqu'il s'agit du dernier nœud, il pointe vers null, car il n'y a pas de nœud suivant dans la séquence. Dans l'exemple ci-dessus, le nœud contenant « 3 » serait le nœud de queue.

### Liste simplement chaînée vs liste doublement chaînée

En ce qui concerne les listes chaînées, il existe deux types principaux.

Celles qui sont « simplement » chaînées, et celles qui sont « doublement » chaînées.

**Simplement chaînée** signifie que chaque nœud ne pointe que vers au plus 1 autre nœud, le nœud qui le précède. Cela est illustré dans l'exemple ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/Yii0EYpRWc8SQO4mOq0Lejev6T8uTe4unJfv)
_Un exemple de liste simplement chaînée._

**Doublement chaînée** signifie que chaque nœud peut pointer vers 2 autres nœuds, le nœud qui le précède **et le nœud qui le suit.** Comme nous pouvons le voir dans l'exemple ci-dessous, puisque qu'il n'y a pas de nœud précédant le nœud de tête (qui est 5), l'un de ses pointeurs pointe vers null.

![Image](https://cdn-media-1.freecodecamp.org/images/ucPAE2WqQmZiN1dIkbtr4LpONEZW-UPPnPyI)
_Un exemple de liste doublement chaînée._

### D'accord, je comprends tout cela. Mais comment fonctionne le code ?

Coder des listes chaînées peut être un **problème de 4 lignes ou un problème de 400 lignes.** Cela dépend de la manière dont vous souhaitez l'aborder.

Au niveau le plus simple, comme nous l'avons discuté, une liste chaînée est simplement **un ensemble de nœuds connectés.**

Ainsi, tout ce dont nous avons vraiment besoin pour créer cette structure est un objet nœud.

```
class linkedListNode:    def __init__(self, value, nextNode=None):        self.value = value        self.nextNode = nextNode
```

Ici, nous pouvons voir que nous avons simplement créé une classe qui a un attribut value et nextNode.

Pour créer un nœud, nous passons simplement une valeur.

```
node1 = linkedListNode("3") # "3"node2 = linkedListNode("7") # "7"node3 = linkedListNode("10") # "10"
```

Ici, nous avons créé 3 nœuds individuels.

L'étape suivante consiste simplement à les connecter ensemble.

```
node1.nextNode = node2 node2.nextNode = node3 
```

La première ligne ci-dessus fait pointer node1 vers node2 :

"3" → "7"

La deuxième ligne ci-dessus fait pointer node2 vers node3 :

"7" → "10"

Ensemble, nous obtenons une liste chaînée qui ressemble à ceci :

"3" → "7" → "10" → Null

**Note : "10" pointe vers null, car aucun nextNode n'a été assigné à node3, et le nextNode par défaut est Null.**

Comme je l'ai mentionné précédemment, il existe de nombreuses façons différentes de faire cela. Ceci est simplement la plus simple.

Si vous essayez de créer une classe LinkedList entière, [cette vidéo](https://www.youtube.com/watch?v=6sBsF13n5ig) explique en détail comment faire cela.

### Parcourir une liste chaînée

Si vous passez un entretien de programmation et qu'on vous pose une question sur les listes chaînées, on ne vous donnera pas tous les nœuds.

Tout ce que vous obtiendrez est le nœud de tête.

![Image](https://cdn-media-1.freecodecamp.org/images/05jgbOs3qG84t7qmpEd-Ubhl9QyQgYWUiiV-)
_Tout ce qui est passé ici est le nœud de tête._

À partir de ce nœud de tête, vous devez obtenir le reste de la liste.

Commençons par comprendre comment obtenir la valeur et nextNode d'un nœud en Python.

Disons que nous avons un nœud simplement nommé 'node'.

Obtenir la valeur du nœud :

```
node.value
```

Obtenir le nextNode du nœud :

```
node.nextNode
```

#### **Parcours**

La première chose que nous voulons faire est de créer une variable appelée "currentNode" qui garde une trace du nœud où nous nous trouvons. Nous voulons l'assigner à notre nœud de tête au début.

```
currentNode = head
```

Maintenant, tout ce que nous avons à faire est de vérifier simplement si notre nœud actuel est Null ou non. Si ce n'est pas le cas, nous faisons en sorte que notre 'currentNode' soit égal au 'nextNode' du 'currentNode'.

```
currentNode = node1while currentNode is not None:    currentNode = currentNode.nextNode
```

Disons que nous avons la liste chaînée suivante : "3" → "7" → "10".

Notre tête et premier 'currentNode' est "3".

Lorsque nous faisons

```
currentNode = currentNode.nextNode
```

Nous réassignons 'currentNode' au voisin de notre nœud actuel, qui dans ce cas est "7".

Cela continue jusqu'à ce que currentNode pointe vers None, auquel cas la boucle s'arrête.

Et c'est la manière de base de parcourir une liste chaînée en Python.

[Lien vers le code sur Github.](https://github.com/AtotheY/YoutubeTutorials/blob/master/Introductions/linkedListOnlyNodes.py)

### Insertion d'éléments

Lorsque vous insérez un élément dans une liste chaînée, vous l'insérez à l'arrière sauf indication contraire.

Utilisons l'exemple suivant :

"3" → "7" → "10" → Null

Disons que nous voulons insérer un "4".

Nous trouverions simplement le nœud de queue, dans ce cas "10", et nous définirons son nextNode à notre nœud "4".

"3" → "7" → "10" → "4" → Null

```
node4 = linkedListNode("4")node3.nextNode = node4
```

Maintenant, disons que nous étions en entretien, et que tout ce que nous avions était le nœud de tête.

Nous parcourons simplement la liste chaînée pour trouver la queue. Une fois que nous avons la queue, nous définissons simplement son nextNode à notre nouveau nœud que nous créons.

```
def insertNode(head, valuetoInsert):    currentNode = head    while currentNode is not None:        if currentNode.nextNode is None:            currentNode.nextNode = linkedListNode(valuetoInsert)            return head        currentNode = currentNode.nextNode
```

### Suppression d'éléments

La suppression peut devenir un peu délicate.

Prenons le même exemple.

"3" → "7" → "10" → Null

Si nous voulions supprimer le "7", tout ce que nous devons faire est de pointer le "3" vers le "10" afin que le "7" ne soit jamais référencé.

"3" → "10" → Null

Pour ce faire, nous devrions parcourir la liste tout en gardant non seulement une trace du currentNode, mais aussi en gardant une trace du **previousNode.**

Nous devrions également tenir compte du fait que le nœud de tête pourrait être le nœud que nous voulons supprimer.

Dans le code ci-dessous, nous supprimons simplement la première instance de la valeur que nous voulons supprimer.

Notez qu'il existe de nombreuses façons d'accomplir cela, et la solution ci-dessous pourrait ne pas être le code le plus propre que vous verrez dans votre vie. Cependant, dans le feu de l'action d'un entretien, l'interviewer ne s'attendra probablement pas à un code parfait.

```
def deleteNode(head, valueToDelete):    currentNode = head    previousNode = None    while currentNode is not None:        if currentNode.value == valueToDelete:            if previousNode is None:                 newHead = currentNode.nextNode                currentNode.nextNode = None                return newHead # Supprimé la tête            previousNode.nextNode = currentNode.nextNode            return head        previousNode = currentNode        currentNode = currentNode.nextNode    return head # Valeur à supprimer non trouvée.
```

Dans le code ci-dessus, une fois que nous avons trouvé le nœud que nous voulons supprimer, nous définissons le "nextNode" du nœud précédent au "nextNode" du nœud supprimé pour le retirer complètement de la liste.

### Analyse de la complexité temporelle Big O

****NOTE** Il s'agit des complexités temporelles pour la structure de nœud ci-dessus, qui est la plus susceptible d'apparaître lors d'un entretien. Dans les cas pratiques, vous pouvez stocker des attributs dans une classe LinkedList pour réduire ces complexités.**

'n' = le nombre d'éléments à l'intérieur de la liste chaînée.

**Insertion à l'arrière de la liste chaînée —** Nous parcourons tous les n éléments pour trouver la queue et insérer notre nouveau nœud. **O(n)**

**Insertion à l'avant de la liste chaînée —** Nous créons simplement le nouveau nœud et définissons son nextNode à la tête. Pas besoin de parcourir la liste. **O(1)**

**Parcours —** Nous parcourons tous les n éléments une fois. **O(n)**

**Suppression —** Dans le pire des cas, le nœud que nous supprimons est le dernier nœud, nous obligeant à parcourir toute la liste. **O(n)**

### Vous pouvez maintenant aborder les questions d'entretien sur les listes chaînées !

Vous avez maintenant les connaissances fondamentales nécessaires pour commencer à aborder les questions d'entretien sur les listes chaînées !

Elles peuvent commencer facilement et devenir difficiles très rapidement.

Dans le prochain article, je vais passer en revue quelques questions courantes et techniques que vous pouvez utiliser pour les résoudre.

**Si vous êtes un étudiant cherchant à décrocher votre stage ou emploi à temps plein de rêve dans les deux prochaines années, commencez à pratiquer maintenant !**

J'ai lancé une communauté ([www.theforge.ca](http://www.theforge.ca)) où nous mettons en relation des étudiants avec des mentors et des experts de l'industrie qui les aident à naviguer vers leur emploi de rêve.

Merci d'avoir lu, et bonne chance !