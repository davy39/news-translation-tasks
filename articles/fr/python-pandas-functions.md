---
title: Comment commencer avec Pandas en Python – un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-09T00:48:41.000Z'
originalURL: https://freecodecamp.org/news/python-pandas-functions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6040d911a7946308b768178e.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Comment commencer avec Pandas en Python – un guide pour débutants
seo_desc: "By Suchandra Datta\nThe Pandas package in Python gives you a bunch of cool\
  \ functions and features that help you manipulate data more efficiently. It also\
  \ lets you perform numerous data cleaning and data preprocessing steps with very\
  \ little hassle. \nTh..."
---

Par Suchandra Datta

Le package Pandas en Python vous offre une série de fonctions et de fonctionnalités cool qui vous aident à manipuler les données plus efficacement. Il vous permet également d'effectuer de nombreuses étapes de nettoyage et de prétraitement des données avec très peu de tracas. 

Ce n'est pas génial ? Voici une liste de certaines des fonctions et astuces Pandas les plus fréquemment utilisées pour vous aider à profiter de votre voyage en science des données. 

## Comment supprimer les valeurs manquantes dans un DataFrame

Se débarrasser des valeurs manquantes est l'une des tâches les plus courantes en nettoyage de données. Les valeurs manquantes peuvent être présentes dans une seule ligne ou colonne ou dans plusieurs lignes et colonnes. 

Selon votre application et votre domaine de problème, vous pouvez utiliser différentes approches pour gérer les données manquantes – comme l'interpolation, la substitution par la moyenne, ou simplement la suppression des lignes avec des valeurs manquantes. 

Pandas offre la fonction `dropna` qui supprime toutes les lignes (pour axis=0) ou toutes les colonnes (pour axis=1) où des valeurs manquantes sont présentes. Certains des arguments pour la fonction dropna sont les suivants :

* `axis` qui spécifie si les lignes doivent être supprimées (axis=0) ou si les colonnes doivent être supprimées (axis=1)
* `subset` qui spécifie une liste de colonnes à considérer pour les valeurs manquantes lorsque axis=0
* `inplace` qui spécifie si les modifications doivent être apportées dans le DataFrame existant lui-même

Consultez la documentation liée [ici](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) pour une couverture plus approfondie. 

Dans l'exemple ci-dessous, nous créons un petit DataFrame avec des valeurs manquantes puis nous supprimons les lignes avec des valeurs manquantes dans n'importe quelle colonne.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-4.png)
_Supprimer les valeurs manquantes dans Pandas_

## Comment supprimer les doublons dans un DataFrame

Une autre tâche courante de nettoyage de données est la suppression des lignes en double. La fonction `drop_duplicates` effectue cela avec des arguments similaires à `dropna` tels que :

* `subset`, qui spécifie un sous-ensemble de colonnes à considérer pour les valeurs en double lorsque axis=0
* `inplace`
* `keep`, qui spécifie quelles valeurs en double conserver. Keep peut être égal à first, last, ou False pour supprimer tous les doublons.

Consultez la documentation liée [ici](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) pour plus d'informations détaillées. 

Dupliquons quelques lignes et supprimons-les de notre ensemble de données :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-5.png)
_Supprimer les valeurs en double dans Pandas_

## Comment supprimer les lignes avec des valeurs spécifiques à une colonne

Supposons que nous voulons conserver uniquement les lignes où le type de projet est Web ou où le nombre d'heures travaillées est égal à 12. Voici comment nous pouvons le faire. 

En utilisant cette méthode, nous pouvons filtrer les lignes en fonction de certaines valeurs spécifiques de colonne :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-8.png)
_Supprimer les lignes avec des valeurs spécifiques à une colonne_

## Comment convertir des DataFrames en JSON

Les DataFrames sont des structures super cool optimisées qui sont excellentes à utiliser. Et JSON est l'un des formats de données les plus populaires pour un échange de données transparent. 

