---
title: Comment configurer les interfaces réseau sous Linux
subtitle: ''
author: Eti Ijeoma
co_authors: []
series: null
date: '2025-06-16T21:52:38.019Z'
originalURL: https://freecodecamp.org/news/configure-network-interfaces-in-linux
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750110739161/ebf2347c-ac63-4fab-ad2f-5d9229e77eaa.png
tags:
- name: networking
  slug: networking
- name: Linux
  slug: linux
seo_title: Comment configurer les interfaces réseau sous Linux
seo_desc: Networking is an essential part of any Linux system. Proper networking allows
  communication between devices and the internet. Understanding the network interface
  is vital when setting up servers, solving connectivity issues, and managing device
  traff...
---

La mise en réseau est une partie essentielle de tout système Linux. Une mise en réseau appropriée permet la communication entre les appareils et Internet. Comprendre l'interface réseau est vital lors de la configuration des serveurs, de la résolution des problèmes de connectivité et de la gestion du flux de trafic des appareils.

Un problème courant rencontré en matière de mise en réseau est la perte de connectivité après la modification des paramètres réseau, ce qui entraîne l'impossibilité d'accéder au système. Cela se produit généralement en raison d'une adresse IP mal configurée, de paramètres incorrects et d'une mauvaise compréhension des configurations des interfaces réseau.

Dans cet article, nous vous guiderons à travers la compréhension de ces configurations d'interfaces réseau, la configuration et la gestion des interfaces réseau sous Linux, la vérification des interfaces disponibles, la configuration des adresses IP statiques et dynamiques, et les meilleures pratiques à considérer lors de la configuration des interfaces réseau. À la fin de cet article, vous aurez une base solide en matière d'interfaces réseau.

## Table des matières

