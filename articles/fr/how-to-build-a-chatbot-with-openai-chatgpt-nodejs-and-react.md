---
title: Comment créer un ChatBot alimenté par IA avec OpenAI, ChatGPT, Node.js et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T22:08:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chatbot-with-openai-chatgpt-nodejs-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-sanket-mishra-16629368.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: chatgpt
  slug: chatgpt
- name: node js
  slug: node-js
- name: openai
  slug: openai
- name: React
  slug: react
seo_title: Comment créer un ChatBot alimenté par IA avec OpenAI, ChatGPT, Node.js
  et React
seo_desc: "By Njoku Samson Ebere\nArtificial Intelligence (AI) has been making waves\
  \ lately, with ChatGPT revolutionizing the internet with the chat completion functionality.\
  \ \nYou can do a lot with it: drafting an email or other piece of writing, answering\
  \ quest..."
---

Par Njoku Samson Ebere

L'intelligence artificielle (IA) a fait beaucoup parler d'elle récemment, avec [ChatGPT](https://platform.openai.com/) révolutionnant l'internet avec la fonctionnalité de [chat completion](https://platform.openai.com/docs/guides/chat). 

On peut faire beaucoup de choses avec : rédiger un email ou un autre texte, répondre à des questions sur un ensemble de documents, créer des agents conversationnels, donner à votre logiciel une interface en langage naturel, tutorer dans diverses matières, traduire des langues, et bien plus encore.  
  
Cet article enseignera les bases de la création d'une application de chat en utilisant la fonctionnalité de [chat completion](https://platform.openai.com/docs/guides/chat) pour faciliter l'intégration de chaque programmeur. Ce n'est pas aussi difficile que cela en a l'air. Vous verrez cela en suivant ce tutoriel. 

Vous apprendrez les points suivants :

* Comment créer une application de chat CLI avec Node.js uniquement.
* Comment créer une application de chat en utilisant uniquement React.
* Comment combiner React et Node.js pour créer un meilleur logiciel d'IA de chat.

Ce tutoriel sera basé sur le modèle [`gpt-3.5-turbo`](https://platform.openai.com/docs/models/gpt-3-5).

%[https://youtu.be/T-9-_1w82Jg]

## Prérequis

Ce tutoriel nécessite des connaissances de base en JavaScript, CSS, React et Node.js.  
  
Vous avez également besoin d'un compte sur la plateforme OpenAI où ChatGPT est hébergé. C'est gratuit, vous pouvez donc en créer un [ici](https://platform.openai.com/overview).

## Comment créer une application de chat IA CLI avec Node.js

Cette section se concentrera sur la création d'une application de chat qui ne fonctionnera que sur le terminal en utilisant [Node.js](https://nodejs.org/).

%[https://youtu.be/4uTO3xZx5r4]

Commencez par créer un répertoire pour le projet :

```cmd
mkdir nodejs-chatgpt-tutorial
```

Naviguez dans le dossier :

```cmd
cd nodejs-chatgpt-tutorial
```

Initialisez le projet :

```
npm init -y
```

Cela créera un fichier `package.json` pour suivre les détails du projet.

Ajoutez la ligne de code suivante au fichier :

```javascript
"type": "module"
```

Cela vous permettra d'utiliser l'instruction d'importation de module ES6.  
  
Installez [OpenAI](https://openai.com/) avec la commande suivante :

```cmd
npm i openai

```

Créez un fichier où tout le code résidera. Nommez-le `index.js` :

```cmd
touch index.js
```

Importez `Configuration` et `OpenAIApi` du module [OpenAI](https://openai.com/) et `readline` du module [readline](https://nodejs.org/api/readline.html) :

```javascript
import { Configuration, OpenAIApi } from "openai";
import readline from "readline";
```

Construisez la configuration OpenAI comme ceci :

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
```

Ce code crée une nouvelle instance de l'objet `Configuration`. À l'intérieur, vous entrerez les valeurs pour votre `organization` et `apiKey`. Vous pouvez trouver les détails de votre organisation dans [settings](https://platform.openai.com/account/org-settings) et les informations de votre apiKey dans [API](https://platform.openai.com/account/api-keys) [keys](https://platform.openai.com/account/api-keys). Si vous n'avez pas de clé API existante, vous pouvez en créer une.  
  
Entrez le code suivant après la configuration pour créer une nouvelle instance de l'API OpenAI :

```javascript
const openai = new OpenAIApi(configuration);
```

Vous l'utiliserez tout au long du projet.

Tapez le code ci-dessous pour tester la fonction `createChatCompletion` :

```javascript
openai
  .createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: "Hello" }],
  })
  .then((res) => {
    console.log(res.data.choices[0].message.content);
  })
  .catch((e) => {
    console.log(e);
  });
```

Ce code appelle la fonction `createChatCompletion` qui déclenche un endpoint (`https://api.openai.com/v1/chat/completions`). La fonction accepte un objet d'arguments (le `model` de chatGPT utilisé et un tableau de `messages` entre l'utilisateur et l'IA. Nous verrons comment utiliser le tableau `messages` pour garder un historique de la conversation et améliorer l'application dans la section suivante).  
  
Chaque message est un objet contenant le `role` (c'est-à-dire qui a envoyé le message. La valeur peut être `assistant` s'il provient de l'IA ou `user` lorsque le message provient d'un humain) et le `content` (l'information envoyée).  
  
Enfin, le code imprime la réponse (`res.data.choices[0].message.content`) de l'IA. Exécutez le fichier dans le terminal avec cette commande :

```cmd
node index
```

Cela retournera une réponse de l'IA après quelques secondes.  
  
Et c'est tout ce qu'il faut pour créer le chatbot !   
  
Mais il serait utile de rendre l'application plus interactive en demandant une entrée de l'utilisateur au lieu de coder en dur le contenu du message dans le code. Le module [readline](https://nodejs.org/api/readline.html) nous aidera à cet égard.  
  
Pour le rendre interactif, supprimez le dernier code que vous avez tapé et ajoutez ce qui suit :

```javascript
const userInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
```

Ce code crée une interface utilisateur dans le terminal qui permet aux utilisateurs de taper leurs questions.

Ensuite, invitez l'utilisateur à entrer un message en utilisant le code ci-dessous :

```javascript
userInterface.prompt();

```

Enfin, entrez le code suivant :

```javascript
userInterface.on("line", async (input) => {
  await openai
    .createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: input }],
    })
    .then((res) => {
      console.log(res.data.choices[0].message.content);
      userInterface.prompt();
    })
    .catch((e) => {
      console.log(e);
    });
});
```

Dans le code ci-dessus,

* Lorsque l'utilisateur tape quelque chose et appuie sur `Enter`, le code ci-dessus déclenche une fonction de rappel.
* Il transmet tout ce qui a été tapé par l'utilisateur en tant qu'`input`.
* L'`input` est maintenant utilisé comme `content`.
* Après l'affichage de la réponse de l'IA, l'utilisateur est invité à entrer un autre message dans le bloc `then`.

Voir tout le code sur [GitHub](https://github.com/EBEREGIT/nodejs-chatgpt-tutorial).  
  
Exécutez le fichier et discutez avec l'IA. Cela ressemblera à l'image ci-dessous :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682935202577_Screenshot+2023-05-01+at+10.58.02.png)
_Chat CLI avec IA_

Super ! C'est un chat CLI interactif.  
  
Cela est utile pour quelques personnes (comme les ingénieurs), mais il offre une bonne sécurité car il est côté serveur.   
  
Mais qu'en est-il des autres qui ne comprennent peut-être pas comment utiliser une application CLI ? Ils auront besoin de quelque chose de plus facile à utiliser avec une meilleure interface utilisateur (UI) et une meilleure expérience utilisateur (UX). La section suivante se concentrera sur la création de ce type d'application en utilisant [React](https://react.dev/).

## Comment créer une application de chat en utilisant React

Cette section vise à aider les développeurs frontend à se familiariser avec l'API ChatGPT pour créer une application de chat et construire une meilleure interface utilisateur pour offrir de meilleures expériences aux utilisateurs. Vous pouvez appliquer les connaissances que vous acquérez ici à d'autres frameworks ou bibliothèques frontend.

%[https://youtu.be/JrfaQ5dYbWg]

La première chose à faire est de configurer une structure de base React. J'utiliserai [Vite](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) à cette fin. Vous pouvez utiliser Vite pour échafauder n'importe quel projet frontend JavaScript moderne. Utilisez la commande suivante :

```javascript
npm create vite@latest
```

Cette commande vous invitera à créer un nom et un dossier pour votre projet et à choisir un framework ou une bibliothèque (ce tutoriel utilise React). Après cela, vous naviguerez dans le dossier et exécuterez la commande suivante :

```javascript
npm install
npm run dev
```

Ces commandes installeront les dépendances nécessaires et démarreront le serveur local sur le port `5173`  
  
Ensuite, installez [OpenAI](https://openai.com/) avec la commande suivante :

```javascript
npm i openai
```

Ce module donne accès à tout ce dont nous avons besoin pour créer l'application de chat.  
  
Maintenant, nous sommes prêts à commencer à écrire le code !  
  
Naviguez dans le fichier `src/App.jsx` et supprimez tout son contenu. Ensuite, ajoutez les instructions d'importation suivantes :

```javascript
import { useState } from "react";
import { Configuration, OpenAIApi } from "openai";
```

Le code ci-dessus importe la `Configuration` pour configurer les valeurs de configuration et `OpenAIApi` pour nous donner accès aux fonctionnalités de chat completion.  
  
Après cela, construisez la configuration comme ceci :

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
```

Ce code crée une nouvelle instance de l'objet `Configuration`. À l'intérieur, vous entrez les valeurs pour votre `organization` et `apiKey`. Vous pouvez trouver les détails de votre organisation dans [settings](https://platform.openai.com/account/org-settings) et les informations de votre apiKey dans [API](https://platform.openai.com/account/api-keys) [keys](https://platform.openai.com/account/api-keys). Si vous n'avez pas de clé API existante, vous pouvez en créer une.  
  
Entrez le code suivant après la configuration pour créer une nouvelle instance de l'API OpenAI :

```javascript
const openai = new OpenAIApi(configuration);
```

Nous l'utiliserons tout au long du projet.  
  
Créez et exportez une fonction par défaut :

```javascript
function App() {

  return (
    <main>
      <h1>Tutoriel Chat AI</h1>
    <main/>
  );
}
export default App;
```

Cette fonction contiendra le reste du code.  
  
Configurez les états suivants avant l'instruction `return` :

```javascript
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
```

* Le `message` contiendra les informations envoyées de l'application à l'IA.
* Le tableau `chats` gardera une trace de tous les messages envoyés par les deux parties (utilisateur et IA).
* La variable `isTyping` informera l'utilisateur si le bot est en train de taper ou non.

Tapez les lignes de code suivantes sous la balise h1

```javascript
      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>
```

Le code ci-dessus affichera `Typing` chaque fois que l'utilisateur attend une réponse de l'IA.  
  
Créez un formulaire dans lequel un utilisateur peut taper un message en ajoutant le code ci-dessous dans l'élément `main` :

```javascript
      <form action="" onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Tapez un message ici et appuyez sur Entrée..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
```

Ce code crée un formulaire avec une seule entrée. Chaque fois que le formulaire est soumis en appuyant sur la touche `Enter`, il déclenche la fonction `chat`.  
  
La fonction chat prendra deux (2) arguments (`e` et `message`) comme ceci :

```javascript
const chat = async (e, message) => {

}

```

Entrez les lignes suivantes dans la fonction :

```javascript
    e.preventDefault();
    
    if (!message) return;
    setIsTyping(true);
```

Le code ci-dessus empêche le `form` de recharger la page web, vérifie si un message a été tapé avant la soumission, et définit `isTyping` sur `true` pour indiquer que l'application a commencé à travailler sur l'entrée fournie.   
  
ChatGPT a un format dans lequel les messages doivent être. Il suit le modèle suivant :

```
{role: user | assistant, content: message à envoyer
```

Chaque message (`content`) doit indiquer qui l'a envoyé. Le rôle est `assistant` lorsque le chat provient de l'IA mais `user` s'il provient d'un humain. Donc, avant d'envoyer le message, assurez-vous de le formater correctement et de l'ajouter au tableau (`chats`) comme ceci :

```javascript
    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");
```

La dernière ligne ci-dessus efface l'entrée pour qu'un utilisateur puisse taper une autre note.  
  
Maintenant, nous allons appeler l'endpoint `createChatCompletion` en déclenchant la fonction `createChatCompletion` en utilisant le code ci-dessous :

```javascript
  await openai
      .createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "system",
            content:
              "Vous êtes un EbereGPT. Vous pouvez aider avec les tâches de conception graphique",
          },
          ...chats,
        ],
      })
```

La fonction `createChatCompletion` prend au moins deux (2) arguments (`model` et `messages`) :

* Le modèle spécifie la version de chatGPT utilisée.
* Les messages sont une liste de tous les messages échangés entre un utilisateur et l'IA jusqu'à présent et un message système qui donne à l'IA une idée du type d'assistance qu'elle peut fournir.

```javascript
          {
            role: "system",
            content:
              "Vous êtes un EbereGPT. Vous pouvez aider avec les tâches de conception graphique",
          }
```

Vous pouvez changer le contenu pour ce qui vous convient.  
  
Les `messages` n'ont pas besoin de contenir plus d'un objet dans le tableau. Il peut s'agir d'un seul message. Mais lorsqu'il s'agit d'un tableau, il fournit un historique de messages sur lequel l'IA peut s'appuyer pour donner de meilleures réponses à l'avenir, et il permet à l'utilisateur de taper moins puisque cela peut ne pas être nécessaire d'être trop descriptif tout le temps.  
  
La fonction `createChatCompletion` retourne une promesse. Utilisez donc un bloc `then...catch...` pour obtenir la réponse.

```javascript
      .then((res) => {
        msgs.push(res.data.choices[0].message);
        setChats(msgs);
        setIsTyping(false);
      })
      .catch((error) => {
        console.log(error);
      });
```

Ce code ajoute le message retourné par l'IA dans le tableau `chats` et définit `isTyping` sur false, indiquant que l'IA a terminé de répondre.   
  
Vous devriez maintenant recevoir un retour (`Typing`) chaque fois que vous envoyez un message :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682702095176_Screenshot+2023-04-28+at+18.14.08.png)
_Application de chat donnant un retour lorsque l'IA est sur le point de répondre_

Il est temps d'afficher l'historique du chat pour que l'utilisateur puisse le voir.  
  
Tapez le code suivant juste en dessous de la balise `h1` :

```javascript
      <section>
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p key={index} className={chat.role === "user" ? "user_msg" : ""}>
                <span>
                  <b>{chat.role.toUpperCase()}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>
```

Le code ci-dessus parcourt les `chats` et les affiche un par un à l'utilisateur. Il affiche le `role` en majuscules et le `content` du message côte à côte.  
  
Voici à quoi devrait ressembler la sortie :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682702531307_Screenshot+2023-04-28+at+18.21.23.png)
_ChatBot fonctionnant comme prévu sans CSS_

Cela a l'air cool !   
  
Mais ajouter un peu de style lui donnera un look engageant comme [WhatsApp](https://www.whatsapp.com/) ou [Messenger](https://www.messenger.com/).   
  
Remplacez le contenu du fichier `src/index.css` par ce qui suit :

```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
h1 {
  font-size: 3.2em;
  line-height: 1.1;
  text-align: center;
  position: sticky;
  top: 0;
  background-color: #242424;
}
main{
  max-width: 500px;
  margin: auto;
}
p{
  background-color: darkslategray;
  max-width: 70%;
  padding: 15px;
  border-radius: 50px;
}
p span{
  margin: 5px;
}
p span:first-child{
  margin-right: 0;
}
.user_msg{
  text-align: right;
  margin-left: 30%;
  display: flex;
  flex-direction: row-reverse;
}
.hide {
  visibility: hidden;
  display: none;
}
form{
  text-align: center;
  position: sticky;
  bottom: 0;
}
input{
  width: 100%;
  height: 40px;
  border: none;
  padding: 10px;
  font-size: 1.2rem;
}
input:focus{
  outline: none;
}
```

Et supprimez tous les styles du fichier `src/App.css`.

Vous pouvez trouver le [code complet sur GitHub](https://github.com/EBEREGIT/react-chatgpt-tutorial).  
  
L'application devrait maintenant avoir un nouveau look :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682704193641_Screenshot+2023-04-28+at+18.48.44.png)
_ChatBot fonctionnant comme prévu avec CSS_

Cela conclut la création d'un chatbot avec React et ChatGPT. Ce n'est pas aussi difficile que cela en a l'air.  
  
Mais les applications frontend comme celle-ci sont meilleures pour la démonstration, pas pour la production. Le problème avec la création de l'application de cette manière est que le frontend expose la clé API aux cyberattaques. 

Pour résoudre ce problème, il peut être judicieux d'enregistrer la clé API et l'ID de l'organisation quelque part en sécurité dans le cloud et de les référencer ou de créer un backend pour votre application avec une meilleure sécurité.  
  
La section suivante travaillera sur le problème.

## Comment combiner React et Node.js pour créer un logiciel d'IA de chat Fullstack

Cette section combinera les forces des sections précédentes pour créer une application plus sécurisée tout en exhibant une meilleure UI et UX. 

Nous améliorerons la section Node en utilisant un serveur pour exposer un endpoint pour la consommation du frontend et simplifier le frontend pour interagir avec le backend au lieu de contacter [OpenAI](https://openai.com/) directement.

%[https://youtu.be/OJ7AgZVH118]

### Comment configurer le projet

Cette partie créera les dossiers et fichiers nécessaires pour le projet.  
  
Créez le répertoire du projet :

```cmd
mkdir react-node-chatgpt-tutorial
```

Naviguez dans le dossier :

```cmd
cd react-node-chatgpt-tutorial
```

Installez React en utilisant Vite et nommez le dossier `frontend`. Utilisez cette commande :

```cmd
npm create vite@latest
```

Après cela, vous naviguerez dans le dossier et exécuterez la commande suivante :

```cmd
npm install
npm run dev
```

Ces commandes installeront les dépendances nécessaires et démarreront le serveur local sur le port `5173`.  
  
Créez le dossier backend :

```cmd
mkdir backend
```

Maintenant, naviguez dans le dossier backend et initialisez le projet avec cette commande :

```cmd
npm init -y
```

Cela créera un fichier `package.json` pour suivre les détails du projet.  
  
Ajoutez la ligne de code suivante au fichier :

```javascript
"type": "module"
```

Cela permettra l'utilisation de l'instruction d'importation de module ES6.  
  
Installez [OpenAI](https://openai.com/) et d'autres dépendances avec la commande suivante :

```cmd
npm i openai body-parser cors express
```

Créez un fichier où tout le code résidera. Nommez-le `index.js` :

```
touch index.js
```

Cela complète la configuration du projet. Il y a maintenant deux dossiers (`frontend` et `backend`).

### Comment construire un serveur 

Cette partie se concentrera sur la création d'un serveur local pour écouter sur le port `8000`.

La première chose à faire est d'importer les modules nécessaires comme ceci :

```javascript
import { Configuration, OpenAIApi } from "openai";
import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
```

Ensuite, configurez `express`, un `port` à écouter, le `body-parser` pour recevoir l'entrée, et `cors` pour permettre des communications libres entre le frontend et le backend. Utilisez le code ci-dessous :

```javascript
const app = express();
const port = 8000;
app.use(bodyParser.json());
app.use(cors());
```

Enfin, tapez le code suivant :

```javascript
app.listen(port, () => {
  console.log(`listening on port ${port}`);
});
```

Cela complète la configuration du serveur.  
  
Lorsque vous exécutez `index.js`, vous devriez obtenir la sortie suivante :

```
listening on port 8000
```

### Comment créer un endpoint

Dans cette partie, nous allons construire un endpoint qui recevra les messages du frontend en utilisant le corps de la requête et retournera une réponse à l'appelant.  
  
Commencez par établir les paramètres de configuration comme nous l'avons fait dans les sections précédentes :

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
const openai = new OpenAIApi(configuration);
```

Ensuite, créez une route POST asynchrone en utilisant le code ci-dessous :

```javascript
app.post("/", async (request, response) => {
  
});
```

Cet endpoint sera appelé en utilisant `http://localhost:8000/`  
  
Dans la fonction de rappel, entrez le code ci-dessous pour recevoir l'entrée `chats` du corps de la requête (`request.body`) :

```javascript
const { chats } = request.body;
```

Maintenant, appelez l'endpoint `createChatCompletion` comme nous l'avons fait dans la section React :

```javascript
  const result = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: "Vous êtes un EbereGPT. Vous pouvez aider avec les tâches de conception graphique",
      },
      ...chats,
    ],
  });
```

La différence ici est qu'au lieu d'utiliser le bloc `then...catch...`, nous l'avons assigné à une variable (`result`) et retourné la réponse en utilisant `response.json()` comme dans le code suivant :

```javascript
  response.json({
    output: result.data.choices[0].message,
  });
```

Trouvez le code pour cette partie sur [GitHub ici](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial/tree/master/backend).  
  
Voici la sortie lors du test sur Postman :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682943795836_Screenshot+2023-05-01+at+13.22.17.png)
_Sortie de Postman_

Cela conclut la partie backend du code. La partie suivante connectera le frontend au backend en utilisant l'endpoint (`http://localhost:8000/`) nouvellement créé.

### Comment se connecter au backend depuis le frontend.

Cette partie nous amène au frontend, où nous allons créer un formulaire. Le formulaire enverra un message au backend via l'endpoint de l'API et recevra une réponse par le même moyen.  
  
Naviguez vers le fichier `frontend/src/App.jsx` et tapez le code suivant :

```javascript
import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);

  const chat = async (e, message) => {
    e.preventDefault();

    if (!message) return;
    setIsTyping(true);

    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");

    alert(message);
  };

  return (
    <main>
      <h1>Tutoriel FullStack Chat AI</h1>

      <section>
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p key={index} className={chat.role === "user" ? "user_msg" : ""}>
                <span>
                  <b>{chat.role.toUpperCase()}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>

      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>

      <form action="" onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Tapez un message ici et appuyez sur Entrée..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
    </main>
  );
}
export default App;
```

Ce code est similaire au code de la section précédente. Mais nous avons supprimé les configurations OpenAI car nous n'en aurons plus besoin dans cette section. 

À ce stade, une alerte apparaît chaque fois que le formulaire est soumis. Cela changera dans un instant.  
  
Dans la fonction chat, supprimez le message `alert` et tapez ce qui suit :

```javascript
fetch("http://localhost:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        chats,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        msgs.push(data.output);
        setChats(msgs);
        setIsTyping(false);
      })
      .catch((error) => {
        console.log(error);
      });
```

Le code ci-dessus appelle l'endpoint que nous avons créé et transmet le tableau `chats` pour qu'il soit traité. Il retourne ensuite une réponse qui est ajoutée aux `chats` et affichée dans l'interface utilisateur.  
  
Voici à quoi ressemble l'interface utilisateur pour le moment :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682945738011_Screenshot+2023-05-01+at+13.55.10.png)
_Interface utilisateur du chat Fullstack avant le style_

L'interface utilisateur peut avoir meilleure allure si vous ajoutez les styles suivants au fichier `frontend/src/index.css` :

```css

:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

html, body{
  scroll-behavior: smooth;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
  text-align: center;
  position: sticky;
  top: 0;
  background-color: #242424;
}

main{
  max-width: 800px;
  margin: auto;
}

p{
  background-color: darkslategray;
  max-width: 70%;
  padding: 15px;
  border-radius: 50px;
}

p span{
  margin: 5px;
}

p span:first-child{
  margin-right: 0;
}

.user_msg{
  text-align: right;
  margin-left: 30%;
  display: flex;
  flex-direction: row-reverse;
}

.hide {
  visibility: hidden;
  display: none;
}

form{
  text-align: center;
  position: sticky;
  bottom: 0;
}

input{
  width: 100%;
  height: 40px;
  border: none;
  padding: 10px;
  font-size: 1.2rem;
  background-color: rgb(28, 23, 23);
}

input:focus{
  outline: none;
}
```

Et supprimez tous les styles du fichier `frontend/src/App.css`.

Le code pour cette partie est sur [GitHub](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial/tree/master/frontend).  
  
Voici la sortie finale :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682946018213_Screenshot+2023-05-01+at+13.59.37.png)
_ChatBot FullStack fonctionnant comme prévu avec CSS_

Félicitations pour avoir terminé ce projet !  
  
Le chatbot full stack a demandé plus de travail, mais il nous a aidés à séparer les préoccupations, à construire une application plus sécurisée et attrayante, et à offrir une meilleure expérience aux utilisateurs. Donc cela en valait la peine.  
  
Vous pouvez trouver le [code pour cette section sur GitHub](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial).

## Conclusion

Ce tutoriel a, espérons-le, montré que toute personne ayant des connaissances de base en programmation peut créer des logiciels alimentés par l'IA. Vous avez appris à créer un chatbot en utilisant React et Node.js, et nous avons discuté des avantages et des inconvénients de chaque technologie. Enfin, nous avons construit une solution à la fois fonctionnelle, sécurisée et visuellement attrayante.  
  
Après avoir lu ce tutoriel, vous pouvez maintenant explorer les fonctionnalités de l'IA comme la manipulation d'images et l'interaction audio. Prenez votre temps pour parcourir la [documentation](https://platform.openai.com/docs/introduction) et voir comment vous pouvez développer ce que nous avons couvert ici.