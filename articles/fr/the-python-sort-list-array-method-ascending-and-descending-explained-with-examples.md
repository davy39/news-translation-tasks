---
title: La Méthode Python Sort List Array – Ascendant et Descendant Expliqués avec
  des Exemples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-04-12T12:57:47.000Z'
originalURL: https://freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/sort-method.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: La Méthode Python Sort List Array – Ascendant et Descendant Expliqués avec
  des Exemples
seo_desc: 'If you want to learn how to work with the sort() method in your Python
  projects, then this article is for you. This method is very powerful and you can
  customize it to fit your needs, so let''s see how it works in detail.

  You will learn:


  How to use t...'
---

Si vous souhaitez apprendre à travailler avec la méthode `sort()` dans vos projets Python, alors cet article est fait pour vous. Cette méthode est très puissante et vous pouvez la personnaliser pour répondre à vos besoins, alors voyons comment elle fonctionne en détail.

**Vous apprendrez :**

* Comment utiliser cette méthode et personnaliser sa fonctionnalité.
* Quand l'utiliser et quand ne pas l'utiliser.
* Comment l'appeler en passant différentes combinaisons d'arguments.
* Comment trier une liste dans l'ordre ascendant et descendant.
* Comment comparer les éléments d'une liste en fonction de valeurs intermédiaires.
* Comment vous pouvez passer des fonctions lambda à cette méthode.
* Comment cette méthode se compare à la fonction `sorted()`.
* Pourquoi la méthode `sort()` effectue un tri stable.
* Comment le processus de mutation fonctionne en coulisses.

Êtes-vous prêt ? Commençons ! ⭐

## 🔹 Objectif et Cas d'Utilisation

Avec la méthode `sort()`, vous pouvez trier une liste soit :

* Dans l'Ordre Ascendant
* Dans l'Ordre Descendant

Cette méthode est utilisée pour trier une liste en place, ce qui signifie qu'elle la **modifie** ou la modifie directement sans créer de copies supplémentaires, alors souvenez-vous :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-113.png)

Vous en apprendrez plus sur la mutation dans cet article (je vous le promets !), mais pour l'instant, il est très important que vous sachiez que la méthode `sort()` modifie la liste, donc sa version originale est perdue.

À cause de cela, vous ne devriez utiliser cette méthode que si :

* Vous voulez modifier (trier) la liste de manière permanente.
* Vous n'avez pas besoin de conserver la version originale de la liste.

Si cela correspond à vos besoins, alors la méthode `.sort()` est exactement ce que vous cherchez.

## 🔸 Syntaxe et Arguments

Voyons comment vous pouvez appeler `.sort()` pour tirer parti de toute sa puissance.

Voici l'appel le plus basique (sans arguments) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-41.png)

Si vous ne passez aucun argument, par défaut :

* La liste sera triée dans l'ordre ascendant.
* Les éléments de la liste seront comparés directement en utilisant leurs valeurs avec l'opérateur `<`.

Par exemple :

```python
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort()
>>> b
[2, 3, 3, 6, 7, 8, 9] # Trié !
```

### Arguments Personnalisés

Pour personnaliser le fonctionnement de la méthode `sort()`, vous pouvez passer deux arguments optionnels :

* Key
* Reverse

Voyons comment ils changent le comportement de cette méthode. Voici un appel de méthode avec ces deux arguments :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-42.png)

Avant d'expliquer comment ils fonctionnent, j'aimerais expliquer quelque chose que vous avez probablement remarqué dans le diagramme ci-dessus – dans l'appel de la méthode, les noms des paramètres doivent être inclus avant leurs valeurs correspondantes, comme ceci :

* `key=<f>`
* `reverse=<value>`

