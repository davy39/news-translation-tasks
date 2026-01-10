---
title: La commande React Scripts Start – Explication des scripts NPM de Create-React-App
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-01-04T16:15:00.000Z'
originalURL: https://freecodecamp.org/news/create-react-app-npm-scripts-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/cra-npm-scripts-explained.png
tags:
- name: create-react-app
  slug: create-react-app
- name: npm
  slug: npm
- name: npm scripts
  slug: npm-scripts
- name: React
  slug: react
seo_title: La commande React Scripts Start – Explication des scripts NPM de Create-React-App
seo_desc: "Creating a React application requires you to set up build tools such as\
  \ Babel and Webpack. These build tools are required because React's JSX syntax is\
  \ a language that the browser doesn't understand. \nTo run your React application,\
  \ you need to turn y..."
---

La création d'une application React nécessite la configuration d'outils de build tels que Babel et Webpack. Ces outils de build sont nécessaires car la syntaxe JSX de React est un langage que le navigateur ne comprend pas. 

Pour exécuter votre application React, vous devez transformer votre JSX en JavaScript standard, que les navigateurs comprennent.

[Create React App (CRA)](https://github.com/facebook/create-react-app) est un outil pour créer des applications React monopages officiellement soutenu par l'équipe React. 

Le script génère les fichiers et dossiers nécessaires pour démarrer l'application React et l'exécuter dans le navigateur. Cela vous permet de vous concentrer sur le codage de votre application sans avoir à vous soucier des configurations de build.

## Les dépendances utilisées par create-react-app

Bien que vous ne voyiez pas Babel ou Webpack listés comme dépendances dans le fichier `package.json` généré, CRA utilise toujours Babel et Webpack sous le capot. C'est simplement que les configurations sont cachées dans le [package `react-scripts`](https://github.com/facebook/create-react-app/tree/master/packages/react-scripts).

Lorsque vous regardez le fichier `package.json` de react-scripts, vous verrez tous les packages nécessaires pour faire fonctionner React dans le navigateur. Il contient 58 packages, de la ligne 31 à 88 :

%[https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/package.json#L30]

C'est beaucoup de packages ! Décomposons un peu pour comprendre à quoi servent ces packages.

*Veuillez noter que cet article a été écrit en utilisant Create React App version 4.0.1 comme référence. Cet article vous aidera à comprendre ce qui se passe sous le capot lorsque vous utilisez les scripts NPM de Create React App.*

### Babel

Le but principal de Babel est de rendre votre code lisible par les anciens navigateurs. Depuis la sortie de ES 2015, les navigateurs ont vu des progrès lents mais réguliers pour implémenter de nouvelles API et fonctionnalités JavaScript. 

Les navigateurs les plus avancés comme Chrome et Safari peuvent supporter les nouvelles versions de JavaScript, mais JSX est une fonctionnalité spécifique à React qui ne fait pas partie des versions ES.

Babel transforme votre code JavaScript moderne en une version plus ancienne, puis ajoute des _polyfills_, un morceau de code qui implémente les fonctionnalités manquantes dans le navigateur mais nécessaires à votre application.

### ESLint

ESLint est un linter JavaScript qui analysera votre code et signalera toute erreur de code. La bibliothèque vous avertira depuis la console si vous avez des erreurs. Il fonctionne également bien avec un éditeur de code moderne comme VSCode.

### Jest

Jest est une bibliothèque de test de Facebook qui fonctionne très bien avec React. Les dépendances pour Jest vous permettent d'écrire des scripts de test pour votre application sans avoir à installer une autre bibliothèque de test.

### PostCSS

PostCSS est un plugin JavaScript pour transformer votre CSS. Les plugins PostCSS peuvent analyser votre CSS, supporter la syntaxe des variables et des mixins, transpiler la syntaxe CSS future, et bien plus encore en fonction de ses configurations.

### Webpack

Webpack est un bundler de modules pour JavaScript qui rassemble tout ce dont votre application a besoin. Cette bibliothèque peut également exécuter des tâches comme l'exécution de Babel, Jest, ESLint et PostCSS sur votre code.

Maintenant que vous avez une idée de l'utilisation des dépendances, continuons avec la compréhension de ce que `react-scripts` fait vraiment en arrière-plan.

## Ce que font react-scripts

Les react-scripts sont simplement des scripts pour exécuter les outils de build nécessaires pour transformer la syntaxe JSX de React en JavaScript standard de manière programmatique. 

Il y a quatre scripts fournis par ce package :

```json
"scripts: {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject"
},
```

Lorsque vous exécutez l'un des scripts, le [/bin/react-scripts.js](https://github.com/facebook/create-react-app/tree/master/packages/react-scripts/bin) sera exécuté pour démarrer le processus. Ce script examinera les arguments que vous avez passés dans l'appel. Il n'accepte que les arguments start, build, test et eject.

Tout autre argument que vous passez entraînera le retour d'un script inconnu dans le journal :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cra-unknown-script-2.png)
_Sortie de la console de script inconnu de CRA_

Lorsque vous passez un argument valide, il exécutera les scripts situés dans le [dossier `/scripts`](https://github.com/facebook/create-react-app/tree/master/packages/react-scripts/scripts). Commençons par examiner le script `start.js`.

## Comment fonctionne le processus react-scripts start

Avec l'argument `start`, NPM commencera le processus pour rendre un serveur de développement disponible pour votre application React. Voici une liste des tâches pour ce script :

* Définir l'environnement de build en `development` pour Node et Babel
* S'assurer que les variables d'environnement sont lues pour le processus de build 
* Vérifier que les packages installés dans votre projet ne sont pas obsolètes
* Vérifier si le code est en TypeScript ou non
* Importer les packages requis pour le processus, principalement les modules liés à Webpack
* Vérifier le port et l'IP hôte disponibles, par défaut 0.0.0.0:3000
* Exécuter le compilateur et écouter les messages de Webpack. Webpack prendra en charge l'utilisation de Babel, ESLint et d'autres outils pour préparer votre code
* Pendant que Webpack est en cours d'exécution, le script ouvrira votre navigateur et démarrera le serveur de développement

Le serveur de développement créé par [WebpackDevServer](https://github.com/facebook/create-react-app/blob/8bf050aa7c16078fed5e51ac8388d6100c29e105/packages/react-scripts/scripts/start.js#L37) créera également un écouteur pour les changements dans votre fichier JavaScript. Lorsque vous apportez des modifications et enregistrez votre fichier JavaScript, le serveur de développement recompilera votre code et rafraîchira rapidement le navigateur.

## Comment utiliser la commande react-scripts build

La commande `build` lancera le processus de création d'une application React prête pour la production. Principalement, elle effectue les mêmes étapes qu'une commande `start`, sauf qu'elle définit l'environnement de build en `production`.

Au lieu de vérifier les ports disponibles et d'exécuter un serveur de développement, le script exécutera la [fonction](https://github.com/facebook/create-react-app/blob/8bf050aa7c16078fed5e51ac8388d6100c29e105/packages/react-scripts/scripts/build.js#L152) [`build`](https://github.com/facebook/create-react-app/blob/8bf050aa7c16078fed5e51ac8388d6100c29e105/packages/react-scripts/scripts/build.js#L152), qui regroupera tous vos fichiers séparés en un seul fichier `bundle.js`. La build de production garantira également que votre code est optimisé et minifié pour assurer les meilleures performances.

Si vous avez déjà exécuté la commande `build` auparavant, le script prendra la taille actuelle de votre fichier et la comparera avec la prochaine build. Il vous montrera combien la taille du fichier a changé :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cra-build-result.png)
_React montre la comparaison après gzip dans la console_

Le résultat final de cette commande peut être trouvé dans le dossier `build/`, qui est généré à la racine de votre projet.

## Comment utiliser la commande react-scripts test

La commande `test` exécutera tous les scripts de test que vous avez écrits en utilisant [Jest](https://jestjs.io/). Vos tests seront exécutés sous un environnement Node. Jest fonctionnera en mode interactif de surveillance, ce qui signifie que chaque fois que vous enregistrez un fichier, il réexécutera les tests, comme la commande `start` recompile le code.

Vous pouvez enregistrer vos fichiers de test n'importe où dans le dossier `src/`, et le script trouvera et exécutera tout fichier avec les extensions `.test.js` ou `.spec.js`. Il exécutera également tout fichier `.js` sous le dossier `__tests__/`.

Vous pouvez voir le résultat des tests depuis le terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cra-test-result-1.png)
_Journal de la console du résultat de la commande react-scripts test_

Gardez à l'esprit que la commande de test de CRA ne couvre que les tests de vos composants et de la logique métier sous un environnement stable. Pour exécuter un test de bout en bout dans le navigateur, vous devez utiliser une autre bibliothèque de test.

## Comment utiliser la commande react-scripts eject

La dernière commande, `eject`, est utilisée pour supprimer la dépendance à `react-scripts` et exposer les outils de build et les configurations pour que vous puissiez les modifier. 

Tous les fichiers de configuration de `react-scripts` seront copiés dans le dossier `config/` à la racine de votre projet, et les scripts pour exécuter le build seront copiés dans le dossier `scripts/`. Les dépendances seront également déplacées dans le fichier `package.json` de votre racine.

Cette commande est une opération irréversible. Une fois que vous avez éjecté de la configuration CRA, vous ne pouvez pas revenir en arrière. Si vous avez commis votre code dans un système de gestion de code source comme Git, vous pouvez annuler les changements avec `git checkout` ou `git reset`.

Généralement, vous n'avez pas besoin d'exécuter cette commande car CRA a déjà fourni des configurations sensées adaptées aux petits et moyens projets. Si vous êtes intéressé à en apprendre plus, j'ai écrit un article sur l'éjection de votre application React ici :

[Doit-on éjecter son Create React App ?](https://sebhastian.com/create-react-app-eject/)

## Conclusion

Alors que de plus en plus de personnes utilisent CRA, l'équipe de développement recevra plus de retours sur la façon dont l'outil est utilisé dans des projets réels. Les informations obtenues par l'équipe de développement garantiront que CRA restera à jour avec les derniers outils et les meilleures pratiques pour construire des applications React.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !