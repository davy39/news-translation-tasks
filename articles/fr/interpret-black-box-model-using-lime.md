---
title: Comment interpréter les modèles de boîte noire en utilisant LIME (Local Interpretable
  Model-Agnostic Explanations)
subtitle: ''
author: Josua Naiborhu
co_authors: []
series: null
date: '2022-10-17T15:12:31.000Z'
originalURL: https://freecodecamp.org/news/interpret-black-box-model-using-lime
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/LIME.jpeg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Comment interpréter les modèles de boîte noire en utilisant LIME (Local
  Interpretable Model-Agnostic Explanations)
seo_desc: "Machine learning models are black box models. By giving input to these\
  \ models, we can get output based on the particular model we're using. \nThe way\
  \ humans interpret things is different from how machines interpret them. So it's\
  \ helpful to use tools t..."
---

Les modèles d'apprentissage automatique sont des modèles de boîte noire. En donnant une entrée à ces modèles, nous pouvons obtenir une sortie basée sur le modèle particulier que nous utilisons. 

La manière dont les humains interprètent les choses est différente de la manière dont les machines les interprètent. Il est donc utile d'utiliser des outils qui peuvent transformer la sortie de certains modèles d'apprentissage automatique en quelque chose que les humains ou les utilisateurs non techniques peuvent comprendre.

Dans un contexte commercial, l'interprétation du modèle joue un rôle important dans la prise de décisions basées sur les données. Plus nous interprétons bien la sortie, plus il est facile pour les utilisateurs non techniques de comprendre cette sortie.

Dans ce tutoriel, je vais donc expliquer l'un des packages les plus populaires que vous pouvez utiliser pour interpréter le modèle de boîte noire de la sortie – un package appelé LIME (Local Interpretable Model-Agnostic Explanations).

## Qu'est-ce que LIME ?

LIME est un outil d'apprentissage automatique agnostique aux modèles qui vous aide à interpréter vos modèles de ML. Le terme **agnostique aux modèles** signifie que vous pouvez utiliser LIME avec n'importe quel modèle d'apprentissage automatique lors de l'entraînement de vos données et de l'interprétation des résultats. 

LIME utilise des modèles "intrinsèquement interprétables" tels que les arbres de décision, les modèles linéaires et les modèles heuristiques basés sur des règles pour expliquer les résultats aux utilisateurs non techniques sous forme visuelle. Vous pouvez utiliser LIME pour les problèmes de régression et de classification afin d'interpréter vos modèles de boîte noire. 

## Collecte des données

