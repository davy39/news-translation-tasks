---
title: Comment créer une application de chat en temps réel avec React, Node, Socket.io
  et HarperDB
subtitle: ''
author: Danny
co_authors: []
series: null
date: '2022-08-04T15:53:22.000Z'
originalURL: https://freecodecamp.org/news/build-a-realtime-chat-app-with-react-express-socketio-and-harperdb
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-keira-burton-6146929.jpg
tags:
- name: Chat
  slug: chat
- name: full stack
  slug: full-stack
- name: node js
  slug: node-js
- name: React
  slug: react
seo_title: Comment créer une application de chat en temps réel avec React, Node, Socket.io
  et HarperDB
seo_desc: "In this article, we will be using Socket.io and HarperDB to build a fullstack,\
  \ real-time chat application with chat rooms. \nThis will be a great project to\
  \ learn how to put together fullstack apps, and how to create an app where the backend\
  \ can commu..."
---

Dans cet article, nous allons utiliser Socket.io et HarperDB pour construire une application de chat fullstack en temps réel avec des salles de discussion. 

Ce sera un excellent projet pour apprendre à assembler des applications fullstack et à créer une application où le backend peut communiquer avec le frontend en temps réel.

Normalement, en utilisant des requêtes HTTP, le serveur ne peut pas pousser des données vers le client en temps réel. Mais en utilisant Socket.io, le serveur est capable de pousser des informations en temps réel au client concernant certains événements qui se sont produits sur le serveur.

L'application que nous allons construire aura deux pages :

Une page pour rejoindre une salle de discussion :

