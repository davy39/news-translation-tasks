---
title: La commande Git Cherry Pick
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T22:08:00.000Z'
originalURL: https://freecodecamp.org/news/the-git-cherry-pick-command
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d79740569d1a4ca37f4.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
seo_title: La commande Git Cherry Pick
seo_desc: 'Git Cherry Pick

  The git cherry-pick command applies the changes introduced by some existing commits.
  This guide will be focusing on explaining this feature as much as possible but of
  course the real Git documentation will always come in handy.

  Checko...'
---

## **Git Cherry Pick**

La commande `git cherry-pick` applique les modifications introduites par certains commits existants. Ce guide se concentrera sur l'explication de cette fonctionnalité autant que possible, mais bien sûr, la vraie [documentation Git](https://git-scm.com/docs/git-cherry-pick) sera toujours utile.

### **Basculer vers une branche existante et Cherry Pick depuis master**

Pour appliquer la modification introduite par le commit à la pointe de la branche master et créer un nouveau commit avec cette modification. Exécutez la commande suivante

```shell
git cherry-pick master
```

### **Vérifier une modification depuis un commit différent**

Pour appliquer la modification introduite par le commit à la valeur de hachage particulière que vous souhaitez, exécutez la commande suivante

```shell
git cherry-pick {HASHVALUE}
```

Cela ajoutera les modifications incluses dans ce commit à votre dépôt actuel.

### **Appliquer certains commits d'une branche à une autre**

`cherry-pick` vous permet de choisir entre les commits d'une branche à une autre. Supposons que vous avez deux branches `master` et `develop-1`. Dans la branche `develop-1`, vous avez 3 commits avec les identifiants de commit `commit-1`, `commit-2` et `commit-3`. Ici, vous pouvez appliquer uniquement `commit-2` à la branche `master` par :

```shell
git checkout master
git cherry-pick commit-2
```

Si vous rencontrez des conflits à ce stade, vous devez les résoudre et les ajouter en utilisant `git add`, puis vous pouvez utiliser le drapeau continue pour appliquer le cherry-pick.

```shell
git cherry-pick --continue
```

Si vous souhaitez annuler un cherry-pick en cours, vous pouvez utiliser le drapeau abort :

```shell
git cherry-pick --abort
```

## Plus d'informations sur les commandes Git :

* [10 astuces de terminal que chaque développeur devrait connaître](https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/)
* [Toutes les commandes Git qu'un développeur a utilisées en une semaine](https://www.freecodecamp.org/news/git-cheat-sheet-and-best-practices-c6ce5321f52/)