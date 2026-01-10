---
title: Bonnes pratiques Git – Un guide de contrôle de version pour débutants
subtitle: ''
author: Adekola Olawale
co_authors: []
series: null
date: '2023-05-16T16:33:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-best-practices-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/header-min-1.jpg
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Bonnes pratiques Git – Un guide de contrôle de version pour débutants
seo_desc: 'If you''re a software developer, you may be familiar with the concept of
  version control. Version control is the practice of managing changes to your codebase
  over time. It''s an essential tool for any development project.

  One of the most popular versi...'
---

Si vous êtes un développeur de logiciels, vous êtes peut-être familier avec le concept de contrôle de version. Le contrôle de version est la pratique de gestion des changements apportés à votre base de code au fil du temps. C'est un outil essentiel pour tout projet de développement.

L'un des systèmes de contrôle de version les plus populaires est Git, largement utilisé par les développeurs du monde entier. Git est un outil puissant et flexible qui peut vous aider à gérer votre base de code, à collaborer avec d'autres développeurs et à suivre les changements au fil du temps.

Mais Git peut aussi être complexe et intimidant, surtout si vous êtes nouveau dans le contrôle de version. Dans ce tutoriel, nous allons couvrir certaines des meilleures pratiques pour utiliser Git, y compris les commandes de base, les dépôts distants et les outils de collaboration.

Que vous soyez débutant ou développeur expérimenté, ce guide vous aidera à tirer le meilleur parti de Git et à améliorer votre flux de travail.

## Table des matières

