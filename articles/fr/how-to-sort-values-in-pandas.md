---
title: pandas.DataFrame.sort_values - Comment trier des valeurs dans Pandas
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-13T21:52:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-values-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/sort-in-pandas-1.png
tags:
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: pandas.DataFrame.sort_values - Comment trier des valeurs dans Pandas
seo_desc: 'When analyzing and manipulating data using Pandas, you might want to sort
  the data in a certain order. This makes it easier to understand and visualize data.

  In this article, you''ll learn how to sort data in ascending and descending order
  using Panda...'
---

Lors de l'analyse et de la manipulation de données avec Pandas, vous pourriez vouloir trier les données dans un certain ordre. Cela facilite la compréhension et la visualisation des données.

Dans cet article, vous apprendrez comment trier des données par ordre croissant et décroissant en utilisant la méthode `sort_values()` de Pandas.

## Comment trier des valeurs dans Pandas

Vous pouvez utiliser la méthode `sort_values()` pour trier les valeurs d'un ensemble de données. Par défaut, la méthode trie les valeurs par ordre croissant.

Dans cette section, vous apprendrez comment trier des données par ordre croissant et décroissant à l'aide de la méthode `sort_values()`.

### Comment trier des valeurs par ordre croissant à l'aide de la méthode `sort_values()` de Pandas

La méthode `sort_values()` prend plusieurs paramètres, comme on peut le voir dans la [documentation de Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html).

Nous nous concentrerons sur les paramètres `by` et `ascending`. C'est-à-dire :

```txt
Dataframe.sort_values(by, ascending)
```

* Le paramètre `by` indique la colonne ou l'index à trier.
* `ascending` est utilisé pour spécifier l'ordre dans lequel les valeurs doivent être triées. Par défaut, il est défini sur `True`.

Voici un exemple :

```python
import pandas as pd

# créer un exemple de dataframe
data = {'cost': [50000, 30000, 70000, 60000]}

df = pd.DataFrame(data)

df
```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 0 | laptop | 500 |
| 1 | monitor | 300 |
| 2 | HDMI | 700 |
| 3 | speaker | 600 |

Dans le tableau ci-dessus, nous avons différents articles ainsi que le coût de chaque article. Pour trier les articles par ordre croissant en utilisant leur coût, vous pouvez faire ceci :

```python
import pandas as pd

data = {'item': ['laptop', 'monitor', 'HDMI', 'speaker'],
        'cost': [500, 300, 700, 600]
       }

df = pd.DataFrame(data)

sorted_data = df.sort_values(by='cost', ascending=True)

sorted_data


```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 1 | monitor | 300 |
| 0 | laptop | 500 |
| 3 | speaker | 600 |
| 2 | HDMI | 700 |

Dans le code ci-dessus, la méthode `sort_values()` a été utilisée pour trier la colonne `cost`.

* En utilisant le paramètre `by`, nous avons spécifié quelle colonne devait être triée : `by='cost'`
* En utilisant le paramètre `ascending`, nous avons défini l'ordre des données à trier : `ascending=True`.

Notez que l'ordre par défaut de la méthode `sort_values()` est `ascending=True`. Donc, si vous supprimez le paramètre `ascending`, les valeurs seront toujours triées par ordre croissant.

### Comment trier des valeurs par ordre décroissant à l'aide de la méthode `sort_values()` de Pandas

Vous pouvez trier les valeurs par ordre décroissant en définissant simplement le paramètre `ascending` sur `False`.

Nous travaillerons avec le même code que dans la section précédente :

```python
import pandas as pd

# créer un exemple de dataframe
data = {'cost': [50000, 30000, 70000, 60000]}

df = pd.DataFrame(data)

df
```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 0 | laptop | 500 |
| 1 | monitor | 300 |
| 2 | HDMI | 700 |
| 3 | speaker | 600 |

Voici le code pour trier la colonne `cost` par ordre décroissant :

```python
import pandas as pd

data = {'item': ['laptop', 'monitor', 'HDMI', 'speaker'],
        'cost': [500, 300, 700, 600]
       }

df = pd.DataFrame(data)

sorted_data = df.sort_values(by='cost', ascending=False)

sorted_data


```

|    |      item      |  cost |
|----------|:-------------:|------:|
| 2 | HDMI | 700 |
| 3 | speaker | 600 |
| 0 | laptop | 500 |
| 1 | monitor | 300 |

En définissant la valeur du paramètre `ascending` sur `False`, nous avons trié les données par coût dans l'ordre décroissant.

## Résumé

Dans cet article, nous avons appris à trier des valeurs dans Pandas à l'aide de la méthode `sort_values()`.

Nous avons vu deux exemples de code sur la façon de trier des données dans Pandas par ordre croissant ou décroissant.

Vous pouvez utiliser le paramètre `ascending` de la méthode `sort_values()` pour trier les données par ordre croissant ou décroissant.

Bon codage !