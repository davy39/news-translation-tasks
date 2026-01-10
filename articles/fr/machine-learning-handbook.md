---
title: Manuel des Fondamentaux du Machine Learning – Concepts Clés, Algorithmes et
  Exemples de Code Python
subtitle: ''
author: Tatev Aslanyan
co_authors: []
series: null
date: '2023-10-24T14:59:14.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/The-Machine-Learning-Fundamentals-Handbook-Cover.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: handbook
  slug: handbook
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Manuel des Fondamentaux du Machine Learning – Concepts Clés, Algorithmes
  et Exemples de Code Python
seo_desc: 'If you''re planning to become a Machine Learning Engineer, Data Scientist,
  or you want to refresh your memory before your interviews, this handbook is for
  you.

  In it, we''ll cover the key Machine Learning algorithms you''ll need to know as
  a Data Scient...'
---

Si vous prévoyez de devenir Ingénieur en Machine Learning, Scientifique des Données, ou si vous souhaitez rafraîchir votre mémoire avant vos entretiens, ce manuel est fait pour vous.

Dans ce manuel, nous couvrirons les algorithmes clés du Machine Learning que vous devez connaître en tant que Scientifique des Données, Ingénieur en Machine Learning, Chercheur en Machine Learning et Ingénieur IA.

Tout au long de ce manuel, j'inclurai des exemples pour chaque algorithme de Machine Learning avec son code Python pour vous aider à comprendre ce que vous apprenez.

Que vous soyez débutant ou que vous ayez une certaine expérience avec le Machine Learning ou l'IA, ce guide est conçu pour vous aider à comprendre les fondamentaux des algorithmes de Machine Learning à un niveau élevé.

En tant que praticien expérimenté du machine learning, je suis ravi de partager mes connaissances et mes perspectives avec vous.

## Ce que vous allez apprendre

