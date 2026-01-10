---
title: Comment ajouter l'authentification à une application Vue en utilisant Auth0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T20:11:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-auth0
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/0_j4pVnDlQTDvfWtw_-1.jpeg
tags:
- name: Auth0
  slug: auth0
- name: authentication
  slug: authentication
- name: vue
  slug: vue
seo_title: Comment ajouter l'authentification à une application Vue en utilisant Auth0
seo_desc: 'By Jennifer Bland

  Auth0 is a flexible, drop-in solution to add authentication and authorization services
  to your applications. See how easy it is to add to your Vue application so you can
  register and login users with their email address and a passwo...'
---

Par Jennifer Bland

Auth0 est une solution flexible et prête à l'emploi pour ajouter des services d'authentification et d'autorisation à vos applications. Voyez à quel point il est facile de l'ajouter à votre application Vue afin de pouvoir enregistrer et connecter des utilisateurs avec leur adresse e-mail et un mot de passe.

# Ce que nous allons créer

Nous allons créer une application Vue très simple en utilisant le Vue CLI. Nous allons modifier l'application échafaudée par défaut afin de pouvoir utiliser Auth0 pour soit enregistrer un nouvel utilisateur, soit connecter un utilisateur existant. Une fois qu'un utilisateur est connecté, il aura accès à la page **À propos**.

Les utilisateurs pourront s'enregistrer avec l'application en utilisant le système d'authentification par e-mail et mot de passe dans Auth0.

# Création de notre projet

Je vais utiliser le Vue CLI pour échafauder un projet pour commencer. Pour cela, vous devez avoir le Vue CLI installé sur votre système. Si vous **NE L'AVEZ PAS** installé, vous pouvez l'installer globalement avec cette commande :

```
npm install -g @vue/cli
```

Maintenant, nous pouvons utiliser le Vue CLI pour créer notre projet. Créez un nouveau projet en utilisant cette commande :

```
vue create vue-authentication-auth0
```

Vous serez invité à choisir un préréglage. Choisissez « Sélectionner les fonctionnalités manuellement » et sélectionnez « babel », « Router » et « Linter / Formatter ».

On vous demandera si vous souhaitez utiliser le mode historique pour le routeur. Choisissez « Oui » (devrait être la valeur par défaut).

Vous pouvez sélectionner n'importe quel linter que vous souhaitez, mais pour ce tutoriel, je vais sélectionner « Eslint + Prettier ».

Une fois que le Vue CLI a terminé, il vous donnera les commandes pour changer de répertoire dans le nouveau répertoire qui vient d'être créé et la commande pour démarrer le serveur. Suivez ces instructions. Une fois le serveur démarré, vous pouvez ouvrir votre navigateur à l'adresse `localhost:8080`. Vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_aULwhJQrKCD0RZ8t.png)

# Comment configurer un compte Auth0

La première chose que vous devrez faire est de créer un compte avec Auth0 si vous n'en avez pas déjà un. Il est gratuit de créer un compte. Vous pouvez [créer votre compte gratuit ici](https://auth0.com/signup).

# Comment créer notre application Auth0

Une fois que vous avez créé votre compte Auth0 gratuit, connectez-vous à votre compte. Dans la navigation de gauche, cliquez sur Applications.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_dx-jheyJRHChE5ET.png)

À partir de là, cliquez sur le bouton Créer une application.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_zXLpqqkLENVyAASt.png)

Une boîte de dialogue s'affichera pour que vous puissiez fournir un nom pour votre application et spécifier le type d'application que vous allez créer.

Le nom de mon application est **Vue Authentication Auth0**. Vous pouvez mettre ce que vous voulez pour le nom de votre application.

Pour le type d'application, sélectionnez **Application Web à Page Unique**.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_44vQOJ9golspep06.png)

Après la création de votre application, l'onglet Démarrage rapide fournira des instructions sur la façon d'implémenter Auth0 dans votre application Web en utilisant les frameworks JavaScript les plus populaires.

Puisque nous utilisons Vue.js pour notre application, cliquez sur l'icône Vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_jGC1dkmWfYbUhXQL.png)

Auth0 fournit des instructions très détaillées sur la façon d'implémenter leur produit d'authentification en tant que service. Pour ce tutoriel, nous allons implémenter leurs instructions dans l'application Vue que nous avons déjà créée.

