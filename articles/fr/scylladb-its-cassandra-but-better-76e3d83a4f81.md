---
title: ScyllaDB est meilleur que Cassandra, et voici pourquoi.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T16:07:39.000Z'
originalURL: https://freecodecamp.org/news/scylladb-its-cassandra-but-better-76e3d83a4f81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yRMqqIGUndAm3sJbqIIq1g.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: ScyllaDB est meilleur que Cassandra, et voici pourquoi.
seo_desc: 'By Kartik Khare

  ScyllaDB is one of the newest NoSQL database which offers really high throughput
  at sub millisecond latencies. The important point is that it accomplishes this at
  a fraction of the cost of a modern NoSQL database.

  ScyllaDB implements ...'
---

Par Kartik Khare

[ScyllaDB](https://www.scylladb.com/) est l'une des plus récentes bases de données NoSQL qui offre un débit très élevé avec des latences inférieures à la milliseconde. Le point important est qu'elle y parvient à une fraction du coût d'une base de données NoSQL moderne.

ScyllaDB implémente presque toutes les fonctionnalités de [Cassandra](http://cassandra.apache.org/) en C++. Mais dire qu'il s'agit d'un simple portage en C++ serait une sous-estimation. Les développeurs de Scylla ont apporté de nombreuses modifications sous le capot qui ne sont pas visibles pour l'utilisateur mais qui conduisent à une énorme amélioration des performances.

### Vous plaisantez, n'est-ce pas ?

Non, [je ne plaisante pas](https://www.scylladb.com/product/benchmarks/aws-c3-2xlarge-benchmark/).

Comme vous pouvez le voir (si vous avez cliqué sur ce lien), dans la plupart des cas, la latence au 99,9e percentile de Scylla est 5 à 10 fois meilleure que celle de Cassandra.

De plus, dans les benchmarks mentionnés [ici](https://www.scylladb.com/product/benchmarks/ycsb-cluster-benchmark/), un cluster Scylla standard de 3 nœuds offre presque les mêmes performances qu'un cluster Cassandra de 30 nœuds (ce qui conduit à une réduction des coûts de 10 fois).

### Comment cela est-il possible ?

Le point le plus important est que Scylla est écrit en C++14. Il est donc normal qu'il soit plus rapide que Cassandra, qui fonctionne uniquement sur la JVM.

Cependant, de nombreuses optimisations significatives de bas niveau ont été apportées à Scylla, ce qui le rend meilleur que ses concurrents.

### Approche Shared-Nothing

Cassandra repose sur des threads pour le parallélisme. Le problème est que les threads nécessitent un changement de contexte, ce qui est lent.

De plus, pour la communication entre les threads, vous devez verrouiller la mémoire partagée, ce qui entraîne à nouveau une perte de temps de traitement.

ScyllaDB utilise le [framework seastar](http://www.seastar-project.org/) pour répartir les requêtes sur chaque cœur. L'application n'a qu'un seul thread par cœur. Ainsi, si une session est gérée par le cœur 1 et qu'une requête pour cette session arrive sur le cœur 2, elle est dirigée vers le cœur 1 pour traitement. N'importe quel cœur peut ensuite gérer la réponse.

L'avantage de l'approche shared-nothing est que chaque thread dispose de sa propre mémoire, CPU et files d'attente de tampons NIC.

Dans les cas où la communication entre les cœurs ne peut pas être évitée, Seastar offre une communication inter-cœurs asynchrone et sans verrou, hautement scalable. Ces primitives sans verrou incluent les Futures et les Promises, qui sont assez couramment utilisées en programmation et donc conviviales pour les développeurs.

### Éviter le noyau

Lorsqu'une ligne est trouvée dans un SSTable, elle doit être envoyée via le réseau au client. Cela implique de copier les données de l'espace utilisateur vers l'espace noyau.

Cependant, le noyau Linux effectue généralement des opérations de verrouillage multithread qui ne sont pas scalables.

ScyllaDB résout ce problème en utilisant la pile réseau de Seastar.

La pile réseau de Seastar fonctionne dans l'espace utilisateur et utilise [DPDK](https://dpdk.org/) pour un traitement plus rapide des paquets. DPDK contourne le noyau pour copier les données directement dans le tampon NIC et traite un paquet en 80 cycles CPU. (source : [Site Web DPDK](https://dpdk.org/))

### Ne pas compter sur le Page Cache

Le Page Cache est idéal lorsque vous avez des E/S séquentielles et que les données sont stockées sur le disque au format filaire.

Cependant, dans Scylla/Cassandra, nous avons des données sous forme de SSTables. Le Page Cache stocke les données dans le même format, ce qui occupe une grande partie de la mémoire pour de petites données et nécessite une sérialisation/désérialisation lorsque vous souhaitez les transférer.

ScyllaDB, au lieu de compter sur le Page Cache, alloue la majeure partie de sa mémoire au row-cache.

Le Row-Cache contient les données dans un format mémoire optimisé qui occupe moins d'espace et ne nécessite pas de sérialisation/désérialisation.

Un autre avantage de l'utilisation du row cache est qu'il n'est pas supprimé lors de la compaction, contrairement au page cache qui est écrasé.

Ce sont les principales optimisations de ScyllaDB qui le rendent beaucoup plus rapide, plus fiable et moins cher que Cassandra. Scylla possède de nombreuses autres optimisations sous le capot que vous pouvez trouver [ici](https://www.scylladb.com/product/).

**_Si vous êtes curieux d'en savoir plus sur des conceptions comme celles ci-dessus ou si vous souhaitez entrer en contact, connectez-vous avec moi sur [LinkedIn](http://www.linkedin.com/in/kartik-khare) ou [Facebook](https://www.facebook.com/KK.corps) ou envoyez un email à [kharekartik@gmail.com](mailto:kharekartik@gmail.com)_**