---
title: Comment écrire un script pour changer votre arrière-plan Zoom chaque jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-14T18:05:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-script-to-change-zoom-background
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/zoom-background-article-image.png
tags:
- name: automation
  slug: automation
- name: Script
  slug: script
seo_title: Comment écrire un script pour changer votre arrière-plan Zoom chaque jour
seo_desc: "By Saransh Kataria\nOver the past few months, I've found a new use for\
  \ the pictures that I've taken while hiking. I started using them as Zoom virtual\
  \ backgrounds. \nIf you are anything like me and take a lot of pictures, it can\
  \ be hard to decide which..."
---

Par Saransh Kataria

Au cours des derniers mois, j'ai trouvé une nouvelle utilisation pour les photos que j'ai prises en randonnée. J'ai commencé à les utiliser comme arrière-plans virtuels Zoom. 

Si vous êtes comme moi et que vous prenez beaucoup de photos, il peut être difficile de décider laquelle est la plus belle. J'ai donc décidé de toutes les utiliser, à différents jours. 

Malheureusement, Zoom ne propose pas cette fonctionnalité intégrée. Étant développeur logiciel, j'ai dû automatiser le processus de choix d'un arrière-plan virtuel Zoom aléatoire chaque jour.

# Que fait le script ?

Zoom dispose bien d'une API que j'aurais pu utiliser pour changer mon arrière-plan chaque jour – mais cela semblait trop d'efforts pour cette tâche. Les développeurs logiciels sont nés paresseux, non ? :)

J'ai plutôt découvert que l'application Zoom crée une copie de l'arrière-plan sélectionné dans son dossier de préférences et y fait référence. Le script prend simplement un fichier aléatoire et remplace ce fichier d'arrière-plan. Et voilà ! Un arrière-plan virtuel Zoom différent est affiché. 

Vous pouvez ensuite mettre cela dans une tâche cron pour qu'elle soit exécutée tous les jours (ou à la fréquence de votre choix) afin de changer périodiquement l'arrière-plan.

# Installation

J'ai placé toutes les images que je souhaite utiliser comme arrière-plans dans un dossier de mon répertoire utilisateur. Le mien se trouve à `/zoom/bgpictures/`, et c'est ce que j'utilise dans le script. Mais il s'agit d'une variable que vous pouvez modifier selon vos préférences.

Ensuite, nous définissons un arrière-plan virtuel Zoom dans notre application. Peu importe lequel vous choisissez. Tout ce dont nous avons besoin est l'ID unique que Zoom attribuera à cet arrière-plan. 

Il peut y avoir des fichiers déjà dans le répertoire, mais nous voulons sélectionner celui qui correspond à l'image que nous venons de télécharger pour éviter de remplacer un fichier différent. 

Le répertoire se trouve à : `~/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom`. Le nom du fichier sera quelque chose comme : `9WAE197F-90G2-4EL2-9M1F-AP784B4C2FAD`

# Comment écrire le script

Nous allons utiliser un script bash pour remplacer l'image que nous venons d'utiliser. Je vais placer ce script dans le dossier Zoom que j'ai créé pour les images d'arrière-plan. Encore une fois, il peut être nommé comme vous le souhaitez – je nomme le mien `~/zoom/zoombg.sh`. 

Le script est le suivant :

```bash
#!/bin/bash
# Le nom du fichier que nous avons copié auparavant et qui sera remplacé
OG_BG="9WAE197F-90G2-4EL2-9M1F-AP784B4C2FAD";

# Répertoire où Zoom stocke les arrière-plans
ZOOM_DIR="/Users/$USER/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/";

# Répertoire de nos images
BGPATH="/Users/$USER/zoom/bgpictures/";

# Choix d'un fichier aléatoire
NEW_BG=$(find "$BGPATH" -type f | sort -R | head -1);

# Remplacement du fichier
cp -R "$NEW_BG" "$ZOOM_DIR/$OG_BG";
```

Si vous choisissez des chemins différents pour le répertoire, assurez-vous simplement de les modifier dans la variable. Nous devons rendre ce script exécutable en exécutant la commande :

```bash
chmod 755 ~/zoom/zoombg.sh
```

# Comment changer votre arrière-plan Zoom de manière aléatoire

Le script est prêt. Tout ce que nous avons à faire est de le mettre dans une tâche cron, qui est un planificateur de tâches intégré basé sur le temps. Nous devons décider d'un calendrier pour la fréquence à laquelle nous voulons changer l'arrière-plan virtuel Zoom. Je le fais à 9h55 tous les jours, car mes réunions commencent à 10h.

Si vous êtes nouveau dans les tâches cron, vous pouvez utiliser le [générateur](https://corntab.com/) pour vous aider. J'utilise :

```bash
55 9 * * 1-5 /Users/saranshkataria/zoom/zoombg.sh > /dev/null 2>&1
```

La première partie (55 9 * * 1-5) est celle que vous devrez personnaliser selon votre calendrier. La deuxième partie indique simplement au système d'exploitation ce qu'il doit faire à ce moment-là. Vous devrez mettre à jour le chemin si vous avez choisi un emplacement différent pour le script bash.

Pour le mettre dans une tâche cron, tapez :

```bash
crontab -e
```

et cela ouvrira un éditeur utilisant vi. Appuyez sur la touche I du clavier pour entrer en mode insertion, collez la ligne, puis appuyez sur Échap suivi de « :wq » et entrez pour sauvegarder et quitter.

C'est tout ! Maintenant, vous aurez un arrière-plan virtuel Zoom aléatoire chaque jour (ou à la fréquence de votre choix).

Si vous utilisez Windows, vous pouvez modifier le script en conséquence et cela devrait être assez simple à utiliser.

Si vous avez des questions, n'hésitez pas à me contacter.

_Lisez plus de mes articles sur : [https://www.wisdomgeek.com](https://www.wisdomgeek.com/)_