---
title: Ce qu'il ne faut pas enregistrer dans un dépôt Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-14T22:18:40.000Z'
originalURL: https://freecodecamp.org/news/what-not-to-save-into-a-git-repository-29779ee94b96
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca75a740569d1a4ca769d.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: tips
  slug: tips
seo_title: Ce qu'il ne faut pas enregistrer dans un dépôt Git
seo_desc: 'You should not commit these four types of files into your Git repository.


  Files that don’t belong to the project

  Files that are automatically generated

  Libraries (depends on the situation)

  Credentials


  Files that don’t belong to the project

  Files li...'
---

Vous ne devriez pas commiter ces quatre types de fichiers dans votre dépôt Git.

1. Les fichiers qui n'appartiennent pas au projet
2. Les fichiers générés automatiquement
3. Les bibliothèques (selon la situation)
4. Les informations d'identification

### Les fichiers qui n'appartiennent pas au projet

Les fichiers comme `.DS_Store` (pour Mac OS), `Thumds.db` (pour Windows), `.vscode` (pour les éditeurs de code) n'ont rien à voir avec votre projet.

Ils ne devraient pas être ajoutés au dépôt.

### Les fichiers générés automatiquement

Cela inclut les fichiers provenant de préprocesseurs (comme Sass vers CSS). Vous n'ajoutez pas le CSS. Vous ajoutez les fichiers Sass.

Si vous utilisez des compilateurs JavaScript comme Webpack ou Rollup, vous n'ajoutez pas le fichier JavaScript généré. Vous ajoutez le code que vous écrivez.

### Les bibliothèques

Si vous n'utilisez pas de gestionnaire de paquets, vous devriez ajouter vos bibliothèques. Cela est dû au fait que si vous voulez télécharger la bibliothèque, vous devez :

1. Rechercher la bibliothèque sur Google
2. Aller sur le site web
3. Trouver le lien
4. Télécharger la bibliothèque
5. La placer dans votre projet

Ce processus est fastidieux. Si votre code a besoin de la bibliothèque pour fonctionner, vous devriez ajouter la bibliothèque.

En revanche, si vous utilisez un gestionnaire de paquets, vous ne devriez pas ajouter une bibliothèque car vous pouvez l'installer avec une seule commande comme `npm install`.

### Les informations d'identification

Vous ne devriez pas stocker d'informations d'identification comme des noms d'utilisateur, des mots de passe, des clés API et des secrets API.

Si quelqu'un d'autre vole vos informations d'identification, il peut en faire de mauvaises choses. J'ai presque perdu entre 40 000 $ et 60 000 $ parce qu'un ami a accidentellement exposé mes informations d'identification Amazon. Heureusement, le montant a été annulé.

Si vous ne voulez pas vous retrouver dans des situations délicates comme moi, alors ne stockez pas vos informations d'identification dans un dépôt Git.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une quelconque manière ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=What%20not%20to%20save%20into%20a%20Git%20repository%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/what-not-to-save-into-a-git-repo/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/what-not-to-save-into-a-git-repo).
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.