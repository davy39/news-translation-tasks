---
title: Comment héberger votre projet sur GitHub – Expliqué avec des exemples
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2024-08-08T11:37:16.000Z'
originalURL: https://freecodecamp.org/news/host-your-first-project-on-github
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-11.47.51-PM.png
tags:
- name: deployment
  slug: deployment
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Web Hosting
  slug: web-hosting
seo_title: Comment héberger votre projet sur GitHub – Expliqué avec des exemples
seo_desc: 'Seven years ago, I began my journey into web development with HTML and
  CSS. As soon as I got the hang of JavaScript, I built my first website. The excitement
  was overwhelming, and I wanted to share it with my friends and the world.

  Like many beginner...'
---

Il y a sept ans, j'ai commencé mon parcours en développement web avec HTML et CSS. Dès que j'ai compris JavaScript, j'ai construit mon premier site web. L'excitation était débordante, et je voulais le partager avec mes amis et le monde.

Comme beaucoup de débutants, j'ai commencé à rechercher des plateformes d'hébergement, pour découvrir le coût des domaines et de l'hébergement. C'est alors que j'ai découvert Git et GitHub, réalisant que je pouvais partager mes projets sans dépenser un centime.

Si vous êtes dans la même situation, incertain quant à Git et GitHub et comment partager vos projets, cet article est pour vous. C'est le guide que j'aurais souhaité avoir il y a sept ans.

