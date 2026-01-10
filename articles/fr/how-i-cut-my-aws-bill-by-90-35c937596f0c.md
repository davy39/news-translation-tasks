---
title: Comment j'ai réduit ma facture AWS de 90 % en passant au serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-30T09:41:04.000Z'
originalURL: https://freecodecamp.org/news/how-i-cut-my-aws-bill-by-90-35c937596f0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xJn9adGp0wgU4INAtwFxMA.jpeg
tags:
- name: AWS
  slug: aws
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai réduit ma facture AWS de 90 % en passant au serverless
seo_desc: 'By Avner Sorek

  In short, I was able to move my side project — an Express.JS application — from
  AWS Elastic Beanstalk to Lambda+APIG. It took me less than a day and it resulted
  in a ~90% reduction of costs.

  This could be beneficial for any non-mission...'
---

Par Avner Sorek

En bref, j'ai pu déplacer mon projet secondaire — une application Express.JS — d'AWS Elastic Beanstalk vers Lambda+APIG. Cela m'a pris moins d'une journée et a entraîné une réduction d'environ 90 % des coûts.

Cela pourrait être bénéfique pour toute application (ou environnement) non critique, et je crois que cela pourrait être un changement de jeu pour les projets secondaires et les petites entreprises.

Tout d'abord, pour être tout à fait transparent — l'application en question est un **projet secondaire** et n'est soumise à aucun accord de niveau de service ou à des exigences de performance. Il s'agit d'un site web appelé [libhive](https://www.libhive.com). libhive analyse le code dans le registre [npm](https://www.npmjs.com/) et trouve des exemples de packages utilisant d'autres packages. Il est construit en Node.JS avec ExpressJS, et soutenu par DynamoDB.

libhive reçoit un modeste nombre de 50 à 150 visites par jour. Il y a quelques mois, après avoir décidé de ne plus poursuivre ce projet, je voulais toujours le garder en vie — mais en minimisant les coûts de maintenance. Le site fonctionnait sur Elastic Beanstalk avec 2 instances micro, qui étaient opérationnelles 24h/24 et 7j/7 pour la redondance.

J'ai pu effectuer une transition très rapide vers AWS Lambda et API Gateway. Cela a été principalement grâce à [aws-serverless-express](https://github.com/awslabs/aws-serverless-express) d'AWS labs, qui adapte les applications ExpressJS à lambda presque sans effort. J'admets avoir une certaine expérience avec Lambda et APIG, mais la configuration n'a pas pris longtemps et a à peine nécessité des changements de code. Cela m'a pris moins d'une journée complète de travail.

Le graphique ci-dessus montre les coûts AWS (en USD) sur trois mois — avril était encore à 100 % Elastic Beanstalk, j'ai fait le changement pendant le mois de mai et juin était entièrement serverless. Les coûts d'avril étaient principalement liés à Elastic Compute — spécifiquement 18 $ pour deux instances t2.micro et 20 $ pour un load balancer "classique" — tout fonctionnant 24h/24 et 7j/7. Ces coûts ont été complètement réduits (je paie encore un peu pour certains volumes EBS). Pendant le mois de juin, j'ai eu 631 187 requêtes vers APIG — ce qui a coûté 2,21 $, et le même nombre de requêtes vers Lambda, résultant en 386 731 GB-secondes, qui tombent entièrement sous le niveau gratuit de Lambda — donc aucun coût n'a été engagé.

#### Réduction des coûts avec peu de travail — trop beau pour être vrai ?

Bien sûr. Passer à Lambda a un prix — le service est plus lent, et des "démarrages à froid" se produisent parfois. Cela est également dû à mon architecture Lambda — je fais tourner un petit monolithe dans une seule fonction Lambda, qui obtient des données de Dynamo et rend des vues HTML. Cela a rendu la migration super facile, mais est loin d'être une configuration serverless idéale.

### Ce que cela signifie pour vous ?

Si vous envisagez cela pour l'entreprise pour laquelle vous travaillez (ou que vous dirigez) — je ne recommanderais **pas** de déplacer des applications de production vers Lambda, surtout pas comme cela. Cependant — si vous exécutez plusieurs environnements de développement/test sur Elastic Beanstalk ou EC2, vous pourriez être en mesure de réduire significativement vos coûts pour ces environnements **non-production**, et dans les grandes équipes/entreprises — vous pourriez en avoir beaucoup, et ces coûts peuvent s'accumuler.

#### Bonne nouvelle pour les petits

Si vous êtes comme moi — un développeur avec un projet secondaire — ces coûts réduits pourraient faire une énorme différence. La capacité d'avoir plus qu'un site web statique en fonctionnement, à un dixième du coût, peut être un véritable changement de jeu. **Les barrières à l'entrée pour les produits logiciels deviennent de plus en plus faibles — et je crois que c'est une bonne nouvelle pour tout le monde.**

_Avez-vous une histoire similaire ? Une question ? Souhaitez-vous que j'écrive un article plus technique sur les détails du processus de migration ? Faites-le moi savoir dans les commentaires ci-dessous. Merci pour votre lecture._