---
title: Apprenez à créer votre premier bot sur Telegram avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:40:49.000Z'
originalURL: https://freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vUK3nWPkSEJVAFRLLJbxHA.jpeg
tags:
- name: api
  slug: api
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Software Engineering
  slug: software-engineering
seo_title: Apprenez à créer votre premier bot sur Telegram avec Python
seo_desc: 'By Dzaky Widya Putra

  Imagine this, there is a message bot that will send you a random cute dog image
  whenever you want, sounds cool right? Let’s make one!

  For this tutorial, we are going to use Python 3, python-telegram-bot, and public
  API RandomDog....'
---

Par Dzaky Widya Putra

Imaginez ceci, il y a un bot qui vous envoie une image aléatoire de chien mignon chaque fois que vous le souhaitez, cela semble cool, non ? Créons-en un !

Pour ce tutoriel, nous allons utiliser **Python 3, [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot),** et l'API publique [**RandomDog**](https://random.dog/)**.**

À la fin de ce tutoriel, vous aurez un bot anti-stress qui vous enverra des images de chiens mignons chaque fois que vous en aurez besoin, youpi !

### Installation

Avant de commencer à écrire le programme, nous devons générer un token pour notre bot. Le token est nécessaire pour accéder à l'API de Telegram, et installer les dépendances nécessaires.

#### 1. Créez un nouveau bot dans BotFather

Si vous souhaitez créer un bot sur Telegram, vous devez "enregistrer" votre bot avant de pouvoir l'utiliser. Lorsque nous "enregistrons" notre bot, nous obtenons le token pour accéder à l'API de Telegram.

Allez sur [BotFather](https://telegram.me/BotFather) (si vous l'ouvrez sur un ordinateur, assurez-vous d'avoir l'application Telegram), puis créez un nouveau bot en envoyant la commande `/newbot`. Suivez les étapes jusqu'à obtenir le nom d'utilisateur et le token pour votre bot. Vous pouvez accéder à votre bot en utilisant cette URL : `[https://telegram.me/YOUR_BOT_USERNAME](https://telegram.me/YOUR_BOT_USERNAMEa)` et votre token devrait ressembler à ceci.

```
704418931:AAEtcZ*************
```

#### 2. Installez la bibliothèque

Puisque nous allons utiliser une bibliothèque pour ce tutoriel, installez-la avec cette commande.

```
pip3 install python-telegram-bot
```

Si la bibliothèque est installée avec succès, alors nous sommes prêts à commencer.

### Écrire le programme

Créons notre premier bot. Ce bot devrait renvoyer une image de chien lorsque nous envoyons la commande `/bop`. Pour cela, nous pouvons utiliser l'API publique de [**RandomDog**](https://random.dog/) pour générer des images aléatoires de chiens.

Le flux de travail de notre bot est aussi simple que ceci :

> accéder à l'API -> obtenir l'URL de l'image -> envoyer l'image

#### 1. Importer les bibliothèques

Tout d'abord, importons toutes les bibliothèques dont nous avons besoin.

```py
from telegram.ext import Updater, CommandHandler
import requests
import re
```

#### 2. Accéder à l'API et obtenir l'URL de l'image

Créons une fonction pour obtenir l'URL. En utilisant la bibliothèque requests, nous pouvons accéder à l'API et obtenir les données JSON.

```
contents = requests.get('https://random.dog/woof.json').json()
```

Vous pouvez vérifier les données JSON en accédant à cette URL : `https://random.dog/woof.json` dans votre navigateur. Vous verrez quelque chose comme ceci à l'écran :

```
{"url":"https://random.dog/*****.JPG"}
```

Obtenez l'URL de l'image puisque nous avons besoin de ce paramètre pour pouvoir envoyer l'image.

```
image_url = contents['url']
```

Encapsulez ce code dans une fonction appelée `get_url()`.

```py
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
```

#### 3. Envoyer l'image

Pour envoyer un message/image, nous avons besoin de deux paramètres : l'URL de l'image et l'ID du destinataire — cela peut être l'ID d'un groupe ou d'un utilisateur.

Nous pouvons obtenir l'URL de l'image en appelant notre fonction `get_url()`.

```
url = get_url()
```

Obtenez l'ID du destinataire avec ce code :

```
chat_id = update.message.chat_id
```

Après avoir obtenu l'URL de l'image et l'ID du destinataire, il est temps d'envoyer le message, qui est une image.

```
bot.send_photo(chat_id=chat_id, photo=url)
```

Encapsulez ce code dans une fonction appelée `bop`, et assurez-vous que votre code ressemble à ceci :

```py
def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
```

#### 4. `Programme principal`

Enfin, créez une autre fonction appelée `main` pour exécuter notre programme. **N'oubliez pas de remplacer** `YOUR_TOKEN` par le token que nous avons généré précédemment dans ce tutoriel.

```py
def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
```

À la fin, votre code devrait ressembler à ceci :

```py
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

#### 5. Exécuter le programme

Super ! Vous avez terminé votre premier programme. Maintenant, vérifions s'il fonctionne. Enregistrez le fichier, nommez-le `main.py`, puis exécutez-le avec cette commande.

```
python3 main.py
```

Allez sur votre bot Telegram en accédant à cette URL : `https://telegram.me/YOUR_BOT_USERNAME`. Envoyez la commande `/bop`. Si tout se passe parfaitement, le bot répondra avec une image aléatoire de chien. Mignon, non ?

![Image](https://cdn-media-1.freecodecamp.org/images/cgojJGcVwIVamFkYrpcRzrOOBJ0xFB0cTkTP)
_Une image générée aléatoirement_

### Gestion des erreurs

Super ! Maintenant, vous avez un bot qui vous enverra une image de chien mignon chaque fois que vous le souhaitez.

Il y a plus ! L'API [**RandomDog**](https://random.dog/) ne génère pas seulement des images, mais aussi des vidéos et des GIF. Si nous accédons à l'API et que nous obtenons une vidéo ou un GIF, il y a une erreur et le bot ne l'enverra pas.

Corrigeons cela pour que le bot n'envoie qu'un message avec une pièce jointe d'image. Si nous obtenons une vidéo ou un GIF, nous appellerons à nouveau l'API jusqu'à obtenir une image.

#### 1. Correspondance de l'extension de fichier avec regex

Nous allons utiliser une regex pour résoudre ce problème.

Pour distinguer une image d'une vidéo ou d'un GIF, nous pouvons regarder l'extension du fichier. Nous avons seulement besoin de la dernière partie de notre URL.

```
https://random.dog/*****.JPG
```

Nous devons d'abord définir quelles extensions de fichier sont autorisées dans notre programme.

```
allowed_extension = ['jpg','jpeg','png']
```

Ensuite, utilisez la regex pour extraire l'extension du fichier de l'URL.

```
file_extension = re.search("([^.]*)$",url).group(1).lower()
```

En utilisant ce code, créez une fonction appelée `get_image_url()` pour itérer l'URL jusqu'à obtenir l'extension de fichier que nous voulons (jpg, jpeg, png).

```py
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
```

#### 2. Modifiez votre code

Super ! Maintenant, pour la dernière partie, remplacez la ligne `url = get_url()` dans la fonction `bop()` par `url = get_image_url()`, et votre code devrait ressembler à ceci :

```py
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

Bien ! Tout devrait fonctionner parfaitement. Vous pouvez également consulter mon compte [GitHub](https://github.com/dzakyputra/doggobot) pour obtenir le code.

Enfin, félicitations pour avoir terminé ce tutoriel, et vous avez maintenant un bot Telegram cool.

N'hésitez pas à laisser un commentaire si vous pensez qu'il y a des erreurs dans mon code ou dans mon écriture, car je suis encore en train d'apprendre et je veux m'améliorer.

Merci et bonne chance pour la pratique ! 😊