---
title: Comment créer un bot GitHub avec PhantomJS, React et le framework Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T17:50:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-github-bot-with-phantomjs-react-and-serverless-framework-7b66bb575616
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3x2LwtrTs0Hr2zIm_VUqPA.png
tags:
- name: bots
  slug: bots
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer un bot GitHub avec PhantomJS, React et le framework Serverless
seo_desc: 'By Pavel Vlasov

  This tutorial is about building a simple Serverless bot that returns a chart with
  top GitHub repository contributors for a selected period. It is relevant to those
  who have some experience with React, JavaScript, TypeScript, Node.js, ...'
---

Par Pavel Vlasov

Ce tutoriel explique comment construire un bot Serverless simple qui retourne un graphique avec les principaux contributeurs d'un dépôt GitHub pour une période sélectionnée. Il est destiné à ceux qui ont une certaine expérience avec React, JavaScript, TypeScript, Node.js, Amazon Web Services (AWS) et le framework Serverless.

Vous pouvez consulter [le code sur GitHub](https://github.com/threadheap/github-stats-bot/blob/master/tsconfig.json).

#### Services et outils que nous utiliserons

Avant de plonger dans le codage, faisons un rapide aperçu des services AWS et des outils que nous utiliserons.

Pour récupérer les principaux contributeurs d'un dépôt, nous utiliserons [l'API de statistiques de GitHub](https://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts), l'incroyable [Nivo](http://nivo.rocks/#/pie) pour afficher les données, [Storybook](https://github.com/storybooks/storybook) pour vérifier l'apparence de notre graphique, [PhantomJS](http://phantomjs.org/) pour transformer du HTML en image, et le [framework Serverless](https://serverless.com/) pour interagir avec AWS.

#### Commençons

J'utiliserai TypeScript. Si vous préférez [ES6](http://es6-features.org/#Constants), vous devrez configurer [Babel](https://babeljs.io/).

Tout d'abord, vous devez créer `[tsconfig.json](https://github.com/threadheap/github-stats-bot/blob/master/tsconfig.json)` à la racine de votre dépôt. Les options auxquelles il faut prêter attention incluent :

```
"module": "commonjs","target": "es5","lib": ["es6", "esnext.asynciterable"],"moduleResolution": "node","jsx": "react"
```

Ensuite, nous créerons une API simple pour interroger les statistiques de GitHub. Vous pouvez suivre la structure de fichiers du dépôt GitHub ou utiliser la vôtre. Par exemple :

Pour accéder à l'API GitHub, vous devrez [créer un jeton d'accès personnel](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).

