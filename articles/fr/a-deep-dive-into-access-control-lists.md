---
title: Qu'est-ce qu'une ACL ? Explication des listes de contrôle d'accès
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2023-04-14T14:43:14.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-access-control-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/towfiqu-barbhuiya-FnA5pAzqhMM-unsplash.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: computer networking
  slug: computer-networking
- name: Security
  slug: security
seo_title: Qu'est-ce qu'une ACL ? Explication des listes de contrôle d'accès
seo_desc: 'In computing, access control is the concept of limiting or regulating a
  person or machine''s access to certain information or resources.

  One of the major mechanisms you use to do that is an access control list (ACL).
  An ACL is a set of rules for allow...'
---

En informatique, le contrôle d'accès est le concept de limitation ou de régulation de l'accès d'une personne ou d'une machine à certaines informations ou ressources.

L'un des principaux mécanismes que vous utilisez pour cela est une liste de contrôle d'accès (ACL). Une ACL est un ensemble de règles pour autoriser ou refuser l'accès à certaines ressources. Les ressources dans ce cas peuvent être des fichiers, des réseaux ou des appareils.

Dans cet article, nous parlerons de ce que sont vraiment les listes de contrôle d'accès et de la manière dont vous pouvez les utiliser. Nous allons aborder :

* Les ACL de système de fichiers et les ACL de réseau

* Les pare-feu et le filtrage de paquets avec état

* Les ACL dans le réseau cloud (Azure NSG, AWS SG, AWS NACL)

* Les ACL dans le DNS (BIND9)

* Les ACL dans le réseau central (types d'ACL Cisco, types d'ACL Huawei)

## Prérequis

Pour comprendre cet article, vous avez besoin d'une compréhension de base des réseaux, des pare-feu et de l'informatique en nuage. Vous pourriez particulièrement avoir besoin de comprendre les bases des concepts d'[adressage IP](https://www.linkedin.com/pulse/ip-addressing-chidiadi-anyanwu) et de [DNS](https://www.linkedin.com/pulse/dns-deep-dive-chidiadi-anyanwu/).

## Types de listes de contrôle d'accès

Lorsque nous parlons d'ACL, beaucoup de gens pensent uniquement aux réseaux. Mais en fait, il existe deux types d'ACL :

* Les ACL de système de fichiers

* Les ACL de réseau

Les ACL de système de fichiers aident les systèmes d'exploitation à connaître les privilèges d'accès de l'utilisateur pour différents fichiers ou répertoires du système. Les ACL NFSv4 et POSIX sont des exemples de types d'ACL de système de fichiers.

Les ACL de réseau sont appliquées sur les interfaces et vous les utilisez pour autoriser ou refuser le trafic provenant de certaines sources ou à destination de certaines destinations. C'est ce sur quoi je vais me concentrer dans cet article.

## Structure d'une règle ACL

Une ACL est comme un groupe de règles identifié par un nom ou un numéro. Une règle ACL a généralement un numéro de priorité, les critères (adresse source, adresse de destination, etc.) et l'instruction d'autorisation/refus.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Cisco-ACL-structure.png align="left")

*Structure ACL Cisco*

## Pare-feu et ACL

Un pare-feu est un dispositif ou un logiciel de sécurité qui surveille le trafic entrant et sortant d'un dispositif ou d'un réseau, et filtre le trafic indésirable ou malveillant.

Jusqu'à l'inspection de paquets avec état, les ACL étaient le principal mécanisme par lequel les pare-feu fonctionnaient. Avec les ACL, les paquets sont autorisés ou refusés en fonction des propriétés spécifiées dans les règles.

Les ACL sont sans état. Vous devez créer une règle entrante et une règle sortante correspondante, sinon les paquets d'un côté pourraient être bloqués.

Avec l'inspection de paquets avec état (également connue sous le nom de filtrage dynamique de paquets), vous pouvez alors créer des politiques de sécurité pour un type de trafic. Le pare-feu établirait une session chaque fois qu'un paquet est autorisé, de sorte que toute réponse à ce paquet est autorisée même s'il n'y avait pas de politique spécifique pour l'autoriser.

Cela rend les choses plus faciles et plus efficaces que l'utilisation d'ACL qui sont unidirectionnelles. Mais cela signifie également que plus de ressources informatiques sont utilisées par le pare-feu et que le réseau est ralenti.

Aujourd'hui, les pare-feu sont beaucoup plus complexes avec l'inspection approfondie des paquets (DPI), les capacités de système de détection d'intrusion (IDS)/système de prévention d'intrusion (IPS), et même les capacités antivirus, mais cela dépasse le cadre de cet article.

