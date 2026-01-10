---
title: "Comment d\x027\x02epanner votre r\x02eau sous Linux \x02 \x02 Guide de d\x02\
  epannage du mod\x02ele OSI"
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2024-03-25T17:34:59.000Z'
originalURL: https://freecodecamp.org/news/how-troubleshoot-network-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/taylor-vick-M5tzZtFCOfs-unsplash.jpg
tags:
- name: Linux
  slug: linux
- name: network
  slug: network
seo_title: "Comment d\x027\x02epanner votre r\x02eau sous Linux \x02 \x02 Guide de\
  \ d\x02epannage du mod\x02ele OSI"
seo_desc: 'In the world of networking, you may find yourself troubleshooting problems
  such as difficulty connecting to other computers or to SSH, problems with IP tables,
  or being unable to access websites.

  However, have you ever attempted to troubleshoot your ...'
---

Dans le monde des reseaux, vous pouvez etre amene  resoudre des problemes tels que des difficultes  se connecter  d'autres ordinateurs ou  SSH, des problemes avec les tables IP, ou l'impossibilite d'acceder  des sites web.

Cependant, avez-vous dej tente de depanner votre reau en appliquant le modele OSI ? Grace  une methodologie ascendante basee sur l'architecture Open Systems Interconnection (OSI), nous decouvrirons les complexites du depannage reau, vous fournissant les connaissances et les outils essentiels pour resoudre efficacement une grande variete de difficultes reseau.

## Qu'est-ce que le modele OSI (Open Systems Interconnection) ?

Le modele Open Systems Interconnection (OSI) est un cadre conceptuel qui categorise les fonctions des communications reau en sept niveaux distincts. En d'autres termes, l'OSI standardise la facon dont differents systemes informatiques peuvent communiquer entre eux.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-24-at-15.28.35.png)
_sept couches du modele OSI_

## Comment depanner un site web en appliquant les principes du modele OSI

Considerons l'exemple suivant de depannage d'un site web heberge sur votre serveur qui ne fonctionne pas. Nous utiliserons Linux comme systeme d'exploitation. Je crois que la technique de diviser pour regner est une meilleure methode pour le debogage.

Le modele OSI est une methode pour decomposer efficacement un probleme afin que vous puissiez simplifier methodiquement l'environnement pour decouvrir une solution et le resoudre.

### Couche physique

Comme je l'ai precedemment mentionne, en matiere de debogage, il est generalement preferable de commencer par le bas. La couche physique est la couche inferieure dans le modele OSI. Les elements cles de cette couche sont les cables Ethernet, les hubs et les commutateurs.  ce niveau, vous devez verifier l'alimentation lectrique et l'etat des appareils, ainsi qu'examiner les statistiques des interfaces.

* L'outil "ifconfig" fournit un apercu detaille de toutes les cartes Ethernet presentes dans votre systeme.
* De plus, vous avez le choix d'utiliser les commandes "IP link show". Si le resultat montre "down", cela suggere que la couche 1 ne fonctionne pas.
* Parfois, les connexions Ethernet peuvent etre physiquement connectees au serveur mais non activees par defaut. Pour les activer, utilisez la commande ci-dessous.

```bash
IP link set eth0 up
```

* Si vous cherchez des informations plus detaillees, l'utilitaire ethtool peut etre tres utile. Cet utilitaire permet d'interroger et de modifier les parametres. Il vous permet d'ajuster des parametres tels que la vitesse, le port, la negociation automatique, les emplacements PCI et le dechargement de la somme de controle.

### Couche de liaison de donnees

La couche de liaison de donnees permet la transmission de donnees entre deux appareils connectes au meme reau. Il y a deux composants dans cette couche. Le premier composant est la couche de controle d'acces au support (MAC), qui inclut le fonctionnement de l'adressage materiel et du controle d'acces.

La deuxieme couche est la couche de liaison logique, qui permet la creation d'une connexion logique entre differents supports. Un probleme courant dans cette couche est l'incapacite de deux serveurs  etablir une connectivite. Des outils tels que ping, traceroute, arp, macof et Wireshark sont utilises pour tester la couche de liaison de donnees.

Cela peut aider  verifier la transmission et la reception correctes des trames de donnees parmi les appareils au sein du meme groupe reau.

### Couche reau

Le role de la couche reau est de faciliter le deplacement des donnees entre deux reseaux. Les appareils reau qui fonctionnent  la couche 3 du modele OSI sont les routeurs. Le role principal d'un routeur est de faciliter la communication entre les reseaux. Travailler avec des adresses IP fait partie de cette couche.

 cette etape, vous devez principalement rechercher des problemes avec les adresses IP. Vous pouvez taper "ip -br address show" pour voir l'adresse. Vous pouvez voir si votre carte reau a recu une adresse IP. Vous ne recevez peut-etre pas d'adresses IP dynamiques du DHCP si vous l'utilisez pour les obtenir.