* [Qu'est-ce que le contrôle de version ?](#heading-questce-que-le-controle-de-version)
    
* [Qu'est-ce que Git ?](#heading-questce-que-git)
    
* [Comment commencer avec Git](#heading-comment-commencer-avec-git)
    
* [Comment configurer un nouveau dépôt Git](#heading-comment-configurer-un-nouveau-depot-git)
    
* [Commandes de base pour créer et valider les changements](#heading-commandes-de-base-pour-creer-et-valider-les-changements)
    
* [Comment collaborer avec Git](#heading-comment-collaborer-avec-git)
    
* [Bonnes pratiques pour utiliser Git](#heading-bonnes-pratiques-pour-utiliser-git)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le contrôle de version ?

Le contrôle de version est la gestion des changements apportés aux documents, fichiers ou tout autre type de données. Dans le développement de logiciels, il est essentiel pour gérer et suivre les changements apportés à la base de code, assurer la qualité du code, réduire les erreurs et améliorer la collaboration entre les membres de l'équipe.

Sans contrôle de version, la gestion et le suivi des changements de code seraient une tâche difficile et sujette aux erreurs. Les outils de contrôle de version comme Git fournissent un moyen de gérer les changements de code, de suivre les versions et de collaborer avec les membres de l'équipe. Cela en fait un composant critique du développement logiciel moderne, utilisé par pratiquement toutes les équipes de développement logiciel.

## Qu'est-ce que Git ?

Git est un système de contrôle de version populaire utilisé par les développeurs pour gérer les changements de code. Il permet aux développeurs de suivre les changements apportés à leur base de code, de collaborer avec les membres de l'équipe et de revenir à des versions précédentes si nécessaire.

Git est largement utilisé dans le développement de logiciels en raison de sa flexibilité, de sa rapidité et de sa capacité à gérer de grandes bases de code avec facilité. Il offre également une gamme de fonctionnalités et d'outils pour gérer et organiser le code, tels que le branchement et la fusion. Et il dispose d'une grande et active communauté d'utilisateurs qui contribuent à son développement et fournissent un support.

## Comment commencer avec Git

![Image](https://www.freecodecamp.org/news/content/images/2023/05/FireShot-Capture-140---Git---Downloads---git-scm.com.png align="left")

*Page de téléchargement de Git*

### Comment installer Git

Git est un système de contrôle de version populaire utilisé par les développeurs de logiciels pour gérer et suivre les changements de code. Voici les étapes pour installer Git :

#### Étape 1 : Télécharger Git

Pour commencer, allez sur le site officiel de Git ([https://git-scm.com/downloads](https://git-scm.com/downloads)) et téléchargez l'installateur approprié pour votre système d'exploitation.

Comme vous pouvez le voir sur la page de téléchargement dans le graphique, la page de téléchargement de Git est suffisamment intelligente pour détecter le système d'exploitation (OS) que vous utilisez – c'est sur cette base que le graphique de bureau affichera le bouton de téléchargement à l'intérieur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-installer-ui-1.png align="left")

*Interface utilisateur de l'installateur Git*

#### Étape 2 : Exécuter l'installateur

Une fois le téléchargement terminé, exécutez l'installateur et suivez les invites. Le processus d'installation variera en fonction de votre système d'exploitation, mais l'installateur devrait vous guider tout au long du processus.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-installer-ui-step2.png align="left")

*Options d'installation de Git*

#### Étape 3 : Sélectionner les options d'installation

Au cours du processus d'installation, vous serez invité à sélectionner diverses options. Pour la plupart des utilisateurs, les options par défaut seront suffisantes, mais vous pouvez choisir de personnaliser votre installation si vous le souhaitez.

Sur Windows et macOS, vous pouvez accepter les options d'installation par défaut, mais sur Linux, vous devrez peut-être personnaliser le processus d'installation en fonction de votre distribution.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-installation-done-1.png align="left")

*Installation de Git terminée*

#### Étape 4 : Terminer l'installation

Une fois que vous avez sélectionné vos options d'installation, l'installateur installera Git sur votre ordinateur. Cela peut prendre quelques minutes en fonction de votre système.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-bash-snippet.png align="left")

*Vérifier l'installation de Git*

#### Étape 5 : Vérifier l'installation

Une fois l'installation terminée, vous pouvez vérifier que Git a été installé correctement en ouvrant une invite de commande ou une fenêtre de terminal et en exécutant la commande `git --version`. Cela devrait afficher la version actuelle de Git installée sur votre système, quelque chose comme `git version 2.40.1.windows.1`.

### Comment configurer un nouveau dépôt Git

Les dépôts Git sont utilisés pour gérer et suivre les changements de code. La configuration d'un nouveau dépôt Git est un processus simple qui ne prend que quelques étapes.

#### Étape 1 : Créer un nouveau répertoire

La première étape pour configurer un nouveau dépôt Git est de créer un nouveau répertoire sur votre ordinateur. Ce répertoire servira de répertoire racine pour votre nouveau dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-bash-init-snippet.png align="left")

`git init`

#### Étape 2 : Initialiser Git

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-file.png align="left")

*Fichier .git*

Une fois que vous avez installé Git, l'étape suivante consiste à initialiser un nouveau dépôt. Pour ce faire, naviguez jusqu'au répertoire racine de votre projet dans la ligne de commande ou le terminal et exécutez la commande `git init`. Cela créera un nouveau répertoire **.git** dans le répertoire racine de votre projet, où Git stocke toutes ses métadonnées et informations de contrôle de version.

Une fois que vous avez initialisé le dépôt, vous pouvez commencer à suivre les changements de votre projet et à faire des validations. Il est important de noter que vous n'avez besoin d'initialiser un dépôt qu'une seule fois pour chaque projet, vous n'aurez donc pas besoin de répéter cette étape pour les validations ou changements ultérieurs.

#### Étape 3 : Ajouter des fichiers

Après avoir initialisé votre dépôt Git, l'étape suivante consiste à commencer à suivre les changements de votre projet en ajoutant des fichiers à la zone de préparation.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-stage.png align="left")

*Fichiers en préparation*

Pour ce faire, utilisez la commande `git add <nomdufichier>` pour ajouter chaque fichier à la zone de préparation. Vous pouvez également utiliser la commande `git add .` pour ajouter tous les fichiers du répertoire courant et de ses sous-répertoires à la zone de préparation en une seule fois.

De plus, comme vous pouvez le voir dans le graphique ci-dessus, il y a une étiquette **(master)** après **~/Desktop/Projects/GIT for Beginners**. Le **(master)** signifie la branche actuelle pour le projet. Il s'agit de la branche par défaut pour tous les projets qui initialisent Git.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-staging.png align="left")

*Extrait de préparation Git*

Une fois qu'un fichier est ajouté à la zone de préparation, il est prêt à être validé dans le dépôt. Il est important de noter que l'ajout de fichiers à la zone de préparation ne les valide pas réellement – il les prépare simplement pour la validation. Vous pouvez continuer à ajouter et modifier des fichiers selon vos besoins avant de faire une validation.

#### Étape 4 : Valider les changements

Après avoir ajouté des fichiers à la zone de préparation, l'étape suivante consiste à valider les changements dans votre dépôt en utilisant la commande `git commit`.

Lors de la validation des changements, il est important de fournir un message clair et descriptif qui explique les changements que vous avez apportés dans la validation. Ce message sera utilisé pour suivre les changements dans l'historique du dépôt et aidera les autres contributeurs à comprendre les changements que vous avez apportés.

Pour valider les changements, utilisez la commande `git commit -m 'message de validation'`, en remplaçant `'message de validation'` par un message clair et descriptif qui explique les changements apportés dans la validation. Une fois validés, les changements seront enregistrés dans l'historique du dépôt et pourront être suivis, restaurés ou fusionnés avec d'autres branches selon les besoins.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-commit.png align="left")

*Validation Git*

#### Étape 5 : Se connecter à un dépôt distant

Pour partager vos changements avec d'autres développeurs ou collaborer sur un projet, vous pouvez connecter votre dépôt local à un dépôt distant en utilisant Git.

Un dépôt distant est une copie de votre dépôt qui est hébergée sur un serveur, tel que GitHub, GitLab ou BitBucket, et permet à plusieurs contributeurs de travailler sur la même base de code.

Pour se connecter à un dépôt distant, utilisez la commande `git remote add` suivie de l'URL du dépôt distant.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-add.png align="left")

*Se connecter à un dépôt distant*

Par exemple, pour se connecter à un dépôt GitHub, vous utiliseriez la commande `git remote add origin <URL du dépôt>`. Avant même de pouvoir vous connecter au dépôt distant, vous devez le créer.

Naviguez vers [S](https://scribehow.com/shared/How_to_Create_a_New_Repository_on_GitHub__OGEKiV2UT42dB8Kre8KfCg)cribe et suivez les étapes pour créer un dépôt sur GitHub. Mais avant de faire cela, vous devez créer un compte GitHub si vous n'en avez pas déjà un.

Une fois connecté, vous pouvez pousser vos changements vers le dépôt distant en utilisant la commande `git push -u <branche par défaut>`. Cette commande est souvent utilisée lors de la première poussée de changements pour établir la relation entre la branche locale et la branche distante.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-push.png align="left")

*Première poussée distante Git*

Cependant, pour les poussées de changements ultérieures, utilisez la commande `git push` sans spécifier d'arguments supplémentaires. Git tentera de pousser les changements de la branche locale actuelle sur votre machine locale (ordinateur) vers la branche correspondante sur le dépôt distant. Il suppose que la branche locale et la branche distante ont le même nom.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-push2.png align="left")

*Poussée distante Git ultérieure*

La commande `git pull` récupère les derniers changements apportés par d'autres contributeurs depuis un dépôt distant et les fusionne automatiquement dans la branche actuelle. En se connectant à un dépôt distant, vous pouvez collaborer avec d'autres développeurs et contribuer à des projets open source.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-pull.png align="left")

*Git Pull*

En suivant ces étapes simples, vous pouvez configurer un nouveau dépôt Git et commencer à gérer les changements de votre base de code.

### Commandes de base pour créer et valider les changements

Une fois que vous avez configuré un nouveau dépôt Git et ajouté des fichiers, vous devrez valider les changements dans votre dépôt. Voici les commandes de base pour créer et valider les changements dans Git.

#### Étape 1 : Vérifier le statut

Avant de valider les changements, vous devez vérifier le statut de votre dépôt pour voir quels changements ont été apportés. Pour ce faire, exécutez la commande `git status` dans un terminal ou une fenêtre d'invite de commande.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-status.png align="left")

*Statut Git*

#### Étape 2 : Préparer les changements

Pour valider les changements, vous devrez d'abord les préparer en utilisant la commande `git add`. Cela indique à Git quels fichiers inclure dans la prochaine validation. Vous pouvez préparer tous les changements en exécutant la commande `git add .` ou préparer des changements spécifiques en exécutant la commande `git add <nomdufichier>`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-stage-css.png align="left")

*Préparation Git*

Lorsque vous préparez les changements, Git prend un instantané des fichiers à ce moment précis. Cet instantané inclut tous les changements que vous avez apportés depuis la dernière validation.

La préparation des changements vous permet de passer en revue attentivement vos changements avant de les valider. Vous pouvez préparer les changements en petits morceaux et les valider séparément, ou préparer tous les changements et les valider ensemble. Cela vous donne plus de contrôle sur les changements que vous apportez à votre base de code et vous aide à suivre les changements apportés au fil du temps.

En préparant les changements dans Git, vous pouvez vous assurer que vos validations reflètent avec précision les changements que vous avez apportés à votre base de code.

#### Étape 3 : Valider les changements

Une fois que vous avez préparé vos changements, vous pouvez les valider dans votre dépôt en utilisant la commande `git commit`. Cela crée un nouvel instantané de votre dépôt avec les changements que vous avez apportés.

La validation est un instantané des changements apportés à ce moment-là, et elle inclut une référence à la validation précédente dans l'historique de la branche. Cela permet aux développeurs de suivre les changements apportés au code au fil du temps, de collaborer avec d'autres développeurs et de revenir à des versions précédentes du code si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-commit2.png align="left")

*Validation Git*

Vous devrez inclure un message de validation pour décrire les changements que vous avez apportés en utilisant le drapeau `-m`. Par exemple, `git commit -m "Ajout d'une nouvelle fonctionnalité"`, la partie "Ajout d'une nouvelle fonctionnalité" est le nom de la validation.

En incluant un message de validation clair et concis comme "Ajout d'une nouvelle fonctionnalité", d'autres développeurs peuvent rapidement comprendre le but de la validation et les changements qui ont été apportés. Cela facilite la collaboration et la maintenance du code.

#### Étape 4 : Pousser les changements

Si vous travaillez en équipe ou souhaitez partager vos changements avec d'autres, vous pouvez pousser vos changements vers un dépôt distant en utilisant la commande `git push`. Cela télécharge vos changements vers un dépôt partagé que d'autres peuvent accéder.

Pour pousser les changements vers un dépôt distant, vous devrez d'abord ajouter une URL distante en utilisant la commande `git remote add`. Cela indique à Git où pousser vos changements.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-add-2.png align="left")

*Git*

Par exemple, `git remote add origin [https://github.com/username/repository.git](https://github.com/username/repository.git)`. Avant d'obtenir une URL distante pour pousser, vous devez créer un dépôt sur votre compte GitHub. Pour ce faire, naviguez vers [https://bit.ly/417ULB7](https://bit.ly/417ULB7).

En ajoutant un dépôt distant, vous établissez une connexion entre votre dépôt local et le dépôt distant, vous permettant de pousser et de tirer des changements entre eux.

Voici ce que fait `git remote add <URL du dépôt>` :

1. `git remote` : C'est une commande Git qui gère les dépôts distants associés à votre dépôt local.
    
2. `add` : C'est une option utilisée avec la commande `git remote` pour ajouter un nouveau dépôt distant.
    
3. `<URL du dépôt>` : Il s'agit de l'URL du dépôt distant que vous souhaitez ajouter. Il pointe généralement vers le service d'hébergement de dépôt Git où se trouve votre dépôt distant.
    

Une fois que vous avez ajouté une URL distante, vous pouvez pousser vos changements vers le dépôt distant en utilisant la commande `git push`. Par exemple, `git push origin master` pousse les changements vers la branche "master" du dépôt distant.

Il est important de noter que vous aurez besoin des autorisations appropriées pour pousser des changements vers un dépôt distant. Si vous travaillez en équipe, vous devrez peut-être coordonner avec les autres pour vous assurer d'avoir les autorisations nécessaires.

Pousser des changements vers un dépôt distant facilite la collaboration avec d'autres sur des projets de développement logiciel et garantit que vos membres d'équipe travaillent avec la dernière version de la base de code.

En suivant ces commandes de base, vous pouvez créer et valider des changements dans votre dépôt Git. Avec Git, vous pouvez facilement suivre les changements de votre base de code et collaborer avec d'autres sur des projets de développement logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/collaboration-vector-min.jpg align="left")

## Comment collaborer avec Git

Un avantage clé de l'utilisation de Git est sa capacité à faciliter la collaboration entre les développeurs. Git vous permet de travailler sur la même base de code avec d'autres simultanément, sans écraser les changements des autres développeurs.

Pour collaborer sur un projet Git, vous utilisez généralement un dépôt central qui sert de source de vérité pour le projet. Chaque développeur dispose d'une copie locale du dépôt sur sa machine, et ils apportent des changements et les valident dans leur dépôt local.

Lorsque vous êtes prêt à partager vos changements avec le reste de l'équipe, vous poussez vos changements vers le dépôt central. Les autres membres de l'équipe peuvent ensuite tirer ces changements vers leurs dépôts locaux.

### Qu'est-ce que les dépôts distants ?

Les dépôts distants sont un composant essentiel des flux de travail Git. Un *dépôt distant* est un dépôt sous contrôle de version qui est hébergé sur un serveur distant. Il peut être accessible et modifié par plusieurs développeurs depuis différents emplacements.

L'utilisation de dépôts distants vous permet de collaborer efficacement avec d'autres développeurs sur la même base de code, de partager votre travail avec d'autres et de suivre les changements apportés à la base de code au fil du temps.

Dans Git, les dépôts distants sont généralement hébergés sur des plateformes telles que GitHub, GitLab ou Bitbucket, et vous pouvez y accéder en utilisant la ligne de commande Git ou une interface utilisateur graphique.

Lorsque vous travaillez avec des dépôts distants, vous pouvez pousser vos changements locaux vers le dépôt distant ou tirer des changements du dépôt distant vers votre copie locale pour garder votre base de code à jour.

Git fournit des outils puissants pour gérer les dépôts distants, tels que la création de branches, la gestion des demandes de tirage et la résolution des conflits de fusion. Cela en fait un choix populaire pour les équipes de développement logiciel distribuées.

En utilisant des dépôts distants dans Git, vous pouvez collaborer avec d'autres sur des projets de développement logiciel et partager votre base de code avec eux.

### Comment cloner un dépôt

Le clonage d'un dépôt est une tâche courante lors de l'utilisation de Git. Le clonage crée une copie locale d'un dépôt distant, y compris tous les fichiers et l'historique du projet.

Le clonage d'un dépôt est simple dans Git, et vous pouvez le faire de plusieurs manières, telles que l'utilisation de la ligne de commande ou d'une interface utilisateur graphique. C'est un processus simple qui vous permet d'accéder au code du dépôt, à l'historique des validations et aux branches. Passons en revue les étapes impliquées dans le clonage d'un dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-clone.png align="left")

*Copier l'URL du dépôt*

1. **Copier l'URL du dépôt** : Commencez par obtenir l'URL du dépôt distant que vous souhaitez cloner. Vous pouvez trouver cette URL sur la plateforme d'hébergement du dépôt, telle que GitHub ou GitLab.
    
2. **Ouvrir un terminal ou une invite de commande.** Ouvrez votre interface de ligne de commande préférée. Cela pourrait être le Terminal sur macOS et Linux ou l'Invite de commande sur Windows.
    
3. **Naviguer vers l'emplacement souhaité** : Utilisez la commande `cd` pour naviguer vers le répertoire où vous souhaitez cloner le dépôt. Par exemple, si vous souhaitez le cloner dans le répertoire "Projects" sur votre bureau, vous exécuteriez `cd ~/Desktop/Projects`.
    

![Image](https://www.freecodecamp.org/news/content/images/2023/05/terminal-cd.png align="left")

*Changement de répertoire*

4. **Cloner le dépôt** : Exécutez la commande `git clone` suivie de l'URL du dépôt. Cette commande lance le processus de clonage et crée une copie locale du dépôt. Par exemple, pour cloner un dépôt avec l'URL, vous exécuteriez `git clone [https://github.com/username/repository.git](https://github.com/username/repository.git.)`[.](https://github.com/username/repository.git.)
    

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-cloning.png align="left")

*Clonage Git*

5. **Vérifier le processus de clonage** : Une fois le processus de clonage terminé, vous verrez les fichiers du dépôt et l'historique des validations dans le répertoire spécifié. Vous pouvez maintenant naviguer dans le dépôt cloné en utilisant `cd repository` (où le nom du répertoire est le même que celui du dépôt cloné).
    

Si vous observez le graphique ci-dessous, la commande `cd better-commits` change le répertoire en better-commits, qui a le même nom que le dépôt cloné, comme expliqué précédemment. Pour vérifier davantage s'il y a des fichiers clonés dans le répertoire, la commande `ls` est utilisée pour lister tous les fichiers dans le répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/verify-clone.png align="left")

*Vérifier* `git clone`

C'est tout ! Vous avez réussi à cloner un dépôt Git sur votre machine locale. Vous pouvez maintenant commencer à travailler avec le code, apporter des modifications et utiliser les fonctionnalités de contrôle de version de Git pour gérer votre projet efficacement.

La commande `git clone <URL du dépôt>` est utilisée pour créer une copie d'un dépôt Git distant sur votre machine locale. Elle vous permet de récupérer l'historique complet, les branches et les fichiers du dépôt distant et configure une copie locale avec laquelle vous pouvez travailler.

Voici ce que fait `git clone <URL du dépôt>` :

1. `git clone` : C'est une commande Git qui crée un clone ou une copie d'un dépôt Git distant.
    
2. `<URL du dépôt>` : Il s'agit de l'URL du dépôt distant que vous souhaitez cloner. Il pointe généralement vers le service d'hébergement de dépôt Git où se trouve le dépôt distant.
    

Lorsque vous exécutez la commande `git clone <URL du dépôt>`, elle crée un nouveau répertoire sur votre machine locale avec le même nom que le dépôt distant. Elle initialise un nouveau dépôt Git dans ce répertoire et copie tous les fichiers et l'historique des validations du dépôt distant dans le dépôt local.

De plus, la commande `git clone` configure automatiquement une connexion entre votre dépôt local et le dépôt distant. Elle configure le dépôt distant comme source amont par défaut et lui attribue le nom `origin`.

Le clonage de dépôts est une partie clé des flux de travail Git et un outil essentiel pour les équipes de développement logiciel distribuées, que vous collaboriez avec d'autres, contribuiez à des projets open source ou travailliez simplement sur vos projets. Il vous permet d'avoir une copie locale de la base de code et vous maintient synchronisé avec les derniers changements du dépôt distant.

### Comment pousser et tirer des changements dans Git

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-push-1.png align="left")

*Paramétrage de la branche amont Git Push*

La branche amont fait référence à la branche sur un dépôt distant à laquelle votre branche locale est associée. Elle représente la branche distante avec laquelle votre branche locale sera synchronisée lors de l'utilisation de commandes comme `git pull` ou `git push`.

Lorsque vous configurez une branche amont, elle établit une connexion entre votre branche locale et la branche correspondante dans le dépôt distant. Cette connexion vous permet de pousser et de tirer facilement des changements entre les branches locales et distantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-push2-1.png align="left")

*Git Push sans configurer de branche amont*

Inversement, lorsque vous souhaitez mettre à jour votre copie locale du dépôt avec les changements apportés par d'autres, vous pouvez tirer les changements du dépôt distant en utilisant la commande `git pull`. Tirer met à jour votre dépôt local avec les derniers changements apportés au dépôt distant.

Ces opérations sont essentielles pour collaborer sur un projet Git et maintenir la copie locale du dépôt de chacun à jour avec les derniers changements.

Git fournit des outils pour résoudre les conflits qui peuvent survenir lors de la poussée ou du tirage de changements, tels que la fusion de changements ou le choix des changements à conserver. En utilisant la poussée et le tirage dans les flux de travail Git, vous pouvez travailler plus efficacement et efficacement sur des projets de développement logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/best-practices-vector-min.jpg align="left")

