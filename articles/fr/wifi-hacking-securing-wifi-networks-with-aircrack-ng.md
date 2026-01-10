---
title: WiFi Hacking 101 – Comment sécuriser vos réseaux WiFi avec Aircrack-NG
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-18T18:14:51.000Z'
originalURL: https://freecodecamp.org/news/wifi-hacking-securing-wifi-networks-with-aircrack-ng
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: penetration testing
  slug: penetration-testing
- name: wifi
  slug: wifi
seo_title: WiFi Hacking 101 – Comment sécuriser vos réseaux WiFi avec Aircrack-NG
seo_desc: 'Imagine a world without WiFi. We would still be using long wires of ethernet
  cables to connect to the internet.

  There is no debate about how much easier WiFi has made our lives. Now we can connect
  to the internet at coffee shops, subway stations, and...'
---

Imaginez un monde sans WiFi. Nous utiliserions encore de longs câbles Ethernet pour nous connecter à Internet.

Il n'y a pas de débat sur la facilité que le WiFi a apportée à nos vies. Maintenant, nous pouvons nous connecter à Internet dans les cafés, les stations de métro et presque partout où nous allons.

Cependant, le WiFi est également un réseau vulnérable par rapport à l'Ethernet. S'il n'est pas correctement sécurisé, il est facile de réaliser des attaques de type "man-in-the-middle" en utilisant [des outils comme Wireshark](https://medium.com/manishmshiva/wireshark-a-walkthrough-of-the-best-packet-analyzer-in-the-world-9af0358ed9a1).

Par exemple, si vous êtes connecté à un réseau Starbucks, toute personne connectée à ce réseau peut voir le trafic réseau de chaque autre personne.

