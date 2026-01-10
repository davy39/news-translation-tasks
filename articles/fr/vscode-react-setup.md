---
title: Comment configurer VSCode pour vos projets React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-17T16:54:36.000Z'
originalURL: https://freecodecamp.org/news/vscode-react-setup
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/setup-vscode-for-react-projects.png
tags:
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Comment configurer VSCode pour vos projets React
seo_desc: 'The ultimate tool you have when you''re developing your projects is your
  code editor. Which is why it''s so important to set it up properly.

  In this step-by-step guide, we will go from a completely new VSCode installation
  to a code editor perfectly pre...'
---

L'outil ultime que vous avez lorsque vous développez vos projets est votre éditeur de code. C'est pourquoi il est si important de le configurer correctement.

Dans ce guide étape par étape, nous allons passer d'une installation complètement nouvelle de VSCode à un éditeur de code parfaitement préparé pour votre prochain projet React.

Commençons !

## Comment installer VSCode

La première étape pour configurer Visual Studio Code (VSCode en abrégé) est de l'installer sur votre ordinateur.

Rendez-vous sur [code.visualstudio.com](https://code.visualstudio.com) et téléchargez la version adaptée à votre ordinateur (c'est 100% gratuit).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.08.06-AM.png)
_Installez la version adaptée à votre système d'exploitation_

Une fois votre installation terminée et que vous ouvrez l'application VSCode, vous devriez être accueilli par un écran d'accueil qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.19.32-AM.png)
_Écran d'accueil de VSCode (après installation)_

## Choisissez un thème de couleur que vous aimez

Bien que le thème par défaut fourni avec VSCode soit très agréable et lisible, je préfère utiliser un thème tiers que je trouve plus reposant pour mes yeux.

Il peut sembler trivial de passer du temps à choisir un thème. Mais comme vous passerez des heures à lire du texte sur votre éditeur, vous voulez choisir des couleurs que vous aimez et qui ne fatigueront pas vos yeux.

Je utilise personnellement et recommande vivement le Material Theme pour toutes mes installations de VSCode.

Pour installer le Material Theme, allez dans (en haut de l'écran) :

**Affichage** > **Extensions** (ou utilisez le raccourci ⇧ + ⌘ (Ctrl) + X)

Ensuite, recherchez "Material Theme" dans la barre latérale et installez le premier résultat qui apparaît. 

Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.36.24-AM.png)
_Installation du Material Theme_

Une fois installé, il vous donnera un menu déroulant pour choisir parmi une série de variantes différentes.

L'option par défaut est excellente, mais je trouve personnellement que la variante "Material Theme Ocean High Contrast" est la plus belle.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.37.38-AM.png)
_Material Theme pour VSCode_

## Rendez votre texte facile à lire

C'est le moment idéal pour ajouter quelques paramètres de base qui rendent le code que vous écrivez confortable à lire.

Les paramètres qui amélioreront la lisibilité de votre code sont la taille de la police, la taille des tabulations et la famille de polices.

Vous pouvez modifier les préférences de VSCode en allant dans (en haut de votre écran) :

**Code** > **Préférences** > **Paramètres** (ou utilisez le raccourci : ⌘ (Ctrl) + ,)

Les paramètres que j'ai trouvés les plus confortables au fil des années pour le développement sur bureau et ordinateur portable sont une taille de police de 18 et une taille de tabulation définie à 2.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.27.06-AM.png)
_Paramètres de texte pour VSCode_

De plus, pour que votre texte ait l'air parfait, je trouve que le texte est plus beau lorsque vous augmentez le niveau de zoom par défaut de l'éditeur.

Pour augmenter le niveau de zoom, allez dans les préférences (⌘ (Ctrl) + ,) et tapez "**niveau de zoom**".

Je recommande de changer le niveau de zoom de 0 à 1.

Et enfin, par préférence, j'aime supprimer les liens de fil d'Ariane par défaut qui se trouvent en haut de l'éditeur.

Vous pouvez supprimer les fils d'Ariane en allant dans :

**Affichage** > **Afficher les fils d'Ariane** (et assurez-vous qu'il n'est pas coché).

Voici à quoi ressemble notre éditeur de code avec un fichier de composant exemple que j'ai ajouté à mon bureau :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.49.42-AM.png)
_Apparence d'un composant React dans VSCode_

## Formatez votre code avec l'extension Prettier

Vous avez peut-être remarqué dans l'exemple ci-dessus que le code n'est pas très bien formaté.

Heureusement, vous pouvez automatiquement formater chaque fichier .js que vous écrivez en utilisant l'extension Prettier pour VSCode.

Pour pouvoir formater instantanément notre code à chaque fois que nous enregistrons un fichier .js, nous pouvons à nouveau aller dans l'onglet des extensions (⇧ + ⌘ (Ctrl) + X), taper "**prettier**" et l'installer :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.51.35-AM.png)
_Extension Prettier pour VSCode_

Ensuite, nous pouvons retourner aux préférences (⌘ (Ctrl) + ,) et rechercher "**format on save**" et nous assurer qu'il est coché :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.53.36-AM.png)
_Paramètre Format on Save_

Et à nouveau dans les préférences, recherchez le paramètre "**default formatter**" et définissez-le sur Prettier.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.55.30-AM.png)
_Paramètre Default formatter_

Maintenant, si nous retournons à un fichier non formaté et que nous cliquons sur enregistrer, il sera instantanément formaté pour nous !

Voici à quoi ressemble notre composant factice après avoir cliqué sur enregistrer :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.57.23-AM.png)
_Composant React formaté (avec Prettier)_

Consultez la documentation de l'extension Prettier pour voir comment vous pouvez la configurer davantage selon vos préférences de formatage. Cependant, je recommande personnellement d'utiliser les options par défaut.

## Comment taper rapidement du JSX avec Emmet

VSCode est livré avec un support intégré pour un outil incroyable appelé Emmet qui vous permet d'écrire des balises HTML très rapidement.

Cependant, Emmet n'est pas configuré par défaut pour être utilisé avec JSX, que React utilise à la place de HTML.

Pour écrire votre JSX plus rapidement, vous pouvez utiliser Emmet avec React en allant dans :

**Code** > **Préférences** > **Paramètres** (⌘ (Ctrl) + ,)

Puis tapez dans la barre de recherche, "**emmet include languages**".

Après cela, cliquez sur le bouton "Add Item" et ajoutez le paramètre suivant :

élément : **javascript**, valeur : **javascriptreact** (puis cliquez sur ok)

Votre paramètre ajouté devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-11.10.32-AM.png)
_Paramètre Emmet Include Languages_

Maintenant que nous avons inclus React comme langage pour Emmet, nous pouvons commencer à écrire notre JSX beaucoup plus rapidement.

Voici une rapide démonstration de la productivité que vous pouvez atteindre avec Emmet :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/emmet-react.gif)
_Démonstration rapide des raccourcis Emmet_

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à tout comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*