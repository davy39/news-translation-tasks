---
title: Apprendre le Serverless en créant votre propre application Slack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-08T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/make-a-serverless-slack-app
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/serverless-1.jpg
tags:
- name: aws lambda
  slug: aws-lambda
- name: JavaScript
  slug: javascript
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
- name: slack
  slug: slack
seo_title: Apprendre le Serverless en créant votre propre application Slack
seo_desc: "By Lekha Surasani\nServerless architecture is the industry's latest buzzword\
  \ and many of the largest tech companies have begun to embrace it. \nIn this article,\
  \ we'll learn what it is and why you should use it. We'll also set up AWS, create\
  \ our serverl..."
---

Par Lekha Surasani

L'architecture Serverless est le dernier mot à la mode dans l'industrie et de nombreuses grandes entreprises technologiques ont commencé à l'adopter. 

Dans cet article, nous allons apprendre ce que c'est et pourquoi vous devriez l'utiliser. Nous allons également configurer AWS, créer notre application serverless et créer une application Slack !

## Qu'est-ce que le Serverless ?

Le Serverless est un paradigme de cloud computing dans lequel le développeur n'a plus à se soucier de la maintenance d'un serveur – il se concentre simplement sur le code. 

Les fournisseurs de cloud, tels qu'AWS ou Azure, sont désormais responsables de l'exécution du code et de la maintenance des serveurs en allouant dynamiquement leurs ressources. Une variété d'événements peut déclencher l'exécution du code, y compris des tâches cron, des requêtes http ou des événements de base de données. 

Le code que les développeurs envoient au cloud est généralement juste une fonction, donc, souvent, l'architecture serverless est mise en œuvre en utilisant des Functions-as-a-Service, ou FaaS. Les principaux fournisseurs de cloud fournissent des frameworks pour FaaS, tels qu'AWS Lambda et Azure Functions.

## Pourquoi le Serverless ?

Non seulement le serverless permet aux développeurs de se concentrer uniquement sur le code, mais il présente également de nombreux autres avantages. 

Puisque les fournisseurs de cloud sont désormais responsables de l'exécution du code et allouent dynamiquement les ressources en fonction des déclencheurs d'événements, vous payez généralement par requête, ou lorsque votre code est en cours d'exécution. 

De plus, puisque les fournisseurs de cloud gèrent vos serveurs, vous n'avez pas à vous soucier de la mise à l'échelle – le fournisseur de cloud s'en chargera. Cela rend les applications serverless moins coûteuses, plus faciles à maintenir et plus faciles à mettre à l'échelle.

---

## Configuration d'AWS Lambda

Pour ce tutoriel, j'utiliserai AWS Lambda, donc tout d'abord, nous créerons un [compte AWS](https://aws.amazon.com/). Je trouve l'interface utilisateur d'AWS difficile à comprendre et à naviguer, donc je vais ajouter des captures d'écran pour chaque étape.

Une fois connecté, vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-17.png)
_Écran principal_

Ensuite, nous allons configurer un utilisateur IAM. Un utilisateur [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) (Identity and Access Management) interagit avec AWS et ses ressources en votre nom. Cela vous permet de créer différents utilisateurs IAM avec différentes permissions et objectifs, sans compromettre la sécurité de votre compte utilisateur racine.

Cliquez sur l'onglet "services" en haut de la page, et tapez "IAM" dans la barre :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-27.png)

Cliquez sur le premier résultat, et vous verrez, dans la barre latérale de gauche, que vous êtes sur le tableau de bord. Cliquez sur l'option "Utilisateurs" pour créer notre nouvel utilisateur IAM. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-28.png)

Cliquez sur le bouton "Ajouter un utilisateur" pour créer un nouvel utilisateur. Remplissez les détails comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-29.png)

