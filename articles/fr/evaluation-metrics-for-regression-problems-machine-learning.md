---
title: Principaux indicateurs d'évaluation pour les problèmes de régression en Machine
  Learning
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-08-01T14:37:27.000Z'
originalURL: https://freecodecamp.org/news/evaluation-metrics-for-regression-problems-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/regression-metrics-image.jpeg
tags:
- name: Machine Learning
  slug: machine-learning
- name: metrics
  slug: metrics
- name: '#Regression'
  slug: regression
seo_title: Principaux indicateurs d'évaluation pour les problèmes de régression en
  Machine Learning
seo_desc: 'A regression problem is a common type of supervised learning problem in
  Machine Learning. The end goal is to predict quantitative values – for example,
  continuous values such as the price of a car, the weight of a dog, and so on.

  But to be sure that ...'
---

Un problème de régression est un type courant de problème d'apprentissage supervisé en Machine Learning. L'objectif final est de prédire des valeurs quantitatives – par exemple, des valeurs continues telles que le prix d'une voiture, le poids d'un chien, et ainsi de suite.

Mais pour être sûr que votre modèle performe bien dans ses prédictions, vous devez évaluer le modèle.

Il existe certains indicateurs d'évaluation qui peuvent vous aider à déterminer si les prédictions du modèle sont précises à un certain niveau de performance.

Dans ce tutoriel, vous apprendrez les principaux indicateurs d'évaluation pour les problèmes de régression, ainsi que quand utiliser chacun d'eux. Sans plus attendre, commençons.

## Qu'est-ce que les Résidus ?

Avant d'aborder les principaux indicateurs d'évaluation, vous devez comprendre ce que signifie "résidu" lorsque vous évaluez un modèle de régression.

Il n'est pas idéal ou possible pour un modèle de prédire avec précision la valeur d'une variable continue dans un problème de régression. Un modèle de régression ne peut prédire que des valeurs inférieures ou supérieures à la valeur réelle. Par conséquent, le seul moyen de déterminer la précision du modèle est par les résidus.

Les résidus sont la différence entre les valeurs réelles et prédites. Vous pouvez considérer les résidus comme une distance. Ainsi, plus le résidu est proche de zéro, mieux notre modèle performe dans ses prédictions.

Voici la formule pour calculer les résidus :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/residuals.png align="left")

```javascript
Dans la formule ci-dessus :

ei -- représente la valeur du résidu.
yi -- représente la valeur réelle.
y^i -- représente la valeur prédite.

Par exemple, si la valeur réelle dans le jeu de données est 5 et la valeur prédite est 8, la valeur du résidu sera -3.
```

## Principaux indicateurs d'évaluation pour les problèmes de régression

Les principaux indicateurs d'évaluation que vous devez connaître pour les problèmes de régression incluent :

### Score R2

Le score R2 (prononcé R-Squared Score) est une mesure statistique qui nous indique à quel point notre modèle réalise toutes ses prédictions sur une échelle de zéro à un.

Comme mentionné ci-dessus, il n'est pas idéal pour un modèle de prédire les valeurs réelles dans un problème de régression (contrairement à un problème de classification qui a des niveaux discrets de valeur).

Mais nous pouvons utiliser le score R2 pour déterminer la précision de notre modèle en termes de distance ou de résidu. Vous pouvez calculer le score R2 en utilisant la formule ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image.png align="left")

#### Quand utiliser le score R2

Vous pouvez utiliser le score R2 pour obtenir la précision de votre modèle sur une échelle de pourcentage, c'est-à-dire 0–100, tout comme dans un modèle de classification.

Examinons comment implémenter le score R2 en Python. Nous avons donc un petit jeu de données qui contient les valeurs réelles et les prédictions.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_mzvi2wZRSVv5W0pPmod3ag.png align="left")

Pour implémenter le score R2 en Python, nous allons utiliser la bibliothèque d'indicateurs d'évaluation Scikit-Learn.

```python
from sklearn.metrics import r2_score
score = r2_score(data["Actual Value"], data["Preds"])
print("La précision de notre modèle est {}%".format(round(score, 2) *100))
```

La fonction `r2_score` nécessite deux paramètres – la valeur réelle et les valeurs prédites que nous lui avons passées ci-dessus. Le résultat de l'indicateur est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_0xW0Hg0DXj5vhFJoAGC_nw-1.png align="left")

Nous pouvons donc dire que notre modèle a prédit ces valeurs avec une précision de 82 %.

### Erreur Absolue Moyenne (MAE)

La MAE est simplement définie comme la somme de toutes les distances/résidus (la différence entre la valeur réelle et la valeur prédite) divisée par le nombre total de points dans le jeu de données.

C'est la distance moyenne absolue de notre prédiction de modèle.

