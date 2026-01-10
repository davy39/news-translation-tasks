---
title: Comment commencer avec le Machine Learning en environ 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-25T18:41:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-machine-learning-in-less-than-10-minutes-b5ea68462d23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5SpR1EAjK1V7P_-V4xUt3w.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment commencer avec le Machine Learning en environ 10 minutes
seo_desc: 'By Tirmidzi Faizal Aflahi

  With the rise of Machine Learning inside industries, the need for a tool that can
  help you iterate through the process quickly has become vital. Python, a rising
  star in Machine Learning technology, is often the first choice...'
---

Par Tirmidzi Faizal Aflahi

Avec l'essor du Machine Learning dans les industries, le besoin d'un outil qui peut vous aider à itérer rapidement à travers le processus est devenu vital. Python, une étoile montante dans la technologie du Machine Learning, est souvent le premier choix pour vous mener au succès. Ainsi, un guide sur le Machine Learning avec Python est vraiment nécessaire.

### Introduction au Machine Learning avec Python

Alors, pourquoi Python ? D'après mon expérience, Python est l'un des langages de programmation les plus faciles à apprendre. Il est nécessaire d'itérer rapidement le processus, et le scientifique des données n'a pas besoin d'avoir une connaissance approfondie du langage, car il peut le maîtriser très rapidement.

**À quel point c'est facile ?**

```
pour tout dans la_liste :    print(tout)
```

**C'est aussi simple que ça**. La syntaxe est étroitement liée à l'anglais (ou à la langue humaine, pas à une machine). Et il n'y a pas d'accolades stupides qui confondent les humains. J'ai une collègue qui travaille dans l'assurance qualité, pas en tant qu'ingénieure logicielle, et elle peut écrire du code Python au niveau production en une journée. (Pour de vrai !)

Ainsi, les créateurs des bibliothèques que nous allons discuter ci-dessous ont choisi Python pour leur langage de choix. Et en tant qu'analyste et scientifique des données, nous pouvons simplement utiliser leurs chefs-d'œuvre pour nous aider à accomplir les tâches. Ce sont les bibliothèques incroyables, **qui sont indispensables pour le Machine Learning avec Python**.

1. **Numpy**

La célèbre bibliothèque d'analyse numérique. Elle vous aidera à faire beaucoup de choses, du calcul de la médiane de la distribution des données, au traitement des tableaux multidimensionnels.

**2. Pandas**

Pour le traitement des fichiers CSV. Bien sûr, vous aurez besoin de traiter quelques tableaux, et de voir des statistiques, et c'est l'outil qu'il vous faut utiliser.

**3. Matplotlib**

Après avoir stocké les données dans des data frames Pandas, vous aurez peut-être besoin de quelques visualisations pour mieux comprendre les données. Les images valent toujours mieux que des milliers de mots.

**4. Seaborn**

C'est aussi un autre outil de visualisation, mais plus axé sur la visualisation statistique. Des choses comme les histogrammes, ou les camemberts, ou les courbes, ou peut-être les tableaux de corrélation.

**5. Scikit-Learn**

C'est le boss final du Machine Learning avec Python. LE SOI-DISANT Machine Learning avec Python, c'est ce gars-là. Scikit-Learn. Tout ce dont vous avez besoin, des algorithmes aux améliorations, se trouve ici.

**6. Tensorflow et Pytorch**

Je ne parle pas trop de ces deux-là. Mais si vous êtes intéressé par le Deep Learning, jetez un coup d'œil, cela en vaudra la peine. (Je donnerai un autre tutoriel sur le Deep Learning la prochaine fois, restez à l'écoute !)