1. [**Chapitre 1 : Qu'est-ce que le Machine Learning ?**](#heading-chapter-1-quest-ce-que-le-machine-learning)

2. [**Chapitre 2 : Les algorithmes de Machine Learning les plus populaires**](#heading-chapter-2-les-algorithmes-de-machine-learning-les-plus-populaires)

* 2.1 Régression Linéaire et Moindres Carrés Ordinaires (OLS)

* 2.2 Régression Logistique et MLE

* 2.3 Analyse Discriminante Linéaire (LDA)

* 2.4 Régression Logistique vs LDA

* 2.5 Naïve Bayes

* 2.6 Naïve Bayes vs Régression Logistique

* 2.7 Arbres de Décision

* 2.8 Bagging

* 2.9 Forêt Aléatoire

* 2.10 Boosting ou Techniques d'Ensemble (AdaBoost, GBM, XGBoost)

[**3. Chapitre 3 : Sélection de Caractéristiques**](#heading-chapter-3-selection-de-caracteristiques-en-machine-learning)

* 3.1 Sélection de Sous-ensembles

* 3.2 Régularisation (Ridge et Lasso)

* 3.3 Réduction de Dimensionalité (PCA)

[**4. Chapitre 4 : Technique de Rééchantillonnage**](#heading-chapter-4-techniques-de-reechantillonnage-en-machine-learning)

* 4.1 Validation Croisée : (Ensemble de Validation, LOOCV, K-Fold CV)

* 4.2 k optimal dans K-Fold CV

* 4.5 Bootstrapping

[**5. Chapitre 5 : Techniques d'Optimisation**](#heading-chapter-5-techniques-doptimisation)

* 5.1 Techniques d'Optimisation : Descente de Gradient par Lots (GD)

* 5.2 Techniques d'Optimisation : Descente de Gradient Stochastique (SGD)

* 5.3 Techniques d'Optimisation : SGD avec Momentum

* 5.4 Optimiseur Adam

[**6. Clôture**](#heading-a-propos-de-lauteur-cest-moi)

* 6.1 Points Clés à Retenir & La Suite

* 6.2 À Propos de l'Auteur — C'est Moi !

* 6.3 Comment Pouvez-Vous Approfondir ?

* 6.4 Connectez-vous avec Moi

## Prérequis

Pour tirer le meilleur parti de ce manuel, il sera utile d'être familier avec certains concepts clés du ML :

### Terminologie de Base :

* Données d'Entraînement & Données de Test : Ensembles de données utilisés pour entraîner et évaluer les modèles.

* Caractéristiques : Variables aidant aux prédictions, nous les appelons également variables indépendantes

* Variable Cible : Le résultat prédit, également appelé variable dépendante ou variable de réponse

### Problème de Surapprentissage en Machine Learning

Comprendre le surapprentissage, comment il est lié au compromis biais-variance, et comment vous pouvez le corriger est très important. Nous examinerons également en détail les techniques de régularisation dans ce guide. Pour une compréhension détaillée, référez-vous à :

%[https://towardsdatascience.com/bias-variance-trade-off-overfitting-regularization-in-machine-learning-d79c6d8f20b4] 

### Lectures Fondamentales pour les Débutants

Si vous n'avez aucune connaissance statistique préalable et souhaitez apprendre ou rafraîchir votre compréhension des concepts statistiques essentiels, je recommande cet article : [**Concepts Statistiques Fondamentaux pour la Science des Données**](https://link-to-article.com/)

Pour un guide complet sur le lancement d'une carrière en Science des Données et IA, et des informations sur la sécurisation d'un emploi en Science des Données, vous pouvez vous plonger dans mon précédent manuel : [**Lancement de Votre Carrière en Science des Données & IA**](https://link-to-handbook.com/)

### Outils/Langages à utiliser en Machine Learning

En tant que Chercheur en Machine Learning ou Ingénieur en Machine Learning, il existe de nombreux outils techniques et langages de programmation que vous pourriez utiliser dans votre travail quotidien. Mais pour aujourd'hui et pour ce manuel, nous utiliserons le langage de programmation et les outils :

1. Bases de Python : Variables, types de données, structures et mécanismes de contrôle.

2. Bibliothèques Essentielles : `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `xgboost`

3. Environnement : Familiarité avec Jupyter Notebooks ou PyCharm comme IDE.

Se lancer dans ce voyage du Machine Learning avec une base solide assure une expérience plus profonde et éclairante.

Maintenant, commençons-nous ?

## Chapitre 1 : Qu'est-ce que le Machine Learning ?

Le Machine Learning (ML), une branche de l'intelligence artificielle (IA), fait référence à la capacité d'un ordinateur à apprendre de manière autonome à partir de motifs de données et à prendre des décisions sans programmation explicite. Les machines utilisent des algorithmes statistiques pour améliorer la prise de décision et la performance des tâches.

Au cœur du ML, il s'agit d'une méthode où les ordinateurs s'améliorent dans les tâches en apprenant à partir des données. Imaginez cela comme enseigner aux ordinateurs à prendre des décisions en leur fournissant des exemples, un peu comme montrer des images pour enseigner à un enfant à reconnaître des animaux.

Par exemple, en analysant les habitudes d'achat, les algorithmes de ML peuvent aider les plateformes de shopping en ligne à recommander des produits (comme Amazon suggère des articles que vous pourriez aimer).

Ou considérons les plateformes de messagerie qui apprennent à marquer le spam en reconnaissant des motifs dans les courriers indésirables. En utilisant des techniques de ML, les ordinateurs améliorent discrètement nos expériences numériques quotidiennes, rendant les recommandations plus précises et protégeant nos boîtes de réception.

Au cours de ce voyage, vous découvrirez le monde fascinant du ML, où la technologie apprend et grandit à partir des informations qu'elle rencontre. Mais avant de le faire, examinons quelques bases du Machine Learning que vous devez connaître pour comprendre tout type de modèle de Machine Learning.

### Types d'Apprentissage en Machine Learning :

Il existe trois principales façons dont les modèles peuvent apprendre :

* Apprentissage Supervisé : Les modèles prédisent à partir de données étiquetées (vous avez à la fois les caractéristiques et les étiquettes, X et Y)

* Apprentissage Non Supervisé : Les modèles identifient des motifs de manière autonome, où vous n'avez pas de données étiquetées (vous n'avez que des caractéristiques, pas de variable de réponse, seulement X)

* Apprentissage par Renforcement : Les algorithmes apprennent via des retours d'action.

### Métriques d'Évaluation des Modèles :

En Machine Learning, chaque fois que vous entraînez un modèle, vous devez toujours l'évaluer. Et vous voudrez utiliser le type d'évaluation le plus courant en fonction de la nature de votre problème.

Voici les métriques d'évaluation des modèles ML les plus courantes par type de modèle :

1. Métriques de Régression :

* MAE, MSE, RMSE : Mesurent les différences entre les valeurs prédites et les valeurs réelles.

* R-Carré : Indique la variance expliquée par le modèle.

2. Métriques de Classification :

* Précision : Pourcentage de prédictions correctes.

* Précision, Rappel, F1-Score : Évaluent la qualité des prédictions.

* Courbe ROC, AUC : Évaluent le pouvoir discriminatoire du modèle.

* Matrice de Confusion : Compare les classifications réelles vs prédites.

3. Métriques de Clustering :

* Score de Silhouette : Évalue la similarité des objets au sein des clusters.

* Indice de Davies-Bouldin : Évalue la séparation des clusters.

## Chapitre 2 : Algorithmes de Machine Learning les plus populaires

Dans ce chapitre, nous allons simplifier la complexité des algorithmes essentiels de Machine Learning (ML). Ce sera une ressource précieuse pour les rôles allant des Scientifiques des Données aux Ingénieurs en Machine Learning en passant par les Chercheurs en IA.

Nous commencerons par les bases en 2.1 avec la Régression Linéaire et les Moindres Carrés Ordinaires (OLS), puis nous passerons à la section 2.2 qui explore la Régression Logistique et l'Estimation par Maximum de Vraisemblance (MLE).

La section 2.3 explore l'Analyse Discriminante Linéaire (LDA), qui est contrastée avec la Régression Logistique en 2.4. Nous abordons Naïve Bayes en 2.5, offrant une analyse comparative avec la Régression Logistique en 2.6.

En 2.7, nous passons en revue les Arbres de Décision, explorant ensuite les méthodes d'ensemble : le Bagging en 2.8, et la Forêt Aléatoire en 2.9. Diverses techniques de Boosting populaires se déroulent dans les segments suivants, discutant d'AdaBoost en 2.10, du Modèle de Boosting de Gradient (GBM) en 2.11, et concluant avec l'Extreme Gradient Boosting (XGBoost) en 2.12.

Tous les algorithmes que nous allons discuter ici sont fondamentaux et populaires dans le domaine, et chaque Scientifique des Données, Ingénieur en Machine Learning et Chercheur en IA doit les connaître au moins à ce niveau élevé.

Notez que nous n'entrerons pas dans les détails des [techniques d'apprentissage non supervisé](https://www.freecodecamp.org/news/supervised-vs-unsupervised-learning/) ici, ou n'entrerons pas dans les détails granulaires de chaque algorithme.

### 2.1 Régression Linéaire

Lorsque la relation entre deux variables est linéaire, vous pouvez utiliser la méthode statistique de Régression Linéaire. Elle peut vous aider à modéliser l'impact d'un changement unitaire dans une variable, *la variable indépendante*, sur les valeurs d'une autre variable, *la variable dépendante*.

Les variables dépendantes sont souvent appelées variables de réponse ou variables expliquées, tandis que les variables indépendantes sont souvent appelées régresseurs ou variables explicatives.

Lorsque le modèle de Régression Linéaire est basé sur une seule variable indépendante, alors le modèle est appelé *Régression Linéaire Simple*. Mais lorsque le modèle est basé sur plusieurs variables indépendantes, il est appelé *Régression Linéaire Multiple*.

La Régression Linéaire Simple peut être décrite par l'expression suivante :

![Image](https://miro.medium.com/v2/resize:fit:1400/0*oLHnTG7OkSaBpmni.png align="left")

où **Y** est la variable dépendante, **X** est la variable indépendante qui fait partie des données, **β0** est l'interception qui est inconnue et constante, et **β1** est le coefficient de pente ou un paramètre correspondant à la variable X qui est également inconnu et constant. Enfin, **u** est le terme d'erreur que le modèle fait lors de l'estimation des valeurs de Y.

L'idée principale derrière la régression linéaire est de trouver la meilleure ligne droite, *la ligne de régression*, à travers un ensemble de données appariées (X, Y). Un exemple d'application de la Régression Linéaire est la modélisation de l'impact de la longueur des nageoires sur la masse corporelle des manchots, qui est visualisée ci-dessous :

![Image Source: The Author](https://www.freecodecamp.org/news/content/images/2023/10/image-83.png align="left")

*\[Source de l'Image : L'Auteur\] Ligne de régression montrant la meilleure ligne ajustée aux points de données réels dans les données.*

La Régression Linéaire Multiple avec trois variables indépendantes peut être décrite par l'expression suivante :

![Image](https://miro.medium.com/v2/resize:fit:1400/0*O6gSvCYw8FxXAW54.png align="left")

où **Y** est la variable dépendante, **X** est la variable indépendante qui fait partie des données, **β0** est l'interception qui est inconnue et constante, et **β1**, **β2**, **β3** sont les coefficients de pente ou un paramètre correspondant aux variables X1, X2, X3 qui sont également inconnus et constants. Enfin, **u** est le terme d'erreur que le modèle fait lors de l'estimation des valeurs de Y.

### 2.1.1 Moindres Carrés Ordinaires

Les moindres carrés ordinaires (OLS) sont une méthode pour estimer les paramètres inconnus tels que **β0** et **β1** dans un modèle de régression linéaire. Le modèle est basé sur le principe des *moindres carrés* qui minimise la somme des carrés des différences entre la variable dépendante observée et ses valeurs prédites par la fonction linéaire de la variable indépendante, souvent appelée *valeurs ajustées*.

Cette différence entre les valeurs réelles et prédites de la variable dépendante **Y** est appelée *résidu*. Ce que fait l'OLS, c'est minimiser la somme des résidus au carré. Ce problème d'optimisation aboutit aux estimations OLS suivantes pour les paramètres inconnus β0 et β1 qui sont également connus sous le nom d'*estimations de coefficients*.

![Image](https://miro.medium.com/v2/resize:fit:1400/0*jFQQnpCqqPeKOGeJ.png align="left")

Une fois ces paramètres du modèle de Régression Linéaire Simple estimés, les *valeurs ajustées* de la variable de réponse peuvent être calculées comme suit :

![Image](https://miro.medium.com/v2/resize:fit:1400/0*v66iFYRMqQOENjX0.png align="left")

#### Erreur Standard

Les *résidus* ou les termes d'erreur estimés peuvent être déterminés comme suit :

![Image](https://miro.medium.com/v2/resize:fit:1400/0*EqX54WI0SqwPlQ2S.png align="left")

Il est important de garder à l'esprit la différence entre les termes d'erreur et les résidus. Les termes d'erreur ne sont jamais observés, tandis que les résidus sont calculés à partir des données. L'OLS estime les termes d'erreur pour chaque observation mais pas le terme d'erreur réel. Ainsi, la vraie variance d'erreur est encore inconnue.

De plus, ces estimations sont sujettes à l'incertitude d'échantillonnage. Cela signifie que nous ne pourrons jamais déterminer l'estimation exacte, la vraie valeur, de ces paramètres à partir des données d'échantillon dans une application empirique. Mais nous pouvons l'estimer en calculant la variance résiduelle de l'échantillon.

### **2.1.2 Hypothèses OLS**

La méthode d'estimation OLS fait les hypothèses suivantes qui doivent être satisfaites pour obtenir des résultats de prédiction fiables :

* **Hypothèse (A1)** : l'hypothèse de **Linéarité** stipule que le modèle est linéaire en paramètres.

* **A2** : l'hypothèse d'**Échantillon Aléatoire** stipule que toutes les observations de l'échantillon sont sélectionnées de manière aléatoire.

* **A3** : l'hypothèse d'**Exogénéité** stipule que les variables indépendantes ne sont pas corrélées avec les termes d'erreur.

* **A4** : l'hypothèse d'**Homoscedasticité** stipule que la variance de tous les termes d'erreur est constante.

* **A5** : l'hypothèse de **Pas de Multicolinéarité Parfaite** stipule qu'aucune des variables indépendantes n'est constante et qu'il n'y a pas de relations linéaires exactes entre les variables indépendantes.

Notez que la description ci-dessus pour la Régression Linéaire provient de mon article intitulé [Guide Complet de la Régression Linéaire](https://pub.towardsai.net/complete-guide-to-linear-regression-86c5eddb7eda).

Pour un article détaillé sur la Régression Linéaire, consultez ce post :

%[https://pub.towardsai.net/complete-guide-to-linear-regression-86c5eddb7eda] 

### 2.1.3 Régression Linéaire en Python

Imaginez que vous avez un ami, Alex, qui collectionne des timbres. Chaque mois, Alex achète un certain nombre de timbres, et vous remarquez que le montant que Alex dépense semble dépendre du nombre de timbres achetés.

Maintenant, vous voulez créer un petit outil qui peut prédire combien Alex dépensera le mois prochain en fonction du nombre de timbres achetés. C'est là que la Régression Linéaire entre en jeu.

En termes techniques, nous essayons de prédire la variable dépendante (montant dépensé) en fonction de la variable indépendante (nombre de timbres achetés).

Voici un exemple simple de code Python utilisant `scikit-learn` pour effectuer une Régression Linéaire sur un ensemble de données créé.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Données d'exemple
timbres_achetes = np.array([1, 3, 5, 7, 9]).reshape((-1, 1))  # Remodelage pour en faire un tableau 2D
montant_depense = np.array([2, 6, 8, 12, 18])

# Création d'un Modèle de Régression Linéaire
modele = LinearRegression()

# Entraînement du Modèle
modele.fit(timbres_achetes, montant_depense)

# Prédictions
prochain_mois_timbres = 10
depense_predite = modele.predict([[prochain_mois_timbres]])

# Tracé
plt.scatter(timbres_achetes, montant_depense, color='blue')
plt.plot(timbres_achetes, modele.predict(timbres_achetes), color='red')
plt.title('Timbres Achetés vs Montant Dépensé')
plt.xlabel('Timbres Achetés')
plt.ylabel('Montant Dépensé ($)')
plt.grid(True)
plt.show()

# Affichage de la Prédiction
print(f"Si Alex achète {prochain_mois_timbres} timbres le mois prochain, il dépensera probablement ${depense_predite[0]:.2f}.")
```

* **Données d'exemple** : `timbres_achetes` représente le nombre de timbres que Alex a achetés chaque mois et `montant_depense` représente l'argent correspondant dépensé.

* **Création et Entraînement du Modèle** : Utilisation de `LinearRegression()` de `scikit-learn` pour créer et entraîner notre modèle en utilisant `.fit()`.

* **Prédictions** : Utilisation du modèle entraîné pour prédire le montant que Alex dépensera pour un nombre donné de timbres. Dans le code, nous prédisons le montant pour 10 timbres.

* **Tracé** : Nous traçons les points de données originaux (en bleu) et la ligne prédite (en rouge) pour comprendre visuellement la capacité de prédiction de notre modèle.

* **Affichage de la Prédiction** : Enfin, nous imprimons la dépense prédite pour un nombre spécifique de timbres (10 dans ce cas).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/LinearRegression.png align="left")

*\[Source de l'Image : L'Auteur\] Visualisation de la Ligne de Régression, meilleure ligne ajustée par le modèle LR par rapport aux points de données réels, pour voir à quel point le modèle a pu ajuster les données.*

### 2.2 Régression Logistique

Une autre technique très populaire de Machine Learning est la Régression Logistique, qui, bien que nommée régression, est en réalité une technique de classification supervisée.

La régression logistique est une méthode de Machine Learning qui modélise la probabilité conditionnelle qu'un événement se produise ou qu'une observation appartienne à une certaine classe, sur la base d'un ensemble de données donné de variables indépendantes.

Lorsque la relation entre deux variables est linéaire et que la variable dépendante est une variable catégorielle, vous pouvez vouloir prédire une variable sous la forme d'une probabilité (nombre entre 0 et 1). Dans ces cas, la Régression Logistique est utile.

C'est parce que pendant le processus de prédiction en Régression Logistique, le classificateur prédit la probabilité (une valeur entre 0 et 1) de chaque observation appartenant à une certaine classe, généralement à l'une des deux classes de la variable dépendante.

Par exemple, si vous voulez prédire la probabilité ou la probabilité qu'un candidat soit élu ou non lors d'une élection donnée la popularité du candidat, les succès passés et d'autres variables descriptives sur ce candidat, vous pouvez utiliser la Régression Logistique pour modéliser cette probabilité.

Ainsi, plutôt que de prédire la variable de réponse, la Régression Logistique modélise la probabilité que Y appartienne à une catégorie particulière.

C'est similaire à la Régression Linéaire avec une différence étant qu'au lieu de Y, elle prédit les log odds. En termes statistiques, nous modélisons la distribution conditionnelle de la réponse **Y**, étant donné le(s) prédicteur(s) **X**. Ainsi, la LR aide à prédire la probabilité que Y appartienne à une certaine classe (0 et 1) étant donné les caractéristiques **P(Y|X=x)**.

Le nom Logistique dans la Régression Logistique vient de la fonction sur laquelle cette approche est basée, qui est la **Fonction Logistique**. La Fonction Logistique garantit que pour des valeurs trop grandes et trop petites, la probabilité correspondante est toujours dans les limites [0,1].

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-46.png align="left")

*probabilité qu'une observation appartienne à une certaine classe en fonction de sa valeur de caractéristique X*

Dans l'équation ci-dessus, **P(X)** représente la probabilité que Y appartienne à une certaine classe (0 et 1) étant donné les caractéristiques P(Y|X=x). **X** représente la variable indépendante, **β0** est l'interception qui est inconnue et constante, **β1** est le coefficient de pente ou un paramètre correspondant à la variable X qui est également inconnu et constant, similaire à la Régression Linéaire. ***e*** représente la fonction exp().

#### Odds et Log Odds

La Régression Logistique et sa technique d'estimation MLE sont basées sur les termes Odds et Log Odds. Où **Odds** est défini comme suit :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*s5_x03xuUHM_n3SAMujx7w.png align="left")

*rapport de cotes*

et **Log Odds** est défini comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-14-at-5.39.11-AM.png align="left")

*log rapport de cotes*

#### 2.2.1 Estimation par Maximum de Vraisemblance (MLE)

Alors que pour la Régression Linéaire, nous utilisons OLS (Moindres Carrés Ordinaires) ou LS (Moindres Carrés) comme technique d'estimation, pour la Régression Logistique, nous devons utiliser une autre technique d'estimation.

Nous ne pouvons pas utiliser LS dans la Régression Logistique pour trouver la meilleure ligne d'ajustement (pour effectuer l'estimation) car les erreurs peuvent alors devenir très grandes ou très petites (même négatives) alors que dans le cas de la Régression Logistique, nous visons une valeur prédite dans [0,1].

Ainsi, pour la Régression Logistique, nous utilisons la technique MLE, où la fonction de vraisemblance calcule la probabilité d'observer le résultat étant donné les données d'entrée et le modèle. Cette fonction est ensuite optimisée pour trouver l'ensemble de paramètres qui résulte en la somme de vraisemblance la plus grande sur l'ensemble de données d'entraînement.

![Image](https://miro.medium.com/v2/resize:fit:1400/1*u7XLRKF3BVsvyF5zXLxEsg.png align="left")

*Source de l'Image : L'Auteur*

La fonction logistique produira toujours une courbe en forme de S comme ci-dessus, quelle que soit la valeur de la variable indépendante X, ce qui entraîne une estimation sensée la plupart du temps.

#### 2.2.2 Fonction(s) de Vraisemblance de la Régression Logistique

La fonction de vraisemblance peut être exprimée comme suit :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*BR90pVIpXkTobihxToP8bg.png align="left")

Ainsi, la **fonction de log-vraisemblance** peut être exprimée comme suit :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*573K4SJ2pDY5bmKndL8e_A.png align="left")

ou, après transformation des multiplicateurs en sommation, nous obtenons :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*nabbNqzEzMBR-2cIdfnRtA.png align="left")

Ensuite, l'idée derrière le MLE est de trouver un ensemble d'estimations qui maximiserait cette fonction de vraisemblance.

* **Étape 1** : Projeter les points de données dans une ligne candidate qui produit une valeur de log (odds) d'échantillon.

* **Étape 2** : Transformer le log (odds) de l'échantillon en probabilités de l'échantillon en utilisant la formule suivante :

![Image](https://miro.medium.com/v2/resize:fit:1320/1*Tab5F2hMLHo9AMhEbjJQoQ.png align="left")

* **Étape 3** : Obtenir la vraisemblance globale ou le log de la vraisemblance globale.

* **Étape 4** : Faire tourner la ligne de log (odds) encore et encore, jusqu'à trouver le log (odds) optimal maximisant la vraisemblance globale

#### 2.2.3 Valeur de coupure dans la Régression Logistique

Si vous prévoyez d'utiliser la Régression Logistique à la fin pour obtenir une valeur binaire {0,1}, alors vous avez besoin d'un point de coupure pour transformer les valeurs estimées par observation de la plage [0,1] à une valeur 0 ou 1.

Selon votre cas individuel, vous pouvez choisir un point de coupure correspondant, mais un point de coupure populaire est 0,5. Dans ce cas, toutes les observations avec une valeur prédite inférieure à 0,5 seront assignées à la classe 0 et les observations avec une valeur prédite supérieure ou égale à 0,5 seront assignées à la classe 1.

#### 2.2.4 Métriques de Performance dans la Régression Logistique

Puisque la Régression Logistique est une méthode de classification, des métriques de classification courantes telles que le rappel, la précision, la mesure F-1 peuvent toutes être utilisées. Mais il existe également un système de métriques qui est également couramment utilisé pour évaluer la performance du modèle de Régression Logistique, appelé [**Déviance**](https://en.wikipedia.org/wiki/Deviance_(statistics)).

#### 2.2.5 Régression Logistique en Python

Jenny est une lectrice avide de livres. Jenny lit des livres de différents genres et tient un petit journal où elle note le nombre de pages et si elle a aimé le livre (Oui ou Non).

Nous voyons un schéma : Jenny apprécie généralement les livres qui ne sont ni trop courts ni trop longs. Maintenant, pouvons-nous prédire si Jenny aimera un livre en fonction de son nombre de pages ? C'est là que la Régression Logistique peut nous aider !

En termes techniques, nous essayons de prédire un résultat binaire (aimer/ne pas aimer) en fonction d'une variable indépendante (nombre de pages).

Voici un exemple simplifié en Python utilisant `scikit-learn` pour implémenter la Régression Logistique :

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Données d'exemple
pages = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500]).reshape(-1, 1)
aimes = np.array([0, 1, 1, 1, 0, 0, 0, 0, 0])  # 1 : Aime, 0 : N'aime pas

# Création d'un Modèle de Régression Logistique
modele = LogisticRegression()

# Entraînement du Modèle
modele.fit(pages, aimes)

# Prédictions
predire_pages_livre = 260
prediction_aime = modele.predict([[predire_pages_livre]])

# Tracé
plt.scatter(pages, aimes, color='forestgreen')
plt.plot(pages, modele.predict_proba(pages)[:, 1], color='darkred')
plt.title('Pages du Livre vs Aime/N'aime pas')
plt.xlabel('Nombre de Pages')
plt.ylabel('Probabilité d\'Aimer')
plt.axvline(x=predire_pages_livre, color='green', linestyle='--')
plt.axhline(y=0.5, color='grey', linestyle='--')
plt.show()

# Affichage de la Prédiction
print(f"Jenny va {'aimer' if prediction_aime[0] == 1 else 'ne pas aimer'} un livre de {predire_pages_livre} pages.")
```

* **Données d'exemple** : `pages` représente le nombre de pages dans les livres que Jenny a lus, et `aimes` représente si elle les a aimés (1 pour aimer, 0 pour ne pas aimer).

* **Création et Entraînement du Modèle** : Nous instancions `LogisticRegression()` et entraînons le modèle en utilisant `.fit()` avec nos données.

* **Prédictions** : Nous prédisons si Jenny aimera un livre avec un nombre particulier de pages (260 dans cet exemple).

* **Tracé** : Nous visualisons les points de données originaux (en bleu) et la courbe de probabilité prédite (en rouge). La ligne pointillée verte représente le nombre de pages que nous prédisons, et la ligne pointillée grise indique le seuil (0,5) au-dessus duquel nous prédisons un "aime".

* **Affichage de la Prédiction** : Nous affichons si Jenny aimera un livre du nombre de pages donné selon la prédiction de notre modèle.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-8.44.09-PM.png align="left")

*\[Source de l'Image : L'Auteur\] Visualisation du modèle de classification de la régression logistique, vous pouvez voir la probabilité d'aimer un nombre donné de pages du livre, ici le point de coupure est 0,5*

### 2.3 Analyse Discriminante Linéaire (LDA)

Une autre technique de classification, étroitement liée à la Régression Logistique, est l'Analyse Discriminante Linéaire (LDA). Alors que la Régression Logistique est généralement utilisée pour modéliser la probabilité qu'une observation appartienne à une classe de la variable de résultat avec 2 catégories, la LDA est généralement utilisée pour modéliser la probabilité qu'une observation appartienne à une classe de la variable de résultat avec 3 catégories et plus.

La LDA offre une approche alternative pour modéliser la probabilité conditionnelle de la variable de résultat étant donné cet ensemble de prédicteurs qui aborde les problèmes de la Régression Logistique. Elle modélise la distribution des prédicteurs X séparément dans chacune des classes de réponse (c'est-à-dire, étant donné Y), puis utilise le **théorème de Bayes** pour inverser ces deux éléments en estimations pour Pr(Y = k|X = x).

Notez que dans le cas de la LDA, ces distributions sont supposées être normales. Il s'avère que le modèle est très similaire en forme à la régression logistique. Dans l'équation ici :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*jMSHLN0-cAG3zKGCxXWY7w.png align="left")

π_k représente la probabilité a priori globale qu'une observation choisie aléatoirement provienne de la k-ième classe. f_k(x), qui est égal à Pr(X = x|Y = k), représente la probabilité a posteriori, et est la fonction de densité de X pour une observation qui provient de la k-ième classe (fonction de densité des prédicteurs).

C'est la probabilité que X=x étant donné que l'observation provient d'une certaine classe. En d'autres termes, c'est la probabilité que l'observation appartienne à la k-ième classe, étant donné la valeur du prédicteur pour cette observation.

En supposant que f_k(x) est Normal ou Gaussien, la densité normale prend la forme suivante (c'est le paramètre normal unidimensionnel) :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*0dOVbhy_xPi9rIa7Z7j2Fg.png align="left")

![Image](https://miro.medium.com/v2/resize:fit:1400/1*yM_kH6TL6EUvMZiTJvCwKQ.png align="left")

où μ_k et σ_k² sont les paramètres de moyenne et de variance pour la k-ième classe. En supposant que σ_1² = · · · = σ_K² (il y a un terme de variance partagé à travers toutes les K classes, que nous notons par σ²).

Ensuite, la LDA approxime le classificateur de Bayes en utilisant les estimations suivantes pour πk, βk, et σ² :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*EloSKpmgw0Jhz-ubEGaogg.png align="left")

Alors que la Régression Logistique est généralement utilisée pour modéliser la probabilité qu'une observation appartienne à une classe de la variable de résultat avec 2 catégories, la LDA est généralement utilisée pour modéliser la probabilité qu'une observation appartienne à une classe de la variable de résultat avec 3 catégories et plus.

#### 2.3.1 Analyse Discriminante Linéaire en Python

Imaginez Sarah, qui aime cuisiner et essayer divers fruits. Elle voit que les fruits qu'elle aime sont généralement de tailles et de niveaux de douceur spécifiques.

Maintenant, Sarah est curieuse : peut-elle prédire si elle aimera un fruit en fonction de sa taille et de sa douceur ? Utilisons l'Analyse Discriminante Linéaire (LDA) pour l'aider à prédire si elle aimera certains fruits ou non.

En termes techniques, nous essayons de classer les fruits (aimer/ne pas aimer) en fonction de deux variables prédictives (taille et douceur).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Données d'exemple
# [taille, douceur]
caracteristiques_fruits = np.array([[3, 7], [2, 8], [3, 6], [4, 7], [1, 4], [2, 3], [3, 2], [4, 3]])
aimes_fruits = np.array([1, 1, 1, 1, 0, 0, 0, 0])  # 1 : Aime, 0 : N'aime pas

# Création d'un Modèle LDA
modele = LinearDiscriminantAnalysis()

# Entraînement du Modèle
modele.fit(caracteristiques_fruits, aimes_fruits)

# Prédiction
nouveau_fruit = np.array([[2.5, 6]])  # [taille, douceur]
prediction_aime = modele.predict(nouveau_fruit)

# Tracé
plt.scatter(caracteristiques_fruits[:, 0], caracteristiques_fruits[:, 1], c=aimes_fruits, cmap='viridis', marker='o')
plt.scatter(nouveau_fruit[:, 0], nouveau_fruit[:, 1], color='darkred', marker='x')
plt.title('Appréciation des Fruits Basée sur la Taille et la Douceur')
plt.xlabel('Taille')
plt.ylabel('Douceur')
plt.show()

# Affichage de la Prédiction
print(f"Sarah va {'aimer' if prediction_aime[0] == 1 else 'ne pas aimer'} un fruit de taille {nouveau_fruit[0, 0]} et de douceur {nouveau_fruit[0, 1]}.")
```

* **Données d'exemple** : `caracteristiques_fruits` contient deux caractéristiques - la taille et la douceur des fruits, et `aimes_fruits` représente si Sarah les aime (1 pour aimer, 0 pour ne pas aimer).

* **Création et Entraînement du Modèle** : Nous instancions `LinearDiscriminantAnalysis()` et l'entraîons en utilisant `.fit()` avec nos données d'exemple.

* **Prédiction** : Nous prédisons si Sarah aimera un fruit avec une taille et un niveau de douceur particuliers ([2.5, 6] dans cet exemple).

* **Tracé** : Nous visualisons les points de données originaux, codés par couleur en fonction des préférences de Sarah (jaune pour aimer et violet pour ne pas aimer), et marquons le nouveau fruit avec un 'x' rouge.

* **Affichage de la Prédiction** : Nous affichons si Sarah aimera un fruit avec la taille et le niveau de douceur donnés selon la prédiction de notre modèle.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-8.48.44-PM.png align="left")

*\[Source de l'Image : L'Auteur\] Graphique montrant les résultats de classification des fruits, si Sarah aime ou n'aime pas le fruit en fonction de la taille et du niveau de douceur des fruits*

### 2.4 Régression Logistique vs LDA

La régression logistique est une approche populaire pour effectuer une classification lorsqu'il y a deux classes. Mais lorsque les classes sont bien séparées ou que le nombre de classes dépasse 2, les estimations des paramètres pour le modèle de régression logistique sont surprenamment instables.

Contrairement à la Régression Logistique, la LDA ne souffre pas de ce problème d'instabilité lorsque le nombre de classes est supérieur à 2. Si n est petit et que la distribution des prédicteurs X est approximativement normale dans chacune des classes, la LDA est à nouveau plus stable que le modèle de Régression Logistique.

### 2.5 Naïve Bayes

Une autre méthode de classification qui repose sur la Règle de Bayes comme la LDA est l'approche de Classification Naïve Bayes. Pour en savoir plus sur le Théorème de Bayes, la Règle de Bayes et un exemple correspondant, vous pouvez lire [ces](https://www.freecodecamp.org/news/bayes-rule-explained/) [articles](https://towardsdatascience.com/fundamentals-of-statistics-for-data-scientists-and-data-analysts-69d93a05aae7).

Comme la Régression Logistique, vous pouvez utiliser l'approche Naïve Bayes pour classer une observation dans l'une des deux classes (0 ou 1).

L'idée derrière cette méthode est de calculer la probabilité qu'une observation appartienne à une classe étant donnée la probabilité a priori pour cette classe et la probabilité conditionnelle de chaque valeur de caractéristique donnée pour une classe donnée. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-49.png align="left")

où Y représente la classe de l'observation, k est la k-ième classe et x1, ..., xn représentent les caractéristiques 1 à n, respectivement. f_k(x) = Pr(X = x|Y = k), représente la probabilité a posteriori, qui, comme dans le cas de la LDA, est la fonction de densité de X pour une observation qui provient de la k-ième classe (fonction de densité des prédicteurs).

Si vous comparez l'expression ci-dessus avec celle que vous avez vue pour la LDA, vous verrez quelques similitudes.

Dans la LDA, nous faisons une hypothèse très importante et forte à des fins de simplification : à savoir, que f_k est la fonction de densité pour une variable aléatoire normale multivariée avec une moyenne spécifique à la classe μ_k, et une matrice de covariance partagée Σ.

Cette hypothèse aide à remplacer le problème très difficile d'estimer K fonctions de densité p-dimensionnelles par le problème beaucoup plus simple, qui est d'estimer K vecteurs de moyenne p-dimensionnels et une matrice de covariance (p × p)-dimensionnelle.

Dans le cas du Classificateur Naïve Bayes, il utilise une approche différente pour estimer f_1(x), ..., f_K(x). Au lieu de faire une hypothèse que ces fonctions appartiennent à une famille particulière de distributions (par exemple normale ou normale multivariée), nous faisons plutôt une seule hypothèse : au sein de la k-ième classe, les p prédicteurs sont indépendants. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-51.png align="left")

