---
title: Comment créer votre première application CRUD avec Laravel et MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T13:06:08.000Z'
originalURL: https://freecodecamp.org/news/laravel-5-7-tutorial-build-your-first-crud-app-with-laravel-and-mysql-15cbd06c6cef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xAFAiAxqZVrOVLBTo9tf6w.jpeg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: Ubuntu
  slug: ubuntu
seo_title: Comment créer votre première application CRUD avec Laravel et MySQL
seo_desc: 'By Ahmed Bouchefra

  Throughout this tutorial for beginners you’ll learn to use Laravel 5.7 — the latest
  version of one of the most popular PHP frameworks — to create a CRUD web application
  with a MySQL database from scratch. We’ll go through the proce...'
---

Par Ahmed Bouchefra

Tout au long de ce tutoriel pour débutants, vous apprendrez à utiliser Laravel 5.7 — la dernière version de l'un des frameworks PHP les plus populaires — pour créer une application web CRUD avec une base de données MySQL à partir de zéro. Nous passerons par le processus étape par étape en commençant par l'installation de Composer (gestionnaire de paquets PHP) et en continuant jusqu'à l'implémentation et le service de votre application.

### Prérequis

Ce tutoriel suppose que vous avez PHP et MySQL installés sur votre système. Suivez les instructions pour votre système d'exploitation afin d'installer les deux.

Vous devez également être familier avec le bash Linux/macOS où nous exécuterons les commandes de ce tutoriel.

La familiarité avec PHP est requise puisque Laravel est basé sur PHP.

Pour le développement, j'utiliserai une machine Ubuntu 16.04, donc les commandes de ce tutoriel ciblent ce système, mais vous devriez pouvoir suivre ce tutoriel dans n'importe quel système d'exploitation que vous utilisez.

### Installation de PHP 7.1

Laravel v5.7 nécessite PHP 7.1 ou supérieur, vous avez donc besoin de la dernière version de PHP installée sur votre système. Le processus est simple sur la plupart des systèmes.

Sur Ubuntu, vous pouvez suivre ces instructions.

Tout d'abord, ajoutez le PPA `ondrej/php` qui contient la dernière version de PHP :

```bash
$ sudo add-apt-repository ppa:ondrej/php $ sudo apt-get update
```

Ensuite, installez PHP 7.1 en utilisant la commande suivante :

```bash
$ sudo apt-get install php7.1
```

Si vous utilisez Ubuntu 18.04, PHP 7.2 est inclus dans le dépôt Ubuntu par défaut pour 18.04, vous devriez donc pouvoir l'installer en utilisant la commande suivante :

```bash
$ sudo apt-get install php
```

> _Ce tutoriel est testé avec PHP 7.1 mais vous pouvez également utiliser des versions plus récentes comme PHP 7.2 ou PHP 7.3_

### Installation des modules PHP 7.1 requis

Laravel nécessite un ensemble de modules. Vous pouvez les installer en utilisant la commande suivante :

```bash
$ sudo apt-get install php7.1 php7.1-cli php7.1-common php7.1-json php7.1-opcache php7.1-mysql php7.1-mbstring php7.1-mcrypt php7.1-zip php7.1-fpm php7.1-xml
```

### Installation de PHP Composer

Commençons notre voyage en installant Composer, le gestionnaire de paquets PHP.

Naviguez dans votre répertoire personnel, puis téléchargez l'installateur depuis le site officiel en utilisant `curl` :

```bash
$ cd ~ $ curl -sS https://getcomposer.org/installer -o composer-setup.php
```

Vous pouvez ensuite installer `composer` globalement sur votre système en utilisant la commande suivante :

```bash
$ sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```

Au moment de l'écriture, Composer 1.8 sera installé sur votre système. Vous pouvez vous assurer que votre installation fonctionne comme prévu en exécutant `composer` dans votre terminal :

Vous devriez obtenir la sortie suivante :

