---
title: React et Firebase sont tout ce dont vous avez besoin pour héberger vos applications
  web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T00:25:32.000Z'
originalURL: https://freecodecamp.org/news/react-and-firebase-are-all-you-need-to-host-your-web-apps-f7ab55919f53
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ytMIcp6uu6UIZpApG1LFYg.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: React et Firebase sont tout ce dont vous avez besoin pour héberger vos
  applications web
seo_desc: 'By Ashish Nandan Singh

  A lot of modern web development stories don’t have good endings because of the complex
  number of technologies involved and the development approach adopted to get work
  done.

  The real question is, how can we make this journey le...'
---

Par Ashish Nandan Singh

Beaucoup d'histoires de développement web moderne n'ont pas de bonnes fins en raison du nombre complexe de technologies impliquées et de l'approche de développement adoptée pour accomplir le travail.

La vraie question est, comment pouvons-nous rendre ce voyage moins douloureux, ou devrais-je dire plus fructueux et efficace ? Idéalement, les technologies que nous choisissons devraient être bien établies et avoir un excellent soutien communautaire.

Dans cet article, nous allons examiner deux technologies qui sont très bien établies et ont un fort soutien communautaire, qui nous permettent de créer des applications web en direct plus efficacement.

#### Prérequis :

* Vous connaissez un peu React, au moins les bases
* Vous avez Node.js et NPM installés
* Vous savez comment utiliser la ligne de commande

#### Voici donc ce que nous allons couvrir aujourd'hui :

* Créer une application React simple avec create-react-app
* Se connecter à la console Firebase et créer un nouveau projet
* La déployer sur l'hébergement **Firebase** avec une simple commande

Lorsque j'ai initialement essayé de déployer une application web **React** sur l'hébergement **Firebase** et que je voulais faire fonctionner l'application web, j'ai rencontré quelques obstacles. J'ai compris qu'il pourrait être utile de compiler toutes les recherches que j'ai menées dans un article complet pour aider la communauté. Alors commençons.

À un niveau élevé, cet article est divisé en **trois** parties :

1. Mettre en place une application **React** très basique
2. Créer un compte **Firebase**
3. Connecter notre console **Firebase** à notre application **React**

### Partie 1 - créer l'application React

Vous savez probablement que **create-react-app myapp** est le meilleur moyen de créer un modèle de base pour une application React. Non seulement il crée un modèle de base très simple, mais il ajoute également les dépendances requises pour que React fonctionne.

Si vous ne réalisez pas la vraie magie et la puissance pure de cette commande d'une ligne, essayez de créer un répertoire pour React à partir de zéro. Ce n'est qu'alors que vous réaliserez la vraie douleur impliquée. Un grand merci à ces développeurs qui ont mis en place cette commande en premier lieu.

Pour commencer, nous devons installer **create-react-app** sur notre machine.

```
$ npm install -g create-react-app
```

Le drapeau -g dans la commande ci-dessus installe le package NPM globalement sur la machine.

Une fois cela fait, nous utiliserons ce package pour obtenir un modèle de base pour React.

```
$ create-react-app myapp
```

Cela créera un répertoire appelé **myapp**. Maintenant, nous devons naviguer dans le répertoire et exécuter la commande ci-dessous.

```
$ cd myapp
$ npm start
```

Une fois que vous exécutez la commande ci-dessus, un serveur de développement local devrait démarrer et rendre l'application React initiale à l'emplacement **localhost:3000**

J'espère que c'était rapide et facile. Nous avons une dernière étape à compléter, mais regardons d'abord **Firebase**. Nous reviendrons à la dernière étape avec React après cela.

### Partie 2 - Configuration de Firebase

Commençons par comprendre ce qu'est **Firebase** avant de plonger dans sa configuration.

**Firebase** est une plateforme de développement d'applications mobiles et web qui fournit aux développeurs une pléthore d'outils et de services pour les aider à développer des applications de haute qualité, à développer leur base d'utilisateurs et à gagner plus de profit.

