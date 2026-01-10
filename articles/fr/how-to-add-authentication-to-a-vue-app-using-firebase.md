---
title: Comment ajouter l'authentification à une application Vue en utilisant Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-11T15:36:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/0_zPahR_9e795a1Vpp-1.jpeg
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: vue
  slug: vue
seo_title: Comment ajouter l'authentification à une application Vue en utilisant Firebase
seo_desc: 'By Jennifer Bland

  Firebase provides a very simple and quick way to add authentication to your Vue.js
  application. In this article I will show you how easy it is to allow users to register
  with your application using their email and password.

  What we ...'
---

Par Jennifer Bland

Firebase fournit un moyen très simple et rapide d'ajouter l'authentification à votre application Vue.js. Dans cet article, je vais vous montrer à quel point il est facile de permettre aux utilisateurs de s'inscrire à votre application en utilisant leur email et leur mot de passe.

# Ce que nous allons créer

Nous allons créer une application Vue très simple en utilisant le Vue CLI. Nous allons modifier l'application échafaudée par défaut afin qu'elle fournisse un formulaire pour s'inscrire en tant que nouvel utilisateur, une page de connexion et une page de tableau de bord uniquement visible pour les personnes connectées.

Les utilisateurs pourront s'inscrire à l'application en utilisant le système d'authentification par email et mot de passe de Firebase. Une fois qu'ils se sont inscrits et connectés, ils seront présentés avec la page du tableau de bord.

# Comment créer notre projet

J'utiliserai le Vue CLI pour échafauder un projet pour commencer. Pour cela, vous devez avoir le Vue CLI installé sur votre système. Si vous ne l'avez **PAS** installé, vous pouvez l'installer globalement avec cette commande :

```
npm install -g @vue/cli
```

Maintenant, nous pouvons utiliser le Vue CLI pour créer notre projet. Créez un nouveau projet en utilisant cette commande :

```
vue create vue-firebase-auth-tutorial
```

On vous demandera de choisir un préréglage. Choisissez « Sélectionner manuellement les fonctionnalités » et sélectionnez « babel », « Router » et « Linter / Formatter ».

On vous demandera si vous souhaitez utiliser le mode historique pour le routeur. Choisissez « Oui » (devrait être la valeur par défaut).

Vous pouvez sélectionner n'importe quel linter que vous souhaitez, mais pour ce tutoriel, je sélectionnerai « Eslint + Prettier ».

Une fois que le Vue CLI a terminé, il vous donnera les commandes pour changer de répertoire dans le nouveau répertoire qui vient d'être créé et la commande pour démarrer le serveur. Suivez ces instructions.

Une fois le serveur démarré, vous pouvez ouvrir votre navigateur à l'adresse `localhost:8080`. Vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/vueapp.png)

# Firebase

Pour ce tutoriel, je suppose que vous avez déjà créé un compte avec Firebase. Si ce n'est pas le cas, vous devez le faire avant de continuer.

Nous utiliserons le SDK Firebase dans notre application pour fournir la fonctionnalité d'authentification. Vous pouvez installer Firebase dans votre application en utilisant cette commande :

```
npm install firebase
```

# Comment créer le projet dans Firebase

L'étape suivante consiste à ajouter un projet dans votre console Firebase. Connectez-vous à votre console Firebase. Cliquez sur le bouton pour ajouter un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/addProject.png)

Si vous souhaitez ajouter Google Analytics à votre projet, vous pouvez le faire, mais je ne l'ajouterai pas pour ce tutoriel. Cliquez sur le bouton « Créer un projet ».

Une fois que Firebase a créé votre nouveau projet, vous devrez ajouter Firebase à votre application. Cliquez sur l'icône web.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/addFirebase.png)

On vous demandera d'entrer un surnom pour votre application. J'ai entré un surnom « Vue Firebase Auth Tutorial ». Après avoir entré votre surnom, cliquez sur le bouton « Enregistrer l'application ».

