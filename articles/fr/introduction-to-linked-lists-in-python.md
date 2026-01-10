---
title: Les listes chaînées en Python – Explications avec exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-22T16:08:05.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-linked-lists-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/chain-3481377_1280.jpg
tags:
- name: data
  slug: data
- name: Python
  slug: python
seo_title: Les listes chaînées en Python – Explications avec exemples
seo_desc: "By Fakorede Damilola\nDifferent programming languages offer different ways\
  \ to store and access data.\nSome of the data structures you can use are collections\
  \ such as arrays, lists, maps, sets, and so on. \nThese all do an awesome job storing\
  \ and accessi..."
---

Par Fakorede Damilola

Différents langages de programmation offrent différentes manières de stocker et d'accéder aux données.

Certaines des structures de données que vous pouvez utiliser sont des collections telles que les tableaux (arrays), les listes, les maps, les ensembles (sets), et ainsi de suite.

Toutes ces structures font un excellent travail pour stocker et accéder aux données, mais vous pourriez parfois avoir besoin de quelque chose de différent. Une autre structure de données couramment utilisée est appelée une liste chaînée (Linked List).

## Qu'est-ce qu'une liste chaînée ?

Les listes chaînées sont une structure de données qui stocke les données sous la forme d'une chaîne. La structure d'une liste chaînée est telle que chaque élément de donnée possède une connexion avec le suivant (et parfois avec l'élément précédent également). Chaque élément d'une liste chaînée est appelé un nœud (node).

Vous pouvez l'imaginer comme une véritable chaîne, où chaque anneau ou nœud est connecté.
Quelque chose comme ceci

![Image](https://www.freecodecamp.org/news/content/images/2022/09/A-chain.png)

Comme toute autre structure de données, les listes chaînées ont leurs avantages et leurs inconvénients :

### Avantages des listes chaînées :

1. Grâce au système en chaîne des listes chaînées, vous pouvez ajouter et supprimer des éléments rapidement. Cela ne nécessite pas non plus de réorganiser la structure de données, contrairement aux tableaux ou aux listes. Les structures de données linéaires sont souvent plus faciles à implémenter en utilisant des listes chaînées.
2. Les listes chaînées ne nécessitent pas non plus de taille fixe ou de taille initiale en raison de leur structure en chaîne.

### Inconvénients des listes chaînées :

1. Plus de mémoire est requise par rapport à un tableau. C'est parce que vous avez besoin d'un pointeur (qui occupe sa propre mémoire) pour vous diriger vers l'élément suivant.
2. Les opérations de recherche sur une liste chaînée sont très lentes. Contrairement à un tableau, vous n'avez pas l'option d'accès aléatoire.

## Quand devriez-vous utiliser une liste chaînée ?

Vous devriez utiliser une liste chaînée plutôt qu'un tableau quand :

1. Vous ne savez pas combien d'éléments seront dans la liste (c'est l'un des avantages - la facilité d'ajout d'éléments).
2. Vous n'avez pas besoin d'un accès aléatoire aux éléments (contrairement à un tableau, vous ne pouvez pas accéder à un élément à un index particulier dans une liste chaînée).
3. Vous voulez pouvoir insérer des éléments au milieu de la liste.
4. Vous avez besoin d'une insertion/suppression en temps constant (contrairement à un tableau, vous n'avez pas à décaler tous les autres éléments de la liste au préalable).

Ce sont quelques points que vous devriez considérer avant d'essayer d'implémenter une liste chaînée.

Maintenant que la théorie est terminée, il est temps d'en implémenter une. Nous allons le faire en utilisant Python, mais la majeure partie de ce que nous apprenons ici s'applique à n'importe quel langage que vous utilisez. Le plus important est de comprendre comment cela fonctionne.

## Comment utiliser les listes chaînées en Python

Voici une astuce lors de la création d'une liste chaînée. C'est quelque chose qui m'a aidé à bien mieux comprendre.

Il suffit de réaliser que chaque élément que vous ajouterez à la liste n'est qu'un nœud (semblable à un anneau dans une chaîne). Ce qui différencie la **head** (qui est le premier nœud de la liste), c'est que vous lui avez donné le titre de **head**, puis vous avez commencé à y ajouter d'autres nœuds.

Rappelez-vous qu'une liste chaînée est similaire à la façon dont une chaîne est couplée. 
Joe est ici avec quelques anneaux, et il va nous aider.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Joe-and-the-chain.png)

