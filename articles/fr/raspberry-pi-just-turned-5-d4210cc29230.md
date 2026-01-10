---
title: Raspberry Pi vient de fêter ses 5 ans. Voici une brève histoire de l'ordinateur
  le plus petit au monde pour les passionnés.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-11T22:04:14.000Z'
originalURL: https://freecodecamp.org/news/raspberry-pi-just-turned-5-d4210cc29230
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7GJdUsrLnqQ3RLdBz4rOVQ.jpeg
tags:
- name: Makers
  slug: makers
- name: Raspberry Pi
  slug: raspberry-pi
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Raspberry Pi vient de fêter ses 5 ans. Voici une brève histoire de l'ordinateur
  le plus petit au monde pour les passionnés.
seo_desc: 'By Terren Peterson

  Raspberry Pi just turned five years old. In this short period of time, twelve million
  of these devices have been sold, enabling countless maker projects around the world.

  Let’s walk through the evolution of these devices, and explo...'
---

Par Terren Peterson

Raspberry Pi vient de fêter ses cinq ans. En cette courte période, douze millions de ces appareils ont été vendus, permettant d'innombrables projets de bricolage à travers le monde.

Parcourons l'évolution de ces appareils et explorons comment ils peuvent être utilisés dans des projets.

### Au début…

La première génération des appareils Raspberry Pi est sortie en 2012. On pouvait en placer un sur une carte de 3" x 2" (sans inclure les protrusions des accessoires). Ils utilisaient une carte SD standard comme disque local et disposaient de deux ports USB.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OSKRsxwiE_21fMktNr_QUg.jpeg)
_Matériel pour la première génération de Raspberry Pi_

Le prix était extrêmement bas (les objectifs initiaux étaient de 35 $ et 25 $ pour le Pi seul). Des passionnés comme moi les ont rapidement achetés et ont commencé des projets d'Internet des objets.

Des utilisateurs comme moi ont rapidement réalisé qu'il fallait plusieurs extensions matérielles avant de pouvoir connecter l'appareil à un réseau sans fil — ou même pour le connecter à un clavier et une souris. On voulait aussi le monter dans un boîtier durable pour prévenir l'usure de la carte.

Nous avons acheté notre premier Raspberry Pi pour Noël en 2013. Ma fille et moi l'avons utilisé pour son projet scientifique, qui impliquait la création d'une alarme à LED capable de détecter lorsqu'un intrus s'approchait de son [château Minecraft](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/). L'appareil supportait le scripting en Python et toutes les extensions pertinentes pour effectuer des appels HTTP/S à distance en utilisant le SDK Minecraft.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NQZW2wbaER_kCp2FZkvb0A.jpeg)

### Génération 2

Raspberry Pi a ajouté des améliorations majeures à sa deuxième génération, sortie début 2015. Cela incluait un doublement du nombre de ports USB. Cela a éliminé le besoin d'un hub USB. Au lieu de cela, on pouvait brancher un adaptateur sans fil, un clavier et une souris directement sur l'appareil en même temps.

Pour faire de la place à une expansion des broches GPIO, ils ont retiré les ports RCA et 3,5 mm peu utilisés et ont ajouté une carte microSD plus petite pour le disque local. Ils ont mis à niveau le CPU intégré d'un simple cœur à un quadricœur, augmentant les capacités de traitement de l'appareil.

Bien que les changements visuels de l'appareil aient été mineurs, ces mises à niveau majeures étaient toutes basées sur l'utilisation et les retours de la communauté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tKRzlUEkT19jlTZiDTH8dg.jpeg)
_Comparaison des appareils de 2e et 1re génération_

En expérimentant avec cette nouvelle génération d'appareils, j'ai découvert que les broches GPIO étaient idéales pour faire fonctionner des capteurs. La taille et la puissance étaient également idéales pour des [projets de jardinage d'intérieur](https://www.hackster.io/terren/simple-gardening-service-manage-indoor-gardens-using-iot-be95d1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zz0tmv-oDBExbSg4xoWHrA.jpeg)

Je pouvais utiliser une seule unité montée dans mon expérience pour enregistrer l'humidité, la température et le contenu d'humidité du sol. Je pouvais également capturer des photos en accéléré en ajoutant une caméra, puis télécharger toutes les données dans le Cloud pour traitement et diffusion sur un site web.

Je pouvais également utiliser les broches GPIO pour contrôler des relais qui instruisent les moteurs de s'allumer et de s'éteindre. Cela pouvait être très utile lors de la construction d'une [machine de lancer à commande vocale](https://www.hackster.io/terren/roxie-the-voice-activated-pitching-machine-94e4f2) comme celle dans la vidéo ci-dessous.

### Réduction à Zero

Raspberry Pi a lancé une deuxième gamme fin 2015 : le Raspberry Pi Zero. Le prix cible a également chuté, avec 5 $ comme nouvelle norme (bien qu'il était difficile de trouver un détaillant avec des stocks).

Bien que le Zero n'ait pas le même nombre de ports — juste un micro USB — il avait un avantage massif en termes de taille et de consommation d'énergie. Il pesait seulement 9 grammes, et la carte était seulement un tiers de la taille. Il continuait à supporter l'ajout d'une caméra, et le système d'exploitation était le même que pour les modèles plus grands.

La consommation d'énergie du Zero était inférieure à un Watt, lui permettant de tirer une puissance minimale soit d'une source d'alimentation USB directe, soit d'une batterie locale. Alors que le Model B était devenu plus puissant, il consommait également jusqu'à 4 Watts — plus du double du modèle initial. Cela pouvait être un facteur limitant lors de la collecte de données à distance dans des situations où une source d'alimentation stable n'était pas disponible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JGmS1vrsjE72qNQ4Ft5hww.jpeg)
_Raspberry Pi Zero vs. Model B de 2e génération_

La réduction de taille a permis à l'appareil d'être plus facilement caché dans des projets d'Internet des objets, y compris ce système de reconnaissance d'image que j'ai construit pour [surveiller mon stock de grains de café](https://medium.freecodecamp.com/how-i-built-a-fully-automated-system-that-restocks-my-kitchens-coffee-from-amazon-87072b65efd0).

![Image](https://cdn-media-1.freecodecamp.org/images/1*G1MQH50H359-2HKD9fTuFQ.jpeg)
_JavaWatch basé sur un Raspberry Pi Zero_

### Qu'est-ce qui suit ?

Dans le cadre de leur cinquième anniversaire, Raspberry Pi [vient d'annoncer](https://www.raspberrypi.org/blog/#raspberry-pi-zero-w-joins-family) une nouvelle version sans fil du Zero avec un prix de seulement 10 $ ! En regardant la photo ci-dessus, il est facile de voir l'avantage. Étant donné que les connecteurs sans fil nécessitent un port USB, vous avez besoin d'un adaptateur si grand qu'il peut rendre le petit appareil maladroit dans des projets comme celui-ci.

La dernière version intègre la connexion WiFi sur la carte elle-même, éliminant le besoin d'un dongle et le coût supplémentaire d'un adaptateur WiFi séparé.

Mon hypothèse est que la prochaine version passera à un CPU multicœur pour gérer un traitement plus important. Il y a une parité avec la plupart des autres capacités du modèle plus grand, donc vous n'aurez peut-être pas besoin de nombreux autres accessoires.

Le nombre d'utilisations pour ces appareils est illimité. Ils resteront certainement très demandés.

Merci d'avoir lu. J'espère que vous pourrez bientôt expérimenter avec un Raspberry Pi.