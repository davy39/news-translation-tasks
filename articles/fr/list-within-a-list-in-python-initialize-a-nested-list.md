---
title: Liste dans une Liste en Python – Comment Initialiser une Liste Imbriquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-16T17:24:40.000Z'
originalURL: https://freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/List-Within-a-List-in-Python
seo_title: Liste dans une Liste en Python – Comment Initialiser une Liste Imbriquée
---

How-to-Initialize-a-Nested-List-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLes listes sont un type de données intégré en Python. Et vous pouvez\
  \ les utiliser pour stocker une collection d'éléments. \nLes listes sont ordonnées, mutables et\
  \ contiennent des éléments de différents types de données, tels que des chaînes de caractères, des entiers et d'autres\
  \ listes. \nEn Python, les listes..."
---

Par Shittu Olumide

Les listes sont un type de données intégré en Python. Et vous pouvez les utiliser pour stocker une collection d'éléments. 

Les listes sont ordonnées, mutables et contiennent des éléments de différents types de données, tels que des chaînes de caractères, des entiers et d'autres listes. 

En Python, les listes sont une structure de données fondamentale que vous utiliserez fréquemment, que vous soyez développeur web, scientifique des données ou autre.

## Comment Créer une Liste en Python

Vous pouvez créer une liste en Python en séparant les éléments par des virgules et en utilisant des crochets `[]`. Créons une liste d'exemple :

```py
maListe = [3.5, 10, "code", [1, 2, 3], 8]

```

D'après l'exemple ci-dessus, vous pouvez voir qu'une liste peut contenir plusieurs types de données. Afin d'accéder à ces éléments dans une chaîne, nous utilisons l'indexation. Le premier index est `0`, le deuxième index est `1`, et ainsi de suite. 

Les listes viennent avec une large gamme de méthodes telles que :

* `append()` : ajoute un élément à la fin de la liste.
* `insert()` : ajoute un élément à une position spécifiée dans la liste.
* `remove()` : supprime la première occurrence d'un élément spécifié de la liste.
* `pop()` : supprime l'élément à une position spécifiée dans la liste et le retourne.
* `sort()` : trie les éléments de la liste par ordre croissant.
* `reverse()` : inverse l'ordre des éléments de la liste.
* `count()` : retourne le nombre de fois qu'un élément spécifié apparaît dans la liste.
* `index()` : retourne l'index de la première occurrence d'un élément spécifié dans la liste.
* `extend()` : étend la liste en ajoutant des éléments d'un autre itérable.

En Python, vous pouvez également avoir des listes dans une liste. Et c'est ce que nous allons discuter dans la section suivante.

## Comment une Liste dans une Liste Fonctionne en Python

Une liste dans une autre liste est appelée une liste imbriquée en Python. Nous pouvons également dire qu'une liste qui a d'autres listes comme éléments est une liste imbriquée. 

Lorsque nous voulons conserver plusieurs ensembles de données connectées dans une seule liste, cela peut être utile.

Voici une illustration d'une liste imbriquée en Python :

```py
maListe = [[22, 14, 16], ["Joe", "Sam", "Abel"], [True, False, True]]

```

Comme nous l'avons dit plus tôt, pour accéder aux éléments de cette liste imbriquée, nous utilisons l'indexation. Pour accéder à un élément dans l'une des sous-listes, nous utilisons deux indices – l'index de la sous-liste et l'index de l'élément dans la sous-liste. 

Utilisons l'exemple de la liste imbriquée ci-dessus et accédons à une sous-liste/élément particulier :

```py
# impression d'une sous-liste
print(maListe[0])
[22, 14, 16]

# impression d'un élément dans une sous-liste
print(maListe[0][1]) # sortie : 14

# modification d'un élément dans une sous-liste
maListe[0][1] = 20
print(maListe) # sortie : [[22, 20, 16], ["Joe", "Sam", "Abel"], [True, False, True]]

```

Regardons comment nous pouvons initialiser correctement une liste imbriquée en Python.

## Comment Initialiser une Liste Imbriquée en Python

Nous savons qu'une liste imbriquée est une liste à l'intérieur d'une autre liste. Mais créer une liste de listes en Python peut être un peu délicat car il y a des mauvaises et des bonnes façons de le faire.

### Comment NE PAS initialiser une liste imbriquée

