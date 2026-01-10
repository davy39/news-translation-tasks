---
title: Échec de la mise à jour de Discord – Comment corriger l'erreur sur un PC Windows
  10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-18T15:31:45.000Z'
originalURL: https://freecodecamp.org/news/discord-update-failed-how-to-fix-the-error-on-a-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/discord--1-.png
tags:
- name: Chat
  slug: chat
- name: discord
  slug: discord
- name: 'update '
  slug: update
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Échec de la mise à jour de Discord – Comment corriger l'erreur sur un PC
  Windows 10
seo_desc: 'Discord is a popular chat app for gamers and anyone else who wants to create
  an online community. Despite its popularity, one major problem users report about
  Discord is the update failed loop.

  Discord has to update often because the Discord team imp...'
---

Discord est une application de chat populaire pour les joueurs et toute personne souhaitant créer une communauté en ligne. Malgré sa popularité, un problème majeur signalé par les utilisateurs de Discord est la boucle d'échec de mise à jour.

Discord doit souvent se mettre à jour car l'équipe Discord implémente régulièrement de nouvelles fonctionnalités et des corrections de bugs. 

De plus, l'application elle-même doit charger de nouveaux messages depuis les salons de discussion et les messages privés. Une fois la mise à jour échouée, Discord reste bloqué dans une boucle d'échec de mise à jour.

Dans ce guide, je vais vous montrer 4 façons de corriger l'erreur de mise à jour échouée de Discord sur un ordinateur Windows 10.

## Ce que nous allons couvrir
- [Vérifiez votre connexion Internet](#heading-verifiez-votre-connexion-internet)
- [Exécutez Discord en tant qu'administrateur](#heading-executez-discord-en-tant-quadministrateur)
- [Renommez le fichier Update.exe de Discord](#heading-renommez-le-fichier-updateexe-de-discord)
- [Désactivez temporairement votre programme antivirus et VPN](#heading-desactivez-temporairement-votre-programme-antivirus-et-vpn)
- [Désinstallez et réinstallez Discord](#heading-desinstallez-et-reinstallez-discord)
- [Conclusion](#heading-conclusion)

## Solution 1 : Vérifiez votre connexion Internet

La première chose que je vous suggère de faire est de vérifier votre connexion Internet.

C'est parce que Discord a besoin d'une connexion Internet pour se mettre à jour, car la mise à jour doit être effectuée via Internet. Une fois qu'il n'y a pas de connexion Internet, la mise à jour ne se fera pas.

Assurez-vous que votre PC Windows 10 est connecté à Internet et que la connexion Internet est suffisamment forte.
![ss1-4](https://www.freecodecamp.org/news/content/images/2022/08/ss1-4.png)
![ss2-4](https://www.freecodecamp.org/news/content/images/2022/08/ss2-4.png) 

## Solution 2 : Exécutez Discord en tant qu'administrateur

Une solution courante à ce problème est d'exécuter l'application Discord en tant qu'administrateur. 

Cela pourrait résoudre le problème car toute application que vous souhaitez installer nécessite des privilèges d'administrateur. Discord n'est pas une exception, donc lui accorder des privilèges d'administrateur peut lui permettre de creuser plus profondément dans le problème et de le résoudre.

Pour exécuter Discord en tant qu'administrateur, recherchez Discord et sélectionnez Exécuter en tant qu'administrateur à droite :
![ss3-4](https://www.freecodecamp.org/news/content/images/2022/08/ss3-4.png)

## Solution 3 : Renommez le fichier Update.exe de Discord
Il existe un exécutable séparé pour mettre à jour Discord. Il s'agit du fichier update.exe dans le dossier Discord. 

Renommer ce fichier peut forcer Discord à en télécharger un nouveau et ainsi résoudre le problème pour vous.

**Suivez ces étapes pour renommer le fichier update.exe de Discord**
Appuyez sur `WIN` (touche du logo Windows) + `R` sur votre clavier et tapez `%localappdata%`.
![ss4-5](https://www.freecodecamp.org/news/content/images/2022/08/ss4-5.png)

Recherchez le dossier Discord et ouvrez-le.
![ss5-5](https://www.freecodecamp.org/news/content/images/2022/08/ss5-5.png)

Faites un clic droit sur le fichier `Update.exe` et sélectionnez renommer. Ensuite, renommez-le en quelque chose comme « Updater.exe ». Vous ne devez pas changer l'extension.
![ss6-4](https://www.freecodecamp.org/news/content/images/2022/08/ss6-4.png) 

Ouvrez à nouveau l'application et voyez si le problème est résolu.

## Solution 4 : Désactivez temporairement votre programme antivirus et VPN

Les programmes antivirus et les VPN sont connus pour interférer avec le fonctionnement normal des ordinateurs et des connexions Internet. Donc, si vous en avez un ou les deux sur votre PC, cela pourrait empêcher Discord de se mettre à jour.

Pour désactiver votre antivirus et VPN, ouvrez le Gestionnaire des tâches, faites un clic droit sur `WIN` (touche du logo Windows) et sélectionnez Gestionnaire des tâches.
![ss7-3](https://www.freecodecamp.org/news/content/images/2022/08/ss7-3.png)
 
Sous les processus, faites un clic droit sur Discord et sélectionnez « Fin de tâche ».
![ss8-3](https://www.freecodecamp.org/news/content/images/2022/08/ss8-3.png) 


## Solution 5 : Désinstallez et réinstallez Discord

Si les solutions déjà discutées ne fonctionnent pas pour vous, le dernier recours est de désinstaller Discord et de le réinstaller.

**Étape 1** : Rendez-vous dans le Panneau de configuration et sélectionnez Désinstaller un programme.
![ss9-2](https://www.freecodecamp.org/news/content/images/2022/08/ss9-2.png) 

**Étape 2** : Recherchez Discord, faites un clic droit dessus et sélectionnez désinstaller.
![ss10-2](https://www.freecodecamp.org/news/content/images/2022/08/ss10-2.png) 

**Étape 3** : Pour supprimer complètement Discord, appuyez sur `WIN` + `R` sur votre clavier, tapez `%localappdata%`, et cliquez sur OK.
![ss4-5](https://www.freecodecamp.org/news/content/images/2022/08/ss4-5.png)

**Étape 4** : Faites un clic droit sur le dossier Discord et sélectionnez Supprimer.
![ss11-2](https://www.freecodecamp.org/news/content/images/2022/08/ss11-2.png) 

**Étape 4** : [Téléchargez Discord](https://discord.com/download) à nouveau et installez-le.
![ss12-2](https://www.freecodecamp.org/news/content/images/2022/08/ss12-2.png)

## Conclusion

J'espère que les solutions discutées ci-dessus vous aideront à mettre à jour Discord afin que vous puissiez commencer à l'utiliser à nouveau.

Merci d'avoir lu.