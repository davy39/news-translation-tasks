---
title: Comment créer et synchroniser des dépôts Git et GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-27T17:50:47.000Z'
originalURL: https://freecodecamp.org/news/create-and-sync-git-and-github-repositories
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail-4.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment créer et synchroniser des dépôts Git et GitHub
seo_desc: 'By Deborah Kurata

  Working with Git and GitHub is often an essential part of your daily programming
  tasks. In many cases, you''ll want both a local Git repository and a remote GitHub
  repository for a project.


  With the local repository, you work on you...'
---

Par Deborah Kurata

Travailler avec Git et GitHub est souvent une partie essentielle de vos tâches de programmation quotidiennes. Dans de nombreux cas, vous aurez besoin à la fois d'un dépôt Git local et d'un dépôt GitHub distant pour un projet.

* Avec le **dépôt local**, vous travaillez sur votre propre copie du projet. Vous effectuez et testez les modifications indépendamment avant de pousser ces changements vers le dépôt distant pour que d'autres puissent les examiner et les fusionner.
* Vous utilisez le **dépôt distant** pour le stockage hors site et pour partager le projet avec d'autres.

Ce tutoriel examine deux scénarios :

* **Local d'abord** : Vous créez d'abord un dépôt local et effectuez un Commit de votre code dans ce dépôt. Plus tard, vous créez un dépôt distant. Une fois les deux dépôts en place, vous voulez les garder synchronisés. Ce scénario est courant si vous avez commencé un projet seul et que vous souhaitez ensuite le partager.
* **Distant d'abord** : Dans ce scénario, il existe déjà un dépôt distant et vous souhaitez travailler avec ce code. Vous utilisez ce dépôt distant pour créer votre dépôt local afin de pouvoir effectuer et tester des modifications localement. Une fois les deux dépôts en place, vous voulez les garder synchronisés. Ce scénario est courant si vous travaillez en équipe ou sur un projet open source qui possède déjà un dépôt GitHub.

Voici ce que nous allons couvrir dans ce tutoriel :