# Comment configurer les paramètres de votre application

Vous pouvez accéder à vos paramètres en cliquant sur l'onglet Paramètres en haut de la page.

Vous verrez votre Domaine et votre ID Client sous Informations de base. Nous reviendrons à cela plus tard car nous aurons besoin de stocker ces valeurs pour que notre application fonctionne.

Dans la section URI de l'application, nous devrons définir nos **URL de rappel autorisées**, **URL de déconnexion autorisées** et **Origines Web autorisées**.

Pour tester notre application localement, nous utiliserons l'URL **http://localhost:8080**.

**NOTE :** si vous décidez d'héberger votre application quelque part comme sur Netlify ou Heroku, vous devrez mettre à jour tous ces paramètres avec l'URL de votre application hébergée.

Définissez vos **URL de rappel autorisées**, **URL de déconnexion autorisées** et **Origines Web autorisées** sur **http://localhost:8080**.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_nX1DoL-RXVC1x4oD.png)

# Comment installer le SDK Auth0

Retournez à votre application Vue et ajoutez le SDK Client Auth0 avec cette commande :

```
npm install @auth0/auth0-spa-js
```

# Comment créer un wrapper d'authentification

Le SDK Auth0 nécessite qu'il soit initialisé avant que votre application Vue ne démarre.

Vue dispose de hooks de cycle de vie que nous pourrions potentiellement utiliser pour initialiser le SDK. Vous pourriez penser que nous pourrions utiliser un hook **beforeCreate** dans le fichier **App.vue**, mais cela ne fonctionnera pas. Laissez-moi vous montrer pourquoi.

Voici une image des hooks de cycle de vie de Vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_NuSvkkm1kohKVJbt.png)

**beforeCreate** est le tout premier hook de cycle de vie de Vue à se déclencher. Mais remarquez dans cette image qu'il se déclenche après la création de l'application Vue avec **new Vue()**.

Nous devons pouvoir initialiser le SDK Auth0 avant le **new Vue()** qui crée notre application Vue. Vue fournit un mécanisme pour cela avec le plugin Vue.

Pour utiliser un plugin, vous devez l'appeler avec la commande **Vue.use()**. Cette commande doit être effectuée avant de démarrer votre application en appelant **new Vue()**.

Le wrapper d'authentification que nous allons créer sera en fait un plugin Vue.

Dans le répertoire **src**, créez un nouveau répertoire appelé **auth**. À l'intérieur de ce répertoire auth, créez un fichier appelé **index.js**.

Nous allons copier le code fourni dans l'onglet Démarrage rapide et le coller dans ce fichier. Voici le code :

