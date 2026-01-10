---
title: Authentification Angular simplifiée avec Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-07T23:30:08.000Z'
originalURL: https://freecodecamp.org/news/angular-2-authentication-made-easy-with-firebase-246c282d9ef8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oOBXowI2IO9eCTcxP1BT-Q.jpeg
tags:
- name: angular2
  slug: angular2
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: Security
  slug: security
- name: Web Development
  slug: web-development
seo_title: Authentification Angular simplifiée avec Firebase
seo_desc: 'By Wassim Chegham


  UPDATE: The code in this article has been updated to Angular Final. We also assume
  that you’re using the latest Angular CLI.


  Any serious Web application requires some sort of authentication feature. In this
  blog post, we’ll set up...'
---

Par Wassim Chegham

> MISE À JOUR : Le code dans cet article a été mis à jour pour Angular Final. Nous supposons également que vous utilisez le dernier Angular CLI.

Toute application Web sérieuse nécessite une forme d'authentification. Dans cet article de blog, nous allons configurer cette fonctionnalité pour une application Angular en utilisant Firebase, grâce à la bibliothèque officielle [AngularFire2](https://github.com/angular/angularfire2).

### Créer un nouveau projet Firebase

Avant d'utiliser Firebase avec notre application, nous devons créer un nouveau projet dans notre [console de développement Firebase](https://console.firebase.google.com/) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZzoMPcmlDgYRLCQgAFiU8Q.png)
_Console de développement Firebase_

Pour utiliser la fonctionnalité d'authentification Firebase, nous devons activer les **fournisseurs de connexion** que nous voulons utiliser dans notre projet. Dans notre cas, nous allons utiliser Google, Facebook, Twitter et Github pour connecter nos utilisateurs.

Vous pouvez trouver la page d'authentification dans : Votre App → Auth → MÉTHODE DE CONNEXION :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wfIpVAzDOEVFUJR2UjUp5g.png)

Certains fournisseurs, tels que Facebook, Twitter et Github, nécessitent que vous fournissiez une **ID d'application/client/API** et des clés **secrètes d'application/client/API**, et que vous utilisiez l'**URI OAuth** donnée comme URI de redirection :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cmB2uiqwESrHHwKo1RVkgA.png)

Afin d'obtenir ces informations, vous devrez créer une application pour chaque fournisseur en utilisant votre compte développeur de chaque service (Github, Facebook et Twitter).

### Configurer vos services

![Image](https://cdn-media-1.freecodecamp.org/images/1*M372rrSgYuiwgODlftxKDQ.png)
_Paramètres de l'application Github_

Pour Github, allez dans vos [paramètres de développeur](https://github.com/settings/developers), et [enregistrez](https://github.com/settings/applications/new) une nouvelle application.

Utilisez votre **ID client** et **secret client** de l'application dans votre page de configuration Firebase.

Vous devez également remplir l'**URL de rappel d'autorisation** en utilisant l'**URI OAuth** de Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UsjnM5koHUhanSlGXYR6Yg.png)
_Paramètres de l'application Twitter_

Pour Twitter, allez dans vos [paramètres de gestion de l'application](https://apps.twitter.com/), et [créez une nouvelle](https://apps.twitter.com/app/new) application.

Utilisez votre **clé API** et **secret API** de l'application dans votre page de configuration Firebase.

Vous devez également remplir l'**URL de rappel** (dans l'onglet Paramètres) en utilisant l'**URI OAuth** de Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*blTSqtexKVeShcVPDMHKaw.png)
_Console de développement Facebook_

Enfin, pour Facebook, allez sur la [page d'accueil de vos applications de développeur](https://developers.facebook.com/apps/), et cliquez sur le bouton vert "Ajouter une nouvelle application" en haut à droite.

Utilisez votre **ID d'application** et **secret d'application** dans votre page de configuration Firebase.

Vous devez également ajouter une nouvelle plateforme Web. Cliquez sur **+Ajouter une plateforme** en bas de la page et remplissez l'URL du site avec l'URI de redirection de Firebase (c'est-à-dire **URI OAuth**).

Maintenant, vous êtes prêt à utiliser Google, Twitter, Github et Facebook comme fournisseurs d'authentification pour votre application web.

### Utiliser AngularFire dans votre application

Pour l'étape suivante, je vais utiliser une application Angular que j'ai échafaudée grâce à l'[Angular CLI officiel](https://github.com/angular/angular-cli).

Dans cette application, je vais utiliser les fournisseurs d'authentification que nous venons de configurer à l'étape précédente.

Voici à quoi ressemble l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wmQDx_-Q87Gr-nu9iFRXGg.png)

En cliquant sur un bouton, vous appellerez un fournisseur spécifique, authentifierez l'utilisateur et obtiendrez ses informations :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zgPhCyiM1Z93aWXD-u3__g.png)
_Utilisateur connecté avec github.com_

#### Installer et configurer angularfire2

Tout d'abord, nous devons installer les bibliothèques _firebase_ et _angularfire2_ :

```
$ npm install angularfire2 firebase --save
```

Ensuite, nous devons installer les types _Firebase_ :

```
$ npm install @types/firebase
```

Et ajouter ces types à votre fichier **src/tsconfig.json** :

```
{  "compilerOptions": {    "declaration": false,    "emitDecoratorMetadata": true,    "experimentalDecorators": true,    "lib": ["es6", "dom"],    "mapRoot": "./",    "module": "es6",    "moduleResolution": "node",    "outDir": "../dist/out-tsc",    "sourceMap": true,    "target": "es5",    "typeRoots": [      "../node_modules/@types"    ],    "types": [      "jasmine",      "firebase",      "node"    ]  }}
```

Un processus de configuration plus détaillé est décrit dans [la documentation officielle](https://github.com/angular/angularfire2/blob/master/docs/1-install-and-setup.md).

#### Configurer _AngularFire_ pour votre application

Afin d'utiliser Firebase avec Angular, nous devons fournir une configuration pour les services AngularFire.

Commençons par la configuration Firebase par défaut qui ressemble à ceci :

```
defaultFirebase({  apiKey: "AIzaSyCk3weREVFpOIN6pL_QVVNFRl3C3keMIRU",  authDomain: "angular2-auth.firebaseapp.com",  databaseURL: "https://angular2-auth.firebaseio.com",  storageBucket: "angular2-auth.appspot.com"})
```

_Note : Ne vous inquiétez pas de cette **apiKey** exposée. Cette clé est uniquement utilisée pour identifier les différents services de votre projet : une sorte d'identifiant de projet._

Vous pouvez obtenir votre **apiKey** Firebase, **projectId**, **databaseName** et **bucket ID** depuis le tableau de bord de votre application.

Cliquez sur le bouton **CONFIGURATION WEB** en haut à droite :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qzOQlZJtR6U9luzBDaVwrw.png)

Ensuite, pour notre cas d'utilisation, nous voulons fournir une méthode d'authentification par défaut :

```
firebaseAuthConfig({  method: AuthMethods.Popup})
```

Ici, nous choisissons d'utiliser une **fenêtre contextuelle** pour permettre à l'utilisateur de se connecter. Nous pourrions également utiliser une méthode de redirection comme ceci :

```
firebaseAuthConfig({  method: AuthMethods.Redirect})
```

Créons maintenant un _CoreModule_ dans **src/app/core.module.ts** où nous mettrons notre configuration. Il est considéré comme une bonne pratique de regrouper les dépendances principales dans un NgModule séparé nommé [CoreModule](https://angular.io/docs/ts/latest/guide/ngmodule.html#!#core-module). Voici un exemple d'un tel module :

```
import { BrowserModule } from '@angular/platform-browser';import { HttpModule } from '@angular/http';import { NgModule } from '@angular/core';import { FormsModule } from '@angular/forms';import {   AngularFireModule,   AuthMethods,   AuthProviders } from "angularfire2";
```

```
const firebaseConfig = {  apiKey: "AIzaSyCk3weREVFpOIN6pL_QVVNFRl3C3keMIRU",  authDomain: "angular2-auth.firebaseapp.com",  databaseURL: "https://angular2-auth.firebaseio.com",  storageBucket: "angular2-auth.appspot.com"};
```

```
@NgModule({  imports: [    BrowserModule,    FormsModule,    HttpModule,    AngularFireModule.initializeApp(firebaseConfig,{      provider: AuthProviders.Google,      method: AuthMethods.Popup    })  ],  exports: [    BrowserModule,  ]})export class CoreModule {}
```

#### Utilisation dans vos composants

Maintenant, nous sommes enfin prêts à implémenter la fonctionnalité d'authentification pour notre application Angular.

Nous devons injecter le service **AngularFire** dans le constructeur du composant :

```
import { Component } from '@angular/core';import { AngularFire, AuthProviders } from 'angularfire2';
```

```
@Component({  moduleId: module.id,  selector: 'app-root',  templateUrl: 'app.component.html',  styleUrls: ['app.component.css']})export class AppComponent {  user = {};
```

```
  constructor(    public af: AngularFire  ) {    this.af.auth.subscribe(user => {      if(user) {        // utilisateur connecté        this.user = user;      }      else {        // utilisateur non connecté        this.user = {};      }    });  }}
```

> Dans une application réelle, vous créeriez un service séparé qui gère l'authentification. Pensez au [principe de responsabilité unique](https://en.wikipedia.org/wiki/Single_responsibility_principle) et à [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Mais pour ce tutoriel, nous allons garder cela simple.

Le service **AngularFire** nous donne la propriété **auth** qui implémente l'API Observable. Cela signifie que nous devons nous abonner à cette propriété **auth** afin d'obtenir l'état d'authentification. Une valeur **NULL** signifie que l'utilisateur n'est pas connecté.

Ajoutons quelques boutons dans la vue du composant :

```
<button md-raised-button (click)="login()">  <img width="30" src="google-logo.png" />Utiliser mon compte Google</button><button md-raised-button (click)="logout()">  Déconnexion</button>
```

Nous allons utiliser ces boutons pour nous connecter et nous déconnecter, en utilisant le fournisseur Google comme exemple.

Dans **_app.component.ts_**, nous devons implémenter les méthodes **_login()_** et **_logout()_** :

```
login() {  this.af.auth.login({    provider: AuthProviders.Google  });} logout() {  this.af.auth.logout();}
```

Pour connecter un utilisateur, nous appelons la méthode **this.af.auth.login()** en utilisant le fournisseur Google, et **this.af.auth.logout()** pour déconnecter un utilisateur.

La méthode **AngularFire login()** a généralement besoin d'une méthode d'authentification. Dans notre cas, elle utilisera la méthode par défaut (c'est-à-dire **AuthMethods.Popup**) que nous avons configurée lors de la phase de démarrage.

Si vous devez remplacer la méthode d'authentification lors de l'appel de la méthode **login()**, fournissez simplement une nouvelle configuration d'authentification :

```
login() {  this.af.auth.login({    provider: AuthProviders.Google,    method: AuthMethods.Redirect  });}
```

Une fois que tout est configuré et fonctionne correctement, nous pouvons inspecter l'objet **_user_** contenant tous les jetons de session de l'utilisateur envoyés par Google (le fournisseur d'authentification) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mQcUhIAo_anodDNp_Z0tnQ.png)

Vous pouvez obtenir les informations de l'utilisateur telles que le **displayName** et le **photoURL** à partir de l'entrée **auth.provideData**.

C'est tout ! Vos utilisateurs peuvent maintenant se connecter en utilisant leurs comptes Google.

Vous pouvez ajouter Github et Facebook de manière similaire.

Voir l'application complète fonctionnelle [hébergée sur Firebase](https://angular2-auth.firebaseapp.com) ou lire le code source complet [sur Github](https://github.com/manekinekko/angular-firebase-authentication).

> NOTE : Je suis en train de migrer ce dépôt vers Angular final ([voir la branche](https://github.com/manekinekko/angular-firebase-authentication/tree/migration-to-angular-2.0.0)). Ce processus est en attente à cause de [ce problème](https://github.com/manekinekko/angular-firebase-authentication/issues/3) dans AngularFire2.

[**manekinekko/angular-firebase-authentication**](https://github.com/manekinekko/angular-firebase-authentication)  
[_angular-firebase-authentication - Une démonstration Angular des fournisseurs d'authentification Firebase_github.com](https://github.com/manekinekko/angular-firebase-authentication)

### Conseils et références

_Suivez [@manekinekko](https://twitter.com/manekinekko) pour en savoir plus sur la plateforme web._