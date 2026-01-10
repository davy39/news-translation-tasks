---
title: Comment configurer l'authentification des utilisateurs GitHub en utilisant
  Firebase et React (avec Hooks)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-06T18:18:52.000Z'
originalURL: https://freecodecamp.org/news/github-user-authentication-using-firebase-and-reactjs-with-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Modern-Music-Electronic-Channel-Youtube-Thumbnail-3.png
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: GitHub
  slug: github
- name: React
  slug: react
seo_title: Comment configurer l'authentification des utilisateurs GitHub en utilisant
  Firebase et React (avec Hooks)
seo_desc: 'By Rishi Purwar

  In this tutorial, I will walk you through the process of creating a GitHub User
  Authentication System using Firebase and React (with hooks).

  If you have ever tried building an authentication system before, you might agree
  that it can ...'
---

Par Rishi Purwar

Dans ce tutoriel, je vais vous guider à travers le processus de création d'un système d'authentification des utilisateurs GitHub en utilisant Firebase et React (avec hooks).

Si vous avez déjà essayé de construire un système d'authentification auparavant, vous pourriez être d'accord pour dire que cela peut être douloureux. C'est là que Firebase intervient. Firebase fournit une authentification utilisateur prête à l'emploi, donc vous n'avez pas besoin d'écrire un code d'authentification complexe à partir de zéro – ce qui fait gagner beaucoup de temps.

Dans cet article, nous allons construire un simple composant de carte de profil qui affichera les données du profil GitHub d'un utilisateur authentifié, telles que la photo de profil, le nom d'affichage et le nom d'utilisateur.

Nous verrons également comment utiliser `ContextAPI` et le hook `useReducer` pour gérer l'état de l'utilisateur authentifié comme un pro.

🚀 Commençons !

Notez que vous aurez besoin d'une compréhension de base de React pour suivre ce tutoriel.