Vous pouvez nommer votre utilisateur comme vous le souhaitez, mais j'ai choisi `serverless-admin`. Assurez-vous que votre utilisateur a un "accès programmatique" à AWS, **pas** un "accès à la console de gestion AWS". Vous utiliseriez ce dernier pour les coéquipiers, ou d'autres _humains_ qui ont besoin d'un accès à AWS. Nous avons juste besoin que cet utilisateur interagisse avec AWS Lambda, donc nous pouvons simplement lui donner un accès programmatique. 

Pour les permissions, j'ai choisi d'attacher des politiques existantes puisque je n'ai pas de groupes, et je n'ai pas d'utilisateurs existants dont je veux copier les permissions. Dans cet exemple, je vais créer l'utilisateur avec un accès administrateur puisque c'est juste pour un projet personnel ; cependant, si vous deviez utiliser une application serverless dans un environnement de production réel, votre utilisateur IAM devrait être limité pour n'accéder qu'aux parties nécessaires de AWS pour Lambda. (Les instructions peuvent être trouvées [ici](https://serverless.com/blog/abcs-of-iam-permissions/)).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-58.png)

Je n'ai pas ajouté de tags et j'ai créé l'utilisateur. Il est vital de sauvegarder les informations qui vous sont données sur l'écran suivant - l'ID d'accès et la clé d'accès secrète.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot_2019-08-04-IAM-Management-Console.png)

Ne quittez pas cet écran sans avoir copié les deux ! Vous ne pourrez plus voir la clé d'accès secrète après cet écran.

Enfin, nous allons ajouter ces identifiants à la ligne de commande AWS. Utilisez ce [guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) pour configurer aws cli.

Assurez-vous de l'avoir installé en exécutant `aws --version`. Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-04-at-2.02.27-PM.png)

Ensuite, exécutez `aws configure` et remplissez les invites :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-04-at-5.42.53-PM.png)

J'ai déjà configuré la région par défaut comme `us-east-2`, mais vous pouvez utiliser [ceci](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) pour déterminer quelle est votre région.

Pour vous assurer que vous avez configuré vos identifiants correctement, vous pouvez exécuter `cat ~/.aws/credentials` dans votre terminal.

Si vous souhaitez configurer un profil autre que celui par défaut, vous pouvez exécuter la commande comme suit : `aws configure --profile [nom du profil]`.

Si vous avez eu du mal à suivre les étapes, vous pouvez également consulter [la documentation d'AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

---

## Configuration de serverless

Allez dans votre terminal et installez le package `serverless` globalement en utilisant `npm` : `npm i -g serverless`. ([Plus d'informations sur serverless ici](https://serverless.com/))  

Votre terminal devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-04-at-1.55.12-PM.png)

Ensuite, naviguez jusqu'au répertoire où vous souhaitez créer l'application, puis exécutez `serverless` et suivez les invites :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-04-at-5.55.03-PM.png)

Pour cette application, nous utiliserons Node.js. Vous pouvez nommer votre application comme vous le souhaitez, mais j'ai appelé la mienne `exampleSlackApp`.

Ouvrez votre éditeur de code préféré sur le contenu de `exampleSlackApp` (ou ce que vous avez appelé votre application).

Tout d'abord, nous allons examiner `serverless.yml`. Vous verrez qu'il y a beaucoup de code commenté ici décrivant les différentes options que vous pouvez utiliser dans le fichier. Lisez-le définitivement, mais je l'ai réduit à juste :

```
service: exampleslackapp

provider:
  name: aws
  runtime: nodejs10.x
  region: us-east-2

functions:
  hello:
    handler: handler.hello
```

 J'ai inclus `region` puisque la valeur par défaut est `us-east-1` mais mon profil aws est configuré pour `us-east-2`.

Déployons ce que nous avons déjà en exécutant `serverless deploy` dans le répertoire de l'application que `serverless` vient de créer pour nous. La sortie devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-05-at-12.07.10-AM.png)

Et si vous exécutez `serverless invoke -f hello` dans votre terminal, il exécutera l'application, et vous devriez voir :

```
{
    "statusCode": 200,
    "body": "{\n  \"message\": \"Go Serverless v1.0! Your function executed successfully!\",\n  \"input\": {}\n}"
}
```

Pour une preuve supplémentaire que notre application Slack est en ligne, vous pouvez retourner à la console AWS. Allez dans le menu déroulant des services, recherchez "Lambda", et cliquez sur la première option ("Exécuter du code sans penser aux serveurs").

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-32.png)

