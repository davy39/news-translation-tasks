---
title: Comment créer une application de chat en temps réel avec Laravel Reverb
subtitle: ''
author: San B
co_authors: []
series: null
date: '2024-03-27T18:13:43.000Z'
originalURL: https://freecodecamp.org/news/laravel-reverb-realtime-chat-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/laravel-reverb-react-chat-boolfalse.png
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment créer une application de chat en temps réel avec Laravel Reverb
seo_desc: 'In March of 2024, Laravel 11 was released. And with it arrived a new tool
  in the Laravel ecosystem: Laravel Reverb.

  Reverb is a separate open-source package that''s a first-party WebSocket server
  for Laravel applications. It helps facilitate real-time...'
---

En mars 2024, [Laravel 11 a été publié](https://blog.laravel.com/laravel-11-now-available). Et avec lui est arrivé un nouvel outil dans l'écosystème Laravel : [Laravel Reverb](https://reverb.laravel.com/).

Reverb est un package open-source séparé qui est un serveur WebSocket de première partie pour les applications Laravel. Il aide à faciliter la communication en temps réel entre le client et le serveur.

Avant ce nouveau package, Laravel avait la diffusion d'événements, mais fondamentalement, il n'avait pas de moyen intégré pour configurer un serveur WebSocket auto-hébergé. Heureusement, Reverb nous donne maintenant cette option.

Laravel Reverb a quelques caractéristiques clés : il est écrit en PHP, il est rapide et il est scalable. Il a été développé en particulier pour être scalable horizontalement. 

Reverb permet essentiellement d'exécuter une application sur un seul serveur – mais si l'application commence à dépasser ce serveur, vous pouvez ajouter plusieurs serveurs supplémentaires. Ensuite, ces serveurs peuvent tous communiquer entre eux pour distribuer les messages entre eux.

Dans cet article, vous apprendrez à créer une application de chat en temps réel en utilisant Laravel Reverb. Cela vous permettra d'implémenter facilement des communications WebSocket entre votre backend et votre frontend. 

Pour une technologie frontend, vous pouvez utiliser ce que vous voulez – mais dans ce cas, nous utiliserons React.js avec l'outil de construction Vite.js.

À la fin de cet article, vous aurez une application full-stack en temps réel sur votre machine locale, qui fonctionnera comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/article-video-1.gif)
_Démonstration de l'application montrant l'échange de messages entre deux utilisateurs connectés_

## **Table des matières**

