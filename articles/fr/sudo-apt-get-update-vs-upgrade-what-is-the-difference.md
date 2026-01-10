---
title: sudo apt-get update vs upgrade – Quelle est la différence ?
date: '2022-05-02T19:30:12.000Z'
author: Kristofer Koishigawa
authorURL: https://www.freecodecamp.org/news/author/scissorsneedfoodtoo/
originalURL: https://freecodecamp.org/news/sudo-apt-get-update-vs-upgrade-what-is-the-difference
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/gabriel-heinzer-4Mw7nkQDByk-unsplash.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_desc: 'sudo apt-get update and sudo apt-get upgrade are two commands you can use
  to keep all of your packages up to date in Debian or a Debian-based Linux distribution.

  They''re common commands for Linux admins and people doing DevOps, but are handy
  to know ...'
---


`sudo apt-get update` et `sudo apt-get upgrade` sont deux commandes que vous pouvez utiliser pour maintenir tous vos paquets à jour sous Debian ou une distribution Linux basée sur Debian.

<!-- more -->

Ce sont des commandes courantes pour les administrateurs Linux et les personnes travaillant dans le DevOps, mais elles sont utiles à connaître même si vous n'utilisez pas souvent la ligne de commande.

Dans cet article, je vais détailler ce que font ces deux commandes, comment les utiliser et répondre à quelques questions fréquemment posées.

## Quelles sont les différences entre `sudo apt-get update` et `sudo apt-get upgrade` ?

La principale différence est que `sudo apt-get update` récupère la dernière version de la liste des paquets depuis les dépôts logiciels de votre distribution, ainsi que tous les dépôts tiers que vous auriez pu configurer. En d'autres termes, elle détermine quelle est la dernière version de chaque paquet et dépendance, mais elle ne téléchargera ni n'installera aucune de ces mises à jour.

La commande `sudo apt-get upgrade` télécharge et installe les mises à jour pour chaque paquet et dépendance obsolète sur votre système. Cependant, le simple fait de lancer `sudo apt-get upgrade` ne mettra pas automatiquement les paquets à jour – vous aurez toujours la possibilité de passer en revue les changements et de confirmer que vous souhaitez effectuer les mises à jour.

## Comment utiliser la commande `sudo apt-get update`

Dans votre distribution Linux basée sur Debian (Debian, Ubuntu, Linux Mint, Kali Linux, Raspberry Pi OS, etc.), ouvrez une fenêtre de terminal.

Selon votre distribution, le terminal peut porter des noms différents selon la manière dont vous l'ouvrez. Par exemple, dans Ubuntu et Linux Mint, le terminal par défaut est Gnome Terminal, mais il peut être listé sous "Terminal" dans le menu des applications.

Dans le terminal, saisissez `sudo apt-get update` dans la ligne de commande, entrez votre mot de passe administrateur et appuyez sur la touche Entrée.

S'il y a des mises à jour, vous verrez une sortie similaire à celle-ci :

