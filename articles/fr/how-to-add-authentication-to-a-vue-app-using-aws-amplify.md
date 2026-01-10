---
title: Comment ajouter l'authentification à une application Vue en utilisant AWS Amplify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-14T22:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/0_QrOUXeTdCaxjv6o_-1.jpeg
tags:
- name: authentication
  slug: authentication
- name: AWS
  slug: aws
- name: vue
  slug: vue
seo_title: Comment ajouter l'authentification à une application Vue en utilisant AWS
  Amplify
seo_desc: 'By Jennifer Bland

  In this article, we’re going to create a very simple Vue application using the Vue
  CLI. We’ll modify the default scaffolded application so it provides a form to register
  as a new user, a login page, and a dashboard page only shown t...'
---

Par Jennifer Bland

Dans cet article, nous allons créer une application Vue très simple en utilisant le CLI Vue. Nous allons modifier l'application échafaudée par défaut pour qu'elle fournisse un formulaire permettant de s'inscrire en tant que nouvel utilisateur, une page de connexion et une page de tableau de bord uniquement visible pour les personnes connectées.

Les utilisateurs pourront s'inscrire en utilisant un email et un mot de passe. Une fois inscrits et connectés, ils seront présentés avec la page du tableau de bord.

# Comment créer notre projet

J'utiliserai le CLI Vue pour échafauder un projet pour commencer. Pour cela, vous devez avoir le CLI Vue installé sur votre système. Si vous ne l'avez pas installé, vous pouvez l'installer globalement avec cette commande :

```
npm install -g @vue/cli
```

Maintenant, nous pouvons utiliser le CLI Vue pour créer notre projet. Créez un nouveau projet en utilisant cette commande :

```
vue create vue-amplify-auth-tutorial
```

On vous demandera de choisir un préréglage. Choisissez « Sélectionner les fonctionnalités manuellement », puis sélectionnez « babel », « Router » et « Linter / Formatter ».

On vous demandera si vous souhaitez utiliser le mode historique pour le routeur. Choisissez « Oui » (devrait être la valeur par défaut).

Pour un linter, je sélectionne « ESLint avec prévention des erreurs uniquement ».

Une fois que le CLI Vue a terminé, il vous donnera les commandes pour changer de répertoire dans le nouveau répertoire qui vient d'être créé et la commande pour démarrer le serveur. Suivez ces instructions.

Une fois le serveur démarré, vous pouvez ouvrir votre navigateur à l'adresse `localhost:8080`. Vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_S9E-Jj_1zY76iZBj.png)

# Qu'est-ce qu'AWS Amplify ?

AWS Amplify est un framework open-source créé par Amazon qui contient un ensemble d'outils et de services qui peuvent être utilisés ensemble ou séparément.

L'un des outils est Amplify Auth. Amplify Auth vous permet de configurer rapidement une authentification sécurisée et de contrôler ce à quoi les utilisateurs ont accès dans votre application.

Le framework Amplify utilise Amazon Cognito comme principal fournisseur d'authentification. Amazon Cognito est un service robuste de répertoire d'utilisateurs qui gère l'inscription des utilisateurs, l'authentification, la récupération de compte et d'autres opérations.

# Créer un compte AWS

Pour commencer, vous devrez créer un compte AWS ici. Si vous n'avez pas de compte AWS, [suivez les instructions ici pour en créer un](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).

# Installer et configurer le CLI Amplify

Le CLI Amplify est une chaîne d'outils unifiée pour créer des services cloud AWS pour votre application. Vous pouvez l'installer globalement avec cette commande :

```
npm install -g @aws-amplify/cli
```

Ensuite, nous devons configurer Amplify en exécutant la commande suivante :

```
amplify configure
```