Jetons un coup d'œil à l'[histoire](https://en.wikipedia.org/wiki/Firebase) de Firebase avant de le configurer.

#### Une brève histoire

En 2011, avant d'être connu sous le nom de Firebase, c'était une startup appelée Envolve. Envolve, en tant que produit, fournissait aux développeurs une API qui permettait l'intégration de la fonctionnalité de chat en ligne dans leur site web.

L'entreprise a remarqué que les développeurs utilisaient Envolve pour synchroniser les données de l'application, telles que l'état du jeu en temps réel, entre leurs utilisateurs et pas seulement les messages de chat.

Cela a conduit les fondateurs d'Envolve, [James Tamplin](https://twitter.com/JamesTamplin) et [Andrew Lee](https://twitter.com/startupandrew), à séparer le système de chat et l'architecture en temps réel. En avril 2012, Firebase a été créé en tant qu'entreprise distincte qui fournissait un Backend-as-a-Service avec une fonctionnalité en temps réel.

Après son acquisition par Google en 2014, **Firebase** a rapidement évolué pour devenir le géant multifonctionnel de la plateforme mobile et web qu'il est aujourd'hui.

Cette seule image décrit Firebase dans toute sa puissance.

![Image](https://cdn-media-1.freecodecamp.org/images/AHeQftRHGKMPbL1hrGjjNwSy50WR1hznRDum)
_Firebase en un mot_

#### Connexion à Firebase

Alors commençons par ceci : allez sur [https://firebase.google.com/](https://firebase.google.com/) et connectez-vous avec votre compte Google. Une fois connecté, cliquez sur **Aller à la console**. Vous aurez la possibilité de **Créer un nouveau projet**.

Une fois le projet créé, vous avez la possibilité d'ajouter Firebase à toute application mobile Android ou iOS et même à une application web.

### Partie 3 - Firebase et React

Cliquez sur l'option pour **Ajouter Firebase à votre application web**. Vous obtiendrez une boîte de dialogue avec un extrait de code.

![Image](https://cdn-media-1.freecodecamp.org/images/q29q6TWFRpO8fBSqa2Iew9yalAp1cv9xYTrr)

Ajoutez cet extrait de code tout en bas de votre fichier **index.html** dans votre projet. Assurez-vous que cet extrait de code est ajouté avant toutes les autres balises de script dans votre fichier **index.html**.

Si vous regardez attentivement l'image ci-dessus, vous pouvez voir qu'il y a quelques liens fournis tout en bas. Cliquez sur le premier lien et consultez le **Guide de démarrage avec Firebase pour les applications web**. Vous serez présenté avec l'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/RjW3YKRiGKdBHAOOVG4VIaaocSea-mfv03aT)

Cliquez sur Commencer.

![Image](https://cdn-media-1.freecodecamp.org/images/mdzfKVYwIKbA52JVK2Cx06HwKoDZqfIoBffH)

Allez dans votre répertoire racine et entrez la commande ci-dessus dans votre terminal. Cela téléchargera les outils Firebase sur votre machine localement.

L'étape suivante et finale consiste à initialiser Firebase et à déployer le code source dans votre répertoire vers Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/qy-wadU6iKB0MbUpuR5RiKNzchc4SMGZPuxF)

Une fois que vous avez cliqué sur terminer, et que vous avez suivi toutes les étapes ci-dessus et les avez entrées dans votre terminal, vous devriez avoir une liste des derniers enregistrements de déploiement affichés sur la page web.

![Image](https://cdn-media-1.freecodecamp.org/images/u20bSEdlkw0FxqgixU3LvUx7yoChgPS1Iuzg)

### Revenir à React, comme promis

Vous souvenez-vous dans la partie React ci-dessus, j'ai dit que nous reviendrions pour faire une dernière chose ? Nous allons faire cela maintenant.

Naviguez jusqu'au répertoire où votre application est créée.

La façon dont React fonctionne est qu'il vous permet de créer une version de build. Il s'agit d'une version beaucoup plus minifiée de toute la bibliothèque de code mammouth qu'il met en place si vous avez une application assez dense.

Pour obtenir cette version minifiée et compressée, nous pouvons utiliser notre terminal et une commande très utile :

```
$ npm run build
```

Cela crée un nouveau dossier dans votre répertoire d'application nommé **build**. Ce dossier contient quelques fichiers qui sont les pièces les plus essentielles de votre application React entière.

### Conclusion

Si vous avez suivi toutes les étapes avec soin et que vous avez lu un peu de la documentation officielle, tout cela devrait être un jeu d'enfant.

Personnellement, je pense que **Firebase a déjà révolutionné la façon dont les développeurs testent et utilisent l'hébergement en tant que service**. Il s'agit d'une méthode beaucoup plus simple et plus détendue pour héberger vos applications efficacement, sans entrer dans les détails de l'hébergement.