---
title: La réalité de l'exécution d'une application Node en production sur AWS Elastic
  Beanstalk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-21T16:08:21.000Z'
originalURL: https://freecodecamp.org/news/the-reality-of-running-a-production-node-app-on-aws-elastic-beanstalk-55c78b5dad0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sUif8A5X81bOpkLssOTbcg.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
seo_title: La réalité de l'exécution d'une application Node en production sur AWS
  Elastic Beanstalk
seo_desc: 'By Jared Nutt

  Lessons learned from 2 years of running a production Node app on AWS’ ELB platform


  _Photo by [Unsplash](https://unsplash.com/photos/1ZZ96uESRJQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="...'
---

Par Jared Nutt

#### Leçons tirées de 2 ans d'exécution d'une application Node en production sur la plateforme ELB d'AWS

![Image](https://cdn-media-1.freecodecamp.org/images/6DRA1yuoVD7jj2JoXxmeLHLuf2atDKrotLtz)
_Photo par [Unsplash](https://unsplash.com/photos/1ZZ96uESRJQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Shane Rounce</a> sur <a href="https://unsplash.com/search/photos/technology?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Introduction

Soyons honnêtes, le [calculateur de prix AWS](https://calculator.s3.amazonaws.com/index.html) est confus. Cela est en partie dû à la méthode de paiement _à la carte_ proposée par AWS. Cela rend difficile la fourniture d'un bon devis à un client. Espérons que cet article puisse éclairer sur le coût de l'exécution d'une application, ainsi que sur quelques moyens de réduire les coûts.

### Le coût réel de l'exécution d'une application

Je gère une application web Node sur ELB depuis environ deux ans. La première année était géniale, ils vous donnaient tout gratuitement (pour la plupart) ! Après cela, vous devez commencer à payer pour des choses, comme les instances EC2.

Cet article se concentrera sur les exigences spécifiques de mon application, qui est une application Express basée sur Node hébergée sur Elastic Beanstalk.

Pour plus de détails sur la construction, voir mon article précédent [ici](https://medium.freecodecamp.org/how-to-deploy-a-node-js-app-to-the-aws-elastic-beanstalk-f150899ed977).

#### Décomposition

Voici ce que j'exécute actuellement sur AWS :

Environnement EBS unique (Région Ouest des États-Unis) :

* 1 Classic Load Balancer
* 1 instance EC2 t2.micro
* Bucket S3 qui contient des images (7 Go au moment de l'écriture)
* 1 Zone hébergée Route 53

**18 $** (Load Balancer) + **5 $** (EC2 avec une RI) + **0,50 $** (Route 53) + **0,17 $** (S3) + **0,21 $** (Transfert de données) = Environ **25 $** par mois.

De plus, j'héberge une base de données MongoDB ailleurs, donc si vous prévoyez d'héberger une base de données sur AWS, cela entraînera des coûts supplémentaires. Décomposons les différents coûts.

#### Load Balancer

C'est la partie la plus chère de la pile. Cela coûte :

* 0,025 $ par heure de Classic Load Balancer (ou partie d'heure)
* 0,008 $ par Go de données traitées par un Classic Load Balancer

Cela signifie que si vous exécutez votre application 24 heures sur 24, cela coûtera environ 18 $ + frais de données, chaque mois.

#### Instance EC2

Les instances EC2 à la demande sont plus chères qu'elles ne devraient l'être. Pour économiser de l'argent ici, reportez-vous à la section ci-dessous sur les instances EC2 réservées. Au cas où vous vous poseriez la question, cela coûterait 8,40 $ pour exécuter le même type d'instance EC2 que mentionné ci-dessus, à la demande.

#### S3

J'ai quelques buckets S3. Un pour ma page d'accueil statique, un pour stocker des images et un pour stocker la version de l'application. Autant que je sache, ELB crée automatiquement celui pour gérer les versions de l'application.

Le S3 est assez bon marché, donc je ne m'inquiète pas trop de essayer de réduire les coûts, mais il existe des moyens d'économiser de l'argent via leur système [Glacier](https://aws.amazon.com/glacier/).

#### Base de données

J'héberge ma base de données MongoDB chez mLab, qui va bientôt disparaître. Je mettrai donc à jour cela lorsque j'aurai compris combien cela va réellement coûter une fois que je serai forcé de passer à Atlas de Mongo.

### Instances EC2 réservées

Parlons des Instances Réservées (RI). Le système de facturation convolué d'Amazon est la partie la plus confuse de la gestion de quoi que ce soit sur AWS. Les Instances Réservées peuvent atténuer une partie du coût, mais sont beaucoup trop confuses.

Après beaucoup de lectures et de discussions avec le service client d'AWS, voici ce que j'ai plus ou moins compris.

Tout d'abord, il existe deux façons différentes de réserver l'endroit où se trouve la RI : Régionale et Zone de Disponibilité. Régionale signifie qu'elle est spécifique à l'une des régions principales, par exemple us-west-2 (Oregon). La zone de disponibilité (AZ) est spécifique à une zone au sein de cette région, par exemple us-west-2**a** (Oregon).

J'ai acheté une RI dans us-west-2 et elle a été automatiquement appliquée à mon instance exécutée dans cette zone. Si vous en achetez une dans l'AZ, elle ne s'appliquera qu'à l'AZ spécifique, par exemple us-west-2a, donc si ELB lance une instance EC2 dans us-west2b, vous n'avez pas de chance.

De plus, il existe des types "standard" et "convertibles" de RI. Je ne suis pas sûr à 100 % de ce que cela signifie, mais d'après ce que je comprends, convertible est plus flexible sur ce que vous pouvez échanger, mais plus cher.

Enfin, il existe trois types de modes de paiement : Sans frais initiaux, frais initiaux partiels, Tous les frais initiaux. C'est assez simple, vous payez soit rien, soit une partie, soit tout lorsque vous réservez l'instance. Il n'y a pas d'avantage en termes de coût, que je puisse voir. Cependant, en tant que nouveau compte, vous ne pouvez probablement pas opter pour l'option sans frais initiaux.

Selon le support AWS :

> Les Instances Réservées (RI) sans frais initiaux peuvent poser un risque de facturation significatif pour les nouveaux comptes, car elles constituent une obligation contractuelle de payer mensuellement pour toute la durée de la RI. Pour cette raison, les nouveaux comptes et les comptes peu utilisés ne peuvent pas souscrire à des RI sans frais initiaux jusqu'à ce qu'un historique de facturation réussi soit établi avec nous.

Vous pourriez rencontrer cette erreur si vous essayez d'acheter une RI sans frais initiaux.

> Erreur : Votre quota actuel ne vous permet pas d'acheter le nombre requis d'instances réservées (Service : AmazonEC2 ; Code de statut : 400 ; Code d'erreur : ReservedInstancesLimitExceeded ;)

Avertissement : Pour une raison quelconque, il faut un certain temps pour que l'instance réservée "prenne effet", ce qui signifie que le premier jour du mois coûte toujours plus cher. Je ne suis pas sûr de la raison, mais si je la découvre, je mettrai à jour cela. Voir le graphique ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/JNI-ha2AnV7fhXmn8AbusMNAY33UW6mug6lW)

### Points douloureux

Ce ne sont que quelques plaintes mineures concernant l'EBS global, que j'ai décidé d'inclure en addendum à mon article original, au cas où vous seriez curieux.

#### Les mises à jour automatiques ne sont pas vraiment automatiques

Les versions de Node ne s'alignent pas d'une version à l'autre.

Veuillez vous reporter à l'étape ci-dessous pour savoir comment je gère les changements de versions Linux lorsque Node ne fonctionne pas.

#### Exécuter plus d'un environnement

Avoir un environnement de développement et un environnement de production en cours d'exécution en même temps est facile, mais c'est cher. Cela double le coût, en fait. Par conséquent, je détruit généralement l'environnement de développement dès que j'ai terminé avec lui.

#### La documentation est horrible

AWS est trop grand pour son propre bien. C'est en partie pour cela que j'écris ceci. Il était vraiment difficile de trouver des réponses à mes besoins spécifiques.

### Comment je gère les mises à jour

J'ai deux instances séparées de mon dépôt Git installées sur mon ordinateur portable. J'en ai une pour le développement et une pour la production.

J'utilise l'environnement de développement pour, eh bien, développer ! C'est assez simple. J'utilise le dossier de production uniquement dans le but de tirer les mises à jour de la branche principale de Git, d'exécuter ma configuration webpack et de déployer sur le serveur de production.

La raison pour laquelle ils sont séparés est que je peux maintenir des configurations Elastic Beanstalk séparées et ne pas avoir à m'inquiéter de déployer au mauvais endroit.

#### Mises à jour ne nécessitant pas de changement d'environnement Linux

Pour les mises à jour ne nécessitant aucun changement dans l'environnement Linux, c'est aussi simple que d'exécuter `eb deploy` dans le terminal. C'est incroyable et cela prend environ 10 minutes pour se propager.

#### Mises à jour nécessitant un changement d'environnement Linux

Occasionnellement, vous voudrez mettre à jour l'environnement Linux mais vous ne pourrez pas le faire parce qu'AWS est incroyablement stupide (je suis sûr qu'il y a une raison) et ne permet que certaines versions de Node sur chaque build Linux. Pour cela, c'est un peu plus compliqué, mais gérable.

1. Poussez vers la configuration de production sous le nouvel environnement. La dernière fois que j'ai fait cela, j'ai simplement créé une nouvelle instance via `eb create prod-1`. Cela fera ce qu'il faut et déployera votre application dans un nouvel environnement.
2. Assurez-vous que toutes vos mises à jour fonctionnent. Cela semble assez évident, mais c'est un bon moment pour s'assurer qu'il n'y a pas eu de problèmes avec la nouvelle build.
3. Assurez-vous que vos variables d'environnement sont configurées correctement. Cela fait un peu partie de la version précédente, mais assurez-vous que vous tirez de la bonne base de données, ou autre.
4. Assurez-vous que votre load balancer a le même certificat SSL (si applicable). Fait amusant, si vous essayez d'accéder à une instance ELB en https sans certificat, cela échouera !
5. Échangez les instances. Enfin, après que tout semble bon à aller, il y a un bouton dans la console pour échanger les URLs des instances. FACILE. Vous n'avez pas à changer quoi que ce soit dans Route 53, il fait tout pour vous.

Donc, voilà. Comment gérer vos mises à jour. Assez facile.

### Réflexions finales

Si vous avez des suggestions pour le rendre moins cher/plus facile, je serais ravi de les entendre. J'aime la discussion sur les outils et les options autant que le prochain développeur !

Sur ce, je vous laisse avec ceci : Bon codage !