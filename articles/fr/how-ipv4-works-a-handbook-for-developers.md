---
title: Comment fonctionne IPv4 – Un guide pour les développeurs
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2025-04-30T15:52:50.448Z'
originalURL: https://freecodecamp.org/news/how-ipv4-works-a-handbook-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746028336196/79d97781-a9b8-4be3-86a1-47322e9640ff.png
tags:
- name: IPv4
  slug: ipv4
- name: computer networks
  slug: computer-networks
- name: networking
  slug: networking
- name: network
  slug: network
- name: ip address
  slug: ip-address
- name: IP
  slug: ip
- name: handbook
  slug: handbook
seo_title: Comment fonctionne IPv4 – Un guide pour les développeurs
seo_desc: The Internet Protocol version 4 (IPv4) is one of the core protocols of standards-based
  internetworking methods in the Internet and other packet-switched networks. IPv4
  is still the most widely deployed Internet protocol. Google’s IPv6 Statistics show...
---

Le protocole Internet version 4 (IPv4) est l'un des protocoles principaux des méthodes d'interconnexion basées sur des normes dans l'Internet et d'autres réseaux à commutation de paquets. IPv4 est toujours le protocole Internet le plus largement déployé. Les [statistiques IPv6 de Google](https://www.google.com/intl/en/ipv6/statistics.html) montrent que 44,29 % du trafic vers les services Google le 24 avril 2025 est en IPv6, ce qui implique que 55,71 % passe par IPv4.

Ce guide vous fera parcourir tous les aspects de IPv4, de la compréhension des adresses IP à l'examen des en-têtes de paquets et de la fragmentation. Vous apprendrez :

* Comment fonctionnent les adresses IP et leurs différents formats

* Les schémas d'adressage réseau, des longueurs fixes à CIDR

* Les adresses IPv4 spéciales et leurs utilisations

* La structure et le but de chaque champ dans l'en-tête IPv4

* Comment IPv4 gère la fragmentation des paquets à travers différents réseaux

Que vous soyez ingénieur réseau, développeur logiciel ou professionnel de l'informatique, comprendre IPv4 est crucial pour travailler avec les réseaux informatiques modernes.

### Ce que nous allons couvrir :

1. [Contexte](#heading-contexte)

2. [Comprendre les adresses IP](#heading-comprendre-les-adresses-ip)

3. [Identifiant de réseau et identifiant d'hôte](#heading-identifiant-de-reseau-et-identifiant-dhote)

4. [Comment déterminer les parties réseau et hôte](#heading-comment-determiner-les-parties-reseau-et-hote)

* [Approche à longueur fixe](#heading-approche-a-longueur-fixe)

* [Quels sont les inconvénients ici ? 🤔](#heading-quels-sont-les-inconvenients-ici)

5. [Adressage par classes](#heading-adressage-par-classes)

* [Attribution des adresses IP](#heading-attribution-des-adresses-ip)

* [Quels sont les inconvénients ici ? 🤔](#heading-quels-sont-les-inconvenients-ici-1)

6. [CIDR : Routage interdomaine sans classe](#heading-cidr-routage-interdomaine-sans-classe)

* [Exemple concret](#heading-exemple-concret)

7. [Masques de sous-réseau](#heading-masques-de-sous-reseau)

8. [Résumé intermédiaire – Adresses IPv4](#heading-resume-intermediaire-adresses-ipv4)

9. [Testez-vous](#heading-testez-vous)

* [Conversion entre la notation préfixe et les masques de sous-réseau](#heading-conversion-entre-la-notation-prefixe-et-les-masques-de-sous-reseau)

* [Travailler en sens inverse avec les masques de sous-réseau](#heading-travailler-en-sens-inverse-avec-les-masques-de-sous-reseau)

* [Préfixes non alignés sur les octets](#heading-prefixes-non-alignes-sur-les-octets)

* [Déterminer l'appartenance au réseau](#heading-determiner-lappartenance-au-reseau)

10. [Adresses IPv4 spéciales](#heading-adresses-ipv4-speciales)

* [L'adresse "Cet hôte" : 0.0.0.0](#heading-ladresse-cet-hote-0000)

* [Adresses "Ce réseau"](#heading-adresses-ce-reseau)

* [Adresses de diffusion](#heading-adresses-de-diffusion)

* [Adresses de boucle locale : 127.0.0.0/8](#heading-adresses-de-boucle-locale-1270008)

* [Résumé des adresses IPv4 spéciales](#heading-resume-des-adresses-ipv4-speciales)

11. [En-tête IPv4](#heading-en-tete-ipv4)

* [La structure de l'en-tête](#heading-la-structure-de-len-tete)

* [En-tête IPv4 – Résumé intermédiaire](#heading-en-tete-ipv4-resume-intermediaire)

12. [Fragmentation IPv4](#heading-fragmentation-ipv4)

* [Pourquoi la fragmentation est nécessaire](#heading-pourquoi-la-fragmentation-est-necessaire)

* [Comment fonctionne la fragmentation dans IP](#heading-comment-fonctionne-la-fragmentation-dans-ip)

* [Champ d'identification](#heading-champ-didentification)

* [Décalage de fragment](#heading-decalage-de-fragment)

* [Indicateurs Plus de fragments et Ne pas fragmenter](#heading-indicateurs-plus-de-fragments-et-ne-pas-fragmenter)

* [Exemple de fragmentation](#heading-exemple-de-fragmentation)

* [Fragmentation IPv4 – Résumé](#heading-fragmentation-ipv4-resume)

13. [Résumé – IPv4](#heading-resume-ipv4)

* [Adressage et structure du réseau](#heading-adressage-et-structure-du-reseau)

* [Structure de l'en-tête IPv4](#heading-structure-de-len-tete-ipv4)

* [Fragmentation](#heading-fragmentation)

* [Mots finaux](#heading-mots-finaux)

14. [À propos de l'auteur](#heading-a-propos-de-lauteur)

15. [Références supplémentaires](#heading-references-supplementaires)

## Notes rapides avant de commencer

1. Vous pouvez trouver plus de contenu sur les réseaux informatiques sur ma chaîne YouTube : [Liste de lecture Réseaux informatiques](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)

2. Je travaille sur un livre sur les réseaux informatiques ! Êtes-vous intéressé à lire les versions initiales et à fournir des commentaires ? Envoyez-moi un email : [gitting.things@gmail.com](mailto:gitting.things@gmail.com)

## Contexte

IP signifie "Internet Protocol", donc IPv4 est la version 4 du protocole Internet. Il a été décrit dans le RFC 791 par l'IETF, publié en septembre 1981, et déployé pour la première fois en production en 1982 sur SATNET (le réseau de satellites à paquets de l'Atlantique), qui était un réseau satellite précoce qui formait un segment initial de l'Internet.

IPv4 est sans connexion et fonctionne selon un modèle de livraison au mieux. Cela signifie qu'il ne garantit pas la livraison, l'ordre correct des paquets ou la validité des données. Il est conçu pour être rapide et flexible.

## Comprendre les adresses IP

Les adresses IP sont des adresses logiques hiérarchiques qui alimentent la plupart des connexions Internet aujourd'hui. Chacune se compose de `4` octets, ou `32` bits. Elles sont généralement écrites en notation décimale pointée, par exemple :

[![Un exemple d'adresse IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744039300370/348d757a-c6b0-4930-8e3a-ee753c45f3fa.png align="center")](https://www.youtube.com/watch?v=zlDkqP3lMmU)

Testez-vous – L'adresse suivante représente-t-elle une adresse IP valide ?

[![Est-ce une adresse IPv4 valide ? (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744039900249/587d8b94-1ac3-478c-87d9-4b0fd97023b2.png align="center")](https://www.youtube.com/watch?v=zlDkqP3lMmU)

Non. Puisque les points séparent différents octets, chaque valeur doit être comprise entre `0` et `255`. Comme le nombre `392` est supérieur à `255`, il ne peut pas être représenté dans un seul octet.

[![Ce n'est pas une adresse IPv4 valide (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744040039746/71392606-7ac8-441d-ac36-2cf05bb8d67f.png align="center")](https://www.youtube.com/watch?v=zlDkqP3lMmU)

## Identifiant de réseau et identifiant d'hôte

Les adresses IP ont deux parties : un **identifiant de réseau** (ou ID de réseau) qui appartient à tous les hôtes du réseau et un **identifiant d'hôte** (ou ID d'hôte) qui identifie l'hôte spécifique dans ce réseau.

L'identifiant de réseau sera le même pour tous les hôtes du réseau, et est également appelé un "préfixe". Par exemple, considérons un identifiant de réseau de `201.22.3`. Étant donné que ceci est le préfixe du réseau, les adresses suivantes :

```plaintext
201.22.3.15
201.22.3.91
```

Font partie du même réseau, car elles partagent le même préfixe. La première adresse appartient à l'hôte numéro `15` dans ce réseau, et la seconde appartient à l'hôte numéro `91`.

Cette adresse a un préfixe différent, ou un identifiant de réseau différent, et appartient donc à un réseau différent :

```plaintext
201.22.14.50
```

Dans les exemples ci-dessus, il y a un identifiant de réseau composé de 3 octets, ou 24 bits, et un identifiant d'hôte composé de 1 octet, ou 8 bits.

[![Identifiant de réseau vs Identifiant d'hôte (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744040184260/2511a5f3-3a98-40e4-aabe-7853e3febacf.png align="center")](https://www.youtube.com/watch?v=zlDkqP3lMmU)

## Comment déterminer les parties réseau et hôte

Une question se pose : comment savez-vous quels bits font partie de l'ID de réseau, et lesquels font partie de l'ID d'hôte ? Plusieurs approches ont évolué au fil du temps pour relever ce défi.

### Approche à longueur fixe

Considérons cette solution : Pour chaque adresse IP, le premier octet le plus significatif représenterait l'ID de réseau, et les trois octets restants, les moins significatifs, représenteraient l'ID d'hôte. De cette façon, il est vraiment facile de lire les adresses IP. Par exemple, pour cette adresse :

```plaintext
20.12.1.92
```

Vous savez qu'elle décrit le réseau `20`, et l'hôte `12.1.92` à l'intérieur de ce réseau. Toute adresse IP qui ne commence pas par `20`, comme `22.1.2.3`, résiderait dans un réseau différent, et toute adresse IP qui commence par `20`, comme `20.1.2.3`, serait dans le même réseau.

![Approche à longueur fixe pour l'adressage IP (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744040959545/38c8766b-5ad2-4fb1-98b1-612c70fbe8ad.png align="center")

### Quels sont les inconvénients ici ? 🤔

Avec seulement un octet (8 bits) pour représenter l'ID de réseau, vous n'avez que 2^8, ou `256`, réseaux différents. Bien sûr, il y a beaucoup plus de réseaux que cela dans le monde réel. Même dans les premiers jours de l'internet, les universités et les grandes entreprises avaient chacune besoin de leurs propres identifiants de réseau.

En général, l'utilisation d'une longueur fixe pour l'ID de réseau et d'une longueur fixe pour l'ID d'hôte n'est pas assez flexible. Si vous décidez que les deux octets les plus significatifs représenteront l'ID de réseau et que les deux octets les moins significatifs représenteront l'ID d'hôte, vous pouvez représenter jusqu'à 2^16, ou `65,536` réseaux, ce qui n'est pas suffisant non plus. De plus, certains réseaux, comme ceux des grandes entreprises, pourraient nécessiter plus de `65,536` identifiants d'hôtes.

## Adressage par classes

La solution réside dans l'apport de quelque flexibilité. Considérons une autre approche appelée "adressage par classes". Dans cette approche, le nombre de bits dédiés à l'ID de réseau change d'une adresse à l'autre, et vous pouvez déterminer l'ID de réseau en regardant le premier octet le plus significatif de l'adresse.

* Toute adresse commençant par un nombre entre `1` et `127` appartient à la "Classe A", ce qui signifie que son ID de réseau se compose de 1 octet, laissant 3 octets pour l'ID d'hôte.

* Toute adresse commençant par un nombre entre `128` et `191` appartient à la "Classe B", ce qui signifie que son ID de réseau est de 2 octets de long, et son ID d'hôte est également de 2 octets de long.

* Toute adresse commençant par un nombre entre `192` et `223` appartient à la "Classe C", donc elle a 3 octets d'ID de réseau, et 1 octet d'ID d'hôte.

Vous pouvez voir la représentation complète de cette approche dans le tableau ci-dessous :

| Classe | Plage du premier octet | Taille de l'ID de réseau | Taille de l'ID d'hôte |
| --- | --- | --- | --- |
| A | `1` - `127` | 1 octet | 3 octets |
| B | `128` - `191` | 2 octets | 2 octets |
| C | `192` - `223` | 3 octets | 1 octet |
| D | `224` - `239` | (multidiffusion) | |
| E | `240` - `255` | (réservé) | |

![Approche d'adressage par classes (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744088968355/e7f128c0-3173-4bb5-8872-3f820de6b354.png align="center")

Par exemple, à quelle classe appartient cette adresse ?

```plaintext
(1) 130.12.204.5
```

Puisqu'elle commence par `130`, qui est entre `128` et `191`, elle appartient à la "Classe B". Cela signifie que son ID de réseau est `130.12`, et son ID d'hôte est `204.5`. Appelons-la "adresse numéro 1".

Cette adresse et l'adresse suivante (2) appartiennent-elles au même réseau ?

```plaintext
(2) 130.90.2.40
```

Non, puisque leurs identifiants de réseau sont différents, elles ne sont pas dans le même réseau.

À quelle classe appartient l'adresse suivante ?

```plaintext
(3) 200.1.1.9
```

Elle appartient à la classe C, car la valeur de son premier octet, `200`, est entre `192` et `223`. Cela signifie que son identifiant de réseau est `200.1.1`, et toute adresse commençant par ce préfixe résidera dans le même réseau. Cette adresse spécifique décrit l'hôte `9` dans ce réseau.

Pour compléter le tableau, les adresses commençant par une valeur entre `224` et `239` appartiennent à la "Classe D" – c'est-à-dire les adresses de multidiffusion – des adresses qui appartiennent à plusieurs appareils. Les adresses commençant par une valeur entre `240` et `255` étaient réservées pour une utilisation future. Les adresses commençant par `0` sont des adresses spéciales.

### Attribution des adresses IP

Dans les premiers jours de l'Internet, les adresses IPv4 étaient attribuées aux organisations par l'Internet Assigned Numbers Authority (IANA). À mesure que l'Internet grandissait, cette responsabilité a été distribuée à cinq registres Internet régionaux (RIR) qui gèrent l'allocation des adresses pour différentes régions géographiques. Les grandes organisations recevaient des blocs d'adresses en fonction de leurs besoins, les classes d'adresses déterminant la taille de ces blocs.

### Quels sont les inconvénients ici ? 🤔

Bien que l'adressage par classes permette plus de flexibilité par rapport à l'approche à longueur fixe, même cette approche n'est pas assez flexible.

Considérons ce scénario : Une petite startup avec seulement deux fondateurs a besoin d'un identifiant de réseau. De quelle classe auraient-ils besoin ?

Obtenir une classe A ou B serait excessif, donc ils pourraient obtenir une classe C – permettant `256` adresses. C'est plus que nécessaire actuellement, mais permet une certaine expansion. Que se passe-t-il si la startup grandit à plus de `256` employés (et appareils) ?

À ce stade, ils devraient obtenir une adresse de classe B, donnant pas moins de `65,536` adresses, alors qu'ils n'ont besoin que d'un peu plus de `256` adresses. Cela signifie gaspiller plus de `60,000` adresses.

Cela est devenu un vrai problème au début des années 1990 alors que l'Internet grandissait plus rapidement. Le besoin de plus d'adresses IP est devenu apparent, et il y avait une épuisement imminent de l'espace d'adressage IPv4. Les cas où `60,000` adresses étaient gaspillées ne pouvaient plus être tolérés.

## CIDR : Routage interdomaine sans classe

L'une des mesures pour gérer cette pénurie d'adresses a été d'abandonner l'adressage par classes en 1993 et de passer à une autre approche appelée CIDR – Routage interdomaine sans classe. Cette approche est toujours utilisée aujourd'hui.

CIDR permet une flexibilité lors du choix de l'ID de réseau et de l'ID d'hôte. Il permet aux administrateurs réseau de créer des sous-réseaux de la taille précise, plutôt que d'être limité aux classes A, B ou C.

Commençons par un exemple simple. Dans la notation CIDR, nous ajoutons un suffixe indiquant combien de bits sont utilisés pour la partie réseau :

```plaintext
(4) 200.8.3.1/16
```

Cette notation de barre oblique spécifie combien de bits décrivent l'ID de réseau. Dans l'exemple (4) ci-dessus, les premiers `16` bits (ou `2` octets) sont utilisés pour l'ID de réseau. Donc, dans ce cas, `200.8` est l'identifiant de réseau, et `3.1` est l'identifiant d'hôte. Le fait que `200.8` soit l'ID de réseau signifie que toutes les adresses de `200.8.0.0` à `200.8.255.255` sont dans ce réseau.

![Adresse de masque de sous-réseau de 16 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744090490906/0a18b364-7ca2-4ed0-8f27-2103bcbdd579.png align="center")

Considérons ces adresses supplémentaires :

```plaintext
(5) 200.2.13.5
(6) 200.8.21.6
```

Étant donné ce préfixe d'adresse de `16` bits, ou `2` octets, lesquelles de ces adresses appartiennent au même réseau que l'exemple (4) (`200.8.3.1/16`) ?

La première adresse (5) (`200.2.13.5`) n'appartient pas à ce réseau, car ses premiers `16` bits – `200.2`, sont différents des premiers `16` bits de l'adresse de l'exemple.

La deuxième adresse (6) (`200.8.21.6`) appartient au même réseau que celle de l'adresse de l'exemple.

![Adresse de masque de sous-réseau de 16 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744090582529/d314c9ca-73a3-4e48-92b8-b0a6c24ac7d3.png align="center")

### Exemple concret

En pratique, un FAI peut recevoir un grand bloc comme `104.16.0.0/12` du RIR. Cela leur donne le contrôle de toutes les adresses de `104.16.0.0` à `104.31.255.255`. Le FAI peut ensuite allouer des sous-réseaux plus petits aux clients, comme donner à une petite entreprise un sous-réseau `/24` avec `256` adresses, ou à une entreprise plus grande un sous-réseau `/20` avec `4,096` adresses.

## Masques de sous-réseau

Une autre façon d'exprimer le préfixe de réseau est d'utiliser un [masque de sous-réseau](https://www.ipxo.com/blog/what-is-subnet-mask/), comme suit :

```plaintext
255.255.0.0
```

Lorsque converti en binaire, `255` en décimal équivaut à huit `1` en binaire – donc tous les bits sont activés. Donc si vous traduisez ce masque en binaire, vous obtenez :

```plaintext
11111111 11111111 00000000 00000000
```

En d'autres termes, `16` bits sont activés, ce qui signifie un préfixe de réseau de `16` bits. Les deux conventions (notation CIDR et masques de sous-réseau) sont utilisées très fréquemment.

![Adresse de masque de sous-réseau de 16 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744090679551/5466e739-1e1b-4e34-a044-0d680ca9ad6e.png align="center")

Avec CIDR, une adresse peut résider dans différents réseaux étant donné différents préfixes de réseau, ou masques de sous-réseau. Si vous considérez la même adresse d'exemple avec un préfixe différent, disons de `8` bits – les deux adresses supplémentaires appartiendraient au même réseau, car elles partagent toutes les `8` premiers bits – `200`.

Comment présenteriez-vous un préfixe de réseau de `8` bits sous forme de masque de sous-réseau ? Vous avez besoin que les `8` premiers bits soient activés, donc cela signifie `255` en décimal, et les bits restants sont désactivés, résultant en ce masque de sous-réseau :

```plaintext
255.0.0.0
```

![Adresse de masque de sous-réseau de 8 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744141258583/c4f606ff-410b-4b1f-92c5-505b5309cfa8.png align="center")

Que se passe-t-il si vous utilisez un préfixe de réseau de `24` bits ? D'abord, comment l'exprimeriez-vous sous forme de masque de sous-réseau ? Vous avez besoin que `24` bits soient activés, donc cela fait 3 fois 8 bits activés, résultant en :

```plaintext
255.255.255.0
```

![Adresse de masque de sous-réseau de 24 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744297152994/0dae747f-2a10-4ad6-9e29-b21df15e6169.png align="center")

Maintenant, aucune des adresses supplémentaires ne réside dans le même réseau que l'adresse d'exemple, car elles ne partagent pas son ID de réseau de `200.8.3`.

![CIDR (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744297174124/16ad2016-c358-474b-964c-4bde75359670.png align="center")

Notez que les préfixes de réseau n'ont pas besoin de représenter des octets complets. Par exemple, vous pouvez utiliser un préfixe de réseau de `12` bits, ou `11` bits, ou `22` bits. Lorsque la longueur du préfixe n'est pas un multiple de `8`, le masque de sous-réseau aura une valeur autre que `0` ou `255` dans l'une de ses positions.

Cela résout le problème concernant la startup. Si une startup a `300` employés, elle devrait obtenir un ID de réseau de `23` bits, laissant `9` bits pour les hôtes dans leurs réseaux. Cela signifie 2^9, ou `512` adresses, ce qui devrait être suffisant.

## Résumé intermédiaire – Adresses IPv4

Dans cette section, vous avez appris les bases des adresses IPv4. Les adresses IP sont des adresses logiques hiérarchiques composées de `4` octets. Les adresses IP ont deux parties : un identifiant de réseau qui appartient à tous les hôtes du réseau, et un identifiant d'hôte qui identifie l'hôte spécifique dans le réseau.

Vous avez exploré diverses options pour déterminer l'identifiant de réseau et l'identifiant d'hôte :

1. Approche à longueur fixe – trop rigide et limitée

2. Approche d'adressage par classes – meilleure mais toujours gaspilleuse

3. CIDR (Classless Interdomain Routing) – flexible et efficace

CIDR offre beaucoup plus de flexibilité et aide à surmonter le problème majeur de la pénurie d'adresses IPv4. Cependant, CIDR n'est qu'une partie de la solution à la pénurie d'adresses IPv4, avec d'autres solutions incluant le NAT (Network Address Translation) et finalement, IPv6.

La section suivante explorera les adresses IPv4 spéciales puis examinera l'en-tête des paquets IPv4.

## Testez-vous

Maintenant, pratiquez les concepts que vous avez appris et assurez-vous de vous sentir à l'aise avec eux.

Prenez un moment pour essayer de répondre aux questions suivantes avant de vérifier les réponses.

### Conversion entre la notation préfixe et les masques de sous-réseau

Comment représenteriez-vous un préfixe de réseau de `16` bits, écrit comme ceci `/16`, sous forme de masque de sous-réseau ?

Vous avez besoin de `16` bits qui sont activés. Lorsque `8` bits sont activés, vous obtenez `255` en décimal, donc vous utiliseriez :

```plaintext
255.255.0.0
```

![Adresse de masque de sous-réseau de 16 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465135834/ff449f60-e660-4fea-b427-994a87be2c89.png align="center")

Étant donné ce préfixe de réseau, ces adresses appartiennent-elles au même réseau ?

![Ces adresses correspondent-elles au réseau défini précédemment ? (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465178617/ef7ddeca-86b2-4bb2-8e1d-471ef4f64a45.png align="center")

Oui, elles le font, car elles partagent les mêmes `16` bits les plus significatifs, ou deux octets

![Ces adresses appartiennent au même réseau (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465209149/25744a22-16b3-484d-9821-12920dd59be4.png align="center")

Cette adresse appartient-elle au même réseau que les adresses précédentes ?

![Adresse supplémentaire (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465232371/92bcb42c-5067-43e6-8cec-1eae9347d16a.png align="center")

Oui, elle le fait. Encore une fois, elle partage les deux octets les plus significatifs.

![Cette adresse appartient également au réseau défini précédemment (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465259087/a4b9c525-3b4d-4501-bcf8-db62ebf47247.png align="center")

Et celle-ci ? Appartient-elle au même réseau que les adresses précédentes ?

![Adresse supplémentaire. Cette adresse appartient-elle au réseau défini précédemment ? (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465285214/f57fd6c2-7665-4565-943e-959b981fedc8.png align="center")

Non, car les deux premiers octets ne sont pas `42.31` – il s'agit d'un réseau différent. Donc cette adresse décrit l'hôte `1.2`, dans le réseau `42.32`.

![Non, cette adresse n'appartient pas au même réseau que les autres (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465302503/0fdd959f-2d10-4a56-826d-e71604ca5267.png align="center")

### Travailler en sens inverse avec les masques de sous-réseau

Essayons l'autre sens. Vous avez ce masque de sous-réseau :

```plaintext
255.255.255.0
```

Comment l'exprimeriez-vous en utilisant un préfixe de réseau ?

Vous avez trois occurrences de `255`, ce qui signifie trois fois `8` bits qui sont activés, donc au total vous avez `24` bits qui sont activés. Donc vous pouvez aussi écrire `/24`. Cela signifie `3` octets.

![Masque de sous-réseau de 24 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465331643/b1f3ab4c-8e7e-449d-8879-fee3bf90ce1c.png align="center")

Étant donné ce masque de sous-réseau, les adresses (1) et (3) ci-dessus appartiennent-elles au même réseau ?

![Ces adresses ont-elles le même ID de réseau étant donné un masque de sous-réseau de 24 bits ? (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465436680/ca71584d-53dc-4116-a109-d32c11e997ef.png align="center")

Oui, elles le font, car elles ont toutes les deux les trois octets les plus significatifs identiques – réseau `42.31.93`.

![Masque de sous-réseau de 24 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465461745/c01f5958-f675-45c5-bc41-de857483e25d.png align="center")

Et les adresses (1) et (2) ?

![Ces adresses ont-elles le même ID de réseau étant donné un masque de sous-réseau de 24 bits ? (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465532664/a0ef8f73-27d5-4488-98a9-1dbeaf457797.png align="center")

Étant donné ce préfixe de réseau, elles n'appartiennent pas au même réseau. La première adresse appartient au réseau `42.31.93`, et la deuxième adresse appartient au réseau `42.31.1`.

![Masque de sous-réseau de 24 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465498737/6d4cb056-126a-422f-94bc-4392a996869c.png align="center")

### Préfixes non alignés sur les octets

Les préfixes de réseau n'ont pas besoin d'être alignés sur `8` bits, ou des octets complets. Supposons que vous avez un préfixe de réseau de `14` bits. Comment le convertiriez-vous en masque de sous-réseau ?

Eh bien, le premier octet est clair : vous avez `8` bits activés, donc le premier octet est `255`. Et le suivant ?

En binaire, vous voudriez avoir six `1` supplémentaires, puis deux `0` – donc en binaire vous écririez :

```plaintext
11111100
```

En convertissant en décimal, ce nombre binaire représente `252`. Donc votre masque de sous-réseau est :

```plaintext
255.252.0.0
```

Une autre façon de faire cette conversion : Vous savez que huit `1` en binaire représentent `255` en décimal. Vous savez aussi que `11` en binaire est `3`, donc vous pouvez simplement soustraire `3` de `255` et obtenir `252`.

![Masque de sous-réseau de 14 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465576989/bb1a90c1-1563-4970-b0f5-e0f502e82563.png align="center")

Ensuite, essayez l'autre sens. Vous avez le masque de sous-réseau suivant :

```plaintext
255.255.224.0
```

Combien de bits représentent le préfixe de réseau ?

Les deux premiers octets sont clairs : vous avez `16` bits. En convertissant le troisième octet en binaire : `224` en décimal est `11100000` en binaire. Cela signifie que vous avez trois `1` supplémentaires, donc vous pouvez écrire le masque de sous-réseau ci-dessus comme un préfixe de `/19` bits – `16` bits pour les deux octets `255`, et `3` bits supplémentaires pour l'octet `224`.

![Masque de sous-réseau de 19 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465642118/2587e3bc-0c88-48a9-b876-b96fd3a493d1.png align="center")

### Déterminer l'appartenance au réseau

Considérons les adresses suivantes :

![Deux adresses IP (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465744667/86337750-0f67-4ed7-b8c2-7d6fcf330a71.png align="center")

Font-elles partie du même réseau ? 🤔

Cela dépend du masque de sous-réseau.

Si le préfixe de réseau est `/8`, alors elles font partie du même réseau, car elles partagent le même ID de réseau.

![Masque de sous-réseau de 8 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465761356/67c590e1-daf5-4276-96ff-a39ee914d2d3.png align="center")

D'un autre côté, si le préfixe de réseau est `/16`, alors elles ont des ID de réseau différents, et donc n'appartiennent pas au même réseau. Mais que se passe-t-il avec les préfixes intermédiaires ? Résideront-elles dans le même réseau pour un préfixe de `/9` ? `/14` ?

La façon d'aborder cette question est de convertir le deuxième octet de ces adresses en binaire. Pour la première adresse, cet octet est `24`, qui en binaire est :

```plaintext
00011000
```

Pour la deuxième adresse, le deuxième octet est `23`, qui en binaire est :

```plaintext
00010111
```

![Masque de sous-réseau de 12 bits (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465797029/fcbc4bd8-e273-4032-afb3-f10e2028738b.png align="center")

Vous pouvez voir que les `4` bits les plus significatifs dans le deuxième octet sont identiques. Si vous ajoutez les `8` premiers bits de l'adresse, vous voyez que les `12` bits les plus significatifs de ces adresses sont les mêmes.

Donc, si vous avez un préfixe de réseau de `/11`, ces adresses appartiennent-elles au même réseau ?

Oui, elles le font – leurs `11` bits les plus significatifs sont identiques.

Et `/13` ?

Non, avec ce préfixe de réseau, elles ne partagent pas le même identifiant de réseau, car leur `13`ème bit est différent.

Cette pratique devrait vous aider à vous sentir à l'aise avec les masques de sous-réseau et les préfixes de réseau. Dans la section suivante, vous apprendrez les adresses IP spéciales puis examinerez l'en-tête des paquets IP.

## Adresses IPv4 spéciales

Maintenant que vous êtes à l'aise avec les adresses IP et les masques de sous-réseau, explorons certaines adresses IP qui ont des significations spéciales.

### L'adresse "Cet hôte" : 0.0.0.0

L'adresse `0.0.0.0` signifie "cet hôte" et est utilisée dans deux scénarios :

Premièrement, lorsqu'une machine démarre et n'a pas encore d'adresse IP. Les adresses IP sont des adresses logiques qui doivent être attribuées à une machine. Avant cette attribution, un appareil n'a aucune adresse IP. Si l'appareil doit communiquer à ce stade, il peut utiliser cette adresse spéciale, `0.0.0.0`.

Deuxièmement, lors de l'écriture d'applications réseau qui doivent écouter les connexions entrantes sur toutes les interfaces réseau. Par exemple, si une machine a deux interfaces – l'une avec l'adresse IP `1.1.1.1`, et une autre avec l'adresse `2.2.2.2` – écouter sur l'adresse `0.0.0.0` signifie accepter les connexions indépendamment de l'interface réseau qui les reçoit.

### Adresses "Ce réseau"

Une autre classe d'adresses spéciales sont celles commençant par des zéros, où les zéros signifient "ce réseau".

Par exemple, si vous avez une machine avec l'adresse :

```plaintext
12.34.55.55
```

Et un préfixe de réseau de `16` bits, cette machine peut envoyer un paquet à un autre appareil sur le réseau en utilisant son adresse complète, par exemple `12.34.66.66`, ou alternativement utiliser la notation spéciale des zéros et envoyer le paquet à :

```plaintext
0.0.66.66
```

Cela signifie "envoyer un paquet à l'hôte `66.66` sur ce réseau". Bien sûr, le destinataire doit également connaître le préfixe de réseau pertinent pour interpréter correctement cette adresse.

### Adresses de diffusion

L'adresse `255.255.255.255`, où tous les bits sont définis sur `1`, est l'adresse de tous les hôtes du réseau local – l'adresse de diffusion. Cela est similaire à [l'adresse de diffusion dans Ethernet](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/#heading-unicast-and-multicast-bits) (`FF:FF:FF:FF:FF:FF`). Dans les deux cas, tous les bits sont définis sur `1`.

L'utilisation d'un identifiant de réseau approprié où l'identifiant d'hôte est entièrement défini sur des `1` peut être utilisée pour envoyer un paquet de diffusion à des réseaux distants. Par exemple, considérons un réseau `12.34.0.0/16` et un autre réseau avec l'ID de réseau `12.35.0.0/16`. Si une machine à `12.34.55.55` veut envoyer un paquet à tous les appareils de l'autre réseau, elle pourrait utiliser l'adresse de destination : `12.35.255.255`.

Bien que cela soit autorisé selon la spécification IP (RFC), en pratique, cette fonctionnalité est souvent désactivée car elle peut créer des vulnérabilités de sécurité.

### Adresses de boucle locale : 127.0.0.0/8

Toutes les adresses du réseau `127.0.0.0/8` (c'est-à-dire toutes les adresses qui commencent par `127`) sont des adresses de boucle locale. Les paquets envoyés à l'une de ces adresses ne sont pas mis sur le réseau physique mais sont traités localement au sein du système d'exploitation. Cela est extrêmement utile pour le développement et le débogage.

Par exemple, lors du développement d'un simple programme de chat, vous avez besoin de deux clients qui échangent des données. Une approche serait d'utiliser deux ordinateurs physiques différents, mais cela est fastidieux – vous devriez écrire un message sur un ordinateur, vérifier l'autre ordinateur pour voir s'il a été reçu, puis écrire un message sur le deuxième ordinateur, et revenir au premier pour valider la réception.

Une approche beaucoup plus simple est d'utiliser une adresse de boucle locale. Les deux clients peuvent s'exécuter sur la même machine et se connecter l'un à l'autre. Vous pouvez exécuter deux programmes clients différents sur le même ordinateur physique et échanger des messages entre eux sans avoir besoin d'une machine supplémentaire.

Par exemple, vous pourriez utiliser l'adresse `127.0.0.1`, avec un client écoutant sur le port `1337` et l'autre sur le port `1338`. Lorsque le client A envoie un paquet au client B, ce paquet ne quitte jamais votre carte réseau mais reste au sein du système d'exploitation. Le client B reçoit le paquet de l'interface de boucle locale comme s'il avait été reçu du réseau physique.

Après le débogage, votre code client n'a pas besoin d'être modifié – la seule différence est qu'ils communiqueront en utilisant de vraies adresses IP au lieu de l'adresse de boucle locale.

![Fonctionnement de la boucle locale (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1744736895494/fd1e4a8d-a834-4bf4-b4b9-1e83cf851161.png align="center")

### Résumé des adresses IPv4 spéciales

Pour résumer les adresses IPv4 spéciales que vous avez apprises :

| Adresse spéciale | Signification | Utilisation |
| --- | --- | --- |
| `0.0.0.0` | "Cet hôte" | Utilisé pendant le démarrage ou pour écouter sur toutes les interfaces |
| Adresses commençant par `0` | "Ce réseau" | Envoyer à des hôtes sur le réseau local |
| `255.255.255.255` | Diffusion | Envoyer à tous les hôtes sur le réseau local |
| ID de réseau avec tous les 1 dans la partie hôte | Diffusion dirigée | Envoyer à tous les hôtes sur un réseau spécifique |
| `127.0.0.0/8` | Boucle locale | Test et débogage sans utiliser le réseau physique |

Dans la section suivante, vous apprendrez la structure de l'en-tête IPv4.

## En-tête IPv4

Maintenant que vous comprenez les adresses IP, les sous-réseaux et les adresses spéciales, il est temps d'examiner en détail la structure de l'en-tête IPv4.

### La structure de l'en-tête

![En-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745583720695/21521520-3029-4a0a-b4e7-fa484ca350ab.png align="center")

Le diagramme ci-dessus montre l'en-tête de IPv4 tel que défini dans le RFC 791. Examinons chaque champ :

#### Version (4 bits)

![Champ Version dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745589954987/cb357d49-73ab-43e6-93b5-c2b7c7e3eb4a.png align="center")

L'en-tête commence par le champ Version, qui se compose de quatre bits. Pour un paquet IPv4, la version est `4`, donc ce champ portera toujours la valeur `4` (ou `0100` en binaire).

❓ Pourquoi l'en-tête commence-t-il par le champ Version ? 🤔

(Note – lorsque je commence une phrase par le symbole ❓ – c'est une question qui vous est adressée, et je vous encourage à essayer d'y répondre avant de continuer la lecture).

La raison est que les champs restants peuvent différer selon la version. Si un appareil réseau lit un paquet IP et que le champ de version porte la valeur `4`, il s'attendra à ce que le reste du paquet suive la structure IPv4. Si elle porte une autre valeur, comme `6`, les champs restants sont différents, comme dans IPv6.

#### Longueur de l'en-tête Internet (IHL) (4 bits)

![Champ IHL dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745590070221/ca452338-299c-422c-aef4-8fe8569dd218.png align="center")

Ce champ indique la longueur de l'en-tête lui-même.

❓ Pourquoi devons-nous spécifier la longueur ? 🤔

Contrairement à [Ethernet](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), où la taille de l'en-tête est fixe, la longueur de l'en-tête IPv4 peut varier en raison des champs optionnels. Pour un paquet IP sans options spéciales, l'en-tête se compose de `20` octets, ce qui est le cas le plus courant.

Le champ IHL ne spécifie pas la longueur en octets directement mais en unités de mots de 4 octets. Donc pour spécifier une longueur de `20` octets, la valeur serait `5` (5 × 4 = 20). Ce codage permet au champ d'utiliser seulement 4 bits tout en spécifiant des longueurs d'en-tête jusqu'à `60` octets (quand IHL = `15`).

Un paquet IPv4 courant commence donc par l'octet `0x45` en hexadécimal, ce qui signifie qu'il s'agit de la version `4` du protocole IP, et que l'en-tête fait `20` octets de long.

#### Type de service (TOS) (8 bits)

![Champ TOS dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745590323255/e8a30561-bfbf-4bcd-a07c-3dbce88fc6c4.png align="center")

L'idée derrière ce champ est que tous les paquets ne sont pas également importants. Vous pouvez vouloir donner la priorité à certains paquets par rapport à d'autres.

Par exemple, les paquets transportant des données en temps réel (comme la voix ou la visioconférence) sont plus sensibles au temps que les paquets transportant, par exemple, des e-mails ou des téléchargements de fichiers. Si un routeur est actuellement surchargé, il devrait idéalement prioriser les paquets sensibles au temps.

Le champ Type de service permet aux expéditeurs d'indiquer la priorité de leurs paquets. Cependant, sur l'Internet public, ce champ est souvent ignoré par les routeurs car tout expéditeur peut définir n'importe quelle valeur de priorité. Dans la plupart des cas, ce champ porte la valeur `0`.

#### Longueur totale (16 bits)

![Champ Longueur totale dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745590421285/07a4b428-3a97-4ea8-9006-5fd8bb215d95.png align="center")

Ce champ spécifie la longueur totale du paquet IP, y compris l'en-tête et la charge utile (données).

❓ Pourquoi est-il nécessaire de spécifier la longueur ? 🤔

Malheureusement, la couche IP ne sait pas nécessairement si certains des octets dans le paquet sont en fait un remplissage de la deuxième couche. J'ai décrit cela en détail dans [un article précédent](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/#heading-the-problem-with-the-type-length-field), où j'ai montré que dans le protocole Ethernet, dans certains cas, [l'entité Ethernet réceptrice ne peut pas distinguer les octets qui appartiennent à la charge utile et ceux qui sont simplement du remplissage](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/#heading-the-problem-with-the-type-length-field). La couche IP doit savoir précisément quels octets appartiennent au paquet réel, d'où le champ Longueur totale.

❓ Quelle est la taille maximale d'un paquet IPv4 ? 🤔

Étant donné que ce champ fait `16` bits de long, un paquet IPv4 peut contenir un maximum de 2^16-1 octets, soit `65,535` octets, y compris l'en-tête. La taille minimale est de `20` octets, composée uniquement de l'en-tête sans options ni charge utile.

#### Champs de fragmentation (32 bits)

![Champs de fragmentation dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591136348/bb1035af-c967-4bb8-992c-c10e31b64cd1.png align="center")

Les quatre prochains octets sont dédiés au contrôle de la fragmentation. Je couvrirai ces champs dans une section séparée, car ils impliquent un sujet complexe méritant une attention spéciale.

#### Temps de vie (8 bits)

![Champ TTL dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591194176/3f3f98f6-b079-43d3-9ee3-b052b7f4f6d7.png align="center")

Malgré son nom, ce champ ne mesure pas réellement le temps mais plutôt le nombre maximum de sauts de routage qu'un paquet peut traverser avant d'être rejeté.

Pour comprendre son but, considérons ce scénario : Si la Machine A envoie un paquet à la Machine B à travers une série de routeurs, mais qu'il y a une boucle de routage où le Routeur 2 envoie au Routeur 3, qui envoie au Routeur 4, qui renvoie au Routeur 2, le paquet pourrait circuler indéfiniment, consommant de la bande passante et n'atteignant jamais sa destination.

![Un problème de routage causant une boucle infinie (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745775904428/72ba07f9-461d-483f-be16-773218d8f863.png align="center")

Le champ TTL empêche cela en fixant une limite au nombre de sauts qu'un paquet peut effectuer :

1. L'expéditeur définit une valeur TTL initiale (souvent `64` ou `128`)

2. Chaque routeur qui traite le paquet décrémente le TTL de `1`

3. Si un routeur reçoit un paquet avec TTL = `1`, il le décrémente à `0` et rejette le paquet

4. Le routeur envoie ensuite un message ICMP "Time Exceeded" à l'expéditeur d'origine

Cela ne résout pas le problème sous-jacent des boucles de routage, mais cela empêche les paquets de circuler éternellement.

Dans IPv6, ce champ est renommé "Hop Limit", ce qui décrit plus précisément sa fonction.

#### Protocole (8 bits)

![Champ Protocole dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591243041/ab9be6ea-5f11-4bb1-b93f-f0d9deef0c6f.png align="center")

Ce champ décrit la charge utile du paquet IPv4. Par exemple :

* Une valeur de `6` signifie que la charge utile est TCP

* Une valeur de `17` signifie que la charge utile est UDP

Cela aide le système récepteur à savoir quel gestionnaire de protocole doit traiter le contenu du paquet. C'est similaire au [champ Type dans Ethernet](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/#heading-type-length-field-ethernet-ii-type-2-bytes), qui spécifie le protocole de la couche encapsulée dans la trame Ethernet.

#### Somme de contrôle de l'en-tête (16 bits)

![Champ Somme de contrôle de l'en-tête dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591295127/9953fb34-2b2f-4c9f-bf39-7a18ceaf2b1a.png align="center")

Il s'agit d'une somme de contrôle de 16 bits utilisée pour vérifier la validité de l'en-tête uniquement (c'est-à-dire en excluant la charge utile). L'expéditeur calcule cette valeur en fonction des champs de l'en-tête, et le récepteur la calcule également pour valider que l'en-tête a été reçu correctement.

❓ La somme de contrôle doit être recalculée par chaque routeur. Pourquoi ? 🤔

Parce que le champ TTL change à chaque saut. Par exemple, si un paquet commence avec TTL = `7`, chaque routeur va :

1. Vérifier la somme de contrôle actuelle basée sur TTL = `7`

2. Décrémenter TTL à `6`

3. Calculer une nouvelle somme de contrôle basée sur TTL = `6`

4. Transférer le paquet avec la nouvelle somme de contrôle

Si la vérification de la somme de contrôle échoue, l'appareil abandonne le paquet. Cela empêche les paquets avec des en-têtes corrompus (qui pourraient avoir des adresses de destination incorrectes, par exemple) d'être transférés.

#### Adresses source et de destination (32 bits chacune)

![Champs Adresses source et de destination dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591643443/b2409ba4-d2e3-468a-af2a-a71fc4ce4c30.png align="center")

Ces champs contiennent les adresses IPv4 source et de destination, respectivement. Chacun fait 4 octets (32 bits) de long, comme vous l'avez appris dans les sections précédentes sur l'adressage IPv4.

#### Options (Longueur variable)

![Options dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591747762/66a3d602-4379-453a-b221-b4f694c3363c.png align="center")

La plupart des paquets IPv4 n'incluent pas d'options, mais lorsqu'elles sont présentes, elles peuvent fournir des fonctionnalités supplémentaires :

* **Enregistrement de route** : Chaque routeur qui traite le paquet ajoute sa propre adresse à cette option, créant une trace du chemin du paquet

* **Routage source** : Permet à l'expéditeur de spécifier la route que le paquet doit suivre :

  * Routage source strict : L'ensemble de la route doit être suivi exactement

  * Routage source lâche : Certains routeurs doivent être traversés, mais le chemin exact entre eux est flexible

#### Remplissage

Dans certains cas, l'en-tête se termine par des octets de remplissage (généralement des `0`).

❓ Pourquoi l'en-tête IPv4 a-t-il un remplissage ? 🤔

Comme expliqué précédemment, le champ IHL spécifie la longueur de l'en-tête en unités de 4 octets, donc la longueur totale de l'en-tête doit être un multiple de 4 octets. Si les options rendent la longueur de l'en-tête non divisible par 4, des octets de remplissage (généralement `0`) sont ajoutés pour atteindre le multiple suivant de 4.

Par exemple, si vous avez 3 octets d'options, vous auriez besoin de 1 octet de remplissage pour rendre la longueur totale de l'en-tête un multiple de 4 octets.

### En-tête IPv4 – Résumé intermédiaire

Vous avez maintenant appris la structure de l'en-tête IPv4, à l'exception des champs de fragmentation que je couvrirai dans la section suivante.

L'en-tête IPv4 regroupe efficacement toutes les informations de routage et de contrôle nécessaires dans une structure compacte, généralement de 20 octets de long (sans options). Cette conception permet un traitement rapide par les routeurs tout en offrant la flexibilité nécessaire pour la communication Internet. Il est incroyable de voir à quel point IPv4 est prépondérant, même après tant d'années depuis sa publication.

Dans la section suivante, vous apprendrez la fragmentation IPv4.

## Fragmentation IPv4

Dans la section précédente, vous avez appris la plupart de la structure de l'en-tête IPv4, à l'exception de 32 bits dédiés à la fragmentation. Ce sujet mérite une attention spéciale, car il révèle des aspects importants de la manière dont les paquets IP voyagent à travers différents réseaux.

![Champs de fragmentation dans l'en-tête IPv4 (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745591136348/bb1035af-c967-4bb8-992c-c10e31b64cd1.png align="center")

### Pourquoi la fragmentation est nécessaire

Pour comprendre ce qu'est la fragmentation et pourquoi elle est nécessaire, considérons le scénario réseau suivant :

![Deux réseaux avec des MTU différents (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745770107962/b3bc6c7a-2adb-4868-893c-ec9e51303567.png align="center")

Dans ce diagramme, vous avez deux réseaux différents où la Machine A réside dans un réseau et la Machine B réside dans un autre. Un routeur transmet les paquets entre ces deux réseaux.

Ces deux réseaux ont des unités de transmission maximale (MTU) différentes. Le MTU fait référence à la taille maximale d'une trame qui peut être transmise dans un réseau. Par exemple :

* La Machine B est connectée à un réseau Ethernet avec un MTU de `1500` octets

* La Machine A est connectée à un réseau différent avec un MTU de `2000` octets

Les MTU différents proviennent des différents protocoles et matériels que les différents réseaux ont. Ethernet a un MTU de `1500` octets. Cette taille maximale a été choisie car la RAM était chère à la fin des années 1970 lorsque Ethernet était planifié, et un récepteur aurait besoin de plus de RAM si une trame pouvait être plus grande. D'autres réseaux ont été conçus à différentes époques où les prix de la RAM pouvaient être plus bas, ou ont simplement d'autres considérations qui affectent le MTU.

Maintenant, considérons ce scénario : la Machine A veut envoyer un paquet à la Machine B. Ce paquet fait `1800` octets de long. Du point de vue de A, il n'y a pas de problème puisque son réseau supporte les paquets de cette taille. La Machine A transmet le paquet.

Lorsque le routeur reçoit ce paquet, il est confronté à un problème : il ne peut pas simplement transmettre le paquet au réseau de B car le paquet est trop grand pour le MTU du réseau. Le routeur doit **fragmenter** le paquet – le diviser en morceaux plus petits de jusqu'à `1500` octets, qui seront ensuite réassemblés par la Machine B.

### Comment fonctionne la fragmentation dans IP

Examinons le scénario plus en détail. Le routeur doit prendre un paquet IP de `1800` octets et le diviser en deux fragments, chacun composé de jusqu'à `1500` octets. Si la Machine A envoie un autre paquet de `1800` octets à la Machine B, le routeur devra également le diviser – résultant en quatre fragments différents qui seront réassemblés en deux paquets séparés.

![Deux paquets IP, chacun composé de deux fragments (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745770316245/b137efa8-ae1c-42cb-918a-f6d0ee7b2c3a.png align="center")

Lorsque la Machine B reçoit ces fragments, elle doit s'assurer qu'elle réassemble le fragment #1 avec le fragment #2 du paquet A, et le fragment #1 avec le fragment #2 du paquet B – et non, par exemple, le fragment #1 du paquet A avec le fragment #2 du paquet B. Elle doit également réassembler les fragments dans le bon ordre – pour structurer un paquet qui se compose de #1#2 et non de #2#1.

![Problèmes possibles dans le réassemblage des paquets à partir de deux fragments (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745770377464/12aad8f1-0251-4289-bc9a-75084dbc1f7a.png align="center")

### Champ d'identification

Tout d'abord, concentrons-nous sur le fait de s'assurer que la Machine B réassemble les fragments du même paquet (par exemple, le fragment #1 et le fragment #2 du paquet A dans l'exemple ci-dessus, plutôt que le fragment #1 du paquet A et le fragment #2 du paquet B). Cela est réalisé en utilisant le champ d'identification de IPv4. Les fragments appartenant au même paquet auront la même valeur d'identification. Par exemple, les deux fragments du paquet A pourraient avoir l'identification définie sur `100`, et les deux fragments du paquet B pourraient avoir l'identification `200`.

![Le champ d'identification garantit que les fragments du même paquet original sont réassemblés ensemble (Source : https://youtube.com/BriefVid)](https://cdn.hashnode.com/res/hashnode/image/upload/v1745770785114/6f04e59b-adfc-44a9-bf6e-1118ab748160.png align="center")

Il est important de noter que le partage des valeurs d'identification n'est pas suffisant pour que les fragments appartiennent au même paquet. Les fragments du même paquet doivent également partager :

* La même adresse IP source

* La même adresse IP de destination

* La même valeur de protocole (indiquant si la charge utile est TCP, UDP, etc.)

### Décalage de fragment

Étant donné que IP est un protocole sans connexion, il n'y a aucune garantie que les fragments arriveront à la Machine B dans le bon ordre. Le fragment #2 du paquet A peut arriver avant le fragment #1. Pour gérer ce problème, chaque fragment transporte un champ Offset, qui indique le décalage depuis le début du paquet original.

Le champ Offset se compose de 13 bits, ce qui signifie qu'il peut porter des valeurs de `0` à `8191` (2^13-1). Cela pose un problème potentiel, car la taille maximale d'un paquet IP peut être de `65,535` octets (puisque le champ Total Length de l'en-tête IP se compose de 16 bits).

Pour résoudre cette limitation, la valeur encodée dans le champ Offset est en fait multipliée par `8` (2^3). Cela signifie que la taille minimale d'un fragment est de `8` octets, à l'exception du dernier fragment.

❓ Pourquoi les paquets IP transportent-ils un décalage en octets divisé par 8, au lieu d'un simple numéro de fragment séquentiel ? 🤔

Bien que l'utilisation de numéros de séquence puisse sembler plus simple, cela créerait des problèmes lorsque les paquets doivent être fragmentés plusieurs fois.

Par exemple, si l'ordinateur A envoie un paquet au premier routeur, qui le fragmente en morceaux de `1480` octets et `320` octets, puis ces fragments sont envoyés à un autre routeur qui doit les fragmenter à nouveau en morceaux encore plus petits, comment les numéroteriez-vous ?

Avec les décalages d'octets, la solution est simple – si le premier fragment a un décalage de `0` et le suivant a un décalage de `1480`, alors si nous devons les diviser en fragments de `800` octets maximum, nous aurions :

* Premier fragment : `800` octets avec un décalage de `0`

* Deuxième fragment : `680` octets avec un décalage de `800`

* Troisième fragment : `320` octets avec un décalage de `1480`

### Indicateurs Plus de fragments et Ne pas fragmenter

Lorsque la Machine B reçoit un fragment, elle doit savoir si celui-ci est un paquet entier en soi ou si elle doit s'attendre à des fragments supplémentaires. À cette fin, chaque fragment IP transporte un bit Plus de fragments (`MF`) qui est défini sur `1` pour chaque fragment qui n'est pas le dernier fragment du paquet. Pour le dernier fragment, il est défini sur `0`.

Dans le cas où le paquet se compose d'un seul fragment – le bit `MF` sera défini sur `0`, et le champ de décalage contiendra également la valeur `0` (c'est-à-dire 13 bits de `0`).

Un autre bit lié à la fragmentation est le bit Ne pas fragmenter (`DF`). Lorsque ce drapeau est activé, les appareils intermédiaires ne doivent pas fragmenter le paquet original, même s'il dépasse le MTU. Au lieu de cela, ils doivent le rejeter et généralement envoyer un message ICMP "Fragmentation nécessaire" à la source.

Dans notre exemple, si la Machine A définit le bit Ne pas fragmenter sur `1`, le routeur rejetterait le paquet et en informerait la Machine A.

Notez qu'immédiatement après le champ d'identification et avant le drapeau `DF`, il y a un bit réservé défini sur `0`. Ce bit a été réservé au cas où il serait nécessaire à l'avenir, pour une raison inconnue des auteurs originaux de IPv4.

### Exemple de fragmentation

Considérons à nouveau notre exemple ci-dessus – avec la Machine A résidant dans un réseau où le MTU est `2000`, et la Machine B résidant dans un réseau où le MTU est `1500`. La Machine A envoie un paquet qui fait `1800` octets de long.

❓ Pouvez-vous remplir les valeurs dans ces tableaux ?

**Premier fragment :**

| Longueur totale | |
| --- | --- |
| Identification | |
| Ne pas fragmenter | |
| Plus de fragments | |
| Décalage | |

**Deuxième fragment :**

| Longueur totale | |
| --- | --- |
| Identification | |
| Ne pas fragmenter | |
| Plus de fragments | |
| Décalage | |

Pour notre exemple ci-dessus, les valeurs des champs de fragmentation pertinents dans IP seraient les suivantes :

**Premier fragment :**

* Longueur totale : `1500` (y compris `20` octets d'en-tête IP, donc `1480` octets de charge utile)

* Identification : `1337` (valeur arbitraire)

* Bit Ne pas fragmenter : `0` (désactivé, pour permettre une fragmentation supplémentaire si nécessaire)

* Bit Plus de fragments : `1` (activé, car ce n'est pas le dernier fragment)

* Décalage : `0` (c'est le premier fragment)

**Deuxième fragment :**

* Longueur totale : `340` (y compris `20` octets d'en-tête IP, donc `320` octets de charge utile – avec le premier fragment, nous obtenons `1800` octets de charge utile)

* Identification : `1337` (même que le premier fragment, indiquant qu'ils appartiennent ensemble)

* Bit Ne pas fragmenter : `0` (désactivé, pour permettre une fragmentation supplémentaire si nécessaire)

* Bit Plus de fragments : `0` (désactivé, car c'est le dernier fragment)

* Décalage : `185` (1480/8 = 185, ou `0xB9` en hexadécimal)

### Fragmentation IPv4 – Résumé

Vous avez maintenant appris la dernière partie de l'en-tête IPv4 : la fragmentation. La fragmentation est nécessaire pour permettre aux paquets de voyager à travers des réseaux avec différents MTU. L'en-tête IPv4 inclut plusieurs champs spécifiquement conçus pour supporter la fragmentation :

* Identification (16 bits) : Identifie les fragments qui appartiennent ensemble

* Drapeaux (3 bits) : Incluant les indicateurs "Plus de fragments" et "Ne pas fragmenter"

* Décalage de fragment (13 bits) : Indique où dans le paquet original ce fragment appartient

Avec cette connaissance, vous comprenez maintenant chaque bit et octet de l'en-tête IPv4 et comment les paquets IP peuvent traverser des réseaux avec différentes caractéristiques.

## Résumé – IPv4

Dans ce guide complet sur IPv4, vous avez appris les éléments fondamentaux des communications Internet. Récapitulons les concepts clés que nous avons couverts :

### Adressage et structure du réseau

* Les adresses IPv4 sont des nombres de 32 bits généralement écrits en notation décimale pointée

* Les réseaux peuvent être identifiés en utilisant diverses méthodes :

  * Approche à longueur fixe (historiquement)

  * Adressage par classes (classes A, B, C, D, E)

  * CIDR (approche moderne permettant des tailles de réseau flexibles)

* Les adresses spéciales servent des objectifs spécifiques :

  * `0.0.0.0` pour "cet hôte"

  * `127.0.0.0/8` pour la boucle locale

  * `255.255.255.255` pour la diffusion

### Structure de l'en-tête IPv4

* L'en-tête contient des champs cruciaux pour le routage et le traitement des paquets :

  * Version et IHL pour l'interprétation de l'en-tête

  * Type de service pour la priorisation du trafic

  * Longueur totale pour la taille du paquet

  * Divers champs pour le contrôle de la fragmentation

  * TTL pour prévenir les boucles de routage infinies

  * Protocole pour identifier le protocole encapsulé

  * Somme de contrôle pour la détection d'erreurs

  * Adresses source et de destination

### Fragmentation

* Permet aux paquets IPv4 de traverser des réseaux avec différents MTU

* Utilise trois champs clés :

  * Identification pour regrouper les fragments

  * Drapeaux pour contrôler la fragmentation

  * Décalage de fragment pour réassembler les paquets

### Mots finaux

Bien que IPv4 ait des limitations, en particulier ses contraintes d'espace d'adressage, sa conception élégante et ses fonctionnalités robustes lui ont permis de rester l'épine dorsale de l'Internet pendant plus de quatre décennies. Comprendre IPv4 fournit un contexte essentiel pour travailler avec les réseaux modernes et aide à la transition vers de nouveaux protocoles comme IPv6.

## **À propos de l'auteur**

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne YouTube [Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Gitting Things Done](https://www.freecodecamp.org/news/gitting-things-done-book/) (en anglais) et [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

### **Références supplémentaires**

* [Liste de lecture Réseaux informatiques - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)