Explorons quelques situations de réseau où les ACL sont utilisées.

## ACL dans le réseau cloud

Les principaux fournisseurs de services cloud (CSP) fournissent des formes d'ACL ou des capacités de pare-feu pour que leurs clients les utilisent dans leur infrastructure cloud.

Par exemple, dans Microsoft Azure, nous avons ce que l'on appelle les groupes de sécurité réseau (NSG) et dans AWS, nous avons les groupes de sécurité (SG) et la liste de contrôle d'accès réseau (NACL). Ce sont toutes des implémentations de la sécurité de type ACL.

### AWS

Un groupe de sécurité AWS détermine quel trafic est autorisé vers et depuis les ressources attachées à ce groupe de sécurité. Il se compose d'une liste de règles entrantes et sortantes, et est avec état.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--320--1.png align="left")

*Groupe de sécurité AWS par défaut*

Une liste de contrôle d'accès réseau AWS est une autre liste de règles mais au niveau du sous-réseau. Les règles se composent du numéro de règle, du type, du protocole, de la plage de ports, de la source, de la destination et des champs d'autorisation/refus. Une NACL peut être appliquée à plus d'un sous-réseau, mais un sous-réseau ne peut pas être attaché à plus d'une NACL.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--319--nacl-3-1.png align="left")

*Règles entrantes pour AWS NACL*

### Azure

Un groupe de sécurité réseau Azure est une fonctionnalité de pare-feu qui fonctionne à la fois au niveau du sous-réseau et de la carte d'interface réseau (NIC) des ressources dans votre VNet. Il s'agit essentiellement également d'une liste de règles ACL composée du numéro de priorité, du nom, du port, du protocole, de la source et de la destination.

Ici, vous pouvez utiliser des adresses IP, des balises de service ou des groupes de sécurité d'application (ASG) dans les champs source et destination. Les NSG sont avec état.

Les règles des groupes de sécurité réseau Azure et des NACL AWS sont très similaires aux règles ACL utilisées dans le réseau central. De plus, vous ne pouvez pas vraiment désigner les groupes de sécurité AWS et les NSG Azure comme des ACL car ils ne sont pas sans état.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Microsoft-NSG-rules-image.png align="left")

*NSG Azure*

## ACL dans le DNS

[Les serveurs DNS aident à résoudre les noms de domaine en adresses IP](https://www.linkedin.com/pulse/dns-deep-dive-chidiadi-anyanwu/). S'ils acceptent et répondent aux requêtes de chaque appareil autour d'eux, cela affectera leurs performances et les rendra vulnérables aux attaques DDoS. Par conséquent, les administrateurs DNS utilisent des ACL pour déterminer qui peut envoyer des requêtes DNS aux serveurs.

Par exemple, dans un serveur BIND9, une telle ACL serait définie dans le fichier named.conf, et ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--308--1.png align="left")

*Une ACL dans BIND9*

## ACL dans le réseau central

Cela est un peu plus complexe que les autres contextes que nous avons discutés ci-dessus. Les ACL sur les appareils réseau sont configurées sur les interfaces et sont utilisées dans de nombreux scénarios différents. Il existe également différents types d'ACL. Par appareils réseau, j'entends des appareils comme les routeurs, les commutateurs, les pare-feu, les contrôleurs d'accès, etc.

Généralement, ces ACL sont identifiées par leurs noms ou leurs numéros ACL, et leurs règles suivent le format :

*autoriser/refuser les critères*

Pour les appareils Cisco, il existe deux principaux types d'ACL IPv4 :

* Les listes d'accès standard

* Les listes d'accès étendues

### ACL standard

Ces ACL autorisent ou refusent le trafic en fonction uniquement de l'adresse IP source.

```python
R1(config)#access-list 10 permit 192.168.17.0 0.0.0.255
```

La règle ci-dessus indique au routeur d'autoriser les paquets provenant du sous-réseau *192.168.17.0/24*. Notez que *0.0.0.255* n'est pas un masque de sous-réseau. Il s'agit d'un caractère générique qui indique à l'appareil dans quelle mesure il doit correspondre à l'adresse que vous avez entrée. *255* signifie que n'importe quel nombre est acceptable tandis que *0* signifie qu'il doit correspondre exactement.

Ici, la partie réseau *192.168.17* doit être exactement la même dans n'importe quel paquet, tandis que le dernier octet (la partie hôte) peut être n'importe quoi. Vous pouvez en apprendre davantage sur l'adressage IP [ici](https://www.linkedin.com/pulse/ip-addressing-chidiadi-anyanwu).

