---
title: Comment ignorer des fichiers de votre package npm
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-22T16:02:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-ignore-files-from-your-npm-package-4724e6d9575d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F6R34rqTupBQxrVe7GS4fw.jpeg
tags:
- name: npm
  slug: npm
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment ignorer des fichiers de votre package npm
seo_desc: 'You can decide what files people get when they download your npm package
  in three ways:


  With the .gitignore file

  With the .npmignore file

  With the files property


  We’ll look at each method and discuss which methods you should (or shouldn’t) be
  using...'
---

Vous pouvez décider quels fichiers les gens obtiennent lorsqu'ils téléchargent votre package npm de trois manières :

1. Avec le fichier `.gitignore`
2. Avec le fichier `.npmignore`
3. Avec la propriété `files`

Nous examinerons chaque méthode et discuterons des méthodes que vous devriez (ou ne devriez pas) utiliser.

### Exclure des fichiers avec gitignore

Tout d'abord, npm vérifiera votre dépôt pour un fichier `.gitignore`. Si un fichier `.gitignore` existe, npm ignorera les fichiers selon ce qui est listé dans le fichier `.gitignore`.

C'est la manière la plus courante pour les auteurs de packages d'empêcher les gens de télécharger des fichiers supplémentaires.

Prenons un exemple simple. Supposons que vous avez la structure de répertoire suivante.

```
- nom-du-projet/   |- index.js   |- package.json   |- node_modules/
```

Supposons que vous ne voulez pas que les gens téléchargent le dossier `node_modules`. Vous ne voulez pas non plus sauvegarder le `node_modules` dans le dépôt Git.

Ce que vous ferez, c'est créer un fichier `.gitignore`.

```
# .gitignore node_modules
```

Dans ce cas, Git et npm ignorent tous les deux le dossier `node_modules`.

### Blacklister des fichiers avec npmignore

Une deuxième méthode consiste à blacklister des fichiers avec un fichier `.npmignore`. Le fichier `.npmignore` fonctionne de la même manière qu'un fichier `.gitignore`. Si un fichier est listé dans le fichier `.npmignore`, le fichier sera exclu du package.

**Note importante :** Si vous avez un fichier `.npmignore`, npm utilisera le fichier `.npmignore`. **npm ignorera complètement le fichier `.gitignore`**. (De nombreux développeurs croient à tort que npm utilisera à la fois les fichiers `.npmignore` et `.gitignore`. Ne faites pas la même erreur !)

Vous pouvez utiliser cette méthode si vous souhaitez exclure des fichiers du package mais les conserver dans le dépôt Git.

Prenons un autre exemple. Supposons que vous avez écrit des tests pour votre package et que vous les avez tous placés dans un dossier `tests`. Voici votre structure de répertoire :

```
- nom-du-projet/  |- index.js |- package.json |- node_modules/ |- tests/
```

Vous souhaitez exclure `node_modules` de votre dépôt Git et de votre package.

Vous souhaitez inclure `tests` dans votre dépôt Git, mais l'exclure du package.

Si vous optez pour la méthode du fichier `npmignore`, vous pouvez écrire ceci dans vos fichiers `.gitignore` et `.npmignore` :

```
# .gitignore node_modules
```

```
# .npmignore node_modules tests
```

### Whitelister des fichiers avec la propriété files

Une troisième méthode consiste à **whitelister** les fichiers que vous souhaitez **inclure** dans le fichier `package.json`, sous la propriété `files`.

Note : npm donnera la priorité à cette méthode par rapport aux autres méthodes mentionnées ci-dessus. C'est la méthode la plus simple pour limiter les fichiers que les autres téléchargent.

Cette approche est assez simple. Ce dont vous avez besoin, c'est de créer une propriété `files` dans le fichier `package.json`. Ensuite, fournissez une liste des fichiers que vous souhaitez inclure.

Voici un exemple :

```
{   "files": [      "index.js"   ] }
```

Note : Certains fichiers, comme `package.json`, sont [toujours inclus](https://docs.npmjs.com/files/package.json) dans un package. Vous n'avez pas besoin d'écrire ces fichiers dans la propriété `files`.

### Quelle méthode utiliser ?

Les trois méthodes fonctionnent. Choisissez celle avec laquelle vous êtes le plus à l'aise. Pour les projets simples, la méthode du fichier `.gitignore` devrait suffire.

Si votre projet est plus avancé, vous pourriez vouloir blacklister des fichiers avec `.npmignore` ou whitelister des fichiers avec la propriété `files`. Choisissez-en une. Il n'y a pas besoin des deux.

### Un conseil rapide

Vous pouvez utiliser `npm pack` pour générer un package. Ce package inclut les fichiers que les autres obtiendront.

```
npm pack
```

Essayez-le !

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=How%20to%20ignore%20files%20from%20your%20npm%20package%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/ignoring-files-from-npm-package/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/ignoring-files-from-npm-package/)_._  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.