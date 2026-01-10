---
title: Series et DataFrame en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T20:03:08.000Z'
originalURL: https://freecodecamp.org/news/series-and-dataframe-in-python-a800b098f68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QH4RGlNwXUFnJSytytvb6A.jpeg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: technology
  slug: technology
- name: women in tech
  slug: women-in-tech
seo_title: Series et DataFrame en Python
seo_desc: 'By Shubhi Asthana

  A couple of months ago, I took the online course “Using Python for Research” offered
  by Harvard University on edX. While taking the course, I learned many concepts of
  Python, NumPy, Matplotlib, and PyPlot. I also had an opportunity ...'
---

Par Shubhi Asthana

Il y a quelques mois, j'ai suivi le cours en ligne "Using Python for Research" proposé par l'Université Harvard sur edX. Pendant ce cours, j'ai appris de nombreux concepts de Python, NumPy, Matplotlib et PyPlot. J'ai également eu l'opportunité de travailler sur des études de cas pendant ce cours et j'ai pu appliquer mes connaissances sur des ensembles de données réels. Pour plus d'informations sur ce programme, consultez [ici](https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/4bdcc373b7a944f8861a3f190c10edca/).

J'ai appris deux concepts importants dans ce cours — Series et DataFrame. Je souhaite vous les présenter à travers un court tutoriel.

Pour commencer le tutoriel, obtenons le dernier code source de Python depuis le site officiel [ici](https://www.python.org/).

Une fois Python installé, vous utiliserez une interface graphique appelée [IDLE](https://www.python.org/downloads/) pour travailler avec Python.

Importons Pandas dans notre espace de travail. [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) est une bibliothèque Python qui fournit des structures de données et des outils d'analyse de données pour différentes fonctions.

### **Series**

Une Series est un objet unidimensionnel qui peut contenir n'importe quel type de données tel que des entiers, des flottants et des chaînes de caractères. Prenons une liste d'éléments comme argument d'entrée et créons un objet Series pour cette liste.

```
>>> import pandas as pd
```

```
>>> x = pd.Series([6,3,4,6])
```

```
>>> x
```

```
0 6
```

```
1 3
```

```
2 4
```

```
3 6
```

```
dtype: int64
```

Les étiquettes d'axe pour les données sont appelées index. La longueur de l'index doit être la même que la longueur des données. Comme nous n'avons pas passé d'index dans le code ci-dessus, l'index par défaut sera créé avec les valeurs `[0, 1, … len(data) -1]`.

Allons-y et définissons des index pour les données.

```
>>> x = pd.Series([6,3,4,6], index=['a', 'b', 'c', 'd'])
```

```
>>> x
```

```
a 6
```

```
b 3
```

```
c 4
```

```
d 6
```

```
dtype: int64
```

L'index dans la colonne la plus à gauche fait maintenant référence aux données dans la colonne de droite.

Nous pouvons rechercher les données en faisant référence à leur index :

```
>>> x["c"]
```

```
4
```

Python nous donne les données pertinentes pour l'index.

Un exemple de type de données est le dictionnaire défini ci-dessous. L'index et les valeurs correspondent aux clés et aux valeurs. Nous pouvons utiliser l'index pour obtenir les valeurs des données correspondant aux étiquettes de l'index.

```
>>> data = {'abc': 1, 'def': 2, 'xyz': 3}
```

```
>>> pd.Series(data)
```

```
abc 1
```

```
def 2
```

```
xyz 3
```

```
dtype: int64
```

Une autre caractéristique intéressante des Series est d'avoir des données sous forme de valeur scalaire. Dans ce cas, la valeur des données est répétée pour chacun des index définis.

```
>>> x = pd.Series(3, index=['a', 'b', 'c', 'd'])
```

```
>>> x
```

```
a 3
```

```
b 3
```

```
c 3
```

```
d 3
```

```
dtype: int64
```

### **DataFrame**

Un DataFrame est un objet bidimensionnel qui peut avoir des colonnes de types potentiellement différents. Différents types d'entrées incluent des dictionnaires, des listes, des séries, et même un autre DataFrame.

C'est l'objet pandas le plus couramment utilisé.

Allons-y et créons un DataFrame en passant un tableau NumPy avec des dates comme index et des colonnes étiquetées :

```
>>> import numpy as np
```

```
>>> dates = pd.date_range('20170505', periods = 8)
```

```
>>> dates
```

```
DatetimeIndex(['2017–05–05', '2017–05–06', '2017–05–07', '2017–05–08',
```

```
'2017–05–09', '2017–05–10', '2017–05–11', '2017–05–12'],
```

```
dtype='datetime64[ns]', freq='D')
```

```
>>> df = pd.DataFrame(np.random.randn(8,3), index=dates, columns=list('ABC'))
```

```
>>> df
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.613538 -0.052423 -1.206090
```

```
2017–05–07 0.772951 0.835798 0.345913
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
2017–05–10 0.275916 -0.420183 1.744796
```

```
2017–05–11 -0.206065 0.910706 -0.028646
```

```
2017–05–12 1.178219 0.783122 0.829979
```

Un DataFrame avec une plage de dates de 8 jours est créé comme montré ci-dessus. Nous pouvons afficher les lignes du haut et du bas du cadre en utilisant `df.head` et `df.tail` :

```
>>> df.head()
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.613538 -0.052423 -1.206090
```

```
2017–05–07 0.772951 0.835798 0.345913
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
>>> df.tail()
```

```
A B C
```

```
2017–05–08 1.339559 0.900384 -1.037658
```

```
2017–05–09 -0.695919 1.372793 0.539752
```

```
2017–05–10 0.275916 -0.420183 1.744796
```

```
2017–05–11 -0.206065 0.910706 -0.028646
```

```
2017–05–12 1.178219 0.783122 0.829979
```

Nous pouvons également observer un résumé statistique rapide de nos données :

```
>>> df.describe()
```

```
A B C
```

```
count 8.000000 8.000000 8.000000
```

```
mean 0.372040 0.729842 -0.109691
```

```
std 0.731262 0.657931 1.244801
```

```
min -0.695919 -0.420183 -2.065571
```

```
25% -0.230018 0.574236 -1.079766
```

```
50% 0.444727 0.868091 0.158633
```

```
75% 0.874268 1.026228 0.612309
```

```
max 1.339559 1.508536 1.744796
```

Nous pouvons également appliquer des fonctions aux données comme la somme cumulative, afficher des histogrammes, fusionner des DataFrames, concaténer et remodeler des DataFrames.

```
>>> df.apply(np.cumsum)
```

```
A B C
```

```
2017–05–05 -0.301877 1.508536 -2.065571
```

```
2017–05–06 0.311661 1.456113 -3.271661
```

```
2017–05–07 1.084612 2.291911 -2.925748
```

```
2017–05–08 2.424171 3.192296 -3.963406
```

```
2017–05–09 1.728252 4.565088 -3.423654
```

```
2017–05–10 2.004169 4.144905 -1.678858
```

```
2017–05–11 1.798104 5.055611 -1.707504
```

```
2017–05–12 2.976322 5.838734 -0.877526
```

Vous pouvez lire plus de détails sur ces structures de données [ici](http://pandas.pydata.org/pandas-docs/stable/dsintro.html).