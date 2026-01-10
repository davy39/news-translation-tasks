---
title: Comment exécuter les défis Backend de freeCodeCamp en local
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-15T17:31:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-the-freecodecamp-backend-challenges-locally
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/joshua-reddekopp-GkFQEOubrCo-unsplash.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Web Development
  slug: web-development
seo_title: Comment exécuter les défis Backend de freeCodeCamp en local
seo_desc: 'For the freeCodeCamp Back End Development and APIs certification, you can
  do all of the challenges locally and submit the local server link. But how does
  that work exactly?

  In this article, I will walk you through step by step how to setup the backen...'
---

Pour la certification [Back End Development and APIs](https://www.freecodecamp.org/learn/back-end-development-and-apis/) de freeCodeCamp, vous pouvez réaliser tous les défis en local et soumettre le lien du serveur local. Mais comment cela fonctionne-t-il exactement ?

Dans cet article, je vais vous guider étape par étape pour configurer les défis backend sur votre ordinateur local et soumettre le lien localhost.

## Comment cloner le dépôt GitHub de freeCodeCamp

Pour la section [Managing Packages with NPM](https://www.freecodecamp.org/learn/back-end-development-and-apis/#managing-packages-with-npm), vous devrez utiliser ce [dépôt GitHub](https://github.com/freeCodeCamp/boilerplate-npm/).

Sur le dépôt GitHub, cliquez sur le bouton vert `Code` situé sur le côté droit de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-2.27.21-PM.png)

Copiez l'URL ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-2.28.19-PM.png)

Si vous utilisez un Mac, ouvrez l'application Terminal. Si vous utilisez Windows, ouvrez l'invite de commande.

Dans la ligne de commande, exécutez `cd Desktop` et appuyez sur `enter` pour changer de répertoire vers votre bureau.

```
jessicawilkins@Dedrias-MacBook-Pro-2 ~ % cd Desktop
```

Vous devriez maintenant être dans le répertoire Desktop et voir ce résultat dans la ligne de commande.

```
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop %
```

Ensuite, exécutez `git clone [https://github.com/freeCodeCamp/boilerplate-npm.git](https://github.com/freeCodeCamp/boilerplate-npm.git)`. C'est l'URL que vous avez copiée précédemment depuis GitHub.

```
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % git clone https://github.com/freeCodeCamp/boilerplate-npm.git
```

Vous devriez voir ce résultat dans la ligne de commande pour le clonage réussi du dossier.

```
Cloning into 'boilerplate-npm'...
remote: Enumerating objects: 46, done.
remote: Total 46 (delta 0), reused 0 (delta 0), pack-reused 46
Unpacking objects: 100% (46/46), done.
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop %
```

Vous devriez pouvoir voir le nouveau dossier sur votre bureau.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-2.43.24-PM.png)

## Comment installer node_modules

Dans la ligne de commande, exécutez `cd boilerplate-npm` pour changer de répertoire vers le dossier que nous venons de cloner depuis GitHub.

```
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % cd boilerplate-npm
```

Ensuite, exécutez `npm install` pour installer le dossier `node_modules`. Le dossier `node_modules` contient toutes les dépendances nécessaires pour exécuter votre projet.

Sans ce dossier, vous ne pourrez pas exécuter aucun des défis. C'est pourquoi nous devons l'installer dans le dossier du projet.

```
jessicawilkins@Dedrias-MacBook-Pro-2 boilerplate-npm % npm install
```

Une fois installé, vous devriez voir ce résultat dans la ligne de commande :

```
added 50 packages, and audited 51 packages in 2s

found 0 vulnerabilities
jessicawilkins@Dedrias-MacBook-Pro-2 boilerplate-npm %
```

## Comment soumettre le lien localhost

Allez dans votre éditeur de code préféré et ouvrez le dossier du projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-3.04.51-PM.png)

Ensuite, complétez le premier [défis](https://www.freecodecamp.org/learn/back-end-development-and-apis/managing-packages-with-npm/how-to-use-package-json-the-core-of-any-node-js-project-or-npm-package) qui consiste à ajouter un auteur à votre fichier `package.json`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-3.05.54-PM.png)

Retournez à la ligne de commande et exécutez `npm start` qui démarrera le serveur local.

```
jessicawilkins@Dedrias-MacBook-Pro-2 boilerplate-npm % npm start
```

Vous devriez voir ce résultat dans la ligne de commande :

```
> start
> node server.js

Node.js listening on port 3000
```

Allez dans votre navigateur et ouvrez un nouvel onglet. Tapez [`http://localhost:3000/`](http://localhost:3000/).

Vous devriez voir ce résultat dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-3.14.23-PM.png)

C'est le serveur local que vous utiliserez pour tous les défis backend.

Pendant que le serveur est toujours en cours d'exécution, allez au [premier défis](https://www.freecodecamp.org/learn/back-end-development-and-apis/managing-packages-with-npm/how-to-use-package-json-the-core-of-any-node-js-project-or-npm-package) et soumettez le lien localhost.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-3.16.40-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-3.18.16-PM.png)

Une fois que vous avez terminé les défis, vous pouvez arrêter le serveur en utilisant `Ctrl+C` dans la ligne de commande.

Ce sont les étapes pour compléter les défis backend de freeCodeCamp en utilisant le localhost.

Pour les autres sections de la certification [Back End Development and APIs](https://www.freecodecamp.org/learn/back-end-development-and-apis/), vous devrez utiliser le dépôt GitHub correspondant.

Pour la section [Basic and Express](https://www.freecodecamp.org/learn/back-end-development-and-apis/basic-node-and-express/meet-the-node-console), vous devez cloner [ce dépôt GitHub](https://github.com/freeCodeCamp/boilerplate-express/).

Pour la section [MongoDB and Mongoose](https://www.freecodecamp.org/learn/back-end-development-and-apis/mongodb-and-mongoose/install-and-set-up-mongoose), vous devez cloner [ce dépôt GitHub](https://github.com/freeCodeCamp/boilerplate-mongomongoose/).