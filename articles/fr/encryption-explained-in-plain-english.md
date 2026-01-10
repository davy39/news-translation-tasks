---
title: Chiffrement à clé symétrique et asymétrique – Expliqué en français simple
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-04-05T20:09:48.000Z'
originalURL: https://freecodecamp.org/news/encryption-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: Chiffrement à clé symétrique et asymétrique – Expliqué en français simple
seo_desc: 'Encryption is a way of scrambling data so that it can only be read by the
  intended recipient.

  Encryption is an integral part of our daily lives – whether you are sending messages
  to friends on WhatsApp, visiting a website and your browser is making s...'
---

Le chiffrement est une méthode de brouillage des données afin qu'elles ne puissent être lues que par le destinataire prévu.

Le chiffrement fait partie intégrante de notre vie quotidienne, que ce soit pour envoyer des messages à des amis sur WhatsApp, visiter un site web et vérifier son authenticité, ou entrer vos coordonnées bancaires lors d'un achat en ligne. Le chiffrement protège vos données des regards potentiellement malveillants et indiscrets.

Cet article abordera :

* Les algorithmes et clés de chiffrement
  
* Le chiffrement à clé symétrique et asymétrique
  
* Comment le TLS/SSL utilise à la fois le chiffrement symétrique et asymétrique
  

## Algorithmes et clés de chiffrement

Au début de cet article, j'ai décrit le chiffrement comme une méthode de brouillage des données afin qu'elles ne puissent être lues que par le destinataire prévu. Décomposons ce que cela signifie.

Imaginons que vous souhaitiez écrire une lettre à un ami et que vous souhaitiez vous assurer que seul l'ami peut lire son contenu. Comment empêcher les regards indiscrets de tous les intermédiaires par lesquels la lettre pourrait passer avant d'arriver à votre ami ? C'est-à-dire, comment empêcher le facteur, le concierge de leur immeuble, ou l'un de leurs amis de lire la lettre ?

Vous commencez avec une lettre non brouillée que tout le monde peut lire. Cela s'appelle le **texte en clair**. Pour brouiller le contenu du message, vous avez besoin d'un **algorithme de chiffrement** et d'une **clé**. L'algorithme de chiffrement utilise la clé pour brouiller le contenu du message. Ce message chiffré est appelé **texte chiffré**.

Le processus de chiffrement est illustré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-9.png align="left")

Lorsque votre ami reçoit le message, il devra le déchiffrer en utilisant l'**algorithme** et la **clé**. Cela est illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-10.png align="left")

Les deux ingrédients clés nécessaires pour envoyer un message à votre ami, que seul lui peut lire, sont un **algorithme de chiffrement** et une **clé**.

L'algorithme de chiffrement est simplement une formule mathématique conçue pour brouiller les données, tandis que la clé est utilisée comme partie de la formule. L'algorithme de chiffrement est générique, mais la clé, utilisée comme entrée de l'algorithme, est ce qui garantit l'unicité des données brouillées.

Examinons l'un des algorithmes de chiffrement les plus simples, appelé le Chiffre de César. Dans sa forme la plus simple, cet algorithme remplace simplement chaque lettre par la lettre suivante de l'alphabet. Ainsi, A devient B, et B devient C, et ainsi de suite.

Avec cet algorithme, le texte 'Anniversaire Surprise' devient 'Bojwfstbqj Tvsqtjtf', indéchiffrable pour l'œil non averti.

Avec l'exemple du Chiffre de César, l'**algorithme** est la formule utilisée pour remplacer chaque lettre de l'alphabet par une autre. La **clé** est le nombre de décalages effectués entre chaque lettre. Avec une clé de 0, A est A, un choix de clé évidemment mauvais car les données ne sont pas brouillées. Avec une clé de 1, A devient B. Avec une clé de 10, A devient K.

