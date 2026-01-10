---
title: Comment mettre à niveau de Node 16 et Jest 26 tout en restant sur React Scripts
  4
subtitle: ''
author: Harsh Deep
co_authors: []
series: null
date: '2024-07-10T19:35:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-upgrade-node-and-jest-while-on-react-scripts-v4
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/image0.png
tags:
- name: Jest
  slug: jest
- name: Node.js
  slug: nodejs
- name: React
  slug: react
seo_title: Comment mettre à niveau de Node 16 et Jest 26 tout en restant sur React
  Scripts 4
seo_desc: Recently, I was trying to upgrade some of my open source projects. They
  were made using create-react-app around 2019, and I wanted to upgrade to a newer
  version of NodeJS and Jest. This would let me take advantage of the security updates,
  bug fixes, ...
---

Récemment, j'ai essayé de mettre à niveau certains de mes projets open source [projets](https://github.com/classtranscribe/FrontEnd/). Ils ont été créés en utilisant [create-react-app](https://github.com/facebook/create-react-app) vers 2019, et je voulais passer à une version plus récente de NodeJS et Jest. Cela me permettrait de bénéficier des mises à jour de sécurité, des corrections de bugs, des améliorations de vitesse et des nouvelles fonctionnalités que l'écosystème a développées depuis. 

Malheureusement, ce n'était pas aussi simple que de lancer `$ nvm use 18` et de naviguer vers le coucher de soleil. Heureusement, si vous suivez toutes les étapes appropriées, vous franchirez de nombreux obstacles significatifs et réussirez la mise à niveau. Dans ce guide, je partagerai toutes les connaissances que j'aurais aimé avoir avant de commencer le processus. L'objectif est de faire fonctionner votre application React avec Node 18+ et Jest 29+ sans effectuer la mise à niveau périlleuse vers React Scripts 5.

Si vous pouvez passer à React Scripts 5 (ce qui est impraticable pour la plupart des applications réelles), je recommande vivement cette voie. En effet, la dernière version de CRA corrige de nombreux problèmes avec les anciennes dépendances, comme l'enveloppe `MD4` ou les formes de retour Babel `process()`, que nous aborderons manuellement dans ce tutoriel. Si vous pouvez passer à la v5, les versions de Node 18+ devraient fonctionner directement.

Malheureusement, le passage à React Scripts 5 introduit de nombreux changements majeurs, principalement dus à la mise à niveau vers Webpack 5. Bien que de nombreuses petites applications de niveau tutoriel puissent être mises à niveau assez facilement, toute application réelle fait face à un parcours difficile pour la mise à niveau. 

Si l'approche de mise à niveau vers React Scripts 5 ne fonctionne pas pour vous, vous pouvez suivre ce que j'ai écrit ci-dessous pour faire fonctionner la mise à niveau de Node tout en restant sur React Scripts 4. À la fin de cette page, j'ai écrit une petite note sur mon parcours en essayant la mise à niveau `v5`.

Le parcours de mise à niveau de chacun variera, surtout en considérant le Jenga des dépendances `npm` et le manque relatif de maintenance des React Scripts de Create React App ces dernières années.

Ce sont les étapes de la mise à niveau que j'ai essayées avec quelques applications React différentes, mais vous pourriez rencontrer des problèmes que je n'ai pas rencontrés moi-même. Google est votre meilleur ami dans ces cas, et il vous mènera souvent à Stackoverflow, aux problèmes GitHub, à d'autres tutoriels, et peut-être même au code source. N'ayez pas peur ; vous pourrez le comprendre ! 

Note : Dans ce tutoriel, je ferai référence à Create React App comme CRA. React Scripts est le nom du package installé qui abstrait toute la configuration créée par la commande Create React App, et dans la plupart des cas, vous verrez les ressources en ligne utiliser les deux de manière interchangeable.

## Table des matières

