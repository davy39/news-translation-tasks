---
title: Ces astuces NPM feront de vous un pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T21:18:00.000Z'
originalURL: https://freecodecamp.org/news/10-npm-tricks-that-will-make-you-a-pro-a945982afb25
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_RA4XguCJLF-m4a7bwrC5FQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: 'tech '
  slug: tech
seo_title: Ces astuces NPM feront de vous un pro
seo_desc: 'By Carl-Johan Kihl

  After using NPM for almost 8 years, I’ve learned things along the way that I wish
  I knew when I started. Let’s call them tricks, things that drastically improved
  my way of working with NPM. Today I want to share my top 10 tricks wi...'
---

Par Carl-Johan Kihl

Après avoir utilisé NPM pendant près de 8 ans, j'ai appris des choses en cours de route que j'aurais aimé connaître lorsque j'ai commencé. Appelons-les des astuces, des choses qui ont considérablement amélioré ma façon de travailler avec NPM. Aujourd'hui, je veux partager avec vous mes 10 meilleures astuces.

### 1. Gagnez du temps. ⏳ Utilisez des raccourcis

C'est l'une des fonctionnalités les plus utiles mais pas si bien documentées. Un raccourci pour une commande peut sembler une chose triviale, mais la vérité est que vous écrivrez **30 à 60 %** de code en moins. Vous gagnerez du temps que vous pourrez consacrer à quelque chose de significatif, comme boire une tasse de café supplémentaire ☕️ ?

Au lieu de `npm **install**` <package>  
écrivez `npm **i**` <package>.

Au lieu de `npm **install**` **--save** <package>   
écrivez `npm **i -S**` <package>.

Au lieu de `npm **install**` **--save-dev** <package>   
écrivez `npm **i -D**` <package>.

Au lieu de `npm **install**` **--global** <package>   
écrivez `npm **i -G**` <package>.

? Bonus raccourci ! Vous voulez impressionner vos collègues ? ? Le voici...

Au lieu de `npm **test**`  
écrivez `npm **t**`.

### 2. Installez plusieurs packages en une seule commande

Pourquoi écrire plusieurs lignes lorsque vous pouvez en écrire une ? ? Si vous connaissez vos packages par cœur, l'option la plus rapide est de les installer tous en une seule ligne, mais soyez prudent ! Un package mal orthographié et toute la commande échouera. Si vous n'êtes pas sûr des noms, installez-les un par un.

```
npm i -S react redux react-redux 
```

### 3. Installez des packages à partir de différentes sources

Par défaut, lors de l'exécution de `npm-install`, NPM installera la dernière version du _registre npm_ ([https://registry.npmjs.org](https://registry.npmjs.org/))

Mais il y a plus ! NPM peut installer des packages à partir d'autres sources, comme une URL ou un fichier tarball.

Lors de la création de vos propres packages ou de pull-requests pour des packages existants, cette fonctionnalité est puissante. Par exemple, si vous avez votre propre fork de [Redux](https://redux.js.org/), vous pouvez installer votre package directement depuis votre fork. _(Remplacez_ `_username_` _par votre nom d'utilisateur sur GitHub.)_

```
npm i https://github.com/username/redux
```

Encore mieux, si vous utilisez un dépôt GitHub, vous pouvez utiliser ce raccourci :

`npm i **username/redux**`

Il y a plus ! Vous pouvez également installer un package à partir d'une branche spécifique. Utile pour tester une future version. Ajoutez simplement `#` suivi du nom de la branche à la fin.

```
npm i username/redux#branche
```

? Bonus raccourci ! Vous n'utilisez pas GitHub ? Pas de problème, il existe des raccourcis pour **BitBucket** et **GitLab** également :

```
npm i bitbucket:username/myrepository
npm i gitlab:username/myrepository
```

### 4. Lier des packages

Parfois, vous souhaitez travailler sur un projet et développer ses packages en même temps. Commiter et pousser votre package vers un dépôt distant pour chaque changement que vous souhaitez essayer est fastidieux ! ? Au lieu de cela, vous pouvez utiliser une fonctionnalité appelée _lien de package_.

Le _lien de package_ fonctionne en créant un lien symbolique dans votre dossier node_modules qui pointe vers le dépôt local de votre package. De cette manière, vous pouvez modifier les packages localement et les changements seront instantanément disponibles dans le projet qui les utilise.

La manière la plus simple de comprendre le _lien de package_ est de l'essayer !  
Disons que nous avons un projet appelé `myproject` et un package appelé `mypackage`. Nous voulons que `mypackage` soit une dépendance de `myproject`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6UqU6s3lTXURBArAseZ-fQ.png)
_Un projet et un package._

