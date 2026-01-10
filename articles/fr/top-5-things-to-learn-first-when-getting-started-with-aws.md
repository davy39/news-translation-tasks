---
title: 'AWS Cheatsheet : Les 5 choses principales à apprendre en premier pour commencer
  avec Amazon Web Services'
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-07T16:04:12.000Z'
originalURL: https://freecodecamp.org/news/top-5-things-to-learn-first-when-getting-started-with-aws
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/aws.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: 'AWS Cheatsheet : Les 5 choses principales à apprendre en premier pour
  commencer avec Amazon Web Services'
seo_desc: "AWS has taken the tech community by storm. It’s easily sold as one of the\
  \ most reliable providers with an exhaustive list of services from object storage\
  \ to machine learning. \nBut it can easily be overwhelming for someone new to the\
  \ cloud. Where shou..."
---

AWS a conquis la communauté technologique. Il est facilement présenté comme l'un des fournisseurs les plus fiables avec une liste exhaustive de services allant du stockage d'objets à l'apprentissage automatique. 

Mais cela peut facilement être écrasant pour quelqu'un qui est nouveau dans le cloud. Par où commencer lorsque vous essayez d'apprendre AWS ?

* [Stockage d'objets avec AWS S3](#heading-stockage-dobjets-avec-aws-s3)
* [Héberger et déployer un site web statique avec AWS S3 et CloudFront](#heading-heberger-et-deployer-un-site-web-statique-avec-aws-s3-et-cloudfront)
* [Créer une fonction serverless avec AWS Lambda](#heading-creer-une-fonction-serverless-avec-aws-lambda)
* [Lancer un serveur géré avec AWS EC2](#heading-lancer-un-serveur-gerer-avec-aws-ec2)
* [Apprendre les acronymes AWS](#heading-apprendre-les-acronymes-aws) (sérieusement)

## Stockage d'objets avec AWS S3

S3 est la solution d'AWS pour le stockage d'objets. D'un point de vue très simple, les buckets S3 sont un peu comme un disque dur dans le cloud pour les fichiers statiques. Cela signifie que bien que vous puissiez télécharger presque n'importe quoi sur S3, une fois qu'il y est, vous ne pouvez pas vraiment faire grand-chose avec, sauf le télécharger ou l'écraser.

Mais S3 est bon marché et le stockage est un service dont presque tous les sites web ont besoin. Cela fait de S3 un service vraiment précieux qui est une partie de facto de toute architecture moderne.

Vous avez quelques images simples que vous voulez stocker ? Déposez-les dans un bucket S3. Vous avez quelques PDF que vous générez pour des rapports ? Stockez-les et accédez-y depuis un bucket S3.

Bien que vous ne puissiez pas exécuter le code, les navigateurs fonctionnent en téléchargeant des fichiers comme JavaScript puis en exécutant ces fichiers par eux-mêmes, ce qui en fait une combinaison parfaite pour les actifs web statiques ou les photos.

### Ressources pour apprendre

* [Amazon S](https://aws.amazon.com/s3/)3 (aws.amazon.com)
* [Comment télécharger des fichiers et des dossiers vers un bucket S3 ?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html) (docs.aws.amazon.com)

## Héberger et déployer un site web statique avec AWS S3 et CloudFront

Prenons ce que nous venons d'apprendre sur AWS S3 un peu plus loin. Puisque les navigateurs téléchargent finalement des fichiers pour les utiliser, nous pouvons utiliser S3 comme moyen d'héberger des sites web statiques avec une simple case à cocher !

S3 offre une [option de configuration](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/static-website-hosting.html) qui nous permet de servir un site web à partir d'un simple bucket. Il configure le bucket pour permettre les requêtes HTTP que le navigateur peut reconnaître, ce qui fait que l'application [Gatsby](https://www.gatsbyjs.org/) que vous venez de compiler ou même un simple fichier HTML est un candidat parfait pour S3.

CloudFront intervient à la fin et fournit le CDN (ou réseau de diffusion de contenu) pour notre site web. Là où S3 nous permet d'héberger le site web dans un bucket, CloudFront se place devant le bucket en tant que couche de réseau distribué en cache qui permet à notre site web d'atteindre les navigateurs de nos visiteurs plus rapidement que directement depuis S3.

### Ressources pour apprendre

* [Amazon S](https://aws.amazon.com/s3/)3 (aws.amazon.com)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront/) (aws.amazon.com)
* [Comment héberger et déployer un site web statique ou une application JAMstack sur AWS S3 et CloudFront](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/) (freecodecamp.org)
* [Comment héberger et déployer un site web statique ou une application JAMstack sur AWS S3 & CloudFront](https://www.youtube.com/watch?v=1lDGDzmbQWg) (youtube.com)
* [Hébergement d'un site web statique sur Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) (docs.aws.amazon.com)

## Créer une fonction serverless avec AWS Lambda

Si vous êtes nouveau dans le monde serverless, l'idée n'est pas qu'il n'y ait littéralement aucun serveur. C'est juste qu'en tant que client, vous n'avez pas à gérer ces serveurs.

La plupart des fournisseurs de cloud ont une sorte de solution pour les services serverless, mais l'une des plus populaires est l'utilisation des fonctions Lambda d'AWS.

Les fonctions Lambda sont ce à quoi elles ressemblent, une fonction, mais elles s'exécutent dans le cloud. Vous n'avez pas à vous soucier des ressources qui font fonctionner cette fonction, juste de l'environnement dans lequel vous voulez écrire, comme node ou python.

C'est puissant et bon marché ! Cela aide à abstraire la logique en une seule fonction dans un cloud qui peut être mis à l'échelle autant que vous le souhaitez (à condition que les services tiers auxquels elle fait appel puissent être mis à l'échelle autant).

Que pouvez-vous faire avec Lambda ? Voici quelques exemples :

* Lire et écrire des données vers S3 ou une base de données
* Traiter des données avec une logique complexe
* Créer une application web en utilisant [Express](https://expressjs.com/)

Il y a beaucoup de potentiel que la familiarisation avec AWS Lambda peut débloquer !

### Ressources pour apprendre

* [AWS Lambda](https://aws.amazon.com/lambda/) (aws.amazon.com)
* [Apprendre AWS Lambda à partir de zéro](https://egghead.io/playlists/learn-aws-lambda-from-scratch-d29d?af=atzgap) (egghead.io)
* [Tutoriel sur les fonctions AWS Lambda Cron Job – Comment planifier des tâches](https://www.freecodecamp.org/news/using-lambda-functions-as-cronjobs/) (freecodecamp.org)

## Lancer un serveur géré avec AWS EC2

L'un des grands arguments de vente d'AWS est que nous pouvons faire toutes nos opérations de calcul dans notre cloud. Et cela s'applique à tout !

Au cœur d'AWS se trouve Amazon [EC2](https://aws.amazon.com/ec2/) (Elastic Compute Cloud) qui, dans sa forme la plus simple, est un serveur dans le cloud.

En utilisant EC2, vous pouvez lancer un serveur avec une variété de configurations disponibles où vous pouvez faire presque tout ce que vous voulez. Vous pouvez commencer petit si vous ne voulez faire que des opérations simples ou vous pouvez mettre à l'échelle à la fois verticalement et horizontalement pour vous donner beaucoup de puissance de traitement pour vos opérations gourmandes en données.

Parmi les choses que vous pouvez faire avec EC2, on trouve :

* Lancer une nouvelle instance de Wordpress ou de votre CMS préféré
* Gérer un serveur web personnalisé
* Traiter des données scientifiques nécessitant beaucoup de calculs

### Ressources pour apprendre

* [Amazon EC2](https://aws.amazon.com/ec2/) (aws.amazon.com)
* [Comment lancer un serveur distant sur AWS](https://www.freecodecamp.org/news/getting-started-with-server-administration-on-aws/) (freecodecamp.org)
* [Exécuter un bureau virtuel Ubuntu](https://ubuntu.com/tutorials/ubuntu-desktop-aws) (ubuntu.com)
* [De zéro à AWS EC2 pour la science des données](https://medium.com/@junseopark/from-zero-to-aws-ec2-for-data-science-62e7a22d4579) (medium.com)

## Apprendre les acronymes AWS

Sérieusement. En tant qu'ingénieur front-end qui construit des sites web depuis longtemps, l'une des choses les plus précieuses pour moi afin d'être productif avec le reste de mon équipe a été d'apprendre les acronymes des différents services AWS.

S3 ? EC2 ? CF ? Je peux imaginer beaucoup de mauvaises réponses à cela, mais être simplement capable de savoir ce que ces choses signifient me rend capable de suivre la conversation.

Même si je travaille principalement sur le front-end, je devrais avoir une compréhension des concepts de l'endroit où nous stockons et hébergeons nos applications statiques. Cela signifie que je devrais savoir que S3 est le Simple Storage Service et qu'il agit presque comme un disque dur dans le cloud pour les fichiers statiques.

Mais apprendre les acronymes ne signifie pas nécessairement que vous devez savoir comment les services fonctionnent. 

Bien que les choses à apprendre que j'ai listées ci-dessus soient bonnes à savoir pratiquement, si vous êtes uniquement concentré sur le front-end d'une application, vous ne devriez pas être censé comprendre comment les services ELB (Elastic Load Balancer) ou EMR (Elastic MapReduce) fonctionnent. Mais être capable de savoir CE QU'ils sont est extrêmement utile lorsque vous travaillez avec le reste de votre équipe.

### Ressources pour apprendre les acronymes AWS

Il existe de nombreuses façons d'apprendre les acronymes. Vous pouvez simplement aller sur le [site web d'AWS](https://aws.amazon.com/products/?nc2=h_ql_prod) et parcourir la liste de tous les services, mais ce n'est probablement pas la méthode la plus efficace.

Il existe une tonne de ressources disponibles pour apprendre les fondamentaux d'AWS, y compris un [cours gratuit de 4 heures pour le cours AWS Certified Cloud Practitioner](https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/) de freecodecamp.org. 

Bien que vous n'ayez pas à passer l'examen pour apprendre le matériel, c'est définitivement un bonus si vous voulez faire l'investissement, car c'est une autre chose que vous pouvez ajouter à votre CV, ce qui vous rendra finalement plus précieux.

Mais commencez par vous concentrer sur les services dont vous entendez le plus parler ou ceux que votre équipe utilise. Cela vous aidera grandement à devenir plus efficace en tant que membre de votre équipe.

## Autres outils pour vous aider à gérer AWS

Bien que vous puissiez certainement être productif en travaillant avec chaque service AWS individuellement, il existe une tonne d'outils qui peuvent faciliter encore plus le travail avec ces services.

### AWS SDK

Directement d'AWS, le [AWS SDK](https://aws.amazon.com/tools/). Il existe en plusieurs langues, comme le [AWS SDK pour Javascript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/) que vous pouvez utiliser [via npm](https://www.npmjs.com/package/aws-sdk).

Avec le SDK, vous pouvez interfacer les services AWS directement dans votre application.

### Serverless Framework

Les outils autour du monde serverless sont encore jeunes, mais le [Serverless Framework](https://www.serverless.com/) est l'un des outils qui ont persisté le plus longtemps pour aider à construire des applications serverless.

Serverless, à ne pas confondre avec le concept, vous aidera à lancer des applications web en gérant le déploiement des services AWS que vous souhaitez.

### AWS Lightsail

Bien que vous puissiez lancer une instance EC2 pour faire ce que vous voulez, [AWS Lightsail](https://aws.amazon.com/lightsail/) peut prendre en charge une partie du travail lourd pour vous.

Lightsail propose des services de type cliquer-et-lancer comme le lancement d'un nouveau serveur Wordpress ou d'un environnement LAMP.

### AWS Amplify

Si vous voulez un outil pour gérer vos services et simplement être productif, [AWS Amplify](https://aws.amazon.com/amplify/) peut vous aider à construire rapidement des applications web et mobiles avec une variété de services.

Cela inclut l'authentification, le stockage de données, l'analytique, l'apprentissage automatique, et bien plus encore.

## Avez-vous déjà travaillé avec AWS ?

Quel est votre service préféré ? [Faites-le moi savoir sur Twitter !](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3a5 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f3fb Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>