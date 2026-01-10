---
title: Comment utiliser la méthode Groupby de Pandas DataFrame
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-25T21:32:38.000Z'
originalURL: https://freecodecamp.org/news/pandas-dataframe-groupby-method
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Pandas-Groupby
seo_title: Comment utiliser la méthode Groupby de Pandas DataFrame
---

1.jpg
étiquettes:
- nom: analyse de données
  slug: analyse-de-donnees
- nom: pandas
  slug: pandas
- nom: Python
  slug: python
seo_title: null
seo_desc: "Par Faith Oyama\nPandas est une bibliothèque open-source rapide et accessible en\n  \ Python conçue pour l'analyse et la manipulation de données. \nCette bibliothèque possède de nombreuses\
  \ fonctions et méthodes pour accélérer le processus d'analyse de données. L'une de mes préférées\
  \ est la méthode groupby, principalement parce qu'elle permet d'obtenir rapidement des informations sur vos données en les transformant, en les agrégeant et en les divisant en diverses catégories.\n"
---

Par Faith Oyama

Pandas est une bibliothèque open-source rapide et accessible en Python conçue pour l'analyse et la manipulation de données. 

Cette bibliothèque possède de nombreuses fonctions et méthodes pour accélérer le processus d'analyse de données. L'une de mes préférées est la méthode `groupby`, principalement parce qu'elle permet d'obtenir rapidement des informations sur vos données en les transformant, en les agrégeant et en les divisant en diverses catégories.

Dans cet article, vous apprendrez à utiliser la fonction `groupby` de Pandas, comment agréger des données et regrouper des DataFrames Pandas avec plusieurs colonnes en utilisant la méthode `groupby`.

## **Quoi installer sur mon ordinateur pour suivre cet article ?**

Pour cet article, j'utiliserai un notebook Jupyter. Vous pouvez installer Jupyter notebook et le faire fonctionner sur votre ordinateur via le [site officiel](https://jupyter.org/install). 

Après avoir installé Juypter, créez un nouveau notebook et exécutez `Import pandas as pd` pour importer pandas et `Import numpy as np` pour importer NumPy.

NumPy nous permettra de travailler avec des tableaux multidimensionnels et des fonctions mathématiques de haut niveau. D'autre part, Pandas nous permettra de manipuler nos données et d'accéder à `df.groupby()`, la méthode `groupby`.

Commençons.

