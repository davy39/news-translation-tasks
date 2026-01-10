---
title: Comment automatiser les tâches Excel avec Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-01T19:04:17.000Z'
originalURL: https://freecodecamp.org/news/automate-excel-tasks-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/FreecodeCamp.png
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: Python
  slug: python
seo_title: Comment automatiser les tâches Excel avec Python
seo_desc: 'Excel is a surprisingly common tool for data analysis.

  Data analysts can readily modify, examine, and display huge amounts of data with
  Excel, which makes it simpler to gain insights and make wise choices.

  Excel''s versatility lets users carry out a v...'
---

Excel est un outil surprenamment courant pour l'analyse de données.

Les analystes de données peuvent facilement modifier, examiner et afficher de grandes quantités de données avec Excel, ce qui simplifie l'obtention d'informations et la prise de décisions judicieuses.

La polyvalence d'Excel permet aux utilisateurs d'effectuer une variété de tâches d'analyse de données, des opérations mathématiques simples aux analyses statistiques complexes. De plus, Excel offre des possibilités d'automatisation grâce à l'utilisation de programmes tiers comme Python ou le langage de programmation intégré VBA.

Excel est fréquemment utilisé pour l'analyse de données dans divers secteurs, notamment la banque, la santé et le marketing, grâce à sa polyvalence et à sa facilité d'utilisation.

Mais en tant qu'analyste de données, vous pouvez souvent vous retrouver à répéter des tâches fastidieuses au quotidien lors de l'utilisation d'Excel.

Ces tâches peuvent inclure la copie et le collage de données, la mise en forme de cellules et la création de graphiques, entre autres. Avec le temps, cela peut devenir monotone et chronophage, vous laissant moins de temps pour vous concentrer sur des aspects plus importants de l'analyse de données, tels que l'identification de tendances, de valeurs aberrantes et d'informations.

C'est pourquoi l'automatisation d'Excel avec Python peut être un changement de jeu, vous aidant à rationaliser vos flux de travail et à libérer du temps pour une analyse plus significative.

Dans ce tutoriel, je vais vous montrer quelques méthodes utiles pour créer, mettre à jour et analyser des feuilles de calcul Excel en utilisant la programmation Python. Commençons.

## Comment fusionner deux feuilles de calcul séparées avec Python

Les analystes de données doivent souvent travailler sur plusieurs feuilles de calcul, ce qui peut devenir chaotique lorsqu'il faut fusionner ces fichiers ensemble.

Le code ci-dessous vous aide à fusionner deux fichiers séparés ensemble.

```python
import pandas as pd

# Lire les deux fichiers Excel

file1 = pd.read_excel('file1.xlsx')file2 = pd.read_excel('file2.xlsx')

# Fusionner les deux fichiers en utilisant la méthode concat()
merged_file = pd.concat([file1, file2], ignore_index=True)

# Écrire le fichier fusionné dans un nouveau fichier Excel
merged_file.to_excel('merged_file.xlsx', index=False)
```

Dans ce code, nous importons d'abord la bibliothèque Pandas, que nous utiliserons pour lire et manipuler les fichiers Excel.

Nous utilisons ensuite la méthode `read_excel()` pour lire `file1.xlsx` et `file2.xlsx`. Ensuite, nous utilisons la méthode `concat()` pour fusionner les deux fichiers ensemble. L'argument `ignore_index=True` garantit que les valeurs d'index des deux fichiers sont réinitialisées, afin que nous n'ayons pas de valeurs d'index en double dans le fichier fusionné.

Enfin, nous utilisons la méthode `to_excel()` pour écrire le fichier fusionné dans un nouveau fichier Excel nommé `merged_file.xlsx`. Nous définissons également `index=False` pour nous assurer que la colonne d'index n'est pas incluse dans le fichier de sortie.

## Comment importer et exporter des données avec Python

Cette tâche implique l'utilisation de bibliothèques Python telles que Pandas pour lire des fichiers Excel dans un objet DataFrame. Vous pouvez ensuite le manipuler et l'analyser en utilisant Python.

Vous pouvez également exporter des données de Python vers un fichier Excel en utilisant les mêmes bibliothèques.

```python
import pandas as pd
# Importer le fichier Excel

df = pd.read_excel('filename.xlsx', sheet_name='Sheet1')

# Exporter vers un fichier Excel
df.to_excel('new_filename.xlsx', index=False)
```

