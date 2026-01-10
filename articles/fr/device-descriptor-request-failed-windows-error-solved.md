---
title: Échec de la demande de descripteur de périphérique – Comment corriger l'erreur
  de périphérique USB inconnu dans Windows 10
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2022-10-28T23:49:33.000Z'
originalURL: https://freecodecamp.org/news/device-descriptor-request-failed-windows-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Screenshot1.jpg
tags:
- name: error
  slug: error
- name: usb
  slug: usb
- name: Windows 10
  slug: windows-10
seo_title: Échec de la demande de descripteur de périphérique – Comment corriger l'erreur
  de périphérique USB inconnu dans Windows 10
seo_desc: "Recently my uncle, who lives in Australia, sent my parents, who live in\
  \ South Africa, a flash drive that was full of pictures of our Australian family\
  \ getting up to various Australian activities. \nBut it was very frustrating for\
  \ my poor Mom when her ..."
---

Récemment, mon oncle, qui vit en Australie, a envoyé à mes parents, qui vivent en Afrique du Sud, une clé USB remplie de photos de notre famille australienne s'adonnant à diverses activités australiennes. 

Mais ce fut très frustrant pour ma pauvre maman lorsque son ordinateur portable n'a pas reconnu le périphérique USB (la clé USB contenant les photos de la famille australienne). 

J'ai le _privilège_ d'être le membre de la famille vers qui on se tourne lorsque quelque chose ne va pas avec quelque chose lié à l'informatique, parce que je suis programmeur. Cela signifie que je dois tout savoir sur les ports USB, les imprimantes, les scanners, bref, tout ce qui est lié à l'informatique... n'est-ce pas ? 

À l'époque, je dois avouer que je n'avais aucune idée de pourquoi Windows 10 ne reconnaissait pas la clé USB. J'ai donc fait quelques recherches. Dans ce cas particulier, le périphérique externe (la clé USB) était le coupable. 

Il s'avère cependant que ce problème d'« Échec de la demande de descripteur de périphérique » peut survenir pour de nombreuses raisons différentes, certaines liées au matériel et d'autres au logiciel. 

Dans cet article, je vais d'abord aborder les problèmes matériels possibles, puis nous examinerons les problèmes logiciels possibles. Pour chaque cause de l'erreur « Échec de la demande de descripteur de périphérique », je vous guiderai à travers les étapes nécessaires pour résoudre le problème.

## Causes possibles et solutions pour l'erreur "Échec de la demande de descripteur de périphérique"

Les sept titres suivants listent ce qui peut avoir causé le problème « Échec de la demande de descripteur de périphérique ». Dans les sections suivantes de cet article, je vous donnerai des détails sur la manière dont vous pourrez peut-être résoudre le problème.

* **Défaillance matérielle USB**
* **Exécuter le dépannage du matériel et des périphériques**
* **Mettre à jour le pilote du périphérique USB**
* **Désactiver le démarrage rapide**
* **Désactiver le paramètre de suspension sélective USB**
* **Retirer le périphérique USB et analyser les modifications matérielles**
* **Mettre à jour Windows 10**

## Défaillance matérielle USB

Le problème « Échec de la demande de descripteur de périphérique » peut avoir été causé par un problème matériel. Nous pouvons facilement tester si le problème provient d'un problème matériel et non d'un problème lié au système d'exploitation en effectuant les vérifications suivantes :

Tout d'abord, branchez le périphérique concerné dans un port USB différent sur le même ordinateur. Par précaution, essayez plusieurs ports USB. Si le périphérique concerné fonctionne lorsqu'il est branché dans un autre port USB, cela signifie que la source du problème est probablement le port USB utilisé lorsque le problème survient. 

Dans ce cas, vous pouvez simplement marquer le port USB causant le problème comme défectueux et utiliser le port USB qui fonctionne. Vous pouvez également souhaiter remplacer le port USB défectueux à un moment donné.

Deuxièmement, vous pouvez brancher le périphérique concerné dans un port USB sur un autre ordinateur. Si le périphérique ne fonctionne pas sur un autre ordinateur, cela indique que le périphérique lui-même est le problème. Votre seule solution dans ce cas peut être de réparer ou de remplacer le périphérique lui-même.

## Exécuter le dépannage du matériel et des périphériques

Windows nous fournit un outil très pratique que vous pouvez utiliser pour effectuer le dépannage. Vous pouvez utiliser cet outil pour dépanner les problèmes matériels possibles. 

Suivez ces étapes pour utiliser l'outil **Dépannage** :

* Tout d'abord, invoquez la boîte "Exécuter". Vous pouvez le faire en appuyant sur la touche Windows + R.
* Entrez la commande suivante dans la boîte "Exécuter" : **msdt.exe -id DeviceDiagnostic**

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-235.png)

* Appuyez sur le bouton **OK**. 
* Sélectionnez Avancé – et assurez-vous que la case à cocher "Appliquer les réparations automatiquement" est cochée. Appuyez sur le bouton "Suivant" et suivez les instructions pour effectuer la tâche de dépannage.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-236.png)

## Désinstaller et mettre à jour le pilote du périphérique USB

Pour désinstaller le pilote du périphérique USB, nous pouvons utiliser l'outil **Gestionnaire de périphériques** fourni par Windows. Pour exécuter le **Gestionnaire de périphériques**, suivez ces étapes :

