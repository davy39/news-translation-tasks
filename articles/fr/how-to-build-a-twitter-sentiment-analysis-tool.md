---
title: Comment créer un outil d'analyse de sentiment Twitter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T23:52:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-twitter-sentiment-analysis-tool
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b3f740569d1a4ca2aa8.jpg
tags:
- name: nlp
  slug: nlp
- name: Node.js
  slug: nodejs
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: Comment créer un outil d'analyse de sentiment Twitter
seo_desc: 'By Dirk Hoekstra

  This weekend I had some time on my hands and decided to build a Twitter sentiment
  analysis tool.

  The idea is that you enter a search term and the tool will search recent tweets.
  It will then use sentiment analysis to determine how po...'
---

Par Dirk Hoekstra

Ce week-end, j'avais un peu de temps devant moi et j'ai décidé de créer un outil d'analyse de sentiment Twitter.

L'idée est que vous saisissiez un terme de recherche et que l'outil recherche les tweets récents. Il utilisera ensuite l'analyse de sentiment pour déterminer si Twitter est positif ou négatif à propos du sujet.

Par exemple, vous pourriez rechercher « Donald Trump » pour obtenir le sentiment de Twitter sur le président.

Plongeons dans le vif du sujet !

## Obtenir une clé API Twitter

La toute première chose à faire est de créer une application Twitter afin d'obtenir une clé API. 

