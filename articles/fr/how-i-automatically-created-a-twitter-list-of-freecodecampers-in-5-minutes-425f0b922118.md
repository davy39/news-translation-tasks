---
title: Comment j'ai automatiquement créé une Liste Twitter de FreeCodeCampers en 5
  minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T23:20:25.000Z'
originalURL: https://freecodecamp.org/news/how-i-automatically-created-a-twitter-list-of-freecodecampers-in-5-minutes-425f0b922118
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mUQDjnECZGSncv_imkD3yA.jpeg
tags:
- name: coding
  slug: coding
- name: freeCodeCamp.org
  slug: freecodecamp
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Twitter
  slug: twitter
seo_title: Comment j'ai automatiquement créé une Liste Twitter de FreeCodeCampers
  en 5 minutes
seo_desc: 'By Monica Powell

  Using Twython Twitter API wrapper to add users to a Twitter List


  We are going to create a Python script that will automatically search Twitter for
  individuals who use the #freeCodeCamp hashtag and add them to a Twitter list of
  “Free...'
---

Par Monica Powell

#### Utilisation de l'API Twython Twitter pour ajouter des utilisateurs à une Liste Twitter

![Image](https://cdn-media-1.freecodecamp.org/images/1*mUQDjnECZGSncv_imkD3yA.jpeg)

Nous allons créer un script Python qui recherchera automatiquement sur Twitter les individus utilisant le hashtag **#freeCodeCamp** et les ajoutera à une liste Twitter de « FreeCodeCampers ». Les [listes Twitter](https://help.twitter.com/en/using-twitter/twitter-lists) permettent de regrouper des individus sur Twitter et de collecter tous leurs tweets dans un flux, sans avoir à suivre chaque compte individuel. Les listes Twitter peuvent contenir jusqu'à 5 000 comptes Twitter individuels.

Nous pouvons accomplir cela en suivant ces étapes :

* Installer les packages Python nécessaires
* Enregistrer une application auprès de Twitter
* Générer et accéder à nos identifiants Twitter
* Effectuer des appels API Twitter [Search](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets) et [List](https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-list)

Alors, commençons.

### 1. Installer les packages Python nécessaires

Créez un fichier nommé `addToFreeCodeCampList.py`, qui contiendra notre script principal, puis importez deux modules Python dans ce fichier :

* **Import Config** : Dans le même répertoire que notre script `addToFreeCodeCampList.py`, créez un fichier nommé `config.py` qui stocke nos identifiants confidentiels de l'API Twitter. Nous allons importer nos identifiants API depuis ce fichier dans notre script `addToFreeCodeCampList.py` en incluant la ligne `import config`. Twitter nécessite une clé API valide, un secret API, un jeton d'accès et un secret de jeton pour toutes les requêtes API.
* **Import Twython** : [Twython](https://github.com/ryanmcgrath/twython) est un wrapper Python pour l'API Twitter qui facilite l'accès et la manipulation programmatiques des données de Twitter en utilisant Python. Nous pouvons importer Twython avec la ligne suivante `from twython import Twython, TwythonError`.

Votre script `addToFreeCodeCampList.py` devrait maintenant ressembler à ceci.

```
import config
from twython import Twython, TwythonError
```

### 2. Enregistrer une application auprès de Twitter

Nous devons authentifier notre application pour accéder à l'API Twitter. Vous devez avoir un compte Twitter pour accéder au [site de gestion des applications de Twitter](https://apps.twitter.com/). Le site de gestion des applications est l'endroit où vous pouvez visualiser/modifier/créer des clés API, des secrets API, des jetons d'accès et des secrets de jetons.

1. Pour créer ces identifiants, nous devons créer une application Twitter. Allez sur le site de gestion des applications et cliquez sur « Create New App ». Cela devrait vous diriger vers une page similaire à celle ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H8TiOR6qnIXo_sNoRb7OGw.png)

2. Remplissez les champs obligatoires et cliquez sur « Create your Twitter application ». Vous serez alors redirigé vers une page avec les détails de votre application.

### 3. Générer et accéder à nos identifiants Twitter

1. Cliquez sur l'onglet « Keys and Access Tokens » et copiez la « Consumer Key (API Key) » et la « Consumer Secret (API Secret) » dans le fichier `config.py`
2. Faites défiler jusqu'en bas de la page et cliquez sur « Create my access token ». Copiez le « Access Token » et le « Access Token Secret » générés dans le fichier `config.py`.

Pour référence, je recommande de formater votre config.py de manière similaire au fichier ci-dessous :

3. Actuellement, tous nos identifiants Twitter se trouvent dans notre fichier `config.py` et nous avons importé `config` dans notre fichier `addToFreeCodeCampList.py`. Cependant, nous n'avons pas encore passé d'informations entre les fichiers.

Changeons cela en créant un objet Twython et en passant la clé API nécessaire, les secrets API et le jeton API de notre fichier `config.py` avec ce qui suit :

```
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
```

Le fichier `addToFreeCodeCampList.py` devrait maintenant ressembler à ceci :

```
import config
```

```
from twython import Twython, TwythonError
```

```
# créer un objet Twython en passant les mots de passe secrets nécessaires
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
```

### 4. Effectuer des appels API Twitter Search et List

1. Faisons un appel API pour rechercher sur Twitter et retourner les 100 tweets les plus récents (à l'exclusion des retweets) contenant « #freeCodeCamp » :

```
# retourner les tweets contenant #FreeCodeCamp
response = twitter.search(q='#FreeCodeCamp -filter:retweets', result_type='recent', count=100)
```

2. Regarder les tweets retournés par notre recherche

```
# pour chaque tweet retourné par la recherche de #FreeCodeCamp
for tweet in response['statuses']:
    # imprimer les infos du tweet si nécessaire pour le débogage
    print(tweet)
    print(tweet['user']['screen_name'])
```

Un seul tweet retourné par cet appel API ressemble à ceci en JSON :

```
{'created_at': 'Sun Dec 24 00:23:05 +0000 2017', 'id': 944725078763298816, 'id_str': '944725078763298816', 'text': 'Why is it so hard to wrap my head around node/express. Diving in just seems so overwhelming. Templates, forms, post… https://t.co/ae52rro63i', 'truncated': True, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/ae52rro63i', 'expanded_url': 'https://twitter.com/i/web/status/944725078763298816', 'display_url': 'twitter.com/i/web/status/9…', 'indices': [117, 140]}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 48602981, 'id_str': '48602981', 'name': 'Matt Huberty', 'screen_name': 'MattHuberty', 'location': 'Oxford, MS', 'description': "I'm a science and video game loving eagle scout with a Microbio degree from UF. Nowadays I'm working on growing my tutoring business at Ole Miss. Link below!", 'url': 'https://t.co/dfuqNNoBYZ', 'entities': {'url': {'urls': [{'url': 'https://t.co/dfuqNNoBYZ', 'expanded_url': 'http://www.thetutorcrew.com', 'display_url': 'thetutorcrew.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 42, 'friends_count': 121, 'listed_count': 4, 'created_at': 'Fri Jun 19 04:00:44 +0000 2009', 'favourites_count': 991, 'utc_offset': -28800, 'time_zone': 'Pacific Time (US & Canada)', 'geo_enabled': False, 'verified': False, 'statuses_count': 199, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/777294001598758912/FVOIrnb4_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/777294001598758912/FVOIrnb4_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/48602981/1431670621', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 1, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}
MattHuberty
```

et à ceci sur Twitter.com :

3. Ajouter les auteurs de tweets à notre liste Twitter

Pour ajouter l'auteur du tweet à notre liste Twitter, nous avons besoin du nom d'utilisateur associé au tweet `tweet['user']['screen_name']`

Essayons d'ajouter les utilisateurs de ces tweets à notre liste Twitter « FreeCodeCampers ». J'ai créé ma liste Twitter à l'adresse [https://twitter.com/waterproofheart/lists/freecodecampers](https://twitter.com/waterproofheart/lists/freecodecampers), ce qui signifie que pour mon script, le slug est `freecodecampers` et le `owner_screen_name` est le mien, waterproofheart.

```
for tweet in response['statuses']:
```

```
# essayer d'ajouter chaque utilisateur ayant tweeté le hashtag à la liste
try:
    twitter.add_list_member(slug='YOUR_LIST_SLUG', owner_screen_name='YOUR_USERNAME', screen_name=tweet['user']['screen_name'])
```

```
# si pour une raison quelconque Twython ne peut pas ajouter l'utilisateur à la liste, imprimer le message d'exception
except TwythonError as e:
    print(e)
```

Vous pouvez créer votre propre liste Twitter en naviguant vers votre profil Twitter, en cliquant sur « Lists » sur le bureau et en cliquant sur le côté droit pour « Create new list ». Consultez la [documentation officielle des listes Twitter](https://help.twitter.com/en/using-twitter/twitter-lists) pour plus d'informations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TPUBuOqUwh_WXUNrUu6MyA.png)

Vous pouvez tester votre script en exécutant `python addToFreeCodeCampList.py` dans le terminal.

Mon script final ressemble à ceci :

Ce script peut être configuré pour s'exécuter automatiquement en local ou à distance via un [cron job](https://en.wikipedia.org/wiki/Cron), ce qui permet d'effectuer des tâches selon un calendrier défini.

N'hésitez pas à commenter ci-dessous ou à [me tweeter](https://twitter.com/waterproofheart) si vous avez des questions, des suggestions ou si vous souhaitez partager comment vous avez modifié ce script !

*Si vous avez aimé lire cet article, envisagez d'appuyer sur le bouton d'applaudissements ?. Vous voulez voir plus de mon travail ? Consultez m[on GitHub](https://github.com/M0nica/) pour voir mon code et en savoir plus sur mon expérience de développement sur h[ttp://aboutmonica.com](http://aboutmonica.com).*