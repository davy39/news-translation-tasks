---
title: Apprendre les bases de Git en moins de 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T17:15:44.000Z'
originalURL: https://freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4kDk9CZEEJBllqd3Fx549A.png
tags:
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: version control
  slug: version-control
seo_title: Apprendre les bases de Git en moins de 10 minutes
seo_desc: 'By Gowtham Venkatesan

  Yes, the title is a clickbait. There is no way you can understand the basics of
  git technology in just 10 minutes. But you can get pretty close in about 25 minutes.
  And that is the purpose of this article.

  If you want to get sta...'
---

Par Gowtham Venkatesan

Oui, le titre est un appât à clics. Il n'y a aucun moyen de vraiment _comprendre_ les bases de la technologie git en seulement 10 minutes. Mais vous pouvez vous en approcher en environ 25 minutes. Et c'est le but de cet article.

Si vous voulez commencer à apprendre la technologie Git, vous êtes au bon endroit. Ceci est un guide complet pour les débutants sur Git. Il existe de nombreux clients pour Git. La technologie est la même peu importe le client. Mais dans ce guide, nous utiliserons GitHub pour comprendre Git.

#### Commençons !

### Qu'est-ce que le contrôle de version ?

> Le contrôle de version est un système qui enregistre les modifications apportées à un fichier ou à un ensemble de fichiers au fil du temps, afin que vous puissiez rappeler des versions spécifiques plus tard. Idéalement, nous pouvons placer n'importe quel fichier de l'ordinateur sous contrôle de version.

#### Euh... D'accord... Mais pourquoi ?

#### Voici pourquoi :

Un système de contrôle de version (VCS) vous permet de restaurer des fichiers à un état précédent, de restaurer l'ensemble du projet à un état précédent, de revoir les modifications apportées au fil du temps, de voir qui a modifié quelque chose qui pourrait causer un problème, qui a introduit un problème et quand, et plus encore. L'utilisation d'un VCS signifie également que si vous faites des erreurs ou perdez des fichiers, vous pouvez généralement les récupérer facilement. Et parfois, vous voulez simplement savoir **"qui a écrit ce code pourri"**, et avoir accès à cette information en vaut la peine ?.

### Alors, qu'est-ce que Git ?

Git est un système de contrôle de version pour suivre les modifications des fichiers informatiques et coordonner le travail sur ces fichiers entre plusieurs personnes. Git est un **_Système de Contrôle de Version Distribué_**. Ainsi, Git ne dépend pas nécessairement d'un serveur central pour stocker toutes les versions des fichiers d'un projet. Au lieu de cela, chaque utilisateur "clone" une copie d'un dépôt (une collection de fichiers) et a l'**_historique complet_** du projet sur son propre disque dur. Ce clone contient _toutes_ les métadonnées de l'original tandis que l'original lui-même est stocké sur un serveur auto-hébergé ou un service d'hébergement tiers comme GitHub.

Git vous aide à **_suivre les modifications_** que vous apportez à votre code. C'est essentiellement l'historique de votre éditeur de code (sans mode incognito ?). Si à un moment donné lors du codage vous rencontrez une erreur fatale et ne savez pas ce qui la cause, vous pouvez toujours revenir à l'état stable. C'est donc très utile pour le débogage. Ou vous pouvez simplement voir quelles modifications vous avez apportées à votre code au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lp_67l9zwur7aaFAhpVDrg.png)
_Un exemple simple de l'historique des versions d'un fichier._

Dans l'exemple ci-dessus, les trois cartes représentent différentes versions du même fichier. Nous pouvons sélectionner quelle version du fichier nous voulons utiliser à tout moment. Je peux donc sauter d'une version à l'autre du fichier dans le continuum temporel de git.

Git vous aide également à **_synchroniser le code_** entre plusieurs personnes. Imaginez donc que vous et votre ami collaborez sur un projet. Vous travaillez tous les deux sur les mêmes fichiers de projet. Maintenant, Git prend les modifications que vous et votre ami avez faites indépendamment et les fusionne dans un seul dépôt "**Master**". Ainsi, en utilisant Git, vous pouvez vous assurer que vous travaillez tous les deux sur la version la plus récente du dépôt. Vous n'avez donc pas à vous soucier d'envoyer vos fichiers par email et de travailler avec un nombre ridicule de copies du fichier original. Et collaborer à distance devient aussi facile que le HTML ?.

