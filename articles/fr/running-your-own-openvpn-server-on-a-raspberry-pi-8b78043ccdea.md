---
title: Comment exécuter votre propre serveur OpenVPN sur un Raspberry PI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T10:14:17.000Z'
originalURL: https://freecodecamp.org/news/running-your-own-openvpn-server-on-a-raspberry-pi-8b78043ccdea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WEXV6clyYAztJhQ97TtYNw.png
tags:
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: vpn
  slug: vpn
seo_title: Comment exécuter votre propre serveur OpenVPN sur un Raspberry PI
seo_desc: 'By Denis Nuțiu


  My Raspberry, serving as an OpenVPN server

  Hello everyone!

  In this short article I will explain how to setup your own VPN (Virtual Private
  Network) server on a Raspberry PI with OpenVPN. After we setup the server, we will
  setup an obf...'
---

Par Denis Nuțiu

![Image](https://cdn-media-1.freecodecamp.org/images/aShx3zgBveeNtJo-SyE1AF5Zs4UquT2lNpR6)
_Mon Raspberry, servant de serveur OpenVPN_

Bonjour à tous !

Dans cet article court, je vais expliquer comment configurer votre propre serveur VPN (Virtual Private Network) sur un Raspberry PI avec OpenVPN. Après avoir configuré le serveur, nous mettrons en place un serveur d'obfuscation afin de déguiser notre trafic, indiquant ainsi que nous utilisons un VPN. Cela nous aidera à contourner certaines formes de censure.

### Pourquoi utiliser un VPN ?

Tout d'abord, parlons des raisons pour lesquelles vous pourriez vouloir utiliser un serveur VPN :

1. Éviter les attaques de type "man in the middle". Si vous avez un utilisateur malveillant sur votre réseau local — même votre colocataire — cette personne est en mesure de surveiller votre trafic non chiffré et de le manipuler.
2. Cacher votre activité internet de votre FAI (Fournisseur d'Accès à Internet) ou de votre Université, dans mon cas.
3. Déblocage de services. Mon Université bloque tous les paquets UDP (User Datagram Protocol). Cela signifie que je ne peux pas utiliser d'application qui communique via UDP. Je ne peux pas utiliser mon client de messagerie, jouer à des jeux, ou même utiliser Git !

J'ai décidé de configurer un VPN sur mon internet domestique en utilisant un Raspberry Pi. De cette façon, je peux me connecter à mon réseau domestique lorsque je suis à l'Université. Si vous avez besoin d'un serveur VPN dans un autre pays, vous pouvez acheter un serveur privé virtuel à 5 $/mois chez [DigitalOcean](https://m.do.co/c/22f012126c25). Vous pouvez utiliser mon lien de parrainage pour obtenir 10 $ de réduction — cela représente deux mois de VPN gratuit. Mais vous n'êtes pas obligé de l'utiliser si vous ne le souhaitez pas.

### Installation d'OpenVPN

Cette étape est vraiment facile, car nous allons utiliser un script shell pour le faire pour vous. Vous n'avez donc qu'à "appuyer" sur suivant et terminer.

L'installation prendra beaucoup de temps, en fonction de la taille de la clé que vous avez choisie. Sur mon Raspberry Pi 3 Model B, cela a pris environ 3 heures.

Veuillez vous rendre sur ce dépôt et suivre les instructions

[**Angristan/OpenVPN-install**](https://github.com/Angristan/OpenVPN-install)  
[_OpenVPN-install - Configurez votre propre serveur OpenVPN sur Debian, Ubuntu, Fedora CentOS, et Arch Linux_github.com](https://github.com/Angristan/OpenVPN-install)

Si vous ne connaissez pas l'adresse IP de votre serveur, mettez simplement `0.0.0.0`. J'ai choisi `443` pour le port et **TCP** (Transmission Control Protocol) pour le protocole.

**Note** : Cela est très important car mon université n'autorise que les ports **TCP/80** et **TCP/443**, le reste est bloqué. De plus, Obfsproxy ne fonctionne qu'avec TCP, alors assurez-vous de choisir **TCP** !

Après que le script ait terminé, vous obtiendrez un fichier **.ovpn**. Il peut être importé dans votre client VPN préféré, et tout devrait fonctionner directement.

#### Tester la connexion

Importez le fichier .ovpn dans votre client VPN et changez l'IP `0.0.0.0` par l'IP locale de votre Raspberry PI. Selon votre configuration réseau, elle peut être de la forme `192.168.*.*`.

_Note : Cela ne fonctionnera que si vous êtes connecté au même WiFi que le Pi._

![Image](https://cdn-media-1.freecodecamp.org/images/RwesiNeDbzJfYs6cuC7KtJ0IWIuHExaale8S)
_Viscosity connecté avec succès à mon serveur VPN._

**J'ai configuré mon routeur pour que le PI obtienne toujours une adresse IP réservée. Vous devrez peut-être vérifier les paramètres de votre routeur si vous souhaitez faire quelque chose de similaire.**

Si la connexion est réussie, félicitations, vous avez maintenant un serveur VPN ! Mais vous ne pouvez pas y accéder depuis l'extérieur... pour l'instant.

Si vous voulez uniquement un serveur OpenVPN sans le proxy d'obfuscation, vous pouvez passer directement à **Redirection de port**.

### Installation du **Proxy d'Obfuscation**

Obfs4 est un proxy de brouillage. Il déguise votre trafic internet pour qu'il ressemble à du bruit. Une personne qui espionne votre trafic ne saura pas ce que vous faites, et cela vous protégera des attaques par sondage actif utilisées par le Grand Pare-feu de Chine.

_Note : Cette méthode ne fonctionnera pas si votre adversaire n'autorise que le trafic sur liste blanche :(_

#### Installons maintenant le serveur proxy.

0. Installez le paquet requis :

```
apt-get update && apt-get install obfs4proxy
```

1. Créez un répertoire qui contiendra la configuration.

```
sudo mkdir -p /var/lib/tor/pt_state/obfs4
```

2. Créez le fichier de configuration.

```
sudo nano /var/lib/tor/pt_state/obfs4/obfs4.config
```

Dans le fichier de configuration, vous collerez les éléments suivants :

```
TOR_PT_MANAGED_TRANSPORT_VER=1TOR_PT_STATE_LOCATION=/var/lib/tor/pt_state/obfs4TOR_PT_SERVER_TRANSPORTS=obfs4TOR_PT_SERVER_BINDADDR=obfs4-0.0.0.0:444TOR_PT_ORPORT=127.0.0.1:443
```

**TOR_PT_SERVER_BINDADDR** est l'adresse sur laquelle le proxy écoutera les nouvelles connexions. Dans mon cas, c'est `0.0.0.0:444` — pourquoi 444 et non 443 ? Parce que je ne veux pas changer la configuration du serveur OpenVPN qui écoute actuellement sur 443. De plus, je mapperai cette adresse plus tard sur 443 en utilisant la redirection de port.

**TOR_PT_ORPORT** doit pointer vers le serveur OpenVPN. Dans mon cas, mon serveur fonctionne sur `127.0.0.1:443`

3. Créez un fichier de service SystemD.

```
sudo nano /etc/systemd/system/obfs4proxy.service
```

Puis collez le contenu suivant :

```
[Unit]Description=Obfsproxy Server[Service]EnvironmentFile=/var/lib/tor/pt_state/obfs4/obfs4.configExecStart=/usr/bin/obfs4proxy -enableLogging true -logLevelStr INFO[Install]WantedBy=multi-user.target
```

4. Démarrez le proxy d'obfuscation.

Maintenant, assurez-vous qu'OpenVPN est en cours d'exécution et exécutez les commandes suivantes pour démarrer le proxy et l'activer au démarrage.

```
sudo systemctl start obfs4proxysudo systemctl enable obfs4proxy
```

5. Sauvegardez la clé du certificat

Après que le service ait démarré, exécutez la commande suivante et sauvegardez la clé du certificat.

```
cat /var/lib/tor/pt_state/obfs4/obfs4_bridgeline.txt
```

La clé est de la forme `Bridge obfs4 <IP ADDRESS>:<PORT> <FIN**GER**PRINT> c`ert=KEY iat-mode=0. Vous en aurez besoin lorsque vous vous connecterez au VPN.

6. Tester les connexions.

Ouvrez votre client VPN et changez l'IP de 443 à 444 pour vous connecter au proxy au lieu du serveur OpenVPN.

Après cela, trouvez l'option Pluggable Transport dans votre client OpenVPN et voyez s'il supporte **obfs4**.

![Image](https://cdn-media-1.freecodecamp.org/images/k2ce9ab0OAcKCXASAkmIU6GyYVKLr7L1odm1)
_Viscosity supporte différentes méthodes d'obfuscation telles que : obfs2, obfs3, obfs4 et ScrambleSuit_

Si tout fonctionne, alors vous êtes prêt ! Félicitations ! Il ne reste que quelques petites choses à ajuster avant d'utiliser ce VPN depuis l'extérieur.

### **Redirection de port**

Pour accéder au serveur OpenVPN depuis l'extérieur, nous devons débloquer les ports, car ils sont probablement bloqués. Comme vous vous en souvenez, j'ai réservé l'adresse IP de mon PI sur mon routeur pour qu'elle soit toujours `192.168.1.125` afin qu'elle ne change pas si le PI se déconnecte ou si le routeur redémarre.

De cette façon, j'ai défini les règles suivantes dans ma table de redirection de port :

![Image](https://cdn-media-1.freecodecamp.org/images/NqZZFwzTrUAyzVuAHAHDly0Dpoe3zSO24N-i)
_Page des paramètres de redirection de port du TL-WR841N._

Le port extérieur **443** pointera vers le port du serveur d'obfuscation **444**. Si vous n'avez pas de serveur d'obfuscation, laissez **443->443**.

Le port 25 pointera vers le port SSH 22 du PI. Cela est uniquement pour ma propre commodité.

Au cas où je voudrais accéder directement au serveur OpenVPN sans le proxy d'obfuscation, j'ai créé une règle **444->443**

Le port de service est le port **EXTÉRIEUR** qui sera utilisé avec votre adresse IP **PUBLIQUE**. Pour trouver votre IP publique, utilisez un service comme whatsmyip.com.

Le port interne est le port **INTÉRIEUR**. Il ne peut être utilisé que lorsque vous êtes connecté au réseau.

_Note : La première règle dit de rediriger toutes les connexions de **PUBLIC_IP:443** vers **192.168.1.125:444**_

#### Test

1. Trouvez votre IP publique et remplacez votre ancienne IP par l'IP publique dans le fichier .ovpn ou dans le client VPN.
2. Connectez-vous au VPN.

C'est tout.

### **DNS Dynamique**

Dans la plupart des cas, votre IP changera car il s'agit d'une IP dynamique. Une façon de contourner cela est de créer un petit programme sur le PI qui sauvegarde votre IP et vous envoie un e-mail tous les jours ou ainsi. Vous pouvez également stocker l'IP dans une base de données en ligne telle que Firebase.

Mon routeur a un paramètre DNS Dynamique. De cette façon, je peux utiliser un fournisseur de services comme NoIP et obtenir un domaine comme `example.no-ip.com` qui pointera toujours vers mon adresse IP publique.

![Image](https://cdn-media-1.freecodecamp.org/images/d-BrxA5r4qqvGgqjRzuSXGnMGcAncBIKUlu8)
_Page des paramètres DDNS du TL-WR841N_

#### Autres ressources :

* [A Childs Garden Of Pluggable Transports](https://trac.torproject.org/projects/tor/wiki/doc/AChildsGardenOfPluggableTransports)
* [Viscosity-Obsfurcation/](https://www.sparklabs.com/support/kb/article/setting-up-an-obfuscation-server-with-obfsproxy-and-viscosity/)
* [https://www.pluggabletransports.info/transports/](https://www.pluggabletransports.info/transports/)

Si vous avez des questions, contactez-moi sur [Twitter](https://twitter.com/denisnutiu).