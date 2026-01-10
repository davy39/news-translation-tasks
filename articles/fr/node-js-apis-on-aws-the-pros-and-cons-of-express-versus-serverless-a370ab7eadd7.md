---
title: API Node.js sur AWS — les avantages et inconvénients d'Express versus Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T15:49:44.000Z'
originalURL: https://freecodecamp.org/news/node-js-apis-on-aws-the-pros-and-cons-of-express-versus-serverless-a370ab7eadd7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tgtdC3Ks4buR3XfITJMxsQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: API Node.js sur AWS — les avantages et inconvénients d'Express versus Serverless
seo_desc: 'By William Woodhead

  Recently I have been playing around with Serverless + AWS lambda and I have to say,
  I have been awestruck.

  Over the past few years I have almost exclusively used Express and AWS EC2 (and
  more recently Docker) to build JavaScript R...'
---

Par William Woodhead

Récemment, j'ai exploré [Serverless](https://serverless.com/) + AWS Lambda et je dois dire que j'ai été impressionné.

Au cours des dernières années, j'ai presque exclusivement utilisé [Express](http://expressjs.com/) et [AWS EC2](https://aws.amazon.com/ec2/) (et plus récemment [Docker](https://www.docker.com/)) pour construire des API REST JavaScript.

Cet article présente les avantages et inconvénients d'[Express](http://expressjs.com/) et de [Serverless](https://serverless.com/) et explique pourquoi il était logique pour notre équipe chez [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness) de passer à Serverless. Cet article s'adresse aux équipes techniques cherchant à déployer et gérer des API Node.js sur AWS (ou similaires).

