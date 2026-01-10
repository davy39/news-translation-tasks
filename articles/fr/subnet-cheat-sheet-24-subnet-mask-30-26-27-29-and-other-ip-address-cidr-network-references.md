---
title: Guide de référence des sous-réseaux – Masque de sous-réseau 24, 30, 26, 27,
  29 et autres références CIDR d'adresses IP
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-02-12T19:06:00.000Z'
originalURL: https://freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9647740569d1a4ca10a9.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: Network Engineering
  slug: network-engineering
- name: networking
  slug: networking
seo_title: Guide de référence des sous-réseaux – Masque de sous-réseau 24, 30, 26,
  27, 29 et autres références CIDR d'adresses IP
seo_desc: 'As a developer or network engineer, you may need to occasionally look up
  subnet mask values and figure out what they mean.

  To make your life easier, the freeCodeCamp community has made this simple cheat
  sheet. Just scroll or use Ctrl/Cmd + f to find ...'
---

En tant que développeur ou ingénieur réseau, vous pouvez parfois avoir besoin de consulter les valeurs des masques de sous-réseau et de comprendre leur signification.

Pour vous faciliter la tâche, la communauté freeCodeCamp a créé cette simple fiche mémo. Il vous suffit de faire défiler ou d'utiliser Ctrl/Cmd + f pour trouver la valeur que vous cherchez.

Voici les tableaux, suivis de quelques explications sur leur signification.

| CIDR | Masque de sous-réseau | Masque générique | Nombre d'adresses IP | Nombre d'adresses IP utilisables |
|------|----------------------|------------------|---------------------|----------------------------------|
| /32  | 255.255.255.255      | 0.0.0.0          | 1                   | 1                                |
| /31  | 255.255.255.254      | 0.0.0.1          | 2                   | 2*                              |
| /30  | 255.255.255.252      | 0.0.0.3          | 4                   | 2                                |
| /29  | 255.255.255.248      | 0.0.0.7          | 8                   | 6                                |
| /28  | 255.255.255.240      | 0.0.0.15         | 16                  | 14                               |
| /27  | 255.255.255.224      | 0.0.0.31         | 32                  | 30                               |
| /26  | 255.255.255.192      | 0.0.0.63         | 64                  | 62                               |
| /25  | 255.255.255.128      | 0.0.0.127        | 128                 | 126                              |
| /24  | 255.255.255.0        | 0.0.0.255        | 256                 | 254                              |
| /23  | 255.255.254.0        | 0.0.1.255        | 512                 | 510                              |
| /22  | 255.255.252.0        | 0.0.3.255        | 1 024               | 1 022                            |
| /21  | 255.255.248.0        | 0.0.7.255        | 2 048               | 2 046                            |
| /20  | 255.255.240.0        | 0.0.15.255       | 4 096               | 4 094                            |
| /19  | 255.255.224.0        | 0.0.31.255       | 8 192               | 8 190                            |
| /18  | 255.255.192.0        | 0.0.63.255       | 16 384              | 16 382                           |
| /17  | 255.255.128.0        | 0.0.127.255      | 32 768              | 32 766                           |
| /16  | 255.255.0.0          | 0.0.255.255      | 65 536              | 65 534                           |
| /15  | 255.254.0.0          | 0.1.255.255      | 131 072             | 131 070                          |
| /14  | 255.252.0.0          | 0.3.255.255      | 262 144             | 262 142                          |
| /13  | 255.248.0.0          | 0.7.255.255      | 524 288             | 524 286                          |
| /12  | 255.240.0.0          | 0.15.255.255     | 1 048 576           | 1 048 574                        |
| /11  | 255.224.0.0          | 0.31.255.255     | 2 097 152           | 2 097 150                        |
| /10  | 255.192.0.0          | 0.63.255.255     | 4 194 304           | 4 194 302                        |
| /9   | 255.128.0.0          | 0.127.255.255    | 8 388 608           | 8 388 606                        |
| /8   | 255.0.0.0            | 0.255.255.255    | 16 777 216          | 16 777 214                       |
| /7   | 254.0.0.0            | 1.255.255.255    | 33 554 432          | 33 554 430                       |
| /6   | 252.0.0.0            | 3.255.255.255    | 67 108 864          | 67 108 862                       |
| /5   | 248.0.0.0            | 7.255.255.255    | 134 217 728         | 134 217 726                      |
| /4   | 240.0.0.0            | 15.255.255.255   | 268 435 456         | 268 435 454                      |
| /3   | 224.0.0.0            | 31.255.255.255   | 536 870 912         | 536 870 910                      |
| /2   | 192.0.0.0            | 63.255.255.255   | 1 073 741 824       | 1 073 741 822                    |
| /1   | 128.0.0.0            | 127.255.255.255  | 2 147 483 648       | 2 147 483 646                    |
| /0   | 0.0.0.0              | 255.255.255.255  | 4 294 967 296       | 4 294 967 294                    |

