---
title: Un tutoriel complet sur le boilerplate React — De zéro à héros
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T19:01:41.000Z'
originalURL: https://freecodecamp.org/news/a-complete-react-boilerplate-tutorial-from-zero-to-hero-20023e086c4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IRVIWE6HiS8wQstgybKwvw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Un tutoriel complet sur le boilerplate React — De zéro à héros
seo_desc: 'By Leonardo Maldonado

  When we’re starting learn React, to make our projects we need to make a boilerplate
  from scratch or use some provided by the community. Almost all the times it’s the
  create-react-app that we use to create an app with no build co...'
---

Par Leonardo Maldonado

Lorsque nous commençons à apprendre React, pour réaliser nos projets, nous devons créer un boilerplate à partir de zéro ou utiliser celui fourni par la communauté. Presque tout le temps, c'est _create-react-app_ que nous utilisons pour créer une application sans configuration de build. Ou nous créons simplement notre propre boilerplate simple à partir de zéro.

De cela, il vient à l'esprit : pourquoi ne pas créer un boilerplate avec toutes les dépendances que j'utilise toujours et le laisser prêt ? La communauté a également pensé de cette manière, donc maintenant nous avons plusieurs boilerplates créés par la communauté. Certains sont plus complexes que d'autres, mais ils ont toujours le même objectif d'économiser le maximum de temps.

Cet article vous apprendra comment vous pouvez construire votre propre boilerplate à partir de zéro avec les principales dépendances utilisées dans la communauté React aujourd'hui. Nous allons utiliser certaines des fonctionnalités modernes les plus courantes ces jours-ci et à partir de là, vous pouvez le personnaliser comme vous le souhaitez.

