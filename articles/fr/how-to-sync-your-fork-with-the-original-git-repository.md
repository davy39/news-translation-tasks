---
title: Comment synchroniser votre fork avec le dépôt Git original
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-11T18:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b23740569d1a4ca29ed.jpg
tags:
- name: Git
  slug: git
seo_title: Comment synchroniser votre fork avec le dépôt Git original
seo_desc: 'By Johan Rin

  You''re contributing to an open-source project, and you noticed that your fork is
  out of sync with the original repository. How can you correct that?

  TL;DR version

  # Add a new remote upstream repository

  git remote add upstream https://git...'
---

Par Johan Rin

Vous contribuez à un projet open-source et vous avez remarqué que votre fork n'est plus synchronisé avec le dépôt original. Comment corriger cela ?

## Version TL;DR

```bash
# Ajouter un nouveau dépôt distant upstream
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

# Synchroniser votre fork
git fetch upstream
git checkout master
git merge upstream/master
```

## Ajouter un nouveau dépôt distant upstream

Vous avez cloné votre fork sur votre ordinateur et commencé à travailler sur votre problème.

Saviez-vous que votre fork est un orphelin ? Si vous listez les dépôts distants configurés, vous ne verrez que votre fork comme origin :

```bash
git remote -v
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```

Aucun signe de parents ! Où est le dépôt original ?

Nous devons configurer cette information pour rétablir la relation familiale en ajoutant un nouveau dépôt distant upstream :

```shell
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

Vous avez sauvé la famille ! Vous pouvez maintenant voir à la fois le dépôt original et le fork :

```bash
git remote -v
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

## Synchroniser votre fork

Tout est maintenant configuré. Vous pouvez synchroniser votre fork avec seulement 2 commandes.

Assurez-vous d'être à la racine de votre projet et également dans la branche master. Sinon, vous pouvez basculer vers la branche master :

```bash
git checkout master
Switched to branch 'master'
```

Maintenant, vous devez récupérer les changements depuis le dépôt original :

```bash
git fetch upstream
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 7 (delta 5), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), 1.72 Kio | 160.00 Kio/s, done.
From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY
   909ef5a..0b228a8  master     -> upstream/master
```

Et fusionner les changements dans votre branche master :

```bash
git merge upstream/master
Updating 909ef5a..0b228a8
Fast-forward
 node.js/WorkingWithItems/batch-get.js               | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/batch-write.js             | 95 +++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------
 node.js/WorkingWithItems/delete-item.js             | 37 ++++++++++++++++++------------------
 node.js/WorkingWithItems/get-item.js                | 31 +++++++++++++++++--------------
 node.js/WorkingWithItems/put-item-conditional.js    | 51 +++++++++++++++++++++++++-------------------------
 node.js/WorkingWithItems/put-item.js                | 49 ++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/transact-get.js            | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/transact-write.js          | 79 ++++++++++++++++++++++++++++++++++++++++-------------------------------------
 node.js/WorkingWithItems/update-item-conditional.js | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/update-item.js             | 47 ++++++++++++++++++++++++----------------------
 10 files changed, 282 insertions(+), 260 deletions(-)
```

C'est tout ! Votre fork est maintenant à jour.

Des questions ? N'hésitez pas à me contacter sur [Twitter](https://twitter.com/johanrin) !