---
title: Qu'est-ce que npm ? Un tutoriel sur le gestionnaire de paquets Node pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-16T16:50:53.000Z'
originalURL: https://freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/cover-4.png
tags:
- name: node
  slug: node
- name: npm
  slug: npm
seo_title: Qu'est-ce que npm ? Un tutoriel sur le gestionnaire de paquets Node pour
  débutants
seo_desc: 'By Stanley Nguyen

  This article should serve as an all-in-one essential guide for Node.js'' favorite
  sidekick: npm.

  Node.js has been taking the world by storm since 2009. Hundreds of thousands of
  systems have been built using Node.js, prompting the dev...'
---

Par Stanley Nguyen

Cet article devrait servir de guide essentiel tout-en-un pour le fidèle compagnon de Node.js : npm.

Node.js a pris le monde d'assaut depuis 2009. Des centaines de milliers de systèmes ont été construits en utilisant Node.js, incitant la communauté des développeurs à affirmer que "JavaScript est en train de dévorer le logiciel".

L'un des principaux facteurs du succès de Node est npm - son gestionnaire de paquets populaire, qui permet aux développeurs JavaScript de partager des paquets utiles comme [lodash](https://www.npmjs.com/package/lodash) et [moment](https://www.npmjs.com/package/moment) rapidement et facilement.

Au moment où j'écris cet article, npm a facilité la publication de plus de 1,3 million de paquets avec un taux de téléchargement hebdomadaire de plus de 16 milliards ! Ces chiffres sont fantastiques pour tout outil logiciel. Alors maintenant, parlons de ce qu'est exactement npm.

## Qu'est-ce que NPM ?

NPM – ou "Node Package Manager" – est le gestionnaire de paquets par défaut pour l'environnement d'exécution JavaScript Node.js.

Il est également connu sous le nom de "Ninja Pumpkin Mutants", "Nonprofit Pizza Makers", et une multitude d'autres noms aléatoires que vous pouvez explorer et probablement contribuer sur [npm-expansions](https://github.com/npm/npm-expansions).

NPM se compose de deux parties principales :

