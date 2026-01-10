---
title: Comment configurer un environnement de développement intégré (IDE)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-17T21:25:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-an-integrated-development-environment-ide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f42740569d1a4ca41a5.jpg
tags:
- name: beginner
  slug: beginner
- name: C
  slug: c
- name: ide
  slug: ide
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
- name: tutorial purgatory
  slug: tutorial-purgatory
seo_title: Comment configurer un environnement de développement intégré (IDE)
seo_desc: 'By M. S. Farzan

  If you''re moving from online tutorials to building your own projects, you might
  be overwhelmed by the idea of setting up your own integrated development environment
  (IDE), or wonder why you even need one to get your work done.

  In this...'
---

Par M. S. Farzan

Si vous passez [des tutoriels en ligne à la création de vos propres projets](https://www.freecodecamp.org/news/how-to-choose-a-programming-language-and-escape-tutorial-purgatory/), vous pourriez être submergé par l'idée de configurer votre propre environnement de développement intégré (IDE), ou vous demander pourquoi vous en avez même besoin pour accomplir votre travail.

Dans cet article, je vais discuter de ce qu'est un IDE et vous donner quelques idées sur ce à quoi le vôtre pourrait ressembler, en particulier si vous travaillez en JavaScript, bien que les informations seront applicables indépendamment du langage ou du type de projet.

Voici une version vidéo de cet article si vous préférez (28 minutes de visionnage) :

%[https://youtu.be/f-JWTicIOwI]

## Qu'est-ce qu'un environnement de développement intégré ?

Un environnement de développement intégré, en termes simples, est tout ce dont un programmeur a besoin pour accomplir son travail. La composition réelle d'un IDE variera selon les langages de programmation, les types de projets et même entre les programmeurs, mais il y a certaines choses qui sont communes à de nombreux IDE, que je vais couvrir ci-dessous.

La manière la plus simple de comprendre un IDE est de considérer une solution "tout-en-un" comme [Unity](https://unity.com/). En tant que moteur de jeu entièrement fonctionnel, Unity dispose de tout ce dont vous aurez besoin pour créer un jeu 2D ou 3D : une interface graphique qui vous permet de construire votre monde de jeu, un éditeur de code (Visual Studio) où vous pouvez écrire des scripts, un moyen de télécharger des dépendances et des actifs, et même une intégration GitHub afin que vous puissiez suivre les versions de construction et collaborer sur des projets. Pour des projets plus petits, Unity peut être considéré comme un environnement de développement intégré entièrement fonctionnel, où tout est déjà configuré pour vous après avoir téléchargé le moteur de jeu.

D'autres IDE peuvent varier considérablement en complexité, en particulier si vous venez d'un tutoriel en ligne qui vous permet de coder directement dans le navigateur. L'une de mes critiques concernant les réponses courantes à la question, "quel langage de programmation devrais-je apprendre ?" est l'idée que l'apprentissage de JavaScript est plus facile parce que "il s'exécute simplement dans votre navigateur".

Dites cela à quiconque a tenté de configurer un IDE pour Create React App, qui nécessite plusieurs composants pour démarrer - aucun d'entre eux n'étant apparent lorsque vous travaillez à travers des tutoriels en ligne. Pour travailler réellement en tant que développeur, vous aurez besoin de quatre choses principales pour configurer votre environnement de développement intégré : un éditeur de code, une interface de ligne de commande (CLI), un système de contrôle de version et un gestionnaire de paquets.

Un avertissement majeur : votre IDE peut varier considérablement en fonction du langage de programmation ou du type de projet, mais vous aurez probablement besoin d'un ou plusieurs des éléments suivants dans tous les cas !

## Outil IDE #1 : Éditeur de code (et compilateur)

Un grand nombre de tutoriels en ligne vous permettent de coder directement dans le navigateur, ce qui est idéal pour comprendre les concepts de base de la programmation, mais à long terme, vous aurez besoin d'un éditeur qui vous permet de sauvegarder votre code (et de le compiler, si vous utilisez un langage comme C# ou C++).

Il existe de nombreux éditeurs de code, tels que [Atom](https://atom.io/) (léger, gratuit et open source), [Sublime](https://www.sublimetext.com/) (super populaire avec des tonnes d'intégrations), et [Visual Studio / Visual Studio Code](https://visualstudio.microsoft.com/) (supporté par Microsoft et agréable à utiliser). Il serait réducteur de dire qu'ils sont "tous identiques", car chacun offre une approche différente pour soutenir votre flux de travail de codage, vous pourriez donc en essayer un ou deux avant de décider lequel vous préférez.

## Outil IDE #2 : Interface de ligne de commande (CLI)

Si vous avez un ordinateur, vous avez sans doute utilisé votre explorateur de fichiers ou une autre interface graphique de navigation pour accéder au système de fichiers, créer des dossiers, supprimer des fichiers, et ainsi de suite.

L'interface de ligne de commande (CLI) vous permet de faire la même chose... en texte brut. Ce qui peut sembler super archaïque ou ennuyeux au début, mais une fois que vous aurez compris comment enchaîner les commandes et les intégrer dans votre flux de travail, vous commencerez à voir la puissance de la CLI et à quel point elle est essentielle à la plupart des environnements de développement.

Sur Mac, vous pourriez utiliser le Terminal. Comme j'ai installé GitHub pour Windows (plus sur GitHub ci-dessous) sur ma machine, j'utilise Git Bash pour mon travail. Il existe plusieurs options ici pour vous, et il pourrait être utile de consulter quelques tutoriels sur la ligne de commande pour comprendre certains des principes de base afin que vous vous sentiez à l'aise de l'utiliser dans votre IDE.

## Outil IDE #3 : Système de contrôle de version

Il existe plusieurs [ressources](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) qui fournissent des aperçus de ce qu'est le contrôle de version et pourquoi vous devriez l'utiliser. Il suffit de dire que lorsque vous construisez autre chose qu'un projet simple, vous aurez besoin d'un moyen de sauvegarder votre travail, de partager votre code avec des collaborateurs et de suivre les différentes versions de construction afin que vous puissiez modifier certaines parties de la base de code et pas d'autres.

[GitHub](https://github.com/) n'est pas le seul système de contrôle de version disponible, mais c'est la référence actuelle, et il serait judicieux de consulter quelques tutoriels pour apprendre à tirer parti de ses fonctionnalités, même si vous finissez par l'utiliser simplement comme méthode de sauvegarde à distance.

De plus, bien qu'il existe plusieurs modules complémentaires pour intégrer GitHub directement dans votre éditeur de code (ou moteur de jeu), la pratique standard pour effectuer des tâches liées à Git est d'utiliser l'interface de ligne de commande, ce qui fournit une autre raison de devenir compétent avec votre CLI de choix.

## Outil IDE #4 : Gestionnaire de paquets

Pour certains IDE, comme avec notre exemple Unity ci-dessus, tout ce que vous avez à faire est de télécharger et d'installer le logiciel pour commencer à construire vos projets. La plupart des dépendances dont vous aurez besoin seront incluses avec votre téléchargement initial, et si ce n'est pas le cas, il y aura un moyen d'y accéder depuis le moteur de jeu (par exemple, l'[Asset Store](https://assetstore.unity.com/) de Unity).

Pour d'autres IDE, plus du type "choisissez votre propre aventure", vous devrez assembler les choses vous-même, et l'un des composants essentiels sera un gestionnaire de paquets comme [NPM](https://www.npmjs.com/) ou [Conda](https://docs.conda.io/en/latest/).

Les gestionnaires de paquets font beaucoup de choses, et à leur fonctionnalité la plus basique, ils vous aideront à installer toutes les dépendances dont vous aurez besoin pour accomplir votre travail. Si vous souhaitez commencer un projet React, par exemple, vous navigerez vers un dossier via votre CLI, et, après avoir installé NPM (qui est fourni avec [Node.js](https://nodejs.org/en/)), tapez :

```
npx create-react-app my-app 
cd my-app 
npm start
```

La première ligne dit essentiellement : "Hey, NPM ! Télécharge toutes les dépendances pour Create React App, et mets-les dans un dossier appelé 'my-app'."

La deuxième ligne indique ensuite à votre CLI : "Navigue vers le nouveau répertoire appelé 'my-app'."

La troisième ligne lance l'action : "NPM, c'est encore moi. Démarre un serveur de développement qui affiche mon projet dans un navigateur et le met à jour chaque fois que j'apporte des modifications au code."

Une fois que vous avez installé toutes les dépendances nécessaires à l'aide de votre gestionnaire de paquets, vous commencerez à travailler dans votre éditeur de code et à utiliser l'interface de ligne de commande pour faire des demandes de tirage ou pousser du code vers un dépôt distant en utilisant votre système de contrôle de version.

En résumé, un environnement de développement intégré comprend toutes les choses dont vous avez besoin pour accomplir votre travail, et varie en fonction du langage, du type de projet et de vos préférences personnelles. Ordinairement, les IDE incluent un éditeur de code (et un compilateur), une interface de ligne de commande, un système de contrôle de version et un gestionnaire de paquets, mais votre environnement de développement intégré pourrait avoir des exigences différentes ou une combinaison de ceux-ci.

Vous pouvez le faire !

Si vous avez apprécié cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](http://www.twitter.com/sominator).