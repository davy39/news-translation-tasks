---
title: Échec de la vérification de sécurité du noyau – Comment redémarrer le noyau
  dans Windows 10
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2022-09-14T15:41:50.000Z'
originalURL: https://freecodecamp.org/news/kernel-security-check-failure-how-to-restart-the-kernel-in-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/ScreenShot1_BSOD_Anger.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Échec de la vérification de sécurité du noyau – Comment redémarrer le noyau
  dans Windows 10
seo_desc: I’ve been a professional software engineer for many years, and I can testify
  that there are few things worse than getting the dreaded BSOD (Blue Screen of Death).
  Especially when you are about to write a piece of mind bending code at 2am to meet
  a lo...
---

Je suis ingénieur logiciel professionnel depuis de nombreuses années, et je peux témoigner qu'il y a peu de choses plus frustrantes que d'obtenir le redouté BSOD (Blue Screen of Death). Surtout lorsque vous êtes sur le point d'écrire un morceau de code complexe à 2h du matin pour respecter une date limite imminente. 

C'est juste ma perspective en tant qu'ingénieur logiciel, mais reconnaissons-le – utiliser un ordinateur de nos jours est absolument essentiel pour la plupart des professionnels. 

Le fait est que le blue screen of death est aussi bienvenu qu'un pigeon sur un échiquier lors d'un tournoi d'échecs de championnat du monde dans presque toutes les circonstances.

### Ce que vous allez apprendre

Dans cet article, nous allons examiner une cause particulièrement pernicieuse du BSOD, le redouté problème d'"Échec de la vérification de sécurité du noyau". Nous verrons également comment vous pouvez résoudre ce problème, si vous êtes confronté à ce problème abominable. 

## Causes courantes du BSOD

Les raisons courantes pour lesquelles vous pourriez rencontrer le problème "Échec de la vérification de sécurité du noyau" sont les fichiers système corrompus, le matériel défectueux ou les pilotes obsolètes.

### Fichiers système corrompus

Le malware est la cause la plus probable des fichiers système corrompus. Le terme "Malware" est une contraction de l'expression "Logiciel malveillant". Il s'agit d'un logiciel conçu délibérément pour être intrusif et causer des perturbations lorsque vous travaillez sur votre ordinateur. 

Vous avez probablement entendu parler de termes comme virus, virus cheval de Troie, vers, logiciels espions, ransomware, etc. Ce sont tous des exemples de logiciels malveillants, ou malware.

### Matériel défectueux

Une RAM (mémoire) défectueuse ou un disque dur corrompu ou endommagé pourrait être la cause du problème.

### Pilotes obsolètes

Parmi toutes les causes possibles de ce problème "Échec de la vérification de sécurité du noyau", la cause la plus probable est les pilotes obsolètes. 

Le problème des pilotes obsolètes peut provenir d'une mise à niveau d'une ancienne version de Windows vers Windows 10. Le pilote concerné peut avoir fonctionné parfaitement sur l'ancienne version de Windows mais peut être incompatible avec Windows 10.

## Qu'est-ce que le Blue Screen of Death ?

Généralement, vous prenez conscience du problème "Échec de la vérification de sécurité du noyau" lors du démarrage de Windows. C'est à ce moment que Windows effectue un processus de vérification. Si, lors de ce processus, Windows détecte une corruption dans des structures de données critiques, l'erreur Kernel_Security_check_failure est générée. 

Comme vous pouvez le voir sur la capture d'écran ci-dessous, il y a très peu de détails sur l'erreur. Heureusement, le message inclut un code d'arrêt (surligné en jaune) pour aider à identifier pourquoi vous êtes confronté au redouté BSOD.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-347.png)

## Comment corriger l'erreur d'échec de la vérification de sécurité du noyau

Heureusement, il existe de nombreuses solutions potentielles pour résoudre le problème "Échec de la vérification de sécurité du noyau". 

Pour résoudre le problème, vous pouvez suivre un processus d'investigation afin d'identifier la cause du problème. Une fois que vous avez identifié la cause du problème, vous saurez quelle solution appliquer. 

Mais une solution rapide, qui est le premier élément de la liste des solutions possibles fournies dans cet article, pourrait être aussi simple que de mettre à jour votre système vers la dernière version de Windows 10. 

Vous pouvez voir ci-dessous une liste des solutions discutées dans cet article. Les sections suivantes contiennent des instructions étape par étape pour chaque solution potentielle de la liste.

* Mettre à jour vers la dernière version publiée de Windows 10 
* Mettre à jour les pilotes qui doivent être mis à jour
* Vérifier la présence de virus
* Enquêter sur les éventuels fichiers système Windows corrompus
* Tester pour voir si la désactivation du logiciel antivirus corrige le problème
* Enquêter sur les éventuels problèmes avec la RAM
* Enquêter sur les éventuels problèmes de disque dur
* Tester pour voir si la désactivation du logiciel antivirus corrige le problème
* Démarrer le PC en mode sans échec