* un outil CLI (interface en ligne de commande) pour publier et télécharger des paquets, et
* un [dépôt en ligne](https://www.npmjs.com/) qui héberge les paquets JavaScript

Pour une explication plus visuelle, nous pouvons considérer le dépôt [npmjs.com](https://npmjs.com) comme un centre de distribution qui reçoit des paquets de marchandises de la part des vendeurs (auteurs de paquets npm) et distribue ces marchandises aux acheteurs (utilisateurs de paquets npm).

Pour faciliter ce processus, le centre de distribution [npmjs.com](https://npmjs.com) emploie une armée de wombats travailleuses (npm CLI) qui seront assignées comme assistantes personnelles à chaque client individuel de [npmjs.com](https://npmjs.com). Ainsi, les dépendances sont livrées aux développeurs JavaScript comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/wombat-install.png)

et le processus de publication d'un paquet pour vos collègues JS serait quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/wombat-publish.png)

Voyons comment cette armée de wombats aide les développeurs qui souhaitent utiliser des paquets JavaScript dans leurs projets. Nous verrons également comment ils aident les sorciers du logiciel libre à diffuser leurs bibliothèques dans le monde.

## package.json

Chaque projet en JavaScript – qu'il s'agisse de Node.js ou d'une application navigateur – peut être défini comme un paquet npm avec ses propres informations de paquet et son fichier `package.json` pour décrire le projet.

Nous pouvons considérer `package.json` comme des étiquettes estampillées sur ces boîtes de marchandises npm que notre armée de Wombats livre partout.

`package.json` sera généré lorsque `npm init` est exécuté pour initialiser un projet JavaScript/Node.js, avec ces métadonnées de base fournies par les développeurs :

* `name` : le nom de votre bibliothèque/projet JavaScript
* `version` : la version de votre projet. Souvent, pour le développement d'applications, ce champ est souvent négligé car il n'y a pas de besoin apparent de versionner les bibliothèques open source. Mais il peut toujours être utile comme source de la version du déploiement.
* `description` : la description du projet
* `license` : la licence du projet

### scripts npm

`package.json` prend également en charge une propriété `scripts` qui peut être définie pour exécuter des outils en ligne de commande installés dans le contexte local du projet. Par exemple, la partie `scripts` d'un projet npm peut ressembler à ceci :

```json
{
  "scripts": {
    "build": "tsc",
    "format": "prettier --write **/*.ts",
    "format-check": "prettier --check **/*.ts",
    "lint": "eslint src/**/*.ts",
    "pack": "ncc build",
    "test": "jest",
    "all": "npm run build && npm run format && npm run lint && npm run pack && npm test"
  }
}

```

avec `eslint`, `prettier`, `ncc`, `jest` non nécessairement installés comme exécutables globaux mais plutôt comme locaux à votre projet dans `node_modules/.bin/`.

L'introduction récente de [npx](https://www.freecodecamp.org/news/npm-vs-npx-whats-the-difference/) nous permet d'exécuter ces commandes spécifiques au projet `node_modules` comme un programme installé globalement en préfixant `npx ...` (c'est-à-dire `npx prettier --write **/*.ts`).

### dependencies vs devDependencies

Ces deux éléments se présentent sous la forme d'objets clé-valeur avec les noms des bibliothèques npm comme clé et leurs versions formatées [semantically](https://semver.org/) comme valeur. Voici un exemple du [modèle TypeScript Action de Github](https://github.com/actions/typescript-action) :

```json
{
  "dependencies": {
    "@actions/core": "^1.2.3",
    "@actions/github": "^2.1.1"
  },
  "devDependencies": {
    "@types/jest": "^25.1.4",
    "@types/node": "^13.9.0",
    "@typescript-eslint/parser": "^2.22.0",
    "@zeit/ncc": "^0.21.1",
    "eslint": "^6.8.0",
    "eslint-plugin-github": "^3.4.1",
    "eslint-plugin-jest": "^23.8.2",
    "jest": "^25.1.0",
    "jest-circus": "^25.1.0",
    "js-yaml": "^3.13.1",
    "prettier": "^1.19.1",
    "ts-jest": "^25.2.1",
    "typescript": "^3.8.3"
  }
}

```

Ces dépendances sont installées via la commande `npm install` avec les indicateurs `--save` et `--save-dev`. Elles sont destinées à être utilisées pour les environnements de production et de développement/test, respectivement. Nous approfondirons l'installation de ces paquets dans la section suivante.

Entre-temps, il est important de comprendre les signes possibles qui précèdent les versions sémantiques (en supposant que vous avez lu le modèle `major.minor.patch` de [semver](https://semver.org/)) :

* `^` : dernière version mineure. Par exemple, une spécification `^1.0.4` pourrait installer la version `1.3.0` si c'est la dernière version mineure de la série majeure `1`.
* `~` : dernière version de correctif. De la même manière que `^` pour les versions mineures, une spécification `~1.0.4` pourrait installer la version `1.0.7` si c'est la dernière version mineure de la série mineure `1.0`.

Toutes ces versions exactes des paquets seront documentées dans un fichier généré `package-lock.json`.

### package-lock.json

Ce fichier décrit les versions exactes des dépendances utilisées dans un projet JavaScript npm. Si `package.json` est une étiquette descriptive générique, `package-lock.json` est une table des ingrédients.

Et tout comme nous ne lisons généralement pas la table des ingrédients d'un produit (sauf si vous êtes trop ennuyé ou avez besoin de savoir), `package-lock.json` n'est pas destiné à être lu ligne par ligne par les développeurs (sauf si nous sommes désespérés de résoudre les problèmes "ça marche sur ma machine").

`package-lock.json` est généralement généré par la commande `npm install`, et est également lu par notre outil CLI NPM pour garantir la reproduction des environnements de construction pour le projet avec `npm ci`.

## Comment commander efficacement les Wombats NPM en tant qu'"acheteur"

Comme on peut le déduire des 1,3 million de paquets publiés contre 16 milliards de téléchargements mentionnés précédemment, la majorité des utilisateurs de npm utilisent npm dans cette direction. Il est donc bon de savoir comment utiliser cet outil puissant.

### npm install

Il s'agit de la commande la plus couramment utilisée lors du développement d'applications JavaScript/Node.js de nos jours.

Par défaut, `npm install <package-name>` installera la dernière version d'un paquet avec le signe de version `^`. Une commande `npm install` dans le contexte d'un projet npm téléchargera les paquets dans le dossier `node_modules` du projet selon les spécifications de `package.json`, mettant à niveau la version du paquet (et régénérant en conséquence `package-lock.json`) chaque fois que possible en fonction de la correspondance des versions `^` et `~`.

Vous pouvez spécifier un indicateur global `-g` si vous souhaitez installer un paquet dans le contexte global que vous pouvez utiliser partout sur votre machine (ceci est courant pour les paquets d'outils en ligne de commande comme [live-server](https://github.com/tapio/live-server)).

npm a rendu l'installation des paquets JavaScript si facile que cette commande est souvent utilisée incorrectement. Cela fait de npm la cible de nombreuses blagues de programmeurs comme celles-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/npm-jokes.png)

C'est là que l'indicateur `--production` vient à la rescousse ! Dans la section précédente, nous avons discuté des `dependencies` et `devDependencies` destinées à être utilisées en production et en environnement de développement/test, respectivement. Cet indicateur `--production` est ce qui fait la différence dans `node_modules`.

En attachant cet indicateur à la commande `npm install`, nous n'installerons que les paquets de `dependencies`, réduisant ainsi considérablement la taille de notre `node_modules` à ce qui est absolument nécessaire pour que nos applications soient opérationnelles.

Tout comme en tant que scouts, nous n'apportions pas de presse-agrumes à notre stand de limonade, nous ne devrions pas apporter de `devDependencies` en production !

### npm ci

Donc, si `npm install --production` est optimal pour un environnement de production, doit-il y avoir une commande qui est optimale pour mon environnement de développement local et de test ?

La réponse est `npm ci`.

Tout comme si `package-lock.json` n'existe pas déjà dans le projet, il est généré chaque fois que `npm install` est appelé, `npm ci` utilise ce fichier pour télécharger la version exacte de chaque paquet individuel dont le projet dépend.

C'est ainsi que nous pouvons nous assurer que le contexte de notre projet reste exactement le même sur différentes machines, qu'il s'agisse de nos ordinateurs portables utilisés pour le développement ou des environnements de construction CI (Intégration Continue) comme Github Actions.

### npm audit

Avec le nombre énorme de paquets qui ont été publiés et peuvent être facilement installés, les paquets npm sont susceptibles d'être la cible d'auteurs malveillants avec des intentions malveillantes comme [celles-ci](https://medium.com/@jsoverson/how-two-malicious-npm-packages-targeted-sabotaged-one-other-fed7199099c8).

Réalisant qu'il y avait un problème dans l'écosystème, l'organisation npm.js a eu l'idée de [npm audit](https://blog.npmjs.org/post/173719309445/npm-audit-identify-and-fix-insecure). Ils maintiennent une liste de failles de sécurité que les développeurs peuvent auditer leurs dépendances contre en utilisant la commande `npm audit`.

`npm audit` donne aux développeurs des informations sur les vulnérabilités et s'il existe des versions avec des correctifs pour les corriger. Par exemple,

![Image](https://www.freecodecamp.org/news/content/images/2020/06/npm-audit-result.png)

Si les correctifs sont disponibles dans les prochaines versions non critiques, `npm audit fix` peut être utilisé pour mettre à niveau automatiquement les versions des dépendances affectées.

## Comment commander efficacement les Wombats NPM en tant que "vendeur"

Nous avons vu comment utiliser l'outil CLI NPM en tant que consommateur, mais qu'en est-il de son utilisation efficace en tant qu'auteur (et potentiellement devenir un sorcier du logiciel libre JavaScript ?).

### npm publish

Envoyer un paquet à notre centre de distribution [npmjs.com](https://npmjs.com) est super facile car nous devons simplement exécuter `npm publish`. La partie délicate, qui n'est **pas** spécifique aux auteurs de paquets npm, est de déterminer la version du paquet.

La règle d'or selon [semver.org](https://semver.org) :

1. Version MAJEURE lorsque vous apportez des modifications incompatibles à l'API,
2. Version MINEURE lorsque vous ajoutez des fonctionnalités de manière rétrocompatible, et
3. Version PATCH lorsque vous apportez des corrections de bugs rétrocompatibles.

Il est encore plus important de suivre la règle ci-dessus lors de la publication de vos paquets pour vous assurer que vous ne cassez le code de personne, car la correspondance de version par défaut dans npm est `^` (aka la prochaine version mineure).

## ❤️ npm ❤️ JavaScript ❤️ Node.js ❤️

C'est tout ce que nous devons savoir pour commencer à utiliser npm efficacement et commander notre adorable armée de wombats !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/wombats.png)