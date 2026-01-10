---
title: Il y a eu un problème lors de la réinitialisation de votre PC [Réinitialisation
  du PC corrigée sur Windows 10]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-08T17:20:41.000Z'
originalURL: https://freecodecamp.org/news/there-was-a-problem-with-resetting-your-pc-reset-pc-fixed-on-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/reset.png
tags:
- name: Windows 10
  slug: windows-10
seo_title: Il y a eu un problème lors de la réinitialisation de votre PC [Réinitialisation
  du PC corrigée sur Windows 10]
seo_desc: 'There are a number of reasons why you might want to reset your PC. From
  malware attacks to bad PC health, or maybe you just want to start afresh – the list
  goes on.

  When you''re resetting your PC, you might get the error "There was a problem resetting...'
---

Il existe de nombreuses raisons pour lesquelles vous pourriez vouloir réinitialiser votre PC. Des attaques de logiciels malveillants à la mauvaise santé de votre PC, ou peut-être souhaitez-vous simplement repartir à zéro – la liste est longue.

Lorsque vous réinitialisez votre PC, vous pourriez obtenir l'erreur "Il y a eu un problème lors de la réinitialisation de votre PC". Cette erreur pourrait prendre une autre forme comme "Il y a eu un problème lors de l'actualisation de votre PC" et ainsi de suite.

Si vous rencontrez ce problème après avoir tenté de réinitialiser votre PC Windows 10, vous êtes au bon endroit. Parce que, dans ce guide détaillé, je vais vous montrer 4 façons de corriger le problème et de procéder à la réinitialisation complète de votre PC.

Trois des solutions que je vais vous montrer nécessitent des permissions d'administrateur et seront effectuées dans la ligne de commande, à laquelle vous pouvez toujours accéder même si votre ordinateur est bloqué dans la boucle de réinitialisation.

Pour accéder à la ligne de commande sur un PC Windows 10 bloqué dans la boucle de réinitialisation, tentez d'effectuer une réparation de démarrage si vous y êtes invité, puis choisissez l'invite de commande.
![startup-repair-windows](https://www.freecodecamp.org/news/content/images/2021/12/startup-repair-windows.jpg)

Mais puisque vous ne pouvez pas utiliser l'interface graphique (GUI) pour ouvrir l'invite de commande en tant qu'administrateur si votre ordinateur est bloqué dans la boucle de réinitialisation, comment utilisez-vous la ligne de commande en tant qu'administrateur ? Exécutez la commande `powershell "start cmd -v runAs"`.

## Comment corriger l'erreur "Il y a eu un problème lors de la réinitialisation de votre PC"

### Effectuer une analyse SFC

L'outil de vérification des fichiers système (SFC) vous permet d'effectuer une analyse basée sur la ligne de commande qui trouve et corrige les fichiers corrompus qui pourraient empêcher votre ordinateur de se réinitialiser avec succès.

Pour effectuer l'analyse SFC, vous devez suivre les étapes ci-dessous :

**Étape 1** : Appuyez sur la touche `WIN` de votre clavier et recherchez "cmd". Ensuite, choisissez Exécuter en tant qu'administrateur à droite pour utiliser l'invite de commande en tant qu'administrateur. Assurez-vous de cliquer sur "Oui" dans la prochaine invite.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Étape 2** : Dans la ligne de commande, tapez `sfc /scannow` et appuyez sur `ENTRÉE`. L'analyse peut prendre plus de 15 minutes, alors soyez patient.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-2-1.png)

**Étape 3** : Redémarrez votre PC et essayez de le réinitialiser à nouveau.

Si cela ne corrige pas le problème, passez à la solution suivante – l'analyse DISM.

### Effectuer une analyse DISM

Effectuer une analyse DISM pour corriger ce problème est officiellement recommandé par Microsoft.

DISM signifie Deployment Image Servicing and Management Tool. C'est un exécutable en ligne de commande que vous pouvez utiliser pour réparer une image Windows et modifier les supports d'installation de Windows.

