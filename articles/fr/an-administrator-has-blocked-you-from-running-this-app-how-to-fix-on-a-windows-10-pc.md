---
title: Un administrateur vous a bloqué l'exécution de cette application – Comment
  le corriger sur un PC Windows 10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-21T15:51:17.000Z'
originalURL: https://freecodecamp.org/news/an-administrator-has-blocked-you-from-running-this-app-how-to-fix-on-a-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dadminError.jpg
tags:
- name: error
  slug: error
- name: Security
  slug: security
- name: Windows 10
  slug: windows-10
seo_title: Un administrateur vous a bloqué l'exécution de cette application – Comment
  le corriger sur un PC Windows 10
seo_desc: "Sometimes when you decide to open an app or file or install or open a program\
  \ on your Windows 10 PC, you might get the error \"An administrator has blocked\
  \ you from running this app\". \nYou get this error because Windows 10 is optimized\
  \ for protection ..."
---

Parfois, lorsque vous décidez d'ouvrir une application ou un fichier, ou d'installer ou d'ouvrir un programme sur votre PC Windows 10, vous pouvez obtenir l'erreur "Un administrateur vous a bloqué l'exécution de cette application".

Vous obtenez cette erreur parce que Windows 10 est optimisé pour la protection contre les logiciels malveillants grâce à Windows Defender et au Contrôle de compte d'utilisateur (UAC).

Mais parfois, cette protection est trop sensible. Ainsi, à certaines occasions, l'erreur se produit même lorsque vous essayez d'exécuter des applications de confiance ou d'ouvrir des fichiers de confiance.

Aujourd'hui est, espérons-le, le dernier jour où vous verrez cette erreur s'afficher sur votre PC Windows 10. Car dans cet article, je vais vous montrer 5 façons de la corriger, afin que vous puissiez commencer à utiliser votre ordinateur sans craindre cette erreur.

**PS** : Si vous obtenez cette erreur en exécutant une application de confiance ou en essayant d'ouvrir un fichier de confiance, les solutions fournies dans cet article sont pour vous. Si vous ne faites pas confiance à l'application, utilisez l'une des solutions seulement si vous êtes prêt à prendre un risque.