![Image](https://www.freecodecamp.org/news/content/images/2021/01/registerApp.png)

Pour l'étape 2, il vous fournira des instructions sur l'ajout du SDK Firebase à votre application. Nous devons uniquement copier la configuration Firebase et la ligne pour initialiser l'application.

Ouvrez votre fichier **main.js**. Nous allons initialiser Firebase dans notre application Vue. Sous les lignes d'importation existantes, collez la configuration Firebase et la ligne pour initialiser l'application. Vous devrez ajouter une importation pour Firebase. Votre fichier **main.js** devrait ressembler à ceci :

```
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import firebase from "firebase";

var firebaseConfig = {
  apiKey: "VotreConfigIci",
  authDomain: "VotreConfigIci",
  projectId: "VotreConfigIci",
  storageBucket: "VotreConfigIci",
  messagingSenderId: "VotreConfigIci",
  appId: "VotreConfigIci"
};
// Initialiser Firebase
firebase.initializeApp(firebaseConfig);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
```

# Comment définir la méthode d'authentification

Ouvrez votre console Firebase dans votre navigateur. À partir de la console, trouvez le projet que vous venez de créer et cliquez dessus.

Dans le haut de la navigation de gauche, cliquez sur Authentification.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_kYC_j73ZH7guuLxQ.png)

Cliquez sur le bouton « Commencer ».

À partir du menu Authentification, cliquez sur l'onglet « Méthode de connexion ».

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_eFqUqK5d8_jt6O_v.png)

Survolez la première entrée « Email/Mot de passe ». Cliquez sur l'icône du crayon pour ouvrir une boîte de dialogue. Sélectionnez activer.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_3z3Aj1_Sut_C5WHg.png)

Cliquez sur le bouton « Enregistrer ». Vous avez maintenant ajouté la possibilité de créer et d'authentifier des utilisateurs en utilisant leur adresse email et un mot de passe.

# Comment ajouter de nouveaux composants

Lorsque nous avons créé notre application avec Vue Router, il a automatiquement créé deux routes pour notre application — **Accueil** et **À propos**. Nous utiliserons **Accueil** comme la page de connexion de notre application. Nous utiliserons **À propos** comme la page pour s'inscrire en tant que nouvel utilisateur pour notre application.

Lorsque qu'un utilisateur inscrit se connecte à notre application, nous voulons lui montrer la page du tableau de bord. Nous voulons également fournir un moyen pour qu'un utilisateur se déconnecte de notre application. Actuellement, aucune de ces options n'est disponible dans notre application, alors ajoutons-les maintenant.

Ouvrez le fichier **App.vue**. Actuellement, la barre de navigation a deux entrées pour **Accueil** et **À propos**. Nous allons changer **À propos** pour qu'il soit **Inscription** et ajouter deux nouvelles entrées pour **Tableau de bord** et **Déconnexion**. Mettez à jour votre barre de navigation pour qu'elle ressemble à ceci :

```
<div id="nav">
  <router-link to="/">Accueil</router-link> |
  <router-link to="/inscription">Inscription</router-link> |
  <router-link to="/tableau-de-bord">Tableau de bord</router-link> |
  <button @click="deconnexion">Déconnexion</button>
</div>
```

Lorsque vous cliquez sur le bouton de déconnexion, il appelle la méthode de déconnexion. Nous la définirons plus tard.

# Comment créer notre composant de connexion

Ouvrez le fichier **Home.vue** dans le dossier des vues. Supprimez tout le code HTML dans la section template. Remplacez-le par ce code qui fournit un formulaire de connexion très basique. Voici le code :

```
<div>   
  <form @submit.prevent="connexion">     
    <h2>Connexion</h2>     
    <input       
      type="email"       
      placeholder="Adresse email..."       
      v-model="email"     
    />     
    <input       
      type="password"       
      placeholder="Mot de passe..."       
      v-model="motDePasse"     
    />     
    <button type="submit">
       Connexion
    </button>   
  </form> 
</div>
```

