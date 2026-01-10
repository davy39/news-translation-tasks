---
title: Comment utiliser Laravel avec Socket.IO
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
seo_title: Comment utiliser Laravel avec Socket.IO
seo_desc: 'By Adnan Sabanovic

  Websockets are cool. They are really helpful if you want to show real-time activities
  from your users (or perhaps some queue jobs).

  Now, if you are afraid of the word “Websockets”, don’t be. I will lay down the instructions
  on how ...'
---

Par Adnan Sabanovic

Les **Websockets** sont géniaux. Ils sont vraiment utiles si vous souhaitez montrer des activités en temps réel de vos utilisateurs (ou peut-être certains travaux de file d'attente).

Maintenant, si vous avez peur du mot « Websockets », ne le soyez pas. Je vais détailler les instructions sur la façon de l'utiliser et je serai là pour répondre à vos questions si nécessaire.

J'ai eu ce défi où j'avais besoin de montrer une liste de personnes qui consultent actuellement une URL spécifique dans **Laravel**. Alors j'ai commencé à réfléchir. Une partie de moi voulait faire un hack rapide (heureusement, ce n'est pas le côté le plus fort de ma personnalité). Tandis que l'autre partie voulait construire quelque chose de cool, réutilisable et durable.

### « Pourquoi ne pas simplement utiliser Pusher ? »

Voici la chose.

