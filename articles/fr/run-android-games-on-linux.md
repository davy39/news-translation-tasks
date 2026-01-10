---
title: Comment exécuter des jeux Android sur Linux avec Android-x86
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-08-17T16:09:12.000Z'
originalURL: https://freecodecamp.org/news/run-android-games-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/jose-article-photo.jpeg
tags:
- name: Android
  slug: android
- name: Games
  slug: games
- name: Linux
  slug: linux
- name: virtual machine
  slug: virtual-machine
seo_title: Comment exécuter des jeux Android sur Linux avec Android-x86
seo_desc: 'In this article, you''ll learn how you can use virtual machines on Linux
  while having fun with vintage games.

  If you have an Android phone, one of your guilty pleasures might be playing some
  very entertaining games. Or it could be that there is an app...'
---

Dans cet article, vous apprendrez comment utiliser des machines virtuelles sur Linux tout en vous amusant avec des jeux vintage.

Si vous avez un téléphone Android, l'un de vos plaisirs coupables pourrait être de jouer à des jeux très divertissants. Ou il pourrait y avoir une application qui ne fonctionne que sur votre téléphone.

Et puis vous pensez – et si vous pouviez exécuter les mêmes jeux sur votre PC de bureau ?

Pour simplifier le scénario, supposons que les applications fonctionnent sur Android.

Une approche pour résoudre votre problème est d'exécuter un émulateur Android sur votre PC. Mais certains d'entre eux, comme [Android-x86](https://www.android-x86.org/download.html), nécessitent de redémarrer votre machine pour qu'ils puissent prendre le contrôle du matériel.

Si vous ne craignez pas une petite perte de performance, vous pouvez exécuter une machine virtuelle en même temps que votre système d'exploitation natif. Plus précisément sur Linux, il existe plusieurs choix, comme [QEMU](https://www.qemu.org/) et [VirtualBox](https://www.virtualbox.org/), pour n'en nommer que quelques-uns.

À la fin de cet article, vous serez en mesure de faire ce qui suit :

* Installer VirtualBox sur Fedora Linux

* Exécuter android-x86 et terminer la configuration de base

* Installer une application depuis le Google Play Store, comme sur votre téléphone.

## **Configuration de base**

Avant de commencer, je suppose que vous avez ce qui suit :

* La capacité d'exécuter des commandes en tant que superutilisateur (comme [SUDO](https://www.sudo.ws/))

* Un compte sur Google.com, afin que vous puissiez utiliser le Play Store depuis la machine virtuelle.

# **Comment installer VirtualBox**

La première étape consiste à installer VirtualBox. À des fins pratiques, notre installation sera basique, juste assez pour exécuter nos jeux :

```python
sudo dnf install -y kernel-devel kernel-devel-5.14.18-100.fc33.x86_64
curl --remote-name --location https://www.virtualbox.org/download/oracle_vbox.asc
sudo rpm --import ./oracle_vbox.asc
sudo dnf install -y https://download.virtualbox.org/virtualbox/6.1.36/VirtualBox-6.1-6.1.36_152435_fedora33-1.x86_64.rpm
sudo dnf install -y virtualbox-guest-additions.x86_64
sudo /sbin/vboxconfig
```

## **Comment installer l'ISO Android-x86**

La première étape consiste à télécharger l'image ISO depuis [Android-x86](https://sourceforge.net/projects/android-x86/). Cette ISO contient le système d'exploitation Android qui sera installé sur notre disque dur virtuel.

Après cela, nous pouvons configurer notre machine virtuelle comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/virtualbox-androidx86.png align="left")

*À quoi ressemble une machine virtuelle terminée sur VirtualBox*

