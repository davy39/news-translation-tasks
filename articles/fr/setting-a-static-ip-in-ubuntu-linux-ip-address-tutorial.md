---
title: Définir une IP statique dans Ubuntu – Tutoriel sur l'adresse IP Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-03-02T21:24:59.000Z'
originalURL: https://freecodecamp.org/news/setting-a-static-ip-in-ubuntu-linux-ip-address-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/setting-static-ip-ubuntu.png
tags:
- name: computer network
  slug: computer-network
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: Définir une IP statique dans Ubuntu – Tutoriel sur l'adresse IP Linux
seo_desc: "In most network configurations, the router DHCP server assigns the IP address\
  \ dynamically by default. If you want to ensure that your system IP stays the same\
  \ every time, you can force it to use a static IP. \nThat's what we will learn in\
  \ this article..."
---

Dans la plupart des configurations réseau, le serveur DHCP du routeur attribue l'adresse IP de manière dynamique par défaut. Si vous souhaitez vous assurer que l'IP de votre système reste la même à chaque fois, vous pouvez forcer l'utilisation d'une IP statique.

C'est ce que nous allons apprendre dans cet article. Nous explorerons deux méthodes pour définir une IP statique dans Ubuntu.

Les adresses IP statiques sont utilisées dans les situations suivantes :

* Configuration du transfert de port.
* Configuration de votre système en tant que serveur, comme un serveur FTP, un serveur web ou un serveur multimédia.

**Prérequis :**

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Une installation d'Ubuntu, de préférence avec une interface graphique.
* Des droits `sudo`, car nous allons modifier des fichiers de configuration système.

## Comment définir une IP statique en utilisant la ligne de commande

Dans cette section, nous allons explorer toutes les étapes en détail nécessaires pour configurer une IP statique.

### Étape 1 : Lancer le terminal

Vous pouvez lancer le terminal en utilisant le raccourci `Ctrl + Shift + t`.

### Étape 2 : Noter les informations sur le réseau actuel

Nous aurons besoin des détails de notre réseau actuel, tels que l'IP actuellement attribuée, le masque de sous-réseau et le nom de l'adaptateur réseau, afin d'appliquer les modifications nécessaires dans les configurations.

Utilisez la commande suivante pour trouver les détails des adaptateurs disponibles et les informations IP respectives.

```bash
ip a
```

La sortie ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-14.png)

Pour mon réseau, l'adaptateur actuel est `eth0`. Il pourrait être différent pour votre système.

* **Notez le nom de l'adaptateur réseau actuel**

Comme mon adaptateur actuel est `eth0`, les détails suivants sont pertinents.

```bash
6: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:df:c3:ad brd ff:ff:ff:ff:ff:ff
    inet 172.23.199.129/20 brd 172.23.207.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fedf:c3ad/64 scope link
       valid_lft forever preferred_lft forever
```

Il est à noter que l'IP actuelle `172.23.199.129` est attribuée dynamiquement. Elle a `20` bits réservés pour le masque de réseau. L'adresse de diffusion est `172.23.207.255`.

* **Notez le sous-réseau**

Nous pouvons trouver les détails du masque de sous-réseau en utilisant la commande suivante :

```bash
ifconfig -a
```

Sélectionnez la sortie correspondant à votre adaptateur et lisez-la attentivement.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-15.png)
_L'IP est `172.23.199.129` et le masque de sous-réseau est `255.255.240.0`_

En fonction de la classe et du masque de sous-réseau, la plage d'IP hôte utilisable pour mon réseau est : `172.23.192.1 - 172.23.207.254`.

Le sous-réseautage est un sujet vaste. Pour plus d'informations sur le sous-réseautage et vos plages d'IP utilisables, consultez cet [article](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/).

### Étape 3 : Apporter des modifications de configuration

