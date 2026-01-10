---
title: Tutoriel Python Discord Bot – Codez un Bot Discord et Hébergez-le Gratuitement
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-12-15T16:25:09.000Z'
originalURL: https://freecodecamp.org/news/create-a-discord-bot-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/discordbot.png
tags:
- name: discord
  slug: discord
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Tutoriel Python Discord Bot – Codez un Bot Discord et Hébergez-le Gratuitement
seo_desc: 'This tutorial will show you how to build your own Discord bot completely
  in the cloud.

  You do not need to install anything on your computer, and you do not need to pay
  anything to host your bot.

  We are going to use a number of tools, including the Di...'
---

Ce tutoriel vous montrera comment construire votre propre bot Discord entièrement dans le cloud.

Vous n'avez pas besoin d'installer quoi que ce soit sur votre ordinateur, et vous n'avez pas besoin de payer pour héberger votre bot.

Nous allons utiliser plusieurs outils, dont l'API Discord, des bibliothèques Python et une plateforme de cloud computing appelée [Repl.it](https://www.repl.it).

Il existe également une version vidéo de ce tutoriel écrit. La vidéo est intégrée ci-dessous et la version écrite se trouve après la vidéo.

%[https://youtu.be/SPTfmiYiuok]

## Comment Créer un Compte de Bot Discord

Pour travailler avec la bibliothèque Python et l'API Discord, nous devons d'abord créer un compte de bot Discord.

Voici les étapes pour créer un compte de bot Discord.

1. Assurez-vous d'être connecté au [site web de Discord](https://discord.com).

2. Accédez à la [page des applications](https://discord.com/developers/applications).

3. Cliquez sur le bouton "Nouvelle Application".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-117.png)

4. Donnez un nom à l'application et cliquez sur "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-118.png)

5. Allez dans l'onglet "Bot" puis cliquez sur "Ajouter un Bot". Vous devrez confirmer en cliquant sur "Oui, faites-le !"

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-119.png)

Conservez les paramètres par défaut pour **Public Bot** (coché) et **Require OAuth2 Code Grant** (décoché).

Votre bot a été créé. L'étape suivante consiste à copier le token.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-122.png)

Ce token est le mot de passe de votre bot, ne le partagez donc avec personne. Il pourrait permettre à quelqu'un de se connecter à votre bot et de faire toutes sortes de mauvaises choses.

Vous pouvez régénérer le token s'il est accidentellement partagé.

## Comment Inviter Votre Bot à Rejoindre un Serveur

Maintenant, vous devez faire en sorte que votre Bot User rejoigne un serveur. Pour ce faire, vous devez créer une URL d'invitation pour celui-ci.

Allez dans l'onglet "OAuth2". Ensuite, sélectionnez "bot" dans la section "scopes".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-123.png)

Maintenant, choisissez les permissions que vous souhaitez pour le bot. Notre bot va principalement utiliser des messages textuels, donc nous n'avons pas besoin de nombreuses permissions. Vous pourriez avoir besoin de plus selon ce que vous voulez que votre bot fasse. Soyez prudent avec la permission "Administrateur".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-124.png)

Après avoir sélectionné les permissions appropriées, cliquez sur le bouton 'copier' au-dessus des permissions. Cela copiera une URL qui peut être utilisée pour ajouter le bot à un serveur.

Collez l'URL dans votre navigateur, choisissez un serveur pour inviter le bot et cliquez sur "Autoriser".

Pour ajouter le bot, votre compte a besoin des permissions "Gérer le Serveur".

Maintenant que vous avez créé le bot user, nous allons commencer à écrire le code Python pour le bot.

## Comment Coder un Bot Discord Basique avec la Bibliothèque discord.py

Nous allons utiliser la bibliothèque Python discord.py pour écrire le code du bot. discord.py est un wrapper d'API pour Discord qui facilite la création d'un bot Discord en Python.

### Comment Créer un Repl et Installer discord.py

Vous pouvez développer le bot sur votre ordinateur local avec n'importe quel éditeur de code. Cependant, dans ce tutoriel, nous allons utiliser Repl.it car cela simplifiera le suivi pour tout le monde. Repl.it est un IDE en ligne que vous pouvez utiliser dans votre navigateur web.

