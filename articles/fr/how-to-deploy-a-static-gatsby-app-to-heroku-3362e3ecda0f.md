---
title: Comment déployer une application Gatsby statique sur Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T19:51:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-static-gatsby-app-to-heroku-3362e3ecda0f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XjHB-v-6y23f0TdUEqEZog.png
tags:
- name: deployment
  slug: deployment
- name: GatsbyJS
  slug: gatsbyjs
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: 'tech '
  slug: tech
seo_title: Comment déployer une application Gatsby statique sur Heroku
seo_desc: 'By Kristin Baumann

  This tutorials explains how to set up the deployment of a static GatsbyJS project
  with Heroku and Github. You will learn how to create a staging and production environment
  for your application so you’re ready for safe continuous de...'
---

Par Kristin Baumann

Ce tutoriel explique comment configurer le déploiement d'un projet GatsbyJS statique avec Heroku et Github. Vous apprendrez à créer un environnement de staging et de production pour votre application afin d'être prêt pour un déploiement continu sécurisé.

Après avoir terminé ce tutoriel, …

* 💡 vous serez en mesure de **construire et déployer une application Gatsby statique**.
* ✨ vous serez en mesure de **déclencher des déploiements automatiques** vers votre environnement de **staging** en poussant vers votre dépôt git. (Vous pouvez examiner l'application de staging et, si elle est appropriée, la promouvoir vers votre site de **production**.)

**Conditions préalables :**

* Votre projet sera basé sur [GatsbyJS](https://www.gatsbyjs.org/) (un générateur de site statique). Vous n'avez pas besoin de connaissances en codage avec Gatsby ou React, mais vous devez avoir [Node](https://nodejs.org/en/download/) et [GatsbyJS](https://www.gatsbyjs.org/docs/) installés.
* Vous aurez besoin d'un compte [Github](https://github.com/) et [Heroku](https://heroku.com/) (tous deux disponibles gratuitement). Git doit être configuré sur votre machine.

### 1.) Créer un nouveau projet Gatsby

Tout d'abord, vous avez besoin d'un nouveau projet Gatsby.

* Vous pouvez créer un nouveau projet dans le dossier `test-project` en exécutant la commande suivante dans votre console :

```
gatsby new test-project https://github.com/gatsbyjs/gatsby-starter-hello-world
```

Cela crée les fichiers essentiels pour une application Gatsby statique à partir d'un pack de démarrage. Vous pouvez démarrer le serveur de développement localement en allant dans le répertoire du projet avec `cd test-project` puis en exécutant `gatsby develop`. Votre application est maintenant disponible sur `localhost:8000`.

### 2.) Configurer un dépôt git

Avec le projet en cours d'exécution localement, vous pouvez maintenant configurer un dépôt git pour votre projet Gatsby.

* Connectez-vous à Github et créez un nouveau dépôt.
* Initialisez un dépôt git dans votre projet avec :

```
git init
```

* Connectez votre dépôt git local à votre dépôt distant avec :

```
git remote add origin <remoteURL>
```

* Faites votre premier commit du projet Gatsby avec :

```
git add .
git commit -m "Initial commit"
git push origin master
```

Les modifications de votre projet Gatsby sont maintenant suivies avec Github, ce qui fournira le déclencheur pour démarrer un déploiement plus tard.

### 3.) Configurer les applications Heroku

Ensuite, vous pouvez configurer les environnements de déploiement continu sur Heroku.

* Créez un nouveau pipeline appelé `test-project` dans le tableau de bord de l'application Heroku
* Dans ce pipeline, créez une nouvelle application pour l'environnement de staging appelée `test-project-staging` et une nouvelle application pour la production appelée `test-project-prod`
* Connectez le pipeline (et non chaque application individuellement) avec votre dépôt Github créé précédemment
* Activez les déploiements automatiques à partir de la branche master pour l'application de staging (mais pas pour l'application de production !)
* Définissez les buildpacks pour les deux applications sur :

```
"heroku/nodejs"
```

```
"https://github.com/heroku/heroku-buildpack-static"
```

Ces buildpacks sont des scripts qui s'exécutent lorsque votre application est déployée et sont spécifiques à votre projet Gatsby statique. Vous pouvez configurer le buildpack statique dans l'étape suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/qNtbliSCD21VxlTI5LE69J5KajixsfdmMSth)
_Votre configuration Heroku incluant un environnement de staging et de production_

### 4.) Préparer votre projet Gatsby pour le déploiement sur Heroku

* Après que votre code soit copié sur Heroku et que les dépendances nécessaires soient installées, le projet Gatsby doit être construit et stocké dans le dossier statique /public. Ajoutez donc un script de construction dans votre fichier `package.json` :

```
{     // ...
```

```
     "scripts": {         // ...
```

```
         "heroku-postbuild": "gatsby build"
```

```
     },
```

```
     // ...}
```

* Créez un fichier appelé `app.json` dans le répertoire racine de votre projet. Ce fichier inclut des informations générales nécessaires pour exécuter une application sur Heroku. Dans notre cas, nous indiquons à nouveau l'utilisation des deux buildpacks :

```
{
```

```
    "buildpacks": [
```

```
     { "url": "heroku/nodejs" },
```

```
     { "url": "https://github.com/heroku/heroku-buildpack-static" }
```

```
    ]
```

```
}
```

* Créez un fichier appelé `static.json` dans le répertoire racine de votre projet. Le fichier `static.json` est utilisé pour la configuration du buildpack statique. Vous pouvez voir plus d'options de configuration [ici](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-static). Dans ce cas, nous définissons uniquement le dossier de notre application construite :

```
{
```

```
    "root": "public/"
```

```
}
```

* (Facultatif) Le déploiement de Heroku échouera si vous avez un fichier `package-lock.json` ainsi qu'un fichier `yarn.lock` dans votre répertoire de projet. Si c'est le cas, choisissez-en un. Par exemple, supprimez le fichier `package-lock.json` si vous utilisez yarn.

### 5.) Tester votre configuration

Félicitations, vous avez presque terminé ! ✨

Vous pouvez maintenant tester votre configuration en validant les modifications de la dernière étape sur Github :

```
git add .
git commit -m "Préparation du déploiement Heroku de l'application Gatsby"
git push origin master
```

Cela devrait déclencher une construction et un déploiement automatiques de votre projet Gatsby vers l'environnement de staging. Vous pouvez ensuite examiner l'application de staging et, si elle est appropriée, la promouvoir vers votre site de production.

_Merci d'avoir lu cet article ! N'hésitez pas à poser des questions ou à laisser des commentaires et suivez-moi sur [Twitter](https://twitter.com/kristin_baumann) pour plus de publications liées à JavaScript et React._