![Image](https://cdn-media-1.freecodecamp.org/images/CxXXE330wof5O5qpQa2L0rh7AAzRduCQJbRt)
_Collage légèrement agressif de leurs logos. Désolé._

#### TL;DR

Passer d'[Express](http://expressjs.com/) à [Serverless](https://serverless.com/) a complètement transformé notre livraison au cours des 6 derniers mois.

**Avantages** : coût réduit | scalabilité et monitoring de déploiement prêts à l'emploi | développement ultra-rapide.

**Inconvénients** : perte de contrôle | l'énigmatique runtime [Lambda](https://aws.amazon.com/lambda/) | écosystème jeune | pas de déploiement sans temps d'arrêt prêt à l'emploi.

#### Qu'est-ce qu'Express | Qu'est-ce que Serverless ?

Express est un package [Node.js](https://nodejs.org) qui, à sa base, est une abstraction bien conçue du module http(s) natif de Node.js.

Serverless, en revanche, est un ensemble d'outils qui interagit avec des plateformes cloud, telles qu'AWS ou [GCP](https://cloud.google.com/), pour déployer et gérer des API.

D'après ces descriptions, on peut voir qu'Express et Serverless sont vraiment très différents — peut-être trop différents pour être comparés. Cependant, la raison pour laquelle je les compare est que Express et Serverless peuvent tous deux être utilisés pour écrire des API Node.js. Alors, plongeons dans quelques comparaisons :

#### Le fichier index

En général, je préfère écrire du code plutôt que de la configuration. Cela signifie que vous pouvez exécuter, tester et déboguer votre travail.

Avec Express, votre fichier index est du code JavaScript. C'est un fichier déclaratif vraiment expressif. Avec Serverless, c'est de la configuration yml, je le crains.

Voici le fichier index.js _Hello World_ d'Express :

```
const express = require('express');const handler = require('./handler');
```

```
const app = express();app.get('/hello-world', handler.helloWorld);app.listen(3000, () => console.log('Écoute sur le port 3000'));
```

Voici le fichier index.yml _Hello World_ de Serverless :

```
service: hello-worldprovider:    name: aws    runtime: nodejs6.10functions:  helloWorld:    handler: handler.helloWorld    events:      - http:        path: hello-world        method: get
```

Assez similaire, mais je préfère personnellement l'approche basée sur les middlewares d'Express. Pour moi, c'est plus lisible et plus facile à tester et à déboguer.

#### Courbe d'apprentissage

C'est un sujet délicat car cela dépend de ce que vous essayez d'accomplir :

* Si vous êtes un hobbyiste Node.js et que vous voulez apprendre à configurer un serveur localhost sur votre propre ordinateur, Express est fait pour vous. C'est un excellent package pour expérimenter, la documentation "get started" sur le site est excellente, et vous pouvez facilement commencer à jouer avec les intricacies de l'architecture basée sur les événements de Node.js.
* Si vous essayez de déployer et de gérer des API Node.js robustes et scalables, la courbe d'apprentissage est définitivement plus facile avec Serverless. Cela est dû au fait que Serverless traite de nombreux problèmes complexes liés au cloud dès la sortie de la boîte. Ceux-ci incluent le déploiement, la surveillance et la provision d'infrastructure, pour n'en nommer que quelques-uns.

#### Opérations — déploiement, mise à l'échelle, journalisation, surveillance...

![Image](https://cdn-media-1.freecodecamp.org/images/bJdnwDUal7mdHyigzm81e-f0nuD3CC0-usJE)
_Engrenages pour représenter les opérations, évidemment._

C'est là que Serverless se distingue vraiment. Express n'est pas conçu pour gérer toutes les complexités des architectures basées sur le cloud par lui-même. Si vous utilisez Express, vous aurez besoin d'aide d'autres packages :

Pour le déploiement et la mise à l'échelle, vous pourriez utiliser [Docker](https://www.docker.com/), [Kubernetes](https://kubernetes.io/), [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) ou d'autres services AWS.

Pour la journalisation, la surveillance et la gestion des erreurs, vous pourriez utiliser [New Relic](https://newrelic.com/), [Datadog](https://www.datadoghq.com/), [Pingdom](https://www.pingdom.com/), et ainsi de suite.

Vous voyez l'idée. Express est un excellent outil de bas niveau pour construire des API, mais vous devez apprendre un tas d'autres packages pour que votre API prospère dans le monde moderne basé sur le cloud. C'est génial si vous voulez configurer vos propres architectures et avoir un contrôle complet.

Avec Serverless, vous obtenez tellement de choses dès la sortie de la boîte. Non pas du package Serverless lui-même, mais parce que Serverless peut interagir automatiquement avec tous les services de votre plateforme cloud. Par exemple, juste avec l'exemple index.yml _Hello World_ que nous avons vu ci-dessus, vous obtiendriez par défaut :

* Surveillance avec AWS Lambda
* Journalisation avec [AWS Cloudwatch](https://aws.amazon.com/cloudwatch/)
* Mise à l'échelle automatique avec AWS Lambda
* Déploiement avec Serverless et [AWS Cloudformation](https://aws.amazon.com/cloudformation/)

C'est absolument incroyable pour les équipes techniques en mouvement rapide qui veulent se concentrer sur l'écriture de code applicatif, et non sur la gestion de l'infrastructure.

_Veuillez noter : Actuellement avec Serverless, nous n'atteignons pas le déploiement sans temps d'arrêt. Je pense qu'il est possible de l'atteindre avec AWS CodeDeploy, mais nous permettons actuellement à l'API de tomber pendant une seconde ou deux._

#### Coût

Pour quiconque construit des API robustes et hautement disponibles sur le cloud, le coût est une considération massive. Serverless a réduit nos coûts d'un montant incroyable :

Une machine Linux EC2 T2-Medium sur AWS vous coûte environ 33 $ par mois pour fonctionner. Nous utilisions 3 de ces machines avant de passer à Serverless.

Avec Serverless + AWS Lambda, vous obtenez 1 million de requêtes gratuitement chaque mois.

Chez Pilcro, nous n'avons pas encore atteint ce benchmark, donc nous avons déjà économisé plus de cent dollars par mois. Avec Serverless et Lambda, **nous pouvons maintenant exécuter nos API gratuitement**.

#### Le runtime AWS Lambda

![Image](https://cdn-media-1.freecodecamp.org/images/NKpXucW4pWZyIhbcklwDRHL8RUzTVVBJxZBz)
_Logo AWS Lambda_

L'un des inconvénients de l'utilisation de Serverless est que vos fonctions d'API sont exécutées dans le runtime AWS Lambda. Cela signifie que vous n'êtes jamais tout à fait sûr de ce qui se passe.

Vous devez également gérer certaines particularités de la fonction AWS Lambda, comme les objets _event_ et _context_ étranges qui sont injectés dans vos gestionnaires :

```
function awsLambdaHandler(event, context, callback) {  ...}
```

```
function expressHandler(req, res, next) {  ...}
```

Je préfère beaucoup le modèle de middleware _req, res, next_ d'Express. Il me semble plus logique et compréhensible.

Une autre particularité est que pour que AWS Lambda exécute vos gestionnaires, ils doivent être chargés dans un contexte d'exécution. Cela peut prendre un certain temps. Les fonctions sont mises en cache dans le contexte d'exécution pendant un certain temps, donc souvent la première requête à une Lambda prendra plus de temps que les requêtes suivantes. Cela peut être irritant si votre API est utilisée de manière peu fréquente.

_Note de côté_ : L'une des grandes choses à propos du runtime AWS Node.js Lambda est qu'ils ont le binaire [ImageMagick](https://www.imagemagick.org) installé. Vous pouvez donc faire de la manipulation d'images dans vos fonctions Lambda dès la sortie de la boîte !

#### Conclusion

Ce n'est pas vraiment une comparaison entre Express et Serverless. C'est une reconnaissance que — dans la quête d'API cloud robustes et scalables — des packages comme Serverless offrent tellement de choses dès la sortie de la boîte, que continuer à utiliser Express (avec d'autres outils) semble être beaucoup de travail et d'apprentissage.

Chez [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness), nos API sont assez simples et standard. Elles sont composées de requêtes REST simples et de quelques fonctions complexes de manipulation d'images.

Parce que nos API sont si simples, la décision d'utiliser Serverless et Lambda était simple — nos principaux moteurs étaient le **coût**, la **scalabilité** et la **vitesse de développement**.

**Coût** parce que... coût.

**Scalabilité** parce que nous sommes construits sur G-Suite, donc nous devions pouvoir nous adapter extrêmement rapidement et efficacement.

**Vitesse de développement** parce que nous devions livrer Pilcro en 6 mois avec une petite équipe technique.

Serverless nous a apporté ces trois avantages, ce qui a complètement transformé notre livraison au cours des 6 derniers mois. L'écosystème de Serverless est encore jeune, donc il y aura probablement beaucoup de développements dans ce domaine au cours des 12 prochains mois.

#### Étapes pour vous aider à décider si vous devez utiliser Serverless

1. À quel point vos API sont-elles complexes ? Avez-vous besoin de la configuration de bas niveau et de la proximité que vous obtenez en utilisant Express ?
2. Comment gérez-vous actuellement le déploiement, la mise à l'échelle et la surveillance ? Êtes-vous satisfait de votre solution ? À quelle vitesse un développeur nouvellement embauché pourrait-il apprendre toutes les différentes parties de votre architecture ?
3. Pourriez-vous économiser de l'argent en passant à Serverless ?

_Si vous avez aimé cette histoire, veuillez ? et partagez-la avec d'autres. Veuillez également consulter ma société [pilcro.com](https://www.pilcro.com/?utm_source=medium&utm_medium=serverless&utm_campaign=awareness). Pilcro est un logiciel de marque pour G-Suite — pour les marketeurs et les agences de marque._