* [Comment créer un nouveau projet React](#heading-comment-creer-un-nouveau-projet-react)
* [🧹 Préparation avant le projet](#heading-preparation-avant-le-projet)
* [Comment configurer Firebase](#heading-comment-configurer-firebase)
* [Comment configurer Firebase Auth](#heading-comment-configurer-firebase-auth)
* [Comment créer une connexion GitHub dans un Hook](#heading-comment-creer-une-connexion-github-dans-un-hook)
* [Comment construire la fonctionnalité de connexion](#heading-comment-construire-la-fonctionnalite-de-connexion)
* [Comment construire la fonctionnalité de déconnexion](#heading-comment-construire-la-fonctionnalite-de-deconnexion)
* [Comment créer un contexte d'authentification](#heading-comment-creer-un-contexte-d-authentification)
* [Comment créer un fournisseur de contexte](#heading-comment-creer-un-fournisseur-de-contexte)
* [Comment créer une fonction de réducteur](#heading-comment-creer-une-fonction-de-reducteur)
* [Comment relier le contexte et le réducteur](#heading-comment-relier-le-contexte-et-le-reducteur)
* [Comment mettre à jour la valeur du contexte Auth](https://www.freecodecamp.org/news/p/95ce6097-8ce9-427b-afeb-a8731e785c4b/comment-mettre-a-jour-la-valeur-du-contexte-auth)
* [Comment persister l'état Auth](#heading-comment-persister-l-etat-auth)
* [Comment ajouter un composant de carte de profil](#heading-comment-ajouter-un-composant-de-carte-de-profil)
* [Comment sauvegarder un utilisateur dans Firebase](#heading-comment-sauvegarder-un-utilisateur-dans-firebase)
* [👋 Merci d'avoir lu ce tutoriel](#heading-merci-d-avoir-lu-ce-tutoriel)

## Comment créer un nouveau projet React

La première étape pour commencer est d'utiliser l'outil [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) pour générer un nouveau projet React. Si vous ne l'avez pas déjà installé, ouvrez d'abord votre terminal et exécutez cette commande pour l'installer globalement :

```
npm install -g create-react-app

```

Une fois installé, vous pouvez exécuter la commande suivante pour générer un nouveau projet React :

```
npx create-react-app react-firebase-github-auth

```

Une fois que vous avez exécuté cette commande, create-react-app prendra quelques minutes pour télécharger et installer toutes les dépendances requises. Cela peut sembler long, mais c'est normal ! Vous pouvez aller vous préparer une tasse de thé pendant ce temps.

Lorsque le processus est terminé, accédez au répertoire en utilisant la commande `cd react-firebase-github-auth`. Maintenant que nous sommes dans notre répertoire de projet, exécutons `code .` pour ouvrir le dossier du projet dans votre éditeur de code (j'utilise VS Code).

Ouvrez maintenant votre terminal en appuyant sur `ctrl + `` et exécutez `npm start` pour démarrer le serveur de développement. Cela ouvrira un nouvel onglet de navigateur avec notre application en cours d'exécution. Votre navigateur affichera quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/BqGj8FM.png)

## 🧹 Préparation avant le projet

Maintenant que vous avez créé un nouveau projet, nous allons faire un peu de ménage avant le projet.

La commande `create-react-app` que nous avons exécutée précédemment a créé beaucoup de fichiers dont nous n'aurons pas besoin dans notre projet. Nous allons supprimer certains des fichiers pour garder les choses bien organisées.

La première chose à faire est de remplacer tout le code du fichier `App.js` par ceci :

```
const App = () => {

  return (
    <div className="App">
      <button className="btn">
        Se connecter avec GitHub
      </button>
      <button className="btn">
        Se déconnecter
      </button>
    </div>
  );
};

export default App;



```

Maintenant que vous avez remplacé tout le code de votre fichier **App.js**, ajoutons un peu de CSS pour votre composant **App**. Ouvrez votre fichier `index.css` et remplacez le contenu par les styles suivants. Nous ne nous concentrerons pas beaucoup sur le style, donc voici les styles que vous pouvez utiliser :

```
@import url("https://fonts.googleapis.com/css2?family=Overpass:wght@400;700&display=swap");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.App {
  font-family: "Overpass", sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: hsl(216, 12%, 8%);
}

.btn {
  border: none;
  background-color: hsl(25, 97%, 53%);
  cursor: pointer;
  border-radius: 6px;
  color: white;
  font-weight: bold;
  padding: 12px 14px;
  font-size: 18px;
  margin-top: 8px;
}

.btn:hover {
  background-color: hsla(25, 97%, 53%, 0.668);
  transition: all 100ms linear;
}

.github-logo {
  width: 18px;
  margin-right: 6px;
  vertical-align: middle;
}

```

Allons-y et supprimons également certains fichiers inutiles. Ouvrez votre terminal et exécutez la commande suivante. Assurez-vous d'être dans le répertoire racine de votre dossier de projet :

```
cd src

rm -- App.test.js App.css logo.svg serviceWorker.js setupTests.js

cd ..

```

Remarque : Si vous avez arrêté votre serveur pour effectuer les tâches de terminal mentionnées ci-dessus, vous devrez le redémarrer en utilisant npm start.

## Comment configurer Firebase

Avant de plonger dans React et de coder de bonnes choses, nous devons configurer notre propre projet Firebase via la console Firebase.

Pour commencer, naviguez dans votre navigateur vers la [console Firebase](https://console.firebase.google.com/). Assurez-vous d'être connecté à votre compte Google.

Maintenant, cliquez sur Ajouter un projet, et vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/1CquSV9Qf.png)

Vous pouvez nommer votre projet comme vous le souhaitez. Mais pour cet exemple, nous l'appellerons "react-firebase-github-auth". Une fois cela fait, cliquez sur le bouton **Continuer**. Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/SfFPlAwOu.png)

Maintenant, vous verrez un bouton bascule pour activer Google Analytics pour ce projet. Mais nous n'en aurons pas besoin, alors cliquez simplement sur ce bouton bascule pour le désactiver. Vous pourrez l'activer plus tard si vous le souhaitez.

Une fois que vous avez créé votre projet Firebase, cliquez sur le bouton **Continuer** pour accéder à votre tableau de bord de projet, qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/dM0vleyHO--1-.png)

Maintenant que nous avons configuré un projet Firebase, allons-y et enregistrons notre application React pour commencer à utiliser Firebase.

Pour cela, cliquez sur l'icône de code (</>) que j'ai indiquée dans la capture d'écran ci-dessus. Maintenant, donnez-lui un nom. Pour ce tutoriel, je l'appellerai "react-firebase-github-auth" et cliquez sur **Enregistrer l'application** pour enregistrer notre application. Vous devriez voir le code de configuration suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/sY07iiBu6--1--2.png)

Copiez tout le code de configuration en cliquant sur le bouton copier dans le presse-papiers et cliquez sur le bouton `Continuer vers la console`. Ensuite, nous devons créer un fichier dans notre projet pour le stocker.

Rendons-nous dans notre application React, créons un nouveau dossier à l'intérieur de `src`, et appelons-le `firebase`. À l'intérieur de ce dossier Firebase, créez un nouveau fichier et nommez-le `config.js` et collez votre code de configuration dans ce fichier.

Si vous le souhaitez, vous pouvez supprimer les commentaires de votre fichier config.js. Vous n'avez pas non plus besoin de créer une variable d'application. Au lieu de cela, vous pouvez appeler `initializeApp()` sans la sauvegarder dans une variable. Maintenant, votre code devrait ressembler à ceci :

```
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyA2jZRiXP36UXbBS2xuV1UE4Yr3dYwhX24",
  authDomain: "react-firebase-github-au-eb675.firebaseapp.com",
  projectId: "react-firebase-github-au-eb675",
  storageBucket: "react-firebase-github-au-eb675.appspot.com",
  messagingSenderId: "605356741694",
  appId: "1:605356741694:web:5efdfac0ea6046e25c2d6f",
};

// Initialiser Firebase
initializeApp(firebaseConfig);

```

Maintenant, installons Firebase en utilisant npm pour notre projet. Pour cela, ouvrez votre terminal et exécutez cette commande :

```
npm install firebase

```

Ce workflow utilise npm et nécessite des bundlers de modules ou des outils de framework JavaScript. Cela est dû au fait que le SDK v9 est optimisé pour fonctionner avec des bundlers de modules afin d'éliminer le code inutilisé (tree-shaking) et de réduire la taille de l'application.

## Comment configurer Firebase Auth

Après avoir créé un projet Firebase dans votre console Firebase, vous devez activer le fournisseur GitHub. Pour cela, suivez ces étapes :

* Allez dans le tableau de bord de votre projet Firebase et cliquez sur l'onglet **Authentification** dans la barre latérale.
* Maintenant, cliquez sur le bouton **Commencer**, puis cliquez sur l'onglet **Méthode de connexion**, puis sélectionnez le fournisseur **Connexion avec GitHub**.
* Après cela, cliquez sur le bouton bascule pour activer l'authentification GitHub.

Maintenant, vous devez ajouter le `Client ID` et le `Client Secret` depuis la console de développement GitHub.

Pour obtenir votre `Client ID` et votre `Client Secret`, commencez par [enregistrer votre application](https://github.com/settings/applications/new) en tant qu'application de développeur sur GitHub, et vous verrez un formulaire d'application qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/P0SjzJSFc--1--3.png)

Remplissez ce formulaire et assurez-vous que votre **URI de redirection OAuth Firebase** (par exemple, my-app-12345.firebaseapp.com/__/auth/handler) est définie comme votre **URL de rappel d'autorisation**. Vous pouvez trouver votre **URI de redirection OAuth Firebase** ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/GltEGGRMI.png)

Maintenant, cliquez sur **Enregistrer l'application**. Vous verrez votre `Client ID`, mais vous devez générer votre `Client secrets` en cliquant sur le bouton **Générer un nouveau secret client**. Maintenant, copiez votre `Client ID` et votre `Client secrets` depuis la page de l'application GitHub et collez-les dans le formulaire des fournisseurs de connexion GitHub Firebase.

Cliquez sur **Enregistrer**.

Maintenant que nous avons activé l'authentification GitHub sur notre projet Firebase, il est temps de l'initialiser sur le frontend.

Tout d'abord, ouvrez votre fichier `config.js` et importez `getAuth` depuis `firebase/auth` juste en dessous de l'instruction d'importation `initializeApp`.

Ensuite, nous allons créer une variable appelée `auth` et la définir égale à `getAuth()`. Et enfin, exportez cette variable `auth` depuis ici.

Votre code devrait ressembler à ceci :

```
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAaHLAnc5DXxHHFtcjIO7dQVe9i9OKsFqg",
  authDomain: "fir-github-auth-b5110.firebaseapp.com",
  projectId: "fir-github-auth-b5110",
  storageBucket: "fir-github-auth-b5110.appspot.com",
  messagingSenderId: "857975576429",
  appId: "1:857975576429:web:0a1d4e6a5a3b08febcac64",
};

// Initialiser Firebase
initializeApp(firebaseConfig);

// Initialiser Firebase Auth
const auth = getAuth();

export { auth };

```

Maintenant que nous avons tout cela configuré, nous pouvons utiliser les services d'authentification Firebase comme **Connexion** et **Déconnexion** dans n'importe quel composant dont nous avons besoin !

## Comment créer une connexion GitHub dans un Hook

Jusqu'à présent, nous avons ajouté Firebase à notre projet. Maintenant, utilisons-le.

Tout d'abord, créons un hook personnalisé pour inscrire les utilisateurs en utilisant leurs comptes GitHub. Pour cela, commencez par créer un dossier à l'intérieur du dossier `src` appelé `hooks`. À l'intérieur de celui-ci, créez un nouveau fichier et nommez-le `useLogin.js`. Dans ce fichier, ajoutez le code suivant :

```
import { GithubAuthProvider, signInWithPopup } from "firebase/auth";
import { auth } from "../firebase/config";
import { useState } from "react";

export const useLogin = () => {
  const [error, setError] = useState(false);
  const [isPending, setIsPending] = useState(false);
  const provider = new GithubAuthProvider();

  const login = async () => {
    setError(null);
    setIsPending(true);

    try {
      const res = await signInWithPopup(auth, provider);
      if (!res) {
        throw new Error("Impossible de compléter l'inscription");
      }

      const user = res.user;
      console.log(user);
      setIsPending(false)
    } catch (error) {
      console.log(error);
      setError(error.message);
      setIsPending(false);
    }
  };

  return { login, error, isPending };
};

```

Je vais vous expliquer le code ci-dessus. Ne vous inquiétez pas, ce n'est pas effrayant ! Vous comprendrez tout en un clin d'œil.

Les deux premières lignes sont assez simples, elles importent simplement quelques éléments de Firebase et auth depuis notre fichier config.js dont nous aurons besoin plus tard. Dans la troisième ligne, nous importons le hook `useState` depuis le module React.

La cinquième ligne est là où les choses deviennent intéressantes ! Nous avons créé une fonction appelée `useLogin` et l'avons exportée immédiatement sur la même ligne. À l'intérieur de cette fonction, nous créons deux états en utilisant le hook useState : `error` et `isPending`.

Nous utiliserons l'état d'erreur pour afficher les erreurs, et l'état isPending pour afficher l'état en attente.

Par exemple, disons qu'un utilisateur clique sur le bouton d'inscription, et nous définissons isPending à `true`. Lorsque la demande d'inscription est terminée, nous pouvons le remettre à false en utilisant setisPending(false). Nous pouvons utiliser cet état `isPending` pour ajouter un chargeur afin de montrer un état en attente dans notre composant.

Et après cela, nous avons créé une instance de l'objet fournisseur GitHub :

```
const provider = new GithubAuthProvider();

```

Ensuite, nous créons une fonction de connexion, et à l'intérieur de celle-ci, nous avons ajouté ce morceau de code :

```
setError(null);
setIsPending(true);

```

Lorsque le code ci-dessus s'exécute, il définira automatiquement l'état de l'erreur à null et l'état de `isPending` à true. Cela signifie que lorsque vous vous connectez, vous ne verrez aucune erreur, mais vous aurez des états en attente sur votre page.

Et juste en dessous, nous avons ajouté un bloc `try-catch`. Dans le bloc try, nous essayons d'inscrire l'utilisateur en utilisant la fonction `signInWithPopup`. Mais nous avons deux façons de demander aux utilisateurs de se connecter avec leurs comptes GitHub : soit en **ouvrant une fenêtre pop-up**, soit en **redirigeant vers la page de connexion**.

Dans ce blog, nous utilisons `signInWithPopup` qui prend deux arguments. Le premier est `auth` et le second est `provider`.

Et dans le bloc `catch`, nous capturons l'erreur si elle se produit dans le bloc try. Si elle se produit, alors nous la définissons en utilisant `setError(error.message)`. Nous définirons également `isPending` égal à `false` car nous avons terminé ce que nous essayions de faire et avons maintenant une réponse – soit un utilisateur connecté, soit une erreur.

Enfin, nous exportons la fonction **login**, **error** et **isPending** afin de pouvoir les utiliser dans d'autres composants.

## Comment construire la fonctionnalité de connexion

Maintenant que nous avons créé un hook `useLogin`, utilisons-le pour connecter les utilisateurs en utilisant leurs comptes GitHub.

Commençons par importer le hook `useLogin` depuis `./hooks/useLogin` dans notre fichier **App.js** que nous avons exporté depuis `useLogin.js`. Ensuite, nous appellerons ce hook au début du composant App et déstructurerons deux choses : la fonction `login` et l'état `isPending` :

```
import { useLogin } from "./hooks/useLogin";
....
const App = () => {
  const { login, isPending } = useLogin();

  return (
    <div className="App">
....

```

Maintenant, ajoutons un gestionnaire d'événements `onClick` à notre bouton `Se connecter avec GitHub` afin d'appeler la fonction `login` lorsque l'utilisateur clique sur le bouton. Nous afficherons également un texte de bouton conditionnellement – si `isPending` est vrai, alors afficher `Chargement...` sinon afficher `Se connecter avec GitHub`.

Votre code de bouton devrait ressembler à ceci :

```
<div className="App">
    <button className="btn" onClick={login}>
        {isPending ? "Chargement..." : "Se connecter avec GitHub"}
    </button>
</div>

```

Maintenant, testons notre bouton de connexion. Cliquez sur le bouton `Se connecter avec GitHub`, et cela devrait ouvrir une nouvelle fenêtre, puis vous devez autoriser votre application React. Ensuite, vous verrez un objet utilisateur imprimé sur votre console qui ressemble à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/2A4p7e3T3-2.png)

Maintenant, ouvrez le tableau de bord de votre projet Firebase et cliquez sur l'onglet Authentification. Vous verrez un utilisateur connecté qui ressemble à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Gda8EuxXf.png)

## Comment construire la fonctionnalité de déconnexion

Maintenant que nous pouvons connecter les utilisateurs, que faisons-nous ensuite ? Eh bien, il est temps de travailler sur la fonctionnalité de déconnexion de l'utilisateur. C'est en fait relativement plus facile que de les connecter.

Alors, commençons par créer un hook personnalisé `useLogout` pour déconnecter l'utilisateur. Pour cela, créez un fichier et nommez-le `useLogout.js` à l'intérieur du dossier `hooks`. Dans ce fichier, ajoutez le code suivant :

```
import { signOut } from "firebase/auth";
import { auth } from "../firebase/config";

export const useLogout = () => {

  const logout = async () => {
    try {
      await signOut(auth);
      console.log("utilisateur déconnecté")
    } catch (error) {
      console.log(error.message);
    }
  };

  return { logout };
};


```

Je vais vous expliquer le code ci-dessus. Vous comprendrez tout en un clin d'œil.

Les deux premières lignes sont assez simples, nous importons simplement la fonction `signOut` de Firebase et `auth` de notre fichier config.js dont nous aurons besoin plus tard.

La quatrième ligne est là où les choses deviennent intéressantes ! Nous avons créé une fonction appelée `useLogout` et l'avons exportée immédiatement sur la même ligne.

Ensuite, nous créons une fonction asynchrone `logout` et l'exportons sur la même ligne. À l'intérieur de celle-ci, nous avons ajouté un bloc `try-catch`. Dans le bloc try, nous déconnectons les utilisateurs en utilisant la méthode `signOut` qui est fournie par `firebase/auth`. Et dans le bloc catch, nous capturons l'erreur si elle se produit dans le bloc try.

Maintenant, importons ce hook `useLogout` dans le composant App.js comme ceci :

```
import { useLogout } from "./hooks/useLogout";

```

Et juste en dessous de la ligne où nous appelons le hook `useLogin()`, appelez également le hook `useLogout` :

```
const { logout } = useLogout();

```

Maintenant, ajoutons un gestionnaire d'événements `onClick` au bouton `Se déconnecter` afin d'appeler la fonction `useLogout` lorsque l'utilisateur clique sur le bouton. Votre code de bouton devrait ressembler à ceci :

```
<button className="btn" onClick={logout}>
    Se déconnecter
</button>

```

Maintenant, il est temps de tester notre fonctionnalité de déconnexion. Cliquez sur le bouton `Se déconnecter` si vous êtes déjà connecté. Si vous n'êtes pas connecté, connectez-vous d'abord, puis cliquez sur le bouton Se déconnecter. Maintenant, vous devriez voir un **"utilisateur déconnecté"** imprimé dans votre console :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/n3gT5cWkg.png)

## Comment créer un contexte d'authentification

Maintenant que nous sommes capables d'inscrire et de déconnecter l'utilisateur, nous voulons stocker l'objet utilisateur dans un état global lorsque l'utilisateur est connecté. Cela nous permettra d'accéder aux données de l'utilisateur dans nos composants sans faire de forage de props.

Si vous ne connaissez pas le contexte, laissez-moi vous l'expliquer brièvement :

[Context API](https://reactjs.org/docs/context.html) est un moyen de partager des données entre les composants React sans utiliser de props. Cela signifie que vous pouvez passer des données directement aux composants qui en ont besoin au lieu de les passer par des composants intermédiaires. Il le fait en fournissant une sorte de stockage global pour les données.

Maintenant, nous allons créer un contexte pour notre application React. La première chose que nous ferons est de créer un dossier pour notre contexte à l'intérieur du dossier `src` et nous l'appellerons `contexts`. Ce dossier sera l'endroit où nous mettrons tous les contextes de notre application (si nous avons plus d'un contexte, alors nous les mettrons tous dans ce dossier. Mais pour cette petite application React, nous allons seulement créer un contexte pour l'authentification).

Maintenant, créons un fichier pour notre contexte sous le dossier contexts et nommons-le `AuthContext.js`. Notre nouveau fichier AuthContext.js est actuellement vide ! Ouvrez-le et donnez-lui ses deux premières lignes :

```
import { createContext } from "react";

export const AuthContext = createContext();

```

Cette fonction `createContext` que React nous fournit crée essentiellement un objet de contexte. Nous utiliserons cet objet pour consommer le contexte dans nos composants. Je vous montrerai comment consommer le contexte dans une section ultérieure.

## Comment créer un fournisseur de contexte

Le AuthContext que nous avons créé ci-dessus nous donne accès au composant `AuthContext.Provider` que nous utilisons pour fournir un contexte à tous les éléments enfants.

Pour définir la valeur du contexte, nous devons utiliser la prop `value` disponible sur le `<AuthContext.Provider value={/* une valeur */}>`.

Copiez le snippet suivant, puis collez-le dans `AuthContext.js` en dessous de votre fonction `createContext()`.

```
const AuthContextProvider = ({ children }) => {

  return (
    <AuthContext.Provider value={/* une valeur */}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContextProvider;

```

## Comment créer une fonction de réducteur

Tout d'abord, parlons de ce que sont les réducteurs. Une fonction de réducteur est une fonction JavaScript qui prend deux paramètres : **state** et **action**. Le paramètre state est l'état actuel de l'application, tandis que le paramètre action est un objet décrivant l'action effectuée par l'utilisateur.

Pour créer une fonction de réducteur, créons d'abord un dossier à l'intérieur du dossier `src` et nommons-le `reducers`. À l'intérieur de ce dossier reducers, créez un fichier et appelez-le `authReducer.js`.

Notre nouveau fichier `authReducer.js` est actuellement vide ! Copiez le snippet suivant, puis collez-le dans authReducer.js.

```
export const authReducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      return { ...state, user: action.payload };
    case "LOGOUT":
      return { ...state, user: null };
    case "AUTH_IS_READY":
      return { ...state, user: action.payload, authIsReady: true };
    default:
      return state;
  }
};


```

Laissez-moi vous expliquer le code ci-dessus :

Le code ci-dessus est essentiellement une fonction qui prend deux paramètres : **state** et **action**. À l'intérieur de cette fonction, nous avons ajouté un switch case pour déterminer le type d'action et exécuter le cas correspondant selon le type d'action.

Par exemple, si vous cliquez sur un bouton de connexion sur votre page web et qu'il envoie une action "LOGIN", cela serait géré par l'une de ces instructions de cas. S'il n'y a pas de correspondance pour l'un de ces cas, alors il retournera l'état inchangé. Cela signifie que si aucune action n'est envoyée, alors rien ne se passe !

Vous vous demandez peut-être ce que signifie cette action. Une action est un objet qui décrit comment mettre à jour l'état. Les actions sont effectuées par un utilisateur lors d'une interaction utilisateur, comme cliquer sur un bouton ou appuyer sur une touche fléchée.

Cet objet d'action a généralement deux clés :

1. **type** : Le type d'action effectuée. Il s'agit simplement d'une chaîne de caractères, et il est important d'utiliser une chaîne descriptive. Par exemple, vous pourriez utiliser **"LOGIN"** ou **"LOGOUT"**, selon ce que vous faites.
2. **payload** : Le payload pour l'action est toute donnée que vous devez transmettre avec le type d'action effectuée. Si vous inscrivez un utilisateur, cela pourrait être les données de l'utilisateur.

Si vous vous demandez où je vais avec cela, ne vous inquiétez pas, cela aura du sens bientôt !

## Comment relier le contexte et le réducteur

Relions notre **authReducer** avec notre **AuthContext**. Pour cela, importez d'abord la fonction de réducteur depuis `authReducer.js` dans le fichier `AuthContext.js`.

```
import { authReducer } from "../reducers/authReducer";

```

Maintenant, nous allons utiliser un hook `useReducer`. Le `useReducer(reducer, initialState)` prend deux arguments : un **réducteur** et un **état initial**.

Dans ce cas, nous passons simplement notre fonction `authReducer` et un objet d'état initial qui a deux propriétés : **user** et **authIsReady** :

```
{
    user: null,
    authIsReady: false,
}

```

Alors, importons le hook `useReducer` dans ce fichier depuis React. Mettez à jour votre toute première ligne pour qu'elle se lise comme ceci :

```
import { createContext, useReducer } from "react";

```

Ce hook useReducer nous retourne un tableau de deux éléments qui ont à la fois notre `state` actuel ainsi que la méthode `dispatch`. (Si vous êtes familier avec Redux, vous savez déjà comment fonctionne cette méthode dispatch.).

Maintenant, ajoutons le code ci-dessous juste au-dessus du mot-clé return du composant `AuthContextProvider` :

```
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    authIsReady: false,
  });

```

Maintenant que nous avons déstructuré les valeurs `state` et `dispatch` du tableau en utilisant la [déstructuration de tableau](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#examples), mettons à jour la prop `value` de `AuthContext.Provider` pour qu'elle inclue toutes ces valeurs :

```
<AuthContext.Provider value={{ ...state, dispatch }}>

```

Ajoutons également un `console.log(state)` juste au-dessus de l'instruction return, afin que nous puissions voir l'état de l'utilisateur lorsqu'il change.

Maintenant que nous avons créé un contexte, importons le composant `AuthContextProvider` dans le fichier `index.js` pour l'utiliser :

```
import AuthContextProvider from "./contexts/AuthContext";

```

Et maintenant, enveloppez votre composant `App` avec le composant `AuthContextProvider` pour fournir un contexte à toute votre application. Pour cela, enveloppez votre composant App comme ceci :

```
<AuthContextProvider>
    <App />
</AuthContextProvider>

```

Maintenant, retournons à notre composant App et voyons comment nous pouvons utiliser l'objet AuthContext afin d'obtenir les détails de l'utilisateur. Tout d'abord, importons l'objet `AuthContext` depuis `AuthContext.js` dans le fichier `App.js` :

```
import { AuthContext } from "./contexts/AuthContext";

```

Et nous devons également importer le hook `useContext` dans ce fichier, afin de pouvoir consommer l'objet AuthContext :

```
import { useContext } from "react";

```

Un hook `useContext` accepte un objet de contexte (la valeur retournée par `createContext()`) et retourne la valeur de contexte actuelle pour ce contexte.

La valeur de contexte actuelle est déterminée par la prop value de `<AuthContext.Provider value={{ ...state, dispatch }}>`.

Maintenant, appelons ce `useContext` avec notre objet `AuthContext`. Ajoutez ce morceau de code juste au-dessus de l'instruction return du composant App

```
const { user } = useContext(AuthContext);
console.log(user);

```

Maintenant, rafraîchissons la page. Vous devriez voir `null` imprimé depuis votre fichier `App.js`. Si vous essayez de vous connecter en utilisant votre compte GitHub, il imprimera toujours `null`.

Si vous vous demandez pourquoi vous ne voyez que `null` même si vous êtes connecté, c'est parce que, lors de la connexion ou de la déconnexion, nous ne mettons pas à jour notre valeur de contexte – elle montre toujours une valeur initiale que nous avons passée.

Pour corriger cela, nous devons mettre à jour notre valeur de contexte en utilisant la méthode `dispatch` chaque fois que nous nous connectons ou nous déconnectons.

## Comment mettre à jour la valeur du contexte Auth

Maintenant que nous avons configuré le contexte Auth et le réducteur Auth, utilisons-les pour mettre à jour l'état.

Tout d'abord, importons l'objet `AuthContext` depuis `AuthContext.js` dans le fichier `useLogin.js` :

```
import { AuthContext } from "../contexts/AuthContext";

```

Et maintenant, importons le hook `useContext` dans ce fichier, afin de pouvoir consommer l'objet AuthContext – mettez à jour votre ligne d'importation `useState` pour qu'elle se lise comme ceci :

```
import { useContext, useState } from "react";

```

Maintenant, appelons ce useContext avec notre objet AuthContext. Ajoutez ce morceau de code en dessous de `GithubAuthProvider()` à l'intérieur de la fonction `useLogin` :

```
const { dispatch } = useContext(AuthContext);

```

Maintenant, envoyons l'action `LOGIN` pour mettre à jour l'état. Pour cela, appelez simplement la fonction `dispatch` avec l'objet d'action juste en dessous de la variable `user` à l'intérieur du bloc try. Votre code de bloc try devrait ressembler à ceci :

```
try {
      const res = await signInWithPopup(auth, provider);
      if (!res) {
        throw new Error("Impossible de compléter l'inscription");
      }

      const user = res.user;
      dispatch({ type: "LOGIN", payload: user });

      console.log(user);
      setIsPending(false);
    }

```

Enregistrez votre fichier et essayez de vous connecter à nouveau, et vous devriez voir un objet utilisateur imprimé sur la console depuis le fichier App.js lorsque vous vous connectez.

Maintenant, faisons la même chose avec la fonctionnalité de déconnexion pour mettre à jour l'état à nouveau lorsque l'utilisateur se déconnecte.

Pour cela, ouvrez votre fichier `useLogout.js` et importez l'objet `AuthContext` depuis `AuthContext.js` :

```
import { AuthContext } from "../contexts/AuthContext";

```

Et maintenant, importez le hook `useContext` dans ce fichier :

```
import { useContext } from "react";

```

Maintenant, appelons ce useContext avec notre objet AuthContext. Ajoutez ce morceau de code au-dessus de la fonction `logout` à l'intérieur de la fonction `useLogout` :

```
const { dispatch } = useContext(AuthContext);

```

Maintenant, envoyons l'action `LOGOUT`. Pour cela, appelez simplement la fonction `dispatch` avec l'objet d'action juste en dessous de `await signOut(auth)` à l'intérieur du bloc try. Votre code de bloc try devrait ressembler à ceci :

```
try {
      await signOut(auth);
      dispatch({ type: "LOGOUT" });
      console.log("utilisateur déconnecté");
    }

```

Enregistrez votre fichier et essayez de vous déconnecter. Vous devriez voir `null` et `utilisateur déconnecté` imprimés sur la console lorsque vous vous déconnectez.

Nous avons maintenant implémenté avec succès la logique derrière l'authentification des utilisateurs en utilisant Firebase et ReactJS.

Mais il reste encore un problème : lorsque vous essayez de rafraîchir la page, vous verrez `null` imprimé sur la console. Cela signifie que vous êtes automatiquement déconnecté lorsque vous faites un rafraîchissement !

Nous ne voulons pas déconnecter nos utilisateurs lors du rafraîchissement. Nous pouvons corriger ce problème en persistant l'état d'authentification en utilisant la méthode [onAuthStateChanged](https://firebase.google.com/docs/auth/web/start#set_an_authentication_state_observer_and_get_user_data) fournie par `firebase/auth`.

## Comment persister l'état Auth

Maintenant, ouvrez votre fichier `AuthContext.js` et importez `onAuthStateChanged` comme ceci :

```
import { onAuthStateChanged } from "firebase/auth";

```

Maintenant, importons le hook `useEffect` dans ce fichier depuis React. Mettez à jour votre toute première ligne pour qu'elle se lise comme ceci :

```
import { createContext, useEffect, useReducer } from "react";

```

Maintenant, importez `auth` depuis le fichier `config.js` :

```
import { auth } from "../firebase/config";

```

Et ensuite, juste au-dessus de l'instruction return, ajoutez ce morceau de code :

```
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      dispatch({ type: "AUTH_IS_READY", payload: user });
    });
    return unsubscribe;
  }, []);

```

Laissez-moi vous expliquer rapidement le code ci-dessus, vous comprendrez tout en un instant.

Dans la première ligne, nous utilisons un hook appelé `useEffect()`, qui prend en arguments une fonction et un tableau de dépendances vide.

Ensuite, nous définissons une méthode `onAuthStateChanged` qui prend deux arguments : premièrement, elle prend l'`auth` que nous avons exporté depuis le fichier `config.js`. Deuxièmement, elle prend une fonction de rappel qui est invoquée **immédiatement** après l'enregistrement de l'observateur `onAuthStateChanged` avec l'état d'authentification actuel et chaque fois que l'état d'authentification change.

Et à l'intérieur de cette fonction de rappel, nous passons toutes les données que nous recevons de l'objet utilisateur et définissons notre méthode dispatch pour envoyer une action avec le type `AUTH_IS_READY` et le payload comme notre objet utilisateur pour mettre à jour la valeur du contexte.

Enfin, la fonction onAuthStateChanged() retourne la [fonction unsubscribe](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) pour désenregistrer l'observateur `onAuthStateChanged`. Nous sauvegardons cette fonction dans une variable et la nommons `unsubscribe`. À la fin, nous retournons cette fonction `unsubscribe` pour le nettoyage afin d'éviter les fuites de mémoire.

Maintenant, si vous faites un rafraîchissement après vous être connecté, vous verrez un objet utilisateur imprimé sur la console.

Donc, c'est tout pour la logique d'authentification. Dans la section suivante, nous ajouterons un composant ProfileCard pour afficher les données de l'utilisateur connecté.

## Comment ajouter un composant de carte de profil

Créons un composant de carte de profil où nous afficherons les données de connexion. Pour cela, créez d'abord un dossier `components` à l'intérieur du dossier `src`. À l'intérieur de ce dossier, créez un fichier et nommez-le `ProfileCard.js` et ajoutez ce morceau de code :

```
import React from "react";
import { useLogout } from "../hooks/useLogout";

const ProfileCard = ({ user }) => {
  const { logout } = useLogout();
  return (
    <>
      <div className="profile-card">
        <img className="profile-img" src={user.photoURL} alt="" />
        <p>
          Nom : <span>{user.displayName}</span>
        </p>
        <p>
          Nom d'utilisateur : <span>{user.reloadUserInfo.screenName}</span>
        </p>
        <p>
          Email : <span>{user.email}</span>
        </p>
        <p>
          ID utilisateur : <span>{user.uid}</span>
        </p>
      </div>
      <button className="btn" onClick={logout}>
        Se déconnecter
      </button>
    </>
  );
};

export default ProfileCard;

```

Comme vous pouvez le voir, ce composant prend une prop user de son composant parent (qui est `App`). Ensuite, nous avons déstructuré cette prop user en utilisant la déstructuration d'objet.

Maintenant, ajoutons un peu de CSS pour ce composant ProfileCard. Copiez et collez simplement le CSS suivant dans votre fichier index.css :

```
.profile-card {
  text-align: center;
  background-color: hsl(213, 19%, 18%);
  border-radius: 8px;
  padding: 16px;
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
  margin-bottom: 4px;
}

.profile-img {
  border-radius: 50%;
  width: 112px;
  border: 4px solid hsl(25, 97%, 53%);
  margin-bottom: 8px;
}

p {
  color: hsl(216, 12%, 54%);
  font-size: 24px;
  font-weight: 700;
}

span {
  color: white;
  font-size: 18px;
  font-weight: 400;
}

```

Maintenant, importons ce composant `ProfileCard` dans le fichier `App.js` :

```
import ProfileCard from "./components/ProfileCard";

```

Maintenant, remplacez simplement le contenu de l'instruction return par ce morceau de code :

```
return (
    <div className="App">
      {user ? (
        <ProfileCard user={user} />
      ) : (
        <button className="btn login-btn" onClick={login}>
          Se connecter avec GitHub
        </button>
      )}
    </div>
  );

```

Comme vous pouvez le voir, nous utilisons une propriété appelée `user` pour déterminer si un utilisateur est connecté ou non.

Si un utilisateur est connecté, alors le composant `ProfileCard` sera affiché. Si un utilisateur n'est pas connecté, alors l'élément bouton `Se connecter avec GitHub` sera affiché.

Maintenant, votre application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/31YHvHfM2.png)

Mais il y a un problème : si vous faites un rafraîchissement, il affiche d'abord un bouton `Se connecter avec GitHub` puis il affiche un composant de profil. Cela se produit parce que Firebase prend un certain temps pour vérifier si un utilisateur est connecté ou non.

Cela peut être une mauvaise expérience utilisateur, surtout si votre application a des routes privées que les utilisateurs ne peuvent accéder que lorsqu'ils sont connectés.

Disons que vous avez un site web où les utilisateurs peuvent accéder à une route privée uniquement lorsqu'ils sont connectés, et s'ils ne sont pas connectés, ils seront redirigés vers la page d'accueil lorsqu'ils essaieront d'accéder à la route privée.

Disons qu'un utilisateur est connecté et se trouve sur la route privée, et pour une raison quelconque, il fait un rafraîchissement. À votre avis, que se passera-t-il ?

Ils seront redirigés vers la page d'accueil parce que Firebase prendra un certain temps pour vérifier s'ils sont connectés ou non. Cela peut être frustrant pour les utilisateurs de votre site web !

Vous vous demandez peut-être comment nous pouvons résoudre ce problème ? 🤔

La solution à ce problème est simple, si vous vous souvenez, nous avons ajouté une propriété appelée `authIsReady` ainsi que la propriété `user` à notre état initial. Nous allons utiliser cette propriété pour résoudre ce problème.

Ouvrez votre fichier `App.js` et mettez à jour votre ligne `useContext(AuthContext)` pour qu'elle se lise comme ceci :

```
const { user, authIsReady } = useContext(AuthContext);

```

Et maintenant, ajoutons une vérification juste après le mot-clé return :

```
  return authIsReady ? (
    <div className="App">
      {user ? (
        <ProfileCard user={user} />
      ) : (
        <button className="btn login-btn" onClick={login}>
          Se connecter avec GitHub
        </button>
      )}
    </div>
  ) : (
    <h1>Préparation de votre authentification, veuillez patienter un moment</h1>
  );

```

Ici, nous vérifions simplement si `authIsReady` est `true`, puis nous affichons un composant `App`. Si ce n'est pas le cas, alors nous affichons un composant `Loader` (dans notre cas, nous affichons simplement un texte laid, mais vous pouvez ajouter un chargeur magnifique à la place).

Remarque : `authIsReady` ne signifie pas que nous sommes connectés. Cela signifie simplement que maintenant que nous avons la valeur de l'utilisateur, elle peut être nulle ou un objet utilisateur.

Donc, maintenant vous avez créé un excellent flux d'inscription !

Mais nous n'avons pas encore terminé. Il est temps de stocker certaines données utilisateur sur Firebase lorsqu'ils s'inscrivent pour la première fois.

C'est quelque chose que je pense personnellement être une très bonne idée. Disons que vous construisez un site web de publication d'emplois où vous voulez lister tous les candidats qui sont inscrits sur votre site web. Comment pourrez-vous le faire si vous ne stockez pas les données des utilisateurs individuels ?

Maintenant, ajoutons une logique pour stocker les données utilisateur dans la section suivante.👋

## Comment sauvegarder un utilisateur dans Firebase

Tout d'abord, créons notre base de données. Pour commencer, allez dans votre **tableau de bord du projet Firebase** et cliquez sur l'onglet **Base de données Firebase** dans la barre latérale.

Maintenant, cliquez sur le bouton **Créer une base de données** pour créer une base de données. Vous serez invité à sélectionner un mode de démarrage pour vos règles de sécurité Cloud Firestore. Pour l'instant, sélectionnez le mode test, mais vous pourrez le changer plus tard. Ensuite, cliquez sur le bouton **Suivant**.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/EFGHwYJ-R.png)

Ensuite, sélectionnez l'emplacement de votre Cloud Firestore et cliquez sur le bouton **Activer**. Maintenant que nous avons configuré notre base de données, nous sommes prêts à écrire du code ! Plongeons-nous directement.

Tout d'abord, ouvrez votre fichier `config.js` et importez le module `getFirestore` depuis Firebase :

```
import { getFirestore } from "firebase/firestore";

```

Ensuite, nous allons créer une variable appelée `db` et la définir égale à `getFirestore()`. Enfin, exportez `db` avec `auth` comme ceci :

```
// Initialiser Firebase Firestore
const db = getFirestore();
export { auth, db };

```

Maintenant, créons un fichier et nommons-le `createUserDocument.js` à l'intérieur du dossier `firebase`. Ensuite, ajoutez ce morceau de code :

```
import { collection, doc, getDocs, query, serverTimestamp, setDoc, where } from "firebase/firestore";

import { db } from "./config";

export const createUserDocument = async (user) => {
  const q = query(collection(db, "users"), where("uid", "==", user.uid));
  const { docs } = await getDocs(q);

  if (docs.length === 0) {
    const { uid, displayName, email, photoURL, reloadUserInfo } = user;

    const docRef = doc(db, `users/${uid}`);
    await setDoc(docRef, {
      displayName,
      email,
      photoURL,
      username: reloadUserInfo.screenName,
      createdAt: serverTimestamp(),
    });
  }
};

```

Je vais vous expliquer le code ci-dessus. Ne vous inquiétez pas, ce n'est pas effrayant ! Vous comprendrez tout en un clin d'œil.

Tout d'abord, nous avons créé une fonction asynchrone appelée `createUserDocument`. Cette fonction sera utilisée pour créer de nouveaux documents utilisateur dans notre base de données.

Ensuite, nous avons utilisé la méthode `query` sur `db` pour interroger la collection `users` avec une clause `where` afin de trouver tous les documents avec un `uid` égal à l'uid de l'utilisateur fourni.

Ensuite, nous passons cette requête `q` à la méthode `getDocs(q)`. Cette méthode retourne un tableau de `docs`.

Et après cela, nous avons ajouté une instruction if pour vérifier si le tableau docs est vide ou non. S'il est vide, alors nous créerons un nouveau docRef en utilisant la méthode `doc` qui prend deux arguments : `db` et l'`id du document`. Cette méthode retourne une référence à ce document.

Enfin, nous appellerons la méthode `setDoc` qui prend à nouveau deux arguments : `docRef` et les données utilisateur que nous voulons sauvegarder dans la base de données.

Maintenant, ouvrez votre fichier `useLogin.js` et importez la fonction `createUserDocument` :

```
import { createUserDocument } from "../firebase/createUserDocument";

```

Et juste au-dessus de l'instruction dispatch, appelez la fonction `createUserDocument` comme ceci :

```
const user = res.user;
await createUserDocument(user);
dispatch({ type: "LOGIN", payload: user });

```

Maintenant, essayez de vous connecter à nouveau et cela devrait sauvegarder le nouvel utilisateur dans Firestore.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/6KFqHkwMa.png)

🎉 C'est tout ! Vous avez implémenté avec succès un excellent flux d'authentification et maintenant votre application est prête à stocker les données utilisateur lorsque les utilisateurs s'inscrivent pour la première fois.

Maintenant, allez et rendez votre application incroyable, et n'oubliez pas de me faire savoir comment cela se passe !

## 👋 Merci d'avoir lu ce tutoriel

Merci d'avoir pris le temps de lire ce guide !

J'espère que vous avez apprécié ce tutoriel et que vous l'avez trouvé utile. Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter via [Twitter](https://twitter.com/thefierycoder) ou [LinkedIn](https://www.linkedin.com/in/thefierycoder/) !

Si vous avez apprécié cet article, je vous serais très reconnaissant de le partager sur votre plateforme de médias sociaux préférée.

N'hésitez pas à jeter un coup d'œil à ma [chaîne YouTube](https://www.youtube.com/c/TheFieryCoder) et à vous abonner si vous l'aimez.

À bientôt, et à la prochaine ! 👋

Merci d'avoir lu.