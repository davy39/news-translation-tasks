---
title: Le guide ultime de Git Reset et Git Revert
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T17:10:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-git-reset-and-git-revert
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ffc740569d1a4ca45e7.jpg
tags:
- name: Git
  slug: git
seo_title: Le guide ultime de Git Reset et Git Revert
seo_desc: 'Welcome to our ultimate guide to the git reset and git revert commands.
  This tutorial will teach you everything you need to know about fixing common mistakes
  and undoing bad commits while using Git.

  Understand the Three Sections of a Git Project

  A Gi...'
---

Bienvenue dans notre guide ultime des commandes `git reset` et `git revert`. Ce tutoriel vous apprendra tout ce que vous devez savoir pour corriger les erreurs courantes et annuler les mauvais commits lors de l'utilisation de Git.

## Comprendre les trois sections d'un projet Git

Un projet Git comporte les trois sections principales suivantes :

1. Répertoire Git
2. Répertoire de travail (ou arbre de travail)
3. Zone de staging

Le **répertoire Git** (situé dans `YOUR-PROJECT-PATH/.git/`) est l'endroit où Git stocke tout ce dont il a besoin pour suivre précisément le projet. Cela inclut les métadonnées et une base de données d'objets qui contient des versions compressées des fichiers du projet.

Le **répertoire de travail** est l'endroit où un utilisateur apporte des modifications locales à un projet. Le répertoire de travail extrait les fichiers du projet de la base de données d'objets du répertoire Git et les place sur la machine locale de l'utilisateur.

Note : **Directory** est également connu sous le nom de **Repository** ou forme courte repo. Le repo sur la machine locale de l'utilisateur est appelé "Local repo" tandis que le repo sur le serveur git est appelé "Remote repo".

La **zone de staging** est un fichier (également appelé "index", "stage", ou "cache") qui stocke des informations sur ce qui sera inclus dans votre prochain commit. Un commit est lorsque vous dites à Git d'enregistrer ces modifications stagées. Git prend un instantané des fichiers tels qu'ils sont et stocke définitivement cet instantané dans le répertoire Git.

Avec trois sections, il existe trois états principaux qu'un fichier peut avoir à tout moment : modifié, commité ou stagé. Vous _modifiez_ un fichier chaque fois que vous apportez des modifications dans votre répertoire de travail. Ensuite, il est _stagé_ lorsque vous le déplacez vers la zone de staging. Enfin, il est _comité_ après un commit.

## Git Reset

La commande `git reset` vous permet de RESET votre head actuel à un état spécifié. Vous pouvez réinitialiser l'état de fichiers spécifiques ainsi que d'une branche entière. Cela est utile si vous n'avez pas encore poussé votre commit vers GitHub ou un autre dépôt distant.

### Réinitialiser un fichier ou un ensemble de fichiers

La commande suivante vous permet de choisir sélectivement des morceaux de contenu et de les annuler ou de les unstager.

```shell
git reset (--patch | -p) [tree-ish] [--] [paths]
```

### Unstager un fichier

Si vous avez déplacé un fichier dans la zone de staging avec `git add`, mais que vous ne souhaitez plus qu'il fasse partie d'un commit, vous pouvez utiliser `git reset` pour unstager ce fichier :

```shell
git reset HEAD FILE-TO-UNSTAGE
```

Les modifications que vous avez apportées seront toujours dans le fichier, cette commande supprime simplement ce fichier de votre zone de staging.

### Réinitialiser une branche à un commit précédent

La commande suivante réinitialise le HEAD de votre branche actuelle au `COMMIT` donné et met à jour l'index. Elle revient essentiellement à l'état de votre branche, puis tous les commits que vous faites par la suite écrasent tout ce qui est venu après le point de réinitialisation. Si vous omettez le `MODE`, il est par défaut `--mixed` :

```shell
git reset MODE COMMIT
```

Les options pour `MODE` sont :

* `--soft` : ne réinitialise pas le fichier d'index ou l'arbre de travail, mais réinitialise HEAD à `commit`. Modifie tous les fichiers en "Changes to be commited"
* `--mixed` : réinitialise l'index mais pas l'arbre de travail et rapporte ce qui n'a pas été mis à jour
* `--hard` : réinitialise l'index et l'arbre de travail. Toutes les modifications apportées aux fichiers suivis dans l'arbre de travail depuis `commit` sont supprimées
* `--merge` : réinitialise l'index et met à jour les fichiers dans l'arbre de travail qui sont différents entre `commit` et HEAD, mais conserve ceux qui sont différents entre l'index et l'arbre de travail
* `--keep` : réinitialise les entrées d'index et met à jour les fichiers dans l'arbre de travail qui sont différents entre `commit` et HEAD. Si un fichier qui est différent entre `commit` et HEAD a des modifications locales, la réinitialisation est abandonnée

