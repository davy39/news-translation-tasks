---
title: Comment créer un bot musical avec Discord.js – Tutoriel pas à pas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-28T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-music-bot-using-discord-js-4436f5f3f0f8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*rFQhPUqebJY9N4Ue
tags:
- name: bots
  slug: bots
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un bot musical avec Discord.js – Tutoriel pas à pas
seo_desc: "By Gabriel Tanner\nThe Discord API provides you with an easy tool to create\
  \ and use your own bots and tools. \nIn this tutorial, you'll learn how you can\
  \ create a basic music bot and add it to your server. The bot will be able to play,\
  \ skip, and stop t..."
---

Par Gabriel Tanner

L'API Discord vous fournit un outil facile pour créer et utiliser vos propres bots et outils. 

Dans ce tutoriel, vous apprendrez à créer un bot musical de base et à l'ajouter à votre serveur. Le bot pourra lire, sauter et arrêter la musique, et prendra également en charge la fonctionnalité de mise en file d'attente.

## Table des matières

1. [Prérequis](#heading-prerequis)
2. [Comment configurer un bot Discord](#heading-comment-configurer-un-bot-discord)  
– [Comment ajouter le bot à votre serveur](#heading-comment-ajouter-le-bot-a-votre-serveur)  
– [Comment créer votre projet](#heading-comment-creer-votre-projet)  
– [Bases de Discord.js](#heading-bases-de-discordjs)
3. [Version 0.13 du bot Discord](#heading-version-013-du-bot-discord)  
– [Comment créer le lecteur Discord](#heading-comment-creer-le-lecteur-discord)  
– [Comment ajouter des commandes slash](#heading-comment-ajouter-des-commandes-slash)  
– [Comment implémenter les interactions](#id="comment-implementer-les-interactions")  
– [Comment lire des chansons](#heading-comment-lire-des-chansons)  
– [Comment sauter des chansons](#heading-comment-sauter-des-chansons)  
– [Comment arrêter des chansons](#heading-comment-arreter-des-chansons)  
– [Code source complet pour index.js](#heading-code-source-complet-pour-indexjs)
4. [Version 0.12 du bot Discord](#heading-version-012-du-bot-discord)  
– [Comment lire les messages](#heading-comment-lire-les-messages)  
– [Comment ajouter des chansons](#heading-comment-ajouter-des-chansons)  
– [Comment lire des chansons](#heading-comment-lire-des-chansons)  
– [Comment sauter des chansons](#heading-comment-sauter-des-chansons)  
– [Comment arrêter des chansons](#heading-comment-arreter-des-chansons)  
– [Code source complet pour index.js](#heading-code-source-complet-pour-indexjs)
5. [Conclusion](#heading-conclusion)

## **Prérequis**

Avant de commencer à créer le bot, assurez-vous d'avoir installé tous les outils nécessaires :

* [Node](https://nodejs.org/en/)
* [NPM](https://www.npmjs.com/)
* [FFMPEG](https://www.ffmpeg.org/)

Après avoir installé ces outils, vous pouvez continuer en configurant votre bot Discord.

## **Comment configurer un bot Discord**

Tout d'abord, vous devez créer une nouvelle application sur le portail de développement de Discord.

Vous pouvez le faire en visitant le [portail](https://discordapp.com/developers/applications/) et en cliquant sur Nouvelle Application.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Creating-application.webp.jpg)
_Créer une nouvelle application Discord_

Après cela, vous devez donner un nom à votre application et cliquer sur le bouton Créer.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/create-bot.webp.jpg)
_Donnez à votre bot le nom que vous souhaitez - J'ai choisi "music-bot"_

Après cela, sélectionnez l'onglet bot et cliquez sur Ajouter un Bot.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-148.png)
_Ajoutez votre bot sous l'onglet "Bot"_

Maintenant, votre bot est créé et vous pouvez continuer en l'invitant sur votre serveur.

### Comment ajouter le bot à votre serveur

Après avoir créé votre bot, vous pouvez l'inviter en utilisant le générateur d'URL OAuth2.

Pour cela, vous devez naviguer vers la page OAuth2 et sélectionner bot dans l'onglet scope.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/oauth-url-generator.png.jpg)
_Sélection de "bot" sur la page du générateur OAuth2_

Après cela, vous devez sélectionner les permissions nécessaires pour lire de la musique et lire les messages.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/bot-permissions.png.jpg)
_Sélectionnez les permissions dont vous aurez besoin - "lire les messages/voir les canaux", "envoyer des messages", "gérer les messages", "ajouter des réactions", "utiliser les commandes slash", "se connecter", et "parler"._

Ensuite, vous pouvez copier votre URL générée et la coller dans votre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/bot-invite-url.png.jpg)
_Copiez l'URL_

Après l'avoir collée, ajoutez-la à votre serveur en sélectionnant le serveur et en cliquant sur le bouton autoriser.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/english-image.png)

### Comment créer votre projet

Maintenant, vous pouvez commencer à créer votre projet en utilisant le terminal.

Tout d'abord, créez un répertoire et déplacez-vous dedans. Vous pouvez le faire en utilisant ces deux commandes :

```bash
mkdir musicbot && cd musicbot
```

Après cela, créez vos modules de projet en utilisant la commande `npm init`. Après avoir entré la commande, il vous sera posé quelques questions – répondez-y et continuez.

Ensuite, vous devez simplement créer les deux fichiers dans lesquels vous travaillerez.

```
touch index.js && touch config.json
```

Maintenant, ouvrez votre projet dans votre éditeur de texte. J'utilise personnellement VS Code et je peux l'ouvrir avec la commande suivante :

```bash
code .
```

### Bases de Discord.js

Maintenant, vous devez installer quelques dépendances avant de pouvoir commencer.

```
npm install discord.js@^12.5.3 ffmpeg fluent-ffmpeg @discordjs/opus ytdl-core --save
```

Après l'installation, vous pouvez continuer en écrivant votre fichier config.json. Ici, sauvegardez le token de votre bot et le préfixe qu'il doit écouter.

```json
{
"prefix": "!",
"token": "votre-token"
}
```

Pour obtenir votre token, vous devez visiter à nouveau le portail des développeurs Discord et le copier depuis la section bot.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/get-token.jpg)
_Obtenez votre token de bot en cliquant sur "Copier" et sauvegardez-le quelque part en sécurité_

Ce sont les seules choses que vous devez faire dans votre fichier `config.json`. Il est donc temps de commencer à écrire votre code JavaScript. 

L'article inclut deux versions : une pour la nouvelle version discord.js v13, qui utilise des commandes slash combinées avec la bibliothèque discord-player pour implémenter la fonctionnalité musicale, et une pour discord.js v12.5.3, qui implémente la fonctionnalité sans bibliothèque. 

L'ancienne version est meilleure pour l'apprentissage, et la nouvelle version fonctionne avec le discord.js actuel et est beaucoup plus facile à implémenter – choisissez celle que vous préférez.

## **Version 0.13 du bot Discord**

Maintenant, vous devez simplement installer quelques dépendances supplémentaires avant de pouvoir commencer.

```
npm install discord.js discord-player @discordjs/opus
```

Après avoir installé les dépendances, importez-les dans vos dépendances.

```javascript
const { Client, GuildMember, Intents } = require("discord.js");
const { Player, QueryType } = require("discord-player");
const config = require("./config.json");
```

Après cela, créez votre client et connectez-vous en utilisant votre token.

```javascript
const client = new Client({
    intents: [Intents.FLAGS.GUILD_VOICE_STATES, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILDS]
});
client.login(config.token);
```

Maintenant, ajoutez quelques écouteurs de base qui console.log lorsqu'ils sont exécutés.

```
client.once('ready', () => {
 console.log('Prêt !');
});

client.on("error", console.error);
client.on("warn", console.warn);
```

Après cela, vous pouvez démarrer votre bot en utilisant la commande `node` et le bot devrait être en ligne sur Discord et imprimer « Prêt ! » dans la console.

```bash
node index.js
```

### Comment créer le lecteur Discord

Maintenant que vous avez créé le client pour le bot Discord, vous pouvez continuer en initialisant votre lecteur. Cela vous permettra de lire et de gérer de la musique dans votre canal Discord.

```javascript
const player = new Player(client);
```

Vous pouvez également ajouter quelques gestionnaires d'erreurs qui seront appelés si une erreur se produit.

```javascript
player.on("error", (queue, error) => {
    console.log(`[${queue.guild.name}] Erreur émise depuis la file d'attente : ${error.message}`);
});
player.on("connectionError", (queue, error) => {
    console.log(`[${queue.guild.name}] Erreur émise depuis la connexion : ${error.message}`);
});
```

La dernière chose que vous devez faire est d'ajouter des écouteurs pour les différents événements du lecteur comme le début ou l'ajout d'une chanson.

```javascript
player.on("trackStart", (queue, track) => {
    queue.metadata.send(`\ud83c\udfb6 | Lecture démarrée : **${track.title}** dans **${queue.connection.channel.name}** !`);
});

player.on("trackAdd", (queue, track) => {
    queue.metadata.send(`\ud83c\udfb6 | Piste **${track.title}** mise en file d'attente !`);
});

player.on("botDisconnect", (queue) => {
    queue.metadata.send("\u274c | J'ai été déconnecté manuellement du canal vocal, vidange de la file d'attente !");
});

player.on("channelEmpty", (queue) => {
    queue.metadata.send("\u274c | Personne n'est dans le canal vocal, je quitte...");
});

player.on("queueEnd", (queue) => {
    queue.metadata.send("\u2705 | File d'attente terminée !");
});
```

Dans la plupart des cas, vous envoyez simplement un message dans le canal texte Discord en utilisant la fonction `send()`.

### Comment ajouter des commandes slash

Après avoir configuré le lecteur avec succès, vous pouvez continuer en ajoutant vos commandes slash à votre client. Cette étape permet à Discord de savoir quelles commandes le bot peut exécuter.

```javascript
client.on("messageCreate", async (message) => {
		if (message.author.bot || !message.guild) return;
    if (!client.application?.owner) await client.application?.fetch();
});
```

Vous pouvez le faire en implémentant une simple commande `!deploy` qui sauvegarde vos commandes dans la variable `guild.commands` d'un message. 

Une commande slash a un nom, une description et un champ options facultatif qui contient les paramètres de la commande. Par exemple, la commande play prend une requête de chanson comme argument.

```javascript
client.on("messageCreate", async (message) => {
		...

		if (message.content === "!deploy" && message.author.id === client.application?.owner?.id) {
        await message.guild.commands.set([
            {
                name: "play",
                description: "Joue une chanson depuis YouTube",
                options: [
                    {
                        name: "query",
                        type: "STRING",
                        description: "La chanson que vous voulez jouer",
                        required: true
                    }
                ]
            },
            {
                name: "skip",
                description: "Passer à la chanson actuelle"
            },
            {
                name: "queue",
                description: "Voir la file d'attente"
            },
            {
                name: "stop",
                description: "Arrêter le lecteur"
            },
        ]);

        await message.reply("Déployé !");
    }
});
```

Après avoir entré `!deploy` dans votre chat texte Discord, les commandes slash seront ajoutées à votre application. En tapant `/` dans le chat, vous devriez voir quelque chose de similaire à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/bot-slash-commands.jpg)
_Exemple d'utilisation des commandes slash_

### Comment implémenter les interactions

Une fois les interactions (commandes slash) définies, vous devrez maintenant les implémenter. 

Toutes les commandes slash déclenchent l'événement `interactionCreate` et peuvent être implémentées à l'intérieur de la fonction asynchrone ci-dessous. Avant d'exécuter une fonctionnalité, exécutez quelques conditionnelles pour vérifier si l'utilisateur est autorisé à effectuer la fonctionnalité donnée.

```javascript
client.on("interactionCreate", async (interaction) => {
    if (!interaction.isCommand() || !interaction.guildId) return;

    if (!(interaction.member instanceof GuildMember) || !interaction.member.voice.channel) {
        return void interaction.reply({ content: "Vous n'êtes pas dans un canal vocal !", ephemeral: true });
    }

    if (interaction.guild.me.voice.channelId && interaction.member.voice.channelId !== interaction.guild.me.voice.channelId) {
        return void interaction.reply({ content: "Vous n'êtes pas dans mon canal vocal !", ephemeral: true });
    }
});
```

Après cela, vérifiez quelle commande est en cours d'exécution en faisant correspondre le `commandName` avec le nom des commandes que vous avez définies ci-dessus.

```javascript
client.on("interactionCreate", async (interaction) => {
    ...

		if (interaction.commandName === "play") {
			// TODO: Implémenter la commande play
		}
});
```

Vous pouvez ensuite ajouter l'implémentation à l'intérieur de l'instruction `if`.

### Comment lire des chansons

La commande play nécessite de rechercher la chanson fournie et d'ajouter le résultat à la file d'attente actuelle des chansons. 

Commençons par récupérer la requête fournie par l'utilisateur en utilisant la fonction `options.get()`. Après cela, vous pouvez utiliser la fonction `player.search()` pour rechercher la chanson souhaitée.

```javascript
if (interaction.commandName === "play") {
    await interaction.deferReply();

    const query = interaction.options.get("query").value;
    const searchResult = await player
        .search(query, {
            requestedBy: interaction.user,
            searchEngine: QueryType.AUTO
        })
        .catch(() => {});
    if (!searchResult || !searchResult.tracks.length) return void interaction.followUp({ content: "Aucun résultat trouvé !" });
}
```

Maintenant que vous avez la chanson, vous pouvez créer une file d'attente pour les chansons (si une file d'attente existe déjà, la fonction `createQueue` retournera celle existante). 

Une fois la file d'attente créée, vous pouvez essayer de rejoindre le canal vocal de l'utilisateur. Si cela réussit, ajoutez la chanson à la file d'attente actuelle en utilisant la fonction `addTracks`.

```javascript
if (interaction.commandName === "play") {
    ...

		const queue = await player.createQueue(interaction.guild, {
        metadata: interaction.channel
    });

    try {
        if (!queue.connection) await queue.connect(interaction.member.voice.channel);
    } catch {
        void player.deleteQueue(interaction.guildId);
        return void interaction.followUp({ content: "Impossible de rejoindre votre canal vocal !" });
    }

    await interaction.followUp({ content: `\u23f1 | Chargement de votre ${searchResult.playlist ? "playlist" : "piste"}...` });
    searchResult.playlist ? queue.addTracks(searchResult.tracks) : queue.addTrack(searchResult.tracks[0]);
    if (!queue.playing) await queue.play();
}
```

Enfin, si la file d'attente n'est pas déjà en lecture, commençons-la en utilisant la fonction `play()`.

### Comment sauter des chansons

Sauter est assez facile – vous pouvez le faire en appelant la fonction `skip()` sur la file d'attente.

```javascript
if (interaction.commandName === "skip") {
    await interaction.deferReply();
    const queue = player.getQueue(interaction.guildId);
    if (!queue || !queue.playing) return void interaction.followUp({ content: "\u274c | Aucune musique n'est en cours de lecture !" });
    const currentTrack = queue.current;
    const success = queue.skip();
    return void interaction.followUp({
        content: success ? `\u2705 | Piste **${currentTrack}** sautée !` : "\u274c | Quelque chose s'est mal passé !"
    });
}
```

Si l'action réussit, vous pouvez écrire un message dans le canal texte Discord en utilisant `interaction.followUp()`.

### Comment arrêter des chansons

La fonctionnalité d'arrêt supprimera toutes les chansons de la file d'attente et le bot quittera le canal vocal. Vous pouvez le faire en détruisant la file d'attente actuelle, ce qui fait automatiquement quitter le canal vocal au bot (sauf si vous le configurez autrement dans la configuration du lecteur).

```javascript
else if (interaction.commandName === "stop") {
        await interaction.deferReply();
        const queue = player.getQueue(interaction.guildId);
        if (!queue || !queue.playing) return void interaction.followUp({ content: "\u274c | Aucune musique n'est en cours de lecture !" });
        queue.destroy();
        return void interaction.followUp({ content: "\ud83d\uded1 | Lecteur arrêté !" });
    }
```

### Code source complet pour index.js :

Voici le code source complet pour le bot musical :

```javascript
const { Client, GuildMember, Intents } = require("discord.js");
const { Player, QueryType } = require("discord-player");
const config = require("./config.json");

const client = new Client({
    intents: [Intents.FLAGS.GUILD_VOICE_STATES, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILDS]
});

client.on("ready", () => {
    console.log("Bot est en ligne !");
    client.user.setActivity({
        name: "\ud83c\udfb6 | Heure de la musique",
        type: "LISTENING"
    });
});
client.on("error", console.error);
client.on("warn", console.warn);

const player = new Player(client);

player.on("error", (queue, error) => {
    console.log(`[${queue.guild.name}] Erreur émise depuis la file d'attente : ${error.message}`);
});
player.on("connectionError", (queue, error) => {
    console.log(`[${queue.guild.name}] Erreur émise depuis la connexion : ${error.message}`);
});

player.on("trackStart", (queue, track) => {
    queue.metadata.send(`\ud83c\udfb6 | Lecture démarrée : **${track.title}** dans **${queue.connection.channel.name}** !`);
});

player.on("trackAdd", (queue, track) => {
    queue.metadata.send(`\ud83c\udfb6 | Piste **${track.title}** mise en file d'attente !`);
});

player.on("botDisconnect", (queue) => {
    queue.metadata.send("\u274c | J'ai été déconnecté manuellement du canal vocal, vidange de la file d'attente !");
});

player.on("channelEmpty", (queue) => {
    queue.metadata.send("\u274c | Personne n'est dans le canal vocal, je quitte...");
});

player.on("queueEnd", (queue) => {
    queue.metadata.send("\u2705 | File d'attente terminée !");
});

client.on("messageCreate", async (message) => {
    if (message.author.bot || !message.guild) return;
    if (!client.application?.owner) await client.application?.fetch();

    if (message.content === "!deploy" && message.author.id === client.application?.owner?.id) {
        await message.guild.commands.set([
            {
                name: "play",
                description: "Joue une chanson depuis YouTube",
                options: [
                    {
                        name: "query",
                        type: "STRING",
                        description: "La chanson que vous voulez jouer",
                        required: true
                    }
                ]
            },
            {
                name: "skip",
                description: "Passer à la chanson actuelle"
            },
            {
                name: "stop",
                description: "Arrêter le lecteur"
            },
        ]);

        await message.reply("Déployé !");
    }
});

client.on("interactionCreate", async (interaction) => {
    if (!interaction.isCommand() || !interaction.guildId) return;

    if (!(interaction.member instanceof GuildMember) || !interaction.member.voice.channel) {
        return void interaction.reply({ content: "Vous n'êtes pas dans un canal vocal !", ephemeral: true });
    }

    if (interaction.guild.me.voice.channelId && interaction.member.voice.channelId !== interaction.guild.me.voice.channelId) {
        return void interaction.reply({ content: "Vous n'êtes pas dans mon canal vocal !", ephemeral: true });
    }

    if (interaction.commandName === "play") {
        await interaction.deferReply();

        const query = interaction.options.get("query").value;
        const searchResult = await player
            .search(query, {
                requestedBy: interaction.user,
                searchEngine: QueryType.AUTO
            })
            .catch(() => {});
        if (!searchResult || !searchResult.tracks.length) return void interaction.followUp({ content: "Aucun résultat trouvé !" });

        const queue = await player.createQueue(interaction.guild, {
            metadata: interaction.channel
        });

        try {
            if (!queue.connection) await queue.connect(interaction.member.voice.channel);
        } catch {
            void player.deleteQueue(interaction.guildId);
            return void interaction.followUp({ content: "Impossible de rejoindre votre canal vocal !" });
        }

        await interaction.followUp({ content: `\u23f1 | Chargement de votre ${searchResult.playlist ? "playlist" : "piste"}...` });
        searchResult.playlist ? queue.addTracks(searchResult.tracks) : queue.addTrack(searchResult.tracks[0]);
        if (!queue.playing) await queue.play();
    } else if (interaction.commandName === "skip") {
        await interaction.deferReply();
        const queue = player.getQueue(interaction.guildId);
        if (!queue || !queue.playing) return void interaction.followUp({ content: "\u274c | Aucune musique n'est en cours de lecture !" });
        const currentTrack = queue.current;
        const success = queue.skip();
        return void interaction.followUp({
            content: success ? `\u2705 | Piste **${currentTrack}** sautée !` : "\u274c | Quelque chose s'est mal passé !"
        });
    } else if (interaction.commandName === "stop") {
        await interaction.deferReply();
        const queue = player.getQueue(interaction.guildId);
        if (!queue || !queue.playing) return void interaction.followUp({ content: "\u274c | Aucune musique n'est en cours de lecture !" });
        queue.destroy();
        return void interaction.followUp({ content: "\ud83d\uded1 | Lecteur arrêté !" });
    } else {
        interaction.reply({
            content: "Commande inconnue !",
            ephemeral: true
        });
    }
});

client.login(config.token);
```

## **Version 0.12 du bot Discord**

Maintenant, vous devrez simplement installer quelques dépendances avant de pouvoir commencer.

```
npm install discord.js ffmpeg fluent-ffmpeg @discordjs/opus ytdl-core --save
```

Après avoir installé les dépendances, importez-les dans vos dépendances.

```
const Discord = require('discord.js');
const {
	prefix,
	token,
} = require('./config.json');
const ytdl = require('ytdl-core');
```

Après cela, créez votre client et connectez-vous en utilisant votre token.

```javascript
const client = new Discord.Client();
client.login(token);
```

Maintenant, ajoutons quelques écouteurs de base qui console.log lorsqu'ils sont exécutés.

```
client.once('ready', () => {
 console.log('Prêt !');
});
client.once('reconnecting', () => {
 console.log('Reconnexion !');
});
client.once('disconnect', () => {
 console.log('Déconnecté !');
});
```

Après cela, vous pouvez démarrer votre bot en utilisant la commande `node` et il devrait être en ligne sur Discord et imprimer « Prêt ! » dans la console.

```bash
node index.js
```

### Comment lire les messages

Maintenant que votre bot est sur votre serveur et capable de se connecter, vous pouvez commencer à lire les messages du chat et à y répondre.

Pour lire les messages, vous n'avez besoin d'écrire qu'une simple fonction :

```javascript
client.on('message', async message => {
  
}
```

Ici, vous créez un écouteur pour l'événement message, obtenez le message et le sauvegardez dans un objet message s'il est déclenché.

Maintenant, vous devez vérifier si le message provient de votre propre bot et l'ignorer si c'est le cas.

```
if (message.author.bot) return;
```

Dans cette ligne, vous vérifiez si l'auteur du message est votre bot et vous retournez si c'est le cas.

Après cela, vérifiez si le message commence par le préfixe que vous avez défini précédemment et retournez si ce n'est pas le cas.

```
if (!message.content.startsWith(prefix)) return;
```

Après cela, vous pouvez vérifier quelle commande vous devez exécuter. Vous pouvez le faire en utilisant quelques instructions if simples :

```javascript
const serverQueue = queue.get(message.guild.id);

if (message.content.startsWith(`${prefix}play`)) {
    execute(message, serverQueue);
    return;
} else if (message.content.startsWith(`${prefix}skip`)) {
    skip(message, serverQueue);
    return;
} else if (message.content.startsWith(`${prefix}stop`)) {
    stop(message, serverQueue);
    return;
} else {
    message.channel.send("Vous devez entrer une commande valide !");
}
```

Dans ce bloc de code, vous vérifiez quelle commande exécuter et appelez la commande. Si la commande d'entrée n'est pas valide, vous écrivez un message d'erreur dans le chat en utilisant la fonction `send()`.

Maintenant que vous savez quelle commande vous devez exécuter, vous pouvez commencer à implémenter ces commandes.

### Comment ajouter des chansons

Commençons par ajouter la commande play. Pour cela, vous aurez besoin d'une chanson et d'une guilde (une guilde représente une collection isolée d'utilisateurs et de canaux et est souvent appelée serveur). Vous aurez également besoin de la bibliothèque ytdl que vous avez installée précédemment.

Tout d'abord, créez une map avec le nom de la file d'attente où vous sauvegardez toutes les chansons que vous tapez dans le chat.

```javascript
const queue = new Map();
```

Après cela, créez une fonction asynchrone appelée execute et vérifiez si l'utilisateur est dans un chat vocal et si le bot a les bonnes permissions. Si ce n'est pas le cas, écrivez un message d'erreur et retournez.

```javascript
async function execute(message, serverQueue) {
  const args = message.content.split(" ");

  const voiceChannel = message.member.voice.channel;
  if (!voiceChannel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour lire de la musique !"
    );
  const permissions = voiceChannel.permissionsFor(message.client.user);
  if (!permissions.has("CONNECT") || !permissions.has("SPEAK")) {
    return message.channel.send(
      "J'ai besoin des permissions pour rejoindre et parler dans votre canal vocal !"
    );
  }
}
```

Maintenant, vous pouvez continuer en obtenant les informations de la chanson et en les sauvegardant dans un objet chanson. Pour cela, utilisez votre bibliothèque `ytdl` qui obtient les informations de la chanson à partir du lien YouTube.

```javascript
const songInfo = await ytdl.getInfo(args[1]);
const song = {
 title: songInfo.title,
 url: songInfo.video_url,
};
```

Cela obtiendra les informations de la chanson en utilisant la bibliothèque `ytdl` que vous avez installée précédemment. Ensuite, sauvegardez les informations dont vous avez besoin dans un objet chanson.

Après avoir sauvegardé les informations de la chanson, vous devez simplement créer un contrat que vous pouvez ajouter à votre file d'attente. 

Pour ce faire, vérifiez d'abord si votre serverQueue est déjà défini, ce qui signifie que de la musique est déjà en cours de lecture. Si c'est le cas, ajoutez la chanson à votre serverQueue existant et envoyez un message de succès. Si ce n'est pas le cas, créez-le et essayez de rejoindre le canal vocal et commencez à lire de la musique.

```javascript
if (!serverQueue) {

}else {
 serverQueue.songs.push(song);
 console.log(serverQueue.songs);
 return message.channel.send(`${song.title} a été ajouté à la file d'attente !`);
}
```

Ici, vérifiez si le `serverQueue` est vide et ajoutez la chanson si ce n'est pas le cas. Maintenant, vous devez simplement créer votre contrat si le `serverQueue` est null.

```javascript
// Création du contrat pour notre file d'attente
const queueContruct = {
 textChannel: message.channel,
 voiceChannel: voiceChannel,
 connection: null,
 songs: [],
 volume: 5,
 playing: true,
};
// Définition de la file d'attente en utilisant notre contrat
queue.set(message.guild.id, queueContruct);
// Ajout de la chanson à notre tableau de chansons
queueContruct.songs.push(song);

try {
 // Ici, nous essayons de rejoindre le vocal et de sauvegarder notre connexion dans notre objet.
 var connection = await voiceChannel.join();
 queueContruct.connection = connection;
 // Appel de la fonction play pour démarrer une chanson
 play(message.guild, queueContruct.songs[0]);
} catch (err) {
 // Affichage du message d'erreur si le bot échoue à rejoindre le vocal
 console.log(err);
 queue.delete(message.guild.id);
 return message.channel.send(err);
}
```

Dans ce bloc de code, vous avez créé un contrat et ajouté votre chanson au tableau de chansons. Après cela, vous avez essayé de rejoindre le chat vocal de l'utilisateur et appelé votre fonction `play()` que vous implémenterez après cela.

### Comment lire des chansons

Maintenant que vous pouvez ajouter nos chansons à votre file d'attente et créer un contrat s'il n'y en a pas encore, vous pouvez implémenter la fonctionnalité de lecture.

Tout d'abord, créez une fonction appelée play qui prend deux paramètres (la guilde et la chanson que vous voulez jouer) et vérifie si la chanson est vide. Si c'est le cas, quittez simplement le canal vocal et supprimez la file d'attente.

```javascript
function play(guild, song) {
  const serverQueue = queue.get(guild.id);
  if (!song) {
    serverQueue.voiceChannel.leave();
    queue.delete(guild.id);
    return;
  }
}
```

Après cela, commencez à lire votre chanson en utilisant la fonction `play()` de la connexion et en passant l'URL de votre chanson.

```javascript
const dispatcher = serverQueue.connection
    .play(ytdl(song.url))
    .on("finish", () => {
        serverQueue.songs.shift();
        play(guild, serverQueue.songs[0]);
    })
    .on("error", error => console.error(error));
dispatcher.setVolumeLogarithmic(serverQueue.volume / 5);
serverQueue.textChannel.send(`Démarrage de la lecture : **${song.title}**`);
```

Ici, vous avez créé un flux et lui avez passé l'URL de notre chanson. Vous avez également ajouté deux écouteurs qui gèrent les événements de fin et d'erreur.

**Note :** Il s'agit d'une fonction récursive, ce qui signifie qu'elle s'appelle elle-même encore et encore. Nous utilisons la récursion pour qu'elle joue la chanson suivante lorsque la chanson est terminée.

Maintenant, vous êtes prêt à lire une chanson en tapant simplement !play URL dans le chat.

### Comment sauter des chansons

Maintenant, vous pouvez implémenter la fonctionnalité de saut. Pour cela, vous devez simplement mettre fin au dispatcher que vous avez créé dans votre fonction `play()` pour qu'il commence la chanson suivante.

```javascript
function skip(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour arrêter la musique !"
    );
  if (!serverQueue)
    return message.channel.send("Il n'y a pas de chanson que je pourrais sauter !");
  serverQueue.connection.dispatcher.end();
}

```

Ici, vous vérifiez si l'utilisateur qui a tapé la commande est dans un canal vocal et s'il y a une chanson à sauter.

### Comment arrêter des chansons

La fonction `stop()` est presque la même que `skip()`, sauf que vous videz le tableau de chansons, ce qui fera supprimer la file d'attente par votre bot et quitter le chat vocal.

```javascript
function stop(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour arrêter la musique !"
    );
  serverQueue.songs = [];
  serverQueue.connection.dispatcher.end();
}
```

### Code source complet pour index.js :

Voici le code source complet pour le bot musical :

```javascript
const Discord = require("discord.js");
const { prefix, token } = require("./config.json");
const ytdl = require("ytdl-core");

const client = new Discord.Client();

const queue = new Map();

client.once("ready", () => {
  console.log("Prêt !");
});

client.once("reconnecting", () => {
  console.log("Reconnexion !");
});

client.once("disconnect", () => {
  console.log("Déconnecté !");
});

client.on("message", async message => {
  if (message.author.bot) return;
  if (!message.content.startsWith(prefix)) return;

  const serverQueue = queue.get(message.guild.id);

  if (message.content.startsWith(`${prefix}play`)) {
    execute(message, serverQueue);
    return;
  } else if (message.content.startsWith(`${prefix}skip`)) {
    skip(message, serverQueue);
    return;
  } else if (message.content.startsWith(`${prefix}stop`)) {
    stop(message, serverQueue);
    return;
  } else {
    message.channel.send("Vous devez entrer une commande valide !");
  }
});

async function execute(message, serverQueue) {
  const args = message.content.split(" ");

  const voiceChannel = message.member.voice.channel;
  if (!voiceChannel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour lire de la musique !"
    );
  const permissions = voiceChannel.permissionsFor(message.client.user);
  if (!permissions.has("CONNECT") || !permissions.has("SPEAK")) {
    return message.channel.send(
      "J'ai besoin des permissions pour rejoindre et parler dans votre canal vocal !"
    );
  }

  const songInfo = await ytdl.getInfo(args[1]);
  const song = {
    title: songInfo.title,
    url: songInfo.video_url
  };

  if (!serverQueue) {
    const queueContruct = {
      textChannel: message.channel,
      voiceChannel: voiceChannel,
      connection: null,
      songs: [],
      volume: 5,
      playing: true
    };

    queue.set(message.guild.id, queueContruct);

    queueContruct.songs.push(song);

    try {
      var connection = await voiceChannel.join();
      queueContruct.connection = connection;
      play(message.guild, queueContruct.songs[0]);
    } catch (err) {
      console.log(err);
      queue.delete(message.guild.id);
      return message.channel.send(err);
    }
  } else {
    serverQueue.songs.push(song);
    return message.channel.send(`${song.title} a été ajouté à la file d'attente !`);
  }
}

function skip(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour arrêter la musique !"
    );
  if (!serverQueue)
    return message.channel.send("Il n'y a pas de chanson que je pourrais sauter !");
  serverQueue.connection.dispatcher.end();
}

function stop(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "Vous devez être dans un canal vocal pour arrêter la musique !"
    );
  serverQueue.songs = [];
  serverQueue.connection.dispatcher.end();
}

function play(guild, song) {
  const serverQueue = queue.get(guild.id);
  if (!song) {
    serverQueue.voiceChannel.leave();
    queue.delete(guild.id);
    return;
  }

  const dispatcher = serverQueue.connection
    .play(ytdl(song.url))
    .on("finish", () => {
      serverQueue.songs.shift();
      play(guild, serverQueue.songs[0]);
    })
    .on("error", error => console.error(error));
  dispatcher.setVolumeLogarithmic(serverQueue.volume / 5);
  serverQueue.textChannel.send(`Démarrage de la lecture : **${song.title}**`);
}

client.login(token);

```

## **Conclusion**

Vous avez réussi jusqu'à la fin ! J'espère que cet article vous a aidé à comprendre l'API Discord et comment vous pouvez l'utiliser pour créer un bot simple. 

Si vous souhaitez voir un exemple de bot Discord plus avancé, vous pouvez visiter mon [dépôt GitHub](https://github.com/TannerGabriel/discord-bot).

Si vous avez trouvé cela utile, envisagez de le recommander et de le partager avec d'autres développeurs.

Si vous avez des questions ou des commentaires, faites-le moi savoir et je serai heureux de vous aider.