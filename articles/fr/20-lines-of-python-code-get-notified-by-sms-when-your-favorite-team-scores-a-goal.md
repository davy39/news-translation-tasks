---
title: 'Un projet Python en 30 lignes de code : comment configurer une notification
  SMS lorsque votre streamer Twitch préféré est en direct'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-15T14:53:06.000Z'
originalURL: https://freecodecamp.org/news/20-lines-of-python-code-get-notified-by-sms-when-your-favorite-team-scores-a-goal
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0d8740569d1a4ca4b21.jpg
tags:
- name: api
  slug: api
- name: Heroku
  slug: heroku
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: 'Un projet Python en 30 lignes de code : comment configurer une notification
  SMS lorsque votre streamer Twitch préféré est en direct'
seo_desc: 'By Pierre de Wulf

  Hi everyone :) Today I am beginning a new series of posts specifically aimed at
  Python beginners. The concept is rather simple: I''ll do a fun project, in as few
  lines of code as possible, and will try out as many new tools as possib...'
---

Par Pierre de Wulf

Bonjour à tous :) Aujourd'hui, je commence une nouvelle série d'articles spécialement destinée aux débutants en Python. Le concept est plutôt simple : je vais réaliser un projet amusant, en aussi peu de lignes de code que possible, et essayer autant d'outils nouveaux que possible.

Par exemple, aujourd'hui, nous allons apprendre à utiliser l'API Twilio, l'API Twitch, et nous verrons comment déployer le projet sur Heroku. Je vais vous montrer comment vous pouvez avoir votre propre notificateur SMS "Twitch Live", en 30 lignes de code, et pour 12 centimes par mois.

**Prérequis** : Vous devez simplement savoir comment exécuter Python sur votre machine et quelques commandes de base dans git (commit & push). Si vous avez besoin d'aide pour cela, je peux vous recommander ces 2 articles :