Maintenant, si vous regardez notre application, vous verrez le formulaire de connexion sur la page d'accueil comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_WZxgr8K-wj5VSgpg.png)

Notre formulaire est un peu encombré avec les champs de saisie et le bouton qui se touchent. Nous pouvons changer cela en ajoutant un peu de style CSS. Nous pouvons ajouter le style CSS dans le fichier **Home.vue**.

Puisque nous allons utiliser ce même formulaire pour inscrire un utilisateur, nous devrions dupliquer le même style CSS dans ce composant. Au lieu de cela, nous pouvons mettre le style dans le fichier **App.vue** et il stylisera à la fois nos formulaires de connexion et d'inscription.

Ouvrez le fichier **App.vue**. Dans le style, ajoutez ceci :

```
input {   
  margin-right: 20px; 
}
```

Maintenant, notre formulaire de connexion a meilleure apparence.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_bM6cZIRgjfNfrvqd.png)

# Comment créer notre formulaire d'inscription

Ouvrez le fichier **About.vue** dans le dossier des vues. Vous pouvez copier le code HTML du fichier **Home.vue** et le coller dans ce fichier. Changez chaque référence de **Connexion** en **Inscription**. Votre fichier **About.vue** devrait ressembler à ceci :

```
<div>
  <form @submit.prevent="inscription">
    <h2>Inscription</h2>
    <input
      type="email"
      placeholder="Adresse email..."
      v-model="email"
    />
    <input
      type="password"
      placeholder="Mot de passe..."
      v-model="motDePasse"
    />
    <button type="submit">Inscription</button>
  </form>
</div>
```

# Comment mettre à jour nos routes

Actuellement, l'URL pour afficher notre page d'inscription est **/about**. Changeons cela pour qu'elle soit **/inscription**. Ouvrez le fichier **index.js** dans le dossier du routeur. Changez la deuxième route pour **/about** en **/inscription**. Votre tableau de routes devrait ressembler à ceci :

```
const routes = [
    {
        path: '/',
        name: 'Accueil',
        component: Accueil,
    },
    {
        path: '/inscription',
        name: 'Inscription',
        component: () =>
            import(/* webpackChunkName: "about" */ '../views/About.vue'),
    },
];
```

Pendant que nous sommes dans ce fichier, ajoutons une entrée pour afficher notre composant de tableau de bord. Ajoutez une 3ème route pour afficher **/tableau-de-bord**. Votre tableau de routes devrait maintenant ressembler à ceci :

```
const routes = [
    {
        path: '/',
        name: 'Accueil',
        component: Accueil,
    },
    {
        path: '/inscription',
        name: 'Inscription',
        component: () =>
            import(/* webpackChunkName: "about" */ '../views/About.vue'),
    },
    {
        path: '/tableau-de-bord',
        name: 'TableauDeBord',
        component: () =>
            import(/* webpackChunkName: "dashboard" */ '../views/TableauDeBord.vue'),
    },
];
```

# Comment créer le composant Tableau de bord

Créez un nouveau fichier appelé **TableauDeBord.vue** dans le dossier des vues. Cette page ne devrait être visible que pour les utilisateurs qui se sont connectés à notre application.

Dans la section template, ajoutez le code HTML suivant qui indique cela.

```
<div>
  <h2>Tableau de bord</h2>
  <p>Cette page n'est visible que pour les utilisateurs actuellement connectés</p>
</div>
```

# Comment inscrire les utilisateurs

Plus tôt, lorsque nous avons mis à jour le fichier **About.vue** pour inscrire les utilisateurs, nous avions un appel à une méthode appelée **Inscription**. Nous devons ajouter la fonctionnalité pour inscrire de nouveaux utilisateurs.