### Flux de travail Git :

Avant de commencer à travailler avec les commandes Git, il est nécessaire que vous compreniez ce qu'elles représentent.

#### Qu'est-ce qu'un dépôt ?

Un **dépôt** alias **repo** n'est rien d'autre qu'une collection de code source.

#### Il y a quatre éléments fondamentaux dans le flux de travail Git.

**Répertoire de travail**, **Zone de préparation**, **Dépôt local** et **Dépôt distant**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iL2J8k4ygQlg3xriKGimbQ.png)
_Diagramme d'un flux de travail Git simple_

**Si vous considérez un fichier dans votre répertoire de travail, il peut être dans trois états possibles.**

1. **Il peut être préparé.** Ce qui signifie que les fichiers avec les modifications mises à jour sont marqués pour être validés dans le dépôt local mais pas encore validés.
2. **Il peut être modifié.** Ce qui signifie que les fichiers avec les modifications mises à jour ne sont pas encore stockés dans le dépôt local.
3. **Il peut être validé.** Ce qui signifie que les modifications que vous avez apportées à votre fichier sont stockées en toute sécurité dans le dépôt local.

* `git add` est une commande utilisée pour ajouter un fichier qui se trouve dans le répertoire de travail à la zone de préparation.
* `git commit` est une commande utilisée pour ajouter tous les fichiers qui sont préparés au dépôt local.
* `git push` est une commande utilisée pour ajouter tous les fichiers validés dans le dépôt local au dépôt distant. Ainsi, dans le dépôt distant, tous les fichiers et modifications seront visibles pour toute personne ayant accès au dépôt distant.
* `git fetch` est une commande utilisée pour obtenir des fichiers du dépôt distant vers le dépôt local mais pas dans le répertoire de travail.
* `git merge` est une commande utilisée pour obtenir les fichiers du dépôt local dans le répertoire de travail.
* `git pull` est une commande utilisée pour obtenir des fichiers du dépôt distant directement dans le répertoire de travail. C'est équivalent à un `git fetch` et un `git merge`.

**Maintenant que nous savons ce qu'est Git et ses terminologies de base, voyons comment nous pouvons placer un fichier sous git**. Nous allons le faire de la bonne manière et de la manière difficile. Sans aucune application GUI.

Je suppose que vous avez déjà un fichier que vous voulez placer sous contrôle de version. Sinon, créez un dossier d'exemple nommé 'MuskCult' et placez-y quelques fichiers de code d'exemple.

### Étape 0 : Créez un compte GitHub. Évidemment.

Si vous n'en avez pas déjà un, vous pouvez en créer un [ici](https://github.com/join).

### Étape 1 : Assurez-vous d'avoir Git installé sur votre machine.

Si vous êtes sur un **Mac**, lancez le terminal et entrez la commande suivante :

```
$ git --version
```

Cela ouvrira un installateur si vous n'avez pas déjà git. Installez-le donc en utilisant l'installateur. Si vous avez déjà git, il vous montrera simplement quelle version de git vous avez installée.

Si vous utilisez **Linux** (deb), entrez ce qui suit dans le terminal :

```
$ sudo apt install git-all
```

Si vous êtes sur **Windows** :

```
$ get a mac
```

