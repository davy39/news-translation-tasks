---
title: Comment configurer l'authentification utilisateur avec React, Redux et Redux
  Saga
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-12T15:30:07.000Z'
originalURL: https://freecodecamp.org/news/login-using-react-redux-redux-saga-86b26c8180e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*y-qgopNVlYcVrXgM84iPfA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: Redux
  slug: redux
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment configurer l'authentification utilisateur avec React, Redux et
  Redux Saga
seo_desc: 'By Zafar Saleem

  UPDATE(12.02.2019): I recently updated this project with most recent react routers
  i.e. version 4.3.1 which is react-router-dom. Please head to its repository to view
  the changes.

  In my previous blog I wrote how to write a scalable ar...'
---

Par Zafar Saleem

**MISE À JOUR (12.02.2019) : J'ai récemment mis à jour ce projet avec les dernières versions de react routers, c'est-à-dire la version 4.3.1 qui est react-router-dom. Veuillez vous rendre sur son dépôt pour voir les changements.**

Dans mon [précédent](https://medium.freecodecamp.org/writing-scalable-architecture-for-node-js-2b58e0523d7f) blog, j'ai écrit comment écrire une architecture évolutive en Node.js. Puisque j'ai utilisé Postman pour tester le fonctionnement de cette plateforme, j'ai pensé que ce serait une bonne idée d'avoir son implémentation côté client. Pour écrire son côté client, j'ai décidé d'utiliser la stack technique suivante :

* React
* Redux
* Redux-Saga
* React Router

**Cet article suppose que vous connaissez déjà React et les concepts de base de Redux et Redux-Saga.**

### Commencer

Clonez le dépôt de mon précédent blog [repository](https://github.com/zafar-saleem/NodeScalableArchitecture). `CD` dans son dossier racine et exécutez `npm install`. Cela installera toutes les dépendances.

Deuxièmement, [installez mongodb](https://docs.mongodb.com/manual/installation/) sur votre machine. Une fois installé, exécutez le serveur mongo en utilisant la commande `mongod` dans votre terminal, s'il n'est pas démarré en tant que service sur votre machine.

Ensuite, assurez-vous que le package [nodemon](https://nodemon.io/) est installé sur votre machine **globalement**. Allez dans le dossier côté serveur et exécutez `nodemon index.js` pour exécuter le serveur backend.

Maintenant que notre backend est opérationnel, il est temps de passer à son implémentation côté client.

Si vous n'avez pas encore installé `create-react-app`, alors installez-le en utilisant la commande suivante.

```
npm install create-react-app -g
```

Cette commande installera `create-react-app` **globalement**.

### Créer le projet

Il est maintenant temps de créer un projet. Utilisez :

```
create-react-app react-login
```

Cela créera un nouveau projet avec le nom `react-login`. Allez-y et `cd` dans ce dossier. Ouvrez votre fichier `package.json` dans votre éditeur préféré et ajoutez les dépendances suivantes :

Nous n'avons pas besoin de propriétés supplémentaires dans ce fichier `package.json`. Nous pouvons simplement les supprimer, mais je vais les laisser telles quelles et avancer pour que nous arrivions à la partie intéressante de ce blog.

Exécutez simplement :

```
npm install
```

ce qui installera toutes les dépendances que nous avons mentionnées ci-dessus.

#### Fichier Index

Pour commencer, ouvrez le fichier `index.js` et placez le code ci-dessous dans ce fichier.

Dans ce code, nous importons `react` et `react-dom`. Ensuite, nous importons `Router` et `browserHistory` de `react-router`. Ceux-ci sont nécessaires pour le routage, que j'utiliserai plus tard dans le fichier `routes/index.js`. Ensuite, nous importons `Provider`, qui est utilisé pour fournir le store aux composants enfants.

`configureStore` et `routes` sont des éléments que nous allons importer ensuite et que je vais implémenter dans un instant. Importons-les simplement tels quels et utilisons-les dans ce fichier comme montré ci-dessus.

Notre fichier index est maintenant configuré.

#### Configuration du Store

Créez un nouveau dossier appelé `store` à l'intérieur du dossier `src`. À l'intérieur de ce nouveau dossier, créez un fichier appelé `configureStore.js`, et collez le code suivant dans ce fichier.

Tout d'abord, nous importons `createStore`, qui sera utilisé pour `createStore`, et `applyMiddleware`, qui sera utilisé pour appliquer des middlewares à notre store — sagas dans ce cas, mais nous y reviendrons plus tard dans ce blog — de `redux`.

Nous importons ensuite `rootReducer` — que nous allons créer plus tard. Pour l'instant, importez-le simplement et utilisez-le tel quel. Cela est suivi par la fonction `configureStore`, qui retourne un objet en appelant la fonction `createStore` et en passant `rootReducer` comme paramètre.

Enfin, `export configureStore` rend `configureStore` disponible dans le fichier `index.js`, construit précédemment.

Maintenant que cela est fait, allez-y et créez le dossier `src/reducers`, créez le fichier _index.js_ et collez le code ci-dessous dans ce fichier.

Ce fichier est responsable de l'importation des autres reducers à l'intérieur du dossier reducers, de les combiner et de les exporter afin qu'ils soient disponibles pour être utilisés dans `configureStore.js`. Nous apporterons des modifications à ce fichier lorsque nous ajouterons de nouveaux reducers plus tard dans ce blog.

#### Fichier de routage

Il est temps de créer le fichier de routes. Allez-y et créez le dossier `src/routes` et à l'intérieur de ce dossier, créez un fichier `index.js`. Ouvrez-le et collez le code ci-dessous.

Le principal objectif de ce fichier est de gérer le routage dans notre projet. Le fichier importe `React`, `Route` et `IndexRoute`. Après cela, nous avons besoin d'un conteneur, dans ce cas, j'importe `container/App`, que nous allons écrire bientôt. Ensuite, il y a `RegisterPage`, qui est un composant, et nous allons l'écrire également.

Dans la `Route` parente, lorsque le chemin d'accès à la page d'accueil correspond, nous rendons simplement notre conteneur `App`. Sur `IndexRoute`, les utilisateurs verront `RegisterPage` qui sera rendu à l'intérieur du conteneur `App`.

#### Conteneur

Il est maintenant temps de créer le conteneur. Allez-y et créez un nouveau dossier appelé `container`. À l'intérieur de ce dossier, créez un nouveau fichier appelé `App.js` et placez le code ci-dessous dans ce fichier.

Cela est assez simple. Le principal objectif de ce fichier est de rendre le reste des composants. `{this.props.children}` sert à cet effet.

#### Inscription

Il est maintenant temps de créer `registerPage`. Créez un nouveau dossier `src/components` et créez un composant à l'intérieur du dossier components appelé `registerPage.js`. Collez le code ci-dessous dans ce composant.

Pour l'instant, ce composant est très simple. Nous le modifierons plus tard pour ajouter un formulaire d'inscription et y mettre quelques fonctionnalités.

#### Résultat

Après avoir créé tous les dossiers et fichiers ci-dessus, exécutez `npm start` dans votre projet, et ouvrez `http://localhost:3000` dans votre navigateur. Vous devriez pouvoir voir le résultat ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N6X4lwUQccUC3mPb8uZ7xg.png)

Cliquer sur login ici ne **redirigera pas** vers la route de login, ce que nous corrigerons ensuite.

### Le faire fonctionner

#### Routage

Pour que le routage fonctionne, créez d'abord un nouveau composant à l'intérieur du dossier components. Nommez-le `loginPage.js` et placez le code ci-dessous dans ce composant.

Ce composant est très simple. Il rend un contenu de base et un lien pour enregistrer le composant.

Ouvrez maintenant le fichier `routes.js`, que nous avons déjà créé ci-dessus, et apportez les modifications suivantes.

Changez la route d'index en `LoginPage` car nous voulons que les utilisateurs arrivent sur le composant de login lorsqu'ils visitent la page d'accueil. Avant de faire cela, importez-le depuis le dossier components.

Actualisez maintenant votre navigateur et vous devriez pouvoir voir `loginPage` en premier. Lorsque vous cliquez sur le lien "Register here", `registerPage` devrait être rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*r4DHKgFjLwuVCNrinhOiTQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*d7NldTSjQ3g50UGB1ar6_A.png)

Maintenant, nous avons les routes de base qui fonctionnent.

### Connexion et inscription

#### Inscription

Afin de faire fonctionner le processus de connexion, je vais d'abord gérer le processus d'inscription afin que nous ajoutions quelques utilisateurs dans notre base de données. Alors, allez-y et ouvrez `components/registerPage.js` et mettez-le à jour avec le contenu ci-dessous.

Il semble y avoir beaucoup de code dans ce fichier maintenant, mais c'est tout simple. Tout d'abord, nous importons `connect` pour connecter notre `store` avec le composant `registerPage`. Ensuite, nous importons `registerUserAction` que nous allons écrire ensuite.

À l'intérieur de la fonction `render`, je vérifie d'abord la réponse du serveur si elle existe, puis j'assigne les propriétés success et message qui sont reçues du serveur. Cela peut être une fonction séparée mais, pour des raisons de simplicité, je les ai placées dans la fonction `render`.

Ensuite, il y a un formulaire d'inscription. Lorsque l'utilisateur clique sur le bouton d'inscription, cela déclenche la fonction `onHandleRegistration` qui obtient les données saisies par l'utilisateur à partir du formulaire, et `dispatch registerUserAction` avec leurs données comme paramètres. Nous allons écrire les actions dans l'étape suivante.

Pour que le code ci-dessus fonctionne, nous avons besoin de `mapStateToProps`, comme nous le faisons en bas du composant, puis nous le connectons avec le composant `registerPage` à la fin.

**Actions**

Il est maintenant temps d'ajouter des actions. Allez-y et créez le dossier `src/actions`. Créez le fichier `index.js` et placez le code ci-dessous dedans.

Ce code exporte quelques constantes que nous utiliserons tout au long de notre projet.

Maintenant, allez-y et créez le fichier `authenticationActions.js` dans le même dossier, et placez le code ci-dessous dedans.

Ici, j'importe le fichier index, qui exporte des constantes, puis j'`export registrationUserAction` et retourne un objet avec le type d'action et les données de l'utilisateur. Le type d'action dans ce cas est `REGISTER_USER`. Cette action sera dispatchée lorsqu'un utilisateur essaie de s'inscrire, et cette action sera disponible dans tout notre projet, que nous écouterons dans nos sagas.

**Sagas**

Nous en sommes maintenant à l'étape où nous pouvons introduire nos sagas dans notre projet. **Si vous êtes nouveau dans Redux-Saga, je vous suggère de lire [ce blog](https://flaviocopes.com/redux-saga/) avant de continuer.**

Si vous connaissez déjà les sagas, allez-y et créez un dossier `src/sagas`. Créez le fichier `index.js`, et placez le code ci-dessous dans ce fichier.

Dans le fichier ci-dessus, j'importe d'abord `fork` de `effects` et `watchUserAuthentication` de `watchers` — qui n'existe pas encore mais nous créerons ce fichier ensuite. Ensuite, j'exporte simplement une [fonction génératrice](https://codeburst.io/understanding-generators-in-es6-javascript-with-examples-6728834016d5) et fork `watchUserAuthentication`.

Maintenant, allez-y et créez un fichier `watcher.js` dans le même dossier que ci-dessus, et placez le code ci-dessous dans ce fichier.

Encore une fois, j'importe l'effet `takeLatest` de `redux-saga`, puis `registerSaga` de `authenticationSaga.js`, que nous allons créer ensuite. Ensuite, j'importe `actions/index.js` comme types.

J'exporte une fonction génératrice qui surveille essentiellement l'action `REGISTER_USER` et fait un appel à `registerSaga`.

Créons maintenant le saga `authenticatioSaga.js` dans le même dossier que ci-dessus, et plaçons le code ci-dessous dans ce fichier.

Dans ce saga, j'importe quelques effets supplémentaires — `put` et `call` de `redux-saga`. Ensuite, `registerUserService` est importé de `service/authenticationService.js`. J'importe toutes les actions comme types de `actions/index.js`. Ensuite, j'exporte la fonction génératrice `registerSaga`.

Cette fonction est responsable de l'appel à `registerUserService`, qui fait un appel ajax à notre serveur pour enregistrer un nouvel utilisateur — que je vais écrire après cette étape. Elle reçoit une réponse de `registerUserService` et met l'action `REGISTER_USER_SUCCESS`. Si une erreur survient, elle met l'action `REGISTER_USER_ERROR`.

**Importer les sagas**

Maintenant que nous avons nos sagas, il est temps de les importer dans notre store. Ouvrez `store/configureStore.js` et mettez à jour son contenu avec le contenu ci-dessous.

Ici, j'importe `createSagaMiddleware`, `rootReducer`, et `rootSaga`. Ensuite, à l'intérieur de la fonction `configureStore`, je crée un nouveau `sagaMiddleware` et le passe à `createStore` en utilisant la fonction `applyMiddleware`. Enfin, j'exécute le `rootSaga`.

Maintenant, il est temps de créer le dossier `src/services` et de créer un nouveau premier service. Nommez-le `authenticationService.js` et placez le code ci-dessous dans ce service.

Ce fichier effectue une requête ajax de base en utilisant l'API fetch avec certains paramètres et en-têtes. C'est un service assez explicite.

**Reducer**

Maintenant que nous faisons une requête au serveur, il est temps de recevoir cette réponse dans notre composant. Pour cela, nous avons besoin d'un **reducer**. Allez-y et créez un fichier `reducers/registerReducer.js` et placez le code ci-dessous dedans.

C'est une fonction reducer simple qui obtient l'état et retourne un nouvel état. Elle vérifie les actions `REGISTER_USER_SUCCESS` et `REGISTER_USER_ERROR`, et retourne le nouvel état au composant.

Maintenant, allez-y et ouvrez le fichier `src/reducers/index.js` et mettez-le à jour avec le contenu suivant.

Dans ce `rootReducer`, j'importerai tous les reducers puis les combinerai avant de les exporter. C'est exactement ce que je fais avec `register`.

**Exécuter le code mis à jour**

Maintenant, nous avons terminé avec le processus d'inscription. Il est temps d'actualiser votre navigateur, d'aller à la route d'inscription et d'entrer quelques données. Si vous entrez un email existant, vous devriez voir le résultat ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzeEPD99OVPG2N0k8KewlA.png)

Si vous entrez un nouvel email, vous devriez être redirigé vers `loginPage`, que nous allons implémenter ensuite.

### Connexion

Il est temps pour nous de connecter l'utilisateur après qu'il soit inscrit. Allez-y et ouvrez le fichier `components/loginPage.js` et mettez-le à jour avec le contenu suivant.

Ce composant est presque identique à `registerPage`. La seule différence est qu'il dispatch `loginUserAction` que nous allons écrire ensuite. Une autre différence est que, si la réponse du serveur est réussie, je recevrai un `JWT token`. Je stocke ce token dans `localStorage`. Vous pouvez utiliser une méthode différente mais pour cet exemple, j'utilise cette approche.

Allez-y et ouvrez `actions/authenticationActions.js` et mettez-le à jour avec le contenu suivant.

Ici, j'exporte la nouvelle fonction `loginUserAction` avec le type d'action `LOGIN_USER` et la `charge utile de l'utilisateur`.

Avant de continuer, allez-y et ouvrez le fichier `actions/index.js` et mettez à jour son contenu avec le suivant.

Maintenant, allez-y et ouvrez le fichier `sagas/watchers.js` et mettez à jour son contenu avec le suivant.

Ici, j'importe simplement `loginSaga` et l'appelle lorsqu'il reçoit l'action `LOGIN_USER`.

Nous n'avons pas encore `loginSaga`. Pour cette raison, allez-y et ouvrez le saga `sagas/authenticationSaga.js` et mettez à jour son contenu avec le suivant.

Ici, j'importe un service supplémentaire — `loginUserService`, que je vais implémenter ensuite — puis j'exporte la nouvelle fonction génératrice nommée `loginSaga`, qui fait à peu près la même chose que `registerSaga`.

Ouvrez maintenant le service `services/authenticationService.js` et mettez à jour son contenu avec le suivant.

Ici, j'ajoute loginUserService qui fait à peu près la même chose que registerUserService, c'est-à-dire envoyer une requête ajax pour connecter l'utilisateur.

Maintenant que nous avons envoyé avec succès une requête au serveur, il est temps de recevoir une réponse de notre serveur vers notre composant de connexion. Pour cela, créez un nouveau reducer _reducers/loginReducer.js_ et placez le code ci-dessous dedans.

Il fait à peu près la même chose que `registerReducer` — écoute les actions `LOGIN_USER_SUCCESS` et `LOGIN_USER_ERROR`, et retourne le nouvel état.

Ouvrez maintenant le fichier `reducers/index.js` et mettez à jour son contenu avec le code ci-dessous.

Ici, j'importe `loginReducer` et le combine avec `register` avant de le retourner en tant que `rootReducer`.

Après cela, actualisez votre navigateur et entrez un email qui n'est pas encore enregistré. Après avoir appuyé sur le bouton de connexion, vous devriez voir le résultat ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rg6-ST-_fpgAIIs2t-DYbA.png)

Si vous entrez un email enregistré, la requête devrait être réussie, mais vous ne devriez pas encore voir quoi que ce soit, car je n'ai pas implémenté le composant `dashboardPage`. Celui-ci ne sera accessible qu'après une authentification réussie. Cela dit, implémentons-le.

### Page de tableau de bord

Créez maintenant le composant `components/dashboardPage.js` et placez le code ci-dessous dans ce composant.

C'est un composant très simple — tout ce qu'il fait est de retourner le texte `Dashboard`.

Ouvrez maintenant la route `routes/index.js` et mettez à jour son contenu avec le suivant.

Ici, je fais quelques nouvelles choses. Tout d'abord, j'importe une `dashboardPage` et je l'ajoute à `route`. Lorsque la route `dashboard` est accessible, la fonction `requireAuth` sera déclenchée. Cette fonction vérifie si l'utilisateur est `loggedIn` ou non. Pour vérifier cela, je cherche `token` dans `localStorage`, que j'ai stocké dans le composant `loginPage` lors d'une connexion réussie. Si elle existe, alors `dashboardPage` est rendu à l'utilisateur.

Maintenant, lorsque vous actualisez la page dans votre navigateur, entrez un email enregistré et appuyez sur entrer, vous devriez voir les résultats ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wnMpcYFl7gupB-gS715JqA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8a6a-rkqeAvlna01G6JH4Q.png)

Donc, voici un système de connexion complet utilisant React, Redux et Redux-Saga. Si vous souhaitez voir le projet entier, alors [clonez ce dépôt](https://github.com/zafar-saleem/react-login).

J'espère que vous avez apprécié cet article.