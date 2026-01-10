---
title: L'exécution du code ne peut pas continuer car msvcp140.dll est introuvable
  – Comment le corriger sur un PC Windows 10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-19T17:47:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-the-code-execution-cannot-proceed-because-msvcp140-dll-was-not-found
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/msvcpdll-3.png
tags:
- name: error handling
  slug: error-handling
- name: Microsoft
  slug: microsoft
- name: Windows 10
  slug: windows-10
seo_title: L'exécution du code ne peut pas continuer car msvcp140.dll est introuvable
  – Comment le corriger sur un PC Windows 10
seo_desc: "msvcp140.dll is a Microsoft C Dynamic Linked Library file responsible for\
  \ running certain Windows apps and games – especially those built on C++. \nSometimes,\
  \ when you're trying to open an app or game, you might get the error “the code execution\
  \ canno..."
---

msvcp140.dll est un fichier de bibliothèque de liens dynamiques (DLL) de Microsoft C responsable de l'exécution de certaines applications et jeux Windows – notamment ceux construits avec C++. 

Parfois, lorsque vous essayez d'ouvrir une application ou un jeu, vous pouvez obtenir l'erreur « l'exécution du code ne peut pas continuer car msvcp140.dll est introuvable ». 

Cette erreur peut également se présenter sous une autre forme : « Le programme ne peut pas démarrer car MSVCP140.dll est introuvable. Essayez de réinstaller le programme pour résoudre ce problème ».

Cela peut se produire parce que le fichier est réellement manquant ou qu'il est disponible mais corrompu. 

Vous pouvez analyser votre ordinateur avec Windows Defender ou un programme antivirus tiers, mais cela ne corrige pas toujours l'erreur.

Si vous obtenez cette erreur lors de l'ouverture d'un jeu ou d'une application sur votre PC Windows 10, vous êtes au bon endroit. Car dans cet article, je vais vous montrer 3 façons de corriger l'erreur et de commencer à utiliser votre application ou à jouer à votre jeu une fois de plus.

## Solution 1 : Réinstaller l'application

Comme suggéré dans le message d'erreur, la réinstallation du programme qui déclenche l'erreur « msvcp140.dll est introuvable » peut résoudre le problème pour vous.

Pour réinstaller une application, procédez comme suit :

**Étape 1** : Cliquez sur Démarrer et sélectionnez Paramètres.
![opensettings-2](https://www.freecodecamp.org/news/content/images/2022/01/opensettings-2.jpg)

**Étape 2** : Sélectionnez Applications parmi les tuiles du menu.
![ss-1-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-3.jpg)

**Étape 3** : Cliquez sur l'application causant l'erreur et sélectionnez Désinstaller.
![ss-](https://www.freecodecamp.org/news/content/images/2022/01/ss-.jpg)

**Étape 4** : Redémarrez votre ordinateur, puis réinstallez l'application en la téléchargeant depuis le site web du fournisseur ou le Microsoft Store.

## Solution 2 : Exécuter l'analyse SFC

Puisque l'erreur pourrait être déclenchée par un fichier corrompu, l'analyse du vérificateur de fichiers système (SFC) peut aider à la corriger. Lorsque vous exécutez ce programme, il vérifie les fichiers de votre ordinateur pour détecter les corruptions et les répare.

Pour exécuter l'analyse SFC, suivez les étapes ci-dessous :

**Étape 1** : Cliquez sur Démarrer et recherchez « cmd ». Cliquez sur Exécuter en tant qu'administrateur à droite, car vous devez exécuter l'analyse en tant qu'administrateur.
![cmd-admin-2](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin-2.jpg)

**Étape 2** : Collez `sfc /scannow` et appuyez sur `ENTRÉE`.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-1.png)

**Étape 3** : Lorsque l'analyse est terminée, fermez l'invite de commande et redémarrez votre PC.

## Solution 3 : Installer Microsoft Visual C++ Redistributable

Si aucune des solutions ci-dessus ne fonctionne pour vous, alors l'installation du package redistribuable Microsoft Visual C++ le corrigera. 

Cela est dû au fait que `msvcp140.dll` et un autre fichier DLL appelé `vcruntime140.dll` sont tous deux des constituants du package Microsoft Visual C++.

Le guide étape par étape suivant vous montre comment installer Microsoft Visual C++ redistribuable :

**Étape 1** : Pour télécharger le fichier, rendez-vous sur la page officielle de téléchargement du package redistribuable Microsoft Visual C++ et cliquez sur Télécharger.
![ss-3-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-2.png)

**Étape 2** : Sur la page suivante, vous verrez l'option de télécharger le fichier pour un système d'exploitation 32 bits et une autre pour un système d'exploitation 64 bits. Sélectionnez celui correspondant à votre système d'exploitation et cliquez sur « Suivant ».
![ss-4b-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4b-1.png)

**Étape 3** : Ouvrez le fichier téléchargé et suivez l'assistant d'installation pour l'installer.
![ss-5-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-2.png)

Si vous avez déjà installé le package Microsoft Visual Studio 2015 et que vous obtenez toujours cette erreur, vous devez désinstaller puis réinstaller le package.

J'espère que ce guide vous aide à corriger l'erreur. 

Merci pour votre lecture.