## Bonnes pratiques pour utiliser Git

Pour tirer le meilleur parti de Git, il est important de suivre les meilleures pratiques lors de l'utilisation de l'outil.

Certaines bonnes pratiques incluent le maintien de validations petites et ciblées, l'utilisation de messages de validation clairs et concis, le branchement fréquent pour isoler les changements et réduire le risque de conflits, et l'utilisation de demandes de tirage pour les revues de code.

Il est également important de pousser régulièrement les changements vers le dépôt distant, de tirer les changements du dépôt distant et de maintenir la copie locale du dépôt à jour.

Examinons chacun de ces points un peu plus en détail maintenant.

### Maintenir les validations petites et ciblées

Lorsque vous travaillez avec Git, il est important de maintenir les validations petites et ciblées sur des changements ou fonctionnalités spécifiques. Cela facilite la compréhension de ce qui a été changé dans chaque validation et aide à réduire le risque de conflits.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/short-focused-commit.png align="left")

*Message de validation court*

Si une validation inclut plusieurs changements, il peut être difficile de comprendre le but de chaque changement et comment ils se rapportent les uns aux autres.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/long-commit.png align="left")

*Message de validation long*

En revanche, si une validation est ciblée sur un seul changement, il est beaucoup plus facile de comprendre le but de ce changement et de le restaurer si nécessaire. Maintenir les validations petites et ciblées facilite également la révision des changements et le suivi de la progression d'un projet au fil du temps.

