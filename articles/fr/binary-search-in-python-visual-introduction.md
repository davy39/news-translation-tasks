---
title: 'Recherche Binaire en Python : Une Introduction Visuelle'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-01-13T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/binary-search-in-python-visual-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Binary-Search-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: programing
  slug: programing
- name: Python
  slug: python
seo_title: 'Recherche Binaire en Python : Une Introduction Visuelle'
seo_desc: 'Welcome

  In this article, you will learn how the Binary Search algorithm works behind the
  scenes and how you can implement it in Python.

  In particular, you will learn:


  How the algorithm works behind the scenes to find a target element.

  How its Python...'
---

## Bienvenue

Dans cet article, vous apprendrez comment l'algorithme de Recherche Binaire fonctionne en coulisses et comment vous pouvez l'implémenter en Python.

**En particulier, vous apprendrez :**

* Comment l'algorithme fonctionne en coulisses pour trouver un élément cible.
* Comment son implémentation Python fonctionne ligne par ligne.
* Pourquoi c'est un algorithme très efficace comparé à la Recherche Linéaire.
* Ses avantages et exigences.

**Commençons ! ✨**

## 🔹 Introduction à la Recherche Binaire

Cet algorithme est utilisé pour trouver un élément dans une séquence ordonnée (par exemple : une liste, un tuple ou une chaîne de caractères).

### Exigences

Pour appliquer l'algorithme de Recherche Binaire à une séquence, la séquence doit déjà être triée par ordre croissant. Sinon, l'algorithme ne trouvera pas la bonne réponse. Si c'est le cas, ce sera par pure coïncidence.

**💡 Astuce :** Vous pouvez trier la séquence avant d'appliquer la Recherche Binaire avec un algorithme de tri qui répond à vos besoins.

### Entrée et Sortie

L'algorithme (implémenté sous forme de fonction) a besoin de ces données :

* Une séquence ordonnée d'éléments (par exemple : liste, tuple, chaîne de caractères).
* L'élément cible que nous recherchons.

Il retourne l'**index** de l'élément que vous recherchez s'il est trouvé. Si l'élément n'est pas trouvé, -1 est retourné.

### Efficacité

Il est très efficace comparé à la Recherche Linéaire (recherche d'un élément un par un, en commençant par le premier) car nous sommes capables de "rejeter" la moitié de la liste à chaque étape.

Commençons à plonger dans cet algorithme.

## 🔸 Parcours Visuel

Nous allons appliquer l'algorithme de Recherche Binaire à cette liste :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-4.png)

**💡 Astuce :** Remarquez que la liste est déjà triée. Elle inclut les indices comme référence visuelle.

### Objectif

Nous voulons trouver l'index de l'entier **67**.

### Intervalle

Faisons semblant d'être l'algorithme. Comment commençons-nous le processus ?

Nous commençons par sélectionner les deux bornes de l'intervalle où nous voulons rechercher. Nous voulons rechercher dans toute la liste, donc nous sélectionnons l'index `0` comme borne inférieure et l'index `5` comme borne supérieure :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-6.png)

### Élément du Milieu

Maintenant, nous devons trouver l'index de l'élément du milieu dans cet intervalle. Nous faisons cela en additionnant la borne inférieure et la borne supérieure et en divisant le résultat par 2 en utilisant la division entière.

Dans ce cas, `(0 + 5)//2` est **`2`** car le résultat de `5/2` est `2.5` et la division entière troncature la partie décimale. Donc l'élément du milieu est situé à l'**index 2**, et l'élément du milieu est le nombre **6** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-7.png)

### Comparaisons

Maintenant, nous devons commencer à comparer l'élément du milieu avec notre élément cible pour voir ce que nous devons faire ensuite.

Nous demandons :
**L'élément du milieu est-il égal à l'élément que nous recherchons ?**

```python
6 == 67 # False
```

Non, ce n'est pas le cas.

Donc nous demandons :
**L'élément du milieu est-il plus grand que l'élément que nous recherchons ?**

```python
6 > 67 # False
```

Non, ce n'est pas le cas.

Donc **l'élément du milieu est plus petit que l'élément que nous recherchons.**

```
6 < 67 # True
```

### Rejeter les Éléments

Puisque la liste est déjà triée, cela nous dit quelque chose d'extrêmement important. Cela nous dit que nous pouvons "rejeter" la moitié inférieure de la liste car nous savons que tous les éléments qui viennent avant l'élément du milieu seront plus petits que l'élément que nous recherchons, donc notre élément cible n'est pas là.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-9.png)

### Recommencer - Choisir les Bornes

Que faisons-nous ensuite ? Nous avons rejeté les éléments et le cycle est répété à nouveau.

Nous devons choisir les bornes pour le nouvel intervalle (voir ci-dessous). Mais remarquez que la borne supérieure est conservée intacte et seule la borne inférieure est changée.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-10.png)

