---
title: 'Python : Supprimer un élément d''une liste – Comment supprimer un élément
  d''une liste en Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-23T18:27:48.000Z'
originalURL: https://freecodecamp.org/news/python-remove-from-list-how-to-remove-an-item-from-a-list-in-python-2
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Remove-from-List
seo_title: 'Python : Supprimer un élément d''une liste – Comment supprimer un élément
  d''une liste en Python'
---

How-to-Remove-an-Item-from-a-List-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nUne liste en Python est une collection d'éléments ordonnés et modifiables. C'est l'une des structures de données les plus polyvalentes et les plus fréquemment utilisées en Python. \nUne liste peut contenir n'importe quel type de données, comme des entiers, des chaînes de caractères, des flottants et même d'autres listes..."
---

Par Shittu Olumide

Une liste en Python est une collection d'éléments ordonnés et modifiables. C'est l'une des structures de données les plus polyvalentes et les plus fréquemment utilisées en Python. 

Une liste peut contenir n'importe quel type de données, comme des entiers, des chaînes de caractères, des flottants et même d'autres listes.

En Python, les listes sont créées en plaçant une séquence de valeurs séparées par des virgules entre des crochets `[]`. 

Par exemple :

```py
numbers = [1,2,3,4,5]

```

Les listes sont des structures de données dynamiques, ce qui signifie qu'elles peuvent être modifiées en ajoutant, supprimant ou changeant leurs éléments. L'indice du premier élément d'une liste est `0`, et l'indice du dernier élément est `n-1`, où n est le nombre d'éléments dans la liste.

Vous pouvez accéder aux listes et les manipuler en utilisant une variété de fonctions et de méthodes intégrées en Python. Certaines des fonctions et méthodes les plus couramment utilisées pour travailler avec des listes incluent `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, et `len()`.

**Cas d'utilisation réel** : Un cas d'utilisation concret de la suppression d'un élément d'une liste en Python se trouve dans les applications de commerce électronique. 

Par exemple, considérons une boutique en ligne qui gère une liste d'articles dans un panier d'achat. Lorsqu'un client souhaite supprimer un article de son panier, la méthode `remove()` ou `pop()` peut être utilisée pour supprimer l'article de la liste. Cela garantit que le panier du client est mis à jour avec les bons articles et les bonnes quantités, et offre une expérience fluide et conviviale pour le client.

Dans cet article, nous allons aborder trois manières différentes de supprimer un élément d'une liste. Il existe plusieurs façons de supprimer un élément d'une liste en Python, selon le cas d'utilisation et les exigences spécifiques. 

## Méthode 1 : Comment supprimer d'une liste en utilisant la méthode `remove()` 

La méthode `remove()` est utilisée pour supprimer la première occurrence d'un élément spécifié dans une liste. Elle prend l'élément à supprimer comme argument et modifie la liste originale. Par exemple :

```py
# Créer une liste de couleurs
colors = ["red", "green", "blue", "yellow"]

# Supprimer la couleur "green"
colors.remove("green")

# Afficher la liste mise à jour
print(colors)

```

Sortie :

```bash
["red", "blue", "yellow"]

```

## Méthode 2 : Comment supprimer d'une liste en utilisant l'instruction `del` 

L'instruction `del` est une instruction polyvalente en Python que vous pouvez utiliser pour supprimer un objet ou un élément d'une liste. Elle prend l'indice de l'élément à supprimer comme argument et modifie la liste originale. Par exemple :

```py
# Créer une liste de nombres
numbers = [1, 2, 3, 4, 5]

# Supprimer le nombre à l'indice 3
del numbers[3]

# Afficher la liste mise à jour
print(numbers)

```

Sortie :

```bash
[1, 2, 3, 5]

```

## Méthode 3 : Comment supprimer d'une liste en utilisant la méthode `pop()` 

La méthode `pop()` est utilisée pour supprimer et renvoyer l'élément à un indice spécifié d'une liste. Elle prend l'indice de l'élément à supprimer comme argument et modifie la liste originale. Si aucun indice n'est spécifié, elle supprime et renvoie le dernier élément de la liste. Par exemple :

```py
# Créer une liste de fruits
fruits = ["apple", "banana", "orange", "mango"]

# Supprimer le fruit à l'indice 2
removed_fruit = fruits.pop(2)

# Afficher la liste mise à jour et le fruit supprimé
print(fruits)       
print(removed_fruit)

```

Sortie :

```bash
["apple", "banana", "mango"]
"orange"

```

## Conclusion

En conclusion, supprimer un élément d'une liste est une opération courante en Python, et il existe plusieurs méthodes disponibles pour accomplir cette tâche. Nous avons abordé trois méthodes couramment utilisées : remove(), l'instruction del, et la méthode pop(), accompagnées d'exemples de code et de commentaires.

Chacune de ces méthodes a ses propres avantages et cas d'utilisation. La méthode `remove()` est utile lorsque la valeur de l'élément à supprimer est connue, tandis que l'instruction `del` est utile lorsque l'indice de l'élément à supprimer est connu. La méthode `pop()` peut être utilisée pour supprimer un élément à un indice spécifique et renvoyer sa valeur.

Retrouvons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !