---
title: Dataframe vers CSV – Comment sauvegarder les Dataframes Pandas par exportation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-24T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/dataframe-to-csv-how-to-save-pandas-dataframes-by-exporting
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Dataframe-to-CSV
seo_title: Dataframe vers CSV – Comment sauvegarder les Dataframes Pandas par exportation
---

How-to-Save-Pandas-Dataframes-by-Exporting.png
tags:
- name: analyse de données
  slug: analyse-de-donnees
- name: dataframe
  slug: dataframe
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nPandas est une bibliothèque open-source largement utilisée en Python pour la manipulation et l'analyse de données. Elle fournit une gamme de structures de données et de fonctions pour travailler avec les données, dont le DataFrame. \nLes DataFrames sont un outil puissant pour..."
---

Par Shittu Olumide

Pandas est une bibliothèque open-source largement utilisée en Python pour la manipulation et l'analyse de données. Elle fournit une gamme de structures de données et de fonctions pour travailler avec les données, dont le DataFrame. 

Les DataFrames sont un outil puissant pour stocker et analyser de grands ensembles de données, mais ils peuvent être difficiles à manipuler s'ils ne sont pas sauvegardés ou exportés correctement.

Il est courant dans l'analyse de données d'exporter les données des DataFrames Pandas dans des fichiers CSV car cela peut aider à économiser du temps et des ressources. En raison de leur portabilité et de leur capacité à être facilement lus par de nombreuses applications, les fichiers CSV sont un format de fichier courant pour le stockage et la distribution de données tabulaires. 

Que vous soyez un analyste de données débutant ou expert, cet article vous guidera à travers le processus de sauvegarde des DataFrames Pandas dans des fichiers CSV et vous donnera des conseils utiles sur la façon de le faire.

## Comment sauvegarder les Dataframes Pandas à l'aide de la méthode `.to_csv()`

La méthode `.to_csv()` est une fonction intégrée dans Pandas qui vous permet de sauvegarder un DataFrame Pandas sous forme de fichier CSV. Cette méthode exporte le DataFrame dans un fichier de valeurs séparées par des virgules (CSV), qui est un format simple et largement utilisé pour stocker des données tabulaires.

La syntaxe pour utiliser la méthode `.to_csv()` est la suivante :

```py
DataFrame.to_csv(filename, sep=',', index=False, encoding='utf-8')

```

Ici, `DataFrame` fait référence au DataFrame Pandas que nous voulons exporter, et `filename` fait référence au nom du fichier sous lequel vous souhaitez sauvegarder vos données.

Le paramètre `sep` spécifie le séparateur qui doit être utilisé pour séparer les valeurs dans le fichier CSV. Par défaut, il est défini sur `,` pour les valeurs séparées par des virgules. Nous pouvons également le définir sur un séparateur différent comme `\t` pour les valeurs séparées par des tabulations.

Le paramètre `index` est une valeur booléenne qui détermine s'il faut inclure l'index du DataFrame dans le fichier CSV. Par défaut, il est défini sur `False`, ce qui signifie que l'index n'est pas inclus.

Le paramètre `encoding` spécifie l'encodage des caractères à utiliser pour le fichier CSV. Par défaut, il est défini sur `utf-8`, qui est un encodage standard pour les fichiers texte.

### Exemple de code

```py
import pandas as pd

# Créer un dataframe d'exemple
Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)

# Sauvegarder le dataframe dans un fichier CSV
df.to_csv('Biodata.csv', index=False)

```

### Explication du code

Décomposons ce que chaque partie de ce code fait :

* `import pandas as pd` : Ceci importe la bibliothèque Pandas et lui assigne l'alias `pd`, ce qui est une convention couramment utilisée.
* `Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'], 'Age': [28, 23, 35, 31], 'Gender': ['M', 'F', 'M', 'F']}` : Ceci crée un dictionnaire Python avec les données que nous voulons stocker dans le DataFrame. Chaque clé représente une colonne dans le DataFrame, et sa valeur correspondante est une liste de valeurs pour cette colonne.
* `df = pd.DataFrame(Biodata)` : Ceci crée un DataFrame Pandas à partir du dictionnaire `Biodata`.
* `df.to_csv('Biodata.csv', index=False)` : Ceci sauvegarde le DataFrame dans un fichier CSV nommé `Biodata.csv`.

## Autres façons de sauvegarder les Dataframes Pandas

Il existe plusieurs méthodes alternatives à `.to_csv()` pour sauvegarder les Dataframes Pandas dans divers formats de fichiers, notamment :

1. `to_excel()` : Cette méthode est utilisée pour sauvegarder un DataFrame sous forme de fichier Excel. 
2. `to_json()` : Cette méthode est utilisée pour sauvegarder un DataFrame sous forme de fichier JSON. 
3. `to_hdf()` : Cette méthode est utilisée pour sauvegarder un DataFrame sous forme de fichier HDF5, qui est un format de données hiérarchique couramment utilisé en calcul scientifique.
4. `to_sql()` : Cette méthode est utilisée pour sauvegarder un DataFrame dans une base de données SQL. 
5. `to_pickle()` : Cette méthode est utilisée pour sauvegarder un DataFrame en tant qu'objet pickled, qui est une représentation sérialisée du DataFrame. 

Ces méthodes alternatives offrent une flexibilité dans le choix du format de fichier qui convient le mieux à votre cas d'utilisation et peuvent être particulièrement utiles pour l'analyse et le partage de données avancés.

## Conclusion

Merci d'avoir lu ! J'espère que vous comprenez maintenant comment vous pouvez facilement convertir vos Dataframes Pandas en les exportant dans un fichier CSV à l'aide de la méthode intégrée `to_csv()`.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !