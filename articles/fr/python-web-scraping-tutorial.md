---
title: Web Scraping avec Python – Comment extraire des données de Twitter en utilisant
  Tweepy et Snscrape
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-07-12T17:58:29.000Z'
originalURL: https://freecodecamp.org/news/python-web-scraping-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/scraping-with-python-article-image.jpeg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Web Scraping avec Python – Comment extraire des données de Twitter en utilisant
  Tweepy et Snscrape
seo_desc: 'If you are a data enthusiast, you''ll likely agree that one of the richest
  sources of real-world data is social media. Sites like Twitter are full of data.

  You can use the data you can get from social media in a number of ways, like sentiment
  analysis...'
---

Si vous êtes un passionné de données, vous serez probablement d'accord pour dire que l'une des sources les plus riches de données réelles est les réseaux sociaux. Des sites comme Twitter regorgent de données.

Vous pouvez utiliser les données que vous pouvez obtenir à partir des réseaux sociaux de plusieurs manières, comme l'analyse de sentiment (analyser les pensées des gens) sur un sujet spécifique ou un domaine d'intérêt.

Il existe plusieurs façons d'extraire (ou de collecter) des données de Twitter. Et dans cet article, nous allons examiner deux de ces méthodes : en utilisant Tweepy et Snscrape.

Nous allons apprendre une méthode pour extraire des conversations publiques de personnes sur un sujet tendance spécifique, ainsi que des tweets d'un utilisateur particulier.

Maintenant, sans plus attendre, commençons.

## Tweepy vs Snscrape – Introduction à nos outils de scraping

Avant de passer à l'implémentation de chaque plateforme, essayons de comprendre les différences et les limites de chaque plateforme.

### Tweepy

Tweepy est une bibliothèque Python pour s'intégrer avec l'API Twitter. Parce que Tweepy est connecté avec l'API Twitter, vous pouvez effectuer des requêtes complexes en plus de l'extraction de tweets. Il vous permet de tirer parti de toutes les capacités de l'API Twitter.

Mais il y a quelques inconvénients – comme le fait que son API standard ne vous permet de collecter des tweets que pour une semaine (c'est-à-dire que Tweepy ne permet pas de récupérer des tweets au-delà d'une fenêtre d'une semaine, donc la récupération de données historiques n'est pas autorisée).

De plus, il y a des limites au nombre de tweets que vous pouvez récupérer à partir du compte d'un utilisateur. Vous pouvez [en savoir plus sur les fonctionnalités de Tweepy ici](https://www.tweepy.org/).

### Snscrape

Snscrape est une autre approche pour extraire des informations de Twitter qui ne nécessite pas l'utilisation d'une API. Snscrape vous permet d'extraire des informations de base telles que le profil d'un utilisateur, le contenu des tweets, la source, et ainsi de suite.

Snscrape n'est pas limité à Twitter, mais peut également extraire du contenu d'autres réseaux sociaux importants comme Facebook, Instagram, et autres.