```
kris@pihole:~ $ sudo apt-get update
Hit:1 https://ftp.harukasan.org/raspbian/raspbian bullseye InRelease
Get:2 https://download.docker.com/linux/raspbian bullseye InRelease [26.7 kB]
Get:3 http://archive.raspberrypi.org/debian bullseye InRelease [23.7 kB]       
Get:4 http://packages.azlux.fr/debian buster InRelease [3,989 B]               
Get:5 http://archive.raspberrypi.org/debian bullseye/main armhf Packages [282 kB]
Get:6 http://packages.azlux.fr/debian buster/main armhf Packages [3,418 B]
Fetched 340 kB in 4s (94.8 kB/s)     
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
3 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

Si vous voulez voir quels paquets peuvent être mis à jour, lancez `apt list --upgradable` :

```
kris@pihole:~ $ apt list --upgradable
Listing... Done
libcamera0/stable 0~git20220426+18e68a9b-1 armhf [upgradable from: 0~git20220303+e68e0f1e-1]
raspi-config/stable 20220425 all [upgradable from: 20220419]
rpi-eeprom/stable 13.13-1 armhf [upgradable from: 13.12-1]
```

Mais s'il n'y a pas de nouvelles versions de paquets ou de dépendances dans le dépôt logiciel de votre distribution, vous verrez une sortie comme celle-ci :

```
kris@pihole:~ $ sudo apt-get update
Get:1 https://download.docker.com/linux/raspbian bullseye InRelease [26.7 kB]
Hit:2 https://ftp.harukasan.org/raspbian/raspbian bullseye InRelease           
Hit:3 http://packages.azlux.fr/debian buster InRelease                         
Hit:4 http://archive.raspberrypi.org/debian bullseye InRelease
Fetched 26.7 kB in 3s (8,789 B/s)
Reading package lists... Done
```

Remarquez qu'il n'est pas fait mention de paquets pouvant être mis à jour, ni de note concernant l'exécution de `apt list --upgradable`.

Cela ne signifie pas nécessairement qu'il n'y a pas de logiciels obsolètes sur votre système, mais simplement que vous avez déjà récupéré la dernière version de la liste des paquets. Vous avez peut-être lancé `sudo apt-get update` plusieurs fois.

Vous pouvez toujours relancer `apt list --upgradable` pour voir si quelque chose peut être mis à jour.

Ou vous pouvez utiliser la commande plus moderne `sudo apt update` à la place. Cette commande vous indiquera toujours le nombre de paquets pouvant être mis à jour, ou une note indiquant que tout est à jour.

Pour plus d'informations sur les différences entre `apt` et `apt-get`, [consultez cette section ci-dessous][1].

## Comment utiliser la commande `sudo apt-get upgrade`

Après avoir exécuté la commande `sudo apt-get update`, dans la même fenêtre de terminal, tapez `sudo apt-get upgrade`, entrez votre mot de passe si nécessaire, et appuyez sur Entrée.

Ensuite, vous verrez une sortie similaire à celle-ci :

```
kris@pihole:~ $ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2,616 kB of archives.
After this operation, 1,596 kB of additional disk space will be used.
Do you want to continue? [Y/n]
```

Vers le bas de la sortie, vous verrez les paquets qui seront mis à jour :

```
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

La quantité de données à récupérer, et la quantité d'espace de stockage que les paquets mis à jour utiliseront une fois installés :

```
Need to get 2,616 kB of archives.
After this operation, 1,596 kB of additional disk space will be used.
```

Et enfin, vous verrez une invite vous demandant si vous souhaitez poursuivre la mise à jour :

```
Do you want to continue? [Y/n]
```

Vous pouvez entrer `y`, `Y`, ou `yes` pour continuer la mise à jour, ou `n`, `N`, ou `no` pour quitter la commande `upgrade`.

Si vous choisissez de quitter, vous verrez une sortie comme celle-ci :

```
kris@pihole:~ $ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2,616 kB of archives.
After this operation, 1,596 kB of additional disk space will be used.
Do you want to continue? [Y/n] n
Abort.
```

Si vous choisissez de continuer la mise à jour, vous verrez une longue sortie comme celle-ci :

```
kris@pihole:~ $ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2,616 kB of archives.
After this operation, 1,596 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.raspberrypi.org/debian bullseye/main armhf libcamera0 armhf 0~git20220426+18e68a9b-1 [548 kB]
Get:2 http://archive.raspberrypi.org/debian bullseye/main armhf raspi-config all 20220425 [30.3 kB]
Get:3 http://archive.raspberrypi.org/debian bullseye/main armhf rpi-eeprom armhf 13.13-1 [2,037 kB]
Fetched 2,616 kB in 3s (1,019 kB/s)   
Reading changelogs... Done
(Reading database ... 43496 files and directories currently installed.)
Preparing to unpack .../libcamera0_0~git20220426+18e68a9b-1_armhf.deb ...
Unpacking libcamera0:armhf (0~git20220426+18e68a9b-1) over (0~git20220303+e68e0f1e-1) ...
Preparing to unpack .../raspi-config_20220425_all.deb ...
Unpacking raspi-config (20220425) over (20220419) ...
Preparing to unpack .../rpi-eeprom_13.13-1_armhf.deb ...
Unpacking rpi-eeprom (13.13-1) over (13.12-1) ...
Setting up rpi-eeprom (13.13-1) ...
Setting up libcamera0:armhf (0~git20220426+18e68a9b-1) ...
Setting up raspi-config (20220425) ...
Processing triggers for man-db (2.9.4-2) ...
Processing triggers for libc-bin (2.31-13+rpt2+rpi1+deb11u2) ...
```

Et une fois cela terminé, tous les paquets et dépendances obsolètes seront mis à jour.