* [Prérequis](#heading-prerequis)
* [Étapes générales](#heading-etapes-generales)
* [Comment installer Laravel](#heading-comment-installer-laravel)
* [Comment créer le modèle et la migration](#heading-comment-creer-le-modele-et-la-migration)
* [Comment ajouter l'authentification](#heading-comment-ajouter-lauthentification)
* [Comment configurer les routes](#heading-comment-configurer-les-routes)
* [Comment configurer un événement Laravel](#heading-comment-configurer-un-evenement-laravel)
* [Comment configurer un travail de file d'attente Laravel](#heading-comment-configurer-un-travail-de-file-dattente-laravel)
* [Comment écrire les méthodes du contrôleur](#heading-comment-ecrire-les-methodes-du-controleur)
* [Comment installer Laravel Reverb](#heading-comment-installer-laravel-reverb)
* [Comment configurer les canaux WebSocket](#heading-comment-configurer-les-canaux-websocket)
* [Comment personnaliser les vues Laravel](#heading-comment-personnaliser-les-vues-laravel)
* [Travaillons sur le frontend](#lets-work-on-the-front-end)
* [Exécuter l'application](#heading-executer-lapplication)
* [Ressources utiles sur Reverb](#heading-ressources-utiles-sur-reverb)
* [Conclusion](#heading-conclusion)

## Prérequis

Vous aurez besoin des outils suivants pour l'application que nous allons construire dans cet article :

* **PHP** : version 8.2 ou supérieure (exécutez `php -v` pour vérifier la version)
* **Composer** (exécutez `composer` pour vérifier qu'il existe)
* **Node.js** : version 20 ou supérieure (exécutez `node -v` pour vérifier la version)
* **MySQL** : version 5.7 ou supérieure (exécutez `mysql --version` pour vérifier s'il existe, ou suivez la [documentation](https://dev.mysql.com/doc/refman/5.7/en/linux-installation.html) pour l'installer)

## Étapes générales

Les principales étapes de cet article seront :

* Installation de Laravel 11.
* Ajout d'un flux d'authentification (échafaudage d'authentification). Laravel fournit un point de départ de base pour cela en utilisant Bootstrap avec React / Vue.
* Installation de Reverb.
* Composants React.js et écoute d'événements dans le frontend.

## Comment installer Laravel

Pour commencer, installez Laravel 11 en utilisant la commande composer :

```shell
composer create-project laravel/laravel:^11.0 laravel-reverb-react-chat && cd laravel-reverb-react-chat/
```

À ce stade, vous pouvez vérifier l'application en exécutant la commande `serve` :

```shell
php artisan serve
```

## Comment créer le modèle et la migration

Vous pouvez générer un modèle et une migration pour les messages en utilisant cette seule commande :

```shell
php artisan make:model -m Message
```

Ensuite, vous devrez configurer le modèle Message avec le code suivant :

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Message extends Model
{
    use HasFactory;

    public $table = 'messages';
    protected $fillable = ['id', 'user_id', 'text'];

    public function user(): BelongsTo {
        return $this->belongsTo(User::class, 'user_id');
    }

    public function getTimeAttribute(): string {
        return date(
            "d M Y, H:i:s",
            strtotime($this->attributes['created_at'])
        );
    }
}
```

Comme vous pouvez le voir, il y a un accessor `getTimeAttribute()` qui formatera l'horodatage de création du message en un format de date et d'heure lisible par l'homme. Il l'affichera en haut de chaque message dans la boîte de chat.

Ensuite, configurez la migration pour la table de base de données `messages` avec ce code :

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void {
        Schema::create('messages', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained();
            $table->text('text')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void {
        Schema::dropIfExists('messages');
    }
};
```

Cette migration crée une table `messages` dans la base de données. La table contient des colonnes pour une clé primaire auto-incrémentée (`id`), une clé étrangère (`user_id`) référençant la colonne `id` de la table `users`, une colonne `text` pour stocker le contenu du message, et `timestamps` pour suivre automatiquement les heures de création et de modification de chaque enregistrement. 

La migration inclut également une méthode de retour en arrière (`down()`) pour supprimer la table `messages` si nécessaire.

Dans cet article, nous utiliserons la base de données MySQL, mais vous pouvez opter pour SQLite comme base de données par défaut si vous préférez. Assurez-vous simplement de configurer correctement vos identifiants de base de données dans le fichier `.env` :

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=database_name
DB_USERNAME=username
DB_PASSWORD=password
```

Après avoir configuré les variables d'environnement, optimisez le cache :

```shell
php artisan optimize
```

Exécutez les migrations pour recréer les tables de la base de données ainsi que pour ajouter la table `messages` :

```shell
php artisan migrate:fresh
```

## Comment ajouter l'authentification

Maintenant, vous pouvez ajouter l'échafaudage d'authentification à votre application. Vous pouvez utiliser le package UI de Laravel pour importer certains fichiers d'actifs. Tout d'abord, vous devrez installer le package approprié :

```shell
composer require laravel/ui
```

Ensuite, importez les actifs liés à React dans l'application :

```shell
php artisan ui react --auth
```

Il peut demander à écraser le fichier `app/Http/Controllers/Controller.php`, et vous pouvez continuer et l'autoriser :

```shell
The [Controller.php] file already exists. Do you want to replace it? (yes/no) [no]
```

Cela effectuera tout l'échafaudage d'authentification compilé et installé, y compris les routes, les contrôleurs, les vues, les configurations vite, et un simple exemple spécifique à React.  
À ce stade, vous n'êtes plus qu'à une étape de ce que l'application soit prête à fonctionner.

**NOTE :** Assurez-vous d'avoir **Node.js** (avec **npm**) version 20 ou supérieure installée. Vous pouvez vérifier cela en exécutant la commande `node -v`. Sinon, installez-le simplement en utilisant la [page officielle](https://nodejs.org/en/download).

```shell
npm install && npm run build
```

La commande ci-dessus installera les packages NPM et construira les actifs frontend. Maintenant, vous pouvez démarrer l'application Laravel et vérifier votre exemple d'application entièrement prêt :

```shell
php artisan optimize && php artisan serve
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/article-image-1.png)
_Capture d'écran de la page d'inscription_

Il est également important de noter que vous pouvez exécuter séparément la commande `dev` au lieu d'utiliser `build` à chaque fois que vous apportez des modifications aux fichiers frontend :

```shell
npm run dev
```

Voir les détails dans le fichier `package.json`, dans le champ `scripts`.

## Comment configurer les routes

Dans cette application de chat en temps réel, vous devrez avoir quelques routes :

* `home` pour la page d'accueil (devrait déjà être ajoutée)
* `message` pour ajouter un nouveau message
* `messages` pour obtenir tous les messages existants

Vous aurez ces types de routes dans le fichier `web.php` :

```php
<?php

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;

Route::get('/', function () { return view('welcome'); });

Auth::routes();

Route::get('/home', [HomeController::class, 'index'])
    ->name('home');
Route::get('/messages', [HomeController::class, 'messages'])
    ->name('messages');
Route::post('/message', [HomeController::class, 'message'])
    ->name('message');

```

Après avoir configuré ces routes, utilisons les avantages des événements Laravel et des travaux de file d'attente.

## Comment configurer un événement Laravel

Vous devez créer un événement `GotMessage` pour écouter un événement spécifique :

```shell
php artisan make:event GotMessage
```

> Les événements de Laravel fournissent une implémentation simple du modèle d'observateur, vous permettant de vous abonner et d'écouter divers événements qui se produisent dans votre application. Les classes d'événements sont généralement stockées dans le répertoire `app/Events`. ([Docs](https://laravel.com/docs/11.x/events))

Configurez un canal WebSocket privé dans la méthode `broadcastOn` pour que tous les utilisateurs authentifiés reçoivent des messages en temps réel. Dans ce cas, nous l'appellerons `"channel_for_everyone"`, mais vous pouvez également le rendre dynamique, en fonction de l'utilisateur, comme `"App.Models.User.{$this->message['user_id']}"`.

```php
<?php

namespace App\Events;

use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class GotMessage implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public function __construct(public array $message) {
        //
    }

    public function broadcastOn(): array {
        // $this->message est disponible ici
        return [
            new PrivateChannel("channel_for_everyone"),
        ];
    }
}
```

Comme vous pouvez le voir, il y a une propriété publique `$massage` en tant qu'argument du constructeur, afin que vous puissiez obtenir les informations du message dans le frontend.

Nous avons déjà utilisé le nom du canal dans le fichier des canaux, et nous l'utiliserons également dans le frontend pour les mises à jour des messages en temps réel.

N'oubliez pas d'implémenter l'interface `ShouldBroadcast` dans la classe de l'événement.

## Comment configurer un travail de file d'attente Laravel

Maintenant, il est temps de créer le travail `SendMessage` pour envoyer des messages :

```shell
php artisan make:job SendMessage
```

> Laravel vous permet de créer facilement des travaux en file d'attente qui peuvent être traités en arrière-plan. En déplaçant les tâches intensives en temps vers une file d'attente, votre application peut répondre aux requêtes web avec une vitesse fulgurante et offrir une meilleure expérience utilisateur à vos clients. ([Docs](https://laravel.com/docs/11.x/queues))

```php
<?php

namespace App\Jobs;

use App\Events\GotMessage;
use App\Models\Message;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

class SendMessage implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function __construct(public Message $message) {
        //
    }

    public function handle(): void {
        GotMessage::dispatch([
            'id' => $this->message->id,
            'user_id' => $this->message->user_id,
            'text' => $this->message->text,
            'time' => $this->message->time,
        ]);
    }
}
```

Le travail de file d'attente `SendMessage.php` est responsable de l'envoi de l'événement `GotMessage` avec des informations sur un message nouvellement envoyé. Il reçoit un objet `Message` lors de sa construction, représentant le message à envoyer. 

Dans sa méthode `handle()`, il envoie l'événement `GotMessage` avec des détails tels que l'ID du message, l'ID de l'utilisateur, le texte et l'horodatage. Ce travail est conçu pour être mis en file d'attente pour un traitement asynchrone, permettant une gestion efficace des tâches d'envoi de messages en arrière-plan.

Comme vous pouvez le voir, il y a une propriété publique `$massage` en tant qu'argument du constructeur, que nous utiliserons pour attacher les informations d'un message au travail de la file d'attente.

## Comment écrire les méthodes du contrôleur

Pour les routes définies, voici les méthodes appropriées du contrôleur :

```php
<?php

namespace App\Http\Controllers;

use App\Jobs\SendMessage;
use App\Models\Message;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function __construct() {
        $this->middleware('auth');
    }

    public function index() {
        $user = User::where('id', auth()->id())->select([
            'id', 'name', 'email',
        ])->first();

        return view('home', [
            'user' => $user,
        ]);
    }

    public function messages(): JsonResponse {
        $messages = Message::with('user')->get()->append('time');

        return response()->json($messages);
    }

    public function message(Request $request): JsonResponse {
        $message = Message::create([
            'user_id' => auth()->id(),
            'text' => $request->get('text'),
        ]);
        SendMessage::dispatch($message);

        return response()->json([
            'success' => true,
            'message' => "Message créé et travail envoyé.",
        ]);
    }
}
```

* Dans la méthode `home`, nous obtiendrons les données de l'utilisateur connecté à partir de la base de données en utilisant le modèle `User` et les enverrons à la vue blade.
* Dans la méthode `messages`, nous récupérerons tous les messages de la base de données en utilisant le modèle `Message`, attacherons les données de la relation `user`, ajouterons le champ `time` (accessor) à chaque élément, et enverrons tout cela à la vue.
* Dans la méthode `message`, un nouveau message sera créé dans la table de la base de données en utilisant le modèle `Message`, et le travail de file d'attente `SendMessage` sera envoyé.

## Comment installer Laravel Reverb

Nous en arrivons maintenant au moment le plus important : il est temps d'installer [Reverb](https://laravel.com/docs/11.x/reverb#installation) dans votre application Laravel.

C'est si facile. Tout le packaging et la configuration nécessaires peuvent être faits en utilisant cette seule commande :

```shell
php artisan install:broadcasting
```

Il vous demandera d'installer Laravel Reverb ainsi que d'installer et de construire les dépendances Node requises pour la diffusion. Appuyez simplement sur Entrée pour continuer.

Après l'exécution de la commande, assurez-vous d'avoir automatiquement ajouté les variables d'environnement spécifiques à reverb au fichier `.env`, comme :

```env
BROADCAST_CONNECTION=reverb

###

REVERB_APP_ID=795051
REVERB_APP_KEY=s3w3thzezulgp5g0e5bs
REVERB_APP_SECRET=gncsnk3rzpvczdakl6pz
REVERB_HOST="localhost"
REVERB_PORT=8080
REVERB_SCHEME=http

VITE_REVERB_APP_KEY="${REVERB_APP_KEY}"
VITE_REVERB_HOST="${REVERB_HOST}"
VITE_REVERB_PORT="${REVERB_PORT}"
VITE_REVERB_SCHEME="${REVERB_SCHEME}"
```

Vous aurez également deux nouveaux fichiers de configuration dans le répertoire `config` :

* `reverb.php`
* `broadcasting.php`

## Comment configurer les canaux WebSocket

Enfin, vous devrez ajouter un canal dans le fichier `channels.php`. Il devrait déjà être créé après l'installation de Reverb.

```php
<?php

use Illuminate\Support\Facades\Broadcast;

Broadcast::channel('channel_for_everyone', function ($user) {
    return true;
});

```

Vous n'aurez qu'un seul canal. Vous pouvez changer le nom du canal et le rendre dynamique – c'est à vous de décider. Dans la fermeture du canal, nous retournerons toujours vrai, mais vous pourrez le modifier plus tard pour ajouter certaines restrictions concernant l'abonnement au canal.

Optimisez les caches une fois de plus :

```shell
php artisan optimize
```

## Comment personnaliser les vues Laravel

Maintenant, votre backend devrait être prêt à ce stade, vous pouvez donc passer au frontend.

Avant de travailler sur les éléments React, vous voudrez configurer les vues Laravel `*.blade.php`. Dans la vue blade `home`, assurez-vous d'avoir la div racine avec un ID de `main` pour rendre tous les composants React là.

```php
@extends('layouts.app')

@section('content')
    <div class="container">
        <div id="main" data-user="{{ json_encode($user) }}"></div>
    </div>
@endsection
```

La div avec l'ID `main` obtient une propriété de données pour contenir les informations `$user` envoyées depuis la méthode `home` du contrôleur.

Je ne mettrai pas tout le contenu de `resources/views/welcome.blade.php` ici, mais vous pouvez simplement apporter les petites modifications suivantes :

* Remplacez `url('/dashboard')` par `url('/home')`;
* Remplacez `Dashboard` par `Home`;
* Supprimez les sections `main` et `footer`.

## Travaillons sur le Front End

Dans Reverb, la diffusion d'événements est effectuée par un pilote de diffusion côté serveur qui diffuse vos événements Laravel afin que le frontend puisse les recevoir dans le client navigateur. 

Dans le frontend, [Laravel Echo](https://github.com/laravel/echo) fait ce travail en coulisses. Echo est une bibliothèque JavaScript qui facilite l'abonnement aux canaux et l'écoute des événements diffusés par votre pilote de diffusion côté serveur.

Vous pouvez trouver la configuration WebSocket configurée avec Echo dans le fichier `resources/js/echo.js`, mais vous n'avez rien à faire là pour ce projet.

Créons quelques composants React afin d'avoir un projet refactorisé et plus lisible.

Créez un composant `Main.jsx` dans le nouveau dossier `components` :

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import '../../css/app.css';
import ChatBox from "./ChatBox.jsx";

if (document.getElementById('main')) {
    const rootUrl = "http://127.0.0.1:8000";
    
    ReactDOM.createRoot(document.getElementById('main')).render(
        <React.StrictMode>
            <ChatBox rootUrl={rootUrl} />
        </React.StrictMode>
    );
}
```

Ici, nous vérifierons s'il existe un élément avec l'ID `'main'`. S'il existe, il procède au rendu de l'application React.

Comme vous pouvez le voir, il y a un composant `ChatBox`. Nous en apprendrons plus à ce sujet bientôt.

Supprimez le fichier `resources/js/components/Example.jsx`, et importez le composant `Main.jsx` dans `app.js` :

```javascript
import './bootstrap';
import './components/Main.jsx';
```

Créez les fichiers `Message.jsx` et `MessageInput.jsx` afin de pouvoir les utiliser dans le composant `ChatBox`.

Le composant `Message` recevra les arguments (champs) `userId` et `message` pour afficher chaque message dans la boîte de chat.

```javascript
import React from "react";

const Message = ({ userId, message }) => {
    return (
        <div className={`row ${
        userId === message.user_id ? "justify-content-end" : ""
        }`}>
            <div className="col-md-6">
		<small className="text-muted">
                    <strong>{message.user.name} | </strong>
                </small>
                <small className="text-muted float-right">
                    {message.time}
                </small>
                <div className={`alert alert-${
                userId === message.user_id ? "primary" : "secondary"
                }`} role="alert">
                    {message.text}
                </div>
            </div>
        </div>
    );
};

export default Message;

```

Le composant `Message.jsx` rend les messages individuels dans l'interface de chat. Il reçoit les props `userId` et `message`. En fonction de si l'expéditeur du message correspond à l'utilisateur actuel, il aligne le message du côté approprié de l'écran. 

Chaque message inclut le nom de l'expéditeur, l'horodatage et le contenu du message lui-même, stylisé différemment selon que le message est envoyé par l'utilisateur actuel ou un autre utilisateur.

Le composant `MessageInput` s'occupera de la création d'un nouveau message :

```javascript
import React, { useState } from "react";

const MessageInput = ({ rootUrl }) => {
    const [message, setMessage] = useState("");

    const messageRequest = async (text) => {
        try {
            await axios.post(`${rootUrl}/message`, {
                text,
            });
        } catch (err) {
            console.log(err.message);
        }
    };

    const sendMessage = (e) => {
        e.preventDefault();
        if (message.trim() === "") {
            alert("Veuillez entrer un message !");
            return;
        }

        messageRequest(message);
        setMessage("");
    };

    return (
        <div className="input-group">
            <input onChange={(e) => setMessage(e.target.value)}
                   autoComplete="off"
                   type="text"
                   className="form-control"
                   placeholder="Message..."
                   value={message}
            />
            <div className="input-group-append">
                <button onClick={(e) => sendMessage(e)}
                        className="btn btn-primary"
                        type="button">Envoyer</button>
            </div>
        </div>
    );
};

export default MessageInput;
```

Le composant `MessageInput` fournit un champ de formulaire pour que les utilisateurs tapent des messages et les envoient dans l'interface de chat. En cliquant sur le bouton, il déclenche une fonction pour envoyer le message au serveur via une requête POST Axios à l'`rootUrl` spécifié qu'il a obtenu du composant parent `ChatBox`. Il gère également la validation pour s'assurer que les utilisateurs ne peuvent pas envoyer de messages vides. Vous pouvez le personnaliser plus tard si vous le souhaitez. 

Maintenant, créez un composant `ChatBox.jsx` pour avoir le frontend prêt :

```javascript
import React, { useEffect, useRef, useState } from "react";
import Message from "./Message.jsx";
import MessageInput from "./MessageInput.jsx";

const ChatBox = ({ rootUrl }) => {
    const userData = document.getElementById('main')
        .getAttribute('data-user');

    const user = JSON.parse(userData);
    // `App.Models.User.${user.id}`;
    const webSocketChannel = `channel_for_everyone`;

    const [messages, setMessages] = useState([]);
    const scroll = useRef();

    const scrollToBottom = () => {
        scroll.current.scrollIntoView({ behavior: "smooth" });
    };

    const connectWebSocket = () => {
        window.Echo.private(webSocketChannel)
            .listen('GotMessage', async (e) => {
                // e.message
                await getMessages();
            });
    }

    const getMessages = async () => {
        try {
            const m = await axios.get(`${rootUrl}/messages`);
            setMessages(m.data);
            setTimeout(scrollToBottom, 0);
        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        getMessages();
        connectWebSocket();

        return () => {
            window.Echo.leave(webSocketChannel);
        }
    }, []);

    return (
        <div className="row justify-content-center">
            <div className="col-md-8">
                <div className="card">
                    <div className="card-header">Boîte de chat</div>
                    <div className="card-body"
                         style={{height: "500px", overflowY: "auto"}}>
                        {
                            messages?.map((message) => (
                                <Message key={message.id}
                                         userId={user.id}
                                         message={message}
                                />
                            ))
                        }
                        <span ref={scroll}></span>
                    </div>
                    <div className="card-footer">
                        <MessageInput rootUrl={rootUrl} />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ChatBox;
```

Le composant `ChatBox` gère une interface de chat dans l'application. Il récupère et affiche les messages d'un serveur en utilisant WebSocket et des requêtes HTTP.

Le composant rend une liste de messages, un champ de saisie de message, et fait automatiquement défiler vers le bas lorsque de nouveaux messages arrivent.

Il définit un canal WebSocket pour les mises à jour de messages en temps réel. Vous devez configurer ce canal en utilisant le même nom qu'il a été écrit dans `routes/channels.php` et dans le travail de file d'attente `app/Events/GotMessage.php`.

De plus, la fonction `leave()` est appelée dans la fonction de nettoyage `useEffect` pour se désabonner du canal WebSocket lorsque le composant est démonté. Cela prévient les fuites de mémoire et les connexions réseau inutiles en empêchant le composant d'écouter les mises à jour sur le canal WebSocket après qu'il ne soit plus nécessaire.

## Exécuter l'application

Maintenant, tout est prêt et il est temps de vérifier l'application. Suivez ces instructions :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/article-image-2.png)
_Capture d'écran du terminal avec toutes les commandes nécessaires_

* Construire les actifs frontend (ce n'est pas une commande "forever" en cours d'exécution) :  
`npm run build`
* Commencer à écouter les événements Laravel :  
`php artisan queue:listen`
* Démarrer le serveur WebSocket :  
`php artisan reverb:start`
* Démarrer le serveur (vous pouvez utiliser une alternative pour votre application comme un serveur en cours d'exécution local) :  
`php artisan serve`

Après que toutes les commandes nécessaires sont en cours d'exécution, vous pouvez vérifier l'application en visitant l'URL par défaut : `http://127.0.0.1:8000`.

Pour les tests, vous pouvez enregistrer deux utilisateurs différents, faire en sorte que ces utilisateurs se connectent, envoyer des messages depuis chacun d'eux, et voir la boîte de chat.

## Ressources utiles sur Reverb

Maintenant que nous avons atteint la fin de cet article, il est utile de lister quelques ressources utiles sur Reverb :

* [Laravel Broadcasting](https://laravel.com/docs/11.x/broadcasting) (documentation officielle)
* [Taylor Otwel - Laravel Update](https://www.youtube.com/watch?v=0g7HqfsCX4Y) (discours à Laracon EU 2024)
* [Joe Dixon sur X](https://twitter.com/_joedixon) (créateur de Reverb)
* [Épisode Laracast](https://laracasts.com/series/lukes-larabits/episodes/17) (exemple pratique avec Reverb)

## Conclusion

Maintenant, vous savez comment créer des applications en temps réel avec Laravel Reverb dans la nouvelle version de Laravel. Avec cela, vous pouvez implémenter des communications WebSocket dans votre application full-stack et éviter d'utiliser des services tiers supplémentaires (comme Pusher et Socket.io).

Si vous voulez avoir une idée claire de comment intégrer React.js dans votre application Laravel sans utiliser d'outils Laravel supplémentaires (comme Inertia), vous pouvez lire mon précédent [article freeCodeCamp](https://www.freecodecamp.org/news/use-react-with-laravel/), où vous pouvez créer une application Tasklist full-stack à page unique.

Le code complet pour cet article est ici sur mon [**GitHub**](https://github.com/boolfalse/laravel-reverb-react-chat)⭐, où je publie activement une grande partie de mon travail sur diverses technologies modernes.

Pour plus d'informations, vous pouvez visiter mon site web : [**boolfalse.com**](https://boolfalse.com/)

N'hésitez pas à partager cet article. 😇