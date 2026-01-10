---
title: Comment déployer votre application Node.js sur Azure
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-07-17T11:56:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-node-js-app-on-azure
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/awsP.jpg
tags:
- name: Azure
  slug: azure
- name: node
  slug: node
- name: Web Hosting
  slug: web-hosting
seo_title: Comment déployer votre application Node.js sur Azure
seo_desc: "The advent of cloud computing marked a turning point in the field of technology.\
  \ It provides easier access for users across the globe to web and mobile applications\
  \ and services. \nModern-day computing services also provide a wide range of features\
  \ wh..."
---

L'avènement du cloud computing a marqué un tournant dans le domaine de la technologie. Il offre un accès plus facile pour les utilisateurs du monde entier aux applications et services web et mobiles. 

Les services informatiques modernes offrent également une large gamme de fonctionnalités qui rendent les applications web plus faciles à utiliser et plus efficaces. Il est donc important pour les développeurs d'avoir une compréhension de base du fonctionnement du cloud.

Cet article est un guide pour débutants sur le déploiement d'applications backend dans le cloud. Nous utiliserons la plateforme Azure comme infrastructure cloud et Node.js/Express pour l'application web backend. Avant de continuer, voici quelques prérequis :

* Compréhension de base du cloud computing (vous pouvez consulter [cet article](https://dev.to/oluwatobi2001/introduction-to-cloud-computing-the-models-benefits-risks-implementation-and-popular-tools-2loh) pour en savoir plus).
* Connaissance de JavaScript.
* VS Code.

Avec cela, commençons.

## Introduction à Azure

Azure est une plateforme de cloud computing développée par Microsoft qui sert de serveur pour déployer et héberger des applications web, des bases de données, du stockage de fichiers, etc. 

Comparé à d'autres services de cloud computing, il est assez convivial pour les débutants et possède une base d'utilisateurs en croissance active. Explorons le portail Azure.

## Comment créer un compte Azure

S'inscrire sur la plateforme Azure est la première étape pour héberger votre application. Tout d'abord, naviguez vers [le site web](https://azure.microsoft.com/en-us/get-started/azure-portal) et complétez le processus d'inscription.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-36.png)
_Page de connexion Azure_



Après votre inscription, vous aurez accès à la console de gestion de l'application Azure où toutes nos activités peuvent être réalisées.

Avant de continuer, voici quelques-uns des services avec lesquels nous allons nous familiariser sur cette plateforme.

* Groupes de ressources Azure
* Services d'applications Azure
* Comptes de stockage
* Bases de données SQL
* Réseaux virtuels

![Image](https://www.freecodecamp.org/news/content/images/2024/07/serc3.PNG)
_Services Azure_

Félicitations pour avoir créé avec succès votre compte Azure.

## Options de déploiement sur Azure

En tant que plateforme de cloud computing, Azure se distingue par sa grande polyvalence. Selon votre niveau de compétence ou vos préférences, vous pouvez déployer des applications web sur Azure via les options suivantes :

* Azure CLI
* Machines virtuelles Azure
* Azure Functions
* Azure Kubernetes Service
* Azure Storage.
* Azure DevOps
* Service de portail Azure

Nous utiliserons le service de portail Azure pour ce tutoriel et son intégration avec VS Code pour déployer une simple application Node.js sur le cloud Azure.

## Comment configurer l'application backend

Nous allons créer notre application web en utilisant Node.js via la ligne de commande et Visual Studio Code.

Tout d'abord, naviguez vers le dossier où votre application sera créée et initialisez un projet Node en exécutant `npm init`.

Ensuite, initialisez l'application en installant le framework `Express`. Cela peut être fait via `npm i express`. 

Continuez et collez le code exemple pour ce tutoriel :

```
const express = require("express");
const app = express();

app.use(express.json());

app.get("/", (req, res) => {
    res.send("Hello, World");
});

app.listen(process.env.PORT || 5000, () => {
    console.log("Server is running on port " + (process.env.PORT || 5000));
});


```

Le code ci-dessus affiche `Hello World` chaque fois qu'il est exécuté.

## Déploiement de l'application

Le code backend que nous avons écrit dans le paragraphe précédent sera déployé sur Azure via l'utilisation de l'extension VS Code d'Azure.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/webVs.PNG)
_Page d'accueil de VS Code_

Naviguez vers l'onglet Extensions, recherchez Azure App Services et installez l'extension. Après une installation réussie, un widget Azure apparaîtra sur votre barre des tâches où vous pourrez vous connecter au cloud Azure.  


![Image](https://www.freecodecamp.org/news/content/images/2024/07/azure-app-service.PNG)
_Marketplace des extensions_

  
Par la suite, nous allons créer une application web basée sur le cloud dans laquelle notre code Node.js sera déployé plus tard.

Dans l'onglet des ressources Azure, cliquer sur l'icône `plus` affichera un menu déroulant où diverses options de développement peuvent être vues. Nous cliquerons sur l'option des services d'applications Azure.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/res-1.png)
_Menu déroulant Azure_

  
Après avoir cliqué dessus, une invite apparaîtra demandant un nom unique pour l'application cloud. Dans mon cas, j'ai choisi newApp777.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newa7.PNG)
_création d'une application web_

Cependant, vous pouvez utiliser tout autre nom que vous souhaitez. Par la suite, vous devrez sélectionner le langage backend de votre choix. Toute version de Node.js sera compatible avec notre application.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newStack.PNG)
_piles web disponibles_

De plus, l'option de service F1 sera utilisée pour ce tutoriel. Cependant, vous pouvez choisir celle que vous souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newTier.PNG)
_Différents niveaux Azure_

Une fois terminé avec succès, votre application sera créée sur le portail Azure.

  
Maintenant, le cœur du sujet. Déployons notre code Node.js sur cette application web. 

Nous cliquerons sur le dossier de code qui nous offre des options pour déployer automatiquement notre code sur un service d'application web Azure.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-35.png)
_Menu déroulant de déploiement_

Dès que cela est fait, la liste des serveurs cloud de votre compte Azure sera affichée. Vous pouvez ensuite sélectionner la nouvelle application que nous venons de créer.  


![Image](https://www.freecodecamp.org/news/content/images/2024/07/sear.PNG)
_déploiement de l'application_

  
Votre code backend devrait alors être déployé sur le serveur cloud NewApp que nous avons créé. Une fois terminé avec succès, vous recevrez un message de succès avec un lien vers votre application cloud.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/pro.PNG)
_interface de l'invite de commande_

Félicitations, vous avez hébergé avec succès votre première application web. Naviguez [ici](https://newapp777.azurewebsites.net/) pour voir l'application hébergée.

![Application Azure](https://www.freecodecamp.org/news/content/images/2024/07/wevpage.PNG)
_La page web de l'application_

## Informations supplémentaires

Jusqu'à présent, nous avons couvert les bases du déploiement d'une application via l'utilisation des extensions VS Code sur les services de portail Azure. À mesure que vous progressez dans le domaine du cloud computing, d'autres domaines intéressants peuvent également être explorés, tels que :

* Surveillance des applications avec Azure Monitor.
* Essentiels du réseau d'applications Azure.
* Intégration de la base de données Azure MySQL.
* Déploiement de fonctions serverless Node JS.

Vous pouvez également interagir avec moi sur mon blog et consulter mes autres articles [ici](https://linktr.ee/tobilyn77). En attendant, continuez à coder !