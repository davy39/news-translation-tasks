---
title: How to code Chrome’s T-Rex as a Telegram game using Node.js
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
seo_title: null
seo_desc: 'By Fernando García Álvarez

  Last month I was really interested in learning how the Telegram game platform works.
  And as I was also really bored of playing Chrome’s T-Rex game alone, I decided to
  make it work as a Telegram game.

  While developing it I n...'
---

By Fernando García Álvarez

Last month I was really interested in learning how the Telegram game platform works. And as I was also really bored of playing Chrome’s T-Rex game alone, I decided to make it work as a Telegram game.

While developing it I noticed there weren’t many Telegram game bot tutorials. Tutorial would explain the whole process of building it, from start to finish. So I decided to write about it.

If you want to see the result, the game is available as [trexjumpbot](https://telegram.me/trexjumpbot) in Telegram and is hosted [here](https://trexgame.herokuapp.com).

### Requirements

You need to have [Node.js](https://nodejs.org) installed

### Step 1: Creating our bot

In order to create a game, we must first create an inline bot. We do this by talking to [BotFather](https://telegram.me/botfather) and sending the command

`/newbot`

Then, we are asked to enter a name and a username for our bot and we are given an API token. We need to save it as we will need it later.

We can also complete our bot info by changing its description (which will be shown when a user enters a chat with our bot under the “What can this bot do?” section) with

`/setdescription`

And also set its picture, in order to make it distinguishable from the chat list. The image must be square and we can set it with the following command:

`/setuserpic`

We can also set the about text, which will appear on the bot’s profile page and also when sharing it with other users

`/setabouttext`

Our bot has to be inline in order to be able to use it for our game. In order to do this, we simply have to execute the following and follow the instructions

`/setinline`

### Step 2: Creating our game

Now that we have our inline bot completely set up, it’s time to ask BotFather to create a game:

`/newgame`

We simply follow the instructions and finally we have to specify a short name for our game. This will act as a unique identifier for it, which we will need later along with our bot API token

### Step 3: Getting T-Rex game source code

As Chromium is open source, some users have extracted the T-Rex game from it and we can easily find its source code online.

In order to make the game, I have used the code available in [this GitHub repo](https://github.com/wayou/t-rex-runner), so go ahead and clone it:

```
git clone https://github.com/wayou/t-rex-runner.git
```

### Step 4: Setting up dependencies

First, go into the cloned folder and move all its files into a new folder called “public”

```
mkdir public && mv * public/.
```

And init the project

```
npm init
```

You can fill the requested info as you want (you can leave the default values), leave the entry point as index.js

We will need Express and node-telegram-bot-api in order to easily interact with Telegram’s API

```
npm install express --savenpm install node-telegram-bot-api --save
```

We are going to add a start script, since it’s necessary in order to deploy the game to Heroku. Open package.json and add the start script under the scripts section:

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

### Step 5: Coding our server

Now that we have all dependencies set up, it’s time to code the server for our bot. Go ahead and create the index.js file:

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

The code above is pretty straightforward. We simply require our dependencies and set the token we got from BotFather and also the short name we defined as the game identifier. Also, we set up the port, initialize Express and declare a queries empty object. This will act as a map to store the Telegram user object under his id, in order to retrieve it later.

Next, we need to make the contents of the public directory available as static files

```
server.use(express.static(path.join(__dirname, 'public')));
```

Now we are going to start defining our bot logic. First, let’s code the /help command

```
bot.onText(/help/, (msg) => bot.sendMessage(msg.from.id, "This bot implements a T-Rex jumping game. Say /game if you want to play."));
```

We have to specify the command as a regex on the first parameter of onText and then specify the bot’s reply with sendMessage. Note we can access the user id in order to reply by using msg.from.id

When our bot receives the /start or /game command we are going to send the game to the user using bot.sendGame

```
bot.onText(/start|game/, (msg) => bot.sendGame(msg.from.id, gameName));
```

Now the user will be shown the game’s title, his high score and a button to play it, but the play button still doesn’t work. So, we are going to implement its logic

```
bot.on("callback_query", function (query) {
```

```
  if (query.game_short_name !== gameName) {
```

```
    bot.answerCallbackQuery(query.id, "Sorry, '" + query.game_short_name + "' is not available.");
```

```
  } else {
```

```
    queries[query.id] = query;
```

```
    let gameurl = "https://YOUR_URL_HERE/index.html?  id="+query.id;
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

When the user clicks the play button Telegram sends us a callback. In the code above when we receive this callback first we check that the requested game is, in fact, our game, and if not we show an error to the user.

If all is correct, we store the query into the queries object defined earlier under its id, in order to retrieve it later to set the high score if necessary. Then we need to answer the callback by providing the game’s URL. Later we are going to upload it to Heroku so you’ll have to enter the URL here. Note that I’m passing the id as a query parameter in the URL, in order to be able to set a high score.

Right now we have a fully functional game but we still are missing high scores and inline behavior. Let’s start with implementing inline and offering our game:

```
bot.on("inline_query", function(iq) {
```

```
  bot.answerInlineQuery(iq.id, [ { type: "game", id: "0", game_short_name: gameName } ] );
```

```
});
```

Last, we are going to implement the high score logic:

```
server.get("/highscore/:score", function(req, res, next) {
```

```
  if (!Object.hasOwnProperty.call(queries, req.query.id)) return   next();
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
  bot.setGameScore(query.from.id, parseInt(req.params.score),  options,
```

```
  function (err, result) {});
```

```
});
```

In the code above, we listen for URLs like /highscore/300?id=5721. We simply retrieve the user from the queries object given its id (if it exists) and the use bot.setGameScore to send the high score to Telegram. The options object is different if the user is calling the bot inline or not, so we check both situations as defined in the [Telegram Bot API](https://core.telegram.org/bots/api#setgamescore)

The last thing we have to do on our server is to simply listen in the previously defined port:

```
server.listen(port);
```

### Step 6: Modifying T-Rex game

We have to modify the T-Rex game we cloned from the GitHub repo in order for it to send the high score to our server.

Open the index.js file under the public folder, and at the top of it add the following lines in order to retrieve the player id from the url:

```
var url = new URL(location.href);
```

```
var playerid = url.searchParams.get("id");
```

Last, we are going to locate the setHighScore function and add the following code to the end of it, in order to submit the high score to our server:

```
// Submit highscore to Telegram
```

```
var xmlhttp = new XMLHttpRequest();
```

```
var url = "https://YOUR_URL_HERE/highscore/" + distance  +
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

### Step 7: Deploying to Heroku

Our game is complete, but without uploading it to a server we can’t test it on Telegram, and Heroku provides us a very straightforward way to upload it.

Start by creating a new app:

![Image](https://cdn-media-1.freecodecamp.org/images/sx9aJgRZAn0RPPzDG1Qg0ZA44gZGfgylGrCr)

Change our URL placeholders with the actual URL (replace with your own):

Replace the URL with the setHighScore function

```
var url = "https://trexgame.herokuapp.com/highscore/" + distance +
```

```
"?id=" + playerid;
```

And also on the callback on the server:

```
let gameurl = "https://trexgame.herokuapp.com/index.html?id="+query.id;
```

Finally, let’s upload our game to Heroku. Let’s follow the steps detailed on the Heroku page: After installing [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), from the project folder login and push the files:

```
heroku logingit initheroku git:remote -a YOUR_HEROKU_APP_NAMEgit add .git commit -m "initial commit"git push heroku master
```

And that’s it!, now you finally have a fully working Telegram game. Go ahead and try it!

Full source code of this example is available on [GitHub](https://github.com/fercarcedo/T-Rex-Telegram-game)

### References

* [http://wimi5.com/como-crear-un-bot-para-juegos-en-telegram-con-nodejs/](http://wimi5.com/como-crear-un-bot-para-juegos-en-telegram-con-nodejs/)
* [https://core.telegram.org/bots/api#setgamescore](https://core.telegram.org/bots/api#setgamescore)
* [https://github.com/wayou/t-rex-runner](https://github.com/wayou/t-rex-runner)

