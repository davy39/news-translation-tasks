---
title: Tutoriel JavaScript Discord Bot – Codez un bot Discord et hébergez-le gratuitement
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-03-08T14:45:50.000Z'
originalURL: https://freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/discordjs.png
tags:
- name: discord
  slug: discord
- name: youtube
  slug: youtube
seo_title: Tutoriel JavaScript Discord Bot – Codez un bot Discord et hébergez-le gratuitement
seo_desc: 'This tutorial will show you how to use JavaScript and Node.js to build
  your own Discord bot completely in the cloud.

  You do not need to install anything on your computer, and you do not need to pay
  anything to host your bot.

  We are going to use a num...'
---

Ce tutoriel vous montrera comment utiliser JavaScript et Node.js pour construire votre propre bot Discord entièrement dans le cloud.

Vous n'avez pas besoin d'installer quoi que ce soit sur votre ordinateur, et vous n'avez pas besoin de payer pour héberger votre bot.

Nous allons utiliser plusieurs outils, y compris l'API Discord, les bibliothèques Node.js et une plateforme de cloud computing appelée [Repl.it](https://www.repl.it).

Si vous préférez coder votre bot Discord en utilisant Python au lieu de JavaScript, [lisez ce tutoriel à la place](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/).

Il existe également une version vidéo de ce tutoriel écrit. La vidéo est intégrée ci-dessous et la version écrite se trouve après la vidéo.

%[https://youtu.be/7rU_KyudGBY]

## Comment créer un compte de bot Discord

Pour travailler avec la bibliothèque Node.js et l'API Discord, nous devons d'abord créer un compte de bot Discord.

Voici les étapes pour créer un compte de bot Discord.

1. Assurez-vous d'être connecté au [site web de Discord](https://discord.com).

2. Accédez à la [page des applications](https://discord.com/developers/applications).

3. Cliquez sur le bouton "Nouvelle Application".

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-117.png)

4. Donnez un nom à l'application et cliquez sur "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-118.png)

5. Allez dans l'onglet "Bot" puis cliquez sur "Ajouter un Bot". Vous devrez confirmer en cliquant sur "Oui, faites-le !"

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-119.png)

Conservez les paramètres par défaut pour **Public Bot** (coché) et **Require OAuth2 Code Grant** (non coché).

Votre bot a été créé. L'étape suivante consiste à copier le token.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-122.png)

Ce token est le mot de passe de votre bot, alors ne le partagez avec personne. Il pourrait permettre à quelqu'un de se connecter à votre bot et de faire toutes sortes de mauvaises choses.

Vous pouvez régénérer le token s'il est accidentellement partagé.

## Comment inviter votre bot à rejoindre un serveur

Maintenant, vous devez faire en sorte que votre Bot User rejoigne un serveur. Pour ce faire, vous devez créer une URL d'invitation pour celui-ci.

Allez dans l'onglet "OAuth2". Ensuite, sélectionnez "bot" sous la section "scopes".

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-123.png)

Maintenant, choisissez les permissions que vous souhaitez pour le bot. Notre bot va principalement utiliser des messages textuels, donc nous n'avons pas besoin de beaucoup de permissions. Vous pourriez avoir besoin de plus selon ce que vous voulez que votre bot fasse. Soyez prudent avec la permission "Administrateur".

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-124.png)

Après avoir sélectionné les permissions appropriées, cliquez sur le bouton 'copier' au-dessus des permissions. Cela copiera une URL qui peut être utilisée pour ajouter le bot à un serveur.

Collez l'URL dans votre navigateur, choisissez un serveur pour inviter le bot, et cliquez sur "Autoriser".

Pour ajouter le bot, votre compte a besoin des permissions "Gérer le serveur".

Maintenant que vous avez créé l'utilisateur bot, nous allons commencer à écrire le code Python pour le bot.

## Comment coder un bot Discord de base avec la bibliothèque discord.js

Nous allons utiliser la bibliothèque Node discord.js pour écrire le code du bot. discord.js est un wrapper d'API pour Discord qui facilite la création d'un bot Discord en Node.js / JavaScript.

### Comment créer un Repl et installer discord.js

Vous pouvez développer le bot sur votre ordinateur local avec n'importe quel éditeur de code. Cependant, dans ce tutoriel, nous allons utiliser Repl.it car cela simplifiera le suivi pour tout le monde. Repl.it est un IDE en ligne que vous pouvez utiliser dans votre navigateur web.

