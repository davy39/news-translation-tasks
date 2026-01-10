---
title: Comment créer un SlackBot avec Node.js et SlackBots.js
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-08-12T14:01:46.000Z'
originalURL: https://freecodecamp.org/news/building-a-slackbot-with-node-js-and-slackbots-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/article-banner--4-.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: api
  slug: api
- name: bots
  slug: bots
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: slack
  slug: slack
seo_title: Comment créer un SlackBot avec Node.js et SlackBots.js
seo_desc: 'Slack is an American cloud-based set of proprietary team collaboration
  software tools and online services, developed by Slack Technologies. Slack is a
  workspace where teams can communicate and collaborate.

  Teamwork in Slack happens in channels — a si...'
---

Slack est un ensemble d'outils logiciels de collaboration d'équipe propriétaires basés sur le cloud et de services en ligne, développé par Slack Technologies. Slack est un espace de travail où les équipes peuvent communiquer et collaborer.

Le travail d'équipe dans Slack se fait dans des canaux - un seul endroit pour les messages, les outils et les fichiers - aidant tout le monde à gagner du temps et à collaborer.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/organize-conversations-slack-product-desktop.png align="left")

---

L'une des fonctionnalités géniales de Slack est [Slack Apps](https://slack.com/apps), les intégrations et [Slack Bots](https://api.slack.com/bot-users).

Un bot Slack est un type d'application Slack conçu pour interagir avec les utilisateurs via la conversation. Votre bot peut envoyer des DM, il peut être mentionné par les utilisateurs, il peut poster des messages ou télécharger des fichiers, et il peut être invité dans des canaux. Cool, non ?

