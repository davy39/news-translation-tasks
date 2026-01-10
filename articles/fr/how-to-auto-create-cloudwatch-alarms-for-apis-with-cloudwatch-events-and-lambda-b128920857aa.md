---
title: Comment créer automatiquement des alarmes CloudWatch pour les API avec CloudWatch
  Events et Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T17:57:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-auto-create-cloudwatch-alarms-for-apis-with-cloudwatch-events-and-lambda-b128920857aa
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2Xre5dsJRMQqIrZA.png
tags:
- name: automation
  slug: automation
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer automatiquement des alarmes CloudWatch pour les API avec
  CloudWatch Events et Lambda
seo_desc: 'By Yan Cui

  In a pre­vi­ous post, I dis­cussed how to auto-sub­scribe a Cloud­Watch Log Group
  to a Lamb­da func­tion using Cloud­Watch Events. The benefit of this is that we
  don’t need a man­u­al process to ensure all Lamb­da logs are forwarded to our...'
---

Par Yan Cui

Dans un [article précédent](https://theburningmonk.com/2017/08/centralised-logging-for-aws-lambda/), j'ai discuté de la manière d'abonner automatiquement un **groupe de journaux CloudWatch** à une fonction Lambda en utilisant **CloudWatch Events**. L'avantage de cela est que nous n'avons pas besoin d'un processus manuel pour garantir que tous les journaux Lambda sont transférés à notre service d'agrégation de journaux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TVbE2siAsoz5JPxp.png)

Bien que cela soit utile en soi, cela ne fait qu'effleurer la surface de ce que nous pouvons faire. **CloudTrail** et **CloudWatch Events** facilitent l'automatisation de nombreuses tâches opérationnelles quotidiennes, avec l'aide de **Lambda**, bien sûr ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*2Xre5dsJRMQqIrZA.png)

Je travaille beaucoup avec **API Gateway** et **Lambda**. Lorsque vous créez une nouvelle API ou apportez des modifications, il y a plusieurs choses que vous devez faire :

* Activer les **métriques détaillées** pour l'étape de déploiement
* Configurer un tableau de bord dans CloudWatch, affichant le nombre de requêtes, les latences et les comptes d'erreurs
* Configurer des **alarmes CloudWatch** pour les latences P99 et les comptes d'erreurs

Étant donné que ces étapes sont manuelles, elles sont souvent oubliées.

Avez-vous déjà oublié de mettre à jour le tableau de bord après avoir ajouté un nouveau point de terminaison à votre API ? Et vous êtes-vous également souvenu de configurer une alarme de latence P99 sur ce nouveau point de terminaison ? Et les alarmes sur le nombre d'erreurs 4XX ou 5xx ?

La plupart des équipes avec lesquelles j'ai travaillé ont certaines conventions autour de ces éléments, mais elles n'ont pas de moyen de les appliquer. Le résultat est que la convention est appliquée de manière inégale et ne peut pas être fiable. Je trouve que cette approche ne s'adapte pas à la taille de l'équipe.

Cela fonctionne lorsque vous êtes une petite équipe. Tout le monde a une compréhension partagée et la discipline nécessaire pour suivre la convention. Lorsque l'équipe grandit, vous avez besoin d'automatisation pour aider à appliquer ces conventions.

Heureusement, nous pouvons automatiser ces étapes manuelles en utilisant le même modèle. Dans l'unité [Monitoring](https://livevideo.manning.com/module/38_9_5/) de mon cours [Production-Ready Serverless](https://bit.ly/production-ready-serverless), j'ai démontré comment vous pouvez faire cela en 3 étapes simples :

* **CloudTrail** capture la requête **CreateDeployment** vers **API Gateway**
* **CloudWatch Events** correspond à ce modèle de requête capturée
* **Lambda** active les métriques détaillées et crée des alarmes pour chaque point de terminaison

Si vous utilisez le framework [Serverless](https://serverless.com/framework/docs/), vous pourriez avoir une fonction qui ressemble à ceci :

Quelques points à noter à partir du code ci-dessus :

* J'utilise le plugin [serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) pour donner à la fonction un rôle IAM sur mesure
* La fonction a besoin de la permission `apigateway:PATCH` pour activer les métriques détaillées
* La fonction a besoin de la permission `apigateway:GET` pour obtenir le nom de l'API et les points de terminaison REST
* La fonction a besoin de la permission `cloudwatch:PutMetricAlarm` pour créer les alarmes
* Les variables d'environnement spécifient les sujets SNS pour les **alarmes CloudWatch**

L'événement capturé ressemble à ceci :

Nous pouvons trouver le `restApiId` et le `stageName` dans l'attribut `detail.requestParameters`. C'est tout ce dont nous avons besoin pour déterminer quels points de terminaison existent et donc quelles alarmes nous devons créer.

À l'intérieur de la fonction de gestion, que vous pouvez trouver [ici](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/functions/create-alarms.js), nous effectuons quelques étapes :

* Activer les métriques détaillées avec un appel `updateStage` à API Gateway
* Obtenir la liste des points de terminaison REST avec un appel `getResources` à API Gateway
* Obtenir le nom de l'API REST avec un appel `getRestApi` à API Gateway
* Pour chacun des points de terminaison REST, créer une alarme de latence P99 dans l'espace de noms `AWS/ApiGateway`

![Image](https://cdn-media-1.freecodecamp.org/images/0*4jj_jV1dNe8XMyEE.png)

Maintenant, chaque fois que je crée une nouvelle API, j'aurai des **alarmes CloudWatch** pour m'alerter lorsque la latence du 99e percentile pour un point de terminaison dépasse 1 seconde, pendant 5 minutes consécutives.

Tout cela, avec seulement quelques lignes de code ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*rXmrxT-GCnEEprlK.png)

Vous pouvez aller plus loin et avoir d'autres fonctions Lambda pour :

* Créer des alarmes CloudWatch pour les erreurs 5xx pour chaque point de terminaison
* Créer un tableau de bord CloudWatch pour l'API

Voilà ! Un modèle utile pour automatiser les tâches opérationnelles manuelles.

Et avant de me parler du plugin [ACloudGuru AWS Alerts Serverless](https://github.com/ACloudGuru/serverless-plugin-aws-alerts) des gens d'ACloudGuru, oui, je le connais. Il a l'air bien, mais il s'agit finalement de quelque chose que le développeur doit se souvenir de faire.

Cela nécessite de la discipline.

Mon expérience me dit que vous ne pouvez jamais compter sur la discipline. C'est pourquoi je préfère avoir une plateforme en place qui générera ces alarmes à la place.