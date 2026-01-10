---
title: Comment empêcher les erreurs avant qu'elles n'atteignent votre base de code
  avec Travis CI et ESLint
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-06-05T16:15:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-stop-errors-before-they-ever-hit-your-codebase-with-travis-ci-and-eslint-7a5a6b1fcd4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yu7AYHjvkRAdyXDuCvIugA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment empêcher les erreurs avant qu'elles n'atteignent votre base de
  code avec Travis CI et ESLint
seo_desc: 'A single misplaced comma in a single JSON file can wreck your app. But
  only if you let it.

  The best way to stop this from happening is to catch that error before it ever gets
  accepted into your codebase. That means tests. And for file formats like JS...'
---

Une simple virgule mal placée dans un fichier JSON peut ruiner votre application. Mais seulement si vous la laissez faire.

La meilleure façon d'empêcher cela est de détecter cette erreur avant qu'elle ne soit acceptée dans votre base de code. Cela signifie des tests. Et pour des formats de fichier comme JSON, cela signifie également le linting.

Je vais vous guider à travers la configuration de Travis CI et ESLint sur votre dépôt GitHub, afin que vous puissiez détecter les erreurs de linting dans les pull requests, avant qu'elles n'atteignent votre base de code.

Mais d'abord, un peu de contexte sur la façon dont j'ai appris à faire cela.

À l'école de médecine, ils ont un processus d'apprentissage appelé [voir un, faire un, enseigner un](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4785880/) :

* voir quelqu'un effectuer une opération
* effectuer cette opération vous-même
* enseigner à quelqu'un d'autre comment effectuer cette opération