![Comment notre page d'accueil de l'application sera : un formulaire avec un champ de saisie pour le nom d'utilisateur, une liste déroulante pour sélectionner la salle et un bouton Rejoindre la salle](https://lh6.googleusercontent.com/SyHBvbkVavSJTxNV1nOi2-V_YYXm3upFOJvAzBXwd1VNu10SKV4WBSyQS1tdf4OhiDbqlq3sLqCxWRSJafZwhfcsp72DSKEy3-hk3JvNVGcmsSgkHHpEH69pnBDVKCv6bXiMza4cC4BZiLCOiqKPAIk)

Et une page de salle de discussion :

![La page de chat terminée](https://lh6.googleusercontent.com/uRkjeHOuGGGf9HnK7bZ1Zd6WeNMo8kaR6Py0_RiEDx1VUuTPx4oYNvfmPlOxNLAicM7bnr9rm0oY0E7k0fwfaZIEz4K1V-5ejOM3ztmrmjIjC8OsRyzNf0HZurxMWUMzdLgic7o8oC-RQxELo8vdcVw)

Voici ce que nous allons utiliser pour construire cette application :

* **Frontend** : [React](https://reactjs.org/docs/create-a-new-react-app.html) (Un framework JavaScript frontend pour construire des applications interactives)
* **Backend** : [Node](https://nodejs.org/en/) et [Express](https://expressjs.com/) (Express est un framework NodeJS très populaire qui nous permet de créer facilement des APIs et des backends)
* **Base de données** : [HarperDB](https://harperdb.io/) (une plateforme de données + applications qui vous permet d'interroger des données en utilisant soit SQL soit NoSQL. HarperDB a également une API intégrée, ce qui nous évite d'avoir à écrire beaucoup de code backend)
* **Communication en temps réel** : [Socket.io](https://socket.io/docs/v3/) (voir ci-dessous !)

[Voici le code source](https://github.com/DoableDanny/Realtime-chat-app-with-rooms) (n'oubliez pas de lui donner une étoile ⭐).

## Table des matières

1. [Qu'est-ce que Socket.io ?](#heading-questce-que-socketio)
2. [Installation du projet](#heading-installation-du-projet)
3. [Comment construire la page "Rejoindre une salle"](#heading-comment-construire-la-page-rejoindre-une-salle)
4. [Comment configurer le serveur](#heading-comment-configurer-le-serveur)
5. [Comment créer notre premier écouteur d'événements Socket.io sur le serveur](#heading-comment-creer-notre-premier-ecouteur-devenements-socketio-sur-le-serveur)
6. [Comment fonctionnent les salles dans Socket.io](#heading-comment-fonctionnent-les-salles-dans-socketio)
7. [Comment construire la page de chat](#heading-comment-construire-la-page-de-chat)
8. [Comment créer le composant Messages (B)](#heading-comment-creer-le-composant-messages-b)
9. [Comment créer un schéma et une table dans HarperDB](#heading-comment-creer-un-schema-et-une-table-dans-harperdb)
10. [Comment créer le composant Envoyer un message (C)](#heading-comment-creer-le-composant-envoyer-un-message-c)
11. [Comment configurer les variables d'environnement HarperDB](#heading-comment-configurer-les-variables-denvironnement-harperdb)
12. [Comment permettre aux utilisateurs d'envoyer des messages entre eux avec Socket.io](#heading-comment-permettre-aux-utilisateurs-denvoyer-des-messages-entre-eux-avec-socketio)
13. [Comment obtenir des messages de HarperDB](#heading-comment-obtenir-des-messages-de-harperdb)
14. [Comment afficher les 100 derniers messages sur le client](#heading-comment-afficher-les-100-derniers-messages-sur-le-client)
15. [Comment afficher la salle et les utilisateurs (A)](#heading-comment-afficher-la-salle-et-les-utilisateurs-a)
16. [Comment retirer un utilisateur d'une salle Socket.io](#heading-comment-retirer-un-utilisateur-dune-salle-socketio)
17. [Comment ajouter l'écouteur d'événements de déconnexion Socket.io](#heading-comment-ajouter-lecouteur-devenements-de-deconnexion-socketio)

## Qu'est-ce que Socket.IO ?

Socket.IO permet au serveur de pousser des informations vers le client en temps réel, lorsque des événements se produisent sur le serveur.

Par exemple, si vous jouiez à un jeu multijoueur, un événement pourrait être votre "ami" marquant un but spectaculaire contre vous.

Avec Socket.IO, vous sauriez (presque) instantanément que vous avez concédé un but.

Sans Socket.IO, le client devrait faire plusieurs appels AJAX de polling pour vérifier que l'événement s'est produit sur le serveur. Par exemple, le client pourrait utiliser JavaScript pour vérifier un événement sur le serveur toutes les 5 secondes.

Socket.IO signifie que le client n'a pas à faire plusieurs appels AJAX de polling pour vérifier si un événement s'est produit sur le serveur. Au lieu de cela, le serveur envoie l'information au client dès qu'il la reçoit. Bien mieux. 👌

Ainsi, Socket.IO nous permet de construire facilement des applications en temps réel, telles que des applications de chat et des jeux multijoueurs.

## Installation du projet

### 1. Comment configurer nos dossiers

Commencez un nouveau projet dans votre éditeur de texte préféré (VS Code pour moi), et créez deux dossiers à la racine appelés client et server.

![Structure des dossiers de l'application de chat en temps réel](https://www.freecodecamp.org/news/content/images/2022/07/folder-structure.JPG)

Nous allons créer notre application frontend React dans le dossier client, et notre backend Node/Express dans le dossier server.

### 2. Comment installer nos dépendances client

Ouvrez un terminal à la racine du projet (dans VS Code, vous pouvez faire cela en appuyant sur Ctrl+' ou en allant dans _terminal_->_nouveau terminal_)

Ensuite, nous allons installer React dans notre répertoire client :

```bash
$ npx create-react-app client
```

Après l'installation de React, changez de répertoire dans le dossier client, et installez les dépendances suivantes :

```bash
$ cd client
$ npm i react-router-dom socket.io-client
```

React-router-dom nous permettra de configurer des routes vers nos différents composants React – créant essentiellement différentes pages.

Socket.io-client est la version client de socket.io, qui nous permet d'« émettre » des événements vers le serveur. Une fois reçus par le serveur, nous pouvons utiliser la version serveur de socket.io pour faire des choses comme envoyer des messages aux utilisateurs dans la même salle que l'expéditeur, ou rejoindre un utilisateur à une salle socket. 

Vous comprendrez mieux cela plus tard lorsque nous mettrons en œuvre ces idées avec du code.

### 3. Comment démarrer l'application React

Vérifions que tout fonctionne en exécutant la commande suivante depuis le répertoire client :

```bash
$ npm start
```

Webpack va construire l'application React et la servir sur [http://localhost:3000](http://localhost:3000) :

![Create react app up and running on localhost](https://www.freecodecamp.org/news/content/images/2022/07/react-is-running.JPG)

Configurons maintenant notre base de données HarperDB que nous utiliserons pour sauvegarder en permanence les messages envoyés par les utilisateurs.

### Comment configurer HarperDB

Tout d'abord, [créez un compte avec HarperDB](https://studio.harperdb.io/).

Ensuite, créez une nouvelle instance cloud HarperDB :

![create HarperDB instance](https://www.freecodecamp.org/news/content/images/2022/03/harper_instance.JPG)

Pour simplifier les choses, sélectionnez l'instance cloud :

![select HarperDB instance type](https://www.freecodecamp.org/news/content/images/2022/03/instance-type.JPG)

Sélectionnez le fournisseur cloud (j'ai choisi AWS) :

![select HarperDB cloud provider](https://www.freecodecamp.org/news/content/images/2022/03/cloud_provider.JPG)

Nommez votre instance cloud, et créez vos identifiants d'instance :

![select HarperDB instance credentials](https://www.freecodecamp.org/news/content/images/2022/03/instance_credentials.JPG)

HarperDB propose un niveau gratuit généreux que nous pouvons utiliser pour ce projet, alors sélectionnez-le :

![select HarperDB instance specs](https://www.freecodecamp.org/news/content/images/2022/03/instance_specs.JPG)

Vérifiez que vos détails sont corrects, puis créez l'instance.

Il faudra quelques minutes pour créer l'instance, alors continuons et créons notre premier composant React !

![HarperDB instance loading](https://www.freecodecamp.org/news/content/images/2022/03/instance_loading.JPG)

## Comment construire la page "Rejoindre une salle"

Notre page d'accueil va finir par ressembler à ceci :

![Comment notre page d'accueil de l'application sera : un formulaire avec un champ de saisie pour le nom d'utilisateur, une liste déroulante pour sélectionner la salle et un bouton Rejoindre la salle](https://www.freecodecamp.org/news/content/images/2022/07/home-page.JPG)

L'utilisateur entrera un nom d'utilisateur, sélectionnera une salle de discussion dans la liste déroulante, puis cliquera sur "Rejoindre la salle". L'utilisateur sera ensuite dirigé vers la page de la salle de discussion.

Alors, créons cette page d'accueil.

### 1. Comment créer le formulaire HTML et ajouter des styles

Créez un nouveau fichier à _src/pages/home/index.js._

Nous allons ajouter un style de base à notre application en utilisant des modules CSS, alors créez un nouveau fichier : _src/pages/home/styles.module.css_.

Notre structure de dossiers devrait maintenant ressembler à ceci :

![pages folder with home page component](https://www.freecodecamp.org/news/content/images/2022/07/pages-folder-structure.JPG)

Maintenant, créons le HTML de base du formulaire :

```jsx
// client/src/pages/home/index.js

import styles from './styles.module.css';

const Home = () => {
  return (
    <div className={styles.container}>
      <div className={styles.formContainer}>
        <h1>{`<>DevRooms</>`}</h1>
        <input className={styles.input} placeholder='Username...' />

        <select className={styles.input}>
          <option>-- Select Room --</option>
          <option value='javascript'>JavaScript</option>
          <option value='node'>Node</option>
          <option value='express'>Express</option>
          <option value='react'>React</option>
        </select>

        <button className='btn btn-secondary'>Join Room</button>
      </div>
    </div>
  );
};

export default Home;
```

Ci-dessus, nous avons une simple entrée de texte pour capturer le nom d'utilisateur, et une liste déroulante de sélection avec quelques options par défaut pour que l'utilisateur sélectionne une salle de discussion à rejoindre.

Importons maintenant ce composant dans App.js, et configurons une route pour le composant en utilisant le package react-router-dom. Ce sera notre page d'accueil, donc le chemin sera simplement "/" :

```jsx
// client/src/App.js

import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';

function App() {
  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/' element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```

Ajoutons maintenant quelques styles de base pour rendre notre application plus présentable :

```css
/* client/src/App.css */

html * {
  font-family: Arial;
  box-sizing: border-box;
}
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  background: rgb(63, 73, 204);
}
::-webkit-scrollbar {
  width: 20px;
}
::-webkit-scrollbar-track {
  background-color: transparent;
}
::-webkit-scrollbar-thumb {
  background-color: #d6dee1;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
}
::-webkit-scrollbar-thumb:hover {
  background-color: #a8bbbf;
}
.btn {
  padding: 14px 14px;
  border-radius: 6px;
  font-weight: bold;
  font-size: 1.1rem;
  cursor: pointer;
  border: none;
}
.btn-outline {
  color: rgb(153, 217, 234);
  border: 1px solid rgb(153, 217, 234);
  background: rgb(63, 73, 204);
}
.btn-primary {
  background: rgb(153, 217, 234);
  color: rgb(0, 24, 111);
}
.btn-secondary {
  background: rgb(0, 24, 111);
  color: #fff;
}
```

Ajoutons également les styles spécifiques à notre composant de page d'accueil :

```css
/* client/src/pages/home/styles.module.css */

.container {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgb(63, 73, 204);
}
.formContainer {
  width: 400px;
  margin: 0 auto 0 auto;
  padding: 32px;
  background: lightblue;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;
}
.input {
  width: 100%;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid rgb(63, 73, 204);
  font-size: 0.9rem;
}
.input option {
  margin-top: 20px;
}

```

Rendons également le bouton "Join Room" en pleine largeur en ajoutant un attribut de style :

```jsx
// client/src/pages/home/index.js

<button className='btn btn-secondary' style={{ width: '100%' }}>Join Room</button>
```

Notre page d'accueil a maintenant l'air solide :

![Fully-styled home page](https://www.freecodecamp.org/news/content/images/2022/07/home-page-html.JPG)

### 2. Comment ajouter une fonctionnalité au formulaire Join Room

Maintenant que nous avons un formulaire de base et un style, il est temps d'ajouter une fonctionnalité.

Voici ce que nous voulons qu'il se passe lorsque l'utilisateur clique sur le bouton "Join Room" :

1. Vérifier que les champs nom d'utilisateur et salle sont remplis.
2. Si c'est le cas, nous émettons un événement socket vers notre serveur.
3. Rediriger l'utilisateur vers la page Chat (que nous créerons plus tard).

Nous allons devoir créer un état pour stocker les valeurs _username_ et _room_. Nous devons également créer une instance de socket.

Nous pourrions créer ces états directement dans notre composant home, mais notre page Chat aura également besoin d'accéder à _username_, _room_ et _socket_. Nous allons donc remonter l'état à App.js, où nous pourrons ensuite passer ces variables aux composants Homepage et Chat page.

Alors, créons notre état et configurons un socket dans App.js, et passons ces variables en tant que props au composant <Home />. Nous passerons également les fonctions set state afin de pouvoir modifier l'état depuis <Home /> :

```jsx
// client/src/App.js

import './App.css';
import { useState } from 'react'; // Add this
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import io from 'socket.io-client'; // Add this
import Home from './pages/home';

const socket = io.connect('http://localhost:4000'); // Add this -- our server will run on port 4000, so we connect to it from here

function App() {
  const [username, setUsername] = useState(''); // Add this
  const [room, setRoom] = useState(''); // Add this

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route
            path='/'
            element={
              <Home
                username={username} // Add this
                setUsername={setUsername} // Add this
                room={room} // Add this
                setRoom={setRoom} // Add this
                socket={socket} // Add this
              />
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

Nous pouvons maintenant accéder à ces props dans notre composant Home. Nous utiliserons la déstructuration pour obtenir les props :

```jsx
// client/src/pages/home/index.js

import styles from './style.module.css';

const Home = ({ username, setUsername, room, setRoom, socket }) => {
  return (
    // ...
  );
};

export default Home;
```

Lorsque l'utilisateur tape son nom d'utilisateur ou sélectionne une salle, nous devons mettre à jour les variables d'état _username_ et _room_ :

```jsx
// client/src/pages/home/index.js

// ...

const Home = ({ username, setUsername, room, setRoom, socket }) => {
  return (
    <div className={styles.container}>
      // ...
        <input
          className={styles.input}
          placeholder='Username...'
          onChange={(e) => setUsername(e.target.value)} // Add this
        />

        <select
          className={styles.input}
          onChange={(e) => setRoom(e.target.value)} // Add this
        >
         // ...
        </select>

        // ...
    </div>
  );
};

export default Home;

```

Maintenant que nous capturons les données saisies par l'utilisateur, nous pouvons créer une fonction de rappel _joinRoom()_ pour lorsque l'utilisateur clique sur le bouton "Join Room" :

```jsx
// client/src/pages/home/index.js

// ...

const Home = ({ username, setUsername, room, setRoom, socket }) => {
  
  // Add this
  const joinRoom = () => {
    if (room !== '' && username !== '') {
      socket.emit('join_room', { username, room });
    }
  };

  return (
    <div className={styles.container}>
      // ...
      
        <button
          className='btn btn-secondary'
          style={{ width: '100%' }}
          onClick={joinRoom} // Add this
        >
          Join Room
        </button>
      // ...
    </div>
  );
};

export default Home;

```

Ci-dessus, lorsque l'utilisateur clique sur le bouton, un événement socket appelé _join_room_ est émis, ainsi qu'un objet contenant le nom d'utilisateur et la salle sélectionnée par l'utilisateur. Cet événement sera reçu par notre serveur un peu plus tard où nous ferons un peu de magie.

Pour terminer notre composant de page d'accueil, nous devons ajouter une redirection en bas de notre fonction _joinRoom()_ pour emmener l'utilisateur à la page _/chat_ :

```jsx
// client/src/pages/home/index.js

// ...
import { useNavigate } from 'react-router-dom'; // Add this

const Home = ({ username, setUsername, room, setRoom, socket }) => {
  const navigate = useNavigate(); // Add this

  const joinRoom = () => {
    if (room !== '' && username !== '') {
      socket.emit('join_room', { username, room });
    }

    // Redirect to /chat
    navigate('/chat', { replace: true }); // Add this
  };

 // ...

```

Testez-le : tapez un nom d'utilisateur et sélectionnez une salle, puis cliquez sur _Join Room_. Vous devriez être dirigé vers la route [http://localhost:3000/chat](http://localhost:3000/chat) – actuellement une page vide.

Mais avant de créer notre frontend de page de chat, faisons fonctionner quelques choses sur le serveur.

## Comment configurer le serveur

Sur le serveur, nous allons écouter les événements socket émis depuis le frontend. Actuellement, nous n'avons qu'un événement join_room émis depuis React, donc nous allons ajouter cet écouteur d'événement en premier.

Mais avant cela, nous devons installer nos dépendances serveur et faire fonctionner le serveur.

### 1. Comment installer les dépendances du serveur

Ouvrez un nouveau terminal (dans VS code : Terminal->Nouveau Terminal), changez de répertoire dans notre dossier serveur, initialisez un fichier package.json, et installez les dépendances suivantes :

```bash
$ cd server
$ npm init -y
$ npm i axios cors express socket.io dotenv
```

* Axios est un package couramment utilisé pour faire facilement des requêtes aux APIs. 
* Cors permet à notre client de faire des requêtes à d'autres origines – nécessaire pour que socket.io fonctionne correctement. Voir [Qu'est-ce que CORS ?](https://medium.com/@electra_chong/what-is-cors-what-is-it-used-for-308cafa4df1a) si vous n'avez jamais entendu parler de CORS auparavant.
* Express est un framework NodeJS qui nous permet d'écrire notre backend plus facilement avec moins de code.
* Socket.io est une bibliothèque qui permet au client et au serveur de communiquer en temps réel – ce qui n'est pas possible avec les requêtes HTTP standard.
* Dotenv est un module qui nous permet de stocker des clés privées et des mots de passe en toute sécurité, et de les charger dans notre code lorsque cela est nécessaire.

Nous allons également installer nodemon comme dépendance de développement, afin de ne pas avoir à redémarrer notre serveur chaque fois que nous apportons une modification au code – ce qui nous fait gagner du temps et de l'énergie :

```bash
$ npm i -D nodemon
```

### 2. Comment démarrer notre serveur

Créez un dossier appelé index.js à la racine de notre répertoire serveur, et ajoutez le code suivant pour démarrer un serveur :

```javascript
// server/index.js

const express = require('express');
const app = express();
const http = require('http');
const cors = require('cors');

app.use(cors()); // Add cors middleware

const server = http.createServer(app);

server.listen(4000, () => 'Server is running on port 4000');
```

Ouvrez le fichier package.json sur notre serveur, et ajoutez un script qui nous permettra d'utiliser nodemon en développement :

```json
{
  ...
  "scripts": {
    "dev": "nodemon index.js"
  },
  ...
}

```

Maintenant, démarrons notre serveur en exécutant la commande suivante :

```bash
$ npm run dev
```

Nous pouvons rapidement vérifier que notre serveur fonctionne correctement en ajoutant un gestionnaire de requêtes get :

```javascript
// server/index.js

const express = require('express');
const app = express();
http = require('http');
const cors = require('cors');

app.use(cors()); // Add cors middleware

const server = http.createServer(app);

// Add this
app.get('/', (req, res) => {
  res.send('Hello world');
});

server.listen(4000, () => 'Server is running on port 3000');
```

Maintenant, allez sur [http://localhost:4000/](http://localhost:4000/) :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/localhost4000.JPG)

Notre serveur est opérationnel. Il est maintenant temps de faire quelques trucs côté serveur avec Socket.io !

## Comment créer notre premier écouteur d'événements Socket.io sur le serveur

Vous vous souvenez quand nous avons émis un événement _join_room_ depuis le client ? Eh bien, nous allons bientôt écouter cet événement sur le serveur et ajouter l'utilisateur à une salle socket.

Mais d'abord, nous devons écouter quand un client se connecte au serveur via socket.io-client.

```javascript
// server/index.js

const express = require('express');
const app = express();
http = require('http');
const cors = require('cors');
const { Server } = require('socket.io'); // Add this

app.use(cors()); // Add cors middleware

const server = http.createServer(app); // Add this

// Add this
// Create an io server and allow for CORS from http://localhost:3000 with GET and POST methods
const io = new Server(server, {
  cors: {
    origin: 'http://localhost:3000',
    methods: ['GET', 'POST'],
  },
});

// Add this
// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
  console.log(`User connected ${socket.id}`);

  // We can write our socket event listeners in here...
});

server.listen(4000, () => 'Server is running on port 3000');
```

Maintenant, lorsque le client se connecte depuis le frontend, le backend capture l'événement de connexion, et enregistrera `User connected` avec l'ID de socket unique pour ce client particulier.

Testons si le serveur capture maintenant l'événement de connexion depuis le client. Allez sur votre application React à [http://localhost:3000/](http://localhost:3000/) et actualisez la page. 

Vous devriez voir le journal suivant dans votre console de terminal serveur :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/user-connected.JPG)

Super, notre client s'est connecté à notre serveur via socket.io. Notre client et notre serveur peuvent maintenant communiquer en temps réel !

## Comment fonctionnent les salles dans Socket.io

D'après la [documentation de Socket.io](https://socket.io/docs/v3/rooms/) :

> "Une _salle_ est un canal arbitraire que les sockets peuvent `joindre` et `quitter`. Elle peut être utilisée pour diffuser des événements à un sous-ensemble de clients."

Ainsi, nous pouvons joindre l'utilisateur à une salle, et ensuite le serveur peut envoyer des messages à tous les utilisateurs dans cette salle – permettant aux utilisateurs d'envoyer des messages les uns aux autres en temps réel. Cool !

### Comment joindre l'utilisateur à une salle Socket.io

Une fois que l'utilisateur s'est connecté via Socket.io, nous pouvons ajouter nos écouteurs d'événements socket sur le serveur pour écouter les événements émis depuis le client. De plus, nous pouvons émettre des événements sur le serveur, et les écouter sur le client.

Écoutons maintenant l'événement _join_room_, capturons les données (nom d'utilisateur et salle), et ajoutons l'utilisateur à une salle socket :

```javascript
// server/index.js

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
  console.log(`User connected ${socket.id}`);

  // Add this
  // Add a user to a room
  socket.on('join_room', (data) => {
    const { username, room } = data; // Data sent from client when join_room event emitted
    socket.join(room); // Join the user to a socket room
  });
});
```

### Comment envoyer un message aux utilisateurs dans une salle

Envoyons maintenant un message à tous les utilisateurs dans la salle, à l'exception de l'utilisateur qui vient de rejoindre, pour les informer qu'un nouvel utilisateur a rejoint :

```javascript
// server/index.js

const CHAT_BOT = 'ChatBot'; // Add this
// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
  console.log(`User connected ${socket.id}`);

  // Add a user to a room
  socket.on('join_room', (data) => {
    const { username, room } = data; // Data sent from client when join_room event emitted
    socket.join(room); // Join the user to a socket room

    // Add this
    let __createdtime__ = Date.now(); // Current timestamp
    // Send message to all users currently in the room, apart from the user that just joined
    socket.to(room).emit('receive_message', {
      message: `${username} has joined the chat room`,
      username: CHAT_BOT,
      __createdtime__,
    });
  });
});
```

Ci-dessus, nous émettons un événement receive_message à tous les clients dans la salle que l'utilisateur actuel vient de rejoindre, ainsi que certaines données : le message, le nom d'utilisateur de l'expéditeur du message, et l'heure à laquelle le message a été envoyé.

Nous ajouterons un écouteur d'événements dans notre application React un peu plus tard pour capturer cet événement et afficher le message à l'écran.

Envoyons également un message de bienvenue à l'utilisateur nouvellement rejoint :

```javascript
// server/index.js

io.on('connection', (socket) => {
  // ...

    // Add this
    // Send welcome msg to user that just joined chat only
    socket.emit('receive_message', {
      message: `Welcome ${username}`,
      username: CHAT_BOT,
      __createdtime__,
    });
  });
});
```

Lorsque nous ajoutons un utilisateur à une salle Socket.io, Socket.io ne stocke que les identifiants de socket pour chaque utilisateur. Mais nous aurons besoin des noms d'utilisateur de tous les utilisateurs dans la salle, ainsi que du nom de la salle. Alors, stockons ces données dans des variables sur le serveur :

```javascript
// server/index.js

// ...

const CHAT_BOT = 'ChatBot';
// Add this
let chatRoom = ''; // E.g. javascript, node,...
let allUsers = []; // All users in current chat room

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
    // ...
    
    // Add this
    // Save the new user to the room
    chatRoom = room;
    allUsers.push({ id: socket.id, username, room });
    chatRoomUsers = allUsers.filter((user) => user.room === room);
    socket.to(room).emit('chatroom_users', chatRoomUsers);
    socket.emit('chatroom_users', chatRoomUsers);
  });
});
```

Ci-dessus, nous envoyons également un tableau de tous les chatRoomUsers au client via l'événement _chatroom_users_, afin que nous puissions lister tous les noms d'utilisateur dans la salle sur le frontend.

Avant d'ajouter plus de code à notre serveur, retournons à notre frontend et créons la page de chat – afin que nous puissions tester si nous recevons les événements _receive_message_. 

## Comment construire la page de chat

Dans votre dossier client, créez deux nouveaux fichiers :

1. src/pages/chat/index.js
2. src/pages/chat/styles.module.css

Ajoutons quelques styles que nous utiliserons dans notre page de chat et nos composants :

```css
/* client/src/pages/chat/styles.module.css */

.chatContainer {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 4fr;
  gap: 20px;
}

/* Room and users component */
.roomAndUsersColumn {
  border-right: 1px solid #dfdfdf;
}
.roomTitle {
  margin-bottom: 60px;
  text-transform: uppercase;
  font-size: 2rem;
  color: #fff;
}
.usersTitle {
  font-size: 1.2rem;
  color: #fff;
}
.usersList {
  list-style-type: none;
  padding-left: 0;
  margin-bottom: 60px;
  color: rgb(153, 217, 234);
}
.usersList li {
  margin-bottom: 12px;
}

/* Messages */
.messagesColumn {
  height: 85vh;
  overflow: auto;
  padding: 10px 10px 10px 40px;
}
.message {
  background: rgb(0, 24, 111);
  border-radius: 6px;
  margin-bottom: 24px;
  max-width: 600px;
  padding: 12px;
}
.msgMeta {
  color: rgb(153, 217, 234);
  font-size: 0.75rem;
}
.msgText {
  color: #fff;
}

/* Message input and button */
.sendMessageContainer {
  padding: 16px 20px 20px 16px;
}
.messageInput {
  padding: 14px;
  margin-right: 16px;
  width: 60%;
  border-radius: 6px;
  border: 1px solid rgb(153, 217, 234);
  font-size: 0.9rem;
}

```

Voyons maintenant à quoi ressemblera notre page de chat :

![La page de chat terminée](https://www.freecodecamp.org/news/content/images/2022/07/chat-page.JPG)

Ajouter tout le code et la logique pour cette page dans un seul fichier pourrait devenir confus et difficile à gérer, alors profitons du fait que nous utilisons un framework frontend génial (React) et **divisons notre page en composants** :

![La page de chat divisée en trois composants](https://www.freecodecamp.org/news/content/images/2022/07/image-248.png)

### Les composants de la page de chat :

**A** : Contient le nom de la salle, une liste des utilisateurs dans cette salle, et un bouton "Quitter" qui retire l'utilisateur de la salle.

**B** : Les messages envoyés. Lors du rendu initial, les 100 derniers messages envoyés dans cette salle seront récupérés depuis la base de données et affichés à l'utilisateur.

**C** : Une entrée et un bouton pour taper et envoyer un message.

Nous allons d'abord créer le composant B, afin de pouvoir afficher les messages à l'utilisateur.

## Comment créer le composant Messages (B)

Créez un nouveau fichier à src/pages/chat/messages.js et ajoutez le code suivant :

```jsx
// client/src/pages/chat/messages.js

import styles from './styles.module.css';
import { useState, useEffect } from 'react';

const Messages = ({ socket }) => {
  const [messagesRecieved, setMessagesReceived] = useState([]);

  // Runs whenever a socket event is recieved from the server
  useEffect(() => {
    socket.on('receive_message', (data) => {
      console.log(data);
      setMessagesReceived((state) => [
        ...state,
        {
          message: data.message,
          username: data.username,
          __createdtime__: data.__createdtime__,
        },
      ]);
    });

	// Remove event listener on component unmount
    return () => socket.off('receive_message');
  }, [socket]);

  // dd/mm/yyyy, hh:mm:ss
  function formatDateFromTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString();
  }

  return (
    <div className={styles.messagesColumn}>
      {messagesRecieved.map((msg, i) => (
        <div className={styles.message} key={i}>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span className={styles.msgMeta}>{msg.username}</span>
            <span className={styles.msgMeta}>
              {formatDateFromTimestamp(msg.__createdtime__)}
            </span>
          </div>
          <p className={styles.msgText}>{msg.message}</p>
          <br />
        </div>
      ))}
    </div>
  );
};

export default Messages;
```

Ci-dessus, nous avons un hook _useEffect_ qui s'exécute chaque fois qu'un événement socket est reçu. Nous obtenons ensuite les données du message passées dans l'écouteur d'événements _receive_message_. À partir de là, nous définissons l'état _messagesReceived_, qui est un tableau d'objets de message contenant le message, le nom d'utilisateur de l'expéditeur et la date à laquelle le message a été envoyé.

Importons notre nouveau composant de messages dans la page de chat, puis créons une route pour la page de chat dans App.js :

```jsx
// client/src/pages/chat/index.js

import styles from './styles.module.css';
import MessagesReceived from './messages';

const Chat = ({ socket }) => {
  return (
    <div className={styles.chatContainer}>
      <div>
        <MessagesReceived socket={socket} />
      </div>
    </div>
  );
};

export default Chat;

```

```jsx
// client/src/App.js

import './App.css';
import { useState } from 'react';
import Home from './pages/home';
import Chat from './pages/chat';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import io from 'socket.io-client';

const socket = io.connect('http://localhost:4000');

function App() {
  const [username, setUsername] = useState('');
  const [room, setRoom] = useState('');

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route
            path='/'
            element={
              <Home
                username={username}
                setUsername={setUsername}
                room={room}
                setRoom={setRoom}
                socket={socket}
              />
            }
          />
          {/* Add this */}
          <Route
            path='/chat'
            element={<Chat username={username} room={room} socket={socket} />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

Testons cela : allez sur la page d'accueil et rejoignez une salle :

![Joining a room as Dan](https://www.freecodecamp.org/news/content/images/2022/07/joining-a-room.JPG)

Nous devrions être redirigés vers la page de chat et recevoir un message de bienvenue de _ChatBot_ : 

![Welcome message received from ChatBot](https://www.freecodecamp.org/news/content/images/2022/07/welcome-message.JPG)

Les utilisateurs peuvent maintenant voir les messages qu'ils reçoivent. Super !

Prochaine étape : configurer notre base de données afin de pouvoir sauvegarder en permanence les messages.

## Comment créer un schéma et une table dans HarperDB

Retournez à votre tableau de bord HarperDB, et cliquez sur "browse". Ensuite, créez un nouveau schéma appelé "realtime_chat_app". Un schéma est simplement un groupe de tables.

Dans ce schéma, créez une table appelée "messages", avec un attribut de hachage de "id".

![Creating our schema and table in HarperDB](https://www.freecodecamp.org/news/content/images/2022/07/image-258.png)

Nous avons maintenant un endroit pour stocker les messages, alors créons le composant SendMessage.

## Comment créer le composant Envoyer un message (C)

Créez le fichier src/pages/chat/send-message.js et ajoutez le code suivant :

```jsx
// client/src/pages/chat/send-message.js

import styles from './styles.module.css';
import React, { useState } from 'react';

const SendMessage = ({ socket, username, room }) => {
  const [message, setMessage] = useState('');

  const sendMessage = () => {
    if (message !== '') {
      const __createdtime__ = Date.now();
      // Send message to server. We can't specify who we send the message to from the frontend. We can only send to server. Server can then send message to rest of users in room
      socket.emit('send_message', { username, room, message, __createdtime__ });
      setMessage('');
    }
  };

  return (
    <div className={styles.sendMessageContainer}>
      <input
        className={styles.messageInput}
        placeholder='Message...'
        onChange={(e) => setMessage(e.target.value)}
        value={message}
      />
      <button className='btn btn-primary' onClick={sendMessage}>
        Send Message
      </button>
    </div>
  );
};

export default SendMessage;
```

Ci-dessus, lorsque l'utilisateur clique sur le bouton "Send Message", un événement socket send_message est émis vers le serveur, ainsi qu'un objet message. Nous allons gérer cet événement sur le serveur sous peu.

Importons _SendMessage_ dans notre page de chat :

```js
// src/pages/chat/index.js

import styles from './styles.module.css';
import MessagesReceived from './messages';
import SendMessage from './send-message';

const Chat = ({ username, room, socket }) => {
  return (
    <div className={styles.chatContainer}>
      <div>
        <MessagesReceived socket={socket} />
        <SendMessage socket={socket} username={username} room={room} />
      </div>
    </div>
  );
};

export default Chat;
```

La page de chat ressemble maintenant à ceci :

![Chat page now has a message input where a message can be typed and sent](https://www.freecodecamp.org/news/content/images/2022/07/image-259.png)

Ensuite, nous devons configurer nos variables d'environnement HarperDB afin de pouvoir commencer à interagir avec la base de données.

## Comment configurer les variables d'environnement HarperDB

Pour pouvoir sauvegarder des messages dans HarperDB, vous aurez besoin de l'URL de votre instance HarperDB et de votre mot de passe API. 

Dans votre tableau de bord HarperDB, cliquez sur votre instance, puis allez dans "config". Vous trouverez votre URL d'instance et votre en-tête d'authentification API HarperDB – c'est-à-dire votre mot de passe "super_user" qui vous permet de faire toute demande à la base de données – POUR VOS YEUX SEULEMENT !

![HarperDB instance URL and API auth header](https://www.freecodecamp.org/news/content/images/2022/07/image-263.png)

Nous allons stocker ces variables dans un fichier .env. **Attention : ne poussez pas le fichier .env sur GitHub !** Ce fichier ne doit pas être visible publiquement. Les variables sont chargées via le serveur en arrière-plan.

Créez les fichiers suivants et ajoutez votre URL HarperDB et votre mot de passe :

```bash
// server/.env

HARPERDB_URL="<your url goes here>"
HARPERDB_PW="Basic <your password here>"
```

Nous allons également créer un fichier .gitignore pour empêcher le .env d'être poussé sur GitHub, ainsi que le dossier node_modules :

```bash
// server/.gitignore

.env
node_modules
```

Note : être bon avec Git et GitHub est un must à 100% pour tous les développeurs. Consultez mon [article sur les workflows Git](https://www.doabledanny.com/git-workflows) si vous avez besoin d'améliorer votre jeu Git.

Ou si vous vous retrouvez constamment à chercher les mêmes commandes Git, et que vous voulez une façon rapide de chercher, réviser et copier/coller des commandes -- consultez ma populaire [feuille de triche des commandes Git PDF](https://doabledanny.gumroad.com/l/git-commands-cheat-sheet-pdf) et [poster de feuille de triche Git physique](https://doabledanny.gumroad.com/l/git-cheat-sheet-poster).

Enfin, chargeons nos variables d'environnement dans notre serveur en ajoutant ce code en haut de notre fichier serveur principal :

```js
// server/index.js

require('dotenv').config();
console.log(process.env.HARPERDB_URL); // remove this after you've confirmed it working
const express = require('express');
// ...
```

## Comment permettre aux utilisateurs d'envoyer des messages entre eux avec Socket.io

Sur le serveur, nous allons écouter l'événement _send_message_, puis envoyer le message à tous les utilisateurs dans la salle :

```js
// server/index.js

const express = require('express');
// ...
const harperSaveMessage = require('./services/harper-save-message'); // Add this

// ...

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
    
  // ...

  // Add this
  socket.on('send_message', (data) => {
    const { message, username, room, __createdtime__ } = data;
    io.in(room).emit('receive_message', data); // Send to all users in room, including sender
    harperSaveMessage(message, username, room, __createdtime__) // Save message in db
      .then((response) => console.log(response))
      .catch((err) => console.log(err));
  });
});

server.listen(4000, () => 'Server is running on port 3000');

```

Nous devons maintenant créer la fonction _harperSaveMessage_. Créez un nouveau fichier à server/services/harper-save-message.js, et ajoutez ce qui suit :

```js
// server/services/harper-save-message.js

var axios = require('axios');

function harperSaveMessage(message, username, room) {
  const dbUrl = process.env.HARPERDB_URL;
  const dbPw = process.env.HARPERDB_PW;
  if (!dbUrl || !dbPw) return null;

  var data = JSON.stringify({
    operation: 'insert',
    schema: 'realtime_chat_app',
    table: 'messages',
    records: [
      {
        message,
        username,
        room,
      },
    ],
  });

  var config = {
    method: 'post',
    url: dbUrl,
    headers: {
      'Content-Type': 'application/json',
      Authorization: dbPw,
    },
    data: data,
  };

  return new Promise((resolve, reject) => {
    axios(config)
      .then(function (response) {
        resolve(JSON.stringify(response.data));
      })
      .catch(function (error) {
        reject(error);
      });
  });
}

module.exports = harperSaveMessage;

```

Ci-dessus, l'enregistrement des données peut prendre un peu de temps, donc nous retournons une promesse qui sera résolue si les données sont enregistrées avec succès, ou rejetée si ce n'est pas le cas.

Si vous vous demandez d'où vient le code ci-dessus, HarperDB fournit une section "[exemples de code](https://studio.harperdb.io/resources/examples/QuickStart%20Examples/Create%20dev%20Schema)" géniale dans leur tableau de bord studio, ce qui facilite grandement la vie :

![HarperDB code examples](https://www.freecodecamp.org/news/content/images/2022/07/image-265.png)

Il est temps de tester ! Rejoignez une salle en tant qu'utilisateur, puis envoyez un message. Ensuite, allez sur HarperDB et cliquez sur "browse", puis cliquez sur la table "messages". Vous devriez voir votre message dans la base de données :

![Our first messages in the database](https://www.freecodecamp.org/news/content/images/2022/07/image-264.png)

Cool 😊. Alors, quoi ensuite ? Eh bien, ce serait génial si les 100 derniers messages envoyés dans la salle étaient chargés lorsqu'un utilisateur rejoint une salle, n'est-ce pas ?

## Comment obtenir des messages de HarperDB

Sur le serveur, créons une fonction qui récupère les 100 derniers messages envoyés dans une salle particulière (remarquez comment HarperDB nous permet également d'utiliser des requêtes SQL 👍) :

```js
// server/services/harper-get-messages.js

let axios = require('axios');

function harperGetMessages(room) {
  const dbUrl = process.env.HARPERDB_URL;
  const dbPw = process.env.HARPERDB_PW;
  if (!dbUrl || !dbPw) return null;

  let data = JSON.stringify({
    operation: 'sql',
    sql: `SELECT * FROM realtime_chat_app.messages WHERE room = '${room}' LIMIT 100`,
  });

  let config = {
    method: 'post',
    url: dbUrl,
    headers: {
      'Content-Type': 'application/json',
      Authorization: dbPw,
    },
    data: data,
  };

  return new Promise((resolve, reject) => {
    axios(config)
      .then(function (response) {
        resolve(JSON.stringify(response.data));
      })
      .catch(function (error) {
        reject(error);
      });
  });
}

module.exports = harperGetMessages;
```

Nous appellerons cette fonction chaque fois qu'un utilisateur rejoint une salle :

```js
// server/index.js

// ...
const harperSaveMessage = require('./services/harper-save-message');
const harperGetMessages = require('./services/harper-get-messages'); // Add this

// ...

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
  console.log(`User connected ${socket.id}`);

  // Add a user to a room
  socket.on('join_room', (data) => {
      
    // ...

    // Add this
    // Get last 100 messages sent in the chat room
    harperGetMessages(room)
      .then((last100Messages) => {
        // console.log('latest messages', last100Messages);
        socket.emit('last_100_messages', last100Messages);
      })
      .catch((err) => console.log(err));
  });

 // ...
```

Ci-dessus, si les messages sont récupérés avec succès, nous émettons un événement Socket.io appelé _last_100_messages_. Nous allons maintenant écouter cet événement sur le frontend.

## Comment afficher les 100 derniers messages sur le client

Ci-dessous, nous ajoutons un hook useEffect qui contient un écouteur d'événements Socket.io pour l'événement _last_100_messages_. À partir de là, les messages sont triés par ordre de date, avec les plus récents en bas, et l'état _messagesReceived_ est mis à jour.

Lorsque _messagesReceived_ est mis à jour, un useEffect s'exécute pour faire défiler la div _messageColumn_ jusqu'au message le plus récent. Cela améliore l'expérience utilisateur de notre application 👍.

```js
// client/src/pages/chat/messages.js

import styles from './styles.module.css';
import { useState, useEffect, useRef } from 'react';

const Messages = ({ socket }) => {
  const [messagesRecieved, setMessagesReceived] = useState([]);

  const messagesColumnRef = useRef(null); // Add this

  // Runs whenever a socket event is recieved from the server
  useEffect(() => {
    socket.on('receive_message', (data) => {
      console.log(data);
      setMessagesReceived((state) => [
        ...state,
        {
          message: data.message,
          username: data.username,
          __createdtime__: data.__createdtime__,
        },
      ]);
    });

    // Remove event listener on component unmount
    return () => socket.off('receive_message');
  }, [socket]);

  // Add this
  useEffect(() => {
    // Last 100 messages sent in the chat room (fetched from the db in backend)
    socket.on('last_100_messages', (last100Messages) => {
      console.log('Last 100 messages:', JSON.parse(last100Messages));
      last100Messages = JSON.parse(last100Messages);
      // Sort these messages by __createdtime__
      last100Messages = sortMessagesByDate(last100Messages);
      setMessagesReceived((state) => [...last100Messages, ...state]);
    });

    return () => socket.off('last_100_messages');
  }, [socket]);

  // Add this
  // Scroll to the most recent message
  useEffect(() => {
    messagesColumnRef.current.scrollTop =
      messagesColumnRef.current.scrollHeight;
  }, [messagesRecieved]);

  // Add this
  function sortMessagesByDate(messages) {
    return messages.sort(
      (a, b) => parseInt(a.__createdtime__) - parseInt(b.__createdtime__)
    );
  }

  // dd/mm/yyyy, hh:mm:ss
  function formatDateFromTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString();
  }

  return (
    // Add ref to this div
    <div className={styles.messagesColumn} ref={messagesColumnRef}>
      {messagesRecieved.map((msg, i) => (
        <div className={styles.message} key={i}>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span className={styles.msgMeta}>{msg.username}</span>
            <span className={styles.msgMeta}>
              {formatDateFromTimestamp(msg.__createdtime__)}
            </span>
          </div>
          <p className={styles.msgText}>{msg.message}</p>
          <br />
        </div>
      ))}
    </div>
  );
};

export default Messages;

```

## Comment afficher la salle et les utilisateurs (A)

Nous avons créé les composants B et C, alors terminons en créant A.

![La page de chat divisée en trois composants](https://www.freecodecamp.org/news/content/images/2022/07/image-248.png)

Sur le serveur, lorsqu'un utilisateur rejoint une salle, nous émettons un événement _chatroom_users_ qui envoie tous les utilisateurs de la salle à tous les clients de cette salle. Écoutez cet événement dans un composant appelé _RoomAndUsers._

Ci-dessous, il y a également un bouton "Quitter" qui, lorsqu'il est pressé, provoque l'émission d'un événement _leave_room_ vers le serveur. Il redirige ensuite l'utilisateur vers la page d'accueil.

```js
// client/src/pages/chat/room-and-users.js

import styles from './styles.module.css';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const RoomAndUsers = ({ socket, username, room }) => {
  const [roomUsers, setRoomUsers] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    socket.on('chatroom_users', (data) => {
      console.log(data);
      setRoomUsers(data);
    });

    return () => socket.off('chatroom_users');
  }, [socket]);

  const leaveRoom = () => {
    const __createdtime__ = Date.now();
    socket.emit('leave_room', { username, room, __createdtime__ });
    // Redirect to home page
    navigate('/', { replace: true });
  };

  return (
    <div className={styles.roomAndUsersColumn}>
      <h2 className={styles.roomTitle}>{room}</h2>

      <div>
        {roomUsers.length > 0 && <h5 className={styles.usersTitle}>Users:</h5>}
        <ul className={styles.usersList}>
          {roomUsers.map((user) => (
            <li
              style={{
                fontWeight: `${user.username === username ? 'bold' : 'normal'}`,
              }}
              key={user.id}
            >
              {user.username}
            </li>
          ))}
        </ul>
      </div>

      <button className='btn btn-outline' onClick={leaveRoom}>
        Leave
      </button>
    </div>
  );
};

export default RoomAndUsers;
```

Importons ce composant dans la page de chat :

```js
// client/src/pages/chat/index.js

import styles from './styles.module.css';
import RoomAndUsersColumn from './room-and-users'; // Add this
import SendMessage from './send-message';
import MessagesReceived from './messages';

const Chat = ({ username, room, socket }) => {
  return (
    <div className={styles.chatContainer}>
      {/* Add this */}
      <RoomAndUsersColumn socket={socket} username={username} room={room} />

      <div>
        <MessagesReceived socket={socket} />
        <SendMessage socket={socket} username={username} room={room} />
      </div>
    </div>
  );
};

export default Chat;

```

## Comment retirer un utilisateur d'une salle Socket.io

Socket.io fournit une méthode _leave()_ que vous pouvez utiliser pour retirer un utilisateur d'une salle Socket.io. Nous suivons également nos utilisateurs dans un tableau en mémoire serveur, donc nous allons également retirer l'utilisateur de ce tableau :

```js
// server/index.js

const leaveRoom = require('./utils/leave-room'); // Add this

// ...

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
    
  // ...

  // Add this
  socket.on('leave_room', (data) => {
    const { username, room } = data;
    socket.leave(room);
    const __createdtime__ = Date.now();
    // Remove user from memory
    allUsers = leaveRoom(socket.id, allUsers);
    socket.to(room).emit('chatroom_users', allUsers);
    socket.to(room).emit('receive_message', {
      username: CHAT_BOT,
      message: `${username} has left the chat`,
      __createdtime__,
    });
    console.log(`${username} has left the chat`);
  });
});

server.listen(4000, () => 'Server is running on port 3000');

```

Nous devons maintenant créer la fonction _leaveRoom()_ :

```js
// server/utils/leave-room.js

function leaveRoom(userID, chatRoomUsers) {
  return chatRoomUsers.filter((user) => user.id != userID);
}

module.exports = leaveRoom;

```

Pourquoi mettre cette fonction courte dans un dossier utils séparé, demandez-vous ? Parce que nous allons l'utiliser à nouveau plus tard et nous ne voulons pas nous répéter (en gardant notre code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)).

Testons les choses : ouvrez deux fenêtres côte à côte, et rejoignez le chat sur les deux :

![Deux fenêtres discutant en temps réel.](https://www.freecodecamp.org/news/content/images/2022/07/image-266.png)

Ensuite, cliquez sur le bouton de départ dans la fenêtre 2 :

![L'utilisateur est retiré du chat lorsqu'il clique sur le bouton Quitter](https://www.freecodecamp.org/news/content/images/2022/07/image-267.png)

L'utilisateur est retiré du chat, et un message est envoyé aux autres utilisateurs – les informant qu'ils sont partis. Bien !

## Comment ajouter l'écouteur d'événements de déconnexion Socket.io

Que se passe-t-il si l'utilisateur est déconnecté du serveur, par exemple si sa connexion Internet est coupée ? Socket.io fournit un écouteur d'événements de _déconnexion_ intégré pour cela. Ajoutons cela à notre serveur pour retirer un utilisateur de la mémoire lorsqu'il se déconnecte :

```js
// server/index.js

// ...

// Listen for when the client connects via socket.io-client
io.on('connection', (socket) => {
    
  // ...
    
  // Add this
  socket.on('disconnect', () => {
    console.log('User disconnected from the chat');
    const user = allUsers.find((user) => user.id == socket.id);
    if (user?.username) {
      allUsers = leaveRoom(socket.id, allUsers);
      socket.to(chatRoom).emit('chatroom_users', allUsers);
      socket.to(chatRoom).emit('receive_message', {
        message: `${user.username} has disconnected from the chat.`,
      });
    }
  });
});

server.listen(4000, () => 'Server is running on port 3000');

```

Et voilà – vous venez de construire une application de chat fullstack en temps réel avec un frontend React, un backend Node/Express et une base de données HarperDB. Bon travail !

La prochaine fois, je prévois de découvrir les [Fonctions Personnalisées](https://harperdb.io/docs/custom-functions/) de HarperDB, qui permettent aux utilisateurs de définir leurs propres points de terminaison API au sein de HarperDB. Cela signifie que nous pouvons construire notre application entière en un seul endroit ! Voir un exemple de la façon dont HarperDB réduit la pile [dans cet article](https://harperdb.io/blog/mean-stack-alternative/).

## Un défi pour vous 💪

Si vous actualisez la page de chat, le nom d'utilisateur et la salle de l'utilisateur seront perdus. Voyez si vous pouvez empêcher ces informations d'être perdues lorsque l'utilisateur actualise la page. Indice : le [stockage local](https://www.w3schools.com/html/html5_webstorage.asp) pourrait être utile !

## **Merci d'avoir lu !**

Si vous avez trouvé cet article utile, vous pouvez :

* [Vous abonner à ma chaîne YouTube](https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA). Je vais télécharger des tutoriels approfondis et des vidéos de projets sur React/NextJS/Node/Express.
* [Me suivre sur Twitter](https://twitter.com/doabledanny) où je tweete sur mon parcours de freelance, mes projets parallèles et mes apprentissages actuels.
* [Consulter ma boutique Gumroad](https://doabledanny.gumroad.com/) où je crée des aides-mémoire et des posters utiles et populaires (8000 téléchargements à ce jour).
* [Consulter mon blog de développement web](https://www.doabledanny.com/blog/)