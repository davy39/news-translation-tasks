---
title: Présentation de Matterhorn ? un modèle de serveur API Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T16:27:16.000Z'
originalURL: https://freecodecamp.org/news/announcing-matterhorn-a-node-js-api-server-boilerplate-4994759f1bf6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gpo6knTSfsz0E9qjtCmBEQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Présentation de Matterhorn ? un modèle de serveur API Node.js
seo_desc: 'By Ethan Arrowood

  Happy holidays developers ? Recently, I published Matterhorn ?, an API boilerplate
  project built with Node.js and TypeScript. The API server uses Fastify, a fast and
  low overhead web framework. The project comes with a configured ty...'
---

Par Ethan Arrowood

Joyeuses fêtes aux développeurs ? Récemment, j'ai publié M[atterhorn ?,](https://github.com/Ethan-Arrowood/matterhorn) un projet de modèle d'API construit avec Node.js et TypeScript. Le serveur API utilise Fastify, un framework web rapide et peu gourmand en ressources. Le projet inclut un système de typage configuré (TypeScript), un exécuteur de tests (Jest), un linter (TSLint), et même un pipeline CI (Azure DevOps).

Cet article donnera un bref aperçu du projet et des insights sur certaines décisions de conception.

[**Ethan-Arrowood/matterhorn**](https://github.com/Ethan-Arrowood/matterhorn)  
[_Un projet de modèle d'API construit sur Node.js et TypeScript ? - Ethan-Arrowood/matterhorng_ithub.com](https://github.com/Ethan-Arrowood/matterhorn)

### Aperçu

> ? Psst! Cette section d'aperçu est très similaire à la documentation du projet sur G[itHub](https://github.com/Ethan-Arrowood/matterhorn#matterhorn-)

Commencez rapidement en suivant ces étapes :

1. ? Fork le dépôt
2. ?‍♀️ Clonez-le sur votre ordinateur
3. ?‍♀️ Exécutez `npm run install && npm run dev`
4. ? Modifiez n'importe quel fichier dans `src/`
5. ? Regardez l'application se reconstruire et se relancer automatiquement

✨ C'est tout pour le guide utilisateur de base. Plongeons maintenant dans certaines des commandes disponibles par défaut. Toutes les commandes ci-dessous peuvent être exécutées avec `npm run <script>`. Ce projet utilise les modules npm `opn` et `rimraf` pour permettre des scripts npm agnostiques de plateforme.

* `build` — construit les fichiers TypeScript et les sortie dans `lib/`
* `build:watch` — reconstruit automatiquement les fichiers si des changements sont détectés dans `src/`
* `clean` — supprime récursivement les répertoires `lib/` et `coverage/`
* `clean:build` — supprime récursivement le répertoire `lib/`
* `clean:coverage` — supprime récursivement le répertoire `coverage/`
* `coverage` — exécute la suite de tests et génère des rapports de couverture de code
* `coverage:open` — exécute `npm run coverage` puis ouvre les résultats dans un navigateur
* `dev` — exécute simultanément `build:watch` et `start:watch`
* `lint` — exécute le linter configuré par TSLint sur le répertoire `src/`
* `start` — exécute l'application depuis `lib/`. Assurez-vous d'utiliser `npm run build` d'abord !
* `start:watch` — relance le serveur si de nouveaux changements sont détectés dans `lib/`
* `test` — exécute les tests unitaires définis dans le répertoire `tests/`
* `test:ci` — exécute les tests unitaires et génère les fichiers nécessaires pour l'intégration CI

#### Arguments de ligne de commande et variables d'environnement

Matterhorn implémente un exemple d'utilisation des arguments de ligne de commande et des variables d'environnement. Il utilise `yargs-parser` pour gérer les arguments de ligne de commande. Les arguments de ligne de commande sont passés via la commande de démarrage : `node lib/index.js <command line arguments>`.

L'argument `--log` a été activé comme exemple. Exécuter `npm run start` démarre le projet sans aucun argument de ligne de commande. Cette commande est destinée à être utilisée en production, donc le logging est désactivé par défaut (c'est-à-dire que nous ne passons pas l'argument `--log`).

Si vous utilisez cette commande pour tester votre code localement et que vous souhaitez voir la sortie de logging, exécutez `npm run start -- --log`. Cela passe l'argument de ligne de commande via npm et dans la commande aliasée.

Les variables d'environnement fonctionnent de manière similaire aux arguments de ligne de commande. Elles peuvent être définies de plusieurs manières selon le terminal et le système d'exploitation que vous utilisez. Dans un terminal bash, vous pouvez spécifier des variables d'environnement en préfixant l'assignation à la commande.

Par exemple, ce projet a la variable d'environnement `PORT` activée. Dans un terminal bash, exécutez `PORT=8080 npm run start` pour exécuter l'API sur le port 8080.

### Décisions de conception

J'ai construit ce projet parce que je me suis rendu compte que je copiais et collais constamment des fichiers de configuration pour de nouveaux projets Node.js. J'adore ce que l'équipe `create-react-app` a accompli et j'imagine Matterhorn évoluer en un outil similaire. À l'avenir, j'ai hâte de développer un CLI complet pour aider les développeurs à se lancer avec Node.js et TypeScript encore plus rapidement.

Matterhorn est un projet opinionné. Les systèmes de build et de linting sont configurés selon mes préférences, mais sont très faciles à modifier. Par exemple, dans `tslint.json`, j'ai défini la règle `"semicolon"` comme `false` — pour imposer l'utilisation de points-virgules dans l'application, changez cela en `true`.

De plus, ce projet contient un fichier `azure-pipelines.yml`. Cela définit le pipeline CI (intégration continue) sur Azure DevOps, un outil robuste offert par Microsoft pour permettre aux équipes de planifier plus intelligemment, de collaborer mieux et de livrer plus rapidement avec un ensemble de services de développement modernes. Cela a été une autre décision opinionnée en raison de mon expérience avec l'outil. Il existe de nombreuses autres excellentes options CI telles que Travis CI ou Circle CI que j'espère soutenir à l'avenir.

### J'espère que vous apprécierez !

Merci d'avoir pris le temps de lire cet article et de découvrir Matterhorn ?. Le projet est open source, et j'encourage les développeurs de tous niveaux à venir contribuer. Consultez-le sur G[itHub](https://github.com/Ethan-Arrowood/matterhorn) et si vous souhaitez entendre parler des futures mises à jour ainsi que d'autres choses que je développe, suivez-moi sur T[witter.](https://twitter.com/ArrowoodTech)

Meilleurs vœux ? ~ Ethan Arrowood