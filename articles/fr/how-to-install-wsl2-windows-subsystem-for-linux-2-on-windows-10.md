---
title: Comment installer WSL2 (Windows Subsystem for Linux 2) sur Windows 10
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-16T17:30:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/install-WSL2--2-.png
tags:
- name: Linux
  slug: linux
- name: Windows
  slug: windows
seo_title: Comment installer WSL2 (Windows Subsystem for Linux 2) sur Windows 10
seo_desc: "Linux is a widely used operating system and is quite important for developers.\
  \ \nThere are times when you might need to have both operating systems – Windows\
  \ and Linux – either for work, study, or even just experimentation. \nLuckily, Windows\
  \ provides ..."
---

Linux est un système d'exploitation largement utilisé et assez important pour les développeurs. 

Il arrive que vous ayez besoin des deux systèmes d'exploitation – Windows et Linux – que ce soit pour le travail, les études ou même simplement pour expérimenter. 

Heureusement, Windows fournit un utilitaire pratique pour utiliser Linux aux côtés de Windows. Cet utilitaire s'appelle WSL (Windows Subsystem for Linux). Sa version récente est WSL2 et dans ce guide, nous allons en discuter en détail. 

Nous allons couvrir :

* Qu'est-ce que WSL2 et quels sont ses avantages ?
* Comment installer WSL2 sur Windows 10 avec les paramètres par défaut.
* Comment installer WSL2 avec une distribution Linux spécifique.

## Qu'est-ce que WSL2 ?

Windows Subsystem for Linux fournit une couche de compatibilité qui vous permet d'exécuter des exécutables binaires Linux nativement sur Windows. 

**WSL2 (Windows Subsystem for Linux version 2)** est la dernière version de WSL. L'architecture de WSL2 remplace celle de WSL en utilisant une machine virtuelle légère. Dans la nouvelle version, vous pouvez exécuter un noyau Linux réel, ce qui améliore les performances globales.

### Avantages de l'utilisation de WSL

Il y a plusieurs avantages à utiliser WSL par rapport à une configuration de machine virtuelle traditionnelle :

* La configuration de WSL est simple et ne prend pas beaucoup de temps.
* Il est léger par rapport aux machines virtuelles où vous devez allouer des ressources depuis la machine hôte.
* Vous n'avez pas besoin d'installer d'ISO ou d'image de disque virtuel pour les machines Linux, qui tendent à être des fichiers lourds.
* Vous pouvez utiliser Windows et Linux côte à côte.

## Comment installer WSL2

Tout d'abord, activez l'option `windows subsystem for Linux` dans les paramètres. 

* Allez dans Démarrer. Recherchez "Activer ou désactiver des fonctionnalités Windows".
* Cochez l'option Windows Subsystem for Linux.	

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-42.png)
_Activer ou désactiver des fonctionnalités Windows._

Ensuite, ouvrez votre invite de commande et fournissez les commandes d'installation.

* Ouvrez l'invite de commande en tant qu'administrateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-47.png)

* Exécutez la commande suivante :

```bash
wsl --install
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-31.png)

Note : Par défaut, **Ubuntu** sera installé. Mais vous pouvez installer n'importe quelle distribution de votre choix. Nous verrons comment faire plus tard.

Une fois l'installation terminée, vous devrez redémarrer votre machine Windows. Donc, redémarrez votre machine Windows.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-32.png)

Après le redémarrage, vous pourriez voir une fenêtre comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-43.png)

Une fois l'installation d'Ubuntu terminée, vous serez invité à entrer votre nom d'utilisateur et votre mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-35.png)

Et voilà ! Vous êtes prêt à utiliser Ubuntu.

Lancez Ubuntu en recherchant dans le menu Démarrer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-44.png)

Et voici notre instance Ubuntu lancée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-46.png)
_Ubuntu lancé via WSL2_

## Comment installer une distribution Linux spécifique

Si vous utilisez la méthode par défaut comme montré ci-dessus, Ubuntu sera installé. Vous pouvez trouver la liste des distributions disponibles en exécutant la commande suivante sur l'invite de commande Windows :

```bash
wsl --list --online
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-33.png)
_Liste des distributions Linux disponibles en ligne_

Pour installer une distribution spécifique, utilisez la commande suivante :

```bash
wsl --install -d DISTRO-NAME
```

Par exemple, pour installer Debian, la commande serait modifiée comme suit :

```bash
wsl --install -d Debian
```

Suivez les invites et la distribution spécifique sera installée.

**Astuce** : Vous pouvez également rechercher des mises à jour comme montré ci-dessous :

```bash
wsl --update
```

Vérifiez le statut en lançant Windows PowerShell.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-37.png)
_Vérifier le statut de WSL_

## Conclusion

WSL est un excellent utilitaire pour utiliser Linux sur une machine Windows native. Il offre une opportunité d'apprentissage, surtout pour ceux qui commencent. J'espère que vous avez trouvé cet article utile.

Connectons-nous sur [Twitter](https://twitter.com/hira_zaira) !

Lisez mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Discutons sur [Discord](https://discordapp.com/users/Zaira_H#2603).