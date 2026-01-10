---
title: Qu'est-ce que le modèle OSI ? Réseautage informatique pour débutants
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2021-10-04T16:27:49.000Z'
originalURL: https://freecodecamp.org/news/osi-model-computer-networking-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/banner-1.jpg
tags:
- name: computer networking
  slug: computer-networking
seo_title: Qu'est-ce que le modèle OSI ? Réseautage informatique pour débutants
seo_desc: 'In this article, you will learn about the core concepts of the Open Systems
  Interconnections (OSI) model in a simple and easy way.

  As a developer, it''s a good idea to learn how things work "under the hood". That
  way you understand what your code and ...'
---

Dans cet article, vous apprendrez les concepts de base du modèle Open Systems Interconnections (OSI) de manière simple et facile.

En tant que développeur, il est bon de comprendre comment les choses fonctionnent "sous le capot". Ainsi, vous comprenez ce que votre code et les outils que vous utilisez font réellement.

Mais il peut sembler plus facile de s'appuyer sur l'abstraction de la boîte noire et d'ignorer le fonctionnement interne.

Une abstraction de boîte noire populaire est l'internet.

Bien sûr, beaucoup d'entre nous connaissent probablement les bases de ce qu'est l'internet et comment il fonctionne. Il y a un client et un serveur qui "communiquent" simplement entre eux en utilisant quelque chose appelé HTTP ou HTTPS ?

Mais c'est là que s'arrête la connaissance de la plupart des gens.

Je ne dis pas que nous ne devrions pas utiliser les abstractions – je dis simplement que nous devrions avoir une idée de base de comment les choses fonctionnent.

C'est pourquoi j'écris cet article : pour démystifier cette boîte noire et vous aider à apprendre comment les ordinateurs communiquent entre eux sur un réseau.

## Qu'est-ce que le modèle OSI ?

