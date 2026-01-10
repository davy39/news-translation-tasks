---
title: Qu'est-ce que PostCSS ? Comment utiliser les plugins pour automatiser les tâches
  CSS
subtitle: ''
author: Yasir Tobbileh
co_authors: []
series: null
date: '2022-01-31T17:29:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-postcss
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/postcss-1.PNG
tags:
- name: automation
  slug: automation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: PostCSS
  slug: postcss
seo_title: Qu'est-ce que PostCSS ? Comment utiliser les plugins pour automatiser les
  tâches CSS
seo_desc: "PostCSS is a Node.js tool that transforms your styles using JavaScript\
  \ plugins.  \nIt generates more downloads per week on NPM than other CSS preprocessors\
  \ like Sass, Less, and Stylus combined.\n\nPostCSS download trends comparing to\
  \ other CSS preproces..."
---

PostCSS est un outil Node.js qui transforme vos styles à l'aide de plugins JavaScript.  
  
Il génère plus de téléchargements par semaine sur [NPM](https://www.npmtrends.com/less-vs-postcss-vs-sass-vs-stylus) que d'autres préprocesseurs CSS comme Sass, Less et Stylus combinés.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/trend.PNG)
_Tendances de téléchargement de PostCSS comparées à d'autres préprocesseurs CSS_

## Dans cet article, nous allons discuter :

* Qu'est-ce que PostCSS ?
* Fonctionnalités et avantages de PostCSS
* Quelques plugins PostCSS populaires
* Comment configurer les configurations PostCSS

# Qu'est-ce que PostCSS ?

PostCSS est un outil JavaScript qui transforme votre code CSS en un arbre syntaxique abstrait (AST) puis fournit une API (interface de programmation d'applications) pour l'analyser et le modifier à l'aide de plugins JavaScript.

PostCSS offre un large écosystème de plugins pour effectuer différentes fonctionnalités comme le linting, la minification, l'insertion de préfixes vendeurs, et bien d'autres choses.

Malgré son nom, ce n'est ni un post-processeur ni un pré-processeur, c'est simplement un **transpileur** qui transforme une syntaxe spéciale de plugin PostCSS en CSS Vanilla. Vous pouvez le considérer comme l'outil [**Babel**](https://babeljs.io/docs/en/) pour CSS.

Vous pouvez utiliser PostCSS en conjonction avec des préprocesseurs existants comme Sass, Less et Stylus. Ou vous pouvez l'utiliser comme une alternative à tous ceux-ci puisqu'il possède toutes les fonctionnalités requises pour être utilisé seul.

Vous avez peut-être déjà utilisé PostCSS sans le savoir. Il est utilisé dans le plugin populaire Autoprefixer qui est utilisé pour ajouter automatiquement des préfixes vendeurs aux propriétés CSS qui les nécessitent.

PostCSS est également utilisé par d'autres technologies comme Vite et Next.js, ainsi que par le framework CSS [TailwindCSS](https://tailwindcss.com/docs/using-with-preprocessors#using-post-css-as-your-preprocessor) qui est un plugin PostCSS.

# Fonctionnalités et avantages de PostCSS

* PostCSS est entièrement personnalisable, vous pouvez donc utiliser uniquement les plugins et fonctionnalités dont vous avez besoin pour votre application.
* Il offre également des temps de construction rapides par rapport à d'autres préprocesseurs.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_WVCihSMXXK0xkCw2a3g8iQ.png)
_Différents temps de construction pour différents préprocesseurs CSS comparés à PostCSS_

* Si vous le souhaitez, vous pouvez écrire vos propres plugins personnalisés. Et vous pouvez l'utiliser avec du CSS régulier ainsi qu'avec d'autres préprocesseurs comme Sass.

PostCSS est tout au sujet des plugins (par lui-même, il est simplement une API). Il dispose d'un écosystème de 356 plugins (au moment de la rédaction de cet article). Chaque plugin a été créé pour une tâche spécifique.

Vous pouvez naviguer à travers les plugins en utilisant le [répertoire des plugins](https://github.com/postcss/postcss/blob/main/docs/plugins.md) sur la page GitHub officielle de PostCSS, ou en utilisant ce [catalogue recherchable de plugins PostCSS](https://www.postcss.parts/).

Avant de commencer avec le code, je vous recommande fortement de suivre ces étapes :

1. Téléchargez ou forkez le dépôt [**postcss-tutorial**](https://github.com/adamA113/postcss-tutorial) sur votre machine et essayez de suivre. (Assurez-vous de lire le fichier README.md.)
2. Installez le **plugin** [**PostCSS Language Support**](https://marketplace.visualstudio.com/items?itemName=csstools.postcss) si vous utilisez l'éditeur Visual Studio Code, afin que votre éditeur puisse reconnaître toute nouvelle syntaxe et arrêter de vous donner des erreurs (ignorez cette étape si vous utilisez d'autres éditeurs de code).

# Plugins PostCSS populaires

### PostCSS Import

L'un des plugins les plus basiques et importants à utiliser est [postcss-import](https://github.com/postcss/postcss-import). Il nous permet d'importer des fichiers CSS dans d'autres fichiers.

Pour voir comment utiliser ce plugin, allez dans `src/style.css` dans le dépôt postcss-tutorial.

```css
@import './components/comp1.css';
@import './components/comp2.css';
```

Vous pouvez voir que c'est très similaire à la façon dont nous utilisons la méthode @import dans Sass. 

**Note :** `postcss-import` est différent de la [règle import](https://developer.mozilla.org/en-US/docs/Web/CSS/@import) en CSS natif. Vous devriez éviter la règle import en CSS natif, car elle peut empêcher les feuilles de style d'être téléchargées simultanément, ce qui affecte la vitesse de chargement et les performances.

Le navigateur doit attendre que chaque fichier importé soit chargé au lieu de pouvoir charger tous les fichiers CSS à la fois.

## [Autoprefixer](https://github.com/postcss/autoprefixer)

C'est l'un des plugins PostCSS les plus populaires. Vous l'utilisez pour analyser et ajouter des préfixes vendeurs comme `-webkit`, `-moz` et `-ms` aux règles CSS en utilisant les valeurs du site [Can I Use](https://caniuse.com/).

Nous utilisons le site Can I Use pour voir quels navigateurs supportent une fonctionnalité CSS avec leurs versions. Cela nous aide à déterminer si nous devons ajouter un préfixe ou non.

Autoprefixer utilise [Browserslist](https://github.com/browserslist/browserslist), vous pouvez donc spécifier les navigateurs que vous souhaitez cibler dans votre projet avec des requêtes.

Nous pouvons configurer notre Browserslist dans le fichier package.json en utilisant une clé "browserslist" :

```json
 "browserslist": [ 
     "defaults"  
 ]
```

La requête `defaults` ci-dessus est une version courte de :

* `> 0.5%` navigateurs qui ont au moins 0,5 % d'utilisation mondiale.
* `last 2 versions` les deux dernières versions pour _chaque_ navigateur,
* `Firefox ESR` la dernière [version étendue de support de Firefox](https://support.mozilla.org/en-US/kb/choosing-firefox-update-channel)., 
* `not dead` navigateurs qui ont reçu un support officiel ou des mises à jour au cours des 24 derniers mois.

Ou nous pouvons utiliser un fichier `.browserslistrc` dans le répertoire racine, et y insérer nos configurations.

```
defaults
```

Pour tester ce plugin, nous avons ajouté quelques règles CSS qui nécessitent des préfixes dans le fichier `src/components/comp2.css` :

```css
label {
  user-select: none;
}

::selection {
  color: white;
  background: blue;
}

::placeholder {
  color: gray;
}
```

Sur la base de nos paramètres "browserslist" précédents, le résultat final sera :

```css
label {
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

::-moz-selection {
  color: white;
  background: blue;
}

::selection {
  color: white;
  background: blue;
}

::-moz-placeholder {
  color: gray;
}

:-ms-input-placeholder {
  color: gray;
}

::placeholder {
  color: gray;
}
```

## [PostCSS Preset Env](https://github.com/csstools/postcss-plugins/tree/main/plugin-packs/postcss-preset-env)

Ce plugin nous permet d'utiliser du CSS moderne (comme le nesting et les requêtes média personnalisées) dans notre code, en le convertissant en CSS Vanilla qui peut être compris par les navigateurs.

Il dispose d'une option `stage` qui détermine quelles fonctionnalités CSS doivent être polyfillées en fonction de leur stabilité dans le processus de mise en œuvre en tant que standard web.

Le `stage` peut être de 0 (expérimental) à 4 (stable), ou false. Le stage 2 est celui par défaut.

Pour le nesting, nous devons utiliser le stage 1.

```javascript
module.exports = {
    plugins: [
        require('postcss-preset-env')({ stage: 1 })
    ],
}
```

De plus, le plugin preset-env inclut par défaut le plugin [Autoprefixer](https://github.com/postcss/autoprefixer) et l'option `[browsers](https://github.com/csstools/postcss-preset-env#browsers)` lui sera transmise automatiquement.

Dans le fichier `src/components/comp1.css`, nous avons utilisé la fonctionnalité de nesting de manière très similaire à ce que nous avons dans le préprocesseur Sass :

```css
article {
    background: purple;

    & .title {
        font-size: 6rem;
    }

    & li {
        list-style-type: none;
    }
}
```

Puisque le nesting n'est pas supporté dans le CSS actuel, nous devons convertir le code ci-dessus pour que les navigateurs web puissent le comprendre.

Le code suivant est le résultat final :

```css
article {
    background: purple
}

article .title {
        font-size: 6rem;
    }

article li {
        list-style-type: none;
    }
```

## [PostCSS Nested](https://github.com/postcss/postcss-nested)

Si nous voulons **uniquement** utiliser la fonctionnalité de nesting, alors ce plugin est le choix parfait car il produit le même résultat que le plugin précédent.

## [PostCSS Mixins](https://github.com/postcss/postcss-mixins)

Les mixins vous permettent de définir des styles qui peuvent être réutilisés dans tout votre code.

Dans notre code, nous avons utilisé quelques mixins dans le fichier `src/components/comp1.css`.

Nous définissons d'abord le mixin en utilisant le mot-clé `@defin-mixin` suivi du nom du mixin. Ensuite, nous l'utilisons en écrivant le nom après le mot-clé `@mixin`. 

```css
@define-mixin reset-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

nav ul {
  @mixin reset-list;
}
```

Les mixins ne sont pas supportés dans le CSS actuel, ils doivent donc être compilés en CSS Vanilla.

Le code final sera :

```css
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
```

## [Stylelint](https://stylelint.io/)

C'est un linter CSS qui nous aide à éviter les erreurs dans notre code avant qu'elles ne cassent notre interface utilisateur (UI).

Il peut être configuré de [plusieurs manières](https://stylelint.io/user-guide/configure). L'une d'entre elles consiste à utiliser une propriété `stylelint` dans `package.json` comme suit :

```json
"stylelint": {
    "rules": {
      "color-no-invalid-hex": true
    }
  }
```

À l'intérieur de `stylelint`, nous avons plusieurs options à configurer. Ici, nous ne couvrirons que l'option "rules" qui vous permet de définir les règles que le linter doit rechercher et donne des erreurs lorsqu'elles ne sont pas suivies.

La règle `"color-no-invalid-hex": true` donne une erreur dans le terminal si une valeur hexadécimale invalide est fournie comme couleur pour une propriété CSS donnée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/invalid-1.PNG)
_Le linter Styleint donne une erreur car une valeur hexadécimale invalide est fournie comme couleur à la ligne 11._

**Note :** Aucune règle n'est activée par défaut et il n'y a pas de valeurs par défaut. Vous devez configurer explicitement chaque règle pour l'activer.

## [Cssnano](https://cssnano.co/docs/Introduction/)

C'est un minificateur utilisé pour réduire autant que possible la taille du fichier CSS final afin que votre code soit prêt pour un environnement de production.

Certaines parties seront modifiées pour réduire autant que possible la taille, comme la suppression des espaces inutiles, des nouvelles lignes, le renommage des valeurs et des variables, les sélecteurs fusionnés ensemble, et ainsi de suite.

Voici donc notre code CSS final avant le processus de minification :

```css
* {
  padding: 0;
  margin: 0;
}

article {
    background: purple
}

article .title {
        font-size: 6rem;
    }

article li {
        list-style-type: none;
    }

nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

body {
  font-family: sans-serif, Calibri;
  font-size: 16px;
}

label {
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

::-moz-selection {
  color: white;
  background: blue;
}

::selection {
  color: white;
  background: blue;
}

::-moz-placeholder {
  color: gray;
}

:-ms-input-placeholder {
  color: gray;
}

::placeholder {
  color: gray;
}
```

Après le processus de minification, notre code CSS final prêt pour l'environnement de production sera comme ceci :

```css
*{margin:0;padding:0}article{background:purple}article .title{font-size:6rem}article li{list-style-type:none}nav ul{list-style:none;margin:0;padding:0}body{font-family:sans-serif,Calibri;font-size:16px}label{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}::-moz-selection{background:blue;color:#fff}::selection{background:blue;color:#fff}::-moz-placeholder{color:gray}:-ms-input-placeholder{color:gray}::placeholder{color:gray}
```

## [PostCSS Normalize](https://github.com/csstools/postcss-normalize)

Ce plugin vous permet d'utiliser certaines parties de la bibliothèque populaire [normalize.css](https://github.com/csstools/normalize.css) ou [sanitize.css](https://github.com/csstools/sanitize.css).

Ces bibliothèques CSS fournissent un style par défaut cohérent et multi-navigateurs des éléments HTML, elles corrigent également les bugs et les incohérences courantes des navigateurs.

Ce plugin dépend des valeurs que vous fournissez pour `"**browserslist"**` pour afficher les styles corrects pour les éléments HTML. Voici un [exemple](https://github.com/csstools/postcss-normalize#examples) de cela.

# Comment configurer PostCSS

Pour commencer à utiliser PostCSS, nous devons d'abord l'installer ainsi que son [interface en ligne de commande](https://github.com/postcss/postcss-cli) (CLI) globalement en utilisant cette commande :

```bash
npm i -g postcss-cli
```

* `-g` pour le télécharger globalement.

Ensuite, installez PostCSS localement en utilisant la commande suivante :

```bash
npm i -D postcss
```

* `-D` est l'abréviation de `--save-dev` pour enregistrer les packages installés en tant que dépendances de développement.

Pour commencer à utiliser PostCSS, nous devons avoir au moins un plugin téléchargé.

Si vous suivez avec le dépôt [postcss-tutorial](https://github.com/adamA113/postcss-tutorial), vous pouvez simplement exécuter `npm install` pour télécharger tous les packages et dépendances.

## **Configurer PostCSS en utilisant l'interface de ligne de commande PostCSS**

La syntaxe générale pour la commande à exécuter dans le terminal est :

```
 postcss [input.css] [OPTIONS] [-o|--output output.css] [--watch|-w]
 postcss <input.css> [OPTIONS] --dir <output-directory> [--watch|-w]
```

Nous pouvons exécuter la commande suivante directement dans le terminal :

```bash
postcss src/style.css --use postcss-import --dir public --watch
```

L'option `--use` liste les plugins que nous utilisons.

L'option `--watch` surveille les fichiers pour tout changement et les recompile.

## **Configurer PostCSS via les scripts NPM dans le fichier package.json**

À l'intérieur du fichier package.json dans les "scripts", nous devons taper ce qui suit :

```json
"postcss:watch": "postcss src/style.css --use postcss-import 
--dir public --watch"
```

La commande ci-dessus créera un nouveau répertoire appelé 'public' qui contient notre fichier CSS Vanilla final, qui porte le même nom que le fichier source (style.css).

Si nous voulons que le fichier de sortie ait un nom différent de celui du fichier source, nous devons remplacer `--dir public` par `-o public/<file-name>`.

Par exemple : `-o public/main.css`.

Nous pouvons configurer notre commande pour qu'elle s'exécute dans l'interface de ligne de commande PostCSS avec différentes [options](https://github.com/postcss/postcss-cli) pour obtenir le résultat souhaité.

Maintenant, pour exécuter la commande ci-dessus, nous tapons `npm run <command name>` dans notre terminal. (notre `<command name>` est **postcss:watch**, vous pouvez choisir n'importe quel nom que vous voulez).

À mesure que notre projet grandit, il est plus probable que nous ajoutions plus de plugins. Pour chaque plugin utilisé, nous devons écrire son nom après le mot-clé `--use` dans la commande ci-dessus, ce qui la rend incroyablement longue et ce n'est pas une bonne pratique.

La solution alternative est de créer un fichier postcss.config.js.

## Configurer PostCSS en créant un fichier de configuration PostCSS

Dans le répertoire racine de votre projet, créez un fichier et nommez-le **postcss.config.js**.

Le code à l'intérieur ressemblera à ceci :

```javascript
module.exports = {
    plugins: [
     	require('postcss-import'),
        require('postcss-mixins'),
        require("stylelint"),
        require('postcss-preset-env')({ stage: 1 }),
        require('cssnano'),
    ],
}
```

À l'intérieur du tableau des plugins, nous ajoutons nos plugins.

**Note :** Il est très important d'ajouter le plugin postcss-import en haut de notre liste car il est requis par la documentation.

La commande qui exécute PostCSS dans notre fichier package.json doit être modifiée en :

```json
"postcss:watch": "postcss src/style.css --dir public --watch"
```

Comme vous pouvez le voir, le seul changement requis est de supprimer l'option `--use` puisque la liste de nos plugins est mentionnée dans un fichier séparé maintenant.

## **Configurer PostCSS en utilisant des exécuteurs de tâches (ou des bundlers de modules)**

PostCSS peut être configuré pour fonctionner avec divers exécuteurs de tâches comme [Gulp](https://github.com/postcss/gulp-postcss), [Grunt](https://github.com/C-Lodder/grunt-postcss), et des bundlers de modules comme [Rollup](https://github.com/egoist/rollup-plugin-postcss) et [Webpack](https://github.com/webpack-contrib/postcss-loader).

Dans cette section, nous verrons comment configurer Grunt pour PostCSS.

Tout d'abord, nous devons installer grunt localement dans les dépendances "dev" :

```bash
npm i -D grunt
```

Et ensuite installer grunt-cli globalement :

```bash
npm install -g grunt-cli
```

Maintenant, nous devons créer un fichier à la racine de notre projet et le nommer **Gruntfile.js**.

Ensuite, nous devons installer un plugin spécifique [@lodder/grunt-postcss](https://www.npmjs.com/package/@lodder/grunt-postcss) pour nous permettre d'exécuter PostCSS en utilisant Grunt via la commande suivante :

```bash
npm i -D @lodder/grunt-postcss
```

À l'intérieur de la fonction `initCnfig`, nous configurons notre configuration PostCSS.

```javascript
module.exports = function(grunt) {

    grunt.initConfig({
        postcss: {
            options: {
                processors: [
                    require('postcss-import')(),
                    require('postcss-mixins'),
                    require("stylelint"),
                    require('postcss-preset-env')({ stage: 1 }),
                    require('cssnano')(),
                ]
            },
            dist: {
                src: 'src/style.css',
                dest: 'public/style.css'
            }
        }
    })

    grunt.loadNpmTasks('@lodder/grunt-postcss');
}
```

Ici, nous nous en tiendrons au minimum de base pour exécuter PostCSS, qui est :

* Appeler nos plugins à l'intérieur du tableau `processors`.
* Configurer le fichier source et le fichier de destination dans l'objet `dist`.

Pour plus de configuration, vous pouvez toujours consulter la documentation officielle pour [@lodder/grunt-postcss](https://github.com/C-Lodder/grunt-postcss).

Pour terminer notre configuration, nous devons charger notre plugin en utilisant la méthode `grunt.loadNpmTasks`.

Enfin, pour exécuter notre tâche Grunt, nous tapons :

```bash
grunt postcss
```

# **Conclusion**

PostCSS existe depuis 2015 et est très populaire parmi les préprocesseurs CSS.

Vous pouvez l'utiliser comme un outil autonome ou en conjonction avec d'autres préprocesseurs existants.

La façon dont vous l'utilisez et comment (autonome ou en conjonction) dépend des besoins de votre projet.

Maintenant, c'est à vous de découvrir la grande variété de plugins qu'il offre et de commencer à jouer avec. Bon codage :)