Commencez par aller sur [Repl.it](https://repl.it). Créez un nouveau Repl et choisissez "Python" comme langage.

Pour utiliser la bibliothèque discord.py, il suffit d'écrire `import discord` en haut de `main.py`. Repl.it installera automatiquement cette dépendance lorsque vous appuierez sur le bouton "run".

Si vous préférez coder le bot localement, vous pouvez utiliser cette commande sur MacOS pour installer discord.py :

`python3 -m pip install -U discord.py`

Vous devrez peut-être utiliser `pip3` au lieu de `pip`.

Si vous utilisez Windows, vous devez utiliser la ligne suivante :

`py -3 -m pip install -U discord.py`

### Comment Configurer les Événements Discord pour Votre Bot

discord.py tourne autour du concept d'événements. Un événement est quelque chose que vous écoutez et auquel vous répondez. Par exemple, lorsqu'un message est envoyé, vous recevez un événement à ce sujet auquel vous pouvez répondre.

Créons un bot qui répond à un message spécifique. Ce code de bot simple, ainsi que l'explication du code, est tiré de [la documentation discord.py](https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot). Nous ajouterons plus de fonctionnalités au bot plus tard.

Ajoutez ce code à main.py. (Vous pouvez nommer le fichier autre chose si vous le souhaitez, mais pas discord.py.) Je vais expliquer ce que fait tout ce code sous peu.

```python
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Nous nous sommes connectés en tant que {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Bonjour !')

client.run(os.getenv('TOKEN'))
```

Lorsque vous avez créé votre bot user sur Discord, vous avez copié un token. Maintenant, nous allons créer un fichier `.env` pour stocker le token. Si vous exécutez votre code localement, vous n'avez pas besoin du fichier `.env`. Il suffit de remplacer `os.getenv('TOKEN')` par le token.

Les fichiers `.env` sont utilisés pour déclarer des variables d'environnement. Sur Repl.it, la plupart des fichiers que vous créez sont visibles par tout le monde, mais les fichiers `.env` ne sont visibles que par vous. Les autres personnes consultant un repl public ne pourront pas voir le contenu du fichier `.env`.

Donc, si vous développez sur Repl.it, n'incluez des informations privées comme des tokens ou des clés que dans un fichier `.env`.

Cliquez sur le bouton "Ajouter un fichier" et créez un fichier nommé `.env`.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-19-1.png)

À l'intérieur du fichier, ajoutez la ligne suivante, y compris votre token réel que vous avez copié précédemment :

```
TOKEN=[coller le token ici]
```

Maintenant, passons en revue ce que fait chaque ligne de code dans votre code de bot Discord.

1. La première ligne importe la bibliothèque discord.py.
2. La deuxième ligne importe la bibliothèque os, mais celle-ci n'est utilisée que pour obtenir la variable `TOKEN` à partir du fichier `.env`. Si vous n'utilisez pas de fichier `.env`, vous n'avez pas besoin de cette ligne.
3. Ensuite, nous créons une instance de [`Client`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client). C'est la connexion à Discord.
4. Le décorateur `[@client.event()](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.event)` est utilisé pour enregistrer un événement. Il s'agit d'une bibliothèque asynchrone, donc les choses sont faites avec des rappels. Un rappel est une fonction qui est appelée lorsque quelque chose d'autre se produit. Dans ce code, l'événement `[on_ready()](https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready)` est appelé lorsque le bot est prêt à être utilisé. Ensuite, lorsque le bot reçoit un message, l'événement `[on_message()](https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message)` est appelé.
5. L'événement `[on_message()](https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message)` se déclenche chaque fois qu'un message est reçu, mais nous ne voulons pas qu'il fasse quoi que ce soit si le message vient de nous-mêmes. Donc, si le `[Message.author](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.author)` est le même que le `[Client.user](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.user)`, le code retourne simplement.
6. Ensuite, nous vérifions si le [`Message.content`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.content) commence par `'$hello'`. Si c'est le cas, alors le bot répond avec `'Bonjour !'` dans le canal où il a été utilisé.
7. Maintenant que le bot est configuré, la dernière ligne exécute le bot avec le token de connexion. Il obtient le token à partir de notre fichier `.env`.