Une chose importante à retenir à propos de la commande `sudo apt-get upgrade` est qu'elle ne met à jour que ce qu'elle peut sans rien supprimer.

Par exemple, si une mise à jour nécessite une nouvelle dépendance, la commande `upgrade` la téléchargera et l'installera, mais elle ne supprimera pas l'ancienne dépendance. La suppression des anciennes dépendances nécessite une commande différente. Vous verrez souvent cela lors de la mise à jour vers une nouvelle version du noyau (kernel).

Si vous voyez un message similaire à celui-ci après la mise à jour :

```
The following packages were automatically installed and are no longer required:
  g++-8 gir1.2-mutter-4 libapache2-mod-php7.2 libcrystalhd3
Use 'sudo apt autoremove' to remove them.
```

Vous pouvez suivre la suggestion et utiliser `sudo apt autoremove` pour supprimer ces paquets inutiles.

## Comment utiliser des options spéciales avec la commande `sudo apt-get upgrade`

Il existe un certain nombre d'options ou de paramètres spéciaux que vous pouvez utiliser avec la commande `sudo apt-get upgrade`, mais deux se distinguent : `--dry-run` et `--yes`.

### Comment utiliser l'option `--dry-run` :

L'option `--dry-run` (alternativement, `-s` ou `--simulate`) simule ce qui se passerait pendant le processus de mise à jour, mais ne modifie rien concrètement sur votre système :

```
kris@pihole:~ $ sudo apt-get upgrade --dry-run
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Inst libcamera0 [0~git20220303+e68e0f1e-1] (0~git20220426+18e68a9b-1 Raspberry Pi Foundation:stable [armhf])
Inst raspi-config [20220331] (20220425 Raspberry Pi Foundation:stable [all])
Inst rpi-eeprom [13.12-1] (13.13-1 Raspberry Pi Foundation:stable [armhf])
Conf libcamera0 (0~git20220426+18e68a9b-1 Raspberry Pi Foundation:stable [armhf])
Conf raspi-config (20220425 Raspberry Pi Foundation:stable [all])
Conf rpi-eeprom (13.13-1 Raspberry Pi Foundation:stable [armhf])
```

Encore une fois, bien que Debian et les distributions basées sur Debian soient très stables, cette option est utile si vous voulez vous assurer qu'il n'y aura pas de conflits lors d'une mise à jour.

### Comment utiliser l'option `--yes` :

L'option `--yes` (alternativement, `-y` ou `--assume-yes`) répond automatiquement "oui" à toutes les invites si cela est sûr :

```
kris@pihole:~ $ sudo apt-get upgrade --yes
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  libcamera0 raspi-config rpi-eeprom
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2,616 kB of archives.
After this operation, 1,596 kB of additional disk space will be used.
Get:1 http://archive.raspberrypi.org/debian bullseye/main armhf libcamera0 armhf 0~git20220426+18e68a9b-1 [548 kB]
Get:2 http://archive.raspberrypi.org/debian bullseye/main armhf raspi-config all 20220425 [30.3 kB]
Get:3 http://archive.raspberrypi.org/debian bullseye/main armhf rpi-eeprom armhf 13.13-1 [2,037 kB]
...
Processing triggers for libc-bin (2.31-13+rpt2+rpi1+deb11u2) ...
```

Notez que l'étape `Do you want to continue? [Y/n]` est ignorée ci-dessus, et tous les paquets sont mis à jour directement.

## FAQ

### Que sont `sudo` et `apt-get` ?

Une chose importante à noter à propos de `sudo apt-get update` et `sudo apt-get upgrade` est que les deux commandes sont composées de trois parties : `sudo`, `apt-get`, et `update` ou `upgrade`.

`sudo` signifie "superuser do" (le super-utilisateur fait), et vous permet d'exécuter des programmes avec des privilèges root ou administrateur.

Par exemple, redémarrer un système nécessite des privilèges de niveau super-utilisateur/root, donc exécuter `reboot` dans le terminal pourrait renvoyer des erreurs similaires à celle-ci :

```
Failed to set wall message, ignoring: Interactive authentication required.
Failed to reboot system via logind: Interactive authentication required.
Failed to open initctl fifo: Permission denied
Failed to talk to init daemon.
```

Mais si vous lancez `sudo reboot`, puis entrez votre mot de passe administrateur, vous exécuterez la commande `reboot` en tant que super-utilisateur, et votre système redémarrera immédiatement.