* [Qu'est-ce que les interfaces réseau ?](#heading-quest-ce-que-les-interfaces-reseau)
    
* [Types d'interfaces réseau sous Linux](#heading-types-dinterfaces-reseau-sous-linux)
    
* [Pourquoi les interfaces réseau sont importantes](#heading-pourquoi-les-interfaces-reseau-sont-importantes)
    
* [Comment lister les interfaces réseau sous Linux](#heading-comment-lister-les-interfaces-reseau-sous-linux)
    
* [Comment configurer les interfaces réseau sous Linux](#heading-comment-configurer-les-interfaces-reseau-sous-linux)
    
* [Comment configurer un pont réseau sous Linux](#heading-comment-configurer-un-pont-reseau-sous-linux)
    
* [Meilleures pratiques pour configurer les interfaces réseau sous Linux](#heading-meilleures-pratiques-pour-configurer-les-interfaces-reseau-sous-linux)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que les interfaces réseau ?

Une interface réseau est un point de connexion au sein du système Linux qui permet la communication avec d'autres appareils au sein du réseau. C'est ainsi que le noyau Linux relie le côté logiciel du réseau au côté matériel. Les systèmes Linux fournissent de nombreuses interfaces réseau qui aident à faciliter la communication entre le système et d'autres réseaux externes.

Les interfaces réseau Linux sont essentielles pour le dépannage, la configuration, la gestion et l'optimisation des tâches de mise en réseau. Comprendre ce qu'elles sont et comment elles fonctionnent vous permet d'optimiser la mise en réseau et la sécurité de votre serveur.

## Types d'interfaces réseau sous Linux

Les interfaces réseau peuvent être classées en deux catégories principales : les interfaces réseau physiques et virtuelles.

### Interfaces réseau physiques

Les adaptateurs réseau physiques sont les composants matériels de l'interface réseau qui connectent le système à un réseau physique. Ces réseaux physiques incluent le Wi-Fi et l'Ethernet. Ces adaptateurs, communément appelés cartes d'interface réseau (NIC), peuvent être identifiés par leurs noms d'appareils, tels que wlan0 et eth0. Ils incluent les éléments suivants :

1. **Interface Ethernet (eth0, eth1, etc.)**
    
    L'interface Ethernet est utilisée pour les connexions filaires via une carte Ethernet et aide à configurer la mise en réseau haut débit. Elle peut être utilisée dans les centres de données et les serveurs.
    
2. **Interface Wi-Fi (wlan0, wlan1, etc.)**
    
    Cela représente un adaptateur réseau sans fil, et il permet la connectivité sans fil via les réseaux Wi-Fi aux serveurs.
    

### Interfaces réseau virtuelles

Les interfaces réseau virtuelles sont des interfaces basées sur des logiciels gérées par le système d'exploitation Linux. Elles intègrent des technologies de virtualisation réseau comme Docker ou KVM. Il existe plusieurs interfaces réseau virtuelles, et les plus courantes incluent :

* **Interface de boucle locale** : Il s'agit d'une interface spéciale qui permet à un système de communiquer en interne. Elle est définitivement assignée à l'adresse IP 127.0.0.1, appelée [localhost](http://localhost).
    
* **Interface de pont** : Elles sont utilisées pour connecter plusieurs interfaces réseau. Elles sont utiles pour les environnements de virtualisation (par exemple, Linux KVM, mise en réseau Docker).
    
* **Interface de tunnel** : Elle est utilisée pour les VPN et les tunnels réseau. Elle aide à faciliter le passage du trafic réseau chiffré.
    

## Pourquoi les interfaces réseau sont importantes

Les interfaces réseau constituent un composant essentiel d'un système Linux. Elles permettent la communication entre les appareils et Internet, et la configuration appropriée de ces interfaces offre les avantages suivants :

**Connectivité transparente** : Les interfaces réseau permettent aux appareils de communiquer sur les réseaux locaux et Internet, permettant un échange de données approprié entre les serveurs et les réseaux.

**Gestion appropriée du réseau** : Les administrateurs peuvent configurer les interfaces réseau en créant, gérant et assignant des IP statiques ou dynamiques et en optimisant le flux de trafic.

**Sécurité améliorée** : Les administrateurs peuvent configurer les interfaces réseau avec des pare-feu et des VPN pour sécuriser les données et prévenir les accès non autorisés.

**Elle offre un support pour la virtualisation et la conteneurisation** : Les interfaces réseau virtuelles assurent une communication appropriée entre les machines virtuelles, les conteneurs Docker et d'autres serveurs physiques. Cela les rend essentielles pour la création et la gestion des environnements DevOps.

## Comment lister les interfaces réseau sous Linux

Vous pouvez vérifier les interfaces réseau disponibles dans l'environnement Linux en utilisant les commandes suivantes.

1. **En utilisant la commande** `ip` **:**
    
    Pour lister toutes les interfaces réseau et leur statut, vous pouvez utiliser la commande `ip link show`. Elle affiche des détails sur les interfaces réseau, comme le nom, le statut et l'adresse MAC.
    
2. **En utilisant la commande** `ifconfig`
    
    Pour lister toutes les interfaces réseau, utilisez cette commande : `ifconfig -a`. La commande affiche également des détails sur les interfaces réseau et leur état actuel.
    
3. **En utilisant** [`nmcli`](https://networkmanager.dev/docs/api/latest/nmcli.html) **pour les systèmes contrôlés par NetworkManager**
    
    Pour vérifier le statut de toutes les interfaces réseau gérées par NetworkManager, exécutez :
    
    `nmcli device status`.
    
4. **En utilisant le répertoire** `/sys/class/net/`
    
    Pour lister toutes les interfaces réseau, exécutez `ls /sys/class/net/`. Cette commande est utile pour les scripts et l'automatisation car elle fournit un moyen fiable de vérifier les interfaces disponibles de manière programmatique.
    

## Comment configurer les interfaces réseau sous Linux

La configuration des interfaces réseau est essentielle pour gérer les serveurs et les postes de travail Linux. Comprendre cette configuration vous aidera à garantir une connectivité fluide au sein de vos systèmes. Cette section vous donnera les informations correctes sur la configuration des interfaces réseau.

### Assigner une adresse IP statique

Une adresse IP statique garantit que l'appareil conserve la même IP après chaque redémarrage. Cela est particulièrement utile pour les serveurs et les appareils qui ont besoin d'une adressage cohérent. Pour assigner une adresse IP statique, l'interface de ligne de commande NetworkManager (**nmcli**) fournit un utilitaire en ligne de commande pour configurer l'interface réseau comme montré ci-dessous.

```bash
nmcli connection modify eth0 ipv4.addresses 192.168.1.100/24   # définir une adresse IPv4 statique et un masque de sous-réseau

nmcli connection modify eth0 ipv4.gateway 192.168.1.1          # définir la passerelle par défaut

nmcli connection modify eth0 ipv4.dns "8.8.8.8 8.8.4.4"        # configurer les serveurs DNS primaire et secondaire

nmcli connection modify eth0 ipv4.method manual                # basculer l'interface du mode DHCP au mode manuel

nmcli connection up eth0                                       # redémarrer l'interface pour appliquer les modifications
```

Ces commandes définissent une IP fixe, une passerelle et un DNS sur eth0, basculent l'interface en mode manuel et la redémarrent pour que les nouveaux paramètres prennent effet. Les paramètres persistent après les redémarrages car ils sont stockés par `NetworkManager`.

### Assigner une adresse IP temporaire

La commande `ip` vous permet de configurer les interfaces de manière dynamique (non persistante après les redémarrages) :

```bash
ip addr add 192.168.1.100/24 dev eth0     # assigner 192.168.1.100/24 à l'interface eth0 (temporaire)

ip route add default via 192.168.1.1      # définir la passerelle par défaut à 192.168.1.1
```

Ces deux commandes donnent à eth0 l'IP `192.168.1.100/24` et pointent tout le trafic sortant vers la passerelle `192.168.1.1`. Les paramètres durent uniquement jusqu'au prochain redémarrage ou à la réinitialisation de l'interface.

### Assigner une adresse IP avec ifconfig (obsolète)

Les anciens systèmes utilisent encore `ifconfig` et `route`. Ces commandes sont également temporaires.

```bash
ifconfig eth0 192.168.1.100 netmask 255.255.255.0 up  # assigner 192.168.1.100/24 à eth0 et l'activer

route add default gw 192.168.1.1 eth0                # définir la passerelle par défaut à 192.168.1.1 via eth0
```

> **Remarque :** Préférez `ip` ou `nmcli` sur les systèmes modernes.

### Activer DHCP avec nmcli

Une adresse assignée par DHCP permet au réseau de distribuer automatiquement une adresse IP.

```bash
nmcli connection modify eth0 ipv4.method auto   # basculer eth0 pour utiliser DHCP pour l'adressage automatique

nmcli connection up eth0                        # redémarrer la connexion pour que le nouveau paramètre DHCP prenne effet
```

Pour renouveler ou demander un bail directement :

```bash
dhclient eth0   # demander ou renouveler manuellement une adresse IP via DHCP sur l'interface eth0
```

Ces commandes définissent eth0 pour utiliser DHCP, redémarrent le lien pour que le changement prenne effet et (facultativement) déclenchent un renouvellement instantané du bail.

### Assigner plusieurs adresses IP à une seule interface

Une interface réseau peut avoir plusieurs adresses assignées, ce qui la rend applicable pour héberger plusieurs services sur une seule interface.

**En utilisant la commande IP (assignation temporaire)**

```bash
ip addr add 192.168.1.101/24 dev eth0   # ajouter une adresse IPv4 supplémentaire à eth0 (temporaire)

ip addr add 2001:db8::1/64 dev eth0     # ajouter une adresse IPv6 à eth0 (temporaire)
```

Ces deux commandes attachent une adresse IPv4 supplémentaire et une adresse IPv6 à eth0 jusqu'à la réinitialisation de l'interface ou le redémarrage du système.

**Configuration persistante (Netplan)**

Modifiez le fichier `/etc/netplan/01-netcfg.yaml` :

```bash
network:

  version: 2

  renderer: networkd

  ethernets:

    eth0:

      addresses:

        - 192.168.1.100/24

        - 192.168.1.101/24

        - 2001:db8::1/64
```

Après avoir modifié le fichier, exécutez `sudo netplan apply` pour que les adresses supplémentaires soient conservées après les redémarrages.

## Comment configurer un pont réseau sous Linux

Un pont réseau permet à plusieurs interfaces d'agir comme un seul segment de réseau, ce qui est utile dans la virtualisation (KVM, Docker).

**En utilisant** `brctl` **(package bridge-utils)**

```bash
brctl addbr br0                       # créer une nouvelle interface de pont nommée br0

brctl addif br0 eth0                  # ajouter l'interface physique eth0 au pont

ip addr add 192.168.1.100/24 dev br0  # assigner une adresse IP au pont, et non à eth0

ip link set br0 up                    # activer l'interface de pont
```

Ces commandes créent le pont br0, attachent eth0 à celui-ci, donnent au pont sa propre IP et l'activent.

####   
**En utilisant nmcli (pour les systèmes gérés par NetworkManager)**

```bash
nmcli connection add type bridge ifname br0                       # créer un nouveau pont nommé br0

nmcli connection modify br0 bridge.stp no                         # désactiver le protocole Spanning Tree

nmcli connection add type bridge-slave ifname eth0 master br0     # attacher l'interface physique eth0 à br0

nmcli connection up br0                                           # activer le pont pour que les paramètres prennent effet
```

Cette séquence construit le même pont via NetworkManager, désactive le [STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol) pour une convergence plus rapide, lie eth0 en tant qu'esclave et active le pont pour que les invités puissent atteindre le réseau.

## Meilleures pratiques pour configurer les interfaces réseau sous Linux

### **Rendre vos configurations persistantes**

L'une des erreurs que commettent les ingénieurs réseau dans la mise en réseau Linux est de faire des modifications qui ne persistent pas après un redémarrage. Bien que certaines commandes puissent modifier les paramètres réseau de manière temporaire, elles ne sauvegardent pas ces modifications de manière permanente.

Pour garantir que ces paramètres réseau survivent aux redémarrages du serveur, modifiez les fichiers de configuration du système tels que `/etc/network/interfaces`. Une fois que vous avez assuré que toutes les modifications sont persistantes, il n'y aura pas de perturbations inattendues lors du redémarrage du système.

### **Assigner des IP statiques pour les serveurs**

Les adresses IP statiques sont les meilleures pour les serveurs et les infrastructures critiques. Contrairement aux adresses DHCP, qui peuvent changer avec le temps, les adresses IP statiques sont plus stables et fiables. Pour des services comme l'hébergement web et la gestion de bases de données, les IP statiques jouent un rôle clé, car les adresses IP n'ont pas besoin de changer.

### **Sécuriser vos interfaces réseau**

Les interfaces réseau sont les points d'entrée dans un système, donc si elles sont mal configurées, elles pourraient poser un risque de sécurité considérable. Pour réduire les attaques, les administrateurs doivent désactiver toutes les interfaces réseau inutilisées en modifiant le fichier de configuration pour empêcher l'activation automatique. De plus, vous devriez utiliser des outils de pare-feu pour contrôler le trafic qui tente d'atteindre le système.

### **Surveiller vos interfaces réseau**

En tant qu'administrateur système, la surveillance des interfaces réseau aide à prévenir les temps d'arrêt et à garantir une fiabilité appropriée du réseau. Vous pouvez vérifier le statut de vos interfaces réseau en exécutant des commandes comme `link show` ou `if-config -a`. Vous pouvez également les surveiller en temps réel en utilisant des outils comme Netstat. La surveillance de vos systèmes garantit que les problèmes de réseau sont détectés suffisamment tôt, réduisant les temps d'arrêt et améliorant la stabilité du réseau.

### **Mettre à jour constamment les packages réseau**

Vous devez constamment mettre à jour les outils et les pilotes de gestion réseau car cela aide à implémenter les correctifs de sécurité et autres améliorations de performance, car les packages réseau obsolètes peuvent causer des vulnérabilités de sécurité. Il existe des packages spécifiques liés au réseau tels que `network-manager`, `bridge-utils` et `iproute2`.

## Conclusion

La configuration des interfaces réseau sous Linux est une compétence fondamentale que tout administrateur système devrait maîtriser. Que ce soit pour configurer des adresses IP statiques ou activer le DHCP, la compréhension de ces concepts garantira que vos systèmes sont stables et disposent d'une connectivité appropriée. La mise en œuvre des meilleures pratiques comme la surveillance du trafic et la sécurisation de l'interface réseau vous donne les meilleurs résultats. Alors que vous continuez à travailler avec Linux, vous pouvez expérimenter différentes configurations pour approfondir votre compréhension des interfaces réseau.