Et voici votre application !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-33.png)

Ensuite, nous allons explorer l'utilisation réelle de serverless en construisant notre application Slack. Notre application Slack publiera une citation aléatoire de [Ron Swanson](https://en.wikipedia.org/wiki/Ron_Swanson) sur Slack en utilisant une [commande slash](https://api.slack.com/slash-commands) comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-07-at-10.23.40-PM.png)

Les étapes suivantes n'ont pas nécessairement à être effectuées dans l'ordre dans lequel je les ai faites, donc si vous voulez sauter certaines étapes, n'hésitez pas !

---

## Ajout de l'API à notre code

J'utilise [cette API](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api?ref=public-apis) pour générer des citations de Ron Swanson puisque la documentation est assez simple (et bien sûr, c'est gratuit). Pour voir comment les requêtes sont faites et ce qui est retourné, vous pouvez simplement mettre cette URL dans votre navigateur :

[`https://ron-swanson-quotes.herokuapp.com/v2/quotes`](https://ron-swanson-quotes.herokuapp.com/v2/quotes)

Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-59.png)

Donc, nous pouvons prendre notre fonction initiale et la modifier comme suit :

```
module.exports.hello = (event) => {
  getRon();
};
```

et `getRon` ressemble à ceci :

```
function getRon() {
  request('https://ron-swanson-quotes.herokuapp.com/v2/quotes', function (err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
  })
}
```

Maintenant, vérifions si cela fonctionne. Pour tester ce code localement, dans votre terminal : `serverless invoke local -f hello`. Votre sortie devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-07-at-9.41.53-PM.png)
_Spoiler : Il y avait une mauvaise façon de consommer de l'alcool_

`serverless invoke -f hello` exécuterait le code que vous avez déployé, comme nous l'avons vu dans les sections précédentes. `serverless invoke local -f hello`, cependant, exécute votre code local, donc c'est utile pour les tests. Allez-y et déployez en utilisant `serverless deploy` !

---

## Créer votre application Slack

Pour créer votre application Slack, suivez ce [lien](https://api.slack.com/apps?new_app=1). Cela vous obligera à vous connecter à un espace de travail Slack, alors assurez-vous d'en faire partie d'un auquel vous pouvez ajouter cette application. J'en ai créé un de test pour mes besoins. Vous serez invité avec cette fenêtre modale. Vous pouvez remplir ce que vous voulez, mais voici ce que j'ai comme exemple :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-61.png)

À partir de là, vous serez redirigé vers la page d'accueil de votre application. Vous devriez définitivement explorer ces pages et les options. Par exemple, j'ai ajouté la personnalisation suivante à mon application :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-62.png)
_Les informations d'affichage peuvent être trouvées dans l'onglet "Informations de base" de l'application_

Ensuite, nous devons ajouter quelques permissions à l'application :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot_2019-08-07-Slack-API-Applications-lekha_test-Slack.png)

Pour obtenir un jeton d'accès OAuth, vous devez ajouter quelques étendues et permissions, que vous pouvez faire en faisant défiler vers le bas :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-64.png)

J'ai ajouté "Modifier vos chaînes publiques" pour que le bot puisse écrire dans une chaîne, "Envoyer des messages en tant que Ron Swanson" pour que lorsque le message est publié, cela ressemble à un utilisateur appelé Ron Swanson qui publie le message, et des commandes slash pour que l'utilisateur puisse "demander" une citation comme montré dans la capture d'écran au début de l'article. Après avoir sauvegardé les modifications, vous devriez pouvoir faire défiler vers le haut jusqu'à OAuths & Permissions pour voir :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-65.png)

