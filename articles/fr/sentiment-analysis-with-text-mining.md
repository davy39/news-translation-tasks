---
title: Analyse de sentiment avec le text mining
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-13T21:42:41.000Z'
originalURL: https://freecodecamp.org/news/sentiment-analysis-with-text-mining
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/dictionary.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
- name: Sentiment analysis
  slug: sentiment-analysis
- name: text mining
  slug: text-mining
seo_title: Analyse de sentiment avec le text mining
seo_desc: 'By Bert Carremans

  In this tutorial, I will explore some text mining techniques for sentiment analysis.
  We''ll look at how to prepare textual data. After that we will try two different
  classifiers to infer the tweets'' sentiment. We will tune the hyperp...'
---

Par Bert Carremans

Dans ce tutoriel, je vais explorer quelques techniques de text mining pour l'analyse de sentiment. Nous examinerons comment préparer les données textuelles. Après cela, nous essaierons deux classificateurs différents pour déduire le sentiment des tweets. Nous ajusterons les hyperparamètres des deux classificateurs avec une recherche par grille. Enfin, nous évaluerons les performances sur un ensemble de métriques comme la précision, le rappel et le score F1.

Pour ce projet, nous travaillerons avec l'ensemble de données [Twitter US Airline Sentiment sur Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment). Il contient le texte du tweet et une variable avec trois valeurs de sentiment possibles. Commençons par importer les packages et configurer quelques paramètres.

```python
import numpy as np 
import pandas as pd 
pd.set_option('display.max_colwidth', -1)
from time import time
import re
import string
import os
import emoji
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
sns.set(font_scale=1.3)
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import gensim
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')
np.random.seed(37)
```

## Chargement des données

Nous lisons le fichier séparé par des virgules que nous avons téléchargé depuis les ensembles de données Kaggle. Nous mélangeons le cadre de données au cas où les classes seraient triées. L'application de la méthode `reindex` sur la `permutation` des indices originaux est bonne pour cela. Dans ce notebook, nous travaillerons avec la variable `text` et la variable `airline_sentiment`.

```python
df = pd.read_csv('../input/Tweets.csv')
df = df.reindex(np.random.permutation(df.index))
df = df[['text', 'airline_sentiment']]
```

## Analyse exploratoire des données

### Variable cible

Il y a trois étiquettes de classe que nous allons prédire : négatif, neutre ou positif.

Les étiquettes de classe sont déséquilibrées comme nous pouvons le voir ci-dessous dans le graphique. C'est quelque chose que nous devons garder à l'esprit pendant la phase d'entraînement du modèle. Avec le `factorplot` du package seaborn, nous pouvons visualiser la distribution de la variable cible.

```python
sns.factorplot(x="airline_sentiment", data=df, kind="count", size=6, aspect=1.5, palette="PuBuGn_d")
plt.show();
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*v99Gfk4iL4POvy2F.png)
_Distribution déséquilibrée des étiquettes de classe cible_

### Variable d'entrée

Pour analyser la variable `text`, nous créons une classe `TextCounts`. Dans cette classe, nous calculons quelques statistiques de base sur la variable textuelle.

* `count_words` : nombre de mots dans le tweet
* `count_mentions` : références à d'autres comptes Twitter commencent par un @
* `count_hashtags` : nombre de mots étiquetés, précédés d'un #
* `count_capital_words` : nombre de mots en majuscules sont parfois utilisés pour "crier" et exprimer des émotions (négatives)
* `count_excl_quest_marks` : nombre de points d'interrogation ou d'exclamation
* `count_urls` : nombre de liens dans le tweet, précédés par http(s)
* `count_emojis` : nombre d'emojis, qui pourraient être un bon signe du sentiment

```python
class TextCounts(BaseEstimator, TransformerMixin):
    
    def count_regex(self, pattern, tweet):
        return len(re.findall(pattern, tweet))
    
    def fit(self, X, y=None, **fit_params):
        # la méthode fit est utilisée lorsque des opérations spécifiques doivent être effectuées sur les données d'entraînement, mais pas sur les données de test
        return self
    
    def transform(self, X, **transform_params):
        count_words = X.apply(lambda x: self.count_regex(r'\w+', x)) 
        count_mentions = X.apply(lambda x: self.count_regex(r'@\w+', x))
        count_hashtags = X.apply(lambda x: self.count_regex(r'#\w+', x))
        count_capital_words = X.apply(lambda x: self.count_regex(r'\b[A-Z]{2,}\b', x))
        count_excl_quest_marks = X.apply(lambda x: self.count_regex(r'!|\?', x))
        count_urls = X.apply(lambda x: self.count_regex(r'http.?://[^\s]+[\s]?', x))
        # Nous allons remplacer les symboles emoji par une description, ce qui facilite l'utilisation d'une regex pour le comptage
        # De plus, cela résultera en ayant plus de mots dans le tweet
        count_emojis = X.apply(lambda x: emoji.demojize(x)).apply(lambda x: self.count_regex(r':[a-z_&]+:', x))
        
        df = pd.DataFrame({'count_words': count_words
                           , 'count_mentions': count_mentions
                           , 'count_hashtags': count_hashtags
                           , 'count_capital_words': count_capital_words
                           , 'count_excl_quest_marks': count_excl_quest_marks
                           , 'count_urls': count_urls
                           , 'count_emojis': count_emojis
                          })
        
        return df
tc = TextCounts()
df_eda = tc.fit_transform(df.text)
df_eda['airline_sentiment'] = df.airline_sentiment
```

Il pourrait être intéressant de voir comment les variables TextStats se rapportent à la variable de classe. Nous écrivons donc une fonction `show_dist` qui fournit des statistiques descriptives et un graphique par classe cible.

```python
def show_dist(df, col):
    print('Statistiques descriptives pour {}'.format(col))
    print('-'*(len(col)+22))
    print(df.groupby('airline_sentiment')[col].describe())
    bins = np.arange(df[col].min(), df[col].max() + 1)
    g = sns.FacetGrid(df, col='airline_sentiment', size=5, hue='airline_sentiment', palette="PuBuGn_d")
    g = g.map(sns.distplot, col, kde=False, norm_hist=True, bins=bins)
    plt.show()
```

Ci-dessous, vous pouvez trouver la distribution du nombre de mots dans un tweet par classe cible. Pour brièveté, nous nous limiterons à cette seule variable. Les graphiques pour toutes les variables TextCounts se trouvent dans le [notebook sur Github](https://github.com/bertcarremans/TwitterUSAirlineSentiment).

![Image](https://cdn-media-1.freecodecamp.org/images/0*snmvA3GQOb_S9wV8.png)

* Le nombre de mots utilisés dans les tweets est plutôt faible. Le plus grand nombre de mots est de 36 et il y a même des tweets avec seulement 2 mots. Nous devons donc être prudents lors du nettoyage des données pour ne pas supprimer trop de mots. Mais le traitement du texte sera plus rapide. Les tweets négatifs contiennent plus de mots que les tweets neutres ou positifs.
* Tous les tweets ont au moins une mention. Cela résulte de l'extraction des tweets basée sur les mentions dans les données Twitter. Il semble ne pas y avoir de différence dans le nombre de mentions en ce qui concerne le sentiment.
* La plupart des tweets ne contiennent pas de mots-clés. Cette variable ne sera donc pas conservée lors de l'entraînement du modèle. Encore une fois, aucune différence dans le nombre de mots-clés en ce qui concerne le sentiment.
* La plupart des tweets ne contiennent pas de mots en majuscules et nous ne voyons pas de différence dans la distribution entre les sentiments.
* Les tweets positifs semblent utiliser un peu plus de points d'exclamation ou d'interrogation.
* La plupart des tweets ne contiennent pas d'URL.
* La plupart des tweets n'utilisent pas d'emojis.

## Nettoyage du texte

Avant de commencer à utiliser le texte des tweets, nous devons le nettoyer. Nous allons le faire dans la classe `CleanText`. Avec cette classe, nous allons effectuer les actions suivantes :

* supprimer les mentions, car nous voulons généraliser aux tweets d'autres compagnies aériennes également.
* supprimer le signe de mot-clé (#) mais pas le mot-clé lui-même car cela peut contenir des informations
* mettre tous les mots en minuscules
* supprimer toutes les ponctuations, y compris les points d'interrogation et d'exclamation
* supprimer les URL car elles ne contiennent pas d'informations utiles. Nous n'avons pas remarqué de différence dans le nombre d'URL utilisées entre les classes de sentiment
* veiller à convertir les emojis en un seul mot.
* supprimer les chiffres
* supprimer les mots vides
* appliquer le `PorterStemmer` pour conserver la racine des mots

```python
class CleanText(BaseEstimator, TransformerMixin):
    def remove_mentions(self, input_text):
        return re.sub(r'@\w+', '', input_text)
    
    def remove_urls(self, input_text):
        return re.sub(r'http.?://[^\s]+[\s]?', '', input_text)
    
    def emoji_oneword(self, input_text):
        # En compressant le tiret bas, l'emoji est conservé comme un seul mot
        return input_text.replace('_','')
    
    def remove_punctuation(self, input_text):
        # Créer une table de traduction
        punct = string.punctuation
        trantab = str.maketrans(punct, len(punct)*' ')  # Chaque symbole de ponctuation sera remplacé par un espace
        return input_text.translate(trantab)
    def remove_digits(self, input_text):
        return re.sub('\d+', '', input_text)
    
    def to_lower(self, input_text):
        return input_text.lower()
    
    def remove_stopwords(self, input_text):
        stopwords_list = stopwords.words('english')
        # Certains mots qui pourraient indiquer un certain sentiment sont conservés via une liste blanche
        whitelist = ["n't", "not", "no"]
        words = input_text.split() 
        clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
        return " ".join(clean_words) 
    
    def stemming(self, input_text):
        porter = PorterStemmer()
        words = input_text.split() 
        stemmed_words = [porter.stem(word) for word in words]
        return " ".join(stemmed_words)
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, **transform_params):
        clean_X = X.apply(self.remove_mentions).apply(self.remove_urls).apply(self.emoji_oneword).apply(self.remove_punctuation).apply(self.remove_digits).apply(self.to_lower).apply(self.remove_stopwords).apply(self.stemming)
        return clean_X
```

Pour montrer à quoi ressemblera la variable de texte nettoyée, voici un exemple.

```python
ct = CleanText()
sr_clean = ct.fit_transform(df.text)
sr_clean.sample(5)
```

> _glad rt bet bird wish flown south winter_  
> _point upc code check baggag tell luggag vacat day tri swimsuit_  
> _vx jfk la dirti plane not standard_  
> _tell mean work need estim time arriv pleas need laptop work thank_  
> _sure busi go els airlin travel name kathryn sotelo_

Un effet secondaire du nettoyage du texte est que certaines lignes n'ont plus aucun mot dans leur texte. Pour le `CountVectorizer` et le `TfIdfVectorizer`, cela ne pose pas de problème. Cependant, pour l'algorithme `Word2Vec`, cela provoque une erreur. Il existe différentes stratégies pour traiter ces valeurs manquantes.

* Supprimer la ligne complète, mais dans un environnement de production, cela n'est pas souhaitable.
* Imputer la valeur manquante avec un texte de remplacement comme *[no_text]*
* Lors de l'application de Word2Vec : utiliser la moyenne de tous les vecteurs

Ici, nous allons imputer avec un texte de remplacement.

```python
empty_clean = sr_clean == ''
print('{} enregistrements n'ont plus de mots après le nettoyage du texte'.format(sr_clean[empty_clean].count()))
sr_clean.loc[empty_clean] = '[no_text]'
```

Maintenant que nous avons le texte nettoyé des tweets, nous pouvons voir quels sont les mots les plus fréquents. Ci-dessous, nous allons montrer les 20 mots les plus fréquents. Le mot le plus fréquent est "flight".

```python
cv = CountVectorizer()
bow = cv.fit_transform(sr_clean)
word_freq = dict(zip(cv.get_feature_names(), np.asarray(bow.sum(axis=0)).ravel()))
word_counter = collections.Counter(word_freq)
word_counter_df = pd.DataFrame(word_counter.most_common(20), columns = ['word', 'freq'])
fig, ax = plt.subplots(figsize=(12, 10))
sns.barplot(x="word", y="freq", data=word_counter_df, palette="PuBuGn_d", ax=ax)
plt.show();
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*hBvkYfey1Astmd02.png)

## Création de données de test

Pour vérifier les performances des modèles, nous aurons besoin d'un ensemble de test. Évaluer sur les données d'entraînement ne serait pas correct. Vous ne devriez pas tester sur les mêmes données utilisées pour l'entraînement du modèle.