Sauf si vous utilisez un [VPN](https://us.norton.com/internetsecurity-privacy-what-is-a-vpn.html) ou si le site utilise HTTPS, vos données (y compris les mots de passe et les détails de carte de crédit) seront visibles par tout le réseau.

Si vous travaillez pour une entreprise, il est probable qu'ils utilisent également un réseau WiFi. Vous êtes-vous déjà demandé à quel point il est sécurisé ? Savez-vous si quelqu'un dans le parking est connecté à votre réseau et capture les données confidentielles de votre entreprise ?

Avec des outils comme Wireshark et Aircrack, vous pouvez effectuer des audits de sécurité de vos réseaux WiFi. Alors que Wireshark peut vous aider à surveiller ce qui se passe sur votre réseau, Aircrack est davantage un outil offensif qui vous permet d'attaquer et d'accéder à des réseaux WiFi.

Penser comme un attaquant a toujours été la meilleure façon de défendre un réseau. En apprenant à travailler avec Aircrack, vous serez en mesure de comprendre les étapes exactes qu'un attaquant suivrait pour accéder à votre réseau. Vous pourrez ensuite effectuer des audits de sécurité de votre propre réseau pour vous assurer qu'il n'est pas vulnérable.

> **_Une petite note : Je n'encourage en aucun cas l'utilisation d'outils offensifs illégaux. Ce tutoriel est purement éducatif et vise à vous aider à mieux défendre vos réseaux._**

Avant d'examiner Aircrack en détail, voici quelques termes que vous devriez connaître.

* **Point d'accès** — Le réseau WiFi auquel vous souhaitez vous connecter.
* **SSID** — Le nom du point d'accès. Par exemple, « Starbucks ».
* **Fichier Pcap** — Fichier de capture de paquets. Contient des paquets capturés sur un réseau. Le format commun pour des outils incluant Wireshark et Nessus.
* **Wired Equivalent Privacy (WEP)** — Algorithme de sécurité pour les réseaux sans fil.
* **Wi-Fi Protected Access (WPA & WPA2)** — Algorithme de sécurité plus robuste comparé au WEP.
* **IEEE 802.11** — [Protocole de réseau local sans fil (LAN)](https://en.wikipedia.org/wiki/IEEE_802.11).
* **Mode moniteur** — Capture des paquets réseau dans l'air sans se connecter à un routeur ou à un point d'accès.

[J'ai récemment écrit un article sur les 100 termes que vous devriez connaître en tant que testeur d'intrusion](https://medium.com/manishmshiva/penetration-testing-100-terms-you-need-to-know-a723c38cd8c8). Vous pouvez le consulter si vous êtes intéressé.

## Qu'est-ce qu'Aircrack-NG ?

Aircrack est une suite logicielle qui vous aide à attaquer et à défendre les réseaux sans fil.

Aircrack n'est pas un outil unique, mais une collection complète d'outils, chacun remplissant une fonction spécifique. Ces outils incluent un détecteur, un renifleur de paquets, un craqueur WEP/WPA, et ainsi de suite.

Le but principal d'Aircrack est de capturer les paquets et de lire les hachages pour craquer les mots de passe. Aircrack supporte presque toutes les dernières interfaces sans fil.

Aircrack est open-source et peut fonctionner sur les plateformes Linux, FreeBSD, macOS, OpenBSD et Windows.

Le « NG » dans Aircrack-ng signifie « nouvelle génération ». Aircrack-ng est une version mise à jour d'un ancien outil appelé Aircrack. [Aircrack est également préinstallé dans Kali Linux](https://tools.kali.org/wireless-attacks/aircrack-ng).

### Adaptateur WiFi

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1.jpeg)

Avant de commencer à travailler avec Aircrack, vous aurez besoin d'un adaptateur WiFi. Aircrack ne fonctionne qu'avec un contrôleur d'interface réseau sans fil dont le pilote supporte le mode de surveillance brut et peut renifler le trafic 802.11a, 802.11b et 802.11g.

Les adaptateurs WiFi typiques (généralement intégrés à votre ordinateur) n'ont pas la capacité de surveiller le trafic d'autres réseaux. Vous ne pouvez les utiliser que pour vous connecter à un point d'accès WiFi.

Avec un adaptateur WiFi compatible Aircrack, vous pouvez activer le « mode moniteur » avec lequel vous pouvez renifler le trafic des réseaux auxquels vous n'êtes pas connecté. Vous pouvez ensuite utiliser ces données capturées pour craquer le mot de passe de ce réseau.

[Consultez la liste des adaptateurs WiFi compatibles avec Kali Linux ici](https://www.kalilinux.in/2020/07/wifi-adapter-kali-linux-2020.html).

## Outils Aircrack

Maintenant que vous savez ce que vous pouvez faire avec Aircrack, examinons chacun de ses outils.

### Airmon-ng

Airmon-ng est un script qui met votre carte d'interface réseau en mode moniteur. Une fois ce mode activé, vous devriez pouvoir capturer des paquets réseau sans avoir besoin de vous connecter ou de vous authentifier auprès d'un point d'accès.

Vous pouvez utiliser la commande `airmon-ng` pour lister les interfaces réseau et `airmon-ng start <nom de l'interface>` pour démarrer une interface en mode moniteur.

```
# airmon-ng start wlan0

  PID Name
  718 NetworkManager
  870 dhclient
 1104 avahi-daemon
 1105 avahi-daemon
 1115 wpa_supplicant

PHY\tInterface\tDriver\t\tChipset

phy0\twlan0\t\tath9k_htc\tAtheros Communications, Inc. AR9271 802.11n
\t\t(mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
\t\t(mac80211 station mode vif disabled for [phy0]wlan0
```

Dans l'exemple ci-dessus, vous pouvez voir que l'interface réseau `wlan0` a été transformée en `wlan0mon` — ce qui signifie que le mode moniteur a été activé pour celle-ci.

### Airodump-ng

Airodump-ng est un utilitaire de capture de paquets qui capture et sauvegarde des paquets de données brutes pour une analyse ultérieure. Si vous avez un récepteur GPS connecté à votre ordinateur, airodump-ng peut récupérer les coordonnées des points d'accès.

Après avoir activé le mode moniteur avec airmon-ng, vous pouvez commencer à capturer des paquets avec airodump. L'exécution de la commande `airodump-ng` listera les points d'accès disponibles. L'ESSID (ou SSID) est le nom du réseau sans fil.

```
# airodump-ng
CH  9 ][ Elapsed: 1 min ][ 2007-04-26 17:41 ][ WPA handshake: 00:14:6C:7E:40:80
                                                                                                            
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
                                                                                                            
 00:09:5B:1C:AA:1D   11  16       10        0    0  11  54.  OPN              NETGEAR                         
 00:14:6C:7A:41:81   34 100       57       14    1   9  11e  WEP  WEP         bigbear 
 00:14:6C:7E:40:80   32 100      752       73    2   9  54   WPA  TKIP   PSK  teddy                             
                                                                                                            
 BSSID              STATION            PWR   Rate   Lost  Packets  Notes  Probes
                                
 00:14:6C:7A:41:81  00:0F:B5:32:31:31   51   36-24    2       14
 (not associated)   00:14:A4:3F:8D:13   19    0-0     0        4           mossy 
 00:14:6C:7A:41:81  00:0C:41:52:D1:D1   -1   36-36    0        5
 00:14:6C:7E:40:80  00:0F:B5:FD:FB:C2   35   54-54    0       99           teddy
```

### Aircrack-ng

Une fois que vous avez capturé suffisamment de paquets avec airodump-ng, vous pouvez craquer la clé avec aircrack-ng. Aircrack utilise des attaques statistiques, par force brute et par dictionnaire pour casser la clé WEP/WPA.

```
Aircrack-ng 1.4


                 [00:00:03] 230 keys tested (73.41 k/s)


                         KEY FOUND! [ biscotte ]


    Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6 
                     39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE 

    Transcient Key : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49 
                     73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08 
                     AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97 
                     D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD 

    EAPOL HMAC     : 52 27 B8 3F 73 7C 45 A0 05 97 69 5C 30 78 60 BD

```

Il est important de noter que vous avez besoin de suffisamment de paquets pour craquer la clé. De plus, aircrack-ng utilise des algorithmes sophistiqués pour craquer les clés à partir des paquets réseau.

Si vous êtes intéressé à en savoir plus sur la façon dont Aircrack fait cela, [ce serait un bon point de départ](https://www.aircrack-ng.org/doku.php?id=aircrack-ng).

### Aireplay-ng

Aireplay-ng est utilisé pour créer du trafic artificiel sur un réseau sans fil. Aireplay peut soit capturer le trafic d'un réseau en direct, soit utiliser les paquets d'un fichier Pcap existant pour les injecter dans un réseau.

Avec aireplay-ng, vous pouvez effectuer des attaques telles que l'authentification fictive, l'injection de paquets, l'attaque caffe-latte, et ainsi de suite.

L'attaque Cafe Latte vous permet d'obtenir une clé WEP à partir d'un appareil client. Vous pouvez le faire en capturant un [paquet ARP](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/arp.html) du client, en le manipulant, puis en l'envoyant au client.

Le client générera alors un paquet qui peut être capturé par airodump-ng. Enfin, aircrack-ng peut être utilisé pour craquer la clé WEP à partir de ce paquet modifié.

### Airbase-ng

Airbase-ng est utilisé pour transformer l'ordinateur d'un attaquant en un point d'accès pirate auquel d'autres peuvent se connecter.

En utilisant Airbase, vous pouvez prétendre être un point d'accès légitime et effectuer des attaques de type "man-in-the-middle" sur les appareils qui se connectent à votre système.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/2.png)

Cette attaque est également appelée "**Attaque du Jumeau Maléfique**". Supposons que vous êtes chez Starbucks en essayant de vous connecter à leur WiFi, un attaquant peut créer un autre point d'accès avec le même nom (généralement avec une meilleure puissance de signal) vous faisant croire que le point d'accès appartient à Starbucks.

Il est difficile pour les utilisateurs réguliers de différencier un point d'accès légitime d'un point d'accès pirate. Ainsi, l'attaque du jumeau maléfique reste l'une des attaques sans fil les plus dangereuses que nous rencontrons aujourd'hui.

En plus de ceux-ci, il y a quelques outils supplémentaires à utiliser dans l'arsenal Aircrack.

* **Packetforge-ng** — Utilisé pour créer des paquets chiffrés pour injection.
* **Airdecap-ng** — Déchiffre les fichiers de capture chiffrés WEP/WPA après avoir craqué la clé avec aircrack-ng. Cela vous donnera accès aux noms d'utilisateur, mots de passe et autres données sensibles.
* **Airolib-ng** — Stocke les phrases de passe WPA/WPA2 pré-calculées dans une base de données. Utilisé avec aircrack-ng lors du craquage des mots de passe.
* **Airtun-ng** — Crée des interfaces de tunnel virtuel.

## Résumé

Le monde est un endroit plus connecté, grâce au WiFi. Nous profitons des avantages du WiFi presque tous les jours. Avec tous ses avantages, c'est aussi un réseau vulnérable capable d'exposer nos informations privées, si nous ne sommes pas prudents.

J'espère que cet article vous a aidé à comprendre la sécurité WiFi et Aircrack en détail. Pour en savoir plus sur Aircrack, [consultez leur wiki officiel](https://www.aircrack-ng.org/doku.php).

_Vous avez aimé cet article ?_ [**_Rejoignez ma Newsletter_**](http://tinyletter.com/manishmshiva) _et recevez un résumé de mes articles et vidéos envoyés à votre email chaque lundi. Vous pouvez également [**trouver mon blog ici**](https://medium.com/manishmshiva).