Je plaisante... Détendez-vous... Le nombre de personnes que j'ai déclenchées... Ouf...
Allez sur ce [**lien**](https://www.apple.com/macos/what-is/) ou ce [lien](https://gitforwindows.org/) pour plus d'informations sur la façon de l'obtenir.

### Étape 2 : Dites à Git qui vous êtes.

Présentez-vous. Glissez-vous. Sérieusement, mentionnez votre nom d'utilisateur Git et votre adresse email, car chaque commit Git utilisera ces informations pour vous identifier comme l'auteur.

```
$ git config --global user.name "VOTRE_NOM_DUTILISATEUR"

$ git config --global user.email "je_suis_satoshi@musk.com"

$ git config --global --list # Pour vérifier les informations que vous venez de fournir
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JbyUdhLMEdglRxQk6PH7Vg.gif)

### Étape 3 : Générez/vérifiez votre machine pour les clés SSH existantes. (Facultatif)

Pourquoi demandez-vous ? En utilisant le **protocole SSH**, vous pouvez **vous connecter et vous authentifier** aux **serveurs et services distants**. Avec les clés SSH, vous pouvez vous connecter à GitHub sans fournir votre nom d'utilisateur ou votre mot de passe à chaque visite.

Suivez ce [lien](https://help.github.com/articles/about-ssh/) pour en savoir plus sur SSH.
Allez [**ici**](https://help.github.com/articles/checking-for-existing-ssh-keys/) pour vérifier si vous avez une clé SSH existante.
Allez [**ici**](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) pour générer une clé SSH.
Allez [**ici**](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) pour ajouter la clé SSH à votre compte GitHub.
Et enfin, allez [**ici**](https://help.github.com/articles/testing-your-ssh-connection/) pour tester sa connexion.

Si vous avez configuré SSH, chaque commande git qui a un lien, vous la remplacez par :

```
Au lieu de : https://github.com/username/reponame

Vous utilisez : git@github.com:username/reponame.git

           Remarque : Vous pouvez utiliser les deux méthodes alternativement
```

**J'utiliserai le protocole SSH dans ce tutoriel.**

### Étape 4 : Utilisons Git

Créez un nouveau dépôt sur GitHub. Suivez ce [lien](https://github.com/new).
Maintenant, localisez le dossier que vous voulez placer sous git dans votre terminal.

```
$ cd Desktop/MuskCult
```

#### Initialiser Git :

Et pour le placer sous git, entrez :

```
$ touch README.md    # Pour créer un fichier README pour le dépôt
$ git init           # Initialise un dépôt git vide
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q_DUXRghgFQb9F47mUB6LQ.gif)

Maintenant, allez modifier le fichier README.md pour fournir des informations sur le dépôt.

#### Ajouter des fichiers à la zone de préparation pour le commit :

Maintenant, pour ajouter les fichiers au dépôt git pour le commit :

```
$ git add .  
# Ajoute tous les fichiers dans le dépôt local et les prépare pour le commit

OU si vous voulez ajouter un fichier spécifique

$ git add README.md 
# Pour ajouter un fichier spécifique
```

#### Avant de commiter, voyons quels fichiers sont préparés :

```
$ git status # Liste tous les nouveaux fichiers ou modifiés à commiter
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*a2_hw7cMe2R9R_aI86dB-A.gif)

#### Commiter les modifications que vous avez apportées à votre dépôt Git :

Maintenant, pour commiter les fichiers que vous avez ajoutés à votre dépôt git :

```
$ git commit -m "Premier commit"
# Le message dans les " " est donné afin que les autres utilisateurs puissent lire le message et voir quelles modifications vous avez apportées
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*LoUwFy29RkgCS7hCajd_3g.gif)

#### Annuler les modifications que vous venez de faire à votre dépôt Git :

Maintenant, supposons que vous venez de faire une erreur dans votre code ou que vous avez placé un fichier indésirable dans le dépôt, vous pouvez annuler les fichiers que vous venez d'ajouter en utilisant :

