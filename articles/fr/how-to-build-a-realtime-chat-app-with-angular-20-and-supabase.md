---
title: Comment créer une application de chat en temps réel avec Angular 20 et Supabase
subtitle: ''
author: deji adesoga
co_authors: []
series: null
date: '2025-06-16T21:48:44.790Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-chat-app-with-angular-20-and-supabase
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750094888966/7ac31fee-bd4d-4353-b8cb-911ac60b4516.png
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
- name: supabase
  slug: supabase
- name: Frontend Development
  slug: frontend-development
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de chat en temps réel avec Angular 20 et
  Supabase
seo_desc: Chat applications let you talk in real-time with your friends, family, or
  coworkers, and help you quickly, effectively, and efficiently transfer of information.
  When you’re building modern web applications, chat applications are now pretty much
  a req...
---

Les applications de chat vous permettent de discuter en temps réel avec vos amis, votre famille ou vos collègues, et aident à transférer rapidement, efficacement et de manière efficace des informations. Lorsque vous construisez des applications web modernes, les applications de chat sont désormais pratiquement une exigence pour permettre la collaboration et améliorer l'expérience utilisateur.

Dans ce tutoriel, nous allons décomposer comment construire une application de chat en utilisant des technologies modernes comme Angular et Supabase. La construction de cette application de chat vous aidera à apprendre des fonctionnalités telles que Google OAuth 2.0 pour l'authentification, Angular router pour la navigation, le garde de route `CanActivate` pour la protection des routes, et comment appeler les fonctions Supabase pour créer, récupérer et supprimer des chats.

Sur le backend, vous apprendrez à créer des tables de base de données dans Supabase. Vous en apprendrez également sur les fonctions Supabase et les déclencheurs Supabase.

## **Table des matières**

