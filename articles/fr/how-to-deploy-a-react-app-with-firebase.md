---
title: Comment héberger et déployer une application React avec Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-24T15:55:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-app-with-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-pixabay-207241.jpg
tags:
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: Comment héberger et déployer une application React avec Firebase
seo_desc: 'By Juliet Ofoegbu

  As a front-end developer, you may have used a free hosting platform like Vercel,
  Netlify, or GitHub pages to deploy your front-end projects.

  Personally, I typically use Vercel and Netlify. But I also like trying out different
  web te...'
---

Par Juliet Ofoegbu

En tant que développeur front-end, vous avez peut-être utilisé une plateforme d'hébergement gratuite comme Vercel, Netlify ou GitHub Pages pour déployer vos projets front-end.

Personnellement, j'utilise généralement Vercel et Netlify. Mais j'aime aussi essayer différentes technologies web, et j'ai utilisé les fonctionnalités d'authentification et de stockage de Firebase sur différents projets auparavant. J'ai donc décidé d'utiliser Firebase pour déployer un projet React-TypeScript, et cela s'est très bien passé.

## Qu'est-ce que Firebase ?

[Firebase](https://firebase.google.com/) est une plateforme Backend-as-a-Service (BaaS) appartenant à Google que vous pouvez utiliser pour effectuer des opérations backend comme l'authentification, les fonctionnalités de base de données en temps réel, et ainsi de suite.

Firebase donne aux développeurs front-end la possibilité de travailler avec des fonctionnalités backend sans avoir besoin de se plonger profondément dans le développement backend.

Vous pouvez également utiliser Firebase pour héberger et déployer des projets. Il fournit une URL d'hébergement après le déploiement que vous pouvez partager avec d'autres pour qu'ils puissent voir votre application sur leur propre appareil, tout comme d'autres plateformes d'hébergement et de déploiement.

Suivez ces procédures étape par étape pour déployer avec succès vos projets React en utilisant Firebase.

## Créez votre projet React

Selon la méthode que vous préférez utiliser pour créer des projets React, allez-y et créez-en un. Par exemple, vous pouvez le faire en utilisant CRA : `npx create-react-app nom-de-l-app` ou en utilisant Vite : `npm create vite@latest` (recommandé).

Utilisez `cd nom-de-l-app` pour naviguer vers le répertoire du projet. Ensuite, `npm start` ou `npm run dev` pour démarrer votre serveur de développement. Construisez votre projet souhaité, créez un dépôt GitHub et poussez le projet vers GitHub.

Nous avons maintenant terminé la première partie de la procédure. Passons à la partie suivante.

## Comment configurer et installer Firebase

Si vous n'avez pas de compte sur Firebase, allez sur ce [site](https://firebase.google.com/) pour créer un compte sur Firebase ou connectez-vous si vous en avez déjà un. Si vous avez un compte Google, il sera facile de créer un compte sur Firebase.

Après vous être connecté avec succès, vous devrez créer un projet sur Firebase. Voici comment faire :

### Étape 1 : Tableau de bord de la console Firebase.

Allez dans le tableau de bord de votre console Firebase, où vous devriez voir le texte "Go to console" en haut à droite de votre page après vous être connecté.

La page qui s'ouvre aura un bouton "Create a project". Cliquez sur ce bouton et il vous mènera à la page où vous entrerez les détails de votre projet (Étape 2).

Si vous avez déjà utilisé Firebase, cela signifie que vous avez déjà des projets sur Firebase. Dans ce cas, il affichera une page comme celle ci-dessous affichant une liste de vos projets et une case pour ajouter un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Firebase-console---Google-Chrome-25_07_2023-19_24_33.jpg)
_Console Firebase_

### Étape 2 : Créer un nouveau projet

Cliquez sur la carte "Add project". Une page vous demandant de donner un nom à votre projet s'ouvrira.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Firebase-console---Google-Chrome-25_07_2023-19_24_55.png)
_Création d'un projet_

### Étape 3 : Remplir les détails du projet

Dans cet exemple, j'ai nommé le projet "My React APP".

Si vous êtes nouveau sur Firebase, vous devrez cocher la case "Accept Firebase terms" et la deuxième case.

Cliquez sur le bouton "continue". La page suivante qui s'affiche a un bouton bascule pour activer ou désactiver Google Analytics pour le projet. Désactivez ce bouton bascule car nous n'avons pas besoin de Google Analytics pour cette démonstration.

Cliquez sur le bouton "Create Project" et il devrait commencer à créer votre projet Firebase.

Si ce n'est pas la première fois que vous utilisez Firebase, cliquez sur le bouton "Continue" sur la page ci-dessus, désactivez Google Analytics et créez un nouveau projet.

### Étape 4 : Installer Firebase et les outils Firebase

L'étape suivante consiste à aller dans le terminal de votre projet sur VS Code, votre interface de ligne de commande ou tout autre éditeur de code que vous utilisez. Assurez-vous d'être dans le dossier principal du projet que vous souhaitez déployer, puis installez Firebase dans le projet en utilisant cette commande : `npm install firebase`.

