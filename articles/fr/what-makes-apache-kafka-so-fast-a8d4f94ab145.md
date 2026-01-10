---
title: Voici ce qui rend Apache Kafka si rapide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T19:50:39.000Z'
originalURL: https://freecodecamp.org/news/what-makes-apache-kafka-so-fast-a8d4f94ab145
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P6PWPLZ7vv1LzN2jo1lNvA.png
tags:
- name: big data
  slug: big-data
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici ce qui rend Apache Kafka si rapide
seo_desc: 'By Kartik Khare

  What is Apache Kafka?

  Apache Kafka is a distributed streaming platform, which allows you to:


  Publish and subscribe to streams of records, similar to a message queue or enterprise
  messaging system.

  Store streams of records in a fault-...'
---

Par Kartik Khare

#### Qu'est-ce qu'Apache Kafka ?

[Apache Kafka](https://kafka.apache.org/) est une plateforme de streaming distribuée, qui permet de :

* Publier et s'abonner à des flux d'enregistrements, similaire à une file d'attente de messages ou un système de messagerie d'entreprise.
* Stocker des flux d'enregistrements de manière tolérante aux pannes et durable.
* Traiter des flux d'enregistrements au fur et à mesure qu'ils se produisent.

Si vous n'avez jamais utilisé Kafka auparavant, vous pouvez vous rendre ici pour un [démarrage rapide](https://kafka.apache.org/quickstart) et revenir à cet article une fois que vous serez familiarisé avec le cas d'utilisation.

Kafka supporte une plateforme hautement distribuée, tolérante aux pannes, avec un débit élevé et une livraison de messages à faible latence. Ici, nous allons nous concentrer sur l'aspect de livraison à faible latence.

#### Faible latence en I/O = Système de fichiers ?

La plupart des systèmes de données traditionnels utilisent la mémoire vive (RAM) comme stockage de données, car la RAM offre des latences extrêmement faibles.

Bien que cette approche les rende rapides, le coût de la RAM est bien plus élevé que celui du disque. De tels systèmes sont généralement plus coûteux à exécuter lorsque vous avez des centaines de Go de données circulant dans le système.

Kafka s'appuie sur le système de fichiers pour le stockage et la mise en cache. Le problème est que les disques sont plus lents que la RAM. Cela est dû au fait que le temps de recherche sur un disque est grand par rapport au temps nécessaire pour lire les données.

Mais si vous pouvez éviter la recherche, alors vous pouvez atteindre des latences aussi faibles que la RAM dans certains cas. Cela est réalisé par Kafka grâce à l'**I/O séquentiel**.

Un avantage de l'I/O séquentiel est que vous obtenez un cache sans écrire de logique dans votre application pour cela. Les systèmes d'exploitation modernes allouent la plupart de leur mémoire libre à la mise en cache du disque. Ainsi, si vous lisez de manière ordonnée, le système d'exploitation peut toujours lire à l'avance et stocker les données dans un cache à chaque lecture de disque.

Cela est bien meilleur que de maintenir un cache dans une application JVM. Cela est dû au fait que les objets JVM sont "lourds" et peuvent entraîner une collecte de déchets élevée, ce qui devient pire à mesure que la taille des données augmente.

#### N'utilisez pas d'arbres

La plupart des bases de données modernes utilisent une forme ou une autre de [structure de données en arbre](https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c) pour le stockage de données persistant. Par exemple, MongoDB utilise [BTree](https://en.wikipedia.org/wiki/B-tree), tandis que Cassandra utilise [LSM tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree).

Ces structures fournissent une [performance de recherche O(log N)](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/).

Pour un système de messagerie qui nécessite de nombreuses opérations de lecture et d'écriture à effectuer simultanément, l'utilisation d'arbres peut entraîner beaucoup d'I/O aléatoires. Cela entraîne de nombreuses recherches sur disque, ce qui est désastreux pour les performances.

Une [file d'attente](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) est une structure de données bien meilleure pour un système de messagerie. La plupart du temps, les données sont ajoutées au système, et les lectures sont simples. Toutes ces opérations sont O(1), ce qui est beaucoup plus performant.

#### Ne copiez pas !

L'une des principales inefficacités des systèmes de traitement de données est la [sérialisation et la désérialisation](https://en.wikipedia.org/wiki/Serialization) (traduction dans des formats adaptés au stockage et à la transmission) des données lors des transferts.

Cela peut être rendu plus rapide en utilisant de meilleurs formats de données binaires, tels que les protocoles buffers ou les Flat buffers, au lieu de JSON.

Mais comment éviter complètement la sérialisation/désérialisation ?

Kafka aborde cela de deux manières :

1. Utiliser un format de données binaire standardisé pour les [producteurs, brokers et consommateurs](https://kafka.apache.org/documentation/#api) (afin que les données puissent être transmises sans modification)
2. Ne pas copier les données dans l'application ("zero-copy")

Le premier point est explicite. C'est le second qui nécessite de l'attention.

Un transfert de données courant d'un fichier à une socket peut se dérouler comme suit :

1. Le système d'exploitation lit les données du disque dans le pagecache dans l'espace noyau
2. L'application lit les données de l'espace noyau dans un tampon en espace utilisateur
3. L'application écrit les données dans l'espace noyau dans un tampon de socket
4. Le système d'exploitation copie les données du tampon de socket vers le tampon NIC, où elles sont envoyées sur le réseau

Cependant, si nous avons le même format standardisé pour les données qui ne nécessite pas de modification, alors nous n'avons pas besoin de l'étape 2 (copie des données de l'espace noyau vers l'espace utilisateur).

Si nous gardons les données dans le même format qu'elles seront envoyées sur le réseau, alors nous pouvons copier directement les données du pagecache vers le tampon NIC. Cela peut être fait via un appel système [sendfile](http://man7.org/linux/man-pages/man2/sendfile.2.html) du système d'exploitation.

Plus de détails sur l'approche zero-copy peuvent être trouvés dans cet [article](https://www.ibm.com/developerworks/linux/library/j-zerocopy/).

#### Qu'y a-t-il d'autre ?

Kafka utilise de nombreuses autres techniques en plus de celles mentionnées ci-dessus pour rendre les systèmes beaucoup plus rapides et efficaces :

1. Regroupement des données pour réduire les appels réseau, et également convertir de nombreuses écritures aléatoires en écritures séquentielles.
2. Compression des lots (et non des messages individuels) en utilisant les codecs [LZ4](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm)), [SNAPPY](https://en.wikipedia.org/wiki/Snappy_(compression)) ou [GZIP](https://en.wikipedia.org/wiki/Gzip). Beaucoup de données sont cohérentes entre les messages d'un lot (par exemple, les champs de message et les informations de métadonnées). Cela peut conduire à de meilleurs taux de compression.

Pour en savoir plus sur la conception de Kafka, vous pouvez vous référer à leur [article officiel](https://kafka.apache.org/0102/documentation.html#majordesignelements).

Il est important de noter que toutes les techniques mentionnées ci-dessus peuvent être appliquées dans la plupart des systèmes pour obtenir des latences faibles. Elles n'impliquent pas de manipuler le noyau, de régler la collecte des déchets, d'utiliser des applications natives ou d'utiliser des structures de données extrêmes.

Un inconvénient, cependant, est que certaines de ces techniques sont spécifiques à des cas similaires à une plateforme de messagerie. Elles ne seraient pas adaptées à une base de données distribuée plus générale.

**_Si vous êtes curieux d'en savoir plus sur des conceptions comme celle-ci ou si vous avez une opportunité, connectez-vous avec moi sur [LinkedIn](http://www.linkedin.com/in/kartik-khare) ou [Facebook](https://www.facebook.com/KK.corps) ou envoyez un mail à [kharekartik@gmail.com](mailto:kharekartik@gmail.com)_**