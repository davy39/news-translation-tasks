---
title: Les méthodes de liste Python expliquées en français simple
subtitle: ''
author: Gold Agbonifo Isaac
co_authors: []
series: null
date: '2023-09-24T14:08:41.000Z'
originalURL: https://freecodecamp.org/news/python-list-methods-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/A.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Les méthodes de liste Python expliquées en français simple
seo_desc: We often make plans about the things we want, what we need to do, and places
  we want to visit. These lists could go on forever! However, there are times when
  we need to build a program that requires us to organize and manipulate information
  using lis...
---

Nous faisons souvent des plans concernant les choses que nous voulons, ce que nous devons faire et les endroits que nous voulons visiter. Ces listes pourraient être infinies ! Cependant, il arrive que nous devions créer un programme qui nécessite d'organiser et de manipuler des informations à l'aide de listes. 

Dans cet article, nous allons explorer comment créer et travailler avec des listes en Python, en fournissant des explications simples pour les débutants.

## Comprendre les listes Python

En Python, une liste est une structure de données fondamentale utilisée pour stocker des informations ou des objets spécifiques. Si vous n'êtes pas familier avec le concept de structure de données, pensez-y comme à un moyen d'organiser et de stocker des données afin de pouvoir y accéder et les manipuler facilement. Les structures de données existent pour vous aider à structurer vos données de manière efficace.

Plongeons dans ce que vous pouvez faire avec une liste Python et comment vous pouvez y parvenir.

## Méthodes de liste en Python

Python offre une large gamme de fonctionnalités pour les listes, et je vais vous en présenter quelques-unes.

### La méthode `.append()`

Cette méthode vous permet d'ajouter un élément à la fin d'une liste.

Voici comment cela fonctionne :

```python

# Imaginez que votre liste contient des articles que vous devez acheter
things_i_need = ["shoes", "bags", "groceries"]

# Soudain, vous vous souvenez de quelque chose d'autre à ajouter
things_i_need.append("toiletries")

# Maintenant, imprimons la liste mise à jour
print(things_i_need)

Vous pouvez utiliser la méthode `.append()` pour ajouter des éléments de n'importe quel type de données à une liste, qu'il s'agisse de nombres, de chaînes de caractères, ou même de contenus d'une autre liste.

### La méthode `.extend()`

Cette méthode fait une chose et la fait vraiment bien. Elle vous permet d'étendre vos listes en ajoutant plus d'éléments à la liste.

Maintenant, ne vous trompez pas en vous demandant : "Cela signifie-t-il que la méthode `.append()` est la même que la méthode `.extend()` ?" Eh bien, la réponse à cela est NON.

La méthode `.extend()` vous permet d'ajouter plus d'éléments à la fin d'une liste, tandis que la méthode `.append()` est utilisée pour ajouter un seul élément. Si vous devez ajouter beaucoup d'éléments à votre liste, alors la méthode `.extend()` est celle qu'il vous faut.

La méthode `.extend()` prend une autre liste (ce qui pourrait être appelé un itérable) comme argument (un argument est une pièce d'information que vous attachez à une fonction ou à un programme pour lui permettre d'accomplir sa tâche efficacement), puis ajoute chaque élément à la liste originale.

Voici un exemple de code pour illustrer davantage notre explication :

```python
# nous allons utiliser la même liste Things_I_need
Things_I_need = ["shoes", "bags", "groceries"]

# Vous vous souvenez soudainement que vous avez besoin de plus de choses

Additional_stuffs_I_need = ["clothes", "skincare", "makeup"]

# Maintenant, vous pouvez ajouter cette nouvelle liste à votre liste précédente
Things_I_need.extend(Additional_stuffs_I_need)

# Votre liste est maintenant ["shoes", "bags", "groceries", "clothes", "skincare", "makeup"]

Donc, si vous devez étendre votre liste avec plus d'éléments, n'oubliez pas d'utiliser la méthode `.extend()` !

### La méthode `.insert()`

Contrairement aux méthodes que nous avons discutées jusqu'à présent, la méthode `.insert()` offre une fonctionnalité unique. Elle ne vous permet pas seulement d'ajouter des éléments, mais aussi de spécifier leurs positions ! Plutôt impressionnant, n'est-ce pas ?

