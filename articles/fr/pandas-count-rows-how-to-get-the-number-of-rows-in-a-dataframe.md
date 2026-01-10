---
title: Pandas Compter les Lignes – Comment Obtenir le Nombre de Lignes dans un Dataframe
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-19T15:11:58.000Z'
originalURL: https://freecodecamp.org/news/pandas-count-rows-how-to-get-the-number-of-rows-in-a-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/nacho-capelo-hMXuZrfmCWM-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Pandas Compter les Lignes – Comment Obtenir le Nombre de Lignes dans un
  Dataframe
seo_desc: "Pandas is a library built on the Python programming language. You can use\
  \ it to analyze and manipulate data.\nA dataframe is two-dimensional data structure\
  \ in Pandas that organizes data in a tabular format with rows and columns. \nIn\
  \ this article, you'..."
---

Pandas est une bibliothèque construite sur le langage de programmation Python. Vous pouvez l'utiliser pour analyser et manipuler des données.

Un dataframe est une structure de données bidimensionnelle dans Pandas qui organise les données dans un format tabulaire avec des lignes et des colonnes.

Dans cet article, vous apprendrez comment obtenir le nombre de lignes dans un dataframe en utilisant les éléments suivants :

* La fonction `len()`.
* L'attribut `shape`.
* L'attribut `index`.
* L'attribut `axes`.

## Comment Obtenir le Nombre de Lignes dans un Dataframe en Utilisant la Fonction `len()`

Vous pouvez utiliser la fonction `len()` pour retourner la longueur d'un objet. Avec un dataframe, la fonction retourne le nombre de lignes.

Considérez le dataframe ci-dessous :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df
```

|    |      name        |  age |
|----------|:-------------:|------:|
| 0 |  John  | 2 |
| 1 |    Jane | 10 |
| 2 | Jade | 3 |

Dans l'exemple ci-dessus, nous avons créé un dataframe avec trois lignes — ligne 0, 1 et 2.

Vous pouvez utiliser la fonction `len()` pour vérifier le nombre de lignes :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df)

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

Dans le code ci-dessus, nous avons passé le dataframe en tant que paramètre à la fonction `len()` et l'avons stocké dans une variable appelée `num_of_rows` :

```python
num_of_rows = len(df)
```

Lorsque `num_of_rows` a été imprimé, nous avons obtenu une valeur de 3 (le nombre de lignes).

## Comment Obtenir le Nombre de Lignes dans un Dataframe en Utilisant l'Attribut `shape`

L'attribut `shape` retourne un tuple avec le nombre de lignes et de colonnes dans un dataframe.

Voici un exemple utilisant le même dataframe que dans la dernière section :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.shape

print(num_of_rows)
# (3, 2)
```

Dans le code ci-dessus, un tuple — (3, 2) — a été retourné lorsque nous avons utilisé l'attribut `shape` sur le dataframe : `df.shape`.

La première valeur, 3, est le nombre de lignes dans le dataframe tandis que la deuxième valeur, 2, est le nombre de colonnes.

Puisque nous ne sommes intéressés que par le nombre de lignes, nous pouvons extraire uniquement cette valeur en utilisant son index dans le tuple (rappelons que les numéros d'index commencent à 0). C'est-à-dire :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.shape[0]

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

Maintenant, nous obtenons uniquement le nombre de lignes en utilisant son index dans le tuple : `df.shape[0]`.

## Comment Obtenir le Nombre de Lignes dans un Dataframe en Utilisant l'Attribut `index`

Vous pouvez utiliser l'attribut `index` pour accéder au nombre d'éléments dans un dataframe, ce qui correspond au nombre de lignes.

Vous pouvez faire cela de deux manières différentes :

* En utilisant la propriété `size` de l'attribut `index`.
* En passant la propriété `index` en tant que paramètre à la fonction `len()`.

Voici des exemples pour expliquer les méthodes ci-dessus :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.index.size

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

Dans l'exemple ci-dessus, nous avons accédé au nombre de lignes dans le dataframe en utilisant `df.index.size`.

Sans la propriété `size`, vous obtiendriez un résultat comme ceci : `RangeIndex(start=0, stop=3, step=1)`.

* `start` désigne le premier numéro d'index.
* `stop` désigne le nombre de lignes dans le dataframe.
* `step` désigne la manière dont les index sont incrémentés (les index sont augmentés de 1 dans notre cas).

Ainsi, la propriété `size` est une manière de spécifier que vous êtes uniquement intéressé par le nombre d'éléments dans le dataframe.

Voici un autre exemple qui utilise la fonction `len()` :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df.index)

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

Dans le code ci-dessus, nous avons passé `df.index` en tant que paramètre à la fonction `len()`. Cela retourne le nombre de lignes dans le dataframe.

La différence entre cet exemple et le précédent est que nous n'attachons pas la propriété `size` à `df.index`. Au lieu de cela, nous utilisons `df.index` comme paramètre de la fonction `len()`.

## Comment Obtenir le Nombre de Lignes dans un Dataframe en Utilisant l'Attribut `axes`

L'attribut `axes` retourne la valeur comme l'attribut `index` : `RangeIndex(start=0, stop=3, step=1)`.

De même, vous pouvez retourner le nombre de lignes en utilisant soit la propriété `size`, soit la fonction `len()` :

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = df.axes[0].size

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

```python
import pandas as pd

data = {
  "name": ["John", "Jane", "Jade"],
  "age": [2, 10, 3]
}

df = pd.DataFrame(data)
df

num_of_rows = len(df.axes[0])

print(f"Le nombre de lignes est {num_of_rows}")
# Le nombre de lignes est 3
```

La logique dans les deux blocs de code ci-dessus est la même que celle de la dernière section :

* `df.index.size` retourne le nombre d'éléments/lignes dans le dataframe.
* `len(df.index)` retourne le nombre de lignes dans le dataframe.

## Résumé

Dans cet article, nous avons parlé des dataframes dans Pandas. Ce sont des structures de données bidimensionnelles qui organisent les données en lignes et en colonnes.

Nous avons vu différentes méthodes pour obtenir le nombre de lignes dans un dataframe. Nous avons discuté des méthodes suivantes avec des exemples de code pour montrer leur application :

* La fonction `len()`.
* L'attribut `shape`.
* L'attribut `index`.
* L'attribut `axes`.

Bon codage ! Vous pouvez en apprendre plus sur Python sur [mon blog](https://ihechikara.com/).