Eh bien, j'ai configuré Travis CI + ESLint sur l'un de nos dépôts. Ensuite, [Eric Leung](https://github.com/erictleung) m'a demandé de le faire sur un autre dépôt. Et maintenant, je vous enseigne comment le faire.

Voir un, faire un, enseigner un.

Dans ce cas, [Eric Leung](https://github.com/erictleung) m'a demandé de configurer Travis CI afin que [Mark McEwan](https://github.com/mmcewan) puisse installer awesome_bot.

![Image](https://cdn-media-1.freecodecamp.org/images/nZBuN-97IQ6wVGdM6VpHuBtxXPprx-g03vZq)

Vous remarquerez qu'en bas de la pull request, GitHub a inclus une petite bannière nous encourageant à configurer l'intégration continue (CI) en utilisant leur nouveau Marketplace. C'est un endroit parfait pour commencer.

### Étape #1 : Installer Travis CI dans le GitHub Marketplace

![Image](https://cdn-media-1.freecodecamp.org/images/2sHSNwqj04BwUoJ2V3m7Vvve2okel0Sunj5q)

Travis CI est gratuit et open source. Vous pouvez donc simplement le choisir dans le menu et passer par le processus de checkout.

### Étape #2 : Créer une nouvelle branche

Si vous avez déjà [cloné le dépôt](https://help.github.com/articles/cloning-a-repository/) sur votre ordinateur local, vous pouvez créer une nouvelle branche en ouvrant le dépôt dans votre terminal et en tapant :

```
git checkout -b feature/add-travis
```

### Étape #3 : Créer un fichier .gitignore (si vous n'en avez pas déjà un)

Tapez ceci dans votre terminal :

```
touch .gitignore
```

Puis ouvrez le fichier .gitignore dans votre éditeur de code préféré et ajoutez la ligne suivante :

```
node_modules
```

Presto. Maintenant, vous n'allez pas commiter accidentellement des fichiers de packages npm dans votre dépôt.

### Étape #4 : Initialiser npm (si vous ne l'avez pas déjà fait)

Vous aurez besoin de npm pour ESLint. Dans votre terminal, exécutez :

```
npm init
```

Maintenant, vous devez répondre à beaucoup de questions. Si vous êtes pressé, vous pouvez répondre à celles-ci en appuyant plusieurs fois sur la touche Entrée pour accepter les réponses par défaut.

```
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (how-to-contribute-to-open-source) 
version: (1.0.0) 
description: 
entry point: (index.js) 
test command: 
git repository: (https://github.com/FreeCodeCamp/how-to-contribute-to-open-source.git) 
keywords: 
author: 
license: (ISC)
About to write to /Users/michaelq/web/how-to-contribute-to-open-source/package.json:

{
  "name": "how-to-contribute-to-open-source",
  "version": "1.0.0",
  "description": "This is a list of resources for people who are new to contributing to open source.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/FreeCodeCamp/how-to-contribute-to-open-source.git"
  },
  "author": "",
  "license": "BSD-3-Clause",
  "bugs": {
    "url": "https://github.com/FreeCodeCamp/how-to-contribute-to-open-source/issues"
  },
  "homepage": "https://github.com/FreeCodeCamp/how-to-contribute-to-open-source#readme"
}

Is this ok? (yes) 
```

Vous avez maintenant un fichier package.json dans votre dépôt.

### Étape #5 : Installer ESLint et vos packages de linting

Selon les types de fichiers dans votre dépôt, vous pouvez installer une variété de packages de linting différents. Le dépôt sur lequel je travaille est [How to Contribute to Open Source](https://github.com/freeCodeCamp/how-to-contribute-to-open-source) (donnez-lui un ⭐, ?).

Les seuls fichiers qu'il utilise actuellement sont des fichiers Markdown, mais nous ajouterons inévitablement du JSON à un moment donné. J'ai donc inclus les packages ESLint pour Markdown et JSON.

Voici la commande que j'ai exécutée dans mon terminal pour installer tout cela avec npm :

```
npm install --save-dev eslint eslint-plugin-json eslint-plugin-markdown
```

Notez que la partie `--save-dev` ajoutera ces packages au fichier package.json de votre dépôt.

### Étape #6 : Créer et configurer votre fichier .eslintrc

Dans votre terminal, tapez :

```
touch .eslintrc
```

Puis ouvrez-le avec votre éditeur de code préféré. Voici à quoi ressemble le mien pour JSON et Markdown :

```json
{
  "plugins": [
    "json",
    "markdown"
  ]
}
```

### Étape #7 : Créer et configurer votre fichier .travis.yml

Dans votre terminal, tapez :

```
touch .travis.yml
```

Puis ouvrez-le avec votre éditeur de code préféré. Voici à quoi ressemble le mien :

```yml
language: node_js

node_js:
  - '6'
  
before_install: if [[ `npm -v` != 3* ]]; then npm i -g npm@3; fi

cache:
  directories:
    - node_modules
    
sudo: false
```

### Étape #8 : Mettre à jour votre fichier package.json

Dans l'étape #4, votre commande `npm initialize` a créé un fichier package.json. En faisant cela, npm a ajouté la ligne suivante à l'objet `"scripts"` par défaut :

```
"echo \"Error: no test specified\" && exit 1"
```

Cette ligne fera échouer la construction de Travis CI. Remplaçons-la donc par quelque chose de plus significatif.

Voici à quoi ressemble mon fichier package.json après avoir remplacé cette ligne par trois nouveaux scripts :

```json
{
  "name": "how-to-contribute-to-open-source",
  "version": "1.0.0",
  "description": "This is a list of resources for people who are new to contributing to open source.",
  "main": "index.js",
  "dependencies": {},
  "devDependencies": {
    "eslint": "^3.19.0",
    "eslint-plugin-json": "^1.2.0",
    "eslint-plugin-markdown": "^1.0.0-beta.6"
  },
  "scripts": {
    "lint": "eslint . --ext .json --ext .md",
    "pretest": "npm run lint",
    "test": "echo \"No tests\""
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/FreeCodeCamp/how-to-contribute-to-open-source.git"
  },
  "author": "",
  "license": "BSD-3-Clause",
  "bugs": {
    "url": "https://github.com/FreeCodeCamp/how-to-contribute-to-open-source/issues"
  },
  "homepage": "https://github.com/FreeCodeCamp/how-to-contribute-to-open-source#readme"
}
```

Notez qu'il existe deux façons pour Travis CI d'exécuter des tests. Par défaut, il utilise `npm test`. Mais l'autre façon est de l'utiliser dans le fichier `package.json`. Vous pouvez en lire plus à ce sujet [ici](https://docs.travis-ci.com/user/languages/javascript-with-nodejs/#Default-Test-Script).

Notez également que dans votre fichier `package.json`, vous pouvez définir des scripts que vous voulez que npm exécute en premier avant d'exécuter d'autres scripts en ajoutant un nouveau script avec le préfixe `pre`, comme nous l'avons fait ici avec `pretest`, qui s'exécute avant `test`.

### Étape #9 : Stage, commit, puis push

Dans votre terminal, stagez vos nouveaux fichiers :

```
git add .gitignore
git add .travis.yml
git add .eslintrc
git add package.json
```

Et commitez :

```
git commit -m "add and configure Travis CI and ESLint"
```

Puis poussez vers votre propre branche du dépôt sur GitHub.

```
git push origin feature/add-travis
```

### Étape #10 : Ouvrir une pull request dans l'interface utilisateur de GitHub

GitHub a une fonctionnalité sympa où il détecte votre push récent et propose de vous aider à créer la pull request. Naviguez vers le dépôt sur GitHub et passez par son workflow de pull request.

![Image](https://cdn-media-1.freecodecamp.org/images/781mDkV8y9H9JQqR5k7kvxSC0IIpZi4JBLi7)

### Étape #11 : Vérifier que la build a réussi

OK — le moment de vérité !

Sur votre pull request, Travis CI devrait immédiatement se mettre au travail. S'il échoue, il vous enverra un email pour vous le dire :

![Image](https://cdn-media-1.freecodecamp.org/images/tV3Jbc3WF4vwwOupUMgelisoorVe3BGv9gax)

Vous pouvez consulter le log et essayer de comprendre pourquoi il a échoué.

Une fois que vous l'aurez corrigé, il vous enverra un autre email comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vslpqCV1yLwtm7fOmO7HJ8roI5KVmXcVvEUt)

Et l'interface de la pull request ressemblera à quelque chose comme ceci — indiquant que tous vos tests et processus ESLint ont réussi.

![Image](https://cdn-media-1.freecodecamp.org/images/Vjw6Z4D7NiHKnO1qrpDLSFQkr1FCvq0Ar42H)

### Étape #12 : Fête !

Si vous avez suivi à la maison, félicitations ! Prenez une boisson de votre choix et tapez-vous sur l'épaule. Vous serez maintenant en mesure de détecter les erreurs de linting dans les pull requests avant de les fusionner. Et toute votre équipe pourra se reposer un peu plus facilement.

À partir de là, vous pouvez continuer à ajouter progressivement plus de tests, et Travis CI sera toujours prêt, prêt à exécuter fidèlement ces tests pour vous. C'est la puissance de l'open source !

Merci d'avoir lu, et bon codage !

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps.**