```
$ git reset HEAD~1
# Supprime le commit le plus récent
# Commitez à nouveau !
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rxOX_U-ZRmGfhgIhNWlDIQ.gif)

#### Ajouter une origine distante et pousser :

Maintenant, chaque fois que vous faites des modifications dans vos fichiers et que vous les enregistrez, elles ne seront pas automatiquement mises à jour sur GitHub. Toutes les modifications que nous avons faites dans le fichier sont mises à jour dans le dépôt local. Maintenant, pour mettre à jour les modifications dans le master :

```
$ git remote add origin URL_du_dépôt_distant
# définit la nouvelle origine distante
```

La commande **git remote** vous permet de créer, de voir et de supprimer des connexions à d'autres dépôts.

```
$ git remote -v
# Liste les connexions distantes que vous avez avec d'autres dépôts.
```

La commande **git remote -v** liste les URLs des connexions distantes que vous avez avec d'autres dépôts.

```
$ git push -u origin master # pousse les modifications vers l'origine
```

Maintenant, la commande **git push** pousse les modifications de votre dépôt local vers le dépôt distant que vous avez spécifié comme origine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w-nfopsKIks_JRzFe5D8xA.gif)

Et maintenant, si nous allons vérifier notre page de dépôt sur GitHub, elle devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aQljQFkytY84BgmlVtpgmw.png)

Et c'est tout. Vous venez d'ajouter les fichiers au dépôt que vous venez de créer sur GitHub.

#### Voir les modifications que vous avez apportées à votre fichier :

Une fois que vous commencez à faire des modifications sur vos fichiers et que vous les enregistrez, le fichier ne correspondra pas à la dernière version qui a été commise dans git. Pour voir les modifications que vous venez de faire :

```
$ git diff # Pour montrer les modifications des fichiers non encore préparées
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*xym1QvvvWorfoyGMXv28Yg.gif)

#### Revenir à la dernière version commise dans le dépôt Git :

Maintenant, vous pouvez choisir de revenir à la dernière version commise en entrant :

```
$ git checkout .

OU pour un fichier spécifique

$ git checkout -- <nom_du_fichier>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYgYkfo3W4MUA8CJl12rXg.gif)

#### Voir l'historique des commits :

Vous pouvez utiliser la commande **git log** pour voir l'historique des commits que vous avez faits sur vos fichiers :

```
$ git log
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*9w7uBJcQMxc708DBw8Sewg.gif)

Chaque fois que vous faites des modifications que vous voulez voir reflétées sur GitHub, les commandes suivantes sont les plus courantes :

```
$ git add .
$ git status # Liste tous les nouveaux fichiers ou modifiés à commiter
$ git commit -m "Deuxième commit"
$ git push -u origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rWBJnBdF1V8YO_mi-jEfxA.gif)

Maintenant, si nous allons voir notre dépôt, nous pouvons identifier si le commit a réussi en regardant le message de commit pour chaque fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QHM8m5HGavHkdzPz06UWGw.png)

### Étape 5 : C'est bien et bon... Mais comment télécharger et travailler sur d'autres dépôts sur GitHub ?

#### Cloner un dépôt Git :

Localisez le répertoire dans lequel vous voulez cloner le dépôt. Copiez le lien du dépôt que vous voulez et entrez ce qui suit :

```
$ git clone URL_du_dépôt_distant
```

N'hésitez pas à cloner le dépôt que j'ai créé ci-dessus en utilisant : [https://github.com/Gothamv/MuskCult](https://github.com/Gothamv/MuskCult)

![Image](https://cdn-media-1.freecodecamp.org/images/1*6NACk8-IiBjbauM-k-aesQ.gif)

#### Pousser les modifications vers le dépôt Git :

Maintenant, vous pouvez travailler sur les fichiers que vous voulez et commiter les modifications localement. Si vous voulez pousser les modifications vers ce dépôt, vous devez soit être [ajouté comme collaborateur](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/) pour le dépôt, soit créer ce qu'on appelle une pull request. Allez voir comment en faire une [ici](https://help.github.com/articles/creating-a-pull-request/) et envoyez-moi une pull request avec votre fichier de code.

#### Collaborer :

Imaginez donc que vous et votre ami collaborez sur un projet. Vous travaillez tous les deux sur les mêmes fichiers de projet. Chaque fois que vous faites des modifications et les poussez dans le dépôt master, votre ami doit tirer les modifications que vous avez poussées dans le dépôt git. Cela signifie que pour vous assurer de travailler sur la dernière version du dépôt git chaque fois que vous commencez à travailler, la commande git pull est la solution.

Voici un exemple d'un projet sur lequel mon ami et moi collaborons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2-tl2rHsgPqiv88aI55CPw.png)
_Il y a eu un commit sur le dépôt._

Donc, pour vous assurer que ces modifications sont reflétées sur ma copie locale du dépôt :

```
$ git pull origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ySDKu2OEdkc26yOUp-TJJQ.gif)

