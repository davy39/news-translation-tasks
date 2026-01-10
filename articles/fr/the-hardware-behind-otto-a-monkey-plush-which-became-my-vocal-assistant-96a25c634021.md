---
title: 'Le matériel derrière Otto : un doudou singe devenu mon assistant vocal'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T07:36:32.000Z'
originalURL: https://freecodecamp.org/news/the-hardware-behind-otto-a-monkey-plush-which-became-my-vocal-assistant-96a25c634021
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PiGGkpQ-b6g5yj5wb1-fLQ.png
tags:
- name: AI
  slug: ai
- name: Electronics
  slug: electronics
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Le matériel derrière Otto : un doudou singe devenu mon assistant vocal'
seo_desc: 'By Flavio De Stefano

  Otto is a monkey plush that we found in a highway store during a trip with my girlfriend
  in February 2017.

  Its ability, while being extremely cute, was to listen to you, then walk and repeat
  all things with a higher pitch.

  My goa...'
---

Par Flavio De Stefano

Otto est un doudou singe que nous avons trouvé dans un magasin d'autoroute lors d'un voyage avec ma copine en février 2017.

Sa capacité, tout en étant extrêmement mignon, était de vous écouter, puis de marcher et de répéter toutes les choses avec une tonalité plus élevée.

Mon objectif était de le rendre plus puissant en le transformant en assistant vocal.

![Image](https://cdn-media-1.freecodecamp.org/images/COJTbvLC2I42BpC0vSMkIT6k4NBhl0UU18SY)
_SkeletOtto et Otto_

Ceci est la première partie d'une série sur Otto.

À l'origine, il était composé des éléments matériels suivants :

* Un moteur connecté à ses jambes pour lui permettre de marcher
* Une carte intégrée simple et fermée (aux modifications)
* Un microphone et un haut-parleur
* Un bouton-poussoir pour démarrer la phase d'écoute
* Quatre piles AA
* Un interrupteur pour couper complètement l'alimentation du circuit

Je voulais remplacer toutes ces choses par du matériel frais et **programmable**.

Le vrai défi ici était de trouver les bons composants qui s'adaptaient au boîtier d'origine. L'espace disponible n'était pas très grand, donc chaque choix devait être fait consciencieusement.

#### Carte de base

Le matériel préféré pour ce projet est la carte Raspberry PI.

Elles sont minuscules et suffisamment puissantes pour permettre aux développeurs d'utiliser un langage de programmation de haut niveau et des bibliothèques intégrées sans flasher le logiciel à chaque fois.

De plus, vous pouvez déboguer votre application dans un environnement plus confortable.

Le meilleur matériel à l'époque était le Raspberry Pi Zero W. Lancé à la fin du mois de février 2017, le Pi Zero W possède toutes les fonctionnalités du Pi Zero original mais avec une connectivité ajoutée.

![Image](https://cdn-media-1.freecodecamp.org/images/W3wJFAEqo4qznGUNqgsRJ378nCWaqhKJnzTS)
_Raspberry Pi Zero W_

La carte n'était pas suffisante pour un tel projet, donc j'ai ajouté du matériel supplémentaire.

#### Composants audio

Pour construire un assistant vocal, nous avons besoin de composants audio. Les exigences pour ces composants sont, bien sûr, un haut-parleur et un microphone.

Pour le microphone, j'ai essayé un microphone USB. Le problème avec cet accessoire était qu'il n'était pas aussi sensible que je l'aurais souhaité. De plus, un hub USB supplémentaire était nécessaire pour le connecter.

De plus, je ne pouvais pas connecter facilement un haut-parleur brut.

Pour cette raison, j'ai opté pour l'achat d'une carte supplémentaire qui accomplissait très bien cette tâche : [**ReSpeaker 2-Mics Pi HAT.**](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html)

ReSpeaker 2-Mics Pi HAT est une carte d'extension à double microphone pour Raspberry Pi conçue pour les applications d'IA et vocales.

La carte est développée sur la base de WM8960, un codec stéréo à faible consommation. Il y a 2 microphones de chaque côté de la carte pour collecter les sons. Elle offre également 3 LEDs RGB APA102, 1 bouton utilisateur et 2 interfaces Grove sur la carte.

Je ne prévoyais pas de connecter des LEDs à ma carte, mais le fait que ce HAT ait des LEDs intégrées m'a fait penser à les utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/k7MQ4agg2sWiQDawXk6cYrlQClwDRRoO42LX)
_ReSpeaker 2-Mics Pi HAT — Spécifications matérielles_

Ensuite, j'ai pris un ancien mini-haut-parleur Bluetooth, je l'ai démonté et je l'ai connecté au port de sortie JST 2.0 Speaker Out.

Pour le faire fonctionner, vous devez installer leurs pilotes sur votre carte. Les pilotes sont également utilisés pour contrôler les LEDs dans votre application via un protocole standard.

![Image](https://cdn-media-1.freecodecamp.org/images/8mM4GG3AQTMy-g7eQnJL0c20uTuvHnSjxSOl)
_ReSpeaker 2-Mics Pi HAT_

_Astuce : lorsque vous installez un shield, toutes vos broches GPIO sont couvertes. Il est utile de savoir quelles broches sont **réellement utilisées** par votre carte. Pour cela, utilisez [https://pinout.xyz/](https://pinout.xyz/)_

Par exemple, pour cette carte, consultez ce lien : [https://pinout.xyz/pinout/respeaker_2_mics_phat](https://pinout.xyz/pinout/respeaker_2_mics_phat)

#### Alimentation de la carte

La carte Raspberry Pi peut être facilement alimentée via une entrée USB 5V. Le problème avec cette approche est que vous devez acheter un pack de batteries et le connecter via USB.

Je n'ai pas trouvé de pack de batteries assez petit pour s'adapter à mon doudou, donc mon unique alternative était d'utiliser des batteries LiPo.

![Image](https://cdn-media-1.freecodecamp.org/images/HfXn7YZnmt89j10xAtkQAe94r7pu4wXWbM24)
_Batterie LiPo — 3.7V 2000mAh_

Vous ne pouvez pas connecter votre batterie LiPo directement à votre carte, vous devez utiliser un convertisseur. Il peut être alimenté par n'importe quelle batterie LiIon/LiPoly 3.7V, puis il convertit la sortie de la batterie en 5.2V DC.

Initialement, j'ai acheté un [**LiPo SHIM**](https://shop.pimoroni.com/products/lipo-shim), mais je n'ai pas remarqué que ce contrôleur alimente votre carte sans charger vos batteries.

Pour cette raison, je suis passé à [**Adafruit PowerBoost 500 Charger.**](https://shop.pimoroni.com/products/powerboost-500-charger-rechargeable-5v-lipo-usb-boost-500ma) Il dispose d'un circuit de chargeur de batterie intégré. Vous pourrez garder votre projet en fonctionnement même pendant la charge de la batterie !

![Image](https://cdn-media-1.freecodecamp.org/images/4XO2X19DkFrdmMQjjPtDySyPnBs38Fqkc2bV)
_Adafruit PowerBoost 500 Charger_

#### Matériel supplémentaire

Le logiciel utilise le concept de "mot clé" pour démarrer l'interaction. Basiquement, il écoute continuellement un mot clé, comme "Hey Otto", puis vous parlez et dites des commandes.

Pour avoir une méthode alternative pour démarrer l'interaction, j'ai installé un **bouton-poussoir** connecté directement à la carte GPIO, à la broche GPIO8.

![Image](https://cdn-media-1.freecodecamp.org/images/AbfTw6DM4xshozwQGOlgqUg-avN-5skzEFEy)
_Bouton-poussoir_

Maintenant, une seule chose manquait : **l'interrupteur marche-arrêt.**

J'ai connecté ce simple composant au PowerBoost Charger via son port ENABLE. Le but du port ENABLE est de déconnecter complètement la sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/4CoVDgx6OzOzkkcFBVKqGLQSmRmIQKCdRVPZ)
_Interrupteur marche-arrêt_

#### Connecter tout ensemble

Ici vous pouvez voir en détails le schéma de circuit complet ([https://www.circuit-diagram.org/circuits/0d85ce05](https://www.circuit-diagram.org/circuits/0d85ce05))

![Image](https://cdn-media-1.freecodecamp.org/images/LE5xX5LHgXWFVDpDIr3iWDPXvdztUmTgt0WC)
_Schéma de circuit d'Otto_

Et voici un aperçu du travail :

![Image](https://cdn-media-1.freecodecamp.org/images/mk8sBTQqHDokaq1MrbGo6PGXnWdnnKTUjq6x)
_Le matériel derrière Otto_