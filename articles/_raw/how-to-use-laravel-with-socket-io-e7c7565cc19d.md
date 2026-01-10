---
title: How to use Laravel with Socket.IO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-29T13:37:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-laravel-with-socket-io-e7c7565cc19d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d_F57yseG4_ZPqHQ8GoTlQ.jpeg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: SocketIO
  slug: socketio
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Adnan Sabanovic

  Websockets are cool. They are really helpful if you want to show real-time activities
  from your users (or perhaps some queue jobs).

  Now, if you are afraid of the word “Websockets”, don’t be. I will lay down the instructions
  on how ...'
---

By Adnan Sabanovic

**Websockets** are cool. They are really helpful if you want to show real-time activities from your users (or perhaps some queue jobs).

Now, if you are afraid of the word “_Websockets_”, don’t be. I will lay down the instructions on how you can use it and will be around to answer your questions if you need to.

I had this challenge where I needed it to show a list of people who are currently viewing a specific URL in **Laravel**. So I started thinking. Part of me wanted to do a quick hack (luckily that’s not the strongest side of mine). Whilst the other wanted to build something cool, reusable and long-lasting.

### “Why don’t you just use Pusher?”

Here is the thing.

Laravel comes with Pusher enabled. Even though _Pusher_ seems like a quick “_Plug and play_” solution (which it is), it comes with limitations. Check out [https://pusher.com/pricing](https://pusher.com/pricing)

And most of the tutorials trick you with their title of implementing Websockets when in reality they just want to give you Pusher. (And my favorite part is when they say that you can easily switch to socket.io)

### “We want to have an unlimited number of connections”

> We don’t want to worry about limitations.

Let’s start.

I am using vagrant / homestead.

For this, we will need to read about [Event Broadcasting](https://laravel.com/docs/5.6/broadcasting).

Things to note here (so I don’ t have to repeat things):

**1.** ShouldBroadcast Interface for Events

**2.** Enabling Broadcast routes and using routes/channels.php to authenticate users

**3.** Public Channel — Everyone can listen

**4.** Private Channel — You need to authorize users before they can join a channel

**5.** Presence Channel — Like Private but you can pass a lot of additional metadata on that channel and get a list of people who have joined the channel.broadcastOn() Event method

### Create Your Event

```
php artisan make:event MessagePushed
```

You can even follow the specific example in the Event Broadcasting documentation. (Which we should really).

### Install Redis

Before this, I actually had queues setup with Supervisor/Redis/Horizon. Horizon is great and you can find information about that in here [https://laravel.com/docs/5.6/horizon](https://laravel.com/docs/5.6/horizon)

Once you have your queues working, that MessagePushed event will need to use queues.

**Note**: For all of this to work, make sure you edit your .env file:

```
BROADCAST_DRIVER=redis
```

```
QUEUE_DRIVER=redis
```

```
(this is from the horizon setup actually, but we will need that for later)
```

```
REDIS_HOST=127.0.0.1
```

```
REDIS_PASSWORD=null
```

```
REDIS_PORT=6379
```

### Install Laravel Echo Server

So this part is actually where we install socket.io server that is bundled inside laravel-echo-server. You can find about it here: [https://github.com/tlaverdure/laravel-echo-server](https://github.com/tlaverdure/laravel-echo-server)

**Note**: Check the requirements at the top!

Run the following (as stated in the document)

```
npm install -g laravel-echo-server
```

And then run the init in order to get your laravel-echo-server.json file generated in the app root (which we will need to configure).

```
laravel-echo-server init
```

Once you have generated your laravel-echo-server.json file, it should look like this.

```
{
```

```
"authHost": "http://local-website.app",
```

```
"authEndpoint": "/broadcasting/auth",
```

```
"clients": [
```

```
{
```

```
"appId": "my-app-id",
```

```
"key": "my-key-generated-with-init-command"
```

```
}
```

```
],
```

```
"database": "redis",
```

```
"databaseConfig": {
```

```
"redis": {},
```

```
"sqlite": {
```

```
"databasePath": "/database/laravel-echo-server.sqlite"
```

```
},
```

```
"port": "6379",
```

```
"host": "127.0.0.1"
```

```
},
```

```
"devMode": false,
```

```
"host": null,
```

```
"port": "6001",
```

```
"protocol": "http",
```

```
"socketio": {},
```

```
"sslCertPath": "",
```

```
"sslKeyPath": "",
```

```
"sslCertChainPath": "",
```

```
"sslPassphrase": ""
```

```
}
```

**Note**: If you want to push this to your public server, make sure to add **laravel-echo-server.json** to your **.gitignore. G**enerate this file on the server, otherwise you will need to change your authHost all the time.

_Run your Laravel Echo Server_

You have to run it in order to start websockets.

```
laravel-echo-server start 
```

(inside your root — where your laravel-echo-server.json is placed)

It should start successfully. (Now we will want to add this to supervisor on your server, so it is started automatically and restarted in case it crashes)

Inside your **/etc/supervisor/conf.d/laravel-echo.conf** (just create this file inside your **conf.d** folder) place the following:

```
[program:laravel-echo]
```

```
directory=/var/www/my-website-folder
```

```
process_name=%(program_name)s_%(process_num)02d
```

```
command=laravel-echo-server start
```

```
autostart=true
```

```
autorestart=true
```

```
user=your-linux-user
```

```
numprocs=1
```

```
redirect_stderr=true
```

```
stdout_logfile=/var/www/my-website-folder/storage/logs/echo.log
```

Once you position in your Laravel root, you can run

```
pwd
```

to get the path for your ‘directory’ above and ‘stdout_logfile’ prefix.

Your user will be your Linux user (vagrant or Ubuntu or some other)

Save the file and go out.   
   
If you used vim laravel-echo.conf then when inside, press I (like Istanbul) on your keyboard to edit a file with VIM and then type ESC following :wq! To close the file and save it.

Next, we need to run the following commands:

```
sudo supervisorctl stop all sudo supervisorctl reread
```

```
sudo supervisorctl reload
```

After that check to see if laravel echo is running

```
sudo supervisorctl status
```

### Install Laravel Echo and Socket IO client

```
npm install --save laravel-echo
```

```
npm install --save socket.io-client
```

And then in your bootstrap.js (I am using Vue js) register your Echo

```
import Echo from "laravel-echo"window.io = require('socket.io-client');
```

```
// Have this in case you stop running your laravel echo server
```

```
if (typeof io !== 'undefined') {  window.Echo = new Echo({    broadcaster: 'socket.io',    host: window.location.hostname + ':6001',  });}
```

Now check again how to listen for your events on specific channels.

Following the documentation on Laravel Broadcasting we shared above, if you set your **broadcastOn()** method to return a **new PresenceChannel** (I will explain the particular case I did, but feel free to ask questions in case you need something else implemented. I find this to be of higher complexity than simply using a public channel, so we can scale down with no problems) then we want to listen for that channel on Javascript side (frontend).

Here is a concrete example:

1. I pushed an event onto a presence channel (I was dealing with surveys)

```
public function broadcastOn()
```

```
{
```

```
return new PresenceChannel('survey.' . $this->survey->id);
```

```
}
```

2. After you push the event, it will go through channels.php. In there we want to create an authorization for this user. (Remember to return an array for presence channel authorization and not a Boolean.)

```
Broadcast::channel('survey.{survey_id}', function ($user, $survey_id) {
```

```
return [
```

```
'id' => $user->id,
```

```
'image' => $user->image(),
```

```
'full_name' => $user->full_name
```

```
];
```

```
});
```

3. Then in my VueJs component that loads on the page I want to monitor I define a method that will be initiated from created() method on load:

```
listenForBroadcast(survey_id) {
```

```
Echo.join('survey.' + survey_id)
```

```
.here((users) => {
```

```
this.users_viewing = users;
```

```
this.$forceUpdate();
```

```
})
```

```
.joining((user) => {
```

```
if (this.checkIfUserAlreadyViewingSurvey(user)) {
```

```
this.users_viewing.push(user);
```

```
this.$forceUpdate();
```

```
}
```

```
})
```

```
.leaving((user) => {
```

```
this.removeViewingUser(user);
```

```
this.$forceUpdate();
```

```
});
```

```
},
```

I obviously pulled some code out of the context here but I have this ‘users_viewing’ array to keep my current users that joined the channel.

And that would be it really.

Hope you were able to follow as I tried to be detailed as I can.

Happy coding!

Follow me on [Twitter](https://twitter.com/adnanxteam)  
Add me on [LinkedIn](https://www.linkedin.com/in/adnansabanovic)