1. [Prérequis](#heading-prerequisites)
2. [Comment valider chaque étape](#heading-how-to-validate-every-step)
3. [Comment passer à React Scripts v4.0.3](#heading-how-to-bump-to-react-scripts-v403)
4. [Comment passer à la version Node 18](#heading-how-to-bump-node-version-to-18)  
– [Comprendre le problème MD4](#heading-understanding-the-md4-issue)
5. [Comment éjecter de React Scripts](#heading-how-to-eject-out-of-react-scripts)  
– [Comment ajouter des ignores de linter pour les fichiers éjectés](#heading-how-to-add-linter-ignores-for-ejected-files)  
– [Comment mettre à jour votre Dockerfile et autres processus de build avec les dossiers éjectés](#heading-how-to-update-your-dockerfile-and-other-build-processes-with-the-ejected-folders-1)  
– [Comment corriger les chemins absolus pour Jest](#heading-how-to-fix-absolute-paths-for-jest)  
– [Comment mettre à jour votre Dockerfile et autres processus de build avec les dossiers éjectés](#heading-how-to-update-your-dockerfile-and-other-build-processes-with-the-ejected-folders-1)
6. [Comment remplacer Webpack MD4 par SHA256](#heading-how-to-override-webpack-md4-to-sha256)
7. [Comment mettre à niveau vers la dernière version de Jest](#heading-how-to-upgrade-to-the-latest-version-of-jest)  
– [Comment passer à Jest 28](#heading-how-to-bump-to-jest-28)  
– [Comment définir explicitement jsdom comme environnement de test](#heading-how-to-explicitly-set-jsdom-as-the-test-environment)  
– [Comment corriger le type de retour du transformateur pour process() et processAsync()](#heading-how-to-fix-transformer-return-type-for-process-and-processasync)  
– [Comment passer à Jest 29](#heading-how-to-bump-jest-to-29)
8. [Jusqu'où devrais-je mettre à niveau NodeJS ?](#heading-how-far-should-i-upgrade-nodejs)
9. [Devriez-vous toujours utiliser Create React Scripts ? Quelles sont les alternatives ?](#heading-should-you-still-use-create-react-scripts-what-alternatives-are-there)
10. [Conclusion](#heading-conclusion)
11. [Alternativement : Comment mettre à niveau vers React Scripts 5.0.1](#heading-alternatively-how-to-upgrade-to-react-scripts-501)

## Prérequis

Pour suivre ce guide, vous devriez avoir une application React qui est :

* créée avec `create-react-app` v4 ou mise à niveau pour utiliser `react-scripts` v4. J'ai testé ce tutoriel sur les deux scénarios.
* en cours d'exécution sur Node 16

Si vous utilisez NodeJS en dessous de la version 16, je vous recommande vivement de passer à la version 16. Le chemin de mise à niveau vers la version 16 n'est pas trop mauvais, mais le passage de la version 16 à la version 18 crée des problèmes de rupture avec les paramètres par défaut de CRA 4. 

Notre application utilisait également `jest` (v26), le framework de test le plus courant dans React et fourni par défaut dans CRA v4. Si vous n'utilisez pas Jest, vous pouvez alors sauter les étapes qui lui sont pertinentes.

Nous utilisions également `yarn`, mais le processus devrait être identique avec une syntaxe différente si vous utilisez un autre gestionnaire de paquets comme `npm`.

Idéalement, vous avez une certaine couverture de cas de test pour vous assurer que les choses ne se cassent pas entre les versions, il est donc bien de prendre le temps d'écrire quelques tests d'intégration et unitaires larges avant toute mise à niveau.

Je recommande d'utiliser le contrôle de version comme `git` pour chaque étape tout en travaillant sur une branche. J'ai recommencé trois fois différentes en utilisant différentes stratégies de mise à niveau jusqu'à ce que j'ai quelque chose qui fonctionnait. Voici une rapide [introduction](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) aux branches `git` si vous n'êtes pas familier avec elles.

Je recommande également d'utiliser [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager) pour changer rapidement de versions. Vous n'êtes pas obligé de l'utiliser, et il existe de nombreuses autres alternatives pour gérer les versions, mais cela rend le changement très facile avec juste `nvm use`. J'utiliserai la syntaxe `nvm` dans ce tutoriel, mais cela devrait être assez similaire pour votre outil.

## Comment valider chaque étape

Tout au long du tutoriel, pour vous assurer que tout fonctionne toujours, vous exécuterez les commandes suivantes :

* `$ yarn build` – Construction de bout en bout pour détecter de nombreux problèmes au niveau des bibliothèques
* `$ yarn test` – Tests de régression pour détecter les ruptures de fonctionnalité
* `$ yarn start` – Les scripts de démarrage pour détecter de nombreux bugs d'initialisation.

Si vous avez d'autres étapes de validation (constructions CI, Docker, environnements de staging, tests de fumée), assurez-vous qu'elles fonctionnent déjà et utilisez-les tout au long du processus pour valider que la mise à niveau a fonctionné correctement. Pour le reste du tutoriel, je ferai référence à ces commandes de validation.

Avant de commencer la mise à niveau, assurez-vous que toutes les étapes de validation fonctionnent sur votre Node 16 actuel et CRA 4. À la fin du tutoriel, toutes ces étapes de validation devraient également fonctionner. En fin de compte, assurez-vous d'utiliser réellement votre application React de manière extensive comme test final une fois que tout le processus de mise à niveau est terminé.

Occasionnellement, vous devrez peut-être exécuter `$ rm -rf node_modules` et `$ rm package.lock.json` / `$ rm yarn.lock` car certains changements de bibliothèque peuvent ne pas se propager correctement. Idéalement, vous n'aurez pas besoin de faire cela, mais c'est raisonnablement sûr car cela télécharge simplement tous les paquets à nouveau.

## Comment passer à React Scripts v4.0.3

Selon le moment où vous avez commencé votre projet avec CRA, vous serez probablement à différentes versions de la v4. Tout d'abord, nous passons à la dernière version mineure pour faciliter le reste du processus de mise à niveau.

Il ne devrait pas y avoir de changements majeurs entre les versions mineures, mais assurez-vous de la mettre à niveau de manière incrémentielle dans votre `package.json` en allant de `4.0.0` -> `4.0.1` -> `4.0.2` -> `4.0.3`. Passer à `4.0.3` rationalisera votre processus de mise à niveau puisque ces mises à jour mineures comportent de nombreuses corrections de bugs, de bibliothèques et de dépendances utiles sans créer de nouveau travail pour l'instant. 

J'ai exécuté `$ yarn install` après chaque étape puis vérifié mes commandes de validation pour m'assurer que tout fonctionnait toujours.

```json
... 
"dependencies": { 
	"react-scripts": "4.0.1", 
    ... 
}, 
...
```

Dans mes projets, je n'ai rencontré aucun problème, mais votre expérience peut varier. La documentation officielle du [changelog CRA v4](https://github.com/facebook/create-react-app/blob/main/CHANGELOG-4.x.md) contient une liste des petits changements et des étapes de mise à niveau entre les versions, ce qui permettra de réduire les causes.

## Comment passer à la version Node 18

Après vous être assuré que vos commandes de validation fonctionnent sur votre Node 16 actuel, définissez votre version sur 18. Ensuite, nous travaillons à corriger toutes les commandes de validation jusqu'à ce que toutes fonctionnent. Occasionnellement, vous pourriez revenir à la version 16 pour vous assurer que les choses fonctionnent toujours dans l'ancienne version. 

Dans votre ligne de commande, exécutez ce qui suit :

```sh
$ nvm install 18
$ nvm use 18
```

> Note : Si vous avez un fichier `.nvmrc`, vous pouvez omettre les numéros de version dans les commandes `nvm install` et `nvm use`. Mettez à jour le fichier lorsque vous changez les versions de node.

Malheureusement, si vous essayez `$ yarn start` ou `$ yarn build`, vous rencontrerez immédiatement l'erreur de cryptographie qui provient de `openssl`, qui bloque tout le chiffrement utilisant MD4. C'est l'erreur principale bloquant la mise à niveau vers Node 18 tout en étant sur CRA 4.

```
Error: error:0308010C:digital envelope routines::unsupported
```

### Comprendre le problème MD4

MD4 est un ancien algorithme de chiffrement des années 1990 et est considéré comme très peu sécurisé depuis 1995 ([Wikipedia](https://en.wikipedia.org/wiki/MD4)). OpenSSL à partir de la version 3 a changé MD4 pour qu'il ne soit plus pris en charge par défaut, mais il peut être activé avec un indicateur de legacy non sécurisé [flag](https://github.com/openssl/openssl/issues/21247) sur votre système `openssl` ou `--openssl-legacy-provider` si vous l'ajoutez à votre script node/CRA (voir la documentation Node [docs](https://nodejs.org/api/cli.html#--openssl-legacy-provider)). 

C'est une solution apparemment simple au problème, mais c'est plus un dernier recours puisque permettre une cryptographie non sécurisée est généralement une mauvaise idée, et OpenSSL a désactivé l'algorithme entièrement pour une raison.

> Note : Si vous êtes curieux, Webpack a une discussion de 1000+ réponses [discussion](https://github.com/webpack/webpack/issues/14532) sur ce sujet qui pourrait contenir quelque chose d'utile. Les versions ultérieures de Webpack ont également finalement [autorisé](https://github.com/webpack/webpack/pull/14306) un meilleur algorithme appelé [xxHash](https://github.com/Cyan4973/xxHash), ajouté une implémentation MD4 `wasm` intégrée [implémentation](https://github.com/webpack/webpack/pull/14584), et ajouté une nouvelle option de configuration appelée [deterministic](https://webpack.js.org/configuration/optimization/#optimizationmoduleids) qui contourne le problème. 

Je recommande vivement de lire cette réponse StackOverflow [réponse](https://stackoverflow.com/questions/69692842/error-message-error0308010cdigital-envelope-routinesunsupported) pour un aperçu rapide des principales options si nous ne le corrigeons pas nous-mêmes. Puisque la mise à niveau des dépendances n'est pas possible ici, et que nous ne voulons pas rester sur une ancienne version de Node ou permettre des algorithmes non sécurisés, nous devons plonger dans les internes de CRA pour le corriger.  

## Comment éjecter de React Scripts

CRA est conçu pour une expérience sans configuration pour les applications React qui vous permet de vous concentrer uniquement sur le travail de votre logique métier. 

Lorsque vous souhaitez commencer à modifier la configuration, CRA n'a pas de méthode intégrée pour remplacer une option. Au lieu de cela, il offre une commande appelée `eject` qui copie tous les internes de CRA vers votre projet tout en laissant vos commandes yarn/npm intactes et en supprimant ensuite React scripts de votre projet entièrement. C'est une action irréversible, alors assurez-vous de sauvegarder la version précédente dans `git`. 

```shell
$ yarn eject
```

C'est une commande énorme qui modifiera de nombreux fichiers dans les répertoires `config/` et `scripts/` ainsi que votre liste de paquets dans `package.json`. Une fois que vous relancez `yarn install`, assurez-vous d'exécuter toutes vos commandes de validation pour vous assurer que tout fonctionne toujours sur Node 16 puisque rien n'aurait dû changer en termes de fonctionnalité.

Alternativement, si vous ne souhaitez pas essayer `eject`, il existe également des solutions de contournement comme :

* CRACO utilise un mécanisme de remplacement astucieux pour vous permettre de continuer à utiliser React Scripts tout en personnalisant. Lisez [Getting Started](https://craco.js.org/docs/getting-started/) et [Why I built CRACO](https://medium.com/workleap/why-i-built-craco-33ff39f4fc94). Commencez avec la version `6.4.5` pour CRA v4.
* [patch-package](https://github.com/ds300/patch-package) applique des modifications spécifiques aux paquets npm pour votre projet, puis vous partagez le patch avec votre équipe/projet. Pour ce guide, vous patcherez `react-scripts` avec les configurations webpack et config modifiées.
* Forking CRA avec vos propres modifications. De cette façon, vous pouvez toujours garder la configuration zéro de CRA sans hacks pour intégrer de nouvelles fonctionnalités, mais cela pourrait se compliquer. Voici un guide que j'ai vu en ligne : [Customizing create-react-app: How to Make Your Own Template](https://auth0.com/blog/how-to-configure-create-react-app/).

Il y a aussi [react-app-rewired](https://github.com/timarney/react-app-rewired) pour un but similaire, mais il est principalement non maintenu en ce moment et destiné aux anciennes versions de CRA derrière la v4.

### Comment ajouter des ignores de linter pour les fichiers éjectés

Beaucoup des nouveaux fichiers de la configuration éjectée peuvent ne pas suivre les règles du linter de votre projet existant. Jusqu'à ce que vous ayez terminé la mise à niveau, je recommande simplement d'ajouter de nouveaux ignores en haut des fichiers échouant comme :

```js
/* eslint-disable import/order */

// reste du fichier
...
```

Une fois que vous avez terminé l'ensemble du tutoriel, n'hésitez pas à revenir en arrière et à essayer de corriger certains des problèmes de linter, mais il peut être acceptable de laisser ces fichiers tels quels puisque vous y entrerez rarement pour changer quelque chose.

### Comment corriger les chemins absolus pour Jest

Dans votre `package.json`, l'option `"testRunner"` de Jest peut être codée avec le chemin absolu qui n'a de sens que sur votre ordinateur. Vous voudrez donc le changer en un chemin basé sur le répertoire racine de votre projet. 

Bien que cela puisse fonctionner correctement pour votre développement local, cela posera problème pour tout collaborateur ou ordinateur cloud.

```json
... 
"jest": { 
	... 
    "testRunner": "/my/computer/path/project_name/node_modules/jest-circus/runner.js", 
    ... 
}, 
...
```

Nous utilisons l'option `<rootDir>` fournie par [Jest](https://jestjs.io/docs/configuration#rootdir-string) :

```json
... 
"jest": { 
	... 
    "testRunner": "<rootDir>/node_modules/jest-circus/runner.js", 
    ... 
}, 
...
```

Vous n'aurez peut-être pas à faire cela sur tous les projets, mais `"modulePaths"` peut également avoir besoin d'une mise à jour :

```json
...
"jest": { 
    ... 
    "modulePaths": [ "/my/computer/path/project_name/src" ] 
    ... 
}, 
...
```

Supprimez simplement la référence au chemin absolu de votre ordinateur :

```json
...
"jest": { 
    ... 
    "modulePaths": [ "src" ] 
    ... 
}, 
...
```

### Comment mettre à jour votre Dockerfile et autres processus de build avec les dossiers éjectés

Assurez-vous d'inclure les nouveaux dossiers éjectés, `scripts/` et `config/`, dans votre `Dockerfile` et autres processus de build que vous pourriez utiliser et qui existaient en dehors de CRA. 

Par exemple, le Dockerfile aura les ajouts de nouveaux répertoires que CRA a créés et que nous voulons également copier.

```dockerfile
... 
COPY scripts scripts/
COPY config config/ 
...
```

## Comment remplacer Webpack MD4 par SHA256

Basé sur cette [réponse StackOverflow](https://stackoverflow.com/a/78005686), nous ajoutons à `webpack.config.js` juste avant de commencer à définir `module.exports` pour utiliser le SHA256 relativement plus moderne et sécurisé au lieu de MD4 qui est également intégré dans Webpack :

```js
// ... 
// https://stackoverflow.com/a/78005686 
const crypto = require("crypto"); 
const crypto_orig_createHash = crypto.createHash; crypto.createHash = algorithm => crypto_orig_createHash(algorithm == "md4" ? "sha256" : algorithm); 
// This is the production and development configuration. 
// It is focused on developer experience, fast rebuilds, and a minimal bundle. 
module.exports = function (webpackEnv) 
// ...
```

Une fois que vous avez changé cela, les erreurs d'enveloppe devraient disparaître et vos commandes de validation devraient maintenant fonctionner pour Node 18.

## Comment mettre à niveau vers la dernière version de Jest

L'`eject` expose également la configuration Babel utilisée pour faire fonctionner les versions plus récentes de Jest correctement. Cela fonctionne très bien pour la version 26, mais le déplacement de la configuration CRA vers la dernière version (v29 au moment de l'écriture) comporte quelques étapes supplémentaires. 

Vous devriez passer par `v26` -> `v28` -> `v29` (en sautant v27) pour toutes les dépendances Jest. Cette partie est facultative si vous êtes satisfait de Jest 26 de CRA v4, mais jusqu'à ce que vous éjectiez, vous êtes bloqué pour la mise à niveau vers une version récente de Jest.

Je saute Jest 27 car cela nécessitera un changement dans `config/jest/babelTransform.js` où vous devrez changer `module.exports = babelJest.default.createTransformer({` en `module.exports = babelJest.createTransformer({`. C'était un bug [corrigé](https://github.com/jestjs/jest/pull/12399) dans la version 28. Cependant, si vous souhaitez passer par Jest 27 également, vous pourrez suivre le reste des étapes avec ce changement et ensuite éventuellement le revenir en arrière sur Jest 28.

Je recommande également vivement de lire les articles d'introduction pour chaque mise à niveau de version de Jest :

* [Jest 27 : Nouveaux paramètres par défaut pour Jest, édition 2021 ](https://jestjs.io/blog/2021/05/25/jest-27)
* [Jest 28 : Réduction du poids et amélioration de la compatibilité ](https://jestjs.io/blog/2022/04/25/jest-28)
* [Jest 29 : Changements de format de snapshot](https://jestjs.io/blog/2022/08/25/jest-29)

La plupart des problèmes proviennent de Jest 28 ayant de nombreux changements majeurs, mais le reste du chemin de mise à niveau est assez simple.

### Comment passer à Jest 28

Pour chaque mise à niveau, je recommande de faire une recherche et un remplacement pour tous les nombreux paquets liés à Jest dans votre `package.json` puisque les numéros de version sont tous synchronisés. Une fois que vous avez mis à jour les numéros, exécutez simplement `$ yarn install` :

```json
... 
"devDependencies": { 
    ...
    "babel-jest": "^28.1.3", 
    ...
    "jest": "^28.1.3", 
    "jest-circus": "^28.1.3", 
    "jest-resolve": "^28.1.3", 
    ...
} 
...
```

### Comment définir explicitement `jsdom` comme environnement de test

Si vous essayez d'exécuter vos tests directement avec `$ yarn test`, vous obtiendrez cette erreur :

```
 Erreur de validation : 
L'environnement de test jest-environment-jsdom est introuvable. 
Assurez-vous que l'option de configuration testEnvironment pointe vers un module node existant. 
Documentation de configuration : https://jestjs.io/docs/configuration 
À partir de Jest 28, "jest-environment-jsdom" n'est plus fourni par défaut, assurez-vous de l'installer séparément.
```

Dans Jest 27, Jest a [changé l'environnement de test par défaut](https://jestjs.io/blog/2021/05/25/jest-27) pour être destiné à un environnement backend NodeJS plus léger. Cependant, nous avons une application frontend, donc nous voulons toujours tester avec un environnement de navigateur simulé sur lequel les anciennes versions de Jest étaient basées, appelé [jsdom](https://github.com/jsdom/jsdom). 

Pour corriger cela, ajoutez `"jest-environment-jsdom"` à vos dépendances, puis exécutez `$ yarn install`.

```json
... 
"devDependencies": { 
    ...
    "babel-jest": "^28.1.3", 
    ...
    "jest": "^28.1.3", 
    "jest-circus": "^28.1.3", 
    "jest-resolve": "^28.1.3", 
    "jest-environment-jsdom": "^28.1.3", 
    ...
} 
...
```

### Comment corriger le type de retour du transformateur pour `process()` et `processAsync()`

Maintenant, si vous exécutez `yarn test`, vous obtiendrez ceci :

```
FAIL  src/App.test.js 
 La suite de test n'a pas pu s'exécuter 
 Valeur de retour invalide : la méthode `process()` ou/et `processAsync()` du transformateur de code trouvé à "path/in/my/computer" 
doit retourner un objet ou une promesse se résolvant en un objet. L'objet doit avoir une propriété `code` avec une chaîne de code traité. 
Cette erreur peut être causée par un changement majeur dans Jest 28 : https://jestjs.io/docs/upgrading-to-jest28#transformer Documentation de la transformation de code : https://jestjs.io/docs/code-transformation
```

C'est parce que les fonctions `process()` qui retournaient une chaîne attendent maintenant un objet au format `{ code: `old_string_here` }`. 

Pour corriger cela, nous allons dans notre dossier `config/jest` éjecté, et nous changeons la forme de sortie pour tous nos fichiers. Pour CSS, c'est un changement de ligne unique :

```js
// This is a custom Jest transformer turning style imports into empty objects. 
// http://facebook.github.io/jest/docs/en/webpack.html 

module.exports = { 
    process() { 
        return { code: 'module.exports = {};' }; 
    }, 
    getCacheKey() { 
        // The output is always the same. 
        return 'cssTransform'; 
    }, 
};
```

et pour les fichiers, vous devez changer les deux instructions de retour de branche :

```js
const path = require('path'); 
const camelcase = require('camelcase'); 

// This is a custom Jest transformer turning file imports into filenames. // http://facebook.github.io/jest/docs/en/webpack.html 
module.exports = { 
	process(src, filename) { 
    	const assetFilename = JSON.stringify(path.basename(filename)); 
        if (filename.match(/\.svg$/)) { 
            // Based on how SVGR generates a component name: 
            // https://github.com/smooth-code/svgr/blob/01b194cf967347d43d4cbe6b434404731b87cf27/packages/core/src/state.js#L6 
            const pascalCaseFilename = camelcase(path.parse(filename).name, { pascalCase: true, }); 
            const componentName = `Svg${pascalCaseFilename}`; 
            return { code: `const React = require('react')...` // pretty long string }; 
        }
        
        return {code: `module.exports = ${assetFilename};` }; 
    }, 
};
```

Note : Au moment de l'écriture, le lien du message d'erreur vers le guide de mise à niveau [ne fonctionne pas](https://github.com/jestjs/jest/issues/15112#issuecomment-2160883936), mais vous pouvez trouver le lien correct à l'adresse [https://jest-archive-august-2023.netlify.app/docs/28.x/upgrading-to-jest28/](https://jest-archive-august-2023.netlify.app/docs/28.x/upgrading-to-jest28/). Il y a aussi un ancien [lien d'archive](https://web.archive.org/web/20230330085721/https://jestjs.io/docs/28.x/upgrading-to-jest28#transformer) si cela ne fonctionne pas.

### Comment passer à Jest 29

Une fois que toutes les étapes de validation fonctionnent avec Jest 28, la mise à niveau vers 29 devrait être plus fluide. Mettez simplement à jour votre `package.json` et exécutez `$ yarn install` :

```json
... 
"devDependencies": { ... 
    "babel-jest": "^29.7.0", 
    "jest": "^29.7.0", 
    "jest-circus": "^29.7.0", 
    "jest-resolve": "^29.7.0", 
    "jest-environment-jsdom": "^29.7.0" ... 
} 
...
```

À ce stade, `$ yarn test` devrait fonctionner correctement avec votre suite de tests existante. 

## Jusqu'où devrais-je mettre à niveau NodeJS ?

Essayer de décider jusqu'où mettre à niveau les versions de Node peut être une question délicate. En suivant les étapes ci-dessus, j'ai pu faire fonctionner toutes les versions de Node jusqu'à la plus récente, Node 22. 

Au moment de l'écriture, la version 18 est un bon point d'arrêt en termes de support actuel et de support récent d'ECMAScript. Mais si vous cherchez à décider, alors les trois facteurs suivants sont les plus importants :

1. Support des bibliothèques : Regardez toutes vos bibliothèques critiques et voyez si elles ont une forte préférence pour une certaine version ou ont des problèmes majeurs pour les versions plus récentes. Les versions ultérieures de Node sont généralement meilleures, mais parfois les anciennes bibliothèques n'ont pas reçu les bons correctifs et pourraient bloquer votre mise à niveau.
2. Fenêtres de support : Différentes versions de Node ont une fenêtre où les mainteneurs la considèrent comme "Maintenance", "Active", "Courante" ou "Non supportée", et avec le temps, les versions plus anciennes perdent leur maintenance. Les versions paires sont également désignées LTS (Long Term Support), offrant un support pendant une longue période et ce qui fonctionne pour la plupart des gens. Le site web a un tableau utile pour cela : [https://nodejs.org/en/about/previous-releases](https://nodejs.org/en/about/previous-releases).
3. Support des fonctionnalités du langage : La spécification ECMAScript évolue toujours chaque année, et pouvoir utiliser la nouvelle syntaxe avec des constructions plus agréables est toujours une grande amélioration de la qualité de vie. J'adore [https://node.green/](https://node.green/) qui a un tableau des versions de Node contre les fonctionnalités de syntaxe ECMAScript avec des exemples de code pour chaque fonctionnalité.

Grâce à des technologies comme [Babel](https://babeljs.io/) (fournis avec Create React App), vous n'avez pas à vous soucier trop des utilisateurs finaux de votre site web, car les nouvelles fonctionnalités de Node seront simplement transpilées en des fonctionnalités compatibles avec les navigateurs.

## Devriez-vous toujours utiliser Create React Scripts ? Quelles sont les alternatives ?

Dans ce tutoriel, j'ai décidé de m'éjecter de CRA pour accéder à la configuration de Webpack et Babel, et de nombreux projets CRA ont finalement fait de même. La maintenance de CRA a presque cessé alors que l'écosystème continue d'évoluer. 

Personnellement, je recommande à quelqu'un créant un projet React aujourd'hui d'essayer de nouvelles alternatives comme [Vite](https://vitejs.dev/guide/) ou [Parcel](https://parceljs.org/recipes/react/) qui ont de belles applications de démarrage simples et faciles à comprendre. Malheureusement, elles n'ont peut-être pas autant de fonctionnalités que ce que CRA offre, mais c'est suffisant pour presque tout le développement moderne pratique. 

Dans le contexte de l'éducation, mes anciens tutoriels utilisaient `create-react-app`, et c'était une aide majeure, mais mes nouveaux tutoriels utiliseront Vite.

Néanmoins, votre application et votre expérience de développement peuvent être très différentes des miennes. Je recommande de lire et d'apprendre à partir de ces ressources pour former votre propre perspective :

* Problème GitHub [issue](https://github.com/reactjs/react.dev/pull/5487) avec plus de 200 réponses et des milliers de réactions sur le fait de savoir si Create React App devrait être remplacé par Vite dans la documentation officielle. Il contient également une [note](https://github.com/reactjs/react.dev/pull/5487#issuecomment-1409720741) du côté des mainteneurs de CRA expliquant beaucoup de contexte important qui vaut vraiment la peine d'être lu. Le mainteneur de Parcel a également fait un très bon [commentaire](https://github.com/reactjs/react.dev/pull/5487#issuecomment-1399360209).
* Certains commentaires intéressants ([un](https://github.com/reactjs/react.dev/pull/5487#issuecomment-1423368130), [deux](https://github.com/facebook/create-react-app/issues/13598)) sur la façon dont CRA a créé une expérience React simple et facile à utiliser dès la sortie de la boîte sans se soucier de l'enfer de la configuration et en se concentrant sur l'application réelle.
* [Article de news](https://medium.com/@vivekdwivedi/the-end-of-an-era-react-team-no-longer-recommends-create-react-app-f2fe6e842d13) expliquant que l'équipe React a choisi d'arrêter de recommander Create React App, ainsi que certains contextes derrière cela et les alternatives futures.

## Conclusion

À ce stade, vous devriez être en mesure d'exécuter tous vos scripts de validation et d'avoir une application qui fonctionne avec Node 18+ et Jest 29+.

Dans un monde idéal, vous rencontreriez les mêmes obstacles que moi, et tout fonctionnerait. En réalité, l'application de chacun est différente, et Internet regorge de nombreux développeurs qui ont traversé ce processus de mise à niveau avec divers problèmes. 

Je vous recommande vivement de faire de Google, StackOverflow, GitHub et de la documentation officielle des bibliothèques vos meilleurs amis dans le processus, et je vous souhaite bonne chance !

### Alternativement : Comment mettre à niveau vers React Scripts 5.0.1

Cela dépasse le cadre de ce tutoriel, donc je serai plus bref ici – mais voici quelques informations pour vous aider à démarrer. 

Je suggère de commencer par le changelog officiel de CRA v5 qui inclut tous les changements majeurs ainsi que certaines instructions de mise à niveau de version : [https://github.com/facebook/create-react-app/blob/main/CHANGELOG.md](https://github.com/facebook/create-react-app/blob/main/CHANGELOG.md).

La mise à niveau de la version est assez facile, en définissant `react-scripts` sur `5.0.1` dans votre `package.json`, mais ensuite la partie difficile est tous les changements majeurs.

La partie la plus compliquée de la mise à niveau est la mise à niveau vers Webpack 5 depuis Webpack 4. Lisez le guide officiel de Webpack [Vers v5 depuis v4](https://webpack.js.org/migrate/5/) qui donne un bon aperçu, et cherchez sur Internet des guides pour cette mise à niveau. Voici quelques autres obstacles que vous pourriez rencontrer :

* Pour `@babel/helper-compilation-targets: 'opera_mobile' is not a valid target`, vous pouvez ajouter `"not op_mob >= 1"` au tableau `browserslist` comme suggéré par ce [commentaire](https://github.com/babel/babel/issues/16171#issuecomment-2015227043) sur le suivi des problèmes de babel. Les autres commentaires peuvent également être utiles.
* Vous devrez probablement accéder aux internes de CRA pour de nombreuses étapes en utilisant soit React Scripts `eject` ou quelque chose comme [CRACO version 7](https://craco.js.org/docs/getting-started/).
* Webpack 5 a un changement majeur qui supprime le support pour de nombreuses API spécifiques aux navigateurs comme `os`, `http`, `util` qui fonctionnaient dans Webpack 4 et que votre application pouvait utiliser. Vous pouvez soit les ajouter tous en utilisant un package comme [node-polyfill-webpack-plugin](https://github.com/Richienb/node-polyfill-webpack-plugin) ou ajouter des imports pièce par pièce en suivant cette [feuille de triche](https://gist.github.com/ef4/d2cf5672a93cf241fd47c020b9b3066a).
* Pour les erreurs de chargement du parseur Babel eslint comme `Error: Failed to load parser 'babel-eslint' declared in '.eslintrc': Cannot find module 'babel-eslint'`, vous devrez peut-être remplacer `"parser": "babel-eslint"` par `"parser": "@babel/eslint-parser"` dans votre `.eslintrc` et installer `"@babel/eslint-parser"` dans votre `package.json`. Cela pourrait être causé par le déplacement de `babel-eslint` vers le monorepo `@babel`, voir [The State of babel-eslint](https://babeljs.io/blog/2020/07/13/the-state-of-babel-eslint) pour plus d'informations.
* Certaines importations de types de fichiers qui fonctionnaient avec Webpack 4 commenceront à échouer avec `Module build failed: UnhandledSchemeError` (l'erreur réelle a pris plusieurs écrans dans mon Terminal). La solution ici sera de corriger les préfixes des fichiers que vous importez, et pour les fichiers externes qui étaient inclus, voir si vous pouvez trouver un package npm pour cela. Par exemple, l'un de mes projets a arrêté d'utiliser `semantic-ui.min.css` téléchargé depuis Internet, et à la place, j'ai ajouté `"semantic-ui-css": "^2.5.0"` à mon `package.json`. Lisez définitivement ce [fil de discussion](https://github.com/webpack/webpack/issues/12792) dans le dépôt webpack pour plus d'informations.

Après tout cela, j'ai pu faire fonctionner `yarn test` et `yarn build` avec succès, mais `yarn start` avait encore trop de problèmes et j'ai pivoté pour faire fonctionner CRA v4 à la place. Espérons que vous pourrez aller plus loin que moi.