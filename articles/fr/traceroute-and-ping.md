---
title: Comment utiliser les commandes Traceroute et Ping pour résoudre les problèmes
  de connectivité réseau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-04T23:46:48.000Z'
originalURL: https://freecodecamp.org/news/traceroute-and-ping
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-pixabay-163064--1-.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Network Engineering
  slug: network-engineering
seo_title: Comment utiliser les commandes Traceroute et Ping pour résoudre les problèmes
  de connectivité réseau
seo_desc: "By Megan Kaczanowski\nPing and traceroute are common commands you can use\
  \ to troubleshoot network problems. \nPing is a simple command that can test the\
  \ reachability of a device on the network. \nTraceroute is a command you use to\
  \ 'trace' the route that..."
---

Par Megan Kaczanowski

Ping et traceroute sont des commandes courantes que vous pouvez utiliser pour résoudre les problèmes de réseau. 

Ping est une commande simple qui peut tester la joignabilité d'un appareil sur le réseau. 

Traceroute est une commande que vous utilisez pour "tracer" le chemin qu'un paquet emprunte lorsqu'il se rend à sa destination. Elle est utile pour tracer les problèmes de réseau, découvrir où les connexions échouent et identifier les problèmes de latence. 

## Comment fonctionne ping ? 

Ping utilise les messages ICMP (Internet Control Message Protocol) Echo pour voir si un hôte distant est actif ou inactif, combien de temps un message aller-retour prend pour atteindre l'hôte cible et revenir, et toute perte de paquets. 

Il envoie une requête et attend une réponse (qu'il reçoit si la destination répond dans le délai d'attente). 

C'est essentiellement un moyen rapide et facile de vérifier que vous pouvez atteindre une destination sur Internet. Si vous pouvez, c'est parfait ! Si ce n'est pas le cas, vous pouvez utiliser traceroute pour enquêter sur ce qui se passe à chaque étape entre votre appareil et la destination.

### Exemple de commande ping et résultats :

hostname ~ % ping -c 5 www.google.com

PING www.google.com (216.58.212.228): 56 data bytes

_La commande ping, configurée pour envoyer 5 paquets à google.com._

64 bytes from 216.58.212.228: icmp_seq=0 ttl=113 time=42.262 ms

64 bytes from 216.58.212.228: icmp_seq=1 ttl=113 time=34.796 ms

64 bytes from 216.58.212.228: icmp_seq=2 ttl=113 time=35.805 ms

64 bytes from 216.58.212.228: icmp_seq=3 ttl=113 time=45.299 ms

64 bytes from 216.58.212.228: icmp_seq=4 ttl=113 time=150.292 ms

_Ceci montre les résultats de chaque ping individuel, avec leur temps d'aller-retour en millisecondes._

--- www.google.com ping statistics ---

5 packets transmitted, 5 packets received, 0.0% packet loss

round-trip min/avg/max/stddev = 34.796/61.691/150.292/44.474 ms

_Les statistiques de l'ensemble du test - le temps minimum pour atteindre la destination, la moyenne, le maximum et l'écart type._

## Comment fonctionne traceroute ?

