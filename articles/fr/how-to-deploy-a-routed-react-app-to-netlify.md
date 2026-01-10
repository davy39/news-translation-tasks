---
title: Comment déployer une application React Router sur Netlify et corriger l'erreur
  "Page Not Found"
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-03T17:16:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-routed-react-app-to-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/netlify1-1-1.png
tags:
- name: Netlify
  slug: netlify
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment déployer une application React Router sur Netlify et corriger l'erreur
  "Page Not Found"
seo_desc: 'Have you ever experienced a “PAGE NOT FOUND” error when trying to access
  or refresh an application that uses React Router? Don''t worry, you''re not alone.

  In this article, you will learn how to deploy a React application that uses react-router
  without...'
---

Avez-vous déjà rencontré une erreur « PAGE NOT FOUND » en essayant d'accéder ou d'actualiser une application qui utilise React Router ? Ne vous inquiétez pas, vous n'êtes pas seul.

Dans cet article, vous apprendrez comment déployer une application React qui utilise react-router sans aucun problème.

## Le problème du déploiement des applications react-router

Pour vous assurer que vos utilisateurs sont satisfaits, vous donnerez généralement la priorité à l'expérience utilisateur lors de la création d'une application. Une bonne expérience utilisateur garantit que votre site Web ou votre application est facile à comprendre, facile à utiliser et facile à naviguer. 

Si vous avez déjà publié une application React sur Netlify qui utilise React Router, vous remarquerez probablement qu'en naviguant à travers vos routes, vous obtenez une erreur (**page not found**) lorsque vous actualisez votre navigateur. Cela crée une mauvaise expérience utilisateur. 

À travers cet article, vous apprendrez comment déployer une application React via la CLI Netlify et comment résoudre le problème de déploiement d'une application react-router.

## Qu'est-ce que Netlify ?

Selon [leur documentation](https://docs.netlify.com/), « Netlify est une plateforme tout-en-un pour automatiser les projets web modernes. » 

Netlify aide les développeurs web à construire et déployer leurs applications instantanément. Cet outil pratique remplace votre infrastructure d'hébergement et facilite votre pipeline d'intégration et de déploiement continus avec un seul workflow. Cela peut vraiment aider à augmenter votre productivité.

La CLI Netlify (Command Line Interface) vous aide à construire, tester et déployer facilement des applications directement depuis votre ligne de commande. 

Elle vous permet de :

1. démarrer un projet en quelques secondes
2. configurer le déploiement continu
3. exécuter un serveur de développement local que vous pouvez partager avec d'autres développeurs
4. déployer vos projets globalement

Vous pouvez vous inscrire pour un [compte Netlify](http://netlify.app) avec votre e-mail ou votre compte Git.  
Si vous n'avez pas de compte Git, vous pouvez créer un compte GitHub, GitLab ou Bitbucket en un rien de temps.

Voyons donc comment vous pouvez déployer votre application react-router en utilisant la CLI Netlify.

## Comment déployer votre application via la CLI Netlify

Pour commencer à utiliser la CLI de Netlify, vous devez avoir Node.js installé sur votre ordinateur. Vous pouvez vous rendre [ici](https://nodejs.org/en/download/) pour installer Node.js. 

Ensuite, vous pouvez commencer par installer la CLI Netlify en utilisant cette commande :

```js
npm install netlify-cli -g
```

Maintenant que vous avez installé la CLI de Netlify, vous pouvez déployer votre application sur Netlify. Avant cela, vous voudrez peut-être obtenir votre dossier build (j'expliquerai pourquoi ci-dessous). 

Pour obtenir votre dossier build, tapez la commande suivante :

```js
yarn run build
// ou
npm run build
```

Si vous ne vous êtes pas encore connecté à votre compte Netlify, vous pourriez voir une fenêtre contextuelle demandant l'autorisation d'accéder à Netlify.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify3.png)

Après avoir accédé à la CLI Netlify, vous recevrez une invite vous demandant ce que vous aimeriez faire. Sélectionnez l'option **create and configure a new site**. Vous pouvez utiliser vos touches fléchées pour naviguer entre les options.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify4.png)

Vous recevrez des invites pour sélectionner une équipe et un nom de site pour votre application. Vous pouvez soit saisir votre nom préféré pour votre application, soit utiliser le nom par défaut que vous pourrez modifier plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify5.1.png)

Vous recevrez une invite demandant quel répertoire publier. Saisissez **build** comme dossier de déploiement et appuyez sur Entrée pour déployer votre application React. Le dossier build qui a été généré au début de ce tutoriel servira de chemin de déploiement.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify7.png)

Si vous obtenez une réponse finale indiquant **« Si tout semble correct sur votre URL de brouillon, déployez-la sur l'URL de votre site principal avec le flag --prod »**, vous êtes sur la bonne voie. Vous recevrez l'URL de brouillon du site Web pour prévisualiser votre application.

Vous pouvez déployer sur le site principal en exécutant la commande suivante :

```js
netlify deploy --prod
```

Génial. Vous avez maintenant l'URL de votre site Web.

## Comment corriger l'erreur « Page Not Found »

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify1.png)
_page not found, erreur netlify_

Pour éviter l'erreur page-not-found chaque fois que vous essayez d'accéder à votre application ou que vous êtes sur d'autres routes, vous devez configurer des règles de redirection et de réécriture pour votre application react-router. 

La règle de redirection aidera votre application à éviter une erreur 404. Toutes les requêtes seront redirigées vers le /index.html au lieu de donner une erreur 404.

Pour configurer vos règles de redirection, vous devez créer un fichier sans extension nommé (_redirects) à l'intérieur de votre dossier public.

Incluez la commande suivante dans le fichier _redirects :

```_redirects
/*    /index.html  200
```

Pour voir les changements dans votre application, vous devrez la déployer à nouveau avec la commande suivante :

```js
netlify deploy
```

## Conclusion

Cet article a expliqué comment déployer une application react-router en utilisant la CLI de Netlify et comment corriger l'erreur page-not-found lors de l'accès à vos routes.

J'espère que vous avez trouvé cet article utile.

**Continuez à construire et continuez à déployer !**