Tout d'abord, nous combinons les variables `TextCounts` avec la variable `CleanText`. Initialement, j'ai fait l'erreur d'exécuter TextCounts et CleanText dans le `GridSearchCV`. Cela a pris trop de temps car il applique ces fonctions à chaque exécution de la GridSearch. Il suffit de les exécuter une seule fois.

```python
df_model = df_eda
df_model['clean_text'] = sr_clean
df_model.columns.tolist()
```

Ainsi, `df_model` contient maintenant plusieurs variables. Mais nos vectoriseurs (voir ci-dessous) n'auront besoin que de la variable `clean_text`. Les variables `TextCounts` peuvent être ajoutées telles quelles. Pour sélectionner les colonnes, j'ai écrit la classe `ColumnExtractor` ci-dessous.

```python
class ColumnExtractor(TransformerMixin, BaseEstimator):
    def __init__(self, cols):
        self.cols = cols
    def transform(self, X, **transform_params):
        return X[self.cols]
    def fit(self, X, y=None, **fit_params):
        return self
X_train, X_test, y_train, y_test = train_test_split(df_model.drop('airline_sentiment', axis=1), df_model.airline_sentiment, test_size=0.1, random_state=37)
```

## Réglage des hyperparamètres et validation croisée

Comme nous le verrons ci-dessous, les vectoriseurs et les classificateurs ont tous des paramètres configurables. Pour choisir les meilleurs paramètres, nous devons tester sur un ensemble de validation séparé. Cet ensemble de validation n'a pas été utilisé pendant l'entraînement. Cependant, l'utilisation d'un seul ensemble de validation peut ne pas produire des résultats de validation fiables. En raison du hasard, vous pourriez avoir une bonne performance du modèle sur l'ensemble de validation. Si vous divisez les données autrement, vous pourriez obtenir d'autres résultats. Pour obtenir une estimation plus précise, nous effectuons une validation croisée.

Avec la validation croisée, nous divisons les données en un ensemble d'entraînement et de validation plusieurs fois. La métrique d'évaluation est ensuite moyennée sur les différents plis. Heureusement, GridSearchCV applique la validation croisée directement.

Pour trouver les meilleurs paramètres pour un vectoriseur et un classificateur, nous créons un `Pipeline`.

## Métriques d'évaluation

Par défaut, GridSearchCV utilise le scoreur par défaut pour calculer le `best_score_`. Pour le `MultiNomialNb` et le `LogisticRegression`, cette métrique de score par défaut est la précision.

Dans notre fonction `grid_vect`, nous générons également le `classification_report` sur les données de test. Cela fournit quelques métriques intéressantes par classe cible. Cela pourrait être plus approprié ici. Ces métriques sont la précision, le rappel et le score F1.

* Précision : Parmi toutes les lignes que nous avons prédites comme étant une certaine classe, combien avons-nous correctement prédites ?
* Rappel : Parmi toutes les lignes d'une certaine classe, combien avons-nous correctement prédites ?
* Score F1 : Moyenne harmonique de la Précision et du Rappel.

