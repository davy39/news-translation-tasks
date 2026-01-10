---
title: Git Switch Branch – Comment changer de branche dans Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-19T23:37:29.000Z'
originalURL: https://freecodecamp.org/news/git-switch-branch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60770740776bd507fe31f89c.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Switch Branch – Comment changer de branche dans Git
seo_desc: 'By John Mosesman

  Switching branches is something you''ll need to do often in Git.

  To do this, you can use the git checkout command.

  How to create a new branch in Git

  To create a new branch in Git, you use the git checkout command and pass the -b
  flag ...'
---

Par John Mosesman

Changer de branche est une opération que vous devrez effectuer souvent dans Git.

Pour cela, vous pouvez utiliser la commande `git checkout`.

## Comment créer une nouvelle branche dans Git

Pour créer une nouvelle branche dans Git, vous utilisez la commande `git checkout` avec l'option `-b` suivie d'un nom.

Cela créera une nouvelle branche à partir de la branche actuelle. L'historique de la nouvelle branche commencerà à l'endroit actuel de la branche dont vous vous êtes "détaché".

En supposant que vous êtes actuellement sur une branche appelée `master` :

```
(master)$ git checkout -b ma-fonctionnalite
Switched to a new branch 'ma-fonctionnalite'
(ma-fonctionnalite)$
```

Ici, vous pouvez voir une nouvelle branche créée appelée `ma-fonctionnalite` qui a été créée à partir de `master`.

## Comment basculer vers une branche existante dans Git

Pour basculer vers une branche existante, vous pouvez utiliser à nouveau `git checkout` (sans l'option `-b`) et passer le nom de la branche vers laquelle vous souhaitez basculer :

```
(ma-fonctionnalite)$ git checkout master
Switched to branch 'master'
(master)$

```

Il existe également un raccourci pratique pour revenir à la branche précédente sur laquelle vous étiez en passant `-` à `git checkout` au lieu d'un nom de branche :

```
(ma-fonctionnalite)$ git checkout -
Switched to branch 'master'
(master)$ git checkout -
Switched to branch 'ma-fonctionnalite'
(ma-fonctionnalite)$
```

## Comment vérifier un commit spécifique

Pour vérifier ou basculer vers un commit spécifique, vous pouvez également utiliser `git checkout` et passer le [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) du commit au lieu d'un nom de branche.

Après tout, les branches ne sont vraiment que des pointeurs et des traceurs de commits spécifiques dans l'historique Git.

### Comment trouver un SHA de commit

Une façon de trouver le SHA d'un commit est de consulter le journal Git.

Vous pouvez consulter le journal en utilisant la commande `git log` :

```
(ma-fonctionnalite)$ git log
commit 94ab1fe28727b7f8b683a0084e00a9ec808d6d39 (HEAD -> ma-fonctionnalite, master)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Apr 12 10:31:11 2021 -0500

    Ce est le deuxième message de commit.

commit 035a128d2e66eb9fe3032036b3415e60c728f692 (blah)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Apr 12 10:31:05 2021 -0500

    Ce est le premier message de commit.

```

Sur la première ligne de chaque commit après le mot `commit` se trouve une longue chaîne de caractères et de chiffres : `94ab1fe28727...`

Cela s'appelle le SHA. Un SHA est un identifiant unique généré pour chaque commit.

Pour vérifier un commit spécifique, vous devez simplement passer le SHA du commit comme paramètre à `git checkout` :

```
(ma-fonctionnalite)$ git checkout 035a128d2e66eb9fe3032036b3415e60c728f692
Note: switching to '035a128d2e66eb9fe3032036b3415e60c728f692'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 035a128 a
((HEAD detached at 035a128))$

```

> **Note** : Vous n'avez généralement besoin d'utiliser que les premiers caractères du SHA—les quatre ou cinq premiers caractères de la chaîne sont probablement uniques dans le projet.

## Qu'est-ce qu'un état HEAD détaché ?

Le résultat de la vérification d'un commit spécifique vous place dans un état "HEAD détaché".

[D'après la documentation :](http://git-scm.com/docs/git-checkout#_detached_head)

> [un état HEAD détaché] signifie simplement que `HEAD` fait référence à un commit spécifique, par opposition à une branche nommée

En gros, le `HEAD` (l'un des pointeurs internes de Git qui suit où vous vous trouvez dans l'historique Git) s'est détourné des branches connues, et donc les changements à partir de ce point formeraient un nouveau chemin dans l'historique Git.

Git veut s'assurer que c'est ce que vous avez l'intention de faire, il vous donne donc un "espace libre" pour expérimenter—comme décrit par la sortie :

```
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.
```

À partir de cette position, vous avez deux options :

* Expérimenter puis jeter vos changements en revenant à votre branche précédente
* Travailler à partir de là et démarrer une nouvelle branche à partir de ce point

Vous pouvez utiliser la commande `git switch -` pour annuler les changements que vous avez effectués et revenir à votre branche précédente.

Si vous souhaitez plutôt conserver vos changements et continuer à partir de là, vous pouvez utiliser `git switch -c <new-branch-name>` pour _créer une nouvelle branche_ à partir de ce point.

## Conclusion

La commande `git checkout` est une commande utile et polyvalente.

Vous pouvez l'utiliser pour créer de nouvelles branches, vérifier une branche, vérifier des commits spécifiques, et plus encore.

Si vous avez aimé ce tutoriel, je parle également de sujets comme celui-ci [sur Twitter](https://twitter.com/johnmosesman), et j'écris à leur sujet [sur mon site.](https://johnmosesman.com/)