---
title: Comment ajouter TypeScript à un projet JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-27T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-typescript-to-a-javascript-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/1_9XMpTyccrky0eW5Wz6DoWQ.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment ajouter TypeScript à un projet JavaScript
seo_desc: "By dor sever\nI love writing code. And I want to be really good at it.\
  \ But somehow, writing JavaScript has never been my strong suit. \nNo matter how\
  \ much I practiced, the same mistakes kept appearing in production: cannot read\
  \ property <> of undefined..."
---

Par dor sever

J'adore écrire du code. Et je veux être vraiment bon dans ce domaine. Mais d'une manière ou d'une autre, écrire en JavaScript n'a jamais été mon point fort. 

Peu importe combien je pratiquais, les mêmes erreurs continuaient d'apparaître en production : des exceptions `cannot read property <> of undefined`, la fameuse chaîne `[Object object]`, et même des appels de fonction avec un nombre invalide de paramètres.  


De plus, la plupart des bases de code sur lesquelles je travaillais étaient vraiment grandes et en JavaScript. Voici donc un joli diagramme de ce que cela faisait de ressembler à moi :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/typescript-vs-javascript--1-.png)
_Nous pouvons faire beaucoup mieux !_

Dans cet article, j'éviterai d'expliquer pourquoi TypeScript est génial (et il l'est), et me concentrerai sur les tâches que vous devez accomplir si vous souhaitez migrer votre projet JavaScript vanilla vers un projet TypeScript mixte.

À la fin de cet article, vous serez une personne plus heureuse et pourrez répondre aux questions suivantes :

* Comment puis-je ajouter des types à mon projet JavaScript ?
* Qu'est-ce que TypeScript ?
* Comment puis-je utiliser TypeScript dans un projet JavaScript ?
* Quelles sont les étapes pour convertir une application JavaScript pour supporter TypeScript ?
* Comment puis-je gérer la construction et le packaging ?
* Comment puis-je gérer le linting ?
* Comment puis-je "vendre" TypeScript à mon organisation et aux développeurs ?

## Comment puis-je ajouter des types à mon projet JavaScript ?

Le JavaScript vanilla ne supporte pas les types pour le moment, nous avons donc besoin d'une sorte d'abstraction par-dessus JavaScript pour le faire. 

Quelques abstractions courantes sont l'utilisation du vérificateur de types statique de Facebook appelé `[flow](https://github.com/facebook/flow)` et le langage de Microsoft appelé :`[typescript](https://github.com/microsoft/TypeScript)`.

Cet article de blog examinera l'utilisation et l'ajout de TypeScript à votre projet JavaScript.

## Qu'est-ce que TypeScript ?

TypeScript est un sur-ensemble typé de JavaScript qui compile en JavaScript simple.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/superset.png)
_Si vous connaissez JavaScript, vous êtes déjà à plus de la moitié du chemin._

TypeScript se compose de plusieurs parties. La première est le langage TypeScript — il s'agit d'un nouveau langage qui contient toutes les fonctionnalités de JavaScript. Consultez les [spécifications](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md) pour plus d'informations.

La seconde est le compilateur TypeScript, `tsc` (le moteur du système de types) qui est un moteur de compilation qui construit les fichiers ts et génère des fichiers js.

## Hello world en TypeScript

Par exemple, voici les étapes à suivre pour écrire votre première application TypeScript :

1. installer TypeScript avec `npm i typescript`
2. créer un dossier appelé `example` et y accéder (dans votre terminal)
3. créer un fichier appelé `hello.world.ts`
4. écrire le code suivant dedans :

```typescript
const firstWords:string = "hello world"
console.info(firstWords);

```

puis l'enregistrer.

5. exécuter la commande `tsc` pour exécuter le compilateur TypeScript sur le dossier courant

6. remarquer que vous avez obtenu un fichier `hello.js` que vous pouvez maintenant exécuter :) 

7. exécuter `node ./hello.js`

## Comment puis-je utiliser TypeScript dans un projet JavaScript ?

