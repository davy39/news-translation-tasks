---
title: Comment construire un modèle de régression linéaire – Exemple de Machine Learning
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-09-06T13:53:46.000Z'
originalURL: https://freecodecamp.org/news/build-a-linear-regression-model-with-an-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Linear-Regression-with-an-Example
seo_title: Comment construire un modèle de régression linéaire – Exemple de Machine
  Learning
---

Banner.png
tags:
- name: Intelligence Artificielle
  slug: intelligence-artificielle
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "Depuis le lancement de ChatGPT d'OpenAI, tout le monde veut apprendre sur l'IA et le ML. \nNon seulement cela – tout le monde veut construire et lancer un produit d'IA \npar eux-mêmes pour marquer leur position dans la compétition mondiale. \nEt si vous possédez déjà un produit SaaS, vous voulez peut-être intégrer des fonctionnalités d'IA et de ML pour retenir vos clients et être compétitif sur le marché mondial. \nDans ce tutoriel, vous apprendrez à construire un modèle de régression linéaire. C'est l'une des premières choses que vous apprendrez à faire en étudiant le Machine Learning, donc cela vous aidera à faire votre premier pas dans ce marché compétitif. \n"
---

Depuis le lancement de ChatGPT d'OpenAI, tout le monde veut apprendre sur l'IA et le ML. 

Non seulement cela – tout le monde veut construire et lancer un produit d'IA par eux-mêmes pour marquer leur position dans la compétition mondiale. 

Et si vous possédez déjà un produit SaaS, vous voulez peut-être intégrer des fonctionnalités d'IA et de ML pour retenir vos clients et être compétitif sur le marché mondial. 

Dans ce tutoriel, vous apprendrez à construire un modèle de régression linéaire. C'est l'une des premières choses que vous apprendrez à faire en étudiant le Machine Learning, donc cela vous aidera à faire votre premier pas dans ce marché compétitif. 

## Table des matières

<ul><li><a href="#pre-requis">Pré-requis</a></li><li><a href="#quest-ce-que-la-regression-lineaire">Qu'est-ce que la régression linéaire ?</a></li><li><a href="#metriques-devaluation">Métriques d'évaluation</a></li><li><a href="#exemple-de-regression-lineaire-modele-de-prediction-de-prix-de-voiture">Exemple de régression linéaire – Modèle de prédiction de prix de voiture</a></li><li><a href="#comment-construire-le-modele">Comment construire le modèle</a></li><li><a href="#conclusion">Conclusion</a></li></ul>

## Pré-requis

1. Expérience de niveau intermédiaire avec un IDE (de préférence VS Code)
2. Compréhension de base des fichiers Python Notebook (.pynb)
3. Bonne compréhension du langage de programmation Python
4. Connaissance de base de Pandas (pour manipuler les dataframes), Numpy, Scikit Learn, et des bibliothèques Matplot
5. Certaines connaissances en statistiques sont utiles pour analyser les données

## Qu'est-ce que la régression linéaire ?

La régression linéaire est une méthode d'apprentissage supervisé, où la sortie prédite sera continue par nature. Par exemple, des choses comme la prédiction de prix, la prédiction de notes, et ainsi de suite. 

La régression linéaire est une technique statistique et d'apprentissage automatique fondamentale utilisée pour modéliser la relation entre une variable dépendante (également connue sous le nom de variable cible ou de réponse) et une ou plusieurs variables indépendantes (prédicteurs ou caractéristiques). 

Elle vise à établir une équation linéaire qui représente au mieux l'association entre ces variables, nous permettant de faire des prédictions et de tirer des conclusions à partir des données.

L'objectif principal de la régression linéaire est de trouver la ligne de "meilleur ajustement" (ou hyperplan dans des dimensions supérieures) qui minimise la différence entre les valeurs prédites et les valeurs observées réelles. 

Cette ligne de meilleur ajustement est définie par une équation linéaire de la forme :

Y = b0 + b1X1 + b2X2 +...+ bnXn

Dans cette équation :