Allez dans le dossier `mypackage` et écrivez

```
npm link
```

Bien ! Maintenant, allez dans le dossier `myproject` et écrivez

`npm link mypackage`

Terminé ! Jetez un coup d'œil à la structure du dossier

![Image](https://cdn-media-1.freecodecamp.org/images/1*N_dNE4jtEeBcWnGgE7g5xw.png)

Comme vous pouvez le voir, `myproject/node_modules/mypackage` est maintenant un lien symbolique vers le dossier `mypackage` ! Maintenant, vous pouvez continuer à développer `mypackage` et toutes les modifications que vous apportez seront instantanément disponibles dans `myproject`.

### 5. La commande npx

Il existe de nombreux outils de script sur NPM que vous utiliserez probablement mais qui ne feront pas partie de votre bundle d'exécution. Grunt, gulp, react-create-app, react-native-cli et mocha n'en sont que quelques-uns.

Avant NPM 5.x, vous deviez installer ces outils soit en tant que packages globaux, soit en tant que devDependencies. Cela prenait du temps, non seulement pour l'installation, mais aussi pour maintenir tous vos outils pour plusieurs projets. De plus, la plupart des outils ne seront utilisés qu'une ou deux fois.

Ici, le binaire NPX vient à la rescousse et nous fait gagner beaucoup de travail ! Par exemple, pour démarrer un nouveau projet react, vous pouvez simplement écrire :

`npx create-react-app my-new-project`

La dernière version de [create-react-app](https://github.com/facebook/create-react-app) sera téléchargée et exécutée immédiatement. Plus besoin d'installer et de maintenir des outils en tant que packages globaux.

### 6. Surveillez et nettoyez votre projet

![Image](https://cdn-media-1.freecodecamp.org/images/1*5o6_Xpf35l3TivVl9YFSFw.jpeg)

Il est important de comprendre ce qui se passe sous le capot lors de l'installation de packages afin de résoudre les problèmes et de rendre l'arborescence des dépendances et la taille finale du bundle aussi petites que possible.

Tout d'abord, nous avons besoin d'un bon aperçu de l'arborescence des dépendances et des versions de packages qui ont été installées. Utilisez la commande `npm list`. Ajoutez le flag `--depth=0` pour lister uniquement les packages de premier niveau et ajoutez `-g` pour lister vos packages globaux.

`npm list
npm list --depth=0 -g`

![Image](https://cdn-media-1.freecodecamp.org/images/1*W6rh263TrzZReldwNC7TCg.png)

NPM est bon pour s'auto-maintenir et aplatir l'arborescence des dépendances à la volée, mais il est toujours bon de **dedupe** votre projet avant de le publier. Cela pourrait supprimer quelques packages pour vous.

`npm dedupe`

C'est aussi une excellente idée d'avoir un bon aperçu de vos packages obsolètes et manquants. Il est difficile de ne pas aimer cette vue pour ses colonnes bien organisées et le schéma de couleurs de Noël ??

`npm outdated`

![Image](https://cdn-media-1.freecodecamp.org/images/1*XY6mBtNPP5LcMS7Ee1IxYQ.png)
_La liste des packages obsolètes est vraiment belle !_

Si vous obtenez beaucoup de lignes rouges, vous devez exécuter `npm update` pour mettre à jour vos packages vers la dernière version possible selon votre package.json, ce qui est également indiqué dans la colonne **wanted**

`npm update`

Super ! Maintenant, si vous exécutez `npm outdated` à nouveau, toutes les lignes rouges devraient avoir disparu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hJU3FI-AlLNzyBz9i_Byrg.png)

Si vous utilisez le caret `^` devant vos versions dans package.json, les versions majeures ne seront pas mises à jour (d'où les lignes jaunes). C'est bien, car il peut y avoir des changements cassants lors de la mise à jour vers une nouvelle version majeure.

Si vous souhaitez toujours tout mettre à jour vers la dernière version, vous pouvez utiliser l'outil `npm-update-all`. C'est aussi simple que d'exécuter cette commande dans votre dossier de projet.

`npx npm-update-all`

Cool ! Maintenant, vous avez la dernière version de toutes vos dépendances. Votre package.json est également mis à jour. ⚠️ Attention aux changements cassants ⚠️

![Image](https://cdn-media-1.freecodecamp.org/images/1*9A29MdExsP7IjULGhZU3PA.png)
_Comme vous pouvez le voir, npm-update-all mettra à jour tous vos packages vers la dernière version._

### 7. Allez à la page d'accueil d'un package

Besoin de vérifier la documentation d'un package ? Pourquoi vous donner la peine de passer au navigateur et de commencer à googler lorsque tout ce dont vous avez besoin est le terminal ? ?

Ouvrez le dépôt pour un package dans le navigateur

`npm repo <package>`

Ouvrez la page d'accueil

`npm home <package>`

Ouvrez la documentation

`npm docs <package>`

### 8. Utilisez les scripts NPM

J'adore les scripts npm ! Au lieu d'utiliser des exécuteurs de tâches comme Gulp et Grunt pour automatiser les tâches répétitives, vous pouvez, dans la plupart des cas, utiliser des scripts npm à la place pour plusieurs raisons :

➡ Moins de dev-dependencies ou de dépendances globales à maintenir.  
➡ Pas de nouveaux outils à apprendre pour les contributeurs et les membres de l'équipe  
➡ Moins de code et de configuration.

Tout d'abord, vous avez des scripts prédéfinis comme `start, install, test, prepublish` qui ont des significations spéciales dans NPM. Vous pouvez lire comment ils peuvent être utilisés dans mon [tutoriel précédent](https://itnext.io/step-by-step-building-and-publishing-an-npm-typescript-package-44fe7164964c) où nous construisons un package npm à partir de zéro.

Vous pouvez également créer vos propres scripts personnalisés. Voici un exemple de script qui formatera votre code dans le dossier `src` avec [ESLint](https://eslint.org/) :

package.json :

```
"scripts": {
  "test": "jest",
  "format": "eslint src --fix"
}
```

Maintenant, vous pouvez exécuter `npm run format` et [ESLint](https://eslint.org/) fera son travail.

Vous pouvez faire beaucoup de choses avec les scripts npm comme exécuter des commandes shell et enchaîner des scripts les uns après les autres. Consultez [npm-scripts](https://docs.npmjs.com/misc/scripts) pour une compréhension plus approfondie de cette fonctionnalité puissante.

### 9. Exécuter des scripts NPM dans vsCode

Parfois, j'ai **30** scripts npm dans mon package.json (sans blague). ? Heureusement, si vous utilisez [Visual Studio Code](https://code.visualstudio.com/), vous pouvez lister tous vos scripts npm dans l'explorateur et exécuter vos scripts d'un simple clic de bouton ! Assurez-vous que ce paramètre est activé :

`npm.enableScriptExplorer: true`

![Image](https://cdn-media-1.freecodecamp.org/images/1*QJt2B9fgYJ8FXSwQh3IzBg.png)
_Exécutez vos scripts d'un simple clic de bouton ! VSCode prend en charge la liste des scripts de plusieurs packages en même temps._

### 10. Définissez vos valeurs par défaut

Lors de la création d'un nouveau projet, vous exécuterez `npm init` et vous serez interrogé sur votre projet. Pour gagner du temps, vous écrivrez probablement `npm init -y` pour remplir le package.json avec des valeurs par défaut.

Mais quelles sont exactement vos valeurs par défaut ? ? J'aime en définir certaines moi-même pour gagner encore plus de temps ! ?

npm config set init.author.name "Carl-Johan (C-J) Kihl"  
npm config set init.author.email "carljohan.kihl@mail.com"

### Résumé

Ce sont mes conseils pour NPM pour l'instant ! Si vous avez d'autres astuces et conseils que vous souhaitez partager, ajoutez un commentaire ci-dessous ! ?

? Bonus raccourci !  
Imaginez, c'est vendredi soir et vous êtes sur le point de finaliser un nouveau projet, mais vous êtes trop fatigué pour écrire `npm dedupe`. ?

Pas de problème ! Économisez trois lettres en écrivant :

`npm **ddp**`

Merci d'avoir lu.