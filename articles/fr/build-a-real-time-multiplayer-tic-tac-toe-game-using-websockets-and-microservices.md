---
title: Construire un jeu de Morpion multijoueur en temps réel en utilisant WebSockets
  et Microservices
subtitle: ''
author: Birkaran Sachdev
co_authors: []
series: null
date: '2024-11-18T21:55:22.147Z'
originalURL: https://freecodecamp.org/news/build-a-real-time-multiplayer-tic-tac-toe-game-using-websockets-and-microservices
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731400068976/3c951db9-929a-4d13-ba77-759932833a9a.jpeg
tags:
- name: SocketIO
  slug: socketio
- name: websockets
  slug: websockets
- name: Redis
  slug: redis
- name: Node.js
  slug: nodejs
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: Construire un jeu de Morpion multijoueur en temps réel en utilisant WebSockets
  et Microservices
seo_desc: In this tutorial, we’ll build a real-time multiplayer Tic-Tac-Toe game using
  Node.js, Socket.IO, and Redis. This game allows two players to connect from different
  browser tabs, take turns playing, and see real-time updates as they play. We'll
  use Red...
---

Dans ce tutoriel, nous allons construire un **jeu de Morpion multijoueur en temps réel** en utilisant **Node.js**, **Socket.IO** et **Redis**. Ce jeu permet à deux joueurs de se connecter depuis différents onglets de navigateur, de jouer à tour de rôle et de voir les mises à jour en temps réel pendant qu'ils jouent. Nous utiliserons **Redis** pour gérer la synchronisation de l'état du jeu sur plusieurs serveurs WebSocket, rendant notre application scalable.

À la fin, vous aurez un jeu entièrement fonctionnel avec des capacités en temps réel et une solide compréhension de l'utilisation des WebSockets et de Redis pour construire des applications scalables en temps réel.

### Ce que vous allez apprendre

* Comment utiliser **Socket.IO** pour la communication en temps réel.

* Comment utiliser **Redis Pub/Sub** pour synchroniser l'état du jeu sur plusieurs clients.

* Comment configurer une architecture de serveur WebSocket scalable.

### **Prérequis**

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* Node.js (v16 ou supérieur)

* Redis

* Docker (optionnel, pour exécuter Redis dans un conteneur)

* Connaissances de base en JavaScript, Node.js et WebSockets.

## **Table des matières**