C'est parce que l'élément que nous recherchons pourrait être dans la moitié supérieure de la liste. La borne supérieure est conservée intacte et la borne inférieure est changée pour "réduire" l'intervalle à un intervalle où notre élément cible pourrait être trouvé.

💡 **Astuce :** Si l'élément du milieu avait été plus grand que l'élément que nous recherchons, la borne supérieure aurait été changée et la borne inférieure aurait été conservée intacte. De cette façon, nous aurions rejeté la moitié supérieure de la liste et continué à rechercher dans la moitié inférieure.

### Élément du Milieu

Maintenant, nous devons trouver l'index de l'élément du milieu en additionnant la borne inférieure à la borne supérieure et en divisant le résultat par 2 en utilisant la division entière.

Le résultat de `(3+5)//2` est `4`, donc l'élément du milieu est situé à l'**index** `**4**` et l'élément du milieu est **67**.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-11.png)

### Comparaisons

Nous demandons :
**L'élément du milieu est-il égal à l'élément que nous recherchons ?**

```
67 == 67 # True
```

Oui, c'est le cas ! Donc nous avons trouvé l'élément à l'index **4**. La valeur 4 est retournée et l'algorithme a été complété avec succès.

💡 **Astuce :** Si l'élément n'avait pas été trouvé, le processus aurait continué jusqu'à ce que l'intervalle ne soit plus valide. Si l'élément n'avait pas été trouvé dans toute la liste, -1 aurait été retourné.

## 🔹 Parcours du Code

Maintenant que vous avez une intuition visuelle de comment l'algorithme fonctionne en coulisses, plongeons dans l'implémentation Python itérative en l'analysant ligne par ligne :

```
def binary_search(data, elem):

    low = 0
    high = len(data) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1
```

### En-tête

Voici l'en-tête de la fonction :

```
def binary_search(data, elem):
```

Elle prend deux arguments :

* La séquence ordonnée d'éléments (par exemple : liste, tuple ou chaîne de caractères).
* L'élément que nous voulons trouver.

### Intervalle Initial

La ligne suivante définit les bornes inférieure et supérieure initiales :

```python
low = 0
high = len(data) - 1
```

La borne inférieure initiale est l'index `0` et la borne supérieure initiale est le dernier index de la séquence.

### Boucle

Nous allons répéter le processus tant qu'il y a un intervalle valide, tant que la borne inférieure est plus petite ou égale à la borne supérieure.

```python
while low <= high:
```

💡 **Astuce :** Rappelez-vous que les bornes sont des indices.

### Élément du Milieu

À chaque itération, nous devons trouver l'index de l'élément du milieu. Pour ce faire, nous additionnons les bornes inférieure et supérieure et divisons le résultat par 2 en utilisant la division entière.

```python
middle = (low + high)//2
```

💡 **Astuce :** Nous utilisons la division entière au cas où la liste ou l'intervalle contient un nombre pair d'éléments. Par exemple, si la liste avait 6 éléments et que nous n'utilisions pas la division entière, `middle` serait le résultat de `(0 + 5)/2` qui est `2.5`. Un index ne peut pas être un float, donc nous tronquons la partie décimale en utilisant `//` et sélectionnons l'élément à l'index `2`.

### Comparaisons

Avec ces conditionnelles (voir ci-dessous), nous déterminons quoi faire en fonction de la valeur de l'élément du milieu `data[middle]`. Nous le comparons à l'élément cible que nous recherchons.

```python
if data[middle] == elem:
    return middle
elif data[middle] > elem:
    high = middle - 1
else:
    low = middle + 1
```

Il y a trois options :

* Si l'élément du milieu est égal à l'élément que nous recherchons, nous retournons l'index immédiatement car nous avons trouvé l'élément.

```python
if data[middle] == elem:
    return middle
```

* Si l'élément du milieu est plus grand que l'élément que nous recherchons, nous réassignons la borne supérieure car nous savons que l'élément cible est dans la moitié inférieure de la liste.

```python
elif data[middle] > elem:
    high = middle - 1
```

* Sinon, la seule option restante est que l'élément du milieu est plus petit que l'élément que nous recherchons, donc nous réassignons la borne inférieure car nous savons que l'élément cible est dans la moitié supérieure de la liste.

```python
else:
    low = middle + 1
```

### Élément Non Trouvé

Si la boucle est complétée sans trouver l'élément, la valeur -1 est retournée.

```python
return -1
```

et nous avons l'implémentation finale de l'algorithme de Recherche Binaire :

```
def binary_search(data, elem):

    low = 0
    high = len(data) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1
```

## 🔹 Cas Particuliers

Voici quelques cas particuliers que vous pourriez rencontrer en commençant à travailler avec cet algorithme :

### Éléments Répétés