Un probleme courant qui survient souvent est l'absence d'une passerelle amont pour une route specifique ou l'absence d'une route par defaut. Lorsqu'un paquet IP est transmis  un autre reau, il doit etre dirige vers une passerelle pour un traitement supplementaire.

Comprendre le routage des paquets vers leurs destinations finales est crucial pour la passerelle. La table de routage contient la liste des passerelles pour diverses routes et peut etre geree  l'aide des commandes "ip route". Nous pouvons egalement verifier la connectivite en envoyant des pings  la passerelle par defaut ou au-dela de la passerelle.

### Couche transport

Des protocoles comme le Transmission Control Protocol (TCP) et le User Datagram Protocol (UDP) sont utilises par la couche transport pour controler le trafic reau entre les systemes et s'assurer que les donnees circulent efficacement.

La couche transport est responsable de l'envoi des paquets de donnees, de la recherche d'erreurs, du controle du flux de donnees et de leur mise dans le bon ordre. Vous pouvez rencontrer des problemes dans cette couche, comme des ports qui n'ecoutent pas. Votre service ne demarre peut-etre pas parce que le port est dej utilise. Vous pouvez voir quels ports sont ouverts en executant "commad "netstat -antlp | grep "LISTEN"".

Un probleme qui survient souvent est lie  la connectivite  distance. Considerez un scenario ou votre systeme local est incapable d'etablir une connexion avec un port distant, specifiquement HTTP sur le port 80. La commande `telnet` tente de creer une connexion TCP avec l'hote et le port specifies. Cette capacite est ideale pour effectuer des tests de connectivite TCP  distance.

Pour verifier un port UDP distant, vous pouvez utiliser l'utilitaire "netcat".

### Couche session

Cette couche est responsable de la facilitation de l'initiation et de la terminaison de la communication entre les deux appareils (par exemple : l'authentification). La periode pendant laquelle la communication est initiee et terminee est appelee la session.

Dans cette couche, vous devez enqueter sur les identifiants, les certificats des serveurs, l'ID de session et les cookies des clients.

### Couche presentation

La couche presentation du modele OSI est responsable de la mise en forme et de la transformation des donnees de maniere  ce qu'elles puissent etre presentees  l'utilisateur.

Les methodes de chiffrement SSL ou TLS sont des elements cles de cette couche. Ici, vous devez examiner les problemes de chiffrement et de dechiffrement.

### Couche application

Le systeme reoit les entrees de l'utilisateur et transmet les sorties  l'utilisateur. Les protocoles suivants fonctionnent  ce niveau.

Vous devez verifier les fichiers de configuration sur votre serveur pour toute mauvaise configuration. De plus, il est essentiel de consulter les fichiers de journalisation sur les serveurs pour obtenir des informations plus detaillees sur les problemes.

* File Transfer Protocol (FTP)
* Simple Mail Transfer Protocol (SMTP)
* Secure Shell (SSH)
* Internet Message Access Protocol (IMAP)
* Domain Name Service (DNS)
* Hypertext Transfer Protocol (HTTP).

## **Conclusion**

Le depannage des problemes reau sous Linux peut etre une tache ardue, mais en appliquant les principes du modele OSI, vous pouvez diagnostiquer et resoudre les problemes de maniere systematique avec une plus grande efficacite.

En commencant par la couche inferieure et en remontant, nous avons explore divers outils et techniques adaptes  chaque niveau du modele OSI.

En commencant par la couche physique, nous avons inspecte les composants materiels et utilise des outils comme `ifconfig` et `ip link show` pour verifier la connectivite. En remontant  la couche de liaison de donnees, nous nous sommes concentres sur les adresses MAC et avons utilise des utilitaires comme `ping` et `Wireshark` pour les tests.  la couche reau, nous avons aborde l'adressage IP et le routage, en employant des commandes telles que `ip route` et `ping` pour diagnostiquer les problemes.

En passant  la couche transport, nous avons traite des problemes lies  TCP et UDP, en utilisant des commandes comme `netstat` et `telnet` pour verifier les ports ouverts et tablir des connexions. Plus haut dans la pile, nous avons discute de l'importance de la gestion des sessions et du chiffrement aux couches session et presentation respectivement.

Enfin,  la couche application, nous avons examine des protocoles specifiques comme FTP, SMTP, SSH et HTTP, en soulignant l'importance des fichiers de configuration et de l'analyse des journaux pour resoudre les problemes.