[Guide d'installation et de configuration de Python 3](https://realpython.com/installing-python/)

[Le tutoriel ultime des commandes Git pour débutants](https://www.freecodecamp.org/news/git-commands/) de [Adrian Hajdin](https://www.freecodecamp.org/news/author/adrianhajdin/).

**Ce que vous allez apprendre** :

* API Twitch
* API Twilio
* Déploiement sur Heroku
* Configuration d'un planificateur sur Heroku

**Ce que vous allez construire** :

Les spécifications sont simples : nous voulons recevoir un SMS dès qu'un streamer Twitch spécifique est en direct. Nous voulons savoir quand cette personne commence à streamer et quand elle arrête. Nous voulons que tout cela fonctionne automatiquement, toute la journée.

Nous allons diviser le projet en 3 parties. Tout d'abord, nous verrons comment savoir programmatiquement si un streamer Twitch particulier est en ligne. Ensuite, nous verrons comment recevoir un SMS lorsque cela se produit. Nous terminerons en voyant comment faire fonctionner ce code toutes les X minutes, afin de ne plus jamais manquer un moment de la vie de notre streamer préféré.

# Ce streamer Twitch est-il en direct ?

Pour savoir si un streamer Twitch est en direct, nous pouvons faire deux choses : nous pouvons aller sur l'URL du streamer et essayer de voir si le badge "Live" est présent.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Capture-d-e-cran-2019-08-14-a--15.49.31.png)
_Capture d'écran d'un streamer Twitch en direct._

Ce processus implique le scraping et n'est pas facilement réalisable en Python en moins de 20 lignes de code. Twitch exécute beaucoup de code JS et une simple requête request.get() ne suffira pas.

Pour que le scraping fonctionne dans ce cas, nous devrions scraper cette page dans Chrome pour obtenir le même contenu que ce que vous voyez dans la capture d'écran. C'est faisable, mais cela prendra beaucoup plus de 30 lignes de code. Si vous souhaitez en savoir plus, n'hésitez pas à consulter mon récent [guide de web scraping sans se faire bloquer](https://www.daolf.com/posts/avoiding-being-blocked-while-scraping-ultimate-guide/). (J'ai récemment lancé ScrapingBee, un [outil de web scraping](https://www.scrapingbee.com/blog/web-scraping-tools/), d'où ma connaissance dans le domaine ;))

Au lieu d'essayer de scraper Twitch, nous allons utiliser leur API. Pour ceux qui ne sont pas familiers avec le terme, une API est une interface programmatique qui permet aux sites web d'exposer leurs fonctionnalités et données à quiconque, principalement aux développeurs. Dans le cas de Twitch, leur API est exposée via HTTP, ce qui signifie que nous pouvons obtenir beaucoup d'informations et faire beaucoup de choses en faisant simplement une requête HTTP.

## Obtenez votre clé API

Pour cela, vous devez d'abord créer une clé API Twitch. De nombreux services imposent une authentification pour leurs API afin de s'assurer que personne n'en abuse ou pour restreindre l'accès à certaines fonctionnalités par certaines personnes.

Veuillez suivre ces étapes pour obtenir votre clé API :

* Créez un compte Twitch
* Créez maintenant un compte [dev Twitch](https://dev.twitch.tv/) -> "Signing up with Twitch" en haut à droite
* Allez sur votre "dashboard" une fois connecté
* "Register your application"
* Nom -> Peu importe, URL de redirection Oauth -> http://localhost, Catégorie -> Peu importe

Vous devriez maintenant voir, en bas de votre écran, votre client-id. Gardez cela pour plus tard.

## Ce streamer Twitch est-il en direct maintenant ?

Avec votre clé API en main, nous pouvons maintenant interroger l'API Twitch pour obtenir les informations que nous voulons, alors commençons à coder. Le snippet suivant consomme simplement l'API Twitch avec les bons paramètres et imprime la réponse.

```python
# requests est le package à utiliser en python pour faire des requêtes http
# https://2.python-requests.org/en/master/
import requests

# C'est l'une des routes où Twitch expose des données,
# Ils en ont beaucoup plus : https://dev.twitch.tv/docs
endpoint = "https://api.twitch.tv/helix/streams?"

# Pour s'authentifier, nous devons passer notre clé api via l'en-tête
headers = {"Client-ID": "<YOUR-CLIENT-ID>"}

# Le endpoint précédemment défini a besoin de certains paramètres, ici, le streamer Twitch que nous voulons suivre
# Avertissement, je ne sais même pas qui c'est, mais il était le premier sur Twitch à avoir un stream en direct afin que je puisse avoir de beaux exemples
params = {"user_login": "Solary"}

# Il est maintenant temps de faire la requête réelle
response = request.get(endpoint, params=params, headers=headers)
print(response.json())
```

La sortie devrait ressembler à ceci :

```json
{
   'data':[
      {
         'id':'35289543872',
         'user_id':'174955366',
         'user_name':'Solary',
         'game_id':'21779',
         'type':'live',
         'title':"Wakz duoQ w/ Tioo - GM 400LP - On récupère le chall après les -250LP d'inactivité !",
         'viewer_count':4073,
         'started_at':'2019-08-14T07:01:59Z',
         'language':'fr',
         'thumbnail_url':'https://static-cdn.jtvnw.net/previews-ttv/live_user_solary-{width}x{height}.jpg',
         'tag_ids':[
            '6f655045-9989-4ef7-8f85-1edcec42d648'
         ]
      }
   ],
   'pagination':{
      'cursor':'eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19'
   }
}
```

Ce format de données est appelé JSON et est facilement lisible. L'objet `data` est un tableau qui contient tous les streams actuellement actifs. La clé `type` garantit que le stream est actuellement `live`. Cette clé sera vide sinon (en cas d'erreur, par exemple).

Donc, si nous voulons créer une variable booléenne en Python qui stocke si l'utilisateur actuel est en train de streamer, tout ce que nous devons ajouter à notre code est :

```python
json_response = response.json()

# Nous obtenons uniquement les streams
streams = json_response.get('data', [])

# Nous créons une petite fonction, (un lambda), qui teste si un stream est en direct ou non
is_active = lambda stream: stream.get('type') == 'live'
# Nous filtrons notre tableau de streams avec cette fonction afin de ne garder que les streams qui sont actifs
streams_active = filter(is_active, streams)

# any retourne True si streams_active a au moins un élément, sinon False
at_least_one_stream_active = any(streams_active)

print(at_least_one_stream_active)
```

À ce stade, `at_least_one_stream_active` est True lorsque votre streamer Twitch préféré est en direct.

Voyons maintenant comment recevoir une notification par SMS.

# Envoyez-moi un SMS, MAINTENANT !

Pour nous envoyer un SMS, nous allons utiliser l'API Twilio. Il suffit d'aller [ici](https://www.twilio.com/try-twilio) et de créer un compte. Lorsque vous êtes invité à confirmer votre numéro de téléphone, veuillez utiliser le numéro de téléphone que vous souhaitez utiliser dans ce projet. Ainsi, vous pourrez utiliser les 15 $ de crédit gratuit que Twilio offre aux nouveaux utilisateurs. À environ 1 centime par SMS, cela devrait suffire pour que votre bot fonctionne pendant un an.

Si vous allez sur la [console](https://www.twilio.com/console), vous verrez votre `Account SID` et votre `Auth Token`, sauvegardez-les pour plus tard. Cliquez également sur le gros bouton rouge "Get My Trial Number", suivez les étapes et sauvegardez ce numéro pour plus tard.

Envoyer un SMS avec l'API Twilio Python est très facile, car ils fournissent un package qui fait le travail fastidieux pour vous. Installez le package avec `pip install Twilio` et faites simplement :

```python
from twilio.rest import Client
client = Client(<Your Account SID>, <Your Auth Token>)
client.messages.create(
	body='Test MSG',from_=<Your Trial Number>,to=<Your Real Number>)

```

Et c'est tout ce dont vous avez besoin pour vous envoyer un SMS, incroyable, n'est-ce pas ?

# Mettre tout ensemble

Nous allons maintenant mettre tout ensemble et raccourcir un peu le code afin de rester sous les 30 lignes de code Python.

```python
import requests
from twilio.rest import Client
endpoint = "https://api.twitch.tv/helix/streams?"
headers = {"Client-ID": "<YOUR-CLIENT-ID>"}
params = {"user_login": "Solary"}
response = request.get(endpoint, params=params, headers=headers)
json_response = response.json()
streams = json_response.get('data', [])
is_active = lambda stream:stream.get('type') == 'live'
streams_active = filter(is_active, streams)
at_least_one_stream_active = any(streams_active)
if at_least_one_stream_active:
    client = Client(<Your Account SID>, <Your Auth Token>)
	client.messages.create(body='LIVE !!!',from_=<Your Trial Number>,to=<Your Real Number>)
```

# Éviter les doubles notifications

Ce snippet fonctionne très bien, mais si ce snippet s'exécute toutes les minutes sur un serveur, dès que notre streamer Twitch préféré est en direct, nous recevrons un SMS toutes les minutes.

Nous avons besoin d'un moyen de stocker le fait que nous avons déjà été notifiés que notre streamer est en direct et que nous n'avons plus besoin d'être notifiés.

Le bon côté de l'API Twilio est qu'elle offre un moyen de récupérer notre historique de messages, donc nous devons simplement récupérer le dernier SMS que nous avons envoyé pour voir si nous avons déjà envoyé un texte nous notifiant que le streamer est en direct.

Voici ce que nous allons faire en pseudocode :

```
if favorite_twitcher_live and last_sent_sms is not live_notification:
	send_live_notification()
if not favorite_twitcher_live and last_sent_sms is live_notification:
	send_live_is_over_notification()
```

De cette façon, nous recevrons un SMS dès que le stream commence, ainsi que lorsqu'il est terminé. Ainsi, nous ne serons pas spammés - parfait, n'est-ce pas ? Codons cela :

```python
# réutilisation de notre client Twilio
last_messages_sent = client.messages.list(limit=1)
last_message_id = last_messages_sent[0].sid
last_message_data = client.messages(last_message_id).fetch()
last_message_content = last_message_data.body
```

Mettons maintenant tout ensemble à nouveau :

```py
import requests
from twilio.rest import Client
client = Client(<Your Account SID>, <Your Auth Token>)

endpoint = "https://api.twitch.tv/helix/streams?"
headers = {"Client-ID": "<YOUR-CLIENT-ID>"}
params = {"user_login": "Solary"}
response = request.get(endpoint, params=params, headers=headers)
json_response = response.json()
streams = json_response.get('data', [])
is_active = lambda stream:stream.get('type') == 'live'
streams_active = filter(is_active, streams)
at_least_one_stream_active = any(streams_active)

last_messages_sent = client.messages.list(limit=1)
if last_messages_sent:
	last_message_id = last_messages_sent[0].sid
	last_message_data = client.messages(last_message_id).fetch()
	last_message_content = last_message_data.body
    online_notified = "LIVE" in last_message_content
    offline_notified = not online_notified
else:
	online_notified, offline_notified = False, False

if at_least_one_stream_active and not online_notified:
	client.messages.create(body='LIVE !!!',from_=<Your Trial Number>,to=<Your Real Number>)
if not at_least_one_stream_active and not offline_notified:
	client.messages.create(body='OFFLINE !!!',from_=<Your Trial Number>,to=<Your Real Number>)
```

Et voilà !

Vous avez maintenant un snippet de code, en moins de 30 lignes de Python, qui vous enverra un SMS dès que votre streamer Twitch préféré passe en ligne/hors ligne et sans vous spammer.

Il nous faut maintenant un moyen d'héberger et d'exécuter ce snippet toutes les X minutes.

# La quête d'un hébergeur

Pour héberger et exécuter ce snippet, nous allons utiliser Heroku. Heroku est honnêtement l'un des moyens les plus simples d'héberger une application sur le web. L'inconvénient est que c'est vraiment cher par rapport à d'autres solutions. Heureusement pour nous, ils ont un plan gratuit généreux qui nous permettra de faire ce que nous voulons pour presque rien.

Si vous ne l'avez pas déjà, vous devez créer un [compte Heroku](https://www.heroku.com/). Vous devez également [télécharger et installer le client Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Vous devez maintenant déplacer votre script Python dans son propre dossier, n'oubliez pas d'ajouter un fichier `requirements.txt`. Le contenu de ce dernier commence par :

```
requests
twilio
```

`cd` dans ce dossier et faites simplement un `heroku create --app <nom_de_l_app>`.

Si vous allez sur votre [tableau de bord de l'application](https://dashboard.heroku.com/apps), vous verrez votre nouvelle application.

Nous devons maintenant initialiser un dépôt git et pousser le code sur Heroku :

```
git init
heroku git:remote -a <nom_de_l_app>
git add .
git commit -am 'Déploiement du script révolutionnaire'
git push heroku master
```

Votre application est maintenant sur Heroku, mais elle ne fait rien. Comme ce petit script ne peut pas accepter de requêtes HTTP, aller sur `<nom_de_l_app>.herokuapp.com` ne fera rien. Mais cela ne devrait pas être un problème.

Pour que ce script fonctionne 24/7, nous devons utiliser un simple add-on Heroku appelé "Heroku Scheduler". Pour installer cet add-on, cliquez sur le bouton "Configure Add-ons" sur votre tableau de bord de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Capture-d-e-cran-2019-08-15-a--12.50.40.png)

Ensuite, dans la barre de recherche, cherchez Heroku Scheduler :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Capture-d-e-cran-2019-08-15-a--12.53.12.png)

Cliquez sur le résultat, puis sur "Provision"

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Capture-d-e-cran-2019-08-15-a--12.50.59.png)

Si vous retournez à votre tableau de bord de l'application, vous verrez l'add-on :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Capture-d-e-cran-2019-08-15-a--12.54.16.png)

Cliquez sur le lien "Heroku Scheduler" pour configurer un travail. Ensuite, cliquez sur "Create Job". Ici, sélectionnez "10 minutes", et pour la commande d'exécution, sélectionnez `python <nom_de_votre_script>.py`. Cliquez sur "Save job".

Bien que tout ce que nous avons utilisé jusqu'à présent sur Heroku soit gratuit, le Heroku Scheduler exécutera le travail sur l'instance à 25 $/mois, mais prorata à la seconde. Comme ce script prend environ 3 secondes à s'exécuter, pour que ce script s'exécute toutes les 10 minutes, vous ne devriez avoir à dépenser que 12 centimes par mois.

# Idées pour des améliorations

J'espère que vous avez aimé ce projet et que vous vous êtes amusé à le mettre en place. En moins de 30 lignes de code, nous avons fait beaucoup, mais tout cela est loin d'être parfait. Voici quelques idées pour l'améliorer :

* Envoyez-vous plus d'informations sur le stream actuel (jeu joué, nombre de spectateurs...)
* Envoyez-vous la durée du dernier stream une fois que le streamer est hors ligne
* Ne vous envoyez pas de SMS, mais plutôt un email
* Surveillez plusieurs streamers en même temps

N'hésitez pas à me dire dans les commentaires si vous avez d'autres idées.

# Conclusion

J'espère que vous avez aimé cet article et que vous avez appris des choses en le lisant. Je crois vraiment que ce genre de projet est l'un des meilleurs moyens d'apprendre de nouveaux outils et concepts. J'ai récemment lancé une [API de web scraping](https://www.scrapingninja.co) où j'ai beaucoup appris en la réalisant.

Veuillez me dire dans les commentaires si vous avez aimé ce format et si vous voulez en faire plus.

J'ai beaucoup d'autres idées et j'espère que vous les aimerez. N'hésitez pas à partager ce que vous construisez avec ce snippet, les possibilités sont infinies.

Bon codage.

Pierre

## Vous ne voulez pas manquer mon prochain article :

Vous pouvez vous abonner [ici](https://www.daolf.com/stay_updated/) à ma newsletter.