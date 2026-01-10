---
title: Comment utiliser l'interface en ligne de commande – pour les débutants
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2022-09-27T21:11:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-cli-beginner-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/BEGINNERS--HACK-ON-USING-CLI--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: command line
  slug: command-line
seo_title: Comment utiliser l'interface en ligne de commande – pour les débutants
seo_desc: "There's a lot to learn when you're getting into tech. But fortunately there\
  \ are some skills that you can use across different programming languages, operating\
  \ systems, and tools. \nAnd knowing how to use the command line interface (also\
  \ known as the c..."
---

Il y a beaucoup à apprendre quand on débute dans la tech. Mais heureusement, il existe des compétences que vous pouvez utiliser à travers différents langages de programmation, systèmes d'exploitation et outils.

Et savoir utiliser l'interface en ligne de commande (également connue sous le nom d'invite de commande ou de terminal, selon votre système d'exploitation) est l'une de ces compétences.

Que vous fassiez du développement Web, du développement de jeux, du développement d'applications, du Cloud Engineering, du DevOps ou de nombreuses autres disciplines technologiques, vous utiliserez probablement la ligne de commande assez souvent.

## Histoire de la ligne de commande

Aux débuts de l'informatique, les développeurs utilisaient MS-DOS pour naviguer dans le système informatique.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-390.png)

Le Disk Operating System (**DOS**) est un type de système d'exploitation qui utilise des commandes (mots) pour interagir avec l'ordinateur.

Le DOS n'utilisait pas de pointeurs de souris, d'icônes ou de graphiques, les utilisateurs étaient donc contraints d'utiliser des commandes textuelles pour faire fonctionner le système informatique.

Par exemple, pour aller dans un dossier particulier, vous tapiez :

`cd <nom du dossier>`

L'interface en ligne de commande (ou CLI pour court) est similaire au DOS dans le sens où elle utilise des commandes pour effectuer diverses opérations, comme la création de fichiers, la création de dossiers, l'installation de programmes, et bien d'autres choses encore.

L'avancement de la technologie au fil des ans a apporté la populaire GUI (Graphical User Interface ou Interface Graphique) et a rendu les systèmes d'exploitation moins stressants à utiliser.

Bien que les développeurs (et les utilisateurs non techniques) utilisent souvent la GUI de nos jours, il est parfois utile ou nécessaire de travailler directement depuis la CLI, quel que soit votre Stack.

## Qu'est-ce que la CLI ? Est-ce un langage de programmation ?

