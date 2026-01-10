---
title: Comment configurer Jest & Enzyme comme un pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T18:00:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-jest-enzyme-like-a-boss-8455a2bc6d56
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tozYeK-3Cjp7xjBAJE0FeQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: Comment configurer Jest & Enzyme comme un pro
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@quinoal?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Quino
  Al / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  When I started out...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-249.png)
_Photo par [Unsplash](https://unsplash.com/@quinoal?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Quino Al</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Lorsque j'ai commencé à écrire des tests pour mon application React, il m'a fallu plusieurs essais avant de comprendre comment configurer mon environnement de test en utilisant `Jest` et `Enzyme`. Ce tutoriel suppose que vous avez déjà une application React configurée avec `webpack` et `babel`. Nous continuerons à partir de là.

Ceci fait partie d'une série d'articles que j'ai écrits. Je parle de la manière de configurer une application React pour la production de la bonne manière et de la manière facile.

* **Partie 1** [Comment combiner Webpack 4 et Babel 7 pour créer une fantastique application React](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff) (Parle de la configuration de webpack avec babel, ainsi que de la prise en charge de .scss)
* **Partie 2** [Ces outils vous aideront à écrire du code propre](https://medium.freecodecamp.org/these-tools-will-help-you-write-clean-code-da4b5401f68e) (Parle de l'automatisation de votre code, afin que tout le code que vous écrivez soit du bon code)
* Ceci est la **Partie 3** dans laquelle je vais parler de la configuration de Jest avec Enzyme.

Avant de commencer, si à un moment donné vous vous sentez bloqué, n'hésitez pas à consulter le [**dépôt de code**](https://github.com/adeelibr/react-starter-kit). Les PR sont les bienvenus si vous pensez que les choses peuvent être améliorées.

### Prérequis

Vous devez avoir Node installé afin d'utiliser npm (node package manager).

D'abord, créez un dossier appelé `app`, puis ouvrez votre terminal et allez dans ce dossier `app` et tapez :

```
npm init -y
```

Cela créera un fichier `package.json` pour vous. Dans votre fichier `package.json`, ajoutez ce qui suit :

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "Un modèle de base pour React",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage --colors",
  },
  "devDependencies": {
    "@babel/core": "^7.0.0",
    "@babel/polyfill": "^7.0.0-beta.51",
    "@babel/preset-env": "^7.0.0-beta.51",
    "@babel/preset-react": "^7.0.0-beta.51",
    "babel-core": "^7.0.0-bridge.0",
    "babel-jest": "^23.4.2",
    "enzyme": "^3.3.0",
    "enzyme-adapter-react-16": "^1.1.1",
    "jest": "^23.4.2"
  }
}
```

Ensuite, créez un dossier appelé `src` dans votre dossier `app`. Le dossier `src/app/` est l'endroit où tout votre code React ainsi que ses tests résideront. Mais avant cela, comprenons pourquoi nous avons fait ce que nous avons fait dans notre fichier `package.json`.

Je parlerai des `scripts` dans un instant (promis). Mais avant cela, apprenons pourquoi nous avons besoin des dépendances suivantes. Je veux que vous sachiez ce qui va dans votre `package.json`. Alors commençons.

`@babel/core` Puisque généralement nous utilisons webpack pour compiler notre code React. Babel est une dépendance majeure qui aide à dire à webpack comment compiler le code. Ceci est également une dépendance pair pour utiliser Jest.

`@babel/polyfill` Jest nécessite une chose appelée `regenerator-runtime`, @babel/polyfill est livré avec cela et quelques autres fonctionnalités sympas.

`@babel/preset-env` et `@babel/preset-react` sont pour les fonctionnalités comme ES6 et React, donc lors de l'écriture de tests unitaires, `Jest` connaît la syntaxe **ES6** et **JSX**.

`babel-core` Ceci est principalement une dépendance pour `Jest`, car nous avons besoin de `babel-core` pour que Jest fonctionne.

`babel-jest` aidera Babel à comprendre le code que nous écrivons dans `Jest`.

`enzyme` Ceci est une bibliothèque d'assertion qui facilite l'assertion, la manipulation et la traversée de la sortie de vos composants React.

`enzyme-adapter-react-16` Un adaptateur/middleware pour aider Jest à se connecter avec `enzyme`.

`jest` Jest est la bibliothèque de test sur laquelle nous exécuterons nos tests.

Vous pouvez consulter un exemple très simple et minimaliste par les gens sympas de **jest**. Il utilise babel pour exécuter un test simple [**ici**](https://github.com/facebook/jest/tree/master/examples/babel-7).

De plus, si vous souhaitez [configurer webpack pour React](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff), voici un guide détaillé sur la manière dont je l'ai fait. Ou vous pouvez simplement parcourir l'ensemble du code source qui utilise la structure de base minimale de ce dont vous aurez besoin lors de la configuration de votre application React avec jest/enzyme ([**kit de démarrage ici**](https://github.com/adeelibr/react-starter-kit)).

Ensuite, créons un fichier appelé `jest.config.js` dans notre dossier principal `app` et ajoutons le code suivant. Je parlerai de ce que cela fait dans un instant.

```javascript
// Pour une explication détaillée concernant chaque propriété de configuration, visitez :
// https://jestjs.io/docs/en/configuration.html

