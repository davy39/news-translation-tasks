---
title: Comment créer votre propre bot Twitter de messages directs automatiques gratuitement
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-04T17:28:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-own-auto-direct-message-twitter-bot-for-free-e851265ce730
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yAlQxm27HPR2qjRcqizY2w.png
tags:
- name: bots
  slug: bots
- name: Node.js
  slug: nodejs
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer votre propre bot Twitter de messages directs automatiques
  gratuitement ?
seo_desc: 'By Youssouf El Azizi

  Creating a welcome message for your new followers in Twitter is the first step to
  getting more people to engage with your tweets and links. As you might know, there
  are many online services that help you send auto direct messages...'
---

Par Youssouf El Azizi

Créer un message de bienvenue pour vos nouveaux abonnés sur Twitter est la première étape pour inciter davantage de personnes à interagir avec vos tweets et vos liens. Comme vous le savez peut-être, il existe de nombreux services en ligne qui vous aident à envoyer des messages directs automatiques (DM) à vos nouveaux abonnés. Mais je trouve fou que les services en ligne facturent entre 5 et 15 dollars pour un simple outil de création de bots, alors que vous pouvez en construire un vous-même gratuitement.

Dans cet article, je vais vous présenter mon propre bot Twitter que j'ai développé pour envoyer un message de bienvenue à mes nouveaux abonnés sur Twitter. Je vous montrerai également comment il a très bien fonctionné pour moi pendant six mois.

À la fin de cet article, vous serez en mesure de créer votre propre bot Twitter de messages directs automatiques, de la création de votre message au déploiement du bot, le tout gratuitement !

Cet article se compose de deux sections. Dans la première section, je décris étape par étape comment le script fonctionne et comment vous pouvez facilement contribuer avec d'autres services de bots Twitter. La deuxième section est un tutoriel étape par étape qui vous explique comment déployer et utiliser le bot sans même avoir besoin de connaître Node.js.

### De quoi avez-vous besoin ?

Pour développer ce bot, nous avons besoin de :

