---
title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : ajout de l''authentification
  avec Firebase'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T01:13:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-spa-using-vue-js-vuex-vuetify-and-firebase-adding-authentication-with-firebase-d9932d1e4365
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_oxBC3QDl02cB2MDOzGXZg.png
tags:
- name: software development
  slug: software-development
- name: vue
  slug: vue
- name: '#vue-router'
  slug: vue-router
- name: Vue.js
  slug: vuejs
- name: Vuex
  slug: vuex
seo_title: 'Comment créer une SPA avec Vue.js, Vuex, Vuetify et Firebase : ajout de
  l''authentification avec Firebase'
seo_desc: 'By Jennifer Bland

  Part 4: learn how to use Firebase to add authentication and a cart


  Meal Prep application

  Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and
  Firebase.

  This is part four of my four-part series on building...'
---

Par Jennifer Bland

#### Partie 4 : apprendre à utiliser Firebase pour ajouter l'authentification et un panier

![Image](https://cdn-media-1.freecodecamp.org/images/OEAiRGPTXUXg4SP-gqbkQthWuYTwQrThqkdu)
_Application Meal Prep_

Apprenez à créer un site web de livraison de repas en utilisant Vue.js, Vuex, Vue Router et Firebase.

Il s'agit de la quatrième partie de ma série en quatre parties sur la création d'une application Vue. Voici une liste de toutes les parties :

[Partie 1 : Installation de Vue et création d'une SPA utilisant Vuetify et Vue Router](https://medium.com/p/838b40721a07)

[Partie 2 : Utilisation de Vue Router](https://medium.com/p/fc5bd065fe18)

[Partie 3 : Utilisation de Vuex et accès à l'API](https://medium.com/p/f8036aa464ad)

[Partie 4 : Utilisation de Firebase pour l'authentification et le panier](https://medium.com/p/d9932d1e4365)

### Récapitulatif

Dans la première partie de cette série, nous avons créé notre application Vue en utilisant le CLI Vue. Nous avons également ajouté Vuetify à l'application. Nous avons utilisé Vuetify pour styliser notre page d'accueil.

Dans la deuxième partie, nous avons utilisé Vue Router pour ajouter la navigation entre les différentes pages de notre application. Nous avons ajouté des composants pour toutes les pages de notre application.

Dans la troisième partie, nous avons été initiés à Vuex. Nous nous sommes inscrits à une API pour fournir des recettes et avons utilisé axios pour les récupérer. Ces données ont été stockées dans le store Vuex, ce qui les a rendues accessibles à chaque composant de l'application.

### Qu'est-ce que Firebase ?

Firebase est une infrastructure cloud en temps réel pour les applications côté client. Firebase peut transformer toute application _Frontend_ en un produit full-stack capable de s'adapter infiniment dans le cloud. Il abstrait la plupart de vos fonctionnalités complexes côté serveur comme l'authentification des utilisateurs, la persistance des données, le stockage de fichiers et les microservices, afin que vous puissiez vous concentrer sur la création d'une expérience incroyable pour l'utilisateur final.

La première étape consiste à aller sur [firebase et créer un nouveau compte](https://firebase.google.com). Connectez-vous au compte que vous avez créé. Vous verrez ce tableau de bord :

![Image](https://cdn-media-1.freecodecamp.org/images/nh3agjDtQIfZb5NsgLroWojeEEZ0Nm-uI614)
_Démo Firebase_

Cliquez sur le bouton `Ajouter un projet`. Entrez un nom pour votre projet. J'ai entré « meal-prep » pour le nom de mon projet. Cochez toutes les cases. Ensuite, cliquez sur le bouton `créer un projet`.

![Image](https://cdn-media-1.freecodecamp.org/images/33vedZNLJ3WoqpIr7XzQRpXznXO8TOfQHY-Z)
_Boîte de dialogue Ajouter un nouveau projet sur Firebase_

Une fois votre projet créé, Firebase vous amènera à la page d'accueil de votre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/G80ee1kcRa8BJmt-ZjJp7yvrZEzpiply5seN)
_Page d'accueil du projet_

Nous devons intégrer la configuration de notre projet dans notre application meal-prep. Cliquez sur le bouton web pour ajouter Firebase à votre application. (NOTE : si vous n'êtes pas sûr de quel bouton il s'agit, c'est le bouton avec le `<`;/>. Dans l'image ci-dessus, le bouton est juste au-dessus des mots « get started ». Cliquez sur le bouton de copie pour copier le snippet dans votre presse-papiers.

![Image](https://cdn-media-1.freecodecamp.org/images/nstMKziQenAP2sNjXnSyoPGKRNuVdEjTufzq)
_Snippet de configuration Firebase_

Ensuite, nous devons incorporer ce snippet dans notre application de préparation de repas. Vous pouvez initialiser votre application firebase dans le fichier `main.js`. Vous pouvez le faire dans le fichier `App.vue`.

Au lieu de cela, nous allons créer un nouveau répertoire appelé firebase dans le dossier src. À l'intérieur de ce nouveau répertoire, créez un fichier appelé `index.js`. Collez le contenu de votre presse-papiers dans ce fichier. Supprimez les deux lignes avec les balises `script`. Dans la première ligne du fichier, importez firebase. Sur la dernière ligne, initialisez firebase. Votre fichier devrait ressembler à ceci :

```
import firebase from 'firebase';const config = {    apiKey: "<youKeyHere>",    authDomain: "<youKeyHere>",    databaseURL: "<youKeyHere>",    projectId: "<youKeyHere>",    storageBucket: "<youKeyHere>",    messagingSenderId: "<youKeyHere>"};firebase.initializeApp(config);
```

Nous importons firebase depuis un package npm que nous n'avons pas encore installé. Installons-le maintenant. Dans votre terminal, installez firebase avec cette commande :

```
npm install firebase --save
```

Maintenant que nous avons installé firebase et créé un fichier de configuration, nous devons ajouter ce fichier à notre application pour que Vue en soit conscient. Ouvrez le fichier `main.js` et importez le fichier de configuration que nous avons créé. Voici à quoi ressemble mon fichier `main.js` :

```
import '@babel/polyfill';import Vue from 'vue';import './plugins/vuetify';import App from './App.vue';import router from './router';import store from './store';import '@/firebase/';Vue.config.productionTip = false;new Vue({    router,    store,    render: h => h(App)}).$mount('#app');
```

Retournez à votre console firebase dans le navigateur. Cliquez sur `Authentification`. Cliquez sur le bouton `configurer la méthode de connexion`.

![Image](https://cdn-media-1.freecodecamp.org/images/eKoTHvMZxWj28bIBc1vy18y4Q4fnSSypzEjD)
_Configuration de l'authentification dans firebase_

Dans la liste des fournisseurs de connexion, cliquez sur Email/Mot de passe :

![Image](https://cdn-media-1.freecodecamp.org/images/yiS92UoxyI60pQDvGKkmeduz0cqML4qRBPuw)
_Liste des fournisseurs de connexion_

Activez l'option permettant à tous les utilisateurs de s'inscrire en utilisant leur adresse e-mail et leur mot de passe. Ensuite, cliquez sur le bouton `enregistrer`.

![Image](https://cdn-media-1.freecodecamp.org/images/85suaEwdDT71E0k3QbSPegLPeABexqZGJ3ov)
_Activer l'inscription en utilisant l'e-mail et le mot de passe_

#### Création du formulaire d'inscription

Dans un article précédent, nous avons ébauché les fichiers Join.vue et Signin.vue. Ces deux fichiers auront presque le même code. Nous allons créer le formulaire Join en premier. Une fois terminé, nous le copierons/collerons dans le formulaire Signin.

Ouvrez le composant Join.vue. Vous pouvez supprimer tout ce qui se trouve dans le template. Vuetify a une structure de mise en page par défaut pour les composants. Elle se présente comme suit :

* v-container
* v-layout
* v-flex

Alors créons cette mise en page maintenant dans le composant. Le début de notre fichier ressemble à ceci :

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>            </v-flex>        </v-layout>    </v-container></template>
```

Pour le `v-container`, nous ajoutons `fill-height`. Nous ajoutons cela pour centrer le formulaire verticalement dans la fenêtre. Pour le `v-flex`, nous ajoutons les valeurs `xs12`, `sm8` et `md4`. Cela est similaire à la définition de la largeur des colonnes de Bootstrap. Sur les appareils extra-petits, le formulaire occupera toutes les 12 colonnes, ce qui signifie tout l'écran. Sur les appareils petits, le formulaire occupera 3/4 de la largeur de l'écran. Sur les écrans moyens et grands, le formulaire occupera 1/3 de l'écran.

À l'intérieur du `v-flex`, nous allons utiliser un `v-card`. Nous ajoutons `class=elevation-12"` au `v-card` pour qu'il semble flotter au-dessus de la page. Pour le haut du formulaire, nous utiliserons un `v-toolbar`. Nous lui donnons une couleur `primary`. Pour l'installation par défaut de Vuetify, la couleur principale est bleue. Nous voulons que le texte dans la barre d'outils soit en texte blanc au lieu du noir par défaut. Pour rendre le texte blanc, nous ajoutons `dark` au `v-toolbar`.

Ensuite, nous avons un `v-card-text`. À l'intérieur, nous avons un `v-form`. Pour le formulaire, nous lui donnons une référence avec le nom `form`. Nous l'assignons au `v-model` avec une valeur de `valid`.

La dernière chose que nous ajoutons est `lazy-validation`. Notre formulaire doit capturer l'e-mail et le mot de passe de l'utilisateur. Nous utiliserons deux `v-text-field` pour capturer ces valeurs. Pour améliorer l'apparence, j'ai préfixé une icône pour chaque champ. Chaque champ a un `v-model` et des `rules`.

Avant que le formulaire ne soit soumis, le champ sera validé par rapport à toutes les règles définies. S'ils passent, alors vous pouvez soumettre le formulaire. Nous en profiterons lorsque l'utilisateur cliquera sur le bouton Join.

Le dernier élément à ajouter au formulaire est un bouton. Nous ajoutons un `v-card-actions` et ajoutons un bouton. Voici à quoi ressemble le template pour notre composant :

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>                <v-card class="elevation-12">                    <v-toolbar dark color="primary">                        <v-toolbar-title>Join Form</v-toolbar-title>                    </v-toolbar>                    <;v-card-text>                        <v-form ref="form" v-model="valid" lazy-validation>;                            &lt;v-text-field prepend-icon="person" name="email" label="Email" type="email"                                          v-model="email" :rules="emailRules" required>                            </v-text-field>                            <v-text-field prepend-icon="lock" name="password" label="Password" id="password"                                          type="password" required v-model="password" :rules="passwordRules">                            </v-text-field>                        </v-form>                    </v-card-text>                    <v-card-actions>                        <v-spacer></v-spacer>                        <v-btn color="primary" :disabled="!valid" @click="submit">Join</v-btn>                    </v-card-actions>                </v-card>            </v-flex>        </v-layout>    </v-container></template>
```

Nous avons défini plusieurs modèles dans notre template. Nous devons les ajouter à la section `data` de notre script. Dans le script, ajoutez un objet de données. Nous ajouterons valid, email, password, emailRules et passwordRules.

Email et password contiendront les valeurs que l'utilisateur saisit dans les deux champs de texte. Valid indiquera si notre formulaire a passé toutes les règles que nous avons créées. Pour l'email, nous vérifions que le champ n'est pas vide. Nous vérifions également que le contenu correspond à une expression régulière de base pour valider l'adresse e-mail. Pour le mot de passe, nous vérifions que le champ n'est pas vide. Nous vérifions également que le mot de passe contient au moins six caractères.

Voici à quoi ressemble l'objet de données maintenant :

```
data() {    return {        valid: false,        email: '',        password: '',        emailRules: [            v => !!v || 'E-mail is required',            v => /.+@.+/.test(v) || 'E-mail must be valid'        ],        passwordRules: [            v => !!v || 'Password is required',            v =>                v.length >= 6 ||                'Password must be greater than 6 characters'        ]    };},
```

La dernière chose que nous devons ajouter est les méthodes. Dans les méthodes, nous avons `submit()`. Cette méthode va d'abord valider notre formulaire. Si elle passe la validation, elle appellera une action dans notre store Vuex appelée `userJoin`. Nous lui passons l'email et le mot de passe que l'utilisateur a saisis dans le formulaire.

Voici à quoi ressemblent les méthodes :

```
methods: {    submit() {        if (this.$refs.form.validate()) {            this.$store.dispatch('userJoin', {                email: this.email,                password: this.password            });        }    }}
```

#### Création de l'action userJoin dans Vuex

Ouvrez le fichier `store.js`. Nous allons créer une nouvelle action appelée `userJoin`. Par défaut, le premier paramètre passé à cette action est `context`. J'utiliserai la déstructuration d'objet pour obtenir uniquement `commit` de `context`. Commit est la façon dont j'appellerai ma mutation.

J'utiliserai firebase pour créer le nouvel utilisateur dans la base de données firebase. Pour pouvoir utiliser firebase dans le store, je devrais l'importer. En haut du fichier, importez firebase avec cette commande :

```
import firebase from 'firebase';
```

L'authentification Firebase fournit une méthode appelée `createUserWithEmailAndPassword`. Nous passerons l'email et le mot de passe de l'utilisateur à cette méthode. Si elle réussit à enregistrer l'utilisateur, elle retournera un objet utilisateur. Lorsqu'elle réussit, nous appellerons deux mutations : `setUser` et `setIsAuthenticated`. Voici à quoi ressemble l'action :

```
userJoin({ commit }, { email, password }) {    firebase        .auth()        .createUserWithEmailAndPassword(email, password)        .then(user => {            commit('setUser', user);            commit('setIsAuthenticated', true);        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);        });}
```

Cette action appelle deux mutations. Alors créons-les maintenant. Dans les mutations, ajoutez une nouvelle mutation appelée `setUser`. Définissez la valeur d'état de l'utilisateur sur la charge utile. Ensuite, créez une deuxième mutation appelée `setIsAuthenticated`. Définissez la valeur d'état de isAuthenticated sur la charge utile. Voici à quoi ressemblent les deux mutations :

```
setUser(state, payload) {    state.user = payload;},setIsAuthenticated(state, payload) {    state.isAuthenticated = payload;}
```

Dans l'état, nous devons ajouter deux nouvelles valeurs : `user` et `isAuthenticated`. Voici à quoi ressemble l'état maintenant :

```
state: {    recipes: [],    apiUrl: 'https://api.edamam.com/search',    user: null,    isAuthenticated: false},
```

#### Test d'ajout d'un nouvel utilisateur

Démarrez votre serveur avec la commande `npm run serve`. Cliquez sur le bouton `Join` dans la navigation. Entrez votre email et un mot de passe et cliquez sur le bouton join. Lorsque vous cliquez sur le bouton, rien de visible ne se passe. Pour vérifier que l'utilisateur a été enregistré, allez dans la console firebase de votre navigateur. Cliquez sur `Authentification`. Vous devriez voir une liste des utilisateurs qui ont été enregistrés pour votre application. Ici, vous pouvez voir que l'utilisateur que je viens d'enregistrer a été créé.

![Image](https://cdn-media-1.freecodecamp.org/images/vYkETdpPAbqno517wwsXH-g6tHJWZQXcQnrj)
_L'utilisateur a été enregistré_

Nous devons notifier l'utilisateur qu'il a été créé avec succès. Nous le ferons, mais plus tard. D'abord, nous allons copier et coller le contenu du composant Join.vue dans le composant `Signin.vue`. Il n'y a que deux changements que vous devrez apporter dans le template. Changez le titre en « Login Form ». Pour le bouton, faites en sorte que le texte dise « Login ». Dans la méthode submit, faites en sorte qu'elle envoie à `userLogin`. Juste pour être sûr que vous avez tout correctement, voici à quoi ressemble mon fichier Signin.vue complet :

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>                <v-card class="elevation-12">                    <v-toolbar dark color="primary">                        <v-toolbar-title>Login Form</v-toolbar-title>                    </v-toolbar>                    <;v-card-text>                        <v-form ref="form" v-model="valid" lazy-validation>;                            &lt;v-text-field prepend-icon="person" name="email" label="Email" type="email"                                          v-model="email" :rules="emailRules" required>                            </v-text-field>                            <v-text-field prepend-icon="lock" name="password" label="Password" id="password"                                          type="password" required v-model="password" :rules="passwordRules">                            </v-text-field>                        </v-form>                    </v-card-text>                    <v-card-actions>                        <v-spacer></v-spacer>                        <v-btn color="primary" :disabled="!valid" @click="submit">Login</v-btn>                    </v-card-actions>                </v-card&gt;            </v-flex&gt;        </v-layout>    </v-container></template><script>export default {    name: 'Signin',    data() {        return {            valid: false,            email: '',            password: '',            emailRules: [                v => !!v || 'E-mail is required',                v => /.+@.+/.test(v) || 'E-mail must be valid'            ],            passwordRules: [                v => !!v || 'Password is required',                v =&gt;                    v.length >= 6 ||                    'Password must be greater than 6 characters'            ]        };    },    methods: {        submit() {            if (this.$refs.form.validate()) {                this.$store.dispatch('userLogin', {                    email: this.email,                    password: this.password                });            }        }    }};</script><style scoped></style>
```

C'est tout. Vous avez maintenant créé les formulaires Join et Login.

Nous devons créer l'action pour Login. Ouvrez le fichier `store.js`. Créez une nouvelle action appelée userLogin. Nous utiliserons firebase pour connecter l'utilisateur. Firebase fournit une méthode appelée `signInWithEmailAndPassword`. Nous appellerons cette méthode et passerons l'email et le mot de passe de l'utilisateur qu'ils ont saisis dans le formulaire. Si l'utilisateur a saisi correctement son email et son mot de passe, nous appellerons les deux mutations `setUser` et `setIsAuthenticated`. Voici à quoi ressemble l'action `userLogin` :

```
userLogin({ commit }, { email, password }) {    firebase        .auth()        .signInWithEmailAndPassword(email, password)        .then(user => {            commit('setUser', user);            commit('setIsAuthenticated', true);        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);        });},
```

#### Redirection vers le profil

Lorsque l'utilisateur s'inscrit ou se connecte avec succès, nous voulons le rediriger vers son profil. Lorsque nous avons créé notre application initialement, le CLI Vue 3 a créé deux routes pour nous. Ces routes étaient `/` et `/about`. Finalement, le profil contiendra une liste de toutes les recettes que l'utilisateur a commandées depuis la page `menu`. Vous vous souvenez du bouton que nous avons placé en bas de chaque recette ? Ce bouton ajoutera la recette au profil de l'utilisateur et la stockera dans la base de données dans firebase.

Pour rediriger l'utilisateur vers le profil, nous allons d'abord importer le routeur en haut du fichier store.js. Le routeur est importé avec la commande :

```
import router from '@/router';
```

Ensuite, dans les deux actions, nous redirigeons l'utilisateur vers /about s'ils s'inscrivent ou se connectent avec succès. Vous pouvez faire la redirection avec cette commande :

```
router.push('/about');
```

Si l'utilisateur échoue à s'inscrire ou à se connecter avec succès, nous redirigeons l'utilisateur vers la page d'accueil. _(NOTE : dans un scénario parfait, nous fournirons une notification à l'utilisateur expliquant pourquoi l'inscription ou la connexion a échoué)._ Vous pouvez les rediriger vers la page d'accueil avec cette commande :

```
router.push('/');
```

Pour tester la redirection, démarrez votre serveur et cliquez sur le bouton Login. Entrez l'email et le mot de passe que vous avez utilisés lorsque vous avez créé votre compte utilisateur. Cliquez sur le bouton Join. Si tout a fonctionné avec succès, vous devriez être redirigé vers la page About.

#### Mise à jour de la navigation

La navigation comporte des boutons pour `Sign In` et `Join`. Lorsqu'un utilisateur s'inscrit ou se connecte avec succès, nous aimerions masquer ces deux boutons. À leur place, nous voulons afficher un bouton `Logout`.

Ouvrez le composant `AppNavigation`. Nous allons regrouper les deux boutons actuels dans une div. Nous allons supprimer la classe pour masquer les boutons sur les appareils petits et extra-petits. Au lieu de cela, nous placerons cette classe sur la div. Nous ajoutons un `v-if` à la div pour ne l'afficher que si l'utilisateur n'est actuellement pas authentifié. En dessous de la `div`, nous ajouterons un nouveau bouton pour Logout. Ce nouveau bouton aura un style de contour avec une couleur blanche. Lorsque vous cliquez sur ce bouton, il appellera la méthode `logout`. Nous ajoutons un v-else à ce bouton pour l'afficher lorsque l'utilisateur est authentifié.

Ensuite, ajoutez une méthode appelée `logout`. Cette méthode appellera une action dans notre store appelée `userSignOut`.

Nous devons également ajouter une nouvelle propriété calculée appelée `isAuthenticated`. Cette propriété retourne la valeur de isAuthenticated dans l'état de notre store.

Voici à quoi devrait ressembler votre AppNavigation :

```
<template>    <span>        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>            <v-list>                <template v-for="(item, index) in items">                    <v-list-tile :key="index">                        <v-list-tile-content>                            {{item.title}}                        </v-list-tile-content>                    <;/v-list-tile>                    <v-divider :key="`divider-${index}`"></v-divider>                </template>            </v-list>        </v-navigation-drawer>        <v-toolbar app color="brown darken-4" dark>            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>            <v-spacer class="hidden-md-and-up"></v-spacer>            <router-link to="/"&gt;                <v-toolbar-title to="/">{{appTitle}}</v-toolbar-title>;            </router-link>            <;v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>            <v-spacer class="hidden-sm-and-down"></v-spacer>            <;div v-if="!isAuthenticated" class="hidden-sm-and-down">                <v-btn flat to="/sign-in">SIGN IN</v-btn>                <v-btn color="brown lighten-3" to="/join">JOIN</v-btn>            </div>            <v-btn v-else outline color="white" @click="logout">Logout</v-btn>        </v-toolbar>    </span></template><script>export default {    name: 'AppNavigation',    data() {        return {            appTitle: 'Meal Prep',            drawer: false,            items: [{ title: 'Menu' }, { title: 'Sign In' }, { title: 'Join' }]        };    },    computed: {        isAuthenticated() {            return this.$store.getters.isAuthenticated;        }    },    methods: {        logout() {            this.$store.dispatch('userSignOut');        }    }};</script><style scoped>a {    color: white;    text-decoration: none;}</style>
```

Nous devons ajouter le getter et l'action que nous venons de définir. Ouvrez le fichier `store.js`. Créez une nouvelle action appelée `userSignout`. Cette action utilisera firebase.auth() pour déconnecter l'utilisateur. Après avoir déconnecté l'utilisateur, elle définit les variables d'état `user` à null et `isAuthenticated` à false. Voici la méthode `userSignout` dans le store :

```
userSignOut({ commit }) {    firebase        .auth()        .signOut()        .then(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);            router.push('/');        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);            router.push('/');        });}
```

Ensuite, nous devons ajouter une section `getters` à l'objet store. La méthode getters `isAuthenticated` retournera true ou false en fonction de l'authentification de l'utilisateur. Voici à quoi ressemble la section `getters` du store :

```
getters: {    isAuthenticated(state) {        return state.user !== null && state.user !== undefined;    }}
```

### Ajout de recettes à la base de données

Une fois qu'un utilisateur est connecté, il peut cliquer sur n'importe quelle recette pour l'ajouter à son compte. Ses recettes seront affichées dans son profil, qui est la route `/about`. Nous avons besoin d'une base de données pour stocker ces recettes. Allez dans votre console firebase dans le navigateur. Cliquez sur `database` dans le panneau de navigation latéral gauche. Sur l'écran suivant, vous verrez des boutons pour créer une base de données en temps réel ou une base de données cloud firestore. Assurez-vous de créer une nouvelle base de données en temps réel. Dans la boîte de dialogue, assurez-vous de sélectionner `démarrer en mode test`. Ensuite, cliquez sur le bouton `activer`.

![Image](https://cdn-media-1.freecodecamp.org/images/nHYgB0KpSgNkOE49AhvBos0IHr3mWw35ZJQJ)
_Démarrer la base de données en mode test_

Maintenant, nous voulons stocker les recettes de l'utilisateur dans la base de données. Ouvrez le composant MealRecipes. Si un utilisateur essaie de commander une recette et qu'il n'est pas connecté, nous devons le rediriger vers la page de connexion. Alors prenons soin de cela maintenant. Sur le bouton `Order`, ajoutez un @click qui appelle la méthode orderRecipe. Assurez-vous de passer `item` comme argument à la méthode. Votre bouton devrait ressembler à ceci :

```
<v-card-actions>    &lt;v-btn color="green" dark @click="orderRecipe(item)">Order</v-btn></v-card-actions>
```

Avant de créer notre méthode, nous allons créer une valeur calculée pour isAuthenticated. Il s'agit du même code exact que nous avons utilisé dans `AppNavigation` précédemment pour afficher et masquer correctement le bouton de connexion et de déconnexion. Ajoutez un isAuthenticated calculé. Il devrait ressembler à ceci :

```
export default {    name: 'MealRecipes',    computed: {        recipes() {            return this.$store.state.recipes;        },        isAuthenticated() {            return this.$store.getters.isAuthenticated;        }    }};
```

Maintenant, nous sommes prêts à créer notre méthode orderRecipe. Ajoutez cette méthode et son paramètre. Dans cette méthode, nous voulons d'abord vérifier si l'utilisateur est connecté ou non. S'il ne l'est pas, nous voulons le rediriger vers `/sign-in`. S'il est connecté, nous voulons appeler une action dans le store Vuex qui ajoutera la recette au compte utilisateur dans la base de données. Voici à quoi ressemble notre méthode :

```
methods: {    orderRecipe(item) {        if (this.isAuthenticated) {            this.$store.dispatch('addRecipe', item);        } else {            this.$router.push('/sign-in');        }    }}
```

Ouvrez le fichier store.js. Nous devons créer une nouvelle action pour ajouter des recettes. Dans cette action, nous allons utiliser firebase pour ajouter la recette à une base de données appelée `users`. Lorsque l'utilisateur a été enregistré dans firebase, un identifiant utilisateur unique lui a été attribué. Nous utiliserons cet `uid` pour stocker le nom de la recette dans la base de données.

Dans cette action, nous utiliserons `state` pour obtenir la valeur de l'utilisateur actuellement sélectionné. L'`user` dans `state` est un objet. Cet objet a une clé appelée user. Dans cet objet, nous trouverons l'`uid`. Nous l'utilisons pour pousser le titre de la recette sélectionnée dans la base de données. Voici l'action :

```
addRecipe({ state }, payload) {    firebase        .database()        .ref('users')        .child(state.user.user.uid)        .push(payload.recipe.label);}
```

Maintenant, démarrez votre serveur et connectez-vous. Sélectionnez un régime dans la page menu. Ensuite, commandez quelques recettes. Les recettes que vous avez commandées devraient être affichées dans la base de données dans firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/SBJUuIRCRWT2Fu3iAiZeEERyYXPTfeLaSLwt)
_Recettes ajoutées à la base de données_

Maintenant que nous avons ajouté les recettes à la base de données, nous devons en fait les afficher sur la page de profil pour l'utilisateur. Ouvrez le fichier `About.vue`. Chaque fois que cette page est chargée, elle doit récupérer toutes les recettes de l'utilisateur. Pour ce faire, nous ajoutons `mounted()` dans notre script. Cela appellera une méthode appelée `getRecipes`.

Créons cette méthode maintenant. Dans la méthode, nous allons appeler une action dans notre store Vuex qui récupérera toutes les recettes de l'utilisateur. Nous n'avons pas encore créé cette action dans le store, mais en termes simples, cette action récupérera les recettes de l'utilisateur. Ensuite, elle les stockera dans une variable dans `state` appelée `userRecipes`.

Avant de quitter About.vue, ajoutez une propriété calculée pour `userRecipes`. Cela retournera les `userRecipes` de `state` dans notre store. Voici à quoi devrait ressembler le script About.vue :

```
export default {    name: 'About',    computed: {        userRecipes() {            return this.$store.state.userRecipes;        }    },    mounted() {        this.getRecipes();    },    methods: {        getRecipes() {            this.$store.dispatch('getUserRecipes');        }    }};
```

Ensuite, ouvrez votre fichier `store.js`. Nous devons créer l'action `getUserRecipes`. Lorsque l'utilisateur se connecte, nous stockons une variable dans `state` appelée user. Cette variable aura l'ID utilisateur unique attribué à cet utilisateur lorsqu'il a été enregistré dans firebase. Nous voulons obtenir toutes les recettes dans la base de données des utilisateurs qui ont cet ID utilisateur. Une fois que nous avons toutes les recettes, nous voulons définir userRecipes pour les contenir. Voici l'action getUserRecipes :

```
getUserRecipes({ state, commit }) {    return firebase        .database()        .ref('users/' + state.user.user.uid)        .once('value', snapshot => {            commit('setUserRecipes', snapshot.val());        });}
```

Dans nos mutations, nous devons ajouter un `setUserRecipes`. Il ressemble à ceci :

```
setUserRecipes(state, payload) {    state.userRecipes = payload;}
```

Nous devons également ajouter un `userRecipes` dans `state`. Nous définissons sa valeur initiale à un tableau vide. Voici mon objet state complet :

```
state: {    recipes: [],    apiUrl: 'https://api.edamam.com/search',    user: null,    isAuthenticated: false,    userRecipes: []},
```

Maintenant que nous obtenons les recettes, nous devons les afficher sur la page pour l'utilisateur. Alors retournez à votre fichier `About.vue`. Dans le template, nous allons parcourir toutes les recettes de l'utilisateur et les afficher. Je vais vous montrer mon code pour le template d'abord, puis expliquer ce que j'ai fait :

```
<template>    <v-container >        <v-layout column>;            <h1 class="title my-3">My Recipes</h1>            <div v-for="(item, idx) in userRecipes" class="subheading mb-2" :key="idx">                {{item}}            </div>        </v-layout>    </v-container></template>
```

J'ai défini la mise en page pour qu'elle soit `column`. Je l'ai fait parce que je veux que chaque recette soit listée sur la page. Pour rendre les choses plus claires, j'ai ajouté un titre. J'ai ajouté my-3 pour ajouter une marge supérieure et inférieure afin qu'il y ait un espacement entre le titre et la liste des recettes. Ensuite, j'ai parcouru chaque recette et je l'ai affichée. Voici ce que l'utilisateur voit s'il a des recettes :

![Image](https://cdn-media-1.freecodecamp.org/images/AXzGqeL9LhTRcYHIFkQgEjQwRAW4UFRP4Enr)
_Liste de mes recettes_

C'est super, mais si un utilisateur se connecte et n'a pas de recettes ? Ils voient le titre « My Recipes » et une page blanche. Ce n'est pas un design convivial. Alors changeons-le pour afficher quelque chose de plus convivial.

Nous allons afficher un bouton qui emmènera l'utilisateur à la page `menu`. Dans notre template, nous ajouterons ce bouton. Pour faire rediriger le bouton vers la page menu, nous pouvons ajouter `to=/menu` au bouton. Voici mon template final pour le composant `About.vue`.

```
<template>    <v-container >        <v-layout column>;            <h1 class="title my-3">My Recipes</h1>            <div v-for="(item, idx) in userRecipes" class="subheading mb-2" :key="idx">                {{item}}            </div>            &lt;v-flex mt-4>                <v-btn color="primary" to="/menu">Go To Menu</v-btn>            </v-flex>        </v-layout>    </v-container></template>
```

#### Affichage du profil dans la navigation

La dernière chose que nous devons ajouter est la possibilité d'afficher un lien vers le profil dans la navigation. Tout comme le bouton de déconnexion, cela ne doit être affiché que si l'utilisateur est authentifié.

Ouvrez les composants AppNavigation. Nous allons regrouper le bouton de profil et le bouton de déconnexion dans une div. C'est la même chose que nous avons faite précédemment pour les boutons `Sign In` et `Join`. Ajoutez une div et déplacez le bouton de déconnexion pour qu'il soit à l'intérieur de cette div. Ajoutez un autre bouton pour `profile`. Ce bouton sera plat, tout comme le bouton `Sign In`.

Voici à quoi ressemble mon AppNavigation maintenant :

```
<template>    <span>        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>            <v-list>                <template v-for="(item, index) in items">                    <v-list-tile :key="index">                        <v-list-tile-content>                            {{item.title}}                        </v-list-tile-content>                    <;/v-list-tile>                    <v-divider :key="`divider-${index}`"></v-divider>                </template>            </v-list>        </v-navigation-drawer>        <v-toolbar app color="brown darken-4" dark>            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>            <v-spacer class="hidden-md-and-up"></v-spacer>            <router-link to="/"&gt;                <v-toolbar-title to="/">{{appTitle}}</v-toolbar-title>;            </router-link>            <;v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>            <v-spacer class="hidden-sm-and-down"></v-spacer>            <;div v-if="!isAuthenticated" class="hidden-sm-and-down"&gt;                <v-btn flat to="/sign-in">SIGN IN</v-btn>                <v-btn color="brown lighten-3" to="/join">JOIN</v-btn>            </div>            <div v-else>                <v-btn flat to="/about">PROFILE</v-btn>                <v-btn outline color="white" @click="logout">Logout</v-btn>            </div>        </v-toolbar>    </span></template>
```

### Ajout de gardes de route

Actuellement, l'utilisateur peut naviguer vers la page de profil en la tapant dans l'URL du navigateur. Nous ne voulons pas permettre aux utilisateurs de faire cela s'ils ne sont pas connectés. Vue Router fournit la possibilité d'ajouter des gardes de route avant de naviguer vers une URL. Nous voulons tester si un utilisateur est authentifié avant de lui permettre de rediriger vers la page `/about`.

Ouvrez le fichier `router.js`. Les gardes de route fonctionnent en conjonction avec les balises meta. Trouvez la route `/about`. Nous allons ajouter une balise meta `authRequired`. La route devrait ressembler à ceci :

```
{    path: '/about',    name: 'about',    component: () =&gt; import('./views/About.vue'),    meta: {        authRequired: true    }},
```

Les gardes de route sont vérifiés dans une méthode appelée beforeEach qui fait partie de Vue Router. Cette méthode reçoit trois paramètres :

* la route vers laquelle vous allez
* la route d'où vous venez
* une méthode next qui continue avec la route actuelle

Notre méthode beforeEach vérifiera chaque route vers laquelle nous allons pour voir si elle contient la balise meta authRequired. Si c'est le cas, elle vérifiera si l'utilisateur est authentifié. Si l'utilisateur n'est pas authentifié, il sera redirigé vers la page `/sign-in`. Si l'utilisateur est connecté, la route sera autorisée à se poursuivre. Si un utilisateur accède à une page qui n'a pas la balise meta authRequired, la route se poursuivra.

Voici la méthode que j'ai ajoutée à mon routeur pour effectuer cette vérification :

```
router.beforeEach((to, from, next) => {    if (to.matched.some(record => record.meta.authRequired)) {        if (!store.state.user) {            next({                path: '/sign-in'            });        } else {            next();        }    } else {        next();    }});
```

### Obtenez le code

Bien que ce soit une série en 4 parties, vous pouvez obtenir le [code finalisé dans mon compte GitHub.](https://github.com/ratracegrad/meal-prep) Aidez-moi et **étoilez le dépôt** lorsque vous obtenez le code.

### Résumé

Dans cette partie de la série, vous avez appris :

* Qu'est-ce que Firebase
* Utilisation de Firebase pour authentifier les utilisateurs qui se connectent avec un email et un mot de passe
* Utilisation de Firebase pour stocker les recettes qu'un utilisateur a commandées
* Utilisation de gardes de route pour empêcher les utilisateurs d'accéder aux pages s'ils ne sont pas authentifiés
* Affichage de la liste des recettes de l'utilisateur depuis la base de données sur Firebase

Si vous avez aimé cet article, applaudissez-le. Si vous pensez que quelqu'un d'autre pourrait bénéficier de cet article, partagez-le avec lui.

Si vous avez des questions ou trouvez quelque chose qui ne va pas avec le code, laissez un commentaire. Si vous avez d'autres sujets que vous aimeriez que j'aborde, laissez un commentaire.

#### Autres articles

Voici d'autres articles que j'ai écrits et que vous pourriez vouloir lire.

[**Comment ajouter l'internationalisation à une application Vue**](https://medium.freecodecamp.org/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b)  
[_Hola! Bonjour. Ciao. 4f60597d. Voici comment vous ajoutez l'internationalisation à Vue._medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b)[**Patterns d'instanciation en JavaScript**](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)  
[_Les patterns d'instanciation sont des moyens de créer quelque chose en JavaScript. JavaScript fournit quatre méthodes différentes pour créer2026_medium.com](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)[**Voici 5 mises en page que vous pouvez faire avec FlexBox**](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)  
[_La mise en page flexible CSS 2014 Flexbox 2014 fournit une solution simple aux problèmes de conception et de mise en page que les concepteurs et2026_hackernoon.com](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)

[**Suivez-moi sur Twitter !**](https://twitter.com/ratracegrad)