module.exports = {
  // Efface automatiquement les appels et instances de mock entre chaque test
  clearMocks: true,

  // Un tableau de motifs globaux indiquant un ensemble de fichiers pour lesquels les informations de couverture doivent être collectées
  collectCoverageFrom: ['src/**/*.{js,jsx,mjs}'],

  // Le répertoire où Jest doit sortir ses fichiers de couverture
  coverageDirectory: 'coverage',

  // Un tableau d'extensions de fichiers que vos modules utilisent
  moduleFileExtensions: ['js', 'json', 'jsx'],

  // Les chemins vers les modules qui exécutent du code pour configurer ou préparer l'environnement de test avant chaque test
  setupFiles: ['<rootDir>/enzyme.config.js'],

  // L'environnement de test qui sera utilisé pour les tests
  testEnvironment: 'jsdom',

  // Les motifs globaux que Jest utilise pour détecter les fichiers de test
  testMatch: ['**/__tests__/**/*.js?(x)', '**/?(*.)+(spec|test).js?(x)'],

  // Un tableau de chaînes de motifs regexp qui sont comparées à tous les chemins de test, les tests correspondants sont ignorés
  testPathIgnorePatterns: ['\\\\node_modules\\\\'],

  // Cette option définit l'URL pour l'environnement jsdom. Elle est reflétée dans les propriétés telles que location.href
  testURL: 'http://localhost',

  // Un tableau de chaînes de motifs regexp qui sont comparées à tous les chemins de fichiers sources, les fichiers correspondants ne seront pas transformés
  transformIgnorePatterns: ['<rootDir>/node_modules/'],
  
  // Indique si chaque test individuel doit être rapporté pendant l'exécution
  verbose: false,
};
```

Ensuite, créez un fichier appelé `enzyme.config.js` dans votre dossier principal `app` et ajoutez le code suivant.

```javascript
/** Utilisé dans jest.config.js */
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });
```

Parlons d'abord de `jest.config.js`

`clearMocks` effacera tous les mocks, afin que le mock dans le `n-ième` test ne mute pas ou n'affecte pas le test à la position `n+1`.

`collectCoverageFrom` indique à Jest de collecter la couverture de code de tous les fichiers .js dans le dossier `src/`. La couverture vous indique le pourcentage de code couvert par vos cas de test.

`coverageDirectory` indique à Jest que le répertoire de couverture doit être nommé `coverage` dans le dossier principal `app/`.

`moduleFileExtensions` prend un tableau d'extensions qui indique à Jest quels fichiers il peut tester. Nous lui disons de tester tous les fichiers .js|.jsx|.json.

`setupFiles` ceci est vraiment important, car il indique à Jest le chemin à partir duquel il peut obtenir les configurations pour enzyme (plus sur cela plus tard)

`testEnvironment` spécifie l'environnement sur lequel Jest exécutera ses tests, puisque nous testons une application web. J'ai défini l'environnement sur `jsdom`.

`testMatch` indique à Jest quels fichiers il testera. Je passe ici 2 configurations, l'une étant de tester tous les fichiers dans un dossier nommé `__tests__` ou de tester tous les fichiers qui se terminent par `spec.js|.jsx` ou `test.js|.jsx`.

`testPathIgnorePatterns` Je ne veux pas que Jest exécute des tests dans mon dossier `node_modules`. J'ai donc ignoré ces fichiers ici.

`testURL` Cette option définit l'URL pour l'environnement jsdom. Elle est reflétée dans les propriétés telles que location.href.

`transformIgnorePatterns` Un tableau de chaînes de motifs regexp qui sont comparées à tous les chemins de fichiers sources, les fichiers correspondants ne seront pas transformés. Ici, je ne lui donne qu'un seul motif pour `node_modules`.

`verbose` Si vrai, donne un journal très détaillé lorsque vous exécutez des tests. Je ne veux pas voir cela, et je veux me concentrer uniquement sur l'essentiel de mes tests. J'ai donc défini sa valeur sur `false`.

Parlons de `enzyme.config.js`

Je passe le chemin de `enzyme.config.js` dans mes `setupFiles` dans les configurations de Jest. Lorsque Jest accède à ce fichier, il prend les configurations d'enzyme. Cela signifie que tous les tests seront exécutés sur Jest. Mais les assertions et tout le reste seront effectués par enzyme.

Avec cela en place, nos configurations sont terminées. Parlons des scripts :

```
"scripts": {    
    "test": "jest",
    "test:watch": "jest --watch",    
    "test:coverage": "jest --coverage --colors",  
},
```

`npm run test` cela exécutera Jest et exécutera tous les tests.

`npm run test:watch` exécutera tous les tests et restera en mode surveillance, afin que lorsque nous apportons des modifications à nos cas de test, il exécutera à nouveau ces cas de test.

`npm run test:coverage` générera un rapport de couverture basé sur tous les tests qu'il exécute, et vous donnera un rapport de couverture détaillé dans le dossier `app/coverage`.

Avant d'exécuter un test, nous devons en créer un. Alors commençons. Dans votre dossier `app/src/`, créez un fichier appelé **WelcomeMessage.js**.

```
import React, { Fragment } from 'react';