```
import Vue from "vue";
import createAuth0Client from "@auth0/auth0-spa-js";
/** Définir une action par défaut à effectuer après l'authentification */
const DEFAULT_REDIRECT_CALLBACK = () =>
  window.history.replaceState({}, document.title, window.location.pathname);
let instance;
/** Retourne l'instance actuelle du SDK */
export const getInstance = () => instance;
/** Crée une instance du SDK Auth0. Si une instance a déjà été créée, elle retourne cette instance */
export const useAuth0 = ({
  onRedirectCallback = DEFAULT_REDIRECT_CALLBACK,
  redirectUri = window.location.origin,
  ...options
}) => {
  if (instance) return instance;
// L'instance est simplement un objet Vue
  instance = new Vue({
    data() {
      return {
        loading: true,
        isAuthenticated: false,
        user: {},
        auth0Client: null,
        popupOpen: false,
        error: null
      };
    },
    methods: {
      /** Authentifie l'utilisateur en utilisant une fenêtre popup */
      async loginWithPopup(options, config) {
        this.popupOpen = true;
try {
          await this.auth0Client.loginWithPopup(options, config);
        } catch (e) {
          // eslint-disable-next-line
          console.error(e);
        } finally {
          this.popupOpen = false;
        }
this.user = await this.auth0Client.getUser();
        this.isAuthenticated = true;
      },
      /** Gère le rappel lors de la connexion en utilisant une redirection */
      async handleRedirectCallback() {
        this.loading = true;
        try {
          await this.auth0Client.handleRedirectCallback();
          this.user = await this.auth0Client.getUser();
          this.isAuthenticated = true;
        } catch (e) {
          this.error = e;
        } finally {
          this.loading = false;
        }
      },
      /** Authentifie l'utilisateur en utilisant la méthode de redirection */
      loginWithRedirect(o) {
        return this.auth0Client.loginWithRedirect(o);
      },
      /** Retourne toutes les revendications présentes dans le jeton d'identification */
      getIdTokenClaims(o) {
        return this.auth0Client.getIdTokenClaims(o);
      },
      /** Retourne le jeton d'accès. Si le jeton est invalide ou manquant, un nouveau est récupéré */
      getTokenSilently(o) {
        return this.auth0Client.getTokenSilently(o);
      },
      /** Obtient le jeton d'accès en utilisant une fenêtre popup */
getTokenWithPopup(o) {
        return this.auth0Client.getTokenWithPopup(o);
      },
      /** Déconnecte l'utilisateur et supprime leur session sur le serveur d'autorisation */
      logout(o) {
        return this.auth0Client.logout(o);
      }
    },
    /** Utilisez cette méthode de cycle de vie pour instancier le client SDK */
    async created() {
      // Créez une nouvelle instance du client SDK en utilisant les membres de l'objet d'options donné
      this.auth0Client = await createAuth0Client({
        ...options,
        client_id: options.clientId,
        redirect_uri: redirectUri
      });
try {
        // Si l'utilisateur revient à l'application après l'authentification..
        if (
          window.location.search.includes("code=") &&
          window.location.search.includes("state=")
        ) {
          // gère la redirection et récupère les jetons
          const { appState } = await this.auth0Client.handleRedirectCallback();
// Notifie les abonnés que le rappel de redirection a eu lieu, en passant l'appState
          // (utile pour récupérer tout état pré-authentification)
          onRedirectCallback(appState);
        }
      } catch (e) {
        this.error = e;
      } finally {
        // Initialisez notre état d'authentification interne
        this.isAuthenticated = await this.auth0Client.isAuthenticated();
        this.user = await this.auth0Client.getUser();
        this.loading = false;
      }
    }
  });
return instance;
};
// Créez un simple plugin Vue pour exposer l'objet wrapper dans toute l'application
export const Auth0Plugin = {
  install(Vue, options) {
    Vue.prototype.$auth = useAuth0(options);
  }
};
```

# Comment créer un fichier de configuration

L'objet d'options passé au plugin est utilisé pour fournir les valeurs pour **clientId** et **domain** dont j'ai parlé plus tôt et que j'ai dit que nous obtiendrions plus tard.

Dans le répertoire racine de votre application, créez un nouveau fichier appelé **auth_config.json**. Nous allons remplir les valeurs de votre application pour **domain** et **clientId**. Mettez ce code dans le fichier auth_config.json et assurez-vous de le mettre à jour avec les valeurs de votre application.

```
{   
  "domain": "yourAppValuesHere",   
  "clientId": "yourAppValuesHere"
}
```

Ce fichier de configuration contient des valeurs non sensibles relatives à votre application Auth0. Ce fichier ne doit pas être validé dans le contrôle de source. Nous pouvons faire cela en ajoutant le nom de fichier au fichier **.gitignore**.

Ouvrez le fichier **.gitignore** et ajoutez `auth_config.json` dans le fichier.

# Comment ajouter le plugin à notre application Vue

Maintenant que nous avons créé notre plugin, nous devons dire à Vue de l'utiliser. Ouvrez le fichier **main.js**. Ajoutez ces deux instructions d'importation qui importent notre plugin ainsi que notre domaine et clientId du fichier **auth_config.json**.

```
// Importer la configuration Auth0
import { domain, clientId } from "../auth_config.json";
// Importer le plugin ici
import { Auth0Plugin } from "./auth";
```

Ensuite, nous devons dire à Vue d'utiliser notre plugin. Après les instructions d'importation, ajoutez ce code :

```
// Installer le plugin d'authentification ici
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});
```

# Comment se connecter à l'application

Si vous regardez le code du plugin dans le fichier **auth/index.js**, vous remarquerez qu'il y a deux méthodes de connexion différentes fournies : **loginWithPopup** et **loginWithRedirect**.

Auth0 fournit une page de connexion hébergée que toute application peut utiliser pour se connecter ou enregistrer des utilisateurs pour leur application.