Ainsi, le classificateur de Bayes suppose que la valeur d'une variable ou caractéristique particulière est indépendante de la valeur de toute autre variable (non corrélée), étant donné la variable de classe/étiquette.

Par exemple, un fruit peut être considéré comme une banane s'il est jaune, de forme ovale et d'environ 5 à 10 cm de long. Ainsi, le classificateur Naïve Bayes considère que chacune de ces différentes caractéristiques du fruit contribue indépendamment à la probabilité que ce fruit soit une banane, indépendamment de toute corrélation possible entre les caractéristiques de couleur, de forme et de longueur.

#### Estimation Naïve Bayes

Comme la Régression Logistique, dans le cas de l'approche de classification Naïve Bayes, nous utilisons l'Estimation par Maximum de Vraisemblance (MLE) comme technique d'estimation. Il existe un excellent article fournissant un résumé détaillé et concis de cette approche avec un exemple correspondant que vous pouvez trouver [ici](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c).

### 2.5.1 Naïve Bayes en Python

Tom est un passionné de cinéma qui regarde des films de différents genres et enregistre ses commentaires—s'il les a aimés ou non. Il a remarqué que le fait qu'il aime un film peut dépendre de deux aspects : la durée du film et son genre. Pouvez-vous prédire si Tom aimera un film en fonction de ces deux caractéristiques en utilisant Naïve Bayes ?

Techniquement, nous voulons prédire un résultat binaire (aimer/ne pas aimer) en fonction des variables indépendantes (durée du film et genre).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# Données d'exemple
# [durée_film, code_genre] (en supposant que le genre est codé comme : 0 pour Action, 1 pour Romance, etc.)
caracteristiques_films = np.array([[120, 0], [150, 1], [90, 0], [140, 1], [100, 0], [80, 1], [110, 0], [130, 1]])
aimes_films = np.array([1, 1, 0, 1, 0, 1, 0, 1])  # 1 : Aime, 0 : N'aime pas

# Création d'un Modèle Naïve Bayes
modele = GaussianNB()

# Entraînement du Modèle
modele.fit(caracteristiques_films, aimes_films)

# Prédiction
nouveau_film = np.array([[100, 1]])  # [durée_film, code_genre]
prediction_aime = modele.predict(nouveau_film)

# Tracé
plt.scatter(caracteristiques_films[:, 0], caracteristiques_films[:, 1], c=aimes_films, cmap='viridis', marker='o')
plt.scatter(nouveau_film[:, 0], nouveau_film[:, 1], color='darkred', marker='x')
plt.title('Appréciation des Films Basée sur la Durée et le Genre')
plt.xlabel('Durée du Film (min)')
plt.ylabel('Code de Genre')
plt.show()

# Affichage de la Prédiction
print(f"Tom va {'aimer' if prediction_aime[0] == 1 else 'ne pas aimer'} un film de {nouveau_film[0, 0]} minutes de genre code {nouveau_film[0, 1]}.")
```

* **Données d'exemple** : `caracteristiques_films` contient deux caractéristiques : la durée du film et le genre (encodé en nombres), tandis que `aimes_films` indique si Tom les aime (1 pour aimer, 0 pour ne pas aimer).

* **Création et Entraînement du Modèle** : Nous instancions `GaussianNB()` (un classificateur Naïve Bayes supposant une distribution gaussienne des données) et l'entraîons avec `.fit()` en utilisant nos données.

* **Prédiction** : Nous prédisons si Tom aimera un nouveau film, étant donné sa durée et son code de genre ([100, 1] dans ce cas).

* **Tracé** : Nous visualisons les points de données originaux, codés par couleur en fonction des préférences de Tom (jaune pour aimer et violet pour ne pas aimer). Le 'x' rouge représente le nouveau film.

* **Affichage de la Prédiction** : Nous imprimons si Tom aimera un film de la durée et du code de genre donnés, selon la prédiction de notre modèle.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-8.51.54-PM.png align="left")

*\[Source de l'Image : L'Auteur\] Appréciation des films basée sur la durée et le genre en utilisant le Naïve Bayes Gaussien*

### 2.6 Naïve Bayes vs Régression Logistique

Le Classificateur Naïve Bayes s'est avéré plus rapide et présente un biais plus élevé et une variance plus faible. La régression logistique a un faible biais et une variance plus élevée. Selon votre cas individuel et le compromis biais-variance, vous pouvez choisir l'approche correspondante.

### 2.7 Arbres de Décision

Les Arbres de Décision sont une méthode d'apprentissage supervisée et non paramétrique en Machine Learning utilisée à la fois pour la classification et la régression. L'idée est de créer un modèle qui prédit la valeur d'une variable cible en apprenant des règles de décision simples à partir des prédicteurs de données.

Contrairement à la Régression Linéaire ou à la Régression Logistique, les Arbres de Décision sont des alternatives de modèles simples et utiles lorsque la relation entre les variables indépendantes et la variable dépendante est suspectée d'être non linéaire.

Les méthodes basées sur les arbres stratifient ou segmentent l'espace des prédicteurs en régions plus petites. L'idée derrière la construction des Arbres de Décision est de diviser l'espace des prédicteurs en régions distinctes et mutuellement exclusives X1, X2, ..., Xp → R_1, R_2, ..., R_N où les régions sont sous forme de boîtes ou de rectangles. Ces régions sont trouvées par division binaire récursive puisque la minimisation de la RSS n'est pas réalisable. Cette approche est souvent appelée approche gloutonne.

Les arbres de décision sont construits par division de haut en bas. Ainsi, au début, toutes les observations appartiennent à une seule région. Ensuite, le modèle divise successivement l'espace des prédicteurs. Chaque division est indiquée via deux nouvelles branches plus bas sur l'arbre.

Cette approche est parfois appelée *gloutonne* car à chaque étape du processus de construction de l'arbre, la meilleure division est faite à cette étape particulière, plutôt que de regarder vers l'avant et de choisir une division qui conduira à un meilleur arbre dans une étape future.

#### Critères d'arrêt

Il existe certains critères d'arrêt couramment utilisés lors de la construction d'Arbres de Décision :

* Nombre minimum d'observations dans la feuille.

* Nombre minimum d'échantillons pour une division de nœud.

* Profondeur maximale de l'arbre (profondeur verticale).

* Nombre maximal de nœuds terminaux.

* Nombre maximal de caractéristiques à considérer pour la division.

Par exemple, répétez ce processus de division jusqu'à ce qu'aucune région ne contienne plus de 100 observations. Approfondissons

*1. Nombre minimum d'observations dans la feuille :

Si une division proposée aboutit à un nœud feuille avec moins d'un nombre défini d'observations, cette division peut être rejetée. Cela empêche l'arbre de devenir trop complexe.

*2. Nombre minimum d'échantillons pour une division de nœud :

Pour procéder à une division de nœud, le nœud doit avoir au moins autant d'échantillons. Cela garantit qu'il y a une quantité significative de données pour justifier la division.

*3. Profondeur maximale de l'arbre (profondeur verticale) :

Cela limite le nombre de fois où un arbre peut se diviser. C'est comme dire à l'arbre combien de questions il peut poser sur les données avant de prendre une décision.

*4. Nombre maximal de nœuds terminaux :

C'est le nombre total de nœuds finaux (ou feuilles) que l'arbre peut avoir.

*5. Nombre maximal de caractéristiques à considérer pour la division :

Pour chaque division, l'algorithme ne considère qu'un sous-ensemble de caractéristiques. Cela peut accélérer l'entraînement et aider à la généralisation.

Lors de la construction d'un arbre de décision, surtout lorsqu'on traite avec un grand nombre de caractéristiques, l'arbre peut devenir trop grand avec trop de feuilles. Cela affectera l'**interprétabilité** du modèle et pourrait potentiellement entraîner un problème de surapprentissage. Par conséquent, choisir un bon critère d'arrêt est essentiel pour l'interprétabilité et pour la performance du modèle.

#### RSS/Indice de Gini/Entropie/Pureté des Nœuds

Lors de la construction de l'arbre, nous utilisons le RSS (pour les Arbres de Régression) et l'Indice de Gini/Entropie (pour les Arbres de Classification) pour choisir le prédicteur et la valeur pour diviser les régions. L'Indice de Gini et l'Entropie sont souvent appelés mesures de Pureté des Nœuds car ils décrivent la pureté des feuilles des arbres.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-53.png align="left")

#### Indice de Gini

L'indice de Gini mesure la variance totale à travers K classes. Il prend une petite valeur lorsque tous les taux d'erreur de classe sont soit 1 soit 0. C'est aussi pourquoi il est appelé une mesure de pureté des nœuds - l'indice de Gini prend de petites valeurs lorsque les nœuds de l'arbre contiennent principalement des observations de la même classe.

L'indice de Gini est défini comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-54.png align="left")

où p̂mk représente la proportion d'observations d'entraînement dans la m-ième région qui proviennent de la k-ième classe.

#### Entropie

L'entropie est une autre mesure de pureté des nœuds, et comme l'indice de Gini, l'entropie prendra une petite valeur si le m-ième nœud est pur. En fait, l'indice de Gini et l'entropie sont assez similaires numériquement et peuvent être exprimés comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-55.png align="left")

#### Exemple de Classification par Arbre de Décision

Examinons un exemple où nous avons trois caractéristiques décrivant le comportement passé des consommateurs :

* **Récence** (À quand remonte le dernier achat du client ?)

* **Monétaire** (Combien d'argent le client a-t-il dépensé sur une période donnée ?)

* **Fréquence** (À quelle fréquence ce client a-t-il fait un achat sur une période donnée ?)

Nous utiliserons la version de classification de l'Arbre de Décision pour classer les clients dans l'une des 3 classes (Bon : 1, Meilleur : 2 et Meilleur : 3), étant donné les caractéristiques décrivant le comportement du client.

Dans l'arbre suivant, où nous utilisons l'Indice de Gini comme mesure de pureté, nous voyons que la première caractéristique qui semble être la plus importante est la Récence. Regardons l'arbre puis interprétons-le :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-56.png align="left")

*\[Source de l'Image : L'Auteur\] Arbre de décision*

Les clients qui ont une récence de 202 ou plus (la dernière fois qu'ils ont fait un achat il y a plus de 202 jours) ont alors 93 % de chances que cette observation soit assignée à la classe 1 (basiquement, nous pouvons étiqueter ces clients comme des clients de la Classe Bon).

Pour les clients avec une Récence inférieure à 202 (ils ont fait un achat récemment), nous regardons leur valeur Monétaire et si elle est inférieure à 1394, alors nous regardons leur Fréquence. Si la Fréquence est alors inférieure à 44, nous pouvons alors étiqueter la classe de ces clients comme Meilleure ou (classe 2). Et ainsi de suite.

#### Implémentation Python des Arbres de Décision

Alex est intrigué par la relation entre le nombre d'heures étudiées et les scores obtenus par les étudiants. Alex a collecté des données auprès de ses pairs sur leurs heures d'étude et leurs scores de test respectifs.

Il se demande : pouvons-nous prédire le score d'un étudiant en fonction du nombre d'heures qu'il étudie ? Utilisons la Régression par Arbre de Décision pour le découvrir.

Techniquement, nous prédisons un résultat continu (score de test) en fonction d'une variable indépendante (heures d'étude).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree

# Données d'exemple
# [heures_etudiees]
heures_etude = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
scores_test = np.array([50, 55, 70, 80, 85, 90, 92, 98])

# Création d'un Modèle de Régression par Arbre de Décision
modele = DecisionTreeRegressor(max_depth=3)

# Entraînement du Modèle
modele.fit(heures_etude, scores_test)

# Prédiction
nouvelle_heure_etude = np.array([[5.5]])  # exemple d'heures étudiées
score_predit = modele.predict(nouvelle_heure_etude)

# Tracé de l'Arbre de Décision
plt.figure(figsize=(12, 8))
plot_tree(modele, filled=True, rounded=True, feature_names=["Heures d'Étude"])
plt.title('Arbre de Régression par Arbre de Décision')
plt.show()

# Tracé des Heures d'Étude vs. Scores de Test
plt.scatter(heures_etude, scores_test, color='darkred')
plt.plot(np.sort(heures_etude, axis=0), modele.predict(np.sort(heures_etude, axis=0)), color='orange')
plt.scatter(nouvelle_heure_etude, score_predit, color='green')
plt.title('Heures d\'Étude vs Scores de Test')
plt.xlabel('Heures d\'Étude')
plt.ylabel('Scores de Test')
plt.grid(True)
plt.show()

# Affichage de la Prédiction
print(f"Score de test prédit pour {nouvelle_heure_etude[0, 0]} heures d'étude : {score_predit[0]:.2f}.")
```

* **Données d'exemple** : `heures_etude` contient les heures étudiées, et `scores_test` contient les scores de test correspondants.

* **Création et Entraînement du Modèle** : Nous créons un `DecisionTreeRegressor` avec une profondeur maximale spécifiée (pour éviter le surapprentissage) et l'entraîons avec `.fit()` en utilisant nos données.

* **Tracé de l'Arbre de Décision** : `plot_tree` aide à visualiser le processus de décision du modèle, représentant les divisions basées sur les heures d'étude.

* **Prédiction & Tracé** : Nous prédisons le score de test pour une nouvelle valeur d'heure d'étude (5,5 dans cet exemple), visualisons les points de données originaux, les scores prédits par l'arbre de décision et la nouvelle prédiction.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-8.54.27-PM.png align="left")

*\[Source de l'Image : L'Auteur\] Visualisation du régressor d'arbre de décision*

La visualisation représente un modèle d'arbre de décision entraîné sur des données d'heures d'étude. Chaque nœud représente une décision basée sur les heures d'étude, se ramifiant à partir de la racine supérieure en fonction de conditions qui prévoient le mieux les scores de test. Le processus se poursuit jusqu'à atteindre une profondeur maximale ou jusqu'à ce qu'il n'y ait plus de divisions significatives. Les nœuds feuilles en bas donnent les prédictions finales, qui pour les arbres de régression, sont la moyenne des valeurs cibles pour les instances d'entraînement atteignant cette feuille. Cette visualisation met en évidence l'approche prédictive du modèle et l'influence significative des heures d'étude sur les scores de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-8.54.43-PM.png align="left")

*\[Source de l'Image : L'Auteur\] Heures d'étude vs scores de test tracés en utilisant le régressor d'arbre de décision*

Le graphique "Heures d'Étude vs. Scores de Test" illustre la corrélation entre les heures d'étude et les scores de test correspondants. Les points de données réels sont représentés par des points rouges, tandis que les prédictions du modèle sont montrées comme une fonction en escalier orange, caractéristique des arbres de régression. Un marqueur "x" vert met en évidence une prédiction pour un nouveau point de données, représentant ici une durée d'étude de 5,5 heures. Les éléments de conception du graphique, tels que les lignes de grille, les étiquettes et les légendes, améliorent la compréhension des valeurs réelles par rapport aux valeurs anticipées.

### 2.8 Bagging

L'un des plus grands inconvénients des Arbres de Décision est leur variance élevée. Vous pourriez vous retrouver avec un modèle et des prédictions faciles à expliquer mais trompeuses. Cela entraînerait des conclusions et des décisions commerciales incorrectes.

Ainsi, pour réduire la variance des Arbres de Décision, vous pouvez utiliser une méthode appelée Bagging. Pour comprendre ce qu'est le Bagging, il y a deux termes que vous devez connaître :

* **Bootstrapping**

* **Théorème Central Limite (CLT)**

Vous pouvez en savoir plus sur le Bootstrapping, qui est une technique de rééchantillonnage, plus tard dans ce manuel. Pour l'instant, vous pouvez considérer le Bootstrapping comme une technique qui effectue un échantillonnage à partir des données originales avec remplacement, ce qui crée une copie des données très similaire mais pas exactement identique aux données originales.

Le Bagging est également basé sur les mêmes idées que le CLT, qui est l'un des théorèmes les plus importants, sinon le plus important, en Statistiques. Vous pouvez lire plus en détail sur le CLT [ici](http://Supposons que X1, X2, ..., Xn sont toutes des variables aléatoires indépendantes avec la même distribution sous-jacente, également appelées indépendantes et identiquement distribuées ou i.i.d, où toutes les X ont la même moyenne μ et le même écart-type σ. À mesure que la taille de l'échantillon augmente, la distribution de probabilité de X converge en distribution vers une distribution normale avec une moyenne μ et une variance σ au carré. Le Théorème Central Limite peut être résumé comme suit :).

Mais l'idée qui est également utilisée dans le Bagging est que si vous prenez la moyenne de nombreux échantillons, alors la variance est considérablement réduite par rapport à la variance de chacun des modèles basés sur des échantillons individuels.

Ainsi, étant donné un ensemble de n observations indépendantes Z1,...,Zn, chacune avec une variance σ2, la variance de la moyenne Z̄ des observations est donnée par σ2/n. Ainsi, la moyenne d'un ensemble d'observations réduit la variance.

Pour plus de détails statistiques, consultez le tutoriel suivant :

