---
title: Comment construire et déployer un beau site portfolio personnel avec AWS S3,
  Route53 et CloudFront ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T21:03:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-a-beautiful-personal-portfolio-site-with-aws-s3-route53-and-cloudfront-8827975129ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lkRw8tZ_QI_tDfz0Tagufg.jpeg
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment construire et déployer un beau site portfolio personnel avec AWS
  S3, Route53 et CloudFront ?
seo_desc: 'By Nicholas Vincent-Hill

  This is a step-by-step guide to creating a responsive static billboard/portfolio
  site, deploying it to the web with AWS, and serving it securely with HTTPS.

  This guide is designed for beginner and intermediate-level software ...'
---

Par Nicholas Vincent-Hill

_Ceci est un guide étape par étape pour créer un site statique responsive de type billboard/portfolio, le déployer sur le web avec AWS, et le servir de manière sécurisée avec HTTPS._

Ce guide est conçu pour les ingénieurs logiciels et les développeurs web de niveau débutant et intermédiaire cherchant une manière facile de créer un site personnel pour moins cher que les services payants comme SquareSpace ou d'autres constructeurs de sites. Les exigences techniques de base incluent une connaissance de HTML/CSS/JS, npm et Git (le processus avancé de création de site utilise Gatsby.js qui nécessite une connaissance de React.js et GraphQL).

