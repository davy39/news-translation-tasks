---
title: 'Tutoriel : Créer une application d''on-boarding communautaire avec Serverless,
  StepFunctions et StackStorm…'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-18T18:15:36.000Z'
originalURL: https://freecodecamp.org/news/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QdErjJE8X0jg3SfR7QyBVQ.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Python
  slug: python
- name: serverless
  slug: serverless
- name: slack
  slug: slack
seo_title: 'Tutoriel : Créer une application d''on-boarding communautaire avec Serverless,
  StepFunctions et StackStorm…'
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  Read on if you are:


  A serve...'
---

Par Dmitri Zimine

Construisez une application Serverless réelle sur AWS avec le [Serverless framework](https://serverless.com/framework/) et des fonctions prêtes à l'emploi du catalogue open-source [StackStorm Exchange](https://exchange.stackstorm.org).

Épisode un | [Épisode deux](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) | [Épisode trois](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a) | [Épisode quatre](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)

Continuez votre lecture si vous êtes :

* Un développeur Serverless utilisant le [Serverless framework](https://serverless.com/framework/) qui souhaite découvrir des fonctions prêtes à l'emploi du catalogue open-source StackStorm Exchange,
* Un utilisateur de [StackStorm](https://stackstorm.com) qui travaille sur AWS et regrette l'absence de la richesse des intégrations de [StackStorm Exchange](https://exchange.stackstorm.org) à cet endroit.
* Toute personne disposant de 2 heures pour suivre ce tutoriel et apprendre le Serverless avec quelque chose de plus élaboré et concret qu'un [exemple Hello-world](https://serverless.com/framework/docs/providers/aws/examples/hello-world/).

Si vous n'avez que 8 minutes, parcourez le texte et les exemples, passez 30 secondes supplémentaires à explorer [StackStorm Exchange](https://exchange.stackstorm.org) pour voir le potentiel, et ajoutez cet article à vos favoris pour y revenir quand vous en aurez besoin.

#### Intro

Lorsque j'ai [exploré Serverless avec Python, StepFunctions et un Front-end Web](https://medium.com/@dzimine/exploring-serverless-with-python-stepfunctions-and-web-front-end-8e0bf7203d4b), une chose m'a manqué : un catalogue d'intégrations réutilisables. Quelque chose comme les [200 connecteurs pour Azure Logic apps](https://docs.microsoft.com/en-us/azure/connectors/apis-list#popular-connectors). Ou les [130 packs d'intégration pour StackStorm](https://exchange.stackstorm.org).

Quand nous avons besoin d'intégrer Slack, Jira, Stripe ou Nest, pourrions-nous éviter de plonger dans leurs API et leurs mécanismes d'authentification, et simplement saisir une fonction prête à l'emploi ?

C'est désormais possible : StackStorm vient d'[annoncer un plugin pour le Serverless framework](https://stackstorm.com/2017/12/14/stackstorm-exchange-goes-serverless) qui transforme les intégrations de StackStorm Exchange en fonctions AWS Lambda.

Dans ce tutoriel, je vais montrer comment utiliser le plugin et les intégrations Exchange dans le contexte de la création d'une application d'on-boarding communautaire Serverless à partir de zéro. Rendons cela interactif et amusant.

Je suppose que vous n'avez aucune familiarité avec le [Serverless framework](https://serverless.com/framework/) ni avec StackStorm. Mais vous devriez savoir coder et être assez astucieux pour compenser les erreurs et les omissions que je ferai inévitablement.

Nous irons lentement, avec des détails minutieux, c'est pourquoi il y aura quatre épisodes.

Dans ce premier épisode, je vais tout configurer et déployer ma première action StackStorm Exchange.

Dans le prochain épisode, nous ajouterons d'autres actions.

Dans le troisième épisode, je les relierai ensemble avec une AWS StepFunction.

Dans le quatrième épisode, nous ajouterons un Front-end Web avec une réflexion et un résumé. Chaque épisode prendra environ une heure à suivre.

Prêt ? C'est parti.

### L'application

Nous allons construire une application d'on-boarding communautaire. En fait, nous allons reconstruire de zéro celle que nous utilisons chez StackStorm. C'est comme [SlackIn](http://rauchg.com/slackin/) avec un flux de travail d'on-boarding personnalisable en plusieurs étapes. L'application présente un formulaire web d'inscription, qui transmet les informations du nouvel utilisateur via API Gateway au workflow StepFunction qui exécute les étapes d'intégration.

Dans mon cas, les étapes sont 1) inviter les utilisateurs sur Slack 2) créer un enregistrement de contact dans l'outil CRM ActiveCampaign et 3) placer un enregistrement utilisateur dans une table DynamoDB interne. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QdErjJE8X0jg3SfR7QyBVQ.png)

Vous pouvez trouver l'implémentation précédente [sur GitHub](https://github.com/dzimine/slack-signup-serverless), ou [l'utiliser et rejoindre la communauté StackStorm](https://stackstorm.com/community-signup) sur Slack pour vos questions concernant l'intégration de StackStorm Exchange.

#### Préparation

Tout d'abord, vous aurez besoin d'un compte AWS, de NodeJS, de Docker et du Serverless framework. Et de Slack ! Car notre première action consistera à inviter des utilisateurs sur Slack.

1. Assurez-vous que [Node.JS](https://nodejs.org/) est installé et que sa version est `8.4.0` ou supérieure.
2. [Installez le Serverless framework](https://serverless.com/framework/docs/providers/aws/guide/installation/), et configurez vos identifiants AWS en [suivant ce guide](https://serverless.com/framework/docs/providers/aws/guide/credentials/).
3. [Installez Docker](https://docs.docker.com/engine/installation/). Le plugin l'utilise pour l'environnement de build afin de rendre les binaires des lambdas compatibles avec l'environnement d'exécution AWS, quel que soit l'OS que vous utilisez pour le développement. Il existe un moyen de le faire fonctionner sans Docker, mais ne prenez pas de risques.
4. Slack ! Notre action nécessitera un accès administrateur et utilisera une API Slack non documentée (docs ici, jeu de mots volontaire) pour inviter de nouveaux utilisateurs. Le plus simple est de [créer une nouvelle équipe](https://slack.com/get-started). Cela prend 4 min. Slack ne s'en plaindra pas — cela montrera de la croissance à leurs investisseurs.
5. Une fois l'espace de travail créé, il est temps d'obtenir un jeton d'authentification. Allez sur [api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens). Ne craignez pas les « Legacy Warnings » : ce tutoriel deviendra obsolète avant eux. Faites ce qu'ils disent, récupérez votre jeton.

**ASTUCE DE PRO :** Utilisez [ce petit hack](https://github.com/StackStorm-Exchange/stackstorm-slack#obtaining-auth-token) pour obtenir et utiliser le jeton d'authentification de votre propre utilisateur. C'est beaucoup plus rapide, idéal pour tester et déboguer. Mais s'il vous plaît, ne l'utilisez jamais, au grand jamais, en production !

### Créer un projet, ajouter une première action

Essayez `sls --help` pour vous assurer qu'au moins quelque chose fonctionne. `sls` est un raccourci pour `serverless`, la CLI du Serverless framework. Maintenant, posez votre café, il est temps de créer un projet. Certains aiment utiliser les templates fournis avec serverless : `sls create --template`. Je préfère commencer de zéro :

```
mkdir slack-signup-serverless-stormless
cd slack-signup-serverless-stormless
```

```
npm init
```

```
# Une fois que vous avez répondu aux questions, le projet est configuré.
```

Ensuite, installez `[serverless-plugin-stackstorm](https://github.com/StackStorm/serverless-plugin-stackstorm)`, celui qui connecte les actions de [StackStorm Exchange](https://exchange.stackstorm.org).

```
npm install --save-dev serverless-plugin-stackstorm
```

… et créez un fichier `serverless.yml` minimal pour que la commande `sls` reconnaisse le plugin.

Maintenant, **créez la première action**. J'utiliserai le [pack Slack de StackStorm Exchange](https://exchange.stackstorm.org/#slack), qui a fait ses preuves. Quelle action, me direz-vous ? D'accord, StackStorm Exchange n'est pas encore assez intelligent pour afficher la liste des actions du pack, mais `sls stackstorm` va nous sauver.

`sls stackstorm info --pack slack`

Oh là là ! Il y en a tellement ! Qu'est-ce que c'est ? Je suppose que j'ai besoin d'une PR pour afficher la description de l'action. En attendant, `| grep admin` nous donnera celle dont nous avons besoin : `slack.users.admin.invite`. Interrogeons l'action pour connaître ses paramètres :

```
$ sls stackstorm info --action slack.users.admin.invite
slack.users.admin.invite ...... Envoyer une invitation pour rejoindre une organisation Slack
Parameters
  attempts [integer]  ......... la description est manquante
  channels [string]  .......... Canaux à rejoindre automatiquement.
  email [string] (requis) ... Adresse e-mail à laquelle envoyer l'invitation.
  first_name [string]  ........ Prénom de l'utilisateur
  set_active [boolean]  ....... L'utilisateur doit-il être actif.
  token [string]  ............. Jeton API Slack.
Configuration
  action_token [string]  ...... Jeton d'action Slack.
  admin [object]  ............. Paramètres spécifiques à l'action d'administration.
  post_message_action [object]   Paramètres spécifiques à l'action d'envoi de message.
  sensor [object]  ............ Paramètres spécifiques au capteur.
```

Génial ! Nous pouvons voir qu'il n'y a qu'un seul paramètre requis, `email`, mais j'ajouterai `first_name` pour rester convivial. Le jeton peut être passé en tant que paramètre ou en tant que config. Et si je choisis d'utiliser la config, mes connaissances préalables me suggèrent que l'objet `admin [object]` ne nécessite que `admin_token`. Celui-là même que je vous ai demandé de mémoriser lors de la configuration de l'espace de travail Slack.

**ASTUCE DE PRO :** Pendant que nous peaufinons encore le plugin pour exposer tous les détails de la configuration, vous pouvez les découvrir en explorant le schéma de configuration du pack StackStorm Exchange dans le fichier `config.schema.yaml`. Par exemple, voici [config.example.yaml](https://github.com/StackStorm-Exchange/stackstorm-slack/blob/master/config.schema.yaml#L47-L78) pour notre pack Slack.

Nous avons maintenant tout ce dont nous avons besoin pour créer le cœur de tout projet Serverless : le `serverless.yml`. Le voici :

C'est le bon moment pour en apprendre un peu plus sur Serverless. Faites une petite pause pour parcourir les [Concepts fondamentaux](https://serverless.com/framework/docs/providers/aws/guide/intro/) et ajoutez la [Référence Serverless.yml](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/) à vos favoris.

J'ai ajouté la section `events` aux lignes 9 à 12 afin que nous puissions invoquer la fonction avec un appel REST via un endpoint AWS API Gateway. Le Serverless framework s'occupera de toute la magie de la Gateway.

Notez que cette configuration par défaut demande à API Gateway de transmettre l'appel REST POST avec le corps du POST sous la clé `body` ([détails ici](https://serverless.com/framework/docs/providers/aws/events/apigateway#simple-http-endpoint)). Lorsque nous envoyons un POST `{"first_name": "Santa", "email": "santa@mad.russian.xmas.com"}`, l'événement transmis à la Lambda est :

```
..."body": {    "first_name": "Santa",     "email": "santa@mad.russian.xmas.com"}
```

Connaître la structure des données d'entrée est important pour les mapper aux paramètres d'entrée de l'action. C'est intuitif : `input` représente le paramètre `event` du [modèle de programmation AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html) (au fait, devrions-nous l'appeler `event` ? Votez avec une PR !).

[Jinja](http://jinja.pocoo.org/) est utilisé pour mapper les entrées ; nos amis JavaScript moins familiers avec cet outil Python courant le trouvent assez intuitif dans les cas simples ; et Stack-overflow regorge d'astuces Jinja magiques.

Aux lignes 16 et 17 de `serverless.yml`, je mappe les deux paramètres du corps d'entrée aux paramètres d'entrée de l'action souhaitée. En option, vous pouvez également former une sortie de fonction à partir des résultats de l'action. Je vais rester simple pour l'instant (lignes 20 à 22) et garder d'autres astuces pour plus tard.

Pour garder la configuration séparée, j'ai créé un fichier `env.yml` et j'y ai mis mes paramètres de configuration :

```
# ./env.yml
# ATTENTION : Ne pas commiter sur Github :)
slack:
  admin_token: "xoxs-111111111111-..."
  organization: "my-team"
```

Ensuite, je l'ai utilisé dans `serverless.yml` comme ceci : `admin: ${file(env.yml):slack}`. Notez comment cette syntaxe place l'objet de la clé du fichier dans la clé de `serverless.yml`.

Ok, c'est tout ! La fonction est prête à s'envoler vers AWS avec `sls deploy`. Mais je vais y aller **doucement**. Étape par étape. Tout d'abord, je vais la packager localement.

```
sls package
```

La toute première fois prend beaucoup de temps car c'est le moment où le plugin installe ses dépendances d'exécution. Il récupère les images Docker depuis le Hub. Il installe les runners StackStorm — le code qui sait comment exécuter les packs StackStorm Exchange. Il récupère le pack `slack` depuis l'Exchange. Il installe les dépendances Python du pack `slack`. Il fait beaucoup de travail pour nous, et cela prend du temps. Bonne nouvelle : ce n'est que la première fois.

Oh, ai-je mentionné que vous devez être connecté ? Ou supposons-nous que la connexion internet est une denrée de base comme l'air que l'on respire et l'électricité ? Du moins avant que la FCC n'abroge la neutralité du net ? Donc oui, vous avez besoin d'une connexion internet pour vivre dans le monde Serverless.

Maintenant, exécutons cela localement.

```
sls stackstorm docker run --function InviteSlack --verbose \
--data \
'{"body": {"first_name": "Santa", "email": "santa@mad.russian.xmas.com"}}'
```

Les exécutions locales se font dans un conteneur — vous verrez la sortie CLI `Spin Docker container to run a function`. Cela prend un peu plus de temps, mais garantit que l'environnement d'exécution correspond très étroitement à AWS Lambda, donc mieux vaut prévenir que guérir.

Lorsque je débogue les transformations de paramètres d'entrée et de sortie, je ne veux peut-être pas appeler la fonction réelle, comme dans le cas de la limitation du débit de l'API Slack. Utilisez le paramètre `--passthrough` qui indique au plugin de faire une exécution à blanc (dry-run) et de sauter l'invocation de l'action.

Maintenant, nous sommes vraiment prêts. Déployons la fonction sur AWS et exécutons-la en mode « serverless ».

```
sls deploy
```

Cela prendra un certain temps — maintenant c'est serverless (et honnêtement, notre bundle est un peu volumineux, patience ! les développeurs du plugin sont actuellement occupés à résoudre d'autres problèmes, nous l'optimiserons dès que possible).

**ASTUCE DE PRO :** si quelque chose ne va pas à ce stade, il est fort probable que votre configuration AWS ne soit pas correcte. Revenez à « Préparation, étape 2 ». Lisez le document [Installation de Serverless](https://serverless.com/framework/docs/providers/aws/guide/installation/). Cherchez sur Google, Stack-overflow, le [canal Gitter](https://gitter.im/serverless/serverless) de Serverless ou le [Forum](https://forum.serverless.com/).

Vous pourriez être curieux de voir à quoi cela ressemble dans la console AWS. Si le PRO en vous dit « non, tu devrais rester cool et utiliser la CLI », ne l'écoutez pas. Faites-vous plaisir, ouvrez un navigateur et jetez un coup d'œil à votre Lambda. Pendant que vous y êtes, vous pourriez également inspecter l'endpoint API Gateway que `sls` a créé pour vous.

Mais pour le tester, nous allons retourner au terminal. Voici comment exécuter votre Lambda avec `sls` :

```
sls invoke --function InviteSlack --log --data '{"body": {"first_name": "Santa", "email": "santa@mad.russian.xmas.com"}}'
```

Enfin, faisons un POST sur l'endpoint de l'API. L'endpoint a été affiché à la fin de `sls deploy` et vous auriez dû en prendre note, mais ce n'est pas grave si vous ne l'avez pas fait : vous pouvez toujours l'obtenir en tapant `sls info`.

Vous, les amoureux de `curl`, allez-y, utilisez-le pour faire le POST ; assurez-vous de définir l'en-tête `Content-Type=application/json`. Moi, je vais frimer avec [httpie](https://httpie.org/), alias CURL pour les humains :

```
# NE PAS copier-coller ! Utilisez VOTRE endpoint !
```

```
http --json POST  https://VOTRE-ENDPOINT.amazonaws.com/dev/invite \
email=test@example.com first_name=Dmitri
```

Comment ça s'est passé ? Tout a fonctionné, du moins pour moi. Lançons une autre commande `sls` très utile pour vérifier les logs CloudWatch :

```
sls logs --function InviteSlack
```

Succès ! Et c'est la fin du premier épisode. C'est assez pour l'instant : c'est la période de Noël, allez-y doucement, profitez-en !

L'exemple de code jusqu'à présent est sur GitHub à l'adresse [1-add-first-action](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/1-add-first-action).

[**Épisode 2**](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) : **Ajouter plus d'actions**

J'espère que cela vous a aidé à apprendre quelque chose de nouveau, à trouver quelque chose d'intéressant ou a suscité de bonnes réflexions. N'hésitez pas à partager vos réflexions dans les commentaires ici, ou à m'envoyer un tweet [@dzimine](https://twitter.com/dzimine).