Le Chiffre de César est un algorithme de chiffrement relativement faible. Pourquoi ? Puisqu'il n'y a que 26 lettres dans la langue anglaise, vous ne pouvez produire qu'un maximum de 25 textes chiffrés possibles. Si vous n'avez pas la clé, vous devez simplement décaler chaque lettre jusqu'à 25 fois jusqu'à ce que vous voyiez des mots et des phrases cohérents, moment auquel vous savez que vous avez réussi à déchiffrer le message.

Un mauvais algorithme de chiffrement est celui qui peut être facilement déchiffré en utilisant une petite quantité de force brute (c'est-à-dire, en essayant toutes les permutations possibles) – et 25 textes chiffrés possibles est un nombre objectivement petit d'options à parcourir.

Les algorithmes de chiffrement modernes comme AES-256, utilisés par AWS, GCP et Azure pour chiffrer les données, sont considérablement plus compliqués et sécurisés que le Chiffre de César. Sur la base des capacités informatiques actuelles, il faudrait des billions et des billions d'années au supercalculateur le plus avancé pour utiliser la force brute afin de déchiffrer les données chiffrées avec AES-256 \[[1](https://scrambox.com/article/brute-force-aes/)\]. Même l'univers n'est pas aussi ancien.

## Chiffrement à clé symétrique et asymétrique

Le cœur de tout processus de chiffrement est l'algorithme de chiffrement et la clé. Il existe de nombreux types d'algorithmes de chiffrement. Mais il existe, en général, deux types de clés – les clés symétriques et asymétriques.

Dans le chiffrement à clé symétrique, la même clé utilisée pour chiffrer les données est utilisée pour les déchiffrer. Dans le chiffrement à clé asymétrique, une clé est utilisée pour chiffrer les données (la clé publique) et une autre clé est utilisée pour les déchiffrer (la clé privée).

### Chiffrement à clé asymétrique

Tout d'abord, examinons le chiffrement à clé asymétrique avec une simple analogie.

Imaginez que vous souhaitiez envoyer quelque chose à votre ami, mais qu'il était absolument essentiel que personne d'autre, à part votre ami, ne puisse avoir accès à cet objet. Votre ami achète donc une boîte indestructible, fabriquée dans le métal le plus résistant de la planète, et vous l'envoie afin que vous puissiez y placer l'objet. Votre ami vous envoie également la clé qui ne peut être utilisée que pour verrouiller la boîte.

Maintenant, cette boîte a une autre propriété spéciale. Elle a deux trous de serrure. Un trou de serrure pour ouvrir la boîte, un autre pour la verrouiller.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-11.png align="left")

Naturellement, cette boîte aura également besoin de deux clés – une pour l'ouvrir et une autre pour la verrouiller.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-12.png align="left")

Les deux clés sont similaires, mais pas identiques. Comme vous pouvez le voir dans l'image ci-dessus, par exemple, la clé utilisée pour ouvrir la boîte a deux dents tandis que la clé utilisée pour verrouiller la boîte en a trois.

En tant qu'expéditeur de l'objet, vous n'avez que la boîte pour y placer l'objet et une clé pour verrouiller la boîte. Seul votre ami a la clé qui peut déverrouiller la boîte.

La clé utilisée pour verrouiller la boîte est appelée la clé publique, et ne peut pas être utilisée pour l'ouvrir, car cela nécessite la clé privée. Si quelqu'un interceptait le colis et faisait une copie de la clé publique, il ne pourrait pas l'utiliser pour ouvrir la boîte, seulement pour la verrouiller. Seule la personne qui détient la clé privée peut ouvrir la boîte.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-13.png align="left")

Le chiffrement à clé asymétrique est utilisé lorsqu'il y a deux ou plusieurs parties impliquées dans le transfert de données. Ce type de chiffrement est utilisé pour chiffrer les données en transit, c'est-à-dire chiffrer les données envoyées entre deux ou plusieurs systèmes. L'exemple le plus populaire de chiffrement à clé asymétrique est [RSA](https://nordvpn.com/blog/rsa-encryption/).

### Chiffrement à clé symétrique

