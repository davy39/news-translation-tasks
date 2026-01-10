---
title: Comment utiliser Azure Static Web Apps pour déployer une application Angular
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-04-14T23:42:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-azure-static-web-apps-to-deploy-angular-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/cover_2.png
tags:
- name: Angular
  slug: angular
- name: Azure
  slug: azure
- name: Web Applications
  slug: web-applications
seo_title: Comment utiliser Azure Static Web Apps pour déployer une application Angular
seo_desc: "CI/CD has changed the way IT teams release new software versions. \nIn\
  \ this tutorial I'll share my experience with Azure Static Web Apps – Azure's PaaS\
  \ solution. I'll show you how you can take advantage of its flexibility to deploy\
  \ an Angular App just..."
---

Le CI/CD a changé la façon dont les équipes informatiques publient de nouvelles versions de logiciels. 

Dans ce tutoriel, je vais partager mon expérience avec Azure Static Web Apps – la solution PaaS d'Azure. Je vais vous montrer comment vous pouvez tirer parti de sa flexibilité pour déployer une application Angular simplement en poussant votre code vers un dépôt Git.

Il existe de nombreuses ressources sur le CI/CD sur le web, et dans cet article, je souhaite me concentrer sur Azure Web Apps pour vous montrer comment cela peut simplifier considérablement votre flux de travail. 

Si vous souhaitez en savoir plus sur le CI/CD, le [blog](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment) d'Atlassian contient des informations utiles. Et voici un guide approfondi et [basé sur un projet sur le sujet](https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws/).

## De quoi avons-nous besoin pour ce projet ?

Au cours de ce tutoriel, nous utiliserons les technologies et outils suivants :

