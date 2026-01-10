---
title: Comment configurer l'intégration et le déploiement continus pour votre application
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T01:27:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-continuous-integration-and-deployment-for-your-react-app-d09ae4525250
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJiNN3izrhZXN6TNm0koMg.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment configurer l'intégration et le déploiement continus pour votre
  application React
seo_desc: 'By Zac Kwan

  Setting up a React development environment can be confusing and daunting to newcomers.
  You might have heard developers talking about how different packages like babel,
  Webpack and so on, are needed as well (but this is debatable).

  With Re...'
---

Par Zac Kwan

La configuration d'un environnement de développement **React** peut être déroutante et intimidante pour les nouveaux venus. Vous avez peut-être entendu des développeurs parler de différents packages comme **babel**, **Webpack** et autres, qui sont également nécessaires (mais cela est discutable).

Avec la popularité croissante de React, il existe quelques projets de modèle qui visent à aider les développeurs à créer un environnement de développement React approprié. [**create-react-app**](https://github.com/facebookincubator/create-react-app) est l'un des modèles de démarrage les plus populaires.

Il vise à permettre aux développeurs de créer une application React avec **zéro configuration de build**.

Les développeurs n'ont plus à se soucier de la manière dont `webpack` doit être configuré, de ce qui doit être configuré avec `babel` pour utiliser `es6`, ou de quel package `linter` et `test` utiliser. Tout fonctionnera directement. **Oui, c'est si facile !**

Pour les développeurs qui doivent gérer la configuration sous-jacente, il dispose d'une commande `npm run eject` qui leur permet de modifier la configuration et de faire ce qu'ils ne pouvaient pas faire auparavant. La seule chose à noter est que une fois `eject` exécuté, il n'est pas possible de revenir en arrière.

### Stack de développement pour React

J'ai écrit le guide suivant pour aider les développeurs à construire un **stack d'intégration continue et de déploiement continu pour leur application React**. Nous utiliserons [**CircleCI**](https://circleci.com), [**CodeClimate**](https://codeclimate.com)**,** et [**Heroku**](https://heroku.com). Si vous n'avez pas de compte sur l'un de ces services, inscrivez-vous — ils sont GRATUITS !

À la fin, nous aurons une application React dans un [Dépôt Github](https://github.com/Zaccc123/awesome-cicd-react) qui déployera automatiquement toute modification sur la branche `_master_` vers [**Heroku**](https://heroku.com) après que tous les tests soient passés. [Voici](https://awesome-cicd-react.herokuapp.com) un exemple du site **React** déployé.

#### **Commençons !**

La première étape consiste à suivre le guide [**create-react-app**](https://github.com/facebookincubator/create-react-app) pour créer une nouvelle application React. Faites ceci :

```
$ npm install -g create-react-app
$ create-react-app my-react-app
$ cd my-react-app/
$ npm start
```

Ensuite, le navigateur devrait automatiquement ouvrir une page à l'adresse [http://localhost:3000/](http://localhost:3000/](http://localhost:3000/).). Si vous voyez une page **Bienvenue dans React** en cours d'exécution, tout est bon.

#### **Configuration de CircleCI**

Ensuite, nous devons ajouter une petite configuration pour configurer [**CircleCI**](https://circleci.com) pour notre projet. Créez un dossier `.circleci` et un fichier `config.yml` dans ce répertoire et ajoutez ce qui suit :

```
version: 2
jobs:
  build:
    docker:
      - image: circleci/node:8
    steps:
      - checkout
      - restore_cache: # étape spéciale pour restaurer le cache des dépendances
          key: dependency-cache-{{ checksum "package.json" }}
      - run:
          name: Configuration des dépendances
          command: npm install
      - run:
          name: Configuration du test-reporter de Code Climate
          command: |
            curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
            chmod +x ./cc-test-reporter
      - save_cache: # étape spéciale pour sauvegarder le cache des dépendances
          key: dependency-cache-{{ checksum "package.json" }}
          paths:
            - ./node_modules
      - run: # exécuter les tests
          name: Exécuter les tests et la couverture
          command: |
            ./cc-test-reporter before-build
            npm test -- --coverage
            ./cc-test-reporter after-build --exit-code $?
```

Cette configuration est pour [CircleCI 2.0](https://circleci.com/docs/2.0/). Ils mettent fin à [Circle 1.0](https://circleci.com/docs/1.0/) le 31 août 2018.

L'étape `build` configure un `node:8` avec une image Docker. Il nécessite `v6` ou supérieur pour fonctionner.

Dans `steps`, nous commençons par vérifier le projet, restaurer à partir du cache si disponible, puis installer les dépendances. Nous installons également `cc-test-reporter`, un outil fourni par CodeClimate pour envoyer un rapport de couverture.

Nous exécutons ensuite le `test` entre les commandes `before-build` et `after-build` selon la [documentation de CodeClimate](https://docs.codeclimate.com/docs/configuring-test-coverage). Cela notifie CodeClimate du rapport en attente et, une fois terminé, il envoie soit le rapport, soit un statut d'échec.

#### **Configuration de Git**

Créez un dépôt dans [**Github**](https://github.com) et faites ce qui suit :

```
$ git init
$ git remote add origin git@github.com:username/new-repo-here
$ git add .
$ git commit -m "first commit"
$ git push -u origin master
```

Cela poussera le projet que nous avons créé vers GitHub.

#### **Construction et test du projet**

Rendez-vous sur [**CircleCI**](https://circleci.com), connectez-vous et construisez le projet nouvellement créé. À la fin de la construction, vous devriez voir un échec sur `Run Test and Coverage`.

![Image](https://cdn-media-1.freecodecamp.org/images/xfFDemobQXl0bQqLcFTPlYH2nbZrCbSOSTey)

### **Configuration de CodeClimate**

L'échec ci-dessus est dû au fait que nous ne sommes pas encore autorisés à publier un rapport sur CodeClimate. Donc, maintenant, rendez-vous sur [**CodeClimate**](https://codeclimate.com), connectez-vous et construisez le projet GitHub créé. Nous devrions obtenir ceci à la fin de l'analyse :

![Image](https://cdn-media-1.freecodecamp.org/images/KbRpYcTUdK-5JfYQkC4PtenUIGlAEUKfRckI)
_analyse de codeclimate_

Pour résoudre le problème de CircleCI et utiliser les commentaires de `Test Coverage`, nous aurons besoin de l'`ID du Test Reporter`. Cela peut être récupéré dans l'onglet `Settings > Test Coverage`. Copiez l'`ID du Test Reporter` sans le partager avec qui que ce soit.

Dans [**CircleCI**](https://circleci.com), naviguez vers `Project > Settings > Environment variable` et ajoutez `CC_TEST_REPORTER_ID` avec l'`ID du Test Reporter` copié.

![Image](https://cdn-media-1.freecodecamp.org/images/hwSIlgr-NHjjVUsevYMsgvQ2EKWolGDHi5td)

### **Configuration du déploiement sur Heroku**

Pour déployer React sur [**Heroku**](https://heroku.com), nous utiliserons un [buildpack](https://github.com/mars/create-react-app-buildpack). Faites ce qui suit :

```
$ heroku create REPLACE_APP_NAME_HERE — buildpack https://github.com/mars/create-react-app-buildpack.git
$ git push heroku master
$ heroku open
```

Nous avons poussé la dernière branche `master` vers `heroku` avec `git push heroku master`. Une page web s'ouvrira à la fin, affichant la page **Bienvenue dans React**.

Ensuite, nous devrons naviguer vers l'application nouvellement créée dans le [**Tableau de bord Heroku**](https://dashboard.heroku.com/apps) pour configurer le déploiement automatisé. Faites ce qui suit sur le tableau de bord :

* Allez dans l'onglet **Deploy** et **Connect** au dépôt GitHub correct.
* **Activez** le déploiement automatique et **cochez** `Attendre que le CI passe avant le déploiement`.

![Image](https://cdn-media-1.freecodecamp.org/images/FVc8xtFqrBOMAIGYlRpSJJ1PBnlfCitMxkHr)
_activer le déploiement automatique_

### **Nous avons terminé !**

En quelques étapes, nous avons un ensemble complet d'intégration et de déploiement continus automatisés prêt. Maintenant, avec chaque commit qui est poussé vers [**GitHub**](https://github.com), il enverra un déclencheur à [**CircleCI**](https://circleci.com) et [**CodeClimate**](https://codeclimate.com). Une fois les tests passés, s'il s'agissait de la branche master, il sera également automatiquement déployé vers [**Heroku**](https://heroku.com)**.**

Voir le dépôt exemple [**ici**](https://github.com/Zaccc123/awesome-cicd-react) et le site web déployé [**ici**](https://awesome-cicd-react.herokuapp.com) !

### Conclusion

Il s'agit d'une mise à jour de mon précédent [article](https://medium.com/@Zaccc123/https-medium-com-zaccc123-continuous-integration-and-deployment-setup-for-react-app-7b5f4bd76cdd) il y a presque un an. L'utilisation de CircleCI a été mise à jour vers `2.0`, et nous utilisons également le `cc-test-reporter` mis à jour par `CodeClimate`. Si vous êtes intéressé par la migration, vous pouvez consulter la [demande de tirage](https://github.com/Zaccc123/awesome-cicd-react/pull/3).

### Merci d'avoir lu ! Si vous aimez cela, n'hésitez pas à cliquer sur ???

J'aime lire et écrire sur la technologie et les produits, en particulier ceux liés à l'augmentation de la productivité des développeurs. Vous pouvez me dire bonjour sur mon [Twitter](https://twitter.com/Zaccc123) ou sur mon [blog](https://zackwan.app).