---
title: Explication de Git Pull
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T18:33:00.000Z'
originalURL: https://freecodecamp.org/news/git-pull-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/clem-onojeghuo-gBnHMsAOWrs-unsplash.jpg
tags:
- name: Git
  slug: git
seo_title: Explication de Git Pull
seo_desc: 'git pull is a Git command used to update the local version of a repository
  from a remote.

  It is one of the four commands that prompts network interaction by Git. By default,
  git pull does two things.


  Updates the current local working branch (current...'
---

`git pull` est une commande Git utilisée pour mettre à jour la version locale d'un dépôt à partir d'un dépôt distant.

C'est l'une des quatre commandes qui déclenchent une interaction réseau avec Git. Par défaut, `git pull` fait deux choses.

1. Met à jour la branche locale de travail actuelle (branche actuellement extraite)
2. Met à jour les branches de suivi distant pour toutes les autres branches.

`git pull` récupère (`git fetch`) les nouveaux commits et fusionne [(`git merge`)](https://guide.freecodecamp.org/git/git-merge) ceux-ci dans votre branche locale.

La syntaxe de cette commande est la suivante :

```shell
# Format général
git pull OPTIONS REPOSITORY REFSPEC

# Récupérer depuis une branche spécifique
git pull REMOTE-NAME BRANCH-NAME
```

dans laquelle :

* **OPTIONS** sont les options de la commande, telles que `--quiet` ou `--verbose`. Vous pouvez en savoir plus sur les différentes options dans la [documentation Git](https://git-scm.com/docs/git-pull)
* **REPOSITORY** est l'URL de votre dépôt. Exemple : [https://github.com/freeCodeCamp/freeCodeCamp.git](https://github.com/freeCodeCamp/freeCodeCamp.git)
* **REFSPEC** spécifie quelles références récupérer et quelles références locales mettre à jour
* **REMOTE-NAME** est le nom de votre dépôt distant. Par exemple : _origin_.
* **BRANCH-NAME** est le nom de votre branche. Par exemple : _develop_.

**Note**

Si vous avez des modifications non validées, la partie fusion de la commande `git pull` échouera et votre branche locale restera inchangée.

Ainsi, vous devriez _toujours valider vos modifications dans une branche avant de récupérer_ de nouveaux commits depuis un dépôt distant.

**Table des matières**

* [Utilisation de `git pull`](https://guide.freecodecamp.org/git/git-pull/#utilisation-de-git-pull)
* [Contrôle de version distribué](https://guide.freecodecamp.org/git/git-pull/#controle-de-version-distribue)
* [`git fetch` + `git merge`](https://guide.freecodecamp.org/git/git-pull/#git-fetch-plus-git-merge)
* [`git pull` dans les IDE](https://guide.freecodecamp.org/git/git-pull/#git-pull-dans-les-ide)

### **Utilisation de git pull**

Utilisez `git pull` pour mettre à jour un dépôt local à partir du dépôt distant correspondant. Exemple : Tout en travaillant localement sur `master`, exécutez `git pull` pour mettre à jour la copie locale de `master` et mettre à jour les autres branches de suivi distant. (Plus d'informations sur les branches de suivi distant dans la section suivante.)

Mais, il y a quelques points à garder à l'esprit pour que cet exemple soit vrai :

Le dépôt local a un dépôt distant lié

* Vérifiez cela en exécutant `git remote -v`
* S'il y a plusieurs dépôts distants, `git pull` pourrait ne pas suffire. Vous devrez peut-être entrer `git pull origin` ou `git pull upstream`.

La branche sur laquelle vous êtes actuellement a une branche de suivi distant correspondante

* Vérifiez cela en exécutant `git status`. Si aucune branche de suivi distant n'existe, Git ne sait pas d'où récupérer les informations.

### **Contrôle de version distribué**

Git est un **Système de Contrôle de Version Distribué** (DVCS). Avec DVCS, les développeurs peuvent travailler sur le même fichier en même temps dans des environnements séparés. Après avoir _poussé_ le code vers le dépôt distant partagé, d'autres développeurs peuvent _récupérer_ le code modifié.

#### **Interactions réseau dans Git**

Il n'y a que quatre commandes qui déclenchent des interactions réseau dans Git. Un dépôt local n'a aucune connaissance des modifications apportées au dépôt distant jusqu'à ce qu'il y ait une demande d'informations. Et, un dépôt distant n'a aucune connaissance des modifications locales jusqu'à ce que les commits soient poussés.

Les quatre commandes réseau sont :

* `git clone`
* `git fetch`
* `git pull`
* `git push`

#### **Branches dans DVCS**

Lorsque vous travaillez avec Git, il peut sembler qu'il y ait beaucoup de copies du même code partout. Il existe différentes versions du même fichier sur chaque branche. Et, différentes copies des mêmes branches sur l'ordinateur de chaque développeur et sur le dépôt distant. Pour suivre cela, Git utilise ce qu'on appelle des **branches de suivi distant**.

Si vous exécutez `git branch --all` dans un dépôt Git, les branches de suivi distant apparaissent en rouge. Ce sont des copies en lecture seule du code tel qu'il apparaît sur le dépôt distant. (Quand a eu lieu la dernière interaction réseau qui aurait apporté des informations localement ? Souvenez-vous quand ces informations ont été mises à jour pour la dernière fois. Les informations dans les branches de suivi distant reflètent les informations de cette interaction.)

Avec les **branches de suivi distant**, vous pouvez travailler dans Git sur plusieurs branches sans interaction réseau. Chaque fois que vous exécutez les commandes `git pull` ou `git fetch`, vous mettez à jour les **branches de suivi distant**.

### **git fetch plus git merge**

`git pull` est une commande combinée, équivalente à `git fetch` + `git merge`.

#### **git fetch**

Seul, `git fetch` met à jour toutes les branches de suivi distant dans le dépôt local. Aucun changement n'est réellement reflété sur aucune des branches de travail locales.

#### **git merge**

Sans aucun argument, `git merge` fusionnera la branche de suivi distant correspondante avec la branche de travail locale.

#### **git pull**

`git fetch` met à jour les branches de suivi distant. `git merge` met à jour la branche actuelle avec la branche de suivi distant correspondante. En utilisant `git pull`, vous obtenez les deux parties de ces mises à jour. Mais, cela signifie que si vous êtes sur la branche `feature` et que vous exécutez `git pull`, lorsque vous basculerez sur `master`, les nouvelles mises à jour ne seront pas incluses. Chaque fois que vous basculez sur une autre branche qui peut avoir de nouveaux changements, il est toujours bon d'exécuter `git pull`.

### **git pull dans les IDE**

Le langage courant dans d'autres IDE peut ne pas inclure le mot `pull`. Si vous cherchez les mots `git pull` mais ne les voyez pas, cherchez le mot `sync` à la place.

### **récupération d'une PR (Pull Request) distante dans le dépôt local**

À des fins de révision et autres, les PR dans le dépôt distant doivent être récupérées dans le dépôt local. Vous pouvez utiliser la commande `git fetch` comme suit pour y parvenir.

`git fetch origin pull/ID/head:BRANCHNAME`

ID est l'identifiant de la pull request et BRANCHNAME est le nom de la branche que vous souhaitez créer. Une fois la branche créée, vous pouvez utiliser `git checkout` pour basculer vers cette branche.

### **Autres ressources sur Git que vous pourriez aimer :**

* [Git merge et Git rebase](https://www.freecodecamp.org/news/the-ultimate-guide-to-git-merge-and-git-rebase/)
* [Git checkout](https://www.freecodecamp.org/news/git-checkout-file-from-another-branch/)
* [Git commit](https://www.freecodecamp.org/news/git-commit-command-explained/)
* [Git stash](https://www.freecodecamp.org/news/git-stash-explained/)
* [Git branch](https://www.freecodecamp.org/news/git-branch-explained-how-to-delete-checkout-create-and-rename-a-branch-in-git/)