1. Y représente la variable dépendante que nous voulons prédire.
2. X1,X2,...,Xn sont les variables indépendantes ou caractéristiques.
3. b0 est l'interception (la valeur de Y lorsque toutes les valeurs X sont nulles).
4. b1,b2,...,bn sont les coefficients qui déterminent la relation entre chaque variable indépendante et la variable dépendante.

La régression linéaire suppose qu'il existe une relation linéaire entre les prédicteurs et la variable cible.

L'objectif du modèle est d'estimer les coefficients (b0,b1,...,bn) qui minimisent la somme des différences quadratiques entre les valeurs prédites et les valeurs réelles dans les données d'entraînement. Ce processus est souvent appelé "ajustement du modèle". 

## Métriques d'évaluation

Les métriques d'évaluation pour un modèle de régression linéaire sont :

1. Coefficient de détermination ou R-carré (R2)
2. Erreur quadratique moyenne racine (RMSE)

Voyons ce que chacune de ces métriques représente.

### R-carré

Le R-carré décrit la quantité de variation capturée par le modèle développé. Il varie toujours entre 0 et 1. Plus la valeur du R-carré est élevée, mieux le modèle s'ajuste aux données. 

### Erreur quadratique moyenne racine

Le RMSE mesure l'ampleur moyenne des erreurs ou résidus entre les valeurs prédites générées par un modèle et les valeurs observées réelles dans un ensemble de données. Il varie toujours entre 0 et l'infini positif. Des valeurs de RMSE plus faibles indiquent de meilleures performances prédictives. 

## Exemple de régression linéaire – Modèle de prédiction de prix de voiture

Dans cet exemple, nous allons essayer de prédire le prix des voitures en construisant un modèle de régression linéaire. J'ai trouvé [ce problème](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) et l'ensemble de données sur Kaggle. J'ai remarqué qu'il y a une [soumission](https://www.kaggle.com/code/farzadnekouei/polynomial-regression-regularization-assumptions/notebook) pour ce problème, ce qui était parfait. En fait, j'ai construit ma solution en prenant une partie de cette solution. 

Plongeons dans le problème. 

Nous avons un ensemble de données de voitures d'occasion, qui contient le nom de la voiture, l'année, le prix de vente, le prix actuel, le nombre de kilomètres parcourus, le type de carburant, le type de vendeur, la transmission, et si le vendeur est le propriétaire. Notre objectif est de prédire le prix de vente de la voiture.

Explorons la solution. 

### Importer les packages requis :

Vous aurez besoin de divers packages pour travailler sur ce problème. Voici comment vous pouvez tous les importer :

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline
from statsmodels.stats.diagnostic import normal_ad
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from scipy import stats
```

### Importer l'ensemble de données

Vous pouvez télécharger l'ensemble de données (car data.csv) depuis [Kaggle](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) ou vous pouvez le télécharger depuis mon [dépôt Github](https://github.com/5minslearn/Car-Price-Prediction-using-Linear-Regression/blob/master/car%20data.csv). 

```python
df = pd.read_csv('./car data.csv')
```

### Pré-traiter l'ensemble de données

Le code ci-dessous montre les colonnes et leur type de données ainsi que le nombre de lignes. Notre ensemble de données a 9 colonnes et 301 lignes. 

```python
df.info()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-12.png)
_Type de données des colonnes dans l'ensemble de données_

La colonne "Car_Name" décrit le nom de la voiture. Ce champ doit être ignoré de notre ensemble de données. Cela est dû au fait que seules les caractéristiques de la voiture comptent et non son nom. 

Le code ci-dessous retourne le nombre de noms de voitures uniques dans notre ensemble de données. 

```python
df['Car_Name'].nunique()
```

Nous avons 98 noms de voitures uniques dans notre ensemble de données. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-28.png)
_Nombre de noms de voitures uniques_

Clairement, cela n'ajoute aucune signification à notre ensemble de données, puisque il y a tant de catégories. Supprimons cette colonne. 

```python
df.drop('Car_Name', axis=1, inplace=True)
```

L'ensemble de données a la colonne nommée "Year". Idéalement, nous avons besoin de l'âge de la voiture sur l'année où elle a été achetée / vendue. Donc, convertissons cela en "Age" et supprimons la colonne "Year". 