Convertissons notre DataFrame en JSON en utilisant [`to_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) qui nécessite des arguments comme :

* `orient`, qui spécifie ce que doivent être les paires clé et valeur. Par défaut, il s'agit des colonnes, donc le nom de la colonne est la clé et chaque colonne est la valeur.
* `date_format` qui spécifie le format de la date. Le format par défaut est epoch. 

Regardez l'exemple ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-11.png)
_Convertir un DataFrame en JSON_

Nous pouvons voir que `to_json` a retourné une chaîne avec le schéma suivant :

```
column_0 :
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}, 
column_1:
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}, 
...
column_N:
{ row_index_0: column_value_0, row_index_1:column_value_1, ...}
   
```

Si nous voulons convertir chaque ligne en un dictionnaire, nous devons spécifier que `orient=records` et le parser en utilisant le module JSON.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-12.png)
_Convertir un DataFrame en JSON avec orient=records_

## Comment compter le nombre de valeurs uniques dans une colonne

Supposons que nous voulons savoir combien de types de projets différents existent. Nous pouvons obtenir cette information en utilisant la fonction `nunique`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-13.png)
_Compter le nombre de valeurs uniques dans une colonne_

## Comment sauvegarder un DataFrame en fichier .csv

Une seule ligne de code est nécessaire pour sauvegarder le DataFrame en fichier csv :

```
dataset.to_csv("save_as_csv.csv")
```

## Comment sauvegarder plusieurs listes en un seul fichier .csv

Supposons que nous avons trois listes séparées comme source de données et que nous voulons les sauvegarder ensemble dans un seul fichier csv. Cela implique simplement deux étapes :

* les convertir en un nombre de tuples en utilisant zip, 
* puis les convertir en une liste.

Dans l'exemple ci-dessous, nous suivons cette approche pour convertir les trois listes en un seul DataFrame que nous pouvons maintenant sauvegarder en fichier .csv.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-15.png)
_Sauvegarder plusieurs listes en un seul fichier csv_

### Comment lire des DataFrames de manière efficace en mémoire

Souvent, nous devons lire des fichiers si volumineux qu'ils ne peuvent pas tenir en mémoire. Pour de tels ensembles de données mammouth, nous utilisons une approche différente. 

Tout d'abord, nous créons un objet `TextFileReader`. Ensuite, nous spécifions un paramètre appelé `chunksize` qui spécifie combien de lignes du fichier nous voulons lire à la fois, disons 4 lignes. Nous lisons donc 4 lignes à la fois, effectuons certaines tâches sur ce chunk, et passons aux 4 lignes suivantes. 

Les petits chunks sont plus susceptibles de tenir en mémoire que le fichier entier de milliers de lignes. L'exemple suivant montre comment fonctionne le chunking.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-16.png)
_Lire un DataFrame de manière efficace en mémoire_

Ici, nous lisons l'ensemble de données `california` 1000 lignes à la fois, supprimons toutes les lignes où `median_income` est inférieur ou égal à 3, et ajoutons ces chunks réduits ensemble pour créer un ensemble de données plus petit. 

Vous pouvez économiser plus de mémoire en lisant uniquement les colonnes dont vous avez besoin et en spécifiant des types de données plus petits pour les colonnes comme décrit en détail dans la documentation liée [ici](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html).

## Comment modifier toutes les valeurs dans un DataFrame en utilisant `apply`

Revenons à notre exemple de DataFrame de projets pour illustrer cela. Nous nous concentrons sur la colonne `Hours_Worked`, en augmentant le compte de 1 s'il s'agit d'un nombre pair et de 2 s'il s'agit d'un nombre impair. Nous utilisons une fonction lambda à cette fin.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-17.png)
_Modifier toutes les valeurs dans un DataFrame en utilisant apply_

## Conclusion

Pandas est un package puissant qui peut sembler intimidant parfois en raison de son ampleur. C'est pourquoi j'ai essayé de lister certaines des fonctions les plus utiles que j'ai rencontrées. 

Ces fonctions Pandas vous aideront à accélérer vos efforts d'analyse de données. Merci pour votre temps et j'espère que vous avez apprécié la lecture de cet article. 

### 



###