---
title: Voici comment authentifier les utilisateurs avec Vue.js et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T18:29:59.000Z'
originalURL: https://freecodecamp.org/news/authentication-with-vue-js-firebase-5c3a82149f66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tMQzjqwzmhLS12xUUgyeKA.png
tags:
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici comment authentifier les utilisateurs avec Vue.js et Firebase
seo_desc: 'By Gareth Redfern

  In this tutorial we will work through building a simple Vue.js app. It will use
  Firebase for authentication and allow users to sign-up. Once signed-up users access
  protected areas of a web application via a sign-in page.

  To keep thi...'
---

Par Gareth Redfern

Dans ce tutoriel, nous allons construire une application Vue.js simple. Elle utilisera Firebase pour l'authentification et permettra aux utilisateurs de s'inscrire. Une fois inscrits, les utilisateurs accèdent aux zones protégées d'une application web via une page de connexion.

Pour garder les choses aussi simples et courtes que possible, on suppose que vous êtes familier avec [Vue.js.](https://vuejs.org/v2/guide/) Vous pouvez démarrer un projet en utilisant le [CLI](https://vuejs.org/v2/guide/installation.html#CLI) et [webpack](https://webpack.js.org/). Nous travaillerons sur deux sujets principaux pour créer notre application :

1. Utiliser [vue-router 2](https://router.vuejs.org/en/) pour charger et protéger les pages de l'application web.
2. Configurer un backend Firebase qui utilise l'[authentification Firebase](https://firebase.google.com/docs/auth/) pour gérer l'inscription et la connexion des utilisateurs.

Les [fichiers du tutoriel](https://github.com/garethredfern/vue-auth-demo) sont téléchargeables gratuitement sur GitHub. Dans la mesure du possible, des commentaires ont été ajoutés pour expliquer ce que fait le code. Pour faire fonctionner le site sur votre machine locale, suivez les instructions du fichier README. Le répertoire principal dans lequel nous écrirons notre code est le [répertoire src.](https://github.com/garethredfern/vue-auth-demo/tree/master/src) Si vous avez déjà construit des applications Vue par le passé, cela devrait vous être familier.

### Architecture de l'application

L'application que nous construisons aura une page d'accueil simple où l'utilisateur navigue pour accéder au site. Il devra s'inscrire pour obtenir un compte via un formulaire d'inscription. Une fois enregistré, une page de connexion permettra à l'utilisateur d'accéder à un tableau de bord (la zone sécurisée du site).

### Gestion des routes et sécurisation des pages

Le premier concept à comprendre est comment envoyer des requêtes de page et sécuriser les pages derrière une connexion. Pour ce faire, nous installerons [vue-router 2](https://router.vuejs.org/en/), une bibliothèque officielle pour la gestion des routes. Pour bien comprendre les routes simples, nous ignorerons d'abord la sécurisation des pages. Configurons la structure du site :

* Accueil (Home)
* Inscription (Sign-up)
* Connexion (Sign-in)
* Tableau de bord (Dashboard - nous sécuriserons cette page par la suite)
* Erreur/404 (page générique)

Il y a deux fichiers principaux à examiner pour acquérir une compréhension de base de ce que fait vue-router. Dans le fichier [main.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js), nous [importons VueRouter](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js#L4) et indiquons à Vue que nous voulons [l'utiliser](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js#L26). Ensuite, nous créons une instance VueRouter et passons les routes que l'application utilisera via un fichier [routes.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/router/routes.js) séparé.

Ici, nous définissons également le mode du routeur ; par défaut, vue-router chargera chaque page avec un hash (#) dans l'URL. Dans les navigateurs modernes, nous pouvons utiliser l'API HTML5 History et supprimer la nécessité d'avoir ce hash dans l'URL.

Il y aurait également une certaine configuration serveur à effectuer pour que cela fonctionne, pour plus d'informations, lisez la [documentation officielle](https://router.vuejs.org/en/essentials/history-mode.html).

```javascript
Vue.use(VueRouter);
```

```javascript
const router = new VueRouter({ routes: routes,  mode: 'history'} );
```

Le fichier [routes.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/router/routes.js) importe tous les composants que vous afficherez sur le site. Il exporte un [tableau de toutes vos routes](https://github.com/garethredfern/vue-auth-demo/blob/master/src/router/routes.js#L12) sous forme d'objets. Chaque objet possède les paires clé-valeur suivantes :

* route name (optionnel)
* path (l'URL vers laquelle l'utilisateur navigue)
* component (le composant Vue à charger)

Pour expliquer un peu plus, jetez un œil au code suivant :

```javascript
{
 path: '/sign-in', // définit l'URL que l'utilisateur visitera
 name: 'signIn', // utilisez ce nom comme raccourci dans vos liens
 component: SignIn // charge le composant SignIn
}
```

Pour chaque route, nous répétons le code ci-dessus et changeons les propriétés pour toutes nos options de route. Ensuite, nous ajouterons les balises d'ouverture et de fermeture `<router-view></router-view>` `[tags t](https://github.com/garethredfern/vue-auth-demo/blob/master/src/App.vue#L5)` au fichier App.js. Celles-ci agissent comme des emplacements réservés, indiquant à Vue où permuter les composants lorsqu'un chemin de route est sélectionné. Une fois cela en place, vous devriez pouvoir naviguer vers chaque URL et le composant correspondant à ce chemin se chargera.

#### Sécuriser les routes

Le vue-router offre un moyen de sécuriser les routes en utilisant des [Navigation Guards](https://router.vuejs.org/en/advanced/navigation-guards.html). Il existe trois niveaux de gardes avec lesquels vous pouvez travailler :

* Gardes globaux (ce que nous utiliserons) : définis une seule fois sur l'instance de route.
* Gardes par route : définis sur chaque route séparément.
* Gardes au sein des composants : définis dans chaque composant.

Vous pourriez choisir n'importe laquelle de ces méthodes, mais par simplicité, nous configurerons le garde pour qu'il s'exécute globalement à chaque chargement de page ; cela a probablement la charge de travail la plus élevée, alors gardez cela à l'esprit. Pour faire fonctionner nos routes sécurisées, nous vérifierons deux choses :

1. La route a-t-elle une propriété meta avec `requiresAuth` défini sur true.
2. L'utilisateur est-il connecté et authentifié via l'authentification Firebase.

Travaillons sur les points ci-dessus pour mieux comprendre ce qui se passe. Le vue-router possède des [champs meta de route](https://router.vuejs.org/en/advanced/meta.html) où vous pouvez ajouter des données à récupérer pour cette route particulière. Nous pouvons l'utiliser pour définir un simple booléen `requiresAuth` pour nos pages protégées :

```javascript
{   
  path: '/dashboard',   
  name: 'dashboard',   
  component: Dashboard,   
  meta: {    
    requiresAuth: true   
  }
},
```

Avec le code ci-dessus en place, nous vérifions si la route nécessite une authentification avant qu'elle ne se charge. Cette vérification utilise le garde de navigation global défini dans le fichier [main.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js).

```javascript
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  if(requiresAuth) {   
    next('/sign-in');
  } else {  
    next();
  }
});
```

Ici, nous appelons la méthode `beforeEach` sur l'instance du routeur. Elle prend 3 arguments expliqués en détail dans la [documentation](https://router.vuejs.org/en/advanced/navigation-guards.html), mais le principal sur lequel se concentrer est l'argument `next`. C'est là que vous dites au routeur quoi faire lorsque la condition `requiresAuth` est vraie.

Dans notre application, nous l'utilisons pour envoyer l'utilisateur vers la page de connexion. Pour accéder aux métadonnées de la route, nous définissons une constante qui prend l'argument `to` (la route vers laquelle nous naviguons). La documentation explique comment vous pouvez accéder aux champs meta que vous avez définis :

> Tous les enregistrements de route mis en correspondance par une route sont exposés sur l'objet `$route` (et également sur les objets de route dans les gardes de navigation) en tant que tableau `$route.matched`. Par conséquent, nous devrons itérer sur `$route.matched` pour vérifier les champs meta dans les enregistrements de route.

Avec le tableau meta à notre disposition, nous pouvons itérer dessus en utilisant une fonction ES6 :

```javascript
const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
```

Nous passons `requiresAuth` dans la conditionnelle. Si `true`, envoyez l'utilisateur vers la page de connexion, si `false`, chargez la page normalement.

Il vaut la peine de prendre le temps de lire la [documentation.](https://router.vuejs.org/en/advanced/navigation-guards.html) Acquérez une bonne compréhension de ce que fait la méthode `beforeEach`. C'est un principe clé pour comprendre les gardes de route. Ensuite, nous passerons à l'utilisation de Firebase pour authentifier l'utilisateur et ajouterons une vérification au garde de route.

### Authentification avec Firebase

Firebase offre un système complet de backend et d'authentification. Il peut être ajouté au front-end de votre application web. Pour cette démo, nous utiliserons son API d'authentification pour permettre aux utilisateurs de s'inscrire et de se connecter. Une fois connectés, les utilisateurs authentifiés peuvent consulter le contenu protégé. La première chose à faire est de créer un compte sur [Firebase](https://firebase.google.com/). Je suggère également de regarder comment débuter avec Firebase Auth.

Une fois que vous avez un compte configuré, vous devrez créer un projet dans Firebase. Plutôt que d'entrer dans les détails ici, vous pouvez lire [la documentation sur Firebase.](https://firebase.google.com/docs/web/setup) Ils fournissent un excellent ensemble d'instructions pour vous aider à démarrer. Notez que vous devrez copier et coller vos paramètres de configuration et les remplacer dans le fichier [main.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js#L10) du projet. Assurez-vous d'activer l'authentification par e-mail et mot de passe comme méthode de connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*i_Dbk3o4Ai6GNuvOfNGnnA.png)

Une fois Firebase configuré et vos paramètres de configuration ajoutés, examinons la dernière partie du processus d'authentification. Ajoutez une deuxième conditionnelle à la méthode `beforeEach` du garde de route que nous avons créée précédemment.

```javascript
router.beforeEach((to, from, next) => {
  const currentUser = Firebase.auth().currentUser;
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !currentUser) {
    next('/sign-in');
  } else if (requiresAuth && currentUser) {
    next();
  } else {
    next();
  }
});
```

Nous avons ajouté une variable `currentUser`, qui renvoie l'utilisateur actuellement connecté depuis Firebase. Si personne n'est connecté, elle renvoie null. Nous pouvons l'utiliser comme deuxième vérification dans notre instruction conditionnelle. Si `requiresAuth` et `currentUser` sont tous deux vrais, la route affichera la page.

Si cette condition n'est pas remplie, l'utilisateur est renvoyé vers une page de connexion. Si la route n'est pas protégée par le tag meta `requiresAuth`, la page est chargée normalement et aucune authentification n'est requise.

#### S'assurer que Firebase est initialisé avant de charger Vue

Nos routes ont été configurées de sorte que si vous êtes déjà connecté, vous soyez redirigé vers la page du tableau de bord. Malheureusement, cela ne se produira pas tel quel. L'exécution du garde de navigation `beforeEach` a lieu avant la fin de l'initialisation de Firebase. C'est un piège important qu'[Anas Mammeri](https://medium.com/@anas.mammeri) explique dans [son article](https://medium.com/@anas.mammeri/vue-2-firebase-how-to-build-a-vue-app-with-firebase-authentication-system-in-15-minutes-fdce6f289c3c).

#### Utiliser Vue pour gérer l'inscription et la connexion

Nous avons besoin que les utilisateurs puissent s'inscrire et se connecter à notre application. Jetez un œil aux deux composants Vue [SignUp.vue](https://github.com/garethredfern/vue-auth-demo/blob/master/src/components/SignUp.vue) et [SignIn.vue.](https://github.com/garethredfern/vue-auth-demo/blob/master/src/components/SignIn.vue) Ils fonctionnent tous deux de manière similaire, en liant les champs d'e-mail et de mot de passe à la propriété data.

L'intégration avec Firebase se produit lorsque la méthode `signUp` ou `signIn` est exécutée. Ces fonctions sont fournies par Firebase. Nous passons l'e-mail et le mot de passe de la propriété data de Vue. En cas de succès, naviguez vers le tableau de bord en utilisant la méthode `replace` de vue-router. Si des erreurs surviennent, une alerte avec le message d'erreur s'affiche.

```javascript
signUp: function() {  
  Firebase.auth()          
    .createUserWithEmailAndPassword(this.email, this.password)          
    .then( user => { this.$router.replace('dashboard'); },          
    error => { alert(error.message); });
}
```

```javascript
signIn: function() {  
  Firebase.auth()          
    .signInWithEmailAndPassword(this.email, this.password)          
    .then( user => { this.$router.replace("dashboard"); },          
    error => { alert(error.message); });
}
```

Si vous chargez le site dans votre navigateur, vous devriez maintenant pouvoir vous inscrire et vous connecter. Tout ce qu'il nous reste à faire est de fournir à l'utilisateur un lien de déconnexion.

#### Permettre aux utilisateurs de se déconnecter

Examinez le composant [Header.vue](https://github.com/garethredfern/vue-auth-demo/blob/master/src/components/Header.vue). Nous pouvons utiliser une méthode `signOut` de Firebase qui se déclenche lorsqu'un utilisateur clique sur le bouton de déconnexion. Ensuite, redirigez-le vers la page de connexion avec la méthode `replace` de vue-router.

```javascript
signOut: function() {  
  Firebase.auth()    
    .signOut()    
    .then(() => {      
      this.$router.replace('sign-in');    
    });
}
```

Chargez le site dans votre navigateur et cliquez sur le bouton de déconnexion. Vous devriez maintenant être redirigé vers la page de connexion.

### Conclusion et apprentissage supplémentaire

Notre application dispose désormais d'une authentification Firebase de base avec quelques principes fondamentaux de vue-router ajoutés. Ensuite, nous devons examiner comment nous gérons l'état de l'utilisateur. L'état aide à afficher le contenu et les liens selon qu'un utilisateur est connecté ou non. Après avoir examiné quelques options, ce serait un bon cas d'utilisation pour [plonger dans Vuex](https://medium.com/@garethredfern/managing-user-state-with-vuex-firebase-77eebc64f546).