---
title: 'Erreur : failed to push some refs to – Comment corriger dans Git'
date: '2022-07-28T20:04:11.000Z'
author: Ihechikara Abba
authorURL: https://www.freecodecamp.org/news/author/Ihechikara/
originalURL: https://freecodecamp.org/news/error-failed-to-push-some-refs-to-how-to-fix-in-git
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/roman-synkevych-wX2L8L-fGeA-unsplash.jpg
tags:
- name: error
  slug: error
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_desc: 'When collaborating with other developers using Git, you might encounter
  the error: failed to push some refs to [remote repo] error.

  This error mainly occurs when you attempt to push your local changes to GitHub while
  the local repository (repo) has n...'
---


Lors de la collaboration avec d'autres développeurs utilisant Git, vous pouvez rencontrer l'erreur `error: failed to push some refs to [remote repo]`.

<!-- more -->

Cette erreur se produit principalement lorsque vous tentez de pusher vos modifications locales vers GitHub alors que le dépôt (repo) local n'a pas encore été mis à jour avec les modifications apportées au dépôt distant.

Ainsi, Git essaie de vous dire de mettre à jour le dépôt local avec les modifications actuelles du distant avant de pusher vos propres modifications. Cela est nécessaire pour ne pas écraser les changements effectués par d'autres.

Nous allons aborder deux façons possibles de corriger cette erreur dans les sections qui suivent.

## Comment corriger l'erreur `error: failed to push some refs to` dans Git

Nous pouvons corriger l'erreur `error: failed to push some refs to [remote repo]` dans Git en utilisant les commandes `git pull origin [branch]` ou `git pull --rebase origin [branch]`. Dans la plupart des cas, cette dernière permet de corriger l'erreur.

Voyons comment utiliser les commandes ci-dessus.

### Comment corriger l'erreur `error: failed to push some refs to` dans Git en utilisant `git pull`

Effectuer un pull signifie « fetcher » (récupérer) les nouvelles modifications apportées au dépôt distant et les fusionner (merge) avec le dépôt local.

Une fois la fusion terminée, vous pouvez ensuite pusher vos propres modifications de code vers GitHub.

Dans notre cas, nous essayons de nous débarrasser de l'erreur `error: failed to push some refs to [remote repo]` en effectuant un pull.

Voici comment faire :

```
git pull origin main
```

Si vous travaillez sur une branche différente, vous devrez remplacer `main` dans l'exemple ci-dessus par le nom de votre branche.

Gardez à l'esprit qu'il y a des chances d'échec lors de l'utilisation de cette commande pour synchroniser vos dépôts distant et local afin de supprimer l'erreur. Si la requête réussit, continuez et exécutez la commande ci-dessous pour pusher vos propres modifications :

```
git push -u origin main
```

Si l'erreur persiste, vous recevrez un message indiquant : `fatal: refusing to merge unrelated histories`. Dans ce cas, utilisez la solution de la section suivante.

### Comment corriger l'erreur `error: failed to push some refs to` dans Git en utilisant `git pull --rebase`

La commande `git pull --rebase` est utile dans les situations où votre branche locale a un commit de retard sur la branche distante.

Pour corriger l'erreur, exécutez les commandes suivantes :

```
git pull --rebase origin main

git push -u origin main
```

Si la première commande ci-dessus s'exécute avec succès, vous devriez recevoir une réponse indiquant : `Successfully rebased and updated refs/heads/main`.

La deuxième commande pushe l'état actuel de votre dépôt local vers la branche distante.

## Résumé

Dans cet article, nous avons parlé de l'erreur `error: failed to push some refs to [remote repo]`.

Cette erreur se produit lorsque vous tentez de pusher vos modifications locales vers le dépôt distant sans avoir mis à jour votre dépôt local avec les nouvelles modifications apportées au dépôt distant.

Nous avons examiné deux commandes que vous pouvez utiliser pour corriger l'erreur : `git pull origin [branch]` et `git pull --rebase origin [branch]`.

J'espère que cela vous aidera à corriger l'erreur.

Bon code !