Cliquez sur le bouton pour installer l'application dans l'espace de travail, et vous aurez un jeton d'accès OAuth ! Nous reviendrons à cela dans une seconde, alors copiez-le ou souvenez-vous qu'il est à cet endroit.

---

## Connecter le code et l'application Slack

Dans AWS Lambda, trouvez votre fonction d'application Slack. Votre section Code de la fonction devrait montrer notre code mis à jour avec l'appel à notre API Ron Swanson (si ce n'est pas le cas, retournez à votre terminal et exécutez `serverless deploy`). 

Faites défiler vers le bas jusqu'à la section qui dit "[Variables d'environnement](https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html)", et mettez votre jeton d'accès OAuth Slack ici (vous pouvez nommer la clé comme vous le souhaitez) :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot_2019-08-07-Lambda-Management-Console.png)

Retournez à notre code et ajoutons Slack dans notre fonction. En haut de notre fichier, nous pouvons déclarer une `const` avec notre nouveau jeton OAuth : 

`const SLACK_OAUTH_TOKEN = process.env.OAUTH_TOKEN`. 

`process.env` récupère simplement nos variables d'environnement ([lecture supplémentaire](https://nodejs.org/dist/latest-v8.x/docs/api/process.html#process_process_env)). Ensuite, examinons l'[API Slack](https://api.slack.com/methods/chat.postMessage) pour comprendre comment publier un message dans une chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-67.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-76.png)

Les deux images ci-dessus que j'ai prises de l'API sont les plus pertinentes pour nous. Donc, pour faire cette requête API, j'utiliserai `request` en passant un objet appelé `options` :

```
  let options = {
    url: 'https://slack.com/api/chat.postMessage',
    headers: {
      'Accept': 'application/json',
    },
    method: 'POST',
    form: {
      token: SLACK_OAUTH_TOKEN,
      channel: 'general', // codage en dur pour l'instant
      text: 'I am here',
    }
  }
```

et nous pouvons faire la requête :

```
  request(options, function(err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
  })
```

Enfin, je vais envelopper le tout dans une fonction :

```
function postRon(quote) {
  let options = {
    url: 'https://slack.com/api/chat.postMessage',
    headers: {
      'Accept': 'application/json',
    },
    method: 'POST',
    form: {
      token: SLACK_OAUTH_TOKEN,
      channel: 'general',
      text: quote,
    }
  }

  request(options, function(err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
  })
}
```

et nous pouvons l'appeler depuis `getRon` comme ceci :

```
function getRon() {
  request('https://ron-swanson-quotes.herokuapp.com/v2/quotes', function (err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
    postRon(body.substring(2, body.length - 2)) // ici pour l'analyse, supprimez si vous voulez voir comment/pourquoi je l'ai fait
  })
}
```

Donc notre code devrait ressembler à ceci :

```
'use strict';
let request = require('request');

const SLACK_OAUTH_TOKEN = process.env.OAUTH_TOKEN

module.exports.hello = (event) => {
  getRon();
};

function getRon() {
  request('https://ron-swanson-quotes.herokuapp.com/v2/quotes', function (err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
    postRon(body.substring(2, body.length - 2))
  })
}

function postRon(quote) {
  let options = {
    url: 'https://slack.com/api/chat.postMessage',
    headers: {
      'Accept': 'application/json',
    },
    method: 'POST',
    form: {
      token: SLACK_OAUTH_TOKEN,
      channel: 'general',
      text: quote,
    }
  }

  request(options, function(err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
  })
}
```

Maintenant, testons ! Malheureusement, notre variable d'environnement dans AWS Lambda n'est pas disponible pour nous lorsque nous exécutons `serverless invoke local -f hello`. Il y a plusieurs façons d'aborder cela, mais pour nos besoins, vous pouvez simplement remplacer la valeur de `SLACK_OAUTH_TOKEN` par votre véritable jeton OAuth (assurez-vous que c'est une chaîne). Mais assurez-vous de le remettre avant de le pousser vers le contrôle de version ! 

