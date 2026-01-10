---
title: Comment améliorer la qualité du code en apprentissage automatique avec Scikit-learn
  Pipeline et ColumnTransformer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-08T16:31:20.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-pipeline
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Python-Power-BI-1.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
seo_title: Comment améliorer la qualité du code en apprentissage automatique avec
  Scikit-learn Pipeline et ColumnTransformer
seo_desc: 'By Yannawut Kimnaruk

  When you''re working on a machine learning project, the most tedious steps are often
  data cleaning and preprocessing. Especially when you''re working in a Jupyter Notebook,
  running code in many cells can be confusing.

  The Scikit-le...'
---

Par Yannawut Kimnaruk

Lorsque vous travaillez sur un projet d'apprentissage automatique, les étapes les plus fastidieuses sont souvent le nettoyage et le prétraitement des données. Surtout lorsque vous travaillez dans un Jupyter Notebook, l'exécution de code dans de nombreuses cellules peut être déroutante.

La bibliothèque Scikit-learn dispose d'outils appelés Pipeline et ColumnTransformer qui peuvent vraiment faciliter votre vie. Au lieu de transformer le dataframe étape par étape, le pipeline combine toutes les étapes de transformation. Vous pouvez obtenir le même résultat avec moins de code. Il est également plus facile de comprendre les flux de travail des données et de les modifier pour d'autres projets.

Cet article vous montrera étape par étape comment créer le pipeline d'apprentissage automatique, en commençant par un exemple simple et en progressant vers un exemple plus compliqué.

Si vous êtes familier avec le pipeline Scikit-learn et ColumnTransformer, vous pouvez sauter directement à la partie qui vous intéresse.

## Table des matières

