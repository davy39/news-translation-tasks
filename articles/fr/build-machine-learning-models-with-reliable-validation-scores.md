---
title: Comment construire des modèles de machine learning avec des scores de validation
  fiables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-05T17:15:59.000Z'
originalURL: https://freecodecamp.org/news/build-machine-learning-models-with-reliable-validation-scores
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Untitled-presentation.jpg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Comment construire des modèles de machine learning avec des scores de validation
  fiables
seo_desc: "By Saheed Azeez\nImagine that you took a test in school, and you expected\
  \ to score 80-90% based on how you thought you performed. But when the results came\
  \ out, you learned that you scored 50-60% in the test. You'd be shocked, right?\
  \ \nWell sometimes t..."
---

Par Saheed Azeez

Imaginez que vous passiez un test à l'école et que vous vous attendiez à obtenir un score de 80-90% en fonction de votre performance perçue. Mais lorsque les résultats sont publiés, vous apprenez que vous avez obtenu 50-60%. Vous seriez choqué, n'est-ce pas ?

Eh bien, parfois, ces mêmes scénarios se produisent dans les problèmes de machine learning. Vous pouvez construire un modèle de machine learning avec une très bonne performance de validation, mais dans le monde réel, la performance du modèle est moins bonne.

Un exemple pratique est d'être bien classé dans le tableau de bord public d'un concours de machine learning sur [Kaggle](https://www.kaggle.com/) et, lorsque le tableau de bord privé (final) est publié, votre classement chute.

Dans cet article, je vais discuter de la manière de construire des modèles dont les scores de validation sont plus proches des performances réelles. Je vais également parler des raisons pour lesquelles les scores de validation sont souvent très différents des performances réelles ou des performances du tableau de bord (pour les compétitions de machine learning). Enfin, je donnerai quelques conseils pour vous aider à réduire cette différence de performance.

### Voici ce que nous allons couvrir :

1. [Prérequis](#heading-prerequisites)
2. [Qu'est-ce que les scores de validation en machine learning ?](#heading-quest-ce-que-les-scores-de-validation-en-machine-learning)
3. [Comment construire un modèle avec de bons scores de validation](#heading-comment-construire-un-modele-avec-de-bons-scores-de-validation)
* [Sélectionner les bonnes métriques d'évaluation](#select-the-right-evaluation-metrics)
* [Sélectionner la bonne division train-validation](#select-the-right-train-validation-split)
* [Gérer les données d'entraînement et de test de distributions différentes](#handle-train-and-test-data-of-different-distributions)
* [Gérer les fuites de données](#manage-data-leakage)
* [Supprimer les doublons](#drop-duplicate-date-points)
* [Traiter correctement les valeurs aberrantes](#properly-deal-with-any-outliers)
* [Essayer la validation croisée](#try-cross-validation)
4. [Conclusion](#heading-conclusion)

## Prérequis

Si vous avez déjà construit un modèle de machine learning, alors vous devriez être en mesure de comprendre et d'apprendre de cet article.

## Qu'est-ce que les scores de validation en machine learning ?

Pour comprendre ce qu'est un score de validation, vous devez d'abord comprendre les différents types de jeux de données utilisés dans l'entraînement et l'évaluation des modèles.

Tout d'abord, un **jeu de données d'entraînement** est le jeu de données initial sur lequel vous souhaitez construire votre modèle. Votre modèle apprendra ses paramètres à partir des données d'entraînement. Cela est généralement représenté par _X_ ou _x_ ou _train_ dans la plupart des notebooks.

Après avoir construit votre modèle sur les données d'entraînement, vous voudrez voir comment votre modèle se comporte sur des données qu'il n'a jamais vues auparavant. C'est là que les **données de validation** interviennent. Comme leur nom l'indique, vous les utilisez pour valider la performance de votre modèle.

Mais la plupart du temps, vous n'aurez pas de données de validation séparées à utiliser – vous devrez donc extraire un pourcentage de vos données d'entraînement pour valider le modèle. La performance de votre modèle sur les données de validation est ce qu'on appelle le **score de validation** ou **performance de validation**.

Cela est important car vous construisez (ou construirez éventuellement) un modèle pour résoudre un problème commercial ou réel. Le modèle sera utilisé pour prédire des instances pour lesquelles vous n'aurez pas de réponses (cible), et cette prédiction est ce qui compte le plus.

Dans le cadre d'une compétition de machine learning, vous pouvez appeler ce problème réel les **données de test**. La performance que votre modèle exhibe sur ces données est ce qu'on appelle la **performance réelle**.

Remarque : Ce que j'appelle données de validation peut également être appelé données de test par d'autres ingénieurs, et ce que j'appelle données de test peut être appelé données de performance réelle. J'ai donné cette description basée sur mon expérience des concours de Machine Learning.

## Comment construire un modèle avec de bons scores de validation

### 1) Sélectionner les bonnes métriques d'évaluation

L'une des premières étapes avant de construire un modèle basé sur vos données est d'identifier ce qui fait un bon modèle. Vous devriez vous poser la question "Pourquoi le modèle A devrait-il être meilleur que le modèle B" ? Vous devez utiliser une sorte de score qui évalue la performance d'un modèle par rapport à un autre.

Il existe de nombreuses métriques pour les problèmes de **classification** (f1-score, précision, roc auc score et bien d'autres) et de **régression** (erreur quadratique moyenne, erreur absolue moyenne, erreur absolue en pourcentage moyenne, etc.).

Les métriques d'évaluation doivent également se traduire par l'application réelle du modèle.

Par exemple, la métrique d'évaluation pour un modèle de régression ouvert aux valeurs aberrantes **devrait être l'erreur quadratique moyenne** et non **l'erreur absolue moyenne**. Pour les problèmes de classification impliquant des données déséquilibrées, les métriques d'évaluation préférées devraient être le **f1_score** plutôt que la **précision**, car il prend en compte le déséquilibre des données dans son calcul. Et ainsi de suite.

Voici un exemple d'application de métriques d'évaluation sur un problème de régression simple :

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Générer un jeu de données d'exemple à des fins de démonstration, avec 1000 points de données et 10 caractéristiques
X, y = make_regression(n_samples=1000, n_features=10, noise=0.5, random_state=42)

# Diviser le jeu de données en ensembles d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression (Régression linéaire dans cet exemple)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = regressor.predict(X_val)

# Calculer les métriques de régression
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

# Afficher les résultats
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/regression-metrics-1.png)
_Résultat des métriques_

Et voici un exemple d'application de métriques d'évaluation sur un problème de classification simple :

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Générer un jeu de données d'exemple à des fins de démonstration
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Diviser le jeu de données en ensembles d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un classificateur (Forêt aléatoire dans cet exemple)
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de validation
y_pred = classifier.predict(X_val)
y_proba = classifier.predict_proba(X_val)[:, 1]  # Estimations de probabilité pour ROC-AUC et log_loss

# Calculer les métriques de classification
accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)
roc_auc = roc_auc_score(y_val, y_proba)
logloss = log_loss(y_val, y_proba)

# Afficher les résultats
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC-AUC Score: {roc_auc:.4f}")
print(f"Log Loss: {logloss:.4f}")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/classification-metrics.png)
_Le résultat_

### 2) Sélectionner la bonne division train-validation

Comme je l'ai mentionné précédemment, de nombreuses fois, vous devrez extraire un pourcentage de vos données d'entraînement pour les utiliser comme données de validation.

Vous êtes peut-être familier avec la ligne de code ci-dessous qui aide à diviser les données :

```python
# Diviser le jeu de données en ensembles d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
```

Alors, comment savoir quel pourcentage de division utiliser ?

Eh bien, une réponse simple est de trouver un équilibre entre un pourcentage de division qui n'est pas trop grand – après tout, vous ne voulez pas extraire trop de vos données d'entraînement et perdre des informations – et un qui n'est pas trop petit – afin que vos données de validation ne soient pas trop petites et que vous puissiez faire confiance aux scores de validation que vous obtiendrez.

Pour les problèmes de machine learning tabulaires, un pourcentage de division entre **10% (0.1)** et **25% (0.25)** devrait être suffisant.

### 3) Gérer les données d'entraînement et de test de distributions différentes

Il arrive que les données d'entraînement et les données de test (ou l'endroit où le modèle sera appliqué) aient des distributions différentes.

Par exemple, supposons que nous construisons un modèle pour prédire les défauts de paiement de prêts. Mais alors que les données d'entraînement disponibles proviennent de Londres, le modèle est destiné aux utilisateurs de Lagos. Bien que, dans une certaine mesure, les comportements des utilisateurs soient universels, il y aura des différences de mode de vie ou de revenu entre les lieux qui se refléteront dans les données et pourraient également affecter la performance du modèle.

Puisque vos données de validation sont extraites des données d'entraînement (emplacement de Londres), le score de validation pourrait ne pas être très fiable, car le modèle (entraîné sur les utilisateurs de Londres) pourrait donner, par exemple, une précision de 75% sur les données de validation (utilisateurs de Londres) – mais il pourrait avoir une précision moins bonne dans le monde réel, à Lagos, car la **distribution des données est différente !**

La solution ici serait de **supprimer certaines caractéristiques** qui pourraient être liées au mode de vie de Londres et non à celui de Lagos. Vous devrez peut-être faire une exploration des données pour identifier ces caractéristiques – ou mieux encore, obtenir des données de Lagos pour entraîner le modèle si elles sont disponibles.

Ce n'est qu'un exemple montrant comment les différences de distribution des données basées sur l'emplacement peuvent affecter les résultats de votre modèle. Il existe de nombreux autres facteurs qui peuvent causer des différences de distribution des données comme les variations culturelles, économiques ou démographiques.

Vous pouvez supprimer des caractéristiques avec la ligne de code ci-dessous :

```python
caracteristiques_supprimees = ["caracteristique1", "caracteristique2", "caracteristique3"]  # Une liste de caractéristiques que vous souhaitez supprimer
donnees.drop(caracteristiques_supprimees, axis=1, inplace=True)

```

### 4) Gérer les fuites de données

Vous seriez très heureux si votre modèle obtenait un f1_score de 99% ou une erreur quadratique moyenne proche de 0, dans votre performance de validation. Eh bien, de tels modèles sont principalement irréalistes dans le monde réel, et se produisent principalement en raison de **fuites de données**.

Les fuites de données se produisent lorsque votre modèle apprend des motifs ou des informations pendant l'entraînement qui ne seront pas disponibles lors du déploiement réel ou de l'utilisation dans le monde réel du modèle.

Une cause courante de fuite de données est lorsque vous oubliez de supprimer votre colonne cible ou d'autres colonnes qui ne seront pas disponibles dans le monde réel lorsque vous appliquez votre modèle à partir de vos données d'entraînement avant d'entraîner le modèle. Puisque vos données de validation auront également ces mêmes informations (puisqu'elles sont extraites de vos données d'entraînement), elles donneront ainsi un **score irréaliste** qui ne sera pas atteignable dans le monde réel.

Une autre cause est lorsque vous avez des colonnes qui indiquent des valeurs futures. Supposons que vous prédisez les prix des actions, et que votre jeu de données inclut une caractéristique qui représente les prix moyens futurs des actions de cette semaine. Cela pourrait causer une fuite de données futures car dans le monde réel, vous n'aurez pas le prix moyen des actions de cette semaine (qui inclut des valeurs du futur) à l'avance.

Pour prévenir les fuites de données, il est essentiel de pré-traiter et de nettoyer soigneusement les données pour s'assurer que seules les informations disponibles au moment de la prédiction sont utilisées pendant l'entraînement.

Vous pouvez également diviser les données en ensembles d'entraînement et de validation avant toute étape de pré-traitement des données pour simuler un scénario réel pour votre ensemble de validation. Soyez prudent lorsque vous utilisez des données temporelles, et assurez-vous que les informations futures ne sont pas incluses lors de l'entraînement du modèle.

### 5) Supprimer les doublons

Il arrive souvent que les données d'entraînement que vous recevrez contiennent des doublons (instances de données où toutes les colonnes ont les mêmes valeurs). Dans ces cas, lorsque vous divisez les données en entraînement et validation, il y a une forte probabilité que certaines instances de données dans l'entraînement se retrouvent également dans l'ensemble de validation.

Vous voudrez éviter cela, car le score de validation que vous obtiendrez ne reflétera pas la véritable performance de votre modèle dans le monde réel, car votre modèle a déjà vu certaines des instances de données que vous utilisez pour le valider pendant l'entraînement. C'est comme voir les questions de votre examen à l'avance.

Il est donc important de **supprimer les doublons** avant de diviser les données en entraînement et validation.

La suppression des doublons dans les dataframes peut facilement être effectuée avec [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) comme ceci :

```python
# où df est votre dataframe
df.drop_duplicates(subset=None
                   keep='first',
                   inplace=False, 
                   ignore_index=False)
```

### 6) Éviter le surapprentissage

Le surapprentissage se produit lorsque votre modèle apprend trop bien à partir des données d'entraînement, capturant du bruit et des motifs spécifiques qui ne sont pas généralisables à de nouvelles données.

Puisque vos données de validation sont un sous-ensemble extrait de vos données d'entraînement, le score de validation pourrait être **élevé**, mais la performance dans le monde réel sera **mauvaise**.

Vous pouvez réduire l'effet de la régularisation en appliquant des techniques sur votre modèle telles que le dropout (pour les réseaux de neurones), l'élagage (pour les arbres de décision), ou en ajoutant des termes de régularisation aux modèles linéaires.

De plus, ajustez soigneusement les hyperparamètres pour trouver le bon équilibre entre la complexité du modèle et la généralisation.

### 7) Traiter correctement les valeurs aberrantes

Les valeurs aberrantes sont des points de données qui s'écartent considérablement du reste du jeu de données. Elles peuvent avoir un impact substantiel sur la performance de votre modèle, en particulier si elles sont présentes dans les colonnes **cibles** des problèmes de régression. La présence de valeurs aberrantes peut rendre les scores de validation pour les problèmes de régression très peu fiables.

Voyons un exemple :

**Sans valeurs aberrantes :**

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Exemple de sortie cible
actual_val_target = [10, 5, 6, 7, 8, 10, 2, 8, 12, 13]
# Exemple de prédiction d'un modèle
predicted_val_target = [9.5, 5.2, 5.8, 7.3, 7.5, 10.4, 0.5, 8.1, 12.5, 12.8]

print(f"Root mean square error sans valeurs aberrantes {mean_squared_error(actual_val_target, predicted_val_target, squared=False)}")
print(f"Mean absolute error sans valeurs aberrantes {mean_absolute_error(actual_val_target, predicted_val_target)}")
```

Le résultat peut être vu ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1703858169667/8e2156bc-4abe-4820-9d10-5bc91562af8d.png)

**Avec une valeur aberrante (50) :**

```python

# 13 a été remplacé par 50 pour être une valeur aberrante
actual_val_target = [10, 5, 6, 7, 8, 10, 2, 8, 12, 50]
predicted_val_target = [9.5, 5.2, 5.8, 7.3, 7.5, 10.4, 0.5, 8.1, 12.5, 12.8]

print(f"Root mean square error avec valeurs aberrantes {mean_squared_error(actual_val_target, predicted_val_target, squared=False)}")
print(f"Mean absolute error avec valeurs aberrantes {mean_absolute_error(actual_val_target, predicted_val_target)}")
```

Résultat :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1703858201531/73eb5b50-b7e4-4770-9e0f-457fbdcfd24b.png)

Vous pouvez voir qu'une seule valeur aberrante peut affecter le score de validation et le rendre peu fiable. Il est donc crucial de traiter les valeurs aberrantes de manière appropriée.

Quelques conseils pour gérer les valeurs aberrantes :

* **Identifier et comprendre les valeurs aberrantes :** Utilisez des méthodes statistiques ou des techniques de visualisation pour identifier les valeurs aberrantes dans vos données. Comprenez si ces valeurs aberrantes sont des points de données authentiques ou des erreurs de collecte de données.
* **Stratégies de traitement :** Selon la nature des valeurs aberrantes, vous pouvez choisir de les supprimer, de les transformer ou d'utiliser des modèles robustes qui sont moins sensibles aux valeurs extrêmes.
* **Traitement cohérent :** Assurez-vous que les mêmes techniques de gestion des valeurs aberrantes sont appliquées de manière cohérente aux ensembles de données d'entraînement et de validation pour maintenir la cohérence dans le prétraitement des données.

### 8) Essayer la validation croisée

Lors de la construction de modèles, vous divisez généralement les données en deux (entraînement et validation). Mais en entraînant le modèle uniquement sur l'entraînement, vous avez perdu tous les motifs qui peuvent être appris à partir des données de validation.

Et si vous divisez vos données en plusieurs plis ?

Vous pouvez valider le modèle sur un pli et construire le modèle sur les autres. Faites cela jusqu'à ce que vous ayez utilisé tous les plis comme validations. Ainsi, si vos données étaient divisées en 10 plis, vous pouvez construire des modèles sur 10 sous-échantillons des données. C'est ce qu'est la validation croisée.

Vous pouvez trouver la moyenne des scores de validation sur chaque pli et cela aide à fournir une estimation plus robuste de la manière dont votre modèle se généralise aux données invisibles.

```python
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Générer un jeu de données synthétique à des fins de démonstration
X, y = make_regression(n_samples=1000, n_features=10, noise=0.5, random_state=42)

# Créer un modèle de régression linéaire
regressor = LinearRegression()

# Exemple utilisant cross_val_score
cv_scores = cross_val_score(regressor, X, y, cv=5, scoring='neg_mean_squared_error')
rmse_scores = np.sqrt(-cv_scores)  # Prendre la racine carrée pour obtenir RMSE

print("Scores RMSE validés croisés :", rmse_scores)
print("RMSE moyen :", np.mean(rmse_scores))

# Exemple utilisant cross_val_predict
predicted_values = cross_val_predict(regressor, X, y, cv=5)
```

Pour plus de détails sur la validation croisée, vous pouvez consulter la documentation de sklearn sur [_cross_val_score_](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html) et [_cross_val_predict_](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate).

## Conclusion

Le point le plus important à retenir de cet article est que vous devez essayer autant que possible de simuler un scénario réel pour votre ensemble de validation afin que votre score de validation puisse être aussi fiable que possible.

Je vous souhaite le meilleur pour vos futurs modèles.

Merci !