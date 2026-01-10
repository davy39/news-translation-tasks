---
title: Le guide rapide du fonctionnement des ordinateurs pour les nouveaux codeurs
  désespérés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T07:02:57.000Z'
originalURL: https://freecodecamp.org/news/the-quick-guide-to-the-way-computers-work-for-desperate-new-coders-fcdb34cbe8a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j4oOOKFcBCmSOfVlAx5UTA.jpeg
tags:
- name: internet
  slug: internet
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le guide rapide du fonctionnement des ordinateurs pour les nouveaux codeurs
  désespérés
seo_desc: 'By Danielle Ormshaw

  The sole purpose of your computer is to send and receive information in the form
  of numbers — one and zero.

  When I first understood the weight of that concept, I became transfixed. How can
  we create such complex interactions from ...'
---

Par Danielle Ormshaw

Le seul but de votre ordinateur est d'envoyer et de recevoir des informations sous forme de nombres — un et zéro.

Quand j'ai compris pour la première fois l'importance de ce concept, j'en suis restée fascinée. Comment pouvons-nous créer des interactions aussi complexes à partir d'une série de uns et de zéros ?

J'ai étudié des textes d'informatique et j'ai fouillé l'internet. Je luttais pour comprendre comment tout cela s'assemblait. Voici le guide que j'aurais aimé trouver il y a des mois, quand j'ai commencé ce voyage.

#### Les humains communiquent en utilisant le système décimal

Quand les humains veulent communiquer en utilisant des nombres, ils utilisent le système décimal. Le système décimal a dix chiffres (0–9), et les humains l'interprètent en fonction de la colonne dans laquelle ces chiffres apparaissent. Prenons le nombre décimal 148. Quand vous lisez cet exemple, vous suivez subconsciemment les étapes ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/dDhLCsHJho2mEfhcyTU6p62DYz7B6uYXYURd)
_Image courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

1. Multipliez le nombre le plus à droite par 10^0.
2. Multipliez le nombre du milieu par 10^1.
3. Multipliez le nombre le plus à gauche par 10^2.
4. Additionnez les résultats des étapes 1–3.

En utilisant ce système, vous avez pu extrapoler le sens correct — cent quarante-huit.

Dans le système décimal, nous multiplions toujours les chiffres par 10 à la puissance de quelque chose. Chaque fois que nous ajoutons une nouvelle colonne du côté gauche du tableau, cette puissance doit augmenter de un. De cette manière, nous disons que le système décimal a une base de 10. Assez simple ?

#### Les ordinateurs communiquent en utilisant le système binaire

Quand les ordinateurs veulent communiquer, ils utilisent un système similaire. Le système binaire a deux chiffres (0,1), et nous pouvons le décomposer de la même manière que le système décimal. Cette fois, au lieu de travailler avec une base de 10, nous travaillons avec une base de 2.

Prenons le nombre binaire 110. Quand un ordinateur interprète ce code binaire, il suivra les étapes ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/On4kpucSuObeC674s2uIY41mDzZYuvPzlwMU)
_Image courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

1. Multipliez le nombre le plus à droite par 2^0.
2. Multipliez le nombre du milieu par 2^1.
3. Multipliez le nombre le plus à gauche par 2^2.
4. Additionnez les résultats des étapes 1–3.

Encore une fois, chaque fois que nous ajoutons une nouvelle colonne du côté gauche du tableau, nous devons augmenter la puissance de un.

#### L'internet est un système physique, conçu pour déplacer l'information

Nous avons appris à utiliser le code binaire pour stocker des informations, mais comment cela fonctionne-t-il en pratique ?

L'internet est comme un coursier de livraison Amazon. Au lieu d'expédier des colis, il expédie des bits. Peu importe que vous envoyiez une photo ou un document — chaque morceau d'information sur l'internet est représenté en bits. Chaque bit a une valeur binaire unique (zéro ou un), et huit bits se combinent pour former un octet.