Commencez par aller sur [Repl.it](https://repl.it). Créez un nouveau Repl et choisissez "Node.js" comme langage. Cela signifie que le langage de programmation sera JavaScript.

Pour utiliser la bibliothèque discord.js, ajoutez simplement `const Discord = require("discord.js");` en haut de `main.js`. Repl.it installera automatiquement cette dépendance lorsque vous appuierez sur le bouton "run".

### Comment configurer les événements Discord pour votre bot

discord.js tourne autour du concept d'événements. Un événement est quelque chose que vous écoutez et auquel vous répondez. Par exemple, lorsqu'un message est envoyé, vous recevrez un événement à ce sujet auquel vous pourrez répondre.

Créons un bot qui répond à un message spécifique. Ce code de bot simple est tiré directement de [la documentation discord.js](https://discord.js.org/#/docs/main/stable/general/welcome). Nous ajouterons plus de fonctionnalités au bot plus tard.

Ajoutez ce code à main.js. Je vais expliquer ce que fait tout ce code sous peu.

```javascript
const Discord = require("discord.js")
const client = new Discord.Client()

client.on("ready", () => {
  console.log(`Connecté en tant que ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "ping") {
    msg.reply("pong");
  }
})

client.login(process.env.TOKEN)
```

Lorsque vous avez créé votre utilisateur bot sur Discord, vous avez copié un token. Maintenant, nous allons créer un fichier `.env` pour stocker le token.

Les fichiers `.env` sont utilisés pour déclarer des variables d'environnement. Sur Repl.it, la plupart des fichiers que vous créez sont visibles par tout le monde, mais les fichiers `.env` ne sont visibles que par vous. Les autres personnes consultant un repl public ne pourront pas voir le contenu du fichier `.env`.

Donc, si vous développez sur Repl.it, n'incluez des informations privées comme des tokens ou des clés que dans un fichier `.env`.

Cliquez sur le bouton "Ajouter un fichier" et créez un fichier nommé `.env`.

À l'intérieur du fichier, ajoutez la ligne suivante, y compris votre token réel que vous avez copié précédemment :

```
TOKEN=[coller le token ici]
```

Maintenant, passons en revue ce que fait chaque ligne de code dans votre code de bot Discord.

La première ligne importe la bibliothèque discord.js. Ensuite, nous créons une instance d'un [`Client`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client). C'est la connexion à Discord.

Le `client.on()` est utilisé pour vérifier les événements. Il accepte un nom d'événement, puis une fonction de rappel à appeler lorsque l'événement a lieu. Dans ce code, l'événement `ready` est appelé lorsque le bot est prêt à être utilisé. Ensuite, lorsqu'un nouveau message est envoyé sur le serveur Discord, l'événement `message` est appelé.

Le code vérifie si le [`msg.content`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.content) est égal à `'ping'`. Si c'est le cas, alors le bot répond avec `'pong'` sur le canal.

Maintenant que le bot est configuré, la dernière ligne exécute le bot avec le token de connexion. Il obtient le token de notre fichier `.env`.

Nous avons le code pour le bot, alors maintenant nous devons simplement l'exécuter.

### Comment exécuter le bot

Maintenant, cliquez sur le bouton d'exécution en haut pour exécuter votre bot dans repl.it.

Maintenant, allez dans votre salon Discord et tapez "ping". Votre bot devrait retourner "pong".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image.png)

## Comment améliorer le bot

Maintenant que nous avons un bot de base qui fonctionne, nous allons l'améliorer. Il s'appelle "Encourage Bot" pour une raison.

Ce bot répondra avec un message d'encouragement chaque fois que quelqu'un envoie un message contenant un mot triste ou déprimant.

N'importe qui pourra ajouter des messages d'encouragement pour que le bot les utilise et les messages soumis par les utilisateurs seront stockés dans la base de données de Repl.it.

Le bot retournera également une citation inspirante aléatoire d'une API lorsque quelqu'un tapera le message "$inspire" dans le chat.

Nous commencerons par ajouter la fonctionnalité "$inspire".

### Comment ajouter des citations inspirantes au bot

Nous obtiendrons des citations inspirantes d'une API appelée zenquotes.io. Nous devons importer le module node-fetch, ajouter une fonction `getQuote()` et mettre à jour notre code de bot pour appeler la fonction.

Voici le code mis à jour. Après le code, j'expliquerai les nouvelles parties.

```javascript
const Discord = require("discord.js")
const fetch = require("node-fetch")
const client = new Discord.Client()