Exécutez `serverless invoke local -f hello`, et avec un peu de chance, vous devriez voir un message comme celui-ci dans votre chaîne #general :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-69.png)

_Veuillez noter que j'ai mis le nom de ma chaîne comme 'general' puisque c'est mon espace de travail de test ; cependant, si vous êtes dans un espace de travail réel, vous devriez créer une chaîne séparée pour tester les applications, et y mettre le message à la place pendant que vous testez._

Et dans votre terminal, vous devriez voir quelque chose comme :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-07-at-10.48.38-PM.png)

Si cela fonctionne, allez-y et déployez-le en utilisant `serverless deploy`. Si ce n'est pas le cas, la meilleure façon de déboguer cela est d'ajuster le code et d'exécuter `serverless invoke local -f hello`.

---

## Ajout d'une commande slash

La dernière et dernière partie consiste à ajouter une commande slash ! Retournez à la page d'accueil de votre fonction dans AWS Lambda et cherchez le bouton qui dit "Ajouter un déclencheur" :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-70.png)
_Nous allons ajouter une API Gateway (comme je l'ai déjà)._

Cliquez sur le bouton pour accéder à la page "Ajouter un déclencheur", et sélectionnez "API Gateway" dans la liste :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-71.png)

 J'ai rempli les informations principalement sur la base des valeurs par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-72.png)

J'ai également laissé cette API ouverte à l'utilisation – cependant, si vous utilisez cela en production, vous devriez discuter avec votre équipe du protocole standard à utiliser. "Ajoutez" l'API, et vous devriez recevoir un point de terminaison d'API. Gardez-le à portée de main, car nous en aurons besoin pour l'étape suivante. 

Passons à notre application Slack et ajoutons une commande slash :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-73.png)

Cliquez sur "Créer une nouvelle commande" et une nouvelle fenêtre devrait s'ouvrir pour créer une commande. Voici comment j'ai rempli la mienne :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot_2019-08-07-Slack-API-Applications-lekha_test-Slack-1-.png)

Vous pouvez entrer ce que vous voulez pour "commande" et "description courte", mais pour "URL de requête", vous devriez mettre votre point de terminaison d'API.

Enfin, nous allons revenir à notre code pour faire quelques ajustements finaux. Si vous essayez d'utiliser la commande slash, vous devriez recevoir une sorte d'erreur – cela est dû au fait que Slack attend une réponse et AWS attend que vous donniez une réponse lorsque le point de terminaison est atteint. Donc, nous allons changer notre fonction pour permettre un `callback` ([pour référence](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-handler.html)) :

```
module.exports.hello = (event,context,callback) => {
  getRon(callback);
};
```

et ensuite nous allons changer `getRon` pour faire quelque chose avec le `callback` :

```
function getRon(callback) {
  request('https://ron-swanson-quotes.herokuapp.com/v2/quotes', function (err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
    callback(null, SUCCESS_RESPONSE)
    postRon(body.substring(2, body.length - 2))
  })
}
```

où `SUCCESS_RESPONSE` est en haut du fichier :

```
const SUCCESS_RESPONSE = {
  statusCode: 200,
  body: null
}
```

Vous pouvez mettre le callback ici ou dans `postRon` – cela dépend simplement de vos objectifs avec le callback. 

Notre code à ce stade ressemble maintenant à quelque chose comme ceci :

