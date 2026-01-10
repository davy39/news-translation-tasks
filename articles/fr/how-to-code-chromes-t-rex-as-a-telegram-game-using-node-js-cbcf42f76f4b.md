---
title: Comment coder le T-Rex de Chrome en tant que jeu Telegram en utilisant Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T15:27:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-chromes-t-rex-as-a-telegram-game-using-node-js-cbcf42f76f4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LqIHGPfQ0pZL-2rdQDkYyQ.png
tags:
- name: bots
  slug: bots
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment coder le T-Rex de Chrome en tant que jeu Telegram en utilisant
  Node.js
seo_desc: 'By Fernando García Álvarez

  Last month I was really interested in learning how the Telegram game platform works.
  And as I was also really bored of playing Chrome’s T-Rex game alone, I decided to
  make it work as a Telegram game.

  While developing it I n...'
---

Par Fernando García Álvarez

Le mois dernier, je m'intéressais vraiment à apprendre comment fonctionne la plateforme de jeux Telegram. Et comme je m'ennuyais aussi de jouer seul au jeu du T-Rex de Chrome, j'ai décidé de le faire fonctionner comme un jeu Telegram.

En le développant, j'ai remarqué qu'il n'y avait pas beaucoup de tutoriels sur les bots de jeux Telegram. Les tutoriels expliqueraient tout le processus de construction, du début à la fin. J'ai donc décidé d'écrire à ce sujet.

