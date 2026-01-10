---
title: Comment configurer un VPN domestique en utilisant Tailscale sur un Raspberry
  Pi
subtitle: ''
author: Daniel Anomfueme
co_authors: []
series: null
date: '2025-03-28T15:32:45.025Z'
originalURL: https://freecodecamp.org/news/set-up-a-home-vpn-using-tailscale-on-a-raspberry-pi
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743175949441/1a8c4705-556c-4a1f-899a-9ac8e968fdc3.png
tags:
- name: iot
  slug: iot
- name: Raspberry Pi
  slug: raspberry-pi
- name: vpn
  slug: vpn
- name: networking
  slug: networking
- name: Homelab
  slug: homelab
seo_title: Comment configurer un VPN domestique en utilisant Tailscale sur un Raspberry
  Pi
seo_desc: 'In this article, you’ll learn how to set up a VPN which you can host on
  a Raspberry Pi. I am a fan of Raspberry Pis because these small form factor computers
  are a favourite tool for tinkerers, like me.

  This VPN will allow you to access your home net...'
---

Dans cet article, vous apprendrez à configurer un VPN que vous pouvez héberger sur un Raspberry Pi. Je suis un fan des Raspberry Pi car ces petits ordinateurs de forme compacte sont un outil préféré des bricoleurs, comme moi.

Ce VPN vous permettra d'accéder à votre réseau domestique depuis n'importe où, comme si vous étiez encore chez vous. Pourquoi est-ce utile, pourriez-vous demander ? Eh bien, cela vous permet d'utiliser l'IP de votre réseau domestique, peu importe où vous vous trouvez, ce qui est bon pour la confidentialité.