Ses avantages sont qu'il n'y a pas de limites au nombre de tweets que vous pouvez récupérer ou à la fenêtre de tweets (c'est-à-dire la plage de dates des tweets). Ainsi, Snscrape vous permet de récupérer des données anciennes.

Mais l'un des inconvénients est qu'il manque toutes les autres fonctionnalités de Tweepy – encore, si vous voulez seulement extraire des tweets, Snscrape serait suffisant.

Maintenant que nous avons clarifié la distinction entre les deux méthodes, passons en revue leur implémentation une par une.

## Comment utiliser Tweepy pour extraire des tweets

Avant de commencer à utiliser Tweepy, nous devons d'abord nous assurer que nos identifiants Twitter sont prêts. Avec cela, nous pouvons connecter Tweepy à notre clé API et commencer l'extraction.

Si vous n'avez pas d'identifiants Twitter, vous pouvez vous inscrire pour un compte développeur Twitter en allant [ici](https://developer.twitter.com/). On vous posera quelques questions de base sur la manière dont vous prévoyez d'utiliser l'API Twitter. Après cela, vous pouvez commencer l'implémentation.

La première étape consiste à installer la bibliothèque Tweepy sur votre machine locale, ce que vous pouvez faire en tapant :

```javascript
pip install git+https://github.com/tweepy/tweepy.git
```

### Comment extraire des tweets d'un utilisateur sur Twitter

Maintenant que nous avons installé la bibliothèque Tweepy, extrayons 100 tweets d'un utilisateur appelé `john` sur Twitter. Nous allons examiner l'implémentation complète du code qui nous permettra de faire cela et en discuter en détail afin de comprendre ce qui se passe :

```python
import tweepy

consumer_key = "XXXX" #Votre clé API/Consumer key 
consumer_secret = "XXXX" #Votre clé secrète API/Consumer Secret Key
access_token = "XXXX"    #Votre clé de jeton d'accès
access_token_secret = "XXXX" #Votre clé secrète de jeton d'accès

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


username = "john"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
```

Maintenant, passons en revue chaque partie du code dans le bloc ci-dessus.

```python
import tweepy

consumer_key = "XXXX" #Votre clé API/Consumer key 
consumer_secret = "XXXX" #Votre clé secrète API/Consumer Secret Key
access_token = "XXXX"    #Votre clé de jeton d'accès
access_token_secret = "XXXX" #Votre clé secrète de jeton d'accès

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)
```

Dans le code ci-dessus, nous avons importé la bibliothèque Tweepy dans notre code, puis nous avons créé quelques variables où nous stockons nos identifiants Twitter (Le gestionnaire d'authentification Tweepy nécessite quatre de nos identifiants Twitter). Nous avons ensuite passé ces variables dans le gestionnaire d'authentification Tweepy et les avons enregistrées dans une autre variable.

Ensuite, la dernière instruction d'appel est celle où nous avons instancié l'API Tweepy et passé les paramètres requis.

```python
username = "john"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
```

Dans le code ci-dessus, nous avons créé le nom de l'utilisateur (le @nom dans Twitter) dont nous voulons récupérer les tweets ainsi que le nombre de tweets. Nous avons ensuite créé un gestionnaire d'exceptions pour nous aider à attraper les erreurs de manière plus efficace.

Après cela, `api.user_timeline()` retourne une collection des tweets les plus récents postés par l'utilisateur que nous avons choisi dans le paramètre `screen_name` et le nombre de tweets que vous voulez récupérer.

Dans la ligne de code suivante, nous avons passé certains attributs que nous voulons récupérer de chaque tweet et les avons enregistrés dans une liste. Pour voir plus d'attributs que vous pouvez récupérer d'un tweet, lisez [ceci](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline).

Dans le dernier bloc de code, nous avons créé un dataframe et passé la liste que nous avons créée ainsi que les noms des colonnes que nous avons créées.

Notez que les noms des colonnes doivent être dans la séquence de la manière dont vous les avez passés dans le conteneur d'attributs (c'est-à-dire, la manière dont vous avez passé ces attributs dans une liste lorsque vous récupériez les attributs du tweet).

Si vous avez correctement suivi les étapes que j'ai décrites, vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-17.png align="left")

*Image par l'Auteur*

Maintenant que nous avons terminé, passons à un autre exemple avant de passer à l'implémentation de Snscrape.

### Comment extraire des tweets à partir d'une recherche de texte

Dans cette méthode, nous allons récupérer un tweet en fonction d'une recherche. Vous pouvez faire cela comme suit :

```python
import tweepy

consumer_key = "XXXX" #Votre clé API/Consumer key 
consumer_secret = "XXXX" #Votre clé secrète API/Consumer Secret Key
access_token = "XXXX"    #Votre clé de jeton d'accès
access_token_secret = "XXXX" #Votre clé secrète de jeton d'accès

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "sex for grades"
no_of_tweets =150


try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
```

Le code ci-dessus est similaire au code précédent, sauf que nous avons changé la méthode de l'API de `api.user_timeline()` à `api.search_tweets()`. Nous avons également ajouté `tweet.user.name` à la liste des conteneurs d'attributs.

Dans le code ci-dessus, vous pouvez voir que nous avons passé deux attributs. Cela est dû au fait que si nous passons uniquement `tweet.user`, il ne retournera qu'un objet dictionnaire utilisateur. Nous devons donc également passer un autre attribut que nous voulons récupérer de l'objet utilisateur, qui est `name`.

Vous pouvez aller [ici](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user) pour voir une liste d'attributs supplémentaires que vous pouvez récupérer d'un objet utilisateur. Maintenant, vous devriez voir quelque chose comme ceci une fois que vous l'exécutez :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-18.png align="left")

*Image par l'Auteur.*

D'accord, cela conclut à peu près l'implémentation de Tweepy. Rappelez-vous simplement qu'il y a une limite au nombre de tweets que vous pouvez récupérer, et vous ne pouvez pas récupérer de tweets de plus de 7 jours avec Tweepy.

## Comment utiliser Snscrape pour extraire des tweets

Comme je l'ai mentionné précédemment, Snscrape ne nécessite pas d'identifiants Twitter (clé API) pour y accéder. Il n'y a également aucune limite au nombre de tweets que vous pouvez récupérer.

Pour cet exemple, cependant, nous allons simplement récupérer les mêmes tweets que dans l'exemple précédent, mais en utilisant Snscrape à la place.

Pour utiliser Snscrape, nous devons d'abord installer sa bibliothèque sur notre PC. Vous pouvez le faire en tapant :

```javascript
pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```

### Comment extraire des tweets d'un utilisateur avec Snscrape

Snscrape inclut deux méthodes pour obtenir des tweets de Twitter : l'interface de ligne de commande (CLI) et un wrapper Python. Gardez simplement à l'esprit que le wrapper Python est actuellement non documenté – mais nous pouvons encore nous en sortir avec des essais et des erreurs.

Dans cet exemple, nous allons utiliser le wrapper Python car il est plus intuitif que la méthode CLI. Mais si vous êtes bloqué avec un code, vous pouvez toujours vous tourner vers la communauté GitHub pour obtenir de l'aide. Les contributeurs seront heureux de vous aider.

Pour récupérer des tweets d'un utilisateur particulier, nous pouvons faire ce qui suit :

```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
```

Passons en revue certaines parties du code que vous pourriez ne pas comprendre au premier abord :

```python
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
  
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
```

Dans le code ci-dessus, ce que fait `sntwitter.TwitterSearchScraper` est de retourner un objet de tweets à partir du nom de l'utilisateur que nous lui avons passé (qui est john).

Comme je l'ai mentionné précédemment, Snscrape n'a pas de limites sur le nombre de tweets, donc il retournera autant de tweets de cet utilisateur. Pour gérer cela, nous devons ajouter la fonction enumerate qui va itérer à travers l'objet et ajouter un compteur afin que nous puissions accéder aux 100 tweets les plus récents de l'utilisateur.

Vous pouvez voir que la syntaxe des attributs que nous obtenons de chaque tweet ressemble à celle de Tweepy. Voici la liste des attributs que nous pouvons obtenir du tweet Snscrape, qui a été compilée par Martin Beck.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Sns.Scrape.png align="left")

*Crédit : Martin Beck*

D'autres attributs pourraient être ajoutés, car la bibliothèque Snscrape est encore en développement. Par exemple, dans l'image ci-dessus, `source` a été remplacé par `sourceLabel`. Si vous passez uniquement `source`, il retournera un objet.

Si vous exécutez le code ci-dessus, vous devriez voir quelque chose comme ceci également :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-19.png align="left")

