---
title: 'Comment développer votre mémoire musculaire en science des données : Découper
  et mapper les données pour le Machine Learning…'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T17:53:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-data-science-muscle-memory-slicing-and-mapping-data-for-machine-learning-d38e65986c69
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XAZDpZm4Bqf1zRY6E1of9A.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: 'Comment développer votre mémoire musculaire en science des données : Découper
  et mapper les données pour le Machine Learning…'
seo_desc: 'By Zhen Liu

  When processing data using the Pandas library in Python, are you always confused
  when it comes to loc and iloc, or map, apply and applymap? Want to quickly select
  the subset you need and create some new features before creating your machi...'
---

Par Zhen Liu

Lorsque vous traitez des données avec la bibliothèque Pandas en Python, êtes-vous toujours confus face à loc et iloc, ou map, apply et applymap ? Vous voulez rapidement sélectionner le sous-ensemble dont vous avez besoin et créer de nouvelles fonctionnalités avant de créer vos modèles de machine learning ? Utilisez ce tutoriel pour vous entraîner chaque matin pendant 10 minutes, et répétez-le pendant une semaine.

**C'est comme faire quelques petits crunchs par jour — pas pour vos abdos, mais pour vos muscles en science des données.** Graduellement, vous remarquerez le changement.

Suite à mon précédent ["Data Science Workout" sur le prétraitement des données](https://medium.freecodecamp.org/how-to-build-up-your-muscle-memory-for-data-science-with-python-5960df1c930e), dans ce tutoriel, nous nous concentrerons sur 1) la sélection de sous-ensembles de données et 2) la création de nouvelles fonctionnalités.

```
contenu : 1) découper et trancher les données pour créer votre matrice de fonctionnalités (loc, iloc et etc)
```

```
2) assigner, mapper et transformer les données à l'échelle ou à l'étiquette idéale pour la modélisation (map, apply, applymap et plus)
```

Tout d'abord, chargez les bibliothèques et les données Zillow pour notre exercice :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eaM_mFSWaGj89cAvF7Bnsg.png)

### 1. Découper et trancher les données

#### 1.1 Sélection de colonnes

**Qu'est-ce que loc et iloc ?**

Dans pandas, loc et iloc sont deux méthodes pour sélectionner des lignes et des colonnes par étiquette(s) ou un tableau booléen.

`.loc[]` : vous utilisez l'**index** de la ligne (peut être à la fois entier et chaîne. Cela dépend de ce qu'est l'index, par exemple, l'index peut être des noms, et peut être un nombre), et le nom de la colonne pour l'indexation (ne peut pas utiliser d'entier pour indexer l'emplacement de la colonne).

`.iloc[]` : vous ne pouvez utiliser que des entiers pour faire de l'indexation basée sur la **position**.

Exemple : sélectionner des colonnes par nom en utilisant `.loc[]` :

Les deux expressions ci-dessus vous donnent le même résultat que ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6rt-DcBmN3eMwyCZ6Atsug.png)

Que faire si je veux sélectionner les 5 premières colonnes ?

Maintenant, nous utilisons `.iloc[]` : il découpe les colonnes ou les lignes par emplacement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*shZsBFfbpSBMvR-MjIUcPQ.png)

Déjà confus avec loc() ? Ne vous inquiétez pas — je vais vous montrer plus d'exemples ! Mais gardez à l'esprit que `.loc[] -> indexé` vs `.iloc[] -> position` basé.

#### 1.2 Sélection de lignes

Sélectionner des lignes en utilisant l'index par `.loc[]` (l'index actuel dans le dataframe est le numéro de ligne assigné automatiquement, il commence à 1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*xaSYiVkEPkKXLW0h8Un1TA.png)

Sélectionner des lignes en utilisant l'emplacement par `.iloc[]` :

Si vous sélectionnez les 2e, 3e et 5e lignes dans l'ordre (rappelez-vous que Python compte à partir de 0 lorsqu'il travaille en position, donc c'est [1,2,4])

#### 1.3 Sélectionner à la fois des colonnes et des lignes

Utiliser iloc pour obtenir les lignes 1–5, et les 6 premières colonnes par emplacement, peut être réalisé en utilisant loc en utilisant l'index de ligne et les noms de colonnes. Rappelez-vous que Python ne découpe pas inclusivement l'index de fin, donc `.iloc[1:6, …]` ne sélectionne que les lignes 1–5 par position, tandis que `.loc[1:5, …]` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CojkR9GznWZuVbQh6jwtQQ.png)

