---
title: Créer un Bot Twitter en Python avec Tweepy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-08T01:11:47.000Z'
originalURL: https://freecodecamp.org/news/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PONvGc-nH38lwuley7JoSg.png
tags:
- name: bots
  slug: bots
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Twitter
  slug: twitter
- name: Web Development
  slug: web-development
seo_title: Créer un Bot Twitter en Python avec Tweepy
seo_desc: 'By Lucas Kohorst

  With about 15% of Twitter being composed of bots, I wanted to try my hand at it.
  I googled how to create a Twitter bot and was brought to a cleanly laid out web
  app. It allowed you to create a bot that would like, follow, or retweet ...'
---

Par Lucas Kohorst

Avec environ 15 % de Twitter composé de bots, j'ai voulu essayer de créer le mien. J'ai cherché sur Google comment créer un bot Twitter et j'ai été dirigé vers une application web bien conçue. Elle permettait de créer un bot qui pouvait aimer, suivre ou retweeter un tweet en fonction d'un mot-clé. Le problème était que vous ne pouviez créer qu'un seul bot pour une seule fonction.

J'ai donc décidé de coder un bot moi-même avec Python et la bibliothèque Tweepy.

### Installation

Tout d'abord, j'ai téléchargé Tweepy. Vous pouvez le faire en utilisant le gestionnaire de paquets pip.

```
pip install tweepy
```

Vous pouvez également cloner le dépôt GitHub si vous n'avez pas pip installé.

```
git clone https://github.com/tweepy/tweepy.gitcd tweepypython setup.py install
```

Vous devrez importer Tweepy et Tkinter (pour l'interface graphique).

```
import tweepyimport Tkinter
```

### Identifiants

Ensuite, nous devons lier notre compte Twitter à notre script Python. Rendez-vous sur [apps.twitter.com](https://apps.twitter.com/) et connectez-vous avec votre compte. Créez une application Twitter et générez une Clé de consommateur, un Secret de consommateur, un Jeton d'accès et un Secret de jeton d'accès. Maintenant, vous êtes prêt à commencer !

Sous vos instructions d'importation, stockez vos identifiants dans des variables, puis utilisez le deuxième bloc de code pour authentifier votre compte avec Tweepy.

```
consumer_key = 'clé de consommateur'consumer_secret = 'secret de consommateur'access_token = 'jeton d'accès'access_token_secret = 'secret de jeton d'accès'
```

```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)auth.set_access_token(access_token, access_token_secret)api = tweepy.API(auth)
```

Pour vérifier si votre programme fonctionne, vous pouvez ajouter :

```
user = api.me()print (user.name)
```

Cela devrait retourner le nom de votre compte Twitter dans la console.

### Construire le Bot

Ce bot est conçu pour :

1. Suivre tout le monde qui vous suit.
2. Mettre en favoris et retweeter un tweet en fonction de mots-clés.
3. Répondre à un utilisateur en fonction d'un mot-clé.

La première étape est la plus simple, il suffit de **boucler** à travers vos abonnés et de suivre chacun d'eux.

```
for follower in tweepy.Cursor(api.followers).items():    follower.follow()    print ("Suivi de tout le monde qui suit " + user.name)
```

À ce stade, pour vous assurer que votre code fonctionne, vous devriez vous connecter à Twitter et observer le nombre de personnes que vous suivez augmenter.

À partir de ce point, en plus de la configuration et de l'emballage des étiquettes dans l'interface graphique, je code tout sous la fonction `mainFunction()`.

```
def mainFunction():    #Le code
```

Vous pouvez peut-être voir où cela mène. Pour mettre en favoris ou retweeter un tweet, nous pouvons utiliser une boucle for et une instruction try comme ceci :

```
search = "Mot-clé"
```

```
numberOfTweets = "Nombre de tweets avec lesquels vous souhaitez interagir"
```

```
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):    try:        tweet.retweet()        print('Retweeté le tweet')
```

```
    except tweepy.TweepError as e:        print(e.reason)
```

```
    except StopIteration:        break
```

Pour mettre en favoris un tweet, vous pouvez simplement remplacer

```
tweet.retweet()
```

par

```
tweet.favorite()
```

Pour répondre à un utilisateur en fonction d'un mot-clé, nous devons stocker le nom d'utilisateur et l'ID Twitter de l'utilisateur.

```
tweetId = tweet.user.idusername = tweet.user.screen_name
```

Nous pouvons ensuite boucler à travers les tweets et mettre à jour notre statut (tweet) à chaque utilisateur.

```
phrase = "Ce que vous souhaitez que votre tweet de réponse dise"
```

```
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):            try:                tweetId = tweet.user.id                username = tweet.user.screen_name                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)                print ("Répondu avec " + phrase)                       except tweepy.TweepError as e:                print(e.reason)
```

```
           except StopIteration:                break
```

Si vous souhaitez utiliser le script uniquement via le terminal et mettre à jour le code chaque fois que vous souhaitez l'exécuter, vous avez alors terminé votre bot.

### Créer l'Interface Graphique

Nous pouvons créer une application GUI qui prendra nos entrées du mot-clé que vous souhaitez rechercher et si vous souhaitez mettre un tweet en favoris ou non.

Nous devons d'abord initialiser Tkinter et configurer la disposition.

Pour créer notre interface utilisateur, nous allons avoir sept étiquettes pour la recherche, le nombre de tweets et la réponse. Plus les questions : souhaitez-vous répondre, mettre en favoris, retweeter le tweet et suivre l'utilisateur.

Rappelez-vous que le code ci-dessous est **en dehors** et **au-dessus** de notre `mainFunction()`.

```
root = Tk()
```

```
label1 = Label( root, text="Recherche")E1 = Entry(root, bd =5)
```

```
label2 = Label( root, text="Nombre de Tweets")E2 = Entry(root, bd =5)
```

```
label3 = Label( root, text="Réponse")E3 = Entry(root, bd =5)
```

```
label4 = Label( root, text="Répondre ?")E4 = Entry(root, bd =5)
```

```
label5 = Label( root, text="Retweeter ?")E5 = Entry(root, bd =5)
```

```
label6 = Label( root, text="Mettre en favoris ?")E6 = Entry(root, bd =5)
```

```
label7 = Label( root, text="Suivre ?")E7 = Entry(root, bd =5)
```

Nous devons également **emballer** chaque étiquette pour qu'elles apparaissent, puis appeler la fonction root dans une boucle pour qu'elle reste à l'écran et ne se ferme pas immédiatement.

Voici à quoi ressemble l'**emballage** de la première étiquette. J'ai emballé toutes les étiquettes sous la `mainFunction()`.

```
label1.pack()E1.pack()
```

```
root.mainloop()
```

Si vous avez exécuté uniquement votre code GUI, cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/FyVf-GWVdug0wuVsY7tIJrmjP4PJdVvJwvmU)

Cependant, entrer du texte dans les étiquettes ou cliquer sur le bouton de soumission ne fera rien à ce stade, car l'interface n'est pas encore connectée au code.

Pour stocker l'entrée de l'utilisateur dans les étiquettes, nous devons utiliser la fonction `.get()`. J'ai utilisé des fonctions individuelles pour chaque étiquette.

```
def getE1():    return E1.get()
```

Ensuite, dans ma `mainFunction()`, j'ai appelé la fonction `getE1()` et stocké l'entrée dans une variable. Pour E1, cela ressemble à ceci :

```
getE1()search = getE1()
```

Vous devez faire cela pour chaque étiquette. Pour l'étiquette `numberOfTweets`, assurez-vous de convertir l'entrée en entier.

```
getE2()numberOfTweets = getE2()numberOfTweets = int(numberOfTweets)
```

Pour les quatre dernières étiquettes (Répondre, Mettre en favoris, Retweeter et Suivre), nous devons vérifier si l'entrée de l'utilisateur est "oui" ou "non" pour exécuter ou non la fonction donnée. Cela peut être accompli avec des instructions **if**.

Voici le code pour la fonction **répondre** :

```
if reply == "yes":
```

```
    for tweet in tweepy.Cursor(api.search,     search).items(numberOfTweets):            try:                tweetId = tweet.user.id                username = tweet.user.screen_name                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)                print ("Répondu avec " + phrase)                       except tweepy.TweepError as e:                print(e.reason)
```

```
except StopIteration:                break
```

Pour les fonctions de mise en favoris, de retweet et de suivi, remplacez simplement **reply** par "retweet", "favorite" et "follow". Ensuite, copiez et collez le code que vous avez écrit ci-dessus pour chacun sous l'instruction **if**. 

Maintenant, nous devons simplement ajouter le bouton **submit** et lui dire d'appeler la `mainFunction()` et d'exécuter le code pour notre bot Twitter. Encore une fois, n'oubliez pas de l'emballer !

```
submit = Button(root, text ="Submit", command = mainFunction)
```

C'est tout ! Après avoir exécuté votre script de bot, une application GUI devrait s'exécuter et vous pourrez répondre, retweeter, mettre en favoris et suivre les utilisateurs.

Avec ce bot Twitter, j'ai créé le compte [FreeWtr](https://twitter.com/FreeWtr) qui prône l'utilisation de l'eau du robinet filtrée plutôt que de l'eau en bouteille. Voici une capture d'écran du profil.

![Image](https://cdn-media-1.freecodecamp.org/images/DzAOfETdkXdCFlKhwI3Fh1LBl-cIw9VdRLKX)

Voici le [code source complet](https://github.com/Fidel-Willis/TwitterBot) sur GitHub.