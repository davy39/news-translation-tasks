---
title: Comment créer un bot Telegram en utilisant Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-12-16T17:42:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-telegram-bot-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Telegram-Bot.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: Python
  slug: python
seo_title: Comment créer un bot Telegram en utilisant Python
seo_desc: "Automated chatbots are quite useful for stimulating interactions. We can\
  \ create chatbots for Slack, Discord, and other platforms. \nIn this article, I'll\
  \ teach you how to build a Telegram chatbot that will tell you your horoscope. So,\
  \ let’s get starte..."
---

Les chatbots automatisés sont assez utiles pour stimuler les interactions. Nous pouvons créer des chatbots pour Slack, Discord et d'autres plateformes. 

Dans cet article, je vais vous apprendre à construire un chatbot Telegram qui vous donnera votre horoscope. Alors, commençons !

## Comment obtenir votre jeton de bot

Pour configurer un nouveau bot, vous devrez parler à BotFather. Non, ce n'est pas une personne – c'est aussi un bot, et il est le patron de tous les bots Telegram.

1. Recherchez @botfather dans Telegram.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-16-092357.png)
_BotFather Telegram Bot_

2. Commencez une conversation avec BotFather en cliquant sur le bouton Start.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-16-092531.png)
_Cliquez sur le bouton Start_

3. Tapez `/newbot`, et suivez les instructions pour configurer un nouveau bot. Le BotFather vous donnera un jeton que vous utiliserez pour authentifier votre bot et lui donner accès à l'API Telegram.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-16-093337.png)
_Obtention du jeton d'accès_

**Note :** Assurez-vous de stocker le jeton de manière sécurisée. Toute personne ayant accès à votre jeton peut facilement manipuler votre bot.

## Comment configurer votre environnement de codage

Configurons l'environnement de codage. Bien qu'il existe diverses bibliothèques disponibles pour créer un bot Telegram, nous utiliserons la bibliothèque [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/). Il s'agit d'une implémentation Python simple mais extensible pour l'API Telegram Bot avec des capacités à la fois synchrones et asynchrones.

Installez la bibliothèque pyTelegramBotAPI en utilisant pip :

```bash
pip install pyTelegramBotAPI
```

Ensuite, ouvrez votre éditeur de code préféré et créez un fichier `.env` pour stocker votre jeton comme suit :

```bash
export BOT_TOKEN=votre-jeton-de-bot-ici
```

Après cela, exécutez la commande `source .env` pour lire les variables d'environnement depuis le fichier `.env`.

## Comment créer votre premier bot

Toutes les implémentations de l'API sont stockées dans une seule classe appelée `TeleBot`. Elle offre de nombreuses façons d'écouter les messages entrants ainsi que des fonctions comme `send_message()`, `send_document()`, et d'autres pour envoyer des messages.

Créez un nouveau fichier `bot.py` et collez le code suivant :

```python
import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
```

Dans le code ci-dessus, nous utilisons la bibliothèque `os` afin de lire les variables d'environnement stockées dans notre système.

Si vous vous souvenez, nous avons exporté une variable d'environnement appelée `BOT_TOKEN` dans l'étape précédente. La valeur de `BOT_TOKEN` est lue dans une variable appelée `BOT_TOKEN`. Ensuite, nous utilisons la classe `TeleBot` pour créer une instance de bot et lui passons le `BOT_TOKEN`.

Nous devons ensuite enregistrer des gestionnaires de messages. Ces gestionnaires de messages contiennent des filtres qu'un message doit passer. Si un message passe le filtre, la fonction décorée est appelée et le message entrant est fourni comme argument.

Définissons un gestionnaire de messages qui gère les commandes entrantes `/start` et `/hello`.

```python
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Salut, comment ça va ?")
```

N'importe quel nom est acceptable pour une fonction qui est décorée par un gestionnaire de messages, mais elle ne peut avoir qu'un seul paramètre (le message).

Ajoutons un autre gestionnaire qui renvoie tous les messages texte entrants à l'expéditeur.

```python
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
```

Le code ci-dessus utilise une expression `lambda` pour tester un message. Puisque nous devons renvoyer tous les messages, nous retournons toujours `True` depuis la fonction `lambda`.

Vous avez maintenant un bot simple qui répond aux commandes `/start` et `/hello` avec un message statique et renvoie tous les autres messages envoyés. Ajoutez ce qui suit à la fin de votre fichier pour lancer le bot :

```python
bot.infinity_polling()
```

C'est tout ! Nous avons un bot Telegram prêt. Exécutons le fichier Python et allons sur Telegram pour tester le bot.

Recherchez le bot en utilisant son nom d'utilisateur si vous ne parvenez pas à le trouver. Vous pouvez le tester en envoyant des commandes comme `/hello` et `/start` et d'autres textes aléatoires.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-16-101334.png)
_Test du bot_

Note : Tous les gestionnaires de messages sont testés dans l'ordre dans lequel ils ont été déclarés dans le fichier source.

Pour plus d'informations sur l'utilisation de la bibliothèque pyTelegramBotAPI, vous pouvez vous référer à leur **[documentation](https://github.com/eternnoir/pyTelegramBotAPI)**.

## Comment coder le bot d'horoscope

Concentrons-nous maintenant sur la construction de notre bot d'horoscope. Nous allons utiliser l'enchaînement de messages dans le bot. Le bot demandera d'abord votre signe du zodiaque, puis le jour, et ensuite il répondra avec l'horoscope pour ce jour particulier.

En coulisses, le bot interagit avec une API pour obtenir les données de l'horoscope.

Nous allons utiliser l'[API Horoscope](https://horoscope-app-api.vercel.app/) que j'ai construite dans un autre tutoriel. Si vous souhaitez apprendre à en construire une, vous pouvez suivre [ce tutoriel](https://ashutoshkrris.hashnode.dev/how-to-create-a-horoscope-api-with-beautiful-soup-and-flask). Assurez-vous d'explorer les API [ici](https://horoscope-app-api.vercel.app/) avant de commencer.

### Comment récupérer les données de l'horoscope

Créons une fonction utilitaire pour récupérer les données de l'horoscope pour un jour particulier.

```python
import requests

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Obtenir l'horoscope quotidien pour un signe du zodiaque.
    Arguments clés :
    sign:str - Signe du zodiaque
    day:str - Date au format (YYYY-MM-DD) OU TODAY OU TOMORROW OU YESTERDAY
    Retour:dict - Données JSON
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()
```

Dans le code Python ci-dessus, nous avons créé une fonction qui accepte deux arguments de chaîne – `sign` et `day` – et retourne des données JSON. Nous envoyons une requête GET sur l'URL de l'API et passons `sign` et `day` comme paramètres de requête.

Si vous testez la fonction, vous obtiendrez une sortie similaire à celle-ci :

```json
{
   "data":{
      "date": "15 déc. 2022",
      "horoscope_data": "Restez discret pendant la journée et essayez de ne pas vous laisser entraîner dans le verbiage frivole qui domine les heures d'éveil. Après le coucher du soleil, n'hésitez pas à exprimer votre opinion. Vous pouvez remarquer qu'il y a un ton sobre et une sensation restrictive aujourd'hui qui vous laisse l'impression de ne jamais pouvoir vous libérer de votre situation actuelle. Ne vous laissez pas piéger par cet état d'esprit négatif."
   },
   "status": 200,
   "success": true
}
```

Note : Vous pouvez en savoir plus sur la bibliothèque `requests` en Python dans [ce tutoriel](https://ashutoshkrris.hashnode.dev/how-to-interact-with-web-services-using-python).

### Comment ajouter un gestionnaire de messages

Maintenant que nous avons une fonction qui retourne les données de l'horoscope, créons un gestionnaire de messages dans notre bot qui demande le signe du zodiaque de l'utilisateur.

```python
@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "Quel est votre signe du zodiaque ?\nChoisissez-en un : *Bélier*, *Taureau*, *Gémeaux*, *Cancer*, *Lion*, *Vierge*, *Balance*, *Scorpion*, *Sagittaire*, *Capricorne*, *Verseau*, et *Poissons*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)
```

La fonction ci-dessus est un peu différente des autres fonctions que nous avons définies précédemment. La fonctionnalité d'horoscope du bot sera invoquée par la commande `/horoscope`. Nous envoyons un message texte à l'utilisateur, mais remarquez que nous avons défini le `parse_mode` sur **Markdown** lors de l'envoi du message.

Puisque nous allons utiliser l'enchaînement de messages, nous avons utilisé la méthode `register_next_step_handler()`. Cette méthode accepte deux paramètres : **le message** envoyé par l'utilisateur et **la fonction de rappel** qui doit être appelée après le message. Ainsi, nous passons la variable `sent_msg` et une nouvelle fonction `day_handler` que nous allons définir ensuite.

Définissons la fonction `day_handler()` qui accepte le message.

```python
def day_handler(message):
    sign = message.text
    text = "Quel jour voulez-vous connaître ?\nChoisissez-en un : *AUJOURDHUI*, *DEMAIN*, *HIER*, ou une date au format AAAA-MM-JJ."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())
```

Nous récupérons le signe du zodiaque depuis l'attribut `message.text`. Similaire à la fonction précédente, il demande également le jour pour lequel vous voulez connaître l'horoscope.

À la fin, nous utilisons la même méthode `register_next_step_handler()` et passons le `sent_msg`, la fonction de rappel `fetch_horoscope`, et le `sign`.

Définissons maintenant la fonction `fetch_horoscope()` qui accepte le message et le signe.

```python
def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Voici votre horoscope !")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
```

Il s'agit de la fonction finale où nous obtenons le signe depuis le paramètre de la fonction et le jour depuis l'attribut `message.text`.

Ensuite, nous récupérons l'horoscope en utilisant la fonction `get_daily_horoscope()` et construisons notre message. À la fin, nous envoyons le message avec les données de l'horoscope.

## Démo du bot

Une fois que vous exécutez le fichier Python, vous pouvez tester cette fonctionnalité. Voici la démo :

%[https://youtube.com/shorts/nTHI2rPV_RE?feature=share]

## Étapes suivantes recommandées

Pour l'instant, le bot cesse de fonctionner dès que nous arrêtons notre application Python. Afin de le faire fonctionner en permanence, vous pouvez déployer le bot sur des plateformes comme Heroku, Render, etc.

Voici un lien vers le [dépôt GitHub pour ce projet](https://github.com/ashutoshkrris/Telegram-Horoscope-Bot) - n'hésitez pas à le consulter.

Vous pouvez également ajouter plus de fonctionnalités au bot en explorant les [API Telegram](https://core.telegram.org/).

Merci d'avoir lu ! Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris)[.](https://ireadblog.com/)