Nous avons le code pour le bot, maintenant nous devons simplement l'exécuter.

### Comment Exécuter le Bot

Maintenant, cliquez sur le bouton run en haut pour exécuter votre bot dans repl.it.

Si vous écrivez le bot localement, vous pouvez utiliser ces commandes dans le terminal pour exécuter le bot :

Sur Windows :

`py -3 main.py`

Sur les autres systèmes :

`python3 main.py`

Maintenant, allez dans votre salon Discord et tapez "$hello". Votre bot devrait retourner "Bonjour !".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-141.png)

## Comment Améliorer le Bot

Maintenant que nous avons un bot de base qui fonctionne, nous allons l'améliorer. Il s'appelle "Encourage Bot" pour une raison.

Ce bot répondra avec un message d'encouragement chaque fois que quelqu'un envoie un message contenant un mot triste ou déprimant.

N'importe qui pourra ajouter des messages d'encouragement pour que le bot les utilise et les messages soumis par les utilisateurs seront stockés dans la base de données de Repl.it.

Le bot retournera également une citation inspirante aléatoire à partir d'une API lorsque quelqu'un tapera le message "$inspire" dans le chat.

Nous commencerons par ajouter la fonctionnalité "$inspire".

### Comment Ajouter des Citations Inspirantes au Bot

Nous obtiendrons des citations inspirantes à partir d'une API appelée zenquotes.io. Nous devons importer quelques modules Python supplémentaires, ajouter une fonction `get_quote()` et mettre à jour notre code de bot pour appeler la fonction.

Voici le code mis à jour. Après le code, j'expliquerai les nouvelles parties.

```python
import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Nous nous sommes connectés en tant que {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
```

Nous devons maintenant importer le module `requests`. Ce module permet à notre code de faire une requête HTTP pour obtenir des données à partir de l'API. L'API retourne du JSON, donc le module `json` facilite le travail avec les données retournées.

La fonction `get_quote()` est assez simple. Tout d'abord, elle utilise le module requests pour demander des données à partir de l'URL de l'API. L'API retourne une citation inspirante aléatoire. Cette fonction pourrait facilement être réécrite pour obtenir des citations à partir d'une API différente, si celle-ci cesse de fonctionner.

Ensuite, à l'intérieur de la fonction, nous utilisons `json.loads()` pour convertir la réponse de l'API en JSON. Par essais et erreurs, j'ai découvert comment obtenir la citation à partir du JSON dans le format de chaîne que je voulais. La citation est retournée par la fonction sous forme de chaîne.

La dernière partie mise à jour dans le code se trouve vers la fin. Auparavant, elle recherchait un message commençant par "$hello". Maintenant, elle recherche "$inspire". Au lieu de retourner "Bonjour !", elle obtient la citation avec `quote = get_quote()` et retourne la citation.

À ce stade, vous pouvez exécuter votre code et l'essayer.

## Comment Ajouter des Messages d'Encouragement au Bot

Maintenant, nous allons implémenter la fonctionnalité où le bot répond avec des messages d'encouragement lorsqu'un utilisateur publie un message avec un mot triste.

### Comment Ajouter des Mots Tristes au Bot

Tout d'abord, nous devons créer une liste Python qui contient les mots tristes auxquels le bot répondra.

Ajoutez la ligne suivante après la création de la variable `client` :

`sad_words = ["triste", "déprimé", "malheureux", "en colère", "misérable"]`

N'hésitez pas à ajouter plus de mots à la liste.

### Comment Ajouter des Messages d'Encouragement au Bot

Maintenant, nous allons ajouter une liste de messages d'encouragement auxquels le bot répondra.

Ajoutez la liste suivante après la liste `sad_words` que vous avez créée :

```python
starter_encouragements = [
  "Remontez le moral !",
  "Accrochez-vous.",
  "Vous êtes une personne / un bot génial !"
]
```

Comme avant, n'hésitez pas à ajouter plus de phrases de votre choix à la liste. Je n'utilise que trois éléments pour l'instant car plus tard nous ajouterons la possibilité pour les utilisateurs d'ajouter plus de phrases encourageantes pour que le bot les utilise.

### Comment Répondre aux Messages

