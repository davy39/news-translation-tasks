---
title: 'Régression linéaire vs régression logistique : comment choisir le bon modèle
  de régression pour vos données'
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-05-28T13:02:08.000Z'
originalURL: https://freecodecamp.org/news/linear-regression-vs-logistic-regression
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Linear-vs-Logistic-Regession.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: MathJax
  slug: mathjax
- name: '#Regression'
  slug: regression
seo_title: 'Régression linéaire vs régression logistique : comment choisir le bon
  modèle de régression pour vos données'
seo_desc: 'Regression models identify trends in a dataset and predict outcomes based
  on the trends they have analyzed and identified.

  Linear and Logistic Regression are two types of regression models that are similar
  but carry out their functions in distinct wa...'
---

Les modèles de régression identifient les tendances dans un ensemble de données et prédisent les résultats en fonction des tendances qu'ils ont analysées et identifiées.

La régression linéaire et la régression logistique sont deux types de modèles de régression qui sont similaires mais qui accomplissent leurs fonctions de manière distincte. Ce sont également deux techniques fondamentales en apprentissage automatique qui prédisent les résultats en analysant les données précédemment fournies.

La régression linéaire et la régression logistique sont toutes deux des modèles d'apprentissage supervisé qui semblent entrelacés – il peut donc être difficile de les distinguer, car elles partagent la même notion de prédiction des résultats en fonction des variables d'entrée.

Mais voici la principale différence : la régression linéaire se concentre sur la prédiction de valeurs continues, tandis que la régression logistique est spécifiquement conçue pour la classification binaire (Oui ou Non). Ainsi, bien qu'elles aient des noms similaires, il existe des différences clés dans leurs applications, leurs équations et leurs objectifs.

Dans cet article, vous apprendrez les similitudes et les différences entre la régression linéaire et la régression logistique, explorerez les caractéristiques clés de chacune et apprendrez à choisir entre elles.

## Table des matières

