---
title: Comment créer un chatbot dictionnaire WhatsApp en utilisant Twilio, FastAPI
  et MongoDB
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2023-08-02T23:47:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-whatsapp-dictionary-chatbot-using-twilio-fast-api-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/WHATSAPP-DICTIONARY-CHATBOT.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: MongoDB
  slug: mongodb
seo_title: Comment créer un chatbot dictionnaire WhatsApp en utilisant Twilio, FastAPI
  et MongoDB
seo_desc: 'Sometimes you want to check what a word means while chatting with someone
  in WhatsApp. But you don''t want to exit or minimize the app.

  Well, how about building a WhatsApp bot that can give you the meaning of words you
  want to know?

  In this tutorial, ...'
---

Parfois, vous voulez vérifier la signification d'un mot tout en discutant avec quelqu'un sur WhatsApp. Mais vous ne voulez pas quitter ou minimiser l'application.

Et si vous construisiez un bot WhatsApp qui peut vous donner la signification des mots que vous voulez connaître ?

Dans ce tutoriel, vous apprendrez à créer un chatbot qui peut servir de dictionnaire. Il sera facilement accessible sur WhatsApp en utilisant l'API Twilio MessagingX WhatsApp pour envoyer et recevoir des messages. Nous utiliserons Fast API pour créer le serveur web et interagir avec la base de données, et MongoDB pour stocker les mots et leurs significations dans une base de données.

À la fin de ce tutoriel, vous aurez développé un chatbot fonctionnel qui peut définir des mots en temps réel pendant que vous conversez sur WhatsApp.

## Prérequis

* Python 3.9+ installé sur votre machine.

* Compte MongoDB gratuit – si vous n'en avez pas, vous pouvez en créer un [ici](https://www.mongodb.com/cloud/atlas/lp/try4?utm_ad_campaign_id=12212624539&adgroup=115749718303&cq_cmp=12212624539&gad=1).