Dans l'image graphique *Message de validation long* ci-dessus, vous pouvez voir qu'il y a jusqu'à trois changements qui ont été implémentés en fonction du message de validation : Le drapeau `-m` signifie message, et avec ce type de message, il serait difficile pour les développeurs examinant vos changements de code de se concentrer car plusieurs changements ont été implémentés en une seule validation.

Pour faciliter la révision des changements de code, limitez-vous à un seul changement, probablement le changement *Corriger le lien brisé dans le pied de page*. Ensuite, validez le changement en conséquence, comme dans l'image graphique *Message de validation court* ci-dessus.

Faire cela facilitera le processus de flux de travail pour vos membres d'équipe, et ils apprécieront de travailler avec vous.

### Utiliser des messages de validation clairs et concis

Lorsque vous apportez des changements à une base de code, il est important d'utiliser des messages de validation clairs et concis qui décrivent les changements que vous avez apportés et pourquoi.

Un bon message de validation doit fournir suffisamment d'informations pour comprendre le contexte du changement sans être trop long ou verbeux. Des messages de validation clairs et concis facilitent la compréhension par d'autres développeurs de ce que vous avez changé et pourquoi, ce qui est particulièrement important lors de la révision des changements ou de l'investigation des problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-commit3.png align="left")

*Message de validation concis*

