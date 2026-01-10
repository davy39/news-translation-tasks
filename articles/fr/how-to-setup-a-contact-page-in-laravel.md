---
title: Comment configurer une page de contact dans Laravel avec et sans pièces jointes
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-07-29T16:26:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-contact-page-in-laravel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c997d740569d1a4ca2005.jpg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment configurer une page de contact dans Laravel avec et sans pièces
  jointes
seo_desc: 'I recently struggled a bit when trying to set up a contact page in Laravel.
  So I figured that I should blog about my experience, as it might help someone who
  wants to do the same.

  Laravel is an open source PHP framework used to develop web applicatio...'
---

J'ai récemment eu un peu de mal à configurer une page de contact dans Laravel. J'ai donc pensé que je devrais bloguer sur mon expérience, car cela pourrait aider quelqu'un qui souhaite faire de même.

Laravel est un framework PHP [open source](https://opensource.com/resources/what-open-source) utilisé pour développer des applications web. Il suit le modèle architectural modèle-vue-contrôleur.

## Prérequis

1. [Installer composer](https://getcomposer.org/download/)
2. Configurer votre serveur local ([xampp](https://www.apachefriends.org/download.html), [wamp](https://www.wampserver.com/en/download-wampserver-64bits/))
3. Assurez-vous d'avoir un éditeur de code installé ([sublime text](https://www.sublimetext.com/3), [vs code](https://code.visualstudio.com/download), [atom](https://atom.io/) etc)
4. Installer [Git](https://git-scm.com/downloads) (permet le contrôle de source et la gestion de versions)

## Getting Started 

Avec Git installé, vous avez accès à Git bash. Avec bash ouvert, vous pouvez travailler avec le terminal pour exécuter des commandes qui vous permettent d'installer et d'utiliser Laravel et ses packages facilement. 

## Installer Laravel via composer

Une fois que vous avez satisfait toutes les conditions ci-dessus, nous utiliserons la commande suivante pour configurer l'installateur Laravel :

```
composer global require laravel/installer
```

La commande ci-dessus nous permet de télécharger l'installateur Laravel en utilisant composer que nous avons installé précédemment.

```
laravel new project_name

```

Ce processus d'installation prend un certain temps, alors soyez patient. **Notez** que l'installation sera effectuée dans le répertoire que vous spécifiez dans votre terminal bash ou tout autre terminal que vous choisissez d'utiliser.

## Générer un échafaudage d'authentification de base 

Une fois que nous avons une copie de l'application Laravel installée, nous devrions générer un échafaudage d'authentification de base.

```
cd project_name

composer require laravel/ui

php artisan ui vue --auth
```

La commande ci-dessus installera la vue de mise en page, la vue d'inscription et la vue de connexion, ainsi que les routes pour toutes les authentifications utilisateur.

## Configuration des variables d'environnement dans le fichier .env 

Ensuite, nous devons configurer nos variables d'environnement et établir une connexion à notre base de données (**dans cet article, nous utiliserons une adresse IP fictive partagée**).

```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=server_username
DB_PASSWORD=server_password


MAIL_DRIVER=smtp
MAIL_HOST=domain.com
MAIL_PORT=465
MAIL_USERNAME=noreply@domain.com
MAIL_PASSWORD=domain_password
MAIL_ENCRYPTION=ssl
MAIL_FROM_ADDRESS=noreply@domain.com
MAIL_FROM_NAME="${APP_NAME}"
```

Nous avons maintenant terminé la configuration de la connexion à la base de données. Dans mon cas, je travaille avec Xampp où j'ai `DB_USERNAME=root` et `DB_PASSWORD=`. N'oubliez pas non plus de démarrer votre serveur local comme indiqué ci-dessous. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/xampp.PNG)
_Image du serveur xampp_

## Versioning de la base de données et démarrage du serveur de développement 

Avant de pouvoir exécuter des migrations dans Laravel, vous devez établir une connexion à votre base de données. Puisque j'ai spécifié `your_database_name` dans la configuration .env ci-dessus, je peux cliquer sur "créer" et phpMyAdmin construira une base de données vide.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/your_database_name.PNG)
_Ajout d'un nom de base de données_

Dans Git bash, naviguez ou cd dans le répertoire `project_name` et exécutez la commande suivante :

```
cd project_name

php artisan migrate 
```

Cela exécutera toutes les migrations Laravel par défaut dans notre application tant que vous avez créé une `DB_DATABASE` correspondante que nous avons créée ci-dessus. 

```
php artisan serve
```

Nous pouvons maintenant démarrer notre serveur de développement : 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/php-artisan-serve.PNG)
_Démarrage du serveur de développement_

## Création d'un fichier contact.blade.php

Configurer une page de contact dans le **dossier resources > views** comme ceci :

```php
@extends('layouts.client.app')

@section('content')

<!-- section contact -->
    <div class="contact">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-7 col-lg-8 col-md-8">
                    <div class="section-title">
                        <h2>Contactez-nous</h2>
                    </div>
                </div>
            </div>

            @if(session('status'))
            <div class="row justify-content-center">
                <div class="col-xl-8 col-lg-8 col-md-8">
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Succès ! </strong>  &nbsp; {{ session('status') }}
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                </div>
            </div>
            @endif
        </div>
    </div>
@endsection

```

L'extrait de code ci-dessus étendra un fichier de mise en page contenant la section d'en-tête. Il contient également le titre de la section "Contactez-nous" ainsi qu'un message qui est retourné et affiché à l'utilisateur si et seulement si le message a été envoyé avec succès.  

L'accent principal ici est sur la section du formulaire que vous pouvez voir dans l'extrait de code suivant :

```php
<div class="row justify-content-center">
    <div class="col-xl-8 col-lg-8">
        <div class="login-form">
            <form method="POST" action="{{ route('addContact') }}" enctype="multipart/form-data">
                @csrf
                <div class="row">

                    <div class="col-6">
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Nom Complet') }}</label>

                            <input type="text" class="form-control @error('fullname') is-invalid @enderror" name="fullname" value="{{ isset(Auth::user()->firstname) ? Auth::user()->firstname : '' }} {{ isset(Auth::user()->lastname) ? Auth::user()->lastname : '' }}" required autocomplete="Fullname" autofocus>

                            @error('fullname')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>
                    
                    <div class="col-6">

                        <div class="form-group">
                            <label for="email" class="col-form-label text-md-right">{{ __('Adresse Email') }}</label>

                            <input type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ isset(Auth::user()->email) ? Auth::user()->email : '' }}" required autocomplete="email" autofocus>

                            @error('email')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    
                    </div>

                    <div class="col-6">
                        
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Numéro de Téléphone') }}</label>

                            <input type="text" class="form-control @error('phone_number') is-invalid @enderror" name="phone_number" value="{{ isset(Auth::user()->phone_number) ? Auth::user()->phone_number : '' }}" required autocomplete="phone_number" autofocus>

                            @error('phone_number')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                
                    
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Sujet') }}</label>

                            <input type="text" class="form-control @error('subject') is-invalid @enderror" name="subject" required autofocus>

                            @error('subject')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                        <div class="form-group">

                            <label for="password" class="col-form-label text-md-right">{{ __('Message') }}</label>

                            <textarea class="form-control @error('message') is-invalid @enderror" name="message" required></textarea>

                            @error('message')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                    </div>

                    <div class="col-6">
                
                        <div class="form-group">
                            <label for="name" class="col-form-label text-md-right">{{ __('Joindre une Capture d\'écran') }}</label>

                            <input type="file" accept="image/*" class="form-control @error('screenshot') is-invalid @enderror" name="screenshot" autofocus>

                        </div>
                    </div>
                </div>

                <div class="form-group row mb-0">
                    <div class="col-md-6 offset-md-4">
                        <button type="submit" class="btn btn-primary">
                            {{ __('Envoyer le Message') }}
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
```

L'extrait ci-dessus contient les différents champs de saisie que nous utiliserons pour traiter les informations de l'utilisateur. Les champs incluent NOM COMPLET, ADRESSE EMAIL, NUMÉRO DE TÉLÉPHONE, SUJET ou OBJET, MESSAGE, TÉLÉCHARGEMENT D'IMAGE (le cas échéant) et enfin un bouton ENVOYER LE MESSAGE pour traiter la soumission du formulaire. 

Ensuite, nous fusionnerons les deux extraits de code pour les rendre plus significatifs.

```php
@extends('layouts.client.app')
@section('content')
<div class="contact">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-xl-7 col-lg-8 col-md-8">
                <div class="section-title">
                    <h2>Contactez-nous</h2>
                </div>
            </div>
        </div>

        @if(session('status'))
        <div class="row justify-content-center">
            <div class="col-xl-8 col-lg-8 col-md-8">
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Succès ! </strong>  &nbsp; {{ session('status') }}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div>
        </div>
        @endif
        <div class="row justify-content-center">
                <div class="col-xl-8 col-lg-8">
                    <div class="login-form">
                        <form method="POST" action="{{ route('addContact') }}" enctype="multipart/form-data">
                            @csrf
                            <div class="row">

                                <div class="col-6">
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Nom Complet') }}</label>

                                        <input type="text" class="form-control @error('fullname') is-invalid @enderror" name="fullname" value="{{ isset(Auth::user()->firstname) ? Auth::user()->firstname : '' }} {{ isset(Auth::user()->lastname) ? Auth::user()->lastname : '' }}" required autocomplete="Fullname" autofocus>

                                        @error('fullname')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>
                                
                                <div class="col-6">

                                    <div class="form-group">
                                        <label for="email" class="col-form-label text-md-right">{{ __('Adresse Email') }}</label>

                                        <input type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ isset(Auth::user()->email) ? Auth::user()->email : '' }}" required autocomplete="email" autofocus>

                                        @error('email')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                
                                </div>

                                <div class="col-6">
                                    
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Numéro de Téléphone') }}</label>

                                        <input type="text" class="form-control @error('phone_number') is-invalid @enderror" name="phone_number" value="{{ isset(Auth::user()->phone_number) ? Auth::user()->phone_number : '' }}" required autocomplete="phone_number" autofocus>

                                        @error('phone_number')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                            
                                
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Sujet') }}</label>

                                        <input type="text" class="form-control @error('subject') is-invalid @enderror" name="subject" required autofocus>

                                        @error('subject')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                                    <div class="form-group">

                                        <label for="password" class="col-form-label text-md-right">{{ __('Message') }}</label>

                                        <textarea class="form-control @error('message') is-invalid @enderror" name="message" required></textarea>

                                        @error('message')
                                            <span class="invalid-feedback" role="alert">
                                                <strong>{{ $message }}</strong>
                                            </span>
                                        @enderror
                                    </div>
                                </div>

                                <div class="col-6">
                            
                                    <div class="form-group">
                                        <label for="name" class="col-form-label text-md-right">{{ __('Joindre une Capture d\'écran') }}</label>

                                        <input type="file" accept="image/*" class="form-control @error('screenshot') is-invalid @enderror" name="screenshot" autofocus>

                                    </div>
                                </div>
                            </div>

                            <div class="form-group row mb-0">
                                <div class="col-md-6 offset-md-4">
                                    <button type="submit" class="btn btn-primary">
                                        {{ __('Envoyer le Message') }}
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
        </div>
    </div>
</div>
@endsection
```

L'image ci-dessous est une simple mise en page de ce à quoi ressemble la page de contact pour le moment. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Contact-us-2.PNG)
_Page de contact_

## Ajouter des routes pour activer les requêtes GET & POST 

Tout d'abord, nous configurerons les routes dans **routes > web.php** pour rendre la page de contact via une requête **GET** et envoyer des emails via la requête **POST** (qui a été spécifiée dans l'attribut du formulaire ci-dessus).

```php
Route::get('/contact', 'HomeController@index')->name('contact');

Route::post('/contact', 'HomeController@send_mail')->name('addContact');
```

## Ajout de logique dans le HomeController  

Dans **app > Http > Controllers**, Laravel scaffold a généré un HomeController. 

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
	public function index()
    {
        return view('template.client.contact'); //affiche la page de contact
    }
   
}
```

Le fichier Controller est l'endroit où réside la logique de l'application. Laravel Scaffold a déjà généré le HomeController par défaut. Nous allons donc nous en contenter et créer une fonction nommée `index`. Nous l'utiliserons pour afficher la page de contact chaque fois que l'utilisateur visite la route ou l'URL dans l'application.

```php
<?php

use Illuminate\Support\Facades\Mail;

use App\Mail\ContactFormMail;

class HomeController extends Controller
{
    public function send_mail(Request $request)
    {
        $this->validate($request, [
            'fullname' => ['required', 'string', 'max:255' ], 
            'email' => ['required', 'string', 'email', 'max:255' ],
            'phone_number' => ['string', 'max:255'],
            'subject' => ['required', 'string', 'max:255'],
            'message' => ['required', 'string', 'max:255']
        ]);

        $contact = [
            'fullname' => $request['fullname'], 
            'email' => $request['email'],
            'phone_number' => $request['phone_number'],
            'subject' => $request['subject'],
            'message' => $request['message'],
            'screenshot' => $request->file('screenshot')->store('contact', 'public')
        ];

    
        Mail::to('receipent@domain.com')->send(new ContactFormMail($contact));
        
        return redirect()->route('contact')->with('status', 'Votre email a été reçu');
    }
}
```

Dans le même HomeController, nous devons créer une autre fonction nommée `send_mail`. La fonction validera toutes les entrées de l'utilisateur et vérifiera que les champs ne sont pas laissés vides et que les bonnes données sont analysées. 

Ensuite, créez une variable appelée `$create` pour stocker les valeurs de tableau de toutes les données utilisateur, y compris les téléchargements d'images. 

Laravel est livré avec un système de fichiers qui nous permet de travailler facilement avec les images. Le `Mail::to(....)` et `send` sont livrés avec Illuminate\Support\Facade que j'ai inclus en haut de l'extrait. J'ai également inclus un Mailable, que je vais expliquer bientôt. 

Nous devons maintenant alerter les utilisateurs lorsque le message a été envoyé et les rediriger. 

En rassemblant les extraits de code maintenant, le HomeController ressemblera à ceci :

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Illuminate\Support\Facades\Mail;

use App\Mail\ContactFormMail;

class HomeController extends Controller
{
	public function index()
    {
        return view('template.client.contact'); //affiche la page de contact
    }
    
    public function send_mail(Request $request)
    {
        $this->validate($request, [
            'fullname' => ['required', 'string', 'max:255' ], 
            'email' => ['required', 'string', 'email', 'max:255' ],
            'phone_number' => ['string', 'max:255'],
            'subject' => ['required', 'string', 'max:255'],
            'message' => ['required', 'string', 'max:255']
        ]);

        $contact = [
            'fullname' => $request['fullname'], 
            'email' => $request['email'],
            'phone_number' => $request['phone_number'],
            'subject' => $request['subject'],
            'message' => $request['message'],
            'screenshot' => $request->file('screenshot')->store('contact', 'public')
        ];

    
        Mail::to('receipent@domain.com')->send(new ContactFormMail($contact));
        
        return redirect()->route('contact')->with('status', ' Votre email a été reçu');
    }
}
```

Après avoir fusionné les deux fonctions ci-dessus, nous avons terminé la logique pour le HomeController. Passons maintenant à l'étape suivante. 

## Génération d'un [Laravel Mailable](https://laravel.com/docs/7.x/mail) 

Chaque email envoyé dans l'application Laravel est représenté comme un "mailable", au cas où vous vous poseriez des questions sur le nom. Créons un mailable markdown pour les informations de contact que nous voulons traiter :

```php
php artisan make:mail ContactFormMail --markdown=template.client.contactform
```

La commande ci-dessus générera un fichier markdown dans le répertoire **resources > views > template > client** et créera également un fichier mailable dans **app > Mail > ContactFormMail.php**.

Dans ContactFormMail.php, nous avons l'extrait de code suivant qui nous permet d'envoyer des emails **sans** pièce jointe :

```php
<?php

namespace App\Mail;
use App\User;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class ContactFormMail extends Mailable
{
    use Queueable, SerializesModels;

    /**
    * Créer une nouvelle instance de message.
    *
    * @return void
    */

    public function __construct($data)
    {
        $this->user = $data;
    }

    /**
     * Construire le message.
     *
     * @return $this
     */
    public function build()
    {
        return $this->from('noreply@domain.com')
                ->markdown('template.client.contactform')
                ->with([
                        'subject' => $this->user['subject'],
                        'message' => $this->user['message'],
                        'email' => $this->user['email'],
                        'phone_number' => $this->user['phone_number'],
                        'fullname' => $this->user['fullname'],
                    ]);
    }
}

```

Décortiquons un peu ce code.

Dans la méthode `**_construct**`, je parse toutes les données utilisateur comme paramètre et les réassigne. Dans la méthode `**build**`, toute la configuration de la classe mailable est effectuée.

La méthode `**from**` spécifie l'expéditeur du mail, c'est-à-dire qui envoie le mail (dans mon cas **noreply@domain.com**).

La méthode `**with**` vous permet de choisir de personnaliser la manière dont les mails seront rendus dans le markdown qui a été généré. Dans cet article, nous allons assigner tous les champs à des paires clé-valeur dans le tableau afin que dans le markdown, nous puissions accéder à chaque valeur avec sa propre clé unique.

La méthode `**markdown**` accepte le nom du modèle markdown à rendre avec un paramètre de données optionnel (si nous n'utilisions pas la méthode `**with**`).

Et enfin, la méthode `**to**` spécifie le destinataire du mail. Dans le HomeController ci-dessus, changez 'receipent@domain.com' par l'adresse réelle du destinataire.

## Ajout de données au fichier Markdown  

Maintenant, nous devons configurer le fichier markdown dans le répertoire **resources > views > template > client**. Puisque nous avons déjà des paires clé-valeur en place, il est plus facile de les référencer avec des clés dans le fichier markdown comme montré ci-dessous :

```php
@component('mail::message')
# {{$subject}}

## {{$message}}

N'hésitez pas à me contacter via {{$phone}} ou {{$email}}

Merci,<br>
{{$fullname}}

{{ config('app.name') }}
@endcomponent
```

À ce stade, nous avons presque terminé 💡. Félicitations pour avoir suivi le processus jusqu'ici. Vous avez maintenant appris à envoyer un email sans pièce jointe. Maintenant, voyons comment le faire avec une pièce jointe.

## Envoyer des mails avec une pièce jointe

Laravel est déjà livré avec un [système de fichiers](https://laravel.com/docs/7.x/filesystem) puissant, donc envoyer des mails avec une pièce jointe n'est pas trop difficile. Nous allons utiliser cette fonctionnalité et créer un stockage pour les utilisateurs où nous stockerons leurs fichiers joints dans l'application.  

```php
php artisan storage:link
```

**NOTE** : Dans le HomeController ci-dessus, j'ai déjà spécifié un répertoire de stockage pour les téléchargements. Vous devriez faire de même en créant un dossier (appelé **contact**) dans **storage > app > public > contact** .

De plus, dans **config > filesystems.php**, vérifiez et assurez-vous que le disque du système de fichiers par défaut est défini sur `return ['default' => 'public']`.

Maintenant, le **[Cont](https://www.freecodecamp.org/news/p/7a16e74f-8e36-4e21-9344-feba5c03da08/ContactFormMail.php)actFormMail.php** ressemble à ceci. Nous sommes maintenant en mesure d'utiliser la méthode `attachFromStorage` qui fait référence au chemin du fichier.

```php
<?php

namespace App\Mail;
use App\User;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class ContactFormMail extends Mailable
{
    use Queueable, SerializesModels;

    /**
    * Créer une nouvelle instance de message.
    *
    * @return void
    */
    public $user;

    public function __construct($data)
    {
        $this->user = $data;
    }

    /**
     * Construire le message.
     *
     * @return $this
     */
    public function build()
    {
        return $this->from('noreply@domain.com')
                ->markdown('template.client.contactform')
                ->attachFromStorage($this->user['screenshot'])
                ->with([
                        'subject' => $this->user['subject'],
                        'message' => $this->user['message'],
                        'email' => $this->user['email'],
                        'phone_number' => $this->user['phone_number'],
                        'fullname' => $this->user['fullname']
                    ]);
    }
}

```

La seule addition ici sera **attachFromStorage.** Il est utilisé pour traiter les fichiers joints (soit une image ou un pdf) pendant tout le processus d'envoi de mail. 

Dans le fichier markdown que nous avons utilisé précédemment, nous pouvons le retravailler légèrement pour qu'il ressemble à ce qui est montré ci-dessous :

```
<div class="row">
	<h1 class="text-dark">{{$subject}}</h1>

	<h3>{{$message}}</h3> 

	<h4>Vous pouvez me joindre par mail ou téléphone : {{$email}} ou {{$phone_number}}<br/>
	Merci
	</h4>
</div>



```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_20200724-180046.png)
_Capture d'écran d'un message mail réussi_

Yaaay, nous pouvons maintenant faire une danse de la joie car nous avons enfin terminé 💃🕺💃

<iframe src="https://giphy.com/embed/zQLjk9d31jlMQ" width="480" height="262" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dancing-dance-woo-zQLjk9d31jlMQ">via GIPHY</a></p>

Maintenant que vous avez parcouru l'ensemble de l'article, vous devriez être en mesure de mettre en œuvre une fonctionnalité d'envoi de mail similaire dans vos applications Laravel. 

Pour en savoir plus, vous pouvez consulter la documentation officielle de [Laravel ici.](https://laravel.com/docs/)