[Netplan](https://netplan.io/) est l'outil de gestion de réseau par défaut pour les dernières versions d'Ubuntu. Les fichiers de configuration pour Netplan sont écrits en utilisant YAML et se terminent par l'extension `.yaml`.

Remarque : Soyez prudent avec les espaces dans le fichier de configuration, car ils font partie de la syntaxe. Sans une indentation correcte, le fichier ne sera pas lu correctement.

* Allez dans le répertoire `netplan` situé à `/etc/netplan`.

Listez le contenu du répertoire `/etc/netplan`.

Si vous ne voyez aucun fichier, vous pouvez en créer un. Le nom peut être n'importe quoi, mais par convention, il devrait commencer par un nombre comme `01-` et se terminer par `.yaml`. Le nombre définit la priorité si vous avez plus d'un fichier de configuration.

Je vais créer un fichier nommé `01-network-manager-all.yaml`.

Ajoutons ces lignes au fichier. Nous allons construire le fichier étape par étape.

```bash
network:
 version: 2
```

Le nœud de premier niveau dans un fichier de configuration Netplan est un mappage `network:` qui contient `version: 2` (ce qui signifie qu'il utilise la version 2 de la définition de réseau).

Ensuite, nous allons ajouter un renderer, qui contrôle le réseau global. Le renderer est `systemd-networkd` par défaut, mais nous allons le définir sur `NetworkManager`.

Maintenant, notre fichier ressemble à ceci :

```bash
network:
 version: 2
 renderer: NetworkManager
```

Ensuite, nous allons ajouter `ethernets` et faire référence au nom de l'adaptateur réseau que nous avons recherché précédemment à l'étape #2. Les autres types de périphériques pris en charge sont `modems:`, `wifis:` ou `bridges:`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
```

Comme nous définissons une IP statique et que nous ne voulons pas attribuer dynamiquement une IP à cet adaptateur réseau, nous allons définir `dhcp4` sur `no`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
```

Maintenant, nous allons spécifier l'IP statique spécifique que nous avons notée à l'étape #2 en fonction de notre sous-réseau et de la plage d'IP utilisable. C'était `172.23.207.254`.

Ensuite, nous allons spécifier la passerelle, qui est le routeur ou le périphérique réseau qui attribue les adresses IP. Le mien est sur `192.168.1.1`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
     addresses: [172.23.207.254/20]
     gateway4: 192.168.1.1
```

Ensuite, nous allons définir `nameservers`. C'est là que vous définissez un serveur DNS ou un second serveur DNS. Ici, la première valeur est `8.8.8.8`, qui est le serveur DNS principal de Google, et la deuxième valeur est `8.8.8.4`, qui est le serveur DNS secondaire de Google. Ces valeurs peuvent varier en fonction de vos besoins.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
     addresses: [172.23.207.254/20]
     gateway4: 192.168.1.1
     nameservers:
         addresses: [8.8.8.8,8.8.8.4]
```

### Étape 4 : Appliquer et tester les modifications

Nous pouvons tester les modifications avant de les appliquer de manière permanente en utilisant cette commande :

```bash
sudo netplan try

```

S'il n'y a pas d'erreurs, il vous demandera si vous souhaitez appliquer ces paramètres.

Maintenant, enfin, testez les modifications avec la commande `ip a` et vous verrez que l'IP statique a été appliquée.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-17.png)
_IP statique appliquée_

## Comment définir une IP statique en utilisant l'interface graphique

Il est très facile de définir une IP statique via l'interface graphique d'Ubuntu. Voici les étapes :

* Recherchez `settings`.
* Cliquez sur l'onglet Network ou Wi-Fi, selon l'interface que vous souhaitez modifier.
* Pour ouvrir les paramètres de l'interface, cliquez sur l'icône d'engrenage à côté du nom de l'interface.
* Sélectionnez "Manuel" dans l'onglet IPV4 et entrez votre adresse IP statique, le masque de réseau et la passerelle.
* Cliquez sur le bouton `Apply`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-16.png)
_Définition manuelle d'une IP statique en utilisant le bureau Ubuntu._

* Vérifiez en utilisant la commande `ip a`

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-18.png)
_IP statique mise à jour via l'interface graphique_

## Conclusion

Dans cet article, nous avons couvert deux méthodes pour définir l'IP statique dans Ubuntu. J'espère que vous avez trouvé l'article utile.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).