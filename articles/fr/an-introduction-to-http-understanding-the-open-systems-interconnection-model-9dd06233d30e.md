---
title: 'Une introduction à HTTP : Exploration de la télécommunication dans les systèmes
  informatiques'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T16:29:27.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7pzeTboIfH5UxaFnVnGhnA.jpeg
tags:
- name: https
  slug: https
- name: network
  slug: network
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction à HTTP : Exploration de la télécommunication dans les
  systèmes informatiques'
seo_desc: 'By Cher Don

  Get to know the Open Systems Interconnection model


  Overview

  Throughout this series, we will be tackling the basics such as:(Part 1) How does
  DNS work?(Part 2) Network Stack, OSI Model [You are here!](Part 3) HTTP Methods
  and Formats(Part...'
---

Par Cher Don

#### Découvrez le modèle d'interconnexion des systèmes ouverts

![Image](https://cdn-media-1.freecodecamp.org/images/AboxQNs-z1kZCMDrUuPqdsHzdyVLBBE5MeFL)

### Aperçu

Tout au long de cette série, nous aborderons les bases telles que :   
[(Partie 1) Comment fonctionne le DNS ?](https://medium.freecodecamp.org/an-introduction-to-http-domain-name-system-servers-b3e7060eca98)   
(Partie 2) Pile réseau, modèle OSI _[Vous êtes ici !]_  
(Partie 3) Méthodes et formats HTTP   
(Partie 4) Identification du client   
(Partie 5) Authentification Basic/Digest   
(Partie 6) HTTPS fonctionnant avec SSL/TLS

### Modèle OSI

Le modèle d'interconnexion des systèmes ouverts (OSI) est un modèle standardisé pour la télécommunication dans les systèmes informatiques. Il ne tient pas compte de la technologie sous-jacente, mais plutôt des couches impliquées dans la communication. Explorons les différentes couches du modèle OSI :

![Image](https://cdn-media-1.freecodecamp.org/images/Yc4ZTugFjR4A1zuGQqAQbN6Ez77yBttblRUI)
_Modèle OSI typique à 5 couches_

### 1. Couche Application

Cette couche permet aux applications de communiquer sur le réseau une fois la connexion établie, comme par exemple du navigateur Web (Application) au Serveur. Des exemples de protocoles de cette couche incluent HTTP et TELNET.

#### HyperText Transfer Protocol (HTTP)

Un ensemble de règles pour transférer des fichiers sur Internet. Par exemple, lorsque vous entrez l'URL dans le navigateur, le navigateur envoie une requête HTTP pour la page web. L'hôte renvoie ensuite la page web, ainsi que tous les éléments qu'elle contient, tels que des images, du texte, des vidéos, des polices de style, etc.

### 2. Couche Transport

Cette couche est responsable de la communication de messages de hôte à hôte. Des exemples de protocoles de cette couche incluent TCP et UDP.

#### Transmission Control Protocol (TCP)

Le protocole orienté connexion le plus courant. Il définit comment établir et maintenir une conversation réseau. Il est responsable de l'établissement d'une connexion (appelée _socket_) entre le client et l'hôte dans un handshake à trois voies.

![Image](https://cdn-media-1.freecodecamp.org/images/aZwDUnYpTUmP4-20iIQpxYRqP2PGJRAI52N5)

L'utilisateur demandant les données enverra un paquet de données SYN au serveur, demandant une _synchronisation_. Le serveur répondra ensuite avec un SYN-ACK à l'utilisateur, indiquant qu'il a _accusé réception_ du paquet de données et qu'il souhaite également se connecter. La connexion est ainsi établie lorsque l'utilisateur envoie le dernier ACK au serveur.

TCP est le plus courant en raison de son élégance, car il est capable d'offrir ce qui suit :

**Communication orientée connexion**  
 Établir un protocole de handshake entre les points de terminaison pour garantir la connexion avant l'échange de données, et transmettre sous forme de flux de données (paquets de données).

**Fiabilité**  
En utilisant des sommes de contrôle, il garantit que les paquets de données transmis et reçus sont identiques. Si des paquets sont manquants/corrompus, il demandera une re-transmission des paquets de données en envoyant un message NACK à l'expéditeur.

**Ordre**  
Les paquets de données sont numérotés et transmis. Ainsi, TCP garantira que les paquets reçus sont réorganisés avant d'être livrés à l'application.

**Contrôle de flux**  
Le taux de transmission des données est régulé pour améliorer l'efficacité tout en prévenant les dépassements/sous-dépassements de tampon, où les données sont envoyées plus rapidement que le récepteur ne peut les traiter, et vice versa.  
Les mécanismes derrière cela sont expliqués ci-dessous dans la section [TCP Slow Start](#heading-installation).

**Multiplexage**  
En gros, il est capable d'envoyer plusieurs flux d'informations simultanément sur le même socket. Cela est fait via différents ports sur le socket. Nous discuterons des différences entre [Multiplexage et Pipelining](#8aeb) plus loin dans l'article.

#### User Datagram Protocol (UDP)

Bien que similaire à TCP, il s'agit d'un protocole sans connexion. Il est l'opposé complet de TCP, ce qui le rend non fiable et non ordonné. Les paquets perdus ne seront pas re-transmis, provoquant des lacunes dans les données.

![Image](https://cdn-media-1.freecodecamp.org/images/-YFU7rjDOESeBDk4iwsJJ3DXbF7kTF4FPKPQ)

Cependant, cela le rend idéal pour les applications sensibles au temps, telles que les appels vocaux sur Internet (VoIP). Cela est dû au fait qu'il ne nécessite pas le handshake à trois voies avant la transmission, ce qui le rend rapide. De plus, les paquets de données perdus ne posent pas de problème dans la VoIP, car l'oreille humaine est très bonne pour gérer les courts intervalles typiques des paquets perdus.

### 3. Couche Réseau

Cette couche est responsable de la fourniture de chemins de routage de données pour les connexions réseau. En gros, elle déplace les paquets de données à travers le réseau avec le chemin le plus logique.

#### Internet Protocol (IP)

Définir la structure des paquets de données, ainsi que les étiqueter avec les informations de source et de destination.

Les informations de source et de destination sont sous la forme d'adresses IP, qui peuvent être sous la forme `104.16.121.127` (IPv4), ou `2001:db8:0:1234:0:567:8:1` (IPv6).

### 4. Couche Liaison/Physique

Cette couche est la racine du modèle OSI, où les informations sont transmises soit dans le Réseau Local (LAN) pour la couche Liaison, et un signal physique tel qu'électrique, mécanique dans la couche Physique sous forme de mots de code ou de symboles.

### Visualisation des routes

En utilisant `tracert google.com`, la route peut être tracée du côté client (votre ordinateur) à l'hôte (google.com).

![Image](https://cdn-media-1.freecodecamp.org/images/hcYgb-j6sNT4L3em4eSD-K5DzC798H6zwYDn)

D'après ce qui précède, vous pouvez voir la route commençant depuis mon appareil `192.168.1.254` vers le routeur `10.243.128.1`, avant de passer par le Fournisseur de Services Internet (FAI) situé au Portugal, et ainsi de suite.

### Couches complémentaires

#### Modèle TCP/IP

![Image](https://cdn-media-1.freecodecamp.org/images/75nPgdIHhsTD5xSIbj1bTjRlNryTU3291Ndo)
_TCP demandera la re-transmission des paquets de données perdus et les réorganisera_

IP est uniquement responsable de la structure du paquet de données. Ainsi, il ne fera pas d'amendements si le paquet de données est corrompu ou perdu. C'est là que TCP entre en jeu, en numérotant les paquets de données avant de les envoyer au client. Du côté du client, TCP demandera la re-transmission des paquets perdus/corrompus, puis réorganisera les paquets de données.

#### Modèle HTTP/TCP

Comme nous l'avons mentionné précédemment, HTTP peut maintenant faire des requêtes via la connexion établie par [TCP Handshake](#heading-installation). Mais comment se complètent-ils ?

**Connexions HTTP persistantes**   
Cela permettrait plusieurs requêtes/réponses HTTP sur une seule connexion TCP, plutôt que d'ouvrir une nouvelle connexion à chaque requête/réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/-F9J9R9grtdhm7aQ1Y1ptqz1xL8Ft8c4x-0T)
_Exemple de réponse pour une connexion persistante_

Cela est fait via l'en-tête HTTP, où `Connection: Keep-Alive`. Par défaut, la connexion ne se fermera qu'après une autre réponse où `Connection: Close` est envoyé après 30 secondes d'inactivité.

**TCP Slow Start**  
Comme mentionné précédemment, TCP supporte le [contrôle de flux](#heading-installation). Cela est fait via TCP Slow Start, qui est une forme de prévention de la congestion du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/rV1aQqU5LxUsUJaX1-jDTn1VVCpKORoM10lb)

L'expéditeur a une fenêtre de congestion (CWND) et le récepteur a une fenêtre de réception (RWND). Si les données sont plus grandes que la fenêtre de congestion/réception, il y aurait un sous-dépassement/dépassement de tampon respectivement.

Pour éviter cela, l'expéditeur commencera par envoyer un paquet de données avec une petite fenêtre de congestion (CWND = 1), pour sonder lentement le récepteur pour sa fenêtre de réception.

Le récepteur répondra avec un accusé de réception, incitant l'expéditeur à doubler les paquets de données à chaque fois jusqu'à ce qu'aucun accusé de réception ne soit reçu. À ce stade, le nombre optimal de paquets de données a été découvert, permettant à d'autres algorithmes de contrôle de congestion de maintenir la connexion à cette vitesse.

**Travailler ensemble**  
Ainsi, TCP Slow Start est capable de déterminer le nombre optimal de paquets de données à envoyer avant que la connexion ne soit fermée. Cela permettra d'optimiser la quantité de données envoyées de l'hôte au client sans le risque de dépassement de tampon (les données sont envoyées plus rapidement qu'elles ne peuvent être reçues).

### Autres fonctionnalités HTTP

#### HTTP Pipelining

![Image](https://cdn-media-1.freecodecamp.org/images/Lw7lr7o1l1yyIyMDwRugYYE0DR4jjgNoxFuE)

Cette fonctionnalité dans la version HTTP/1.1 permet d'envoyer plusieurs requêtes à la fois sur le même socket, sans attendre de réponse. Cependant, elle a été remplacée par le Multiplexage TCP dans la nouvelle version HTTP/2.

La différence clé est que bien que les deux permettent plusieurs requêtes à la fois sur le même socket, le Pipelining nécessite toujours que les réponses soient envoyées dans l'ordre. Cela signifie que si les éléments demandés sont dans l'ordre (A, B, C), le client ne recevra pas l'élément C si l'élément B n'a pas été livré correctement.

Dans le Multiplexage, l'ordre n'a pas d'importance. Cela permettrait un temps de livraison plus rapide.

Ces méthodes sont mieux utilisées pour la méthode idempotente, qui sont des méthodes qui répondent indépendamment du nombre de fois demandées — par exemple, demander une page web plusieurs fois répondra à la même page web.

#### Connexions parallèles

Vous avez déjà ouvert une page web et vu plusieurs composants de la page web (barre vidéo, miniatures, boutons) se charger simultanément ?

![Image](https://cdn-media-1.freecodecamp.org/images/kSoqraJbI4QgwnlADZzo32d5E2dQb2408ODU)
_Multiples composants se chargeant simultanément | Photo gracieuseté de [Cloudflare Mobile SDK](https://www.cloudflare.com/products/mobile-sdk/" rel="noopener" target="_blank" title=")_

Cela est rendu possible avec les Connexions Parallèles, où il y a plus d'une connexion TCP établie en même temps, permettant à ces composants de se charger simultanément au lieu de l'un après l'autre.

Cependant, bien que cela puisse sembler se charger plus rapidement, cela peut être limité par la bande passante limitée du client. Si toutes les Connexions Parallèles sont en compétition pour la bande passante limitée, chaque composant se chargera proportionnellement plus lentement, résultant en aucun avantage en termes de vitesse de chargement totale.

### Conclusion

Avec le modèle OSI, nous pouvons facilement comprendre le tableau général des réseaux, et comment ils interagissent les uns avec les autres, du matériel au logiciel.

En général, c'est également un excellent outil d'enseignement ainsi qu'une référence pour le dépannage. Le modèle est également utile pour la conception, car il examine les fonctions à chaque couche, forçant à réfléchir sur la conception couche par couche.

Ce que j'ai couvert jusqu'à présent est le modèle OSI à 5 couches, alors qu'il existe également le [modèle OSI à 7 couches](https://www.webopedia.com/quick_ref/OSI_Layers.asp) qui traite également de l'identification, de l'authentification et du chiffrement des données.

Ceci est la partie 2 de la série d'introductions à HTTP. Vous pouvez lire le premier article sur l'importance des serveurs DNS dans la [Partie 1](https://medium.freecodecamp.org/an-introduction-to-http-domain-name-system-servers-b3e7060eca98). Explorons la structure des requêtes HTTP ensuite dans la Partie 3 !

Salut ! Je suis [Cher Don](https://www.freecodecamp.org/news/an-introduction-to-http-understanding-the-open-systems-interconnection-model-9dd06233d30e/undefined), actuellement en train de poursuivre un diplôme en science des données. Je suis le CTO de [Paralegal Bot](https://www.linkedin.com/company/paralegal-bot/), et vous pouvez trouver mon site web ci-dessous. Merci pour la lecture !

[**Piqued;**](http://www.piqued.co)  
[_Contenu de qualité Nous offrons le meilleur contenu pour les concepts difficiles à comprendre. Nous avons été là et avons ressenti la même chose que vous... www.piqued.co](http://www.piqued.co)