Par défaut, traceroute envoie trois paquets de données pour tester chaque "saut" (quand un paquet est passé entre des routeurs, cela s'appelle un "saut"). 

Il envoie d'abord 3 paquets à un port inaccessible sur l'hôte cible, chacun avec une valeur TTL (Time-To-Live) de 1. Cela signifie que dès qu'il atteint le premier routeur dans le chemin (dans votre réseau), il expirera. Le premier routeur répondra avec un message ICMP Time Exceeded Message (TEM), car le datagramme a expiré. 

Ensuite, 3 autres datagrammes sont envoyés, avec le TTL défini à 2, ce qui fait que le deuxième routeur (votre FAI) dans le chemin répond avec un ICMP TEM. 

Cela continue jusqu'à ce que les datagrammes aient finalement un TTL suffisamment long pour atteindre la destination. Lorsqu'ils y parviennent, comme les messages sont envoyés à un port invalide, un message ICMP port inaccessible est retourné, signalant que le traceroute est terminé. 

Dans ce cas, un message d'erreur est en fait un comportement attendu, et non un signe que quelque chose a mal tourné.

La partie la plus importante d'un traceroute est généralement les temps d'aller-retour. Idéalement, vous cherchez des temps cohérents tout au long de la trace. 

Si vous voyez des temps soudainement augmenter (latence élevée) sur un saut spécifique, et continuer à augmenter à mesure que la trace approche la cible, cela peut indiquer un problème commençant avec l'augmentation soudaine. 

Cependant, si une latence élevée se produit au milieu, mais reste cohérente vers la fin, ou si la latence élevée diminue vers la fin, cela n'indique pas nécessairement un problème.

Si vous voyez une latence élevée au début de la trace, cela peut indiquer un problème avec votre réseau local. Vous devriez travailler avec votre administrateur local (ou vous-même, si vous êtes votre propre administrateur local) pour le résoudre. Par défaut, Windows utilise ICMP pour transmettre les données tandis que Linux utilise UDP.

### Exemple de commande traceroute et résultat :

hostname ~ % traceroute www.google.com 

traceroute to www.google.com (216.58.212.228), 64 hops max, 52 byte packets

_La commande pour traceroute vers google._

1  homerouter.cpe (192.168.8.1)  10.129 ms  1.528 ms  1.373 ms

_Le premier saut est dans un réseau local. Ici, nous avons le numéro de saut (1), le nom de domaine/adresse IP (dans ce cas, un routeur domestique), puis RTT1, RTT2 et RTT3 (Round Trip Time - le temps qu'il faut pour qu'un paquet atteigne le saut et revienne à l'ordinateur, en millisecondes). C'est la latence du saut._ 

_Il y a trois nombres car, par défaut, la commande envoie trois paquets de données. En général, les temps supérieurs à 150 ms sont inhabituels pour un trajet dans les États-Unis continentaux, bien que les signaux traversant un océan puissent dépasser ce temps._

2  * * *

_Saut 2 : Il y a deux possibilités pour les étoiles comme celles-ci - soit ICMP/UDP n'étaient pas configurés sur l'appareil de réception et il n'a pas répondu, soit les paquets ont été abandonnés en raison d'un problème de réseau (comme un pare-feu ou des délais d'attente de paquets)._ 

_Dans ce cas, comme c'est très proche du début de la trace, il est probable que cela soit dû au fait que l'appareil n'est pas configuré pour envoyer des réponses à un traceroute._

3  192.168.213.21 (192.168.213.21)  26.641 ms  31.671 ms  26.824 ms

4  192.168.213.22 (192.168.213.22)  20.294 ms  22.496 ms  19.922 ms

5  * * *

6  * * *

_Ces étoiles, plus loin dans la trace, sont plus susceptibles d'être dues à un pare-feu de la cible bloquant les requêtes (bien que les requêtes HTTP devraient encore pouvoir être traitées dans la plupart des cas), un problème de connexion possible, ou un problème de chemin de retour (c'est-à-dire que le signal atteint le routeur, mais n'obtient pas de réponse)._

_La trace se poursuivra ensuite jusqu'à ce qu'elle atteigne la cible._

## Conclusion

En résumé, ping est un moyen (très) rapide de savoir si un hôte est joignable sur un réseau, tandis que traceroute peut vous aider à diagnostiquer les problèmes de connectivité. 

Ce sont deux commandes utiles à connaître, car comprendre comment elles fonctionnent et ce que signifie la sortie peut être très utile lors du dépannage de la connectivité réseau.

Vous devriez également savoir comment les utiliser pour les entretiens en réseau ou en sécurité, où des questions comme "sur quel port ping fonctionne-t-il (c'est une question piège car ping utilise ICMP) ?" sont couramment posées.