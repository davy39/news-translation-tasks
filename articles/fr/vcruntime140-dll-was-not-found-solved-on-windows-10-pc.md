---
title: vcruntime140.dll introuvable [Résolu sur PC Windows 10]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-04T14:11:12.000Z'
originalURL: https://freecodecamp.org/news/vcruntime140-dll-was-not-found-solved-on-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Vcruntime.png
tags:
- name: error
  slug: error
- name: how-to
  slug: how-to
- name: Windows 10
  slug: windows-10
seo_title: vcruntime140.dll introuvable [Résolu sur PC Windows 10]
seo_desc: 'Have you ever tried to open an app on your computer only to see the error
  "The program can''t start because vcruntime140.dll is missing from your computer.
  Try reinstalling it to fix this problem."?

  This is a common issue with Windows 10 and it can be...'
---

Avez-vous déjà essayé d'ouvrir une application sur votre ordinateur pour voir l'erreur « Le programme ne peut pas démarrer car vcruntime140.dll est manquant sur votre ordinateur. Essayez de le réinstaller pour résoudre ce problème » ?

Il s'agit d'un problème courant avec Windows 10 et cela peut être assez frustrant.

Mais ne vous inquiétez pas – dans ce guide, j'expliquerai de quoi il s'agit cette erreur, et surtout, je vous montrerai deux méthodes différentes pour la corriger.

## Qu'est-ce que l'erreur « vcruntime140.dll introuvable » et quelles en sont les causes ?

L'extension « .dll » est liée aux bibliothèques de liens dynamiques (DLL), qui sont des bibliothèques contenant le code et les données utilisés par un programme.

Une fois qu'un programme est créé, il est associé à une DLL, qui est activée uniquement lorsque ce programme particulier est lancé.

Si la DLL requise est manquante ou corrompue, un message d'erreur indiquant à l'utilisateur comment la corriger s'affiche.

Une DLL requise peut être manquante en raison de logiciels malveillants, d'une installation incomplète, et surtout de fichiers manquants du package redistribuable Microsoft Visual Studio 2015.

## Comment corriger l'erreur vcruntime140.dll introuvable

Vous pouvez corriger l'erreur vcruntime140.dll introuvable en installant le package Microsoft Visual Studio 2015 ou en le réparant.

Si vous obtenez cette erreur en essayant d'utiliser le programme WAMP Server – un programme qui vous permet de créer des sites WordPress localement et de coder en PHP – voici ce que vous devez faire.

Vous pouvez également corriger l'erreur en téléchargeant le fichier vcruntime140.dll en particulier et en le déplaçant dans le bon dossier sur votre ordinateur Windows 10.

### Solution 1 : Installer ou réparer Microsoft Visual Studio 2015 Redistributable

**Étape 1** : Téléchargez le package d'installation de Visual Studio 2015 Redistributable depuis la [page officielle de téléchargement du package redistribuable Microsoft Visual C++](https://www.microsoft.com/en-us/download/details.aspx?id=52685).
![ss-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-1.png)

Dès que vous cliquez sur le bouton de téléchargement, vous verrez l'option de télécharger le fichier pour un système d'exploitation 32 bits et un autre pour un système d'exploitation 64 bits.
![ss-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-2.png)

Choisissez celui qui correspond au système d'exploitation de votre ordinateur Windows 10.

**Étape 2** : Ouvrez le fichier téléchargé et suivez l'assistant d'installation pour l'installer.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-3.png)

**Étape 3** : Assurez-vous d'accepter la licence et les conditions en cochant la case, puis cliquez sur installer.

Si vous avez déjà installé le package Microsoft Visual Studio 2015 et que vous obtenez toujours cette erreur, vous devez « Réparer » le package à la place.

### Comment réparer le package Microsoft Visual Studio 2015 Redistributable

**Étape 1** : Allez dans le Panneau de configuration en cliquant sur Démarrer et en recherchant « panneau de configuration » puis en appuyant sur `ENTRÉE`.

**Étape 2** : Sous Programmes, sélectionnez « Désinstaller un programme ».
![ss-4-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-3.jpg)

**Étape 3** : Recherchez le programme Microsoft Visual Studio 2015 Redistributable, faites un clic droit dessus, puis sélectionnez « Modifier ».
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-3.jpg)

**Étape 4** : Cliquez sur « Réparer ».
![ss-6-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-2.jpg)

### Solution 2 : Télécharger le fichier vcruntime140.dll

**Étape 1** : Téléchargez le fichier vcruntime140.dll depuis ce [site web](https://www.dll-files.com/vcruntime140.dll.html).
![ss-7-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-1.png)

Choisissez l'option qui correspond à votre système d'exploitation et un fichier Zip sera téléchargé.
![ss-8](https://www.freecodecamp.org/news/content/images/2021/11/ss-8.png)

**Étape 2** : Extrayez le fichier Zip avec l'option d'extraction native de Windows 10 ou une application comme WinRAR.

**Étape 3** : Glissez-déposez le fichier vcruntime140.dll dans le répertoire d'installation de l'application affichant le message d'erreur.

Assurez-vous de confirmer que cela résout le problème, sinon, téléchargez et installez Microsoft Visual Studio 2015 Redistributable à la place.

## Conclusion

Dans ce guide, vous avez appris comment corriger l'erreur ennuyeuse vcruntimed140.dll introuvable, afin de pouvoir utiliser des applications et jouer à des jeux sans problème sur votre ordinateur Windows 10.

En plus des deux solutions expliquées dans cet article, vous pouvez également mettre à jour votre Windows 10 vers la dernière version, ce qui peut également corriger l'erreur.

Merci d'avoir lu. Si vous trouvez cet article utile, envisagez de le partager avec vos amis.