---
title: Qu'est-ce que le surapprentissage en apprentissage automatique ?
subtitle: ''
author: Mene-Ejegi Ogbemi
co_authors: []
series: null
date: '2023-10-16T20:21:22.000Z'
originalURL: https://freecodecamp.org/news/what-is-overfitting-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Banner
seo_title: Qu'est-ce que le surapprentissage en apprentissage automatique ?
---

Tech-writing---Overfitting.jpg
tags:
- name: Intelligence Artificielle
  slug: intelligence-artificielle
- name: Apprentissage Automatique
  slug: apprentissage-automatique
- name: Surapprentissage
  slug: surapprentissage
seo_title: null
seo_desc: "Avez-vous déjà effectué une tâche sans vraiment réfléchir au processus impliqué ? Par exemple, faire du café, attacher vos chaussures ou marcher dans votre quartier. Dans ces types d'activités, vous avez fait ces choses si souvent que vous les avez maîtrisées. Vous pouvez penser à quelque chose d'autre, mais vous effectuez ces activités de la même manière. Ce phénomène est appelé mémoire procédurale en psychologie. Nous avons ce genre de chose avec les modèles d'apprentissage automatique également, mais ce n'est pas aussi positif que chez les humains. Cela est connu sous le nom de surapprentissage en apprentissage automatique."
---

Avez-vous déjà effectué une tâche sans vraiment réfléchir au processus impliqué ? Par exemple, faire du café, attacher vos chaussures ou marcher dans votre quartier. 

Dans ces types d'activités, vous avez fait ces choses si souvent que vous avez maîtrisé le processus. Vous pouvez penser à quelque chose d'autre, mais vous effectuez ces activités de la même manière. Ce phénomène est appelé mémoire procédurale en psychologie.

Nous avons ce genre de chose avec les modèles d'apprentissage automatique également, mais ce n'est pas aussi positif que chez les humains. Cela est connu sous le nom de surapprentissage en apprentissage automatique. 

## Qu'est-ce que le surapprentissage ?

Dans le surapprentissage, un modèle devient si bon avec nos données d'entraînement qu'il a maîtrisé chaque motif, y compris le bruit. Cela fait que le modèle performe bien avec les données d'entraînement mais mal avec les données de test ou de validation.

L'illustration ci-dessous montre comment un modèle optimal s'adapte aux données par rapport au surapprentissage. 

Dans le graphique, nous avons nos caractéristiques sur l'axe des x. Dans les ensembles de données, les caractéristiques sont des données qui peuvent être utilisées pour prédire un résultat. La variable de sortie est le résultat basé sur ces caractéristiques. Les points bleus représentent les points de données où les caractéristiques déterminent les variables de sortie. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/overfitting-illustration.jpg)

Dans le graphique optimal, notre modèle essaie de trouver la tendance généralisée. Mais dans notre graphique surapprenti, le modèle essaie de maîtriser chaque point de données, résultant en une courbe asymétrique.

Un exemple d'étude de cas serait de prédire si un client serait en défaut de paiement sur un prêt bancaire. En supposant que nous avons un ensemble de données de 100 000 clients contenant des caractéristiques telles que les données démographiques, le revenu, le montant du prêt, l'historique de crédit, le dossier d'emploi et le statut de défaut, nous divisons nos données en données d'entraînement et de test. 

Notre ensemble de données d'entraînement contient 80 000 clients, tandis que notre ensemble de données de test contient 20 000 clients. Dans l'ensemble de données d'entraînement, nous observons que notre modèle a une précision de 97 %, mais en prédiction, nous n'obtenons qu'une précision de 50 %. Cela montre que nous avons un problème de surapprentissage.

Pouvez-vous dire pourquoi le surapprentissage est un problème ? Oui ! Il produit une prédiction incorrecte. C'est le but des modèles d'apprentissage automatique de faire des prédictions pour aider à la prise de décision commerciale. Nous perdons du temps et des ressources lorsque notre modèle fait des prédictions incorrectes. 

Imaginez prédire qu'un client remboursera un prêt, et le client fait défaut. Non pas un seul client, mais des milliers de clients. Cela peut causer une crise pour toute institution financière.