```python
df.insert(0, "Age", df["Year"].max()+1-df["Year"] )
df.drop('Year', axis=1, inplace=True)
```

"Age" est calculé en trouvant la différence entre l'année maximale disponible dans notre ensemble de données et l'année de cette voiture particulière. Cela est dû au fait que nos calculs seront spécifiques à cette période particulière et à cet ensemble de données. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-27.png)
_Visualiser les données dans l'ensemble de données_

### Comment trouver les valeurs aberrantes

Une valeur aberrante est un point de données qui diffère significativement des autres observations. Elles peuvent faire chuter les performances du modèle. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-26.png)
_Comment déterminer les valeurs aberrantes ?_

Les colonnes catégorielles auront le type de données "object". Regroupons les colonnes numériques et catégorielles dans un tableau NumPy. Les 5 premiers éléments du tableau seront des colonnes numériques et les 3 autres seront des colonnes catégorielles. 

Nous pouvons tracer les données dans les colonnes en utilisant la bibliothèque `seaborn`. Les colonnes catégorielles contiendront plusieurs barres, tandis que les colonnes numériques contiendront des barres simples. 

Essayons de trouver les valeurs aberrantes dans notre ensemble de données en utilisant le code suivant :

```python
sns.set_style('darkgrid')
colors = ['#0055ff', '#ff7000', '#23bf00']
CustomPalette = sns.set_palette(sns.color_palette(colors))

OrderedCols = 
np.concatenate([df.select_dtypes(exclude='object').columns.values,  df.select_dtypes(include='object').columns.values])

fig, ax = plt.subplots(2, 4, figsize=(15,7),dpi=100)

for i,col in enumerate(OrderedCols):
    x = i//4
    y = i%4
    if i<5:
        sns.boxplot(data=df, y=col, ax=ax[x,y])
        ax[x,y].yaxis.label.set_size(15)
    else:
        sns.boxplot(data=df, x=col, y='Selling_Price', ax=ax[x,y])
        ax[x,y].xaxis.label.set_size(15)
        ax[x,y].yaxis.label.set_size(15)

plt.tight_layout()    
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-25.png)
_Détermination des valeurs aberrantes dans l'ensemble de données_

Essayons de trouver les valeurs aberrantes en utilisant la **règle de l'intervalle interquartile**. 

Cela est basé sur le concept de quartiles, qui divisent un ensemble de données en quatre parties égales. La règle IQR (Intervalle Interquartile) se concentre spécifiquement sur la plage de valeurs dans les 50% du milieu des données et utilise cette plage pour identifier les valeurs aberrantes potentielles.

Nous devons trouver les valeurs de quantile minimale et maximale pour chaque valeur unique dans les colonnes catégorielles et filtrer les échantillons aberrants qui ne s'inscrivent pas dans le 25e et 75e percentile de notre colonne cible (Prix de vente). 

D'autre part, les valeurs aberrantes dans les colonnes numériques peuvent être filtrées par les 25e et 75e percentiles de la même colonne. Nous n'avons pas besoin de filtrer par rapport à la colonne cible. 

```python
outliers_indexes = []
target = 'Selling_Price'

for col in df.select_dtypes(include='object').columns:
    for cat in df[col].unique():
        df1 = df[df[col] == cat]
        q1 = df1[target].quantile(0.25)
        q3 = df1[target].quantile(0.75)
        iqr = q3-q1
        maximum = q3 + (1.5 * iqr)
        minimum = q1 - (1.5 * iqr)
        outlier_samples = df1[(df1[target] < minimum) | (df1[target] > maximum)]
        outliers_indexes.extend(outlier_samples.index.tolist())
        
        
for col in df.select_dtypes(exclude='object').columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3-q1
    maximum = q3 + (1.5 * iqr)
    minimum = q1 - (1.5 * iqr)
    outlier_samples = df[(df[col] < minimum) | (df[col] > maximum)]
    outliers_indexes.extend(outlier_samples.index.tolist())
    