Le code donné importe la bibliothèque Pandas et lit un fichier Excel nommé "filename.xlsx" à partir de la feuille "Sheet1" du classeur, stockant les données dans un dataframe Pandas nommé "df". Le dataframe est ensuite exporté vers un nouveau fichier Excel nommé "new_filename.xlsx" en utilisant la méthode "to_excel". Le paramètre "index=False" est utilisé pour exclure l'indexation des lignes dans le fichier de sortie.

Essentiellement, le code copie le contenu du fichier Excel original vers un nouveau fichier en utilisant Pandas.

## Comment nettoyer et transformer des données en utilisant Python

Cette tâche implique l'utilisation de bibliothèques Python telles que Pandas pour nettoyer et transformer des données dans Excel.

Cela peut inclure la suppression des doublons, le filtrage des données en fonction de critères spécifiques et l'exécution de calculs sur les données.

```python
import pandas as pd

# Supprimer les doublons
df = df.drop_duplicates()

# Filtrer les données
df = df[df['column_name'] > 10]

# Effectuer des calculs
df['new_column'] = df['column1'] + df['column2']
```

L'extrait de code ci-dessus effectue des tâches de nettoyage et de manipulation de données sur un dataframe Pandas nommé 'df' en utilisant la bibliothèque Pandas.

Tout d'abord, il supprime les lignes en double de 'df' en utilisant la méthode "drop_duplicates". Ensuite, il filtre le dataframe 'df' en sélectionnant les lignes où la valeur dans la colonne 'column_name' est supérieure à 10 et attribue le résultat filtré à un nouveau dataframe appelé 'data_df'.

Enfin, une nouvelle colonne nommée 'new_column' est ajoutée à 'df' qui contient la somme des valeurs de 'column1' et 'column2'.

Dans l'ensemble, le code nettoie et manipule efficacement les données en supprimant les doublons, en filtrant des lignes spécifiques et en ajoutant une nouvelle colonne calculée au dataframe original.

## Comment effectuer une analyse de données avec Python

Cette tâche implique l'utilisation de bibliothèques Python telles que Pandas et NumPy pour effectuer une analyse de données sur des données Excel.

Cela peut inclure le calcul de statistiques récapitulatives, telles que la moyenne et l'écart type, ou la création de rapports personnalisés en regroupant les données en fonction de critères spécifiques.

```python
import pandas as pd
import numpy as np

# Calculer les statistiques récapitulatives
df.describe()
# Créer des rapports personnalisés
df.pivot_table(values='column_name', index='category_name', columns='date')
```

Le code utilise les bibliothèques Pandas et NumPy et effectue des tâches d'analyse de données et de reporting sur un dataframe Pandas nommé "df".

Tout d'abord, il calcule les statistiques récapitulatives pour les données numériques du dataframe en utilisant la méthode "describe". Cette méthode génère des informations précieuses sur la distribution des données, la tendance centrale et la dispersion.

Ensuite, le code utilise la méthode "pivot_table" pour créer des rapports personnalisés à partir du dataframe. Cette méthode résume et agrège les données du dataframe et peut produire des tableaux dans divers formats.

Dans ce code, il génère un nouveau dataframe où les valeurs de 'column_name' sont regroupées par les colonnes 'category_name' et 'date'.

Dans l'ensemble, le code effectue des tâches d'analyse statistique et de reporting sur le dataframe pour obtenir des informations à partir des données.

## Comment créer des graphiques avec Python

Cette tâche implique l'utilisation de bibliothèques Python telles que matplotlib ou seaborn pour créer des graphiques et des diagrammes à partir de données Excel.

Vous pouvez personnaliser ces graphiques pour afficher des données spécifiques et les formater pour répondre à des exigences particulières.

```python
import pandas as pd
import matplotlib.pyplot as plt
# Créer un graphique à barres
df.plot(kind='bar', x='category_name', y='sales')
plt.show()
# Créer un nuage de points
df.plot(kind='scatter', x='column1', y='column2')plt.show()
```

Le code importe deux bibliothèques, Pandas et matplotlib.pyplot en utilisant les alias 'pd' et 'plt', respectivement.