*Image par l'Auteur*

Maintenant, faisons de même pour l'extraction par recherche.

### Comment extraire des tweets à partir d'une recherche de texte avec Snscrape

```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
```

Encore une fois, vous pouvez accéder à beaucoup de données historiques en utilisant Snscrape (contrairement à Tweepy, car son API standard ne peut pas dépasser 7 jours. L'API premium est de 30 jours.). Nous pouvons donc passer la date à partir de laquelle nous voulons commencer la recherche et la date à laquelle nous voulons qu'elle se termine dans la méthode `sntwitter.TwitterSearchScraper()`.

Ce que nous avons fait dans le code précédent est essentiellement ce dont nous avons discuté auparavant. La seule chose à garder à l'esprit est que until fonctionne de manière similaire à la fonction range en Python (c'est-à-dire qu'elle exclut le dernier entier). Donc, si vous voulez obtenir des tweets d'aujourd'hui, vous devez inclure le jour suivant aujourd'hui dans le paramètre "until".

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-21.png align="left")

*Image de l'Auteur.*

Maintenant, vous savez également comment extraire des tweets avec Snscrape !

### Quand utiliser chaque approche

Maintenant que nous avons vu comment chaque méthode fonctionne, vous vous demandez peut-être quand utiliser laquelle.

Eh bien, il n'y a pas de règle universelle pour savoir quand utiliser chaque méthode. Tout dépend d'une question de préférence et de votre cas d'utilisation.

Si vous voulez acquérir un nombre illimité de tweets, vous devriez utiliser Snscrape. Mais si vous voulez utiliser des fonctionnalités supplémentaires que Snscrape ne peut pas fournir (comme la géolocalisation, par exemple), alors vous devriez définitivement utiliser Tweepy. Il est directement intégré avec l'API Twitter et offre une fonctionnalité complète.

Néanmoins, Snscrape est la méthode la plus couramment utilisée pour le scraping de base.

# Conclusion

Dans cet article, nous avons appris comment extraire des données de Python en utilisant Tweepy et Snscrape. Mais ceci n'était qu'un bref aperçu de la manière dont chaque approche fonctionne. Vous pouvez en apprendre plus en explorant le web pour des informations supplémentaires.

J'ai inclus quelques ressources utiles que vous pouvez utiliser si vous avez besoin d'informations supplémentaires. Merci d'avoir lu.

%[https://github.com/JustAnotherArchivist/snscrape] 

%[https://docs.tweepy.org/en/stable/index.html] 

%[https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af]