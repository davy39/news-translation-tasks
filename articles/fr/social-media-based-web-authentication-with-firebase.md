---
title: Comment configurer l'authentification Web des réseaux sociaux en utilisant
  Firebase
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-08-31T00:12:32.000Z'
originalURL: https://freecodecamp.org/news/social-media-based-web-authentication-with-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Article-Cover--3.png
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: social media
  slug: social-media
- name: Web App Security
  slug: web-app-security
seo_title: Comment configurer l'authentification Web des réseaux sociaux en utilisant
  Firebase
seo_desc: 'User authentication is extremely important in the context of web development.
  The way users log in affects their overall experience and engagement with an application.
  It also affects how they initially perceive it.

  Authentication techniques are cont...'
---

L'authentification des utilisateurs est extrêmement importante dans le contexte du développement web. La manière dont les utilisateurs se connectent affecte leur expérience globale et leur engagement avec une application. Cela affecte également leur perception initiale de celle-ci.

Les techniques d'authentification évoluent constamment à mesure que les sites de réseaux sociaux continuent de gagner en popularité. La possibilité de se connecter aux applications web en utilisant des comptes de réseaux sociaux est une avancée utile dans ce domaine.

Cet article explique comment vous pouvez améliorer le processus de connexion des utilisateurs pour les applications web en employant l'authentification via les réseaux sociaux grâce à Firebase. Il aborde les avantages, les méthodes de configuration et les approches d'intégration tout en offrant des directives utiles.

## Voici ce que nous allons couvrir :

