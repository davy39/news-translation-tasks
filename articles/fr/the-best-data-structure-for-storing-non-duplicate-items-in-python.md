---
title: La meilleure structure de données pour stocker des éléments non dupliqués en
  Python
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-08-03T15:08:47.000Z'
originalURL: https://freecodecamp.org/news/the-best-data-structure-for-storing-non-duplicate-items-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/The-Best-Data-Structure-For-Storing-Non-Duplicate-Items-In-Python.png
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: La meilleure structure de données pour stocker des éléments non dupliqués
  en Python
seo_desc: "If you're coding in Python and you need to store non-duplicate items while\
  \ ensuring each item is unique, which data structure should you use? \nI'd recommend\
  \ the set data structure. It's an unordered collection of unique elements, meaning\
  \ it cannot co..."
---

Si vous codez en Python et que vous devez stocker des éléments non dupliqués tout en garantissant que chaque élément est unique, quelle structure de données devez-vous utiliser ?

Je vous recommande la structure de données `set`. Il s'agit d'une collection non ordonnée d'éléments uniques, ce qui signifie qu'elle ne peut pas contenir d'éléments dupliqués.

Lorsque vous ajoutez des éléments à un set, Python supprime automatiquement les doublons. Cela en fait un choix parfait pour les scénarios où vous devez stocker une collection d'éléments tout en garantissant leur unicité.

## Comment utiliser un `set` en Python

Vous pouvez créer un set en Python en utilisant des accolades `{}` ou la fonction intégrée `set()`.

Supposons que vous sachiez déjà que vous aurez des éléments dupliqués mais que vous ne souhaitez pas conserver les doublons. Vous pouvez alors commencer à entrer directement les éléments dans un set. Voici un exemple :

```python
# Création d'un set
my_set = {1, 2, 3, 4, 3, 5}  # Le doublon '3' est automatiquement supprimé

print(my_set)  # Sortie : {1, 2, 3, 4, 5}
```

Ici, j'ai créé un set dans la variable `my_set`, et j'ai deux éléments dupliqués. Comme vous pouvez le voir dans la sortie, les doublons ont été supprimés.

Si vous avez une liste avec des doublons potentiels et que vous souhaitez les supprimer pour créer un set, vous pouvez simplement convertir la liste en set en utilisant la fonction `set()`.

Supposons que vous ayez déjà une liste contenant beaucoup de données, par exemple les données des clients de votre magasin. À la fin du mois, vous souhaitez savoir exactement combien de clients individuels sont venus à votre magasin.

Pendant le mois, vous avez stocké les identifiants uniques des clients dans une liste et les avez enregistrés à chaque fois qu'ils visitaient votre magasin. Comme certains clients sont venus plus d'une fois ce mois-là, il est très probable que la liste où vous avez stocké les identifiants des clients contienne des données dupliquées (ce qui est redondant lorsque vous essayez de calculer tous les clients uniques).

Vous souhaitez donc une solution où vous n'extrayez que les identifiants de clients uniques de cette liste particulière, mais par sécurité, vous ne souhaitez pas modifier ou changer les données de la liste originale.

Dans ce cas, vous pouvez simplement créer une nouvelle variable pour extraire les données uniques de cette liste et les stocker là. Vous pouvez également utiliser la fonctionnalité de set ici. Par exemple :

```python
# Suppression des doublons d'une liste et création d'un set
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)

print(my_set)  # Sortie : {1, 2, 3, 4, 5}
```

Ici, j'ai ma liste dans la variable `my_list` qui contient actuellement des éléments dupliqués, `2` (apparaît deux fois) et `4` (apparaît également deux fois).

Mais dans la deuxième ligne, j'ai initialisé une nouvelle variable nommée `my_set` où je stocke le set de `my_list`. Comme le set supprime automatiquement les doublons et ne conserve qu'un seul élément des doublons, je stocke tous les éléments uniques dans ma variable `my_set`.

Mais si j'affiche `my_list`, j'obtiendrai toujours les valeurs dupliquées ensemble. Cela est dû au fait que nous n'avons pas du tout changé la liste originale. Nous avons simplement créé une nouvelle variable nommée `my_set` et stocké uniquement les valeurs uniques de cette liste.

Mais si vous souhaitez vraiment supprimer les doublons de la liste originale et créer une autre liste, vous pouvez supprimer les doublons de la liste en la convertissant d'abord en set puis en liste à nouveau. De cette manière, vous pouvez obtenir une nouvelle liste sans les doublons.

Par exemple :

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = list(set(my_list)) # Suppression des doublons en convertissant d'abord en set puis en liste
print(new_list) # Sortie : [1, 2, 3, 4, 5]
```

Mais si vous souhaitez vraiment modifier la liste originale, vous pouvez créer un set et supprimer les doublons, puis vous pouvez à nouveau convertir cela en liste et stocker les données de la liste dans la liste originale à nouveau !

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list)) # Modification de la liste pour supprimer les doublons des données de la liste précédente et stockage des nouvelles données sans doublons dans cette liste
print(my_list) # Sortie : [1, 2, 3, 4, 5]
```

Les sets offrent des tests d'appartenance rapides et des opérations efficaces pour les opérations de théorie des ensembles (comme l'union, l'intersection et la différence), ce qui en fait un excellent choix pour gérer des collections d'éléments uniques en Python.

## **🏺 Vidéo explicative**

Je sais que beaucoup d'entre vous préfèrent regarder une vidéo plutôt que de suivre un article complet. Ne vous inquiétez pas ! J'ai également créé un tutoriel vidéo complet pour vous :

%[https://www.youtube.com/watch?v=3IKzhY5jlKk]

## Conclusion

J'espère que vous avez apprécié cet article.

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur :

🎁GitHub : [FahimFBA](https://github.com/FahimFBA)

🎁YouTube : [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)