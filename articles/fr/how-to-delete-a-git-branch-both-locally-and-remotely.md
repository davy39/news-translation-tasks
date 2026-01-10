---
title: Comment supprimer une branche Git localement et à distance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T19:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e53740569d1a4ca3c89.jpg
tags:
- name: Git
  slug: git
seo_title: Comment supprimer une branche Git localement et à distance
seo_desc: 'In most cases, it is simple to delete a Git branch. You''ll learn how to
  delete a Git brach locally and remotely in this article.

  TL;DR version

  // delete branch locally

  git branch -d localBranchName


  // delete branch remotely

  git push origin --delete ...'
---

Dans la plupart des cas, il est simple de supprimer une branche Git. Vous apprendrez comment supprimer une branche Git localement et à distance dans cet article.

### Version TL;DR

```bash
// supprimer la branche localement
git branch -d nomDeLaBrancheLocale

// supprimer la branche à distance
git push origin --delete nomDeLaBrancheDistante

```

## Quand supprimer les branches

Il est courant pour un dépôt Git d'avoir différentes branches. Elles sont un excellent moyen de travailler sur différentes fonctionnalités et corrections tout en isolant le nouveau code de la base de code principale. 

Les dépôts ont souvent une branche `main` pour la base de code principale et les développeurs créent d'autres branches pour travailler sur différentes fonctionnalités.

Une fois le travail terminé sur une fonctionnalité, il est souvent recommandé de supprimer la branche.

## Supprimer une branche LOCALMENT

Git ne vous permettra pas de supprimer la branche sur laquelle vous vous trouvez actuellement, vous devez donc vous assurer de basculer vers une branche que vous ne supprimez PAS. Par exemple : `git checkout main`

Supprimez une branche avec `git branch -d <branche>`.

Par exemple : `git branch -d fix/authentication`

L'option `-d` supprimera la branche uniquement si elle a déjà été poussée et fusionnée avec la branche distante. Utilisez `-D` à la place si vous voulez forcer la suppression de la branche, même si elle n'a pas encore été poussée ou fusionnée.

La branche est maintenant supprimée localement.

## Supprimer une branche À DISTANCE

Voici la commande pour supprimer une branche à distance : `git push <remote> --delete <branche>`.

Par exemple : `git push origin --delete fix/authentication`

La branche est maintenant supprimée à distance.

Vous pouvez également utiliser cette commande plus courte pour supprimer une branche à distance : `git push <remote> :<branche>`

Par exemple : `git push origin :fix/authentication`

Si vous obtenez l'erreur ci-dessous, cela peut signifier que quelqu'un d'autre a déjà supprimé la branche.

```bash
error: unable to push to unqualified destination: remoteBranchName The destination refspec neither matches an existing ref on the remote nor begins with refs/, and we are unable to guess a prefix based on the source ref. error: failed to push some refs to 'git@repository_name'

```

 Essayez de synchroniser votre liste de branches en utilisant :

```
git fetch -p

```

Le flag `-p` signifie "élaguer". Après la récupération, les branches qui n'existent plus sur le dépôt distant seront supprimées.

Si vous avez trouvé ce tutoriel utile, notre organisation à but non lucratif propose plus de 11 000 tutoriels sans fioritures comme celui-ci. Tous gratuits. Parlez-en à vos amis. 😉