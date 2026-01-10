---
title: Comment déclarer votre amour comme un programmeur ❤️
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-14T11:19:17.000Z'
originalURL: https://freecodecamp.org/news/send-a-romantic-message-every-hour-to-your-valentine
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/declare-your-love-as-a-programmer.png
tags:
- name: Node.js
  slug: nodejs
seo_title: Comment déclarer votre amour comme un programmeur ❤️
seo_desc: 'By Florin Pop

  Today is Valentines Day! ?

  How nice would it be if you sent a Romantic Message every hour to your loved one?
  But even better...

  How awesome would it be to do it automatically using a Node.js script? We are after
  all... programmers, righ...'
---

Par Florin Pop

Aujourd'hui, c'est la Saint-Valentin ! ?

Ce serait bien si vous envoyiez un message romantique chaque heure à votre bien-aimé(e) ? Mais encore mieux...

Ce serait génial de le faire automatiquement en utilisant un script Node.js ! Après tout, nous sommes des programmeurs, n'est-ce pas ? ?

Dans ce court tutoriel, je vais vous montrer comment faire.

P.S. Pour les paresseux, voici un tutoriel vidéo :

%[https://youtu.be/HxqMPlyZC3w]

## Créer une tâche CRON

Tout d'abord, nous devons créer une tâche CRON qui exécutera une fonction chaque heure.

Pour cela, installons le package `node-cron` dans notre application NodeJS :

`npm install node-cron`

Ensuite, nous allons planifier une fonction pour qu'elle s'exécute chaque heure :

```js
const cron = require('node-cron');

cron.schedule('0 * * * *', () => {
	sendMessage();
});
```

Parfait. Nous n'avons pas encore la fonction `sendMessage()`, mais nous la créerons plus tard.

De plus, si vous ne savez pas comment fonctionne la chaîne CRON, voici un [site génial](https://crontab.guru/#*_*_*_*_*) où vous pouvez la tester.

En gros, `'0 * * * *'` signifie : `Exécuter chaque heure à 0 minute`, donc cela s'exécutera à : `00:00, 01:00, 02:00`, etc... Vous avez compris l'idée !

## Se connecter à Twilio

Nous avons besoin d'un compte Twilio, alors rendez-vous sur [Twilio.com](www.twilio.com/referral/79CRPu) et créez-en un. Vous devez vérifier votre adresse e-mail et également vérifier le numéro auquel vous souhaitez envoyer le message. (J'ai dû "voler" le téléphone de ma femme pour vérifier le numéro ?)

Ils vous poseront quelques questions comme : "Quel langage de programmation utilisez-vous ?" Vous pouvez choisir Node.js et vous arriverez sur la page `/console`.

Ici, vous obtiendrez l'`ACCOUNT SID` et l'`AUTH TOKEN`. Nous en avons besoin pour appeler l'API Twilio, nous allons donc les stocker dans un fichier `config.js`.

**Avertissement :** Ne partagez pas l'**AUTH TOKEN**. Il s'agit d'une clé secrète, nous allons donc la stocker dans ce fichier "secret" config.js.

Super.

La prochaine étape sera de créer un numéro d'essai (vous pouvez trouver le bouton sur la page `/console`). Ce numéro sera utilisé pour envoyer les messages DEPUIS.

Maintenant que tout est en place, retournons à notre code !

Nous devons installer le package Twilio : `npm install twilio` et nous devons utiliser les données que nous avons stockées dans le fichier `./config.js`.

Avec l'`ACCOUNT_SID` et l'`AUTH_TOKEN`, nous pouvons également stocker le `PHONE_NR` de notre bien-aimé(e), car nous allons l'utiliser pour indiquer à Twilio où envoyer le message.

Faisons cela et créons également la fonction `sendMessage()`, qui enverra... un message ?.

```js
const config = require('./config');
const accountSid = config.ACCOUNT_SID;
const authToken = config.AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

function sendMessage() {
	client.messages
		.create({
			body: 'Votre message ici',
			from: '+19166191713',
			to: config.PHONE_NR
		})
		.then(message => {
			console.log(message);
		});
}
```

Vous pouvez voir que la fonction `client.messages.create()` nécessite trois choses :

1. Le corps/le message
2. Le numéro DEPUIS (il s'agit du numéro d'essai créé ci-dessus)
3. Le numéro À (il s'agit du numéro auquel nous voulons envoyer le message)

## Obtenir les messages

Nous avons besoin d'une liste de 24 messages romantiques, alors créons un fichier `messages.js` et mettons tous les messages dans un tableau.

```js
module.exports = [
	`Si je pouvais te donner une chose dans la vie, je te donnerais la capacité de te voir à travers mes yeux, seulement alors réaliserais-tu à quel point tu es spécial(e) pour moi.`,
	`Si tu étais un film, je te regarderais encore et encore.`,
	`Dans une mer de gens, mes yeux te cherchent toujours.`
];
```

J'ai seulement ajouté 3 messages ci-dessus, mais vous pouvez remplir le tableau jusqu'à obtenir 24 messages.

## Combiner le tout

Maintenant que nous avons les 3 composants :

- la tâche CRON
- l'appel Twilio sendMessage()
- les messages

Nous pouvons les combiner dans le code final :

```js
const cron = require('node-cron');

const config = require('./config');
const accountSid = config.ACCOUNT_SID;
const authToken = config.AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const messages = require('./messages');

const currentMessage = 0;

function sendMessage() {
	client.messages
		.create({
			body: messages[currentMessage],
			from: '+19166191713',
			to: config.PHONE_NR
		})
		.then(message => {
			currentMessage++;
			console.log(message);
		});
}

cron.schedule('0 * * * *', () => {
	console.log('Message envoyé !');
	sendMessage();
});
```

Vous pouvez voir que j'ai ajouté un compteur `currentMessage` qui sera incrémenté chaque fois que nous envoyons un message, de cette façon nous allons parcourir tout le tableau de messages.

C'est tout ! ?

Maintenant vous pouvez exécuter le script et il enverra un message romantique, chaque heure, à votre bien-aimé(e) !

Bonne Saint-Valentin ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/declare-your-love-as-a-programmer/)_