Le chiffrement à clé symétrique utilise la même clé pour le chiffrement et le déchiffrement. Cela rend le partage de la clé difficile, car toute personne qui intercepte le message et voit la clé peut alors déchiffrer vos données.

C'est pourquoi le chiffrement à clé symétrique est généralement utilisé pour chiffrer les données au repos. AES-256 est l'algorithme de chiffrement à clé symétrique le plus populaire. Il est utilisé par AWS pour chiffrer les données stockées sur les disques durs (volumes EBS) et les compartiments S3. GCP et Azure l'utilisent également pour chiffrer les données au repos.

## Comment le TLS/SSL utilise à la fois le chiffrement symétrique et asymétrique

La principale force du chiffrement à clé symétrique est qu'il est plus facile et plus rapide de chiffrer et de déchiffrer les données en utilisant une seule clé, tout comme il est plus facile de construire une boîte avec une seule serrure et une seule clé.

La faiblesse du chiffrement à clé symétrique est que si la clé est exposée, vos données ne sont plus chiffrées de manière sécurisée. Ainsi, si vous deviez partager la clé avec une partie externe, il y a un risque que la clé soit exposée, laissant vos données à risque d'être déchiffrées.

Le chiffrement à clé symétrique est idéal pour chiffrer les données au repos, où vous n'avez pas besoin de partager la clé avec un autre système.

Avec le chiffrement asymétrique, ce n'est pas un problème puisque deux clés séparées sont utilisées – la clé publique pour chiffrer les données et la clé privée pour les déchiffrer.

La clé publique peut être facilement partagée avec n'importe qui et ne pose aucun risque pour le déchiffrement de vos données, puisque la clé privée est nécessaire pour le déchiffrement.

L'inconvénient du chiffrement à clé asymétrique est que le processus de chiffrement et de déchiffrement est plus lent et plus compliqué. Le chiffrement à clé asymétrique est idéal pour chiffrer les données en transit, où vous devez partager la clé avec un autre système.

Et s'il existait un moyen d'obtenir la vitesse et la simplicité computationnelle du chiffrement symétrique sans augmenter le risque d'exposer vos clés ?

Le chiffrement TLS/SSL utilise à la fois des clés symétriques et asymétriques pour chiffrer les données en transit, et est utilisé avec le protocole HTTP pour des communications sécurisées sur un réseau informatique.

### Explication du chiffrement TLS/SSL

TSL (Transport Layer Security) et SSL (Secure Sockets Layer) sont souvent utilisés de manière interchangeable pour signifier la même chose. Mais lorsque les gens disent SSL, ils veulent souvent dire TLS.

TLS est généralement considéré comme plus sécurisé que SSL grâce à plusieurs améliorations apportées au protocole, telles que des algorithmes cryptographiques plus robustes. En raison des préoccupations de sécurité avec SSL, la plupart des navigateurs web et applications modernes ont abandonné le support de SSL et ne supportent que TLS. Par conséquent, TLS est devenu la norme pour la communication sécurisée sur Internet.

### Comment utiliser le chiffrement symétrique et asymétrique en même temps

Imaginons que vous souhaitiez envoyer un colis de manière sécurisée à votre ami. Mais vous ne voulez pas continuer à utiliser la boîte indestructible spéciale qui a deux trous de serrure et deux verrous. Elle est chère, lourde et peu pratique pour des communications fréquentes. Vous voulez toujours utiliser une boîte indestructible, mais une plus simple, avec un seul verrou et une seule clé.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-14.png align="left")

Cependant, si vous utilisez une boîte avec un seul verrou et une seule clé, vous devez maintenant trouver comment partager la clé de cette boîte plus simple avec votre ami de manière sécurisée.

Puisque la même clé est utilisée pour ouvrir et verrouiller la boîte, vous ne pouvez pas simplement envoyer la clé à votre ami sans la protéger d'une manière ou d'une autre au préalable. Si la clé est interceptée et qu'une copie est prise par quelqu'un, ils peuvent maintenant ouvrir votre boîte et prendre ce qu'il y a à l'intérieur.