Comme nous l'avons discuté dans les sections précédentes, chaque validation doit être limitée à un seul changement dans le code. Maintenir les messages de validation simples et succincts renforce cela en aidant vos membres d'équipe à comprendre ce que chacune de vos validations concerne.

Un excellent message de validation doit comporter moins de 10 mots. Lorsque votre message de validation devient plus long, il commence à devenir trop verbeux, et le message principal de la validation peut être perdu.

Voici des exemples de messages de validation clairs et efficaces :

* Mettre à jour les dépendances vers les dernières versions
    
* Ajouter une gestion des erreurs pour la connexion à la base de données
    
* Supprimer les instructions console.log de débogage
    
* Mettre à jour le style pour la réactivité mobile
    
* Refactoriser les noms de variables pour plus de clarté
    

```bash
git commit -m 'Mettre à jour les dépendances vers les dernières versions'
git commit -m 'Ajouter une gestion des erreurs pour la connexion à la base de données'
git commit -m 'Supprimer les instructions console.log de débogage'
git commit -m 'Mettre à jour le style pour la réactivité mobile'
git commit -m 'Refactoriser les noms de variables pour plus de clarté'
```

L'utilisation de bons messages de validation facilite également le suivi des changements au fil du temps et la compréhension de l'historique d'un projet.