#### Voici deux autres commandes git utiles :

```
$ git fetch
    ET
$ git merge
```

En termes simples, `git fetch` suivi d'un `git merge` est égal à un `git pull`. Mais alors, pourquoi existent-ils ?

Lorsque vous utilisez `git pull`, Git essaie de faire votre travail automatiquement pour vous. **Il est sensible au contexte**, donc Git fusionnera tous les commits tirés dans la branche sur laquelle vous travaillez actuellement. `git pull` **fusionne automatiquement les commits sans vous laisser les revoir d'abord**.

Lorsque vous utilisez `git fetch`, Git rassemble tous les commits de la branche cible qui n'existent pas dans votre branche actuelle et **les stocke dans votre dépôt local**. Cependant, **il ne les fusionne pas avec votre branche actuelle**. Cela est particulièrement utile si vous devez garder votre dépôt à jour, mais que vous travaillez sur quelque chose qui pourrait se casser si vous mettez à jour vos fichiers. Pour intégrer les commits dans votre branche master, vous utilisez `git merge`.

### Une dernière chose :

```
.gitignore
```

Alors, qu'est-ce que c'est ?

`.gitignore` indique à git quels fichiers (ou motifs) il doit ignorer. Il est généralement utilisé pour éviter de commiter des fichiers transitoires de votre répertoire de travail qui ne sont pas utiles aux autres collaborateurs, tels que les produits de compilation, les fichiers temporaires créés par les IDE, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3NFtOjfz0NvNSwba7YCmDA.png)

Dans l'exemple ci-dessus, des fichiers comme __pycache__, .DS_Store sont utilisés par le système pour stocker des informations pour un accès plus rapide. Cela n'est pas utile pour les autres collaborateurs. Nous pouvons donc dire à git de les ignorer en ajoutant un fichier `.gitignore`.

Utilisez la commande touch pour créer le fichier `.gitignore` :

```
$ touch .gitignore
```

Et vous pouvez ajouter les motifs suivants pour dire à git d'ignorer ces fichiers.

```
/*.cmake
/*.DS_Store
/.user
/build
etc. selon les fichiers que vous voulez que git ne suive pas
```

### Et c'est à peu près tout pour les bases. Restez à l'écoute pour la partie 2 qui se concentrera sur Branch, Merge, Stash, Rebase, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*azp-S618Nvx4KigFrRABzQ.gif)

### Si vous avez aimé l'article, n'oubliez pas d'appuyer sur le bouton Clap et assurez-vous de me suivre pour la partie 2.

### À plus 

**Références :**

[**Ajout d'un projet existant à GitHub en utilisant la ligne de commande - Documentation utilisateur**](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
[_Mettre votre travail existant sur GitHub peut vous permettre de partager et de collaborer de nombreuses manières. Si vous migrez votre..._help.github.com](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)

[**Comment annuler (presque) n'importe quoi avec Git**](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)
[_L'une des fonctionnalités les plus utiles de tout système de contrôle de version est la capacité de "défaire" vos erreurs. Dans Git, "défaire"..._blog.github.com](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)

[**Git sur la ligne de commande - Documentation 0.3 Ne pas avoir peur de commiter**](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html)
[_Il existe d'autres moyens d'installer Git ; vous pouvez même obtenir une application graphique Git, qui inclura la ligne de commande..._dont-be-afraid-to-commit.readthedocs.io](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html)

[**Commencer à utiliser Git sur la ligne de commande | GitLab**](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
[_Documentation pour GitLab Community Edition, GitLab Enterprise Edition, Omnibus GitLab, et GitLab Runner._docs.gitlab.com](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)

[**Quelle est la différence entre 'git pull' et 'git fetch' ?**](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)
[_Note du modérateur : Étant donné que cette question a déjà reçu soixante-sept réponses (certaines d'entre elles supprimées)..._stackoverflow.com](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)