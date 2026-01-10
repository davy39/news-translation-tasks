---
title: Comment créer une application de chat en temps réel avec ReactJS et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-13T22:26:07.000Z'
originalURL: https://freecodecamp.org/news/building-a-real-time-chat-app-with-reactjs-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Cover-Images-freeCodeCamp.png
tags:
- name: Chat
  slug: chat
- name: Firebase
  slug: firebase
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de chat en temps réel avec ReactJS et Firebase
seo_desc: "By Timonwa Akintokun\nIn this article, I'm going to show you how to build\
  \ a real-time chat app using React.js and Firebase. \nIn the app, we will allow\
  \ the user to log in with their Google account using Firebase's Google sign-in Authentication.\
  \ We will..."
---

Par Timonwa Akintokun

Dans cet article, je vais vous montrer comment créer une application de chat en temps réel en utilisant React.js et Firebase. 

Dans l'application, nous permettrons à l'utilisateur de se connecter avec son compte Google en utilisant l'authentification de connexion Google de Firebase. Nous stockerons et récupérerons également tous les messages de la salle de chat en utilisant Cloud Firestore de Firebase.

## Prérequis

Vous devez avoir Node.js installé sur votre système. Vous devez également avoir des connaissances intermédiaires en CSS, JavaScript et Reactjs. Enfin, vous devez savoir comment utiliser le terminal de commande. Vous n'avez pas besoin de savoir comment utiliser Firebase.

## Qu'est-ce que Firebase ?

Firebase est un Backend-as-a-Service (Baas). C'est une plateforme de développement d'applications soutenue par Google qui permet aux développeurs de créer des applications iOS, Android et web. 

Il fournit des outils pour suivre les analyses, signaler et corriger les plantages d'applications, et créer des expériences marketing et produit. Ceux-ci aident les développeurs à développer des applications de qualité, à développer leur base d'utilisateurs et à réaliser des profits. 

Nous utiliserons deux de leurs outils : Firebase Authentication et Cloud Firestore.

### **Firebase Authentication**

Firebase Authentication (SDK) est un outil Firebase qui prend en charge différentes méthodes d'authentification comme les mots de passe, les numéros de téléphone, Google, Facebook, Twitter, Github, et plus encore. Dans cette application, nous utiliserons l'authentification de connexion Google.

### **Cloud Firestore**

Cloud Firestore est un serveur de base de données NoSQL basé sur le cloud pour stocker et synchroniser des données. Il stocke les données dans des documents sous forme de paires clé-valeur, et les documents sont organisés en collections. 

Les documents peuvent également avoir des sous-collections, vous permettant d'imbriquer des collections dans des collections. Les données sont également synchronisées automatiquement entre tous les appareils à l'écoute.

Maintenant que vous avez une idée de comment Firebase et Cloud Firestore fonctionnent, construisons notre application.

**Note :** Pour la portée de cet article, j'ai déjà pré-écrit le CSS et pré-construit les composants pour l'application de chat. Vous pouvez trouver le code final du projet sur [GitHub](https://github.com/Timonwa/react-chat) et le CSS et les composants dans le [dossier setup](https://github.com/Timonwa/react-chat/tree/main/setup). Vous pouvez également voir le projet final avec ce [lien live](https://react-chat-timonwa.vercel.app/).

## Comment créer notre application React

Clonez ce [dépôt GitHub](https://github.com/Timonwa/react-chat), supprimez le dossier src dans le répertoire racine et remplacez-le par le dossier src situé dans le [dossier setup](https://github.com/Timonwa/react-chat/tree/main/setup). 

Alternativement, vous pouvez créer votre application React en exécutant le code dans votre terminal, `npx create-react-app react-chat`, pour la créer. Ici, `react-chat` est le nom de l'application. Ensuite, vous pouvez exécuter `npm install firebase react-firebase-hooks` pour installer **firebase** et **react-firebase-hooks**. 

Supprimez le dossier **src** actuel et remplacez-le par celui du [dossier setup](https://github.com/Timonwa/react-chat/tree/main/setup) pour utiliser le CSS pré-écrit et les composants pré-construits. (Optionnellement, vous pouvez écrire les vôtres vous-même.)

Votre nouveau dossier **src** contient maintenant les éléments suivants : 

* un dossier components avec un composant **NavBar** ayant les boutons **Google sign-in** et **Sign Out**, 
* un composant **Welcome** qui sera visible pour l'utilisateur non connecté, 
* un composant **Chatbox** qui sera visible uniquement lorsque l'utilisateur est connecté, 
* le composant **Message** pour afficher le message d'un utilisateur, et 
* un composant **SendMessage** afin que l'utilisateur puisse saisir et envoyer ses messages.

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667917866994_image2.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667917866994_image2.png)

Il contient également :

* un dossier **img** où l'image de connexion Google pour le bouton de connexion est stockée,
* un fichier **App.css** avec les codes CSS pré-écrits, 
* le nouveau fichier **App.js** avec tous nos composants importés, 
* et le fichier **index.js**. 

Exécutez `npm start` pour voir l'application dans le navigateur. Notre application devrait ressembler à ceci :

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667916861885_image1.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667916861885_image1.png)
_Notre application React_

Maintenant, créons un compte Firebase et configurons notre projet Firebase.

## Comment configurer le projet Firebase

Si vous n'avez pas déjà de compte [Firebase](https://firebase.google.com/), vous pouvez en ouvrir un en utilisant votre Gmail (vous ne pouvez utiliser que [google mail](https://mail.google.com/mail/)). Sur la page d'accueil, cliquez sur **Get started** puis sur **Add project**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667929969308_image3.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667929969308_image3.png)

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667929996407_image4.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667929996407_image4.png)
_Comment configurer un projet Firebase_

