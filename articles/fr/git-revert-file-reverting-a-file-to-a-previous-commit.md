---
title: Git Revert File – Restaurer un fichier à un commit précédent
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-18T15:39:20.000Z'
originalURL: https://freecodecamp.org/news/git-revert-file-reverting-a-file-to-a-previous-commit
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pexels-tatiana-fet-1105766.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Revert File – Restaurer un fichier à un commit précédent
seo_desc: 'Git is a version control system that helps teams and individuals track
  and record changes made to a file or an entire project.

  When working with Git, you often commit your changes and then push them to a remote
  repository.

  Suppose you have made a lot...'
---

Git est un système de contrôle de version qui aide les équipes et les individus à suivre et enregistrer les modifications apportées à un fichier ou à un projet entier.

Lorsqu'on travaille avec Git, on commite souvent ses modifications puis on les pousse vers un dépôt distant.

Supposons que vous ayez fait beaucoup de commits et que vous réalisiez plus tard que votre version actuelle des modifications est incorrecte. Ou vous découvrez une situation qui nécessite de revenir à un commit précédent, comme un bug étrange.

Modifier manuellement chaque ligne de code dans votre fichier pour le ramener à son état d'origine ou à un état spécifique de commit et faire un nouveau commit peut conduire à un historique de commits désordonné. Restaurer le fichier est une méthode beaucoup plus propre pour gérer cela.

Il existe de nombreuses approches possibles, mais dans cet article, vous apprendrez la meilleure approche, la méthode `git checkout`.

Si vous êtes pressé, voici la commande :

```bash
$ git checkout SHA-HASH -- fichier/chemin-du-fichier
```

Mais supposons que vous n'êtes pas pressé. Commençons par apprendre comment localiser tous les commits précédents et leurs SHA hash. Ensuite, nous verrons comment restaurer un fichier à un commit précédent.

## Comment trouver le SHA/ID du commit

Il existe de nombreuses façons d'obtenir le SHA et les détails de chaque commit. La meilleure méthode est d'utiliser la commande suivante dans votre terminal :

```bash
$ git log
```

Cette commande affichera une liste de tous les commits que vous avez faits dans vos projets pour tous les fichiers et leurs codes de hachage :

![](https://paper-attachments.dropbox.com/s_E7BE213D0AE03E619B0ABFE8B0450BCDCD832D2BDB3CB303964F1820DADBA52A_1660857327507_image.png align="left")

Mais une commande plus simple à utiliser est la commande suivante, où vous ajoutez l'option `oneline` :

```bash
$ git log --oneline
```

**Note :** L'option `oneline` affiche la sortie comme un commit par ligne.

```bash
198d425 (HEAD -> main) initial
c368a1c new removal
bcbef35 updated readme 2
da9cc5f (origin/main) updated Readme
a5150af first commit
```

L'utilisation de cette commande seule retournerait tous les commits effectués sur ce projet. Si vous souhaitez restaurer un fichier particulier à un commit précédent, vous devez d'abord voir tous les commits effectués sur ce fichier.

Pour ce faire, ajoutez le nom du fichier à la commande :

```bash
$ git log --oneline README.md
```

Dans une situation où le fichier est situé dans un autre dossier, vous pouvez soit naviguer dans votre terminal vers le dossier, soit utiliser le chemin du fichier dans la commande comme vu ci-dessous :

```bash
$ git log --oneline src/App.js
```

Cela retournera uniquement les commits pour le fichier spécifié et le SHA hash du commit suivi du message de commit. Vous utiliserez le SHA hash pour restaurer votre fichier :

```bash
198d425 (HEAD -> main) initial
c368a1c new removal
bcbef35 updated readme 2
da9cc5f (origin/main) updated Readme
a5150af first commit
```

## Comment restaurer un fichier à un commit précédent

Maintenant que vous savez comment obtenir le code SHA, vous pouvez utiliser la commande `git checkout` pour restaurer votre fichier à n'importe quel commit que vous souhaitez en passant également le nom du fichier ou le chemin du fichier :

```bash
$ git checkout da9cc5f -- README.md

Ou

$ git checkout 55a1dff -- src/App.js
```

Assurez-vous simplement de vouloir restaurer un fichier avant de le faire, car vous allez abandonner vos modifications locales actuelles du fichier. Git remplacera le fichier par la version committée spécifiée. Utilisez cela uniquement si vous êtes sûr et ne voulez pas de ces modifications locales non enregistrées.

## Conclusion

Dans cet article, vous avez appris comment restaurer un fichier à un commit précédent avec la commande `git checkout`.

Il est essentiel de savoir que lorsque vous restaurez, vous devrez commiter les modifications à nouveau (les modifications restaurées). Vous pouvez le faire avec la commande de commit standard :

```bash
$ git commit -m 'message de commit'
```

Ensuite, vous pouvez pousser ce commit vers le dépôt distant comme vous le souhaitez.

Vous pouvez en apprendre plus sur Git dans cette [vidéo](https://www.freecodecamp.org/news/git-for-professionals/) ou cet [article](https://www.freecodecamp.org/news/learn-git-and-version-control-in-an-hour/).

Amusez-vous bien à coder !