[**Le boilerplate créé par cet article sera disponible ici !**](https://github.com/leonardomso/react-bolt)

### Installation

Tout d'abord, nous allons créer un dossier pour démarrer notre boilerplate. Vous pouvez le nommer comme vous le souhaitez, je vais nommer le mien **_react-bolt_**.

Ouvrez votre terminal et créez-le comme ceci :

```
mkdir react-bolt
```

Maintenant, allez dans votre dossier créé et tapez la commande suivante :

```
npm init -y
```

_NPM_ va créer un fichier `package.json` pour vous, et toutes les dépendances que vous avez installées et vos commandes seront là.

Maintenant, nous allons créer la structure de dossier de base pour notre boilerplate. Elle sera comme ceci pour l'instant :

```
react-bolt    |--config    |--src    |--tests
```

### Webpack

Webpack est le module-bundler le plus célèbre pour les applications JavaScript de nos jours. Basiquement, il regroupe tout votre code et génère un ou plusieurs bundles. Vous pouvez en apprendre plus à ce sujet [ici](https://webpack.js.org/).

Dans ce boilerplate, nous allons l'utiliser, alors installez toutes ces dépendances :

```
npm install --save-dev webpack webpack-cli webpack-dev-server webpack-merge html-webpack-plugin clean-webpack-plugin img-loader url-loader file-loader 
```

Maintenant, dans notre dossier `config`, nous allons créer un autre dossier appelé `webpack`, puis à l'intérieur de ce dossier `webpack`, créez 5 fichiers.

Créez un fichier appelé `paths.js`. À l'intérieur de ce fichier se trouvera le répertoire cible pour tous vos fichiers de sortie.

À l'intérieur, mettez tout ce code :

Maintenant, créez un autre fichier appelé `rules.js`, et mettez le code suivant à l'intérieur :

Après cela, nous allons créer 3 fichiers supplémentaires :

`webpack.common.babel.js`

`webpack.dev.babel.js`

`webpack.prod.babel.js`

Basiquement, dans notre fichier `webpack.common.babel.js`, nous avons configuré notre entrée et notre sortie et inclus également tous les plugins nécessaires. Dans le fichier `webpack.dev.babel.js`, nous avons défini le mode sur développement. Et dans notre fichier `webpack.prod.babel.js`, nous avons défini le mode sur production.

Après cela, dans notre dossier racine, nous allons créer le dernier fichier webpack appelé `webpack.config.js` et y mettre le code suivant :

Notre configuration webpack est prête, alors maintenant nous allons travailler sur d'autres parties du boilerplate avec Babel, ESLint, Prettier, etc.

### Babel

Je pense que presque tout le monde qui travaille avec React a probablement entendu parler de Babel et de la façon dont ce simple transpileur facilite notre vie. Si vous ne savez pas ce que c'est, Babel est basiquement un transpileur qui convertit votre code JavaScript en ancien ES5 JavaScript qui peut s'exécuter dans n'importe quel navigateur.

Nous allons utiliser un ensemble de plugins Babel, alors dans notre dossier racine, installez :

```
npm install --save-dev @babel/core @babe/cli @babel/node @babel/plugin-proposal-class-properties @babel/plugin-proposal-object-rest-spread @babel/plugin-syntax-dynamic-import @babel/plugin-syntax-import-meta @babel/plugin-transform-async-to-generator @babel/plugin-transform-runtime @babel/preset-env @babel/preset-react @babel/register @babel/runtime babel-eslint babel-jest babel-loader babel-core@7.0.0-bridge.0
```

Après cela, nous allons créer un fichier dans notre dossier racine appelé `.babelrc` et à l'intérieur de ce fichier, nous allons mettre le code suivant :

Maintenant, notre projet est compilé par Babel, et nous pouvons utiliser la syntaxe JavaScript de nouvelle génération sans aucun problème.

### ESLint

L'outil le plus utilisé pour le linting des projets de nos jours est ESLint. Il est vraiment utile pour trouver certaines classes de bugs, tels que ceux liés à la portée des variables, à l'assignation de variables non déclarées, et ainsi de suite.

Tout d'abord, installez les dépendances suivantes :

```
npm install --save-dev eslint eslint-config-airbnb eslint-config-prettier eslint-loader eslint-plugin-babel eslint-plugin-import eslint-plugin-jsx-a11y eslint-plugin-prettier eslint-plugin-react 
```

Ensuite, dans notre dossier racine, créez un fichier appelé `.eslintrc` et mettez le code suivant à l'intérieur :

### Prettier

Prettier est basiquement un formateur de code. Il analyse votre code et le réimprime avec ses propres règles qui prennent en compte la longueur maximale de la ligne, en enveloppant le code lorsque cela est nécessaire.

Vous devez simplement l'installer :

```
npm install --save-dev prettier
```

Et dans notre dossier racine, créez un fichier appelé `.prettierrc` et mettez le code suivant à l'intérieur :

### React

React est une bibliothèque d'application JavaScript open-source pour construire des interfaces utilisateur. Elle a été développée par Facebook et possède une énorme communauté derrière elle. Si vous lisez cet article, je suppose que vous connaissez déjà React, mais si vous voulez en apprendre plus à ce sujet, vous pouvez lire [ici](https://reactjs.org/).

Nous allons installer les dépendances suivantes :

```
npm install --save react react-dom cross-env
```

Et à l'intérieur de notre dossier `src`, nous allons créer un simple fichier HTML `index.html` et y mettre le code suivant :

Après cela, nous allons créer un simple projet React. À l'intérieur de notre dossier `src`, créez un fichier `index.js` comme ceci :

À l'intérieur de notre dossier `src`, nous allons avoir la structure suivante :

```
src    |--actions    |--components    |--reducers    |--reducers    |--store
```

Créez un fichier appelé `App.js` à l'intérieur du dossier `components`, et mettez le code suivant à l'intérieur :

### Redux

Redux facilite la gestion de l'état de votre application. Une autre façon de voir cela est qu'il vous aide à gérer les données que vous affichez et comment vous répondez aux actions de l'utilisateur. Ces jours-ci, beaucoup de gens préfèrent d'autres options comme _MobX_ ou simplement le _setState_ lui-même, mais je vais rester avec Redux pour ce boilerplate.

Tout d'abord, nous allons installer quelques dépendances :

```
npm install --save redux react-redux redux-thunk
```

Ensuite, nous allons créer notre store Redux et y mettre un état. Dans notre dossier `store`, créez un fichier `index.js` et mettez le code suivant à l'intérieur :

Maintenant, à l'intérieur de notre dossier `reducers`, créez un `index.js` et mettez le code suivant :

Enfin, nous allons dans notre `index.js` dans notre dossier `src`, et enveloppons le code avec le `<Provider` /> et passons notre `store` en tant que props pour le rendre disponible à notre application.

Cela va être comme ceci :

Tout est fait. Notre store Redux est configuré et prêt à l'emploi.

### React Router

React Router est la bibliothèque de routage standard pour React. Basiquement, il garde votre UI synchronisée avec l'URL. Nous allons l'utiliser dans notre boilerplate, alors installez-le :

```
npm install --save react-router-dom
```

Après cela, allez dans notre `index.js` dans notre dossier `src` et enveloppez tout le code là avec le `<BrowserRouter>`.

Notre `index.js` dans notre dossier `src` va finir comme ceci :

### Styled Components

Styled Components facilite le CSS pour tout le monde, car il vous aide à organiser votre projet React. Son objectif est d'écrire des composants plus petits et réutilisables. Nous allons l'utiliser, et si vous voulez en apprendre plus à ce sujet, lisez [ici](https://www.styled-components.com/).

Tout d'abord, installez-le :

```
npm install --save styled-components
```

Ensuite, dans notre fichier `App.js` à l'intérieur de notre dossier `components`, nous allons créer un simple titre en utilisant Styled Components. Notre titre va être comme ceci :

Et à l'intérieur de notre fichier, nous devons importer les composants stylisés, donc notre fichier va finir comme ceci :

### Jest & React Testing Library

Jest est une bibliothèque de test JavaScript open-source de Facebook. Elle facilite le test de votre application et nous donne beaucoup d'informations sur ce qui donne la bonne sortie et ce qui ne le fait pas. React Testing Library est une solution très légère pour tester les composants React. Basiquement, cette bibliothèque est un remplacement pour Enzyme.

Chaque application a besoin de certains types de tests. Je ne vais pas écrire de tests dans cet article, mais je vais vous montrer comment vous pouvez configurer ces outils pour commencer à tester vos applications.

Tout d'abord, nous allons installer les deux :

```
npm install --save-dev jest jest-dom react-testing-library
```

Après cela, allez dans notre package.json et mettez ce qui suit après tout :

Ensuite, allez dans notre dossier `config`, et à l'intérieur, créez un autre dossier appelé `tests` et à l'intérieur de ce dossier, créez 2 fichiers.

Tout d'abord, créez un fichier appelé `jest.config.js` et mettez le code suivant à l'intérieur :

Ensuite, créez un fichier appelé `rtl.setup.js` et mettez le code suivant à l'intérieur :

Tout est fait. Notre boilerplate est prêt à l'emploi et vous pouvez l'utiliser maintenant.

Maintenant, allez dans notre fichier `package.json` et mettez le code suivant :

Maintenant, si vous exécutez la commande `npm start` et allez sur `localhost:8080`, nous devrions voir notre application fonctionner correctement !

[**Si vous voulez voir mon code final, le boilerplate créé par cet article est disponible ici !**](https://github.com/leonardomso/react-bolt)

J'ai quelques idées pour certaines fonctionnalités que j'aimerais inclure dans le boilerplate, alors n'hésitez pas à contribuer !

? S[**uivez-moi sur Twitter !**](https://twitter.com/leonardomso)   
**✨** S[**uivez-moi sur GitHub !**](https://github.com/leonardomso)

_Je cherche une opportunité à distance, alors si vous en avez une, j'aimerais en entendre parler, alors s'il vous plaît contactez-moi !_