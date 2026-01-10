---
title: Comment publier un package npm - Expliqué avec des exemples
subtitle: ''
author: Ikegah Oliver
co_authors: []
series: null
date: '2025-09-24T19:55:44.840Z'
originalURL: https://freecodecamp.org/news/how-to-publish-an-npm-package
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758743190885/78dd4f19-53eb-4101-9cf9-7c22ab5f6be2.png
tags:
- name: npm
  slug: npm
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
seo_title: Comment publier un package npm - Expliqué avec des exemples
seo_desc: If you’ve spent any time working with JavaScript, you’ve most likely come
  across npm—whether installing packages like Express, Lodash, or React, or running
  commands like npm init. While using npm is second nature for many JavaScript developers,
  some ...
---

Si vous avez passé du temps à travailler avec JavaScript, vous avez très probablement rencontré npm — que ce soit en installant des packages comme Express, Lodash ou React, ou en exécutant des commandes comme `npm init`. Bien que l'utilisation de npm soit une seconde nature pour de nombreux développeurs JavaScript, certains n'ont jamais exploré comment ces packages sont créés, structurés et partagés avec le reste du monde. Derrière chaque commande se cache un système puissant pour construire, gérer et distribuer du code JavaScript à grande échelle.

Cet article vous guidera à travers les bases de npm, expliquera son fonctionnement en coulisses et démontrera étape par étape comment créer et publier votre propre package npm sur le registre officiel npm. Que vous soyez un débutant commençant tout juste avec JavaScript ou un développeur chevronné ayant utilisé npm sans jamais publier de package, ce guide vous aidera à naviguer en toute confiance dans l'ensemble du processus, de la configuration au partage de votre code avec la communauté mondiale des développeurs.

## Table des matières

