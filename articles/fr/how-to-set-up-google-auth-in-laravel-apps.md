---
title: Comment configurer l'authentification Google dans les applications Laravel
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2024-12-03T15:23:38.361Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-google-auth-in-laravel-apps
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732711351776/931a1ade-e652-4a0b-a16e-925482128fc0.png
tags:
- name: Laravel
  slug: laravel
- name: google authenticator
  slug: google-authenticator
- name: google auth
  slug: google-auth
- name: 'socialite '
  slug: socialite
seo_title: Comment configurer l'authentification Google dans les applications Laravel
seo_desc: 'In this digital world, it’s important for your applications to have a smooth
  and secure authentication process. This helps improve user experience and the overall
  security of your apps.

  Google Authentication is among the most trusted and convenient w...'
---

Dans ce monde numérique, il est important que vos applications disposent d'un processus d'authentification fluide et sécurisé. Cela permet d'améliorer l'expérience utilisateur et la sécurité globale de vos applications.

L'authentification Google est l'une des méthodes les plus fiables et pratiques pour permettre aux utilisateurs de se connecter à un site en utilisant leur compte Google. Et cela signifie qu'ils n'ont pas à retenir un autre nom d'utilisateur et mot de passe.

L'intégration de Google OAuth dans votre application [Laravel](https://laravel.com/) simplifie le processus de connexion, encourage l'engagement des utilisateurs et renforce la crédibilité de votre plateforme. Dans ce tutoriel, je vais vous guider à travers les étapes de mise en œuvre de l'authentification Google dans une application Laravel. Nous allons passer de la configuration des identifiants de l'API Google à la configuration du package Socialite de Laravel.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Avantages de l'utilisation de Google Auth dans une application Laravel](#heading-avantages-de-lutilisation-de-google-auth-dans-une-application-laravel)
    