Les étapes ci-dessous expliquent comment exécuter une analyse DISM :

**Étape 1** : Appuyez sur la touche `WIN` de votre clavier et recherchez "cmd". Ensuite, choisissez Exécuter en tant qu'administrateur à droite pour utiliser l'invite de commande en tant qu'administrateur. Assurez-vous de cliquer sur "Oui" dans la prochaine invite.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Étape 2** : Collez `dism /Online /Cleanup-Image /RestoreHealth` et appuyez sur `ENTRÉE`. Cela prend encore plus de temps que l'analyse SFC, alors soyez patient.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-3.png)

**Étape 3** : Une fois l'analyse terminée, redémarrez votre ordinateur et essayez de le réinitialiser à nouveau.
![completed-scan](https://www.freecodecamp.org/news/content/images/2021/12/completed-scan.png)

### Désactiver et réactiver ReAgentC.exe

REAgentC est un outil de récupération Windows qui tente de corriger les erreurs de démarrage lorsque votre ordinateur ne parvient pas à démarrer.

Puisque c'est ce que fait REAgent.exe, il peut y avoir des erreurs avec celui-ci si votre PC ne parvient pas à se réinitialiser. Ainsi, le désactiver et le réactiver peut corriger le problème pour vous.

Vous pouvez désactiver et réactiver REAgent.exe avec les étapes mises en évidence ci-dessous :

**Étape 1** : Appuyez sur la touche `WIN` de votre clavier et recherchez "cmd". Ensuite, choisissez Exécuter en tant qu'administrateur à droite.
![ss-1-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-1-2.jpg)

**Étape 2** : Tapez `reagentc /disable` et appuyez sur `ENTRÉE` pour désactiver REAgent.exe

**Étape 3** : Tapez `reagentc /enable` et appuyez sur `ENTRÉE` pour réactiver REAgent.exe
![ss-4](https://www.freecodecamp.org/news/content/images/2021/12/ss-4.png)

**Étape 4** : Redémarrez votre PC et essayez de le réinitialiser une fois de plus.

### Actualiser Windows depuis Windows Security

Avant de passer par cette solution, assurez-vous que vos fichiers sont sauvegardés.

Windows Security (anciennement Windows Defender) est largement connu comme un puissant programme antivirus pour les ordinateurs Windows 10, mais il y a plus à cela.

Avec Windows Security, vous pouvez donner à votre PC Windows 10 un nouveau départ. Les étapes ci-dessous vous montrent comment faire.

**Étape 1** : Appuyez sur `WIN` (touche du logo Windows) + I sur votre clavier pour lancer les Paramètres.

**Étape 2** : Choisissez Mise à jour et sécurité parmi les tuiles du menu.
![ss-5-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-1.jpg)

**Étape 3** : Passez à l'onglet Windows Security à gauche et sélectionnez "Performances et santé de l'appareil".
![ss-6-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-2.jpg)


**Étape 5** : Cliquez sur le lien "Informations supplémentaires" sous Nouveau départ.
![ss-7-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-7-2.jpg)

**Étape 6** : Cliquez sur le bouton "Démarrer".
![ss-8-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-8-1.jpg)

**Étape 7** : Suivez le reste des invites pour actualiser votre PC avec Windows Security.

## Mots de la fin

Ce guide vous a montré plusieurs façons de corriger votre PC lorsqu'il ne se réinitialise pas correctement. Maintenant, espérons que vous pouvez réinitialiser votre ordinateur et commencer à l'utiliser à nouveau avec succès.

En dernier recours, vous pouvez installer un nouveau système d'exploitation Windows 10 à partir d'un lecteur USB ou d'un DVD amorçable si vous rencontrez toujours l'erreur après avoir essayé les solutions suggérées dans cet article. En fait, certaines erreurs ne disparaissent pas à moins de faire cela.

Sachez que vous pouvez également rencontrer ce problème sur Windows 8 et 8.1, vous pouvez donc appliquer les mêmes solutions suggérées dans cet article.