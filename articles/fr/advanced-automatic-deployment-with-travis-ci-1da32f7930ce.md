---
title: Comment configurer le déploiement automatique avancé avec Travis CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T11:58:53.000Z'
originalURL: https://freecodecamp.org/news/advanced-automatic-deployment-with-travis-ci-1da32f7930ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zuVag9ipdXYb-A4ojT_FxQ.png
tags:
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer le déploiement automatique avancé avec Travis CI
seo_desc: 'By Amir Off

  This post is a sequel to my previous Advanced Web Development and Deployment Workflow
  tutorial. In that tutorial, I showed how I automated my development and deployment
  workflow. A lot has changed since then due to the rapid development o...'
---

Par Amir Off

Cet article est la suite de mon précédent tutoriel [**Advanced Web Development and Deployment Workflow**](https://codeburst.io/web-development-with-ide-version-control-and-deployment-1eaabb5a256). Dans ce tutoriel, j'ai montré comment j'ai automatisé mon flux de développement et de déploiement. Beaucoup de choses ont changé depuis, en raison du développement rapide des outils et technologies web — et bien sûr de mon besoin d'améliorer mon flux de travail en tant que développeur web.

### Mon Cas d'Utilisation

J'utilise un service d'hébergement mutualisé pour mon portfolio personnel [website](https://www.amiroff.me/) et la plupart du code est composé d'actifs statiques front-end :

![Image](https://cdn-media-1.freecodecamp.org/images/1*29ynOaYNgPeFTqw6qAx1Lw.png)
_Structure des fichiers de mon site web_

Dans le [passé](https://codeburst.io/web-development-with-ide-version-control-and-deployment-1eaabb5a256), je devais exécuter une tâche Gulp.js pour minifier, uglifier et traiter tout le code source. Il le sort dans un dossier bundle avec le fichier index.html prêt à être déployé sur mon service d'hébergement via FTP.

Pour automatiser le processus, j'ai utilisé [DeployBot](http://deploybot.com/). C'est un service qui permet d'utiliser vos dépôts existants et de déployer vers plusieurs emplacements comme FTP, SFTP, Amazon, etc.

Là où DeployBot ne répond pas à mes besoins, c'est qu'il fonctionne uniquement comme un tunnel qui déploie mon dépôt GitHub chaque fois qu'un changement est commis dans le dépôt. Cela signifiait que je devais télécharger mon code bundlé vers une branche séparée — je l'ai appelée « deployment » dans mon cas — et il téléchargeait tous les fichiers de cette branche vers le serveur d'hébergement via FTP.

J'ai vu cela comme une mauvaise pratique et une solution de confort temporaire. Mon code sur GitHub devrait être un code « source » et non un ensemble de fichiers JavaScript et CSS minifiés et uglifiés et d'autres fichiers traités.

### La Solution

Pour éliminer le problème que j'avais avec DeployBot, j'ai dû l'abandonner pour Travis CI — un service d'intégration et de livraison continues qui s'intègre avec GitHub. De cette façon, j'ai pu supprimer la branche « deployment » que j'avais dans mon dépôt et laisser Travis CI faire tout le travail d'exécution des tâches Gulp.js pour moi et de déploiement ultérieur vers mon serveur d'hébergement via FTP. Tout ce que j'avais à faire était de pousser mon code source et Travis CI ferait le reste. Plus besoin d'exécuter les tâches Gulp.js manuellement, puis de basculer vers la branche « deployment » et de la pousser manuellement vers GitHub.

Dans le code ci-dessous, je définis le fichier de script « **.travis.yml** » requis pour que Travis CI s'exécute :

```yml
// Définition de la langue de l'environnement
language: node_js

// Utilisation de la dernière version de Node.js
node_js:
- node

// Script pour installer les dépendances
before_script:
- npm install -g --silent

// Le script de build réel pour Gulp.js
script:
- gulp build --prod

// Déploiement vers le serveur d'hébergement via FTP
after_script:
- gulp deploy --user $FTP_USER --password $FTP_PASSWORD
```

💡 _À la ligne 18, les identifiants FTP sont extraits de Travis CI_

C'est une excellente fonctionnalité car elle me permet de définir des variables d'environnement protégées, les identifiants de connexion FTP « **$FTP_USER** » et « **$FTP_PASSWORD** » dans ce cas. Ces variables sont chiffrées et intégrées dans le fichier de script « **.travis.yml** » à l'exécution. De cette façon, je peux commiter mon code source vers GitHub sans exposer de données sensibles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C9yaH-9TXV_a1JiIsXX0AA.png)
_Définition des variables d'environnement sur la page des paramètres de build de Travis CI_

Pour qu'elles fonctionnent, j'ai dû utiliser un package appelé [**vinyl-ftp**](https://www.npmjs.com/package/vinyl-ftp). Il est décrit comme,

> Un adaptateur vinyl pour FTP. Prend en charge les transferts parallèles, les transferts conditionnels, les fichiers tamponnés ou en flux, et plus encore. Souvent, il performe mieux que votre client FTP de bureau préféré.

```js
const ftp = require('vinyl-ftp');
const minimist = require('minimist');
const args = minimist(process.argv.slice(2));

gulp.task('deploy', () => {
    const remotePath = '/amiroffme/';
    const conn = ftp.create({
        host: 'ftp.amiroff.me',
        user: args.user,
        password: args.password
    });
    console.log('Connexion FTP réussie !');
    gulp.src('build/**/*.*')
        .pipe(conn.dest(remotePath));
});
```

💡 _Aux lignes 9 et 10, la tâche de déploiement analyse l'utilisateur et le mot de passe à partir des options d'argument que le script Travis CI exécute :_

```
$ gulp deploy --user $FTP_USER --password $FTP_PASSWORD
```

J'ai dû installer un autre package npm populaire appelé [**minimist**](https://www.npmjs.com/package/minimist) pour pouvoir analyser les arguments « user » et « password » comme dans le CLI ci-dessus.

En plus d'installer les deux packages npm précédents, j'ai dû refactoriser mon fichier de tâches Gulp.js pour me permettre d'exécuter une build de développement afin que je puisse travailler sur le code localement. Le déploiement continu en production est génial, mais je voulais toujours pouvoir exécuter mon code localement et avoir un environnement de développement réel avec une build de développement réelle. 😊

```js
// Tâche de build principale
gulp.task('build', ['html', 'images', 'sass', 'js', (args.prod ? 'production' : 'development')], () => {
    // Afficher les informations de build
    console.log(packageFile.name + ' "' + packageFile.description + '" v' + packageFile.version);
});

// Ne s'exécute que pour la build de production
gulp.task('production', () => {
    console.log('Ceci est une build de production');
    console.log('Veuillez exécuter le script suivant pour le déploiement :');
    console.log('gulp deploy --user $FTP_USER --password $FTP_PASSWORD');
});

// Ne s'exécute que pour la build de développement
gulp.task('development', () => {
    browsersync(browserSyncConfig);
    console.log('Ceci est une build de développement');
    console.log('Les changements de fichiers seront surveillés et déclencheront un rechargement de la page');
    gulp.watch(html.watch, ['html', browsersync.reload]);
    gulp.watch(images.src, ['images', browsersync.reload]);
    gulp.watch(css.watch, ['sass', browsersync.reload]);
    gulp.watch(js.src, ['js', browsersync.reload]);
});
```

💡 _À la ligne 2, je vérifie les arguments de build puis exécute la tâche de build en conséquence._

Si la tâche détecte l'argument « **prod** » comme dans le script de build Travis CI :

```
$ gulp build --prod
```

elle ignore la tâche **development** qui est conçue pour les builds de développement locaux et exécute la tâche **production** à la place.

L'exécution de la build sans l'argument « **prod** » déclenchera la tâche **development** qui surveille les changements de fichiers et recharge la page — très similaire à tout environnement de développement.

```
$ gulp build
```

### Conclusion

Plus besoin de basculer entre les branches et de copier et pousser manuellement les actifs bundlés vers GitHub. Je peux simplement travailler localement et pousser vers GitHub et Travis CI s'occupe du reste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G5EkaZP-_t63dNFyzjZNeg.png)
_Historique des builds de mon Travis CI_

J'espère que vous avez apprécié la lecture ! Veuillez [**suivre**](https://medium.com/@amiroffme) et **partager** pour plus de contenu tech 🤖💖