Laravel est livré avec Pusher activé. Même si _Pusher_ semble être une solution rapide « Plug and play » (ce qu'il est), il vient avec des limitations. Consultez [https://pusher.com/pricing](https://pusher.com/pricing)

Et la plupart des tutoriels vous trompent avec leur titre d'implémentation de Websockets alors qu'en réalité, ils veulent simplement vous donner Pusher. (Et ma partie préférée est quand ils disent que vous pouvez facilement passer à socket.io)

### « Nous voulons avoir un nombre illimité de connexions »

> Nous ne voulons pas nous soucier des limitations.

Commençons.

J'utilise vagrant / homestead.

Pour cela, nous devrons lire sur [Event Broadcasting](https://laravel.com/docs/5.6/broadcasting).

Points à noter ici (pour que je n'aie pas à répéter les choses) :

**1.** Interface ShouldBroadcast pour les événements

**2.** Activation des routes de diffusion et utilisation de routes/channels.php pour authentifier les utilisateurs

**3.** Canal Public — Tout le monde peut écouter

**4.** Canal Privé — Vous devez autoriser les utilisateurs avant qu'ils ne puissent rejoindre un canal

**5.** Canal de Présence — Comme le canal Privé, mais vous pouvez passer beaucoup de métadonnées supplémentaires sur ce canal et obtenir une liste des personnes qui ont rejoint le canal.broadcastOn() Méthode d'événement

### Créer Votre Événement

```
php artisan make:event MessagePushed
```

Vous pouvez même suivre l'exemple spécifique dans la documentation sur la diffusion d'événements. (Ce que nous devrions vraiment faire).

### Installer Redis

Avant cela, j'avais en fait configuré des files d'attente avec Supervisor/Redis/Horizon. Horizon est génial et vous pouvez trouver des informations à ce sujet ici [https://laravel.com/docs/5.6/horizon](https://laravel.com/docs/5.6/horizon)

Une fois que vos files d'attente fonctionnent, cet événement MessagePushed devra utiliser les files d'attente.

**Note** : Pour que tout cela fonctionne, assurez-vous de modifier votre fichier .env :

```
BROADCAST_DRIVER=redis
```

```
QUEUE_DRIVER=redis
```

```
(ceci vient en fait de la configuration d'horizon, mais nous en aurons besoin pour plus tard)
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

### Installer Laravel Echo Server

Cette partie est en fait celle où nous installons le serveur socket.io qui est intégré dans laravel-echo-server. Vous pouvez en trouver plus ici : [https://github.com/tlaverdure/laravel-echo-server](https://github.com/tlaverdure/laravel-echo-server)

**Note** : Vérifiez les exigences en haut !

Exécutez ce qui suit (comme indiqué dans le document)

```
npm install -g laravel-echo-server
```

Puis exécutez l'init afin de générer votre fichier laravel-echo-server.json dans la racine de l'application (que nous devrons configurer).

```
laravel-echo-server init
```

Une fois que vous avez généré votre fichier laravel-echo-server.json, il devrait ressembler à ceci.

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

**Note** : Si vous souhaitez pousser cela sur votre serveur public, assurez-vous d'ajouter **laravel-echo-server.json** à votre **.gitignore**. Générez ce fichier sur le serveur, sinon vous devrez changer votre authHost tout le temps.

_Exécutez votre Laravel Echo Server_

Vous devez l'exécuter pour démarrer les websockets.

```
laravel-echo-server start 
```

(à l'intérieur de votre racine — où votre laravel-echo-server.json est placé)

Il devrait démarrer avec succès. (Maintenant, nous voudrons ajouter cela à supervisor sur votre serveur, afin qu'il soit démarré automatiquement et redémarré en cas de plantage)

À l'intérieur de votre **/etc/supervisor/conf.d/laravel-echo.conf** (créez simplement ce fichier à l'intérieur de votre dossier **conf.d**), placez ce qui suit :

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

Une fois que vous êtes positionné dans votre racine Laravel, vous pouvez exécuter

```
pwd
```

pour obtenir le chemin pour votre 'directory' ci-dessus et le préfixe 'stdout_logfile'.

Votre utilisateur sera votre utilisateur Linux (vagrant ou Ubuntu ou autre)

Enregistrez le fichier et sortez.   
   
Si vous avez utilisé vim laravel-echo.conf, alors une fois à l'intérieur, appuyez sur I (comme Istanbul) sur votre clavier pour éditer un fichier avec VIM, puis tapez ESC suivi de :wq! pour fermer le fichier et l'enregistrer.

Ensuite, nous devons exécuter les commandes suivantes :

```
sudo supervisorctl stop all sudo supervisorctl reread
```

```
sudo supervisorctl reload
```

Après cela, vérifiez si laravel echo est en cours d'exécution

```
sudo supervisorctl status
```

### Installer Laravel Echo et le client Socket IO

```
npm install --save laravel-echo
```

```
npm install --save socket.io-client
```

Puis dans votre bootstrap.js (j'utilise Vue js), enregistrez votre Echo

```
import Echo from "laravel-echo"window.io = require('socket.io-client');
```

```
// Ayez ceci au cas où vous arrêtez d'exécuter votre serveur laravel echo
```

```
if (typeof io !== 'undefined') {  window.Echo = new Echo({    broadcaster: 'socket.io',    host: window.location.hostname + ':6001',  });}
```

Maintenant, vérifiez à nouveau comment écouter vos événements sur des canaux spécifiques.

En suivant la documentation sur la diffusion Laravel que nous avons partagée ci-dessus, si vous définissez votre méthode **broadcastOn()** pour retourner un **new PresenceChannel** (je vais expliquer le cas particulier que j'ai fait, mais n'hésitez pas à poser des questions si vous avez besoin d'implémenter autre chose. Je trouve que cela est de complexité plus élevée que simplement utiliser un canal public, donc nous pouvons réduire l'échelle sans problèmes), alors nous voulons écouter ce canal du côté Javascript (frontend).

Voici un exemple concret :

1. J'ai poussé un événement sur un canal de présence (je traitais avec des enquêtes)

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

2. Après avoir poussé l'événement, il passera par channels.php. Là, nous voulons créer une autorisation pour cet utilisateur. (N'oubliez pas de retourner un tableau pour l'autorisation du canal de présence et non un booléen.)

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

3. Ensuite, dans mon composant VueJs qui se charge sur la page que je veux surveiller, je définis une méthode qui sera initiée à partir de la méthode created() au chargement :

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

J'ai évidemment sorti du contexte ici, mais j'ai ce tableau 'users_viewing' pour garder mes utilisateurs actuels qui ont rejoint le canal.

Et ce serait tout.

J'espère que vous avez pu suivre car j'ai essayé d'être aussi détaillé que possible.

Bon codage !

Suivez-moi sur [Twitter](https://twitter.com/adnanxteam)  
Ajoutez-moi sur [LinkedIn](https://www.linkedin.com/in/adnansabanovic)