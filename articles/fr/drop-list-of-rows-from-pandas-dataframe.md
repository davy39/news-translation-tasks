---
title: Analyse de données avec Pandas – Comment supprimer une liste de lignes d'un
  DataFrame Pandas
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2021-06-01T20:47:43.000Z'
originalURL: https://freecodecamp.org/news/drop-list-of-rows-from-pandas-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/cut_lemons--1-.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: dataframe
  slug: dataframe
- name: pandas
  slug: pandas
seo_title: Analyse de données avec Pandas – Comment supprimer une liste de lignes
  d'un DataFrame Pandas
seo_desc: 'A Pandas dataframe is a two dimensional data structure which allows you
  to store data in rows and columns. It''s very useful when you''re analyzing data.

  When you have a list of data records in a dataframe, you may need to drop a specific
  list of rows ...'
---

Un DataFrame Pandas est une structure de données bidimensionnelle qui permet de stocker des données en lignes et en colonnes. Il est très utile lors de l'analyse de données.

Lorsque vous avez une liste d'enregistrements de données dans un DataFrame, vous pouvez avoir besoin de supprimer une liste spécifique de lignes en fonction des besoins de votre modèle et de vos objectifs lors de l'étude de vos analyses. 

Dans ce tutoriel, vous apprendrez à supprimer une liste de lignes d'un DataFrame Pandas. 

