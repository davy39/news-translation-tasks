---
title: Comment construire un chatbot IA avec Spring AI, React et Docker
subtitle: ''
author: Vikas Rajput
co_authors: []
series: null
date: '2024-09-23T14:27:25.876Z'
originalURL: https://freecodecamp.org/news/ai-chatbot-with-spring-react-docker
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/6UDansS-rPI/upload/d57a180a4cda63056c786838a71c6679.jpeg
tags:
- name: Springboot
  slug: springboot
- name: Java
  slug: java
- name: AI
  slug: ai
- name: Docker
  slug: docker
- name: React
  slug: reactjs
- name: openai
  slug: openai
seo_title: Comment construire un chatbot IA avec Spring AI, React et Docker
seo_desc: 'Hey Java developers, I’ve got good news: Spring now has official support
  for building AI applications using the Spring AI module.

  In this tutorial, we’ll build a chatbot application using Spring Boot, React, Docker,
  and OpenAI. This app will let user...'
---

Salut les développeurs Java, j'ai une bonne nouvelle : Spring dispose désormais d'un support officiel pour la création d'applications d'IA à l'aide du module [Spring AI](https://spring.io/projects/spring-ai).

Dans ce tutoriel, nous allons construire une application de chatbot en utilisant [**Spring Boot**](https://spring.io/projects/spring-boot), [**React**](https://react.dev/), [**Docker**](https://www.docker.com/) et [**OpenAI**](https://openai.com/). Cette application permettra aux utilisateurs d'interagir avec un chatbot alimenté par l'IA, de poser des questions et de recevoir des réponses en temps réel.

L'intégralité du code source mentionné dans cet article est déjà disponible sur le [répertoire GitHub](https://github.com/vikasrajputin/springboot-react-docker-chatbot). N'hésitez pas à lui donner une étoile et à le fork pour l'expérimenter.

Pour vous donner une idée de ce que nous allons construire, voici à quoi ressemblera l'application finale :

![UI de l'application Chatbot utilisant Spring AI, React, Docker par Vikas Rajput](https://cdn.hashnode.com/res/hashnode/image/upload/v1726657239698/5170bf73-b317-4281-bcd1-583454d4113f.png align="center")

Vous êtes prêt ? Construisons-la de zéro !

## **Table des matières**

* [Prérequis](#heading-prerequis)
    
* [Obtenir votre clé OpenAI](#heading-obtenir-votre-cle-openai)
    
* [Créer l'API REST avec Spring Boot](#heading-creer-lapi-rest-avec-spring-boot)
    
* [Créer l'interface de chat avec Reactjs](#heading-creer-linterface-de-chat-avec-reactjs)
    
* [Comment dockeriser l'application](#heading-comment-dockeriser-lapplication)
    
* [Exécuter l'application](#heading-executer-lapplication)
    
* [Félicitations 🎉](#heading-felicitations)
    

## **Prérequis**

Avant de plonger dans la création du chatbot, voici quelques éléments avec lesquels vous devrez être familier :

1. Compréhension de base de **Java** et **Spring Boot**.
    
2. Compréhension de base de **React** et **CSS**.
    
3. Installez le [JDK](https://jdk.java.net/java-se-ri/17-MR1), le [Node Package Manager](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) et [Docke](https://docs.docker.com/get-started/get-docker/)[r](https://docs.docker.com/desktop/) sur votre machine.
    

## **Obtenir votre clé OpenAI**

Tout d'abord, vous devrez vous inscrire pour un compte [OpenAI](https://platform.openai.com/) si vous n'en avez pas. Une fois connecté, vous serez redirigé vers la page d'accueil.

Dans le coin supérieur droit, cliquez sur le menu "Dashboard". Dans la barre latérale, cliquez sur "API Keys", puis cliquez sur le bouton "Create new secret key" pour générer votre clé secrète :

![Comment générer votre clé OpenAI](https://cdn.hashnode.com/res/hashnode/image/upload/v1726818120291/5f1681a0-fdbe-401e-ab4b-769fe38d7957.png align="center")

Copiez la clé secrète et conservez-la en lieu sûr, car vous en aurez besoin plus tard pour connecter votre application à l'API OpenAI.

Vous pouvez consulter le [guide de référence de l'API](https://platform.openai.com/docs/api-reference/authentication) d'OpenAI pour en savoir plus sur la manière d'appeler les API, les requêtes acceptées et les réponses fournies.

## **Créer l'API REST avec Spring Boot**

Rendez-vous sur [spring initializer](https://start.spring.io/) pour générer le code de base :

![Créer une application Spring AI via spring initializer](https://cdn.hashnode.com/res/hashnode/image/upload/v1726662395429/cd4b07fd-2597-43bf-8038-1821003125bb.png align="center")

Vous pouvez choisir le groupe, l'artefact, le nom, la description et le package de votre choix. Nous avons utilisé Maven comme outil de build, Spring Boot version 3.3.3, Jar comme option de packaging et Java version 17.

Cliquez sur le bouton générer et le fichier zip sera téléchargé. Dézippez les fichiers et importez-les comme projet Maven dans votre IDE préféré (le mien est IntelliJ).

### Configurer votre clé OpenAI dans Spring

Vous pouvez soit utiliser le fichier `application.properties` existant, soit créer un fichier `application.yaml`. J'adore travailler avec Yaml, j'ai donc créé un fichier `application.yaml` pour y placer toutes mes configurations Spring Boot.

Ajoutez la clé OpenAIKey, le modèle et la température à votre fichier `application.yaml` :

```yaml
spring:
  ai:
    openai:
      chat:
        options:
          model: "gpt-3.5-turbo"
          temperature: "0.7"
      key: "METTEZ_VOTRE_CLE_OPEN_API_ICI"
```

Une configuration similaire dans `application.properties` ressemblerait à ceci :

```basic
spring.ai.openai.chat.options.model=gpt-3.5-turbo
spring.ai.openai.chat.options.temperature=0.7
spring.ai.openai.key="METTEZ_VOTRE_CLE_OPEN_API_ICI"
```

### Créer le ChatController

Créons une API `GET` avec l'URL `/ai/chat/string` et une méthode pour gérer la logique :

```java
@RestController
public class ChatController {

    @Autowired
    private final OpenAiChatModel chatModel;

    @GetMapping("/ai/chat/string")
    public Flux<String> generateString(@RequestParam(value = "message", defaultValue = "Raconte-moi une blague") String message) {
        return chatModel.stream(message);
    }
}
```

* Tout d'abord, nous ajoutons `@RestController` pour marquer la classe `ChatController` comme notre contrôleur Spring.
    
* Ensuite, nous injectons la dépendance pour la classe `OpenAiChatModel`. Elle est fournie par défaut avec la dépendance Spring AI que nous avons utilisée.
    
* `OpenAiChatModel` possède une méthode `stream(message)` qui accepte le prompt sous forme de `String` et renvoie une réponse `String` (techniquement, c'est un `Flux` de `String` car nous avons utilisé une version réactive de la méthode).
    
* En interne, `OpenAiChatModel.stream(message)` appellera l'API OpenAI et récupérera la réponse. L'appel OpenAI utilisera les étapes de configuration mentionnées dans votre fichier `application.yaml`, assurez-vous donc d'utiliser une clé OpenAI valide.
    
* Nous avons créé une méthode pour gérer l'appel de l'API GET, qui accepte le message et renvoie un `Flux<String>` comme réponse.
    

### Compiler, exécuter et tester l'API REST

Utilisez les commandes Maven pour compiler et exécuter l'application Spring Boot :

```bash
./mvnw clean install spring-boot:run
```

Idéalement, elle s'exécutera sur le port `8080`, sauf si vous avez personnalisé le port. Assurez-vous que ce port est libre pour exécuter l'application avec succès.

Vous pouvez utiliser soit [Postman](https://www.postman.com/), soit la commande [Curl](https://curl.se/) pour tester votre API REST :

```bash
curl --location 'http://localhost:8080/ai/chat/string?message=Comment%20allez-vous%3F'
```

## Créer l'interface de chat avec React.js

Nous allons faire simple pour les besoins de ce tutoriel, alors pardonnez-moi si je ne suis pas toutes les meilleures pratiques React.

### Créer `App.js` pour gérer le formulaire de l'interface de chat

Nous utiliserons `useState` pour gérer l'état :

```js
const [messages, setMessages] = useState([]);
const [input, setInput] = useState('');
const [loading, setLoading] = useState(false);
```

* `messages` : stockera tous les messages du chat. Chaque message a un `text` (texte) et un `sender` (expéditeur, soit 'user' soit 'ai').
    
* `input` : pour conserver ce que l'utilisateur tape dans la zone de texte.
    
* `loading` : cet état est défini sur `true` pendant que le chatbot attend une réponse de l'IA, et sur `false` lorsque la réponse est reçue.
    

Créons une fonction `handleSend` et appelons-la lorsque l'utilisateur envoie un message en cliquant sur un bouton ou en appuyant sur Entrée :

```js
const handleSend = async () => {
    if (input.trim() === '') return;
    
    const newMessage = { text: input, sender: 'user' };
    setMessages([...messages, newMessage]);
    setInput('');
    setLoading(true);

    try {
        const response = await axios.get('http://localhost:8080/ai/chat/string?message=' + input);
        const aiMessage = { text: response.data, sender: 'ai' };
        setMessages([...messages, newMessage, aiMessage]);
    } catch (error) {
        console.error("Erreur lors de la récupération de la réponse de l'IA", error);
    } finally {
        setLoading(false);
    }
};
```

Voici ce qui se passe étape par étape :

* **Vérifier l'entrée vide** : si le champ d'entrée est vide, la fonction s'arrête prématurément (rien n'est envoyé).
    
* **Nouveau message de l'utilisateur** : un nouveau message est ajouté au tableau `messages`. Ce message contient le `text` (ce que l'utilisateur a tapé) et est marqué comme envoyé par l'utilisateur ('user').
    
* **Réinitialiser l'entrée** : le champ d'entrée est vidé après l'envoi du message.
    
* **Démarrer le chargement** : en attendant que l'IA réponde, `loading` est défini sur `true` pour afficher un indicateur de chargement.
    
* **Effectuer la requête API** : le code utilise `axios` pour requêter l'API du chatbot IA, en passant le message de l'utilisateur. Lorsque la réponse arrive, un nouveau message de l'IA est ajouté au chat.
    
* **Gestion des erreurs** : s'il y a un problème pour obtenir la réponse de l'IA, une erreur est enregistrée dans la console.
    
* **Arrêter le chargement** : enfin, l'état de chargement est désactivé.
    

Écrivons une fonction pour mettre à jour l'état `input` chaque fois que l'utilisateur tape quelque chose dans le champ d'entrée :

```js
const handleInputChange = (e) => {
    setInput(e.target.value);
};
```

Ensuite, créons une fonction pour vérifier si l'utilisateur appuie sur la touche Entrée. Si c'est le cas, elle appelle `handleSend()` pour envoyer le message :

```js
const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
        handleSend();
    }
};
```

Créons maintenant les éléments de l'interface utilisateur pour afficher les messages du chat :

```js
{messages.map((message, index) => (
    <div key={index} className={`message-container ${message.sender}`}>
        <img
            src={message.sender === 'user' ? 'user-icon.png' : 'ai-assistant.png'}
            alt={`${message.sender} avatar`}
            className="avatar"
        />
        <div className={`message ${message.sender}`}>
            {message.text}
        </div>
    </div>
))}
```

Ce bloc affiche tous les messages du chat :

* **Itération sur les messages** : chaque message est affiché sous forme de `div` en utilisant `.map()`.
    
* **Style des messages** : le nom de la classe du message change en fonction de l'expéditeur (`user` ou `ai`), ce qui permet de savoir clairement qui a envoyé le message.
    
* **Images d'avatar** : chaque message affiche un petit avatar, avec une image différente pour l'utilisateur et pour l'IA.
    

Ajoutons une logique pour afficher le chargeur en fonction d'un indicateur :

```js
{loading && (
    <div className="message-container ai">
        <img src="ai-assistant.png" alt="IA avatar" className="avatar" />
        <div className="message ai">...</div>
    </div>
)}
```

Pendant que l'IA réfléchit (quand `loading` est `true`), nous affichons un message de chargement (`...`) afin que l'utilisateur sache qu'une réponse arrive bientôt.

Enfin, créons un bouton pour envoyer le message :

```jsx
<button onClick={handleSend}>
    <FaPaperPlane />
</button>
```

Ce bouton déclenche la fonction `handleSend()` lorsqu'on clique dessus. L'icône utilisée ici est un [avion en papier](https://react-icons.github.io/react-icons/icons/fa/), courant pour les boutons d'envoi.

Le code complet de `Chatbot.js` ressemble à ceci :

```javascript
import React, { useState } from 'react';
import axios from 'axios';
import { FaPaperPlane } from 'react-icons/fa';
import './Chatbot.css';

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSend = async () => {
        if (input.trim() === '') return;
        
        const newMessage = { text: input, sender: 'user' };
        setMessages([...messages, newMessage]);
        setInput('');
        setLoading(true);

        try {
            const response = await axios.get('http://localhost:8080/ai/chat/string?message=' + input);
            const aiMessage = { text: response.data, sender: 'ai' };
            setMessages([...messages, newMessage, aiMessage]);
        } catch (error) {
            console.error("Erreur lors de la récupération de la réponse de l'IA", error);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSend();
        }
    };

    return (
        <div className="chatbot-container">
            <div className="chat-header">
                <img src="ChatBot.png" alt="Chatbot Logo" className="chat-logo" />
                <div className="breadcrumb">Accueil &gt; Chat</div>
            </div>
            <div className="chatbox">
                {messages.map((message, index) => (
                    <div key={index} className={`message-container ${message.sender}`}>
                        <img
                            src={message.sender === 'user' ? 'user-icon.png' : 'ai-assistant.png'}
                            alt={`${message.sender} avatar`}
                            className="avatar"
                        />
                        <div className={`message ${message.sender}`}>
                            {message.text}
                        </div>
                    </div>
                ))}
                {loading && (
                    <div className="message-container ai">
                        <img src="ai-assistant.png" alt="IA avatar" className="avatar" />
                        <div className="message ai">...</div>
                    </div>
                )}
            </div>
            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={handleInputChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Tapez votre message..."
                />
                <button onClick={handleSend}>
                    <FaPaperPlane />
                </button>
            </div>
        </div>
    );
};

export default Chatbot;
```

Utilisez `<Chatbot/>` à l'intérieur d' `App.js` pour charger l'interface utilisateur du Chatbot :

```javascript
function App() {
  return (
    <div className="App">
            <Chatbot />
        </div>
  );
}
```

En parallèle, nous utilisons également du CSS pour rendre notre chatbot un peu plus attrayant. Vous pouvez vous référer à [App.css](https://github.com/vikasrajputin/springboot-react-docker-chatbot/blob/main/chatbot-ui/src/App.css) et [Chatbot.css](https://github.com/vikasrajputin/springboot-react-docker-chatbot/blob/main/chatbot-ui/src/Chatbot.css) pour cela.

### Exécuter le Frontend

Utilisez la commande `npm` pour exécuter l'application :

```bash
npm start
```

Cela devrait lancer le frontend sur l'URL `http://localhost:3000`. L'application est maintenant prête à être testée.

Mais exécuter le backend et le frontend séparément est un peu fastidieux. Utilisons donc Docker pour simplifier l'ensemble du processus de construction.

## **Comment dockeriser l'application**

Dockerisons l'ensemble de l'application pour faciliter son regroupement et son déploiement n'importe où sans tracas. Vous pouvez installer et configurer Docker depuis le [site officiel de Docker](https://docs.docker.com/get-started/get-docker/).

### Dockeriser le Backend

Le backend de notre chatbot est construit avec Spring Boot, nous allons donc créer un `Dockerfile` qui compile l'application Spring Boot en un fichier JAR exécutable et l'exécute dans un conteneur.

Écrivons le `Dockerfile` pour cela :

```dockerfile
# Commencer avec une image officielle disposant de Java installé
FROM openjdk:17-jdk-alpine

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier de build Maven/Gradle et le code source dans le conteneur
COPY target/chatbot-backend.jar /app/chatbot-backend.jar

# Exposer le port de l'application
EXPOSE 8080

# Commande pour exécuter l'application Spring Boot
CMD ["java", "-jar", "chatbot-backend.jar"]
```

* `FROM openjdk:17-jdk-alpine` : spécifie que le conteneur doit être basé sur une image Alpine Linux légère incluant le JDK 17, nécessaire pour exécuter Spring Boot.
    
* `WORKDIR /app` : définit le répertoire de travail dans le conteneur sur `/app`, où résideront nos fichiers d'application.
    
* `COPY target/chatbot-backend.jar /app/chatbot-backend.jar` : copie le fichier JAR compilé depuis votre machine locale (généralement dans le dossier `target` après le build Maven ou Gradle) vers le conteneur.
    
* `EXPOSE 8080` : indique à Docker que l'application écoutera les requêtes sur le port 8080.
    
* `CMD ["java", "-jar", "chatbot-backend.jar"]` : spécifie la commande qui s'exécutera au démarrage du conteneur. Elle lance le fichier JAR qui démarre l'application Spring Boot.
    

### Dockeriser le Frontend

Le frontend de notre chatbot est construit avec React. Nous pouvons le dockeriser en créant un Dockerfile qui installe les dépendances nécessaires, compile l'application et la sert via un serveur web léger comme NGINX.

Écrivons le `Dockerfile` pour le frontend React :

```dockerfile
# Utiliser une image Node pour construire l'application React
FROM node:16-alpine AS build

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le package.json et installer les dépendances
COPY package.json package-lock.json ./
RUN npm install

# Copier le reste du code de l'application et le compiler
COPY . .
RUN npm run build

# Utiliser un serveur NGINX léger pour servir l'application compilée
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Exposer le port 80 pour le trafic web
EXPOSE 80

# Démarrer NGINX
CMD ["nginx", "-g", "daemon off;"]
```

* `FROM node:16-alpine AS build` : utilise une image Node.js légère pour construire l'application React. Nous installons toutes les dépendances et compilons l'application dans ce conteneur.
    
* `WORKDIR /app` : définit le répertoire de travail à l'intérieur du conteneur sur `/app`.
    
* `COPY package.json package-lock.json ./` : copie `package.json` et `package-lock.json` pour installer les dépendances.
    
* `RUN npm install` : installe les dépendances listées dans le package.json.
    
* `COPY . .` : copie tout le code source du frontend dans le conteneur.
    
* `RUN npm run build` : compile l'application React. Les fichiers compilés se trouveront dans un dossier `build`.
    
* `FROM nginx:alpine` : après la compilation de l'application, cette ligne démarre un nouveau conteneur basé sur le serveur web `nginx`.
    
* `COPY --from=build /app/build /usr/share/nginx/html` : copie l'application React compilée du premier conteneur vers le conteneur nginx, en la plaçant dans le dossier par défaut où NGINX sert les fichiers.
    
* `EXPOSE 80` : expose le port 80, qu'NGINX utilise pour servir le trafic web.
    
* `CMD ["nginx", "-g", "daemon off;"]` : démarre le serveur NGINX au premier plan pour servir votre application React.
    

### Docker Compose pour exécuter les deux

Maintenant que nous avons des Dockerfiles séparés pour le frontend et le backend, nous allons utiliser `docker-compose` pour orchestrer l'exécution des deux conteneurs simultanément.

Écrivons le fichier `docker-compose.yml` à la racine du projet :

```yaml
version: '3'
services:
  backend:
    build: ./backend
    ports:
      - "8080:8080"
    networks:
      - chatbot-network

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - backend
    networks:
      - chatbot-network

networks:
  chatbot-network:
    driver: bridge
```

* `version: '3'` : définit la version de Docker Compose utilisée.
    
* `services:` : définit les services que nous voulons exécuter.
    
    * `backend` : ce service construit le backend en utilisant le Dockerfile situé dans le répertoire `./backend` et expose le port 8080.
        
    * `frontend` : ce service construit le frontend en utilisant le Dockerfile situé dans le répertoire `./frontend`. Il mappe le port 3000 de l'hôte au port 80 à l'intérieur du conteneur.
        
* `depends_on:` : garantit que le frontend attend que le backend soit prêt avant de démarrer.
    
* `networks:` : cette section définit un réseau partagé pour que le backend et le frontend puissent communiquer entre eux.
    

## Exécuter l'application

Pour exécuter l'intégralité de l'application (frontend et backend), vous pouvez utiliser la commande suivante :

```bash
docker-compose up --build
```

Cette commande va :

* Construire les images du frontend et du backend.
    
* Démarrer les deux conteneurs (backend sur le port 8080, frontend sur le port 3000).
    
* Configurer le réseau pour que les deux services puissent communiquer.
    

Maintenant, vous pouvez vous rendre sur `http://localhost:3000`, charger l'interface utilisateur du chatbot et commencer à poser vos questions à l'IA.

## Félicitations 🎉

Vous avez réussi à construire une application de chatbot full-stack en utilisant Spring Boot, React, Docker et OpenAI.

Le code source présenté dans le projet est disponible sur [GitHub](https://github.com/vikasrajputin/springboot-react-docker-chatbot). S'il vous a été utile, donnez-lui une étoile, et n'hésitez pas à le fork et à l'expérimenter.