```
'use strict';
let request = require('request');

const SLACK_OAUTH_TOKEN = OAUTH_TOKEN

const SUCCESS_RESPONSE = {
  statusCode: 200,
  body: null
}

module.exports.hello = (event,context,callback) => {
  getRon(callback);
};

function getRon(callback) {
  request('https://ron-swanson-quotes.herokuapp.com/v2/quotes', function (err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
    callback(null, SUCCESS_RESPONSE)
    postRon(body.substring(2, body.length - 2))
  })
}

function postRon(quote) {
  let options = {
    url: 'https://slack.com/api/chat.postMessage',
    headers: {
      'Accept': 'application/json',
    },
    method: 'POST',
    form: {
      token: SLACK_OAUTH_TOKEN,
      channel: 'general',
      text: quote,
    }
  }

  request(options, function(err, resp, body) {
    console.log('error:', err)
    console.log('statusCode:', resp && resp.statusCode)
    console.log('body', body)
  })
}
```

Vous devriez maintenant pouvoir utiliser la commande `/ron` dans Slack et obtenir une citation de Ron Swanson en retour. Si ce n'est pas le cas, vous pouvez utiliser les journaux Cloudwatch pour voir ce qui n'a pas fonctionné :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot_2019-08-07-Lambda-Management-Console-1-.png)

La façon dont notre code fonctionne maintenant, nous avons codé en dur le nom de la chaîne. Mais ce que nous voulons vraiment, c'est que la citation soit publiée dans le message où vous avez utilisé `/ron`. 

Donc, nous pouvons maintenant utiliser la partie `event` de notre fonction. 

```
module.exports.hello = (event,context,callback) => {
  console.log(event)
  getRon(callback);
};
```

Utilisez `/ron` pour exécuter la fonction, puis vérifiez vos journaux Cloudwatch pour voir ce qui est enregistré dans la console (vous devrez peut-être actualiser). Vérifiez les journaux les plus récents et vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-74.png)

Le premier élément de cette liste (où il est écrit "resource", "path", etc.) est l'événement, donc si vous développez cela, vous verrez une longue liste de choses, mais ce que nous cherchons est 'body' tout en bas :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-75.png)
_où est Waldo : édition spot the param_

Body est une chaîne avec quelques informations pertinentes, dont "channel_id". Nous pouvons utiliser channel_id (ou channel_name) et le passer dans la fonction qui crée notre message Slack. Pour votre commodité, j'ai déjà analysé cette chaîne : `event.body.split("&")[3].split("=")[1]` devrait vous donner le channel_id. J'ai codé en dur l'entrée (3) où se trouvait le channel_id pour simplifier.

Maintenant, nous pouvons modifier notre code pour enregistrer cette chaîne en tant que variable :

`let channel = 'general'` (comme notre solution de repli)

```
module.exports.hello = (event,context,callback) => {
  console.log(event)
  channel = event.body.split("&")[3].split("=")[1]
  console.log(context)
  getGoat(callback);
};
```

et dans `postRon` :

```
  let options = {
    url: 'https://slack.com/api/chat.postMessage',
    headers: {
      'Accept': 'application/json',
    },
    method: 'POST',
    form: {
      token: SLACK_OAUTH_TOKEN,
      channel: channel,
      text: quote,
    }
  }
```

Enfin, si vous utilisez une commande Slack dans n'importe quelle chaîne de votre espace de travail, vous devriez pouvoir voir une citation de Ron Swanson apparaître ! Si ce n'est pas le cas, comme je l'ai mentionné précédemment, les outils les plus courants que j'utilise pour déboguer les applications serverless sont `serverless invoke local -f <nom de la fonction>` et les journaux Cloudwatch.

---

Espérons que vous avez réussi à créer une application Slack fonctionnelle ! J'ai inclus des ressources et des lectures de fond dispersées dans l'article et je suis heureux de répondre à toutes les questions que vous pourriez avoir !

_Dépôt final avec le code :_ [https://github.com/lsurasani/ron-swanson-slack-app/](https://github.com/lsurasani/ron-swanson-slack-app/)