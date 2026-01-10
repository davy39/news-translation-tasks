---
title: Comment construire un cryptobot en Python et le connecter à Facebook Messenger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T17:03:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-cryptobot-in-python-and-connect-it-to-facebook-messenger-4bba14107fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bXgJOdnBncMGMKKJVPCbmw.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: Cryptocurrency
  slug: cryptocurrency
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment construire un cryptobot en Python et le connecter à Facebook Messenger
seo_desc: 'By Paul Pinard

  Meet Sato the Cryptobot, who is able to fetch any cryptocurrency price from an external
  API!


  Chatbots have an incredible potential. Yet, for bots to be efficient, they must
  integrate and exchange data with existing services and proces...'
---

Par Paul Pinard

#### Rencontrez Sato le Cryptobot, capable de récupérer le prix de toute cryptomonnaie depuis une API externe !

![Image](https://cdn-media-1.freecodecamp.org/images/nkzd3jArmXtaw3vlJ2FJzSBC6ba6qnreD4nM)

Les chatbots ont un potentiel incroyable. Pourtant, pour que les bots soient efficaces, ils doivent s'intégrer et échanger des données avec des services et des processus existants.

**La capacité à récupérer des données depuis une API externe permet des cas d'utilisation plus complexes qu'une simple logique de questions-réponses**. De plus, cette capacité combinée avec le NLP offre encore plus d'opportunités.

Par exemple, Sato — le cryptobot que nous allons construire aujourd'hui — est capable de reconnaître toutes les cryptomonnaies, même celles qui ne sont pas encore listées. Je n'aurai rien à faire pour qu'il puisse traiter des requêtes sur des cryptos apparaissant même dans des années, car Sato, au fond, a compris ce qu'est un symbole de cryptomonnaie (après avoir été nourri avec des milliers d'exemples).

### Que construisons-nous aujourd'hui ?

À la fin de ce tutoriel, nous aurons un bot capable de récupérer des données depuis une API tierce en fonction des entrées de nos utilisateurs, et de leur répondre avec la valeur récupérée. Voici le résultat final de ce que nous allons construire aujourd'hui : un cryptobot aka un chatbot capable de récupérer le prix de toute cryptomonnaie.

![Image](https://cdn-media-1.freecodecamp.org/images/mVEyhtJ375H0xIgX8Wiu6h2FgHfbnIKz5Rb6)
_Ce que vous aurez à la fin de ce tutoriel_

Pressé ? Voici tout ce dont vous avez besoin pour construire le vôtre :

* Un chatbot créé avec [SAP Conversational AI](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c). Inscrivez-vous [ici](https://cai.tools.sap/signup?utm_source=freecodecamp&utm_medium=blog&utm_campaign=LG2019), c'est totalement gratuit !
* [Le dépôt GitHub](https://github.com/Ahirice/sato/)

Besoin de le voir pour le croire ? C'est sage ! Cliquez [ici](https://www.messenger.com/login.php?next=https%3A%2F%2Fwww.messenger.com%2Ft%2Fsatofolio) !

Ou si vous préférez comprendre comment il a été fait, suivez le tutoriel.

### 1. Construire la base de votre chatbot : choisissez votre chemin

L'objectif aujourd'hui est de construire un bot capable de reconnaître une question sur le prix de toute cryptomonnaie. Laissez libre cours à votre imagination, **cela pourrait être vraiment n'importe quoi impliquant des données disponibles sur des API tierces**.

Avant de plonger dans le tutoriel, laissez-moi vous donner quelques informations sur le fonctionnement de Sato.

#### Rencontrez Sato, le cryptobot

Sato est un bot conçu pour répondre aux questions de base sur les cryptomonnaies et récupérer leurs prix. Voici un aperçu de ce qu'il peut faire :

1. Récupérer les prix des cryptomonnaies (ce que nous allons construire aujourd'hui) : Sato reconnaît les symboles des cryptomonnaies (« ETH », « BTC ») et récupère leur prix sur l'API [cryptocompare](https://www.cryptocompare.com/api/) pour enfin retourner les valeurs en BTC et USD à l'utilisateur.
2. Répondre aux questions des utilisateurs sur les portefeuilles — portefeuilles en ligne, portefeuilles d'échange, portefeuilles froids et portefeuilles matériels.
3. Aborder les questions sur les clés privées et publiques ainsi que la sécurité des cryptomonnaies.
4. Présenter brièvement les principales cryptomonnaies, actuellement BTC, ETH, BCH et LTC.

#### À l'intérieur de Sato

Aujourd'hui, nous nous concentrerons sur la compétence de récupération des prix des cryptos, car elle nécessite un appel à une API externe. Essentiellement, Sato a besoin de trois choses pour pouvoir détecter une question sur le prix des cryptos et retourner la valeur demandée :

Premièrement, il a besoin d'une intention [(@crypto_price](https://cai.tools.sap/ahirice/sato-cryptobot/train/crypto_price?utm_source=blog&utm_campaign=sato)) avec des expressions diverses et des cryptomonnaies mentionnées, afin qu'il puisse reconnaître efficacement ces questions. Voici quelques-unes des expressions utilisées pour définir l'intention @crypto_price :

![Image](https://cdn-media-1.freecodecamp.org/images/9xvqHOnxa19Q2lJZALPpNX3Drn9ji7GvnPsc)
_Un échantillon des expressions utilisées pour définir l'intention @crypto_price_

Deuxièmement, pour que Sato puisse reconnaître toutes les cryptomonnaies, il aura besoin de la plus grande liste que vous puissiez trouver. J'en ai trouvé 1200+ sur CoinMarketCap, ce qui est suffisant pour commencer. J'ai créé un gazette des noms de crypto pour améliorer sa compréhension.

Troisièmement, nous devrons construire une compétence qui se déclenche lorsque l'intention @ask_price ou l'entité #crypto_name est reconnue :

![Image](https://cdn-media-1.freecodecamp.org/images/ODAOHbkV4oNuDxMlCBybhtorXtXsrbPDBmdr)
_Sato — Cryptobot / déclencheurs de compétence crypto_main_

Vous pouvez également ajouter #crypto_name comme exigence, pour vous assurer qu'aucun appel d'API n'est déclenché sans paramètres :

![Image](https://cdn-media-1.freecodecamp.org/images/bpD4Pbv-Tuxr47GSwC2fqGyhMe-SqHG6uTC4)
_Sato — Cryptobot / exigences de compétence crypto_main_

Cette compétence doit également appeler votre webhook que nous allons configurer ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/135D8rog-svOYx2Ypr0trbn0TtGLHM4T6n-w)
_Sato — Cryptobot / actions de compétence crypto_main_

N'oubliez pas d'ajouter une réinitialisation de la mémoire après le déclenchement du webhook, cela est nécessaire pour nettoyer la mémoire après chaque réponse.

Enfin, nous testerons notre bot directement dans Messenger, vous devrez donc créer une page et une application et les connecter. Tout est documenté dans l'onglet `CONNECT` et dans le [tutoriel de démarrage](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/).

Pour rester concis, **ce tutoriel ne détaillera pas la création d'un bot**. Nous partirons d'un bot déjà fonctionnel.

Pour me rejoindre là-bas, vous avez deux options :

* Option A : construisez votre propre bot (qui n'a pas besoin d'être un cryptobot) en suivant le tutoriel de démarrage et en créant un [compte sur SAP Conversational AI](https://cai.tools.sap/signup?utm_source=freecodecamp&utm_medium=blog&utm_campaign=LG2019).
* Option B : [forker Sato](https://cai.tools.sap/ahirice/sato-cryptobot/train/intents) et commencer à partir de là. C'est pourquoi SAP Conversational AI est une plateforme de chatbot collaborative. Cela fonctionne presque comme GitHub !

![Image](https://cdn-media-1.freecodecamp.org/images/QZmtXl1BvCSUOw71M02FiAvKyzYnU0tqrYuN)
_Forker un bot sur SAP Conversational AI_

### 2. Code serveur de base et exigences

Puisque nous voulons interagir avec notre bot, nous aurons besoin d'un serveur pour pouvoir recevoir les résultats du NLP effectué par SAP Conversational AI et envoyer nos réponses.

Sur le [constructeur de bot](https://cai.tools.sap/bot-builder), allez dans l'onglet `CODE` pour trouver un exemple de code de base nécessaire pour démarrer votre API. Nous donnons des exemples en Node.JS, PHP, Python et Ruby. Ce tutoriel sera uniquement en Python.

Voici le code de base pour Python :

```
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  print(json.loads(request.get_data()))
  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Roger that',
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
```

Prenez le temps de regarder le code pour mieux comprendre ce que nous allons faire : nous allons construire sur ce code pendant ce tutoriel. Vous pouvez l'enregistrer dans votre éditeur de texte préféré pour l'instant.

#### Exigences

Comme vous pouvez le voir, le script du serveur utilise [Flask comme framework web](http://flask.pocoo.org/), nous en aurons donc besoin.

Pour l'appel API, nous utiliserons également [Requests](http://docs.python-requests.org/en/master/). Allons-y et installons les deux :

```
pip install Flask
pip install requests
```

### 3. Tester le serveur : NGROK

Maintenant que nous avons le serveur de base, faisons-le fonctionner et testons-le. Cela nous permettra d'être plus progressifs dans le processus afin que le débogage (si nécessaire) soit simplifié.

Pour exposer notre serveur local à Internet, nous aurons besoin de ngrok.

_Note : Si vous utilisez Windows comme moi, il existe un gestionnaire de paquets génial, [Chocolatey](https://chocolatey.org/) qui fonctionne presque comme apt-get sur UNIX. Avec lui, vous pourrez installer ngrok en une ligne `choco install ngrok_portable`. De plus, Chocolatey ajoute ngrok à votre PATH, vous permettant de démarrer ngrok à partir de n'importe quel terminal simplement en tapant `ngrok`._

Maintenant, il est temps de démarrer notre serveur et de le tester, cela implique :

1. Définir un déclencheur de webhook dans votre bot (détaillé dans l'étape 1)
2. Exécuter votre script Python
3. Exposer le port 5000 à Internet avec ngrok : `ngrok http 5000`
4. Copier l'URL de redirection de ngrok et la coller comme URL de base de votre bot sur SAP Conversational AI

### 4. Préparer l'appel à l'API externe

Il est temps de commencer à construire ! Jetons un coup d'œil à l'appel API que nous allons faire pour obtenir le prix de toute cryptomonnaie. Plusieurs API sont disponibles à cet effet, alors je suis allé de l'avant et j'en ai choisi une : [Cryptocompare API](https://www.cryptocompare.com/api/).

[Cryptocompare API](https://www.cryptocompare.com/api/) offre des milliers de possibilités, mais pour simplifier, nous en resterons aux bases. **Nous voulons le prix de la crypto correspondante en BTC, USD et EUR**.

Voici comment l'appel est structuré (ici pour ETH) :

`https://min-api.cryptocompare.com/data/price?fsym="ETH"&tsyms=BTC,USD,EUR"`

Vous avez deux paramètres :

* `fsym` : le symbole de la cryptomonnaie, c'est ici que nous devrons récupérer le crypto_name reconnu dans l'entité #crypto_name.
* `tsyms` : la devise dans laquelle le prix sera retourné. Nous avons choisi BTC, USD et EUR ici.

Donc, dans notre cas, nous n'aurons besoin d'adapter que le paramètre `fsym` à la cryptomonnaie reconnue, tandis que le reste de l'appel reste le même.

### 5. Adapter l'appel API pour inclure le symbole reconnu dans l'entrée utilisateur

Maintenant que nous savons comment récupérer les prix, nous devons revenir à notre code serveur et le mettre à niveau pour qu'il puisse :

* Connaître le #crypto_name reconnu par SAP Conversational AI.
* Faire un appel API à Cryptocompare en utilisant le #crypto_name.

Commençons !

#### Étape 1 : Trouver nos données dans le JSON de SAP Conversational AI

Jetons un coup d'œil aux données retournées par SAP Conversational AI sur une entrée utilisateur. Pour ce faire, vous cliquez sur le bouton `CHAT WITH YOUR BOT` présent sur toutes les pages, dans le coin inférieur droit. Ensuite, vous pouvez basculer entre la conversation et la vue JSON en cliquant sur le cercle d'information orange comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/L640-OoPuVyK3rF5SAEYQXI2ss4qv2sTE4Cf)
_Vérifiez le JSON de la conversation._

Ici, notre symbole est accessible avec `['conversation']['memory']['crypto']['raw']`. Puisque la valeur et le raw sont identiques dans ce cas, vous pouvez utiliser l'un ou l'autre.

Sur notre serveur, le JSON retourné par le panneau de test du site est **encapsulé dans le dictionnaire `data`** (voir le code du serveur). Nous avons donc besoin d'une étape supplémentaire pour le récupérer sur notre serveur :

```
# RÉCUPÉRER LE NOM DE LA CRYPTO
crypto_name = data['conversation']['memory']['crypto']['value']
```

#### Étape 2 : Faire un appel API en utilisant l'entité reconnue

```
import requests
r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
```

Allez-y et imprimez-le, mais vous pourriez être déçu :

![Image](https://cdn-media-1.freecodecamp.org/images/AN1-kvadGRTMSbUU3P0oyVnnHAnvmpcYrOFo)

En effet, si vous voulez obtenir les valeurs retournées par l'appel, vous devez imprimer `r.json()`. La bonne nouvelle est que le JSON retourné par Cryptocompare est vraiment aussi simple que possible :

![Image](https://cdn-media-1.freecodecamp.org/images/aDUzK6ox4aFmpZgkZul3M8KKFNZbtyGawLjH)
_JSON de Cryptocompare_

Super ! Maintenant, il ne nous reste plus qu'une dernière étape à comprendre : retourner les prix à l'utilisateur.

#### Étape 3 : Retourner les données récupérées à l'utilisateur

Maintenant, il est temps de terminer la mise à niveau de notre code serveur de base : nous devons modifier les réponses retournées pour inclure nos données fraîchement récupérées. Pour ce faire, nous allons modifier le message retourné par notre code serveur :

```
return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Roger that',
    }],
```

Nous allons modifier uniquement les réponses, pour inclure les prix que nous avons récupérés :

```
replies=[{
     'type': 'text',
     'content': 'Le prix de %s est %f BTC et %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
   }],
```

Puisque la réponse est une chaîne de caractères, nous devons utiliser l'opérateur modulo (%) pour inclure nos prix dans la chaîne. Ici, le premier %s indique à Python de chercher une chaîne de caractères tandis que les deux %f suivants indiquent des flottants.

Notre serveur mis à niveau est maintenant terminé, voici le code complet :

```
from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())
  # RÉCUPÉRER LE NOM DE LA CRYPTO
  crypto_name = data['conversation']['memory']['crypto']['raw']
  # RÉCUPÉRER LES PRIX EN BTC/USD/EUR
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Le prix de %s est %f BTC et %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
```

Avec notre nouveau serveur terminé, nous avons maintenant toutes les pièces de notre puzzle. Assemblons-les :

1. Exécutez votre script Python,
2. Exposez le port 5000 à Internet avec ngrok : `ngrok http 5000`,
3. Copiez l'URL de redirection de ngrok et collez-la comme URL de base de votre bot sur SAP Conversational AI

Maintenant que vous avez les bases pour construire un bot capable de récupérer des données tierces, à vous de jouer !

PS : Puisque ce tutoriel utilise ngrok, votre ordinateur doit être allumé et ngrok doit être en cours d'exécution pour que votre bot fonctionne.

Publié à l'origine sur le [blog SAP Conversational AI](https://cai.tools.sap/blog/python-cryptobot/).