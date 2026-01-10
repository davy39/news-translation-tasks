---
title: La compression de données compte-t-elle sur un Internet quantique ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-28T15:37:24.000Z'
originalURL: https://freecodecamp.org/news/does-data-compression-matter-on-a-quantum-internet-f6b986473c1c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jB_VRVuG5z8Dtp2i4N1o9g.png
tags:
- name: data compression
  slug: data-compression
- name: General Programming
  slug: programming
- name: quantum computing
  slug: quantum-computing
- name: 'Science '
  slug: science
- name: technology
  slug: technology
seo_title: La compression de données compte-t-elle sur un Internet quantique ?
seo_desc: 'By Colt McAnlis

  Disclaimer: This is a hypothetical think piece. It is a personal opinion and doesn’t
  represent the opinion of any of the companies (or secret societies) I may (..or
  may not) be involved with. If you tear a hole through space-time afte...'
---

Par Colt McAnlis

_Avertissement : Il s'agit d'un article de réflexion hypothétique. C'est une opinion personnelle et elle ne représente pas l'opinion d'aucune des entreprises (ou sociétés secrètes) avec lesquelles je pourrais (ou ne pourrais pas) être associé. Si vous déchirez un trou dans l'espace-temps après avoir lu cet article... c'est de votre faute._

