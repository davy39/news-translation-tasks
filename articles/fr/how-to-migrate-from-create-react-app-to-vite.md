---
title: Comment migrer de create-react-app vers Vite en utilisant Jest et Browserslist
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2023-10-06T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-migrate-from-create-react-app-to-vite
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-tima-miroshnichenko-5380664.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
- name: vite
  slug: vite
seo_title: Comment migrer de create-react-app vers Vite en utilisant Jest et Browserslist
seo_desc: The React team no longer recommends using create-react-app (CRA) as a bundler
  to create a new React application. The team and community realized that even though
  CRA was a jump-starter, it lacked the flexibility needed to configure or manage
  large an...
---

L'équipe React ne recommande plus d'utiliser [create-react-app (CRA)](https://github.com/facebook/create-react-app) comme bundler pour créer une nouvelle application React. L'équipe et la communauté ont réalisé que même si CRA était un bon point de départ, il manquait de flexibilité nécessaire pour configurer ou gérer des applications grandes et complexes.

De nos jours, l'équipe recommande d'utiliser des [frameworks React de qualité production](https://react.dev/learn/start-a-new-react-project#production-grade-react-frameworks) comme [NextJS](https://nextjs.org/), [Remix](https://www.freecodecamp.org/news/p/b2e8aa42-17f7-486f-9fab-b47f9704248b/Remix), [Gatsby](https://www.gatsbyjs.com/), ou [Expo](https://expo.dev/) pour les applications natives. Bien que les frameworks soient le choix préféré, l'équipe React recommande également d'utiliser [Vite](https://vitejs.dev/) ou [Parcel](https://parceljs.org/) pour des processus de build personnalisés.

Cela est en partie dû au fait que le [package CRA n'a pas été mis à jour](https://www.npmjs.com/package/create-react-app) depuis environ un an. Cela peut causer certains problèmes où des packages déjà mis à jour vers des versions plus récentes ne peuvent pas être utilisés dans une application existante. Par conséquent, vous devrez peut-être mettre à jour les applications existantes en remplaçant le package CRA par les alternatives recommandées — Vite ou Parcel.

Cet article vous guide à travers les étapes pour migrer une application basée sur la production de CRA vers Vite. Vous apprendrez le "pourquoi" de chaque étape, comment conserver `Jest` pour les tests, et comment mettre à jour votre `browserslist` puisque cela ne fonctionne pas avec `vite` directement.

Dans la section conclusion, vous pouvez trouver une demande de pull request qui inclut tous les changements. À la fin de chaque étape, vous trouverez un exemple de texte de commit qui montre le changement de code requis par étape.

## Étape 1 : Installer `Vite` et les Plugins

Voici les commandes pour installer les packages dont nous avons besoin :

```bash
yarn add vite @vitejs/plugin-react vite-tsconfig-paths

OU

npm install vite @vitejs/plugin-react vite-tsconfig-paths
```

En plus de Vite, nous ajoutons deux plugins — `@vitejs/plugin-react` et `vite-tsconfig-paths`.

Le plugin `vitejs/plugin-react` [plugin](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md#vitejsplugin-react-) active le rafraîchissement rapide en développement, utilise le runtime JSX automatique, et des plugins ou presets Babel personnalisés. Il enrichit votre expérience de développement React.

Le plugin `vite-tsconfig-paths` [plugin](https://github.com/aleclarson/vite-tsconfig-paths) résout les imports pour le mappage des chemins TypeScript. Par exemple, vous pouvez utiliser `components/ComponentName` au lieu de `./../components/ComponentName`.

### Autres plugins Vite

Un autre plugin que vous pourriez considérer est `vite-plugin-svgr`, qui [transforme](https://github.com/pd4d10/vite-plugin-svgr) les SVG en composants React et utilise [svgr](https://github.com/gregberge/svgr) sous le capot. Je l'ai laissé de côté puisque nous n'avons pas un tel cas d'utilisation dans l'application que je migre.

Vous pouvez également consulter d'autres plugins officiels de Vite [ici](https://vitejs.dev/plugins/).

[Étape 1 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/2b37990690f7898117b1a0cb89e1118451bd24d9).

## Étape 2 : Créer un fichier de configuration `Vite`

En exécutant `vite` dans le terminal de commande, Vite essaie de trouver un fichier `vite.config.ts` dans le répertoire racine du projet. Vous pouvez lire plus sur [la page de Vite](https://vitejs.dev/config/) pour savoir comment configurer davantage ce fichier pour l'[intellisense](https://vitejs.dev/config/#config-intellisense), les [configurations basées sur l'environnement](https://vitejs.dev/config/#conditional-config), la [configuration asynchrone](https://vitejs.dev/config/#async-config), et [l'utilisation des variables d'environnement](https://vitejs.dev/config/#using-environment-variables-in-config).

À la racine de votre application, créez un fichier nommé `vite.config.ts` avec le contenu suivant :

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import viteTsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
    // selon votre application, base peut aussi être "/"
    base: '',
    plugins: [react(), viteTsconfigPaths()],
    server: {    
        // cela garantit que le navigateur s'ouvre au démarrage du serveur
        open: true,
        // cela définit un port par défaut à 3000  
        port: 3000, 
    },
})
```

[Étape 2 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/557e8fbda9f8a19bf58ae0eeb1aa81e14111729a).

## Étape 3 : Créer une référence de fichier de types `Vite`

Cette étape est nécessaire pour référencer un fichier de déclarations de types qui aide aux vérifications de types et à l'Intellisense. Par défaut, les types Vite sont pour un environnement NodeJS. Pour le code côté client, [Vite fournit les définitions de types](https://vitejs.dev/guide/env-and-mode.html#intellisense-for-typescript) dans [`vite/client.d.ts`](https://github.com/vitejs/vite/blob/main/packages/vite/client.d.ts).

À la racine de votre application, créez un fichier nommé `vite-env.d.ts` avec le contenu suivant :

```js
/// <reference types="vite/client" />
```

[Étape 3 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/3002d2dbe1a421c0f31f57658ddde3030e898d1a).

## Étape 4 : Déplacer le fichier `index.html`

Vite a un [répertoire racine](https://vitejs.dev/guide/#index-html-and-project-root) à partir duquel vos fichiers sont servis. Puisque `index.html` est le point d'entrée pour le serveur de Vite, le fichier doit être dans le répertoire racine.

Depuis le répertoire public, déplacez le fichier `index.html` à la racine de votre projet.

[Étape 4 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/940f1f743fe6a380b157b86256aef7e29b2457a1).

## Étape 5 : Mettre à jour le fichier `index.html`

Deux mises à jour sont nécessaires ici :

### Supprimer `%PUBLIC_URL%`

Vite [résout automatiquement](https://vitejs.dev/guide/#index-html-and-project-root) les URLs à l'intérieur de `index.html`, donc il n'y a pas besoin de placeholders `%PUBLIC_URL%`. Vous pouvez faire une recherche et remplacer à l'intérieur de votre fichier `index.html` pour cela. Assurez-vous de supprimer toutes les occurrences.

Avant :

```html
<link rel="icon" type="image/svg+xml" href="%PUBLIC_URL%/favicon.svg" />
```

Après :

```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
```

### Ajouter le script de module à la fin de la balise body

Vite traite `index.html` [comme du code source et fait partie du graphe de modules](https://vitejs.dev/guide/#index-html-and-project-root). Il résout `<script type="module" src="...">` qui référence votre code source JavaScript.

À la fin de la balise body dans le fichier `index.html`, ajoutez le script comme montré ci-dessous :

```html
<body>
	{/* autres ici */}
	<script type="module" src="/src/index.tsx"></script>
</body>
```

[Étape 5 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/406b9765c5c166a0bafff6332f8a908156b794c4).

## Étape 6 : Remplacer CRA par `Vite`

Vous pouvez maintenant supprimer CRA, ajouter les scripts `Vite` au fichier `package.json`, et mettre à jour `tsconfig.json`.

### Supprimer CRA

Pour supprimer CRA, exécutez la commande suivante. Cela supprimera `react-scripts` de nos packages installés.

```bash
yarn remove react-scripts

OU

npm uninstall react-scripts
```

Après avoir exécuté la commande ci-dessus, supprimez le fichier `react-app-env.d.ts`.

### Ajouter les scripts Vite au fichier `package.json`

Avec Vite installé, vous pouvez utiliser le binaire `vite` dans vos scripts. Cela pourrait signifier remplacer `react-scripts` à quelques endroits. Votre attention devrait se porter sur les clés `start` et `build`. La clé `preview` est un ajout qui aide à prévisualiser la build de production localement.

Notez que `start` est `vite` et non `vite start`.

```javascript
{  
  "scripts": {
    "start": "vite", // démarrer le serveur de développement
    "build": "tsc && vite build", // build pour la production
    "preview": "vite preview" // prévisualiser localement la build de production
  }
},
```

### Mettre à jour `tsconfig.json`

Ici, votre attention devrait se porter sur `isolatedModules`, `lib`, `target`, et `types`. Pour plus d'options, voici un [fichier tsconfig d'exemple de Vite](https://github.com/vitejs/create-vite-app/blob/master/template-react-ts/tsconfig.json).

```javascript
{  
    "compilerOptions": {    
        "lib": ["dom", "dom.iterable", "esnext"],    
        "target": "ESNext",    
        "types": ["vite/client"],
        "isolatedModules": true,
    },
 }

```

### Mettre à jour `process.env.REACT_APP_VARIABLE` (optionnel)

Cela est nécessaire si votre application utilise des variables d'environnement. Vite utilise `import.meta.env.REACT_APP_VARIABLE` au lieu de `process.env.REACT_APP_VARIABLE`. Vous pouvez trouver plus de détails sur [les variables d'environnement et les modes de Vite ici](https://vitejs.dev/guide/env-and-mode.html).

Avant :

```javascript
process.env.REACT_APP_VARIABLE
```

Après :

```javascript
import.meta.env.REACT_APP_VARIABLE
```

### Remplacer `REACT_` par `VITE_` (optionnel)

Vous n'avez besoin de cela que si vous avez mis à jour `process.env` ci-dessus. Remplacez vos variables d'environnement `REACT_` pour qu'elles commencent par `VITE_`. Cela est nécessaire car Vite filtre toute variable d'environnement ne commençant pas par `VITE_`.

Avant :

```javascript
REACT_APP_API_BASE
```

Après :

```javascript
VITE_APP_API_BASE
```

[Étape 6 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/775b3e841f107c2116e46d2a94b3ca9e697561e9).

## Étape 7 : Exécuter votre Application

```bash
yarn start

OU

npm start
```

Félicitations ! Vous avez réussi la première étape de la migration de votre application de CRA vers Vite. Vous devriez voir un écran qui ressemble à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-05-at-17.21.43-1.png)

Pas d'exemple de commit. ;)

## Problèmes possibles et leurs solutions

### Erreur `global` non défini

Si vous avez cette erreur, définissez global dans votre fichier `vite.config.ts` comme montré ci-dessous :

```javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  // ...
  define: {
    // voici la principale mise à jour
    global: 'globalThis',
  },
});
```

### Si vous utilisez `@emotion/react` ou `@emotion/css`

Vous devez informer Vite à ce sujet. Pour cela, installez `@emotion/babel-plugin`.

```shell
yarn add @emotion/babel-plugin

OU

npm install @emotion/babel-plugin
```

Ensuite, mettez à jour votre plugin `react` de Vite dans le `vite.config.ts` comme montré ci-dessous :

```javscript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import viteTsconfigPaths from 'vite-tsconfig-paths';
import svgr from 'vite-plugin-svgr';

export default defineConfig({
  // ...
  plugins: [
    // voici la principale mise à jour
    react({
      jsxImportSource: '@emotion/react',
      babel: {
        plugins: ['@emotion/babel-plugin'],
      },
    }),
  ],
  // ...
});

```

### Oh non, mes tests unitaires ne fonctionnent pas !

À ce stade, essayez d'exécuter vos tests unitaires — `yarn test` ou `npm run test`. Il est possible qu'ils ne fonctionnent pas. Les étapes suivantes mettent en évidence comment vous pouvez corriger vos tests unitaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-06-at-16.20.33.png)

Vos tests unitaires ne fonctionnent pas parce que CRA utilise `react-scripts test` pour exécuter les tests, donc nous voulons passer à l'utilisation de `jest`.

## Étape 8 : Installer Jest et les dépendances liées à TypeScript

Pour commencer, vous devez installer `jest`, `ts-jest`, et `jest-environment-jsdom`. `jest` sera notre nouveau binaire pour exécuter les tests, `[ts-jest](https://www.npmjs.com/package/ts-jest)` est un transformateur avec support de source map qui vous permet d'exécuter des tests dans des projets TypeScript, et `jest-environment-jsdom` imite le comportement du navigateur pendant les exécutions de test.

```shell
yarn add -D jest @types/jest ts-jest jest-environment-jsdom

OU

npm install --save-dev jest @types/jest ts-jest jest-environment-jsdom
```

[Étape 8 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/66283764d616c4572ecd53d51ac1711f30fbe8e0).

## Étape 9 : Mettre à jour la configuration Jest

Cela dépend de votre configuration Jest actuelle. Si elle est configurée dans `package.json`, vous pouvez mettre à jour comme suit. Ici, vous vous concentrez sur `preset`, `testEnvironment`, `moduleNameMapper`, et `modulePaths`.

`preset` est défini sur `ts-jest/presets/js-with-ts` pour permettre TypeScript avec JavaScript. Vous pouvez également le définir simplement sur `ts-jest` selon votre application.

`moduleNameMapper` configure Jest pour gérer élégamment les assets tels que les feuilles de style et les images.

```json
  "jest": {
    "preset": "ts-jest/presets/js-with-ts",
    "testEnvironment": "jest-environment-jsdom",
    "moduleNameMapper": {
      "\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$": "<rootDir>/__mocks__/fileMock.js",
      "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
    },
    "modulePaths": [
      // vous pouvez mettre à jour cela pour correspondre à la configuration de votre application
      "<rootDir>/src"
    ],
  },
```

Puisque nous avons référencé un fichier dans `moduleNameMapper` ci-dessus, nous devons créer le fichier et ses fichiers correspondants. L'étape 10 s'en occupe. Cette configuration est expliquée plus en détail dans [la documentation de Jest ici](https://jestjs.io/docs/webpack#handling-static-assets).

[Étape 9 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/4383f05fce07ac1de3c80d04f581e40218f8c83b).

## Étape 10 : Ajouter le répertoire `__mocks__` à la racine de votre projet

À la racine de votre projet, créez un dossier nommé `__mocks__`.

À l'intérieur du dossier `__mocks__` créé, ajoutez un fichier nommé `styleMock.js` et ajoutez le contenu suivant :

```javascript
module.exports = {}
```

À l'intérieur du dossier `__mocks__` créé, ajoutez un fichier nommé `fileMock.js` et ajoutez le contenu suivant.

```javascript
module.exports = 'test-file-stub'
```

[Étape 10 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/d6da2a8984176041fcbfe08ca2bf0e9339fb25b4).

## Étape 11 : Mettre à jour les scripts `package.json`

Maintenant que nous avons `jest` correctement installé, nous pouvons remplacer `react-scripts tests` par `jest`. Les changements doivent être comme montré ci-dessous. Si vous n'avez pas les clés `test:coverage` ou `test:debug` dans votre code auparavant, n'hésitez pas à les ignorer.

Avant :

```json
"scripts": {
    "test": "react-scripts test",
    "test:coverage": "react-scripts test --coverage .",
    "test:debug": "react-scripts test --inspect-brk --runInBand --no-cache"
}
```

Après :

```json
"scripts": {
    "test": "jest",
    // vous pouvez ajouter cela pour garder le mode watch activé
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage .",
    "test:debug": "jest --inspect-brk --runInBand --no-cache"
}
```

[Étape 11 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/e27a66593954ffcb36d77c3e86076444a0cf82e5).

## Étape 12 : Exécuter vos Tests

```shell
yarn test

OU

npm test
```

Si vous rencontrez un problème lié à `import.meta`, vous pouvez le résoudre en déplaçant toutes vos clés d'environnement vers un seul fichier et en simulant ce fichier dans votre test. Vous pouvez [regarder ce commit](https://github.com/suretrust/stock-ticker/commit/07d15d1f000ec2cef7ec6dd01fccb43af3e67d30) pour mieux comprendre ce que je veux dire.

Pas d'exemple de commit. :)

Ah, ça marche ! Mais qu'en est-il de la configuration browserslist ?

## Qu'est-ce que la configuration browserslist ?

Il s'agit d'une configuration utilisée pour partager vos navigateurs cibles ou pris en charge parmi plusieurs dépôts frontend. 

Il existe diverses normes selon l'industrie. Par exemple, dans l'EdTech, il est possible que tous les utilisateurs apprenant en ligne utilisent des navigateurs similaires en termes de marque, de version et de taille d'écran. Cette liste des navigateurs couramment utilisés peut facilement devenir une norme pour l'industrie de l'EdTech.

Une application d'exemple de la configuration browserslist est lorsque vous devez être compatible avec des navigateurs plus anciens. Transmettre cette plage à la configuration browserslist aide votre bundler à compiler votre code en utilisant des polyfills compatibles avec vos navigateurs cibles. De cette façon, votre page a des performances optimisées avec une bonne expérience utilisateur.

[Mozilla définit un Polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill) comme un morceau de code (généralement JavaScript sur le Web) utilisé pour fournir des fonctionnalités modernes sur des navigateurs plus anciens qui ne les prennent pas en charge nativement.

La configuration browserslist est souvent définie dans le fichier `package.json` ou `.browserslistrc` comme montré ci-dessous.

### `package.json`

```javascript
{
  "browserslist": [
    "iOS >= 9",
    "Android >= 4.4",
    "last 2 versions",
    "> 0.2%",
    "not dead"
  ]
}
```

### `.browserslistrc`

```javascript
iOS >= 9
Android >= 4.4
last 2 versions
> 0.2%
not dead
```

Vous pouvez également [lire plus sur Browserslist ici](https://modernjs.dev/builder/en/guide/advanced/browserslist).

## Pourquoi `browserslist` est-il un problème avec Vite ?

Vite utilise ESBuild sous le capot qui attend un format différent du format habituel `browserslist`.

Format attendu par ESBuild : `['es2015', 'safari11', 'ios11']`

Format Browserslist : `['defaults', 'Safari >= 11', 'ios_saf >= 11']`

En raison de cette divergence, Vite ignore votre configuration `browserslist` qui se trouve actuellement dans le fichier `package.json` ou `.brwserslistrc`. 

Pour corriger cela, vous pouvez utiliser un package appelé [`browserslist-to-esbuild`](https://github.com/marcofugaro/browserslist-to-esbuild) qui effectue cette conversion sous le capot et passe la configuration à `build.target` à l'intérieur du fichier `vite.config.ts`. Les étapes 13 et 14 s'en occupent.

## Étape 13 : Installer `browserslist-to-esbuild`

```shell
yarn add browserslist-to-esbuild

OU 

npm install browserslist-to-esbuild
```

[Étape 13 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/fc7239af0a0da0b4bd844f8d17b3860b794f0ea5).

## Étape 14 : Configurer le `browserslist` dans la configuration Vite

Dans le fichier `vite.config.ts`, mettez à jour comme montré ci-dessous.

```javascript
import { defineConfig } from 'vite'
import browserslistToEsbuild from 'browserslist-to-esbuild'

export default defineConfig({
  ..
  build: {
    // --> ["chrome79", "edge92", "firefox91", "safari13.1"]
    target: browserslistToEsbuild(), 
  },
  ..
})
```

Et ensuite, vous pouvez passer vos configurations comme montré ci-dessous,

```javascript
export default defineConfig({
  ..
  build: {
    // vous pouvez également passer votre configuration browserslist habituelle ici
    target: browserslistToEsbuild([
    	'>0.2%',
    	'not dead',
    	'not op_mini all'
    ]),
  },
  ..
})
```

[Étape 14 exemple de commit](https://github.com/suretrust/stock-ticker/pull/1/commits/b8758cd4ac9e0e1d79e361b1b0097714bc6a85ae).

## Conclusion

Voilà ! Vous avez terminé et votre application est entièrement migrée.

Vous avez manqué une étape ? Voici une [demande de pull request d'exemple qui met en évidence tous les changements](https://github.com/suretrust/stock-ticker/pull/1) impliqués.

Vous avez appris le "pourquoi" et le "comment" de remplacer `create-react-app` par `Vite`. J'espère que vous êtes aussi fier de vous-même que je l'étais de moi-même pour ce que j'ai appris dans le processus de la migration.

D'accord, c'est tout ! Bon codage !