Ensuite, installez les outils Firebase que nous utiliserons pour l'hébergement et le déploiement en utilisant cette commande : `npm install -g firebase-tools`.

### Étape 5 : Se connecter à Firebase en utilisant le terminal

Après avoir configuré le projet Firebase et installé les dépendances nécessaires, vous devrez vous connecter à Firebase sur le terminal en utilisant cette commande : `firebase login`.

Une invite vous demandant de sélectionner Oui ou Non à une question sur le fait de "Permettre à Firebase de collecter des informations sur l'utilisation et les rapports d'erreurs de la CLI et de la suite d'émulateurs" apparaîtra. Sélectionnez l'option "Yes".

### Étape 6 : Sélectionner le compte

Une fenêtre s'ouvrira sur le navigateur par défaut qui vous demandera de sélectionner votre compte Firebase pour la connexion.

Après une authentification réussie, un message de succès apparaîtra sur le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-login-on-terminal.jpg)
_Connexion à l'interface de ligne de commande Firebase_

### Étape 7 : Exécuter la construction du projet

Utilisez la commande `npm run build` pour construire les scripts du projet. Cette commande génère automatiquement une version de production de votre application en regroupant tous les fichiers JavaScript, CSS et autres ressources nécessaires dans un seul dossier "build" dans le répertoire du projet.

Ce processus est important car il optimise le code et les ressources pour les performances. Cela réduit la taille globale de l'application et la rend efficace pour le déploiement.

Après l'achèvement réussi de la deuxième partie, nous en arrivons à la partie suivante de ce processus de déploiement.

## Comment initialiser Firebase

Maintenant, nous devons initialiser Firebase, alors nous allons passer en revue les étapes pour le faire.

### Étape 1 : Initialiser Firebase

Initialisez Firebase pour ce projet en utilisant cette commande sur le terminal : `firebase init`. Il vous informera que vous êtes sur le point d'initialiser un projet Firebase dans le répertoire.

Certaines invites qui apparaîtront après cette commande sont : "Are you ready to proceed?", à laquelle vous taperez "Y" pour "Yes".

L'invite suivante est : "Which Firebase features do you want to set up for this directory?". Utilisez la touche fléchée vers le bas de votre clavier pour pointer sur l'option "Hosting:Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys". Appuyez sur la barre d'espace puis sur entrée.

### Étape 2 : Configuration du projet

Cette étape connecte votre répertoire de projet avec le projet Firebase. Lorsque vous êtes invité à sélectionner un projet, choisissez l'option "Use an existing project".

Ensuite, lorsque vous êtes invité à "select a default Firebase project for the directory", sélectionnez le projet Firebase particulier que vous avez créé dans la partie 1 de ce processus.

Vous pourriez voir d'autres options de projet si vous avez plus d'un projet Firebase sur votre console Firebase.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-init.jpg)
_Connexion du projet à Firebase._

### Étape 3 : Configuration de l'hébergement

Ce processus fera apparaître quelques invites auxquelles vous devrez répondre.

La première est : "What do you want to use as your public directory?", à laquelle vous choisirez ou taperez "build".

Ensuite, lorsque vous êtes invité à "Configure as a single-page app (rewrite all urls to /index.html)", sélectionnez l'option "Y" ou "Yes".

Lorsque vous êtes invité à "Set up automatic builds and deploys with GitHub?", choisissez l'option "Yes". De plus, lorsque vous êtes invité avec la question "File build/index.html already exists. Overwrite?", choisissez "No".

### Étape 4 : Autoriser Firebase avec GitHub

Vous devrez autoriser Firebase avec votre compte GitHub. Une fenêtre s'ouvrira sur votre navigateur qui vous demandera d'autoriser Firebase dans votre GitHub et de saisir votre mot de passe GitHub. Après une authentification réussie, vous recevrez un message de succès sur votre terminal avec votre nom d'utilisateur GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-hosting-set-up.jpg)
_Configuration de l'hébergement Firebase_

Si vous avez suivi avec succès et que vous êtes arrivé à ce stade, vous avez bien fait jusqu'à présent. Nous sommes à mi-chemin du déploiement de notre projet.

## Comment choisir un dépôt GitHub et configurer le flux de travail GitHub

### Étape 1 : Sélectionner le dépôt GitHub

Tout d'abord, vous devrez taper le dépôt GitHub que vous souhaitez utiliser pour configurer un flux de travail GitHub pour les déploiements Firebase.

Le format pour faire cela est "username/repository". Souvenez-vous dans la partie 1 de ce processus, vous avez construit un projet et l'avez poussé vers GitHub. Ce dépôt GitHub est ce que vous utiliserez.

Par exemple, disons que votre nom d'utilisateur GitHub est "CoderDev" et que le dépôt du projet est "Firebase-Deployment". Vous taperez "CoderDev/Firebase-Deployment" dans le terminal. Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-github-4.jpg)

### Étape 2 : Jeton secret GitHub

Après avoir configuré un flux de travail GitHub, il créera un compte de service avec des permissions d'administrateur Firebase Hosting et téléchargera le JSON du compte de service vers GitHub en tant que jeton secret.

