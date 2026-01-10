---
title: Comment configurer ESLint, Prettier, StyleLint et lint-staged dans Next.js
subtitle: ''
author: Naveed Ausaf
co_authors: []
series: null
date: '2024-09-16T19:43:05.417Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-eslint-prettier-stylelint-and-lint-staged-in-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726515328917/f3ecbc80-6d06-45ee-b307-89ed1a7bc854.jpeg
tags:
- name: Next.js
  slug: nextjs
- name: eslint
  slug: eslint
- name: Prettier
  slug: prettier
- name: React
  slug: reactjs
- name: Stylelint
  slug: stylelint
- name: Lint-Staged
  slug: lint-staged
seo_title: Comment configurer ESLint, Prettier, StyleLint et lint-staged dans Next.js
seo_desc: 'A linter is a tool that scans code for potential issues. This is invaluable
  with a programming language like JavaScript which is so loosely typed.

  Even for TypeScript, which is a strongly typed language whose compiler does a great
  job of detecting er...'
---

Un **linter** est un outil qui analyse le code pour détecter des problèmes potentiels. C'est inestimable avec un langage de programmation comme JavaScript qui est si faiblement typé.

Même pour TypeScript, qui est un langage fortement typé dont le compilateur fait un excellent travail de détection des erreurs au moment de la compilation, les linters tels qu'ESLint disposent de plugins qui capturent des problèmes non détectés par le compilateur.

Lorsque vous générez une nouvelle application à l'aide de la CLI Next.js (`npx create-next-app`), ESLint est configuré par défaut. Mais la configuration de linting générée par `create-next-app` présente plusieurs problèmes :

