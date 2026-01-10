---
title: Utiliser Gulp 4 dans votre flux de travail pour les fichiers Sass et JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T03:27:19.000Z'
originalURL: https://freecodecamp.org/news/gulp-4-walk-through-with-example-code-c3c018eab306
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Gulp-4-workflow-walkthrough.png
tags:
- name: Gulp
  slug: gulp
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Utiliser Gulp 4 dans votre flux de travail pour les fichiers Sass et JS
seo_desc: 'By Jessica Chan

  This post was originally published on Coder-Coder.com.


  This tutorial will explain, step by step, how to set up Gulp 4 in your workflow,
  as well as how to migrate from Gulp 3 to Gulp 4 syntax.


  Need to just quickly get your Gulp 3 gul...'
---

Par Jessica Chan

<p><em>Cet article a été initialement publié sur <a href="https://coder-coder.com/gulp-4-walk-through/">Coder-Coder.com</a>.</em></p>

Ce tutoriel expliquera, étape par étape, comment configurer Gulp 4 dans votre flux de travail, ainsi que comment migrer de la syntaxe Gulp 3 à Gulp 4.

> _Besoin de faire fonctionner rapidement votre fichier gulpfile.js de Gulp 3 avec Gulp 4 ? [Cliquez ici](#migrating) pour accéder directement à cette partie de l'article._

1. Installez le gulp-cli sur votre ligne de commande en exécutant `npm install gulp-cli -g`.
2. Installez Gulp en exécutant `npm install gulp`.
3. Installez d'autres packages npm pour votre flux de travail Gulp.
4. Créez un fichier `gulpfile.js` à la racine de votre projet.
5. Importez vos packages npm en tant que modules dans votre gulpfile.
6. Ajoutez vos tâches au gulpfile pour compiler vos fichiers SCSS/JS et exécuter une tâche de surveillance.
7. Exécutez la commande `gulp` pour exécuter toutes vos tâches.

### Qu'est-ce que Gulp et que fait-il ?

Gulp est un outil qui exécutera diverses tâches pour vous dans votre flux de travail de développement web. Il peut être appelé un bundler, un outil de build ou un task runner. Tous ces termes signifient à peu près la même chose.

Des outils similaires sont Webpack et Grunt (bien que Grunt devienne rapidement obsolète).

Voici ce que nous allons faire faire à Gulp pour nous :

1. Compiler nos fichiers Sass en CSS
2. Ajouter des préfixes vendeurs à notre CSS
3. Minifier notre fichier CSS final
4. Concaténer (c'est-à-dire combiner) nos fichiers JS
5. Uglifier notre fichier JS final
6. Déplacer les fichiers CSS/JS finaux dans notre dossier `/dist`.

Plutôt cool, n'est-ce pas ?!

Le fonctionnement est le suivant : toutes vos configurations et tâches sont stockées dans un fichier `gulpfile.js`. Et vous exécutez Gulp sur votre ligne de commande.

Le grand avantage est que, une fois votre gulpfile configuré, vous pouvez facilement le réutiliser pour d'autres projets. C'est donc un gain de temps énorme !

Passons à l'installation et à la configuration de Gulp sur votre ordinateur.

### Installation de Gulp, en utilisant un projet de démonstration fonctionnel

Avant de pouvoir exécuter Gulp, vous devrez installer quelques éléments :

* Installez [Node.js](https://nodejs.org/en/) si vous ne l'avez pas encore.
* Installez l'[Utilitaire de ligne de commande Gulp](https://www.npmjs.com/package/gulp-cli) en exécutant `npm install --global gulp-cli`.

Une fois que Gulp est opérationnel, consultez un projet de démonstration que j'ai construit et qui utilise Gulp ! Il s'agit d'un projet de modèle de front-end destiné à être un moyen rapide pour moi de commencer avec n'importe quel site web front-end simple.

(J'ai également de nombreux extraits de code dans le reste de ce tutoriel, donc vous pouvez vous y référer également !)

**Pour configurer le projet de modèle de front-end :**

* Clonez ou téléchargez le [dépôt Git](https://github.com/thecodercoder/frontend-boilerplate) de ce projet sur votre ordinateur.
* Ouvrez le projet, et dans le dossier racine du projet, allez sur votre ligne de commande et exécutez `npm install`. Cela installera les packages npm listés dans le fichier `package.json`, en particulier Gulp 4.

Vous devriez maintenant avoir les fichiers du projet configurés, et tous les packages npm installés que nous utiliserons pour exécuter les tâches Gulp.

Puisque les fichiers du dépôt sont prêts à l'emploi, si vous tapez `gulp` dans la ligne de commande, vous devriez voir une sortie comme celle-ci :

```
> gulp [22:29:48] Using gulpfile ~\Documents\GitHub\frontend-boilerplate\gulpfile.js [22:29:48] Starting 'default'... [22:29:48] Starting 'scssTask'... [22:29:48] Starting 'jsTask'... [22:29:48] Finished 'jsTask' after 340 ms [22:29:48] Finished 'scssTask' after 347 ms [22:29:48] Starting 'watchTask'...
```

Et vous avez exécuté Gulp !

### Que se passe-t-il dans le projet lorsque vous exécutez Gulp ?

Très bien, vous avez réussi à faire fonctionner le projet ! Maintenant, examinons plus en détail ce qu'il y a dans le projet et comment il fonctionne.

Tout d'abord, voici un bref aperçu de la structure des fichiers de notre projet :

* **index.html** — votre fichier HTML principal
* **package.json** — contient tous les packages npm à installer lorsque vous exécutez `npm install`.
* **gulpfile.js** — contient la configuration et exécute toutes les tâches Gulp
* **/app** — dossier de travail, vous éditerez les fichiers SCSS/JS ici
* **/dist** — Gulp générera les fichiers ici, ne modifiez pas ces fichiers

Dans votre flux de travail, vous éditerez les fichiers HTML, SCSS et JS. Gulp détectera ensuite les modifications et compilera tout. Ensuite, vous chargerez vos fichiers CSS/JS finaux à partir du dossier `/dist` dans votre fichier `index.html`.

Maintenant que nous avons Gulp en cours d'exécution, examinons de plus près comment Gulp fonctionne.

### Que contient exactement le fichier gulpfile.js ?

Voici une explication détaillée de chaque section du gulpfile, et de ce qu'elles font :

#### Étape 1 : Initialiser les modules npm

Tout en haut du fichier `gulpfile.js`, nous avons un ensemble de constantes qui importent les packages npm que nous avons installés précédemment, en utilisant la fonction `require()`.

Voici ce que font nos packages :

Package Gulp :

* `gulp` — exécute tout dans le fichier gulpfile.js. Nous exportons uniquement les fonctions gulp spécifiques que nous utiliserons, comme `src`, `dest`, `watch`, et d'autres. Cela nous permet d'appeler ces fonctions directement sans le préfixe `gulp`, par exemple, nous pouvons simplement taper `src()` au lieu de `gulp.src()`.

Packages CSS :

* `gulp-sourcemaps` — mappe les styles CSS vers le fichier SCSS original dans les outils de développement de votre navigateur
* `gulp-sass` — compile SCSS en CSS
* `gulp-postcss` — exécute autoprefixer et cssnano (voir ci-dessous)
* `autoprefixer` — ajoute des préfixes vendeurs au CSS
* `cssnano` — minifie le CSS

> _Si vous avez déjà utilisé Gulp, vous vous demandez peut-être pourquoi j'utilise directement `autoprefixer` et `cssnano`, au lieu de `gulp-autoprefixer` et `gulp-cssnano`. Pour une raison quelconque, les utiliser fonctionnera, mais empêchera les sourcemaps de fonctionner. Lisez plus sur ce problème [ici](https://github.com/gulp-sourcemaps/gulp-sourcemaps/issues/60)._

Packages JS :

* `gulp-concat` — concatène plusieurs fichiers JS en un seul fichier
* `gulp-uglify` — minifie le JS

Maintenant que nous avons ajouté nos modules, utilisons-les !

#### Étape 2 : Utiliser les modules pour exécuter vos tâches

Une « tâche » dans Gulp est essentiellement une fonction qui remplit un but spécifique.

Nous créons quelques tâches utilitaires pour compiler nos fichiers SCSS et JS, et aussi pour surveiller ces fichiers pour toute modification. Ensuite, ces tâches utilitaires seront exécutées dans notre tâche Gulp par défaut lorsque nous tapons `gulp` sur la ligne de commande.

#### **Création de constantes pour les chemins de fichiers**

Avant d'écrire nos tâches, nous avons quelques lignes de code qui enregistrent nos chemins de fichiers en tant que constantes. Cela est facultatif, mais j'aime utiliser des variables de chemin afin de ne pas avoir à les retaper manuellement chaque fois :

Ce code crée des constantes `scssPath` et `jsPath` que nous utiliserons pour indiquer à Gulp où se trouvent les fichiers.

#### **Tâche Sass**

Voici le code pour notre tâche Sass :

```
function scssTask(){        return src(files.scssPath)        .pipe(sourcemaps.init())        .pipe(sass())        .pipe(postcss([ autoprefixer(), cssnano() ]))        .pipe(sourcemaps.write('.'))        .pipe(dest('dist')    );}
```

Notre tâche Sass, appelée `scssTask()`, fait plusieurs choses. Dans Gulp, vous pouvez enchaîner plusieurs fonctions en utilisant la fonction Gulp `pipe()` après la première fonction.

Dans notre tâche, Gulp exécute d'abord `src()` pour charger le répertoire source des fichiers SCSS. Il utilise la constante que nous avons créée précédemment, `files.scssPath`.

Ensuite, après `src()`, nous transmettons tout le reste dans le processus de build. Vous pouvez penser à cela comme ajouter de plus en plus de sections de tuyau à un tuyau existant.

Les fonctions qu'il exécute sont :

* `sourcemaps.init()` — les sourcemaps doivent être ajoutées en premier après `src()`
* `sass()` effectue la compilation de tous les fichiers SCSS en un fichier CSS
* `postcss()` exécute deux autres plugins :
* - `autoprefixer()` pour ajouter des préfixes vendeurs au CSS
* - `cssnano()` pour minifier le fichier CSS
* `sourcemaps.write()` crée le fichier sourcemaps dans le même répertoire.
* `dest()` indique à Gulp de placer le fichier CSS final et le fichier sourcemaps CSS dans le dossier `/dist`.

#### **Tâche JS**

Voici le code pour notre tâche JavaScript :

```
function jsTask(){    return src([files.jsPath])        .pipe(concat('all.js'))        .pipe(uglify())        .pipe(dest('dist')    );}
```

Notre tâche JavaScript, appelée `jsTask()`, exécute également plusieurs fonctions :

* `src()` pour charger les fichiers JS à partir de `files.jsPath`.
* `concat()` pour concaténer tous les fichiers JS en un seul fichier JS.
* `uglify()` pour uglifier/minifier le fichier JS.
* `dest()` pour déplacer le fichier JS final dans le dossier `/dist`.

#### **Tâche Watch**

La fonction `watch()` est une partie super pratique de Gulp. Lorsque vous l'exécutez, elle s'exécutera en continu, attendant de détecter toute modification des fichiers que vous lui dites de surveiller. Lorsqu'elle détecte des modifications, elle exécutera un nombre quelconque de tâches que vous lui dites d'exécuter.

C'est génial car vous n'avez pas à continuer à exécuter manuellement `gulp` après chaque modification de code.

Voici le code pour notre tâche watch :

```
function watchTask(){    watch(        [files.scssPath, files.jsPath],        parallel(scssTask, jsTask)    );}
```

La fonction `watch()` prend trois paramètres, mais nous n'en utilisons que deux :

* globs, c'est-à-dire les chaînes de chemin de fichier,
* options (non utilisées), et
* tâches, c'est-à-dire les tâches que nous voulons exécuter.

Ce que nous faisons faire à notre tâche watch est de surveiller les fichiers dans nos répertoires `scssPath` et `jsPath`. Ensuite, si des modifications sont apportées dans l'un ou l'autre, exécuter les tâches `scssTask` et `jsTask` simultanément.

Maintenant que nous avons configuré nos tâches utilitaires, nous devons configurer notre tâche principale Gulp.

#### **Tâche par défaut**

Il s'agit de la tâche principale Gulp, qui s'exécutera automatiquement si vous tapez `gulp` sur la ligne de commande.

```
exports.default = series( parallel(scssTask, jsTask), watchTask);
```

Gulp recherchera automatiquement une tâche `default` dans votre `gulpfile.js` lorsque vous utiliserez la commande `gulp`. Vous devez donc exporter la tâche par défaut pour qu'elle fonctionne.

Notre tâche par défaut fera ce qui suit :

* Exécuter les tâches `scssTask` et `jsTask` simultanément en utilisant `parallel()`
* Ensuite, exécuter la tâche `watchTask`

Vous remarquerez également que nous plaçons toutes ces tâches à l'intérieur de la fonction `series()`.

**Il s'agit de l'un des principaux nouveaux changements dans Gulp 4 pour la gestion des tâches — vous êtes tenu d'envelopper toutes les tâches (même les tâches uniques) soit dans `series()`, soit dans `parallel()`.**

### Une note sur l'enregistrement des tâches : ce qui a changé dans Gulp 4

Si vous avez utilisé la fonction `tasks()` pour exécuter tout, vous avez peut-être remarqué qu'il y a une différence maintenant.

Au lieu d'utiliser `gulp.task()` pour contenir toutes vos fonctions de tâche, nous créons des fonctions réelles comme `scssTask()` et `watchTask()`.

Cela suit les directives officielles de Gulp pour la création de tâches.

L'équipe Gulp recommande d'utiliser `exports` plutôt que `tasks()` :

> _« Dans le passé, `task()` était utilisé pour enregistrer vos fonctions en tant que tâches. Bien que cette API soit toujours disponible, l'exportation devrait être le mécanisme d'enregistrement principal, sauf dans les cas particuliers où les exports ne fonctionneront pas. » [[Documentation Gulp](https://gulpjs.com/docs/en/getting-started/creating-tasks)]_

Ainsi, bien qu'ils vous permettent toujours d'utiliser la fonction `task()`, il est plus actuel de créer des fonctions JS pour chaque tâche, puis de les exporter.

<a name="migrating"></a>

Si possible, je recommanderais de mettre à jour votre syntaxe pour refléter cela, car il est possible que Gulp déprécie `task()` à un moment donné.

### Problèmes de migration de Gulp 3 ?

Si vous avez utilisé Gulp 3 et que tout ce que vous voulez est de faire fonctionner cette chose avec Gulp 4, vous avez de la chance !

Auparavant, dans Gulp 3, vous pouviez simplement lister une seule fonction ou plusieurs fonctions dans un tableau. Cependant, dans Gulp 4, le faire sans les envelopper dans `series()` ou `parallel()` générera maintenant une erreur.

Quelque chose comme :

`AssertionError [ERR_ASSERTION]: Task function must be specified`

Gulp 4 introduit deux nouvelles fonctions pour exécuter des tâches : `series()` et `parallel()`. Il vous donne l'option d'exécuter plusieurs tâches simultanément, ou l'une après l'autre.

Ainsi, pour corriger rapidement l'erreur, placez toutes vos tâches dans une fonction `series()` ou `parallel()`.

**Tâches en syntaxe (ancienne) Gulp 3**

Dans Gulp 3, vous auriez peut-être exécuté des tâches de cette manière :

`gulp.task('default', ['sass', 'js', 'watch']);`

`gulp.watch('app/scss/*.scss', ['sass']);`

**Tâches en syntaxe Gulp 4**

Placez ces tâches dans une fonction series() comme ceci :

`gulp.task('default', gulp.series('sass', 'js', 'watch'));`

`gulp.watch('app/scss/*.scss', gulp.series('sass'));`

Et cela corrigera l'erreur de fonction de tâche avec le plus petit changement possible ! ?

### **Téléchargement des fichiers du projet**

Tout le code que j'ai affiché ici provient d'un dépôt GitHub que j'ai pour le modèle de front-end. Il est destiné à être un kit de démarrage rapide pour tout projet de site web front-end simple.

Vous êtes libre de le consulter, de le personnaliser et de l'utiliser pour vos propres projets !

[Consultez le dépôt GitHub ici.](https://github.com/thecodercoder/frontend-boilerplate)

### **En conclusion**

J'espère que vous avez trouvé ce guide sur la façon de faire fonctionner Gulp 4 utile !

Si vous avez aimé cet article ou si vous avez une question, n'hésitez pas à laisser un commentaire ci-dessous ! ?

**Vous voulez plus ?**

? Lisez plus de tutoriels sur mon blog, [coder-coder.com.](https://coder-coder.com)  
? Inscrivez-vous ici pour recevoir des emails sur les nouveaux articles.  
? Rejoignez plus de 24 000 autres — Suivez @[thecodercoder sur Instagram.](https://www.instagram.com/thecodercoder/)  
? Consultez les tutoriels de codage sur [ma chaîne YouTube](https://www.youtube.com/c/codercodertv).