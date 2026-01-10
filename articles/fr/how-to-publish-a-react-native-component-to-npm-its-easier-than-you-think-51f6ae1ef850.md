---
title: Comment publier un composant React Native sur NPM — c'est plus facile que vous
  ne le pensez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-01T19:20:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-a-react-native-component-to-npm-its-easier-than-you-think-51f6ae1ef850
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-eB8L7-mDpQKLYPE
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: npm
  slug: npm
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Comment publier un composant React Native sur NPM — c'est plus facile que
  vous ne le pensez
seo_desc: 'By Colby Miller

  So you want to contribute to the open source community? That’s awesome! Helping
  to grow React Native’s fairly young ecosystem is great.

  When I decided to take on this task not long ago, I noticed there wasn’t much material
  around publ...'
---

Par Colby Miller

Vous souhaitez contribuer à la communauté open source ? C'est génial ! Aider à développer l'écosystème encore jeune de React Native est formidable.

Lorsque j'ai décidé de me lancer dans cette tâche il n'y a pas si longtemps, j'ai remarqué qu'il n'y avait pas beaucoup de documentation sur la publication de composants React Native sur NPM. J'espère donc que cet article aidera à simplifier le processus pour les autres.

> **Note :** Tout le code exemple ci-dessous provient de [react-native-progress-steps](https://www.npmjs.com/package/react-native-progress-steps), mon tout premier package NPM.

Avant de commencer, assurez-vous de vous inscrire pour un compte sur NPM. Vous pouvez le faire [ici](https://www.npmjs.com/signup).

### Installation initiale

Commençons par créer un dossier où notre composant React Native résidera.

```bash
mkdir <nom_du_dossier> && cd <nom_du_dossier>

# Par exemple
mkdir mon-composant && cd mon-composant
```

> **Note :** Pour garder cet article concis, je suppose que vous avez déjà Node et NPM installés sur votre ordinateur. Si ce n'est pas le cas, consultez cette [documentation](https://www.npmjs.com/get-npm) pour obtenir de l'aide.

Une fois dans le dossier, nous devons initialiser un nouveau package NPM en tapant `npm init`. Cela créera un fichier `package.json` qui contiendra des métadonnées importantes sur le composant React Native.

Une série de questions sera affichée, telles que le nom du package, la version, la description, les mots-clés, etc.

**Important :** Lorsque vous êtes invité à indiquer le _point d'entrée_, assurez-vous de saisir `index.js` et d'appuyer sur Entrée. Ce sera le fichier qui exporte votre composant principal.

```json
{
  "name": "react-native-progress-steps",
  "version": "1.0.0",
  "description": "Un composant React Native simple et entièrement personnalisable qui implémente une interface utilisateur de progression par étapes.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/colbymillerdev/react-native-progress-steps.git"
  },
  "keywords": [
    "react-native",
    "react-component",
    "react-native-component",
    "react",
    "react native",
    "mobile",
    "ios",
    "android",
    "ui",
    "stepper",
    "progress",
    "progress-steps"
  ],
  "author": "Colby Miller",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/colbymillerdev/react-native-progress-steps/issues"
  },
  "homepage": "https://github.com/colbymillerdev/react-native-progress-steps#readme"
}
```

### Structure du projet

L'étape suivante consiste à configurer une structure de dossiers pour votre composant React Native. Cela dépend vraiment de vous, mais je vais partager un exemple simple du mien ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQTDB-sc4d0Dt0o_oT9tEQ.png)

Vous remarquerez certains fichiers que nous n'avons pas encore créés. Nous allons les aborder sous peu.

Créons le fichier `index.js`. Ce sera le fichier le plus important pour exporter/importer correctement votre composant. Accédez au dossier racine du projet et tapez `touch index.js`.

Il existe plusieurs façons de procéder pour le contenu de ce fichier.

* Écrire directement la classe du composant dans le fichier `index.js` et l'exporter là.
* Créer un fichier JavaScript de composant séparé et l'exporter dans `index.js`.
* Enfin, créer plusieurs fichiers JavaScript de composants et de conteneurs et exporter tous ceux nécessaires dans le fichier `index.js`. C'est l'approche que j'ai suivie et qui peut être vue dans l'exemple ci-dessous.

```js
import ProgressSteps from './src/ProgressSteps/ProgressSteps';
import ProgressStep from './src/ProgressSteps/ProgressStep';

export { ProgressSteps, ProgressStep };
```

Peu importe l'approche choisie, ce qui est exporté dans ce fichier est ce que l'application consommatrice importera et rendra finalement. C'est la partie importante à retenir.

```js
import { ProgressSteps, ProgressStep } from 'react-native-progress-steps';
```

### Dépendances

Nous devons déterminer quelles dépendances doivent être installées pour que notre composant React Native fonctionne correctement.

Il existe trois types de dépendances différents :

* **peerDependencies** : Ces dépendances sont nécessaires pour que le composant fonctionne ; cependant, elles sont censées être déjà installées sur l'application. Un exemple de cela est `react-native` lui-même. Cependant, dans le cas de React Native, il n'est pas nécessaire d'ajouter `react-native` comme une dépendance peer.
* **dependencies** : Celles-ci sont également nécessaires pour que le composant fonctionne, mais vous ne pouvez pas supposer que l'application consommatrice les a installées. Certains exemples seraient `lodash` et `prop-types`.
* **devDependencies** : Celles-ci sont plus simples. Ce sont tous les packages nécessaires pour développer le composant React Native. Des exemples de ceux-ci seraient votre linter, votre framework de test et babel.

### Installation de la dépendance Babel

Notre prochaine étape consiste à connecter notre composant à Babel. Nous pouvons simplement le faire en installant la dépendance de développement suivante :

```js
npm install metro-react-native-babel-preset --save-dev
```

Après l'installation, nous devons créer un fichier `.babelrc` et y ajouter ce qui suit :

```json
{
  "presets": ["module:metro-react-native-babel-preset"]
}
```

### Création de .gitignore et .npmignore

L'une des dernières étapes consiste à créer les fichiers standard `.gitignore` et `.npmignore` comme bonne pratique. Cela évitera également tout problème lors de la publication sur NPM.

```
# Logs
*.log
npm-debug.log

# Données d'exécution
tmp
build
dist

# Répertoire des dépendances
node_modules
```

```
# Logs
*.log
npm-debug.log

# Répertoire des dépendances
node_modules

# Données d'exécution
tmp

# Exemples (si applicable à votre projet)
examples
```

### Test

Normalement, il est relativement simple de lier et d'installer notre package localement dans des applications, sans avoir à le publier sur NPM au préalable.

Cela se ferait en utilisant la commande `npm link` à l'intérieur du répertoire racine de notre package. Ensuite, naviguez vers une application et tapez `npm link <nom-du-package>` puis `npm install`.

Cependant, au moment de la rédaction de cet article, React Native et la commande `npm link` ne fonctionnent pas bien ensemble.

Il existe deux solutions que j'ai trouvées jusqu'à présent qui résolvent ce problème :

#### 1. Installation du package dans une application en utilisant un chemin local

Pour ce faire, naviguez vers une application et installez directement votre package là en utilisant son chemin de répertoire.

```bash
npm i <chemin_vers_le_projet>

# Par exemple
npm i ../mon-composant
```

Après avoir apporté des modifications à votre package, vous devrez revenir à l'application et réinstaller. Ce n'est pas une solution idéale, mais c'est une solution qui fonctionne.

#### 2. Création d'un dossier Examples et utilisation de npm pack

La commande `npm pack` est un excellent moyen de rapidement empaqueter votre composant React Native et de le préparer pour les tests. Elle crée un fichier `.tgz` qui peut ensuite être installé dans une application déjà existante.

Créons un dossier `/examples` à l'intérieur du répertoire racine de notre package NPM. Ce dossier sera essentiellement sa propre application React Native qui exécute et affiche vos exemples.

Cela peut être fait en créant un projet React Native en utilisant `react-native init examples`.

> **Note :** Cela nécessite d'avoir React Native déjà installé sur votre ordinateur. Vous pouvez suivre le guide Facebook [ici](https://facebook.github.io/react-native/docs/getting-started.html).

Après cela, exécutez la commande `npm pack` pour générer un fichier qui aura une convention de nommage similaire à `nom-du-package-0.0.0.tgz`.

Ensuite, allez dans le dossier `/examples` et installez votre composant en exécutant `npm i ../nom-du-package-0.0.0.tgz` ou `yarn add ../nom-du-package-0.0.0.tgz` dans le terminal. N'oubliez pas de remplacer `nom-du-package` et `0.0.0` respectivement.

Créez un ou plusieurs fichiers JavaScript qui afficheront votre composant. Pour cet exemple, nous appellerons ce fichier `ExampleOne.js`. Il est important de souligner que vous devriez importer le composant que vous venez d'installer en utilisant yarn ou npm dans ce fichier.

Une fois le fichier créé, ouvrez `App.js` et importez/exportez le fichier d'exemple. Ce qui est exporté dans ce fichier est ce qui sera affiché lors de l'exécution du projet sur un simulateur ou un appareil.

```js
import ExampleOne from './ExampleOne'

export default ExampleOne;
```

Enfin, nous pouvons exécuter l'application en utilisant `react-native run-ios` ou `react-native run-android`. Nous devrions maintenant pouvoir voir notre composant et le tester correctement.

Après avoir apporté des modifications au code de votre package NPM, n'oubliez pas d'exécuter la commande `npm pack`, puis allez dans le dossier `/examples` pour `npm install` ou `yarn add` le fichier `.tgz`.

> Un avantage intéressant de cette option est la possibilité pour d'autres utilisateurs d'exécuter vos exemples sur un simulateur ou un appareil. Cela leur permet d'essayer votre composant sans avoir à l'importer d'abord dans leur propre application. De plus, le fichier `.tgz` peut être facilement partagé entre collègues, amis, etc.

### Publication sur NPM

Enfin, nous sommes prêts à partager notre composant React Native avec la formidable communauté open source !

La publication est très rapide et facile. Connectez-vous simplement à votre compte NPM depuis le terminal en utilisant `npm login`, puis publiez en utilisant `npm publish`.

Une chose à retenir est que NPM nous oblige à incrémenter la version dans `package.json` à chaque fois avant la publication.

### Conclusion

Nous avons couvert énormément de matériel dans cet article. Si vous rencontrez des problèmes, n'hésitez pas à me poser une question dans les commentaires ci-dessous. Merci de m'avoir suivi, j'ai hâte de voir ce que vous allez construire !

_Les contributions, les pull requests et les recommandations sont toujours les bienvenues pour [react-native-progress-steps](https://www.npmjs.com/package/react-native-progress-steps). Essayez-le dans votre prochain projet et faites-moi savoir ce que vous en pensez !_