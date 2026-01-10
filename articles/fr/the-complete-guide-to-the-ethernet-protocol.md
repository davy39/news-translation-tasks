---
title: Comment fonctionne le protocole Ethernet – Un guide complet
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-10-21T17:12:40.000Z'
originalURL: https://freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/The-Ethernet-Protocol-Book-Cover--1-.png
tags:
- name: computer networking
  slug: computer-networking
- name: handbook
  slug: handbook
- name: internet
  slug: internet
- name: networking
  slug: networking
seo_title: Comment fonctionne le protocole Ethernet – Un guide complet
seo_desc: 'Whether you’ve been aware of it or not, you’ve probably used the Ethernet
  in the past. Does this cable look familiar?


  _(Source: Wikipedia)_

  Ethernet is extremely popular, and is the most widely used Data Link Layer protocol,
  at least where the devic...'
---

Que vous en ayez été conscient ou non, vous avez probablement utilisé l'Ethernet par le passé. Ce câble vous semble-t-il familier ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-94.png)
_(Source : [Wikipedia](https://en.wikipedia.org/wiki/Ethernet_physical_layer#/media/File:EthernetCableYellow3.jpg))_

Ethernet est extrêmement populaire et est le protocole de la couche de liaison de données le plus largement utilisé, du moins lorsque les appareils sont reliés par des câbles physiques (plutôt que sans fil).

Si vous avez besoin d'un rappel sur la couche de liaison de données et son rôle dans le modèle des couches, consultez [mon précédent article](https://www.freecodecamp.org/news/the-five-layers-model-explained/).

Dans ce tutoriel, vous apprendrez tout sur Ethernet – son histoire, ainsi que chaque bit et octet de la trame Ethernet. Vous découvrirez également comment les protocoles sont formés, pourquoi il est si difficile de les modifier après leur publication, et quelles leçons peuvent être tirées pour d'autres protocoles.

## Voici ce que nous allons couvrir :

1. [Un peu d'histoire de l'Ethernet](#heading-un-peu-dhistoire-de-lethernet)
2. [Aperçu de la trame Ethernet](#heading-aperçu-de-la-trame-ethernet)
   - [Avant la trame – préambule (8 octets)](#heading-avant-la-trame-préambule-8-octets)
   - [Adresse de destination et adresse source (6 octets chacune)](#heading-adresse-de-destination-et-adresse-source-6-octets-chacune)
   - [Champ Type / Longueur – Ethernet II (Type) (2 octets)](#heading-champ-type-longueur-ethernet-ii-type-2-octets)
   - [Données et bourrage (46-1500 octets)](#heading-données-et-bourrage-46-1500-octets)
   - [Somme de contrôle – CRC32 (4 octets)](#heading-somme-de-contrôle-crc32-4-octets)
   - [Le problème avec le champ Type / Longueur](#heading-le-problème-avec-le-champ-type-longueur)
3. [Comment fonctionnent les adresses Ethernet](#heading-comment-fonctionnent-les-adresses-ethernet)
   - [Bits Unicast et Multicast](#heading-bits-unicast-et-multicast)
   - [Bit globalement unique / localement administré](#heading-bit-globalement-unique-localement-administré)
4. [Pourquoi une trame Ethernet a-t-elle une longueur minimale ?](#heading-pourquoi-une-trame-ethernet-a-t-elle-une-longueur-minimale)
   - [Comment les collisions sont-elles gérées dans Ethernet ?](#heading-comment-les-collisions-sont-elles-gérées-dans-ethernet)
5. [Conclusion](#heading-conclusion)

# Un peu d'histoire de l'Ethernet

La première version d'Ethernet a été mise en œuvre en 1976. En 1978, une deuxième version a été publiée par DEC, Intel et Xerox qui ont travaillé ensemble pour publier **DIX** (qui signifie DEC, Intel et Xerox). Cela a également été appelé "Ethernet II".

En 1983, avec un changement que nous allons discuter bientôt, une nouvelle version d'Ethernet a été publiée – la norme IEEE 802.3, par l'association des normes IEEE.

Ethernet II et IEEE 802.3 sont largement utilisés, nous allons donc les couvrir tous les deux. Comme vous le verrez, ils sont presque identiques. Habituellement, les deux sont simplement appelés « Ethernet ».

Pour ce tutoriel, afin d'être précis sur ce que nous entendons, je préciserai explicitement si je parle d'Ethernet II ou d'IEEE 802.3.


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-95.png)
_Les versions d'Ethernet (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

# Aperçu de la trame Ethernet

Examinons le format de la trame Ethernet :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-98.png)
_En-tête et pied de la trame Ethernet (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

## Avant la trame – Préambule (8 octets)

Tout d'abord, il y a un **préambule** composé de 8 octets, chacun contenant le motif de bits alternant `1` et `0`, c'est-à-dire `10101010`.

Dans Ethernet II, les 8 octets avaient ce motif. Dans 802.3, les sept premiers octets portent la valeur `10101010`, mais le dernier bit du dernier octet est défini sur `1`, donc l'octet porte la valeur `1010101**1**`.

Ce dernier octet est appelé le **début de trame**. Les deux derniers bits `1` indiquent au récepteur que le reste de la trame est sur le point de commencer.

L'envoi de ce motif de bits avant une nouvelle trame permet aux appareils du réseau de synchroniser facilement leurs horloges de réception. Notez que le préambule ne fait pas vraiment partie de la trame réelle – il précède simplement chaque trame, et vous ne le verrez donc pas sur de nombreux diagrammes du protocole Ethernet.


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-99.png)
_Préambule Ethernet (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

## Adresse de destination et adresse source (6 octets chacune)

Ensuite, nous avons deux adresses, chacune composée de **6** octets. Je décrirai les adresses Ethernet plus en détail plus tard dans cet article, mais pour l'instant, notons qu'une trame commence par une adresse de **destination**, suivie de l'adresse **source**.

Pourquoi la trame commence-t-elle par l'adresse de destination ? Y a-t-il une raison à cela ?

Eh bien, il y en a une. La toute première chose qu'un appareil est susceptible de faire avec une trame qu'il a reçue est de vérifier si cette trame lui est destinée ou non. Si la trame n'est pas destinée à cet appareil, elle peut être simplement abandonnée. Par conséquent, l'adresse de destination arrive en premier.

Pourquoi l'adresse source est-elle importante ? Eh bien, pour savoir à qui le récepteur doit envoyer une réponse, si nécessaire. Cette adresse source joue également un rôle dans la manière dont certains appareils réseau sont implémentés, comme nous le verrons dans de futurs articles.

## Champ Type / Longueur – Ethernet II (Type) (2 octets)

Ensuite, nous avons un champ assez problématique, appelé le champ **Type** ou **Longueur**.

Dans Ethernet II, ce champ est appelé **Type**, et indique au récepteur quel type de charge utile cette trame transporte.

Par exemple, si cette trame transporte une couche IP (c'est-à-dire que les _données_ de la couche Ethernet sont un paquet IP), alors la carte réseau réceptrice doit transmettre la charge utile de la trame au gestionnaire IP. Si la charge utile de la trame est ARP, alors le gestionnaire ARP doit la traiter.

Par **gestionnaire**, j'entends le code qui gère ce protocole, par exemple le code qui analyse ARP.

Nous reviendrons sur le besoin de Longueur et comment il est traité dans IEEE 802.3 sous peu.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-100.png)
_Dans Ethernet II, le champ Type transporte le type de la charge utile (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

## Données et bourrage (46-1500 octets)

Après ce champ, nous obtenons jusqu'à 1500 octets de **données**. Ce nombre a été choisi parce que la RAM était chère en 1978, et un récepteur aurait eu besoin de plus de RAM si la trame avait été plus grande.

Cela signifie que si la troisième couche veut envoyer plus de 1500 octets de données sur Ethernet, elle doit être envoyée sur plusieurs trames.

Il y a aussi une longueur minimale de données, qui est de 46 octets. Avec les autres champs de la trame, la longueur minimale d'une trame Ethernet est de 64 octets au total.

Pourquoi aurions-nous besoin d'une longueur de trame minimale ? Nous en discuterons dans une section ultérieure.

Pour l'instant, étant donné que nous avons une longueur minimale pour une trame Ethernet, que se passe-t-il si l'expéditeur veut envoyer un message très court, disons juste un octet ?

Dans ce cas, l'expéditeur doit **bourrer** le message, par exemple avec des `0` jusqu'à atteindre la longueur minimale. Par exemple, si l'expéditeur veut envoyer seulement 1 octet de données, comme la lettre `A`, il devra ajouter 45 octets de `0`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-101.png)
_46-1500 octets de données, avec bourrage si nécessaire (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

## Somme de contrôle – CRC32 (4 octets)

Enfin, mais non des moindres, nous avons une **somme de contrôle**. Il s'agit d'une [somme de contrôle CRC 32 bits](https://en.wikipedia.org/wiki/Cyclic_redundancy_check), utilisée pour déterminer si les bits de la trame ont été reçus correctement. En cas d'erreur, la trame est abandonnée.

Le CRC est calculé sur **l'ensemble de la trame** – c'est-à-dire, y compris l'en-tête. Notez qu'il n'inclut pas le préambule, car il ne fait pas vraiment partie de la trame.

Lorsque nous utilisons CRC-32 pour la somme de contrôle, nous définissons un surcoût fixe de 32 bits, ou 4 octets, indépendamment de la longueur des données. En d'autres termes, si nous envoyons seulement 1 octet de données, nous obtenons une somme de contrôle de 32 bits, et si nous envoyons mille octets de données – nous obtenons toujours 32 bits de somme de contrôle.

## Le problème avec le champ Type / Longueur

Auparavant, nous avons mentionné que le champ **Données** doit être d'au moins 46 octets, et si ce n'est pas le cas, nous le bourrons. Pour simplifier, supposons que nous bourrons avec des `0`, comme l'indique la norme.

Eh bien, nous avons en fait un problème ici.

Supposons que l'expéditeur veut envoyer un seul octet, composé du caractère `A`. Il enverra donc un `A` suivi de 45 `0`.

Que se passe-t-il si l'expéditeur veut envoyer `A` et zéro ? C'est-à-dire, les données consistent réellement en `A0`. Dans ce cas, il enverrait également un `A`, suivi de 45 `0`. Mais cette fois, le premier zéro fait réellement partie des données, et non du bourrage.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-102.png)
_Que l'expéditeur souhaite envoyer `A` comme données ou `A0` comme données, en raison du bourrage, la trame se compose de `A` et de 45 `0` (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

En tant que récepteur, vous auriez besoin d'un moyen de différencier ces cas, et de comprendre quels octets appartiennent au bourrage, et quels octets appartiennent aux données, en cas de trame courte.

Ethernet II a traité ce problème en... Eh bien, en ne le traitant pas. C'est-à-dire, la troisième couche recevra les données et le bourrage, qui serait un `A` suivi de 45 `0` dans cet exemple. Elle devra ensuite déterminer par elle-même quels octets appartiennent aux données et lesquels n'en font pas partie.

Cela est réalisable, bien sûr, si la troisième couche inclut un champ de longueur. Cependant, cette solution est loin d'être élégante – pourquoi la troisième couche traiterait-elle un problème de bourrage qui devrait être traité par la deuxième couche ?

C'est une violation claire de notre modèle de couches (si vous souhaitez voir un aperçu du modèle des couches, reportez-vous à [ce tutoriel](https://www.freecodecamp.org/news/the-five-layers-model-explained/)).

Pour cette raison, l'IEEE a décidé de changer le champ **Type** en un champ **Longueur** dans IEEE 802.3. Ainsi, par exemple, une trame transportant un seul octet de données, `A`, aura le champ Longueur défini sur `1`, tandis qu'une trame transportant deux octets de données, `A0`, aura le champ Longueur défini sur `2`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-103.png)
_Dans 802.3, le champ Longueur sépare les données du bourrage (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

C'est une solution élégante, mais deux problèmes se posent maintenant :

Premièrement, si vous recevez une trame Ethernet, comment savez-vous si c'est une trame Ethernet II, où ce champ signifie Type, ou une trame IEEE 802.3, où ce champ signifie longueur ?

Deuxièmement, que se passe-t-il avec le champ Type ? Comment le récepteur saurait-il quel protocole est transporté dans la trame ?

Commençons par la première question. Juste pour clarifier, au moment où IEEE 802.3 a été publié, de nombreuses cartes Ethernet étaient déjà en service. Les gens ne voulaient pas remplacer leurs cartes réseau simplement parce qu'une nouvelle norme avait été publiée.

Réfléchissez-y, voudriez-vous acheter une nouvelle carte réseau ? Ou peut-être vos amis qui ne sont pas programmeurs – achèteraient-ils une nouvelle carte parce que quelqu'un leur a dit que « les geeks de l'internet » avaient décidé qu'il y avait « une nouvelle norme » (quoi que cela signifie ?).

La solution était de permettre à Ethernet II et IEEE 802.3 de fonctionner sur le même réseau.

Heureusement, toutes les valeurs **Type** utilisées à cette époque avaient des valeurs supérieures à `1500`. La solution est donc simple : si ce champ a une valeur inférieure ou égale à `1500`, il signifie en fait Longueur. Si elle a une valeur supérieure ou égale à `1536`, elle signifie Type. Les valeurs intermédiaires n'ont actuellement aucune signification.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-104.png)
_Le champ Type/Longueur est divisé : les valeurs égales ou inférieures à 1500 sont des valeurs de Longueur, et les valeurs égales ou supérieures à 1536 sont des valeurs de Type. (Source : [Brief](https://www.youtube.com/watch?v=SoTRqDLND6Y&ab_channel=Brief))_

Par exemple, si nous voyons une trame où la valeur de ce champ est `400`, il est clair que nous avons une trame IEEE 802.3, qui est longue de `400` octets.

Maintenant, essayez : dans le cas où nous voyons une trame où ce champ est défini sur `20`, s'agit-il d'une trame Ethernet II ou IEEE 802.3 ?

En effet, il s'agit d'une trame IEEE 802.3, qui a `20` octets de données, et donc `26` octets de bourrage. Et... dans le cas où nous voyons une trame où ce champ est défini sur `2000` ?

Dans ce cas, nous savons qu'il s'agit d'une trame Ethernet II, et `2000` est le Type.

C'est ainsi que nous savons si nous traitons une trame Ethernet 2 ou une trame IEEE 802.3.

Ensuite, comment une trame IEEE 802.3 contient-elle les informations de Type ? C'est-à-dire, étant donné qu'IEEE 802.3 a remplacé le champ Type, il n'y avait aucun moyen pour le récepteur de déterminer quoi faire avec une trame entrante. Ainsi, IEEE 802.3 ajoute un autre en-tête du [protocole 802.2 LLC (Logical Link Control)](https://en.wikipedia.org/wiki/IEEE_802.2) juste avant les données. Cet en-tête transmet les informations de type.

Ainsi, une trame IEEE 802.3 aura un champ d'adresse de destination, puis un champ source, puis un champ de longueur, et ensuite un en-tête LLC, suivi des données et de la somme de contrôle.

### Attendez, IEEE 802.3 n'a-t-il pas été publié en 1983 ? Pourquoi est-il pertinent ? 🤔

Comme mentionné précédemment, en 1978, Ethernet II a été publié. Peu de temps après, en 1983, un nouveau format est sorti – et ses auteurs ont permis la compatibilité ascendante, croyant probablement que dans quelques années, tous les appareils seraient mis à niveau vers la nouvelle norme.

Oh, comme ils avaient tort.

Si vous vérifiez votre propre réseau (à condition que vous soyez connecté à un réseau Ethernet), je parie que vous verrez des trames Ethernet II.

Votre appareil prend probablement en charge les deux versions, mais par défaut, il transmettra des trames Ethernet II, plutôt que 802.3. Après tout, il est garanti que tout appareil connecté à un réseau Ethernet peut lire les trames Ethernet II, et il n'est pas garanti que l'appareil puisse lire les trames 802.3. Si Ethernet II fonctionne, pourquoi ne pas l'utiliser ?

Tous les protocoles de troisième couche ont dû tenir compte du fait qu'Ethernet ne résout pas le problème de différenciation des données du bourrage. Donc, si tous les protocoles gèrent déjà cela, pourquoi ne pas simplement... garder les choses telles qu'elles sont ?

Les appareils terminaux (comme les ordinateurs personnels) communiquent presque toujours via Ethernet II. IEEE 802.3 est également très courant, cependant, et il est utilisé par défaut sur la plupart des appareils réseau modernes (comme les commutateurs).

Cette histoire implique en fait une leçon très importante.

Il est très, très difficile de remplacer les protocoles après coup, surtout lorsqu'ils sont implémentés sur des appareils matériels (comme les cartes réseau).

### Qu'est-ce qu'un intervalle inter-paquets ?

Après qu'une trame Ethernet est envoyée, les émetteurs attendent une très courte période de temps avant de transmettre la trame suivante, afin de permettre au récepteur de savoir que la transmission d'une trame est terminée. Ce temps d'inactivité entre les trames est appelé « intervalle inter-paquets ».

# Comment fonctionnent les adresses Ethernet

Chaque trame Ethernet transporte deux adresses – d'abord, la destination, et ensuite, la source. Nous avons mentionné que l'adresse de destination apparaît en premier afin que le récepteur puisse déterminer si la trame est pertinente pour lui. Si ce n'est pas le cas, la trame sera rejetée.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-105.png)
_Adresses Ethernet dans la trame Ethernet (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

À quoi ressemble une adresse Ethernet ?

Une adresse Ethernet se compose de 6 octets – c'est-à-dire 48 bits. Habituellement, elles sont présentées en base hexadécimale, délimitées soit par des tirets, soit par des deux-points, comme vous pouvez le voir dans ces exemples :


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-106.png)
_Deux représentations de la même adresse Ethernet (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

```
00:01:42:a9:c2:dd
00-01-42-a9-c2-dd
```

Ce sont deux représentations de la même adresse Ethernet, et il n'y a pas de réelle différence entre les deux.

En général, les adresses Ethernet sont censées être globalement uniques. C'est-à-dire, aucun deux appareils Ethernet ne partagent la même adresse (au moins, en théorie).

Les trois premiers octets de toute adresse sont appelés **OUI** – Organisationally Unique Identifier. Pour s'assurer que les adresses sont uniques, l'IEEE attribue ces OUI à divers fabricants, tels que Dell, HP ou IBM.

Cette partie de l'adresse est également appelée **Vendor ID** (à l'exception des deux bits les moins significatifs, comme nous le verrons). Ensuite, les fabricants attribuent les 3 octets restants à des hôtes spécifiques. Cette partie est également appelée **Host ID**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-107.png)
_Les 3 octets les plus significatifs sont le Vendor ID, et les 3 octets les moins significatifs sont le Host ID (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

Par exemple, l'OUI `00:01:42` appartient à Cisco. Maintenant, Cisco peut fabriquer une carte réseau et lui attribuer l'adresse `00:01:42:00:00:01`. Ensuite, elle peut fabriquer une autre carte et lui attribuer l'adresse `00:01:42:00:00:02`, et ainsi de suite. Ces deux adresses partagent le même **Vendor ID**, mais ont des **Host IDs** différents.

Puisqu'un seul OUI laisse 3 octets à utiliser pour les Host IDs, nous avons `2^24` Host IDs par OUI – c'est-à-dire 16 777 216 Host IDs. Bien sûr, les grands fabricants ont besoin de beaucoup plus d'adresses, et ainsi, plusieurs OUI leur sont attribués. Par exemple, `00:01:64` est un autre OUI qui appartient à Cisco.

## Bits Unicast et Multicast

Les adresses Ethernet comportent également deux bits spéciaux.

Le premier bit spécial indique si l'adresse est une adresse unicast ou multicast. Unicast signifie que l'adresse représente un seul appareil. Les adresses multicast représentent un groupe d'appareils – comme toutes les imprimantes du réseau, ou tous les appareils du même réseau local.

Le bit représentant si l'adresse est unicast ou multicast est le bit le moins significatif dans l'octet le plus significatif. Attendez, quoi ?

Considérons l'adresse Ethernet suivante :

`06:b2:d9:a2:32:9e`

L'octet le plus significatif est `06`.

Convertissons cela en binaire :

`00000110`

Maintenant, nous regardons le bit le moins significatif – c'est-à-dire ce `0` :


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-108.png)
_Quand le bit le moins significatif dans l'octet le plus significatif est défini sur `0`, il s'agit d'une adresse Unicast (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

Ce bit est éteint. Cela signifie qu'il s'agit d'une adresse **unicast**. En d'autres termes, elle appartient à un seul appareil, comme la carte réseau d'un ordinateur.

Considérons une autre adresse :

`11:c0:ff:ee:d8:ab`

L'octet le plus significatif est `11` (en base hexadécimale).

Convertissons cela en binaire :

`00010001`

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-109.png)
_Quand le bit le moins significatif dans l'octet le plus significatif est défini sur `1`, il s'agit d'une adresse Multicast (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

Le bit le moins significatif est celui-ci. Puisqu'il est allumé, nous pouvons dire qu'il s'agit d'une adresse **multicast**. C'est-à-dire, c'est l'adresse d'un groupe. Vous pouvez envoyer une trame à cette adresse, et tous les appareils qui appartiennent à ce groupe considéreront la trame comme envoyée à eux.

Une adresse multicast très célèbre est appelée l'adresse de **diffusion**, c'est-à-dire le groupe qui contient toutes les machines. L'adresse de ce groupe est :

`FF:FF:FF:FF:FF:FF`

En d'autres termes, l'adresse où tous les bits sont allumés.

**Toutes** les machines font partie du groupe de diffusion.

### Bit globalement unique / localement administré

Le deuxième bit spécial indique si l'adresse est effectivement globalement unique. Ce bit est le deuxième bit le moins significatif dans l'octet le plus significatif. Euh, quoi ?

Eh bien, encore une fois, considérons la première adresse d'avant :

`06:b2:d9:a2:32:9e`

Le premier octet est `06`.

Converti en binaire, nous obtenons :

`00000110`

Donc, le deuxième bit le moins significatif est celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-110.png)
_Quand le deuxième bit le moins significatif dans l'octet le plus significatif est défini sur `1`, cette adresse n'est **pas** globalement unique (Source : [Brief](https://www.youtube.com/watch?v=sGZzU4U39Bw&ab_channel=Brief))_

Ce bit est allumé, et ainsi nous savons que cette adresse n'est en fait **pas** globalement unique. L'IEEE n'attribuera jamais cette adresse à un fournisseur. Alors, quelle est cette adresse ? Eh bien, dans ce cas, c'est simplement une adresse que j'ai inventée. Si je le voulais, je pourrais l'attribuer à un appareil spécifique. Le fait que ce bit soit allumé déclare qu'elle n'est pas globalement unique.

Considérons une autre adresse :

`00:01:42:a9:c2:dd`

Le premier octet est `00`, donc le deuxième bit le moins significatif est `0`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-111.png)

Il s'agit effectivement d'une adresse globalement unique, attribuée à Cisco.

### Adresses Ethernet – Récapitulatif

Donc, en résumé, une adresse Ethernet a deux parties principales : l'identifiant du fournisseur et l'identifiant de l'hôte.

Il y a également deux bits spéciaux : le bit le moins significatif dans l'octet le plus significatif indique si l'adresse est unicast ou multicast. Le deuxième bit le moins significatif dans l'octet le plus significatif indique si l'adresse est globalement unique.

# Pourquoi une trame Ethernet a-t-elle une longueur minimale ?

Ceci est plus une partie « bonus » de cet article, et concerne les collisions. Les collisions sont un sujet très intéressant, mais comme cet article se concentre sur le protocole Ethernet, les collisions ne seront pas notre focus. Je vais donc aborder ce problème brièvement. Bien qu'il ne soit pas crucial à comprendre pour comprendre les trames Ethernet, j'ai promis un aperçu _complet_ du protocole Ethernet.

Dans l'aperçu, j'ai mentionné qu'une trame Ethernet se compose d'un minimum de 46 octets de données et d'un maximum de 1500 octets de données. J'ai déjà expliqué pourquoi nous avons cette limite maximale, mais qu'en est-il du minimum ?

Pour simplifier notre discussion, considérons un réseau utilisant l'Ethernet classique où tous les ordinateurs sont attachés à un seul câble.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-112.png)
_Un réseau « Ethernet classique » avec quatre appareils connectés via un seul câble (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Supposons que A veut envoyer un message à B, et que C veut envoyer un message à D. Supposons que pendant que A transmet sa trame, C transmet également sa trame. Dans ce cas, les trames vont _entrer en collision_.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-113.png)
_En cas de transmission de données par deux appareils en même temps, leurs trames entreront en collision (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Lorsque cela se produit, nous obtenons des erreurs – un peu comme le cas où deux personnes commencent à parler en même temps, et il est impossible de comprendre l'une ou l'autre.

## Comment les collisions sont-elles gérées dans Ethernet ?

Ethernet utilise deux mécanismes principaux pour gérer les collisions. Le premier s'appelle **CSMA**, qui signifie **Carrier Sense Multiple Access**. Cela signifie essentiellement que lorsqu'une station veut transmettre des données, elle vérifie d'abord le canal pour voir si quelqu'un d'autre transmet en vérifiant le niveau du signal de la ligne. Si le canal est utilisé, la station attendra et réessayera.

Ainsi, si A transmet et que C veut envoyer des données, C attendra que A termine sa transmission avant de commencer à transmettre.

C'est un peu comme le cas dans une conversation humaine, où une personne attend que l'autre arrête de parler, et seulement alors cette personne parle.

Pourtant, tout comme le cas où deux personnes pourraient commencer à parler en même temps, deux machines Ethernet pourraient commencer à transmettre des données en même temps. Dans ce cas, **CD** – **Collision Detection** – entre en jeu. La détection de collision signifie que les appareils de transmission détectent le fait qu'une collision s'est produite. Cela est réalisé en écoutant le canal pendant la transmission.

Par exemple, supposons que la station A transmet le flux de bits `11001010`. Pendant la transmission, A écoute également le canal. Si aucune collision ne s'est produite, A lirait également le signal `11001010` de la ligne.


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-114.png)
_Avec la **détection de collision**, A écoute le canal pendant la transmission des données. En cas d'absence de collision, A détecte exactement le flux de bits qu'il a envoyé (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Si, cependant, une collision s'est produite, disons avec une trame envoyée par C, alors A lirait quelque chose de différent de la ligne – par exemple, `11011010`. De cette manière, la machine A réalise que sa trame est entrée en collision.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-115.png)
_Avec la **détection de collision**, A écoute le canal pendant la transmission des données. En cas de collision, A lit un flux de bits différent de celui qu'il a envoyé (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

La machine A peut réaliser qu'une collision s'est produite même avant d'avoir terminé la transmission de la trame. Ensuite, la machine A arrête de transmettre et envoie un signal JAM pour informer l'autre station qu'une collision s'est produite. En conséquence, les deux stations arrêtent de transmettre et attendent un intervalle de temps aléatoire avant d'essayer de soumettre à nouveau.

La durée d'attente des stations augmente avec le nombre de collisions dans le réseau. Ainsi, lors de la première collision, A et C attendent une durée relativement courte avant de transmettre à nouveau. Si une autre collision se produit, ils pourraient attendre plus longtemps.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-116.png)
_Après qu'une collision se produit, la durée d'attente des stations augmente avec le nombre de collisions dans le réseau (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Maintenant, revenons à Ethernet. Ethernet exige que les trames valides doivent être d'au moins 64 octets de long, de l'adresse de destination à la somme de contrôle, y compris les deux. Ainsi, ces données doivent être d'au moins 46 octets de long. Si la trame est trop courte, elle doit être bourrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-117.png)
_La longueur minimale d'une trame Ethernet se compose de 46 octets de données, ou 64 octets au total (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Une raison d'avoir cette longueur minimale est directement liée au mécanisme de détection de collision mentionné ci-dessus.

Considérons le scénario suivant. L'hôte A veut transmettre une trame très très courte à B, une trame qui n'est que d'un octet de long. J'exagère bien sûr, cela ne peut pas vraiment se produire dans Ethernet, mais cela sera utile pour l'explication.

L'hôte A transmet cette trame, qui se compose de 8 `1`. Ensuite, A écoute le canal pendant la transmission, et lit également 8 `1` de celui-ci, arrivant à la conclusion que la trame a été transmise avec succès.

Cependant, avant que la trame n'atteigne l'autre extrémité du réseau, D commence à transmettre une trame très courte, d'un octet de long, composée de 8 `0`. D écoute le canal pendant la transmission, et lit également 8 `0` de celui-ci, concluant que la trame a été transmise avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-118.png)
_A et D envoient tous deux une trame très courte, et ils terminent la transmission sans réaliser qu'une collision est susceptible de se produire (Source : [Brief](https://www.youtube.com/watch?v=ECl8DnWeVD4&ab_channel=Brief))_

Maintenant, ces deux trames très courtes entrent en collision. Pourtant, ni A ni D ne sont conscients de cette collision, car ils ont déjà conclu que la trame a été livrée avec succès.

Afin d'éviter de tels cas, la trame doit être suffisamment longue pour empêcher une station de terminer sa transmission avant que le premier bit de la trame n'atteigne l'extrémité éloignée de la ligne. Avoir une longueur minimale pour les trames Ethernet résout ce problème.

Ceci était une très brève discussion sur les collisions. Si vous souhaitez en savoir plus sur ce sujet, reportez-vous à la section "ressources supplémentaires" ci-dessous.

# Conclusion

Dans ce tutoriel, nous avons couvert chaque bit et octet du protocole Ethernet. Vous devriez maintenant avoir une bonne compréhension de ce protocole, ainsi qu'une référence à consulter lorsque nécessaire.

## **À propos de l'auteur**

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne YouTube [Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

### **Références supplémentaires**

* [Liste de lecture Computer Networks - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)
* [Carrier-sense multiple access with collision detection - Wikipedia](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection)
* [Carrier Sense Multiple Access Collision Detect (CSMA/CD) Explained - ITPRC](https://www.itprc.com/carrier-sense-multiple-access-collision-detect-csmacd-explained/)