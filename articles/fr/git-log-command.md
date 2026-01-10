---
title: Commande Git Log Expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T00:20:00.000Z'
originalURL: https://freecodecamp.org/news/git-log-command
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dfc740569d1a4ca3abd.jpg
tags:
- name: Git
  slug: git
seo_title: Commande Git Log Expliquée
seo_desc: 'What does git log do?

  The git log command displays all of the commits in a repository’s history.

  By default, the command displays each commit’s:


  Secure Hash Algorithm (SHA)

  author

  date

  commit message


  Navigating Git Log

  Git uses the Less terminal pa...'
---

## **Que fait git log ?**

La commande `git log` affiche tous les commits de l'historique d'un dépôt.

Par défaut, la commande affiche pour chaque commit :

* Secure Hash Algorithm (SHA)
* auteur
* date
* message de commit

## Naviguer dans Git Log

Git utilise le pagineur de terminal Less pour parcourir l'historique des commits. Vous pouvez le naviguer avec les commandes suivantes :

* pour descendre d'une ligne, utilisez j ou [B
* pour monter d'une ligne, utilisez k ou [A
* pour descendre d'une page, utilisez la barre d'espace ou le bouton Page Down
* pour monter d'une page, utilisez b ou le bouton Page Up
* pour quitter le log, utilisez q

## Drapeaux de Git Log

Vous pouvez personnaliser les informations présentées par `git log` en utilisant des drapeaux.

### --oneline

`git log --oneline`

Le drapeau `--oneline` fait en sorte que `git log` affiche

* un commit par ligne
* les sept premiers caractères du SHA
* le message de commit

### --stat

`git log --stat`

Le drapeau `--stat` fait en sorte que `git log` affiche

* les fichiers qui ont été modifiés dans chaque commit
* le nombre de lignes ajoutées ou supprimées
* une ligne de résumé avec le nombre total de fichiers et de lignes modifiés

### --patch ou -p

`git log --patch`

ou, la version plus courte

`git log -p`

Le drapeau `--patch` fait en sorte que `git log` affiche

* les fichiers que vous avez modifiés
* l'emplacement des lignes que vous avez ajoutées ou supprimées
* les changements spécifiques que vous avez apportés

## Voir un nombre spécifié de commits par auteur

Pour voir un nombre spécifié de commits par un auteur dans le dépôt actuel (optionnellement dans un format préttifié), la commande suivante peut être utilisée

`git log --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" -n {NUMBER_OF_COMMITS} --author="{AUTHOR_NAME}" --all`

### Commencer à un commit spécifique

Pour commencer `git log` à un commit spécifique, ajoutez le SHA :

`git log 7752b22`

Cela affichera le commit avec le SHA 7752b22 et tous les commits faits avant ce commit. Vous pouvez combiner cela avec n'importe quel autre drapeau.

### --graph

`git log --graph`

Le drapeau `--graph` vous permet de voir votre `git log` sous forme de graphique. Pour rendre les choses intéressantes, vous pouvez combiner cette commande avec l'option `--oneline` que vous avez apprise ci-dessus.

`git log --graph --oneline`

La sortie serait similaire à,

```text
* 64e6db0 Update index.md
* b592012 Update Python articles (#5030)
* ecbf9d3 Add latest version and remove duplicate link (#8860)
* 7e3934b Add hint for Compose React Components (#8705)
* 99b7758 Added more frameworks (#8842)
* c4e6a84 Add hint for "Create a Component with Composition" (#8704)
*   907b004 Merge branch 'master' of github.com:freeCodeCamp/guide
|\  
| * 275b6d1 Update index.md
* |   cb74308 Merge branch 'dogb3rt-patch-3'
|\ \  
| |/  
|/|   
| *   98015b6 fix merge conflicts after folder renaming
| |\  
|/ /  
| * fa83460 Update index.md
* | 6afb3b5 rename illegally formatted folder name (#8762)
* | 64b1fe4 CSS3: border-radius property (#8803)
```

L'un des avantages de l'utilisation de cette commande est qu'elle vous permet d'obtenir un aperçu de la manière dont les commits ont été fusionnés et de la manière dont l'historique git a été créé.

Il existe de nombreuses autres options que vous pourriez utiliser en combinaison avec `--graph`. Parmi elles, `--decorate` et `--all`. Assurez-vous de les essayer également. Et vous pouvez vous référer à la [documentation](https://git-scm.com/docs/git-log) pour plus d'informations utiles.

### Plus d'informations :

* [Git Basics - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
* [Git Log](https://git-scm.com/docs/git-log)

## **Autres ressources sur Git** 

* [Git Checkout](https://www.freecodecamp.org/news/git-checkout-explained/)
* [Git Commit](https://www.freecodecamp.org/news/git-commit-command-explained/)
* [Git Stash](https://www.freecodecamp.org/news/git-stash-explained/)
* [Git Branch](https://www.freecodecamp.org/news/git-delete-branch-how-to-remove-a-local-or-remote-branch/)