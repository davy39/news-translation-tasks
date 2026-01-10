---
title: Apprendre les bases de l'architecture réseau pour débutants
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-11T19:05:27.000Z'
originalURL: https://freecodecamp.org/news/network-architecture-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-brett-sayles-2881232.jpg
tags:
- name: architecture
  slug: architecture
- name: computer network
  slug: computer-network
- name: Security
  slug: security
seo_title: Apprendre les bases de l'architecture réseau pour débutants
seo_desc: "Networking is engineering, magic, and skilled trade all rolled into one.\
  \ Getting all the countless pieces to talk nicely – and reliably – to each other\
  \ is complicated. Troubleshooting unexpected outages is worse. \nBut, once you've\
  \ got it all running ..."
---

La mise en réseau est à la fois de l'ingénierie, de la magie et un métier qualifié. Faire en sorte que les innombrables pièces communiquent bien – et de manière fiable – entre elles est compliqué. Résoudre les pannes inattendues est pire.

Mais une fois que tout fonctionne bien, c'est là que vous devriez vraiment vous inquiéter : car c'est exactement à ce moment-là que les méchants commencent à tambouriner à la porte en essayant de trouver un moyen d'entrer.

Dans cet article, nous allons couvrir juste assez des fondamentaux les plus importants de la mise en réseau afin que les discussions sur la sécurité réseau que vous pourriez rencontrer aient du sens.

Cet article provient de [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Vous pouvez également suivre avec cette vidéo :

%[https://www.youtube.com/watch?v=tsAEFWVJKsc&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=5]

## Comprendre IPv4 et le routage NAT

Les réseaux IP (où IP signifie Internet Protocol) sont l'épine dorsale de l'Internet, connectant les appareils et transmettant des données sur le réseau.

IP est responsable du routage des paquets de données d'un appareil à un autre, et IP version 4 est le format d'adresse IP le plus largement utilisé. IPv4 utilise une adresse 32 bits, et se compose de quatre nombres 8 bits appelés octets. Les adresses IPv4 sont écrites en notation décimale où chaque octet est séparé par un point.

Un exemple d'adresse hôte IPv4 pourrait ressembler à ceci :

```
192.168.2.34
```

La traduction d'adresse réseau est une méthode utilisée pour permettre aux adresses IPv4 privées d'accéder à l'Internet. NAT mappe les adresses IP privées à une seule adresse IP publique, qui est assignée par un fournisseur d'accès Internet (FAI).

Lorsque un appareil dans un réseau privé souhaite accéder à l'Internet, il envoie une requête à la passerelle NAT. La passerelle NAT traduit l'adresse IP privée de l'appareil en l'adresse IP publique assignée par le FAI et transmet la requête à l'Internet.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-11.png)
_Explication de l'adressage NAT dans un diagramme_

Lorsque la réponse de l'Internet est reçue, la passerelle NAT traduit l'adresse IP publique en l'adresse IP privée de l'appareil et envoie la réponse à l'appareil.

De cette manière, NAT permet à plusieurs appareils dans un réseau privé de partager une seule adresse IP publique et d'accéder à l'Internet, tout en masquant leurs adresses IP privées du public. NAT fournit également un niveau de sécurité de base en masquant le réseau interne de l'Internet.

## Comprendre IPv6

IP version 6 est le dernier format d'adresse IP. IPv6 utilise une adresse 128 bits, et est composé de huit segments hexadécimaux 16 bits séparés par des deux-points.

Voici un exemple de ce à quoi une adresse IPv6 pourrait ressembler :

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

IPv6 a été créé parce que nous manquions d'adresses IPv4 – puisque les adresses 32 bits d'IPv4 permettent un maximum de seulement 4,3 milliards d'adresses uniques.

C'était bien dans les premiers jours de l'Internet, mais à mesure que le nombre d'appareils connectés à l'Internet a augmenté, la demande d'adresses IP uniques a dépassé le nombre disponible dans l'espace d'adressage IPv4.

Pour remédier à cette pénurie, IPv6 a été développé avec son espace d'adressage plus grand, permettant 340 billions, billions, billions d'adresses uniques. Cet espace d'adressage important garantit qu'il y aura assez d'adresses IP uniques pour tous les appareils connectés à l'Internet pour toujours. Littéralement.

De plus, les adresses IPv6 surmontent certaines autres limitations d'IPv4, telles que la sécurité améliorée, l'auto-configuration et le support pour l'allocation hiérarchique d'adresses et le routage.

## Définir les protocoles de routage

TCP (Transmission Control Protocol) et UDP (User Datagram Protocol) sont deux des protocoles de couche transport les plus courants utilisés dans les réseaux IP.

TCP est un protocole orienté connexion fiable qui fournit une vérification des erreurs et un contrôle de flux. UDP est un protocole sans connexion qui fournit une transmission de données rapide mais avec moins de fiabilité.

ICMP (Internet Control Message Protocol) est un protocole de couche réseau utilisé pour envoyer des messages d'erreur, tester la connectivité réseau (en particulier, à travers un outil appelé `ping`), et effectuer d'autres fonctions.

DHCP (Dynamic Host Configuration Protocol) est un protocole utilisé pour assigner dynamiquement des adresses IP aux appareils sur un réseau. Dans un réseau domestique ou de petite entreprise, DHCP est généralement effectué par un routeur ou un serveur DHCP dédié, qui est responsable de l'assignation dynamique des adresses IP aux appareils sur le réseau.

Voici comment le processus de DHCP fonctionne typiquement :

* Lorsqu'un appareil se connecte au réseau, il diffuse une requête pour une adresse IP.
* Le serveur DHCP reçoit la requête et assigne une adresse IP unique à l'appareil, ainsi que d'autres informations réseau telles que le masque de sous-réseau, la passerelle par défaut et les adresses des serveurs DNS.
* L'appareil reçoit l'adresse IP assignée et les autres informations réseau du serveur DHCP et les utilise pour configurer ses paramètres réseau.
* Enfin, le serveur DHCP maintient une table des adresses IP assignées et des appareils auxquels elles ont été assignées, afin de s'assurer que chaque appareil sur le réseau a une adresse IP unique.

Dans un réseau domestique ou de petite entreprise, le routeur ou le serveur DHCP est généralement configuré pour assigner automatiquement des adresses IP aux appareils sur le réseau. Cela élimine le besoin de configuration manuelle des adresses IP et facilite la connexion des appareils au réseau.

Avec ces bases, vous serez dans une bien meilleure position pour comprendre les discussions sur les problèmes de sécurité réseau que vous entendez ou lisez.

Cet article et la vidéo qui l'accompagne sont extraits de [mon cours Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/).