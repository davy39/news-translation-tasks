---
title: Comment créer le backend d'une application de suivi de crypto-monnaie en utilisant
  Swift et Laravel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:28:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-the-backend-of-a-crypto-tracking-app-using-swift-and-laravel-1d9122bc290b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U-_YZ407G1keDN56lNaXtQ.jpeg
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: Laravel
  slug: laravel
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment créer le backend d'une application de suivi de crypto-monnaie en
  utilisant Swift et Laravel
seo_desc: 'By Neo Ighodaro

  Part 1


  _Photo by [Unsplash](https://unsplash.com/photos/aUHr4gcQCCE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">André François McKenzie on <a href="https://unsplash.com/...'
---

Par Neo Ighodaro

#### Partie 1

![Image](https://cdn-media-1.freecodecamp.org/images/qYBbPa7FXKpFgfQUGtLv0UAzONrnqtSdBl-5)
_Photo par [Unsplash](https://unsplash.com/photos/aUHr4gcQCCE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">André François McKenzie</a> sur <a href="https://unsplash.com/search/photos/cryptocurrency?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Vous aurez besoin des éléments suivants installés sur votre machine : Xcode, le CLI Laravel, SQLite et Cocoapods. Une familiarité avec l'IDE Xcode sera utile.

### Introduction

La crypto-monnaie a été et reste l'une des plus grandes tendances de cette année. Avec des monnaies comme Bitcoin atteignant des sommets records et de nouvelles entreprises créant des tokens et des offres, cela montre tout le potentiel que les crypto-monnaies ont. Cependant, les prix des crypto-monnaies sont erratiques et peuvent chuter ou grimper en un instant, il est donc toujours bon de garder un œil sur les changements.

Dans cet article, nous allons construire une application qui suit les changements du marché des crypto-monnaies. L'application se concentrera sur le BTC et l'ETH et permettra aux utilisateurs de l'application de définir des montants minimum et maximum auxquels ils souhaitent être notifiés du prix actuel de la monnaie. L'application sera construite en utilisant Swift, Laravel, Pusher Channels et Pusher Beams.

### Prérequis

Pour suivre ce tutoriel, vous avez besoin des éléments suivants :

* [Xcode](https://developer.apple.com/xcode) installé sur votre machine.
* Connaissance de l'IDE Xcode.
* Connaissance de base du [Framework Laravel](https://laravel.com/).
* Connaissance de base du [langage de programmation Swift](http://developer.apple.com/swift).
* [CLI Laravel](https://laravel.com/docs/5.6/installation) installé sur votre machine.
* SQLite installé sur votre machine. [Guide d'installation](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm).
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installé sur votre machine.
* Application [Pusher Beams](https://pusher.com/beams) et [Channels](https://pusher.com/channels).

### Ce que nous allons construire

Nous commencerons par construire le backend de l'application en utilisant Laravel. Ensuite, nous construirons l'application iOS en utilisant Swift. Si vous souhaitez tester les notifications push, vous devrez exécuter l'application sur un appareil réel.

### Comment l'application cliente fonctionnera

Pour l'application cliente, l'application iOS, nous créerons une simple liste qui affichera les monnaies disponibles et les prix actuels en dollars. Chaque fois que le prix de la crypto-monnaie change, nous déclencherons un événement en utilisant Pusher Channels afin que les prix soient mis à jour.

À partir de l'application, vous pourrez définir un prix minimum et maximum de changement lorsque vous souhaitez être alerté. Par exemple, vous pouvez configurer l'application pour envoyer une notification push à l'application lorsque le prix d'un Etherium (ETH) passe en dessous de 500 $. Vous pouvez également configurer l'application pour recevoir une notification lorsque le prix du Bitcoin dépasse 5000 $.

### Comment l'application backend fonctionnera

Pour l'application backend, nous utiliserons Laravel et nous créerons des endpoints qui permettent à un utilisateur de mettre à jour les paramètres et de charger les paramètres pour un appareil. L'API sera responsable de la vérification des prix actuels de la crypto-monnaie et de l'envoi d'une mise à jour Channels et d'une notification Beams lorsque le prix change.

Cependant, parce que les prix ne changent pas de manière très prévisible, nous simulerons les changements de monnaie afin que nous puissions prévisualiser l'application en action. Nous utiliserons également la [planification des tâches](https://laravel.com/docs/5.6/scheduling) dans Laravel pour déclencher les vérifications des prix actuels des monnaies.

Dans un environnement de production, nous définirons le planificateur comme un cronjob, mais parce que nous sommes en développement, nous exécuterons manuellement la commande pour déclencher les changements de prix.

### À quoi ressemblera l'application

Lorsque nous aurons terminé l'application, voici à quoi elle ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/mRQw2yNxaOb3PXYPtqYV7qHp5J5BqIWdal9C)

Commençons.

### Configuration de Pusher Beams et Channels

#### Configuration de Pusher Channels

Connectez-vous à votre [tableau de bord Pusher](https://dashboard.pusher.com). Si vous n'avez pas de compte, créez-en un. Votre tableau de bord devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/RS-2j91z505-2KRm2sSUYa46oVM1jh9WYR0v)

Créez une nouvelle application Channels. Vous pouvez facilement le faire en cliquant sur la grande carte **Créer une nouvelle application Channels** en bas à droite. Lorsque vous créez une nouvelle application, des clés vous sont fournies. Conservez-les en sécurité car vous en aurez bientôt besoin.

#### Configuration de Pusher Beams

Ensuite, connectez-vous au nouveau [tableau de bord Pusher](https://dash.pusher.com/), ici nous créerons une instance Pusher Beams. Vous devriez vous inscrire si vous n'avez pas encore de compte. Cliquez sur le bouton **Beams** dans la barre latérale, puis cliquez sur **Créer**, cela lancera une fenêtre contextuelle pour **Créer une nouvelle instance Beams**. Nommez-la `cryptoalat`.

![Image](https://cdn-media-1.freecodecamp.org/images/yOT20aNZkSLD15v7dv6szLwe0yAcU-dBQj1b)

Dès que vous créez l'instance, un guide de démarrage rapide vous sera présenté. Sélectionnez le **démarrage rapide IOS** et suivez l'assistant.

![Image](https://cdn-media-1.freecodecamp.org/images/F21GIadi91kKhGTlWN8O6KMCQJ-bTt5bjjqo)

Lorsque vous avez terminé de créer l'application Beams, un identifiant d'instance et une clé secrète vous seront fournis, nous en aurons besoin plus tard.

### Configuration de votre application backend

Dans votre terminal, exécutez la commande suivante pour créer un nouveau projet Laravel :

```bash
$ laravel new cryptoapi
```

Cette commande créera un nouveau projet Laravel et installera toutes les dépendances Laravel requises.

Ensuite, installons certaines des dépendances spécifiques au projet. Ouvrez le fichier `composer.json` et dans la propriété `require`, ajoutez les dépendances suivantes :

```json
// Fichier : composer.json
    "require": {
        [...]
        
        "neo/pusher-beams": "^1.0",
        "pusher/pusher-php-server": "~3.0"
    },
```

Exécutez maintenant la commande suivante pour installer ces dépendances.

```bash
$ composer update
```

Lorsque l'installation est terminée, ouvrez le projet dans un éditeur de texte de votre choix. [Visual Studio Code](https://code.visualstudio.com/) est assez bien.

### Configuration de notre bibliothèque Pusher Beams

La première chose que nous voulons faire est de configurer la [bibliothèque Pusher Beams](https://github.com/neoighodaro/pusher-beams) que nous venons de récupérer en utilisant composer. Pour configurer, ouvrez le fichier `.env` et ajoutez les clés suivantes :

```
PUSHER_BEAMS_SECRET_KEY="PUSHER_BEAMS_SECRET_KEY"
    PUSHER_BEAMS_INSTANCE_ID="PUSHER_BEAMS_INSTANCE_ID"
```

Vous devez remplacer les espaces réservés `PUSHER_BEAMS_*` par les clés que vous avez obtenues lors de la configuration de votre application Beams.

Ensuite, ouvrez le fichier `config/broadcasting.php` et faites défiler jusqu'à ce que vous voyiez la clé `connections`. Vous y trouverez les paramètres `pusher`, ajoutez ce qui suit à la configuration `pusher` :

```php
'pusher' => [
        // [...]
        
        'beams' => [
            'secret_key' => env('PUSHER_BEAMS_SECRET_KEY'),
            'instance_id' => env('PUSHER_BEAMS_INSTANCE_ID'),
        ],
    ],
```

### Configuration de notre bibliothèque Pusher Channels

L'étape suivante consiste à configurer Pusher Channels. Laravel est livré avec un support natif pour Pusher Channels, nous n'avons donc pas besoin de faire grand-chose pour le configurer.

Ouvrez le fichier `.env` et mettez à jour les clés suivantes :

```
BROADCAST_DRIVER=pusher

    // [...]
    
    PUSHER_APP_ID="PUSHER_APP_ID"
    PUSHER_APP_KEY="PUSHER_APP_KEY"
    PUSHER_APP_SECRET="PUSHER_APP_SECRET"
    PUSHER_APP_CLUSTER="PUSHER_APP_CLUSTER"
```

Ci-dessus, vous avez défini le `BROADCAST_DRIVER` sur `pusher`, puis pour les autres clés `PUSHER_APP_*`, remplacez les espaces réservés par les clés obtenues depuis votre tableau de bord Pusher. C'est tout ce que nous devons faire pour configurer Pusher Channels pour cette application.

### Construction de l'application backend

Maintenant que nous avons configuré toutes les dépendances, nous pouvons commencer à construire l'application. Nous commencerons par créer les routes. Cependant, au lieu de créer des contrôleurs pour relier aux routes, nous ajouterons la logique directement aux routes.

#### Configuration de la base de données, de la migration et du modèle

Puisque nous travaillerons avec une base de données, nous devons configurer la base de données avec laquelle nous allons travailler. Pour simplifier les choses, nous utiliserons SQLite. Créez un fichier `database.sqlite` vide dans le répertoire `database`.

Ouvrez le fichier `.env` et remplacez :

```
DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=homestead
    DB_USERNAME=homestead
    DB_PASSWORD=secret
```

Par

```
DB_CONNECTION=sqlite
    DB_DATABASE=/full/path/to/your/database.sqlite
```

Ensuite, créons une migration pour la table `devices`. Nous utiliserons cette table pour stocker les appareils et leurs paramètres de notification. Cela nous aidera à savoir quels appareils envoyer des notifications push.

Exécutez la commande suivante pour créer la migration et le modèle :

```bash
$ php artisan make:model Device -m
```

> _Le drapeau `-m` instruira artisan de créer une migration avec le modèle._

Cette commande générera deux fichiers, le fichier de migration dans `database/migrations` et le modèle dans le répertoire `app`. Modifions d'abord le fichier de migration.

Ouvrez le fichier de migration `*_create_devices_table.php` dans le répertoire `database/migrations` et remplacez le contenu par ce qui suit :

```php
<?php

    use Illuminate\Support\Facades\Schema;
    use Illuminate\Database\Schema\Blueprint;
    use Illuminate\Database\Migrations\Migration;
    
    class CreateDevicesTable extends Migration
    {
        /**
         * Exécuter les migrations.
         *
         * @return void
         */
        public function up()
        {
            Schema::create('devices', function (Blueprint $table) {
                $table->increments('id');
                $table->string('uuid')->unique();
                $table->float('btc_min_notify')->default(0);
                $table->float('btc_max_notify')->default(0);
                $table->float('eth_min_notify')->default(0);
                $table->float('eth_max_notify')->default(0);
            });
        }
        
        /**
         * Annuler les migrations.
         *
         * @return void
         */
        public function down()
        {
            Schema::dropIfExists('devices');
        }
    }
```

Dans la méthode `up`, nous avons défini la structure de la table `devices`. Nous avons le champ `uuid` qui sera une chaîne unique pour chaque appareil enregistré. Nous avons deux champs `btc_notify` qui sont là pour sauvegarder les prix minimum et maximum du BTC auxquels l'appareil doit être notifié. Même chose pour les champs `eth_*_notify`.

Pour exécuter la migration, exécutez la commande suivante :

```bash
$ php artisan migrate
```

Ouvrez le modèle `app/Device.php` et remplacez le contenu par le code ci-dessous :

```php
<?php
    namespace App;
    
    use Illuminate\Database\Eloquent\Model;
    use Illuminate\Notifications\Notifiable;
    
    class Device extends Model
    {
        use Notifiable;
        
        public $timestamps = false;
        
        protected $fillable = [
            'uuid', 
            'btc_min_notify', 
            'btc_max_notify', 
            'eth_min_notify', 
            'eth_max_notify',
        ];
        
        protected $cast = [
            'btc_min_notify' => 'float',
            'btc_max_notify' => 'float',
            'eth_min_notify' => 'float',
            'eth_max_notify' => 'float'
        ];
        
        public function scopeAffected($query, string $currency, $currentPrice)
        {
            return $query->where(function ($q) use ($currency, $currentPrice) {
                $q->where("${currency}_min_notify", '>', 0)
                  ->where("${currency}_min_notify", '>', $currentPrice);
            })->orWhere(function ($q) use ($currency, $currentPrice) {
                $q->where("${currency}_max_notify", '>', 0)
                  ->where("${currency}_max_notify", '<', $currentPrice);
            });
        }
    }
```

Dans le modèle ci-dessus, nous avons défini la propriété `$timestamps` sur `false` pour nous assurer qu'Eloquent n'essaie pas de mettre à jour les champs `created_at` et `updated_at`, ce qui est le comportement normal.

Nous avons également la méthode `scopeAffected` qui est un exemple de [portée Eloquent](https://laravel.com/docs/5.6/eloquent#local-scopes). Nous l'utilisons pour obtenir les appareils affectés après qu'un changement de prix s'est produit sur une monnaie. Ainsi, si, par exemple, le prix du BTC baisse, cette méthode vérifie les appareils et les paramètres pour voir les appareils qui doivent être notifiés de ce changement.

> _Les portées locales vous permettent de définir des ensembles communs de contraintes que vous pouvez facilement réutiliser dans toute votre application. Par exemple, vous pouvez avoir besoin de récupérer fréquemment tous les utilisateurs considérés comme « populaires ». Pour définir une portée, préfixez une méthode de modèle Eloquent avec `scope`. - [Documentation Laravel](https://laravel.com/docs/5.6/eloquent#local-scopes)._

Nous utiliserons cette portée plus tard dans notre application lorsque nous devrons savoir quels appareils envoyer des notifications push.

#### Création des routes

Ouvrez le fichier `routes/api.php` et remplacez le contenu du fichier par le code suivant :

```php
// Fichier : routes/api.php
    <?php
    use App\Device;
    use Illuminate\Http\Request;
```

Ensuite, ajoutons la première route. Ajoutez le code suivant au fichier des routes :

```php
// Fichier : routes/api.php
    Route::get('/settings', function (Request $request) {
        return Device::whereUuid($request->query('u'))->firstOrFail()['settings'];
    });
```

Dans la route ci-dessus, nous retournons les paramètres pour l'appareil fourni dans le paramètre de requête `u`. Cela signifie que si un appareil enregistré atteint le point de terminaison `/settings` et passe l'UUID de l'appareil par le paramètre `u`, les paramètres de cet appareil seront retournés.

Ensuite, dans le même fichier de routes, collez ce qui suit en bas du fichier :

```php
Route::post('/settings', function (Request $request) {
        $settings = $request->validate([
            'btc_min_notify' => 'int|min:0',
            'btc_max_notify' => 'int|min:0',
            'eth_min_notify' => 'int|min:0',
            'eth_max_notify' => 'int|min:0',
        ]);
        
        $settings = array_filter($settings, function ($value) { return $value > 0; });
        
        $device = Device::firstOrNew(['uuid' => $request->query('u')]);
        $device->fill($settings);
        $saved = $device->save();
        
        return response()->json([
            'status' => $saved ? 'success' : 'failure'
        ], $saved ? 200 : 400);
    });
```

Ci-dessus, nous avons défini la route pour la route `POST /settings`. Cette route enregistre les paramètres dans la base de données. Elle créera une nouvelle entrée si le paramètre n'existe pas déjà ou mettra à jour l'existant s'il existe.

C'est tout pour les routes.

#### Création des jobs, événements et notificateurs

Ensuite, nous devons créer le [job Laravel](https://laravel.com/docs/5.6/queues#creating-jobs) qui s'exécutera à intervalles pour vérifier s'il y a un changement dans le prix de la monnaie.

Exécutez la commande suivante pour créer un nouveau job Laravel :

```bash
$ php artisan make:job CheckPrices
```

Cela créera une nouvelle classe `CheckPrices` dans le répertoire `app`. Ouvrez cette classe et remplacez le contenu par ce qui suit :

```php
<?php

    namespace App\Jobs;
    
    use App\Device;
    use Illuminate\Bus\Queueable;
    use Illuminate\Queue\SerializesModels;
    use Illuminate\Queue\InteractsWithQueue;
    use Illuminate\Contracts\Queue\ShouldQueue;
    use Illuminate\Foundation\Bus\Dispatchable;
    use App\Events\CurrencyUpdated;
    use App\Notifications\CoinPriceChanged;
    
    class CheckPrices implements ShouldQueue
    {
        use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;
        
        protected $supportedCurrencies = ['ETH', 'BTC'];
        
        /**
         * Exécuter le job.
         *
         * @return void
         */
        public function handle()
        {
            $payload = $this->getPricesForSupportedCurrencies();
            
            if (!empty($payload)) {
                $this->triggerPusherUpdate($payload);
                $this->triggerPossiblePushNotification($payload);
            }
        }
        
        private function triggerPusherUpdate($payload)
        {
            event(new CurrencyUpdated($payload));
        }
        
        private function triggerPossiblePushNotification($payload)
        {
            foreach ($this->supportedCurrencies as $currency) {
                $currentPrice = $payload[$currency]['current'];
                
                $currency = strtolower($currency);
                
                foreach (Device::affected($currency, $currentPrice)->get() as $device) {
                    $device->notify(new CoinPriceChanged($currency, $device, $payload));
                }
            }
        }
        
        public function getPricesForSupportedCurrencies(): array
        {
            $payload = [];
            
            foreach ($this->supportedCurrencies as $currency) {
                if (config('app.debug') === true) {
                    $response = [
                        $currency => [
                            'USD' => (float) rand(100, 15000)
                        ]
                    ];
                } else {
                    $url = "https://min-api.cryptocompare.com/data/pricehistorical?fsym={$currency}&tsyms=USD&ts={$timestamp}";
                    
                    $response = json_decode(file_get_contents($url), true);
                }
                
                if (json_last_error() === JSON_ERROR_NONE) {
                    $currentPrice = $response[$currency]['USD'];
                    
                    $previousPrice = cache()->get("PRICE_${currency}", false);
                    
                    if ($previousPrice == false or $previousPrice !== $currentPrice) {
                        $payload[$currency] = [
                            'current' => $currentPrice,
                            'previous' => $previousPrice,
                        ];
                    }
                    
                    cache()->put("PRICE_${currency}", $currentPrice, (24 * 60 * 60));
                }
            }
            
            return $payload;
        }
    }
```

Dans la classe ci-dessus, nous implémentons l'interface `ShouldQueue`. Cela fait en sorte que le job peut et sera mis en file d'attente. Dans un serveur de production, la mise en file d'attente des jobs rend votre application plus rapide car elle met en file d'attente les jobs qui peuvent prendre un certain temps à s'exécuter pour une exécution ultérieure.

Nous avons quatre méthodes dans cette classe. La première est la méthode `handle`. Celle-ci est appelée automatiquement lorsque le job est exécuté. Dans cette méthode, nous récupérons les prix des monnaies disponibles et vérifions si le prix a changé. Si c'est le cas, nous publions un événement Pusher Channel puis vérifions s'il y a des appareils qui doivent être notifiés en fonction des paramètres de l'utilisateur. Si c'est le cas, nous envoyons une notification push à cet appareil.

Nous avons la méthode `triggerPusherUpdate` qui déclenche un événement `CurrencyUpdated`. Nous créerons cet événement dans la section suivante. Nous avons également une méthode `triggerPossiblePushNotification` qui obtient la liste des appareils qui doivent être notifiés du changement de monnaie puis notifie l'utilisateur en utilisant la classe `CoinPriceChanged`, que nous créerons dans la section suivante.

Enfin, nous avons la méthode `getPricesForSupportedCurrencies` qui récupère simplement le prix actuel d'une monnaie. Dans cette méthode, nous avons un mode de débogage qui simule le prix actuel d'une monnaie.

Pour vous assurer que cette classe que nous venons de créer est planifiée correctement, ouvrez le fichier `app/Console/Kernel.php` et dans la méthode `schedule`, ajoutez le code suivant à la méthode `schedule` :

```php
$schedule->job(new \App\Jobs\CheckPrices)->everyMinute();
```

Maintenant, chaque fois que nous exécutons la commande `php artisan schedule:run`, tous les jobs dans cette méthode `schedule` seront exécutés. Normalement, dans un environnement de production, nous devons ajouter la commande de planification comme un cronjob, cependant, nous exécuterons cette commande manuellement.

La prochaine chose à faire sera de créer les notificateurs et les événements. Dans votre terminal, exécutez les commandes suivantes :

```bash
$ php artisan make:event CurrencyUpdated    $ php artisan make:notification CoinPriceChanged
```

Cela créera une classe dans les répertoires `Events` et `Notifications`.

Dans la classe d'[événement](https://laravel.com/docs/5.6/events), `CurrencyUpdated`, collez le code suivant :

```
<?php

    namespace App\Events;
    
    use Illuminate\Broadcasting\Channel;
    use Illuminate\Queue\SerializesModels;
    use Illuminate\Foundation\Events\Dispatchable;
    use Illuminate\Broadcasting\InteractsWithSockets;
    use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
    
    class CurrencyUpdated implements ShouldBroadcast
    {
        use Dispatchable, InteractsWithSockets, SerializesModels;
        
        public $payload;
        
        public function __construct($payload)
        {
            $this->payload = $payload;
        }
        
        public function broadcastOn()
        {
            return new Channel('currency-update');
        }
        
        public function broadcastAs()
        {
            return 'currency.updated';
        }
    }
```

Dans la classe d'événement ci-dessus, nous avons la méthode `broadcastOn` qui spécifie le canal Pusher sur lequel nous voulons diffuser un événement. Nous avons également la méthode `broadcastAs` qui spécifie le nom de l'événement que nous voulons diffuser sur le canal.

Dans la classe de [notification](https://laravel.com/docs/5.6/notifications) `CoinPriceChanged`, remplacez le contenu par le code suivant :

```php
<?php

    namespace App\Notifications;
    
    use App\Device;
    use Illuminate\Bus\Queueable;
    use Neo\PusherBeams\PusherBeams;
    use Neo\PusherBeams\PusherMessage;
    use Illuminate\Notifications\Notification;
    
    class CoinPriceChanged extends Notification
    {
        use Queueable;
        
        private $currency;
        private $device;
        private $payload;
        
        public function __construct(string $currency, Device $device, array $payload)
        {
            $this->currency = $currency;
            $this->device = $device;
            $this->payload = $payload;
        }
        
        public function via($notifiable)
        {
            return [PusherBeams::class];
        }
        
        public function toPushNotification($notifiable)
        {
            $currentPrice = $this->payload[strtoupper($this->currency)]['current'];
            
            $previousPrice = $this->payload[strtoupper($this->currency)]['current'];
            
            $direction = $currentPrice > $previousPrice ? 'climbed' : 'dropped';
            
            $currentPriceFormatted = number_format($currentPrice);
            
            return PusherMessage::create()
                    ->iOS()
                    ->sound('success')
                    ->title("Price of {$this->currency} has {$direction}")
                    ->body("The price of {$this->currency} has {$direction} and is now \${$currentPriceFormatted}");
        }
        
        public function pushNotificationInterest()
        {
            $uuid = strtolower(str_replace('-', '_', $this->device->uuid));
            
            return "{$uuid}_{$this->currency}_changed";
        }
    }
```

Dans la classe ci-dessus, nous avons la classe `toPushNotification` qui prépare la notification push en utilisant la bibliothèque Pusher Beams. Nous avons également la méthode `pushNotificationInterest` qui définit le nom de l'intérêt de la notification push en fonction de la monnaie et de l'ID de l'appareil.

C'est tout pour le backend, maintenant exécutez simplement la commande suivante pour démarrer le serveur :

```
$ php artisan serve
```

Cela démarrera un serveur PHP avec notre application en cours d'exécution. De plus, si vous devez déclencher manuellement un changement de monnaie, exécutez la commande suivante :

```bash
$ php artisan schedule:run
```

Maintenant que nous avons terminé avec le backend, nous pouvons créer l'application en utilisant Swift et Xcode.

### Conclusion

Dans cette partie de l'article, nous avons créé le backend de notre application d'alerte de crypto-monnaie. [Dans la partie suivante](https://pusher.com/tutorials/cryptocurrency-tracking-swift-laravel-part-2), nous verrons comment nous pouvons créer l'application qui consommera l'API que nous venons de créer dans cette partie.

Le code source de cette application est disponible sur [GitHub](https://github.com/neoighodaro/cryptocurrency-alert-ios-app).

Cet article a été publié pour la première fois sur [pusher.](https://pusher.com/tutorials/cryptocurrency-tracking-swift-laravel-part-1)