C'est parce qu'ils sont des [**arguments uniquement par mot-clé**](https://docs.python.org/3/glossary.html#keyword-only-parameter). Si vous passez une valeur personnalisée pour eux, leurs **noms** doivent être spécifiés dans l'appel de la méthode, suivis d'un signe égal `=` et de leurs valeurs correspondantes, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-46.png)

Sinon, si vous essayez de passer les arguments directement comme nous le faisons normalement pour les paramètres positionnels, vous verrez cette erreur parce que la fonction ne saura pas quel argument correspond à quel paramètre :

```python
TypeError: sort() takes no positional arguments
```

### Reverse

Maintenant que vous savez ce que sont les arguments uniquement par mot-clé, commençons par `reverse`.

La valeur de `reverse` peut être soit `True` soit `False` :

* `False` signifie que la liste sera triée dans l'ordre ascendant.
* `True` signifie que la liste sera triée dans l'ordre descendant (inverse).

**💡 Astuce :** Par défaut, sa valeur est `False` – si vous ne passez aucun argument pour ce paramètre, la liste est triée dans l'ordre ascendant.

Voici quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-123.png)
_Par défaut, reverse est False_

```python
# Liste d'entiers
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort()
>>> b
[2, 3, 3, 6, 7, 8, 9]

# Liste de chaînes de caractères
>>> c = ["A", "Z", "D", "T", "U"]
>>> c.sort()
>>> c
['A', 'D', 'T', 'U', 'Z']

```

💡 **Astuce :** Si les éléments de la liste sont des chaînes de caractères, ils sont triés par ordre alphabétique.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-117.png)
_Pour spécifier que reverse est True, afin que la liste doive être triée dans l'ordre descendant (inverse)._

```python
# Liste d'entiers
>>> b = [6, 3, 8, 2, 7, 3, 9]
>>> b.sort(reverse=True)
>>> b
[9, 8, 7, 6, 3, 3, 2]

# Liste de chaînes de caractères
>>> c = ["A", "Z", "D", "T", "U"]
>>> c.sort(reverse=True)
>>> c
['Z', 'U', 'T', 'D', 'A']
```

💡 **Astuce :** Remarquez comment la liste est triée dans l'ordre descendant si `reverse` est `True`.

### Key

Maintenant que vous savez comment travailler avec le paramètre `reverse`, voyons le paramètre `key`.

Ce paramètre est un peu plus détaillé car il détermine comment les éléments de la liste sont comparés pendant le processus de tri.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-120.png)
_Syntaxe de Base_

La valeur de `key` est soit :

* `None`, ce qui signifie que les éléments de la liste seront comparés directement. Par exemple, dans une liste d'entiers, les entiers eux-mêmes peuvent être utilisés pour la comparaison.
* **Une** **fonction** d'un argument qui génère une valeur intermédiaire pour chaque élément. Cette valeur intermédiaire est calculée une seule fois et elle est utilisée pour faire les comparaisons pendant tout le processus de tri. Nous utilisons cela lorsque nous ne voulons pas comparer les éléments directement, par exemple, lorsque nous voulons comparer des chaînes de caractères en fonction de leur longueur (la valeur intermédiaire).

💡 **Astuce :** Par défaut, la valeur de `key` est `None`, donc les éléments sont comparés directement.

**Par exemple :**

Disons que nous voulons trier une liste de chaînes de caractères en fonction de leur longueur, de la chaîne la plus courte à la plus longue. Nous pouvons passer la fonction `len` comme valeur de `key`, comme ceci :

```python
>>> d = ["aaa", "bb", "c"]
>>> d.sort(key=len)
>>> d
['c', 'bb', 'aaa']
```

💡 **Astuce :** Remarquez que nous passons uniquement le nom de la fonction (`len`) sans parenthèses car nous n'appelons pas la fonction. C'est très important.

Remarquez la différence entre comparer les éléments directement et comparer leur longueur (voir ci-dessous). Utiliser la valeur par défaut de `key` (`None`) aurait trié les chaînes de caractères par ordre alphabétique (à gauche), mais maintenant nous les trions en fonction de leur longueur (à droite) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-49.png)

Que se passe-t-il en coulisses ? Chaque élément est passé comme argument à la fonction `len()`, et la valeur retournée par cet appel de fonction est utilisée pour effectuer les comparaisons pendant le processus de tri :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-122.png)

Cela donne une liste avec un critère de tri différent : la longueur.

**Voici un autre exemple :**

