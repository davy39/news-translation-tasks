---
title: git config – Comment configurer les paramètres Git pour améliorer votre flux
  de travail de développement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-09T19:14:42.000Z'
originalURL: https://freecodecamp.org/news/git-config-how-to-configure-git-settings
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-thisisengineering-3861958.jpg
tags:
- name: configuring settings
  slug: configuring-settings
- name: Git
  slug: git
- name: Productivity
  slug: productivity
seo_title: git config – Comment configurer les paramètres Git pour améliorer votre
  flux de travail de développement
seo_desc: "By Dillion Megida\ngit config is a powerful command in Git. You can use\
  \ the Git configuration file to customize how Git works. \nThis file exists in the\
  \ project level where Git is initialized (/project/.git/config) or at the root level\
  \ (~/.gitconfig). ..."
---

Par Dillion Megida

`git config` est une commande puissante dans Git. Vous pouvez utiliser le fichier de configuration Git pour personnaliser le fonctionnement de Git. 

Ce fichier existe au niveau du projet où Git est initialisé (`/project/.git/config`) ou au niveau de la racine (`~/.gitconfig`). Si aucune configuration n'est spécifiée, Git utilise ses paramètres par défaut.

Dans cet article, vous apprendrez quelques configurations Git utiles qui peuvent améliorer votre flux de travail de développement. Les conseils partagés ici sont des choses qui ont fonctionné pour moi. Il y en a beaucoup d'autres que vous pourrez essayer après votre lecture.

# Conseils de configuration Git

Voici quelques conseils de configuration globale de Git.

## 1. Choisir l'éditeur par défaut pour Git

Lorsque vous essayez de faire des commits dans Git, il ouvrira par défaut un éditeur `vi` qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-18.png)

Cet éditeur peut être difficile à utiliser, et si vous êtes comme moi, vous voudrez peut-être utiliser votre éditeur préféré pour rédiger des commits. Dans votre fichier `~/.gitconfig`, ajoutez ce qui suit :

```txt
[core]
    editor = code --wait
```

ou utilisez cette commande shell :

```txt
git config --global core.editor "code --wait"
```

Cette configuration indique à Git que pour les opérations telles que les commits et les tags, je souhaite utiliser mon [éditeur VSCode](https://code.visualstudio.com/).


Pour d'autres types d'éditeurs, veuillez vous référer à cette image d' [Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-19.png)
_Configurations d'éditeur pour git d'après [git config | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)_

## 2. Élagage Git (pruning) pendant le fetch

Savez-vous ce que fait la commande d'élagage (pruning) pendant le fetch ? Sinon, vous voudrez peut-être d'abord consulter cet article qui explique comment [supprimer les branches locales obsolètes avec l'option git prune et la commande branch delete](https://dillionmegida.com/p/delete-outdated-branches/#git-fetch---prune).

TL;DR : L'élagage pendant le fetch est une méthode de nettoyage qui supprime les références distantes obsolètes dans votre répertoire `.git` lorsque vous effectuez un `git fetch --prune`.

Comme je l'explique dans l'article que je viens de lier, vous pouvez automatiser cela sans toujours ajouter l'option `--prune`. Pour ce faire, ajoutez ce qui suit à `~/.gitconfig` :

```txt
[fetch]
    prune = true
```

ou utilisez la commande suivante :

```shell
git config --global fetch.prune true
```

Une fois cela en place, l'élagage se produira chaque fois que vous ferez un `git fetch`.

## 3. Les alias Git

Dans le fichier de configuration Git, vous pouvez ajouter des alias pour ces commandes longues que vous tapez de temps en temps. Par exemple, les commits, le stashing, etc.

Supposons que vous vouliez ajouter un alias pour ajouter un commit vide. Dans ce cas, vous pouvez ajouter ce qui suit au fichier de configuration :

```txt
[alias]
    empty = "git commit --allow-empty"
```

ou dans le terminal :

```shell
git config --global alias.empty "git commit --allow-empty"
```

Et vous pouvez utiliser la commande comme ceci :

```shell
git empty "Empty commit"
```

Vous pouvez également ajouter d'autres commandes shell en dehors de Git comme alias. Par exemple, un alias qui supprime les branches locales qui ont été fusionnées à distance :

```txt
[alias]
    delete-local-merged = "!git fetch && git branch --merged | egrep -v 'master' | xargs git branch -d"
```

Le point d'exclamation "!" indique à Git de l'exécuter comme une commande shell et non comme une commande `git *`.

Pour l'alias, nous faisons un git fetch. Ensuite, nous récupérons les branches fusionnées, nous passons cela en entrée à la commande egrep, nous filtrons la branche "master" et nous supprimons les branches.

## 4. Définir la branche par défaut

Lors de l'initialisation d'un dépôt (`git init`), la branche par défaut est `master`. Aujourd'hui, certains développeurs préféreraient que ce soit `main` ou tout autre chose.

Vous n'avez pas besoin de créer une nouvelle branche appelée `main`, de supprimer la branche `master` et d'utiliser `main` comme branche par défaut. C'est un long processus. Dans le fichier de configuration Git, vous pouvez définir une branche par défaut lors de l'initialisation de Git. Voici comment :

```txt
[init]
    defaultBranch = main (ou n'importe quel nom que vous voulez)
```

De cette façon, `git init` créera une branche "main" par défaut.

## 5. Afficher le statut court par défaut

Par défaut, la commande `git status` vous montre les changements dans votre projet avec de longs détails. C'est sous ce format :

```bash
Sur la branche [nom de la branche]
Votre branche est à jour avec ...

Modifications qui ne sont pas prêtes pour le commit :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera commité)
  (utilisez "git restore <fichier>..." pour abandonner les modifications dans le répertoire de travail)
    modifié : ...
    
Fichiers non suivis :
  (utilisez "git add <fichier>..." pour inclure ce qui sera commité)
    ...
    
aucune modification ajoutée au commit (utilisez "git add" et/ou "git commit -a")
```

C'est une sortie utile avec des instructions, mais parfois vous avez juste besoin d'un résumé de l'état du dépôt. L'option `--short` ajoutée à `git status` donne une sortie formatée courte. Le résultat ressemblerait à ceci :

```bash
M [fichier]
?? [fichier]
```

"M" signifie modifié, et "??" signifie non suivi (untracked). Nous pouvons améliorer ce processus encore plus en en faisant la vue d'état par défaut en utilisant la configuration suivante :

```txt
[status]
    short = true
```

# Conclusion
Dans cette liste non exhaustive, nous avons vu cinq façons d'améliorer notre flux de travail de développement en personnalisant le fonctionnement de Git par défaut. 

Vous pouvez trouver plus d'informations sur toutes les options de configuration de Git (des branches aux pulls, en passant par les fetches, et bien d'autres) dans la [documentation git-config](https://git-scm.com/docs/git-config).