%[https://medium.com/lunartechai/fundamentals-of-statistics-for-data-scientists-and-data-analysts-69d93a05aae7] 

Le Bagging est essentiellement une *agrégation Bootstrap* qui construit **B** arbres en utilisant des échantillons Bootstrap. Le Bagging peut être utilisé pour améliorer la précision (réduire la variance de nombreuses approches) en prenant des échantillons répétés à partir d'une seule donnée d'entraînement.

Ainsi, dans le Bagging, nous générons B échantillons d'entraînement bootstrap, sur la base desquels B arbres similaires (arbres corrélés) sont construits et finissent par être agrégés pour calculer les prédictions, en prenant la moyenne de ces prédictions pour ces B-échantillons. Notamment, chaque arbre est construit sur un ensemble de données bootstrap, indépendamment des autres arbres.

Ainsi, dans le cas du Bagging, à chaque division d'arbre, toutes les p caractéristiques sont considérées, ce qui entraîne des arbres similaires puisque chaque fois les prédicteurs les plus forts sont en haut et les plus faibles en bas, ce qui fait que tous les arbres bagués se ressembleront beaucoup.

#### 2.8.1 Bagging dans les Arbres de Régression

Pour appliquer le bagging aux arbres de régression, nous construisons simplement **B arbres de régression** en utilisant B ensembles d'entraînement bootstrap, et nous faisons la moyenne des prédictions résultantes. Ces arbres sont cultivés en profondeur et ne sont pas élagués. Ainsi, chaque arbre individuel a une variance élevée mais un faible biais. La moyenne de ces B arbres réduit la variance.

#### 2.8.2 Bagging dans les Arbres de Classification

Pour une observation de test donnée, nous pouvons enregistrer la classe prédite par chacun des B arbres, et **prendre une majorité de votes** : la prédiction globale est la classe majoritaire la plus courante parmi les B prédictions.

#### 2.8.3 Estimation de l'Erreur OOB (Out-of-Bag)

Lorsque le Bagging est appliqué aux arbres de décision, il n'est plus nécessaire d'appliquer la Validation Croisée pour estimer le taux d'erreur de test. Dans le bagging, nous ajustons les arbres de manière répétée aux échantillons bootstrap - et en moyenne seulement 2/3 de ces observations sont utilisées. Le tiers restant n'est pas utilisé pendant le processus d'entraînement. Ce sont les observations Out-of-bag.

Ainsi, il y a au total B/3 prédictions par i-ème observation non utilisée dans l'entraînement. Nous pouvons prendre la moyenne des valeurs de réponse pour ces cas (ou la classe majoritaire). Ainsi, par observation, l'erreur OOB et la moyenne de celles-ci forment le **taux d'erreur de test**.

#### 2.8.4 Bagging en Python

Rencontrez Lucy, une coach de fitness qui est curieuse de prédire la perte de poids de ses clients en fonction de leur apport calorique quotidien et de la durée de leurs séances d'entraînement. Lucy dispose de données de clients passés mais reconnaît que les prédictions individuelles peuvent être sujettes à des erreurs. Utilisons le Bagging pour créer un modèle de prédiction plus stable.

Techniquement, nous prédirons un résultat continu (perte de poids) en fonction de deux variables indépendantes (apport calorique quotidien et durée de l'entraînement), en utilisant le Bagging pour réduire la variance des prédictions.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree  # Assurez-vous que plot_tree est importé
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Données d'exemple
donnees_clients = np.array([[2000, 60], [2500, 45], [1800, 75], [2200, 50], [2100, 62], [2300, 70], [1900, 55], [2000, 65]])
perte_poids = np.array([3, 2, 4, 3, 3.5, 4.5, 3.7, 4.2])

# Division Train-Test
X_train, X_test, y_train, y_test = train_test_split(donnees_clients, perte_poids, test_size=0.25, random_state=42)

# Création d'un Modèle de Bagging
estimateur_de_base = DecisionTreeRegressor(max_depth=4)
modele = BaggingRegressor(base_estimator=estimateur_de_base, n_estimators=10, random_state=42)

# Entraînement du Modèle
modele.fit(X_train, y_train)

# Prédiction & Évaluation
y_pred = modele.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Affichage de la Prédiction et de l'Évaluation
print(f"Vraie perte de poids : {y_test}")
print(f"Perte de poids prédite : {y_pred}")
print(f"Erreur Quadratique Moyenne : {mse:.2f}")

# Visualisation de l'un des Estimateurs de Base (si souhaité)
plt.figure(figsize=(12, 8))
arbre = modele.estimators_[0]
plt.title('L\'un des Arbres de Décision de Base du Bagging')
plot_tree(arbre, filled=True, rounded=True, feature_names=["Apport Calorique", "Durée de l\'Entraînement"])
plt.show()
```

Vraie perte de poids : [2. 4.5]  
Perte de poids prédite : [3.1 3.96]  
Erreur Quadratique Moyenne : 0.75

* **Données d'exemple** : `donnees_clients` contient l'apport calorique quotidien et la durée de l'entraînement, et `perte_poids` contient la perte de poids correspondante.

* **Division Train-Test** : Nous divisons les données en ensembles d'entraînement et de test pour valider la performance prédictive du modèle.

* **Création et Entraînement du Modèle** : Nous instancions `BaggingRegressor` avec `DecisionTreeRegressor` comme estimateur de base et l'entraîons en utilisant `.fit()` avec nos données d'entraînement.

* **Prédiction & Évaluation** : Nous prédisons la perte de poids pour les données de test, en évaluant la qualité de la prédiction avec l'Erreur Quadratique Moyenne (MSE).

* **Visualisation de l'un des Estimateurs de Base** : Optionnellement, visualisez un arbre de l'ensemble pour comprendre les processus de décision individuels (en gardant à l'esprit qu'un arbre individuel peut ne pas bien performer, mais collectivement ils produisent des prédictions stables).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Bagging.png align="left")

*Source de l'Image : L'Auteur (il s'agit de l'un des arbres de décision dans le Bagging)*

### 2.9 Forêt Aléatoire

Les forêts aléatoires offrent une amélioration par rapport aux arbres bagués grâce à une petite modification qui décorrèle les arbres.

Comme dans le bagging, nous construisons un certain nombre d'arbres de décision sur des échantillons d'entraînement bootstrap. Mais lors de la construction de ces arbres de décision, chaque fois qu'une division dans un arbre est considérée, un échantillon aléatoire de m prédicteurs est choisi comme candidats de division parmi l'ensemble complet de p prédicteurs.

La division est autorisée à utiliser uniquement l'un de ces m prédicteurs. Un échantillon frais et aléatoire de m prédicteurs est pris à chaque division, et généralement nous choisissons **m ≈ √p** — c'est-à-dire, le nombre de prédicteurs considérés à chaque division est approximativement égal à la racine carrée du nombre total de prédicteurs. C'est aussi la raison pour laquelle la Forêt Aléatoire est appelée "aléatoire".

La principale différence entre le bagging et les forêts aléatoires est le choix de la taille du sous-ensemble de prédicteurs m qui décorrèle les arbres.

Utiliser une petite valeur de m dans la construction d'une forêt aléatoire sera généralement utile lorsque nous avons un grand nombre de prédicteurs corrélés. Ainsi, si vous avez un problème de Multicolinéarité, la RF est une bonne méthode pour résoudre ce problème.

Ainsi, contrairement au Bagging, dans le cas de la Forêt Aléatoire, à chaque division d'arbre, tous les p prédicteurs ne sont pas considérés — mais seulement m prédicteurs sélectionnés aléatoirement parmi eux. Cela entraîne des arbres non similaires étant décorrélés. Et en raison du fait que la moyenne des arbres décorrélés entraîne une variance plus faible, la Forêt Aléatoire est plus précise que le Bagging.

#### 2.9.1 Implémentation Python de la Forêt Aléatoire

Noah est un botaniste qui a collecté des données sur diverses espèces de plantes et leurs caractéristiques, telles que la taille des feuilles et la couleur des fleurs. Noah est curieux de savoir s'il pourrait prédire l'espèce d'une plante en fonction de ces caractéristiques.

Ici, nous utiliserons la Forêt Aléatoire, une méthode d'apprentissage par ensemble, pour l'aider à classer les plantes.

Techniquement, nous visons à classer les espèces de plantes en fonction de certaines variables prédictives en utilisant un modèle de Forêt Aléatoire.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Données Étendues
caracteristiques_plantes = np.array([
    [3, 1], [2, 2], [4, 1], [3, 2], [5, 1], [2, 2], [4, 1], [5, 2],
    [3, 1], [4, 2], [5, 1], [3, 2], [2, 1], [4, 2], [3, 1], [4, 2],
    [5, 1], [2, 2], [3, 1], [4, 2], [2, 1], [5, 2], [3, 1], [4, 2]
])
especes_plantes = np.array([
    0, 1, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1
])

# Division Train-Test
X_train, X_test, y_train, y_test = train_test_split(caracteristiques_plantes, especes_plantes, test_size=0.25, random_state=42)

# Création d'un Modèle de Forêt Aléatoire
modele = RandomForestClassifier(n_estimators=10, random_state=42)

# Entraînement du Modèle
modele.fit(X_train, y_train)

# Prédiction & Évaluation
y_pred = modele.predict(X_test)
rapport_classification = classification_report(y_test, y_pred)

# Affichage de la Prédiction et de l'Évaluation
print("Rapport de Classification :")
print(rapport_classification)


# Tracé en Nuage de Points Visualisant les Classes
plt.figure(figsize=(8, 4))
for espece, marqueur, couleur in zip([0, 1], ['o', 's'], ['forestgreen', 'darkred']):
    plt.scatter(caracteristiques_plantes[especes_plantes == espece, 0],
                caracteristiques_plantes[especes_plantes == espece, 1],
                marker=marqueur, color=couleur, label=f'Espèce {espece}')
plt.xlabel('Taille des Feuilles')
plt.ylabel('Couleur des Fleurs (codée)')
plt.title('Nuage de Points des Espèces')
plt.legend()
plt.tight_layout()
plt.show()

# Visualisation des Importances des Caractéristiques
plt.figure(figsize=(8, 4))
importances_caracteristiques = modele.feature_importances_
caracteristiques = ["Taille des Feuilles", "Couleur des Fleurs"]
plt.barh(caracteristiques, importances_caracteristiques, color = "darkred")
plt.xlabel('Importance')
plt.ylabel('Caractéristique')
plt.title('Importance des Caractéristiques')
plt.show()
```

* **Données d'exemple** : `caracteristiques_plantes` contient la taille des feuilles et la couleur des fleurs, tandis que `especes_plantes` indique l'espèce de la plante respective.

* **Division Train-Test** : Nous séparons les données en ensembles d'entraînement et de test.

* **Création et Entraînement du Modèle** : Nous instancions `RandomForestClassifier` avec un nombre spécifié d'arbres (10 dans ce cas) et l'entraîons en utilisant `.fit()` avec nos données d'entraînement.

* **Prédiction & Évaluation** : Nous prédisons l'espèce pour les données de test et évaluons les prédictions en utilisant un rapport de classification qui fournit la précision, le rappel, le score f1 et le support.

* **Visualisation des Importances des Caractéristiques** : Nous utilisons un graphique à barres horizontales pour afficher l'importance de chaque caractéristique dans la prédiction de l'espèce de la plante. La Forêt Aléatoire quantifie l'utilité des caractéristiques pendant le processus de construction de l'arbre, que nous visualisons ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Random-Forest.png align="left")

*\[Source de l'Image : L'Auteur\] Nuage de points des espèces*

![Image](https://www.freecodecamp.org/news/content/images/2023/10/RandomForest.png align="left")

*\[Source de l'Image : L'Auteur\] vous pouvez voir que la caractéristique Couleur des Fleurs a le plus grand impact dans la détermination de l'espèce de la plante.*

### 2.10 Boosting ou Modèles d'Ensemble

Comme le Bagging (moyenne d'Arbres de Décision corrélés) et la Forêt Aléatoire (moyenne d'Arbres de Décision non corrélés), le Boosting vise à améliorer les prédictions résultant d'un arbre de décision. Le Boosting est un modèle de Machine Learning supervisé qui peut être utilisé pour les problèmes de régression et de classification.

Contrairement au Bagging ou à la Forêt Aléatoire, où les arbres sont construits indépendamment les uns des autres en utilisant l'un des B échantillons bootstrap (copie de la date d'entraînement initiale), dans le Boosting, les arbres sont construits séquentiellement et dépendent les uns des autres. Chaque arbre est cultivé en utilisant les informations des arbres cultivés précédemment.

Le Boosting n'implique pas d'échantillonnage bootstrap. Au lieu de cela, chaque arbre s'ajuste sur une version modifiée de l'ensemble de données original. C'est une méthode de conversion des apprenants faibles en apprenants forts.

Dans le boosting, chaque nouvel arbre est ajusté sur une version modifiée de l'ensemble de données original. Ainsi, contrairement à l'ajustement d'un seul grand arbre de décision aux données, ce qui revient à ajuster les données de manière rigide et potentiellement à surajuster, l'approche de boosting apprend lentement.

Étant donné le modèle actuel, nous ajustons un arbre de décision aux résidus du modèle. C'est-à-dire, nous ajustons un arbre en utilisant les résidus actuels, plutôt que le résultat Y, comme réponse. Nous ajoutons ensuite cet nouvel arbre de décision à la fonction ajustée afin de mettre à jour les résidus.

Chacun de ces arbres peut être plutôt petit, avec seulement quelques nœuds terminaux, déterminés par le paramètre d dans l'algorithme. Maintenant, examinons les 3 modèles de Boosting les plus populaires en Machine Learning :

* AdaBoost

* GBM

* XGBoost

#### 2.10.1 Boosting : AdaBoost

Le premier algorithme d'Ensemble que nous allons examiner aujourd'hui est AdaBoost. Comme dans toutes les techniques de boosting, dans le cas d'AdaBoost, les arbres sont construits en utilisant les informations de l'arbre précédent - et plus spécifiquement la partie de l'arbre qui n'a pas bien performé. Cela s'appelle le faible apprenant (Decision Stump). Ce Decision Stump est construit en utilisant seulement un seul prédicteur et non tous les prédicteurs pour effectuer la prédiction.

Ainsi, AdaBoost combine des faibles apprenants pour faire des classifications et chaque souche est faite en utilisant les erreurs de la souche précédente. Voici le plan étape par étape pour construire un modèle AdaBoost :

* **Étape 1** : Attribution initiale des poids - attribuer un poids égal à toutes les observations de l'échantillon où ce poids représente l'importance des observations étant correctement classées : **1/N** (tous les échantillons sont également importants à ce stade).

* **Étape 2** : Sélection du prédicteur optimal - Le premier timbre est construit en obtenant le RSS (en cas de régression) ou l'indice GINI/Entropie (en cas de classification) pour chaque prédicteur. Choisir la souche qui fait le meilleur travail en termes de précision de prédiction : la souche avec le plus petit RSS ou GINI/Entropie est sélectionnée comme l'arbre suivant.

* **Étape 3** : Calcul du poids des souches basé sur l'erreur totale des souches - L'importance de cette souche dans l'arbre final est ensuite déterminée en utilisant l'erreur totale que cette souche commet. Où une souche qui n'est pas meilleure qu'un lancer de pièce aléatoire avec une erreur totale égale à 0,5 obtient un poids de 0. Poids = 0,5*log(1-Erreur Totale/Erreur Totale)

* **Étape 4** : Mise à jour des poids des observations - Nous augmentons le poids des observations qui ont été incorrectement prédites et diminuons les observations restantes qui avaient une précision plus élevée ou ont été correctement classées, de sorte que la souche suivante aura une importance plus élevée de prédire correctement la valeur de cette observation.

* **Étape 5** : Construction de la souche suivante basée sur les poids mis à jour - Utilisation de l'indice Gini pondéré pour choisir la souche suivante.

* **Étape 6** : Combinaison de B souches - Ensuite, toutes les souches sont combinées en tenant compte de leur importance, somme pondérée.

#### Implémentation Python d'AdaBoost

Imaginez un scénario où nous visons à prédire les prix des maisons en fonction de certaines caractéristiques comme le nombre de pièces et l'âge de la maison.

Pour cet exemple, générons des données synthétiques où : num_rooms : Le nombre de pièces dans la maison. house_age : L'âge de la maison en années. price : Le prix de la maison en milliers de dollars :

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error

# Seed pour la reproductibilité
np.random.seed(42)

# Générer des données synthétiques
num_samples = 200
num_rooms = np.random.randint(3, 10, num_samples)
house_age = np.random.randint(1, 100, num_samples)
noise = np.random.normal(0, 50, num_samples)

# Supposons une relation linéaire avec price = 50*rooms + 0.5*age + noise
price = 50*num_rooms + 0.5*house_age + noise

# Créer un DataFrame
data = pd.DataFrame({'num_rooms': num_rooms, 'house_age': house_age, 'price': price})

# Tracer
plt.scatter(data['num_rooms'], data['price'], label='Num Rooms vs Price', color = 'forestgreen')
plt.scatter(data['house_age'], data['price'], label='House Age vs Price', color = 'darkred')
plt.xlabel('Valeur de la Caractéristique')
plt.ylabel('Prix')
plt.legend()
plt.title('Graphiques de Dispersion des Caractéristiques vs Prix')
plt.show()

# Diviser les données en ensembles d\'entraînement et de test
X = data[['num_rooms', 'house_age']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser et entraîner le modèle AdaBoost Regressor
model_ab = AdaBoostRegressor(n_estimators=100, random_state=42)
model_ab.fit(X_train, y_train)

# Prédictions
predictions = model_ab.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f"Erreur Quadratique Moyenne : {mse:.2f}")
print(f"Racine de l\'Erreur Quadratique Moyenne : {rmse:.2f}")

# Visualisation : Prix Réels vs Prédits
plt.scatter(y_test, predictions, color = 'darkred')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
plt.xlabel('Prix Réels')
plt.ylabel('Prix Prédits')
plt.title('Prix Réels vs Prédits des Maisons avec AdaBoost')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-79.png align="left")

*\[Source de l'Image : L'Auteur\] Graphique de dispersion des caractéristiques vs prix*

![Image](https://www.freecodecamp.org/news/content/images/2023/10/AdaBoost.png align="left")

*\[Source de l'Image : L'Auteur\] Prix réels vs prédits des maisons avec AdaBoost*

#### 2.10.2 Algorithme de Boosting : Modèle de Boosting de Gradient (GBM)

AdaBoost et Gradient Boosting sont très similaires l'un à l'autre. Mais comparé à AdaBoost, qui commence le processus en sélectionnant une souche et continue à la construire en utilisant les apprenants faibles de la souche précédente, Gradient Boosting commence avec une seule feuille au lieu d'un arbre ou d'une souche.

Le résultat correspondant à cette feuille choisie est alors une première estimation pour la variable de résultat. Comme dans le cas d'AdaBoost, Gradient Boosting utilise les erreurs de la souche précédente pour construire l'arbre. Mais contrairement à AdaBoost, les arbres que Gradient Boost construit sont plus grands qu'une souche. C'est un paramètre où nous définissons un nombre maximal de feuilles.

Pour s'assurer que l'arbre n'est pas en surapprentissage, Gradient Boosting utilise le Taux d'Apprentissage pour mettre à l'échelle les contributions du gradient. Gradient Boosting est basé sur l'idée que faire beaucoup de petits pas dans la bonne direction (gradients) entraînera une variance plus faible (pour les données de test).

La principale différence entre les algorithmes AdaBoost et Gradient Boosting est la manière dont les deux identifient les faiblesses des apprenants faibles (par exemple, les arbres de décision). Alors que le modèle AdaBoost identifie les faiblesses en utilisant des points de données de poids élevé, le gradient boosting effectue la même chose en utilisant des gradients dans la fonction de perte (y=ax+b+e, e nécessite une mention spéciale car il s'agit du terme d'erreur).

La fonction de perte est une mesure indiquant à quel point les coefficients d'un modèle sont bons pour ajuster les données sous-jacentes. Une compréhension logique de la fonction de perte dépendrait de ce que nous essayons d'optimiser.

#### Arrêt Précoce

Le processus spécial de réglage du nombre d'itérations pour un algorithme (tel que GBM et Random Forest) est appelé "Arrêt Précoce" - un phénomène que nous avons abordé lors de la discussion sur les Arbres de Décision.

L'Arrêt Précoce effectue l'optimisation du modèle en surveillant la performance du modèle sur un ensemble de données de test séparé et en arrêtant la procédure d'entraînement une fois que la performance sur les données de test cesse de s'améliorer au-delà d'un certain nombre d'itérations.

Il évite le surapprentissage en tentant de sélectionner automatiquement le point d'inflexion où la performance sur l'ensemble de données de test commence à diminuer tandis que la performance sur l'ensemble de données d'entraînement continue de s'améliorer à mesure que le modèle commence à surapprendre.

Dans le contexte de GBM, l'arrêt précoce peut être basé soit sur un ensemble d'échantillons hors sac ("OOB") soit sur une validation croisée ("CV"). Comme mentionné précédemment, le moment idéal pour arrêter l'entraînement du modèle est lorsque l'erreur de validation a diminué et a commencé à se stabiliser avant qu'elle ne commence à augmenter en raison du surapprentissage.

Pour construire GBM, suivez ce processus étape par étape :

* **Étape 1** : Entraînez le modèle sur les données existantes pour prédire la variable de résultat

* **Étape 2** : Calculez le taux d'erreur en utilisant les prédictions et les valeurs réelles (Résidu Pseudo)

* **Étape 3** : Utilisez les caractéristiques existantes et le Résidu Pseudo comme variable de résultat pour prédire à nouveau les résidus

* **Étape 4** : Utilisez les résidus prédits pour mettre à jour les prédictions de l'Étape 1, tout en mettant à l'échelle cette contribution à l'arbre avec un taux d'apprentissage (hyper paramètre)

* **Étape 5** : Répétez les étapes 1-4, le processus de mise à jour des résidus pseudo et de l'arbre tout en mettant à l'échelle avec le taux d'apprentissage, pour avancer lentement dans la bonne direction jusqu'à ce qu'il n'y ait plus d'amélioration ou que nous arrivions à notre règle d'arrêt

L'idée est que chaque fois que nous ajoutons un nouvel arbre mis à l'échelle au modèle, les résidus devraient devenir plus petits.

À toute étape m, le modèle de Gradient Boosting produit un modèle qui est un ensemble de l'étape précédente F(m-1) et du taux d'apprentissage eta multiplié par la dérivée négative de la fonction de perte par rapport à la sortie du modèle à l'étape m-1 : (apprenant faible à l'étape m-1).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-64.png align="left")

#### Implémentation Python de GBM

```python
# Initialiser et entraîner le modèle Gradient Boosting Regressor
model_gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42)
model_gbm.fit(X_train, y_train)

# Prédictions
predictions = model_gbm.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f"Erreur Quadratique Moyenne : {mse:.2f}")
print(f"Racine de l\'Erreur Quadratique Moyenne : {rmse:.2f}")

# Visualisation : Prix Réels vs Prédits
plt.scatter(y_test, predictions, color = 'orange')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
plt.xlabel('Prix Réels')
plt.ylabel('Prix Prédits')
plt.title('Prix Réels vs Prédits des Maisons avec GBM')
plt.show()
```