* /31 est un cas spécial détaillé dans [RFC 3021](https://tools.ietf.org/html/rfc3021) où les réseaux avec ce type de masque de sous-réseau peuvent attribuer deux adresses IP comme une liaison point à point.

Et voici un tableau des conversions décimales en binaires pour les masques de sous-réseau et les octets génériques :

|     | Masque de sous-réseau |     | Générique |
|-----|-----------------------|-----|-----------|
| 0   | 00000000              | 255 | 11111111  |
| 128 | 10000000              | 127 | 01111111  |
| 192 | 11000000              | 63  | 00111111  |
| 224 | 11100000              | 31  | 00011111  |
| 240 | 11110000              | 15  | 00001111  |
| 248 | 11111000              | 7   | 00000111  |
| 252 | 11111100              | 3   | 00000011  |
| 254 | 11111110              | 1   | 00000001  |
| 255 | 11111111              | 0   | 00000000  |

Notez que le masque générique est simplement l'inverse du masque de sous-réseau.

Si vous êtes nouveau dans le domaine de l'ingénierie réseau, vous pouvez [obtenir une meilleure idée de comment fonctionnent les réseaux informatiques ici](https://www.freecodecamp.org/news/computer-networks-and-how-to-actually-understand-them-c1401908172d/).

Enfin, cette fiche mémo et le reste de l'article se concentrent sur les adresses IPv4, et non sur le protocole IPv6 plus récent. Si vous souhaitez en savoir plus sur IPv6, consultez l'article sur les réseaux informatiques ci-dessus.

## Comment fonctionnent les blocs d'adresses IP ?

Les adresses IPv4 comme `192.168.0.1` sont en réalité des représentations décimales de quatre blocs binaires.

Chaque bloc est de 8 bits et représente des nombres de 0 à 255. Parce que les blocs sont des groupes de 8 bits, chaque bloc est connu sous le nom d'**octet**. Et puisque il y a quatre blocs de 8 bits, chaque adresse IPv4 est de 32 bits.

Par exemple, voici à quoi ressemble l'adresse IP `172.16.254.1` en binaire :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1125px-Ipv4_address.png)
_Source : [IPv4](https://en.wikipedia.org/wiki/IPv4)_

Pour convertir une adresse IP entre ses formes décimale et binaire, vous pouvez utiliser ce tableau :

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| x  | x  | x  | x  | x | x | x | x |

Le tableau ci-dessus représente un octet de 8 bits.

Maintenant, disons que vous voulez convertir l'adresse IP `168.210.225.206`. Tout ce que vous avez à faire est de diviser l'adresse en quatre blocs (`168`, `210`, `225` et `206`), et de convertir chacun en binaire en utilisant le tableau ci-dessus.

Rappelez-vous qu'en binaire, 1 est l'équivalent de "on" et 0 est "off". Donc pour convertir le premier bloc, `168`, en binaire, commencez simplement par le début du tableau et placez un 1 ou un 0 dans cette cellule jusqu'à obtenir une somme de `168`.

Par exemple :

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1   | 0  | 1  | 0  | 1 | 0 | 0 | 0 |

128 + 32 + 8 = 168, ce qui en binaire est `10101000`.

Si vous faites cela pour le reste des blocs, vous obtiendrez `10101000.11010010.11100001.11001110`.

## Qu'est-ce que le sous-réseautage ?

Si vous regardez le tableau ci-dessus, il peut sembler que le nombre d'adresses IP est pratiquement illimité. Après tout, il y a presque 4,2 milliards d'adresses IPv4 disponibles.

Mais si vous pensez à la croissance d'Internet et au nombre de dispositifs connectés de nos jours, il ne vous surprendra peut-être pas d'apprendre qu'il y a déjà une [pénurie d'adresses IPv4](https://whatismyipaddress.com/ipv4-shortage).

Parce que la pénurie a été reconnue il y a des années, les développeurs ont trouvé un moyen de diviser une adresse IP en réseaux plus petits appelés sous-réseaux.

Ce processus, appelé sous-réseautage, utilise la section hôte de l'adresse IP pour la diviser en ces réseaux plus petits ou sous-réseaux.

Généralement, une adresse IP est composée de bits de réseau et de bits d'hôte :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/network-and-host-bits.png)
_Source : [Qu'est-ce que IPv4](https://support.huawei.com/enterprise/en/doc/EDOC1100145159)_

Ainsi, généralement, le sous-réseautage fait deux choses : il nous donne un moyen de diviser les réseaux en sous-réseaux et permet aux dispositifs de déterminer si un autre dispositif/adresse IP est sur le même réseau local ou non.

Une bonne façon de penser au sous-réseautage est d'imaginer votre réseau sans fil à la maison.

Sans sous-réseautage, chaque dispositif connecté à Internet aurait besoin de sa propre adresse IP unique.

Mais puisque vous avez un routeur sans fil, vous n'avez besoin que d'une seule adresse IP pour votre routeur. Cette adresse IP publique ou externe est généralement gérée automatiquement et est attribuée par votre fournisseur de services Internet (FAI).

Ensuite, chaque dispositif connecté à ce routeur a sa propre adresse IP privée ou interne :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/home-network-diagram.png)
_Source : [Quelle est mon adresse IP ?](https://www.popularmechanics.com/technology/a32729384/how-to-find-ip-address/)_

Maintenant, si votre dispositif avec l'adresse IP interne `192.168.1.101` veut communiquer avec un autre dispositif, il utilisera l'adresse IP de l'autre dispositif et le masque de sous-réseau.

La combinaison des adresses IP et du masque de sous-réseau permet au dispositif à `192.168.1.101` de déterminer si l'autre dispositif est sur le même réseau (comme le dispositif à `192.168.1.103`), ou sur un réseau complètement différent quelque part ailleurs en ligne.

Intéressamment, l'adresse IP externe attribuée à votre routeur par votre FAI fait probablement partie d'un sous-réseau, qui peut inclure de nombreuses autres adresses IP pour les maisons ou entreprises à proximité. Et tout comme les adresses IP internes, elle a également besoin d'un masque de sous-réseau pour fonctionner.

### Comment fonctionnent les masques de sous-réseau

Les masques de sous-réseau fonctionnent comme un sorte de filtre pour une adresse IP. Avec un masque de sous-réseau, les dispositifs peuvent examiner une adresse IP et déterminer quelles parties sont les bits de réseau et quelles parties sont les bits d'hôte.

Ensuite, en utilisant ces informations, il peut déterminer la meilleure façon pour que ces dispositifs communiquent.

Si vous avez exploré les paramètres réseau sur votre routeur ou votre ordinateur, vous avez probablement vu ce nombre : `255.255.255.0`.

Si c'est le cas, vous avez vu un masque de sous-réseau très courant pour les réseaux domestiques simples.

Comme les adresses IPv4, les masques de sous-réseau sont de 32 bits. Et tout comme la conversion d'une adresse IP en binaire, vous pouvez faire la même chose avec un masque de sous-réseau.

Par exemple, voici notre tableau de tout à l'heure :

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| x  | x  | x  | x  | x | x | x | x |

Maintenant, convertissons le premier octet, 255 :

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1   | 1  | 1  | 1  | 1 | 1 | 1 | 1 |

Assez simple, n'est-ce pas ? Donc tout octet qui est `255` est simplement `11111111` en binaire. Cela signifie que `255.255.255.0` est en réalité `11111111.11111111.11111111.00000000` en binaire.

Maintenant, regardons un masque de sous-réseau et une adresse IP ensemble et calculons quelles parties de l'adresse IP sont les bits de réseau et les bits d'hôte.

Voici les deux en décimal et en binaire :

| Type | Décimal | Binaire |
|:--:|:--:| :--: |
| Adresse IP | 192.168.0.101 | 11000000.10101000.00000000.01100101 |
| Masque de sous-réseau | 255.255.255.0 | 11111111.11111111.11111111.00000000 |

Avec les deux disposés comme ceci, il est facile de séparer `192.168.0.101` en bits de réseau et en bits d'hôte.

Chaque fois qu'un bit dans un masque de sous-réseau binaire est 1, alors le même bit dans une adresse IP binaire fait partie du réseau, et non de l'hôte.

Puisque l'octet `255` est `11111111` en binaire, cet octet entier dans l'adresse IP fait partie du réseau. Donc les trois premiers octets, `192.168.0`, sont la partie réseau de l'adresse IP, et `101` est la partie hôte.

En d'autres termes, si le dispositif à `192.168.0.101` veut communiquer avec un autre dispositif, en utilisant le masque de sous-réseau, il sait que tout ce qui a l'adresse IP `192.168.0.xxx` est sur le même réseau local.

Une autre façon d'exprimer cela est avec un identifiant de réseau, qui est simplement la partie réseau de l'adresse IP. Donc l'identifiant de réseau de l'adresse `192.168.0.101` avec un masque de sous-réseau de `255.255.255.0` est `192.168.0.0`.

Et c'est la même chose pour les autres dispositifs sur le réseau local (`192.168.0.102`, `192.168.0.103`, et ainsi de suite).

### Que signifie CIDR et qu'est-ce que la notation CIDR ?

**CIDR** signifie Classless Inter-Domain Routing, et est utilisé dans IPv4, et plus récemment, dans le routage IPv6.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1920px-IP_Address_Match.svg.png)
_Source : [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)_

CIDR a été introduit en 1993 comme un moyen de ralentir l'utilisation des adresses IPv4, qui étaient rapidement épuisées sous l'ancien système d'adressage IP Classful sur lequel Internet a été initialement construit.

CIDR englobe quelques concepts majeurs.

Le premier est le sous-masquage de longueur variable (VLSM), qui permettait essentiellement aux ingénieurs réseau de créer des sous-réseaux au sein de sous-réseaux. Et ces sous-réseaux pouvaient être de différentes tailles, de sorte qu'il y aurait moins d'adresses IP inutilisées.

Le deuxième concept majeur introduit par CIDR est la notation CIDR.

La notation CIDR est en réalité simplement une abréviation pour le masque de sous-réseau, et représente le nombre de bits disponibles pour l'adresse IP. Par exemple, le `/24` dans `192.168.0.101/24` est équivalent à l'adresse IP `192.168.0.101` et au masque de sous-réseau `255.255.255.0`.

### Comment calculer la notation CIDR

Pour déterminer la notation CIDR pour un masque de sous-réseau donné, tout ce que vous avez à faire est de convertir le masque de sous-réseau en binaire, puis de compter le nombre de uns ou de chiffres "on". Par exemple :

| Type | Décimal | Binaire |
|:--:|:--:| :--: |
| Masque de sous-réseau | 255.255.255.0 | 11111111.11111111.11111111.00000000 |

Parce qu'il y a trois octets de uns, il y a 24 bits "on" ce qui signifie que la notation CIDR est `/24`.

Vous pouvez l'écrire des deux manières, mais je suis sûr que vous serez d'accord pour dire que `/24` est beaucoup plus facile à écrire que `255.255.255.0`.

Cela est généralement fait avec une adresse IP, alors regardons le même masque de sous-réseau avec une adresse IP :

| Type | Décimal | Binaire |
|:--:|:--:| :--: |
| Adresse IP | 192.168.0.101 | 11000000.10101000.00000000.01100101 |
| Masque de sous-réseau | 255.255.255.0 | 11111111.11111111.11111111.00000000 |

Les trois premiers octets du masque de sous-réseau sont tous des bits "on", donc cela signifie que les trois mêmes octets dans l'adresse IP sont tous des bits de réseau.

Regardons le dernier quatrième octet un peu plus en détail :

| Type | Décimal | Binaire |
|:--:|:--:| :--: |
| Adresse IP | 101 | 01100101 |
| Masque de sous-réseau | 0 | 00000000 |

Dans ce cas, parce que tous les bits de cet octet dans le masque de sous-réseau sont "off", nous pouvons être certains que tous les bits correspondants de cet octet dans l'adresse IP font partie de l'hôte.

Lorsque vous écrivez la notation CIDR, cela est généralement fait avec l'identifiant de réseau. Donc la notation CIDR de l'adresse IP `192.168.0.101` avec un masque de sous-réseau de `255.255.255.0` est `192.168.0.0/24`.

Pour voir plus d'exemples sur la façon de calculer la notation CIDR et l'identifiant de réseau pour une adresse IP et un masque de sous-réseau donnés, consultez cette vidéo :

%[https://www.youtube.com/watch?v=XQ3T14SIlV4]

## Adressage IP Classful

Maintenant que nous avons passé en revue quelques exemples de base de sous-réseautage et de CIDR, zoomons et regardons ce que l'on appelle l'adressage IP Classful.

Avant que le sous-réseautage ne soit développé, toutes les adresses IP tombaient dans une classe particulière :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/subnetting.png)
_Source : [Subnetting for dummies](https://community.spiceworks.com/networking/articles/2489-subnetting-for-dummies)_

Notez qu'il existe des adresses IP de classe D et E, mais nous les aborderons plus en détail un peu plus tard.

Les adresses IP Classful donnaient aux ingénieurs réseau un moyen de fournir à différentes organisations une plage d'adresses IP valides.

Il y avait beaucoup de problèmes avec cette approche qui ont finalement conduit au sous-réseautage. Mais avant d'aborder ceux-ci, regardons de plus près les différentes classes.

### Adresses IP de classe A

Pour les adresses IP de classe A, le premier octet (8 bits / 1 octet) représente l'identifiant de réseau, et les trois octets restants (24 bits / 3 octets) sont l'identifiant d'hôte.

Les adresses IP de classe A vont de `1.0.0.0` à `127.255.255.255`, avec un masque par défaut de `255.0.0.0` (ou `/8` en CIDR).

Cela signifie que l'adressage de classe A peut avoir un total de 128 (2<sup>7</sup>) réseaux et 16 777 214 (2<sup>24</sup>-2) adresses utilisables par réseau.

De plus, notez que la plage `127.0.0.0` à `127.255.255.255` dans la plage de classe A est réservée pour l'adresse de rebouclage de l'hôte (voir [RFC5735](https://tools.ietf.org/html/rfc5735)).

### Adresses IP de classe B

Pour les adresses IP de classe B, les deux premiers octets (16 bits / 2 octets) représentent l'identifiant de réseau et les deux octets restants (16 bits / 2 octets) sont l'identifiant d'hôte.

Les adresses IP de classe B vont de `128.0.0.0` à `191.255.255.255`, avec un masque de sous-réseau par défaut de `255.255.0.0` (ou `/16` en CIDR).

L'adressage de classe B peut avoir 16 384 (2<sup>14</sup>) adresses de réseau et 65 534 (2<sup>16</sup>) adresses utilisables par réseau.

### Adresses IP de classe C

Pour les adresses IP de classe C, les trois premiers octets (24 bits / 3 octets) représentent l'identifiant de réseau et le dernier octet (8 bits / 1 octet) est l'identifiant d'hôte.

Les adresses IP de classe C vont de `192.0.0.0` à `223.255.255.255`, avec un masque de sous-réseau par défaut de `255.255.255.0` (ou `/24` en CIDR).

La classe C se traduit par 2 097 152 (2<sup>21</sup>) réseaux et 254 (2<sup>8</sup>-2) adresses utilisables par réseau.

### Adresses IP de classe D et de classe E

Les deux dernières classes sont les classes D et E.

Les adresses IP de classe D sont réservées aux multicasts. Elles occupent la plage de `224.0.0.0` à `239.255.255.255`.

Les adresses IP de classe E sont expérimentales et sont tout ce qui est supérieur à `240.0.0.0`.

### Le problème avec les adresses IP Classful

Le principal problème avec les adresses IP Classful est qu'elles n'étaient pas efficaces et pouvaient entraîner un grand nombre d'adresses IP gaspillées.

Par exemple, imaginez que vous faites partie d'une grande organisation à cette époque. Votre entreprise compte 1 000 employés, ce qui signifie qu'elle tomberait dans la classe B.

Mais si vous regardez ci-dessus, vous verrez qu'un réseau de classe B peut supporter jusqu'à 65 534 adresses utilisables. C'est bien plus que ce dont votre organisation aurait probablement besoin, même si chaque employé avait plusieurs dispositifs avec une adresse unique.

Et il n'y avait aucun moyen pour votre organisation de revenir à la classe C - il n'y aurait tout simplement pas assez d'adresses IP utilisables.

Ainsi, bien que les adresses IP Classful aient été utilisées à l'époque où les adresses IPv4 sont devenues courantes, il est rapidement devenu clair qu'un meilleur système serait nécessaire pour garantir que nous n'épuiserions pas toutes les ~4,2 milliards d'adresses utilisables.

Les adresses IP Classful ne sont plus utilisées depuis qu'elles ont été remplacées par CIDR en 1993, et sont principalement étudiées pour comprendre l'architecture initiale d'Internet et pourquoi le sous-réseautage est important.

## J'espère que cette fiche mémo a été une référence utile pour vous

Si vous avez trouvé cela utile, veuillez le partager avec vos amis afin que plus de personnes puissent en bénéficier.

De plus, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/kriskoishigawa) et à me faire savoir ce que vous en pensez.