* [Table des matières](#heading-table-des-matieres)
    
* [Prérequis](#heading-prealables)
    
* [Installations et configuration du compte](#heading-installations-et-configuration-du-compte)
    
* [Comment créer l'interface utilisateur de l'application Angular](#heading-comment-creer-linterface-utilisateur-de-lapplication-angular)
    
* [Comment configurer un nouveau projet Supabase](#heading-comment-configurer-un-nouveau-projet-supabase)
    
* [Comment configurer Google OAuth 2.0 pour l'authentification et l'autorisation](#heading-comment-configurer-google-oauth-20-pour-lauthentification-et-lautorisation)
    
* [Comment configurer le routeur de l'application Angular](#heading-comment-configurer-le-routeur-de-lapplication-angular)
    
* [Comment configurer le service d'authentification](#heading-comment-configurer-le-service-dauthentification)
    
    * [Comment créer les fonctions de service pour la fonctionnalité de connexion et de déconnexion](#heading-comment-creer-les-fonctions-de-service-pour-la-fonctionnalite-de-connexion-et-de-deconnexion)
        
    * [Comment intégrer la fonction de service d'authentification dans le modèle](#heading-comment-integrer-la-fonction-de-service-dauthentification-dans-le-modele)
        
* [Comment créer une protection de route dans Angular](#heading-comment-creer-une-protection-de-route-dans-angular)
    
* [Comment créer et configurer la table des utilisateurs dans Supabase en utilisant l'éditeur SQL](#heading-comment-creer-et-configurer-la-table-des-utilisateurs-dans-supabase-en-utilisant-lediteur-sql)
    
    * [Comment configurer les politiques de sécurité au niveau des lignes dans Supabase avec l'éditeur SQL](#heading-comment-configurer-les-politiques-de-securite-au-niveau-des-lignes-dans-supabase-avec-lediteur-sql)
        
    * [Comment configurer les fonctions Supabase dans Supabase avec l'éditeur SQL](#heading-comment-configurer-les-fonctions-supabase-dans-supabase-avec-lediteur-sql)
        
    * [Comment configurer le déclencheur Supabase dans Supabase avec l'éditeur SQL](#heading-comment-configurer-le-declencheur-supabase-dans-supabase-avec-lediteur-sql)
        
* [Comment créer et configurer la table de chat dans Supabase en utilisant l'interface utilisateur](#heading-comment-creer-et-configurer-la-table-de-chat-dans-supabase-en-utilisant-linterface-utilisateur)
    
* [Comment créer et configurer les politiques de la table de chat dans Supabase](#heading-comment-creer-et-configurer-les-politiques-de-la-table-de-chat-dans-supabase)
    
* [Comment intégrer la fonctionnalité pour créer un nouveau message de chat dans l'application Angular](#heading-comment-integrer-la-fonctionnalite-pour-creer-un-nouveau-message-de-chat-dans-lapplication-angular)
    
* [Comment récupérer des données dans l'application Angular depuis Supabase](#heading-comment-recuperer-des-donnees-dans-lapplication-angular-depuis-supabase)
    
* [Comment supprimer des données dans l'application Angular](#heading-comment-supprimer-des-donnees-dans-lapplication-angular)
    
* [Comment implémenter la fonctionnalité de déconnexion dans l'application Angular](#heading-comment-implementer-la-fonctionnalite-de-deconnexion-dans-lapplication-angular)
    
* [Conclusion](#heading-conclusion)
    

## **Prérequis**

* HTML
    
* JavaScript
    
* TypeScript
    

## **Installations et configuration du compte :**

Avant de commencer, assurez-vous d'avoir installé et prêt ce qui suit :

* **Node.js et npm :** Angular nécessite Node. Vous pouvez vérifier si vous l'avez (et quelle version vous avez) en exécutant `node -v` dans votre terminal.
    
* **Angular CLI :** Il s'agit de l'outil en ligne de commande pour échafauder et gérer les projets Angular. Si vous ne l'avez pas, installez-le avec `npm install -g @angular/cli`. Vérifiez avec `ng version`.
    
* **Un compte Supabase :** Supabase offre un niveau gratuit. Inscrivez-vous sur le site [Supabase](http://supabase.com/) si vous ne l'avez pas déjà fait.
    

Vous pouvez également regarder la version vidéo de cet article ci-dessous, ou sur ma [chaîne YouTube](https://youtu.be/8SRhekaJ5iI?si=Vddj2ayZ0rF1R3W2) :

%[https://youtu.be/8SRhekaJ5iI?si=Vddj2ayZ0rF1R3W2] 

## Comment créer l'interface utilisateur de l'application Angular

Pour créer l'interface utilisateur de l'application, nous utiliserons [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/). Dans le fichier `index.html` de l'application Angular, vous allez coller le lien CDN de Bootstrap 5 comme indiqué ci-dessous :

```xml
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>NgChat</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>

<body>
  <app-root></app-root>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>

</body>

</html>
```

Ci-dessus, vous avez deux liens CDN de Bootstrap 5. Le premier est la balise `<link>` dans la section head, tandis que le second est la balise `<script>` qui se trouve juste en dessous de la balise `<app-root></app-root>`.

Maintenant que vous avez le lien CDN de Bootstrap 5 configuré dans le projet, l'étape suivante consiste à créer deux nouveaux composants appelés **chat** et **login**, respectivement, dans un dossier pages. Vous pouvez le faire en utilisant la commande ci-dessous :

```powershell
ng g c pages/chat-component && ng g c pages/login-component
```

Le fichier `login-component.html` contiendra le code ci-dessous :

```xml
<section class="login-block">
  <div class="container">

    <div class="row">
      <div class="col-md-12">
        <a class="btn btn-lg btn-google btn-block text-uppercase btn-outline" href="#"><img
            src="https://res.cloudinary.com/dz4tt9omp/image/upload/v1712537582/google-logo.png"> Inscription avec Google</a>
      </div>
    </div>
  </div>
</section>
```

Tandis que le fichier `login-component.css` contiendra le code ci-dessous :

```css
.login-block {
  width: 300px;
  margin: 0 auto;
  display:flex;
  justify-content:center;
  align-items:center;
  height:100vh;
}

.btn {
  border-radius: 2px;
  text-transform: capitalize;
  font-size: 15px;
  padding: 10px 19px;
  cursor: pointer
}


.btn-google {
  color: #545454;
  background-color: #ffffff;
  box-shadow: 0 1px 2px 1px #ddd;
}
```

Pour voir à quoi ressemble l'interface utilisateur, vous pouvez appeler la balise `<app-login />` avec le fichier `app.component.html`, puisque les navigations de route n'ont pas encore été configurées. L'interface utilisateur devrait ressembler à la capture d'écran ci-dessous :

![Capture d'écran d'une page web s'exécutant sur localhost au port 4200. La page affiche un fond blanc centré avec un seul bouton étiqueté "INSCRIPTION AVEC GOOGLE" qui inclut une icône de logo Google. Le bouton est légèrement surélevé avec un effet d'ombre.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746232060227/98f18b59-d433-486b-adbe-f28302e8d901.png align="center")

## Comment configurer un nouveau projet Supabase

Pour configurer Supabase, vous devrez créer un nouveau compte sur [Supabase.com](https://supabase.com/) en utilisant soit un compte GitHub, soit l'email et le mot de passe traditionnels. Une fois que vous avez fait cela, vous serez présenté avec un formulaire pour créer une nouvelle organisation comme vous pouvez le voir dans l'image ci-dessous :

![Formulaire Supabase pour créer une nouvelle organisation avec des champs pour le nom, le type et le plan.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747178536860/972076bf-ae5e-4b33-b18c-011e1e63b3a0.png align="center")

L'organisation sera créée aussi rapidement que votre vitesse Internet. Une fois cela fait, le formulaire suivant que vous verrez vous permettra de créer un nouveau projet Supabase.

![Interface Supabase pour créer un nouveau projet, montrant des champs pour l'organisation, le nom du projet, le mot de passe de la base de données et la sélection de la région.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747180463389/a41cd54d-4514-4a8b-8230-a348723b0a2f.png align="center")

Comme vous pouvez le voir sur l'image ci-dessus, tout ce que vous avez à faire pour créer un nouveau projet est de définir un mot de passe de base de données et de sélectionner une région proche de l'endroit où vous pensez que la plupart de vos utilisateurs seront. Cela aidera à réduire la latence. Avec cela, vous pouvez maintenant cliquer sur le bouton créer pour créer un nouveau projet.

Une fois la création du projet terminée, vous serez redirigé vers le tableau de bord ci-dessous :

![Tableau de bord Supabase montrant un nouveau projet sans tables et une liste de tâches en cours.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747180885966/b9b89775-36cb-49e8-a596-c5ae4bad75a7.png align="center")

Avec cela, vous avez maintenant configuré votre nouveau projet Supabase.

## Comment configurer Google OAuth 2.0 pour l'authentification et l'autorisation

Pour configurer Google OAuth 2.0, vous devez créer un compte sur [Google Cloud Console](https://console.cloud.google.com). Une fois que vous avez créé un compte, vous serez redirigé vers le tableau de bord, où vous pouvez créer un nouveau projet en cliquant sur le bouton sélectionner un projet en haut à gauche du tableau de bord.

![Page d'accueil de la console Google Cloud montrant une offre de crédit gratuit de 300 $. Un bouton 'Sélectionner un projet' est mis en évidence près du haut.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747353793461/b42cd8f9-5a6c-4579-be15-074f9bf90e13.png align="center")

Une fois que vous avez sélectionné le projet nouvellement créé, vous pouvez maintenant commencer à implémenter Google OAuth 2.0 en suivant ces étapes :

* Cliquez sur le menu hamburger sur le côté gauche du tableau de bord et survolez **APIs et services.**
    
* Cliquez sur **Identifiants**, sur la page Identifiants, sélectionnez **Créer des identifiants** dans le menu supérieur du tableau de bord. Un menu déroulant apparaîtra. Sélectionnez **Créer un ID client OAuth**.
    
* Sur la page ID client, vous obtiendrez un message d'avertissement qui dit « Pour créer un ID client OAuth, vous devez d'abord configurer votre écran de consentement. » Cliquez sur le bouton **Configurer l'écran de consentement**.
    

Ensuite, vous serez dirigé vers la page de marque. Cliquez sur le bouton commencer, et vous serez présenté avec un formulaire sur la page de vue d'ensemble comme vous pouvez le voir ci-dessous. Ensuite, remplissez simplement le formulaire :

![Console Google Cloud montrant la page 'Créer une marque' sous la plateforme Google Auth. L'utilisateur remplit les informations de l'application, y compris le nom de l'application et l'email de support, dans le cadre des étapes de configuration du projet.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747358499033/47c07eda-9b1e-45ce-ae0b-bb478178a0a2.png align="center")

Vous pouvez maintenant créer l'écran de consentement OAuth en vous rendant dans l'onglet Clients sur le côté gauche du tableau de bord et en remplissant les détails pour le type de votre application, le nom de votre client OAuth 2.0, ainsi que les origines JavaScript autorisées.

Pour les origines JavaScript autorisées, vous pouvez entrer l'URL ([http://localhost:4200](http://localhost:4200)), puisque c'est l'URL de développement pour notre application Angular. Ensuite, cliquez sur le bouton créer. Vous pouvez obtenir un avertissement disant « Note : Il peut falloir cinq minutes à quelques heures pour que les paramètres prennent effet. »

Une fois la configuration terminée, vous obtiendrez une modale qui contient un ID client et un secret client, comme vous pouvez le voir ci-dessous :

![Une boîte de dialogue de création de client OAuth de Google Cloud affiche l'ID client, le secret client, la date de création, l'état activé et un avertissement concernant le téléchargement des identifiants avant juin 2025.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747361106624/6ba6ed98-469a-4154-9d47-6719d982176e.png align="center")

Assurez-vous de copier l'ID client et le secret client, car vous les utiliserez dans le tableau de bord Supabase.

Pour compléter la configuration de l'authentification et de l'autorisation, rendez-vous sur le tableau de bord Supabase. Ensuite, naviguez jusqu'au menu Authentification, qui se trouve dans les éléments du côté gauche du tableau de bord. Dans cette partie du tableau de bord, vous sélectionnerez **Connexion / Fournisseurs**.

Sur la page Connexion / Fournisseurs, faites défiler jusqu'à **Fournisseurs d'authentification**, puis sélectionnez et activez **Google**. C'est ici que vous collerez les identifiants de l'ID client et du secret client créés sur la **Console Google Cloud**. Ensuite, cliquez sur le bouton enregistrer – et assurez-vous de copier l'URL de rappel (pour OAuth).

La dernière étape de ce processus consiste à revenir au tableau de bord GCP, et sous l'onglet Clients, cliquez sur l'icône d'édition des ID clients OAuth 2.0 que vous avez créés précédemment.

Sous les URI de redirection autorisées, cliquez sur le bouton Ajouter un URI. Une boîte d'entrée apparaîtra. Collez le lien de l'URL de rappel (pour OAuth) que vous avez récupéré dans le tableau de bord Supabase et cliquez sur enregistrer.

## Comment configurer le routeur de l'application Angular

Plus tôt dans ce tutoriel, vous avez créé deux composants : Chat et Login. À ce stade, vous devez configurer la configuration de route dans le fichier `app.routes.ts`. Dans ce fichier, ajoutez le code ci-dessous :

```typescript
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'chat',
    loadComponent: () =>
      import('./pages/chat/chat-component').then((com) => com.ChatComponent),
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./pages/login/login-component').then((com) => com.LoginComponent),
  },
  {
    path: '',
    loadComponent: () =>
      import('./pages/login/login-component').then((com) => com.LoginComponent),
  },
];
```

Ci-dessus, vous pouvez voir que les deux composants ont maintenant leurs routes séparées appelées **chat** et **login**, respectivement. Ils peuvent être accessibles n'importe où dans l'application.

## Comment configurer le service d'authentification

Pour configurer le service d'authentification dans l'application Angular, utilisez la commande suivante :

```bash
ng g s services/auth-service
```

Ensuite, vous allez générer les dossiers d'environnements pour configurer les variables d'environnement en utilisant la commande ci-dessous :

```bash
ng g environments
```

La dernière configuration que vous devez faire à partir du terminal avant de commencer à créer la fonction pour le service d'authentification Angular est d'installer Supabase avec la commande ci-dessous :

```bash
npm i @supabase/supabase-js
```

Et avec cela, vous avez maintenant Supabase installé dans le projet et vous pouvez commencer à intégrer les fonctions dans le service. Commencez par le fichier `environment.development.ts`. La structure actuelle de ce fichier devrait ressembler à ceci par défaut :

```typescript
export const environment = {};
```

Pour configurer ce fichier, vous devez vous rendre sur le tableau de bord Supabase. Localisez et sélectionnez le menu des paramètres sur le panneau de gauche du tableau de bord. Sous l'onglet **Configuration**, cliquez sur Data API.

![Capture d'écran des paramètres de l'API Supabase, montrant la section de l'URL du projet et des clés API avec des flèches pointant vers l'URL et les clés, plus des boutons pour copier chaque identifiant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747569518560/94ae00c7-4f62-4cc7-a0f9-250088754acb.png align="center")

Vous pouvez maintenant récupérer à la fois l'URL du projet et la clé publique anon (la flèche pointe vers elle dans l'image ci-dessus). Vous pouvez maintenant vous rendre dans le fichier `environment.development.ts` et coller les valeurs du lien copié en suivant le format ci-dessous :

```typescript
export const environment = {
  production: false,
  supabaseUrl: 'https://zktqzszvllbxvjfzkhvk.supabase.co',
  supabaseKey:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InprdHF6c3p2bGxieHZqZnpraHZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcyNTg3MDgsImV4cCI6MjA2MjgzNDcwOH0.qf3MA-La6se8QijzLFALKc_XdiISmzDk7AZw4-na0uA',
};
```

Avec les variables d'environnement toutes en place, vous pouvez maintenant créer les fonctions pour le service d'authentification.

Dans le fichier `auth-service.ts` que vous avez créé précédemment, commencez par importer le package Supabase ainsi que le fichier d'environnements comme vous pouvez le voir ci-dessous :

```typescript
import { Injectable } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';
```

Ensuite, complétez l'injection du package `npm` Supabase en l'injectant dans votre constructeur :

```typescript
import { Injectable } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  supabase!: SupabaseClient;

  constructor() {
      this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );
  }
}
```

### Comment créer les fonctions de service pour la fonctionnalité de connexion et de déconnexion

La dernière étape pour configurer le service `Auth` est de créer les fonctions qui seront appelées plus tard dans le modèle. Vous allez créer quatre fonctions que vous pouvez voir dans le code ci-dessous :

```typescript
  private router = inject(Router);
  private _ngZone = inject(NgZone);

  constructor() {
    this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );

    this.supabase.auth.onAuthStateChange((event, session) => {
 
      localStorage.setItem('session', JSON.stringify(session?.user));

      if (session?.user) {
        this._ngZone.run(() => {
          this.router.navigate(['/chat']);
        });
      }
    });
  }

  get isLoggedIn(): boolean {
    const user = localStorage.getItem('session') as string;

    return user === 'undefined' ? false : true;
  }

  async signInWithGoogle() {
    await this.supabase.auth.signInWithOAuth({
      provider: 'google',
    });
  }

  async signOut() {
    await this.supabase.auth.signOut();
  }
}
```

La première fonction créée est dans le constructeur. Il s'agit de la fonction de rappel `onAuthStateChange` qui est dérivée de Supabase et nous permet d'écouter les changements d'authentification. Elle accepte deux paramètres appelés `event` et `session`.

Ici, deux conditions ont été instanciées dans la fonction de rappel `onAuthStateChange`. Elles disent que lorsque `session?.user` existe, vous procédez à la définition de la valeur dans le stockage local, puis naviguez vers le tableau de bord en utilisant le routeur Angular (qui a été importé et injecté en utilisant la fonction `inject()`).

La deuxième fonction, `isLoggedIn()`, est une fonction getter qui retourne un booléen. Elle retourne soit vrai soit faux, selon qu'elle est capable de récupérer la session utilisateur depuis `localStorage`. Cette fonction sera utilisée dans le garde d'authentification que vous créerez plus tard.

La troisième fonction, `signInWithGoogle()`, permet à l'utilisateur de se connecter au tableau de bord en utilisant la méthode `signInWithOAuth()` fournie par Supabase. Cela permet à l'utilisateur de se connecter au tableau de bord en utilisant un compte Google Gmail.

La fonction finale, `signOut()`, permet aux utilisateurs de se déconnecter du tableau de bord en réinitialisant l'état de la session utilisateur à null.

Avec toutes ces fonctions créées, le code final dans le fichier `auth-service.ts` devrait ressembler à ceci :

```typescript
import { Injectable, NgZone, inject } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private supabase!: SupabaseClient;

  private router = inject(Router);
  private _ngZone = inject(NgZone);
  constructor() {
    this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );

    this.supabase.auth.onAuthStateChange((event, session) => {
      console.log('event', event);
      console.log('session', session);

      localStorage.setItem('session', JSON.stringify(session?.user));

      if (session?.user) {
        this._ngZone.run(() => {
          this.router.navigate(['/chat']);
        });
      }
    });
  }

  get isLoggedIn(): boolean {
    const user = localStorage.getItem('session') as string;

    return user === 'undefined' ? false : true;
  }

  async signInWithGoogle() {
    await this.supabase.auth.signInWithOAuth({
      provider: 'google',
    });
  }

  async signOut() {
    await this.supabase.auth.signOut();
  }
}
```

Vous pouvez maintenant utiliser ces fonctions n'importe où dans le projet Angular comme une forme de gestion d'état.

### Comment intégrer la fonction de service d'authentification dans le modèle

La première fonction que nous utiliserons est la fonction `signInWithGoogle()`. Nous l'utiliserons dans le fichier `login-component.ts` pour permettre aux utilisateurs de se connecter à l'application comme vous pouvez le voir ci-dessous :

```typescript
import { Component, inject } from '@angular/core';
import { AuthService } from '../../services/auth-service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login-component.html',
  styleUrl: './login-component.css',
})
export class LoginComponent {
  private auth = inject(AuthService);

  async handleAuth() {
    const response = await this.auth.signInWithGoogle();
  }
}
```

Ci-dessus, vous avez implémenté trois fonctionnalités :

* Importation de `AuthService` dans `LoginComponent`
    
* Injection de `AuthService` en utilisant la fonction Inject dans `LoginComponent`
    
* Création de la fonction `handleAuth()` qui vous permet d'appeler `signInWithGoogle()` depuis le fichier `AuthService`.
    

Maintenant, vous pouvez vous rendre dans le fichier `login-component.html` et appeler la fonction `handleAuth()` comme ci-dessous dans la balise `<a>` :

```xml
<section class="login-block">
  <div class="container">

    <div class="row">
      <div class="col-md-12">
        <a (click)="handleAuth()" class="btn btn-lg btn-google btn-block text-uppercase btn-outline" href="#"><img
            src="https://res.cloudinary.com/dz4tt9omp/image/upload/v1712537582/google-logo.png"> Inscription avec Google</a>
      </div>
    </div>
  </div>
</section>
```

Avant de tester l'implémentation, vous devrez définir la configuration de l'URL dans le tableau de bord Supabase. La configuration de l'URL permet les URL que les fournisseurs d'authentification autorisent à rediriger et à poster l'authentification, y compris les caractères génériques.

![Interface affichant les paramètres d'authentification, y compris la configuration de l'URL du site et les URL de redirection autorisées pour une application web.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748363896805/0b8f2ed1-ba45-44b9-93b8-0f470cb5ff32.png align="center")

Comme vous pouvez le voir dans l'image ci-dessus, les deux URL de redirection fournies sont localhost, puisque nous créons encore l'application sur notre machine locale.

Avec cela, vous pouvez tester la configuration de Google OAuth 2.0 en tapant l'URL localhost ([http://localhost:4200](http://localhost:4200/)) dans le navigateur, en cliquant sur le bouton **Inscription avec Google**, et en sélectionnant un compte Gmail avec lequel vous souhaitez vous inscrire/connecter. Ensuite, vous devriez être redirigé vers le composant Chat.

## Comment créer une protection de route dans Angular

Pour créer une protection de route dans Angular, vous pouvez utiliser un mécanisme intégré appelé **Route Guard**. Le Route Guard est utilisé pour contrôler l'accès à certaines parties de l'application Angular en utilisant certaines conditions avant qu'une route ne soit activée ou accessible à l'utilisateur.

Dans notre cas, vous allez générer le Route Guard en tant que fonction (ce qui est la valeur par défaut dans notre version actuelle d'Angular (20), au lieu de le faire en tant que classe) en utilisant la commande ci-dessous :

```bash
ng generate guard auth-guard
```

Vous verrez alors cette invite qui demande « Quel type de garde souhaitez-vous créer ? » :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748365560338/650c5bf7-8e1c-45cf-915b-c988c167416a.png align="center")

Utilisez la barre d'espace pour sélectionner `CanActivate`, puis appuyez sur la touche Entrée pour générer le Guard. Deux fichiers seront générés : le fichier `auth-guard.spec.ts` (pour les tests), et le fichier `auth-guard.ts`. Dans le fichier `auth-guard.ts`, vous verrez le code de base suivant :

```typescript
import { CanActivateFn } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  return true;
};
```

Vous pouvez commencer à modifier le modèle ci-dessus en important le routeur Angular, le fichier `AuthService` que vous avez créé précédemment, ainsi que la fonction Inject :

```typescript
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './services/auth-service';
import { inject } from '@angular/core';
```

Ensuite, utilisez le getter `isLoggedIn` que vous avez créé précédemment dans le fichier `AuthService` (qui retourne un booléen) pour activer conditionnellement le tableau de bord de chat pour l'utilisateur en fonction de son statut de connexion en utilisant le code ci-dessous :

```typescript
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './services/auth-service';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  if (inject(AuthService).isLoggedIn === false) {
    inject(Router).navigate(['/login']);
    return false;
  } else {
    return true;
  }
};
```

Pour compléter l'intégration du Guard, rendez-vous dans le fichier `app.routes.ts` et importez et injectez le Guard d'authentification comme vous pouvez le voir ci-dessous :

```typescript
import { Routes } from '@angular/router';
import { authGuard } from './auth-guard';

export const routes: Routes = [
  {
    path: 'chat',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./pages/chat/chat-component').then((com) => com.ChatComponent),
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./pages/login/login-component').then((com) => com.LoginComponent),
  },
  {
    path: '',
    loadComponent: () =>
      import('./pages/login/login-component').then((com) => com.LoginComponent),
  },
];
```

Avec cela, l'implémentation de la protection de route est maintenant complète et seuls les utilisateurs authentifiés peuvent voir le tableau de bord.

## Comment créer et configurer la table des utilisateurs dans Supabase en utilisant l'éditeur SQL

Pour créer et configurer la table des utilisateurs, utilisez le schéma ci-dessous :

* id (uuid)
    
* full\_name (text)
    
* avatar\_url (text)
    

Vous pouvez utiliser l'**éditeur SQL** dans Supabase. L'éditeur SQL est le troisième élément du panneau de menu dans le tableau de bord Supabase. Ici, vous allez taper la requête ci-dessous dans le champ de saisie de l'éditeur SQL :

```pgsql
CREATE TABLE public.users (
   id uuid not null references auth.users on delete cascade,
   full_name text NULL,
   avatar_url text NULL,
   primary key (id)
);
```

Vous pouvez maintenant cliquer sur le bouton Exécuter en bas à droite. Vous devriez obtenir un message qui dit : **Succès. Aucune ligne retournée**, comme vous pouvez le voir dans l'image ci-dessous :

![Code SQL pour créer une table de profil utilisateur avec des champs pour l'id, le nom complet et l'URL de l'avatar. Retourne Aucune ligne retournée après exécution.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748394167618/5db26c97-a947-4233-8232-3aba72187a12.png align="center")

Maintenant, allons-y et activons la sécurité au niveau des lignes, ainsi que la fonction Supabase et le déclencheur.

### Comment configurer les politiques de sécurité au niveau des lignes dans Supabase avec l'éditeur SQL

La sécurité au niveau des lignes (RLS) dans Supabase vous permet de contrôler l'accès aux lignes individuelles de vos tables de base de données en fonction d'une logique personnalisée. C'est l'une des fonctionnalités principales pour construire des applications multi-utilisateurs sécurisées avec Supabase.

RLS vous permet de définir des politiques SQL qui déterminent quels utilisateurs peuvent `SELECT`, `INSERT`, `UPDATE`, ou `DELETE` des lignes spécifiques dans une table.

Pour activer RLS dans la table **users**, tapez la commande ci-dessous dans votre éditeur SQL :

```pgsql
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
```

Pour les besoins de ce tutoriel, vous allez créer seulement deux politiques, qui sont :

1. La capacité pour les utilisateurs d'accéder à leur propre profil
    
2. La capacité pour les utilisateurs de mettre à jour leur propre profil
    

#### La capacité pour les utilisateurs d'accéder à leur propre profil

Pour permettre aux utilisateurs d'accéder à leur propre profil, retournez à l'éditeur SQL et créez un nouveau snippet avec la requête suivante :

```pgsql
CREATE POLICY "Permit Users to Access Their Profile"
  ON public.users
  FOR SELECT
  USING ( auth.uid() = id );
```

Avec cette requête, les utilisateurs pourront accéder à leur propre profil tant que l'ID de l'utilisateur authentifié correspond à l'`id` de la colonne de la ligne.

#### La capacité pour les utilisateurs de mettre à jour leur propre profil

Pour permettre aux utilisateurs de mettre à jour leur propre profil, retournez à l'éditeur SQL et créez un nouveau snippet avec la requête suivante :

```pgsql
CREATE POLICY "Permit Users to Update Their Profile"
  ON public.users
  FOR UPDATE
  USING ( auth.uid() = id );
```

Avec la requête ci-dessus, les utilisateurs pourront mettre à jour leur propre profil tant que l'ID de l'utilisateur authentifié correspond à l'`id` de la colonne de la ligne.

![Capture d'écran de l'éditeur SQL affichant un script de politique pour les mises à jour de profil utilisateur, avec un panneau de navigation et aucune ligne retournée.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748397263186/11e886f4-0d08-4907-9859-9269ee0da2ef.png align="center")

### Comment configurer les fonctions Supabase dans Supabase avec l'éditeur SQL

Les **fonctions Supabase** sont des fonctions serverless qui peuvent être déployées et exécutées dans votre projet Supabase en utilisant les **fonctions Supabase Edge**.

Dans ce projet, vous allez créer une fonction de déclenchement qui crée automatiquement une nouvelle ligne dans la table des utilisateurs chaque fois qu'un nouvel utilisateur est créé dans la table `auth.users`.

```pgsql
CREATE
OR REPLACE FUNCTION public.user_profile() RETURNS TRIGGER AS $$ BEGIN INSERT INTO public.users (id, full_name,avatar_url)
VALUES
  (
    NEW.id,
    NEW.raw_user_meta_data ->> 'full_name'::TEXT,
    NEW.raw_user_meta_data ->> 'avatar_url'::TEXT
  );
RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

Pour résumer la requête ci-dessus :

* Vous commencez par définir ou remplacer une fonction nommée `user_profile()` qui sera utilisée comme déclencheur.
    
* Ensuite, le déclencheur insère une nouvelle ligne dans la table `public.users`, puis extrait le `full_name` et `avatar_url` des métadonnées de l'utilisateur sous forme de texte.
    
* L'enregistrement inséré est maintenant retourné lorsque la fonction de déclenchement est complète
    
* Enfin, vous utilisez le mot-clé `SECURITY DEFINER` afin que la fonction puisse s'exécuter avec les privilèges de l'utilisateur qui l'a créée.
    

### Comment configurer le déclencheur Supabase dans Supabase avec l'éditeur SQL

Un déclencheur dans Supabase est une fonctionnalité PostgreSQL utilisée pour exécuter automatiquement une fonction en réponse à des événements sur une table (SELECT, INSERT, UPDATE, ou DELETE). Il est principalement utilisé avec la sécurité au niveau des lignes ou la synchronisation des données entre les tables.

Dans ce projet, vous allez créer un déclencheur Supabase qui exécute automatiquement une fonction après qu'un nouvel utilisateur a été créé dans la table `auth.users`.

```pgsql
 CREATE TRIGGER
  create_user_trigger
  AFTER INSERT ON auth.users
  FOR EACH ROW
  EXECUTE PROCEDURE
    public.user_profile();
```

Pour résumer la requête ci-dessus :

* La première ligne crée un **déclencheur** nommé `create_user_trigger`.
    
* Ensuite, l'instruction INSERT ON est activée lorsqu'un utilisateur s'inscrit et qu'une nouvelle ligne est insérée dans la table `auth.users`
    
* Ensuite, le déclencheur s'exécute une fois pour chaque nouvel utilisateur ajouté dans une nouvelle ligne.
    
* Enfin, la fonction personnalisée `public.user_profile()` est appelée pour effectuer une logique, généralement en insérant des données dans la table `users`.
    

Avec l'intégration ci-dessus, vous pouvez maintenant vous connecter au tableau de bord avec un nouveau compte Google et consulter la table des utilisateurs. Vous y verrez les données contenant l'**id**, le **full\_name** et l'**avatar\_url** comme vous pouvez le voir ci-dessous :

![Capture d'écran d'un éditeur de table de base de données affichant les données des utilisateurs, y compris le nom et l'URL de l'avatar, avec des options de filtrage et de tri.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748560146471/4c7663a8-6708-461a-8ed5-7ed8a3931318.png align="center")

## Comment créer et configurer la table de chat dans Supabase en utilisant l'interface utilisateur

Pour créer la table de chat, vous allez utiliser l'interface utilisateur dans Supabase au lieu de l'éditeur SQL. Pour ce faire, vous devez vous rendre dans le menu Éditeur de table du tableau de bord et cliquer sur le bouton **Nouvelle table**.

Une fois sélectionné, une modale apparaîtra contenant certains champs de saisie tels que le nom de la table, la description et les colonnes. Vous pouvez appeler la table chat et omettre la description pour l'instant puisque c'est facultatif. Dans la section des colonnes, remplissez les champs en utilisant le schéma ci-dessous :

* id (uuid)
    
* Created At (date)
    
* text (text)
    
* editable (boolean)
    
* sender (uuid)
    

Vous pouvez voir la configuration pour cela dans le tableau ci-dessous :

![Capture d'écran d'une interface d'éditeur de table affichant des champs pour créer une nouvelle table de base de données avec divers types de données et options.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748564800333/0e879684-75d3-4c47-9f38-56d6041d6b38.png align="center")

Ensuite, vous devez ajouter une relation de clé étrangère pour la table des utilisateurs. Pour ce faire, faites défiler jusqu'en bas de la modale et cliquez sur le bouton **Ajouter une relation de clé étrangère**. Cela fera apparaître une autre modale par-dessus la modale actuelle. Ici, vous pouvez suivre les étapes suivantes :

* Sous l'étiquette **Sélectionner une table à référencer**, sélectionnez la table **users**.
    
* Sous l'étiquette **public.chat**, sélectionnez l'option **sender**.
    
* Sous l'étiquette public.users, sélectionnez **uuid.**
    
* Sous l'étiquette **Action si la ligne référencée est mise à jour**, sélectionnez **Cascade**.
    
* Sous l'étiquette **Action si la ligne référencée est supprimée**, sélectionnez également **Cascade**.
    

Si vous avez suivi les étapes ci-dessus, vous pouvez maintenant cliquer sur le bouton enregistrer, ce qui crée avec succès la table de chat.

## Comment créer et configurer les politiques de la table de chat dans Supabase

La dernière étape que vous devez effectuer pour la table de chat est d'ajouter une politique de sécurité au niveau des lignes. Vous pouvez le faire en cliquant sur le bouton **Ajouter une politique RLS** en haut de la page de la table de chat.

![Une interface web affichant un éditeur de table avec des options pour gérer les données de chat et d'utilisateur dans un schéma de base de données.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748567233239/6f69e305-5e09-4485-89b7-0115d41c8e0f.png align="center")

Une nouvelle page apparaîtra. Ensuite, vous pouvez cliquer sur le bouton **Créer une politique**, qui affiche une modale.

La première politique que vous allez créer est la politique **DELETE**, qui aura la configuration que vous pouvez voir dans l'image ci-dessous :

![Capture d'écran d'une interface de paramètres de politique de base de données pour supprimer des enregistrements d'utilisateurs en fonction de l'ID utilisateur dans une application de chat.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748779442105/f977dafb-ab73-4bb7-8643-9aa4e889c359.png align="center")

D'après l'image ci-dessus, nous avons fait ces quatre implémentations :

* Tout d'abord, nous avons entré le nom de la politique comme « **Supprimer par ID utilisateur** ».
    
* Ensuite, nous avons sélectionné la clause de commande de politique **DELETE**.
    
* Puis, sous les rôles ciblés, nous avons sélectionné authentifié dans la liste déroulante, pour permettre uniquement aux utilisateurs authentifiés d'effectuer des opérations de suppression.
    
* Enfin, sous la section **UTILISER LES OPTIONS CI-DESSUS POUR MODIFIER**, à la ligne 7, nous conditionnons la requête comme `(auth.uid() = sender)` Cela permet uniquement aux utilisateurs connectés de supprimer leurs données.
    

Vous pouvez maintenant cliquer sur le bouton **Enregistrer la politique** pour compléter la configuration DELETE.

La deuxième politique que vous allez créer est la politique **INSERT**, qui aura la configuration que vous pouvez voir dans l'image ci-dessous :

![Une interface de configuration de politique pour l'insertion d'enregistrements dans une table de chat, ciblant les utilisateurs authentifiés avec des critères spécifiques.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748823531256/14aea41d-f221-42df-a739-b40a680395e3.png align="center")

D'après l'image ci-dessus, quatre implémentations ont été faites :

* Tout d'abord, nous avons entré le nom de la politique comme « **Insertion pour les utilisateurs authentifiés** ».
    
* Ensuite, nous avons sélectionné la clause de commande de politique **INSERT**.
    
* Puis, sous les rôles ciblés, nous avons sélectionné authentifié dans la liste déroulante pour permettre uniquement aux utilisateurs authentifiés d'effectuer des opérations d'insertion.
    
* Enfin, sous la section **UTILISER LES OPTIONS CI-DESSUS POUR MODIFIER**, à la ligne 7, la requête a été conditionnée comme `((sender = auth.uid()) AND (created_at = now()))`. La première condition garantit que le champ `sender` dans la ligne insérée correspond à l'ID de l'utilisateur actuellement connecté (à partir du JWT Supabase), tandis que la deuxième condition garantit que le champ `created_at` est exactement égal à l'horodatage actuel au moment de l'insertion.
    

La troisième politique que vous allez créer est la politique **SELECT**, qui aura la configuration que vous pouvez voir dans l'image ci-dessous :

![Configuration de la politique de sécurité au niveau des lignes pour une table de base de données, spécifiant les permissions d'accès pour les utilisateurs authentifiés en fonction des critères SELECT.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748824129598/8c15b701-dadb-4763-b5eb-e9484bd84470.png align="center")

D'après l'image ci-dessus, nous avons implémenté quatre choses :

* Tout d'abord, nous avons entré le nom de la politique comme « **Lire les données pour les utilisateurs authentifiés** ».
    
* Ensuite, nous avons sélectionné la clause de commande de politique **SELECT**, *jeu de mots intended* **😊***.*
    
* Puis, sous les rôles ciblés, nous avons sélectionné authentifié dans la liste déroulante pour permettre uniquement aux utilisateurs authentifiés d'effectuer des opérations de sélection.
    
* Enfin, sous la section **UTILISER LES OPTIONS CI-DESSUS POUR MODIFIER**, à la ligne 7, la requête a été conditionnée comme `true`. Cela permet à tous les utilisateurs authentifiés de lire toutes les lignes, ou chats dans notre cas.
    

Avec l'implémentation ci-dessus, vous avez créé toutes les politiques nécessaires pour l'application de chat.

## Comment intégrer la fonctionnalité pour créer un nouveau message de chat dans l'application Angular

Maintenant, ajoutons le code qui permet aux utilisateurs de créer un nouveau message de chat. Commencez par créer un nouveau service Angular en utilisant la commande ci-dessous :

```powershell
ng g s services/chat-service
```

Dans le fichier `chat-service.ts`, vous pouvez maintenant configurer le client Supabase, comme nous l'avons fait dans le fichier `auth-service.ts` comme vu ci-dessous :

```typescript
import { Injectable, signal } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  supabase!: SupabaseClient;

  constructor() {
    this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );
  }
}
```

Ensuite, créez la fonction qui vous permet de créer un nouveau message de chat. La fonction appelée `chatMessage()` est ci-dessous :

```typescript
import { Injectable, signal } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  supabase!: SupabaseClient;

  constructor() {
    this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );
  }

  async chatMessage(text: string) {
    try {
      const { data, error } = await this.supabase.from('chat').insert({ text });

      if (error) {
        alert(error.message);
      }
    } catch (error) {
      alert(error);
    }
  }
}
```

La fonction `chatMessage` ci-dessus envoie un message de chat en l'insérant dans la table `chat` dans Supabase.

Vous pouvez maintenant appeler ce service dans le fichier `chat-component.ts`. Dans le fichier `chat-component.ts`, importez et injectez le fichier `chat-service.ts`.

Pour envoyer les données à la base de données Supabase, vous devez configurer un formulaire réactif. Le formulaire réactif dans Angular vous permet d'obtenir des données à partir d'un champ de saisie, qui peuvent être passées en tant que charge utile et ensuite insérées dans la base de données.

Pour configurer un formulaire réactif dans Angular, suivez ces étapes :

* Importez `FormBuilder`, `FormGroup`, `ReactiveFormsModule`, et `Validators` depuis `@angular/forms`
    
* Insérez le `ReactiveFormsModule` à l'intérieur du tableau des imports.
    
* Injectez le `FormBuilder` en tant que variable.
    
* Déclarez une propriété qui contiendra le **groupe de formulaires réactifs.**
    
* Injectez le `FormBuilder` dans le hook de cycle de vie `ngOnInit`.
    

Le code pour la configuration du formulaire réactif est ci-dessous :

```typescript
import { Component, inject } from '@angular/core';
import { AuthService } from '../../services/auth-service';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './chat-component.html',
  styleUrl: './chat-component.css',
})
export class ChatComponent {
  chatForm!: FormGroup;
  private fb = inject(FormBuilder);

  ngOnInit() {
    this.chatForm = this.fb.group({
      chat_message: ['', Validators.required],
    });
  }
}
```

Pour compléter la configuration du formulaire réactif, liez le `FormGroup` dans le fichier HTML. Liez également l'attribut disabled, qui désactive le bouton lorsque le formulaire est invalide, comme vous pouvez le voir ci-dessous :

```xml
  <form [formGroup]="chatForm">
          <div class="flex-grow-0 py-3 px-4 border-top">
              <div class="input-group">
                <input formControlName="chat_message" type="text" class="form-control" placeholder="Tapez votre message">
                <button [disabled]="!chatForm.valid" class="btn btn-primary">Envoyer</button>
              </div>
           </div>
    </form>
```

Avec la configuration du formulaire réactif complète, vous pouvez maintenant créer la fonction qui appelle le service qui vous permet de créer un nouveau message de chat.

```typescript
import { Component, inject } from '@angular/core';
import { AuthService } from '../../services/auth-service';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { ChatService } from '../../services/chat-service';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './chat-component.html',
  styleUrl: './chat-component.css',
})
export class ChatComponent {
  private chat_service = inject(ChatService);
  chatForm!: FormGroup;
  private fb = inject(FormBuilder);

  ngOnInit() {
    this.chatForm = this.fb.group({
      chat_message: ['', Validators.required],
    });
  }

  onSubmit() {
    const formValue = this.chatForm.value.chat_message;
    this.chat_service
      .chatMessage(formValue)
      .then((res) => {
        this.chatForm.reset();
      })
      .catch((err) => {
        alert(err.message);
      });
  }
}
```

La fonction `onSubmit()` dans le code ci-dessus effectue essentiellement les tâches suivantes :

* Récupère les données du champ de saisie du formulaire réactif en utilisant la variable appelée `formValue`
    
* Appelle la méthode `chatMessage()` depuis le `ChatService`, en passant les données du champ de saisie.
    
* Si cela réussit, elle réinitialise le formulaire.
    
* Si une erreur survient, elle affiche une alerte avec le message d'erreur.
    

Dans le fichier `chat-component.html`, utilisez la directive `(ngSubmit)` pour lier la fonction `onSubmit()` au formulaire :

```xml
<form [formGroup]="chatForm" (ngSubmit)="onSubmit()">
```

Vous pouvez maintenant tester pour voir si les données que nous envoyons depuis le champ de saisie sont sauvegardées directement dans la table de base de données **chat**.

**NOTE :** assurez-vous de **supprimer tous les utilisateurs actuels sauvegardés dans la table des utilisateurs et la page d'authentification sur Supabase** avant d'essayer cela pour obtenir les meilleurs résultats.

![Capture d'écran d'une interface de chat montrant un message de "Sharon Doe," avec un horodatage et un champ de saisie de texte en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749042436895/a50416e7-3f8b-48a9-b8f3-96df520b2238.png align="center")

D'après l'image ci-dessus, vous cliquerez sur le bouton d'envoi et enverrez les données **Test** dans le champ de saisie.

![Interface de l'éditeur de table affichant la table "chat" avec des colonnes incluant ID, created_at, text, editable et sender, montrant des entrées et des options de configuration.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749043485066/94b53998-e924-44c2-bbfd-e26d591fdf54.png align="center")

Les données devraient maintenant être sauvegardées avec succès dans la base de données et l'opération **INSERT** devrait maintenant être intégrée dans l'application Angular.

## Comment récupérer des données dans l'application Angular depuis Supabase

Pour récupérer des données depuis la table de chat de Supabase, commencez par créer une fonction de service dans le fichier `chat-service.ts`, comme vu ci-dessous :

```typescript
import { Injectable, signal } from '@angular/core';
import { SupabaseClient, createClient } from '@supabase/supabase-js';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  supabase!: SupabaseClient;

  constructor() {
    this.supabase = createClient(
      environment.supabaseUrl,
      environment.supabaseKey
    );
  }

  async chatMessage(text: string) {
    try {
      const { data, error } = await this.supabase.from('chat').insert({ text });
      if (error) {
        alert(error.message);
      }
    } catch (error) {
      alert(error);
    }
  }

    async listChat() {
    try {
      const { data, error } = await this.supabase
        .from('chat')
        .select('*,users(*)');

      if (error) {
        alert(error.message);
      }

      return data;
    } catch (error) {
      throw error;
    }
  }
}
```

Pour résumer la fonction ci-dessus appelée `listChat()` :

* Nous récupérons les messages de chat depuis la table `chat` en utilisant la clause `from`.
    
* Ensuite, nous incluons les informations sur l'utilisateur associé en joignant la table des utilisateurs avec `(select(', users()'))`.
    
* Un message d'alerte est affiché s'il y a une erreur Supabase.
    
* Enfin, les données récupérées sont retournées, une erreur est lancée si quelque chose ne va pas.
    

Avant de vous rendre dans le fichier `chat-component.ts` pour consommer la fonction de service `listChat()`, vous devez créer une interface qui aide à structurer le tableau d'objets retourné par Supabase. Cela nous donne une sécurité de type et une cohérence.

Pour configurer l'interface, créez un dossier **interface** dans le répertoire **app**. Ici, vous créerez un fichier appelé `chat-response.ts`. Ensuite, créez la structure ci-dessous :

```typescript
export interface Ichat {
  created_at: string;
  editable: boolean;
  id: string;
  sender: string;
  text: string;
  users: {
    avatar_url: string;
    id: string;
    full_name: string;
  };
}
```

En revenant au fichier `chat-component.ts`, importez à la fois l'interface qui a été nommée `Ichat` ainsi que `signal` et `effect` depuis `@angular/core` :

```typescript
import { Component, effect, inject, signal } from '@angular/core';
import { AuthService } from '../../services/auth-service';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { ChatService } from '../../services/chat-service';
import { Ichat } from '../../interface/chat-response';
```

Ensuite, créez une variable appelée `chats`, qui contiendra la réponse du client Supabase en tant que signal :

```typescript
  chats = signal<Ichat[]>([]);
```

Avec cela, vous pouvez maintenant créer la fonction qui récupère le tableau d'objets de chat depuis le tableau de bord Supabase :

```typescript
  onListChat() {
    this.chat_service
      .listChat()
      .then((res: Ichat[] | null) => {
        console.log(res);
        if (res !== null) {
          this.chats.set(res);
        } else {
          console.log('Aucun message trouvé');
        }
      })
      .catch((err) => {
        alert(err.message);
      });
  }
```

Pour résumer la fonction ci-dessus, nous avons commencé par :

* Appeler la fonction `listChat()` depuis le `ChatService` pour récupérer les messages de chat.
    
* Si des messages sont retournés, elle met à jour le signal des chats avec le résultat, en utilisant la méthode `set()` dérivée des signaux.
    
* Dans le cas où aucun message n'est retourné, elle enregistre `"Aucun message trouvé"` dans la console.
    
* Si une erreur se produit, elle affiche une alerte avec le message d'erreur.
    

Nous appelons ensuite la fonction `onListChat()` dans le constructeur en utilisant la fonction `effect()`, qui aide à gérer les opérations asynchrones.

```typescript
constructor() {
    effect(() => {
      this.onListChat();
    });
  }
```

Lorsque l'application est sauvegardée, vous pouvez voir les données dans la console à partir de l'image ci-dessous :

![Capture d'écran d'une application de chat montrant un message de Sharon Doe, ainsi que des outils de développement affichant les données du message dans un tableau d'objets.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749066359110/dedaa60a-c711-42d9-bac1-c9a130fcc4d1.png align="center")

Vous pouvez maintenant afficher les données de chat dans le fichier HTML de la page en vous débarrassant du texte de remplissage.

Pour ce faire, vous pouvez utiliser le flux de contrôle `@for` dans Angular comme vu ci-dessous :

```typescript
<main>
  <div class="container">
    <h3 class="mb-3">Supa Chat <button class="btn btn-secondary" style="float: right;">Déconnexion</button>
    </h3>
    <div class="card">
      <div>

        <div class="col-12 col-lg-12 col-xl-12">
          @for (msg of this.chats(); track msg) {
          <div class="position-relative">
            <div class="chat-messages p-4">
              <div class="chat-message-left pb-4">
                <div class="me-5">
                  <img src={{msg?.users?.avatar_url}} class="rounded-circle mr-1" alt="image" width="40" height="40">
                  <div class="text-muted small text-nowrap mt-2">{{msg?.created_at | date: 'M/d/yy, h:mm a'}}</div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                  <div class="font-weight-bold mb-1">{{msg?.users?.full_name}}</div>
                  {{msg?.text}}
                </div>
              </div>
            </div>
          </div>
          } @empty {
          <div>Aucun chat disponible</div>
          }

          <form [formGroup]="chatForm" (ngSubmit)="onSubmit()">
            <div class="flex-grow-0 py-3 px-4 border-top">
              <div class="input-group">
                <input formControlName="chat_message" type="text" class="form-control" placeholder="Tapez votre message">
                <button [disabled]="!chatForm.valid" class="btn btn-primary">Envoyer</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>
```

D'après le code ci-dessus, juste au-dessus de la `div` avec la classe `position-relative`, nous avons déclaré le flux de contrôle `@for (msg of this.chats(); track msg)`, qui fait ce qui suit :

* Parcourt le tableau retourné par `this.chats()` qui est la variable de signal qui a été déclarée dans le modèle.
    
* Assigne chaque élément du tableau à la variable `msg`.
    
* Suit chaque élément par identité `track msg` pour les mises à jour du DOM.
    

Ensuite, dans la boucle, vous avez appelé les données dans la balise HTML appropriée pour afficher l'image, la date à laquelle le chat a été créé, le nom complet et le message de chat également.

Enfin, vous avez créé un bloc `@empty` qui affiche le message `Aucun chat disponible` s'il n'y a aucun élément dans le tableau.

Vous devriez obtenir le résultat ci-dessous :

![Une interface de chat affichant deux messages de l'utilisateur "adedeji adesoga," datés du 4 juin 2025, avec une boîte de saisie de texte en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749082870784/85184bf1-3cfe-4808-a149-64a6b925e097.png align="center")

## Comment supprimer des données dans l'application Angular

Lors de la création de la fonctionnalité de suppression, vous devez d'abord créer une fonction de service dans le fichier `chat-service.ts` comme vu ci-dessous :

```typescript
  async deleteChat(id: string) {
    const data = await this.supabase.from('chat').delete().eq('id', id);
    return data;
  }
```

Tout ce que fait la fonction ci-dessus est de trouver l'id spécifique fourni à partir du paramètre, et de retourner le résultat de l'opération de suppression.

Ensuite, suivez le chat sélectionné qui a été cliqué à partir du tableau des chats listés et passez ensuite les données à votre service.

Pour ce faire, créez d'abord une fonction dans le service appelée `selectedChats()` qui aide à recevoir les données du modèle :

```typescript
 public savedChat = signal({});

 selectedChats(msg: Ichat) {
    this.savedChat.set(msg);
  }
```

Ci-dessus, nous avons créé la variable appelée `savedChat`. Elle est déclarée comme un signal qui aide à recevoir l'objet du chat que nous voulons supprimer en utilisant la méthode `set()`.

Vous pouvez maintenant vous rendre dans le fichier `chat-component.ts` pour créer la fonction qui passe les données à la fonction `selectedChats()`.

Vous pouvez voir cette fonction ci-dessous :

```typescript
 openDropDown(msg: Ichat) {
    console.log(msg);
    this.chat_service.selectedChats(msg);
  }
```

Comme vous pouvez le voir dans la fonction ci-dessus, une fois que vous la liez à l'élément HTML, elle s'assurera que vous obtenez l'objet du chat spécifique qui a été cliqué.

Dans notre fichier `chat-component.html`, créez un menu déroulant qui aidera à obtenir ce résultat comme vu ci-dessous :

```typescript
<main>
  <div class="container">
    <h3 class="mb-3">Supa Chat <button class="btn btn-secondary" style="float: right;">Déconnexion</button>
    </h3>
    <div class="card">
      <div>

        <div class="col-12 col-lg-12 col-xl-12">
          @for (msg of this.chats(); track msg) {
          <div class="position-relative">
            <div class="chat-messages p-4">
              <div class="chat-message-left pb-4">
                <div class="me-5">
                  <img src={{msg?.users?.avatar_url}} class="rounded-circle mr-1" alt="image" width="40" height="40">
                  <div class="text-muted small text-nowrap mt-2">{{msg?.created_at | date: 'M/d/yy, h:mm a'}}</div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                  <div class="font-weight-bold mb-1">{{msg?.users?.full_name}}</div>
                  {{msg?.text}}
                </div>

                <!-- Menu du bouton de la modale de suppression-->
                <div class="dropdown">
                  <span (click)="openDropDown(msg)" class="mt-3 ms-5" type="button" id="dropdownMenuButton1"
                    data-bs-toggle="dropdown" aria-expanded="false">
                    ...
                  </span>
                  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                    <li>
                      <a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Supprimer</a>
                    </li>
                  </ul>
                </div>


              </div>
            </div>
          </div>
          } @empty {
          <div>Aucun chat disponible</div>
          }

          <form [formGroup]="chatForm" (ngSubmit)="onSubmit()">
            <div class="flex-grow-0 py-3 px-4 border-top">
              <div class="input-group">
                <input formControlName="chat_message" type="text" class="form-control" placeholder="Tapez votre message">
                <button [disabled]="!chatForm.valid" class="btn btn-primary">Envoyer</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>
```

D'après le code ci-dessus, notez ce qui suit : le commentaire avec le texte `<!-- Menu du bouton de la modale de suppression-->` est créé dans le flux de contrôle `@for`. Cela est essentiel car il permet à `openDropDown(msg)` de recevoir le bon objet en tant que paramètre lorsque le menu déroulant est cliqué. Un rapide coup d'œil à la console révélera cela.

Vous pouvez maintenant créer le composant de la modale de suppression, qui vous permet de consommer le service de suppression requis pour qu'un chat soit supprimé.

Pour créer le composant de suppression, utilisez la commande ci-dessous :

```powershell
ng g component layout/modal-component
```

Le design pour le composant de suppression est une modale Bootstrap 5 qui ressemble à ceci :

```typescript
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Titre de la modale</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
      </div>
      <div class="modal-body">
        Êtes-vous vraiment sûr de vouloir supprimer ce message ?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Non</button>
        <button [attr.data-bs-dismiss]="!this.dismiss() === true ? 'modal' : null" (click)="deleteChat()" type="button"
          class="btn btn-primary">Oui</button>
      </div>
    </div>
  </div>
</div>
```

Si vous collez le code ci-dessus directement dans votre éditeur de code, vous allez obtenir une série d'erreurs car nous n'avons pas créé la fonction `deleteChat()` ainsi que la variable de signal `dismiss()` dans le fichier de modèle. Allons-y et faisons cela.

La première étape pour configurer le composant de fichier `modal-componet.ts` est d'importer les modules appropriés comme vu ci-dessous :

```typescript
import { Component, effect, inject, signal } from '@angular/core';
import { ChatService } from '../../services/chat.service';
import { Router } from '@angular/router';
```

Ensuite, injectez le `chatservice`, le `routeur Angular`, ainsi que la variable `dismiss` qui est un signal comme vu ci-dessous :

```typescript
  private chat_service = inject(ChatService);
  private router = inject(Router);
  dismiss = signal(false);
```

Avec cela, vous pouvez maintenant créer la fonction `deleteChat()` comme vu ci-dessous :

```typescript
deleteChat() {
    const id = (this.chat_service.savedChat() as { id: string }).id;

    console.log(id);

    this.chat_service
      .deleteChat(id)
      .then(() => {
        let currentUrl = this.router.url;

        this.dismiss.set(true);

        this.router
          .navigateByUrl('/', { skipLocationChange: true })
          .then(() => {
            this.router.navigate([currentUrl]);
          });
      })
      .catch((err) => {
        console.log(err);
        alert(err.message);
      });
  }
```

* La première chose que nous avons faite sous la méthode `deleteChat()` a été d'extraire l'`id` du service de chat.
    
* Cet `id` est ensuite passé dans la méthode `deleteChat()` de notre service qui aide à supprimer le chat spécifique qui a été sélectionné.
    
* Une fois le chat supprimé, la route actuelle est rechargée pour mettre à jour l'interface utilisateur.
    

Pour activer la modale, vous devez importer le composant Modal dans le fichier `chat-component.html` (dernière ligne de code ci-dessous :

```xml
<main>
  <div class="container">
    <h3 class="mb-3">Supa Chat <button class="btn btn-secondary" style="float: right;">Déconnexion</button>
    </h3>
    <div class="card">
      <div>

        <div class="col-12 col-lg-12 col-xl-12">
          @for (msg of this.chats(); track msg) {
          <div class="position-relative">
            <div class="chat-messages p-4">
              <div class="chat-message-left pb-4">
                <div class="me-5">
                  <img src={{msg?.users?.avatar_url}} class="rounded-circle mr-1" alt="image" width="40" height="40">
                  <div class="text-muted small text-nowrap mt-2">{{msg?.created_at | date: 'M/d/yy, h:mm a'}}</div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                  <div class="font-weight-bold mb-1">{{msg?.users?.full_name}}</div>
                  {{msg?.text}}
                </div>

                <!-- Menu du bouton de la modale de suppression-->
                <div class="dropdown">
                  <span (click)="openDropDown(msg)" class="mt-3 ms-5" type="button" id="dropdownMenuButton1"
                    data-bs-toggle="dropdown" aria-expanded="false">
                    ...
                  </span>
                  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                    <li>
                      <a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Supprimer</a>
                    </li>
                  </ul>
                </div>


              </div>
            </div>
          </div>
          } @empty {
          <div>Aucun chat disponible</div>
          }

          <form [formGroup]="chatForm" (ngSubmit)="onSubmit()">
            <div class="flex-grow-0 py-3 px-4 border-top">
              <div class="input-group">
                <input formControlName="chat_message" type="text" class="form-control" placeholder="Tapez votre message">
                <button [disabled]="!chatForm.valid" class="btn btn-primary">Envoyer</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>

<!-- modal -->

<app-modal />
```

**NOTE :** N'oubliez pas d'importer le fichier **ModalComponent** dans le fichier `chat-component.ts` pour éviter d'avoir des erreurs.

Vous avez maintenant implémenté la capacité à insérer, lire et supprimer des données. La dernière implémentation consiste à intégrer la fonctionnalité de déconnexion.

## Comment implémenter la fonctionnalité de déconnexion dans l'application Angular

Plus tôt dans le tutoriel, dans le fichier `auth-service.ts`, vous avez créé une fonction appelée `signOut()` comme vu ci-dessous :

```typescript
 async signOut() {
    await this.supabase.auth.signOut();
  }
```

Dans le fichier `chat-component.ts`, vous allez importer et injecter la méthode `sigOut()`. Pour ce faire, suivez ces étapes :

* Importez et injectez le routeur Angular.
    
* Importez et injectez le fichier de service d'authentification
    
* Créez la fonction `logOut()` qui consomme le service `signOut()` :
    

```javascript
async logOut() { 
this.auth .signOut() .then(() =>
 { this.router.navigate(['/login']); }) 
.catch((err) => {
 alert(err.message);
 });
 }
```

* Enfin, dans le fichier `chat-component.html`, dans la balise de bouton en haut de la page, appelez la fonction `logout()` en utilisant le gestionnaire d'événements `(click)` :
    

```xml
  <h3 class="mb-3">Supa Chat 
    <button (click)="logOut()" class="btn btn-secondary" style="float: right;">Déconnexion</button>
  </h3>
```

Une fois le bouton Déconnexion cliqué, l'utilisateur est redirigé vers la page de connexion et l'état de l'utilisateur est réinitialisé dans le navigateur.

## Conclusion

Dans ce tutoriel, vous avez appris à créer une application de chat en temps réel en utilisant Angular et Supabase. Nous avons couvert les concepts clés suivants :

* Comment créer des tables de base de données dans Supabase
    
* Comment créer des déclencheurs et des fonctions dans Supabase
    
* Comment utiliser les signaux pour gérer l'état dans Angular
    
* Comment créer une authentification et une autorisation en utilisant Supabase et Google OAuth 2.0
    
* Comment travailler avec les formulaires réactifs dans Angular
    

et bien plus encore.

Vous pouvez accéder au code complet en clonant le dépôt sur [GitHub](https://github.com/desoga10/ng-chat-20).

Si vous avez trouvé cet article utile, envisagez de vous abonner à ma [chaîne YouTube](https://www.youtube.com/@TheCodeAngle) où je partage des tutoriels pratiques sur les technologies modernes de développement web comme JavaScript, HTML, CSS, Angular, Supabase, Firebase, React, les API tierces et les outils d'IA, et bien plus encore. Santé !