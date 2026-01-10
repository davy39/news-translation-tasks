---
title: 'How to build a SPA using Vue.js, Vuex, Vuetify, and Firebase: adding authentication
  with Firebase'
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
seo_title: null
seo_desc: 'By Jennifer Bland

  Part 4: learn how to use Firebase to add authentication and a cart


  Meal Prep application

  Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and
  Firebase.

  This is part four of my four-part series on building...'
---

By Jennifer Bland

#### Part 4: learn how to use Firebase to add authentication and a cart

![Image](https://cdn-media-1.freecodecamp.org/images/OEAiRGPTXUXg4SP-gqbkQthWuYTwQrThqkdu)
_Meal Prep application_

Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and Firebase.

This is part four of my four-part series on building a Vue application. Here is a list of all the parts:

[Part 1: Installing Vue and Building an SPA using Vuetify and Vue Router](https://medium.com/p/838b40721a07)

[Part 2: Using Vue Router](https://medium.com/p/fc5bd065fe18)

[Part 3: Using Vuex and accessing API](https://medium.com/p/f8036aa464ad)

[Part 4: Using Firebase for Authentication & Cart](https://medium.com/p/d9932d1e4365)

### Recap

In the first part of this series, we created our Vue application using the Vue CLI. Also, we added Vuetify to the app. We used Vuetify to style our home page.

In the second part, we used Vue Router to add navigation between the different pages of our app. We added components for all the pages in our application.

In the third part, we were introduced to Vuex. We signed up for an API to provide recipes and used axios to retrieve them. This data was stored in the Vuex store which made it accessible to every component in the application.

### What is Firebase?

Firebase is a real-time cloud infrastructure for client-side apps. Firebase can turn any _Frontend_ application into a full-stack product capable of scaling infinitely in the cloud. It abstracts away most of your complex server-side features like user authentication, data persistence, file storage, and microservices, so you can focus on building an awesome experience for the end user.

The first step is to go to [firebase and create a new account](https://firebase.google.com). Log in to the account that you created. You will see this dashboard:

![Image](https://cdn-media-1.freecodecamp.org/images/nh3agjDtQIfZb5NsgLroWojeEEZ0Nm-uI614)
_Firebase Demo_

Click the `Add Project` button. Enter a name for your project. I entered “meal-prep” for the name of my project. Check all checkboxes. Then click the `create project` button.

![Image](https://cdn-media-1.freecodecamp.org/images/33vedZNLJ3WoqpIr7XzQRpXznXO8TOfQHY-Z)
_Add new project dialog on Firebase_

Once your project is created, Firebase will take you to your project’s home page.

![Image](https://cdn-media-1.freecodecamp.org/images/G80ee1kcRa8BJmt-ZjJp7yvrZEzpiply5seN)
_Project Home Page_

We need to integrate our project’s configuration into our meal-prep application. Click on the web button to add Firebase to your application. (NOTE: if you are not sure which button that is, it is the button with the `<`;/>. In the image above, the button is right above the words “get started.” Click the copy button to copy the snippet to your clipboard.

![Image](https://cdn-media-1.freecodecamp.org/images/nstMKziQenAP2sNjXnSyoPGKRNuVdEjTufzq)
_Firebase config snippet_

Next, we need to incorporate this snippet into our meal prep application. You can initialize your firebase application in the `main.js` file. You can do it in the `App.vue` file.

Instead, we are going to create a new directory called firebase in the src folder. Inside this new directory create a file called `index.js`. Paste the contents of your clipboard into this file. Remove the two lines with the `script` tags. In the first line of the file import firebase. On the last line initialize firebase. Your file should look like this:

```
import firebase from 'firebase';const config = {    apiKey: "<youKeyHere>",    authDomain: "<youKeyHere>",    databaseURL: "<youKeyHere>",    projectId: "<youKeyHere>",    storageBucket: "<youKeyHere>",    messagingSenderId: "<youKeyHere>"};firebase.initializeApp(config);
```

We are importing firebase from an npm package that we have not installed yet. Let’s install it now. In your terminal, install firebase with this command:

```
npm install firebase --save
```

Now that we have installed firebase and created a config file, we need to add this file to our application so Vue is aware of it. Open up the `main.js` file and import in the config file we created. Here is what my `main.js` file looks like:

```
import '@babel/polyfill';import Vue from 'vue';import './plugins/vuetify';import App from './App.vue';import router from './router';import store from './store';import '@/firebase/';Vue.config.productionTip = false;new Vue({    router,    store,    render: h => h(App)}).$mount('#app');
```

Go back to your firebase console in the browser. Click on `Authentication`. Click on the `set up sign-in method` button.

![Image](https://cdn-media-1.freecodecamp.org/images/eKoTHvMZxWj28bIBc1vy18y4Q4fnSSypzEjD)
_Setting up authentication in firebase_

In the list of sign-in providers, click on Email/Password:

![Image](https://cdn-media-1.freecodecamp.org/images/yiS92UoxyI60pQDvGKkmeduz0cqML4qRBPuw)
_List of sign-in providers_

Enable the option to all users to sign up using their email address and password. Then click the `save` button.

![Image](https://cdn-media-1.freecodecamp.org/images/85suaEwdDT71E0k3QbSPegLPeABexqZGJ3ov)
_Enable sign up using email and password_

#### Creating Sign Up Form

In a previous post, we stubbed out the Join.vue and Signin.vue files. These two files will have almost the same code. We will create the Join form first. When we are finished we will copy/paste it into the Signin form.

Open the Join.vue component. You can remove everything that is in the template. Vuetify has a default layout structure for components. It flows like this:

* v-container
* v-layout
* v-flex

So let’s create that layout now in the component. The start of our file looks like this:

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>            </v-flex>        </v-layout>    </v-container></template>
```

For the `v-container` we are adding `fill-height`. We add this so that it centers the form vertically in the window. For the `v-flex` we add `xs12` `sm8` and `md4` values. This is similar to Bootstrap’s column width definition. On extra-small devices, the form will take up all 12 columns meaning the whole screen. On small devices, the form will be 3/4 of the screen wide. On medium and large screens the form will be 1/3 of the screen.

Inside the `v-flex` we are going to use a `v-card`. We add `class=”elevation-12"` to the `v-card` so that it appears to be floating above the page. For the top of the form, we will use a `v-toolbar`. We give it a color of `primary`. For the default installation of Vuetify the primary color is blue. We want the text in the toolbar to be white text instead of the default black. To turn the text white we add `dark` to the `v-toolbar`.

Next, we have a `v-card-text`. Inside of it, we have a `v-form`. For the form we are giving it a reference with the name of `form`. We are assigning it to the `v-model` with a value of `valid`.

The last thing we add is `lazy-validation`. Our form needs to capture the user’s email and password. We will use two `v-text-field` to capture these values. To make things look better I have prepended an icon for each field. Each field has a `v-model` and `rules`.

Before the form is submitted the field will be validated against all rules that are defined. If they pass then you can submit the form. We will take advantage of this when the user clicks the Join button.

The last item to add to the form is a button. We add a `v-card-actions` and add a button. Here is what the template looks like for our component:

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>                <v-card class="elevation-12">                    <v-toolbar dark color="primary">                        <v-toolbar-title>Join Form</v-toolbar-title>                    </v-toolbar>                    <;v-card-text>                        <v-form ref="form" v-model="valid" lazy-validation>;                            &lt;v-text-field prepend-icon="person" name="email" label="Email" type="email"                                          v-model="email" :rules="emailRules" required>                            </v-text-field>                            <v-text-field prepend-icon="lock" name="password" label="Password" id="password"                                          type="password" required v-model="password" :rules="passwordRules">                            </v-text-field>                        </v-form>                    </v-card-text>                    <v-card-actions>                        <v-spacer></v-spacer>                        <v-btn color="primary" :disabled="!valid" @click="submit">Join</v-btn>                    </v-card-actions>                </v-card>            </v-flex>        </v-layout>    </v-container></template>
```

We defined several models in our template. We need to add them to the `data` section of our script. In the script add a data object. We will add valid, email, password, emailRules and passwordRules.

Email and password will contain the values the user inputs into the two text fields. Valid will tell if our form has passed all the rules we have created. For email, we check to make sure that the field is not empty. We also check that the contents match a basic RegExp to validate the email address. For password, we check to make sure the field is not empty. We also check to make sure the password is at least six characters in length.

Here is what the data object looks like now:

```
data() {    return {        valid: false,        email: '',        password: '',        emailRules: [            v => !!v || 'E-mail is required',            v => /.+@.+/.test(v) || 'E-mail must be valid'        ],        passwordRules: [            v => !!v || 'Password is required',            v =>                v.length >= 6 ||                'Password must be greater than 6 characters'        ]    };},
```

The last thing we need to add is methods. In methods, we have `submit()`. This method will validate our form first. If it passes validation then it will call an action in our Vuex store called `userJoin`. We pass it the email and password the user entered in the form.

Here is what the methods look like:

```
methods: {    submit() {        if (this.$refs.form.validate()) {            this.$store.dispatch('userJoin', {                email: this.email,                password: this.password            });        }    }}
```

#### Creating userJoin Action in Vuex

Open up the `store.js` file. We will create a new action called `userJoin`. By default the first parameter passed to this action is `context`. I will use object destructuring to get just `commit` from `context`. Commit is how I will call my mutation.

I will be using firebase to create the new user in the firebase database. To be able to use firebase in the store, I will need to import it. At the top of the file import firebase with this command:

```
import firebase from 'firebase';
```

Firebase authentication provides a method called `createUserWithEmailAndPassword`. We will pass the user’s email and password into this method. If it succeeds in registering the user it will return a user object. When it succeeds we will call two mutations: `setUser` and `setIsAuthenticated`. Here is what the action looks like:

```
userJoin({ commit }, { email, password }) {    firebase        .auth()        .createUserWithEmailAndPassword(email, password)        .then(user => {            commit('setUser', user);            commit('setIsAuthenticated', true);        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);        });}
```

This action calls two mutations. So let’s create then now. In mutations add a new mutation called `setUser`. Set the state value of user to the payload. Next, create a second mutation called `setIsAuthenticated`. Set the state value of isAuthenticated to the payload. Here is what the two mutations look like:

```
setUser(state, payload) {    state.user = payload;},setIsAuthenticated(state, payload) {    state.isAuthenticated = payload;}
```

In state, we need to add two new value: `user` and `isAuthenticated`. Here is what state looks like now:

```
state: {    recipes: [],    apiUrl: 'https://api.edamam.com/search',    user: null,    isAuthenticated: false},
```

#### Test Adding a New User

Start your server with the command `npm run serve`. Click on the `Join` button in the navigation. Enter your email and a password and click the join button. When you click the button nothing visible happens. To verify that the user was registered, go the firebase console in your browser. Click on `Authentication`. You should see a list of users that have been registered for your application. Here you can see that the user I just registered was created.

![Image](https://cdn-media-1.freecodecamp.org/images/vYkETdpPAbqno517wwsXH-g6tHJWZQXcQnrj)
_User has been registered_

We need to notify the user that they have been successfully created. We will do this but later. First, we are going to copy and paste the contents of the Join.vue component into the `Signin.vue` component. There are only two changes you will need to make in the template. Change the title to “Login Form.” For the button make the text say “Login.” In the submit method have it dispatch to `userLogin`. Just to make sure you have it correct, here is what my entire Signin.vue file looks like:

```
<template>    <v-container fill-height>        <v-layout align-center justify-center>            &lt;v-flex xs12 sm8 md4>                <v-card class="elevation-12">                    <v-toolbar dark color="primary">                        <v-toolbar-title>Login Form</v-toolbar-title>                    </v-toolbar>                    <;v-card-text>                        <v-form ref="form" v-model="valid" lazy-validation>;                            &lt;v-text-field prepend-icon="person" name="email" label="Email" type="email"                                          v-model="email" :rules="emailRules" required>                            </v-text-field>                            <v-text-field prepend-icon="lock" name="password" label="Password" id="password"                                          type="password" required v-model="password" :rules="passwordRules">                            </v-text-field>                        </v-form>                    </v-card-text>                    <v-card-actions>                        <v-spacer></v-spacer>                        <v-btn color="primary" :disabled="!valid" @click="submit">Login</v-btn>                    </v-card-actions>                </v-card&gt;            </v-flex&gt;        </v-layout>    </v-container></template><script>export default {    name: 'Signin',    data() {        return {            valid: false,            email: '',            password: '',            emailRules: [                v => !!v || 'E-mail is required',                v => /.+@.+/.test(v) || 'E-mail must be valid'            ],            passwordRules: [                v => !!v || 'Password is required',                v =&gt;                    v.length >= 6 ||                    'Password must be greater than 6 characters'            ]        };    },    methods: {        submit() {            if (this.$refs.form.validate()) {                this.$store.dispatch('userLogin', {                    email: this.email,                    password: this.password                });            }        }    }};</script><style scoped></style>
```

That’s it. You have now created both the Join and Login forms.

We need to create the action for Login. Open up the `store.js` file. Create a new action called userLogin. We will use firebase to login the user. Firebase provides a method called `signInWithEmailAndPassword`. We will call this method and pass in the user’s email and password they entered into the form. If the user entered their email and password correctly then we will call the two mutations `setUser` and `setIsAuthenticated`. Here is what the `userLogin` action looks like:

```
userLogin({ commit }, { email, password }) {    firebase        .auth()        .signInWithEmailAndPassword(email, password)        .then(user => {            commit('setUser', user);            commit('setIsAuthenticated', true);        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);        });},
```

#### Redirecting to Profile

When a user successfully registers or login, we want to redirect them to their profile. When we created our app initially the Vue CLI 3 it created two routes for us. Those routes were `/` and `/about`. Eventually, the profile will contain a list of all recipes that the user has ordered from the `menu` page. Remember the button we put at the bottom of every recipe? That button will add the recipe to the user’s profile and store it in the database in firebase.

To redirect the user to the profile we will first import router at the top of the store.js file. The router is imported with the command:

```
import router from '@/router';
```

Next, in both actions we redirect the user to /about if they successfully register or login. You can do the redirection with this command:

```
router.push('/about');
```

If the user fails to register an account or login successfully we will redirect the user to the home page. _(NOTE: in a perfect scenario we will provide some notice to the user why the registration or login failed)._ You can redirect them to the home page with this command:

```
router.push('/');
```

To test the redirection, start your server and click on the Login button. Enter the email and password you used when you created your user account. Click the Join button. If everything worked successfully you should be redirected to the About page.

#### Updating the navigation

The navigation has buttons for `Sign In` and `Join`. When a user successfully registers or login we would like to hide these two buttons. In their place, we want to show a `Logout` button.

Open up the `AppNavigation` component. We are going to group the two current buttons in a div. We are going to remove the class to hide the buttons on small and extra-small devices. Instead, we will place this class on the div. We add a `v-if` to the div to only show if the user is currently not authenticated. Below the `div` we will add a new button for Logout. This new button will have a style of outline with a color of white. When you click on this button it will call the method `logout`. We add a v-else to this button to show when the user is authenticated.

Next, add a method called `logout`. This method will call an action in our store called `userSignOut`.

We also need to add a new computed property called `isAuthenticated`. This property returns the value of isAuthenticated in the state of our store.

Here is what your AppNavigation should look like:

```
<template>    <span>        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>            <v-list>                <template v-for="(item, index) in items">                    <v-list-tile :key="index">                        <v-list-tile-content>                            {{item.title}}                        </v-list-tile-content>                    <;/v-list-tile>                    <v-divider :key="`divider-${index}`"></v-divider>                </template>            </v-list>        </v-navigation-drawer>        <v-toolbar app color="brown darken-4" dark>            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>            <v-spacer class="hidden-md-and-up"></v-spacer>            <router-link to="/"&gt;                <v-toolbar-title to="/">{{appTitle}}</v-toolbar-title>;            </router-link>            <;v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>            <v-spacer class="hidden-sm-and-down"></v-spacer>            <;div v-if="!isAuthenticated" class="hidden-sm-and-down">                <v-btn flat to="/sign-in">SIGN IN</v-btn>                <v-btn color="brown lighten-3" to="/join">JOIN</v-btn>            </div>            <v-btn v-else outline color="white" @click="logout">Logout</v-btn>        </v-toolbar>    </span></template><script>export default {    name: 'AppNavigation',    data() {        return {            appTitle: 'Meal Prep',            drawer: false,            items: [{ title: 'Menu' }, { title: 'Sign In' }, { title: 'Join' }]        };    },    computed: {        isAuthenticated() {            return this.$store.getters.isAuthenticated;        }    },    methods: {        logout() {            this.$store.dispatch('userSignOut');        }    }};</script><style scoped>a {    color: white;    text-decoration: none;}</style>
```

We need to add the getter and action we just defined. Open up the `store.js` file. Create a new action called `userSignout`. This action will use firebase.auth() to sign the user out. After signing the user out, it sets the state variables `user` to null and `isAuthenticated` to false. Here is the `userSignout` method in the store:

```
userSignOut({ commit }) {    firebase        .auth()        .signOut()        .then(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);            router.push('/');        })        .catch(() => {            commit('setUser', null);            commit('setIsAuthenticated', false);            router.push('/');        });}
```

Next, we need to add a `getters` section to the store object. The `isAuthenticated` getters method will return true or false based on user authentication. Here is what the `getters` section of the store looks like:

```
getters: {    isAuthenticated(state) {        return state.user !== null && state.user !== undefined;    }}
```

### Adding Recipes to Database

Once a user is logged in they can click on any recipe to add it to their account. Their recipes will be shown in their profile which is the `/about` route. We need a database to store these recipes. Go to your firebase console in the browser. Click on `database` in the left side navigation panel. On the next screen you will see buttons to create a realtime database or a cloud firestore database. Make sure you create a new realtime database. In the dialog make sure you select to `start in test mode`. Then click the `enable` button.

![Image](https://cdn-media-1.freecodecamp.org/images/nHYgB0KpSgNkOE49AhvBos0IHr3mWw35ZJQJ)
_Start database in test mode_

Now we want to store the user’s recipes in the database. Open up the MealRecipes component. If a user tries to order a recipe and they are not logged in then we should redirect them to the login page. So let’s take care of that now. On the `Order` button add an @click that calls the method orderRecipe. Be sure to pass in `item` as an argument to the method. Your button should look like this:

```
<v-card-actions>    &lt;v-btn color="green" dark @click="orderRecipe(item)">Order</v-btn></v-card-actions>
```

Before we create our method, we will create a computed value for isAuthenticated. This is the exact same code we used in `AppNavigation` earlier to show and hide the login and logout button correctly. Add a computed isAuthenticated. It should look like this:

```
export default {    name: 'MealRecipes',    computed: {        recipes() {            return this.$store.state.recipes;        },        isAuthenticated() {            return this.$store.getters.isAuthenticated;        }    }};
```

Now we are ready to create our orderRecipe method. Add this method and its parameter. In this method, we want to first check if the user is logged in or not. If they are not we want to redirect them to `/sign-in` . If they are signed in then we want to call an action in the Vuex store that will append the recipe to the user account in the database. Here is what our method looks like:

```
methods: {    orderRecipe(item) {        if (this.isAuthenticated) {            this.$store.dispatch('addRecipe', item);        } else {            this.$router.push('/sign-in');        }    }}
```

Open up the store.js file. We need to create a new action to add recipes. In this action, we are going to use firebase to add the recipe to a database called `users`. When the user was registered in firebase they were assigned a unique userid. We will be using this `uid` to store the name of the recipe in the database.

In this action, we will be using `state` to get the value of the currently selected user. The `user` in `state` is an object. That object has a key called user. In that object, we will find the `uid`. We use that to push the title of the selected recipe into the database. Here is the action:

```
addRecipe({ state }, payload) {    firebase        .database()        .ref('users')        .child(state.user.user.uid)        .push(payload.recipe.label);}
```

Now start your server and log in. Select a diet from the menu page. Then order a couple of recipes. The recipes you ordered should be shown in the database in firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/SBJUuIRCRWT2Fu3iAiZeEERyYXPTfeLaSLwt)
_Recipes added to the database_

Now that we have the recipes added to the database, we actually need to display them on the profile page for the user. Open up the `About.vue` file. Whenever this page is loaded it should fetch all the user’s recipes. To do this we add `mounted()` in our script. This will call a method called `getRecipes`.

Let’s create that method now. In the method, we are going to call an action in our Vuex store that will get all the user’s recipes. We have not created this action in the store yet but in simple terms, this action will get the user’s recipes. Then it will store them in a variable in `state` called `userRecipes`.

Before we leave About.vue, add a computed property for `userRecipes`. This will return the `userRecipes` from `state` in our store. This is what About.vue script should look like:

```
export default {    name: 'About',    computed: {        userRecipes() {            return this.$store.state.userRecipes;        }    },    mounted() {        this.getRecipes();    },    methods: {        getRecipes() {            this.$store.dispatch('getUserRecipes');        }    }};
```

Next, open up your `store.js` file. We need to create the `getUserRecipes` action. When the user logins we store a variable in `state` called user. This variable will have the unique user ID assigned to that user when it was registered in firebase. We want to get all the recipes in the users database that have this user ID. Once we get all the recipes we want to set userRecipes to contain them. Here is the getUserRecipes action:

```
getUserRecipes({ state, commit }) {    return firebase        .database()        .ref('users/' + state.user.user.uid)        .once('value', snapshot => {            commit('setUserRecipes', snapshot.val());        });}
```

In our mutations, we need to add a `setUserRecipes`. It looks like this:

```
setUserRecipes(state, payload) {    state.userRecipes = payload;}
```

We also need to add a `userRecipes` in `state`. We set its initial value to an empty array. Here is my entire state object:

```
state: {    recipes: [],    apiUrl: 'https://api.edamam.com/search',    user: null,    isAuthenticated: false,    userRecipes: []},
```

Now that we are getting the recipes we need to display them on the page to the user. So go back to your `About.vue` file. In the template, we are going to loop through all the user’s recipes and display them. I am going to show you my code for the template first then explain what I have done:

```
<template>    <v-container >        <v-layout column>;            <h1 class="title my-3">My Recipes</h1>            <div v-for="(item, idx) in userRecipes" class="subheading mb-2" :key="idx">                {{item}}            </div>        </v-layout>    </v-container></template>
```

I have set the layout to be `column`. I did this because I want each recipe to be listed on the page. To make things look clearer I have added a title. I added my-3 to add margin-top and margin-bottom so that there is spacing between the title and the list of recipes. Next, I looped through each recipe and display it. This is what the user sees if they have recipes:

![Image](https://cdn-media-1.freecodecamp.org/images/AXzGqeL9LhTRcYHIFkQgEjQwRAW4UFRP4Enr)
_List of my recipes_

This is great, but when if a user logs in and they do not have any recipes? They see the title “My Recipes” and a blank page. This is not a user-friendly design. So let’s change it to display something more friendly.

We will display a button that will take the user to the `menu` page. In our template, we will add this button. To make the button redirect to the menu page we can add `to=”/menu”` to the button. Here is my final template for the `About.vue` component.

```
<template>    <v-container >        <v-layout column>;            <h1 class="title my-3">My Recipes</h1>            <div v-for="(item, idx) in userRecipes" class="subheading mb-2" :key="idx">                {{item}}            </div>            &lt;v-flex mt-4>                <v-btn color="primary" to="/menu">Go To Menu</v-btn>            </v-flex>        </v-layout>    </v-container></template>
```

#### Showing Profile in Navigation

The last thing we need to add is the ability to show a link to the profile in the navigation. Just like the logout button, this should only be shown if the user is authenticated.

Open up the AppNavigation components. We are going to group the profile button and the logout button in a div. This is the same thing we did earlier for the `Sign In` and `Join` buttons. Add a div and move the logout button to be inside this div. Add another button for `profile`. This button will be flat just like the `Sign In` button.

Here is what my AppNavigation looks like now:

```
<template>    <span>        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>            <v-list>                <template v-for="(item, index) in items">                    <v-list-tile :key="index">                        <v-list-tile-content>                            {{item.title}}                        </v-list-tile-content>                    <;/v-list-tile>                    <v-divider :key="`divider-${index}`"></v-divider>                </template>            </v-list>        </v-navigation-drawer>        <v-toolbar app color="brown darken-4" dark>            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>            <v-spacer class="hidden-md-and-up"></v-spacer>            <router-link to="/"&gt;                <v-toolbar-title to="/">{{appTitle}}</v-toolbar-title>;            </router-link>            <;v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>            <v-spacer class="hidden-sm-and-down"></v-spacer>            <;div v-if="!isAuthenticated" class="hidden-sm-and-down"&gt;                <v-btn flat to="/sign-in">SIGN IN</v-btn>                <v-btn color="brown lighten-3" to="/join">JOIN</v-btn>            </div>            <div v-else>                <v-btn flat to="/about">PROFILE</v-btn>                <v-btn outline color="white" @click="logout">Logout</v-btn>            </div>        </v-toolbar>    </span></template>
```

### Adding Route Guards

Currently, the user can navigate to the profile page by typing it into the URL of the browser We don’t want to let users do this if they are not logged in. Vue Router provides the ability to add route guards before navigating to a URL. We want to test if a user is authenticated before allowing them to redirect to the `/about` page.

Open up the `router.js` file. Route guards work in conjunction with meta tags. Find the `/about` route. We will add a `authRequired` meta tag to it. The route should look like this:

```
{    path: '/about',    name: 'about',    component: () =&gt; import('./views/About.vue'),    meta: {        authRequired: true    }},
```

Route guards are checked in a method called beforeEach that is part of Vue Router. This method is passed three parameters:

* the route you are going to
* the route you came from
* a next method that continues with the current route

Our beforeEach method will check every route that we are going to to see if it contains the meta tag of authRequired. If it does, it will check to see if the user is Authenticated. If the user is not authenticated it will redirect them to the `/sign-in` page. If the user is logged in then it will allow the route to proceed. If a user routes to any page that does not have the authRequired meta tag then the route will proceed.

Here is the method I have added to my router to do this checking:

```
router.beforeEach((to, from, next) => {    if (to.matched.some(record => record.meta.authRequired)) {        if (!store.state.user) {            next({                path: '/sign-in'            });        } else {            next();        }    } else {        next();    }});
```

### Get the Code

Even though this is a 4-part series, you can get the [finished code in my GitHub account.](https://github.com/ratracegrad/meal-prep) Please help me out and **star the repo** when you get the code.

### Summary

In this part of this series, you have learned:

* What is firebase
* Using firebase to authenticate users who sign in with email and password
* Using firebase to store the recipes a user has ordered
* Using route guards to not users access pages if they are not authenticated
* Display user’s list of recipes from the database on firebase

If you enjoyed this article please clap for it. If you think somebody else would benefit from this article please share it with them.

If you have any questions or find anything wrong with the code, please leave a comment. If there are other topics you would like for me to write about, please leave a comment.

#### Other Articles

Here are other articles I have written that you might want to read.

[**How to add Internationalization to a Vue Application**](https://medium.freecodecamp.org/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b)  
[_¡Hola! Bonjour. Ciao. 你好. Here is how you add internationalization to Vue._medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b)[**Instantiation Patterns in JavaScript**](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)  
[_Instantiation patterns are ways to create something in JavaScript. JavaScript provides four different methods to create…_medium.com](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)[**Here are 5 Layouts That You Can Make With FlexBox**](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)  
[_The CSS Flexible Box Layout — Flexbox — provides a simple solution to the design and layout problems designers and…_hackernoon.com](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)

[**Follow Me On Twitter!**](https://twitter.com/ratracegrad)