Cette commande ouvrira une nouvelle fenêtre de navigateur et vous demandera de vous connecter à la console AWS. Une fois connecté, retournez à votre terminal et appuyez sur `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SBiQgDy2bw0OGeX3.png)

On vous demandera de spécifier la région AWS. Sélectionnez la région la plus proche de vous.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_Wx3wr2Ohnd7_2RAG.png)

Vous devrez spécifier le nom d'utilisateur du nouvel utilisateur IAM. Il fournira un nom par défaut que vous pouvez utiliser en appuyant sur entrée ou vous pouvez spécifier votre propre nom. Je vais appeler mon utilisateur `auth-demo`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_z0qKKxKSjp_1K98H.png)

Lorsque vous appuyez sur `Entrée`, vous serez redirigé vers votre navigateur.

Cliquez sur le bouton Suivant : Autorisations.

Cliquez sur le bouton Suivant : Balises.

Cliquez sur le bouton Suivant : Examen.

Cliquez sur le bouton Créer un utilisateur.

Maintenant, retournez à votre terminal et appuyez sur `Entrée` pour continuer.

Tapez l'`accessKeyId` de l'utilisateur que vous venez de créer, puis appuyez sur `Entrée`.

Tapez le `secretAccessKey` de l'utilisateur que vous venez de créer, puis appuyez sur `Entrée`.

On vous demandera de saisir un nom de profil. J'accepte la valeur fournie (par défaut) en appuyant simplement sur `Entrée`.

Lorsque tout est terminé, vous devriez recevoir un message dans votre terminal indiquant que le nouvel utilisateur a été configuré avec succès.

# Initialiser un nouveau back-end

Maintenant que nous avons une application Vue en cours d'exécution, il est temps de configurer Amplify afin que nous puissions créer les services back-end nécessaires pour supporter l'application. À partir de la racine de votre application Vue, exécutez :

```
amplify init
```

# Créer le service d'authentification

Nous devons ajouter un service d'authentification à notre application Vue. Dans le répertoire racine de votre application Vue, entrez cette commande :

```
amplify add auth
```

Lorsque vous initialisez Amplify, on vous demandera certaines informations sur votre application. Entrez un nom de projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_0Q7RiIPnBCAo90Kf.png)

Définissez le nom de l'environnement back-end sur `dev`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SMbI1iNM5XELFdfp.png)

Parfois, le CLI vous demandera de modifier un fichier — il utilisera cet éditeur pour ouvrir ces fichiers. Sélectionnez votre logiciel d'édition de code préféré.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_juPUaS2SIkR0UnxL.png)

Amplify fournira des fichiers de configuration pour votre application front-end afin de se connecter à cet environnement back-end. Puisque Vue est basé sur JavaScript, nous sélectionnerons cela ici.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_enPauC_uAMYzoDFV.png)

Nous utilisons Vue, alors sélectionnez cela comme notre framework JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_xOxbC5xEGdudv-ej.png)

Le CLI Vue configure les fichiers sources de votre projet dans un dossier `./src`. Sélectionnez `src` pour le chemin du répertoire source.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_iLN4pnHKGUGB3tCz.png)

Lorsque votre projet est prêt à être hébergé, Vue générera votre site web, prêt pour une utilisation publique, dans un dossier appelé `dist`. C'est la valeur par défaut, donc vous pouvez simplement appuyer sur `Entrée` pour continuer.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_u1tw63qKuNAsPJ9B.png)

Le déploiement automatisé d'Amplify doit savoir quelles étapes sont nécessaires pour construire votre application pour la publication. Ici, nous définirons cela comme le script de construction par défaut du CLI Vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_SqFEoy03S2eingpb.png)

Si Amplify doit exécuter l'application en mode développement, il doit savoir comment démarrer le serveur de développement. Encore une fois, nous utiliserons les scripts par défaut du CLI Vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_WR5XjxUw9TmYlTUv.png)

Enfin, Amplify a besoin d'un compte AWS pour se connecter afin que nous puissions commencer à créer les services back-end. Il s'agit du profil que vous avez créé avec la commande `amplify configure` précédemment. Sélectionnez « oui » en tapant `y` et en appuyant sur `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_oTD19eyWt9KdCb6J.png)

Procédez à la sélection de votre profil dans la liste, puis appuyez sur `Entrée`. Amplify va maintenant commencer à déployer votre framework back-end.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_fX2wHxziZZil6sJ3.png)

Lorsque vous initialisez un nouveau projet Amplify, plusieurs choses se produisent :