J'utiliserai ceci pour illustrer au fur et à mesure... vous pouvez donc réfléchir dans cette direction (ceci n'est pas un cours d'art – je répète, ceci n'est pas un cours d'art :) ).

Créons donc d'abord les nœuds :

```python
class Node:    
	def __init__(self,value):        
		self.value = value        
		self.next = None
```

C'est tout. Nous ajoutons la **`value`** car pour que n'importe quoi soit ajouté à la liste chaînée, il doit au moins avoir une valeur (par exemple, sauf dans des situations rares, vous n'ajoutez pas une chaîne vide à un tableau, n'est-ce pas ?).

Le **`next`** signifie qu'il est possible que nous voulions chaîner d'autres nœuds – je veux dire, c'est l'objectif principal d'une liste chaînée.

Ensuite, nous allons définir quelques fonctions de base :

```python
class LinkedList:
	def __init__(self,head=None):
		self.head = head    
		def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
```

La méthode `append()` vous permet d'ajouter un nouveau nœud à la liste. Explorons comment elle fonctionne.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/append.png)

Si j'ai deux valeurs – disons 1 et 2 – et que je veux les ajouter à la liste, la première chose est de les définir comme des nœuds individuels (c'est-à-dire, comme des anneaux d'une chaîne). Je peux le faire comme ceci :

```python
e1 = Node(1)
e2 = Node(2)
```

Je peux maintenant définir une liste chaînée puisque mes nœuds sont prêts. Une liste chaînée (comme les chaînes que nous voyons – a toujours une tête, n'est-ce pas ?), je peux donc définir ma liste chaînée avec une valeur de tête qui est simplement un autre nœud (anneau) :

```python
ll = LinkedList(e1)
```

Maintenant, d'après le code ci-dessus, **`e1`** est la tête de la liste chaînée, ce qui est juste une façon élégante de dire le point de départ de ma liste chaînée. Je peux y ajouter d'autres éléments, et comme chaque chaîne doit être connectée (c'est-à-dire l'une dans l'autre), je dois d'abord configurer le cas de base pour vérifier si la liste a une tête.

Ce qui fait une liste chaînée, c'est le fait qu'elle a un point de départ. Si ce n'est pas le cas, nous devons simplement définir le nouvel élément comme la tête. Mais si elle a déjà une tête, je dois parcourir toute la liste et vérifier si l'un des nœuds a un **`next`** qui est vide (c'est-à-dire **`None`**).

Encore une fois, une liste chaînée est comme une chaîne, n'est-ce pas ? Donc chaque nœud doit pointer vers un autre avec le pointeur **`next`**. Une fois qu'un nœud a un `next` qui est `none`, cela signifie simplement que c'est la fin de la liste. Je peux donc facilement ajouter le nouveau nœud à cette position.

Créons une méthode pour **supprimer** (delete) un nœud. Mais avant de le faire, réfléchissons-y un instant. Imaginez que vous avez une chaîne et que vous découvrez qu'un anneau est fragile. Que faites-vous ?

Vous trouvez d'abord l'anneau fragile, puis vous le retirez et vous connectez celui d'avant et celui d'après ensemble. Mais si l'anneau fragile est le premier, c'est facile – vous le retirez simplement et vous n'avez pas vraiment besoin de joindre quoi que ce soit. Le deuxième anneau devient automatiquement la tête de la chaîne. Essayez de visualiser cela.

Nous voulons faire la même chose ici. Nous trouvons donc d'abord l'anneau fragile – dans ce cas, ce sera la valeur que nous recherchons – puis nous prendrons celui d'avant et celui d'après et nous les joindrons ensemble :

```python
class LinkedList:    
	def __init(...)    
	def append(...)    
	  def delete(self, value):
        """Supprimer le premier nœud avec une valeur donnée."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None
```

Ce que nous faisons ici, c'est simplement parcourir chaque nœud pour voir si c'est la valeur que nous voulons supprimer. Mais au fur et à mesure que nous avançons dans la liste, nous devons garder une trace de la valeur précédente (nous devons toujours relier la liste). Nous faisons cela avec **`prev = current`** comme vous pouvez le voir ci-dessus ou ci-dessous :).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/delete-1.png)

Ainsi, lorsque le nœud a été trouvé, le **`prev`** qui contient le nœud précédent peut être facilement commuté (c'est-à-dire la valeur suivante) pour pointer vers un autre nœud – dans ce cas, les autres nœuds connectés au nœud que nous voulons supprimer. J'espère que cela a du sens :).

Travaillons sur l'**insertion d'un nœud** à une position particulière. Nous utiliserons notre analogie de la chaîne pour mieux comprendre cela.

Lorsque vous tenez une chaîne et que vous voulez augmenter sa longueur, vous avez trois options. Vous pouvez :

1. Ajouter un maillon (élément) au début de la chaîne (cela devrait être assez simple, n'est-ce pas ?)
2. L'ajouter à la fin de la chaîne (un peu comme le point 1)
3. Ou vous pouvez l'ajouter à n'importe quel point au milieu (un peu plus délicat)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/insert3.png)

Une chose que vous devez garder à l'esprit est que, quel que soit l'endroit où vous décidez de l'ajouter, vous devez y rattacher les autres nœuds. Cela n'est possible que si vous gardez une trace des autres nœuds avec une boucle.

Voyons cela en action :

```python
	class LinkedList:   
	def __init(...)    
	def append(...) 
    def delete(...)
    def insert(self, new_element, position):
        """Insérer un nouveau nœud à la position donnée.
        Supposons que la première position soit "1".
        Insérer à la position 3 signifie entre
        le 2ème et le 3ème élément."""
        count=1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count+1 == position:
                new_element.next =current.next
                current.next = new_element
                return
            else:
                count+=1
                current = current.next
            # break

        pass
```

On nous donne une position pour insérer le nœud dans le code ci-dessus. Si la position est un, cela signifie qu'il s'agira de la racine. Comme nous n'en sommes pas sûrs, nous pouvons initialiser une boucle et un compteur pour suivre la boucle.

Si la position où nous devons insérer est un (c'est-à-dire la racine), stockez simplement la racine actuelle dans une variable temporaire, créez une nouvelle racine, puis ajoutez la racine précédente (c'est-à-dire toute la chaîne) à cette nouvelle racine.

Si la position n'est pas un, continuez à parcourir la chaîne jusqu'à ce que vous trouviez la position.

Enfin pour cet article, travaillons sur l'affichage des valeurs de notre liste chaînée dans le format que vous souhaitez – par exemple, en les imprimant ou en les ajoutant à une collection de listes. Je vais simplement imprimer les valeurs.

C'est assez simple, similaire à une chaîne physique : vous regardez simplement partout où il y a un nœud et récupérez la valeur, puis passez au nœud suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/print.png)

```python
class LinkedList:   
	def __init(...)    
	def append(...) 
    def insert(...)
	def delete(...)    
	def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
```

C'est tout sur les listes chaînées pour le moment ! Nous travaillerons sur la résolution de quelques questions sur les listes chaînées plus tard.

## Conclusion

Dans cet article, j'ai expliqué :

* Comment fonctionne une liste chaînée
* Les avantages et les inconvénients d'une liste chaînée
* Comment implémenter une liste chaînée avec Python

Vous pouvez trouver le code de [cet article ici](https://github.com/fakoredeDamilola/articles/blob/master/code/linkedList.py). Merci de m'avoir lu.