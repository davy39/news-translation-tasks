---
title: "Comment utiliser Linux sur une machine Windows \x13 5 approches différentes"
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-06-09T15:03:52.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-use-linux-on-a-windows-machine
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/5-ways-to-use-Linux-on-a-Windows-machine.png
tags:
- name: Linux
  slug: linux
- name: Windows
  slug: windows
- name: WSL
  slug: wsl
seo_title: "Comment utiliser Linux sur une machine Windows \x13 5 approches différentes"
seo_desc: "As a developer, you might need to run both Linux and Windows side by side.\
  \ Luckily, there are a number of ways you can get the best of both worlds without\
  \ getting different computers for each operating system. \nIn this article, we'll\
  \ explore a few wa..."
---

En tant que développeur, vous pourriez avoir besoin d'exécuter à la fois Linux et Windows côte à côte. Heureusement, il existe plusieurs façons d'obtenir le meilleur des deux mondes sans avoir besoin de différents ordinateurs pour chaque système d'exploitation. 

Dans cet article, nous allons explorer quelques façons d'utiliser Linux sur une machine Windows. Certaines d'entre elles sont basées sur le navigateur ou le cloud et ne nécessitent aucune installation préalable pour les utiliser.

Voici les méthodes que nous allons discuter :

* Dual boot
* Windows Subsystem for Linux (WSL)
* Machines virtuelles (VM)
* Solutions basées sur le navigateur
* Solutions basées sur le cloud

## Option 1 : "Dual-boot" Linux + Windows 

Avec le dual boot, vous pouvez installer Linux aux côtés de Windows sur votre ordinateur, ce qui vous permet de choisir quel système d'exploitation utiliser au démarrage. 

Cela nécessite de partitionner votre disque dur et d'installer Linux sur une partition séparée. Avec cette approche, vous ne pouvez utiliser qu'un seul système d'exploitation à la fois.

