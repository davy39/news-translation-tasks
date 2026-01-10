---
title: Comment créer un bot Twitter à partir de zéro avec Golang
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T17:33:50.000Z'
originalURL: https://freecodecamp.org/news/creating-a-twitter-bot-from-scratch-with-golang-e1f37a66741
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W8H2r9xXvzAyI0U7PEqLOQ.png
tags:
- name: bots
  slug: bots
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un bot Twitter à partir de zéro avec Golang
seo_desc: 'By Kofo Okesola

  So a little background: I recently picked up Golang and decided to create a Twitter
  bot as a side project. Then came the problem. There is little to no documentation
  on using the Twitter API with Golang ?(particularly the oauth1 and C...'
---

Par Kofo Okesola

Un peu de contexte : j'ai récemment commencé à apprendre Golang et j'ai décidé de créer un [bot Twitter](https://twitter.com/_definethis) comme projet secondaire. Ensuite, le problème est survenu. Il y a peu ou pas de documentation sur l'utilisation de l'API Twitter avec Golang (particulièrement les parties de chiffrement oauth1 et CRC). Après quelques jours d'essais et d'erreurs et après l'avoir finalement terminé, je veux partager le processus. Espérons que cela aide quelqu'un.

### **Que allons-nous construire ?**

Nous allons créer un bot Twitter qui sera servi depuis notre machine locale. Il répondra à tout tweet qui est tagué avec un "hello world".

Voici une brève explication de ce que ce programme Go fera. Il va :

* Écouter et répondre à la validation [CRC du webhook](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/guides/securing-webhooks).
* Enregistrer une URL de webhook qui pointe vers lui.
* Écouter les tweets et répondre avec "hello world".

### De quoi avez-vous besoin ?

* Quelques connaissances de base de Golang
* Un compte développeur Twitter approuvé. [Comment postuler](https://developer.twitter.com/en/apply-for-access.html).
* Vous devez avoir un environnement de développement d'API d'activité de compte configuré — appelez-le `dev` pour ce projet
* Une [application Twitter](https://developer.twitter.com/en/apps) avec des clés de consommateur générées et des jetons d'accès (accès en lecture et écriture)
* Golang [installé](https://golang.org/doc/install) sur votre machine de développement.
* Un peu de détermination.

### Prêt ? C'est parti

D'abord, créez votre dossier de projet dans votre `$GOPATH/src/`. Nous allons appeler ce projet et notre dossier `hellobot`. Dans celui-ci, créez le fichier intro `/hellobot.go`.

La première chose que nous devons faire est de créer un endpoint pour que notre application écoute les vérifications CRC et réponde. Twitter résume bien les exigences pour la vérification.

![Image](https://cdn-media-1.freecodecamp.org/images/1*smwO5H254k6BLXfzciXgJA.png)

#### Configuration d'un serveur

La première chose que nous faisons est de charger le fichier `.env`. Pour cela, nous utilisons le plugin [godotenv](https://github.com/joho/godotenv). Le fichier .env est généralement dans ce format :

```
CONSUMER_KEY=CONSUMER_SECRET=ACCESS_TOKEN_KEY=ACCESS_TOKEN_SECRET=WEBHOOK_ENV=devAPP_URL=
```

> Note : Nous allons utiliser la commande `go get` de base pour installer toutes nos dépendances, compte tenu de la petite taille de notre projet

Ensuite, nous configurons notre serveur en utilisant [mux](https://github.com/gorilla/mux) comme gestionnaire, et nous écoutons la route de base et `webhook/twitter`. Si vous installez cela en utilisant `go install` et exécutez `hellobot`, lorsque vous l'exécutez et naviguez vers votre localhost:9090, vous devriez voir le message

![Image](https://cdn-media-1.freecodecamp.org/images/1*3OhpTAjdKTs8LV63wwA1ZQ.png)

#### Validation CRC

Maintenant pour le CRC, mettez à jour votre fonction `CrcCheck()` avec le code suivant :

Voici ce que nous faisons dans la fonction :

* Définir l'en-tête sur 'application/json'
* Obtenir le paramètre d'URL crc_token
* Le chiffrer en utilisant Hmac sha256 et l'encoder
* L'imprimer dans le response writer

Assurez-vous de remplacer `CONSUMER_SECRET` par la clé secrète de consommateur réelle de votre application. Maintenant, si vous naviguez vers `localhost:9090/webhook/twitter?crc_token=test`, vous devriez obtenir une réponse similaire à celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0d-9kjmYKyloZwqVlhifkg.png)

Maintenant que nous avons une route CRC fonctionnelle, il est temps d'enregistrer notre webhook. Quelques points à noter ici. Twitter n'acceptera pas les URL basées sur `localhost` ni une URL avec un numéro de port ou une URL non-https comme webhook. Une solution pendant le développement est d'utiliser un service comme [ngrok](https://ngrok.com/). Il suffit de l'[installer](https://ngrok.com/download) et de démarrer un serveur de développement pointant vers votre port 9090 :

```
ngrok http 9090 
```

Vous devriez voir une réponse similaire à celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wvDCZdXBVP6b2a07z9Yupw.png)

Maintenant, si vous allez sur l'URL <id>.ngrok.io, vous devriez voir la même réponse que localhost:9090. N'oubliez pas d'ajouter l'URL à votre fichier .env `APP_ENV`

#### Enregistrement du webhook

Pour ce tutoriel, nous allons vérifier la présence d'un flag `register` dans la liste des arguments. Vous pouvez ajouter ceci à votre code :

Ici, notre bot vérifie la présence de `-register` dans la liste des arguments. Ensuite, il exécute `registerWebhook()` comme une goroutine. Nous définissons la fonction `registerWebhook()` dans un fichier `client.go` que nous utiliserons pour toutes les requêtes Twitter. Maintenant, pour le corps de la fonction :

Donc, une décomposition du nouveau code. La première chose est de créer une fonction `CreateClient()`. Cette fonction retourne un pointeur vers un client OAuth `http.Client` que nous pouvons ensuite utiliser pour faire toutes les requêtes Twitter au nom du compte de notre bot. N'oubliez pas d'exécuter `go get` dans le dossier du projet afin qu'il puisse récupérer la [bibliothèque go pratique](https://github.com/dghubble/oauth1) que nous utilisons pour toutes les requêtes OAuth. Dans la fonction `registerWebhook`, nous :

* Récupérons un client
* Passons l'URL de notre webhook comme paramètre en utilisant `url.Values`
* Faisons une réponse post à l'[endpoint d'enregistrement du webhook](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/api-reference/aaa-premium#post-account-activity-all-env-name-webhooks) puis décompressons (décodons) et lisons la réponse

Ensuite, nous devons que notre code [abonne notre webhook à des événements](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/api-reference/aaa-premium#post-account-activity-all-env-name-subscriptions).

> Note : Vous pouvez utiliser l'application [account-activity-dashboard](https://github.com/twitterdev/account-activity-dashboard) créée par Twitter pour gérer les webhooks pendant le développement

Mettez à jour votre fichier `client.go` comme montré ci-dessous :

Le code ci-dessus est très simple. Vérifiez après l'enregistrement, abonnez-vous aux événements et vérifiez un code de statut de `204`. Maintenant, si vous exécutez `go install` sur votre code et exécutez le code comme `hellobot -register`, vous devriez obtenir la réponse suivante :

```
Starting ServerRegistering webhook...Webhook id of <hook_id> has been registeredSubscribing webapp...Subscribed successfully
```

#### Écoute des événements

Maintenant, nous devons que notre webhook écoute réellement les événements une fois que l'URL est appelée. Mettez à jour vos fichiers comme montré ci-dessous :

Ce que nous faisons dans `hellobot.dev` est d'écouter les requêtes post vers nos routes et de les passer à la fonction appropriée. Pendant ce temps, dans `client.go`, nous ajoutons les structures appropriées que nous utiliserons pour [analyser la charge utile JSON](https://www.sohamkamani.com/blog/2017/10/18/parsing-json-in-golang/) pour notre bot.

Maintenant, mettez à jour votre code pour qu'il envoie le tweet sur le tag.

Les mises à jour que nous avons ajoutées à nos fichiers sources sont simplement pour répondre aux événements de webhook. Vérifiez si c'était un [tweet_create_event](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/guides/account-activity-data-objects#tweet_create_events) et envoyez une réponse comme une réponse en utilisant la méthode `SendTweet()` dans notre fichier `client.go`.

> Note : Tout tweet envoyé comme réponse doit inclure le handle de l'utilisateur auquel il répond comme contenu initial de la réponse

Maintenant, si vous exécutez cela avec les identifiants appropriés, votre bot devrait répondre aux tags et répondre avec "Hello World".

### Conclusion

Maintenant que c'est fait, et puisque c'est une version extrêmement basique d'un bot, vous pouvez essayer d'ajouter quelques choses :

* Vérifier et ignorer les événements de retweet
* Ajouter un nom à la réponse
* Répondre au tweet en cas d'erreur quelque part sur l'application.

_Le code pour ce tutoriel est sur [Github ici](https://github.com/kofoworola/hellobot). N'hésitez pas à le fork et à jouer avec_

Santé !