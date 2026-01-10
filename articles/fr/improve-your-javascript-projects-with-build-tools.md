---
title: Comment améliorer votre code JavaScript avec des configurations d'outils de
  build puissants
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2024-07-02T15:56:38.000Z'
originalURL: https://freecodecamp.org/news/improve-your-javascript-projects-with-build-tools
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/aaron-burden-4eWwSxaDhe4-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment améliorer votre code JavaScript avec des configurations d'outils
  de build puissants
seo_desc: I have been a frontend developer for over 6 years now, mostly working with
  Javascript, TypeScript, and React. When stepping into the world of the front end,
  the number of libraries and build tools available can be overwhelming – especially
  since each...
---

Je suis développeur frontend depuis plus de 6 ans, travaillant principalement avec JavaScript, TypeScript et React. En entrant dans le monde du développement frontend, le nombre de bibliothèques et d'outils de build disponibles peut être écrasant – surtout puisque chacun a ses propres options de configuration.

Au début, ces choix de configuration peuvent sembler une sorte de magie. Mais une fois que vous commencez à comprendre leur but, il devient clair que ces configurations ont du sens.

Des outils tels que ESLint, Prettier, les hooks Git et autres peuvent vous aider à maintenir votre code efficacement et judicieusement. Dans cet article, nous allons plonger dans ces outils qui rendent votre code maintenable et qui peuvent aider à booster votre productivité (et celle de votre équipe) également.

Alors sans plus attendre, commençons.

## Table des matières :

