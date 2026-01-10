---
title: Comment choisir une stratégie de déploiement pour votre application Next.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-01T14:19:51.000Z'
originalURL: https://freecodecamp.org/news/deployment-strategies-for-nextjs-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Grey-Minimalist-Tips-Blog-Banner--1-.png
tags:
- name: deployment
  slug: deployment
- name: Next.js
  slug: nextjs
seo_title: Comment choisir une stratégie de déploiement pour votre application Next.js
seo_desc: 'By Tobenna Okeke

  Many projects are migrating from React to Next.js in 2023. So now''s the right time
  to understand an important step in creating a Next.js application: deployment.

  Deploying a Next.js application is an essential step in the lifecycle o...'
---

Par Tobenna Okeke

De nombreux projets migrent de React vers Next.js en 2023. C'est donc le bon moment pour comprendre une étape importante dans la création d'une application Next.js : le déploiement.

Le déploiement d'une application Next.js est une étape essentielle dans le cycle de vie de votre produit web. Et comme diverses stratégies de déploiement existent, choisir la bonne peut être un défi.

Cet article discutera des différentes stratégies et pratiques de déploiement pour les applications Next.js. Nous explorerons les forces de chaque stratégie, y compris l'hébergement statique, les fonctions serverless, la conteneurisation et le déploiement sur serveur traditionnel.

Nous aborderons également les pratiques essentielles pour optimiser le processus de déploiement et améliorer les performances et la fiabilité de votre application Next.js.

Voici ce que nous couvrirons dans ce tutoriel :