* Il crée un répertoire de premier niveau appelé `amplify` qui stocke votre définition back-end. Au cours du tutoriel, vous ajouterez des capacités telles que l'authentification, l'API GraphQL, le stockage et les règles d'autorisation pour l'API. À mesure que vous ajoutez des fonctionnalités, le dossier `amplify` grandira avec des modèles d'infrastructure-as-code qui définissent votre pile back-end. L'infrastructure-as-code est une méthode de meilleure pratique pour créer une pile back-end reproductible.
* Il crée un fichier appelé `aws-exports.js` dans le répertoire `src` qui contient toute la configuration des services que vous créez avec Amplify. C'est ainsi que le client Amplify peut obtenir les informations nécessaires sur vos services back-end.
* Il modifie le fichier `.gitignore`, en ajoutant certains fichiers générés à la liste d'ignorance.
* Un projet cloud est créé pour vous dans la console AWS Amplify, accessible en exécutant `amplify console`. La console fournit une liste d'environnements back-end, des liens profonds vers les ressources provisionnées par catégorie Amplify, l'état des déploiements récents et des instructions sur la manière de promouvoir, cloner, tirer et supprimer des ressources back-end.

Pour déployer le service, exécutez la commande `push`.

# Installer les bibliothèques Amplify

Nous devons installer les dépendances Amplify dans notre application Vue. Vous pouvez les installer avec cette commande :

```
npm install aws-amplify
```

# Configurer notre application

Nous devons ajouter Amplify à notre application Vue. Ouvrez le fichier `main.js` et ajoutez ce qui suit après la dernière ligne d'importation :

```
import Amplify from 'aws-amplify';
import awsconfig from './aws-exports'; 
Amplify.configure(awsconfig);
```

Le code ci-dessus configure avec succès Amplify. À mesure que vous ajoutez ou supprimez des catégories et que vous apportez des mises à jour à votre configuration back-end en utilisant le CLI Amplify, la configuration dans `aws-exports.js` se mettra à jour automatiquement.

# Créer une page d'inscription

Nous avons besoin d'une page qui permettra aux nouveaux utilisateurs de s'inscrire à notre application. Dans le dossier views, créez un nouveau fichier appelé `Register.vue`.

Nous devons ajouter cette nouvelle page à nos routes, puis l'afficher dans la navigation. Ouvrez le fichier `index.js` dans le dossier `router`. Ajoutez ceci au tableau des routes.

```
{
    path: '/register',
    name: 'Register',
    component: () =>
        import(/* webpackChunkName: "register" */ '../views/Register.vue'),
},
```

Maintenant, ajoutez ceci à notre navigation. Ouvrez le fichier `App.vue` et ajoutez une entrée pour `Register` dans la nav. Votre nav devrait ressembler à ceci :

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link>
</div>
```

Retournez à votre fichier `Register.vue`. Cette page contiendra un formulaire pour qu'un utilisateur puisse entrer son email et un mot de passe pour s'inscrire en tant que nouvel utilisateur. Voici le code que vous devez mettre dans la section template :

```
<div class="container">
    <form @submit.prevent="register">
        <h2>Register</h2>
        <input
            type="email"
            v-model="email"
            placeholder="Email address..."
        />
        <input
            type="password"
            v-model="password"
            placeholder="password..."
        />
        <button>Register</button>
    </form>