Remplissez le formulaire **Create a project** en fournissant un nom de projet. Si vous souhaitez activer Google Analytics pour votre projet, laissez-le activé. Sinon, désactivez-le. Après cela, cliquez sur **Create project**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667930368482_image5.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667930368482_image5.png)
_Créer un projet_

Une fois créé, cliquez sur **Continue**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667930783189_image8.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667930783189_image8.png)
_Ce que vous verrez pendant que Firebase crée votre projet._

Choisissez le type d'application où vous souhaitez ajouter Firebase. Pour cet article, nous avons choisi l'icône de code car nous construisons une application web. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667931932857_image9.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667931932857_image9.png)
_Choisissez le type d'application auquel vous souhaitez ajouter Firestore_

Entrez un surnom pour votre application et cliquez sur **Register app**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667934485512_image10.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667934485512_image10.png)
_Enregistrez votre application_

Ensuite, sélectionnez `npm`, copiez le snippet de code en dessous (nous l'utiliserons plus tard), et cliquez sur **Continue to console**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667934988668_image11.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667934988668_image11.png)
_Snippet de code_

## Comment configurer l'authentification Firebase

Pour configurer l'authentification Firebase, allez dans le menu sur le côté gauche de l'écran, cliquez sur **Build**, et sélectionnez **Authentication** dans le menu déroulant. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937032772_image12.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937032772_image12.png)
_Sélectionnez l'authentification dans le menu déroulant_

Cliquez sur **Get started** et sélectionnez **Google** dans l'onglet **Sign-in method's**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937105063_image13.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937105063_image13.png)
_Choisissez votre méthode de connexion d'authentification_

Activez **Google**, choisissez votre **Project support email**, et cliquez sur **Save**. 

![https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937310260_image14.png](https://paper-attachments.dropboxusercontent.com/s_B6DDEC735898D3445BBF655B53FFE42B53361DCD6229DE6836CD5302F930DF9D_1667937310260_image14.png)

## Comment configurer Cloud Firestore

Encore une fois, allez dans le menu sur le côté gauche de l'écran. Cliquez sur **Build** et sélectionnez **Firestore Database** dans le menu déroulant. Ensuite, cliquez sur **Create database** et remplissez le formulaire. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image9-2.png)
_Configuration de Cloud Firestore_

Sélectionnez le mode dans lequel vous souhaitez que votre base de données fonctionne, production ou test. 

Le mode test signifie que tout client aura un accès en lecture/écriture à votre base de données pendant 30 jours. Le mode production signifie que personne n'aura d'accès en lecture/écriture à votre base de données. Vous devrez modifier vos règles pour accorder l'accès à des clients spécifiques. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image10-2.png)
_Choisissez le mode test ou le mode production (nous choisissons le mode production)._

Sélectionnez **production mode** et cliquez sur **Next**. 

Sélectionnez un emplacement où vous souhaitez que votre Firestore soit stocké et cliquez sur **Enable**. Il sera par défaut à l'emplacement le plus proche de vous. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image11-2.png)
_Définissez un emplacement (par défaut, l'emplacement le plus proche de vous)_

Ensuite, nous modifions nos règles. Cliquez sur l'onglet **Rules** et modifiez les règles, 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image12-2.png)
_Modifiez les règles via l'onglet Rules_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image13-2.png)
_Règle à remplacer_

Remplacez la règle actuelle par le code ci-dessous et cliquez sur **Publish**. 

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if true;
      allow create, update, delete, write: if request.auth != null;
    }
  }
}
```

Le `allow read: if true;` signifie que n'importe qui peut lire votre base de données. Le `allow create, update, delete, write: if request.auth != null;` signifie que seuls les clients authentifiés peuvent créer, mettre à jour, supprimer et écrire dans votre base de données. 

Vous pouvez soit commencer à ajouter/créer une collection dans votre base de données, soit en créer une automatiquement dans votre application React, ce que nous ferons plus tard. Si vous souhaitez créer une collection dans Cloud Firestore, retournez à l'onglet de données en cliquant sur **Data** à côté de **Rules**, puis cliquez sur **Add Collection**. 

Entrez le nom de la collection, par exemple "messages", et cliquez sur **Next**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image14-2.png)
_Démarrer une collection dans Firestore_

Maintenant, créez un **document** pour la Collection. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image15-1.png)
_Création d'un document pour la collection_

Vous pouvez soit cliquer sur **Auto_ID** pour générer un identifiant pour le document, soit en entrer un vous-même. 

Après cela, créez les paires clé-valeur du Document. L'entrée **Field** représente le nom de la clé, le **Type** définit le type de données (chaîne, nombre, horodatage, etc.), et la **Value** est la valeur de la clé. 

Vous pouvez également ajouter plus de documents en cliquant sur le signe plus, sinon, cliquez sur **Save** pour sauvegarder votre collection. 

Notre projet Firebase est configuré. Retournez à notre application React. 

## Comment configurer Firebase dans React

Dans notre dossier **src**, créez un fichier appelé `firebase.js` et collez le code que nous avions copié. 

Importons également les services `getAuth` et `getFirestore` depuis les bibliothèques **auth** et **firestore** de Firebase, respectivement, et exportons-les. Vous pouvez en savoir plus sur les bibliothèques disponibles de Firebase dans leur [documentation](https://firebase.google.com/docs/web/setup#available-libraries). 

Notre configuration Firebase devrait ressembler à ceci : 

```js
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: REACT_APP_API_KEY_GOES_HERE,
  authDomain: REACT_APP_AUTH_DOMAIN_GOES_HERE,
  projectId: REACT_APP_PROJECT_ID_GOES_HERE,
  storageBucket: REACT_APP_STORAGE_BUCKET_GOES_HERE,
  messagingSenderId: REACT_APP_MESSSAGING_SENDER_ID_GOES_HERE,
  appId: REACT_APP_APP_ID_GOES_HERE,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
```

## Comment implémenter Firebase dans notre application React

### **Comment authentifier les utilisateurs avec leur compte Google**

Nous voulons que nos utilisateurs aient accès à la salle de chat et puissent envoyer des messages s'ils sont connectés. Ils devraient voir la page de bienvenue s'ils ne le sont pas. Ils devraient également voir le bouton Sign Out s'ils sont connectés et le bouton Google Sign-in s'ils ne le sont pas. 

Cette authentification sera gérée dans notre composant NavBar, qui contient nos boutons de connexion et de déconnexion. 

Dans notre composant `NavBar`, nous importons actuellement notre image de connexion Google et la stockons sous forme de const appelée `GoogleSignin`. Nous avons également un état appelé `user` défini sur false, une fonction `googleSignIn` qui définit l'état de l'utilisateur sur `true`, et une fonction `signOut` qui définit l'état de l'utilisateur sur `false`. 

Nous avons également un élément `nav` avec une balise `h1` représentant le titre de notre application et deux boutons rendus conditionnellement en fonction de l'état de l'utilisateur. 

```js
import React, { useState } from "react";
import GoogleSignin from "../img/btn_google_signin_dark_pressed_web.png";

