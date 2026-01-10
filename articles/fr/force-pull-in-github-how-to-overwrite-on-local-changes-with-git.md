---
title: Force Pull dans GitHub – Comment écraser les modifications locales avec Git
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-16T17:32:02.000Z'
originalURL: https://freecodecamp.org/news/force-pull-in-github-how-to-overwrite-on-local-changes-with-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/jannis-brandt-4mHaSX8zvJI-unsplash.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Force Pull dans GitHub – Comment écraser les modifications locales avec
  Git
seo_desc: 'While working on a project as part of a team, you may get an error message
  telling you that you can''t execute git pull on your repository because you have
  local changes.

  Why does this happen?

  This error usually occurs when several people are introduc...'
---

Lorsqu'on travaille sur un projet en équipe, il est possible de recevoir un message d'erreur indiquant qu'il est impossible d'exécuter `git pull` sur votre dépôt en raison de modifications locales.

Pourquoi cela se produit-il ?

Cette erreur survient généralement lorsque plusieurs personnes apportent des mises à jour au même fichier. Essentiellement, il existe des fichiers identiques avec des contenus différents.

Il peut être nécessaire de forcer `git pull` et d'écraser vos modifications locales avec celles du dépôt distant.

Par défaut, Git n'écrasera pas les modifications. Pour des raisons de sécurité, il vous informe que vous avez des modifications locales qui seront écrasées par les nouvelles modifications introduites et validées dans le dépôt Git.

Dans cet article, vous apprendrez à écraser les modifications locales avec les dernières versions du dépôt distant.

Commençons !

## Comment forcer `git pull` pour écraser les modifications locales dans Git

Gardez à l'esprit que lorsque vous exécutez les commandes dans les sections suivantes, vous perdrez vos modifications locales non validées sur votre système. Toutes les modifications seront remplacées par celles du dépôt.

### Récupérer toutes les modifications distantes

Tout d'abord, récupérez toutes les modifications les plus récentes du dépôt distant.

Pour ce faire, vous devez exécuter la commande `git fetch` comme suit :

```bash
git fetch --all
```

La commande ci-dessus téléchargera les dernières mises à jour du dépôt distant et synchronisera votre dépôt local avec le dépôt distant.

### Réinitialiser votre branche locale

Ensuite, exécutez la commande `git reset --hard`.

La syntaxe générale de cette commande ressemble à ceci :

```bash
git reset --hard remote/nom-de-la-branche-distante
```

Ainsi, si le `nom-de-la-branche-distante` est appelé `main`, vous écrivez ce qui suit :

```bash
git reset --hard origin/main
```

Cette commande supprimera et écrasera toutes vos modifications locales non validées et définira l'état de la branche à l'état du dépôt distant que vous venez de récupérer.

L'option `--hard` effectue une réinitialisation complète sur la branche `origin/main`.

Vous perdrez toutes les modifications locales non validées suivies par Git. Les fichiers et répertoires locaux non suivis par Git ne sont pas affectés.

### Supprimer les fichiers et dossiers non suivis

Pour supprimer tous les fichiers et répertoires non suivis par Git de votre répertoire de travail, vous pouvez utiliser la commande `git clean` :

```bash
git clean -fd
```

Gardez à l'esprit que cette opération est irréversible !

### Tirer

Enfin, exécutez la commande `git pull` :

```bash
git pull
```

## Comment forcer `git pull` et sauvegarder les modifications locales dans Git

Si vous souhaitez être prudent, vous pouvez vouloir sauvegarder les modifications locales non validées, car vous les perdrez après avoir exécuté la commande `git reset --hard`.

Vous pouvez utiliser la commande `git stash` pour sauvegarder les modifications locales non validées pour une utilisation ultérieure :

```bash
git stash
```

Cette commande sauvegardera les modifications locales dans un stash, et vous pourrez les appliquer plus tard si nécessaire après les étapes `fetch`, `reset` et `clean` mentionnées dans la section précédente.

Pour réappliquer les modifications stashées à une date ultérieure, utilisez la commande `git stash pop` :

```bash
git stash pop
```

## Conclusion

Dans cet article, vous avez appris comment forcer `git pull` pour écraser les modifications locales dans Git et comment sauvegarder les modifications locales dans un stash si nécessaire.

Merci d'avoir lu, et bon codage !