Il existe plusieurs stratégies pour effectuer cette "migration" (au niveau de l'entreprise et du code). Je les ai listées ci-dessous par leur "coût" et par la valeur qu'elles apportent. 

Je suggérerais de commencer par "le support TS de l'application" et d'avancer une fois que vous avez prouvé la valeur à votre équipe de développement.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/typescript-migration-steps.png)
_Le processus de migration TypeScript, itérez à travers le processus seulement si vous prouvez la valeur._

### L'approche "petit pas pour l'homme" - Ajout du support TS pour les applications existantes

![Image](https://www.freecodecamp.org/news/content/images/2020/07/small-step.jpeg)
_Un petit pas pour un développeur. Les types sont merveilleux :)_

Ma première suggestion est de créer un mélange des deux langages dans un seul projet, puis d'écrire tout le code "futur" en TypeScript.

La combinaison de deux langages dans un seul projet semble assez terrible au premier abord, mais cela fonctionne plutôt bien puisque TS a été conçu pour une utilisation progressive. Au début, il peut être utilisé simplement comme du JS avec des fichiers .ts et des lignes d'importation étranges.

Dans cette stratégie, nous compilerons les fichiers TypeScript migrés et copierons simplement les fichiers JavaScript dans un dossier de sortie.

L'énorme avantage de cette approche est qu'elle permet une courbe d'apprentissage progressive pour l'équipe de développement (et pour vous) avec le langage et ses fonctionnalités. Elle vous donne également une expérience pratique et un aperçu de ses avantages et inconvénients.

Je recommande vivement de commencer par cette étape, puis d'itérer avec votre équipe avant de passer à l'étape suivante. Pour un guide rapide "comment faire", faites défiler jusqu'à la partie `Les étapes pour convertir une application JavaScript pour supporter TypeScript`.

### L'approche ouverte aux affaires - Ajout du support TS pour les bibliothèques existantes.

Une fois que vous avez une certaine expérience pratique avec TS et que votre équipe de développement est d'accord pour avancer, je suggère de convertir vos bibliothèques et modules internes pour supporter TS. 

Cela peut être fait de deux manières :

**La première manière** implique l'utilisation de [fichiers de déclaration](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html). Une simple addition de fichiers `d.ts` aide le compilateur TS à vérifier les types du code JavaScript existant et vous donne un support d'auto-complétion dans votre IDE. 

C'est l'option la "moins chère", car elle ne nécessite aucun changement de code dans la bibliothèque. Elle vous donne également un maximum de puissance et de support de types dans votre code futur.

**La deuxième manière** est d'effectuer une réécriture complète en TypeScript, ce qui peut être chronophage et sujet aux erreurs. Je vous déconseille de le faire, sauf si cela s'avère rentable pour votre équipe.

### Le squelette - une étape vers l'avenir

![Image](https://www.freecodecamp.org/news/content/images/2020/07/future.jpeg)
_Le squelette TypeScript est la voie pour assurer un avenir radieux !_

Je suppose que la plupart des développeurs sont "paresseux" et commencent généralement leur application en copiant à partir d'un squelette (qui contient généralement des logs, des métriques, de la configuration, etc.).

Cette étape vous aide à naviguer vers un avenir radieux, en créant un squelette "officiel" pour votre entreprise. Il sera 100% TS, et dépréciera l'ancien squelette JS s'il existe.

Ce [typescript-node-starter](https://github.com/microsoft/TypeScript-Node-Starter#getting-started) est un très bon premier projet pour commencer.

### **L'approche tout compris - Conversion d'une base de code complète de JS en TS**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/allin.jpeg)
_Je suis tout à fait pour ! Rendons toutes les choses typées !_

Cette option nécessite une réécriture totale du code JavaScript en TypeScript.   
  
Je recommanderais de faire cela comme dernière étape dans le processus de migration TS, car cela nécessite une réécriture totale de l'application et une connaissance approfondie de TypeScript et de ses fonctionnalités.

Vous pouvez effectuer une telle réécriture (c'est un long processus) de la manière suivante :

1. Définir des types clairs pour la logique métier de votre application, l'API et les HTTP.
2. Utiliser les packages `@types` pour toutes les bibliothèques dans votre `package.json`. La plupart des bibliothèques supportent TS, et dans ce processus, je suggère de les migrer une par une (en ajoutant simplement `@types/<package_name>` dans votre fichier `package.json`).
3. Convertir les composants logiques de votre application dans l'ordre de leur importance. Plus la logique métier est unique, mieux c'est.
4. Convertir les parties IO de votre application, les couches de base de données, les files d'attente, etc.
5. Convertir vos tests.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/champagne.jpeg)
_Les types sont une raison de célébrer :)_

Gardez à l'esprit qu'il existe des outils automatisés conçus pour faciliter ce processus, par exemple [ts-migrate](https://github.com/airbnb/ts-migrate) de l'équipe Airbnb. 

Il aborde ce problème sous un angle différent et convertit tous les fichiers en TypeScript. Il permet également des améliorations progressives (comme mentionné dans les étapes ci-dessus) tandis que l'ensemble du code est en TypeScript dès le premier jour.

## Comment convertir une application JavaScript pour supporter TypeScript.

### Installer TypeScript 

en exécutant : `npm install typescript`.

### Fichier de configuration TypeScript

Ajoutez un fichier de configuration TypeScript, qui peut être créé en utilisant la commande `tsc --init` dans votre CLI.

Voici un exemple de notre configuration initiale :

```json
{
 "compilerOptions": {
   "target": "esnext",
   "module": "commonjs",
   "allowJs": true,
   "checkJs": false,
   "outDir": "dist",
   "rootDir": ".",
   "strict": false,
   "esModuleInterop": true /* Active l'interopérabilité d'émission entre CommonJS et les modules ES via la création d'objets de namespace pour toutes les importations. Implique 'allowSyntheticDefaultImports'. */,
   "forceConsistentCasingInFileNames": true, /* Interdit les références avec une casse incohérente vers le même fichier. */
   "declaration": true, /* Génère un fichier '.d.ts' correspondant. */
   "strictNullChecks": true,
   "resolveJsonModule": true,
   "sourceMap": true,
   "baseUrl": ".",
   "paths": {
    "*": [
      "*",
      "src/*",
      "src/installation/*",
      "src/logic/*",
      "src/models/*",
      "config/*"
    ]
  },
 },
  "exclude": ["node_modules", "dist"],
  "include": [
    "./src",
    "./test",
    "./*",
    "./config" 
  ]
}
```

Quelques points à noter ci-dessus :

* Nous lisons tous les fichiers dans le répertoire `src` ou `test` ou `config` (en utilisant le drapeau `include`).
* Nous acceptons les fichiers JavaScript comme entrées (en utilisant le drapeau `allowJs`).
* Nous émettons tous les fichiers de sortie dans `build` (en utilisant le drapeau `outDir`).

### Créez votre premier fichier .TS dans votre projet 

Je recommande de commencer par ajouter un fichier TypeScript simple (ou en changeant un fichier JS vraiment simple en un fichier TS) et de le déployer. Prenez cette migration étape par étape.

### Prenez soin de votre fichier package.json

Voici à quoi ressemble notre `package.json` avant et après :

```json
{
  "scripts": {
    "start": "node ./application.js",
    "mocha": "mocha --recursive --reporter spec -r test/bootstrap.js",
    "test": "npm run mocha -- test/ -r test/integration/bootstrap.js", 
  }
}
```

```json
{
  "scripts": {
    "start": "node ./dist/application.js",
    "build-dist": "./node_modules/typescript/bin/tsc",
    "mocha": "mocha --recursive --reporter spec -r ./dist/test/bootstrap.js",
    "test": "npm run mocha -- ./dist/test/ -r ./dist/test/integration/bootstrap.js"
  }
}
```

Comme vous pouvez le voir, la plupart des changements concernaient l'ajout du préfixe `dist` à la plupart de nos commandes de build. Nous avons également ajouté un script `build-dist` qui compile notre base de code et déplace tous les fichiers vers un dossier dédié appelé `dist`.

### Ajouter source-map-support

L'un des grands problèmes lors de l'ajout de TypeScript à votre projet est que vous ajoutez une couche d'indirection entre le code que vous écrivez et le code qui s'exécute réellement en production (puisque `.ts` est transpilé en `.js` au moment de l'exécution).

Par exemple, imaginez le programme TypeScript suivant :

```typescript
const errorMessage: string = "this is bad"

throw new Error(a)
```

Lorsque nous l'exécutons, il génère la trace de pile suivante :

```typescript
Error: this is bad
    at Object.<anonymous> (/Users/dorsev/work/git/example/hello.js:3:7)
```

Cela pose problème puisque notre base de code ne contient que des fichiers `.ts`. Et comme la plupart des codes de production contiennent des centaines de lignes, il sera vraiment chronophage de traduire correctement ces numéros et fichiers. 

Heureusement pour nous, il existe une solution pour cela appelée [source-map-support](https://www.npmjs.com/package/source-map-support) !

Cela nous permet de garantir que les traces de pile auront des noms de fichiers `.ts` et des numéros de ligne appropriés comme nous en avons l'habitude :) 

Cela peut être fait en exécutant `npm install source-map-support` puis en ajoutant la ligne suivante dans les premières lignes de votre application :

`require('source-map-support').install();`

Le code ressemble maintenant à ceci :

```typescript
require('source-map-support').install();
const a:string = "this is bad"
throw new Error(a)
```

Et lorsque nous le compilons, nous exécutons `tsc --sourcemap hello.ts`. Maintenant, nous obtenons la trace de pile suivante qui est géniale :) 

```victory
Error: this is bad
    at Object.<anonymous> (/Users/dorsev/work/git/example/hello.ts:3:7)
```

Dans les versions récentes de `nodejs`, cela est supporté nativement en utilisant le drapeau [flag](https://github.com/nodejs/node/pull/29564) `--enable-source-maps`.

## Comment prendre soin de votre build (Travis) et de votre packaging

Examinons simplement les changements avant et après sur notre fichier de configuration de build.

Voici à quoi ressemblait notre fichier `.travis` avant (édition simplifiée) :

```yaml
jobs:
  include:
  - &build-and-publish
    before_script:
    - npm install --no-optional --production
    - npm prune --production
    before_deploy:
     - XZ_OPT=-0 tar --exclude=.git --exclude=reports.xml --exclude=${ARTIFACTS_MAIN_DIR}
       --exclude=.travis.yml --exclude=test -cJf "${ARTIFACTS_PATH}/${REPO_NAME}".tar.xz * .??*
  
  - &test
    before_script:
     - npm install --no-optional
    script:
     - echo "Running tests"
     - npm run lint && npm test
```

Et voici à quoi il ressemblait après :

```yaml
jobs:
  include:
  - &build-and-publish
    before_script:
    - npm install --no-optional --production
    - npm run build-dist  # Build dist folder
    - npm prune --production
    before_deploy:
     - cp -rf config/env-templates ./dist/config/
     - cp -rf node_modules ./dist/
     - cd dist
     - XZ_OPT=-0 tar --exclude=.git --exclude=reports.xml --exclude=${ARTIFACTS_MAIN_DIR} --exclude=.travis.yml --exclude=test -cJf "${REPO_NAME}.tar.xz" *
     - mv ${REPO_NAME}.tar.xz "../${ARTIFACTS_PATH}"
     - cd ..

  - &test
    before_script:
     - npm install --no-optional
     - npm run build-dist
    script:
     - echo "Running tests"
     - npm run lint && npm test
```

Remarquez que la plupart des changements concernent le "packaging" dans le fichier `tar.xz` et l'exécution de la commande `build-dist` avant d'accéder au dossier `dist`.

## Comment puis-je prendre soin du linting ?

Il existe plusieurs solutions de linting disponibles.

La première solution que nous avons utilisée était [tsfmt](https://github.com/vvakame/typescript-formatter) — mais nous avons ensuite décidé de ne pas l'utiliser car elle nécessite de maintenir deux configurations séparées pour votre projet (une pour TypeScript utilisant `tsfmt` et une séparée pour JavaScript utilisant `eslint`). Le projet semble également obsolète.

Nous avons ensuite trouvé [TSLint](https://palantir.github.io/tslint/) qui nous a redirigés vers le [plugin eslint pour TypeScript](https://github.com/typescript-eslint/typescript-eslint). Nous l'avons ensuite configuré comme suit :

Voici notre `eslintrc.js` :

```javascript
module.exports = {
    rules: {
        indent: [2, 2, {
            SwitchCase: 1
        }],
        'no-multi-spaces': 2,
        'no-trailing-spaces': 2,
        'space-before-blocks': 2,
    },
    overrides: [{
        files: ['**/*.ts'],
        parser: '@typescript-eslint/parser',
        plugins: ['@typescript-eslint'],
        extends: ['plugin:@typescript-eslint/eslint-recommended', 'plugin:@typescript-eslint/recommended']
    }]
}
```

Que nous avons configuré pour s'exécuter en utilisant une commande `lint-fix` dans notre `package.json` qui ressemble à ceci :

```json
{
    "scripts": {
        "lint-fix": "node_modules/.bin/eslint . --fix"
    },
    "pre-commit": ["lint-fix"]
}
```

## Comment "vendre" TypeScript à votre équipe de développement 

Je crois que l'un des aspects les plus critiques de l'introduction de TypeScript dans votre organisation est le "pitch" et la manière dont vous le présentez à votre équipe de développement.

Voici la [présentation](https://github.com/dorsev/typescript-talk/blob/master/typescript_meetup.md) que nous avons présentée en interne et qui tournait autour des sujets suivants :

1. Expliquer pourquoi nous pensons que TypeScript est génial
2. Qu'est-ce que TypeScript
3. Quelques exemples de code basiques. Le point principal dans cette partie n'est pas d'"enseigner" 100% TypeScript, car les gens le feront par eux-mêmes. Au lieu de cela, donnez aux gens le sentiment qu'ils peuvent lire et écrire TypeScript, et que la courbe d'apprentissage n'est pas si difficile.
4. Exemples de code avancés, comme les types Union et les types de données algébriques qui fournissent des valeurs énormes à un développeur JS. Ce sont de vrais régal, en plus du langage typé et du compilateur qui attireront vos développeurs.
5. Comment commencer à l'utiliser. Encouragez les gens à télécharger l'IDE `vs-code` et à ajouter une annotation ([//@ts-check](https://code.visualstudio.com/docs/nodejs/working-with-javascript#_type-checking-javascript)) pour qu'ils puissent commencer à voir la magie ! Dans notre entreprise, nous avons préparé à l'avance quelques erreurs vraiment cool que `ts-check` attrape, et nous avons fait une démonstration en direct (2-3 minutes) pour montrer à quelle vitesse le compilateur TypeScript peut les aider en utilisant des docs JS avec des annotations de type ou `ts-check`.
6. Plongez profondément dans certaines fonctionnalités. Expliquez les fichiers `ts.d` et les packages `@types` qui sont certaines des choses que vous rencontrerez très tôt dans vos bases de code TypeScript.
7. PR en direct de votre travail. Nous avons montré le PR que nous avons créé tôt, et avons encouragé les gens à le réviser et à l'essayer par eux-mêmes. 
8. Partagez quelques ressources cool. Il y a beaucoup de contenu en ligne, et il est difficile de distinguer le bon du mauvais. Faites une faveur à vos coéquipiers et creusez plus profondément pour essayer de trouver du contenu de qualité sur les outils que vous utilisez et dont vous avez besoin. Faites défiler jusqu'à la conclusion pour mes ressources.
9. Créez une pull request publique. Je recommande d'essayer d'obtenir autant de soutien que possible pour son approbation.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-5780-10-20-at-10.09.59-AM.png)
_Ajout de TypeScript à un projet ! Hourra !_

10. Créez un buzz positif dans votre organisation à propos du changement !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-5780-10-20-at-10.13.33-AM.png)

Je recommande vivement d'ajuster cette liste en fonction de votre équipe, de vos normes et de vos contraintes de temps.

## Conclusion

**TypeScript est super génial** ! Si vous écrivez des logiciels de qualité production et que les exigences commerciales et la disponibilité sont élevées, je vous encourage fortement à essayer TypeScript. 

**N'oubliez pas de prendre les choses une étape à la fois.** Les nouveaux langages et frameworks sont difficiles, alors prenez le temps d'apprendre et de vous éduquer, vous et votre équipe, avant de pousser ce processus vers l'avant. 

**Créez une boucle de feedback courte et une proposition de valeur.** Il est difficile de "vendre" un nouveau langage à votre équipe et à votre direction, car cela prend du temps et des ressources. 

Alors concevez votre processus de migration avec des boucles de feedback courtes, et essayez de définir des KPI clairs (moins de bugs en production, des temps de refactoring plus faciles, etc.) et assurez-vous que la proposition de valeur pour votre cas d'utilisation est constamment justifiée jusqu'à ce qu'elle devienne la norme de facto.   

**Rendez les ressources d'apprentissage facilement disponibles.** J'ai vraiment apprécié [cette](https://youtu.be/vxvQPHFJDRo) conférence sur les premiers pas avec TypeScript et [cet article de blog](https://dylanvann.com/incrementally-migrating-to-typescript/) sur la migration incrémentale vers TypeScript. 

De plus, ne manquez pas le projet `[deno](https://github.com/denoland/deno)` et le projet `[ts-node](https://github.com/TypeStrong/ts-node)`. Je suis super excité et j'ai hâte de les utiliser bientôt.