const NavBar = () => {
  const [user, setUser] = useState(false);
  const googleSignIn = () => {
    setUser(true);
  };
  const signOut = () => {
    setUser(false);
  };
  return (
    <nav className="nav-bar">
      <h1>React Chat</h1>
      {user ? (
        <button onClick={signOut} className="sign-out" type="button">
          Sign Out
        </button>
      ) : (
        <button className="sign-in">
          <img
            onClick={googleSignIn}
            src={GoogleSignin}
            alt="sign in with google"
            type="button"
          />
        </button>
      )}
    </nav>
  );
};
export default NavBar;
```

Apportons des modifications au composant **NavBar**. Importons ce qui suit : 

```js
import { auth } from "../firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { GoogleAuthProvider, signInWithRedirect } from "firebase/auth";
```

Remplacez l'état de l'utilisateur par le code ci-dessous : 

`const [user] = useAuthState(auth);`

Et modifiez les fonctions googleSignIn et signOut : 

```js
const googleSignIn = () => {
  const provider = new GoogleAuthProvider();
  signInWithRedirect(auth, provider);
};
const signOut = () => {
  auth.signOut();
};
```

La fonction `useAuthState` est déclenchée lorsque l'utilisateur se connecte ou se déconnecte, nous permettant d'accéder aux détails de l'utilisateur. Actuellement, l'état de l'utilisateur est `null`. Une fois connecté, l'état de l'utilisateur changera pour les données fournies par la méthode d'authentification - dans ce cas, Google. 

Dans la fonction `googleSignIn`, nous informons Firebase que l'utilisateur souhaite se connecter avec Google en utilisant `GoogleAuthProvider()`. Il le redirige également vers la page de connexion de Google. 

Après que l'utilisateur se soit connecté avec succès, ses données sont sauvegardées dans `auth`, et l'utilisateur est redirigé vers notre application. La fonction `signOut` efface les données d'authentification, les ramenant à `null`. Le nouvel état de l'utilisateur détermine également quels boutons d'authentification sont rendus à l'utilisateur. 

Ajoutons également l'authentification à notre fichier **App.js**. Importons ce qui suit : 

```js
import { auth } from "./firebase";
import { useAuthState } from "react-firebase-hooks/auth";
```

Ajoutez le nouvel état de l'utilisateur afin que nous puissions l'utiliser pour rendre le composant **Welcome** si l'utilisateur n'est pas connecté ou le composant **Chatbox** si l'utilisateur est connecté. 

```js
const [user] = useAuthState(auth);
```

Le code final ressemble à ceci : 

```js
import { auth } from "./firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import "./App.css";
import NavBar from "./components/NavBar";
import ChatBox from "./components/ChatBox";
import Welcome from "./components/Welcome";

function App() {
  const [user] = useAuthState(auth);
  return (
    <div className="App">
      <NavBar />
      {!user ? <Welcome /> : <ChatBox />}
    </div>
  );
}
export default App;
```

Testons nos nouvelles fonctions de connexion et de déconnexion, nous voyons ce qui suit : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-b6465d1647-1.gif)
_Démo de l'application_

Maintenant, faisons de même pour notre composant **Welcome**, qui contient actuellement le code suivant : 

```js
import React from "react";
import GoogleSignin from "../img/btn_google_signin_dark_pressed_web.png";

const Welcome = () => {
  const googleSignIn = () => {};

  return (
    <main className="welcome">
      <h2>Welcome to React Chat.</h2>
      <img src="/logo512.png" alt="ReactJs logo" width={50} height={50} />
      <p>Sign in with Google to chat with with your fellow React Developers.</p>
      <button className="sign-in">
        <img
          onClick={googleSignIn}
          src={GoogleSignin}
          alt="sign in with google"
          type="button"
        />
      </button>
    </main>
  );
};
export default Welcome;
```

Nous importons ce qui suit : 

```js
import { auth } from "../firebase";
import { GoogleAuthProvider, signInWithRedirect } from "firebase/auth";
```

et modifions également la fonction googleSignIn : 

```js
const googleSignIn = () => {
    const provider = new GoogleAuthProvider();
    signInWithRedirect(auth, provider);
};
```

Maintenant, nous pouvons également nous connecter à partir du deuxième bouton de connexion : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/video2-1.gif)
_Démo de l'application mise à jour_

### **Comment envoyer et stocker des messages dans Firebase**

Actuellement, nous affichons un message fictif depuis notre composant **Message**, et le bouton **Send** ne effectue aucune action. Lorsque l'utilisateur saisit un message et clique sur le bouton **Send**, nous voulons que le message soit immédiatement visible dans la salle de chat. 

Avec notre composant **SendMessage** actuel ayant le code ci-dessous, modifions-le : 

```js
import React from "react";

