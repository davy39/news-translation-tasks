---
title: Comment j'ai construit un bot Slack RH avec Node et Botkit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T16:18:30.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-hr-slack-bot-with-node-and-botkit-6b23b81531bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3qx-9q-OBdf0zcge4Ca8yw.jpeg
tags:
- name: bots
  slug: bots
- name: Human Resources
  slug: human-resources
- name: slack
  slug: slack
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit un bot Slack RH avec Node et Botkit
seo_desc: 'By Alexandre Robin

  Why create a Slack Bot ?

  I am an HR professional. More specifically I am a Human Resources Information System
  (HRIS) Consultant. I work with Application Tracking Systems, Learning Management
  Systems, and Core HR. But I have never h...'
---

Par Alexandre Robin

### Pourquoi créer un bot Slack ?

Je suis un professionnel des ressources humaines. Plus spécifiquement, je suis consultant en systèmes d'information des ressources humaines (HRIS). Je travaille avec des systèmes de suivi des candidatures, des systèmes de gestion de l'apprentissage et des systèmes RH de base. Mais je n'ai jamais eu l'opportunité de travailler avec un bot RH. Ce qui pourrait être l'avenir des RH.

J'ai lu beaucoup de choses sur les bots sur Slack et Messenger, et j'en ai utilisé certains dans ma vie quotidienne — Product Hunt, GitHub et Trello. Mais pour des besoins RH, je n'ai jamais eu l'opportunité de travailler avec un outil adapté à mes besoins.

C'est pourquoi j'ai décidé de travailler sur mon propre bot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyhNkd0jd7Zd3zBDLaKpSg.png)
_Moi commençant à travailler_

### Mes objectifs

Mon bot devrait être capable de gérer tous les besoins qu'une petite entreprise pourrait avoir sur Slack :

* Intégration
* Mettre les gens en contact
* Rappels
* Annonces
* Anniversaires / Anniversaires de travail
* Et bien plus encore

### Révision des bases

Pour ce programme, j'utiliserai :

* Botkit
* Node JS
* Serveur Express
* MongoDB
* API Slack & bien sûr

Botkit est :

> Une façon facile de construire des utilisateurs bots, surtout si vous travaillez déjà avec [Node.js](https://nodejs.org/), est le [**Botkit**](https://howdy.ai/botkit/) de Howdy. Botkit est un framework qui prend en charge la plupart de ces gymnastiques API, afin que vous puissiez vous concentrer sur le comportement de votre bot.

Exactement ce que je cherchais :-)

Botkit fournit un modèle pour Slack. Mais j'ai choisi de partir de zéro pour avoir une meilleure compréhension de mon bot. Cependant, c'est une bonne idée de s'entraîner avec un bot créé sur [Glitch](https://glitch.com/botkit).

#### Comment fonctionnent les bots Slack ?

Je ne suis pas un expert. J'ai lu et relu la documentation officielle de Slack et Botkit. Je ne suis toujours pas sûr d'avoir tout compris. Voici ma compréhension du comportement d'un bot Slack :

Chaque application sur Slack a un "périmètre" qui est un périmètre sur lequel une application peut lire ou effectuer des actions. Un bot fait partie d'une application créée et installée sur Slack.

Par conséquent, lorsque vous installez une application sur Slack, vous lui donnez accès à certaines informations et permissions. Pour votre bot, vous voulez qu'il soit, au moins, capable d'envoyer et de répondre aux messages d'autres utilisateurs.

Il y a alors deux cas :

1. Vous voulez que votre bot réagisse aux événements se produisant **directement dans Slack**
2. Vous voulez que votre bot réagisse aux événements se produisant **sur votre serveur**

Nous verrons les deux dans cet article !

### Mise en route

Avant toute chose, vous aurez besoin d'un serveur. Dans mon cas, Express.

Ci-dessous, vous trouverez mon fichier server.js :

```javascript
var express = require('express');
var app = express();
var http = require('http').Server(app);
var dotenv = require('dotenv');

// configuration ===========================================
//charge les variables d'environnement,
dotenv.load();

// dossier public pour les images, css,...
app.use(express.static(__dirname + '/public'))

//analyse
app.use(bodyParser.json()); // pour analyser application/json
app.use(bodyParser.urlencoded({
    extended: true
})); //pour analyser url encoded

// moteur de vue ejs
app.set('view engine', 'ejs');

// routes
require('./routes/routes')(app);

//botkit
require('./controllers/botkit')


//DÉMARRAGE ===================================================
http.listen(app.get('port'), function() {
    console.log('écoute sur le port ' + app.get('port'));
});
```

Ce port doit être public et accessible, pas seulement sur un localhost.