En suivant cette meilleure pratique, vous pouvez améliorer la qualité et la maintenabilité de votre base de code et faciliter le travail avec le code pour vous-même et les autres à l'avenir.

### Brancher fréquemment pour isoler les changements

Le branchement est une fonctionnalité puissante de Git qui vous permet de travailler sur différents changements ou fonctionnalités en isolation de la base de code principale. En créant une branche pour chaque changement ou fonctionnalité, vous pouvez apporter et tester des changements sans affecter la base de code principale, et fusionner vos changements dans la base de code principale une fois les changements terminés.

Le branchement fréquent facilite également la gestion des changements et la collaboration avec d'autres développeurs. Par exemple, si plusieurs développeurs travaillent sur différents changements, chacun peut créer sa propre branche et les fusionner dans la base de code principale une fois leurs changements terminés.

Le branchement fréquent en CI/CD (Intégration Continue/Déploiement Continu) est une meilleure pratique qui implique la création de branches séparées pour isoler les changements. Il permet un développement parallèle, permettant aux équipes de travailler indépendamment sur différentes fonctionnalités ou corrections de bugs sans conflit. En travaillant sur des branches isolées, les développeurs peuvent se concentrer sur leurs changements spécifiques, exécuter des tests et assurer la stabilité.

Cette approche facilite l'intégration sans risque, car les changements sont soigneusement testés au sein des branches avant d'être fusionnés dans la base de code principale. Le branchement fréquent favorise une collaboration efficace, accélère les cycles de développement et améliore la qualité globale du logiciel en fournissant un environnement contrôlé pour les changements individuels.

Pour créer une branche, utilisez la commande `git branch <nom-de-la-branche>` dans votre terminal. Pour basculer vers la nouvelle branche, utilisez `git checkout <nom-de-la-branche>`. Vous pouvez également combiner ces deux étapes en une seule commande : `git checkout -b <nom-de-la-branche>`. Cette commande créera la branche et basculera simultanément vers la branche nouvellement créée.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-branch.png align="left")

*Branchement Git*

Observez dans l'image graphique *Branchement Git* ci-dessus que la commande `git checkout -b stellar-feature` a créé et basculé vers la branche `stellar-feature` simultanément. Cela est différent de la création de la branche moonshot-experiment avec la commande `git branch moonshot-experiment` puis de basculer vers celle-ci avec la commande `git checkout moonshot-experiment`.

En suivant cette meilleure pratique, vous pouvez réduire le risque de conflits et d'erreurs dans votre base de code.

### Utiliser les demandes de tirage pour les revues de code

Les revues de code sont une partie essentielle du processus de développement logiciel. Elles aident à garantir que les changements de code sont de haute qualité, suivent les meilleures pratiques et répondent aux exigences du projet.

Une façon de faciliter les revues de code est d'utiliser les demandes de tirage. Les demandes de tirage vous permettent de partager vos changements avec d'autres et de demander des commentaires avant de les fusionner dans la base de code principale.

