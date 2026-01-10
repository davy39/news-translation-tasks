---
title: Tutoriel sur les réseaux informatiques – Comment les applications réseau communiquent
  via Internet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T19:54:27.000Z'
originalURL: https://freecodecamp.org/news/computer-networking-how-applications-talk-over-the-internet
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/network-applications-article-image.jpeg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: internet
  slug: internet
seo_title: Tutoriel sur les réseaux informatiques – Comment les applications réseau
  communiquent via Internet
seo_desc: "By Sahil Gupta\nNetwork applications are computer applications that participate\
  \ in a computer network. These applications talk to each other by plugging into\
  \ the network. \nFor example, when you visit google.com, your browser acts as a\
  \ network applicat..."
---

Par Sahil Gupta

Les applications réseau sont des applications informatiques qui participent à un réseau informatique. Ces applications communiquent entre elles en se connectant au réseau. 

Par exemple, lorsque vous visitez google.com, votre navigateur agit comme une application réseau qui utilise l'[Internet](https://en.wikipedia.org/wiki/Internet) pour communiquer avec l'application réseau s'exécutant sur l'ordinateur de Google. 

Généralement, les mécanismes de cette communication sont abstraits pour le développeur d'applications.

En surface, cette communication peut sembler être une [Communication Inter-Processus](https://en.wikipedia.org/wiki/Inter-process_communication) entre [deux applications s'exécutant sur le même ordinateur](https://en.wikipedia.org/wiki/Unix_domain_socket). Mais la communication réseau présente un ensemble différent de défis. 

Par exemple, la communication peut prendre une éternité en temps informatique. Il faut 0,1337 seconde (2 * 3,14 * 6400 / 30000) pour que la lumière fasse le tour de la Terre. En supposant un CPU modeste fonctionnant à 1 GHz, il peut effectuer 10^9 opérations en 1 seconde. 

Supposons qu'il faille quelques opérations pour que les processus (s'exécutant sur la même machine) communiquent, soit environ 10^-7 - 10^-8 secondes. Cela se traduit par des temps de communication ~1 million de fois plus lents avec un ordinateur situé de l'autre côté de la Terre !

Cet article examinera comment les applications réseau communiquent entre elles, spécifiquement via Internet. Pour un aperçu de haut niveau de l'Internet, voir [cet article](https://blog.devgenius.io/how-does-the-internet-work-256891cdbb77).

## Introduction aux réseaux informatiques

