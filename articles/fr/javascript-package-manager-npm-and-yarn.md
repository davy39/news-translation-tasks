---
title: Gestionnaire de paquets JavaScript – Guide complet sur NPM et Yarn
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-04-05T00:08:08.000Z'
originalURL: https://freecodecamp.org/news/javascript-package-manager-npm-and-yarn
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/package-manager-npm-and-yarn-explained-curology-pDsmoI5j3B8-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: npm
  slug: npm
- name: software development
  slug: software-development
- name: Yarn
  slug: yarn
seo_title: Gestionnaire de paquets JavaScript – Guide complet sur NPM et Yarn
seo_desc: 'A package manager is a tool developers use to automate finding, downloading,
  installing, configuring, upgrading, and removing a system''s packages.

  This article will show you all you need to get started with package managers like
  NPM and Yarn.

  But why...'
---

Un **gestionnaire de paquets** est un outil que les développeurs utilisent pour automatiser la recherche, le téléchargement, l'installation, la configuration, la mise à jour et la suppression des paquets d'un système.

Cet article vous montrera tout ce dont vous avez besoin pour commencer avec des gestionnaires de paquets comme NPM et Yarn.

Mais pourquoi exactement avons-nous besoin d'un gestionnaire de paquets dans notre flux de travail de développement ? Découvrons-le.

## Pourquoi avez-vous besoin d'un gestionnaire de paquets ?

Supposons qu'il n'y ait pas de gestionnaires de paquets. Dans ce cas, vous devriez faire manuellement ce qui suit :

* Trouver tous les paquets corrects pour votre projet
* Vérifier que les paquets n'ont pas de vulnérabilités connues
* Télécharger les paquets
* Les installer à l'emplacement approprié
* Suivre les nouvelles mises à jour pour tous vos paquets
* Mettre à jour chaque paquet dès qu'une nouvelle version est disponible
* Supprimer les paquets dont vous n'avez plus besoin

Gérer manuellement des dizaines ou des centaines de paquets est une tâche fastidieuse et chronophage.