La méthode "plot" de Pandas est ensuite utilisée pour créer deux types de graphiques. Le premier type de graphique est un graphique à barres qui montre la relation entre les colonnes 'category_name' et 'sales' dans le dataframe "df".

Le deuxième type de graphique est un nuage de points qui montre la relation entre les colonnes 'column1' et 'column2' dans le même dataframe. Le code utilise les paramètres "kind='bar'" pour le graphique à barres et "kind='scatter'" pour le nuage de points pour créer les graphiques respectifs.

Enfin, la méthode "show" est appelée pour afficher les graphiques à l'écran. En résumé, le code utilise Pandas et matplotlib pour créer un graphique à barres et un nuage de points afin de visualiser les données dans le dataframe "df".

## Comment faire de la visualisation de données en Python

Cette tâche implique l'utilisation de bibliothèques Python telles que Plotly et bokeh pour créer des visualisations de données interactives à partir de données Excel.

Ces visualisations permettent aux utilisateurs d'explorer les données de nouvelles manières, telles que zoomer sur des points de données spécifiques ou filtrer les données en fonction de critères particuliers.

```python
import pandas as pd
import plotly.express as px
# Créer une carte thermique
fig = px.imshow(df.corr())
fig.show()
# Créer un graphique en courbes
fig = px.line(df, x='date', y='sales', color='category')
fig.show()
```

Le code utilise les bibliothèques Pandas et plotly.express pour créer deux types de visualisations. Tout d'abord, une carte thermique est créée en utilisant la méthode "imshow" de plotly.express qui visualise la corrélation entre les colonnes du dataframe "df".

Ensuite, un graphique en courbes est créé en utilisant la méthode "line" de plotly.express qui affiche la relation entre les colonnes 'date' et 'sales' tout en différenciant les catégories en fonction de la colonne 'category' du dataframe. Les deux graphiques sont affichés en utilisant la méthode "show".

## Comment automatiser la génération de rapports avec Python

Cette tâche implique l'utilisation de scripts Python pour automatiser le processus de génération de rapports à partir de données Excel.

Vous pouvez configurer ces scripts pour qu'ils s'exécutent selon un calendrier régulier, par exemple quotidiennement ou hebdomadairement. Ils peuvent également se mettre à jour automatiquement lorsque de nouvelles données deviennent disponibles.

```python
import pandas as pd
# Créer un rapport quotidien
df_daily = df[df['date'] == '2022-01-01']
df_daily.to_excel('daily_report.xlsx', index=False)
# Créer un rapport hebdomadaire
df_weekly = df.groupby('category').sum()
df_weekly.to_excel('weekly_report.xlsx', index=False)
```

Le code crée un rapport quotidien en créant un nouveau dataframe "df_daily" qui inclut uniquement les lignes où la colonne 'date' est égale à '2022-01-01'. Cela est réalisé en utilisant la fonction d'indexation booléenne de Pandas.

Par la suite, la méthode "to_excel" est utilisée pour exporter les données filtrées vers un fichier Excel nommé "daily_report.xlsx", sans inclure la colonne d'index.

Ensuite, le code crée un rapport hebdomadaire en regroupant le dataframe "df" par la colonne 'category' et en additionnant les valeurs de toutes les autres colonnes. Cela est accompli en utilisant les méthodes "groupby" et "sum" de Pandas.

Le résultat est enregistré dans un nouveau dataframe nommé "df_weekly". Enfin, la méthode "to_excel" est utilisée pour exporter les données agrégées vers un fichier Excel nommé "weekly_report.xlsx", sans inclure la colonne d'index.

En résumé, le code crée deux rapports en utilisant la bibliothèque Pandas. Le premier rapport est un rapport quotidien qui inclut uniquement les données d'une date spécifique, et le deuxième rapport est un rapport hebdomadaire qui agrège les données par catégorie. Les deux rapports sont exportés vers des fichiers Excel en utilisant la méthode "to_excel".

## Comment automatiser les tâches répétitives avec des macros et des scripts en Python

Cette tâche implique l'utilisation de Python pour automatiser les tâches répétitives dans Excel, telles que la saisie de données ou la mise en forme. Vous pouvez le faire en créant des macros ou des scripts qui peuvent s'exécuter automatiquement, ou en utilisant Python pour interagir directement avec l'application Excel.

