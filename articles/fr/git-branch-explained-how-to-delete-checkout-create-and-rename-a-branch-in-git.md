---
title: 'Git Branch Expliqué : Comment Supprimer, Checkout, Créer et Renommer une Branche
  dans Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-02T22:32:00.000Z'
originalURL: https://freecodecamp.org/news/git-branch-explained-how-to-delete-checkout-create-and-rename-a-branch-in-git
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cda740569d1a4ca348c.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
- name: version control
  slug: version-control
seo_title: 'Git Branch Expliqué : Comment Supprimer, Checkout, Créer et Renommer une
  Branche dans Git'
seo_desc: 'Git Branch

  Git’s branching functionality lets you create new branches of a project to test
  ideas, isolate new features, or experiment without impacting the main project.

  Table of Contents


  View Branches

  Checkout a Branch

  Create a New Branch

  Rename a ...'
---

## **Git Branch**

La fonctionnalité de branchement de Git vous permet de créer de nouvelles branches d'un projet pour tester des idées, isoler de nouvelles fonctionnalités ou expérimenter sans impacter le projet principal.

**Table des Matières**

* [Voir les Branches](https://guide.freecodecamp.org/git/git-branch/#voir-les-branches)
* [Checkout une Branche](https://guide.freecodecamp.org/git/git-branch/#checkout-une-branche)
* [Créer une Nouvelle Branche](https://guide.freecodecamp.org/git/git-branch/#creer-une-nouvelle-branche)
* [Renommer une Branche](https://guide.freecodecamp.org/git/git-branch/#renommer-une-branche)
* [Supprimer une Branche](https://guide.freecodecamp.org/git/git-branch/#supprimer-une-branche)
* [Comparer les Branches](https://guide.freecodecamp.org/git/git-branch/#comparer-les-branches)
* [Aide avec Git Branch](https://guide.freecodecamp.org/git/git-branch/#aide-avec-git-branch)
* [Plus d'Informations](https://guide.freecodecamp.org/git/git-branch/#plus-dinformations)

### **Voir les Branches**

Pour voir les branches dans un dépôt Git, exécutez la commande :

```shell
git branch
```

Pour voir à la fois les branches de suivi à distance et les branches locales, exécutez la commande :

```shell
git branch -a
```

Il y aura un astérisque (*) à côté de la branche sur laquelle vous vous trouvez actuellement.

Il existe plusieurs options différentes que vous pouvez inclure avec `git branch` pour voir différentes informations. Pour plus de détails sur les branches, vous pouvez utiliser l'option `-v` (ou `-vv`, ou `--verbose`). La liste des branches inclura la valeur SHA-1 et la ligne de sujet du commit pour le `HEAD` de chaque branche à côté de son nom.

Vous pouvez utiliser l'option `-a` (ou `--all`) pour afficher les branches locales ainsi que les branches distantes d'un dépôt. Si vous souhaitez uniquement voir les branches distantes, utilisez l'option `-r` (ou `--remotes`).

### **Checkout une Branche**

Pour basculer vers une branche existante, exécutez la commande :

```shell
git checkout NOM-DE-LA-BRANCHE
```

Généralement, Git ne vous permettra pas de basculer vers une autre branche à moins que votre répertoire de travail soit propre, car vous perdriez toutes les modifications du répertoire de travail qui ne sont pas validées. Vous avez trois options pour gérer vos modifications :

1. les supprimer (voir [Git checkout pour plus de détails](https://www.freecodecamp.org/news/git-checkout-explained/)) ou
2. les valider (voir [Git commit pour plus de détails](https://www.freecodecamp.org/news/git-commit-command-explained/)) ou
3. les stocker (voir [Git stash pour plus de détails](https://www.freecodecamp.org/news/git-stash-explained/)).

### **Créer une Nouvelle Branche**

Pour créer une nouvelle branche, exécutez la commande :

```shell
git branch NOUVEAU-NOM-DE-BRANCHE
```

Notez que cette commande crée uniquement la nouvelle branche. Vous devrez exécuter `git checkout NOUVEAU-NOM-DE-BRANCHE` pour basculer vers celle-ci.

Il existe un raccourci pour créer et basculer vers une nouvelle branche en une seule fois. Vous pouvez passer l'option `-b` (pour branch) avec `git checkout`. Les commandes suivantes font la même chose :

```shell
# Méthode en deux étapes
git branch NOUVEAU-NOM-DE-BRANCHE
git checkout NOUVEAU-NOM-DE-BRANCHE

# Raccourci
git checkout -b NOUVEAU-NOM-DE-BRANCHE
```

Lorsque vous créez une nouvelle branche, elle inclura tous les commits de la branche parente. La branche parente est la branche sur laquelle vous vous trouvez lorsque vous créez la nouvelle branche.

### **Renommer une Branche**

Pour renommer une branche, exécutez la commande :

```shell
git branch -m ANCIEN-NOM-DE-BRANCHE NOUVEAU-NOM-DE-BRANCHE

# Alternative
git branch --move ANCIEN-NOM-DE-BRANCHE NOUVEAU-NOM-DE-BRANCHE
```

### **Supprimer une Branche**

Git ne vous permettra pas de supprimer une branche sur laquelle vous vous trouvez actuellement. Vous devez d'abord basculer vers une autre branche, puis exécuter la commande :

```shell
git branch -d BRANCHE-A-SUPPRIMER

# Alternative :
git branch --delete BRANCHE-A-SUPPRIMER
```

La branche vers laquelle vous basculez fait une différence. Git générera une erreur si les modifications de la branche que vous essayez de supprimer ne sont pas entièrement fusionnées dans la branche actuelle. Vous pouvez outrepasser cela et forcer Git à supprimer la branche avec l'option `-D` (notez la lettre majuscule) ou en utilisant l'option `--force` avec `-d` ou `--delete` :

```shell
git branch -D BRANCHE-A-SUPPRIMER

# Alternatives
git branch -d --force BRANCHE-A-SUPPRIMER
git branch --delete --force BRANCHE-A-SUPPRIMER
```

### **Comparer les Branches**

Vous pouvez comparer les branches avec la commande `git diff` :

```shell
git diff PREMIERE-BRANCHE..DEUXIEME-BRANCHE
```

Vous verrez une sortie colorée pour les changements entre les branches. Pour toutes les lignes qui ont changé, la version de la `DEUXIEME-BRANCHE` sera une ligne verte commençant par un "+", et la version de la `PREMIERE-BRANCHE` sera une ligne rouge commençant par un "-". Si vous ne voulez pas que Git affiche deux lignes pour chaque changement, vous pouvez utiliser l'option `--color-words`. Au lieu de cela, Git affichera une ligne avec le texte supprimé en rouge et le texte ajouté en vert.

Si vous voulez voir une liste de toutes les branches qui sont complètement fusionnées dans votre branche actuelle (en d'autres termes, votre branche actuelle inclut tous les changements des autres branches qui sont listées), exécutez la commande `git branch --merged`.

### **Aide avec Git Branch**

Si vous oubliez comment utiliser une option, ou si vous souhaitez explorer d'autres fonctionnalités autour de la commande `git branch`, vous pouvez exécuter l'une de ces commandes :

```shell
git help branch
git branch --help
man git-branch
```

### **Plus d'Informations :**

* [La commande `git merge`](https://www.freecodecamp.org/news/the-ultimate-guide-to-git-merge-and-git-rebase/)
* [La commande `git checkout`](https://www.freecodecamp.org/news/git-checkout-explained/)
* [La commande `git commit`](https://www.freecodecamp.org/news/git-commit-command-explained/)
* [La commande `git stash`](https://www.freecodecamp.org/news/git-stash-explained/)
* Documentation Git : [branch](https://git-scm.com/docs/git-branch)