Voyons l'une des mauvaises façons d'initialiser une liste imbriquée (bien que ce soit la manière la plus basique et la plus rapide d'initialiser une liste imbriquée) :

```py
# Créer une liste avec 5 références de la même sous-liste
maListe = [[]] * 5
print(maListe)  # sortie : [[], [], [], [], []]

```

Initialiser une liste imbriquée de cette manière a l'inconvénient que chaque entrée dans la liste a le même `ID`, pointant vers le même objet liste. 

Vérifions cela en parcourant la liste et en imprimant l'id de chaque objet sous-liste.

```py
for objets in maListe:
    print(id(objets))

# sortie :

200792200
200792200
200792200
200792200
200792200

```

Voyons pourquoi cela est très mauvais. Nous allons insérer un élément dans la deuxième sous-liste puis vérifier le contenu de la liste principale.

```py
# Insérer 7 dans la deuxième sous-liste
maListe[1].append(7)
print(maListe)

# sortie : [[7], [7], [7], [7], [7]]

```

L'élément a été inséré dans toutes les sous-listes, car elles ont le même ID. Par conséquent, elles ne sont pas des listes différentes. Comme vous pouvez le voir, c'est une manière incorrecte d'initialiser une liste imbriquée.

### Comment initialiser une liste imbriquée

#### En utilisant la compréhension de liste et range()

En utilisant la compréhension de liste, nous pouvons créer une sous-liste et l'ajouter à la liste principale pour chaque élément d'une séquence de nombres de `0` à `n-1` que nous avons générée en utilisant la fonction `range()` de Python.

```py
maListe = [[] for i in range(5)]
print(maListe) 

# sortie : [[], [], [], [], []]

```

Cela crée une liste imbriquée qui a 5 sous-listes. Maintenant, voyons si chaque sous-liste a un ID différent. Nous allons également insérer un élément dans une sous-liste.

```py
# parcourir la liste et imprimer chaque id de sous-liste.
for objets in maListe:
    print(id(objets))
    
# sortie : 
200739688
200739944
200739848
200739912
200739880

# modifier l'élément dans une sous-liste – insérons 7 dans la deuxième sous-liste
maListe[1].append(7)
print(maListe)

# Sortie : [[], [7], [], [], []]

```

Comme vous pouvez le voir, l'élément (7) est seulement inséré dans la deuxième sous-liste et les autres sous-listes sont laissées vides car elles ont toutes des IDs ou objets différents.

#### En utilisant une boucle for

Supposons que nous voulons construire une liste qui contient quatre sous-listes différentes. Pour y parvenir, nous allons d'abord créer une nouvelle liste vide, puis utiliser une boucle for pour itérer de 0 à 3. Nous ajouterons une liste vide à la nouvelle liste après chaque itération.

```py
maListe = []
# Itérer sur une séquence de nombres de 0 à 3
for i in range(4):
    # À chaque itération, ajouter une liste vide à la liste principale
    maListe.append([])
print(maListe)

# sortie : [[], [], [], []]

```

Pour confirmer si toutes les sous-listes ont des IDs différents, vous pouvez faire ceci :

```py
for objets in maListe:
    print(id(objets))

# sortie :

200792232
200792296
200792168
200740648

```

Les IDs distincts de chaque sous-liste attestent que ce sont des objets distincts.

#### En utilisant Numpy

Le module [Numpy](https://numpy.org/) de Python inclut une fonction appelée `empty()` qui génère des tableaux Numpy vides d'une forme spécifiée. Utiliser Numpy pour initialiser une liste imbriquée peut être une manière pratique de construire et de travailler avec des structures de données bidimensionnelles en Python.

```py
import numpy 
num = 5

# Créer un tableau Numpy 2D de forme (5, 0) et le convertir en une liste imbriquée
maListe = numpy.empty((num, 0)).tolist()
print(maListe)

# sortie : [[], [], [], [], []]

```

Nous avons maintenant 5 sous-listes – vérifions leurs IDs.

```py
for objets in maListe:
    print(id(objets))

# sortie :

200739944
200739848
200739912
200740616
200739688

```

C'est une autre confirmation que toutes les sous-listes sont des objets différents. Donc si nous voulons modifier une sous-liste, les sous-listes restantes ne seront pas affectées. 

## Conclusion

Nous sommes arrivés à la fin de cet article. Les points clés à retenir sont que l'initialisation d'une liste imbriquée peut être délicate - et il y a une manière incorrecte (et plusieurs manières correctes) de le faire. 

Il existe de nombreuses autres façons d'initialiser une liste imbriquée en Python, mais celles ci-dessus sont les plus populaires et les plus largement utilisées. 

Une fois que nous avons créé la liste imbriquée, nous pouvons accéder et modifier ses éléments en utilisant l'indexation comme vous l'avez vu ci-dessus. 

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !