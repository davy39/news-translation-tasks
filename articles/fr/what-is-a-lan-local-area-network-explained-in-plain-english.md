---
title: Qu'est-ce qu'un LAN ? Le réseau local expliqué en termes simples
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-07-20T20:24:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-lan-local-area-network-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/server-311338_640.png
tags:
- name: computer networking
  slug: computer-networking
- name: network
  slug: network
seo_title: Qu'est-ce qu'un LAN ? Le réseau local expliqué en termes simples
seo_desc: 'A local area network (LAN) is really nothing more than a structure for
  organizing and protecting network communications for all the devices running within
  a single home or office.

  Let me break that down a bit. When I say, within a single home or offi...'
---

Un réseau local (LAN) n'est vraiment rien de plus qu'une structure pour organiser et protéger les communications réseau de tous les appareils fonctionnant au sein d'un seul foyer ou bureau.

Permettez-moi de décomposer cela un peu. Lorsque je dis, _au sein d'un seul foyer ou bureau_, je veux dire tous les appareils qui sont connectés via une connexion physique ou sans fil à un routeur réseau. Ce routeur peut être un point d'accès WiFi ou le modem que votre fournisseur de services Internet (FAI) vous a donné. 

Par _organiser_, je veux dire que chaque appareil se voit attribuer une adresse d'identification, et son accès à Internet au-delà de votre réseau local est défini. 

Et par _protéger_, je veux dire que, généralement, les demandes de trafic dirigées vers vos appareils depuis des réseaux externes seront analysées et filtrées pour aider à prévenir l'accès non autorisé et potentiellement dangereux. 

Basé en partie sur [le contenu de mon livre Linux in Action](https://www.amazon.com/gp/product/1617294934/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1617294934&linkCode=as2&tag=projemun-20&linkId=1a460c0cd9a39e01821133b90632cba8), je vais essayer d'expliquer comment tout cela fonctionne.

# Adressage IPv4

Voici à quoi cela pourrait ressembler. Le routeur dans cette image a une adresse IP _publique_ de 183.23.100.34 à laquelle tout le trafic entrant et sortant est associé. 

En même temps, le routeur agit comme un serveur de protocole de configuration dynamique des hôtes (DHCP), attribuant des adresses IP _privées_ à tous les PC, ordinateurs portables, smartphones et serveurs de la maison. Les appareils utiliseront ces adresses chaque fois qu'ils communiqueront entre eux.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/lan-figure1.png)
_Une topographie typique de réseau local (LAN)_

Remarquez comment tous les appareils locaux sont décrits comme utilisant quelque chose appelé "adresses IP NAT". NAT signifie Network Address Translation, et c'est la méthode utilisée pour organiser les appareils au sein d'un LAN privé. 

Mais pourquoi ? Qu'est-ce qui ne va pas avec le fait de donner à tous les appareils le même type d'adresse IP publique que le routeur ?

Au début, il y avait IPv4. Les adresses IPv4 sont des nombres de 32 bits composés de quatre octets de 8 bits séparés par des points. Voici à quoi cela pourrait ressembler :

```
192.168.1.10

```

# Notation de sous-réseau

Parce qu'il est extrêmement important de s'assurer que les systèmes savent quel type de sous-réseau une adresse réseau utilise, nous avons besoin d'une notation standard qui peut communiquer avec précision quels octets font partie du réseau et lesquels sont disponibles pour les appareils. 

Il existe deux normes couramment utilisées : la notation CIDR (Classless Inter-Domain Routing) et le masque de réseau. 

En utilisant CIDR, un réseau peut être représenté comme 192.168.1.0/24. Le /24 vous indique que les trois premiers octets (8×3=24) composent la partie réseau, ne laissant que le quatrième octet pour les adresses des appareils. Le deuxième réseau (ou sous-réseau), en CIDR, serait décrit comme 192.168.2.0/24.

Ces deux mêmes réseaux pourraient également être décrits par un masque de réseau de 255.255.255.0. Cela signifie que tous les 8 bits de chacun des trois premiers octets sont utilisés par le réseau, mais aucun du quatrième.

# Comprendre les réseaux privés

En théorie, le protocole IPv4 permet environ quatre milliards d'adresses uniques, allant de 1.0.0.0 à 255.255.255.255. 

Mais même si toutes ces quatre milliards d'adresses étaient pratiquement disponibles, cela ne suffirait toujours pas pour couvrir chacun des milliards de téléphones cellulaires, des milliards d'ordinateurs portables et de bureau, et des milliards d'autres voitures connectées au réseau, appareils et dispositifs de l'Internet des objets qui sont déjà là. Sans parler des milliards d'autres qui arrivent bientôt.

Ainsi, les ingénieurs réseau ont réservé trois plages d'adresses IPv4 à utiliser exclusivement dans les réseaux privés. Les appareils utilisant une adresse de ces plages ne seront pas directement accessibles depuis l'Internet public et ne pourront pas accéder aux ressources Internet. Voici les trois plages :

```
Entre 10.0.0.0 et 10.255.255.255
Entre 172.16.0.0 et 172.31.255.255
Entre 192.168.0.0 et 192.168.255.255

```

Souvenez-vous de ce que le "T" dans NAT signifiait ? C'était "Translation" (Traduction). Ce que cela signifie, c'est qu'un routeur activé NAT prendra les adresses IP privées utilisées dans les demandes de trafic entre le LAN et l'Internet et les _traduira_ en l'adresse publique du routeur. Le routeur, fidèle à son nom, _acheminera_ ensuite ces demandes vers leurs destinations appropriées.

Cette simple reconception de l'adressage réseau a permis d'économiser des milliards d'adresses pour une utilisation avec des appareils - comme les téléphones cellulaires - qui ne faisaient pas partie d'un réseau privé. Tous ces ordinateurs portables, PC, et ainsi de suite fonctionnant dans tous ces foyers et bureaux partageraient commodément (et de manière transparente) les IP publiques de leurs routeurs.

Problème résolu ? Eh bien, pas tout à fait. Vous voyez, même avec cette utilisation efficace des adresses, il n'y en aura toujours pas assez pour l'explosion des appareils publics qui arrivent en ligne. Pour gérer ce problème, d'autres ingénieurs réseau ont inventé le protocole _IPv6_. Voici à quoi une adresse IPv6 pourrait ressembler :

```
2002:0df6:0001:004b:0100:6c2e:0370:7234

```

Cela a l'air compliqué, n'est-ce pas ? Et cela semble être un nombre beaucoup plus grand que cet exemple IPv4 faible d'avant.

Oui et oui. Je suis devenu assez bon pour me souvenir de certains types d'adresses IPv4, mais je n'ai jamais même essayé de "télécharger" un de ces monstres. 

Pour une chose, c'est hexadécimal, ce qui signifie qu'il utilise les nombres entre 0 et 9 _et_ les six premières lettres de l'alphabet (a-f) ! En outre, il y a huit octets au lieu de quatre, et l'adresse est de 128 bits au lieu de 32 bits.

Tout cela signifie que, une fois le protocole pleinement mis en œuvre, nous ne risquerons pas de manquer d'adresses pendant très, très longtemps (c'est-à-dire : pour toujours). Et ce que _cela_ signifie, c'est que, du point de vue de l'allocation des adresses, il n'y a plus besoin de réseaux NAT privés. 

Bien que, pour des raisons de sécurité, vous voudrez toujours donner à vos appareils une certaine protection au sein de votre LAN.

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/)._