Maintenant, nous devons mettre à jour notre bot pour utiliser les deux listes que nous avons créées. Tout d'abord, importez le module random car le bot choisira des messages d'encouragement de manière aléatoire. Ajoutez la ligne suivante aux instructions d'importation en haut du code : `import random`.

Maintenant, nous allons mettre à jour la fonction `on_message()` pour vérifier tous les messages afin de voir s'ils contiennent un mot de la liste `sad_words`. Si un mot triste est trouvé, le bot enverra un message d'encouragement aléatoire.

Voici le code mis à jour :

```python
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
```

C'est un bon moment pour tester le bot. Vous en savez assez maintenant pour créer votre propre bot. Mais ensuite, vous apprendrez comment implémenter des fonctionnalités plus avancées et stocker des données en utilisant la base de données de Repl.it.

### Comment Activer les Messages Soumis par les Utilisateurs

Le bot est complètement fonctionnel, mais maintenant, rendons-le possible de mettre à jour le bot directement depuis Discord. Un utilisateur devrait pouvoir ajouter plus de messages d'encouragement pour que le bot les utilise lorsqu'il détecte un mot triste.

Nous allons utiliser la base de données intégrée de Repl.it pour stocker les messages soumis par les utilisateurs. Cette base de données est un magasin clé-valeur intégré à chaque repl.

En haut du code, sous les autres instructions d'importation, ajoutez `from replit import db`. Cela nous permettra d'utiliser la base de données de Repl.it.

Les utilisateurs pourront ajouter des messages d'encouragement personnalisés pour que le bot les utilise directement depuis le chat Discord. Avant d'ajouter de nouvelles commandes pour le bot, créons deux fonctions d'assistance qui ajouteront des messages personnalisés à la base de données et les supprimeront.

Ajoutez le code suivant après la fonction `get_quote()` :

```python
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements
```

La fonction `update_encouragements()` accepte un message d'encouragement comme argument.

Tout d'abord, elle vérifie si "encouragements" est une clé dans la base de données. Si c'est le cas, elle obtient la liste des encouragements déjà dans la base de données, ajoute le nouveau à la liste et stocke la liste mise à jour dans la base de données sous la clé "encouragements".

Si la base de données ne contient pas déjà "encouragements", une nouvelle clé de ce nom est créée et le nouveau message d'encouragement est ajouté comme premier élément de la liste.

La fonction `delete_encouragement()` accepte un index comme argument.

Elle obtient la liste des encouragements de la base de données stockée sous la clé "encouragements". Si le nombre d'éléments dans la liste des encouragements est supérieur à l'index, alors l'élément de la liste à cet index est supprimé.

Enfin, la liste mise à jour est stockée dans la base de données sous la clé "encouragements".

Voici le code mis à jour pour la fonction `on_message()`. Après le code, j'expliquerai les nouvelles sections.

```python
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
 
  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("Nouveau message d'encouragement ajouté.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
```

La première nouvelle ligne de code ci-dessus est `options = starter_encouragements`. Nous faisons une copie de `starter_encouragements` car nous allons ajouter les messages soumis par les utilisateurs à cette liste avant de choisir un message aléatoire pour que le bot l'envoie.

