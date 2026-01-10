---
title: Comment obtenir un accès wifi gratuit sur les réseaux publics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-01T22:19:16.000Z'
originalURL: https://freecodecamp.org/news/free-wifi-on-public-networks-daf716cebc80
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e2RzdGIwHAmNUHULsf9aOg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment obtenir un accès wifi gratuit sur les réseaux publics
seo_desc: 'By Kyle McDonald

  This short tutorial describes a few methods for gaining access to the internet,
  a basic human right, from public wireless networks.

  This tutorial has been tested on Mac, should work on Linux, and hasn’t been tested
  on Windows.

  Prepar...'
---

Par Kyle McDonald

Ce court tutoriel décrit quelques méthodes pour accéder à Internet, [un droit humain fondamental](https://en.wikipedia.org/wiki/Right_to_Internet_access#2011:_UN_Special_Rapporteur_report), depuis les réseaux sans fil publics.

Ce tutoriel a été testé sur Mac, devrait fonctionner sur Linux et n'a pas été testé sur Windows.

### Préparation

Assurez-vous d'effectuer cette étape _avant_ de vous retrouver sans accès Internet.

1. Installez [Python pip](https://pip.pypa.io/en/stable/installing/).
2. Faites une copie de [ce dépôt](https://github.com/kylemcdonald/FreeWifi) et installez les dépendances pour le script que nous allons utiliser :

```
git clone https://github.com/kylemcdonald/FreeWificd FreeWifi && pip install -r requirements.txt
```

### Comment obtenir du temps supplémentaire

Si vous aviez un accès Internet gratuit mais que votre temps est écoulé, la première chose à essayer est d'ouvrir une fenêtre de navigation privée/incognito. Voici les instructions pour quelques navigateurs :

* [Chrome](https://support.google.com/chrome/answer/95464?source=gsearch&hl=en) (mobile et desktop)
* [Safari pour iOS](https://support.apple.com/en-us/HT203036)
* [Safari pour Mac](https://support.apple.com/kb/ph21413?locale=en_US)
* [Microsoft Edge](https://support.microsoft.com/en-us/instantanswers/34b9a3a6-68bc-510b-2a9e-833107495ee5/browse-inprivate-in-microsoft-edge)

Une fenêtre de navigation privée/incognito effacera temporairement les cookies qui pourraient avoir été utilisés pour suivre le temps que vous avez passé en ligne, vous faisant apparaître comme un "nouvel utilisateur" et vous permettant de vous reconnecter au portail sans fil.

Malheureusement, la plupart des systèmes suivent les adresses MAC au lieu des cookies. Une adresse MAC est un identifiant unique attribué à chaque interface réseau. Cela signifie que vous devez obtenir une nouvelle adresse MAC pour obtenir du temps supplémentaire. Heureusement, les adresses MAC peuvent être modifiées logiciellement, sans changer le matériel. L'utilitaire en ligne de commande `spoof-mac` facilite cela en entrant `sudo spoof-mac randomize Wi-Fi`. Si la commande échoue, essayez d'entrer `spoof-mac list --wifi` pour vérifier le nom de votre appareil sans fil d'abord, et utilisez-le manuellement. Après avoir randomisé votre MAC, essayez de vous reconnecter au portail sans fil. Une fois que vous avez terminé d'utiliser Internet, exécutez `sudo spoof-mac reset Wi-Fi` pour réinitialiser votre adresse MAC.

Notez que le spoofing d'adresse MAC peut être interprété comme une activité illégale selon la raison pour laquelle vous le faites. Dans certains cas, il n'est certainement pas illégal : les systèmes d'exploitation mobiles récents comme iOS 8+ et Android 6+ randomisent automatiquement leur adresse MAC lors de la recherche de réseaux sans fil pour éviter d'être suivis. Mais lorsque [Aaron Swartz a libéré JSTOR](https://en.wikipedia.org/wiki/MAC_spoofing#Controversy), le spoofing d'adresse MAC a été présenté comme un signe d'intention de commettre un crime.

### Comment obtenir un accès gratuit

Si le réseau est ouvert, mais que vous ne pouvez pas obtenir d'accès pour une raison quelconque, vous pouvez également essayer de spoofing l'adresse MAC d'un appareil qui utilise déjà le réseau. Pour le routeur, votre appareil et l'autre appareil sembleront être un seul appareil. Cela peut causer quelques problèmes mineurs s'ils s'interrompent mutuellement, mais pour une navigation légère, cela fonctionne généralement bien.

Pour trouver les adresses MAC des autres appareils utilisant le réseau, vous devez d'abord vous connecter au réseau. Vous n'avez pas besoin d'avoir accès à Internet, juste une connexion. Tout d'abord, sur Mac OS, exécutez la commande `sudo chmod o+r /dev/bpf*` une fois pour vous assurer de pouvoir capturer les données sans fil (vous devez le refaire si vous redémarrez votre ordinateur).

Ensuite, dans votre terminal, exécutez la commande `python wifi-users.py`. Vous devriez voir une barre de progression immédiatement :

```
SSID: nonoinflightGateway: 00:e0:4b:22:96:d9100%|████████████████████████████████████| 1000/1000 [00:46<00:00, 21.46it/s]Total of 5 user(s):27:35:96:a8:66:7f   6359 bytes36:fe:83:9c:35:eb   9605 bytes65:01:3c:cc:20:e8   17306 bytes8c:6f:11:2c:f0:ee   20515 bytes0a:4f:b2:b8:e8:56   71541 bytes
```

S'il n'y a pas beaucoup de trafic sur le réseau, cela peut prendre plus de temps. Si cela prend trop de temps, tapez `CTRL-C` pour annuler la capture et afficher les résultats disponibles. Enfin, nous voulons spoofing l'une de ces adresses MAC. Par exemple, dans ce cas, nous entrerions `sudo spoof-mac set 0a:4f:b2:b8:e8:56 Wi-Fi` pour essayer de spoofing l'adresse avec le plus de trafic (ils ont probablement une connexion).

Après avoir exécuté cette commande, essayez d'accéder à Internet. Si vous n'avez pas de connexion, essayez la prochaine MAC dans la liste. Si votre connexion Internet est interrompue pendant l'utilisation de cette adresse MAC, essayez de vous déconnecter et de vous reconnecter au réseau sans fil. Notez que l'utilisateur original de l'adresse MAC que vous avez copiée peut également subir ces mêmes interruptions de connexion si vous utilisez tous les deux activement le réseau.

### Comment cela fonctionne

`wifi-users.py` utilise `tcpdump` pour collecter les paquets sans fil. Ensuite, nous recherchons dans ces paquets des indices de l'adresse MAC (BSSID) de notre réseau sans fil. Enfin, nous recherchons des paquets de données qui mentionnent l'adresse MAC d'un utilisateur ainsi que le BSSID du réseau (ou la passerelle du réseau), et nous notons cette adresse MAC en utilisant une certaine quantité de données. Ensuite, nous trions les adresses MAC des utilisateurs par la quantité totale de données et les affichons.

Au lieu de capturer le trafic sans fil, dans certaines situations, vous pouvez également utiliser la commande `arp -a` pour obtenir une liste des adresses MAC des appareils sur le réseau sans fil. Ensuite, vous pouvez soit utiliser `spoof-mac` pour copier l'adresse, soit utiliser `ifconfig` directement sur Linux et OSX. Pour les spécificités de l'utilisation de `ifconfig`, consultez les implémentations de `set_interface_mac` dans [SpoofMac's interfaces.py](https://github.com/feross/SpoofMAC/blob/master/spoofmac/interface.py).

_Cet article est dédié à Lauren McCarthy, qui m'a appris le plus sur l'art de faire une bonne affaire._