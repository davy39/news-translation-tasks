---
title: Comment utiliser Scapy – Outil de réseau Python expliqué
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-12-21T21:02:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-scapy-python-networking
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Computer-Networks-Hub-Switch--1-.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Python
  slug: python
seo_title: Comment utiliser Scapy – Outil de réseau Python expliqué
seo_desc: "In this post you will learn about an amazing tool named Scapy. Scapy is\
  \ a Python library that enables us to send, sniff, and dissect network frames. \n\
  It is useful in a variety of use cases, one of which is to actually get some hands-on\
  \ experience whe..."
---

Dans cet article, vous apprendrez à utiliser un outil incroyable nommé **Scapy**. Scapy est une bibliothèque Python qui nous permet d'envoyer, de capturer et de dissecter des trames réseau.

Elle est utile dans une variété de cas d'utilisation, notamment pour obtenir une expérience pratique lors de l'apprentissage des réseaux informatiques. Ne serait-ce pas génial si, par exemple, en [apprenant sur Ethernet](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), vous pouviez créer, envoyer, capturer et analyser des trames Ethernet par vous-même ? Scapy est l'outil parfait pour cela.

De plus, vous pouvez utiliser Scapy pour créer des applications basées sur le réseau, analyser le trafic réseau pour examiner les données, et bien d'autres cas.

