---
title: Les protocoles TCP et UDP – Expliqués en termes simples
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2023-08-10T22:19:30.000Z'
originalURL: https://freecodecamp.org/news/tcp-and-udp-protocols
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-159304.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: computer networking
  slug: computer-networking
seo_title: Les protocoles TCP et UDP – Expliqués en termes simples
seo_desc: 'Did you know that it''s thanks to the TCP and UDP protocols that the internet
  works?

  But what do these acronyms mean?

  Well, TCP stands for Transmission Control Protocol and UDP stands for User Datagram
  Protocol

  Ok, but what are they? Why are they usef...'
---

Saviez-vous que c'est grâce aux protocoles TCP et UDP que l'internet fonctionne ?

Mais que signifient ces acronymes ?

Eh bien, TCP signifie Transmission Control Protocol et UDP signifie User Datagram Protocol.

D'accord, mais qu'est-ce que c'est ? Pourquoi sont-ils utiles ? Pourquoi est-ce grâce à ces protocoles que l'internet fonctionne ?

Dans cet article, nous commencerons par une simple analogie pour vous aider à comprendre les idées derrière TCP et UDP. Ensuite, j'expliquerai comment ils fonctionnent en termes simples. Ensuite, nous discuterons de l'importance de ces protocoles et nous comprendrons leurs différences clés.

## Qu'est-ce que TCP et UDP ? Expliqué avec une analogie

![Image](https://www.freecodecamp.org/news/content/images/2023/03/letter.jpg)
_Photo par Suzy Hazelwood de Pexels : https://www.pexels.com/photo/shallow-focus-of-letter-paper-1157151/_

Vous pouvez penser à TCP et UDP de manière similaire à un service postal.

Tout comme un **service postal** envoie des **lettres** à des **individus**, TCP et UDP envoient des **paquets** à des **ordinateurs**.

Les paquets sont simplement des unités de données formatées en octets.

TCP fonctionne davantage comme un service de courrier recommandé. Avec le courrier recommandé, l'expéditeur envoie un colis à un destinataire et est notifié lorsque le colis est livré. L'expéditeur peut également suivre le colis s'il est perdu ou retardé.

En revanche, UDP est comme un service postal ordinaire. L'expéditeur envoie un colis sans confirmation de livraison. Il n'y a également aucun suivi ni garantie que le colis sera livré.

## Comment fonctionnent TCP et UDP ?

TCP et UDP sont tous deux des protocoles utilisés pour garantir que les données sont transmises de manière fiable et sécurisée entre les appareils sur un réseau.

TCP établit une connexion entre l'expéditeur et le destinataire, puis les données sont transmises entre les paquets.

TCP garantit également que tous les paquets sont livrés dans l'ordre. De plus, il dispose de mécanismes pour renvoyer les paquets perdus et gérer le contrôle de flux.

Pendant ce temps, UDP envoie des paquets sans établir de connexion. Pour cette raison, les paquets peuvent être perdus ou arriver dans le désordre, car il n'y a aucun mécanisme pour demander une retransmission.

## TCP vs UDP – Quelle est la différence ?

TCP et UDP ont tous deux été développés à partir des années 1980.

TCP est important en programmation car il fournit un moyen fiable et sécurisé pour que les appareils communiquent entre eux sur un réseau.

Sans TCP, il serait difficile pour les appareils de communiquer de manière sécurisée, et beaucoup des applications que nous utilisons aujourd'hui n'existeraient pas.

Par exemple, la communication par e-mail, les transferts de fichiers et les transactions en ligne seraient tous très difficiles sans TCP.

TCP est préféré pour la transmission de données sécurisée, ordonnée et fiable, ainsi que pour la livraison de grandes quantités de données avec un délai minimal et en atténuant la congestion du réseau.

UDP est également important pour les connexions qui nécessitent beaucoup de bande passante où la sécurité n'est pas un problème.

Par exemple, les services de streaming vidéo, les plateformes de jeux en ligne et les appareils IoT peuvent tous utiliser UDP pour transmettre des données.

## Conclusion

Grâce à ces protocoles, l'internet peut fonctionner en toute sécurité et les appareils peuvent communiquer efficacement entre eux.

Ces concepts sont clés à comprendre si vous êtes intéressé par les réseaux informatiques. Si vous souhaitez en savoir plus sur les réseaux, vous pouvez [lire ce tutoriel](https://www.freecodecamp.org/news/computer-networking-how-applications-talk-over-the-internet/).