Eh bien, la méthode `insert()` est assez intrigante car elle vous donne le contrôle sur les positions où vos éléments seront insérés, et cela est réalisé grâce à l'utilisation d'index. (Rappelez-vous, en informatique, l'indexation commence généralement à 0 !)

Voici un exemple pour démontrer comment cela fonctionne :

```python
# Utilisation de la liste 'things_I_need' à nouveau

things_I_need = ["shoes", "bags", "groceries"]

# Supposons que vous vouliez ajouter quelque chose de plus important que les chaussures, les sacs ou les courses.

# Vous pouvez insérer un tel élément comme premier de la liste
things_I_need.insert(0, "my_meds")

# Ici, '0' représente la position que vous avez choisie pour le nouvel élément.
# Maintenant, imprimons notre résultat final
print(things_I_need)

# La nouvelle liste serait : ['my_meds', 'shoes', 'bags', 'groceries']

La méthode `.insert()` est assez pratique, alors n'oubliez pas de l'utiliser lorsque vous devez manipuler des positions !

### La méthode `.remove()`

Avez-vous déjà réalisé que vous avez accidentellement ajouté un élément deux fois à votre liste ? Eh bien, en plus de la solution évidente d'utiliser la touche de suppression, vous pouvez en fait supprimer la première occurrence d'un élément de votre liste !

Voici un exemple pour vous montrer comment cela fonctionne :

```python
# Utilisation de la liste 'things_I_need' à nouveau.
# Supposons que votre amour pour les chaussures vous a fait l'écrire deux fois.
things_I_need = ["shoes", "bags", "groceries", "shoes"]

# Vous avez remarqué la duplication et décidé de supprimer une des chaussures.
things_I_need.remove("shoes")

# Maintenant, imprimez votre liste mise à jour avec la première occurrence de "shoes" supprimée.
print(things_I_need)

# La nouvelle liste est ["bags", "groceries", "shoes"].

Cependant, veuillez être prudent avec la méthode `.remove()`. Assurez-vous de ne jamais tenter de supprimer un élément qui n'est pas dans la liste, sinon vous rencontrerez une erreur de valeur. Cela se produit parce que vous essayez d'accéder à un élément qui est hors de portée ou hors des limites.

### La méthode `.pop()`

Similaire à la méthode `.remove()`, vous pouvez utiliser la méthode `.pop()` pour supprimer des éléments d'une liste.

Cependant, il y a une différence : la méthode `.pop()` offre plus de flexibilité que la méthode `.remove()`. Vous pouvez supprimer un élément à une position spécifique dans une liste en spécifiant cette position.

Ce qui est encore plus intéressant, c'est que si vous oubliez de spécifier ce que vous voulez supprimer, elle supprimera automatiquement le dernier élément de votre liste.

Voici un exemple de la façon dont vous pouvez utiliser `.pop()` pour supprimer un élément par index :

```python
# Utilisation de la liste 'things_I_need' à nouveau.
things_I_need = ["shoes", "bags", "groceries"]

# Supposons que vous vouliez être économique en supprimant les chaussures
popped_list = things_I_need.pop(0)

# Maintenant, imprimez votre nouvelle liste économique
print(popped_list)

# La nouvelle liste est ["bags", "groceries"]

### La méthode `.clear()`

Vous avez fait une liste et décidé qu'elle était redondante. Vous réalisez soudainement que tout ce que vous avez mis dans votre liste n'était pas important. Vous pouvez utiliser la méthode `.clear()` pour vider votre liste.

Voici comment faire :

```python
# Utilisation de la liste things_I_need
things_I_need = ["shoes", "bags", "groceries"]

things_I_need = things_I_need.clear(things_I_need)
print(things_I_need)

# La nouvelle liste est vide []

### La méthode `.index()`

La méthode `.index()` est un outil en Python qui vous aide à trouver où se trouve la première occurrence d'un élément spécifique dans une liste. Elle vous indique la position de cet élément dans la liste, comme sa place dans une file d'éléments.

Voici un exemple :

```python
# Utilisation d'une liste de choses dont vous avez besoin
things_I_need = ["shoes", "bags", "groceries", "shoes", "bags"]

# Trouver l'index de la première occurrence de "shoes"
shoes_index = things_I_need.index("shoes")

# Trouver l'index de la première occurrence de "bags"
bags_index = things_I_need.index("bags")

print("Index de 'shoes' :", shoes_index)
print("Index de 'bags' :", bags_index)

# Sortie : Index de 'shoes' : 0
# Sortie : Index de 'bags' : 1

### La méthode `.count()`

La méthode `.count()` en Python est pratique pour compter les occurrences.

Permettez-moi de vous expliquer : elle vous aide à découvrir combien de fois un élément spécifique apparaît dans votre liste. Cela peut être vraiment utile, surtout lorsque vous traitez avec des listes plus grandes.

Voici un exemple pour comprendre comment cela fonctionne :

```python

# Utilisation d'une liste de choses dont vous avez besoin
things_I_need = ["shoes", "bags", "groceries", "shoes", "bags"]

# Compter les occurrences de "shoes"
shoes_count = things_I_need.count("shoes")

# Compter les occurrences de "bags"
bags_count = things_I_need.count("bags")

print("Nombre de shoes :", shoes_count)
print("Nombre de bags :", bags_count)

### La méthode `.reverse()`

`.reverse()` vous donne essentiellement une version alternative de votre liste en vous donnant une liste à l'envers.

Par exemple, si vous aviez une liste de nombres 1, 2, 3, 4, 5, l'inverse serait 5, 4, 3, 2, 1.

Voici comment vous pouvez utiliser la méthode `.reverse()` en Python :

```python
# Utilisation d'une liste de choses dont vous avez besoin
things_I_need = ["shoes", "bags", "groceries"]

# Inverser l'ordre des éléments dans la liste en place
things_I_need.reverse()

# Imprimer la liste inversée
print(things_I_need)

# La sortie est ['groceries', 'bags', 'shoes']

### La méthode `.copy()`

Que signifie faire une copie de quelque chose ? Créer un duplicata de l'original, n'est-ce pas ? Avoir une autre version de quelque chose, non ? Eh bien, c'est exactement ce que fait la méthode `.copy()` !

Et voici comment elle le fait :

```python
# Utilisation d'une liste de choses dont vous avez besoin
things_I_need = ["shoes", "bags", "groceries"]

# Créer une copie de la liste en utilisant la méthode .copy()
copied_list = things_I_need.copy()

# Imprimer la liste copiée
print(copied_list)

## Conclusion

Vous êtes maintenant arrivé à la fin du tutoriel. À ce stade, j'espère que vous avez saisi les bases de l'utilisation des méthodes dans les listes Python. J'ai apprécié écrire ceci, et j'espère que vous vous êtes amusé aussi !