const SendMessage = () => {
  return (
    <form className="send-message">
      <label htmlFor="messageInput" hidden>
        Enter Message
      </label>
      <input
        id="messageInput"
        name="messageInput"
        type="text"
        className="form-input__input"
        placeholder="type message..."
      />
      <button type="submit">Send</button>
    </form>
  );
};
export default SendMessage;
```

Tout d'abord, nous importons `useState` depuis React, `auth` et `db` depuis notre fichier de configuration firebase, et `addDoc`, `collection` et `serverTimestamp` depuis la bibliothèque Firestore. 

```js
import React, { useState } from "react";
import { auth, db } from "../firebase";
import { addDoc, collection, serverTimestamp } from "firebase/firestore";
```

Nous créons un état appelé `message` qui est initialement défini sur une chaîne vide et passé en tant que valeur à la balise `input`. Une fonction `onChange` est également ajoutée à l'input, qui définit l'état `message` sur ce que l'utilisateur tape. 

```js
const SendMessage = () => {
  const [message, setMessage] = useState("");
    
  return (
    <form className="send-message">
      <input
        ...
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
};
```

Nous créons également une fonction appelée `sendMessage`, et nous ajoutons un attribut `onSubmit` à notre formulaire, qui exécute la fonction `sendMessage` lorsque l'utilisateur clique sur `Send`. Notez que le bouton doit avoir `type="submit"` pour que l'attribut `onSubmit` fonctionne. 

```js
 const sendMessage = async (event) => {
    event.preventDefault();
    if (message.trim() === "") {
      alert("Enter valid message");
      return;
    }
    const { uid, displayName, photoURL } = auth.currentUser;
    await addDoc(collection(db, "messages"), {
      text: message,
      name: displayName,
      avatar: photoURL,
      createdAt: serverTimestamp(),
      uid,
    });
    setMessage("");
  };
  
  return (
    <form onSubmit={(event) => sendMessage(event)} className="send-message">
...
```

La fonction `sendMessage` est une fonction asynchrone. Elle vérifie d'abord si l'utilisateur essaie d'envoyer une chaîne vide ou des espaces blancs comme message et alerte l'utilisateur. 

Si le message n'est pas une chaîne vide, elle obtient l'**uid**, le **displayName** et le **photoURL** de l'utilisateur à partir des données `auth` fournies lorsqu'ils se connectent. Cela correspond à l'**id unique**, au **nom complet** et à l'**URL de la photo** de l'utilisateur, respectivement. 

Une fois cela fait, elle utilise `addDoc()` pour créer un **document** à l'intérieur d'une **collection** appelée **messages** dans notre **base de données**, à laquelle nous avons accès via l'importation `db`. Si la **collection** n'existe pas, elle la créera pour nous. 

Elle crée également des **paires clé-valeur**, stockant notre **message** dans **text**, **displayName** dans **name**, stockant l'**heure** à laquelle le message a été sauvegardé dans notre base de données dans **createdAt**, et ensuite l'**uid** de l'utilisateur. 

Ces paires clé-valeur sont ce qui constitue les données de notre document. Après cela, elle réinitialise l'état du message à une chaîne vide. 

### **Comment récupérer les messages de notre base de données**

Après avoir envoyé le message de l'utilisateur, nous devons l'afficher à l'écran pour l'utilisateur. Allons dans notre composant **ChatBox**, nous importons ce qui suit : 

```js
import { useEffect, useRef, useState } from "react";
import {
  query,
  collection,
  orderBy,
  onSnapshot,
  limit,
} from "firebase/firestore";
import { db } from "../firebase";
```

Nous créons un hook `useEffect` qui s'exécutera chaque fois que des modifications sont apportées dans la salle de chat, comme l'envoi ou la suppression d'un message. 

```js
useEffect(() => {
  const q = query(
    collection(db, "messages"),
    orderBy("createdAt", "desc"),
    limit(50)
  );
  const unsubscribe = onSnapshot(q, (QuerySnapshot) => {
    const fetchedMessages = [];
    QuerySnapshot.forEach((doc) => {
      fetchedMessages.push({ ...doc.data(), id: doc.id });
    });
    const sortedMessages = fetchedMessages.sort(
      (a, b) => a.createdAt - b.createdAt
    );
    setMessages(sortedMessages);
  });
  return () => unsubscribe;
}, []);
```

Dans ce hook `useEffect`, nous avons une const `q`, une requête Firebase qui interroge notre base de données à la recherche d'une **collection de messages**. Elle **trie** ensuite les documents de la collection en fonction de la clé **createdAt**, et retourne un maximum de **50** documents (messages sauvegardés). 

La const `unsubscribe` représente la fonction `onSnapshot` qui écoute les changements dans le document. Elle a un tableau vide appelé `messages`. 

La boucle `forEach` parcourt tous les **documents** de la **collection** et sauvegarde les données dans le nouveau tableau. Elle définit ensuite le tableau de messages initial sur le nouveau tableau de messages. 

Nous utilisons également une **fonction map** sur notre tableau de messages pour rendre chaque donnée de message/document dans notre composant **Message**. 

```js
{messages?.map((message) => (
  <Message key={message.id} message={message} />
))}
```

Le code final ressemble à ceci : 

```js
import React, { useEffect, useRef, useState } from "react";
import {
  query,
  collection,
  orderBy,
  onSnapshot,
  limit,
} from "firebase/firestore";
import { db } from "../firebase";
import Message from "./Message";
import SendMessage from "./SendMessage";

const ChatBox = () => {
  const [messages, setMessages] = useState([]);
  const scroll = useRef();

  useEffect(() => {
    const q = query(
      collection(db, "messages"),
      orderBy("createdAt", "desc"),
      limit(50)
    );

    const unsubscribe = onSnapshot(q, (QuerySnapshot) => {
      const fetchedMessages = [];
      QuerySnapshot.forEach((doc) => {
        fetchedMessages.push({ ...doc.data(), id: doc.id });
      });
      const sortedMessages = fetchedMessages.sort(
        (a, b) => a.createdAt - b.createdAt
      );
      setMessages(sortedMessages);
    });
    return () => unsubscribe;
  }, []);

  return (
    <main className="chat-box">
      <div className="messages-wrapper">
        {messages?.map((message) => (
          <Message key={message.id} message={message} />
        ))}
      </div>
      {/* when a new message enters the chat, the screen scrolls down to the scroll div */}
      <span ref={scroll}></span>
      <SendMessage scroll={scroll} />
    </main>
  );
};

export default ChatBox;
```

Allons dans notre composant **Message**, et rendons les données qui lui sont passées dans notre navigateur. 

```js
import React from "react";
import { auth } from "../firebase";
import { useAuthState } from "react-firebase-hooks/auth";
const Message = ({ message }) => {
  const [user] = useAuthState(auth);

  return (
    <div
      className={`chat-bubble ${message.uid === user.uid ? "right" : ""}`}>
      <img
        className="chat-bubble__left"
        src={message.avatar}
        alt="user avatar"
      />
      <div className="chat-bubble__right">
        <p className="user-name">{message.name}</p>
        <p className="user-message">{message.text}</p>
      </div>
    </div>
  );
};
export default Message;

```

Nous avons importé `auth` et `useAuthState`, et stocké les détails de l'utilisateur dans `user`. Nous avons déstructuré la prop messages et passé l'avatar dans l'attribut src de l'image. Nous avons également remplacé le nom et le message fictifs par ceux obtenus à partir des données du message. 

Nous avons également conditionné un style CSS pour qu'il prenne effet en fonction de l'uid de l'auteur du message. Ainsi, si l'uid de l'auteur du message est le même que l'uid de la personne connectée, alors les styles CSS stockés dans le sélecteur **right** doivent être ajoutés à la div. Sinon, aucun nouveau style ne doit être ajouté. 

Actuellement, tous les messages sont positionnés à gauche, donc si l'utilisateur connecté est l'auteur du message, son message doit être positionné à droite. Visualisons ces changements dans notre navigateur : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/video3-1.gif)
_Démo de l'application mise à jour_

Le message est envoyé et stocké dans notre base de données. Ensuite, tous les messages sont récupérés, et la salle de chat est mise à jour en temps réel avec les nouveaux messages. 

Le nom et l'avatar de l'utilisateur sont également présents sur la carte de message. Mais nous pouvons également voir que le chat ne fait pas défiler vers le bas lorsqu'un nouveau message arrive. Corrigons cela. 

### **Comment ajouter le défilement vers le bas**

Allons dans notre **ChatBox.js**, nous importons le hook `useRef` et créons une const appelée `scroll` : 

```js
import React, { useEffect, useRef, useState } from "react";
...
const scroll = useRef();
```

Nous créons ensuite un élément `span` avec un attribut `ref` dont la valeur est **scroll**, et passons également le **scroll** dans notre composant **Messages** : 

```js
<main className="chat-box">
   ...
   {/* when a new message enters the chat, the screen scrolls dowwn to the scroll div */}
   <span ref={scroll}></span>
   <SendMessage scroll={scroll} />
</main>
```

Nous allons ensuite dans le composant **Messages**, accédons à la const scroll, et ajoutons `scroll.current.scrollIntoView({ behavior: "smooth" })` en bas de notre fonction `sendMessage`. 

Ce code indique au navigateur de faire en sorte que la span de défilement soit visible dans le navigateur après l'envoi d'un message. C'est pourquoi la balise span a été placée en bas de tous les messages. 

```js
const SendMessage = ({ scroll }) => {

  const sendMessage = async (event) => {
   ...
    setMessage("");
    scroll.current.scrollIntoView({ behavior: "smooth" });
  };
  ...
};
```

En revenant au navigateur, nous devrions voir le chat défiler vers le bas lorsque l'utilisateur envoie un nouveau message. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/video4-1.gif)
_Démo montrant le chat défilant vers le bas avec un nouveau message_

## Comment ajouter des domaines autorisés

Lors du déploiement de notre application React, il est essentiel d'ajouter notre domaine à la liste des domaines autorisés dans Firebase. Cette étape garantit que notre application communique correctement avec les services Firebase. Voici comment procéder :

Dans la console Firebase, accédez à la section **Authentication** depuis la barre latérale gauche et cliquez sur l'onglet **Settings**. Faites défiler jusqu'à la section **Authorized Domains**, puis cliquez sur le bouton **Add Domain**. Ajoutez le ou les domaines sur lesquels votre application React sera déployée. 

Par exemple, si vous déployez votre application sur [https://my-react-chat-app.com](https://my-react-chat-app.com), entrez my-react-chat-app.com comme domaine autorisé. Cliquez sur le bouton **Add** pour appliquer les modifications. 

![Image](https://res.cloudinary.com/denkuysrh/image/upload/v1686503300/Article%20Images/freeCodeCamp/react-chat-app/FireShot_Capture_002_-_react-chat_-_Authentication_-_Firebase_console_-_console.firebase.google.com_yhkjop.png)

En ajoutant le domaine de votre application à la liste des domaines autorisés, vous accordez la permission aux services Firebase d'être accessibles depuis ce domaine. Sans ajouter le domaine, vous pourriez rencontrer des erreurs lors de la tentative d'établissement de connexions ou d'exécution d'opérations avec Firebase. 

## Conclusion

Et voilà pour la création d'une application de chat en temps réel. Félicitations ! 

Dans ce tutoriel, nous avons appris à utiliser Firebase et React pour créer une application de chat en temps réel. Nous avons également authentifié les utilisateurs en utilisant la méthode de connexion Google de Firebase Authentication et stocké les messages de la salle de chat dans une base de données en utilisant Cloud Firestore. Nous avons également appris à utiliser certains des services et bibliothèques de Firebase. 

Vous pouvez trouver le code de ce projet sur [GitHub](https://github.com/Timonwa/react-chat), et vous pouvez explorer la salle de chat en utilisant ce [lien live](https://react-chat-timonwa.vercel.app/). 

Si vous avez aimé cet article, envisagez de le partager pour aider d'autres développeurs. Vous pouvez également visiter [mon blog](https://blog.timonwa.com/) pour lire plus d'articles de ma part et vous pouvez vous connecter avec moi sur [Twitter](https://twitter.com/timonwa_) et [LinkedIn](https://www.linkedin.com/in/timonwa/). 

À la prochaine, les gars, salut ! 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/HoDL1vbXj-1.gif)