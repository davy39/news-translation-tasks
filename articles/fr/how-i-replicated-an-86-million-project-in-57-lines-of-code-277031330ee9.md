---
title: Comment j'ai répliqué un projet de 86 millions de dollars en 57 lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-28T23:25:59.000Z'
originalURL: https://freecodecamp.org/news/how-i-replicated-an-86-million-project-in-57-lines-of-code-277031330ee9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BU46LufhEIhxIt_BUyPaRQ.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: hackathons
  slug: hackathons
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
seo_title: Comment j'ai répliqué un projet de 86 millions de dollars en 57 lignes
  de code
seo_desc: 'By Tait Brown

  When an experiment with existing open source technology does a “good enough” job


  The Victoria Police are the primary law enforcement agency of Victoria, Australia.
  With over 16,000 vehicles stolen in Victoria this past year — at a cost...'
---

Par Tait Brown

#### Quand une expérience avec une technologie open source existante fait un travail "suffisant"

![Image](https://cdn-media-1.freecodecamp.org/images/1*xU8VOotxa_HpI908SBACAQ.jpeg)

La police de Victoria est l'agence principale de maintien de l'ordre de Victoria, en Australie. Avec plus de 16 000 véhicules volés à Victoria cette année passée — pour un coût d'environ 170 millions de dollars — le département de police expérimente diverses solutions technologiques pour lutter contre le vol de voitures. Ils appellent ce système BlueNet.

Pour aider à prévenir les ventes frauduleuses de véhicules volés, il existe déjà un service web de VicRoads [service basé sur le web](https://www.vicroads.vic.gov.au/registration/buy-sell-or-transfer-a-vehicle/buy-a-vehicle/check-vehicle-registration/vehicle-registration-enquiry) pour vérifier l'état des immatriculations des véhicules. Le département a également investi dans un scanner de plaques d'immatriculation stationnaire — une caméra sur trépied fixe qui scanne le trafic passant pour identifier automatiquement les véhicules volés.

Ne me demandez pas pourquoi, mais un après-midi, j'ai eu l'envie de prototyper un scanner de plaques d'immatriculation monté sur véhicule qui vous notifierait automatiquement si un véhicule avait été volé ou n'était pas immatriculé. Comprenant que ces composants individuels existaient, je me suis demandé à quel point il serait difficile de les connecter ensemble.

Mais c'est après quelques recherches sur Google que j'ai découvert que la police de Victoria avait récemment mené un essai d'un dispositif similaire, et que le coût estimé du déploiement était de l'ordre de 86 000 000 de dollars. Un commentateur perspicace a souligné que le coût de 86 millions de dollars pour équiper 220 véhicules revient à un montant plutôt élevé de **390 909 dollars par véhicule**.

Surely we can do a bit better than that.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6AfjJMn_bKbNBEX5sWUVOg.png)
_Systèmes existants de reconnaissance de plaques d'immatriculation stationnaires_

### Les Critères de Succès

Avant de commencer, j'ai défini quelques exigences clés pour la conception du produit.

#### **_Exigence #1 : Le traitement de l'image doit être effectué localement_**

Diffuser une vidéo en direct vers un entrepôt de traitement central semblait être l'approche la moins efficace pour résoudre ce problème. En plus de la facture astronomique pour le trafic de données, vous introduisez également une latence réseau dans un processus qui peut déjà être assez lent.

Bien qu'un algorithme centralisé de machine learning ne fera que devenir plus précis avec le temps, je voulais savoir si une implémentation locale sur l'appareil serait "suffisante".

#### **_Exigence #2 : Cela doit fonctionner avec des images de faible qualité_**

Puisque je n'ai pas de caméra Raspberry Pi ou de webcam USB, je vais utiliser des images de dashcam — elles sont facilement disponibles et constituent une source idéale de données d'exemple. En prime, la vidéo de dashcam représente la qualité globale des images que vous attendez des caméras montées sur véhicules.

#### **_Exigence #3 : Cela doit être construit en utilisant une technologie open source_**

Compter sur un logiciel propriétaire signifie que vous serez facturé à chaque fois que vous demanderez un changement ou une amélioration — et les factures continueront pour chaque demande ultérieure. Utiliser une technologie open source est une évidence.

### **Ma solution**

À un niveau élevé, ma solution prend une image d'une vidéo de dashcam, la traite via un système de reconnaissance de plaques d'immatriculation open source installé localement sur l'appareil, interroge le service de vérification d'immatriculation, puis retourne les résultats pour affichage.

Les données retournées à l'appareil installé dans le véhicule de la force de l'ordre incluent la marque et le modèle du véhicule (qu'il n'utilise que pour vérifier si les plaques ont été volées), le statut d'immatriculation, et toute notification du véhicule signalé comme volé.

Si cela semble plutôt simple, c'est parce que c'est vraiment le cas. Par exemple, le traitement de l'image peut être entièrement géré par la bibliothèque _openalpr_.

Voici tout ce qui est impliqué pour reconnaître les caractères sur une plaque d'immatriculation :

> **Un petit bémol**  
> L'accès public aux API de VicRoads n'est pas disponible, donc les vérifications de plaques d'immatriculation se font via le web scraping pour ce prototype. Bien que généralement mal vu — c'est une preuve de concept et je ne surcharge pas les serveurs de qui que ce soit.

Voici à quoi ressemble la saleté de mon scraping de preuve de concept :

### Résultats

Je dois dire que j'ai été agréablement surpris.

Je m'attendais à ce que la reconnaissance de plaques d'immatriculation open source soit plutôt médiocre. De plus, les algorithmes de reconnaissance d'image ne sont probablement pas optimisés pour les plaques d'immatriculation australiennes.

La solution a pu reconnaître les plaques d'immatriculation dans un large champ de vision.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BU46LufhEIhxIt_BUyPaRQ.jpeg)
_Annotations ajoutées pour l'effet. Plaque d'immatriculation identifiée malgré les reflets et la distorsion de l'objectif._

Bien que, la solution ait parfois des problèmes avec certaines lettres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yZYByyp5YlgqnSPjQsDW6A.jpeg)
_Lecture incorrecte de la plaque, a confondu le M avec un H_

