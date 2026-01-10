---
title: Qu'est-ce que Git ?
date: '2019-11-06T17:02:56.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/the-beginners-guide-to-git-github
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-pic.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_desc: 'By Thanoshan MV

  What is Git?

  Git is a free, open-source version control software. It was created by Linus Torvalds
  in 2005. This tool is a version control system that was initially developed to work
  with several developers on the Linux kernel.

  This b...'
---


Par Thanoshan MV

<!-- more -->

# **Qu'est-ce que Git ?**

Git est un logiciel de **gestion de versions** gratuit et open-source. Il a été créé par Linus Torvalds en 2005. Cet outil est un système de gestion de versions qui a été initialement développé pour travailler avec plusieurs développeurs sur le noyau Linux.

Cela signifie essentiellement que Git est un outil de suivi de contenu. Git peut donc être utilisé pour stocker du contenu — et il est principalement utilisé pour stocker du code en raison des autres fonctionnalités qu'il offre.

Les projets réels impliquent généralement plusieurs développeurs travaillant en parallèle. Ils ont donc besoin d'un système de gestion de versions comme Git pour s'assurer qu'il n'y a pas de conflits de code entre eux.

De plus, les exigences de ces projets changent souvent. Un système de gestion de versions permet donc aux développeurs de revenir en arrière et de retourner à une version antérieure de leur code.

Le système de branches de Git permet aux développeurs de travailler individuellement sur une tâche (Par exemple : Une branche -> Une tâche OU Une branche -> Un développeur). Considérez Git comme une petite application logicielle qui contrôle votre base de code, si vous êtes un développeur.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/vcs.png) _Montre le fonctionnement de Git_

# **Dépôts Git**

Si nous voulons commencer à utiliser Git, nous devons savoir où héberger nos dépôts.

Un dépôt (ou « Repo » pour faire court) est un projet qui contient plusieurs fichiers. Dans notre cas, un dépôt contiendra des fichiers basés sur du code.

Il existe deux façons d'héberger vos dépôts. L'une est en ligne (sur le cloud) et la seconde est hors ligne (auto-installée sur votre serveur).

Il existe trois services d'hébergement Git populaires : GitHub (détenu par Microsoft), GitLab (détenu par GitLab) et BitBucket. Nous utiliserons GitHub comme service d'hébergement.

# **Avant d'utiliser Git, nous devrions savoir pourquoi nous en avons besoin**

### Git facilite la contribution aux projets open source

Presque tous les projets open-source utilisent GitHub pour gérer leurs projets. L'utilisation de GitHub est gratuite si votre projet est open-source, et elle inclut un wiki et un gestionnaire de tickets (issue tracker) qui facilitent l'inclusion d'une documentation plus approfondie et l'obtention de retours sur votre projet.

Si vous souhaitez contribuer, il vous suffit de forker (obtenir une copie) un projet, d'apporter vos modifications, puis d'envoyer au projet une pull request via l'interface web de GitHub. Cette pull request est votre façon de dire au projet que vous êtes prêt à ce qu'ils examinent vos modifications.

### Documentation

En utilisant GitHub, vous facilitez l'obtention d'une excellente documentation. Leur section d'aide et leurs guides proposent des articles sur presque tous les sujets liés à Git auxquels vous pouvez penser.

### Options d'intégration

GitHub peut s'intégrer à des plateformes courantes telles qu'Amazon et Google Cloud, à des services tels que Code Climate pour suivre vos retours, et peut appliquer la coloration syntaxique dans plus de 200 langages de programmation différents.

### Suivre les modifications du code à travers les versions

Lorsque plusieurs personnes collaborent sur un projet, il est difficile de suivre les révisions — qui a changé quoi, quand, et où ces fichiers sont stockés.

GitHub s'occupe de ce problème en gardant une trace de tous les changements qui ont été poussés (pushed) vers le dépôt.

Tout comme avec Microsoft Word ou Google Drive, vous pouvez disposer d'un historique des versions de votre code afin que les versions précédentes ne soient pas perdues à chaque itération. Il est facile de revenir à la version précédente et de contribuer à votre travail.

### Valoriser votre travail

Êtes-vous un développeur qui souhaite attirer des recruteurs ? GitHub est le meilleur outil sur lequel vous pouvez compter pour cela.

Aujourd'hui, lors de la recherche de nouvelles recrues pour leurs projets, la plupart des entreprises consultent les profils GitHub. Si votre profil est disponible, vous aurez plus de chances d'être recruté, même si vous ne venez pas d'une grande université ou d'une école prestigieuse.

# **Maintenant, nous allons apprendre à utiliser Git et GitHub**

### Création d'un compte GitHub

Pour créer votre compte, vous devez vous rendre sur le site web de [GitHub][1] et remplir le formulaire d'inscription.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/github-webpage.png) _Page web officielle de GitHub_

### Installation de Git

Nous devons maintenant installer les outils Git sur notre ordinateur. Nous utiliserons le CLI pour communiquer avec GitHub.

