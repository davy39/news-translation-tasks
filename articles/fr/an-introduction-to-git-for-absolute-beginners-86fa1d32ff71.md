---
title: Git pour les débutants absolus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-06T17:04:28.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-git-for-absolute-beginners-86fa1d32ff71
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TnsFDs-DEye722CrQXjv8w.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: version control
  slug: version-control
- name: Web Development
  slug: web-development
seo_title: Git pour les débutants absolus
seo_desc: 'By Shahzan

  If you’re new to the programming world, then learning Git should be something on
  top of your priority list.

  Git is one such tool which you will encounter on a day-to-day basis as part of your
  job.

  What you can expect in this post

  In this p...'
---

Par Shahzan

Si vous êtes nouveau dans le monde de la programmation, alors apprendre Git devrait être quelque chose en haut de votre liste de priorités.

Git est un outil que vous rencontrerez au quotidien dans le cadre de votre travail.

#### Ce à quoi vous pouvez vous attendre dans cet article

Dans cet article, je vais donner un aperçu de Git et comment commencer à l'utiliser.

* Qu'est-ce que Git ?
* Terminologies associées à Git
* Interagir avec Git en utilisant la ligne de commande

Je promets d'expliquer les sujets de la manière la plus simplifiée possible.

#### Alors commençons par comprendre, qu'est-ce que Git ?

Git est un système de contrôle de version.

#### Maintenant, qu'est-ce qu'un système de contrôle de version (VCS) ?

Un VCS surveille et suit toutes les modifications apportées aux fichiers qui sont surveillés par lui.

Il permet également à plusieurs développeurs de partager et de travailler collaborativement sur le même ensemble de fichiers, sans entrer en conflit avec le travail des autres.

Il ne suit pas seulement quels fichiers ont été modifiés, mais il suit également

* Quels changements ont été faits ?
* Qui a fait ces changements ?
* Quand ces changements ont été faits.

Pour que vous puissiez partager et travailler collaborativement avec d'autres développeurs, vous avez besoin d'un accès à un service hébergé basé sur Git.

Certains des fournisseurs de services hébergés Git populaires sont :