En utilisant les demandes de tirage, d'autres développeurs peuvent examiner vos changements, fournir des commentaires et suggérer des améliorations. Les demandes de tirage facilitent également le suivi des changements et garantissent que les changements de code sont correctement testés et documentés avant d'être fusionnés.

L'utilisation de demandes de tirage (PR) pour les revues de code dans les projets open source permet la collaboration et le contrôle de qualité. Les développeurs créent une branche, apportent des modifications, les poussent vers un dépôt bifurqué et soumettent une PR. Les réviseurs fournissent des commentaires, suggèrent des modifications et discutent des améliorations. Une fois approuvées, les modifications sont fusionnées dans le projet principal, garantissant une base de code robuste et bien révisée.

Les PR favorisent l'implication de la communauté et permettent aux responsables de projet de garantir la qualité du code et de maintenir les normes de codage.

Les PR pour les revues de code sont principalement appliquées dans deux situations :

* Travailler sur un projet avec des membres d'équipe dans votre entreprise
    
* Aider à améliorer les projets open source par le biais de corrections de bugs et l'ajout de nouvelles fonctionnalités.
    

Et ces projets open source peuvent même être des bibliothèques ou des frameworks (par exemple, React, Vue, et autres) avec lesquels vous travaillez pour construire des applications.

#### Travailler sur des projets avec des membres d'équipe

En s'appuyant sur les meilleures pratiques que nous avons discutées précédemment, créez une nouvelle branche et basculez vers celle-ci avec la commande `git checkout -b blackhole-security`. À ce stade, vous pouvez commencer à travailler sur le projet et vous assurer de vous en tenir à travailler sur la fonctionnalité pour laquelle vous avez créé la branche.

Cela signifie que vous ne devez travailler que sur la fonctionnalité *blackhole-security* dans le projet ; ne commencez pas à construire une fonctionnalité comme *supernova-optimization*. Cela facilitera la révision de votre code par le réviseur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/git-pr.png align="left")

*Demande de tirage Git*

Une fois que vous avez terminé de travailler sur la fonctionnalité *blackhole-security*, préparez et validez les changements avec la commande `git commit -am 'Blackhole security fully implemented'`. À ce stade, vous pouvez maintenant pousser votre changement vers le dépôt distant pour que votre chef de projet le révise. Vous pouvez le faire avec la commande `git push origin blackhole-security`. Ou si vous travailliez sur une branche nommée *planet-discovery*, vous utiliseriez la commande `git push origin planet-discovery`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image-pr.png align="left")

*Comparer & Demande de tirage*

L'image graphique **Comparer & Demande de tirage** ci-dessus, comme vous pouvez le voir dans le rectangle rouge, a un bouton à cliquer pour créer une demande de tirage.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/FireShot-Capture-143---Comparing-master...blackhole-security---Kola92_git-for-beginners---github.com.png align="left")

*Ouvrir la demande de tirage*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/FireShot-Capture-144---Blackhole-security-by-Kola92---Pull-Request--1---Kola92_git-for-begin_---github.com.png align="left")

*Fusionner la demande de tirage*

L'image graphique **Ouvrir la demande de tirage** ci-dessus a le bouton **Créer une demande de tirage** pour ouvrir la demande de tirage pour la révision de code. Avec l'image graphique **Fusionner la demande de tirage**, c'est l'écran où votre réviseur de code fournit des commentaires si nécessaire avant de fusionner votre PR dans la branche *master*.

#### Travailler sur des projets open source