Pour Ubuntu :

1.  Tout d'abord, mettez à jour vos paquets.

```
sudo apt update
```

2.  Ensuite, installez Git et GitHub avec apt-get

```
sudo apt-get install git
```

3.  Enfin, vérifiez que Git est correctement installé

```
git --version
```

4.  Exécutez les commandes suivantes avec vos informations pour définir un nom d'utilisateur et un e-mail par défaut lorsque vous allez sauvegarder votre travail.

```
git config --global user.name "MV Thanoshan"
git config --global user.email "example@mail.com"
```

# **Travailler avec des projets GitHub**

Nous travaillerons avec les projets GitHub de deux manières.

### Type 1 : Créer le dépôt, le cloner sur votre PC et y travailler (Recommandé)

Le type 1 consiste à créer un dépôt totalement neuf sur GitHub, à le cloner sur notre ordinateur, à travailler sur notre projet et à le repousser (push).

Créez un nouveau dépôt en cliquant sur le bouton « new repository » sur la page web de GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/new-repo.png)

Choisissez un nom pour votre premier dépôt, ajoutez une petite description, cochez la case « Initialize this repository with a README » et cliquez sur le bouton « Create repository ».

![Image](https://www.freecodecamp.org/news/content/images/2019/11/readme.png)

Bien joué ! Votre premier dépôt GitHub est créé.

Votre première mission est d'obtenir une copie du dépôt sur votre ordinateur. Pour ce faire, vous devez « cloner » le dépôt sur votre ordinateur.

Cloner un dépôt signifie que vous prenez un dépôt qui se trouve sur le serveur et que vous le clonez sur votre ordinateur – tout comme si vous le téléchargiez. Sur la page du dépôt, vous devez récupérer l'adresse « HTTPS ».

![Image](https://www.freecodecamp.org/news/content/images/2019/11/github-project.png)

Une fois que vous avez l'adresse du dépôt, vous devez utiliser votre terminal. Utilisez la commande suivante sur votre terminal. Lorsque vous êtes prêt, vous pouvez saisir ceci :

```
git clone [HTTPS ADDRESS]
```

Cette commande créera une copie locale du dépôt hébergé à l'adresse indiquée.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/cmd-1.png) _Message de sortie de la commande « git clone »_

Maintenant, votre dépôt est sur votre ordinateur. Vous devez vous y déplacer avec la commande suivante.

```
cd [NAME OF REPOSITORY]
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/cmd-2.png)

Comme vous pouvez le voir sur l'image ci-dessus, le nom de mon dépôt est « My-GitHub-Project » et cette commande m'a permis d'aller dans ce répertoire spécifique.

**REMARQUE :** Lorsque vous clonez, Git crée un dépôt sur votre ordinateur. Si vous le souhaitez, vous pouvez accéder à votre projet via l'interface utilisateur de l'ordinateur au lieu d'utiliser la commande « cd » ci-dessus sur le terminal.

Maintenant, dans ce dossier, nous pouvons créer des fichiers, travailler dessus et les sauvegarder localement. Pour les sauvegarder dans un endroit distant — comme GitHub — nous devons effectuer un processus appelé « commit ». Pour ce faire, retournez sur votre terminal. Si vous l'avez fermé, comme je l'ai indiqué précédemment, utilisez la commande « cd ».

```
cd [NAME OF REPOSITORY]
```

Maintenant, dans le terminal, vous êtes dans le répertoire de votre dépôt. Il y a 4 étapes dans un commit : « status », « add », « commit » et « push ». Toutes les étapes suivantes doivent être effectuées au sein de votre projet. Passons-les en revue une par une.

1.  « status » : La première chose à faire est de vérifier les fichiers que vous avez modifiés. Pour ce faire, vous pouvez taper la commande suivante pour faire apparaître une liste de modifications.

```
git status
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/git-status-1.png)

2.  « add » : À l'aide de la liste de modifications, vous pouvez ajouter tous les fichiers que vous souhaitez télécharger avec la commande suivante,

```
git add [FILENAME] [FILENAME] [...]
```

Dans notre cas, nous allons ajouter un simple fichier HTML.

```
git add sample.html
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/sample.png)

3.  « commit » : Maintenant que nous avons ajouté les fichiers de notre choix, nous devons écrire un message pour expliquer ce que nous avons fait. Ce message pourra être utile plus tard si nous voulons consulter l'historique des modifications. Voici un exemple de ce que nous pouvons mettre dans notre cas.

```
git commit -m "Added sample HTML file that contain basic syntax"
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/commit-1.png)

4.  « push » : Nous pouvons maintenant mettre notre travail sur GitHub. Pour ce faire, nous devons « pousser » (push) nos fichiers vers le Remote. Le Remote est une instance dupliquée de notre dépôt qui réside ailleurs sur un serveur distant. Pour ce faire, nous devons connaître le nom du remote (la plupart du temps, le remote est nommé origin). Pour trouver ce nom, tapez la commande suivante.

