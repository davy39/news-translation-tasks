---
title: Comment déployer un modèle NLP avec FastAPI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-28T20:35:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-an-nlp-model-with-fastapi
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/1_u3IjD13EgKyfby4MD6SAmw.jpeg
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment déployer un modèle NLP avec FastAPI
seo_desc: 'By Davis David

  If you''re working with Natural Language Processing, knowing how to deploy a model
  is one of the most important skills you''ll need to have.

  Model deployment is the process of integrating your model into an existing production
  environmen...'
---

Par Davis David

Si vous travaillez avec le traitement du langage naturel, savoir comment déployer un modèle est l'une des compétences les plus importantes que vous devrez avoir.

Le déploiement de modèle est le processus d'intégration de votre modèle dans un environnement de production existant. Le modèle recevra des entrées et prédira une sortie pour la prise de décision pour un cas d'utilisation spécifique.

> _"Seulement lorsque un modèle est entièrement intégré aux systèmes métiers, nous pouvons extraire une réelle valeur de ses prédictions" — Christopher Samiullah_

Il existe différentes façons de déployer votre modèle [NLP](https://hackernoon.com/your-guide-to-natural-language-processing-nlp-dw8g360f?ref=hackernoon.com) en production, comme utiliser Flask, Django, Bottle ou d'autres frameworks. Mais dans l'article d'aujourd'hui, vous apprendrez comment construire et déployer votre modèle NLP avec **FastAPI**.

Dans cet article, vous apprendrez :

* Comment construire un modèle NLP qui classe les critiques de films IMDB en différents sentiments.
* Qu'est-ce que FastAPI et comment l'installer.
* Comment déployer votre modèle avec FastAPI.
* Comment utiliser votre modèle NLP déployé dans n'importe quelle application Python.

Alors, commençons. 🚀

## Comment construire un modèle NLP

Tout d'abord, nous devons construire notre modèle NLP. Nous allons utiliser le [jeu de données IMDB Movie](https://www.kaggle.com/c/word2vec-nlp-tutorial/data?ref=hackernoon.com) pour construire un modèle simple qui peut classer si une critique de film est positive ou négative. Voici les étapes que vous devez suivre pour cela.

### Importer les packages importants

Tout d'abord, nous devons importer certains packages Python pour charger les données, nettoyer les données, créer un modèle de machine learning (classificateur) et sauvegarder le modèle pour le déploiement.

```python
# importer les modules importants
import numpy as np
import pandas as pd
# modules sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB # classificateur
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    plot_confusion_matrix,
)
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# modules de prétraitement de texte
from string import punctuation
# modules de prétraitement de texte
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re # expression régulière
# Télécharger les dépendances
for dependency in (
    "brown",
    "names",
    "wordnet",
    "averaged_perceptron_tagger",
    "universal_tagset",
):
    nltk.download(dependency)

import warnings
warnings.filterwarnings("ignore")
# initialisation du générateur de nombres aléatoires
np.random.seed(123)
```

Charger le jeu de données depuis le dossier de données :

```python
# charger les données
data = pd.read_csv("../data/labeledTrainData.tsv", sep='\t')
```

Puis afficher un échantillon du jeu de données :

```python
# afficher les cinq premières lignes des données
data.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_esD8-cAwTmwoXXFY.jpeg)

Notre jeu de données a 3 colonnes :

* **Id** — Il s'agit de l'identifiant de la critique
* **Sentiment** — soit positif (1) ou négatif (0)
* **Review** — commentaire sur le film

Ensuite, vérifions la forme du jeu de données :

```python
# vérifier la forme des données
data.shape
```

(25000, 3)

Le jeu de données contient 25 000 critiques.

Maintenant, nous devons vérifier si le jeu de données contient des valeurs manquantes :

```python
# vérifier les valeurs manquantes dans les données
data.isnull().sum()
```

id 0  
sentiment 0  
review 0  
dtype: int64

La sortie montre que notre jeu de données ne contient aucune valeur manquante.

### Comment évaluer la distribution des classes

Nous pouvons utiliser la méthode **`value_counts()`** du package Pandas pour évaluer la distribution des classes de notre jeu de données.

```python
# évaluer la distribution des sentiments des nouvelles
data.sentiment.value_counts()
```

1 12500  
0 12500  
Name: sentiment, dtype: int64

Dans ce jeu de données, nous avons un nombre égal de critiques positives et négatives.

### Comment traiter les données

Après avoir analysé le jeu de données, l'étape suivante consiste à prétraiter le jeu de données dans le bon format avant de créer notre modèle de machine learning.

Les critiques de ce jeu de données contiennent beaucoup de mots et de caractères inutiles dont nous n'avons pas besoin lors de la création d'un modèle de machine learning.

Nous allons nettoyer les messages en supprimant les stopwords, les nombres et la ponctuation. Ensuite, nous convertirons chaque mot en sa forme de base en utilisant le processus de lemmatisation dans le package NLTK.

La fonction `text_cleaning()` gérera toutes les étapes nécessaires pour nettoyer notre jeu de données.

```python
stop_words = stopwords.words('english')
def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Nettoyer le texte, avec l'option de supprimer les stop_words et de lemmatiser les mots
    # Nettoyer le texte
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r'http\S+',' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text) # supprimer les nombres
    
    # Supprimer la ponctuation du texte
    text = ''.join([c for c in text if c not in punctuation])
    
    # Optionnellement, supprimer les stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionnellement, raccourcir les mots à leurs racines
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    
    # Retourner une liste de mots
    return(text)
```

Maintenant, nous pouvons nettoyer notre jeu de données en utilisant la fonction **text_cleaning()** :

```python
# nettoyer la critique
data["cleaned_review"] = data["review"].apply(text_cleaning)
```

Ensuite, diviser les données en variables de fonctionnalités et de cible comme ceci :

```python
# diviser les fonctionnalités et la cible des données
X = data["cleaned_review"]
y = data.sentiment.values
```

Notre fonctionnalité pour l'entraînement est la variable **`cleaned_review`** et la cible est la variable **`sentiment`**.

Nous divisons ensuite notre jeu de données en données d'entraînement et de test. La taille du test est de 15 % de l'ensemble du jeu de données.

```python
# diviser les données en entraînement et validation
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    test_size=0.15,
    random_state=42,
    shuffle=True,
    stratify=y,
)
```

### Comment créer un modèle NLP

Nous allons entraîner l'algorithme Multinomial [Naive Bayes](https://www.freecodecamp.org/news/how-naive-bayes-classifiers-work/) pour classer si une critique est positive ou négative. Il s'agit de l'un des algorithmes les plus courants utilisés pour la classification de texte.

Mais avant d'entraîner le modèle, nous devons transformer nos critiques nettoyées en valeurs numériques afin que le modèle puisse comprendre les données.

Dans ce cas, nous allons utiliser la méthode [**`TfidfVectorizer`**](https://www.freecodecamp.org/news/how-to-extract-keywords-from-text-with-tf-idf-and-pythons-scikit-learn-b2a0f3d7e667/) de scikit-learn. TfidfVectorizer nous aidera à convertir une collection de documents textuels en une matrice de fonctionnalités TF-IDF.

Pour appliquer cette série d'étapes (prétraitement et entraînement), nous allons utiliser une [classe Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html?ref=hackernoon.com) de scikit-learn qui applique séquentiellement une liste de transformations et un estimateur final.

```python
# Créer un classificateur dans un pipeline
sentiment_classifier = Pipeline(steps=[
                               ('pre_processing',TfidfVectorizer(lowercase=False)),
                                 ('naive_bayes',MultinomialNB())
                                 ])
