---
title: Comment utiliser Git et GitHub – Les bases du contrôle de version pour débutants
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-07-12T16:55:20.000Z'
originalURL: https://freecodecamp.org/news/git-and-github-the-basics
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/git-github.png
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment utiliser Git et GitHub – Les bases du contrôle de version pour
  débutants
seo_desc: 'A Version Control System is a tool you use to track, make, and manage changes
  to your software code. It''s also called source control.

  A version control system helps developers store every change they make to a file
  at different stages so they and the...'
---

Un système de contrôle de version est un outil que vous utilisez pour suivre, créer et gérer les modifications de votre code logiciel. On l'appelle aussi contrôle de source.

Un système de contrôle de version aide les développeurs à stocker chaque modification qu'ils apportent à un fichier à différentes étapes, afin qu'eux et leurs coéquipiers puissent récupérer ces modifications plus tard.

Il existe trois types de systèmes de contrôle de version, qui sont :

* Systèmes de contrôle de version locaux

* Systèmes de contrôle de version centralisés

* Systèmes de contrôle de version distribués.

## Qu'est-ce qu'un système de contrôle de version local (LVCS) ?

Il s'agit d'un type de système de contrôle de version très courant et simple à utiliser. Mais cette méthode est assez sujette aux erreurs et aux attaques car les fichiers sont stockés dans votre système local.

Cela signifie que vous pourriez perdre le fichier système ou oublier accidentellement le répertoire/dossier du fichier sur lequel vous travaillez (et écrire dans un autre répertoire).

## Qu'est-ce qu'un système de contrôle de version centralisé (CVCS) ?

Dans ce type de contrôle de version, un serveur agit comme un dépôt qui stocke chaque version du code. Le CVCS aide différents développeurs à collaborer ensemble.

Malgré la collaboration et la communication utiles entre les développeurs, si un serveur tombe en panne pendant quelques secondes ou est corrompu, il y a un risque de perdre votre travail. Malheureusement, c'est un très gros problème avec le CVCS.

Dans le CVCS, seuls quelques développeurs peuvent travailler ensemble sur un projet.

## Qu'est-ce qu'un système de contrôle de version distribué (DVCS) ?

Il s'agit du type de système de contrôle de version le plus récent et le plus couramment utilisé de nos jours.

Dans un DVCS, tous les développeurs disposent d'une sauvegarde complète (clone) de toutes les données du serveur. Cela signifie que chaque fois que le serveur est hors service ou défectueux, vous pouvez toujours travailler sur votre projet et vous pouvez copier ou sauvegarder vos dépôts sur le serveur pour les restaurer.

Lorsque vous utilisez un DVCS, de nombreux développeurs peuvent travailler ensemble sur un projet. Un DVCS populaire est Git, dont nous allons parler plus en détail maintenant.

## Qu'est-ce que Git ?

Git est un système de contrôle de version distribué gratuit et open source que vous pouvez utiliser pour suivre les modifications de vos fichiers. Vous pouvez travailler sur tous types de projets dans Git, des petits aux grands.

Avec Git, vous pouvez ajouter des modifications à votre code et ensuite les valider (ou les sauvegarder) lorsque vous êtes prêt. Cela signifie que vous pouvez également revenir aux modifications que vous avez faites précédemment.

Git fonctionne main dans la main avec GitHub – alors, qu'est-ce que GitHub ?

## Qu'est-ce que GitHub ?

GitHub est une interface web où vous stockez vos dépôts Git et suivez et gérez vos modifications de manière efficace. Il donne accès au code à divers développeurs travaillant sur le même projet. Vous pouvez apporter vos propres modifications à un projet en même temps que d'autres développeurs apportent les leurs.

Si vous faites accidentellement une erreur dans le code de votre projet en apportant des modifications, vous pouvez facilement revenir à l'étape précédente où l'erreur ne s'est pas encore produite.

## Pourquoi utiliser GitHub

Il y a tant de raisons pour lesquelles vous devriez apprendre et utiliser GitHub. Examinons-en quelques-unes maintenant.

### Gestion de projet efficace

GitHub est un endroit où vos dépôts Git sont stockés. GitHub facilite la tâche des développeurs travaillant sur le même projet mais dans différents endroits pour être sur la même longueur d'onde.