Un autre exemple intéressant est le tri d'une liste de chaînes de caractères comme si elles étaient toutes écrites en lettres minuscules (par exemple, en rendant "Aa" équivalent à "aa").

Selon l'ordre lexicographique, les lettres majuscules viennent avant les lettres minuscules :

```python
>>> "E" < "e"
True
```

Ainsi, la chaîne `"Emma"` viendrait avant `"emily"` dans une liste triée, même si leurs versions en minuscules seraient dans l'ordre inverse :

```
>>> "Emma" < "emily"
True
>>> "emma" < "emily"
False
```

Pour éviter de distinguer entre les lettres majuscules et minuscules, nous pouvons passer la fonction `str.lower` comme `key`. Cela générera une version en minuscules des chaînes de caractères qui sera utilisée pour les comparaisons :

```python
>>> e = ["Emma", "emily", "Amy", "Jason"]
>>> e.sort(key=str.lower)
>>> e
['Amy', 'emily', 'Emma', 'Jason']
```

Remarquez que maintenant, `"emily"` vient avant `"Emma"` dans la liste triée, ce qui est exactement ce que nous voulions.

💡 **Astuce :** si nous avions utilisé le processus de tri par défaut, toutes les chaînes de caractères commençant par une lettre majuscule seraient venues avant toutes les chaînes de caractères commençant par une lettre minuscule :

```python
>>> e = ["Emma", "emily", "Amy", "Jason"]
>>> e.sort()
>>> e
['Amy', 'Emma', 'Jason', 'emily']
```

**Voici un exemple utilisant la Programmation Orientée Objet (POO) :**

Si nous avons cette classe Python très simple :

```python
>>> class Client:
	def __init__(self, age):
		self.age = age
```

Et nous créons quatre instances :

```python
>>> client1 = Client(67)
>>> client2 = Client(23)
>>> client3 = Client(13)
>>> client4 = Client(35)
```

Nous pouvons créer une liste qui les référence :

```python
>>> clients = [client1, client2, client3, client4]
```

Ensuite, si nous définissons une fonction pour obtenir l'`age` de ces instances :

```python
>>> def get_age(client):
	return client.age
```

Nous pouvons trier la liste en fonction de leur âge en passant la fonction `get_age` comme argument :

```python
>>> clients.sort(key=get_age)
```

Voici la version finale triée de la liste. Nous utilisons une boucle for pour imprimer l'âge des instances dans l'ordre où elles apparaissent dans la liste :

```python
>>> for client in clients:
	print(client.age)

	
13
23
35
67
```

Exactement ce que nous voulions – maintenant la liste est triée dans l'ordre ascendant en fonction de l'âge des instances.

💡 **Astuce :** Au lieu de définir une fonction `get_age`, nous aurions pu utiliser une fonction lambda pour obtenir l'âge de chaque instance, comme ceci :

```python
>>> clients.sort(key=lambda x: x.age)
```

Les **fonctions lambda** sont petites et simples, des fonctions anonymes, ce qui signifie qu'elles n'ont pas de nom. Elles sont très utiles pour ces scénarios lorsque nous voulons les utiliser uniquement dans des endroits particuliers pendant une très courte période.

Voici la structure de base de la fonction lambda que nous utilisons pour trier la liste :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-90.png)
_Structure de Base d'une Fonction Lambda_

### Passer les Deux Arguments

Super ! Maintenant vous savez personnaliser la fonctionnalité de la méthode `sort()`. Mais vous pouvez emmener vos compétences à un tout nouveau niveau en combinant l'effet de `key` et `reverse` dans le même appel de méthode :

```python
>>> f = ["A", "a", "B", "b", "C", "c"]
>>> f.sort(key=str.lower, reverse=True)
>>> f
['C', 'c', 'B', 'b', 'A', 'a']
```

Voici les différentes combinaisons des arguments et leur effet :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-124.png)

### L'Ordre des Arguments Uniquement par Mot-Clé N'a Pas d'Importance

Puisque nous spécifions les noms des arguments, nous savons déjà quelle valeur correspond à quel paramètre, donc nous pouvons inclure soit `key` soit `reverse` en premier dans la liste et l'effet sera exactement le même.