* [Comment configurer la connexion Google Laravel](#heading-comment-configurer-la-connexion-google-laravel)
    
* [Conclusion](#heading-conclusion)
    

### Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants :

1. Laravel 11
    
2. Un compte développeur Google.
    
3. Connaissances de base de Laravel et de l'authentification.
    
4. Composer pour gérer les packages
    

Une fois que vous avez ces prérequis prêts, vous êtes prêt à plonger dans l'intégration de l'authentification Google dans votre application Laravel.

### Avantages de l'utilisation de Google Auth dans une application Laravel

Il y a de nombreux avantages à cette configuration. Voici quelques-uns :

* Intégration simplifiée avec Socialite
    
* Authentification utilisateur transparente
    
* Sécurité améliorée
    
* Flux utilisateur personnalisable
    
* Meilleure évolutivité
    
* Support solide de l'écosystème
    
* Maintenance plus facile
    

## Comment configurer la connexion Google Laravel

Que vous travailliez sur un projet personnel ou une application prête pour la production, suivre ces étapes vous aidera à intégrer facilement l'authentification Google. Commençons.

### Étape 1 : Configurer un projet Google Cloud

Pour utiliser l'authentification Google dans votre application Laravel, vous devez d'abord configurer un projet Google Cloud. Suivez ces étapes pour configurer votre projet :

1. Visitez la [console Google Cloud](https://console.cloud.google.com/) et connectez-vous avec votre compte Google.
    
    ![Étape 1 de l'authentification Laravel](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208476305/836ff373-152a-4b99-93f3-c7684591e5c7.png align="center")
    
2. Cliquez sur le menu déroulant **"Sélectionner un projet"** dans la barre de navigation supérieure. Dans la fenêtre contextuelle, cliquez sur **"Nouveau projet"** pour créer un nouveau projet et fournissez les détails demandés. Ensuite, cliquez sur **Créer un projet**.
    
    ![Créer un projet d'authentification Laravel](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208488866/409092b9-20b5-4888-9c15-f22eff4226c8.png align="center")
    
3. Une fois que vous avez créé le projet, ouvrez le menu de gauche de la console et sélectionnez **APIs & Services > Identifiants**.
    
    ![APIs & Identifiants](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208517526/9b7df08c-8e8f-4db4-b297-a3f320edd0f0.png align="center")
    
4. Sur la page Identifiants, cliquez sur **Créer des identifiants** > **ID client OAuth**.
    
    ![ID client OAuth](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208549370/6dcd64f1-1fe4-4a8b-b37e-f74b38bd694a.png align="center")
    
5. Si c'est la première fois que vous créez un ID client, il vous demandera de configurer l'écran de consentement. Vous pouvez configurer votre écran de consentement en cliquant sur **Configurer l'écran de consentement**. Si vous avez déjà configuré l'écran de consentement, vous pouvez ignorer cette étape.
    
    * Sélectionnez **Externe** si votre application est destinée à un usage public, ou **Interne** si elle est limitée aux utilisateurs de votre organisation Google Workspace.
        
        ![Consentement OAuth](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208660871/53aaf9a2-74d4-4cca-b4e5-9c5cfa9b3066.png align="center")
        
    * Remplissez les détails requis, comme le **nom de l'application**, l'**email de support utilisateur** et toute information de marque. Cliquez sur **Enregistrer et continuer**.
        
        ![Écran de consentement OAuth](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208766209/4f458336-9a2a-4238-af89-de954ed2bcf4.png align="center")
        
    
    Après avoir configuré l'écran de consentement, retournez à la page **Identifiants** et sélectionnez à nouveau **ID client OAuth**.
    
6. Choisissez le **Type d'application** comme **Application Web** et fournissez un nom pour les identifiants du client (par exemple, Connexion sociale Laravel).
    
7. Sous **URIs de redirection autorisés**, ajoutez l'URL de rappel pour votre application :
    
    * Exemple : `http://votre-url-d-app.com/callback/google`
        
    * Si vous testez localement, utilisez : [http://127.0.0.1:8000/api/auth/google/callback](http://127.0.0.1:8000/api/auth/google/callback)
        
        ![ID client OAuth](https://cdn.hashnode.com/res/hashnode/image/upload/v1733208840271/b7c309bc-4880-481b-acda-c0fecf4a0ee5.png align="center")
        
8. Cliquez sur **Créer**, et Google générera un **ID client** et un **Secret client** pour votre projet. Enregistrez ces identifiants, car ils seront nécessaires dans les étapes suivantes.
    

### Étape 2 : Créer un nouveau projet Laravel et installer le package Laravel Socialite

Si vous n'en avez pas déjà un, vous pouvez créer un nouveau projet Laravel en utilisant la commande suivante :

```bash
composer create-project --prefer-dist laravel/laravel social-auth-example
```

Pour intégrer l'authentification Google dans un projet Laravel, nous utiliserons [Laravel Socialite](https://laravel.com/docs/11.x/socialite). Socialite est un package Laravel de première partie qui simplifie l'authentification OAuth avec des services populaires comme Google, Facebook, Twitter, et plus encore.

Pour installer Socialite, ouvrez votre terminal dans le répertoire racine de votre projet Laravel et exécutez la commande suivante :

```bash
composer require laravel/socialite
```

### Étape 3 : Configurer les variables d'environnement

Dans cette étape, nous allons configurer notre application Laravel pour utiliser les identifiants Google OAuth que nous avons collectés dans l'étape 1.

Localisez votre fichier `.env` dans le répertoire racine de votre projet et ajoutez les variables d'environnement suivantes :

```tsx
GOOGLE_CLIENT_ID=votre-id-client
GOOGLE_CLIENT_SECRET=votre-secret-client
GOOGLE_REDIRECT_URL=http://votre-domaine.com/auth/google/callback
```

Allez-y et remplacez tous les espaces réservés par les secrets.

Comprenons chaque variable d'environnement une par une :

* `GOOGLE_CLIENT_ID` : Un identifiant unique pour votre application, fourni par Google.
    
* `GOOGLE_CLIENT_SECRET` : Une clé privée utilisée par votre application pour s'authentifier de manière sécurisée avec l'API de Google.
    
* `GOOGLE_REDIRECT_URL` : L'URL où Google redirige les utilisateurs après qu'ils se sont connectés. Cela doit correspondre à l'URI de redirection que vous avez spécifié lors de la création des identifiants dans l'étape 1.
    

### Étape 4 : Mettre à jour les fichiers de configuration

Pour permettre à Laravel Socialite d'utiliser les identifiants Google OAuth, nous devons configurer les détails du fournisseur dans le fichier `config/services.php`.

Dans le fichier `services.php`, ajoutez la configuration suivante pour le fournisseur Google :

```php
'google' => [
    'client_id' => env('GOOGLE_CLIENT_ID'),        // Votre ID client Google
    'client_secret' => env('GOOGLE_CLIENT_SECRET'), // Votre secret client Google
    'redirect' => env('GOOGLE_REDIRECT_URL'),      // Votre URL de redirection Google
]
```

### Étape 5 : Créer des contrôleurs et des routes pour l'authentification.

Dans cette étape, nous allons créer un contrôleur pour gérer la redirection et les rappels OAuth de Google et configurer les routes nécessaires pour déclencher ces méthodes.

Exécutez la commande Artisan suivante pour générer le contrôleur `GoogleAuthController` :

```php
php artisan make:controller GoogleAuthController
```

Cela créera un contrôleur à l'emplacement `app/Http/Controllers/GoogleAuthController.php`.

Remplacez le contenu du fichier `GoogleAuthController.php` nouvellement créé par le code suivant :

```php
<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Models\User;
use Laravel\Socialite\Facades\Socialite;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Str;
use Throwable;

class GoogleAuthController extends Controller
{
    /**
     * Redirige l'utilisateur vers la page OAuth de Google.
     */
    public function redirect()
    {
        return Socialite::driver('google')->redirect();
    }

    /**
     * Gère le rappel de Google.
     */
    public function callback()
    {
        try {
            // Obtenir les informations de l'utilisateur depuis Google
            $user = Socialite::driver('google')->user();
        } catch (Throwable $e) {
            return redirect('/')->with('error', 'L\'authentification Google a échoué.');
        }

        // Vérifier si l'utilisateur existe déjà dans la base de données
        $existingUser = User::where('email', $user->email)->first();

        if ($existingUser) {
            // Connecter l'utilisateur s'il existe déjà
            Auth::login($existingUser);
        } else {
            // Sinon, créer un nouvel utilisateur et le connecter
            $newUser = User::updateOrCreate([
                'email' => $user->email
            ], [
                'name' => $user->name,
                'password' => bcrypt(Str::random(16)), // Définir un mot de passe aléatoire
                'email_verified_at' => now()
            ]);
            Auth::login($newUser);
        }

        // Rediriger l'utilisateur vers le tableau de bord ou toute autre page sécurisée
        return redirect('/dashboard');
    }
}
```

Ce contrôleur contient deux fonctions :

1. Redirect : Redirige l'utilisateur vers la page OAuth de Google.
    
2. Callback : Gère le rappel de Google et redirige l'utilisateur vers le tableau de bord ou toute autre page sécurisée.
    

Définissons les routes de `redirect` et `callback` dans le fichier `routes/web.php` :

```php
use App\Http\Controllers\GoogleAuthController;

// Route pour rediriger vers la page OAuth de Google
Route::get('/auth/google/redirect', [GoogleAuthController::class, 'redirect'])->name('auth.google.redirect');

// Route pour gérer le rappel de Google
Route::get('/auth/google/callback', [GoogleAuthController::class, 'callback'])->name('auth.google.callback');
```

### Étape 6 : Tester l'authentification Google Laravel dans votre projet.

Nous avons configuré l'authentification Google, il est donc temps de la tester pour nous assurer qu'elle fonctionne de manière transparente. Dans cette étape, nous utiliserons un bouton de connexion qui redirige l'utilisateur vers la page d'authentification de Google et le ramène à une route protégée après une connexion réussie.

Tout d'abord, nous ajouterons le bouton suivant qui donne aux utilisateurs la possibilité de se connecter avec Google :

```html
<a href="{{ route('auth.google.redirect') }}" class="btn bg-blue-100 p-3 shadow-sm border rounded-md text-blue-900">
	Se connecter avec Google 
</a>
```

À des fins de test, j'ai défini une route protégée et un `dashboard`. Cette route ne sera accessible qu'aux utilisateurs authentifiés. Après la connexion, nous redirigerons les utilisateurs vers cette page. Définissons cette route dans `web.php` :

```php
Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware('auth')->name('dashboard');
```

Ensuite, créez un fichier de vue blade pour le tableau de bord à l'emplacement `resources/views/dashboard.blade.php`. Voici le contenu du tableau de bord :

```html
<html>
	<head>
	    <title>Tableau de bord</title>
	</head>
	
	<body>
	    <h1>Tableau de bord</h1>
	    <p>Bienvenue sur le tableau de bord, {{ auth()->user()->name }} !</p>
	</body>

</html>
```

Ici, nous utilisons l'aide `auth()->user()` pour afficher le nom de l'utilisateur connecté, qui est récupéré depuis le compte Google qu'il a utilisé pour se connecter.

Maintenant, essayons de nous connecter.

Voici la page de connexion :

![Écran de connexion - "Se connecter avec Google"](https://cdn.hashnode.com/res/hashnode/image/upload/v1732703980184/ecc90d0d-142b-43fe-8457-1b84a54f62d3.png align="center")

En cliquant sur le bouton, vous serez redirigé vers l'écran de consentement de Google :

![Exemple d'authentification Google Laravel - écran de consentement](https://cdn.hashnode.com/res/hashnode/image/upload/v1732703936372/59f4a5bf-907d-4dda-ba8b-6909cf0a4376.png align="center")

Cliquez sur continuer, et vous devriez être connecté à l'application. Vous serez redirigé vers un écran comme ci-dessous. Vous pouvez voir le message de bienvenue avec le nom de l'utilisateur.

![Exemple d'authentification Laravel - écran de bienvenue](https://cdn.hashnode.com/res/hashnode/image/upload/v1732703886846/17ab7939-34c1-4d82-9527-99afb78cf3eb.png align="center")

C'est tout ! Vous avez réussi à implémenter et à tester l'authentification Google dans votre projet Laravel. Maintenant, vos utilisateurs peuvent se connecter en utilisant leurs comptes Google, améliorant ainsi la sécurité et la commodité.

Pour vous référer à l'implémentation complète, vous pouvez trouver le code source complet de ce projet sur GitHub ici : [**Intégration de la connexion Google pour Laravel** - Dépôt GitHub](https://github.com/DeepKumbhare85/social-auth-example)

## Conclusion

Vous avez maintenant configuré l'authentification Google dans votre application Laravel en utilisant Socialite ! Vous pouvez étendre cette méthode pour inclure d'autres fournisseurs OAuth comme Facebook, Twitter ou GitHub en ajoutant des configurations supplémentaires au fichier `config/services.php`.

L'intégration de Google OAuth est une fonctionnalité courante pour les applications web modernes, et Laravel Socialite la rend facile à implémenter.

Au cas où vous auriez besoin de plus d'options de connexion sociale comme GitHub, Twitter et Facebook, vous pouvez envisager des modèles Laravel SaaS prêts à l'emploi.

La plupart des modèles Laravel SaaS pré-construits offrent une intégration transparente avec des plateformes populaires telles que Google, GitHub, Facebook et Twitter. Par exemple, il existe des ressources premium et open source comme :

* [Laravel Starter Kit](https://demos.themeselection.com/jetship-laravel-starter-kit/) (Premium)
    
    * Basé sur Tailwind CSS
        
    * Vient avec une configuration de lien magique en un clic
        
    * Prend en charge diverses méthodes d'authentification, y compris la connexion traditionnelle par email/mot de passe
        
    * Authentification 2FA
        
* [SaaS Boilerplate](https://github.com/miracuthbert/saas-boilerplate) (Open Source)
    
    * Multi-tenancy avec une seule base de données
        
    * Panneau de développement
        
    * Gérer les jetons d'accès personnel
        
* [Laranuxt](https://github.com/fumeapp/laranuxt) (Open Source)
    
    * Nuxt UI, une collection de composants construits par l'équipe NuxtJS, alimentés par Tailwind CSS
        
    * Bibliothèque d'authentification pour aider avec les sessions utilisateur et la connexion/déconnexion
        
    * Exemple de middleware d'authentification
        
* [Laravel Vue Boilerplate](https://github.com/alefesouza/laravel-vue-boilerplate) (Open Source)
    
    * WebSockets avec Laravel Echo et Pusher.
        
    * Workbox pour un meilleur développement PWA.
        
    * Laravel GraphQL
        

L'utilisation de l'un de ces modèles Laravel SaaS peut accélérer vos flux de travail, car vous n'avez pas besoin de tout configurer à partir de zéro.

Un merci spécial à [Deep Kumbhare](https://github.com/DeepKumbhare85), un développeur Laravel expérimenté et passionné, qui m'a aidé à préparer cet article.

J'espère que cet article vous aidera à configurer la connexion Google avec Laravel.