* [Aperçu du projet](#heading-aperçu-du-projet)

* [Étape 1 : Configuration de votre environnement de développement](#heading-étape-1-configuration-de-votre-environnement-de-développement)

* [Étape 2 : Configuration du projet](#heading-étape-2-configuration-du-projet)

* [Étape 3 : Implémentation du serveur WebSocket avec Redis](#heading-étape-3-implémentation-du-serveur-websocket-avec-redis)

* [Étape 4 : Implémentation de l'interface frontend React](#heading-étape-4-implémentation-de-linterface-frontend-react)

* [Étape 5 : Exécution de l'application](#heading-étape-5-exécution-de-lapplication)

* [Étape 6 : Visualisation des messages Redis en temps réel](#heading-étape-6-visualisation-des-messages-redis-en-temps-réel)

* [Démonstration](#heading-démonstration)

* [Conclusion](#heading-conclusion)

## **Aperçu du projet**

Nous allons construire un jeu de Morpion en temps réel avec les fonctionnalités suivantes :

* **Deux joueurs** peuvent se connecter et jouer une partie.

* Le plateau de jeu se met à jour en temps réel sur différents onglets de navigateur.

* Le jeu annonce un gagnant ou déclare un match nul lorsque le plateau est rempli.

Nous utiliserons :

* **Node.js** avec **Socket.IO** pour gérer les connexions WebSocket.

* **Redis** Pub/Sub pour gérer la synchronisation de l'état du jeu entre les clients.

## **Étape 1 : Configuration de votre environnement de développement**

### **Installation de Node.js**

Assurez-vous que Node.js est installé sur votre système :

```bash
node -v
```

Si vous ne l'avez pas installé, téléchargez-le depuis [Node.js.](https://nodejs.org/en)

### **Installation de Redis**

Vous pouvez installer Redis localement ou l'exécuter dans un conteneur Docker.

#### **macOS (en utilisant Homebrew)**

Tout d'abord, assurez-vous que vous avez [Homebrew](https://brew.sh/) installé sur votre système avant d'exécuter les commandes ci-dessous :

```bash
brew install redis
brew services start redis
```

Vérifiez que le conteneur Redis est en cours d'exécution avec la commande suivante :

```bash
redis-cli ping
```

Vous devriez voir :

```bash
PONG
```

#### **Utilisation de Docker pour exécuter Redis**

```bash
docker run --name redis-server -p 6379:6379 -d redis
```

Vérifiez si Redis est en cours d'exécution en utilisant :

```bash
docker exec -it redis-server redis-cli ping
```

## **Étape 2 : Configuration du projet**

### **1. Création du répertoire du projet**

```bash
mkdir morpion
cd morpion
npm init -y
```

### **2. Installation des dépendances**

```bash
npm install express socket.io redis dotenv
```

### **3. Création des variables d'environnement**

Créez un fichier `.env` à la racine de votre projet avec le contenu suivant :

```bash
PORT=3000
REDIS_HOST=localhost
REDIS_PORT=6379
```

## **Étape 3 : Implémentation du serveur WebSocket avec Redis**

Dans cette étape, nous allons configurer un serveur WebSocket qui gère les interactions de jeu en temps réel en utilisant **Node.js**, **Socket.IO** et **Redis**. Ce serveur gérera l'état du jeu, traitera les mouvements des joueurs et assurera la synchronisation entre plusieurs clients en utilisant Redis Pub/Sub.

Nous allons décomposer chaque section du code pour que vous compreniez exactement comment tout s'assemble.**Explication du code du serveur**

Créez un fichier nommé `server.js` et ajoutez le code suivant :

```javascript
import dotenv from 'dotenv';
import express from 'express';
import http from 'http';
import { Server } from 'socket.io';
import { createClient } from 'redis';

dotenv.config(); // Charge les variables d'environnement depuis le fichier .env

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "http://localhost:5173",
    methods: ["GET", "POST"],
  }
});
```

* **dotenv** : Charge les variables d'environnement depuis un fichier `.env` pour garder les informations sensibles comme les ports et les clés en sécurité.

* **express** : Configure un serveur Express de base pour gérer les requêtes HTTP.

* **http** : Nous créons un serveur HTTP en utilisant le module intégré `http` de Node, que nous utiliserons avec **Socket.IO** pour la communication WebSocket.

* **Socket.IO** : Cette bibliothèque permet une communication en temps réel et bidirectionnelle entre le serveur et les clients.

* **Configuration CORS** : Permet les requêtes cross-origin depuis notre frontend s'exécutant sur `localhost:5173`.

Ensuite, pour créer des clients Redis publisher et subscriber, nous ajouterons le code suivant à `server.js` :

```javascript
// Initialiser les clients Redis
const pubClient = createClient();
const subClient = createClient();
await pubClient.connect();
await subClient.connect();
```

Nous utilisons **Redis** pour gérer la synchronisation des données en temps réel entre les clients connectés.

* **pubClient** : Utilisé pour publier des messages (comme les mises à jour de l'état du jeu).

* **subClient** : S'abonne aux messages (écoute les mises à jour).

* **connect()** : Établit une connexion au serveur Redis.

Dans ce paradigme, un client est utilisé pour publier les mises à jour, et l'autre s'abonne aux mises à jour. Cela aide à éviter les comportements de blocage, puisque les clients Redis en mode **subscribe** ne peuvent que recevoir des messages.

Pour s'abonner aux canaux Redis pour les mises à jour du jeu, nous ajouterons le code suivant à `server.js` :

```javascript
// S'abonner au canal Redis pour les mises à jour du jeu
await subClient.subscribe('mouvements-jeu', (message) => {
  gameState = JSON.parse(message);
  io.emit('etatJeu', gameState);
});
```

* **subClient.subscribe** : Écoute les messages sur le canal `mouvements-jeu`.

* Chaque fois qu'un nouveau mouvement est effectué par un joueur, l'état du jeu est mis à jour dans Redis, et tous les clients connectés sont informés du nouvel état.

* Le paramètre `message` contient l'état du jeu sous forme de chaîne. Nous le parsons en un objet JavaScript et diffusons l'état mis à jour en utilisant **Socket.IO**.

Ensuite, pour définir l'état du jeu et les fonctions, nous ajouterons le code suivant à `server.js` :

```javascript
// Définir l'état initial du jeu
let gameState = {
  board: Array(9).fill(null),
  xIsNext: true,
};

// Fonction pour réinitialiser le jeu
function resetGame() {
  gameState = {
    board: Array(9).fill(null),
    xIsNext: true,
  };
}
```

* **gameState** : Garde une trace de l'état actuel du plateau et de celui dont c'est le tour (`xIsNext`).

  * Le plateau est représenté comme un tableau de 9 cellules (chaque cellule peut être 'X', 'O', ou `null`).

  * Le drapeau `xIsNext` détermine de quel joueur c'est le tour.

* **resetGame()** : Réinitialise le plateau et l'indicateur de tour à leur état initial, permettant de commencer une nouvelle partie.

Ensuite, pour gérer les connexions WebSocket, ajoutons le code suivant à `server.js` :

```javascript
io.on('connection', (socket) => {
  console.log('Nouveau client connecté :', socket.id);

  // Envoyer l'état actuel du jeu au client nouvellement connecté
  socket.emit('etatJeu', gameState);
```

* L'événement `io.on('connection')` est déclenché lorsqu'un nouveau client se connecte.

* **socket.id** : Un identifiant unique pour chaque client connecté.

* Nous envoyons immédiatement l'état actuel `gameState` au nouveau client afin qu'il puisse voir le plateau actuel.

Pour gérer les mouvements des joueurs, nous ajouterons le code suivant à `server.js` :

```javascript
  // Gérer les mouvements des joueurs
  socket.on('faireMouvement', (index) => {
    // Empêcher de faire un mouvement si la cellule est déjà prise ou si le jeu est terminé
    if (gameState.board[index] || calculateWinner(gameState.board)) return;

    // Mettre à jour le plateau et changer de tour
    gameState.board[index] = gameState.xIsNext ? 'X' : 'O';
    gameState.xIsNext = !gameState.xIsNext;

    // Publier l'état mis à jour du jeu sur Redis
    pubClient.publish('mouvements-jeu', JSON.stringify(gameState));
    io.emit('etatJeu', gameState);
  });
```

* **faireMouvement** : Cet événement est déclenché lorsqu'un joueur clique sur une cellule.

  * **Validation** : Nous vérifions si la cellule est déjà occupée ou si le jeu est terminé avant de faire un mouvement.

  * **Mise à jour de l'état du jeu** : Si le mouvement est valide, nous mettons à jour le plateau et changeons de tour.

* L'état du jeu mis à jour est ensuite :

  1. **Publié sur Redis** : Cela garantit que toutes les instances du serveur restent synchronisées.

  2. **Diffusé à tous les clients** : Cela met immédiatement à jour le plateau de jeu pour tous les joueurs.

Pour gérer les redémarrages de jeu, nous ajouterons le code suivant à `server.js` :

```javascript
// Gérer les redémarrages de jeu
socket.on('redemarrerJeu', () => {
  resetGame();
  io.emit('etatJeu', gameState);
});
```

Pour gérer la déconnexion des clients, nous ajouterons le code suivant à `server.js` :

```javascript
 socket.on('disconnect', () => {
    console.log('Client déconnecté :', socket.id);
  });
});
```

Enfin, pour traiter la logique du jeu, nous ajouterons les fonctions suivantes à `server.js` :

```javascript
// Fonction pour vérifier s'il y a un gagnant
function calculateWinner(board) {
  const lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
  ];
  for (let [a, b, c] of lines) {
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return board[a];
    }
  }
  return null;
}

function isBoardFull(board) {
  return board.every((cell) => cell !== null);
}
```

* **calculateWinner()** : Vérifie s'il y a une combinaison gagnante sur le plateau.

* **isBoardFull()** : Vérifie si toutes les cellules sont remplies, indiquant un match nul.

## **Étape 4 : Implémentation de l'interface frontend React**

Dans cette étape, nous construisons une interface frontend React simple et interactive pour notre jeu de Morpion. Cette interface permet aux joueurs de se connecter au serveur WebSocket, de faire des mouvements et de voir le plateau de jeu se mettre à jour en temps réel.

Dans `App.jsx`, ajoutez le code suivant :

```javascript
import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:3000');

function App() {
  const [gameState, setGameState] = useState({
    board: Array(9).fill(null),
    xIsNext: true,
    winner: null
  });

  useEffect(() => {
    socket.on('etatJeu', (state) => {
      setGameState(state);
    });

    return () => socket.off('etatJeu');
  }, []);

  const handleClick = (index) => {
    if (gameState.board[index] || gameState.winner) return;
    socket.emit('faireMouvement', index);
  };

  const renderCell = (index) => (
    <button onClick={() => handleClick(index)}>{gameState.board[index]}</button>
  );

  return (
    <div>
      <h1>Morpion Multijoueur</h1>
      <div className="board">
        {[...Array(9)].map((_, i) => renderCell(i))}
      </div>
      <button onClick={() => socket.emit('redemarrerJeu')}>Redémarrer le jeu</button>
    </div>
  );
}

export default App;
```

Voici un résumé de la manière dont l'application React est décomposée :

* **Connexion WebSocket** :

  * Le frontend établit une connexion au serveur en utilisant `socket.io-client`.

* **Gestion de l'état** :

  * L'état du jeu (`gameState`) est géré avec `useState` de React et inclut :

    * Le **plateau** (9 cellules).

    * Le drapeau **xIsNext** pour indiquer le tour du joueur actuel.

    * Le statut du **gagnant**.

* **Mises à jour en temps réel** :

  * Le hook `useEffect` :

    * Écoute les mises à jour de `etatJeu` depuis le serveur.

    * Met à jour l'état local du jeu lorsque des changements sont détectés.

    * Nettoie l'écouteur WebSocket lorsque le composant est démonté.

* **Gestion des mouvements des joueurs** :

  * La fonction `handleClick` :

    * Vérifie si une cellule est déjà occupée ou si le jeu a un gagnant avant de permettre un mouvement.

    * Envoie un événement `faireMouvement` au serveur avec l'index de la cellule cliquée.

* **Rendu du plateau de jeu** :

  * La fonction `renderCell` crée un bouton pour chaque cellule du plateau.

  * Le plateau est affiché en utilisant une grille 3x3.

* **Redémarrer le jeu** :

  * Le bouton "Redémarrer le jeu" émet un événement `redemarrerJeu` pour réinitialiser le plateau de jeu pour tous les joueurs.

* **Interface utilisateur** :

  * Une disposition simple et interactive qui permet aux joueurs de jouer à tour de rôle et de voir les mises à jour en temps réel.

## **Étape 5 : Exécution de l'application**

### **Démarrage du backend**

Pour démarrer le serveur backend, ouvrez une nouvelle fenêtre de terminal et exécutez les commandes suivantes :

```bash
cd morpion
npm start
```

### **Démarrage du frontend**

Pour démarrer le serveur frontend React, ouvrez une nouvelle fenêtre de terminal et exécutez les commandes ci-dessous (n'utilisez pas la même que celle où le serveur backend est en cours d'exécution, car vous avez besoin des deux en cours d'exécution simultanément pour exécuter le jeu).

```bash
cd morpion-client
npm run dev
```

### **Accès au jeu**

Ouvrez votre navigateur et accédez à :

```bash
http://localhost:5173
```

## **Étape 6 : Visualisation des messages Redis en temps réel**

Pendant que le jeu est en cours, vous pouvez visualiser les messages Redis pour voir les mises à jour de l'état du jeu en temps réel.

Ouvrez un terminal et exécutez :

```bash
redis-cli
SUBSCRIBE mouvements-jeu
```

Cela affichera les mises à jour du jeu :

```bash
1) "message"
2) "mouvements-jeu"
3) "{\"board\":[\"X\",null,\"O\",null,\"X\",null,null,null,null],\"xIsNext\":false}"
```

Chaque fois qu'un mouvement est effectué ou que l'état du jeu change, le serveur publie l'état du jeu mis à jour sur le canal `mouvements-jeu`. En utilisant `redis-cli`, vous pouvez surveiller ces mises à jour en temps réel, pendant que le jeu est en cours.

## **Démonstration**

Dans cette démonstration, vous verrez le jeu de Morpion s'exécuter localement, démontrant les mises à jour en temps réel alors que les joueurs jouent à tour de rôle.

Le gameplay met en avant des fonctionnalités telles que le changement de tour, les mises à jour du plateau et les annonces de l'état du jeu (gagnant ou match nul). Cela met en lumière comment le jeu utilise la communication WebSocket pour offrir une expérience fluide et interactive.

%[https://www.youtube.com/watch?v=2aCllaBR6Xg&t=2s] 

## **Conclusion**

Félicitations, vous avez réussi à construire un jeu de Morpion multijoueur en temps réel en utilisant Node.js, Socket.IO et Redis. Voici ce que vous avez appris :

* Communication WebSocket en temps réel en utilisant **Socket.IO**.

* Gestion de l'état du jeu en utilisant **Redis Pub/Sub**.

* Construction d'un frontend réactif avec **React**.

### **Prochaines étapes**

* Ajouter une authentification des joueurs.

* Implémenter une fonctionnalité de chat.

* Déployer votre application sur un fournisseur cloud pour la scalabilité.

Bonne programmation !