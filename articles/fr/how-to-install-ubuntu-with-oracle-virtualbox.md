---
title: Comment installer Ubuntu sur VirtualBox
date: '2019-12-06T12:10:50.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/how-to-install-ubuntu-with-oracle-virtualbox
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/ubuntu-1479782_1280.jpg
tags:
- name: Ubuntu
  slug: ubuntu
- name: 'VirtualBox '
  slug: virtualbox
seo_desc: 'By Thanoshan MV

  What is VirtualBox?

  Oracle VM VirtualBox is a cross-platform virtualization application developed by
  the Oracle Corporation. It allows users to install operating systems on virtual
  hard disks such as Windows, macOS, Solaris and Linux....'
---


Par Thanoshan MV

<!-- more -->

## Qu'est-ce que VirtualBox ?

Oracle VM VirtualBox est une application de virtualisation multiplateforme développée par Oracle Corporation. Elle permet aux utilisateurs d'installer des systèmes d'exploitation sur des disques durs virtuels, tels que Windows, macOS, Solaris et Linux.

Par exemple, vous pouvez exécuter Windows et Linux sur votre Mac, faire tourner un serveur Windows sur votre serveur Linux, ou utiliser Linux sur votre PC Windows tout en exécutant vos autres applications existantes.

L'espace disque et la mémoire vive (RAM) sont les seuls problèmes que vous rencontrerez lors de l'installation de plusieurs machines virtuelles.

## Pourquoi vous en aurez besoin

-   Oracle VirtualBox est facile à installer et à utiliser.
-   C'est gratuit.
-   Vous pouvez exécuter et tester n'importe quel système d'exploitation en toute sécurité.
-   Si vous êtes un développeur, VirtualBox peut être utilisé comme un outil pour tester vos propres projets de développement en toute sécurité dans plusieurs environnements d'OS.
-   Il peut s'exécuter partout, des petits systèmes embarqués aux ordinateurs portables.
-   C'est idéal pour les tests et la reprise après sinistre, car il peut être facilement copié, sauvegardé et transporté entre les hôtes.

## Installation de VirtualBox

VirtualBox peut être téléchargé ici : [Téléchargements VirtualBox][1]

## Pourquoi Ubuntu ?

-   C'est gratuit.
-   Personnalisation facile : l'environnement de bureau GNOME vous aide à personnaliser l'interface facilement.
-   C'est sécurisé.
-   Ubuntu est open-source.
-   Une communauté amicale et solidaire.
-   Faibles exigences système.
-   Selon [FOSSBYTES][2], Ubuntu est la deuxième meilleure distribution Linux pour la programmation et les développeurs [Édition 2019].
-   C'est adapté aux débutants.

## Configuration pour Ubuntu

Tout d'abord, ouvrez VirtualBox, puis cliquez sur "New" (Nouveau) pour créer une machine virtuelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/start-1.png)

Saisissez "Ubuntu" comme nom, sélectionnez "Linux" comme type, et sélectionnez Ubuntu (64-bit) comme version.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--14-.png)

**NOTE :** Sélectionnez la quantité de mémoire que vous souhaitez, mais n'ajoutez pas plus de 50 % de votre RAM totale.

Cochez l'option "Create a virtual hard disk now" (Créer un disque dur virtuel maintenant) afin que nous puissions définir plus tard la taille du disque dur virtuel de notre OS Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--16-.png)

Maintenant, nous voulons sélectionner "VHD (Virtual Hard Disk)".

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--17--1.png)

Ensuite, nous allons allouer dynamiquement le stockage sur notre disque dur physique.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--18-.png)

Nous devons spécifier la taille de notre OS Ubuntu. La taille recommandée est de 10 Go, mais vous pouvez l'augmenter si vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--19-.png)

Après avoir créé un disque dur virtuel, vous verrez Ubuntu dans votre tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--20-.png)

Maintenant, nous devons configurer le fichier image disque Ubuntu (.iso).

Le fichier image disque Ubuntu peut être téléchargé ici : [Téléchargement de l'OS Ubuntu][3]

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--23-.png)

Pour configurer le fichier image disque Ubuntu, allez dans les paramètres et suivez ces étapes :

1.  Cliquez sur "Storage" (Stockage)
2.  Dans les périphériques de stockage, cliquez sur "Empty" (Vide)
3.  Dans les attributs, cliquez sur l'icône de disque et "Choose Virtual Optical Disk File" (Choisir un fichier de disque optique virtuel)
4.  Sélectionnez le fichier image disque Ubuntu et ouvrez-le

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--25-.png)

Cliquez sur OK.

Votre OS Ubuntu est prêt à être installé dans VirtualBox. Commençons !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--26-.png)

**NOTE :** Les étapes d'installation d'Ubuntu sur VirtualBox et les étapes d'installation réelle de l'OS peuvent varier. Ce guide vous aide uniquement à installer Ubuntu dans VirtualBox.

## Installons Ubuntu !

Cliquez sur "Install Ubuntu" (Installer Ubuntu).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--27-.png)

Sélectionnez la disposition de votre clavier.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--29-.png)

Dans la section "Updates and other software" (Mises à jour et autres logiciels), cochez "Normal installation" (Installation normale) et continuez.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--30-.png)

Dans "Installation type" (Type d'installation), cochez "Erase disk and install Ubuntu" (Effacer le disque et installer Ubuntu).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--31-.png)

Cliquez sur "Continue" (Continuer).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--32-.png)

Choisissez votre emplacement actuel.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--33-.png)

Maintenant, configurez votre profil.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--34-.png)

Vous verrez Ubuntu en cours d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--35-.png)

Après l'installation, redémarrez le système.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--36-.png)

Après vous être connecté, vous verrez le bureau Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--40-.png)

Nous avons installé Ubuntu avec succès dans VirtualBox. Il est prêt à être utilisé pour vos futurs projets de développement.

## Vérifions l'installation.

Ouvrez votre terminal (Appuyez sur Ctrl+Alt+T), tapez les commandes ci-dessous et vérifiez si elles fonctionnent.

1.  pwd : Cela affichera le répertoire de travail actuel.
2.  ls : Cela listera tous les éléments de votre répertoire actuel.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--43-.png)

Après avoir vérifié cela, éteignez votre machine en utilisant la commande suivante.

```
poweroff
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot--44-.png)

## Conclusion

VirtualBox est gratuit et constitue un excellent outil pour exécuter plusieurs systèmes d'exploitation sur un seul OS. Ubuntu présente de nombreux avantages. Si vous débutez sur Linux, je vous recommande d'utiliser Ubuntu car il est très accessible aux débutants.

N'hésitez pas à me faire savoir si vous avez des questions.

Vous pouvez me contacter et vous connecter avec moi sur [Twitter][4] et [Medium][5].

Merci de m'avoir lu.

**Bon code !**

[1]: https://www.virtualbox.org/wiki/Downloads
[2]: https://fossbytes.com/best-linux-distros-for-programming-developers/
[3]: https://ubuntu.com/#download
[4]: https://twitter.com/ThanoshanMV
[5]: https://medium.com/@mvthanoshan9