Ainsi, cet appel de méthode :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-53.png)

Est équivalent à :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-54.png)

Voici un exemple :

```python
>>> a = ["Zz", "c", "y", "o", "F"]
>>> a.sort(key=str.lower, reverse=True)
>>> a
['Zz', 'y', 'o', 'F', 'c']
```

Si nous changeons l'ordre des arguments, nous obtenons exactement le même résultat :

```python
>>> a = ["Zz", "c", "y", "o", "F"]
>>> a.sort(reverse=True, key=str.lower)
>>> a
['Zz', 'y', 'o', 'F', 'c']
```

## 🔹 Valeur de Retour

Maintenant, parlons un peu de la valeur de retour de cette méthode. La méthode `sort()` retourne `None` – elle ne retourne **pas** une version triée de la liste, comme nous pourrions nous y attendre intuitivement.

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#list.sort) :

> Pour rappeler aux utilisateurs qu'elle opère par effet de bord, elle ne retourne pas la séquence triée.

En gros, cela est utilisé pour nous rappeler que nous modifions la liste originale en mémoire, et non en générant une nouvelle copie de la liste.

Voici un exemple de la valeur de retour de `sort()` :

```python
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]

# Assigner la valeur de retour à cette variable :
>>> val = nums.sort()

# Vérifier la valeur de retour :
>>> print(val)
None
```

Vous voyez ? `None` a été retourné par l'appel de la méthode.

**💡 Astuce :** Il est très important de ne pas confondre la méthode `sort()` avec la fonction `sorted()`, qui est une fonction qui fonctionne de manière très similaire, mais qui **ne modifie pas** la liste originale. Au lieu de cela, `sorted()` génère et retourne une nouvelle copie de la liste, déjà triée.

Voici un exemple que nous pouvons utiliser pour les comparer :

```python
# La méthode sort() retourne None
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
>>> val = nums.sort()
>>> print(val)
None
```

```python
# sorted() retourne une nouvelle copie triée de la liste originale
>>> nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
>>> val = sorted(nums)
>>> val
[2.4, 2.6, 3.5, 6.5, 7.3, 7.4]

# Mais elle ne modifie pas la liste originale
>>> nums
[6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
```

C'est très important car leur effet est très différent. Utiliser la méthode `sort()` lorsque vous aviez l'intention d'utiliser `sorted()` peut introduire des bugs sérieux dans votre programme car vous ne réaliserez peut-être pas que la liste est en train d'être modifiée.

## 🔸 La Méthode sort() Effectue un Tri Stable

Maintenant, parlons un peu des caractéristiques de l'algorithme de tri utilisé par `sort()`.

Cette méthode effectue un tri stable car elle fonctionne avec une implémentation de [TimSort](https://en.wikipedia.org/wiki/Timsort), un algorithme de tri très efficace et stable.

Selon la [Documentation Python](https://docs.python.org/3/library/stdtypes.html#list.sort) :

> Un tri est stable s'il garantit **de ne pas changer l'ordre relatif des éléments qui sont égaux** – cela est utile pour trier en plusieurs passes (par exemple, trier par département, puis par grade de salaire).

Cela signifie que si deux éléments ont la même valeur ou valeur intermédiaire (clé), ils sont garantis de rester dans le même ordre relatif l'un par rapport à l'autre.

Voyons ce que je veux dire. Veuillez regarder cet exemple pendant quelques instants :

```python
>>> d = ["BB", "AA", "CC", "A", "B", "AAA", "BBB"]
>>> d.sort(key=len)
>>> d
['A', 'B', 'BB', 'AA', 'CC', 'AAA', 'BBB']
```

Nous comparons les éléments en fonction de leur **longueur** car nous avons passé la fonction `len` comme argument pour `key`.

Nous pouvons voir qu'il y a trois éléments de longueur 2 : `"BB"`, `"AA"`, et `"CC"` dans cet ordre.

Maintenant, remarquez que ces trois éléments sont dans le même ordre relatif dans la liste triée finale :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-92.png)

C'est parce que l'algorithme est garanti d'être stable et que les trois avaient la même valeur intermédiaire (clé) pendant le processus de tri (leur longueur était 2, donc leur clé était 2).

💡 **Astuce :** La même chose s'est produite avec `"A"` et `"B"` (longueur 1) et `"AAA"` et `"BBB"` (longueur 3), leur ordre original relatif l'un par rapport à l'autre a été préservé.

Maintenant vous savez comment fonctionne la méthode `sort()`, alors plongeons dans la mutation et comment elle peut affecter votre programme.

## 🔹 Mutation et Risques

Comme promis, voyons comment le processus de mutation fonctionne en coulisses :

Lorsque vous définissez une liste en Python, comme ceci :

```python
a = [1, 2, 3, 4]
```

Vous créez un objet à un emplacement mémoire spécifique. Cet emplacement est appelé l'"adresse mémoire" de l'objet, représentée par un entier unique appelé **id**. 

Vous pouvez penser à un id comme une "étiquette" utilisée pour identifier un endroit spécifique en mémoire :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-40.png)

