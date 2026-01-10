---
title: Comment configurer un serveur VPN à la maison gratuitement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-15T20:19:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-vpn-server-at-home
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/grey-and-black-macbook-pro-showing-vpn-2064586--1-.jpg
tags:
- name: Security
  slug: security
- name: self hosting
  slug: self-hosting
- name: vpn
  slug: vpn
seo_title: Comment configurer un serveur VPN à la maison gratuitement
seo_desc: 'By Yehuda Clinton

  In this article, I''m going to guide you, step-by-step, through the process of setting
  up a WireGuard VPN on a Linux server. It will let you access secure internet resources
  from insecure places like coffee shops.

  But why a VPN? And ...'
---

Par Yehuda Clinton

Dans cet article, je vais vous guider, étape par étape, à travers le processus de configuration d'un VPN WireGuard sur un serveur Linux. Cela vous permettra d'accéder à des ressources internet sécurisées depuis des endroits non sécurisés comme les cafés.

## Mais pourquoi un VPN ? Et pourquoi WireGuard ?

Chaque fois que vous vous connectez, par exemple, au site web de votre banque depuis un lieu distant, vous risquez d'exposer des mots de passe et d'autres informations sensibles à quiconque écoute sur le réseau.

Espérons, bien sûr, que le site web de la banque lui-même sera chiffré, ce qui signifie que les données clés circulant entre la banque et votre PC ou smartphone seront illisibles pour quiconque écoute en chemin.

Et qu'en est-il si vous vous connectez depuis votre domicile ou votre bureau ? Avec un VPN, vous pouvez être raisonnablement sûr que les éléments de données non obscurcis par le chiffrement régulier ne seront pas vus par les mauvaises personnes.

Mais que se passe-t-il si vous vous connectez via un routeur WiFi public dans un aéroport ou un café ? Êtes-vous sûr que le réseau n'a pas été compromis ou qu'il n'y a pas de pirates informatiques qui observent sans être détectés ?

Pour contrer cette menace très réelle, vous pouvez ouvrir une connexion sur votre ordinateur portable ou votre téléphone vers un serveur VPN. Ainsi, tous vos transferts de données se font via un tunnel virtuel. Chaque partie de vos connexions sensibles sera invisible pour quiconque sur le réseau local depuis lequel vous vous connectez.

WireGuard est le plus récent des trois grands acteurs dans le monde des VPN open source, les deux autres étant IPsec et OpenVPN.

WireGuard est conçu pour être plus simple, plus rapide et plus flexible que les autres. C'est le nouveau venu, mais il s'est rapidement fait des amis importants. À l'initiative de Linus Torvalds, le créateur de Linux lui-même, WireGuard a récemment été intégré au noyau Linux.

# Où construire votre serveur VPN ?

Bien sûr, vous pouvez toujours assembler un serveur VPN à la maison et configurer le transfert de port via le routeur de votre FAI. Mais il sera souvent plus pratique de le faire fonctionner dans le cloud.

Ne vous inquiétez pas. Je vous assure que cette méthode sera beaucoup plus proche d'une configuration "installez et oubliez" rapide et sans douleur. Et il est hautement improbable que ce que vous construisez à la maison soit aussi fiable – ou sécurisé – que l'infrastructure fournie par les grands fournisseurs de cloud comme AWS.

Cependant, si vous avez un serveur internet professionnel sécurisé qui traîne à la maison (ou si vous êtes prêt à prendre un risque avec un Raspberry Pi de rechange que vous avez sous la main), alors cela fonctionnera à peu près de la même manière.

Grâce à WireGuard, que ce soit dans le cloud ou sur un serveur physique, créer votre propre VPN domestique n'a jamais été aussi facile. Toute la configuration peut être faite en une demi-heure.

# Préparation