#### Quelle est la différence entre iloc et loc ?

Pour mieux démontrer la différence, nous changeons l'index de l'ordre par défaut à la colonne 'SizeRank', qui est le rang de la taille de la région.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f2pjDF6INUnjS12krT0MHA.png)

Sélectionner par index [1,2,4] : cela vous donne les lignes avec l'index (rang de taille) qui est 1,2,4.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TgoJpmJ62IxqgqjFuk-thA.png)

Sélectionner en utilisant l'emplacement [1,2,4] :

![Image](https://cdn-media-1.freecodecamp.org/images/1*peRA5VIeSE-cb7qsbDq3Dw.png)

#### 1.4 Obtenir une cellule spécifique par emplacement

#### 1.5 Exemple dans le processus de machine learning : découper les données pour la matrice des caractéristiques (X), et le vecteur de réponse (y)

Si vous voulez voir si le loyer mensuel peut être utilisé comme données d'entraînement pour identifier l'état, alors votre X est le loyer mensuel, et Y est l'état _(juste un exemple de découpage de données pour les caractéristiques et la variable de réponse, vous pouvez essayer de voir si cette prédiction fonctionnera)._

`dataframe.values` vous donne la forme d'un tableau, que vous pouvez utiliser directement dans sklearn (comme le nouveau X et y dans les lignes 16–17).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bm3I0hBM5TJZclWsTNX9NA.png)

#### 1.6 Sous-ensemble basé sur des conditions

Si nous voulons sélectionner les 10 plus grandes régions :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QLeuPgVJDetf1CURc12rLQ.png)

Autres variations :

Que se passe-t-il si nous appliquons une règle à l'ensemble du dataframe ? Il ne filtrera pas les lignes ou les colonnes mais affichera NA pour les cellules qui ne répondent pas aux exigences :

Si nous filtrons avec une variation de la valeur d'une colonne :

#### Qu'est-ce qu'une fonction lambda ?

Les **fonctions lambda** peuvent être utilisées partout où des objets **fonction** sont requis. Elle est anonyme, mais vous pouvez lui assigner une variable, par exemple :

vous pouvez définir f = lambda x: max(x)- min(x). Ici, nous filtrons les régions lorsque SizeRank est un nombre pair.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vYYOUYwVs9wEBy1k5Gnj-g.png)

Utiliser lambda pour appliquer une règle sur plus d'une colonne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BGbSizOQEFTYnCMtQLcTKw.png)

#### Exemples de filtrage à la fois des colonnes et des lignes

Cela donne une erreur si nous exécutons raw_df[raw_df.loc[0]>450000] car il y a des colonnes non numériques comme l'état ou la ville. En utilisant ce que nous avons appris de mon dernier article, nous sélectionnons uniquement les colonnes numériques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SV4u6--0X7wWiNcWsaYrrQ.png)

Si nous voulons sélectionner les données classées dans le top 5 en taille, et ne garder que les mois où le loyer est supérieur à 450 000 pour la première ligne [index==0]

