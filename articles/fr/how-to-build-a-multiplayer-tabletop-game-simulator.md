---
title: Comment construire un simulateur de jeu de table multijoueur avec Vue, Phaser,
  Node, Express et Socket.IO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T23:31:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-multiplayer-tabletop-game-simulator
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/How-to-Tabletop-Game-Simulator
seo_title: Comment construire un simulateur de jeu de table multijoueur avec Vue,
  Phaser, Node, Express et Socket.IO
---

Thumb.png
étiquettes:
- name: ES6
  slug: es6
- name: Express
  slug: express
- name: Express JS
  slug: express-js
- name: Express.js
  slug: expressjs
- name: Développement de jeux
  slug: game-development
- name: GameDev
  slug: gamedev
- name: JavaScript
  slug: javascript
- name: phaser 3
  slug: phaser-3
- name: SocketIO
  slug: socketio
seo_title: null
seo_desc: "Par M. S. Farzan\nAssembler toutes les pièces d'une application JavaScript full stack peut être une entreprise complexe.  \nDans ce tutoriel, nous allons construire\
  \ un simulateur de jeu de table multijoueur en utilisant Vue, Phaser, Node/Express et Socket.IO\
  \ pour apprendre..."
---

Par M. S. Farzan

Assembler toutes les pièces d'une application JavaScript full stack peut être une entreprise complexe.  

