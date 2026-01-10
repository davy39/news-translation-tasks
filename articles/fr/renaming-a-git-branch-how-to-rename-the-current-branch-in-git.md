---
title: Renommer une branche Git – Comment renommer la branche actuelle dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-07T18:22:39.000Z'
originalURL: https://freecodecamp.org/news/renaming-a-git-branch-how-to-rename-the-current-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/git-branches.png
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Renommer une branche Git – Comment renommer la branche actuelle dans Git
seo_desc: 'If you are using Git for version control, it’s likely you’ve created branches
  for various reasons.

  Since you have those branches in place, you might want to rename any of them if
  you find a typo, for example, or change the code''s purpose.

  In this art...'
---

Si vous utilisez Git pour le contrôle de version, il est probable que vous ayez créé des branches pour diverses raisons.

Puisque vous avez ces branches en place, vous pourriez vouloir renommer l'une d'entre elles si vous trouvez une faute de frappe, par exemple, ou si vous changez le but du code.

Dans cet article, je vais vous montrer comment renommer la branche sur laquelle vous travaillez sans basculer vers une autre branche.

## Comment renommer une branche dans Git
Pour renommer une branche sur laquelle vous ne travaillez pas actuellement, vous exécutez généralement la commande `git branch -m ancien-nom nouveau-nom`.

Par exemple, je suis actuellement sur la branche principale et j'ai pu renommer `kolade-works` en `kolade-codes`.

![ss1-1](https://www.freecodecamp.org/news/content/images/2022/09/ss1-1.png) 

Passez à la section suivante de cet article pour voir comment vous pouvez renommer la branche actuelle dans Git.

## Comment renommer la branche actuelle dans Git
La première chose que vous devez faire est d'exécuter `git branch` pour voir les branches que vous avez en place :

![ss2-1](https://www.freecodecamp.org/news/content/images/2022/09/ss2-1.png) 

Ensuite, assurez-vous d'être dans la branche dont vous voulez changer le nom. Vous pouvez le faire en exécutant `git checkout nom-de-la-branche`.

Dans ce cas, je veux changer la branche `fix-bug` en `bug-fixes`. Je vais donc exécuter `git checkout fix-bug` :

![ss3-1](https://www.freecodecamp.org/news/content/images/2022/09/ss3-1.png) 

Vous pouvez voir que git bash m'indique la branche dans laquelle je me trouve actuellement, qui est `fix bug`.

Pour renommer la branche, vous devez exécuter la commande `git branch -m nouveau-nom`.

Rappelons que j'ai mentionné que je voulais renommer la branche `fix bug` en `bug-fixes`, donc je vais exécuter `git branch -m bug-fixes`.

![ss4-1](https://www.freecodecamp.org/news/content/images/2022/09/ss4-1.png) 

`-m` dans cette situation est un drapeau qui signifie `move` (déplacer).

Vous pouvez voir que le nom de la branche a été changé avec succès en `bug fixes`.

Pour confirmer cela, vous pouvez exécuter à nouveau `git branch` :

![ss5-1](https://www.freecodecamp.org/news/content/images/2022/09/ss5-1.png) 

## Conclusion
Cet article vous a montré comment renommer une branche Git locale, surtout si c'est la branche actuelle. Même si ce n'est pas la branche actuelle, vous avez également appris la commande à utiliser dans ce cas.

Si vous voulez apprendre à renommer une branche distante également, j'ai écrit [un article](https://www.freecodecamp.org/news/how-to-rename-a-local-or-remote-branch-in-git/) à ce sujet aussi.

Merci d'avoir lu.