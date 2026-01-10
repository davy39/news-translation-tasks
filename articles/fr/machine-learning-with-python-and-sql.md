---
title: Comment effectuer des tâches de machine learning avec Python et SQL
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-09T17:57:45.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-with-python-and-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/just.JPG
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment effectuer des tâches de machine learning avec Python et SQL
seo_desc: 'Machine learning has become a popular field in recent years, with various
  applications in data analysis, computer vision, natural language processing, and
  more.

  Python is one of the most widely used programming languages for machine learning,
  thanks ...'
---

Le machine learning est devenu un domaine populaire ces dernières années, avec diverses applications dans l'analyse de données, la vision par ordinateur, le traitement du langage naturel, et plus encore.

Python est l'un des langages de programmation les plus utilisés pour le machine learning, grâce à son riche écosystème de bibliothèques, de frameworks et d'outils.

Mais pour construire un système de machine learning, vous devez avoir accès à des données. La plupart des données sont stockées dans des bases de données, en particulier les bases de données SQL, utilisées par les entreprises et les organisations pour stocker et gérer des données.

Dans cet article, nous allons explorer comment effectuer du machine learning avec Python et SQL.

## Comment se connecter à une base de données SQL avec Python

Pour effectuer du machine learning avec des données stockées dans une base de données SQL, la première étape consiste à se connecter à la base de données en utilisant Python.

Nous allons utiliser la bibliothèque PyMySQL, qui est un client MySQL en Python pur qui vous permet de vous connecter à un serveur de base de données MySQL et d'exécuter des requêtes SQL.

Voici un exemple de comment se connecter à une base de données MySQL en utilisant PyMySQL :

```python
import pymysql

# Connexion à la base de données
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Création d'un objet curseur
cursor = connection.cursor()

# Exécution d'une requête SQL
query = "SELECT * FROM table_name"
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchall()

# Fermeture du curseur et de la connexion
cursor.close()
connection.close()
```

Ce code se connecte à une base de données MySQL en cours d'exécution sur le localhost et sélectionne toutes les lignes d'une table nommée `table_name`. Le résultat est ensuite récupéré et stocké dans la variable result.

## Comment utiliser Python pour le machine learning avec des données SQL

Une fois que nous nous sommes connectés à la base de données SQL, nous pouvons utiliser des bibliothèques Python comme Pandas pour lire les données dans un DataFrame Pandas.

Un DataFrame est une structure de données bidimensionnelle étiquetée avec des colonnes de types potentiellement différents. C'est comme une feuille de calcul ou une table SQL.

Voici un exemple de comment utiliser Pandas pour lire des données à partir d'une base de données SQL :

```python
import pandas as pd
import pymysql

# Connexion à la base de données
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Lecture des données dans un DataFrame Pandas
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Fermeture de la connexion
connection.close()
```

Ce code utilise Pandas pour lire toutes les données de la table `table_name` dans la base de données `database_name` et les stocke dans un DataFrame Pandas nommé df. Nous fermons ensuite la connexion à la base de données.

Avec les données dans un DataFrame Pandas, nous pouvons utiliser des bibliothèques Python comme Scikit-learn pour effectuer diverses tâches de machine learning.

Scikit-learn est une bibliothèque populaire de machine learning qui fournit différents algorithmes pour la classification, la régression, le clustering, et plus encore.

Voici un exemple de comment utiliser Scikit-learn pour effectuer une régression logistique sur les données :

```python
import pandas as pd
import pymysql
from sklearn.linear_model import LogisticRegression

# Connexion à la base de données
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Lecture des données dans un DataFrame Pandas
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Préparation des données
X = df[['feature_1', 'feature_2']]
y = df['target']

# Création d'un modèle de régression logistique
model = LogisticRegression()

# Entraînement du modèle
model.fit(X, y)

# Fermeture de la connexion
connection.close()
```

Ce code utilise Pandas pour lire les données de la table `table_name` dans la base de données `database_name` et les stocke dans un DataFrame Pandas nommé df.

Nous préparons ensuite les données en sélectionnant deux caractéristiques (`feature_1` et `feature_2`) et la variable cible (y) à partir du DataFrame.

Enfin, nous créons un modèle de régression logistique en utilisant la classe `LogisticRegression` de Scikit-learn et nous entraînons le modèle en utilisant la méthode `fit()`.

Nous pouvons également utiliser Scikit-learn pour diviser les données en ensembles d'entraînement et de test, ainsi que pour évaluer les performances du modèle. Voici un exemple de comment diviser les données et évaluer le modèle :

```python
import pandas as pd
import pymysql
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Connexion à la base de données
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Lecture des données dans un DataFrame Pandas
df = pd.read_sql('SELECT * FROM table_name', con=connection)

# Préparation des données
X = df[['feature_1', 'feature_2']]
y = df['target']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Création d'un modèle de régression logistique
model = LogisticRegression()

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision : {accuracy}")

# Fermeture de la connexion
connection.close()
```

Ce code utilise la méthode `train_test_split()` de Scikit-learn pour diviser les données en ensembles d'entraînement et de test.

Nous créons ensuite un modèle de régression logistique, nous l'entraîons en utilisant la méthode `fit()` sur les données d'entraînement, nous faisons des prédictions sur l'ensemble de test en utilisant la méthode `predict()`, et nous évaluons les performances du modèle en utilisant la méthode `accuracy_score()`.

## Conclusion

Dans cet article, nous avons exploré comment effectuer du machine learning avec Python et SQL.

Nous nous sommes d'abord connectés à une base de données SQL en utilisant PyMySQL, puis nous avons utilisé Pandas pour lire les données dans un DataFrame Pandas. Nous avons ensuite utilisé Scikit-learn pour effectuer une régression logistique sur les données, ainsi que pour diviser les données en ensembles d'entraînement et de test et évaluer les performances du modèle.

Avec ces outils, vous pouvez effectuer des tâches puissantes de machine learning sur des données stockées dans des bases de données SQL.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).