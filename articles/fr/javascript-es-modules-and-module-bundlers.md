---
title: Le Guide des Modules JavaScript – Guide Complet des Modules ES et des Bundlers
  de Modules
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-05-11T23:06:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-es-modules-and-module-bundlers
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/JavaScript-Module-Book-Cover--1-.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: json
  slug: json
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Le Guide des Modules JavaScript – Guide Complet des Modules ES et des Bundlers
  de Modules
seo_desc: 'Modules and Module Bundlers are essential components of modern web development.
  But understanding how they work can quickly become overwhelming.

  This article will show you all you need to know about ES Modules and Module Bundlers
  in plain English.

  Ta...'
---

**Modules** et **Bundlers de Modules** sont des composants essentiels du développement web moderne. Mais comprendre comment ils fonctionnent peut rapidement devenir écrasant.

Cet article vous montrera tout ce que vous devez savoir sur les Modules ES et les Bundlers de Modules en anglais simple.

## Table des Matières

1. [Qu'est-ce qu'un Module JavaScript ?](#heading-quest-ce-quun-module-javascript)
2. [Pourquoi Utiliser des Modules ?](#heading-pourquoi-utiliser-des-modules)
3. [Types Courants de Systèmes de Modules en JavaScript](#heading-types-courants-de-systemes-de-modules-en-javascript)
4. [Comment Convertir un Fichier JavaScript en Module](#heading-comment-convertir-un-fichier-javascript-en-module)
5. [Comment Utiliser un Module ES](#heading-comment-utiliser-un-module-es)
6. [Comment Exporter le Code d'un Module](#heading-comment-exporter-le-code-dun-module)
7. [Comment Importer du Code Exporté](#heading-comment-importer-du-code-exporte)
8. [Comment Utiliser le Code Importé d'un Module](#heading-comment-utiliser-le-code-importe-dun-module)
9. [Comment Renommer les Exportations et Importations dans les Modules ES](#heading-comment-renommer-les-exportations-et-importations-dans-les-modules-es)
10. [Pourquoi Renommer le Code d'un Module ?](#heading-pourquoi-renommer-le-code-dun-module)
11. [Comment Renommer Plusieurs Exportations dans un Module ES](#heading-comment-renommer-plusieurs-exportations-dans-un-module-es)
12. [Comment Renommer Plusieurs Importations dans un Module ES](#heading-comment-renommer-plusieurs-importations-dans-un-module-es)
13. [Comment Importer Tous les Éléments Exportables d'un Module ES en Une Seule Fois](#heading-comment-importer-tous-les-elements-exportables-dun-module-es-en-une-seule-fois)
14. [Comment Exporter Anonymement vers un Module ES](#heading-comment-exporter-anonymement-vers-un-module-es)
15. [Qu'est-ce qu'un Fichier d'Agrégation ?](#heading-quest-ce-quun-fichier-dagregation)
16. [Projet : Comment Utiliser un Fichier d'Agrégation](#heading-projet-comment-utiliser-un-fichier-dagregation)
17. [Comment Utiliser la Syntaxe `import()` pour Charger un Module Dynamiquement](#heading-comment-utiliser-la-syntaxe-import-pour-charger-un-module-dynamiquement)
18. [Qu'est-ce que `import.meta` dans les Modules ES ?](#heading-quest-ce-que-importmeta-dans-les-modules-es)
19. [Révision Rapide des Modules Jusqu'à Présent](#heading-revision-rapide-des-modules-jusqua-present)
20. [Qu'est-ce qu'un Bundler de Modules ?](#heading-quest-ce-quun-bundler-de-modules)
21. [Pourquoi Avez-Vous Besoin d'un Bundler de Modules ?](#heading-pourquoi-avez-vous-besoin-dun-bundler-de-modules)
22. [Comment Fonctionne un Bundler de Modules ?](#heading-comment-fonctionne-un-bundler-de-modules)
23. [Comment Utiliser Webpack](#heading-comment-utiliser-webpack)
24. [Comment Faire en Sorte que Webpack Génère Automatiquement le Fichier HTML de Votre Application](#heading-comment-faire-en-sorte-que-webpack-genere-automatiquement-le-fichier-html-de-votre-application)
25. [Comment Faire en Sorte que `HtmlWebpackPlugin` Utilise Votre Fichier Source comme Modèle pour Générer Automatiquement une Nouvelle Page HTML](#heading-comment-faire-en-sorte-que-htmlwebpackplugin-utilise-votre-fichier-source-comme-modele-pour-generer-automatiquement-une-nouvelle-page-html)
26. [Choses Importantes à Savoir sur la Mise à Jour de Votre Application](#heading-choses-importantes-a-savoir-sur-la-mise-a-jour-de-votre-application)
27. [Comment Relancer Webpack Automatiquement](#heading-comment-relancer-webpack-automatiquement)
28. [Comment Recharger le Navigateur Automatiquement](#heading-comment-recharger-le-navigateur-automatiquement)
29. [Qu'est-ce que le Fichier de Configuration de Webpack ?](#heading-quest-ce-que-le-fichier-de-configuration-de-webpack)
30. [Options de Configuration Courantes de Webpack](#heading-options-de-configuration-courantes-de-webpack)
31. [Aperçu](#heading-aperçu)

Alors, sans plus tarder, commençons avec les modules.

## Qu'est-ce qu'un Module JavaScript ?

Un **module** JavaScript est un fichier qui permet d'exporter son code. Cela permet à d'autres fichiers JavaScript d'importer et d'utiliser le code exporté comme leurs dépendances.

Plus précisément, un module est simplement un fichier JavaScript qui permet de partager son code avec d'autres fichiers au sein de votre projet (ou avec le monde via des [gestionnaires de paquets](https://www.codesweetly.com/package-manager-explained) comme Yarn et NPM).

## Pourquoi Utiliser des Modules ?

À ses débuts, les gens utilisaient JavaScript principalement pour des tâches de script triviales comme fournir des morceaux d'interactivité aux pages web là où c'était nécessaire. En d'autres termes, les développeurs utilisaient principalement JavaScript pour écrire de petits scripts—pas de grands.

Aujourd'hui, cependant, JavaScript a évolué pour devenir un outil de script vaste capable de faire bien plus que simplement rendre les pages web interactives.

Il est maintenant courant d'avoir un grand code JavaScript utilisé pour diverses fonctions comme le développement de sites web côté serveur, le développement de jeux et le développement d'applications mobiles.

Puisque JavaScript peut être utilisé pour pratiquement n'importe quelle tâche de programmation, un besoin est apparu de partager des scripts entre les fichiers d'un projet et le monde.

Ainsi, la communauté JavaScript a développé le système de modules pour permettre aux développeurs de partager leurs scripts à la demande.

## Types Courants de Systèmes de Modules en JavaScript

Voici quelques-uns des systèmes de modules populaires en JavaScript :

* [Asynchronous Module Definition (AMD)](https://github.com/amdjs/amdjs-api/blob/master/AMD.md)
* [Modules CommonJS](https://en.wikipedia.org/wiki/CommonJS)
* [Universal Module Definition (UMD)](https://github.com/umdjs/umd)
* [Modules ES](https://tc39.es/ecma262/#sec-modules)

**Note :** Les modules ES sont parfois appelés "modules JS" ou "modules ECMAScript".

Parmi les systèmes de modules listés ci-dessus, le système de modules ES est la norme officielle pour JavaScript.

Les trois autres (AMD, CommonJS et UMD) ont été créés par divers développeurs lorsque JavaScript n'avait pas de système de modules standardisé.

Cependant, depuis l'apparition des modules ES dans la norme ECMAScript 2015, les systèmes de modules précédents sont progressivement devenus partie de l'histoire de JavaScript.

Par conséquent, cet article se concentrera sur la manière dont les modules ES fonctionnent.

Tout d'abord, il est essentiel de savoir comment convertir un fichier JavaScript en module. Alors, discutons-en ci-dessous.

## Comment Convertir un Fichier JavaScript en Module

Pour convertir un fichier JavaScript en module ES, procédez comme suit :

### Étape 1 : Créer un répertoire de projet

Créez un dossier de projet—où les fichiers HTML et JavaScript de ce projet résideront.

### Étape 2 : Créer vos fichiers de code

Créez les fichiers suivants à l'intérieur de votre dossier de projet :

1. `index.html`
2. `index.js`

### Étape 3 : Ajouter votre fichier JavaScript à votre document HTML

Ouvrez votre fichier `index.html` et reproduisez le code ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>Tutoriel sur les Modules ES</h1>

    <!-- Ajoutez le fichier JavaScript "index.js" à ce document HTML -->
    <script type="module" src="index.js"></script>
  </body>
</html>
```

Dans l'extrait HTML ci-dessus, nous avons utilisé l'attribut `type="module"` de `<script>` pour convertir le fichier JavaScript `index.js` en module ES.

Maintenant que nous savons comment convertir un fichier JavaScript en module, voyons comment en utiliser un.

## Comment Utiliser un Module ES

Suivez les étapes ci-dessous pour apprendre à utiliser un module ES.

### Étape 1 : Créer un répertoire de projet

Créez un dossier de projet—où les fichiers HTML et modules de ce projet résideront.

### Étape 2 : Créer vos fichiers de code

Créez les fichiers suivants à l'intérieur de votre dossier de projet :

1. `index.html`
2. `module-1.js`
3. `module-2.js`

### Étape 3 : Ajouter les modules à votre document HTML

Ouvrez votre fichier `index.html` et reproduisez le code ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>Tutoriel sur les Modules ES</h1>
    <h2>Vérifiez la console</h2>

    <script type="module" src="module-1.js"></script>
    <script type="module" src="module-2.js"></script>
  </body>
</html>
```

Voici les principales choses que nous avons faites dans l'extrait HTML ci-dessus :

1. Nous avons ajouté les deux fichiers JavaScript à notre document HTML.
2. Nous avons utilisé l'attribut `type="module"` pour convertir les fichiers JavaScript réguliers en fichiers de module ES.

**Notez** que JavaScript différère automatiquement les modules ES. Vous n'avez donc pas besoin d'utiliser un attribut `defer` dans l'élément `<script>` de votre module.

De plus, l'ordinateur exécutera un module une seule fois—peu importe le nombre de balises `<script>` que vous utilisez pour le référencer.

### Étape 4 : Voir votre application

Ouvrez votre fichier `index.html` dans n'importe quel navigateur pour voir l'état actuel de votre application.

![Ouvrez votre fichier HTML dans votre navigateur - Tutoriel sur les Modules](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-open-html-file-in-chrome-browser-codesweetly.png)
_Ouverture d'un fichier index.html dans un navigateur Chrome_

Une fois ouvert, si vous inspectez la console de votre navigateur, vous verrez des messages d'erreur.

![Erreur de politique CORS dans la console du navigateur - Tutoriel sur les Modules](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-cors-policy-error-codesweetly.png)
_Inspection de la console d'un navigateur Chrome_

Le navigateur a lancé une erreur de politique CORS car les modules ES ne fonctionnent que via les URL `http://` et `https://`—pas localement via une URL `file://`.

En d'autres termes, puisque notre fichier HTML contient deux modules ES, nous devons charger le document via un schéma `http://`.

Les deux façons typiques de charger un document HTML via un schéma `http://` sont :

* En utilisant un serveur local, ou
* Par l'utilisation d'un Bundler de Modules

Nous discuterons des Bundlers de Modules plus en détail plus tard dans cet article. Pour l'instant, voyons comment utiliser un serveur local pour charger le fichier `index.html` via un schéma `http://`.

#### Comment exécuter un fichier HTML via un serveur local

Les étapes ci-dessous vous montreront comment utiliser une extension de serveur local [VS Code](https://code.visualstudio.com/) pour exécuter votre fichier HTML.

**Note :** Supposons que votre éditeur de code est Atom ou Sublime Text. Dans ce cas, suivez les liens ci-dessous pour apprendre comment installer un plugin de serveur local.

* [Atom Live Server](https://atom.io/packages/atom-live-server)
* [Sublime Text Live Server](https://youtu.be/5CinAgQylao)

##### 1. Ajoutez votre dossier de projet à l'espace de travail de VSCode

![Ajoutez votre dossier de projet à l'espace de travail de VSCode](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-add-proj-folder-to-vscode-workspace-codesweetly.gif)
_Ajout d'un dossier de projet à l'espace de travail de VSCode_

##### 2. Installez un serveur local (Live Server par Ritwick Dey)

![Installez le Live Server par Ritwick Dey](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-install-live-server-codesweetly.png)
_Installation du Live Server VSCode par Ritwick Dey_

##### 3. Ouvrez votre fichier HTML dans l'éditeur de code

![Ouvrez votre fichier HTML dans votre éditeur de code](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-open-html-file-in-code-editor-codesweetly.png)
_Ouverture du fichier HTML dans l'éditeur VSCode_

##### 4. Utilisez Live Server pour exécuter le fichier HTML dans votre navigateur par défaut

![Exécutez votre fichier HTML avec Live Server - Tutoriel sur les Modules](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-run-html-file-with-live-server-codesweetly.png)
_Ouverture du fichier HTML du projet avec Live Server_

Votre application devrait maintenant se charger avec le schéma `http://`—sans aucune erreur CORS dans la console de votre navigateur.

**Quelques points à noter :**

* Supposons que vous n'avez pas ajouté votre dossier de projet à l'espace de travail de VSCode (étape 1). Dans ce cas, le Live Server pourrait ne pas charger votre fichier correctement.
* Live Server rechargera automatiquement votre navigateur chaque fois que vous enregistrerez des modifications dans votre fichier HTML.
* Supposons que vous souhaitiez arrêter le Live Server. Dans ce cas, faites un clic droit sur la page de l'éditeur HTML et cliquez sur "Stop Live Server".
* Les modules JavaScript fonctionnent en mode strict par défaut. Ainsi, vous devez respecter les règles de syntaxe strictes de JavaScript. Sinon, votre programme pourrait mal fonctionner.

Maintenant que vous avez converti votre fichier JavaScript en module ES, vous pouvez commencer à utiliser les mots-clés `export` et `import` pour partager le code de vos modules. Discutons-en ci-dessous.

## Comment Exporter le Code d'un Module

Il existe deux façons équivalentes d'exporter un élément d'un module.

1. Placer un mot-clé `export` avant votre code
2. Créer une instruction d'exportation

Discutons des deux façons ci-dessous.

### Comment partager le code d'un module en plaçant un mot-clé `export` avant le code

Une façon d'exporter un élément est de placer un mot-clé `export` avant le code que vous souhaitez partager avec d'autres modules.

Par exemple, ouvrez votre fichier `module-1.js` et reproduisez le code ci-dessous :

```js
// module-1.js

// Exporter la variable "bestClub" :
export const bestClub = "Votre Club";

```

Vous pouvez voir comment nous avons placé le mot-clé `export` avant l'instruction de variable `const` dans l'extrait ci-dessus.

Nous avons précédé la variable `const` du mot-clé `export` pour dire à l'ordinateur de partager la variable `bestClub` avec d'autres modules qui la demandent.

**Note :** Le mot-clé `export` met en évidence le code que vous souhaitez partager avec d'autres modules.

**Voici un autre exemple :**

```js
// Exporter la fonction "multiply" :
export function multiply(x, y) {
  return x * y;
}

```

L'instruction ci-dessus indique à l'ordinateur d'exporter `multiply()` vers les modules qui la demandent.

Voyons maintenant la deuxième façon d'exporter le code d'un module.

### Comment partager le code d'un module en créant une instruction d'exportation

Une autre façon de partager le code d'un module est d'utiliser le mot-clé `export` comme une instruction autonome. Vous pouvez le faire en précédant un seul mot-clé `export` d'un bloc (`{...}`) de noms séparés par des virgules du code que vous souhaitez partager.

**Voici un exemple :**

```js
// Créer une variable nommée "bestClub" :
const bestClub = "Votre Club";

// Créer une fonction nommée "multiply" :
function multiply(x, y) {
  return x * y;
}

// Créer un tableau nommé "fruits" :
const fruits = ["Mango", "Apple", "Orange", "Lemon"];

// Exporter les trois instructions ci-dessus :
export { bestClub, multiply, fruits };

```

L'extrait ci-dessus a utilisé une instruction `export` pour indiquer que l'ordinateur peut partager `bestClub`, `multiply` et `fruits` avec d'autres modules qui en font la demande.

Gardez à l'esprit que `export` fonctionne uniquement comme un élément de premier niveau. Il ne fonctionnerait donc pas dans une fonction, par exemple.

Par conséquent, l'extrait ci-dessous lancera une erreur car nous avons utilisé le mot-clé `export` à l'intérieur de la fonction.

```js
function wrong() {
  export let bestClub = "Votre Club";
  return bestClub;
}

```

**Note :**

* Le mot-clé `export` fonctionne uniquement à l'intérieur des modules—pas à l'intérieur des programmes JavaScript réguliers.
* JavaScript [hoiste](https://www.codesweetly.com/javascript-hoisting) les instructions `export`. Vous pouvez donc les définir n'importe où dans votre module.
* Les modules exportés fonctionnent en mode strict par défaut—peu importe si vous avez spécifié l'instruction `strict`.

Voyons maintenant comment importer le code exporté.

## Comment Importer du Code Exporté

Pour importer du code exporté, utilisez l'instruction `import` des modules ES.

Par exemple, ouvrez votre fichier `module-2.js` et reproduisez le code ci-dessous :

```js
// module-2.js

import { bestClub } from "./module-1.js";

```

Dans l'extrait ci-dessus, nous avons utilisé une instruction `import` pour importer la variable `bestClub` du fichier `module-1.js`.

Ainsi, `module-2.js` est un module de premier niveau car il contient un autre script.

D'autre part, `module-1.js` est un sous-module car il s'agit d'un script utilisé à l'intérieur d'un autre fichier.

**Note :**

* Nous utilisons l'instruction `import` pour importer des éléments d'autres modules.
* Il est obligatoire d'encadrer vos exportations nommées avec des accolades lors de leur importation.

Gardez à l'esprit qu'une instruction `import` ne peut obtenir le code d'un autre module que s'il est exporté avec le mot-clé `export`.

Par exemple, l'instruction `import` ci-dessous importera les éléments `bestClub`, `multiply` et `fruits` s'ils ont été marqués pour l'exportation dans le fichier `module-1.js`.

```js
// Importer trois éléments du fichier module-1.js :
import { bestClub, multiply, fruits } from "./module-1.js";

```

Supposons que vous n'avez pas utilisé le mot-clé `export` pour marquer les trois éléments comme des fonctionnalités exportables. Dans ce cas, l'instruction `import` lancera une `Uncaught SyntaxError`.

**Note :**

* "Spécificateur de module" et "spécificateur d'importation" sont d'autres noms que les gens donnent à la chaîne de chemin de fichier `"./module-1.js"` dans l'extrait ci-dessus.
* Le point (`.`) dans le spécificateur de module `"./module-1.js"` signifie _"même répertoire"_. En d'autres termes, le point indique à l'ordinateur de trouver le fichier `module-1.js` dans le même dossier où se trouve le module actuel.
* Le module actuel mentionné dans l'extrait ci-dessus est le fichier où l'instruction `import` a été définie.

Une alternative à la syntaxe de point (`.`) du spécificateur d'importation est d'écrire le chemin relatif complet vers l'emplacement d'un module.

**Voici un exemple :**

```js
// Importer trois éléments du fichier module-1.js :
import { bestClub, multiply, fruits } from "/codesweetly/blog/notes/modular-javascript/es-modules/module-1.js";

```

Vous pouvez voir à quel point l'instruction `import` ci-dessus est longue. Nous utilisons souvent la syntaxe de point en raison de sa longueur courte et portable.

Supposons que vous choisissez d'utiliser la syntaxe de point. Dans ce cas, gardez à l'esprit que certains systèmes de modules (comme Node.js et les bundlers de modules) vous permettent d'omettre le point et l'extension de fichier comme suit :

```js
// Importer trois éléments du fichier module-1.js :
import { bestClub, multiply, fruits } from "module-1";

```

Cependant, d'autres systèmes de modules, comme les modules ES, ne permettent pas de telles omissions.

**Note :**

* Un spécificateur de module sans point ni extension de fichier est appelé un spécificateur de module "nu".
* Un élément importé d'un module est une vue en lecture seule de la fonctionnalité exportée. Vous pouvez donc modifier le code uniquement à l'intérieur du module qui l'a exporté—pas dans le module qui l'a importé.
* JavaScript importe le code d'un module comme une liaison en direct. Donc, supposons que vous mettez à jour la valeur du code importé dans le module d'exportation. Dans ce cas, vos modifications se refléteront également dans le module d'importation.

Discutons maintenant de l'utilisation du code importé.

## Comment Utiliser le Code Importé d'un Module

Une fois que vous avez importé votre code, vous pouvez l'utiliser comme s'il avait été défini dans le module dans lequel vous l'avez importé.

**Voici un exemple :**

```js
// module-2.js

import { bestClub } from "./module-1.js";

const myBestClub = bestClub + " " + "est mon meilleur club.";

console.log(myBestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-ka4gdj?devtoolsheight=33&file=module-2.js)

**Note :**

* Le mot-clé `import` fonctionne uniquement à l'intérieur des modules—pas à l'intérieur des programmes JavaScript réguliers.
* Les fonctionnalités d'un module importé ne sont pas disponibles dans la portée globale. Vous pouvez donc accéder aux éléments importés uniquement dans le script dans lequel vous les avez importés—pas dans d'autres endroits comme la console JavaScript.
* JavaScript [hoiste](https://www.codesweetly.com/javascript-hoisting) les instructions `import`. Vous pouvez donc les définir n'importe où dans votre module.
* Les modules importés fonctionnent en mode strict par défaut—peu importe si vous avez spécifié l'instruction `strict`.

Maintenant que nous savons comment utiliser un module ES, discutons de la manière de renommer le code que vous souhaitez exporter (ou importer).

## Comment Renommer les Exportations et Importations dans les Modules ES

Supposons que vous souhaitiez renommer le code que vous exportez (ou importez). Dans ce cas, utilisez le mot-clé `as`.

**Voici un exemple :**

```js
// module-1.js

// Créer une variable nommée "bestClub" :
const bestClub = "Votre Club";

// Exporter la variable bestClub sous le nom "favoriteTeam" :
export { bestClub as favoriteTeam };

```

Dans l'extrait ci-dessus, nous avons dit à l'ordinateur d'exporter la variable `bestClub` _comme_ `favoriteTeam`.

Par conséquent, lors de l'importation de la variable, vous utiliserez le nom `favoriteTeam`—et non `bestClub`.

**Voici un exemple :**

```js
// module-2.js

import { favoriteTeam } from "./module-1.js";

const myBestClub = favoriteTeam + " " + "est mon meilleur club.";

console.log(myBestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-dltrvv?devtoolsheight=33&file=module-2.js)

Nous avons renommé la variable `bestClub` dans l'exemple ci-dessus lors de son exportation. Cependant, vous pouvez également la renommer lors de son importation.

**Voici un exemple :**

```js
// module-1.js

// Créer une variable nommée "bestClub" :
const bestClub = "Votre Club";

// Exporter la variable bestClub :
export { bestClub };

```

```js
// module-2.js

import { bestClub as favoriteTeam } from "./module-1.js";

const myBestClub = favoriteTeam + " " + "est mon meilleur club.";

console.log(myBestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-qrnt6y?devtoolsheight=33&file=module-2.js)

Le choix de renommer votre code lors de l'exportation ou de l'importation vous appartient entièrement.

Cependant, de nombreux développeurs préfèrent renommer lors de l'importation car vous n'avez pas toujours le contrôle sur le fichier source d'un code, surtout lors de l'importation depuis un module tiers.

## Pourquoi Renommer le Code d'un Module ?

Le renommage peut aider à prévenir les erreurs des navigateurs dues aux conflits de noms. Par exemple, considérons ces extraits :

```js
// module-1.js

// Créer une variable nommée "bestClub" :
const bestClub = "Votre Club";

// Exporter la variable bestClub :
export { bestClub };

```

```js
// module-2.js

import { bestClub } from "./module-1.js";

const bestClub = bestClub + " " + "est mon meilleur club.";

console.log(bestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-vvcy2d?devtoolsheight=33&file=module-2.js)

Lorsque vous exécutez les extraits ci-dessus, le navigateur lancera une erreur similaire à :

```js
"SyntaxError: Identifier 'bestClub' has already been declared"
```

Le navigateur a lancé l'erreur car le nom du code importé est en conflit avec la variable `bestClub` de `module-2.js`.

Cependant, vous pouvez rectifier l'erreur en renommant simplement le code importé comme suit :

```js
// module-2.js

import { bestClub as favoriteTeam } from "./module-1.js";

const bestClub = favoriteTeam + " " + "est mon meilleur club.";

console.log(bestClub);

```

Gardez à l'esprit que vous pouvez également renommer plusieurs exportations. Voyons comment ci-dessous.

## Comment Renommer Plusieurs Exportations dans un Module ES

Vous pouvez renommer plusieurs exportations en séparant chaque instruction `as` par une virgule.

**Voici un exemple :**

```js
// module-1.js

const bestClub = "Votre Club";
const fruits = ["Grape", "Apple", "Pineapple", "Lemon"];

function multiply(x, y) {
  return x * y;
}

// Exporter les trois instructions ci-dessus :
export { 
  bestClub as favoriteTeam, 
  fruits as crops, 
  multiply as product 
};

```

```js
// module-2.js

import { favoriteTeam, crops, product } from "./module-1.js";

const bestClub = `I bought ${product(2, 11)} ${crops[2]}s at ${favoriteTeam}.`;

console.log(bestClub);

```

**[Essayez-le sur StackBlitz](https://stackblitz.com/edit/web-platform-ir5f1h?devtoolsheight=33&file=module-1.js)**

Vous pouvez également renommer plusieurs importations. Voyons comment.

## Comment Renommer Plusieurs Importations dans un Module ES

Vous pouvez renommer plusieurs importations en séparant chaque instruction `as` par une virgule.

**Voici un exemple :**

```js
// module-1.js

const bestClub = "Votre Club";
const fruits = ["Grape", "Apple", "Pineapple", "Lemon"];
function multiply(x, y) {
  return x * y;
}

// Exporter les trois instructions ci-dessus :
export { bestClub, fruits, multiply };

```

```js
// module-2.js

import { 
  bestClub as favoriteTeam, 
  fruits as crops, 
  multiply as product 
} from "./module-1.js";

const bestClub = `I bought ${product(2, 11)} ${crops[2]}s at ${favoriteTeam}.`;

console.log(bestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-yinyru?devtoolsheight=33&file=module-2.js)

Supposons que vous souhaitiez importer tout le contenu exportable de `module-1.js` sans spécifier le nom de chaque importation. Comment pouvez-vous faire cela ? Découvrons-le.

## Comment Importer Tous les Éléments Exportables d'un Module ES en Une Seule Fois

Supposons que vous souhaitiez importer tous les éléments exportables d'un module spécifique sans spécifier le nom de chaque importation. Dans ce cas, utilisez la syntaxe `import * as` pour importer les éléments via un objet de module.

**Voici un exemple :**

```js
// Importer toutes les fonctionnalités exportables du module "countries.js" :
import * as allCountries from "./countries.js";

```

L'instruction ci-dessus indique à l'ordinateur d'importer tout le contenu exportable du module `./countries.js` et d'encapsuler les importations dans un objet de module nommé `allCountries`.

Après l'importation, vous pouvez utiliser les éléments importés comme avant. Cependant, vous devez maintenant y accéder via le nom de l'objet de module.

**Voici un exemple :**

```js
// module-1.js

const bestClub = "Votre Club";
const fruits = ["Grape", "Apple", "Pineapple", "Lemon"];
function multiply(x, y) {
  return x * y;
}

// Exporter les trois instructions ci-dessus :
export { bestClub, fruits, multiply };

```

```js
// module-2.js

import * as firstModule from "./module-1.js";

const bestClub = `I bought ${firstModule.multiply(2, 11)} ${firstModule.fruits[2]}s at ${firstModule.bestClub}.`;

console.log(bestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-s5bug2?devtoolsheight=33&file=module-2.js)

Alors, que faire si vous préférez exporter le contenu d'un module anonymement ? Discutons de la technique que vous pouvez utiliser.

## Comment Exporter Anonymement vers un Module ES

Jusqu'à présent, nous avons exporté des éléments en indiquant explicitement le nom du code spécifique que nous souhaitons partager—par exemple, `export { bestClub }`.

Une telle technique d'exportation est appelée **exportation nommée**.

Vous pouvez également exporter anonymement en utilisant la technique d'**exportation par défaut**. Mais qu'est-ce qu'une exportation par défaut exactement ? Découvrons-le.

### Qu'est-ce qu'une Exportation par Défaut dans les Modules ES ?

**Exportation par défaut** est une technique que les développeurs utilisent pour exporter du code anonymement (sans nom).

Vous pouvez implémenter une exportation par défaut en précédant le mot-clé `default` au code que vous souhaitez exporter. En faisant cela, l'ordinateur partagera le code comme une exportation par défaut.

En d'autres termes, le code sera exporté avec le nom spécial, `default`—au lieu de son nom d'origine (s'il en avait un).

Ainsi, lors de l'importation du code, vous aurez les options de l'importer avec le nom `default`, un nom personnalisé de votre choix, ou sans aucun nom.

**Voici un exemple :**

```js
// module-1.js

const bestClub = "Votre Club";

// Exporter la variable bestClub comme une exportation par défaut :
export default bestClub;

```

Nous n'avons pas utilisé d'accolades dans l'instruction d'exportation par défaut ci-dessus car vous ne pouvez avoir qu'une seule exportation par défaut dans un module.

Alternativement, vous pouvez également réécrire le code ci-dessus comme suit :

```js
// module-1.js

// Exporter la valeur de la chaîne comme une exportation par défaut :
export default "Votre Club";

```

Gardez à l'esprit que vous pouvez utiliser la technique d'exportation par défaut pour partager une fonction, une variable, une chaîne, une classe ou un littéral d'objet.

Cependant, vous ne pouvez pas préfixer le mot-clé `export default` à un mot-clé `var`, `let` ou `const`.

En d'autres termes, l'extrait ci-dessous lancera une `SyntaxError`.

```js
export default const bestClub = "Votre Club";
```

Discutons maintenant de l'importation d'une exportation par défaut.

### Comment Importer une Exportation par Défaut dans un Module ES

Il existe deux façons équivalentes d'importer une exportation par défaut :

* Utiliser la syntaxe `default as`
* Spécifier uniquement le nom du code importé

Discutons des deux techniques d'importation.

#### Comment utiliser la syntaxe `default as` pour importer une exportation par défaut

Une façon d'importer une exportation par défaut est d'utiliser la syntaxe `default as` comme suit :

```js
import { default as newName } from "./module-relative-path.js";
```

**Voici un exemple :**

```js
// module-1.js

// Exporter la valeur de la chaîne comme une exportation par défaut :
export default "Votre Club";

```

```js
// module-2.js

import { default as favoriteTeam } from "./module-1.js";

const bestClub = favoriteTeam + " " + "est mon meilleur club.";

console.log(bestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-zcyvst?devtoolsheight=33&file=module-2.js)

Remarquez que nous n'avons pas eu besoin de spécifier le nom du code que nous avons importé du fichier `module-1.js`. Au lieu de cela, nous avons utilisé le mot-clé `default` pour importer le code anonymement.

Ensuite, nous avons renommé le code importé _comme_ `favoriteTeam`.

Voyons maintenant la deuxième façon d'importer une exportation par défaut.

#### Comment importer une exportation par défaut en spécifiant uniquement le nom du code importé

Une autre façon d'importer une exportation par défaut est d'ignorer les accolades (`{...}`), le mot-clé `default` et le mot-clé `as`.

Au lieu de cela, spécifiez simplement le nom que vous souhaitez utiliser pour référencer le code importé comme suit :

```js
import newName from "./module-relative-path.js";
```

**Voici un exemple :**

```js
// module-1.js

// Exporter la valeur de la chaîne comme une exportation par défaut :
export default "Votre Club";

```

```js
// module-2.js

import favoriteTeam from "./module-1.js";

const bestClub = favoriteTeam + " " + "est mon meilleur club.";

console.log(bestClub);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-rgrlh7?devtoolsheight=33&file=module-2.js)

Vous pouvez voir que la technique d'importation raccourcie ci-dessus est plus propre que l'option précédente.

**Note :**

* L'instruction `export default` permet à un module JavaScript de s'interpoler (fonctionner de manière fiable) avec les systèmes de modules CommonJS et AMD existants.
* Consultez la section "[Default exports](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/)" de _ES6 In Depth: Modules_ pour en savoir plus sur l'interpolation.

Avant de conclure notre discussion sur les modules ES, vous devez savoir que vous pouvez utiliser un fichier d'agrégation pour colliger les instructions `import` de votre projet.

Mais qu'est-ce qu'un fichier d'agrégation, je vous entends demander ? Découvrons-le ci-dessous.

## Qu'est-ce qu'un Fichier d'Agrégation ?

Un **fichier d'agrégation** est un script utilisé uniquement pour importer et réexporter les éléments que vous avez exportés d'autres modules.

En d'autres termes, au lieu d'encombrer votre [module de premier niveau](https://www.codesweetly.com/web-tech-glossary#top-level-module-javascript) avec plusieurs instructions d'importation de divers fichiers, vous pouvez créer un seul script parent (le fichier d'agrégation).

Le seul but du script parent sera d'importer et de réexporter des éléments d'autres modules.

Ensuite, dans votre module de premier niveau, vous pouvez simplement importer tout code requis du fichier d'agrégation seul—pas de nombreux autres scripts.

En faisant cela, vous rendrez votre module de premier niveau plus propre.

Alors, que signifie tout cela exactement ? Voyons avec un mini-projet.

## Projet : Comment Utiliser un Fichier d'Agrégation

Suivez les étapes ci-dessous pour apprendre à utiliser un fichier d'agrégation.

### Étape 1 : Créer un répertoire de projet

Créez un dossier de projet—où les fichiers HTML et modules de ce projet résideront.

### Étape 2 : Créer vos fichiers de code

Créez les fichiers suivants à l'intérieur de votre dossier de projet :

1. `index.html`
2. `index.js`
3. `preferences.js`
4. `calculation.js`
5. `bio.js`

### Étape 3 : Ajouter les modules à votre document HTML

Ouvrez votre fichier `index.html` et reproduisez le code ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>Comment utiliser un fichier d'agrégation - Tutoriel sur les Modules ES</h1>
    <h2>Vérifiez la console</h2>

    <script type="module" src="index.js"></script>
    <script type="module" src="preferences.js"></script>
    <script type="module" src="calculation.js"></script>
    <script type="module" src="bio.js"></script>
  </body>
</html>

```

Voici les principales choses que nous avons faites dans l'extrait HTML ci-dessus :

1. Nous avons ajouté les quatre fichiers JavaScript à notre document HTML.
2. Nous avons utilisé l'attribut `type="module"` pour convertir les fichiers JavaScript réguliers en fichiers de module ES.

### Étape 4 : Exporter des éléments de votre module `preference`

Ouvrez votre module `preferences.js` et exportez certains éléments comme suit :

```js
const bestFruits = ["Grape", "Apple", "Pineapple", "Lemon"];
const bestColor = "White";
const bestNumber = 111;
const bestClub = "Votre Club";
const bestTime = "Now";

export { bestClub, bestFruits };

```

### Étape 5 : Exporter des éléments de votre module `calculation`

Ouvrez votre module `calculation.js` et exportez certains éléments comme suit :

```js
function add(x, y) {
  return x + y;
}

function subtract(x, y) {
  return x - y;
}

export function multiply(x, y) {
  return x * y;
}

function divide(x, y) {
  return x / y;
}

```

### Étape 6 : Exporter des éléments de votre module `bio`

Ouvrez votre module `bio.js` et exportez certains éléments comme suit :

```js
const aboutMe = {
  firstName: "Oluwatobi",
  lastName: "Sofela", 
  companyName: "CodeSweetly",
  profession: "Web Developer",
  gender: "Male",
};

export default aboutMe;

```

### Étape 7 : Importer les fonctionnalités exportées

Pour importer les éléments exportés dans votre module de premier niveau, vous avez deux options :

1. Importer directement des modules d'exportation vers votre script de premier niveau.
2. Importer depuis un fichier d'agrégation vers votre module de premier niveau.

Voyons la différence entre les deux options.

#### Importer directement des modules d'exportation vers votre script de premier niveau

Une façon d'importer votre code est de l'importer directement des scripts d'exportation vers votre module de premier niveau.

Par exemple, ouvrez votre fichier `index.js` et importez le contenu exporté des modules `preferences.js`, `calculation.js` et `bio.js` comme suit :

```js
// index.js

import { bestFruits } from "./preferences.js";
import { multiply } from "./calculation.js";
import aboutMe from "./bio.js";

const news = `All ${aboutMe.companyName}'s staff gave Tom ${multiply(7, 129)} ${bestFruits[2]}s.`;

console.log(news);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-dqmd1u?devtoolsheight=33&file=index.js)

Vous pouvez voir que nous avons importé des éléments directement depuis trois scripts d'exportation dans le module `index.js`.

La technique d'importation ci-dessus fonctionne bien. Cependant, une alternative plus propre est d'utiliser un fichier d'agrégation. Voyons comment.

#### Importer depuis un fichier d'agrégation vers votre module de premier niveau

Une autre façon d'importer votre code est de l'importer depuis un fichier d'agrégation vers votre module de premier niveau.

Suivez les étapes ci-dessous pour voir comment vous pouvez créer et utiliser un fichier d'agrégation.

##### 1. Créer le fichier d'agrégation

Vous pouvez nommer le fichier `aggregator.js` ou tout autre nom que vous préférez.

![Créer un fichier d'agrégation - Tutoriel sur les Modules](https://www.freecodecamp.org/news/content/images/2022/05/module-tutorial-aggregator-file-highlight-codesweetly.png)
_Mise en évidence du fichier d'agrégation du projet_

##### 2. Ajouter le script d'agrégation à votre fichier HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>Comment utiliser un fichier d'agrégation - Tutoriel sur les Modules ES</h1>
    <h2>Vérifiez la console</h2>

    <script type="module" src="index.js"></script>
    <script type="module" src="preferences.js"></script>
    <script type="module" src="calculation.js"></script>
    <script type="module" src="bio.js"></script>
    <script type="module" src="aggregator.js"></script>
  </body>
</html>

```

Notez ce qui suit :

1. `index.js` est le [module de premier niveau](https://www.codesweetly.com/web-tech-glossary#top-level-module-javascript) car c'est le fichier où nous avons importé et utilisé `preferences.js`, `calculation.js` et `bio.js`.
2. `preferences.js`, `calculation.js` et `bio.js` sont les [sous-modules](https://www.codesweetly.com/web-tech-glossary#submodule-javascript) car ce sont les fichiers que nous avons importés dans le module de premier niveau.
3. `aggregator.js` est le [module parent](https://www.codesweetly.com/web-tech-glossary#parent-module-es-module) car c'est le script pour agréger et réexporter les trois sous-modules.

Techniquement, vous pouvez indiquer uniquement le module de premier niveau dans le fichier HTML de votre projet comme suit :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>Comment utiliser un fichier d'agrégation - Tutoriel sur les Modules ES</h1>
    <h2>Vérifiez la console</h2>

    <script type="module" src="index.js"></script>
  </body>
</html>

```

En faisant cela, vous évitez d'encombrer votre page HTML avec les sous-modules et le module parent.

Voyons maintenant comment utiliser le module d'agrégation.

##### 3. Utiliser le module d'agrégation pour agréger les sous-modules

Voici comment utiliser le module d'agrégation pour importer et réexporter tous les éléments exportés de votre projet :

```js
// aggregator.js

import { bestFruits } from "./preferences.js";
import { multiply } from "./calculation.js";
import aboutMe from "./bio.js";

export { bestFruits, multiply, aboutMe };

```

Vous pouvez voir que nous avons utilisé le fichier d'agrégation uniquement pour importer et réexporter les fonctionnalités exportées de notre projet.

La manière abrégée d'écrire les instructions `import`/`export` ci-dessus est la suivante :

```js
// aggregator.js

export { bestFruits } from "./preferences.js";
export { multiply } from "./calculation.js";
export { default as aboutMe } from "./bio.js";

```

Gardez à l'esprit que la syntaxe suivante est invalide :

```js
export aboutMe from "./bio.js";
```

En d'autres termes, chaque fois que vous utilisez la syntaxe `export...from` pour réexporter une exportation par défaut, assurez-vous de renommer la réexportation comme suit :

```js
export { default as aboutMe } from "./bio.js";
```

Voyons maintenant comment importer les fonctionnalités réexportées depuis un fichier d'agrégation.

##### 4. Importer vos exportations depuis le fichier d'agrégation

Une fois que vous avez agrégé tous vos sous-modules dans le module d'agrégation, allez dans votre script de premier niveau (`index.js` dans ce cas) et importez les éléments exportés.

**Voici un exemple :**

```js
// index.js

import { bestFruits, multiply, aboutMe } from "./aggregator.js";

const news = `All ${aboutMe.companyName}'s staff gave Tom ${multiply(7, 129)} ${bestFruits[2]}s.`;

console.log(news);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-fttqqb?devtoolsheight=33&file=index.js)

Vous voyez, comme par magie, nous avons nettoyé notre code en remplaçant trois instructions `import` par une seule ligne !

L'utilisation d'un fichier d'agrégation pour colliger les exportations de votre projet aide à séparer les préoccupations et rend votre module de premier niveau plus propre.

Jusqu'à présent, nous avons utilisé la syntaxe `import` statique pour indiquer à l'ordinateur d'évaluer le code des modules importés au moment du chargement.

Mais supposons que vous préférez charger vos modules de manière conditionnelle ou à la demande. Dans ce cas, vous pouvez utiliser la syntaxe `import()` dynamique. Voyons exactement comment cela fonctionne ci-dessous.

## Comment Utiliser la Syntaxe `import()` pour Charger un Module Dynamiquement

Pour charger votre module de manière conditionnelle ou à la demande, utilisez la syntaxe `import()` comme suit :

```js
import("./module/relative-path.js").then(function (module) { });
```

La syntaxe `import()` fait deux choses principales :

1. Elle charge son argument de spécificateur de module (`"./module/relative-path.js"` dans ce cas).
2. Elle retourne un objet de promesse qui se résout en un objet de module contenant les exportations du spécificateur d'importation.

Ainsi, puisque la syntaxe `import()` retourne une promesse, vous pouvez également utiliser le mot-clé `await` avec elle.

**Voici un exemple :**

```js
const module = await import("./module/relative-path.js");
```

**Note :** Bien que `import()` ressemble à un appel de fonction, ce n'en est pas un. Au lieu de cela, le code `import()` est une syntaxe spéciale des modules ES qui utilise des parenthèses (similaires à la syntaxe [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)).

Par conséquent, vous ne pouvez pas [appeler](https://www.codesweetly.com/call-apply-bind-javascript/#what-is-the-call-method), [appliquer](https://www.codesweetly.com/call-apply-bind-javascript/#what-is-the-apply-method), ou [lier](https://www.codesweetly.com/call-apply-bind-javascript/#what-is-the-bind-method) la syntaxe `import()` car elle n'hérite pas des propriétés de `Function.prototype`.

Pour voir précisément comment `import()` fonctionne en pratique, mettons à jour notre projet précédent en suivant les étapes ci-dessous.

### 1. Mettre à jour votre fichier HTML

Ouvrez votre fichier `index.html` et faites ce qui suit :

1. Mettez à jour le contenu de votre `<h1>` en "The Latest News".
2. Remplacez l'élément `<h2>` par un élément `<p>` vide.
3. Créez un élément `<button>`.

En d'autres termes, votre fichier `index.html` devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>The Latest News</h1>
    <p id="news-paragraph"></p>
    <button id="news-button">Get the News</button>

    <script type="module" src="index.js"></script>
  </body>
</html>

```

### 2. Mettre à jour votre module `index.js`

Ouvrez votre fichier `index.js` et reproduisez le code ci-dessous :

```js
// index.js

const paragraphElement = document.getElementById("news-paragraph");
const buttonElement = document.getElementById("news-button");

async function displayNews() {
  let news = null;
  // highlight-next-line
  const aggregatorModule = await import("./aggregator.js");
 
  news = `All ${aggregatorModule.aboutMe.companyName}'s staff gave Tom ${aggregatorModule.multiply(7, 129)} ${aggregatorModule.bestFruits[2]}s.`;

  paragraphElement.innerText = news;
}

buttonElement.addEventListener("click", displayNews);

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-pw3xpq?file=index.js)

Vous pouvez voir comment nous avons utilisé la méthode `import()` pour charger le module d'agrégation à la demande (quand un utilisateur clique sur le bouton)—plutôt qu'au démarrage.

Bien que l'importation dynamique puisse améliorer les performances de temps de chargement initial de votre programme, il est préférable de l'utiliser uniquement lorsque cela est nécessaire.

**Note :** La méthode `import()` n'exige pas que son [argument](https://www.codesweetly.com/javascript-arguments) ait un `<script>` de `type="module"`. Vous pouvez donc l'utiliser dans un fichier JavaScript régulier.

Maintenant, supposons que vous souhaitiez obtenir des [métadonnées](https://en.wikipedia.org/wiki/Metadata) sur votre module actuel. Dans ce cas, vous pouvez utiliser la syntaxe `import.meta`.

## Qu'est-ce que `import.meta` dans les Modules ES ?

Le code `import.meta` est un objet contenant des informations sur votre module actuel.

**Voici un exemple :**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body>
    <h1>À propos de import.meta</h1>
    <h2>Vérifiez la console ⬇⬇⬇</h2>

    <script type="module">
      console.log(import.meta);
      console.log(import.meta.url);
    </script>
  </body>
</html>

```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-8ky5vd?devtoolsheight=33&file=index.html)

Le code `import.meta` dans l'extrait ci-dessus retournera certaines informations sur le module dans lequel il a été utilisé.

## Révision Rapide des Modules Jusqu'à Présent

Nous avons appris qu'un module JavaScript est simplement un fichier avec une capacité supplémentaire à partager son code avec d'autres modules au sein d'un projet—ou [avec le monde](https://www.codesweetly.com/package-manager-explained/#how-to-publish-your-project-to-the-npm-registry) via des gestionnaires de paquets comme Yarn et NPM.

Nous avons également utilisé un serveur local pour charger nos documents HTML via un schéma `http://`—ce qui a permis aux navigateurs de charger nos applications sans lancer d'erreur CORS.

Cependant, les serveurs en direct sont limités aux développements et tests locaux.

En d'autres termes, vous ne pouvez pas utiliser un serveur en direct en production pour servir votre document HTML via un schéma `http://`. Au lieu de cela, il serait préférable d'utiliser un _bundler de modules_.

Mais qu'est-ce qu'un bundler de modules, je vous entends demander ? Découvrons-le ci-dessous.

## Qu'est-ce qu'un Bundler de Modules ?

Un **bundler de modules** est un outil que les développeurs utilisent pour regrouper les [modules](#heading-quest-ce-quun-module-javascript) et les dépendances d'une application dans un seul fichier JavaScript compatible avec les navigateurs.

## Pourquoi Avez-Vous Besoin d'un Bundler de Modules ?

Les bundlers de modules permettent aux navigateurs d'accéder au fichier que vous avez spécifié dans une instruction `require()` ou `import`.

En d'autres termes, supposons qu'un navigateur exécute un fichier JavaScript avec une instruction `require("./node_module/test/sample/app.js")`. Dans ce cas, le navigateur lancera une erreur disant `Uncaught ReferenceError: require is not defined`.

L'ordinateur lancera une telle erreur car les navigateurs ne peuvent pas accéder aux fichiers spécifiés dans un programme JavaScript.

Cependant, vous pouvez utiliser un bundler de modules pour créer un nouveau fichier JavaScript contenant du code que les navigateurs peuvent lire.

## Comment Fonctionne un Bundler de Modules ?

Un bundler de modules effectue son travail de bundling comme suit :

### Tout d'abord, il crée un fichier de script de sortie

Le bundler de modules créera d'abord un "fichier de script de sortie" dans le dossier `dist` de votre projet.

**Note :**

* Le bundler utilise le _fichier de script de sortie_ pour sauvegarder le code bundlé.
* Un **fichier de sortie** est la version compilée d'un fichier d'entrée. En d'autres termes, un fichier de script de sortie fait référence au fichier JavaScript qu'un bundler génère automatiquement pour votre projet.
* Un **point d'entrée** est un fichier qu'un bundler utilise pour commencer à construire un [graphe de dépendances](https://webpack.js.org/concepts/dependency-graph/) de tous les modules du projet dont il a besoin pour combiner en un seul module compatible avec les navigateurs.
* Un point d'entrée est le fichier le plus critique d'une étape de construction qui lie (directement ou indirectement) à chaque autre module d'un projet.

### Ensuite, le bundler de modules compile votre code

Deuxièmement, le bundler vérifiera le point d'entrée de l'étape de construction pour toute occurrence de certaines instructions `require()` ou `import`.

Supposons que le bundler de modules trouve une instruction `require()` ou `import`. Dans ce cas, le bundler compilera (combinera) le contenu de chaque dépendance spécifiée dans les instructions avec le contenu du point d'entrée.

**Note :**

* Une **étape de construction** est un processus par lequel un bundler de modules construit un nouveau fichier JavaScript compatible avec les navigateurs.
* Le fichier de sortie d'une étape de construction est parfois appelé un **code de distribution**. En d'autres termes, le code de distribution est la version minifiée et optimisée du code source.
* Une **dépendance** est un fichier dont votre script a besoin pour fonctionner comme prévu. Donc, dans `import { variable } from "./path/to/module.js"`, `module.js` est le fichier de dépendance car c'est un script dont notre application dépend pour fonctionner comme conçu.

Discutons maintenant de la dernière chose qu'un bundler de modules fait.

### Enfin, il sauvegarde le code compilé

La dernière étape d'un bundler de modules est de sauvegarder le code compilé dans le [fichier de script de sortie de l'étape 1](#heading-tout-dabord-il-cree-un-fichier-de-script-de-sortie).

En conséquence, le fichier de script de l'étape 1 (la sortie de l'étape de construction) contiendra le contenu du point d'entrée et de ses dépendances—mais aucune instruction `require()` ou `import`.

**Note :** Des exemples typiques de bundlers de modules sont [webpack](https://webpack.js.org), [browserify](http://browserify.org/), [rollup](https://rollupjs.org/guide/en/), et [parcel](https://parceljs.org/).

Maintenant que nous savons comment fonctionne un bundler de modules, discutons de l'utilisation d'un bundler populaire—_Webpack_.

## Comment Utiliser Webpack

Suivez les étapes ci-dessous pour apprendre à utiliser Webpack afin de regrouper le fichier JavaScript de votre projet et ses dépendances en un seul fichier de script de sortie.

### Étape 1 : Créer un répertoire de projet

Créez un dossier de projet—où les fichiers de ce projet résideront.

### Étape 2 : Aller dans le dossier racine du projet

En utilisant la ligne de commande, naviguez jusqu'au répertoire racine de votre projet comme suit :

```bash
cd path/to/project/root-directory
```

**Note :** Un **répertoire racine** est un dossier contenant tous les autres fichiers et sous-dossiers d'un projet spécifique.

En d'autres termes, le dossier que vous avez créé à l'étape 1 est votre dossier racine car il abritera tout ce qui concerne ce projet particulier.

### Étape 3 : Créer un fichier `package.json`

Créez un fichier [package.json](https://www.codesweetly.com/package-json-file-explained) dans le répertoire racine de votre projet comme suit :

```bash
npm init -y
```

Alternativement, vous pouvez utiliser Yarn comme ceci :

```bash
yarn init -y
```

**Note :**

* Le drapeau `-y` indique à NPM (ou Yarn) de [créer un fichier `package.json` par défaut](https://www.codesweetly.com/package-json-file-explained/#how-to-create-a-default-packagejson-file).
* Vous devez avoir Node et NPM installés sur votre système pour que le code d'initialisation ci-dessus fonctionne. Vous pouvez obtenir les deux en installant la dernière version LTS depuis le site [Node.js](https://nodejs.org/en/).

### Étape 4 : Installer le bundler de modules Webpack

Installez `webpack` et `webpack-cli` localement dans votre projet en tant que bibliothèques de [dépendance de développement](https://www.codesweetly.com/package-manager-explained/#npm-installation-command) :

```bash
npm install webpack webpack-cli --save-dev
```

Ou, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn add webpack webpack-cli --dev
```

**Note :** Le package `webpack-cli` permet d'exécuter webpack sur la ligne de commande.

### Étape 5 : Créer les répertoires de votre projet

Créez un dossier de code "source" (`./src`) et un dossier de code "distribution" (`./dist`).

```bash
mkdir src dist
```

**Note :** Bien que `src` et `dist` soient les noms typiquement donnés aux dossiers de code source et de distribution, vous êtes libre de choisir tout autre nom que vous préférez.

### Étape 6 : Créer vos fichiers de code source

Créez les fichiers suivants à l'intérieur du répertoire de code source nouvellement créé :

1. `index.html`
2. `index.js`

**Note :**

* Webpack recommande de sauvegarder le [code source](https://www.codesweetly.com/web-tech-glossary#source-code) dans un répertoire `./src` et le [code de distribution](https://www.codesweetly.com/web-tech-glossary#distribution-code) dans un répertoire `./dist`.
* Webpack ne modifie aucun autre code à part les instructions `require()`, `import` et `export`.

### Étape 7 : Ajouter le fichier JavaScript à votre document HTML

Ouvrez votre fichier `index.html` et reproduisez le code ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body id="body">
    <h1>Tutoriel sur le Bundler de Modules</h1>
    <button id="button">Cliquez-moi pour changer de couleur !</button>

    <script src="./index.js"></script>
  </body>
</html>

```

Voici les principales choses que nous avons faites dans l'extrait HTML ci-dessus :

1. Nous avons créé un élément `<h1>` et `<button>`.
2. Nous avons ajouté le fichier JavaScript de l'étape 6 à notre document HTML.

**Note :** Lorsque vous utilisez un bundler, vous n'avez pas besoin d'ajouter l'attribut `type="module"` à l'élément `<script>` de votre projet. Au lieu de cela, le bundler traitera automatiquement tous les scripts contenant des instructions `import` et `export` comme des modules.

### Étape 8 : Installer certaines dépendances

En utilisant votre éditeur de texte, [installez les dépendances de votre projet localement](https://www.codesweetly.com/package-manager-explained/#local-package-installation).

Par exemple, voici comment vous pouvez installer le package [randomColor](https://www.npmjs.com/package/randomcolor) comme une dépendance locale :

```bash
npm install randomcolor --save
```

**Note :**

* Utilisez la commande `npm install package-name --save` pour les dépendances dont votre application a besoin en production.
* Utilisez la commande `npm install package-name --save-dev` pour les dépendances dont votre application a besoin uniquement pour son développement et ses tests locaux.

Alternativement, vous pouvez utiliser Yarn comme suit :

```bash
yarn add randomcolor
```

**Note :** Utilisez la commande `yarn add package-name --dev` pour les dépendances dont votre application a besoin uniquement pour son développement et ses tests locaux.

### Étape 9 : Importer vos dépendances

Importez vos dépendances dans votre code source JavaScript avec la méthode `require()` ou l'instruction `import`.

Par exemple, voici comment utiliser l'instruction `import` pour importer la dépendance `randomColor` de l'étape 8 dans votre fichier de script `index.js` :

```js
// index.js

import randomColor from "randomcolor";

```

L'équivalence de la méthode `require()` de l'extrait ci-dessus est la suivante :

```js
// index.js

const randomColor = require("randomcolor");

```

**Note :**

* L'instruction `import` est la méthode native de JavaScript pour importer des modules.
* La fonction `require()` est la syntaxe CommonJS pour importer des modules dans un script.
* Une autre façon d'importer les dépendances de votre projet est de les charger implicitement avec la balise `<script>` de votre document HTML. Cependant, une telle technique pollue la portée globale. Il est donc préférable d'utiliser la syntaxe `import` ou `require()`.

### Étape 10 : Utiliser les dépendances

Utilisez les dépendances que vous avez importées à l'étape 9 pour faire ce que vous désirez.

Par exemple, voici comment vous pouvez utiliser la dépendance `randomColor` :

```js
// index.js

import randomColor from "randomcolor";

const bodyElement = document.getElementById("body");
const buttonElement = document.getElementById("button");

function changeBodyColor() {
  const color = randomColor();
  bodyElement.style.backgroundColor = color;
}

buttonElement.addEventListener("click", changeBodyColor);

```

Dans l'extrait ci-dessus, nous avons dit à l'ordinateur que chaque fois qu'un utilisateur clique sur le `buttonElement`, il doit :

1. Invoquer la fonction `changeBodyColor`.
2. Initialiser la variable `color` de la fonction avec la sortie d'[invocation](https://www.codesweetly.com/declaration-initialization-invocation-in-programming/#what-does-invocation-mean-in-programming) de `randomColor`.
3. Utiliser la valeur de la variable `color` pour styliser la couleur de fond de `bodyElement`.

Regroupons maintenant notre point d'entrée (le fichier `index.js`) et la dépendance `randomColor` en un seul fichier JavaScript.

### Étape 11 : Démarrer l'étape de construction

En utilisant votre terminal, créez votre bundle en exécutant webpack comme suit :

```bash
npx webpack
```

Après avoir exécuté la commande ci-dessus, webpack fera ce qui suit :

1. Il utilisera votre `index.js` comme point d'entrée.
2. Il créera un bundle (le fichier de sortie) dans le dossier `dist` de votre projet contenant le contenu du point d'entrée et de ses dépendances.

**Note :**

* Par défaut, Webpack génère son bundle sous forme de fichier `main.js`—qu'il sauvegardera dans le dossier de distribution que vous avez créé à l'étape 5. Cependant, vous pouvez modifier le paramètre par défaut en créant un fichier de configuration—que Webpack utilisera automatiquement. Nous discuterons de la création et de l'utilisation d'un fichier de configuration [plus tard](#heading-quest-ce-que-le-fichier-de-configuration-de-webpack) dans ce guide.
* [NPX](https://nodejs.dev/learn/the-npx-nodejs-package-runner) est l'exécuteur de paquets de Node qui trouvera et exécutera automatiquement Webpack.

Notre prochaine étape est de dire aux navigateurs d'utiliser le nouveau bundle créé. Faisons cela ci-dessous.

### Étape 12 : Référencer les navigateurs au nouveau bundle créé

Maintenant que vous avez créé un fichier bundle compatible avec les navigateurs, vous devez dire aux navigateurs de l'utiliser au lieu du fichier de code source `index.js`.

Par conséquent, allez dans votre fichier HTML et remplacez la référence à votre code source JavaScript par le bundle de distribution de Webpack.

Par exemple, au lieu d'utiliser `"./index.js"` dans la balise `<script>` de votre fichier HTML, vous utiliseriez `"../dist/main.js"` comme suit :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body id="body">
    <h1>Tutoriel sur le Bundler de Modules</h1>
    <button id="button">Cliquez-moi pour changer de couleur !</button>

    <script src="../dist/main.js"></script>
  </body>
</html>

```

Vérifions maintenant notre application !

### Étape 13 : Vérifier votre application dans le navigateur

Ouvrez votre fichier HTML dans le navigateur pour confirmer que le navigateur peut lire avec succès votre application et ses dépendances.

Rappelez-vous que vous avez créé votre fichier HTML manuellement dans [l'étape 6](#heading-etape-6-creer-vos-fichiers-de-code-source). Cependant, Webpack peut également en générer un automatiquement pour vous. Découvrons comment.

## Comment Faire en Sorte que Webpack Génère Automatiquement le Fichier HTML de Votre Application

Supposons que votre application génère maintenant plusieurs bundles, ou que vous avez commencé à [utiliser des hachages](https://www.codesweetly.com/javascript-module-bundler#substitutions-technique-3-content-hash) pour créer des noms de fichiers uniques. Dans ce cas, vous pourriez trouver de plus en plus difficile de gérer votre fichier HTML manuellement.

Par conséquent, Webpack vous permet d'utiliser le [HtmlWebpackPlugin](https://webpack.js.org/plugins/html-webpack-plugin/) pour générer et gérer automatiquement le fichier `index.html` de votre projet.

Suivez les étapes ci-dessous pour apprendre à utiliser `HtmlWebpackPlugin` pour générer et gérer automatiquement le fichier HTML de votre projet.

### Étape 1 : Installer `HtmlWebpackPlugin`

Installez le `HtmlWebpackPlugin` comme suit :

```bash
npm install html-webpack-plugin --save-dev
```

Ou, si votre gestionnaire de paquets est Yarn, utilisez :

```bash
yarn add html-webpack-plugin --dev
```

### Étape 2 : Créer un fichier de configuration

Créez un fichier de configuration Webpack dans le [dossier racine](https://www.codesweetly.com/web-tech-glossary#root-directory) de votre projet comme suit :

```bash
touch webpack.config.js
```

### Étape 3 : Ajouter le plugin à la configuration de webpack

Ouvrez votre fichier `webpack.config.js` et ajoutez le plugin `HtmlWebpackPlugin` comme suit :

```js
// webpack.config.js

const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = { 
  plugins: [new HtmlWebpackPlugin()] 
}

```

**Note :** Nous discuterons de l'utilisation d'un fichier de configuration [plus tard](#heading-quest-ce-que-le-fichier-de-configuration-de-webpack) dans ce guide.

### Étape 4 : Exécuter l'étape de construction

Une fois que vous avez installé et ajouté `HtmlWebpackPlug` à votre projet, recompilez vos modules comme suit :

```bash
npx webpack
```

Après avoir exécuté l'étape de construction, `HtmlWebpackPlugin` fera ce qui suit :

1. Il générera automatiquement un nouveau fichier `index.html`.
2. Le plugin insérera automatiquement les bundles que Webpack a générés dans le document HTML nouvellement créé.
3. Il sauvegardera automatiquement le nouveau fichier HTML à l'intérieur du dossier de distribution de votre projet.

En d'autres termes, après avoir exécuté une construction, l'invocation de `new HtmlWebpackPlugin()` (dans le fichier de configuration) générera automatiquement un fichier `dist/index.html` avec le contenu suivant :

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Webpack App</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <script defer src="main.js"></script>
  </head>
  <body>
  </body>
</html>

```

Remarquez que le document HTML généré par `HtmlWebpackPlugin` ne contient pas les éléments `<h1>` et `<button>` de votre fichier source.

En d'autres termes, supposons que vous ouvrez le fichier `dist/index.html` dans le navigateur. Dans ce cas, le navigateur ouvrira une page HTML vide.

Le `HtmlWebpackPlugin` a omis le contenu de l'élément `<body>` du code source car il n'a pas créé le nouveau fichier à partir du document original. Au lieu de cela, il a automatiquement créé une nouvelle page HTML qui inclut uniquement les bundles générés par Webpack.

Cependant, vous pouvez également dire à `HtmlWebpackPlugin` d'utiliser votre fichier source comme modèle. Voyons comment ci-dessous.

## Comment Faire en Sorte que `HtmlWebpackPlugin` Utilise Votre Fichier Source comme Modèle pour Générer Automatiquement une Nouvelle Page HTML

Pour faire en sorte que `HtmlWebpackPlugin` utilise votre fichier HTML source comme modèle, procédez comme suit :

### 1. Mettre à jour votre fichier HTML

Ouvrez votre fichier HTML _source_ `index.html` et supprimez la balise `<script>` que vous avez [précédemment utilisée](#heading-etape-12-referencer-les-navigateurs-au-nouveau-bundle-cree) pour référencer le bundle de distribution de Webpack.

Ainsi, votre code source HTML devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
  </head>
  <body id="body">
    <h1>Tutoriel sur le Bundler de Modules</h1>
    <button id="button">Cliquez-moi pour changer de couleur !</button>
  </body>
</html>

```

Nous avons supprimé le script du bundle codé à la main car `HtmlWebpackPlugin` en insérera automatiquement un lors de la génération automatique du nouveau fichier HTML.

**Rappelez-vous :** Le plugin utilisera votre code source comme modèle pour créer le nouveau fichier. Par conséquent, la suppression de la référence au bundle codé à la main aide à éviter les conflits de scripts.

Configurons maintenant le plugin pour utiliser votre code source comme modèle.

### 2. Mettre à jour votre fichier de configuration

Ouvrez le fichier `webpack.config.js` de votre projet et mettez à jour les paramètres de `HtmlWebpackPlugin` comme suit :

```js
// webpack.config.js

const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = { 
  plugins: [new HtmlWebpackPlugin({
    template: "./src/index.html"
  })] 
}

```

Dans l'extrait de configuration ci-dessus, nous avons fait ce qui suit :

1. Nous avons passé un argument d'objet contenant une propriété `template` à la fonction `HtmlWebpackPlugin`.
2. Nous avons initialisé la propriété `template` avec le chemin vers notre code source HTML.

Ainsi, si vous exécutez maintenant la commande `npx webpack`, `HtmlWebpackPlugin` utilisera `./src/index.html` comme modèle pour générer le nouveau fichier `dist/index.html`.

Par conséquent, le fichier HTML de distribution nouvellement créé ressemblera à ceci :

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module ES - CodeSweetly</title>
    <script defer="defer" src="main.js"></script>
  </head>
  <body id="body">
    <h1>Tutoriel sur le Bundler de Modules</h1>
    <button id="button">Cliquez-moi pour changer de couleur !</button>
  </body>
</html>

```

Supposons qu'un fichier `index.html` existe déjà dans votre répertoire de sortie (`dist`). Dans ce cas, le nouveau fichier généré par `HtmlWebpackPlugin` remplacera le fichier HTML existant.

### 3. Vérifier votre application dans le navigateur

Ouvrez le fichier `dist/index.html` nouvellement généré dans le navigateur pour confirmer que le navigateur peut lire avec succès votre application et ses dépendances.

**Note :**

* `HtmlWebpackPlugin` vous permet de spécifier comment et où vous souhaitez qu'il génère votre fichier HTML en fournissant des [options de configuration](https://github.com/jantimon/html-webpack-plugin#options) spécifiques. Par exemple, `new HtmlWebpackPlugin({ title: "A CodeSweetly Project" })` indique au plugin d'utiliser `"A CodeSweetly Project"` comme titre du fichier HTML généré.
* Supposons que vous obtenez un message d'erreur (par exemple, `ReferenceError: __webpack_base_uri__ is not defined`). Dans ce cas, vous devez probablement mettre à jour votre dépendance Webpack. Vous pouvez le faire en exécutant `npm update webpack webpack-cli` sur votre terminal.

## Choses Importantes à Savoir sur la Mise à Jour de Votre Application

Chaque fois que vous apportez des modifications à votre code source, assurez-vous de faire ce qui suit pour que vos mises à jour se reflètent dans le navigateur :

1. Relancez l'étape de construction.
2. Rafraîchissez votre navigateur.

Répéter manuellement le processus de relance de l'étape de construction et de rafraîchissement de votre navigateur peut être fastidieux. Heureusement, Webpack offre un moyen d'automatiser les deux tâches. Découvrons comment.

## Comment Relancer Webpack Automatiquement

Supposons que vous souhaitiez automatiser le processus de relance de l'étape de construction. Dans ce cas, vous pouvez ajouter une propriété `watch` au champ `scripts` de votre [package.json](https://www.codesweetly.com/package-json-file-explained/).

Par exemple, procédez comme suit :

### 1. Ajouter `watch` aux champs `scripts`

Ouvrez le fichier `package.json` de votre projet et ajoutez une propriété `watch` à son champ `scripts` comme suit :

```json
{
  "name": "your_package",
  "version": "1.0.0",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "watch": "webpack --progress --watch"
  }
}

```

L'extrait ci-dessus a ajouté une propriété `"watch"`—avec la valeur `"webpack --progress --watch"`—au champ `"scripts"` de notre fichier `package.json`.

### 2. Exécuter le script `watch`

En utilisant votre terminal, invoquez le script `watch` de votre `package.json` comme suit :

```bash
npm run watch
```

Alternativement, vous pouvez utiliser Yarn comme ceci :

```bash
yarn run watch
```

Une fois que vous avez invoqué le script `watch`, NPM exécutera `"webpack --progress --watch"`.

### Qu'est-ce que `"webpack --progress --watch"` ?

La commande `"webpack --progress --watch"` indique à NPM de :

1. Exécuter Webpack.
2. Passer les options `--progress` et `--watch` à la configuration de Webpack.

L'option `--progress` fera en sorte que NPM affiche le pourcentage de progression de la compilation de Webpack.

L'option `--watch` active le mode de surveillance de Webpack.

En d'autres termes, `--watch` indique à Webpack de surveiller et de recompiler automatiquement vos modules chaque fois que vous enregistrez des modifications dans les fichiers de votre graphe de dépendances.

À titre d'exemple, allez dans votre fichier `index.js` et ajoutez une instruction `console.log` à la fonction `changeBodyColor()` comme suit :

```js
// index.js

import randomColor from "randomcolor";

const bodyElement = document.getElementById("body");
const buttonElement = document.getElementById("button");

function changeBodyColor() {
  const color = randomColor();
  bodyElement.style.backgroundColor = color;
  console.log(color);
}

buttonElement.addEventListener("click", changeBodyColor);

```

Ensuite, enregistrez vos modifications. Puis rafraîchissez votre navigateur.

Après le rafraîchissement, faites ce qui suit :

1. Ouvrez la console de votre navigateur.
2. Cliquez sur le bouton `"Click Me to Change Color!"` de votre application.

Vous pouvez voir que le drapeau `--watch` a automatiquement recompilé vos modules lorsque vous avez enregistré les modifications de votre code source.

Par conséquent, vous n'avez plus besoin d'exécuter manuellement la commande `npx webpack` à nouveau. Au lieu de cela, le drapeau `--watch` surveillera et recompilera automatiquement vos modules chaque fois que vous enregistrerez des modifications.

**Note :**

* Après avoir exécuté `npm run watch`, votre terminal actuellement ouvert continuera à traiter les activités de la commande `watch`. Vous ne pourrez donc pas entrer de commande sur ce terminal jusqu'à ce que vous arrêtiez l'exécution de `watch`. Cependant, vous pouvez ouvrir une nouvelle fenêtre de terminal à utiliser simultanément avec celle qui traite `watch`. En d'autres termes, utilisez un terminal pour exécuter `watch` et un autre pour entrer des commandes.
* Pour arrêter l'exécution de `watch`, utilisez `ctrl + c` sur Windows ou `cmd + c` sur Mac.
* Vous pouvez renommer la clé `"watch"` (ou toute autre [clé de script](https://www.codesweetly.com/package-json-file-explained/#scripts)) en tout autre nom que vous préférez.
* Vous pouvez ignorer la surveillance de gros dossiers comme `node_modules` en les ajoutant au champ [watchOptions.ignored](https://webpack.js.org/configuration/watch/#watchoptionsignored) du [fichier de configuration](https://www.codesweetly.com/javascript-module-bundler#what-exactly-is-webpacks-configuration-file) de votre projet.

Maintenant que nous savons comment automatiser l'exécution de Webpack, discutons de la manière de recharger le navigateur automatiquement.

## Comment Recharger le Navigateur Automatiquement

Supposons que vous souhaitiez automatiser le processus de rechargement de votre navigateur. Dans ce cas, vous pouvez utiliser le package [dev server](https://github.com/webpack/webpack-dev-server) de Webpack.

Les étapes suivantes vous montreront comment configurer et utiliser le package.

### Étape 1 : Installer le serveur web de webpack

En utilisant votre terminal, installez le package `webpack-dev-server` comme suit :

```bash
npm install webpack-dev-server --save-dev
```

Ou, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn add webpack-dev-server --dev
```

**Note :** Le package `webpack-dev-server` active le mode de surveillance par défaut. Par conséquent, vous n'avez pas besoin d'activer manuellement un script `watch` chaque fois que vous utilisez le serveur de développement.

En d'autres termes, une fois que vous avez décidé d'utiliser le serveur de développement de Webpack, faites ce qui suit :

1. Utilisez `ctrl + c` sur Windows ou `cmd + c` sur Mac pour arrêter l'exécution de `watch` (si le script est toujours en cours d'exécution).
2. Supprimez la propriété `watch` que vous avez [précédemment ajoutée](#heading-comment-relancer-webpack-automatiquement-1) à votre fichier `package.json`.

### Étape 2 : Spécifier l'emplacement de vos fichiers

Dites au serveur web où il doit obtenir les fichiers que Webpack n'a pas générés en ajoutant une option `devServer` au fichier de configuration que vous avez [créé précédemment](#heading-etape-2-creer-un-fichier-de-configuration) :

```js
// webpack.config.js

const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = { 
  plugins: [new HtmlWebpackPlugin({
    template: "./src/index.html"
  })],
  devServer: {
    static: "./dist"
  }
}

```

L'extrait de configuration ci-dessus indique au serveur de développement de servir les contenus que Webpack n'a pas construits depuis le dossier `dist` du projet.

Notez que le serveur de développement sert les fichiers sur `localhost:8080` par défaut. Cependant, vous pouvez spécifier le port que vous souhaitez utiliser en ajoutant une propriété `port` à l'option `devServer` comme suit :

```js
// webpack.config.js

const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = { 
  plugins: [new HtmlWebpackPlugin({
    template: "./src/index.html"
  })],
  devServer: {
    static: "./dist",
    port: 5001
  }
}

```

**Note :**

* `webpack-dev-server` utilise le répertoire [output.path](https://www.codesweetly.com/javascript-module-bundler#outputpath) pour servir les fichiers bundlés. En d'autres termes, le serveur de développement utilisera `http://[devServer.host]:[devServer.port]/[output.publicPath]/[output.filename]` pour générer l'URL du fichier bundlé.
* Nous discuterons de l'utilisation d'un fichier de configuration [plus tard](#heading-quest-ce-que-le-fichier-de-configuration-de-webpack) dans ce guide.

Voyons maintenant comment exécuter le serveur de développement.

### Étape 3 : Exécuter le serveur de développement

Il existe deux façons d'exécuter le serveur de développement.

* Utiliser NPX sur votre CLI
* Utiliser le champ scripts de `package.json`

Discutons des deux façons ci-dessous.

#### Comment exécuter le serveur de développement de Webpack en utilisant NPX sur votre CLI

En utilisant le terminal, naviguez jusqu'au répertoire racine de votre projet—où se trouve le fichier `webpack.config.js`—puis utilisez NPX pour exécuter le serveur de développement comme ceci :

```bash
npx webpack serve --mode development --open
```

L'extrait ci-dessus utilise NPX pour faire ce qui suit :

1. Exécuter l'étape de construction en exécutant Webpack.
2. Servir le fichier de sortie de l'étape de construction depuis la mémoire, et non depuis votre disque dur.

**Note :**

* Le serveur de développement nécessite un document HTML (généralement un fichier `index.html`) pour servir la sortie de l'étape de construction.
* Le drapeau `--mode development` indique à Webpack d'exécuter l'étape de construction en mode développement.
* Le drapeau `--open` indique au serveur de développement d'ouvrir votre navigateur par défaut.

Gardez à l'esprit que le serveur de développement ne sauvegarde pas le fichier de sortie de l'étape de construction dans l'un de vos répertoires de projet. Au lieu de cela, il fait ce qui suit :

1. Il conserve les fichiers de sortie de l'étape de construction [en mémoire](https://en.wikipedia.org/wiki/In-memory_processing) (la RAM de votre système).
2. Il sert les fichiers de sortie depuis la mémoire, et non depuis le [disque dur](https://www.computerhope.com/jargon/m/memory.htm#storage) de votre système.

L'utilisation de la mémoire de votre système pour construire et servir le fichier de sortie rend le serveur de développement rapide pour servir votre bundle.

Cependant, lorsque votre application est prête pour la production, n'oubliez pas d'exécuter la commande de compilation `npx webpack` pour sauvegarder votre bundle dans le dossier de distribution de votre projet—plutôt qu'en mémoire.

Discutons maintenant de la deuxième façon d'exécuter le serveur de développement.

#### Comment exécuter le serveur de développement de Webpack en utilisant le champ scripts de `package.json`

Une autre façon d'exécuter le serveur de développement est d'ajouter la commande `"webpack serve --mode development --open"` au champ `scripts` de votre `package.json` comme suit :

```json
{
  "name": "your_package",
  "version": "1.0.0",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "webpack serve --mode development --open"
  }
}

```

Ensuite, vous pouvez utiliser `npm run start` sur votre terminal pour exécuter la commande `webpack serve --mode development --open`.

Une fois que vous avez démarré le serveur de développement—via l'option 1 ou 2, votre navigateur par défaut s'ouvrira automatiquement avec la page HTML de votre projet.

Ensuite, chaque fois que vous enregistrerez des modifications dans votre code source, le serveur de développement rechargera automatiquement votre navigateur pour refléter les mises à jour récentes.

**Note :**

* Après avoir exécuté `npm run start`, votre terminal actuellement ouvert continuera à traiter les activités du serveur de développement. Vous ne pourrez donc pas entrer de commande sur ce terminal jusqu'à ce que vous arrêtiez le serveur. Cependant, vous pouvez ouvrir une nouvelle fenêtre de terminal tout en utilisant celle actuelle pour traiter le serveur. En d'autres termes, utilisez un terminal pour exécuter le serveur de développement et un autre pour entrer des commandes.
* Pour arrêter l'exécution du serveur de développement, utilisez `ctrl + c` sur Windows ou `cmd + c` sur Mac.
* Vous pouvez renommer la clé `"start"` (ou toute autre [clé de script](https://www.codesweetly.com/package-json-file-explained/#scripts)) en tout autre nom que vous préférez.
* Consultez la [documentation de Webpack](https://webpack.js.org/configuration/dev-server) pour plus de façons de configurer le serveur de développement.

Rappelez-vous que nous avons utilisé un fichier de configuration dans [l'étape 2](#heading-etape-2-specifier-lemplacement-de-vos-fichiers). Parlons plus de ce que fait le fichier.

## Qu'est-ce que le Fichier de Configuration de Webpack ?

Le **fichier de configuration** de Webpack est un fichier JavaScript qui vous permet de modifier ou d'étendre les paramètres par défaut de Webpack.

Par exemple, le paramètre par défaut de Webpack suppose que le point d'entrée de votre projet est `src/index.js`.

De plus, par défaut, Webpack minimisera, optimisera et sortira le résultat de son étape de construction dans un fichier `dist/main.js`.

Cependant, supposons que vous souhaitiez changer ces paramètres par défaut (ou ajouter plus de configurations). Dans ce cas, vous devrez créer un fichier de configuration—que Webpack utilisera automatiquement.

Les étapes suivantes vous montreront comment créer et utiliser un fichier de configuration Webpack.

**Note :** Vous pouvez sauter les étapes 1 et 2 si votre projet a déjà un fichier de configuration.

### Étape 1 : Aller dans le dossier racine du projet

Naviguez jusqu'au répertoire racine de votre projet comme suit :

```bash
cd path/to/project/root-directory
```

### Étape 2 : Créer le fichier de configuration de votre projet

Créez un fichier de configuration dans le dossier racine de votre projet comme suit :

```bash
touch webpack.config.js
```

### Étape 3 : Spécifier vos configurations

Ouvrez le fichier `webpack.config.js` de votre projet et spécifiez les [options de configuration](https://webpack.js.org/configuration/#options) que vous souhaitez changer (ou ajouter).

**Voici un exemple :**

```js
// webpack.config.js

const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = { 
  plugins: [new HtmlWebpackPlugin()] 
};

```

Voici ce que nous avons fait dans le fichier de configuration ci-dessus :

1. Nous avons initialisé la variable `HtmlWebpackPlugin` avec le package `"html-webpack-plugin"`.
2. Nous avons exporté un objet contenant la configuration `plugins` que nous voulons que Webpack utilise.

Ainsi, chaque fois que vous exécutez l'étape de construction, Webpack utilisera automatiquement les paramètres que vous avez spécifiés dans le fichier de configuration—plutôt que ses paramètres par défaut.

Exécutons maintenant l'étape de construction.

### Étape 4 : Exécuter le bundler de modules

En utilisant votre terminal, créez votre bundle en exécutant Webpack comme suit :

```bash
npx webpack --config webpack.config.js
```

Le code `--config webpack.config.js` utilisé dans l'extrait ci-dessus est facultatif. Nous l'avons utilisé ci-dessus pour illustrer qu'il est possible de passer une configuration de [n'importe quel nom](https://webpack.js.org/configuration/#use-a-different-configuration-file)—ce dont vous pourriez avoir besoin pour des configurations complexes qui nécessitent une division en plusieurs fichiers.

Cependant, Webpack utilisera le fichier `webpack.config.js` par défaut s'il est présent dans le répertoire racine de votre projet.

Gardez à l'esprit que [plugins](https://webpack.js.org/concepts/plugins/) n'est qu'une des nombreuses options que vous pouvez utiliser dans un fichier de configuration.

Discutons d'autres options de configuration que les développeurs utilisent.

## Options de Configuration Courantes de Webpack

Voici les options de configuration populaires que vous pouvez utiliser pour modifier (ou étendre) les paramètres par défaut de Webpack.

### entry

Le champ `entry` spécifie le ou les fichiers que vous souhaitez que Webpack utilise pour commencer le processus de bundling de l'application.

**Voici un exemple :**

```js
// webpack.config.js

module.exports = {
  entry: "./src/index.js",
};

```

L'extrait ci-dessus indique à Webpack de commencer son processus de bundling à partir de `"./src/index.js"`.

Supposons que vous avez utilisé un tableau (ou un objet) comme valeur du champ `entry`. Dans ce cas, Webpack traitera tous les éléments du tableau (ou de l'objet) comme les points d'entrée de l'application.

**Voici un exemple :**

```js
// webpack.config.js

module.exports = {
  entry: [
    "./src/index.js",
    "./src/index-two.js",
    "./src/index-three.js"
  ]
}

```

Le code ci-dessus indique à Webpack de commencer son processus de bundling à partir des trois fichiers spécifiés dans le tableau `entry` (c'est-à-dire `"./src/index.js"`, `"./src/index-two.js"`, et `"./src/index-three.js"`).

**Voici un autre exemple :**

```js
// webpack.config.js

module.exports = {
  entry: {
    index: "./src/index.js",
    indexTwo: "./src/index-two.js",
    indexThree: "./src/index-three.js"
  }
}

```

Le code ci-dessus indique à Webpack de commencer son processus de bundling à partir des trois fichiers spécifiés dans l'objet `entry` (c'est-à-dire `"./src/index.js"`, `"./src/index-two.js"`, et `"./src/index-three.js"`).

**Note :**

* Si la valeur de `entry` est une chaîne ou un tableau, Webpack créera un chunk (bundle)—qu'il nommera `main` par défaut.
* Si la valeur de `entry` est un objet, Webpack créera un ou plusieurs chunks. Le nombre spécifique de chunks créés dépendra du nombre total de propriétés de l'objet.
* Supposons que la valeur de `entry` est un objet. Dans ce cas, Webpack utilisera chaque clé pour nommer chaque chunk. Par exemple, dans `entry: { home: './home-module.js' }`, Webpack créera un chunk (bundle) nommé `home`.

### context

Le champ `context` pointe Webpack vers le répertoire contenant vos fichiers d'entrée.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "index.js",
  context: path.resolve(__dirname, "src")
}

```

L'extrait ci-dessus indique à Webpack de localiser le fichier d'entrée `index.js` dans le répertoire `src` du projet.

### output

Le champ `output` spécifie comment et où Webpack doit sortir les bundles et les actifs qu'il a traités.

Les trois options couramment utilisées avec le champ `output` sont `path`, `filename`, et `clean`.

#### output.path

L'option `output.path` spécifie le répertoire de sortie où vous souhaitez que Webpack place le fichier bundlé.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist")
  }
}

```

L'extrait ci-dessus a utilisé l'option `output.path` pour indiquer à Webpack d'utiliser le dossier `"./dist"` du projet comme répertoire de sortie.

#### output.filename

L'option `output.filename` spécifie comment Webpack doit nommer chaque bundle qu'il crée.

Supposons que vous créez un seul bundle via un seul point d'entrée. Dans ce cas, vous pouvez spécifier un nom statique comme nom de fichier du bundle.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "codesweetly.js",
    path: path.resolve(__dirname, "dist")
  }
}

```

L'option `output.filename` indique à Webpack d'utiliser `"codesweetly.js"` comme nom de fichier du bundle créé après le traitement de `"./src/index.js"`.

Supposons que vous souhaitiez créer plusieurs bundles via deux points d'entrée ou plus, la division de code, ou divers plugins. Dans ce cas, il est préférable de générer dynamiquement le nom de fichier de chaque bundle via l'une des techniques de substitution de Webpack.

**Note :** Les substitutions—dans Webpack—faisant référence à l'utilisation de chaînes entre crochets pour créer des [modèles](https://webpack.js.org/configuration/output/#template-strings) pour les noms de fichiers.

Discutons maintenant des trois techniques de substitution couramment utilisées.

##### Technique de substitutions 1 : Nom d'entrée

La technique de nommage **"nom d'entrée"** fait en sorte que Webpack crée le nom de chaque bundle en [concaténant](https://www.codesweetly.com/web-tech-glossary#concatenation) le nom du point d'entrée d'un bundle avec une chaîne donnée.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: {
    home: "./src/home-module.js",
    promo: "./src/promo-module.js",
    music: "./src/music-module.js"
  },
  output: {
    filename: "[name].bundle.js",
    path: path.resolve(__dirname, "dist")
  }
}

```

L'option `output.filename` indique à Webpack de créer le nom de fichier de chaque bundle en concaténant le nom de chaque point d'entrée avec la valeur de chaîne `".bundle.js"`.

Ainsi, par exemple, supposons que Webpack a terminé le traitement du point d'entrée `promo` (c'est-à-dire `"./src/promo-module.js"`). Dans ce cas, le nom final du bundle sera `"promo.bundle.js"`.

Discutons maintenant de la deuxième technique de substitutions.

##### Technique de substitutions 2 : ID de chunk interne

La technique de nommage **"ID de chunk interne"** fait en sorte que Webpack crée le nom de chaque bundle en concaténant l'ID du point d'entrée d'un bundle avec une chaîne donnée.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: {
    home: "./src/home-module.js",
    promo: "./src/promo-module.js",
    music: "./src/music-module.js"
  },
  output: {
    filename: "[id].bundle.js",
    path: path.resolve(__dirname, "dist")
  }
}

```

L'option `output.filename` indique à Webpack de créer le nom de fichier de chaque bundle en concaténant l'ID de chunk interne de chaque point d'entrée avec la valeur de chaîne `".bundle.js"`.

Discutons maintenant de la troisième technique de substitutions.

##### Technique de substitutions 3 : Hachage de contenu

La technique de nommage **"hachage de contenu"** fait en sorte que Webpack crée le nom de chaque bundle en concaténant les hachages du contenu généré avec une chaîne donnée.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: {
    home: "./src/home-module.js",
    promo: "./src/promo-module.js",
    music: "./src/music-module.js"
  },
  output: {
    filename: "[contenthash].bundle.js",
    path: path.resolve(__dirname, "dist")
  }
}

```

L'option `output.filename` indique à Webpack de créer le nom de fichier de chaque bundle en concaténant le hachage de contenu de chaque chunk avec la valeur de chaîne `".bundle.js"`.

Gardez à l'esprit que Webpack vous permet de combiner différentes substitutions—par exemple, `filename: "[name].[contenthash].bundle.js"`.

Vous pouvez également utiliser une fonction pour retourner un nom de fichier comme suit :

```js
filename: (pathData) => {
  return pathData.chunk.name === "main" ? "[name].js" : "[name].bundle.js";
}

```

Webpack vous permet également d'initialiser la propriété filename avec une structure de dossier comme suit :

```js
filename: "codesweetly/[name]/bundle.js"
```

Discutons maintenant de la troisième propriété couramment utilisée dans le champ `output`.

#### output.clean

À mesure que Webpack génère et sauvegarde de plus en plus de fichiers dans votre répertoire de sortie, il est courant d'encombrer le dossier `/dist` d'un projet avec des fichiers inutilisés.

Ainsi, une bonne pratique consiste à nettoyer votre répertoire de sortie avant chaque étape de construction. En faisant cela, votre dossier `/dist` ne contiendra que les fichiers utilisés.

Voyons comment effectuer le nettoyage ci-dessous :

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "codesweetly.js",
    path: path.resolve(__dirname, "dist"),
    clean: true
  }
}

```

L'option `clean` dans l'extrait ci-dessus indique à Webpack de nettoyer le répertoire de sortie du projet avant chaque étape de construction.

En d'autres termes, Webpack videra le répertoire de sortie avant de commencer chaque étape de construction.

Par conséquent, le répertoire de sortie ne contiendra que les fichiers générés à partir du processus de compilation—aucun des anciens fichiers que Webpack y avait précédemment sauvegardés.

Discutons maintenant d'une autre option de configuration populaire que vous pouvez utiliser pour modifier (ou étendre) les paramètres par défaut de Webpack.

### module

Le champ `module` permet à Webpack de traiter les actifs—comme les fichiers CSS et les polices—en tant que [modules](#heading-quest-ce-quun-module-javascript) dans le graphe de dépendances.

Ainsi, supposons que vous souhaitez que Webpack regrouper des actifs non-JavaScript tels que des images, des fichiers CSS, des polices, etc. Dans ce cas, vous pouvez utiliser l'option `module` pour spécifier comment Webpack doit gérer ces actifs avant de les ajouter au graphe de dépendances.

Voici quelques façons courantes d'utiliser l'option `module`.

#### Comment utiliser l'option `module` de Webpack pour charger des feuilles de style CSS

Voici comment vous pouvez utiliser l'option module de Webpack pour charger des feuilles de style CSS :

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  module: {
    rule: [
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"]
      }
    ]
  }
}

```

L'extrait de configuration ci-dessus a utilisé la propriété `module` pour indiquer à Webpack d'utiliser `"style-loader"` et `"css-loader"` pour charger les fichiers CSS.

Gardez à l'esprit que l'ordre des chargeurs est important.

En d'autres termes, Webpack lit les chargeurs de droite à gauche. Par conséquent, il exécutera d'abord le `"css-loader"` avant le `"style-loader"`.

Ainsi, ["css-loader"](https://github.com/webpack-contrib/css-loader) transmettra son résultat (c'est-à-dire la ressource traitée) au `"style-loader"`. Ensuite, ["style-loader"](https://github.com/webpack-contrib/style-loader) insérera la ressource CSS finale dans l'élément `<head>` de votre page HTML.

Il est nécessaire d'installer les chargeurs que vous souhaitez que Webpack utilise pour charger vos actifs CSS.

Ainsi, par exemple, avant que Webpack puisse utiliser le fichier de configuration précédent pour charger les actifs ".css", vous devez installer `"style-loader"` et `"css-loader"`.

Voici comment installer les deux chargeurs :

```bash
npm install style-loader css-loader --save-dev
```

Alternativement, si votre gestionnaire de paquets est Yarn, exécutez :

```bash
yarn add style-loader css-loader --dev
```

**Note :**

* `"css-loader"` aide à interpréter et à résoudre les éléments `@import` et `url()` tels que `import`, `require()`, et `url('./my-image.png')`.
* `"style-loader"` aide à injecter une balise `<style>` et les styles dérivés de `"css-loader"` dans le fichier HTML de votre projet.

Voyons maintenant comment utiliser l'option `module` pour charger des images.

#### Comment utiliser l'option `module` de Webpack pour charger des images

Voici comment vous pouvez utiliser l'option `module` de Webpack pour charger des images :

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  module: {
    rule: [
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: "asset/resource"
      }
    ]
  }
}

```

L'extrait de configuration ci-dessus a utilisé la propriété module pour indiquer à webpack de charger les fichiers `".png"`, `".svg"`, `".jpg"`, `".jpeg"`, et `".gif"` en tant que [modules d'actifs de ressource](https://webpack.js.org/guides/asset-modules/#resource-assets).

Ainsi, supposons que l'instruction `import` suivante se trouve dans votre fichier de script :

```js
import anyImage from "./your-image.png";
```

Dans ce cas, voici comment Webpack chargera l'image :

1. Webpack traitera `your-image.png`.
2. Il ajoutera l'image traitée à votre répertoire _output_.
3. Webpack initialisera la variable `anyImage` avec l'URL de l'image traitée.

**Note :** Lors du traitement et de l'ajout de `your-image.png` au dossier de sortie, Webpack changera le nom de fichier de l'image en quelque chose comme `150b55a1bf7461efb720.png`.

Voyons maintenant comment utiliser l'option `module` pour charger des polices.

#### Comment utiliser l'option `module` de Webpack pour charger des polices

Voici comment vous pouvez utiliser l'option `module` de Webpack pour charger des polices :

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  module: {
    rule: [
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: "asset/resource"
      }
    ]
  }
}

```

L'extrait de configuration ci-dessus a utilisé la propriété `module` pour indiquer à Webpack de charger les fichiers `".woff"`, `".woff2"`, `".eot"`, `".ttf"`, et `".otf"` en tant que [modules d'actifs de ressource](https://webpack.js.org/guides/asset-modules/#resource-assets).

Une fois que vous avez configuré le chargeur, vous pouvez incorporer vos polices via la déclaration CSS [@font-face](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face).

**Voici un exemple :**

```css
/* styles.css */

@font-face {
  font-family: "Digital7";
  src: url("./digital-7.regular.woff") format("woff"),
       url("./digital-7.regular.ttf") format("truetype");
  font-weight: 600;
  font-style: italic;
}

div {
  color: red;
  font-family: "Digital7";
}

```

Chaque fois que `css-loader` charge la feuille de style ci-dessus, il traitera les polices spécifiées et ajoutera les copies traitées au répertoire de sortie de votre projet.

**Note :**

* Webpack changera le nom de fichier des polices traitées en quelque chose de similaire à `93911ab167c943140756.ttf`.
* Consultez la [documentation de Webpack](https://webpack.js.org/guides/asset-management/#loading-data) pour apprendre à charger les fichiers JSON, CSV, TSV et XML.

Discutons maintenant d'une autre option de configuration populaire que vous pouvez utiliser pour modifier (ou étendre) les paramètres par défaut de Webpack.

### devtool

Le champ `devtool` indique à Webpack de convertir un fichier compilé au format de code source. Ainsi, facilitant le débogage du fichier exact (et de la ligne) où une erreur s'est produite dans votre code source.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  devtool: "source-map"
}

```

Au moment de la compilation, si Webpack voit une propriété `devtool` dans votre script de configuration, il générera un fichier `.js.map` que le navigateur utilisera au lieu du fichier `.js`.

**Note :** Il existe différentes [options devtool](https://webpack.js.org/configuration/devtool/) pour spécifier si et comment Webpack doit générer les source maps.

Discutons maintenant d'une autre option de configuration populaire que vous pouvez utiliser pour modifier (ou étendre) les paramètres par défaut de Webpack.

### mode

Le champ `mode` indique à Webpack la configuration d'optimisation intégrée spécifique que vous souhaitez qu'il utilise pour construire votre fichier de sortie.

Vous pouvez spécifier si Webpack doit utiliser la configuration `production`, `development`, ou aucune (`none`) pour optimiser votre bundle. Discutons de chacun des trois paramètres d'optimisation ci-dessous.

#### Mode Développement

Un paramètre `mode: "development"` indique à Webpack de construire un fichier de sortie pour une utilisation dans l'environnement de développement.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  devtool: "source-map",
  mode: "development"
}

```

La configuration d'un `mode: "development"` fera en sorte que Webpack crée un bundle qui :

* est rapide à construire
* est moins optimisé
* inclut des commentaires
* n'est pas minifié
* produit des messages d'erreur utiles
* est facile à déboguer

Voici un exemple d'un bundle `mode: "development"` :

![Un bundle en mode développement](https://www.freecodecamp.org/news/content/images/2022/05/bundle-development-mode-webpack-codesweetly.png)
_Image d'un bundle en mode développement compilé avec webpack_

Pour rendre un fichier de sortie non minifié lisible, assurez-vous que le champ [devtool](#heading-devtool) de Webpack n'est pas `eval`.

Chaque fois que vous définissez le `mode` sur `development`, Webpack peut définir par défaut la valeur de `devtool` sur `eval`. Assurez-vous donc de sélectionner un `devtool` différent—comme [source-map](https://webpack.js.org/configuration/devtool/#devtool) ou de le désactiver en définissant sa valeur sur `"false"`—chaque fois que vous souhaitez rendre votre fichier de sortie lisible.

Supposons que vous choisissez d'exécuter Webpack en mode développement. Dans ce cas, n'oubliez pas de changer votre configuration en mode production lorsque vous êtes prêt à déployer votre application.

Discutons maintenant de la configuration de Webpack pour construire votre fichier de sortie en mode production.

#### Mode Production

Un paramètre `mode: "production"` indique à Webpack de construire un fichier de sortie pour une utilisation dans l'environnement de production.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  devtool: "source-map",
  mode: "production"
}

```

La configuration d'un `mode: "production"` fera en sorte que Webpack crée un bundle qui :

* est lent à construire
* est plus optimisé
* exclut les commentaires
* est minifié
* ne produit pas de messages d'erreur détaillés
* est difficile à déboguer

Voici un exemple d'un bundle `mode: "production"` :

![Un bundle en mode production](https://www.freecodecamp.org/news/content/images/2022/05/bundle-production-mode-webpack-codesweetly.png)
_Image d'un bundle en mode production compilé avec webpack_

**Note :** Webpack [recommande](https://webpack.js.org/guides/production/#source-mapping) d'avoir des source maps—comme `source-map`—activées en production.

Discutons maintenant de la configuration de Webpack pour construire votre fichier de sortie sans aucun paramètre d'optimisation.

#### Mode Aucun

Un paramètre `mode: "none"` indique à Webpack de construire un fichier de sortie sans l'optimiser pour le développement ou la production.

**Voici un exemple :**

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  mode: "none"
}

```

Voici un exemple d'un bundle `mode: "none"` :

![Un bundle en mode aucun](https://www.freecodecamp.org/news/content/images/2022/05/bundle-none-mode-webpack-codesweetly.png)
_Image d'un bundle en mode aucun compilé avec webpack_

#### Choses importantes à savoir sur l'option `mode`

Pour faciliter le passage entre le mode développement et le mode production, vous pouvez stocker les configurations `mode` dans le champ `"scripts"` de votre fichier `package.json`.

**Voici un exemple :**

```json
{
  "name": "your-app-name",
  "version": "1.0.0",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "webpack --mode development",
    "build": "webpack --mode production"
  }
}

```

L'extrait ci-dessus a initialisé la propriété `"dev"` des scripts avec la commande de mode `development` de Webpack.

De même, nous avons initialisé la propriété `"build"` des scripts avec la commande de mode `production` de Webpack.

Par conséquent, supposons que vous exécutez `npm run dev` sur votre terminal. Dans ce cas, Webpack exécutera l'étape de construction en mode développement.

## Aperçu

Cet article a discuté de ce qu'est un module JavaScript et de son fonctionnement. Nous avons également discuté de l'utilisation d'un bundler de modules populaire (Webpack) pour regrouper le fichier JavaScript d'un projet et ses dépendances en un seul fichier de sortie.

Et voilà. J'espère que vous avez trouvé cet article utile.

Merci d'avoir lu !

### **Et voici une ressource utile sur ReactJS :**

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✔
* Il contient des extraits de code en direct ✔
* Il contient des projets évolutifs ✔
* Il contient de nombreux exemples faciles à comprendre ✔

Le livre [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![Livre React Explained Clearly Maintenant Disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)