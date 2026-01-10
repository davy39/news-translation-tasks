---
title: How to create a two-player game with Python and Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-30T23:35:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-two-player-game-with-python-and-vue-4220c5592d53
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nvqAP0AgGAWA6-vu.gif
tags:
- name: gaming
  slug: gaming
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Neo Ighodaro

  In this tutorial, we will create a realtime tic-tac-toe game using Python and Pusher
  channels. Here’s a demo of how the game will look and behave upon creation:


  You will need Python 3+, virtualenv, and Flask installed on your machine...'
---

By Neo Ighodaro

In this tutorial, we will create a realtime tic-tac-toe game using Python and Pusher channels. Here’s a demo of how the game will look and behave upon creation:

![Image](https://cdn-media-1.freecodecamp.org/images/MuzX8tcbRETbqqNijym55kvnzPcPcsOqZbJp)

You will need Python 3+, virtualenv, and Flask installed on your machine.The advent of the PC and the internet has redefined the term “entertainment” and the means by which it can be obtained. While a console or some special hardware would have been required to play games in the past, games are only a click away in today’s world of technology.

This multiplayer game will allow a player to connect using their preferred username (or generate a random username where a player doesn’t connect with a username) and choose to play with another player from a list of other online players.

The game itself follows the conventional principles of the popular [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game. The “online player(s)” feature is powered by [Pusher presence channels](https://pusher.com/docs/client_api_guide/client_presence_channels) and the realtime updates of a player’s move across multiple windows is powered by [Pusher private channels.](https://pusher.com/docs/client_api_guide/client_private_channels) The source code for this tutorial is available here [GitHub](https://github.com/neoighodaro/python-pusher-multiplayer-game).

Let’s get started.

### Prerequisites

To follow along, a basic knowledge of Python, Flask, JavaScript (ES6 syntax) and Vue is required. You will also need the following installed on your machine:

1. [Python (v3.x)](https://www.python.org/)
2. [Virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [Flask](http://flask.pocoo.org/)

Virtualenv is great for creating isolated Python environments, so we can install dependencies in an isolated environment without polluting our global packages directory.

### Setting up the environment

We will create the project folder and activate a virtual environment within it:

```bash
$ mkdir python-pusher-mutiplayer-game
    $ cd python-pusher-mutiplayer-game
    $ virtualenv .venv
    $ source .venv/bin/activate # Linux based systems
    $ \path\to\env\Scripts\activate # Windows users
```

We will install [Flask](http://flask.pocoo.org/) using this command:

```bash
$ pip install flask
```

### Setting up Pusher

To integrate Pusher into the multiplayer game, we need to create a Pusher channels application from the Pusher dashboard. If you don’t already have a Pusher account, head over to the [Pusher website](https://pusher.com/) and create one.

After creating an account, create a new channels application and enable client events from the application dashboard. To enable client events, click on **App settings** and scroll to the bottom of the page then select the option that says **Enable client events,** and update the **App settings.**

### Building the backend server

Back in the project directory, let’s install the [Python Pusher library](https://github.com/pusher/pusher-http-python) with this command:

```bash
$ pip install pusher
```

We will create a new file and call it `app.py`, this is where we will write all the code for the Flask backend server. We will also create a folder and call it `templates`, this folder will hold the markup files for this application.

Let’s write some code to register the endpoints for the game and serve the view, open the `app.py` file and paste the following code:

```py
// File: ./app.py
    from flask import Flask, render_template, request, jsonify, make_response, json
    from pusher import pusher
    app = Flask(__name__)
    pusher = pusher_client = pusher.Pusher(
      app_id='PUSHER_APP_ID',
      key='PUSHER_APP_KEY',
      secret='PUSHER_APP_SECRET',
      cluster='PUSHER_APP_CLUSTER',
      ssl=True
    )
    name = ''
    @app.route('/')
    def index():
      return render_template('index.html')
    @app.route('/play')
    def play():
      global name
      name = request.args.get('username')
      return render_template('play.html')
    @app.route("/pusher/auth", methods=['POST'])
    def pusher_authentication():
      auth = pusher.authenticate(
        channel=request.form['channel_name'],
        socket_id=request.form['socket_id'],
        custom_data={
          u'user_id': name,
          u'user_info': {
            u'role': u'player'
          }
        }
      )
      return json.dumps(auth)
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
    name = ''
```

> _Replace the `PUSHER_APP_*` keys with the values on your Pusher dashboard._

In the code above, we defined three endpoints, here’s what they do:

* `/` - renders the front page that asks a player to connect with a username.
* `/play` - renders the game view.
* `/pusher/auth` - authenticates Pusher’s presence and private channels for connected players.

### Building the frontend

In the `templates` folder, we will create two files:

1. `index.html`
2. `play.html`

The `index.html` file will render the connection page, so open the `templates/index.html` file and paste the following code:

```html
<!-- File: ./templates/index.html -->
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="Neo Ighodaro">
            <title>TIC-TAC-TOE</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
            <style>
                  :root {
                    --input-padding-x: .75rem;
                    --input-padding-y: .75rem;
                  }
                  html,
                  body, body > div {
                    height: 100%;
                  }
                  body > div {
                    display: -ms-flexbox;
                    display: flex;
                    -ms-flex-align: center;
                    align-items: center;
                    padding-top: 40px;
                    padding-bottom: 40px;
                    background-color: #f5f5f5;
                  }
                  .form-signin {
                    width: 100%;
                    max-width: 420px;
                    padding: 15px;
                    margin: auto;
                  }
                  .form-label-group {
                    position: relative;
                    margin-bottom: 1rem;
                  }
                  .form-label-group > input,
                  .form-label-group > label {
                    padding: var(--input-padding-y) var(--input-padding-x);
                  }
                  .form-label-group > label {
                    position: absolute;
                    top: 0;
                    left: 0;
                    display: block;
                    width: 100%;
                    margin-bottom: 0; /* Override default `<label>` margin */
                    line-height: 1.5;
                    color: #495057;
                    cursor: text; /* Match the input under the label */
                    border: 1px solid transparent;
                    border-radius: .25rem;
                    transition: all .1s ease-in-out;
                  }
                  .form-label-group input::-webkit-input-placeholder {
                    color: transparent;
                  }
                  .form-label-group input:-ms-input-placeholder {
                    color: transparent;
                  }
                  .form-label-group input::-ms-input-placeholder {
                    color: transparent;
                  }
                  .form-label-group input::-moz-placeholder {
                    color: transparent;
                  }
                  .form-label-group input::placeholder {
                    color: transparent;
                  }
                  .form-label-group input:not(:placeholder-shown) {
                    padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
                    padding-bottom: calc(var(--input-padding-y) / 3);
                  }
                  .form-label-group input:not(:placeholder-shown) ~ label {
                    padding-top: calc(var(--input-padding-y) / 3);
                    padding-bottom: calc(var(--input-padding-y) / 3);
                    font-size: 12px;
                    color: #777;
                  }
            </style>
          </head>
          <body>
            <div id="app">
              <form class="form-signin">
                <div class="text-center mb-4">
                  <img class="mb-4" src="https://thestore.gameops.com/v/vspfiles/photos/Tic-Tac-Go-14.gif" alt="" width="72" height="72">
                  <h1 class="h3 mb-3 font-weight-normal">TIC-TAC-TOE</h1>
                  <p>PUT IN YOUR DETAILS TO PLAY</p>
                </div>
                <div class="form-label-group">
                    <input type="name" id="inputUsername" ref="username" class="form-control" placeholder="Username" required="" autofocus="">
                      <label for="inputUsername">Username</label>
                </div>
                <div class="form-label-group">
                  <input type="email" id="inputEmail" ref="email" class="form-control" placeholder="Email address" autofocus="" required>
                    <label for="inputEmail">Email address</label>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit" @click.prevent="login">Connect</button>
                <p class="mt-5 mb-3 text-muted text-center">© 2017-2018</p>
              </form>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
            <script>
            var app = new Vue({
              el: '#app',
              methods: {
                login: function () {
                  let username = this.$refs.username.value
                  let email = this.$refs.email.value
                  window.location.replace(`/play?username=${username}&email=${email}`);
                }
              }
            })
            </script>
        </body>
    </html>
```

When a player visits the connection page and puts in a username and email, the browser window will be redirected to the game view.

Let’s write the markup for the game view. Open the `play.html` file and paste the following code:

```html
<!-- file: ./templates/play.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
      <title>TIC-TAC-TOE</title>
    </head>
    <body>
      <div id="app" class="container-fluid">
        <div class="container-fluid clearfix mb-3 shadow">
          <img class="float-left my-3" src="https://thestore.gameops.com/v/vspfiles/photos/Tic-Tac-Go-14.gif" height="62px" width="62px"
          />
          <div class="float-right w-25 py-3">
            <img class="my-3 mx-3 rounded-circle border" src="http://dfsanonymous.club/wp-content/uploads/2017/11/DFSAnonymous-NewLogo.png"
              height="62px" width="62px" />
            <p class="d-inline"> {% raw %} {{ username }} {% endraw %} </p>
          </div>
        </div>
        <div class="row mx-5" style="height: 50vh">
          <div class="col-8 h-50 align-self-center">
            <div class="row border rounded invisible h-50 w-75 m-auto" style="font-size: 3.6rem" ref="gameboard" @click="playerAction">
              <div class="h-100 pr-2 col border border-dark" data-id="1" ref="1"></div>
              <div class="col pr-2 border border-dark" data-id="2" ref="2"></div>
              <div class="col pr-2 border border-dark" data-id="3" ref="3"></div>
              <div class="w-100"></div>
              <div class="h-100 pr-2 col border border-dark" data-id="4" ref="4"></div>
              <div class="col pr-2 border border-dark" data-id="5" ref="5"></div>
              <div class="col pr-2 border border-dark" data-id="6" ref="6"></div>
              <div class="w-100"></div>
              <div class="h-100 pr-2 col border border-dark" data-id="7" ref="7"></div>
              <div class="col pr-2 border border-dark" data-id="8" ref="8"></div>
              <div class="col pr-2 border border-dark" data-id="9" ref="9"></div>
            </div>
          </div>
          <div class="col-4 pl-3">
            <div class="row h-100">
              <div class="col border h-75 text-center" style="background: rgb(114, 230, 147);">
                <p class="my-3"> {% raw %} {{ players }} {% endraw %} online player(s) </p>
                <hr/>
                <li class="m-auto py-3 text-dark" style="cursor: pointer;" v-for="member in connectedPlayers" @click="choosePlayer">
                  {% raw %} {{ member }} {% endraw %}
                </li>
              </div>
              <div class="w-100"></div>
              <div class="col text-center py-3 border h-25" style="background: #b6c0ca; font-size: 1em; font-weight: bold">
                {% raw %} {{ status }} {% endraw %}
              </div>
            </div>
          </div>
        </div>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script src="https://js.pusher.com/4.2/pusher.min.js"></script>
      <script>
      </script>
    </body>
    </html>
```

The code above defines the layout of the game view but does not contain any interactivity or realtime features. In the scripts section, before the closing `body` tag, we included the Vue and Pusher libraries because they are required for the game to work.

Let’s include the JavaScript code that will drive the entire game process and define its logic.

In the same file, add the code below in between the `script` tag that is just before the closing `body` tag:

```js
var app = new Vue({
      el: '#app',
      data: {
        username: '',
        players: 0,
        connectedPlayers: [],
        status: '',
        pusher: new Pusher('PUSHER_APP_KEY', {
          authEndpoint: '/pusher/auth',
          cluster: 'PUSHER_APP_CLUSTER',
          encrypted: true
        }),
        otherPlayerName: '',
        mychannel: {},
        otherPlayerChannel: {},
        firstPlayer: 0,
        turn: 0,
        boxes: [0, 0, 0, 0, 0, 0, 0, 0, 0]
      },
      created () {
        let url = new URL(window.location.href);
        let name = url.searchParams.get("username");
        if (name) {
          this.username = name
          this.subscribe();
          this.listeners();
        } else {
          this.username = this.generateRandomName();
          location.assign("/play?username=" + this.username);
        }
      },
      methods: {
        // We will add methods here
      }
    });
```

> _Replace the `PUSHER_APP_*` keys with the keys on your Pusher dashboard._

Above, we create a new instance of Vue and we target the `#app` selector. We define all the defaults in the `data`object and then in the `create()` function which is called automatically when the Vue component is created, we check for a user and assign the user to the username if one was supplied.

We also make calls to the `subscribe` and `listeners` methods. Let’s define those inside the `methods` object. Inside the `methods` object, paste the following functions:

```js
// [...]
    subscribe: function () {
      let channel = this.pusher.subscribe('presence-channel');
      this.myChannel = this.pusher.subscribe('private-' + this.username)
      channel.bind('pusher:subscription_succeeded', (player) => {
        this.players = player.count - 1
        player.each((player) => {
          if (player.id != this.username)
            this.connectedPlayers.push(player.id)
        });
      });
      channel.bind('pusher:member_added', (player) => {
        this.players++;
        this.connectedPlayers.push(player.id)
      });
      channel.bind('pusher:member_removed', (player) => {
        this.players--;
        var index = this.connectedPlayers.indexOf(player.id);
        if (index > -1) {
          this.connectedPlayers.splice(index, 1)
        }
      });
    },
    listeners: function () {
      this.pusher.bind('client-' + this.username, (message) => {
        if (confirm('Do you want to start a game of Tic Tac Toe with ' + message)) {
          this.otherPlayerName = message
          this.otherPlayerChannel = this.pusher.subscribe('private-' + this.otherPlayerName)
          this.otherPlayerChannel.bind('pusher:subscription_succeeded', () => {
            this.otherPlayerChannel.trigger('client-game-started', this.username)
          })
          this.startGame(message)
        } else {
          this.otherPlayerChannel = this.pusher.subscribe('private-' + message)
          this.otherPlayerChannel.bind('pusher:subscription_succeeded', () => {
            this.otherPlayerChannel.trigger('client-game-declined', "")
          })
          this.gameDeclined()
        }
      }),
      this.myChannel.bind('client-game-started', (message) => {
        this.status = "Game started with " + message
        this.$refs.gameboard.classList.remove('invisible');
        this.firstPlayer = 1;
        this.turn = 1;
      })
      this.myChannel.bind('client-game-declined', () => {
        this.status = "Game declined"
      })
      this.myChannel.bind('client-new-move', (position) => {
        this.$refs[position].innerText = this.firstPlayer ? 'O' : 'X'
      })
      this.myChannel.bind('client-your-turn', () => {
        this.turn = 1;
      })
      this.myChannel.bind('client-box-update', (update) => {
        this.boxes = update;
      })
      this.myChannel.bind('client-you-lost', () => {
        this.gameLost();
      })
    },
    // [...]
```

In the `subscribe` method, we subscribe to our Pusher presence channel, and then subscribe to the private channel for the current user. In the `listeners` method we register the listeners for all the events we are expecting to be triggered on the private channel we subscribed to.

Next, we will add other helper methods to our methods class. Inside the methods class, add the following functions to the bottom after the `listeners` method:

```js
// Generates a random string we use as a name for a guest user
    generateRandomName: function () {
      let text = '';
      let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      for (var i = 0; i < 6; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
      }
      return text;
    },
    // Lets you choose a player to play as.
    choosePlayer: function (e) {
      this.otherPlayerName = e.target.innerText
      this.otherPlayerChannel = this.pusher.subscribe('private-' + this.otherPlayerName)
      this.otherPlayerChannel.bind('pusher:subscription_succeeded', () => {
        this.otherPlayerChannel.trigger('client-' + this.otherPlayerName, this.username)
      });
    },
    // Begins the game
    startGame: function (name) {
      this.status = "Game started with " + name
      this.$refs.gameboard.classList.remove('invisible');
    },
    // User declined to play
    gameDeclined: function () {
      this.status = "Game declined"
    },
    // Game has ended with current user winning
    gameWon: function () {
      this.status = "You WON!"
      this.$refs.gameboard.classList.add('invisible');
      this.restartGame()
    },
    // Game has ended with current user losing
    gameLost: function () {
      this.turn = 1;
      this.boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
      this.status = "You LOST!"
      this.$refs.gameboard.classList.add('invisible');
      this.restartGame()
    },
    // Restarts a game
    restartGame: function () {
      for (i = 1; i < 10; i++) {
        this.$refs[i].innerText = ""
      }
      this.$refs.gameboard.classList.remove('invisible');
    },
    // Checks tiles to see if the tiles passed are a match
    compare: function () {
      for (var i = 1; i < arguments.length; i++) {
        if (arguments[i] === 0 || arguments[i] !== arguments[i - 1]) {
          return false
        }
      }
      return true;
    },
    // Checks the tiles and returns true if theres a winning play
    theresAMatch: function () {
      return this.compare(this.boxes[0], this.boxes[1], this.boxes[2]) ||
        this.compare(this.boxes[3], this.boxes[4], this.boxes[5]) ||
        this.compare(this.boxes[6], this.boxes[7], this.boxes[8]) ||
        this.compare(this.boxes[0], this.boxes[3], this.boxes[6]) ||
        this.compare(this.boxes[1], this.boxes[4], this.boxes[7]) ||
        this.compare(this.boxes[2], this.boxes[5], this.boxes[8]) ||
        this.compare(this.boxes[2], this.boxes[4], this.boxes[6]) ||
        this.compare(this.boxes[0], this.boxes[4], this.boxes[8])
    },
    // Checks to see if the play was a winning play
    playerAction: function (e) {
      let index = e.target.dataset.id - 1
      let tile = this.firstPlayer ? 'X' : 'O'
      if (this.turn && this.boxes[index] == 0) {
        this.turn = 0
        this.boxes[index] = tile
        e.target.innerText = tile
        this.otherPlayerChannel.trigger('client-your-turn', "")
        this.otherPlayerChannel.trigger('client-box-update', this.boxes)
        this.otherPlayerChannel.trigger('client-new-move', e.target.dataset.id)
        if (this.theresAMatch()) {
          this.gameWon()
          this.boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
          this.otherPlayerChannel.trigger('client-you-lost', '')
        }
      }
    },
```

Above, we have added several helper methods that the game needs to function properly and before each method, we have added a comment to show what the method does.

Let’s test the game now.

### Testing the game

We can test the game by running this command:

```bash
$ flask run
```

Now if we visit [localhost:5000](http://localhost:5000/), we should see the connection page and test the game:

![Image](https://cdn-media-1.freecodecamp.org/images/Vmj8BM420J2JpEiLvfPO7qrLxfYiPHIGuwI6)

### Conclusion

In this tutorial, we have learned how to leverage the Pusher SDK in creating an online multiplayer game powered by a Python backend server.

The source code for this tutorial is available on [GitHub](https://github.com/neoighodaro/python-pusher-multiplayer-game)

This post first appeared on the [Pusher Blog](https://pusher.com/tutorials/game-python-vue)