Dans ce tutoriel, nous allons construire un simulateur de jeu de table multijoueur en utilisant [Vue](https://vuejs.org/), [Phaser](http://phaser.io/), [Node](https://nodejs.org/)/[Express](https://expressjs.com/), et [Socket.IO](https://socket.io/) pour apprendre plusieurs concepts qui seront utiles dans n'importe quelle application full stack.

Vous pouvez suivre ce tutoriel vidéo également (1 heure 16 minutes de visionnage) :

%[https://youtu.be/laNi0fdF_DU]

Tous les fichiers du projet pour ce tutoriel sont disponibles sur [GitHub](https://github.com/sominator/tabletop-project).

## Aperçu du projet

Notre projet présentera une instance de jeu Phaser qui nous permettra de créer des jetons et des cartes à l'écran, et de les déplacer sur un plateau de jeu numérique.

L'instance Phaser sera enveloppée dans un composant Vue qui gérera des choses comme le chat multijoueur et les commandes. Ensemble, Phaser et Vue composeront notre front-end (désigné ici comme le "client"), et nous utiliserons Socket.IO pour communiquer avec d'autres joueurs et lier ensemble les parties front-end et back-end de notre application.

Le back-end (désigné ici comme le "serveur") sera un simple serveur Express qui reçoit les événements Socket.IO du client et agit en conséquence. L'ensemble de l'application s'exécutera sur Node comme runtime.

Vous n'avez pas besoin d'être un expert dans l'un des frameworks ci-dessus pour compléter ce projet, mais il serait bon d'avoir une solide fondation en JavaScript et HTML/CSS de base avant d'essayer de maîtriser les spécificités. Vous pouvez également suivre ma série sur [Apprendre JavaScript en créant des jeux de table numériques et des applications web](https://www.freecodecamp.org/news/learn-javascript-by-making-digital-tabletop-games-and-web-apps/).  

Vous voudrez également vous assurer d'avoir Node et [Git](https://github.com/) installés, ainsi que votre éditeur de code préféré et une interface de ligne de commande (vous pouvez suivre mon tutoriel sur la configuration d'un IDE [ici](https://www.freecodecamp.org/news/how-to-set-up-an-integrated-development-environment-ide/) si vous avez besoin d'aide).

Commençons !

## Partie 1 : Bases du client

Nous commencerons à construire notre client en installant le [Vue CLI](https://cli.vuejs.org/), qui nous aidera avec certains outils et nous permettra d'apporter des modifications à nos fichiers sans avoir à recharger notre navigateur web.

Dans une ligne de commande, tapez ce qui suit pour installer le Vue CLI globalement :

```cli
npm install -g @vue/cli
```

Naviguez vers un répertoire souhaité et créez un nouveau dossier pour notre projet :

```cli
mkdir tabletop-project
cd tabletop-project
```

Nous pouvons maintenant utiliser le Vue CLI pour créer un projet front-end pour nous :

```cli
vue create client
```

Vous pouvez simplement appuyer sur "entrée" aux prompts suivants, sauf si vous avez des préférences spécifiques.

Le Vue CLI a utilement créé un projet front-end pour nous, que nous pouvons voir dans notre éditeur de code :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1.JPG)

Naviguons vers notre nouveau dossier client dans notre CLI et exécutons l'application template :

```cli
cd client
npm run serve
```

Après un peu de travail, le Vue CLI devrait commencer à afficher notre application dans un navigateur web à l'adresse http://localhost:8080 par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/2.JPG)

Cool ! Nous avons la structure de base de notre client. Cassons-la en créant deux nouveaux composants dans le dossier /components, appelés Game.vue et Chat.vue (vous pouvez supprimer HelloWorld.vue et tout ce qui se trouve dans le dossier assets si vous êtes obsédé par la propreté comme je le suis).

Remplacez le code dans App.vue par ce qui suit :

```html
<template>
    <div id="app">
        <div id="game">
            <Game />
        </div>
        <div id="border" />
        <div id="input">
            <Chat />
        </div>
    </div>
</template>

<script>
    import Chat from './components/Chat.vue';
    import Game from './components/Game.vue';

    export default {
        name: 'App',
        components: {
            Chat,
            Game
        }
    }
</script>

<style>
    #app {
        font-family: 'Trebuchet MS';
        text-align: left;
        background-color: black;
        color: cyan;
        display: flex;
    }
    #game {
        width: 50vw;
        height: 100vh;
    }
    #input {
        width: 50vw;
        height: 100vh;
    }
    #border {
        border-right: 2px solid cyan;
    }
    @media (max-width: 1000px) {
        #app {
            flex-direction: column;
        }
        #game {
            width: 100vw;
            height: 50vh;
        }
        #input {
            width: 100vw;
            height: 50vh;
        }
    }
</style>

```

Comme vous pouvez le voir, un composant Vue a ordinairement trois sections : Template, Script et Style, qui contiennent respectivement tout HTML, JavaScript et CSS pour ce composant. Nous avons simplement importé nos composants Game et Chat ici et ajouté un peu de style pour lui donner un look cyberpunk lorsqu'il est en marche.

C'est en fait tout ce que nous devons faire pour configurer notre composant App.vue, qui abritera tout le reste dans notre client. Avant de pouvoir faire quoi que ce soit avec, nous devons faire fonctionner notre serveur !

## Partie 2 : Bases du serveur

À notre répertoire racine (tabletop-project, au-dessus de /client), initialisez un nouveau projet dans une nouvelle interface de ligne de commande en tapant :

```cli
npm init
```

Comme avec notre client, vous pouvez appuyer sur "entrée" aux prompts, sauf s'il y a des spécificités que vous aimeriez désigner à ce moment-là.

Nous devons installer Express et Socket.IO, ainsi que [Nodemon](https://nodemon.io/) pour surveiller nos fichiers serveur et redémarrer si nécessaire :

```cli
npm install --save express socket.io nodemon
```

Ouvrons le nouveau fichier package.json dans ce répertoire racine et ajoutons une commande "start" dans la section "scripts" :

```javascript
  "scripts": {
    "start": "nodemon server.js"
  },
```

Créez un nouveau fichier appelé server.js dans ce répertoire, et entrez le code suivant :

```javascript
const server = require('express')();
const http = require('http').createServer(server);
const io = require('socket.io')(http);

io.on('connection', function (socket) {
    console.log('Un utilisateur s\'est connecté : ' + socket.id);
    
    socket.on('send', function (text) {
        let newText = "<" + socket.id + "> " + text;
        io.emit('receive', newText);
    });

    socket.on('disconnect', function () {
        console.log('Un utilisateur s\'est déconnecté : ' + socket.id);
    });
});

http.listen(3000, function () {
    console.log('Serveur démarré !');
});
```

Excellent ! Notre serveur simple écoutera maintenant sur http://localhost:3000, et utilisera Socket.IO pour journaliser dans la console lorsqu'un utilisateur se connecte et se déconnecte, avec son ID de socket.

Lorsque le serveur reçoit un événement "send" d'un client, il créera une nouvelle chaîne de texte qui inclut l'ID de socket du client qui a émis l'événement, et émettra son propre événement "receive" à tous les clients avec le texte qu'il a reçu, interpolé avec l'ID de socket.

Nous pouvons tester le serveur en retournant à notre ligne de commande et en le démarrant :

```cli
npm run start
```

La console de commande devrait maintenant afficher :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/3-4.JPG)

Cool ! Retournez au composant Chat de notre client pour commencer à construire la fonctionnalité de notre front-end.

## Partie 3 : Chat

Ouvrons une interface de ligne de commande séparée et naviguons vers le répertoire /client. Dans ce répertoire, installez la version client de Socket.IO :

```cli
npm install --save socket.io-client
```

Dans /client/src/components/Chat.vue, ajoutez le code suivant :

```html
<template>
    <div id="container">
        <div id="output">
            <h1>STRUCT</h1>
            <p v-for="(text, index) in textOutput" :key="index">{{text}}</p>
        </div>
        <div id="input">
            <form>
                <input type="text" v-model="textInput" :placeholder="textInput" />
                <input type="submit" value="Envoyer" v-on:click="submitText" />
            </form>
        </div>
    </div>
</template>

<script>
    import io from 'socket.io-client';
    let socket = io('http://localhost:3000');

    export default {
        name: 'Chat',
        data: function () {
            return {
                textInput: null,
                textOutput: []
            }
        },
        methods: {
            submitText: function (event) {
                event.preventDefault();
                socket.emit('send', this.textInput);
            }
        },
        created: function () {
            socket.on('connect', () => {
                console.log('Connecté !');
            });
            socket.on('receive', (text) => {
                this.textOutput.push(text);
                this.textInput = null;
            });
        }
    }
</script>

<style scoped>
    #container {
        text-align: left;
        display: flex;
        flex-direction: column;
        margin-left: 1vw;
        min-height: 100vh;
    }
    h1 {
        text-align: center;
    }
    .hotpink {
        color: hotpink;
    }
    #input {
        position: fixed;
        margin-top: 95vh;
    }
    input[type=text] {
        height: 20px;
        width:  40vw;
        border: 2px solid cyan;
        background-color: black;
        color: hotpink;
        padding-left: 1em;
    }
    input[type=submit]{
        height: 25px;
        width: 5vw;
        background-color: black;
        color: cyan;
        border: 2px solid cyan;
        margin-right: 2vw;
    }
    input[type=submit]:focus{
        outline: none;
    }
    input[type=submit]:hover{
        color: hotpink;
    }
    @media (max-width: 1000px) {
        #container {
            border-left: none;
            border-top: 2px solid cyan;
            min-height: 50vh;
        }
        #input {
            margin-top: 43vh;
        }
        #output {
            margin-right: 10vw;
        }
        input[type=text] {
            width: 60vw;
        }
        input[type=submit] {
            min-width: 10vw;
        }
    }
</style>

```

Examinons ce qui précède de bas en haut avant de continuer. Entre les balises <style>, nous avons ajouté du CSS pour renforcer le côté cyberpunk de notre chat. Vous pouvez styliser cela comme vous le souhaitez !

Entre les balises <script>, nous avons importé la version client de Socket.IO et l'avons stockée dans une variable appelée "socket" qui communique via http://localhost:3000, où le serveur écoute.

Nous avons ensuite donné un nom au composant ("Chat"), et utilisé les objets data, methods et created que Vue utilise pour gérer l'interactivité pour nous.

Dans l'objet data, nous stockons deux variables : textInput, qui commence par null, et textOutput, qui est un tableau vide.

Dans l'objet methods, nous créons une fonction simple, submitText, qui émet un événement "send" via Socket.IO avec le textInput et empêche le comportement par défaut d'un tel événement (comme l'envoi de données via un formulaire HTML).

Dans l'objet created, qui est déclenché lorsque le composant est initialisé, nous avons deux références au socket. La première indique que lorsqu'il reçoit un événement "connect" du serveur, le socket doit journaliser dans la console qu'il est "Connecté !" La seconde indique que lorsque le socket reçoit un événement "receive", il doit pousser le texte de cet événement dans le tableau textOutput et effacer la variable textInput.

Entre nos balises <template>, nous avons notre HTML qui inclut les sections d'entrée et de sortie. La section de sortie a un en-tête nommé "Struct" (qui est le langage de programmation dans [mes livres et jeux](https://www.nightpathpub.com/entromancy)), et utilise le rendu de liste de Vue pour afficher un élément <p> pour chaque morceau de texte dans le tableau textOutput.

La section d'entrée a un formulaire simple avec des liaisons d'entrée de formulaire Vue et un gestionnaire d'événements pour recevoir l'entrée de texte, la stocker dans notre variable textInput et déclencher l'événement "send" Socket.IO lorsque le bouton "Envoyer" est cliqué.

Ouf ! Notre chat est maintenant fonctionnel. Enregistrez tout et naviguez vers votre onglet de navigateur qui exécute le client à l'adresse http://localhost:8080 :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/4.JPG)

Notez que vous pouvez ouvrir un autre onglet de navigateur, qui se connectera au serveur avec un nouvel ID de socket, et le chat devrait commencer à se remplir entre les deux clients :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/6.JPG)

Pendant ce temps, votre console de ligne de commande devrait également indiquer lorsque les clients se connectent et se déconnectent du serveur (avec des ID de socket différents, bien sûr) :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/5.JPG)

Super. Passons à la construction de notre simulateur de tabletop dans Phaser !

## Partie 4 : Simulateur de tabletop

Nous aurons besoin d'un composant Vue pour héberger notre instance Phaser, et pour ce faire, nous emprunterons à [Sun0fABeach](https://github.com/Sun0fABeach) le [Vue - Phaser 3 Webpack boilerplate](https://github.com/Sun0fABeach/vue-phaser3) (vous pourriez même utiliser ce boilerplate pour créer votre client si vous le souhaitez).

Dans notre fichier /client/src/components/Game.vue, ajoutez le code suivant :

```html
<template>
    <div :id="containerId" v-if="downloaded" />
    <div class="placeholder" v-else>
        Téléchargement...
    </div>
</template>

<script>
    export default {
        name: 'Game',
        data: function () {
            return {
                downloaded: false,
                gameInstance: null,
                containerId: 'game-container'
            }
        },
        async mounted() {
            const game = await import(../game/game');
            this.downloaded = true;
            this.$nextTick(() => {
                this.gameInstance = game.launch(this.containerId)
            })
        },
        destroyed() {
            this.gameInstance.destroy(false);
        }
    }
</script>

<style scoped>

</style>

```

Ce composant rendra notre instance de jeu lorsqu'elle sera prête, et gardera un espace réservé jusqu'à ce moment-là (généralement juste quelques secondes). Cela ne fonctionnera pas encore, car nous n'avons pas créé d'instance de jeu avec laquelle travailler.

Dans une interface de ligne de commande au répertoire /client, tapez ce qui suit :

```cli
npm install --save phaser
```

Phaser gérera le rendu de tous nos objets de jeu comme les jetons et les cartes, tout en les rendant interactifs avec la fonctionnalité de glisser-déposer.

Dans le dossier /client/src, ajoutez un nouveau dossier appelé "game", et un sous-dossier dans ce dossier appelé "scenes".

Dans le dossier /client/src/game, ajoutez un fichier appelé game.js, et dans /client/src/game/scenes, ajoutez un fichier appelé gamescene.js. Votre structure de fichiers devrait maintenant ressembler à :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/7.JPG)

Notre fichier game.js gérera la configuration initiale de notre instance Phaser, important notre gamescene.js et lançant notre jeu dans le containerId de notre composant Vue (il met également à l'échelle l'instance à la taille du conteneur). Voici à quoi il devrait ressembler :

```javascript
import Phaser from "phaser";
import GameScene from "./scenes/gamescene";


function launch(containerId) {
    return new Phaser.Game({
        type: Phaser.AUTO,
        parent: containerId,
        scene: [
            GameScene
        ],
        scale: {
            mode: Phaser.Scale.FIT,
            width: '100%',
            height: '100%'
        }
    });
}

export default launch;
export { launch }
```

La fonctionnalité principale de notre simulateur sera dans le fichier gamescene.js, où nous écrirons :

```javascript
import Phaser from 'phaser';
import io from 'socket.io-client';

export default class GameScene extends Phaser.Scene {
    constructor() {
        super({
            key: 'GameScene'
        });
    }

    preload() {
        
    }

    create() {
        this.socket = io('http://localhost:3000');
        
        this.socket.on('struct create', (width, height) => {
            let token = this.add.rectangle(300, 300, width, height, 0x00ffff).setInteractive();
            this.input.setDraggable(token);
        });
        
        this.input.on('drag', (pointer, gameObject, dragX, dragY) => {
            gameObject.x = dragX;
            gameObject.y = dragY;
        });
    }

    update() {

    }
}
```

Notre architecture Phaser utilise des [classes](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes) JavaScript pour créer des [scènes](https://photonstorm.github.io/phaser3-docs/Phaser.Scene.html), et possède trois fonctions principales : preload, create et update.

La fonction preload est utilisée pour préparer des assets comme des sprites pour une utilisation dans une scène.

La fonction update est appelée une fois par frame, et nous ne l'utilisons pas dans notre projet.

La fonction create est appelée lorsqu'une scène est créée, et c'est là que tout notre travail est effectué. Nous initialisons une variable socket et y stockons la connexion Socket.IO à http://localhost:3000, puis nous référençons un événement "struct create" que nous attendons de recevoir du serveur.

Lorsque le client reçoit un événement "struct create", notre instance Phaser doit créer un rectangle aux coordonnées (x, y) de (300, 300), en utilisant les paramètres de largeur et de hauteur désignés par cet événement, et une couleur cyberpunk amusante que nous avons choisie. Phaser rendra ensuite ce rectangle interactif et alertera le système d'entrée qu'il doit également être glissable.

Nous avons également écrit un peu de logique qui indique à Phaser ce qu'il doit faire lorsque le rectangle est glissé ; à savoir, il doit suivre la direction du pointeur de la souris.

Tout ce que nous avons à faire maintenant est de revenir à notre server.js et d'ajouter la logique pour notre événement "struct create" :

```javascript
const server = require('express')();
const http = require('http').createServer(server);
const io = require('socket.io')(http);

io.on('connection', function (socket) {
    console.log('Un utilisateur s\'est connecté : ' + socket.id);
    
    socket.on('send', function (text) {
        let newText = "<" + socket.id + "> " + text;
        if (text === 'struct card') {
            io.emit('struct create', 130, 180)
        };
        if (text === 'struct token') {
            io.emit('struct create', 100, 100)
        };
        io.emit('receive', newText);
    });

    socket.on('disconnect', function () {
        console.log('Un utilisateur s\'est déconnecté : ' + socket.id);
    });
});

http.listen(3000, function () {
    console.log('Serveur démarré !');
});
```

Notre serveur agit maintenant comme un simple analyseur lorsqu'il reçoit un événement "send" d'un client. Si le client envoie le texte "struct card", le serveur émettra notre événement "struct create", avec des arguments de 130 x 180 pixels pour la largeur et la hauteur d'une carte.

Si le client envoie le texte "struct token", le serveur émettra plutôt notre événement "struct create" avec des arguments de 100 x 100 pixels pour la largeur et la hauteur d'un jeton.

Essayez ! Enregistrez tout, assurez-vous que le serveur est en cours d'exécution, et ouvrez quelques onglets dans un navigateur web pointant vers http://localhost:8080. Lorsque vous discutez dans un onglet, cela devrait apparaître dans l'autre avec l'ID de socket de votre client, et vice versa. 

Si votre chat est la commande "struct card" ou "struct token", une carte ou un jeton glissable, respectivement, devrait apparaître dans les deux clients.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/8.JPG)

Sympa !

## Conclusion

En suivant ce tutoriel, vous devriez maintenant avoir un simulateur de jeu de table multijoueur fonctionnel avec chat, création de cartes et de jetons, et fonctionnalité de glisser-déposer.

Vous pouvez continuer à construire cette application full stack simple en améliorant le style, en ajoutant une barre de défilement au chat, ou en permettant aux joueurs de choisir des noms d'utilisateur et de se connecter à des instances de chat spécifiques en utilisant les [Socket.IO rooms](https://socket.io/docs/rooms/).

Vous pouvez améliorer la fonctionnalité du jeu de société en distribuant plusieurs cartes et jetons à la fois, ou en vous familiarisant avec les [exemples Phaser](http://phaser.io/examples) pour ajouter vos propres fonctionnalités. Vous pouvez également suivre mon tutoriel sur [Comment construire un jeu de cartes multijoueur avec Phaser 3, Express et Socket.IO](https://www.freecodecamp.org/news/how-to-build-a-multiplayer-card-game-with-phaser-3-express-and-socket-io/) pour vous inspirer. 

Bien sûr, il n'y a aucune raison pour que vous deviez utiliser des commandes de chat pour créer des objets de jeu. Vous pourriez tout faire cela depuis l'instance Phaser si vous le souhaitez, mais vous devrez créer vos propres boutons ou une autre interactivité d'entrée (selon mon expérience, Vue est bien meilleur pour gérer le texte, d'où nos commandes de chat). 

La fonctionnalité actuelle pourrait cependant être utile dans le cas où vous voudriez pouvoir rendre, par exemple, des dés à l'écran en exécutant une commande de chat.

De plus, si vous souhaitez déployer votre nouvelle application, vous pouvez d'abord lire mon article sur [Trois choses à considérer avant de déployer votre première application full stack](https://www.freecodecamp.org/news/3-things-to-consider-before-deploying-your-first-full-stack-app/), puis suivre mon tutoriel pour [Apprendre à déployer une application web full stack avec Heroku](https://www.freecodecamp.org/news/how-to-deploy-a-full-stack-web-app-with-heroku/).

Bon codage !

Si vous avez aimé cet article, veuillez envisager de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer en chef de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](https://twitter.com/sominator).