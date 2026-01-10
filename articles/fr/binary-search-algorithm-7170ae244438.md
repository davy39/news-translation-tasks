---
title: Algorithmes de recherche binaire expliqués à l'aide d'images de caméra de sécurité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-17T19:22:09.000Z'
originalURL: https://freecodecamp.org/news/binary-search-algorithm-7170ae244438
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gjDukf9SgTpJOq2tFe9Iyw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Algorithmes de recherche binaire expliqués à l'aide d'images de caméra
  de sécurité
seo_desc: 'By Julia Geist


  Binary search, also known as half-interval search or logarithmic search, is a search
  algorithm that finds the position of a target value within a sorted array.


  Context

  I used to live in a building that had a communal kitchen for over...'
---

Par Julia Geist

> La recherche binaire, également connue sous le nom de recherche par moitié d'intervalle ou recherche logarithmique, est un algorithme de recherche qui trouve la position d'une valeur cible dans un tableau trié.

### Contexte

Je vivais dans un bâtiment qui avait une cuisine commune pour plus de 100 étudiants. Comme vous pouvez l'imaginer, il y avait presque toujours des plats non lavés dans l'évier. Un groupe de mon école a proposé l'idée d'installer une Nest Cam pour attraper les coupables et les dénoncer en utilisant le flux de la Nest Cam.

Pour illustrer mon propos, disons que vous avez trouvé des plats sales à 12h, et que vous n'étiez pas dans la cuisine depuis un jour.

Pensez à la manière dont vous rechercheriez la personne qui a laissé les plats. Regarderiez-vous les 24 heures de footage, depuis le début, jusqu'à ce que vous trouviez le coupable ?

Probablement pas. Très probablement, vous sauteriez dans le footage, vérifiant si les plats étaient dans l'évier, disons, 12 heures plus tôt — à minuit. Si c'était le cas, alors vous sauriez que cela s'est produit avant minuit. Vous pourriez revenir à 22h après cela. Si les plats n'y sont pas, vous avez maintenant réduit la période de 22h à minuit — en d'autres termes, vous avez exclu tout moment avant 22h. Vous continueriez ce processus jusqu'à ce que vous trouviez le coupable.