### Note importante sur les réinitialisations hard

Soyez très prudent lorsque vous utilisez l'option `--hard` avec `git reset` car elle réinitialise votre commit, la zone de staging et votre répertoire de travail. Si cette option n'est pas utilisée correctement, on peut finir par perdre le code qui est écrit.

## Git Revert

Les commandes `git revert` et `git reset` annulent les commits précédents. Mais si vous avez déjà poussé votre commit vers un dépôt distant, il est recommandé de ne pas utiliser `git reset` car il réécrit l'historique des commits. Cela peut rendre le travail sur un dépôt avec d'autres développeurs et le maintien d'un historique cohérent des commits très difficile.

Au lieu de cela, il est préférable d'utiliser `git revert`, qui annule les modifications apportées par un commit précédent en créant un tout nouveau commit, tout cela sans altérer l'historique des commits.

### Annuler un commit ou un ensemble de commits

La commande suivante vous permet d'annuler les modifications d'un commit précédent ou de plusieurs commits et de créer un nouveau commit.

```shell
git revert [--[no-]edit] [-n] [-m parent-number] [-s] [-S[<keyid>]] <commit>…
git revert --continue
git revert --quit
git revert --abort
```

### Options courantes :

```shell
  -e
  --edit
```

* Il s'agit de l'option par défaut et elle n'a pas besoin d'être définie explicitement. Elle ouvre l'éditeur de texte par défaut de votre système et vous permet de modifier le message du nouveau commit avant de valider l'annulation.
* Cette option fait l'inverse de `-e`, et `git revert` n'ouvrira pas l'éditeur de texte.
* Cette option empêche `git revert` d'annuler un commit précédent et d'en créer un nouveau. Au lieu de créer un nouveau commit, `-n` annulera les modifications du commit précédent et les ajoutera à l'Index de Staging et au Répertoire de Travail.

```shell
  --no-edit
```

```shell
-n
--no-commit
```

### Exemple.

Imaginons la situation suivante : 1.) Vous travaillez sur un fichier et vous ajoutez et validez vos modifications. 2.) Vous travaillez ensuite sur quelques autres choses et faites quelques autres commits. 3.) Maintenant, vous réalisez que, il y a trois ou quatre commits, vous avez fait quelque chose que vous aimeriez annuler - comment pouvez-vous faire cela ?

Vous pourriez penser à utiliser `git reset`, mais cela supprimera tous les commits après celui que vous souhaitez modifier - `git revert` à la rescousse ! Passons en revue cet exemple :

```shell
mkdir learn_revert # Crée un dossier appelé `learn_revert`
cd learn_revert # `cd` dans le dossier `learn_revert`
git init # Initialise un dépôt git

touch first.txt # Crée un fichier appelé `first.txt`
echo Start >> first.txt # Ajoute le texte "Start" à `first.txt`

git add . # Ajoute le fichier `first.txt`
git commit -m "adding first" # Valide avec le message "Adding first.txt"

echo WRONG > wrong.txt # Ajoute le texte "WRONG" à `wrong.txt`
git add . # Ajoute le fichier `wrong.txt`
git commit -m "adding WRONG to wrong.txt" # Valide avec le message "Adding WRONG to wrong.txt"

echo More >> first.txt # Ajoute le texte "More" à `first.txt`
git add . # Ajoute le fichier `first.txt`
git commit -m "adding More to first.txt" # Valide avec le message "Adding More to first.txt"

echo Even More >> first.txt # Ajoute le texte "Even More" à `first.txt`
git add . # Ajoute le fichier `first.txt`
git commit -m "adding Even More to First.txt" # Valide avec le message "Adding More to first.txt"

# OH NON ! Nous voulons annuler le commit avec le texte "WRONG" - annulons-le ! Comme ce commit était à 2 commits de notre position actuelle, nous pouvons utiliser git revert HEAD~2 (ou nous pouvons utiliser git log et trouver le SHA de ce commit)

git revert HEAD~2 # cela nous placera dans un éditeur de texte où nous pourrons modifier le message de commit.

ls # wrong.txt n'est plus là !
git log --oneline # notez que l'historique des commits n'a pas été altéré, nous avons simplement ajouté un nouveau commit reflétant la suppression du `wrong.txt`
```

Et avec cela, vous êtes un pas de plus vers l'obtention de votre ceinture noire en Git.