Pour apprendre à supprimer des colonnes, vous pouvez lire ici [Comment supprimer des colonnes dans Pandas](https://www.stackvidhya.com/drop-column-in-pandas/). 

## Comment supprimer une ligne ou une colonne dans un DataFrame Pandas

Pour supprimer une ligne ou une colonne dans un DataFrame, vous devez utiliser la méthode `drop()` disponible dans le DataFrame. Vous pouvez lire plus sur la méthode `drop()` dans la documentation [ici](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html). 

**Axe du DataFrame**

 - Les lignes sont désignées par `axis=0`
 - Les colonnes sont désignées par `axis=1`

**Étiquettes du DataFrame**

 - Les lignes sont étiquetées par le numéro d'index commençant par 0, par défaut.
 - Les colonnes sont étiquetées par des noms. 

**Paramètres de la méthode Drop()**

 - `index` - la liste des lignes à supprimer
 - `axis=0` - Marque les lignes dans le DataFrame à supprimer
 - `inplace=True` - Effectue l'opération de suppression dans le même DataFrame, plutôt que de créer un nouvel objet DataFrame lors de l'opération de suppression. 

### Exemple de DataFrame Pandas

Notre DataFrame exemple contient les colonnes *product_name*, *Unit_Price*, *No_Of_Units*, *Available_Quantity*, et *Available_Since_Date*. Il contient également des lignes avec des valeurs NaN qui sont utilisées pour désigner les valeurs manquantes. 

```python
import pandas as pd

data = {"product_name":["Keyboard","Mouse", "Monitor", "CPU","CPU", "Speakers",pd.NaT],
        "Unit_Price":[500,200, 5000.235, 10000.550, 10000.550, 250.50,None],
        "No_Of_Units":[5,5, 10, 20, 20, 8,pd.NaT],
        "Available_Quantity":[5,6,10,"Not Available","Not Available", pd.NaT,pd.NaT],
        "Available_Since_Date":['11/5/2021', '4/23/2021', '08/21/2021','09/18/2021','09/18/2021','01/05/2021',pd.NaT]
       }

df = pd.DataFrame(data)

df
```

Le DataFrame ressemblera à ceci :

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.000</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.000</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Monitor</td>
      <td>5000.235</td>
      <td>10</td>
      <td>10</td>
      <td>08/21/2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Speakers</td>
      <td>250.500</td>
      <td>8</td>
      <td>NaT</td>
      <td>01/05/2021</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaT</td>
      <td>NaT</td>
      <td>NaT</td>
    </tr>
  </tbody>
</table>
</div>

Et voilà, nous avons créé notre DataFrame exemple. 

Après chaque opération de suppression, vous imprimerez le DataFrame en utilisant `df`, ce qui imprimera le DataFrame dans un format de tableau `HTML` régulier. 

Vous pouvez lire ici comment [Imprimer joliment un DataFrame](https://www.stackvidhya.com/pretty-print-dataframe/) pour imprimer le DataFrame dans différents formats visuels. 

Ensuite, vous apprendrez à supprimer une liste de lignes dans différents cas d'utilisation. 

## Comment supprimer une liste de lignes par index dans Pandas

Vous pouvez supprimer une liste de lignes de Pandas en passant la liste des index à la méthode `drop()`. 

```python
df.drop([5,6], axis=0, inplace=True)

df
```

Dans ce code,

 - `[5,6]` est l'index des lignes que vous souhaitez supprimer
 - `axis=0` indique que les lignes doivent être supprimées du DataFrame
 - `inplace=True` effectue l'opération de suppression dans le même DataFrame

Après avoir supprimé les lignes avec l'index 5 et 6, vous aurez les données suivantes dans le DataFrame :


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.000</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.000</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Monitor</td>
      <td>5000.235</td>
      <td>10</td>
      <td>10</td>
      <td>08/21/2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.550</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
  </tbody>
</table>
</div>

C'est ainsi que vous pouvez supprimer des lignes avec un index spécifique. 

Ensuite, vous apprendrez à supprimer une plage d'index. 

## Comment supprimer des lignes par plage d'index dans Pandas

Vous pouvez également supprimer une liste de lignes dans une plage spécifique. 

Une plage est un ensemble de valeurs avec une limite inférieure et une limite supérieure. 

Cela peut être utile dans les cas où vous souhaitez créer un ensemble de données d'exemple en excluant des plages spécifiques de données. 

Vous pouvez créer une plage de lignes dans un DataFrame en utilisant la méthode `df.index()`. Ensuite, vous pouvez passer cette plage à la méthode `drop()` pour supprimer les lignes comme montré ci-dessous. 

```python
df.drop(df.index[2:4], inplace=True)

df
```

Voici ce que fait ce code :

 - `df.index[2:4]` génère une plage de lignes de 2 à 4. La limite inférieure de la plage est inclusive et la limite supérieure de la plage est exclusive. Cela signifie que les lignes 2 et 3 seront supprimées et que la ligne 4 ne sera *pas* supprimée. 
 - `inplace=True` effectue l'opération de suppression dans le même DataFrame

Après avoir supprimé les lignes dans la plage 2-4, vous aurez les données suivantes dans le DataFrame :

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.00</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.00</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CPU</td>
      <td>10000.55</td>
      <td>20</td>
      <td>Not Available</td>
      <td>09/18/2021</td>
    </tr>
  </tbody>
</table>
</div>

C'est ainsi que vous pouvez supprimer la liste de lignes dans le DataFrame en utilisant sa plage. 

## Comment supprimer toutes les lignes après un index dans Pandas

Vous pouvez supprimer toutes les lignes après un index spécifique en utilisant `iloc[]`. 

Vous pouvez utiliser `iloc[]` pour sélectionner des lignes en utilisant leur index de position. Vous pouvez spécifier le début et la fin de la position séparés par un `:`. Par exemple, vous utiliserez `2:3` pour sélectionner les lignes de 2 à 3. Si vous souhaitez sélectionner toutes les lignes, vous pouvez simplement utiliser `:` dans `iloc[]`. 

Cela peut être utile dans les cas où vous souhaitez diviser l'ensemble de données à des fins d'entraînement et de test. 

Utilisez le code suivant pour sélectionner les lignes de 0 à l'index 2. Cela entraîne la suppression des lignes après l'index 2. 

```python
df = df.iloc[:2]

df
```

Dans ce code, `:2` sélectionne les lignes jusqu'à l'index 2. 

C'est ainsi que vous pouvez supprimer toutes les lignes après un index spécifique. 

Après avoir supprimé les lignes après l'index 2, vous aurez les données suivantes dans le DataFrame :

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Keyboard</td>
      <td>500.0</td>
      <td>5</td>
      <td>5</td>
      <td>11/5/2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.0</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
  </tbody>
</table>
</div>

C'est ainsi que vous pouvez supprimer les lignes après un index spécifique. 

Ensuite, vous apprendrez à supprimer des lignes avec des conditions. 

## Comment supprimer des lignes avec plusieurs conditions dans Pandas

Vous pouvez supprimer des lignes dans le DataFrame en fonction de conditions spécifiques. 

Par exemple, vous pouvez supprimer des lignes où la valeur de la colonne est supérieure à *X* et inférieure à *Y*. 

Cela peut être utile dans les cas où vous souhaitez créer un ensemble de données qui ignore les colonnes avec des valeurs spécifiques. 

Pour supprimer des lignes en fonction de certaines conditions, sélectionnez l'index des lignes qui passent la condition spécifique et passez cet index à la méthode `drop()`.  

```python
df.drop(df[(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)].index, inplace=True)

df
```

Dans ce code, 

 - `(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)` est la condition pour supprimer les lignes. 
 - `df[].index` sélectionne l'index des lignes qui passent la condition. 
 - `inplace=True` effectue l'opération de suppression dans le même DataFrame plutôt que d'en créer un nouveau.

Après avoir supprimé les lignes avec la condition qui a le `unit_price` supérieur à 400 et inférieur à 600, vous aurez les données suivantes dans le DataFrame :

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_name</th>
      <th>Unit_Price</th>
      <th>No_Of_Units</th>
      <th>Available_Quantity</th>
      <th>Available_Since_Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Mouse</td>
      <td>200.0</td>
      <td>5</td>
      <td>6</td>
      <td>4/23/2021</td>
    </tr>
  </tbody>
</table>
</div>

C'est ainsi que vous pouvez supprimer des lignes dans le DataFrame en utilisant certaines conditions. 

## Conclusion

Pour résumer, dans cet article, vous avez appris ce qu'est la méthode `drop()` dans un DataFrame Pandas. Vous avez également vu comment les lignes et les colonnes du DataFrame sont étiquetées. Et enfin, vous avez appris à supprimer des lignes en utilisant des index, une plage d'index et en fonction de conditions. 

Si vous avez aimé cet article, n'hésitez pas à le partager. 

### Vous pourriez également aimer

- [Comment ajouter une colonne à un DataFrame dans Pandas](https://www.stackvidhya.com/add-column-to-dataframe/)
 - [Comment renommer une colonne dans Pandas](https://www.stackvidhya.com/rename-column-in-pandas/)