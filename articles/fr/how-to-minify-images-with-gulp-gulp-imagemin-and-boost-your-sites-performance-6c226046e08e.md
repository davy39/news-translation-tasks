---
title: Comment minifier des images avec Gulp & gulp-imagemin et améliorer les performances
  de votre site
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T19:47:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-minify-images-with-gulp-gulp-imagemin-and-boost-your-sites-performance-6c226046e08e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca58e740569d1a4ca6a30.jpg
tags:
- name: Gulp
  slug: gulp
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment minifier des images avec Gulp & gulp-imagemin et améliorer les
  performances de votre site
seo_desc: 'By Jonathan Sexton

  Images are everywhere across the internet. You would be hard pressed to find a single
  page or application that doesn’t contain at least one image in some form or another.
  Images are great way to help tell stories and emphasize crit...'
---

Par Jonathan Sexton

Les images sont partout sur Internet. Vous auriez du mal à trouver une seule page ou application qui ne contient pas au moins une image sous une forme ou une autre. Les images sont un excellent moyen d'aider à raconter des histoires et de mettre en avant des parties critiques de nos vies.

Mais si vous êtes comme moi, vous savez qu'avoir une image volumineuse peut sérieusement affecter les performances de votre site/application. Aujourd'hui, je vais donc vous apprendre à utiliser Gulp et un package `npm` appelé `gulp-imagemin` pour réduire la taille de vos images à la volée.

Si vous ne savez pas ce que signifient tous ces termes, ne vous inquiétez pas ! J'ai quelques liens et descriptions pertinents ci-dessous pour vous aider à vous mettre à jour.

