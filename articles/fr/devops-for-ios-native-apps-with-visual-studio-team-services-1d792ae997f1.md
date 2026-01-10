---
title: Comment utiliser Visual Studio Team Services pour les applications natives
  iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-11T09:18:21.000Z'
originalURL: https://freecodecamp.org/news/devops-for-ios-native-apps-with-visual-studio-team-services-1d792ae997f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mm3f1tm-X0dpyjNbiubucw.gif
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Visual Studio Team Services pour les applications natives
  iOS
seo_desc: 'By Khawaja Farooq

  Visual Studio Team Services (VSTS) provides an easy way to share code, automate
  builds, run unit tests, and ship software. Developers from a wide range of platforms
  rely on it. It promotes continuous integration, which can accelerat...'
---

Par Khawaja Farooq

[Visual Studio Team Services](https://www.visualstudio.com/team-services/) (VSTS) offre un moyen facile de partager du code, d'automatiser les builds, d'exécuter des tests unitaires et de livrer des logiciels. Les développeurs de diverses plateformes s'appuient sur cet outil. Il favorise l'intégration continue, ce qui peut accélérer le processus de la conception à la livraison.

Microsoft a accompli un travail substantiel pour améliorer DevOps pour les plateformes mobiles et autres. Cependant, il n'existe pas de spécificités pour la plateforme native iOS. Voici un guide sur la façon de configurer VSTS pour un projet iOS, afin que vous puissiez exploiter ses capacités d'intégration continue.

Voici les prérequis pour commencer :

1. Projet Xcode buildable sur GitHub / TFS
2. Compte VSTS

### Créer un projet VSTS

Créez un nouveau projet d'équipe → _Paramètres > Vue d'ensemble > Nouveau projet d'équipe_

![Image](https://cdn-media-1.freecodecamp.org/images/5A8zGgcE0E9K8mDwFCz5BXOaDQ7vd6SFb0Gl)

L'étape suivante consiste à importer votre dépôt existant. Pour l'instant, nous utilisons GitHub. Cliquez sur _importer un dépôt_.

![Image](https://cdn-media-1.freecodecamp.org/images/1d1RSYgmeYA-ZfyKTc6G8XYthoZYEw7X5S0w)

Vous avez maintenant votre propre copie du dépôt que vous devriez pouvoir voir !

### Installer l'agent de build iOS

VSTS n'a pas d'agent préinstallé pour construire un projet Xcode. Cette partie est cruciale.

Heureusement, la configuration est couverte par [James Montemagno pour Xamarin iOS](https://blog.xamarin.com/continuous-integration-for-ios-apps-with-visual-studio-team-services/). Pour plus de commodité, je cite ici quelques-unes des étapes.

Vous devrez installer les éléments suivants pour préparer votre Mac :

1. [Homebrew OS X](https://brew.sh/)
2. [.NET Core](https://www.microsoft.com/net/core#macos)
3. Installez npm en utilisant la commande : **brew install npm**
4. Créez un [jeton d'accès personnel](https://www.visualstudio.com/en-us/docs/setup-admin/team-services/use-personal-access-tokens-to-authenticate) (PAT) et pour la portée : _Agent Pools (lecture, gestion)_

#### File d'attente de l'agent

1. Créez une nouvelle file d'attente d'agent « OSX » → _Paramètres > Files d'attente d'agents_
2. Téléchargez et configurez l'agent de build pour OS X.

![Image](https://cdn-media-1.freecodecamp.org/images/NAUNW7VQqw2hrykcwebAuOGtM2d0vR6LtTPf)

Une fois la configuration terminée, exécutez l'agent de build avec la commande suivante :

```
./run.sh
```

Bien joué ! Vous avez un agent de build sur site en cours d'exécution.

### Créer la définition de build Xcode

Une fois que vous avez installé l'agent de build, il est temps de créer une définition de build. Ces étapes créeront une définition de build pour Xcode iOS au lieu de Xamarin. Allez à → _Build & Release > Nouvelle définition >_ Xcode

![Image](https://cdn-media-1.freecodecamp.org/images/4LvE4SuRG5N0qxdYKwSQUlhVCi0USraGR6Cr)

N'oubliez pas de sélectionner votre pool d'agents que vous venez de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/56A8HwKcOuabTD90G6YtIlANIbjgL8yjOn30)

La définition de build Xcode peut ressembler à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/yvVzVxSGbdcjjCZYdqMq8-2tT5eAM6-LdkWb)

Le _chemin de l'espace de travail_ varie selon que vous utilisez un espace de travail Xcode ou simplement un projet.

Dans le cas où vous utilisez un espace de travail Xcode :

```
*.xcodeproj/project.xcworkspace
```

Pour un projet Xcode :

```
*.xcodeproj
```

Vous pouvez également utiliser certaines utilités pour [copier et publier vos artefacts de build](https://www.visualstudio.com/en-us/docs/build/steps/utility/copy-and-publish-build-artifacts).

Ensuite, enregistrez la définition de build et mettez en file d'attente une nouvelle build...

![Image](https://cdn-media-1.freecodecamp.org/images/2RpYOp-3o9-teatL7pMOdGdQC07Ib0zcgNlf)

Vous devriez obtenir une erreur de build. Nous devons apporter une modification à la configuration du projet Xcode.

### Configurer le projet/espace de travail Xcode

VSTS a besoin d'un schéma de projet partagé pour construire le projet. Assurez-vous de l'activer. _Xcode_ → _Product > Schemes > Manage schemes_

![Image](https://cdn-media-1.freecodecamp.org/images/KMojWE198TJHgM6B7MB-IIoBfqMy10Lp3taL)

Maintenant, poussez les modifications vers votre contrôle de source et construisez à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/y0IatW3Lfq-dKdu1xlu0TeYwoMxr57Aray42)

### Déployer sur HockeyApp

HockeyApp aide les testeurs pour les tests bêta des applications. Il est facile d'installer [l'extension VSTS](https://marketplace.visualstudio.com/items?itemName=ms.hockeyapp) depuis le marketplace. Cela permet à l'application d'être téléchargée après une build réussie.

![Image](https://cdn-media-1.freecodecamp.org/images/8F1g9Qo9BhY-YvAPtarq-eBfjwcbNca1ntny)

[**_Télécharger & importer la définition de build exemple_**](https://github.com/khawajafarooq/XcodeBuildDefinition)

Visual Studio Team Services offre une intégration continue pour les développeurs iOS. En automatisant de nombreuses tâches répétitives, il vous fait gagner du temps.

Une autre option est [MacinCloud](http://www.macincloud.com/), une solution cloud pour construire des applications natives iOS. Pour l'instant, nous avons examiné les capacités de build sur site, car _Azure_ ne fournit pas de support VM pour Mac OS X. Essayez VSTS et laissez vos commentaires ou contactez-moi sur Twitter [@khfarooq](https://twitter.com/khfarooq), c'est ce qui me motive. Merci pour votre lecture ! 😊