```bash
______  / ____/___  ____ ___  ____  ____  ________  _____ / /   / __ \/ __ `__ \/ __ \/ __ \/ ___/ _ \/ ___// /___/ /_/ / / / / / / /_/ / /_/ (__  )  __/ /\____/\____/_/ /_/ /_/ .___/\____/____/\___/_/                    /_/Composer version 1.8.0 2018-12-03 10:31:16Usage:  command [options] [arguments]Options:  -h, --help                     Display this help message  -q, --quiet                    Do not output any message  -V, --version                  Display this application version      --ansi                     Force ANSI output      --no-ansi                  Disable ANSI output  -n, --no-interaction           Do not ask any interactive question      --profile                  Display timing and memory usage information      --no-plugins               Whether to disable plugins.  -d, --working-dir=WORKING-DIR  If specified, use the given directory as working directory.  -v|vv|vvv, --verbose           Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

Pour plus d'informations, consultez ce [tutoriel](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-18-04).

Si vous avez installé Composer avec succès sur votre système, vous êtes prêt à créer un projet Laravel 5.7.

### Installation et création d'un projet Laravel 5.7

Dans cette section, nous présenterons Laravel puis procéderons à son installation et à la création d'un projet Laravel 5.7.

### À propos de Laravel

La [documentation de Laravel](https://packagist.org/packages/laravel/framework) le décrit comme :

> _Laravel est un framework d'application web avec une syntaxe expressive et élégante. Nous croyons que le développement doit être une expérience agréable et créative pour être vraiment épanouissante. Laravel tente de supprimer la douleur du développement en facilitant les tâches courantes utilisées dans la majorité des projets web, telles que :_

> _Laravel est accessible, mais puissant, fournissant les outils nécessaires pour des applications grandes et robustes._

Générer un projet Laravel 5.7 est facile et simple. Dans votre terminal, exécutez la commande suivante :

```bash
$ composer create-project --prefer-dist laravel/laravel laravel-first-crud-app
```

Cela installera `laravel/laravel` **v5.7.19**.

> **_Note_**_: Assurez-vous d'avoir au moins PHP 7.1 installé sur votre système. Sinon, composer utilisera Laravel 5.5 pour votre projet._

Vous pouvez vérifier la version installée dans votre projet en utilisant :

```bash
$ cd laravel-first-crud-app $ php artisan -V Laravel Framework 5.7.22
```

### Installation des dépendances front-end

Dans votre projet généré, vous pouvez voir qu'un fichier `package.json` est généré qui inclut de nombreuses bibliothèques front-end qui peuvent être utilisées par votre projet :

* axios,
* bootstrap,
* cross-env,
* jquery,
* laravel-mix,
* lodash,
* popper.js,
* resolve-url-loader,
* sass,
* sass-loader,
* vue.

> **_Note_**_: Vous pouvez utiliser vos bibliothèques préférées avec Laravel, pas spécifiquement celles ajoutées à `package.json`._

> _Le fichier `package.json` dans votre projet Laravel inclut quelques paquets tels que `vue` et `axios` pour vous aider à commencer à construire votre application JavaScript._

> _Il inclut également `bootstrap` pour vous aider à commencer avec Bootstrap pour styliser votre UI._

> _Il inclut [Laravel Mix](https://laravel.com/docs/5.7/mix#working-with-stylesheets) pour vous aider à compiler vos fichiers SASS en CSS simple._

Vous devez utiliser `npm` pour installer les dépendances front-end :

```bash
$ npm install
```

Après avoir exécuté cette commande, un dossier `node_modules` sera créé et les dépendances seront installées dans celui-ci.

> **_Note_**_: Vous devez avoir Node.js et npm installés sur votre système avant de pouvoir installer les dépendances front-end._

### Création d'une base de données MySQL

Créons maintenant une base de données MySQL que nous utiliserons pour persister les données dans notre application Laravel. Dans votre terminal, exécutez la commande suivante pour lancer le client `mysql` :

```bash
$ mysql -u root -p
```

Lorsque vous y êtes invité, entrez le mot de passe de votre serveur MySQL lorsque vous l'avez installé.

Ensuite, exécutez l'instruction SQL suivante pour créer une base de données `db` :

```bash
mysql> create database db;
```

Ouvrez le fichier `.env` et mettez à jour les informations d'identification pour accéder à votre base de données MySQL :

```
DB_CONNECTION=mysql DB_HOST=127.0.0.1 DB_PORT=3306 DB_DATABASE=db DB_USERNAME=root DB_PASSWORD=******
```

Vous devez entrer le nom de la base de données, le nom d'utilisateur et le mot de passe.

À ce stade, vous pouvez exécuter la commande `migrate` pour créer votre base de données et un ensemble de tables SQL nécessaires par Laravel :

> **_Note_**_: Vous pouvez exécuter la commande `migrate` à tout autre moment de votre développement pour ajouter d'autres tables SQL dans votre base de données ou pour modifier votre base de données si vous devez ajouter des modifications plus tard._

### Création de votre premier modèle Laravel

Laravel utilise le modèle architectural MVC pour organiser votre application en trois parties découplées :

* Le Modèle qui encapsule la couche d'accès aux données,
* La Vue qui encapsule la couche de représentation,
* Le Contrôleur qui encapsule le code pour contrôler l'application et communique avec les couches modèle et vue.

Le [MDN](https://developer.mozilla.org/en-US/docs/Glossary/MVC) définit MVC comme :

> **MVC** (Modèle-Vue-Contrôleur) est un modèle de conception logicielle couramment utilisé pour implémenter les interfaces utilisateur, les données et la logique de contrôle. Il met l'accent sur une séparation entre la logique métier du logiciel et l'affichage. Cette "séparation des préoccupations" permet une meilleure division du travail et une maintenance améliorée.

Maintenant, créons notre premier modèle Laravel. Dans votre terminal, exécutez la commande suivante :

```
$ php artisan make:model Contact --migration
```

Cela créera un modèle Contact et un fichier de migration. Dans le terminal, nous obtenons une sortie similaire à :

```
Model created successfully. Created Migration: 2019_01_27_193840_create_contacts_table
```

Ouvrez le fichier de migration `database/migrations/xxxxxx_create_contacts_table` et mettez-le à jour en conséquence :

```php
<?phpuse Illuminate\Support\Facades\Schema;use Illuminate\Database\Schema\Blueprint;use Illuminate\Database\Migrations\Migration;class CreateContactsTable extends Migration{    /**     * Run the migrations.     *     * @return void     */    public function up()    {        Schema::create('contacts', function (Blueprint $table) {            $table->increments('id');            $table->timestamps();            $table->string('first_name');            $table->string('last_name');            $table->string('email');            $table->string('job_title');            $table->string('city');               $table->string('country');                    });    }    /**     * Reverse the migrations.     *     * @return void     */    public function down()    {        Schema::dropIfExists('contacts');    }}
```

Nous avons ajouté les champs `first_name`, `last_name`, `email`, `job_title`, `city` et `country` dans la table `contacts`.

Vous pouvez maintenant créer la table `contacts` dans la base de données en utilisant la commande suivante :

```bash
$ php artisan migrate
```

Maintenant, regardons notre modèle `Contact`, qui sera utilisé pour interagir avec la table de base de données `contacts`. Ouvrez le fichier `app/Contact.php` et mettez-le à jour :

```php
<?phpnamespace App;use Illuminate\Database\Eloquent\Model;class Contact extends Model{    protected $fillable = [        'first_name',        'last_name',        'email',        'city',        'country',        'job_title'           ];}
```

### Création du contrôleur et des routes

Après avoir créé le modèle et migré notre base de données, créons maintenant le contrôleur et les routes pour travailler avec le modèle `Contact`. Dans votre terminal, exécutez la commande suivante :

```bash
$ php artisan make:controller ContactController --resource
```

> _Le routage des ressources Laravel attribue les routes "CRUD" typiques à un contrôleur avec une seule ligne de code. Par exemple, vous pouvez souhaiter créer un contrôleur qui gère toutes les requêtes HTTP pour les "photos" stockées par votre application. En utilisant la commande Artisan `make:controller`, nous pouvons rapidement créer un tel contrôleur._

> _Cette commande générera un contrôleur à `app/Http/Controllers/PhotoController.php`. Le contrôleur contiendra une méthode pour chacune des opérations de ressource disponibles._

Ouvrez le fichier `app/Http/Controllers/ContactController.php`. Voici le contenu initial :

```php
<?phpnamespace App\Http\Controllers;use Illuminate\Http\Request;class ContactController extends Controller{    /**     * Display a listing of the resource.     *     * @return \Illuminate\Http\Response     */    public function index()    {        //    }    /**     * Show the form for creating a new resource.     *     * @return \Illuminate\Http\Response     */    public function create()    {        //    }    /**     * Store a newly created resource in storage.     *     * @param  \Illuminate\Http\Request  $request     * @return \Illuminate\Http\Response     */    public function store(Request $request)    {        //    }    /**     * Display the specified resource.     *     * @param  int  $id     * @return \Illuminate\Http\Response     */    public function show($id)    {        //    }    /**     * Show the form for editing the specified resource.     *     * @param  int  $id     * @return \Illuminate\Http\Response     */    public function edit($id)    {        //    }    /**     * Update the specified resource in storage.     *     * @param  \Illuminate\Http\Request  $request     * @param  int  $id     * @return \Illuminate\Http\Response     */    public function update(Request $request, $id)    {        //    }    /**     * Remove the specified resource from storage.     *     * @param  int  $id     * @return \Illuminate\Http\Response     */    public function destroy($id)    {        //    }}
```

La classe `ContactController` étend la classe `Controller` disponible depuis Laravel et définit un ensemble de méthodes qui seront utilisées pour effectuer les opérations CRUD sur le modèle `Contact`.

Vous pouvez lire le rôle de la méthode dans le commentaire au-dessus.

Maintenant, nous devons fournir des implémentations pour ces méthodes.

Mais avant cela, ajoutons le routage. Ouvrez le fichier `routes/web.php` et mettez-le à jour en conséquence :

```php
<?phpRoute::get('/', function () {    return view('welcome');});Route::resource('contacts', 'ContactController');
```

En utilisant la méthode statique `resource()` de `Route`, vous pouvez créer plusieurs routes pour exposer plusieurs actions sur la ressource.

Ces routes sont mappées à diverses méthodes `ContactController` que nous devrons implémenter dans la section suivante :

* GET `/contacts`, mappé à la méthode `index()`,
* GET `/contacts/create`, mappé à la méthode `create()`,
* POST `/contacts`, mappé à la méthode `store()`,
* GET `/contacts/{contact}`, mappé à la méthode `show()`,
* GET `/contacts/{contact}/edit`, mappé à la méthode `edit()`,
* PUT/PATCH `/contacts/{contact}`, mappé à la méthode `update()`,
* DELETE `/contacts/{contact}`, mappé à la méthode `destroy()`.

Ces routes sont utilisées pour servir des modèles HTML et également comme points de terminaison d'API pour travailler avec le modèle `Contact`.

> **_Note_**_: Si vous souhaitez créer un contrôleur qui n'exposera qu'une API RESTful, vous pouvez utiliser la méthode `apiResource` pour exclure les routes qui sont utilisées pour servir les modèles HTML :_

```php
Route::apiResource('contacts', 'ContactController');
```

### Implémentation des opérations CRUD

Implémentons maintenant les méthodes du contrôleur ainsi que les vues.

### C : Implémentation de l'opération de création et ajout d'un formulaire

Le `ContactController` inclut

* la méthode `store()` qui mappe à l'API endpoint `POST /contacts` qui sera utilisée pour créer un contact dans la base de données, et
* la méthode `create()` qui mappe à la route `GET /contacts/create` qui sera utilisée pour servir le formulaire HTML utilisé pour soumettre le contact à l'API endpoint `POST /contacts`.

Implémentons ces deux méthodes.

Rouvrez le fichier `app/Http/Controllers/ContactController.php` et commencez par importer le modèle `Contact` :

```php
use App\Contact;
```

Ensuite, localisez la méthode `store()` et mettez-la à jour en conséquence :

```php
public function store(Request $request)    {        $request->validate([            'first_name'=>'required',            'last_name'=>'required',            'email'=>'required'        ]);        $contact = new Contact([            'first_name' => $request->get('first_name'),            'last_name' => $request->get('last_name'),            'email' => $request->get('email'),            'job_title' => $request->get('job_title'),            'city' => $request->get('city'),            'country' => $request->get('country')        ]);        $contact->save();        return redirect('/contacts')->with('success', 'Contact saved!');    }
```

Ensuite, localisez la méthode `create()` et mettez-la à jour :

```php
public function create() { return view('contacts.create'); }
```

La fonction `create()` utilise la méthode `view()` pour retourner le modèle `create.blade.php` qui doit être présent dans le dossier `resources/views`.

Avant de créer le modèle `create.blade.php`, nous devons créer un modèle de base qui sera étendu par le modèle de création et tous les autres modèles que nous créerons plus tard dans ce tutoriel.

Dans le dossier `resources/views`, créez un fichier `base.blade.php` :

```bash
$ cd resources/views $ touch base.blade.php
```

Ouvrez le fichier `resources/views/base.blade.php` et ajoutez le modèle blade suivant :

```html
<!DOCTYPE html><html lang="en"><head>  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <title>Laravel 5.7 & MySQL CRUD Tutorial</title>  <link href="{{ asset('css/app.css') }}" rel="stylesheet" type="text/css" /></head><body>  <div class="container">    @yield('main')  </div>  <script src="{{ asset('js/app.js') }}" type="text/js"></script></body></html>
```

Maintenant, créons le modèle `create.blade.php`. Tout d'abord, créez un dossier contacts dans le dossier views :

```bash
$ mkdir contacts
```

Ensuite, créez le modèle

```bash
$ cd contacts $ touch create.blade.php
```

Ouvrez le fichier `resources/views/contacts/create.blade.php` et ajoutez le code suivant :

```php
@extends('base')@section('main')<div class="row"> <div class="col-sm-8 offset-sm-2">    <h1 class="display-3">Add a contact</h1>  <div>    @if ($errors->any())      <div class="alert alert-danger">        <ul>            @foreach ($errors->all() as $error)              <li>{{ $error }}</li>            @endforeach        </ul>      </div><br />    @endif      <form method="post" action="{{ route('contacts.store') }}">          @csrf          <div class="form-group">                  <label for="first_name">First Name:</label>              <input type="text" class="form-control" name="first_name"/>          </div>          <div class="form-group">              <label for="last_name">Last Name:</label>              <input type="text" class="form-control" name="last_name"/>          </div>          <div class="form-group">              <label for="email">Email:</label>              <input type="text" class="form-control" name="email"/>          </div>          <div class="form-group">              <label for="city">City:</label>              <input type="text" class="form-control" name="city"/>          </div>          <div class="form-group">              <label for="country">Country:</label>              <input type="text" class="form-control" name="country"/>          </div>          <div class="form-group">              <label for="job_title">Job Title:</label>              <input type="text" class="form-control" name="job_title"/>          </div>                                   <button type="submit" class="btn btn-primary-outline">Add contact</button>      </form>  </div></div></div>@endsection
```

Voici une capture d'écran de notre formulaire de création !

![Image](https://cdn-media-1.freecodecamp.org/images/-RNUu-7wdVnznYFz81jAGskP80HRSWh4vlNs)

Remplissez le formulaire et cliquez sur le bouton **Add contact** pour créer un contact dans la base de données. Vous devriez être redirigé vers la route /contacts qui n'a pas encore de vue associée.

### R : Implémentation de l'opération de lecture et obtention des données

Ensuite, implémentons l'opération de lecture pour obtenir et afficher les données des contacts de notre base de données MySQL.

Allez dans le fichier `app/Http/Controllers/ContactController.php`, localisez la méthode `index()` et mettez-la à jour :

```php
public function index()    {        $contacts = Contact::all();        return view('contacts.index', compact('contacts'));    }
```

Ensuite, vous devez créer le modèle d'index. Créez un fichier `resources/views/contacts/index.blade.php` :

```bash
$ touch index.blade.php
```

Ouvrez le fichier `resources/views/contacts/index.blade.php` et ajoutez le code suivant :

```php
@extends('base')@section('main')<div class="row"><div class="col-sm-12">    <h1 class="display-3">Contacts</h1>      <table class="table table-striped">    <thead>        <tr>          <td>ID</td>          <td>Name</td>          <td>Email</td>          <td>Job Title</td>          <td>City</td>          <td>Country</td>          <td colspan = 2>Actions</td>        </tr>    </thead>    <tbody>        @foreach($contacts as $contact)        <tr>            <td>{{$contact->id}}</td>            <td>{{$contact->first_name}} {{$contact->last_name}}</td>            <td>{{$contact->email}}</td>            <td>{{$contact->job_title}}</td>            <td>{{$contact->city}}</td>            <td>{{$contact->country}}</td>            <td>                <a href="{{ route('contacts.edit',$contact->id)}}" class="btn btn-primary">Edit</a>            </td>            <td>                <form action="{{ route('contacts.destroy', $contact->id)}}" method="post">                  @csrf                  @method('DELETE')                  <button class="btn btn-danger" type="submit">Delete</button>                </form>            </td>        </tr>        @endforeach    </tbody>  </table><div></div>@endsection
```

### U : Implémentation de l'opération de mise à jour

Ensuite, nous devons implémenter l'opération de mise à jour. Allez dans le fichier `app/Http/Controllers/ContactController.php`, localisez la méthode `edit($id)` et mettez-la à jour :

```php
public function edit($id)    {        $contact = Contact::find($id);        return view('contacts.edit', compact('contact'));            }
```

Ensuite, vous devez implémenter la méthode `update()` :

```php
public function update(Request $request, $id)    {        $request->validate([            'first_name'=>'required',            'last_name'=>'required',            'email'=>'required'        ]);        $contact = Contact::find($id);        $contact->first_name =  $request->get('first_name');        $contact->last_name = $request->get('last_name');        $contact->email = $request->get('email');        $contact->job_title = $request->get('job_title');        $contact->city = $request->get('city');        $contact->country = $request->get('country');        $contact->save();        return redirect('/contacts')->with('success', 'Contact updated!');    }
```

Maintenant, vous devez ajouter le modèle d'édition. Dans le dossier `resources/views/contacts/`, créez un fichier `edit.blade.php` :

```bash
$ touch edit.blade.php
```

Ouvrez le fichier `resources/views/contacts/edit.blade.php` et ajoutez ce code :

```php
@extends('base') @section('main')<div class="row">    <div class="col-sm-8 offset-sm-2">        <h1 class="display-3">Update a contact</h1>        @if ($errors->any())        <div class="alert alert-danger">            <ul>                @foreach ($errors->all() as $error)                <li>{{ $error }}</li>                @endforeach            </ul>        </div>        <br />         @endif        <form method="post" action="{{ route('contacts.update', $contact->id) }}">            @method('PATCH')             @csrf            <div class="form-group">                <label for="first_name">First Name:</label>                <input type="text" class="form-control" name="first_name" value={{ $contact->first_name }} />            </div>            <div class="form-group">                <label for="last_name">Last Name:</label>                <input type="text" class="form-control" name="last_name" value={{ $contact->last_name }} />            </div>            <div class="form-group">                <label for="email">Email:</label>                <input type="text" class="form-control" name="email" value={{ $contact->email }} />            </div>            <div class="form-group">                <label for="city">City:</label>                <input type="text" class="form-control" name="city" value={{ $contact->city }} />            </div>            <div class="form-group">                <label for="country">Country:</label>                <input type="text" class="form-control" name="country" value={{ $contact->country }} />            </div>            <div class="form-group">                <label for="job_title">Job Title:</label>                <input type="text" class="form-control" name="job_title" value={{ $contact->job_title }} />            </div>            <button type="submit" class="btn btn-primary">Update</button>        </form>    </div></div>@endsection
```

### D : Implémentation de l'opération de suppression

Enfin, nous procéderons à l'implémentation de l'opération de suppression. Allez dans le fichier `app/Http/Controllers/ContactController.php`, localisez la méthode `destroy()` et mettez-la à jour en conséquence :

```php
public function destroy($id)    {        $contact = Contact::find($id);        $contact->delete();        return redirect('/contacts')->with('success', 'Contact deleted!');    }
```

Vous pouvez remarquer que lorsque nous redirigeons vers la route `/contacts` dans nos méthodes d'API CRUD, nous passons également un message de succès mais il n'apparaît pas dans notre modèle `index`. Changeons cela !

Allez dans le fichier `resources/views/contacts/index.blade.php` et ajoutez le code suivant :

```html
<div class="col-sm-12">  @if(session()->get('success'))    <div class="alert alert-success">      {{ session()->get('success') }}      </div>  @endif</div>
```

Nous devons également ajouter un bouton pour nous emmener au formulaire de création. Ajoutez ce code sous l'en-tête :

```html
<div>    <a style="margin: 19px;" href="{{ route('contacts.create')}}" class="btn btn-primary">New contact</a></div>
```

Voici une capture d'écran de la page après avoir créé un contact :

![Image](https://cdn-media-1.freecodecamp.org/images/u0BBQCteFr4ss8hw5Xnehpi2yXRFe1lQ1eP9)

### Conclusion

Nous avons atteint la fin de ce tutoriel. Nous avons créé une application CRUD avec Laravel 5.7, PHP 7.1 et MySQL.

J'espère que vous avez apprécié le tutoriel et je vous retrouve dans le prochain !