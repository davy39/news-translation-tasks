---
title: Qu'est-ce que le modèle TCP/IP ? Explication des couches et des protocoles
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-11-30T23:25:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover-2.png
tags:
- name: internet
  slug: internet
seo_title: Qu'est-ce que le modèle TCP/IP ? Explication des couches et des protocoles
seo_desc: "A significant part of the process of creating something is the ability\
  \ to imagine things that do not yet exist. \nThis skill was instrumental to the\
  \ creation of the Internet. If no one had imagined the underlying technology that\
  \ most now take for gran..."
---

Une partie importante du processus de création de quelque chose est la capacité à imaginer des choses qui n'existent pas encore. 

Cette compétence a été instrumentale dans la création de l'Internet. Si personne n'avait imaginé la technologie sous-jacente que la plupart prennent maintenant pour acquise chaque jour, il n'y aurait pas de mèmes de chats.

Pour rendre l'Internet possible, deux choses qui devaient être imaginées étaient les _couches_ et les _protocoles_.

Les couches sont des divisions conceptuelles qui regroupent des fonctions similaires ensemble. Le mot « protocole » signifie « la manière dont nous avons convenu de faire les choses ici », plus ou moins.

En bref, les couches et les protocoles peuvent être expliqués à un enfant de cinq ans comme « des idées sur lesquelles les gens se sont mis d'accord et qu'ils ont écrites pour que d'autres personnes puissent faire des choses avec les mêmes idées ».

La suite de protocoles Internet est décrite en termes de couches et de protocoles. Collectivement, la suite fait référence aux protocoles de communication qui permettent notre défilement sans fin.

Elle est souvent appelée par ses protocoles fondateurs : le Transmission Control Protocol (TCP) et l'Internet Protocol (IP). Regroupés sous le nom TCP/IP, ces protocoles décrivent comment les données sur l'Internet sont emballées, adressées, envoyées et reçues.

Voici pourquoi la suite de protocoles Internet, ou TCP/IP, est un gâteau arc-en-ciel imaginaire à couches.

## **Les couches sont imaginaires**

Si vous considérez la nature générale d'un gâteau arc-en-ciel à couches, il est principalement composé de douceur vanillée qui fond dans la bouche. Cette douceur est elle-même composée de quelque chose comme des œufs, du beurre, de la farine et un édulcorant.

