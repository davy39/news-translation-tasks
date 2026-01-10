---
title: Comment déployer votre modèle NLP en production en tant qu'API avec Algorithmia
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-17T21:02:19.000Z'
originalURL: https://freecodecamp.org/news/deploy-ml-model-to-production-as-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/pexels-cottonbro-5053740.jpg
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment déployer votre modèle NLP en production en tant qu'API avec Algorithmia
seo_desc: 'By Davis David

  Did you know that 90% of machine learning models never actually make it into production?

  This means that the topic of machine learning deployment is rarely discussed when
  people learn machine learning. As a result, many AI practitioner...'
---

Par Davis David

Saviez-vous que 90 % des modèles de machine learning ne sont jamais réellement mis en production ?

Cela signifie que le sujet du déploiement du machine learning est rarement discuté lorsque les gens apprennent le machine learning. En conséquence, de nombreux praticiens de l'IA savent comment créer des modèles ML utiles, mais ils trouvent difficile de les déployer en production. 

Il va sans dire que le déploiement du machine learning est l'une des compétences les plus importantes que vous devriez avoir si vous allez travailler avec des modèles ML.

![Image](https://developers.decoded.africa/content/images/2020/10/1_jBjJw7jq71pw4iZkqyp2Uw.jpeg)

Le déploiement de modèle est le processus d'intégration de votre modèle dans un environnement de production existant. Le modèle recevra des entrées et prédira une sortie pour la prise de décision pour un cas d'utilisation spécifique. 

Par exemple, un modèle peut être déployé dans un site de commerce électronique et il peut prédire si un avis sur un produit spécifique est **positif** ou **négatif**.

> Seule lorsque le modèle est entièrement intégré aux systèmes métiers, nous pouvons extraire une réelle valeur de ses prédictions. - Christopher Samiullah

Il existe différentes façons de déployer votre modèle de machine learning en production. Mais dans l'article d'aujourd'hui, vous apprendrez comment déployer votre modèle NLP en production en tant qu'API avec Algorithmia.

Dans cet article, vous apprendrez :

* Comment créer un modèle NLP qui détecte les messages SMS spam
* Comment utiliser Algorithmia, une plateforme MLOps.
* Comment déployer votre modèle sur la plateforme Algorithmia
* Comment utiliser votre modèle NLP déployé dans n'importe quelle application Python.

Notre première étape est de créer un modèle de machine learning capable de détecter les messages SMS spam. Alors commençons !

## Comment construire le modèle ML

Tout d'abord, nous devons construire notre modèle. Voici les étapes à suivre pour ce faire.

### Importer les packages Python 

Nous commençons par importer tous les packages Python importants que nous utiliserons pour charger les données, pré-traiter les données et créer un modèle de classification de texte.

```python
# import important modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from string import punctuation 

# sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    plot_confusion_matrix,
    f1_score,
    roc_auc_score,
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score, RandomizedSearchCV

# text preprocessing modules
from nltk.tokenize import word_tokenize
from cleantext import clean

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import re #regular expression


from wordcloud import WordCloud, STOPWORDS

# Download dependency
for dependency in (
    "brown",
    "names",
    "wordnet",
    "averaged_perceptron_tagger",
    "universal_tagset",
    "stopwords"
):
    nltk.download(dependency)

#nltk.download('stopwords')

import warnings
warnings.filterwarnings("ignore")
# seeding
np.random.seed(123)
```

### Charger le jeu de données Spam

Ensuite, nous chargeons le jeu de données spam depuis le répertoire de données, comme ceci :

```python
# load data
data = pd.read_csv("../data/spam.tsv", sep="\t")
```

Regardons les cinq premières lignes du jeu de données.

```python
# show top five rows
data.head()
```

![Image](https://developers.decoded.africa/content/images/2020/10/head.PNG)

Le jeu de données contient quatre colonnes, mais nous nous concentrerons uniquement sur les colonnes message et label.

Vérifions la forme du jeu de données :

```python
# check the shape
data.shape
```

output: (5572, 4)  
  
Nous avons 5572 lignes et 4 colonnes.

### Comment gérer les valeurs manquantes

Parfois, les données peuvent contenir des valeurs manquantes. Nous pouvons utiliser la méthode **isnull()** de pandas pour vérifier si notre jeu de données contient des valeurs manquantes.

```python
# check missing values
data.isnull().sum()
```

![Image](https://developers.decoded.africa/content/images/2020/10/check-missing.PNG)

La sortie montre que notre jeu de données ne contient aucune valeur manquante.

### Comment évaluer la distribution des classes

Nous pouvons utiliser la méthode **value_counts()** du package pandas pour évaluer la distribution des classes de notre jeu de données.

```python
# evalute class distribution
data["label"].value_counts()
```

![Image](https://developers.decoded.africa/content/images/2020/10/class-distribution.PNG)

Dans ce jeu de données, nous avons plus de messages légitimes (ham) que de messages spam.

### Analyse exploratoire des données

C'est une étape très importante dans la création de votre projet de machine learning. Elle vous aide à mieux comprendre votre jeu de données. 

Dans cette étape, nous allons trouver les mots fréquents utilisés dans les messages légitimes et les messages spam. 

```python
# collect words from the dataset
def collect_words(data, label):
    collected_words = " "

    # iterate through the csv file
    for val in data.message[data["label"] == label]:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
            collected_words = collected_words + words + " "

    return collected_words
```

La fonction ci-dessus appelée **collect_words()** collectera tous les mots du jeu de données selon leurs labels (ham ou spam). 

Ensuite, nous pouvons visualiser les mots fréquents en utilisant le package Python **wordcloud**. Nous commencerons par les messages étiquetés comme ham (légitimes).

```python
# visualize ham labeled sms
cloud_stopwords = set(STOPWORDS)
ham_words = collect_words(data, label="ham")

print("Total words {}".format(len(ham_words)))

wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=cloud_stopwords,
    min_font_size=10,
).generate(ham_words)

# plot the WordCloud image
plt.figure(figsize=(15, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
```

Total words: 349132

![Image](https://developers.decoded.africa/content/images/2020/10/first-cloud.png)

Comme vous pouvez le voir dans les messages légitimes, les mots les plus fréquents sont _will, gt, now, ok, call, want, got,_ et ainsi de suite.

Maintenant, nous pouvons visualiser les mots les plus fréquents dans les messages étiquetés comme spam. 

```python
# visualize spam labeled sms
cloud_stopwords = set(STOPWORDS)
spam_words = collect_words(data, label="spam")

print("Total words {}".format(len(spam_words)))

wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=cloud_stopwords,
    min_font_size=10,
).generate(spam_words)

# plot the WordCloud image
plt.figure(figsize=(10, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
```

Total words: 104304

![Image](https://developers.decoded.africa/content/images/2020/10/second-cloud.png)

Dans la figure ci-dessus, il est montré que les mots les plus fréquents sont ceux comme _call, claim, free, txt, mobile, reply, offer_ et ainsi de suite.

### Comment traiter les données

Après avoir exploré et analysé le jeu de données, l'étape suivante consiste à pré-traiter le jeu de données dans le bon format avant de créer notre modèle de machine learning.

Nous remplaçons d'abord les classes ham et spam par des valeurs numériques. La classe ham sera étiquetée comme 0 et la classe spam sera étiquetée comme 1.

```python
# replace ham to 0 and spam to 1
new_data = data.replace({"ham": 0, "spam": 1})
new_data.head()
```

![Image](https://developers.decoded.africa/content/images/2020/10/new-labeled.PNG)

Les messages de ce jeu de données contiennent beaucoup de mots et de caractères inutiles dont nous n'avons pas besoin lors de la création de modèles de machine learning. 

Nous allons nettoyer les messages en supprimant les stopwords, les nombres et la ponctuation. Ensuite, nous allons convertir les mots en minuscules, et enfin convertir chaque mot en sa forme de base en utilisant le processus de lemmatisation dans le package NLTK.

La fonction **text_cleaning()** gérera toutes les étapes nécessaires pour nettoyer notre jeu de données.

```
stop_words =  stopwords.words('english')

def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Clean the text, with the option to remove stop_words and to lemmatize word

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"ur", " your ", text)
    text = re.sub(r" nd "," and ",text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r" tkts "," tickets ",text)
    text = re.sub(r" c "," can ",text)
    text = re.sub(r" e g ", " eg ", text)
    text =  re.sub(r'http\S+',' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text) # remove numbers
    text = re.sub(r" u "," you ",text)
    text = text.lower()  # set in lowercase 
        
    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])
    
    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer() 
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    
    # Return a list of words
    return(text)
```

Maintenant, nous pouvons nettoyer notre jeu de données en utilisant la fonction **text_cleaning()**.

```python
#clean the dataset 
new_data["clean_message"] = new_data["message"].apply(text_cleaning)
```

Nous divisons ensuite notre jeu de données en données d'entraînement et de test. La taille du test est de 15 % de l'ensemble du jeu de données.

```python
# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    new_data["clean_message"],
    new_data["label"],
    test_size=0.15,
    random_state=0,
    shuffle=True,
    stratify=data["label"],
)
```

La méthode CountVectorizer de scikit-learn nous aidera à transformer notre jeu de données nettoyé en valeurs numériques. La méthode convertit une collection de documents textuels en une matrice de comptes de tokens.

```python
# Transform text data 
vectorizer = CountVectorizer(lowercase=False)
vectorizer.fit(X_train)

#transform train data 
X_train_trans = vectorizer.transform(X_train)

#transform test data
X_text_trans = vectorizer.transform(X_test)
```

### Comment créer notre modèle

Nous allons entraîner l'algorithme Multinomial Naive Bayes pour classer si un message est légitime ou spam. C'est l'un des algorithmes les plus courants utilisés pour la classification de texte.

```python
# Create a classifier

spam_classifier = MultinomialNB()
    
```

Ensuite, nous entraînons notre classificateur en utilisant la validation croisée pour éviter le surapprentissage.

```python
# Train the model with cross validation
scores = cross_val_score(spam_classifier,X_train_trans,y_train,cv=10,verbose=3,n_jobs=-1)
```

![Image](https://developers.decoded.africa/content/images/2020/10/first-cross-validation.PNG)

Voyons le score moyen.

```python
# find the mean of the all scores
scores.mean()
```

output: 0.9767713936539371  
  
La moyenne des scores est d'environ 97,68 %. Notre modèle performe bien, mais nous pouvons améliorer ses performances en optimisant ses valeurs d'hyperparamètres avec la méthode Randomized Search de scikit-learn.

```python
# fine turning model parameters

distribution = {"alpha": [1, 0.1, 0.01, 0.001, 0.0001, 0, 0.2, 0.3]}

grid = RandomizedSearchCV(
    spam_classifier,
    param_distributions=distribution,
    n_jobs=-1,
    cv=10,
    n_iter=20,
    random_state=42,
    return_train_score=True,
    verbose=2,
)
```

Nous allons optimiser l'hyperparamètre **alpha** de notre modèle pour obtenir la meilleure valeur qui augmentera les performances de notre modèle. 

```python
# training with randomized search
grid.fit(X_train_trans, y_train)
```

![Image](https://developers.decoded.africa/content/images/2020/10/random-search.PNG)

Pour montrer les résultats de l'optimisation des hyperparamètres :

```python
# summarize the results of the random parameter search
print(grid.best_score_)
print(grid.best_estimator_)
print(grid.best_params_)
```

0.9767713936539371  
 MultinomialNB(alpha=1)  
 {'alpha': 1}

Le meilleur score est le même que le précédent. Maintenant, testons notre modèle avec les données de test.

```python
# predict on the test data
y_pred = spam_classifier.predict(X_text_trans)
```

Les performances du modèle seront évaluées en utilisant la métrique d'évaluation **accuracy_score**.

```python
# check accuracy score
accuracy_score(y_test, y_pred)
```

output: 0.9760765550239234  
  
La précision de notre modèle est d'environ **97,6 %**, ce qui est une bonne performance.

Une autre métrique d'évaluation utile à utiliser est **f1_score** lorsque vous avez un déséquilibre de classe dans votre jeu de données.

```python
# check f1_ score
f1_score(y_test, y_pred)
```

output: 0.908256880733945  
  
Le score est de **0,91**, ce qui est proche de **1**. Cela signifie que notre modèle a de bonnes performances et nous pouvons maintenant le déployer en production.

Le modèle sera sauvegardé dans le répertoire des modèles.

```python
#save model 
import joblib 

joblib.dump(spam_classifier, '../models/spam-detection-model.pkl')
```

['../models/spam-detection-model.pkl']  
  
Notre Count Vectorizer sera également sauvegardé dans le répertoire de pré-traitement.

```ptython
#save Vectorizer
joblib.dump(vectorizer,'../preprocessing/count_vectorizer.pkl')
```

['../preprocessing/count_vectorizer.pkl']

Après avoir créé notre modèle de détection de spam, il est temps de le déployer sur la plateforme Algorithmia.

## Qu'est-ce qu'Algorithmia ?

[Algorithmia](https://algorithmia.com/) est un outil MLOps qui fournit un moyen simple et plus rapide de déployer votre modèle de machine learning en production. 

Algorithmia se spécialise dans les **"algorithmes en tant que service"**. Il permet aux utilisateurs de créer des extraits de code qui exécutent le modèle ML et de les héberger sur Algorithmia. Ensuite, vous pouvez appeler votre code en tant qu'API. 

Maintenant, votre modèle peut être utilisé pour différentes applications de votre choix, telles que des applications web, des applications mobiles ou du commerce électronique avec un simple appel d'API depuis Algorithmia.

![Image](https://developers.decoded.africa/content/images/2020/11/190.png)

Algorithmia prend en charge les modèles de machine learning développés par différents langages de programmation tels que R, Python, Java et Scala. Il prend également en charge les frameworks populaires de machine et de deep learning tels que Pytorch, Tensorflow, scikit-learn, XGBoost et Keras. 

Algorithmia utilise à la fois des CPU et des GPU sur sa couche d'Intelligence Artificielle serverless pour optimiser les coûts et maximiser ses performances pour répondre à vos besoins. 
Actuellement, cette plateforme compte plus de 60 000 développeurs avec 4 500 algorithmes.

Voici six étapes que vous devez suivre pour déployer votre modèle de machine learning sur Algorithmia.

### Étape 1 : Créer un compte sur Algorithmia

La première étape consiste à créer un compte sur Algorithmia en visitant cette page : [https://algorithmia.com/signup](https://algorithmia.com/signup).

### Étape 2 : Créer un nouvel algorithme

Après avoir créé et confirmé votre compte et votre email, l'étape suivante consiste à créer un nouvel algorithme en cliquant sur le bouton du menu déroulant nommé **"Create New"**. Ensuite, vous sélectionnez simplement **Algorithm** en haut à droite de la page.

![Image](https://developers.decoded.africa/content/images/2020/11/create--new-algorithm.PNG)

Ensuite, entrez le nom de l'algorithme, par exemple DÉTECTION DE SPAM SMS. Dans la section **source code**, vous pouvez déterminer où le code source de votre algorithme sera hébergé. 

Par défaut, le code source sera sur la plateforme Algorithmia. Vous pouvez choisir de le garder sur GitHub, mais pour cet article, nous utiliserons l'option par défaut. 

La section suivante spécifie l'environnement. Algorithmia vous donne différentes options pour sélectionner différents environnements tels que Python, R, JavaScript, Java et Scala. L'option par défaut est Python 3.X, et ici nous continuerons avec cette option. Enfin, cliquez sur le bouton "**Create new Algorithm**".

### Étape 3 : Télécharger le modèle pré-entraîné et le CountVectorizer sur Algorithmia

Vous pouvez télécharger votre modèle sélectionné dans la section des données en cliquant sur **Data Sources** dans le panneau de gauche de la plateforme Algorithmia. Ensuite, cliquez sur le répertoire **My hosted data** où vous pouvez créer un nouveau dossier pour garder tous vos fichiers pkl téléchargés pour cet algorithme spécifique. 

À l'intérieur du répertoire "My hosted data", j'ai créé un nouveau dossier appelé **sms_spam_detection**. Ensuite, j'ai téléchargé notre modèle pré-entraîné et le CountVectorizer entraîné pour convertir les messages textuels (sms) en un vecteur de comptes de termes/tokens.

![Image](https://developers.decoded.africa/content/images/2020/11/data-source.PNG)

### Étape 4 : Ajouter le code source

Après avoir téléchargé notre modèle pré-entraîné, cliquez sur l'onglet **Source Code**. Il ouvrira un IDE où vous ajoutez le code source pour exécuter le modèle de machine learning que nous avons créé. Voici comment ajouter le code source : 

**(a) Importer les packages**   
Nous commençons par importer les packages Python importants, y compris Algorithmia, qui appellera l'algorithme que nous avons créé.

```python
import sys
import joblib
import pickle
import numpy as np
import Algorithmia
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from string import punctuation
import re 
import nltk
#download dependency
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
```

NB : La plateforme d'Algorithmia importera automatiquement le package Python Algorithmia dans le fichier.

**(b) Créer le Client**   
Nous créons ensuite un client à partir du package Algorithmia qui fournit un moyen standardisé d'appeler n'importe quel algorithme.

```python

# we are creating the variable in global scope to use throughout our algorithm.
client = Algorithmia.client()
```

**(c) Ajouter des fonctions pour charger le modèle pré-entraîné et les fichiers pkl de countvectorizer**  
La fonction **load_model()** chargera notre modèle pré-entraîné depuis le répertoire de la source de données et la fonction **load_preprocessing()** chargera le fichier countvectorizer.

```python
def load_preprocessing():
    # Get file by name
    # Open file and load model
    file_path = 'data://Davis/sms_spam_detection/count-vectorizer.pkl'
    object_path = client.file(file_path).getFile().name
    # Open file and preprocessin object
    with open(object_path, 'rb') as f:
        object = joblib.load(f)
        return object    

def load_model():
    # Get file by name
    # Open file and load model
    file_path = 'data://Davis/sms_spam_detection/spam-detection-model.pkl'
    model_path = client.file(file_path).getFile().name
    # Open file and load model
    with open(model_path, 'rb') as f:
        model = joblib.load(f)
        return model

# Load model outside of the apply function so it only gets loaded once

model = load_model()
vectorizer = load_preprocessing()
```

**(d) Ajouter la fonction pour nettoyer l'entrée de texte**  
Ici, nous utiliserons la même fonction **text_clean()** pour nettoyer les messages SMS.

```python
#set stopwords
stop_words = stopwords.words('english')

def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Clean the text, with the option to remove stop_words and to lemmatize word

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"ur", " your ", text)
    text = re.sub(r" nd ", " and ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r" tkts ", " tickets ", text)
    text = re.sub(r" c ", " can ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r'http\S+', ' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text)  # remove numbers
    text = re.sub(r" u ", " you ", text)
    text = text.lower()  # set in lowercase

    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])

    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)

    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)

    # Return a list of words
    return (text)
```

**(e) Ajouter la fonction pour pré-traiter l'entrée**  
La méthode **process_input()** pré-traitera l'entrée SMS avant de faire une prédiction.

```python
def process_input(input):
    # Preprocess and Create numpy array from the input
    
    message = str(input)
    clean_message = text_cleaning(message)
    
    #vectorize the message 
    vect_message = vectorizer.transform([clean_message])
    
    print(vect_message)
    
    return vect_message
```

**(f) Ajouter la fonction pour appliquer le modèle pour la prédiction**  
La dernière fonction appelée **apply()** sera responsable de la réalisation des prédictions à partir du texte SMS pré-traité. Elle retournera _"normal message"_ si le message est légitime et _"spam message"_ si le message est du spam.

```python
def apply(input):
    # pefrom prediction from the input. 
   
    message = process_input(input)
    prediction = model.predict(message)
    if prediction[0] == 0:
        return "normal message"
    else:
        return "spam message"

```

  
Enfin, nous sauvegardons le code source ajouté dans le fichier.

![Image](https://developers.decoded.africa/content/images/2020/11/ide.PNG)

### Étape 5 : Ajouter les dépendances à Algorithmia

Cliquez sur l'onglet **dependencies** depuis l'interface utilisateur et ajoutez les packages suivants dont notre modèle dépend :

* numpy
* joblib
* scikit-learn == 0.22.2.post1
* unidecode
*  nltk == 3.5

Ensuite, cliquez sur **save dependencies** dans le coin inférieur droit :

![Image](https://developers.decoded.africa/content/images/2020/11/dependencies.PNG)

NB : Le fichier de dépendances dans Algorithmia est le même qu'un fichier requirements.txt qui récupère les dépendances listées depuis PyPi. 

Sur la page de l'éditeur, cliquez sur l'onglet **build** en haut à droite pour installer toutes les dépendances listées dans le fichier de dépendances. Si toutes les dépendances sont installées avec succès, vous verrez qu'une version spécifique de votre algorithme est maintenant en ligne et prête à être publiée.

![Image](https://developers.decoded.africa/content/images/2020/11/specific-version.PNG)

### Étape 6 : Publier l'algorithme

Notre dernière étape consiste à publier l'algorithme. Il y a 3 étapes pour publier un algorithme : documenter tous les changements, ajouter un exemple d'entrée et de sortie, et configurer les paramètres de l'algorithme.

**(a) Documenter les changements**  
Vous verrez votre historique de commit et vous pourrez ajouter une note de version.

![Image](https://developers.decoded.africa/content/images/2020/11/document-changes.PNG)

**(b) Ajouter un exemple**  
Dans cette section, vous créez votre entrée et sortie d'exemple afin que les utilisateurs puissent essayer votre algorithme.

![Image](https://developers.decoded.africa/content/images/2020/11/input-and-output-example.PNG)

**(c) Configurer les paramètres de l'algorithme**   
Enfin, vous sélectionnez si votre algorithme sera **public** (ce qui signifie que n'importe qui peut l'appeler) ou **privé** (ce qui signifie que seuls les propriétaires peuvent l'appeler). Vous devez également définir la redevance et ensuite cliquer sur le bouton **publish** en bas de la page.

![Image](https://developers.decoded.africa/content/images/2020/11/configure-settings.PNG)

Notre modèle NLP a été déployé avec succès sur la plateforme Algorithmia. Voyons comment nous pouvons utiliser notre modèle déployé dans une application Python telle que Flask ou Django.

## Comment installer le client Python Algorithmia

Nous commençons par installer le client Python Algorithmia en utilisant PIP. Cela nous aidera à appeler notre code qui exécute le modèle NLP.

```command
pip install algorithmia
```

### Collecter la clé API

Cliquez sur l'onglet "API Key" de votre panneau d'algorithme pour collecter la clé API qui vous aidera à appeler le code qui exécute le modèle NLP.

### Créer le client Algorithmia 

Nous commençons par importer le package Python Algorithmia, puis nous créons l'objet client de l'algorithme

```python
import Algorithmia

# Authenticate with your API key
apiKey = "YOUR_API_KEY"

# Create the Algorithmia client object
client = Algorithmia.client(apiKey)
```

### Appeler l'algorithme 

Pour appeler l'algorithme, nous devons ajouter le nom de l'algorithme avec sa version à l'objet client que nous avons créé. 

Le nom est **"Davis/spam_detection/0.2.0"**, qui inclut le nom de votre compte sur Algorithmia suivi du nom de l'algorithme que nous avons créé. La dernière partie est la version de l'algorithme (0.2.0).

```
# Create the algorithm object using the Summarizer algorithm
algo = client.algo('Davis/spam_detection/0.2.0')

# Pass in input required by algorithm
input_sms = "Win a \u00c2\u00a31000 cash prize or a prize worth \u00c2\u00a35000"

try:
    # Get the result
    print(algo.pipe(input_sms).result)
except Exception as error:
    # Algorithm error if, for example, the input is not correctly formatted
    print(error)
```

Pour cet exemple, le modèle prédit que le SMS est un **"spam message"**. Cool, ça marche !

## Conclusion

Félicitations, vous êtes arrivé à la fin de cet article !

Vous pouvez télécharger le jeu de données et le notebook utilisés dans cet article ici : [https://github.com/Davisy/SMS-Spam-Text-Classification](https://github.com/Davisy/SMS-Spam-Text-Classification)

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Je peux également être contacté sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).