const styles = {
  heading: {
    color: '#fff',
    textAlign: 'center',
    marginBottom: 15,
  },
  logo: {
    width: 250,
    heading: 250,
    objectFit: 'cover',
  },
};

const WelcomeMessage = ({ imgPath }) => {
  return (
    <Fragment>
      <h1 style={styles.heading}>
        Bienvenue
      </h1>
      <img src={imgPath} alt="logo de l'application" style={styles.logo} />
    </Fragment>
  );
};

export default WelcomeMessage;
```

Dans le même dossier, créez un fichier appelé [**WelcomeMessage.test.js**](https://gist.github.com/adeelibr/ac60da132758c7ebbcb30e28672975fe)

```
import React from 'react';
import { shallow } from enzyme;

// Composants
import WelcomeMessage from './WelcomeMessage';

function setup() {
  const props = {
    imgPath: 'some/image/path/to/a/mock/image',
  };
  const wrapper = shallow(<WelcomeMessage />);
  return { wrapper, props };
}

describe('Suite de tests WelcomeMessage', () => {
  it('Devrait avoir une image', () => {
    const { wrapper } = setup();
    expect(wrapper.find('img').exists()).toBe(true);
  });
});
```

Une chose à noter ici est que vous ne pourrez pas réellement exécuter le fichier `WelcomMessage.js` puisque vous n'avez pas configuré `webpack` avec `babel`. Si vous cherchez un moyen de le configurer, consultez mon tutoriel sur [Comment combiner Webpack 4 et Babel 7 pour créer une fantastique application React](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff). De plus, si vous voulez simplement le code source de ce tutoriel, voici le [**dépôt de code**](https://github.com/adeelibr/react-starter-kit). Il a déjà Jest et Enzyme configurés. N'hésitez pas à faire un fork et à commencer à jouer avec la base de code.

Revenons au code que nous venons d'écrire, dans votre terminal, tapez `npm run test`. Il exécutera un script et trouvera tous les fichiers qui se terminent par `*.test.js` et les exécutera. Après avoir exécuté, vous verrez un message comme celui-ci :

```
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

Je sais que ce n'est pas un test unitaire très pratique, mais je voulais que ce tutoriel se concentre uniquement sur la configuration de Jest et Enzyme.

Encore une fois, voici le code source de ce [**tutoriel**](https://github.com/adeelibr/react-starter-kit).