## Causes du surapprentissage

### Données bruyantes

Le bruit dans les données apparaît souvent comme des erreurs, des fluctuations ou des valeurs aberrantes dans les données. Cela peut être causé par des erreurs de saisie de données, le vieillissement des données, des erreurs de transmission de données, etc. 

Trop de bruit dans les données peut amener le modèle à penser que ce sont des points de données valides. L'ajustement du motif de bruit dans l'ensemble de données d'entraînement entraînera de mauvaises performances sur le nouvel ensemble de données.  
  
Par exemple, supposons que nous construisons un modèle d'apprentissage automatique pour classer des images de chats et de chiens. Mais certaines des images dans l'ensemble de données sont floues ou mal éclairées. Bien que le modèle puisse bien performer sur les données d'entraînement, il pourrait avoir du mal sur les données de test puisqu'il doit avoir maîtrisé un certain motif avec les images floues dans l'ensemble de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Cat-and-dog-3.jpg)

Sur la photo ci-dessus, vous pouvez voir que nous avons certaines images floues qui ne peuvent pas être étiquetées si ce sont des chats ou des chiens. Dans ces cas, le modèle pourrait également apprendre ces motifs parallèlement aux caractéristiques pertinentes. Supprimer ces images peut réduire le surapprentissage.

### Données d'entraînement insuffisantes

Il y aura moins de motifs et de bruits à analyser si nous n'avons pas suffisamment de données d'entraînement. Cela signifie que la machine ne peut apprendre que peu de choses sur nos données. 

En utilisant notre exemple précédent, si nos données d'entraînement contiennent moins d'images de chiens mais beaucoup plus de chats, le modèle apprend tellement sur les chats que lorsque nous alimentons le système avec une image de chien, il donnera probablement une sortie incorrecte.

### Modèle trop complexe

Dans un modèle complexe, il y a de nombreux paramètres capables de capturer des motifs et des relations dans les données d'entraînement. En conséquence, notre modèle fait une prédiction plus précise. 

Mais cela peut poser un problème, puisque le modèle peut commencer à capturer du bruit, des fluctuations ou des valeurs aberrantes. Regardons un modèle d'arbre de décision, comment il fonctionne et comment le surapprentissage peut se produire lorsqu'il devient trop complexe.

Un modèle d'arbre de décision fonctionne en décomposant répétitivement les données en caractéristiques significatives, faisant de chaque point un nœud. Cela crée une structure en forme d'arbre. 

Pour faire une prédiction, il commence à partir du nœud racine et suit les branches vers le bas, décomposant et ajustant chaque caractéristique jusqu'à ce qu'il atteigne le nœud feuille. La prédiction est ensuite faite sur la base de la valeur associée au nœud feuille.

Regardons un diagramme d'arbre simple de la façon dont un arbre de décision peut prédire si un client est susceptible de faire défaut sur un prêt basé sur certaines caractéristiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/decision-tree-flowchart.png)
_Diagramme d'arbre montrant si un client est susceptible de faire défaut sur un prêt_

Ce modèle commence par créer un nœud parent qui est le score de crédit. Selon que le score de crédit du demandeur est élevé ou faible, il descend au nœud suivant, qui est soit le ratio dette/revenu soit le statut d'emploi. Ensuite, il fait la prédiction finale quant à savoir si le client est susceptible de faire défaut ou non.

Un arbre de décision peut devenir trop complexe lorsqu'il crée trop de nœuds, le rendant trop détaillé ou spécifique aux données d'entraînement. 

Regardons un exemple de programme d'apprentissage automatique qui prédit si un client fera défaut sur un prêt ou non en utilisant un modèle d'arbre de décision. Pour être spécifique, je ne montrerai pas le processus de nettoyage et de visualisation. Je vais simplement insister sur les fonctions requises et comment le surapprentissage peut se produire avec un modèle d'arbre de décision. 