* [Qu'est-ce que npm ?](#heading-qu-est-ce-que-npm)
    
* [Composants de npm](#heading-composants-de-npm)
    
* [L'interface de ligne de commande](#heading-l-interface-de-ligne-de-commande)
    
* [Le registre](#heading-le-registre)
    
* [Le site web](#heading-le-site-web)
    
* [Qu'est-ce que le fichier package.json ?](#heading-qu-est-ce-que-le-fichier-package-json)
    
* [Comment fonctionne npm](#heading-comment-fonctionne-npm)
    
* [Comment publier une bibliothèque npm](#heading-comment-publier-une-bibliotheque-npm)
    
* [Comment vérifier et installer votre package](#heading-comment-comment-verifier-et-installer-votre-package)
    
* [Comment mettre à jour votre package](#heading-comment-mettre-a-jour-votre-package)
    
* [Notes et bonnes pratiques](#heading-notes-et-bonnes-pratiques)
    
* [Au-delà des bases](#heading-au-dela-des-bases)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que npm ?

npm, qui signifie Node Package Manager, est un outil en ligne de commande pour installer et gérer des packages JavaScript. C'est un écosystème qui alimente le développement JavaScript moderne ([Node.js](http://node.js), outils frontend, Frameworks, etc.). Les développeurs utilisent npm pour partager et emprunter des packages, et de nombreuses organisations utilisent npm pour gérer le développement privé.

Essentiellement, npm est à JavaScript ce que pip est à Python ou Maven à Java. Il permet aux développeurs de réutiliser du code écrit par d'autres (la plupart du temps pour remplir une fonction dans leur projet), de gérer les dépendances et de partager leur propre code avec le monde.

Vous pouvez utiliser npm pour :

* Obtenir et utiliser des packages de code dans vos applications, tels quels ou avec des modifications personnalisées.
    
* Télécharger et exécuter instantanément des outils autonomes.
    
* Exécuter des packages directement depuis le registre sans les installer en utilisant npx.
    
* Partager votre propre code avec des développeurs du monde entier via le registre npm.
    
* Limiter l'accès à des packages spécifiques afin que seuls les développeurs approuvés puissent les utiliser.
    
* Créer des organisations pour gérer le code, les équipes et les packages en un seul endroit.
    
* Collaborer en tant qu'équipes virtuelles en utilisant des comptes organisationnels partagés.
    
* Gérer facilement les différentes versions des packages et leurs dépendances.
    
* Maintenir vos applications à jour en vous synchronisant avec les dernières mises à jour de packages.
    
* Explorer différents packages offrant diverses solutions au même problème.
    
* Se connecter avec des développeurs travaillant sur des défis et des projets similaires.
    

## Composants de npm

npm se compose de trois éléments de base :

* L'interface de ligne de commande (CLI)
    
* Le registre
    
* Le site web
    

## L'interface de ligne de commande

Il existe différentes commandes npm que vous pouvez exécuter sur votre terminal. Par exemple, `npm init` peut être utilisé pour initialiser un projet Node, `npm install` peut être utilisé pour installer un package. Il vous permet également de faire des choses comme :

* Publier des packages (`npm publish`)
    
* Mettre à jour des packages (`npm update`)
    
* Gérer le versionnage (`npm version`)
    
* Exécuter des scripts (`npm run build`, `npm test`, etc.)
    

Considérez-le comme votre panneau de contrôle.

## Le registre

Vous pouvez trouver l'énorme base de données publique sur [https://registry.npmjs.org](https://registry.npmjs.org), où les packages sont stockés et partagés. Elle contient également toutes les méta-informations entourant le package.

Exemple, lorsque vous exécutez :

```bash
npm install express
```

npm récupère le package Express depuis le registre.

Le registre npm permet la collaboration en permettant aux développeurs de :

* Publier leurs propres packages
    
* Installer des packages créés par d'autres
    
* Découvrir de nouveaux outils et bibliothèques
    

Ses fonctionnalités de collaboration incluent :

* Packages open-source : Le code est publiquement visible (généralement hébergé sur GitHub).
    
* Versionnage : Plusieurs versions du même package permettent aux utilisateurs d'adopter les mises à jour en toute sécurité.
    
* Packages avec scope : Les espaces de noms permettent aux équipes et aux organisations de gérer la propriété.
    
* Issues & pull requests : La plupart des packages npm renvoient vers GitHub, permettant aux développeurs de contribuer aux corrections et aux améliorations.
    
* Organisations : Les équipes peuvent gérer l'accès aux packages partagés, qu'ils soient privés ou publics.
    

## Le site web

Sur [https://www.npmjs.com](https://www.npmjs.com), c'est là que vous pouvez :

* Parcourir les packages.
    
* Lire la documentation.
    
* Consulter les statistiques de téléchargement et les dépendances.
    
* Créer et gérer votre compte, votre organisation et l'accès aux packages.
    

## Qu'est-ce que le fichier package.json ?

Un composant très important de tout outil npm que vous rencontrerez en tant que développeur JavaScript installant un package npm est le fichier `package.json`. C'est un fichier de métadonnées qui réside à la racine de chaque projet npm ou Node. Il indique à npm (et aux autres outils) tout ce qu'il doit savoir sur votre projet, comme :

* Le nom du projet.
    
* Ses dépendances.
    
* Comment l'exécuter.
    
* Comment le versionner.
    
* Et comment le publier.
    

Vous pouvez le voir comme le plan directeur de votre projet JavaScript. Sans lui, npm ne sait pas comment travailler avec votre code.

Vous pouvez créer un fichier `package.json` en tapant la commande `npm init` dans votre terminal et en répondant aux questions posées. Alternativement, vous pouvez créer un fichier nommé `package.json` et le remplir manuellement avec du contenu JSON.

### Champs clés dans un fichier package.json npm

Voici une liste des champs couramment utilisés et comment ils interagissent avec npm :

1. `name` et `version`
    
    ```json
    "name": "mon-super-package",
    "version": "1.0.0"
    ```
    
    * Requis pour la publication.
        
    * `name` doit être unique (si vous publiez sur le registre public npm).
        
    * `version` suit le versionnage sémantique (semver) (par exemple, majeur.mineur.correctif).  
        
2. `description`, `keywords`, `author`, et `license`
    
    ```json
    "description": "Un utilitaire pour convertir le markdown en HTML",
    "keywords": ["markdown", "html", "convertisseur"],
    "author": "Ikegah Oliver",
    "license": "MIT"
    ```
    
    * Aide les utilisateurs de npm à découvrir votre package.
        
    * Apparaît sur [npmjs.com](http://npmjs.com).
        
    * Définit la licence de collaboration.
        
3. `scripts`
    
    ```json
    "scripts": {
      "start": "node index.js",
      "test": "jest",
      "build": "tsc"
    }
    ```
    
    * Définit des commandes personnalisées.
        
    * S'exécute avec npm run test, npm run build, etc.
        
    * Automatise les processus de build, test, lint, déploiement.
        
4. `main` et `exports`
    
    ```json
    "main": "dist/index.js",
    "exports": {
      ".": "./dist/index.js"
    }
    ```
    
    * `main` : Point d'entrée pour `require()` ou import.
        
    * `exports` : Contrôle précisément quelles parties de votre package sont exposées (particulièrement utile pour l'ESM moderne et la sécurité des packages).
        
5. `dependencies` et `devDependencies`
    
    ```json
    "dependencies": {
      "express": "^4.18.2"
    },
    "devDependencies": {
      "eslint": "^8.0.0",
      "jest": "^29.0.0"
    }
    ```
    
    * `dependencies` : Packages de base dont votre projet a besoin pour fonctionner en production (par exemple, `express`).
        
    * `devDependencies` : Packages utilisés uniquement pendant le développement, comme les outils de test ou de build (par exemple, `jest`).
        
6. `engines`
    
    ```json
    "engines": {
      "node": ">=14.0.0"
    }
    ```
    
    * Spécifie la version de Node.js supportée par votre package.
        
    * Aide à avertir les utilisateurs avant qu'ils ne l'installent avec une version non supportée.
        
7. `private`
    
    ```json
    "private":"true"
    ```
    
    * Empêche la publication accidentelle sur le registre public npm.
        
    * Utilisé pour les monorepos et les projets internes uniquement.
        
8. `files` (optionnel)
    
    ```json
    "files":["/dist", "README.md"]
    ```
    
    * Contrôle quels fichiers sont inclus lorsque vous exécutez npm publish.
        
    * Réduit la taille du package, omet les artefacts de build ou les fichiers de test.
        

Un fichier `package.json` npm minimal ressemble à ceci :

```json
{
  "name": "@oliver/markdown-to-html",
  "version": "1.0.0",
  "description": "Convertit le markdown en HTML avec des styles",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "test": "jest"
  },
  "keywords": ["markdown", "html", "convertisseur"],
  "author": "Ikegah Oliver",
  "license": "MIT",
  "dependencies": {
    "marked": "^5.0.0"
  },
  "devDependencies": {
    "jest": "^29.0.0"
  },
  "engines": {
    "node": ">=14.0.0"
  },
  "files": ["dist/", "README.md"]
}
```

Le fichier `package.json` joue un rôle central dans chaque flux de travail npm. Il définit l'identité de votre projet, liste ses dépendances, spécifie des scripts utiles et décrit comment le package doit se comporter lorsqu'il est publié. Sans lui, npm ne peut pas installer correctement les packages, exécuter des commandes ou publier votre code sur le registre.

## Comment fonctionne npm

Lorsque vous tapez `npm install` dans votre terminal, npm lance un processus en coulisses pour installer les packages nécessaires à votre projet. Selon la façon dont vous exécutez la commande, le processus varie légèrement comme suit :

### **Méthode 1** - `package.json` contient déjà des dépendances

Si votre `package.json` liste des packages sous `dependencies` ou `devDependencies`, npm va :

1. **Lire ces entrées :** Il examine les noms et les plages de versions de chaque dépendance.
    
2. **Contacter le registre :** npm interroge [https://registry.npmjs.org](https://registry.npmjs.org) pour récupérer les métadonnées de chaque package requis.
    
3. **Télécharger les bonnes versions :** Il sélectionne les versions qui correspondent à vos règles de version (telles que ^4.17.0) et télécharge les fichiers `.tgz`.
    
4. **Déballer et installer :** Il place les packages dans le répertoire `node_modules` et les met en cache.
    
5. **Mettre à jour package-lock.json :** Il enregistre les versions exactes et l'arborescence des dépendances dans ce fichier pour garantir des installations cohérentes ultérieurement.
    

### **Méthode 2** - Vous exécutez `npm install <nom-du-package>` sans dépendances existantes

Si votre `package.json` n'a pas encore de dépendances et que vous exécutez quelque chose comme ceci dans votre terminal :

```bash
npm install express
```

Alors npm va :

1. **Résoudre la version du package :** Il récupère la dernière version d'Express (sauf si vous spécifiez une version manuellement).
    
2. **Télécharger et installer :** Le tarball est téléchargé et placé dans le dossier `node_modules/` qui est automatiquement généré. Un tarball est la version compressée du package (`express` dans ce cas), contenant les fichiers JavaScript du package, un `package.json`, un README, et tout ce que l'auteur a inclus pour la distribution que npm télécharge et extrait sur votre machine.
    
3. **Ajouter au** `package.json` : npm ajoute automatiquement le package à votre liste de dépendances comme ceci :
    

```json
"dependencies": {
  "express": "^4.18.2"
}
```

4. **Créer un** `package-lock.json` **(s'il n'existe pas) :** Il écrit toutes les informations de version pour verrouiller les choses pour les futures installations.
    

Note : Si vous exécutez `npm install --save-dev jest`, il ajoutera le package sous devDependencies à la place.

## Comment publier une bibliothèque npm

Pour suivre cette section du guide, vous devrez disposer des prérequis suivants :

* Une connexion réseau stable
    
* Un éditeur de code avec un terminal (comme VSCode)
    
* Des connaissances de base en JavaScript et Node
    
* Une compréhension de base du langage de balisage Markdown (pour la documentation README)
    

Maintenant, plongeons dans la publication d'une bibliothèque npm. En supposant que vous venez de construire et de tester un outil JavaScript fantastique que vous aimeriez partager avec le monde, et permettre aux gens de l'utiliser dans leurs projets et applications, les étapes ci-dessous vous guideront de l'outil sur votre machine locale à sa mise à disposition publique en tant que package npm :

### Étape 1 : Créer un compte npm gratuit

Avant de publier, vous aurez besoin d'un compte npm.

* Allez sur [https://www.npmjs.com/signup](https://www.npmjs.com/signup).
    
* Remplissez le formulaire avec votre nom d'utilisateur, votre e-mail et votre mot de passe.
    
* Confirmez votre adresse e-mail en cliquant sur le lien dans l'e-mail de vérification.
    

### Étape 2 : Se connecter depuis la ligne de commande

Une fois votre compte créé, vous devez vous connecter via votre terminal. Exécutez :

```bash
npm login
```

npm vous demandera votre nom d'utilisateur, votre mot de passe et votre adresse e-mail. Si tout est correct, npm générera un jeton d'authentification et le stockera localement, afin que vous n'ayez pas à vous connecter à chaque fois.

### Étape 3 : Créer un fichier `package.json`

Si votre projet n'a pas encore de fichier `package.json`, créez-en un en tapant cette commande dans votre terminal :

```bash
npm init
```

Vous serez invité à remplir les informations suivantes :

* **name** : Doit être unique s'il est public.
    
* **version** : Commencez par 1.0.0 (cela représente la première version de votre projet ; par la suite, vous la modifierez en conséquence après chaque mise à jour).
    
* **description** : Résumé en une ligne de votre package.
    
* **entry point** : Fichier d'entrée de votre projet, généralement `index.js` ou `dist/index.js`.
    
* **keywords** : Aide les autres à découvrir votre package.
    
* **author** : Votre nom ou votre identifiant GitHub.
    
* **license** : Utilisez MIT, ISC ou une autre licence open-source.
    

Quand vous aurez terminé, npm générera un `package.json` comme celui-ci :

```json
{
  "name": "mon-super-package",
  "version": "1.0.0",
  "description": "Un package de démonstration pour la publication npm",
  "main": "index.js",
  "keywords": ["demo", "npm", "tutoriel"],
  "author": "Votre Nom",
  "license": "MIT"
}
```

### Étape 4 : Ajouter un [README.md](http://readme.md)

Expliquez ce que fait votre package et comment l'utiliser dans un fichier `README.md`. Le README apparaît sur la page de votre package sur [npmjs.com](http://npmjs.com). Exemple de contenu :

````markdown
# mon-super-package

Un package simple qui dit bonjour.

## Utilisation

```js
const greet = require('mon-super-package');
console.log(greet('Oliver'));
// Résultat : Hello, Oliver!
```
````

### Étape 5 : Ajouter un fichier .npmignore

Cela exclura des dossiers comme `node_modules`, `dist` ou `.env`, et tout autre fichier ou dossier au sein du package que vous ne souhaitez pas publier. Exemple de contenu :

```bash
node_modules
.env
dist
```

### Étape 6 : Vérifier si le nom de package choisi est disponible

Avant de publier, vérifiez que le nom de package que vous avez choisi n'est pas déjà pris. Pour vérifier, exécutez cette commande sur votre terminal :

```bash
npm search mon-super-package
```

Ou entrez l'URL [https://www.npmjs.com/package/mon-super-package](https://www.npmjs.com/package/mon-super-package) dans votre navigateur (remplacez mon-super-package par le nom que vous avez choisi). Si aucune page de package ne s'affiche, le nom n'est pas pris.

Si le nom du package est déjà pris, changez-le dans votre `package.json` et dans toute documentation (`README.md`), ou publiez-le sous un scope. Un scope est comme un espace de noms lié à votre nom d'utilisateur npm ou à votre organisation. Il garantit que le nom de votre package est unique, même si le nom de base est courant. Par exemple, si mon-super-package est pris, vous pouvez publier sous un scope en définissant la section name dans son `package.json` comme ceci :

```json
{
  "name": "@votrenom/mon-super-package"
}
```

### Étape 7 : Publier votre package

Vous êtes maintenant prêt à publier. Exécutez :

```bash
npm publish
```

Si vous avez utilisé un nom avec scope, lors de la publication, vous devez le rendre public :

```bash
npm publish --access public
```

Si tout est valide, npm publiera votre package et vous donnera une URL comme :

[https://www.npmjs.com/package/mon-super-package](https://www.npmjs.com/package/mon-super-package)

## Comment vérifier et installer votre package

Visitez la page de votre projet sur npm pour le voir en direct. Par exemple : [https://www.npmjs.com/package/mon-super-package](https://www.npmjs.com/package/mon-super-package), ou recherchez le nom de votre projet dans la barre de recherche du site npm.

Maintenant, essayez de l'installer dans un projet node :

```bash
npm install mon-super-package
```

Testez ses fonctionnalités, selon ce pour quoi il a été conçu.

## Comment mettre à jour votre package

Si vous apportez des modifications ou mettez à jour des fonctionnalités dans votre package, vous pouvez publier la mise à jour.

Après avoir appliqué vos modifications, vous pouvez mettre à jour la version dans votre `package.json`. En utilisant le versionnage sémantique, vous pouvez le mettre à jour comme suit :

* Mise à jour de correctif (patch) : 1.0.0 → 1.0.1
    
* Mise à jour mineure : 1.0.0 → 1.1.0
    
* Mise à jour majeure : 1.0.0 → 2.0.0
    

Ou vous pouvez utiliser la CLI :

```bash
npm version <type_de_mise_à_jour>
```

Remplacez `<type_de_mise_à_jour>` par votre nouvelle version sémantique.

Maintenant, exécutez :

```bash
npm publish
```

## Notes et bonnes pratiques

Bien que la publication sur npm soit simple, vous devez tout de même suivre les bonnes pratiques pour maintenir un package propre, sécurisé et convivial.

* Exclure les fichiers sensibles : N'incluez jamais de fichiers `.env`, d'identifiants ou de secrets. Utilisez `.npmignore` ou le champ "files" dans `package.json` pour contrôler ce qui est publié.
    
* Tester avant de publier : Exécutez `npm pack` pour prévisualiser le package et installez-le localement dans un autre projet pour vous assurer que tout fonctionne.
    
* Dépublier avec précaution : Vous pouvez dépublier dans les 72 heures en utilisant `npm unpublish --force`, mais évitez de le faire fréquemment pour ne pas casser d'autres projets qui dépendent de votre package.
    
* Toujours incrémenter la version : npm ne vous permettra pas d'écraser une version, utilisez donc le versionnage sémantique (npm version patch|minor|major) avant de publier des mises à jour.
    
* Ajouter l'essentiel : Incluez un fichier `README.md` clair, une licence et des mots-clés pertinents pour rendre votre package découvrable et facile à utiliser.
    

## Au-delà des bases

Maintenant que vous maîtrisez les bases, vous pouvez mettre vos compétences npm à profit et monter en niveau en tant que développeur. Voici quelques étapes simples et pratiques que vous pouvez suivre :

### S'impliquer dans l'Open Source

L'un des meilleurs moyens d'acquérir une expérience concrète est de contribuer à des projets existants sur npm. Consultez leurs dépôts sur GitHub et GitLab et voyez comment vous pouvez y contribuer. Cela vous apprend à collaborer, à gérer les revues de code et les versions. Un excellent moyen de commencer est de chercher des projets sur GitHub avec le label "good first issue".

### Maintenir votre propre package

La publication n'est que la première étape. Pour maîtriser véritablement le processus, maintenez votre package à jour. Cela implique de corriger les bugs, d'écouter les retours des utilisateurs et d'ajouter de nouvelles fonctionnalités. Vous apprendrez rapidement le versionnage, l'assurance que votre package reste compatible avec les projets plus anciens, et la gestion efficace des dépendances.

### Approfondir les fonctionnalités avancées

Explorez des sujets npm avancés comme le versionnage sémantique, l'utilisation de packages privés, la création de packages avec scope et l'automatisation de vos versions avec des pipelines CI/CD. Ce sont des compétences essentielles pour tout développeur professionnel.

Suivre ces étapes vous aidera à passer de la simple compréhension de npm à son utilisation confiante dans des scénarios réels.

## Conclusion

Félicitations ! Vous avez maintenant appris les bases de npm, du fichier `package.json` à la publication et à la maintenance d'un package JavaScript avec la bibliothèque npm. Grâce à ces connaissances, vous pouvez partager vos outils JavaScript avec le monde, collaborer avec d'autres développeurs et contribuer à l'écosystème croissant des bibliothèques open-source.

En suivant les bonnes pratiques, en testant localement et en apprenant des erreurs courantes, vous pouvez créer en toute confiance des packages propres, sécurisés et utiles pour d'autres développeurs. Que vous construisiez un petit utilitaire ou un Framework complet, la publication sur npm donne de la visibilité à vos idées et vous aide à contribuer à la communauté JavaScript au sens large.

Si vous souhaitez acquérir une expérience pratique en collaborant sur un vrai package, j'ai publié un projet npm appelé [route-pilot](https://www.npmjs.com/package/route-pilot?activeTab=readme), un outil CLI puissant pour tester et analyser les routes Express.js dans vos applications Node.js. Je recherche activement des contributeurs qui souhaitent améliorer le code, ajouter de nouvelles fonctionnalités ou affiner la documentation. C'est un moyen simple de s'entraîner à travailler avec npm dans un cadre collaboratif tout en en apprenant davantage sur le développement open-source. Rendez-vous sur le [dépôt GitHub](https://github.com/oliverTwist2/express-route-tester) et rejoignez-nous. Nous serions ravis de vous compter parmi nous !