Avant de commencer la collaboration sur un projet open source, vous devrez bifurquer le dépôt open source (une bifurcation est une copie personnelle d'un dépôt qui permet un développement et une contribution indépendants sans altérer le code source).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/FireShot-Capture-145---Fork-imartinez_privateGPT---github.com.png align="left")

*Créer une nouvelle bifurcation*

Lorsque le dépôt a terminé la bifurcation, vous pouvez cloner le dépôt bifurqué `git clone [https://github.com/Kola92/privateGPT.git](https://github.com/Kola92/privateGPT.git.)`[.](https://github.com/Kola92/privateGPT.git.)

Une fois que le dépôt bifurqué a été cloné sur votre machine locale, vous pouvez créer une branche et basculer vers celle-ci. Ensuite, vous pouvez commencer à travailler sur le projet en validant, en poussant vers le dépôt distant et en créant une PR pour la révision de code.

Les bonnes PR aident à améliorer la qualité et la maintenabilité de votre base de code et garantissent que les changements sont correctement révisés et approuvés avant d'être fusionnés.

### Maintenir le dépôt propre et à jour

Un dépôt propre et à jour est crucial pour maintenir la santé et l'utilisabilité de votre base de code.

Une façon de maintenir le dépôt propre est d'éviter de valider des fichiers inutiles, tels que des fichiers temporaires ou des artefacts de construction. Cela maintient le dépôt petit et facilite la navigation. Les fichiers suivants sont considérés comme inutiles :

* Fichiers ou répertoires spécifiques à l'IDE (par exemple, .idea, .vscode) qui sont utilisés pour les configurations de l'environnement de développement local.
    
* Fichiers temporaires ou fichiers de sauvegarde créés par des éditeurs de texte ou d'autres outils (par exemple, .bak, .tmp).
    
* Répertoires de dépendances ou de packages (par exemple, node\_modules, vendor) qui peuvent être régénérés en utilisant des gestionnaires de packages.
    
* Fichiers de configuration contenant des informations sensibles (par exemple, clés API, et mots de passe). Utilisez des variables d'environnement ou des fichiers de configuration en dehors du dépôt pour ces données sensibles.
    
* Artefacts de construction ou répertoires de sortie (par exemple, dist, build) qui peuvent être régénérés pendant le processus de construction.
    

Pour éviter de valider des fichiers inutiles dans un dépôt, suivez ces étapes :

1. Créez un fichier `.gitignore` dans le répertoire racine de votre dépôt.
    
2. Ouvrez le fichier `.gitignore` dans un éditeur de texte.
    
3. Listez les noms de fichiers, répertoires ou motifs de fichiers que vous souhaitez exclure du contrôle de version, chacun sur une nouvelle ligne.
    
4. Enregistrez le fichier `.gitignore`.
    

Les motifs courants à inclure dans `.gitignore` sont :

* Noms de répertoires (par exemple, `node_modules/`, `dist/`, `build/`)
    
* Extensions de fichiers (par exemple, `*.log`, `*.tmp`, `.env`)
    
* Fichiers spécifiques (par exemple, `secrets.txt`, `config.ini`)
    

![Image](https://www.freecodecamp.org/news/content/images/2023/05/gitignore.png align="left")

*Création du fichier* `.gitignore`

Assurez-vous que le fichier `.gitignore` est validé et poussé vers le dépôt. Git exclura alors automatiquement les fichiers et répertoires listés de la préparation ou de la validation.

Passez régulièrement en revue et mettez à jour le fichier `.gitignore` à mesure que de nouveaux fichiers ou répertoires deviennent inutiles à inclure dans le dépôt. Cette pratique aide à maintenir un historique de contrôle de version propre et ciblé.

#### Raisons d'éviter de valider des fichiers inutiles

Comme mentionné précédemment, éviter les fichiers inutiles dans un dépôt est crucial pour maintenir l'efficacité, la sécurité et la collaboration. Voici quelques raisons pour lesquelles c'est important :

1. **Taille du dépôt réduite** : Les fichiers inutiles peuvent alourdir la taille du dépôt, rendant le clonage et la récupération plus lents pour les collaborateurs.
    
2. **Performance améliorée** : Les grands dépôts avec des fichiers inutiles peuvent affecter la performance de diverses opérations Git, telles que le branchement, la fusion et la navigation dans l'historique.
    
3. **Collaboration améliorée** : Exclure les fichiers inutiles garantit que seul le code et les actifs pertinents sont partagés entre les membres de l'équipe, améliorant la collaboration et réduisant la confusion.
    
4. **Clarté du contrôle de version** : En omettant les fichiers inutiles, l'historique du contrôle de version reste ciblé sur les changements significatifs, facilitant la compréhension et la révision de la chronologie de développement.
    
5. **Sécurité et confidentialité** : Éviter l'inclusion d'informations sensibles, telles que les clés API ou les mots de passe, dans le dépôt aide à maintenir la sécurité et la confidentialité.
    
6. **Maintenance et déploiement plus faciles** : Lorsque les fichiers inutiles sont exclus, les tâches de maintenance, telles que le clonage ou le déploiement du dépôt, deviennent plus rapides et plus rationalisées.
    

De plus, il est important de maintenir le dépôt à jour en tirant régulièrement les changements de la branche principale et en résolvant les conflits. Cela prévient les conflits de fusion et garantit que tout le monde travaille avec la version la plus récente du code.

En suivant ces meilleures pratiques, vous pouvez travailler plus efficacement et collaborativement sur des projets Git, réduire le risque d'erreurs et de conflits, et maintenir votre base de code propre et maintenable.

## Conclusion

Dans ce tutoriel, nous avons couvert certaines des meilleures pratiques pour utiliser Git afin de gérer vos projets de développement logiciel.

Nous avons discuté de l'importance du contrôle de version et de la manière dont Git peut vous aider à suivre les changements apportés à votre base de code. Nous avons également couvert les commandes de base pour créer et valider les changements, et comment travailler avec des dépôts distants. Enfin, nous avons discuté de certaines des meilleures pratiques pour utiliser Git, y compris le maintien de validations petites et ciblées, l'utilisation de messages de validation clairs et concis, le branchement fréquent pour isoler les changements, et l'utilisation de demandes de tirage pour les revues de code.

Bien que nous ayons couvert certaines des bases de Git, il y a beaucoup plus à apprendre et à explorer. Git est un outil puissant qui peut vous aider à gérer des projets de développement logiciel complexes, à collaborer avec d'autres développeurs et à rationaliser votre flux de travail.

Je vous encourage à continuer à apprendre sur Git et à explorer ses capacités. En faisant cela, vous pouvez devenir un développeur plus efficace et plus performant, et améliorer la qualité et la maintenabilité de votre base de code.

Que vous soyez débutant ou développeur expérimenté, il y a toujours quelque chose de nouveau à apprendre sur Git. Alors continuez à explorer, continuez à expérimenter, et continuez à repousser les limites de ce que vous pouvez faire avec Git.