1. [Pourquoi utiliser l'authentification par les réseaux sociaux ?](#heading-pourquoi-utiliser-lauthentification-par-les-reseaux-sociaux)
2. [Prérequis](#heading-prerequis)
3. [Qu'est-ce que Firebase et pourquoi l'utiliser pour l'authentification ?](#heading-quest-ce-que-firebase-et-pourquoi-lutiliser-pour-lauthentification)
4. [Comment configurer Firebase pour l'authentification par les réseaux sociaux](#heading-comment-configurer-firebase-pour-lauthentification-par-les-reseaux-sociaux)
5. [Comment configurer votre application React](#heading-comment-configurer-votre-application-react)
6. [Comment intégrer l'authentification par les réseaux sociaux dans votre application](#heading-comment-integrer-lauthentification-par-les-reseaux-sociaux-dans-votre-application)
7. [Offrir à la fois l'authentification par les réseaux sociaux et par email/mot de passe](#heading-offrir-a-la-fois-lauthentification-par-les-reseaux-sociaux-et-par-emailmot-de-passe)
8. [Conclusion](#heading-conclusion)

## Pourquoi utiliser l'authentification par les réseaux sociaux ?

Je suis sûr que vous en avez assez de la routine habituelle nom d'utilisateur-mot de passe lors de la connexion à une nouvelle plateforme. Cela implique souvent de créer un nouveau mot de passe sur-le-champ ou de recourir à des conventions de mot de passe non sécurisées qui pourraient accorder un accès non autorisé à vos nombreux comptes.

Heureusement, l'authentification par les réseaux sociaux offre certains avantages :

1. Expérience utilisateur sans effort : Les choix de connexion par les réseaux sociaux simplifient le processus d'inscription, rendant pratique pour les utilisateurs de commencer à utiliser l'application.
2. Sécurité renforcée : Les plateformes de réseaux sociaux mettent en œuvre des mesures de sécurité robustes qui peuvent renforcer la sécurité des utilisateurs de votre application.
3. Élimination des tracas liés aux mots de passe : Grâce à l'authentification par les réseaux sociaux, les utilisateurs sont soulagés du fardeau de se souvenir de nombreux mots de passe, réduisant ainsi l'inconvénient de la gestion des identifiants.
4. Réduction de l'abandon de compte : La connexion par les réseaux sociaux incite les utilisateurs à rejoindre et à interagir avec votre application, minimisant ainsi les chances qu'ils quittent le processus d'inscription inachevé.
5. Accès à des informations utilisateur fiables : Les plateformes de réseaux sociaux fournissent des informations substantielles sur les utilisateurs, qui peuvent être exploitées pour personnaliser l'expérience offerte par votre application.
6. Récupération de compte simplifiée : En cas de mots de passe oubliés, l'authentification par les réseaux sociaux présente une approche simple pour les utilisateurs de retrouver l'accès à leurs comptes.

En résumé, l'authentification par les réseaux sociaux offre une méthode pratique et sécurisée pour les utilisateurs de rejoindre et d'utiliser votre application. Cela conduit à une meilleure expérience utilisateur, à une diminution de l'abandon de compte et vous donne accès à des informations précieuses sur les utilisateurs.

## Prérequis

Cet article est destiné à ceux qui ont une solide compréhension des concepts suivants :

* HTML, CSS et JavaScript
* React et le routage React
* Familiarité fondamentale avec l'utilisation de Firebase

## Qu'est-ce que Firebase et pourquoi l'utiliser pour l'authentification ?

Firebase sert de plateforme complète, fournissant aux développeurs des services backend et des outils pour créer des applications web et mobiles.

L'un de ses principaux services est un service d'authentification qui simplifie le processus d'intégration des fonctionnalités d'authentification dans les applications.

Avec [Firebase](https://firebase.google.com/), la mise en œuvre de l'authentification devient plus simple, grâce à sa fourniture de composants d'interface utilisateur pré-construits, d'API conviviales pour les développeurs et de support pour diverses méthodes d'authentification.

## Comment configurer Firebase pour l'authentification par les réseaux sociaux

### Étape 1 : Créer un projet Firebase

1. Allez sur [la console Firebase](https://console.firebase.google.com/) et connectez-vous avec votre compte Google.
2. Cliquez sur le bouton "Ajouter un projet".
3. Entrez un nom pour votre projet et sélectionnez un emplacement pour le stockage de vos données.
4. Cliquez sur le bouton "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-22-082447.png)
_Page d'accueil de la console Firebase_

### Étape 2 : Enregistrer une application Web

Cette fonctionnalité vous permet d'enregistrer vos applications web pour accéder aux fonctionnalités de Firebase via des applications web.

1. Dans la console Firebase, cliquez sur l'icône "Web" (</>).
2. Cliquez sur le bouton "Ajouter une application".
3. Entrez un nom pour votre application et sélectionnez le type d'application "Web".
4. Cliquez sur le bouton "Enregistrer".

Après avoir créé un projet Firebase et enregistré une application web, vous pouvez commencer à utiliser Firebase pour l'authentification par les réseaux sociaux.

### Étape 3 : Découvrir les méthodes de connexion par les réseaux sociaux

Pour ce faire, une fois votre projet créé, vous devrez naviguer vers la section "Authentification" dans le menu de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2-Auth-side-bar-shown.png)
_Affichage de la barre latérale d'authentification_

Sous l'onglet "Méthode de connexion", vous trouverez une liste de fournisseurs d'authentification parmi lesquels vous pouvez en choisir un :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-22-082758.png)
_Affichage des différentes méthodes d'authentification_

### Étape 4 : Configurer les fournisseurs de réseaux sociaux

#### Comment configurer l'authentification Google :

Pour configurer l'authentification Google, ajoutez simplement un email de support, et vous êtes prêt.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/google-enable.png)
_Ajout d'un email de support pour l'authentification Google_

#### Comment configurer l'authentification GitHub :

Pour configurer l'authentification GitHub, vous aurez besoin d'un ID client et d'un secret client. Pour les obtenir, connectez-vous à votre [compte GitHub](https://github.com/) et allez dans Paramètres > Paramètres du développeur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/github--settings.png)
_Panneau des paramètres GitHub_

Ensuite, naviguez vers OAuth et créez une nouvelle application OAuth.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Setting-up-Github-OAuth.png)
_Création d'une application OAuth GitHub_

Pour obtenir l'URL de rappel d'autorisation, retournez à votre console Firebase et copiez l'URL dans la configuration GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/github-callback-url.png)
_URL de rappel GitHub_

Remarque : Pour compléter ce processus, vous devez avoir votre application déjà hébergée ou au moins une URL où votre application sera hébergée.

Ensuite, vous serez redirigé vers une page où votre application a été enregistrée et vous avez votre ID client et votre secret.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/3-Github-Client-ID-and-Secret-generated.png)
_ID client et secret GitHub générés_

Copiez ces détails et utilisez-les pour enregistrer GitHub en tant que service d'authentification sur Firebase.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/4-Filling-in-github-details-in-fb.png)
_Remplissage des détails GitHub sur Firebase_

#### Comment configurer l'authentification Twitter :

Similaire à GitHub, commencez par vous connecter à votre compte développeur Twitter. Si vous n'en avez pas, inscrivez-vous avec le [Portail des développeurs Twitter](https://developer.twitter.com/en/portal/petition/essential/basic-info). Cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Twitter-Developers-signup.png)
_Inscription des développeurs Twitter_

Après avoir rempli les détails, vous serez redirigé vers la page d'accueil.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/5-twitter-dev-homepage.png)
_Page d'accueil des développeurs Twitter_

Cliquez sur votre application par défaut et configurez l'authentification utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Twitter-user-auth-setup.png)
_Configuration de l'application OAuth Twitter_

N'oubliez pas d'obtenir l'URL de rappel de Firebase et de définir l'URL du site web sur l'URL où votre application est hébergée.

Après l'avoir configuré, naviguez vers les clés et jetons de votre projet et générez de nouveaux.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-25-164558.png)
_Génération de nouvelles clés et secrets d'application_

Collez ces détails dans Firebase pour configurer l'authentification Twitter.

Et avec cela, vos trois plateformes de réseaux sociaux sont configurées pour l'authentification.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/All-auths-setup.png)
_Toutes les authentifications configurées_

## Comment configurer votre application React

Maintenant, nous devons configurer votre application React. Vous allez commencer par créer une nouvelle application React en utilisant [Vite](https://vitejs.dev/guide/).

Créez un dossier sur votre ordinateur et ouvrez ce dossier avec votre IDE préféré. Ouvrez le terminal de cet IDE et exécutez cette commande :

```bash
npm create vite@latest
```

Lorsque les détails se chargent, sélectionnez React et attendez que l'installation soit terminée.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Vite-React.png)
_Création d'une application React avec Vite_

Vous serez laissé avec quelques fichiers et du code de base que vous pouvez supprimer.

Ensuite, exécutez `npm run dev` dans le terminal pour démarrer un serveur de développement sur le port `http://localhost:5173/`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Vit-setup.png)
_Application React en cours d'exécution dans le navigateur_

Pour utiliser Firebase dans votre application, vous devez d'abord définir un fichier de configuration Firebase. Ce fichier contient toutes les données nécessaires utilisées pour identifier votre application Firebase.

Créez donc un dossier dans votre répertoire `src` appelé `firebase`. Ensuite, placez un fichier `config.js` dans ce dossier et collez les détails du fichier de configuration de votre console Firebase que vous avez sauvegardés précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/6-firebase-config-in-vscode.png)
_Détails de la configuration Firebase_

Enfin, installez Firebase via votre terminal pour utiliser ses services dans votre application.

```bash
npm i firebase
```

## Comment intégrer l'authentification par les réseaux sociaux dans votre application

Considérant la taille de cette section, elle sera divisée en plusieurs sous-sections.

1. Configuration de la logique UI pour l'authentification
2. Configuration de la logique d'authentification
3. Mise en œuvre de l'état d'authentification global
4. Création d'un hook personnalisé pour l'authentification par les réseaux sociaux
5. Création de routes et mise en œuvre du routage
6. Authentification par les réseaux sociaux
7. Garde de route via l'état de l'utilisateur
8. Création d'un hook useLogout
9. Test de la fonctionnalité de déconnexion

### Comment configurer la logique UI pour l'authentification

Créez un dossier (pages) dans le répertoire `src` qui contient les pages que vous souhaitez dans votre application.

Pour cette implémentation, il y aura 2 fichiers dans le dossier pages, `Auth.jsx` et `Home.jsx`. Ces fichiers serviront de pages que l'utilisateur peut voir soit lorsqu'il est authentifié, soit non.

### Comment configurer la logique d'authentification

Commencez par importer et initialiser l'authentification Firebase, ainsi que les plateformes de réseaux sociaux activées sur Firebase dans votre configuration.

```js
import {
  getAuth,
  GoogleAuthProvider,
  GithubAuthProvider,
  TwitterAuthProvider,
} from "firebase/auth";

// Initialiser Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const googleProvider = new GoogleAuthProvider();
const githubProvider = new GithubAuthProvider();
const twitterProvider = new TwitterAuthProvider();
```

Ensuite, exportez ces fonctions initialisées pour les utiliser dans d'autres parties de votre application.

```js
export { auth, googleProvider, githubProvider, twitterProvider };
```

### Comment implémenter l'état d'authentification global

Pour garantir un état d'authentification cohérent dans toute votre application, envisagez d'utiliser l'approche du contexte React.

#### Étape 1 : Créer un AuthContext

Commencez par générer un dossier de contexte dans votre répertoire src, puis créez un fichier `AuthContext.jsx` dans celui-ci. Dans le fichier `AuthContext`, importez les hooks essentiels de React et Firebase.

```js
import { createContext, useReducer, useEffect, useContext } from "react";
import { auth } from "../firebase/config";

export const AuthContext = createContext();
```

#### Étape 2 : Définir une fonction de réducteur

Construisez une fonction de réducteur pour gérer les changements d'état pour les actions liées à l'authentification en utilisant le code suivant :

```js
export const authReducer = (state, action) => {
  switch (action.type) {
    // Lorsque le type d'action est "LOGIN", met à jour l'état avec les nouvelles informations de l'utilisateur
    case "LOGIN":
      return { ...state, user: action.payload };

    // Lorsque le type d'action est "LOGOUT", met à jour l'état pour supprimer les informations de l'utilisateur
    case "LOGOUT":
      return { ...state, user: null };

    // Lorsque le type d'action est "AUTH_IS_READY", met à jour l'état avec les informations de l'utilisateur et
    // définit un état pour indiquer que le processus d'authentification est terminé
    case "AUTH_IS_READY":
      return { user: action.payload, authIsReady: true };

    // Pour tout autre type d'action, retourne l'état actuel sans aucun changement
    default:
      return state;
  }
};

```

#### Étape 3 : Créer le composant AuthContextProvider

Créez un composant fournisseur qui enveloppe votre composant App entier, en utilisant le réducteur pour la gestion de l'état d'authentification.

```js
import { useEffect, useReducer } from "react";
import { onAuthStateChanged } from "firebase/auth"; 


// Composant fournisseur de contexte d'authentification
export const AuthContextProvider = ({ children }) => {
  // Initialiser l'état d'authentification en utilisant un réducteur
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    authIsReady: false,
  });

  // Effet pour déterminer l'état initial d'authentification et mettre à jour le contexte
  useEffect(() => {
    // Souscrire aux changements d'état d'authentification
    const unsub = onAuthStateChanged(auth, (user) => {
      // Dispatcher une action pour mettre à jour l'état avec les informations de l'utilisateur
      dispatch({ type: "AUTH_IS_READY", payload: user });

      // Se désabonner pour éviter d'autres mises à jour inutiles
      unsub(); // Se désabonner une fois que l'état initial d'authentification est déterminé
    });
  }, []);

  // Fournir l'état d'authentification et la fonction de dispatch aux composants enfants
  return (
    <AuthContext.Provider value={{ ...state, dispatch }}>
      {children}
    </AuthContext.Provider>
  );
};


```

#### Étape 4 : Implémenter le hook personnalisé useAuthContext

Vous pouvez simplifier l'accès au contexte d'authentification avec un hook personnalisé, comme ceci :

```js
import { useContext } from "react";

// Hook personnalisé pour accéder au contexte d'authentification
export function useAuthContext() {
  // Obtenir le contexte d'authentification du fournisseur AuthContextProvider le plus proche
  const context = useContext(AuthContext);

  // Vérifier si le contexte a été obtenu avec succès
  if (!context) {
    throw Error("useAuthContext doit être utilisé à l'intérieur d'un AuthContextProvider");
  }

  // Retourner l'objet de contexte d'authentification pour une utilisation dans les composants
  return context;
}

```

#### Comment intégrer le AuthContextProvider

Enfin, intégrez le `AuthContextProvider` dans votre configuration principale d'application

```js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { AuthContextProvider } from "./context/AuthContext.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AuthContextProvider>
      <App />
    </AuthContextProvider>
  </React.StrictMode>
);```

Avec cela, toutes les parties de votre application peuvent accéder aux valeurs de contexte du `AuthContext`.

### Comment créer un hook personnalisé pour l'authentification par les réseaux sociaux

Les processus d'authentification Firebase sont similaires en termes de structure et de code. Il est donc judicieux de suivre le principe DRY et de créer un hook utilitaire qui effectue l'authentification pour toutes les plateformes de réseaux sociaux. Cela vous permet de réutiliser le même code pour chaque plateforme, rendant votre code plus efficace et plus facile à maintenir.

Voici le processus étape par étape à suivre pour créer un hook personnalisé pour l'authentification par les réseaux sociaux.

#### Étape 1 : Créer le hook personnalisé

Dans votre répertoire source, créez un dossier hooks et, à l'intérieur, créez un fichier nommé `useSocialSignup.jsx`.

#### Étape 2 : Importer les dépendances

Importez les fonctions nécessaires de React et Firebase dans votre fichier `useSocialSignup`.

```js
import { useEffect, useState } from "react";
import { signInWithPopup } from "firebase/auth";
import { auth } from "../firebase/config";
import { useAuthContext } from "../context/AuthContext";
```

#### Étape 3 : Définir la fonction du hook

Développez la fonction `useSocialSignup`, qui prend un fournisseur comme paramètre et retourne un objet contenant un état d'erreur, un état en attente et la fonction de connexion pour le fournisseur social.

```js
export const useSocialSignup = (provider) => {
  // Variables d'état pour gérer le processus d'inscription
  const [error, setError] = useState(null);
  const [isPending, setIsPending] = useState(false);
  const [isCancelled, setIsCancelled] = useState(false);

  // Accéder à la fonction de dispatch du contexte d'authentification
  const { dispatch } = useAuthContext();

  // Fonction pour initier le processus d'inscription sociale
  const signInWithSocial = async () => {
    setError(null);
    setIsPending(true);

    try {
      const res = await signInWithPopup(auth, provider);

      dispatch({ type: "LOGIN", payload: res.user });

      if (!isCancelled) {
        setIsPending(false);
        setError(null);
      }
    } catch (err) {
      setError(err.message);
      setIsPending(false);
    }
  };

  // Hook d'effet pour définir isCancelled à true lorsque le composant est démonté
  useEffect(() => {
    return () => setIsCancelled(true);
  }, []);

  // Retourner les valeurs et fonctions pour l'utilisation du composant
  return { error, isPending, signInWithSocial };
};

```

Ce hook encapsule le processus de connexion avec les fournisseurs sociaux. Il gère les états d'erreur, en attente et d'annulation, interagit avec l'authentification Firebase et utilise le contexte d'authentification pour dispatcher des actions.

### Comment créer des routes et implémenter le routage

Pour garantir une navigation fluide et une expérience utilisateur optimale, la configuration des routes devient cruciale après la mise en œuvre de la logique d'authentification. Ces étapes bien organisées vous guident tout au long du processus.

#### Étape 1 : Installer react-router-dom 

Installez [le package react-router-dom](https://www.npmjs.com/package/react-router-dom), un choix populaire pour gérer le routage dans les applications React.

```bash
npm i react-router-dom
```

#### Étape 2 : Importer les dépendances

Dans votre fichier `App.jsx`, importez les composants et fonctions nécessaires pour le routage.

```js
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import Auth from "./pages/Auth";
```

#### Étape 3 : Définir les routes

Enveloppez le contenu de votre application dans un composant BrowserRouter et utilisez le composant Routes pour définir vos routes. Utilisez le composant Route pour mapper chaque chemin de route à son composant correspondant.

```js
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </BrowserRouter>
  );
}
```

Pour l'instant, vous pouvez naviguer librement entre les routes, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Onauth-routing.gif)
_Navigation entre les routes sans authentification_

### Authentification par les réseaux sociaux

Pour vous assurer que vos efforts n'ont pas été vains, rendez-vous sur `Auth.jsx` pour implémenter l'authentification.

#### Étape 1 : Importer les dépendances

Dans votre fichier `Auth.jsx`, commencez par importer les fournisseurs nécessaires, le contexte et le hook d'inscription personnalisé.

```js
import {
  googleProvider,
  twitterProvider,
  githubProvider,
} from "../firebase/config";
import { useSocialSignup } from "../hooks/useSocialSignup";
import {useEffect} from 'react'

import {useAuthContext} from "../context/AuthContext"
```

#### Étape 2 : Créer des instances du hook

Créez des instances du hook personnalisé `useSocialSignup` pour chaque fournisseur d'authentification.

```js
const google = useSocialSignup(googleProvider);
const twitter = useSocialSignup(twitterProvider);
const github = useSocialSignup(githubProvider);
```

#### Étape 3 : Ajouter des boutons pour l'inscription sociale

Créez des boutons pour chaque option d'inscription sociale (Google, Twitter, GitHub) et attachez des gestionnaires d'événements onClick pour appeler la fonction `signInWithSocial` du hook respectif.

```js
return (
  <div className="utility__page">
    <h1>Bienvenue sur ma page d'authentification</h1>

    <button onClick={google.signInWithSocial}>
      <img src={GoogleIcon} alt="" />
      <span>Google</span>
    </button>

    <button onClick={twitter.signInWithSocial}>
      <img src={TwitterIcon} alt="" />
      <span>Twitter</span>
    </button>

    <button onClick={github.signInWithSocial}>
      <img src={GithubIcon} alt="" />
      <span>GitHub</span>
    </button>
  </div>
);
```

#### Étape 4 : Appliquer le style

Vous pouvez utiliser le CSS fourni ci-dessous pour styliser vos composants pour une apparence propre et organisée.

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 62.5%;
  color: #121212;
}

.utility__page {
  display: flex;
  width: 100%;
  height: 100vh;
  justify-content: center;
  align-items: center;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  row-gap: 2rem;
  flex-direction: column;
  background: #e2dbd9;
}

h1 {
  font-size: 5rem;
}

button {
  padding: 1rem 4rem;
  font-size: 2rem;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

button img {
  width: 20px;
  height: 20px;
}

.user {
  font-size: 3rem;
  display: flex;
  align-items: center;
  column-gap: 1rem;
}

.logout {
  background: rgb(208, 84, 84);
  color: #fff;
}

.profile_img {
  width: 5rem;
  height: 5rem;
  border-radius: 50%;
}
```

Pour l'instant, votre page d'authentification ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Auth-page.png)
_Page d'authentification après l'application du style_

#### Étape 5 : Tester l'authentification

Pour tester l'authentification, importez l'utilisateur de votre `AuthContext` et journalisez-le dans la console en utilisant un `useEffect`.

```js
  const { user } = useAuthContext();
  useEffect(() => console.log(user), [user]);
```

Tester l'authentification donne maintenant ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/first-login-giffy.gif)
_Authentification confirmée dans la console via l'objet utilisateur_

Comme vous pouvez le voir, vous avez réussi à connecter un utilisateur en utilisant l'authentification par les réseaux sociaux. Félicitations !

Pour confirmer, rendez-vous sur votre page d'authentification Firebase et vérifiez les utilisateurs valides.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Valid-users-check.png)
_Confirmation de l'utilisateur inscrit sur Firebase_

N'hésitez pas à essayer d'autres méthodes de connexion car elles fonctionnent toutes de la même manière.

### Garde de route via l'état de l'utilisateur

Pour empêcher l'accès non autorisé, configurez des gardes de route qui vérifient l'état d'authentification de l'utilisateur dans votre fichier `App.jsx`.

```js
const { user, authIsReady } = useAuthContext();

if (!authIsReady) {
  return null; // Retourner null en attendant que authIsReady soit prêt
}

return (
  <BrowserRouter>
    <Routes>
      {user ? (
        <>
          {/* Routes authentifiées */}
          <Route path="/" element={<Home />} />
          {/* Gardes de route */}
          <Route path="*" element={<Navigate to="/" />} />
        </>
      ) : (
        <>
          {/* Routes d'authentification */}
          <Route path="/auth" element={<Auth />} />
          {/* Gardes de route */}
          <Route path="*" element={<Navigate to="/auth" />} />
        </>
      )}
    </Routes>
  </BrowserRouter>
);


```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/plain-home-page-after-auth.png)
_Redirigé vers la page d'accueil après l'ajout des gardes de route_

Comme vous pouvez le voir, vous avez été redirigé vers la page d'accueil, et même si vous essayez d'aller sur la page d'authentification, vous serez redirigé ici.

#### Comment personnaliser la page d'accueil

Pour la page d'accueil, récupérez les détails de l'utilisateur et affichez-les si un utilisateur est authentifié.

```js
import { useAuthContext } from "../context/AuthContext";

export default function Home() {
  const { user } = useAuthContext();
  return (
    <div className="utility__page ">
      <h1> Page d'accueil</h1>
      {user && (
        <>
          <div className="user">
            <p> Vous êtes connecté en tant que : </p>

            <span>{user.displayName} </span>
            <img className="profile_img" src={user.photoURL} alt=""/>
          </div>
         </>
      )}
    </div>
  );
}

```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Auth-showing-details.png)
_Page d'accueil montrant les détails personnalisés de l'utilisateur_

Et voilà ! Vous avez pu récupérer quelques détails sur cet utilisateur en fonction des informations sur le réseau social qu'il a utilisé pour se connecter.

### Comment créer un hook useLogout

La dernière étape pour compléter votre processus d'authentification est de fournir aux utilisateurs la possibilité de se déconnecter de votre application. Voici comment créer un hook useLogout :

#### Étape 1 : Créer le hook

Créez un nouveau fichier appelé useLogout.jsx dans votre dossier hooks. Importez les hooks et fonctions nécessaires.

```js
import { useEffect, useState } from "react";
import { auth } from "../firebase/config";
import { signOut } from "firebase/auth";
import { useAuthContext } from "../context/AuthContext";
```

#### Étape 2 : Créer les états du hook

Créez des états pour gérer le processus de déconnexion, y compris les états d'erreur, en attente et d'annulation.

```js
// État d'erreur pour les erreurs potentielles lors de la déconnexion 
const [error, setError] = useState(null); 
// État pour indiquer si la déconnexion est en cours 
const [isPending, setIsPending] = useState(false); 
// État pour suivre si l'opération est annulée
const [isCancelled, setIsCancelled] = useState(false); 
```

#### Étape 3 : Extraire la fonction de dispatch du contexte d'authentification

Cette fonction sera utilisée pour indiquer qu'une action de déconnexion a été appelée :

```js
const { dispatch } = useAuthContext();
```

#### Étape 4 : Créer la logique du hook

Utilisez un bloc try-catch pour créer la logique de déconnexion d'un utilisateur :

```js
try { 
// Initiation de la déconnexion en utilisant la fonction signOut de Firebase 
    await signOut(auth); 
    dispatch({ type: "LOGOUT" }); // Dispatch d'une action LOGOUT 
// Si l'opération n'a pas été annulée, réinitialiser l'état en attente et l'erreur 
   if (!isCancelled) { 
       setIsPending(false); // Réinitialisation de isPending après la fin de l'appel asynchrone 
       setError(null); // Effacement de toute erreur qui aurait pu se produire 
     } 
   } catch (err) { 
      // Gestion de l'erreur de déconnexion 
     if (!isCancelled) { 
        console.log(err.message); // Journalisation du message d'erreur
        setError(err.message); // Définition de l'état d'erreur en cas d'erreur 
        setIsPending(false); // Réinitialisation de l'état en attente si une erreur se produit 
   } 
}
```

#### Étape 5 : Comment gérer le démontage

Dans le cas où le composant est démonté (la page se ferme ou il y a un changement de route), vous voudrez gérer cette occurrence pour éviter les erreurs.

```js
// Hook d'effet pour définir isCancelled à true lorsque le composant est démonté
   useEffect(() => { 
       return () => setIsCancelled(true); // La fonction de nettoyage s'exécute lorsque le composant est démonté }, []);
```

#### Étape 5 : Exporter les valeurs

Retournez les valeurs et fonctions pertinentes pour que d'autres composants les utilisent.

```js
 return { logout, error, isPending };
```

Pour faciliter l'accessibilité, voici le hook useLogout complet.

```js
// Importation des hooks et fonctions nécessaires
import { useEffect, useState } from "react";
import { auth } from "../firebase/config"; // Importation de l'instance auth de Firebase
import { signOut } from "firebase/auth"; // Importation de la fonction signOut de Firebase
import { useAuthContext } from "../context/AuthContext"; // Importation du hook personnalisé pour accéder au contexte d'authentification

// Hook personnalisé pour gérer la déconnexion de l'utilisateur
export const useLogout = () => {
  // Variables d'état pour gérer le processus de déconnexion
  const [error, setError] = useState(null); // État d'erreur pour les erreurs potentielles lors de la déconnexion
  const [isPending, setIsPending] = useState(false); // État pour indiquer si la déconnexion est en cours
  const [isCancelled, setIsCancelled] = useState(false); // État pour suivre si l'opération est annulée
  const { dispatch } = useAuthContext(); // Accès à la fonction de dispatch du contexte d'authentification

  // Fonction pour initier le processus de déconnexion
  const logout = async () => {
    setError(null); // Effacement des erreurs précédentes
    setIsPending(true); // Indication que le processus de déconnexion est en cours

    try {
      // Initiation de la déconnexion en utilisant la fonction signOut de Firebase
      await signOut(auth);
      dispatch({ type: "LOGOUT" }); // Dispatch d'une action LOGOUT

      // Si l'opération n'a pas été annulée, réinitialiser l'état en attente et l'erreur
      if (!isCancelled) {
        setIsPending(false); // Réinitialisation de isPending après la fin de l'appel asynchrone
        setError(null); // Effacement de toute erreur qui aurait pu se produire
      }
    } catch (err) {
      // Gestion de l'erreur de déconnexion
      if (!isCancelled) {
        console.log(err.message); // Journalisation du message d'erreur
        setError(err.message); // Définition de l'état d'erreur en cas d'erreur
        setIsPending(false); // Réinitialisation de l'état en attente si une erreur se produit
      }
    }
  };

  // Hook d'effet pour définir isCancelled à true lorsque le composant est démonté
  useEffect(() => {
    return () => setIsCancelled(true); // La fonction de nettoyage s'exécute lorsque le composant est démonté
  }, []);

  // Retour des valeurs et fonctions pertinentes pour l'utilisation du composant
  return { logout, error, isPending };
};
```

### Comment tester la fonctionnalité de déconnexion

Dans votre composant Home.jsx, importez le hook useLogout et extrayez la fonction logout. Attachez la fonction logout à un événement onClick d'un bouton pour permettre aux utilisateurs de se déconnecter.

```js
import { useLogout } from "../hooks/useLogout";

export default function Home() {
  const { user } = useAuthContext();
  const { logout } = useLogout(); // fonction logout extraite

  return (
    <div className="utility__page ">
      <h1> Page d'accueil</h1>
      {user && (
        <>
          <div className="user">
            <p> Vous êtes connecté en tant que : </p>
            <span>{user.displayName} </span>
            <img className="profile_img" src={user.photoURL} alt="" />
          </div>
           // fonction logout utilisée
          <button className="logout" onClick={logout}>
             Se déconnecter
          </button>
        </>
      )}
    </div>
  );
}
```

Pour l'instant, votre page d'accueil ressemble à ceci ;

![Image](https://www.freecodecamp.org/news/content/images/2023/08/before-logout.png)
_Page d'accueil avant de déconnecter l'utilisateur_

Cliquez sur le bouton et déconnectez l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/login-out-and-in.gif)
_Test de la fonctionnalité de connexion et de déconnexion_

Avec cela, votre processus d'authentification est complètement configuré, félicitations !

## Trouver le bon équilibre : Offrir à la fois l'authentification par les réseaux sociaux et par email/mot de passe

L'authentification des utilisateurs est une partie clé de l'expérience utilisateur sur toute application web. L'authentification par les réseaux sociaux peut offrir une expérience simplifiée et une sécurité renforcée, mais il est important de trouver un équilibre en offrant également l'option d'authentification par email/mot de passe. Cela garantit l'inclusivité, répond à diverses préférences des utilisateurs et aborde les préoccupations en matière de confidentialité. 

En offrant les deux options, vous créez un processus d'authentification polyvalent et centré sur l'utilisateur qui contribue à une expérience utilisateur positive.

Un exemple de page d'authentification idéale peut être vu ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Final-signup-page.png)
_Page d'authentification standard_

## Directives pour la création de pages d'authentification

Il est important d'appliquer certaines bonnes pratiques de base lors de la création de pages d'authentification, telles que :

1. Montrer toutes les façons possibles dont un utilisateur peut s'authentifier de manière claire et concise.
2. Utiliser des icônes authentiques de l'entreprise pour établir la confiance. Vous pouvez trouver des SVG d'entreprise gratuits sur des sites comme [Font Awesome](https://fontawesome.com/), [Google icons](https://fonts.google.com/icons), et ainsi de suite.
3. Utiliser des icônes intuitives pour étiqueter les entrées telles que l'enveloppe pour le courrier et le cadenas pour le mot de passe.
4. Aborder les préoccupations en matière de confidentialité en communiquant clairement comment les données de l'utilisateur seront utilisées et protégées pendant le processus d'authentification.

Pour faciliter l'accessibilité, voici un lien vers le [dépôt](https://github.com/Daiveedjay/OAuth-Article).

## Conclusion

En conclusion, l'utilisation de la connexion par les réseaux sociaux avec Firebase est une stratégie intelligente. Elle combine convivialité, sécurité et confidentialité. 

En offrant diverses façons de se connecter, les sites web peuvent accommoder différentes préférences des utilisateurs, être plus inclusifs et s'adapter aux nouvelles tendances. 

Équilibrer les options d'authentification de cette manière rend les utilisateurs heureux et construit la confiance. Cela est important pour créer des sites web modernes et assurer des connexions fluides et centrées sur l'utilisateur.

### Informations de contact

Vous souhaitez me contacter ? N'hésitez pas à me contacter via les moyens suivants :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com