Si vous voulez voir le résultat, le jeu est disponible sous le nom de [trexjumpbot](https://telegram.me/trexjumpbot) sur Telegram et est hébergé [ici](https://trexgame.herokuapp.com).

### Prérequis

Vous devez avoir [Node.js](https://nodejs.org) installé

### Étape 1 : Créer notre bot

Pour créer un jeu, nous devons d'abord créer un bot en ligne. Nous faisons cela en parlant à [BotFather](https://telegram.me/botfather) et en envoyant la commande

`/newbot`

Ensuite, nous devons entrer un nom et un nom d'utilisateur pour notre bot et nous recevons un jeton API. Nous devons le sauvegarder car nous en aurons besoin plus tard.

Nous pouvons également compléter les informations de notre bot en modifiant sa description (qui sera affichée lorsqu'un utilisateur entre dans un chat avec notre bot sous la section « Que peut faire ce bot ? ») avec

`/setdescription`

Et aussi définir son image, afin de le rendre distinguable de la liste de chats. L'image doit être carrée et nous pouvons la définir avec la commande suivante :

`/setuserpic`

Nous pouvons également définir le texte de présentation, qui apparaîtra sur la page de profil du bot et également lors de son partage avec d'autres utilisateurs

`/setabouttext`

Notre bot doit être en ligne pour pouvoir l'utiliser pour notre jeu. Pour ce faire, nous devons simplement exécuter ce qui suit et suivre les instructions

`/setinline`

### Étape 2 : Créer notre jeu

Maintenant que notre bot en ligne est complètement configuré, il est temps de demander à BotFather de créer un jeu :

`/newgame`

Nous suivons simplement les instructions et enfin nous devons spécifier un nom court pour notre jeu. Cela servira d'identifiant unique pour celui-ci, dont nous aurons besoin plus tard avec notre jeton API de bot.

### Étape 3 : Obtenir le code source du jeu T-Rex

Comme Chromium est open source, certains utilisateurs ont extrait le jeu T-Rex et nous pouvons facilement trouver son code source en ligne.

Pour créer le jeu, j'ai utilisé le code disponible dans [ce dépôt GitHub](https://github.com/wayou/t-rex-runner), alors allez-y et clonez-le :

```
git clone https://github.com/wayou/t-rex-runner.git
```

### Étape 4 : Configurer les dépendances

Tout d'abord, allez dans le dossier cloné et déplacez tous ses fichiers dans un nouveau dossier appelé « public »

```
mkdir public && mv * public/.
```

Et initialisez le projet

```
npm init
```

Vous pouvez remplir les informations demandées comme vous le souhaitez (vous pouvez laisser les valeurs par défaut), laissez le point d'entrée comme index.js

Nous aurons besoin d'Express et de node-telegram-bot-api pour interagir facilement avec l'API de Telegram

```
npm install express --savenpm install node-telegram-bot-api --save
```

Nous allons ajouter un script de démarrage, car il est nécessaire pour déployer le jeu sur Heroku. Ouvrez package.json et ajoutez le script de démarrage sous la section scripts :

```
"scripts": {
```

```
"test": "echo \"Error: no test specified\" && exit 1",
```

```
"start": "node index.js"
```

```
}
```

### Étape 5 : Coder notre serveur

Maintenant que nous avons toutes les dépendances configurées, il est temps de coder le serveur pour notre bot. Allez-y et créez le fichier index.js :

```
const express = require("express");
```

```
const path = require("path");
```

```
const TelegramBot = require("node-telegram-bot-api");
```

```
const TOKEN = "YOUR_API_TOKEN_GOES_HERE";
```

```
const server = express();
```

```
const bot = new TelegramBot(TOKEN, { polling: true } );
```

```
const port = process.env.PORT || 5000;
```

```
const gameName = "SHORT_NAME_YOUR_GAME";
```

```
const queries = {};
```

Le code ci-dessus est assez simple. Nous requérons simplement nos dépendances et définissons le jeton que nous avons obtenu de BotFather ainsi que le nom court que nous avons défini comme identifiant de jeu. Nous définissons également le port, initialisons Express et déclarons un objet queries vide. Cela servira de carte pour stocker l'objet utilisateur Telegram sous son identifiant, afin de le récupérer plus tard.

Ensuite, nous devons rendre le contenu du répertoire public disponible en tant que fichiers statiques

```
server.use(express.static(path.join(__dirname, 'public')));
```

Maintenant, nous allons commencer à définir la logique de notre bot. Tout d'abord, codons la commande /help

```
bot.onText(/help/, (msg) => bot.sendMessage(msg.from.id, "Ce bot implémente un jeu de saut de T-Rex. Dites /game si vous voulez jouer."));
```

Nous devons spécifier la commande sous forme de regex sur le premier paramètre de onText, puis spécifier la réponse du bot avec sendMessage. Notez que nous pouvons accéder à l'identifiant de l'utilisateur pour répondre en utilisant msg.from.id

Lorsque notre bot reçoit la commande /start ou /game, nous allons envoyer le jeu à l'utilisateur en utilisant bot.sendGame

```
bot.onText(/start|game/, (msg) => bot.sendGame(msg.from.id, gameName));
```

Maintenant, l'utilisateur verra le titre du jeu, son meilleur score et un bouton pour y jouer, mais le bouton de lecture ne fonctionne toujours pas. Nous allons donc implémenter sa logique

```
bot.on("callback_query", function (query) {
```

```
  if (query.game_short_name !== gameName) {
```

```
    bot.answerCallbackQuery(query.id, "Désolé, '" + query.game_short_name + "' n'est pas disponible.");
```

```
  } else {
```

```
    queries[query.id] = query;
```

```
    let gameurl = "https://YOUR_URL_HERE/index.html?id="+query.id;
```

```
    bot.answerCallbackQuery({
```

```
      callback_query_id: query.id,
```

```
      url: gameurl
```

```
    });
```

```
  }
```

```
});
```

Lorsque l'utilisateur clique sur le bouton de lecture, Telegram nous envoie un rappel. Dans le code ci-dessus, lorsque nous recevons ce rappel, nous vérifions d'abord que le jeu demandé est, en fait, notre jeu, et si ce n'est pas le cas, nous affichons une erreur à l'utilisateur.

Si tout est correct, nous stockons la requête dans l'objet queries défini précédemment sous son identifiant, afin de la récupérer plus tard pour définir le meilleur score si nécessaire. Ensuite, nous devons répondre au rappel en fournissant l'URL du jeu. Plus tard, nous allons le télécharger sur Heroku, vous devrez donc entrer l'URL ici. Notez que je passe l'identifiant en tant que paramètre de requête dans l'URL, afin de pouvoir définir un meilleur score.

Actuellement, nous avons un jeu entièrement fonctionnel, mais il nous manque encore les meilleurs scores et le comportement en ligne. Commençons par implémenter en ligne et offrir notre jeu :

```
bot.on("inline_query", function(iq) {
```

```
  bot.answerInlineQuery(iq.id, [ { type: "game", id: "0", game_short_name: gameName } ] );
```

```
});
```

Enfin, nous allons implémenter la logique du meilleur score :

```
server.get("/highscore/:score", function(req, res, next) {
```

```
  if (!Object.hasOwnProperty.call(queries, req.query.id)) return next();
```

```
  let query = queries[req.query.id];
```

```
  let options;
```

```
  if (query.message) {
```

```
    options = {
```

```
      chat_id: query.message.chat.id,
```

```
      message_id: query.message.message_id
```

```
    };
```

```
  } else {
```

```
    options = {
```

```
      inline_message_id: query.inline_message_id
```

```
    };
```

```
  }
```

```
  bot.setGameScore(query.from.id, parseInt(req.params.score), options,
```

```
  function (err, result) {});
```

```
});
```

Dans le code ci-dessus, nous écoutons les URL comme /highscore/300?id=5721. Nous récupérons simplement l'utilisateur à partir de l'objet queries donné son identifiant (s'il existe) et utilisons bot.setGameScore pour envoyer le meilleur score à Telegram. L'objet options est différent si l'utilisateur appelle le bot en ligne ou non, nous vérifions donc les deux situations comme défini dans l'[API Telegram Bot](https://core.telegram.org/bots/api#setgamescore)

La dernière chose que nous devons faire sur notre serveur est simplement d'écouter sur le port défini précédemment :

```
server.listen(port);
```

### Étape 6 : Modifier le jeu T-Rex

Nous devons modifier le jeu T-Rex que nous avons cloné depuis le dépôt GitHub afin qu'il envoie le meilleur score à notre serveur.

Ouvrez le fichier index.js sous le dossier public, et en haut de celui-ci, ajoutez les lignes suivantes afin de récupérer l'identifiant du joueur depuis l'URL :

```
var url = new URL(location.href);
```

```
var playerid = url.searchParams.get("id");
```

Enfin, nous allons localiser la fonction setHighScore et ajouter le code suivant à la fin de celle-ci, afin de soumettre le meilleur score à notre serveur :

```
// Soumettre le meilleur score à Telegram
```

```
var xmlhttp = new XMLHttpRequest();
```

```
var url = "https://YOUR_URL_HERE/highscore/" + distance +
```

```
"?id=" + playerid;
```

```
xmlhttp.open("GET", url, true);
```

```
xmlhttp.send();
```

### Étape 7 : Déployer sur Heroku

Notre jeu est complet, mais sans le télécharger sur un serveur, nous ne pouvons pas le tester sur Telegram, et Heroku nous fournit un moyen très simple de le télécharger.

Commencez par créer une nouvelle application :

![Image](https://cdn-media-1.freecodecamp.org/images/sx9aJgRZAn0RPPzDG1Qg0ZA44gZGfgylGrCr)

Remplacez nos espaces réservés d'URL par l'URL réelle (remplacez par la vôtre) :

Remplacez l'URL avec la fonction setHighScore

```
var url = "https://trexgame.herokuapp.com/highscore/" + distance +
```

```
"?id=" + playerid;
```

Et aussi sur le rappel sur le serveur :

```
let gameurl = "https://trexgame.herokuapp.com/index.html?id="+query.id;
```

Enfin, téléchargeons notre jeu sur Heroku. Suivons les étapes détaillées sur la page Heroku : Après avoir installé [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), depuis le dossier du projet, connectez-vous et poussez les fichiers :

```
heroku logingit initheroku git:remote -a YOUR_HEROKU_APP_NAMEgit add .git commit -m "initial commit"git push heroku master
```

Et c'est tout ! Maintenant, vous avez enfin un jeu Telegram entièrement fonctionnel. Allez-y et essayez-le !

Le code source complet de cet exemple est disponible sur [GitHub](https://github.com/fercarcedo/T-Rex-Telegram-game)

### Références

* [http://wimi5.com/como-crear-un-bot-para-juegos-en-telegram-con-nodejs/](http://wimi5.com/como-crear-un-bot-para-juegos-en-telegram-con-nodejs/)
* [https://core.telegram.org/bots/api#setgamescore](https://core.telegram.org/bots/api#setgamescore)
* [https://github.com/wayou/t-rex-runner](https://github.com/wayou/t-rex-runner)