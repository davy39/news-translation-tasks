---
title: Guide du débutant pour Git — Comment commencer et créer votre premier dépôt
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2019-05-16T16:54:03.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/how-to-start-and-create-your-first-repository.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Guide du débutant pour Git — Comment commencer et créer votre premier dépôt
seo_desc: 'If you are a developer and you want to get started with Git and GitHub,
  then this article is made for you.

  After a short introduction on what is Git and how to use it, you will be able to
  create and work on a GitHub project.

  What is Git?

  Git is a fre...'
---

#### Si vous êtes un développeur et que vous souhaitez commencer avec Git et GitHub, alors cet article est fait pour vous.

Après une courte introduction sur ce qu'est Git et comment l'utiliser, vous serez en mesure de créer et de travailler sur un projet GitHub.

#### Qu'est-ce que Git ?

[Git](https://git-scm.com/) est un logiciel libre et open source créé par [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) en 2005. Cet outil est un système de contrôle de version qui a été initialement développé pour travailler avec plusieurs développeurs sur le noyau Linux.

De nombreux systèmes de contrôle existent, comme CVS, SVN, Mercurial et autres, mais aujourd'hui Git est le logiciel standard pour le contrôle de version.

#### Contrôle de version, c'est ça ?

Si vous êtes nouveau dans le monde du développement, ces mots ne vous diront rien. Cependant, ne vous inquiétez pas, après ce court paragraphe, vous saurez exactement ce qu'est un « Système de Contrôle de Version (VCS) ».

Le contrôle de version est un système de gestion qui prend en compte les modifications que vous avez apportées à un fichier ou à un ensemble de fichiers (exemple : un projet de code). Avec ce système, les développeurs peuvent collaborer et travailler ensemble sur le même projet.

Un système de branches est porté par le contrôle de version et permet aux développeurs de travailler individuellement sur une tâche (exemple : une branche, une tâche ou une branche, un développeur) avant de combiner toutes les modifications apportées par les collaborateurs dans la branche principale.

Toutes les modifications apportées par les développeurs sont tracées et sauvegardées dans un historique. Cela peut être bénéfique pour suivre les modifications apportées par chaque collaborateur.

![Image](https://cdn-media-1.freecodecamp.org/images/YB4J4fBv4xEjfjrWvizRE7EjMHkyMqelVXJ7)
_Système de Contrôle de Version (VCS) historique des modifications — Copyright à [ToolsQA](https://www.toolsqa.com/git/version-control-system/" rel="noopener" target="_blank" title=") post_

#### Où trouver les dépôts Git

Si vous souhaitez commencer à utiliser Git, vous devez savoir où héberger vos dépôts. Il existe de nombreuses plateformes d'hébergement où vous pouvez mettre votre code gratuitement. Certaines options ne sont pas gratuites, mais généralement vous n'en avez pas besoin sauf dans des cas spécifiques.

Voici les trois services d'hébergement Git les plus populaires :

* [**GitHub**](https://github.com/)**:** Racheté récemment par Microsoft — Lancé en 2008 (31 millions d'utilisateurs en octobre 2018).
* [**GitLab**](https://about.gitlab.com/)**:** Propriété de GitLab Inc. — Lancé en 2011.
* [**BitBucket**](https://bitbucket.org/product/)**:** Propriété d'Atlassian — Lancé en juin 2008.

> Note : Les plateformes d'hébergement sont disponibles de deux manières, sur le cloud (hébergé en ligne) ou auto-installé sur votre serveur (hébergement privé).

#### Pourquoi utiliser Git en tant que développeur

Cet outil est incontournable pour les développeurs du monde entier. Voici une liste des avantages de cet outil :

* Plus de copies, lorsque vous terminez votre travail sur une mise à jour significative pour votre application ou une correction de bug, vous devez simplement « pousser » votre projet en ligne pour le sauvegarder.
* Supprimez et cassez votre code ; vous devez simplement taper une commande pour revenir à la version précédente et continuer votre travail.
* Travaillez avec vos amis sans envoyer un e-mail avec le projet compressé chaque fois que le code change.
* Vous pouvez vous permettre d'oublier ce que vous avez fait. Une simple commande est nécessaire pour vérifier vos modifications depuis la dernière fois que vous avez sauvegardé votre travail.

Je viens de vous dire les principaux avantages si vous n'utilisez pas Git pour le moment. Croyez-moi ; cet outil peut devenir primordial. Par exemple, vous pouvez configurer des services pour travailler avec Git et déployer et tester automatiquement votre code.

### Maintenant, pratiquons avec Git et GitHub

Maintenant que vous savez ce qu'est Git et GitHub, il est temps de pratiquer avec des exercices concrets.

Après ces exercices, vous serez en mesure de créer et de gérer vos projets via GitHub avec toutes les fonctionnalités de base de Git.

> Note : J'ai choisi GitHub comme notre service d'hébergement pour Git parce que c'est le plus utilisé dans le monde. Ne vous inquiétez pas ; la procédure est assez similaire sur les autres services.

> **Veuillez noter que cet article suppose que vous connaissez les commandes de base du SHELL. Si ce n'est pas le cas, certaines parties de cet article seront confuses.**

#### Étape #1 — Il est temps de commencer !

Vous avez hâte de commencer ? Faisons-le !

Ce premier exercice n'est pas très compliqué ; il est divisé en deux étapes. L'installation de Git et la création d'un compte GitHub.

**a. Création d'un compte GitHub**

Pour créer votre compte, vous devez vous connecter sur [la page principale de GitHub](https://github.com/) et remplir le formulaire d'inscription.

![Image](https://cdn-media-1.freecodecamp.org/images/9D4-dwak0kefb74cMYnfNrPmWkf9vGhDB1T0)
_Page principale de GitHub avec formulaire d'inscription_

Rien de plus ! Vous êtes officiellement un nouveau membre de GitHub !

**b. Installation de Git**

Maintenant, vous devez installer les outils Git sur votre ordinateur. Il existe différents logiciels Git, mais il est préférable d'installer celui de base pour commencer. Nous utiliserons la ligne de commande pour communiquer avec GitHub.

Une fois que vous êtes plus à l'aise avec la ligne de commande, vous pouvez télécharger un logiciel Git avec une interface utilisateur.

* _Pour Ubuntu :_

Tout d'abord, mettez à jour vos paquets :

```
$ sudo apt update
```

Ensuite, installez Git avec apt-get :

```
$ sudo apt-get install git
```

Enfin, vérifiez que Git est installé correctement :

```
$ git --version
```

* _Pour MacOSX :_

Tout d'abord, téléchargez le dernier [installeur Git pour Mac](https://sourceforge.net/projects/git-osx-installer/files/).

Ensuite, suivez les instructions à l'écran.

Enfin, ouvrez un terminal et vérifiez que Git est installé correctement :

```
$ git --version
```

* _Pour Windows :_

Tout d'abord, téléchargez le dernier [installeur Git pour Windows](https://gitforwindows.org/).

Ensuite, suivez les instructions à l'écran (vous pouvez laisser les options par défaut).

Enfin, ouvrez un terminal (exemple : powershell ou git bash) et vérifiez que Git est installé correctement :

```
$ git --version
```

* _Pour tous les utilisateurs :_

Une dernière étape est nécessaire pour compléter l'installation correctement ! Vous devez exécuter dans votre terminal les commandes suivantes avec vos informations pour définir un nom d'utilisateur et un email par défaut lorsque vous allez sauvegarder votre travail :

```
$ git config --global user.name "Gaël Thomas"
$ git config --global user.email "example@mail.com"
```

#### Étape #2 — Votre premier projet GitHub !

Maintenant que vous êtes prêt, vous pouvez retourner à la page principale de GitHub et cliquer sur l'icône « + » dans la barre de menu.

![Image](https://cdn-media-1.freecodecamp.org/images/W1EU4osppAAyktghCia7BSC4gPmjCqXXIKZF)
_Barre de menu GitHub avec l'icône « + »_

Une fois que vous cliquez sur ce bouton, un nouveau menu apparaît avec une entrée « New repository ». Cliquez dessus !

![Image](https://cdn-media-1.freecodecamp.org/images/MFs72raHwu-NB6M9e70hQ9Lx2qNLaVvYlw6V)
_Sous-menu avec l'entrée « New repository »_

[La page de création de dépôt](https://github.com/new) apparaîtra. Choisissez un nom sympa pour votre premier dépôt et mettez une petite description avant de cliquer sur le bouton « Create repository ».

> Note : Dans le contexte de cet article, veuillez ne pas cocher « Initialize this repository with a README ». Nous créerons un fichier « README » plus tard !

![Image](https://cdn-media-1.freecodecamp.org/images/mxGU5eGEki7FsedthUt8Vyi3uqAhL02FbmXF)
_Menu de création de dépôt_

Bien joué ! Votre premier dépôt GitHub est créé. Si vous voulez voir tous vos dépôts, vous devez cliquer sur votre photo de profil dans la barre de menu puis sur « Your repositories ».

![Image](https://cdn-media-1.freecodecamp.org/images/q6w-ifrkLlL5MNVCY9a8qeWs5vadw7Zxa0Fd)
_Sous-menu avec l'entrée « Your repositories »_

#### Étape #3 — Une bonne couverture

Il est temps de faire votre première modification à votre dépôt. Que pensez-vous de créer une couverture pour celui-ci, une sorte de texte de bienvenue ?

**a. Une version locale de votre projet**

Votre première mission est d'obtenir une copie du dépôt sur votre ordinateur. Pour cela, vous devez « cloner » le dépôt. Sur la page du dépôt, vous devez obtenir l'adresse « HTTPS ».

![Image](https://cdn-media-1.freecodecamp.org/images/cxRrZUe-tW2Wkn0WUg-MsN1m1WesvGPlJT7V)
_Page du dépôt avec l'adresse « HTTPS »_

Une fois que vous avez l'adresse du dépôt, vous devez utiliser votre terminal (via les commandes shell) pour vous déplacer à l'endroit où vous voulez mettre la copie du répertoire (par exemple, vous pouvez vous déplacer dans votre dossier « Documents »). Lorsque vous êtes prêt, vous pouvez entrer :

```
$ git clone [ADRESSE HTTPS]
```

Cette commande créera une copie locale du dépôt hébergé à l'adresse donnée.

![Image](https://cdn-media-1.freecodecamp.org/images/bTrnxOfRwjx1JN55RmAdn4h0bs2B9WoMWa89)
_Message de sortie de la commande « git clone »_

Maintenant, votre dépôt est sur votre ordinateur. Vous devez vous y déplacer avec :

```
$ cd [NOM DU DÉPÔT]
```

> Note : Lorsque vous clonez, Git créera un dépôt sur votre ordinateur. Si vous le souhaitez, vous pouvez accéder à votre projet avec l'interface utilisateur de l'ordinateur.

**b. Édition du dépôt**

Maintenant, vous pouvez créer un fichier nommé « README.md » dans votre dossier (via le terminal ou l'interface utilisateur sur votre ordinateur). Je ne vous donne pas plus de détails sur cette étape, rien de particulier. Ouvrez votre dossier et ajoutez un fichier comme s'il s'agissait d'un dossier standard.

Si vous voulez faire quelque chose de cool, copiez et collez ce modèle dans votre fichier « README.md ». Vous pouvez remplacer les informations entre les crochets pour personnaliser la sortie.

```markdown
### Mon premier dépôt est génial !

Je suis [PSEUDO/NOM] et voici mon premier dépôt GitHub.
Si vous voyez ce fichier sur mon projet, c'est parce que j'apprends Git.

Mon humeur :

> [NOM DE L'HUMEUR]

Ma couleur préférée :

> [NOM DE LA COULEUR]

Merci beaucoup pour votre lecture ! ☺
```

**c. Partageons notre travail !**

Maintenant que vous avez modifié votre projet, vous devez le sauvegarder. Ce processus est appelé commit.

Pour cela, retournez à votre terminal. Si vous l'avez fermé, retournez dans votre dossier.

Lorsque vous voulez sauvegarder votre travail, quatre étapes sont nécessaires. Ces étapes sont appelées : « status », « add », « commit » et « push ». J'ai préparé une procédure standard pour vous à effectuer chaque fois que vous voulez sauvegarder votre travail.

> Note : Toutes les étapes suivantes doivent être effectuées dans votre projet.

* « status » : La première chose à faire une fois votre travail terminé est de vérifier les fichiers que vous avez modifiés. Pour cela, vous pouvez taper la commande suivante pour faire apparaître une liste des modifications :

```
$ git status
```

![Image](https://cdn-media-1.freecodecamp.org/images/mS45A-0l4Zq3cFP762AVpCXoCP-xjm8842nr)
_Sortie de « git status » dans notre projet_

* « add » : À l'aide de la liste des modifications, vous pouvez ajouter tous les fichiers que vous voulez télécharger avec la commande suivante :

```
$ git add [NOM DU FICHIER] [NOM DU FICHIER] [...]
```

Dans notre cas, nous allons ajouter « README.md » parce que nous voulons sauvegarder ce fichier.

```
$ git add README.md
```

> Note : Si vous tapez à nouveau « git status », le « README.md » apparaîtra maintenant en vert. Cela signifie que nous avons ajouté le fichier correctement.

* « commit » : Maintenant que nous avons ajouté les fichiers de notre choix, nous devons écrire un message pour expliquer ce que nous avons fait. Ce message peut être utile plus tard si nous voulons vérifier l'historique des modifications. Voici un exemple de ce que nous pouvons mettre dans notre cas.

```
$ git commit -m "Ajout de README.md avec une bonne description."
```

* « push » : Vous y êtes, vous pouvez maintenant mettre votre travail en ligne ! Si vous tapez la commande suivante, tout votre travail sera mis en ligne et visible directement sur la page du dépôt.

```
$ git push origin master
```

Vous l'avez fait ! Si vous retournez sur la page de votre dépôt sur GitHub, vous allez voir votre fichier « README.md » avec un bel aperçu.

![Image](https://cdn-media-1.freecodecamp.org/images/7ORzDxuPUCooIQZsGVdKHmzCQYzh-ia0Go09)
_Page du dépôt avec le fichier « README.md »_

### Commandes utiles pour Git

Il vous manque encore quelques commandes essentielles en tant que débutant avec Git. Voici une liste qui vous sera utile pendant votre projet.

* Afficher l'historique des commits (toutes les modifications apportées au projet).

```
$ git log
```

* Revenir en arrière sur toutes vos modifications depuis le dernier commit.

```
$ git checkout .
```

* Revenir en arrière sur toutes les modifications d'un fichier spécifique depuis le dernier commit.

```
$ git checkout [NOM DU FICHIER]
```

* Afficher les dernières modifications d'un fichier depuis le dernier commit.

```
$ git diff [NOM DU FICHIER]
```

* Supprimer tous les fichiers inattendus dans votre projet (non commités).

```
$ git clean -dfx
```

* Ajouter tous les fichiers et faire un commit en même temps.

```
$ git commit -am [MESSAGE]
```

#### Qu'est-ce qui suit ?

Dans la prochaine partie de ce guide pour débutants, vous découvrirez ces trois sujets :

* Qu'est-ce qu'un bon message de commit.
* Pourquoi c'est essentiel.
* Une checklist pour écrire vos messages de commit.

-> [Guide du débutant pour Git — Comment écrire un bon message de commit](https://herewecode.io/blog/a-beginners-guide-to-git-how-to-write-a-good-commit-message/)

## Conclusion

J'espère que vous avez trouvé ce guide et ces exemples sur Git/GitHub utiles ! Si vous avez des questions ou des commentaires, n'hésitez pas à demander.

Si vous voulez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration de soi et mon parcours en tant que développeur full stack !

Vous pouvez trouver d'autres articles comme celui-ci sur mon site web : [herewecode.io](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/herewecode.io).

###