Tout d'abord, consultons la [documentation Firebase sur la création d'un compte basé sur un mot de passe](https://firebase.google.com/docs/auth/web/password-auth). Firebase Auth dispose d'une méthode appelée **createUserWithEmailAndPassword**. Vous devez passer l'email et le mot de passe de l'utilisateur. Cette méthode inscrira soit l'utilisateur et retournera un objet utilisateur, soit elle retournera un message d'erreur. Implémentons cette méthode maintenant.

Ouvrez le fichier **About.vue**. Nous devons ajouter l'email et le mot de passe à notre objet de données. Dans votre section script, ajoutez l'objet de données suivant :

```
data() { 
  return { 
    email: '', 
    motDePasse: '', 
  }; 
},
```

Ensuite, ajoutez un objet de méthodes avec une méthode appelée **inscription**. Nous pouvons littéralement copier l'exemple de la documentation Firebase pour cette méthode. Nous devons apporter les modifications suivantes au code de la documentation :

* Nous n'utiliserons pas l'objet utilisateur
* Afficher une alerte si la connexion échoue
* Si l'utilisateur est inscrit, le rediriger vers la page de connexion

Voici le code pour la méthode d'inscription :

```
methods: {
  inscription() {
    firebase
      .auth()
      .createUserWithEmailAndPassword(this.email, this.motDePasse)
      .then(() => {
        alert('Inscription réussie ! Veuillez vous connecter.');
        this.$router.push('/');
      })
      .catch(error => {
        alert(error.message);
      });
  },
},
```

Testons l'inscription de notre premier utilisateur pour notre application. Cliquez sur **Inscription** dans la navigation. Entrez une adresse email et un mot de passe et cliquez sur le bouton **Inscription**.

Si l'utilisateur a été inscrit avec succès, vous devriez recevoir une alerte et être redirigé vers la page de connexion.

Si l'inscription échoue, vous devriez recevoir une alerte avec un message d'erreur.

Pour vérifier si l'utilisateur a été inscrit avec succès, allez dans votre console Firebase et cliquez sur votre projet. Dans la navigation de gauche, cliquez sur **Authentification**. Ensuite, cliquez sur l'onglet **Utilisateurs**. Vous verrez votre utilisateur listé :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/0_zBdB2l8pNamJpc-h.png)

Maintenant que nous avons implémenté avec succès l'inscription de nouveaux utilisateurs pour notre application, nous devons implémenter la possibilité pour les utilisateurs de se connecter.

# Comment connecter les utilisateurs

