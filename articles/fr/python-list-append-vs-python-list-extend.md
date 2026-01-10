---
title: Python List Append VS Python List Extend – Les différences expliquées avec
  des exemples de méthodes de tableau
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-03-22T23:27:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-vs-python-list-extend
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Image
seo_title: Python List Append VS Python List Extend – Les différences expliquées avec
  des exemples de méthodes de tableau
---

Append-vs-Extend-1.png
tags:
- name: Python
  slug: python
- name: Tutoriel
  slug: tutoriel
seo_title: null
seo_desc: "\U0001F539 Bienvenue\nSi vous voulez apprendre à travailler avec .append() et\
  \ .extend() et comprendre leurs différences, alors vous êtes au bon endroit.\
  \ Ce sont des méthodes de liste puissantes que vous utiliserez définitivement dans vos projets Python.\n\
  \ Dans cet article, vous allez apprendre :\n\
  * Comment et quand utiliser la méthode .append().\n  * Comment et quand utiliser la méthode .extend(). \n  * Leurs principales différences. \n\
  Commençons. F4A0"
---

## F4A0 Bienvenue

Si vous voulez apprendre à travailler avec `.append()` et `.extend()` et comprendre leurs différences, alors vous êtes au bon endroit. Ce sont des méthodes de liste puissantes que vous utiliserez définitivement dans vos projets Python.

Dans cet article, vous allez apprendre :

* Comment et quand utiliser la méthode `.append()`.
* Comment et quand utiliser la méthode `.extend()`. 
* Leurs principales différences. 

Commençons. ✨

## F4A0 Append

Voyons comment la méthode `.append()` fonctionne en coulisses.

### Cas d'utilisation

Vous devriez utiliser cette méthode lorsque vous voulez **ajouter un seul élément à la fin** d'une liste.

**F4A1 Conseils :** Vous pouvez ajouter des éléments de n'importe quel type de données puisque les listes peuvent avoir des éléments de différents types de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-105.png)

### Syntaxe et arguments

Pour appeler la méthode `.append()`, vous devrez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-104.png)

**De gauche à droite :**

* La liste qui sera modifiée. Il s'agit généralement d'une variable qui référence une liste. 
* Un point, suivi du nom de la méthode `.append()`. 
* Entre parenthèses, l'élément qui sera ajouté à la fin de la liste. 

F4A1 **Conseils :** Le point est très important. Cela s'appelle la "notation par point". Le point signifie essentiellement "appeler cette méthode sur cette liste particulière", donc l'effet de la méthode sera appliqué à la liste qui se trouve avant le point. 

### Exemples

Voici un exemple de l'utilisation de `.append()` :

```python
# Définir la liste
>>> nums = [1, 2, 3, 4]

# Ajouter l'entier 5 à la fin de la liste existante
>>> nums.append(5)

# Voir la valeur mise à jour de la liste
>>> nums
[1, 2, 3, 4, 5]
```

F4A1 **Conseils :** Lorsque vous utilisez `.append()`, la liste originale est modifiée. La méthode ne crée pas de copie de la liste – elle modifie la liste originale en mémoire. 

Faisons semblant que nous menons une recherche et que nous voulons analyser les données collectées en utilisant Python. Nous devons ajouter une nouvelle mesure à la liste existante de valeurs. 

Comment faisons-nous cela ? Nous utilisons la méthode `.append()` ! 

Vous pouvez le voir ici :

```python
# Liste existante
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Ajouter le nombre décimal à la fin de la liste existante
>>> nums.append(7.34)

# Voir la valeur mise à jour de la liste
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 7.34]
```

### Équivalent à...

Si vous êtes familier avec le découpage de chaînes, de listes ou de tuples, ce que `.append()` fait réellement en coulisses est équivalent à :

```python
a[len(a):] = [x]
```

Avec cet exemple, vous pouvez voir qu'ils sont équivalents. 

En utilisant `.append()` :

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums.append(4.52)
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 4.52]
```

En utilisant le découpage de liste :

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums[len(nums):] = [4.52]
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 4.52]
```

### Ajout d'une séquence