1. [Comment la régression linéaire et la régression logistique font des prédictions](#heading-comment-la-regression-lineaire-et-la-regression-logistique-font-des-predictions)
   - [Régression linéaire](#heading-regression-lineaire)
   - [Régression logistique](#heading-regression-logistique)

2. [Quelles sont les similitudes entre la régression linéaire et la régression logistique ?](#heading-quelles-sont-les-similitudes-entre-la-regression-lineaire-et-la-regression-logistique)

3. [Quelles sont les différences entre la régression linéaire et la régression logistique ?](#heading-quelles-sont-les-differences-entre-la-regression-lineaire-et-la-regression-logistique)

4. [Quand utiliser la régression linéaire vs la régression logistique pour vos projets de données](#heading-quand-utiliser-la-regression-lineaire-vs-la-regression-logistique-pour-vos-projets-de-donnees)

5. [Quels sont les autres types de modèles de régression ?](#heading-quels-sont-les-autres-types-de-modeles-de-regression)

6. [Conclusion](#heading-conclusion)

## Comment la régression linéaire et la régression logistique font des prédictions

### Régression linéaire

La régression linéaire est la forme la plus simple de régression, supposant une relation linéaire (ligne droite) entre la variable d'entrée et la variable de sortie. En termes simples, elle utilise la puissance d'une ligne droite.

L'équation pour la régression linéaire simple peut être exprimée comme y = mx + b, où :

* y est la variable dépendante

* x est la variable indépendante

* m est la pente

* et b est l'ordonnée à l'origine.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/New-Linear-regression-image-1.png align="left")

*Graphique de régression linéaire ([Source](https://images.app.goo.gl/hnuLSSqSZewaDsN18))*

Dans un ensemble de données sur les prix des maisons, les variables indépendantes sont les colonnes utilisées pour prédire le prix de la maison, telles que la "Surface", les "Chambres", l'"Âge" et l'"Emplacement". La variable dépendante sera la colonne "Prix" – la caractéristique à prédire.

Vous pouvez [en savoir plus sur la régression linéaire ici](https://www.freecodecamp.org/news/how-to-build-a-house-price-prediction-model/).

### Régression logistique

La régression logistique est une technique puissante d'apprentissage automatique supervisé. Elle aide à catégoriser les résultats en deux groupes en supposant une relation linéaire entre les caractéristiques et le résultat, puis en calculant la probabilité que le résultat tombe dans un groupe ou l'autre.

L'équation mathématique calcule une sortie basée sur la relation, et la sortie est ensuite transformée à l'aide d'une fonction sigmoïde pour la contraindre entre `0 et 1`. La voici :

$$y = e^(\beta0 + \beta1X1 + \beta2X2+\ldots \beta nXn) / (1 + e^(\beta0 + \beta1 x 1 + \beta2 x 2 +\ldots \beta n x n))$$

Où :

* y donne la probabilité de succès de la variable catégorielle y

* e (x) est le nombre d'Euler, l'inverse de la fonction logarithme naturel ou fonction sigmoïde, ln (x)

* \beta0 est l'ordonnée à l'origine lorsque toutes les variables d'entrée indépendantes sont égales à 0

* \beta1X1 est le coefficient de régression (B1) de la première variable indépendante (X1), la valeur d'impact de la première variable indépendante sur la variable dépendante

* \beta nXn est le coefficient de régression (BN) de la dernière variable indépendante (XN), lorsqu'il y a plusieurs valeurs d'entrée

![Image](https://www.freecodecamp.org/news/content/images/2024/05/New-Logistic-Regression-image.png align="left")

*Graphique de régression logistique ([Source](https://images.app.goo.gl/vfYBcVSrdvR2Mkki9))*

Cela est couramment utilisé dans des domaines comme la détection de spam et le diagnostic médical. Il est utilisé pour interpréter la probabilité qu'une observation tombe dans une classe spécifique.

Vous pouvez [en savoir plus sur la régression logistique ici](https://dev.to/oluwadamisisamuel1/how-to-build-a-logistic-regression-model-a-spam-filter-tutorial-261b).

## Quelles sont les similitudes entre la régression linéaire et la régression logistique ?

1. **Relation linéaire :** La régression linéaire et la régression logistique supposent toutes deux une relation linéaire entre les caractéristiques d'entrée et la sortie.

2. **Apprentissage supervisé :** Les deux sont des algorithmes d'apprentissage automatique supervisé, ce qui signifie qu'ils nécessitent des données d'entraînement étiquetées.

3. **Limitations :** Les deux algorithmes ont des limitations similaires, notamment :

* Les relations non linéaires entre les variables d'entrée et de sortie conduiront à des résultats inexacts.

* Les données non nettoyées et les valeurs manquantes conduiront à de mauvaises performances du modèle. Vous pouvez [en savoir plus sur le nettoyage des données ici](https://www.freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj/).

* Les deux modèles sont sujets au [surapprentissage](https://www.freecodecamp.org/news/what-is-overfitting-machine-learning/), ce qui réduit l'utilisation de la sélection de caractéristiques.

## Quelles sont les différences entre la régression linéaire et la régression logistique ?

1. **Type de sortie :** La régression linéaire prédit une sortie continue (par exemple, le prix d'une maison) sur un graphique en ligne droite, tandis que la régression logistique prédit des probabilités pour une classification binaire (comme si un patient a un cancer ou non) sur une courbe en forme de S.

2. **Équation et fonction d'activation :** La régression linéaire utilise une équation linéaire simple tandis que la régression logistique utilise la fonction logistique (sigmoïde) pour transformer la sortie en probabilités.

3. **Fonction de perte :** La régression linéaire minimise la somme des différences au carré, tandis que la régression logistique minimise la perte logistique (log loss).

4. **Type d'apprentissage supervisé :** La régression linéaire est un modèle de régression. La régression logistique est un modèle de classification.

## Quand utiliser la régression linéaire vs la régression logistique pour vos projets de données

Vous pouvez utiliser la régression linéaire pour résoudre des problèmes où la relation entre les variables peut être raisonnablement approximée par une ligne droite. Cela signifie qu'elle est bien adaptée pour comprendre les changements progressifs ou les tendances, plutôt que les sauts brusques ou les relations complexes. Voici quelques exemples de cas d'utilisation :

* Prédiction des prix des maisons

* Identification des relations

* Tendances et analyse du marché

* Évaluation des risques commerciaux

* Recherche scientifique

* Estimation des prix

* Comprendre l'impact

D'autre part, la régression logistique est un outil puissant pour comprendre les événements binaires et faire des prédictions basées sur les caractéristiques données. Elle excelle dans le calcul de la probabilité qu'un résultat soit "Oui" ou "Non". Cela s'applique à une large gamme de scénarios comme :

* Détection de fraude

* Filtre anti-spam

* Applications en médecine

* Attrition des clients

* Estimation de probabilité

## Quels sont les autres types de modèles de régression ?

La régression linéaire et la régression logistique ne sont pas les seuls modèles de régression disponibles. Il existe d'autres modèles que vous pouvez utiliser lorsque la régression linéaire et logistique échouent :

* **La régression Ridge** est une technique de régularisation utilisée pour réduire la complexité d'un modèle en introduisant une petite quantité de biais. Elle rend le modèle moins susceptible au surapprentissage.

* **La régression Lasso** est une technique de régularisation qui réduit également la complexité d'un modèle. Elle évite le surapprentissage en réduisant le coefficient pour qu'il devienne plus proche de zéro. Elle est particulièrement utile lorsque la sélection de caractéristiques est cruciale.

* **La régression polynomiale** capture les relations non linéaires en utilisant une ligne courbe. Elle aborde directement les limitations de la régression linéaire et logistique en modélisant une relation non linéaire entre les variables.

## Conclusion

La régression linéaire et la régression logistique partagent le concept fondamental d'une relation linéaire entre les variables d'entrée et les variables de sortie. Mais leurs applications, leurs équations mathématiques et leurs cas d'utilisation diffèrent considérablement.

Comprendre ces différences est crucial lors du choix du modèle approprié pour un problème donné.

Cet article a mis en lumière leur fonctionnement interne et leurs cas d'utilisation, vous équipant ainsi pour faire le bon choix et un choix éclairé. Assurez-vous d'explorer davantage pour augmenter vos connaissances et compétences, et prenez le temps d'apprendre des modèles d'apprentissage automatique plus complexes qui conviendront le mieux à vos problèmes de données.

Si vous avez trouvé cela utile, vous pouvez me contacter sur [LinkedIn](http://www.linkedin.com/in/samuel-oluwadamisi-01b3a4236), [mon blog personnel](https://dev.to/oluwadamisisamuel1) et sur [X (anciennement Twitter)](https://x.com/Data_Steve_).