* Node.js installé
* [Twit](https://github.com/ttezel/twit) : Client API Twitter pour node (REST & Streaming API)
* [Compte Github](https://github.com/)
* [Compte Twitter](https://twitter.com/)
* [Compte Heroku](https://www.heroku.com/) pour déployer le bot.

Si vous n'êtes pas familier avec Node.js, ou peut-être que vous n'êtes pas programmeur, vous pouvez forker le projet depuis GitHub et l'utiliser comme le vôtre.

Commençons.

### Section 1 : Utiliser Node.js

Si vous avez déjà cloné le projet sur votre ordinateur, vous verrez cette structure :

```
$ cd twitter-bot$ tree .   .
├── config.js
├── index.js
├── LICENSE
├── package.json
├── Procfile
├── README.md
└── src    
    ├── AutoDM.js    
    └── Twit.js
```

Comme vous pouvez le voir, le projet est une simple application Node.js avec un fichier index.js comme point d'entrée :

![Image](https://cdn-media-1.freecodecamp.org/images/bDZu23ehtOOzuXJSj41zkcerKC4pulB2zbjG)
_fichier infex.js_

Le fichier index est un simple script qui importe et appelle la fonction `AutoDM`.

Pour rendre l'application plus amusante, j'ai ajouté un simple message qui s'affiche lorsque l'application a démarré avec succès.

Comme je l'ai déjà mentionné, j'utilise le package Twit pour me connecter à l'API Twitter. Pour ce faire, nous devons créer une simple application Twitter et initialiser l'instance Twit avec la configuration de votre application comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/t-rkEY638vfI7M0Ho6uEYWGqIF3yQ64digAQ)
_fichier Twit.js_

![Image](https://cdn-media-1.freecodecamp.org/images/VdJcNIAqmjHucdxYPmDerDaJDsjOX1j9nOoT)
_fichier config.js_

`process.env.XXXXXXX` est une variable d'environnement que nous devons ajouter à notre application Heroku lors de l'étape de déploiement.

Maintenant, la partie amusante est de créer la fonction AutoDM :

Comme vous pouvez le voir ci-dessous, `AutoDM` est une simple fonction fléchée. Elle écoute l'événement de flux `follow` de l'API Twitter et exécute la fonction SendMessage.

![Image](https://cdn-media-1.freecodecamp.org/images/FEvQdynCkWcsm-0cWlgT2zhLDagu8S8etjbj)
_fichier AutoDM.js_

La fonction `sendMessge` reçoit, en tant que paramètre, l'utilisateur qui vous suit (`screen_name`). Nous devons créer un objet avec `screen_name` et un message texte. Nous envoyons ensuite une requête POST à l'API Twitter pour envoyer un DM à `@screen_name` comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/J7ZkL16xhbvlINNQ8ApFrXp3snStygyV4tLU)
_Fonction SendMessge_

Maintenant, réfléchissez à la manière dont vous souhaitez vous présenter. Vous pouvez modifier la fonction `GenerateMessage` existante pour créer votre propre message de bienvenue. N'oubliez pas d'ajouter quelques politesses, cela augmente les chances que l'utilisateur clique sur votre lien ou réponde à votre message.

![Image](https://cdn-media-1.freecodecamp.org/images/nxNbhd6rc4RgA1Rha-T0n8WBCBNVQK3J0g8K)
_Fonction GenerateMessge_

C'est facile, n'est-ce pas ? Vous pouvez lire plus de code depuis le [dépôt Github](https://github.com/yjose/twitter-bot).

Peut-être que vous n'êtes pas convaincu par la structure des fichiers du projet ou pourquoi nous ne pouvons pas simplement utiliser un fichier simple pour faire tout cela. Vous avez raison de vous poser la question, mais nous utilisons cette structure de projet pour simplifier la contribution au projet. Vous pouvez facilement créer un simple service Twitter comme suivre ou retweeter en exportant une fonction comme autoDM dans un nouveau fichier et en l'appelant dans le fichier index. Donc, si vous avez des idées pour développer de nouveaux services, n'hésitez pas à créer des PR ou des issues pour demander de nouveaux services.

### Créer votre propre bot Twitter ?

#### Étape 1 : Github.

Forker le dépôt du projet sur GitHub [https://github.com/yjose/twitter-bot](https://github.com/yjose/twitter-bot). Vous pouvez donner une étoile au dépôt pour montrer votre soutien.

Maintenant, personnalisez votre message de bienvenue en mettant à jour la fonction `GenerateMessage` et validez vos modifications.

#### Étape 2 : Twitter

Créez une application Twitter. Allez sur [https://apps.twitter.com/](https://apps.twitter.com/), cliquez sur le bouton `Create New App`, puis complétez tous les champs comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/xlx0f6muu4r4eo-pv3-v2xnrg760DsiTKgS6)

Allez dans la section `Permissions` et donnez à l'application l'accès pour envoyer des messages directs en cochant l'option `Read,Write and Access direct messages`.

![Image](https://cdn-media-1.freecodecamp.org/images/BbprSRsg268VlWjy3LqtJTKKqZthLty3MEWp)

Allez dans l'onglet `Key and Access Tokens`, puis cliquez sur le bouton `Generate Access Token` en bas de la page.

Maintenant, copiez toutes vos clés `Consumer Key`, `Consumer Secret`, `Access Token` et `Access Token Secret`. Nous devons les ajouter toutes plus tard en tant que variables Heroku.

#### Étape 3 : Heroku

* Créez un [compte Heroku](https://dashboard.heroku.com/). C'est gratuit !
* Connectez-vous à votre compte Heroku et créez une nouvelle application en cliquant sur le bouton `New`, puis sur l'option `Create new App`.
* Choisissez le nom de votre application, puis cliquez sur `Create App`

![Image](https://cdn-media-1.freecodecamp.org/images/ITgjEvvPRmNRNRu9KHOOWIu2ToWsfEnRvF6l)

Choisissez Github comme méthode de déploiement, puis cliquez sur le bouton de connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/wdyUfZs6Bn-qgvCnxnJmNnXSMZj70yhUqEov)

Tapez le nom de votre dépôt de bot : `twitter-bot` dans votre cas.

![Image](https://cdn-media-1.freecodecamp.org/images/-f-CE8KQCVR7rE0o57K7Ud7OvPWRdenJRUZT)

Maintenant, vous devez ajouter toutes les clés en tant que variables Heroku dans l'onglet des paramètres, et configurer la section des variables.

![Image](https://cdn-media-1.freecodecamp.org/images/xVSpF6QG8Mmlven4QVt5QqE5M4GdZFxPblml)

Retournez à la section de déploiement et cliquez sur `enable automatic deploys`, puis sur le bouton `deploy branch` pour déployer votre application pour la première fois.

![Image](https://cdn-media-1.freecodecamp.org/images/81P3e6VP0hTsy8Shorf2dz8SdeEzi3zTua-L)

Allez dans la section des ressources, activez le dyno worker et désactivez le dyno web.

![Image](https://cdn-media-1.freecodecamp.org/images/tyRf3fmibAGJLZCCCmSrM-f8ejkg31voAppR)

Pour savoir si votre application a démarré avec succès, cliquez sur le bouton `more` en haut à droite de la page, puis sur l'option `view logs`. Vous trouverez une simple console avec une sortie similaire à cette capture d'écran. J'ai quelques nouveaux abonnés et le message a été envoyé avec succès ?.

![Image](https://cdn-media-1.freecodecamp.org/images/qyKAybGAo8wEFBmvRMB809mes7Mxm8iz0dEI)

### Démo en direct

Pour vous assurer que le projet fonctionne parfaitement, vous n'avez qu'à me [**suivre**](https://twitter.com/ElaziziYoussouf) et mon bot Twitter vous enverra un message de bienvenue ?.

Si vous avez un problème avec la mise en œuvre de ce tutoriel, faites-le moi savoir dans les commentaires.

Merci d'avoir lu ! Si vous pensez que d'autres personnes devraient lire cet article et utiliser ce projet, applaudissez pour moi, tweetez et partagez l'article.

N'oubliez pas de me suivre sur Medium pour être informé de mes futurs articles.

> **_Lisez plus d'histoires [https://elazizi.com/](https://elazizi.com/)_**