Avec les éléments de la [matrice de confusion](https://en.wikipedia.org/wiki/Confusion_matrix), nous pouvons calculer la Précision et le Rappel.

```python
# Basé sur http://scikit-learn.org/stable/auto_examples/model_selection/grid_search_text_feature_extraction.html
def grid_vect(clf, parameters_clf, X_train, X_test, parameters_text=None, vect=None, is_w2v=False):
    
    textcountscols = ['count_capital_words','count_emojis','count_excl_quest_marks','count_hashtags'
                      ,'count_mentions','count_urls','count_words']
    
    if is_w2v:
        w2vcols = []
        for i in range(SIZE):
            w2vcols.append(i)
        features = FeatureUnion([('textcounts', ColumnExtractor(cols=textcountscols))
                                 , ('w2v', ColumnExtractor(cols=w2vcols))]
                                , n_jobs=-1)
    else:
        features = FeatureUnion([('textcounts', ColumnExtractor(cols=textcountscols))
                                 , ('pipe', Pipeline([('cleantext', ColumnExtractor(cols='clean_text')), ('vect', vect)]))]
                                , n_jobs=-1)
    
    pipeline = Pipeline([
        ('features', features)
        , ('clf', clf)
    ])
    
    # Joindre les dictionnaires de paramètres ensemble
    parameters = dict()
    if parameters_text:
        parameters.update(parameters_text)
    parameters.update(parameters_clf)
    # Assurez-vous d'avoir la version 0.19 ou supérieure de scikit-learn pour utiliser plusieurs métriques de score
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=5)
    
    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0 = time()
    grid_search.fit(X_train, y_train)
    print("done in %0.3fs" % (time() - t0))
    print()
    print("Best CV score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
        
    print("Test score with best_estimator_: %0.3f" % grid_search.best_estimator_.score(X_test, y_test))
    print("\n")
    print("Classification Report Test Data")
    print(classification_report(y_test, grid_search.best_estimator_.predict(X_test)))
                        
    return grid_search
```

## Grilles de paramètres pour GridSearchCV

Dans la recherche par grille, nous allons étudier la performance du classificateur. L'ensemble de paramètres utilisés pour tester la performance est spécifié ci-dessous.

```python
# Paramètres de la grille pour les vectoriseurs (Count et TFIDF)
parameters_vect = {
    'features__pipe__vect__max_df': (0.25, 0.5, 0.75),
    'features__pipe__vect__ngram_range': ((1, 1), (1, 2)),
    'features__pipe__vect__min_df': (1,2)
}

# Paramètres de la grille pour MultinomialNB
parameters_mnb = {
    'clf__alpha': (0.25, 0.5, 0.75)
}

# Paramètres de la grille pour LogisticRegression
parameters_logreg = {
    'clf__C': (0.25, 0.5, 1.0),
    'clf__penalty': ('l1', 'l2')
}
```

## Classificateurs

Ici, nous allons comparer les performances d'un `MultinomialNB` et d'une `LogisticRegression`.

```python
mnb = MultinomialNB()
logreg = LogisticRegression()
```

### CountVectorizer

Pour utiliser des mots dans un classificateur, nous devons convertir les mots en nombres. Le `CountVectorizer` de Sklearn prend tous les mots dans tous les tweets, attribue un ID et compte la fréquence du mot par tweet. Nous utilisons ensuite ce sac de mots comme entrée pour un classificateur. Ce sac de mots est un ensemble de données clairsemé. Cela signifie que chaque enregistrement aura de nombreux zéros pour les mots n'apparaissant pas dans le tweet.

```python
countvect = CountVectorizer()
# MultinomialNB
best_mnb_countvect = grid_vect(mnb, parameters_mnb, X_train, X_test, parameters_text=parameters_vect, vect=countvect)
joblib.dump(best_mnb_countvect, '../output/best_mnb_countvect.pkl')
# LogisticRegression
best_logreg_countvect = grid_vect(logreg, parameters_logreg, X_train, X_test, parameters_text=parameters_vect, vect=countvect)
joblib.dump(best_logreg_countvect, '../output/best_logreg_countvect.pkl')
```

### TF-IDF Vectorizer

Un problème avec CountVectorizer est qu'il peut y avoir des mots qui apparaissent fréquemment. Ces mots peuvent ne pas avoir d'informations discriminatoires. Ainsi, ils peuvent être supprimés. [TF-IDF (fréquence de terme — fréquence inverse de document)](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) peut être utilisé pour réduire le poids de ces mots fréquents.

```python
tfidfvect = TfidfVectorizer()
# MultinomialNB
best_mnb_tfidf = grid_vect(mnb, parameters_mnb, X_train, X_test, parameters_text=parameters_vect, vect=tfidfvect)
joblib.dump(best_mnb_tfidf, '../output/best_mnb_tfidf.pkl')
# LogisticRegression
best_logreg_tfidf = grid_vect(logreg, parameters_mnb, X_train, X_test, parameters_text=parameters_vect, vect=tfidfvect)
joblib.dump(best_logreg_tfidf, '../output/best_logreg_tfidf.pkl')
```

### Word2Vec

Une autre façon de convertir les mots en valeurs numériques est d'utiliser `Word2Vec`. Word2Vec mappe chaque mot dans un espace multidimensionnel. Il le fait en tenant compte du contexte dans lequel un mot apparaît dans les tweets. En conséquence, les mots qui sont similaires sont également proches les uns des autres dans l'espace multidimensionnel.

L'algorithme Word2Vec fait partie du package [gensim](https://radimrehurek.com/gensim/models/word2vec.html).

L'algorithme Word2Vec utilise des listes de mots comme entrée. À cette fin, nous utilisons la méthode `word_tokenize` du package `nltk`.

```python
SIZE = 50
X_train['clean_text_wordlist'] = X_train.clean_text.apply(lambda x : word_tokenize(x))
X_test['clean_text_wordlist'] = X_test.clean_text.apply(lambda x : word_tokenize(x))
model = gensim.models.Word2Vec(X_train.clean_text_wordlist
, min_count=1
, size=SIZE
, window=5
, workers=4)
model.most_similar('plane', topn=3)
```

Le modèle Word2Vec fournit un vocabulaire des mots dans tous les tweets. Pour chaque mot, vous avez également ses valeurs de vecteur. Le nombre de valeurs de vecteur est égal à la taille choisie. Ce sont les dimensions sur lesquelles chaque mot est mappé dans l'espace multidimensionnel. Les mots avec une occurrence inférieure à `min_count` ne sont pas conservés dans le vocabulaire.

Un effet secondaire du paramètre min_count est que certains tweets pourraient ne pas avoir de valeurs de vecteur. Ce serait le cas lorsque le(s) mot(s) dans le tweet apparaissent dans moins de min_count tweets. En raison du petit corpus de tweets, il y a un risque que cela se produise dans notre cas. Ainsi, nous définissons la valeur min_count égale à 1.

Les tweets peuvent avoir un nombre différent de vecteurs, selon le nombre de mots qu'ils contiennent. Pour utiliser cette sortie pour la modélisation, nous allons calculer la moyenne de tous les vecteurs par tweet. Ainsi, nous aurons le même nombre (c'est-à-dire la taille) de variables d'entrée par tweet.

