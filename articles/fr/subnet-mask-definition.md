---
title: Définition du masque de sous-réseau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-20T08:06:00.000Z'
originalURL: https://freecodecamp.org/news/subnet-mask-definition
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/denny-muller-JyRTi3LoQnc-unsplash-1.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: networking
  slug: networking
- name: Tech Terms
  slug: tech-terms
seo_title: Définition du masque de sous-réseau
seo_desc: 'A subnet mask defines the range of IP addresses that can be used within
  a network or subnet. It also separates an IP address into two parts: network bits
  and host bits.

  Subnet masks are used when subnetting, which is when you break a network up into
  ...'
---

Un masque de sous-réseau définit la plage d'adresses IP qui peuvent être utilisées au sein d'un réseau ou d'un sous-réseau. Il sépare également une adresse IP en deux parties : les bits de réseau et les bits d'hôte.

Les masques de sous-réseau sont utilisés lors de la création de sous-réseaux, c'est-à-dire lorsque vous divisez un réseau en réseaux plus petits. En ajustant le masque de sous-réseau, vous pouvez définir le nombre d'adresses IP disponibles au sein d'un réseau.

Par exemple, un masque de sous-réseau courant pour les réseaux domestiques simples est `255.255.255.0`. Ce masque de sous-réseau permet jusqu'à 254 adresses IP utilisables au sein du réseau domestique. En d'autres termes, jusqu'à 254 ordinateurs, téléphones et autres appareils connectés à Internet peuvent se connecter à votre routeur/réseau et accéder à Internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/home-network-diagram-1.png)
_Un réseau / sous-réseau simple. Source : [What Is My IP Address?](https://www.popularmechanics.com/technology/a32729384/how-to-find-ip-address/)_

Les masques de sous-réseau divisent une adresse IP en bits de réseau et en bits d'hôte. Lorsqu'un appareil voit les bits de réseau et d'hôte de l'adresse IP d'un autre appareil, il peut déterminer si l'autre appareil fait partie du même réseau (domestique, professionnel, etc.) ou se trouve ailleurs en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/network-and-host-bits-2.png)
_Une adresse IP et un masque de sous-réseau. Source : [IPv4](https://support.huawei.com/enterprise/en/doc/EDOC1100145159)_

Consultez [cet article](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) pour plus d'informations sur les sous-réseaux, les masques de sous-réseau et leur fonctionnement.


## Termes techniques associés :

* [Définition du sous-réseau](https://www.freecodecamp.org/news/subnet-definition/)