---
title: 'Vue Test Utils et Jest : comment écrire des tests unitaires simples pour les
  composants Vue'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-08T13:24:32.000Z'
originalURL: https://freecodecamp.org/news/simple-unit-tests-with-vue-test-utils-and-jest-c384d7abc321
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KlrR7EWfaDgtcW5hJGFjHQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: 'Vue Test Utils et Jest : comment écrire des tests unitaires simples pour
  les composants Vue'
seo_desc: 'By Edd Yerburgh

  In this tutorial I’m going to show you how to test Vue components.

  We’re going to write unit tests and snapshot tests with Jest and Vue Test Utils.
  All without Webpack.

  This tutorial is for users familiar with unit testing. If you’re ...'
---

Par Edd Yerburgh

Dans ce tutoriel, je vais vous montrer comment tester les composants Vue.

Nous allons écrire des tests unitaires et des tests de snapshot avec Jest et Vue Test Utils. Tout cela sans Webpack.

Ce tutoriel s'adresse aux utilisateurs familiers avec les tests unitaires. Si vous débutez avec les tests unitaires, consultez mon article sur [les tests unitaires des composants Vue pour débutants](https://eddyerburgh.me/unit-test-vue-components-beginners).

### Installation

J'ai créé [un projet de démarrage simple](https://github.com/eddyerburgh/vue-unit-test-starter/). Clonez-le dans un répertoire :

```
git clone https://github.com/eddyerburgh/vue-unit-test-starter.git
```

Accédez au répertoire et installez les dépendances :

```
cd vue-unit-test-starter && npm install
```

Une fois les dépendances installées, lancez le serveur de développement :

```
npm run dev
```

Maintenant, nous pouvons revenir au code.

Une chose à aborder est les alias. Les alias sont un moyen d'utiliser une notation abrégée pour importer des fichiers. Au lieu de longues instructions d'importation comme celle ci-dessous :

```
import someModule from '../../../../../src/components/someModule'
```

Vous pouvez utiliser une notation abrégée, ou alias. Un alias courant est le symbole `@`, qui résout vers le répertoire `src` :

```
import someModule from '@/components/someModule'
```

Note : Vous pouvez définir n'importe quel alias, mais les projets vue-cli utilisent `@` pour faire référence au répertoire `src`.