Nous faisons cela avec la fonction `compute_avg_w2v_vector`. Dans cette fonction, nous vérifions également si les mots dans le tweet apparaissent dans le vocabulaire du modèle Word2Vec. Si ce n'est pas le cas, une liste remplie de 0.0 est retournée. Sinon, la moyenne des vecteurs de mots.

```python
def compute_avg_w2v_vector(w2v_dict, tweet):
    list_of_word_vectors = [w2v_dict[w] for w in tweet if w in w2v_dict.vocab.keys()]
    
    if len(list_of_word_vectors) == 0:
        result = [0.0]*SIZE
    else:
        result = np.sum(list_of_word_vectors, axis=0) / len(list_of_word_vectors)
        
    return result
X_train_w2v = X_train['clean_text_wordlist'].apply(lambda x: compute_avg_w2v_vector(model.wv, x))
X_test_w2v = X_test['clean_text_wordlist'].apply(lambda x: compute_avg_w2v_vector(model.wv, x))
```

Cela nous donne une série avec un vecteur de dimension égale à `SIZE`. Maintenant, nous allons diviser ce vecteur et créer un DataFrame avec chaque valeur de vecteur dans une colonne séparée. De cette manière, nous pouvons concaténer les variables Word2Vec aux autres variables TextCounts. Nous devons réutiliser l'index de `X_train` et `X_test`. Sinon, cela posera des problèmes (doublons) dans la concaténation plus tard.

```python
X_train_w2v = pd.DataFrame(X_train_w2v.values.tolist(), index= X_train.index)
X_test_w2v = pd.DataFrame(X_test_w2v.values.tolist(), index= X_test.index)
# Concaténer avec les variables TextCounts
X_train_w2v = pd.concat([X_train_w2v, X_train.drop(['clean_text', 'clean_text_wordlist'], axis=1)], axis=1)
X_test_w2v = pd.concat([X_test_w2v, X_test.drop(['clean_text', 'clean_text_wordlist'], axis=1)], axis=1)
```

