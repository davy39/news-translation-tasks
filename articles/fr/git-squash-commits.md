---
title: Git Squash Commits – Fusionner les N derniers Commits en un seul Commit
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-22T23:16:43.000Z'
originalURL: https://freecodecamp.org/news/git-squash-commits
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/squashCommits.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Git Squash Commits – Fusionner les N derniers Commits en un seul Commit
seo_desc: "If you are working on a project and trying to implement a new feature,\
  \ you might commit your code a few times to test things out. This lets you see how\
  \ the code works or looks. \nWhile doing this, things might get messy because you\
  \ now have several co..."
---

Si vous travaillez sur un projet et essayez d'implémenter une nouvelle fonctionnalité, vous pourriez Commit votre code quelques fois pour tester les choses. Cela vous permet de voir comment le code fonctionne ou à quoi il ressemble.

En faisant cela, les choses peuvent devenir désordonnées car vous avez maintenant plusieurs Commits, même pour des choses qui ne sont pas nécessaires.

Pour cette raison, vous pourriez vouloir combiner tous ces Commits en un seul Commit. Ce processus est appelé **squashing de Commits**.

Dans cet article, je vais vous montrer comment le squashing de Commits fonctionne dans Git afin que vous puissiez combiner plusieurs Commits désordonnés ou inutiles en un seul Commit sans perdre vos modifications.

## Comment faire un squash de Commits dans Git avec le Rebase interactif
Dans ce processus, vous allez récupérer tous les Commits avec la commande `git rebase` et le flag `i` et les regrouper avec `squash`. En plus du squashing, la commande vous permet également de supprimer des Commits, de reformuler des messages de Commit et d'ajouter de nouveaux fichiers.

J'ai ces Commits que j'aimerais combiner en un seul :

![Screenshot-2023-03-22-at-11.10.52](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.10.52.png)

Notez que j'ai deux branches – `main` et `new-feature`. Je veux faire un squash de tous les Commits de la branche `new-feature` en un seul Commit.

Je peux voir ces Commits parce que j'ai exécuté la commande `git log --oneline`. Ils sont également déjà sur GitHub :

![Screenshot-2023-03-22-at-11.11.23](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.11.23.png)

La première chose que vous devez faire est de dire à Git jusqu'où vous voulez remonter le rebase. Donc, si vous voulez faire un squash de tous ces Commits dans la branche `new-feature` ensemble, vous devez remonter de 6 Commits.

Pour ce faire, exécutez cette commande :

```bash
git rebase -i HEAD~6
```

Cela ouvrira l'éditeur de votre choix pour Git. Le défaut est Vim, mais dans mon cas, c'est VS Code. Voici à quoi ressemble l'éditeur :

![Screenshot-2023-03-22-at-11.28.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.28.12.png)

Maintenant, vous devez remplacer tous ces `pick` par `squash` (ou simplement `s`) à l'exception du premier.

**Note :** `pick` ou `p` utilisera uniquement ces Commits, mais `squash` ou `s` les utilisera et les combinera tous ensemble.

Le premier Commit est celui dans lequel vous les combinerez sans perdre vos modifications.

Après avoir fait cela, enregistrez le fichier et fermez-le. Git ouvrira un autre éditeur où vous pourrez voir le nouveau message de Commit qu'il génère pour vous :

![Screenshot-2023-03-22-at-11.36.02](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.36.02.png)

Vous pouvez tous les supprimer et ajouter votre message personnalisé :

![Screenshot-2023-03-22-at-11.37.45](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.37.45.png)

Ou vous pouvez le laisser tel quel. Si vous ajoutez un nouveau message de Commit, enregistrez le fichier et fermez-le.

Après avoir fait cela, vous devriez voir un message de succès dans le terminal.

Consultez à nouveau votre log Git en exécutant `git log --oneline` et vous devriez voir que tous les Commits ont été combinés :

![Screenshot-2023-03-22-at-11.41.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.41.21.png)

N'oubliez pas que le nouveau message de Commit est \"Ready to deploy\". Si vous poussez votre branche vers Git, vous verrez également un seul message de Commit :

![Screenshot-2023-03-22-at-11.43.07](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.43.07.png)

## Comment faire un squash de Commits dans Git avec la commande `merge` et le flag `--squash` 
Vous pouvez également combiner plusieurs Commits en un seul lorsque vous êtes sur le point de fusionner des branches.

Cela aide à nettoyer la branche entrante des Commits redondants. L'inconvénient de cette approche est que vous n'avez pas autant de contrôle qu'avec `rebase`.

Pour ce faire, je vais annuler le squash que j'ai fait à l'étape précédente en exécutant `git reset --hard HEAD@{7}`.

En exécutant à nouveau `git log --oneline`, je peux voir tous les Commits une fois de plus :

![Screenshot-2023-03-22-at-11.54.06](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.54.06.png)

J'ai de nouveau poussé la branche vers GitHub, donc je peux voir ces Commits là-bas aussi :

![Screenshot-2023-03-22-at-11.56.32](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.56.32.png)

Maintenant, pour faire le squash avec la commande `git merge`, je vais passer à la branche principale en exécutant `git switch main`.

Pour fusionner la branche `new-feature` vers `main` et faire un squash des Commits, j'utiliserai la commande `git merge` avec le flag `--squash` :

```bash
git merge --squash new-feature
```

Si vous exécutez `git log --oneline` à ce stade, vous n'aurez pas encore de Commit sur la branche `new-feature` :

![Screenshot-2023-03-22-at-12.00.25](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.00.25.png)

Mais si vous exécutez `git status`, vous verrez des modifications et des fichiers que vous devez Commit :

![Screenshot-2023-03-22-at-12.01.11](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.01.11.png)

Si vous utilisez VS Code, vous verrez également l'onglet Git indiquant que vous avez des modifications à Commit :

![Screenshot-2023-03-22-at-12.02.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.02.24.png)

Maintenant, commitez les fichiers avec un message approprié. Après cela, exécutez `git log --oneline` et vous verrez votre nouveau message de Commit :

![Screenshot-2023-03-22-at-12.04.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.04.33.png)

Après avoir poussé vers main, créé une pull request sur GitHub et l'avoir fusionnée, voici ce que je vois dans la branche `main` :

![Screenshot-2023-03-22-at-12.09.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.09.12.png)

## Conclusion
Cet article vous a montré comment faire un squash de plusieurs Commits en un seul Commit de deux manières différentes. Peu importe l'option que vous choisissez, l'objectif final de combiner les Commits est atteint.

Si vous voulez avoir plus de contrôle, vous pouvez utiliser l'option `rebase` avec le flag `i`. Mais si vous ne voulez pas passer par ce processus, vous pouvez faire un squash des Commits pendant que vous fusionnez. Soyez simplement conscient qu'avec cette option, vous devez commiter vos modifications à nouveau.

Merci de m'avoir lu. Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille.