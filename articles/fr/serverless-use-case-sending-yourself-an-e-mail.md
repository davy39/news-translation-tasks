---
title: 'Serverless Pratique : Comment s''envoyer des blagues sur Chuck Norris par
  e-mail'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-04T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/serverless-use-case-sending-yourself-an-e-mail
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/title-cards3-1.jpg
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: serverless
  slug: serverless
seo_title: 'Serverless Pratique : Comment s''envoyer des blagues sur Chuck Norris
  par e-mail'
seo_desc: 'By Jared Nutt

  Front Matter

  Serverless is one of those terms that has been increasing in popularity lately.
  In fact, when I wrote an article about my AWS architecture, several people mentioned
  to go serverless.


  Serverless doesn''t actually mean there ...'
---

Par Jared Nutt

## Introduction

Serverless est l'un de ces termes qui gagnent en popularité ces derniers temps. En fait, lorsque j'ai écrit un article sur mon architecture AWS, plusieurs personnes m'ont suggéré de passer au serverless.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_U5wGn9apS7AQerUKFlG1Sg.png)

Serverless ne signifie pas _réellement_ qu'il n'y a pas de serveurs, mais comme [Paul Biggar l'a dit](https://thenewstack.io/dark-a-new-programming-language-for-deployless-deployments/) :

> "..il y a des serveurs dans le serverless... vous n'avez simplement pas à y penser."

<iframe src="https://giphy.com/embed/l0K4b3pJqjWMyF6JG" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Serverless est un terme à la mode qui ne fait pas référence à un framework spécifique, cependant, j'ai trouvé que le [Serverless Framework](https://serverless.com/) est la méthode la plus simple pour commencer.

_Note : Pour faire court, "**sls**" est synonyme de [Serverless Framework](https://serverless.com/)._

## Prérequis

Honêtement, la documentation pour le Serverless Framework est si bonne qu'il serait injuste de la recréer ici. Donc, pour garder cet article très ciblé, je vais me concentrer sur des éléments en dehors des guides de démarrage rapide. J'ai inclus les guides spécifiques à AWS ci-dessous :

[Guide de démarrage rapide Serverless AWS](https://serverless.com/framework/docs/providers/aws/guide/quick-start/)

[Commencer avec le Serverless Framework et AWS](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

Je vous suggère de lire ces guides d'abord, si vous n'avez jamais fait quoi que ce soit avec le serverless.

Alternativement, vous pouvez coder avec moi dans ma vidéo de démarrage ci-dessous :

%[https://www.youtube.com/watch?v=sYGE0zQ8tCQ]

<iframe src="https://giphy.com/embed/lz5t2GlcU6CskRIxNI" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

## Vocabulaire

Il y a beaucoup de termes qui entourent **sls** et qui peuvent obscurcir ce à quoi ils font référence. Voici quelques termes clés :

**Service** : La façon dont je vois un service, c'est qu'il s'agit d'une collection de code qui est entièrement servie depuis un seul endroit. Peut contenir une ou plusieurs fonctions.

**Stage** : Cela indique le "type" d'environnement dans lequel vous exécutez. Habituellement, il est divisé en "dev" et "prod". Le stage est une variable du service.

**Fonction** : Un morceau de code qui s'exécute lorsqu'il est appelé. Wow, quelle description géniale. Ce n'est pas nouveau pour quiconque a programmé quoi que ce soit, cependant, il est important de connaître la relation entre une fonction et un service. Il peut y avoir une ou plusieurs fonctions qui font partie d'un Service.

**Provider** : Simplement dit, l'endroit où votre service est déployé, par exemple AWS, GCP, etc.

### Une plongée plus profonde

J'ai trouvé cet article fantastique qui explique en profondeur ce qu'est le Serverless, si vous voulez plus d'informations :

[https://dev.to/sosnowski/anatomy-of-aws-lambda-1i1e](https://dev.to/sosnowski/anatomy-of-aws-lambda-1i1e)

## Ce que nous construisons

Nous allons créer une fonction qui récupère une blague sur Internet et l'envoie par e-mail.

### Ce qu'elle fait

1. Récupère les données de l'API.
2. Crée un modèle d'e-mail.
3. Envoie le modèle d'e-mail.
4. Profit.

### Outils

* Serverless Framework
* Compte AWS (Optionnel)
* AWS CLI
* NPM
* nodemailer

Si vous aimez apprendre via des vidéos, consultez la version vidéo de cet article ici :

%[https://www.youtube.com/watch?v=bZpC9xaKU9k]

## Construire le projet

### Outillage

L'outillage pour **sls** est assez simple. Tout ce que j'ai utilisé, ce sont les CLIs serverless et npm. Si vous n'avez pas npm installé, [installez-le d'abord](https://changelog.com/posts/install-node-js-with-homebrew-on-os-x). Ensuite, exécutez :

`npm i -g serverless`

### Initialisation

Il est généralement bon de commencer avec un modèle. Il y en a plusieurs sur la page [exemples aws serverless](https://serverless.com/framework/docs/providers/aws/examples/).

Pour ce projet, j'ai utilisé le modèle aws-nodejs en exécutant la commande suivante dans le terminal :

```
serverless create --template aws-nodejs --path my-service
```

_Note : si vous ne fournissez pas de flag de chemin, il initialisera le projet dans le dossier dans lequel vous vous trouvez._

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-25-at-12.47.36-PM.png)
_L'Art ASCII est le Meilleur Art_

Si vous consultez le répertoire, il devrait y avoir trois fichiers :

*  `handler.js` 
*  `serverless.yml`
*  `.gitignore` 

Si vous exécutez `sls invoke local -f hello`, vous devriez obtenir une réponse avec un message de succès.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/invoke-local.gif)

### Déploiement

Habituellement, le déploiement d'une application est laissé pour la fin du tutoriel, mais pas pour sls. Dans le cas du [guide de démarrage rapide Serverless](https://serverless.com/framework/docs/providers/aws/guide/quick-start/), c'est l'étape 2.

J'apprécie vraiment cette approche car je préfère commencer la partie déploiement dès que possible dans le développement. Personnellement, je pense qu'il est beaucoup plus facile de faire fonctionner un déploiement lorsque vous avez quelques routes.

**Providers**

Maintenant vient la grande question... où allons-nous déployer ce projet ? Pour ce tutoriel, je vais utiliser AWS, mais vous pouvez utiliser le service que vous préférez.

Voici le guide de démarrage rapide pour configurer AWS comme provider : [Guide de démarrage rapide Serverless AWS](https://serverless.com/framework/docs/providers/aws/guide/quick-start/).

**_Serverless Enterprise_**

Il n'est pas immédiatement apparent sur leur site web quel est le prix de leur édition Enterprise. Cependant, une fois que vous vous inscrivez, ils vous enverront un e-mail qui dit ceci :

> Le niveau gratuit du Serverless Framework inclut tout ce dont vous avez besoin pour développer et déboguer des applications serverless plus efficacement. Vous avez un accès complet à la console Serverless Framework Enterprise, mais vous êtes limité à 1 000 invocations de fonction par mois. Si vous êtes intéressé par l'extension de votre utilisation de Serverless Framework Enterprise au-delà du niveau gratuit, [contactez-nous](https://serverless-289f5d947191.intercom-mail.com/via/e?ob=cY7cHS%2BZj2VcQFfJ784nQVM8V6MMQueJzyEgtPxcKEcydcqbYBJd1OePOwyM01xR&h=4c812da8d71e5f78f9ff82836acbf93df5fe7fb5-22378777535&l=a31459550e6f3973d9146212384178952e265336-984217) pour plus de détails sur les plans et les tarifs disponibles.

**Déployer le projet**

Après avoir configuré vos identifiants, exécutez simplement la commande `sls deploy` dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-25-at-1.37.13-PM.png)
_Cet écran donne beaucoup d'informations (très apprécié), mais que signifie-t-il ?_

La chose la plus confuse pour moi après avoir tapé cette commande était de me demander... où est-il allé ?

<iframe src="https://giphy.com/embed/26DNdV3b6dqn1jzR6" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Dans le cas d'AWS, il crée une pile CloudFormation qui gère ce **Service** pour vous. AWS l'appelle une **Application**. Pour voir ce qui vient de se passer, consultez votre [Console Lambda sur AWS](https://console.aws.amazon.com/lambda/). Vous devriez voir la fonction que vous venez de déployer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-27-at-4.32.35-PM.png)

Si elle n'apparaît pas, vérifiez que vous êtes dans la bonne région. La région par défaut est us-east-1 (Nord de la Virginie). Elle peut être changée via le menu déroulant en haut à droite :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-27-at-4.35.54-PM.png)

**Testez-le**

Pour vous assurer que cela a fonctionné, exécutez simplement `sls invoke -f hello` dans votre terminal. Vous devriez obtenir la même réponse qu'avant, mais cette fois depuis le cloud !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/invoke-cloud.gif)

### Développement local

[W](https://nodemon.io/)e avons déjà testé localement une fois avec `sls invoke local -f hello`. Si vous faites quelque chose de plus compliqué et que vous souhaitez un rafraîchissement de code de style nodemon, consultez [Serverless Offline](https://www.npmjs.com/package/serverless-offline).

## Commencez à écrire !

Maintenant que notre projet est configuré, commençons à écrire du code réel !

Ouvrez à nouveau le fichier `serverless.yml` et apportons quelques modifications.

```yaml
functions:
  sendEmail:
    handler:
     emailHandler.sendEmail
  hello:
    handler: handler.hello
```

Tout d'abord, nous avons ajouté une nouvelle fonction et un nouveau gestionnaire. Le gestionnaire fait référence à un fichier dans le répertoire racine appelé emailHandler (qui n'existe pas encore). Allons le créer !

```js
// emailHandler.js
module.exports.sendEmail = async event => {
  return {
    statusCode: 400,
    body: JSON.stringify(
      {
        message: 'Email envoyé !',
      },
      null,
      2,
    ),
  };
};
```

Si vous invoquez la fonction via `sls invoke local -f sendEmail`, vous devriez obtenir ceci :

```json
{
    "statusCode": 400,
    "body": "{\n  \"message\": \"Email envoyé!\"\n}"
}
```

Très bien, faisons quelque chose d'un peu plus utile. Je suis tombé sur [cette](https://api.chucknorris.io/) API qui sert des blagues sur Chuck Norris, ce qui est parfait pour ce petit tutoriel.

```js
// emailHandler.js
module.exports.sendEmail = async event => {
  // récupère la blague de l'API
  const response = await fetch('https://api.chucknorris.io/jokes/random');
  //  récupère le JSON
  const joke = await response.json();
  return {
    statusCode: 400,
    body: JSON.stringify(
      {
        message: joke.value,
      },
      null,
      2,
    ),
  };
};
```

 Super ! Maintenant, nous obtenons des blagues ! Construisons la partie e-mail.

### Variables d'environnement

Avant d'aller trop loin dans ce projet, vous avez probablement réalisé que nous allons devoir récupérer quelques secrets. En supposant que nous ne voulons pas que le monde ait nos clés API, bien sûr.

<iframe src="https://giphy.com/embed/5UzXVV0RDlkTyYdvlY" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

**Stages**

Normalement, lorsque vous travaillez avec une application node, l'environnement Node dictera s'il s'agit de "dev" ou de "production". Dans sls, cela est décidé par la balise "stage", qui est attachée au provider.

Une excellente explication de [Serverless Stack](https://serverless-stack.com/chapters/stages-in-serverless-framework.html) :

> Le Serverless Framework vous permet de créer des stages pour votre projet à déployer. Les stages sont utiles pour créer des environnements de test et de développement. Typiquement, vous créez un environnement de staging qui est un clone indépendant de votre environnement de production. Cela vous permet de tester et de vous assurer que la version du code que vous êtes sur le point de déployer est prête à être mise en production.

### Mettre en file d'attente les secrets

Créez `env.yml` dans le répertoire racine.

Assurez-vous de l'ajouter à .gitignore

Ajoutez nos variables.

```yaml
# Ajoute les variables d'environnement pour les différents stages
prod:
  MAIL_HOST: ""
  MAIL_PORT: 2525
  MAIL_USER: ""
  MAIL_PASS: ""
dev:
  MAIL_HOST: ""
  MAIL_PORT: 2525
  MAIL_USER: ""
  MAIL_PASS: ""

```

Référencez les variables dans `serverless.yml`

```yaml
provider:
  name: aws
  runtime: nodejs10.x
  stage: dev
  environment:
    MAIL_HOST: ${file(env.yml):${self:provider.stage}.MAIL_HOST}
    MAIL_PORT: ${file(env.yml):${self:provider.stage}.MAIL_PORT}
    MAIL_USER: ${file(env.yml):${self:provider.stage}.MAIL_USER}
    MAIL_PASS: ${file(env.yml):${self:provider.stage}.MAIL_PASS}

```

Oui, c'est une ligne assez longue et folle, mais en gros, cela dit simplement :

Lire le fichier (env.yml) -> Utiliser le stage dans lequel nous exécutons (dev) -> Utiliser la variable associée à ce stage

Pour plus de lectures sur le sujet du chargement des secrets : consultez cet article : [**Charger les secrets depuis env.yml**](https://serverless-stack.com/chapters/load-secrets-from-env-yml.html)

### Envoyer l'e-mail

Pour simplifier, je vais utiliser [Mailtrap](https://mailtrap.io/). C'est un outil fantastique pour tester les e-mails, qui ne nécessite pas de configurer un serveur d'e-mails.

**Installer nodemailer**

Pour installer nodemailer, vous devez initialiser un projet npm. Allez-y et faites-le via la ligne de commande :

```bash
npm init -y
```

Puis installez nodemailer

```bash
npm i nodemailer
```

**Ajoutez vos clés API**

Récupérez vos clés API depuis la boîte de réception Demo de Mailtrap et ajoutez-les à votre `env.yml`

Pour envoyer le mail, nous allons utiliser nodemailer. Voici le code pour Mailtrap + nodemailer :

```js
const nodemailer = require('nodemailer');
// récupère les variables du processus
const { MAIL_HOST, MAIL_PORT, MAIL_USER, MAIL_PASS } = process.env;

// crée le transport
const transport = nodemailer.createTransport({
  host: MAIL_HOST,
  port: MAIL_PORT,
  auth: {
    user: MAIL_USER,
    pass: MAIL_PASS,
  },
});

module.exports.sendEmail = async event => {
  // récupère la blague de l'API
  const response = await fetch('https://api.chucknorris.io/jokes/random');
  //  récupère le JSON
  const joke = await response.json();
  // crée un modèle HTML
  const html = `
	<h1>Blague du jour</h1>
	<p>${joke.value}</p>
	`;

  // envoie le mail avec notre objet de transport
  let info = await transport.sendMail({
    from: '"Chuck Norris" <noreply@chuck.com>', // adresse de l'expéditeur
    to: 'nom@email.com', // liste des destinataires
    subject: 'Blague quotidienne', // ligne d'objet
    html, // corps html
  });

  return {
    statusCode: 400,
    body: JSON.stringify(
      {
        message: joke.value,
      },
      null,
      2,
    ),
  };
};

```

Si tout s'est bien passé, invoquez localement et vérifiez votre mailtrap.

`sls invoke local -f sendEmail`

```json
{
    "statusCode": 400,
    "body": "{\n  \"message\": \"La gomme à mâcher préférée de Chuck Norris, ce sont les balles.\"\n}"
}
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-25-at-4.11.11-PM.png)
_Voir dans Mailtrap_

<iframe src="https://giphy.com/embed/2fQ1Gq3KOpvNs4NTmu" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

## Et ensuite ?

Cet article est devenu un peu long, donc je vais m'arrêter ici. Cependant, dans la prochaine édition de _Practical Serverless_, je vais inclure la connexion à une base de données (pas aussi facile que cela devrait l'être) et la configuration d'exécutions automatiques de fonctions via un cron (beaucoup plus facile que cela en a l'air !).

## Réflexions finales

Je vous laisse décider de la praticité de vous envoyer des blagues, mais je pense que son utilisation va au-delà de M. Norris. Ceci est la partie 1 d'une série appelée _Practical Serverless_. Si vous avez des suggestions à ajouter, n'hésitez pas !

Comme toujours, bon codage !

## Dépôt de code

[https://github.com/DarthOstrich/sls-part1-sendemail](https://github.com/DarthOstrich/sls-part1-sendemail)

## Ressources

  
[https://serverless.com/learn/use-cases/](https://serverless.com/learn/use-cases/)

[https://serverless.com/framework/docs/getting-started/](https://serverless.com/framework/docs/getting-started/)

[https://medium.com/a-man-with-no-server/running-aws-lambda-and-api-gateway-locally-serverless-offline-3c64b3e54772](https://medium.com/a-man-with-no-server/running-aws-lambda-and-api-gateway-locally-serverless-offline-3c64b3e54772)