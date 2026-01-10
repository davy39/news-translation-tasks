---
title: Techniques d'ingénierie des caractéristiques pour les données structurées –
  Tutoriel de Machine Learning
subtitle: ''
author: ‘Funmi
co_authors: []
series: null
date: '2023-11-27T21:13:30.000Z'
originalURL: https://freecodecamp.org/news/feature-engineering-techniques-for-structured-data
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/pexels-pawe--l-1320737--1-.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: structured data
  slug: structured-data
seo_title: Techniques d'ingénierie des caractéristiques pour les données structurées
  – Tutoriel de Machine Learning
seo_desc: "Feature engineering is an essential step in the data preprocessing process,\
  \ especially when dealing with tabular data. \nIt involves creating new features\
  \ (columns), transforming existing ones, and selecting the most relevant attributes\
  \ to improve the..."
---

L'ingénierie des caractéristiques est une étape essentielle dans le processus de prétraitement des données, en particulier lorsqu'on traite des données tabulaires.

Elle implique la création de nouvelles caractéristiques (colonnes), la transformation de celles existantes et la sélection des attributs les plus pertinents pour améliorer la performance et la précision des modèles de machine learning.

L'ingénierie des caractéristiques aide le modèle à comprendre les motifs sous-jacents, les relations et les nuances des données. Elle joue un rôle crucial dans le succès d'un projet de machine learning, car elle peut transformer un bon modèle en un excellent modèle en optimisant les caractéristiques d'entrée. Une ingénierie des caractéristiques efficace conduit également à des temps d'entraînement plus rapides et à des résultats plus interprétables.

Avant de plonger dans le domaine de l'ingénierie des caractéristiques, vous devez reconnaître le rôle pivot du nettoyage des données pour assurer le succès de l'ingénierie des caractéristiques. Traiter les valeurs manquantes, gérer les valeurs aberrantes et résoudre les incohérences améliore non seulement l'intégrité des données, mais établit également une base solide pour l'extraction et la transformation ultérieures des caractéristiques.

Dans ce tutoriel, nous explorerons le concept de l'ingénierie des caractéristiques pour les données structurées. Nous aborderons certaines techniques telles que la mise à l'échelle des caractéristiques, la création de caractéristiques, la sélection de caractéristiques et le binning. Nous utiliserons un ensemble de données hypothétique pour démontrer ces diverses techniques d'ingénierie des caractéristiques.

Commençons par créer des données factices.

## Comment créer des données factices

Nous utiliserons Python et la bibliothèque `pandas` pour créer un ensemble de données factice pour nos exemples d'ingénierie des caractéristiques. Voici comment vous pouvez générer des données factices :

```python

import pandas as pd
import numpy as np
# Créer un dataframe d'exemple
data = {
'Âge': [25, 30, 35, 40, 45],
'Revenu': [50000, 60000, 75000, 90000, 80000],
'Éducation': ['Lycée', 'Licence', 'Master', 'Doctorat', 'Licence'],
'Ville': ['New York', 'San Francisco', 'Chicago', 'Los Angeles', 'Miami'],
'Genre': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme'],
'Productivité': [5, 4, 3, 2, 4]
}
df = pd.DataFrame(data)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1026.jpg)
_Sortie du code_

Comme on peut le voir ci-dessus, l'ensemble de données factice créé se compose de six caractéristiques : 'Âge', 'Revenu', 'Éducation', 'Ville', 'Genre' et 'Productivité'.

Maintenant, explorons différentes techniques d'ingénierie des caractéristiques.

## Encodage One-Hot

L'encodage one-hot est une méthode utilisée pour convertir des variables catégorielles en une matrice binaire. Notre ensemble de données contient certaines colonnes remplies de mots tels que le genre, l'éducation et les villes.

Mais les machines aiment les nombres, pas les mots. Nous utiliserons donc une technique appelée encodage one-hot. C'est comme donner à chaque catégorie son propre interrupteur - soit il est allumé (1) ou éteint (0). Il crée une colonne binaire pour chaque catégorie au sein d'une caractéristique catégorielle.

Cette technique est essentielle car de nombreux algorithmes de machine learning ne peuvent pas travailler directement avec des données catégorielles.

### Exemple d'encodage One-Hot

Appliquons l'encodage one-hot aux colonnes 'Éducation', 'Ville' et 'Genre' de notre ensemble de données. Nous utiliserons la fonction `get_dummies` de `pandas` à cet effet :

```python
## Effectuer l'encodage one-hot
df_encoded = pd.get_dummies(df, columns=['Éducation', 'Ville', 'Genre'])

