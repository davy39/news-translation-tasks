---
title: Le modèle OSI – Les 7 couches de la mise en réseau expliquées en français
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-21T16:38:58.000Z'
originalURL: https://freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/network-3537401_1920.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
seo_title: Le modèle OSI – Les 7 couches de la mise en réseau expliquées en français
seo_desc: 'By Chloe Tucker

  This article explains the Open Systems Interconnection (OSI) model and the 7 layers
  of networking, in plain English.

  The OSI model is a conceptual framework that is used to describe how a network functions.
  In plain English, the OSI m...'
---

Par Chloe Tucker

Cet article explique le modèle Open Systems Interconnection (OSI) et les 7 couches de la mise en réseau, en français.

Le modèle OSI est un cadre conceptuel utilisé pour décrire le fonctionnement d'un réseau. En français, le modèle OSI a aidé à standardiser la manière dont les systèmes informatiques s'envoient des informations.

Apprendre la mise en réseau est un peu comme apprendre une langue - il y a beaucoup de normes et puis quelques exceptions. Par conséquent, il est important de vraiment comprendre que le modèle OSI n'est pas un ensemble de règles. C'est un outil pour comprendre comment les réseaux fonctionnent.

Une fois que vous aurez appris le modèle OSI, vous serez en mesure de mieux comprendre et apprécier cette entité glorieuse que nous appelons l'Internet, ainsi que de pouvoir dépanner les problèmes de réseau avec une plus grande fluidité et facilité.

Tous hail l'Internet !

## Prérequis

Vous n'avez besoin d'aucune expérience préalable en programmation ou en mise en réseau pour comprendre cet article. Cependant, vous aurez besoin de :

* Une familiarité de base avec les termes courants de mise en réseau (expliqués ci-dessous)
* Une curiosité sur le fonctionnement des choses :)

## Objectifs d'apprentissage

Au cours de cet article, vous apprendrez :

1. Ce qu'est le modèle OSI
2. Le but de chacune des 7 couches
3. Les problèmes qui peuvent survenir à chacune des 7 couches
4. La différence entre le modèle TCP/IP et le modèle OSI

## Termes courants de mise en réseau

Voici quelques termes courants de mise en réseau que vous devriez connaître pour tirer le meilleur parti de cet article. J'utiliserai ces termes lorsque je parlerai des couches OSI ensuite.

### Nœuds

Un nœud est un appareil électronique physique connecté à un réseau, par exemple un ordinateur, une imprimante, un routeur, etc. Si configuré correctement, un nœud est capable d'envoyer et/ou de recevoir des informations sur un réseau.

Les nœuds peuvent être configurés adjacents les uns aux autres, où le Nœud A peut se connecter directement au Nœud B, ou il peut y avoir un nœud intermédiaire, comme un commutateur ou un routeur, configuré entre le Nœud A et le Nœud B.