![Image](https://cdn-media-1.freecodecamp.org/images/rke7oIm8BmhDL4tzXCBTkZRlObF829oZFrut)
_Illustration courtesy of [Twitter](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title="">Danielle Ormshaw</a> on <a href="https://twitter.com/SchnucklePi/status/971362650918670337" rel="noopener" target="_blank" title=")._

Quand vous téléchargez un fichier sur votre ordinateur, vous voyez probablement une taille de fichier en kilooctets ou en mégaoctets. Le kilooctet est de mille octets, et le mégaoctet est d'un million d'octets.

La transmission de l'information binaire peut se faire de trois manières :

1. Transmission électrique.
2. Transmission par fibre optique.
3. Transmission sans fil.

Les fournisseurs de services internet (FAI) fournissent l'infrastructure physique qui supporte ces systèmes.

#### Chaque appareil connecté à l'internet a une adresse unique

Quand vous commandez un colis sur Amazon, le coursier utilise votre adresse pour livrer au bon endroit. L'internet fonctionne exactement de la même manière.

Quand nous cherchons quelque chose sur Google, nous envoyons notre demande à une chaîne unique de nombres, connue sous le nom d'adresse IP. Ces demandes incluront une multitude de bits et l'adresse IP de l'appareil d'origine. C'est comme une « adresse de retour », et le destinataire peut maintenant comprendre d'où vient la demande.

Cela dit, quand nous voulons visiter Google, nous ne tapons pas une chaîne de nombres dans le navigateur. Alors, comment nos ordinateurs savent-ils où envoyer chaque demande ?

#### L'internet fonctionne via une série de protocoles et de points de contrôle

Le système de noms de domaine (DNS) convertit les adresses web lisibles par les humains en adresses IP numériques. Dans le cas où le DNS ne connaît pas l'adresse, il engagera un réseau de serveurs connectés pour trouver la réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/6d9E3Ds1Tgab45xyrutKvKCDDqjDFPHmVjNJ)
_Illustration courtesy of [Twitter](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title="">Danielle Ormshaw</a> on <a href="https://twitter.com/SchnucklePi/status/971746123298889729" rel="noopener" target="_blank" title=")._

Quand deux appareils communiquent, ils envoient des informations en paquets. Nous devons souvent diviser les informations en plusieurs paquets. Chacun contiendra des octets d'informations et les adresses IP d'envoi et de réception.

Les paquets se déplacent à travers le réseau d'appareils en utilisant un système de gestion du trafic. Les routeurs suivent les chemins que les paquets peuvent prendre et identifient le chemin le « moins cher ». Le chemin le moins cher est souvent défini comme celui avec le moins de congestion. Lors de la gestion des paquets, les routeurs peuvent également prendre en compte des facteurs non techniques, comme la politique internationale.

Les paquets peuvent prendre différents chemins à travers le réseau et arrivent souvent à destination dans le désordre. Comment le réseau gère-t-il cela ?

Le protocole de contrôle de transmission (TCP) agit comme un contrôle d'inventaire. Si tous les paquets sont présents, TCP envoie un accusé de réception à l'appareil d'envoi. Sinon, TCP « refusera de signer » pour la livraison et demandera tous les paquets manquants.

![Image](https://cdn-media-1.freecodecamp.org/images/M4qSQ2gLbtyVUQAYMRtlChaPOYuvfzV9mD9A)
_Illustration courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

En résumé, le serveur de noms de domaine (DNS) traduit les adresses web lisibles par les humains en une adresse IP. Les informations sont décomposées, transportées et acceptées sous forme de paquets. Les paquets contiennent des informations binaires sous forme de bits, et les câbles électriques, les fibres optiques et les réseaux sans fil envoient ces bits entre les adresses IP.

#### Qu'est-ce qui suit ?

Si cet article vous a aidé à comprendre les bases, montrez votre appréciation avec une salve d'applaudissements ou en me suivant sur [Twitter](https://twitter.com/SchnucklePi). Bon codage !