```

Après l'encodage one-hot, notre ensemble de données aura maintenant des colonnes binaires pour chaque catégorie au sein de 'Éducation', 'Ville' et 'Genre'. Cette transformation permet aux modèles de machine learning de comprendre et d'utiliser efficacement ces variables catégorielles.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1028.jpg)
_Sortie du code_

Comme vous pouvez le voir sur l'image ci-dessus, les colonnes catégorielles sont maintenant transformées en une matrice binaire.

## Mise à l'échelle des caractéristiques

La mise à l'échelle des caractéristiques est cruciale lorsqu'on travaille avec des caractéristiques numériques ayant différentes échelles. La mise à l'échelle garantit que toutes les caractéristiques contribuent de manière égale au modèle, empêchant toute caractéristique de dominer les autres.

Dans nos données, 'Âge' et 'Revenu' peuvent avoir des échelles différentes. 'Âge' peut aller de 0 à 100, tandis que 'Revenu' peut aller de 20 000 à 200 000. La mise à l'échelle des caractéristiques les met sur la même échelle pour qu'elles fonctionnent bien ensemble.

### Exemple de mise à l'échelle des caractéristiques

Dans notre ensemble de données, 'Âge' et 'Revenu' ont des échelles différentes. Pour mettre à l'échelle ces caractéristiques, nous utiliserons `StandardScaler` du module `sklearn.preprocessing` :

```python
from sklearn.preprocessing import StandardScaler
# Initialiser le StandardScaler
scaler = StandardScaler()
# Ajuster et transformer les colonnes sélectionnées
df_encoded[['Âge', 'Revenu']] = scaler.fit_transform(df_encoded[['Âge', 'Revenu']])


```

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1021-1.jpg)
_Sortie du code_

D'après la sortie du code ci-dessus, nous pouvons voir que 'Âge' et 'Revenu' ont été mis à l'échelle pour avoir une moyenne de 0 et un écart-type de 1. Cela les rend compatibles pour la modélisation et aide les algorithmes qui dépendent des distances ou des gradients à mieux performer.

## Création de caractéristiques

La création de caractéristiques est l'une des techniques les plus pivots en ingénierie des caractéristiques. Elle implique la génération de nouvelles caractéristiques (colonnes) à partir de celles existantes pour fournir des informations supplémentaires au modèle. Elle peut aider à découvrir des relations et des motifs complexes au sein des données.

Disons que nous mélangeons 'Âge' et 'Revenu' pour créer une nouvelle caractéristique appelée 'Revenu par Âge'. Cette nouvelle caractéristique pourrait aider notre modèle à comprendre comment l'argent et l'âge sont liés.

### Exemple de création de caractéristiques

Dans notre ensemble de données, nous pouvons créer une nouvelle caractéristique, 'Revenu par Âge', pour capturer la relation entre le revenu et l'âge. Cela peut être une caractéristique utile pour certaines tâches de prédiction :

```python
# Créer une nouvelle caractéristique 'Revenu par Âge'
df_encoded['Revenu par Âge'] = df_encoded['Revenu'] / df_encoded['Âge']

```

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1022.jpg)
_Sortie du code_

La caractéristique 'Revenu par Âge' fournit une mesure du revenu relatif à l'âge, ce qui pourrait être précieux dans divers scénarios de modélisation. Avec cela, une colonne supplémentaire a été créée.

## Sélection de caractéristiques

La sélection de caractéristiques est le processus de choix des caractéristiques les plus pertinentes pour une tâche de modélisation donnée. Réduire le nombre de caractéristiques peut améliorer la performance du modèle, réduire le surapprentissage et accélérer l'entraînement. Cela facilite le travail de votre modèle car il n'a pas à traiter des choses inutiles.

### Exemple de sélection de caractéristiques

Supposons que nous voulons sélectionner les caractéristiques les plus pertinentes pour prédire la 'Productivité'. Nous pouvons utiliser des techniques de sélection de caractéristiques comme l'élimination récursive de caractéristiques (RFE) avec un modèle de régression linéaire :

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# Séparer la variable cible et les caractéristiques
X = df_encoded.drop('Productivité', axis=1)
y = df_encoded['Productivité']

# Initialiser le modèle de régression linéaire
model = LinearRegression()

# Effectuer RFE avec validation croisée
rfe = RFE(model, n_features_to_select=3)  # Sélectionner les 3 meilleures caractéristiques
fit = rfe.fit(X, y)  # Corrigé : utiliser X au lieu de x

# Imprimer les caractéristiques sélectionnées
selected_features = X.columns[fit.support_]
print('Caractéristiques sélectionnées :', selected_features)
```