function getQuote() {
  return fetch("https://zenquotes.io/api/random")
    .then(res => {
      return res.json()
      })
    .then(data => {
      return data[0]["q"] + " -" + data[0]["a"]
    })
}

client.on("ready", () => {
  console.log(`Connecté en tant que ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.author.bot) return
    
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }
})

client.login(process.env.TOKEN)
```

Nous devons maintenant importer le module `node-fetch`. Ce module permet à notre code de faire une requête HTTP pour obtenir des données de l'API.

La fonction `getQuote()` est assez simple. Tout d'abord, elle utilise le module node-fetch pour demander des données à l'URL de l'API. L'API retourne une citation inspirante aléatoire. Cette fonction pourrait facilement être réécrite pour obtenir des citations d'une autre API, si celle-ci cesse de fonctionner.

Ensuite, la fonction convertit la réponse de l'API en JSON et crée une chaîne à retourner. Par essais et erreurs, j'ai découvert comment obtenir la citation du JSON dans le format de chaîne que je voulais. La citation est retournée par la fonction sous forme de chaîne.

La dernière partie mise à jour dans le code se trouve vers la fin. Auparavant, elle recherchait le message "ping". Maintenant, elle recherche "$inspire". Au lieu de retourner "pong", elle obtient la citation avec `getQuote()` et retourne la citation. Nous utilisons `msg.channel.send()` pour envoyer le message au canal. De plus, le code vérifie si le message provient du bot lui-même et, si c'est le cas, il quitte la fonction pour ne rien faire.

À ce stade, vous pouvez exécuter votre code et l'essayer.

## Comment ajouter des messages d'encouragement au bot

Maintenant, nous allons implémenter la fonctionnalité où le bot répond avec des messages d'encouragement lorsqu'un utilisateur publie un message avec un mot triste.

### Comment ajouter des mots tristes au bot

Tout d'abord, nous devons créer un tableau qui contient les mots tristes auxquels le bot répondra.

Ajoutez la ligne suivante après la création de la variable `client` :

`sadWords = ["sad", "depressed", "unhappy", "angry", "miserable"]`

N'hésitez pas à ajouter plus de mots à la liste.

### Comment ajouter des messages d'encouragement au bot

Maintenant, nous allons ajouter un tableau de messages d'encouragement auxquels le bot répondra.

Ajoutez le tableau suivant après la liste `sadWords` que vous avez créée :

```python
encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]
```

Comme avant, n'hésitez pas à ajouter plus de phrases de votre choix au tableau. Je n'utilise que trois éléments pour l'instant car plus tard nous ajouterons la possibilité pour les utilisateurs d'ajouter plus de phrases encourageantes pour que le bot les utilise.

### Comment répondre aux messages

Maintenant, nous devons mettre à jour notre bot pour utiliser les deux listes que nous avons créées.

Nous allons maintenant mettre à jour la fonction `message` pour vérifier tous les messages afin de voir s'ils contiennent un mot de la liste `sadWords`. Si un mot triste est trouvé, le bot enverra un message d'encouragement aléatoire.

Voici le code mis à jour :

```javascript
client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  if (sadWords.some(word => msg.content.includes(word))) {
    const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
    msg.reply(encouragement)
  }

})
```

C'est un bon moment pour tester le bot. Vous en savez assez maintenant pour créer votre propre bot. Mais ensuite, vous apprendrez comment implémenter des fonctionnalités plus avancées et stocker des données en utilisant la base de données de Repl.it.

### Comment activer les messages soumis par les utilisateurs

Le bot est complètement fonctionnel, mais maintenant, rendons-le possible de mettre à jour le bot directement depuis Discord. Un utilisateur devrait pouvoir ajouter plus de messages encourageants pour que le bot les utilise lorsqu'il détecte un mot triste.

Nous allons utiliser la base de données intégrée de Repl.it pour stocker les messages soumis par les utilisateurs. Cette base de données est un magasin clé-valeur intégré à chaque repl.

En haut du code, sous les autres instructions d'importation, ajoutez :

```javascript
const Database = require("@replit/database")
const db = new Database()
```

Cela nous permettra d'utiliser la base de données de Repl.it. Lorsque vous exécutez le code, Repl.it devrait installer le module de base de données automatiquement. Si pour une raison quelconque cela ne se produit pas, vous devrez peut-être aller dans l'onglet Shell (pas la Console) et taper "npm install @replit/database".

Après l'endroit où le tableau `encouragements` est créé, insérez le code suivant pour ajouter les encouragements à la base de données si nécessaire :

```javascript
db.get("encouragements").then(encouragements => {
  if (!encouragements || encouragements.length < 1) {
    db.set("encouragements", starterEncouragements)
  }  
})
```

Renommez également le tableau `encouragements` vers le haut en `starterEncouragements`.

Les utilisateurs pourront ajouter des messages encourageants personnalisés pour que le bot les utilise directement depuis le chat Discord. Avant d'ajouter de nouvelles commandes pour le bot, créons deux fonctions d'assistance qui ajouteront des messages personnalisés à la base de données et les supprimeront.

Ajoutez le code suivant après la fonction `getQuote()` :

```javascript
function updateEncouragements(encouragingMessage) {
  db.get("encouragements").then(encouragements => {
    encouragements.push([encouragingMessage])
    db.set("encouragements", encouragements)
  })
}

function deleteEncouragment(index) {
  db.get("encouragements").then(encouragements => {
    if (encouragements.length > index) {
      encouragements.splice(index, 1)
      db.set("encouragements", encouragements)
    }
  })
}
```

La fonction `updateEncouragements()` accepte un message encourageant comme argument.

Tout d'abord, elle obtient les "encouragements" de la base de données. Ensuite, elle ajoute le nouvel encouragement au tableau et stocke le tableau mis à jour dans la base de données sous la clé "encouragements".

La fonction `deleteEncouragement()` accepte un index comme argument.

Elle obtient la liste des encouragements de la base de données stockée sous la clé "encouragements". Si la longueur est supérieure à l'index, alors l'élément de la liste à cet index est supprimé. Enfin, la liste mise à jour est stockée dans la base de données sous la clé "encouragements".

Voici le code mis à jour pour la fonction `message`. Après le code, j'expliquerai les nouvelles sections.

```javascript
client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  
  if (sadWords.some(word => msg.content.includes(word))) {
    db.get("encouragements").then(encouragements => {
      const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
      msg.reply(encouragement)
    })
  }

  if (msg.content.startsWith("$new")) {
    encouragingMessage = msg.content.split("$new ")[1]
    updateEncouragements(encouragingMessage)
    msg.channel.send("New encouraging message added.")
  }

  if (msg.content.startsWith("$del")) {
    index = parseInt(msg.content.split("$del ")[1])
    deleteEncouragment(index)
    msg.channel.send("Encouraging message deleted.")
  }
})
```

La section des mots tristes a été mise à jour pour utiliser les messages encourageants de la base de données afin que les messages soumis par les utilisateurs puissent être utilisés.

La nouvelle section de code suivante est utilisée pour ajouter un nouveau message soumis par l'utilisateur à la base de données. Si un message Discord commence par "$new", alors le texte après "$new" sera utilisé comme un nouveau message encourageant.

Le code `msg.content.split('$new ')[1]` sépare le message de la commande "$new" et stocke le message dans une variable. Dans cette ligne de code, notez l'espace dans `'$new '`. Nous voulons tout ce qui se trouve _après_ l'espace.

Nous appelons la fonction d'assistance `updateEncouragements` avec le nouveau message, puis le bot envoie un message au chat discord confirmant que le message a été ajouté.

La troisième nouvelle section (à la fin du code ci-dessus) vérifie si un nouveau message Discord commence par "$del". C'est la commande pour supprimer un élément de la liste "encouragements" dans la base de données.

L'index est séparé du message Discord commençant par "$del". Ensuite, la fonction `deleteEncouragement()` est appelée en passant l'index à supprimer. La liste mise à jour des encouragements est chargée dans la variable `encouragements`, puis le bot envoie un message à Discord avec la liste actuelle.

## Fonctionnalités finales du bot

Le bot devrait fonctionner, donc c'est un bon moment pour le tester. Nous allons maintenant ajouter quelques fonctionnalités finales.

Nous allons ajouter la possibilité d'obtenir une liste de messages soumis par les utilisateurs directement depuis Discord et nous allons ajouter la possibilité d'activer et de désactiver la réponse du bot aux mots tristes.

Je vais vous donner le code final complet du programme, puis je discuterai des mises à jour ci-dessous le code.

```javascript
const Discord = require("discord.js")
const fetch = require("node-fetch")
const Database = require("@replit/database")

const db = new Database()
const client = new Discord.Client()

const sadWords = ["sad", "depressed", "unhappy", "angry", "miserable"]

const starterEncouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

db.get("encouragements").then(encouragements => {
  console.log(encouragements)
  if (!encouragements || encouragements.length < 1) {
    db.set("encouragements", starterEncouragements)
  }  
})

db.get("responding").then(value => {
  if (value == null) {
    db.set("responding", true)
  }  
})

function getQuote() {
  return fetch("https://zenquotes.io/api/random")
    .then(res => {
      return res.json()
      })
    .then(data => {
      return data[0]["q"] + " -" + data[0]["a"]
    })
}

function updateEncouragements(encouragingMessage) {
  db.get("encouragements").then(encouragements => {
    encouragements.push([encouragingMessage])
    db.set("encouragements", encouragements)
  })
}

function deleteEncouragment(index) {
  db.get("encouragements").then(encouragements => {
    if (encouragements.length > index) {
      encouragements.splice(index, 1)
      db.set("encouragements", encouragements)
    }
  })
}

client.on("ready", () => {
  console.log(`Connecté en tant que ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  db.get("responding").then(responding => {
    if (responding && sadWords.some(word => msg.content.includes(word))) {
      db.get("encouragements").then(encouragements => {
        const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
        msg.reply(encouragement)
      })
    }
  })

  if (msg.content.startsWith("$new")) {
    encouragingMessage = msg.content.split("$new ")[1]
    updateEncouragements(encouragingMessage)
    msg.channel.send("New encouraging message added.")
  }

  if (msg.content.startsWith("$del")) {
    index = parseInt(msg.content.split("$del ")[1])
    deleteEncouragment(index)
    msg.channel.send("Encouraging message deleted.")
  }

  if (msg.content.startsWith("$list")) {
    db.get("encouragements").then(encouragements => {
      msg.channel.send(encouragements)
    })
  }
    
  if (msg.content.startsWith("$responding")) {
    value = msg.content.split("$responding ")[1]

    if (value.toLowerCase() == "true") {
      db.set("responding", true)
      msg.channel.send("Responding is on.")
    } else {
      db.set("responding", false)
      msg.channel.send("Responding is off.")
    }
  }
})

client.login(process.env.TOKEN)
```

La première section ajoutée au code se trouve juste sous la liste `starterEncouragements` :

```javascript
db.get("responding").then(value => {
  if (value == null) {
    db.set("responding", true)
  }  
})
```

Nous créons une nouvelle clé dans la base de données appelée "responding" et nous la définissons sur "true". Nous l'utiliserons pour déterminer si le bot doit répondre aux mots tristes ou non. Puisque la base de données est sauvegardée même après l'arrêt du programme, nous ne créons la nouvelle clé que si elle n'existe pas déjà.

La nouvelle partie suivante du code se trouve dans la section qui répond aux mots tristes et est maintenant à l'intérieur de cette instruction if. Le bot ne répondra aux mots tristes que si `db.get("responding") = true`. La possibilité de mettre à jour cette valeur vient après cette section suivante.

Ensuite, après le code pour faire répondre le bot à la commande "$del", il y a un nouveau code pour répondre à la commande "$list" lorsqu'elle est envoyée en tant que message Discord.

Le bot envoie la liste des encouragements en tant que message Discord.

La nouvelle section finale arrive ensuite. Ce code fait répondre le bot à la commande "$responding". Cette commande prend un argument soit "true" soit "false". Voici un exemple d'utilisation : "$responding true".

Le code extrait d'abord l'argument avec `value = msg.content.split("$responding ")[1]` (comme avant, notez l'espace dans `"$responding "`). Ensuite, il y a une instruction if/else qui définit de manière appropriée la clé "responding" dans la base de données et envoie un message de notification en retour à Discord. Si l'argument est autre chose que "true", le code suppose "false".

Le code pour le bot est complet ! Vous pouvez maintenant exécuter le bot et l'essayer. Mais il y a une étape importante supplémentaire que nous allons discuter ensuite.

## Comment configurer le bot pour qu'il s'exécute en continu

Si vous exécutez votre bot dans repl.it puis fermez l'onglet dans lequel il s'exécute, votre bot s'arrêtera.

Mais il existe deux façons de garder votre bot en cours d'exécution en continu, même après avoir fermé votre navigateur web.

La première façon et la plus simple est de s'inscrire à un plan payant sur Repl.it. Leur plan payant le moins cher s'appelle le Hacker Plan et il inclut cinq Repls toujours actifs.

Vous pouvez obtenir trois mois gratuits en utilisant ce lien (limité aux 1000 premières personnes) : https://repl.it/claim?code=tryalwayson2103

Une fois que vous avez souscrit à ce plan, ouvrez votre Repl et cliquez sur le nom en haut. Ensuite, sélectionnez l'option "Always On".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-36.png)

Il existe une autre façon de garder votre code en cours d'exécution même sur le niveau gratuit, mais c'est un peu plus compliqué. Repl.it continuera à exécuter un serveur web même après la fermeture de l'onglet. Mais même un serveur web ne s'exécutera que pendant une heure maximum sans aucune utilisation.

Voici ce que disent les docs de repl.it :

> Une fois déployé, le serveur continuera à s'exécuter en arrière-plan, même après avoir fermé l'onglet du navigateur. Le serveur restera éveillé et actif jusqu'à une heure après sa dernière requête, après quoi il entrera dans un stade de sommeil. Les repls en sommeil seront réveillés dès qu'ils recevront une autre requête ; il n'est pas nécessaire de relancer le repl. Cependant, si vous apportez des modifications à votre serveur, vous devrez redémarrer le repl afin de voir ces modifications reflétées dans la version live.

Pour garder le bot en cours d'exécution en continu, nous allons utiliser un autre service gratuit appelé Uptime Robot à l'adresse [https://uptimerobot.com/](https://uptimerobot.com/).

Uptime Robot peut être configuré pour ping le serveur web du bot sur repl.it toutes les 5 minutes. Avec des pings constants, le bot n'entrera jamais dans le stade de sommeil et continuera simplement à s'exécuter.

Nous devons donc faire deux choses de plus pour que notre bot s'exécute en continu :

1. créer un serveur web dans repl.it et
2. configurer Uptime Robot pour ping en continu le serveur web.

### Comment créer un serveur web dans repl.it

Créer un serveur web est plus simple que vous ne le pensez.

Pour ce faire, créez un nouveau fichier dans votre projet appelé `server.js`.

Ensuite, ajoutez le code suivant :

```javascript
const express = require("express")

const server = express()

server.all("/", (req, res) => {
  res.send("Bot is running!")
})

function keepAlive() {
  server.listen(3000, () => {
    console.log("Server is ready.")
  })
}

module.exports = keepAlive
```

Dans ce code, nous utilisons express pour démarrer un serveur web. Le serveur retourne "Bot is running!" à quiconque le visite. Le serveur s'exécutera sur un thread séparé de notre bot. Nous ne discuterons pas de tout ici puisque le reste n'est pas vraiment pertinent pour notre bot.

Maintenant, nous devons simplement faire en sorte que le bot exécute ce serveur web.

Ajoutez la ligne suivante vers le haut de `index.js` pour importer le serveur.

```python
const keepAlive = require("./server")
```

Pour démarrer le serveur web lorsque `index.js` est exécuté, ajoutez la ligne suivante comme avant-dernière ligne, juste avant que le bot ne s'exécute.

`keepAlive()`

Lorsque vous exécutez le bot sur repl.it après avoir ajouté ce code, une nouvelle fenêtre de serveur web s'ouvrira. Une URL est affichée pour le serveur web. Copiez l'URL afin de pouvoir l'utiliser dans la section suivante.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-1.png)

### Comment configurer Uptime Robot

Maintenant, nous devons configurer Uptime Robot pour ping le serveur web toutes les cinq minutes. Cela fera en sorte que le bot s'exécute en continu.

Créez un compte gratuit sur [https://uptimerobot.com/](https://uptimerobot.com/).

Une fois connecté à votre compte, cliquez sur "Add New Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-21.png)

Pour le nouveau moniteur, sélectionnez "HTTP(s)" comme type de moniteur et nommez-le comme vous le souhaitez. Ensuite, collez l'URL de votre serveur web de repl.it. Enfin, cliquez sur "Create Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-22.png)

C'est fait ! Maintenant, le bot s'exécutera en continu afin que les gens puissent toujours interagir avec lui sur Repl.it.

## Conclusion

Vous savez maintenant comment créer un bot Discord avec JavaScript et le faire fonctionner en continu dans le cloud.

Il y a beaucoup d'autres choses que la bibliothèque discord.js peut faire. Donc, si vous voulez donner à un bot Discord encore plus de fonctionnalités, votre prochaine étape est de consulter [la documentation de discord.js](https://discord.js.org/#/docs/main/stable/general/welcome).