* La [Minification](https://en.wikipedia.org/wiki/Minification_(programming)), ou minification comme j'aime l'appeler, est l'acte ou le processus de suppression des parties inutiles du code source pour réduire sa taille.
* `Gulp` est un outil de build JavaScript qui vous permet d'automatiser certaines parties de votre flux de travail pour rationaliser votre processus. Il s'occupe de certains aspects importants mais peu intéressants de votre flux de travail (comme la réduction de la taille des images) afin que vous puissiez vous concentrer sur la construction. Vous pouvez [trouver Gulp ici](https://gulpjs.com/).
* Pour utiliser `npm`, nous devons installer `Node.js`, qui est, en résumé, le framework qui permet aux développeurs d'utiliser du code JavaScript dans un environnement serveur (back-end). Vous pouvez [trouver Node ici](https://nodejs.org/en/download/).
* `npm` (Node Package Manager) est et fait ce que son nom implique. C'est un gestionnaire de packages pour JavaScript et "le plus grand registre de logiciels au monde". Imaginez `npm` comme une immense zone de stockage pour des packages/utilitaires géniaux pour aider les développeurs. Vous pouvez [trouver npm ici](https://www.npmjs.com/).
* `gulp-imagemin` est l'un de ces packages géniaux dont j'ai parlé plus tôt. En utilisant ce package, nous pourrons automatiquement réduire la taille de nos images à chaque fois qu'une sauvegarde se produit. Vous pouvez [trouver gulp-imagemin ici](https://www.npmjs.com/package/gulp-imagemin).

D'accord, maintenant que les explications sont terminées, passons aux parties amusantes :D

### Structure des fichiers du projet

Commencez par ouvrir votre éditeur de texte préféré et créez un répertoire pour votre projet, ou si vous avez déjà un répertoire existant, naviguez jusqu'à ce répertoire dans votre terminal et passez à la **section Installation de Node & npm**.

Si vous utilisez [VS Code](https://code.visualstudio.com/), vous pouvez trouver le [terminal intégré](https://code.visualstudio.com/docs/editor/integrated-terminal) en appuyant sur `ctrl + ` (tilde).

Voici à quoi ressemble la structure de mon projet dans mon terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/SFUA0D00x1r1kSEyEAha4U0uoXy5zUVKElHf)

Et voici à quoi ressemble la structure des fichiers de mon projet dans l'explorateur de VS Code :

![Image](https://cdn-media-1.freecodecamp.org/images/8GrSHZyzovwyyYWmHSBRWhR0CBVrZPKQfUsX)

Comme vous pouvez le voir, j'ai un répertoire séparé pour mes fichiers de base et les fichiers minifiés. Une fois que vous avez établi votre répertoire de projet, il est temps de commencer à installer tout ce dont nous aurons besoin.

### Installation de Node & npm

D'accord, maintenant que notre répertoire est opérationnel, commençons à installer nos dépendances. Si vous avez déjà installé `Node & npm`, vous pouvez passer à la **section Installation de Gulp & gulp-imagemin**.

1. Tout d'abord, entrez `node --v` dans votre terminal pour vérifier si Node est installé. Si c'est le cas, vous obtiendrez quelque chose comme `v8.9.3`.
2. Si vous n'obtenez rien ou une erreur, téléchargez et [installez Node depuis ici](https://nodejs.org/en/download/). Cela peut prendre quelques minutes, donc soyez patient.
3. Une fois `Node.js` installé, vous aurez également `npm` installé car il est fourni avec `Node`. Vous pouvez vérifier la version de `npm` en tapant `npm -v` dans votre terminal. Vous devriez obtenir quelque chose comme `6.4.1`.
4. Ensuite, nous devons créer un fichier `package.json` pour notre projet. Nous faisons cela en utilisant la commande `npm init` (en savoir plus sur `[package.json](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/)` [ici](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/)). Vous serez invité à répondre à une série de questions, mais si vous ne voulez pas y répondre, vous n'avez pas à le faire, appuyez simplement sur Entrée jusqu'à ce que vous voyiez `Is this OK? (yes)`, puis appuyez sur `Entrée` une dernière fois et vous aurez terminé cette section.

![Image](https://cdn-media-1.freecodecamp.org/images/ra8Rx3jITz4p8TiUA32gdv9o0PmTqoLvrYd5)

Vous remarquerez que ce fichier a été créé dans un répertoire différent de celui avec lequel j'ai commencé. C'est pour que je puisse fournir un exemple, car j'ai déjà installé tout cela dans mon répertoire de projet actuel.

### Installation de Gulp & gulp-imagemin

Une fois `Node & npm` installés, nous pouvons maintenant installer `Gulp & gulp-imagemin` en suivant ces étapes :

1. Tout d'abord, tapez `npm install --save-dev gulp` dans votre terminal. Si vous voulez savoir ce que fait le flag `--save-dev`, consultez ce [post Stack Overflow](https://stackoverflow.com/questions/19223051/what-does-save-dev-mean-in-npm-install-grunt-save-dev).
2. Encore une fois, soyez patient car l'installation de Gulp peut prendre une minute, mais vous obtiendrez finalement quelque chose comme ceci : `gulp@4.0.0 added 318 packages from 218 contributors and audited 6376 packages in 49.362s found 0 vulnerabilities`
3. Vous pouvez vérifier votre version de Gulp en tapant `gulp -v` dans votre terminal et vous obtiendrez quelque chose de similaire à ceci : `[13:06:56] CLI version 2.0.1 [13:06:56] Local version 4.0.0`
4. Maintenant, installons `gulp-imagemin` en tapant `npm install --save-dev gulp-imagemin` et vous obtiendrez quelque chose comme ceci : `gulp-imagemin@5.0.3 added 232 packages from 97 contributors and audited 10669 packages in 39.103s found 0 vulnerabilities`
5. Et la dernière étape de cette section est de créer notre `gulpfile.js`. **Il est très important que votre fichier ait exactement ce nom et soit au niveau le plus externe de la structure de votre dossier de projet !**

### Écriture du code — Enfin le plaisir !

D'accord, maintenant que nous avons terminé l'installation de tout au bon endroit, ouvrons notre `gulpfile.js` et écrivons le code réel qui fera tout le travail.

1. Commencez par requérir `gulp` :
```javascript
const gulp = require('gulp');
```
Nous profitons essentiellement du système de modules de Node pour utiliser du code situé dans différents fichiers.

2. Maintenant, requérez `gulp-imagemin` :
```javascript
const imagemin = require('gulp-imagemin');
```
Encore une fois, nous profitons du système de modules pour utiliser ce code dans notre projet.

3. Maintenant, nous devons écrire la fonction qui fera tout le travail de compression des images :

```javascript
function imgSquash() {
  return gulp.src("./img/*")
    .pipe(imagemin())
    .pipe(gulp.dest("./minified/images"));
}
```

4. Si vous avez configuré votre répertoire en suivant le mien, le code ci-dessus fonctionnera. Si votre répertoire est différent, vous devrez modifier les lignes `.src & .dest` pour correspondre à l'emplacement de vos fichiers et à l'endroit où vous souhaitez qu'ils soient envoyés après avoir été minifiés.

5. `Gulp` fonctionne sur la base de tâches et nous pouvons lui en donner beaucoup pour le garder occupé. Une fois que nous avons défini la fonction réelle pour faire le travail, nous devons dire à `Gulp` quoi faire avec cette fonction :

```javascript
gulp.task("imgSquash", imgSquash);
```

6. Maintenant, nous voulons que `Gulp` surveille notre répertoire donné pour les changements (nouvelles images) et, lorsqu'il les détecte, nous voulons qu'il exécute automatiquement notre fonction `imgSquash`, minifie nos images et les envoie à la destination que nous avons définie. Nous y parvenons en définissant une autre tâche pour surveiller le répertoire :

```javascript
gulp.task("watch", () => {
  gulp.watch("./img/*", imgSquash);
});
```

7. La dernière étape de l'écriture du code consiste à définir la dernière tâche pour appeler nos tâches `imgSquash` et `watch` en succession :

```javascript
gulp.task("default", gulp.series("imgSquash", "watch"));
```

Ici, le mot "default" fait référence au mot `gulp` dans le terminal et `gulp.series` garantira que la fonction `imgSquash` s'exécute et que Gulp surveille immédiatement le répertoire pour les changements.

Voici à quoi devrait ressembler notre fichier terminé :

![Image](https://cdn-media-1.freecodecamp.org/images/PGzForat5pR93lI2H5W4hSfBJcPFojPVcoJ6)

Enregistrez ce fichier, ouvrez votre terminal et tapez `gulp` puis appuyez sur Entrée. Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/tSVYnl8tIMN0VIy8KoZbE81GXwtdPAIDl4Wi)

Comme vous pouvez le voir, chaque fois qu'un nouveau fichier était ajouté au répertoire de base, nos tâches se déclenchaient car Gulp surveillait et exécutait immédiatement notre fonction `imgSquash` pour minifier nos images. Lorsque vous avez terminé d'utiliser Gulp, vous pouvez appuyer sur `ctrl + c` dans votre terminal pour terminer le processus de surveillance.

Maintenant, vous pouvez commencer à utiliser vos images minifiées sur votre site web/application et profiter de ce gain de performance nouvellement trouvé !

### Conclusion

Gulp est un outil de build JavaScript très puissant qui peut aider à automatiser certains des aspects plus fastidieux, mais importants, de la construction de votre projet. En moins d'une heure de travail, vous avez pu minifier vos images, réduisant ainsi le temps de chargement et augmentant les performances de votre site web/application. C'est génial et vous devriez être fier de vous !

Ce n'est qu'une des nombreuses façons dont les outils de build comme Gulp peuvent vous aider. Il existe de nombreuses autres façons dont il peut aider (minification/concaténation de fichiers CSS/JS) et j'espère que vous explorerez certaines de ces options géniales.

Si vous avez aimé cet article, envisagez de faire un don en applaudissements car cela aide les autres à trouver mon travail. De plus, laissez un commentaire et faites-moi savoir sur quoi vous travaillez et comment Gulp vous aide à vous concentrer sur la construction.

Et enfin, cet article a été initialement publié sur [mon blog personnel](https://jonathansexton.me/blog). Pendant que vous y êtes, n'oubliez pas de vous inscrire à la **Newsletter**, que vous pouvez trouver en haut à droite de la page de mon blog. Je l'envoie mensuellement (je promets de ne pas spammer votre boîte de réception) et elle est remplie d'articles géniaux de tout le web que je pense que vous trouverez utiles.

Comme toujours, passez une journée géniale remplie d'amour, de bonheur et de codage !