Dans les projets vue-cli, [Webpack est utilisé pour ajouter cette fonctionnalité](https://github.com/eddyerburgh/jest-vue-starter/blob/master/build/webpack.base.conf.js#L25). C'est bien, mais nous n'utilisons pas Webpack pour exécuter nos tests. Nous avons besoin d'une autre façon de résoudre les alias.

C'est là que babel intervient. Il existe un plugin — babel-plugin-module-resolver — qui résout les alias dans babel. Vous pouvez le voir dans le `.babelrc`. Il n'est utilisé que dans l'environnement de test, car lorsque vous exécutez la build de développement ou de production, Webpack s'occupe de la résolution des alias.

Consultez ce fichier :

Ok, maintenant que vous avez une vue d'ensemble du projet, il est temps d'ajouter Jest.

### Jest

Jest est un framework de test. C'est l'un des [frameworks de test les plus rapides pour les composants Vue en fichier unique](https://github.com/eddyerburgh/vue-unit-test-perf-comparison) (SFC).

En plus d'exécuter des tests, Jest propose une multitude d'autres fonctionnalités prêtes à l'emploi, comme les mocks, la couverture de code et les tests de snapshot.

La première chose à faire est d'installer Jest :

```
npm install --save-dev jest
```

Pour tester les SFC, vous devez les compiler en JavaScript avant d'exécuter les tests. Si vous essayez d'exécuter un SFC non compilé, vous obtiendrez une erreur de syntaxe.

Jest ne compile pas les fichiers `.vue` par défaut. Vous devez lui indiquer de les compiler. Vous faites cela en ajoutant un champ `jest` au `package.json`.

Ajoutez le code ci-dessous à votre `package.json`.

```
"jest": {    "moduleFileExtensions": [      "js",      "json",      "vue"    ],    "transform": {      "^.+\\.js$": "<rootDir>/node_modules/babel-jest",      ".*\\.(vue)$": "<rootDir>/node_modules/vue-jest"    }  }
```

Vous verrez un champ `moduleFileExtensions`. Cela indique à Jest d'exécuter les fichiers avec une extension `.vue`, ainsi que `.js` et `.json`.

Il y a aussi un champ `transform`. Cela indique à Jest comment compiler les fichiers avant de les exécuter. Il correspond à tous les fichiers `.js` et les compile avec babel-jest. Tous les fichiers `.vue` sont compilés avec vue-jest.

Ce sont des transformations personnalisées construites pour Jest. babel-jest compile JavaScript. vue-jest prend les fichiers `.vue` et les compile en JavaScript.

Vous devez installer les deux packages :

```
npm install --save-dev babel-jest vue-jest
```

Ok, maintenant vous devriez ajouter un test de vérification, pour vous assurer que tout fonctionne.

Dans `src/components`, créez un répertoire `__tests__`. Ajoutez un fichier `MessageToggle.spec.js`. Le chemin complet du fichier sera donc `src/components/__tests__/MessageToggle.spec.js`.

Copiez le code ci-dessous dans le fichier :

Jest exécute automatiquement tous les fichiers `.js` dans le répertoire `__tests__`. Il ajoute même une variable d'environnement de test, donc tout ce que fait votre script de test est d'exécuter Jest.

Dans le champ `scripts` de votre `package.json`, ajoutez le script `unit` :

```
"unit": "jest"
```

Maintenant, exécutez le script :

```
npm run unit
```

Super, premier test réussi ?.

Maintenant, vous allez écrire des tests plus complexes en utilisant Vue Test Utils.

### Vue Test Utils

[Vue Test Utils](https://github.com/vuejs/vue-test-utils/) est en version bêta pour le moment, mais vous pouvez l'utiliser sans problème. L'API est pratiquement finalisée.

Installez-le :

```
npm install --save-dev @vue/test-utils
```

Maintenant, vous allez remplacer le test dans `MessageToggle.spec.js` par des tests utilisant Vue Test Utils.

Copiez le code ci-dessous dans `src/components/__tests__/MessageToggle.spec.js`

Ici, nous pouvons utiliser la fonction `[mount](https://github.com/vuejs/vue-test-utils/blob/dev/docs/en/api/mount.md)` pour retourner un objet wrapper. Le wrapper contient quelques méthodes d'assistance, comme `text`, qui aident à assert les composants. Vous pouvez voir une liste complète dans [la documentation](https://github.com/vuejs/vue-test-utils/tree/dev/docs/en/api/wrapper).

Ok, ajoutons un test plus complexe qui effectue une action sur le composant `Messagetoggle`. Copiez le code ci-dessous dans `MessageToggle.spec.js` :

Cette fois, nous cliquons sur un bouton (`#toggle-message`) dans `MessageToggle` et vérifions que le texte de la balise `<p>` a changé correctement.

Maintenant, exécutez le script de test :

```
npm run unit
```

Woop, tests réussis ! ?

Vue Test Utils abstrait les internes de Vue. Donc tout ce que vous avez à faire est d'apprendre l'API de Vue Test Utils.

Maintenant, vous allez écrire un test pour le composant List. Le composant List prend des props, heureusement Vue Test Utils nous donne un moyen de passer des props lors du montage du composant.

Créez un fichier `/src/components/__tests__/List.spec.js`, et collez le code ci-dessous

Cette fois, vous remarquerez que nous utilisons la fonction `shallow`. C'est la même chose que `mount`, sauf qu'elle ne rend le composant qu'à un niveau de profondeur. Généralement, il est préférable d'utiliser shallow.

Maintenant que vous avez écrit quelques tests unitaires, il est temps de regarder les tests de snapshot.

### Tests de snapshot

Jest a cette grande fonctionnalité appelée tests de snapshot.

Les tests de snapshot prennent essentiellement une copie de votre arbre de composants sous forme de chaîne, puis la comparent chaque fois que vous exécutez vos tests. Si le HTML rendu du composant change, le test échoue.

Ajoutons un test de snapshot à `Messag.spec.js`.

Vous devez rendre le composant en une chaîne en utilisant le vue-server-renderer. La chaîne retournée n'est pas très joli, donc vous devriez ajouter jest-serializer-vue pour embellir vos snapshots.

```
npm install --save-dev vue-server-renderer jest-serializer-vue
```

Vous devez également indiquer à Jest d'utiliser le serializer. Ajoutez un champ `snapshotSerializers` à l'intérieur du champ `jest` dans votre `package.json` :

```
"snapshotSerializers": [    "<rootDir>/node_modules/jest-serializer-vue"]
```

Maintenant, mettez à jour List.spec.js pour inclure un test de snapshot :

Ce test monte le composant de manière superficielle et le rend en une chaîne HTML avec vue-server-renderer.

Maintenant, exécutez vos tests :

```
npm run unit
```

Vous verrez une nouvelle sortie concernant un snapshot sauvegardé. Allez jeter un coup d'œil dans `src/components/__tests__/__snapshots__/List.spec.js.snap` :

```
// Jest Snapshot v1, https://goo.gl/fbAQLP
```

```
exports[`List.vue has same HTML structure 1`] = `<ul>    <li>        list item one    </li>    <li>        list item two    </li></ul>`;
```

Cool, un snapshot. ?

Maintenant, si le balisage de `List.vue` change, Jest vous avertira que le snapshot a changé lorsque vous exécuterez vos tests.

### Conclusion

Maintenant, vous avez configuré des tests unitaires et des tests de snapshot avec Jest et Vue Test Utils.

J'ai passé rapidement sur quelques concepts. Vous pouvez consulter [le dépôt finalisé sur GitHub](https://github.com/eddyerburgh/jest-vue-example) si votre projet n'a pas fonctionné correctement.

Jest a [beaucoup plus de fonctionnalités](https://facebook.github.io/jest/) pour faciliter les tests.

Vue Test Utils a également beaucoup plus de méthodes — [consultez la documentation](https://github.com/vuejs/vue-test-utils/tree/dev/docs/en).

Les tests unitaires des composants Vue n'ont jamais été aussi faciles, alors sortez et écrivez quelques tests !

Si vous avez appris quelque chose de cet article, partagez et donnez un ? pour faire passer le mot !