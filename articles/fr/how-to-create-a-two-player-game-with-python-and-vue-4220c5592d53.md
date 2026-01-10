---
title: Comment créer un jeu à deux joueurs avec Python et Vue
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
seo_title: Comment créer un jeu à deux joueurs avec Python et Vue
seo_desc: 'By Neo Ighodaro

  In this tutorial, we will create a realtime tic-tac-toe game using Python and Pusher
  channels. Here’s a demo of how the game will look and behave upon creation:


  You will need Python 3+, virtualenv, and Flask installed on your machine...'
---

Par Neo Ighodaro

Dans ce tutoriel, nous allons créer un jeu de morpion en temps réel en utilisant Python et les canaux Pusher. Voici une démonstration de l'apparence et du comportement du jeu une fois créé :

![Image](https://cdn-media-1.freecodecamp.org/images/MuzX8tcbRETbqqNijym55kvnzPcPcsOqZbJp)

Vous aurez besoin de Python 3+, virtualenv et Flask installés sur votre machine. L'avènement de l'ordinateur personnel et d'Internet a redéfini le terme "divertissement" et les moyens par lesquels on peut l'obtenir. Alors qu'une console ou un matériel spécial aurait été nécessaire pour jouer à des jeux par le passé, les jeux ne sont plus qu'à un clic dans le monde technologique d'aujourd'hui.

Ce jeu multijoueur permettra à un joueur de se connecter en utilisant son nom d'utilisateur préféré (ou de générer un nom d'utilisateur aléatoire si un joueur ne se connecte pas avec un nom d'utilisateur) et de choisir de jouer avec un autre joueur parmi une liste d'autres joueurs en ligne.

Le jeu lui-même suit les principes conventionnels du populaire jeu de [morpion](https://en.wikipedia.org/wiki/Tic-tac-toe). La fonctionnalité "joueur(s) en ligne" est alimentée par les [canaux de présence Pusher](https://pusher.com/docs/client_api_guide/client_presence_channels) et les mises à jour en temps réel des mouvements d'un joueur sur plusieurs fenêtres sont alimentées par les [canaux privés Pusher](https://pusher.com/docs/client_api_guide/client_private_channels). Le code source de ce tutoriel est disponible ici sur [GitHub](https://github.com/neoighodaro/python-pusher-multiplayer-game).

Commençons.

### Prérequis

Pour suivre ce tutoriel, une connaissance de base de Python, Flask, JavaScript (syntaxe ES6) et Vue est requise. Vous aurez également besoin des éléments suivants installés sur votre machine :

1. [Python (v3.x)](https://www.python.org/)
2. [Virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [Flask](http://flask.pocoo.org/)

Virtualenv est idéal pour créer des environnements Python isolés, afin que nous puissions installer des dépendances dans un environnement isolé sans polluer notre répertoire global de paquets.

### Configuration de l'environnement

Nous allons créer le dossier du projet et activer un environnement virtuel à l'intérieur :

```bash
$ mkdir python-pusher-mutiplayer-game
    $ cd python-pusher-mutiplayer-game
    $ virtualenv .venv
    $ source .venv/bin/activate # Systèmes basés sur Linux
    $ \path\to\env\Scripts\activate # Utilisateurs Windows
```

Nous allons installer [Flask](http://flask.pocoo.org/) en utilisant cette commande :

```bash
$ pip install flask
```

### Configuration de Pusher

Pour intégrer Pusher dans le jeu multijoueur, nous devons créer une application de canaux Pusher à partir du tableau de bord Pusher. Si vous n'avez pas déjà de compte Pusher, rendez-vous sur le [site web de Pusher](https://pusher.com/) et créez-en un.

Après avoir créé un compte, créez une nouvelle application de canaux et activez les événements clients à partir du tableau de bord de l'application. Pour activer les événements clients, cliquez sur **Paramètres de l'application** et faites défiler jusqu'en bas de la page, puis sélectionnez l'option qui dit **Activer les événements clients**, et mettez à jour les **Paramètres de l'application**.

### Construction du serveur backend

De retour dans le répertoire du projet, installons la [bibliothèque Python Pusher](https://github.com/pusher/pusher-http-python) avec cette commande :

```bash
$ pip install pusher
```

Nous allons créer un nouveau fichier et l'appeler `app.py`, c'est ici que nous écrirons tout le code pour le serveur backend Flask. Nous allons également créer un dossier et l'appeler `templates`, ce dossier contiendra les fichiers de balisage pour cette application.

Écrivons un peu de code pour enregistrer les points de terminaison pour le jeu et servir la vue, ouvrez le fichier `app.py` et collez le code suivant :

```py
// Fichier : ./app.py
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

> _Remplacez les clés `PUSHER_APP_*` par les valeurs de votre tableau de bord Pusher._

Dans le code ci-dessus, nous avons défini trois points de terminaison, voici ce qu'ils font :

* `/` - affiche la page d'accueil qui demande à un joueur de se connecter avec un nom d'utilisateur.
* `/play` - affiche la vue du jeu.
* `/pusher/auth` - authentifie les canaux de présence et privés de Pusher pour les joueurs connectés.

### Construction du frontend

Dans le dossier `templates`, nous allons créer deux fichiers :

1. `index.html`
2. `play.html`

Le fichier `index.html` affichera la page de connexion, alors ouvrez le fichier `templates/index.html` et collez le code suivant :

```html
<!-- Fichier : ./templates/index.html -->
    <!DOCTYPE html>
    <html lang="fr">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="Neo Ighodaro">
            <title>MORPION</title>
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
                    margin-bottom: 0; /* Remplacer la marge par défaut du `<label>` */
                    line-height: 1.5;
                    color: #495057;
                    cursor: text; /* Correspondre à l'entrée sous le label */
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
                  <h1 class="h3 mb-3 font-weight-normal">MORPION</h1>
                  <p>ENTREZ VOS DÉTAILS POUR JOUER</p>
                </div>
                <div class="form-label-group">
                    <input type="name" id="inputUsername" ref="username" class="form-control" placeholder="Nom d'utilisateur" required="" autofocus="">
                      <label for="inputUsername">Nom d'utilisateur</label>
                </div>
                <div class="form-label-group">
                  <input type="email" id="inputEmail" ref="email" class="form-control" placeholder="Adresse e-mail" autofocus="" required>
                    <label for="inputEmail">Adresse e-mail</label>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit" @click.prevent="login">Se connecter</button>
                <p class="mt-5 mb-3 text-muted text-center">
9 2017-2018</p>
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

Lorsque qu'un joueur visite la page de connexion et entre un nom d'utilisateur et un e-mail, la fenêtre du navigateur sera redirigée vers la vue du jeu.

Écrivons le balisage pour la vue du jeu. Ouvrez le fichier `play.html` et collez le code suivant :

```html
<!-- fichier : ./templates/play.html -->
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
      <title>MORPION</title>
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
                <p class="my-3"> {% raw %} {{ players }} {% endraw %} joueur(s) en ligne </p>
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

Le code ci-dessus définit la disposition de la vue du jeu mais ne contient aucune interactivité ou fonctionnalité en temps réel. Dans la section des scripts, avant la balise de fermeture `body`, nous avons inclus les bibliothèques Vue et Pusher car elles sont nécessaires pour que le jeu fonctionne.

Incluons le code JavaScript qui pilotera l'ensemble du processus du jeu et définira sa logique.

Dans le même fichier, ajoutez le code ci-dessous entre la balise `script` qui se trouve juste avant la balise de fermeture `body` :

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
        // Nous ajouterons des méthodes ici
      }
    });
```

> _Remplacez les clés `PUSHER_APP_*` par les clés de votre tableau de bord Pusher._

Ci-dessus, nous créons une nouvelle instance de Vue et nous ciblons le sélecteur `#app`. Nous définissons toutes les valeurs par défaut dans l'objet `data` et ensuite dans la fonction `create()` qui est appelée automatiquement lorsque le composant Vue est créé, nous vérifions la présence d'un utilisateur et attribuons l'utilisateur au nom d'utilisateur si un nom a été fourni.

Nous faisons également appel aux méthodes `subscribe` et `listeners`. Définissons celles-ci à l'intérieur de l'objet `methods`. À l'intérieur de l'objet `methods`, collez les fonctions suivantes :

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
        if (confirm('Voulez-vous commencer une partie de Morpion avec ' + message)) {
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
        this.status = "Partie commencée avec " + message
        this.$refs.gameboard.classList.remove('invisible');
        this.firstPlayer = 1;
        this.turn = 1;
      })
      this.myChannel.bind('client-game-declined', () => {
        this.status = "Partie déclinée"
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

Dans la méthode `subscribe`, nous nous abonnons à notre canal de présence Pusher, puis nous nous abonnons au canal privé pour l'utilisateur actuel. Dans la méthode `listeners`, nous enregistrons les écouteurs pour tous les événements que nous attendons d'être déclenchés sur le canal privé auquel nous nous sommes abonnés.

Ensuite, nous allons ajouter d'autres méthodes d'assistance à notre classe de méthodes. À l'intérieur de la classe de méthodes, ajoutez les fonctions suivantes à la fin après la méthode `listeners` :

```js
// Génère une chaîne aléatoire que nous utilisons comme nom pour un utilisateur invité
    generateRandomName: function () {
      let text = '';
      let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      for (var i = 0; i < 6; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
      }
      return text;
    },
    // Permet de choisir un joueur avec qui jouer.
    choosePlayer: function (e) {
      this.otherPlayerName = e.target.innerText
      this.otherPlayerChannel = this.pusher.subscribe('private-' + this.otherPlayerName)
      this.otherPlayerChannel.bind('pusher:subscription_succeeded', () => {
        this.otherPlayerChannel.trigger('client-' + this.otherPlayerName, this.username)
      });
    },
    // Commence le jeu
    startGame: function (name) {
      this.status = "Partie commencée avec " + name
      this.$refs.gameboard.classList.remove('invisible');
    },
    // L'utilisateur a refusé de jouer
    gameDeclined: function () {
      this.status = "Partie déclinée"
    },
    // Le jeu s'est terminé avec l'utilisateur actuel gagnant
    gameWon: function () {
      this.status = "Vous avez GAGNÉ !"
      this.$refs.gameboard.classList.add('invisible');
      this.restartGame()
    },
    // Le jeu s'est terminé avec l'utilisateur actuel perdant
    gameLost: function () {
      this.turn = 1;
      this.boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
      this.status = "Vous avez PERDU !"
      this.$refs.gameboard.classList.add('invisible');
      this.restartGame()
    },
    // Redémarre un jeu
    restartGame: function () {
      for (i = 1; i < 10; i++) {
        this.$refs[i].innerText = ""
      }
      this.$refs.gameboard.classList.remove('invisible');
    },
    // Vérifie les cases pour voir si les cases passées sont une correspondance
    compare: function () {
      for (var i = 1; i < arguments.length; i++) {
        if (arguments[i] === 0 || arguments[i] !== arguments[i - 1]) {
          return false
        }
      }
      return true;
    },
    // Vérifie les cases et retourne vrai s'il y a un coup gagnant
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
    // Vérifie si le coup était un coup gagnant
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

Ci-dessus, nous avons ajouté plusieurs méthodes d'assistance dont le jeu a besoin pour fonctionner correctement et avant chaque méthode, nous avons ajouté un commentaire pour montrer ce que fait la méthode.

Testons le jeu maintenant.

### Tester le jeu

Nous pouvons tester le jeu en exécutant cette commande :

```bash
$ flask run
```

Maintenant, si nous visitons [localhost:5000](http://localhost:5000/), nous devrions voir la page de connexion et tester le jeu :

![Image](https://cdn-media-1.freecodecamp.org/images/Vmj8BM420J2JpEiLvfPO7qrLxfYiPHIGuwI6)

### Conclusion

Dans ce tutoriel, nous avons appris comment exploiter le SDK Pusher pour créer un jeu multijoueur en ligne alimenté par un serveur backend Python.

Le code source de ce tutoriel est disponible sur [GitHub](https://github.com/neoighodaro/python-pusher-multiplayer-game)

Cet article est d'abord apparu sur le [Blog Pusher](https://pusher.com/tutorials/game-python-vue)