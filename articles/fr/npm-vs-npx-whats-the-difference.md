---
title: npm vs npx — Quelle est la différence ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T19:02:15.000Z'
originalURL: https://freecodecamp.org/news/npm-vs-npx-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/npm-vs-npx-whats-the-difference-1024x538.jpg
tags:
- name: npm
  slug: npm
seo_title: npm vs npx — Quelle est la différence ?
seo_desc: 'By Carol-Theodor Pelu

  If you’ve ever used Node.js, then you must have used npm for sure.

  npm (node package manager) is the dependency/package manager you get out of the
  box when you install Node.js. It provides a way for developers to install package...'
---

Par Carol-Theodor Pelu

Si vous avez déjà utilisé [Node.js](https://nodejs.org/), alors vous avez certainement utilisé _npm_.

**npm** (node package manager) est le gestionnaire de dépendances/packages que vous obtenez dès l'installation de Node.js. Il fournit un moyen pour les développeurs d'installer des packages à la fois globalement et localement.

Parfois, vous pourriez vouloir examiner un package spécifique et essayer quelques commandes. Mais vous ne pouvez pas faire cela sans installer les dépendances dans votre dossier local `node_modules`.

C'est là que **npx** entre en jeu.

Dans cet article, nous allons examiner les différences entre **npm** et **npx** et apprendre à tirer le meilleur parti des deux.

Tout d'abord, comprenons ce qu'est réellement npm et ce que nous pouvons faire avec.

Vous voulez regarder une vidéo pour compléter votre lecture ? Jetez un œil à ceci :

%[https://www.youtube.com/watch?v=fSHWc8RTJug]

## npm le gestionnaire de packages

npm est plusieurs choses. Tout d'abord, c'est un dépôt en ligne pour la publication de projets Node.js open-source.

Ensuite, c'est un outil CLI qui vous aide à installer ces packages et à gérer leurs versions et dépendances. Il existe des centaines de milliers de bibliothèques et d'applications Node.js sur npm, et beaucoup plus sont ajoutées chaque jour.

npm en lui-même n'exécute aucun package. Si vous voulez exécuter un package en utilisant npm, vous devez spécifier ce package dans votre fichier `package.json`.

Lorsque des exécutables sont installés via des packages npm, npm crée des liens vers eux :

* les installations **locales** ont des liens créés dans le répertoire `./node_modules/.bin/`
* les installations **globales** ont des liens créés à partir du répertoire global `bin/` (par exemple : `/usr/local/bin` sur Linux ou `%AppData%/npm` sur Windows)

Pour exécuter un package avec npm, vous devez soit taper le chemin local, comme ceci :

```bash
$ ./node_modules/.bin/your-package
```

soit vous pouvez exécuter un package installé localement en l'ajoutant dans votre fichier `package.json` dans la section scripts, comme ceci :

```js
{
  "name": "your-application",
  "version": "1.0.0",
  "scripts": {
    "your-package": "your-package"
  }
}
```

Ensuite, vous pouvez exécuter le script en utilisant `npm run` :

```bash
npm run your-package
```

Vous pouvez voir que l'exécution d'un package avec npm seul nécessite un certain cérémonial.

Heureusement, c'est là que **npx** devient pratique.

## npx l'exécuteur de packages

Depuis la version npm [5.2.0](https://github.com/npm/npm/releases/tag/v5.2.0), npx est pré-empaqueté avec npm. Donc, c'est pratiquement une norme de nos jours.

**npx** est également un outil CLI dont le but est de faciliter l'installation et la gestion des dépendances hébergées dans le registre npm.

Il est maintenant très facile d'exécuter tout type d'exécutable basé sur Node.js que vous installeriez normalement via npm.

Vous pouvez exécuter la commande suivante pour voir si elle est déjà installée pour votre version actuelle de npm :

```bash
$ which npx
```

Si ce n'est pas le cas, vous pouvez l'installer comme ceci :

```bash
$ npm install -g npx
```

Une fois que vous vous êtes assuré de l'avoir installé, voyons quelques cas d'utilisation qui rendent **npx** extrêmement utile.

### Exécuter un package installé localement facilement

Si vous souhaitez exécuter un package installé localement, tout ce que vous avez à faire est de taper :

```bash
$ npx your-package
```

npx vérifiera si `<command>` ou `<package>` existe dans `$PATH`, ou dans les binaires du projet local, et si c'est le cas, il l'exécutera.

### Exécuter des packages non installés précédemment

Un autre avantage majeur est la possibilité d'exécuter un package qui n'a pas été installé précédemment.

Testons cela en exécutant :

```bash
$ npx cowsay wow	
```

![](https://i2.wp.com/neutrondev.com/wp-content/uploads/2020/01/npx-cowsay-wow-npm-vs-npx.jpg)

C'est génial car parfois vous voulez simplement utiliser certains outils CLI mais vous ne voulez pas les installer globalement juste pour les tester.

Cela signifie que vous pouvez économiser de l'espace disque et simplement les exécuter uniquement lorsque vous en avez besoin. Cela signifie également que vos variables globales seront moins polluées.

### Exécuter du code directement depuis GitHub

![execute-gist-script-with-npx](https://www.freecodecamp.org/news/content/images/2020/01/execute-gist-scripts-with-npx.jpg)

Celui-ci est assez génial.

Vous pouvez utiliser npx pour exécuter n'importe quel gist ou dépôt GitHub. Concentrons-nous sur l'exécution d'un gist GitHub car il est plus facile à créer.

Le script le plus basique se compose du fichier JS principal et d'un `package.json`. Après avoir configuré les fichiers, tout ce que vous avez à faire est d'exécuter npx avec le lien vers ce gist comme montré dans l'image ci-dessus.

[Ici](https://gist.github.com/Tynael/0861d31ea17796c9a5b4a0162eb3c1e8), vous pouvez trouver le code que j'ai utilisé pour cet exemple.

**Assurez-vous de lire attentivement tout script avant de l'exécuter pour éviter de sérieux problèmes qui peuvent survenir en raison de code malveillant.**

### Tester différentes versions de packages

npx rend extrêmement facile le test de différentes versions d'un package ou module Node.js. Pour tester cette fonctionnalité géniale, nous allons installer localement le package `create-react-app` et tester une version à venir.

Cela listera quelques balises de distribution vers la fin de la sortie. Les balises de distribution fournissent des alias pour les numéros de version, ce qui facilite grandement la saisie.

```bash
$ npm v create-react-app
```

![create-react-app-dist-tags](https://www.freecodecamp.org/news/content/images/2020/01/create-react-app-dist-tags.jpg)

Utilisons npx pour essayer la balise de distribution `next` de `create-react-app` qui créera l'application dans un répertoire sandbox.

```bash
$ npx create-react-app@next sandbox
```

npx installera temporairement la version suivante de `create-react-app`, puis il l'exécutera pour échafauder l'application et installer ses dépendances.

Une fois installé, nous pouvons naviguer vers l'application comme ceci :

```bash
$ cd sandbox
```

et ensuite la démarrer avec cette commande :

```bash
$ npm start
```

![create-react-app-npx-next-version](https://www.freecodecamp.org/news/content/images/2020/01/create-react-app-npx-next-version.jpg)

Il ouvrira automatiquement l'application React dans votre fenêtre de navigateur par défaut.
Maintenant, nous avons une application qui fonctionne sur la version suivante du package `create-react-app` !

![index-page-react-app](https://www.freecodecamp.org/news/content/images/2020/01/react-app.jpg)
_C'est ainsi que la page d'index de votre application React devrait ressembler._

## Conclusion

npx nous aide à éviter les problèmes de versionnement, de dépendances et d'installation de packages inutiles que nous voulons simplement essayer.

Il fournit également un moyen clair et facile d'exécuter des packages, des commandes, des modules et même des gists et des dépôts GitHub.

Si vous n'avez pas utilisé npx auparavant, maintenant c'est un bon moment pour commencer !

Ceci a été initialement publié sur [mon blog](https://neutrondev.com/npm-vs-npx-whats-the-difference/).
Vous pouvez me contacter et me poser des questions sur [Twitter](https://twitter.com/pelu_carol) et [Facebook](https://www.facebook.com/neutrondevcom).