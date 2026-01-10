---
title: Qu'est-ce que msmpeng.exe ? Pourquoi utilise-t-il beaucoup de CPU et de disque
  ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-21T15:01:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-msmpeng-exe-why-is-it-of-high-cpu-disk-usage
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/joseph-greve-BPJKc4r7_eo-unsplash.jpg
tags:
- name: Security
  slug: security
- name: Windows
  slug: windows
seo_title: Qu'est-ce que msmpeng.exe ? Pourquoi utilise-t-il beaucoup de CPU et de
  disque ?
seo_desc: "msmpeng.exe is an important part of Windows Security, formerly known as\
  \ Windows Defender. It scans your computer for various threats ranging from malware\
  \ to spyware, then renders the appropriate solution(s). \nIn this article, I will\
  \ take you through ..."
---

msmpeng.exe est une partie importante de Windows Security, anciennement connu sous le nom de Windows Defender. Il analyse votre ordinateur pour détecter diverses menaces, allant des logiciels malveillants aux logiciels espions, puis applique les solutions appropriées. 

Dans cet article, je vais vous expliquer ce qu'est msmpeng.exe, pourquoi il consomme trop de CPU, et 2 méthodes différentes pour l'empêcher d'utiliser trop de CPU.

## Qu'est-ce que msmpeng.exe ?

Msmpeng.exe signifie Microsoft Malware Protection Engine. Également connu sous le nom d'Antimalware service executable, c'est le programme antivirus intégré pour les ordinateurs Windows 10. 

Ce programme s'exécute en arrière-plan et analyse votre ordinateur pour détecter des menaces telles que des logiciels malveillants, des virus, des vers, etc., puis les met en quarantaine ou les supprime. 

## Pourquoi msmpeng.exe utilise-t-il beaucoup de CPU et de disque ?

msmpeng.exe consomme trop d'espace disque CPU car il s'exécute activement en arrière-plan et analyse chaque partie de votre ordinateur. Cela fait bien sûr de msmpeng.exe un programme gourmand en ressources.

Outre cela, une autre raison pour laquelle msmpeng.exe utilise une grande quantité de CPU est que le programme analyse son propre dossier (`C:\Program Files\Windows Defender`). Des ressources matérielles faibles ont également été liées à une consommation excessive d'espace disque CPU par msmpeng.exe.

## Comment empêcher msmpeng.exe d'utiliser trop d'espace disque CPU

Il existe 2 méthodes principales pour empêcher l'exécutable du service Antimalware de Windows 10 d'utiliser trop de CPU. Premièrement, vous pouvez empêcher Windows Defender d'analyser son propre dossier et désactiver la protection en temps réel, et deuxièmement, vous pouvez reprogrammer les analyses de Windows Defender.

### Solution 1 : Empêcher Windows Defender d'analyser son propre dossier