```
git remote
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/remote-1.png)

Comme vous pouvez le voir sur l'image ci-dessus, il est indiqué que le nom de notre remote est origin. Nous pouvons maintenant « pousser » notre travail en toute sécurité avec la commande suivante.

```
git push origin master
```

Maintenant, si nous allons sur notre dépôt sur la page web de GitHub, nous pouvons voir le fichier sample.html que nous avons poussé vers le remote — GitHub !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/push-1.png)

**REMARQUE** : Parfois, lorsque vous utilisez des commandes Git dans le terminal, cela peut vous mener à l'éditeur de texte VIM (un éditeur de texte basé sur le CLI). Pour vous en débarrasser, vous devez taper

```
:q
```

puis ENTRÉE.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/-q.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/11/explanation.png) _Décrit le fonctionnement du pull & push_

Puller est l'acte de recevoir depuis GitHub.

Pousser (Pushing) est l'acte d'envoyer vers GitHub.

### Type 2 : Travailler sur votre projet localement, puis créer le dépôt sur GitHub et le pousser vers le remote.

Le type 2 vous permet de créer un nouveau dépôt à partir d'un dossier existant sur votre ordinateur et de l'envoyer sur GitHub. Dans de nombreux cas, vous avez peut-être déjà créé quelque chose sur votre ordinateur que vous souhaitez soudainement transformer en dépôt sur GitHub.

Je vais vous expliquer cela avec un projet web de formulaire d'enquête que j'ai réalisé précédemment et qui n'avait pas été ajouté à GitHub.

Comme je l'ai déjà mentionné, lors de l'exécution de commandes Git, nous devons nous assurer que nous sommes dans le bon répertoire dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/type-2.png)

Par défaut, n'importe quel répertoire de notre ordinateur n'est pas un dépôt Git – mais nous pouvons le transformer en dépôt Git en exécutant la commande suivante dans le terminal.

```
git init
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/init.png)

Après avoir converti notre répertoire en dépôt Git, la première chose à faire est de vérifier les fichiers que nous avons en utilisant la commande suivante.

```
git status
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/status-2.png)

Il y a donc deux fichiers dans ce répertoire que nous devons « ajouter » à notre Repo.

```
git add [FILENAME] [FILENAME] [...]
```

**REMARQUE** : Pour « ajouter » tous les fichiers de notre dépôt, nous pouvons utiliser la commande suivante :

```
git add .
```

Une fois la staging area (le processus d'ajout) terminée, nous pouvons vérifier si les fichiers ont été ajoutés avec succès ou non en exécutant `git status`.

Si ces fichiers particuliers sont en vert comme sur l'image ci-dessous, vous avez fait votre travail !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/green.png)

Ensuite, nous devons faire un « commit » avec une description.

```
git commit -m "Adding web Survey form"
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/survey-form.png)

Si mon dépôt avait commencé sur GitHub et que je l'avais téléchargé sur mon ordinateur, un remote y serait déjà attaché (Type 1). Mais si je commence mon dépôt sur mon ordinateur, il n'a pas de remote associé, je dois donc ajouter ce remote (Type 2).

Pour ajouter ce remote, nous devons d'abord aller sur GitHub. Créez un nouveau dépôt et nommez-le comme vous le souhaitez pour le stocker sur GitHub. Cliquez ensuite sur le bouton « Create repository ».

**REMARQUE** : Dans le Type 2, veuillez ne pas initialiser le dépôt avec un fichier README lors de la création d'un nouveau dépôt sur la page web de GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/new-repo-2.png)

Après avoir cliqué sur le bouton « Create repository », vous trouverez l'image ci-dessous en tant que page web.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/web-page.png)

Copiez l'adresse HTTPS. Maintenant, nous allons créer le remote pour notre dépôt.

```
git remote add origin [HTTPS ADDRESS]
```

Après avoir exécuté cette commande, nous pouvons vérifier si nous avons ajouté le remote avec succès ou non par la commande suivante

```
git remote
```

Et s'il affiche « origin », vous avez ajouté le remote à votre projet.

**REMARQUE** : Rappelez-vous simplement que nous pouvons indiquer n'importe quel nom pour le remote en changeant le nom « origin ». Par exemple :

```
git remote add [REMOTE NAME] [HTTPS ADDRESS]
```

Maintenant, nous pouvons pousser notre projet vers GitHub sans aucun problème !

```
git push origin master
```

Après avoir terminé ces étapes une par une, si vous allez sur GitHub, vous pourrez trouver votre dépôt avec les fichiers !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/final.png)

# **Conclusion**

Merci à tous d'avoir lu. Je viens d'expliquer les bases de Git et GitHub. Je vous encourage vivement à lire d'autres articles liés à Git et GitHub. J'espère que cet article vous a aidé.

[Consultez][2] mon article original sur Medium.

Merci.

**Bon codage !**

[1]: https://github.com/
[2]: https://medium.com/@mvthanoshan9/ubuntu-a-beginners-guide-to-git-github-44a2d2fda0b8