![Image](http://localhost:63342/4f800f8a-bbed-4dd8-b03c-00449c9f6698/1437651526/fileSchemeResource/59ea74abf47f101ded05f883e4d4c256-virtualbox-androidx86.png?_ijt=r1jlidvb50q7p9rgbjri12egof align="left")

Quelques points à noter :

* Après le premier démarrage, j'ai constaté que 1 Go pour l'image Android n'était pas suffisant. Les performances se sont considérablement améliorées après avoir augmenté la RAM à 3 Go.

* Un autre changement concernait le 'Contrôleur graphique'. À l'origine, c'était VMSVGA, mais Android refusait de démarrer en mode graphique, alors j'ai basculé vers VboxVGA et cela a fonctionné.

* 2 CPU et 8 Go d'espace disque étaient suffisants pour mon jeu.

* Enfin, j'ai spécifié que le contrôleur IDE était l'ISO android-x86.

Pour démarrer la machine virtuelle, vous cliquez sur le bouton 'Démarrer' dans l'interface graphique, puis vous devrez prendre quelques décisions comme la partition amorçable :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-partition.png align="left")

*Partitionnement de votre disque virtuel. Nous attribuons 8 Go et nous assurons que la partition peut démarrer*

Une fois cela fait, vous pouvez choisir votre nouvelle partition pour effectuer l'installation :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-newpartition.png align="left")

*Après la création de la nouvelle partition, vous pouvez la choisir et y installer le système d'exploitation Android*

Ensuite, l'installation se poursuivra :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-install.png align="left")

*L'installateur copie les fichiers de l'image ISO Android vers le disque dur virtuel*

Une fois l'installation terminée, vous pouvez éteindre la machine virtuelle.

## **Premier démarrage**

Maintenant, vous devrez aller dans les options avancées et sélectionner le disque virtuel (au lieu de l'image ISO) pour démarrer :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/android-x86-boot-from-disk.png align="left")

*Vous pouvez soit démarrer depuis le disque dans ce menu, soit changer l'ordre de démarrage sur la machine virtuelle*

Après cela, Android vous demandera quelques informations de configuration de base, comme il le fait sur votre téléphone. Le résultat final peut ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-running.png align="left")

*La machine virtuelle ressemble exactement à votre téléphone Android.*

## **Comment installer des jeux depuis le Google Play Store**

Dans mon cas, j'ai décidé d'installer un jeu où je peux combattre les forces du mal en tant que [Mazinger Z/ Tranzor Z](https://en.wikipedia.org/wiki/Mazinger_Z) des années 1970 (Oui, j'adore [Go Nagai](https://en.wikipedia.org/wiki/Go_Nagai) Mazinger Z). Pour ce faire, recherchez sur le Play Store et installez le jeu :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/android-x86-play-store.png align="left")

*Après que Android est en cours d'exécution et que vos identifiants sont configurés, vous pouvez télécharger et installer n'importe quel programme Android que vous souhaitez.*

Et maintenant, succès ! Nous avons le jeu en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/androidx86-mazingerz.png align="left")

*Désolé, mais maintenant il est temps de jouer en tant que Mazinger Z !*

# **Qu'avons-nous appris ici ?**

* Nous avons réussi à installer un moteur de machine virtuelle et à exécuter le système d'exploitation Android ainsi que notre système Fedora habituel

* Vous avez vu comment vous pouvez essayer et abandonner la configuration de systèmes d'exploitation entiers, sans avoir à passer par la difficulté de configurer un système de démarrage dual avec Grub sur Linux

Une autre fonctionnalité intéressante de l'exécution du jeu à l'intérieur d'une machine virtuelle est que vous pouvez geler complètement le jeu, puis revenir et le restaurer exactement au même point où vous l'avez laissé.

Enfin, vous pouvez faire beaucoup plus de choses avec une machine virtuelle que simplement exécuter des jeux, par exemple :

* Vous pouvez [analyser des logiciels malveillants en toute sécurité](https://www.varonis.com/blog/malware-analysis-tools), exécuter des applications non fiables et contenir tout dommage qu'elles peuvent causer.

* Essayer une nouvelle version de système d'exploitation avant de décider de faire une installation propre (ce n'est pas un gros problème de nos jours, car la plupart d'entre eux fournissent un CD live que vous pouvez démarrer pour essayer), mais cela reste très pratique.

* Pouvoir exécuter plusieurs systèmes d'exploitation simultanément, sans redémarrer votre machine. Vous commencerez probablement à essayer des options plus avancées de votre machine virtuelle de choix, comme [VirtualBox](https://www.virtualbox.org/manual/ch09.html).

Jouer à des jeux sur votre PC est une porte d'entrée pour apprendre des choses plus complexes plus tard. De plus, le facteur amusement est indéniable. Amusez-vous !