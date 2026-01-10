---
title: Comment configurer une application OAuth GitHub
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-10-27T21:31:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-github-oauth-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-george-becker-333837--1-.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: GitHub
  slug: github
- name: oauth
  slug: oauth
seo_title: Comment configurer une application OAuth GitHub
seo_desc: "GitHub is an incredibly useful OAuth provider, especially if you are building\
  \ an application targeted toward developers. \nIn this article, we will give you\
  \ a quick rundown of how to set up a GitHub OAuth application.\nCreate Your Application\n\
  Begin by ..."
---

GitHub est un fournisseur OAuth incroyablement utile, surtout si vous développez une application destinée aux développeurs. 

Dans cet article, nous allons vous donner un aperçu rapide de la manière de configurer une application OAuth GitHub.

## Créer votre application

Commencez par naviguer vers vos paramètres GitHub (assurez-vous d'être connecté !). Faites défiler jusqu'en bas de la barre latérale et cliquez sur "Paramètres du développeur".

Cela vous mènera à la page des applications :

![Vue des applications OAuth GitHub, montrant une application hacktoberfest et mattermost qui ont été précédemment autorisées.](https://www.freecodecamp.org/news/content/images/2022/10/image-230.png)
_Vous pourriez voir certaines applications que vous avez précédemment autorisées._

Cliquez sur le bouton "Nouvelle application OAuth" pour créer une nouvelle application.

![La page de nouvelle application OAuth, montrant les champs de formulaire pour le nom de l'application, l'URL de la page d'accueil, la description de l'application et l'URL de rappel d'autorisation.](https://www.freecodecamp.org/news/content/images/2022/10/image-232.png)

Remplissez le formulaire et cliquez sur "Enregistrer l'application". Cela créera votre application et vous mènera à la page des paramètres.

![La page des paramètres de l'application, qui montre les mêmes champs de formulaire que le formulaire précédent, avec des options supplémentaires pour transférer la propriété, révoquer les jetons utilisateur, générer des secrets clients et télécharger un logo.](https://www.freecodecamp.org/news/content/images/2022/10/image-233.png)

Pour les applications OAuth, vous aurez besoin de l'ID client. Vous devrez également générer un secret client. Cliquez sur "Générer un nouveau secret client" pour ce faire.

![Le nouveau secret client (obfusqué pour la sécurité dans cette image)](https://www.freecodecamp.org/news/content/images/2022/10/image-234.png)

Assurez-vous de sauvegarder ce secret dans un endroit sécurisé, car vous ne pourrez plus le consulter par la suite.

## Utiliser votre nouvelle application

Maintenant que vous avez un ID client et un secret, vous pouvez utiliser votre application OAuth dans votre projet. 

Si vous souhaitez apprendre comment faire, [le programme de freeCodeCamp peut vous l'enseigner](https://www.freecodecamp.org/learn/quality-assurance/#advanced-node-and-express). 

Bon codage !