Nous vérifions si "encouragements" est déjà dans les clés de la base de données (ce qui signifie qu'un utilisateur a soumis au moins un message personnalisé). Si c'est le cas, nous ajoutons les messages des utilisateurs aux encouragements de départ.

Ensuite, au lieu d'envoyer un message aléatoire à partir de `starter_encouragements`, le bot envoie maintenant un message aléatoire à partir de `options`.

La nouvelle section de code suivante est utilisée pour ajouter un nouveau message soumis par l'utilisateur à la base de données. Si un message Discord commence par "$new", alors le texte après "$new" sera utilisé comme un nouveau message d'encouragement.

Le code `msg.split("$new ",1)[1]` sépare le message de la commande "$new" et stocke le message dans une variable. Dans cette ligne de code, notez l'espace dans `"$new "`. Nous voulons tout ce qui se trouve _après_ l'espace.

Nous appelons la fonction d'assistance `update_encouragements` avec le nouveau message, puis le bot envoie un message au chat discord confirmant que le message a été ajouté.

La troisième nouvelle section (à la fin du code ci-dessus) vérifie si un nouveau message Discord commence par "$del". Il s'agit de la commande pour supprimer un élément de la liste "encouragements" dans la base de données.

Tout d'abord, une nouvelle variable appelée `encouragements` est initialisée comme un tableau vide. La raison en est que cette section de code enverra un message avec un tableau vide si la base de données n'inclut pas de clé "encouragement".

Si la clé "encouragement" est dans la base de données, l'index sera séparé du message Discord commençant par "$del". Ensuite, la fonction `delete_encouragement()` est appelée en passant l'index à supprimer. La liste mise à jour des encouragements est chargée dans la variable `encouragements`, puis le bot envoie un message à Discord avec la liste actuelle.

## Fonctionnalités Finales du Bot

Le bot devrait fonctionner, c'est donc un bon moment pour le tester. Nous allons maintenant ajouter quelques fonctionnalités finales.

Nous allons ajouter la possibilité d'obtenir une liste de messages soumis par les utilisateurs directement depuis Discord et nous allons ajouter la possibilité d'activer et de désactiver la réponse du bot aux mots tristes.

Je vais vous donner le code final complet du programme, puis je discuterai des mises à jour sous le code.

```python
import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["triste", "déprimé", "malheureux", "en colère", "misérable"]

starter_encouragements = [
  "Remontez le moral !",
  "Accrochez-vous.",
  "Vous êtes une personne / un bot génial !"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("Nous nous sommes connectés en tant que {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("Nouveau message d'encouragement ajouté.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Réponse activée.")
    else:
      db["responding"] = False
      await message.channel.send("Réponse désactivée.")

client.run(os.getenv("TOKEN"))
```

La première section ajoutée au code se trouve juste sous la liste `starter_encouragements` :

```python
if "responding" not in db.keys():
  db["responding"] = True
```

Nous créons une nouvelle clé dans la base de données appelée "responding" et nous la définissons sur "True". Nous l'utiliserons pour déterminer si le bot doit répondre aux mots tristes ou non. Comme la base de données est sauvegardée même après l'arrêt du programme, nous ne créons la nouvelle clé que si elle n'existe pas déjà.

La nouvelle partie suivante du code est que la section qui répond aux mots tristes est maintenant à l'intérieur de cette instruction if : `if db["responding"]:`. Le bot ne répondra aux mots tristes que si `db["responding"] = True`. La possibilité de mettre à jour cette valeur vient après cette section suivante.

Ensuite, après le code pour faire répondre le bot à la commande "$del", il y a un nouveau code pour répondre à la commande "$list" lorsqu'elle est envoyée en tant que message Discord.

Cette section commence par créer une liste vide appelée `encouragements`. Ensuite, s'il y a déjà des encouragements dans la base de données, ces encouragements remplacent la liste vide qui vient d'être créée.

Enfin, le bot envoie la liste des encouragements en tant que message Discord.

La dernière nouvelle section arrive ensuite. Ce code fait répondre le bot à la commande "$responding". Cette commande prend un argument soit "true" soit "false". Voici un exemple d'utilisation : "$responding true".

Le code extrait d'abord l'argument avec `value = msg.split("$responding ",1)[1]` (comme avant, notez l'espace dans `"$responding "`). Ensuite, il y a une instruction if/else qui définit de manière appropriée la clé "responding" dans la base de données et envoie un message de notification en retour à Discord. Si l'argument est autre chose que "true", le code suppose "false".

Le code pour le bot est complet ! Vous pouvez maintenant exécuter le bot et l'essayer. Mais il y a une étape importante supplémentaire que nous allons discuter ensuite.

## Comment Configurer le Bot pour Qu'il Fonctionne en Continu

Si vous exécutez votre bot dans repl.it puis fermez l'onglet dans lequel il s'exécute, votre bot cessera de fonctionner.

Mais il existe deux façons de garder votre bot en fonctionnement continu, même après avoir fermé votre navigateur web.

La première façon et la plus simple est de s'inscrire à un plan payant sur Repl.it. Leur plan payant le moins cher s'appelle le Hacker Plan et il inclut cinq repls toujours actifs.

Vous pouvez obtenir trois mois gratuits en utilisant ce lien (limité aux 1000 premières personnes) : https://repl.it/claim?code=tryalwayson2103

Une fois que vous avez souscrit à ce plan, ouvrez votre Repl et cliquez sur le nom en haut. Ensuite, sélectionnez l'option "Always On".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-35-1.png)

Il existe une autre façon de garder votre code en fonctionnement même sur le niveau gratuit, mais c'est un peu plus compliqué. Repl.it continuera à exécuter un serveur web même après la fermeture de l'onglet. Mais même un serveur web ne fonctionnera que jusqu'à une heure sans aucune utilisation.

Voici ce que disent les docs de repl.it :

> Une fois déployé, le serveur continuera à fonctionner en arrière-plan, même après avoir fermé l'onglet du navigateur. Le serveur restera éveillé et actif jusqu'à une heure après sa dernière requête, après quoi il entrera dans un état de veille. Les repls en veille seront réveillés dès qu'ils recevront une autre requête ; il n'est pas nécessaire de relancer le repl. Cependant, si vous apportez des modifications à votre serveur, vous devrez redémarrer le repl pour voir ces modifications reflétées dans la version live.

Pour garder le bot en fonctionnement continu, nous allons utiliser un autre service gratuit appelé Uptime Robot à l'adresse [https://uptimerobot.com/](https://uptimerobot.com/).

Uptime Robot peut être configuré pour ping le serveur web du bot sur repl.it toutes les 5 minutes. Avec des pings constants, le bot n'entrera jamais dans l'état de veille et continuera simplement à fonctionner.

Nous devons donc faire deux choses de plus pour que notre bot fonctionne en continu :

1. créer un serveur web dans repl.it et
2. configurer Uptime Robot pour ping en continu le serveur web.

### Comment Créer un Serveur Web dans repl.it

Créer un serveur web est plus simple que vous ne le pensez.

Pour ce faire, créez un nouveau fichier dans votre projet appelé `keep_alive.py`.

Puis ajoutez le code suivant :

```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bonjour. Je suis en vie !"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

```

Dans ce code, nous utilisons Flask pour démarrer un serveur web. Le serveur retourne "Bonjour. Je suis en vie !" à quiconque le visite. Le serveur s'exécutera sur un thread séparé de notre bot. Nous ne discuterons pas de tout ici puisque le reste n'est pas vraiment pertinent pour notre bot.

Maintenant, nous devons simplement faire en sorte que le bot exécute ce serveur web.

Ajoutez la ligne suivante vers le haut de `main.py` pour importer le serveur.

```python
from keep_alive import keep_alive
```

Pour démarrer le serveur web lorsque `main.py` est exécuté, ajoutez la ligne suivante comme avant-dernière ligne, juste avant que le bot ne s'exécute.

`keep_alive()`

Lorsque vous exécutez le bot sur repl.it après avoir ajouté ce code, une nouvelle fenêtre de serveur web s'ouvrira. Une URL est affichée pour le serveur web. Copiez l'URL afin de pouvoir l'utiliser dans la section suivante.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-20-1.png)

### Comment Configurer Uptime Robot

Maintenant, nous devons configurer Uptime Robot pour ping le serveur web toutes les cinq minutes. Cela fera fonctionner le bot en continu.

Créez un compte gratuit sur [https://uptimerobot.com/](https://uptimerobot.com/).

Une fois connecté à votre compte, cliquez sur "Add New Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-21-1.png)

Pour le nouveau moniteur, sélectionnez "HTTP(s)" comme type de moniteur et nommez-le comme vous le souhaitez. Ensuite, collez l'URL de votre serveur web de repl.it. Enfin, cliquez sur "Create Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-22-1.png)

C'est fait ! Maintenant, le bot fonctionnera en continu afin que les gens puissent toujours interagir avec lui sur Repl.it.

## Conclusion

Vous savez maintenant comment créer un bot Discord avec Python et le faire fonctionner en continu dans le cloud.

Il y a beaucoup d'autres choses que la bibliothèque discord.py peut faire. Donc, si vous voulez donner encore plus de fonctionnalités à un bot Discord, votre prochaine étape est de consulter [la documentation de discord.py](https://discordpy.readthedocs.io/en/latest/index.html).