Si vous n'avez pas entendu parler, une équipe de recherche en Chine vient de faire un bond énorme en matière de réalisation de l'utilisation de [l'intrication quantique comme moyen de communication valide](http://science.sciencemag.org/cgi/doi/10.1126/science.aan3211). Leur processus consistait à utiliser un satellite en orbite basse pour créer une paire de photons intriqués, puis les envoyer à des emplacements très éloignés l'un de l'autre. Même à des distances jamais réalisées auparavant, les photons ont conservé leur intrication, ce qui a mis l'internet en ébullition quant à l'avenir de la communication et quant au moment où le nouvel internet quantique se concrétisera.

Maintenant, en regardant les maths, **je suis encore un peu dubitatif quant à l'utilisation viable de l'intrication quantique** pour la communication. Cette personne en maths [l'explique](https://www.forbes.com/sites/chadorzel/2016/05/04/the-real-reasons-quantum-entanglement-doesnt-allow-faster-than-light-communication/#1c0c3f153a1e) un [peu mieux que](https://medium.com/starts-with-a-bang/ask-ethan-can-we-use-quantum-entanglement-to-communicate-faster-than-light-e0d7097c0322) je ne pourrais jamais le faire. Cependant, de nombreuses personnes émettent l'hypothèse que ce sont les premières étapes d'un nouvel internet quantique où des choses comme [l'échange d'intrication](http://spectrum.ieee.org/telecom/security/two-steps-closer-to-a-quantum-internet) et [la lumière tordue](https://en.wikipedia.org/wiki/Orbital_angular_momentum_of_light) pourraient combler ces lacunes.

**Proposons alors une expérience de pensée** : supposons qu'il existe un avenir où un internet existe, dont la technologie est basée sur l'intrication quantique. Cela signifie que les données peuvent être transmises entre deux emplacements, à une vitesse proche de celle de la lumière, sans milieu de connexion physique entre les emplacements.

Dans un tel monde, la compression de données a-t-elle encore de l'importance ?

### Une petite idée sur le fonctionnement d'un internet QE

Nous devons supposer qu'en raison de la technologie actuelle, la première réalisation d'un Internet QE (QEI) serait très similaire aux systèmes télégraphiques du passé. Le coût de maintenance et d'exploitation de ces premiers sites QEI limiterait leur disponibilité, ce qui signifie que la communication ne pourrait se faire qu'entre une poignée de sites.

Ces sites nécessiteraient deux caractéristiques principales :

1. Un système non centralisé qui peut distribuer des paires de photons intriqués aux sites (un satellite en orbite basse, par exemple).
2. Un système d'enregistrement qui consigne les résultats des tests d'intrication et peut les stocker / les récupérer.

![Image](https://cdn-media-1.freecodecamp.org/images/Xp0h0wKzejEnv3nQ4yA-OAbVQ0AZU064giIv)

Le point #2 serait très probablement construit sur la technologie moderne d'aujourd'hui. Vous pouvez donc vous attendre à une situation où un milliard de paires de photons sont envoyées à un site, échantillonnées de manière synchronisée et stockées sous forme de données binaires à l'emplacement.

À partir de ce point, les données seraient très probablement distribuées à leur destination finale en utilisant des méthodes plus conventionnelles (par exemple, une connexion par fibre optique).

### Limites d'une première génération de QEI

Évidemment, nous avons toujours des goulots d'étranglement basés sur les données ici :

1. Il existe une limite physique au nombre de paires intriquées qui peuvent être stockées sur un site, limitant ainsi sa bande passante totale.
2. Il existe une limite physique à la vitesse à laquelle les paires intriquées peuvent être envoyées du distributeur aux sites sur une base régulière, limitant ainsi la bande passante totale du système.
3. Les facteurs environnementaux entraîneront une perte de données lors du transfert de photons des sites vers le système de distribution. Ainsi, il y aura un besoin de redondance dans le processus, limitant la bande passante totale du système.

En observant ce qui précède, vous pouvez rapidement voir que la bande passante globale d'un QEI serait limitée par les systèmes ci-dessus, indépendamment de la capacité de l'information à voyager entre les sites par des moyens quantiques. Il est donc évident que la réduction de la taille des données envoyées à travers les sites sera importante, mais les algorithmes de compression de données d'aujourd'hui auront-ils un sens ?

### Compression de données pour un QEI

Il existe quelques définitions de « données » qui les représentent comme une entité physique, et à mesure que la réalisation (potentielle) d'un Internet quantique se concrétise, le besoin de transfert de photons rend ce concept encore plus réel.

En fait, cela pourrait être la plus grande ramification d'un internet quantique intriqué : vos données ont maintenant une manifestation et un coût très physiques.

Il est donc évident que la compression de données, en tant que science, sera toujours nécessaire dans un avenir QEI, mais la vraie question que nous devrions nous poser est la suivante : **Les algorithmes de compression d'aujourd'hui sont-ils suffisamment bons pour supporter un internet quantique ?**

Mon opinion ? Pas du tout.

![Image](https://cdn-media-1.freecodecamp.org/images/muYjkNnMLxY6BjdD-TiW37VflNvJOFyizCaS)

Comme expliqué dans « [Comprendre la compression](https://www.amazon.com/Understanding-Compression-Data-Modern-Developers/dp/1491961538) », les systèmes d'aujourd'hui sont encore basés sur l'architecture de base de Shannon selon laquelle « le symbole le plus fréquent obtient les plus petits bits ». Il y a beaucoup de puissance dans ce processus, mais jusqu'à ce que nous sortions de l'espace des symboles et que nous commencions à obtenir la puissance de calcul pour gérer la compression entièrement dans l'espace des vecteurs de bits, [nous allons laisser beaucoup d'informations sur la table](http://ieeexplore.ieee.org/abstract/document/1054929/). (Mais _c'est mon opinion impopulaire personnelle..._)

Regardons au-delà de cela. Existe-t-il des systèmes potentiels où, plutôt que d'appliquer [Brotli](https://github.com/google/brotli) à un ensemble de données, nous pouvons l'appliquer directement aux photons intriqués ? Allons-nous commencer à parler d'algorithmes pour faire des diffs contre les photons sur un site et les données transmises, afin que nous puissions réduire le nombre de paires mises à jour ? Que se passe-t-il lorsque nous commençons à penser en termes de [qubits](https://en.wikipedia.org/wiki/Qubit), plutôt que simplement en bits ? Devons-nous commencer à penser à l'encodage LZ dans un espace à 8 dimensions ?

Évidemment, la réalisation et la standardisation de l'informatique quantique créeront un changement technologique massif dans le fonctionnement de notre monde. Et j'ai toutes les raisons de croire que la compression de données sera également là.