Cet article suppose que vous avez quelques connaissances de base en réseaux informatiques, par exemple sur [le modèle en couches](https://www.freecodecamp.org/news/the-five-layers-model-explained/). Il suppose également que vous avez quelques connaissances de base en Python.

# Qu'allez-vous apprendre ?

Dans cet article, nous commencerons par les bases – qu'est-ce que Scapy et comment l'installer.

Vous apprendrez comment capturer des données et les analyser avec Scapy, et comment les afficher de manière significative.

Vous apprendrez également comment créer des trames ou des paquets, et comment les envoyer. Ensemble, vous devriez avoir un nouvel outil puissant à votre disposition.

# Comment installer Scapy

Pour installer Scapy, vous pouvez simplement utiliser `pip install scapy`.

Si vous rencontrez des problèmes, suivez simplement [la documentation officielle](https://scapy.readthedocs.io/en/latest/installation.html).

# Comment utiliser Scapy

Pour l'instant, ouvrons la ligne de commande et tapons **`scapy`**.

Vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-83.png)
_Exécution de Scapy depuis la CLI (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Notez que les messages d'avertissement sont normaux.

Puisque c'est un environnement Python, _dir_, _help_, et toute autre fonction Python pour la récupération d'informations sont disponibles pour vous. Bien sûr, vous pouvez toujours combiner du code Python avec vos scripts Scapy.

# Comment travailler avec des paquets et des trames dans Scapy

Les paquets et les trames dans Scapy sont décrits par des objets créés en empilant différentes couches. Ainsi, un paquet peut avoir un nombre variable de couches, mais décrira toujours la séquence d'octets qui ont été envoyés (ou qui vont être envoyés) sur le réseau.

Créons une trame composée d'une couche Ethernet, avec une couche IP par-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-85.png)
_Empilement des couches (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Regardez comme c'est facile ! Nous avons utilisé l'opérateur `/` afin d'empiler la couche IP par-dessus la couche Ethernet.

Notez que lorsque nous regardons cet objet, il ne nous indique que les valeurs non par défaut. Le type d'Ethernet est `0x800` (en base hexadécimale) car c'est le type lorsqu'une couche IP est surchargée.

Examinons plus en détail les champs du paquet :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-86.png)
_Avec la méthode `show`, nous pouvons observer tous les champs de la trame (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Plutôt cool ! 😊

# Comment capturer avec Scapy

Scapy nous permet également de capturer le réseau en exécutant la commande **sniff**, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-87.png)
_Capture avec la commande `sniff` (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Après avoir exécuté `sniff` avec `count=2`, Scapy capture votre réseau jusqu'à ce que `2` trames soient reçues. Ensuite, il retourne – et dans ce cas, la variable `packets` stockera les trames qui ont été reçues.

La valeur de retour de sniff peut être traitée comme une liste. Par conséquent, `packets[0]` contiendra le premier paquet reçu, et `packets[1]` contiendra le second :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-88.png)
_La valeur de retour de `sniff` est itérable, donc elle peut être accédée comme une liste (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Une fonction d'aide `summary` est également disponible et fournira des informations minimales concernant la collection de paquets :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-89.png)
_En utilisant `summary`, nous pouvons obtenir quelques informations sur la collection de paquets (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Lorsque nous regardons une trame spécifique, chaque couche ou champ peut être accédé de manière très élégante. Par exemple, afin d'obtenir la section **IP** du paquet, nous pouvons y accéder comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-90.png)
_Accès à une couche spécifique (et sa charge utile) (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Notez que cela nous montre tout à partir de la couche IP et au-dessus (c'est-à-dire, la charge utile de la couche IP). Observons maintenant l'adresse Ethernet source de cette trame :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-91.png)
_Accès à un champ spécifique (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_


Bien et facile. Maintenant, vous allez apprendre à exécuter une commande spécifique pour chaque trame que vous capturez.

Tout d'abord, créez la fonction de rappel qui sera exécutée sur chaque paquet. Par exemple, une fonction qui imprimera simplement l'adresse Ethernet source de la trame reçue :


![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-92.png)
_Définition d'une fonction de rappel qui reçoit une trame comme argument (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Maintenant, nous pouvons passer cette fonction à `sniff`, en utilisant l'argument `prn` :


![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-93.png)
_Exécution d'une fonction de rappel sur chaque trame capturée (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Les adresses Ethernet ont été imprimées à la suite de l'exécution de `print_source_ethernet`, où chaque fois, elle reçoit une trame capturée comme argument.
Notez que vous pouvez écrire la même chose en Python en utilisant une fonction lambda, comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-94.png)
_Définition de la fonction de rappel en utilisant `lambda` (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Si vous préférez écrire une fonction explicite comme celle que nous avons écrite ci-dessus, c'est parfaitement acceptable.

Nous voulons généralement **filtrer** le trafic que nous recevons – et ne regarder que les trames pertinentes. La fonction `sniff` de Scapy peut prendre une fonction de filtre comme argument – c'est-à-dire, une fonction qui sera exécutée sur chaque trame, et retournera une valeur `booléenne` – si cette trame est filtrée ou non.

Par exemple, supposons que nous souhaitons filtrer uniquement les trames qui sont envoyées en diffusion. Écrivons une simple fonction de filtrage qui fait exactement cela :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-95.png)
_Une simple fonction de filtrage (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Maintenant, nous pouvons utiliser le paramètre `lfilter` de `sniff` afin de filtrer les trames pertinentes :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-96.png)
_Filtrage des trames basé sur une fonction de filtre (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Afin de clarifier, dessinons ce processus :


![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-97.png)
_Le processus de capture et de filtrage avec `lfilter` (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_


Une trame `f` est reçue par la carte réseau. Elle est ensuite transférée à `lfilter(f)`. Si la fonction de filtre retourne `False`, `f` est rejetée. Si le filtre retourne `True`, alors nous exécutons la fonction `prn` sur `f`.

Nous pouvons donc maintenant combiner ces deux arguments de `sniff`, à savoir `lfilter` et `prn`, et imprimer l'adresse source de chaque trame qui est envoyée à l'adresse de diffusion. Faisons cela maintenant en utilisant `lambda` :


![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-98.png)
_Combinaison de `lfilter` et `prn` 🚪🏽 (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Cela équivaut à écrire la ligne suivante, sans lambda :

```py
sniff(count=2, lfilter=is_broadcast_frame, prn=print_source_ethernet)
```

Lisible, rapide et utile. Avez-vous remarqué que j'aime Scapy ? 🤩

D'accord, jusqu'à présent nous avons appris à capturer des trames. Lors de la capture, nous savons comment filtrer uniquement les trames pertinentes, et comment exécuter une fonction sur chaque trame filtrée.

# Comment créer des trames dans Scapy

Pour créer une trame, il suffit de créer une couche Ethernet en utilisant `Ether()`. Ensuite, empilez des couches supplémentaires par-dessus. Par exemple, pour empiler une couche `IP` :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-99.png)
_Création d'une trame avec deux couches empilées (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Alternativement, nous pouvons simplement ajouter des données brutes, comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-100.png)
_Utilisation de données brutes comme charge utile (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Si vous souhaitez spécifier une valeur spécifique, par exemple l'adresse de destination de la trame, vous pouvez le faire lors de la création initiale de la trame, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-101.png)
_Création d'une trame et spécification de valeurs spécifiques (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Ou, nous pouvons modifier le champ spécifique après la création :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-102.png)
_Modification de valeurs spécifiques (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Comment pouvons-nous regarder la trame que nous venons de créer ? Une façon est d'observer une trame en utilisant `show`, comme nous l'avons fait ci-dessus. Une autre façon de regarder une trame est de regarder son flux d'octets, comme dans Wireshark. Vous pouvez le faire en utilisant la fonction `hexdump` :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-103.png)
_Affichage du flux d'octets hexadécimal (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Eh bien, encore mieux – nous pouvons simplement la regarder dans Wireshark ! En exécutant `wireshark(frame)`.

# Comment envoyer des trames dans Scapy

Vous pouvez envoyer des trames en utilisant `sendp`, comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-104.png)
_Envoi de trames avec `sendp` (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Observons dans Wireshark tout en envoyant la trame pour nous assurer qu'elle est effectivement envoyée :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-105.png)
_Observation de la trame que nous avons envoyée en utilisant Wireshark (Source : [Brief](https://www.youtube.com/watch?v=f0vpwwNAcdI&ab_channel=Brief))_

Notez que nous utilisons `sendp` uniquement lorsque nous envoyons une trame entière, en utilisant la deuxième couche et au-dessus. Si vous souhaitez envoyer un paquet incluant uniquement la troisième couche et au-dessus, utilisez `send` à la place.

# Récapitulatif

Dans cet article, vous avez découvert un outil incroyable appelé Scapy. Vous avez vu comment vous pouvez capturer, comment filtrer les paquets, et comment exécuter une fonction sur les paquets capturés. Vous avez également appris comment créer et envoyer des trames.

## À propos de l'auteur

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne Brief [YouTube Channel](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

## **Ressources supplémentaires**

* [Liste de lecture sur les réseaux informatiques - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)
* [Documentation officielle de Scapy](https://scapy.readthedocs.io/en/latest/)