Pour le moment, ce serveur est une page blanche, ne montrant et ne traitant rien.

Vous aurez ensuite besoin d'une application Slack : suivez simplement ce [lien](https://api.slack.com/apps) pour en créer une.

Ensuite, vous devrez configurer votre contrôleur. Le contrôleur est le cerveau de votre bot. Il contient toutes les compétences et configurations. Ci-dessous se trouve mon fichier botkit.js. Il a presque le même contenu que celui trouvé dans le kit de démarrage de Botkit disponible ici : [https://github.com/howdyai/botkit-starter-slack](https://github.com/howdyai/botkit-starter-slack)

```javascript
var mongoUri = 'mongodb://localhost:27017/nameofyourDB'
var database = require('../config/database')({
    mongoUri: mongoUri
})
var request = require('request')

if (!process.env.SLACK_ID || !process.env.SLACK_SECRET || !process.env.PORT) {
    console.log('Erreur : Spécifiez SLACK_ID SLACK_SECRET et PORT dans l'environnement');
    process.exit(1);
}

var controller = Botkit.slackbot({
    storage: database,
    clientVerificationToken: process.env.SLACK_TOKEN
})

exports.controller = controller
   
//FONCTIONS DE CONNEXION=====================================================

exports.connect = function(team_config) {
        var bot = controller.spawn(team_config);
        controller.trigger('create_bot', [bot, team_config]);
    }
    // juste une façon simple de s'assurer que nous ne
    // nous connectons pas à la RTM deux fois pour la même équipe
var _bots = {};

function trackBot(bot) {
    _bots[bot.config.token] = bot;
}

controller.on('create_bot', function(bot, team) {
    if (_bots[bot.config.token]) {
        // déjà en ligne ! ne rien faire.
        console.log("déjà en ligne ! ne rien faire.")
    } else {
        bot.startRTM(function(err) {
            if (!err) {
                trackBot(bot);
                console.log("RTM ok")
                controller.saveTeam(team, function(err, id) {
                    if (err) {
                        console.log("Erreur lors de l'enregistrement de l'équipe")
                    } else {
                        console.log("Équipe " + team.name + " enregistrée")
                    }
                })
            } else {
                console.log("RTM échoué")
            }
            bot.startPrivateConversation({
                user: team.createdBy
            }, function(err, convo) {
                if (err) {
                    console.log(err);
                } else {
                    convo.say('Je suis un bot qui vient de rejoindre votre équipe');
                    convo.say('Vous devez maintenant /invite me to a channel so that I can be of use!');
                }
            });
        });
    }
});

//RÉACTIONS AUX ÉVÉNEMENTS==========================================================
// Gérer les événements liés à la connexion websocket à Slack

controller.on('rtm_open', function(bot) {
    console.log('** L'API RTM vient de se connecter !')
});

controller.on('rtm_close', function(bot) {
    console.log('** L'API RTM vient de se fermer');
    // vous pouvez vouloir tenter de la rouvrir
});
```

#### Déverrouiller le premier cas : réagir aux événements se produisant sur Slack

![Image](https://cdn-media-1.freecodecamp.org/images/1*51uJInZFmmF_0gD3ICFr9Q.jpeg)

Lorsque vous donnez les bonnes permissions à votre application, chaque fois qu'un message est envoyé sur un canal, Slack envoie une requête à votre serveur avec certaines informations — l'ID du canal, l'utilisateur, le timestamp et, surtout, le contenu du message.

Si nous voulons que notre bot réagisse à un simple message comme "Hi", nous devons donner à Slack une adresse pour envoyer les informations.

Dans un fichier routes.js, écrivez :

```javascript
var Request = require('request')
var slack = require('../controllers/botkit')
module.exports = function(app) {
 app.post('/slack/receive', function(req,res){
//répondre à Slack que le webhook a été reçu.
    res.status(200);
// Maintenant, transmettre le webhook pour être traité
    slack.controller.handleWebhookPayload(req, res)
  })
}
```

Nous avons maintenant un webhook : [http://votre-ip-ou-domaine:port/slack/receive](http://votre-ip-ou-domaine:port/slack/receive)

Une fois que Slack est informé de cette route via la page Event Subscriptions de votre application Slack, il pourra lui envoyer du JSON. Vous pourrez le recevoir grâce à la partie d'analyse du fichier server.js ci-dessus.

Voici un schéma (simple) pour expliquer le processus derrière cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*c-Km3PgTIihfbthJC0BFfw.png)

1- SLACK « Voici un fichier JSON avec le dernier événement sur votre canal Slack »

2- SERVEUR « Okay bien reçu, je l'envoie à Botkit »

3- BOTKIT « Voici une réponse temporaire, attendez une seconde »

4- BOTKIT « Oui ! J'entends un mot-clé, voici un objet JSON avec l'action à effectuer »

Si nous voulons que notre bot réagisse chaque fois qu'il entend « Hello », nous pouvons simplement ajouter cette fonction .hears() à notre contrôleur :

```javascript
controller.hears(['hello', 'hi'], 'direct_message,direct_mention,mention', function(bot, message) {
controller.storage.users.get(message.user, function(err, user) {
        if (user && user.name) {
            bot.reply(message, 'Hello ' + user.name + '!!');
        } else {
            bot.reply(message, 'Hello.');
        }
    });
});
```

Remarquez la partie `storage.users.get()` dans cet extrait. Botkit est compatible avec presque tous les systèmes de base de données disponibles sur le marché. J'ai décidé d'utiliser MongoDB parce qu'il était sur ma liste d'apprentissage depuis longtemps. De plus, la documentation avec Botkit est détaillée.

Maintenant, nous devons laisser notre imagination faire le travail et trouver quelques fonctionnalités amusantes à créer.

#### Deuxième cas : initier une conversation avec votre bot

![Image](https://cdn-media-1.freecodecamp.org/images/1*pEUkhsJtGgYrzGvq0xf57Q.jpeg)

Pour cette fonctionnalité, je voulais que mon bot réagisse à des événements qui n'étaient pas initiés sur Slack. Par exemple, faire une routine quotidienne. Si c'est l'anniversaire de quelqu'un dans l'entreprise, envoyez-lui un sondage demandant ses sentiments sur ses premiers mois/semaines.

J'ai décidé d'utiliser node-cron : [https://github.com/kelektiv/node-cron](https://github.com/kelektiv/node-cron) pour gérer la vérification quotidienne.

Ci-dessous, un cronjob qui se déclenche tous les jours de la semaine à 9h00. Grâce à la méthode Date(), le bot obtient la date du jour et peut la comparer à la date d'entrée de l'utilisateur.

Pour obtenir uniquement les bons utilisateurs et éviter une boucle forEach, nous pouvons utiliser une requête sur notre base de données :

```javascript
var dailyCheck = new CronJob('00 00 9 * * 1-5', function() {
        /*
         * S'exécute tous les jours de la semaine (du lundi au vendredi)
         * à 09:00:00 AM. Il ne s'exécute pas le samedi
         * ou le dimanche.
         */
        console.log(`DailyCheck déclenché ${new Date()}`)
        
        //Obtient la date du jour
        let d = new Date()
        d.setUTCHours(0, 0, 0, 0)
        
        let threeMonthsAgo = new Date()
        threeMonthsAgo.setUTCMonth(d.getUTCMonth() - 3)
        threeMonthsAgo.setUTCHours(0, 0, 0, 0)


        let sevenDaysAgo = new Date()
        sevenDaysAgo.setUTCDate(d.getUTCDate() - 7)
        sevenDaysAgo.setUTCHours(0, 0, 0, 0)


        controller.storage.users.find({
            "joinedDate": {
                "$eq": +sevenDaysAgo
            }
        }, function(err, user) {
            user.forEach(function(member) {
                console.log(`Message envoyé à ${member.name}(${member.id})`)
                bot.startPrivateConversation({
                    user: member.id
                }, Conversations.sendSurvey7)
            })
        })
    }, function() {
        /* Cette fonction est exécutée lorsque le travail s'arrête */
    }, true,
    /* Démarrer le travail maintenant */
    timeZone = 'Europe/Paris' /* Fuseau horaire de ce travail. */ )
```

Et… Tada !

![Image](https://cdn-media-1.freecodecamp.org/images/0*MSZ0zXebVZ_wwCKP.)
« Un robot nommé Pepper tenant une iPad » par [Unsplash](https://unsplash.com/@agkdesign?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alex Knight</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Conclusion

Après plus d'un an en tant que campeur et en apprenant à coder, je suis vraiment heureux de pouvoir commencer et terminer un projet comme celui-ci. J'ai maintenant un bot qui fonctionne et qui effectue presque toutes les actions que j'avais en tête lors de la phase de conception. Et j'ai encore beaucoup d'idées !

Je travaille toujours sur ce bot. Le dépôt GitHub est disponible ici : [https://github.com/alexandrobin/hrbot](https://github.com/alexandrobin/hrbot). Certains des commits sont en français, mais la base de code est commentée en anglais. :-)

De plus, il est assez facile de le déployer sur Heroku avec une base de données Mongolab si vous n'avez pas de serveur !

Si vous avez des suggestions ou si vous êtes intéressé par cet article et ce projet, n'hésitez pas à laisser un commentaire ! Je serais ravi de discuter avec vous.