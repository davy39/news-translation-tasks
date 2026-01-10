---
title: Comment créer un jeu de cartes multijoueur avec Phaser 3, Express et Socket.IO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-25T20:57:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-multiplayer-card-game-with-phaser-3-express-and-socket-io
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Client-2-2.PNG
tags:
- name: ES6
  slug: es6
- name: Express
  slug: express
- name: Express JS
  slug: express-js
- name: Express.js
  slug: expressjs
- name: Game Development
  slug: game-development
- name: GameDev
  slug: gamedev
- name: JavaScript
  slug: javascript
- name: phaser 3
  slug: phaser-3
- name: SocketIO
  slug: socketio
seo_title: Comment créer un jeu de cartes multijoueur avec Phaser 3, Express et Socket.IO
seo_desc: 'By M. S. Farzan

  I''m a tabletop game developer, and am continually looking for ways to digitize
  game experiences.  In this tutorial, we''re going to build a multiplayer card game
  using Phaser 3, Express, and Socket.IO.

  In terms of prerequisites, you''ll...'
---

Par M. S. Farzan

Je suis un développeur de [jeux de société](https://www.nightpathpub.com/entromancy) et je cherche constamment des moyens de numériser les expériences de jeu. Dans ce tutoriel, nous allons créer un jeu de cartes multijoueur en utilisant [Phaser 3](http://phaser.io/), [Express](https://expressjs.com/), et [Socket.IO](https://socket.io/).

En termes de prérequis, assurez-vous d'avoir [Node](https://nodejs.org/en/)/[NPM](https://www.npmjs.com/) et [Git](https://github.com/) installés et configurés sur votre machine. Une certaine expérience avec JavaScript serait utile, et vous pourriez vouloir suivre le [tutoriel de base de Phaser](http://phaser.io/tutorials/making-your-first-phaser-3-game) avant de vous attaquer à celui-ci.

Un grand merci à Scott Westover pour [son tutoriel sur le sujet](https://gamedevacademy.org/create-a-basic-multiplayer-game-in-phaser-3-with-socket-io-part-1/), à Kal_Torak et à la communauté Phaser pour avoir répondu à toutes mes questions, et à mon bon ami Mike pour m'avoir aidé à conceptualiser l'architecture de ce projet.

Note : nous allons utiliser des actifs et des couleurs de mon jeu de cartes de société, _[Entromancy: Hacker Battles](https://www.nightpathpub.com/hacker-battles)_. Si vous préférez, vous pouvez utiliser vos propres images (ou même des [rectangles Phaser](http://phaser.io/examples/v3/view/game-objects/shapes/rectangle)) et des couleurs, et vous pouvez accéder à l'ensemble du code du projet sur [GitHub](https://github.com/sominator/multiplayer-card-project).

Si vous préférez un tutoriel plus visuel, vous pouvez également suivre la vidéo accompagnant cet article :

%[https://youtu.be/fEwAgKBgoJM]

Commençons !

## Le Jeu

Notre simple jeu de cartes présentera un client Phaser qui gérera la plupart de la logique du jeu et fera des choses comme distribuer des cartes, fournir une fonctionnalité de glisser-déposer, et ainsi de suite.

Côté serveur, nous allons lancer un serveur Express qui utilisera Socket.IO pour communiquer entre les clients et faire en sorte que lorsqu'un joueur joue une carte, elle apparaisse dans le client d'un autre joueur, et vice-versa.

Notre objectif pour ce projet est de créer un cadre de base pour un jeu de cartes multijoueur que vous pouvez développer et ajuster pour répondre à la logique de votre propre jeu.

Commençons par le client !

## Le Client

Pour échafauder notre client, nous allons cloner le modèle de projet Phaser 3 Webpack semi-officiel sur [GitHub](https://github.com/photonstorm/phaser3-project-template).

Ouvrez votre interface de ligne de commande préférée et créez un nouveau dossier :

```cli
mkdir multiplayer-card-project
cd multiplayer-card-project
```

Clonez le projet git :

```cli
git clone https://github.com/photonstorm/phaser3-project-template.git
```

Cette commande téléchargera le modèle dans un dossier appelé "phaser3-project-template" dans /multiplayer-card-project. Si vous souhaitez suivre la structure de fichiers de notre tutoriel, allez-y et changez le nom de ce dossier de modèle en "client".

Naviguez dans ce nouveau répertoire et installez toutes les dépendances :

```cli
cd client
npm install
```

Votre structure de dossier de projet devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/File-Structure-1-4.PNG)

Avant de modifier les fichiers, revenons à notre CLI et entrons la commande suivante dans le dossier /client :

```cli
npm start
```

Notre modèle Phaser utilise Webpack pour lancer un serveur local qui sert une simple application de jeu dans notre navigateur (généralement à http://localhost:8080). Super !

Ouvrons notre projet dans votre éditeur de code préféré et apportons quelques modifications pour l'adapter à notre jeu de cartes. Supprimez tout dans /client/src/assets et remplacez-les par les images de cartes de [GitHub](https://github.com/sominator/multiplayer-card-project/tree/master/client/src/assets).

Dans le répertoire /client/src, ajoutez un dossier appelé "scenes" et un autre appelé "helpers".

Dans /client/src/scenes, ajoutez un fichier vide appelé "game.js".

Dans /client/src/helpers, ajoutez trois fichiers vides : "card.js", "dealer.js", et "zone.js".

Votre structure de projet devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/File-Structure-2.PNG)

Cool ! Votre client pourrait vous donner des erreurs parce que nous avons supprimé certaines choses, mais ne vous inquiétez pas. Ouvrez /src/index.js, qui est le point d'entrée principal de notre application front-end. Entrez le code suivant :

```javascript
import Phaser from "phaser";
import Game from "./scenes/game";

const config = {
    type: Phaser.AUTO,
    parent: "phaser-example",
    width: 1280,
    height: 780,
    scene: [
        Game
    ]
};

const game = new Phaser.Game(config);
```

Tout ce que nous avons fait ici est de restructurer le code standard pour utiliser le système de "scène" de Phaser afin que nous puissions séparer nos scènes de jeu plutôt que d'essayer de tout entasser dans un seul fichier. Les scènes peuvent être utiles si vous créez plusieurs mondes de jeu, construisez des choses comme des écrans d'instructions, ou essayez généralement de garder les choses bien organisées.

Passons à /src/scenes/game.js et écrivons un peu de code :

```javascript
export default class Game extends Phaser.Scene {
    constructor() {
        super({
            key: 'Game'
        });
    }

    preload() {
        this.load.image('cyanCardFront', 'src/assets/CyanCardFront.png');
        this.load.image('cyanCardBack', 'src/assets/CyanCardBack.png');
        this.load.image('magentaCardFront', 'src/assets/MagentaCardFront.png');
        this.load.image('magentaCardBack', 'src/assets/MagentaCardBack.png');
    }

    create() {
        this.dealText = this.add.text(75, 350, ['DEAL CARDS']).setFontSize(18).setFontFamily('Trebuchet MS').setColor('#00ffff').setInteractive();
    }
    
    update() {
    
    }
}
```

Nous utilisons les [classes ES6](https://www.freecodecamp.org/news/how-to-use-github-and-es6-features-to-create-and-structure-your-code/) pour créer une nouvelle scène de jeu, qui incorpore les fonctions preload(), create() et update().

preload() est utilisé pour... bien... précharger tous les actifs que nous utiliserons pour notre jeu.

create() est exécuté lorsque le jeu démarre, et c'est là que nous établirons une grande partie de notre interface utilisateur et de la logique du jeu.

update() est appelé une fois par frame, et nous ne l'utiliserons pas dans notre tutoriel (mais il peut être utile dans votre propre jeu en fonction de ses exigences).

Dans la fonction create(), nous avons créé un peu de texte qui dit "DEAL CARDS" et l'avons rendu interactif :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Deal-Cards.PNG)

Très cool. Créons un peu de code de remplissage pour comprendre comment nous voulons que tout cela fonctionne une fois qu'il est opérationnel. Ajoutez ce qui suit à votre fonction create() :

```javascript
		let self = this;

		this.card = this.add.image(300, 300, 'cyanCardFront').setScale(0.3, 0.3).setInteractive();
        this.input.setDraggable(this.card);

		this.dealCards = () => {
        
        }

		this.dealText.on('pointerdown', function () {
            self.dealCards();
        })

        this.dealText.on('pointerover', function () {
            self.dealText.setColor('#ff69b4');
        })

        this.dealText.on('pointerout', function () {
            self.dealText.setColor('#00ffff');
        })

        this.input.on('drag', function (pointer, gameObject, dragX, dragY) {
            gameObject.x = dragX;
            gameObject.y = dragY;
        })
```

Nous avons ajouté beaucoup de structure, mais il ne s'est pas passé grand-chose. Maintenant, lorsque notre souris survole le texte "DEAL CARDS", il est mis en évidence en rose cyberpunk, et il y a une carte aléatoire sur notre écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Card.PNG)

Nous avons placé l'image aux coordonnées (x, y) (300, 300), défini son échelle pour qu'elle soit un peu plus petite, et l'avons rendue interactive et glissable. Nous avons également ajouté un peu de logique pour déterminer ce qui devrait se passer lorsqu'elle est glissée : elle devrait suivre les coordonnées (x, y) de notre souris.

Nous avons également créé une fonction dealCards() vide qui sera appelée lorsque nous cliquons sur notre texte "DEAL CARDS". De plus, nous avons sauvegardé "this" - c'est-à-dire la scène dans laquelle nous travaillons actuellement - dans une variable appelée "self" afin que nous puissions l'utiliser dans toutes nos fonctions sans nous soucier de la portée.

Notre scène de jeu va devenir désordonnée rapidement si nous ne commençons pas à déplacer les choses, alors supprimons le bloc de code qui commence par "this.card" et passons à /src/helpers/card.js pour écrire :

```javascript
export default class Card {
    constructor(scene) {
        this.render = (x, y, sprite) => {
            let card = scene.add.image(x, y, sprite).setScale(0.3, 0.3).setInteractive();
            scene.input.setDraggable(card);
            return card;
        }
    }
}
```

Nous avons créé une nouvelle classe qui accepte une scène comme paramètre, et qui possède une fonction render() qui accepte les coordonnées (x, y) et un sprite. Maintenant, nous pouvons appeler cette fonction depuis ailleurs et lui passer les paramètres nécessaires pour créer des cartes.

Importons la carte en haut de notre scène de jeu :

```javascript
import Card from '../helpers/card';
```

Et entrez le code suivant dans notre fonction dealCards() vide :

```javascript
		this.dealCards = () => {
        	for (let i = 0; i < 5; i++) {
                let playerCard = new Card(this);
                playerCard.render(475 + (i * 100), 650, 'cyanCardFront');
            }
    	}
```

Lorsque nous cliquons sur le bouton "DEAL CARDS", nous parcourons une boucle for qui crée des cartes et les affiche séquentiellement à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Cards.PNG)

GÉNIAL. Nous pouvons faire glisser ces cartes autour de l'écran, mais il pourrait être agréable de limiter où elles peuvent être déposées pour soutenir notre logique de jeu.

Passons à /src/helpers/zone.js et ajoutons une nouvelle classe :

```javascript
export default class Zone {
    constructor(scene) {
        this.renderZone = () => {
            let dropZone = scene.add.zone(700, 375, 900, 250).setRectangleDropZone(900, 250);
            dropZone.setData({ cards: 0 });
            return dropZone;
        };
        this.renderOutline = (dropZone) => {
            let dropZoneOutline = scene.add.graphics();
            dropZoneOutline.lineStyle(4, 0xff69b4);
            dropZoneOutline.strokeRect(dropZone.x - dropZone.input.hitArea.width / 2, dropZone.y - dropZone.input.hitArea.height / 2, dropZone.input.hitArea.width, dropZone.input.hitArea.height)
        }
    }
}
```

Phaser a des zones de dépôt intégrées qui nous permettent de dicter où les objets de jeu peuvent être déposés, et nous en avons configuré une ici et lui avons fourni un contour. Nous avons également ajouté une petite donnée appelée "cards" à la zone de dépôt que nous utiliserons plus tard.

Importons notre nouvelle zone dans la scène de jeu :

```javascript
import Zone from '../helpers/zone';
```

Et appelons-la dans la fonction create() :

```javascript
        this.zone = new Zone(this);
        this.dropZone = this.zone.renderZone();
        this.outline = this.zone.renderOutline(this.dropZone);
```

Pas mal du tout !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Zone.PNG)

Nous devons ajouter un peu de logique pour déterminer comment les cartes doivent être déposées dans la zone. Faisons cela sous la fonction "this.input.on('drag')" :

```javascript
        this.input.on('dragstart', function (pointer, gameObject) {
            gameObject.setTint(0xff69b4);
            self.children.bringToTop(gameObject);
        })

        this.input.on('dragend', function (pointer, gameObject, dropped) {
            gameObject.setTint();
            if (!dropped) {
                gameObject.x = gameObject.input.dragStartX;
                gameObject.y = gameObject.input.dragStartY;
            }
        })

        this.input.on('drop', function (pointer, gameObject, dropZone) {
            dropZone.data.values.cards++;
            gameObject.x = (dropZone.x - 350) + (dropZone.data.values.cards * 50);
            gameObject.y = dropZone.y;
            gameObject.disableInteractive();
        })
```

En commençant par le bas du code, lorsqu'une carte est déposée, nous incrémentons la valeur de données "cards" sur la zone de dépôt, et nous attribuons les coordonnées (x, y) de la carte à la zone de dépôt en fonction du nombre de cartes déjà présentes. Nous désactivons également l'interactivité sur les cartes après qu'elles aient été déposées afin qu'elles ne puissent pas être rétractées :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Zone-Dropped.PNG)

Nous avons également fait en sorte que nos cartes aient une teinte différente lorsqu'elles sont glissées, et si elles ne sont pas déposées sur la zone de dépôt, elles retourneront à leurs positions de départ.

Bien que notre client ne soit pas tout à fait complet, nous avons fait tout ce que nous pouvons avant d'implémenter le backend. Nous pouvons maintenant distribuer des cartes, les faire glisser à l'écran et les déposer dans une zone de dépôt. Mais pour avancer, nous devrons configurer un serveur capable de coordonner notre fonctionnalité multijoueur.

## Le Serveur

Ouvrons une nouvelle ligne de commande dans notre répertoire racine (au-dessus de /client) et tapons :

```cli
npm init
npm install --save express socket.io nodemon
```

Nous avons initialisé un nouveau package.json et installé Express, Socket.IO et [Nodemon](https://nodemon.io/) (qui surveillera notre serveur et le redémarrera en cas de changements).

Dans notre éditeur de code, modifions la section "scripts" de notre package.json pour qu'elle dise :

```javascript
  "scripts": {
    "start": "nodemon server.js"
  },
```

Excellent. Nous sommes prêts à assembler notre serveur ! Créez un fichier vide appelé "server.js" dans notre répertoire racine et entrez le code suivant :

```javascript
const server = require('express')();
const http = require('http').createServer(server);
const io = require('socket.io')(http);

io.on('connection', function (socket) {
    console.log('Un utilisateur s\'est connecté : ' + socket.id);

    socket.on('disconnect', function () {
        console.log('Un utilisateur s\'est déconnecté : ' + socket.id);
    });
});

http.listen(3000, function () {
    console.log('Serveur démarré !');
});
```

Nous importons Express et Socket.IO, et demandons au serveur d'écouter sur le port 3000. Lorsqu'un client se connecte ou se déconnecte de ce port, nous enregistrons l'événement dans la console avec l'ID de socket du client.

Ouvrez une nouvelle interface de ligne de commande et démarrez le serveur :

```cli
npm run start
```

Notre serveur devrait maintenant fonctionner sur localhost:3000, et Nodemon surveillera nos fichiers backend pour tout changement. Il ne se passera pas grand-chose d'autre à part le journal de la console indiquant que le "Serveur démarré !"

Dans notre autre interface de ligne de commande ouverte, naviguons vers notre répertoire /client et installons la version client de Socket.IO :

```cli
cd client
npm install --save socket.io-client
```

Nous pouvons maintenant l'importer dans notre scène de jeu :

```javascript
import io from 'socket.io-client';
```

Super ! Nous avons presque connecté nos fronts et backs ends. Tout ce que nous avons à faire est d'écrire un peu de code dans la fonction create() :

```javascript
		this.socket = io('http://localhost:3000');

        this.socket.on('connect', function () {
        	console.log('Connecté !');
        });

```

Nous initialisons une nouvelle variable "socket" qui pointe vers notre port local 3000 et enregistre dans la console du navigateur lors de la connexion.

Ouvrez et fermez quelques navigateurs à l'adresse http://localhost:8080 (où notre client Phaser est servi) et vous devriez voir ce qui suit dans votre interface de ligne de commande :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Console.PNG)

YES. Commençons à ajouter de la logique à notre fichier server.js qui répondra aux besoins de notre jeu de cartes. Remplacez le code existant par ce qui suit :

```javascript
const server = require('express')();
const http = require('http').createServer(server);
const io = require('socket.io')(http);
let players = [];

io.on('connection', function (socket) {
    console.log('Un utilisateur s\'est connecté : ' + socket.id);

    players.push(socket.id);

    if (players.length === 1) {
        io.emit('isPlayerA');
    };

    socket.on('dealCards', function () {
        io.emit('dealCards');
    });

    socket.on('cardPlayed', function (gameObject, isPlayerA) {
        io.emit('cardPlayed', gameObject, isPlayerA);
    });

    socket.on('disconnect', function () {
        console.log('Un utilisateur s\'est déconnecté : ' + socket.id);
        players = players.filter(player => player !== socket.id);
    });
});

http.listen(3000, function () {
    console.log('Serveur démarré !');
});
```

Nous avons initialisé un tableau vide appelé "players" et ajoutons un identifiant de socket chaque fois qu'un client se connecte au serveur, tout en supprimant l'identifiant de socket lors de la déconnexion.

Si un client est le premier à se connecter au serveur, nous demandons à Socket.IO d'"[émettre](https://socket.io/get-started/chat/#Emitting-events)" un événement indiquant qu'il sera le Joueur A. Par la suite, lorsque le serveur reçoit un événement appelé "dealCards" ou "cardPlayed", il doit émettre en retour aux clients qu'ils doivent se mettre à jour en conséquence.

Croyez-le ou non, c'est tout le code dont nous avons besoin pour faire fonctionner notre serveur ! Tournons notre attention vers la scène de jeu. Tout en haut de la fonction create(), tapez ce qui suit :

```javascript
		this.isPlayerA = false;
        this.opponentCards = [];
```

Sous le bloc de code qui commence par "this.socket.on(connect)", écrivez :

```javascript
		this.socket.on('isPlayerA', function () {
        	self.isPlayerA = true;
        })
```

Maintenant, si notre client est le premier à se connecter au serveur, le serveur émettra un événement qui indique au client qu'il sera le Joueur A. Le socket client reçoit cet événement et transforme notre booléen "isPlayerA" de faux en vrai.

Note : à partir de ce point, vous devrez peut-être recharger la page de votre navigateur (réglée sur http://localhost:8080), plutôt que de laisser Webpack le faire automatiquement pour vous, afin que le client se déconnecte correctement du serveur et s'y reconnecte.

Nous devons reconfigurer notre logique dealCards() pour supporter l'aspect multijoueur de notre jeu, étant donné que nous voulons que le client nous distribue un certain ensemble de cartes qui peuvent être différentes de celles de notre adversaire. De plus, nous voulons afficher les dos des cartes de notre adversaire sur notre écran, et vice versa.

Nous allons nous rendre dans le fichier vide /src/helpers/dealer.js, importer card.js, et créer une nouvelle classe :

```javascript
import Card from './card';

export default class Dealer {
    constructor(scene) {
        this.dealCards = () => {
            let playerSprite;
            let opponentSprite;
            if (scene.isPlayerA) {
                playerSprite = 'cyanCardFront';
                opponentSprite = 'magentaCardBack';
            } else {
                playerSprite = 'magentaCardFront';
                opponentSprite = 'cyanCardBack';
            };
            for (let i = 0; i < 5; i++) {
                let playerCard = new Card(scene);
                playerCard.render(475 + (i * 100), 650, playerSprite);

                let opponentCard = new Card(scene);
                scene.opponentCards.push(opponentCard.render(475 + (i * 100), 125, opponentSprite).disableInteractive());
            }
        }
    }
}
```

Avec cette nouvelle classe, nous vérifions si le client est le Joueur A, et déterminons quels sprites doivent être utilisés dans chaque cas.

Ensuite, nous distribuons des cartes à notre client, tout en affichant les dos des cartes de notre adversaire en haut de l'écran et en les ajoutant au tableau opponentCards que nous avons initialisé dans notre scène de jeu.

Dans /src/scenes/game.js, importons le Dealer :

```javascript
import Dealer from '../helpers/dealer';
```

Puis remplaçons notre fonction dealCards() par :

```javascript
		this.dealer = new Dealer(this);
```

Sous le bloc de code qui commence par "this.socket.on('isPlayerA')", ajoutez ce qui suit :

```javascript
		this.socket.on('dealCards', function () {
            self.dealer.dealCards();
            self.dealText.disableInteractive();
        })
```

Nous devons également mettre à jour notre fonction dealText pour correspondre à ces changements :

```javascript
        this.dealText.on('pointerdown', function () {
            self.socket.emit("dealCards");
        })
```

Ouf ! Nous avons créé une nouvelle classe Dealer qui gérera la distribution des cartes à nous et l'affichage des cartes de notre adversaire à l'écran. Lorsque le socket client reçoit l'événement "dealcards" du serveur, il appellera la fonction dealCards() de cette nouvelle classe, et désactivera le dealText afin que nous ne puissions pas simplement continuer à générer des cartes sans raison.

Enfin, nous avons changé la fonctionnalité de dealText afin que, lorsqu'elle est pressée, le client émet un événement au serveur indiquant que nous voulons distribuer des cartes, ce qui relie tout ensemble.

Lancez deux navigateurs séparés pointant vers http://localhost:8080 et appuyez sur "DEAL CARDS" sur l'un d'eux. Vous devriez voir différents sprites sur chaque écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Client-1.PNG)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Client-2.PNG)

Notez à nouveau que si vous avez des problèmes avec cette étape, vous devrez peut-être fermer l'un de vos navigateurs et recharger le premier pour vous assurer que les deux clients se sont déconnectés du serveur, ce qui devrait être enregistré dans la console de votre ligne de commande.

Nous devons encore déterminer comment afficher nos cartes déposées dans le client de notre adversaire, et vice-versa. Nous pouvons faire tout cela dans notre scène de jeu ! Mettez à jour le bloc de code qui commence par "this.input.on('drop')" avec une ligne à la fin :

```javascript
        this.input.on('drop', function (pointer, gameObject, dropZone) {
            dropZone.data.values.cards++;
            gameObject.x = (dropZone.x - 350) + (dropZone.data.values.cards * 50);
            gameObject.y = dropZone.y;
            gameObject.disableInteractive();
            self.socket.emit('cardPlayed', gameObject, self.isPlayerA);
        })
```

Lorsque une carte est déposée dans notre client, le socket émettra un événement appelé "cardPlayed", passant les détails de l'objet de jeu et le booléen isPlayerA du client (qui peut être vrai ou faux, selon que le client a été le premier à se connecter au serveur).

Rappelons que, dans notre code serveur, Socket.IO reçoit simplement l'événement "cardPlayed" et émet le même événement vers tous les clients, passant les mêmes informations sur l'objet de jeu et isPlayerA du client qui a initié l'événement.

Écrivons ce qui devrait se passer lorsqu'un client reçoit un événement "cardPlayed" du serveur, sous le bloc de code "this.socket.on('dealCards')" :

```javascript
 		this.socket.on('cardPlayed', function (gameObject, isPlayerA) {
            if (isPlayerA !== self.isPlayerA) {
                let sprite = gameObject.textureKey;
                self.opponentCards.shift().destroy();
                self.dropZone.data.values.cards++;
                let card = new Card(self);
                card.render(((self.dropZone.x - 350) + (self.dropZone.data.values.cards * 50)), (self.dropZone.y), sprite).disableInteractive();
            }
        })
```

Le bloc de code compare d'abord le booléen isPlayerA qu'il reçoit du serveur avec le propre isPlayerA du client, ce qui est une vérification pour déterminer si le client qui reçoit l'événement est le même que celui qui l'a généré.

Réfléchissons un peu plus à cela, car cela expose un composant clé de la manière dont notre relation client-serveur fonctionne, en utilisant Socket.IO comme connecteur.

Supposons que le Client A se connecte d'abord au serveur et est informé par l'événement "isPlayerA" qu'il doit changer son booléen isPlayerA en **vrai**. Cela déterminera le type de cartes qu'il génère lorsqu'un utilisateur clique sur "DEAL CARDS" via ce client.

Si le Client B se connecte au serveur en second, il n'est jamais invité à modifier son booléen isPlayerA, qui reste **faux**. Cela déterminera également le type de cartes qu'il génère.

Lorsque le Client A dépose une carte, il émet un événement "cardPlayed" au serveur, passant des informations sur la carte qui a été déposée, et son booléen isPlayerA, qui est **vrai**. Le serveur relaie ensuite toutes ces informations à tous les clients avec son propre événement "cardPlayed".

Le Client A reçoit cet événement du serveur et note que le booléen isPlayerA du serveur est **vrai**, ce qui signifie que l'événement a été généré par le Client A lui-même. Rien de spécial ne se produit.

Le Client B reçoit le même événement du serveur et note que le booléen isPlayerA du serveur est **vrai**, bien que le propre isPlayerA du Client B soit **faux**. En raison de cette différence, il exécute le reste du bloc de code.

Le code qui suit stocke la "texturekey" - essentiellement, l'image - de l'objet de jeu qu'il reçoit du serveur dans une variable appelée "sprite". Il détruit l'un des dos de carte de l'adversaire qui sont rendus en haut de l'écran, et incrémente la valeur de données "cards" dans la zone de dépôt afin que nous puissions continuer à placer des cartes de gauche à droite.

Le code génère ensuite une nouvelle carte dans la zone de dépôt qui utilise la variable sprite pour créer la même carte qui a été déposée dans l'autre client (si vous aviez des données attachées à cet objet de jeu, vous pourriez utiliser une approche similaire pour les attacher ici également).

Votre code final /src/scenes/game.js devrait ressembler à ceci :

```javascript
import io from 'socket.io-client';
import Card from '../helpers/card';
import Dealer from "../helpers/dealer";
import Zone from '../helpers/zone';

export default class Game extends Phaser.Scene {
    constructor() {
        super({
            key: 'Game'
        });
    }

    preload() {
        this.load.image('cyanCardFront', 'src/assets/CyanCardFront.png');
        this.load.image('cyanCardBack', 'src/assets/CyanCardBack.png');
        this.load.image('magentaCardFront', 'src/assets/magentaCardFront.png');
        this.load.image('magentaCardBack', 'src/assets/magentaCardBack.png');
    }

    create() {
        this.isPlayerA = false;
        this.opponentCards = [];

        this.zone = new Zone(this);
        this.dropZone = this.zone.renderZone();
        this.outline = this.zone.renderOutline(this.dropZone);

        this.dealer = new Dealer(this);

        let self = this;

        this.socket = io('http://localhost:3000');

        this.socket.on('connect', function () {
            console.log('Connecté !');
        });

        this.socket.on('isPlayerA', function () {
            self.isPlayerA = true;
        })

        this.socket.on('dealCards', function () {
            self.dealer.dealCards();
            self.dealText.disableInteractive();
        })

        this.socket.on('cardPlayed', function (gameObject, isPlayerA) {
            if (isPlayerA !== self.isPlayerA) {
                let sprite = gameObject.textureKey;
                self.opponentCards.shift().destroy();
                self.dropZone.data.values.cards++;
                let card = new Card(self);
                card.render(((self.dropZone.x - 350) + (self.dropZone.data.values.cards * 50)), (self.dropZone.y), sprite).disableInteractive();
            }
        })

        this.dealText = this.add.text(75, 350, ['DEAL CARDS']).setFontSize(18).setFontFamily('Trebuchet MS').setColor('#00ffff').setInteractive();

        this.dealText.on('pointerdown', function () {
            self.socket.emit("dealCards");
        })

        this.dealText.on('pointerover', function () {
            self.dealText.setColor('#ff69b4');
        })

        this.dealText.on('pointerout', function () {
            self.dealText.setColor('#00ffff');
        })

        this.input.on('drag', function (pointer, gameObject, dragX, dragY) {
            gameObject.x = dragX;
            gameObject.y = dragY;
        })

        this.input.on('dragstart', function (pointer, gameObject) {
            gameObject.setTint(0xff69b4);
            self.children.bringToTop(gameObject);
        })

        this.input.on('dragend', function (pointer, gameObject, dropped) {
            gameObject.setTint();
            if (!dropped) {
                gameObject.x = gameObject.input.dragStartX;
                gameObject.y = gameObject.input.dragStartY;
            }
        })

        this.input.on('drop', function (pointer, gameObject, dropZone) {
            dropZone.data.values.cards++;
            gameObject.x = (dropZone.x - 350) + (dropZone.data.values.cards * 50);
            gameObject.y = dropZone.y;
            gameObject.disableInteractive();
            self.socket.emit('cardPlayed', gameObject, self.isPlayerA);
        })
    }

    update() {

    }
}
```

Enregistrez tout, ouvrez deux navigateurs et cliquez sur "DEAL CARDS". Lorsque vous faites glisser et déposez une carte dans un client, elle devrait apparaître dans la zone de dépôt de l'autre, tout en supprimant un dos de carte, signifiant qu'une carte a été jouée :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Card-Played-1.PNG)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Card-Played-2.PNG)

C'est tout ! Vous devriez maintenant avoir un modèle fonctionnel pour votre jeu de cartes multijoueur, que vous pouvez utiliser pour ajouter vos propres cartes, art et logique de jeu.

Une première étape pourrait être d'ajouter à votre classe Dealer en la faisant mélanger un tableau de cartes et en retourner une aléatoire (indice : consultez [Phaser.Math.RND.shuffle([array])](https://photonstorm.github.io/phaser3-docs/Phaser.Math.RandomDataGenerator.html#shuffle__anchor)).

Bon codage !

Si vous avez aimé cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. a écrit et travaillé pour des entreprises de jeux vidéo et des sites éditoriaux de haut profil tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](https://twitter.com/sominator).