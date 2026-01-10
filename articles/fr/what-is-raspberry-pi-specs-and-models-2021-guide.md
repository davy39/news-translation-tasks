---
title: Qu'est-ce que le Raspberry Pi ? Spécifications et modèles (Guide 2021)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-25T16:17:20.000Z'
originalURL: https://freecodecamp.org/news/what-is-raspberry-pi-specs-and-models-2021-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Raspberry-Pi-2-Bare-FL-bigger.jpeg
tags:
- name: Internet of Things
  slug: internet-of-things
- name: iot
  slug: iot
- name: Raspberry Pi
  slug: raspberry-pi
seo_title: Qu'est-ce que le Raspberry Pi ? Spécifications et modèles (Guide 2021)
seo_desc: 'By Veronica Stork

  Introduction

  Are you curious about the IoT (Internet of Things?) Have you always wanted to try
  to make your own robot, smart mirror, or bird feeder camera? What about building
  a computer for a fraction of the cost of a commercially ...'
---

Par Veronica Stork

## Introduction

Êtes-vous curieux à propos de l'IoT (Internet des objets) ? Avez-vous toujours voulu essayer de fabriquer votre propre robot, miroir intelligent ou caméra pour mangeoire à oiseaux ? Et si vous construisiez un ordinateur pour une fraction du coût d'une machine disponible dans le commerce ?

Si vous avez répondu oui à l'une de ces questions, vous pourriez apprécier de jouer avec un Raspberry Pi.

Dans cet article, je vais expliquer ce qu'est un Raspberry Pi (et ce qu'il n'est pas). Ensuite, je vous montrerai quelques utilisations possibles, et enfin, je listerai tous les modèles actuels avec leurs spécifications.

## Qu'est-ce que le Raspberry Pi ?

Un Raspberry Pi est un ordinateur monocarte (SBC) créé au Royaume-Uni par la [Raspberry Pi Foundation](https://www.raspberrypi.org/about/). Il s'agit d'une organisation caritative qui "œuvre pour mettre le pouvoir de l'informatique et de la création numérique entre les mains des gens du monde entier".

Le premier modèle du Raspberry Pi a été lancé en 2012, et en 2021, il y a eu cinq générations de ces cartes. Un microcontrôleur (plus d'informations à ce sujet plus tard), appelé le Pico, a été lancé au début de l'année 2021.

### Broches GPIO

Ce qui distingue le Pi d'un ordinateur moyen est l'ensemble de 40 broches GPIO (General Purpose Input Output).

Les broches GPIO sont exactement ce à quoi elles ressemblent. Elles sont conçues pour entrer et sortir des bits simples. Cela signifie que vous pouvez les utiliser pour ajouter toutes sortes de fonctionnalités à votre Raspberry Pi en utilisant des interrupteurs, des buzzers, des lumières, des capteurs, et ainsi de suite.

### Chapeaux Raspberry Pi

Il existe un certain nombre de cartes d'extension que vous pouvez attacher au Raspberry Pi en utilisant les broches GPIO.

Les chapeaux Raspberry Pi (Hardware Attached on Top) sont des cartes d'extension conçues selon certaines spécifications. Le Raspberry Pi peut détecter et configurer automatiquement les chapeaux, ce qui facilite l'installation.

Il existe une énorme variété de chapeaux et d'autres cartes d'extension que vous pouvez acheter, mais en voici quelques-uns notables :

* **[PoE+ HAT](https://www.raspberrypi.org/products/poe-plus-hat/)** – Alimentation par Ethernet
* **[Sense HAT](https://www.raspberrypi.org/products/sense-hat/)** – Conçu pour la mission [Astro Pi](https://astro-pi.org/), le Sense HAT inclut un gyroscope, un accéléromètre, un magnétomètre et des capteurs pour la température, l'humidité et la pression barométrique.
* **[Pimoroni Explorer HAT Pro](https://shop.pimoroni.com/products/explorer-hat)** – Carte polyvalente avec pavés tactiles, bornes à pinces crocodile et entrées analogiques
* **[Adafruit Capacitive Touch HAT](https://www.adafruit.com/product/2340)** – Similaire à un [Makey Makey](https://makeymakey.com/), ce chapeau vous permet d'utiliser n'importe quel objet conducteur pour déclencher des événements en utilisant Python.

### Systèmes d'exploitation Raspberry Pi

Le Raspberry Pi fonctionne souvent sous une forme de Linux, mais il existe de nombreux systèmes d'exploitation que vous pouvez utiliser.

Sur le site officiel, vous trouverez une liste des [images de systèmes d'exploitation](https://www.raspberrypi.org/software/operating-systems/) disponibles pour le téléchargement. Cela inclut le système d'exploitation officiel Raspberry Pi OS, Debian Buster et Ubuntu (bureau, cœur et serveur).

Vous trouverez également RetroPie, une plateforme de jeu spécialisée, et LibreELEC, une distribution Linux légère spécifiquement créée pour être utilisée avec le lecteur multimédia open source [Kodi](https://kodi.tv/).

### Raspberry Pi VS Arduino

Vous avez peut-être entendu parler des cartes Arduino et vous êtes demandé quelle est la différence entre elles et le Raspberry Pi.

La principale différence est que les Pis (à l'exception du Pico et du RP2040) sont des ordinateurs complets avec des systèmes d'exploitation. Vous pouvez connecter votre Pi à un clavier, une souris et un moniteur et l'utiliser comme vous utiliseriez un Mac ou un PC.

L'Arduino, en revanche, est un microcontrôleur. Il ne peut pas fonctionner indépendamment comme un ordinateur, mais est programmé à l'aide d'un ordinateur puis utilisé pour contrôler des choses comme des caméras, des lumières, des robots, etc.

Comme le dit le site officiel d'Arduino : « Les cartes Arduino sont capables de lire des entrées... et de les transformer en sortie. »

## À quoi sert le Raspberry Pi ?

Faites une recherche sur Internet et vous trouverez une multitude de projets créés à l'aide de Raspberry Pis.

Les cas d'utilisation courants incluent la domotique, les consoles de jeu, les serveurs, les amplificateurs WiFi, les appareils de streaming, les stations météo et les ordinateurs domestiques. (Fait amusant : une grande partie de cet article a été écrite sur un Raspberry Pi.)

Pendant la pandémie de Covid-19, les Raspberry Pi ont même été utilisés pour contrôler des [respirateurs](https://www.engadget.com/raspberry-pi-ventilators-covid-19-163729140.html) dans certaines zones fortement touchées.

## Modèles de Raspberry Pi

Tous les modèles de Raspberry Pi actuellement en production disposent de 40 broches GPIO.

Cette liste n'inclut pas les microcontrôleurs Raspberry Pi, le Pico et le RP2040.

Vous pouvez trouver où acheter l'une de ces cartes sur le [site web de Raspberry Pi](https://www.raspberrypi.org/products/).

| Modèle | Processeur | RAM | Connectivité | USB | HDMI | Alimentation | Prix |
| ----- | -------- | ------ | ------------ | ---- | ------------- | ----- | ---- |
| Zero | BCM2835 | 512MB | Aucun | Micro USB OTG | Mini HDMI | Micro USB | 5 $ |
| Zero W | BCM2835 | 512MB | LAN sans fil 802.11 b/g/n | Micro USB OTG | Mini HDMI | Micro USB | 10 $ |
| Raspberry Pi 1 Modèle A+ | BCM2835 | 512MB | Aucun | 1x USB 2.0 | HDMI pleine taille | Micro USB | 25 $ |
| Raspberry Pi 1 Modèle B+ | BCM2835 | 512MB | Ethernet 100 base | 4x USB 2.0 | HDMI pleine taille | Micro USB | 30 $ |
| Raspberry Pi 3 Modèle A+ | BCM2837B0 | 512MB | Sans fil dual-band, Bluetooth 4.2 | 1x USB 2.0 | HDMI pleine taille | 5V DC via Micro USB | 25 $ |
| Raspberry Pi 3 Modèle B | BCM2837 | 1GB | Ethernet, sans fil, BLE | 4x USB 2.0 | HDMI pleine taille | 2.1A via Micro USB | 35 $ |
| Raspberry Pi 3 Modèle B+ | BCM2837B0 | 1GB | Sans fil dual-band, Bluetooth 4.2, BLE | 4x USB 2.0 | HDMI pleine taille | 5V DC via Micro USB et Power-over-Ethernet (PoE) | 35 $ |
| Raspberry Pi 4 Modèle B | BCM2711 | 2GB, 4GB ou 8GB | Ethernet Gigabit, sans fil dual-band, Bluetooth | 2x USB 3.0 et 2x USB 2.0 | 2x micro HDMI | 5V DC via USB-C | 35 $, 55 $, 75 $ |
| Raspberry Pi 400 | BCM2711 | 4GB | Ethernet Gigabit, sans fil dual-band, Bluetooth | 2x USB 3.0 et 1x USB 2.0 | 2x micro HDMI | 5V DC via USB | 70 $ |

## Conclusion

Le Raspberry Pi est un moyen abordable d'explorer l'électronique, le matériel et la programmation informatique. Il peut être utilisé pour une multitude de projets, des plus farfelus (comme une [machine à dessiner alimentée par un hamster](https://www.raspberrypi.org/blog/hamsters-all-the-way-down/)) aux plus importants (comme des [laboratoires informatiques](https://www.raspberrypi.org/blog/building-computer-labs-in-western-africa/) dans les nations en développement.)

Maintenant que vous connaissez les bases, pourquoi ne pas sortir et créer quelque chose ? Que vous connectiez un Capacitive Touch HAT à votre Raspberry Pi et le transformiez en un piano à bananes ou que vous installiez Linux dessus et l'utilisiez pour faire vos devoirs, j'espère que vous passerez un bon moment à créer quelque chose de cool et d'utile.