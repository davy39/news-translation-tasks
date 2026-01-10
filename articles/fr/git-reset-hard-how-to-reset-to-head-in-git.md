---
title: Git Reset Hard – Comment réinitialiser à Head dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-10T12:09:39.000Z'
originalURL: https://freecodecamp.org/news/git-reset-hard-how-to-reset-to-head-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/resetToHead.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Reset Hard – Comment réinitialiser à Head dans Git
seo_desc: 'Git is a powerful version control system for tracking and managing changes
  and files in your source codes and other digital assets. One of the core functionalities
  of Git is "commits".

  Commits let you create a snapshot of your code. In other words, i...'
---

Git est un système de contrôle de version puissant pour suivre et gérer les changements et les fichiers dans vos codes sources et autres actifs numériques. L'une des fonctionnalités principales de Git est les "commits".

Les commits vous permettent de créer une capture instantanée de votre code. En d'autres termes, c'est comme sauvegarder votre travail, mais avec certains avantages et différences supplémentaires. Lorsque vous créez un commit, c'est une version de votre code.

Lors de l'utilisation de Git, il peut y avoir des situations où vous souhaitez réinitialiser à un commit particulier ou réinitialiser au commit le plus récent dans la branche actuelle.

Dans cet article, je vais vous montrer comment réinitialiser à `HEAD` dans Git. Mais qu'est-ce que `HEAD` dans Git ? C'est ce que nous allons voir ensuite !


## Ce que nous allons couvrir
- [Qu'est-ce que `HEAD` dans Git ?](#heading-quest-ce-que-head-dans-git)
- [Pourquoi réinitialiser à `HEAD` ou à un autre commit dans Git ?](#heading-pourquoi-reinitialiser-a-head-ou-a-un-autre-commit-dans-git)
- [Comment réinitialiser à `HEAD` dans Git](#heading-comment-reinitialiser-a-head-dans-git)
- [Comment réinitialiser à un commit particulier avec la commande Git Reset](#heading-comment-reinitialiser-a-un-commit-particulier-avec-la-commande-git-reset)
- [Conclusion](#heading-conclusion)


## Qu'est-ce que `HEAD` dans Git ?
Dans Git, `HEAD` pointe vers le sommet de la branche actuelle, qui est le commit où vous avez mis à jour la branche actuelle pour la dernière fois. Ainsi, `HEAD` est une référence au commit le plus récent dans la branche actuelle.

Lorsque vous créez un nouveau commit, Git met automatiquement à jour `HEAD` pour pointer vers le nouveau commit. Vous pouvez utiliser la commande `git log --oneline` pour afficher l'historique des commits de la branche actuelle, et le commit en haut de la liste est celui vers lequel `HEAD` pointe actuellement.

Par exemple, dans le code d'exemple que j'utilise pour vous montrer comment réinitialiser à `HEAD` dans Git, le `HEAD` actuel est le hash de commit `d8cd0ee`, avec le message de commit `Linked JavaScript file` :

![Screenshot-2023-04-10-at-10.39.42](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.39.42.png)

`HEAD` peut également être utilisé pour faire référence à l'état actuel du répertoire de travail. Par exemple, si vous apportez des modifications à des fichiers dans votre répertoire de travail mais ne les avez pas encore commises, vous pouvez utiliser la commande `git diff HEAD` pour voir les différences entre le répertoire de travail et le dernier commit :

![Screenshot-2023-04-10-at-10.43.29](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.43.29.png)

Ainsi, lorsque nous parlons de réinitialiser à `HEAD`, cela signifie réinitialiser la branche actuelle au commit le plus récent. En plus de `HEAD`, vous pouvez également réinitialiser à d'autres commits avec la commande `git reset --hard <commit-hash>`.

Vous pouvez même utiliser certains nombres avec `HEAD` lui-même pour revenir à un commit particulier. Par exemple, `HEAD{0}` signifie `HEAD` lui-même, `HEAD{1}` signifie le commit avant `HEAD`, `HEAD{2}` signifie deux commits avant `HEAD`, et ainsi de suite.


## Pourquoi réinitialiser à `HEAD` ou à un autre commit dans Git ?
Certaines des situations qui pourraient vous amener à réinitialiser à `HEAD` dans Git incluent les suivantes :
- annuler des changements indésirables : si vous avez des changements non commités qui vous déroutent et que vous voulez vous en débarrasser
- annuler la mise en stage des changements : si vous avez ajouté des changements à la zone de staging et que vous ne les voulez plus
- corriger un mauvais commit : si vous avez déjà un commit et que vous avez découvert qu'il y a des problèmes avec celui-ci qui vous déroutent
- diviser un commit : si le commit que vous ou un membre de l'équipe avez fait implique trop de changements qui sont différents en portée


## Comment réinitialiser à `HEAD` dans Git
Pour plus de clarté, exécutez `git log --oneline` pour afficher votre historique de commits :

![Screenshot-2023-04-10-at-10.39.42-1](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.39.42-1.png)

Si c'est une grande base de code et que vous voulez voir plus de détails, vous pouvez exécuter `git log --oneline --graph` :

![Screenshot-2023-04-10-at-11.04.56](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.04.56.png)

La commande `git log --oneline --graph` inclut une représentation graphique de l'historique des commits. Cela peut être particulièrement utile pour visualiser des scénarios complexes de branchement et de fusion.

Dans les deux captures d'écran ci-dessus, le `HEAD` est le hash de commit `d8cd0ee`, avec le message de commit `Linked JavaScript file`. C'est le commit précédent que j'ai fait.

Pour réinitialiser la base de code à ce commit, j'exécuterais `git reset --hard HEAD` :

![Screenshot-2023-04-10-at-11.10.45](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.10.45.png)

Vous pouvez voir que j'ai obtenu la réponse `HEAD is now at d8cd0ee Linked JavaScript file`, comme vous pouvez le voir sur la capture d'écran également.

La commande `git reset --hard HEAD` supprimera toutes les modifications non commitées même si vous les avez ajoutées à la zone de staging.


## Comment réinitialiser à un commit particulier avec la commande Git Reset
En plus de réinitialiser à `HEAD` lui-même, vous pouvez également réinitialiser à un commit particulier.

Tout d'abord, exécutez `git reflog` pour voir comment chaque commit est associé à `HEAD` :

![Screenshot-2023-04-10-at-11.17.37](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.17.37.png)

Vous pouvez maintenant exécuter `git reset --hard HEAD@{n}` pour revenir à un commit particulier. Par exemple, je veux revenir au message de commit `Linked CSS file`. Donc, j'exécuterais `git reset --hard HEAD@{5}` pour revenir à ce commit :

![Screenshot-2023-04-10-at-11.25.13](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.25.13.png)

Vous pouvez voir que `HEAD` s'est déplacé vers un autre commit. J'exécuterais à nouveau `git log --oneline` pour voir `HEAD` et les autres commits :

![Screenshot-2023-04-10-at-11.26.46](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.26.46.png)


## Conclusion
Cet article vous a montré comment réinitialiser votre base de code à HEAD et à un commit particulier en utilisant les commandes `git reset --hard HEAD` et `git reset --hard HEAD@{n}`.

Soyez conscient que la commande `git reset --hard HEAD` ou `git reset --hard HEAD@{n}` supprimera vos modifications non commitées, même si vous les avez mises en stage. Si vous ne voulez pas que vos modifications non mises en stage soient supprimées, vous pouvez utiliser le drapeau `--soft` au lieu du drapeau `--hard`.

Merci d'avoir lu.