![Image](https://cdn-media-1.freecodecamp.org/images/t1WQMX7wWxGGHHyXER-9NOVgc0FZPN2WMgAT)
_Recherche binaire du moment où la tasse orange est mise dans l'évier (vidéo YouTube utilisée)_

Ce qui vous aurait pris jusqu'à 24 heures, si vous aviez regardé le footage dans son intégralité, ne prend maintenant que quelques secondes.

Que vous le sachiez ou non, le processus spécifique que nous venons de parcourir est une recherche binaire ! Une recherche binaire est une manière très spécifique de sauter en avant et en arrière dans le footage.

À savoir, le footage est divisé à son point médian pour vérifier la présence des plats à chaque fois. Remarquez comment la distance jusqu'au point médian devient exponentiellement plus petite à chaque clic.

Les recherches binaires sont utilisées pour trouver des éléments rapidement et efficacement. Le piège, cependant, est que **les recherches binaires ne fonctionnent que lorsque la structure que vous parcourez est triée**.

Dans l'exemple de la Nest Cam, par quoi le footage est-il trié ? Que cherchons-nous dans cet arrangement trié ?

Dans ce cas, les données que nous recherchons sont triées par temps. Le temps permet une mesure linéaire. Par conséquent, il nous permet d'effectuer une recherche binaire pour trouver quelqu'un qui ne lave pas ses plats en quelques secondes.

Nous avons également besoin de quelque chose que nous recherchons. Dans ce cas, il s'agit de la présence de plats non lavés dans l'évier commun.

### Algorithme de recherche binaire

![Image](https://cdn-media-1.freecodecamp.org/images/d27KVv4hAnngmMMZ1rz4GjXIgsceR5H9tHzP)

En programmation, une recherche binaire peut être utilisée dans une multitude de contextes. C'est un moyen extrêmement rapide de trouver des éléments dans une structure triée.

Les recherches binaires peuvent être implémentées de manière itérative ou récursive. Une implémentation itérative utilise une boucle `while`. Pendant ce temps, une implémentation récursive s'appellera elle-même depuis son propre corps.

En code, je vais effectuer une recherche binaire sur un ensemble de données relativement simple et trié pour mettre en évidence l'implémentation centrale d'une recherche binaire.

Étant donné un tableau de nombres triés, retourne `True` si 53 est un élément.

```
[0, 3, 4, 5, 6, 15, 18, 22, 25, 27, 31, 33, 34, 35, 37, 42, 53, 60]
```

#### Itératif

Dans l'approche itérative, une boucle while s'exécute jusqu'à ce que la plage de possibilités soit nulle. Cela est fait en changeant les bornes supérieure et inférieure de l'endroit où nous cherchons et en calculant l'index du milieu de cette plage.

La plage existe entre les bornes inférieure et supérieure, inclusivement.

![Image](https://cdn-media-1.freecodecamp.org/images/zO-GtUNZ6ezlXEHMhdvP4JjOxmmqBZCePp9L)

Avant que la boucle `while` ne commence, la borne inférieure est zéro et la borne supérieure est la longueur du tableau. La borne supérieure change si le nombre que nous cherchons est dans la première moitié de la plage. La borne inférieure change si le nombre que nous cherchons est dans la deuxième moitié de la plage.

Si la boucle `while` se termine, ce qui signifie qu'il y a une plage de longueur zéro, retourne `False`.

```
def binarySearch(array, number):   lowerBound = 0   upperBound = len(array)
```

```
while lowerBound < upperBound:        middleIndex = int(math.floor(lowerBound + (upperBound — lowerBound) / 2))        if array[middleIndex] == number:             return True        elif array[middleIndex] < number:             lowerBound += 1        elif array[middleIndex] > number:             upperBound = middleIndex   return False
```

J'aimerais élaborer sur cette équation :

`int(math.floor(lowerBound + (upperBound — lowerBound) / 2))`

La longueur de la plage est calculée en soustrayant la borne inférieure de la borne supérieure. Cependant, savoir à quel point la plage est longue n'est pas suffisant.

À ce stade, nous ne savons pas quels index vérifier dans le tableau. Nous décalons donc le tableau vers le haut par la borne inférieure.

Nous divisons ensuite cela par deux, et arrondissons vers le bas, pour obtenir l'index du milieu de la plage. `math.floor` retourne un `float`, donc nous devons également convertir le résultat en `int`.

#### Récursif

Dans l'approche récursive, la fonction s'appellera elle-même depuis son propre corps.

La borne supérieure dans cette fonction est la longueur du tableau passé en argument. Encore une fois, la borne supérieure change si le nombre que nous cherchons est dans la première moitié du tableau. La borne inférieure change si le nombre que nous cherchons est dans la deuxième moitié du tableau.

```
def binarySearch(array, number):    middleIndexOfArray = int(math.floor(len(array) / 2))    if middleIndexOfArray == 0:        return False
```

```
if array[middleIndexOfArray] == number:        return True   elif array[middleIndexOfArray] > number:        return binarySearch(array[:middleIndexOfArray], number)   elif array[middleIndexOfArray] < number:        return binarySearch(array[middleIndexOfArray:], number)
```

La fonction s'appelle ensuite elle-même, passant en argument un tableau de moitié la longueur du tableau qui était son argument.

S'il y a zéro élément dans le tableau, retourne `False`.

Le code est disponible sur mon dépôt [Algorithms and Data Structures](https://github.com/juliascript/Algorithms-and-Data-Structures) — étoilez-le pour rester à jour !

### Prochaines étapes

J'ai écrit ma première recherche binaire pour implémenter un algorithme d'échantillonnage stochastique. Il génère une phrase basée sur la fréquence des mots dans un corpus de texte.

N'hésitez pas à essayer de construire un projet similaire, qui nécessite pas mal de préparation avant de pouvoir implémenter la recherche binaire. Ou pensez à vos propres projets et partagez-les dans les commentaires !

Ceci est le deuxième article de ma série sur les algorithmes et les structures de données. Dans chaque article, je présenterai un problème qui peut être mieux résolu avec un algorithme ou une structure de données pour illustrer l'algorithme/la structure de données elle-même.

Étoilez mon [dépôt d'algorithmes](https://github.com/juliascript/Algorithms-and-Data-Structures) sur Github et suivez-moi sur [Twitter](https://twitter.com/JuliaGeist) si vous souhaitez suivre !