Avec GitHub, vous pouvez facilement suivre et gérer les modifications que vous avez apportées et vérifier les progrès que vous avez réalisés dans votre projet.

### Collaboration et coopération faciles

Avec GitHub, des développeurs du monde entier peuvent travailler ensemble sur un projet sans rencontrer de problèmes.

Les équipes peuvent rester sur la même longueur d'onde tout en travaillant ensemble sur un projet et peuvent facilement organiser et gérer le projet de manière efficace.

### Open Source

GitHub est un système gratuit et open source. Cela signifie que les développeurs peuvent facilement accéder à différents types de code/projets qu'ils peuvent utiliser pour apprendre et développer leurs compétences.

### Polyvalence

Cet attribut de GitHub est très important. GitHub n'est pas une interface web uniquement pour les développeurs. Il peut être utilisé par des designers, des écrivains et toute personne souhaitant suivre l'historique de leurs projets.

## Comment installer Git

Pour commencer à utiliser Git, vous devrez le télécharger sur votre ordinateur si ce n'est pas déjà fait. Vous pouvez le faire en vous rendant sur leur site officiel [website](https://git-scm.com/).

Lorsque Git s'ouvre, faites défiler un peu vers le bas et vous devriez voir un bouton de téléchargement. Allez-y et cliquez dessus.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-23-44-196-1.jpg align="left")

*Bouton de téléchargement sur le site Git*

Choisissez votre système d'exploitation, qu'il s'agisse de Windows, MacOS, Linux/Unix. Dans mon cas, je vais choisir l'option Windows car j'utilise un ordinateur Windows :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-24-33-919.jpg align="left")

*Choisissez votre système d'exploitation*

Cliquez sur le premier lien en haut de la page pour télécharger la dernière version de Git.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-25-06-107.jpg align="left")

*Téléchargez la dernière version de Git en cliquant sur le premier lien*

Lorsque le téléchargement est terminé, procédez à l'installation de Git sur votre ordinateur. Vous devrez vous rendre à l'emplacement où le fichier a été téléchargé et l'installer.

Après l'installation, vous voudrez vous assurer que Git est correctement installé sur votre système. Ouvrez votre invite de commande ou Git bash (celui que vous choisissez d'utiliser) et exécutez la commande :

`git --version`

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-48-13-907.jpg align="left")

Si Git a été correctement installé sur votre ordinateur, il devrait afficher la version actuelle de Git sous la commande que vous venez d'exécuter. Si la version actuelle est affichée, félicitations !

## Comment configurer Git

Maintenant que nous avons installé Git sur notre ordinateur, nous devons le configurer. Nous faisons cela afin que chaque fois que nous travaillons en équipe sur un projet, nous puissions facilement identifier les commits que nous avons faits dans le dépôt.

Pour configurer Git, nous devons spécifier le nom, l'adresse e-mail et la branche en utilisant la commande `git config --global`. Par exemple :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/MINGW64__c_Users_me-7_7_2022-2_38_36-AM.png align="left")

Sur l'image ci-dessus, nous avons utilisé `git config --global user.name` pour configurer le nom d'utilisateur. Dans mon cas, j'ai utilisé mon nom « Derek Emmanuel ». Le même principe s'applique pour `git config --global user.email`.

Git vient avec une branche par défaut appelée master, donc je l'ai changée pour qu'elle s'appelle main en utilisant la commande `git config --global init.default branch main`.

Vous êtes maintenant prêt à commencer à utiliser Git.

## Comment créer un compte GitHub

