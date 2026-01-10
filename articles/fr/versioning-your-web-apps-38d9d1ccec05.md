---
title: Comment utiliser le contrôle de version pour maintenir vos applications web
  à jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-08T03:30:25.000Z'
originalURL: https://freecodecamp.org/news/versioning-your-web-apps-38d9d1ccec05
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wS8MJ0MGrw6ZpVVQmPPHdA.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Comment utiliser le contrôle de version pour maintenir vos applications
  web à jour
seo_desc: 'By Kamlesh Chandnani

  Version Control helps you keep track of which users are using what version of your
  app.

  With native apps, you have to maintain the versioning of your app with each build.
  Then only you will be able to release the new version of y...'
---

Par Kamlesh Chandnani

Le contrôle de version vous aide à suivre quels utilisateurs utilisent quelle version de votre application.

Avec les applications natives, vous devez maintenir la gestion des versions de votre application à chaque build. Ce n'est qu'ainsi que vous pourrez publier la nouvelle version de votre application sur l'App Store/Play Store.

Mais comment allez-vous maintenir les versions de vos applications web ?

Histoire !

Dans les années 90, il y avait des langages côté serveur comme PHP, Java et JSP, qui permettaient à tous vos utilisateurs d'obtenir toujours la dernière version de votre application web.

Mais maintenant, les applications web ont atteint un nouveau niveau. Tout est côté client ! Nous pouvons donc tirer parti des concepts comme le pré-cache, le chargement à la demande, le rendu de données significatives en même temps, et ainsi de suite.

Mais cela peut aussi introduire des problèmes si l'utilisateur accède toujours à la copie mise en cache de notre application web.

Imaginez une entreprise SaaS dont les utilisateurs finaux ne savent pas comment utiliser les applications web/les applications web de nouvelle génération/les PWAs de la bonne manière.

Lorsque cela concerne les applications web modernes comme les PWAs, vous ne pouvez pas garantir que tous vos utilisateurs utilisent la dernière copie du code de votre application.

Supposons que vous avez déployé votre application web pour la première fois, et que les utilisateurs ont commencé à l'utiliser. L'application est mise en cache après la première visite, et par la suite, à chaque visite répétée, l'utilisateur obtiendra la copie mise en cache de votre application jusqu'à ce que la nouvelle version du code de votre application soit disponible. Tout fonctionne sans problème.

Mais maintenant, supposons qu'après un certain temps, lors de la prochaine itération, vous avez ajouté une nouvelle fonctionnalité à votre application web existante et déployé le nouveau morceau de code/bundles.

***BOOM***

Comment garantir que vos utilisateurs utilisent la dernière version de votre application web ?

Comment allez-vous identifier combien d'utilisateurs utilisent encore l'ancienne version de votre application ?

Toutes ces questions vous encouragent à maintenir et à stocker la version actuelle de votre application web, afin que chaque fois que les utilisateurs utilisent votre application, la version de l'application soit également stockée dans le serveur de base de données.

Mais le mystère du "Comment" maintenir les versions reste non résolu !

[Git Revision Webpack Plugin](https://www.npmjs.com/package/git-revision-webpack-plugin) vient à votre secours si vous utilisez webpack pour bundler votre code.

C'est un plugin [webpack](http://webpack.github.io/) simple qui génère les fichiers `VERSION` et `COMMITHASH` pendant les builds basés sur un dépôt [Git](https://www.git-scm.com/) local.

### Utilisation

1. Ajoutez une étiquette à votre commit.

```
syntax: git tag <tag-name>git tag v1.0
```

2. Ajoutez ce qui suit à votre fichier de configuration webpack :

```
const GitRevisionPlugin = require("git-revision-webpack-plugin");
```

```
const gitRevisionPlugin = new GitRevisionPlugin();
```

3. Ajoutez [DefinePlugin](http://webpack.github.io/docs/list-of-plugins.html#defineplugin) de webpack dans votre tableau de plugins.

```
const plugins = [.....new webpack.DefinePlugin({APP_VERSION_INFO: {  VERSION: gitRevisionPlugin.version(), //retourne la sortie de la commande git describe  COMMITHASH: gitRevisionPlugin.commithash(), // retourne le hash du dernier commit  BRANCH: gitRevisionPlugin.branch() // retourne le nom de la branche à partir de laquelle le build a été exécuté};})...]
```

4. Utilisez maintenant `APP_VERSION_INFO` n'importe où dans votre application, car il sera disponible globalement.

```
console.log('Vérifiez la version de l\'application ', APP_VERSION_INFO);
```

**_Avez-vous aimé cette histoire ?_**  
_Recommandez (en cliquant sur le bouton 💜) ou partagez cette histoire pour que d'autres personnes puissent la lire !_