* [GitHub](https://github.com/)
* [Bitbucket](https://bitbucket.org/)
* [Microsoft Visual Studio Team Services](https://visualstudio.microsoft.com/team-services/)

Tous offrent un type de fonctionnalité similaire.

#### Qu'est-ce qu'un dépôt dans Git ?

Un **_dépôt_** est un dossier dont le contenu est suivi par Git. Il est également connu sous le nom de **_repo_**, en termes simples.

Un dépôt peut avoir plusieurs fichiers et sous-dossiers présents dans celui-ci. Habituellement, les fichiers présents dans le dépôt contiennent du code source.

Dans chaque dépôt, il y a un **_dossier .git_**. Ce dossier contient tous les fichiers et dossiers nécessaires à Git pour suivre toutes les modifications apportées aux fichiers dans ce dépôt.

Si nous supprimons ce dossier .git, Git n'identifiera pas ce dossier comme un dépôt ni ne suivra son contenu.

Le dépôt présent sur l'ordinateur local est appelé **_dépôt local_**, et le dépôt situé sur une plateforme Git hébergée est appelé **_dépôt distant_**. 

#### Télécharger et installer Git

Télécharger et installer Git est un processus assez simple.

Vous pouvez [télécharger Git ici](https://git-scm.com/downloads).

Une fois Git téléchargé, [vous pouvez vous référer à ce guide sur la façon de l'installer](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

#### Initialiser un dépôt Git

Avant de commencer à suivre nos fichiers avec Git, nous devons initialiser Git pour le dossier que nous voulons que Git surveille.

En termes simples, Git convertit un dossier en un dépôt afin que son contenu puisse être suivi par lui.

Pour initialiser un dossier en un dépôt Git :

Sur un système basé sur Windows, nous devons **_cliquer avec le bouton droit sur le dossier_** (que nous aimerions voir suivi par Git), puis cliquer sur **_Git Bash Here_**. Cela ouvre une fenêtre de type invite de commande, qui nous permet d'interagir avec Git en utilisant les commandes Git.

> **Note :** Chaque fois que nous souhaitons interagir avec Git, nous interagirons en utilisant les commandes Git via cette fenêtre Git Bash. Notez également que les commandes Git ne diffèrent pas pour les systèmes Windows et Unix.

Dans la fenêtre Git Bash, nous devons taper la commande :

```bash
git init
```

Cette commande initialise le dossier. En gros, elle convertit ce dossier en un dépôt Git.

Dans le cadre de ce processus d'initialisation, il crée également un dossier .git (qui est un dossier caché) dans ce dépôt. Celui-ci contient tous les fichiers nécessaires à Git pour suivre toutes les modifications apportées à ce dépôt.

Mais ce n'est qu'un dossier normal comme les autres dossiers que nous avons sur le système. En terminologie Git, nous l'appelons toujours un dépôt ou un dépôt local, pour être plus précis.

Sur un système basé sur Unix, nous naviguons simplement vers le répertoire (que vous aimeriez voir suivi par Git), et exécutons la commande **git init**, c'est tout. Cela convertit ce répertoire en un dépôt Git.

#### Statut du dépôt

À tout moment, si nous voulons voir ce qui est suivi par Git dans un dépôt, nous pouvons le faire en tapant la commande ci-dessous :

```bash
git status
```

Nous examinerons cette commande plus en détail à un moment donné plus tard dans l'article.

Pour l'instant, retenez simplement que si nous voulons voir ce qui est suivi dans un dépôt par Git, nous pouvons le faire en utilisant cette commande.

#### Suivi d'un dépôt

Même si nous avons initialisé le dossier en tant que dépôt Git, son contenu ne sera pas suivi automatiquement. Nous devons indiquer à Git de surveiller son contenu.

Pour ce faire, nous utilisons la commande **git add**. La syntaxe de cette commande est la suivante :

```bash
git add fichier [fichier] [fichier..]
```

> Note : Tout ce qui est enfermé dans des crochets _[]_ est facultatif. Cela s'applique à toutes les commandes Git répertoriées dans cet article.

Nous pouvons spécifier un seul fichier ou plusieurs fichiers à suivre par Git.

Si nous voulons que Git surveille des fichiers spécifiques présents dans le dépôt, nous pouvons le faire en spécifiant le nom de fichier individuel de chaque fichier que nous aimerions suivre.

Au cas où nous voulons suivre des fichiers appartenant à un type de fichier spécifique, nous pouvons le faire en spécifiant son extension de fichier, comme indiqué ci-dessous. Cela suit tous les fichiers se terminant par l'extension .txt.

```bash
$ git add *.txt
```

Si nous voulons que Git suive tous les fichiers présents dans le dépôt, la syntaxe est la suivante.

```bash
$ git add .
```

Supposons que nous avons les fichiers suivants présents dans notre dépôt :

![Image](https://cdn-media-1.freecodecamp.org/images/Z2s9Bni4O-19bASIGpay70eaDx-yNWHRK9Mi)

Comme vous pouvez le voir, même le dossier .git a été créé dans le cadre du processus d'initialisation. À l'origine, ce dossier était caché — j'ai dû changer les propriétés du dossier pour le rendre visible (juste pour vous le montrer à tous).

Voici à quoi ressemble un dossier .git, immédiatement après l'exécution de la commande git init.

![Image](https://cdn-media-1.freecodecamp.org/images/kKznhad2RUFHV62YbjoWh6c-zvzIGoliSykk)

Voici à quoi ressemblent les contenus du dossier .git après que quelques transactions ont été effectuées sur le dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/UGbIpgCGjcID7R2xJNP4d8hdjx8f5ibGnlj3)

Pour vérifier quels fichiers sont actuellement suivis par Git, nous pouvons utiliser la commande git status :

```bash
$ git status
On branch master

No commits yet

Untracked files:
 (use git add <file> to include in what will be committed)
 
HelloWorld.html
 Notes.txt
 README.md
 
nothing added to commit but untracked files present (use git add to track)
```

En regardant la sortie de la commande **git status**, elle indique qu'aucun des fichiers n'est actuellement suivi par Git.

Allons-y et ajoutons ces fichiers afin qu'ils soient suivis par Git.

La commande pour ajouter ces fichiers est la suivante :

```bash
$ git add HelloWorld.html Notes.txt
```

Maintenant, exécutons la commande git status et vérifions sa sortie.

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
 (use git rm  cached <file> to unstage)
 
new file: HelloWorld.html
 new file: Notes.txt
 
Untracked files:
 (use git add <file> to include in what will be committed)
 
README.md
```

Comme nous pouvons le voir, nous avons les fichiers `HelloWorld.txt` et `Notes.txt` présents dans la zone de staging qui attendent d'être validés.

Le fichier `README.md` n'est pas du tout suivi, car nous n'avons pas inclus ce fichier dans la commande git add que nous avons exécutée précédemment.

Lorsque nous avons exécuté la commande git add, Git a mis en staging tous les fichiers qui ont été spécifiés dans l'entrée de cette commande.

Jusqu'à ce que nous validions ces fichiers, Git ne commencera pas à suivre ces fichiers.

#### Valider les fichiers en staging

Validons ces fichiers en staging en tapant la commande montrée ci-dessous.

```bash
$ git commit -m Initial Commit
```

git commit est la commande utilisée pour valider les fichiers en staging, -m est utilisé pour spécifier les commentaires pour cette opération de validation.

Si nous voulons voir toutes les opérations de validation qui ont été effectuées, nous pouvons le faire en tapant la commande git log, comme montré ci-dessous.

```bash
$ git log

commit 8525b32ffcb92c731f5d04de7fe285a2d0ebe901 (HEAD -> master)

Author: shahzan <sxxxxxxn@gmail.com>

Date: Sun Apr 28 01:12:20 2019 +0100

Initial Commit
```

Chaque fois qu'un changement est fait à un fichier qui est suivi par Git, nous devons re-stager ces fichiers et les re-valider. Jusqu'à ce que ces fichiers ne soient pas re-stagés et re-validés, ils seront suivis par Git.

J'ai fait quelques modifications mineures au fichier Notes.txt, voyons ce que Git a à dire sur ces changements en exécutant la commande git status.

```bash
$ git status

On branch master

Changes not staged for commit:

(use git add <file> to update what will be committed)

(use git checkout  <file> to discard changes in working directory)

modified: Notes.txt

Untracked files:

(use git add <file> to include in what will be committed)

README.md

no changes added to commit (use git add and/or git commit -a)
```

En regardant le bloc de sortie ci-dessus, il est clair que le fichier `Notes.txt` a été modifié et que les changements ne sont pas en staging pour la validation.

Nous utilisons la même commande git add pour re-stager le fichier.

```bash
$ git add Notes.txt

Shahzan@BlackBox MINGW64 /d/Medium Post Pics/Git/Source Code (master)

$ git status

On branch master

Changes to be committed:

(use git reset HEAD <file> to unstage)

modified: Notes.txt

Untracked files:

(use git add <file> to include in what will be committed)

README.md
```

Comme vous pouvez le remarquer dans le bloc de sortie ci-dessus, le fichier a été mis en staging et attend d'être validé.

Encore une fois, nous utilisons la même commande git commit pour re-valider le fichier en staging.

```bash
$ git commit -m Notes.txt file updated

[master 184fcad] Notes.txt file updated

1 file changed, 3 insertions(+), 1 deletion(-)
```

Exécutons la commande git log et voyons si la validation a été réussie.

```bash
$ git log

commit 184fcad4185296103cd9dba0da83520399a11383 (HEAD -> master)

Author: shahzans <shuaib.shahzan@gmail.com>

Date: Sun Apr 28 01:15:38 2019 +0100

Notes.txt file updated

commit 8525b32ffcb92c731f5d04de7fe285a2d0ebe901

Author: shahzans <shuaib.shahzan@gmail.com>

Date: Sun Apr 28 01:12:20 2019 +0100

Initial Commit
```

Comme vous pouvez le remarquer dans le bloc de sortie ci-dessus, les deux opérations de validation sont affichées.

#### Ignorer les fichiers

Dans le dépôt, il peut y avoir des fichiers qui contiennent des données sensibles ou des données de journalisation, que nous ne voulons pas voir suivis par Git en aucune circonstance.

.gitignore est le fichier dans lequel nous pouvons spécifier tous les fichiers que nous ne voulons pas que Git suive.

```bash
$ touch .gitignore
```

La syntaxe pour créer ce fichier est comme indiqué ci-dessus.

Supposons que je ne veux pas que Git suive un fichier se terminant par l'extension .md.

Avant d'ajouter *.md au fichier .gitignore, jetez un coup d'œil à la sortie de la commande git status comme montré dans le bloc de sortie ci-dessous.

```bash
$ git status

On branch master

Untracked files:

(use git add <file> to include in what will be committed)

.gitignore

README.md

nothing added to commit but untracked files present (use git add to track)
```

Comme vous pouvez le remarquer, nous avons `.gitignore` et `README.md` qui sont affichés comme des fichiers non suivis.

Après avoir ajouté *.md au fichier .gitignore, le statut git est comme montré dans le bloc de sortie ci-dessous.

Comme vous pouvez le remarquer, nous n'avons maintenant que .gitignore qui est affiché comme un fichier non suivi.

```bash
$ git status

On branch master

Untracked files:

(use git add <file> to include in what will be committed)

.gitignore

nothing added to commit but untracked files present (use git add to track)
```

Vous pouvez spécifier un nom de fichier individuel ou une entrée générique dans le fichier .gitignore.

#### **Conclusion**

Git est un outil très puissant et il y a beaucoup plus de choses que vous pouvez faire avec lui, comme le branchement, la fusion, les demandes de pull et push et bien plus encore.

Au cas où vous seriez intéressé à en apprendre plus sur Git, [voici un cours que je vous recommande de suivre](http://bit.ly/git-complete) (lien d'affiliation).

### Avant de dire au revoir...

Restez en contact, [cliquez ici pour entrer votre adresse e-mail](https://forms.gle/3U1uBNEC4mDkSpMJ7) (Utilisez ce lien si le widget ci-dessus ne s'affiche pas sur votre écran).

Merci beaucoup d'avoir pris votre temps précieux pour lire cet article.