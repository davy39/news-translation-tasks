---
title: Tutoriel Python Liste Vide – Comment Créer une Liste Vide en Python
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-06-18T14:31:55.000Z'
originalURL: https://freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Empty-list.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: Tutoriel Python Liste Vide – Comment Créer une Liste Vide en Python
seo_desc: "If you want to learn how to create an empty list in Python efficiently,\
  \ then this article is for you. \nYou will learn:\n\nHow to create an empty list\
  \ using square brackets [].\nHow to create an empty list using list().\nTheir use\
  \ cases. \nHow efficient th..."
---

Si vous souhaitez apprendre à créer une liste vide en Python efficacement, alors cet article est fait pour vous. 

**Vous apprendrez :**

* Comment créer une liste vide en utilisant des crochets `[]`.
* Comment créer une liste vide en utilisant `list()`.
* Leurs cas d'utilisation. 
* Leur efficacité (l'un est plus rapide que l'autre !). Nous utiliserons le module `timeit` pour les comparer.

**Commençons ! ✨**

## 💡 Utilisation des Crochets

Vous pouvez créer une liste vide avec une paire de crochets vides, comme ceci :  

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-131.png)

**💡 Astuce :** Nous assignons la liste vide à une variable pour l'utiliser plus tard dans notre programme. 

Par exemple :

```
num = []
```

La liste vide aura une longueur de `0`, comme vous pouvez le voir ici :

```
>>> num = []
>>> len(num)
0
```

Les listes vides sont des valeurs **falsy**, ce qui signifie qu'elles évaluent à `False` dans un contexte booléen :

```python
>>> num = []
>>> bool(num)
False
```

### Ajouter des Éléments à une Liste Vide

Vous pouvez ajouter des éléments à une liste vide en utilisant les méthodes `append()` et `insert()` :

* `append()` ajoute l'élément à la fin de la liste.
* `insert()` ajoute l'élément à l'index particulier de la liste que vous choisissez.

Puisque les listes peuvent être des valeurs truthy ou falsy selon qu'elles sont vides ou non lorsqu'elles sont évaluées, vous pouvez les utiliser dans des conditionnelles comme ceci :

```python
if num:
	print("Cette liste n'est pas vide")
else:
	print("Cette liste est vide")
```

La sortie de ce code est :

```python
Cette liste est vide
```

Parce que la liste était vide, donc elle évalue à False.

En général :

* Si la liste n'est pas vide, elle évalue à `True`, donc la clause if est exécutée.
* Si la liste est vide, elle évalue à `False`, donc la clause else est exécutée. 

### Exemple :

Dans l'exemple ci-dessous, nous créons une liste vide et l'assignons à la variable `num`. Ensuite, en utilisant une boucle for, nous ajoutons une séquence d'éléments (entiers) à la liste qui était initialement vide :

```python
>>> num = []
>>> for i in range(3, 15, 2):
	num.append(i)
```

Nous vérifions la valeur de la variable pour voir si les éléments ont été ajoutés avec succès et confirmons que la liste n'est plus vide :  

```python
>>> num
[3, 5, 7, 9, 11, 13]
```

**💡 Astuce :** Nous utilisons couramment `append()` pour ajouter le premier élément à une liste vide, mais vous pouvez également ajouter cet élément en appelant la méthode `insert()` avec l'index `0` :

```python
>>> num = []
>>> num.insert(0, 1.5) # ajoute le float 1.5 à l'index 0
>>> num
[1.5]
```

## 💠 Utilisation du Constructeur list()

Alternativement, vous pouvez créer une liste vide avec le constructeur de type `list()`, qui crée un nouvel objet liste. 

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#list) :

> Si aucun argument n'est donné, le constructeur crée une nouvelle liste vide, `[]`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-132.png)

💡 **Astuce :** Cela crée un nouvel objet liste en mémoire et puisque nous n'avons pas passé d'arguments à `list()`, une liste vide sera créée.

Par exemple :

```
num = list()
```

Cette liste vide aura une longueur de `0`, comme vous pouvez le voir ici :

```
>>> num = list()
>>> len(num)
0
```

Et c'est une valeur **falsy** lorsqu'elle est vide (elle évalue à `False` dans un contexte booléen) :