Par conséquent, les gestionnaires de paquets – tels que [NPM](https://www.npmjs.com/), [pNPM](https://pnpm.io/), [Bower](https://bower.io/), et [Yarn](https://yarnpkg.com/) – aident à automatiser et à éliminer le processus fastidieux de gestion manuelle de tous vos paquets.

Gardez à l'esprit qu'un gestionnaire de paquets n'est pas la même chose qu'un registre de paquets. Alors, découvrons la principale différence.

## Gestionnaire de paquets vs. Registre de paquets – Quelle est la différence ?

Un **gestionnaire de paquets** est un outil que les développeurs utilisent pour trouver, télécharger, installer, configurer, mettre à jour et désinstaller automatiquement les paquets d'un ordinateur.

NPM (Node Package Manager) et Yarn (Yet Another Resource Negotiator) sont deux gestionnaires de paquets populaires.

Un **registre de paquets** est une base de données (stockage) pour des milliers de paquets (bibliothèques, plugins, frameworks ou outils).

En d'autres termes, un registre de paquets est l'endroit où les paquets sont publiés et installés.

Le [registre NPM](https://www.npmjs.com/) et [GitHub Packages](https://github.com/features/packages) sont deux registres de paquets populaires.

Maintenant que nous savons ce qu'est un gestionnaire de paquets et pourquoi il est nécessaire, nous pouvons discuter de l'utilisation des deux plus populaires – NPM et Yarn.

Notez qu'il existe de nombreux débats NPM vs. Yarn – nous les éviterons donc ici car le meilleur gestionnaire de paquets est celui qui fonctionne le mieux pour vous.

Par conséquent, cet article vous montrera comment NPM et Yarn fonctionnent plutôt que de vous dire quel gestionnaire de paquets est le meilleur. C'est ensuite à vous de décider lequel vous préférez.

Alternativement, vous pouvez choisir d'utiliser NPM pour un projet spécifique et Yarn pour un autre – selon le gestionnaire que vous jugez le mieux adapté au travail.

Alors, sans plus tarder, commençons par apprendre à installer les deux gestionnaires.

## Comment installer Node Package Manager (NPM)

NPM est installé automatiquement lors de l'installation de Node.

Par conséquent, pour installer NPM sur votre système, rendez-vous sur le site [NodeJS](https://nodejs.org/en/) et obtenez la [dernière version LTS ou la version actuelle](https://tamalweb.com/which-nodejs-version).

## Comment installer Yarn

Il est préférable d'installer Yarn via NPM. Donc, installez d'abord NPM depuis le site [Node.js](https://nodejs.org/en/).

Une fois que vous avez installé NPM, procédez à l'installation de Yarn comme suit :

```bash
npm install -g yarn
```

## Comment vérifier la version de Node installée

Pour vérifier la version de Node.js installée sur votre système, exécutez :

```bash
node -v
```

Le drapeau `-v` dans l'extrait ci-dessus est un raccourci pour `--version`.

## Comment vérifier la version de NPM installée

Pour vérifier la version de NPM installée sur votre système, exécutez :

```bash
npm -v
```

## Comment vérifier la version de Yarn installée

Pour vérifier la version de Yarn installée sur votre système, exécutez :

```bash
yarn -v
```

## Comment mettre à jour Node Package Manager

Mettez à jour vers la dernière version de NPM en exécutant :

```bash
npm install npm@latest -g
```

## Comment mettre à jour NodeJS

Supposons que vous souhaitiez mettre à jour votre installation de Node.js. Dans ce cas, vous avez deux options :

### Option 1 : Mettre à jour via le site NodeJS

Une façon de mettre à jour votre installation NodeJS est de télécharger et installer manuellement la dernière version depuis le [site Node.js](https://nodejs.org/en/).

### Option 2 : Mettre à jour via un outil de gestion de version

Une autre façon de mettre à jour votre installation NodeJS est d'utiliser un [gestionnaire de version](https://nodejs.org/en/download/package-manager/) tel que [NVM](https://github.com/nvm-sh/nvm), [n](https://github.com/tj/n), ou [nvs](https://github.com/jasongin/nvs).

## Comment mettre à jour Yarn

Mettez à jour vers la dernière version de Yarn en exécutant :

```bash
yarn set version latest
```

Maintenant que nous avons NPM (ou Yarn) sur notre ordinateur, nous pouvons commencer à utiliser le gestionnaire installé pour trouver, installer, configurer et supprimer les paquets de notre projet.

Mais qu'est-ce qu'un paquet exactement ? Découvrons-le.

## Qu'est-ce qu'un paquet exactement ?

Un **paquet** est un [répertoire](https://www.codesweetly.com/git-basic-introduction/#h-working-directory) (ou projet) qui contient un fichier `package.json` utilisé pour enregistrer des informations à son sujet.

**Note :** Vous ne pouvez publier que des paquets (un projet décrit par un fichier `package.json`) sur le [registre NPM](https://docs.npmjs.com/cli/v6/using-npm/registry).

## Comment installer des paquets

Il existe deux façons d'installer un paquet : localement ou globalement.

### Installation locale de paquet

Un paquet installé localement est celui que vous pouvez utiliser uniquement dans le projet dans lequel vous l'avez installé.

Pour installer un paquet localement, procédez comme suit :

1. Accédez au [répertoire racine](https://www.codesweetly.com/web-tech-glossary/#h-root-directory) de votre projet depuis la ligne de commande.
2. Installez votre paquet en utilisant la commande d'installation NPM ou Yarn ci-dessous (selon le gestionnaire de paquets que vous avez choisi d'utiliser pour votre projet).

**Note :** Vous devez avoir Node et NPM installés sur votre système pour que les commandes d'installation NPM (et Yarn) ci-dessous fonctionnent. Vous pouvez obtenir les deux en installant la dernière version LTS ou la version actuelle depuis le site Node.js.

#### Commande d'installation NPM

```bash
npm install package-name --save
```

Notez que la commande `--save` ci-dessus indique à NPM d'enregistrer `package-name` dans le fichier `package.json` comme l'un des paquets dont le projet dépend.

Supposons que vous souhaitiez installer une version exacte d'un paquet. Dans ce cas, ajoutez un `@[version-number]` après le nom du paquet comme suit :

```bash
npm install package-name@4.14.1 --save
```

Alternativement, si le paquet que vous installez est à des fins de développement et de test, utilisez :

```bash
npm install package-name --save-dev
```

Les commandes ci-dessus amèneront NPM à télécharger trois éléments dans le répertoire racine de votre projet : un dossier `node_modules`, un fichier `package.json` et un fichier `package-lock.json`. Nous discuterons de ces éléments plus en détail plus tard dans cet article.

#### Commande d'installation Yarn

```bash
yarn add package-name
```

Supposons que vous souhaitiez installer une version exacte d'un paquet. Dans ce cas, ajoutez un `@[version-number]` après le nom du paquet comme suit :

```bash
yarn add package-name@4.14.1
```

Alternativement, si le paquet que vous installez est à des fins de développement et de test, utilisez :

```bash
yarn add package-name --dev
```

Les commandes ci-dessus amèneront Yarn à télécharger trois éléments dans le répertoire racine de votre projet : un dossier `node_modules`, un fichier `package.json` et un fichier `yarn.lock`. Nous discuterons de ces éléments plus en détail plus tard dans cet article.

Maintenant que nous savons comment installer un paquet localement, nous pouvons discuter de l'installation globale de paquets.

### Installation globale de paquet

Un paquet installé globalement est un paquet que vous pouvez utiliser n'importe où sur votre système.

Pour installer un paquet globalement, exécutez le code ci-dessous sur votre terminal :

```bash
npm install package-name -g
```

Alternativement, vous pouvez utiliser Yarn comme suit :

```bash
yarn global add package-name
```

Notez que vous pouvez exécuter les commandes ci-dessus depuis n'importe quel emplacement sur votre système.

### Installation locale vs. globale de paquet

Généralement, il est préférable d'installer un paquet localement. Voici quelques-unes des différences entre une installation locale et globale.

#### Différence 1 : Emplacement de l'installation

Un paquet installé localement est installé dans le répertoire où vous avez exécuté la commande `npm install package-name` (ou `yarn add package-name`).

Plus précisément, vous trouverez les paquets installés localement d'un projet dans son répertoire `node_module`.

En revanche, un paquet installé globalement est installé à un seul endroit sur votre système. L'emplacement exact dépend de la configuration de votre système.

#### Différence 2 : Versions de paquet

Supposons que vous avez installé votre paquet localement. Alors, vous pouvez utiliser différentes versions du même paquet pour le développement de plusieurs applications.

Cependant, vous êtes obligé d'utiliser la même version de paquet pour toutes vos applications lorsque vous installez globalement.

#### Différence 3 : Mises à jour

Une installation locale vous permet de choisir les paquets du projet que vous souhaitez mettre à jour vers la dernière version. Cela facilite la gestion des mises à jour qui rompent la compatibilité avec d'autres paquets.

Cependant, la mise à jour d'un paquet installé globalement met à jour le paquet pour tous les projets – ce qui peut causer des cauchemars de maintenance si la mise à jour rompt la compatibilité avec d'autres paquets.

#### Différence 4 : Recommandation d'utilisation

L'installation globale est idéale pour les paquets que vous prévoyez d'utiliser uniquement sur votre ligne de commande – surtout lorsqu'ils fournissent des commandes exécutables réutilisables entre les projets.

Cependant, l'installation locale est idéale pour les paquets que vous prévoyez d'utiliser dans votre programme – via l'instruction `import` ou la fonction `require()`.

#### Différence 5 : Exemples

[NPM](https://www.npmjs.com/), [React Native CLI](https://reactnative.dev/docs/environment-setup), [Gatsby CLI](https://www.gatsbyjs.com/docs/reference/gatsby-cli/), [Grunt CLI](https://gruntjs.com/getting-started), et [Vue CLI](https://cli.vuejs.org/) sont des exemples bien connus de paquets globaux.

Des exemples courants de paquets locaux sont [Webpack](https://webpack.js.org/), [Lodash](https://lodash.com/), [Jest](https://jestjs.io/), et [MomentJS](https://momentjs.com/).

**Note :**

* Vous pouvez [effectuer une installation locale et globale](https://nodejs.org/en/blog/npm/npm-1-0-global-vs-local-installation/#when-you-can-t-choose) des paquets que vous prévoyez d'utiliser à la fois sur la ligne de commande et dans votre projet. Des exemples typiques de tels paquets sont [ExpressJS](https://expressjs.com/) et [CoffeeScript](https://coffeescript.org/).
* Votre gestionnaire de paquets n'exécute pas un paquet installé. NPM (et Yarn) installent uniquement les paquets dans le répertoire `node_modules`. Et si vous aviez spécifié la commande `--save`, votre gestionnaire ajouterait des détails sur le paquet au fichier `package.json`.
* Pour exécuter (lancer) un paquet [exécutable](https://helpdeskgeek.com/how-to/what-is-an-executable-file-how-to-create-one/), vous devez le faire explicitement vous-même. Nous discuterons de la manière de procéder dans une section ultérieure de cet article.

Mais qu'est-ce que le dossier `node_modules`, le fichier `package.json`, le fichier `package-lock.json` et le fichier `yarn.lock` ? Découvrons-le.

## Qu'est-ce qu'un dossier `node_modules` ?

Le répertoire **node_modules** est le dossier où NPM place tous les paquets qu'il télécharge localement pour votre projet.

## Qu'est-ce qu'un fichier `package.json` ?

Un fichier **package.json** est un document JSON que les gestionnaires de paquets – comme NPM et Yarn – utilisent pour stocker des informations sur un projet spécifique.

En d'autres termes, un fichier `package.json` est un fichier de métadonnées de projet.

### Avantages d'un fichier `package.json`

Un fichier `package.json` :

* permet de publier votre projet sur le registre NPM
* facilite la gestion et l'installation de votre paquet par d'autres
* aide NPM à gérer facilement les dépendances d'un [module](https://www.codesweetly.com/javascript-modules-tutorial/)
* rend votre paquet reproductible et partageable avec d'autres développeurs

### Comment créer un fichier `package.json`

Accédez au répertoire racine de votre projet et initialisez la création d'un fichier `package.json` en exécutant :

```bash
npm init
```

Ou, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn init
```

Une fois que vous avez exécuté la commande d'initialisation ci-dessus, votre gestionnaire de paquets vous guidera à travers la création du fichier `package.json` en posant quelques questions sur votre projet.

Si vous souhaitez ignorer le questionnaire, vous pouvez créer un fichier `package.json` par défaut. Voyons comment.

### Comment créer un fichier `package.json` par défaut

Supposons que vous préférez ignorer le questionnaire invité par la commande `npm init` (ou `yarn init`). Dans ce cas, accédez au [répertoire racine](https://www.codesweetly.com/web-tech-glossary/#h-root-directory) de votre projet et exécutez :

```bash
npm init -y
```

Ou, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn init -y
```

La commande ci-dessus utilisera [des valeurs par défaut extraites du répertoire actuel](https://docs.npmjs.com/creating-a-package-json-file#default-values-extracted-from-the-current-directory) pour créer le fichier `package.json` de votre projet.

**Note :** Le drapeau `-y` est un raccourci pour `--yes`.

Une fois que votre gestionnaire de paquets a terminé son processus d'initialisation, le fichier `package.json` de votre projet contiendra un objet avec un ensemble de propriétés.

**Voici un exemple :**

```json
{
  "name": "codesweetly-project",
  "version": "1.0.0",
  "main": "index.js"
}
```

Vous pouvez voir que le fichier `package.json` ci-dessus contient les champs `name`, `version` et `main`. Apprenons-en plus sur ces propriétés ci-dessous.

### Les champs du `package.json`

Les propriétés du `package.json` rendent votre projet utilisable par les gestionnaires de paquets et les utilisateurs finaux.

Supposons que vous souhaitiez publier votre paquet sur le registre NPM. Dans ce cas, votre fichier `package.json` doit avoir les champs `"name"` et `"version"`.

Cependant, si vous ne prévoyez pas de publier votre paquet, dans ce cas, tous les champs – y compris les propriétés `"name"` et `"version"` – sont facultatifs.

Apprenons-en plus sur les champs couramment utilisés dans un fichier `package.json`.

#### name

Le champ `"name"` est une propriété utilisée pour enregistrer le nom d'un projet.

La valeur de la propriété `"name"` doit être :

* un seul mot
* en lettres minuscules
* et inférieure ou égale à 214 caractères

Notez que vous pouvez joindre des mots ensemble avec des traits d'union et des underscores.

**Voici un exemple :**

```json
{
  "name": "code_sweetly-project"
}
```

#### version

Le champ `"version"` indique le numéro de version actuel d'un projet.

La propriété `"version"` doit être sous la forme d'un format `major.minor.patch`. Elle doit également suivre les [directives de version sémantique](https://docs.npmjs.com/about-semantic-versioning).

**Voici un exemple :**

```json
{
  "version": "1.0.0"
}
```

#### description

Le champ `"description"` est une propriété contenant une brève description du but d'un projet.

NPM recommande d'avoir une propriété `"description"` pour faciliter la recherche de votre paquet sur le site NPM.

Votre description sera l'une des choses affichées lorsque les gens exécuteront la commande `npm search`.

**Voici un exemple :**

```json
{
  "description": "Une brève description de ce paquet (projet)"
}
```

#### main

Le champ `"main"` indique le [point d'entrée](https://www.codesweetly.com/web-tech-glossary/#entry-point) d'un projet.

En d'autres termes, lorsque quelqu'un exécute la fonction `require()`, Node résoudra l'invocation à `require(<package.json:main>)`.

**Voici un exemple :**

```json
{
  "main": "./src/index.js"
}
```

#### private

Le champ `"private"` permet aux gestionnaires de paquets de savoir s'ils doivent publier votre projet sur le registre NPM.

**Voici un exemple :**

```json
{
  "private": true
}
```

Si vous définissez la propriété `"private"` de votre package.json sur `true`, les gestionnaires de paquets ne publieront pas votre projet.

Par conséquent, définir la propriété est un excellent moyen d'éviter la publication accidentelle de votre paquet.

#### scripts

Le champ `"scripts"` définit les commandes de script que vous souhaitez exécuter à divers moments du cycle de vie de votre projet.

**Voici un exemple :**

```json
{
  "scripts": {
    "test": "jest",
    "dev": "webpack --mode development",
    "build": "webpack --mode production",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build" 
  }
}
```

Le champ `"scripts"` ci-dessus contient cinq propriétés dont les valeurs sont les commandes que nous voulons que notre gestionnaire de paquets exécute chaque fois que nous invoquons la clé de la propriété.

Ainsi, par exemple, l'exécution de `npm run dev` exécutera la commande `"webpack --mode development"`.

#### keywords

Le champ `"keywords"` spécifie un tableau de mots-clés qui peuvent aider les gens à découvrir votre paquet.

**Voici un exemple :**

```json
{
  "keywords": [
    "drag",
    "drop",
    "drag and drop",
    "dragndrop",
    "draggable" 
  ]
}
```

La propriété `"keywords"` fait partie des informations affichées lorsque les gens exécutent la commande `npm search`.

#### author

Le champ `"author"` répertorie les détails de l'auteur d'un projet.

**Voici un exemple :**

```json
{
  "author": "Oluwatobi Sofela <oluwatobiss@codesweetly.com> (https://www.codesweetly.com)"
}
```

Vous pouvez également écrire l'extrait ci-dessus comme suit :

```json
{
  "author": {
    "name": "Oluwatobi Sofela",
    "email": "oluwatobiss@codesweetly.com",
    "url": "https://www.codesweetly.com"
  }
}
```

Notez que les propriétés `"email"` et `"url"` sont facultatives.

#### dependencies

Le champ `"dependencies"` répertorie tous les paquets dont un projet dépend en production.

**Voici un exemple :**

```json
{
  "dependencies": {
    "first-package": "^1.0.4",
    "second-package": "~2.1.3"
  }
}
```

Ainsi, chaque fois qu'un utilisateur installe votre projet depuis le registre NPM, la propriété des dépendances garantit que les gestionnaires de paquets peuvent automatiquement trouver et installer les paquets répertoriés.

Notez que vous pouvez ajouter un paquet au champ `"dependencies"` de l'une des manières suivantes :

* Ajoutez manuellement le nom et la [version sémantique](https://docs.npmjs.com/about-semantic-versioning) de chaque paquet dont votre projet dépend en production.
* Exécutez la commande `npm install package-name --save-prod` sur votre terminal. Ou `yarn add package-name` si Yarn est votre gestionnaire de paquets.

#### devDependencies

Le champ `"devDependencies"` répertorie tous les paquets dont un projet n'a pas besoin en production – mais nécessite pour ses besoins de développement et de test locaux.

**Voici un exemple :**

```json
{
  "devDependencies": {
    "first-dev-package": "^5.8.1",
    "second-dev-package": "3.2.2.0.0"
  }
}
```

Notez que les paquets répertoriés dans le champ `"devDependencies"` seront disponibles dans l'environnement de développement du projet mais pas sur son serveur de production.

Supposons qu'un utilisateur installe le projet via la commande `npm install` (ou `yarn add`). Dans ce cas, le gestionnaire de paquets trouvera et téléchargera toutes les `devDependencies` répertoriées dans le répertoire `node_modules` du projet.

Gardez à l'esprit que vous pouvez ajouter un paquet au champ `"devDependencies"` de l'une des manières suivantes :

* Ajoutez manuellement le nom et la version sémantique de chaque paquet dont votre projet dépend pour ses besoins de développement et de test.
* Exécutez la commande `npm install package-name --save-dev` sur votre terminal. Ou `yarn add package-name --dev` si Yarn est votre gestionnaire de paquets.

#### homepage

Le champ `"homepage"` spécifie l'URL de la page d'accueil de votre projet.

**Voici un exemple :**

```json
{
  "homepage": "https://codesweetly.com/package-json-file-explained"
}
```

Maintenant que nous savons ce qu'est un fichier `package.json`, nous pouvons discuter du `package-lock.json`.

## Qu'est-ce qu'un fichier `package-lock.json` ?

Le fichier **package-lock.json** est un [document](https://www.codesweetly.com/document-vs-data-vs-code/#h-what-is-a-document) que NPM utilise pour enregistrer la version exacte de tous les paquets que vous avez installés localement dans le répertoire `node_modules` de votre projet.

Un fichier `package-lock.json` rend une application 100 % reproductible de la manière exacte dont vous l'avez publiée sur le registre NPM.

Ainsi, supposons qu'un utilisateur clone votre application et exécute la commande `npm install`. Dans ce cas, `package-lock.json` garantit que l'utilisateur télécharge la version exacte des paquets que vous avez utilisés pour développer l'application.

Par exemple, disons qu'un utilisateur a cloné votre application ne contenant _aucun_ fichier `package-lock.json`, et qu'une dépendance utilisée dans l'application a une version plus récente.

Supposons que le numéro de version de la dépendance dans le fichier `package.json` contient un signe circonflexe (par exemple, `^2.6.2`). Dans ce cas, NPM installera la dernière version mineure de la dépendance – ce qui pourrait amener l'application à produire des résultats erronés.

Cependant, supposons que l'utilisateur a cloné votre application contenant un fichier `package-lock.json`. Dans ce cas, NPM installera la version exacte de la dépendance telle qu'enregistrée dans le fichier `package-lock.json` – indépendamment du fait qu'une version plus récente existe.

Par conséquent, les utilisateurs obtiendront toujours votre application de la manière précise dont vous l'avez publiée sur le registre NPM.

En d'autres termes, NPM utilise le fichier `package-lock.json` pour verrouiller les dépendances de votre paquet aux numéros de version spécifiques que vous avez utilisés pour le développement du projet.

**Note :** NPM mettra à jour les paquets enregistrés dans le fichier `package-lock.json` chaque fois que vous exécuterez la commande `npm update`.

## Qu'est-ce qu'un fichier `yarn.lock` ?

Le fichier `yarn.lock` est un document que Yarn utilise pour enregistrer la version exacte de tous les paquets que vous avez installés localement dans le répertoire `node_modules` de votre projet.

Le fichier `yarn.lock` est comparable au fichier de verrouillage [package-lock.json](#heading-quest-ce-quun-fichier-package-lockjson) de NPM.

Nous avons mentionné précédemment que votre gestionnaire de paquets n'exécute pas un paquet installé – vous devez le faire explicitement vous-même. Discutons de la manière de procéder.

## Comment exécuter un paquet exécutable

Il existe plusieurs façons d'exécuter un paquet exécutable. Voici les techniques standard.

### Localiser et exécuter manuellement le paquet

Une façon d'exécuter un paquet exécutable est de taper son chemin local sur votre ligne de commande comme suit :

```bash
./node_modules/.bin/package-name
```

### Ajouter le paquet au champ `scripts` du package.json

Une autre façon d'exécuter un paquet est de l'ajouter d'abord au champ `"scripts"` du fichier package.json de votre projet comme ceci :

```json
{
  "name": "your_package",
  "version": "1.0.0",
  "scripts": {
    "desired-name": "name-of-package-to-execute"
  }
}
```

Ensuite, vous pouvez exécuter le paquet comme suit :

```bash
npm run desired-name
```

Notez que la commande ci-dessus est un raccourci pour `npm run-script desired-name`.

Alternativement, vous pouvez exécuter le paquet avec Yarn comme suit :

```bash
yarn run desired-name
```

**Voici un exemple :**

```json
{
  "name": "codesweetly-app",
  "version": "1.0.0",
  "scripts": {
    "build": "webpack",
  }
}
```

L'extrait ci-dessus a ajouté [webpack](https://www.codesweetly.com/javascript-module-bundler/) au champ `"scripts"` de votre `package.json`. Nous pouvons donc maintenant exécuter `webpack` sur la ligne de commande comme ceci :

```bash
npm run build
```

Ou, si votre gestionnaire de paquets est Yarn, vous pouvez exécuter webpack comme ceci :

```bash
yarn run build
```

### Utiliser NPX

Une façon plus rapide d'exécuter un paquet exécutable est d'utiliser NPX comme suit :

```bash
npx package-name
```

Avec NPX, vous n'avez plus besoin d'ajouter votre paquet au champ `"scripts"` du fichier `package.json` de votre projet.

NPX (Node Package Execute) est un [exécuteur de paquets Node](https://nodejs.dev/learn/the-npx-nodejs-package-runner) qui trouve et exécute automatiquement un paquet spécifié.

**Voici un exemple :**

```bash
npx webpack
```

La commande ci-dessus trouvera et exécutera automatiquement [webpack](https://www.codesweetly.com/javascript-module-bundler/). Nous n'avons donc pas besoin d'ajouter la propriété `"build": "webpack"` au champ `"scripts"` de notre fichier `package.json`.

**Note :** NPX est automatiquement installé lorsque vous installez Node 8.2/NPM 5.2.0 ou une version ultérieure.

Vous pouvez également exécuter du code en utilisant votre version préférée de Node.js. Découvrons comment.

## Comment exécuter du code en utilisant votre version préférée de Node.js

Vous pouvez utiliser le caractère `@` et le [paquet node npm](https://www.npmjs.com/package/node) pour spécifier la version de Node.js que vous souhaitez utiliser pour exécuter votre code.

**Voici un exemple :**

```bash
npx node@7 index.js
```

L'extrait ci-dessus indique à NPX d'exécuter `index.js` avec la dernière version de Node à partir de la version majeure 7.

L'utilisation de la commande `node@` est un moyen utile d'éviter d'utiliser des outils de gestion de version Node.js comme [nvm](https://github.com/nvm-sh/nvm) pour basculer entre les versions de Node.

Supposons que vous souhaitiez confirmer la version de Node que NPX utilisera pour exécuter votre code. Dans ce cas, exécutez :

```bash
npx node@7 -v
```

L'extrait ci-dessus affichera la dernière version de Node à partir de la version majeure 7 que NPX utilisera pour exécuter votre code – par exemple, `v7.10.1`.

## Comment vérifier les paquets locaux obsolètes

Pour déterminer si l'un des paquets de votre projet est obsolète, exécutez :

```bash
npm outdated
```

Si la commande ne produit aucune sortie, cela signifie que tous les paquets de votre projet sont à jour.

Sinon, consultez cet [article npm-outdated](https://docs.npmjs.com/cli/v6/commands/npm-outdated) pour une explication détaillée de la sortie de la commande.

Alternativement, vous pouvez utiliser Yarn comme suit :

```bash
yarn outdated
```

**Note :** Pour vérifier l'état obsolète d'un paquet spécifique, ajoutez le nom du paquet après le mot-clé `outdated` – par exemple, `npm outdated lodash`.

## Comment vérifier les paquets globaux obsolètes

Pour confirmer quel paquet global est obsolète, exécutez :

```bash
npm outdated -g --depth=0
```

## Comment vérifier les paquets installés localement

Voici trois façons de vérifier les paquets installés localement :

### Paquets installés localement et leurs dépendances

```bash
npm list
```

Ou utilisez Yarn comme suit :

```bash
yarn list
```

### Paquets installés localement – sans leurs dépendances

```bash
npm list --depth=0
```

Ou,

```bash
yarn list --depth=0
```

### Vérifier si un paquet spécifique a été installé localement

```bash
npm list package-name
```

## Comment vérifier les paquets installés globalement

Voici trois façons de vérifier les paquets installés globalement :

### Paquets installés globalement et leurs dépendances

```bash
npm list -g
```

Ou utilisez Yarn comme suit :

```bash
yarn list -g
```

### Paquets installés globalement – sans leurs dépendances

```bash
npm list -g --depth=0
```

Ou,

```bash
yarn list -g --depth=0
```

### Vérifier si un paquet spécifique a été installé globalement

```bash
npm list -g package-name
```

## Comment mettre à jour les paquets

Voici comment mettre à jour les paquets avec NPM et Yarn :

### Comment mettre à jour un paquet spécifique vers sa dernière version

```bash
npm update package-name
```

Ou, pour les projets gérés avec Yarn, exécutez :

```bash
yarn upgrade package-name
```

### Comment mettre à jour tous les paquets installés localement d'un projet

```bash
npm update
```

Ou,

```bash
yarn upgrade
```

### Comment mettre à jour un paquet global spécifique

Vous pouvez mettre à jour un paquet installé globalement comme ceci :

```bash
npm update package-name -g
```

### Comment mettre à jour tous les paquets installés globalement sur votre système

```bash
npm update -g
```

## Comment désinstaller les paquets

Voici comment désinstaller les paquets avec NPM et Yarn :

### Comment désinstaller un paquet d'un projet spécifique

Tout d'abord, accédez au [répertoire racine](https://www.codesweetly.com/web-tech-glossary/#h-root-directory) du projet depuis la ligne de commande et exécutez :

```bash
npm uninstall package-name
```

**Note :**

* Ajoutez le drapeau `-S` (ou `--save`) pour supprimer les références au paquet dans le champ `dependencies` du fichier `package.json` du projet.
* Ajoutez le drapeau `-D` (ou `--save-dev`) pour supprimer les références au paquet dans le champ `devDependencies` du fichier `package.json` du projet.

Pour les projets gérés avec Yarn, exécutez :

```bash
yarn remove package-name
```

**Note :** La commande `yarn remove` mettra automatiquement à jour les fichiers `package.json` et `yarn.lock` du projet.

### Comment désinstaller un paquet global

```bash
npm uninstall package-name -g
```

Notez qu'il est préférable de ne pas supprimer manuellement les paquets du dossier `node_modules`, car une telle action peut affecter d'autres _modules_ qui en dépendent.

Mais qu'est-ce qu'un module dans NodeJS ? Découvrons-le ci-dessous.

## Qu'est-ce qu'un module dans NodeJS ?

Un **module** dans NodeJS est tout fichier dans le dossier `node_modules` que l'ordinateur peut charger via la fonction `require()` de Node.

**Voici un exemple :**

```js
const myModule = require("./codesweetly.js");
```

Supposons que l'ordinateur a réussi à utiliser la fonction `require()` pour charger le fichier `codesweetly.js`. Dans ce cas, cela signifie que `codesweetly.js` est un module – assigné à la variable `myModule`.

Gardez à l'esprit qu'un module peut également être un paquet – mais pas toujours.

Un module n'est _pas_ un paquet s'il n'a _pas_ de fichier `package.json` utilisé pour enregistrer des informations à son sujet.

De plus, notez que pour qu'un module soit chargeable par la fonction `require()`, le module doit être l'un des éléments suivants :

* Un paquet – dont le fichier `package.json` contient un champ `"main"`.
* Un fichier JavaScript.

## Comment publier votre projet sur le registre NPM

NPM est un registre gratuit pour les [auteurs de paquets publics](https://www.npmjs.com/products).

Ainsi, vous pouvez l'utiliser pour publier n'importe quel projet (dossier) de votre ordinateur qui contient un fichier `package.json`.

Voici les étapes nécessaires pour partager votre paquet avec le monde.

### Étape 1 : Connectez-vous ou inscrivez-vous

Rendez-vous sur le [site NPM](https://www.npmjs.com/) et connectez-vous (ou inscrivez-vous si vous n'avez pas encore de compte).

**Note :** assurez-vous de vérifier votre email après avoir créé un nouveau compte. Sinon, vous obtiendrez une erreur `403 Forbidden` lors de la publication de votre paquet.

### Étape 2 : Connectez-vous

Connectez-vous à votre compte NPM depuis la ligne de commande comme suit :

```bash
npm login
```

**Note :** Vous pouvez utiliser la commande `npm whoami` pour vérifier si vous êtes actuellement connecté.

### Étape 3 : Publiez votre paquet !

Accédez au répertoire racine de votre projet et publiez-le comme suit :

```bash
npm publish
```

Assurez-vous que le nom de votre paquet n'existe pas actuellement sur NPM. Sinon, vous obtiendrez une erreur lors de la publication.

Vous pouvez utiliser la commande `npm search` (ou la barre de recherche du [site NPM](https://www.npmjs.com/)) pour rechercher si le nom que vous souhaitez utiliser existe déjà sur NPM.

Supposons que tous les noms appropriés pour votre paquet sont déjà pris. Dans ce cas, NPM vous permet de publier votre projet en tant que portée.

En d'autres termes, vous pouvez publier votre paquet en tant que sous-section de votre nom d'utilisateur. Voyons comment ci-dessous.

### Comment publier votre paquet en tant que portée de votre nom d'utilisateur

Ouvrez votre fichier `package.json` et faites précéder le nom de votre paquet par votre nom d'utilisateur.

**Voici un exemple :**

```json
{
  "name": "@username/package-name",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT"
}
```

Le paramètre par défaut de NPM suppose qu'un paquet avec un nom de portée est un projet privé. Vous obtiendrez donc une erreur si vous utilisez la commande `npm publish` pour partager un paquet avec un nom de portée.

Par conséquent, pour publier votre paquet en tant que portée de votre nom d'utilisateur, ajoutez le drapeau `--access=public` à la commande `npm publish` :

```bash
npm publish --access=public
```

**Note :** Vous pouvez rendre votre projet un paquet de portée pendant le processus d'initialisation en utilisant la commande `npm init --scope=username` au lieu de `npm init`.

## Aperçu

Cet article a discuté de ce qu'est un gestionnaire de paquets. Nous avons également examiné le fonctionnement de deux gestionnaires de paquets populaires (NPM et Yarn).

Merci d'avoir lu !

### **Et voici une ressource utile sur ReactJS :**

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✔
* Il contient des extraits de code en direct ✔
* Il contient des projets évolutifs ✔
* Il contient de nombreux exemples faciles à comprendre ✔

Le livre [React Explained Clearly](https://amzn.to/30iVPIG) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![React Explained Clearly Book Now Available at Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://amzn.to/30iVPIG)