* [Pourquoi le déploiement est-il important dans le cycle de vie du développement ?](#heading-pourquoi-le-deploiement-est-il-important-dans-le-cycle-de-vie-du-developpement)
* [Stratégies de déploiement pour les projets Next.js](#heading-strategies-de-deploiement-pour-les-projets-nextjs)
* [Option #1 : Hébergement statique](#heading-option-1-hebergement-statique)
* [Option #2 : Fonctions serverless](#heading-option-2-fonctions-serverless)
* [Option #3 : Conteneurisation](#heading-option-3-conteneurisation)
* [Option #4 : Rendu côté edge (ESR)](#heading-option-4-rendu-cote-edge-esr)
* [Bonnes pratiques pour le déploiement d'applications Next.js](#heading-bonnes-pratiques-pour-le-deploiement-dapplications-nextjs)
* [Bonnes pratiques pour la gestion des variables d'environnement dans une application Next.js](#heading-bonnes-pratiques-pour-la-gestion-des-variables-denvironnement-dans-une-application-nextjs)
* [Conclusion](#heading-conclusion)

Cet article fournira des informations complètes qu'un développeur débutant ou intermédiaire peut utiliser pour déployer une application Next.js fluide.

# Pourquoi le déploiement est-il important dans le cycle de vie du développement ?

Déployer un projet est plus important que de le démarrer. Une application doit résoudre des problèmes pour ses utilisateurs – mais comment vos utilisateurs peuvent-ils résoudre leurs problèmes avec votre application si vous ne la déployez pas (la rendant disponible au monde) ? Le processus de déploiement peut faire échouer tout votre travail acharné si vous manquez une étape.

Le processus de développement implique :

* Mettre votre application sur une plateforme d'hébergement.
* La configurer.
* S'assurer qu'elle fonctionne sans problème pour les utilisateurs du monde entier.

Voici quelques raisons pour lesquelles le déploiement est essentiel :

* Accessibilité des utilisateurs : L'utilisabilité d'un projet est un critère important. Le déploiement est l'étape finale, sans laquelle vos utilisateurs ne peuvent pas interagir avec votre application. Les utilisateurs doivent pouvoir accéder à votre projet et utiliser ses fonctionnalités sans problème.
* Test avec de vrais utilisateurs : Déployer votre projet est le seul moyen de vérifier s'il résout le problème souhaité. Cela vous permet de tester et de résoudre les bugs provenant de vrais utilisateurs et de données, et de corriger l'application pour qu'elle fonctionne comme prévu.
* Évolutivité et fiabilité : Déployer votre application permet à votre produit de s'adapter, de gérer plus d'utilisateurs et d'augmenter le trafic. L'évolutivité et la fiabilité sont des raisons pour lesquelles vous devez utiliser le processus de déploiement approprié, car il pourrait compromettre vos efforts si votre produit ne peut pas gérer une augmentation soudaine du trafic.
* Intégration et déploiement continus (CI/CD) : Le processus de déploiement met en œuvre un flux de travail transparent. Avec les pratiques CI/CD, votre base de code est toujours testée, validée et déployée dans l'environnement de production. Cela facilite également l'ajout de fonctionnalités et évite les erreurs.

# Stratégies de déploiement pour les projets Next.js

Voici un aperçu des différentes options de déploiement pour les flux de travail et les exigences des produits Next.js.

## Option #1 : Hébergement statique

![https://www.cosmicjs.com/blog/static-site-generators-explained-in-5-minutes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r6o809j5b8acjhov7nur.png)
_Diagramme illustrant l'hébergement statique_

Un simple site web statique avec peu ou pas de rendu côté serveur peut être hébergé sur des plateformes d'hébergement fixes comme Vercel, Netlify, Amazon Simple Storage Service (AWS S3), GitHub Pages ou Surge.

Next.js génère des fichiers HTML statiques pendant le processus de construction, et vous pouvez l'héberger sur l'une des plateformes ci-dessus.

### Avantages de l'hébergement statique pour les applications Next.js

* Performances améliorées : Les applications Next.js génèrent des fichiers HTML pré-rendus pendant le processus de construction, et elles prennent en charge la génération de site statique (SSG). Si vous hébergez de manière statique, le fichier pré-rendu peut être mis en cache sur un réseau de diffusion de contenu (CDN) mondial, améliorant les performances en chargeant rapidement.
* Évolutivité : Une application hébergée de manière statique avec un CDN permettra la distribution mondiale des fichiers, améliorant ainsi l'évolutivité et réduisant la charge sur le serveur d'origine. Le CDN garantira des temps de chargement rapides même lors de pics de trafic pour les utilisateurs du monde entier.
* Sécurité : L'hébergement statique a peu ou pas de traitement côté serveur, ce qui réduit la surface d'attaque. De plus, les fichiers statiques sont moins vulnérables aux attaques courantes des applications web.
* Charge serveur réduite : La charge de travail du serveur d'origine est réduite car Next.js a des fichiers HTML pré-rendus.
* Avantages de la mise en cache : Puisque les fichiers statiques sont mis en cache sur le CDN, cela réduira le nombre de requêtes faites au serveur d'origine.
* Rentabilité : L'hébergement statique n'a pas besoin de gestion de base de données ou de traitement côté serveur. Il sera moins cher pour les petites applications et les sites web avec peu de trafic.

### Cas d'utilisation de l'hébergement statique pour les applications Next.js

L'hébergement statique est excellent pour les applications Next.js avec peu de rendu et de maintenance. 
Voici quelques cas d'utilisation à considérer :

1. Pages de destination : Il s'agit d'un site web simple utilisé pour des campagnes marketing ou des lancements de produits. Une page de destination Next.js doit être hébergée de manière statique pour garantir une gestion fluide du trafic élevé et un temps de chargement rapide.
2. Sites de contenu et portfolios : Les sites web avec plusieurs contenus statiques comme les blogs, les sites de documentation et les sites de base de connaissances bénéficient de performances améliorées et d'un temps de chargement réduit lorsqu'ils utilisent l'hébergement statique.
3. Prototypes et démonstrations : Les applications Next.js peuvent être utilisées par les développeurs pour des démonstrations internes et des prototypages avec des clients, car elles peuvent être facilement déployées.
4. Applications monopages (SPA) : Les SPA contiennent généralement des contenus dynamiques, mais la partie statique peut être pré-rendue et hébergée de manière statique pour améliorer le temps de chargement.

### Exemples de plateformes d'hébergement statique pour les applications Next.js

Plusieurs plateformes d'hébergement statique peuvent facilement héberger une application Next statique. 

1. Vercel : Il s'agit d'une plateforme d'hébergement couramment utilisée. Elle fournit des fonctionnalités intégrées et une facilité d'utilisation, ce qui la rend idéale pour l'hébergement d'applications Next.js statiques et serverless. Vercel offre un support CDN mondial, une intégration rapide et un déploiement automatique.
2. Firebase Hosting : Cela est fourni par Google Firebase et prend en charge les sites statiques de Next.js. Il prend également en charge les sites web dynamiques mais offre un hébergement statique transparent.
3. Netlify : Cette option dispose de l'une des configurations les plus simples et d'une interface conviviale pour les développeurs. Elle prend en charge le déploiement continu, les fonctions serverless et la gestion des formulaires.
4. GitHub Pages : Les pages GitHub sont les plus faciles à configurer. Vous créez une branche gh-pages, et cela fonctionnera si vous avez une source HTML, mais Next.js ne le fait pas. Vous pouvez donc héberger votre application Next.js en pré-rendant les pages pendant le processus de construction.
5. Amazon Simple Storage Service (AWS S3) : Cela peut être utilisé pour héberger des sites web statiques. Vous devez configurer un bucket S3 pour l'hébergement de sites web statiques, puis utiliser AWS Cloudfront comme CDN pour de meilleures performances.
6. Render : Cette plateforme d'hébergement cloud héberge des sites statiques et couvre les fonctions serverless. Elle permet aux sites statiques Next.js d'être hébergés.

### Comment déployer une application Next.js sur une plateforme d'hébergement statique

Déployer votre application Next.js statique sur une plateforme d'hébergement statique est simple. Voici les étapes à suivre :

#### Étape 1 : Codez votre application Next.js

Tout d'abord, vous devez terminer votre code Next.js et vous assurer qu'il est prêt pour le déploiement. Il doit être testé et fonctionner comme prévu.

Ensuite, initialisez votre code et commitez-le dans un dépôt Git.

#### Étape 2 : Choisissez une plateforme d'hébergement

Maintenant, vous devez simplement choisir une plateforme d'hébergement comme celles listées ci-dessus. Vous n'aurez besoin que d'une petite configuration puisque c'est statique.

Vous pouvez vous inscrire pour la version gratuite ou passer à la version pro.

#### Étape 3 : Connectez votre dépôt

Lorsque vous vous connectez à la plateforme d'hébergement, vous trouverez soit "Connecter un dépôt" soit "Importer un projet" juste après avoir cliqué sur Créer un nouveau projet.

![connecting repo to vercel](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ba4lvf52137fy3o0441u.png)
_Importation d'un dépôt_

Donnez à la plateforme d'hébergement la permission d'accéder à votre dépôt Git, et choisissez le dépôt avec votre application Next.js.

#### Étape 4 : Configurez les paramètres de déploiement

Maintenant, vous devez sélectionner la branche que vous souhaitez déployer. Choisissez la commande de construction. Pour une application Next.js, la commande de construction est généralement `npm run build` ou `yarn build`.

Sélectionnez le répertoire de sortie. Puisque nous déployons une application Next.js, la sortie est typique, `out` ou `build`.

#### Étape 5 : Déployez votre application

Maintenant, il est temps de déployer votre application – la plateforme gérera l'ensemble du processus. Et ensuite, elle construit automatiquement les fichiers statiques de votre application.

Pour déployer l'application, cliquez sur le bouton `Deploy` ou l'équivalent présenté par la plateforme d'hébergement.

#### Étape 6 : Domaine personnalisé

Maintenant, vous pouvez configurer votre domaine personnalisé à partir d'un tiers ou utiliser la version pro si disponible.

Configurez les enregistrements DNS de votre domaine personnalisé pour pointer vers la plateforme d'hébergement. (_Cette étape est facultative._)

#### Étape 7 : Vérifiez et testez

Une fois le déploiement terminé, vous recevrez une URL de la plateforme d'hébergement.

Visitez l'URL pour confirmer que votre application Next.js est déployée avec succès et fonctionne comme prévu. Cela devrait ressembler à ceci :

![deployment tab](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/irf72o479w0p3o74wmuy.png)
_Page de déploiement sur Vercel_

#### Étape 8 : Déploiement continu

Enfin, c'est un bon moment pour mettre en œuvre une stratégie de déploiement continu si la plateforme d'hébergement statique le permet. Cela permettra à vos modifications sur le dépôt Git d'être automatiquement déployées. 

Pour ce faire, vous devez implémenter des webhooks pour déclencher des constructions et des déploiements lorsque du nouveau code est poussé.

Passons en revue les étapes pour configurer le déploiement continu sur GitHub :

1. Allez dans les paramètres du dépôt du projet que vous souhaitez déployer.

![set the repo](https://www.freecodecamp.org/news/content/images/2023/08/image-172.png)
_Paramètres du dépôt_

2. Sélectionnez Webhooks sur le côté gauche

![webhooks setting for repo](https://www.freecodecamp.org/news/content/images/2023/08/image-173.png)
_Sélectionnez les webhooks_

3. Cliquez sur `Add webhook` ou `New workflow`

4. Configurez le webhook

Fournissez l'URL où la plateforme d'hébergement enverra le webhook.

![webhook](https://www.freecodecamp.org/news/content/images/2023/08/image-174.png)
_Configuration du webhook_

5. Sélectionnez un événement pour déclencher

Comme vous pouvez le voir, il y a trois événements, et celui que nous devons choisir est `Just the Push event`. Cela déclenchera les développements lorsque du nouveau code est poussé.

6. Ajoutez un secret

Le secret est un mot de passe qui ajoute une couche supplémentaire de sécurité. Il sera également demandé par la plateforme d'hébergement.

7. Enregistrez et testez

Enregistrez et testez comment les webhooks sont déclenchés lorsque vous poussez du nouveau code.

## Option #2 : Fonctions serverless

Les projets Next.js peuvent être intégrés avec des fonctions serverless telles que AWS Lambda en utilisant la fonction serverless de Vercel ou serverless. Avec cette option, les développeurs peuvent créer des fonctionnalités dynamiques côté serveur sans se soucier de la gestion de l'infrastructure serveur traditionnelle. 

Cette option de déploiement aide à gérer la soumission de formulaires, les appels API et d'autres calculs côté serveur de manière évolutive et économique.

Il existe quelques plateformes qui prennent en charge l'option de fonction serverless :

* Amazon Web Services Lambda
* Azure Functions
* Google Cloud Function
* IBM Cloud Functions
* Alibaba Cloud Function
* Vercel

Ces plateformes simplifient la gestion et permettent aux développeurs de se concentrer davantage sur le codage que sur la configuration.

### Avantages des fonctions serverless pour les applications Next.js

L'utilisation de la fonction serverless pour héberger une application Next.js présente plusieurs avantages qui améliorent les performances, et ils incluent :

* Évolutivité : Les fonctions serverless s'adaptent en fonction de la demande. Elles sont conçues pour gérer les pics soudains de trafic et garantir que les utilisateurs bénéficient d'une expérience cohérente.
* Efficacité des coûts : La plateforme de fonction serverless facture en fonction de l'utilisation réelle plutôt que de la maintenance de serveurs dédiés, ce qui permet d'économiser des coûts.
* Architecture de microservices : Les fonctions serverless vous permettent de créer des applications complexes lorsque vous combinez des fonctions mineures pour résoudre un problème particulier.
* Itérations de développement plus rapides : Avec la fonction serverless, vous pouvez vous concentrer sur des fonctionnalités spécifiques puisqu'elles sont isolées et apporter rapidement des modifications sans affecter l'ensemble du projet.
* Sécurité et isolation : Puisque les fonctions serverless prennent en charge un environnement isolé, réduisant le taux de bugs d'une fonction affectant une autre, elles sont hautement sécurisées.
* Distribution mondiale : Les plateformes serverless sont connues pour avoir un réseau mondial de centres de données, ce qui déploie les fonctions de votre application Next.js plus près des utilisateurs et réduit la latence.

### Cas d'utilisation des fonctions serverless pour les applications Next.js

Plusieurs sites web bénéficient beaucoup de l'utilisation d'une plateforme de fonction serverless. Certains types de ces applications Next.js incluent :

1. Applications de formulaires et d'interactions utilisateur : L'utilisation de fonctions serverless pour gérer les connexions utilisateur, les inscriptions et autres éléments interactifs peut augmenter l'expérience utilisateur et les performances en rendant ces processus transparents et asynchrones.
2. Récupération de données en temps réel : Les fonctions serverless peuvent récupérer des informations en temps réel à partir d'une base de données ou d'API sans solliciter votre serveur principal.
3. Contenu dynamique : Utilisez l'option d'hébergement de fonction serverless lorsque vous avez une application qui génère des données personnalisées telles que des graphiques, des métriques ou du contenu spécifique à l'utilisateur.
4. Authentification et autorisation : L'utilisation d'une fonction serverless lors de l'authentification et de l'autorisation des données peut améliorer la sécurité en déchargeant le travail lourd de validation de jeton et de gestion des utilisateurs.
5. Application e-commerce : Les fonctions serverless sont idéales pour gérer les mises à jour du panier d'achat et intégrer des passerelles de paiement fluides. 
6. Optimisation SEO : L'utilisation de fonctions serverless pour héberger votre application Next.js aide à rendre les métadonnées SEO et améliore la visibilité dans les moteurs de recherche.

### Exemples de plateformes d'hébergement serverless pour les applications Next.js

Nous avons listé plusieurs plateformes d'hébergement de fonctions serverless – maintenant, discutons de quelques-unes des plus populaires.

1. Vercel : Vercel est conçu pour répondre aux besoins de Next.js de manière transparente. Il prend en charge la fonction serverless et offre un réseau de diffusion de contenu (CDN) mondial, augmentant les performances et la fiabilité.
2. AWS Lambda : Amazon Lambda est souvent utilisé avec Amazon API Gateway pour vous permettre de déployer des fonctions serverless et des API. Cette option vous permet également de construire une architecture serverless personnalisée.
3. Azure Functions + Azure Static Web Apps : Cette combinaison de Microsoft Azure Cloud vous permet de déployer facilement votre application Next.js avec des fonctions serverless.
4. Google Cloud Function et Firebase Hosting : Vous pouvez combiner Google Cloud et Firebase Hosting pour profiter des capacités CDN et des fonctions serverless lorsque vous déployez votre application Next.js.
5. Netlify : Netlify permet un déploiement facile des applications Next.js et fournit des fonctions serverless. Il prend en charge la gestion des formulaires, le déploiement continu et un système de contrôle de version.

### Exploration de l'option de déploiement serverless d'AWS Lambda

AWS Lambda d'Amazon Web Services vous permet d'exécuter une fonction serverless sans gérer de serveurs. Il est couramment utilisé pour exécuter des fichiers de code en réponse à des requêtes HTTP, des changements de données dans la base de données et d'autres événements.

Déployer votre application Next.js sur AWS Lambda est simple si vous utilisez l'adaptateur Web fourni par la plateforme. Passons en revue les étapes maintenant.

#### Étape 1 : Emballez votre application Next.js

Assurez-vous que votre projet est prêt et testé localement. Vous pouvez emballer votre projet sous forme de fichiers Zip ou d'une image Docker.

Choisir une image Docker signifie gérer, construire ou pousser des images. Mais le style d'emballage zip est plus simple.

Voyons d'abord comment le faire avec Docker.

#### Étape 2 : Dockerisez votre application

Tout d'abord, vous devrez créer un `Dockerfile` à la racine de votre projet. Utilisez une image de base Node.js dans le `Dockerfile` comme suit : `FROM node:16`.

Ensuite, copiez les fichiers/paquets de l'application Next.js dans le conteneur.

Installez les dépendances nécessaires en utilisant cette commande : `RUN npm install --production`. Et construisez ensuite le projet avec `RUN npm build`.

Spécifiez la commande pour démarrer l'application : `npm run start` ou `yarn start`

#### Étape 3 : Construisez l'image Docker

Maintenant, utilisez la commande `docker build` dans le terminal pour créer une image de votre application et de ses dépendances.

Voici la commande `docker build -t my-nextjs-app .`

* -t ; utilisé pour spécifier le tag de l'image, qui doit être le nom du projet
* `.` pour montrer que Docker doit construire avec le répertoire courant

#### Étape 4 : Poussez l'image vers le registre de conteneurs :

Poussez l'image Docker pour que AWS Lambda puisse y accéder facilement. Dans ce cas, nous poussons vers Amazon Elastic Container Registry (ECR).

Connectez-vous à AWS ECR :

```
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com

```

Taggez l'image Docker :

```
docker tag image_name:tag aws_account_id.dkr.ecr.region.amazonaws.com/repository_name:tag


```

Poussez l'image :

```
docker push aws_account_id.dkr.ecr.region.amazonaws.com/repository_name:tag


```

#### Étape 5 : Créez une fonction AWS Lambda

À partir de la console AWS Lambda, vous créerez une nouvelle fonction lambda. Sélectionnez l'option `Container image` et choisissez l'image Docker dans le registre.

Maintenant, explorons comment le faire avec le **package zip** :

#### Étape 2 : Construisez votre application Next.js :

Utilisez soit `npm run build` soit `yarn build` pour construire votre application Next.js pour la production. Cela construira vos fichiers .jsx bruts en code HTML, CSS et Javascript qui sera présenté au navigateur de l'utilisateur.

#### Étape 3 : Créez un package de déploiement

Créez le répertoire de déploiement et copiez tous les fichiers nécessaires, y compris node_modules, package.json et .next. C'est tout ce dont vous avez besoin pour que votre application Next.js soit prête pour le déploiement en production.

#### Étape 4 : Créez un package zip

Maintenant, créez le package zip avec toutes vos applications Next.js et leurs dépendances. Pour ce faire, ouvrez votre terminal et naviguez jusqu'au répertoire de votre dossier d'application prêt pour la production.

Ensuite, utilisez la commande zip `zip -r my-nextjs-app.zip *` ; cela zippera le package en place et le sauvegardera sous `my-nextjs-app.zip`

_Si vous êtes sur Windows, utilisez `sudo apt-get install zip unzip` pour installer l'application zip._

#### Étape 5 : Téléchargez le package Zip vers AWS Lambda

Dans la console AWS Lambda, configurez une nouvelle fonction Lambda. Choisissez l'option "Upload a .zip file" et téléchargez le package zip que vous avez créé.

Voici comment télécharger le package zip vers AWS Lambda

1. Connectez-vous à votre console de gestion AWS, recherchez `Lambda` dans la barre de recherche des services 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-218.png)
_Page AWS Lambda_

2. Cliquez sur 'Create a function' pour créer une nouvelle fonction lambda.

3. Configurez la fonction

* Sélectionnez l'option 'Author from scratch'.
* Saisissez le nom de la fonction.
* Sélectionnez le runtime ; pour l'application Next.js, vous aurez besoin de Node.js.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-220.png)
_Création d'une fonction lambda_

* Sélectionnez un rôle d'exécution qui accorde une permission complète à la fonction Lambda, puis cliquez sur le bouton 'create function'.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-221.png)
_Sélectionnez un rôle d'exécution._

4. Configurez les déclencheurs de fonction : cliquez sur 'Add trigger' et sélectionnez 'API Gateway' pour l'option serverless. Et configurez comme vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-222.png)

5. À partir de l'onglet 'Code' sous l'onglet 'Function overview', cliquez sur 'upload from' et sélectionnez '.zip file'. Trouvez le fichier `my-nextjs-app.zip` enregistré et téléchargez-le.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-223.png)
_Téléchargement du package zip_

6. Plus de configuration et test : La console de gestion AWS vous permet de configurer 'destination', 'permission', 'function URL' et bien plus encore. Vous pouvez également tester votre application dans la section de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-227.png)
_Test avec la console AWS_

7. Une fois que vous êtes satisfait des configurations et des paramètres, vous pouvez la déployer.

_À partir de maintenant, les étapes seront les mêmes, alors continuons le processus :_

#### Étape 6 : Configurez la fonction Lambda :

Vous devrez définir le délai d'exécution, la mémoire et d'autres configurations de votre fonction Lambda.

Ensuite, définissez une variable d'environnement (uniquement lorsque c'est nécessaire).

Après cela, vous voudrez tester votre fonction Lambda et voir si votre application Next.js fonctionne comme prévu.

#### Étape 7 : Configurez API Gateway (optionnel)

Si votre projet est une API, vous pouvez configurer une API Gateway pour agir comme l'interface HTTP de votre fonction Lambda.

## Option #3 : Conteneurisation

Cette option de déploiement fournit un moyen d'emballer les applications Next.js avec leurs dépendances et de les rendre plus petites et plus cohérentes dans divers environnements. 

Vous pouvez conteneuriser votre application Next.js et la déployer via des plateformes d'orchestration comme Kubernetes ou Elastic Container Service (AWS ECS).

### Avantages de la conteneurisation des applications Next.js

Il existe plusieurs avantages à utiliser une stratégie de déploiement par conteneurisation pour votre application Next.js, qui incluent :

* Portabilité : La portabilité des conteneurs permet aux développeurs de construire une fois et d'exécuter n'importe où. Ce fichier réduit peut être utile dans un environnement cloud hybride ou de déploiement.
* Cohérence : Les conteneurs permettent à votre application Next.js de rester la même sur toutes les machines, la mise en scène et les tests. Cela réduit le problème "ça ne fonctionne pas sur ma machine".
* Isolation : Les conteneurs isolent le système et les autres conteneurs, améliorant la sécurité et minimisant les conflits entre vos applications et leurs dépendances.
* Microservices : Le conteneur a une architecture de microservices qui vous permet de mettre en place des parties plus petites d'une application et des services gérables qui peuvent être développés et testés indépendamment.
* Contrôle de version : Avec les images de conteneurs, vous pouvez les stocker et les versionner dans les registres et apporter des modifications pour passer à la version suivante ou revenir à la version précédente facilement.
* Déploiement rapide : Les conteneurs permettent de démarrer et d'arrêter rapidement, ce qui entraîne des temps de déploiement et de récupération plus rapides.
* Infrastructure as Code (IaC) : Les conteneurs fonctionnent bien avec les pratiques (IaC), vous permettant de définir et de gérer l'infrastructure de votre application via du code.

### Comment conteneuriser et déployer une application Next.js

Nous avons abordé certaines étapes de conteneurisation dans la section sur la stratégie des fonctions serverless. Voici les étapes complètes requises pour déployer votre application Next.js via la conteneurisation.

#### Étape 1 : Dockerisez votre application Next.js

Créez un `Dockerfile` à la racine de votre projet. Utilisez une image de base Node.js dans le `Dockerfile` comme suit : `FROM node:16`.

Copiez les fichiers/paquets de l'application Next.js dans le conteneur et installez les dépendances nécessaires avec la commande `RUN npm install --production`. 

Construisez le projet avec cette commande : `RUN npm build`. 

Ensuite, spécifiez la commande pour démarrer l'application -- `npm run start` (CMD ["npm", "run"]).

#### Étape 2 : Construisez l'image Docker

En utilisant la commande `docker build` dans le terminal, nous pouvons créer une image de notre application et de ses dépendances.

Ensuite, vous voudrez tester votre application Next.js en utilisant la commande `docker run -p 3000:3000 nextjs-app` et vous assurer qu'elle fonctionne comme prévu.

#### Étape 3 : Déployez l'application Next.js conteneurisée

Sélectionnez où stocker votre image Docker – vous pouvez utiliser Amazon ECR, Docker Hub, Google Container Registry, etc.

Ensuite, vous voudrez tagger et pousser l'image Docker. Utilisez la commande `docker tag nextjs-app:latest registry-url/repository-name:tag`. 

Remplacez `registry-url/repository-name:tag` par votre plateforme de registre sélectionnée et les valeurs.

Ensuite, poussez l'image taguée vers le registre choisi avec cette commande : 
`docker push registry-url/repository-name:tag`.

#### Étape 4 : Configurez votre environnement de déploiement

Configurez l'environnement sur votre fournisseur de cloud choisi. Suivez ces étapes

* Choisissez un fournisseur de cloud comme Amazon Web Services (AWS), Google Cloud Platform, Microsoft Azure ou tout autre qui correspond à votre budget et à vos exigences. Créez et connectez-vous à votre compte.
* Configurez un registre de conteneurs sur le fournisseur sélectionné. 
* Configurez la sécurité et les sous-réseaux et créez des réseaux virtuels, car ils contrôleront l'accès réseau à votre application conteneurisée.

#### Étape 5 : Déployez votre application

Maintenant, déployez votre application Next.js en utilisant soit :

* Kubernetes : Appliquez le fichier YAML comme suit `kubectl apply -f filename.yaml`
* AWS ECS : Créez une nouvelle tâche en utilisant la console de gestion AWS ou l'AWS CLI

Ensuite, vous devrez configurer Ingress ou Load Balancer pour rendre votre application disponible en ligne. Et enfin, vous voudrez tester votre application Next déployée.

## Option #4 : Rendu côté edge (ESR)

Cette option de déploiement fournit à l'application Next.js un rendu côté edge pour obtenir des versions mises en cache des pages à partir d'un réseau de diffusion de contenu (CDN). 

Le CDN fait en sorte que les pages se chargent plus rapidement lorsqu'un utilisateur demande une page pour la deuxième fois. Cela est possible car le CDN diffuse des pages pré-rendues, réduisant le temps de réponse.

### Avantages du rendu côté edge (ESR) lors du déploiement d'une application Next.js

Le rendu côté edge rend une partie de l'interface utilisateur sur les serveurs edge d'un CDN, mais ce n'est pas le seul avantage. D'autres avantages incluent :

1. Performances améliorées : L'ESR diminue le temps de chargement du site web en minimisant le temps de trajet aller-retour vers le serveur d'origine. Cela produit un temps de chargement plus rapide et une expérience utilisateur améliorée.
2. Latence réduite : L'ESR charge le contenu à partir d'un serveur plus proche, et même lorsque le serveur d'origine est loin, les utilisateurs reçoivent le contenu rapidement.
3. Optimisation des moteurs de recherche (SEO) améliorée : Le SEO est amélioré car le moteur de recherche peut explorer le contenu HTML pré-rendu à partir des serveurs edge.
4. Évolutivité : L'ESR partage la charge de rendu avec les serveurs d'origine et edge, ce qui aide à gérer plus d'utilisateurs lors des pics de trafic sans surcharger le serveur d'origine ou le faire planter.
5. Charge du serveur réduite : L'ESR permet au serveur d'origine de n'être responsable que de certaines requêtes de rendu des utilisateurs. L'ESR réduit la consommation de ressources et la charge du serveur et améliore les performances globales.
6. Expérience utilisateur cohérente : L'ESR garantit que tous les appareils, quel que soit le navigateur, reçoivent un contenu rendu, offrant une expérience cohérente.
7. Économies de coûts : En utilisant des serveurs edge, vous dépenserez moins de puissance et de ressources sur les serveurs d'origine.

### Comment déployer une application Next.js avec le rendu côté edge (ESR)

Déployer une application Next.js avec le rendu côté edge nécessite un CDN pour rendre certaines parties de votre application Next.js avec des serveurs edge. Voici comment fonctionne le processus.

#### Étape 1 : Préparez votre application Next.js

Assurez-vous que votre application Next.js est fonctionnelle et a été testée localement. Assurez-vous qu'elle est prête à être déployée.

#### Étape 2 : Choisissez votre fournisseur de CDN

Choisissez un fournisseur de CDN avec support ESR. Vous pouvez choisir Cloudflare Workers, Vercel Edge Network ou Fastly. Décidez lequel convient le mieux à votre application.

#### Étape 3 : Configurez le compte CDN

Configurez votre compte CDN, ce qui ne devrait prendre que cinq minutes.

* Inscrivez-vous ou connectez-vous à votre fournisseur de CDN préféré ci-dessus.
* Sélectionnez un plan qui correspond à votre budget et aux exigences de votre application.

#### Étape 4 : Configurez le rendu côté edge

Configurez l'ESR avec les instructions données par le fournisseur de CDN. Le processus implique l'écriture de scripts qui indiquent quelle partie de votre application Next.js doit être rendue sur le serveur edge et quelles parties peuvent être servies sur le serveur d'origine.

#### Étape 5 : Déployez la configuration ESR

Déployez votre configuration ESR sur la plateforme CDN sélectionnée en utilisant la commande appropriée sur le CLI – `vercel deploy`, `wrangler publish`, etc.

#### Étape 6 : Test du rendu côté edge :

Testez la configuration ESR et confirmez que les parties spécifiées de votre application sont rendues sur le serveur edge. Observez les améliorations de performance et assurez-vous que le rendu est cohérent sur divers appareils, navigateurs et emplacements.

#### Étape 7 : Mettez à jour les paramètres DNS

Configurez les paramètres DNS pour pointer vers les serveurs du CDN afin de garantir que les requêtes vers votre application sont acheminées via les serveurs edge.

#### Étape 8 : Surveillez et optimisez :

Une fois déployé, surveillez les performances en temps réel. Vérifiez les outils de surveillance fournis par le CDN pour suivre les métriques, la latence et l'expérience utilisateur.

Notez que les étapes peuvent changer en fonction du fournisseur de CDN que vous avez sélectionné, mais ce sont les étapes de base pour tous. Vous pouvez consulter la documentation pour en savoir plus.

## Bonnes pratiques pour le déploiement d'applications Next.js

Déployer une application Next.js est similaire au déploiement de toute autre application web. Bien que Next.js permette le [développement backend](https://medium.com/codex/can-we-use-next-js-13-as-a-backend-framework-b5f9479a2d#:~:text=checking%20to%20JavaScript.-,Next.,process%20and%20prevent%20runtime%20errors.), les stratégies de déploiement sont presque identiques.

Pour déployer vos applications Next.js de la meilleure et de la manière la plus efficace possible, envisagez les pratiques suivantes :

1. Constructions optimisées : Optimisez le processus de construction de votre Next.js en utilisant les meilleurs paramètres de construction, en tirant parti de la génération de site statique (SSR) ou du rendu côté serveur (SSR).
2. Suivi des erreurs : Intégrez des outils pour trouver et résoudre les problèmes de manière proactive. Surveillez la santé du serveur, l'interaction utilisateur et l'application pour améliorer l'expérience utilisateur et la stabilité de l'application.
3. Variables d'environnement : La gestion des informations sensibles API et config doit être effectuée dans une variable d'environnement. Évitez de mettre des données sensibles dans votre base de code dans tout environnement de déploiement.
4. Intégration et déploiement continus (CI/CD) : Pour diminuer les bugs et les erreurs dans votre application Next.js déployée, vous devez configurer des pipelines CI/CD. Ces pipelines automatiseront le processus de construction, de déploiement et de test de votre projet.
5. Considérations d'évolutivité : Une architecture bien conçue doit être en place pour gérer l'augmentation du trafic. Tirez parti de techniques telles que les fonctions serverless et les mécanismes de mise en cache dans votre application pour gérer les fluctuations de la demande des utilisateurs.
6. Tests automatisés : Effectuez des tests automatisés pour votre application afin de vérifier les performances et la fonctionnalité. Vous pouvez essayer des tests unitaires, des tests d'intégration et des tests de bout en bout pour détecter les bugs plus tôt, encore au stade du déploiement.
7. Contrôle de version : Utilisez un système comme Git pour suivre les changements dans votre base de code et améliorer la collaboration avec les coéquipiers. Avec une plateforme de contrôle de version, vous pouvez facilement annuler les erreurs et les bugs et intégrer des fonctionnalités.
8. Documentation : Un document bien détaillé sur les instructions d'installation, de déploiement et de configuration de votre application Next.js. Cette documentation bien écrite aidera à intégrer de nouveaux membres et à rationaliser le processus de déploiement. 
Ces pratiques sont incroyables et aident à obtenir une application fluide et évolutive.

## Bonnes pratiques pour la gestion des variables d'environnement dans une application Next.js

Nous devons parler des bonnes pratiques et prêter attention à la sécurité. La gestion des variables d'environnement est cruciale pour la sécurité et la gestion de la configuration lors du déploiement de votre application Next.js.

Voici quelques bonnes pratiques :

1. Utilisez `.env.local` pour le déploiement local : Créez un fichier `.env.local` à la racine de votre projet. Ce fichier contiendra des variables à utiliser uniquement lors du déploiement local.
2. Utilisez `.env` pour les variables partagées : Ici, vous pouvez stocker des variables non sensibles soumises au contrôle de version et les partager avec l'équipe. Créez un fichier `.env`, mais ne stockez pas d'informations sensibles ici.
3. Utilisez `.env.production` pour la production : Le fichier `.env.production` contient les variables nécessaires lors du processus de construction de votre application. Ces variables dans le fichier `.env.production` priment sur celles du fichier `.env`.
4. Accès côté serveur : Certaines variables stockées dans le fichier `.env` ne doivent être accessibles que côté serveur pour éviter de les exposer au client. Vous pouvez utiliser les méthodes `getServerSideProps` ou `getInitialProps` pour les définir.
5. Exclusion du contrôle de version : Ne commitez pas les variables ; incluez-les dans un fichier `gitignore` pour éviter les problèmes de sécurité.
6. Intégration CI/CD : Utilisez des pipelines CI/CD pour gérer les variables d'environnement et garantir une configuration cohérente de manière sécurisée.

## Conclusion

Le déploiement est aussi vital que toute autre étape de la création d'une application Next.js ; on pourrait dire que c'est la plus importante car une mauvaise configuration lors du déploiement pourrait affecter les performances de votre application et éloigner les utilisateurs.

Les stratégies sont similaires mais uniques, et celle que vous sélectionnez doit dépendre du type de site web que vous créez. Vous n'avez pas besoin de choisir la stratégie de rendu côté edge lorsque vous créez un site web statique.

Suivez les bonnes pratiques ci-dessus pour déployer une application Next.js sûre et optimisée pour vos utilisateurs.

Ressources supplémentaires :

* [Documentation de Vercel](https://vercel.com/docs/concepts/edge-network/overview)
* [Plus d'informations sur les stratégies de déploiement](https://www.altaro.com/hyper-v/hyper-v-vm-container-nano-deployments/)