* Si vous choisissez SCSS pour le style, vous devriez utiliser [Stylelint](https://stylelint.io/) dans le processus de build pour linter les feuilles de style CSS ou SCSS. Mais il n'est pas configuré automatiquement.
    
* Si vous optez plutôt pour Tailwind pour le style, vous devriez configurer le plugin Tailwind pour ESLint. Mais là encore, cela n'est pas fait dans la configuration ESLint générée.
    
* Si vous choisissez TypeScript, alors dans Next.js v14 et versions antérieures, les règles ESLint spécifiques à TypeScript ne sont pas configurées, contrairement à [ce que stipule la documentation](https://nextjs.org/docs/pages/building-your-application/configuring/eslint#typescript). Bien qu'une application Next.js v15 les ait configurées, je peaufinerais encore la configuration avec les règles de linting plus puissantes fournies par le [projet typescript-eslint](https://typescript-eslint.io/). Celles-ci incluent la règle [no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises) qui indique si vous avez oublié d'utiliser `await` sur une méthode qui renvoie une `Promise`. Ces règles et d'autres de typescript-eslint vous feront gagner énormément de temps lors de l'écriture de votre code TypeScript.
    
* Et enfin, Prettier n'est pas configuré. Prettier est un outil de formatage de code. Il peut empêcher le code formaté de manière incohérente d'entrer dans le dépôt de code, ce qui rendrait difficiles les comparaisons entre différentes versions d'un même fichier. De plus, un code bien formaté est plus facile à manipuler. C'est donc une omission assez importante.
    

Dans ce tutoriel, je vais vous montrer comment je configure le linting et le formatage dans mes projets Next.js de manière à résoudre les problèmes mentionnés ci-dessus. Je vous apprendrai également comment installer et configurer certaines extensions VS Code associées pour l'assistance au codage.

Pour suivre, vous pouvez soit utiliser un projet Next.js que vous avez déjà, soit générer une nouvelle application en exécutant `npx create-next-app` dans le terminal.

Si vous générez une nouvelle application, vos choix vous appartiennent (les valeurs par défaut conviennent), mais assurez-vous de choisir OUI en réponse à la question demandant si vous souhaitez utiliser ESLint :

![Fenêtre de terminal dans laquelle le générateur Next.js, create-next-app, affiche les options de génération de code à l'utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1725930860799/fb38b3b2-5592-4eb4-b8d0-153aeb2d749d.png align="center")

Si vous suivez avec une application existante plutôt qu'une nouvelle, mettez-la à jour en exécutant la [commande suivante](https://nextjs.org/docs/pages/building-your-application/upgrading/version-14) à la racine de l'application :

```bash
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
npm i --save-dev eslint
```

Cela évitera les conflits de version par la suite.

Si vous ne pouvez pas passer à la dernière version, vous devrez spécifier les versions des packages qui seront installés dans ce tutoriel pour contourner tout conflit de version. Soyez averti que cela peut être frustrant.

Maintenant, vous êtes prêt à ouvrir l'application dans votre éditeur de code et à procéder comme suit.

**NOTE SUR LE MONOREPO :** Un monorepo est un dépôt Git qui contient plusieurs projets, chacun dans son propre sous-dossier. Par exemple, [ce dépôt](https://github.com/naveedausaf/flowmazondotnet) est pour une solution full-stack qui contient deux projets : une application Next.js dans le dossier `flowmazonfrontend` et un projet d'API .NET Core dans le dossier `flowmazonbackend` :

![Capture d'écran du dépôt](https://cdn.hashnode.com/res/hashnode/image/upload/v1743632328084/670c756d-a5f9-4333-80dc-446b3a5975bb.png align="center")

Si votre application Next.js est contenue dans un monorepo contenant à la fois une application Next.js et d'autres projets, **je** recommande d'effectuer toute la configuration ci-dessous dans le dossier de l'application Next.js. C'est ce dossier que vous devriez ouvrir dans votre éditeur de code et dans lequel vous devriez faire un `cd` dans le terminal. Il y a une partie de la configuration (lint-staged et Husky) qui devra être faite dans le dossier racine du monorepo. Je l'indiquerai en temps voulu.

## Prérequis

Pour ce tutoriel, je suppose que vous savez comment :

* écrire une application Next.js de base avec deux pages ou plus.
    
* installer des packages NPM supplémentaires dans votre application.
    

## Table des matières

* [Introduction](#heading-introduction)
    
* [Prérequis](#heading-prerequis)
    
* [Table des matières](#heading-table-des-matieres)
    
* [Configurer Prettier](#heading-configurer-prettier)
    
    * [Une note sur les fins de ligne dans Prettier](#heading-une-note-sur-les-fins-de-ligne-dans-prettier)
        
* [Configurer ESLint](#heading-configurer-eslint)
    
    * [Les bases de la configuration ESLint](#heading-les-bases-de-la-configuration-eslint)
        
    * [Configuration ESLint pour TypeScript](#heading-configuration-eslint-pour-typescript)
        
    * [Configuration ESLint pour Tailwind](#heading-configuration-eslint-pour-tailwind)
        
    * [Configuration ESLint pour Prettier](#heading-configuration-eslint-pour-prettier)
        
* [Configurer Stylelint](#heading-configurer-stylelint)
    
* [Configurer les scripts package.json](#heading-configurer-les-scripts-packagejson)
    
* [Configurer lint-staged](#heading-configurer-lint-staged)
    
* [Configurer les extensions VS Code](#heading-configurer-les-extensions-vs-code)
    
* [Vérifications finales et dépannage](#heading-verifications-finales-et-depannage)
    
* [Conclusion](#heading-conclusion)
    

## Configurer Prettier

[Prettier](https://prettier.io/) est un formateur de code opiniâtre qui peut formater presque n'importe quel fichier (`.html`, `.json`, `.js`, `.ts`, `.css`, `.scss`, etc.).

Configurez-le dans votre application comme suit :

1. Installez Prettier :
    
    ```bash
    npm install --save-dev prettier
    ```
    
2. Si vous avez choisi Tailwind pour le style lors de la génération de l'application, installez alors `prettier-plugin-tailwindcss` :
    
    ```bash
      npm install --save-dev prettier-plugin-tailwindcss
    ```
    
    Ce package est un plugin Prettier et fournit des règles pour réorganiser les classes Tailwind utilisées dans un attribut `class` ou `className` selon un ordre canonique. Cela aide à maintenir la cohérence de l'ordre des classes Tailwind utilisées dans le balisage.
    
    %[https://youtu.be/tQkBJXwzY8A?autoplay=1] 
    
3. Créez `.prettierrc.json` à la racine de votre projet. Si vous utilisez SCSS pour le style, collez l'extrait suivant dans ce fichier :
    
    ```json
    {
      "singleQuote": true,
      "jsxSingleQuote": true
    }
    ```
    
    Si vous utilisez plutôt Tailwind, collez ce qui suit dans `.prettierrc.json` :
    
    ```json
    {
      "plugins": ["prettier-plugin-tailwindcss"],
      "singleQuote": true,
      "jsxSingleQuote": true
    }
    ```
    
4. Créez le fichier `.prettierignore` à la racine de l'application, avec le contenu suivant :
    
    ```plaintext
    node_modules
    .next
    .husky
    coverage
    .prettierignore
    .stylelintignore
    .eslintignore
    stories
    storybook-static
    *.log
    playwright-report
    .nyc_output
    test-results
    junit.xml
    docs
    ```
    
    Ce fichier garantit que les fichiers qui ne sont pas du code d'application (c'est-à-dire ceux qui ne sont pas des fichiers `.js`, `.ts`, `.css`, etc.) ne sont pas formatés. Sinon, Prettier finirait par passer trop de temps à traiter des fichiers dont le formatage ne vous importe pas vraiment.
    
    `.prettierignore` (le fichier que nous venons de créer), `.eslintignore` et `.stylelintignore` ont été ignorés car ce sont des fichiers texte brut sans structure, et Prettier se plaindrait de ne pas pouvoir les formater.
    
5. Enfin, **je recommande** de suivre les étapes de [cet article](https://nausaf.hashnode.dev/lf-vs-crlf-configure-git-and-vs-code-on-windows-to-use-unix-line-endings) pour définir LF comme caractère de fin de ligne (EOL), à la fois dans le dépôt et dans vos paramètres VS Code. Le raisonnement pour cela est donné dans la sous-section suivante.
    

### Une note sur les fins de ligne dans Prettier

Prettier [utilise par défaut LF (Line Feed) pour les fins de ligne](https://prettier.io/docs/en/options#end-of-line). Cela signifie que lorsqu'il formate des fichiers, il changera toutes les occurrences de la séquence de caractères CRLF, le cas échéant, en LF.

LF est également la valeur par défaut dans les éditeurs de texte et autres outils sur les systèmes basés sur Unix (Linux, MacOS, etc.). Mais sous Windows, la valeur par défaut pour les fins de ligne est CRLF (Carriage Return suivi de Line Feed).

Les outils Windows tels que les éditeurs de texte et de code peuvent facilement gérer LF comme fin de ligne. Mais CRLF peut être problématique pour les outils sur les systèmes basés sur Unix. Par conséquent, il est logique de n'utiliser que LF comme fin de ligne dans le code, car cela fonctionnerait sur les systèmes Windows et basés sur Unix.

Configurer LF comme caractère EOF dans le dépôt Git et dans les éditeurs de code alignera vos outils sur les paramètres par défaut de Prettier. Cela garantira également que tous les fichiers du dépôt Git ont systématiquement des fins de ligne LF. Ainsi, si un contributeur à votre dépôt est sous Windows (qui utilise CRLF), le code qu'il ajoute ou modifie utiliserait toujours LF : l'éditeur de code créerait les nouveaux fichiers en LF par défaut ; `git commit` convertirait les CRLF éventuels en LF lors du commit.

Enfin, définir LF pour tout le dépôt éviterait les comportements étranges qui surviennent sous Windows lorsque Prettier conserve son réglage par défaut LF mais que Git et votre éditeur continuent d'utiliser CRLF :

* Lorsque l'extension VS Code Prettier formate un fichier (par exemple, configurée sur "autoformat on save"), elle ne modifie pas les fins de ligne CRLF. Mais formater le même fichier en exécutant Prettier via la ligne de commande **change les fins de ligne en LF**. Cette divergence peut être agaçante.
    
* Git peut afficher des avertissements comme celui-ci lorsque vous exécutez `git add .` :
    
    ![Avertissements affichés par la commande git add lorsque certains fichiers contiennent LF mais que la valeur par défaut du dépôt est CRLF](https://cdn.hashnode.com/res/hashnode/image/upload/v1725930986122/b5630966-e8dd-4f47-bb58-eed6eb023ea6.png align="center")
    

## Configurer ESLint

### Les bases de la configuration ESLint

ESLint est livré avec un certain nombre de règles de linting prêtes à l'emploi. Mais vous pouvez également les compléter avec des plugins ESLint.

Un **plugin ESLint** définit certaines règles de linting. Par exemple, si vous regardez dans le [dépôt GitHub du plugin ESLint pour Next](https://github.com/vercel/next.js/tree/canary/packages/eslint-plugin-next), eslint-plugin-next, chaque fichier du dossier [`src/rules`](https://github.com/vercel/next.js/tree/canary/packages/eslint-plugin-next/src/rules) définit une règle de linting comme une fonction TypeScript. Le fichier [`index.js`](https://github.com/vercel/next.js/blob/canary/packages/eslint-plugin-next/src/index.ts) du package exporte ensuite ces fonctions de règle dans l'objet `rules` de son export par défaut :

```typescript
module.exports = {
  rules: {
    'google-font-display': require('./rules/google-font-display'),
    'google-font-preconnect': require('./rules/google-font-preconnect'),
    'inline-script-id': require('./rules/inline-script-id'),
    ...
```

La manière basique d'utiliser ces règles dans votre application est d'installer le package du plugin, puis de le référencer dans le fichier de configuration ESLint à la racine de l'application.

Par exemple, nous pouvons utiliser les règles de `eslint-plugin-next` mentionnées ci-dessus en exécutant `npm install --save-dev eslint-plugin-next`, puis en plaçant le contenu suivant dans le fichier de config ESLint `.eslintrc.json` à la racine :

```json
{
	"plugins": ["next"],
	"rules": {
		"google-font-display": "warning",
	    "google-font-preconnect": "warning",
	    "inline-script-id": "error"
	}
}
```

Si vous exécutez maintenant `npx eslint .` à la racine de votre application, ESLint analysera chaque fichier JavaScript par rapport aux trois règles configurées ci-dessus.

Il existe trois niveaux de sévérité que vous pouvez attribuer à une règle : `off`, `warning` et `error`. Comme le montre l'extrait ci-dessus, vous activez une règle en lui attribuant une sévérité `warning` ou `error` dans le fichier `.eslintrc.json` de l'application.

Lors de la référence à un plugin dans le fichier de configuration ESLint, le préfixe `eslint-plugin-` dans le nom du package du plugin est omis. C'est pourquoi le package `eslint-plugin-next` n'est référencé que par `"next"` dans l'extrait ci-dessus.

Puisqu'il est assez fastidieux de configurer un niveau de sévérité pour chaque règle de chaque plugin, la norme est de référencer une [configuration partageable ESLint](https://eslint.org/docs/latest/extend/shareable-configs), ou **config** pour faire court, exportée par un package NPM. C'est un objet JavaScript qui déclare des plugins et configure des règles avec des niveaux de sévérité, comme nous l'avons fait ci-dessus.

Par exemple, l'export par défaut de `eslint-plugin-next` contient également plusieurs configs ESLint. Voici un autre extrait de l'[`index.js` du plugin](https://github.com/vercel/next.js/blob/canary/packages/eslint-plugin-next/src/index.ts), montrant cette fois les configs exportées :

```typescript
module.exports = {
  rules: {
    'google-font-display': require('./rules/google-font-display'),
    'google-font-preconnect': require('./rules/google-font-preconnect'),
    'inline-script-id': require('./rules/inline-script-id'),
    ...
},
configs: {
    recommended: {
      plugins: ['@next/next'],
      rules: {
        // avertissements
        '@next/next/google-font-display': 'warn',
        '@next/next/google-font-preconnect': 'warn',
        ...

        // erreurs
        '@next/next/inline-script-id': 'error',
        '@next/next/no-assign-module-variable': 'error'
        ...

      }
    },
    'core-web-vitals': {
      plugins: ['@next/next'],
      extends: ['plugin:@next/next/recommended'],
      rules: {
        '@next/next/no-html-link-for-pages': 'error',
        '@next/next/no-sync-scripts': 'error',
      },
    },
}
```

Comme vous pouvez le voir, le plugin exporte deux configs - `recommended` et `core-web-vitals` - qui activent différentes sélections de règles.

La config normalement utilisée dans les projets Next.js est `core-web-vitals`. Nous pouvons l'utiliser dans le fichier `.eslintrc.json` de notre application comme ceci :

```json
{
  "extends": ["plugin:next/core-web-vitals"]
}
```

C'est beaucoup plus simple que de déclarer le plugin et d'assigner une sévérité à chaque règle.

Notez la différence entre *Fichier de Configuration* – il s'agit du fichier nommé `.eslintrc.json` – et *Config Partageable* – il s'agit d'un objet qui configure certaines règles pour une utilisation dans un projet client.

Le contenu du fichier de configuration est lui-même une config. Mais nous importons presque toujours un objet de config bien connu exporté par un package NPM, appelé [shareable config](https://eslint.org/docs/latest/extend/shareable-configs).

En plus des plugins, d'autres packages dont le nom commence par `eslint-config-` (contrairement à `eslint-plugin-`) peuvent fournir des configs. Next.js fournit un tel package nommé `eslint-config-next`. Il réexporte les configs `recommended` et `core-web-vitals` du plugin. Il réexporte également (en v15+) une config de règles TypeScript. Ainsi, au lieu d'utiliser `plugin:next/core-web-vitals`, nous pourrions utiliser :

```json
{
  "extends": ["next/core-web-vitals"]
}
```

Puisque le nom du package n'est pas préfixé par `plugin:`, ESLint le considère comme un package de config, reconstruisant le nom comme `eslint-config-next`. Notez que nous supprimons le préfixe `eslint-config-` lors du référencement.

**NOTE :** Pour référencer une config d'un **plugin** ESLint, il est d'usage de déclarer également le plugin dans le tableau `"plugins"`. Par exemple, pour `eslint-plugin-storybook` :

```json
{
    "plugins": ["storybook"],
    "extends": ["plugin:storybook/recommended"]
}
```

Il est possible de référencer plusieurs configs dans `extends`. Dans ce cas, toutes les règles sont utilisées. En cas de conflit de nom, c'est la dernière config (de gauche à droite) qui l'emporte.

ESLint propose également un nouveau format souvent appelé [flat config](https://eslint.org/docs/latest/use/configure/configuration-files) (non utilisé ici) où les fichiers sont en JavaScript ou TypeScript.

### Configuration ESLint pour TypeScript

**Si votre application utilise TypeScript**, modifiez le fichier de configuration ESLint (.eslintrc.js) comme suit :

1. Dans le terminal, à la racine de l'application, exécutez :
    
    ```bash
    npm install --save-dev @typescript-eslint/parser @typescript-eslint/eslint-plugin typescript
    ```
    
    `@typescript-eslint/eslint-plugin` fournit des règles pour les fichiers TypeScript, et `@typescript-eslint/parser` permet à ESLint d'analyser les fichiers TypeScript.
    
2. Renommez `.eslintrc.json` en `.eslintrc.js` et remplacez son contenu par :
    
    ```javascript
    /* eslint-env node */
    module.exports = {
      root: true,
      extends: [
        'next/core-web-vitals',
      ],
      plugins: ['@typescript-eslint', 'tailwindcss'],
      parser: '@typescript-eslint/parser',
      overrides: [
        {
          files: ['*.ts', '*.tsx'],
          parserOptions: {
            project: ['./tsconfig.json'],
            projectService: true,
            tsconfigRootDir: __dirname,
          },
          extends: [
            'next/core-web-vitals',
            'plugin:@typescript-eslint/recommended',
            //'plugin:@typescript-eslint/recommended-type-checked',
            // 'plugin:@typescript-eslint/strict-type-checked',
            // 'plugin:@typescript-eslint/stylistic-type-checked',
          ]
        },
      ],
    };
    ```
    
    **Voici ce que font les différentes lignes de ce fichier :**
    
    `/* eslint-env node */` empêche ESLint de se plaindre qu'il s'agit d'un module CommonJS.
    
    `root: true` indique qu'il s'agit du fichier de configuration ESLint principal.
    
    `extends:` spécifie les différentes configs ESLint.
    
    `'next/core-web-vitals'` est une config fournie par `eslint-config-next` pour Next.js.
    
    La config `recommended-type-checked` (utilisée dans `overrides`) est fournie par `@typescript-eslint/eslint-plugin`. Elle ajoute des règles de linting qui utilisent l'API de vérification de type de TypeScript.
    
    `parser: '@typescript-eslint/parser'` spécifie l'analyseur TypeScript pour ESLint.
    
    `parserOptions:` indique à l'analyseur où trouver le fichier `tsconfig.json`.
    
    La section `overrides` garantit que les options de l'analyseur TypeScript ne s'appliquent qu'aux extensions `.ts` et `.tsx`. Sinon, l'exécution d'ESLint jetterait des erreurs sur les fichiers `.js` comme `.eslintrc.js` lui-même.

### Configuration ESLint pour Tailwind

**Si votre application utilise Tailwind,** modifiez la config comme suit :

1. Dans le terminal, exécutez `npm install --save-dev eslint-plugin-tailwindcss`.
    
2. Dans la config ESLint, ajoutez `"plugin:tailwindcss/recommended"` à la FIN de `extends`.
    
3. Ajoutez `"tailwindcss"` à `plugins` et ajoutez un objet `rules` :
    
    ```json
    {
      "plugins": [..., "tailwindcss"],
      "rules": {
        "tailwindcss/classnames-order": "off"
      }
    }
    ```
    
4. **Si votre application utilise TYPESCRIPT**, ajoutez également `"plugin:tailwindcss/recommended"` à l'élément `extends` interne dans `overrides` et dupliquez l'objet `rules` à l'intérieur d' `overrides`.

`eslint-plugin-tailwindcss` vérifie que les classes CSS utilisées sont bien des classes Tailwind. Nous désactivons `tailwindcss/classnames-order` car nous utilisons déjà `prettier-plugin-tailwindcss` pour gérer l'ordre des classes.

### Configuration ESLint pour Prettier

1. Exécutez : `npm install --save-dev eslint-config-prettier`.
    
2. Dans la config ESLint, ajoutez `"prettier"` à la FIN de `extends`.
    
3. **Si votre application utilise TypeScript**, ajoutez-le également au `extends` interne d' `overrides`.

Cette config désactive les règles ESLint qui entrent en conflit avec le formatage de Prettier. Elle doit être la dernière dans `extends`.

4. Créez `.eslintignore` à la racine pour ignorer les dossiers ou fichiers futurs.

## Configurer Stylelint

Stylelint est un linter pour CSS et SCSS.

**Si vous utilisez SCSS et NON Tailwind :**

1. Installez sass : `npm install --save-dev sass`.
    
2. Installez Stylelint et ses configs :
    
    ```bash
    npm install --save-dev stylelint stylelint-config-standard-scss stylelint-config-prettier-scss
    ```
    
3. Créez `.stylelintrc.json` à la racine :
    
    ```json
    {
      "extends": [
        "stylelint-config-standard-scss",
        "stylelint-config-prettier-scss"
      ],
      "rules": {
        "selector-class-pattern": null
      }
    }
    ```

4. Créez `.stylelintignore` :
    
    ```json
    styles/globals.css
    styles/Home.module.css
    coverage
    ```

## Configurer les scripts `package.json`

1. Modifiez le script `"build"` pour inclure Prettier et Stylelint :

    **Si vous utilisez Tailwind :** `"build": "prettier --check . && next build"`.
    
    **Si vous utilisez SCSS :** `"build": "prettier --check . && stylelint --allow-empty-input \"**/*.{css,scss}\" && next build"`.

2. Ajoutez un script `"format"` : `"format": "prettier --write ."`.

3. Ajoutez un script `"build:local"` utilisant `prettier --write .` pour formater et builder localement.

## Configurer lint-staged

[lint-staged](https://github.com/okonet/lint-staged) permet d'exécuter des commandes sur les fichiers indexés (staged) de Git. [Husky](https://github.com/typicode/husky) permet de déclencher ces commandes via des hooks Git.

Je préfère n'exécuter que `prettier --check .` sur les fichiers indexés pour m'assurer qu'ils sont bien formatés avant le commit, sans modifier le code automatiquement ni ralentir le processus avec un build complet.

1. Installez lint-staged : `npm install --save-dev lint-staged`.
    
2. Créez `lint-staged.config.js` :
    
    ```javascript
    /* eslint-env node */
    const path = require('path');
    const formatCommand = 'prettier . --check';
    
    module.exports = {
      '*': formatCommand,
    };
    ```

3. Pour un monorepo, ajustez les chemins dans `lint-staged.config.js` pour pointer vers le sous-dossier de l'application.

4. Installez Husky et configurez le hook pre-commit :
    
    ```bash
    npm install --save-dev husky
    npx husky init
    echo "npx lint-staged" > .husky/pre-commit
    ```

## Configurer les extensions VS Code

Installez les extensions suivantes : **ESLint**, **Prettier**, **Stylelint** et **TailwindCSS**.

Ajoutez ceci à `.vscode/settings.json` :

```json
{
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[scss]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "stylelint.validate": ["css", "scss"],
  "editor.formatOnSave": true,
  "eslint.useFlatConfig": false
}
```

## Vérifications finales et dépannage

Exécutez `npm run format`, `npm run build`, puis commitez vos changements. Si vous avez des erreurs :

* Vérifiez vos fichiers `*ignore`.
* Ajoutez des plugins Prettier spécifiques si nécessaire (ex: `prettier-plugin-gherkin`).
* Si TypeScript est trop strict, vous pouvez repasser de `recommended-type-checked` à `recommended`.
* Vous pouvez désactiver une règle localement avec un commentaire `/* eslint-disable rule-name */`.

## Conclusion

Ce tutoriel vous a montré comment configurer les outils de linting et de formatage dans votre application Next.js. J'espère qu'il vous a également donné les bases nécessaires pour comprendre et personnaliser ces configurations selon vos besoins.