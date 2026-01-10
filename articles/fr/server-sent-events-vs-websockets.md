---
title: Server-Sent Events vs WebSockets – Comment choisir un protocole d'échange de
  données en temps réel
subtitle: ''
author: Svitlana Lorman
co_authors: []
series: null
date: '2025-01-03T19:09:01.290Z'
originalURL: https://freecodecamp.org/news/server-sent-events-vs-websockets
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734440242816/4ba6ef33-386a-45f7-872b-5974742855e2.png
tags:
- name: development
  slug: development
- name: websockets
  slug: websockets
- name: Devops
  slug: devops
- name: Developer
  slug: developer
seo_title: Server-Sent Events vs WebSockets – Comment choisir un protocole d'échange
  de données en temps réel
seo_desc: 'In our fast-paced digital era, real-time data exchange has become critical
  in creating responsive and dynamic user experiences. It’s especially important in
  applications like live news updates, chat systems, AI generative platforms, and
  so on.

  In thi...'
---

Dans notre ère numérique rapide, l'échange de données en temps réel est devenu crucial pour créer des expériences utilisateur réactives et dynamiques. Cela est particulièrement important dans des applications comme les mises à jour d'actualités en direct, les systèmes de chat, les plateformes génératives d'IA, et ainsi de suite.

Dans cet article, vous apprendrez à connaître les **WebSockets** et les **Server-Sent Events (SSE)**, deux puissants protocoles de communication qui assurent des interactions en temps réel et fluides dans les applications web modernes.

En examinant leurs différences, avantages et cas d'utilisation, vous obtiendrez une compréhension claire de la manière de choisir le bon protocole pour optimiser la scalabilité et la performance. Cet article inclut également des exemples d'implémentations simples utilisant **Node.js**, vous permettant de voir ces technologies en action.

Pour vous aider à consolider vos connaissances, nous conclurons avec des recommandations de projets pratiques, offrant des opportunités concrètes d'appliquer ce que vous avez appris.

## Table des matières