La méthode **loginWithRedirect** accédera à la page de connexion hébergée. Cela signifie que lorsque les utilisateurs cliquent sur le bouton de connexion, l'URL changera pour pointer vers le site Web Auth0 où l'utilisateur entrera ses identifiants de connexion. Après qu'ils se soient authentifiés avec succès, ils seront redirigés vers notre application.

Si nous ne voulons pas faire cette redirection, Auth0 fournit l'option de se connecter ou d'enregistrer des utilisateurs via une popup qui s'affiche sur notre site Web.

Je vais vous montrer comment utiliser ces deux méthodes de connexion.

Ouvrez le fichier **App.vue**. La barre de navigation contient actuellement deux entrées pour les pages Accueil et À propos. Nous devons ajouter deux boutons pour la connexion. Ajoutez ce code dans la barre de navigation qui devrait ressembler à ceci :

```
<div id="nav">
  <router-link to="/">Accueil </router-link>|
  <router-link to="/about">À propos</router-link> |
  <div v-if="!$auth.loading">
    |
    <button @click="login" v-if="!$auth.isAuthenticated">
      Connexion
    </button>
    |
    <button @click="loginPopup" v-if="!$auth.isAuthenticated">
      Connexion Popup
    </button>
    |</div>
</div>
```

Remarquez que les boutons sont enveloppés dans une directive qui s'assure que **$auth.loading** est faux. Si vous passez en revue le code de notre plugin, il y a une section de données avec une valeur **isAuthenticated**. Cette valeur est définie si un utilisateur s'authentifie avec succès avec Auth0. Si l'utilisateur est authentifié, nous ne voulons pas afficher les deux boutons de connexion.

Lorsque nous ajoutons la div, les boutons apparaissent sur la ligne en dessous des liens pour les boutons Accueil et À propos. Je veux qu'ils soient tous sur la même ligne, donc je mets à jour les styles CSS pour qu'ils soient comme ceci :

```
#nav { 
  display: flex; 
  justify-content: center; 
  padding: 30px; 
} 
#nav a { 
  font-weight: bold; 
  color: #2c3e50; 
  padding: 0 5px; 
}
```

Maintenant, lorsque vous regardez l'application, vous verrez les deux boutons.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_LyHE1bybFhyso-Db.png)

Les deux boutons appellent les méthodes **login** et **loginPopup**. Implémentons-les maintenant.

Ajoutez un objet méthodes avec deux méthodes. Voici le code :

```
methods: { 
  login() { 
    this.$auth.loginWithRedirect(); 
  }, 
  loginPopup() { 
    this.$auth.loginWithPopup(); 
  }, 
}
```

Le **this.$auth** est un handle pour notre plugin. Nous appelons ensuite les méthodes disponibles dans notre plugin.

Retournez à votre application. Si vous cliquez sur le bouton de connexion, vous devriez être redirigé vers la page de connexion hébergée par Auth0.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_BopphiRqeQ3ReXlI.png)

Si vous cliquez sur le bouton Connexion Popup, vous verrez une modale de connexion dans votre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_e40CPdd19xjobDw-.png)

Quelle que soit celle que vous choisissez, vous verrez que vous avez la possibilité de vous connecter ou de vous inscrire. Allez-y et créez un compte. Lorsque vous revenez à l'application, vous verrez que les deux boutons de connexion sont masqués. Ils sont masqués car la valeur **isAuthenticated** dans le plugin est maintenant vraie.

# Comment implémenter la déconnexion

L'étape suivante consiste à implémenter une déconnexion. Ouvrez le fichier **App.vue**. Ajoutez un bouton pour la déconnexion comme ceci :

```
<button @click="logout" v-if="$auth.isAuthenticated">
  Déconnexion
</button>
```

Ici, nous avons une directive pour n'afficher ce bouton que si l'utilisateur est actuellement authentifié. Retournez à votre application et vous devriez maintenant voir le bouton Déconnexion.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_qp0QOUNUP-wz3iUn--1-.png)

Ajoutez cette méthode pour implémenter la fonctionnalité de déconnexion :

```
logout() { 
  this.$auth.logout(); 
  this.$router.push({ path: '/' }); 
}
```

Dans cette méthode, nous appelons la fonction de déconnexion dans notre plugin. Au cas où l'utilisateur se trouverait sur une page qui n'est visible que par les utilisateurs authentifiés, nous redirigeons l'utilisateur vers la page d'accueil.