![Image](https://cdn-media-1.freecodecamp.org/images/luQwcUxH4LKtrtAljJES6hInqWrOU5wyyKX6)
_Photo par [Unsplash](https://unsplash.com/photos/D9Zow2REm8U?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Hitesh Choudhary</a> sur <a href="https://unsplash.com/search/photos/machine-learning?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Projets de Machine Learning avec Python

Bien sûr, lire et étudier seul ne vous mènera pas là où vous devez aller. Vous avez besoin de pratique réelle. Comme je l'ai dit sur [mon blog](https://thedatamage.com), apprendre les outils est inutile si vous ne plongez pas dans les données. Et ainsi, je vous présente un endroit où vous pouvez trouver facilement des projets de Machine Learning avec Python.

![Image](https://cdn-media-1.freecodecamp.org/images/KnGl6NoCxZYgBC6ivnzvAV3ZFpXwhUHw96ap)
_Courtoisie de [Kaggle.com](https://www.kaggle.com" rel="noopener" target="_blank" title=")_

[Kaggle](https://www.kaggle.com/) est une plateforme où vous pouvez plonger directement dans les données. Vous résoudrez des projets et deviendrez vraiment bon en Machine Learning. Quelque chose qui pourrait vous intéresser davantage : les compétitions de Machine Learning qu'il organise peuvent offrir un prix allant jusqu'à 100 000 $. Et vous pourriez vouloir tenter votre chance. Haha.

Mais, la chose la plus importante n'est pas l'argent — c'est vraiment un endroit où vous pouvez trouver des projets de Machine Learning avec Python. Il y a beaucoup de projets que vous pouvez essayer. Mais si vous êtes un débutant, et je suppose que vous l'êtes, vous voudrez rejoindre cette compétition.

Voici un exemple de projet que nous utiliserons dans le tutoriel ci-dessous :

#### [Titanic : Machine Learning à partir d'un désastre](https://www.kaggle.com/c/titanic)

Oui, le célèbre Titanic. Une tragédie en 1912, qui a coûté la vie à 1502 personnes sur 2224 passagers et membres d'équipage. Cette compétition Kaggle (ou je peux dire tutoriel) vous donne les vraies données sur la catastrophe. Et votre tâche est d'expliquer les données afin que vous puissiez prédire si une personne a survécu ou non pendant l'incident.

### Tutoriel de Machine Learning avec Python

Avant de plonger profondément dans les données du Titanic, installons quelques outils dont vous avez besoin.

Bien sûr, Python. Vous devez d'abord l'installer depuis le [site officiel de Python](https://www.python.org/downloads/). Vous devez installer la version 3.6+ pour rester à jour avec les bibliothèques.

Après cela, vous devez installer toutes les bibliothèques via Python pip. Pip devrait être installé automatiquement avec la distribution de Python que vous venez de télécharger.

Ensuite, installez les choses dont vous avez besoin via pip. Ouvrez votre terminal, ligne de commande, ou Powershell, et écrivez ce qui suit :

```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
pip install jupyter
```

Tout semble bon. Mais attendez, qu'est-ce que jupyter ? Jupyter signifie Julia, Python, et R, d'où Jupytr. Mais c'est une combinaison étrange de mots, alors ils l'ont changé en Jupyter. C'est un notebook célèbre où vous pouvez écrire du code Python de manière interactive.

Tapez simplement **jupyter notebook** dans votre terminal et vous ouvrirez une page de navigateur comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/JQzvfXZbikTM5TBLawTDltE9EKzHNsekR2uQ)
_Jupyter Notebook_

Écrivez le code à l'intérieur du rectangle vert et vous pouvez écrire et évaluer du code Python de manière interactive.

Maintenant que vous avez installé tous les outils. C'est parti !

#### Exploration des données

La première étape consiste à explorer les données. Vous devez télécharger les données depuis la [page Titanic sur Kaggle](https://www.kaggle.com/c/titanic/data). Ensuite, placez les données extraites dans un dossier où vous démarrez votre Jupyter notebook.

Ensuite, importez les bibliothèques nécessaires :

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```

Ensuite, chargez les données :

```
train_df = pd.read_csv("train.csv")
train_df.head()
```

Vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/U5ygu70dmuZC7kdEPjEOMKQSx9EcZYbzTl4K)

Ce sont nos données. Elles ont les colonnes suivantes :

1. PassengerId, l'identifiant du passager
2. Survived, s'il/elle a survécu ou non
3. Pclass, la classe du service, peut-être 1 est l'économie, 2 est les affaires, et 3 est la première classe
4. Name, le nom du passager
5. Sex
6. Age
7. Sibsp, ou frères et sœurs et conjoints, nombre de frères et sœurs et conjoints à bord
8. Parch, ou parents et enfants, nombre d'entre eux à bord
9. Ticket, détail du ticket
10. Cabin, leur cabine. NaN signifie inconnu
11. Embarked, l'origine de l'embarquement, S pour Southampton, Q pour Queenstown, C pour Cherbourg

Lors de l'exploration des données, nous trouvons souvent des **données manquantes**. Voyons-les :

```
def missingdata(data):
    total = data.isnull().sum().sort_values(ascending=False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending=False)
    ms = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    ms = ms[ms["Percent"] > 0]
    f, ax = plt.subplots(figsize=(8,6))
    plt.xticks(rotation='90')
    fig = sns.barplot(ms.index, ms["Percent"], color="green", alpha=0.8)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Percent of missing values', fontsize=15)
    plt.title('Percent missing data by feature', fontsize=15)
    return ms
```

```
missingdata(train_df)
```

Nous verrons un résultat comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/9VBtHfQEasEQ4TXI5QUedPHd8xhAIa5-bgBN)

Les données de la cabine, de l'âge et de l'embarquement ont certaines valeurs manquantes. Et les informations sur la cabine sont largement manquantes. Nous devons faire quelque chose à ce sujet. C'est ce que nous appelons le nettoyage des données.

#### Nettoyage des données

C'est ce que nous utilisons 90 % du temps. **Nous ferons beaucoup de nettoyage de données pour chaque projet de Machine Learning**. Lorsque les données sont propres, nous pouvons facilement passer à l'étape suivante sans nous soucier de quoi que ce soit.

La technique la plus courante en nettoyage de données est le **remplissage des données manquantes**. Vous pouvez remplir les données manquantes avec le **Mode, la Moyenne ou la Médiane**. Il n'y a pas de règle absolue pour ces choix — vous pouvez essayer de choisir l'un après l'autre et voir les performances. Mais, pour une règle générale, vous ne pouvez utiliser le mode que pour les données catégorisées, et vous pouvez utiliser la médiane ou la moyenne pour les données continues.

Alors remplissons les données d'embarquement avec le Mode et les données d'âge avec la médiane.

```
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)
```

La technique importante suivante **est de simplement supprimer les données**, surtout pour les données largement manquantes. Faisons-le pour les données de la cabine.

```
drop_column = ['Cabin']
train_df.drop(drop_column, axis=1, inplace=True)
```

Maintenant nous pouvons vérifier les données que nous avons nettoyées.

```
print('vérifier la valeur nan dans les données d'entraînement')
print(train_df.isnull().sum())
```

![Image](https://cdn-media-1.freecodecamp.org/images/pQbu6B1TpBT1QF4VesBrLgcQ9X6inFgaLUgA)

Parfait ! Aucune donnée manquante trouvée. Cela signifie que les données ont été nettoyées.

![Image](https://cdn-media-1.freecodecamp.org/images/fTuXRxBBT8Cf5w0ZNdQE9YhFi-DcjCR6q8x6)
_Photo par [Unsplash](https://unsplash.com/photos/BY34glOW7wA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Robert Bye</a> sur <a href="https://unsplash.com/search/photos/engineering?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Ingénierie des caractéristiques

Maintenant que nous avons nettoyé les données. La prochaine chose que nous pouvons faire est l'ingénierie des caractéristiques.

L'ingénierie des caractéristiques est essentiellement une technique pour trouver des caractéristiques ou des données à partir des données actuellement disponibles. Il existe plusieurs façons de faire cette technique. Plus souvent, il s'agit de bon sens.

Jetons un coup d'œil aux données Embarked : elles sont remplies de Q, S ou C. La bibliothèque Python ne pourra pas traiter cela, car elle n'est capable de traiter que des nombres. Vous devez donc faire ce que l'on appelle la **vectorisation One Hot**, en changeant la colonne en trois colonnes. Disons Embarked_Q, Embarked_S et Embarked_C qui sont remplies de 0 ou 1 selon que la personne a embarqué de ce port ou non.

Un autre exemple est SibSp et Parch. Peut-être qu'il n'y a rien d'intéressant dans ces deux colonnes, mais vous pourriez vouloir savoir à quel point la famille du passager qui a embarqué dans le navire était grande. Vous pourriez supposer que si la famille était plus grande, alors les chances de survie augmenteraient, car ils pourraient s'entraider. D'un autre côté, les personnes seules auraient eu du mal.

Vous voulez donc **créer une autre colonne** appelée taille de la famille, qui se compose de sibsp + parch + 1 (le passager lui-même).

Le dernier exemple s'appelle **bin columns**. C'est une technique qui crée des plages de valeurs pour regrouper plusieurs choses ensemble, car vous supposez qu'il est difficile de différencier les choses avec des valeurs similaires. Par exemple, l'âge. Pour une personne âgée de 5 et 6 ans, y a-t-il une différence significative ? ou pour une personne âgée de 45 et 46 ans, y a-t-il une grande différence ?

C'est pourquoi nous créons des colonnes de bin. Peut-être pour l'âge, nous créerons 4 bins. Enfants (0-14 ans), Adolescents (14-20), Adultes (20-40), et Personnes âgées (40+)

Codons-les :

```
all_data = train_df
```

```
for dataset in all_data:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
```

```
import re
# Définir la fonction pour extraire les titres des noms des passagers
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # Si le titre existe, extraire et le retourner.
    if title_search:
        return title_search.group(1)
    return ""
# Créer une nouvelle caractéristique Titre, contenant les titres des noms des passagers
for dataset in all_data:
    dataset['Title'] = dataset['Name'].apply(get_title)
# Grouper tous les titres non courants en un seul groupe "Rare"
for dataset in all_data:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don',                                                  'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
```

```
dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
```

```
for dataset in all_data:
    dataset['Age_bin'] = pd.cut(dataset['Age'], bins=[0,14,20,40,120], labels=['Children','Teenage','Adult','Elder'])
```

```
for dataset in all_data:
    dataset['Fare_bin'] = pd.cut(dataset['Fare'], bins=[0,7.91,14.45,31,120], labels=['Low_fare','median_fare', 'Average_fare','high_fare'])
                                                                                traindf = train_df
for dataset in traindf:
    drop_column = ['Age','Fare','Name','Ticket']
    dataset.drop(drop_column, axis=1, inplace=True)
```

```
drop_column = ['PassengerId']
traindf.drop(drop_column, axis=1, inplace=True)
traindf = pd.get_dummies(traindf, columns=["Sex","Title","Age_bin","Embarked","Fare_bin"],
                             prefix=["Sex","Title","Age_type","Em_type","Fare_type"])
```

Maintenant, vous avez terminé toutes les caractéristiques. Jetons un coup d'œil à la corrélation pour chaque caractéristique :

```
sns.heatmap(traindf.corr(), annot=True, cmap='RdYlGn', linewidths=0.2) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
```

![Image](https://cdn-media-1.freecodecamp.org/images/7ci5SVreDZSM4T9QraMV26lU5jCinXQdt2t8)

**Les corrélations avec une valeur de 1 signifient fortement corrélées positivement, -1 signifie fortement corrélées négativement**. Par exemple, le sexe masculin et le sexe féminin seront corrélés négativement, puisque les passagers devaient s'identifier comme l'un ou l'autre sexe. Autre que cela, vous pouvez voir que rien n'est fortement lié à quoi que ce soit sauf pour ceux créés via l'ingénierie des caractéristiques. Cela signifie que nous sommes prêts à passer à l'étape suivante.

> Que se passera-t-il si quelque chose est fortement corrélé avec autre chose ? Nous pouvons éliminer l'un d'eux puisque ajouter une autre information via une nouvelle colonne ne donnera pas au système de nouvelles informations puisque les deux sont exactement les mêmes.

### Machine Learning avec Python

Nous sommes maintenant arrivés au sommet du tutoriel : la modélisation du Machine Learning.

```
from sklearn.model_selection import train_test_split #pour diviser les données
from sklearn.metrics import accuracy_score  #pour accuracy_score
from sklearn.model_selection import KFold #pour la validation croisée K-fold
from sklearn.model_selection import cross_val_score #évaluation des scores
from sklearn.model_selection import cross_val_predict #prédiction
from sklearn.metrics import confusion_matrix #pour la matrice de confusion
all_features = traindf.drop("Survived",axis=1)
Targeted_feature = traindf["Survived"]
X_train,X_test,y_train,y_test = train_test_split(all_features,Targeted_feature,test_size=0.3,random_state=42)
X_train.shape,X_test.shape,y_train.shape,y_test.shape
```

Vous pouvez choisir de nombreux algorithmes inclus dans la bibliothèque scikit-learn.

1. Régression logistique
2. Forêt aléatoire
3. SVM
4. K Plus proches voisins
5. Naive Bayes
6. Arbres de décision
7. AdaBoost
8. LDA
9. Gradient Boosting

Vous pourriez être submergé en essayant de comprendre ce qu'est quoi. Ne vous inquiétez pas, traitez cela comme une boîte noire : choisissez celui avec la meilleure performance. (Je créerai un article complet sur ces algorithmes plus tard.)

Essayons avec mon préféré : l'**algorithme de forêt aléatoire**

```
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(criterion='gini', n_estimators=700,
                             min_samples_split=10,min_samples_leaf=1,
                             max_features='auto',oob_score=True,
                             random_state=1,n_jobs=-1)
model.fit(X_train,y_train)
prediction_rm=model.predict(X_test)
print('--------------The Accuracy of the model----------------------------')
print('The accuracy of the Random Forest Classifier is', round(accuracy_score(prediction_rm,y_test)*100,2))
kfold = KFold(n_splits=10, random_state=22) # k=10, diviser les données en 10 parties égales
result_rm=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
print('The cross validated score for Random Forest Classifier is:',round(result_rm.mean()*100,2))
y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
plt.title('Confusion_matrix', y=1.05, size=15)
```

![Image](https://cdn-media-1.freecodecamp.org/images/Xi48VWels-HtX65OHrKkYAxjpk810jJb5eMW)

Wow ! Cela nous donne une précision de 83 %. C'est assez bien pour notre première fois.

Le score validé croisé signifie une méthode de validation K Fold. Si K = 10, cela signifie que vous divisez les données en 10 variations et calculez la moyenne de tous les scores comme score final.

### Réglage fin

Vous avez terminé les étapes du Machine Learning avec Python. Mais, il y a une étape supplémentaire qui peut vous apporter de meilleurs résultats : le réglage fin. Le réglage fin signifie trouver les meilleurs paramètres pour les algorithmes de Machine Learning. Si vous regardez le code pour la forêt aléatoire ci-dessus :

```
model = RandomForestClassifier(criterion='gini', n_estimators=700,
                             min_samples_split=10,min_samples_leaf=1,
                             max_features='auto',oob_score=True,
                             random_state=1,n_jobs=-1)
```

Il y a beaucoup de paramètres que vous devez définir. Ce sont les valeurs par défaut, d'ailleurs. Et vous pouvez changer les paramètres comme vous le souhaitez. Mais bien sûr, cela prendra beaucoup de temps.

Ne vous inquiétez pas — il y a un outil appelé **Grid Search**, qui trouve les paramètres optimaux automatiquement. Cela semble génial, n'est-ce pas ?

```
# Paramètres de réglage du classificateur de forêt aléatoire
model = RandomForestClassifier()
n_estim=range(100,1000,100)
```

```
## Grille de recherche pour les paramètres optimaux
param_grid = {"n_estimators" :n_estim}
```

```
model_rf = GridSearchCV(model,param_grid = param_grid, cv=5, scoring="accuracy", n_jobs= 4, verbose = 1)
```

```
model_rf.fit(train_X,train_Y)
```

```
# Meilleur score
print(model_rf.best_score_)
```

```
# Meilleur estimateur
model_rf.best_estimator_
```

Eh bien, vous pouvez l'essayer par vous-même. Et amusez-vous avec le Machine Learning.

### Conclusion

Alors, c'était comment ? Cela ne semble pas très difficile, n'est-ce pas ? Le Machine Learning avec Python est facile. Tout a été préparé pour vous. Vous pouvez simplement faire la magie. Et apporter du bonheur aux gens.

Cet article a été initialement publié sur mon blog à l'adresse [thedatamage.com](https://thedatamage.com/machine-learning-with-python/)