Nous avons utilisé le code fourni par Firebase pour inscrire un nouvel utilisateur. Sur la [page de documentation Firebase](https://firebase.google.com/docs/auth/web/password-auth), elle fournit un exemple de code pour connecter un utilisateur avec une adresse email et un mot de passe. La méthode d'authentification Firebase que nous utiliserons est **signInWithEmailAndPassword**.

Comme pour l'inscription, nous apporterons les mêmes modifications à l'exemple de code. Nous alerterons l'utilisateur s'il est connecté avec succès et le redirigerons vers la page **Tableau de bord**.

Si la connexion échoue, nous affichons une alerte avec un message d'erreur.

Voici la méthode **connexion** que vous devriez avoir dans votre fichier **Home.vue**.

```
methods: {
  connexion() {
    firebase
      .auth()
      .signInWithEmailAndPassword(this.email, this.motDePasse)
      .then(() => {
        alert('Connexion réussie');
        this.$router.push('/tableau-de-bord');
      })
      .catch(error => {
        alert(error.message);
      });
  },
},
```

# Comment créer une garde de route

Nous ne voulons pas que les utilisateurs puissent naviguer vers **/tableau-de-bord** à moins qu'ils ne soient connectés. Nous pouvons faire cela en ajoutant une garde de route pour /tableau-de-bord.

Ouvrez le fichier **index.js** dans le dossier du routeur. Nous allons ajouter une clé meta à la route **/tableau-de-bord** qui indiquera que l'authentification est requise. Voici la route mise à jour :

```
{
  path: '/tableau-de-bord',
  name: 'TableauDeBord',
  component: () =>
    import(/* webpackChunkName: "dashboard" */ '../views/TableauDeBord.vue'),
  meta: {
    authRequired: true,
  },
},
```

Avant que Vue Router ne traite une route, il dispose d'une méthode appelée **beforeEach**. Nous pouvons vérifier si la route nécessite une authentification en vérifiant la valeur meta.

Si l'authentification est requise, nous devons pouvoir vérifier si l'utilisateur est connecté ou non. Heureusement, il existe un objet **currentUser** dans Firebase Auth. Nous l'utiliserons pour vérifier si l'utilisateur est connecté ou non.

S'ils sont actuellement connectés, nous afficherons la page **Tableau de bord**.

Sinon, nous afficherons une alerte indiquant à l'utilisateur qu'il doit être connecté et le redirigerons vers la page **Accueil** pour qu'il se connecte.

Voici le code :

```
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
    if (firebase.auth().currentUser) {
      next();
    } else {
      alert('Vous devez être connecté pour voir cette page');
      next({
        path: '/',
      });
    }
  } else {
    next();
  }
});
```

# Comment déconnecter les utilisateurs

La dernière chose que nous devons ajouter à notre application est la méthode de déconnexion. Firebase Auth fournit une méthode signOut que nous utiliserons.

Ouvrez le fichier **App.vue**. Nous allons déconnecter l'utilisateur. S'il réussit, il recevra une alerte et sera redirigé vers la page **Accueil**.

Si la déconnexion échoue, nous affichons une alerte avec le message d'erreur et le redirigeons vers la page **Accueil**.

Ajoutez ce code pour la méthode **deconnexion** :

```
methods: {
  deconnexion() {
    firebase
      .auth()
      .signOut()
      .then(() => {
        alert('Déconnexion réussie');
        this.$router.push('/');
      })
      .catch(error => {
        alert(error.message);
        this.$router.push('/');
      });
  },
},
```

Dans le code ci-dessus, nous utilisons Firebase mais nous n'avons aucune référence à celui-ci dans notre fichier index.js. Nous devons l'ajouter. Faites défiler vers le haut du fichier où se trouvent les lignes d'importation existantes. Ajoutez cette ligne :

```
import firebase from 'firebase';
```

Maintenant, avec cela ajouté, vous pouvez pratiquer l'inscription d'un nouvel utilisateur. Ensuite, connectez-vous avec cet utilisateur et vérifiez que vous êtes redirigé vers la page **Tableau de bord**. Ensuite, déconnectez-vous et vérifiez que vous êtes redirigé vers la page **Accueil**.

Félicitations — vous avez ajouté avec succès l'authentification Firebase à votre application Vue !

# Obtenez le code

J'ai le [code complet dans mon compte GitHub ici](https://github.com/ratracegrad/Vue-Firebase-Auth-Tutorial). Si vous obtenez le code, faites-moi plaisir et étoilez mon dépôt. Merci !

# Utilisation d'autres méthodes d'authentification

J'ai écrit plusieurs articles de suivi sur l'ajout d'authentification à votre application Vue en utilisant d'autres méthodes d'authentification.

Si vous souhaitez utiliser Auth0 pour l'authentification, [lisez cet article](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-auth0/).

Si vous souhaitez utiliser AWS Amplify pour l'authentification, [lisez cet article](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify/).

# Conclusion

Firebase est une méthode très efficace pour ajouter l'authentification à vos applications Vue. Il vous permet d'ajouter l'authentification sans avoir à écrire votre propre service Backend et à implémenter l'authentification vous-même.

J'espère que vous avez apprécié cet article. Si vous l'aimez, partagez-le. Merci d'avoir lu.

_Publié à l'origine sur_ [_https://www.jenniferbland.com_](https://www.jenniferbland.com/how-to-add-authentication-to-a-vue-app-using-firebase/) _le 28 décembre 2020._

## Jennifer Bland

#### Ingénieure logicielle. Experte Google Developers. Conférencière principale. Entrepreneure. Alpiniste. Fan de Neil Diamond. Voyageuse du monde. [jenniferbland.com](http://jenniferbland.com/) & [codeprep.io](http://codeprep.io/)

#### 57