Pour démontrer la puissance de Git et GitHub, nous utiliserons un projet réel comme exemple. Prenons le projet "IP Address Tracker application" de [ce tutoriel freeCodeCamp](https://www.freecodecamp.org/news/learn-rest-apis-javascript-project/#practical-example-how-to-build-a-web-application-with-a-public-rest-api). Vous pouvez télécharger le code source du projet [ici](https://github.com/iamspruce/ip-address-tracker/).

Si vous avez suivi le tutoriel et construit le projet, ou si vous avez un projet que vous souhaitez partager, cet article est pour vous. Nous vous guiderons à travers les étapes pour héberger votre projet sur GitHub, le rendant accessible au monde entier.

## Table des matières

1. [Public](#heading-public)
    
2. [Connaissances préalables](#heading-connaissances-prealables)
    
3. [Commencer avec Git et GitHub](#heading-commencer-avec-git-et-github)
    
    1. [Qu'est-ce que Git ?](#heading-quest-ce-que-git)
        
    2. [Qu'est-ce que GitHub ?](#heading-quest-ce-que-github)
        
4. [Comment configurer Git et GitHub](#heading-comment-configurer-git-et-github)
    
    1. [Comment installer Git sur Windows](#heading-comment-installer-git-sur-windows)
        
    2. [Comment installer Git sur macOS](#heading-comment-installer-git-sur-macos)
        
    3. [Comment installer Git sur Linux](#heading-comment-installer-git-sur-linux)
        
    4. [Comment créer un compte GitHub](#heading-comment-creer-un-compte-github)
        
    5. [Comment configurer Git](#heading-comment-configurer-git)
        
5. [Comment initialiser un dépôt Git](#heading-comment-initialiser-un-depot-git)
    
    1. [Étape 1 : Télécharger et ouvrir votre projet](#heading-etape-1-telecharger-et-ouvrir-votre-projet)
        
    2. [Étape 2 : Ouvrir le projet dans VS Code](#heading-etape-2-ouvrir-le-projet-dans-vs-code)
        
    3. [Étape 3 : Ouvrir le terminal dans VS Code](#heading-etape-3-ouvrir-le-terminal-dans-vs-code)
        
    4. [Étape 4 : Initialiser un dépôt Git](#heading-etape-4-initialiser-un-depot-git)
        
6. [Comment suivre les changements avec Git](#heading-comment-suivre-les-changements-avec-git)
    
    1. [Préparer les changements avec git add](#heading-preparer-les-changements-avec-git-add)
        
        1. [Ajouter des fichiers individuels](#heading-ajouter-des-fichiers-individuels)
            
        2. [Ajouter tous les changements à la fois](#heading-ajouter-tous-les-changements-a-la-fois)
            
    2. [Enregistrer les changements avec git commit](#heading-enregistrer-les-changements-avec-git-commit)
        
7. [Comment pousser votre projet sur GitHub](#heading-comment-pousser-votre-projet-sur-github)
    
    1. [Étape 1 : Créer un nouveau dépôt sur GitHub](#heading-etape-1-creer-un-nouveau-depot-sur-github)
        
    2. [Étape 2 : Lier votre dépôt local à GitHub](#heading-etape-2-lier-votre-depot-local-a-github)
        
    3. [Étape 3 : Pousser vos changements locaux sur GitHub](#heading-etape-3-pousser-vos-changements-locaux-sur-github)
        
    4. [Étape 4 : Vérifier votre dépôt sur GitHub](#heading-etape-4-verifier-votre-depot-sur-github)
        
8. [Comment héberger votre projet sur GitHub Pages](#heading-comment-heberger-votre-projet-sur-github-pages)
    
    1. [Qu'est-ce que GitHub Pages ?](#heading-quest-ce-que-github-pages)
        
    2. [Comment activer GitHub Pages](#heading-comment-activer-github-pages)
        
    3. [Comment obtenir l'URL de votre site GitHub Pages](#heading-comment-obtenir-lurl-de-votre-site-github-pages)
        
    4. [Comment mettre à jour votre site GitHub Pages](#heading-comment-mettre-a-jour-votre-site-github-pages)
        
9. [Conclusion](#heading-conclusion)
    

## Public

Ce guide est destiné aux développeurs débutants qui ont commencé à apprendre HTML, CSS et JavaScript et qui souhaitent apprendre à partager leurs projets en utilisant Git et GitHub.

## Connaissances préalables

Avant de vous lancer, assurez-vous d'être familier avec :

* Les opérations de base en ligne de commande.
    
* Les bases de HTML, CSS et JavaScript.
    
* Un éditeur de texte comme VS Code.
    

## Commencer avec Git et GitHub

Je ne vais pas essayer de vous ennuyer avec les différences entre Git et GitHub. Je suis sûr qu'il existe de nombreuses ressources sur le web couvrant déjà ce sujet, mais du point de vue d'un débutant, voici ce qu'ils sont :

### Qu'est-ce que Git ?

Git est un outil qui vous aide à suivre toutes les modifications que vous apportez au code de votre projet. Imaginez que vous construisez un site web sur les chats. Si vous changez le titre du site de "Cat Facts" à "All About Cats", Git se souviendra du changement. Si vous décidez plus tard que vous préférez "Cat Facts", Git vous permet de revenir facilement à cette version.

C'est comme avoir un enregistrement de chaque modification, ajout et suppression que vous faites à votre projet, afin que vous puissiez toujours revenir aux versions précédentes et faire des changements en toute confiance.

### Qu'est-ce que GitHub ?

GitHub est comme un album de coupures basé sur le cloud pour votre code. C'est un enregistrement en ligne où vous sauvegardez chaque modification, ajout et suppression que vous faites à votre projet, afin que vous puissiez y accéder de n'importe où et le partager avec d'autres.

Imaginez avoir une armoire de classement numérique où vous pouvez stocker et gérer différentes versions de votre site web. Vous pouvez inviter des amis à voir et même à vous aider avec votre projet, ce qui facilite la collaboration. GitHub suit les changements et garde tout organisé, donc si quelque chose ne va pas, vous pouvez toujours revenir à une version précédente.

## Comment configurer Git et GitHub

Maintenant que nous savons ce que sont Git et GitHub, configurons-les sur votre ordinateur. Suivez ces instructions étape par étape :

### Comment installer Git sur Windows

Vous pouvez télécharger l'installateur de Git [ici](https://git-scm.com/).

Exécutez l'installateur et suivez les instructions d'installation, en gardant les paramètres par défaut.

### Comment installer Git sur macOS

Ouvrez le Terminal sur votre Mac. Vous pouvez le trouver dans Applications > Utilitaires ou utiliser Spotlight pour le rechercher.

Installez Git en utilisant Homebrew en copiant et collant les commandes suivantes :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

Sortie :

```bash
==> Downloading https://github.com/Homebrew/brew/tarballs/...
==> Installing git
==> Pouring git-2.43.0.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/git/2.30.1: 1,434 files, 43.8MB
```

### Comment installer Git sur Linux

Ouvrez le Terminal sur votre machine Linux. Utilisez ensuite le gestionnaire de paquets de votre distribution pour installer Git.

Par exemple, sur Ubuntu, copiez et collez les commandes suivantes :

```bash
sudo apt-get update
sudo apt-get install git
```

Sortie :

```plaintext
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
git-man liberror-perl
Suggested packages:
git-daemon-run git-daemon-sysvinit git-doc git-el git-email git-gui gitk
gitweb git-mediawiki git-arch git-cvs git-svn git-hg
The following NEW packages will be installed:
git git-man liberror-perl
0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
Need to get 7,841 kB of archives.
After this operation, 43.8 MB of additional disk space will be used.
```

Pour vérifier l'installation, ouvrez le Terminal (s'il n'est pas déjà ouvert) et tapez la commande suivante pour vérifier l'installation :

```bash
git --version
```

Sortie :

```bash
git version 2.43.0
```

Vous devriez voir la version installée de Git affichée.

### Comment créer un compte GitHub

* Allez sur [GitHub](https://github.com/) et cliquez sur "Sign up".
    
* Suivez les instructions pour créer votre compte, choisissez un nom d'utilisateur et un mot de passe, et vérifiez votre email.
    
* Une fois votre compte configuré, personnalisez votre profil avec une biographie, une photo de profil et des liens vers votre site web personnel ou vos réseaux sociaux.
    

### Comment configurer Git

Ouvrez le Terminal et configurez Git avec le même nom d'utilisateur et email que votre compte GitHub :

```bash
git config --global user.name "Votre nom d'utilisateur GitHub"
git config --global user.email "votre.email@example.com"
```

Aucune sortie ne sera affichée, mais Git stockera vos identifiants pour une utilisation future.

## Comment initialiser un dépôt Git

Maintenant que vous avez configuré Git et GitHub, commençons par initialiser Git dans un projet. Vous pouvez utiliser n'importe quel projet de votre choix ou suivre avec notre exemple en utilisant le projet "IP Address Tracker".

### Étape 1 : Télécharger et ouvrir votre projet

Téléchargez le code source de votre projet choisi ou utilisez le projet "IP Address Tracker" depuis [ce lien](https://github.com/iamspruce/ip-address-tracker/). Extrayez le fichier ZIP téléchargé à un emplacement sur votre ordinateur. Cela fournira un exemple concret pour démontrer les concepts de Git.

### Étape 2 : Ouvrir le projet dans VS Code

Ouvrez Visual Studio Code et cliquez sur "File" > "Open Folder" pour sélectionner le dossier où vous avez extrait le projet.

### Étape 3 : Ouvrir le terminal dans VS Code

Cliquez sur "Terminal" > "New Terminal" pour ouvrir le terminal dans VS Code, où nous interagirons avec Git en utilisant des commandes.

### Étape 4 : Initialiser un dépôt Git

Initialisez un dépôt Git en exécutant la commande suivante :

```bash
git init
```

Sortie :

```bash
Initialized empty Git repository in /Users/spruceemmanuel/Documents/IP Address Tracker/.git/
```

Cette commande crée un nouveau dossier caché appelé **.git** dans votre dossier de projet, qui suit les changements de vos fichiers de projet. Lorsque vous exécutez `git init`, Git configure les fichiers et répertoires nécessaires pour commencer le versionnage de notre projet. Cela inclut :

* Un dossier **.git** qui stocke toutes les métadonnées de votre dépôt
    
* Une branche principale, qui est la branche par défaut de votre dépôt
    
* Un pointeur HEAD, qui pointe vers la branche actuelle (dans ce cas, main).
    

En initialisant un dépôt Git, vous dites à Git de commencer à suivre les changements de vos fichiers de projet. Cela vous permet de versionner votre code, de collaborer avec d'autres et de maintenir un enregistrement des changements.

## Comment suivre les changements avec Git

Maintenant que nous avons configuré Git, il est prêt à suivre les changements dans notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-11.30.49-PM.png align="left")

*Contrôle de source VSCode*

Git remarque les changements dans nos fichiers, mais avant de pouvoir enregistrer ces changements, nous devons dire à Git de le faire.

### Préparer les changements avec git add

Pour préparer nos changements à être enregistrés, nous utilisons la commande `git add`. Voici comment cela fonctionne :

#### Ajouter des fichiers individuels

Si vous souhaitez ajouter des fichiers spécifiques, comme index.html, script.js ou styles.css, vous pouvez utiliser git add suivi du nom du fichier. Par exemple :

```bash
git add index.html
```

#### Ajouter tous les changements à la fois

Si vous souhaitez ajouter tous les fichiers modifiés dans le projet à la zone de staging, utilisez :

```bash
git add .
```

### Enregistrer les changements avec git commit

Une fois que nous avons utilisé git add, nous utilisons git commit pour enregistrer nos changements. Voici comment faire :

```bash
git commit -m "Décrivez vos changements ici"
```

Remplacez "Décrivez vos changements ici" par une brève description de ce que vous avez changé. Par exemple :

```bash
git commit -m "Mettre à jour index.html avec un nouveau contenu"
```

Sortie :

```bash
[master (root-commit) be9b1cd] Update index.html with new content
3 files changed, 386 insertions(+)
create mode 100644 index.html
create mode 100644 script.js
create mode 100644 styles.css
```

En utilisant `git add` et `git commit`, vous instruisez Git de suivre et d'enregistrer des versions spécifiques de votre projet. Cela vous aide à gérer les changements, à collaborer avec d'autres et à maintenir un enregistrement de votre progression.

## Comment pousser votre projet sur GitHub

Maintenant que nous avons nos changements suivis et validés localement, il est temps de télécharger notre projet sur GitHub afin de pouvoir le partager avec le monde.

### Étape 1 : Créer un nouveau dépôt sur GitHub

* Allez sur GitHub et connectez-vous à votre compte.
    
* Cliquez sur l'icône "+" dans le coin supérieur droit et sélectionnez "New repository".
    

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-11.36.23-PM.png align="left")

* Remplissez le nom du dépôt (par exemple : "ip-address-tracker"), et ajoutez une description si vous le souhaitez.
    
* Choisissez si vous voulez que le dépôt soit public ou privé.
    
* Ne pas initialiser le dépôt avec un **README**, **gitignore**, ou une licence (puisque nous avons déjà un dépôt local configuré).
    
* Cliquez sur "Create repository".
    

### Étape 2 : Lier votre dépôt local à GitHub

Pour connecter votre dépôt local avec le nouveau dépôt GitHub, vous devez ajouter une origine distante. Suivez ces étapes :

* Copiez l'URL de votre nouveau dépôt GitHub. Elle devrait ressembler à ceci : https://github.com/votreutilisateur/ip-address-tracker.git
    
* Ouvrez le Terminal dans Visual Studio Code et exécutez la commande suivante :
    

```bash
git branch -M main
git remote add origin https://github.com/votreutilisateur/ip-address-tracker.git
```

### Étape 3 : Pousser vos changements locaux sur GitHub

Maintenant, poussez vos validations locales vers le dépôt GitHub avec :

```bash
git push -u origin main
```

Sortie :

```bash
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 645 bytes | 645.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
To https://github.com/votreutilisateur/ip-address-tracker.git
* [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### Étape 4 : Vérifier votre dépôt sur GitHub

Retournez à la page de votre dépôt GitHub. Vous devriez voir tous vos fichiers et l'historique des validations disponibles en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-8.55.48-AM.png align="left")

*Un dépôt hébergé sur GitHub*

## Comment héberger votre projet sur GitHub Pages

Maintenant que votre projet a été initialisé avec Git et poussé sur GitHub, hébergeons-le sur GitHub Pages. GitHub Pages est un service gratuit qui vous permet de publier des projets web directement depuis un dépôt GitHub.

### Qu'est-ce que GitHub Pages ?

GitHub Pages transforme votre dépôt GitHub en un site web. C'est un moyen facile de présenter vos projets sans avoir besoin d'un service d'hébergement séparé. Vous pouvez créer des sites web statiques directement depuis vos dépôts.

### Comment activer GitHub Pages

* Allez sur votre dépôt GitHub dans un navigateur web.
    
* Cliquez sur l'onglet "Settings".
    
* Faites défiler vers le bas jusqu'à la section "Pages" dans le menu de gauche.
    
* Sous "Source", sélectionnez la branche que vous souhaitez publier (généralement main ou master), et choisissez le dossier racine.
    

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-11.12.19-PM.png align="left")

*Sélection de la branche et du dossier racine pour GitHub Pages.*

* Cliquez sur "Save".
    

### Comment obtenir l'URL de votre site GitHub Pages

Après avoir activé GitHub Pages, GitHub vous fournira une URL où votre site est publié. Elle suit généralement ce format :

```bash
https://<username>.github.io/<nom-du-depot>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-11.19.05-PM.png align="left")

*L'URL où votre site GitHub Pages est publié.*

Ouvrez votre navigateur et collez l'URL pour voir votre site web en direct.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screenshot-2024-08-04-at-10.56.40-PM-1.png align="left")

*Visualisation du site web en direct sur GitHub Pages.*

### Comment mettre à jour votre site GitHub Pages

Chaque fois que vous poussez des changements vers la branche sélectionnée dans votre dépôt, GitHub Pages mettra automatiquement à jour votre site en direct. Voici un rappel rapide sur la façon de pousser les changements :

* Apportez des modifications à vos fichiers de projet.
    
* Ajoutez et validez vos changements :
    

```bash
git add .
git commit -m "Votre message de validation"
```

* Poussez les changements vers GitHub :
    

```bash
git push origin main
```

Avec ces étapes, vous avez réussi à héberger votre projet sur GitHub Pages. Félicitations ! Votre projet est maintenant en ligne et accessible au monde entier.

## Conclusion

Il y a quelques années, j'étais à votre place—excité à l'idée de construire mon premier site web mais incertain sur la façon de le partager avec le monde. Aujourd'hui, vous avez non seulement appris ce que sont Git et GitHub, mais aussi comment les utiliser pour héberger votre propre projet.

Imaginez votre excitation lorsque votre projet sera en ligne et que vous pourrez le partager avec vos amis, votre famille et la communauté mondiale. Vous avez maintenant configuré Git, créé un compte GitHub, initialisé un dépôt Git et hébergé votre projet sur GitHub Pages. Chaque étape vous a rapproché de devenir un développeur plus confiant et capable.

Ce n'est que le début. Git et GitHub ont de nombreuses autres fonctionnalités à explorer. Alors que vous continuez à construire et à partager des projets, vous découvrirez de nouvelles façons de collaborer et d'améliorer votre flux de travail.

Continuez à expérimenter, continuez à apprendre, et surtout, continuez à coder. Le monde attend de voir ce que vous créerez ensuite !

Si vous avez des questions, n'hésitez pas à me trouver sur Twitter à [@sprucekhalifa](https://twitter.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus de conseils et de mises à jour. Bon codage !