Maintenant, que pensez-vous de cet exemple ? Que pensez-vous qu'il sera affiché ?

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> nums.append([5.67, 7.67, 3.44])
>>> nums
# SORTIE ?
```

Êtes-vous prêt ? Voici ce qui sera affiché :

```python
[5.6, 7.44, 6.75, 4.56, 2.3, [5.67, 7.67, 3.44]]
```

Vous vous demandez peut-être pourquoi la liste complète a été ajoutée en tant qu'élément unique ? C'est parce que la méthode `.append()` ajoute l'élément entier à la fin de la liste. Si l'élément est une séquence telle qu'une liste, un dictionnaire ou un tuple, la séquence entière sera ajoutée en tant qu'élément unique de la liste existante.

Voici un autre exemple (ci-dessous). Dans ce cas, l'élément est un tuple et il est ajouté en tant qu'élément unique de la liste, et non en tant qu'éléments individuels :

```python
>>> names = ["Lulu", "Nora", "Gino", "Bryan"]
>>> names.append(("Emily", "John"))
>>> names
['Lulu', 'Nora', 'Gino', 'Bryan', ('Emily', 'John')]
```

## F4A0 Extend

Maintenant, plongeons dans la fonctionnalité de la méthode `.extend()`. 

### Cas d'utilisation

Vous devriez utiliser cette méthode si vous devez **ajouter plusieurs éléments à une liste en tant qu'éléments individuels**. 

Permettez-moi d'illustrer l'importance de cette méthode avec un ami familier que vous venez d'apprendre : la méthode `.append()`. Sur la base de ce que vous avez appris jusqu'à présent, si nous voulions ajouter plusieurs éléments **individuels** à une liste en utilisant `.append()`, nous devrions utiliser `.append()` plusieurs fois, comme ceci :

```python
# Liste que nous voulons modifier
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Ajout des éléments
>>> nums.append(2.3)
>>> nums.append(9.6)
>>> nums.append(4.564)
>>> nums.append(7.56)

# Liste mise à jour
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

Je suis sûr que vous pensez probablement que cela ne serait pas très efficace, n'est-ce pas ? Et si je dois ajouter des milliers ou des millions de valeurs ? Je ne peux pas écrire des milliers ou des millions de lignes pour cette tâche simple. Cela prendrait une éternité !

Alors voyons une alternative. Nous pouvons stocker les valeurs que nous voulons ajouter dans une liste séparée et ensuite utiliser une boucle for pour appeler `.append()` autant de fois que nécessaire :

```python
# Liste que nous voulons modifier
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]

# Valeurs que nous voulons ajouter
>>> new_values = [2.3, 9.6, 4.564, 7.56]

# Boucle for qui va ajouter la valeur
>>> for num in new_values:
	nums.append(num)

# Valeur mise à jour de la liste
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

C'est plus efficace, n'est-ce pas ? Nous n'écrivons que quelques lignes. Mais il existe une méthode encore plus efficace, lisible et compacte pour atteindre le même objectif : `.extend()` !

```python
>>> nums = [5.6, 7.44, 6.75, 4.56, 2.3]
>>> new_values = [2.3, 9.6, 4.564, 7.56]

# C'est là que la magie opère ! Plus de boucles for
>>> nums.extend(new_values)

# La liste a été mise à jour avec des valeurs individuelles
>>> nums
[5.6, 7.44, 6.75, 4.56, 2.3, 2.3, 9.6, 4.564, 7.56]
```

Voyons comment cette méthode fonctionne en coulisses. 

### Syntaxe et arguments

Pour appeler la méthode `.extend()`, vous devrez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-110.png)

**De gauche à droite :**

* La liste qui sera modifiée. Il s'agit généralement d'une variable qui fait référence à la liste.
* Un point `.` (Jusqu'à présent, tout est exactement le même qu'avant).
* Le nom de la méthode `extend`. (Maintenant, les choses commencent à changer...).
* Entre parenthèses, un **itérable** (liste, tuple, dictionnaire, ensemble ou chaîne) qui contient les éléments qui seront ajoutés en tant qu'éléments individuels de la liste.

**F4A1 Conseils :** Selon la [documentation Python](https://docs.python.org/3/glossary.html), un itérable est défini comme "un objet capable de retourner ses membres un à la fois". Les itérables peuvent être utilisés dans une boucle for et, parce qu'ils retournent leurs éléments un à la fois, nous pouvons "faire quelque chose" avec chacun d'eux, un par itération.

### En coulisses

Voyons comment `.extend()` fonctionne en coulisses. Voici un exemple :

```python
# Liste qui sera modifiée
>>> a = [1, 2, 3, 4]

# Séquence de valeurs que nous voulons ajouter à la liste a
>>> b = [5, 6, 7]

# Appel de .extend()
>>> a.extend(b)

# Voir la liste mise à jour. Maintenant, la liste a a les valeurs 5, 6 et 7
>>> a
[1, 2, 3, 4, 5, 6, 7]
```

Vous pouvez penser à `.extend()` comme une méthode qui ajoute les éléments individuels de l'itérable dans le même ordre qu'ils apparaissent.

Dans ce cas, nous avons une liste `a = [1, 2, 3, 4]` comme illustré dans le diagramme ci-dessous. Nous avons également une liste `b = [5, 6, 7]` qui contient la séquence de valeurs que nous voulons ajouter. La méthode prend chaque élément de `b` et l'ajoute à la liste `a` dans le même ordre.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-106.png)
_Etape 1. Le premier élément est ajouté._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-107.png)
_Etape 2. Le deuxième élément est ajouté._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-108.png)
_Etape 3. Le troisième élément est ajouté_

Après que ce processus soit terminé, nous avons la liste mise à jour `a` et nous pouvons travailler avec les valeurs en tant qu'éléments individuels de `a`. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-109.png)

F4A1 **Conseils :** La liste `b` utilisée pour étendre la liste `a` reste intacte après ce processus. Vous pouvez travailler avec elle après l'appel à `.extend()`. Voici la preuve :

```python
>>> a = [1, 2, 3, 4]
>>> b = [5, 6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]