Si vous utilisez déjà Slack, vous devriez être familier avec certains bots Slack créatifs comme [Standupbot](https://standupbot.com/), [Birthdaybot](https://birthdaybot.io/) et plus encore.

Dans cet article, je vais vous guider à travers la création de votre premier bot Slack de A à Z avec [Node.js](http://nodejs.org/) et [SlackBots.js](https://github.com/mishk0/slack-bot-api)

> PS : Cet article a été publié [sur mon blog en premier](https://www.bolajiayodeji.com/building-a-slackbot-with-node-js-and-slackbots-js/).

# Description du SlackBot

Nous allons créer un SlackBot simple qui affiche des citations technologiques inspirantes aléatoires et des blagues pour les développeurs/designers.

J'ai créé une [extension chrome](https://github.com/BolajiAyodeji/inspireNuggets) qui affiche des citations technologiques inspirantes aléatoires pour les développeurs/designers sur votre nouvel onglet (vous pouvez la télécharger [ici](https://chrome.google.com/webstore/detail/inspirenuggets-for-chrome/acnfgdioohhajabdofaadfdhmlkphmlb)). Nous allons utiliser le JSON des citations de cette extension comme notre API de citations et l'[API de blagues Chuck Norris](https://api.chucknorris.io/) pour les blagues.

Lorsque l'utilisateur mentionne notre bot et ajoute **inspire me**, le bot retourne une citation aléatoire de [inspireNuggets](https://chrome.google.com/webstore/detail/inspirenuggets-for-chrome/acnfgdioohhajabdofaadfdhmlkphmlb). Lorsque l'utilisateur tape **random joke**, il retourne une blague aléatoire de l'[API Chuck Norris](https://api.chucknorris.io/). Et lorsque l'utilisateur tape help, il retourne le guide d'instructions.

> @inspirenuggets inspire me
> 
> @inspirenuggets random joke
> 
> @inspirenuggets help

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture2.png align="left")

Cet article ne traite pas vraiment de ce que nous allons construire - il s'agit simplement de vous montrer le concept derrière les bots Slack et comment en construire un. Après l'avoir lu, vous pouvez penser à autre chose et construire un bot différent, car il y a de nombreuses possibilités.

Vous pouvez cloner ou forker le projet final [ici](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot).

Assez intéressant, non ? Commençons.

# Prérequis

Nous allons construire ce bot avec Node.js et SlackBots.js. Vous n'avez pas besoin de savoir comment écrire en Node.js, car je vais vous guider à travers. Cependant, le connaître est un avantage. Vous devriez également avoir :

* Des connaissances de base en JavaScript

* ES6 JavaScript

* Un espace de travail Slack

* Une certaine expérience avec Slack

* Certaines compétences en contrôle de version

# Configuration de l'environnement

Commençons par configurer et installer Node.js et Npm.

* Téléchargez Node [ici](https://nodejs.org/en/). Si vous l'avez déjà installé, passez cette étape. Si vous préférez utiliser un gestionnaire de paquets pour l'installer, lisez [ceci](https://nodejs.org/en/download/package-manager/#windows) pour tous les systèmes d'exploitation.

* Vérifiez si vous avez Node installé

```python
node -v
```

* Node.js vient avec Npm, donc vous n'avez pas à l'installer à nouveau.

```python
npm -v
```

Maintenant que nous avons Node.js configuré, initialisons notre projet.

Créez votre répertoire de projet (j'ai appelé le mien Slackbot) et initialisez git :

```python
git init
```

Ensuite, créez un fichier `index.js` :

```python
touch index.js
```

Et initialisez Npm :

```python
npm init
```

Répondez simplement à toutes les questions qui suivent. Si vous avez des problèmes, voici mon propre `package.json` :

```json
{
  "name": "slackbot",
  "version": "1.0.0",
  "description": "Un simple Slackbot qui affiche des citations technologiques inspirantes aléatoires pour les développeurs/designers.",
  "main": "index.js",
  "scripts": {
    "start": "index.js"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/BolajiAyodeji/slackbot.git"
  },
  "author": "Bolaji Ayodeji",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/BolajiAyodeji/slackbot/issues"
  },
  "homepage": "https://github.com/BolajiAyodeji/slackbot#readme"
}
```

# Installation des dépendances

**Maintenant, installons et configurons toutes les bibliothèques dont nous avons besoin.**

## SlackBots.js

[SlackBots.js](https://github.com/mishk0/slack-bot-api) est une bibliothèque Node.js pour une opération facile avec l'API Slack.

```python
npm install slackbots
```

Dans `index.js` :

```python
const SlackBot = require('slackbots');
```

## Axios

[Axios](https://github.com/axios/axios) est un client HTTP basé sur les promesses pour le navigateur et node.js. Si vous connaissez Fetch ou AJAX, ce n'est qu'une bibliothèque qui fait la même chose avec des fonctionnalités bien plus cool. Vous pouvez les voir [ici](https://github.com/axios/axios).

```python
npm install axios
```

Dans `index.js` :

```python
const axios = require('axios')
```

## Nodemon

Pour exécuter un script en Node.js, vous devez exécuter `node index.js`. Chaque fois que vous apportez des modifications à ce fichier, vous devez relancer `node index.js`. Cela devient fastidieux lorsque vous faites autant de changements comme nous allons le faire. C'est pourquoi nous avons besoin de [nodemon](https://github.com/remy/nodemon), un outil qui aide à développer des applications basées sur node.js en redémarrant automatiquement l'application node lorsque des changements de fichiers dans le répertoire sont détectés.

```python
npm install -g nodemon
```

Dans `package.json`, localisez la section scripts et ajoutez un nouveau script de démarrage :

```python
"scripts": {
    "start": "node index.js"
  }
```

Si vous exécutez `npm start`, le fichier s'exécutera mais ne redémarrera pas en cas de changement. Pour corriger cela, utilisez nodemon que nous avons installé au lieu de node comme ceci :

```python
"scripts": {
    "start": "nodemon index.js"
  }
```

# Dotenv

Je ne vais pas expliquer cela en profondeur. Dans quelques jours, je publierai un article sur les variables environnementales, mais pour l'instant, sachez simplement que nous utilisons cela pour cacher les clés secrètes et les jetons comme le jeton d'accès Slack que nous allons utiliser. De cette façon, vous n'avez pas à pousser vos clés secrètes sur GitHub.

Il existe plusieurs façons de faire cela, mais je préfère utiliser dotenv. [Dotenv](https://github.com/motdotla/dotenv) est un module sans dépendance qui charge les variables environnementales d'un fichier .env dans process.env.

```python
npm install dotenv
```

Dans `index.js` :

```python
const dotenv = require('dotenv')

dotenv.config()
```

Après toutes les installations, votre `package.json` devrait ressembler à ceci :

```json
{
  "name": "inspireNuggetsSlackBot",
  "version": "1.0.0",
  "description": "Un simple Slackbot qui affiche des citations technologiques inspirantes aléatoires et des blagues pour les développeurs/designers.",
  "main": "index.js",
  "scripts": {
    "start": "nodemon index.js"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/BolajiAyodeji/inspireNuggetsSlackBot.git"
  },
  "author": "Bolaji Ayodeji",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/BolajiAyodeji/inspireNuggetsSlackBot/issues"
  },
  "homepage": "https://github.com/BolajiAyodeji/inspireNuggetsSlackBot#readme",
  "devDependencies": {
    "dotenv": "^8.0.0"
  },
  "dependencies": {
    "axios": "^0.19.0",
    "slackbots": "^1.2.0"
  }
}
```

# Créez votre espace de travail Slack

Maintenant que nous avons tout configuré, nous avons besoin d'un espace de travail Slack pour exécuter notre bot en développement. Créer un espace de travail est assez facile, lisez [ceci](https://get.slack.help/hc/en-us/articles/206845317-Create-a-Slack-workspace) pour en savoir plus.

# Enregistrez votre Slack Bot

Maintenant que vous avez un espace de travail, vous devriez avoir une URL Slack avec le nom de votre espace de travail. La mienne est `mekafindteam.slack.com`.

Maintenant, vous devrez créer une application Slack. Créez-en une [ici](https://api.slack.com/apps/new).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture5.png align="left")

Entrez le nom de votre application et assurez-vous d'être dans l'espace de travail que vous avez créé si vous êtes dans plusieurs espaces de travail.

Maintenant, vous verrez la page des paramètres > Informations de base. Cliquez sur le premier onglet `Ajouter des fonctionnalités et des fonctionnalités` :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture6.png align="left")

Puisque nous construisons un bot, sélectionnez le champ **Bots**.

Maintenant, vous verrez la page de l'utilisateur Bot :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture7.png align="left")

Cliquez sur le bouton `Ajouter un utilisateur Bot`.

Votre nom d'affichage sera automatiquement rempli à partir du nom de l'application que vous avez déjà choisi. Vous pouvez le mettre à jour, mais je vous conseille d'utiliser le même nom partout avec la même casse d'alphabet pour éviter les erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture8.png align="left")

Maintenant, activez le bouton `Toujours montrer mon bot comme en ligne` pour toujours montrer votre bot comme en ligne. N'oubliez pas que ce bot est comme un utilisateur dans votre espace de travail. Ensuite, cliquez sur le bouton `Ajouter un utilisateur Bot`.

Enregistrez toutes les modifications maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture9.png align="left")

Ensuite, retournez à la page `Informations de base` et sélectionnez l'onglet `Installer votre application dans votre espace de travail`.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture10.png align="left")

Cliquez sur `Installer l'application dans l'espace de travail` :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture11.png align="left")

Cliquez sur autoriser et attendez d'être redirigé vers la page `Informations de base`.

Notez l'onglet `Gérer la distribution` : cette section est nécessaire lorsque vous souhaitez rendre votre bot disponible pour l'installation par d'autres. Pour l'instant, nous construisons en développement et je ne couvrirai pas la distribution dans cet article. Dans mon prochain article, je vous montrerai comment déployer votre bot Slack et le rendre disponible en tant qu'application pour d'autres espaces de travail.

Si vous vérifiez votre espace de travail Slack maintenant, vous devriez voir l'application installée dans la section Applications.

Pour l'instant, il est hors ligne - une fois que nous commencerons à construire le bot, nous l'activerons.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture15.png align="left")

# Personnalisez votre bot Slack

Maintenant que nous avons créé notre bot, faisons quelques personnalisations.

Toujours sur la page `Informations de base`, faites défiler jusqu'à la section `Informations d'affichage` :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture12.png align="left")

C'est du basique : téléchargez simplement un logo, changez votre couleur de fond et ajoutez une courte description.

Votre icône doit être de `512x512px` ou plus grande et votre couleur de fond doit être en HEX. Lisez plus sur les directives de l'application [ici](https://api.slack.com/docs/slack-apps-guidelines).

Voici à quoi ressemble le mien après personnalisation :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture13.png align="left")

# Jetons OAuth du bot Slack

Maintenant que nous avons configuré notre bot Slack, récupérons nos clés de jeton.

Dans la barre de navigation, localisez la section Fonctionnalités et cliquez sur l'onglet `OAuth & Permission` :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture16.png align="left")

Vous verrez deux jetons d'accès :

* Jetons d'accès OAuth

* Jetons d'accès OAuth de l'utilisateur Bot

Copiez le **jeton d'accès OAuth de l'utilisateur Bot**.

Cela changera chaque fois que vous réinstallerez cette application ou lorsque vous l'installerez dans un autre espace de travail. Le jeton doit commencer par `xoxb-`.

> Garder les informations d'identification sécurisées est important que vous développiez des bibliothèques et des outils open source, des intégrations internes pour votre espace de travail, ou des applications Slack pour la distribution dans des espaces de travail à travers le monde. - Slack

C'est pourquoi nous avons installé Dotenv - nous allons le configurer dans la section suivante.

# Construction du bot

Maintenant, construisons notre bot :).

### Tout d'abord, gardons notre jeton d'accès quelque part.

Créez un fichier `.env` et ajoutez ceci :

```python
BOT_TOKEN=VOTRE_JETON_D_ACCES_SLACK_ICI
```

Maintenant, commençons notre SlackBot.js :

```javascript
const bot = new SlackBot({
    token: `${process.env.BOT_TOKEN}`,
    name: 'inspirenuggets'
})
```

Nous venons de créer une variable bot qui initialise une nouvelle instance SlackBot qui a deux valeurs, notre jeton et le nom de l'application.

J'ai utilisé la [syntaxe de chaîne de modèle ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) pour importer notre clé de jeton depuis notre fichier `.env`. dotenv s'en occupe pour nous.

Assurez-vous d'utiliser le même nom que vous avez utilisé lors de la création de votre application Slack, sinon vous aurez des erreurs d'authentification.

Maintenant, démarrez l'application :

```python
npm start
```

nodemon devrait être en cours d'exécution maintenant et notre application Slack devrait également être en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture17.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture18.png align="left")

### Gestionnaire de démarrage

Notre bot ne fait rien maintenant même s'il est en cours d'exécution. Retournez un message.

```javascript
bot.on('start', () => {
    const params = {
        icon_emoji: ':robot_face:'
    }

    bot.postMessageToChannel(
        'random',
        'Get inspired while working with @inspirenuggets',
        params
    );
})
```

Le gestionnaire `bot.on` envoie le message de bienvenue. Nous avons passé deux paramètres, le `'start'` et une fonction qui contient une variable params qui contient également l'emoji slack. Les emojis Slack ont des codes, et vous pouvez les trouver [ici](https://slackmojis.com/). J'ai utilisé `:robot_face:`, mais vous pouvez le changer pour l'emoji de votre choix.

Nous avons également initialisé la fonction `bot.postMessageToChannel` qui est une méthode SlackBot.js pour poster un message dans un canal. Dans cette fonction, nous passons le nom du canal dans lequel nous voulons poster, le message sous forme de chaîne, et la variable params que nous avons déclarée précédemment pour l'emoji. J'ai utilisé le canal **#random** et j'y ai envoyé `Get inspired while working with @inspirenuggets`. Votre application devrait redémarrer automatiquement et votre bot devrait faire ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture19.png align="left")

Cool, non ?  
Vous pouvez également poster des messages aux utilisateurs et aux groupes.

```javascript
    // définissez le nom d'utilisateur existant au lieu de 'user_name'
    bot.postMessageToUser('user_name', 'Hello world!', params); 
   
    
    // définissez le groupe privé au lieu de 'private_group', où le bot existe
    bot.postMessageToGroup('private_group', 'Hello world!', params);
```

### Gestionnaire d'erreurs

Écrivons également une fonction pour vérifier les erreurs et les retourner :

```javascript
bot.on('error', (err) => {
    console.log(err);
})
```

### Gestionnaire de messages

Maintenant, construisons la fonctionnalité principale du bot.

Comme je l'ai dit plus tôt, nous allons utiliser le JSON des citations de l'extension que j'ai construite comme notre API de citations. Le JSON peut être trouvé avec cette URL : `https://raw.githubusercontent.com/BolajiAyodeji/inspireNuggets/master/src/quotes.json`

Lorsque l'utilisateur mentionne notre bot et ajoute **inspire me**, le bot retourne une citation aléatoire de [inspireNuggets](https://chrome.google.com/webstore/detail/inspirenuggets-for-chrome/acnfgdioohhajabdofaadfdhmlkphmlb). Lorsque l'utilisateur tape **random joke**, il retourne une blague aléatoire de l'[API Chuck Norris](https://api.chucknorris.io/). Et lorsque l'utilisateur tape **help**, il retourne le guide d'instructions.

Tout d'abord, vérifions nos mots de commande à partir du message de l'utilisateur (**inspire me**, **random joke,** et **help**) :

```javascript
function handleMessage(message) {
    if(message.includes(' inspire me')) {
        inspireMe()
    } else if(message.includes(' random joke')) {
        randomJoke()
    } else if(message.includes(' help')) {
        runHelp()
    }
}
```

Maintenant, créons les trois fonctions dont nous avons besoin

**inspireMe()**

Notre JSON de démonstration n'est pas vraiment une API, c'est juste un JSON que j'ai utilisé dans l'extension Chrome. Nous y accédons simplement à partir du contenu brut de GitHub. Vous pouvez utiliser n'importe quelle API que vous préférez, vous devrez simplement itérer différemment pour obtenir vos données selon que votre API retourne un tableau ou un objet - peu importe ce qu'elle retourne, ce n'est pas un gros problème.

Consultez mes articles précédents sur :

* [Manipulation de tableaux en JavaScript](https://www.bolajiayodeji.com/manipulating-arrays-in-javascript/) et

* [Itération à travers les objets JavaScript - 5 techniques et tests de performance.](https://www.bolajiayodeji.com/iterating-through-javascript-objects-5-techniques-and-performance-tests/)

```javascript
function inspireMe() {
    axios.get('https://raw.githubusercontent.com/BolajiAyodeji/inspireNuggets/master/src/quotes.json')
      .then(res => {
            const quotes = res.data;
            const random = Math.floor(Math.random() * quotes.length);
            const quote = quotes[random].quote
            const author = quotes[random].author

            const params = {
                icon_emoji: ':male-technologist:'
            }
        
            bot.postMessageToChannel(
                'random',
                `:zap: ${quote} - *${author}*`,
                params
            );

      })
}
```

Nous venons d'utiliser Axios pour obtenir le fichier JSON qui retourne certaines données :

```json
[
    {
        "number": "1",
        "author": "Von R. Glitschka",
        "quote": "The client may be king, but he's not the art director."
    },
    {
        "number": "2",
        "author": "Frank Capra",
        "quote": "A hunch is creativity trying to tell you something."
    },
.
.
.
.
]
```

Ce JSON contient actuellement 210 citations et je les mets à jour fréquemment. Nous voulons donc obtenir une citation aléatoire plus le nom de l'auteur chaque fois que l'utilisateur la demande. À partir de notre réponse Axios, nous faisons simplement ceci :

```javascript

const quotes = res.data;
const random = Math.floor(Math.random() * quotes.length);
const quote = quotes[random].quote
const author = quotes[random].author
```

Et comme nous l'avons fait avec le message de bienvenue, nous retournons simplement la citation et l'auteur au lieu d'un message en chaîne :

```javascript
`:zap: ${quote} - *${author}*`
```

Testons cela :

Tapez `@inspirenuggets inspire me`

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture20.png align="left")

Hourra ! Cela a fonctionné !

PS : Vous pouvez toujours changer le type d'emoji pour chaque demande. Si vous avez remarqué, j'ai changé `inspireMe()` en `:male-technologist:`

**randomJoke()**

Nous obtenons les blagues de l'API Chuck Norris à partir de ce point de terminaison `https://api.chucknorris.io/jokes/random`.

```json
{
"categories": [],
"created_at": "2016-05-01 10:51:41.584544",
"icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
"id": "6vUvusBeSVqdsU9C5-ZJZw",
"updated_at": "2016-05-01 10:51:41.584544",
"url": "https://api.chucknorris.io/jokes/6vUvusBeSVqdsU9C5-ZJZw",
"value": "Chuck Norris once choked a wildcat to death with his sphincter muscle."
}
```

Il s'agit d'une véritable API qui retourne une blague aléatoire à chaque demande, nous n'avons donc pas à faire `Math.floor()` à nouveau.

```javascript
function randomJoke() {
    axios.get('https://api.chucknorris.io/jokes/random')
      .then(res => {
            const joke = res.data.value;

            const params = {
                icon_emoji: ':smile:'
            }
        
            bot.postMessageToChannel(
                'random',
                `:zap: ${joke}`,
                params
            );

      })
}
```

À ce stade, vous devriez déjà comprendre comment cela fonctionne. Faites un post avec le nom du canal, le message et les paramètres.

**runHelp()**

Cela est similaire à notre message de bienvenue : nous voulons simplement retourner un texte personnalisé lorsque l'utilisateur ajoute **help** à la demande.

```javascript
function runHelp() {
    const params = {
        icon_emoji: ':question:'
    }

    bot.postMessageToChannel(
        'random',
        `Type *@inspirenuggets* with *inspire me* to get an inspiring techie quote, *random joke* to get a Chuck Norris random joke and *help* to get this instruction again`,
        params
    );
}
```

Maintenant, testons les trois commandes :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/capture2-1.png align="left")

Tout fonctionne bien maintenant, félicitations !!!! Vous venez de construire votre SlackBot.

---

Il existe un nombre infini de possibilités de bots que vous pouvez construire avec cela pour automatiser votre propre travail ou travail d'équipe.

Vous pouvez construire un bot qui :

* Récupère vos tâches de quelque part et vous rappelle lorsque vous tapez `hey what next`,

* Accueille chaque utilisateur dans votre espace de travail (je l'ai construit pendant l'un des [stages HNG](https://hng.tech/)),

* Vous donne des mises à jour de matchs de football pendant que vous travaillez,

* Dit à votre équipe lorsque vous atteignez une étape dans le nombre d'utilisateurs inscrits,

et bien plus encore...

Il s'agit simplement d'avoir un endroit pour obtenir les données, et quelques compétences de base en itération et la méthode `bot.postMessageToChannel()`.

L'automatisation est une chose que nous devrions apprendre en tant que développeurs. Nous avons beaucoup à faire, donc nous devrions automatiser les tâches plus simples afin d'avoir du temps pour les plus difficiles. J'espère qu'avec cela, vous pourrez automatiser vos tâches et j'ai hâte de voir les idées créatives que vous allez concrétiser.

---

# Code final

Voici notre `index.js` final

```javascript
const SlackBot = require('slackbots');
const axios = require('axios')
const dotenv = require('dotenv')

dotenv.config()

const bot = new SlackBot({
    token: `${process.env.BOT_TOKEN}`,
    name: 'inspirenuggets'
})

// Gestionnaire de démarrage
bot.on('start', () => {
    const params = {
        icon_emoji: ':robot_face:'
    }

    bot.postMessageToChannel(
        'random',
        'Get inspired while working with @inspirenuggets',
        params
    );
})

// Gestionnaire d'erreurs
bot.on('error', (err) => {
    console.log(err);
})

// Gestionnaire de messages
bot.on('message', (data) => {
    if(data.type !== 'message') {
        return;
    }
    handleMessage(data.text);
})

// Gestionnaire de réponses
function handleMessage(message) {
    if(message.includes(' inspire me')) {
        inspireMe()
    } else if(message.includes(' random joke')) {
        randomJoke()
    } else if(message.includes(' help')) {
        runHelp()
    }
}

// inspire Me
function inspireMe() {
    axios.get('https://raw.githubusercontent.com/BolajiAyodeji/inspireNuggets/master/src/quotes.json')
      .then(res => {
            const quotes = res.data;
            const random = Math.floor(Math.random() * quotes.length);
            const quote = quotes[random].quote
            const author = quotes[random].author

            const params = {
                icon_emoji: ':male-technologist:'
            }
        
            bot.postMessageToChannel(
                'random',
                `:zap: ${quote} - *${author}*`,
                params
            );

      })
}

// Blague aléatoire
function randomJoke() {
    axios.get('https://api.chucknorris.io/jokes/random')
      .then(res => {
            const joke = res.data.value;

            const params = {
                icon_emoji: ':smile:'
            }
        
            bot.postMessageToChannel(
                'random',
                `:zap: ${joke}`,
                params
            );

      })
}

// Afficher l'aide
function runHelp() {
    const params = {
        icon_emoji: ':question:'
    }

    bot.postMessageToChannel(
        'random',
        `Type *@inspirenuggets* with *inspire me* to get an inspiring techie quote, *random joke* to get a Chuck Norris random joke and *help* to get this instruction again`,
        params
    );
}
```

# Et ensuite ?

Notre bot ne fonctionne que dans l'environnement de développement pour l'instant, et pour l'utiliser, nous devons toujours exécuter `npm start`.

Ce n'est pas cool, n'est-ce pas ? Nous voudrions l'héberger quelque part où il peut fonctionner en permanence. Dans mon prochain article, je vous montrerai comment héberger cela sur [Heroku](https://herokuapp.com/), [Zeit](https://zeit.co/) ou [Netlify](https://netlify.com) et le publier sur le magasin d'applications Slack afin que n'importe qui dans le monde puisse l'utiliser.  
N'oubliez pas non plus d'ajouter ceci dans votre `.gitignore` avant de pousser sur GitHub :

```python

/.env
/node_modules
```

> **Abonnez-vous à ma** [**newsletter**](https://tinyletter.com/bolajiayodeji/) **pour rester informé.**

# Ressources utiles

* [API Slack](https://api.slack.com/)

* [Documentation de l'API Slack](https://api.slack.com/#read_the_docs)

* [SlackBot.js](https://github.com/slackapi/node-slack-sdk)

* [Applications Slack](https://slack.com/intl/en-in/apps)

* [Directives des applications Slack](https://api.slack.com/docs/slack-apps-guidelines)

* [Une introduction aux applications Slack](https://api.slack.com/start/overview)

* [inspireNuggets](https://github.com/BolajiAyodeji/inspireNuggets)

* [inspireNuggetsSlackBot](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot)