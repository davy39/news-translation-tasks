---
title: Définition du chiffrement – Qu'est-ce qu'un chiffrement par blocs et comment
  fonctionne-t-il pour protéger vos données ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-03T16:21:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-block-cipher
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/block-and-stream-cipher.jpg
tags:
- name: ciphers
  slug: ciphers
- name: Cryptography
  slug: cryptography
- name: cybersecurity
  slug: cybersecurity
seo_title: Définition du chiffrement – Qu'est-ce qu'un chiffrement par blocs et comment
  fonctionne-t-il pour protéger vos données ?
seo_desc: 'By Megan Kaczanowski

  Cryptography is the science of using codes and ciphers to protect messages. And
  encryption involves encoding messages so that only the intended recipient can understand
  the meaning of the message. It''s often used to protect data ...'
---

Par Megan Kaczanowski

La cryptographie est la science de l'utilisation de codes et de chiffrements pour protéger les messages. Et le chiffrement implique de coder les messages de sorte que seul le destinataire prévu puisse comprendre le sens du message. Il est souvent utilisé pour protéger les données en transit.

Le chiffrement est une fonction à double sens – c'est-à-dire que vous devez pouvoir annuler tout brouillage que vous avez fait au message. 

Aujourd'hui, il existe deux types de base d'algorithmes – asymétriques et symétriques. 

Les algorithmes symétriques sont également connus sous le nom d'algorithmes à 'clé secrète', et les algorithmes asymétriques sont connus sous le nom d'algorithmes à 'clé publique'. 

La différence clé entre les deux est que les algorithmes symétriques utilisent la même clé pour le chiffrement et le déchiffrement, tandis que les algorithmes asymétriques utilisent des clés différentes pour le chiffrement et le déchiffrement. 

Pour un aperçu général de la cryptographie et de la différence entre les chiffrements symétriques et asymétriques, consultez [cet article](https://www.freecodecamp.org/news/how-to-send-secret-messages/). 

## Quels principes sont importants lors du développement d'un chiffrement ?

Le principe de Kerckhoff stipule qu'un système cryptographique doit être sécurisé, même si tous les détails (autres que la clé) sont connus publiquement. Claude Shannon a plus tard réécrit ce message comme 'L'ennemi connaît le système.' 

Essentiellement, un système très bien conçu devrait être capable d'envoyer des messages secrets même si un attaquant peut chiffrer et déchiffrer ses propres messages en utilisant le même algorithme (avec une clé différente). La sécurité du message chiffré devrait dépendre entièrement de la clé. 

De plus, afin d'entraver l'analyse statistique (tentatives de briser un algorithme de chiffrement), un bon système cryptographique devrait employer les principes de confusion et de diffusion. 

La confusion nécessite que la clé ne soit pas liée au texte chiffré de manière simple. Chaque caractère du texte chiffré devrait dépendre de plusieurs parties de la clé. Le but est de rendre très difficile pour un attaquant de déterminer la clé à partir du texte chiffré.

La diffusion signifie que si un seul caractère du texte en clair est changé, alors plusieurs caractères du texte chiffré devraient changer. Et si un seul caractère du texte chiffré est changé, alors plusieurs caractères du texte en clair devraient changer. 

Idéalement, la relation entre le texte chiffré et le texte en clair est cachée. Aucune diffusion n'est parfaite (toutes auront certains motifs), mais la meilleure diffusion disperse largement les motifs, même en brouillant plusieurs motifs ensemble. 

La diffusion rend les motifs difficiles à repérer pour un attaquant et nécessite que l'attaquant ait plus de données afin de monter une attaque réussie.

Si vous souhaitez en lire un peu plus, consultez [A Mathematical Theory of Cryptography](https://www.iacr.org/museum/shannon/shannon45.pdf).

## Qu'est-ce que les chiffrements par blocs et par flux ?

Les chiffrements par blocs et par flux sont tous deux des chiffrements à clé symétrique (comme DES, RCx, Blowfish et Rijndael AES). Les chiffrements par blocs convertissent le texte en clair en texte chiffré bloc par bloc, tandis que les chiffrements par flux convertissent un octet à la fois. 

La plupart des algorithmes symétriques modernes sont des chiffrements par blocs, bien que les tailles de bloc varient (comme DES (64 bits), AES (128, 192 et 256 bits), et ainsi de suite).

### Quel est l'avantage d'un chiffrement par flux ?

Le chiffrement par flux est plus rapide (linéaire en temps) et constant en espace. Il est peu probable de propager des erreurs, car une erreur dans la traduction d'un octet n'impactera pas l'octet suivant. 

Cependant, il y a peu de diffusion car un symbole de texte en clair est directement traduit en un symbole de texte chiffré. De plus, le texte chiffré est susceptible aux insertions ou modifications. Si un attaquant est capable de briser l'algorithme, il pourrait être en mesure d'insérer du texte qui semble authentique.

Vous utilisez généralement un chiffrement par flux lorsque la quantité de texte en clair est inconnue (comme le streaming audio ou vidéo), ou lorsque des performances extrêmes sont importantes (comme avec des connexions à très haute vitesse, ou pour des appareils qui doivent être très efficaces et compacts, comme les cartes intelligentes).

Un chiffrement par flux fonctionne en générant une série d'octets pseudo-aléatoires qui dépendent de la clé (pour une clé donnée, la série d'octets est la même pour le chiffrement et le déchiffrement). Différentes clés produiront différentes chaînes d'octets. 

Afin de chiffrer les données, les octets de texte en clair sont XORés avec la chaîne d'octets pseudo-aléatoires. Pour déchiffrer, le texte chiffré est XORé avec la même chaîne afin de voir le texte en clair.

### Quel est l'avantage d'un chiffrement par blocs ?

Un chiffrement par blocs a une diffusion élevée (les informations d'un symbole de texte en clair sont réparties dans plusieurs symboles de texte chiffré). Il est également assez difficile pour un attaquant d'insérer des symboles sans détection, car ils ne peuvent pas facilement les insérer au milieu d'un bloc.

Cependant, il est plus lent qu'un chiffrement par flux (un bloc entier doit être transmis avant que le chiffrement/déchiffrement ne puisse avoir lieu) et si une erreur se produit, elle peut se propager dans tout le bloc, corrompant toute la section.

Les chiffrements par blocs sont un meilleur choix lorsque vous connaissez la taille de la transmission – comme dans le transfert de fichiers. 

## Quels sont les modes courants des chiffrements par blocs ?

Afin de chiffrer des données qui sont plus longues qu'un seul bloc, il existe plusieurs 'modes' qui ont été développés. Ceux-ci décrivent comment appliquer les principes de bloc unique à des messages plus longs.

Il existe 5 modes de confidentialité pour les chiffrements par blocs. Certains de ces modes nécessitent un vecteur d'initialisation (IV) pour fonctionner.

### Qu'est-ce qu'un vecteur d'initialisation (IV) ?

Un IV est essentiellement une autre entrée (en plus du texte en clair et de la clé) utilisée pour créer du texte chiffré. C'est un bloc de données, utilisé par plusieurs modes de chiffrements par blocs pour randomiser le chiffrement afin que différents textes chiffrés soient créés même si le même texte en clair est chiffré à plusieurs reprises. 

Il n'a généralement pas besoin d'être secret, bien qu'il ne puisse pas être réutilisé. Idéalement, il devrait être aléatoire, imprévisible et à usage unique. 

Deux messages identiques chiffrés avec la même clé, mais avec des IV différents, donneront des textes chiffrés différents. Cela rend le travail d'un attaquant plus difficile.

### Mode Livre de Code Électronique (ECB)

Il existe une correspondance fixe entre les blocs d'entrée de texte en clair et les blocs de sortie de texte chiffré (essentiellement comme un véritable livre de code où les mots de texte chiffré sont directement liés aux mots de texte en clair). 

ECB applique la fonction de chiffrement indépendamment à chaque bloc de texte en clair pour le chiffrer (et la fonction inverse à chaque bloc de texte chiffré pour le déchiffrer). Cela signifie que CBC peut chiffrer et déchiffrer plusieurs blocs en parallèle (puisqu'ils ne dépendent pas les uns des autres), accélérant ainsi le processus. 

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-31-at-8.22.20-PM.png)
_https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation_

Pour que ce mode fonctionne correctement, soit la longueur du message doit être un multiple de la taille du bloc, soit vous devez utiliser un remplissage pour que la condition de longueur soit remplie. 

Le remplissage est essentiellement des données supplémentaires qui sont ajoutées afin de garantir que la taille du bloc est respectée. Avec ce mode, étant donné la même clé, le même bloc de texte en clair donnera toujours le même bloc de texte chiffré. Cela le rend vulnérable aux attaques, donc ce mode est rarement utilisé (et devrait être évité). 

### Mode Chaînage de Blocs de Chiffrement (CBC)

Ce mode 'chaîne' ou combine de nouveaux blocs de texte en clair avec le bloc de texte chiffré précédent lors de leur chiffrement, ce qui nécessite un IV pour le premier bloc. Le IV n'a pas besoin d'être secret, mais il doit être imprévisible.

CBC effectue un XOR (OU exclusif) du premier bloc de texte en clair avec le bloc de texte chiffré IV pour créer le premier bloc de texte chiffré. Le IV est envoyé séparément en tant que message court en utilisant le mode ECB. 

Ensuite, CBC applique l'algorithme de chiffrement au bloc, créant le premier bloc de texte chiffré. CBC effectue ensuite un XOR de ce bloc avec le deuxième bloc de texte en clair et applique l'algorithme de chiffrement pour produire le deuxième bloc de texte chiffré, et ainsi de suite jusqu'à la fin du message.

Afin de déchiffrer le message, CBC fait l'inverse - applique l'inverse de l'algorithme de chiffrement au premier bloc de texte chiffré, puis effectue un XOR du bloc avec le IV pour obtenir le premier bloc de texte en clair. 

CBC applique ensuite l'inverse de l'algorithme de chiffrement au deuxième bloc de texte chiffré et effectue un XOR du bloc avec le premier bloc de texte chiffré pour obtenir le deuxième bloc de texte en clair. Ce processus continue jusqu'à ce que le message soit déchiffré.

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-31-at-8.22.37-PM.png)
_https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation_

Parce que chaque bloc d'entrée (sauf le premier) dépend du bloc précédent étant chiffré, CBC ne peut pas effectuer le chiffrement en parallèle. Cependant, puisque le déchiffrement nécessite un XOR avec les blocs de texte chiffré (immédiatement disponibles), il peut être fait en parallèle. CBC est l'un des modes les plus couramment utilisés.

De manière similaire à ECB, pour que ce mode fonctionne correctement, soit la longueur du message doit être un multiple de la taille du bloc, soit vous devez utiliser un remplissage pour que la condition de longueur soit remplie.

### Mode Rétroaction de Chiffrement (CFB)

CFB est similaire à CBC, mais au lieu d'utiliser l'ensemble du bloc de texte chiffré précédent pour calculer le bloc suivant, CFB utilise une fraction du bloc précédent. 

CFB commence avec un IV de la même taille de bloc que celle attendue par le chiffrement par blocs, et le chiffre avec l'algorithme de chiffrement. 

CFB conserve s (significatifs) octets de cette sortie et effectue un XOR avec s octets de texte en clair à transmettre. 

Ensuite, CFB décale le IV de s octets vers la gauche, insérant les octets de texte chiffré produits par l'étape 2 comme les octets de droite (IV reste de la même longueur).

Ensuite, il répète ces étapes.

Pour déchiffrer un message, CFB utilise le IV comme premier bloc et forme chaque bloc suivant en effectuant l'étape 3 ci-dessus et en appliquant l'algorithme de chiffrement pour former des blocs. CFB effectue ensuite un XOR de s bits avec le texte chiffré correspondant pour révéler le texte en clair.

Dans CFB, le système de chiffrement traite s < b bits de texte en clair à la fois, même si l'algorithme lui-même effectue une transformation de b bits en b bits. Cela signifie que s peut être n'importe quel nombre, y compris 1 octet et CFP peut fonctionner comme un chiffrement par flux. 

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-31-at-8.24.31-PM.png)
_https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation_

Malheureusement, cela signifie que CFB peut propager des erreurs en aval. Si un octet est reçu avec une erreur, lorsque CFB l'utilise pour déchiffrer le premier octet, il produira un déchiffrement erroné, provoquant des erreurs en aval lorsqu'il est réinjecté dans le déchiffrement.

Comme CBC, lorsque CFB chiffre, l'entrée de chaque tour dépend du résultat du tour précédent, ce qui signifie que le chiffrement ne peut pas être fait en parallèle, bien que le déchiffrement puisse être effectué en parallèle si les blocs d'entrée sont d'abord créés à partir du IV et du texte chiffré.

### Rétroaction de Sortie (OFB)

OFB est similaire à CFB, mais au lieu de traiter s < b bits en une transformation de b bits en b bits, il traite s bits directement. De manière similaire à CFB, OFB peut être fonctionnellement utilisé comme un chiffrement par flux.

OFB nécessite que le IV soit un nonce unique (nombre utilisé une fois) pour chaque exécution avec une clé donnée. 

Tout d'abord, OFB chiffre le IV avec l'algorithme de chiffrement, pour produire un bloc de sortie. OFB effectue ensuite un XOR de ce bloc avec le premier bloc de texte en clair, produisant le premier bloc de texte chiffré. 

OFB chiffre le premier bloc de sortie avec l'algorithme de chiffrement pour produire le deuxième bloc de sortie. Il effectue ensuite un XOR de ce bloc avec le deuxième bloc de texte en clair pour produire le deuxième bloc de texte chiffré. OFB répète ce processus pour la longueur du message.

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-31-at-8.22.54-PM.png)
_https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation_

Lors du déchiffrement, OFB chiffre le IV avec l'algorithme de chiffrement, produisant un bloc de sortie. OFB effectue ensuite un XOR de ce bloc avec le premier bloc de texte chiffré, récupérant le premier bloc de texte en clair. 

OFB chiffre le premier bloc de sortie avec l'algorithme de chiffrement pour produire le deuxième bloc de sortie. OFB effectue ensuite un XOR avec le deuxième bloc de texte chiffré pour récupérer le deuxième bloc de texte en clair. OFB répète ce processus pour la longueur du message.

Parce que les blocs de sortie pour le déchiffrement sont générés localement, OFB est plus résistant aux erreurs de transmission que CFB.

### Compteur (CTR)

CTR applique l'algorithme de chiffrement à un ensemble de blocs d'entrée uniques (compteurs) afin de produire des sorties qui sont XORées avec le texte en clair pour produire du texte chiffré. 

CTR chiffre le premier compteur avec l'algorithme de chiffrement, puis effectue un XOR de la sortie résultante avec le premier bloc de texte en clair pour produire le premier bloc de texte chiffré. CTR répète cela pour chaque bloc (avec un nouveau compteur – les compteurs doivent être uniques pour tous les messages chiffrés utilisant une seule clé). 

Si le bloc final est un bloc partiel de s octets, les bits les plus significatifs, s, du bloc de sortie sont utilisés pour le XOR, tandis que les b - s octets du bloc de sortie sont rejetés.

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-31-at-8.23.02-PM.png)
_https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation_

Le déchiffrement suit le même schéma. CTR chiffre le compteur avec l'algorithme de chiffrement, puis effectue un XOR de la sortie avec le bloc de texte chiffré correspondant pour produire le bloc de texte en clair. 

Si le bloc final est un bloc partiel de s octets, les bits les plus significatifs, s, du bloc de sortie sont utilisés pour le XOR, tandis que les b - s octets du bloc de sortie sont rejetés.

CTR s'est avéré être au moins aussi sécurisé que les quatre autres modes, tout en pouvant être exécuté en parallèle (chiffrement et déchiffrement), ce qui signifie qu'il est très rapide. 

Chaque bloc peut être récupéré indépendamment si son bloc de compteur peut être déterminé et le chiffrement peut être appliqué aux compteurs à l'avance de la réception du texte en clair ou du texte chiffré (si la mémoire n'est pas une contrainte).

Lecture complémentaire : [Recommandation NIST pour les modes de fonctionnement des chiffrements par blocs](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf)

## Comment les attaquants tentent-ils de briser les chiffrements ?

Il existe un certain nombre de techniques utilisées par les attaquants, mais elles se répartissent généralement dans les catégories d'attaques suivantes, basées sur les informations nécessaires pour les mener à bien. 

Ce n'est pas une liste exhaustive (il existe d'autres attaques comme les attaques par canaux auxiliaires), mais beaucoup des plus courantes tombent dans l'une de ces catégories.

### Attaque à texte chiffré connu

Un attaquant dispose de certains textes chiffrés, mais ne sait pas quel texte en clair a été utilisé pour générer ce texte chiffré. L'attaquant ne peut pas choisir quel texte chiffré il possède et il ne peut pas obtenir/produire davantage. 

Il s'agit du type d'attaque le plus facile à tenter, car il est plus facile d'espionner une conversation chiffrée (en supposant que les personnes ayant la conversation utilisent un chiffrement fort et ne sont pas aussi inquiètes des écoutes). Mais c'est le plus difficile à réussir, tant que les personnes envoyant des messages utilisent un chiffrement suffisamment fort. 

_Par exemple : David trouve un message chiffré (texte chiffré) dans une [boîte aux lettres morte](https://en.wikipedia.org/wiki/Dead_drop#:~:text=A%20dead%20drop%20or%20dead,individuals%20can%20maintain%20operational%20security.), mais n'a aucune idée de ce que signifie le message._

### Attaque à texte en clair connu

Un attaquant dispose de certaines paires de texte en clair et de texte chiffré qu'il n'a pas choisies (donc l'attaquant n'a pas choisi le message qui a été chiffré, mais a réussi à voler un message en clair et son texte chiffré associé). L'attaquant ne peut pas obtenir/produire davantage de paires.

_Par exemple : David trouve une cachette d'un espion ennemi et l'interrompt alors qu'il envoie un message chiffré. L'espion est assez sot pour avoir fui, laissant à la fois le message en clair et son texte chiffré associé écrits._

### Attaque à texte en clair choisi

Un attaquant peut choisir n'importe quel texte en clair et obtenir le texte chiffré en retour (mais il ne peut pas voir la clé elle-même).

Cela est encore divisé en texte en clair choisi par lots (où l'attaquant peut soumettre un ensemble de textes en clair et recevoir le texte chiffré, mais ne peut pas le faire à nouveau) et texte en clair choisi adaptatif (où l'attaquant peut soumettre du texte en clair, recevoir le texte chiffré et soumettre du texte en clair supplémentaire basé sur le texte chiffré précédent.)

_Par exemple : Un État-nation espionne les communications chiffrées d'un autre et sait qu'ils utilisent la même clé pour tout leur chiffrement. Ils envoient une communication diplomatique sensible à l'autre État-nation, sachant qu'elle sera transmise via le canal chiffré, leur donnant ainsi une paire texte en clair - texte chiffré choisie._

### Attaque à texte chiffré choisi

C'est l'inverse de la dernière attaque, où l'attaquant peut choisir n'importe quel texte chiffré et obtenir le texte en clair en retour (mais il ne peut pas voir la clé elle-même).

_Par exemple : David sait qu'un espion ennemi va envoyer un message chiffré demain, alors il remplace le texte par son propre texte chiffré choisi, puis espionne le destinataire, écoutant alors qu'il lit le texte en clair du message._

### Sources/Lecture complémentaire :

* [Recommandations NIST pour les modes de fonctionnement des chiffrements par blocs](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf)
* [Diffusion et Confusion](https://www.nku.edu/~christensen/diffusionandconfusion)
* [Confusion et Diffusion](https://en.wikipedia.org/wiki/Confusion_and_diffusion)
* [Principe de Kerckhoffs](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle)
* [Mécanismes de Remplissage](http://www.crypto-it.net/eng/theory/padding.html)
* [Fondements de l'Informatique : Chiffrement par Flux et par Blocs](https://www.cs.utexas.edu/~byoung/cs361/lecture45.pdf)