Comment pouvez-vous partager cette clé avec votre ami de manière sécurisée afin de pouvoir utiliser cette boîte plus simple pour les communications futures ?

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-15.png align="left")

1. Tout d'abord, votre ami envoie la boîte avec les deux verrous plus la clé publique utilisée pour la verrouiller. Mais vous ne voulez pas continuer à utiliser cette boîte. Vous ne l'utiliserez qu'une seule fois – pour transférer la clé d'une autre boîte plus simple que vous utiliserez pour les échanges futurs.
   
2. Vous placez la clé principale qui sera utilisée dans les échanges futurs à l'intérieur de cette boîte et la verrouillez avec la clé publique envoyée par votre ami.
   
3. Vous envoyez la boîte verrouillée qui contient une copie de la clé principale à l'intérieur à votre ami.
   
4. Votre ami utilise sa clé privée pour ouvrir la boîte. Maintenant, vous avez tous les deux la clé principale et pouvez être sûr que personne d'autre ne l'a puisque elle a été envoyée dans une boîte sécurisée.
   
5. Tous les articles futurs sont ensuite placés dans cette boîte plus simple avec un seul verrou et une seule clé qui peut être ouverte et verrouillée en utilisant la clé principale que vous venez d'envoyer à votre ami.
   

### Séquence de chiffrement TLS/SSL

L'analogie de la section précédente correspond bien à la manière dont le chiffrement TLS/SSL fonctionne réellement. Mais il y a quelques étapes préalables que j'ai ignorées dans cette analogie, comme la création d'une connexion TCP et l'envoi du certificat du serveur (étapes 1 et 2 ci-dessous).

De plus, l'étape 6 est une simplification du processus. En réalité, la clé principale est utilisée pour générer un ensemble supplémentaire de clés que le client et le serveur utiliseront pour chiffrer et déchiffrer les messages et également pour authentifier que les messages ont bien été envoyés par le client et le serveur.

Pour en savoir plus sur les détails de bas niveau, je recommande le chapitre 8 de "[Computer Networking](https://www.amazon.co.uk/Computer-Networking-Global-James-Kurose/dp/1292405465/ref=sr_1_1?keywords=computer+networking+a+top-down+approach&qid=1680219419&sprefix=computer+netw%2Caps%2C168&sr=8-1)" par Kurose & Ross.

Mais, à un niveau élevé, la séquence est la suivante :

1. Le client établit une connexion TCP avec le serveur
   
2. Le client vérifie que le serveur est bien celui qu'il prétend être – le serveur envoie un certificat qui contient la clé publique. La clé privée associée reste avec le serveur.
   
3. Le client crée une clé secrète principale et utilise la clé publique du serveur pour la chiffrer. Cette clé secrète principale est une clé symétrique, donc la même clé est utilisée pour le chiffrement et le déchiffrement.
   
4. Le client envoie la clé secrète principale chiffrée au serveur.
   
5. Le serveur déchiffre la clé principale chiffrée en utilisant sa clé privée.
   
6. Tous les messages futurs entre le client et le serveur utilisent désormais la clé symétrique principale pour chiffrer et déchiffrer les messages.
   

## Le meilleur des deux mondes

L'utilisation à la fois du chiffrement à clé symétrique et asymétrique vous offre la vitesse du chiffrement à clé symétrique sans compromettre la sécurité supplémentaire fournie par le chiffrement à clé asymétrique.

Mais rien n'est gratuit, bien sûr. Avec TLS, il y a une couche supplémentaire de complexité puisque vous devez d'abord utiliser des clés asymétriques pour établir une connexion sécurisée avant d'échanger la clé symétrique pour les communications futures.

Ainsi, en utilisant à la fois le chiffrement symétrique et asymétrique, TLS/SSL obtient le meilleur des deux mondes avec des inconvénients limités.