* [Prérequis](#heading-prerequisites)
* [Quels outils et configurations examinons-nous ?](#heading-what-tools-and-configs-are-we-looking-at)
* [Pourquoi ces conventions sont utiles](#heading-why-these-conventions-are-useful)
* [Comment configurer les conventions de codage](#heading-how-to-setup-coding-conventions)
* [Qu'est-ce qu'ESLint ?](#heading-what-is-eslint)
* [Qu'est-ce que les hooks Git ?](#heading-what-are-git-hooks)
* [Configurer le projet](#heading-set-up-the-project)
* [Règle #1 : `no-unused-vars`](#heading-rule-1-no-unused-vars)
* [Règle #2 : `no-console`](#heading-rule-2-no-console)
* [Règle #3 : `no-duplicate-imports` et tri des imports](#heading-rule-3-no-duplicate-imports-and-sorting-imports)
* [Comment configurer les hooks Git](#heading-how-to-set-up-git-hooks)
* [Gitleaks : Supprimer les secrets avant les commits](#heading-gitleaks-remove-secrets-before-commits)
* [Exécuter les tests unitaires avant les commits](#heading-run-unit-tests-before-commits)
* [Résumé](#heading-summary)

## Prérequis

Avoir quelques connaissances sur les sujets suivants peut vous aider à tirer des enseignements de cet article. Je vous recommande donc vivement de parcourir les ressources suivantes (ou de vous assurer que vous êtes familier avec les outils/concepts listés) :

* Les bases d'[ESLint](https://eslint.org/docs/latest/use/core-concepts/)
* Configurer un simple projet JS avec [npm](https://docs.npmjs.com/cli/v10/commands/npm-init) ou [yarn](https://classic.yarnpkg.com/lang/en/docs/cli/init/)
* [Scripting Bash](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/)
* [Tester le code avec Jest](https://www.youtube.com/watch?v=IPiUDhwnZxA)

## Quels outils et configurations examinons-nous ?

J'ai vu de nombreux dépôts qui appliquent leurs propres conventions strictes – et je suis totalement d'accord avec eux. Un exemple que j'ai trouvé est le [dépôt Cesium](https://github.com/CesiumGS/cesium) et [leurs guides de style](https://github.com/CesiumGS/cesium/blob/main/Documentation/Contributors/CodingGuide/README.md#coding-guide).

En s'inspirant de divers autres dépôts, nous allons plonger dans les directives suivantes dans cet article pour vous aider à avoir une meilleure expérience de développeur :

* Pas de déclarations console
* Pas d'imports et de variables inutilisés
* Tri des déclarations d'import
* Vérifier si des mots de passe, des clés API ou des secrets sont poussés avant un commit
* Vérifier si des tests échouent avant de pousser un commit

### Pourquoi ces conventions sont utiles

J'ai trouvé ces règles utiles car elles augmentent votre productivité en tant que développeur. Elles alignent également les équipes de développement afin que tout le monde suive les mêmes conventions/normes de codage.

Ces conventions m'ont également rendu vigilant quant à l'écriture de bon code et au respect des normes de codage. Maintenant, cela est devenu une habitude pour moi de penser en ces termes et normes car, par exemple, avoir des imports inutilisés et des déclarations console encombre votre code inutilement.

Je trouve que le tri des imports les rend plus lisibles et faciles à gérer. J'ai maintenant l'habitude de regarder les imports dans un composant React en fonction de :

* Imports de bibliothèques
* Imports relatifs

J'ai également trouvé que les outils qui vérifient si des mots de passe ou des secrets sont poussés sont super utiles, car ils peuvent apparaître plus tard dans l'historique des commits.

Mais avant tout, j'aime avoir une règle pour vérifier si des tests échouent ou non avant de faire un commit. Je crois que c'est une stratégie très intelligente, car dans ce cas, vous vérifiez au préalable les échecs des tests unitaires – donc vous saurez si quelque chose doit être corrigé. Cela évite également de surcharger les pipelines CI que vous exécutez sur les dépôts distants.

## Comment configurer les conventions de codage

Avant de plonger dans l'incorporation de ces outils dans votre projet, je souhaite les catégoriser comme suit :

* Règles basées sur ESLint
* Hooks Git

Commençons par comprendre ces catégories.

### Qu'est-ce qu'ESLint ?

ESLint est un linter JavaScript hautement configurable qui vous aide à détecter et à corriger les problèmes dans votre code JavaScript. Chaque configuration, des plugins aux règles et plus encore, est vérifiée par rapport à votre code et applique la valeur par rapport à cette règle si la condition est remplie.

Vous pouvez en savoir plus sur les concepts de base d'ESLint [ici](https://eslint.org/docs/latest/use/core-concepts/).

### Qu'est-ce que les hooks Git ?

Les hooks Git sont une fonctionnalité de Git qui aide Git à s'intégrer dans ses flux de travail afin que certaines actions personnalisées puissent être effectuées en fonction de certains événements. Par exemple, vous pouvez exécuter un script qui va formater certains changements avant de faire un commit.

Il existe plusieurs hooks Git locaux disponibles pour vous. Certains d'entre eux sont ci-dessous :

```
applypatch-msg.sample       pre-push.sample
commit-msg.sample           pre-rebase.sample
post-update.sample          prepare-commit-msg.sample
pre-applypatch.sample       update.sample
pre-commit.sample

```

Vous pouvez en savoir plus sur les hooks Git [ici](https://www.atlassian.com/git/tutorials/git-hooks).

Maintenant que nous savons pourquoi nous divisons ces conventions en ces catégories, commençons notre voyage de compréhension des règles et outils que vous allez apprendre et que vous pouvez utiliser dans vos projets.

## Configurer le projet

Pour démontrer toutes les règles et outils dont nous avons discuté ci-dessus, nous aurons besoin d'un simple projet JavaScript vanilla. J'ai choisi un projet JS vanilla car créer un projet Vite basé sur React serait excessif pour ce guide.

Pour commencer à créer le projet, créez d'abord un répertoire nommé `eslint-hook-examples` avec la commande suivante :

```bash
mkdir eslint-hook-examples
cd eslint-hook-examples

```

À l'intérieur de ce dossier, exécutez la commande suivante pour initialiser un projet JS vanilla :

```bash
yarn init

```

Répondez à la question posée dans l'invite et vous devriez être prêt à partir.

Maintenant, créons un fichier nommé `index.js` à l'intérieur de ce projet et plaçons le contenu suivant à l'intérieur :

```jsx
import { get, debounce } from "lodash";
import { throttle } from "lodash";

const num = 1;
const x = 2;

console.log({ num });


```

J'ai créé le code ci-dessus en gardant à l'esprit que je veux démontrer différentes règles ESLint et hooks Git.

Maintenant, vous devez ajouter ESLint à votre projet. Vous pouvez le faire en exécutant la commande suivante :

```bash
yarn add --dev eslint @eslint/js

```

Ensuite, vous devez créer un fichier nommé `eslint.config.js` dans votre répertoire racine – c'est-à-dire, là où vous avez votre fichier `package.json`. Placez le contenu suivant à l'intérieur de ce fichier :

```jsx
import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    rules: {
      "no-unused-vars": "warn",
    },
  },
];


```

ESLint fonctionne sur les fichiers de configuration que nous définissons dans le fichier `eslint.config.js`. Ce format de configurations est appelé une configuration de fichier plat. Cela est maintenant pris en charge avec les nouvelles versions d'ESLint, supérieures à la v 9. Les versions inférieures à 9 utilisent une convention de nommage de fichier différente `.eslintrc` qui est placée à l'intérieur du répertoire racine du projet.

Vous pouvez en savoir plus sur la configuration de fichier plat [ici](https://eslint.org/docs/latest/use/configure/configuration-files).

Le contenu ci-dessus du fichier `eslint.config.js` charge les configurations recommandées pour JavaScript avec l'aide de `js.configs.recommended`. Il introduit également un autre objet qui définit les `rules` que cette configuration active.

Pour l'instant, il active [no-unused-vars](https://eslint.org/docs/latest/rules/no-unused-vars#rule-details) qui est défini sur une valeur `warn`. Cette valeur `warn` indique à ESLint d'afficher un message d'avertissement lors du linting. Vous pouvez également définir cette valeur sur `error` si vous voulez que le linter affiche ce cas comme une erreur.

```jsx
import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    rules: {
      "no-unused-vars": "error",
    },
  },
];


```

Donnons un essai à cette configuration et exécutons notre ESLinting sur le fichier `index.js`. Pour ce faire, exécutez la commande suivante :

```shell
npx eslint ./index.js
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image.png)
_Sortie de l'exécution de la CLI ESLint_

Après avoir exécuté le linter, vous obtiendrez les problèmes ci-dessus. Toutes nos variables inutilisées sont signalées sous la règle `no-unused-vars` que vous avez définie dans votre fichier `eslint-config.js`.

C'est ainsi que fonctionne le linting. Mais ne serait-ce pas génial si vous pouviez obtenir ces messages d'erreur dans votre IDE lui-même avec une ligne ondulée sous chaque nom de variable qui est inutilisé ? Eh bien, oui – c'est absolument possible. Dans VS Code, vous pouvez le faire en ajoutant l'[extension ESLint VS code](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint).

Une fois l'extension installée dans votre VS Code, vous voudrez la configurer pour qu'elle prenne le fichier de configuration que vous avez créé (`eslint.config.js`).

Pour configurer votre extension, suivez le gif/les étapes ci-dessous pour passer par les paramètres de l'extension.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/eslint_settings-3.gif)
_Extension VSCode ESLint_

* Cliquez sur l'extension VSCode
* Cliquez sur l'extension ESLint
* Ensuite, sous le nom de l'extension, cliquez sur l'icône d'engrenage 🔩.
* Ensuite, cliquez sur les paramètres de l'extension dans le menu déroulant
* Enfin, cliquez sur `settings.json`.

À l'intérieur du fichier `settings.json`, ajoutez le code suivant en bas du fichier :

```jsx
"eslint.options": {
		 "overrideConfigFile": "./eslint.config.js" 
	},

```

Cela garantit que l'extension prend le fichier de configuration que vous avez créé à l'emplacement racine du projet.

Une chose rapide à noter est que toutes les règles peuvent également être définies sur `warn` afin que VSCode puisse donner des avertissements de linting lorsque la règle est respectée.

Voici à quoi ressemble l'extension configurée sur un fichier :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-2.png)
_Linter lorsqu'il est configuré_

Plongeons maintenant dans notre première règle : la règle `no unused variable`.

## Règle #1 : `no-unused-vars`

![Image](https://www.freecodecamp.org/news/content/images/2024/07/rule_1_banner.jpg)
_Photo par [Unsplash](https://unsplash.com/@v2osk?utm_content=creditCopyText&amp;utm_medium=referral&amp;utm_source=unsplash">v2osk</a> sur <a href="https://unsplash.com/photos/assorted-armchair-on-wall-near-door-1hUY8SpJ8Cw?utm_content=creditCopyText&amp;utm_medium=referral&amp;utm_source=unsplash)_

C'est l'une de ces règles ESLint qui ne vous permet pas de garder des variables inutilisées dans votre base de code. Vous pouvez en savoir plus sur cette règle [ici](https://eslint.org/docs/latest/rules/no-unused-vars#rule-details).

Pour configurer cette règle dans votre base de code, vous l'ajouterez dans la section `rules` du fichier `eslint.config.js` :

```jsx
export default [
  {
    rules: {
      "no-unused-vars": "error",
    },
  },
];

```

Nous avons déjà vu cette règle dans la section de configuration du projet. Mais il n'y a pas de mal à la revisiter.

> 💡 NOTE : Cette règle est déjà présente dans `js.configs.recommended` qui contient toutes les règles ESLint recommandées

En action, cette règle mettra en évidence vos variables inutilisées comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/rule_1.png)
_Sortie de la règle #1 configurée_

## Règle #2 : `no-console`

<img width="100%" style="width:100%" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExczIxMjJja2s5NWxjbHBsY3A2OXhzM2U4NW93d3NuYzhweWVlcmJ3eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ge7l7e5EiHUYI3e71P/giphy.webp" alt="A wild thought image">

Je trouve cette règle super utile car les logs inutiles qui ne sont pas importants ne devraient pas être présents dans la base de code. Nous ajoutons généralement ces logs à des fins de débogage.

Cela peut être dangereux car les déclarations `console.log` peuvent révéler des données personnelles sensibles de vos utilisateurs dans la console du navigateur si vous traitez des données personnelles. Vous devez donc être prudent à ce sujet.

Par exemple, il y a de fortes chances que vous oubliiez de supprimer une déclaration console. Plus tard, la même chose vous mordra lors des audits.

Je comprends que ces logs sont utiles en mode développement. Donc, dans ces cas où les logs dépendent de l'environnement, il est préférable d'envelopper ces déclarations `console.log` avec un wrapper personnalisé qui vous aide à activer/désactiver les logs en fonction de l'environnement.

Pour éviter tout ce tracas, ESLint dispose de la règle [no-console](https://eslint.org/docs/latest/rules/no-console#rule-details). Cette règle fournira un linting chaque fois qu'elle trouvera une déclaration console dans votre base de code.

Pour configurer cette règle, vous devez faire la même chose que nous avons faite précédemment :

```jsx
export default [
  {
    rules: {
      "no-unused-vars": "error",
      "no-console": "error", // <---- Ajouter la règle ici
    },
  },
];


```

En action, cette règle lintera votre base de code comme ci-dessous :

![Rule_2.png](https://www.freecodecamp.org/news/content/images/2024/07/Rule_2.png)
_console.log devient une erreur lorsque la règle #2 est configurée_

## Règle #3 : `no-duplicate-imports` et tri des imports

<figure>
    <img width="100%" style="width:100%" src="https://i.giphy.com/26FmPNdnmllMwkoTK.webp" alt="import cargo">
      <figcaption>Cargos triés sur le navire</figcaption>
</figure>


Ce que j'aime dans cette règle, c'est qu'elle vous aide à garder vos imports super lisibles. Avez-vous déjà vu un gros fichier de composant React qui a toutes ses imports et qui semble désordonné ? Oui, ce n'est pas amusant.

Vous pouvez même avoir différents imports qui proviennent de la même bibliothèque. Ces façons d'importer des bibliothèques peuvent être chaotiques et difficiles à suivre. C'est là que la règle ESLint [no-duplicate-imports](https://eslint.org/docs/latest/rules/no-duplicate-imports#rule-details) et le plugin ESLint [eslint-plugin-simple-import-sort](https://github.com/lydell/eslint-plugin-simple-import-sort) entrent en jeu.

`no-duplicate-imports` est une règle ESLint qui stipule que toutes les imports d'un seul module peuvent être regroupées en une seule déclaration d'import.

Considérez l'exemple suivant :

```jsx
import { get, set } from 'lodash';
import { zip } from 'lodash'; // <----- erreur selon no-duplicate-imports
import React from 'react';

```

Comme vous pouvez le voir, les imports des deux premières lignes appartiennent au même module – c'est-à-dire, la bibliothèque Lodash. Si la règle est suivie, alors le code ressemblera à ceci :

```jsx
import { get, set, zip } from 'lodash';
import React from 'react';

```

ESLint n'a aucune règle qui vous aidera à trier vos imports. Dans ce cas, vous pouvez obtenir de l'aide de différents plugins basés sur la communauté sur [awesome-eslint](https://github.com/dustinspecker/awesome-eslint?tab=readme-ov-file).

`awesome-eslint` est un dépôt de configurations ESLint, plugins, parseurs, formateurs, et ainsi de suite. J'ai trouvé ce plugin appelé `eslint-plugin-simple-import-sort` qui vous aide à trier vos imports par ordre alphabétique, avec les imports de bibliothèques en premier et ensuite les imports relatifs.

Voici un extrait de l'exemple du dépôt du plugin réel :

```jsx
import React from "react";
import Button from "../Button";

import styles from "./styles.css";
import type { User } from "../../types";
import { getUser } from "../../api";

import PropTypes from "prop-types";
import classnames from "classnames";
import { truncate, formatNumber } from "../../utils";

```

🡇🔏

```jsx
import classnames from "classnames";
import PropTypes from "prop-types";
import React from "react";

import { getUser } from "../../api";
import type { User } from "../../types";
import { formatNumber, truncate } from "../../utils";
import Button from "../Button";
import styles from "./styles.css";

```

Vous pouvez également définir l'ordre de tri de ce plugin sur quelque chose de différent, que vous pouvez lire plus en détail [ici](https://github.com/lydell/eslint-plugin-simple-import-sort?tab=readme-ov-file#sort-order).

Incorporons ces règles et plugins dans notre projet. Tout d'abord, vous ajouterez la règle `no-duplicate-imports` dans votre configuration :

```jsx
export default [
	{
		rules: {
			"no-duplicate-imports": "error", // <---- ICI
			"no-unused-vars": "error",
			"no-console": "error",
		},
	},
];


```

C'est très similaire aux règles que nous avons configurées précédemment. Nous définissons la valeur de la règle sur `error`.

Ensuite, commencez par configurer le plugin **`eslint-plugin-simple-import-sort`** dans votre projet. Tout d'abord, installez ce plugin avec la commande suivante :

```bash
yarn add --dev eslint-plugin-simple-import-sort

```

Une fois installé, assurez-vous que ce plugin est activé en l'ajoutant dans votre fichier `eslint.config.js` comme suit :

```jsx
import simpleImportSort from "eslint-plugin-simple-import-sort";

export default [
  {
    plugins: {
      "simple-import-sort": simpleImportSort, // <--- ajouter le plugin
    },
    rules: {
      "no-duplicate-imports": "error",
      "no-unused-vars": "error",
      "no-console": "error",
      "simple-import-sort/imports": "error", // <--- se référer à la règle du plugin
    },
  },
];

```

Dans ce code, nous importons d'abord le plugin en tant que `simpleImportSort`. Ensuite, dans le tableau exporté, juste au-dessus de la propriété `rules`, nous ajoutons la propriété `plugins`. Cette propriété consistera en tous les plugins que nous voulons activer sous la forme d'une clé étant l'espace de noms du plugin et la valeur étant l'objet du plugin.

Dans le code ci-dessus, `simple-import-sort` est l'espace de noms du plugin et sa valeur est l'objet du plugin qui est `simpleImportSort`.

Maintenant, pour utiliser les règles qui sont présentes à l'intérieur des plugins, tout ce que vous avez à faire est de vous référer à l'espace de noms du plugin suivi du nom de la règle en tant que clé et de la valeur à être `error` – dans notre cas, à l'intérieur de la section des règles.

Dans notre configuration, nous nous référons à la règle `imports` de l'espace `simple-import-sort` du plugin en tant que `simple-import-sort/imports`.

Une fois que vous avez ajouté cette règle dans la configuration, vous pouvez la voir en action comme ci-dessous :

![sorting_imports-ezgif.com-optimize.gif](https://www.freecodecamp.org/news/content/images/2024/07/sorting_imports-ezgif.com-optimize.gif)
_Imports en cours de tri_

Vous pouvez également configurer ce tri des imports lorsque vous enregistrez votre code en activant `codeActionsOnSave` dans les paramètres de l'extension ESLint VSCode :

```jsx
{
	"[typescriptreact]": {
		"editor.defaultFormatter": "esbenp.prettier-vscode"
	},
	"[typescript]": {
		"editor.defaultFormatter": "esbenp.prettier-vscode"
	},
	"[javascript]": {
		"editor.defaultFormatter": "esbenp.prettier-vscode"
	},
	"workbench.sideBar.location": "right",
	"diffEditor.ignoreTrimWhitespace": false,
	"workbench.colorTheme": "Default Dark+",
	"editor.stickyScroll.enabled": true,
	"prettier.useTabs": true,
	"editor.formatOnSave": true,
	"window.zoomLevel": 1,
	"eslint.options": {
		 "overrideConfigFile": "./eslint.config.js" 
	},
	"eslint.format.enable": true,
	"editor.codeActionsOnSave": { //< ------ Ajouter cette propriété
        "source.fixAll.eslint": "explicit"
    }
}


```

Maintenant que vous comprenez et avez ajouté les règles et plugins ESLint, comprenons et implémentons les hooks Git.

## Comment configurer les hooks Git

<figure>
    <img width="100%" style="width:100%" src="https://i.giphy.com/2VOB4tK9qsQ7efC2Ub.webp" alt="A fish hook">
      <figcaption>Un hameçon</figcaption>
</figure>


Les hooks Git ne sont rien d'autre que des fonctionnalités Git sur stéroïdes. Tous les détails et l'origine des hooks Git sont hors du cadre de cet article, je vous recommande donc vivement de lire plus à leur sujet [ici](https://git-scm.com/docs/githooks).

Il existe de nombreuses bibliothèques qui vous aideront à gérer vos hooks Git. J'utiliserai [Husky](https://typicode.github.io/husky/) ici. Pour installer Husky dans votre base de code, exécutez les commandes suivantes :

```bash
yarn add --dev husky
# Ajouter pinst UNIQUEMENT si votre package n'est pas privé
yarn add --dev pinst

```

Une fois installé, assurez-vous de l'initialiser en faisant ce qui suit :

```bash
npx husky init

```

Cela garantit qu'il crée le dossier `.husky` qui contient le script precommit. Il ajoute également le script prepare à l'intérieur du fichier `package.json`.

Maintenant que vous avez configuré Husky dans votre projet, nous implémenterons notre première fonctionnalité de hook pre-commit.

## Gitleaks : Supprimer les secrets avant les commits

<figure>
    <img width="100%" style="width:100%" src="https://i.giphy.com/yow6i0Zmp7G24.webp" alt="Shhhh">
      <figcaption>Chut</figcaption>
</figure>


Gitleaks est un outil qui analyse votre base de code pour détecter les clés API, les secrets ou les mots de passe. Selon le dépôt :

> _"Gitleaks est un outil SAST pour **détecter** et **prévenir** les secrets codés en dur comme les mots de passe, les clés API et les jetons dans les dépôts Git. Gitleaks est une **solution facile à utiliser, tout-en-un** pour détecter les secrets, passés ou présents, dans votre code."_

Implémentons maintenant Gitleaks dans notre projet avec l'aide des hooks `precommit` avec Husky.

Tout d'abord, installez Gitleaks avec la commande suivante :

```bash
brew install gitleaks

```

Une fois installé, commencez par modifier le fichier de script `precommit` qui se trouve dans le dossier `.husky`.

Notre objectif ici est de vérifier que tous les fichiers qui sont staged sont analysés par l'outil Gitleaks avant que le commit ne se produise. Le hook `precommit` est la meilleure option où vous pouvez exécuter différents scripts avant qu'un commit ne se produise.

Gitleaks a déjà un exemple dans le hook `precommit` Python. Il vérifie si le hook Gitleaks est activé. Si c'est le cas, il exécute la fonction `protect` de Gitleaks sur les fichiers staged. Vous pouvez trouver ce code [ici](https://github.com/gitleaks/gitleaks/blob/26f34692fac6e9daec13c770421b4ed990d1c321/scripts/pre-commit.py).

J'ai converti ce script en un script bash avec l'aide de ChatGPT. Voici le résultat qu'il m'a donné :

```bash
#!/bin/bash

# Script d'assistance à utiliser comme hook pre-commit.

gitleaksEnabled() {
    # Déterminer si le hook pre-commit pour gitleaks est activé.
    local out
    out=$(git config --bool hooks.gitleaks)
    if [ "$out" == "false" ]; then
        return 1
    fi
    return 0
}

# Vérifier si gitleaks est installé
if ! command -v gitleaks &> /dev/null; then
    echo 'Erreur : gitleaks n'est pas installé sur votre système.'
    echo 'Veuillez installer gitleaks pour utiliser ce hook pre-commit.'
    exit 1
fi

if gitleaksEnabled; then
    gitleaks protect -v --staged
    exitCode=$?
    if [ $exitCode -eq 1 ]; then
        echo 'Avertissement : gitleaks a détecté des informations sensibles dans vos modifications.
Pour désactiver le hook precommit de gitleaks, exécutez la commande suivante :

    git config hooks.gitleaks false
'
        exit 1
    fi
else
    echo 'gitleaks precommit désactivé (activer avec `git config hooks.gitleaks true`)'
fi

```

Dans ce script, j'ai également demandé à ChatGPT d'ajouter une fonctionnalité supplémentaire pour vérifier si Gitleaks est installé dans le système ou non. Si ce n'est pas le cas, alors le hook `precommit` arrête son exécution avec le code de sortie 1.

Maintenant, pour essayer votre hook `precommit`, vous devez d'abord stage les modifications :

```bash
git add .

```

Ensuite, commitez les modifications comme suit :

```bash
git commit -m 'feat: ajouté le hook precommit gitleaks'

```

Cela exécutera le hook `precommit` que vous avez défini. Cela ressemblera à ceci :

![gitleaks.png](https://www.freecodecamp.org/news/content/images/2024/07/gitleaks.png)
_outil gitleaks en cours d'exécution avant le commit_

## Exécuter les tests unitaires avant les commits

<figure>
    <img width="100%" style="width:100%" src="https://i.giphy.com/gw3IWyGkC0rsazTi.webp" alt="A printer">
      <figcaption>Chut</figcaption>
</figure>


Une autre utilisation pratique des hooks Git est l'exécution de tests unitaires sur les fichiers staged. Cela est utile car la vérification se produit localement et n'est pas poussée vers le dépôt distant.

Bien que l'exécution des tests unitaires sur CI ne soit pas un problème, l'exécution des tests sur les fichiers staged et associés peut faire gagner du temps. Cela permet au CI de se concentrer sur l'exécution de la suite complète de tests unitaires avant de fusionner le commit dans la branche de release.

Voici donc le flux pour utiliser le hook `precommit` qui exécutera les tests unitaires sur les fichiers staged :

* Trouver les fichiers staged qui ont les extensions de fichier `*.test.js/ts`
* Exécuter ces tests staged ainsi que leur code associé
* Si des échecs ou erreurs de test surviennent lors des tests, alors quitter le hook `precommit` (pour que le commit ne se produise pas).

### Étape 1 : Trouver les fichiers qui sont staged

La première étape consiste à trouver tous les noms de fichiers qui sont staged avec l'extension `*.test.js`. Pour ce faire, vous pouvez utiliser la commande `git diff` :

```bash
git diff --cached --name-only --diff-filter=ACM | grep '\\.test\\.js$'

```

`git diff` vous aide à trouver la différence entre les modifications et le fichier actuel. Vous pouvez en savoir plus sur `git diff` et ses options [ici](https://git-scm.com/docs/git-diff).

Ensuite, en utilisant le [symbole pipe](https://superuser.com/a/756259), nous filtrons la sortie de la commande `git diff` précédente avec l'aide de [grep](https://www.freecodecamp.org/news/grep-command-in-linux-usage-options-and-syntax-examples). Nous disons à grep de trouver tous les noms de fichiers qui se terminent par l'extension `.test.js`.

### Étape 2 : Exécuter le test unitaire sur les fichiers staged

Maintenant, pour exécuter le test unitaire, assurez-vous d'avoir installé [Jest](https://jestjs.io/docs/getting-started) dans votre projet. Pour exécuter le test unitaire sur les fichiers staged et les fichiers qui y sont associés, exécutez la commande suivante :

```bash
yarn run test --coverage --bail --findRelatedTests <staged-files-ending-with-.test.js>

```

La commande ci-dessus exécutera le test sur les fichiers staged actuels et les fichiers qui y sont associés avec l'option `--findRelatedTests`. Elle fournira également un rapport de couverture avec l'option `--coverage` et interrompra les tests lorsqu'un échec sera trouvé avec l'option `--bail`.

Maintenant, la partie principale de la commande ci-dessus est que vous devez fournir les fichiers qui sont staged avec l'extension `.test.js`. Pour ce faire, utilisez la commande de l'étape 1. Puisque vous utilisez un script bash, stockez la sortie de l'étape 1 dans une variable et passez-la à la commande de test unitaire :

```bash
# Lister les fichiers staged *.test.js
stagedTestFiles=$(git diff --cached --name-only --diff-filter=ACM | grep '\\.test\\.js$')

yarn run test --coverage --bail --findRelatedTests $stagedTestFiles

```

Vous ajouterez les commandes ci-dessus dans votre script `precommit`. Le script final du hook pre-commit ressemblera à ceci :

```bash
#!/bin/bash

# Script d'assistance à utiliser comme hook pre-commit.

gitleaksEnabled() {
    # Déterminer si le hook pre-commit pour gitleaks est activé.
    local out
    out=$(git config --bool hooks.gitleaks)
    if [ "$out" == "false" ]; then
        return 1
    fi
    return 0
}

# Pour ============================= TESTS UNITAIRES =============================
# Lister les fichiers staged *.test.js
stagedTestFiles=$(git diff --cached --name-only --diff-filter=ACM | grep '\\.test\\.js$')

if [ -n "$stagedTestFiles" ]; then
    echo "Fichiers staged *.test.js :"
    yarn run test --coverage --bail --findRelatedTests $stagedTestFiles
else
    echo "Aucun fichier *.test.js n'est staged."
fi

# Vérifier si gitleaks est installé
if ! command -v gitleaks &> /dev/null; then
    echo 'Erreur : gitleaks n'est pas installé sur votre système.'
    echo 'Veuillez installer gitleaks pour utiliser ce hook pre-commit.'
    exit 1
fi

# Pour ============================= VÉRIFICATION DES SECRETS =============================
if gitleaksEnabled; then
    gitleaks protect -v --staged
    exitCode=$?
    if [ $exitCode -eq 1 ]; then
        echo 'Avertissement : gitleaks a détecté des informations sensibles dans vos modifications.
Pour désactiver le hook precommit de gitleaks, exécutez la commande suivante :

    git config hooks.gitleaks false
'
        exit 1
    fi
else
    echo 'gitleaks precommit désactivé (activer avec `git config hooks.gitleaks true`)'
fi


```

Pour tester le hook precommit sur le test unitaire, j'ai créé un fichier de test exemple : `index.test.js` :

```jsx
const sum = 1 + 2;

describe("test suite", () => {
	it("check sum suit", () => {
		expect(sum).toBe(3);
	});
});


```

Voici comment le hook `precommit` génère la sortie lorsque le test passe et échoue.

> Note : Ici, j'ai essayé de générer intentionnellement l'erreur dans le fichier `index.test.js`.

Exécutez la commande suivante pour voir la sortie :

```shell
git commit -m 'test commit'
```

![Unit test failure.png](https://www.freecodecamp.org/news/content/images/2024/07/Unit-test-failure.png)
_Échec des tests unitaires_

![Unit test passing.png](https://www.freecodecamp.org/news/content/images/2024/07/Unit-test-passing.png)
_Réussite des tests unitaires_

## Résumé

Pour résumer, voici ce que vous avez appris dans cet article :

* Ce qu'est ESLint et comment vous pouvez le configurer avec des règles et des plugins
* Nous avons également examiné l'extension ESLint de VSCode et l'avons configurée pour utiliser notre fichier de configuration plat existant
* Nous avons appris ce que sont les hooks Git et comment vous pouvez utiliser Husky pour gérer vos hooks.
* Nous avons examiné comment vous pouvez supprimer les secrets et effectuer des tests unitaires avant tout commit.

J'ai beaucoup appris en écrivant ce guide, et j'espère que vous en avez tiré beaucoup !

Vous pouvez trouver le code final [ici](https://github.com/keyurparalkar/eslint-githooks-example).

Merci beaucoup d'avoir lu mon article ! Vous pouvez me suivre sur [Twitter](https://twitter.com/keurplkar), [GitHub](http://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).