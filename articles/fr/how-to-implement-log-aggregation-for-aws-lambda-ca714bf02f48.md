---
title: Comment implémenter l'agrégation de logs pour AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-31T09:00:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-log-aggregation-for-aws-lambda-ca714bf02f48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gV8PnF93tCU_3wmWxBxn4A.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: Comment implémenter l'agrégation de logs pour AWS Lambda
seo_desc: 'By Yan Cui

  Dur­ing the exe­cu­tion of a Lamb­da func­tion, what­ev­er you write to std­out
  (for example, using console.log in Node.js) will be cap­tured by Lamb­da and sent
  to Cloud­Watch Logs asyn­chro­nous­ly in the back­ground. And it does this wi...'
---

Par Yan Cui

Pendant l'exécution d'une fonction Lambda, tout ce que vous écrivez dans stdout (par exemple, en utilisant `console.log` en Node.js) sera capturé par Lambda et envoyé à CloudWatch Logs de manière asynchrone en arrière-plan. Et cela se fait sans ajouter de surcharge à votre temps d'exécution de fonction.

Vous pouvez trouver tous les logs de vos fonctions Lambda dans CloudWatch Logs. Il y a un groupe de logs unique pour chaque fonction. Chaque groupe de logs se compose ensuite de nombreux flux de logs, un pour chaque instance de la fonction en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/kjX-pl1TyZV2Pd45dYwGv2NlJoEQCBL5ygIc)

Vous pouvez envoyer des logs à CloudWatch Logs vous-même via l'opération [PutLogEvents](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html). Ou vous pouvez les envoyer à votre service d'agrégation de logs préféré tel que Splunk ou Elasticsearch.

Mais, rappelez-vous que **tout doit être fait pendant l'invocation d'une fonction**. Si vous effectuez des appels réseau supplémentaires pendant l'invocation, vous paierez pour ce temps d'exécution supplémentaire. Vos utilisateurs devront également attendre plus longtemps pour que l'API réponde.

Ces appels réseau supplémentaires peuvent ajouter seulement 10 à 20 ms par invocation. Mais vous avez des microservices, et une seule action utilisateur peut impliquer plusieurs appels API. Ces 10 à 20 ms par appel API peuvent s'accumuler et ajouter plus de 100 ms à votre latence côté utilisateur, ce qui est suffisant pour [réduire les ventes de 1% selon Amazon](https://blog.gigaspaces.com/amazon-found-every-100ms-of-latency-cost-them-1-in-sales/).

Donc, ne faites pas cela !

Au lieu de cela, traitez les logs de CloudWatch Logs après coup.

Dans la console CloudWatch Logs, vous pouvez sélectionner un groupe de logs et choisir de diffuser les données directement vers le service Elasticsearch hébergé par Amazon.

![Image](https://cdn-media-1.freecodecamp.org/images/D6vXlFNTuMjMQcM9h19AyK2lgEMeVHAi6y-Z)

Cela est très utile si vous utilisez déjà le service Elasticsearch hébergé. Mais si vous évaluez encore vos options, lisez [cet article](https://read.acloud.guru/things-you-should-know-before-using-awss-elasticsearch-service-7cd70c9afb4f) avant de décider d'utiliser l'Elasticsearch hébergé par AWS.

Vous pouvez également diffuser les logs vers une fonction Lambda. Il existe même plusieurs modèles de fonctions Lambda pour pousser les logs CloudWatch vers d'autres services d'agrégation de logs.

Clairement, c'est quelque chose que beaucoup de clients d'AWS ont demandé.

![Image](https://cdn-media-1.freecodecamp.org/images/UY-1KkwDlx2RcjeGTyzncQ9cCZknZGvsaMNd)
_Vous pouvez trouver des modèles pour envoyer les logs CloudWatch vers Sumologic, Splunk et Loggly directement._

Vous pouvez utiliser ces modèles pour vous aider à écrire une fonction Lambda qui enverra les logs CloudWatch à votre service d'agrégation de logs préféré. Mais voici quelques autres choses à garder à l'esprit.

Lorsque vous créez une nouvelle fonction Lambda, elle créera un nouveau groupe de logs dans CloudWatch Logs. Vous voulez éviter un processus manuel pour abonner les groupes de logs à votre fonction d'envoi de logs.

Au lieu de cela, activez CloudTrail, puis configurez un motif d'événement dans CloudWatch Events pour invoquer une autre fonction Lambda lorsqu'un groupe de logs est créé.

Vous pouvez faire cette configuration ponctuelle dans la console CloudWatch.

![Image](https://cdn-media-1.freecodecamp.org/images/031B7URKw4Nxa9j7hdWfWNv9odyBFe4UmPXF)
_Correspondez à l'appel API CreateLogGroup dans CloudWatch Logs et déclenchez une fonction Lambda subscribe-log-group. Cette fonction abonnera le nouveau groupe de logs à la fonction d'envoi de logs._

Si vous travaillez avec plusieurs comptes AWS, vous devriez éviter de rendre la configuration manuelle. Avec le [Framework Serverless](https://serverless.com/framework/), vous pouvez configurer la source d'événement pour cette fonction `subscribe-log-group` dans le fichier `serverless.yml`.

![Image](https://cdn-media-1.freecodecamp.org/images/DHuTPlIAXa-X614O4KinqB80M74H5I5KDgI3)

Une autre chose à garder à l'esprit est que **vous devez éviter d'abonner le groupe de logs de la fonction** `ship-logs` **à lui-même.** Cela créera **une boucle d'invocation infinie** et c'est une leçon _douloureuse_ que vous voulez éviter.

Une dernière chose.

Par défaut, lorsque Lambda crée un nouveau groupe de logs pour votre fonction, la politique de rétention est définie sur `Never Expire`. Cela est excessif, car le [coût de stockage des données](https://aws.amazon.com/cloudwatch/pricing/) peut s'accumuler avec le temps. C'est également inutile si vous envoyez déjà les logs ailleurs !

![Image](https://cdn-media-1.freecodecamp.org/images/nzZDmkdrPAmbAh8z7QFDHd-XUxtnQFzGdsTT)
_Par défaut, les logs de vos fonctions Lambda sont conservés dans CloudWatch Logs pour toujours_

Nous pouvons appliquer la même technique ci-dessus et ajouter une autre fonction Lambda pour mettre à jour automatiquement la politique de rétention à quelque chose de plus raisonnable.

![Image](https://cdn-media-1.freecodecamp.org/images/gvD8ZPfcTRQq4TeV4RW1gE0S0momJHWHDEGO)
_Voici une fonction Lambda pour mettre à jour automatiquement la politique de rétention des logs à 30 jours._

Si vous avez déjà beaucoup de groupes de logs existants, envisagez d'écrire des [scripts](https://github.com/theburningmonk/lambda-logging-demo/blob/master/process_all.js) ponctuels pour les mettre à jour. Vous pouvez le faire en [parcourant](https://github.com/theburningmonk/lambda-logging-demo/blob/master/process_all.js#L21-L35) tous les groupes de logs avec l'appel API [DescribeLogGroups](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html).

Si vous êtes intéressé à appliquer ces techniques vous-même, j'ai préparé un simple [projet de démonstration](https://github.com/theburningmonk/lambda-logging-demo) pour vous. Si vous suivez les instructions dans le README et déployez les fonctions, tous les logs de vos fonctions Lambda seront livrés à [Logz.io](https://logz.io/).