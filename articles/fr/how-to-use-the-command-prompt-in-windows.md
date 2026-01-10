---
title: Comment ouvrir et utiliser l'invite de commande dans Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T23:22:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-command-prompt-in-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d74740569d1a4ca37da.jpg
tags:
- name: command line
  slug: command-line
- name: toothbrush
  slug: toothbrush
- name: Windows
  slug: windows
seo_title: Comment ouvrir et utiliser l'invite de commande dans Windows
seo_desc: "Getting started\nWindows, MacOS and Linux have command line interfaces.\
  \ Windows’ default command line is the command prompt. The command prompt allows\
  \ users to use their computer without pointing and clicking with a mouse. \nThe\
  \ command prompt is a bla..."
---

# **Prise en main**

Windows, MacOS et Linux disposent d'interfaces en ligne de commande. L'interface en ligne de commande par défaut de Windows est l'invite de commande. L'invite de commande permet aux utilisateurs d'utiliser leur ordinateur sans pointer ni cliquer avec une souris. 

L'invite de commande est un écran noir où les utilisateurs tapent des commandes pour utiliser leur ordinateur. Les mêmes tâches qui peuvent être effectuées en pointant et en cliquant avec une souris peuvent également être effectuées avec l'invite de commande. La différence est que de nombreuses tâches telles que la création de dossiers et la suppression de fichiers peuvent être effectuées plus rapidement dans l'invite de commande. 

De plus, elle permet aux utilisateurs de configurer leur ordinateur et d'exécuter des programmes qu'ils ne pourraient pas faire autrement en pointant et en cliquant.

## **Ouvrir l'invite de commande**

Pour accéder à l'invite de commande, cliquez sur le menu démarrer de Windows dans la barre d'outils du bureau (vous pouvez également appuyer sur le bouton Windows de votre clavier) et tapez `cmd` puis appuyez sur `entrée`. L'invite de commande apparaîtra et affichera un texte similaire à ce qui suit :

```text
C:\Users\VotreNomUtilisateur>
```

## **Navigation dans les répertoires (Déplacement dans les dossiers)**

`C:\Users\VotreNomUtilisateur` est appelé votre répertoire de travail actuel (répertoire est une autre façon de dire dossier). C'est comme une adresse qui vous indique où vous vous trouvez sur votre ordinateur. 

Le répertoire de travail actuel peut servir de guide lorsque vous naviguez dans votre ordinateur. À droite du `>`, nous pouvons taper `cd`, qui signifie Change Directory (Changer de répertoire), suivi du nom d'un répertoire vers lequel vous souhaitez naviguer. Dans ce cas, nous taperons `Documents`. Entrez `cd Documents` et votre répertoire de travail actuel devrait ressembler à ce qui suit :

```text
C:\Users\VotreNomUtilisateur\Documents>
```

Pour revenir d'un répertoire en arrière, tapez et entrez `cd..`. Votre répertoire de travail actuel devrait revenir à ceci :

```text
C:\Users\VotreNomUtilisateur>
```

Avec les commandes `cd` et `cd ..`, vous pouvez vous déplacer en avant et en arrière dans les répertoires. Cela peut sembler très basique au début, mais à mesure que vous apprenez plus de commandes, l'invite de commande deviendra un outil très utile et efficace.

## **Voici une liste de commandes courantes :**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-3.25.08-PM.png)

## **Exemples d'utilisation :**

#### **Créer un répertoire**

```text
mkdir nom_du_repertoire_que_vous_souhaitez_creer
```

#### **Obtenir des informations sur une commande**

```text
votre_commande /?
```

#### **Supprimer un fichier et son contenu**

```text
rm /s nom_du_repertoire_que_vous_souhaitez_supprimer
```

## **Conseils utiles :**

* La commande `Ipconfig` affiche l'adresse IP de votre ordinateur
* Si vous tapez une partie du nom d'un répertoire et appuyez sur la touche `tab`, l'invite de commande le complétera automatiquement et si vous appuyez plusieurs fois sur la touche `tab`, elle parcourra les répertoires commençant par la même lettre
* Vous pouvez utiliser d'autres shells ou outils tels que git bash ou cmder pour ajouter plus de commandes et de fonctionnalités à votre invite de commande
* Certaines tâches nécessitent d'exécuter l'invite de commande en tant qu'administrateur en cliquant sur le bouton Windows et en tapant `cmd admin` puis en appuyant sur la touche `entrée`
* Si vous connaissez le chemin d'accès à un fichier ou un répertoire, vous pouvez taper `cd CHEMIN_VERS_VOTRE_REPERTOIRE` au lieu de changer de répertoire plusieurs fois pour accéder à un répertoire ou un fichier
* Lorsque vous appuyez sur la touche de flèche vers le haut, votre commande précédemment entrée apparaîtra et si vous appuyez plusieurs fois, elle parcourra toutes vos commandes précédemment entrées