* Un compte GitHub 
* Node.js (vous pouvez le télécharger [ici](https://nodejs.org/en/download/))
* Npm (gestionnaire de paquets Node.js. Inclus avec l'installation de Node.)
* Angular CLI (un outil en ligne de commande pour créer, développer et maintenir votre application Angular. Vous pouvez le télécharger [ici](https://angular.io/cli).)
* Compte Azure (vous pouvez commencer gratuitement en créant votre compte [ici](https://azure.microsoft.com/en-us/free/). Une fois votre essai gratuit expiré, vérifiez les coûts que vous engagez. Les technologies cloud sont très puissantes et peuvent faciliter votre vie. Mais elles peuvent être coûteuses si elles ne sont pas bien gérées.)

Si vous souhaitez suivre ce tutoriel et reproduire ce que je construis, vous devez être prêt avec ces outils.

## Ce que nous allons construire ici – l'image globale

Voyons comment créer notre application Angular et la déployer avec Azure Web App. Nous allons créer notre application Angular localement et la pousser vers un dépôt GitHub que nous créons spécifiquement pour ce projet. 

Le dépôt aura deux branches : « main » et « develop ». Nous allons créer une application web statique sur Azure et la connecter à la branche « main » du dépôt. 

De retour sur votre machine, modifiez le code et poussez-le vers la branche « develop ». Ensuite, fusionnez la branche « develop » avec la branche « main » et voyez la nouvelle version de votre application en ligne.

Pour être plus clair, je pense qu'une liste rapide nous aidera à récapituler chaque étape :

* Vous allez créer votre application Angular localement avec Angular CLI
* Vous allez la pousser vers un dépôt GitHub
* Vous allez créer une application web statique sur Azure et la connecter à la branche « main » du dépôt du projet
* Vous allez créer un dépôt « develop »
* Vous allez modifier le code de l'application localement et le pousser vers le dépôt « develop »
* Vous allez créer une pull request sur votre projet GitHub de « develop » vers « main » et la fusionner
* Vous allez vérifier si la nouvelle version de l'application est disponible sur l'application web

## Étape 1 – Créer l'application Angular localement

Tout d'abord, créons un répertoire spécifique sur votre ordinateur et déplaçons-nous dedans. Je suis sur Mac, donc j'ouvre mon terminal et je tape :

```
mkdir angular_azure
cd angular_azure
```

Une fois dedans, créez votre nouvelle application Angular appelée « angular_app » :

```
ng new angular_app
```

Angular CLI vous pose quelques questions :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/0.png)

Nous voulons ajouter Angular router et nous voulons également utiliser CSS pour styliser l'application. Une fois que vous recevez un retour positif d'Angular CLI, démarrez votre application localement pour voir si tout fonctionne bien :

```
ng serve --open
```

L'option « --open » indique à Angular CLI que vous souhaitez ouvrir l'application avec votre navigateur par défaut. Cela signifie que vous n'avez pas besoin de copier et coller l'URL dans la barre d'adresse de votre navigateur. Donc, voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/3.png)

  
Il semble que tout fonctionne bien. Vous pouvez arrêter l'application (Ctrl + C) et passer à l'étape suivante

## Étape 2 – Pousser l'application Angular vers votre dépôt GitHub 

Vous devriez avoir créé un nouveau dépôt sur votre compte GitHub dédié à ce projet. J'ai appelé le mien « angular-app-with-azure ». Si vous ne savez pas comment créer un nouveau dépôt, vous pouvez [en savoir plus ici](https://docs.github.com/en/get-started/quickstart/create-a-repo).

Une fois le dépôt prêt, poussez votre application Angular de votre machine vers votre dépôt. Si vous n'ajoutez pas de fichier README lors de la création de votre dépôt, vous devriez voir les instructions sur la façon de pousser votre code directement sur la page de votre dépôt. Cependant, je vais répéter ces instructions ici également :

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<REPO>.git
git push -u origin main
```

Une fois que vous avez exécuté ces commandes avec succès, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/4-1.png)

  
Continuons maintenant.

## Étape 3 – Il est temps de passer à Azure

Maintenant, vous allez créer une toute nouvelle application web statique Azure et la connecter à votre dépôt. Tout d'abord, entrez dans le portail Azure [ici](https://portal.azure.com), et allez dans votre groupe de ressources. Ensuite, vous verrez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/5-1.png)

Cliquez sur « créer » et vous verrez la liste des ressources disponibles sur Azure. Filtrez les ressources par « Static Web App » et sélectionnez-la.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/6.a.png)

Ensuite, passez à l'assistant d'Azure pour créer la ressource. Voyons comment vous devez le remplir.

Tout d'abord, choisissez l'abonnement et le groupe de ressources. Ensuite, passez aux détails de l'application web statique : choisissez le nom – « angular-app » – et restez avec le plan gratuit. Ensuite, sélectionnez votre région – la mienne est « Central US ».

![Image](https://www.freecodecamp.org/news/content/images/2022/04/6-1.png)

Ensuite, continuez avec quelques informations supplémentaires :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/7-1.png)

Vous pouvez synchroniser votre compte GitHub dans la section « Détails de déploiement », puis spécifier l'organisation, le dépôt et la branche à partir desquels vous obtiendrez votre base de code. 

Comme je l'ai dit au début de ce tutoriel, je choisis la branche « main » comme branche de production. 

Maintenant, concentrons-nous sur les « Détails de construction ». Vous allez choisir « Angular » comme « Préréglages de construction », et spécifier que l'application est située dans le répertoire racine dans « Emplacement de l'application ». 

Ensuite, vous allez taper le chemin de l'emplacement de sortie (répertoire « dist » plus le répertoire du nom du projet. Dans mon cas, c'est « dist/angular-app ». C'est là que Angular CLI localise la construction de votre projet. J'ai passé beaucoup de temps à chercher cette info et je pense qu'il est bon de la partager avec vous).

Donc, maintenant vous êtes prêt à créer votre application web statique. Cliquez sur « créer » et voyez ce qui se passe. Voici l'aperçu de mon application :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/555-1.png)

Ensuite, cliquez sur le lien « URL » et voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/33.png)

##   
Étape 4 – Créer une nouvelle branche 

Donc maintenant, vous allez revenir à votre base de code localement et créer votre branche « develop » et la vérifier :

```
git checkout -b develop
```

Ensuite, allez dans :

```
src/app/app.component.html
```

Modifiez le code comme ceci :

```
<p>Poussé vers develop</p>
<router-outlet></router-outlet>
```

Et ensuite, poussez la nouvelle branche vers le dépôt distant :

```
git push origin develop
```

## Étape 5 – Il est temps de fusionner 

Votre application Angular est toujours en ligne avec l'ancienne version. Vous devez fusionner votre branche "develop" avec "main" pour voir les changements en ligne.

Créez une pull request sur GitHub et fusionnez-la. Voici ce que vous devriez voir à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/999.png)

Attendez quelques minutes et vous verrez la nouvelle version de votre application en ligne :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/888-1.png)

## Un récapitulatif rapide et des ressources utiles

J'espère que ce tutoriel vous a montré comment vous pouvez facilement déployer votre code dans un environnement de production avec CI/CD et Azure Static Web App. 

En pratiquant avec ces technologies, j'ai trouvé beaucoup de contenu intéressant sur le web à leur sujet. J'ai pensé qu'il serait bon pour vous de les avoir tous au même endroit :

* [Qu'est-ce que Git ? Un guide pour débutants sur le contrôle de version Git](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/)
* [Comment utiliser Git et les flux de travail Git – un guide pratique](https://www.freecodecamp.org/news/practical-git-and-git-workflows/)
* [Documentation sur les actions GitHub](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
* [Documentation Angular](https://angular.io/)
* [Mon dépôt sur GitHub](https://github.com/mventuri/angular-app-with-azure)

Et n'oubliez pas... Continuez à apprendre et à coder !