![Un portrait d'une fille avec une expression mignonne.](https://images.unsplash.com/photo-1646406694751-9df2f91f1161?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDMwfHxjb25mdXNlZCUyMGRldmVsb3BlcnxlbnwwfHx8fDE2NjM1ODgzMzA&ixlib=rb-1.2.1&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@angshu_purkait?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Angshu Purkait</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Si vous êtes nouveau dans le développement logiciel, il est facile de se laisser emporter par la terminologie variée que vous devrez apprendre. Ne vous inquiétez pas, vous ne participez pas à un concours d'orthographe. Vous êtes plutôt censé apprendre à quoi ces termes se rapportent, comment ils fonctionnent réellement et comment vous pouvez les utiliser.

L'un des termes que vous entendrez assez souvent est l'interface en ligne de commande (également appelée invite de commande ou terminal).

L'interface en ligne de commande (CLI) est un environnement d'édition basé sur le texte. Elle utilise du texte spécifié (connu sous le nom de commandes) pour interagir avec l'ordinateur et effectuer de nombreuses opérations, y compris l'installation et l'utilisation de programmes.

Chaque système d'exploitation est livré avec une invite de commande intégrée. Certains packages d'applications tels que Nodejs, Anaconda, Git, etc., sont également livrés avec leur propre invite de commande.

Il en va de même pour les fournisseurs de Cloud tels qu'AWS, GCP, Azure. Bien que la CLI porte des noms différents selon les plateformes ou les packages, son objectif reste le même : vous permettre d'interagir librement avec le package logiciel ou le système informatique en utilisant des instructions textuelles appelées commandes.

Ainsi, la CLI est un outil, pas un langage de programmation.

Une connaissance de base de la CLI vous aidera tout au long de votre parcours technologique, surtout si vous travaillez dans le développement logiciel. En fait, vous pouvez entièrement construire un programme et l'exécuter directement depuis la CLI.

Cet article va :

* Expliquer comment fonctionne la CLI
* Vous aider à localiser votre CLI selon votre système d'exploitation
* Vous montrer comment effectuer des opérations de base à l'aide de la CLI
* Vous aider à différencier la CLI de la GUI

## Comment fonctionne la CLI

Comme nous l'avons brièvement évoqué plus tôt, la CLI utilise des instructions textuelles pour effectuer des opérations. Ces commandes ont une syntaxe spécifique que vous devez suivre et certains textes doivent être écrits sur la même ligne – sinon, un message d'erreur s'affichera.

Dans le cas de la CLI dans les packages d'applications, les commandes peuvent être relatives au package en question. Mais toutes les CLI suivent la même règle : être sémantiques et sur la même ligne.

Pour utiliser votre CLI :
* Localisez la CLI sur votre PC
* Ouvrez-la
* Tapez les commandes souhaitées
* Appuyez sur la touche Entrée

Plus tard dans ce tutoriel, nous exécuterons quelques commandes à l'aide de la CLI afin que vous puissiez mieux comprendre son fonctionnement.

## La ligne de commande dans différents systèmes d'exploitation

Chaque système d'exploitation est livré avec son interface en ligne de commande par défaut, bien que vous puissiez choisir d'installer une CLI plus avancée selon vos besoins.

Certains systèmes d'exploitation et leurs CLI respectives sont listés ci-dessous :

* Windows : Invite de commande (Command Prompt)
* Linux : Linux Bash Shell
* MacOS : Terminal Mac
* Google Cloud Platform : PowerShell, Cloud shell
* Amazon Web Services : Invite de commande AWS
* Microsoft Azure : Azure CLI bash

![Image](https://www.freecodecamp.org/news/content/images/2022/09/BEGINNERS--HACK-ON-USING-CLI--2-.png)
_Une image de l'invite de commande Windows, d'AWS Cloudshell, du Terminal MacOS et du Terminal Linux_

J'utilise actuellement Windows et l'invite de commande Windows, mais je vais également vous montrer comment localiser votre propre terminal ou invite de commande en fonction des systèmes d'exploitation populaires.

## Comment localiser votre CLI

### Sous Windows

Vous pouvez accéder à l'invite de commande sous Windows en utilisant le répertoire des programmes ou des touches de raccourci.

En utilisant le répertoire des programmes, allez dans votre barre de recherche (à côté de l'icône Windows) et tapez **cmd**. Cela fera apparaître une liste de toutes les invites de commande disponibles sur votre machine, y compris le cmd Windows par défaut. Vous pouvez maintenant sélectionner celui que vous souhaitez.

En utilisant un raccourci clavier, appuyez sur **Windows + R** sur votre clavier et tapez **cmd** dans la boîte de dialogue qui s'affiche.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/CMD-1.PNG)
_Une image montrant le terminal d'exécution_

### Sous MacOS

Comme pour Windows, vous pouvez également ouvrir la CLI sur un Mac OS en utilisant le répertoire des programmes ou un raccourci clavier.

Pour utiliser le répertoire des programmes, localisez le launchpad et tapez **Terminal**. Cela le fera apparaître.

Pour utiliser le raccourci clavier, tapez la combinaison des touches **cmd** + **barre d'espace**.

Voici comment localiser le Terminal MacOS et créer un fichier dans un répertoire :

%[https://vimeo.com/754058144]

## Comment effectuer des opérations de base à l'aide de la CLI

En cours de mathématiques, il était assez facile de mémoriser des formules et de résoudre des équations en utilisant ces formules mémorisées. Mais savoir quand appliquer ces équations dans des scénarios de la vie réelle était – et continue souvent d'être – difficile pour de nombreux étudiants.

Savoir où se trouve votre CLI et comment elle fonctionne est un bon pas dans la bonne direction. Mais laissez-moi vous montrer comment débuter avec la CLI en pratiquant des opérations simples directement depuis votre invite de commande.

### Comment naviguer dans votre PC avec la CLI

Naviguer dans votre PC signifie simplement passer d'un dossier ou d'un fichier à un autre. Si vous ne voulez pas utiliser votre souris pour diriger votre curseur, vous pouvez vous déplacer dans votre PC en utilisant la CLI.

Par exemple sous Windows, si vous voulez ouvrir le bureau, suivez les étapes suivantes :

1. Ouvrez la CLI (CMD) comme expliqué précédemment
2. Ensuite, tapez **cd Desktop** sur l'invite de commande, ce qui vous mènera à votre bureau

Gardez à l'esprit que cette commande est pour Windows (pour Mac, par exemple, elle sera légèrement différente).

Voici ce que vous verrez :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/CMD-2.PNG)

### Comment créer un dossier en utilisant la CLI

Vous connaissez peut-être la méthode habituelle consistant à faire un clic droit sur votre écran et à sélectionner l'option "Nouveau dossier" dans le menu déroulant. Mais il existe un moyen de créer un nouveau dossier en utilisant la CLI.

1. Tout d'abord, ouvrez votre CLI
2. Naviguez jusqu'au dossier ou à l'emplacement où vous souhaitez créer le nouveau dossier
3. Entrez **mkdir <nom_du_nouveau_dossier>**
4. Appuyez sur Entrée
5. Vous pouvez maintenant entrer dans le dossier en tapant **cd <nom_du_nouveau_dossier>**

![Image](https://www.freecodecamp.org/news/content/images/2022/09/CMD-3.PNG)

### Comment installer un package en utilisant la CLI

L'installation d'un package logiciel ou d'une application à l'aide de la CLI dépend du package en question.

Les packages comme Node.js (un package de développement pour le développement BackEnd) nécessitent que vous installiez le Node Package Manager (npm). Ce gestionnaire de packages est ce que vous utiliserez pour installer et exécuter Node et d'autres packages similaires.

Certaines commandes pour installer des packages logiciels via la CLI incluent :

1. `install <nom du package>`
2. `run <nom du package>`

Par exemple, pour installer une nouvelle instance d'une application React :

* Ouvrez le terminal

* Localisez votre environnement local en tapant :

`cd Desktop`

* Créez un répertoire pour l'application en tapant :

`mkdir mon_repertoire` (puis `cd mon_repertoire`)

* Créez l'application React directement dans le répertoire en utilisant la commande :

`npx create-react-app mon-app`

![Image](https://www.freecodecamp.org/news/content/images/2022/09/cmd9.PNG)
_Un terminal montrant les commandes pour installer create-react-app en utilisant l'invite de commande Windows_

## Différences entre la CLI et la GUI

![Image](https://www.freecodecamp.org/news/content/images/2022/09/BEGINNERS--HACK-ON-USING-CLI--3-.png)
_Image GUI vs CLI_

Comme nous l'avons vu, la CLI utilise des commandes pour interagir de manière générale avec l'ordinateur.

D'autre part, l'interface graphique (GUI) est une méthode d'interaction avec l'ordinateur utilisant des icônes, des menus, des clics de souris et des pointeurs.

Un système d'exploitation basé sur une GUI permet aux utilisateurs de faire fonctionner librement l'ordinateur en cliquant, faisant glisser, déposant et utilisant d'autres méthodes visuelles d'interaction.

Contrairement à la GUI, la CLI utilise moins d'espace RAM et interagit directement avec le système d'exploitation.

Pour utiliser la GUI, aucune connaissance en programmation n'est requise. Mais pour utiliser la CLI, vous devez avoir une certaine connaissance de la programmation et des opérations de commande.

## Conclusion

Au fur et à mesure que vous commencez ou progressez dans votre parcours technologique, vous devrez installer de nombreux programmes qui sont étrangers à votre machine locale. Ces programmes peuvent ne pas avoir de méthodes d'installation via GUI et peuvent nécessiter que vous exécutiez une ligne de code ou plus sur votre CLI. À ce stade, la connaissance de l'utilisation de la CLI devient très utile.

Il existe une idée générale selon laquelle la CLI est difficile à utiliser – et il faut en effet un certain temps pour s'y habituer. Mais une fois que vous vous serez familiarisé avec le fonctionnement de la CLI, vous la trouverez beaucoup plus facile à gérer.