Mais... la solution finissait par les reconnaître correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yIx5li10Tin7t0ZAZWVq5w.jpeg)
_Quelques images plus tard, le M est correctement identifié et avec un taux de confiance plus élevé_

Comme vous pouvez le voir dans les deux images ci-dessus, le traitement de l'image quelques images plus tard est passé d'un taux de confiance de 87 % à un peu plus de 91 %.

Je suis confiant, si vous me permettez ce jeu de mots, que la précision pourrait être améliorée en augmentant le taux d'échantillonnage, puis en triant par le taux de confiance le plus élevé. Alternativement, un seuil pourrait être défini pour n'accepter qu'une confiance supérieure à 90 % avant de valider le numéro d'immatriculation.

Ce sont des corrections très simples basées sur le code, et elles n'excluent pas l'entraînement du logiciel de reconnaissance de plaques d'immatriculation avec un ensemble de données local.

#### La question de 86 000 000 de dollars

Pour être honnête, je n'ai absolument aucune idée de ce que comprend le chiffre de 86 millions de dollars — ni ne peux-je parler de la précision de mon outil open source sans entraînement localisé par rapport au système pilote BlueNet.

Je m'attendrais à ce qu'une partie de ce budget inclue le remplacement de plusieurs bases de données et applications logicielles héritées pour supporter les requêtes haute fréquence et à faible latence des plaques d'immatriculation plusieurs fois par seconde, par véhicule.

D'un autre côté, le coût de ~391 000 dollars par véhicule semble plutôt élevé — surtout si le BlueNet n'est pas particulièrement précis et qu'il n'y a pas de grands projets informatiques à désactiver ou à mettre à niveau les systèmes dépendants.

#### Applications futures

Bien qu'il soit facile de se laisser emporter par la nature orwellienne d'un réseau "toujours actif" de dénonciateurs de plaques d'immatriculation, il existe de nombreuses applications positives de cette technologie. Imaginez un système passif scannant les autres automobilistes pour repérer la voiture d'un ravisseur qui alerte automatiquement les autorités et les membres de la famille de leur position et direction actuelles.

Les véhicules Tesla regorgent déjà de caméras et de capteurs capables de recevoir des mises à jour OTA — imaginez les transformer en une flotte de bons samaritains virtuels. Les conducteurs d'Uber et de Lyft pourraient également être équipés de ces dispositifs pour augmenter considérablement la zone de couverture.

En utilisant une technologie open source et des composants existants, il semble possible d'offrir une solution qui fournit un taux de rendement beaucoup plus élevé — pour un investissement bien inférieur à 86 millions de dollars.

**Partie 2** — J'ai publié une mise à jour, dans laquelle je teste avec mes propres images et attrape un véhicule non immatriculé, par ici :

[**Vous vous souvenez de ce scanner de plaques d'immatriculation de 86 millions de dollars que j'ai répliqué ? Voici ce qui s'est passé ensuite.**](https://medium.freecodecamp.org/remember-that-86-million-license-plate-scanner-i-replicated-heres-what-happened-next-9f3c64e8f22b)  
[_Succès, échecs et l'arrestation d'un conducteur très malicieux_medium.freecodecamp.org](https://medium.freecodecamp.org/remember-that-86-million-license-plate-scanner-i-replicated-heres-what-happened-next-9f3c64e8f22b)