Vous pouvez également voir ce jeton secret sur GitHub. Pour ce faire, allez dans le dépôt du projet et basculez vers l'onglet "Settings". Dans le panneau de gauche de la page des paramètres, cliquez sur le menu déroulant "Secrets and variables" et sélectionnez l'option "Actions". Il affichera votre jeton secret comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-github-secrets-1.jpg)
_Jeton secret_

### Étape 3 : Configurer le flux de travail

Vous serez invité avec la question "Set up the workflow to run a build script before every deploy?". Choisissez "Yes" pour cela.

On vous demandera également : "What script should be run before every deploy? (npm ci && npm run build) npm run build". Tapez ceci dans le terminal : `npm ci && npm run build`. Cela créera un fichier de flux de travail dans le répertoire du projet.

Vous verrez maintenant le fichier "firebase-hosting-pull-request.yml" à l'intérieur d'un dossier ".github/workflows" dans votre structure de dossier de projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-github-3.jpg)
_Premier fichier de flux de travail GitHub_

### Étape 4 : Déploiement automatique

Ensuite, on vous demandera si vous souhaitez "Set up automatic deployment to your site's live channel when a PR is merged". Sélectionnez "Yes".

Lorsque vous êtes invité à entrer le nom de la branche GitHub associée au canal live de votre site, tapez ou sélectionnez "main". Cela créera un autre fichier de flux de travail "firebase-hosting-merge.yml" à l'intérieur du dossier ".github/workflows".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-setup-auto.jpg)
_Deuxième fichier de flux de travail GitHub_

### Étape 5 : Générer des dossiers

Les deux opérations effectuées ci-dessus généreront deux dossiers dans votre répertoire de projet. L'un nommé "firebase.json" est l'endroit où les informations de configuration seront écrites, et l'autre nommé ".firebaserc" est l'endroit où les informations du projet seront écrites.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-2-folders.jpg)
_Création de dossiers_

C'est tout ce que vous avez à faire pour initialiser Firebase dans votre projet.

Ces processus sont un peu longs, mais la bonne nouvelle est que tout ce qui reste à faire est de déployer sur Firebase.

## Comment déployer sur Firebase

### Exécuter la commande de déploiement

Exécutez la commande de déploiement `firebase deploy`. Attendez qu'elle se déploie. Une fois terminée, un message de succès s'affichera sur votre terminal avec une URL d'hébergement. C'est le lien live du projet avec une extension de domaine "web.app".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/firebase-deploy--2-.jpg)
_Déploiement Firebase_

C'est tout ! Nous avons terminé le déploiement de notre projet React avec Firebase.

Maintenant, chaque fois que vous ajoutez, commitez et poussez de nouvelles modifications vers ce dépôt GitHub, il construira automatiquement l'application et la redéploiera sur Firebase afin que les modifications soient reflétées dans le site live.

Ce build et ce redéploiement automatiques sont possibles car plus tôt, dans le processus d'initialisation de Firebase, nous avons sélectionné l'option 'yes' pour configurer les builds et déploiements automatiques avec GitHub.

Nous avons également sélectionné l'option "Yes" pour configurer le flux de travail afin d'exécuter le script de build avant chaque déploiement et spécifié les scripts qui doivent être exécutés avant chaque déploiement.

Pour voir comment ce déploiement est effectué après chaque push vers le dépôt, allez dans le dépôt GitHub de ce projet. Basculez vers l'onglet "Actions" pour voir comment l'application est construite et déployée.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/fixed-features-page---OmaJuliet_Liberty-Tours@ad63f32---Google-Chrome-27_07_2023-13_13_32.png)
_Action de build et de déploiement depuis GitHub._

Vous pourriez rencontrer des erreurs lors du déploiement. La bonne chose est que directement sur cette page d'actions GitHub, vous pouvez tracer pour voir d'où vient l'erreur dans l'application.

Disons que vous travaillez avec TypeScript dans le projet, et que vous avez déclaré une fonction et ne l'avez pas utilisée, ou que vous avez appelé un hook et ne l'avez pas utilisé. Votre application peut fonctionner comme elle le devrait sur le navigateur.

Mais lors du déploiement, cela pourrait poser un problème ou provoquer un avertissement et vous devrez le corriger, le commiter et le pousser à nouveau vers le dépôt pour corriger l'erreur. Une fois que vous avez fait cela et que le déploiement est réussi, la page d'action devrait ressembler à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/fixing-deployment-issue---OmaJuliet_Liberty-Tours@fce163f---Google-Chrome-25_07_2023-22_09_27-1.jpg)
_Correction du problème de déploiement_

## Conclusion

Déployer votre projet en utilisant Firebase peut sembler au début un long processus. Mais si vous suivez les étapes de cet article, vous devriez être prêt à partir.

Vous pouvez facilement déployer votre application sur Firebase Hosting et profiter de ses puissantes capacités telles que les processus automatiques, le processus de déploiement simplifié et l'intégration continue avec GitHub en suivant les étapes faciles de cet article.

Si vous souhaitez en savoir plus sur toutes les fonctionnalités que Firebase offre aux développeurs, allez sur la [Documentation officielle de Firebase](https://firebase.google.com/docs) et explorez.