Ce module envoie simplement [la requête](https://api.github.com) avec le jeton fourni et récupère les données.

#### Affichage des graphiques

Pour afficher les données, nous utiliserons Nivo et Storybook. Un composant simple peut ressembler à ceci :

Tout d'abord, configurez Storybook en exécutant la commande suivante dans le dossier racine :

```
npm i -g @storybook/cligetstorybook
```

Copiez le [dossier .storybook](https://github.com/threadheap/github-stats-bot/tree/master/.storybook) dans le dépôt racine et remplacez tous les fichiers existants. Il contient la configuration de Webpack et Storybook. Créez un dossier `stories` et placez-y un exemple de story pour votre composant :

Exécutez `npm run storybook` et ouvrez [localhost](http://localhost:6006/) dans le navigateur. Vous devriez voir le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*exyIVjE5S3_92nKg4h_YvA.png)

Essayez de jouer avec les options et les données de test. Storybook changera l'apparence immédiatement.

#### Transformation de HTML en PNG

Habituellement, les systèmes de chat comme Facebook Messenger et Slack ne permettent pas aux utilisateurs d'insérer des cartes HTML dans le dialogue, donc la prochaine étape sera de construire un helper qui rend le HTML en image PNG.

En utilisant un script simple avec la bibliothèque [jsdom](https://github.com/tmpvar/jsdom), nous pouvons imiter le comportement du navigateur et séquentialiser le HTML, comme ceci :

`createDomForChart` retourne une nouvelle instance de jsdom, et la fonction chart appelle simplement `dom.serialize()` lorsque le rendu du composant est terminé.

Avec PhantomJS, nous pouvons transformer le balisage en image en utilisant ce script simple :

Nous passons `screenshot.js` dans le chemin exécutable de `phantomjs` — ainsi qu'une chaîne HTML, une largeur et une hauteur — et nous obtenons en retour un buffer avec l'image rendue.

Vous pouvez remarquer que j'ai utilisé deux binaires PhantomJS (pour OS X et Linux). Nous aurons besoin de la version Linux plus tard dans un environnement AWS. Vous pouvez les télécharger depuis [PhantomJS.org](http://phantomjs.org/download.html) ou [utiliser les fichiers du dépôt](https://github.com/threadheap/github-stats-bot/tree/master/app/html-to-png/phantomjs).

#### Assemblage de tout

Maintenant, créons une [lambda](https://aws.amazon.com/lambda/) pour gérer les requêtes. Je recommande de mettre la logique de rendu PNG dans un service séparé. Parce que le binaire PhantomJS fait environ 50 Mo, il ralentit le déploiement si vous changez quoi que ce soit dans l'API. De plus, vous pouvez réutiliser cette lambda pour d'autres fins.

Nous commencerons par créer `[webpack.config.ts](https://github.com/threadheap/github-stats-bot/blob/master/webpack.dev.ts)` (pour bundler le code source) et `[serverless.base.js](https://github.com/threadheap/github-stats-bot/blob/master/serverless.base.js)` (pour définir la configuration de base serverless) dans le dossier racine.

Si vous voulez en savoir plus sur les cas d'utilisation des configurations JavaScript serverless, vous pouvez [lire mon article précédent](https://medium.com/@pvlasov/power-up-serverless-framework-with-javascript-configurations-9cf4b9c6ee76).

Vous devrez changer les noms des buckets de déploiement et d'images, comme ceci :

```
deploymentBucket: {    name: 'com.github-stats....deploys'},environment: {    BUCKET: 'com.github-stats....images',    GITHUB_TOKEN: '${env:GITHUB_TOKEN}',    SLACK_TOKEN: '${env:SLACK_TOKEN},    STAGE: '${self:provider.stage}'},
```

C'est parce que le nom du bucket doit être globalement unique.

#### Transformation de HTML en service PNG

Tout d'abord, nous créerons un [handler](https://github.com/threadheap/github-stats-bot/blob/master/app/html-to-png/index.ts) qui retournera une URL de l'image générée. Le handler doit valider et traiter le corps de la requête :

...et si tout est correct, il doit générer l'image et la mettre dans un bucket S3.

Créons `[webpack.config.ts](https://github.com/threadheap/github-stats-bot/blob/master/app/html-to-png/webpack.config.ts)` pour bundler les fichiers sources. Nous utiliserons le plugin `[copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin)` et `[webpack-permissions-plugin](https://github.com/GeKorm/webpack-permissions-plugin)` pour inclure les binaires PhantomJS dans un bundle — et donner des permissions pour l'exécution. Cela nous obligera à exécuter la commande de déploiement avec sudo puisque Webpack n'a pas les permissions de modifier les droits du système de fichiers par défaut.

La dernière étape consistera à utiliser le fichier `[serverless.js](https://github.com/threadheap/github-stats-bot/blob/master/app/html-to-png/serverless.js)` pour lier notre handler à un événement API Gateway.

Maintenant, nous devons effectuer les mêmes étapes pour le [handler de statistiques](https://github.com/threadheap/github-stats-bot/blob/master/app/stats/index.ts), mais nous n'avons pas besoin de faire de changements dans `webpack.config.ts`.

La seule différence est une permission supplémentaire pour invoquer lambda :

```
iamRoleStatements: [                           ...baseConfig.provider.iamRoleStatements,{    Effect: 'Allow',    Action: ['lambda:InvokeFunction'],    Resource: ['*']}]
```

#### Configuration du bot Slack

La dernière étape consistera à créer un service qui gérera les événements de messages pour le bot. Pour garder cela simple, nous gérerons uniquement les événements de mention. Configurons le handler d'événements de base.

Nous devons gérer un événement de vérification de Slack et répondre avec un statut 200 et les paramètres de défi :

```
callback(null, {   body: JSON.stringify({     challenge: (slackEvent as VerificationEvent).challenge   }),   statusCode: 200});
```

Pour gérer correctement un événement Slack, le point de terminaison doit répondre dans les 3000 millisecondes (3 secondes), donc nous devrons répondre immédiatement et envoyer un message de suivi de manière asynchrone en utilisant [l'API postMessage](https://api.slack.com/methods/chat.postMessage).

Dans le code ci-dessus, nous avons analysé le texte du message pour extraire un nom de dépôt et appelé une lambda de statistiques d'images pour récupérer une URL d'image et envoyer un message à Slack. Vous pouvez trouver le code complet du handler [ici](https://github.com/threadheap/github-stats-bot/blob/master/app/slack/index.ts).

Le code pour serverless.js et les configurations Webpack serait similaire au service de statistiques, donc si vous avez des problèmes pour le configurer, consultez le [code source complet](https://github.com/threadheap/github-stats-bot/tree/master/app/slack).

#### Création d'une application Slack

Maintenant, créons une nouvelle application Slack. Allez sur [Slack API](https://api.slack.com), créez un nouveau compte (si vous ne l'avez pas déjà fait), créez une nouvelle application et ajoutez la portée du bot dans la section des portées.

Allez dans la section "OAuth & Permissions" dans la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BtAkQBAhDKgIt5o0Xs3bkg.png)

Ajoutez la portée de l'utilisateur bot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wEGOZdgQffBBPvQULS-iOg.png)

Ensuite, vous pourrez installer l'application dans votre organisation et obtenir l'accès aux jetons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kWV_rEpQwUoWGxyymBhzew.png)

#### Déploiement des services

Vous devrez installer une version du framework serverless **supérieure à 1.26** car les versions antérieures ne supportent pas les fichiers de configuration JavaScript. Et je recommande d'installer [slx](https://github.com/threadheap/serviceless) pour simplifier le déploiement de plusieurs services.

```
npm install -g serverlessnpm install -g serviceless
```

Copiez les jetons du bot GitHub et Slack, et définissez-les comme variables d'environnement GITHUB_TOKEN et SLACK_TOKEN respectivement. Exécutez la commande suivante dans le terminal :

```
sudo GITHUB_TOKEN=<votre jeton> SLACK_TOKEN=<votre jeton slack> slx deploy all
```

Comme mentionné ci-dessus, nous avons besoin de sudo pour définir les permissions d'exécution aux binaires PhantomJS.

Soyez patient ! Le déploiement peut prendre un certain temps. À la fin, vous devriez voir une sortie similaire :

```
Deployment completed successfuly
```

```
[app/html-to-png] [completed]:Service Informationservice: html-to-pngstage: devregion: us-east-1stack: html-to-png-devapi keys:   Noneendpoints:   Nonefunctions:   renderToPng: html-to-png-dev-renderToPngServerless: Removing old service versions...[app/slack] [completed]:Service Informationservice: git-stats-slackstage: devregion: us-east-1stack: git-stats-slack-devapi keys:   Noneendpoints:   POST - https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/stats/slack/event-handlerfunctions:   eventHandler: git-stats-slack-dev-eventHandlerServerless: Removing old service versions...[app/stats] [completed]:Service Informationservice: git-statsstage: devregion: us-east-1stack: git-stats-devapi keys:   Noneendpoints:   GET - https://xxxxxx.execute-api.us-east-1.amazonaws.com/dev/stats/contributors/{owner}/{repo}functions:   getContributorStatsImage: git-stats-dev-getContributorStatsImageServerless: Removing old service versions...
```

La dernière étape consistera à abonner notre point de terminaison aux événements de mention de bot.

Sélectionnez la section "Event Subscription" dans la navigation de l'API Slack.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YcHwjOzxPKOZF-wLYt5TZQ.png)

Ensuite, collez l'URL du handler d'événements que vous pouvez trouver dans la sortie de la commande de déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S0grF5E7HfaP3fihUuj7lg.png)

Il est temps de s'amuser un peu ! Voici quelques exemples d'images rendues :

[serverless/serverless](https://github.com/serverless/serverless)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PpPdZg9hW4ee7VbCLQM7Gw.png)

[facebook/react](https://github.com/facebook/react)

![Image](https://cdn-media-1.freecodecamp.org/images/1*taq4dd5hTHMIXlcUdPl0rQ.png)

[plouc/nivo](https://github.com/plouc/nivo)

![Image](https://cdn-media-1.freecodecamp.org/images/1*KPvScIrez3aAsbwt_nDAuA.png)

### C'est tout !

J'espère que vous avez trouvé cet article utile. J'adorerais voir dans les commentaires d'autres types de statistiques que vous aimeriez voir dans le service.

Merci d'applaudir si vous avez aimé l'article ! Et si vous souhaitez discuter ou vous connecter, vous pouvez me trouver sur [Twitter](https://twitter.com/pvl4sov), [GitHub](https://github.com/pavelvlasov) et [Linkedin](https://www.linkedin.com/in/pavel-vlasov-7647b889/).