Vous pouvez accéder à l'id d'une liste en utilisant la fonction `id()`, en passant la liste comme argument :

```python
>>> a = [1, 2, 3, 4]
>>> id(a)
60501512
```

Lorsque vous **modifiez** la liste, vous la changez directement en mémoire. Vous pourriez demander, pourquoi est-ce si risqué ?

C'est risqué car cela affecte chaque ligne de code qui utilise la liste après la mutation, donc vous pourriez écrire du code pour travailler avec une liste qui est complètement différente de la liste réelle qui existe en mémoire après la mutation.

C'est pourquoi vous devez être très prudent avec les méthodes qui causent une mutation.

En particulier, la méthode `sort()` **modifie** la liste. Voici un exemple de son effet :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-94.png)

Voici un exemple :

```python
# Définir une liste
>>> a = [7, 3, 5, 1]

# Vérifier son id
>>> id(a)
67091624

# Trier la liste en utilisant .sort()
>>> a.sort()

# Vérifier son id (il est le même, donc la liste est le même objet en mémoire)
>>> id(a)
67091624

# Maintenant la liste est triée. Elle a été modifiée !
>>> a
[1, 3, 5, 7]
```

La liste a été modifiée après l'appel de `.sort()`.

Chaque ligne de code qui travaille avec la liste `a` après que la mutation s'est produite utilisera la nouvelle version triée de la liste. Si ce n'était pas ce que vous aviez l'intention de faire, vous ne réaliserez peut-être pas que d'autres parties de votre programme travaillent avec la nouvelle version de la liste.

Voici un autre exemple des risques de mutation au sein d'une fonction :

```python
# Liste
>>> a = [7, 3, 5, 1]

# Fonction qui imprime les éléments de la liste dans l'ordre ascendant.
>>> def print_sorted(x):
	x.sort()
	for elem in x:
		print(elem)

# Appeler la fonction en passant 'a' comme argument
>>> print_sorted(a)
1
3
5
7

# Oups ! La liste originale a été modifiée.
>>> a
[1, 3, 5, 7]
```

La liste `a` qui a été passée comme argument a été modifiée, même si ce n'était pas ce que vous aviez l'intention de faire lorsque vous avez initialement écrit la fonction.

**💡 Astuce :** Si une fonction modifie un argument, cela devrait être clairement indiqué pour éviter d'introduire des bugs dans d'autres parties de votre programme.

## 🔸 Résumé de la Méthode sort()

* La méthode `sort()` vous permet de trier une liste dans l'ordre ascendant ou descendant.
* Elle prend deux arguments uniquement par mot-clé : `key` et `reverse`.
* `reverse` détermine si la liste est triée dans l'ordre ascendant ou descendant.
* `key` est une fonction qui génère une valeur intermédiaire pour chaque élément, et cette valeur est utilisée pour faire les comparaisons pendant le processus de tri.
* La méthode `sort()` modifie la liste, provoquant des changements permanents. Vous devez être très prudent et ne l'utiliser que si vous n'avez pas besoin de la version originale de la liste.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant vous pouvez travailler avec la méthode `sort()` dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️