### ACL étendues

Ces ACL autorisent ou refusent le trafic en fonction de ce que l'on appelle en réseau le 5-tuple (adresse source, adresse de destination, port source, port de destination, protocole de couche transport).

```python
R2(config)#access-list 100 permit tcp 10.1.1.0 0.0.0.255 host 10.2.2.2 eq 80
```

La commande ci-dessus indique au routeur d'autoriser tout paquet utilisant le protocole de couche transport TCP, provenant du réseau 10.1.1.0/24 vers le port 80 ([HTTP](https://www.linkedin.com/pulse/http-network-protocol-chidiadi-anyanwu/)) de l'hôte, 10.2.2.2.

Le terme 5-tuple en réseau provient probablement des mathématiques. Un tuple signifie un enregistrement/une ligne. 5-tuple signifie une ligne avec cinq colonnes – une liste ordonnée de 5 éléments.

Les cinq éléments qui nous intéressent principalement en réseau lors de la gestion des paquets sont les adresses IP (source et destination), les numéros de port (source et destination) et le protocole de couche transport. Ils sont donc généralement appelés 5-tuple.

Les numéros d'ACL 1 - 99 et 1300 - 1999 désignent les ACL standard tandis que les numéros 100 - 199 et 2000 - 2699 désignent les ACL étendues.

De nombreux autres fournisseurs suivent ce modèle, mais Huawei ne le fait pas.

Pour les appareils Huawei, il existe 5 types d'ACL IPv4 :

* ACL de base (numéros d'ACL 2000 - 2999)

* ACL avancées (numéros d'ACL 3000 - 3999)

* ACL de couche 2 (numéros d'ACL 4000 - 4999)

* ACL définies par l'utilisateur (numéros d'ACL 5000 - 5999)

* ACL utilisateur (numéros d'ACL 6000 - 6999)

**ACL de base :** Autorise ou refuse le trafic en fonction de l'adresse source. La plage de numéros d'ACL est de 2000 - 2999.

**ACL avancée :** Autorise ou refuse le trafic en fonction du 5-tuple (adresse IP source, adresse IP de destination, port source, port de destination et type de protocole).

**ACL de couche 2 :** Autorise ou refuse le trafic en fonction des informations dans l'en-tête de trame (adresse MAC source, adresse MAC de destination, type de protocole de couche 2).

**ACL définie par l'utilisateur :** Autorise ou refuse le trafic en fonction des en-têtes de paquet, des décalages, des masques de chaîne de caractères et des chaînes de caractères définies par l'utilisateur.

**ACL utilisateur :** Autorise ou refuse le trafic en fonction des adresses IP source et de destination ou des groupes de liste de contrôle utilisateur (UCL), des ports source et de destination, et des types de protocole IPv4.

```python
acl 3500                                                
 rule 0 deny tcp source 10.1.1.0 0.0.0.255 destination 192.168.0.9 0 destination-port eq 80                                                                
 rule 5 allow tcp source 10.1.1.0 0.0.0.255 destination 192.168.0.9 0 destination-port eq telnet
```

### Refus implicite

Il est également important de noter que même si vous n'ajoutez aucune règle à la fin de votre ACL, la dernière règle est toujours une règle de refus. Elle n'est pas affichée, donc elle est implicite. Mais elle est là. Elle refuse tout paquet qui ne correspond à aucune règle dans votre ACL.

### Quelques points à connaître

Les règles ACL sont exécutées séquentiellement, donc si vous avez la règle 3 et la règle 5, la règle 3 est exécutée en premier.

Il est toujours bon de créer des règles à intervalles (règle 10, règle 20, règle 30) plutôt que simplement en série (règle 1, règle 2, règle 3). La raison est que vous pourriez vouloir ajouter une règle entre deux règles existantes, et vous voulez que le système l'exécute dans cet ordre particulier. Cela évite du stress s'il y avait de l'espace pour cela dès le début.

## Conclusion

Le contrôle d'accès est crucial pour la sécurité. Numériquement, les ACL ont été le mécanisme de choix pour un contrôle d'accès rapide et facile. Bien que d'autres méthodes comme le contrôle d'accès basé sur les rôles (RBAC) et le contrôle d'accès basé sur les attributs (ABAC) aient émergé, l'ACL a toujours sa place dans le contrôle d'accès.

Merci d'avoir lu. Si vous avez apprécié cet article, veuillez le partager pour que d'autres puissent le voir aussi.

Vous pouvez également [me connecter sur LinkedIn](https://linkedin.com/in/chidiadi-anyanwu).