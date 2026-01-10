---
title: Comment utiliser Wireshark, le meilleur analyseur de paquets
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-14T21:12:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-wireshark-packet-analyzer
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wireshark-1.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: penetration testing
  slug: penetration-testing
seo_title: Comment utiliser Wireshark, le meilleur analyseur de paquets
seo_desc: 'Wireshark is the best network traffic analyzer and packet sniffer around.
  In this article, we will look at it in detail.

  Wireshark is a network analyzer that lets you see what’s happening on your network.
  It lets you dissect your network packets at a...'
---

Wireshark est le meilleur analyseur de trafic réseau et renifleur de paquets. Dans cet article, nous allons l'examiner en détail.

Wireshark est un analyseur de réseau qui vous permet de voir ce qui se passe sur votre réseau. Il vous permet de disséquer vos paquets réseau à un niveau microscopique, vous donnant des informations détaillées sur les paquets individuels.

Wireshark a été publié pour la première fois en 1998 (et s'appelait Ethereal à l'époque). Il peut fonctionner sur tous les principaux systèmes d'exploitation. La plupart des entreprises et des organisations gouvernementales préfèrent désormais Wireshark comme analyseur de réseau standard.

Wireshark est également entièrement open-source, grâce à la communauté d'ingénieurs réseau du monde entier. Alors que la plupart des outils de sécurité sont basés sur CLI, Wireshark est livré avec une interface utilisateur fantastique.

## Modèle OSI

Je suppose que vous êtes nouveau dans le domaine des réseaux, nous allons donc passer en revue quelques bases du modèle OSI. Cela est important pour comprendre les fonctions principales de Wireshark.

Le modèle Open Systems Interconnection (OSI) standardise la manière dont deux appareils ou plus se connectent entre eux. Le modèle OSI segmente l'architecture réseau en 7 couches : Application, Présentation, Session, Transport, Réseau, Liaison de données et Physique.

Voici ce que fait chaque couche :

* Couche Physique

Responsable de la connexion physique réelle entre les appareils. Les données sont transférées sous forme de **bits**.
* Couche Liaison de données - S'assure que les données sont exemptes d'erreurs. Les données sont transférées en **trames**.
* Couche Réseau

S'occupe de trouver le meilleur (et le plus rapide) moyen d'envoyer les données. Les adresses IP de l'expéditeur et du destinataire sont ajoutées à l'en-tête à cette couche.
* Couche Transport

Fait office de pont entre la couche réseau et la couche session. Utilise des protocoles comme TCP et UDP pour envoyer et recevoir des données. Les données à cette couche sont appelées un **Segment**.
* Couche Session

Établit et maintient une session entre les appareils.
* Couche Présentation

Les données des segments sont converties en un format plus convivial pour l'homme ici. S'occupe du chiffrement et du déchiffrement.
* Couche Application

La couche qui interagit avec l'utilisateur. Si vous utilisez un navigateur, il se trouve sur la couche application.

Le diagramme ci-dessous devrait vous aider à comprendre comment ces composants fonctionnent ensemble.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-14-at-12.36.06-PM-1.png)
_Modèle OSI_

Si vous êtes intéressé à en apprendre davantage sur le modèle OSI, [voici un article détaillé pour vous](https://www.geeksforgeeks.org/layers-of-osi-model/).

## Paquets

Maintenant que vous avez une solide compréhension du modèle OSI, examinons les paquets réseau. Lorsque des données sont transférées d'un ordinateur à un autre, le flux de données se compose de plus petites unités appelées paquets.

Lorsque vous téléchargez un fichier depuis Internet, les données sont envoyées depuis le serveur sous forme de paquets. Ces paquets sont réassemblés par votre ordinateur pour vous donner le fichier original.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ipv4-packet.png)
_Paquet IPV4_

Un paquet peut contenir les données suivantes :

* adresses IP source et destination
* protocole
* ports source et destination
* données
* longueur, flags, TTL, etc.

Chaque paquet contient des informations précieuses sur les appareils impliqués dans un transfert de paquets. Chaque transfert de données implique des milliers, voire des millions de ces paquets de données envoyés entre les appareils source et destination.

Maintenant, vous pouvez comprendre l'importance de Wireshark. Wireshark vous permet de capturer chacun de ces paquets et de les inspecter pour obtenir des données.

Wireshark, pour un ingénieur réseau, est similaire à un microscope pour un biologiste. Wireshark vous permet d'« écouter » un réseau en direct (après avoir établi une connexion à celui-ci), et de capturer et d'inspecter les paquets à la volée.

En tant qu'ingénieur réseau ou hacker éthique, vous pouvez utiliser Wireshark pour déboguer et sécuriser vos réseaux. En tant que hacker malveillant (ce que je ne recommande pas), vous pouvez "renifler" les paquets dans le réseau et capturer des informations comme les transactions par carte de crédit.

