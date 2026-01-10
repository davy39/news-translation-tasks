---
title: Git Push vers une branche distante – Comment pousser une branche locale vers
  Origin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-26T15:37:54.000Z'
originalURL: https://freecodecamp.org/news/git-push-to-remote-branch-how-to-push-a-local-branch-to-origin
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/git-push-to-remote-branch-article.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Push vers une branche distante – Comment pousser une branche locale
  vers Origin
seo_desc: 'By John Mosesman

  The basic command for pushing a local branch to a remote repository is git push.

  This command has a variety of options and parameters you can pass to it, and in
  this article you''ll learn the ones that you will use the most often.

  How...'
---

Par John Mosesman

La commande de base pour pousser une branche locale vers un dépôt distant est `git push`.

Cette commande possède une multitude d'options et de paramètres que vous pouvez lui passer, et dans cet article, vous apprendrez ceux que vous utiliserez le plus souvent.

## Comment pousser une branche Git locale vers Origin

Si vous exécutez la simple commande `git push`, Git choisira par défaut deux paramètres supplémentaires pour vous : le **remote repository** (dépôt distant) vers lequel pousser et la **branche** à pousser.

La forme générale de la commande est la suivante :

```
$ git push <remote> <branch>
```

Par défaut, Git choisit `origin` pour le remote et votre _branche actuelle_ comme branche à pousser.

Si votre branche actuelle est `main`, la commande `git push` fournira les deux paramètres par défaut—ce qui revient à exécuter `git push origin main`.

Dans l'exemple ci-dessous, le remote `origin` est un dépôt GitHub, et la branche actuelle est `main` :

```
(main)$ git remote -v 
origin  git@github.com:johnmosesman/burner-repo.git (fetch)
origin  git@github.com:johnmosesman/burner-repo.git (push)

(main)$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 274 bytes | 274.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:johnmosesman/burner-repo.git
   b7f661f..ab77dd6  main -> main

```

D'après la sortie, vous pouvez voir que la branche locale `main` a été poussée vers la branche distante `main` :

```
To github.com:johnmosesman/burner-repo.git
   b7f661f..ab77dd6  main -> main

```

## Comment forcer le push d'une branche dans Git

Normalement, vous pousserez vers une branche et ajouterez à son historique de commits.

Mais il y a des moments où vous devez **écraser** (overwrite) de force l'historique d'une branche.

Il y a plusieurs raisons pour lesquelles vous pourriez vouloir faire cela.

La première raison est de corriger une erreur—bien qu'il soit probablement préférable de simplement faire un nouveau commit [annulant les changements.](https://git-scm.com/docs/git-revert)

Le second scénario, plus courant, se produit après une action comme un **[rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)**—ce qui modifie l'historique des commits :

> En interne, Git réalise [un rebase] en créant de nouveaux commits et en les appliquant à la base spécifiée. Il est très important de comprendre que même si la branche semble identique, elle est composée de commits entièrement nouveaux.

Un rebase crée des _commits entièrement nouveaux._ 

Cela signifie que si vous essayez de pousser une branche qui a été rebasée localement—mais pas sur le remote—le dépôt distant reconnaîtra que l'historique des commits a changé, et il vous empêchera de pousser jusqu'à ce que vous régliez les différences :

```
(my-feature)$ git push
To github.com:johnmosesman/burner-repo.git
 ! [rejected]        my-feature -> my-feature (non-fast-forward)
error: failed to push some refs to 'git@github.com:johnmosesman/burner-repo.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

Vous pourriez faire un `git pull` ici pour fusionner les différences, mais si vous voulez _vraiment_ écraser le dépôt distant, vous pouvez ajouter le flag `--force` à votre push :

```
(my-feature)$ git push --force origin my-feature
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 184 bytes | 184.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To github.com:johnmosesman/burner-repo.git
 + edb64e2...52f54da my-feature -> my-feature (forced update)

```

(**Note :** vous pouvez utiliser `-f` comme raccourci au lieu de `--force`.)

Un push forcé est une action destructive—ne l'utilisez que lorsque vous êtes certain que c'est ce que vous voulez faire.

### Force push avec lease

Parfois, vous voudrez peut-être forcer le push—mais seulement si personne d'autre n'a contribué à la branche.

Si quelqu'un d'autre contribue à votre branche et pousse ses modifications vers le remote—et que vous faites un push forcé par-dessus—vous écraserez ses modifications.

Pour éviter ce scénario, vous pouvez utiliser l'option `--force-with-lease`.

Encore une fois [d'après la documentation :](https://git-scm.com/docs/git-push)

> --force-with-lease seul, sans spécifier les détails, protégera toutes les références distantes qui vont être mises à jour en exigeant que leur valeur actuelle soit la même que la branche de suivi à distance que nous avons pour elles.

En gros, vous dites à Git de mettre à jour de force cette branche _seulement si_ elle est identique à la dernière fois que vous l'avez vue.

Si vous collaborez avec d'autres personnes sur votre branche, il serait bon d'éviter d'utiliser `--force` ou du moins d'utiliser `--force-with-lease` pour éviter de perdre les modifications apportées par d'autres collaborateurs.

## Comment pousser vers une branche portant un nom différent sur Git

Vous pousserez généralement votre branche locale vers une branche distante du même nom—mais pas toujours.

Pour pousser vers une branche d'un nom différent, il vous suffit de spécifier _la branche que vous voulez pousser_ et le nom de la branche vers laquelle vous voulez _pousser_, séparés par un deux-points (`:`) .

Par exemple, si vous voulez pousser une branche nommée `some-branch` vers `my-feature` :

```
(some-branch)$ git push origin some-branch:my-feature
Total 0 (delta 0), reused 0 (delta 0)
To github.com:johnmosesman/burner-repo.git
 + 728f0df...8bf04ea some-branch -> my-feature
```

### Comment pousser toutes les branches locales vers le remote

Vous n'aurez pas souvent besoin de pousser toutes les branches de votre local, mais si vous le faites, vous pouvez ajouter le flag `--all` :

```
(main)$ git branch
* main
  my-feature

(main)$ git push --all
...
To github.com:johnmosesman/burner-repo.git
   b7f661f..6e36148  main -> main
 * [new branch]      my-feature -> my-feature

```

## Conclusion

La commande `git push` est une commande que vous utiliserez souvent, et il existe une multitude d'options qui peuvent être utilisées avec elle. Je vous encourage à [lire la documentation](https://git-scm.com/docs/git-push) pour découvrir des options et des raccourcis utiles.

Si vous avez aimé ce tutoriel, je parle aussi de sujets comme celui-ci [sur Twitter](https://twitter.com/johnmosesman), et j'écris à leur sujet [sur mon site.](https://johnmosesman.com/)