```

Ensuite, nous entraînons notre classificateur comme ceci :

```python
# entraîner le classificateur de sentiment
sentiment_classifier.fit(X_train,y_train)
```

Nous créons ensuite une prédiction à partir de l'ensemble de validation :

```python
# tester les performances du modèle sur les données valides
y_preds = sentiment_classifier.predict(X_valid)
```

Les performances du modèle seront évaluées en utilisant la métrique d'évaluation **`accuracy_score`**. Nous utilisons accuracy_score parce que nous avons un nombre égal de classes dans la variable sentiment.

```python
accuracy_score(y_valid,y_preds)
```

0.8629333333333333

La précision de notre modèle est d'environ **86,29 %**, ce qui est une bonne performance.

### Comment sauvegarder le pipeline du modèle

Nous pouvons sauvegarder le pipeline du modèle dans le répertoire du modèle en utilisant le package Python **`joblib`**.

```python
# sauvegarder le modèle
import joblib
joblib.dump(sentiment_classifier, '../models/sentiment_model_pipeline.pkl')
```

Maintenant que nous avons construit notre modèle NLP, apprenons à utiliser FastAPI.

## Qu'est-ce que FastAPI ?

FastAPI est un framework web Python rapide et moderne pour construire différentes [APIs](https://hackernoon.com/how-to-use-the-requests-python-library-to-make-an-api-call-and-save-it-as-a-pandas-dataframe-z43k33rm?ref=hackernoon.com). Il offre des performances plus élevées, il est plus facile à coder et il est livré avec une documentation automatique et interactive.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-rzu32nl.jpeg)

FastAPI est construit sur deux bibliothèques Python majeures **— Starlette** (pour la gestion web) et **Pydantic** (pour la gestion et la validation des données). FastAPI est très rapide par rapport à Flask car il apporte des gestionnaires de fonctions asynchrones.

Si vous voulez en savoir plus sur FastAPI, je vous recommande de lire cet [article](https://tiangolo.medium.com/introducing-fastapi-fdc1206d453f?ref=hackernoon.com) de Sebastián Ramírez.

Dans cet article, nous allons essayer d'utiliser certaines des fonctionnalités de FastAPI pour servir notre modèle NLP.

### Comment installer FastAPI

Tout d'abord, assurez-vous d'installer la dernière version de FastAPI (avec pip) :

```python
pip install fastapi
```

Vous aurez également besoin d'un serveur ASGI pour la production tel que [uvicorn](http://www.uvicorn.org/?ref=hackernoon.com).

```python
pip install uvicorn
```

## Comment déployer un modèle NLP avec FastAPI

Dans cette section, nous allons déployer notre modèle [NLP](https://www.freecodecamp.org/news/learn-natural-language-processing-no-experience-required/) entraîné en tant qu'API REST avec FastAPI. Nous sauvegarderons le code pour notre API dans un fichier Python appelé **main.py**. Ce fichier sera responsable de l'exécution de notre application FastAPI.

### Importer les packages

La première étape consiste à importer les packages qui nous aideront à construire l'application FastAPI et à exécuter le modèle NLP.

```python
# modules de prétraitement de texte
from string import punctuation
# modules de prétraitement de texte
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re  # expression régulière
import os
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI
```

### Comment initialiser une instance d'application FastAPI

Nous pouvons utiliser le code suivant pour initialiser l'application FastAPI :

```python
app = FastAPI(
    title="API de modèle de sentiment",
    description="Une API simple qui utilise un modèle NLP pour prédire le sentiment des critiques de films",
    version="0.1",
)
```

Comme vous pouvez le voir, nous avons personnalisé la configuration de notre application FastAPI en incluant :

* Le titre de l'API
* La description de l'API.
* La version de l'API.

### Comment charger le modèle NLP

Pour charger le modèle NLP, nous utiliserons la méthode **`joblib.load()`** et ajouterons le chemin vers le répertoire du modèle. Le nom du modèle NLP est **`sentiment_model_pipeline.pkl`** :

```python
# charger le modèle de sentiment
with open(
    join(dirname(realpath(__file__)), "models/sentiment_model_pipeline.pkl"), "rb"
) as f:
    model = joblib.load(f)
```

### Comment définir une fonction pour nettoyer les données

Nous utiliserons la même fonction appelée **`text_cleaning()`** de la Partie 1 qui nettoie les données de critique en supprimant les stopwords, les nombres et la ponctuation. Enfin, nous convertirons chaque mot en sa forme de base en utilisant le processus de lemmatisation dans le [package NLTK](https://www.freecodecamp.org/news/natural-language-processing-tutorial-with-python-nltk/).

```python
def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Nettoyer le texte, avec l'option de supprimer les stop_words et de lemmatiser les mots
    # Nettoyer le texte
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)  # supprimer les nombres
    # Supprimer la ponctuation du texte
    text = "".join([c for c in text if c not in punctuation])
    # Optionnellement, supprimer les stop words
    if remove_stop_words:
        # charger les stopwords
        stop_words = stopwords.words("english")
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    # Optionnellement, raccourcir les mots à leurs racines
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    # Retourner une liste de mots
    return text
```

### Comment créer un point de terminaison de prédiction

L'étape suivante consiste à ajouter notre point de terminaison de prédiction appelé « **/predict-review** » avec la méthode de requête GET.

```python
@app.get("/predict-review")
```

> Un point de terminaison d'API est le point d'entrée dans un canal de communication lorsque deux systèmes interagissent. Il fait référence aux points de contact de la communication entre une API et un serveur.

Ensuite, nous définissons une fonction de prédiction pour ce point de terminaison. Le nom de la fonction est **`predict_sentiment()`** avec un paramètre de critique.

La fonction predict_sentiment() effectuera les tâches suivantes :

* Recevoir la critique de film.
* Nettoyer la critique de film en utilisant la fonction **text_cleaning()**. 
* Faire une prédiction en utilisant notre modèle NLP.
* Sauvegarder le résultat de la prédiction dans la variable **output** (soit 0 soit 1).
* Sauvegarder la probabilité de la prédiction dans la variable **probas** et la formater en 2 décimales.
* Enfin, retourner les résultats de la prédiction et de la probabilité.

```python
@app.get("/predict-review")
def predict_sentiment(review: str):
    """
    Une fonction simple qui reçoit un contenu de critique et prédit le sentiment du contenu.
    :param review:
    :return: prediction, probabilities
    """
    # nettoyer la critique
    cleaned_review = text_cleaning(review)
    
    # effectuer la prédiction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])
    probas = model.predict_proba([cleaned_review])
    output_probability = "{:.2f}".format(float(probas[:, output]))
    
    # dictionnaire de sortie
    sentiments = {0: "Negative", 1: "Positive"}
    
    # montrer les résultats
    result = {"prediction": sentiments[output], "Probability": output_probability}
    return result