Les seules exigences économiques sont les frais de zone hébergée AWS Route53 (0,50 $/mois) et le coût d'acquisition d'un domaine (j'ai loué nickvh.tech pour 25 $ pour cinq ans auprès de get.tech). Netlify est également une option gratuite. Le temps estimé est de quatre à cinq heures selon les compétences et l'expérience individuelles.

Ce guide vous permettra, en tant que développeur, de contrôler tous les aspects de la conception, du développement et du déploiement de votre site.

#### **Étape 1 — Créez votre site personnel (la manière facile ou la manière difficile)**

**Voici la manière facile :** allez [ici](https://html5up.net/) et choisissez un modèle HTML/CSS/JS entièrement responsive, super personnalisable et 100 % gratuit (sous [Creative Commons](https://html5up.net/license)). Téléchargez-le et personnalisez-le/construisez-le jusqu'à ce que vous l'aimiez !

Créez un `package.json` en appelant `npm init` dans le répertoire racine de votre projet choisi. Assurez-vous de faire `git init`, d'ajouter toutes les informations non publiques à `.gitignore`, et d'écrire de bons messages de commit.

**Voici la manière difficile :** utilisez Gatsby.js pour construire un site statique et une PWA ultra-rapide à partir de zéro. Ceci n'est pas un tutoriel Gatsby.js (de nombreux excellents tutoriels peuvent être trouvés [ici](https://www.gatsbyjs.org/tutorial/)) et nécessite une connaissance de React.js et GraphQL. Un certain nombre de modèles de démarrage peuvent être trouvés [ici](https://www.gatsbyjs.org/starters/?v=2) (j'ai utilisé le modèle HTML5UP "strata" comme point de départ pour [nickvh.tech](https://www.nickvh.tech/)).

Testez et développez votre site web jusqu'à ce que vous en soyez satisfait et que vous souhaitiez le partager avec le monde. Nous allons construire un pipeline de développement continu avec soit Grunt soit le plugin `gatsby-plugin-s3` plus tard, afin que les révisions/futurs déploiements soient rapides et faciles.

#### **Étape 2 — Obtenez un domaine**

Des sites comme [https://get.tech](https://get.tech/) ou [https://www.namecheap.com](https://www.namecheap.com/) offrent des prix très attractifs pour les domaines. J'ai attendu une promotion et j'ai obtenu [https://nickvh.tech](https://get.tech/) pour 25 $ pour cinq ans. Alternativement, achetez un domaine .dev auprès de [Google](https://domains.google/#/).

#### **Étape 3 — Créez un compte AWS**

Créez un [compte AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). Cette étape est assez simple. Les nouveaux comptes bénéficient de services gratuits pendant un an — détaillés [ici](https://aws.amazon.com/free/). Cela nécessite que vous ayez une carte de crédit active enregistrée auprès d'AWS. **Soyez conscient des implications de sécurité et ne poussez pas accidentellement vos identifiants AWS sur le web public.**

#### **Étape 4 — Configurez les buckets AWS S3**

> _Amazon Simple Storage Service (Amazon S3) est un service de stockage d'objets qui offre une scalabilité, une disponibilité des données, une sécurité et des performances de premier ordre. Cela signifie que les clients peuvent l'utiliser pour stocker et protéger n'importe quelle quantité de données pour une gamme de cas d'utilisation, tels que les sites web, les applications mobiles, la sauvegarde et la restauration, les archives, les applications d'entreprise, les appareils IoT et l'analyse de big data._

AWS S3 est l'endroit où votre site statique résidera ; il y a quelques choses à faire pour configurer cela correctement.

Tout d'abord, créez un bucket ; AWS S3 et Route53 ne fonctionnent correctement que si le nom de votre bucket et le nom de domaine correspondent précisément — nommez votre bucket mysite.domain (c'est-à-dire nickvh.tech). Assurez-vous de définir les permissions correctement ; le public doit pouvoir lire depuis le bucket mais pas y écrire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nDKOVzwkcQamFyaTVWYDHw.png)
_Assurez-vous de donner un accès public en lecture à votre bucket_

Ensuite, naviguez vers « Properties » et configurez AWS S3 pour servir statiquement `index.html` (voir ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jU6929oqVXSINz3o9LHJZg.png)

Créez un bucket (également avec un accès public en lecture activé) nommé www.mysite.domain ([www.nickvh.tech](http://www.nickvh.tech) dans mon cas) et redirigez vers l'adresse du bucket principal (voir ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*3r7p-HOEkXp97fOOdA58dA.png)

Ensuite, créez `aws-keys.json` dans le répertoire racine de votre projet :

Voici un [guide](https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-) pour trouver votre ID de clé d'accès AWS et votre clé secrète.

**N'oubliez pas d'ajouter** `aws-keys.json` **à votre** `.gitignore` **! L'un de mes étudiants a accidentellement poussé ses identifiants AWS sur Github, a été attaqué de manière programmatique et a encouru ~1,3k $ de frais en quelques heures.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vb3KlOUa_yZJ_yyZEz9zEg.png)
_Ne laissez pas cela vous arriver !_

#### Étape 5 — Téléchargez votre site sur AWS S3 avec Grunt ou `gatsby-plugin-s3`

> _Grunt est un exécuteur de tâches JavaScript, un outil utilisé pour effectuer automatiquement des tâches fréquentes telles que la minification, la compilation, les tests unitaires et le linting. Il utilise une interface de ligne de commande pour exécuter des tâches personnalisées définies dans un fichier._

Si vous choisissez la manière facile de créer votre site, vous pouvez utiliser Grunt pour télécharger les fichiers de votre site terminé vers votre bucket AWS S3.

```
npm install grunt grunt-aws-s3 --save-dev
```

Créez un `Gruntfile.js` :

Ajoutez ceci à l'objet scripts de votre `package.json`.

```
"deploy": "grunt deploy"
```

Maintenant, chaque fois que vous souhaitez déployer une nouvelle version de production de votre site, exécutez simplement `npm run deploy`. Cela ne POST/PUT que les fichiers modifiés vers AWS S3 — réduisant le nombre de requêtes pour lesquelles vous devez payer (les nouveaux comptes AWS bénéficient de 2 000 requêtes PUT gratuites/mois pendant la première année).

Alternativement — si vous avez construit votre site avec Gatsby.js, oubliez Grunt et utilisez simplement `gatsby-plugin-s3` pour le déploiement de sites statiques. J'ai écrit un script npm `npm run ship` qui construit le bundle de production et le télécharge vers AWS S3 - `gatsby build && gatsby-plugin-s3 deploy`. Le code de mon site Gatsby peut être trouvé [ici](https://github.com/nvincenthill/portfolio_v3).

#### **Étape 6 — Créez une distribution avec AWS CloudFront**

> _Amazon CloudFront est un service de réseau de diffusion de contenu (CDN) rapide qui livre de manière sécurisée des données, des vidéos, des applications et des API aux clients dans le monde entier avec une faible latence, des vitesses de transfert élevées, le tout dans un environnement convivial pour les développeurs._

Créez une nouvelle distribution CloudFront (en suivant approximativement ces [docs AWS](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-https-requests-s3/)). Assurez-vous de spécifier correctement les **Noms de domaine alternatifs (CNAMEs)** et de demander un certificat SSL personnalisé pour activer HTTPS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dKBOI5qkk-JZUoTs4KOrHQ.png)

Spécifiez également l'**Objet racine par défaut** comme `index.html`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YdRYM7Ygu_pHCViM6ARgYA.png)
_N'oubliez pas de spécifier l'objet racine par défaut_

Cliquez sur Créer une origine pour lier votre bucket S3 à votre distribution CloudFront. Spécifiez le **Nom de domaine d'origine** comme `YOUR_S3_BUCKET_NAME.s3.amazonaws.com`. Ne restreignez pas l'accès au bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q2B1TcFuw2o9vvkXOXwnjQ.png)
_Origine de la distribution CloudFront_

Créez un nouveau comportement et définissez la **Stratégie de protocole du spectateur** sur « Rediriger HTTP vers HTTPS ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*y7BAWIzgm-TCa_jdCBTKqA.png)
_Comportements de la distribution CloudFront_

Vous pouvez également personnaliser les réponses d'erreur — je redirige les erreurs 404 vers une page 404.html personnalisée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CyDZcVNq6o3FtA1fDGOjDw.png)
_Pages d'erreur CloudFront_

#### **Étape 7 — Redirigez le trafic vers votre nouveau CDN avec AWS Route53**

> _Amazon Route 53 est un service web de système de noms de domaine (DNS) hautement disponible et scalable dans le cloud. Il est conçu pour offrir aux développeurs et aux entreprises un moyen extrêmement fiable et économique de router les utilisateurs finaux vers des applications Internet en traduisant des noms comme [www.example.com](http://www.example.com) en adresses IP numériques comme 192.0.2.1 que les ordinateurs utilisent pour se connecter les uns aux autres._

Maintenant, nous devons connecter votre nom de domaine (mysite.domain) à votre distribution CloudFront afin que, lorsqu'un utilisateur fait une requête vers votre domaine, il reçoive votre `index.html` et le reste de votre site statique (en atteignant votre nouveau CDN).

Ouvrez la console AWS Route53 et créez une nouvelle **Zone hébergée**. Voici quelques [docs AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-inactive.html) utiles pour vous aider à démarrer.

**Assurez-vous de mettre à jour les serveurs de noms pour le domaine que vous avez acheté. Utilisez la méthode fournie par le bureau d'enregistrement du domaine que vous avez acheté pour changer les serveurs de noms du domaine (utilisez les quatre serveurs de noms Route53 trouvés dans l'ensemble de records NS — Serveur de noms).**

Créez un nouvel ensemble de records et définissez la cible de l'alias sur votre distribution AWS CloudFront (voir ci-dessous). Assurez-vous de le nommer yoursite.domain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gDQ-77A2FQ0n3Qlr47vcaQ.png)
_Alias de votre distribution CloudFront_

Les modifications des serveurs de noms de domaine prennent du temps à se propager, alors assurez-vous d'attendre quelques minutes avant de tenter d'accéder à votre site via votre nouveau domaine.

#### Étape 8 — Profitez de la gloire de votre site nouvellement déployé ! (ou dépanner les problèmes)

Vous l'avez fait ! Profitez de votre beau nouveau site portfolio déployé sur le web mondial. Consultez [mon site](http://nickvh.tech) que j'ai construit et déployé en utilisant cette stack technique ; j'ai connecté le formulaire de contact avec AWS Lambda en utilisant [ce guide](https://dev.to/adnanrahic/building-a-serverless-contact-form-with-aws-lambda-and-aws-ses-4jm0).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lkRw8tZ_QI_tDfz0Tagufg.jpeg)
_Profitez de votre nouveau beau site portfolio ! [html5up.com](http://html5up.com" rel="noopener" target="_blank" title=")_

> _Lire ensuite :_

> [Scrabblr — Un jeu React avec react-dnd et react-flip-move](https://hackernoon.com/scrabblr-a-react-game-with-react-dnd-and-react-flip-move-40cfaac786e2)