C'est pourquoi il est imprudent de se connecter à un réseau public comme Starbucks et d'effectuer des transactions financières ou d'accéder à des données privées. Même si les sites avec HTTPS peuvent chiffrer vos paquets, ils sont toujours visibles sur le réseau. Si quelqu'un veut vraiment les craquer, il peut le faire.

## Bases de Wireshark

Maintenant, voyons comment vous pouvez utiliser Wireshark. [Téléchargez et installez Wireshark depuis ici](https://www.wireshark.org/#download).

Wireshark dispose d'une interface graphique fantastique, contrairement à la plupart des outils de test de pénétration. Voici à quoi ressemble Wireshark lorsque vous le chargez.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/wireshark-ui-2.png)
_Démarrage de Wireshark_

Wireshark liste les réseaux auxquels vous êtes connecté et vous pouvez en choisir un et commencer à écouter le réseau.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/wireshark-main.png)
_Interface utilisateur de Wireshark_

Il y a trois panneaux dans Wireshark.

### Panneau de liste des paquets

Ce panneau affiche les paquets capturés. Chaque ligne représente un paquet individuel que vous pouvez cliquer et analyser en détail en utilisant les deux autres panneaux.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-4.png)
_Panneau de liste des paquets_

### Panneau de détails des paquets

Vous pouvez sélectionner un paquet et ensuite examiner les informations du paquet plus en détail en utilisant le panneau de détails des paquets. Il affiche des informations telles que les adresses IP, les ports et autres informations contenues dans le paquet.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-4.png)
_Panneau de détails des paquets_

### Panneau d'octets des paquets

Ce panneau donne les données brutes du paquet sélectionné en octets. Les données sont affichées sous forme de vidage hexadécimal, qui affiche les données binaires en hexadécimal.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-3.png)
_Panneau d'octets des paquets_

## Filtres

Wireshark dispose de filtres qui vous aident à affiner le type de données que vous recherchez. Il existe deux principaux types de filtres : le filtre de capture et le filtre d'affichage.

### Filtre de capture

Vous pouvez définir un filtre de capture avant de commencer à analyser un réseau. Lorsque vous définissez un filtre de capture, il ne capture que les paquets qui correspondent au filtre de capture.

Par exemple, si vous devez uniquement écouter les paquets envoyés et reçus depuis une adresse IP, vous pouvez définir un filtre de capture comme suit :

```
host 192.168.0.1
```

Une fois que vous avez défini un filtre de capture, vous ne pouvez pas le modifier jusqu'à ce que la session de capture actuelle soit terminée.

### Filtres d'affichage

Les filtres d'affichage sont appliqués aux paquets capturés. Par exemple, si vous souhaitez afficher uniquement les requêtes provenant d'une IP particulière, vous pouvez appliquer un filtre d'affichage comme suit :

```
ip.src==192.168.0.1
```

Puisque les filtres d'affichage sont appliqués aux données capturées, ils peuvent être modifiés à la volée.

En résumé, les filtres de capture vous permettent de filtrer le trafic tandis que les filtres d'affichage appliquent ces filtres sur les paquets capturés. Puisque Wireshark peut capturer des centaines de paquets sur un réseau occupé, ceux-ci sont utiles lors du débogage.

## Fonctionnalités principales de Wireshark

Maintenant que vous avez une bonne compréhension des bases de Wireshark, examinons quelques fonctionnalités principales. Avec Wireshark, vous pouvez :

* Identifier les menaces de sécurité et les activités malveillantes sur un réseau
* Observer le trafic réseau pour déboguer des réseaux complexes
* Filtrer le trafic en fonction des protocoles, des ports et d'autres paramètres
* Capturer des paquets et les sauvegarder dans un fichier Pcap pour une analyse hors ligne
* Appliquer des règles de coloration à la liste des paquets pour une meilleure analyse
* Exporter les données capturées vers un fichier XML, CSV ou texte brut.

## Conclusion

Wireshark est toujours classé parmi les 10 meilleurs outils de sécurité réseau chaque année. Avec son interface utilisateur simple mais puissante, Wireshark est facile à apprendre et à utiliser. C'est un atout précieux dans la boîte à outils de chaque testeur de pénétration.

J'espère que cet article vous a aidé à avoir une solide compréhension de Wireshark. J'ai récemment écrit un article sur [les 10 outils que vous devriez connaître en tant qu'ingénieur en cybersécurité](https://www.freecodecamp.org/news/10-tools-you-should-know-as-a-cybersecurity-engineer/). N'hésitez pas à le consulter si vous êtes intéressé par la cybersécurité.

_Je rédige régulièrement des articles sur le Machine Learning, la Cybersécurité et DevOps. Vous pouvez vous inscrire à ma_ [_newsletter hebdomadaire_](https://www.manishmshiva.com/) _ici._