Le lien vers le dépôt complet contenant le nettoyage et la visualisation peut être trouvé [ici](https://github.com/ogbemi-ejegi/Overfitting), et vous pouvez obtenir l'ensemble de données [ici](https://www.kaggle.com/datasets/rishikeshkonapure/home-loan-approval?select=loan_sanction_train.csv).

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

%matplotlib inline

#Importation de nos bibliothèques
train = pd.read_csv('/content/train.csv')
test = pd.read_csv('/content/test.csv')

#Combiner les données d'entraînement et de test
df = pd.concat([train, test], axis=0)
df.head()

#Visualiser l'ensemble de données
train.head()

# Copier les caractéristiques requises dans une variable df_
df_ = train[['Gender',
'Married',
'Education',
'Self_Employed',
'Dependents',
'ApplicantIncome',
'CoapplicantIncome',
'LoanAmount',
'Loan_Amount_Term',
'Property_Area',
'Credit_History']]

### Dupliquer une copie de df dans X
X = df_.copy()

### Encodage des étiquettes pour Y
y = train['Loan_Status'].map({'N':0,'Y':1}).astype(int)

### Division entraînement-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement
clf = DecisionTreeClassifier() #changer le modèle ici
clf.fit(X_train, y_train)

# Prédiction
predictions_clf = clf.predict(X_test)

#Imprimer la précision
print('Précision du modèle:', accuracy_score(predictions_clf, y_test))
```

Pour mieux comprendre cela, je vais expliquer ce que fait chaque module :

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
```

Le premier bloc est la section d'importation. C'est ici que nous importons toutes nos dépendances. 

* Numpy est une bibliothèque Python utilisée pour le calcul scientifique. 
* Pandas est une bibliothèque pour l'analyse et la manipulation de données. 
* Matplotlib et Seaborn sont pour la visualisation de données statistiques. 
* `Accuracy_score` est une fonction pour calculer la précision de notre modèle.
* `train_test_split` est utilisé pour diviser notre ensemble de données en données d'entraînement et de test. 
* Le `LabelEncoder` encode les variables catégorielles en variables numériques. 
* `tree` est pour construire un classificateur d'arbre de décision. 
* `metrics` nous aide à évaluer nos modèles.

```python
#Importation de notre ensemble de données
train = pd.read_csv('/content/train.csv')
test = pd.read_csv('/content/test.csv')
```

Ce module importe nos ensembles de données. Nos ensembles de données d'entraînement et de test ont été téléchargés depuis le dépôt public, nous les importons donc séparément.

```python
#Combiner les données d'entraînement et de test
df = pd.concat([train, test], axis=0)
df.head()

```

Pour travailler avec les deux ensembles de données, nous devons les combiner en un seul ensemble de données. La fonction concat combine les deux ensembles de données. Nous utilisons `df.head()` pour visualiser l'ensemble de données qui est montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-76.png)
_Capture d'écran de notre ensemble de données_

```python
# Copier les caractéristiques requises dans une variable df_
df_ = train[['Gender',
'Married',
'Education',
'Self_Employed',
'Dependents',
'ApplicantIncome',
'CoapplicantIncome',
'LoanAmount',
'Loan_Amount_Term',
'Property_Area',
'Credit_History']]

### Dupliquer une copie de df dans X
X = df_.copy()
```

Pour commencer à travailler avec nos caractéristiques, nous avons créé une variable df_ pour stocker toutes les caractéristiques nécessaires à la prédiction. Nous avons dupliqué cela dans la variable X pour créer une copie avec laquelle travailler.

```python
### Encodage des étiquettes pour Y
y = train['Loan_Status'].map({'N':0,'Y':1}).astype(int)
```

Pour travailler avec notre variable de résultat, nous avons dû la convertir d'une valeur catégorielle en une valeur entière. Cela la rend également plus facile à comprendre pour notre modèle. Toutes les valeurs de N ont été converties en 0, tandis que Y a été converti en 1.

```python
### Division entraînement-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Nous utilisons notre `train_test_split` pour diviser nos données en données d'entraînement et de test. Le `test_size = 0.2` signifie que nous utilisons 20 % des données pour les tests et 80 % pour l'entraînement.

```python
# Entraînement
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
```

Nous avons assigné `DecisionTreeClassifier()` à la variable `clf`, que nous utiliserons pour entraîner et ajuster nos données. `DecisionTreeClassifier()` a un argument optionnel nommé `max_depth`. Le nombre assigné à `max_depth` détermine la profondeur de l'arbre. C'est ainsi que nous l'utiliserons pour causer le surapprentissage dans une autre section ci-dessous.

```python
# Prédiction
predictions_clf = clf.predict(X_test)

```

Dans l'extrait de code ci-dessus, `clf.predict` est utilisé pour prédire les données dans `X_test`. 

```python
print('Précision du modèle:', accuracy_score(predictions_clf, y_test))
```

La précision du modèle a été imprimée en utilisant la fonction accuracy_score, que vous pouvez voir dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-77.png)
_Précision du modèle - presque 70%_

Maintenant que nous avons vu comment fonctionne un arbre de décision et même exécuté un modèle d'apprentissage automatique pour prédire si un client fera défaut ou non, voyons comment causer et diagnostiquer le surapprentissage en modifiant le code en utilisant l'argument `max_depth`.

## Comment diagnostiquer le surapprentissage

### Visualisations

L'utilisation de visualisations peut nous aider à détecter le surapprentissage en fournissant des informations sur le comportement de notre modèle. 

Les méthodes de visualisation courantes incluent le traçage des points de données pour la prédiction du modèle, la visualisation des distributions de caractéristiques ou la création de graphiques des limites de décision. 

Pour visualiser le surapprentissage pour notre demande de prêt ci-dessus, j'ai dû modifier le code en créant une itération utilisant différentes valeurs de `max_depth` allant de 1 à 24. Les prédictions sont calculées sur la base des données d'entraînement et de test et stockées dans une liste.

```python
#Création d'une liste pour stocker les valeurs de précision
train_accuracies = []
test_accuracies = []

#Boucle
for depth in range(1, 25):
  tree_model = DecisionTreeClassifier(max_depth = depth)
  tree_model.fit(X_train, y_train)

  train_predictions = tree_model.predict(X_train)
  test_predictions = tree_model.predict(X_test)

  #calculer la précision d'entraînement et de test
  train_accuracy = metrics.accuracy_score(y_train, train_predictions)

  test_accuracy = metrics.accuracy_score(y_test, test_predictions)

  #Ajouter les précisions
  train_accuracies.append(train_accuracy)
  test_accuracies.append(test_accuracy)
```

La différence ici est que nous créons deux variables - `train_accuracies` et `test_accuracies` - pour stocker les valeurs de précision. En utilisant ces variables, nous pouvons utiliser le code ci-dessous pour générer un graphique qui montre les changements entre ces variables lorsque la valeur de `max_depth` change.

```python
#Création de notre graphique
plt.figure(figsize = (10, 5))
sns.set_style("whitegrid")
plt.plot(train_accuracies, label= "précision d'entraînement")
plt.plot(test_accuracies, label="précision de test")
plt.legend(loc = "upper left")
plt.xticks(range(0, 26, 5))
plt.xlabel("max_depth", size = 20)
plt.ylabel("précision", size = 20)
plt.show()
```

Voici à quoi ressemble le graphique :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/overfitting-visualization-1.png)
_Précision d'entraînement vs précision de test_

Vous remarquerez que lorsque les valeurs de `max_depth` sur l'axe des x commencent à augmenter, la précision des données d'entraînement commence à s'améliorer beaucoup pour atteindre un score parfait. Malgré cela, la précision des données de test a diminué de 0,78 à 0,70. C'est un exemple classique de surapprentissage lorsque le modèle devient trop complexe.

### Écarts de précision entre l'entraînement et la validation

L'écart de précision est un bon moyen de savoir si le surapprentissage s'est produit dans votre programme. Cela signifie qu'il y a un large écart entre les données d'entraînement et les données de validation en ce qui concerne la précision. 

En guise de guide, un écart de 5 % est ce que vous devriez rechercher. Les cas où vous avez plus que cela sont souvent un indicateur de surapprentissage : par exemple, notre visualisation ci-dessus montre que lorsque notre valeur `max_depth` était à 20, notre précision d'entraînement était à 100 % tandis que notre précision de test était à 70 %.

## Comment prévenir le surapprentissage

### Collecter plus de données d'entraînement

Comme discuté ci-dessus, des données d'entraînement insuffisantes peuvent causer le surapprentissage car le modèle ne peut pas capturer les motifs et les intricacies pertinents représentés dans les données. 

L'apprentissage automatique nécessite généralement des milliers ou des millions d'enregistrements dans votre ensemble de données pour l'entraînement. Avec cela, il y aura suffisamment de motifs à capturer. Vous pouvez identifier plus facilement les valeurs aberrantes ou le bruit si vous avez fait un nettoyage approprié de l'ensemble de données en utilisant des techniques pertinentes.

### Utiliser des techniques de régularisation

Les techniques de régularisation impliquent la simplification des modèles en pénalisant les caractéristiques moins influentes. Ces pénalités sont intégrées dans la fonction de perte du modèle.

Les techniques de régularisation pour le modèle d'arbre de décision ci-dessus incluent l'élagage, l'élagage de complexité de coût, et autres.

L'élagage est une technique qui implique la suppression des branches inutiles de l'arbre de décision. Par exemple, nous pouvons définir un nombre minimum de clients sur une feuille, comme 20. Cela empêche l'arbre de prendre des décisions basées sur un très petit groupe de clients.

La complexité de coût implique la suppression des branches de l'arbre en fonction de leur complexité. Cela contrôle le compromis entre la complexité de l'arbre et la précision.

### Ensemblage

L'ensemblage consiste à combiner plusieurs modèles d'apprentissage automatique pour contribuer leurs forces et perspectives uniques afin de faire une prédiction. 

L'ensemblage tire parti de la sagesse de la foule pour faire des prédictions plus précises sur des données invisibles, ce qui améliore la généralisation et réduit le risque de surapprentissage. 

Les méthodes d'ensemblage populaires incluent le bagging, le boosting et le stacking, qui ont été réussis dans une large gamme de tâches d'apprentissage automatique.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ENSEMBLE-1.jpg)
_Diagramme montrant comment fonctionne l'ensemblage_

Le diagramme ci-dessus montre comment la méthode d'ensemblage combine divers modèles d'apprentissage automatique pour faire des prédictions. Chaque modèle est entraîné indépendamment sur son sous-ensemble de données respectif. Les prédictions pour les modèles individuels sont ensuite combinées ou la moyenne est obtenue pour faire une prédiction finale.

## Conclusion

Le surapprentissage se produit lorsqu'un modèle s'adapte trop étroitement aux données d'entraînement, ce qui entraîne de grandes performances d'entraînement mais une mauvaise généralisation. Le surapprentissage peut être problématique car il produit des prédictions incorrectes.

Cela peut être causé par un manque de données d'entraînement, un modèle trop complexe ou des données bruyantes. Le diagnostic implique l'évaluation de l'écart de précision entre l'entraînement et la validation, l'utilisation de visualisations pour scruter le comportement du modèle, et ainsi de suite.

Les stratégies de prévention incluent la collecte de plus de données d'entraînement, l'utilisation de techniques de régularisation et l'emploi de méthodes d'ensemblage. Ces approches garantissent que les modèles généralisent bien et font des prédictions précises pour des décisions éclairées.

Merci d'avoir lu ! Veuillez me suivre sur [LinkedIn](https://www.linkedin.com/in/ogbemi-ejegi/) où je publie également plus de contenu lié aux données.

#### Références:

* Siddhardhan. "Overfitting in Machine Learning | Causes for Overfitting and its Prevention" [Vidéo]. Récupéré de [https://www.youtube.com/watch?v=gy8kXdd6K-o](https://www.youtube.com/watch?v=gy8kXdd6K-o)
* Udacity. "Ensemble Learners" [Vidéo]. Récupéré de [https://www.youtube.com/watch?v=Un9zObFjBH0](https://www.youtube.com/watch?v=Un9zObFjBH0)
* White Board Machine Learning. "Overfitting in Decision Trees" [Vidéo]. Récupéré de [https://www.youtube.com/watch?v=eU4X-dL8nYo](https://www.youtube.com/watch?v=eU4X-dL8nYo)