`apt-get` est un outil en ligne de commande dans Debian et les distributions Linux basées sur Debian que vous utilisez pour installer et gérer des paquets.

### Quelle est la différence entre `apt-get` et `apt` ?

`apt` est un outil plus moderne pour installer et gérer des applications sur Debian et les distributions basées sur Debian.

Pour la plupart, `apt` et `apt-get` peuvent être utilisés de manière interchangeable – `sudo apt update` et `sudo apt-get update` mettent toutes deux à jour la liste des paquets sur votre système.

Les principales différences que vous remarquerez sont que `apt` est plus facile à taper, sa sortie est généralement plus utile, et il inclut des fonctionnalités conviviales comme une barre de progression lors de l'installation des paquets.

Bien que la plupart des exemples de cet article utilisent `apt-get`, je vous encourage vivement à utiliser `apt` à la place.

### Les commandes `sudo apt-get update` et `sudo apt-get upgrade` sont-elles sûres ?

Oui, Debian et les distributions basées sur Debian sont généralement très stables, et les commandes `update` et `upgrade` sont sûres à utiliser. C'est parce que les mises à jour majeures pour les paquets / dépendances, et les distributions elles-mêmes, ne sont publiées qu'une ou deux fois par an.

L'inconvénient est que, contrairement aux distributions "bleeding edge" comme Arch Linux, si vous voulez utiliser la version la plus récente d'un paquet, vous devrez peut-être faire un effort supplémentaire. Vous pourriez avoir besoin de configurer un dépôt tiers via un PPA, d'utiliser un système de paquets alternatif comme Snap ou Flatpak, ou de compiler le paquet vous-même.

Mais la stabilité qui accompagne des logiciels légèrement plus anciens en vaut la peine, du moins à mon avis.

### Peut-on enchaîner les commandes `sudo apt-get update` et `sudo apt-get upgrade` ?

Vous vous dites peut-être : n'est-ce pas fastidieux de lancer `sudo apt-get update`, d'attendre que ce soit fini, puis de lancer `sudo apt-get upgrade` ?

Bien que `sudo apt-get update` et `sudo apt-get upgrade` s'exécutent assez rapidement, il est parfois plus facile d'exécuter une suite de commandes et de revenir vérifier quelques minutes plus tard.

Avec l'opérateur `&&`, vous pouvez enchaîner plusieurs commandes comme ceci :

```
sudo apt-get update && sudo apt-get upgrade
```

La chose importante à retenir avec l'opérateur `&&` est que la commande après l'opérateur ne s'exécute que si la commande avant elle réussit.

En utilisant l'exemple ci-dessus, `sudo apt-get upgrade` ne s'exécute que si `sudo apt-get update` réussit. S'il y a une erreur, comme un problème de réseau lors de la mise à jour de la liste des paquets, alors `sudo apt-get upgrade` est ignoré.

### Que sont `sudo apt-get dist-upgrade` et `sudo apt full-upgrade`, et sont-elles sûres ?

Selon [ce fil Stack Overflow][2], ces commandes font la même chose sous le capot – elles mettent à jour les paquets obsolètes et suppriment également intelligemment certains paquets lorsque cela est nécessaire.

Essentiellement, elles sont comme la combinaison des commandes `sudo apt-get upgrade` et `sudo apt autoremove`.

L'exécution de ces commandes _devrait_ être sûre dans la plupart des cas.

Mais beaucoup de gens, moi y compris, recommandent d'utiliser plutôt `sudo apt-get update` et `sudo apt-get upgrade`. Vous avez plus de chances de passer en revue les changements à venir, et comme `upgrade` ne supprime jamais de paquets, c'est moins destructeur.

## `./merci_de_votre_lecture.sh`

Si vous avez trouvé cette analyse de `sudo apt-get update` et `sudo apt-get upgrade` utile, n'hésitez pas à la partager avec vos amis pour que plus de personnes puissent en profiter.

Aussi, n'hésitez pas à me contacter sur [Twitter][3] pour me donner votre avis.

[1]: #heading-quelle-est-la-difference-entre-apt-get-et-apt
[2]: https://askubuntu.com/questions/770135/apt-full-upgrade-versus-apt-get-dist-upgrade
[3]: https://twitter.com/kriskoishigawa