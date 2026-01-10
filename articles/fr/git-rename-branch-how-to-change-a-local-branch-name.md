---
title: Git Renommer une Branche – Comment Changer le Nom d'une Branche Locale
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-03T15:42:12.000Z'
originalURL: https://freecodecamp.org/news/git-rename-branch-how-to-change-a-local-branch-name
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/mila-tovar-NTiW908Uc1A-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: how-to
  slug: how-to
- name: version control
  slug: version-control
seo_title: Git Renommer une Branche – Comment Changer le Nom d'une Branche Locale
seo_desc: "As you are building out a project, there might be times where you need\
  \ to rename a local branch. But how do you do that in Git?\nIn this article, I will\
  \ provide you with two methods for renaming  local branches in Git. \nHow to Rename\
  \ a Branch in Git –..."
---

Lors de la construction d'un projet, il peut arriver que vous deviez renommer une branche locale. Mais comment faire cela dans Git ?

Dans cet article, je vais vous fournir deux méthodes pour renommer des branches locales dans Git.

## Comment Renommer une Branche dans Git – Méthode #1

### Étape 1 : Assurez-vous d'être dans le répertoire racine de votre projet

Vous devrez d'abord ouvrir votre terminal, puis utiliser `cd` (changer de répertoire) pour accéder à la racine de votre projet.

Par exemple, voici à quoi ressemblerait la commande si vous étiez dans le répertoire personnel et que vous souhaitiez accéder au projet situé sur le Bureau.

```
cd Bureau/nom-du-projet
```

Voici un exemple de changement de répertoire vers un projet nommé `Happy_Messages_Bot`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.30.01-PM.png)

### Étape 2 : Allez à la branche que vous souhaitez renommer

Nous pouvons utiliser la commande `git checkout` pour basculer vers une autre branche.

```
git checkout nom-de-la-branche
```

Dans cet exemple, je souhaite basculer vers la branche `test-branch` que j'ai créée.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.39.57-PM.png)

### Étape 3 : Utilisez le drapeau `-m` pour changer le nom de la branche

Voici à quoi ressemblerait la commande pour changer le nom de la branche :

```
git branch -m nouveau-nom-de-branche
```

Dans cet exemple, je souhaite changer le nom de ma branche de `test-branch` à `test-branch2`.

```
git branch -m test-branch2
```

Vous pouvez utiliser `git status` pour voir votre nouveau nom de branche.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.52.02-PM.png)

## Comment Renommer une Branche dans Git – Méthode #2

Nous pouvons renommer la branche locale en une seule commande sans avoir à utiliser `git checkout`.

### Étape 1 : Assurez-vous d'être dans la branche master/main

Pour vérifier si vous êtes dans la branche master/main, exécutez `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.02.20-PM.png)

Si vous n'êtes pas dans la branche master/main, vous devrez exécuter `git checkout master` ou `git checkout main`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.05.28-PM.png)

### Étape 2 : Utilisez le drapeau `-m` pour renommer la branche

Vous pouvez utiliser cette syntaxe pour renommer l'ancienne branche en quelque chose de nouveau.

```
git branch -m ancienne-branche nouvelle-branche
```

Voici à quoi cela ressemblerait pour renommer `test-branch` en `test-branch2`.

```
git branch -m test-branch test-branch2
```

Pour voir votre nouveau nom de branche, vous pouvez exécuter `git branch` qui listera toutes vos branches.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.15.52-PM.png)

Ce sont deux méthodes pour renommer des branches locales dans Git.