outliers_indexes = list(set(outliers_indexes))
print('{} outliers were identified, whose indices are:\n\n{}'.format(len(outliers_indexes), outliers_indexes))
```

En exécutant le code ci-dessus, nous avons trouvé qu'il y a 38 valeurs aberrantes dans notre ensemble de données. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-24.png)
_Liste des indices initiaux des valeurs aberrantes_

Mais gardez à l'esprit qu'il n'est pas toujours judicieux de supprimer les valeurs aberrantes. Elles peuvent être des observations légitimes et il est important d'enquêter sur la nature de la valeur aberrante avant de décider de la supprimer ou non. 

Nous pouvons supprimer les valeurs aberrantes dans deux cas : 

1. La valeur aberrante est due à des données saisies ou mesurées incorrectement
2. La valeur aberrante crée une association significative

Creusons encore plus et trouvons les valeurs aberrantes parfaites. 

Pour cela, supposons que si le prix de vente est supérieur à 33 Lakhs ou si la voiture a parcouru plus de 400 000 kilomètres, ce sont des valeurs aberrantes. Nous les marquerons en vert. Enregistrez tous les indices dans la variable `removing_indices`. Tracez-les au format scatterplot en utilisant la bibliothèque `seaborn`, en comparant chaque colonne avec notre colonne cible. 

```python
# Étiquetage des valeurs aberrantes
df1 = df.copy()
df1['label'] = 'Normal'
df1.loc[outliers_indexes,'label'] = 'Outlier'

# Suppression des valeurs aberrantes
removing_indexes = []
removing_indexes.extend(df1[df1[target]>33].index)
removing_indexes.extend(df1[df1['Kms_Driven']>400000].index)
df1.loc[removing_indexes,'label'] = 'Removing'

# Tracé
target = 'Selling_Price'
features = df.columns.drop(target)
colors = ['#0055ff','#ff7000','#23bf00']
CustomPalette = sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(nrows=3 ,ncols=3, figsize=(15,12), dpi=200)

for i in range(len(features)):
    x=i//3
    y=i%3
    sns.scatterplot(data=df1, x=features[i], y=target, hue='label', ax=ax[x,y])
    ax[x,y].set_title('{} vs. {}'.format(target, features[i]), size = 15)
    ax[x,y].set_xlabel(features[i], size = 12)
    ax[x,y].set_ylabel(target, size = 12)
    ax[x,y].grid()

ax[2, 1].axis('off')
ax[2, 2].axis('off')
plt.tight_layout()
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-23.png)
_Outliers marqués en couleur verte_

Voyons les valeurs aberrantes parfaites :

```python
removing_indexes = list(set(removing_indexes))
removing_indexes
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-22.png)
_Liste des indices des valeurs aberrantes originales_

Nous en avons 2. Nous devons les supprimer. Mais avant cela, nous devons vérifier s'il y a des données nulles dans notre ensemble de données. 

```python
df.isnull().sum()
```

Il n'y a pas de valeurs nulles dans notre ensemble de données. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-21.png)
_Aucune valeur nulle dans l'ensemble de données_

Supprimons les valeurs aberrantes identifiées et réinitialisons l'index du dataframe. 

```python
df1 = df.copy()
df1.drop(removing_indexes, inplace=True)
df1.reset_index(drop=True, inplace=True)
```

### Analyser l'ensemble de données

Analysons les données pour voir combien chaque champ/catégorie est corrélé avec le prix de vente de la voiture. Nous devons faire une analyse de notre ensemble de données pour pouvoir tirer des conclusions à son sujet. 

Pour cela, nous devons identifier les champs numériques et catégoriques dans notre ensemble de données, car la manière de tracer cela diffère pour chaque type.

```python
NumCols = ['Age', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Owner']
CatCols = ['Fuel_Type', 'Seller_Type', 'Transmission']
```

### Analyse bivariée

Si vous n'êtes pas familier avec ce qu'est l'analyse bivariée, [voici une définition de base](https://en.wikipedia.org/wiki/Bivariate_analysis) : 

> L'analyse bivariée est l'une des formes les plus simples d'analyse quantitative. Elle implique l'analyse de deux variables, dans le but de déterminer la relation empirique entre elles. L'analyse bivariée peut être utile pour tester des hypothèses simples d'association.

Comparons le prix de vente avec les autres colonnes en utilisant l'analyse bivariée et essayons d'en tirer quelques conclusions à partir de ces données. 

### Analyse bivariée du prix de vente vs les caractéristiques numériques

Comparons les caractéristiques numériques avec le prix de vente en utilisant l'analyse bivariée. Les colonnes numériques seront tracées dans un graphique de dispersion. 

```python
fig, ax = plt.subplots(nrows=2 ,ncols=2, figsize=(10,10), dpi=90)
num_features = ['Present_Price', 'Kms_Driven', 'Age', 'Owner']
target = 'Selling_Price'
c = '#0055ff'

for i in range(len(num_features)):
    row = i//2
    col = i%2
    ax[row,col].scatter(df1[num_features[i]], df1[target], color=c, edgecolors='w', linewidths=0.25)
    ax[row,col].set_title('{} vs. {}'.format(target, num_features[i]), size = 12)
    ax[row,col].set_xlabel(num_features[i], size = 12)
    ax[row,col].set_ylabel(target, size = 12)
    ax[row,col].grid()

plt.suptitle('Prix de vente vs. Caractéristiques numériques', size = 20)
plt.tight_layout()
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-20.png)
_Analyse bivariée du prix de vente vs les caractéristiques numériques_