Dans ce tutoriel, nous allons examiner un problème de classification en utilisant le jeu de données Churn. Nous allons classer si les clients continueront à utiliser les produits ou non (taux d'attrition) en examinant certaines caractéristiques du jeu de données. 

Vous pouvez télécharger le jeu de données [telco customers churn dataset ici](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/code). 

## Prétraitement des données

Étant donné que ce tutoriel se concentre sur la mise en œuvre de LIME en tant qu'outil d'interprétabilité, nous allons effectuer quelques étapes de prétraitement pour diverses caractéristiques.

Nous commençons le prétraitement en passant en revue les colonnes qui ne sont pas pertinentes pour le résultat cible (attrition). Vous pouvez supprimer le CustomerID en utilisant ce code :

```py
# Suppression de toutes les colonnes non pertinentes
df.drop(columns=['customerID'], inplace = True)
```

Nous avons également quelques valeurs manquantes qui ne sont pas correctement imputées. Pour simplifier, nous avons simplement supprimé les valeurs manquantes en utilisant ce code :

```py
# Suppression des valeurs manquantes
df.dropna(inplace=True)
```

Une autre étape de prétraitement que nous devons effectuer est d'examiner les colonnes catégorielles. La grande majorité des modèles d'apprentissage automatique ne peuvent pas gérer les caractéristiques catégorielles. Nous devons donc prétraiter ce type de caractéristique en une représentation numérique. 

Il existe diverses transformations que nous pouvons effectuer telles que l'encodage par étiquettes, les astuces de hachage, l'encodage one-hot, l'encodage cible, l'encodage ordinal et l'encodage par fréquence. 

Pour ce tutoriel, nous allons utiliser la technique d'encodage par étiquettes en utilisant la bibliothèque scikit-learn comme montré dans le code suivant :

```py
# Encodage par étiquettes des caractéristiques 
categorical_feat =list(df.select_dtypes(include=["object"]))

# Utilisation de l'encodeur d'étiquettes pour transformer les catégories de chaînes en étiquettes entières
le = LabelEncoder()
for feat in categorical_feat:
    df[feat] = le.fit_transform(df[feat]).astype('int')
```

Il est important de noter que lorsque vous travaillez sur un problème/jeu de données réel de ML, vous voudrez vous assurer de réaliser un prétraitement approprié, un génie des caractéristiques, une validation croisée, un réglage des hyperparamètres, et ainsi de suite pour obtenir une meilleure prédiction.

## Modélisation avec XGBoostClassifier et implémentation de LIME

XGBoostClassifier est un algorithme XGBoost que vous pouvez utiliser pour résoudre des problèmes de classification. Il fonctionne en construisant les données dans un arbre de décision et en utilisant les résidus pour être construits à nouveau dans l'arbre de décision suivant de manière séquentielle.

Cet algorithme vous aide à améliorer les performances des prédictions de votre modèle qui peuvent ressembler à la vérité terrain. Cela est dû au fait qu'il améliore les prédictions mal classées (apprenants faibles) en les aidant à devenir des apprenants forts. Il le fait en apprenant la prédiction mal classée qui est utilisée lors de l'itération suivante de l'arbre de décision suivant. 

Vous pouvez consulter le diagramme suivant pour voir comment cet algorithme fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/xgboost.png)
_Figure 4. Structure simplifiée de XGBoost ([source](https://www.researchgate.net/figure/Simplified-structure-of-XGBoost_fig2_348025909))_

Nous pouvons implémenter LIME après avoir traversé le processus d'entraînement sur nos données d'entraînement. 

Nous commençons le processus d'entraînement en divisant les données en ensembles d'entraînement et de test afin d'éviter le surapprentissage. Nous pouvons utiliser la méthode de division disponible dans scikit-learn comme montré dans le code suivant :

```py
features = df.drop(columns=['Churn'])
labels = df['Churn']
# Division des données en ensemble d'entraînement et de test avec un ratio de division de 80:20
x_train,x_test,y_train,y_test = train_test_split(features,labels,test_size=0.2, random_state=123)
```

Nous sélectionnons les caractéristiques et le résultat cible (**churn**) et divisons les données en données d'entraînement et de test. Ensuite, nous pouvons commencer l'entraînement en ajustant **X_train et y_train** en fonction de l'objet d'instanciation du modèle d'apprentissage automatique que nous utilisons. Nous utilisons XGBoostClassifier pour ce tutoriel.

Nous initialisons n_estimators (nombre d'arbres de décision) et random state pour la simplicité du processus d'entraînement. Dans un projet réel de science des données, il y a de nombreux paramètres que vous voudrez ajuster afin de maximiser la capacité de cet algorithme. Vous pouvez vous référer à [**XGBoost parameters**](https://xgboost.readthedocs.io/en/stable/parameter.html) pour en savoir plus.

```py
model = XGBClassifier(n_estimators = 300, random_state = 123)
model.fit(x_train, y_train)
```

Après avoir ajusté les données par le processus d'entraînement, nous allons travailler sur l'interprétation de l'interprétabilité locale. L'interprétabilité locale implique l'analyse de chaque caractéristique d'une instance de données particulière. Nous pouvons sélectionner une instance/échantillon particulier pour vérifier comment les caractéristiques se corrèlent au résultat cible basé sur un échantillon particulier. 

```py
np.random.seed(123)
predict_fn = lambda x: model.predict_proba(x)
# Définition de l'objet explainer LIME
explainer = lime.lime_tabular.LimeTabularExplainer(df[features.columns].astype(int).values,                                               mode='classification',
class_names=['Did not Churn', 'Churn'],                                                 training_labels=df['Churn'],                                                  feature_names=features.columns)
# utilisation de LIME pour obtenir les explications
i = 5
exp=explainer.explain_instance(df.loc[i,features.columns].astype(int).values, predict_fn, num_features=5)
exp.show_in_notebook(show_table=True)
```

Pour obtenir l'explication pour une instance particulière, nous commençons par définir une fonction comme le score de probabilité qui sera utilisé dans le framework LIME. Nous instancions également l'objet explainer LIME. 

LIME a un attribut lime_tabular qui peut interpréter comment les caractéristiques se corrèlent au résultat cible. Nous pouvons également spécifier le mode en classification, training_label au résultat cible (Churn), et les caractéristiques que nous avons sélectionnées dans le processus d'entraînement. 

Nous choisissons l'échantillon 5 et nous obtiendrons l'explication pour cet échantillon particulier. Nous choisissons également les 5 caractéristiques les plus importantes qui contribuent le plus au résultat cible dans le paramètre num_features. 

Ces caractéristiques sont également appelées importance des caractéristiques. L'importance des caractéristiques est la caractéristique qui vérifie la corrélation entre les caractéristiques d'entrée et les caractéristiques cibles. Plus le score de la caractéristique dans le graphique d'importance des caractéristiques est élevé, plus la caractéristique est importante pour être ajustée dans le modèle d'apprentissage automatique.

## Comment interpréter l'interprétabilité locale

![Image](https://www.freecodecamp.org/news/content/images/2022/10/lime1.png)
_Figure 8. Prédiction d'interprétabilité locale_

L'image ci-dessus montre trois graphiques qui montrent chacun des informations essentielles sur nos clients et leurs taux d'attrition. 

Le graphique de gauche montre que l'échantillon 5 dans les données montre l'intervalle de confiance indiquant que ces données sont à 99% d'attrition alors que seulement 1% indique que l'instance n'a pas abandonné. 

Le graphique central montre les scores d'importance des caractéristiques sur cet échantillon particulier avec **MonthlyCharges** ayant un **score d'importance des caractéristiques de 21%**, suivi de **Contract** avec **19%** et **tenure** avec **11%**. Ces caractéristiques ont du sens en fonction de notre croyance que les clients tendent à abandonner davantage avec **des MonthlyCharges plus élevés.** 

Le graphique de droite montre les cinq principales caractéristiques et leurs valeurs respectives. Les caractéristiques mises en évidence en orange contribuent à la **classe 1 (Churn)** alors que les caractéristiques mises en évidence en bleu contribuent à la **classe 0 (pas de Churn)**. 

Nous pouvons également tracer une autre version du deuxième graphique comme montré dans le graphique à barres suivant. Il montre la plage des prédictions d'interprétabilité locale sur l'échantillon 5 dans lequel les MonthlyCharges pour cet échantillon particulier sont supérieurs à 89, le Contract est inférieur à 0, et les TotalCharges sont supérieurs à 401 et inférieurs à 1397.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/lime2.png)
_Figure 9. La plage des prédictions d'interprétabilité locale_

## Comment interpréter l'interprétabilité globale

LIME fournit également une autre explication via l'algorithme SP-LIME qui prend des échantillons représentatifs pour extraire la perspective globale du modèle de boîte noire. 

Cette technique aide les utilisateurs non techniques à comprendre les données non seulement dans une instance particulière (interprétabilité locale) mais aussi à comprendre les données de manière holistique. En comprenant de nombreux échantillons représentatifs et leurs interprétations, les utilisateurs non techniques peuvent capturer la perspective globale des instances de données. 

```py
# Utilisons SP-LIME pour retourner des explications sur quelques ensembles de données d'échantillons 
# et obtenir une perspective de décision globale non redondante du modèle de boîte noire
sp_exp = submodular_pick.SubmodularPick(explainer, 
                                        df[features.columns].values,
                                        predict_fn, 
                                        num_features=5,
                                        num_exps_desired=5)
```

Nous utilisons les attributs sous-modulaires disponibles sur SP-LIME pour obtenir une perspective globale des instances de données. Ensuite, nous visualisons les données pour visualiser les échantillons représentatifs globaux extraits par l'algorithme SP-LIME en utilisant ce code :

```py
[exp.show_in_notebook() for exp in sp_exp.sp_explanations]
print('Explications SP-LIME.')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/lime3-1.png)
_Figure 12. La plage des prédictions d'interprétabilité globale_

Vous pouvez voir comment SP-LIME construit des valeurs d'intervalle pour chaque **échantillon représentatif.** Par exemple, le premier échantillon représentatif montre que l'intervalle de confiance est de 81% d'attrition alors que 19% indique que les instances n'abandonnent pas. 

Les caractéristiques qui influencent la tendance de cette instance à abandonner sont **MonthlyCharge, Contract, tenure, OnlineSecurity, et TechSupport**. Vous pouvez voir cela dans le graphique à barres d'importance des caractéristiques pour le premier échantillon représentatif. Nous pouvons également tracer une autre version du graphique central de chaque échantillon représentatif sur le graphique précédent en utilisant ce code :

```python
[exp.as_pyplot_figure(label=exp.available_labels()[0]) for exp in sp_exp.sp_explanations]
print('Explications locales SP-LIME')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/lime4-1.png)
_Figure 14. Premier et deuxième échantillons représentatifs_

Sur le deuxième échantillon représentatif de la **figure 12**, l'intervalle de confiance est de 100% pas d'attrition. Les caractéristiques qui influencent la tendance de cette instance à ne pas abandonner sont **Contract, tenure, MonthlyCharge, TotalCharges, et OnlineSecurity** comme montré sur le graphique à barres d'importance des caractéristiques suivant pour le deuxième échantillon représentatif.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/lab4.png)
_Figure 15. Troisième échantillon représentatif_

Sur le troisième échantillon représentatif de la **figure 12**, l'intervalle de confiance est de 100% pas d'attrition. Les caractéristiques qui influencent la tendance de cette instance à ne pas abandonner sont **Contract, OnlineSecurity,** et **OnlineBackup** comme montré sur le graphique d'importance des caractéristiques ci-dessus pour le troisième échantillon représentatif. 

Vous pouvez voir la mise en œuvre de LIME et SP-LIME sur les données [en regardant ce notebook](https://nbviewer.org/github/naiborhujosua/Blog_Notes/blob/main/notebook/interpreting-black-box-models.ipynb).

[Voici un article intéressant](https://arxiv.org/abs/1602.04938) sur la confiance dans les modèles.

# Merci d'avoir lu !

Je l'apprécie vraiment ! 🤗. J'écris sur des sujets liés à l'apprentissage automatique et à l'apprentissage profond. J'essaie de garder mes publications simples mais précises, en fournissant toujours des visualisations et des simulations.