```

Voici tous les blocs de code dans le fichier **main.py** :

```python
# modules de prétraitement de texte
from string import punctuation
# modules de prétraitement de texte
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re  # expression régulière
import os
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="API de modèle de sentiment",
    description="Une API simple qui utilise un modèle NLP pour prédire le sentiment des critiques de films",
    version="0.1",
)

# charger le modèle de sentiment
with open(
    join(dirname(realpath(__file__)), "models/sentiment_model_pipeline.pkl"), "rb"
) as f:
    model = joblib.load(f)


# nettoyer les données
def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Nettoyer le texte, avec l'option de supprimer les stop_words et de lemmatiser les mots
    # Nettoyer le texte
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)  # supprimer les nombres
    
    # Supprimer la ponctuation du texte
    text = "".join([c for c in text if c not in punctuation])
    
    # Optionnellement, supprimer les stop words
    if remove_stop_words:
        # charger les stopwords
        stop_words = stopwords.words("english")
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
        
    # Optionnellement, raccourcir les mots à leurs racines
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
        
    # Retourner une liste de mots
    return text

@app.get("/predict-review")
def predict_sentiment(review: str):
    """
    Une fonction simple qui reçoit un contenu de critique et prédit le sentiment du contenu.
    :param review:
    :return: prediction, probabilities
    """
    # nettoyer la critique
    cleaned_review = text_cleaning(review)
    
    # effectuer la prédiction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])
    probas = model.predict_proba([cleaned_review])
    output_probability = "{:.2f}".format(float(probas[:, output]))
    
    # dictionnaire de sortie
    sentiments = {0: "Negative", 1: "Positive"}
    
    # montrer les résultats
    result = {"prediction": sentiments[output], "Probability": output_probability}
    return result