### Analyse bivariée du prix de vente vs les caractéristiques catégorielles

Comparons les caractéristiques catégorielles avec le prix de vente en utilisant l'analyse bivariée. Les colonnes catégorielles seront tracées dans un graphique stripplot. Cela donne la comparaison parmi plusieurs valeurs dans une catégorie. 

```python
fig, axes = plt.subplots(nrows=1 ,ncols=3, figsize=(12,5), dpi=100)
cat_features = ['Fuel_Type', 'Seller_Type', 'Transmission']
target = 'Selling_Price'
c = '#0055ff'

for i in range(len(cat_features)):
    sns.stripplot(ax=axes[i], x=cat_features[i], y=target, data=df1, size=6, color=c)
    axes[i].set_title('{} vs. {}'.format(target, cat_features[i]), size = 13)
    axes[i].set_xlabel(cat_features[i], size = 12)
    axes[i].set_ylabel(target, size = 12)
    axes[i].grid()

plt.suptitle('Prix de vente vs. Caractéristiques catégorielles', size = 20)
plt.tight_layout()
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-19.png)
_Analyse bivariée du prix de vente vs les caractéristiques catégorielles_

Voici les conclusions que nous pouvons tirer de notre analyse de données :

1. Lorsque le prix actuel augmente, le prix de vente augmente également. Ils sont directement proportionnels.
2. Le prix de vente est inversement proportionnel aux kilomètres parcourus.
3. Le prix de vente est inversement proportionnel à l'âge de la voiture.
4. Lorsque le nombre de propriétaires précédents de la voiture augmente, son prix de vente diminue. Donc, le prix de vente est inversement proportionnel au propriétaire.
5. Voitures Diesel > Voitures CNG > Voitures Essence en termes de prix de vente.
6. Le prix de vente des voitures vendues par des particuliers est inférieur au prix des voitures vendues par des concessionnaires.
7. Les voitures automatiques sont plus chères que les voitures manuelles.

### Encodage des variables catégorielles

Nous ne pouvons pas utiliser les champs catégoriques tels quels. Ils doivent être convertis en nombres car les machines ne comprennent que les nombres. 

Par exemple, prenons la colonne Fuel. Selon notre ensemble de données, nous avons des voitures fonctionnant avec deux types de carburant. Ils sont Essence et Diesel. L'encodage des variables catégoriques divisera la colonne de carburant en 2 colonnes (Fuel_Type_Petrol et Fuel_Type_Diesel). 

Supposons qu'une voiture fonctionne à l'essence. Pour cette voiture, les données seront converties en colonne Fuel_Type_Petrol définie sur 1 (Vrai), et la colonne Fuel_Type_Diesel définie sur 0 (Faux). Les ordinateurs peuvent comprendre 1 et 0 plutôt que "Essence" et "Diesel". 

Pour cela, nous effectuerons un encodage one-hot pour les colonnes catégoriques. Pandas offre la méthode `get_dummies` pour encoder les colonnes. 

```python
CatCols = ['Fuel_Type', 'Seller_Type', 'Transmission']

