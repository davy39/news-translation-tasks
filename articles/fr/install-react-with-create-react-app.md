---
title: Comment installer React.js avec create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-28T00:12:06.000Z'
originalURL: https://freecodecamp.org/news/install-react-with-create-react-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c980e740569d1a4ca17e8.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: npm
  slug: npm
- name: React
  slug: react
seo_title: Comment installer React.js avec create-react-app
seo_desc: 'By Cem Eygi

  React is one of the most popular JavaScript libraries in the web development field
  today.

  As a Frontend Developer, I have personally worked with React in my projects and
  probably will continue to work with it in the future. One of the ste...'
---

Par Cem Eygi

React est l'une des bibliothèques JavaScript les plus populaires dans le domaine du développement web aujourd'hui.

En tant que développeur Frontend, j'ai personnellement travaillé avec React dans mes projets et je continuerai probablement à travailler avec dans le futur. L'une des étapes avec lesquelles beaucoup de gens ont du mal est le processus d'installation/configuration de React.

Alors commençons par les bases. Dans cet article, vous allez apprendre comment installer et exécuter une application React de manière facile.

Puisque l'intérêt pour l'apprentissage de React augmente également rapidement jour après jour, j'ai également décidé de créer des tutoriels vidéo sur React sur [ma chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q/). Voici une version vidéo de ce tutoriel :

%[https://youtu.be/QJZ-xgt4SJo]

## Comment télécharger et installer Node.js

Tout d'abord, vous allez avoir besoin de NPM (ou Yarn, alternativement). Utilisons NPM pour cet exemple.

Si vous ne l'avez pas installé sur votre système, alors vous devez vous rendre sur le [site officiel de Node.js](https://nodejs.org/en/) pour télécharger et installer Node, qui inclut également NPM (Node Package Manager).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nodejs.png)
_[Site officiel de Node.js](https://nodejs.org/en/)_

Sélectionnez le bouton "Recommandé pour la plupart des utilisateurs" et téléchargez la version actuelle pour votre système d'exploitation.

Après avoir téléchargé et installé Node, ouvrez votre terminal/invite de commande et exécutez `node -v` et `npm -v` pour voir quelles versions vous avez.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/t1.png)

Votre version de NPM doit être au moins 5.2.0 ou plus récente car create-react-app nécessite que nous ayons [NPX](https://github.com/npm/npm/releases/tag/v5.2.0) installé. Si vous avez une version plus ancienne de NPM, exécutez cette commande pour la mettre à jour :

```
npm install -g npm
```

## Qu'est-ce que create-react-app ?

Étant donné que c'est compliqué et que cela prend beaucoup de temps, nous ne voulons pas configurer React manuellement. create-react-app est une méthode beaucoup plus facile qui effectue toutes les configurations et installations de packages nécessaires automatiquement pour nous et démarre une nouvelle application React localement, prête pour le développement.

Un autre avantage de l'utilisation de create-react-app est que vous n'avez pas à vous occuper des configurations de Babel ou Webpack. Toutes les configurations nécessaires seront faites par create-react-app pour vous.

[Selon la documentation React](https://reactjs.org/docs/create-a-new-react-app.html), create-react-app est l'une des méthodes officiellement supportées pour créer des applications monopages dans React. Vous pouvez trouver d'autres méthodes [ici](https://reactjs.org/docs/create-a-new-react-app.html).

### Comment installer Create-React-App

Pour installer votre application, rendez-vous d'abord dans votre espace de travail (bureau ou un dossier) et exécutez la commande suivante :

```js
npx create-react-app my-app
```

Le processus d'installation peut prendre quelques minutes. Une fois terminé, vous devriez voir un dossier apparaître dans votre espace de travail avec le nom que vous avez donné à votre application.

> Remarque : Si vous êtes sur Mac et que vous recevez des erreurs de permission, n'oubliez pas de devenir super utilisateur d'abord avec la commande sudo.

### Comment exécuter l'application que vous avez créée avec Create-React-App

Une fois l'installation terminée, changez de répertoire pour celui où votre application a été installée :

```
cd my-app
```

et enfin, exécutez `npm start` pour voir votre application en direct sur localhost :

```
npm start
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/rw.png)

Si vous voyez quelque chose comme ceci dans votre navigateur, vous êtes prêt à travailler avec React. Félicitations ! :)

Merci d'avoir lu !