![Dessin animé d'une tranche de gâteau arc-en-ciel à couches, avec la mention « Yay ! Free cake ! »](https://www.freecodecamp.org/news/content/images/2020/11/free-cake.png)

Il n'y a pas grand-chose pour distinguer une couche d'un gâteau arc-en-ciel à couches d'une autre. Souvent, la seule différence entre les couches est la coloration alimentaire et un peu de glaçage. Lorsque vous y pensez, c'est du gâteau du haut en bas. Les couches arc-en-ciel ne sont là que parce que le boulanger a pensé qu'elles devraient l'être.

De manière similaire aux ingrédients du gâteau, les couches dans le contexte de la mise en réseau informatique sont principalement composées de protocoles, d'algorithmes et de configurations, avec quelques données saupoudrées.

Il peut être plus facile de parler de la mise en réseau informatique si ses nombreuses fonctions sont divisées en groupes, donc certaines personnes ont inventé des descriptions de couches, que nous appelons des modèles de réseau. TCP/IP n'est qu'un modèle de réseau parmi d'autres. En ce sens, les couches sont des concepts, pas des choses.

Certaines des personnes en question font partie de l'Internet Engineering Task Force (IETF). Elles ont créé la publication [RFC-1122](https://tools.ietf.org/html/rfc1122), discutant des couches de communication de l'Internet. La moitié d'un tout, la norme :

> ...couvre les couches de protocoles de communication : couche de liaison, couche IP et couche de transport ; sa compagne [RFC-1123](https://tools.ietf.org/html/rfc1123) couvre les protocoles d'application et de support.

Les couches décrites par RFC-1122 et RFC-1123 encapsulent chacune des protocoles qui satisfont la fonctionnalité de la couche. Examinons chacune de ces couches de communication et voyons comment TCP et IP s'empilent dans ce modèle de gâteau à couches Internet.

## **Protocoles de la couche de liaison**

![Dessin animé de la couche de liaison du gâteau](https://www.freecodecamp.org/news/content/images/2020/11/link.png)

La [couche de liaison](https://tools.ietf.org/html/rfc1122#page-21) est la classification la plus basique, ou de plus bas niveau, du protocole de communication. Elle traite de l'envoi d'informations entre hôtes sur le même réseau local et de la traduction des données des couches supérieures vers la couche physique.

Les protocoles de la couche de liaison décrivent comment les données interagissent avec le support de transmission, tel que les signaux électroniques envoyés sur du matériel spécifique. Contrairement aux autres couches, les protocoles de la couche de liaison dépendent du matériel utilisé.

## **Protocoles de la couche Internet**

Les protocoles de la [couche Internet](https://tools.ietf.org/html/rfc1122#page-27) décrivent comment les données sont envoyées et reçues sur l'Internet. Le processus implique l'emballage des données en paquets, l'adressage et la transmission des paquets, et la réception des paquets de données entrants.

![Dessin animé de la couche Internet du gâteau](https://www.freecodecamp.org/news/content/images/2020/11/internet.png)

Le protocole le plus connu de cette couche donne à TCP/IP ses deux dernières lettres. IP est un protocole sans connexion, ce qui signifie qu'il ne garantit pas que les paquets sont envoyés ou reçus dans le bon ordre, le long du même chemin, ou même dans leur intégralité.

La fiabilité est gérée par d'autres protocoles de la suite, tels que ceux de la couche de transport.

Il existe actuellement deux versions de IP en utilisation : IPv4 et IPv6. Les deux versions décrivent comment les appareils sur l'Internet se voient attribuer des adresses IP, qui sont utilisées lors de la navigation vers des mèmes de chats.

IPv4 est plus largement utilisé, mais n'a que [32 bits pour l'adressage](https://tools.ietf.org/html/rfc791#section-2.3), permettant environ 4,3 milliards (environ 4,3×10<sup>9</sup>) d'adresses possibles. Celles-ci s'épuisent, et IPv4 finira par souffrir d'épuisement d'adresses à mesure que de plus en plus de personnes utilisent plus d'appareils sur l'Internet.

La version successeur IPv6 vise à résoudre l'épuisement des adresses en [utilisant 128 bits pour les adresses](https://tools.ietf.org/html/rfc8200#section-1). Cela fournit, euh, beaucoup plus de possibilités d'adresses (environ 3,4×10<sup>38</sup>).

## **Protocoles de la couche de transport**

En mai 1974, Vint Cerf et Bob Kahn (collectivement souvent appelés « les pères de l'Internet ») ont publié un article intitulé [A Protocol for Packet Network Intercommunication](https://web.archive.org/web/20160304150203/http://ece.ut.ac.ir/Classpages/F84/PrincipleofNetworkDesign/Papers/CK74.pdf).

Cet article contenait la première description d'un Transmission Control Program, un concept englobant ce qui serait finalement connu sous le nom de Transmission Control Protocol (TCP) et User Datagram Protocol (UDP). (J'ai eu le plaisir de rencontrer Vint et peux personnellement confirmer que oui, il ressemble exactement à l'Architecte dans les films Matrix.)

![Dessin animé de la couche de transport du gâteau](https://www.freecodecamp.org/news/content/images/2020/11/transport.png)

La [couche de transport](https://tools.ietf.org/html/rfc1122#page-77) encapsule actuellement TCP et UDP. Comme IP, UDP est sans connexion et peut être utilisé pour prioriser le temps sur la fiabilité.

TCP, en revanche, est un protocole de couche de transport orienté connexion qui priorise la fiabilité sur la latence, ou le temps. TCP décrit le transfert de données dans le même ordre qu'elles ont été envoyées, la retransmission des paquets perdus et les contrôles affectant le taux de transmission des données.

## **Protocoles de la couche application**

![Dessin animé de la couche application du gâteau](https://www.freecodecamp.org/news/content/images/2020/11/application.png)

La couche application décrit les protocoles avec lesquels les applications logicielles interagissent le plus souvent. La spécification inclut des descriptions du protocole de connexion à distance [Telnet](https://tools.ietf.org/html/rfc1123#section-3), du [File Transfer Protocol (FTP)](https://tools.ietf.org/html/rfc1123#section-4) et du [Simple Mail Transfer Protocol (SMTP)](https://tools.ietf.org/html/rfc1123#section-5).

Sont également inclus dans la couche application le Hypertext Transfer Protocol (HTTP) et son successeur, Hypertext Transfer Protocol Secure (HTTPS).

HTTPS est sécurisé par Transport Layer Security, ou TLS, qui peut être considéré comme la couche la plus élevée du modèle de réseau décrit par la suite de protocoles Internet.

Si vous souhaitez mieux comprendre TLS et comment ce protocole sécurise votre visualisation de mèmes de chats, je vous invite à [lire mon article sur TLS et la cryptographie](https://victoria.dev/blog/tls).

## **Le gâteau Internet est encore en train de cuire**

Comme un gâteau qui lève encore, des descriptions de couches, de meilleurs protocoles et de nouveaux modèles sont développés chaque jour. L'Internet, ou ce qu'il deviendra dans le futur, est encore en train d'être imaginé.

![Dessin animé du gâteau complet à couches Internet, surmonté de mèmes Nyan Cat](https://www.freecodecamp.org/news/content/images/2020/11/cake.png)

Si vous avez aimé apprendre de cet article, il y en a beaucoup plus d'où cela vient ! J'écris sur l'informatique, la cybersécurité et la construction de grandes équipes techniques. Rejoignez les milliers de personnes qui apprennent de mes articles sur [victoria.dev](https://victoria.dev)! Visitez et abonnez-vous par email ou RSS pour voir les nouveaux articles en premier.