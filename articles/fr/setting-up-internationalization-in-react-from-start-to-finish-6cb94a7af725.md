---
title: Comment configurer l'internationalisation dans React de A à Z
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T07:46:06.000Z'
originalURL: https://freecodecamp.org/news/setting-up-internationalization-in-react-from-start-to-finish-6cb94a7af725
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6lJJiXiCnX2peIeLG3oIZg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer l'internationalisation dans React de A à Z
seo_desc: 'By Austin Tackaberry

  This post will use react-intl to help you go from create-react-app to setting up
  the framework to a completed, translated web app!

  I committed code as I wrote this post, so you will be able to look at my commit
  history to easily ...'
---

Par Austin Tackaberry

Cet article utilisera `react-intl` pour vous aider à passer de `create-react-app` à la configuration du framework jusqu'à une application web traduite et complète !

J'ai commis du code au fur et à mesure que j'écrivais cet article, vous pourrez donc consulter mon historique de commits pour voir facilement comment mon code a évolué de A à Z.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6lJJiXiCnX2peIeLG3oIZg.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/v6kii3H5CcU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Artem Bali</a> sur <a href="https://unsplash.com/search/photos/globe?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Qu'est-ce que l'internationalisation ?

Étant donné que vous avez décidé de cliquer sur le lien vers cet article, il est probable que vous ayez au moins une idée de ce qu'est l'internationalisation (i18n). Tiré directement du [site W3](https://www.w3.org/International/questions/qa-i18n) :

> « L'internationalisation est la conception et le développement d'un produit, d'une application ou d'un contenu de document qui **permet** une localisation facile pour les publics cibles qui varient en culture, région ou langue. »

En tant que développeur, vous souhaitez que votre contenu soit facilement lisible et utilisable par toutes sortes de personnes à travers le monde. Je pense que tout le monde est d'accord avec cela. Mais je sais ce que vous pensez :

« Développer une application web pour les personnes de ma propre culture/région/langue est déjà suffisamment difficile ! Je n'ai pas le temps ni l'énergie pour l'i18n ! »

Vous avez déjà le jargon, je vois. Espérons que cet article vous aidera à réaliser que la configuration de l'i18n pour votre projet n'est pas aussi difficile ou chronophage qu'il n'y paraît.

### Ce que react-intl fait et ne fait pas

Si vous êtes nouveau dans l'i18n, vous pourriez avoir quelques idées sur ce que vous pensez qu'une bibliothèque comme `react-intl` devrait et ne devrait pas être capable de faire.

**Il fait :**

* Vous aider à agréger tout votre contenu dispersé, afin qu'il puisse être facilement traduit plus tard
* Vous aider à gérer la traduction de texte en plus des dates, des nombres, etc.
* Fournir un moyen facile pour que les traductions soient importées dans votre application

**Il ne fait PAS :**

* Traduire votre contenu pour vous
* Vous dire comment découvrir quelle locale l'utilisateur souhaite
* Corriger ce bug sans rapport que vous avez traité pendant les dernières heures (désolé, non ?)

Ok, alors commençons tout de suite !

### Configuration du projet d'exemple

```
$ npx create-react-app i18n-example
```

Je vais ajouter react router pour montrer comment `react-intl` fonctionne avec plusieurs pages.

```
$ cd i18n-example && npm install react-router-dom
```

Mon application d'exemple aura trois composants React : une page principale, une sous-page et un composant qui est importé dans la sous-page. Voir la structure des fichiers et les pages ci-dessous :

```
/src
  /components
    Weather.js
  /pages
    Home.js
    Day.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*T-74w-twF7GYNn7eeFkumg.jpeg)

L'état du projet jusqu'à ce point peut être trouvé [ici](https://github.com/austintackaberry/i18n-example/commit/d792a3fa673e1985340900a728ee6479e79118db).

### Configuration de `react-intl`

Maintenant, le plaisir commence. Nous allons installer `react-intl` et nous mettre au travail !

```
$ npm install react-intl
```

L'objectif principal derrière `react-intl` est de permettre la prise en charge de l'i18n tout en minimisant l'impact sur votre flux de codage normal. Certes, vous avez du contenu à de nombreux endroits dans votre application web. Vous avez du texte, des nombres et des dates dans des paragraphes, des tableaux et des en-têtes.

Que feriez-vous si vous deviez créer une bibliothèque i18n ? Eh bien, vous avez ces morceaux de contenu partout dans votre application web. Et vous voulez que tout soit facilement traduisible. Si vous alliez donner votre contenu à un traducteur, vous ne lui donneriez pas votre code et ne diriez pas « bonne chance, au travail ».

Vous voudriez trouver un moyen de mettre tout votre contenu dans un seul fichier, puis lui donner ce fichier. Ils le traduiraient dans une autre langue, disons de l'anglais vers l'espagnol, et vous donneraient un fichier avec tout le contenu en espagnol.

Ok, super. Vous l'avez fait, mais maintenant vous devez prendre le contenu en espagnol dans ce fichier et le redistribuer à son emplacement d'origine. Comment feriez-vous cela de manière programmatique ? Peut-être attribueriez-vous des identifiants à chaque morceau de contenu, afin de ne pas perdre la trace de l'emplacement d'origine de chaque morceau de contenu.

Et c'est à peu près tout !

La première étape consiste à envelopper votre application dans le composant `<IntlProvider>` :

```
<IntlProvider>
  <App />
</IntlProvider>
```

Maintenant, vous devez identifier le contenu pour `react-intl` qui sera éventuellement traduit. Sur la page d'accueil de mon application, j'ai le paragraphe suivant :

```
<p>It is a beautiful day outside.</p>
```

Je dois dire à `react-intl` que ceci est du contenu que je veux traduire et lui donner un identifiant, afin qu'il puisse suivre ce contenu et son emplacement d'origine :

```
<FormattedMessage
  id="Home.dayMessage"
  defaultMessage="It's a beautiful day outside."
/>
```

Par défaut, le texte sera sorti dans un `<span>`, nous devrons donc l'envelopper dans le `<p>` d'origine si nous voulons qu'il reste un paragraphe.

```
<p>
  <FormattedMessage
    id="Home.dayMessage"
    defaultMessage="It's a beautiful day outside."
  />
</p>

```

Je vais maintenant faire cela pour tout le contenu de mon application web.

L'état du projet jusqu'à présent peut être trouvé [ici](https://github.com/austintackaberry/i18n-example/commit/f85d4d4f6c029a2fa9b29beaf25fcae3de5e6d12).

### Ajout de babel-plugin-react-intl

Maintenant que tout est configuré, vous vous demandez peut-être comment nous pouvons facilement agréger tout ce contenu en un seul fichier. Cependant, à des fins de débogage, il pourrait être utile d'avoir des fichiers JSON individuels pour chaque composant React. Devinez quoi, il y a un plugin babel pour cela !

```
$ npm install babel-plugin-react-intl
```

Ce plugin créera une copie de votre répertoire `src`, mais au lieu d'avoir vos fichiers de composants React, il aura des fichiers json avec le contenu des messages et l'identifiant. Un pour chaque fichier de composant dans votre répertoire `src`. Il le fera lorsque vous exécuterez `npm run build`.

Maintenant, nous devons éjecter de create-react-app, afin de pouvoir ajouter notre nouveau plugin dans notre configuration babel. Assurez-vous de commiter toutes les modifications puis exécutez :

```
$ npm run eject
```

Maintenant, nous devrons ajouter un fichier `.babelrc` dans la racine de notre projet avec le contenu suivant :

```json
{
  "presets":["react-app"],
  "plugins": [
    ["react-intl", {
      "messagesDir": "./public/messages/"
    }]
  ]
}
```

Maintenant que babel peut utiliser notre nouveau plugin que nous venons d'ajouter, nous pouvons passer à notre prochaine étape : générer ces fichiers JSON.

```
$ npm run build
```

Une fois que vous exécutez cela, vous devriez remarquer que vous avez un répertoire `public/messages/src` qui semble être un clone de votre répertoire `src` d'origine, sauf que tous vos fichiers de composants sont en fait des fichiers JSON.

```
/messages
  /src
    /components
      Weather.json
    /pages
      Home.json
      Day.json
```

Maintenant, regardons le contenu de l'un d'eux, Home.json :

```json
[
  {
    "id": "Home.header",
    "defaultMessage": "Hello, world!"
  },
  {
    "id": "Home.dayMessage",
    "defaultMessage": "It's a beautiful day outside."
  },
  {
    "id": "Home.dayLink",
    "defaultMessage": "Click here to find out why!"
  }
]
```

L'état du projet jusqu'à présent peut être trouvé [ici](https://github.com/austintackaberry/i18n-example/commit/5eec540f62ace18e3b34a48ef94599c6f1820470).

### Combinaison des fichiers JSON

Il a fait exactement ce que nous pensions qu'il ferait. Il peut être utile d'avoir notre contenu organisé dans cette structure, mais finalement nous voudrons qu'il soit dans un seul fichier, et nous devons qu'il inclue toutes les traductions que nous allons faire.

Maintenant, nous devons créer un script qui fait cela pour nous. Heureusement, les gens de `react-intl` nous ont donné un bon point de départ avec [ce script](https://github.com/yahoo/react-intl/blob/master/examples/translations/scripts/translate.js).

```js
import * as fs from "fs";
import { sync as globSync } from "glob";
import { sync as mkdirpSync } from "mkdirp";
import last from "lodash/last";

const MESSAGES_PATTERN = "./public/messages/**/*.json";
const LANG_DIR = "./public/locales/";
const LANG_PATTERN = "./public/locales/*.json";

// Essayer de supprimer les fichiers json actuels de public/locales
try {
  fs.unlinkSync("./public/locales/data.json");
} catch (error) {
  console.log(error);
}

// Fusionner les fichiers json traduits (es.json, fr.json, etc) en un seul objet
// afin qu'ils puissent être fusionnés avec l'objet "en" agrégé ci-dessous

const mergedTranslations = globSync(LANG_PATTERN)
  .map(filename => {
    const locale = last(filename.split("/")).split(".json")[0];
    return { [locale]: JSON.parse(fs.readFileSync(filename, "utf8")) };
  })
  .reduce((acc, localeObj) => {
    return { ...acc, ...localeObj };
  }, {});

// Agrège les messages par défaut qui ont été extraits des composants React de l'application d'exemple
// via le plugin Babel React Intl. Une erreur sera levée si
// il y a des messages dans différents composants qui utilisent le même `id`. Le résultat
// est une collection plate de paires `id: message` pour la locale par défaut de l'application.

const defaultMessages = globSync(MESSAGES_PATTERN)
  .map(filename => fs.readFileSync(filename, "utf8"))
  .map(file => JSON.parse(file))
  .reduce((collection, descriptors) => {
    descriptors.forEach(({ id, defaultMessage }) => {
      if (collection.hasOwnProperty(id)) {
        throw new Error(`Duplicate message id: ${id}`);
      }
      collection[id] = defaultMessage;
    });

    return collection;
  }, {});

// Créer un nouveau répertoire dans lequel nous voulons écrire les messages agrégés
mkdirpSync(LANG_DIR);

// Fusionner les messages par défaut agrégés avec les fichiers json traduits et
// écrire les messages dans ce répertoire
fs.writeFileSync(
  `${LANG_DIR}data.json`,
  JSON.stringify({ en: defaultMessages, ...mergedTranslations }, null, 2)
);
```

Nous devrons le modifier un peu car, tel quel, ce script générera une fausse traduction. Nous ne voulons pas cela car ce n'est pas pratique.

Nous valons mieux que cela ! Nous voulons qu'il lise une vraie traduction !

Le script que nous utiliserons pour faire cela est ci-dessous :

Nous devrons enregistrer ce fichier dans notre répertoire `scripts` puis modifier `package.json` pour qu'il exécute réellement le script.

Avant de faire cela, nous devrons faire quelques choses, afin que notre code ESNext puisse être compris. Tout d'abord, nous devrons ajouter `babel-cli` pour nous assurer que le script est transpilé.

```
$ npm install --save-dev babel-cli
```

Ensuite, nous devons ajouter le preset `env` à notre `.babelrc` pour qu'il ressemble à ceci :

```json
{
  "presets":["react-app", "env"],
  "plugins": [
    ["react-intl", {
      "messagesDir": "./public/messages/"
    }]
  ]
}
```

Enfin, nous devons modifier notre `package.json` pour qu'il exécute notre script :

```json
{...
  "scripts": {
    "build:langs": "NODE_ENV='production' babel-node
      scripts/mergeMessages.js",
    "build": "npm run build:langs && node scripts/build.js",
    ...
  },
  ...
}
```

Notez que nous exécutons le script mergeMessages avant `npm run build`. Cela est dû au fait que nous voulons générer notre fichier `data.json` final dans le répertoire `/public` avant que notre script de build ne le copie dans `/build`.

D'accord, maintenant lorsque nous exécutons `npm run build`, nous devrions voir `build/locales/data.json` qui combine tous nos fichiers JSON en un seul.

L'état du projet jusqu'à présent peut être trouvé [ici](https://github.com/austintackaberry/i18n-example/commit/47fe4a87b74f1318337ee13f459725cb45124149).

### Il est temps de commencer à traduire

Maintenant que nous avons créé un script qui agrège nos messages par défaut et nos traductions en un seul fichier, commençons à faire quelques traductions ! Pour cet exemple, nous traduirons en espagnol. Notre script que nous venons de créer lira tous les fichiers `*.json` de `/public/locales`, nous devrons donc nommer notre nouveau fichier de traduction `/public/locales/es.json` et ajouter le contenu ci-dessous :

```json
{
  "Weather.message": "¡Porque está soleado!",
  "Day.homeLink": "Regresar a inicio",
  "Home.header": "¡Hola Mundo!",
  "Home.dayMessage": "Es un hermoso día afuera.",
  "Home.dayLink": "¡Haz clic aquí para averiguar por qué!"
}
```

Maintenant, lorsque nous exécutons `npm run build`, notre script mergeMessages créera un fichier `data.json` dans `/public/locales`, puis il sera copié dans `/build/locales`. Notre fichier `data.json` final ressemblera à ceci :

```json
{
  "en": {
    "Weather.message": "Because it is sunny!",
    "Day.homeLink": "Go back home",
    "Home.header": "Hello, world!",
    "Home.dayMessage": "It's a beautiful day outside.",
    "Home.dayLink": "Click here to find out why!"
  },
  "es": {
    "Weather.message": "¡Porque está soleado!",
    "Day.homeLink": "Regresar a inicio",
    "Home.header": "¡Hola Mundo!",
    "Home.dayMessage": "Es un hermoso día afuera.",
    "Home.dayLink": "¡Haz clic aquí para averiguar por qué!"
  }
}
```

Nous y sommes presque ! La dernière étape consiste à charger dynamiquement la version espagnole du texte si les paramètres de langue du navigateur de l'utilisateur sont en espagnol. Nous devons modifier `index.js` pour lire les paramètres de langue du navigateur, puis donner ces informations ainsi que les traductions correctes à `<IntlProvider />` et finalement à notre application.

Notre fichier `index.js` final ressemble à ceci :

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import registerServiceWorker from "./registerServiceWorker";
import { BrowserRouter } from "react-router-dom";
import { IntlProvider, addLocaleData } from "react-intl";
import en from "react-intl/locale-data/en";
import es from "react-intl/locale-data/es";

import localeData from "./../build/locales/data.json";

addLocaleData([...en, ...es]);

// Définir la langue de l'utilisateur. Différents navigateurs ont la locale de l'utilisateur définie
// sur différents champs de l'objet `navigator`, nous nous assurons donc de tenir compte
// de ces différences en vérifiant tous
const language =
  (navigator.languages && navigator.languages[0]) ||
  navigator.language ||
  navigator.userLanguage;

// Diviser les locales avec un code de région
const languageWithoutRegionCode = language.toLowerCase().split(/[_-]+/)[0];

// Essayer la locale complète, essayer la locale sans code de région, revenir à 'en'
const messages =
  localeData[languageWithoutRegionCode] ||
  localeData[language] ||
  localeData.en;

ReactDOM.render(
  <IntlProvider locale={language} messages={messages}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </IntlProvider>,
  document.getElementById("root")
);
registerServiceWorker();
```

(Code largement copié du gist de [Preethi Kasireddy](https://www.freecodecamp.org/news/setting-up-internationalization-in-react-from-start-to-finish-6cb94a7af725/undefined) [ici](https://gist.github.com/iam-peekay/5a4e9431c9c785d3e62e584503619ecc#file-reactintl9-js))

Une autre petite chose que nous devons faire est de modifier nos configurations webpack pour permettre les imports en dehors de `src` et `node_modules`.

Maintenant, si nous changeons les paramètres de langue de notre navigateur en espagnol, nous devrions voir notre contenu traduit en espagnol !

![Image](https://cdn-media-1.freecodecamp.org/images/1*4DNdd7o70MWMetI9vgR0gw.jpeg)

L'état final du projet peut être trouvé [ici](https://github.com/austintackaberry/i18n-example).