df1 = pd.get_dummies(df1, columns=CatCols, drop_first=True)
df1.head(5)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-18.png)
_Encodage des variables catégorielles_

Supposons que `True` et `False` sont `0` et `1`, respectivement. 

### Analyse de corrélation

Une matrice de corrélation est une matrice qui résume la force et la direction des relations linéaires entre les paires de variables dans un ensemble de données. C'est un outil crucial en statistiques et en analyse de données, utilisé pour examiner les motifs d'association entre les variables et comprendre comment elles peuvent être liées. 

La corrélation est directement proportionnelle si les valeurs sont positives, et inversement proportionnelle si les valeurs sont négatives. 

Voici le code pour trouver la matrice de corrélation en relation avec le prix de vente. 

```python
target = 'Selling_Price'
cmap = sns.diverging_palette(125, 28, s=100, l=65, sep=50, as_cmap=True)
fig, ax = plt.subplots(figsize=(9, 8), dpi=80)
ax = sns.heatmap(pd.concat([df1.drop(target,axis=1), df1[target]],axis=1).corr(), annot=True, cmap=cmap)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-17.png)
_Matrice de corrélation_

À partir de la matrice ci-dessus, nous pouvons déduire que la variable cible "Prix de vente" est fortement corrélée avec le Prix actuel, le Type de vendeur et le Type de carburant. 

## Comment construire le modèle

Nous sommes arrivés à l'étape finale. Entraînons et testons notre modèle. 

Supprimons le "Prix de vente" de l'entrée et définissons-le comme sortie. Cela signifie qu'il doit être prédit. 

```python
X = df1.drop('Selling_Price', axis=1)
y = df1['Selling_Price']
```

Divisons notre ensemble de données en prenant 70% des données pour l'entraînement et 30% des données pour le test. 

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
```

Faisons une sauvegarde de nos données de test. Nous en avons besoin pour la comparaison finale. 

```python
y_test_actual = y_test
```

### Normaliser l'ensemble de données

Le `StandardScaler` est une technique de prétraitement couramment utilisée en apprentissage automatique et en analyse de données pour standardiser ou normaliser les caractéristiques (variables) d'un ensemble de données. Son objectif principal est de transformer les données de sorte que chaque caractéristique ait une moyenne (moyenne) de 0 et un écart-type de 1. 

Normalisons notre ensemble de données en utilisant `StandardScaler`. 

```python
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Il est très important que la transformation `StandardScaler` ne doive être obtenue qu'à partir de l'ensemble d'entraînement, sinon cela entraînera une fuite de données. 

### Entraîner le modèle

```python
linear_reg = LinearRegression()
linear_reg.fit(X_train_scaled, y_train)
```

Trouvons l'interception et le coefficient pour chaque colonne dans notre ensemble de données d'entraînement. 

```python
pd.DataFrame(data = np.append(linear_reg.intercept_ , linear_reg.coef_), index = ['Intercept']+[col+" Coef." for col in X.columns], columns=['Value']).sort_values('Value', ascending=False)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-16.png)
_Valeurs de la pente et de l'interception_

### Comment évaluer le modèle

Scikit Learn fournit une fonctionnalité de métriques qui nous aide à mesurer les métriques de notre modèle. Nous pouvons l'utiliser pour déterminer les métriques incluant l'erreur quadratique moyenne, l'erreur absolue moyenne, l'erreur quadratique moyenne racine et le score R2. 

Il est maintenant temps d'évaluer le modèle :

