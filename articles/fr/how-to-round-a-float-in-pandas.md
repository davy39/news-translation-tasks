---
title: Méthode round() de Pandas – Comment arrondir un flottant dans Pandas
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-13T21:49:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-a-float-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/round-float-in-pandas.png
tags:
- name: float
  slug: float
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Méthode round() de Pandas – Comment arrondir un flottant dans Pandas
seo_desc: "You can use the Pandas library in Python to manipulate and analyze data.\
  \ In most cases, it is used for manipulating and analyzing tabular data. \nIn this\
  \ article, you'll learn how to use the Pandas round() method to round a float value\
  \ to a specified ..."
---

Vous pouvez utiliser la bibliothèque Pandas en Python pour manipuler et analyser des données. Dans la plupart des cas, elle est utilisée pour manipuler et analyser des données tabulaires. 

Dans cet article, vous apprendrez à utiliser la méthode `round()` de Pandas pour arrondir une valeur flottante à un nombre spécifique de décimales. 

Nous commencerons par examiner la syntaxe de la méthode, puis nous verrons quelques applications pratiques du code. 

## Exemple de la méthode round() de Pandas

Voici à quoi ressemble la syntaxe de la méthode `round()` :

```txt
DataFrame.round(decimals)
```

Le paramètre **decimals** représente le nombre de décimales auxquelles un nombre doit être arrondi.

Le nombre de décimales à retourner est passé en tant que paramètre. `round(2)` retourne un arrondi à deux décimales. 

Voici un exemple pour illustrer :

```python
import pandas as pd

data = {'cost':[20.5550, 21.03535, 19.67373, 18.233233]}
  
df = pd.DataFrame(data)

# Arrondir à 2 décimales
df['rounded_cost'] = df['cost'].round(2)
print(df)
```

Dans le code ci-dessus, nous avons une liste de nombres qui se trouvent dans la colonne `cost`. La colonne contient ces valeurs : [20.5550, 21.03535, 19.67373, 18.233233]. 

En utilisant la méthode `round()`, nous avons arrondi les valeurs à 2 décimales : `df['cost'].round(2)`. 

Les valeurs de retour ont été stockées dans une colonne appelée `rounded_cost`. 

Voici le résultat du code :

|    |      cost      |  rounded_cost |
|----------|:-------------:|------:|
| 0 | 20.555000 | 20.56 |
| 1 | 21.035350 | 21.04 |
| 2 | 19.673730 | 19.67 |
| 3 | 18.233233 | 18.23 |

Dans le tableau ci-dessus, vous pouvez voir que les valeurs de la colonne `cost` ont été arrondies à 2 décimales dans la colonne `rounded_cost`. 

## Résumé

Dans cet article, nous avons appris à arrondir des valeurs flottantes avec Pandas en utilisant la méthode `round()`. 

Nous avons commencé par examiner la syntaxe de la méthode `round()`. Nous avons ensuite vu un exemple utilisant la méthode pour arrondir des valeurs flottantes à un nombre spécifique de décimales. 

Bon codage !