![Image](https://www.freecodecamp.org/news/content/images/2021/10/osi-model-layers.png)
_Les sept couches du modèle OSI_

Le modèle Open Systems Interconnection ou OSI est essentiellement un système de référence qui décrit comment les ordinateurs communiquent entre eux sur un réseau.

Il a été créé en 1983 par des représentants de sociétés de télécommunications et officiellement standardisé en 1984 par l'Organisation internationale de normalisation (ISO).

Il est divisé en sept couches. Chaque couche a son propre domaine et reçoit des données de la couche précédente, tout en passant des données à la couche suivante.

Les sept couches sont :

1. Couche Application
2. Couche Présentation
3. Couche Session
4. Couche Transport
5. Couche Réseau
6. Couche Liaison de données
7. Couche Physique

Si nous pensons en termes de codage, chaque couche est une classe avec une certaine fonctionnalité principale, et chaque classe communique uniquement avec la classe au-dessus ou en dessous d'elle.

Gardez à l'esprit que ceci est un modèle de **référence**, ce qui signifie que nous ne l'utilisons pas réellement dans la vie réelle. Il existe un autre modèle très similaire au modèle OSI, mais il encapsule les trois premières couches et les deux dernières.

Ce modèle "de la vie réelle" est appelé le modèle TCP/IP, sur lequel fonctionne l'internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/osi-vs-tcpip-1.png)
_Diagramme OSI vs modèle TCP/IP_

Mais avant de plonger et de traiter chaque couche une par une, voyons pourquoi vous devriez apprendre le modèle OSI s'il n'est même pas utilisé dans la vie réelle.

## Pourquoi apprendre le modèle OSI

Au cours des 20 dernières années, le monde a considérablement changé.

L'internet est arrivé, le "web" est arrivé, et dans l'écosystème web, beaucoup de choses ont changé. Nous avons commencé avec des pages HTML simples, puis est venu JavaScript, et maintenant nous avons tous ces frameworks et parfois cela semble si écrasant.

Mais vous devez vous rappeler ceci :

> Apprenez les fondamentaux, apprenez à partir des premiers principes.

Prenons le web, par exemple, en dehors de tous ces changements que nous avons vus au cours des 20 dernières années.

Le fonctionnement du web n'a pas réellement changé.

Nous utilisons toujours le protocole HTTP.

Il est vrai que le protocole HTTP a été mis à jour, mais pas tant que cela.

Même si nous décomposons HTTP, il est constitué de TCP qui n'a pas non plus beaucoup changé.

Mon propos est que vous devriez cesser de regarder les nouvelles choses brillantes et vous concentrer sur les fondamentaux sur lesquels ces nouvelles choses brillantes sont construites.

Par exemple, je me souviens quand les web sockets étaient une chose populaire.

Mais si nous les décomposons, ils sont basés sur le protocole TCP.

Si vous connaissez TCP, vous pouvez facilement comprendre comment fonctionnent les web sockets et ne pas avoir à vous appuyer sur des abstractions de boîte noire.

J'espère vous avoir convaincu de pourquoi vous devriez apprendre à partir des premiers principes. Cela ne s'applique pas seulement au génie logiciel mais à de nombreux autres domaines également.

Cela étant fait, passons en revue les sept couches du modèle OSI.

## Les sept couches du modèle OSI

### Couche Application

![Image](https://www.freecodecamp.org/news/content/images/2021/09/3.png)
_C'est la couche où se trouve l'utilisateur final_

La couche application est celle où la plupart des ingénieurs logiciels travaillent. Et c'est là que vivent vos navigateurs.

Mais je ne parle pas d'applications concrètes comme Chrome, Skype ou Outlook.

Je parle de choses plus fondamentales, comme les protocoles.

Par exemple :

* Votre navigateur fait une requête à un serveur web en utilisant le protocole HTTP.
* Votre application de messagerie utilise le protocole SMTP pour envoyer et recevoir des e-mails.
* Sans le protocole DNS, vous devriez taper 142.250.150.138 au lieu de google.com.

En résumé, la couche application gère la fondation que presque toutes les applications utilisateur final utilisent.

### Couche Présentation

![Image](https://www.freecodecamp.org/news/content/images/2021/09/4.png)

Une fois que le client fait la requête HTTP, la requête elle-même est transmise à la couche présentation (également appelée couche syntaxique).

Cette couche gère trois fonctionnalités principales :

#### Chiffrement et déchiffrement

Vous ne voulez pas que vos données soient publiques, c'est pourquoi des personnes intelligentes ont créé le Transport Layer Security (TLS). Il chiffrera essentiellement vos données.

Il est également responsable du déchiffrement des requêtes provenant d'autres serveurs pour être consommées par la couche application.

#### Sérialisation et désérialisation

Ce sont de grands mots, mais ce qu'ils signifient essentiellement, c'est "traduction".

Nous voulons "traduire" nos données dans des formes que notre application comprend.

Par exemple, des structures de données simples peuvent être traduites en "objets" que notre application JavaScript comprend.

D'autre part, si nous voulons que nos données passent à la couche suivante, nous traduirons notre objet en structures de données simples qui pourraient être comprises dans les couches inférieures.

#### Compression

C'est une évidence : moins il y a de bits à envoyer, plus la requête sera rapide.

C'est aussi l'une des principales fonctions de la couche présentation. Gardez à l'esprit qu'il s'agit d'une compression sans perte, ce qui signifie qu'aucune information ne sera perdue dans le processus.

Pour être honnête, dans le monde réel, la plupart de ces choses sont faites dans la couche application.

C'est pourquoi dans le modèle TCP/IP, la couche présentation fait partie de la couche application.

### Couche Session

![Image](https://www.freecodecamp.org/news/content/images/2021/09/5-1.png)
_La couche session est responsable de l'ouverture, de la fermeture et de la maintenance des connexions entre le client et le serveur_

Celle-ci est un peu confuse. Et en fait, je n'ai pas trouvé beaucoup de cas d'utilisation pour elle.

La fonction principale de la couche session est de gérer les connexions entre le client et le serveur.

Mais qu'est-ce que cela signifie réellement ?

Donc, disons que vous voulez aller sur google.com

Pour cela, vous devez d'abord établir une connexion avec google.com, donc vous dites "Hey serveur, quoi de neuf, je veux me connecter à google.com".

Le serveur répond : "Oui, bien sûr."

Félicitations, vous venez d'établir une connexion avec le serveur de google.com et pouvez librement envoyer une requête GET pour récupérer la page.

En résumé, cette couche est utilisée pour :

* Ouvrir des connexions
* Maintenir des connexions en vie
* Fermer des connexions.

Maintenant, la vérification de la réalité : dans la vie réelle, cela n'existe pratiquement pas et fait partie de la couche Transport – que nous discuterons ensuite.

### Couche Transport

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Transport-Layer.png)
_TCP et UDP visualisés_

C'est là que les choses intéressantes se passent.

La couche transport est généralement définie en fonction du protocole utilisé.

Les [deux plus populaires sont](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/) :

* Transmission Control Protocol (TCP)
* User Datagram Protocol (UDP)

TCP est l'un des principaux protocoles de la suite internet. Il est utilisé sur le protocole IP (Internet Protocol) pour assurer une transmission fiable des paquets.

TCP corrige de nombreux problèmes qui surviennent lorsque vous utilisez IP, tels que les paquets perdus, les paquets hors d'ordre, les paquets dupliqués et les paquets corrompus.

Vous utiliseriez TCP dans des applications qui nécessitent que tous les paquets soient exempts d'erreurs, comme la messagerie texte.

D'autre part, UDP est sans état, ce qui signifie qu'il ne sauvegarde aucun état entre le client et le serveur. Il est également très léger, ce qui le rend rapide. Mais l'inconvénient est qu'il n'est pas fiable, les paquets peuvent se perdre, être corrompus, etc.

UDP est principalement utilisé lorsque vous ne vous souciez pas vraiment de perdre quelques paquets ici et là, comme le streaming vidéo.

Gardez également à l'esprit que les données dans cette couche sont appelées segments.

En résumé, TCP est fiable mais lent, tandis que UDP est non fiable mais rapide.

### Couche Réseau

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Network-Layer-1.png)
_La couche réseau est responsable de l'envoi de paquets d'un réseau à un autre_

Je ne sais pas vraiment pourquoi cela s'appelle la couche réseau.

Elle devrait s'appeler la couche internet – car le protocole le plus important ici est le protocole Internet (IP).

Ce que fait essentiellement l'IP, c'est qu'il prend les segments du protocole de transport et ajoute des méta-données qui aident à identifier où se trouve votre client dans un réseau local.

Une autre fonction de la couche réseau est le transfert de messages, ce qui signifie qu'elle envoie vos paquets d'un réseau à un autre.

Les données dans cette couche sont appelées paquets.

### Couche Liaison de données

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Data-Link-Layer.png)
_La couche liaison de données est composée de deux parties : MAC et LLC_

Cette couche définit comment les données sont transmises entre deux systèmes.

Elle prend en charge des choses comme la durée pendant laquelle deux systèmes se parlent, la quantité de données qui peut être envoyée et ce qui se passe s'il y a des erreurs. Tout cela est géré dans la couche Liaison de données.

La couche liaison de données est divisée en deux sous-couches :

* Logical Link Layer (LLC) – Cette couche fournit un contrôle de flux, un accusé de réception et une gestion des erreurs en cas de problème.
* Media Access Control (MAC) – Cette couche est responsable de l'attribution d'un numéro d'identification unique basé sur votre carte réseau appelé adresse MAC. Ce qui signifie que deux appareils n'ont pas la même adresse MAC.

Les paquets sont pris de la couche réseau et sont encapsulés avec l'ajout de nouveaux en-têtes pour l'adresse MAC du client et du serveur.

Il y a également un autre sous-ensemble de données ajouté à la fin du paquet qui est utilisé pour la détection d'erreurs. Cela s'appelle la queue.

Une fois ces méta-données ajoutées, les données sont maintenant appelées une trame.

### Couche Physique

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Physical-Layer.png)
_Les bits peuvent être transférés en utilisant l'électricité, les ondes radio, ou même la lumière_