Nous ne considérons que la LogisticRegression car nous avons des valeurs négatives dans les vecteurs Word2Vec. MultinomialNB suppose que les variables ont une [distribution multinomiale](https://en.wikipedia.org/wiki/Multinomial_distribution). Elles ne peuvent donc pas contenir de valeurs négatives.

```python
best_logreg_w2v = grid_vect(logreg, parameters_logreg, X_train_w2v, X_test_w2v, is_w2v=True)
joblib.dump(best_logreg_w2v, '../output/best_logreg_w2v.pkl')
```

## Conclusion

* Les deux classificateurs obtiennent les meilleurs résultats en utilisant les caractéristiques du CountVectorizer
* La régression logistique surpasse le classificateur Naive Bayes multinomial
* La meilleure performance sur l'ensemble de test provient de la LogisticRegression avec les caractéristiques de CountVectorizer.

### Meilleurs paramètres

* Valeur C de 1
* Régularisation L2
* max_df : 0,5 ou fréquence maximale de document de 50 %.
* min_df : 1 ou les mots doivent apparaître dans au moins 2 tweets
* ngram_range : (1, 2), à la fois des mots uniques et des bi-grammes sont utilisés

### Métriques d'évaluation

* Une précision de test de 81,3 %. Cela est meilleur qu'une performance de base de prédiction de la classe majoritaire (ici un sentiment négatif) pour toutes les observations. La base donnerait 63 % de précision.
* La précision est plutôt élevée pour les trois classes. Par exemple, parmi tous les cas que nous prédisons comme négatifs, 80 % sont négatifs.
* Le rappel pour la classe neutre est faible. Parmi tous les cas neutres dans nos données de test, nous n'en prédisons que 48 % comme étant neutres.

## Appliquer le meilleur modèle sur de nouveaux tweets

Pour le plaisir, nous allons utiliser le meilleur modèle et l'appliquer à de nouveaux tweets qui contiennent _@VirginAmerica_. J'ai sélectionné 3 tweets négatifs et 3 tweets positifs à la main.

Grâce au GridSearchCV, nous savons maintenant quels sont les meilleurs hyperparamètres. Nous pouvons donc maintenant entraîner le meilleur modèle sur toutes les données d'entraînement, y compris les données de test que nous avons séparées auparavant.

```python
textcountscols = ['count_capital_words','count_emojis','count_excl_quest_marks','count_hashtags'
,'count_mentions','count_urls','count_words']
features = FeatureUnion([('textcounts', ColumnExtractor(cols=textcountscols))
, ('pipe', Pipeline([('cleantext', ColumnExtractor(cols='clean_text'))
, ('vect', CountVectorizer(max_df=0.5, min_df=1, ngram_range=(1,2)))]))]
, n_jobs=-1)
pipeline = Pipeline([
('features', features)
, ('clf', LogisticRegression(C=1.0, penalty='l2'))
])
best_model = pipeline.fit(df_model.drop('airline_sentiment', axis=1), df_model.airline_sentiment)
# Application sur de nouveaux tweets positifs
new_positive_tweets = pd.Series(["Thank you @VirginAmerica for you amazing customer support team on Tuesday 11/28 at @EWRairport and returning my lost bag in less than 24h! #efficiencyiskey #virginamerica"
,"Love flying with you guys ask these years. Sad that this will be the last trip ? @VirginAmerica #LuxuryTravel"
,"Wow @VirginAmerica main cabin select is the way to fly!! This plane is nice and clean & I have tons of legroom! Wahoo! NYC bound! \u2708\ufe0f"])
df_counts_pos = tc.transform(new_positive_tweets)
df_clean_pos = ct.transform(new_positive_tweets)
df_model_pos = df_counts_pos
df_model_pos['clean_text'] = df_clean_pos
best_model.predict(df_model_pos).tolist()
# Application sur de nouveaux tweets négatifs
new_negative_tweets = pd.Series(["@VirginAmerica shocked my initially with the service, but then went on to shock me further with no response to what my complaint was. #unacceptable @Delta @richardbranson"
,"@VirginAmerica this morning I was forced to repack a suitcase w a medical device because it was barely overweight - wasn't even given an option to pay extra. My spouses suitcase then burst at the seam with the added device and had to be taped shut. Awful experience so far!"
,"Board airplane home. Computer issue. Get off plane, traverse airport to gate on opp side. Get on new plane hour later. Plane too heavy. 8 volunteers get off plane. Ohhh the adventure of travel \u2708\ufe0f @VirginAmerica"])
df_counts_neg = tc.transform(new_negative_tweets)
df_clean_neg = ct.transform(new_negative_tweets)
df_model_neg = df_counts_neg
df_model_neg['clean_text'] = df_clean_neg
best_model.predict(df_model_neg).tolist()
```

Le modèle classe correctement tous les tweets. Un ensemble de test plus grand devrait être utilisé pour évaluer les performances du modèle. Mais sur cet ensemble de données réduit, il fait ce que nous visons. J'espère que vous avez apprécié la lecture de cette histoire. Si c'est le cas, n'hésitez pas à la partager.