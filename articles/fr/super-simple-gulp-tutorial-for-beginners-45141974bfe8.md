---
title: Tutoriel Gulp super simple pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T10:17:27.000Z'
originalURL: https://freecodecamp.org/news/super-simple-gulp-tutorial-for-beginners-45141974bfe8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4oEHylwkvSTcgoxgygdbcg.png
tags:
- name: coding
  slug: coding
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tutoriel Gulp super simple pour débutants
seo_desc: 'By Jessica Chan

  These days, using a build tool is an indispensable part of your web development
  workflow.

  Gulp is one of the most popular build tools these days — along with Webpack.

  But there’s a definite learning curve to learning Gulp. One of the ...'
---

Par Jessica Chan

De nos jours, l'utilisation d'un outil de build est une partie indispensable de votre flux de travail en développement web.

[Gulp](https://gulpjs.com/) est l'un des outils de build les plus populaires ces jours-ci, aux côtés de Webpack.

Mais il y a une courbe d'apprentissage certaine pour apprendre Gulp. L'un des plus grands obstacles est de comprendre les centaines de parties différentes qui le composent.

Et en plus de cela, vous devez tout faire sur la ligne de commande, ce qui peut être incroyablement intimidant si vous n'avez pas beaucoup travaillé avec.

Ce tutoriel vous guidera à travers les bases de npm (Node Package Manager) et la configuration de Gulp pour vos projets front-end. Une fois terminé, vous vous sentirez beaucoup plus confiant pour configurer votre flux de travail et utiliser la ligne de commande !

#### **Alors, quel est l'intérêt de Gulp ?**

Gulp est un énorme gain de temps. En utilisant Gulp, vous pouvez laisser votre ordinateur gérer les tâches fastidieuses, telles que :

* Compiler les fichiers Sass en CSS
* Concaténer (combiner) plusieurs fichiers JavaScript
* Minifier (compresser) vos fichiers CSS et JavaScript
* Et exécuter automatiquement les tâches ci-dessus lorsqu'un changement de fichier est détecté

Gulp peut effectuer beaucoup plus de tâches complexes que celles que j'ai mentionnées ci-dessus. Cependant, ce tutoriel se concentrera uniquement sur les bases de Gulp et son fonctionnement.

#### **Aperçu rapide de ce que nous allons faire**

Voici les étapes que ce tutoriel va suivre :

1. Installer Node.js et npm sur votre ordinateur
2. Installer Gulp et les autres packages nécessaires pour votre projet
3. Configurer votre fichier gulpfile.js pour exécuter les tâches que vous souhaitez
4. Laissez votre ordinateur faire le travail pour vous !

Ne vous inquiétez pas si vous ne comprenez pas tous les termes ci-dessus. Je vais tout expliquer étape par étape.

Maintenant, commençons !

### Configurez votre environnement

#### **Node.js**

Pour faire fonctionner Gulp sur votre ordinateur, vous devez installer Node.js sur votre environnement local.

Node.js se décrit comme un "runtime JavaScript", considéré comme le back-end de JavaScript. Gulp fonctionne avec Node, vous devez donc comprendre que vous devez installer Node avant de commencer.

Vous pouvez le télécharger depuis le site [Node.js](https://nodejs.org/en/). Lorsque vous installez Node, il installe également npm sur votre ordinateur.

Qu'est-ce que npm, demandez-vous ?

#### **Npm (Node Package Manager)**

[Npm](https://www.npmjs.com/get-npm) est une collection continuellement mise à jour de plugins JavaScript (appelés packages), écrits par des développeurs du monde entier. Gulp est l'un de ces plugins. Vous aurez également besoin de quelques autres, que nous aborderons plus tard.

L'avantage de npm est qu'il vous permet d'installer des packages directement sur votre ligne de commande. C'est génial, car vous n'avez pas à aller manuellement sur le site, télécharger et exécuter le fichier pour l'installer.

Voici la syntaxe de base pour installer un package :

`npm install [Nom du Package]`

**Note pour les utilisateurs de Mac :** 
 Selon votre configuration, vous devrez peut-être ajouter le mot-clé "sudo" au début pour exécuter cela avec les permissions root.

Ainsi, pour les Mac, cela ressemblerait à : `sudo npm install [Nom du Package]`

Cela semble assez simple, non ?

#### **Le dossier node_modules**

Une chose à noter : lorsque vous installez un package npm, npm crée un dossier appelé node_modules et stocke tous les fichiers du package là.

Si vous avez déjà eu un projet avec un dossier node_modules et osé voir ce qu'il contenait, vous avez probablement vu qu'il avait beaucoup (et je veux dire BEAUCOUP) de dossiers et fichiers imbriqués.

Pourquoi cela se produit-il ?

Eh bien, c'est parce que les packages npm ont tendance à dépendre d'autres packages npm pour exécuter leur fonction spécifique. Ces autres packages sont connus sous le nom de dépendances.

Si vous écrivez un plugin, il est logique de tirer parti des fonctionnalités des packages existants. Personne ne veut réinventer la roue à chaque fois.

Ainsi, lorsque vous installez un plugin dans votre dossier node_modules, ce plugin installera alors des packages supplémentaires dont **il** a besoin dans son propre dossier node_modules.

Et ainsi de suite jusqu'à ce que vous ayez des dossiers imbriqués à l'infini.

Vous n'avez pas besoin de trop vous soucier de toucher au dossier node_modules à ce stade - je voulais juste brièvement expliquer ce qui se passe dans ce dossier fou.

### Suivi des packages avec package.json

Une autre fonctionnalité cool de npm est qu'il peut se souvenir des packages spécifiques que vous avez installés pour votre projet.

Cela est important au cas où vous devriez tout réinstaller pour une raison quelconque.

De plus, cela facilite la vie des autres développeurs, car ils peuvent rapidement et facilement installer tous les packages pour votre projet sur leurs ordinateurs.

Comment fait-il cela ?

Npm utilise un fichier appelé package.json pour garder une trace des packages et des versions de packages que vous avez installés. Il stocke également d'autres informations sur le projet, comme son nom, son auteur et le dépôt Git.

#### **Création de votre package.json**

Pour initialiser ce fichier, vous pouvez à nouveau utiliser la ligne de commande.

Tout d'abord, naviguez jusqu'à votre dossier de projet, où que vous l'ayez situé sur votre ordinateur.

Ensuite, tapez la commande suivante :  
`npm init`

Npm vous demandera alors d'entrer des informations sur le projet. Pour la majorité des options, vous pouvez appuyer sur entrée et utiliser la valeur par défaut qui est entre parenthèses.

Lorsque vous avez terminé, npm générera le fichier package.json dans votre dossier de projet ! Si vous l'ouvrez dans votre éditeur, vous devriez voir quelque chose comme ceci :

```json
{
  "name": "fichier-gulp-super-simple",
  "version": "1.0.0",
  "description": "Fichier Gulp super simple",
  "main": "gulpfile.js",
  "scripts": {
    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/thecodercoder/Super-Simple-Gulp-File.git"
  },
  "keywords": [
    "gulp"
  ],
  "author": "Jessica @thecodercoder",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/thecodercoder/Super-Simple-Gulp-File/issues"
  },
  "homepage": "https://github.com/thecodercoder/Super-Simple-Gulp-File#readme"
}
```

Bien sûr, pour votre projet, vous aurez votre propre nom et informations au lieu de ce que j'ai ici.

À ce stade, je ne m'inquiéterais pas de rendre tous les champs corrects. Cette partie informative est principalement utilisée pour les packages qui sont publiés sur npm en tant que plugins publics.

Maintenant, ce que vous **allez** mettre dans votre fichier package.json, c'est la liste de tous les packages dont vous avez besoin pour exécuter Gulp.

Voyons comment vous pouvez les ajouter.

#### **Installation des packages**

Dans la section précédente ci-dessus, nous avons parlé de taper : `npm install [Nom du Package]` dans votre ligne de commande pour télécharger et installer le package dans votre dossier node_modules.

Il installera le package et l'enregistrera automatiquement dans votre fichier package.json en tant que dépendance.

**Note :** Avant la version 5.0.0 de npm, vous deviez ajouter le drapeau "--save" pour que npm ajoute le package en tant que dépendance. Vous n'avez plus besoin de le faire avec les versions 5 et supérieures.

Ainsi, si nous voulons installer Gulp dans nos packages, nous taperions : `npm install gulp`.

Cela peut prendre une minute ou deux pour que votre ordinateur installe tout ce qui est lié à Gulp. Vous verrez probablement des messages d'avertissement, mais je ne m'inquiéterais pas de ceux-ci sauf si l'installation échoue.

Maintenant, si vous ouvrez votre fichier package.json, vous verrez en bas que Gulp a été ajouté en tant que dépendance :

```
"dependencies": { "gulp": "^3.9.1" }
```

Cette liste de dépendances grandira à mesure que vous installerez des packages npm supplémentaires.

#### **Autres packages nécessaires pour Gulp**

Initialement, nous voulions utiliser Gulp pour exécuter des tâches comme la compilation de vos fichiers SCSS/CSS et JavaScript. Pour y parvenir, nous utiliserons les packages suivants :

* [gulp-sass](https://www.npmjs.com/package/gulp-sass) — compile vos fichiers Sass en CSS
* [gulp-cssnano](https://www.npmjs.com/package/gulp-cssnano) — minifie vos fichiers CSS
* [gulp-concat](https://www.npmjs.com/package/gulp-concat) — concatène (combine) plusieurs fichiers JavaScript en un seul fichier volumineux
* [gulp-uglify](https://www.npmjs.com/package/gulp-uglify) — minifie vos fichiers JavaScript

Comme avant, installez chaque package en tapant ces lignes une par une. Vous devrez attendre quelques secondes pendant que chacun s'installe avant de passer à la ligne suivante.

```
npm install gulp-sass 
npm install gulp-cssnano 
npm install gulp-concat 
npm install gulp-uglify
```

#### **Gulp-cli vs Gulp global**

Auparavant, pour pouvoir exécuter « gulp » depuis votre ligne de commande, vous deviez installer Gulp globalement sur votre ordinateur local, en utilisant la commande :  
   
`npm install --global gulp`

Cependant, avoir une seule version globale de Gulp pouvait causer des problèmes si vous aviez plusieurs projets nécessitant différentes versions de Gulp.

Le consensus actuel recommande d'installer un package différent, [Gulp-cli](https://gulpjs.org/getting-started), globalement au lieu de Gulp lui-même.

Cela vous permettra toujours d'exécuter la commande « gulp », mais vous pourrez utiliser différentes versions de Gulp dans vos différents projets.

Voici le code pour cela :

```
npm install --global gulp-cli
```

Si vous êtes intéressé, vous pouvez lire plus de contexte sur ce [fil de discussion Treehouse](https://teamtreehouse.com/community/gulp-global-install-gulp-vs-gulpcli).

Très bien, une fois tous vos packages installés, vous avez tous les outils nécessaires. Passons à la configuration de nos fichiers de projet !

### Configurez votre structure de fichiers

Avant de commencer à créer des fichiers et des dossiers, sachez qu'il existe de nombreuses façons différentes de configurer votre structure de fichiers. L'approche que vous utiliserez est bonne pour les projets de base, mais la configuration « correcte » dépendra beaucoup de vos besoins particuliers.

Cette méthode de base vous aidera à comprendre le fonctionnement de base de toutes les parties mobiles. Ensuite, vous pourrez développer ou modifier la configuration selon vos préférences à l'avenir !

Voici à quoi ressemblera l'arborescence du projet :

**Dossier racine du projet**

* index.html
* gulpfile.js
* package.json
* node_modules (dossier)
* app (dossier)
* script.js
* style.scss
* dist (dossier)

Nous avons déjà parlé du fichier package.json et du dossier node_modules. Et le fichier index.html sera, bien sûr, votre fichier principal de site web.

Le fichier gulpfile.js est l'endroit où nous configurerons Gulp pour exécuter toutes les tâches dont nous avons parlé au début de cet article. Nous y reviendrons dans un instant.

Mais pour l'instant, je veux mentionner les deux dossiers, app et dist, car ils sont importants pour le flux de travail de Gulp.

#### **Dossiers App et Dist**

Dans le dossier app, nous avons votre fichier JavaScript de base (script.js) et votre fichier SCSS de base (style.scss). Ces fichiers sont ceux où vous écrirez tout votre code JavaScript et CSS.

Le dossier dist existe uniquement pour stocker les fichiers JavaScript et CSS compilés finaux après que Gulp les ait traités. Vous ne devez apporter aucune modification aux fichiers dist, seulement aux fichiers app. Mais ces fichiers dans dist sont ceux qui seront chargés dans index.html, puisque nous voulons utiliser les fichiers compilés dans le site web.

Encore une fois, il existe de nombreuses façons de configurer vos fichiers et dossiers de projet. L'essentiel est que votre structure ait du sens et vous permette de travailler le plus efficacement possible.

Maintenant, passons au cœur de ce tutoriel : la configuration de Gulp !

### Créez et configurez votre Gulpfile

Le Gulpfile contient le code pour charger les packages installés et exécuter différentes fonctions. Le code effectue deux fonctions de base :

1. Initialiser vos packages installés en tant que modules Node.
2. Créer et exécuter des tâches Gulp.

#### **Initialiser les packages**

Pour tirer parti de toutes les fonctionnalités des packages npm que vous avez ajoutés à votre projet, vous devez les exporter en tant que modules dans Node — d'où le nom du dossier « node_modules ».

En haut de votre Gulpfile, ajoutez les modules comme ceci :

```javascript
var gulp = require('gulp'); 
var cssnano = require('gulp-cssnano'); 
var sass = require('gulp-sass'); 
var concat = require('gulp-concat'); 
var uglify = require('gulp-uglify');
```

Maintenant que les packages sont ajoutés, vous pouvez utiliser leurs fonctions et objets dans vos scripts Gulpfile. Vous utiliserez également certaines fonctions intégrées qui font partie de Node.js.

Si vous souhaitez en savoir plus sur les packages npm et les modules Node, le site npm propose une excellente explication [ici](https://docs.npmjs.com/getting-started/packages).

### **Créez vos tâches Gulp**

La création d'une tâche Gulp se fait en utilisant le code suivant :

```javascript
gulp.task('[Nom de la Fonction]', function(){    
   // Faire des choses ici 
}
```

Cela vous permet d'exécuter la tâche Gulp en tapant `gulp [Nom de la Fonction]` dans la ligne de commande. Cela est important car vous pouvez alors exécuter cette fonction nommée à partir d'autres tâches Gulp.

Plus précisément, nous construisons plusieurs tâches Gulp différentes, qui seront **toutes** exécutées lorsque vous exécuterez la tâche Gulp par défaut.

Certaines des principales fonctions que nous utiliserons sont :

* `.task()` — Crée une tâche, comme mentionné ci-dessus
* `.src()` — Identifie les fichiers que vous allez compiler dans une tâche particulière
* `.pipe()` — Ajoute une fonction au flux Node que Gulp utilise ; vous pouvez transmettre plusieurs fonctions dans la même tâche (lisez un excellent article sur ce sujet sur [florian.ec](https://florian.ec/articles/gulp-js-streams/))
* `.dest()` — Écrit le fichier résultant à un emplacement spécifique
* `.watch()` — Identifie les fichiers pour détecter tout changement

Si vous êtes curieux, vous pouvez en savoir plus sur la documentation de Gulp [ici](https://github.com/gulpjs/gulp/tree/v3.9.1/docs).

Tout est prêt ? Maintenant, passons aux choses sérieuses (cue Mulan music) et écrivons ces tâches !

Voici les tâches suivantes que nous voulons que Gulp exécute :

* Tâche Sass pour compiler SCSS en un fichier CSS et minifier
* Tâche JavaScript pour concaténer les fichiers JavaScript et minifier/uglifier
* Tâche Watch pour détecter lorsque les fichiers SCSS ou JavaScript sont modifiés, et réexécuter les tâches
* Tâche par défaut pour exécuter toutes les tâches nécessaires lorsque vous tapez `gulp` dans la ligne de commande

#### **Tâche Sass**

Pour la tâche Sass, nous voulons d'abord créer la tâche dans Gulp en utilisant `task()`, et nous la nommerons « sass ».

Ensuite, nous ajoutons chaque composant que la tâche exécutera. Tout d'abord, nous désignerons que la source sera le fichier app/scss/style.scss, en utilisant `src()`. Ensuite, nous ajouterons les fonctions supplémentaires.

La première exécute la fonction `sass()` — en utilisant le module gulp-sass que nous avons appelé « sass » en haut du Gulpfile. Il enregistrera automatiquement le fichier CSS avec le même nom que le fichier SCSS, donc le nôtre s'appellera style.css.

La seconde minifie le fichier CSS avec `cssnano()`. Et la dernière place le fichier CSS résultant dans le dossier dist/css.

Voici le code pour tout cela :

```javascript
gulp.task('sass', function(){    
    return gulp.src('app/style.scss')       
        .pipe(sass())       
        .pipe(cssnano())       
        .pipe(gulp.dest('dist/css')); 
});
```

Pour tester, j'ai simplement mis du SCSS de remplissage dans le fichier style.scss :

```css
div {    
    display: block; 
   	&.content {       
        position: relative;    
    } 
} 

.red { 
    color: red; 
}
```

Vous pouvez exécuter chaque tâche Gulp individuelle sur la ligne de commande si vous tapez `gulp` et le nom de la tâche. Donc pour tester la tâche Sass, j'ai tapé `gulp sass` pour vérifier si elle fonctionne sans erreurs, et génère le fichier dist/style.css minifié.

Si tout fonctionne correctement, vous devriez voir des messages comme ceci dans votre ligne de commande :

```
[15:04:53] Début de 'sass'... [15:04:53] Fin de 'sass' après 121 ms
```

En vérifiant dans le dossier dist, on voit qu'il y a effectivement un fichier style.css, et en l'ouvrant, on voit du CSS correctement minifié :

```
div{display:block}div.content{position:relative}.red{color:red}
```

Ok, notre tâche Sass est maintenant terminée. Passons à JavaScript !

#### **Tâche JS**

La tâche Gulp JS est similaire à la tâche Sass, mais comporte quelques éléments différents.

Tout d'abord, nous créerons la tâche et l'appellerons « js », puis nous identifierons les fichiers sources. Dans la fonction `src()`, vous pouvez identifier plusieurs fichiers de différentes manières.

L'une consiste à utiliser le caractère générique `(* )` pour indiquer à Gulp d'utiliser tous les fichiers avec l'extension `*.js` comme ceci :

```
gulp.src('app/*.js')
```

Cependant, cela compilera les fichiers dans l'ordre alphabétique, ce qui pourrait potentiellement causer des erreurs si vous finissez par charger des scripts qui dépendent d'autres scripts avant ces autres fichiers de script.

Vous pouvez contrôler l'ordre en désignant manuellement chaque fichier JavaScript si vous n'avez pas trop de fichiers de script.

La fonction `src()` peut prendre un tableau de valeurs comme paramètre, en utilisant les crochets comme ceci :

```
gulp.src(['app/script.js', 'app/script2.js'])
```

Si vous avez beaucoup de fichiers JavaScript, vous pouvez vous assurer de charger d'abord les dépendances en les gardant dans un sous-dossier séparé, comme par exemple « app/js/plugins ». Ensuite, gardez les autres fichiers JavaScript dans le dossier parent « app/js ».

Ensuite, vous pouvez utiliser la notation générique pour charger tous les scripts de lib (bibliothèque), suivis des scripts réguliers :

```
gulp.src(['app/js/lib/*.js', 'app/js/script/*.js'])
```

Votre approche variera en fonction du nombre et des types de fichiers JavaScript que vous avez.

Une fois que vous avez défini vos fichiers sources, vous allez ajouter les fonctions restantes. La première consiste à concaténer les fichiers en un seul grand fichier JavaScript. La fonction `concat()` nécessite un paramètre avec le nom du fichier résultant.

Ensuite, vous allez uglifier le fichier JavaScript et l'enregistrer à l'emplacement de destination.

Voici le code complet pour la tâche JS :

```javascript
gulp.task('js', function(){    
    return gulp.src(['app/js/plugins/*.js', 'app/js/*.js'])          
        .pipe(concat('all.js'))       
        .pipe(uglify())       
        .pipe(gulp.dest('dist')); 
});
```

Tout comme la tâche Sass, vous pouvez tester que la tâche JS fonctionne en tapant `gulp js` dans la ligne de commande.

```
[14:38:31] Début de 'js'... [14:38:31] Fin de 'js' après 36 ms
```

Maintenant que nous avons terminé nos deux principales tâches de travail Gulp, nous pouvons passer à la tâche Watch.

#### **Tâche Watch**

La tâche Watch surveillera les fichiers que vous lui indiquerez pour tout changement. Une fois qu'elle détecte un changement, elle exécutera les tâches que vous désignerez et continuera à surveiller les changements.

Nous allons créer deux fonctions de surveillance, une pour surveiller les fichiers SCSS et l'autre pour surveiller les fichiers JavaScript.

La fonction `watch()` prend deux paramètres : l'emplacement source, puis les tâches à exécuter lorsqu'un changement est détecté.

La fonction de surveillance Sass surveillera tout fichier SCSS dans le dossier app et exécutera la tâche Sass si elle détecte des changements.

La fonction ressemblera à ceci :

```
gulp.watch('app/*.scss', ['sass']);
```

Pour la fonction de surveillance JS, nous devrons tirer parti d'une fonctionnalité Node très utile appelée « globbing ». Le globbing fait référence à l'utilisation des symboles « ** » comme une sorte de caractère générique pour les dossiers et sous-dossiers. Nous en avons besoin pour les fichiers JavaScript, car nous avons un fichier JavaScript dans le dossier app/js, et un fichier JavaScript dans le dossier app/js/plugins.

Et voici à quoi ressemblera cette fonction :

```
gulp.watch('app/js/**/*.js', ['js']);
```

La façon dont le glob (« ** ») fonctionne est qu'il recherchera des fichiers JavaScript n'importe où dans le dossier app/js. Il recherchera soit directement dans le dossier, soit dans n'importe quel dossier enfant ultérieur, comme le dossier plugins. Le globbing est pratique afin que vous n'ayez pas à désigner chaque sous-dossier comme une source séparée dans la fonction `watch()`.

Voici la tâche Watch complète :

```javascript
gulp.task('watch', function(){       
	gulp.watch('app/*.scss', ['sass']);          
    gulp.watch('app/js/**/*.js', ['js']); 
});
```

Maintenant, nous avons presque terminé ! La dernière tâche à créer est la tâche Gulp par défaut.

#### **Tâche Gulp par défaut**

La tâche Gulp par défaut est celle que vous souhaitez exécuter lorsque vous tapez simplement `gulp` dans la ligne de commande. Lorsque vous créez la tâche, vous devez l'appeler « default » afin que Gulp reconnaisse que c'est ce que vous voulez exécuter.

Ce que nous aimerions faire, c'est exécuter les tâches Sass et JS une fois, puis exécuter la tâche Watch pour réexécuter les tâches lorsque les fichiers sont modifiés.

```
gulp.task('default', ['sass', 'js', 'watch']);
```

Vous pouvez créer d'autres tâches pour exécuter vos builds, il suffit de ne pas réutiliser le nom « default ». Par exemple, disons que vous souhaitez laisser vos fichiers CSS et JavaScript non minifiés par défaut, mais que vous souhaitez les minifier pour la production.

Vous pourriez créer des tâches Gulp séparées pour minifier vos fichiers CSS et JavaScript appelées « minifyCSS » et « minifyJS ». Ensuite, vous n'ajouteriez pas ces tâches à votre tâche Gulp par défaut, mais vous pourriez créer une nouvelle tâche Gulp appelée « prod » qui contient tout ce que la tâche par défaut a, ainsi que vos tâches de minification.

#### **Références dans votre index.html**

Une fois que vous avez fait fonctionner votre processus Gulp, assurez-vous que votre fichier index.html référence tous les fichiers CSS et JavaScript corrects.

Pour les exemples que je vous ai donnés ici, vous voudrez ajouter une référence CSS à `dist/style.css` dans votre <head> :

```html
<link rel="stylesheet" href="dist/style.css">
```

Et ajouter une balise script référençant `dist/all.js` dans votre <body> :

```html
<script src="dist/all.js"></script>
```

### En conclusion

Félicitations pour être arrivé jusqu'au bout ! J'espère que vous avez trouvé ce tutoriel de base sur Gulp utile.

Comme je l'ai mentionné au début, ce n'est qu'un tutoriel très simple sur les bases de npm et Gulp.

La plupart des développeurs ajoutent de nombreuses tâches supplémentaires à leur Gulpfile. Faites-moi savoir si vous seriez intéressé à voir un autre article sur ces sujets plus avancés !

Enfin, vous pouvez consulter tout le code de ce tutoriel sur mon compte GitHub [ici](https://github.com/thecodercoder/Super-Simple-Gulp-File).

J'espère que vous avez trouvé cet article utile ! Faites-moi savoir vos pensées dans les commentaires ci-dessous.

#### Vous en voulez plus ?

* Lisez plus de tutoriels sur mon blog, [coder-coder.com](https://coder-coder.com).
* Inscrivez-vous ici pour recevoir des emails sur les nouveaux articles : [coder-coder.com/subscribe](https://coder-coder.com/subscribe).
* Rejoignez plus de 25 000 autres personnes - Suivez @thecodercoder sur Instagram : [instagram.com/thecodercoder](https://www.instagram.com/thecodercoder/).
* Consultez les tutoriels de codage sur [ma chaîne YouTube](https://www.youtube.com/c/codercodertv).

_Cet article a été initialement publié sur [Coder-Coder.com](https://coder-coder.com/gulp-tutorial-beginners/).