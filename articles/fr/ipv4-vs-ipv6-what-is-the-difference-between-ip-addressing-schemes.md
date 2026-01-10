---
title: IPV4 vs IPV6 – Quelles sont les différences entre les schémas d'adressage IP
  ?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-15T16:30:13.000Z'
originalURL: https://freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/nasa-1lfI7wkGWZ4-unsplash.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: internet
  slug: internet
- name: ipv6
  slug: ipv6
seo_title: IPV4 vs IPV6 – Quelles sont les différences entre les schémas d'adressage
  IP ?
seo_desc: 'The Internet is one of our greatest inventions.

  Millions of people use the Internet every second of the day, and it has changed
  many aspects of our lives – from creating new jobs and a new way of working to influencing
  how news is consumed and how de...'
---

L'Internet est l'une de nos plus grandes inventions.

Des millions de personnes utilisent l'Internet chaque seconde de la journée, et il a changé de nombreux aspects de nos vies – de la création de nouveaux emplois et d'une nouvelle façon de travailler à l'influence de la manière dont les nouvelles sont consommées et dont les décisions sont prises.

Bien qu'il existe depuis un certain temps, les technologies sous-jacentes qui le alimentent n'ont pas beaucoup changé depuis son invention.

Dans cet article, vous en apprendrez davantage sur le protocole Internet, ou IP - ce que c'est, comment il fonctionne, et les différences entre ses différentes versions.

## Comment les ordinateurs communiquent sur l'Internet

Les ordinateurs, et les appareils en général, se connectent et communiquent entre eux sur l'Internet de plusieurs manières : soit avec l'aide d'un grand nombre de câbles sous-marins, soit sans fil.

Les informations sont décomposées en paquets, ou en plus petits morceaux de données, qui sont transférés par des routeurs vers la destination correcte et retour.

Cependant, pour que les ordinateurs puissent communiquer en premier lieu, il doit y avoir un ensemble de règles et une langue commune de communication universellement acceptée que tous les appareils comprennent.

Ce besoin d'une méthode standardisée de communication lors de l'échange de données a conduit à la création de protocoles.

L'un des protocoles clés est le *Protocole Internet*, ou IP.

Le Protocole Internet a une syntaxe particulière qui définit un ensemble de règles et un format spécifié pour la manière dont la communication aura lieu entre les appareils sur divers réseaux. Il rend essentiellement la communication entre les ordinateurs possible.

Ces règles couvrent un grand nombre de choses, comme :
* identifier et localiser chaque appareil sur un réseau
* faire en sorte que les appareils communiquent ensuite entre eux
* dicter à quoi ressemblera le format et le transfert des paquets de données
* déterminer comment chaque paquet atteindra la destination souhaitée
* choisir le chemin le plus rapide et le plus efficace possible pour le routeur, et
* décider comment gérer les erreurs lorsqu'elles se produisent.

Chaque appareil connecté à un réseau a besoin d'un moyen de s'identifier sur divers réseaux.

Lorsque vous souhaitez envoyer une lettre à quelqu'un, vous avez besoin d'un moyen d'identifier le domicile de cette personne afin que le service postal sache où livrer la lettre. Vous ne voulez pas que la lettre soit livrée à la mauvaise personne !

C'est pourquoi, lors de l'envoi d'une lettre, vous incluez l'adresse unique du domicile du destinataire comme adresse de destination et également votre adresse unique de domicile, qui est l'adresse de retour.

Chaque maison a une adresse unique qui la distingue et l'identifie.

De même, la manière d'identifier les ordinateurs et les appareils sur l'Internet afin que nous puissions transmettre et échanger des données, est de connaître leur adresse IP.

Pour envoyer un e-mail à quelqu'un, vous devez connaître l'adresse IP de son ordinateur. L'e-mail est décomposé en plus petits morceaux, ou paquets. La manière dont ils atteignent la destination correcte est parce que chaque paquet inclut également des informations IP.

Lors de l'envoi de quelque chose sur l'Internet, il doit y avoir une adresse de destination et une adresse de retour sur chaque paquet. Les adresses IP sont la manière dont les ordinateurs se trouvent et connaissent leurs emplacements respectifs.

Le Protocole Internet est responsable de la définition du format de l'adressage IP.

## Qu'est-ce qu'une adresse IP ?

Une adresse IP est une adresse réseau, et chaque appareil qui se connecte à un réseau informatique en reçoit une.

Une adresse IP est une séquence unique de chiffres attribuée à un appareil, écrite dans un certain format. Elle identifie globalement chaque appareil dans le réseau interconnecté.

Comme mentionné précédemment, les paquets sont acheminés vers la destination correcte et prévue, et les appareils peuvent envoyer et recevoir des informations sur l'Internet parce que chaque appareil se voit attribuer une adresse IP unique.

Il est peu probable que vous ayez jamais à traiter directement avec des adresses IP ou à en connaître par cœur pour envoyer des informations sur l'Internet - tout cela se passe en arrière-plan.

Si vous êtes curieux et souhaitez connaître votre adresse IP, rendez-vous sur Google.com et tapez "Quelle est mon IP" et vous verrez votre adresse unique dans le premier résultat.

Cela dit, il existe quelques types différents d'adresses IP, que vous verrez dans les sections suivantes.

### Adresses IP privées vs publiques

Chacun possède deux types d'adresses IP : publiques et privées.

L'adresse publique est attribuée à votre routeur domestique par votre Fournisseur d'Accès à Internet (FAI) et c'est l'adresse principale pour tout votre réseau local.

Chez vous, vous pouvez avoir plus d'un ordinateur portable, smartphone ou tablette. Chaque appareil a sa propre adresse IP, mais ils sont tous également sous la même adresse IP principale et publique.