Pour créer un compte GitHub, visitez leur [site officiel](https://github.com/). Cliquez sur le bouton d'inscription dans le coin supérieur droit :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-27-35-732.jpg align="left")

Lorsque le formulaire d'inscription s'ouvre, entrez votre e-mail, créez un mot de passe, entrez votre nom d'utilisateur, puis vérifiez votre compte avant de cliquer sur le bouton créer un compte.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-05-20-35-26-646.jpg align="left")

*Créez votre compte GitHub*

## Commandes Git couramment utilisées

Il existe certaines commandes Git de base que tout développeur devrait savoir utiliser :

* `git config`

* `git init`

* `git add`

* `git commit`

* `git clone`

* `git push`

* `git rm`

* `git branch`

Passons brièvement en revue chacune de ces commandes afin que vous sachiez comment les utiliser.

### Comment utiliser la commande `git config`

Vous utilisez cette commande pour définir le nom d'utilisateur, l'e-mail et la branche d'un utilisateur afin d'identifier qui a fait un commit lors du travail sur un projet. Cette commande est utilisée lorsque vous avez téléchargé Git sur votre ordinateur et que vous souhaitez le personnaliser pour votre usage.

Par exemple :

`git config --global user.name "[nom d'utilisateur]"`

`git config --global user.email [adresse e-mail]`

### Comment utiliser la commande `git init`

Vous utilisez la commande `git init` pour démarrer Git dans votre projet. Cette commande Git est utilisée lorsque vous travaillez sur un projet et que vous souhaitez initialiser Git pour le projet afin de suivre les modifications apportées au projet.

Par exemple :

`git init`

Lorsque vous exécutez cette commande, vous devriez voir un dossier nommé `.git` créé automatiquement dans le dossier actuel dans lequel vous travaillez.

### Comment utiliser la commande `git add`

Cette commande ajoute votre fichier à la zone de staging. La zone de staging est la zone où les fichiers que nous modifions sont ajoutés et où ils attendent le prochain commit.

Pour ajouter un fichier à la zone de staging, vous utilisez la commande `git add`. Elle ajoute tous les fichiers du dossier à la zone de staging.

`git add (nom du fichier)` ajoute le nom du fichier particulier que vous souhaitez commiter dans la zone de staging.

Utilisez cette commande lorsque vous avez apporté des modifications à un fichier et que vous souhaitez les commiter dans votre projet.

### Comment utiliser la commande `git commit`

Cela commite tout fichier que vous avez ajouté avec la commande `git add` ainsi que chaque fichier dans la zone de staging.

Par exemple :

`git commit –m "premier commit"`

Cette commande sauvegarde un fichier de manière permanente dans le dépôt Git. Vous l'utilisez chaque fois qu'un fichier a été ajouté à la zone de staging en utilisant la commande `git add`.

### Comment utiliser la commande `git clone`

Vous utilisez la commande `git clone` pour copier un dépôt existant dans un autre emplacement vers l'emplacement actuel où vous souhaitez qu'il soit.

Par exemple :

`git clone (nom du dépôt)`

Vous utilisez cette commande lorsque vous souhaitez dupliquer un dépôt Git de GitHub dans votre stockage local.

### Comment utiliser la commande `git push`

Vous utilisez cette commande pour télécharger/pousser des fichiers du dépôt/stockage local vers un autre stockage, comme un stockage distant tel que GitHub.

Par exemple :

`git push (nom du stockage distant)`

Vous n'utilisez cette commande que lorsque vous êtes satisfait des modifications et des commits que vous avez faits sur un projet et que vous souhaitez enfin le télécharger/pousser vers le dépôt Git dans GitHub.

### Comment utiliser la commande `git rm`

Vous utilisez cette commande Git pour supprimer un fichier d'un dépôt de travail. Par exemple :

`git rm (nom du fichier)`

Vous utilisez cette commande uniquement lorsque vous souhaitez vous débarrasser de modifications/fichiers indésirables du dépôt Git.

### Comment utiliser la commande `git branch`

Vous utilisez cette commande pour vérifier la branche actuelle sur laquelle vous travaillez, soit `main` soit `master`. Par exemple :

`git branch`

Cette commande vous aide à connaître la branche actuelle sur laquelle vous travaillez.

## Conclusion

Dans ce tutoriel, vous avez appris ce que sont les systèmes de contrôle de version. Vous avez également appris comment installer et configurer Git sur votre ordinateur et créer un compte GitHub. Enfin, nous avons passé en revue certaines commandes Git couramment utilisées.

Si vous souhaitez approfondir Git et GitHub, vous pouvez consulter [ce cours sur la chaîne YouTube freeCodeCamp](https://www.freecodecamp.org/news/git-and-github-crash-course/).

J'espère que ce tutoriel vous a été utile.

Amusez-vous bien à coder !