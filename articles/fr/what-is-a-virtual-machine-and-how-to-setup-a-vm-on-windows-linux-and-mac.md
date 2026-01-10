---
title: Qu'est-ce qu'une machine virtuelle et comment configurer une VM sur Windows,
  Linux et Mac
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-12-19T21:19:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e98740569d1a4ca3df6.jpg
tags:
- name: Virtual Reality
  slug: virtual-reality
- name: 'VirtualBox '
  slug: virtualbox
seo_title: Qu'est-ce qu'une machine virtuelle et comment configurer une VM sur Windows,
  Linux et Mac
seo_desc: "A virtual machine is a program you run on a computer that acts like it\
  \ is a separate computer. It is basically a way to create a computer within a computer.\
  \ \nA virtual machine runs in a window on the host computer and gives a user the\
  \ same experience..."
---

Une machine virtuelle est un programme que vous exécutez sur un ordinateur et qui agit comme s'il s'agissait d'un ordinateur séparé. C'est essentiellement un moyen de créer un ordinateur dans un ordinateur. 

Une machine virtuelle s'exécute dans une fenêtre sur l'ordinateur hôte et offre à l'utilisateur la même expérience que s'il utilisait un ordinateur complètement différent. Les machines virtuelles sont isolées de l'ordinateur hôte. Cela signifie que rien de ce qui s'exécute sur la machine virtuelle ne peut impacter l'ordinateur hôte.

Les machines virtuelles sont souvent utilisées pour exécuter des logiciels sur des systèmes d'exploitation pour lesquels ils n'étaient pas initialement prévus. Par exemple, si vous utilisez un ordinateur Mac, vous pouvez exécuter des programmes Windows dans une machine virtuelle Windows sur l'ordinateur Mac. Les machines virtuelles sont également utilisées pour configurer rapidement des logiciels avec une image, accéder à des données infectées par des virus et tester d'autres systèmes d'exploitation.

Un seul ordinateur physique peut exécuter plusieurs machines virtuelles en même temps. Souvent, un serveur utilise un programme appelé hyperviseur pour gérer plusieurs machines virtuelles qui s'exécutent simultanément. Les machines virtuelles disposent de matériel virtuel, y compris des CPU, de la mémoire, des disques durs, etc. Chaque élément de matériel virtuel est mappé au matériel réel de l'ordinateur hôte.

Il y a quelques inconvénients avec les machines virtuelles. Puisque les ressources matérielles sont indirectes, elles ne sont pas aussi efficaces qu'un ordinateur physique. De plus, lorsque de nombreuses machines virtuelles s'exécutent en même temps sur un seul ordinateur, les performances peuvent devenir instables.

## Programmes de machines virtuelles

Il existe de nombreux programmes de machines virtuelles différents que vous pouvez utiliser. Certaines options sont VirtualBox (Windows, Linux, Mac OS X), VMware Player (Windows, Linux), VMware Fusion (Mac OS X) et Parallels Desktop (Mac OS X).

VirtualBox est l'un des programmes de machines virtuelles les plus populaires car il est gratuit, open source et disponible sur tous les systèmes d'exploitation populaires. Nous allons vous montrer comment configurer une machine virtuelle en utilisant VirtualBox.

## Configuration d'une machine virtuelle (VirtualBox)

![Image](https://upload.wikimedia.org/wikipedia/commons/d/d5/Virtualbox_logo.png)

VirtualBox est un programme de machine virtuelle open source d'Oracle. Il permet aux utilisateurs d'installer virtuellement de nombreux systèmes d'exploitation sur des disques virtuels, y compris Windows, BSD, Linux, Solaris, et plus encore.

Puisque VirtualBox fonctionne sur Windows, Linux et Mac, le processus de configuration d'une machine virtuelle est pratiquement le même dans chaque système d'exploitation.

Commencez par télécharger et installer VirtualBox. Vous pouvez le télécharger à ce lien : [Téléchargements VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Vous devrez également télécharger un fichier .iso pour le système d'exploitation que vous souhaitez exécuter dans votre machine virtuelle. Par exemple, vous pouvez télécharger un fichier .iso de Windows 10 ici : [https://www.microsoft.com/en-us/software-download/windows10ISO](https://www.microsoft.com/en-us/software-download/windows10ISO)

Une fois que vous avez VirtualBox en cours d'exécution, cliquez sur le bouton "Nouveau"

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-68.png)
_Créer une nouvelle machine virtuelle._

Ensuite, vous devrez choisir le système d'exploitation que vous prévoyez d'installer. Dans la boîte "Nom", tapez le nom du système d'exploitation que vous souhaitez installer. VirtualBox devinera le type et la version en fonction du nom que vous tapez, mais vous pouvez modifier ces paramètres si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-69.png)
_Configurer la machine virtuelle._

L'assistant sélectionnera automatiquement les paramètres par défaut en fonction du type et de la version du système d'exploitation que vous avez sélectionnés. Vous pouvez toujours modifier les paramètres au fur et à mesure que vous passez par l'assistant. Il suffit de continuer à cliquer sur "Continuer" et "Créer" jusqu'à ce que vous ayez terminé l'assistant. Il est généralement acceptable d'utiliser les paramètres par défaut.

Ensuite, démarrez la machine virtuelle que vous venez de créer en cliquant sur "Démarrer".

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-71.png)
_Démarrer la machine virtuelle._

Une fois la machine virtuelle démarrée, sélectionnez le fichier image .iso que vous souhaitez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-72.png)
_Installer le système d'exploitation sur la machine virtuelle._

Votre machine virtuelle va maintenant charger le système d'exploitation sélectionné. Le système d'exploitation peut nécessiter une configuration, mais ce sera la même configuration que celle requise si vous l'aviez installé sur un ordinateur standard. 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-73.png)
_Windows 10 s'exécute avec succès dans une machine virtuelle._

Félicitations ! Vous avez exécuté votre première machine virtuelle dans VirtualBox.