Si l'élément que vous recherchez est répété dans la séquence, l'index retourné dépendra du nombre d'éléments et de la séquence d'opérations que l'algorithme effectue sur la séquence.

```python
>>> >>> b = [2, 2, 3, 6, 7, 7]
>>> binary_search(b, 7)
4

```

### Élément Non Trouvé

Si l'élément n'est pas trouvé, -1 est retourné.

```python
>>> b = [2, 2, 3, 6, 7, 7]
>>> binary_search(b, 8)
-1
```

### Séquence Vide

Si la séquence est vide, -1 sera retourné.

```python
>>> b = []
>>> binary_search(b, 8)
-1
```

### Séquence Non Triée

Si la séquence n'est pas triée, la réponse ne sera pas correcte. Obtenir l'index correct est une pure coïncidence et cela pourrait être dû à l'ordre des éléments dans la séquence et à la séquence d'opérations effectuées par l'algorithme.

Cet exemple retourne le résultat correct :

```python
>>> b = [5, 7, 3, 0, -9, 2, 6]
>>> binary_search(b, 6)
6
```

Mais celui-ci ne le fait pas :

```python
>>> b = [5, 7, 3, 0, -9, 2, 10, 6]
>>> binary_search(b, 6)
-1
```

💡 **Astuce :** Réfléchissez à pourquoi le premier exemple retourne le résultat correct. Indice : C'est une pure coïncidence que l'ordre des éléments fasse que l'algorithme atteigne l'index correct, mais le processus étape par étape évalue `0`, puis `2`, et enfin `6`. Dans ce cas particulier, pour cet élément particulier, l'index correct est trouvé même si la séquence n'est pas triée.

## 🔹 Un Exemple Plus Complexe

Maintenant que vous êtes plus familier avec l'algorithme et son implémentation Python, voici un exemple plus complexe :

Nous voulons trouver l'index de l'élément **45** dans cette liste en utilisant la Recherche Binaire :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-12.png)

### Première Itération

Les bornes inférieure et supérieure sont sélectionnées :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-13.png)

L'élément du milieu (**26**) est sélectionné :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-14.png)

Mais l'élément du milieu (**26**) n'est pas l'élément que nous recherchons, il est plus petit que **45** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-15.png)

### Deuxième Itération

Donc nous pouvons rejeter tous les éléments qui sont plus petits que l'élément du milieu et sélectionner de nouvelles bornes. La nouvelle borne inférieure (**27**) est l'élément situé immédiatement à droite de l'élément du milieu précédent :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-16.png)

💡 **Astuce :** Rappelez-vous que la liste est déjà triée.

Le nouvel élément du milieu (**30**) est sélectionné :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-17.png)

L'élément du milieu (**30**) n'est pas l'élément que nous recherchons, il est plus petit que **45** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-18.png)

### Troisième Itération

Nous pouvons rejeter les éléments qui sont plus petits ou égaux à **30** qui n'ont pas déjà été rejetés. La borne inférieure est mise à jour à **32** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-19.png)

Ici nous avons un cas intéressant : l'élément du milieu est l'une des bornes de l'intervalle actuel car `(7+8)//2` est `7`.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-20.png)

L'élément du milieu (**32**) n'est pas l'élément que nous recherchons (**45**), il est plus petit.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-21.png)

### Quatrième Itération

Nous pouvons rejeter les éléments qui sont plus petits ou égaux à **32** qui n'ont pas déjà été rejetés.

Ici nous avons un autre cas très intéressant : l'intervalle ne contient qu'un seul élément.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-22.png)

💡 **Astuce :** Cet intervalle est valide car nous avons écrit cette condition `while high <= low:`, qui inclut les intervalles où l'index de la borne inférieure est égal à l'index de la borne supérieure.

L'élément du milieu est le seul élément de l'intervalle car `(8+8)//2` est `8`, donc l'index de l'élément du milieu est **8** et l'élément du milieu est **45**.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-23.png)

Maintenant, l'élément du milieu est l'élément que nous recherchons, **45** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-24.png)

Donc la valeur **8** (l'index) est retournée :

```
>>> binary_search([1, 3, 7, 15, 26, 27, 30, 32, 45], 45)
8
```

## 🔹 Pratique Supplémentaire

Si vous souhaitez avoir une pratique supplémentaire avec cet algorithme, essayez d'expliquer comment l'algorithme fonctionne en coulisses lorsqu'il est appliqué à cette liste pour trouver l'entier **90** :

```
[5, 8, 15, 26, 38, 56]
```

* Que se passe-t-il étape par étape ?
* Quelle valeur est retournée ?
* L'élément est-il trouvé ?

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant vous pouvez implémenter l'algorithme de Recherche Binaire en Python. Consultez mon cours en ligne "[Python Searching & Sorting Algorithms: A Practical Approach](https://www.udemy.com/course/python-searching-sorting-algorithms/?couponCode=FREECODECAMP-ALG)". Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️