```python
def model_evaluation(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    
    MAE = metrics.mean_absolute_error(y_test, y_pred)
    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    R2_Score = metrics.r2_score(y_test, y_pred)
    
    return pd.DataFrame([MAE, MSE, RMSE, R2_Score], index=['MAE', 'MSE', 'RMSE' ,'R2-Score'], columns=[model_name])

model_evaluation(linear_reg, X_test_scaled, y_test, 'Linear Reg.')
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-15.png)
_Évaluation du modèle_

### Évaluer le modèle en utilisant la validation croisée K-fold

Dans la validation croisée k-fold, l'ensemble de données est divisé en k sous-ensembles de taille approximativement égale ou "folds". Le modèle est entraîné et évalué k fois, chaque fois en utilisant un fold différent comme ensemble de validation et les folds restants comme ensemble d'entraînement. 

Les résultats (par exemple, la précision, l'erreur) de ces k exécutions sont ensuite moyennés pour obtenir une estimation plus robuste des performances du modèle. 

L'avantage est que chaque point de données est utilisé à la fois pour l'entraînement et la validation, réduisant le risque de biais dans l'évaluation. 

```python
linear_reg_cv = LinearRegression()
scaler = StandardScaler()
pipeline = make_pipeline(StandardScaler(),  LinearRegression())

kf = KFold(n_splits=6, shuffle=True, random_state=0) 
scoring = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'neg_root_mean_squared_error', 'r2']
result = cross_validate(pipeline, X, y, cv=kf, return_train_score=True, scoring=scoring)

MAE_mean = (-result['test_neg_mean_absolute_error']).mean()
MAE_std = (-result['test_neg_mean_absolute_error']).std()
MSE_mean = (-result['test_neg_mean_squared_error']).mean()
MSE_std = (-result['test_neg_mean_squared_error']).std()
RMSE_mean = (-result['test_neg_root_mean_squared_error']).mean()
RMSE_std = (-result['test_neg_root_mean_squared_error']).std()
R2_Score_mean = result['test_r2'].mean()
R2_Score_std = result['test_r2'].std()

pd.DataFrame({'Mean': [MAE_mean,MSE_mean,RMSE_mean,R2_Score_mean], 'Std': [MAE_std,MSE_std,RMSE_std,R2_Score_std]},
             index=['MAE', 'MSE', 'RMSE' ,'R2-Score'])
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-14.png)
_Évaluation du modèle en utilisant la validation croisée_

### Visualisation des résultats

Créons un dataframe avec les valeurs réelles et prédites. 

```python
y_test_pred = linear_reg.predict(X_test_scaled)
df_comp = pd.DataFrame({'Actual':y_test_actual, 'Predicted':y_test_pred})
```

Comparons les valeurs cibles réelles et prédites pour les données de test à l'aide d'un graphique à barres. 

```python
def compare_plot(df_comp):
    df_comp.reset_index(inplace=True)
    df_comp.plot(y=['Actual','Predicted'], kind='bar', figsize=(20,7), width=0.8)
    plt.title('Predicted vs. Actual Target Values for Test Data', fontsize=20)
    plt.ylabel('Selling_Price', fontsize=15)
    plt.show()

compare_plot(df_comp)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-13.png)
_Comparaison entre les valeurs réelles et prédites_

Dans le graphique ci-dessus, les lignes bleues indiquent le prix réel et les lignes orange indiquent le prix prédit des voitures. Vous pouvez voir que certaines valeurs prédites sont négatives. Mais dans la plupart de nos cas, notre modèle les a bien prédites. 

Ce n'est pas le modèle parfait. Mais si vous voulez l'ajuster pour faire de meilleures prédictions, faites-le moi savoir via mon [email](mailto:arun@gogosoon.com). J'écrirai un tutoriel à ce sujet si je reçois plus de demandes. 

## Conclusion

Dans ce tutoriel, vous avez appris la régression linéaire avec un exemple pratique. J'espère que cela vous aidera à progresser dans votre parcours en ML. Vous pouvez accéder à l'ensemble de données ci-dessus et au code correspondant depuis ce [dépôt Github](https://github.com/5minslearn/Car-Price-Prediction-using-Linear-Regression). 

J'espère que vous avez apprécié la lecture de cet article. Si vous souhaitez en apprendre davantage sur l'intelligence artificielle / le machine learning / le deep learning, abonnez-vous à mes articles en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_linear_regression_model) qui contient une liste consolidée de tous mes blogs.