Vous pouvez calculer la MAE en utilisant la formule suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_tu6FSDz_FhQbR3UHQIaZNg.png align="left")

Nous pouvons voir que la formule ci-dessus a deux pipelines représentés par le symbole absolu. Le symbole absolu garantit que le résidu négatif (qui peut être un résultat où la valeur prédite est supérieure à la valeur réelle) est converti en positif afin qu'il n'annule pas les autres résidus positifs.

#### Quand utiliser la MAE

Si vous voulez connaître la distance absolue moyenne du modèle lors d'une prédiction, vous pouvez utiliser la MAE. En d'autres termes, vous voulez savoir à quel point les prédictions sont proches de la valeur réelle du modèle en moyenne.

Gardez simplement à l'esprit que les valeurs faibles de MAE indiquent que le modèle prédit correctement. Les valeurs élevées de MAE indiquent que le modèle est mauvais en prédiction.

Voyons maintenant comment implémenter la MAE en Python. Nous allons travailler avec le jeu de données précédent que nous avons utilisé pour trouver le r2_score.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_mzvi2wZRSVv5W0pPmod3ag.png align="left")

Pour implémenter la MAE en Python, nous allons utiliser la bibliothèque d'indicateurs d'évaluation Scikit-Learn.

```python
from sklearn.metrics import mean_absolute_error
score = mean_absolute_error(data["Actual Value"], data["Preds"])
print("L'erreur absolue moyenne de notre modèle est {}".format(round(score, 2)))
```

La MAE nécessite également deux paramètres, la valeur réelle et la valeur prédite.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_muu_mmrUYI6YFn2_LnD8Rw.png align="left")

### Erreur Quadratique Moyenne (RMSE)

Un autre indicateur couramment utilisé est l'erreur quadratique moyenne, qui est la racine carrée de la distance quadratique moyenne (différence entre la valeur réelle et la valeur prédite).

La RMSE est définie comme la racine carrée de tous les carrés de la distance divisée par le nombre total de points.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/0_2IuTz3Tr_dYNc6Df.png align="left")

La RMSE fonctionne de manière similaire à la MAE (c'est-à-dire que vous l'utilisez pour déterminer à quel point la prédiction est proche de la valeur réelle en moyenne), mais avec une légère différence.

Vous utilisez la RMSE pour déterminer s'il y a des erreurs ou des distances importantes qui pourraient être causées si le modèle a surestimé la prédiction (c'est-à-dire que le modèle a prédit des valeurs significativement plus élevées que la valeur réelle) ou sous-estimé les prédictions (c'est-à-dire, des valeurs prédites inférieures à la prédiction réelle).

#### Quand utiliser la RMSE

Si vous êtes préoccupé par les grandes erreurs, la RMSE est un bon indicateur à utiliser. Si le modèle a surestimé ou sous-estimé certains points dans la prédiction (parce que le résidu sera au carré, entraînant une grande erreur), vous devriez utiliser la RMSE.

La RMSE est un indicateur d'évaluation populaire pour les problèmes de régression car elle calcule non seulement à quel point la prédiction est proche de la valeur réelle en moyenne, mais elle indique également l'effet des grandes erreurs. Les grandes erreurs auront un impact sur le résultat de la RMSE.

Examinons comment vous pouvez implémenter la RMSE en Python.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_mzvi2wZRSVv5W0pPmod3ag-2.png align="left")

La bibliothèque d'indicateurs d'évaluation Scikit-learn n'a pas de métrique RMSE, mais elle inclut la méthode de l'erreur quadratique moyenne. La racine carrée de l'erreur quadratique moyenne est appelée RMSE.

Pour obtenir la RMSE, nous pouvons utiliser la méthode de racine carrée de Numpy pour trouver la racine carrée de l'erreur quadratique moyenne, et le résultat obtenu est notre RMSE.

```python
from sklearn.metrics import mean_squared_error
import numpy as np
score = np.sqrt(mean_squared_error(data["Actual Value"], data["Preds"]))
print("L'erreur quadratique moyenne de notre modèle est {}".format(round(score, 2)))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1_URsnCspxUYxXV5vlacxcew.png align="left")

Nous pouvons voir que la valeur de la RMSE est plus grande que celle de la MAE. Cela est dû à certaines grandes erreurs dans le jeu de données.

## Conclusion et ressources supplémentaires

Dans ce tutoriel, vous avez appris certains des principaux indicateurs d'évaluation pour les problèmes de régression que vous utiliserez au quotidien.

Merci d'avoir lu. Voici quelques ressources utiles que j'ai également incluses ci-dessous.

%[https://scikit-learn.org/stable/modules/model_evaluation.html]

[MAE et RMSE – Quel indicateur est le meilleur ? | par JJ | Human in a Machine World | Medium](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d)