Enfin, voici la couche physique.

Ne vous laissez pas tromper par le mot physique – nous ne parlons pas seulement de fils.

Les données peuvent être transférées de nombreuses manières différentes, comme les ondes radio ou même la lumière.

Malheureusement, ces moyens de transport ne connaissent pas les "trames", ils ne connaissent que les bits.

La fonction de cette couche est simplement de transformer les trames en octets (8 bits) et de les envoyer via une méthode de transport (électricité, ondes, lumière, etc.).

Enfin, notre requête sera transmise au serveur, et le serveur passera par le même processus mais à l'envers.

## Conclusion

Dans cet article, vous avez appris :

* Que le modèle OSI est un modèle de référence sur la manière dont deux systèmes communiquent entre eux sur un réseau.
* Nous n'utilisons pas ce modèle dans la vie réelle. Au lieu de cela, nous utilisons un autre modèle similaire appelé le modèle TCP/IP.
* Le modèle OSI est composé de sept parties, chacune avec une fonction spécifique.

J'espère que vous avez appris quelque chose aujourd'hui et je tiens à vous remercier d'être arrivé à la fin.

Je prévois de publier des extraits de contenu similaires à celui-ci sur Twitter, donc si vous êtes intéressé, suivez-moi [@tamerlan_dev](https://twitter.com/tamerlan_dev).