```python
import win32com.client as win32
# Ouvrir le fichier Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')
workbook = excel.Workbooks.Open(r'filename.xlsx')
# Exécuter la macro
excel.Application.Run('macro_name')
# Enregistrer et fermer Excel
fileworkbook.Save()workbook.Close()excel.Quit()
```

Le code utilise le module win32com.client pour interagir avec Microsoft Excel via l'API Windows.

Tout d'abord, une instance de l'application Excel est ouverte en utilisant la méthode `EnsureDispatch()`, et le fichier Excel spécifié est ouvert en utilisant la méthode `Workbooks.Open()`.

Ensuite, une macro est exécutée en utilisant la méthode `Application.Run()`, en passant le nom de la macro comme argument.

Enfin, les modifications apportées au fichier Excel sont enregistrées en utilisant la méthode `Save()`, le classeur est fermé en utilisant la méthode `Close()`, et l'application Excel est terminée en utilisant la méthode `Quit()`.

## Comment extraire des données avec Python

Cette tâche implique l'utilisation de bibliothèques Python telles que requests et Beautiful Soup pour extraire des données de pages web ou d'autres sources et les importer dans Excel.

Vous pouvez ensuite analyser et manipuler ces données en utilisant des bibliothèques Python telles que Pandas.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
# Extraire des données d'une page web
url = 'https://www.website.com/data'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]
# Exporter vers un fichier Excel
df.to_excel('scraped_data.xlsx', index=False)
```

Ce code utilise la bibliothèque requests pour envoyer une requête HTTP GET à l'URL '[https://www.example.com](https://www.example.com/)'. Il utilise ensuite la bibliothèque BeautifulSoup pour analyser le contenu HTML de la réponse dans un objet BeautifulSoup nommé 'soup'.

Vous pouvez ensuite utiliser les méthodes BeautifulSoup telles que `find_all()` pour extraire des données spécifiques du HTML:

`links = []for link in soup.find_all('a'): href = link.get('href') links.append(href)`

Ce code trouve toutes les balises d'ancrage dans le HTML et extrait la valeur de l'attribut 'href' pour chacune d'elles, les ajoutant à une liste nommée 'links'.

## Comment utiliser Python pour intégrer Excel avec d'autres applications

Cette tâche implique l'utilisation de Python pour intégrer Excel avec d'autres applications, telles que des bases de données ou des services web.

Vous pouvez le faire en utilisant des bibliothèques Python telles que pyodbc pour vous connecter à des bases de données ou en utilisant des API pour vous connecter à des services web. Cela permet un transfert et une analyse de données transparents entre différentes applications.

```python
import pandas as pd
import pyodbc
# Se connecter à la base de données
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=db_name;UID=user_id;PWD=password')
# Lire les données de la base de données
query = 'SELECT * FROM table_name'
df = pd.read_sql(query, cnxn)
# Exporter vers un fichier Excel
df.to_excel('database_data.xlsx', index=False)
```

Le code établit une connexion à une base de données SQL Server en utilisant la méthode `pyodbc.connect()`, où le pilote, le nom du serveur, le nom de la base de données, l'identifiant utilisateur et le mot de passe sont fournis comme arguments.

Ensuite, une requête SQL est définie et exécutée pour récupérer des données d'une table dans la base de données en utilisant la méthode `pd.read_sql()`, où la requête SQL et l'objet de connexion sont fournis comme arguments. Les données récupérées sont ensuite stockées dans un DataFrame pandas.

Enfin, les données du DataFrame sont exportées vers un fichier Excel nommé "database_data.xlsx" en utilisant la méthode `to_excel()`, avec la colonne d'index exclue de l'exportation en définissant le paramètre index sur False.

## Conclusion

Python est un langage polyvalent que vous pouvez utiliser pour automatiser de nombreuses tâches Excel. Vous pouvez également utiliser diverses bibliothèques telles que Pandas, openpyxl, xlwings et pyautogui pour manipuler des données, extraire des informations, générer des rapports et automatiser des tâches répétitives.

L'automatisation peut faire gagner du temps et des efforts, réduire les erreurs et augmenter la productivité. La maîtrise de Python peut être une compétence précieuse pour tout professionnel travaillant avec Excel, que vous soyez analyste de données ou financier. En apprenant Python, vous pouvez élever votre travail à de nouveaux sommets.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/). Merci pour la lecture !