# La liste b est intacte !
>>> b
[5, 6, 7]
```

### Exemples

Vous êtes peut-être curieux de savoir comment la méthode `.extend()` fonctionne lorsque vous passez différents types d'itérables. Voyons comment cela fonctionne dans les exemples suivants :

**Pour les tuples :**  
Le processus fonctionne exactement de la même manière si vous passez un tuple. Les éléments individuels du tuple sont ajoutés un par un dans l'ordre où ils apparaissent. 

```python
# Liste qui sera étendue
>>> a = [1, 2, 3, 4]

# Valeurs qui seront ajoutées (l'itérable est un tuple !)
>>> b = (1, 2, 3, 4)

# Appel de la méthode
>>> a.extend(b)

# La valeur de la liste a a été mise à jour
>>> a
[1, 2, 3, 4, 1, 2, 3, 4]
```

**Pour les ensembles :**  
La même chose se produit si vous passez un ensemble. Les éléments de l'ensemble sont ajoutés un par un.

```python
# Liste qui sera étendue
>>> a = [1, 2, 3, 4]

# Valeurs qui seront ajoutées (l'itérable est un ensemble !)
>>> c = {5, 6, 7}

# Appel de la méthode
>>> a.extend(c)

# La valeur de a a été mise à jour
>>> a
[1, 2, 3, 4, 5, 6, 7]
```

**Pour les chaînes :**  
Les chaînes fonctionnent un peu différemment avec la méthode `.extend()`. Chaque caractère de la chaîne est considéré comme un "élément", donc les caractères sont ajoutés un par un dans l'ordre où ils apparaissent dans la chaîne. 

```python
# Liste qui sera étendue
>>> a = ["a", "b", "c"]

# Chaîne qui sera utilisée pour étendre la liste
>>> b = "Bonjour, le monde !"

# Appel de la méthode
>>> a.extend(b)

# La valeur de a a été mise à jour
>>> a
['a', 'b', 'c', 'B', 'o', 'n', 'j', 'o', 'u', 'r', ',', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', ' ', '!']
```

**Pour les dictionnaires :**  
Les dictionnaires ont un comportement particulier lorsque vous les passez en tant qu'arguments à `.extend()`. Dans ce cas, les **clés** du dictionnaire sont ajoutées une par une. Les valeurs des paires clé-valeur correspondantes ne sont pas ajoutées. 

Dans cet exemple (ci-dessous), les clés sont "d", "e" et "f". Ces valeurs sont ajoutées à la liste `a`. 

```python
# Liste qui sera étendue
>>> a = ["a", "b", "c"]

# Dictionnaire qui sera utilisé pour étendre la liste
>>> b = {"d": 5, "e": 6, "f": 7}

# Appel de la méthode
>>> a.extend(b)

# La valeur de a a été mise à jour
>>> a
['a', 'b', 'c', 'd', 'e', 'f']
```

### Équivalent à...

Ce que `.extend()` fait est équivalent à `a[len(a):] = iterable`. Voici un exemple pour illustrer qu'ils sont équivalents :

En utilisant `.extend()` :

```
# Liste qui sera étendue
>>> a = [1, 2, 3, 4]

# Valeurs qui seront ajoutées
>>> b = (6, 7, 8)

# Appel de la méthode
>>> a.extend(b)

# La liste a été mise à jour
>>> a
[1, 2, 3, 4, 6, 7, 8]

```

En utilisant le découpage de liste :

```python
# Liste qui sera étendue
>>> a = [1, 2, 3, 4]

# Valeurs qui seront ajoutées
>>> b = (6, 7, 8)

# Instruction d'affectation. Affecter l'itérable b comme la portion finale de la liste a
>>> a[len(a):] = b

# La valeur de a a été mise à jour
>>> a
[1, 2, 3, 4, 6, 7, 8]
```

Le résultat est le même, mais l'utilisation de `.extend()` est beaucoup plus lisible et compacte, n'est-ce pas ? Python offre vraiment des outils incroyables pour améliorer notre flux de travail. 

## F4A0 Résumé de leurs différences

Maintenant que vous savez comment travailler avec `.append()` et `.extend()`, voyons un résumé de leurs principales différences :

* **Effet** : `.append()` ajoute un seul élément à la fin de la liste tandis que `.extend()` peut ajouter plusieurs éléments individuels à la fin de la liste.
* **Argument** : `.append()` prend un seul élément comme argument tandis que `.extend()` prend un itérable comme argument (liste, tuple, dictionnaires, ensembles, chaînes).

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec `.append()` et `.extend()` dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