Une complexité supplémentaire impliquée dans la communication réseau est la diversité des systèmes finaux (téléphones mobiles, ordinateurs portables, Windows, Mac). Cette complexité est gérée en [abstrayant](https://en.wikipedia.org/wiki/Abstraction_(computer_science)) les différences et en introduisant un ensemble uniforme de règles appelées [**Protocoles**](https://en.wikipedia.org/wiki/Communication_protocol). 

Les protocoles sont les éléments de base de la communication entre les applications réseau. Certains des protocoles populaires incluent HTTP, TCP, IP, SMTP. Comme une langue humaine (comme l'anglais) permet à des personnes diverses de communiquer de manière significative, les protocoles comblent une lacune similaire dans la communication réseau.

La communication réseau est difficile en raison de l'échelle et de l'incertitude inhérentes au réseau. 

Par exemple, les liens peuvent être encombrés, ce qui entraîne la perte de paquets. Une stratégie pour résoudre un problème compliqué consiste à diviser le problème en sous-problèmes, à résoudre les sous-problèmes et à les combiner pour résoudre le problème original. 

[La pile de protocoles](https://en.wikipedia.org/wiki/Protocol_stack) utilise cette idée pour résoudre la communication réseau.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1-1.png)
_Pile de protocoles_

Imaginez que vous construisez un site web pour vendre des pizzas. Lorsque l'utilisateur interagit avec votre site web, le frontend doit communiquer avec votre serveur backend. Ne serait-il pas agréable de pouvoir vous concentrer sur la construction de votre boutique de pizza en ligne sans avoir à vous soucier de la manière dont ces données sont transmises du frontend au serveur backend via Internet ? 

La pile de protocoles s'occupe de la communication réseau pour nous. Une application (frontend) utilise la couche Application pour communiquer avec une autre application (backend). 

La couche application utilise les "services" fournis par la couche Transport pour transmettre des informations à travers le réseau. La couche Transport utilise également les services fournis par la couche Réseau pour remplir son accord de service. 

De cette manière, la couche supérieure utilise les services fournis par les couches inférieures pour communiquer avec d'autres applications via le réseau. La couche Physique constitue les fils qui transportent le signal électrique.

En essence, la pile de protocoles contient diverses couches, où chaque couche se concentre sur la résolution d'une partie du problème plus large.

Les protocoles décrivent la solution aux sous-problèmes, ce qui nous donne le nom de pile de protocoles. Généralement, les protocoles définissent les règles de communication entre deux entités telles que,

* Types de messages, par exemple, messages de requête et de réponse
* Syntaxe des différents types de messages tels que les champs dans les messages
* La sémantique des champs, c'est-à-dire la signification des informations dans les champs
* Règles pour déterminer quand et comment les messages sont envoyés et répondus

Plongeons plus profondément dans la pile de protocoles, en commençant par le haut.

## La couche Application

Les applications métiers utilisent la couche Application pour communiquer via un réseau. Par exemple, passer une commande sur votre boutique de pizza en ligne est fait en utilisant la couche Application. [HTTP](https://en.wikipedia.org/wiki/POST_(HTTP)) est une option pour publier les informations sur votre serveur backend.

Les protocoles de la couche Application définissent comment les applications s'exécutant sur différents systèmes finaux s'échangent des messages. En plus des règles de communication (protocole), les applications ont également besoin d'un moyen de se trouver, c'est-à-dire de s'adresser mutuellement. L'adresse d'une application est définie par :

1.  [Adresse IP](https://en.wikipedia.org/wiki/IP_address) : étiquette numérique assignée à un système final
2. [Numéro de port](https://en.wikipedia.org/wiki/Port_(computer_networking)) : un identifiant qui spécifie le processus de réception dans l'hôte de destination. Les numéros de port sont essentiels pour tenir compte de plusieurs applications réseau s'exécutant sur un hôte. Par exemple, [deux onglets dans un navigateur web agissent comme deux processus différents](https://superuser.com/questions/1055281/do-web-browsers-use-different-outgoing-ports-for-different-tabs).

L'adresse d'une application définit son identité sur le réseau, et le protocole définit les règles de communication. Ensemble, ceux-ci forment l'adresse de [Socket](https://en.wikipedia.org/wiki/Network_socket) (type de protocole, adresse IP, numéro de port). 

Un **socket** est une [interface](https://en.wikipedia.org/wiki/Interface_(computing)) entre la couche application et la couche transport. Il agit comme un point d'entrée dans le réseau, c'est-à-dire qu'une application envoie des messages dans et reçoit des messages réseau à travers son Socket.

En résumé, les applications communiquent entre elles en utilisant des protocoles de la couche Application. La couche Application s'appuie sur les services fournis par la couche Transport pour transmettre des données entre les systèmes finaux. Une paire d'adresse IP et de numéro de port identifie une application. Les informations circulent d'une application vers le réseau à travers son Socket.

Regardons un exemple de deux applications communiquant via Internet en utilisant HTTP. 

HTTP est un protocole populaire de la couche application. La communication se fait entre mon navigateur web et un serveur d'application ([ilovecookies.com](http://ilovecookies.com/)). Lorsque je saisis cette adresse dans mon navigateur web, il envoie un message de requête HTTP au serveur d'application.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2-2.png)
_Message de requête HTTP envoyé par mon navigateur web au serveur ilovecookies.com_

Quelques points à noter sur ce message de requête :

* Le type de requête est GET
* L'hôte auquel il envoie le message est ilovecookies.com (version lisible par l'homme des adresses IP appelée [noms d'hôte](https://en.wikipedia.org/wiki/Hostname))
* La machine source accepte des formats de réponse spécifiques, des langues, etc.

Cette structure fait partie du [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP/1.1_request_messages) qui définit les règles de communication entre deux applications. Lorsque l'application hôte reçoit ce message, elle répond avec un message de réponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-3.png)
_Message de réponse HTTP reçu par mon navigateur web depuis le serveur ilovecookies.com contenant le HTML pour générer la page web_

Nous pouvons observer que le message de réponse contient des données spécifiques au protocole telles que le code d'état (200), le type de contenu, etc., et les données HTML (tronquées pour s'adapter). La paire requête-réponse constitue la communication réseau entre deux applications qui affichent avec succès la page web (ilovecookies.com) sur mon écran.

## La couche Transport

Ensuite, descendons d'un niveau dans la pile de protocoles et comprenons comment la couche transport aide la communication réseau.

La couche transport fournit une communication [**logique**](https://www.pcmag.com/encyclopedia/term/logical-vs-physical) entre les applications s'exécutant sur différents hôtes : du point de vue des applications, c'est comme si les deux hôtes étaient directement connectés. Notez que la communication fournie par la couche transport est logique et non physique : il n'y a pas de lien ou de fil direct entre les hôtes finaux.

La couche transport convertit les messages d'application en morceaux plus petits, encapsule chaque morceau dans un message de transport contenant des en-têtes, et transmet le morceau à la couche réseau.

La raison derrière la division des informations en morceaux est l'utilisation efficace du réseau. L'Internet est si vaste que plusieurs chemins parallèles transmettent des données entre deux hôtes finaux. 

Par exemple, il y a deux chemins possibles pour voyager entre New York et Stamford. L'Internet est une version légèrement extrême de cette idée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/4-1.png)
_Deux routes alternatives entre New York et Stamford_

L'ordre relatif des paquets est une question naturelle autour de la fragmentation et de l'utilisation efficace du réseau : les morceaux doivent être remis dans le même ordre sur l'hôte de réception. La couche transport dans l'hôte de réception est responsable de l'assemblage des morceaux dans le bon ordre.

La couche transport a également besoin de certaines données supplémentaires pertinentes pour ses fonctions. Par exemple, des numéros de séquence relatifs sont ajoutés aux morceaux pour reconstituer le message de l'application. 

Un autre exemple d'information spécifique à la couche transport est le numéro de port. Sur l'hôte de réception, le numéro de port de destination est utile pour router le message vers l'application correcte.

L'Internet met à disposition deux protocoles de couche transport :

* User Datagram Protocol (UDP)
* Transmission Control Protocol (TCP)

Les deux protocoles varient légèrement dans les services de transport qu'ils fournissent à la couche application.

<table>
  <tr>
    <th>TCP</th>
    <th>UDP</th>
  </tr>
  <tr>
    <td>Transfert de données fiable</td>
    <td>Transfert de données non fiable</td>
  </tr>
  <tr>
    <td>Les informations perdues ou corrompues sont récupérées par retransmission</td>
    <td>Aucun mécanisme pour récupérer les données perdues ou corrompues</td>
  </tr>
  <tr>
    <td>Latence plus élevée au coût d'une communication fiable</td>
    <td>Latence plus faible au coût d'une communication non fiable</td>
  </tr>
</table>

Les exigences de service d'une application déterminent le protocole que vous choisissez. Par exemple, un système de paiement aura besoin d'une communication fiable (TCP), tandis qu'un service de streaming vidéo pourrait accepter de perdre certaines informations pour un streaming plus rapide (UDP).

En résumé, la couche transport divise les messages d'application en morceaux et les encapsule dans des messages contenant des informations spécifiques à la couche transport. Les morceaux sont remis dans le bon ordre sur le système de réception pour recréer le message et transmis à l'application appropriée en utilisant le numéro de port.

Continuons l'exemple de communication HTTP entre mon navigateur web et le serveur d'application.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/5-2.png)
_Paquet TCP encapsulant le message de requête HTTP et les en-têtes_

Vous pouvez observer les octets décodés en bas à droite représentant la requête HTTP GET que mon navigateur fait pour le serveur d'application. Nous voyons la requête HTTP comme un champ de charge utile TCP dans ce paquet. 

De plus, le paquet est le premier dans l'ordre relatif avec un numéro de séquence de 1. Il contient également le numéro de port (65012) associé à l'onglet de mon navigateur web et le numéro de port de destination ([80](https://en.wikipedia.org/wiki/Port_(computer_networking)#Common_port_numbers)) sur le serveur d'application.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/sequence-1-and-1449.jpg)
_Premier (numéro de séquence 1) et deuxième (numéro de séquence 1449 qui commence à la fin du paquet 1) paquets TCP correspondant au message de réponse HTTP reçu du serveur ilovecookies.com_

Les deux premiers paquets de la réponse HTTP (57 paquets TCP) sont affichés ici. Dans le coin inférieur droit des deux images, nous pouvons voir les informations spécifiques à HTTP et un peu de HTML correspondant à la page web ilovecookies.com. 

Vous pouvez également voir les informations spécifiques à la couche transport telles que les numéros de port et les numéros de séquence. Remarquez que les numéros de port source et de destination sont inversés par rapport aux paquets de message de requête.

## La couche Réseau

Contrairement à la couche transport, la couche réseau fournit une communication logique entre deux hôtes finaux. Notez la différence subtile entre les services de la couche transport et de la couche réseau.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/network-layer-hosts.jpg)
_Gauche : communication logique fournie par la couche transport, Droite : communication logique fournie par la couche réseau_

La couche réseau prend un paquet de transport de la couche transport et l'encapsule dans un paquet réseau. L'encapsulation est utile pour ajouter des informations spécifiques au fonctionnement du protocole de la couche réseau.

La couche réseau fournit un [service de meilleur effort](https://en.wikipedia.org/wiki/Best-effort_delivery) (le timing, l'ordre relatif, la livraison éventuelle ne sont pas garantis) pour déplacer des données entre deux hôtes. Le service de meilleur effort est la motivation derrière TCP. Comme les protocoles de la couche réseau sont intrinsèquement non fiables, TCP contient une logique supplémentaire pour garantir un transfert de données fiable.

La couche réseau est responsable du déplacement des paquets d'un hôte émetteur vers un hôte récepteur. En plus des hôtes finaux, les protocoles de la couche réseau s'exécutent également sur les **routeurs**, qui font partie du [noyau du réseau](https://en.wikipedia.org/wiki/Backbone_network). Les routeurs sont des dispositifs de commutation de paquets responsables de la transmission des paquets.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/packet-switching-and-small-network.jpg)
_Gauche : dispositif de commutation de paquets, Droite : un petit réseau composé de 3 hôtes finaux et de 1 routeur les connectant ensemble_

Supposons que l'hôte final 1 souhaite envoyer un paquet à l'hôte final 2. L'hôte final 1 transmet le paquet au routeur. Le routeur examine les informations dans le paquet réseau et détermine qu'il doit transmettre le paquet sur le lien 2, auquel l'hôte final 2 est connecté. 

Chaque routeur dispose d'une table de transmission stockée en RAM ([construite dynamiquement](https://en.wikipedia.org/wiki/Routing_protocol)) pour résoudre le lien de transmission correct pour le paquet. Par exemple, la table de routage pour la configuration ci-dessus ressemblera à ceci :

<table>
  <tr>
    <th>Adresse</th>
    <th>Lien</th>
  </tr>
  <tr>
    <td>192.168.1.1</td>
    <td>Lien 1</td>
  </tr>
  <tr>
    <td>168.134.1.1</td>
    <td>Lien 2</td>
  </tr>
  <tr>
    <td>172.158.1.2</td>
    <td>Lien 3</td>
  </tr>
</table>

Les routeurs utilisent les informations (adresse de l'hôte de destination) du paquet réseau pour indexer ([XOR bit à bit](https://en.wikipedia.org/wiki/Exclusive_or#Truth_table)) dans cette table. Vous pouvez voir la table de routage sur votre ordinateur en exécutant les commandes suivantes :

`Mac : netstat -nrf inet`
`Linux : netstat -nr`
`Windows : Get-NetRoute -AddressFamily IPv4`

Remarquez une entrée particulière dans votre table de routage, par défaut ou 0.0.0.0, appelée [passerelle par défaut](https://en.wikipedia.org/wiki/Default_gateway). Un paquet est routé vers la passerelle par défaut si aucune des entrées ne correspond à l'adresse de destination.

L'Internet contient des tonnes de tels dispositifs qui transmettent des paquets pour permettre la communication logique entre deux hôtes finaux. 

Comme tout le monde partage les routeurs et les fils transportant les données sur l'Internet, les routeurs contiennent des files d'attente qui retiennent les paquets entrants pendant que les paquets sortants sont traités (/transmis) par le routeur. La non-fiabilité est introduite dans les protocoles de la couche réseau si les files d'attente sont pleines, ce qui peut se remplir à mesure que le trafic augmente.

Le protocole réseau Internet s'appelle Internet Protocol (IP). Les principaux composants de la couche réseau Internet sont,

1. [IP](https://en.wikipedia.org/wiki/Internet_Protocol) : définit les conventions d'adressage (IPv4, IPv6), le format des paquets, la convention de traitement des paquets
2. [Protocoles de routage](https://en.wikipedia.org/wiki/Routing_protocol) : déterminent le chemin qu'un paquet emprunte de la source à l'hôte
3. [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) : facilité pour signaler les erreurs dans les paquets et répondre aux demandes de certaines informations de la couche réseau

En résumé, la couche réseau fournit une communication logique entre deux hôtes finaux. Les protocoles de la couche réseau s'exécutent sur les hôtes finaux et les dispositifs du noyau du réseau tels que les routeurs. Les routeurs transmettent les paquets réseau, ce qui aide à former la communication logique entre deux hôtes finaux.

Continuons avec notre exemple de communication avec ilovecookies.com. 

Nous avons vu que mon navigateur web crée un message de requête HTTP (protocole de la couche application) et le transmet à la couche transport, qui utilise le protocole TCP pour la communication de bout en bout entre mon application de navigateur web et une application serveur (ilovecookies.com).

![Image](https://www.freecodecamp.org/news/content/images/2022/01/12.png)
_Un paquet IP encapsulant un paquet TCP_

Nous pouvons voir que le paquet réseau encapsule le paquet TCP, qui encapsule le paquet d'application. Le texte en surbrillance vert représente le contenu du paquet réseau, le jaune le paquet de transport, et le texte restant commençant par GET est le paquet d'application. 

Les champs du paquet réseau sont pertinents pour son fonctionnement. Par exemple, l'adresse source est l'adresse IP de ma machine, et l'adresse de destination est l'adresse du serveur [ilovecookies.com](https://mxtoolbox.com/SuperTool.aspx?action=a%3ailovecookies.com&run=toolpage).

L'encapsulation et les informations spécifiques à la couche contenues dans les paquets sont également liées à l'idée de communication logique entre les hôtes et les applications s'exécutant sur eux. 

Par exemple, le paquet réseau inclut les adresses IP des machines finales, tandis que le paquet de transport ne contient que les numéros de port. La couche transport s'appuie sur la couche réseau pour déplacer les données entre les machines finales. Une fois les données arrivées sur le dispositif de réception, la couche transport prend le relais et route le paquet vers l'application correcte en utilisant les numéros de port contenus dans le paquet de transport.

## La couche Liaison

Comparée aux couches que nous avons vues jusqu'à présent, la couche liaison a un champ d'application plus restreint : elle fournit des services pour déplacer les paquets sur les liens individuels du chemin de bout en bout.

Par exemple, les liens sont les lignes pointillées rouges (voir les illustrations ci-dessus). La couche liaison permet le mouvement de nœud à nœud des paquets de la couche réseau sur un seul lien du chemin.

Un protocole de couche liaison définit :

* le format des paquets échangés entre les nœuds aux extrémités du lien
* les actions entreprises sur les paquets par ces nœuds

Un [adaptateur réseau](https://en.wikipedia.org/wiki/Adapter_(computing)#Network_adapter) implémente les protocoles de la couche liaison. L'adaptateur réseau constitue le matériel physique qui permet à un ordinateur de se connecter à un réseau et d'échanger des informations. 

Essayez d'exécuter cette commande pour voir la liste des adaptateurs réseau dans votre ordinateur :

`Mac : networksetup -listallhardwareports`
`Linux : lshw -class network -short`
`Windows : Get-NetAdapter -Name *`

Dans la sortie, vous remarquerez que chaque dispositif a une adresse de couche liaison connue sous le nom d'adresse MAC. La [ROM](https://en.wikipedia.org/wiki/Read-only_memory) des adaptateurs contient des adresses MAC assignées au moment de la fabrication qui sont considérées comme permanentes. Chaque nœud (hôtes et routeurs) a une adresse de couche liaison le long du chemin.

Plus tôt, nous avons parlé de l'adresse IP, qui est également un identifiant pour les dispositifs. La situation est similaire à avoir plusieurs identifiants : adresse domicile et numéro de sécurité sociale. Il existe plusieurs raisons pour lesquelles les nœuds ont des adresses MAC et des adresses de couche réseau.

* Les protocoles des différentes couches sont censés être substituables. Par exemple, [IPX](https://en.wikipedia.org/wiki/IPX/SPX) n'utilise pas d'adresse de couche réseau.
* Les adresses IP sont stockées en RAM et [reconfigurées chaque fois que l'adaptateur est déplacé ou mis sous tension](https://en.wikipedia.org/wiki/IPX/SPX), c'est-à-dire temporaires.
* Supposons que le protocole omette les adresses MAC. L'adaptateur devrait transmettre chaque paquet qu'il reçoit à la pile de protocoles. La couche réseau vérifierait la correspondance de l'adresse IP. Mais cela peut être inefficace si cela est fait trop de fois : les [interruptions](https://en.wikipedia.org/wiki/Interrupt) aident à transmettre les paquets, ce qui peut être [coûteux](https://en.wikipedia.org/wiki/Interrupt#Performance).

En résumé, pour que les couches soient largement des blocs de construction indépendants dans l'architecture réseau, de nombreuses couches doivent avoir leur propre schéma d'adressage. 

Pour un bref récapitulatif, nous avons rencontré trois types d'adresses jusqu'à présent :

* Noms d'hôte pour la couche application (ilovecookies.com). Ceux-ci sont convertis en adresses IP correspondantes en utilisant le [DNS](https://en.wikipedia.org/wiki/Domain_Name_System).
* L'adresse IP pour la couche réseau
* Adresse MAC pour la couche liaison

Comme le Domain Name System, qui aide à résoudre les adresses IP à partir des noms d'hôte, le protocole de résolution d'adresse ([ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)) est utile pour déterminer les adresses MAC (de destination) à partir d'une adresse IP. 

ARP construit une table en RAM qui contient une correspondance entre l'adresse IP et l'adresse MAC. Le protocole inclut des spécifications (telles que [un paquet particulier](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#Packet_structure)) pour créer cette table automatiquement.

La couche réseau transmet le paquet et l'adresse MAC (de la table ARP) du nœud de destination à la couche liaison. La couche liaison encapsule le paquet dans un paquet de couche liaison et le déplace le long du lien vers le nœud de destination. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/13-1.png)
_Un réseau contenant deux hôtes et un routeur_

Supposons que dans la configuration ci-dessus, l'hôte 222.222.222.220 souhaite envoyer un paquet à l'autre hôte 222.222.222.222. La couche réseau utilise ARP pour résoudre l'adresse MAC correspondante en 49-BD-D2-C7-56-A2 et transmet le paquet et l'adresse MAC à la couche liaison. La couche liaison déplace le paquet sur le lien entre les deux hôtes.

Ensuite, considérons un scénario plus complexe où un hôte souhaite envoyer un paquet à un autre hôte sur un réseau différent. Par exemple, un paquet de mon ordinateur à ilovecookies.com voyage de mon [réseau domestique](https://en.wikipedia.org/wiki/Home_network#Infrastructure_devices) à un autre réseau.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/14-1.png)
_Un routeur connectant deux sous-réseaux. Le routeur contient deux adaptateurs pour la liaison et deux adresses IP, l'identifiant sur chaque sous-réseau_

Il y a deux choses à noter sur cette image. Premièrement, le routeur a deux adresses IP. Comme le routeur participe à deux réseaux différents, il nécessite deux adresses IP pour l'identifier dans le réseau respectif. Pour plus de détails, voir [ceci](https://askleo.com/your-routers-two-ip-addresses/).

Deuxièmement, les deux réseaux séparés sont connus sous le nom de [sous-réseaux](https://en.wikipedia.org/wiki/Subnetwork). Un sous-réseau est un regroupement logique de dispositifs réseau qui rend la gestion des dispositifs réseau plus accessible.

Supposons que dans cette configuration, l'hôte 222.222.222.222 souhaite envoyer un paquet à l'hôte 111.111.111.111, ce qui implique un voyage inter-réseau. Il ne localisera pas l'hôte de destination (111.111.111.111) dans son sous-réseau, et il transmet le paquet à la passerelle par défaut (routeur). 

La couche réseau utilise la table ARP pour résoudre l'adresse MAC en 88-B2-2F-54-1A-0F. Le routeur utilise sa table de routage pour livrer le paquet au lien connectant à l'autre sous-réseau. Une fois de plus, la table ARP aide à résoudre l'adresse MAC de l'hôte de destination, et le paquet se déplace le long du lien.

En résumé, la partie adaptateur de votre matériel informatique implémente les protocoles de la couche liaison. Le protocole de la couche liaison définit un schéma d'adressage appelé adresses MAC, et l'ARP est utilisé pour mapper les adresses IP aux adresses MAC. La couche liaison encapsule les paquets de la couche réseau et les déplace sur un lien.

L'un des protocoles populaires de la couche liaison est [Ethernet](https://en.wikipedia.org/wiki/Ethernet). Continuons notre exemple (ilovecookies.com) pour examiner le protocole Ethernet en action.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/15-1.png)
_Un paquet Ethernet encapsulant un paquet IP_

Nous pouvons observer que le paquet Ethernet contient les adresses MAC de destination et de source (omises), et il encapsule le paquet IP.

## Récapitulatif

Récapitulons ce que nous avons vu dans cet article en utilisant l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/16.png)
_Communication réseau de bout en bout entre l'hôte A et l'hôte B_

Les applications informatiques s'exécutant sur deux systèmes différents (appelés hôtes) communiquent en utilisant des protocoles. 

Les protocoles sont des règles qui régissent la communication entre deux hôtes. La pile de protocoles résout plusieurs sous-problèmes pour résoudre le problème de la communication réseau. Chaque couche se concentre sur la résolution d'un sous-problème en utilisant les services offerts par les couches inférieures dans la hiérarchie d'abstraction.

Les protocoles de la couche application fonctionnent au niveau d'abstraction le plus élevé. Une application communique en envoyant des messages qui adhèrent aux règles d'un protocole d'application (par exemple HTTP). 

Le DNS est utilisé pour mapper le nom d'hôte (www.ilovecookies.com) à une adresse IP. Ces messages sont poussés à travers l'interface de socket pour être transmis sur le réseau en utilisant la couche transport.

La couche transport expose une communication logique entre deux applications s'exécutant sur différents hôtes. Elle divise les messages d'application en morceaux plus petits et les encapsule dans des paquets contenant des informations supplémentaires ([en-têtes](https://en.wikipedia.org/wiki/Header_(computing))).

Le message de l'application est créé à partir de ces paquets et poussé à travers l'interface de socket en utilisant le numéro de port sur le paquet. Ces paquets sont envoyés sur le réseau en s'appuyant sur la couche réseau.

Ensuite, la couche réseau prend le relais, fournissant une communication logique entre deux hôtes. Elle encapsule également le paquet de transport dans un paquet réseau. 

L'Internet contient des dispositifs de commutation de paquets qui transmettent des paquets réseau, en utilisant des tables de routage stockées en RAM et construites dynamiquement en utilisant des protocoles de routage. La couche réseau s'appuie sur la couche liaison pour déplacer les paquets.

La couche liaison est responsable du déplacement des paquets sur les liens individuels. Les dispositifs matériels, appelés adaptateurs, implémentent les protocoles de la couche liaison et ont une adresse permanente associée à eux, appelée adresse MAC. L'adresse MAC sert d'identifiant pour cette couche. Le protocole de résolution d'adresse (ARP) mappe les adresses IP aux adresses MAC.

Enfin, la couche liaison transmet les paquets à la couche physique, qui constitue les fils sur lesquels les informations voyagent.

Merci d'avoir lu ! J'espère que vous avez appris quelque chose de nouveau sur les réseaux informatiques aujourd'hui.

### Sources

%[https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-7th-Edition/PGM1101673.html]

%[https://www.wireshark.org/]