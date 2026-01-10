---
title: Comment j'ai construit une application de chat publique et anonyme en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-16T08:36:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-public-anonymous-chat-app-in-javascript-34f082b9b98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eDuyL7l8N39gsDb-KFLtog.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit une application de chat publique et anonyme en JavaScript
seo_desc: 'By Peter Mbanugo

  We’re all familiar with instant messaging and using it to chat to people in realtime.
  Sometimes, though, we might want an app which allows us to send messages anonymously
  to friends, or to chat anonymously with strangers in close pro...'
---

Par Peter Mbanugo

Nous sommes tous familiers avec la messagerie instantanée et son utilisation pour discuter avec des personnes en temps réel. Parfois, cependant, nous pourrions vouloir une application qui nous permet d'envoyer des messages de manière anonyme à des amis, ou de discuter anonymement avec des inconnus à proximité. Un exemple d'une telle application est [Truth](https://itunes.apple.com/us/app/truth-be-honest/id791407399), qui vous permet de parler avec des personnes sur votre liste de contacts sans révéler votre identité.

Dans ce tutoriel, je vais vous montrer comment construire une application de chat publique et anonyme en JavaScript (en utilisant NodeJS et Express sur le serveur, et VanillaJS sur le client) et [Pusher](https://pusher.com/). Pusher nous permet de construire des applications temps réel scalables et fiables. Puisque nous avons besoin d'une livraison en temps réel des messages de chat, cela constitue un composant clé de l'application de chat. L'image ci-dessous représente ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/UzRs8hsRfZPpnqeAPkX6PSuscmYy7ExfoBnT)
_Le produit final_

### Installation

Commençons par [créer un compte Pusher gratuit](https://pusher.com/signup) (ou vous connecter si vous en avez déjà un). Une fois connecté, créez une nouvelle application Pusher depuis le [tableau de bord](https://dashboard.pusher.com/) et notez votre ID d'application, votre clé et votre secret, qui sont uniques à une application.

Pour créer une nouvelle application Pusher, cliquez sur le menu latéral `Vos applications`, puis sur le bouton `Créer une nouvelle application` sous le tiroir. Cela ouvre l'assistant de configuration.

1. Entrez un nom pour l'application. Dans ce cas, je l'appellerai « chat ».
2. Sélectionnez un cluster.
3. Sélectionnez l'option « Créer une application pour plusieurs environnements » si vous souhaitez avoir différentes instances pour le développement, la mise en scène et la production.
4. Sélectionnez **Vanilla JS** comme frontend et **NodeJS** comme backend.
5. Terminez le processus en cliquant sur le bouton `Créer mon application` pour configurer votre instance d'application.

![Image](https://cdn-media-1.freecodecamp.org/images/rrVg7QIPvlWQV67aVfEF6MUx4AFbYcaoIpYz)
_Création de l'application Pusher_

### Coder le serveur

Nous avons besoin d'un backend qui servira nos fichiers statiques et acceptera également les messages d'un client pour ensuite les diffuser à d'autres clients connectés via Pusher. Notre backend sera écrit en NodeJS, nous devons donc le configurer.

Nous avons besoin d'un fichier `package.json`, et je vais l'ajouter en exécutant la commande ci-dessous. J'utiliserai les valeurs par défaut fournies en appuyant sur Entrée pour chaque invite.

> _$ npm init_

Avec le fichier `package.json` ajouté, j'installerai les packages npm **Express**, **body-parser** et **Pusher**. Exécutez la commande suivante :

> _$ npm install --save pusher express body-parser_

Avec ces packages installés, ajoutons un nouveau fichier appelé `server.js` avec le contenu suivant :

```
var express = require('express');var bodyParser = require('body-parser');var Pusher = require('pusher');
```

```
var app = express();app.use(bodyParser.json());app.use(bodyParser.urlencoded({ extended: false }));
```

```
var pusher = new Pusher({ appId: "APP_ID", key: "APP_KEY", secret:  "APP_SECRET", cluster: "APP_CLUSTER" });
```

```
app.post('/message', function(req, res) {  var message = req.body.message;  pusher.trigger( 'public-chat', 'message-added', { message });  res.sendStatus(200);});
```

```
app.get('/',function(req,res){           res.sendFile('/public/index.html', {root: __dirname });});
```

```
app.use(express.static(__dirname + '/public'));
```

```
var port = process.env.PORT || 5000;app.listen(port, function () {  console.log(`app listening on port ${port}!`)});
```

Avec le code ci-dessus, nous avons défini un point de terminaison `/message` qui sera utilisé par un client pour envoyer un message à un autre via Pusher. Les autres routes sont utilisées pour servir les fichiers statiques que nous ajouterons plus tard.

Remplacez les chaînes de caractères de remplissage App ID, Secret et Key par les valeurs de votre tableau de bord Pusher. Ajoutez cette instruction `"start": "node server.js"` dans la propriété **script** de notre fichier `package.json`. Cela nous permettra de démarrer le serveur lorsque nous exécuterons **npm start**.

### Construire le frontend

Passons au frontend, ajoutons un nouveau dossier appelé **public**. Ce dossier contiendra notre page et nos fichiers JavaScript. Ajoutez un nouveau fichier appelé **style.css** avec le contenu ci-dessous, qui contiendra notre définition de style pour la page.

```
@import url("http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css");.chat{    list-style: none;    margin: 0;    padding: 0;}
```

```
.chat li{    margin-bottom: 10px;    padding-bottom: 5px;    border-bottom: 1px dotted #B3A9A9;}
```

```
.chat li.left .chat-body{    margin-left: 60px;}
```

```
.chat li.right .chat-body{    margin-right: 60px;}
```

```
.chat li .chat-body p{    margin: 0;    color: #777777;}
```

```
.panel .slidedown .glyphicon, .chat .glyphicon{    margin-right: 5px;}
```

```
.body-panel{    overflow-y: scroll;    height: 250px;}
```

```
::-webkit-scrollbar-track{    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);    background-color: #F5F5F5;}
```

```
::-webkit-scrollbar{    width: 12px;    background-color: #F5F5F5;}
```

```
::-webkit-scrollbar-thumb{    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);    background-color: #555;}
```

Ajoutez un autre fichier appelé **index.html** avec le balisage ci-dessous.

```
<!DOCTYPE html><html><head>    <!-- Latest compiled and minified CSS -->    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
```

```
    <!-- Optional theme -->    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
```

```
    <script        src="https://code.jquery.com/jquery-2.2.4.min.js"        integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="        crossorigin="anonymous"><;/script>
```

```
    <!-- Latest compiled and minified JavaScript -->    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"&gt;</script>
```

```
    <link rel="stylesheet" href="style.css">    <script src="https://js.pusher.com/4.0/pusher.min.js"></script>    <script src="index.js"></script></head><body>    <div class="container">    <div class="row form-group">        <div class="col-xs-12 col-md-offset-2 col-md-8 col-lg-8 col-lg-offset-2">            <div class="panel panel-primary">                <div class="panel-heading">                    <span class="glyphicon glyphicon-comment"></span> Chat Anonyme                    <div class="btn-group pull-right">                        <button type="button" class="btn btn-default btn-xs dropdown-toggle" data-toggle="dropdown">                            <span class="glyphicon glyphicon-chevron-down"></span>                        </button>                        <ul class="dropdown-menu slidedown">                            <li><a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-refresh">                            </span>Rafraîchir</a></li>                            <li><a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-ok-sign">                            </span>Disponible</a></li>                            <li><a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-remove">                            </span>Occupé</a></li>                            <li><a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-time"></span>                                Absent</a></li>                            <li class="divider"></li>                            <li><a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-off"></span>                                Se déconnecter</a></li>                        </ul>                    </div>                </div>                <div class="panel-body body-panel">                    <ul class="chat">
```

```
                    </ul>                </div>                <div class="panel-footer clearfix">                    <textarea id="message" class="form-control" rows="3"></textarea>                    <span class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-xs-12" style="margin-top: 10px">                        <button class="btn btn-warning btn-lg btn-block" id="btn-chat">Envoyer</button>                    </span>                </div>            </div>        </div>    </div></div>
```

```
<script id="new-message-other" type="text/template">    <li class="left clearfix">        <span class="chat-img pull-left">            <img src="http://placehold.it/50/55C1E7/fff&text=U" alt="User Avatar" class="img-circle" />        </span>        <div class="chat-body clearfix">            <p>                {{body}}            </p>        </div>    </li></script>
```

```
<script id="new-message" type="text/template">    <li id="{{id}}" class="right clearfix">        <div class="chat-body clearfix">            <p>                {{body}}            </p>        </div>    </li></script>
```

```
</body>&lt;/html>
```

J'utilise un modèle de [bootsnipp](http://bootsnipp.com/snippets/6eWd) qui a été légèrement modifié pour afficher uniquement le nom et le message.

Ajoutez un nouveau fichier appelé **index.js** avec le contenu ci-dessous. N'oubliez pas d'ajouter les détails de l'application Pusher :

```
$(document).ready(function(){        var pusher = new Pusher('APP_KEY', {        cluster: 'APP_CLUSTER',        encrypted: false    });
```

```
    let channel = pusher.subscribe('public-chat');    channel.bind('message-added', onMessageAdded);
```

```
    $('#btn-chat').click(function(){        const message = $("#message").val();        $("#message").val("");
```

```
        //envoyer le message        $.post( "http://localhost:5000/message", { message } );    });
```

```
    function onMessageAdded(data) {        let template = $("#new-message").html();        template = template.replace("{{body}}", data.message);
```

```
        $(".chat").append(template);    }});
```

Avec le code de ce fichier, nous obtenons le message à envoyer puis appelons le serveur avec le message. Après cela, nous nous connectons à Pusher en créant un nouvel objet Pusher avec la clé de l'application et le cluster que vous avez définis précédemment.

Nous nous abonnons à un canal et à un événement nommé `message-added`. Le canal est un canal public, vous pouvez donc le nommer comme vous le souhaitez. J'ai choisi de préfixer le mien avec `public-`, mais ce n'est que ma propre convention de nommage personnelle, car il n'y a pas de règles pour un canal public. La différence entre un canal `public` et un canal `private` ou `presence` est qu'un canal public ne nécessite pas qu'un client soit authentifié et peut être souscrit par quiconque connaît le nom du canal. Vous pouvez en savoir plus sur les canaux Pusher [ici](https://pusher.com/docs/client_api_guide/client_channels).

Nous nous connectons à l'événement de clic du bouton de chat sur la page, récupérons le message de la zone de texte sur la page, puis l'envoyons au serveur avec le nom d'utilisateur. Avec tout ce que nous avons configuré, nous pouvons démarrer l'application en exécutant `npm start`. Voici un aperçu de son fonctionnement sur mon ordinateur.

![Image](https://cdn-media-1.freecodecamp.org/images/Ku2BCi85o9F4W6zDSp-rMyfpWngfvrCy3uLr)

### Conclusion

Il s'agit d'une application montrant comment vous pouvez utiliser Pusher pour envoyer des messages en temps réel. Nous avons construit une application de chat publique et anonyme qui permet aux visiteurs de votre site Web d'envoyer des messages anonymes les uns aux autres en temps réel. Vous pouvez trouver le code ici sur [GitHub](https://github.com/pmbanugo/Pusher-Anonymous-Chat-App)

_Cet article a été initialement publié sur [Pusher](https://blog.pusher.com/build-secure-chat-web-app-javascript-auth0-pusher/)_