## Table des matières
- [Désactiver temporairement votre programme antivirus](#heading-solution-1-desactiver-temporairement-votre-programme-antivirus)
- [Désactiver la fonctionnalité Windows Smartscreen](#heading-solution-2-desactiver-la-fonctionnalite-windows-smartscreen)
- [Déverrouiller le fichier](#heading-solution-3-deverrouiller-le-fichier)
- [Exécuter l'application avec l'invite de commandes](#heading-solution-4-executer-lapplication-avec-linvite-de-commandes)
- [Apporter des modifications à la stratégie de groupe](#heading-solution-5-apporter-des-modifications-a-la-strategie-de-groupe)
- [Conclusion](#heading-conclusion)

## Solution 1 : Désactiver temporairement votre programme antivirus

Si vous obtenez l'erreur "Un administrateur vous a bloqué l'exécution de cette application", cela pourrait être dû à votre application antivirus.

Ainsi, désactiver l'application antivirus pourrait fournir une solution.

Que vous utilisiez le Windows Defender intégré ou un programme antivirus tiers, les étapes ci-dessous vous aideront à le désactiver.

**Étape 1** : Appuyez sur `ALT` + `SHIFT` + `ESC` sur votre clavier pour ouvrir le Gestionnaire des tâches.

**Étape 2** : Passez à l'onglet Démarrage.

**Étape 3** : Localisez votre programme antivirus dans la liste, faites un clic droit dessus et sélectionnez "Désactiver".
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.jpg)

**PS** : Si vous ne trouvez pas votre programme antivirus dans l'onglet de démarrage, vérifiez alors l'onglet Processus.

## Solution 2 : Désactiver la fonctionnalité Windows Smartscreen

Windows Smartscreen est une fonctionnalité anti-logiciels malveillants qui travaille avec Windows Defender pour bloquer les logiciels malveillants.

Parfois, elle déclenche cette erreur même lorsque vous utilisez une application de confiance.

Pour désactiver Smartscreen, suivez les étapes ci-dessous :

**Étape 1** : Appuyez sur `WIN` + `S` sur votre clavier et recherchez "smartscreen", puis cliquez sur le résultat de recherche "Contrôle des applications et du navigateur".
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-2.jpg)

**Étape 2** : Ouvrez le lien "Paramètres de protection basés sur la réputation".
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-3.jpg)

**Étape 3** : Désactivez le bouton sous "Blocage des applications potentiellement indésirables".
![ss-4-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-3.jpg)

## Solution 3 : Déverrouiller le fichier

Si vous obtenez l'erreur lors de l'ouverture d'un fichier, cette solution est pour vous.

**Étape 1** : Faites un clic droit sur le fichier et sélectionnez Propriétés.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-3.jpg)

**Étape 2** : Dans l'onglet Général, cochez "Déverrouiller" sous "Sécurité".

**Étape 3** : Cliquez sur Appliquer puis sur Ok.
![ss-6-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-3.jpg)

## Solution 4 : Exécuter l'application avec l'invite de commandes

L'invite de commandes vous permet d'exécuter une application et de contourner la vérification de l'administrateur.

Ainsi, vous pouvez éviter d'obtenir cette erreur si vous exécutez l'application déclenchant l'erreur en utilisant l'invite de commandes.

Les étapes suivantes vous montrent comment exécuter une application avec l'invite de commandes :

**Étape 1** : Localisez l'application déclenchant l'erreur, faites un clic droit dessus et sélectionnez Ouvrir l'emplacement du fichier.
![ss-7-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-1.jpg)

**Étape 2** : Faites un clic droit sur le fichier et sélectionnez Propriétés.
![ss-8-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-8-3.jpg)

**Étape 3** : Dans l'onglet Général, copiez le texte sous Emplacement. Ne fermez pas encore la fenêtre Propriétés.
![ss-9-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-9-1.png)

**Étape 4** : Cliquez sur Démarrer et recherchez "cmd", puis sélectionnez Exécuter en tant qu'administrateur à droite.
![cmd-admin-3](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin-3.jpg)

**Étape 5** : Dans l'invite de commandes, collez le texte que vous avez copié à l'étape 3, puis minimisez l'invite de commandes.
![ss-10-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-10-2.png)

**Étape 5** : Retournez aux Propriétés ouvertes à l'Étape 1 et copiez le nom du fichier.
![ss-11-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-11-1.png)

**Étape 6** : Maximisez l'invite de commandes, tapez "\" (barre oblique) devant le texte que vous avez collé à l'Étape 4, et collez le nom du fichier, comme vous pouvez le voir dans la capture d'écran ci-dessous.
![ss-12-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-12-1.png)

**Étape 7** : Appuyez sur `ENTRÉE` pour enfin lancer l'application.

## Solution 5 : Apporter des modifications à la stratégie de groupe

Avec la stratégie de groupe, vous pouvez apporter des modifications que vous ne trouverez pas facilement ailleurs sur votre ordinateur.

L'une de ces modifications peut être apportée au Contrôle de compte d'utilisateur (UAC) pour permettre aux applications d'échapper à la vérification de l'administrateur.

Pour apporter les modifications qui élimineront l'erreur, suivez les étapes ci-dessous :

**Étape 1** : Appuyez sur `WIN` + `R` sur votre clavier pour ouvrir la boîte de dialogue Exécuter.

**Étape 2** : Dans la boîte de dialogue Exécuter, tapez "gpedit.msc" et appuyez sur `ENTRÉE` sur votre clavier.
![ss-13-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-13-1.png)

**Étape 3** : Sous Configuration de l'ordinateur, développez Paramètres Windows, Paramètres de sécurité et Stratégies locales.

**Étape 4** : Cliquez sur Options de sécurité. N'essayez pas de le développer, cliquez simplement dessus.
![ss-14-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-14-1.jpg)

**Étape 5** : Descendez et double-cliquez sur "Contrôle de compte d'utilisateur : Exécuter tous les administrateurs en mode d'approbation de l'administrateur".
![ss-15](https://www.freecodecamp.org/news/content/images/2022/01/ss-15.jpg)

**Étape 6** : Sélectionnez Désactiver, cliquez sur Appliquer, puis sur Ok.
![ss-16](https://www.freecodecamp.org/news/content/images/2022/01/ss-16.jpg)

## Conclusion

Cet article vous a montré 5 façons différentes de corriger l'erreur "Un administrateur vous a bloqué l'exécution de cette application".

Ce message d'erreur n'est qu'une des 3 façons dont l'erreur pourrait apparaître.

Si vous l'obtenez sous la forme "Votre administrateur système a bloqué ce programme Stratégie de groupe, GPO, Regedit", alors la [solution 5](#heading-solution-5-apporter-des-modifications-a-la-strategie-de-groupe) est pour vous.

Si vous l'obtenez sous la forme "Votre administrateur système a bloqué ce programme uTorrent, Avast, AVG", alors la [solution 1](#heading-solution-1-desactiver-temporairement-votre-programme-antivirus) est pour vous.

En bref, vous devrez simplement déterminer la source de l'erreur et choisir la solution qui convient à votre situation.

Si vous trouvez cet article utile, envisagez de le partager avec vos amis et votre famille.

Merci d'avoir lu.