Typiquement, les routeurs connectent les réseaux à l'Internet et les commutateurs fonctionnent au sein d'un réseau pour faciliter la communication intra-réseau. [En savoir plus sur le hub vs. le commutateur vs. le routeur.](https://www.themillergroup.com/differences-hubs-switches-routers/)

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/1-Router-Image.jpeg)
_[Source](https://www.oreilly.com/library/view/the-illustrated-network/9780128110287/xhtml/chp001.xhtml)_

_Pour les pointilleux parmi nous (oui, je vous vois), **hôte** est un autre terme que vous rencontrerez en mise en réseau. Je définirai un hôte comme un type de nœud qui nécessite une adresse IP. Tous les hôtes sont des nœuds, mais tous les nœuds ne sont pas des hôtes. Veuillez tweeter avec colère contre moi si vous n'êtes pas d'accord._

### Liens

Les liens connectent les nœuds sur un réseau. Les liens peuvent être filaires, comme Ethernet, ou sans fil, comme WiFi.

Les liens peuvent être soit point à point, où le Nœud A est connecté au Nœud B, ou multipoints, où le Nœud A est connecté au Nœud B et au Nœud C.

Lorsque nous parlons de l'information transmise, cela peut également être décrit comme une relation un-à-un vs. un-à-plusieurs.

### Protocole

Un protocole est un ensemble de règles convenues mutuellement qui permet à deux nœuds sur un réseau d'échanger des données.

> "Un protocole définit les règles régissant la syntaxe (ce qui peut être communiqué), la sémantique (comment cela peut être communiqué), et la synchronisation (quand et à quelle vitesse cela peut être communiqué) de la procédure de communication. Les protocoles peuvent être implémentés sur du matériel, des logiciels, ou une combinaison des deux. Les protocoles peuvent être créés par n'importe qui, mais les protocoles les plus largement adoptés sont basés sur des normes." - The Illustrated Network.

Les liens filaires et sans fil peuvent avoir des protocoles.

Bien que n'importe qui puisse créer un protocole, les protocoles les plus largement adoptés sont souvent basés sur des normes publiées par des organisations Internet telles que l'Internet Engineering Task Force (IETF).

### Réseaux

Un réseau est un terme général pour un groupe d'ordinateurs, d'imprimantes, ou tout autre appareil qui souhaite partager des données.

Les types de réseaux incluent LAN, HAN, CAN, MAN, WAN, BAN, ou VPN. Pensez-vous que je fais simplement rimer des choses avec le mot _can_ ? Je ne peux pas dire que je le fais - ce sont tous de vrais types de réseaux. [En savoir plus ici](https://www.c1c.net/blog/network-101/).

### Topologie

La topologie décrit comment les nœuds et les liens s'emboîtent dans une configuration de réseau, souvent représentée dans un diagramme. Voici quelques types courants de topologie de réseau :

![Qu'est-ce que la topologie de réseau ? Meilleurs guides des types et diagrammes - DNSstuff](https://www.freecodecamp.org/news/content/images/2021/11/2-Network-Topology-Types.png)
_[en savoir plus sur les topologies de réseau ici](https://www.dnsstuff.com/what-is-network-topology">Source</a> + <a href="https://www.geeksforgeeks.org/types-of-network-topology/)_

_Un réseau se compose de nœuds, de liens entre les nœuds, et de protocoles qui régissent la transmission de données entre les nœuds._

À quelque échelle et complexité que les réseaux atteignent, vous comprendrez ce qui se passe dans tous les réseaux informatiques en apprenant le modèle OSI et les 7 couches de la mise en réseau.

# Qu'est-ce que le modèle OSI ?

Le modèle OSI se compose de 7 couches de mise en réseau.

Tout d'abord, qu'est-ce qu'une couche ?

![Grotte, Repaire de dragon, montagnes](https://www.freecodecamp.org/news/content/images/2021/11/3-Dragon-Lair.jpeg)
_[Source](https://pixabay.com/photos/cave-dragon-cave-mountains-1766835/)_

Ooo, repaire.

Non, une couche - pas un _repaire_. Ici, il n'y a pas de dragons.

_Une couche est un moyen de catégoriser et de regrouper les fonctionnalités et les comportements sur et d'un réseau._

Dans le modèle OSI, les couches sont organisées du plus tangible et du plus physique, au moins tangible et au moins physique mais plus proche de l'utilisateur final.

Chaque couche _abstrait_ les fonctionnalités de niveau inférieur jusqu'à ce que, lorsque vous atteignez la couche la plus élevée, tous les détails et le fonctionnement interne de toutes les autres couches soient cachés à l'utilisateur final.

Comment se souvenir de tous les noms des couches ? Facile.

* **S'il vous plaît** | Couche Physique
* **Faites** | Couche de Liaison de Données
* **Ne** | Couche Réseau
* **Dites** (le) | Couche Transport
* **Secret** | Couche Session
* **Mot de passe** (à) | Couche Présentation
* **À personne** | Couche Application

_Gardez à l'esprit que bien que certaines technologies, comme les protocoles, puissent logiquement "appartenir" à une couche plus qu'à une autre, toutes les technologies ne s'intègrent pas parfaitement dans une seule couche du modèle OSI. Par exemple, Ethernet, 802.11 (Wifi) et la procédure du protocole de résolution d'adresse (ARP) fonctionnent sur >1 couche._

L'OSI est un modèle et un outil, pas un ensemble de règles.

## Couche OSI 1

La couche 1 est la **couche physique**. Il y a beaucoup de technologie dans la couche 1 - tout, des appareils réseau physiques, du câblage, à la manière dont les câbles se connectent aux appareils. Plus, si nous n'avons pas besoin de câbles, quel est le type de signal et les méthodes de transmission (par exemple, le haut débit sans fil).

Au lieu de lister chaque type de technologie dans la couche 1, j'ai créé des catégories plus larges pour ces technologies. J'encourage les lecteurs à en apprendre davantage sur chacune de ces catégories :

* **Nœuds (appareils) et composants matériels de mise en réseau.** Les appareils incluent les hubs, répéteurs, routeurs, ordinateurs, imprimantes, etc. Les composants matériels qui résident à l'intérieur de ces appareils incluent les antennes, amplificateurs, cartes d'interface réseau (NIC), et plus.
* **Mécanismes d'interface des appareils.** Comment et où un câble se connecte à un appareil (connecteur de câble et prise de l'appareil) ? Quelle est la taille et la forme du connecteur, et combien de broches possède-t-il ? Qu'est-ce qui dicte quand une broche est active ou inactive ?
* **Logique fonctionnelle et procédurale.** Quelle est la fonction de chaque broche dans le connecteur - envoyer ou recevoir ? Quelle logique procédurale dicte la séquence d'événements pour qu'un nœud puisse commencer à communiquer avec un autre nœud sur la couche 2 ?
* **Protocoles et spécifications de câblage.** Ethernet (CAT), USB, [Ligne d'abonné numérique (DSL)](https://www.centurylink.com/home/help/internet/what-is-DSL.html), et plus. Les spécifications incluent la longueur maximale du câble, les techniques de modulation, les spécifications radio, le codage de ligne, et la synchronisation des bits (plus sur cela ci-dessous).
* **Types de câbles.** Les options incluent la paire torsadée blindée ou non blindée, la paire non torsadée, le coaxial et ainsi de suite. [En savoir plus sur les types de câbles ici](https://www.computernetworkingnotes.com/networking-tutorials/network-cable-types-and-specifications.html).
* **Type de signal.** La bande de base est un flux de bits unique à la fois, comme une voie ferrée - sens unique uniquement. Le haut débit consiste en plusieurs flux de bits en même temps, comme une autoroute bidirectionnelle.
* **Méthode de transmission du signal (peut être filaire ou sans fil).** Les options incluent l'électricité (Ethernet), la lumière (réseaux optiques, fibre optique), les ondes radio (802.11 WiFi, variantes a/b/g/n/ac/ax ou Bluetooth). Si sans fil, alors considérer également la fréquence : 2,5 GHz vs. 5 GHz. Si câblé, considérer la tension. Si câblé et Ethernet, considérer également les normes de mise en réseau comme 100BASE-T et les normes connexes.

L'unité de données sur la couche 1 est le bit.

Un bit est la plus petite unité d'information numérique transmissible. Les bits sont binaires, donc soit un 0 soit un 1. Les octets, composés de 8 bits, sont utilisés pour représenter des caractères uniques, comme une lettre, un chiffre ou un symbole.

Les bits sont envoyés vers et depuis les appareils matériels conformément au débit de données pris en charge (taux de transmission, en nombre de bits par seconde ou milliseconde) et sont synchronisés de sorte que le nombre de bits envoyés et reçus par unité de temps reste constant (cela s'appelle la synchronisation des bits). La manière dont les bits sont transmis dépend de la méthode de transmission du signal.

Les nœuds peuvent envoyer, recevoir ou envoyer et recevoir des bits. S'ils ne peuvent faire qu'une seule chose, alors le nœud utilise un mode simplex. S'ils peuvent faire les deux, alors le nœud utilise un mode duplex. Si un nœud peut envoyer et recevoir en même temps, c'est un full-duplex - sinon, c'est juste un half-duplex.

L'Ethernet original était half-duplex. L'Ethernet full-duplex est une option maintenant, avec le bon équipement.

### Comment dépanner les problèmes de la couche OSI 1

Voici quelques problèmes de la couche 1 à surveiller :

* Câbles défectueux, par exemple fils endommagés ou connecteurs cassés
* Appareils réseau matériels cassés, par exemple circuits endommagés
* Choses débranchées (... nous y avons tous été)

S'il y a des problèmes dans la couche 1, tout ce qui est au-delà de la couche 1 ne fonctionnera pas correctement.

### TL;DR

_La couche 1 contient l'infrastructure qui rend la communication sur les réseaux possible._

_Elle définit les spécifications électriques, mécaniques, procédurales et fonctionnelles pour activer, maintenir et désactiver les liens physiques entre les appareils réseau. -_ [Source](https://learning.oreilly.com/videos/wireshark-for-packet/9781839212352/9781839212352-video3_11)

Fait amusant : les câbles de communication sous-marins transmettent des données autour du monde. Cette carte va vous souffler l'esprit : [https://www.submarinecablemap.com/](https://www.submarinecablemap.com/)

Et parce que vous êtes arrivé jusqu'ici, voici un koala :

![Gros plan d'un Koala](https://www.freecodecamp.org/news/content/images/2021/11/4-Koala.jpeg)
_[Source](https://pixabay.com/photos/koala-nature-animals-legs-630117/)_

## Couche OSI 2

La couche 2 est la **couche de liaison de données**. La couche 2 définit comment les données sont formatées pour la transmission, combien de données peuvent circuler entre les nœuds, pendant combien de temps, et quoi faire lorsque des erreurs sont détectées dans ce flux.

En termes techniques plus officiels :

* **Discipline de ligne.** Qui devrait parler pendant combien de temps ? Pendant combien de temps les nœuds devraient-ils pouvoir transmettre des informations ?
* **Contrôle de flux.** Combien de données devraient être transmises ?
* **Contrôle des erreurs - détection et correction.** Toutes les méthodes de transmission de données ont un potentiel d'erreurs, des pics électriques aux connecteurs sales. Une fois que les technologies de la couche 2 informent les administrateurs réseau d'un problème sur la couche 2 ou la couche 1, l'administrateur système peut corriger ces erreurs sur les couches suivantes. La couche 2 est principalement concernée par la détection des erreurs, pas par la correction des erreurs. ([Source](https://learning.oreilly.com/videos/wireshark-for-packet/9781839212352/9781839212352-video3_10))

Il y a deux sous-couches distinctes au sein de la couche 2 :

* **Contrôle d'accès au support (MAC)** : la sous-couche MAC gère l'attribution d'un numéro d'identification matériel, appelé adresse MAC, qui identifie de manière unique chaque appareil sur un réseau. Aucun deux appareils ne devraient avoir la même adresse MAC. L'adresse MAC est attribuée au point de fabrication. Elle est automatiquement reconnue par la plupart des réseaux. Les adresses MAC résident sur les cartes d'interface réseau (NIC). Les commutateurs gardent une trace de toutes les adresses MAC sur un réseau. En savoir plus sur les adresses MAC sur [PC Mag](https://www.pcmag.com/encyclopedia/term/mac-address) et [dans cet article](https://people.richland.edu/dkirby/141macaddress.htm). [En savoir plus sur les commutateurs réseau ici](https://www.networkworld.com/article/3584876/what-is-a-network-switch-and-how-does-it-work.html).
* **Contrôle de liaison logique (LLC)** : la sous-couche LLC gère l'adressage et le contrôle de flux des trames. La vitesse dépend du lien entre les nœuds, par exemple Ethernet ou Wifi.

L'unité de données sur la couche 2 est une _trame_.

Chaque trame contient un en-tête de trame, un corps et un pied de trame :

* En-tête : contient généralement les adresses MAC des nœuds source et destination.
* Corps : se compose des bits transmis.
* Pied : contient des informations de détection d'erreurs. Lorsque des erreurs sont détectées, et selon l'implémentation ou la configuration d'un réseau ou d'un protocole, les trames peuvent être rejetées ou l'erreur peut être signalée aux couches supérieures pour une correction d'erreur supplémentaire. Exemples de mécanismes de détection d'erreurs : Vérification de redondance cyclique (CRC) et Séquence de vérification de trame (FCS). [En savoir plus sur les techniques de détection d'erreurs ici](http://www.msc.uky.edu/ken/cs471/notes/chap5.htm).

![Exemple de trames, de la couche réseau et de la couche physique](https://www.freecodecamp.org/news/content/images/2021/11/5-Frame-Example.jpeg)
_[Source](https://learning.oreilly.com/library/view/the-illustrated-network/9780128110287/xhtml/chp001.xhtml)_

Typiquement, il y a une limite de taille de trame maximale, appelée Unité de Transmission Maximale, MTU. Les trames jumbo dépassent le MTU standard, [en savoir plus sur les trames jumbo ici](https://kb.netgear.com/25091/Guidance-on-the-use-of-jumbo-frames).

### Comment dépanner les problèmes de la couche OSI 2

Voici quelques problèmes de la couche 2 à surveiller :

* Tous les problèmes qui peuvent survenir sur la couche 1
* Connexions (sessions) infructueuses entre deux nœuds
* Sessions qui sont établies avec succès mais qui échouent de manière intermittente
* Collisions de trames

### TL;DR

_La couche de liaison de données permet aux nœuds de communiquer entre eux au sein d'un réseau local. Les fondements de la discipline de ligne, du contrôle de flux et du contrôle des erreurs sont établis dans cette couche._

## Couche OSI 3

La couche 3 est la **couche réseau**. C'est ici que nous envoyons des informations _entre et à travers_ les réseaux grâce à l'utilisation de routeurs. Au lieu de simplement communiquer de nœud à nœud, nous pouvons maintenant faire de la communication de réseau à réseau.

Les routeurs sont le cheval de bataille de la couche 3 - nous ne pourrions pas avoir la couche 3 sans eux. Ils déplacent les paquets de données à travers plusieurs réseaux.

Non seulement ils se connectent aux fournisseurs de services Internet (FAI) pour fournir l'accès à l'Internet, mais ils gardent également une trace de ce qui se trouve sur son réseau (rappelons que les commutateurs gardent une trace de toutes les adresses MAC sur un réseau), des autres réseaux auxquels il est connecté, et des différents chemins pour acheminer les paquets de données à travers ces réseaux.

Les routeurs stockent toutes ces informations d'adressage et de routage dans des tables de routage.

Voici un exemple simple de table de routage :

![Une table de routage montrant la destination, le masque de sous-réseau et l'interface](https://www.freecodecamp.org/news/content/images/2021/11/6-Routing-Table.png)
_[Source + en savoir plus sur les tables de routage ici](https://www.geeksforgeeks.org/routing-tables-in-computer-network/)_

L'unité de données sur la couche 3 est le _paquet de données_. Typiquement, chaque paquet de données contient une trame **plus** un enveloppeur d'informations d'adresse IP. En d'autres termes, les trames sont encapsulées par les informations d'adressage de la couche 3.

Les données transmises dans un paquet sont également parfois appelées la _charge utile_. Bien que chaque paquet ait tout ce dont il a besoin pour atteindre sa destination, le fait qu'il y arrive ou non est une autre histoire.

Les transmissions de la couche 3 sont sans connexion, ou au mieux - elles ne font rien d'autre qu'envoyer le trafic là où il est censé aller. Plus sur les protocoles de transport de données sur la couche 4.

Une fois qu'un nœud est connecté à l'Internet, il se voit attribuer une adresse de protocole Internet (IP), qui ressemble soit à 172.16.254.1 (convention d'adresse IPv4) soit à 2001:0db8:85a3:0000:0000:8a2e:0370:7334 (convention d'adresse IPv6). Les routeurs utilisent les adresses IP dans leurs tables de routage.

Les adresses IP sont associées à l'adresse MAC du nœud physique via le protocole de résolution d'adresse (ARP), qui résout les adresses MAC avec l'adresse IP correspondante du nœud.

ARP est conventionnellement considéré comme faisant partie de la couche 2, mais comme les adresses IP n'existent pas avant la couche 3, il fait également partie de la couche 3.

### Comment dépanner les problèmes de la couche OSI 3

Voici quelques problèmes de la couche 3 à surveiller :

* Tous les problèmes qui peuvent survenir sur les couches précédentes :)
* Routeur ou autre nœud défectueux ou non fonctionnel
* Adresse IP incorrectement configurée

De nombreuses réponses aux questions de la couche 3 nécessiteront l'utilisation d'outils en ligne de commande comme _ping_, _trace_, _show ip route_, ou _show ip protocols_. [En savoir plus sur le dépannage des couches 1-3 ici](https://www.pearsonitcertification.com/articles/article.aspx?p=2873377).

### TL;DR

_La couche réseau permet aux nœuds de se connecter à l'Internet et d'envoyer des informations à travers différents réseaux._

## Couche OSI 4

La couche 4 est la **couche transport**. C'est ici que nous plongeons dans les spécificités de la connexion entre deux nœuds et comment l'information est transmise entre eux. Elle s'appuie sur les fonctions de la couche 2 - discipline de ligne, contrôle de flux et contrôle des erreurs.

Cette couche est également responsable de la segmentation des paquets de données, ou comment les paquets de données sont divisés et envoyés sur le réseau.

Contrairement à la couche précédente, la couche 4 a également une compréhension de l'ensemble du message, et pas seulement du contenu de chaque paquet de données individuel. Avec cette compréhension, la couche 4 est capable de gérer la congestion du réseau en n'envoyant pas tous les paquets en même temps.

Les unités de données de la couche 4 portent plusieurs noms. Pour TCP, l'unité de données est un paquet. Pour UDP, un paquet est appelé un datagramme. Je vais simplement utiliser le terme paquet de données ici pour simplifier.

Le protocole de contrôle de transmission (TCP) et le protocole de datagramme utilisateur (UDP) sont deux des protocoles les plus connus de la couche 4.

TCP, un protocole orienté connexion, privilégie la qualité des données par rapport à la vitesse.

TCP établit explicitement une connexion avec le nœud de destination et nécessite une poignée de main entre les nœuds source et destination lorsque des données sont transmises. La poignée de main confirme que les données ont été reçues. Si le nœud de destination ne reçoit pas toutes les données, TCP demandera une nouvelle tentative.

TCP garantit également que les paquets sont livrés ou réassemblés dans le bon ordre. [En savoir plus sur TCP ici](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/).

UDP, un protocole sans connexion, privilégie la vitesse par rapport à la qualité des données. UDP ne nécessite pas de poignée de main, c'est pourquoi il est appelé sans connexion.

Parce que UDP n'a pas à attendre cette confirmation, il peut envoyer des données à un rythme plus rapide, mais toutes les données ne sont pas nécessairement transmises avec succès et nous ne le saurions jamais.

Si les informations sont divisées en plusieurs datagrammes, sauf si ces datagrammes contiennent un numéro de séquence, UDP ne garantit pas que les paquets sont réassemblés dans le bon ordre. [En savoir plus sur UDP ici](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/).

TCP et UDP envoient tous deux des données à des ports spécifiques sur un appareil réseau, qui a une adresse IP. La combinaison de l'adresse IP et du numéro de port est appelée une socket.

[En savoir plus sur les sockets ici](https://www.dummies.com/programming/networking/cisco/network-basics-tcpudp-socket-and-port-overview/).

[En savoir plus sur les différences et similitudes entre ces deux protocoles ici](https://www.pearsonitcertification.com/articles/article.aspx?p=2873377).

### Comment dépanner les problèmes de la couche OSI 4

Voici quelques problèmes de la couche 4 à surveiller :

* Tous les problèmes qui peuvent survenir sur les couches précédentes :)
* Ports bloqués - vérifiez vos listes de contrôle d'accès (ACL) et pare-feux
* Paramètres de Qualité de Service (QoS). QoS est une fonctionnalité des routeurs/commutateurs qui peut prioriser le trafic, et ils peuvent vraiment tout gâcher. [En savoir plus sur QoS ici](https://www.pcworld.com/article/2689995/quality-of-service-explained-how-routers-with-strong-qos-make-better-home-networks.html).

### TL;DR

_La couche transport fournit une transmission de bout en bout d'un message en segmentant un message en plusieurs paquets de données ; la couche prend en charge la communication orientée connexion et sans connexion._

## Couche OSI 5

La couche 5 est la **couche session**. Cette couche établit, maintient et termine les sessions.

Une session est une connexion convenue mutuellement qui est établie entre deux applications réseau. Pas deux nœuds ! Non, nous avons dépassé les nœuds. Ils étaient _tellement_ couche 4.

Je plaisante, nous avons toujours des nœuds, mais la couche 5 n'a pas besoin de retenir le concept d'un nœud car cela a été abstrait (pris en charge) par les couches précédentes.

Ainsi, une session est une connexion qui est établie entre deux applications spécifiques de l'utilisateur final. Il y a deux concepts importants à considérer ici :

* Modèle client et serveur : l'application qui demande l'information est appelée le client, et l'application qui possède l'information demandée est appelée le serveur.
* Modèle de demande et de réponse : pendant qu'une session est établie et pendant une session, il y a un échange constant de demandes d'information et de réponses contenant cette information ou "hé, je n'ai pas ce que vous demandez."

Les sessions peuvent être ouvertes pendant un très court laps de temps ou un long laps de temps. Elles peuvent également échouer parfois.

Selon le protocole en question, divers processus de résolution des échecs peuvent se déclencher. Selon les applications/protocoles/matériels utilisés, les sessions peuvent prendre en charge les modes simplex, half-duplex ou full-duplex.

Des exemples de protocoles sur la couche 5 incluent le système de base d'entrée/sortie réseau (NetBIOS) et le protocole d'appel de procédure à distance (RPC), et bien d'autres.

À partir de maintenant (couche 5 et au-delà), les réseaux se concentrent sur les moyens d'établir des connexions avec les applications de l'utilisateur final et d'afficher les données à l'utilisateur.

### Comment dépanner les problèmes de la couche OSI 5

Voici quelques problèmes de la couche 5 à surveiller :

* Serveurs indisponibles
* Serveurs incorrectement configurés, par exemple les configurations Apache ou PHP
* Échec de session - déconnexion, délai d'attente, etc.

### TL;DR

_La couche session initie, maintient et termine les connexions entre deux applications de l'utilisateur final. Elle répond aux demandes de la couche présentation et émet des demandes à la couche transport._

## Couche OSI 6

La couche 6 est la **couche présentation**. Cette couche est responsable du formatage des données, tel que le codage des caractères et les conversions, et du chiffrement des données.

Le système d'exploitation qui héberge l'application de l'utilisateur final est généralement impliqué dans les processus de la couche 6. Cette fonctionnalité n'est pas toujours implémentée dans un protocole réseau.

La couche 6 veille à ce que les applications de l'utilisateur final fonctionnant sur la couche 7 puissent consommer avec succès les données et, bien sûr, éventuellement les afficher.

Il y a trois méthodes de formatage des données à connaître :

* Code standard américain pour l'échange d'informations (ASCII) : cette technique de codage sur 7 bits est la norme la plus largement utilisée pour le codage des caractères. Un sur-ensemble est l'ISO-8859-1, qui fournit la plupart des caractères nécessaires pour les langues parlées en Europe de l'Ouest.
* Code d'échange décimal codé binaire étendu (EBDCIC) : conçu par IBM pour une utilisation sur mainframe. Ce codage est incompatible avec d'autres méthodes de codage des caractères.
* Unicode : les codages de caractères peuvent être effectués avec des caractères de 32, 16 ou 8 bits et tentent de prendre en charge chaque alphabet écrit connu.

En savoir plus sur les méthodes de codage des caractères [dans cet article](https://www.smashingmagazine.com/2012/06/all-about-unicode-utf8-character-sets/), [et aussi ici](https://www.smashingmagazine.com/2012/06/all-about-unicode-utf8-character-sets/).

Chiffrement : les protocoles de chiffrement SSL ou TLS résident sur la couche 6. Ces protocoles de chiffrement aident à garantir que les données transmises sont moins vulnérables aux acteurs malveillants en fournissant une authentification et un chiffrement des données pour les nœuds fonctionnant sur un réseau. TLS est le successeur de SSL.

### Comment dépanner les problèmes de la couche OSI 6

Voici quelques problèmes de la couche 6 à surveiller :

* Pilotes inexistants ou corrompus
* Niveau d'accès utilisateur OS incorrect

### TL;DR

_La couche présentation formate et chiffrer les données._

## Couche OSI 7

La couche 7 est la **couche application**.

Fidèle à son nom, c'est la couche qui est finalement responsable de la prise en charge des services utilisés par les applications de l'utilisateur final. Les applications incluent des programmes logiciels qui sont installés sur le système d'exploitation, comme les navigateurs Internet (par exemple, Firefox) ou les programmes de traitement de texte (par exemple, Microsoft Word).

Les applications peuvent effectuer des fonctions réseau spécialisées sous le capot et nécessitent des services spécialisés qui relèvent de la couche 7.

Les programmes de messagerie électronique, par exemple, sont spécifiquement créés pour fonctionner sur un réseau et utiliser la fonctionnalité de mise en réseau, telle que les protocoles de messagerie électronique, qui relèvent de la couche 7.

Les applications contrôleront également l'interaction de l'utilisateur final, telle que les vérifications de sécurité (par exemple, MFA), l'identification des deux participants, l'initiation d'un échange d'informations, et ainsi de suite.

Les protocoles qui fonctionnent à ce niveau incluent le protocole de transfert de fichiers (FTP), le protocole de shell sécurisé (SSH), le protocole de transfert de courrier simple (SMTP), le protocole d'accès aux messages Internet (IMAP), le service de noms de domaine (DNS) et le protocole de transfert hypertexte (HTTP).

Bien que chacun de ces protocoles serve des fonctions différentes et fonctionne différemment, à un niveau élevé, ils facilitent tous la communication d'informations. ([Source](https://jaimelightfoot.com/blog/osi-model/))

### Comment dépanner les problèmes de la couche OSI 7

Voici quelques problèmes de la couche 7 à surveiller :

* Tous les problèmes des couches précédentes
* Applications logicielles incorrectement configurées
* Erreur de l'utilisateur (... nous y avons tous été)

### TL;DR

_La couche application possède les services et fonctions dont les applications de l'utilisateur final ont besoin pour fonctionner. Elle n'inclut pas les applications elles-mêmes._

# **Conclusion**

Notre koala de la couche 1 est tout grandi.

![Koala avec maquillage Photoshopé](https://www.freecodecamp.org/news/content/images/2021/11/6-Koala-Makeup.jpeg)

Vérification de l'apprentissage - pouvez-vous appliquer du maquillage à un koala ?

Vous n'avez pas de koala ?

Eh bien - répondez à ces questions à la place. C'est la meilleure chose suivante, je vous le promets.

* Qu'est-ce que le modèle OSI ?
* Quelles sont chacune des couches ?
* Comment pourrais-je utiliser ces informations pour dépanner les problèmes de réseau ?

Félicitations - vous avez fait un pas de plus vers la compréhension de l'entité glorieuse que nous appelons l'Internet.

## **Ressources d'apprentissage**

Beaucoup de gens _très_ intelligents ont écrit des livres entiers sur le modèle OSI ou des livres entiers sur des couches spécifiques. J'encourage les lecteurs à consulter les livres publiés par O'Reilly sur le sujet ou sur l'ingénierie réseau en général.

Voici quelques ressources que j'ai utilisées lors de la rédaction de cet article :

* The Illustrated Network, 2nd Edition
* Unité de données de protocole (PDU) : [https://www.geeksforgeeks.org/difference-between-segments-packets-and-frames/](https://www.geeksforgeeks.org/difference-between-segments-packets-and-frames/)
* Dépannage le long du modèle OSI : [https://www.pearsonitcertification.com/articles/article.aspx?p=1730891](https://www.pearsonitcertification.com/articles/article.aspx?p=1730891)
* Le modèle OSI démystifié : [https://www.youtube.com/watch?v=HEEnLZV2wGI](https://www.youtube.com/watch?v=HEEnLZV2wGI)
* Modèle OSI pour les nuls : [https://www.dummies.com/programming/networking/layers-in-the-osi-model-of-a-computer-network/](https://www.dummies.com/programming/networking/layers-in-the-osi-model-of-a-computer-network/)

### À propos de moi

Chloe Tucker est une artiste et une passionnée d'informatique basée à Portland, Oregon. En tant qu'ancienne éducatrice, elle recherche continuellement l'intersection de l'apprentissage et de l'enseignement, ou de la technologie et de l'art. Contactez-la sur Twitter [@_chloetucker](https://twitter.com/_chloetucker) et consultez son site web à l'adresse [chloe.dev](https://chloe.dev/).