### Mettre à jour vers la dernière version publiée de Windows 10

Cela peut être le moyen le plus simple de corriger le problème. Pour mettre à jour Windows 10 vers la dernière version de Windows, vous pouvez suivre les étapes suivantes :

* Cliquez sur la touche Windows + I pour invoquer l'application Paramètres.
* Cliquez sur la vignette "Mise à jour et sécurité".
* Cliquez sur le bouton "Rechercher les mises à jour" (des informations sur l'état seront présentées à l'écran concernant la progression du téléchargement et de l'installation)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-348.png)

* Après la mise à jour, vérifiez si le BSOD se produit toujours.

### Mettre à jour les pilotes qui doivent être mis à jour

Un moyen facile de vérifier les pilotes problématiques est d'utiliser le Gestionnaire de périphériques.

Pour invoquer le Gestionnaire de périphériques, appuyez sur la touche Windows + X. Dans la boîte de dialogue qui s'affiche, une structure arborescente est affichée.

Si vous développez tous les nœuds de la structure arborescente, il devrait être évident de voir quels pilotes doivent être mis à jour – vous verrez un point d'exclamation avec un fond jaune à côté des nœuds représentant les pilotes qui doivent être mis à jour.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-349.png)

Pour mettre à jour un pilote, faites simplement un clic droit sur le nœud représentant le pilote concerné (qui doit être mis à jour) et cliquez sur l'élément de menu contextuel "Mettre à jour le pilote". 

Vous verrez alors deux options : vous pouvez soit sélectionner l'option où Windows 10 recherchera le pilote automatiquement, soit choisir l'option manuelle et rechercher sur votre ordinateur le nouveau fichier de pilote pertinent qui peut déjà exister sur votre ordinateur.

L'étape suivante consiste à permettre à la mise à jour de l'installation du pilote de se terminer.

Vous pouvez ensuite continuer à vérifier les autres pilotes problématiques en inspectant le Gestionnaire de périphériques pour les nœuds contenant des points d'exclamation avec des fonds jaunes. Si vous en trouvez d'autres, vous pouvez mettre à jour ces pilotes jusqu'à ce que tous les pilotes problématiques aient été mis à jour de manière appropriée.

Ensuite, vous devez simplement redémarrer votre ordinateur pour que les modifications apportées par les nouveaux pilotes soient complétées. Espérons que cela élimine votre problème de BSOD.

Si le problème persiste, votre investigation doit continuer...

### **Vérifier la présence de virus**

Vous devez vous assurer d'avoir installé les dernières mises à jour de Windows sur votre PC et utiliser le logiciel antivirus pour vérifier la présence de virus. 

Si un ou plusieurs virus sont trouvés, prenez les mesures nécessaires pour supprimer le ou les virus de votre ordinateur.

### Enquêter sur les éventuels fichiers système Windows corrompus

Vous pouvez utiliser l'outil de vérification des fichiers système (SFC) pour corriger les fichiers système corrompus. Voici les étapes que vous pouvez suivre pour exécuter l'outil de vérification des fichiers système.

* Depuis le bureau, utilisez la touche Windows + R pour ouvrir la boîte "Exécuter"
* Dans la boîte "Exécuter", tapez "cmd" puis appuyez sur ctrl+shift+enter pour lancer l'invite de commande avec des privilèges administratifs.
* Cliquez sur le bouton "Oui" de l'invite "Contrôle de compte d'utilisateur" (UAC)
* Tapez "SFC /scannow" dans la fenêtre d'invite de commande et appuyez sur "Entrée".

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-350.png)

L'utilitaire de vérification des fichiers système vérifiera l'intégrité des fichiers système de Windows et effectuera les opérations de réparation appropriées si nécessaire.

Redémarrez votre ordinateur après la fin du processus.

### Tester pour voir si la désactivation du logiciel antivirus corrige le problème

Le logiciel antivirus, bien qu'ayant de bonnes intentions, peut involontairement bloquer des services et applications non nuisibles et les empêcher de fonctionner correctement. 

Cette méthode vous indiquera (pour ainsi dire) que votre logiciel antivirus peut être la cause de votre problème – mais veuillez noter qu'il n'est pas recommandé de faire fonctionner votre ordinateur sans la protection d'un logiciel antivirus approprié.

Pour désactiver temporairement votre logiciel antivirus, vous pouvez simplement invoquer la fenêtre du gestionnaire des tâches. Vous pouvez le faire en appuyant sur ctrl+shift+échap sur votre clavier.

Si le gestionnaire des tâches se charge en mode compact, cliquez sur l'option "Plus de détails". Sélectionnez ensuite l'onglet "Démarrage" en haut de la fenêtre "Gestionnaire des tâches".