![Image](https://www.freecodecamp.org/news/content/images/2023/10/GBM.png align="left")

*\[Source de l'Image : L'Auteur\] Prix réels vs prédits des maisons avec GBM*

#### 2.10.3 Algorithme de Boosting : XGBoost

L'un des algorithmes de Boosting ou d'Ensemble les plus populaires est l'Extreme Gradient Boosting (XGBoost).

La différence entre le GBM et le XGBoost est que dans le cas du XGBoost, les dérivées secondes sont calculées (gradients de second ordre). Cela fournit plus d'informations sur la direction des gradients et comment atteindre le minimum de la fonction de perte.

Rappelez-vous que cela est nécessaire pour identifier l'apprenant faible et améliorer le modèle en améliorant les apprenants faibles.

L'idée derrière le XGBoost est que la dérivée du 2nd ordre tend à être plus précise en termes de trouver la direction exacte. Comme l'AdaBoost, le XGBoost applique une régularisation avancée sous la forme de normes L1 ou L2 pour traiter le surapprentissage.

Contrairement à l'AdaBoost, le XGBoost est parallélisable grâce à son mécanisme de mise en cache spécial, ce qui le rend pratique pour gérer de grands ensembles de données complexes. De plus, pour accélérer l'entraînement, le XGBoost utilise un Algorithme Glouton Approximatif pour ne considérer qu'une quantité limitée de seuils pour diviser les nœuds des arbres.

Pour construire un modèle XGBoost, suivez ce processus étape par étape :

* **Étape 1** : Ajuster un seul arbre de décision - Dans cette étape, la fonction de perte est calculée, par exemple NDCG pour évaluer le modèle.

* **Étape 2** : Ajouter le deuxième arbre - Cela est fait de telle sorte que lorsque cet arbre est ajouté au modèle, il réduit la fonction de perte basée sur les dérivées de premier et de second ordre par rapport à l'arbre précédent (où nous avons également utilisé le taux d'apprentissage eta).

* **Étape 3** : Trouver la direction du prochain mouvement - En utilisant les dérivées de premier et de second degré, nous pouvons trouver la direction dans laquelle la fonction de perte diminue le plus. Cela correspond essentiellement au gradient de la fonction de perte par rapport à la sortie du modèle précédent.

* **Étape 4** : Diviser les nœuds - Pour diviser les observations, le XGBoost utilise un algorithme glouton approximatif (généralement environ 3 quantiles pondérés approximatifs) qui ont une somme de poids similaire. Pour trouver la valeur de division des nœuds, il ne considère pas tous les seuils candidats mais utilise plutôt uniquement les quantiles de ce prédicteur.

Le taux d'apprentissage optimal peut être déterminé en utilisant la validation croisée et la recherche par grille.

#### Implémentation Python Simple de XGBoost

Imaginez que vous avez un ensemble de données contenant des informations sur diverses maisons et leurs prix. L'ensemble de données comprend des caractéristiques comme le nombre de chambres, de salles de bain, la superficie totale, l'année de construction, etc., et vous souhaitez prédire le prix d'une maison en fonction de ces caractéristiques.