* Tout d'abord, invoquez la boîte "Exécuter". Une façon de le faire est d'appuyer sur **Windows + R**. 
* Entrez la commande suivante dans la boîte "Exécuter" : **devmgmt.msc**. Ensuite, appuyez sur le bouton **OK**. 
* Dans la structure arborescente présentée dans la boîte de dialogue **Gestionnaire de périphériques**, développez le nœud **Contrôleurs de bus série universel**. 
* Dans la liste développée des nœuds, sélectionnez le nœud marqué "Périphérique USB inconnu (Échec de la demande de descripteur de périphérique)". 
* Cliquez avec le bouton droit sur ce nœud et sélectionnez **Désinstaller le périphérique** dans le menu contextuel présenté.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-237.png)

* Une fois l'opération de désinstallation terminée, redémarrez votre ordinateur. Cela entraînera la réinstallation du pilote, ce qui peut également résoudre votre problème.

## Désactiver le démarrage rapide

Une cause possible du problème « Échec de la demande de descripteur de périphérique » pourrait provenir d'une fonctionnalité de Windows conçue pour accélérer le processus de démarrage de votre ordinateur. Parfois, cette fonctionnalité de « Démarrage rapide » peut empêcher votre système d'exploitation de détecter les périphériques USB. 

Heureusement, nous avons la possibilité de désactiver cette fonctionnalité. La fonctionnalité « Démarrage rapide » est une fonctionnalité « agréable à avoir » et il est recommandé de l'activer, mais ce n'est pas une fonctionnalité essentielle. 

Pour désactiver la fonctionnalité, suivez ces étapes :

* Appuyez sur Windows + R pour invoquer la boîte "Exécuter". 
* Dans la boîte "Exécuter", tapez "control" et cliquez sur le bouton "OK" pour ouvrir le Panneau de configuration. 
* Dans la zone de recherche de votre Panneau de configuration, tapez "Options d'alimentation" puis cliquez sur "Modifier le comportement des boutons d'alimentation". 
* Sous le titre "Définir les boutons d'alimentation et activer la protection par mot de passe", cliquez sur le lien intitulé "Modifier les paramètres actuellement non disponibles". 
* Assurez-vous que la case à cocher "Activer le démarrage rapide (recommandé)" est décochée. Cliquez sur le bouton "Enregistrer les modifications".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-238.png)

* Redémarrez votre ordinateur et vérifiez si cette solution possible a résolu votre problème de périphérique USB.

## Désactiver le paramètre de suspension sélective USB

Parfois, le port USB est mis en mode basse consommation lorsque le paramètre "Suspension sélective USB" est activé. Cela peut provoquer un comportement anormal lors de la connexion d'un périphérique à un port USB, ce qui peut entraîner le problème "Échec de la demande de descripteur de périphérique". 

Nous pouvons désactiver cette fonctionnalité en toute sécurité, et ce faisant, résoudre potentiellement le problème "Échec de la demande de descripteur de périphérique". 

Pour désactiver le paramètre "Suspension sélective USB", suivez ces étapes.

* Appuyez sur Windows + R pour invoquer la boîte "Exécuter". 
* Dans la boîte "Exécuter", tapez "control" et cliquez sur le bouton "OK" pour ouvrir le Panneau de configuration. 
* Dans votre Panneau de configuration, trouvez et cliquez sur "Options d'alimentation". 
* Cliquez sur le lien "Modifier les paramètres du mode". 
* Cliquez sur le lien "Modifier les paramètres d'alimentation avancés". 
* Trouvez et développez le nœud "Paramètres USB" dans la structure arborescente trouvée dans l'onglet "Paramètres avancés". 
* Développez le nœud enfant "Paramètre de suspension sélective USB". 
* Assurez-vous que "Désactivé" est sélectionné dans la liste déroulante pertinente pour "Sur batterie" et "Branché".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-239.png)

* Cliquez sur le bouton "OK". 
* Redémarrez votre ordinateur. 
* Une fois votre ordinateur redémarré, testez pour voir si le problème "Échec de la demande de descripteur de périphérique" a été résolu.

## Retirer le périphérique USB et analyser les modifications matérielles

* Lancez le **Gestionnaire de périphériques** en appuyant sur Windows + R pour lancer la boîte "Exécuter", puis tapez **devmgmt.msc** dans la boîte "Exécuter" et appuyez sur le bouton "OK". 
* Déconnectez le périphérique problématique du port USB concerné. 
* Dans la boîte de dialogue **Gestionnaire de périphériques**, cliquez sur le bouton "Analyser les modifications matérielles" dans la barre d'outils. Vous pouvez identifier le bouton pertinent en survolant le bouton avec le pointeur de la souris, ce qui affichera le texte d'info-bulle "Analyser les modifications matérielles".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-240.png)

* Lorsque le système reconnaît les modifications matérielles, branchez le périphérique USB concerné et testez si le problème a été résolu.

## Mettre à jour Windows

L'installation de la dernière mise à jour de Windows peut corriger le problème "Échec de la demande de descripteur de périphérique". Pour installer la dernière mise à jour de Windows, vous pouvez suivre ces étapes :

* Ouvrez l'application Paramètres en appuyant sur Windows + I. 
* Cliquez sur l'option "Mise à jour et sécurité". 
* Sélectionnez l'option "Mise à jour Windows". 
* Cliquez sur le bouton "Rechercher les mises à jour".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-241.png)

* Redémarrez l'ordinateur et testez pour voir si le problème "Échec de la demande de descripteur de périphérique" persiste.

## Conclusion

Le problème "Échec de la demande de descripteur de périphérique" peut causer beaucoup de frustration et même de la peine, comme dans le cas de ma pauvre mère, où cela l'a empêchée de voir les photos de famille. 

Ne désespérez pas – espérons que cet article vous fournit un remède efficace pour le problème.