```

### Comment exécuter l'API

La commande suivante nous aidera à exécuter l'application FastAPI que nous avons créée.

```python
uvicorn main:app --reload
```

Voici les paramètres que nous avons définis pour uvicorn pour exécuter notre application FastAPI.

* **main** : le fichier main.py qui contient l'application FastAPI.
* **app** : l'objet créé à l'intérieur de main.py avec la ligne app = FastAPI().
* **—reload** : Permet au serveur de redémarrer automatiquement chaque fois que nous apportons des modifications au code.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_EP-YBqB9hbsOL9Rt.jpeg)

FastAPI fournit une page de documentation interactive automatique. Pour y accéder, naviguez vers [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs) dans votre navigateur et vous verrez la page de documentation créée automatiquement par FastAPI.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_KjAI4upfMAZcUGBR.jpeg)

La page de documentation montre le nom de notre API, la description et sa version. Elle montre également une liste des routes disponibles dans l'API avec lesquelles vous pouvez interagir.

Pour faire une prédiction, cliquez d'abord sur la route « **predict-review** », puis sur le bouton « **Try it out** ». Cela vous permet de remplir le paramètre de critique et d'interagir directement avec l'API.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0__XOHgx7DAjF74r1N.jpeg)

Remplissez le champ de critique en ajoutant une critique de film de votre choix. J'ai ajouté la critique suivante sur le film **Zack Snyder's Justice League** sorti en 2021.

> « J'ai adoré le film du début à la fin. Tout comme Ray Fisher l'a dit, j'espérais que le film ne se termine pas. La scène d'ouverture était époustouflante, j'ai beaucoup aimé cette scène. Contrairement à 'Justice League', le film montre que chaque héros est le meilleur dans son domaine, ce qui nous fait aimer chaque personnage. Merci, Zack et toute l'équipe. »

Ensuite, cliquez sur le bouton d'exécution pour faire une prédiction et obtenir le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_QAM6VjtcDlhgEbQ6.jpeg)

Enfin, le résultat de l'API montre que notre modèle NLP prédit que la critique fournie a un sentiment **Positif** avec une probabilité de **0,70** :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/0_YUFkGlke1PWVoeyo.jpeg)

## Comment utiliser un modèle NLP dans n'importe quelle application Python

Pour utiliser notre API NLP dans n'importe quelle application Python, nous devons installer le package Python requests. Ce package nous aidera à envoyer des requêtes HTTP à l'application FastAPI que nous avons développée.

Pour installer le package requests, exécutez la commande suivante :

```python
pip install requests
```

Ensuite, créez un simple fichier Python appelé **`python_app.py`**. Ce fichier sera responsable de l'envoi de nos requêtes HTTP.

Nous importons d'abord le package requests :

```python
import requests as r
```

Ajoutez une critique de film sur le film **Godzilla vs Kong (2021)** :

```python
# ajouter une critique
review = "Ce film était exactement ce que je voulais dans un film Godzilla vs Kong. Il est grand, bruyant, audacieux et stupide, dans les meilleurs sens possibles. Il a aussi un cœur sous la forme de Jia (Kaylee Hottle) et un Kong super expressif. Les scènes de lui dans le monde creux sont particulièrement percutantes et magnifiquement tournées/animées. Kong est vraiment le cœur émotionnel du film (avec Godzilla plus comme une force indifférente de la nature), et il est si bien fait qu'il pourrait même convertir quelques membres de l'équipe Godzilla."
```

Ensuite, ajoutez la critique dans un paramètre clé à passer à la requête HTTP :

```python
keys = {"review": review}
```

Enfin, nous envoyons une requête à notre API pour faire une prédiction de la critique :

```python
prediction = r.get("http://127.0.0.1:8000/predict-review/", params=keys)
```

Ensuite, nous pouvons voir les résultats de la prédiction :

```python
results = prediction.json()

print(results["prediction"])
print(results["Probability"])
```

Cela affichera la prédiction et sa probabilité. Voici les résultats :

Positive
0.54

## Conclusion

Félicitations 👏👏, vous êtes arrivé à la fin de cet article. J'espère que vous avez appris quelque chose de nouveau et que vous savez maintenant comment déployer votre modèle NLP avec FastAPI.

Si vous voulez en savoir plus sur FastAPI, je vous recommande de suivre ce [cours complet sur FastAPI](https://www.youtube.com/watch?v=7t2alSnE2-I&ref=hackernoon.com) créé par [Bitfumes](https://twitter.com/bitfumes?ref=hackernoon.com).

Vous pouvez télécharger le [code source du projet utilisé dans cet article ici](https://github.com/Davisy/Deploy-NLP-Model-with-FastAPI).

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine dans le prochain article !.

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com)