1. [Qu'est-ce qu'un WebSocket ?](#heading-quest-ce-quun-websocket)
    
2. [Avantages et inconvénients des WebSockets](#heading-avantages-des-websockets)
    
3. [Cas d'utilisation des WebSockets](#heading-cas-dutilisation-des-websockets)
    
4. [Comment créer un serveur WebSocket avec Node.js](#heading-comment-creer-un-serveur-websocket-avec-nodejs)
    
5. [Qu'est-ce que les Server-Sent Events (SSE) ?](#heading-quest-ce-que-les-server-sent-events-sse)
    
6. [Avantages et inconvénients des Server-Sent Events](#heading-avantages-des-server-sent-events)
    
7. [Cas d'utilisation des SSE](#heading-cas-dutilisation-des-sse)
    
8. [Comment implémenter les Server-Sent Events en utilisant Node.js](#heading-comment-implementer-les-server-sent-events-en-utilisant-node-js)
    
9. [WebSockets vs Server-Sent Events](#heading-websockets-vs-server-sent-events)
    
10. [Lequel est le meilleur : Server-Sent Events ou WebSockets ?](#heading-lequel-est-le-meilleur-server-sent-events-ou-websockets)
    
11. [Conclusion](#heading-conclusion)
    

## **Qu'est-ce qu'un WebSocket ?**

En bref, un WebSocket est un protocole de communication qui permet des connexions full-duplex, à faible latence et pilotées par événements entre le serveur et le navigateur. Si vous n'êtes pas familier avec le terme, full-duplex fait référence à la capacité d'envoyer et de recevoir des données simultanément entre un client (comme un navigateur web) et un serveur sur une seule connexion.

Contrairement à [HTTP](https://www.freecodecamp.org/news/what-is-http/), qui fonctionne selon un modèle de requête-réponse, les WebSockets permettent un échange de données persistant et continu. Cela signifie que les données sont échangées en temps réel, et il n'est pas nécessaire de les extraire du serveur à chaque fois.

Le protocole WebSockets a été formalisé en 2011 par l'IETF via la RFC 6455 et est désormais supporté par tous les principaux navigateurs (Chrome, Edge, Safari, etc.).

Bien que les WebSockets diffèrent de HTTP, les deux protocoles fonctionnent sur la couche Application (couche 7) du [modèle OSI](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/) et s'appuient sur [TCP/IP](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/) au niveau de la couche Transport (couche 4). Le modèle OSI (Open Systems Interconnection) est un cadre conceptuel utilisé pour comprendre la communication réseau. Il divise le réseau en 7 couches, chacune responsable d'une fonction spécifique, allant de la transmission physique des données aux interactions de niveau applicatif.

De manière similaire à HTTP et HTTPS, les WebSockets ont un ensemble unique de préfixes :

* **ws** : indique une connexion non cryptée sans TLS et ne doit pas être ouverte depuis des sites sécurisés HTTPS.
    
* **wss** : indique une connexion cryptée sécurisée par TLS et ne doit pas être ouverte depuis des sites HTTP (non sécurisés).
    

### **Comment fonctionnent les WebSockets ?**

Comme je l'ai mentionné précédemment, les WebSockets établissent une connexion persistante et bidirectionnelle entre le client et le serveur. Le processus commence par une poignée de main HTTP initiée par le client, où le client demande une connexion WebSocket en envoyant un en-tête spécifique au serveur. Si le serveur accepte la demande, il répond avec un code de statut 101 confirmant la mise à niveau vers une connexion WebSocket.

Une fois la connexion établie, le protocole WebSocket prend le relais, et le client et le serveur peuvent envoyer et recevoir des données à tout moment sans avoir besoin de poignées de main répétées. Cette connexion continue permet une communication en temps réel avec une latence minimale, car les données sont échangées immédiatement sans attendre de demandes supplémentaires.

La connexion WebSocket reste ouverte jusqu'à ce que le client ou le serveur décide de la fermer. Cela garantit un échange de données efficace et rapide, ce qui en fait un choix idéal pour les applications en temps réel comme les systèmes de chat, les jeux en ligne ou les flux de données en direct.

![Connexion client-serveur full-duplex WebSocket](https://cdn.hashnode.com/res/hashnode/image/upload/v1735898910124/24538662-d00f-4457-a8a4-9da16f618046.png align="center")

### **Avantages des WebSockets**

* **Connexion full-duplex** : le client et le serveur peuvent envoyer et recevoir des données simultanément.
    
* **Faible latence** : puisque les WebSockets maintiennent une connexion ouverte, ils garantissent un délai minimal dans le transfert de données en éliminant le surcoût de l'établissement et de la rupture répétée des connexions, assurant ainsi un délai minimal dans le transfert de données.
    
* **Utilisation réduite de la bande passante** : contrairement aux requêtes HTTP, qui incluent des en-têtes pour chaque requête, les WebSockets ne nécessitent qu'une seule poignée de main, ce qui entraîne des paquets de données plus petits et une consommation réduite de la bande passante.
    
* **Compatibilité multiplateforme** : comme mentionné précédemment, les WebSockets sont supportés par la plupart des navigateurs modernes et des frameworks de programmation, ce qui garantit une large applicabilité.
    

### **Inconvénients des WebSockets**

* **Complexité de l'implémentation** : les WebSockets nécessitent un serveur dédié et un protocole spécial.
    
* **Vulnérabilité aux attaques** : sans une sécurité appropriée (préfixe wss) et des mécanismes d'authentification, les WebSockets sont sensibles au [détournement de WebSocket intersites](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking) (CSWSH) et aux attaques de [l'homme du milieu (MITM)](https://www.ibm.com/think/topics/man-in-the-middle).
    
* **Aucune sécurité intégrée** : contrairement à HTTP, les WebSockets ne supportent pas intrinsèquement les en-têtes de requête-réponse pour une sécurité supplémentaire. Ainsi, il est nécessaire d'implémenter manuellement une authentification basée sur des jetons ou d'autres méthodes sécurisées.
    

## **Cas d'utilisation des WebSockets**

Les WebSockets ont révolutionné la manière dont les applications fournissent une communication en temps réel. Ce protocole alimente diverses industries en permettant un flux de données bidirectionnel à faible latence. Parlons de quelques bons cas d'utilisation pour les WebSockets :

### 1. Applications de chat

La connexion full-duplex des WebSockets garantit que les messages sont livrés instantanément et sans interruption, ce qui en fait le choix parfait pour la communication en temps réel. Cette technologie alimente des plateformes comme Slack, Discord et divers systèmes de chat de support client en direct, offrant des interactions fluides et efficaces.

### 2. Jeux en ligne

Les WebSockets sont essentiels pour les jeux en ligne rapides comme Clash Royal, où la communication en temps réel entre les joueurs et les serveurs est cruciale. En maintenant une connexion persistante et bidirectionnelle, les WebSockets permettent une transmission immédiate des actions, telles que les mouvements ou les attaques, garantissant que tous les joueurs bénéficient d'un gameplay fluide sans latence.

### 3. Tableaux de bord en temps réel

Des outils comme Datadog et les plateformes de commerce électronique utilisent les WebSockets pour garantir que les métriques système, les ventes et les données d'inventaire sont toujours à jour, éliminant ainsi les actualisations manuelles et améliorant l'expérience utilisateur.

Les WebSockets excellent également dans la gestion des big data, le streaming et la visualisation de grands volumes d'informations avec une faible latence. Cela en fait le choix parfait pour des industries telles que la finance, la santé et la logistique, où des informations en temps réel sont essentielles pour une prise de décision efficace.

Un exemple est DataTableDev, un prototype de grille capable de travailler avec des volumes de données massifs, démontrant le potentiel des WebSockets dans le traitement des données en temps réel.

## **Comment créer un serveur WebSocket avec Node.js**

Avant de configurer un simple serveur WebSocket avec Node.js pour gérer des connexions sécurisées, vous aurez besoin d'un [certificat TLS](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) pour garantir que la communication est cryptée. Vous pouvez en obtenir un auprès d'une autorité de certification (CA) de confiance comme [Let's Encrypt](https://letsencrypt.org/) ou utiliser un certificat auto-signé pour les tests.

Voici l'implémentation complète d'un serveur WebSocket Secure (WSS) utilisant Node.js :

Nous commencerons par le côté serveur. Tout d'abord, importons les modules requis :

```javascript
const https = require('https');  // Module pour créer un serveur HTTPS
const fs = require('fs');        // Module pour lire les fichiers (utilisé pour charger les certificats TLS)
const WebSocket = require('ws'); // Bibliothèque WebSocket pour gérer les connexions WebSocket
```

Ensuite, nous chargerons les certificats TLS pour une communication sécurisée (wss://).

```javascript
const serverOptions = {
  cert: fs.readFileSync('cert.pem'), // Charge le certificat TLS pour le cryptage HTTPS
  key: fs.readFileSync('key.pem'),   // Charge la clé privée associée au certificat
};
```

`serverOptions` lit le certificat TLS et la clé privée à partir des fichiers (`cert.pem` et `key.pem`) et les conserve. Ces éléments sont essentiels pour établir une communication sécurisée en utilisant le protocole `wss://` car ils permettent le **cryptage** des données transmises entre le serveur et le client.

Étant donné que le serveur WebSocket fonctionne par-dessus le serveur HTTPS, nous créons et initialisons d'abord le serveur HTTPS en utilisant les `serverOptions`, puis nous configurons le serveur WebSocket.

```javascript
// Crée le serveur HTTPS avec les certificats chargés et l'initialise avec les options TLS
const httpsServer = https.createServer(serverOptions); 
// Crée un serveur WebSocket qui fonctionne par-dessus le serveur HTTPS
const wss = new WebSocket.Server({ server: httpsServer }); 
```

Il est maintenant temps de définir le comportement lorsqu'une nouvelle connexion WebSocket est établie. Vous devrez gérer les messages entrants du client WebSocket, envoyer une réponse en retour et gérer le processus de déconnexion. Dans ce tutoriel, nous garderons cela simple en imprimant les données reçues dans la console.

```javascript
// Définir le comportement lorsqu'une nouvelle connexion WebSocket est établie
wss.on('connection', (ws) => {
  console.log('Client connecté');

  // Gérer les messages entrants du client WebSocket
  ws.on('message', (message) => {
    console.log(`Reçu : ${message}`); 
    ws.send(`Serveur reçu : ${message}`); // Envoyer une réponse au client
  });

  // Gérer lorsqu'un client se déconnecte
  ws.on('close', () => {
    console.log('Client déconnecté');

  // Envoyer un message initial au client lorsque la connexion est établie
  ws.send('Bienvenue sur le serveur WebSocket sécurisé !');
});
```

Enfin, vous devez définir le port où le serveur WebSocket HTTPS écoutera les connexions entrantes. Dans cet exemple, nous utilisons le port `8080`. Après cela, nous démarrons le serveur HTTPS et le faisons écouter sur le port spécifié. Une fois le serveur opérationnel, un message de journalisation sera imprimé pour confirmer que le serveur WebSocket sécurisé est prêt.

```javascript
// Définir le port où le serveur WebSocket HTTPS écoutera les connexions entrantes
const PORT = 8080;

// Démarrer le serveur HTTPS et commencer à écouter sur le port spécifié
httpsServer.listen(PORT, () => {
  console.log(`Serveur WebSocket sécurisé en cours d'exécution à wss://localhost:${PORT}`); // Journaliser un message lorsque le serveur démarre
});
```

Et c'est tout pour la partie côté serveur. Votre code complet devrait ressembler à ceci :

```javascript
// Importer les modules requis
const https = require('https');  // Module pour créer un serveur HTTPS
const fs = require('fs');        // Module pour lire les fichiers (utilisé pour charger les certificats TLS)
const WebSocket = require('ws'); // Bibliothèque WebSocket pour gérer les connexions WebSocket

// Charger les certificats TLS pour une communication sécurisée (wss://)
const serverOptions = {
  cert: fs.readFileSync('cert.pem'), // Charge le certificat TLS pour le cryptage HTTPS
  key: fs.readFileSync('key.pem'),   // Charge la clé privée associée au certificat
};

// Créer le serveur HTTPS avec les certificats chargés et l'initialiser avec les options TLS
const httpsServer = https.createServer(serverOptions); 
// Créer un serveur WebSocket qui fonctionne par-dessus le serveur HTTPS
const wss = new WebSocket.Server({ server: httpsServer }); 

// Définir le comportement lorsqu'une nouvelle connexion WebSocket est établie
wss.on('connection', (ws) => {
  console.log('Client connecté'); 

  // Gérer les messages entrants du client WebSocket
  ws.on('message', (message) => {
    console.log(`Reçu : ${message}`); 
    ws.send(`Serveur reçu : ${message}`); // Envoyer une réponse au client
  });

  // Gérer lorsqu'un client se déconnecte
  ws.on('close', () => {
    console.log('Client déconnecté'); 
  });
  // Envoyer un message initial au client lorsque la connexion est établie
  ws.send('Bienvenue sur le serveur WebSocket sécurisé !');
});

// Définir le port où le serveur WebSocket HTTPS écoutera les connexions entrantes
const PORT = 8080;

// Démarrer le serveur HTTPS et commencer à écouter sur le port spécifié
httpsServer.listen(PORT, () => {
  console.log(`Serveur WebSocket sécurisé en cours d'exécution à wss://localhost:${PORT}`); // Journaliser un message lorsque le serveur démarre
});
```

Pour exécuter le serveur créé avec Node.js, tapez la ligne suivante dans l'invite de commande / Terminal :

`node wss-server.js`

Connectez-vous au serveur en utilisant un client WebSocket ou la console du navigateur à l'adresse `wss://`[`localhost:8080`](http://localhost:8080).

Une fois la connexion établie, le client peut envoyer et recevoir des messages. Nous allons maintenant examiner un exemple simple de la manière de recevoir et d'envoyer des messages côté client.

Pour commencer, définissons une structure HTML de base :

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Client WebSocket</title>
</head>
<body>
  <h1>Client WebSocket</h1>
  <div id="messages"></div>
  <input type="text" id="messageInput" placeholder="Tapez un message">
  <button onclick="sendMessage()">Envoyer le message</button>

  <script>
    <!-- Le code JS va ici -->
  </script>
</body>
</html>
```

L'élément `<button>` a un événement `onclick` qui déclenche la fonction `sendMessage()` lorsqu'il est cliqué. Avant de plonger dans la fonction, établissons d'abord une connexion WebSocket avec le serveur. Nous définirons également des écouteurs d'événements pour gérer les cas suivants :

1. Lorsque la connexion WebSocket est établie avec succès.
    
2. Lorsqu'un message est reçu du serveur.
    

Ces écouteurs d'événements garantiront que nous pouvons interagir avec le serveur et traiter les données entrantes en temps réel.

```javascript
    // Établir une connexion WebSocket avec le serveur
    const socket = new WebSocket('wss://localhost:8080'); 

    // Écouteur d'événement pour lorsque la connexion WebSocket est établie
    socket.addEventListener('open', () => {
      displayMessage('Connecté au serveur WebSocket');

    // Écouteur d'événement pour lorsqu'un message est reçu du serveur
    socket.addEventListener('message', (event) => {
      displayMessage(`Serveur : ${event.data}`); // Afficher le message reçu du serveur
    });
```

Pour afficher le message sur l'interface utilisateur, nous avons créé une fonction appelée `displayMessage`. Voici comment elle est définie :

```javascript
// Fonction pour afficher les messages dans le conteneur de messages
function displayMessage(message) {
      const messageDiv = document.getElementById('messages'); // Obtenir le div où les messages seront affichés
      const newMessage = document.createElement('p'); // Créer un nouvel élément de paragraphe pour le nouveau message
      newMessage.textContent = message; // Définir le contenu textuel du paragraphe sur le message
      messageDiv.appendChild(newMessage); // Ajouter le nouveau paragraphe au conteneur de messages
}
```

Il est maintenant temps de définir la fonction `sendMessage()`. Tout d'abord, nous récupérons un message, puis nous l'envoyons au serveur WebSocket en utilisant la méthode `socket.send()`. Cela transmet le message via la connexion WebSocket établie précédemment, permettant au serveur de le recevoir. Ensuite, sur l'interface utilisateur, nous affichons le message et effaçons le champ de saisie.

Ainsi, le code ressemble à ceci :

```javascript
    // Fonction pour envoyer un message au serveur
    function sendMessage() {
      const message = document.getElementById('messageInput').value; // Obtenir le message du champ de saisie
      socket.send(message); // Envoyer le message via la connexion WebSocket
      displayMessage(`Vous : ${message}`); // Afficher le message dans l'interface utilisateur comme envoyé par l'utilisateur
      document.getElementById('messageInput').value = ''; // Effacer le champ de saisie après l'envoi du message
    }
```

La dernière étape consiste à définir l'écouteur d'événement pour la fermeture de la connexion WebSocket. Pour garder cela simple, nous allons journaliser un message dans la console.

```javascript
 socket.addEventListener('close', () => {
      console.log('Déconnecté du serveur WebSocket'); 
 });
```

Voici à quoi ressemble la partie côté client :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Client WebSocket</title>
</head>
<body>
  <h1>Client WebSocket</h1>
  <div id="messages"></div>
  <input type="text" id="messageInput" placeholder="Tapez un message">
  <button onclick="sendMessage()">Envoyer le message</button>

  <script>
    // Établir une connexion WebSocket avec le serveur
    const socket = new WebSocket('wss://localhost:8080'); // Connexion au serveur WebSocket 

    // Écouteur d'événement pour lorsque la connexion WebSocket est établie
    socket.addEventListener('open', () => {
      displayMessage('Connecté au serveur WebSocket');

    // Écouteur d'événement pour lorsqu'un message est reçu du serveur
    socket.addEventListener('message', (event) => {
      displayMessage(`Serveur : ${event.data}`); // Afficher le message reçu du serveur
    });

    // Fonction pour envoyer un message au serveur
    function sendMessage() {
      const message = document.getElementById('messageInput').value; // Obtenir le message du champ de saisie
      socket.send(message); // Envoyer le message via la connexion WebSocket
      displayMessage(`Vous : ${message}`); // Afficher le message dans l'interface utilisateur comme envoyé par l'utilisateur
      document.getElementById('messageInput').value = ''; // Effacer le champ de saisie après l'envoi du message
    }

    // Fonction pour afficher les messages dans le conteneur de messages
    function displayMessage(message) {
      const messageDiv = document.getElementById('messages'); // Obtenir le div où les messages seront affichés
      const newMessage = document.createElement('p'); // Créer un nouvel élément de paragraphe pour le nouveau message
      newMessage.textContent = message; // Définir le contenu textuel du paragraphe sur le message
      messageDiv.appendChild(newMessage); // Ajouter le nouveau paragraphe au conteneur de messages
    }

    // Écouteur d'événement pour lorsque la connexion WebSocket est fermée
    socket.addEventListener('close', () => {
      console.log('Déconnecté du serveur WebSocket'); 
    });
  </script>
</body>
</html>
```

## **Qu'est-ce que les Server-Sent Events (SSE) ?**

Les Server-Sent Events (SSE) sont une technologie qui permet à un serveur web de pousser des mises à jour vers une page web. Faisant partie de la spécification HTML5, ils fonctionnent de manière similaire aux WebSockets en utilisant une seule connexion HTTP longue durée pour fournir des données en temps réel.

Le concept de SSE est apparu en 2004, avec l'équipe d'[Opera](https://blogs.opera.com/news/) qui a fait les premiers pas vers l'implémentation en 2006. L'une des principales limitations des SSE dans les premiers stades était la limite de connexion imposée par HTTP/1.1, qui restreignait le nombre de connexions simultanées qu'un client pouvait établir avec un serveur. Mais avec l'introduction de HTTP/2, cette limitation a été supprimée. HTTP/2 permet à plusieurs flux de données de circuler sur une seule connexion grâce au multiplexage, permettant une communication plus efficace et scalable pour les SSE.

Les événements envoyés par le serveur (SSE) reposent sur deux composants fondamentaux :

* **EventSource** : Une interface définie par la spécification WHATWG et implémentée par les navigateurs modernes. Elle permet au client (généralement un navigateur) de s'abonner aux événements envoyés par le serveur.
    

* **EventStream** : Un protocole qui spécifie le format en texte brut que les serveurs doivent utiliser pour envoyer des événements, garantissant la compatibilité avec le client EventSource pour une communication fluide.
    

Comme le précise la spécification, les événements peuvent inclure des données textuelles arbitraires et un ID optionnel, et sont séparés par des nouvelles lignes. De plus, les événements SSE ont un type [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types) dédié : `text/event-stream`. Un type MIME (Multipurpose Internet Mail Extensions type) est une norme qui indique la nature et le format d'un fichier ou de données, permettant au navigateur ou au serveur de les interpréter et de les traiter correctement.

### **Comment fonctionnent les Server-Sent Events ?**

Les événements envoyés par le serveur (SSE) fonctionnent en établissant un canal de communication unidirectionnel persistant du serveur vers le client sur une connexion HTTP standard. Le client initie la connexion en créant un objet `EventSource`, qui envoie une requête au serveur pour commencer à diffuser des données. Une fois que le serveur reçoit cette requête, il répond en envoyant un flux continu de mises à jour dans un format spécifique `text/event-stream`. Le client écoute ces événements, gérant automatiquement toute reconnexion si la connexion est perdue.

SSE est idéal pour les applications qui nécessitent des mises à jour en temps réel du serveur, comme les flux d'actualités en direct ou les notifications, car il garantit un flux constant d'informations avec un minimum de surcharge.

![Cette image montre comment fonctionne SSE](https://cdn.hashnode.com/res/hashnode/image/upload/v1735897258671/eec0599a-f5b5-43f2-8552-7f84ac265c3e.png align="center")

### **Avantages des Server-Sent Events**

* **Capacité de polyfill** : Les événements envoyés par le serveur (SSE) peuvent être implémentés en utilisant JavaScript dans les navigateurs qui ne les supportent pas nativement. Cela garantit une compatibilité ascendante en utilisant l'interface SSE standard au lieu de créer une alternative personnalisée.
    
* **Reconnexion automatique** : Les connexions SSE sont conçues pour se reconnecter automatiquement après une interruption. Ainsi, elles réduisent le besoin de code supplémentaire pour gérer cette fonctionnalité essentielle.
    
* **Compatibilité avec les pare-feu** : Les SSE fonctionnent de manière transparente avec les pare-feu d'entreprise qui effectuent une inspection des paquets, ce qui en fait un choix fiable pour les applications d'entreprise.
    

### **Inconvénients des Server-Sent Events**

* **Restrictions de format de données** : SSE est limité à la transmission de messages au format UTF-8, car il ne supporte pas les données binaires.
    
* **Limites de connexion** : Les navigateurs limitent le nombre de connexions SSE simultanées à six par client. Cette limitation devient problématique lorsque plusieurs onglets nécessitent des connexions SSE actives. Pour plus de détails et des solutions potentielles, consultez ce fil StackOverflow : [Server-Sent Events et limites des navigateurs](https://stackoverflow.com/questions/18584525/server-sent-events-and-browser-limits).
    
* **Communication unidirectionnelle** : SSE ne supporte que la messagerie du serveur vers le client, ce qui en fait un choix idéal pour les applications en temps réel en lecture seule comme les cours de bourse. Cependant, cette nature unidirectionnelle peut être une contrainte pour des applications en temps réel plus interactives.
    

## **Cas d'utilisation des SSE**

Les événements envoyés par le serveur sont largement utilisés dans des applications où la livraison de données en temps réel est cruciale. SSE permet au serveur de pousser des mises à jour vers le client automatiquement, ce qui en fait un choix idéal pour les applications nécessitant des flux d'informations en direct. Des flux d'actualités aux tableaux de bord financiers, SSE garantit que les utilisateurs reçoivent le contenu le plus récent sans actualisations constantes de la page.

Voici quelques cas d'utilisation courants pour SSE :

### 1. Flux de réseaux sociaux

Les plateformes de réseaux sociaux utilisent SSE pour pousser instantanément de nouveaux posts, likes et commentaires vers les flux des utilisateurs, offrant une expérience utilisateur plus dynamique et engageante. Un excellent exemple est l'implémentation du flux en temps réel de Twitter (X), qui leur permet de pousser des mises à jour en temps réel vers le navigateur.

### 2. Système de surveillance d'entreprise

SSE permet aux systèmes de surveillance financière et autres applications en temps réel de fournir des mises à jour de données en direct de manière efficace. Par exemple, le Hystrix open-source de Netflix, un composant bien connu pour la surveillance des microservices et la rupture de circuit, inclut un tableau de bord web qui affiche les métriques de performance en temps réel et l'état du circuit. Ce tableau de bord utilise SSE pour pousser les données de performance en temps réel, garantissant que les utilisateurs peuvent surveiller la santé et les performances des microservices au fur et à mesure qu'ils se produisent. Le tableau de bord utilisant SSE fournit une solution efficace et à faible latence pour la mise à jour des données de performance sans nécessiter d'actualisations manuelles constantes ou de sondage.

### 3. IA générative

La technologie SSE joue un rôle clé en coulisses lors de l'interaction avec des chatbots d'IA générative comme ChatGPT et Gemini. Par exemple, lorsqu'un utilisateur demande à ChatGPT d'écrire un article sur un sujet spécifique, le serveur commence à traiter la demande et génère l'article progressivement, souvent par morceaux plutôt que d'un seul coup.

Pendant ce processus, le serveur de ChatGPT utilise SSE pour pousser chaque partie de l'article vers le client en temps réel, permettant à l'utilisateur de voir le contenu apparaître au fur et à mesure de sa génération.

## **Comment implémenter les Server-Sent Events en utilisant Node.js**

Dans cette section, nous allons explorer comment implémenter SSE en utilisant Node.js, un environnement d'exécution JavaScript populaire, pour pousser des mises à jour vers le client en temps réel. Nous allons configurer un serveur de base et envoyer des données en direct au navigateur en utilisant SSE.

Nous commencerons par le côté client (HTML/JavaScript). Tout d'abord, nous allons créer un nouvel objet `EventSource` pour écouter les événements du serveur.

```javascript
const evtSource = new EventSource("sse-demo.js");
```

L'URL `"sse-demo.js"` est le chemin vers le script côté serveur qui générera les événements. Mais si le script générateur d'événements était hébergé sur une origine différente, nous devrions fournir une configuration supplémentaire pour les requêtes cross-origin.

```javascript
// Si le script générateur d'événements est hébergé sur une origine différente (requête cross-origin) :
const evtSource = new EventSource("//api.example.com/sse-demo.js", {
  withCredentials: true,  // Envoie des cookies, des en-têtes d'autorisation avec la requête au serveur
});
```

Cette version garantit que les cookies et les en-têtes d'autorisation sont envoyés avec la requête, permettant une communication sécurisée et s'assurant que les informations d'identification peuvent être incluses dans les requêtes cross-origin. `withCredentials: true` garantit que l'authentification est gérée correctement si nécessaire.

Ensuite, configurons un écouteur d'événements pour gérer le message lorsqu'il est reçu. Pour garder les choses simples, nous afficherons le message sur l'interface utilisateur en l'ajoutant comme un nouvel élément de liste.

```javascript
// Lorsqu'un événement de message est reçu
evtSource.onmessage = (event) => {
  // Créer un nouvel élément de liste pour afficher le message
  const newElement = document.createElement("li");

  // Obtenir la référence à l'élément de liste non ordonnée où les messages seront affichés
  const eventList = document.getElementById("list");

  // Définir le contenu textuel du nouvel élément de liste sur le message reçu
  newElement.textContent = `message : ${event.data}`;

  // Ajouter le nouvel élément de liste à la liste d'événements (ul) dans le HTML
  eventList.appendChild(newElement);
};
```

Ajoutons également un écouteur d'événements pour un événement personnalisé "ping". Encore une fois, nous ajouterons simplement de nouvelles données à la liste et les afficherons sur la page. Ainsi, lorsqu'un événement personnalisé est reçu, un nouvel élément de liste (`<li>`) est créé.

Les données de l'événement, qui contiennent une propriété `time`, sont analysées à partir de JSON, et le temps est affiché dans l'élément de liste. Ce nouvel élément de liste est ensuite ajouté à une liste non ordonnée (`<ul>`) dans le HTML, permettant d'afficher les données de l'événement "ping" sur l'interface utilisateur.

```javascript
// Ajouter un écouteur d'événements pour un type d'événement personnalisé, "ping"
evtSource.addEventListener("ping", (event) => {
  // Créer un nouvel élément de liste pour afficher l'événement ping
  const newElement = document.createElement("li");

  // Obtenir la référence à l'élément de liste non ordonnée où les événements ping seront affichés
  const eventList = document.getElementById("list");

  // Analyser les données de l'événement en tant que JSON (en supposant qu'elles contiennent une propriété time)
  const time = JSON.parse(event.data).time;

  // Définir le contenu textuel du nouvel élément de liste pour afficher le temps de ping
  newElement.textContent = `ping à ${time}`;

  // Ajouter le nouvel élément de liste à la liste d'événements (ul) dans le HTML
  eventList.appendChild(newElement);
});
```

Assurez-vous que votre code pour la partie côté client ressemble à ceci :

```javascript
// Créer un nouvel EventSource pour écouter les événements du serveur
const evtSource = new EventSource("sse-demo.js");

/* Si le script générateur d'événements est hébergé sur une origine différente (requête cross-origin) :
const evtSource = new EventSource("//api.example.com/sse-demo.js", {
  withCredentials: true,  // Envoie des cookies, des en-têtes d'autorisation avec la requête au serveur
});
*/
// Lorsqu'un événement de message est reçu
evtSource.onmessage = (event) => {
  // Créer un nouvel élément de liste pour afficher le message
  const newElement = document.createElement("li");

  // Obtenir la référence à l'élément de liste non ordonnée où les messages seront affichés
  const eventList = document.getElementById("list");

  // Définir le contenu textuel du nouvel élément de liste sur le message reçu
  newElement.textContent = `message : ${event.data}`;

  // Ajouter le nouvel élément de liste à la liste d'événements (ul) dans le HTML
  eventList.appendChild(newElement);
};

// Ajouter un écouteur d'événements pour un type d'événement personnalisé, "ping"
evtSource.addEventListener("ping", (event) => {
  // Créer un nouvel élément de liste pour afficher l'événement ping
  const newElement = document.createElement("li");

  // Obtenir la référence à l'élément de liste non ordonnée où les événements ping seront affichés
  const eventList = document.getElementById("list");

  // Analyser les données de l'événement en tant que JSON (en supposant qu'elles contiennent une propriété time)
  const time = JSON.parse(event.data).time;

  // Définir le contenu textuel du nouvel élément de liste pour afficher le temps de ping
  newElement.textContent = `ping à ${time}`;

  // Ajouter le nouvel élément de liste à la liste d'événements (ul) dans le HTML
  eventList.appendChild(newElement);
});
```

Maintenant, codons la partie côté serveur avec Node.js et Express.js. Express est un framework d'application web minimal et flexible pour Node.js. Il simplifie la création d'applications côté serveur en fournissant des fonctionnalités robustes comme le routage, le support des middlewares et la gestion des requêtes et réponses HTTP. Il aide à rationaliser le développement des API web et des sites web, ce qui en fait un choix parfait pour notre tutoriel.

Notez que vous devrez vous rendre sur la [documentation officielle d'Express.js](https://expressjs.com) et l'installer sur votre machine si vous ne l'avez pas déjà installée.

Ensuite, rendez-vous dans l'IDE et importez le module Express, ce qui nous permet de créer une instance de l'application Express.

```javascript
// Importer le module Express
const express = require('express');
// Créer une instance de l'application Express
const app = express();
```

Il est considéré comme une bonne pratique de spécifier le numéro de port en haut du fichier pour faciliter la configuration et la modification ultérieure. Cette approche améliore la lisibilité et la maintenabilité du code, vous permettant de changer rapidement le numéro de port sans avoir à chercher dans tout le fichier. Cela permet également une meilleure flexibilité lors du déploiement de l'application dans différents environnements (par exemple, développement, staging, production).

Pour ce tutoriel, nous avons défini le numéro de port à `3000`.

```javascript
// Définir le numéro de port pour que le serveur écoute
const port = 3000;
```

Maintenant, configurons la partie côté serveur avec Node.js et Express pour gérer les requêtes SSE. Nous définissons une route (`/sse`) qui enverra un flux continu d'événements au client.

```javascript
// Définir une route qui gère les requêtes vers le point de terminaison /sse
app.get('/sse', (req, res) => {
//....
});
```

Pour que le serveur communique avec le client en utilisant SSE, nous devons définir des en-têtes HTTP spécifiques :

* **Content-Type** : Nous spécifions `'text/event-stream'` pour informer le client que la réponse est un flux SSE.
    
* **Cache-Control** : Le définir à `'no-cache'` garantit que le client reçoit des données fraîches à chaque fois, sans mise en cache.
    
* **Connection** : Cela est défini à `'keep-alive'` pour maintenir la connexion ouverte pour une transmission continue des données.
    

```javascript
app.get('/sse', (req, res) => {
  // Définir l'en-tête Content-Type à 'text/event-stream' pour indiquer que 
  // la réponse sera un flux SSE
  res.setHeader('Content-Type', 'text/event-stream');

  // Empêcher la mise en cache du flux (important pour garantir des mises à jour en temps réel)
  res.setHeader('Cache-Control', 'no-cache');

  // Maintenir la connexion active pour envoyer continuellement des événements
  res.setHeader('Connection', 'keep-alive');
});
```

Vous pouvez utiliser `res.flushHeaders()` pour envoyer les en-têtes immédiatement. Ainsi, le client peut commencer à écouter les événements sans délai.

Pour ajouter un peu de style, envoyons un nouveau message SSE chaque seconde, incluant le numéro du message envoyé. Pour cela, nous initialiserons une variable `counter`, ainsi que l'utilisation de `setInterval` pour envoyer un nouveau message chaque seconde (1000ms).

```javascript
app.get('/sse', (req, res) => {
  // Définir l'en-tête Content-Type à 'text/event-stream' pour indiquer que 
  // la réponse sera un flux SSE
  res.setHeader('Content-Type', 'text/event-stream');

  // Empêcher la mise en cache du flux (important pour garantir des mises à jour en temps réel)
  res.setHeader('Cache-Control', 'no-cache');

  // Maintenir la connexion active pour envoyer continuellement des événements
  res.setHeader('Connection', 'keep-alive');

  // Envoyer les en-têtes immédiatement, afin que le client commence à écouter les événements
  res.flushHeaders();

  // Initialiser une variable de compteur pour les messages
  let counter = 0;

  // Utiliser setInterval pour envoyer un nouveau message chaque seconde (1000ms)
  setInterval(() => {
    // Envoyer un nouveau message SSE, en incrémentant le compteur à chaque fois
    // Chaque message est précédé de 'data: ' et suivi du contenu du message
    res.write(`data: Ceci est le message ${counter++}\n\n`);
  }, 1000); // Cet intervalle s'exécute toutes les 1000 millisecondes (1 seconde)
});
```

La dernière étape consiste à démarrer le serveur Express de la manière suivante :

```javascript
app.listen(port, () => {
  console.log(`Serveur en cours d'exécution à http://localhost:${port}`);
});
```

Et c'est tout ! Assurez-vous que votre code côté serveur ressemble à ceci :

```javascript
// Importer le module Express
const express = require('express');
// Créer une instance de l'application Express
const app = express();

// Définir le numéro de port pour que le serveur écoute
const port = 3000;

// Définir une route qui gère les requêtes vers le point de terminaison /sse
app.get('/sse', (req, res) => {
  // Définir l'en-tête Content-Type à 'text/event-stream' pour indiquer que 
  // la réponse sera un flux SSE
  res.setHeader('Content-Type', 'text/event-stream');

  // Empêcher la mise en cache du flux (important pour garantir des mises à jour en temps réel)
  res.setHeader('Cache-Control', 'no-cache');

  // Maintenir la connexion active pour envoyer continuellement des événements
  res.setHeader('Connection', 'keep-alive');

  // Envoyer les en-têtes immédiatement, afin que le client commence à écouter les événements
  res.flushHeaders();

  // Initialiser une variable de compteur pour les messages
  let counter = 0;

  // Utiliser setInterval pour envoyer un nouveau message chaque seconde (1000ms)
  setInterval(() => {
    // Envoyer un nouveau message SSE, en incrémentant le compteur à chaque fois
    // Chaque message est précédé de 'data: ' et suivi du contenu du message
    res.write(`data: Ceci est le message ${counter++}\n\n`);
  }, 1000); // Cet intervalle s'exécute toutes les 1000 millisecondes (1 seconde)
});

// Démarrer le serveur Express et écouter sur le port spécifié
app.listen(port, () => {
  console.log(`Serveur en cours d'exécution à http://localhost:${port}`);
});
```

## **WebSockets vs Server-Sent Events**

L'objectif des méthodes de transfert de données est de charger et d'afficher de grands ensembles de données aussi rapidement que possible. Cela garantit que l'utilisateur perçoit la réponse comme instantanée et offre une navigation fluide et une expérience utilisateur agréable.

[Jakob Nielsen](https://www.nngroup.com/articles/author/jakob-nielsen/), un ancien principal et cofondateur du Nielsen Norman Group, a décrit trois limites de temps clés que les développeurs devraient considérer lors de l'optimisation des performances web et des applications dans son livre [Usability Engineering](https://www.nngroup.com/books/usability-engineering/). En bref, 0,1 seconde est le seuil pour que les utilisateurs ressentent que le système répond instantanément, ce qui signifie qu'aucun retour spécial n'est nécessaire autre que l'affichage du résultat.

[Vera Didenko](https://www.linkedin.com/in/vera-didenko/), architecte logiciel et développeur chez Flexmonster, a mené des recherches pour identifier le protocole de transfert de données le plus efficace et, sur la base de la contrainte de 100 millisecondes, a calculé le budget de temps pour chaque processus, choisissant finalement les WebSockets comme la méthode optimale pour charger et mettre à jour les données.

![Temps de réponse tolérable étendu de l'ingénierie de l'utilisabilité de Jakob Nielsen.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe5vtbDVh_QdPm4ajDMJ3Gc2l6sF-TZs4YhzZEXLbj0fbsm1iW71lNu7X7TGuu6uUnXZSUPsPWZPjviWFcYnSZFALba9qoGgbHICv6z635gn2Ie9pvYjsv3-n0M7aZCe6Hy7kXNpC5I4P6k0YBqBcg?key=p_cDJW9Yx9AjWig3CS4ijdeZ align="left")

À des fins de recherche, Vera a créé une application utilisant .NET Core et [SignalR](https://learn.microsoft.com/en-us/aspnet/signalr/overview/getting-started/introduction-to-signalr) pour tester et comparer visuellement les performances des WebSockets et des Server-Sent Events afin de découvrir quelle approche de transfert de données est la plus efficace en termes de performance. SignalR est une bibliothèque open-source qui simplifie la fonctionnalité web en temps réel.

Après avoir exécuté plusieurs tests pour toutes les méthodes simultanément tout en augmentant le nombre d'appels à chaque fois, les résultats des tests ont été recueillis au format JSON et alimentés à la [bibliothèque amCharts](https://www.amcharts.com/). Voici les résultats des tests pour 100, 1000 et 10000 appels :

![La performance des WebSockets et des Server-Sent Events](https://cdn.hashnode.com/res/hashnode/image/upload/v1735051327581/c940c14c-636b-4cfc-b55f-5e1fd4f11370.png align="center")

Les résultats de l'expérience montrent que les WebSockets performant le mieux pour cette tâche, se révélant être la technologie de transfert de données la plus efficace en termes de performance dans les scénarios simulés.

### **Lequel est le meilleur : Server-Sent Events ou WebSockets ?**

SSE est une solution plus simple, mais elle n'est pas extensible : si les exigences de votre application web devaient changer, il faudrait probablement la refactoriser en utilisant WebSockets. De plus, avec l'intégration de l'IA, SSE devient encore plus puissant et sécurisé.

Bien que la technologie WebSocket présente plus de travail initial, c'est un framework plus polyvalent et extensible, ce qui en fait une meilleure option pour les applications complexes qui sont susceptibles d'ajouter de nouvelles fonctionnalités au fil du temps.

<table><tbody><tr><td colspan="1" rowspan="1"><p>Fonctionnalité</p></td><td colspan="1" rowspan="1"><p>WebSockets</p></td><td colspan="1" rowspan="1"><p>Server-Sent Events&nbsp;</p></td></tr><tr><td colspan="1" rowspan="1"><p>Communication</p></td><td colspan="1" rowspan="1"><p>Full-duplex (bidirectionnelle)</p></td><td colspan="1" rowspan="1"><p>Unidirectionnelle (serveur vers client)</p></td></tr><tr><td colspan="1" rowspan="1"><p>Support des types de données</p></td><td colspan="1" rowspan="1"><p>Binaire et texte</p></td><td colspan="1" rowspan="1"><p>Texte (uniquement encodé en UTF-8)</p></td></tr><tr><td colspan="1" rowspan="1"><p>Limites de connexion</p></td><td colspan="1" rowspan="1"><p>Limitées par les ressources du serveur</p></td><td colspan="1" rowspan="1"><p>Limitées par le navigateur (par exemple, 6 onglets)</p></td></tr><tr><td colspan="1" rowspan="1"><p>Reconnexion</p></td><td colspan="1" rowspan="1"><p>Nécessite une gestion manuelle</p></td><td colspan="1" rowspan="1"><p>Automatique</p></td></tr><tr><td colspan="1" rowspan="1"><p>Protocole</p></td><td colspan="1" rowspan="1"><p>Protocole personnalisé de bas niveau</p></td><td colspan="1" rowspan="1"><p>Basé sur HTTP</p></td></tr><tr><td colspan="1" rowspan="1"><p>Gestion des pare-feu</p></td><td colspan="1" rowspan="1"><p>Peut rencontrer des problèmes</p></td><td colspan="1" rowspan="1"><p>Fonctionnent de manière transparente</p></td></tr><tr><td colspan="1" rowspan="1"><p>Exemples de cas d'utilisation</p></td><td colspan="1" rowspan="1"><p>Communication en temps réel et pilotée par événements entre clients et serveurs, comme les jeux en ligne, les chats, etc.</p></td><td colspan="1" rowspan="1"><p>Diffusion de données de manière unidirectionnelle (c'est-à-dire « dans une seule direction ») du serveur vers le client pour des données de streaming comme les cours des actions, les prix du bitcoin, etc.</p></td></tr></tbody></table>

En pratique, de nombreux développeurs préfèrent les WebSockets même pour les scénarios nécessitant la réception d'informations plutôt que d'opter pour SSE. Cette préférence n'est pas uniquement due aux limitations de SSE—comme sa dépendance à maintenir une connexion ouverte pour un flux de données continu—mais aussi parce que les WebSockets offrent une plus grande polyvalence et sont souvent considérés comme plus adaptés à l'avenir.

Par exemple, des plateformes populaires comme Reddit et Trello choisissent les WebSockets pour recevoir des données (Reddit et Trello n'envoient des informations aux utilisateurs que lorsqu'ils sont invités à s'abonner à une autre personne).

D'après mon expérience personnelle, je peux souligner que les données SSE n'apparaissent souvent pas dans les outils de développement, ce qui rend le débogage et l'inspection plus difficiles. Vous pouvez vérifier cela en consultant une application web comme ChatGPT, où aucune donnée SSE envoyée par le serveur n'est visible dans l'onglet réseau des outils de développement. Ce manque de transparence peut rendre le travail avec SSE plus difficile que le flux de données plus direct et visible fourni par les WebSockets.

## Conclusion

J'espère que cet article a été à la fois intéressant et utile pour vous ! Si vous souhaitez renforcer davantage vos connaissances et passer au niveau supérieur, je vous recommande vivement de vous plonger dans des projets réels.

Personnellement, j'ai trouvé ceux-ci sur freeCodeCamp vraiment utiles et même un peu stimulants : [Comment construire une application web de journalisation avec Server-Sent Events, RxJS et Express et Apprendre les WebSockets avec Socket.IO](https://www.freecodecamp.org/news/build-a-logging-web-app-with-server-sent-events-rxjs-and-express/). Non seulement ces projets vous donneront une expérience pratique, mais ils vous fourniront également de nouvelles perspectives et compétences précieuses que vous pourrez appliquer à de futurs défis de développement.

Bonne programmation, et continuez à apprendre !