**Étape 1** : Cliquez sur Démarrer ou appuyez sur la touche WIN de votre clavier, puis cliquez sur l'icône d'engrenage pour ouvrir l'application Paramètres.
![ss-1-7](https://www.freecodecamp.org/news/content/images/2021/10/ss-1-7.jpg)

**Étape 2** : Cliquez sur "Mise à jour et sécurité" dans la liste.
![ss-2-8](https://www.freecodecamp.org/news/content/images/2021/10/ss-2-8.jpg)

**Étape 3** : Sélectionnez "Sécurité Windows" et cliquez sur "Protection contre les virus et les menaces".
![ss-3-6](https://www.freecodecamp.org/news/content/images/2021/10/ss-3-6.jpg)

**Étape 4** : L'application Sécurité Windows s'ouvrira. Sous "Paramètres de protection contre les virus et les menaces", cliquez sur le lien "Gérer les paramètres".
![ss-4-7](https://www.freecodecamp.org/news/content/images/2021/10/ss-4-7.jpg)

**Étape 5** : Faites défiler jusqu'à "Exclusions" et cliquez sur le lien "Ajouter ou supprimer des exclusions".
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-5-3.jpg)

**Étape 6** : Sur la page suivante, cliquez sur "Ajouter une exclusion", puis sélectionnez "Dossier".
![ss-6-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-6-5.jpg)

**Étape 7** : Pour éviter de multiples clics, collez "`C:\Program Files\Windows Defender`" dans l'éditeur et cliquez sur "Sélectionner le dossier".
![ss-7-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-7-3.jpg)

**Étape 8** : Immédiatement après avoir cliqué sur "Sélectionner le dossier", une grande fenêtre modale apparaîtra – assurez-vous de cliquer sur Oui. 

Vous pouvez maintenant voir que le dossier a été ajouté comme une exclusion :
![ss-8-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-8-1.jpg)

Windows Defender n'analysera plus ce dossier, donc le taux d'utilisation du CPU devrait diminuer sur votre ordinateur.

### Solution 2 : Désactiver la protection en temps réel et reprogrammer les analyses de Windows Defender

**Étape 1** : Pour désactiver la protection en temps réel et reprogrammer les analyses effectuées par Windows Defender, appuyez sur `WIN` (touche Windows) pour ouvrir la boîte de dialogue Exécuter. 

**Étape 2** : Tapez "taskschd.msc" et cliquez sur "OK". Cela ouvrira l'application Planificateur de tâches.
![ss-9](https://www.freecodecamp.org/news/content/images/2021/10/ss-9.jpg)

**Étape 3** : Développez l'onglet "Planificateur de tâches", puis sélectionnez "Microsoft", puis "Windows".
![ss-10](https://www.freecodecamp.org/news/content/images/2021/10/ss-10.jpg)

**Étape 4** : Faites défiler et sélectionnez "Windows Defender".
![ss-11](https://www.freecodecamp.org/news/content/images/2021/10/ss-11.jpg)

**Étape 5** : Cliquez avec le bouton droit sur "Windows Defender Scheduled Scan" et sélectionnez "Propriétés".
![ss-12](https://www.freecodecamp.org/news/content/images/2021/10/ss-12.jpg)

**Étape 6** : Dans l'onglet Général, décochez "Exécuter avec les privilèges les plus élevés".
![ss-13](https://www.freecodecamp.org/news/content/images/2021/10/ss-13.jpg)

**Étape 7** : Allez dans l'onglet Conditions et assurez-vous que toutes les cases sont décochées.
![ss-14](https://www.freecodecamp.org/news/content/images/2021/10/ss-14.jpg)

**Étape 8** : Enfin, allez dans l'onglet Déclencheurs et cliquez sur "Nouveau".
![ss-15](https://www.freecodecamp.org/news/content/images/2021/10/ss-15.jpg)

**Étape 9** : Enfin, planifiez l'heure à laquelle vous souhaitez que Windows Defender exécute les analyses, choisissez la fréquence, la date et l'heure, puis cliquez sur "OK". Cliquez à nouveau sur "OK".
![ss-16](https://www.freecodecamp.org/news/content/images/2021/10/ss-16.jpg)

**Étape 10** : Redémarrez votre ordinateur. Avec cela, msmpeng.exe ne devrait plus consommer trop d'espace disque CPU.

## Conclusion

Msmpeng.exe, également connu sous le nom d'Antimalware service executable, est un programme pertinent et efficace qui protège votre ordinateur contre les menaces. 

En même temps, il consomme trop d'espace disque CPU, ce qui peut ralentir votre ordinateur et réduire la durée de vie de la batterie, vous pourriez donc être tenté de le désactiver. 

Étant donné que les protections offertes par msmpeng.exe sont utiles, vous devriez chercher des moyens de minimiser ses actions au lieu de le désactiver définitivement, comme cet article vous l'a montré.

Si l'utilisation du disque CPU ne diminue pas, vous pourriez essayer de désactiver définitivement Windows Defender – mais assurez-vous d'obtenir un autre programme antivirus pour votre ordinateur si vous faites cela.

Merci d'avoir lu cet article. Pensez à le partager avec vos amis et votre famille si vous le trouvez utile.