</div>
```

Si vous regardez notre formulaire, les deux champs de saisie et le bouton sont collés les uns aux autres.

Vous voulez ajouter un peu d'espace entre les trois champs ? Je pourrais ajouter du CSS à cette page, mais cela ne s'appliquerait qu'à cette page. Nous allons réutiliser ce formulaire sur la page de connexion que nous allons créer ensuite.

Pour obtenir des styles qui fonctionnent sur les deux pages, mettons le CSS suivant dans le fichier `App.vue`. Ouvrez le fichier `App.vue` et ajoutez le style suivant :

```
:input {   
  margin-right: 10px; 
}
```

Retournez au fichier `Register.vue`. Nous capturons les valeurs que l'utilisateur entre pour son email et son mot de passe, nous devons donc les ajouter à l'objet data. Ajoutez-les à l'objet data pour qu'il ressemble à ceci :

```
data() { 
  return { 
    email: '', 
    password: '', 
  }; 
},
```

Lorsque l'utilisateur soumet le formulaire, il appelle la méthode `register`. Voici le code de cette méthode :

```
async register() {
    try {
        await Auth.signUp({
            username: this.email,
            password: this.password,
        });
        alert('User successfully registered. Please login');
    } catch (error) {
        alert(error.message);
    }
},
```

Cette méthode utilise `Auth` du package `aws-amplify` que nous avons installé. Ajoutez cette importation au début de la section script.

```
import { Auth } from 'aws-amplify';
```

Maintenant, ouvrez votre application et inscrivez un nouvel utilisateur. Si tout se passe bien, vous recevrez une alerte indiquant que l'utilisateur a été inscrit.

# Créer une page de connexion

Une fois qu'un utilisateur a enregistré un compte avec notre application, il a besoin d'une page par laquelle il peut se connecter. Dans le dossier `views`, créez un nouveau fichier appelé `Login.vue`.

Nous devons ajouter cette nouvelle page à nos routes, puis l'afficher dans la navigation. Ouvrez le fichier `index.js` dans le dossier `router`. Ajoutez ceci au tableau des routes.

```
{
    path: '/login',
    name: 'Login',
    component: () =>
        import(/* webpackChunkName: "login" */ '../views/Login.vue'),
},
```

Maintenant, ajoutez ceci à notre navigation. Ouvrez le fichier `App.vue` et ajoutez une entrée pour `Register` dans la nav. Votre nav devrait ressembler à ceci :

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/login">Login</router-link> 
</div>
```

Retournez à votre fichier `Login.vue`. Vous pouvez copier le code HTML dans la section template du fichier `Register.vue` et le coller dans ce nouveau fichier. Changez toutes les références de `Register` en `Login`. Votre section template devrait ressembler à ceci :

```
<div class="container">
    <form @submit.prevent="login">
        <h2>Login</h2>
        <input type="email" v-model="email" placeholder="Email address..." />
        <input type="password" v-model="password" placeholder="password..." />
        <button>Login</button>
    </form>
</div>
```

Dans la section script, ajoutez l'importation pour `Auth` et l'objet data pour l'email et le mot de passe. Votre section script devrait ressembler à ceci :

```
<script>
import { Auth } from 'aws-amplify';
export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: ''
    }
  },
}
</script>
```

La dernière chose que nous devons implémenter est la méthode de connexion. Voici le code :

```
async login() {
    try {
        await Auth.signIn(this.email, this.password);
        alert('Successfully logged in');
    } catch (error) {
        alert(error.message);
    }
},
```

Maintenant, si vous ouvrez votre application, vous pourrez vous connecter avec l'utilisateur que vous avez précédemment inscrit.

# Ajouter une méthode de déconnexion

Nous devons ajouter un bouton pour que les utilisateurs puissent se déconnecter de notre application. Ouvrez le fichier `App.vue`. Ajoutez un bouton pour se déconnecter dans la nav. Votre nav devrait ressembler à ceci :

```
<div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/login">Login</router-link> |
    <button @click="logout">Logout</button>
</div>
```

Dans la section script, ajoutez un objet `methods` et incluez la méthode `logout`. Cela devrait ressembler à ceci :

```
methods: {
    async logout() {
        try {
            await Auth.signOut();
        } catch (error) {
            alert(error.message);
        }
    },
},
```

Félicitations, vous avez ajouté avec succès l'authentification AWS Amplify à votre application Vue.

# Obtenir le code

J'ai le [code complet sur mon compte GitHub ici](https://github.com/ratracegrad/Vue-Amplify-Auth-Tutorial).

# Utilisation d'autres méthodes d'authentification

J'ai écrit plusieurs articles de suivi sur l'ajout d'authentification à votre application Vue en utilisant d'autres méthodes d'authentification.

* [Utilisation de Firebase pour l'authentification](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-firebase/)
* [Utilisation d'Auth0 pour l'authentification](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-auth0/)

# Conclusion

AWS Amplify est un excellent outil qui vous permet d'ajouter une authentification à votre application.

J'espère que vous avez apprécié cet article. Merci d'avoir lu.

_Publié à l'origine sur_ [_https://www.jenniferbland.com_](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-auth0/) _le 31 décembre 2020._