Trouvez le nom représentant votre application antivirus et cliquez sur l'élément de liste pertinent.

Cliquez ensuite sur le bouton de désactivation qui sera présent dans le coin droit de la fenêtre du Gestionnaire des tâches.

Enfin, redémarrez l'ordinateur et voyez si le BSOD apparaît toujours. 

Encore une fois, rappelez-vous que même si cela corrige le problème, vous ne devriez pas faire fonctionner votre ordinateur sans logiciel antivirus. Vous devrez donc probablement chercher des alternatives pour la protection.

### Enquêter sur les éventuels problèmes avec la RAM

Pour identifier les problèmes de RAM (mémoire), vous pouvez invoquer l'outil d'analyse intégré de Windows 10. Pour ce faire, cliquez sur l'icône de la loupe de recherche dans la barre des tâches ou appuyez sur la touche Windows + S.

Tapez "Diagnostic de mémoire" dans la zone de texte de recherche et exécutez la première option présentée dans les résultats de recherche.

Dans la boîte de dialogue contextuelle qui s'affiche, sélectionnez l'option "Redémarrer maintenant et vérifier les problèmes (recommandé)" pour lancer le processus de diagnostic.

Pendant le processus de démarrage, le processus de diagnostic de la mémoire tentera d'identifier les erreurs et problèmes possibles concernant la RAM. Si des problèmes sont trouvés, ils vous seront signalés.

### Enquêter sur les éventuels problèmes de disque dur

Vous pouvez analyser vos disques durs pour détecter toute incohérence et erreur à l'aide de l'outil de vérification de disque.

Pour exécuter l'outil de vérification de disque, assurez-vous d'être connecté à Windows avec un compte administrateur. Suivez ensuite ces étapes :

* Sur le bureau, cliquez sur la touche Windows + R pour lancer la boîte "Exécuter".
* Dans la boîte "Exécuter", tapez "cmd" puis appuyez sur ctrl+shift+enter pour exécuter l'invite de commande en tant qu'administrateur.
* Cliquez sur le bouton "Oui" de l'invite "Contrôle de compte d'utilisateur" (UAC).
* Tapez "chkdsk c: /f" et appuyez sur Entrée

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-351.png)

L'option "/f" tentera de corriger les erreurs trouvées

Vous pourriez également inclure l'option "/r" et l'option "/x" avec cette commande. L'option "/r" localisera les secteurs défectueux et récupérera toute information lisible, tandis que l'option "/x" force le disque dur (sur le point d'être vérifié) à être démonté avant que l'utilitaire ne commence une analyse.

### Démarrer le PC en mode sans échec

Vous pouvez démarrer vos PC en mode sans échec afin que Windows 10 soit démarré avec des fichiers et pilotes minimaux. Pour démarrer Windows 10 en mode sans échec, vous pouvez suivre ces étapes :

* Appuyez sur la touche Windows + I pour invoquer l'application Paramètres.
* Sous l'en-tête "Mise à jour et sécurité", sélectionnez l'onglet "Récupération".
* Sous l'en-tête "Démarrage avancé" dans le volet de droite, appuyez sur le bouton "Redémarrer maintenant".

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-352.png)

* Après le redémarrage du PC sur l'écran "Choisir une option", sélectionnez Dépannage > Options avancées > Paramètres de démarrage > Redémarrer.

Après le redémarrage du PC, une liste d'options s'affiche. Sélectionnez "4" ou appuyez sur "F4" pour démarrer le PC en mode sans échec. Ou si vous devez utiliser Internet, vous pouvez sélectionner "5" ou appuyer sur "F5" pour le mode sans échec avec réseau. 

Si le problème ne se produit pas en mode sans échec, cela signifie que les paramètres par défaut et les pilotes de périphériques de base ne causent pas le problème. 

En supposant que le problème ne se produit pas en mode sans échec, vous savez maintenant que le problème doit être causé par un pilote ou une application supplémentaire qui s'exécute en mode normal.

En utilisant un processus d'élimination, vous pouvez maintenant vous concentrer sur les pilotes et applications supplémentaires pertinents. Vous pouvez désinstaller systématiquement chacune des applications pertinentes en commençant par les plus récemment installées et en travaillant des plus récemment installées aux moins récemment installées. 

Avec chaque désinstallation, vous pouvez tester le problème. Cela permettra, espérons-le, d'identifier l'application ou le programme qui était à l'origine du problème. Vous pouvez ensuite désinstaller le logiciel pertinent pour, espérons-le, vous débarrasser du problème.

## Conclusion

En conclusion, le problème d'échec de la vérification de sécurité du noyau peut être une énorme gêne. Mais espérons que les étapes fournies dans cet article vous aideront à résoudre le problème.