1. [Que signifient Git, GitHub et Dépôt ?](#heading-que-signifient-git-github-et-depot)
2. [Comment installer Git et GitHub](#heading-comment-installer-git-et-github)
3. [Scénario 1 : Local d'abord](#heading-scenario-1-local-dabord)
4. [Comment créer un dépôt local](#heading-comment-creer-un-depot-local)
5. [Comment effectuer un Commit de fichiers dans le dépôt local](#heading-comment-effectuer-un-commit-de-fichiers-dans-le-depot-local)
6. [Comment créer un dépôt GitHub distant](#heading-comment-creer-un-depot-github-distant)
7. [Comment informer Git de l'existence de GitHub](#heading-comment-informer-git-de-lexistence-de-github)
8. [Comment synchroniser les dépôts locaux et distants](#heading-comment-synchroniser-les-depots-locaux-et-distants)
9. [Scénario 2 : Distant d'abord](#heading-scenario-2-distant-dabord)
10. [Comment cloner un dépôt](#heading-comment-cloner-un-depot)
11. [Conclusion](#heading-conclusion)

Commençons par une brève introduction aux termes que nous utilisons, puis passons à nos deux scénarios.

# Que signifient Git, GitHub et Dépôt ?

Un **dépôt**, ou \"repo\" pour faire court, stocke et suit les versions des fichiers de votre projet. Au fur et à mesure que vous modifiez ces fichiers, vous effectuez un Commit (ou copie) de ces fichiers dans le dépôt pour les mettre en sécurité. Le dépôt conserve une liste de toutes vos modifications validées, appelée **historique des commits**.

**Git** est un système de contrôle de version populaire et largement utilisé pour créer et travailler avec des dépôts. Il s'exécute localement sur votre ordinateur. Vous pouvez télécharger, installer et utiliser Git sur n'importe quelle plateforme sans aucun frais. Avec Git, vous créez un dépôt local dans le dossier de travail de votre projet et Git stocke l'historique des commits pour les fichiers de ce dossier.

Si vous débutez avec Git, vous pouvez regarder cette vidéo pour une introduction :

%[https://youtu.be/hfOeWgWp__E]

**GitHub** est un site web qui héberge des dépôts distants sur Internet. Un compte GitHub de base est également gratuit. Utilisez GitHub pour créer un dépôt distant pour votre projet. Avec un dépôt distant, vous pouvez stocker votre code hors site, collaborer avec d'autres, travailler sur des projets d'entreprise ou open source, et montrer votre portfolio à des employeurs potentiels.

Si vous débutez avec GitHub, vous pouvez regarder cette vidéo pour une introduction :

%[https://youtu.be/Uf2LLF7UKMw]

Avant de passer à nos scénarios, nous devons installer Git et créer un compte GitHub.

# Comment installer Git et GitHub

Si vous souhaitez réaliser les exemples présentés dans ce tutoriel, il y a quelques étapes préparatoires. Mais n'hésitez pas à passer à la section suivante si vous avez déjà installé ces outils ou si vous préférez lire cet article sans coder en même temps.

Tout d'abord, installez Git sur votre ordinateur si vous ne l'avez pas déjà. Pour des instructions étape par étape sur l'installation de Git, consultez la deuxième partie de cette vidéo :

%[https://www.youtube.com/watch?v=Xzy-hSdNGOI&t=70s]

Ensuite, créez un compte GitHub, si vous n'en avez pas déjà un. Cette vidéo fournit des instructions étape par étape sur la création d'un compte GitHub :

%[https://youtu.be/GrWL62j3gTU]

Enfin, créez un dossier de travail sur votre ordinateur (j'ai nommé le mien `recipes` dans mon dossier `documents`). Créez ensuite deux fichiers texte simples dans ce dossier : `file1.txt` et `file2.txt`. Même si nous utilisons des fichiers texte, le processus de synchronisation couvert dans cet article est le même avec n'importe quel type de fichiers de code.

Nous sommes maintenant prêts à parcourir nos deux scénarios : local d'abord et distant d'abord.

# Scénario 1 : Local d'abord

Supposons que vous souhaitiez créer un site web de recettes (ou peut-être une application) pour collecter et gérer des recettes. Vous créez un dépôt local afin de pouvoir facilement suivre vos modifications sur les fichiers du projet.

Vous décidez plus tard que vous voulez également un dépôt distant pour garder une copie de vos fichiers hors site et pour partager le projet avec d'autres. Une fois que vous avez le dépôt distant, vous voulez garder votre dépôt local synchronisé avec ce dépôt distant.

Ce scénario est illustré dans la Figure 1 :

![Créer un dépôt local d'abord. Les étapes numérotées sont discutées dans le texte.](https://www.freecodecamp.org/news/content/images/2023/03/Figure1-local-repo.png)
_Figure 1. Créer un dépôt local d'abord._

Selon les numéros de la Figure 1 :

1. Le dépôt local, représenté par une boîte, est créé en premier.
2. Le dépôt distant est créé avec GitHub quelque temps plus tard.
3. Les deux dépôts sont maintenus synchronisés.

Parcourons ces étapes en détail.

## **Comment créer un dépôt local**

Nous avons déjà préparé un dossier de travail et créé deux fichiers qui sont le début de notre projet.

Pour créer un dépôt local pour ce projet, ouvrez votre terminal ou invite de commande et accédez à ce dossier de travail.

Ensuite, initialisez un nouveau dépôt Git en utilisant la commande suivante :

```git
git init
```

Cette commande initialise un nouveau dépôt Git dans le dossier actuel. Le processus d'initialisation crée un dossier `.git` à l'intérieur du dossier du projet qui stocke les fichiers et les données du dépôt.

Ce dossier `.git` peut être masqué par défaut. Dans le Finder du Mac, utilisez `Command + Shift + . (point)` pour faire apparaître les dossiers et fichiers cachés. Sur Windows, utilisez l'onglet Affichage de l'Explorateur de fichiers et cochez `Éléments masqués` pour afficher les dossiers et fichiers cachés.

Nous avons maintenant un dépôt local ! Effectuons un Commit de nos deux fichiers de projet dans ce dépôt.

## **Comment effectuer un Commit de fichiers dans le dépôt local**

Chaque fois que nous créons de nouveaux fichiers, modifions des fichiers existants ou supprimons des fichiers, nous effectuons un Commit de ces modifications dans notre dépôt local. Cela garantit que le dépôt suit l'état actuel de notre projet.

Effectuer un Commit de fichiers dans un dépôt local nécessite deux étapes :

1. Indexer (Stage)
2. Commit

Tout d'abord, ajoutez les fichiers à la zone d'indexation de Git :

```git
git add .
```

Nous indiquons à Git quels fichiers nous voulons inclure dans ce Commit en les ajoutant à une zone d'indexation. L'indexation nous permet de choisir sélectivement les changements à inclure dans un Commit.

L'utilisation du `.` (point) ajoute tous les fichiers du dossier de travail (et de ses sous-dossiers) à la zone d'indexation. Si vous souhaitez seulement ajouter des fichiers spécifiques, vous pouvez les lister à la place.

Ensuite, nous effectuons le Commit des fichiers indexés dans le dépôt local :

```git
git commit -m "Initial commit"
```

Cette commande valide les fichiers de la zone d'indexation Git dans le dépôt local.

l'option `-m` sert au message de Commit. Faites suivre le `-m` du message, entre guillemets. Veillez à définir un message clair décrivant les changements que vous validez.

Pour plus d'informations sur la définition de bons messages de Commit, consultez cette vidéo :

%[https://youtu.be/9UlmPCMZ4tc]

Après ces étapes, le terminal apparaît comme indiqué ci-dessous :

![Résultat de la création d'un dépôt local, puis de l'indexation et du commit des fichiers du projet.](https://www.freecodecamp.org/news/content/images/2023/03/Figure2-git-init.png)
_Figure 2. Création d'un dépôt local, puis indexation et Commit des fichiers du projet._

La commande `init` affiche un message d'état nous indiquant qu'elle a créé un dépôt Git vide.

La commande `add` ne fournit aucune sortie.

La commande `commit` affiche la branche sur laquelle nous nous trouvons ( `main` dans cet exemple), les premiers caractères de l'ID du Commit et le message de Commit. Elle liste ensuite les fichiers modifiés. Dans cet exemple, 2 fichiers ont été modifiés et les deux étaient des insertions (nouveaux fichiers).

Le nombre après `create mode` indique le type de fichier et les permissions. `100644` signifie qu'il s'agit de fichiers réguliers, pas de dossiers, avec des permissions de lecture et d'écriture pour le propriétaire.

Avec notre dépôt local en place, il est temps de créer notre dépôt distant.

## **Comment créer un dépôt GitHub distant**

Nous allons maintenant créer un dépôt distant sur GitHub en utilisant GitHub. Allez sur le site web de GitHub à [www.github.com](http://www.github.com) et connectez-vous. Si vous n'avez pas de compte GitHub, consultez la section \"Comment installer Git et GitHub\" plus haut dans ce tutoriel pour les étapes de création de compte.

Regardez cette vidéo pour voir le processus de création d'un dépôt GitHub :

%[https://youtu.be/QuCdgrYph98]

Après vous être connecté à GitHub, vous êtes dirigé vers votre tableau de bord personnel. Votre tableau de bord personnel GitHub fournit des informations sur vos dépôts et projets.

Si c'est la première fois que vous créez un dépôt sur GitHub, il propose un bouton `Create Repository` pour vous aider à démarrer. Si vous utilisez déjà GitHub, vous verrez un bouton `New` à la place.

Dans les deux cas, cliquer sur le bouton permet d'accéder à la page `Create a new repository` comme indiqué dans la Figure 3.

![La page pour créer un nouveau dépôt distant avec GitHub.](https://www.freecodecamp.org/news/content/images/2023/03/Figure3-create-new-repo.png)
_Figure 3. Créer un nouveau dépôt distant avec GitHub._

Commencez par saisir le nom du dépôt. Un nom de dépôt doit être court mais descriptif de votre projet. Il doit être unique au sein de _votre_ compte GitHub. GitHub vérifie cela pour vous.

Les conventions générales pour les noms de dépôts suggèrent d'utiliser des minuscules. S'il y a plusieurs mots, utilisez des tirets entre les mots, comme recipe-book.

J'ai appelé mon dépôt `recipes`. Et la flèche verte à côté du nom signifie qu'il est unique dans ce compte GitHub.

Optionnellement, vous pouvez fournir une description. C'est ici que vous pouvez mettre plus d'informations sur le dépôt, si vous le souhaitez.

Ensuite, vous avez l'option de créer un dépôt public ou privé. Si vous créez un dépôt public, n'importe qui sur Internet peut le voir. Mais seuls les collaborateurs que vous choisissez peuvent y effectuer des Commits. Vous n'avez donc pas à vous soucier des étrangers modifiant vos fichiers. Si vous créez un dépôt privé, il est privé sauf pour vos collaborateurs choisis.

Pensez à rendre vos dépôts publics pour partager votre code avec d'autres, à moins que votre code ne soit propriétaire.

Vous avez ensuite l'option de créer un fichier readme. Un fichier readme donne à ceux qui regardent un dépôt une idée de ce à quoi sert ce dépôt et des instructions sur la façon de l'utiliser. Cochez la case pour ajouter un fichier readme.

Un modèle .gitignore vous aide à identifier quels fichiers de votre dossier de travail vous ne souhaitez _pas_ inclure dans le suivi de version de Git. Pour une application, vous ne voulez pas inclure les fichiers de build intermédiaires, par exemple, car ils sont souvent volumineux et peuvent facilement être reconstruits à partir des fichiers sources. Pour ce projet simple, nous n'avons pas besoin de modèle .gitignore.

Le choix d'une licence vient ensuite. Une licence permet aux autres développeurs de savoir ce qu'ils peuvent faire avec le code de votre dépôt. Par exemple, s'ils peuvent utiliser librement le code pour leurs propres projets.

GitHub fournit un site web pour vous aider à prendre votre décision. Cliquez sur `learn more` sous l'option `Choose a license` pour accéder à la documentation GitHub. Sur la page de documentation, vous trouverez un lien `choosealicense.com` pour vous aider à choisir la licence qui convient à votre projet.

Pour mon dépôt recipes, je vais choisir une licence simple et permissive : la licence MIT.

Fermez l'onglet du navigateur de documentation, revenez à l'onglet GitHub et sélectionnez la licence souhaitée dans la liste.

Juste au-dessus du bouton `Create repository`, GitHub fournit un résumé afin que vous puissiez revérifier l'action que vous allez effectuer. Cliquez ensuite sur `Create repository`.

Cela crée le dépôt comme indiqué sur la Figure 4. C'est parfait !

![Le dépôt distant GitHub résultant.](https://www.freecodecamp.org/news/content/images/2023/03/Figure4-github-repo.png)
_Figure 4. Notre dépôt distant GitHub._

Comme vous pouvez le voir sur la Figure 4, GitHub a automatiquement effectué notre premier Commit ! Ce Commit est un instantané des deux fichiers que nous lui avons demandé d'ajouter au dépôt : notre fichier de licence et le readme. Il a défini un message de Commit \"Initial commit\". Et par défaut, GitHub affiche le contenu de notre fichier readme.

À ce stade, notre dépôt _local_ contient nos deux fichiers texte. Et notre dépôt _distant_ contient nos fichiers de licence et readme. Nous voulons que les deux dépôts correspondent.

## **Comment informer Git de l'existence de GitHub**

Avant de pouvoir synchroniser les dépôts local et distant, vous devez établir une connexion entre eux. En gros, vous devez indiquer à votre dépôt local où trouver le dépôt distant.

Nous identifions un dépôt distant par son URL. Dans la Figure 4 ci-dessus, remarquez le bouton vert `Code`. Cliquez sur ce bouton pour voir les détails du dépôt (Figure 5).

![Trouver l'URL du dépôt GitHub.](https://www.freecodecamp.org/news/content/images/2023/03/Figure5-repo-link.png)
_Figure 5. Trouver l'URL du dépôt GitHub._

Assurez-vous que l'onglet HTTPS est sélectionné, et cliquez sur l'icône `copy` pour copier l'URL de ce dépôt GitHub.

De retour dans la fenêtre de commande sur votre machine locale, ajoutez le dépôt distant au dépôt local. Listez ensuite les remotes pour confirmer que le distant a été créé.

```git
git remote add recipes-gh https://github.com/DeborahK/recipes.git
git remote
```

La commande `remote add` ajoute le dépôt distant à l'URL fournie. Et elle vous permet d'attribuer un pseudonyme à ce dépôt afin que vous n'ayez pas à taper l'URL lorsque vous vous référez au dépôt distant.

Un pseudonyme courant pour le dépôt distant est `origin`, mais certains trouvent ce nom un peu déroutant, surtout si le dépôt distant n'était pas l'origine du projet. Dans ce cas, j'utilise parfois le nom du dépôt local avec un suffixe `-gh` (pour GitHub) comme pseudonyme du dépôt distant, afin de m'en souvenir facilement. Mais n'hésitez pas à utiliser n'importe quel nom.

La commande `remote` seule affiche la liste des remotes que votre dépôt local connaît. Voici à quoi cela ressemble :

![Établir une connexion avec le dépôt distant.](https://www.freecodecamp.org/news/content/images/2023/03/Figure6-add-remote.png)
_Figure 6. Établir une connexion avec le dépôt distant._

Notre dépôt Git local sait maintenant où trouver son dépôt distant associé. L'étape suivante consiste à synchroniser les dépôts afin que leur historique de commits corresponde.

## **Comment synchroniser les dépôts locaux et distants**

Pour synchroniser nos dépôts locaux et distants, nous récupérons d'abord l'historique des modifications du dépôt distant et le fusionnons dans notre dépôt local en utilisant la commande `pull`. Ensuite, nous poussons notre historique de modifications locales vers le dépôt distant en utilisant la commande `push`.

Si vous préférez synchroniser les dépôts en utilisant VS Code, consultez cette vidéo :

%[https://youtu.be/5vYPLUMP6dg]

Pour tirer depuis le dépôt distant et fusionner vers notre dépôt local en utilisant une commande Git :

```git
git pull recipes-gh main --allow-unrelated-histories

dir		// Sur Windows
OU
ls		// Sur un Mac
```

La commande `pull` nécessite le pseudonyme du dépôt distant (`recipes-gh`) et le nom de la branche. Comme nous n'avons pas créé de branches supplémentaires, nous spécifions la branche principale (`main`). 

Le flag `--allow-unrelated-histories` est requis la première fois que nous faisons un Pull parce que nous voulons fusionner deux dépôts qui ont été créés séparément et qui ne partagent pas actuellement d'historique commun.

Après la première fois, la commande git `pull` ne nécessite plus ce flag :

```git
git pull recipes-gh main
```

Dans les deux cas, la commande `pull` recherche l'URL appropriée pour le dépôt distant en utilisant le pseudonyme fourni ( `recipes-gh` ). 

Elle récupère ensuite l'historique des commits et d'autres données de la branche spécifiée ( `main` ) du dépôt distant qui ne sont pas dans cette branche du dépôt local. 

Elle fusionne ces données dans le dépôt local. S'il y a des conflits, vous devrez les résoudre manuellement avant que Git ne puisse fusionner les changements. 

Enfin, elle met à jour le dossier de travail local avec tous les fichiers du commit le plus récent.

En utilisant la commande `dir` sur Windows, ou la commande `ls` sur un Mac, nous voyons que notre dépôt local contient maintenant nos fichiers originaux plus les fichiers de licence et readme de notre dépôt distant, comme illustré dans la Figure 7.

![Résultat de la récupération de l'historique des modifications depuis le dépôt distant.](https://www.freecodecamp.org/news/content/images/2023/03/Figure7-pull.png)
_Figure 7. Récupération de l'historique des modifications depuis le dépôt distant._

Maintenant, notre dépôt local contient tout l'historique des commits du dépôt distant. 

Ensuite, nous poussons l'historique des modifications de notre dépôt local vers notre dépôt distant à l'aide de la commande `push`.

```git
git push recipes-gh main

```

La commande `push` nécessite le nom du dépôt distant (`recipes-gh`) et le nom de la branche. Comme nous n'avons pas créé de branches supplémentaires, nous spécifions la branche principale (`main`).

Cette commande fusionne l'historique des modifications locales vers le dépôt distant. S'il y a des conflits, vous devrez les résoudre manuellement avant que Git ne fusionne les changements. Voir la Figure 8 pour le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Figure8-push.png)
_Figure 8. Envoi de l'historique des modifications locales vers le dépôt distant._

Pour confirmer que notre dépôt distant inclut tous nos fichiers, visualisez le dépôt distant sur GitHub. Dans la Figure 9, nous voyons que les fichiers de notre dépôt local sont maintenant dans notre dépôt distant et nos dépôts sont synchronisés !

![Notre dépôt distant avec les fichiers de notre dépôt local.](https://www.freecodecamp.org/news/content/images/2023/03/Figure9-github-repo.png)
_Figure 9. Notre dépôt distant avec les fichiers de notre dépôt local._

En résumé, la synchronisation de vos dépôts local et distant implique de tirer tous les changements du dépôt distant vers votre dépôt local, de résoudre les conflits, puis de pousser vos changements locaux vers le dépôt distant.

C'est tout pour le premier scénario. Nous avons créé un dépôt local à partir de nos fichiers existants. Ensuite, nous avons créé un dépôt distant, établi une connexion avec ce dépôt distant et synchronisé nos fichiers. Répétez les commandes `pull` et `push` pour synchroniser les dépôts au fur et à mesure que vous travaillez sur votre projet.

# Scénario 2 : Distant d'abord

Pour notre deuxième scénario, le dépôt distant existe déjà. Ce sera le cas si vous rejoignez une équipe qui a déjà du code dans GitHub, ou si vous voulez travailler sur un projet open source, ou encore si vous avez trouvé du code sur GitHub que vous aimeriez utiliser comme point de départ pour votre projet.

Vous voulez créer votre dépôt local à partir d'un dépôt distant existant. Il existe trois façons simples d'obtenir du code à partir d'un dépôt distant, comme le montre la Figure 10.

![Trois façons d'obtenir du code depuis un dépôt distant : clone, fork et clone, zip.](https://www.freecodecamp.org/news/content/images/2023/03/Figure10-remote-first.png)
_Figure 10. Obtenir du code depuis un dépôt distant._

Sur le côté gauche de la Figure 10, nous avons un scénario : si vous possédez ou avez les droits d'accès pour modifier le dépôt distant, vous pouvez cloner le dépôt distant pour créer votre dépôt local. Vous pouvez ensuite synchroniser directement les modifications entre les deux dépôts.

Le deuxième scénario est illustré au milieu de la Figure 10 : si vous n'êtes pas propriétaire du dépôt distant ou si vous n'avez pas les droits d'accès pour le modifier, utilisez GitHub pour d'abord **fork** (bifurquer) le dépôt. Cela crée une copie du dépôt distant dans votre compte GitHub. Ensuite, clonez votre copie pour créer votre dépôt local.

Ce sera le cas si vous travaillez sur un projet open source ou si vous souhaitez utiliser le code du dépôt de quelqu'un d'autre comme point de départ pour votre projet.

Le troisième scénario est illustré à droite de la Figure 10 – il y a aussi l'option de télécharger un fichier zip du code du dépôt. Cela ne crée _pas_ de dépôt local. Utilisez cette option si vous voulez regarder le code d'un dépôt GitHub, mais que vous ne prévoyez pas d'en suivre les modifications.

Pour vous préparer à l'exemple de ce scénario, vous avez besoin d'un dépôt distant qui n'a pas actuellement de dépôt local associé. Vous pouvez utiliser le dépôt distant `recipes` que vous avez déjà créé dans le premier scénario. Si vous préférez utiliser le dépôt de quelqu'un d'autre pour cet exemple, assurez-vous de le fork d'abord.

Une fois que vous avez un dépôt distant, assurez-vous qu'aucun dépôt local ne lui est associé. Si vous utilisez le dépôt distant `recipes`, supprimez le dossier `recipes` de votre système local. Cela supprime votre dépôt local.

Vous êtes maintenant prêt à créer un nouveau dépôt local à partir de votre dépôt distant sur GitHub.

## **Comment cloner un dépôt**

Pour créer un dépôt local à partir d'un dépôt distant sur GitHub, utilisez la commande `clone`.

Si vous préférez cloner un dépôt en utilisant l'application GitHub Desktop, consultez cette vidéo :

%[https://youtu.be/GpqIr0y2rvc]

Pour cloner à l'aide d'une commande Git, nous avons d'abord besoin de l'URL du dépôt distant. 

Naviguez vers GitHub, connectez-vous, et vous verrez votre tableau de bord personnel. Localisez le dépôt que vous souhaitez cloner. Cliquez sur le bouton vert `Code` pour voir les détails du dépôt comme indiqué précédemment sur la Figure 5. Cliquez sur le bouton de copie à côté de l'URL pour la copier.

Ensuite, ouvrez votre terminal ou invite de commande sur votre ordinateur. Naviguez vers le dossier où vous souhaitez créer le dossier de travail du projet. Je vais naviguer vers mon dossier `documents`.

Ensuite, nous sommes prêts à cloner ce dépôt :

```git
git clone https://github.com/DeborahK/recipes.git
```

La commande `clone` nécessite l'URL du dépôt distant. Nous venons de copier cette URL depuis GitHub, alors collez-la dans le cadre de cette commande.

Lorsque la commande est exécutée, elle crée d'abord le dossier de travail pour le dépôt en utilisant le nom du dépôt distant provenant de l'URL, qui est `recipes` dans cet exemple. Elle copie ensuite l'historique des commits du dépôt distant à l'URL fournie.

Le processus de clonage lie également automatiquement le nouveau dépôt local à son dépôt distant. Et il attribue au dépôt distant le pseudonyme `origin`. Nous pouvons alors référencer le dépôt distant en utilisant ce pseudonyme au lieu de son URL.

Enfin, le processus de clonage copie tous les fichiers du commit le plus récent vers le dossier de travail local. Vous pouvez ensuite ajouter, modifier ou supprimer des fichiers dans ce dossier de travail pendant que vous travaillez localement sur le projet.

Naviguez vers le nouveau dossier `recipes`. Utilisez ensuite la commande `remote` pour visualiser le dépôt distant lié. Et la Figure 11 montre qu'il est bien surnommé `origin`.

![Le résultat du clonage d'un dépôt.](https://www.freecodecamp.org/news/content/images/2023/03/Figure11-git-clone.png)
_Figure 11. Cloner un dépôt._

Remarquez la sortie de l'opération de clonage dans la Figure 11. Git énumère (ou trouve) 10 objets. Nous n'avons pourtant que quatre fichiers dans le dépôt distant `recipes`. Pourquoi trouve-t-il 10 objets ? C'est parce que le processus de clonage copie l'historique complet des commits, pas seulement les fichiers.

Utilisez la commande `rev-list` avec les flags `--objects` et `--all` pour voir la liste des objets.

```git
git rev-list --objects --all

```

La Figure 12 montre la sortie de cette commande :

![Liste des valeurs SHA pour les objets dans le dépôt.](https://www.freecodecamp.org/news/content/images/2023/03/Figure12-git-rev-list.png)
_Figure 12. Liste des objets dans le dépôt._

Chacun des objets ci-dessus est affiché sous forme de SHA, ou identifiant Secure Hash Algorithm. Le SHA est utilisé comme ID pour identifier de manière unique les objets de notre dépôt.

Les trois premiers objets de cette liste (objets 1-3) sont les trois commits effectués dans ce dépôt. En regardant la liste des commits dans GitHub (Figure 13), chaque commit affiche les premiers caractères de son SHA. Ceux-ci correspondent aux trois premiers objets :

* Le Commit de fusion lorsque nous avons fusionné les deux dépôts.
* Le `initial commit` effectué par GitHub sur le dépôt distant créant les fichiers `LICENSE` et `README.md`.
* Le `initial commit` que nous avons fait sur le dépôt local validant `file1.txt` et `file2.txt`.

Les objets du milieu de la liste présentée dans la Figure 12 (objets 5-8) sont les quatre fichiers validés.

Les trois objets restants (objets 4, 9, 10) sont des objets de type tree (arbre). Un objet tree représente l'état d'un dossier, y compris les fichiers et les sous-dossiers de ce dossier. Il maintient la hiérarchie du dossier.

![Historique des commits GitHub, chacun identifié par les premières valeurs du SHA.](https://www.freecodecamp.org/news/content/images/2023/03/Figure13-commit-history.png)
_Figure 13. Historique des commits, chacun identifié par les premières valeurs du SHA._

En utilisant la commande `dir` sur Windows, ou la commande `ls` sur le Mac, nous voyons que notre dossier de travail contient maintenant tous les fichiers de notre dépôt distant.

![Un répertoire des fichiers dans notre dossier de travail.](https://www.freecodecamp.org/news/content/images/2023/03/Figure14-working-folder.png)
_Figure 14. Un répertoire des fichiers dans notre dossier de travail._

Maintenant que nous avons cloné le dépôt, nos dépôts local et distant correspondent. Pour les garder synchronisés, nous utilisons `pull` et `push` comme nous l'avons vu dans la section \"Comment synchroniser les dépôts locaux et distants\" plus haut dans cet article.

Notez que si vous travaillez avec un dépôt distant dont vous n'êtes pas propriétaire, vous n'aurez peut-être pas accès pour pousser vos modifications directement sur le dépôt. Au lieu de cela, vous devrez émettre une **Pull Request**.

Une Pull Request, ou PR, indique aux propriétaires ou aux autres contributeurs que vous avez poussé des changements et que vous demandez que ces changements soient examinés et tirés (pull), ou fusionnés, dans le dépôt distant.

Consultez cette vidéo pour plus d'informations sur les Pull Requests :

%[https://youtu.be/y_A8O3cpDyM]

# Conclusion

Dans le premier scénario, nous avions du code existant et avons créé un dépôt local à partir de ce code. Nous avons ensuite créé un dépôt distant pour conserver une copie des fichiers hors site et partager le projet avec d'autres.

Dans le deuxième scénario, nous avions un dépôt distant existant créé dans GitHub par notre équipe ou par un contributeur open source. Nous avons ensuite cloné ce dépôt pour créer notre dépôt local. De cette façon, nous pouvons travailler sur notre propre copie du projet, et effectuer et tester des modifications indépendamment avant de pousser ces changements vers le dépôt distant pour que d'autres puissent les examiner et les fusionner.

Que vous créiez votre dépôt local en premier, ou votre dépôt GitHub distant en premier, une fois que vous avez les deux dépôts en place, vous pouvez les garder synchronisés avec les commandes Git `pull` et `push`. Ou en soumettant des Pull Requests, ou PR.

Pour plus de détails sur l'apprentissage de Git et GitHub, consultez ce cours :

%[https://youtu.be/pICJdbC7j0Q]

Acquérir une compréhension solide des dépôts locaux et distants, et de la façon de les garder synchronisés, est essentiel lorsque vous travaillez sur votre propre code. C'est encore plus important lorsque vous travaillez en équipe ou sur un projet open source.