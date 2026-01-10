---
title: Comment j'ai construit un bot Twitter qui génère des paroles de chansons
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-30T22:41:15.000Z'
originalURL: https://freecodecamp.org/news/building-a-twitter-lyric-bot-12468255a4ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*znQJ9QO7vwypsv2mZPiUxQ.jpeg
tags:
- name: bots
  slug: bots
- name: Heroku
  slug: heroku
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit un bot Twitter qui génère des paroles de chansons
seo_desc: 'By Shawn Toubeau

  In this article, I will go over how I built my Twitter lyric bot and how you’ll
  be able to set up your very own.

  Procedure

  Here’s a list of the components we have to set up.


  Twitter Account

  Text Editor/IDE

  The bot

  Heroku Automation

  ...'
---

Par Shawn Toubeau

Dans cet article, je vais expliquer comment j'ai construit mon bot Twitter de paroles et comment vous pourrez configurer le vôtre.

### Procédure

Voici une liste des composants que nous devons configurer.

1. Compte Twitter
2. Éditeur de texte/IDE
3. Le bot
4. Automatisation Heroku

### **Créer une nouvelle application Twitter**

Pour créer une nouvelle application Twitter, rendez-vous [ici](https://developer.twitter.com/en/apps). Vous devrez demander un accès développeur. Après avoir soumis la demande, cela peut prendre un certain temps, mais Twitter vous notifiera lorsque vous serez accepté.

### **Configurer l'éditeur/IDE**

Maintenant, vous allez vouloir configurer votre éditeur. Ma préférence est VS Code, donc c'est ce que j'utiliserai.

Assurez-vous d'avoir Git et Node installés.

Allez-y, clonez le dépôt git suivant sur votre ordinateur.

```
git clone https://github.com/ShawnToubeau/lyric-bot.git
```

### Parcours du code

Les 3 fichiers principaux dont le bot se compose sont bot.js, lyrics.txt et .env.

**Note** : Votre clone du projet ne contiendra pas de fichier .env en raison du .gitignore, nous allons donc créer le nôtre plus tard dans l'article !

#### bot.js

En commençant par bot.js, nous commençons par importer Twit, fs et dotenv.

Twit est un module qui supporte l'API Twitter Developer.

Fs, ou file system, est un module d'E/S de fichiers qui nous permet d'interagir avec notre fichier lyrics.txt.

Dotenv est un module qui lit les variables d'environnement stockées dans notre fichier .env.

```
const Twit = require('twit');
```

```
const fs = require('fs');
```

```
require('dotenv').config();
```

```
const order = 4; // longueur de chaque n-gramme
```

```
let nGrams = {};
```

```
const Bot = new Twit({
```

```
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
```

```
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
```

```
  access_token: process.env.TWITTER_ACCESS_TOKEN,
```

```
  access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
```

```
});
```

nGrams est l'objet qui suit les occurrences de sous-chaînes afin que nous puissions utiliser une probabilité pour générer nos propres paroles de manière aléatoire. Vous pouvez en lire plus à ce sujet [ici](https://en.wikipedia.org/wiki/N-gram).

Et Bot est... eh bien... notre Bot ! Nous devons définir certaines variables pour le faire fonctionner. En utilisant le module dotenv, nous pouvons récupérer les valeurs stockées dans notre fichier .env.

Ensuite, nous définissons quelques fonctions comme suit :

#### pickRandomStart()

```
function pickRandomStart(lyrics) {
```

```
  const random = Math.floor(Math.random()*lyrics.length)
```

```
  return lyrics.substring(random, random + order)
```

```
}
```

Cela sélectionne le point de départ où nous récupérons notre premier n-gramme.

#### makeEngramModel()

```
function makeEngramModel(lyrics) {
```

```
  for (let i = 0; i < lyrics.length - order; i++) {
```

```
    const gram = lyrics.substring(i, i + order);
```

```
    if (!nGrams[gram]) {
```

```
    nGrams[gram] = [];
```

```
    }
```

```
    nGrams[gram].push(lyrics.charAt(i + order));
```

```
  }
```

```
}
```

Cela crée le modèle qui suit l'ordre et les occurrences de tous les n-grammes analysés à partir des paroles. En utilisant le nombre d'occurrences comme probabilité du n-gramme, cela nous permet de générer de nouvelles paroles dans un ordre aléatoire.

#### tweet()

```
function tweet() {
```

```
  fs.readFile('lyrics.txt', 'utf8', function(error, lyrics) {
```

```
  if (error) {
```

```
  console.log(error.message);
```

```
  } else {
```

```
    makeEngramModel(lyrics);
```

```
    let currentGram = pickRandomStart(lyrics);
```

```
      // vérifie si le début du tweet ne commence pas
```

```
      // par une ponctuation ou des caractères spéciaux et se termine par un espace
```

```
      while (!currentGram.match(/^[0-9a-zA-Z]+$/)) {
```

```
        currentGram = pickRandomStart(lyrics);
```

```
      }
```

```
      let tweet = currentGram;
```

```
      // s'exécute jusqu'à ce que la limite de caractères soit atteinte tout en terminant le dernier mot
```

```
      for (let j = 0; (j < 150) || (tweet.charAt(j).match(/^[0-9a-zA-Z]+$/)); j++) {
```

```
        const possibilities = nGrams[currentGram];
```

```
        const next = possibilities[Math.floor(Math.random()*possibilities.length)];
```

```
        tweet += next;
```

```
        const len = tweet.length;
```

```
        currentGram = tweet.substring(len-order, len);
```

```
      }
```

```
      console.log(tweet)
```

```
      Bot.post('statuses/update', {status: tweet}, function(error, tweet, response) {
```

```
        if (error) {
```

```
          console.log("Error making post. ", error.message);
```

```
        };
```

```
      });
```

```
    }
```

```
  });
```

```
}
```

Enfin, mais non des moindres, c'est la partie qui interagit avec le bot. Elle commence par lire les paroles en utilisant le module fs, puis crée le modèle n-gramme en utilisant la variable lyrics. Elle sélectionne un point de départ aléatoire à utiliser comme premier n-gramme, qui sera le début des nouvelles paroles. Elle effectue une vérification pour voir si le premier n-gramme ne contient que des caractères alphanumériques, car il a alors une plus grande chance de commencer de manière plus sensée.

Elle enchaîne ensuite des n-grammes sélectionnés aléatoirement qui s'apparient avec le dernier n-gramme ajouté à la variable tweet. Elle fait cela pour au moins 150 caractères et, comme avant, effectue une vérification pour voir si elle se terminera sur un n-gramme alphanumérique. Si elle ne se termine pas sur un n-gramme alphanumérique, elle continuera à enchaîner à partir du modèle jusqu'à ce qu'elle le fasse.

Et enfin, le bot envoie une requête de publication avec les paroles comme charge utile du tweet.

Maintenant que nous avons une bonne idée de comment notre code fonctionne, exécutez la commande suivante :

```
npm install
```

dans le dossier du projet lyric-bot.

Cela installe les modules nécessaires.

### Configuration

Maintenant, vous allez vouloir copier un ensemble de paroles dans le fichier lyrics.txt.

Ensuite, créez un fichier .env. Cela stockera vos jetons d'API Twitter.

À l'intérieur du nouveau fichier, collez ce qui suit :

```
TWITTER_CONSUMER_KEY=
```

```
TWITTER_CONSUMER_SECRET=
```

```
TWITTER_ACCESS_TOKEN=
```

```
TWITTER_ACCESS_TOKEN_SECRET=
```

et copiez les jetons respectifs depuis la console de développement de votre application, une fois que votre demande de développeur est approuvée.

Il est temps de le tester !

Tapez

```
node bot.js
```

Et jetez un coup d'œil à la console !

![Image](https://cdn-media-1.freecodecamp.org/images/9n4D549XRgXATvMh5rHdoh6mz5KfSq4QSKS-)
_Échantillon de paroles créé à partir de Daylily par Movements_

Et consultez également le compte Twitter, bien sûr :

![Image](https://cdn-media-1.freecodecamp.org/images/QlJ4o4NGqHCfCdLnporB-IcYc80I5zce9ZSN)
_Le tweet envoyé par le bot à l'API Twitter_

### **ET VOILÀ !**

Vous avez maintenant un bot Twitter fonctionnel capable de publier de nouvelles paroles de chansons générées ! 🎉

Attendez cependant, nous devons encore l'automatiser...

### Déploiement Heroku

Rendez-vous sur [Heroku.com](http://heroku.com) et connectez-vous. Si vous n'avez pas de compte, vous pouvez en créer un gratuitement ! 😊

Maintenant, depuis le tableau de bord principal, créez une nouvelle application en cliquant sur Nouveau->Créer une nouvelle application.

Entrez un nom disponible, puis cliquez sur Créer une application.

Voici le panneau de contrôle principal de votre application !

Si vous faites défiler vers le bas dans l'onglet 'Deploy', vous verrez des instructions pour 'Deploy using Heroku Git'. Suivez les étapes ici, et une fois que vous avez déployé votre application avec succès, passez à l'étape suivante.

### Automatisation

Allez dans l'onglet 'Overview' et cliquez sur 'Configure Add-Ons'. Ensuite, dans la barre de recherche des add-ons, tapez 'Heroku Scheduler' et sélectionnez-le. Une boîte de dialogue s'affichera, cliquez sur 'Provision'.

Une fois ajouté, vous pouvez cliquer sur l'add-on et créer ce qu'on appelle des 'jobs'. Les jobs sont essentiellement des tâches qui sont exécutées par Heroku Scheduler.

Vous allez vouloir cliquer sur 'Add new job' et une fenêtre de configuration apparaîtra. Dans l'option de commande, tapez ce qui suit :

```
node bot.js
```

et sélectionnez la fréquence à laquelle vous voulez exécuter la commande. Une fois terminé, cliquez sur sauvegarder.

Et avec cela, vous avez déployé avec succès un bot Twitter de paroles ! 🎉

### Remerciements

La plupart du code pour créer le texte personnalisé est attribué à Daniel Shiffman. Vous pouvez trouver son matériel [ici](https://shiffman.net/a2z/markov/) !

Les données de paroles que j'ai utilisées dans cet article ont été échantillonnées à partir d'une chanson appelée Daylily par Movements.

Un grand merci à [Morgan Allgrove-Hodges](https://twitter.com/morgansah) pour avoir donné des commentaires et corrigé mes erreurs de grammaire stupides ! 😊

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/shawn-toubeau/) ou suivez-moi sur [Twitter](https://twitter.com/shawntoubeau) ! J'adore faire de nouvelles rencontres 😊

~ Shawn Toubeau