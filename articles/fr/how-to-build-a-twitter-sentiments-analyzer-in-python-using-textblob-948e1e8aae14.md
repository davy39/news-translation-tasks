---
title: Comment construire un analyseur de sentiment Twitter en Python en utilisant
  TextBlob
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T16:00:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-twitter-sentiments-analyzer-in-python-using-textblob-948e1e8aae14
coverImage: https://cdn-media-1.freecodecamp.org/images/1*keGUEiFDKqcpXVGnfK1Xdg.png
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: Sentiment analysis
  slug: sentiment-analysis
- name: 'tech '
  slug: tech
seo_title: Comment construire un analyseur de sentiment Twitter en Python en utilisant
  TextBlob
seo_desc: 'By Arun Mathew Kurian

  This blog is based on the video Twitter Sentiment Analysis — Learn Python for Data
  Science #2 by Siraj Raval. In this challenge, we will be building a sentiment analyzer
  that checks whether tweets about a subject are negative or...'
---

Par Arun Mathew Kurian

Ce blog est basé sur la vidéo [Twitter Sentiment Analysis — Learn Python for Data Science #2](https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU) de Siraj Raval. Dans ce défi, nous allons construire un analyseur de sentiment qui vérifie si les tweets sur un sujet sont négatifs ou positifs. Nous allons utiliser la bibliothèque Python textblob pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/tP3mRr3cKmn9tJ8tua6Rp2ffqIrJk0e9FwMM)
_image de google_

L'analyse de sentiment, également appelée fouille d'opinions ou IA émotionnelle, est le processus de détermination si un texte est positif, négatif ou neutre. Un cas d'utilisation courant pour cette technologie est de découvrir comment les gens se sentent à propos d'un sujet particulier. L'analyse de sentiment est largement appliquée aux avis et aux médias sociaux pour diverses applications.

L'analyse de sentiment peut être réalisée de nombreuses manières différentes. De nombreuses marques et marketeurs utilisent des outils basés sur des mots-clés qui classent les données (c'est-à-dire sociales, nouvelles, avis, blog, etc.) comme positives/négatives/neutres.

Le marquage automatique des sentiments est généralement réalisé grâce à des listes de mots. Par exemple, les mentions de 'haine' seraient marquées négativement.

Il peut y avoir deux approches pour l'analyse de sentiment.

1. Méthodes basées sur le lexique
2. Méthodes basées sur l'apprentissage automatique.

Dans ce problème, nous utiliserons une méthode basée sur le lexique.

Les méthodes basées sur le lexique définissent une liste de mots positifs et négatifs, avec une valence (par exemple, 'nice' : +2, 'good' : +1, 'terrible' : -1.5, etc.). L'algorithme recherche dans un texte tous les mots connus. Il combine ensuite leurs résultats individuels en les additionnant ou en les moyennant. Certaines extensions peuvent vérifier certaines règles grammaticales, comme la négation ou le modificateur de sentiment (comme le mot 'but', qui pondère différemment les valeurs de sentiment dans le texte, pour mettre l'accent sur la fin du texte).

Construisons maintenant l'analyseur.

#### API Twitter

Avant de commencer à coder, nous devons nous enregistrer pour l'API Twitter [https://apps.twitter.com/](https://apps.twitter.com/). Ici, nous devons enregistrer une application pour générer diverses clés associées à notre API. L'API Twitter peut être utilisée pour effectuer de nombreuses actions comme créer et rechercher.

Maintenant, après avoir créé l'application, nous pouvons commencer à coder.

Nous devons installer deux packages :

> pip install tweepy

Ce package sera utilisé pour gérer l'API Twitter.

> pip install textblob

Ce package sera utilisé pour l'analyse de sentiment.

**sentiment_analyzer.py**

```
import tweepy
from textblob import TextBlob
```

Nous devons déclarer les variables pour stocker les différentes clés associées à l'API Twitter.

```
consumer_key = '[consumer_key]'
```

```
consumer_key_secret = '[consumer_key_secret]'
```

```
access_token = '[access_token]'
```

```
access_token_secret = '[access_token_secret]'
```

L'étape suivante consiste à créer une connexion avec l'API Twitter en utilisant **tweepy** avec ces jetons.

#### **Tweepy**

Tweepy supporte l'authentification OAuth. L'authentification est gérée par la classe **tweepy.OAuthHandler**.

Une instance **OAuthHandler** doit être créée en passant un jeton de consommateur et un secret.

Sur cette instance d'authentification, nous appellerons une fonction set_access_token en passant l'access_token et l'access_token_secret.

Enfin, nous créons notre instance d'API tweepy en passant cette instance d'authentification à la fonction API de tweepy.

```
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
```

```
auth.set_access_token(access_token, access_token_secret)
```

```
api = tweepy.API(auth)
```

Nous pouvons maintenant rechercher sur Twitter n'importe quel sujet en utilisant la méthode de recherche de l'API.

```
public_tweets = api.search('Dogs')
```

Maintenant, nous allons obtenir tous les tweets liés au sujet 'Dogs'. Nous pouvons effectuer une analyse de sentiment en utilisant la bibliothèque textblob.

#### TextBlob

_TextBlob_ est une bibliothèque Python (2 et 3) pour le traitement des données textuelles. Elle fournit une API simple pour plonger dans les tâches courantes de traitement du langage naturel (NLP) telles que l'étiquetage des parties du discours, l'extraction de phrases nominales, l'analyse de sentiment, la classification, la traduction, et plus encore.

Un textblob peut être créé de la manière suivante (exemple, et non partie du code original) :

```
exemple = TextBlob("Python est un langage de programmation de haut niveau, généraliste.")
```

Et la **tokenization** peut être effectuée par les méthodes suivantes :

**words** : retourne les mots du texte

usage :

```
exemple.words
```

**sentences** : retourne les phrases du texte

usage :

```
exemple.sentences
```

#### **Étiquetage des parties du discours**

Les étiquettes des parties du discours peuvent être accessibles via la propriété **tags**.

```
wiki.tags[('Python', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('high-level', 'JJ'), ('general-purpose', 'JJ'), ('programming', 'NN'), ('language', 'NN')]
```

#### **Analyse de sentiment**

La propriété sentiment retourne un tuple nommé de la forme Sentiment (polarité, subjectivité). Le score de polarité est un float dans la plage [-1.0, 1.0]. La subjectivité est un float dans la plage [0.0, 1.0] où 0.0 est très objectif et 1.0 est très subjectif.

Retour au code.

Nous pouvons itérer sur le tableau **publice_tweets**, et vérifier le sentiment du texte de chaque tweet en fonction de la polarité.

```
for tweet in public_tweets:    print(tweet.text)    analysis = TextBlob(tweet.text)    print(analysis.sentiment)    if analysis.sentiment[0]>0:       print 'Positif'    elif analysis.sentiment[0]<0:       print 'Négatif'    else:       print 'Neutre'
```

Maintenant, nous exécutons le code en utilisant la commande suivante :

> python sentiment_analyzer.py

et nous obtenons le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/PE7et-Tuo1r2fw06stPrG2Dq4KgWlFA0pHaA)

Nous pouvons voir que le sentiment du tweet est affiché.

Ceci est un exemple de la manière dont l'analyse de sentiment peut être effectuée sur des données provenant des médias sociaux comme Twitter. J'espère que vous le trouverez utile !

Trouvez le code à l'adresse [https://github.com/amkurian/twitter_sentiment_challenge](https://github.com/amkurian/twitter_sentiment_challenge)