Lancez votre instance cloud, peut-être en utilisant un [tutoriel d'ici](https://www.freecodecamp.org/news/administrating-aws-resources-productively-using-the-aws-cli/).

Assurez-vous que le port **51820** est ouvert vers votre serveur. Cela se fait avec les _groupes de sécurité_ sur AWS et un _pare-feu de réseau VPC_ sur Google Cloud.

Avec les versions modernes de Debian/Ubuntu, Wireguard est disponible pour être installé à partir des gestionnaires de paquets comme ceci :

```
sudo apt install wireguard

```

Ou avec yum, depuis le dépôt EPEL :

```
sudo yum install kmod-wireguard wireguard-tools

```

# Étape un : créer les clés de chiffrement

Dans n'importe quel répertoire sur le serveur où vous souhaitez créer des fichiers contenant les clés publiques et privées, utilisez cette commande :

```
umask 077; wg genkey | tee privatekey | wg pubkey > publickey

```

Faites de même pour le client dans un répertoire différent ou sur votre machine locale. Assurez-vous simplement de pouvoir distinguer les différents ensembles de clés plus tard.

Pour une configuration rapide, vous pouvez utiliser un [générateur de clés en ligne](https://www.wireguardconfig.com). Cependant, je suggère de le faire manuellement la première fois. Assurez-vous que les fichiers ont été créés avec des hachages de clés, car vous les utiliserez dans l'étape suivante.

# Étape deux : créer la configuration du serveur

Vous devez créer un fichier _.conf_ dans le répertoire /etc/wireguard. Vous pouvez même avoir plusieurs VPN fonctionnant en même temps en utilisant différents ports.

Collez le code suivant dans le nouveau fichier :

```
sudo nano /etc/wireguard/wg0.conf

```

```
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
# utilisez la clé privée du serveur
PrivateKey = GPAtRSECRETLONGPRIVATEKEYB0J/GDbNQg6V0s=

# vous pouvez avoir autant de pairs que vous le souhaitez
# n'oubliez pas de remplacer les valeurs ci-dessous par la clé publique du pair

[Peer]
PublicKey = NwsVexamples4sBURwFl6HVchellou6o63r2B0s=
AllowedIPs = 10.0.0.2/32

[Peer]
PublicKey = NwsexampleNbw+s4sBnotFl6HrealxExu6o63r2B0s=
AllowedIPs = 10.0.0.3/32

```

### Démarrer le VPN

```
sudo systemctl start wg-quick@wg0

```

Si vous n'avez pas systemd (ce qui peut être le cas si votre instance utilise Amazon Linux), vous pouvez utiliser `sudo wg-quick up wg0`.

# Étape trois : créer la configuration du client

Tout d'abord, installez Wireguard sur votre machine cliente, soit de la même manière sur Linux, soit via une boutique d'applications si vous utilisez Windows, macOS, Android ou iPhone.

Si vous avez utilisé un générateur de clés en ligne ou un script QR à l'étape un, vous pouvez connecter votre téléphone en prenant une photo du code QR.

Une fois WireGuard installé sur le client, configurez-le en utilisant ces valeurs :

```
# Remplacez la valeur PrivateKey par celle de votre interface client
[Interface]
Address = 10.0.0.2/24
ListenPort = 51820
PrivateKey = CNNjIexAmple4A6NMkrDt4iyKeYD1BxSstzer49b8EI=

# utilisez la clé publique du serveur VPN et l'IP de l'instance cloud
[Peer]
PublicKey = WbdIAnOTher1208Uwu9P17ckEYxI1OFAPZ8Ftu9kRQw=
AllowedIPs = 0.0.0.0/0
Endpoint = 34.69.57.99:51820

```

Il existe de nombreux modules complémentaires optionnels que vous pourriez vouloir en fonction de votre cas d'utilisation, tels que la spécification du DNS ou des clés pré-partagées pour une couche de sécurité supplémentaire.

Démarrez le client de la même manière que le serveur si vous êtes sur Linux ou via l'application elle-même sur d'autres systèmes.

# Testez votre VPN

Tapez "my ip" dans votre navigateur pour découvrir votre adresse IP publique. Si l'IP que vous obtenez est différente de l'adresse que votre ordinateur avait avant de démarrer le VPN, alors vous avez réussi !

(Et si vous avez oublié ce qu'elle était avant, essayez `sudo systemctl stop wg-quick@wg0`, vérifiez et redémarrez-le.)

# Guide de dépannage

Assurez-vous que votre serveur est configuré pour le transfert IP. Vérifiez le fichier /etc/sysctl.conf, ou exécutez :

```
echo 1 > /proc/sys/net/ipv4/ip_forward

```

Votre connexion meurt souvent ? Ajoutez ceci à la section peer de la configuration du client :

```
PersistentKeepalive = 25

```

Vous n'êtes pas sûr de savoir pourquoi cela ne fonctionne pas ? Essayez `sudo tcpdump -i eth` sur le serveur tout en essayant d'utiliser le client.

## Merci d'avoir lu ce guide.

Si vous souhaitez approfondir, envisagez de suivre [mon cours payant Manning sur le VPN WireGuard](https://www.manning.com/liveproject/secure-business-infrastructure-with-a-custom-vpn?a_aid=bootstrap-it&a_bid=b9d7d398&chan=VPN).