C'est ainsi que tous les appareils de votre domicile se connectent à l'Internet – via l'adresse IP publique principale.

Une adresse IP publique est unique, ce qui signifie qu'il n'y a pas deux adresses IP identiques utilisées à un moment donné.

Comme mentionné ci-dessus, si vous avez de nombreux appareils chez vous, chacun a sa propre adresse IP. Cette adresse est une adresse IP privée, et elle ne peut pas accéder directement à l'Internet.

Comme ces appareils se connectent à l'Internet via le routeur (qui a une adresse IP publique), le routeur a besoin d'un moyen d'identifier et de reconnaître chaque appareil séparément, avant de le connecter à l'Internet.

La manière dont le routeur fait cela est en attribuant une adresse IP privée individuelle à chaque appareil. Ensuite, il se souvient de cette adresse chaque fois que l'appareil souhaite se connecter à l'Internet.

### Adresses IP dynamiques vs statiques

Les adresses IP publiques sont divisées en deux catégories : dynamiques et statiques.

Une fois qu'un appareil est connecté à l'Internet, votre Fournisseur d'Accès à Internet vous donne l'une de leurs adresses IP disponibles pour la durée de votre connexion. C'est ainsi que l'appareil pourra envoyer et recevoir des données.

La prochaine fois que vous vous connecterez à l'Internet, votre FAI vous fournira une adresse IP *différente*. Cela signifie que chaque fois que vous vous connectez à l'Internet, vous avez une adresse IP différente. C'est pourquoi ce type d'adresse IP est appelé dynamique - elle change constamment.

En revanche, une adresse IP statique ne change jamais. C'est une adresse permanente. L'adresse est fournie une fois et vous pouvez vous attendre à ce qu'elle reste la même.

Les adresses IP statiques sont souvent utilisées par les serveurs DNS. Un serveur DNS est un grand ordinateur qui stocke les fichiers qui composent un site web. Leur travail est d'envoyer ces fichiers chaque fois qu'ils sont demandés par un utilisateur qui souhaite consulter le site web.

## IPv4 vs IPv6 – Quelles sont les différences ?
### Qu'est-ce qu'une adresse IPv4 ?

IPv4 est la première version, et la plus largement utilisée, du Protocole Internet.

Elle a été lancée pour la première fois en 1980 et est utilisée encore aujourd'hui.

C'est une adresse 32 bits composée de 4 blocs – chaque bloc étant séparé par un point.

Elle ressemble à quelque chose comme ceci :

```
XXX.XXX.XXX.XXX
```

Chaque bloc peut contenir jusqu'à 3 chiffres, et les nombres dans le bloc vont de 0 à 255, en valeurs *décimales*.

Un exemple d'adresse IP est :

```
142.250.185.206
```

Voici un autre exemple :

```
69.171.250.35
```

Ces nombres décimaux sont convertis en binaire, un langage machine, qui est le seul langage que les ordinateurs peuvent comprendre directement.

Ces nombres décimaux, en binaire, sont en fait 4 blocs de 8 chiffres binaires (ou bits).

C'est pourquoi il est appelé une adresse 32 bits – c'est une adresse composée d'une séquence de 32 chiffres binaires.

Par exemple, l'adresse que vous avez vue précédemment, `142.250.185.206` est :

```
10001110.11111010.10111001.11001110
```

en binaire, sous le capot.

Ainsi, `2^32` représente un total de 4 294 967 296 adresses uniques. C'est la limite des adresses IP qu'IPv4 peut fournir pour que chaque appareil se connecte à l'Internet.

Vous pourriez penser que ce grand nombre est plus que suffisant. Mais, à mesure que la population continue de croître et que chaque personne possède de plus en plus d'appareils (et que chaque appareil a besoin de sa propre adresse IP), nous manquons d'adresses depuis un certain temps.

### Qu'est-ce qu'IPv6 ?

IPv6 est la dernière version du Protocole Internet, déployée pour la première fois en 1998.

C'est le successeur d'IPv4 et il y aura un changement progressif vers celui-ci à l'avenir.

Alors qu'IPv4 est une adresse numérique, IPv6 utilise des caractères hexadécimaux alphanumériques – ce qui signifie qu'il contient des nombres *et* des lettres.

De la même manière qu'IPv4 utilise 4 blocs contenant chacun jusqu'à 3 chiffres, IPv6 utilise 8 blocs contenant chacun 4 caractères hexadécimaux.

Dans IPv4, chaque bloc est séparé par un point (`.`). Dans IPv6, chaque bloc est séparé par un deux-points (`:`).

Ainsi, une adresse IPv6 ressemble à quelque chose comme ceci :

```
XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
```

Par exemple :

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

C'est une adresse 128 bits, ce qui signifie qu'il y a `2^128` adresses disponibles.

Cela signifie qu'il y a 340 282 366 920 938 463 463 374 607 431 768 211 456 adresses que nous pouvons utiliser sur l'Internet.

Cela représente 340 *undécillions* d'adresses, ce qui, nous l'espérons, sera plus que suffisant pour tout le monde !

## Conclusion

Et voilà ! Vous connaissez maintenant les bases du Protocole Internet. C'est la technologie sous-jacente que tous les ordinateurs et appareils utilisent pour pouvoir se connecter les uns aux autres et recevoir et échanger des informations.

Vous avez également appris les différences de base entre IPv4 et IPv6. En résumé, IPv6 fournit beaucoup plus d'adresses IP qu'IPv4.

Si vous êtes intéressé à en apprendre davantage sur le fonctionnement de l'Internet, consultez cette [vidéo sur la chaîne YouTube de freeCodeCamp](https://www.youtube.com/watch?v=zN8YNNHcaZc&t=1s) qui explique les fondamentaux de la mise en réseau informatique.

Merci d'avoir lu et bon apprentissage 😊