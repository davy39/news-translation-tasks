---
title: 7 Astuces Git que vous ne pouvez pas ignorer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-11T22:17:28.000Z'
originalURL: https://freecodecamp.org/news/7-git-hacks-you-just-can-t-ignore-41aea137727a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_RzIXapqnP4ZZ9twx5_KSg.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: 7 Astuces Git que vous ne pouvez pas ignorer
seo_desc: 'By Ritesh Shrivastav

  Git has probably saved more developers’ jobs than any other technology. As long
  as you frequently save your work with Git, you will always be able to roll back
  to how your code was in the past, thus reversing those late night mis...'
---

Par Ritesh Shrivastav

Git a probablement sauvé plus d'emplois de développeurs que toute autre technologie. Tant que vous sauvegardez fréquemment votre travail avec Git, vous pourrez toujours revenir à l'état précédent de votre code, annulant ainsi ces erreurs de dernière minute.

Cela dit, l'interface en ligne de commande de Git est notoirement difficile à maîtriser. Explorons 7 astuces pour tirer le meilleur parti de Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*n2QYqEj3coS_yKNl.png)
*crédit photo : [xkcd](http://xkcd.com/" rel="noopener" target="_blank" title=")*

Habituellement, 70 % de l'utilisation de Git se limite à _add_, _commit_, _branch_ et _push / pull_. La plupart des gens sont familiers avec le flux qui va toujours dans une seule direction. Vous êtes-vous déjà demandé comment revenir en arrière ou annuler des étapes si vous avez ajouté des fichiers incorrects au _repo_ ou fait un _commit_ avec un message incorrect sur une mauvaise _branch_ ?

Si vous êtes l'un de ceux qui suivent ce qui est montré dans la bande dessinée ci-dessus, alors cette liste d'astuces Git est pour vous.

#### **1. Modifier un message de commit incorrect**

Le message de commit va vivre très longtemps dans votre base de code, vous voulez donc qu'il définisse correctement les changements.

Cette commande vous permettra de modifier le message de commit le plus récent. Vous devez vous assurer qu'il n'y a pas de changements dans la copie de travail, sinon ils pourraient aussi être commis.

```
$ git commit --amend -m "VOTRE-NOUVEAU-MESSAGE-DE-COMMIT"
```

Si vous avez déjà _poussé_ votre _commit_ vers la branche distante, vous devez alors forcer le push du commit avec cette commande :

```
$ git push <remote> <branch> --force
```

Vous pouvez suivre cette [réponse Stack Overflow](http://stackoverflow.com/questions/179123/edit-an-incorrect-commit-message-in-git/179147#179147) pour plus d'informations.

#### **2. Annuler 'git add' avant de commiter**

Que faire si vous avez ajouté des fichiers incorrects à votre zone de staging, mais que vous n'avez pas encore fait de commit ? Vous pouvez annuler cela avec une simple commande. Si un seul fichier doit être retiré :

```
$ git reset <filename>
```

ou si vous voulez désindexer toutes vos modifications non commises :

```
$ git reset
```

Vous pouvez suivre cette [réponse Stack Overflow](http://stackoverflow.com/questions/348170/undo-git-add-before-commit/348234#348234) pour plus d'informations.

#### **3. Annuler votre commit le plus récent**

Parfois, vous avez accidentellement commis les mauvais fichiers ou oublié quelque chose au départ. Voici un processus en trois étapes pour vous couvrir dans de tels cas.

```
$ git reset --soft HEAD~1# apportez des modifications à vos fichiers de travail si nécessaire$ git add -A .$ git commit -c ORIG_HEAD
```

Lorsque vous exécutez la première commande, Git déplacera votre pointeur HEAD vers le commit que vous avez fait avant celui-ci, afin que vous puissiez déplacer des fichiers ou apporter des modifications si nécessaire.

Ensuite, vous ajoutez toutes vos modifications, et lorsque vous exécutez enfin la dernière commande, Git ouvrira votre éditeur de texte par défaut avec le même message de commit. Vous pouvez modifier ce message si vous le souhaitez, ou vous pouvez remplacer cette étape entièrement en utilisant '-C' au lieu de '-c' dans la commande finale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eiuAyfDRLIr6ZKutQWbJZQ.gif)
_Git + spaghetti = spagitty_

#### **4. Revenir à un commit précédent dans votre repo Git**

'Revenir' peut avoir beaucoup de sens dans de nombreux cas — surtout si vous avez complètement gâché un morceau de code. Le cas le plus courant est lorsque vous voulez revenir dans le temps et explorer un état précédent de votre base de code, puis revenir à votre état actuel. Cela peut être fait par :

```
$ git checkout <SHA>
```

'<SHA>' sont les 8 à 10 premiers caractères du code de hachage du commit où vous voulez aller.

Cela détachera le HEAD et vous permettra de manipuler sans aucune branche sélectionnée. Ne vous inquiétez pas — détacher votre tête n'est pas aussi effrayant que cela en a l'air. Si vous voulez faire des commits pendant que vous êtes ici, vous pouvez le faire en créant une nouvelle branche ici :

```
$ git checkout -b <SHA>
```

Pour revenir à l'état actuel, il suffit de revenir à la branche sur laquelle vous étiez précédemment.

Vous pouvez suivre cette [réponse Stack Overflow](http://stackoverflow.com/questions/4114095/revert-git-repo-to-a-previous-commit/4114122#4114122) pour plus d'informations.

#### **5. Annuler une fusion Git**

Vous devrez peut-être faire une _réinitialisation forcée_ au commit précédent pour annuler une fusion. Ce que 'merge' fait essentiellement, c'est qu'il réinitialise l'index et met à jour les fichiers dans l'arborescence de travail qui sont différents entre _<commit>_ et HEAD, mais conserve ceux qui sont différents entre l'index et l'arborescence de travail (c'est-à-dire ceux qui ont des changements qui n'ont pas été ajoutés).

```
$ git checkout -b <SHA>
```

Mais il y a toujours des moyens alternatifs de faire les choses dans Git, et vous pouvez les explorer [ici](http://stackoverflow.com/questions/2389361/undo-a-git-merge?rq=1).

#### **6. Supprimer les fichiers locaux (non suivis) de la branche Git actuelle**

Supposons que vous ayez beaucoup de fichiers qui ne sont pas suivis (parce qu'ils ne sont pas nécessaires), et que vous ne voulez pas qu'ils apparaissent chaque fois que vous utilisez _git status_. Voici quelques façons de contourner ce problème :

```
$ git clean -f -n         # 1
```

```
$ git clean -f            # 2
```

```
$ git clean -fd           # 3
```

```
$ git clean -fX           # 4
```

```
$ git clean -fx           # 5
```

(1) : l'option _-n_ vous permettra de savoir quels fichiers seront supprimés si vous exécutez (2).

(2) : Cela supprimera tous les fichiers signalés par la commande (1).

(3) : _-d_ si vous voulez aussi supprimer les répertoires.

(4) : _-X_ si vous voulez seulement supprimer les fichiers ignorés.

(5) : _-x_ si vous voulez supprimer à la fois les fichiers ignorés et non ignorés.

Notez la différence de casse de _X_ dans les deux dernières commandes.

Pour plus d'informations, vous pouvez explorer la [documentation officielle de git-clean](http://git-scm.com/docs/git-clean).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bLtPTIsKUeAQHPo2eGrKpw.png)
*Crédit photo : [xkcd](http://xkcd.com/" rel="noopener" target="_blank" title=")*

#### **7. Supprimer une branche Git localement et à distance**

Pour supprimer une branche locale :

```
$ git branch --delete --force <branchName>
```

```
# OU utilisez -D comme raccourci :
```

```
$ git branch -D
```

Pour supprimer une branche distante :

```
$ git push origin --delete <branchName>
```

#### Devenez bon avec Git

Consultez [la documentation officielle de formation GitHub](https://training.github.com/kit/downloads/github-git-cheat-sheet) pour un guide de référence rapide, et la [documentation officielle de Git](https://git-scm.com/docs) pour en savoir plus sur Git.

Si vous avez une astuce Git préférée, postez-la dans les commentaires et dites-nous comment vous l'utilisez.

*Initialement publié sur [blog.projectshrv.com](http://blog.projectshrv.com/7-git-hacks-you-cant-ignore/) le 11 novembre 2015.*