```python
import xgboost as xgb

# Initialiser et entraîner le modèle XGBoost
model_xgb = xgb.XGBRegressor(objective ='reg:squarederror', n_estimators = 100, seed = 42)
model_xgb.fit(X_train, y_train)

# Prédictions
predictions = model_xgb.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f"Erreur Quadratique Moyenne : {mse:.2f}")
print(f"Racine de l\'Erreur Quadratique Moyenne : {rmse:.2f}")

# Visualisation : Prix Réels vs Prédits
plt.scatter(y_test, predictions, color="forestgreen")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
plt.xlabel('Prix Réels')
plt.ylabel('Prix Prédits')
plt.title('Prix Réels vs Prédits des Maisons avec XGBoost')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/XGBoost2.png align="left")

*\[Source de l'Image : L'Auteur\] Prix réels vs prédits des maisons avec XGBoost*

## Chapitre 3 : Sélection de Caractéristiques en Machine Learning

Le chemin vers la construction de modèles de machine learning efficaces implique souvent une question critique : quelles caractéristiques devons-nous inclure pour générer des prédictions fiables tout en gardant le modèle simple et compréhensible ? C'est là que la sélection de sous-ensembles joue un rôle clé.

En Machine Learning, dans de nombreux cas, nous traitons avec un grand nombre de caractéristiques et toutes ne sont pas généralement importantes et informatives pour le modèle. Inclure de telles variables non pertinentes dans le modèle conduit à une complexité inutile dans le modèle de Machine Learning et affecte l'interprétabilité du modèle ainsi que sa performance.

En supprimant ces variables non importantes et en sélectionnant uniquement des caractéristiques relativement informatives, nous pouvons obtenir un modèle qui peut être plus facile à interpréter et potentiellement plus précis.

Regardons un exemple spécifique d'un modèle de Machine Learning pour simplifier.

Supposons que nous regardons un modèle de Régression Linéaire Multiple (plusieurs variables indépendantes et une seule variable de réponse/dépendante) avec un très grand nombre de caractéristiques. Ce modèle est susceptible d'être complexe lorsqu'il s'agit de l'interpréter. En plus de cela, il pourrait entraîner des prédictions inexactes puisque certaines de ces caractéristiques pourraient être non importantes et n'aident pas à expliquer la variable de réponse.

Le processus de sélection des variables importantes dans le modèle est appelé sélection de caractéristiques ou sélection de variables. Ce processus implique d'identifier un sous-ensemble des variables p que nous croyons être liées à la variable dépendante ou de réponse. Pour cela, nous devons exécuter la régression pour toutes les combinaisons possibles de variables indépendantes et sélectionner celle qui donne le modèle le mieux performant ou le moins performant.

Il existe diverses approches que vous pouvez utiliser pour la Sélection de Caractéristiques, généralement divisées en les 3 catégories suivantes :

* Sélection de Sous-ensembles (Meilleure Sélection de Sous-ensembles, Sélection de Caractéristiques Étape par Étape)

* Techniques de Régularisation (L1 Lasso, L2 Ridge Régressions)

* Techniques de Réduction de Dimensionnalité (PCA)

### 3.1 Sélection de Sous-ensembles en Machine Learning

La Sélection de Sous-ensembles en machine learning est une technique conçue pour identifier et utiliser un sous-ensemble de caractéristiques importantes tout en omettant les autres. Cela aide à créer des modèles qui sont plus faciles à interpréter et, dans certains cas, prédisent plus précisément en évitant le surapprentissage.

En naviguant à travers de nombreuses caractéristiques, il devient vital de choisir sélectivement celles qui ont un impact significatif sur le modèle prédictif. La sélection de sous-ensembles fournit une approche systématique pour trier les combinaisons possibles de prédicteurs. Elle vise à sélectionner un sous-ensemble qui représente efficacement les données sans complexité inutile.

* **Meilleure Sélection de Sous-ensembles** : Examine toutes les combinaisons possibles et sélectionne l'ensemble le plus optimal de prédicteurs.

* **Sélection Étape par Étape** : Ajoute ou retire des prédicteurs de manière incrémentielle, ce qui inclut la sélection étape par étape vers l'avant et vers l'arrière.

* **Sélection Aléatoire de Sous-ensembles** : Choisit des sous-ensembles de manière aléatoire, introduisant un élément d'aléatoire dans la sélection du modèle.

C'est un équilibre entre l'utilisation de tous les prédicteurs disponibles, risquant la surcomplexité du modèle et le surapprentissage potentiel, et la construction d'un modèle trop simple qui pourrait négliger des motifs de données importants.

Dans cette section, nous allons explorer ces techniques de sélection de sous-ensembles. Vous apprendrez comment chaque approche fonctionne et affecte la performance du modèle, en veillant à ce que les modèles que nous construisons soient fiables, simples et efficaces.

#### 3.1.1 Techniques de Sélection de Caractéristiques Étape par Étape

L'une des techniques populaires de sélection de sous-ensembles est la Technique de Sélection de Caractéristiques Étape par Étape. Regardons deux méthodes différentes de sélection de caractéristiques étape par étape :

* Sélection Étape par Étape Vers l'Avant

* Sélection Étape par Étape Vers l'Arrière

**Sélection Étape par Étape Vers l'Avant** : Ce que fait la technique de Sélection de Caractéristiques Étape par Étape Vers l'Avant, c'est qu'elle commence avec un modèle vide Null avec seulement une interception. Nous exécutons ensuite un ensemble de régressions simples et choisissons la variable qui a un modèle avec le plus petit RSS (Somme des Carrés des Résidus). Ensuite, nous faisons de même avec des régressions à deux variables et continuons jusqu'à ce que ce soit terminé.

Ainsi, la Sélection Étape par Étape Vers l'Avant commence avec un modèle ne contenant aucun prédicteur, puis ajoute des prédicteurs au modèle, un à la fois, jusqu'à ce que tous les prédicteurs soient dans le modèle. En particulier, à chaque étape, la variable qui donne l'amélioration supplémentaire la plus grande à l'ajustement est ajoutée au modèle.

La Sélection Étape par Étape Vers l'Avant peut être résumée comme suit :

**Étape 1** : Soit M_0 le modèle nul, ne contenant aucune caractéristique.

**Étape 2** : Pour K = 0, ..., p-1 :

* Considérer tous les (p-k) modèles qui contiennent les variables dans M_k avec une caractéristique ou un prédicteur supplémentaire.

* Choisir le meilleur modèle parmi ces p-k modèles, et le définir M_(k+1) en utilisant des métriques de performance telles que [RSS](https://en.wikipedia.org/wiki/Residual_sum_of_squares)/[R-carré](https://www.investopedia.com/terms/r/r-squared.asp).

**Étape 3** : Sélectionner le modèle unique avec la meilleure performance parmi ces M_0, ..., M_p modèles (celui avec la plus petite [Erreur de Validation Croisée](https://datascienceplus.com/cross-validation-estimating-prediction-error/), [C_p](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6), [AIC](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6) [(Critère d'Information d'Akaike)](https://en.wikipedia.org/wiki/Akaike_information_criterion), [BIC](https://en.wikipedia.org/wiki/Bayesian_information_criterion) (Critères d'Information Bayésiens) ou [R-carré ajusté](https://en.wikipedia.org/wiki/Coefficient_of_determinationv) est votre meilleur modèle M*).

Ainsi, l'idée derrière cette Sélection est de commencer simplement et d'augmenter le nombre de prédicteurs dans le modèle. Par nombre de prédicteurs, considérer toutes les combinaisons possibles de variables et sélectionner un seul meilleur modèle : M_k. Ensuite, comparer tous ces modèles avec différents nombres de prédicteurs (meilleurs M_k) et celui qui performe le mieux peut être sélectionné.

Lorsque n < p, c'est-à-dire lorsque le nombre d'observations est plus grand que le nombre de prédicteurs dans la Régression Linéaire, vous pouvez utiliser cette approche pour sélectionner les caractéristiques dans le modèle afin que la LR fonctionne en premier lieu.

**Sélection Étape par Étape Vers l'Arrière** : Contrairement à la Sélection Étape par Étape Vers l'Avant, dans le cas de la Sélection Étape par Étape Vers l'Arrière, l'algorithme de sélection de caractéristiques commence avec le modèle complet contenant tous les p prédicteurs. Ensuite, le meilleur modèle avec p prédicteurs est sélectionné.

Par conséquent, le modèle supprime un par un la variable avec la plus grande valeur p et le meilleur modèle est à nouveau sélectionné.

Chaque fois, le modèle est ajusté à nouveau pour identifier la variable la moins statistiquement significative jusqu'à ce que la règle d'arrêt soit atteinte. (Par exemple, toutes les valeurs p doivent être inférieures à 5 %.) Ensuite, nous comparons tous ces modèles avec différents nombres de prédicteurs (meilleurs M_k) et sélectionnons le modèle unique avec la meilleure performance parmi ces M_0, ..., M_p modèles (celui avec la plus petite [Erreur de Validation Croisée](https://datascienceplus.com/cross-validation-estimating-prediction-error/), [C_p](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6), [AIC](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6) [(Critère d'Information d'Akaike)](https://en.wikipedia.org/wiki/Akaike_information_criterion), [BIC](https://en.wikipedia.org/wiki/Bayesian_information_criterion) (Critères d'Information Bayésiens) ou [R-carré ajusté](https://en.wikipedia.org/wiki/Coefficient_of_determinationv) est votre meilleur modèle M*).

La Sélection Étape par Étape Vers l'Arrière peut être résumée comme suit :

**Étape 1** : Soit M_p le modèle complet, contenant toutes les caractéristiques.

**Étape 2** : Pour k = p, p-1 ..., 1 :

* Considérer tous les k modèles qui contiennent toutes les variables sauf pour l'un des prédicteurs dans le modèle M_k, pour k - 1 caractéristiques.

* Choisir le meilleur modèle parmi ces k modèles, et le définir M_(k-1) en utilisant des métriques de performance telles que [RSS](https://en.wikipedia.org/wiki/Residual_sum_of_squares)/[R-carré](https://www.investopedia.com/terms/r/r-squared.asp).

**Étape 3** : Sélectionner le modèle unique avec la meilleure performance parmi ces M_0, ..., M_p modèles (celui avec la plus petite [Erreur de Validation Croisée](https://datascienceplus.com/cross-validation-estimating-prediction-error/), [C_p](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6), [AIC](https://medium.com/analytics-vidhya/model-selection-cp-aic-bic-and-adjusted-r2-6a0af25945b6) [(Critère d'Information d'Akaike)](https://en.wikipedia.org/wiki/Akaike_information_criterion), [BIC](https://en.wikipedia.org/wiki/Bayesian_information_criterion) (Critères d'Information Bayésiens) ou [R-carré ajusté](https://en.wikipedia.org/wiki/Coefficient_of_determinationv) est votre meilleur modèle M*).

Comme la Sélection Étape par Étape Vers l'Avant, la technique de Sélection Étape par Étape Vers l'Arrière recherche seulement (p+1)/2 modèles, ce qui la rend possible à appliquer dans des contextes où p est trop grand pour appliquer d'autres techniques de sélection.

De plus, la Sélection Étape par Étape Vers l'Arrière n'est pas garantie de produire le meilleur modèle contenant un sous-ensemble des p prédicteurs. Elle nécessite que le nombre d'observations ou de points de données n soit supérieur au nombre de variables du modèle p alors que la Sélection Étape par Étape Vers l'Avant peut être utilisée même lorsque n < p.

### 3.2 Régularisation en Machine Learning

La régularisation, également connue sous le nom de Rétrécissement, est une stratégie largement utilisée pour traiter le problème de surapprentissage dans les modèles de machine learning.

Le concept fondamental de la régularisation implique l'introduction délibérée d'un léger biais dans le modèle, avec l'avantage de réduire notablement sa variance.

Le terme "Rétrécissement" est dérivé de la capacité de la méthode à tirer certains des coefficients estimés vers zéro, en imposant une pénalité pour les empêcher d'élever la variance du modèle de manière excessive.

Deux techniques de régularisation proéminentes se distinguent en pratique : la Régression Ridge, qui utilise la norme L2, et la Régression Lasso, employant la norme L1.

#### 3.2.1 Régression Ridge (Régularisation L2)

Explorons des exemples de régression linéaire multiple, impliquant p variables indépendantes ou prédicteurs utilisés pour modéliser la variable dépendante y.

Il est bon de se rappeler que les Moindres Carrés Ordinaires (OLS), à condition que ses hypothèses soient satisfaites, est une technique d'estimation largement adoptée pour déterminer les paramètres de la régression linéaire. L'OLS recherche les coefficients optimaux en minimisant la somme des carrés des résidus (RSS) du modèle. C'est-à-dire :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*9mdYD6q-ns3ZO5KYw046Uw.png align="left")

où β représente les estimations des coefficients pour différentes variables ou prédicteurs (X).

La Régression Ridge est assez similaire à l'OLS, sauf que les coefficients sont estimés en minimisant une fonction de coût ou de perte légèrement différente. Plus précisément, les estimations des coefficients de la Régression Ridge β̂R sont telles qu'elles minimisent la fonction de perte suivante :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*Yri4m3wximoVgqCdfjqybg.png align="left")

où λ (lambda, qui est toujours positif, ≥ 0) est le paramètre de réglage ou le paramètre de pénalité, et comme on peut le voir dans cette formule, dans le cas de la Ridge, la pénalité L2 ou la norme L2 est utilisée.

De cette manière, la Régression Ridge attribuera une pénalité à certaines variables, réduisant leurs coefficients vers zéro, diminuant ainsi la variance globale du modèle - mais ces coefficients ne deviendront jamais exactement zéro. Ainsi, les paramètres du modèle ne sont jamais définis exactement à 0, ce qui signifie que tous les p prédicteurs du modèle sont toujours intacts.

#### Norme L2 (Distance Euclidienne)

La norme L2 est un terme mathématique qui provient de l'algèbre linéaire. Elle représente une norme euclidienne qui peut être représentée comme suit :

![Image](https://miro.medium.com/v2/resize:fit:968/1*3XOoIOpLRREo4882c2K0kQ.png align="left")

**Paramètre de réglage λ** : le paramètre de réglage λ sert à contrôler l'impact relatif de la pénalité sur les estimations des coefficients de régression. Lorsque λ = 0, le terme de pénalité n'a aucun effet, et la régression ridge produira les estimations des moindres carrés ordinaires. Mais lorsque λ → ∞ (devient très grand), l'impact de la pénalité de rétrécissement augmente, et les estimations des coefficients de régression ridge approchent de 0. Voici une représentation visuelle de cela :

![Image](https://miro.medium.com/v2/resize:fit:1344/1*2ICCHEBIlr2WkJwBdH4ZpQ.png align="left")

*Source de l'Image : L'Auteur*

#### Pourquoi la Régression Ridge Fonctionne-t-elle ?

L'avantage de la régression ridge par rapport aux moindres carrés ordinaires provient du phénomène de compromis biais-variance introduit précédemment. À mesure que λ, le paramètre de pénalité, augmente, la flexibilité de l'ajustement de la régression ridge diminue, ce qui entraîne une variance diminuée mais un biais accru.

#### 3.2.2 Régression Lasso (Régularisation L1)

La Régression Lasso surmonte cet inconvénient de la Régression Ridge. Plus précisément, les estimations des coefficients de la Régression Lasso β̂λL sont les valeurs qui minimisent :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*9xgT0094jajcR3h4LuLjNQ.png align="left")

Comme pour la Régression Ridge, le Lasso réduit les estimations des coefficients vers zéro. Mais dans le cas du Lasso, la **pénalité L1 ou la norme L1** est utilisée, ce qui a pour effet de forcer certaines des estimations des coefficients à être exactement égales à zéro lorsque le paramètre de réglage λ est suffisamment grand.

Ainsi, comme de nombreuses techniques de sélection de caractéristiques, la Régression Lasso effectue une sélection de variables en plus de résoudre le problème de surapprentissage.

![Image](https://miro.medium.com/v2/resize:fit:1400/1*xxJGK_RO3yMMk78jzXC7qw.png align="left")

*\[Source de l'Image : L'Auteur\] Régression Lasso*

#### Norme L1 (Distance de Manhattan)

La norme L1 est un terme mathématique qui provient de l'algèbre linéaire. Elle représente une norme de Manhattan qui peut être représentée comme suit :

![Image](https://miro.medium.com/v2/resize:fit:804/1*-6vGuuy9s8FahKYyEEjSwQ.png align="left")

#### Pourquoi la Régression Lasso Fonctionne-t-elle ?

Comme la Régression Ridge, l'avantage de la Régression Lasso par rapport aux moindres carrés ordinaires provient du compromis biais-variance introduit précédemment. À mesure que λ augmente, la flexibilité de l'ajustement de la régression ridge diminue. Cela conduit à une variance diminuée mais à un biais accru. De plus, le Lasso effectue également une sélection de caractéristiques.

#### 3.2.3 Lasso vs Régression Ridge

La Régression Lasso réduit les estimations des coefficients vers zéro et force même certains de ces coefficients à être exactement égaux à zéro lorsque le paramètre de réglage λ est suffisamment grand. Ainsi, comme de nombreuses techniques de sélection de caractéristiques, la Régression Lasso effectue une sélection de variables en plus de résoudre le problème de surapprentissage.

La comparaison entre la Régression Ridge et la Régression Lasso devient claire lorsque l'on place les deux graphiques précédents côte à côte :

![Image](https://miro.medium.com/v2/resize:fit:1400/1*oq-2dyqDAC9T_MkUYnu61g.png align="left")

*\[Source de l'Image : L'Auteur\] Régression Lasso vs Régression Ridge*

Si vous souhaitez apprendre la régularisation en détail, lisez ce tutoriel :

%[https://towardsdatascience.com/bias-variance-trade-off-overfitting-regularization-in-machine-learning-d79c6d8f20b4] 

## Chapitre 4 : Techniques de Rééchantillonnage en Machine Learning

Lorsque nous n'avons que des données d'entraînement et que nous voulons faire des jugements sur la performance du modèle sur des données invisibles, nous pouvons utiliser des Techniques de Rééchantillonnage pour créer des données de test artificielles.

Les Techniques de Rééchantillonnage sont souvent divisées en deux catégories : la Validation Croisée et le Bootstrapping. Elles sont généralement utilisées pour les trois objectifs suivants :

* Évaluation du Modèle : évaluer la performance du modèle (pour calculer le taux d'erreur de test)

* Variance du Modèle : calculer la variance du modèle pour vérifier la généralisabilité de votre modèle

* Sélection du Modèle : sélectionner la flexibilité du modèle

Par exemple, afin d'estimer la variabilité d'un ajustement de régression linéaire, nous pouvons tirer répétitivement différents échantillons des données d'entraînement, ajuster une régression linéaire à chaque nouvel échantillon, puis examiner dans quelle mesure les ajustements résultants diffèrent.

### 4.1 Validation Croisée

La validation croisée peut être utilisée pour estimer l'erreur de test associée à une méthode d'apprentissage statistique donnée afin de réaliser :

* L'évaluation du modèle : pour évaluer ses performances en calculant le taux d'erreur de test

* La sélection du modèle : pour choisir le niveau de flexibilité approprié.

Vous retenez un sous-ensemble des observations d'entraînement du processus d'ajustement, puis appliquez la méthode d'apprentissage statistique à ces observations retenues.

La validation croisée est généralement divisée en les trois catégories suivantes :

* Approche par Ensemble de Validation

* Validation Croisée K-fold (K-ford CV)

* Validation Croisée Leave One Out (LOOCV)

#### 4.1.1 Approche par Ensemble de Validation

Il s'agit d'une approche simple consistant à diviser aléatoirement les données en ensembles d'entraînement et de validation. Cette approche utilise généralement la fonction [train_test_split() de Sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

Le modèle est ensuite entraîné sur les données d'entraînement (généralement 80 % des données) et les utilise pour prédire les valeurs de l'ensemble de validation ou de test (généralement 20 % des données), ce qui donne le taux d'erreur de test.

#### 4.1.2 Validation Croisée Leave One Out (LOOCV)

La LOOCV est similaire à l'approche par ensemble de validation. Mais chaque fois, elle laisse une observation hors de l'ensemble d'entraînement et utilise les n-1 restantes pour entraîner le modèle et calcule l'MSE pour cette seule prédiction. Ainsi, dans le cas de la LOOCV, le modèle doit être ajusté n fois (où n est le nombre d'observations dans le modèle).

Ensuite, ce processus est répété pour toutes les observations et n fois les MSE sont calculées. La moyenne des MSE est le taux d'erreur de validation croisée et peut être exprimée comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-66.png align="left")


#### 4.1.3 Validation Croisée K-fold (K-ford CV)

La validation croisée K-Fold est le juste milieu entre l'approche par ensemble de validation (variance élevée et biais élevé mais efficace en calcul) et la LOOCV (biais faible et variance faible mais inefficace en calcul).

Dans la validation croisée K-Fold, les données sont échantillonnées aléatoirement en K échantillons de taille égale (K-folds). Ensuite, chaque fois, 1 est utilisé comme validation et le reste comme entraînement, et le modèle est ajusté K fois. La moyenne des K MSE forme le taux d'erreur de test de validation croisée.

Notez que la LOOCV est un cas particulier de la validation croisée K-fold où K = N, et peut être exprimée comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-67.png align="left")


#### 4.2 Sélection du k Optimal dans la Validation Croisée K-fold

Le choix de k dans la validation croisée K-fold est une question de compromis entre le biais et la variance et l'efficacité du modèle. Habituellement, la validation croisée K-Fold et la LOOCV fournissent des résultats similaires et leurs performances peuvent être évaluées en utilisant des données simulées.

Cependant, la LOOCV a un biais plus faible (non biaisé) par rapport à la validation croisée K-fold car la LOOCV utilise plus de données d'entraînement que la validation croisée K-fold. Mais la LOOCV a une variance plus élevée que la validation croisée K-fold car la LOOCV ajuste le modèle sur des données presque identiques pour chaque élément et les résultats sont fortement corrélés par rapport aux résultats de la validation croisée K-fold qui sont moins corrélés.

Puisque la moyenne des résultats fortement corrélés a une variance plus élevée que celle des résultats moins corrélés, la variance de la LOOCV est plus élevée.

* K = N (LOOCV), plus K est grand → variance plus élevée et biais plus faible

* K = 1, plus K est petit → variance plus faible et biais plus élevé

En tenant compte de ces informations, nous pouvons calculer la performance du modèle pour divers K, par exemple K = 3,5,6,7…,10 ou l'erreur de classification de type I, de type II et totale du modèle dans le cas d'un modèle de classification. Ensuite, le K du modèle le mieux performant peut être le K optimal en utilisant l'idée de la courbe ROC (cas de classification) ou la méthode du coude (cas de régression).

### 4.3 Bootstrapping

Le Bootstrapping est une autre technique de rééchantillonnage très populaire qui est utilisée à diverses fins. L'une d'entre elles est d'estimer efficacement la variabilité des estimations/modèles ou de créer des échantillons artificiels à partir d'un échantillon existant et d'améliorer la performance du modèle (comme dans le cas du Bagging ou de la Forêt Aléatoire).

Il est utilisé dans de nombreuses situations où il est difficile ou même impossible de calculer directement l'écart-type d'une quantité d'intérêt.

* C'est une méthode très utile pour quantifier l'incertitude associée à la méthode d'apprentissage statistique et obtenir les erreurs standards/mesure de variabilité.

* Il n'est pas utile pour la Régression Linéaire puisque le R/Python standard fournit ces résultats (SE des coefficients).

Le Bootstrapping est extrêmement pratique pour d'autres méthodes également où la variabilité est plus difficile à quantifier. L'échantillonnage bootstrap est effectué avec remplacement, ce qui signifie que la même observation peut apparaître plus d'une fois dans l'ensemble de données bootstrap.

Ainsi, le Bootstrapping prend l'échantillon d'entraînement original et le rééchantillonne par remplacement, résultant en B échantillons différents. Ensuite, pour chacun de ces échantillons simulés, l'estimation du coefficient est calculée. Ensuite, en prenant la moyenne de ces estimations de coefficients et en utilisant la formule courante pour SE, nous calculons l'Erreur Standard du modèle Bootstrap.

Lisez plus à ce sujet [ici](https://github.com/TatevKaren/mathematics-statistics-for-data-science/tree/main/Bootstrapping).

## Chapitre 5 : Techniques d'Optimisation

Connaître les fondamentaux des modèles de Machine Learning et apprendre à entraîner ces modèles est définitivement une grande partie de devenir un Data Scientist technique. Mais ce n'est qu'une partie du travail.

Pour utiliser le modèle de Machine Learning afin de résoudre un problème commercial, vous devez l'optimiser après avoir établi sa ligne de base. C'est-à-dire, vous devez optimiser l'ensemble des hyperparamètres dans votre modèle de Machine Learning pour trouver l'ensemble des paramètres optimaux qui résultent en le modèle le mieux performant (toutes choses étant égales par ailleurs).

Ainsi, pour optimiser ou ajuster votre modèle de Machine Learning, vous devez effectuer une optimisation des hyperparamètres. En trouvant la combinaison optimale des valeurs des hyperparamètres, nous pouvons diminuer les erreurs que le modèle produit et construire le modèle le plus précis.

Un hyperparamètre de modèle est une constante dans le modèle. Il est externe au modèle, et sa valeur ne peut pas être estimée à partir des données (mais doit plutôt être spécifiée à l'avance avant que le modèle ne soit entraîné). Par exemple, k dans les k-Plus Proches Voisins (kNN) ou le nombre de couches cachées dans les Réseaux de Neurones.

Les méthodes d'optimisation des hyperparamètres sont généralement catégorisées en :

* Recherche Exhaustive ou Approche par Force Brute (comme la Recherche sur Grille)

* Descente de Gradient (GD par Lots, SGD, SDG avec Momentum, Adam)

* Algorithmes Génétiques

Dans ce manuel, je ne discuterai que des deux premiers types de techniques d'optimisation.

### 5.1 Approche par Force Brute (Recherche sur Grille)

La Recherche Exhaustive (souvent appelée Recherche sur Grille ou Approche par Force Brute) est le processus de recherche des hyperparamètres les plus optimaux en vérifiant chacun des candidats pour les hyperparamètres et en calculant le taux d'erreur du modèle.

Une fois que nous avons créé la liste des valeurs possibles pour chacun des hyperparamètres, pour chaque combinaison possible de valeurs d'hyperparamètres, nous calculons le taux d'erreur du modèle et le comparons au modèle optimal actuel (celui avec le taux d'erreur minimum). À chaque itération, le modèle optimal est mis à jour si les nouvelles valeurs de paramètres entraînent un taux d'erreur plus faible.

La méthode d'optimisation est simple. Par exemple, si vous travaillez avec un algorithme de clustering K-means, vous pouvez rechercher manuellement le bon nombre de clusters. Mais s'il y a des centaines ou des milliers de combinaisons possibles de valeurs d'hyperparamètres que vous devez considérer, le modèle peut prendre des heures ou des jours à entraîner — et il devient incroyablement lourd et lent. Ainsi, la plupart du temps, la recherche par force brute est inefficace.

Pour optimiser ou ajuster votre modèle de Machine Learning, vous devez effectuer une optimisation des hyperparamètres. En trouvant la combinaison optimale des valeurs des hyperparamètres, nous pouvons diminuer l'erreur que le modèle produit et construire le modèle le plus précis.

En ce qui concerne les techniques d'optimisation de type Descente de Gradient, leurs variantes telles que la Descente de Gradient par Lots, la Descente de Gradient Stochastique, etc., diffèrent en termes de quantité de données utilisées pour calculer le gradient de la fonction de Perte ou de Coût.

Définissons cette fonction de Perte par **J(θ)** où **θ (thêta)** représente le paramètre que nous voulons optimiser.

La quantité d'utilisation des données concerne un compromis entre la précision de la mise à jour du paramètre et le temps nécessaire pour effectuer une telle mise à jour. À savoir, plus l'échantillon de données que nous utilisons est grand, plus nous pouvons nous attendre à un ajustement plus précis d'un paramètre — mais le processus sera alors beaucoup plus lent.

L'inverse est également vrai. Plus l'échantillon de données est petit, moins les ajustements du paramètre seront précis, mais le processus sera beaucoup plus rapide.

### 5.2 Optimisation par Descente de Gradient (GD)

L'algorithme de Descente de Gradient par Lots (souvent simplement appelé Descente de Gradient ou GD) calcule le gradient de la Fonction de Perte **J(θ)** par rapport au paramètre cible en utilisant l'ensemble des données d'entraînement.

Nous faisons cela en prédisant d'abord les valeurs pour toutes les observations à chaque itération, et en les comparant à la valeur donnée dans les données d'entraînement. Ces deux valeurs sont utilisées pour calculer le terme d'erreur de prédiction par observation qui est ensuite utilisé pour mettre à jour les paramètres du modèle. Ce processus continue jusqu'à ce que le modèle converge.

Le gradient ou la dérivée première de la fonction de perte peut être exprimé comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-70.png align="left")

Ensuite, ce gradient est utilisé pour mettre à jour la valeur de l'itération précédente du paramètre cible. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-71.png align="left")

où

* *θ* : Cela représente le(s) paramètre(s) ou poids(s) d'un modèle que vous essayez d'optimiser. Dans de nombreux contextes, notamment dans les réseaux de neurones, *θ* peut être un vecteur contenant de nombreux poids individuels.

* *η* : Il s'agit du taux d'apprentissage. C'est un hyperparamètre qui dicte la taille du pas à chaque itération tout en se déplaçant vers un minimum de la fonction de coût. Un taux d'apprentissage plus petit peut rendre l'optimisation plus précise mais pourrait également ralentir le processus de convergence, tandis qu'un taux d'apprentissage plus grand pourrait accélérer la convergence mais risque de dépasser le minimum. Peut être [0,1] mais est généralement un nombre entre (0.001 et 0.04)

* ∇_J_(θ) : Il s'agit du gradient de la fonction de coût *J* par rapport au paramètre θ. Il indique la direction et l'amplitude de l'augmentation la plus raide de *J*. En soustrayant cela de la valeur actuelle du paramètre (multipliée par le taux d'apprentissage), nous ajustons *θ* dans la direction de la diminution la plus raide de *J*.

Il y a deux inconvénients majeurs à la GD qui rendent cette technique d'optimisation peu populaire, surtout lorsqu'on traite avec des ensembles de données grands et complexes. Puisque dans chaque itération, l'ensemble des données d'entraînement doit être utilisé et stocké, le temps de calcul peut être très long, ce qui entraîne un processus incroyablement lent. En plus de cela, le stockage de cette grande quantité de données entraîne des problèmes de mémoire, rendant la GD lourde et lente en termes de calcul.

### 5.3 Descente de Gradient Stochastique (SGD)

La méthode de Descente de Gradient Stochastique (SGD), également connue sous le nom de Descente de Gradient Incrémentale, est une approche itérative pour résoudre les problèmes d'optimisation avec une fonction objectif différentielle, exactement comme la GD.

Mais contrairement à la GD, la SGD n'utilise pas l'ensemble complet des données d'entraînement pour mettre à jour la valeur du paramètre à chaque itération. La méthode SGD est souvent appelée approximation stochastique de la descente de gradient qui vise à trouver les points extrêmes ou zéro de la fonction stochastique contenant des paramètres qui ne peuvent pas être estimés directement.

La SGD minimise cette fonction de coût en parcourant les données de l'ensemble de données d'entraînement et en mettant à jour les valeurs des paramètres à chaque itération.

Dans la SGD, tous les paramètres du modèle sont améliorés à chaque étape d'itération avec un seul échantillon d'entraînement. Ainsi, au lieu de parcourir tous les échantillons d'entraînement à la fois pour modifier les paramètres du modèle, l'algorithme SGD améliore les paramètres en regardant un seul ensemble d'entraînement **aléatoirement** échantillonné (d'où le nom **Stochastique**). C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-72.png align="left")

où

* *θ* : Cela représente le(s) paramètre(s) ou poids(s) d'un modèle que vous essayez d'optimiser. Dans de nombreux contextes, notamment dans les réseaux de neurones, *θ* peut être un vecteur contenant de nombreux poids individuels.

* *η* : Il s'agit du taux d'apprentissage. C'est un hyperparamètre qui dicte la taille du pas à chaque itération tout en se déplaçant vers un minimum de la fonction de coût. Un taux d'apprentissage plus petit peut rendre l'optimisation plus précise mais pourrait également ralentir le processus de convergence, tandis qu'un taux d'apprentissage plus grand pourrait accélérer la convergence mais risque de dépasser le minimum.

* ∇_J_(θ, x(i), y(i)) : Il s'agit du gradient de la fonction de coût *J* par rapport au paramètre θ pour une entrée donnée *x(i)* et sa sortie cible correspondante *y(i)*. Il indique la direction et l'amplitude de l'augmentation la plus raide de *J*. En soustrayant cela de la valeur actuelle du paramètre (multipliée par le taux d'apprentissage), nous ajustons *θ* dans la direction de la diminution la plus raide de *J*.

* *x(i)* : Cela représente le *ième* échantillon de données d'entrée de votre ensemble de données.

* *y(i)* : Il s'agit de la vraie sortie cible pour le *ième* échantillon de données d'entrée.

Dans le contexte de la Descente de Gradient Stochastique (SGD), la règle de mise à jour s'applique aux échantillons de données individuels *x(i)* et *y(i)* plutôt qu'à l'ensemble de données complet, ce qui serait le cas pour la Descente de Gradient par Lots.

Cette étape unique améliore la vitesse du processus de recherche des minima globaux du problème d'optimisation et c'est ce qui différencie la SGD de la GD. Ainsi, la SGD ajuste constamment les paramètres en tentant de se déplacer dans la direction du minimum global de la fonction objectif.

La SGD aborde le problème du temps de calcul lent de la GD, car elle est bien adaptée aux grandes données et à la taille du modèle. Mais même si la méthode SGD elle-même est simple et rapide, elle est connue comme un "mauvais optimiseur" car elle est sujette à trouver un optimum local au lieu d'un optimum global.

Dans la SGD, tous les paramètres du modèle sont améliorés à chaque étape d'itération avec un seul échantillon d'entraînement. Ainsi, au lieu de parcourir tous les échantillons d'entraînement à la fois pour modifier les paramètres du modèle, la SGD améliore les paramètres en regardant un seul échantillon d'entraînement.

Cette étape unique améliore la vitesse du processus de recherche du minimum global du problème d'optimisation. C'est ce qui différencie la SGD de la GD.

### 5.4 SGD avec Momentum

Lorsque la fonction d'erreur est complexe et non convexe, au lieu de trouver l'optimum global, l'algorithme SGD se déplace par erreur dans la direction de nombreux minima locaux. Cela entraîne un temps de calcul plus élevé.

Afin de résoudre ce problème et d'améliorer davantage l'algorithme SGD, diverses méthodes ont été introduites. Une méthode populaire pour échapper à un minimum local et se déplacer dans la direction d'un minimum global est le **SGD avec Momentum**.

L'objectif de la méthode SGD avec momentum est d'accélérer les vecteurs de gradient dans la direction du minimum global, ce qui entraîne une convergence plus rapide.

L'idée derrière le momentum est que les paramètres du modèle sont appris en utilisant les directions et les valeurs des ajustements précédents des paramètres. De plus, les valeurs d'ajustement sont calculées de telle manière que les ajustements les plus récents soient pondérés plus lourdement (ils obtiennent des poids plus grands) par rapport aux ajustements très précoces (ils obtiennent des poids plus petits).

La raison de cette différence est que, avec la méthode SGD, nous ne déterminons pas la dérivée exacte de la fonction de perte, mais nous l'estimons sur un petit lot. Puisque le gradient est bruyant, il est probable qu'il ne se déplacera pas toujours dans la direction optimale.

Le momentum aide alors à estimer ces dérivées plus précisément, ce qui entraîne de meilleurs choix de direction lors du déplacement vers le minimum global.

Une autre raison de la différence de performance entre le SGD classique et le SGD avec momentum réside dans la zone appelée Courbure Pathologique, également appelée la **zone de ravin**.

La Courbure Pathologique ou la Zone de Ravin peut être représentée par le graphique suivant. La ligne orange représente le chemin pris par la méthode basée sur le gradient tandis que la ligne bleu foncé représente le chemin idéal vers la direction de fin de l'optimum global.

![Image](https://miro.medium.com/v2/resize:fit:1044/1*kJS9IPV1DcZWkQ4b8QEB8w.png align="left")

*Source de l'Image : L'auteur*

Pour visualiser la différence entre le SGD et le SGD Momentum, regardons la figure suivante.

![Image](https://miro.medium.com/v2/resize:fit:1400/1*aM92FlJ8zn1-ao6Z6ynzEg.png align="left")

*Source de l'Image : L'auteur*

À gauche se trouve la méthode SGD sans Momentum. À droite se trouve le SGD avec Momentum. Le motif orange représente le chemin du gradient dans une recherche du minimum global.

L'idée derrière le momentum est que les paramètres du modèle sont appris en utilisant les directions et les valeurs des ajustements précédents des paramètres. De plus, les valeurs d'ajustement sont calculées de telle manière que les ajustements les plus récents soient pondérés plus lourdement (ils obtiennent des poids plus grands) par rapport aux ajustements très précoces (ils obtiennent des poids plus petits).

### 5.5 Optimiseur Adam

Une autre technique populaire pour améliorer la procédure d'optimisation SGD est l'**Estimation Adaptative du Moment (Adam)** introduite par Kingma et Ba (2015). Adam est la version étendue de la méthode SGD avec momentum.

La principale différence par rapport au SGD avec momentum, qui utilise un seul taux d'apprentissage pour toutes les mises à jour des paramètres, est que l'algorithme Adam définit différents taux d'apprentissage pour différents paramètres.

L'algorithme calcule les taux d'apprentissage adaptatifs individuels pour chaque paramètre en fonction des estimations des deux premiers moments des gradients (première et deuxième dérivée de la fonction de perte).

Ainsi, chaque paramètre a un taux d'apprentissage unique, qui est mis à jour en utilisant la moyenne décroissante exponentielle des premiers moments (la moyenne) et des seconds moments (la variance) des gradients.

## Points Clés à Retenir & La Suite

Dans ce manuel, nous avons couvert l'essentiel et au-delà en matière de machine learning. Des bases aux techniques avancées, nous avons déballé les algorithmes ML populaires utilisés dans le monde entier dans le domaine de la technologie et les méthodes d'optimisation clés qui les alimentent.

Tout en apprenant chaque concept, nous avons vu quelques exemples pratiques et du code Python, en veillant à ce que vous ne compreniez pas seulement la théorie mais aussi son application.

Votre parcours en Machine Learning est en cours, et ce guide est votre référence. Ce n'est pas une lecture ponctuelle - c'est une ressource à consulter à nouveau à mesure que vous progressez et vous épanouissez dans ce domaine. Avec ces connaissances, vous êtes prêt à relever la plupart des défis ML du monde réel avec confiance à un niveau élevé. Mais ce n'est que le début.

## À Propos de l'Auteur — C'est Moi !

Je suis **Tatev**, Chercheur Senior en Machine Learning et IA. J'ai eu le privilège de travailler dans le domaine de la Science des Données dans de nombreux pays, y compris les États-Unis, le Royaume-Uni, le Canada et les Pays-Bas.

Avec un MSc et un BSc en Économétrie à mon actif, mon parcours dans le domaine du Machine Learning et de l'IA a été tout simplement incroyable. En m'appuyant sur mes études techniques pendant mon Bachelor et mon Master, ainsi que sur plus de 5 ans d'expérience pratique dans l'industrie de la Science des Données, dans le Machine Learning et l'IA, j'ai rassemblé ce résumé de haut niveau des sujets de ML pour le partager avec vous.

## Comment Pouvez-Vous Approfondir ?

Après avoir étudié ce guide, si vous êtes désireux d'approfondir encore et que l'apprentissage structuré est votre style, envisagez de nous rejoindre chez [LunarTech](https://lunartech.ai). Suivez le cours "[Fondamentaux du Machine Learning](https://lunartech.ai/fundamentals-of-machine-learning/)", un programme complet qui offre une compréhension approfondie de la théorie, une mise en œuvre pratique, un matériel d'entraînement extensif et une préparation d'entretien sur mesure pour vous préparer au succès à votre propre rythme.

Ce cours fait également partie de [The Ultimate Data Science Bootcamp](https://lunartech.ai/course-overview/) qui a obtenu la reconnaissance d'être l'un des [Meilleurs Bootcamps de Data Science de 2023](https://www.itpro.com/business-strategy/careers-training/358100/best-data-science-boot-camps), et a été présenté dans des publications prestigieuses comme [Forbes](https://www.forbes.com.au/brand-voice/uncategorized/not-just-for-tech-giants-heres-how-lunartech-revolutionizes-data-science-and-ai-learning/), [Yahoo](https://finance.yahoo.com/news/lunartech-launches-game-changing-data-115200373.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAM3JyjdXmhpYs1lerU37d64maNoXftMA6BYjYC1lJM8nVa_8ZwTzh43oyA6Iz0DfqLtjVHnknO0Zb8QTLIiHuwKzQZoodeM85hkI39fta3SX8qauBUsNw97AeiBDR09BUDAkeVQh6eyvmNLAGblVj3GSf1iCo81bwHQxknmhgng#), [Entrepreneur](https://www.entrepreneur.com/ka/business-news/outpacing-competition-how-lunartech-is-redefining-the/463038) et plus encore. C'est votre chance de faire partie d'une communauté qui prospère grâce à l'innovation et au savoir. Vous pouvez [vous inscrire pour un Essai Gratuit du Bootcamp Ultime de Data Science chez LunarTech](https://courses.lunartech.ai/enroll/2519456?price_id=3321299).

%[https://www.forbes.com.au/brand-voice/uncategorized/not-just-for-tech-giants-heres-how-lunartech-revolutionizes-data-science-and-ai-learning/] 

%[https://www.entrepreneur.com/ka/business-news/outpacing-competition-how-lunartech-is-redefining-the/463038] 

%[https://finance.yahoo.com/news/lunartech-launches-game-changing-data-115200373.html] 

## Connectez-vous avec Moi :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-23-at-6.59.27-PM.png align="left")

*Source de l'Image :* [*LunarTech*](https://lunartech.ai)

* [Suivez-moi sur LinkedIn pour une tonne de Ressources Gratuites en ML et IA](https://www.linkedin.com/in/tatev-karen-aslanyan/)

* [Visitez mon Site Web Personnel](https://tatevaslanyan.com/)

* Abonnez-vous à ma [Newsletter sur la Science des Données et l'IA](https://tatevaslanyan.substack.com/)

%[https://tatevaslanyan.substack.com] 

Vous voulez découvrir tout sur une carrière en Science des Données, Machine Learning et IA, et apprendre comment obtenir un emploi en Data Science ? Téléchargez ce [**Manuel de Carrière en Data Science et IA GRATUIT**](https://downloads.tatevaslanyan.com/six-figure-data-science-ebook)

Merci d'avoir choisi ce guide comme compagnon d'apprentissage. Alors que vous continuez à explorer le vaste domaine du machine learning, j'espère que vous le faites avec confiance, précision et un esprit innovant. Meilleurs vœux dans toutes vos futures entreprises !