Dans cet article, nous utiliserons [Tailscale](https://github.com/tailscale/tailscale), un service VPN maillé open-source (Virtual Private Network) qui simplifie la connexion sécurisée des appareils et services à travers différents réseaux. Il permet des connexions chiffrées de point à point en utilisant le protocole open-source [WireGuard](https://www.wireguard.com/). Cela signifie que seuls les appareils sur votre réseau privé peuvent communiquer entre eux.

### Table des matières

* [Prérequis](#heading-prerequis)
    
* [Installer Raspberry Pi OS Lite (32-bit)](#heading-installer-raspberry-pi-os-lite-32-bit)
    
* [Démarrer le Raspberry Pi](#heading-demarrer-le-raspberry-pi)
    
* [Se connecter en SSH au Raspberry Pi et s'identifier](#heading-se-connecter-en-ssh-au-raspberry-pi-et-sidentifier)
    
* [Installer Tailscale sur Raspberry Pi](#heading-installer-tailscale-sur-raspberry-pi)
    
* [Expiration de la clé](#heading-expiration-de-la-cle)
    
* [Configurer le Raspberry Pi comme nœud de sortie](#heading-configurer-le-raspberry-pi-comme-noeud-de-sortie)
    
* [Conclusion](#heading-conclusion)
    

### Prérequis

* Raspberry Pi (je travaille avec un Raspberry Pi 5)
    
* [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
    
* Une carte Micro SD (8 Go suffisent)
    
* Un lecteur de carte Micro SD pour votre ordinateur.
    
* Routeur domestique
    
* Un compte [Tailscale](https://tailscale.com/)
    

## Installer Raspberry Pi OS Lite (32-bit)

Nous allons commencer ce processus en installant le Raspberry Pi OS Lite (32-bit) sur la carte micro SD que nous avons. Nous allons utiliser le logiciel Raspberry Pi Imager qui est disponible gratuitement [ici](https://www.raspberrypi.com/software/).

Lorsque vous exécutez le logiciel d'imagerie, choisissez l'appareil Raspberry Pi, qui pour moi est un Raspberry Pi 5.

Ensuite, dans le système d'exploitation, cliquez sur Raspberry Pi OS (other), puis faites défiler jusqu'à Raspberry Pi OS Lite (32-bit).

Ensuite, sélectionnez votre carte SD que vous avez insérée dans le lecteur de carte, et le lecteur de carte dans l'ordinateur. Votre écran devrait ressembler à ce que vous voyez ci-dessous. Cliquez sur suivant.

![Une capture d'écran du menu de démarrage du logiciel Raspberry Pi Imager.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742929198415/b3cd3476-ed82-4db3-9472-f13df2207ca9.png align="center")

Après avoir cliqué sur suivant, vous devriez voir une fenêtre contextuelle vous demandant si vous souhaitez appliquer les paramètres de personnalisation du système d'exploitation.

![Une capture d'écran du menu d'invite de personnalisation du logiciel Raspberry Pi Imager](https://cdn.hashnode.com/res/hashnode/image/upload/v1742929274780/4482dd16-8f42-41ec-b1cd-af288180adcb.png align="center")

Ensuite, cliquez sur modifier les paramètres. Activez la définition du nom d'hôte et écrivez le nom que vous souhaitez donner au Pi. Pour ce tutoriel, j'utiliserai `dapivpn`*.* Ensuite, activez la définition du nom d'utilisateur et du mot de passe. Choisissez un nom d'utilisateur et un mot de passe fort et sécurisé.

Vous pouvez activer la configuration du LAN sans fil si vous prévoyez d'utiliser le WiFi, mais si vous êtes dans l'équipe câble Ethernet, vous pouvez sauter cette étape. J'utiliserai le WiFi dans ce tutoriel.

Maintenant, vous devrez activer la définition des paramètres locaux et choisir votre fuseau horaire correct et la disposition du clavier.

Après cela, allez dans l'onglet Services, puis activez SSH et cliquez sur "Utiliser l'authentification par mot de passe". Ensuite, cliquez sur sauvegarder, puis sur oui dans l'écran d'application de personnalisation, et encore oui. N'oubliez pas que cela effacera toutes les données sur la carte SD, alors assurez-vous d'utiliser une carte sans fichiers importants.

Voici à quoi devrait ressembler votre Raspberry Pi Imager maintenant :

![Une capture d'écran du logiciel Raspberry Pi Imager effectuant l'opération d'écriture.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742929363470/0c7663d4-a908-4be1-9865-caa665a2ee95.png align="center")

### Démarrer le Raspberry Pi

Une fois cela fait, prenez la carte SD et insérez-la dans votre Raspberry Pi. Ensuite, branchez le câble d'alimentation dans le Raspberry Pi et attendez quelques minutes pour qu'il démarre correctement. Vous saurez qu'il est prêt lorsque la lumière LED verte reste allumée.

Maintenant, vous devriez aller sur votre routeur et définir une IP statique pour le Raspberry Pi. Pour le mien, je l'ai définie sur `192.168.8.21`*.*

### Se connecter en SSH au Raspberry Pi et s'identifier

Ouvrez votre terminal de ligne de commande. Tapez "`ssh <nom d'utilisateur pi>@<adresse_ip_raspberry_pi>`". Pour moi, ce serait :

```bash
ssh danpi@192.168.8.21
```

Ensuite, tapez le mot de passe que vous avez utilisé. Vous devriez voir votre nom d'utilisateur et le nom d'hôte du Pi, ce qui confirme que vous vous êtes connecté avec succès.

![Interface de ligne de commande montrant un processus SSH réussi](https://cdn.hashnode.com/res/hashnode/image/upload/v1743088985613/480325b2-496c-4161-96c6-f150f4020922.png align="center")

Tapez :

```bash
sudo apt update && sudo apt upgrade -y 
```

Vous exécutez cette commande pour vous assurer que tout est à jour localement.

![Interface de ligne de commande montrant la commande de mise à jour en cours d'exécution](https://cdn.hashnode.com/res/hashnode/image/upload/v1742929744252/6200841f-98bb-4bfa-8c30-38159a963e2b.png align="center")

Maintenant, redémarrez votre Pi après cela en tapant :

```bash
sudo reboot
```

## Installer Tailscale sur Raspberry Pi

Maintenant, vous allez ajouter la clé de signature du paquet Tailscale et le dépôt.

```bash
curl -fsSL https://pkgs.tailscale.com/stable/debian/bookworm.noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null 
curl -fsSL https://pkgs.tailscale.com/stable/debian/bookworm.tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list 
```

Installez Tailscale en utilisant ces commandes :

```bash
sudo apt-get update
sudo apt-get install tailscale
```

Ensuite, vous devez connecter votre Pi à votre réseau Tailscale et vous authentifier. Vous pouvez le faire avec la commande suivante :

```bash
sudo tailscale up
```

Votre navigateur devrait ressembler à ceci.

![Capture d'écran du navigateur montrant l'écran d'authentification](https://cdn.hashnode.com/res/hashnode/image/upload/v1742929786462/4d17cfae-0e87-449f-ac13-413a65f3f338.png align="center")

Pour localiser l'adresse IPv4 Tailscale pour le Raspberry Pi, exécutez cette commande :

```bash
tailscale ip -4
```

Vous pouvez également la voir sur le tableau de bord Tailscale dans votre navigateur.

À ce stade, vous avez terminé l'installation de Tailsacle et il ne vous reste plus qu'à faire quelques finitions.

## Expiration de la clé

Il y a une chose que vous devez savoir lorsqu'il s'agit d'ajouter un appareil à Tailsacle. Par défaut, et en tant que fonctionnalité de sécurité, Tailscale exige que les appareils se réauthentifient après qu'une certaine période de temps se soit écoulée, généralement 180 jours.

Si la réauthentification ne se produit pas, les clés expirent et la connexion cesse de fonctionner. C'est à vous de choisir ce que vous préférez, car il s'agit d'une fonctionnalité de sécurité qui comporte certains inconvénients.

Je vais désactiver l'expiration de la clé sur le Raspberry Pi, car je lui fais entièrement confiance. Pour ce faire, vous devez :

* Ouvrir la page [Machines](https://login.tailscale.com/admin/machines) de la console d'administration Tailscale.
    
* Trouver le Raspberry Pi dans la ligne et sélectionner le menu d'options.
    
* Cliquer sur l'option Désactiver l'expiration de la clé. Vous devriez voir une étiquette Expiration Désactivée sous le nom de la machine.
    

## Comment configurer le Raspberry Pi comme nœud de sortie

Une autre chose que vous devez savoir à propos de Tailscale est ce qu'est un nœud de sortie. Un nœud de sortie Tailscale est un appareil désigné dans votre réseau Tailscale qui achemine tout votre trafic internet à travers lui. Peu importe où vous vous trouvez, une fois que vous avez activé cet appareil comme nœud de sortie, lorsque vous activez Tailscale, il achemine votre trafic internet à travers l'appareil.

Idéalement, vous voulez un appareil qui est alimenté 24/7 pour servir de nœud de sortie. C'est pourquoi nous choisissons le Raspberry Pi, car il s'agit d'un ordinateur à faible consommation.

Nous sommes déjà à 90 % du chemin, car nous avons Tailscale en cours d'exécution sur notre Pi. N'oubliez pas d'avoir également Tailscale installé sur autant d'appareils que possible sur votre réseau local. Ce qui reste est de permettre à votre Pi d'agir comme un nœud de sortie, afin que tout votre trafic internet ou LAN soit acheminé à travers lui, vous donnant accès à :

* Les appareils du réseau local à la maison
    
* Votre IP publique à la maison
    
* Les services internes comme le NAS, les imprimantes, les caméras, etc.
    

Pour ce faire, connectez-vous en SSH à votre Raspberry Pi et suivez ces étapes :

* Activer le transfert IP. Le transfert IP permet à votre Raspberry Pi de faire passer le trafic entre ses interfaces réseau. Exécutez les commandes ci-dessous ligne par ligne :
    
    ```bash
    echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
    
    echo "net.ipv6.conf.all.forwarding=1" | sudo tee -a /etc/sysctl.conf
    
    sudo sysctl -p /etc/sysctl.conf
    ```
    
* Annoncer le Raspberry Pi comme nœud de sortie :
    
    ```bash
    sudo tailscale up --advertise-exit-node
    ```
    
* Ouvrir la page [Machines](https://login.tailscale.com/admin/machines) de la console d'administration Tailscale.
    
* Trouver le Raspberry Pi dans la ligne. Vous devriez voir une étiquette Nœud de sortie sur son nom.
    
* Cliquer sur le menu d'options et sélectionner Modifier les paramètres de route.
    
* Cocher la case Utiliser comme nœud de sortie, puis sauvegarder.
    

Maintenant, vous devriez voir l'option d'acheminer l'internet à travers un nœud de sortie lorsque vous ouvrez votre application Tailscale sur mobile ou PC ou partout où vous l'avez installée. Lorsque vous voyez cette option, vous verrez également le Raspberry Pi comme option de nœud de sortie. Vous pouvez également ajouter plus d'appareils comme nœud de sortie si vous voulez plus d'options.

## Conclusion

En utilisant l'application Tailscale sur d'autres appareils, vous pouvez maintenant acheminer le trafic de manière sécurisée à travers le Raspberry Pi en le sélectionnant comme nœud de sortie. Tailscale fournit également des guides clairs, [pas à pas](https://tailscale.com/kb/1408/quick-guide-exit-nodes#use-an-exit-node), adaptés à chaque type d'appareil pour configurer et utiliser un nœud de sortie.

Vous pouvez maintenant être loin de votre internet domestique mais toujours vous connecter à l'internet comme si vous étiez chez vous. À la prochaine fois.