Si cela vous semble être la bonne solution, [voici un tutoriel utile](https://www.freecodecamp.org/news/how-to-dual-boot-windows-10-and-ubuntu-linux-dual-booting-tutorial/) sur la configuration du dual boot sur Windows 10.

## Option 2 : Utiliser Windows Subsystem for Linux (WSL)

Windows Subsystem for Linux fournit une couche de compatibilité qui vous permet d'exécuter des binaires Linux nativement sur Windows.

L'utilisation de WSL présente certains avantages :

* La configuration de WSL est simple et ne prend pas beaucoup de temps.
* Il est léger par rapport aux machines virtuelles où vous devez allouer des ressources à partir de la machine hôte.
* Vous n'avez pas besoin d'installer d'ISO ou d'image de disque virtuel pour les machines Linux, qui ont tendance à être des fichiers lourds.
* Vous pouvez utiliser Windows et Linux côte à côte.

Si cela vous semble être la bonne option, [voici un guide détaillé](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) sur la façon d'installer et d'utiliser WSL.

## Option 3 : Utiliser une machine virtuelle (VM)

Une machine virtuelle (VM) est une émulation logicielle d'un système informatique physique. Elle vous permet d'exécuter plusieurs systèmes d'exploitation et applications sur une seule machine physique simultanément. Voici une explication détaillée des VM :

Vous pouvez utiliser des logiciels de virtualisation tels qu'Oracle VirtualBox ou VMware pour créer une machine virtuelle exécutant Linux dans votre environnement Windows. Cela vous permet d'exécuter Linux en tant que système d'exploitation invité aux côtés de Windows.

Les logiciels de VM fournissent des options pour allouer et gérer les ressources matérielles pour chaque VM, y compris les cœurs de CPU, la mémoire, l'espace disque et la bande passante réseau. Vous pouvez ajuster ces allocations en fonction des exigences des systèmes d'exploitation invités et des applications.

Voici quelques-unes des options disponibles pour la virtualisation :

* [Oracle VirtualBox](https://www.virtualbox.org/)
* [Multipass](https://multipass.run/)
* [VMware Workstation Player](https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workstation-player.html.html)

## Option 4 : Utiliser une solution basée sur le navigateur

Les solutions basées sur le navigateur sont particulièrement utiles pour des tests rapides, l'apprentissage ou l'accès à des environnements Linux depuis des appareils qui n'ont pas Linux installé.

Vous pouvez utiliser des éditeurs de code en ligne ou des terminaux basés sur le web pour accéder à Linux. Notez que vous n'avez généralement pas de privilèges d'administration complets dans ces cas.

### Éditeurs de code en ligne

Les éditeurs de code en ligne offrent des éditeurs avec des terminaux Linux intégrés. Bien que leur objectif principal soit le codage, vous pouvez également utiliser le terminal Linux pour exécuter des commandes et effectuer des tâches.

[Replit](https://replit.com/) est un exemple d'éditeur de code en ligne, où vous pouvez écrire votre code et accéder au shell Linux en même temps.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/replit.gif)
_Replit fournit un éditeur de code et un shell Linux._

### Terminaux Linux basés sur le web

Les terminaux Linux en ligne vous permettent d'accéder à une interface de ligne de commande Linux directement depuis votre navigateur. Ces terminaux fournissent une interface basée sur le web à un shell Linux, vous permettant d'exécuter des commandes et de travailler avec des utilitaires Linux. 

Un exemple est [JSLinux](https://jslinux.org/). La capture d'écran ci-dessous montre un environnement Linux prêt à l'emploi :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/jslinux.gif)
_Accéder à Linux via JSLinux_

## Option 5 : Utiliser une solution basée sur le cloud

Au lieu d'exécuter Linux directement sur votre machine Windows, vous pouvez envisager d'utiliser des environnements Linux basés sur le cloud ou des serveurs privés virtuels (VPS) pour accéder et travailler avec Linux à distance. 

Des services comme Amazon EC2, Microsoft Azure ou DigitalOcean fournissent des instances Linux auxquelles vous pouvez vous connecter depuis votre ordinateur Windows. Notez que certains de ces services offrent des niveaux gratuits, mais ils ne sont généralement pas gratuits à long terme.

## Comment choisir la bonne méthode

Le choix dépend entièrement de votre cas d'utilisation. Mais il existe certains facteurs qui peuvent vous aider à décider quelle option fonctionne le mieux pour vous. Discutons-en :

* Niveau d'accès/privilèges élevés : Si vous avez besoin de privilèges administratifs complets, il est préférable de sauter les solutions basées sur le navigateur. WSL, le dual boot, les VM et les solutions basées sur le cloud vous offrent un contrôle administratif complet.
* Coût : Les solutions basées sur le cloud offrent des services contre des frais d'abonnement. Ce coût varie en fonction du choix du système d'exploitation, des spécifications matérielles de la machine, du trafic, etc. Si vous avez un budget serré, les solutions basées sur le cloud ne sont peut-être pas les meilleures.
* Évolutivité : Si vous commencez tout juste, mais prévoyez de faire du développement intensif en ressources à l'avenir, vous pouvez toujours augmenter les spécifications physiques de votre machine. Certaines options qui supportent la mise à niveau sont les solutions basées sur le cloud et les VM. Vous pouvez ajouter plus de processeurs ou augmenter la RAM selon vos besoins.
* Spécifications matérielles du système actuel : Si votre système actuel a une RAM et un stockage faibles, l'exécution de VM peut rendre le système lourd. Il serait préférable d'opter pour des solutions basées sur le cloud ou le navigateur.
* Basculer : Si vous ne prévoyez pas d'utiliser Windows et Linux côte à côte, le dual-boot peut être une très bonne option. Il offre une expérience Linux complète et ciblée.

## Ma configuration

J'utilise une VM Ubuntu installée via VMWare Workstation Player. Elle fait un excellent travail car je peux fréquemment basculer entre les deux systèmes d'exploitation. C'était également simple à configurer et je peux profiter des privilèges d'administration également !

![Image](https://www.freecodecamp.org/news/content/images/2023/06/my-set.gif)

## Conclusion

J'espère que vous avez trouvé cet article utile. Quelle est votre chose préférée que vous avez apprise dans ce tutoriel ? J'adorerais me connecter avec vous sur l'une de ces [plateformes](https://zaira_.bio.link/). 

À bientôt dans le prochain tutoriel, bon codage 