![Image](https://lh3.googleusercontent.com/wU1odIzH8x7LfrhUHRK-1xDGHWA7NC0WLazO4CCfYku1V3TQtOZvm7r6QaUYGNt4H4MwX-F3mZYq82X4eMg7ZFmSGlO-kkfun2G5-r5MR7len95hg43Qq5z97WxK1_6EC0Z2h6ADCDqIW-BqanEfH4Iou2VFN_RrvK__9cxGzk9_MgS1_bkjS0gwpnPgaQ)
_Importation des bibliothèques requises_

## **Qu'est-ce que `groupby` dans Pandas ?**

Si vous êtes familier avec [SQL et sa syntaxe GROUP BY](https://www.freecodecamp.org/news/sql-aggregate-functions-how-to-group-by-in-mysql-and-postgresql/), vous savez déjà à quel point il est puissant pour résumer et catégoriser les données. 

La méthode `groupby` de Pandas en Python fait la même chose et est idéale pour diviser et catégoriser les données en groupes afin d'analyser vos données plus efficacement. 

Voici la syntaxe pour Pandas `groupby` :

```python
python DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=_NoDefault.no_default, squeeze=_NoDefault.no_default, observed=False, dropna=True)
```

Chaque attribut a une signification :

* `by` – Liste des colonnes que vous souhaitez regrouper.
* `axis` – Par défaut à 0. Il prend 0 ou 'index', 1 ou 'columns'.
* `level` – Utilisé avec MultiIndex.
* `as_index` – Sortie groupée de style SQL.
* `sort` – Par défaut à True. Spécifie si le tri doit être effectué après le regroupement.
* `group_keys` – ajouter des clés de groupe ou non.
* `squeeze` – obsolète dans les nouvelles versions.
* `observed` – À utiliser uniquement si l'un des groupeurs est catégoriel.
* `dropna` – Par défaut à False. Utilisez True pour supprimer None/Nan.

Maintenant, voyons comment cette fonction fonctionne en action.

## **Comment charger le jeu de données**

Pour ce tutoriel, nous utiliserons le jeu de données des ventes de supermarché de Kaggle, que vous pouvez accéder et télécharger [ici](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales).

Après avoir téléchargé le jeu de données, chargez les données dans un dataframe pandas.

Un DataFrame est une structure de données bidimensionnelle composée de lignes et de colonnes. Cela ressemble beaucoup à votre feuille de calcul.

Vous pouvez le faire en exécutant ce code :

```python
df = pd.read_csv(r"C:\Users\Double Arkad\Downloads\archive\supermarket_sales - Sheet1.csv")
```

Après cela, utilisez la méthode `df.head()` pour afficher les premières lignes de votre jeu de données. Après avoir exécuté `df.head()`, vous devriez obtenir le résultat ci-dessous. Cela indique que le jeu de données a été chargé avec succès.

![Image](https://lh3.googleusercontent.com/DqY0WSe2sJ-_Mh7Yx0sGKndujULCR-RxFSm1RdWCcXHrCEq3UJxC-_3ugFtStAgPeHXgrsttTWb9DtpfFz9C0OmhRGDiyjLxWMhZxY0Fls4nfw3qiNlos6DtyQ35jqyv11afGFvlwDCnFOvgVcZj-yv2aJGFmRc9OwJSzjWhE9oK37uv1SK-3UJN6hkgnQ)
_Le jeu de données a été chargé correctement_

## **Comment utiliser la méthode `groupby` dans Pandas**

Supposons que votre employeur vous a demandé de totaliser le nombre d'articles commandés et de les catégoriser selon les différentes options de paiement. Cela vous permettra de déterminer quelle méthode de paiement génère le plus de revenus.

Vous pouvez répondre à cette question avec la fonction `groupby` en regroupant simplement les données en fonction du 'Payment'.

```python
df.groupby('Payment')['Quantity'].sum()
```

![Image](https://lh6.googleusercontent.com/UpPjAe1GL7BbIcRGEAWBz2DoY3WCckOlJ1Rs9WObvgft1D02QvXwgnoaBBSE3l7PdeKFlwOnp98YyUGBOYJ16G5c1gncSsH6JPvX3qjQGjqcOR2qEG0i63WOHI8tX0aTTZsmKgTJJ4GsBvr_wvpHzJM4S-3ft5QPP1rCNxQdjCv9sIc1SNKL0lqxHHlnDg)
_Utilisation de la fonction `sum` avec `groupby`_

La première colonne, 'Payments', est la colonne que vous souhaitez regrouper. La deuxième colonne, 'Quantity', est la colonne sur laquelle vous effectuerez une fonction d'agrégation. Enfin, vous avez la fonction d'agrégation `.sum()`.

La fonction `Sum()` est l'une des nombreuses fonctions que vous pouvez utiliser dans un `groupby`. Vous pourriez également utiliser d'autres fonctions d'agrégation comme `Min()`, `Mean()`, `Median()`, `Count()`, et `Average()` pour trouver la valeur minimale, moyenne, médiane, le compte et la moyenne dans un groupe au sein de votre jeu de données.

Mais en utilisant la fonction `agg()`, vous pouvez effectuer deux ou plusieurs agrégations simultanément.

Voyons comment cela fonctionne.

## **Comment agréger des données en utilisant `groupby` dans Pandas**

### **Pandas `groupby` et `Agg()`**

Voici comment utiliser `agg()` dans une fonction `groupby` pour trouver la méthode de paiement la plus utilisée dans ce supermarché.

```python
df.groupby('Payment')['Quantity'].agg([np.sum, np.mean])
```

![Image](https://lh5.googleusercontent.com/1mljwrO9rcXq5YblmNTSwB6U5m2fijHe27GrBvoU2N2_l-d8ZsSS-d6ssm7R4xFjLPf1KU3kp2a6cFkjRcKQotMo02Dg83F6HGieAIk4_jithoFPtC_ErS3ckrwAz68DKXxU258Gbu5PHQ1Qgayvi-YzV78CuNBqRJL8WbFS6CTWFYxM6cfmrTKwDxCLHg)
_Utilisation de la fonction `agg` avec `groupby`_

Il y a plus de transactions en espèces effectuées. Les transactions par portefeuille électronique et par carte de crédit suivent en termes d'utilisation.

Remarquez ici que nous avons créé un dictionnaire et passé les fonctions d'agrégation à effectuer. Cela a permis d'effectuer simultanément deux calculs statistiques sur nos données ! Bien sûr, vous pouvez ajouter plus de fonctions d'agrégation dans le dictionnaire en fonction des informations que vous souhaitez obtenir.

Voici ce que je veux dire :

```python
df.groupby(['Payment', 'Customer type'])['Quantity'].agg([np.sum, np.mean, np.max, np.min]) 
```

![Image](https://lh4.googleusercontent.com/-HkvhpGBKdBADDRiPX2uw4RPEAl6a1pRLSwltGU4AvYCVVNHkQHCCf4F1r5H8O8kpE10uU3L0o050fLN0uaa_j1SmBLd7n9oCzAesx8ixgr4Gu9Qaxm4MTm2GyqBoi0RmpI9kTYanVnxyyd8j60c-L9lyrQp2zYtV43LOiEDBAC_-84zrVegboZOWwW8Ow)
_Ajout de plus de fonctions d'agrégation_

Dans la fonction `groupby`, nous avons ajouté plus de fonctions d'agrégation à notre calcul statistique pour obtenir des informations sur le nombre maximum et minimum de marchandises commandées dans chaque groupe de paiement.

### Pandas `groupby` et `count()`

Voici comment cela fonctionne :

```python
df.groupby('Payment')['Quantity'].count()
```

Et voici le résultat que vous obtenez :

![Image](https://lh5.googleusercontent.com/J28sp0mmTSkG3TSfMHQ9RRBPZJjEyEbeybfUAS12a7jjJX_oUmrbgUn0yPWWbu2jaOymOAaFossZ1an0EeXW12rFNkT9FRBeUHJ0RmqpPnOrm1FIO3XaGZxOBmdqb-571GwRyPi9q91-gjk-ieJInRLc_a9z8Eb43J05k5BvfknTlCcTOHQYKplfVqCuRA)
_Utilisation de la fonction `count` avec `groupby`_

D'après la sortie, nous comptons le nombre total de commandes passées dans le magasin et regroupons les résultats par chaque méthode de paiement.

## **Comment regrouper les DataFrames Pandas par plusieurs colonnes**

Vous pouvez également regrouper plusieurs colonnes dans la fonction `groupby`. Par exemple, nous avons inclus une colonne ci-dessous dans notre fonction `groupby` appelée 'Customer type'.

```python
df.groupby(['Payment', 'Customer type'])['Quantity'].sum()
```

![Image](https://lh6.googleusercontent.com/qe2y8j4A3LtUeScZGnALEu8oRzUwGZN4qjePTMhuvVqSlIs64tprnq-mBPb6v71ckMfB5aRZ88Jd948dCv7L5duyYmjI3zFNqp11muRmZzN_SmE5ZX2qENwTIh-U1yaZLKoflVH-1KcW1SRXgOGDtw6-lUCxBBX2Tfmlctrf84Z1CvyZNtFgSJ0j_Hr-nw)
_Regroupement de plusieurs colonnes_

Notre sortie montre que les données ont été divisées et catégorisées en deux groupes en fonction de la colonne Customer type. La sortie devient plus facile à analyser.

## Comment agréger plusieurs colonnes en utilisant Pandas `groupby`

Vous pouvez également effectuer des calculs statistiques sur plusieurs colonnes avec la fonction `groupby`. Par exemple, regardons le total des ventes générées et la quantité commandée et regroupons nos résultats par les colonnes "Payment" et "Customer type".

Exécutez le code :

```python
df.groupby(['Payment', 'Customer type']) [['Quantity','Unit price']].sum()
```

![Image](https://lh3.googleusercontent.com/-wKU-8DT6enZr5SQhZh_-NrC-IF7a3B4gNABHIeBHccvIne6nryDy5XXAq5zg-jDwHNKHcv78Z76eXXVW8L67ehPgAr15mr7XuLojTP_ElOsbd4fQwOsMW3KozX6XPs_52A99I5b2PEMUCF1xVHisz8n63mEkcHrVKpInehbLfdgqyOIUDX2AeF8OQQRBg)
_Utilisation de la fonction `sum` avec le regroupement de plusieurs colonnes_

Nous pouvons voir d'après la sortie que le type de paiement "Ewallet" a généré le plus de revenus, et vous pouvez continuer à déterminer quel type de clients a contribué le plus aux revenus du magasin.

## **Résumé**

Dans cet article, vous avez appris l'importance de la méthode `groupby` de Pandas. Vous avez vu comment la fonction `groupby` vous permet d'effectuer de nombreuses opérations sur vos données, de la division des données à l'application d'une fonction comme `Sum()` pour obtenir plus d'informations et ajouter plus de fonctionnalités. 

Pour en savoir plus sur Python et comment vous pouvez l'utiliser pour l'analyse de données, je vous recommande ce [cours Python pour l'analyse de données](https://www.youtube.com/watch?v=r-uOLxNrNk8) sur la [chaîne YouTube freeCodeCamp](https://www.freecodecamp.org/news/learn-data-analysis-with-python-course/). 

Si vous avez aimé lire cet article et/ou avez des questions et souhaitez entrer en contact, vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/faith-oyama-97b843253/) ou [Twitter](https://twitter.com/kin_kema).