![Image](https://cdn-media-1.freecodecamp.org/images/1*KJKwkorO51PqC1brJiFwXg.png)

Maintenant, nous revenons à l'utilisation de raw_df avec toutes les colonnes, et sélectionnons les données classées dans le top 5 en taille, et ne gardons que les colonnes de chaîne cette fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9YshNq95FocnKGKDyhB-lg.png)

Pour que ce type de filtrage fonctionne, les 2 éléments à l'intérieur des [] doivent chacun produire une **série** de résultats booléens (vrai, faux) par eux-mêmes. Sinon, cela ne fonctionnera pas.

Par exemple :

```
num_df.loc[num_df['SizeRank']<=5, num_df.loc[0:3]>450000.0]
```

va échouer, car num_df.loc[**0:3**]>450000.0 ne donne pas **une série** de booléens, c'est **un tableau** de booléens.

Le format comme df.loc[df.A>0, df.loc['index']>0] fonctionnera car il ne traite qu'avec une ligne et une colonne, donc il sélectionne par 2 séries de booléens.

#### Faites attention à la syntaxe !

Cela donne une erreur car ce format supposera qu'il s'agit de lignes mais la commande sélectionne en réalité des colonnes. `.loc[]` a besoin d'un `:` du côté gauche, si la condition concerne les colonnes.

Si la condition concerne les lignes, vous pouvez ignorer le `:` du côté droit.

### 2. Assigner, mapper et transformer les données à l'échelle idéale

#### 2.1. Assigner des valeurs

Utilisez .copy() si vous voulez copier les données pour une transformation tout en gardant les données originales intactes.

Nous allons utiliser ce dataframe copié pour pratiquer l'assignation de valeurs.

* **Assigner des valeurs aux lignes en utilisant** `.loc[]` **ou** `.iloc[]`

![Image](https://cdn-media-1.freecodecamp.org/images/1*o9cIrULQsMIKXdpZ4rx2Gg.png)

* **Assigner des valeurs aux colonnes**

![Image](https://cdn-media-1.freecodecamp.org/images/1*wAJFXnjtTaVYL3Kf7_lz4w.png)

* **Créer une nouvelle colonne en assignant des valeurs par condition**

![Image](https://cdn-media-1.freecodecamp.org/images/1*IvarQTPnK-ONZCnNXcOsaw.png)

**Créer une nouvelle colonne en utilisant des colonnes existantes : Map ou Apply**

* Map : si trop de colonnes doivent changer de valeurs en créant un dictionnaire

![Image](https://cdn-media-1.freecodecamp.org/images/1*Unvhacc4qwWH2SHWge95Dg.png)

**2.2 Map** : il itère sur chaque élément d'une série, mais seulement une série. Nous pouvons utiliser map pour changer les valeurs dans une colonne.

Par exemple : lorsque nous indexons une colonne comme ceci : raw_df['2018–04'], c'est une série ; donc nous pouvons utiliser map pour changer l'unité de valeur en 2018–04 en 'mille' en multipliant par 0,001 dans cette série :

![Image](https://cdn-media-1.freecodecamp.org/images/1*28EvH9LdnWh41uJONFSbPA.png)

Si nous voulons changer plus d'une colonne en milliers, utilisez applymap.

**2.3 ApplyMap** : Cela aide à appliquer une fonction à chaque ÉLÉMENT du dataframe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CxwU6vvMYeJZ8OXHb04dtQ.png)

**2.4 Apply** : utiliser si nous devons appliquer pour une ou plusieurs colonnes plus spécifiquement.

Comme le nom le suggère, il applique une fonction LE LONG de n'importe quel axe du DataFrame.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oyHqbpQj6AkRCCWoiZghCw.png)

#### **Révision : quelle est la différence entre map, appymap et apply ?**

`map` : opération sur chaque élément dans une série, ou une colonne d'un df

`applymap` : chaque élément dans un df (même opération pour les éléments dans toutes les colonnes et lignes)

`apply` : une opération qui prend plusieurs colonnes d'un df

**Forme spéciale de apply :**  
`df[['col1','col2']].apply(sum)` : il retournera la somme de toutes les valeurs de la colonne1 et de la colonne2.

* Forme spéciale de apply dans pandas pour obtenir une valeur agrégée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTvUvOF3A10Kkkt_kRWXyw.png)

Ou utilisez `agg` pour obtenir plus de types de statistiques descriptives :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-PMg9X0wbpv4qiwqyW0y2A.png)

**2.4 Utiliser apply pour redimensionner les données pour le machine learning :**

Normaliser et standardiser les données en Python (vous pouvez utiliser [standard scaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) de sklearn, mais voici le concept).

![Image](https://cdn-media-1.freecodecamp.org/images/1*0ywnr-XGapaNO5Q1zAnq8Q.png)

C'est tout pour la deuxième partie de ma série sur le développement de la mémoire musculaire pour la science des données en Python. La première partie est liée à la fin.

Restez à l'écoute ! Mon prochain tutoriel vous montrera comment "friser les muscles de la science des données" pour joindre et pivoter les données.

Suivez-moi et donnez-moi quelques applaudissements si vous trouvez cela utile :)

Vous pourriez également être intéressé par mon analyse sur la saisonnalité des locations :

[**Comment analyser la saisonnalité des locations et les tendances pour économiser de l'argent sur votre bail**](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a)  
[_Lorsque je cherchais un nouvel appartement à louer, j'ai commencé à me demander : y a-t-il un impact saisonnier ? Y a-t-il un mois…_medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a)