* Compte Twilio gratuit – vous pouvez en créer un [ici](https://www.twilio.com/en-us).

* Compte développeur Merriam-Webster – vous pouvez en créer un [ici](https://www.dictionaryapi.com/register/index).

* Un IDE ou éditeur de texte, tel que [VS code](https://code.visualstudio.com/).

## Configurer votre environnement de développement

Avant de commencer, vous devez configurer votre environnement de développement en créant le répertoire et les fichiers nécessaires. Voici les commandes pour cela :

```shell
mkdir whatsappDictionary
cd whatsappDictionary
touch requirements.txt models.py utils.py main.py .env
```

* `requirements.txt` contient les bibliothèques nécessaires pour faire fonctionner le chatbot.

* `model.py` contient le code connectant votre chatbot au serveur MongoDB.

* `utils.py` inclut le code pour se connecter à l'API Twilio MessagingX WhatsApp.

* `main.py` contient le code pour construire le serveur Fast API et se connecter à l'API Merriam-Webster.

* `whatsappDictionary` est le répertoire pour tous les fichiers.

Ensuite, vous allez créer et activer un environnement virtuel et mettre à jour le gestionnaire de paquets Python `pip` vers la version la plus récente en utilisant la commande suivante :

```shell
python -m venv venv; ./venv/Scripts/Activate; pip --upgrade pip
```

Si vous êtes sur une machine Linux, utilisez cette commande :

```shell
pyton -m venv venv; venv\\Scripts\\activate.bat; pip --upgrade pip
```

Pour en savoir plus sur les environnements virtuels et leurs avantages, vous pouvez lire ce [tutoriel](https://linuxhostsupport.com/blog/why-using-a-python-virtual-environment-is-a-good-choice/#:~:text=Virtual%20environments%20are%20of%20great,the%20help%20of%20virtual%20environments.).

Ensuite, vous devrez remplir le fichier `requirements.txt` avec les dépendances suivantes :

```text
fastapi
uvicorn
twilio
pymongo
pyngrok
requests
dotenv
```

* `fastapi` est un framework Python pour construire des API rapidement et facilement.

* `uvicorn` est une implémentation de serveur ultra-rapide pour Python.

* `twilio` vous permet d'interagir avec l'API Twilio MessagingX WhatsApp.

* `pymongo` est le pilote que vous utiliserez pour vous connecter au serveur MongoDB.

* `pyngrok` vous permet de tunneler un serveur local vers une URL publique.

* `requests` permet d'envoyer des requêtes HTTP en utilisant Python.

* `dotenv` charge les variables d'environnement à partir du fichier *.env*.

Installez ces dépendances en exécutant la commande suivante dans votre terminal :

```shell
pip install -r requirements.txt
```

## Configurer la base de données

Vous souhaitez maintenant configurer une base de données pour stocker les mots et leurs définitions. Vous allez utiliser MongoDB, qui est un langage NoSQL et est facile à configurer.

Vous devrez créer un compte gratuit sur le site MongoDB (si vous n'en avez pas déjà un). Une fois que vous avez un compte, connectez-vous pour créer un nouveau cluster **Shared** et une base de données.

![Cette image montre comment créer un cluster partagé sur MongoDB](https://lh5.googleusercontent.com/Oz_BdWfzS5wphrYXi_WzAX_2e-2rzHPp3wqlTeH4BXP5HSU73Scnt39qO85Ao9TstyzYKjHYnjXXO1qabp43jJF0W6vcGkhQ3mkt6ZHn-OvurIJKAv1WYOYBxmklS0_zw775g51X5xhc3js92qNe7mUErBpnKooWtvzl7AMK6TzAO8X6qwSbbK2lRWeBNQ align="left")

*Image montrant comment créer un cluster partagé sur Mongo DB*

Ensuite, allez dans **Security\_,\_**, puis **ADD NEW DATABASE USER** pour ajouter un nouvel utilisateur avec un accès en lecture/écriture à la base de données.

![Cette image montre l'onglet où vous pouvez ajouter une nouvelle base de données](https://lh3.googleusercontent.com/r0HxaAqOZZn8yIV3ObgfuAojNdkGefNzjPJM4DVRRlPCTIpl9NmvGr-lY0hjLGWlNnyRuHQF34ujKGV2H_F4BjS746TLOfljbMax24kFo9haf0gxa9f2ZQzG-DVxI7qqzQx4W_YuZhh7y7ENSqCgOH60EWAi6hiDYO9_GilZut2uJPgy7aYMaTOd-uQTRg align="left")

*Cette image montre l'onglet où vous pouvez ajouter une nouvelle base de données*

![Cette image montre la fenêtre d'ajout d'un nouvel utilisateur de base de données](https://lh6.googleusercontent.com/iOOmBGx8NfOkCeZ_ioNqLN0aRKoJMs9RWKaRgd1xiex6WnzekwpuKLlSpj963PvfKTRTI7ZZ9pzGIFn_rJ5mFm7rrIodPTTZ1jpdnUEqj4drCOpcQ6ZWb5k6R2azZ5BCBA_zsY_ee5OtJ8m4roU0SHNRFoeXYKMu2yKKLOxpnPoEYBJKpfIavRP5-KBA3A align="left")

*Cette image montre la fenêtre d'ajout d'un nouvel utilisateur de base de données*

Retournez au tableau de bord du cluster, cliquez sur **Connect** puis sur **Drivers**.

![Cette image montre le processus final lors de la tentative de connexion au cluster](https://lh4.googleusercontent.com/EOqNVq2nqObKtABzLQphGDWRFgXPFybQhm11R_XPWdlqgigbzVsMA1zaj2zVjjMjlHpdzauXpfjofw1cyE_RUc2ijI8h_qDLN10sSoMeCGUuGU1DZ3tGB4IqRRkJmgUhNGxDhUX3Zljgo1SSgdLZwWreqFHXpEJ2WuPE62QamlRAop6JtVOfARJbWU4UIg align="left")

*Cette image montre le processus final lors de la tentative de connexion au cluster*

Copiez le code affiché et collez-le dans `model.py` :

![Cette image montre le code sur la façon de se connecter au serveur MongoDB en utilisant le pilote pymongo.](https://lh4.googleusercontent.com/s1M_HQA6uAKPxE6jZtyzh4iLHtk_4m-nIv9IOW9D0igHKEKMrwZjNAAsVIwKOzqCAhNQM-qIimO4pFbKqSAUKh78VJ9ZC02pIP5uCBT7ndw0k-6nte3CLay481osRVkDwDoMkCLaSx4ydTWDRBndVVDVHWIUFEhBjaeWoOkvZVS6SImAnjJ3BTHnT2yIMQ align="left")

*Cette image montre le code sur la façon de se connecter au serveur MongoDB en utilisant le pilote pymongo.*

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb+srv://adejumoridwan:<password>@cluster0.d9jr4ev.mongodb.net/?retryWrites=true&w=majority"

# Envoyer un ping pour confirmer une connexion réussie
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

Donnez votre mot de passe pour exécuter le code et vous connecter au serveur MongoDB. Vous ne voulez pas que quelqu'un voie cela. Allez dans le fichier `.env` que vous avez créé et stockez votre mot de passe là-bas.

```text
MONGO_SECRET=<password>
```

Ensuite, mettez à jour `model.py` pour accéder au fichier `.env`.

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get('MONGO_SECRET')

uri = f"mongodb+srv://adejumoridwan:{password}@cluster0.d9jr4ev.mongodb.net/?retryWrites=true&w=majority"

# Envoyer un ping pour confirmer une connexion réussie
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

* `load_dotenv()` charge les variables dans .env

* `os.environ.get('MONGO_SECRET')` reçoit le mot de passe de .env, qui stocke la variable mot de passe

Exécutez le script pour vous connecter au serveur MongoDB. Vous pouvez créer une collection en cliquant sur le nom de votre cluster et en allant dans Collections. Les collections sont des versions NoSQL des tables SQL.

Cliquez sur **Create Database** pour créer votre base de données :

![Cela montre des informations et des onglets concernant les clusters créés tels que Overview, Collections et ainsi de suite
](https://lh6.googleusercontent.com/yrP5_ej7jaGl3mQH9uXQEkmubLt-50NOiDcd6XG_8bV3yWe-cJZnA6snsN_xoJqpp7XQDFpXMk4xVQZHuY23D4fscJbYJfSExfDzWoeiEOQIXBjosDRchgJPu7ZWtCilXdQg5nuKBmaE10hh_Ht-zAkuGFn-RUoTwuIiH8xY2FCXXKi4TW8T3NyJEo6LyQ align="left")

*Cela montre des informations et des onglets concernant les clusters créés tels que Overview, Collections et ainsi de suite*

Donnez les noms de la base de données et de la collection. Les noms de la base de données et de la collection pour ce tutoriel sont **MY\_DB** et **dictionary**, respectivement.

![La fenêtre montre les options à remplir lorsque vous voulez créer une base de données, comme un nom de base de données, un nom de collection et des préférences supplémentaires.](https://lh4.googleusercontent.com/HdO8oJJXmQhD1n6XeiZdP0qicncdy5U7pyraNu3zX0xi2Qpu7j1JbN_ZmV8FVK4CZu8XHoCAE4wNIwEXu5J0e3ltvITtMjZ7GzI7XxwCPE7UyFnNAlJc9ycRNfmWCNeZiIXBe4hNlf7_F9HvejXz1CKQ644WvgGRFXMBvKqqG3pqM9iBMZHZStS8p93ROA align="left")

*La fenêtre montre les options à remplir lorsque vous voulez créer une base de données, comme un nom de base de données, un nom de collection et des préférences supplémentaires.*

Allez dans `models.py` et mettez à jour le code pour créer un nouveau client et vous connecter au serveur.

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get('MONGO_SECRET')

uri = f"mongodb+srv://adejumoridwan:{password}@cluster0.d9jr4ev.mongodb.net/?retryWrites=true&w=majority"

# Créer un nouveau client et se connecter au serveur
client = MongoClient(uri, server_api=ServerApi('1'))

dictionary_collection = client["MY_DB"]["dictionary"]

# Envoyer un ping pour confirmer une connexion réussie
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

`dictionary_collection` est ce que vous utiliserez pour mettre à jour les entrées dans le serveur plus tard.

## Comment configurer Twilio Sandbox pour WhatsApp

Pour configurer le bac à sable Twilio pour WhatsApp, allez dans la console Twilio. Sous Develop, cliquez sur Messaging, puis sur Try it out. Sous Try it out, cliquez sur Send a WhatsApp Message.

![Ce bac à sable vous permet d'envoyer des messages WhatsApp à votre numéro](https://lh6.googleusercontent.com/QTLWWiK_pb8FYHgyeXucP7r5WB1YpgGpBsC-spLRJWjTsT5rMkmREk7rVwT9aawQFMd-ZxCt1nLfjk57EzA2XfEmFPKSzsZYM9NVFr3XQLwDwCN9m7am7BTSEEFZUOQFSV2BQY82wgNVSCTWZD4DHV7JLo1r3mx49NXJO6eQsG0BxcM62fx-I101wjX9oA align="left")

*Ce bac à sable vous permet d'envoyer des messages WhatsApp à votre numéro*

Pour vous connecter au bac à sable WhatsApp, enregistrez le numéro fourni sur le bac à sable sur votre appareil et envoyez le message join manner-free au numéro, ou vous pouvez scanner le code QR sur votre appareil.

![Ici, vous voyez le bac à sable pour connecter le bac à sable WhatsApp à votre numéro
](https://lh6.googleusercontent.com/k1L4We_5SE5PH8ASRHfrocoEizzY0eKSOnHUEvGi-qD41nowBJtxLEDk6amQboYi59SKxYdW32PC1G74Rj2uP4qo3aLU-GTbThlEnHgj9bUStP5K9_kBVNX5ZkCcAadQZDS1YYtchfIpGCrtWlyVo2UjjXZeIFCYI7UU4HxSDmicSCjZR_l1u9ViUS8eqg align="left")

*Ici, vous voyez le bac à sable pour connecter le bac à sable WhatsApp à votre numéro*

Une fois la connexion réussie, copiez le code et collez-le dans le fichier `utils.py` :

![Ici, vous pouvez voir comment vous connecter à l'API WhatsApp dans divers langages. Actuellement, l'image montre comment se connecter à l'API WhatsApp afin que vous puissiez envoyer des messages depuis Twilio.](https://lh5.googleusercontent.com/0exaxbIgwJQYtD4kKeqcWnAlUy0bmCyap4f4pvGF8txH_meTEmckcEggzLwjL0dGszckstN8whxkYY9iz2EqXTxHfcxO6mfF_wt70NDbGqZVB56lZNZJBEi_Gv9Ee_OVTFF91czWx3AgedQKY5uhim16saPGYcbXTbknc4IL0lMQ0VDHODGJJfE8vjCJFA align="left")

*Ici, vous pouvez voir comment vous connecter à l'API WhatsApp dans divers langages. Actuellement, l'image montre comment se connecter à l'API WhatsApp afin que vous puissiez envoyer des messages depuis Twilio.*

```python
from twilio.rest import Client

account_sid = '<account_sid>'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:<to_number>
)

print(message.sid)
```

La fonction `client.messages.create()` vous permet d'envoyer des messages à votre WhatsApp depuis le bac à sable WhatsApp. Elle prend trois paramètres :

* `from_` est l'endroit d'où provient le message, c'est-à-dire depuis le bac à sable WhatsApp

* `body` prend le corps de votre message

* `to` est le numéro WhatsApp auquel vous envoyez le message

## Comment se connecter à l'API Twilio

Allez dans le fichier .env pour stocker votre jeton d'authentification Twilio, l'ID de compte, le numéro de bac à sable Twilio et le numéro WhatsApp.

```text
MONGO_SECRET="<password>"
TWILIO_ACCOUNT_SID="<account_sid>"
TWILIO_AUTH_TOKEN="<auth_token>"
TWILIO_NUMBER="<twilio_number>"
TO_NUMBER="<to_number>"
```

Mettez à jour le fichier `utils.py` pour accéder à ces variables :

```python
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')
to_number = os.getenv("TO_NUMBER")

message = client.messages.create(
  from_=f'whatsapp:{twilio_number}',
  body='Your appointment is coming up on July 21 at 3PM',
  to=f'whatsapp:{to_number}
)
```

`load_dotenv()` charge les variables d'environnement, et `os.getenv` obtient ces variables à partir de l'environnement.

Ensuite, définissez une fonction `send_message`. Cette fonction aura deux arguments : `to_number` et `text`. La fonction enverra un message défini dans `text` à `to_number`.

```python
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')

def send_message(to_number, text):
      message = client.messages.create(
          from_=f"whatsapp:{twilio_number}",
          body=text,
          to=f"whatsapp:{to_number}"
          )
```

Mettez à jour la fonction `send_message` pour configurer la journalisation en cas d'erreurs rencontrées lors de l'envoi de messages.

```python
import logging
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')

# Configurer la journalisation
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Logique d'envoi de message via l'API de messagerie Twilio
def send_message(to_number, text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=text,
            to=f"whatsapp:{to_number}"
            )
        logger.info(f"Message envoyé à {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi du message à {to_number}: {e}")
```

## Comment construire le backend FastAPI

Dans le fichier `main.py`, configurez une application FastAPI basique.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "I love FreeCodeCamp"}
```

Le code ci-dessous configure un backend FastAPI basique, créant une nouvelle instance de la classe `FastAPI` et l'assignant à la variable app.

Le décorateur `@app.get` crée un nouveau point de terminaison que vous pouvez accéder avec une requête HTTP GET. Le point de terminaison est à l'URL racine `/` et retourne une réponse JSON avec une seule paire clé-valeur : `"message": "I love FreeCodeCamp"`.

Pour exécuter l'application, exécutez la commande suivante dans votre terminal :

```shell
uvicorn main:app --reload
```

Sur votre navigateur, ouvrez l'hôte `http://127.0.0.1:8000`. Vous verrez une réponse JSON de `{"message": "I love FreeCodeCamp"}`. Vous pouvez également accéder à une documentation API interactive fournie par swagger sur l'hôte `http://127.0.0.1:8000/doc` qui vous permet d'interagir avec votre API et de voir si vous avez des erreurs.

![Cette documentation interactive fournie par swagger montre comment interagir avec votre API pour vérifier les erreurs.](https://lh3.googleusercontent.com/3WeI9jW_jeI0WMYhYrWjMUFsbwD6cAANv1DuYNkC2hhl2-HyBMQjEeX5SABC4GdbMyArs88-DkxdgTNES2ogHjFNBMqvNNFyUq3825kBxFGgazth3TWrMv72Qm_9kGs6atTFUSl6NnjeYkdaxHlV7XqFg8JMK9v6t5Dq5rUCxKU7SHv-wZnBPpIy3U31ag align="left")

*Cette documentation interactive fournie par swagger montre comment interagir avec votre API pour vérifier les erreurs.*

## Comment configurer ngrok

Pour recevoir des messages Twilio sur le backend, vous utiliserez `ngrok` pour héberger l'hôte local sur un serveur public. Lisez cet [article](https://www.twilio.com/blog/using-ngrok-2022#:~:text=Open%20a%20terminal%20window%20and,under%20your%20account%2C%20without%20restrictions.) pour apprendre comment configurer ngrok sur votre machine.

Sur l'administrateur ngrok, exécutez la commande ngrok http 8000. Cela rend votre hôte public, et vous pouvez recevoir des messages sur votre backend.

![Ici, vous pouvez voir ngrok en cours d'exécution sur votre machine locale](https://lh6.googleusercontent.com/6oErUtc-WBw1YBNLaw8yjfiMioLW7PpTmUWJY4Y6nrOJ3Q0iKC5fnN8YAvVxBWMYHO296TkMwo7NyKptqOWS_tv_ftUe1Mqetkoz57HCP_rzp3lrjgpvreSkJlPKPV-GA9kQVNbp2biQVSIg-l2uGKKVMFEGG-EHSl57fF_HqiOBE-iXP_4BwAwfHc7KIA align="left")

*Ici, vous pouvez voir ngrok en cours d'exécution sur votre machine locale*

Allez dans votre bac à sable WhatsApp, sous les paramètres du bac à sable, et collez l'URL de transfert `https://b5a6-105-112-120-51.ngrok-free.app` en y ajoutant `/message` sous **When a message comes in** et cliquez sur Save.

![Cette image montre comment configurer votre bac à sable et le lier à l'URL ngrok](https://lh6.googleusercontent.com/VejaBgdyh6Zf5bUCIQyyCZjTvQhWSpEadbP0FliUyOH64QC8fQn9P7wRDgElxo8h7_T7SuleXD01PAeH8hirp2Gn4CaCBDi7IDuIC8V5CfFsjzU-yKxL1_67rCQZ2H77IRpPr0R7P6IegfjyQ72JH-xAjEk0Y-RyckeBM7mFOaoRSrtjMBX3wHDJ1l3QZg align="left")

*Cette image montre comment configurer votre bac à sable et le lier à l'URL ngrok*

## Comment se connecter à l'API Merriam-Webster

Pour configurer un compte de dictionnaire Merriam-Webster, [allez ici](https://www.dictionaryapi.com/register/index) et remplissez vos informations d'identification :

![Image montrant la page pour s'inscrire au Merriam Webster Developer Center](https://lh4.googleusercontent.com/hQ5PhqXwHF1sVLOzsPIf5ehtM7VaGRwEwbA9l11HtIcZnhtkU0HAfR2R9dvXVl0lfmtO1ORIQwFUtNH3tl1Ck-S5e5AeGrHUU4Yq6IusrAKDI4iX4RI5u71whmBiw2jCH_cj0dolHjYjXxEVHInwrxFdH6qrbU3KGKRyKoC-rkEH2qv_DbUiBSCM-pviSg align="left")

*Image montrant la page pour s'inscrire au Merriam Webster Developer Center*

Vous pouvez vous inscrire pour deux clés : Collegiate Dictionary et Collegiate Thesaurus, bien que ce tutoriel utilise uniquement **Collegiate Dictionary**.

![Cela montre les différentes clés que l'on peut demander sur Merriam-Webster](https://lh3.googleusercontent.com/UUUGKxVa_DHx0yelDHCwFzX0uFj3K5tfp6nt4RczGAHnlj1UNZlRxjvXBAsS5_TMcbpnm2jYXWKed_Ek9vAM-qS544fS7mXJTAvdNXYH8tGih6bS7qXozWv5J4-52x1V9Cw1i76-MevLUiMwWuPmi_0EwzB-v2VyzV0kSpaun2Ok5TlmjqXAM6b-w84PvQ align="left")

*Cela montre les différentes clés que l'on peut demander sur Merriam-Webster*

Après avoir rempli tous vos détails, cliquez sur Register et Login.

Dans l'onglet home, allez dans Keys pour obtenir vos clés API.

![Cet onglet de clé montre les clés que vous avez enregistrées](https://lh6.googleusercontent.com/y_AGpxS8q4Pj-jscWFggBGDXgqE7amA7GygGPXknOtNTcATjdU716lvbIgHGOPo-cxIbdQ4q4RBfP8C4sXwGJlAw5SrpOH3uXf6rDCPh78jweyHYSYDyB_NSJ4SsYhnOqJWP788Yj3swTSUq2ostt2kHssn1KL3mFo3e-L_Y400-7amgsiWqHYfvbJZewA align="left")

*Cet onglet de clé montre les clés que vous avez enregistrées*

Mettez à jour le fichier .env, en enregistrant la clé comme `DICTIONARY_KEY`.

```text
MONGO_SECRET="<password>"
TWILIO_ACCOUNT_SID="<account_sid>"
TWILIO_AUTH_TOKEN="<auth_token>"
TWILIO_NUMBER="<twilio_number>"
TO_NUMBER="<to_number>"
DICTIONARY_API_KEY="<dictionary_key>"
```

Mettez à jour le fichier `main.py` comme suit :

```python
from fastapi import FastAPI, Form
import requests
from utils import send_message
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

app = FastAPI()
whatsapp_number = os.getenv("TO_NUMBER")
api_key = os.getenv("DICTIONARY_API_KEY")

@app.post("/message")
async def reply(Body: str = Form()):
    url = f"<https://www.dictionaryapi.com/api/v3/references/collegiate/json/{Body}?key={api_key}>"
    response = requests.get(url)
    # Extraire les données JSON de la réponse
    data = response.json()
    
    definition = data[0]["shortdef"][0]

    send_message(whatsapp_number, definition)
```

`@app.post("/message")` est un décorateur dans le framework fastAPI qui définit une route de requête POST vers l'URL `/message`. La fonction reply définie ci-dessus est appelée lorsqu'une requête POST est envoyée à cette URL.

La fonction `reply` prend un paramètre Body dans le corps de la requête, qui est le message envoyé au chatbot (le mot dont vous voulez obtenir la définition). Elle envoie ensuite une requête HTTP à l'API Merriam-Webster pour récupérer la signification du mot.

La variable `url` stocke le lien vers l'API Merriam-Webster, qui prend le `Body` et la `api_key` pour obtenir des détails concernant le mot fourni.

Vous pouvez faire des requêtes à partir de `url` en utilisant `requests` de la bibliothèque `request` et stocker `request.get(url)` dans la variable `response`.

Vous extrayez ensuite les données JSON de la réponse en utilisant `response.json()` et les stockez dans la variable data.

`data[0]["shortdef"][0]` vous permet d'accéder à la définition courte d'un mot stockée dans la variable definition.

`send_message()` prend la définition et l'envoie à `whatsapp_number`.

Ensuite, vous devrez gérer les situations où quelqu'un envoie une phrase au lieu d'un mot, ou un mot contenant des ponctuations ou des caractères. Mettez donc à jour `main.py` comme suit :

```python
from fastapi import FastAPI, Form
import requests
from utils import send_message
from dotenv import load_dotenv
import os
from typing import List
from models import dictionary_collection

load_dotenv()

app = FastAPI()
whatsapp_number = os.getenv("TO_NUMBER")
api_key = os.getenv("DICTIONARY_API_KEY")

@app.post("/message")
async def reply(Body: str = Form()):
    url = f"<https://www.dictionaryapi.com/api/v3/references/collegiate/json/{Body}?key={api_key}>"
    flag="Please give a valid word"
    
    if Body.isalpha():
        response = requests.get(url)
        # Extraire les données JSON de la réponse
        data = response.json()
        
        definition = data[0]["shortdef"][0]

        send_message(whatsapp_number, definition)
    else:
        return send_message(whatsapp_number, flag)
    
    return ""
```

`flag` est une variable stockant le message à donner si vous fournissez une phrase ou un mot avec des caractères.

La condition `if` vérifie si un message est un mot via `Body.isaplha()`, si vrai, il obtient la définition de l'API Merriam-Webster, si faux, il retourne la fonction `send_message()` disant à l'utilisateur de *Please give a valid word.*

Pour stocker les mots et leurs significations dans la base de données MongoDB, mettez à jour `main.py` comme suit :

```python
from fastapi import FastAPI, Form
import requests
from utils import send_message
from dotenv import load_dotenv
import os
from typing import List
from models import dictionary_collection

load_dotenv()

app = FastAPI()
whatsapp_number = os.getenv("TO_NUMBER")
api_key = os.getenv("DICTIONARY_API_KEY")

@app.post("/message")
async def reply(Body: str = Form()):
    url = f"<https://www.dictionaryapi.com/api/v3/references/collegiate/json/{Body}?key={api_key}>"
    flag="Please give a valid word"
    
    if Body.isalpha():
        response = requests.get(url)
        # Extraire les données JSON de la réponse
        data = response.json()
        
        definition = data[0]["shortdef"][0]

        send_message(whatsapp_number, definition)

        dictionary_db = {"word":Body, "definition":definition}
        dictionary_collection.insert_one(dictionary_db)

    else:
        return send_message(whatsapp_number, flag)
    
    return ""
```

`dictionary_db = {"word": Body, "definition": definition}` crée un dictionnaire avec deux clés, *word* et *definition*, et les valeurs *Body* et *definition*, respectivement.

`dictionary_collection.insert_one(dictionary_db)` insère le dictionnaire dans la collection MongoDB, nommée `dictionary_collection`.

Vous pouvez aller sur votre tableau de bord et voir les éléments ajoutés à la collection.

![Cela contient les éléments qui ont été envoyés et reçus sur votre application](https://lh6.googleusercontent.com/57-VBBJTN9D7J-0Nhv7gm15kFnf8QrOqajdYc1-1THtnfMhDes2B8ZOtEr02JyskDjTEcwPO4Lpvbe5Hd0-OabelyEcYeh9-jUhtOmEvSDDSHxitTQeScjH6bZivfgadAXT7z3T1yJpOnDRb0i2AvI9PEdPSFI_zAO7F0xa0fQhKGkxR6Aeru0j6aXs3WA align="left")

*Cela contient les éléments qui ont été envoyés et reçus sur votre application*

## Tester le ChatBot

Maintenant, vous pouvez discuter avec le chatbot et demander des définitions de mots :

![Image montrant une discussion avec le chatbot dictionnaire](https://lh3.googleusercontent.com/mZnfLJrDEJwMI7oLO9_a1ILmJjGq_NbEllAy_zbOETOEXZ60OV7XScul8GOWE2kvYM4nFvFX_n0QWQ-ffSTf2p2wfsIO4i66uKVxG80SFjDgLaY99EqWPykryl3EgABNYQaE8sYEaFo_69hgfMm0rd78UtPk-zT7NNfUjfSxC2znO6_JZ1oS7e4TIguJPw align="left")

*Image montrant une discussion avec le chatbot dictionnaire*

## Conclusion

Dans ce tutoriel, vous avez appris à créer un chatbot dictionnaire WhatsApp. Vous avez appris à utiliser FastAPI pour alimenter le backend de votre application, à interagir avec l'API Twilio MessagingX WhatsApp, et à utiliser une base de données NoSQL comme MongoDB pour stocker vos données.

Vous pouvez étendre le chatbot pour obtenir des synonymes et des définitions de mots avec plus d'une explication en accédant à plus de métadonnées de l'API Merriam-Webster.

Vous pouvez consulter la [documentation de l'API Merriam-Webster](https://www.dictionaryapi.com/products/json) pour les différentes réponses que vous pouvez obtenir. Assurez-vous de lire la [documentation de l'API Twilio WhatsApp](https://www.twilio.com/docs/whatsapp/quickstart/python) pour des fonctionnalités plus avancées comme l'obtention de réponses multimédias et la prononciation des mots.