À partir de nos données, nous avons utilisé RFE pour sélectionner les 3 meilleures caractéristiques les plus pertinentes pour prédire la 'Productivité'. Cela réduit la dimensionnalité des données et peut améliorer la performance du modèle.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1023-1.jpg)
_Sortie du code_

Cette sortie reçue indique que, selon le processus d'élimination récursive de caractéristiques (RFE), les colonnes : 'Revenu', 'Ville_Miami' et 'Genre_Homme' sont considérées comme les plus importantes ou informatives pour prédire la variable cible 'Productivité' en utilisant un modèle de régression linéaire.

Décomposons l'interprétation :

1. **Revenu** : La caractéristique 'Revenu' est probablement identifiée comme un prédicteur important. Cela suggère que, selon le processus RFE, les changements de revenu ont un impact significatif sur la prédiction de la 'Productivité' basée sur le modèle de régression linéaire donné.
2. **Ville_Miami** : La présence de 'Ville_Miami' comme caractéristique importante suggère que, dans le contexte de nos données, le fait qu'un individu soit de Miami ou non contribue de manière significative à la prédiction de la 'Productivité'.
3. **Genre_Homme** : De même, la caractéristique 'Genre_Homme' est considérée comme importante. Cela implique que, selon le modèle, le genre d'un individu, spécifiquement être un homme, est informatif pour prédire la 'Productivité'.

Il est important de noter que l'interprétation de "l'importance" ici est spécifique au modèle de régression linéaire utilisé en combinaison avec la technique de sélection de caractéristiques RFE. RFE classe les caractéristiques en fonction de leur contribution à la performance du modèle dans la prédiction de la variable cible.

## Binning et Bucketing

Le binning ou bucketing implique le regroupement de données numériques continues en intervalles discrets. Il peut aider à capturer des relations non linéaires et à rendre la modélisation plus robuste.

Considérons un exemple pratique. Basé sur nos données factices, au lieu de traiter la colonne "Âge" comme une variable continue, vous décidez de la regrouper en catégories comme "Jeune", "Milieu de carrière" et "Senior" pour mieux comprendre comment l'âge est lié à la productivité.

Après votre analyse, vous pourriez découvrir que les employés de la catégorie "Milieu de carrière" ont tendance à avoir les niveaux de productivité les plus élevés. Cela ne signifie pas que l'âge cause directement la productivité, mais cela suggère une relation potentielle qui pourrait être influencée par des facteurs tels que l'expérience, le développement des compétences et la familiarité avec le travail.

En regroupant l'âge en catégories, vous avez rendu la relation âge-productivité plus interprétable, ce qui peut fournir à votre modèle des informations plus détaillées.

### Exemple de Binning

Disons que nous voulons créer des bins pour la caractéristique 'Âge'. Nous pouvons utiliser la fonction `cut` de `pandas` pour définir les limites des bins :

```python
# Créer des bins et des labels pour la colonne unique
bins = [-float('inf'), -0.5, 0.5, float('inf')]  # Ajuster les limites des bins si nécessaire
labels = ['Jeune', 'Milieu_Carriere', 'Senior']

# Binner la colonne Âge
df_encoded['Colonne_Binée'] = pd.cut(df_encoded['Âge'], bins=bins, labels=labels, right=False)

# Imprimer le DataFrame mis à jour
df_encoded


```

Le binning de 'Âge' en intervalles discrets permet au modèle de considérer les groupes d'âge comme une caractéristique catégorielle, capturant des relations non linéaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/IMG-1024-1.jpg)
_Sortie du code_

Comme vous pouvez le voir ci-dessus, la colonne 'Âge' a été transformée en une colonne binée, ce qui améliore davantage les informations données au modèle.

## Conclusion

Les techniques d'ingénierie des caractéristiques permettent aux scientifiques des données et aux praticiens du machine learning de créer des caractéristiques plus informatives et pertinentes pour la modélisation.

Dans ce tutoriel, nous avons exploré diverses techniques d'ingénierie des caractéristiques, y compris l'encodage one-hot, la mise à l'échelle des caractéristiques, la création de caractéristiques, la sélection de caractéristiques et le binning.

Expérimentez avec ces techniques pour améliorer vos capacités d'analyse de données et de modélisation. N'oubliez pas que le choix des techniques d'ingénierie des caractéristiques doit être guidé par les exigences spécifiques de votre projet et la nature de vos données.