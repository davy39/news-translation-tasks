---
title: How to create the backend of a crypto tracking app using Swift and Laravel
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
seo_title: null
seo_desc: 'By Neo Ighodaro

  Part 1


  _Photo by [Unsplash](https://unsplash.com/photos/aUHr4gcQCCE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">André François McKenzie on <a href="https://unsplash.com/...'
---

By Neo Ighodaro

#### Part 1

![Image](https://cdn-media-1.freecodecamp.org/images/qYBbPa7FXKpFgfQUGtLv0UAzONrnqtSdBl-5)
_Photo by [Unsplash](https://unsplash.com/photos/aUHr4gcQCCE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">André François McKenzie</a> on <a href="https://unsplash.com/search/photos/cryptocurrency?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> You will need the following installed on your machine: Xcode, the Laravel CLI, SQLite and Cocoapods. Familiarity with the Xcode IDE will be helpful.

### Introduction

Cryptocurrency has been and is still one of the biggest trends this year. With currencies like Bitcoin reaching record highs and new companies creating tokens and offerings, it’s showing just how much potential cryptocurrencies have. However, cryptocurrency prices are erratic and can fall or climb at a moment’s notice, so it’s always a good idea to keep tabs on the changes.

In this article, we will be building an application that keeps tabs on changes to the crypto market. The application will focus on BTC and ETH and will allow users of the application to set minimum and maximum amounts when they would like to be notified about the coin’s current price. The application will be built using Swift, Laravel, Pusher Channels, and Pusher Beams.

### Prerequisites

To follow along you need the following requirements:

* [Xcode](https://developer.apple.com/xcode) installed on your machine.
* Knowledge of the Xcode IDE.
* Basic knowledge using the [Laravel framework](https://laravel.com/).
* Basic knowledge of the [Swift programming language](http://developer.apple.com/swift).
* [Laravel CLI](https://laravel.com/docs/5.6/installation) installed on your machine.
* SQLite installed on your machine. [Installation guide](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm).
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installed on your machine.
* [Pusher Beams](https://pusher.com/beams) and [Channels](https://pusher.com/channels) application.

### What we will be building

We will start out by building the backend of the application using Laravel. Then we will build the iOS application using Swift. If you want to test the push notifications then you will need to run the application on a live device.

### How the client application will work

For the client app, the iOS application, we will create a simple list that will display the available currencies and the current prices to the dollar. Whenever the price of the cryptocurrency changes, we will trigger an event using Pusher Channels so the prices are updated.

From the application, you will be able to set a minimum and maximum price change when you want to be alerted. For instance, you can configure the application to send a push notification to the application when the price of one Etherium (ETH) goes below $500. You can also configure the application to receive a notification when the price of Bitcoin goes above $5000.

### How the backend application will work

For the backend application, we will be using Laravel and we will create endpoints that allow a user update the settings and load the settings for a device. The API will be responsible for checking the current prices of the cryptocurrency and sending both a Channels update and a Beams notification when the price changes.

However, because the prices don’t change very predictably, we will be simulating the currency changes so we can preview the application in action. We will also be using [task scheduling](https://laravel.com/docs/5.6/scheduling) in Laravel to trigger the checks for the current currency prices.

In a production environment we will set the scheduler as a cronjob, but because we are in development, we will manually run the command to trigger price changes.

### How the application will look

When we are done with the application, here’s how the application will look:

![Image](https://cdn-media-1.freecodecamp.org/images/mRQw2yNxaOb3PXYPtqYV7qHp5J5BqIWdal9C)

Let’s get started.

### Setting up Pusher Beams and Channels

#### Setting up Pusher Channels

Log in to your [Pusher dashboard](https://dashboard.pusher.com). If you don’t have an account, create one. Your dashboard should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/RS-2j91z505-2KRm2sSUYa46oVM1jh9WYR0v)

Create a new Channels app. You can easily do this by clicking the big **Create new Channels app** card at the bottom right. When you create a new app, you are provided with keys. Keep them safe as you will soon need them.

#### Setting up Pusher Beams

Next, log in to the new [Pusher dashboard](https://dash.pusher.com/), in here we will create a Pusher Beams instance. You should sign up if you don’t have an account yet. Click on the **Beams** button on the sidebar then click **Create**, this will launch a pop up to **Create a new Beams instance**. Name it `cryptoalat`.

![Image](https://cdn-media-1.freecodecamp.org/images/yOT20aNZkSLD15v7dv6szLwe0yAcU-dBQj1b)

As soon as you create the instance, you will be presented with a quickstart guide. Select the **IOS** quickstart and follow through the wizard.

![Image](https://cdn-media-1.freecodecamp.org/images/F21GIadi91kKhGTlWN8O6KMCQJ-bTt5bjjqo)

When you are done creating the Beams application, you will be provided with an instance ID and a secret key, we will need these later.

### Setting up your backend application

In your terminal, run the command below to create a new Laravel project:

```bash
$ laravel new cryptoapi
```

This command will create a new Laravel project and install all the required Laravel dependencies.

Next, let’s install some of the project specific dependencies. Open the `composer.json` file and in the `require` property, add the following dependencies:

```json
// File: composer.json
    "require": {
        [...]
        
        "neo/pusher-beams": "^1.0",
        "pusher/pusher-php-server": "~3.0"
    },
```

Now run the command below to install these dependencies.

```bash
$ composer update
```

When the installation is complete, open the project in a text editor of your choice. [Visual Studio Code](https://code.visualstudio.com/) is pretty nice.

### Setting up our Pusher Beams library

The first thing we want to do is set up the [Pusher Beams library](https://github.com/neoighodaro/pusher-beams) we just pulled in using composer. To set up, open the `.env` file and add the following keys:

```
PUSHER_BEAMS_SECRET_KEY="PUSHER_BEAMS_SECRET_KEY"
    PUSHER_BEAMS_INSTANCE_ID="PUSHER_BEAMS_INSTANCE_ID"
```

You should replace the `PUSHER_BEAMS_*` placeholders with the keys you got when setting up your Beams application.

Next, open the `config/broadcasting.php` file and scroll until you see the `connections` key. In there, you’ll have the `pusher` settings, add the following to the `pusher` configuration:

```php
'pusher' => [
        // [...]
        
        'beams' => [
            'secret_key' => env('PUSHER_BEAMS_SECRET_KEY'),
            'instance_id' => env('PUSHER_BEAMS_INSTANCE_ID'),
        ],
    ],
```

### Setting up our Pusher Channels library

The next step is to set up Pusher Channels. Laravel comes with native support for Pusher Channels so we do not need to do much to set it up.

Open the `.env` file and update the following keys below:

```
BROADCAST_DRIVER=pusher

    // [...]
    
    PUSHER_APP_ID="PUSHER_APP_ID"
    PUSHER_APP_KEY="PUSHER_APP_KEY"
    PUSHER_APP_SECRET="PUSHER_APP_SECRET"
    PUSHER_APP_CLUSTER="PUSHER_APP_CLUSTER"
```

Above you set the `BROADCAST_DRIVER` to `pusher` and then for the other `PUSHER_APP_*` keys, replace the placeholders with the keys gotten from your Pusher dashboard. That’s all we need to do to set up Pusher Channels for this application.

### Building the backend application

Now that we have set up all the dependencies, we can start building the application. We will start by creating the routes. However, instead of creating controllers to hook into the routes, we will be adding the logic directly to the routes.

#### Setting up the database, migration, and model

Since we will be working with a database, we need to set up the database we are going to be working with. To make things easy we will be using SQLite. Create an empty `database.sqlite` file in the `database` directory.

Open the `.env` file and replace:

```
DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=homestead
    DB_USERNAME=homestead
    DB_PASSWORD=secret
```

With

```
DB_CONNECTION=sqlite
    DB_DATABASE=/full/path/to/your/database.sqlite
```

Next, let’s create a migration for the `devices` table. We will use this table to store devices and their notification settings. This will help us know what devices to send push notifications to.

Run the command below to create the migration and model:

```bash
$ php artisan make:model Device -m
```

> _The `-m` flag will instruct artisan to create a migration alongside the model._

This command will generate two files, the migration file in the `database/migrations` and the model in the `app` directory. Let’s edit the migration file first.

Open the `*_create_devices_table.php` migration file in the `database/migrations` directory and replace the contents with the following:

```php
<?php

    use Illuminate\Support\Facades\Schema;
    use Illuminate\Database\Schema\Blueprint;
    use Illuminate\Database\Migrations\Migration;
    
    class CreateDevicesTable extends Migration
    {
        /**
         * Run the migrations.
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
         * Reverse the migrations.
         *
         * @return void
         */
        public function down()
        {
            Schema::dropIfExists('devices');
        }
    }
```

In the `up` method, we have defined the structure of the `devices` table. We have the `uuid` field which will be a unique string for each device registered. We have two `btc_notify` fields which are there to save the minimum and maximum prices of BTC at which point the device should be notified. Same applies to the* `eth_*_notify` fields.

To run the migration, run the command below:

```bash
$ php artisan migrate
```

Open the `app/Device.php` model and replace the contents with the code below:

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

In the model above, we have set the `$timestamps` property to `false` to make sure that Eloquent does not try to update the `created_at` and `updated_at` fields, which is the normal behavior.

We also have the `scopeAffected` method which is an example of an [Eloquent scope](https://laravel.com/docs/5.6/eloquent#local-scopes). We use this to get the affected devices after a price change has occurred on a currency. So if, for instance, BTC’s price drops, this method will check the devices and the settings to see the devices that need to be notified of this change.

> _Local scopes allow you to define common sets of constraints that you may easily re-use throughout your application. For example, you may need to frequently retrieve all users that are considered “popular”. To define a scope, prefix an Eloquent model method with `scope`. - [Laravel documentation](https://laravel.com/docs/5.6/eloquent#local-scopes)._

We will use this scope later in our application when we need to know what devices to send push notifications to.

#### Creating the routes

Open the `routes/api.php` file and replace the contents of the file with the following code:

```php
// File: routes/api.php
    <?php
    use App\Device;
    use Illuminate\Http\Request;
```

Next, let’s add the first route. Append the code below to the routes file:

```php
// File: routes/api.php
    Route::get('/settings', function (Request $request) {
        return Device::whereUuid($request->query('u'))->firstOrFail()['settings'];
    });
```

In the route above, we are returning the settings for the device supplied in the `u` query parameter. This means if a registered device hits the `/settings` endpoint and passes the device UUID through the `u` parameter, the settings for that device will be returned.

Next, in the same routes file, paste the following at the bottom of the file:

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

Above, we have defined the route for the `POST /settings` route. This route saves settings to the database. It will create a new entry if the setting does not already exist or will update the existing one if it does.

That’s all for the routes.

#### Creating the jobs, events, and notifiers

Next, we need to create the [Laravel job](https://laravel.com/docs/5.6/queues#creating-jobs) that will run at intervals to check if there is a change in the currency price.

Run the command below to create a new Laravel job:

```bash
$ php artisan make:job CheckPrices
```

This will create a new `CheckPrices` class in the `app` directory. Open that class and replace the contents with the following:

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
         * Execute the job.
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

In the class above, we implement the `ShouldQueue` interface. This makes it so that the job can and will be queued. In a production server, queueing jobs makes your application faster as it queues jobs that might take a while to execute for later execution.

We have four methods in this class. The first one is the `handle` method. This one is called automatically when the job is executed. In this method, we fetch the prices for the available currencies and then check if the price has changed. If it has, we publish a Pusher Channel event and then check if there are any devices that need to be notified based on the user’s settings. If there are any, we send a push notification to that device.

We have the `triggerPusherUpdate` method which triggers a `CurrencyUpdated` event. We will create this event in the next section. We also have a `triggerPossiblePushNotification` method which gets the list of devices which should be notified of the currency change and then notifies the user using the `CoinPriceChanged` class, which we will create in the next section.

Lastly, we have the `getPricesForSupportedCurrencies` method which just fetches the current price of a currency. In this method, we have a debug mode that simulates the current price of a currency.

To make sure this class we just created is scheduled properly, open the `app/Console/Kernel.php` file and in the `schedule` method, add the following code to the `schedule` method:

```php
$schedule->job(new \App\Jobs\CheckPrices)->everyMinute();
```

Now every time we run the command `php artisan schedule:run` all the jobs in this `schedule` method will be run. Normally, in a production environment, we will need to add the schedule command as a cronjob, however, we will run this command manually.

The next thing to do will be to create the notifiers and events. In your terminal, run the following commands:

```bash
$ php artisan make:event CurrencyUpdated    $ php artisan make:notification CoinPriceChanged
```

This will create a class in the `Events` and `Notifications` directories.

In the [event](https://laravel.com/docs/5.6/events) class, `CurrencyUpdated` paste the following code:

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

In the event class above, we have the `broadcastOn` method that specifies the Pusher channel we want to broadcast an event on. We also have the `broadcastAs` method which specifies the name of the event we want to broadcast to the channel.

In the `CoinPriceChanged` [notification](https://laravel.com/docs/5.6/notifications) class, replace the contents with the following code:

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

In the class above we have the `toPushNotification` class which prepares the push notification using the Pusher Beams library. We also have the `pushNotificationInterest` method which sets the name for the interest of the push notification depending on the currency and device ID.

That’s all for the backend, now just run the command below to start the server:

```
$ php artisan serve
```

This will start a PHP server with our application running. Also if you need to manually trigger a currency change, run the command below:

```bash
$ php artisan schedule:run
```

Now that we are done with the backend, we can create the application using Swift and Xcode.

### Conclusion

In this part of the article, we have created the backend for our cryptocurrency alert application. [In the next part](https://pusher.com/tutorials/cryptocurrency-tracking-swift-laravel-part-2), we will be seeing how we can create the application that will consume the API we just created in this part.

The source code to this application is available on [GitHub](https://github.com/neoighodaro/cryptocurrency-alert-ios-app).

This article was first published to [pusher.](https://pusher.com/tutorials/cryptocurrency-tracking-swift-laravel-part-1)