```python
>>> num = list()
>>> bool(num)
False
```

### Exemple :

Ceci est une liste entièrement fonctionnelle, donc nous pouvons ajouter des éléments à celle-ci :

```python
>>> num = list()
>>> for i in range(3, 15, 2):
	num.append(i)
```

Et le résultat sera une liste non vide, comme vous pouvez le voir ici :

```python
>>> num
[3, 5, 7, 9, 11, 13]
```

## 💡 Cas d'Utilisation

* Nous utilisons typiquement `list()` pour créer des listes à partir d'itérables existants tels que des chaînes de caractères, des dictionnaires ou des tuples. 
* Vous verrez couramment des crochets `[]` utilisés pour créer des listes vides en Python car cette syntaxe est plus concise et plus rapide. 

## 💠 Efficacité

Attendez ! Je viens de vous dire que `[]` est plus rapide que `list()`...

**Mais combien plus rapide ?** 

Vérifions leur efficacité temporelle en utilisant le module [**timeit**](https://docs.python.org/3/library/timeit.html#module-timeit).

Pour utiliser ce module dans votre programme Python, vous devez l'importer :

```python
>>> import timeit
```

Plus précisément, nous utiliserons la [fonction timeit](https://docs.python.org/3/library/timeit.html#timeit.timeit) de ce module, que vous pouvez appeler avec cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-129.png)

💡 **Astuce :** Le code est répété plusieurs fois pour réduire les différences de temps qui peuvent survenir en raison de facteurs externes tels que d'autres processus qui pourraient être en cours d'exécution à ce moment précis. Cela rend les résultats plus fiables à des fins de comparaison.

**🚦 À vos marques... prêts... partez !** Voici le code et la sortie :

Tout d'abord, nous importons le module.

```python
>>> import timeit
```

Ensuite, nous commençons à tester chaque syntaxe.

### Test de `[]` :

```python
>>> timeit.timeit('[]', number=10**4)
0.0008467000000109692
```

### Test de `list()` :

```python
>>> timeit.timeit('list()', number=10**4)
0.002867799999989984
```

**💡 Astuce :** Remarquez que le code que vous souhaitez chronométrer doit être entouré de guillemets simples `''` ou de guillemets doubles `""`. Le temps retourné par la fonction `timeit` est exprimé en secondes.

Comparez ces résultats :

* `[]` : `0.0008467000000109692` 
* `list()` : `0.002867799999989984`

Vous pouvez voir que `[]` est beaucoup plus rapide que `list()`. Il y avait une différence d'environ `0.002` secondes dans ce test :

```python
>>> 0.002867799999989984 - 0.0008467000000109692
0.0020210999999790147
```

**Je suis sûr que vous devez vous poser cette question maintenant :** Pourquoi `list()` est-il moins efficace que `[]` s'ils font exactement la même chose ?

Eh bien... `list()` est plus lent car il nécessite de rechercher le nom de la fonction, de l'appeler, puis de créer l'objet liste en mémoire. En revanche, `[]` est comme un "raccourci" qui ne nécessite pas autant d'étapes intermédiaires pour créer la liste en mémoire. 

Cette différence de temps n'affectera pas beaucoup les performances de votre programme, mais il est bon de savoir lequel est le plus efficace et comment ils fonctionnent en coulisses.

## 💡 En Résumé

Vous pouvez créer une liste vide en utilisant une paire de crochets vides `[]` ou le constructeur de type `list()`, une fonction intégrée qui crée une liste vide lorsque aucun argument n'est passé. 

Les crochets `[]` sont couramment utilisés en Python pour créer des listes vides car c'est plus rapide et plus concis.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez créer des listes vides dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐

Si vous souhaitez approfondir les listes, vous pourriez aimer lire :

* [Python List Append – Comment Ajouter un Élément à un Tableau, Expliqué avec des Exemples](https://www.freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples/)
* [La Méthode Python Sort List Array – Ascendant et Descendant Expliqués avec des Exemples](https://www.freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples/)
* [Python List Append VS Python List Extend – La Différence Expliquée avec des Exemples de Méthodes de Tableau](https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/)