Rendez-vous sur la [page des applications Twitter](https://developer.twitter.com/en/apps) pour créer une nouvelle application. Vous devez avoir un compte développeur pour pouvoir créer une application.

Si vous n'avez pas de compte développeur, vous pouvez en demander un. La plupart des demandes sont acceptées instantanément. ?

Copiez la `API Key` et le `API Key Secret` que vous trouverez dans votre application Twitter.

## Créer un projet NodeJS

Je vais utiliser NodeJS pour créer cette application. 

Pour créer un nouveau projet, j'exécute :

```
npm init
npm install twitter-lite
```

Cela créera un nouveau projet NodeJS et installera le package `twitter-lite`. Ce package rend l'interaction avec l'API Twitter super facile.

Pour authentifier nos requêtes, nous allons utiliser un jeton porteur (bearer token) OAuth2.0. Le package `twitter-lite` offre un moyen simple de gérer l'authentification Twitter.

Créons un nouveau fichier `index.js` et ajoutons-y le code suivant :

```javascript
const Twitter = require('twitter-lite');

const user = new Twitter({
    consumer_key: "YOUR_API_KEY",
    consumer_secret: "YOUR_API_SECRET",
});

// Envelopper le code suivant dans une fonction asynchrone appelée
// immédiatement afin de pouvoir utiliser des instructions « await ».
(async function() {
    try {
        // Récupérer le jeton porteur de Twitter.
        const response = await user.getBearerToken();
        console.log(`Got the following Bearer token from Twitter: ${response.access_token}`);
        
        // Construire notre client API avec le jeton porteur.
        const app = new Twitter({
            bearer_token: response.access_token,
        });
    } catch(e) {
        console.log("There was an error calling the Twitter API.");
        console.dir(e);
    }
})();
```

Lors de l'exécution, la console affiche ce qui suit :

```
Got the following Bearer token from Twitter: THE_TWITTER_BEARER_TOKEN
```

Génial, pour l'instant tout fonctionne. ?

## Obtenir les tweets récents

La partie suivante consiste à récupérer les tweets récents de l'API Twitter.

Sur la [documentation Twitter](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets), vous pouvez voir qu'il existe un point de terminaison (endpoint) pour rechercher des tweets récents. 

Pour implémenter cela, j'ajoute le code suivant au fichier `index.js` :

```javascript
const Twitter = require('twitter-lite');

(async function() {
    const user = new Twitter({
        consumer_key: "YOUR_API_KEY",
        consumer_secret: "YOUR_API_SECRET",
    });

    try {
        let response = await user.getBearerToken();
        const app = new Twitter({
            bearer_token: response.access_token,
        });

        // Rechercher des tweets récents via l'API Twitter
        response = await app.get(`/search/tweets`, {
            q: "Lionel Messi", // Le terme de recherche
            lang: "en",        // Ne récupérons que les tweets en anglais
            count: 100,        // Limiter les résultats à 100 tweets
        });

        // Parcourir tous les tweets et afficher le texte
        for (tweet of response.statuses) {
            console.dir(tweet.text);
        }
    } catch(e) {
        console.log("There was an error calling the Twitter API");
        console.dir(e);
    }
})();
```

En exécutant cela, vous pouvez voir beaucoup de commentaires Twitter sur Lionel Messi, ce qui signifie que cela fonctionne parfaitement ! ⚽

```
"RT @TheFutbolPage: Some of Lionel Messi's best dribbles."

"RT @MagufuliMugabe: Lionel Messi ? didn't just wake up one day  and become the best player in the world no  HE trained. So if your girl is…"

""RT @goal: The boy who would be King ? Is Ansu Fati the heir to Lionel Messi's throne?"

and many more... 
```

## Effectuer une analyse de sentiment

Pour effectuer l'analyse de sentiment, je vais utiliser l'API Natural Language de Google Cloud. Avec cette API, vous pouvez obtenir le score de sentiment d'un texte avec un simple appel API.

Tout d'abord, rendez-vous sur la [Google Cloud Console](https://console.cloud.google.com/) pour créer un nouveau projet cloud.

Ensuite, rendez-vous sur l' [API Natural Language](https://console.cloud.google.com/apis/api/language.googleapis.com) et activez-la pour le projet.

Enfin, nous devons créer un compte de service pour nous authentifier. Rendez-vous sur la [page de création de compte de service](https://console.cloud.google.com/apis/credentials/serviceaccountkey) pour créer un compte de service. 

Lors de la création d'un compte de service, vous devrez télécharger le fichier `json` contenant la clé privée de ce compte de service. Enregistrez ce fichier dans le dossier du projet.

Google propose un package NodeJS pour interagir avec l'API Natural Language, utilisons-le donc. Pour l'installer, exécutez :

```
npm install @google-cloud/language
```

Pour que le package de langue fonctionne, il doit savoir où se trouve le fichier de clé privée. 

Le package tentera de lire une variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` qui doit pointer vers ce fichier.

Pour définir cette variable d'environnement, je mets à jour la clé `script` dans le fichier `package.json`.

```json
"scripts": {
  "start": "GOOGLE_APPLICATION_CREDENTIALS='./gcloud-private-key.json' node index.js"
}
```

_Notez que pour que cela fonctionne, vous devez lancer le script en exécutant `npm run start`._

Une fois tout cela configuré, nous pouvons enfin commencer à coder.

J'ajoute une nouvelle fonction `getSentiment` au fichier `index.js` :

```javascript
const language = require('@google-cloud/language');
const languageClient = new language.LanguageServiceClient();

async function getSentiment(text) {
    const document = {
        content: text,
        type: 'PLAIN_TEXT',
    };

    // Détecte le sentiment du texte
    const [result] = await languageClient.analyzeSentiment({document: document});
    const sentiment = result.documentSentiment;

    return sentiment.score;
}
```

Cette fonction appelle l'API Google Natural Language et renvoie un score de sentiment compris entre -1 et 1.

Testons cela avec quelques exemples :

```javascript
getSentiment("I HATE MESSI");
```

Renvoie ce qui suit.

```
The sentiment score is -0.40
```

De même :

```javascript
getSentiment("I LOVE MESSI");
```

Renvoie un sentiment plus élevé. ?

```
The sentiment score is 0.89
```

## Assembler le tout

La dernière chose à faire est d'appeler la fonction `getSentiment` avec le texte des tweets.

Il y a cependant un bémol : seuls les 5 000 premiers appels API sont gratuits, après quoi Google vous facturera les appels suivants. 

Pour minimiser le nombre d'appels API, je vais combiner tous les tweets en une seule chaîne de caractères comme ceci :

```javascript
let allTweets = "";
for (tweet of response.statuses) {
	allTweets += tweet.text + "\n";
}

const sentimentScore = await getSentimentScore(allTweets);
console.log(`The sentiment about ${query} is: ${sentimentScore}`);
```

Désormais, je n'ai plus qu'à appeler l'API une seule fois au lieu de 100 fois.

La question finale est bien sûr : que pense Twitter de Lionel Messi ? Lors de l'exécution du programme, il donne le résultat suivant :

```
The sentiment about Lionel Messi is: 0.2
```

Ainsi, Twitter est légèrement positif à l'égard de Lionel Messi.

## Conclusion

Nous avons créé un programme NodeJS qui interagit avec l'API Twitter pour obtenir des tweets récents. Il envoie ensuite ces tweets à l'API Google Cloud Natural Language pour effectuer une analyse de sentiment.

Vous pouvez trouver une version en direct de cette [analyse de sentiment ici](https://coffeecoding.dev/twitter-sentiment-analysis).

Vous pouvez également consulter le code complet [ici sur GitHub](https://github.com/Dirk94/twitter-sentiment-analysis).