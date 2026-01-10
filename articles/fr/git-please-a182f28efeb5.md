---
title: Git S'il Vous Plaît
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-04T17:33:15.000Z'
originalURL: https://freecodecamp.org/news/git-please-a182f28efeb5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PhSXjkYS9MTmoNwlPIdQpQ.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Git S'il Vous Plaît
seo_desc: 'By Buddy Reno

  As the size of a dev team grows, so does the likelihood of someone doing a force
  push and overwriting someone else’s code.

  Here’s what a force push looks like in Git:

  $ git push --force origin master# `--force` can also  be written as `...'
---

Par Buddy Reno

À mesure que la taille d'une équipe de développement grandit, la probabilité que quelqu'un effectue un force push et écrase le code de quelqu'un d'autre augmente également.

Voici à quoi ressemble un force push dans Git :

```
$ git push --force origin master# `--force` peut aussi s'écrire `-f`
```

Cette commande peut causer toutes sortes de problèmes. Elle indique essentiellement à Git que _je ne me soucie pas de ce qui se trouve dans origin/master. Ce que j'ai est correct. Écraser-le._

Alors, que se passe-t-il si un collègue a commis des changements sur une branche que vous n'avez pas encore tirée dans votre propre dépôt ? Elle est écrasée, et votre collègue doit potentiellement refaire son travail (ou ressusciter un commit ou deux s'il l'a encore localement).

Mais tout ce gâchis peut être facilement évité avec un petit changement dans la façon dont vous utilisez le drapeau `force`. Au lieu d'utiliser `--force`, utilisez `--force-with-lease`.

```
$ git push --force-with-lease origin master
```

Pour résumer la [documentation](https://git-scm.com/docs/git-push#git-push---force-with-lease) de Git, l'utilisation de `force-with-lease` indique à Git de vérifier si le dépôt distant est le même que celui que vous essayez de pousser. Si ce n'est pas le cas, Git générera une erreur au lieu d'écraser aveuglément le dépôt distant. Cela vous évitera d'écraser accidentellement un travail que vous ne souhaitez pas écraser.

Je déteste taper `force-with-lease` cependant — surtout parce que je suis habitué à taper le raccourci `-f` pour forcer le push. Heureusement, Git permet d'ajouter des alias pour rendre cela plus rapide. J'aime penser que je demande à Git s'il est d'accord pour forcer le push, donc j'ai aliasé `push --force-with-lease` en `git please`.

```
$ git please origin master
```

Vous pouvez ajouter un alias dans Git en tapant ceci dans votre terminal :

```
git config --global alias.please 'push --force-with-lease'
```

Ou vous pouvez ouvrir votre fichier `~/.gitconfig` et ajouter manuellement l'alias :

```
[alias]	co = checkout	ci = commit	please = push --force-with-lease
```

#### Il y a toujours un piège...

Il est possible de tromper force with lease cependant. Lorsque vous utilisez `git pull` pour obtenir des mises à jour de l'origine, cela exécute deux commandes à la fois. Git exécute un `fetch` pour tirer la référence de tous les changements. Ensuite, il exécute un `merge` pour fusionner les changements que vous venez de tirer dans votre branche actuelle.

Si vous ne faites qu'un `fetch` pour obtenir les dernières mises à jour, vous ne mettrez à jour que vos références — sans fusionner réellement les changements dans votre copie de travail. Ensuite, si vous forcez le push avec lease, Git regardera ces références et pensera que la copie locale est à jour avec le dépôt distant, alors qu'en réalité ce n'est pas encore le cas. Cela trompera Git en écrasant les changements sur le dépôt distant avec votre copie locale, sans avoir fusionné les changements.

La manière la plus simple d'éviter ce problème est d'utiliser toujours `git pull` pour `fetch` et `merge` en même temps. Je n'ai pas rencontré de cas où j'ai dû `fetch` et `merge` manuellement, donc je ne peux pas parler de ces circonstances. L'utilisation de `pull` a toujours fonctionné pour moi.

J'espère que vous trouverez `git please` utile et que, par conséquent, vous n'aurez jamais à récupérer d'un cauchemar de force-push.