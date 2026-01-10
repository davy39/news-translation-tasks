---
title: Comment renommer une colonne dans Pandas – Tutoriel de renommage de Dataframe
  Python Pandas
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-13T18:18:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-a-column-in-pandas
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/how-to-rename-column-in-pandas.svg
tags:
- name: Data Science
  slug: data-science
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Comment renommer une colonne dans Pandas – Tutoriel de renommage de Dataframe
  Python Pandas
seo_desc: "A Pandas Dataframe is a 2-dimensional data structure that displays data\
  \ in tables with rows and columns. \nIn this article, you'll learn how to rename\
  \ columns in a Pandas Dataframe by using: \n\nThe rename() function.\nA List.\n\
  The set_axis() function.\n\nH..."
---

Un Dataframe Pandas est une structure de données bidimensionnelle qui affiche les données dans des tableaux avec des lignes et des colonnes. 

Dans cet article, vous apprendrez à renommer des colonnes dans un Dataframe Pandas en utilisant : 

* La fonction `rename()`.
* Une liste.
* La fonction `set_axis()`.

## Comment renommer une colonne dans Pandas en utilisant la fonction `rename()`

Dans cette section, vous verrez un exemple pratique de renommage d'un Dataframe Pandas en utilisant la fonction `rename()`. 

Commençons par passer des données dans un objet Dataframe : 

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convertir les noms des étudiants en Dataframe
df = pd.DataFrame(students)

print(df)
```

```txt
# Sortie
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

Dans l'exemple ci-dessus, nous avons créé un dictionnaire Python que nous avons utilisé pour stocker les `firstname` et `lastname` des étudiants. 

Nous avons ensuite converti le dictionnaire en Dataframe en le passant comme paramètre à l'objet Dataframe Pandas : `pd.DataFrame(students)`. 

Lorsque nous l'avons imprimé dans la console, nous avons obtenu ce tableau :

```txt
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

Le but ici est de renommer les colonnes. Nous pouvons le faire en utilisant la fonction `rename()`. 

### **Voici à quoi ressemble la syntaxe :**

```
df.rename(columns={"OLD_COLUMN_VALUE": "NEW_COLUMN_VALUE"})
```

Allons-y et changeons les noms des colonnes (`firstname` et `lastname`) dans le tableau de minuscules en majuscules (`FIRSTNAME` et `LASTNAME`). 

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convertir les noms des étudiants en Dataframe
df = pd.DataFrame(students)

df.rename(columns={"firstname": "FIRSTNAME", "lastname": "LASTNAME"}, inplace=True)

print(df)
```

```txt
# Sortie
  FIRSTNAME LASTNAME
0      John      Doe
1      Jane     Done
2      Jade       Do
```

Dans le code ci-dessus, nous avons spécifié que les colonnes `firstname` et `lastname` devaient être renommées en `FIRSTNAME` et `LASTNAME`, respectivement : `df.rename(columns={"firstname": "FIRSTNAME", "lastname": "LASTNAME"}, inplace=True)`

Vous remarquerez que nous avons ajouté le paramètre `inplace=True`. Cela aide à persister les nouvelles modifications dans le Dataframe. Supprimez le paramètre et voyez ce qui se passe ;)

Vous pouvez renommer les colonnes comme vous le souhaitez. Par exemple, nous pouvons utiliser `SURNAME` au lieu de `lastname` en faisant ceci :

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convertir les noms des étudiants en Dataframe
df = pd.DataFrame(students)
df.rename(columns={"firstname": "FIRSTNAME", "lastname": "SURNAME"}, inplace=True)

print(df)
```

```txt
# Sortie
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

Vous pouvez également changer un seul nom de colonne. Vous n'êtes pas obligé de changer tous les noms de colonnes en même temps. 

## Comment renommer une colonne dans Pandas en utilisant une liste

Vous pouvez accéder aux noms des colonnes d'un Dataframe en utilisant `df.columns`. Considérez le tableau ci-dessous :

```txt
  firstname lastname
0      John      Doe
1      Jane     Done
2      Jade       Do
```

Nous pouvons imprimer les noms des colonnes avec le code ci-dessous :

```python 
print(df.columns)

# Index(['firstname', 'lastname'], dtype='object')
```

En utilisant cela, nous pouvons renommer la colonne d'un Dataframe. Voici un exemple :

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convertir les noms des étudiants en Dataframe
df = pd.DataFrame(students)
df.columns = ["FIRSTNAME", "SURNAME"]

print(df)
```

```txt
# Sortie
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

Dans l'exemple ci-dessus, nous avons mis les nouveaux noms de colonnes dans une liste et nous les avons assignés aux colonnes du Dataframe : `df.columns = ["FIRSTNAME", "SURNAME"]`. 

Cela remplacera les anciens noms de colonnes. 

## Comment renommer une colonne dans Pandas en utilisant la fonction `set_axis()`

La syntaxe pour renommer une colonne avec la fonction `set_axis()` ressemble à ceci :

```
df.set_axis([NEW_COLUMN_NAME,...], axis="columns")
```

Voici un exemple de code :

```python
import pandas as pd

students = {
    "firstname": ["John", "Jane", "Jade"], 
    "lastname": ["Doe", "Done", "Do"]
}

# convertir les noms des étudiants en Dataframe
df = pd.DataFrame(students)

df.set_axis(["FIRSTNAME", "SURNAME"], axis="columns", inplace=True) 

print(df)
```

```txt
# Sortie
  FIRSTNAME SURNAME
0      John     Doe
1      Jane    Done
2      Jade      Do
```

Notez que le paramètre `inplace=True` peut déclencher un avertissement car il est obsolète pour la fonction `set_axis()` et sera remplacé à l'avenir. 

## Résumé

Dans cet article, nous avons parlé du renommage d'une colonne dans Pandas. 

Nous avons vu différentes méthodes qui peuvent être utilisées pour renommer une colonne de Dataframe Pandas avec des exemples de code. 

Bon codage !