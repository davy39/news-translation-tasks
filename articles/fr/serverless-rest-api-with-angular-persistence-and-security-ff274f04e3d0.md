---
title: Créons une API REST Serverless avec Angular, Persistance et Sécurité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-02T15:49:06.000Z'
originalURL: https://freecodecamp.org/news/serverless-rest-api-with-angular-persistence-and-security-ff274f04e3d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A3cp3Q48OLI3FxfafhbbvQ.png
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: Créons une API REST Serverless avec Angular, Persistance et Sécurité
seo_desc: 'By Bruno Krebs

  In this post I’ll show you how you can quickly build a serverless full stack app
  with static file hosting, a secure REST API, and a robust persistence layer.

  Here’s how we’ll manage all the moving parts:


  Identity management and securi...'
---

Par Bruno Krebs

Dans cet article, je vais vous montrer comment construire rapidement une application **full stack serverless** avec hébergement de fichiers statiques, une API REST sécurisée et une couche de persistance robuste.

Voici comment nous allons gérer toutes les parties mobiles :

* **Gestion de l'identité et sécurité** soutenues par [Auth0](https://auth0.com/?utm_source=freecodecamp&utm_medium=gp&utm_campaign=serverless_angular_app) et les JSON Web Tokens (JWT)
* **API REST Serverless** fournie par une application [Express](https://expressjs.com/) avec [Webtask](https://webtask.io/)
* **Couche de persistance** avec une base de données [MongoDB](https://www.mongodb.com/) hébergée par [mLab](https://mlab.com/)
* **Hébergement de fichiers statiques** via le déploiement sur [GitHub Pages](https://pages.github.com/)

Puisque cette application est assez simple en termes de fonctionnalités, il ne sera pas nécessaire d'exécuter MongoDB dans votre environnement local. Nous utiliserons mLab pendant le développement ainsi qu'en production. Les seuls outils que vous devrez installer sont [NodeJS et NPM](https://docs.npmjs.com/getting-started/installing-node).

Notre application aura les fonctionnalités suivantes :

* Connexion et déconnexion
* Liste affichant les tâches d'un utilisateur
* Formulaire permettant aux utilisateurs d'ajouter de nouvelles tâches
* Un bouton pour chaque tâche, permettant aux utilisateurs de supprimer ces tâches

### Création d'une nouvelle application Angular

Nous allons créer notre nouvelle application Angular avec [Angular CLI](https://github.com/angular/angular-cli). En fait, nous utiliserons cet outil tout au long du processus pour créer des composants/services et construire notre application pour la production.

Voici une liste de quelques commandes que nous devrons exécuter pour installer Angular CLI et créer le squelette de notre application :

```bash
# installer Angular CLI globalement
npm install -g @angular/cli

# créer le squelette
ng new task-list && cd task-list

# servir le squelette sur notre environnement de développement
ng serve
```

La dernière commande est responsable de l'emballage de notre application avec le profil de développement, et de la servir localement avec [Webpack Development Server](https://webpack.github.io/docs/webpack-dev-server.html). Après avoir exécuté toutes ces commandes, naviguez vers `http://localhost:4200/` pour la voir en fonctionnement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*evRKp0WZYFxlS5Rw.png)

### Sécurisation d'Angular avec Auth0

La première chose dont nous allons nous occuper dans notre application est la sécurité. La sécurité doit être une priorité absolue dans toute application qui gère des données sensibles tierces comme la liste de tâches que nous allons développer.

Pour commencer, [inscrivez-vous pour un compte Auth0 gratuit](https://auth0.com/?utm_source=freecodecamp&utm_medium=gp&utm_campaign=serverless_angular_app) et notez l'`ID Client` et le `Domaine`. Ces deux valeurs seront utilisées pour configurer [Lock](https://auth0.com/docs/libraries/lock) : un système de connexion intégrable.

**Important** : Auth0 nécessite une liste d'_URLs de rappel autorisées_. Cette liste contient toutes les URLs vers lesquelles Auth0 peut rediriger un utilisateur après avoir émis un JWT. Par conséquent, nous devons configurer au moins deux URLs : `http://localhost:4200/` et l'URL où notre application sera exposée, quelque chose comme : `https://brunokrebs.github.io/task-list/`. Cette URL sera définie lorsque nous publierons sur GitHub Pages.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_7yJK5iZyVOCmOw2.png)

Pour utiliser Lock, nous devons installer deux bibliothèques dans notre application : `auth0-lock` et `angular2-jwt`. Puisque nous utilisons TypeScript avec Angular, nous installerons également la bibliothèque `@types/auth0-lock`, qui fournit des définitions TypeScript pour Lock. De plus, puisque nous voulons offrir à nos utilisateurs une interface attrayante, nous allons installer [Angular Material](https://github.com/angular/material2). Ces dépendances sont installées avec les commandes suivantes :

```bash
# Dépendances d'exécution Auth0 Lock et Angular 2 JWT
npm install --save auth0-lock angular2-jwt @angular/material

# Définitions de types pour Auth0 Lock
npm install --save-dev @types/auth0-lock
```

Utilisons Angular CLI pour créer un `NavBarComponent`. Ce composant aura des boutons _Se connecter_ et _Se déconnecter_. Nous créerons également un `AuthService` qui sera responsable de la _connexion_, de la _déconnexion_ et de la validation si l'utilisateur est _authentifié_ ou non.

```bash
# génère les fichiers NavBarComponent sous src/app/nav-bar
ng g component nav-bar

# génère AuthService sous src/app/auth.service.ts
ng g service auth
```

Après avoir exécuté ces commandes, Angular CLI aura créé la structure de fichiers suivante :

```
src
  |-app
    |-nav-bar
      |-nav-bar.component.ts
      |-nav-bar.component.html
      |-nav-bar.component.css
    |-auth.service.ts
```

> _En fait, deux fichiers supplémentaires ont été créés : `src/app/auth.service.spec.ts` et `src/app/nav-bar/nav-bar.component.spec.ts`. Nous utiliserions ces fichiers pour écrire des tests pour le composant et le service. Cependant, pour des raisons de simplicité, nous n'aborderons pas les tests dans cet article. Vous pouvez consulter les références suivantes pour en savoir plus sur les tests dans Angular : [Angular 2 Testing In Depth: Services](https://auth0.com/blog/angular-2-testing-in-depth-services/) ; [Angular Testing](https://angular.io/docs/ts/latest/guide/testing.html) ; [Testing Components in Angular 2 with Jasmine](https://semaphoreci.com/community/tutorials/testing-components-in-angular-2-with-jasmine)_

Pour intégrer avec Lock, implémentons d'abord `src/app/auth.service.ts` avec le code suivant :

```ts
import { Injectable } from '@angular/core';
import Auth0Lock from 'auth0-lock';
import { tokenNotExpired } from 'angular2-jwt';

// À CORRIGER : remplacez ces valeurs par votre propre 'Client ID' et 'Domaine' Auth0
const AUTH0_CLIENT_ID = 'VOTRE_AUTH0_CLIENT_ID';
const AUTH0_DOMAIN = 'VOTRE_AUTH0_DOMAIN';

// c'est la clé du JWT dans le localStorage du navigateur
const ID_TOKEN = 'id_token';

@Injectable()
export class AuthService {
  lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {});

  constructor() {
    // écoute les événements 'authenticated'
    this.lock.on('authenticated', (authResult) => {
      localStorage.setItem(ID_TOKEN, authResult.idToken);
    });
  }

  signIn() { this.lock.show(); }

  signOut() { localStorage.removeItem(ID_TOKEN); }

  authenticated() { return tokenNotExpired(); }
}
```

Dans le code ci-dessus, il y a trois choses qui méritent d'être mentionnées. Premièrement, nous devons remplacer `AUTH0_CLIENT_ID` et `AUTH0_DOMAIN` par les valeurs que nous avons notées précédemment. Deuxièmement, `ID_TOKEN` fait référence à la clé où le JWT sera sauvegardé (dans le `localStorage` du navigateur de l'utilisateur). Et troisièmement, le constructeur de ce service ajoute un écouteur de rappel à l'événement `authenticated` sur Lock. Cet écouteur sauvegarde le token émis par Auth0 dans `localStorage`. Pour déconnecter un utilisateur, il suffit de supprimer ce token du `localStorage`.

Notre classe `AuthService` est prête, mais contrairement aux `composants`, Angular CLI n'ajoute pas les `services` à notre définition `@NgModule` par défaut. Pour ce faire, ouvrez le fichier `src/app/app.module.ts`, ajoutez ce `service` en tant que `provider` et ajoutez Angular Material dans le tableau `imports` :

```ts
// ... autres imports
import { AuthService } from './auth.service';
import { MaterialModule } from '@angular/material';

@NgModule({
  // ... autres propriétés
  imports: [
      // ... autres imports
      MaterialModule.forRoot(),
  ],
  providers: [ AuthService ],
  // ... autres propriétés
})
export class AppModule { }
```

Nous pouvons maintenant nous concentrer sur l'implémentation de notre `NavBarComponent`. Tout d'abord, nous allons injecter `AuthService` et ajouter trois méthodes publiques qui seront utilisées par notre interface HTML. Ensuite, nous implémenterons l'interface et ajouterons quelques règles CSS pour l'améliorer.

Ouvrons le fichier `src/app/nav-bar/nav-bar.component.ts` et implémentons le code suivant :

```ts
import { Component } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {
  constructor(private authService: AuthService) { }
}
```

Ce composant se contente d'injecter `AuthService` et rien d'autre. Injecter un service de cette manière permet à l'interface utilisateur d'appeler ses méthodes, comme nous le verrons. Maintenant, ouvrons `src/app/nav-bar/nav-bar.component.html` et implémentons-le comme suit :

```html
<md-toolbar color="primary">
  <span>Liste de tâches</span>
  <span class="fill-space"></span>
  <button md-button (click)="authService.signIn()" *ngIf="!authService.authenticated()">Se connecter</button>
  <button md-button (click)="authService.signOut()" *ngIf="authService.authenticated()">Se déconnecter</button>
</md-toolbar>
```

Notre `NavBar` expose le titre de notre application ainsi que deux boutons. À tout moment, un seul bouton est vraiment visible pour l'utilisateur. Le bouton _Se connecter_ sera visible lorsque l'utilisateur n'est pas encore `authentifié` et le bouton _Se déconnecter_ sera visible dans le cas contraire. Pour améliorer notre interface, nous avons également ajouté un élément `span.fill-space`. Cet élément sera responsable de pousser les deux boutons vers la bordure droite. Pour y parvenir, nous devons ajouter la règle CSS suivante au fichier `src/app/nav-bar/nav-bar.component.css` :

```css
.fill-space {
  flex: 1 1 auto;
}
```

Bien, nous avons maintenant à la fois le `NavBarComponent` et le `AuthService` entièrement implémentés et intégrés. Mais nous devons encore ajouter ce composant à notre fichier `src/app/app.component.html`, sinon il ne sera jamais rendu. Pour ce faire, remplacez simplement le contenu de ce fichier par la ligne de code suivante :

```html
<app-nav-bar></app-nav-bar>
```

Si nous exécutons notre application maintenant, elle n'aurait pas l'air soignée car la plupart des navigateurs principaux ont une marge de `8px` sur les éléments `body` et parce que nous n'avons pas configuré de [Thème Angular Material](https://github.com/angular/material2/blob/master/guides/theming.md). Nous allons corriger ces deux problèmes en mettant à jour notre fichier `src/styles.css` pour qu'il ressemble à ceci :

```css
@import '~@angular/material/core/theming/prebuilt/indigo-pink.css';

body {
  margin: 0;
}
```

Nous sommes maintenant prêts à partir, alors démarrons notre serveur de développement en exécutant `ng serve`, et dirigeons-nous vers `http://localhost:4200` pour voir comment les choses se présentent. Vous pouvez même vous _connecter_ et vous _déconnecter_, bien qu'il n'y ait pas grand-chose à voir.

![Image](https://cdn-media-1.freecodecamp.org/images/0*aLUpSGtTvWlx1ut-.png)

### Ajout d'un message de bienvenue pour les visiteurs

Pour faire de notre application un endroit convivial, ajoutons un message de bienvenue. Pour ce faire, nous allons d'abord ajouter deux méthodes et injecter `AuthService` dans le fichier `src/app/app.component.ts`, pour qu'il ressemble à ceci :

```ts
import { Component } from '@angular/core';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private authService: AuthService) { }
}
```

Après cela, nous allons ajouter le message, en tant que composant `md-card` de [Angular Material](https://material.angular.io/components/component/card), à `src/app/app.component.html` :

```html
<app-nav-bar></app-nav-bar>

<div class="app-container">
  <md-card *ngIf="!authService.authenticated()">
    <md-card-title>Bonjour, visiteur.</md-card-title>
    <md-card-subtitle>
      Veuillez <a (click)="authService.signIn()">vous connecter</a> pour gérer votre liste de tâches.
    </md-card-subtitle>
  </md-card>
</div>
```

Et enfin, nous allons apporter une correction à l'interface en ajoutant une règle à `src/app/app.component.css` :

```css
.app-container {
  padding: 20px;
}
```

En nous rendant dans notre application, `http://localhost:4200/`, nous pouvons voir notre nouveau message de bienvenue (si nous ne sommes pas authentifiés).

![Image](https://cdn-media-1.freecodecamp.org/images/0*6QrGe-la8oqzP1eQ.png)

### Implémentation de l'API REST Serverless

Maintenant que notre application est intégrée avec Auth0, ce qui permet à nos utilisateurs de se connecter et de se déconnecter, créons notre API REST serverless. Cette API gérera les requêtes `POST` (pour persister de nouvelles tâches), les requêtes `GET` (pour récupérer les tâches d'un utilisateur) et les requêtes `DELETE` (pour supprimer des tâches).

Nous allons d'abord créer un fichier appelé `tasks.js` dans un nouveau dossier appelé `webtask`, puis nous ajouterons le code suivant :

```js
'use strict';
// imports des modules node
const express = require('express');
const mongojs = require('mongojs');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');

// crée une application Express avec un analyseur de corps JSON
const app = new express();
app.use(bodyParser.json());

// définit l'API REST (méthodes HTTP)
app.get('/', getTasks);
app.post('/', addTask);
app.delete('/', deleteTask);

// exporte l'API REST
module.exports = app;

function addTask(req, res) {
  let userCollection = loadUserCollection(req.webtaskContext);
  
  // sauvegarde la nouvelle tâche dans la collection de l'utilisateur
  userCollection.save({
    createdAt: new Date(),
    description: req.body.description
  }, () => res.end())
}

function getTasks(req, res) {
  let userCollection = loadUserCollection(req.webtaskContext);
  
  // récupère toutes les tâches en triant par date de création décroissante
  userCollection.find().sort({ createdAt: -1 }, (err, data) => {
    res.status(err ? 500 : 200).send(err || data);
  });
}

function deleteTask(req, res) {
  let userCollection = loadUserCollection(req.webtaskContext);
  
  // supprime une tâche basée sur son id
  userCollection.remove({ _id: mongojs.ObjectId(req.query.id) }, () => res.end());
}

function loadUserCollection(webtaskContext) {
  // ces secrets sont configurés lors de la création de la Webtask
  const AUTH0_SECRET = webtaskContext.secrets.AUTH0_SECRET;
  const MONGO_USER = webtaskContext.secrets.MONGO_USER;
  const MONGO_PASSWORD = webtaskContext.secrets.MONGO_PASSWORD;
  const MONGO_URL = webtaskContext.secrets.MONGO_URL;
  
  // supprime le préfixe 'Bearer ' qui vient dans l'en-tête d'autorisation,
  let authorizationHeader = webtaskContext.headers.authorization;
  authorizationHeader = authorizationHeader.replace('Bearer ', '');
  
  // vérifie l'authenticité du token
  let token = jwt.verify(authorizationHeader, AUTH0_SECRET);
  
  // se connecte à MongoDB et retourne la collection de l'utilisateur
  let mongodb = mongojs(`${MONGO_USER}:${MONGO_PASSWORD}@${MONGO_URL}`);
  return mongodb.collection(token.sub);
}
```

Le code est assez simple et facile à comprendre, mais une explication générale pourrait être utile. Le but principal de ce fichier est d'exporter une [application Express](https://expressjs.com/en/starter/hello-world.html) qui gère trois méthodes HTTP pour une seule route, la route principale `/`. Ces trois méthodes, comme expliqué précédemment, permettent aux utilisateurs de créer, récupérer et supprimer des tâches à partir de collections dans une base de données MongoDB.

Chaque utilisateur aura sa propre collection — ce n'est pas la meilleure approche, puisque [MongoDB peut gérer un maximum de 24 000 collections](https://docs.mongodb.com/manual/reference/limits/#namespaces), mais c'est suffisant pour commencer. Cette collection est basée sur la revendication `sub`, [qui identifie l'utilisateur](https://tools.ietf.org/html/rfc7519#section-4.1.2), présente dans le JWT émis par Auth0.

La dernière définition de fonction dans le fichier `tasks.js`, `loadUserCollection`, est en fait responsable de deux choses : la sécurité et la connexion à MongoDB. Lorsqu'un utilisateur émet une requête à notre API, la fonction vérifie si l'en-tête `authorization` envoyé a été signé par Auth0. Si aucun n'est envoyé, une erreur non conviviale est générée. Cela est fait via la fonction `jwt.verify` avec l'aide de la clé `AUTH0_SECRET`. La deuxième responsabilité, la connexion à MongoDB, est gérée par le module `mongojs` et dépend de trois variables de configuration : `MONGO_USER`, `MONGO_PASSWORD`, `MONGO_URL`.

Toutes ces variables de configuration — trois pour se connecter à MongoDB et une pour vérifier les tokens Auth0 — sont passées à Webtask lors de la création de la fonction serverless. Nous verrons comment cela se fait bientôt.

C'est l'**implémentation complète de l'API REST**, avec ce code nous sommes prêts à gérer les requêtes des utilisateurs qui seront envoyées par les composants que nous allons créer dans notre application Angular. Mais il y a encore quelques étapes que nous devons effectuer.

### Création d'une base de données MongoDB

Pour nous faciliter la vie et éviter d'avoir à installer et supporter MongoDB nous-mêmes, nous allons utiliser [mLab](https://mlab.com/), un MongoDB hébergé dans le cloud. La première chose que nous devons faire est de [nous rendre sur leur site web](https://mlab.com/) et de nous inscrire pour un compte gratuit. Après avoir vérifié notre adresse e-mail, nous devons [créer un nouveau déploiement](https://mlab.com/create). Puisque nous commençons notre application et que nous n'aurons pas beaucoup de trafic, choisissons le plan **_Single Node_** et le type **_Sandbox_**, qui nous offre 500 Mo de stockage de base de données gratuitement. Vous devrez également saisir un nom de base de données, choisissez quelque chose comme `task-list`.

La dernière chose que nous devrons faire est de créer un utilisateur pour se connecter à cette base de données. Si vous choisissez `task-list` comme nom de votre base de données, [voici le lien pour créer des utilisateurs](https://mlab.com/databases/task-list#users).

![Image](https://cdn-media-1.freecodecamp.org/images/0*f2RlcfJs2OzL0Hr5.png)

### Configuration du compte Webtask

Nous devrons également créer un [compte Webtask](https://webtask.io/), mais cela est aussi facile que possible. Webtask, étant un produit d'Auth0, repose sur Lock et nous permet de créer un compte avec l'un des fournisseurs d'identité (IdP) suivants : Facebook, GitHub, Google ou Microsoft. Il suffit de cliquer sur un bouton pour créer un compte.

Après avoir choisi un IdP, nous sommes présentés avec un processus succinct en trois étapes démontrant comment créer une fonction serverless _Hello World_. Nous avons déjà une Webtask à déployer, alors suivons seulement les deux premières étapes afin de configurer l'outil CLI sur notre ordinateur :

```bash
# installer l'outil CLI Webtask
npm install wt-cli -g

# l'initialiser avec notre adresse e-mail
wt init moi@quelquepart.com
```

Vous serez invité à entrer le code de vérification qui a été envoyé à votre adresse e-mail. C'est l'étape finale de la configuration du compte Webtask.

### Déploiement de notre API REST Serverless

Avec les comptes mLab et Webtask créés et l'outil CLI Webtask correctement configuré, nous pouvons maintenant déployer notre API REST serverless en production. Cela se fait avec le code suivant :

```bash
wt create webtask/tasks.js \
  --meta wt-compiler=webtask-tools/express \
  -s AUTH0_SECRET=secret-from-auth0.com \
  -s MONGO_USER=task-list-user \
  -s MONGO_PASSWORD=111222 \
  -s MONGO_URL=ds147069.mlab.com:47069/task-list \
  --prod
```

La première option passée à l'outil `wt` spécifie que nous voulons `créer` une Webtask basée sur notre fichier `webtask/tasks.js`. Le deuxième paramètre identifie notre code comme étant une application Express, qui doit être pré-compilée par Webtask avec l'aide de l'outil `webtask-tools/express`. Les quatre paramètres suivants sont les `secrets` que nous utilisons dans notre Webtask (le préfixe `-s` les désigne comme `secrets`). Le dernier paramètre crée notre Webtask en mode `production`, ce qui la rend plus rapide.

Soyez conscient que les valeurs ci-dessus doivent être remplacées par des valeurs provenant de notre compte Auth0 et de notre compte mLab. La valeur `AUTH0_SECRET` peut être trouvée au même endroit que l'`ID Client` et le `Domaine`. Et les trois dernières valeurs, liées à MongoDB, peuvent être trouvées sur le tableau de bord de mLab.

Ayant réussi à émettre la commande de création de Webtask, nous pouvons maintenant nous concentrer sur la fonctionnalité principale de notre application Angular, le composant de liste de tâches.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9uq7DErARs8qBz7d.png)

### Construction de notre interface Angular

Il y a deux composants que nous devrons créer pour permettre aux utilisateurs d'interagir avec leurs listes de tâches. Nous créerons un `TaskListComponent`, pour exposer la liste de tâches, et un `TaskFormComponent`, qui permettra à l'utilisateur de créer de nouvelles tâches. En plus de ces composants, nous créerons un `TaskListService` qui gérera toutes les requêtes AJAX. Nous utiliserons Angular CLI pour les créer :

```bash
# crée le composant principal qui liste les tâches
ng g component task-list

# crée un composant pour contenir un formulaire pour ajouter des tâches
ng g component task-list/task-form

# crée un service pour gérer toutes les interactions avec notre API REST
ng g service task-list/task-list
```

### Intégration d'Angular avec l'API REST Serverless

Les composants `TaskListComponent` et `TaskFormComponent` dépendront tous deux de `TaskListService` pour communiquer avec notre API REST serverless, alors traitons d'abord l'implémentation du service.

Ouvrez le fichier de service nouvellement créé, `src/app/task-list/task-list.service.ts`, et insérez le code suivant :

```ts
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthHttp } from 'angular2-jwt';

@Injectable()
export class TaskListService {
  private static TASKS_ENDPOINT =
    'https://wt-e1870b8a73b27cdee73c468b8c8e3bc4-0.run.webtask.io/tasks';

  constructor(private authHttp: AuthHttp) { }

  loadTasks$(): Observable<any> {
    return this.authHttp.get(TaskListService.TASKS_ENDPOINT);
  }
    
  addTask$(task) : Observable<any> {
    return this.authHttp.post(TaskListService.TASKS_ENDPOINT,
      { description: task });
  }
    
  deleteTask$(task): Observable<any> {
    return this.authHttp.delete(TaskListService.TASKS_ENDPOINT +
      '?id=' + task._id);
  }
}
```

Il y a trois choses importantes à noter dans ce code. Premièrement, la constante `TASKS_ENDPOINT`. Cette constante doit référencer l'_URL_ retournée par la commande `wt create` ci-dessus.

Deuxièmement, cette classe n'utilise pas `Http` de `@angular/http`. Elle utilise `AuthHttp`, qui est fourni par `angular2-jwt` et qui s'intègre harmonieusement avec `auth0-lock`. Les instances de cette classe envoient automatiquement un en-tête `authorization` avec tout contenu qu'elles trouvent sur la clé `id_token` dans le `localStorage` du navigateur de l'utilisateur. Comme vous l'avez peut-être remarqué, c'est le même endroit où nous avons stocké les tokens lors de la configuration de `AuthService`.

Troisièmement, toutes les méthodes de `TaskListService` retournent des `Observables`, laissant à l'appelant le soin de décider quoi faire avec la réponse envoyée par notre API REST serverless.

Pour injecter `TaskListService` dans nos composants, nous devons apporter quelques modifications à notre `@NgModule` principal, situé dans `src/app/app.module.ts` :

```ts
// ... autres imports
import { Http, RequestOptions } from '@angular/http';
import { AuthHttp, AuthConfig } from 'angular2-jwt';
import { TaskListService } from './task-list/task-list.service';

// crée une factory pour AuthHttp
export function authHttpFactory(http: Http, options: RequestOptions) {
  return new AuthHttp(new AuthConfig(), http, options);
}

@NgModule({
    // ... autres propriétés
    providers: [
      AuthService,
      TaskListService, // ajoute un nouveau service
      {
        provide: AuthHttp,
        useFactory: authHttpFactory, // définit comment fournir AuthHttp
        deps: [ Http, RequestOptions ]
      }
    ],
    bootstrap: [AppComponent]
})
```

La première modification que nous avons apportée à notre module a été d'ajouter `TaskListService` en tant que fournisseur, comme nous l'avons fait précédemment avec `AuthService`. La deuxième modification a également ajouté un fournisseur, mais sous une forme plus complexe.

Le fournisseur `AuthHttp` avait besoin de l'aide d'une factory - déclarée sous le nom de `authHttpFactory` - pour être créé. Cette factory a `Http` et `RequestOptions` comme dépendances, donc nous avons dû définir le fournisseur sous forme d'objet littéral, en passant ces dépendances explicitement.

### Liste des tâches avec Angular

Notre `TaskListComponent` peut maintenant être implémenté. Nous allons maintenant ouvrir le fichier `src/app/task-list/task-list.component.ts` et appliquer le code ci-dessous :

```ts
import { Component, OnInit } from '@angular/core';
import { TaskListService } from './task-list.service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: [ './task-list.component.css' ]
})
export class TaskListComponent implements OnInit {

  private tasks: String[];

  constructor(private taskListService: TaskListService) { }

  ngOnInit() { this.loadTasks(); }

  private loadTasks() {
    this.taskListService.loadTasks$().subscribe(
      response => this.tasks = response.json(),
      error => console.log(error)
    );
  }

  taskAddedHandler(task) {
    this.taskListService.addTask$(task).subscribe(
      response => this.loadTasks(),
      error => console.log()
    );
  }

  deleteTask(task) {
    this.taskListService.deleteTask$(task).subscribe(
      response => this.loadTasks(),
      error => console.log()
    );
  }
}
```

Cette classe injecte `TaskListService` et ajoute quelques méthodes de rappel aux réponses des `Observables`. Les méthodes `taskAdded$` et `deleteTask$` déclenchent toutes deux un appel à la méthode `loadTasks` lorsque les `Observables` répondent sans erreur. `console.log` est déclenché par ces méthodes pour gérer les cas où des erreurs sont émises par l'API REST serverless.

La méthode `loadTasks` appelle `taskListService.loadTasks$` pour assigner le résultat à la propriété `tasks`.

Avec les trois méthodes exposées et la propriété `task` remplie, nous pouvons maintenant implémenter l'interface `TaskListComponent`, qui se trouve dans le fichier `src/app/task-list/task-list.component.html`.

Voici à quoi ce fichier devrait ressembler :

```html
<md-card>
  <md-card-title>Liste de tâches</md-card-title>
  <md-card-subtitle>Toutes vos tâches en un seul endroit.</md-card-subtitle>
  <md-list>
    <div class="task-item" *ngFor="let task of tasks; trackBy: $index">
      <p><small><strong>{{ task.createdAt | date: 'short' }}</strong></small></p>
      <p>{{ task.description }}</p>
      <button class="delete" md-button md-raised-button
        color="accent" (click)="deleteTask(task)">Supprimer</button>
    </div>
    <div class="task-item" *ngIf="tasks?.length == 0">
      <p>Vous n'avez aucune tâche en attente.</p>
    </div>
  </md-list>
</md-card>
```

Ici, nous avons ajouté un composant `md-list`, [fournis par Angular Material](https://material.angular.io/components/component/list), qui itère à travers les `tasks`, montrant leur date de création et leur description. De plus, chaque tâche a obtenu un `button` qui permet aux utilisateurs de les supprimer.

Pour améliorer notre interface, ajoutons deux règles CSS au fichier `src/app/task-list/task-list.component.css` :

```css
.task-item {
  padding: 10px;
  margin-bottom: 10px;
  background-color: #eee;
}

button.delete {
  float: right;
  top: -60px;
}
```

Cela rendra les différentes tâches distinguables avec une couleur de fond grise, et poussera le bouton de suppression vers la droite, en l'alignant verticalement avec la tâche.

Notre interface est maintenant prête à lister les tâches, nous devons donc la rendre visible en l'ajoutant au fichier `src/app/app.component.html`. Ouvrez-le et ajoutez le `TaskListComponent` comme suit :

```html
<app-nav-bar></app-nav-bar>

<div class="app-container">
  
  <!-- ... carte avec message de bienvenue -->
  
  <app-task-list *ngIf="authService.authenticated()"></app-task-list>
</div>
```

Si nous ouvrons notre application dans un navigateur, en accédant à `http://localhost:4200`, nous verrions l'écran suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4y2oA65Iy07IW6ET.png)

L'achèvement de notre application dépend maintenant de l'implémentation du dernier composant, `TaskFormComponent`, pour permettre aux utilisateurs d'ajouter des tâches à leurs listes.

### Ajout de tâches avec Angular

Pour permettre à un utilisateur d'ajouter des tâches, nous devons ouvrir le fichier `src/app/task-list/task-form/task-form.component.ts` et l'implémenter comme suit :

```ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-task-form',
  templateUrl: './task-form.component.html',
  styleUrls: ['./task-form.component.css']
})
export class TaskFormComponent {

  @Output()
  taskAdded = new EventEmitter();

  public task: String = null;

  addTask() {
    this.taskAdded.emit(this.task);
    this.task = null;
  }
}
```

Ce composant accepte une entrée de tâche de l'utilisateur et émet un événement `taskAdded` avec les données. Le HTML de ce composant, situé dans le fichier `src/app/task-list/task-form/task-form.component.html`, est également très simple :

```html
<div class="task-form">
  <md-input-container>
    <input mdInput [(ngModel)]="task" placeholder="Nouvelle tâche">
  </md-input-container>
  <button md-button md-raised-button color="primary" (click)="addTask()">Ajouter</button>
</div>
```

Lorsque vous cliquez dessus, le bouton _Ajouter_ déclenche la méthode `addTask` dans le composant. Cette méthode déclenche ensuite l'émetteur d'événements `taskAdded`. `TaskListComponent` est le composant qui écoutera ces événements. Nous avons déjà implémenté une méthode, appelée `taskAdded`, qui peut gérer de tels événements. Nous devons simplement mettre à jour le HTML de ce composant pour ajouter `TaskFormComponent` et enregistrer le gestionnaire d'événements.

Pour ce faire, ouvrons `src/app/task-list/task-list.component.html` et ajoutons la balise `app-task-form` juste avant notre liste, comme suit :

```html
<md-card>
  <!-- ... titre et sous-titre de la carte -->
  
  <app-task-form (taskAdded)="taskAddedHandler($event)"></app-task-form>
  
  <!-- ... md-list -->
</md-card>
```

Et voilà. Notre application est maintenant entièrement implémentée et prête à être mise en production.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NnU0RUSzJkBgmtHX.png)

Ou l'est-elle ? Si nous jouons un peu avec l'application, nous verrons que dans certaines conditions, l'expérience utilisateur n'est pas si bonne. L'application prend un certain temps à mettre à jour la liste des tâches lorsqu'une nouvelle tâche est ajoutée ou qu'une tâche existante est supprimée. Il y a donc place à l'amélioration.

### Ajout d'un indicateur de chargement AJAX

Pour résoudre ce problème, utilisons un petit module appelé [Angular 2 Slim Loading Bar](https://github.com/akserg/ng2-slim-loading-bar). Pour l'installer, exécutez `npm install --save ng2-slim-loading-bar` puis ouvrez le fichier `src/app/app.module.ts` pour l'importer :

```ts
// ... autres imports de modules
import { SlimLoadingBarModule } from 'ng2-slim-loading-bar';

@NgModule({
  // ... déclarations
  imports: [
    // ... autres imports
    SlimLoadingBarModule.forRoot()
  ],
  // ... fournisseurs et bootstrap
})
export class AppModule { }
```

Nous importerons également ses règles CSS en ajoutant la ligne suivante en haut de notre fichier `src/styles.css` :

```css
@import '~ng2-slim-loading-bar/bundles/style.css';

/* ... tout le reste ... */
```

Après cela, nous devons faire en sorte que notre `AppComponent` utilise `SlimLoadingBarService`. Pour ce faire, ouvrons `src/app/app.component.ts` et éditons comme suit :

```ts
// ... autres imports
import { SlimLoadingBarService } from 'ng2-slim-loading-bar';

// ... définition du composant
export class AppComponent {
  constructor(private authService: AuthService, private slimLoading: SlimLoadingBarService) { }

  // ... définitions de méthodes
}
```

`SlimLoadingBarService` contient deux méthodes que nous allons utiliser : `start`, qui démarre la barre de chargement ; et `complete`, qui termine l'indicateur de chargement. Ces méthodes seront enregistrées en tant qu'écouteurs d'événements sur `TaskListComponent`. Nous n'avons pas encore créé d'émetteurs d'événements dans ce composant, mais nous pouvons configurer les écouteurs à l'avance. Ouvrons `src/app/app.component.html` et éditons comme ceci :

```html
<app-nav-bar></app-nav-bar>

<div class="app-container">
  <!-- ... message de bienvenue ... -->
  
  <app-task-list *ngIf="authService.authenticated()"
    (startAjaxRequest)="slimLoading.start()"
    (completeAjaxRequest)="slimLoading.complete()">
  </app-task-list>
</div>

<!-- ajoute la barre de chargement slim à notre application -->
<ng2-slim-loading-bar [color]="'gold'" [height]="'4px'"></ng2-slim-loading-bar>
```

La dernière chose que nous devrons faire est d'éditer le fichier `src/app/task-list/task-list.component.ts` pour créer et utiliser les émetteurs d'événements `startAjaxRequest` et `completeAjaxRequest` sur `TaskListComponent` :

```ts
// ... autres imports
import { EventEmitter, Output } from '@angular/core';

// ... définition du composant
export class TaskListComponent implements OnInit {

  @Output()
  startAjaxRequest = new EventEmitter<void>();
    
  @Output()
  completeAjaxRequest = new EventEmitter<void>();
    
  // ... propriétés, constructeur et définitions ngOnInit
    
  private loadTasks() {
    this.startAjaxRequest.emit();
    this.taskListService.loadTasks$().subscribe(
      response => this.tasks = response.json(),
      error => console.log(error),
      () => this.completeAjaxRequest.emit()
    );
  }
    
  taskAddedHandler(task) {
    this.startAjaxRequest.emit();
    this.taskListService.addTask$(task).subscribe(
      response => this.loadTasks(),
      error => console.log()
    );
  }
    
  deleteTask(task) {
    this.startAjaxRequest.emit();
    this.taskListService.deleteTask$(task).subscribe(
      response => this.loadTasks(),
      error => console.log()
    );
  }
}
```

Ici, nous avons créé les deux émetteurs d'événements et les avons ajoutés aux trois méthodes qui dépendent des requêtes AJAX. Chaque fois que l'une de ces méthodes est appelée, nous émettons un événement, via `this.startAjaxRequest.emit()`, pour faire démarrer l'indicateur de barre de chargement de la _Slim Loading Bar_. Après avoir reçu une réponse des requêtes AJAX envoyées par la méthode `loadTasks`, qui met à jour la liste des tâches, nous disons à la _Slim Loading Bar_ de compléter sa progression via `this.completeAjaxRequest.emit()`.

Si nous exécutons notre serveur de développement en émettant `ng serve` et en nous rendant à `http://localhost:4200/`, nous verrons notre application avec une meilleure expérience utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/0*-AfS8WmTmcgGrgPZ.png)

### Mise en ligne avec GitHub Pages

Notre application est prête à être déployée en production. Nous avons une couche de persistance qui sauvegarde toutes les tâches des utilisateurs. Nous avons une API REST serverless qui accepte les requêtes `GET`, `POST` et `DELETE` pour manipuler les tâches. Nous avons la sécurité, fournie par Auth0. Et nous avons une interface d'application Angular à page unique attrayante. La seule chose qui manque est un endroit pour héberger nos fichiers statiques (HTML, CSS et JavaScript).

C'est exactement ce que [GitHub Pages fournit](https://pages.github.com/). Pour l'utiliser, c'est simple. Nous devons simplement créer un dépôt et pousser notre travail vers une branche appelée `gh-pages`. Cette branche doit contenir uniquement nos bundles de production.

Pour créer un dépôt GitHub, allez sur [GitHub](https://github.com/), connectez-vous (ou inscrivez-vous si vous n'avez pas de compte) et choisissez l'option _Créer un nouveau dépôt_. Créez votre nouveau dépôt en le nommant _task-list_. Notez que si vous choisissez un autre nom, vous devrez ajuster le paramètre `base-href` de la commande `ng build` que nous exécuterons plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/0*920F4HsTnQBsRlvi.png)

Maintenant, nous devons ajouter ce dépôt comme un dépôt distant à notre application. Lorsque nous avons créé notre projet avec Angular CLI, il est déjà venu avec [Git](https://git-scm.com/). Nous devons simplement ajouter ce dépôt distant, valider toutes nos modifications et pousser vers sa branche principale :

```bash
# ajoute le nouveau dépôt comme un dépôt distant
git remote add origin git@github.com:VOTRE-UTILISATEUR/VOTRE-DEPOT.git

# valide notre code
git add .
git commit -m "Application Angular de liste de tâches avec une API REST serverless sécurisée."

# pousse le travail vers le nouveau dépôt
git push origin master
```

Ayant notre code en sécurité, nous pouvons maintenant travailler sur la tâche de _mise en ligne_. Deux étapes sont nécessaires ici. La première consiste à préparer notre code pour la production et à le packager. Encore une fois, Angular CLI est pratique. Pour ce faire, nous devons simplement émettre `ng build --prod --base-href=/task-list/`. Notez que nous devons définir `base-href` exactement au même nom que notre dépôt GitHub, sinon notre application ne pourra pas charger toutes les ressources et ne fonctionnera pas.

La deuxième étape était auparavant gérée par Angular CLI, mais [cette commande a été supprimée dans la dernière version](https://github.com/angular/angular-cli/pull/4385), donc nous aurons besoin d'un outil tiers pour nous aider ici. Heureusement, il y en a un qui est très facile à utiliser appelé `angular-cli-ghpages`. Pour l'installer, émettez `npm install -g angular-cli-ghpages`. Après cela, nous devons simplement exécuter `angular-cli-ghpages` (oui, sans aucun paramètre) et voilà. Notre application est en ligne et fonctionne sur GitHub Pages.

**Important** : n'oubliez pas de mettre à jour les _URLs de rappel autorisées_ sur votre compte Auth0. La liste des URLs autorisées doit contenir l'URL où notre application a été exposée. Cela devrait être quelque chose comme `[https://brunokrebs.github.io/task-list/](https://brunokrebs.github.io/task-list/.)`[.](https://brunokrebs.github.io/task-list/.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*0Z-c16AXocwouEsI.png)

### Conclusion

Comme nous avons pu le voir, lorsque nous choisissons les bons outils, il devient facile d'accomplir de grandes choses. Nous avons commencé avec rien, juste une idée de développer une application de liste de tâches, et nous avons réussi à la créer et à la publier sur Internet sans trop d'efforts.

Nous n'avons même pas eu à nous soucier de construire, supporter et sécuriser des serveurs pour héberger notre application web ou notre base de données. Si nous avions dû gérer ces tâches nous-mêmes, nous aurions pris beaucoup plus de temps et nous ne serions pas aussi confiants quant à la sécurité, la tolérance aux pannes et la scalabilité de notre application.

Et ce n'est qu'un début. Nous libérer de tous ces problèmes nous permet de nous concentrer à 100 % sur nos idées et sur ce qui rend nos applications uniques.

> J'adore lire et écrire sur le développement, principalement JavaScript et Java. Si vous voulez partager quelque chose avec moi, ou voulez rester à l'écoute, vous pouvez me rejoindre sur [Twitter](https://twitter.com/brunoskrebs/). De plus, n'hésitez pas à ajouter des commentaires ici ou dans l'un de mes articles.