* [Qu'est-ce que le Pipeline Scikit-learn ?](#heading-qu-est-ce-que-le-pipeline-scikit-learn)
* [Qu'est-ce que le ColumnTransformer de Scikit-learn ?](#heading-qu-est-ce-que-le-columntransformer-scikit-learn)
* [Quelle est la différence entre le Pipeline et le ColumnTransformer ?](#heading-quelle-est-la-difference-entre-le-pipeline-et-le-columntransformer)
* [Comment créer un Pipeline](#heading-comment-creer-un-pipeline)
* [Comment trouver le meilleur hyperparamètre et la meilleure méthode de préparation des données](#heading-comment-trouver-le-meilleur-hyperparametre-et-la-meilleure-methode-de-preparation-des-donnees)
* [Comment ajouter des transformations personnalisées](#heading-comment-ajouter-des-transformations-personnalisees-et-trouver-le-meilleur-modele-d-apprentissage-automatique)
* [Comment choisir le meilleur modèle d'apprentissage automatique](#heading-comment-ajouter-des-transformations-personnalisees-et-trouver-le-meilleur-modele-d-apprentissage-automatique)

## Qu'est-ce que le Pipeline Scikit-learn ?

Avant d'entraîner un modèle, vous devez diviser vos données en un ensemble d'entraînement et un ensemble de test. Chaque jeu de données passera par les étapes de nettoyage et de prétraitement des données avant de les mettre dans un modèle d'apprentissage automatique.

Il n'est pas efficace d'écrire un code répétitif pour l'ensemble d'entraînement et l'ensemble de test. C'est là que le pipeline scikit-learn entre en jeu.

Le pipeline Scikit-learn est une manière élégante de créer un flux de travail d'entraînement de modèle d'apprentissage automatique. Cela ressemble à ceci :

![Image](https://miro.medium.com/max/1308/1*3cbyBR99wFWklU6Sy85NEA.png)
_Illustration du Pipeline_

Tout d'abord, imaginez que vous pouvez créer un seul pipeline dans lequel vous pouvez entrer n'importe quelles données. Ces données seront transformées dans un format approprié avant l'entraînement ou la prédiction du modèle.

Le pipeline Scikit-learn est un outil qui lie toutes les étapes de manipulation des données ensemble pour créer un pipeline. Il raccourcira votre code et le rendra plus facile à lire et à ajuster. (Vous pouvez même visualiser votre pipeline pour voir les étapes à l'intérieur.) Il est également plus facile de performer GridSearchCV sans fuite de données de l'ensemble de test.

## Qu'est-ce que le ColumnTransformer de Scikit-learn ?

Comme indiqué sur le site web de scikit-learn, voici le but de ColumnTransformer :

> "Cet estimateur permet à différentes colonnes ou sous-ensembles de colonnes de l'entrée d'être transformés séparément et les caractéristiques générées par chaque transformateur seront concaténées pour former un seul espace de caractéristiques.
>
> Cela est utile pour les données hétérogènes ou colonnaires, pour combiner plusieurs mécanismes d'extraction de caractéristiques ou transformations en un seul transformateur."

En bref, ColumnTransformer transformera chaque groupe de colonnes de dataframe séparément et les combinera plus tard. Cela est utile dans le processus de prétraitement des données.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-207.png)
_Illustration du ColumnTransformer_

## Quelle est la différence entre le Pipeline et le ColumnTransformer ?

Il y a une grande différence entre Pipeline et ColumnTransformer que vous devez comprendre.

![Image](https://miro.medium.com/max/1190/1*I0F-ALOL8J8f6V33CDKyrA.png)
_Pipeline VS ColumnTransformer_

**Vous utilisez le pipeline** pour plusieurs transformations des mêmes colonnes.

D'autre part, **vous utilisez le ColumnTransformer** pour transformer chaque ensemble de colonnes séparément avant de les combiner plus tard.

D'accord, avec cela en tête, commençons à coder !!

## Comment créer un Pipeline

### Obtenir le jeu de données

Vous pouvez télécharger les données que j'ai utilisées dans cet article à partir de ce [jeu de données kaggle](https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists?datasetId=1019790&sortBy=voteCount&select=aug_train.csv). Voici un échantillon du jeu de données :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-210.png)
_Échantillon du jeu de données_

J'ai écrit un article explorant les données de ce jeu de données que vous pouvez trouver [ici si vous êtes intéressé.](https://medium.com/mlearning-ai/data-analysis-job-change-of-data-scientist-685f3de0a983)

En bref, ce jeu de données contient des informations sur les candidats à un emploi et leur décision de changer d'emploi ou non. Le jeu de données contient à la fois des colonnes numériques et catégorielles.

Notre objectif est de prédire si un candidat changera d'emploi en fonction de ses informations. Il s'agit d'une tâche de classification.

## Plan de prétraitement des données

![Image](https://miro.medium.com/max/1400/1*ZT7S2SuhMd4Zazb2lVWmcw.png)

Notez que j'ai sauté l'encodage des caractéristiques catégorielles pour la simplicité de cet article.

### Voici les étapes que nous allons suivre :

1. Importer les données et les encoder
2. Définir des ensembles de colonnes à transformer de différentes manières
3. Diviser les données en ensembles d'entraînement et de test
4. Créer des pipelines pour les caractéristiques numériques et catégorielles
5. Créer un ColumnTransformer pour appliquer le pipeline à chaque ensemble de colonnes
6. Ajouter un modèle à un pipeline final
7. Afficher le pipeline
8. Passer les données à travers le pipeline
9. (Facultatif) Sauvegarder le pipeline

### Étape 1 : Importer et encoder les données

Après avoir téléchargé les données, vous pouvez les importer en utilisant Pandas comme ceci :

```python
import pandas as pd

df = pd.read_csv("aug_train.csv")
```

Ensuite, encodez la caractéristique ordinale en utilisant un mappage pour transformer les caractéristiques catégorielles en caractéristiques numériques (puisque le modèle ne prend que des entrées numériques).

```python
# Création de dictionnaires de caractéristiques ordinales

relevent_experience_map = {
    'Has relevent experience':  1,
    'No relevent experience':    0
}

experience_map = {
    '<1'      :    0,
    '1'       :    1, 
    '2'       :    2, 
    '3'       :    3, 
    '4'       :    4, 
    '5'       :    5,
    '6'       :    6,
    '7'       :    7,
    '8'       :    8, 
    '9'       :    9, 
    '10'      :    10, 
    '11'      :    11,
    '12'      :    12,
    '13'      :    13, 
    '14'      :    14, 
    '15'      :    15, 
    '16'      :    16,
    '17'      :    17,
    '18'      :    18,
    '19'      :    19, 
    '20'      :    20, 
    '>20'     :    21
} 
    
last_new_job_map = {
    'never'        :    0,
    '1'            :    1, 
    '2'            :    2, 
    '3'            :    3, 
    '4'            :    4, 
    '>4'           :    5
}

# Transformer les caractéristiques catégorielles en caractéristiques numériques

def encode(df_pre):
    df_pre.loc[:,'relevent_experience'] = df_pre['relevent_experience'].map(relevent_experience_map)
    df_pre.loc[:,'last_new_job'] = df_pre['last_new_job'].map(last_new_job_map)
    df_pre.loc[:,'experience'] = df_pre['experience'].map(experience_map)
  
    return df_pre

df = encode(df)
```

### Étape 2 : Définir des ensembles de colonnes à transformer de différentes manières

Les données numériques et catégorielles doivent être transformées de différentes manières. Je définis donc `num_col` pour les colonnes numériques (nombres) et `cat_cols` pour les colonnes catégorielles.

```python
num_cols = ['city_development_index','relevent_experience', 'experience','last_new_job', 'training_hours']

cat_cols = ['gender', 'enrolled_university', 'education_level', 'major_discipline', 'company_size', 'company_type']
```

### Étape 3 : Créer des pipelines pour les caractéristiques numériques et catégorielles

La syntaxe du pipeline est :

```python
Pipeline(steps = [('nom_etape', fonction_de_transformation), …])
```

Pour les **caractéristiques numériques**, j'effectue les actions suivantes :

1. SimpleImputer pour remplir les valeurs manquantes avec la moyenne de cette colonne.
2. MinMaxScaler pour mettre à l'échelle la valeur pour qu'elle varie de 0 à 1 (cela affectera la performance de la régression).

Pour les **caractéristiques catégorielles**, j'effectue les actions suivantes :

1. SimpleImputer pour remplir les valeurs manquantes avec la valeur la plus fréquente de cette colonne.
2. OneHotEncoder pour diviser en plusieurs colonnes numériques pour l'entraînement du modèle. (handle_unknown='ignore' est spécifié pour prévenir les erreurs lorsqu'il trouve une catégorie non vue dans l'ensemble de test)

```python
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline

num_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale',MinMaxScaler())
])
cat_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('one-hot',OneHotEncoder(handle_unknown='ignore', sparse=False))
])
```

### Étape 4 : Créer un ColumnTransformer pour appliquer le pipeline à chaque ensemble de colonnes

La syntaxe du ColumnTransformer est :

```python
ColumnTransformer(transformers=[('nom_etape', fonction_de_transformation, cols), …])
```

Passez les colonnes numériques à travers le pipeline numérique et passez les colonnes catégorielles à travers le pipeline catégoriel créé à l'étape 3.

remainder='drop' est spécifié pour ignorer les autres colonnes dans un dataframe.

n_job = -1 signifie que nous utiliserons tous les processeurs pour exécuter en parallèle.

```python
from sklearn.compose import ColumnTransformer

col_trans = ColumnTransformer(transformers=[
    ('num_pipeline',num_pipeline,num_cols),
    ('cat_pipeline',cat_pipeline,cat_cols)
    ],
    remainder='drop',
    n_jobs=-1)
```

### Étape 5 : Ajouter un modèle au pipeline final

J'utilise le modèle de régression logistique dans cet exemple.

Créez un nouveau pipeline pour mélanger le ColumnTransformer de l'étape 4 avec le modèle de régression logistique. J'utilise un pipeline dans ce cas parce que l'ensemble du dataframe doit passer par l'étape ColumnTransformer et l'étape de modélisation, respectivement.

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0)
clf_pipeline = Pipeline(steps=[
    ('col_trans', col_trans),
    ('model', clf)
])
```

### Étape 6 : Afficher le pipeline

La syntaxe pour cela est `display(nom_pipeline)` :

```python
from sklearn import set_config

set_config(display='diagram')
display(clf_pipeline)
```

![Image](https://miro.medium.com/max/560/1*ZAQ6T65iADOmFx1eCJsjDQ.png)
_Pipeline affiché_

Vous pouvez cliquer sur l'image affichée pour voir les détails de chaque étape.

![Image](https://miro.medium.com/max/1400/1*gahdAdZlFSICnQmiqbQYvg.png)
_Pipeline affiché développé_

### Étape 7 : Diviser les données en ensembles d'entraînement et de test

Divisez 20 % des données en un ensemble de test comme ceci :

```python
from sklearn.model_selection import train_test_split

X = df[num_cols+cat_cols]
y = df['target']
# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
```

Je vais ajuster le pipeline pour l'ensemble d'entraînement et utiliser ce pipeline ajusté pour l'ensemble de test afin d'éviter les fuites de données de l'ensemble de test vers le modèle.

### Étape 8 : Passer les données à travers le pipeline

Voici la syntaxe pour cela :

```python
nom_pipeline.fit, nom_pipeline.predict, nom_pipeline.score
```

`pipeline.fit` passe les données à travers un pipeline. Il ajuste également le modèle.

`pipeline.predict` utilise le modèle entraîné lorsque `pipeline.fit` est utilisé pour prédire de nouvelles données.

`pipeline.score` obtient un score du modèle dans le pipeline (précision de la régression logistique dans cet exemple).

```python
clf_pipeline.fit(X_train, y_train)
# preds = clf_pipeline.predict(X_test)
score = clf_pipeline.score(X_test, y_test)
print(f"Score du modèle : {score}") # précision du modèle
```

![Image](https://miro.medium.com/max/1400/1*Y5liijw_WH1kRMnO4S3ung.png)

### (Facultatif) Étape 9 : Sauvegarder le pipeline

La syntaxe pour cela est `joblib.dumb`.

Utilisez la bibliothèque joblib pour sauvegarder le pipeline pour une utilisation ultérieure, afin de ne pas avoir à créer et ajuster le pipeline à nouveau. Lorsque vous souhaitez utiliser un pipeline sauvegardé, chargez simplement le fichier en utilisant joblib.load comme ceci :

```python
import joblib

# Sauvegarder le pipeline dans le fichier "pipe.joblib"
joblib.dump(clf_pipeline,"pipe.joblib")

# Charger le pipeline lorsque vous souhaitez l'utiliser
same_pipe = joblib.load("pipe.joblib")
```

## Comment trouver le meilleur hyperparamètre et la meilleure méthode de préparation des données

Un pipeline ne rend pas seulement votre code plus propre, il peut également vous aider à optimiser les hyperparamètres et les méthodes de préparation des données.

### Voici ce que nous allons couvrir dans cette section :

* Comment trouver les paramètres de pipeline modifiables
* Comment trouver les meilleurs ensembles d'hyperparamètres : Ajouter un pipeline à Grid Search
* Comment trouver la meilleure méthode de préparation des données : Sauter une étape dans un pipeline
* Comment trouver les meilleurs ensembles d'hyperparamètres et la meilleure méthode de préparation des données

### Comment trouver les paramètres de pipeline modifiables

Tout d'abord, voyons la liste des paramètres qui peuvent être ajustés.

```python
clf_pipeline.get_params()
```

Le résultat peut être très long. Prenez une profonde inspiration et continuez à lire.

La première partie concerne simplement les étapes du pipeline.

![Image](https://miro.medium.com/max/1400/1*JWw_1l68o9z_D9ptmvIIMA.png)

En dessous de la première partie, vous trouverez ce qui nous intéresse : une liste de paramètres que nous pouvons ajuster.

![Image](https://miro.medium.com/max/926/1*NCkmLiyit676K3M-HfEbnw.png)

Le format est **step1_step2_…_paramètre**.

Par exemple, **col_trans**_**cat_pipeline**_**one-hot**_**sparse** signifie le paramètre sparse de l'étape one-hot.

![Image](https://miro.medium.com/max/876/1*ZITc6M2sB8Qxzr5BCnBMHQ.png)

Vous pouvez changer les paramètres directement en utilisant set_param.

```python
clf_pipeline.set_params(model_C = 10)
```

### Comment trouver les meilleurs ensembles d'hyperparamètres : Ajouter un pipeline à Grid Search

Grid Search est une méthode que vous pouvez utiliser pour effectuer le réglage des hyperparamètres. Elle vous aide à trouver les ensembles de paramètres optimaux qui donnent la plus haute précision du modèle.

#### Définir les paramètres de réglage et leur plage.

Créez un dictionnaire de paramètres de réglage (hyperparamètres)

```python
{ 'paramètre_de_réglage' : 'valeur_possible', … }
```

Dans cet exemple, je veux trouver le meilleur type de pénalité et C d'un modèle de régression logistique.

```python
grid_params = {'model__penalty' : ['none', 'l2'],
               'model__C' : np.logspace(-4, 4, 20)}
```

#### Ajouter le pipeline à Grid Search

```python
GridSearchCV(model, paramètre_de_réglage, …)
```

Notre pipeline a une étape de modèle comme étape finale, donc nous pouvons entrer le pipeline directement dans la fonction GridSearchCV.

```python
from sklearn.model_selection import GridSearchCV

gs = GridSearchCV(clf_pipeline, grid_params, cv=5, scoring='accuracy')
gs.fit(X_train, y_train)

print("Meilleur score de l'ensemble d'entraînement : "+str(gs.best_score_))
print("Meilleur ensemble de paramètres : "+str(gs.best_params_))
print("Score de test : "+str(gs.score(X_test,y_test)))
```

![Image](https://miro.medium.com/max/1252/1*JP64DvryL62BV2Z8ctyVXw.png)
_Résultat de Grid Search_

Après avoir défini Grid Search, vous pouvez ajuster Grid Search avec les données et voir les résultats. Voyons ce que fait le code :

* `.fit` : ajuste le modèle et essaie tous les ensembles de paramètres dans le dictionnaire des paramètres de réglage
* `.best_score_` : la plus haute précision parmi tous les ensembles de paramètres
* `.best_params_` : L'ensemble de paramètres qui donne le meilleur score
* `.score(X_test,y_test)` : Le score lors de l'essai du meilleur modèle avec l'ensemble de test.

Vous pouvez lire plus sur GridSearchCV dans la documentation [ici](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).

### Comment trouver la meilleure méthode de préparation des données : Sauter une étape dans un pipeline

Trouver la meilleure méthode de préparation des données peut être difficile sans un pipeline puisque vous devez créer tant de variables pour de nombreux cas de transformation de données.

Avec le pipeline, nous pouvons créer des étapes de transformation de données dans le pipeline et effectuer une recherche sur grille pour trouver la meilleure étape. Une recherche sur grille sélectionnera quelle étape sauter et comparera le résultat de chaque cas.

#### Comment ajuster légèrement le pipeline actuel

Je veux savoir quelle méthode de mise à l'échelle fonctionnera le mieux pour mes données entre MinMaxScaler et StandardScaler.

J'ajoute une étape StandardScaler dans le num_pipeline. Le reste ne change pas.

```python
from sklearn.preprocessing import StandardScaler

num_pipeline2 = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('minmax_scale', MinMaxScaler()),
    ('std_scale', StandardScaler()),
])

col_trans2 = ColumnTransformer(transformers=[
    ('num_pipeline',num_pipeline2,num_cols),
    ('cat_pipeline',cat_pipeline,cat_cols)
    ],
    remainder='drop',
    n_jobs=-1)
    
clf_pipeline2 = Pipeline(steps=[
    ('col_trans', col_trans2),
    ('model', clf)
])
```

![Image](https://miro.medium.com/max/526/1*K1pdg8EFtGLIhNSEUQ0DsA.png)
_Pipeline ajusté_

### Comment effectuer une recherche sur grille

Dans les paramètres de recherche sur grille, spécifiez les étapes que vous souhaitez sauter et définissez leur valeur sur **passthrough**.

Puisque MinMaxScaler et StandardScaler ne doivent pas fonctionner en même temps, j'utiliserai **une liste de dictionnaires** pour les paramètres de recherche sur grille.

```python
[{cas 1},{cas 2}]
```

Si vous utilisez une liste de dictionnaires, la recherche sur grille effectuera une combinaison de chaque paramètre dans le cas 1 jusqu'à ce qu'il soit complet. Ensuite, elle effectuera une combinaison de chaque paramètre dans le cas 2. Il n'y a donc pas de cas où MinMaxScaler et StandardScaler sont utilisés ensemble.

```python
grid_step_params = [{'col_trans__num_pipeline__minmax_scale': ['passthrough']},
                    {'col_trans__num_pipeline__std_scale': ['passthrough']}]
```

Effectuez une recherche sur grille et imprimez les résultats (comme une recherche sur grille normale).

```python
gs2 = GridSearchCV(clf_pipeline2, grid_step_params, scoring='accuracy')
gs2.fit(X_train, y_train)

print("Meilleur score de l'ensemble d'entraînement : "+str(gs2.best_score_))
print("Meilleur ensemble de paramètres : "+str(gs2.best_params_))
print("Score de test : "+str(gs2.score(X_test,y_test)))
```

![Image](https://miro.medium.com/max/1354/1*u-TK9RhHn0eSIRbtEUdWsQ.png)

Le meilleur cas est minmax_scale : 'passthrough', donc StandardScaler est la meilleure méthode de mise à l'échelle pour ces données.

### Comment trouver les meilleurs ensembles d'hyperparamètres et la meilleure méthode de préparation des données

Vous pouvez trouver les meilleurs ensembles d'hyperparamètres et la meilleure méthode de préparation des données en ajoutant des paramètres de réglage au dictionnaire de chaque cas de la méthode de préparation des données.

```python
grid_params = {'model__penalty' : ['none', 'l2'],
               'model__C' : np.logspace(-4, 4, 20)}
               
grid_step_params = [{**{'col_trans__num_pipeline__minmax_scale': ['passthrough']}, **grid_params},
                    {**{'col_trans__num_pipeline__std_scale': ['passthrough']}, **grid_params}]
```

grid_params sera ajouté à la fois au cas 1 (sauter MinMaxScaler) et au cas 2 (sauter StandardScaler).

```python
# Vous pouvez fusionner des dictionnaires en utilisant la syntaxe ci-dessous.

merge_dict = {**dict_1,**dict_2}
```

Effectuez une recherche sur grille et imprimez les résultats (comme une recherche sur grille normale).

```python
gs3 = GridSearchCV(clf_pipeline2, grid_step_params2, scoring='accuracy')
gs3.fit(X_train, y_train)

print("Meilleur score de l'ensemble d'entraînement : "+str(gs3.best_score_))
print("Meilleur ensemble de paramètres : "+str(gs3.best_params_))
print("Score de test : "+str(gs3.score(X_test,y_test)))
```

![Image](https://miro.medium.com/max/1400/1*fLcVD6j9m2QcdkkYpoJOjA.png)

Vous pouvez trouver le meilleur ensemble de paramètres en utilisant .best_params_. Comme minmax_scale : 'passthrough', donc StandardScaler est la meilleure méthode de mise à l'échelle pour ces données.

Vous pouvez afficher tous les cas de recherche sur grille en utilisant .cv_results_:

```python
pd.DataFrame(gs3.cv_results_)
```

![Image](https://miro.medium.com/max/1400/1*Ddwx3CZ1k3kfEXYG2pGkMw.png)
_Résultat de GridSearch_

Il y a 80 cas pour cet exemple. Il y a le temps d'exécution et la précision de chaque cas pour que vous puissiez les considérer, puisque parfois nous pouvons sélectionner le modèle le plus rapide avec une précision acceptable au lieu de celui avec la plus haute précision.

## Comment ajouter des transformations personnalisées et trouver le meilleur modèle d'apprentissage automatique

La recherche du meilleur modèle d'apprentissage automatique peut être une tâche chronophage. Le pipeline peut rendre cette tâche beaucoup plus pratique afin que vous puissiez raccourcir la boucle d'entraînement et d'évaluation du modèle.

### Voici ce que nous allons couvrir dans cette partie :

* Ajouter une transformation personnalisée
* Trouver le meilleur modèle d'apprentissage automatique

### Comment ajouter une transformation personnalisée

En plus des fonctions de transformation de données standard telles que MinMaxScaler de sklearn, vous pouvez également créer votre propre transformation pour vos données.

Dans cet exemple, je vais créer une méthode de classe pour encoder les caractéristiques ordinales en utilisant un mappage pour transformer les caractéristiques catégorielles en caractéristiques numériques. En termes simples, nous allons changer les données de texte en nombres.

Tout d'abord, nous allons effectuer le traitement des données requis avant l'entraînement du modèle de régression.

```python
from sklearn.base import TransformerMixin

class Encode(TransformerMixin):
    
    def __init__(self):
        # Création de dictionnaires de caractéristiques ordinales
        self.rel_exp_map = {
            'Has relevent experience': 1,
            'No relevent experience': 0}
            
    def fit(self, df, y = None):
    	return self
        
    def transform(self, df, y = None):
        df_pre = df.copy()
        df_pre.loc[:,'rel_exp'] = df_pre['rel_exp']\
                               .map(self.rel_exp_map)
        return df_pre
```

Voici une explication de ce qui se passe dans ce code :

* Créez une classe nommée Encode qui hérite de la classe de base appelée TransformerMixin de sklearn.
* À l'intérieur de la classe, il y a 3 méthodes nécessaires : `__init__`, `fit`, et `transform`
* **`__init__`** sera appelé lorsqu'un pipeline est créé. C'est là que nous définissons les variables à l'intérieur de la classe. J'ai créé une variable 'rel_exp_map' qui est un dictionnaire qui mappe les catégories à des nombres.
* **`fit`** sera appelé lors de l'ajustement du pipeline. Je l'ai laissé vide pour ce cas.
* **`transform`** sera appelé lorsqu'une transformation de pipeline est utilisée. Cette méthode nécessite un dataframe (df) comme entrée tandis que y est défini pour être None par défaut (Il est forcé d'avoir un argument y mais je ne l'utiliserai pas de toute façon).
* Dans **transform**, la colonne de dataframe 'rel_exp' sera mappée avec le rel_exp_map.

Notez que le `\` est seulement pour continuer le code à une nouvelle ligne.

Ensuite, ajoutez cette classe Encode comme une étape de pipeline.

```python
pipeline = Pipeline(steps=[
    ('Encode', Encode()),
    ('col_trans', col_trans),
    ('model', LogisticRegression())
])
```

Ensuite, vous pouvez ajuster, transformer ou effectuer une recherche sur grille du pipeline comme un pipeline normal.

### Comment trouver le meilleur modèle d'apprentissage automatique

La première solution qui m'est venue à l'esprit était d'ajouter de nombreuses étapes de modèle dans un pipeline et de sauter une étape en changeant la valeur de l'étape en 'passthrough' dans la recherche sur grille. Cela ressemble à ce que nous avons fait lors de la recherche de la meilleure méthode de préparation des données.

```python
temp_pipeline = Pipeline(steps=[
    ('model1', LogisticRegression()),
    ('model2',SVC(gamma='auto'))
])
```

Mais j'ai vu une erreur comme ceci :

![Image](https://miro.medium.com/max/700/1*2CGj8aBvcPbxDw_p9tpijg.png)
_Erreur lorsqu'il y a 2 classifieurs dans 1 pipeline_

Ah ha – vous ne pouvez pas avoir deux modèles de classification dans un pipeline !

La solution à ce problème est de créer une transformation personnalisée qui reçoit un modèle comme entrée et effectue une recherche sur grille pour trouver le meilleur modèle.

### Voici les étapes que nous allons suivre :

1. Créer une classe qui reçoit un modèle comme entrée
2. Ajouter la classe de l'étape 1 à un pipeline
3. Effectuer une recherche sur grille
4. Imprimer les résultats de la recherche sur grille sous forme de tableau

### Étape 1 : Créer une classe qui reçoit un modèle comme entrée

```python
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

class ClfSwitcher(BaseEstimator):

def __init__(self, estimator = LogisticRegression()):
        self.estimator = estimator
        
def fit(self, X, y=None, **kwargs):
        self.estimator.fit(X, y)
        return self
        
def predict(self, X, y=None):
        return self.estimator.predict(X)
        
def predict_proba(self, X):
        return self.estimator.predict_proba(X)
        
def score(self, X, y):
        return self.estimator.score(X, y)
```

**Explication du code :**

* Créez une classe nommée `ClfSwitcher` qui hérite de la classe de base appelée BaseEstimator de sklearn.
* À l'intérieur de la classe, il y a cinq méthodes nécessaires comme `modèle de classification : __init__`, `fit`, `predict`, `predict_proba` et `score`
* **`__init__`** reçoit un estimateur (modèle) comme entrée. J'ai indiqué LogisticRegression() comme modèle par défaut.
* **`fit`** est pour l'ajustement du modèle. Il n'y a pas de valeur de retour.
* Les autres méthodes sont pour simuler le modèle. Elles retourneront le résultat comme si c'était le modèle lui-même.

### Étape 2 : Ajouter la classe de l'étape 1 à un pipeline

```python
clf_pipeline = Pipeline(steps=[
    ('Encode', Encode()),
    ('col_trans', col_trans),
    ('model', ClfSwitcher())
])
```

### Étape 3 : Effectuer une recherche sur grille

Il y a 2 cas utilisant différents modèles de classification dans les paramètres de recherche sur grille, y compris la régression logistique et la machine à vecteurs de support.

```python
from sklearn.model_selection import GridSearchCV

grid_params = [
    {'model__estimator': [LogisticRegression()]},
    {'model__estimator': [SVC(gamma='auto')]}
]

gs = GridSearchCV(clf_pipeline, grid_params, scoring='accuracy')
gs.fit(X_train, y_train)

print("Meilleur score de l'ensemble d'entraînement : "+str(gs.best_score_))
print("Meilleur ensemble de paramètres : "+str(gs.best_params_))
print("Score de test : "+str(gs.score(X_test,y_test)))
```

![Image](https://miro.medium.com/max/700/1*4rxzC3Wv0y9QOw0G4iHxog.png)
_Résultat de la recherche sur grille_

Le résultat montre que la régression logistique donne le meilleur résultat.

### Étape 4 : Imprimer les résultats de la recherche sur grille sous forme de tableau

```python
pd.DataFrame(gs.cv_results_)
```

![Image](https://miro.medium.com/max/700/1*bzCWW5AJ3Jb2c5fdIR78LA.png)
_Tableau des résultats de la recherche sur grille_

La régression logistique a une précision légèrement supérieure à SVC mais est beaucoup plus rapide (moins de temps d'ajustement).

N'oubliez pas que vous pouvez appliquer différentes méthodes de préparation des données pour chaque modèle également.

## Conclusion

Vous pouvez implémenter le pipeline Scikit-learn et ColumnTransformer des étapes de nettoyage des données aux étapes de modélisation des données pour rendre votre code plus propre.

Vous pouvez également trouver le meilleur hyperparamètre, la meilleure méthode de préparation des données et le meilleur modèle d'apprentissage automatique avec la recherche sur grille et le mot-clé passthrough.

Vous pouvez trouver mon code sur ce [GitHub](https://github.com/Yannawut/ML_Pipeline)