# Comment ne montrer les pages qu'aux utilisateurs authentifiés

Actuellement, notre application n'a qu'une page d'accueil et une page À propos. Au lieu de créer une nouvelle page, définissons la page À propos pour qu'elle ne soit visible que si un utilisateur est connecté.

Nous ne voulons montrer la page À propos dans la barre de navigation que si l'utilisateur est connecté. Nous allons prendre la même directive que nous utilisons pour afficher le bouton Déconnexion et la mettre sur la page À propos dans la barre de navigation. Mettez à jour la barre de navigation pour qu'elle soit comme ceci :

```
<router-link v-if="$auth.isAuthenticated" to="/about">À propos</router-link>
```

# Comment ajouter une garde de route

Nous avons masqué le lien vers la page À propos dans la barre de navigation si un utilisateur n'est pas actuellement authentifié. Mais un utilisateur peut taper l'URL **/about** pour accéder directement à la page. Cela montre qu'un utilisateur non authentifié peut accéder à cette page. Vous pouvez éviter cela en utilisant une garde de route.

Dans le répertoire auth, créez un nouveau fichier appelé **authGuard.js**.

Ajoutez ce code au fichier :

```
import { getInstance } from "./index";
export const authGuard = (to, from, next) => {
  const authService = getInstance();
const fn = () => {
    // Si l'utilisateur est authentifié, continuez avec la route
    if (authService.isAuthenticated) {
      return next();
    }
// Sinon, connectez-vous
    authService.loginWithRedirect({ appState: { targetUrl: to.fullPath } });
  };
// Si le chargement est déjà terminé, vérifiez notre état d'authentification en utilisant `fn()`
  if (!authService.loading) {
    return fn();
  }
// Surveillez la propriété de chargement pour qu'elle change avant de vérifier isAuthenticated
  authService.$watch("loading", loading => {
    if (loading === false) {
      return fn();
    }
  });
};
```

Ce code vérifie si l'utilisateur est actuellement authentifié. S'il ne l'est pas, il affiche la page de connexion hébergée par Auth0 pour que l'utilisateur se connecte. Si l'utilisateur échoue à se connecter ou n'est pas en mesure de se connecter avec succès, il est redirigé loin de la page qu'il essayait d'accéder et qui a la garde de route.

Maintenant, implémentons cette garde de route dans notre routeur Vue. Ouvrez le fichier **index.js** dans le répertoire du routeur.

En haut du fichier, ajoutez une importation pour le fichier authGuard que nous venons de créer :

```
import { authGuard } from "../auth/authGuard";
```

Ensuite, nous devons ajouter la garde de route à la route /about. Mettez à jour la route /about pour qu'elle soit comme ceci :

```
{ 
  path: '/about', 
  name: 'About', 
  component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'), 
  beforeEnter: authGuard 
}
```

Retournez à votre application. Si vous n'êtes pas actuellement authentifié, connectez-vous à votre application. Vous devriez voir l'entrée À propos dans la barre de navigation. Maintenant, déconnectez-vous de l'application. Essayez manuellement d'aller à l'URL **/about**. Vous devriez être redirigé vers la page de connexion hébergée par Auth0.

Félicitations ! Vous avez ajouté avec succès l'authentification Auth0 à votre application Vue.

# Obtenez le code

J'ai le [code complet dans mon compte GitHub ici](https://github.com/ratracegrad/Vue-Auth0-Authentication-Tutorial). Si vous obtenez le code, faites-moi plaisir et étoilez mon dépôt. Merci !

# Utilisation d'autres méthodes d'authentification

J'ai écrit plusieurs articles de suivi sur l'ajout d'authentification à votre application Vue en utilisant d'autres méthodes d'authentification.

Vous souhaitez utiliser Firebase pour l'authentification, [lisez cet article](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-firebase/).

Vous souhaitez utiliser AWS Amplify pour l'authentification, [lisez cet article](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify/).

# Conclusion

Auth0 est un produit d'authentification en tant que service que vous pouvez ajouter à votre application. Il fournit une authentification très facile à utiliser.

J'espère que vous avez apprécié cet article. Si vous l'aimez, partagez-le. Merci d'avoir lu. Et vous pouvez lire plus de mes tutoriels sur [mon site web personnel](https://www.jenniferbland.com/).