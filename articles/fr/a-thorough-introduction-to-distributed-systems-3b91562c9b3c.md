---
title: Une introduction approfondie aux systèmes distribués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T18:44:13.000Z'
originalURL: https://freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iyQPowJqG7o492vz5kNmXw.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: distributed systems
  slug: distributed-systems
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction approfondie aux systèmes distribués
seo_desc: 'By Stanislav Kozlovski

  What is a Distributed System and why is it so complicated?

  With the ever-growing technological expansion of the world, distributed systems
  are becoming more and more widespread. They are a vast and complex field of study
  in com...'
---

Par Stanislav Kozlovski

#### Qu'est-ce qu'un système distribué et pourquoi est-il si compliqué ?

Avec l'expansion technologique toujours croissante du monde, les systèmes distribués deviennent de plus en plus répandus. Ils constituent un vaste et complexe domaine d'étude en informatique.

Cet article vise à vous introduire aux systèmes distribués de manière basique, en vous montrant un aperçu des différentes catégories de tels systèmes sans plonger profondément dans les détails.

## Qu'est-ce qu'un système distribué ?

Un système distribué, dans sa définition la plus simple, est un groupe d'ordinateurs travaillant ensemble pour apparaître comme un seul ordinateur à l'utilisateur final.

Ces machines ont un état partagé, fonctionnent de manière concurrente et peuvent tomber en panne indépendamment sans affecter le temps de fonctionnement de l'ensemble du système.

Je propose que nous travaillons progressivement à travers un exemple de distribution d'un système afin que vous puissiez mieux comprendre tout cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D_X6eX1lUYLQekx_6Uvvlw.png)
_Une pile traditionnelle_

Prenons une base de données ! Les bases de données traditionnelles sont stockées sur le système de fichiers d'une seule machine, chaque fois que vous souhaitez récupérer/insérer des informations, vous parlez directement à cette machine.

Pour distribuer ce système de base de données, nous devrions avoir cette base de données fonctionnant sur plusieurs machines en même temps. L'utilisateur doit pouvoir parler à n'importe quelle machine qu'il choisit et ne doit pas pouvoir dire qu'il ne parle pas à une seule machine — s'il insère un enregistrement dans le nœud #1, le nœud #3 doit être capable de retourner cet enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n-3Db0bssxh7B-A0Jndx0A.png)
_Une architecture qui peut être considérée comme distribuée_

## Pourquoi distribuer un système ?

Les systèmes sont toujours distribués par nécessité. La vérité est que la gestion des systèmes distribués est un sujet complexe rempli de pièges et de mines. C'est un casse-tête de déployer, maintenir et déboguer des systèmes distribués, alors pourquoi s'y aventurer ?

Ce qu'un système distribué vous permet de faire, c'est de **mettre à l'échelle horizontalement**. En revenant à notre exemple précédent du serveur de base de données unique, la seule façon de gérer plus de trafic serait de mettre à niveau le matériel sur lequel la base de données fonctionne. Cela s'appelle **la mise à l'échelle verticale**.

La mise à l'échelle verticale est bien et bonne tant que vous le pouvez, mais après un certain point, vous verrez que même le meilleur matériel n'est pas suffisant pour un trafic suffisant, sans parler de l'hébergement peu pratique.

**La mise à l'échelle horizontale** signifie simplement ajouter plus d'ordinateurs plutôt que de mettre à niveau le matériel d'un seul.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ulnsAJdpvet9EW4bKMK-Rw.png)
_La mise à l'échelle horizontale devient **beaucoup moins chère** après un certain seuil_

C'est significativement moins cher que la mise à l'échelle verticale après un certain seuil, mais ce n'est pas son principal argument de préférence.

La mise à l'échelle verticale ne peut augmenter vos performances que jusqu'aux capacités du dernier matériel. Ces capacités se révèlent **insuffisantes** pour les entreprises technologiques avec des charges de travail modérées à grandes.

Le meilleur aspect de la mise à l'échelle horizontale est que vous n'avez pas de limite sur la quantité que vous pouvez mettre à l'échelle — chaque fois que les performances se dégradent, vous ajoutez simplement une autre machine, potentiellement à l'infini.

La mise à l'échelle facile n'est pas le seul avantage que vous obtenez des systèmes distribués. La **tolérance aux pannes** et la **faible latence** sont également tout aussi importantes.

**Tolérance aux pannes** — un cluster de dix machines réparties dans deux centres de données est intrinsèquement plus tolérant aux pannes qu'une seule machine. Même si un centre de données prend feu, votre application continuerait de fonctionner.

**Faible latence** — Le temps pour qu'un paquet réseau traverse le monde est physiquement limité par la vitesse de la lumière. Par exemple, le temps le plus court possible pour le **temps d'aller-retour** d'une requête (c'est-à-dire, aller et revenir) dans un câble à fibre optique entre New York et Sydney est [160ms](https://www.oreilly.com/learning/primer-on-latency-and-bandwidth). Les systèmes distribués vous permettent d'avoir un nœud dans les deux villes, permettant au trafic de toucher le nœud qui est le plus proche de lui.

Pour qu'un système distribué fonctionne, cependant, vous avez besoin du logiciel fonctionnant sur ces machines pour être spécifiquement conçu pour fonctionner sur plusieurs ordinateurs en même temps et gérer les problèmes qui en découlent. Cela s'avère être une tâche ardue.

### Mise à l'échelle de notre base de données

Imaginez que notre application web est devenue incroyablement populaire. Imaginez également que notre base de données a commencé à recevoir deux fois plus de requêtes par seconde qu'elle ne peut en gérer. Votre application commencerait immédiatement à voir ses performances décliner et cela serait remarqué par vos utilisateurs.

Travaillons ensemble et faisons en sorte que notre base de données puisse répondre à nos demandes élevées.

Dans une application web typique, vous lisez normalement les informations beaucoup plus fréquemment que vous n'insérez de nouvelles informations ou modifiez les anciennes.

Il existe un moyen d'augmenter les performances de lecture et c'est par la stratégie de réplication dite **Primary-Replica**. Ici, vous créez deux nouveaux serveurs de base de données qui se synchronisent avec le principal. Le piège est que vous pouvez **uniquement lire** à partir de ces nouvelles instances.

Chaque fois que vous insérez ou modifiez des informations — vous parlez à la base de données principale. Celle-ci, à son tour, informe de manière asynchrone les réplicas du changement et ils le sauvegardent également.

Félicitations, vous pouvez maintenant exécuter 3 fois plus de requêtes de lecture ! N'est-ce pas génial ?

### Piège

**Attention !** Nous avons immédiatement perdu le **_C_** dans les garanties **ACID** de notre base de données relationnelle, qui signifie Cohérence.

Vous voyez, il existe maintenant une possibilité où nous insérons un nouvel enregistrement dans la base de données, émettons immédiatement après une requête de lecture pour celui-ci et n'obtenons rien en retour, comme s'il n'existait pas !

La propagation des nouvelles informations de la base principale vers la réplica ne se fait pas instantanément. Il existe en fait une fenêtre de temps dans laquelle vous pouvez récupérer des informations obsolètes. Si ce n'était pas le cas, vos performances d'écriture en souffriraient, car elles devraient attendre de manière synchrone que les données soient propagées.

Les systèmes distribués comportent un certain nombre de compromis. Ce problème particulier est celui avec lequel vous devrez vivre si vous souhaitez mettre à l'échelle de manière adéquate.

### Continuer à mettre à l'échelle

En utilisant l'approche de la base de données réplica, nous pouvons mettre à l'échelle horizontalement notre trafic de lecture jusqu'à un certain point. C'est génial, mais nous avons atteint une limite en ce qui concerne notre trafic d'écriture — il est toujours sur un seul serveur !

Nous n'avons pas beaucoup d'options ici. Nous devons simplement diviser notre trafic d'écriture en plusieurs serveurs, car un seul n'est pas capable de le gérer.

Une façon est d'opter pour une [stratégie de réplication multi-primaire](https://en.wikipedia.org/wiki/Multi-master_replication). Là, au lieu de réplicas que vous ne pouvez que lire, vous avez plusieurs nœuds principaux qui supportent les lectures et les écritures. Malheureusement, cela devient compliqué très rapidement, car vous avez maintenant la capacité de [créer des conflits](http://datacharmer.blogspot.bg/2013/03/multi-master-data-conflicts-part-1.html) (par exemple, insérer deux enregistrements avec le même ID).

Optons pour une autre technique appelée [**_sharding_**](https://medium.com/@jeeyoungk/how-sharding-works-b4dec46b3f6) (également appelée **_partitionnement_**).

Avec le sharding, vous divisez votre serveur en plusieurs serveurs plus petits, appelés **_shards_**. Ces shards contiennent tous des enregistrements différents — vous créez une règle quant au type d'enregistrements qui vont dans quel shard. Il est très important de créer la règle de telle sorte que les données soient réparties de manière **uniforme**.

Une approche possible consiste à définir des plages selon certaines informations sur un enregistrement (par exemple, les utilisateurs avec un nom de A à D).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jY6Zy746g2UdUUl7ZhN0VQ.png)

Cette clé de sharding doit être choisie très soigneusement, car la charge n'est pas toujours égale en fonction des colonnes arbitraires. (par exemple, plus de personnes ont un nom commençant par _C_ plutôt que par _Z_). Un seul shard qui reçoit plus de requêtes que les autres est appelé un **_point chaud_** et doit être évité. Une fois divisé, le re-sharding des données devient incroyablement coûteux et peut provoquer des temps d'arrêt significatifs, comme ce fut le cas avec [l'infâme panne de 11 heures de FourSquare](https://mashable.com/2010/10/05/foursquare-downtime-post-mortem/#qyp__Q9UDkqW).

Pour garder notre exemple simple, supposons que notre client (l'application Rails) sait quelle base de données utiliser pour chaque enregistrement. Il est également intéressant de noter qu'il existe de nombreuses stratégies pour le sharding et que ceci est un exemple simple pour illustrer le concept.

Nous avons gagné beaucoup maintenant — nous pouvons augmenter notre trafic d'écriture **_N_** fois où **_N_** est le nombre de shards. Cela nous donne pratiquement presque aucune limite — imaginez à quel point nous pouvons être fins avec ce partitionnement.

### Piège

Tout en ingénierie logicielle est plus ou moins un compromis et ceci ne fait pas exception. Le sharding n'est pas une tâche simple et est mieux évité [jusqu'à ce qu'il soit vraiment nécessaire](https://www.percona.com/blog/2009/08/06/why-you-dont-want-to-shard/).

Nous avons maintenant rendu les requêtes par des clés **autres que la clé partitionnée** incroyablement inefficaces (elles doivent passer par tous les shards). Les requêtes SQL `JOIN` sont encore pires et les requêtes complexes deviennent pratiquement inutilisables.

## Décentralisé vs Distribué

Avant d'aller plus loin, j'aimerais faire une distinction entre les deux termes.

Bien que les mots semblent similaires et puissent être conclus pour signifier la même chose logiquement, leur différence fait un impact technologique et politique significatif.

**_Décentralisé_** est toujours _distribué_ dans le sens technique, mais l'ensemble du système décentralisé n'est pas possédé par un seul acteur. Aucune entreprise ne peut posséder un système décentralisé, sinon il ne serait plus décentralisé.

Cela signifie que la plupart des systèmes que nous allons passer en revue aujourd'hui peuvent être considérés comme des **_systèmes centralisés distribués_** — et c'est ce pour quoi ils sont conçus.

Si vous y réfléchissez — il est plus difficile de créer un système décentralisé car vous devez alors gérer le cas où certains des participants sont malveillants. Ce n'est pas le cas avec les systèmes distribués normaux, car vous savez que vous possédez tous les nœuds.

_Note : Cette définition a été [beaucoup débattue](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/issues/50#issuecomment-154995201) et peut être confondue avec d'autres (pair-à-pair, fédéré). [Dans la littérature ancienne, elle a été définie différemment également.](https://ethereum.stackexchange.com/a/7829) Quoi qu'il en soit, ce que je vous ai donné comme définition est ce que je pense être le plus largement utilisé maintenant que la blockchain et les cryptomonnaies ont popularisé le terme._

### Catégories de systèmes distribués

Nous allons maintenant passer en revue quelques catégories de systèmes distribués et lister leur plus grande utilisation connue en production. Gardez à l'esprit que la plupart de ces chiffres sont obsolètes et sont probablement significativement plus grands au moment où vous lisez ceci.

### Stockages de données distribués

Les stockages de données distribués sont les plus largement utilisés et reconnus comme des bases de données distribuées. La plupart des bases de données distribuées sont des bases de données [NoSQL](https://en.wikipedia.org/wiki/NoSQL) non relationnelles, limitées à la sémantique clé-valeur. Elles offrent des performances et une scalabilité incroyables au détriment de la cohérence ou de la disponibilité.

> **Échelle connue** — [Apple est connue pour utiliser 75 000 nœuds Apache Cassandra stockant plus de 10 pétaoctets de données,](http://cassandra.apache.org/) en 2015

Nous ne pouvons pas aborder les discussions sur les stockages de données distribués sans d'abord introduire le **théorème CAP**.

#### Théorème CAP

[Prouvé il y a longtemps en 2002](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/), le théorème CAP stipule qu'un stockage de données distribué ne peut pas être simultanément cohérent, disponible et tolérant aux partitions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIUyhmHbihiiMRP7hWgBSw.png)
_Choisissez 2 sur 3 (Mais pas Cohérence et Disponibilité)_

Quelques définitions rapides :

* **Cohérence** — Ce que vous lisez et écrivez séquentiellement est ce à quoi vous vous attendez (vous souvenez-vous du piège avec la réplication de la base de données il y a quelques paragraphes ?)
* **Disponibilité** — l'ensemble du système ne meurt pas — chaque nœud non défaillant retourne toujours une réponse.
* **Tolérance aux partitions** — Le système continue de fonctionner et de maintenir ses garanties de cohérence/disponibilité malgré les [partitions réseau](https://www.symantec.com/security_response/glossary/define.jsp?letter=n&word=network-partition)

En réalité, la tolérance aux partitions doit être une donnée pour tout stockage de données distribué. Comme mentionné dans de nombreux endroits, [dont cet excellent article](https://codahale.com/you-cant-sacrifice-partition-tolerance/), vous ne pouvez pas avoir de cohérence et de disponibilité sans tolérance aux partitions.

Réfléchissez-y : si vous avez deux nœuds qui acceptent des informations et que leur connexion meurt — comment peuvent-ils être disponibles et vous fournir simultanément de la cohérence ? Ils n'ont aucun moyen de savoir ce que fait l'autre nœud et, à ce titre, peuvent soit devenir hors ligne _(indisponibles)_ soit travailler avec des informations obsolètes _(incohérentes)_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w2ItPb8JT6Gis0IORj0PYg.png)
_Que faisons-nous ?_

À la fin, vous devez choisir si vous voulez que votre système soit fortement cohérent ou hautement disponible **_en cas de partition réseau_**. 

La pratique montre que la plupart des applications valorisent davantage la disponibilité. Vous n'avez pas nécessairement toujours besoin d'une forte cohérence. Même alors, ce compromis n'est pas nécessairement fait parce que vous avez besoin de la garantie de 100 % de disponibilité, mais plutôt parce que la latence du réseau peut être un problème lorsque vous devez synchroniser les machines pour atteindre une forte cohérence. Ces facteurs et d'autres font que les applications optent généralement pour des solutions qui offrent une haute disponibilité.

De telles bases de données se contentent du modèle de cohérence le plus faible — **_cohérence éventuelle_** [_explication de la cohérence forte vs éventuelle_](https://hackernoon.com/eventual-vs-strong-consistency-in-distributed-databases-282fdad37cf7). Ce modèle garantit que si aucune nouvelle mise à jour n'est apportée à un élément donné, **éventuellement** tous les accès à cet élément retourneront la dernière valeur mise à jour.

Ces systèmes fournissent des propriétés **BASE** (par opposition aux propriétés ACID des bases de données traditionnelles)

* **B**asically **A**vailable — Le système retourne toujours une réponse
* **S**oft state — Le système pourrait changer au fil du temps, même en l'absence d'entrée (en raison de la cohérence éventuelle)
* **E**ventual consistency — En l'absence d'entrée, les données se propageront à chaque nœud tôt ou tard — devenant ainsi cohérentes

Exemples de telles bases de données distribuées disponibles — [Cassandra](http://cassandra.apache.org/), [Riak](http://basho.com/products/riak-kv/), [Voldemort](http://www.project-voldemort.com/voldemort/)

Bien sûr, il existe d'autres stockages de données qui préfèrent une cohérence plus forte — [HBase](https://hbase.apache.org/), [Couchbase](https://www.couchbase.com/), [Redis,](https://redis.io/) [Zookeeper](https://zookeeper.apache.org/)

Le théorème CAP mérite plusieurs articles à lui seul — certains concernant la manière dont vous pouvez [ajuster les propriétés CAP d'un système en fonction du comportement du client](http://www.goland.org/blockchain_and_cap/) et d'autres sur [la manière dont il n'est pas correctement compris](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html).

### Cassandra

Cassandra, comme mentionné ci-dessus, est une base de données No-SQL distribuée qui préfère les propriétés AP du CAP, se contentant de la cohérence éventuelle. Je dois admettre que cela peut être un peu trompeur, car Cassandra est hautement configurable — vous pouvez la faire fournir une forte cohérence au détriment de la disponibilité, mais ce n'est pas son cas d'utilisation courant.

Cassandra utilise le [hachage cohérent](https://en.wikipedia.org/wiki/Consistent_hashing) pour déterminer quels nœuds de votre cluster doivent gérer les données que vous passez. Vous définissez un **facteur de réplication**, qui indique essentiellement à combien de nœuds vous souhaitez répliquer vos données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tiXUe25uM3oLnKbARVOGHg.png)
_Écriture d'échantillon_

Lors de la lecture, vous ne lirez que depuis ces nœuds.

Cassandra est massivement scalable, offrant un débit d'écriture absurdement élevé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2o0w4Vbuynyt3_YJzKtnsw.png)
_Diagramme possiblement biaisé, montrant les benchmarks d'écritures par seconde. [Pris d'ici.](https://academy.datastax.com/planet-cassandra/nosql-performance-benchmarks" rel="noopener" target="_blank" title=")_

Bien que ce diagramme puisse être biaisé et qu'il semble comparer Cassandra à des bases de données configurées pour fournir une forte cohérence (sinon je ne vois pas pourquoi MongoDB perdrait en performance lorsqu'il est mis à niveau de 4 à 8 nœuds), cela devrait tout de même montrer ce dont un cluster Cassandra correctement configuré est capable.

Quoi qu'il en soit, dans le compromis des systèmes distribués qui permet la mise à l'échelle horizontale et un débit incroyablement élevé, Cassandra ne fournit pas certaines fonctionnalités fondamentales des bases de données ACID — à savoir, les transactions.

### Consensus

Les transactions de base de données sont délicates à implémenter dans les systèmes distribués car elles nécessitent que chaque nœud soit d'accord sur l'action à entreprendre (abandonner ou valider). Cela est connu sous le nom de **_consensus_** et c'est un problème fondamental dans les systèmes distribués.

Atteindre le type d'accord nécessaire pour le problème de "validation de transaction" est simple si les processus participants et le réseau sont complètement fiables. Cependant, les systèmes réels sont sujets à un certain nombre de pannes possibles, telles que des plantages de processus, des partitions réseau, et des messages perdus, déformés ou dupliqués.

Cela pose un problème — il a été [prouvé impossible](http://the-paper-trail.org/blog/a-brief-tour-of-flp-impossibility/) de garantir qu'un consensus correct soit atteint dans un délai limité sur un réseau non fiable.

En pratique, cependant, il existe des algorithmes qui atteignent un consensus sur un réseau non fiable assez rapidement. Cassandra fournit en fait des [transactions légères](https://www.beyondthelines.net/databases/cassandra-lightweight-transactions/) grâce à l'utilisation de l'algorithme [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) pour le consensus distribué.

## Calcul distribué

Le calcul distribué est la clé de l'afflux de traitement des Big Data que nous avons vu ces dernières années. C'est la technique de division d'une tâche énorme (par exemple, agréger 100 milliards d'enregistrements), dont aucun ordinateur unique n'est capable de l'exécuter pratiquement seul, en de nombreuses tâches plus petites, chacune pouvant s'adapter à une seule machine de commodité. Vous divisez votre énorme tâche en de nombreuses tâches plus petites, les faites exécuter sur de nombreuses machines en parallèle, agrégez les données de manière appropriée et vous avez résolu votre problème initial. Cette approche vous permet à nouveau de mettre à l'échelle horizontalement — lorsque vous avez une tâche plus grande, incluez simplement plus de nœuds dans le calcul.

> Échelle connue — [Folding@Home](https://en.wikipedia.org/wiki/Folding@home) avait [160k machines actives en 2012](https://www.webcitation.org/6CWRdkzP0?url=http://fah-web.stanford.edu/cgi-bin/main.py?qtype=osstats2)

Un innovateur précoce dans ce domaine était Google, qui, par nécessité de leurs grandes quantités de données, a dû inventer un nouveau paradigme pour le calcul distribué — MapReduce. Ils ont publié un [article à ce sujet en 2004](http://static.googleusercontent.com/media/research.google.com/en/us/archive/mapreduce-osdi04.pdf) et la communauté open source a ensuite créé [Apache Hadoop](https://mapr.com/products/apache-hadoop) basé sur celui-ci.

#### MapReduce

MapReduce peut être simplement défini en deux étapes — [mapping](https://en.wikipedia.org/wiki/Map_(higher-order_function)) les données et [réduction](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) à quelque chose de significatif.

Commençons avec un exemple :

Disons que nous sommes Medium et que nous avons stocké nos énormes informations dans une base de données distribuée secondaire à des fins d'entreposage. Nous voulons récupérer des données représentant le nombre de claps émis chaque jour tout au long d'avril 2017 (il y a un an).

Cet exemple est gardé aussi court, clair et simple que possible, mais imaginez que nous travaillons avec des charges de données (par exemple, analyser des milliards de claps). Nous ne stockerons pas toutes ces informations sur une seule machine, évidemment, et nous ne les analyserons pas avec une seule machine. Nous n'interrogerons pas non plus la base de données de production, mais plutôt une base de données "d'entrepôt" construite spécifiquement pour les travaux hors ligne de faible priorité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eOJWeVtD769sSOCynpFWAA.png)

Chaque travail Map est un nœud séparé transformant autant de données qu'il peut. Chaque travail parcourt toutes les données dans le nœud de stockage donné et les mappe à un simple tuple de la date et du nombre un. Ensuite, trois étapes intermédiaires _(dont personne ne parle)_ sont effectuées — Shuffle, Sort et Partition. Elles organisent davantage les données et les suppriment vers le travail de réduction approprié. Comme nous traitons avec des big data, nous avons chaque travail Reduce séparé pour travailler sur une seule date.

C'est un bon paradigme et cela vous permet de faire beaucoup avec — vous pouvez enchaîner plusieurs travaux MapReduce par exemple.

#### Meilleurs techniques

MapReduce est quelque peu obsolète de nos jours et apporte certains problèmes avec lui. Parce qu'il fonctionne par lots (travaux), un problème survient où si votre travail échoue — vous devez redémarrer tout. Un travail de 2 heures qui échoue peut vraiment ralentir toute votre pipeline de traitement de données et vous ne voulez pas cela, surtout pendant les heures de pointe.

Un autre problème est le temps que vous attendez jusqu'à ce que vous receviez des résultats. Dans les systèmes d'analyse en temps réel (qui ont tous des big data et utilisent donc le calcul distribué), il est important que vos dernières données traitées soient aussi fraîches que possible et certainement pas de quelques heures auparavant.

Ainsi, d'autres [architectures ont émergé](https://www.talend.com/blog/2017/08/28/lambda-kappa-real-time-big-data-architectures/) qui abordent ces problèmes. Notamment [Lambda Architecture](http://lambda-architecture.net/) (mélange de traitement par lots et de traitement en flux) et [Kappa Architecture](http://milinda.pathirage.org/kappa-architecture.com/) (uniquement traitement en flux). Ces avancées dans le domaine ont apporté de nouveaux outils les permettant — [Kafka Streams,](https://kafka.apache.org/documentation/streams/) [Apache Spark](https://spark.apache.org/), [Apache Storm](http://storm.apache.org/), [Apache Samza](http://samza.apache.org/).

### Systèmes de fichiers distribués

Les systèmes de fichiers distribués peuvent être considérés comme des stockages de données distribués. Ils sont la même chose en tant que concept — stocker et accéder à une grande quantité de données à travers un cluster de machines apparaissant comme une seule. Ils vont généralement de pair avec le calcul distribué.

> Échelle connue — [Yahoo est connu pour avoir exécuté HDFS sur plus de 42 000 nœuds pour le stockage de 600 Pétaoctets de données, dès 2011](https://www.slideshare.net/Hadoop_Summit/what-it-takes-to-run-hadoop-at-scale-yahoo-perspectives)

La différence étant que les systèmes de fichiers distribués permettent aux fichiers d'être accessibles en utilisant les mêmes interfaces et sémantiques que les fichiers locaux, et non via une API personnalisée comme le Cassandra Query Language [(CQL)](https://docs.datastax.com/en/cql/3.3/cql/cqlIntro.html).

#### HDFS

Hadoop Distributed File System (HDFS) est le système de fichiers distribué utilisé pour le calcul distribué via le framework Hadoop. Se targuant d'une adoption généralisée, il est utilisé pour stocker et répliquer de grands fichiers (de l'ordre du Go ou du To) sur de nombreuses machines.

Son architecture se compose principalement de **_NameNodes_** et de **_DataNodes_**. Les NameNodes sont responsables de la conservation des métadonnées sur le cluster, comme quel nœud contient quels blocs de fichiers. Ils agissent comme coordinateurs pour le réseau en déterminant où stocker et répliquer les fichiers, en suivant la santé du système. Les DataNodes stockent simplement les fichiers et exécutent des commandes comme répliquer un fichier, en écrire un nouveau et d'autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ur_2AO3TEENy4oXJuCmnHg.png)

Sans surprise, HDFS est mieux utilisé avec Hadoop pour le calcul car il fournit une conscience des données aux travaux de calcul. Lesdits travaux sont ensuite exécutés sur les nœuds stockant les données. Cela exploite la localité des données — optimise les calculs et réduit la quantité de trafic sur le réseau.

#### IPFS

[Interplanetary File System (IPFS)](https://ipfs.io/) est un nouveau protocole/réseau pair-à-pair passionnant pour un système de fichiers distribué. Exploitant la technologie [Blockchain](https://medium.com/p/ad59df18f3c0#fbff), il se targue d'une architecture complètement décentralisée sans propriétaire unique ni point de défaillance.

IPFS offre un système de nommage (similaire au DNS) appelé IPNS et permet aux utilisateurs d'accéder facilement aux informations. Il stocke les fichiers via un versionnage historique, similaire à la façon dont [Git](https://en.wikipedia.org/wiki/Git) le fait. Cela permet d'accéder à tous les états précédents d'un fichier.

Il est encore en cours de développement intensif (v0.4 au moment de la rédaction) mais a déjà vu des projets intéressés à construire dessus ([FileCoin](https://filecoin.io/) ).

### Messagerie distribuée

Les systèmes de messagerie fournissent un lieu central pour le stockage et la propagation de messages/événements au sein de votre système global. Ils vous permettent de découpler votre logique d'application de la communication directe avec vos autres systèmes.

> Échelle connue — [Le cluster Kafka de LinkedIn a traité 1 trillion de messages par jour avec des pics de 4,5 millions de messages par seconde.](https://engineering.linkedin.com/apache-kafka/how-we_re-improving-and-advancing-kafka-linkedin)

![Image](https://cdn-media-1.freecodecamp.org/images/1*67Gl85Pkv8JQUSgSWXfS7A.png)

Simplement dit, une plateforme de messagerie fonctionne de la manière suivante :

Un message est diffusé depuis l'application qui l'a potentiellement créé (appelé un **producteur**), entre dans la plateforme et est lu par potentiellement plusieurs applications qui s'y intéressent (appelées **consommateurs**).

Si vous devez enregistrer un certain événement à plusieurs endroits (par exemple, création d'utilisateur dans la base de données, l'entrepôt, le service d'envoi d'e-mails et tout ce que vous pouvez imaginer), une plateforme de messagerie est le moyen le plus propre de diffuser ce message.

Les consommateurs peuvent soit tirer des informations des courtiers (modèle de tirage) soit faire en sorte que les courtiers poussent des informations directement vers les consommateurs (modèle de poussée).

Il existe quelques plateformes de messagerie populaires de premier ordre :

[RabbitMQ](https://www.rabbitmq.com/) — Courtier de messages qui vous permet de contrôler plus finement les trajectoires des messages via des règles de routage et d'autres paramètres facilement configurables. Peut être appelé un courtier intelligent, car il contient beaucoup de logique et suit de près les messages qui le traversent. Fournit des paramètres pour **AP** et **CP** de **CAP**. Utilise un modèle de poussée pour notifier les consommateurs.

[Kafka](https://kafka.apache.org/) — Courtier de messages (et plateforme complète) qui est un peu plus bas niveau, car il ne suit pas quels messages ont été lus et ne permet pas de logique de routage complexe. Cela l'aide à atteindre des performances incroyables. À mon avis, c'est le plus grand prospect dans ce domaine avec un développement actif de la communauté open-source et le soutien de l'équipe [Confluent](https://www.confluent.io/blog). Kafka a probablement l'utilisation la plus répandue parmi les grandes entreprises technologiques. [J'ai écrit une introduction approfondie à ce sujet, où je détaille toutes ses bonnes caractéristiques.](https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1)

[Apache ActiveMQ](http://activemq.apache.org/) — Le plus ancien du groupe, datant de 2004. Utilise l'API JMS, ce qui signifie qu'il est orienté vers les applications Java EE. Il a été réécrit sous le nom de [ActiveMQ Artemis](https://activemq.apache.org/artemis/), qui offre des performances exceptionnelles à la hauteur de Kafka.

[Amazon SQS](https://aws.amazon.com/sqs/) — Un service de messagerie fourni par AWS. Vous permet de l'intégrer rapidement avec des applications existantes et élimine le besoin de gérer votre propre infrastructure, ce qui peut être un grand avantage, car des systèmes comme Kafka sont notoirement difficiles à configurer. Amazon propose également deux services similaires — [SNS](https://aws.amazon.com/sns/) et [MQ](https://aws.amazon.com/amazon-mq/), ce dernier étant essentiellement ActiveMQ mais géré par Amazon.

### Applications distribuées

Si vous déployez 5 serveurs Rails derrière un seul équilibreur de charge tous connectés à une seule base de données, pourriez-vous appeler cela une application distribuée ? Rappelez-vous ma définition ci-dessus :

> Un système distribué est un groupe d'ordinateurs travaillant ensemble pour apparaître comme un seul ordinateur à l'utilisateur final. Ces machines ont un état partagé, fonctionnent de manière concurrente et peuvent tomber en panne indépendamment sans affecter le temps de fonctionnement de l'ensemble du système.

Si vous comptez la base de données comme un état partagé, vous pourriez soutenir que cela peut être classé comme un système distribué — mais vous auriez tort, car vous avez manqué la partie "travaillant ensemble" de la définition.

Un système est distribué uniquement si les nœuds communiquent entre eux pour coordonner leurs actions.

Par conséquent, quelque chose comme une application exécutant son code back-end sur un [réseau pair-à-pair](https://en.wikipedia.org/wiki/Peer-to-peer) peut mieux être classé comme une application distribuée. Quoi qu'il en soit, tout cela est une classification inutile qui ne sert aucun but autre que d'illustrer à quel point nous sommes pointilleux sur le regroupement des choses.

> Échelle connue — [Essaim BitTorrent de 193 000 nœuds pour un épisode de Game of Thrones, avril 2014](https://torrentfreak.com/game-of-thrones-sets-new-torrent-swarm-record-140415/)

#### Machine virtuelle Erlang

Erlang est un langage fonctionnel qui a une grande sémantique pour la concurrence, la distribution et la tolérance aux pannes. La machine virtuelle Erlang elle-même gère la distribution d'une application Erlang.

Son modèle fonctionne en ayant de nombreux processus **isolés** [légers](https://en.wikipedia.org/wiki/Light-weight_process) tous avec la capacité de communiquer entre eux via un système intégré de passage de messages. Cela s'appelle le [**_modèle d'acteur_**](http://berb.github.io/diploma-thesis/original/054_actors.html) et les bibliothèques Erlang OTP peuvent être considérées comme un framework d'acteurs distribués (dans la lignée de [Akka](https://akka.io/) pour la JVM).

Le modèle est ce qui l'aide à atteindre une grande concurrence plutôt simplement — les processus sont répartis sur les cœurs disponibles du système qui les exécute. Comme cela est indiscernable d'un paramètre réseau (à part la capacité à perdre des messages), la VM d'Erlang peut se connecter à d'autres VM Erlang fonctionnant dans le même centre de données ou même dans un autre continent. Cet essaim de machines virtuelles exécute une seule application et gère les pannes de machine via la reprise (un autre nœud est programmé pour s'exécuter).

En fait, la couche distribuée du langage a été ajoutée afin de fournir une tolérance aux pannes. Un logiciel fonctionnant sur une seule machine est toujours à risque de voir cette machine unique mourir et mettre votre application hors ligne. Un logiciel fonctionnant sur de nombreux nœuds permet une gestion plus facile des pannes matérielles, à condition que l'application ait été construite dans cet esprit.

#### BitTorrent

BitTorrent est l'un des protocoles les plus largement utilisés pour transférer de grands fichiers à travers le web via des torrents. L'idée principale est de faciliter le transfert de fichiers entre différents pairs dans le réseau sans avoir à passer par un serveur principal.

En utilisant un client BitTorrent, vous vous connectez à plusieurs ordinateurs à travers le monde pour télécharger un fichier. Lorsque vous ouvrez un fichier .torrent, vous vous connectez à un soi-disant [**_tracker_**](https://en.wikipedia.org/wiki/BitTorrent_tracker), qui est une machine qui agit comme coordinateur. Il aide à la découverte de pairs, vous montrant les nœuds dans le réseau qui ont le fichier que vous souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n1HB0-fGdvSR4hZNMY1Kig.png)
_un réseau d'échantillon_

Vous avez les notions de deux types d'utilisateurs, un **_leecher_** et un **_seeder_**. Un leecher est l'utilisateur qui télécharge un fichier et un seeder est l'utilisateur qui téléverse ledit fichier.

Le côté amusant des réseaux pair-à-pair est que vous, en tant qu'utilisateur ordinaire, avez la capacité de rejoindre et de contribuer au réseau.

BitTorrent et ses précurseurs ([Gnutella](https://en.wikipedia.org/wiki/Gnutella), [Napster](https://computer.howstuffworks.com/napster2.htm)) vous permettent d'héberger volontairement des fichiers et de téléverser vers d'autres utilisateurs qui les souhaitent. La raison pour laquelle BitTorrent est si populaire est qu'il a été le premier de son genre à fournir des incitations pour contribuer au réseau. Le **_freeriding_**, où un utilisateur ne téléchargeait que des fichiers, était un problème avec les protocoles de partage de fichiers précédents.

BitTorrent a résolu le freeriding dans une certaine mesure en faisant en sorte que les seeders téléversent davantage vers ceux qui fournissent les meilleurs taux de téléchargement. Cela fonctionne en vous incitant à téléverser tout en téléchargeant un fichier. Malheureusement, une fois que vous avez terminé, rien ne vous oblige à rester actif dans le réseau. Cela provoque un manque de seeders dans le réseau qui ont le fichier complet et, comme le protocole repose fortement sur de tels utilisateurs, des solutions comme les [trackers privés](https://www.reddit.com/r/torrents/comments/2413bo/how_and_why_do_private_trackers_exist/ch2o1bo/) ont vu le jour. Les trackers privés vous obligent à être membre d'une communauté (souvent sur invitation uniquement) afin de participer au réseau distribué.

Après des avancées dans le domaine, des torrents sans tracker ont été inventés. Il s'agissait d'une mise à niveau du protocole BitTorrent qui ne reposait pas sur des trackers centralisés pour collecter des métadonnées et trouver des pairs, mais utilisait plutôt de nouveaux algorithmes. Une telle instance est [Kademlia](https://en.wikipedia.org/wiki/Kademlia) ([Mainline DHT](https://en.wikipedia.org/wiki/Mainline_DHT)), une table de hachage distribuée (DHT) qui vous permet de trouver des pairs via d'autres pairs. En effet, chaque utilisateur effectue les tâches d'un tracker.

### Registres distribués

Un registre distribué peut être considéré comme une base de données immuable, en ajout uniquement, qui est répliquée, synchronisée et partagée entre tous les nœuds du réseau distribué.

> Échelle connue — [Le réseau Ethereum a atteint un pic de 1,3 million de transactions par jour le 4 janvier 2018](https://etherscan.io/chart/tx).

Ils exploitent le modèle [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), vous permettant de reconstruire l'état du registre à tout moment de son historique.

#### Blockchain

La blockchain est la technologie sous-jacente actuelle utilisée pour les registres distribués et a en fait marqué leur début. Cette dernière et plus grande innovation dans l'espace distribué a permis la création du premier protocole de paiement véritablement distribué — Bitcoin.

La blockchain est un registre distribué portant une liste ordonnée de toutes les transactions qui se sont jamais produites dans son réseau. Les transactions sont regroupées et stockées dans des blocs. L'ensemble de la blockchain est essentiellement une [liste chaînée](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html) de blocs _(d'où le nom)_. Lesdits blocs sont coûteux en calcul à créer et sont étroitement liés les uns aux autres par la cryptographie.

Simplement dit, chaque bloc contient un hachage spécial (qui commence par X quantité de zéros) du contenu du bloc actuel (sous la forme d'un arbre de Merkle) plus le hachage du bloc précédent. Ce hachage nécessite beaucoup de puissance CPU pour être produit car la seule façon de le trouver est par force brute.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6sFhm0tZ6x55DqcnEHTxsQ.png)
_Blockchain simplifiée_

Les **mineurs** sont les nœuds qui tentent de calculer le hachage (par force brute). Les mineurs sont tous en compétition les uns avec les autres pour trouver qui peut trouver une chaîne aléatoire (appelée **_nonce_**) qui, combinée avec les contenus, produit le hachage mentionné précédemment. Une fois que quelqu'un trouve le nonce correct — il le diffuse à l'ensemble du réseau. Ladite chaîne est ensuite vérifiée par chaque nœud individuellement et acceptée dans leur chaîne.

Cela se traduit par un système où il est absurdement coûteux de modifier la blockchain et absurdement facile de vérifier qu'elle n'a pas été falsifiée.

Il est coûteux de modifier le contenu d'un bloc car cela produirait un hachage différent. Rappelez-vous que le hachage de chaque bloc suivant en dépend. Si vous deviez modifier une transaction dans le premier bloc de l'image ci-dessus — vous modifieriez la racine de Merkle. Cela modifierait à son tour le hachage du bloc (très probablement sans les zéros de tête nécessaires) — ce qui modifierait le hachage du bloc #2 et ainsi de suite. Cela signifie que vous devriez forcer par brute-force un nouveau nonce pour chaque bloc après celui que vous venez de modifier.

Le réseau fait toujours confiance et réplique la chaîne valide la plus longue. Afin de tromper le système et **éventuellement** produire une chaîne plus longue, vous auriez besoin de plus de 50 % de la puissance CPU totale utilisée par tous les nœuds.

La blockchain peut être considérée comme un mécanisme distribué pour le **_consensus émergent_**. Le consensus n'est pas atteint explicitement — il n'y a pas d'élection ou de moment fixe où le consensus se produit. Au lieu de cela, le consensus est un produit **_émergent_** de l'interaction asynchrone de milliers de nœuds indépendants, tous suivant les règles du protocole.

Cette innovation sans précédent est récemment devenue un boom dans l'espace technologique, avec des personnes prédisant qu'elle marquera la création du [Web 3.0](https://medium.com/@matteozago/why-the-web-3-0-matters-and-you-should-know-about-it-a5851d63c949). C'est définitivement l'espace le plus excitant dans le monde de l'ingénierie logicielle en ce moment, rempli de problèmes extrêmement difficiles et intéressants en attente de résolution.

#### Bitcoin

Ce que les précédents protocoles de paiement distribués manquaient, c'était un moyen de prévenir pratiquement le [problème de la double dépense](https://en.wikipedia.org/wiki/Double-spending) en temps réel, de manière distribuée. La recherche a produit des propositions intéressantes[1], mais Bitcoin a été le premier à implémenter une solution pratique avec des avantages clairs sur les autres.

Le problème de la double dépense stipule qu'un acteur (par exemple Bob) ne peut pas dépenser sa ressource unique en deux endroits. Si Bob a 1 $, il ne devrait pas être en mesure de le donner à la fois à Alice et à Zack — c'est un seul actif, il ne peut pas être dupliqué. Il s'avère qu'il est vraiment difficile d'atteindre cette garantie dans un système distribué. Il existe [certaines approches d'atténuation intéressantes](https://arxiv.org/abs/0802.0832v1) antérieures à la blockchain, mais elles ne résolvent pas complètement le problème de manière pratique.

La double dépense est facilement résolue par Bitcoin, car un seul bloc est ajouté à la chaîne à la fois. La double dépense est impossible au sein d'un seul bloc, donc même si deux blocs sont créés en même temps — un seul finira par être sur la chaîne la plus longue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q7OSbezEhFEUXjhQ4mrVDg.jpeg)

Bitcoin repose sur la difficulté d'accumuler de la puissance CPU.

Alors que dans un système de vote, un attaquant n'a besoin que d'ajouter des nœuds au réseau (ce qui est facile, car l'accès libre au réseau est un objectif de conception), dans un schéma basé sur la puissance CPU, un attaquant est confronté à une limitation physique : obtenir l'accès à du matériel de plus en plus puissant.

C'est aussi la raison pour laquelle des groupes malveillants de nœuds doivent contrôler plus de 50 % de la puissance de calcul du réseau pour mener une attaque réussie. Moins que cela, et le reste du réseau créera une blockchain plus longue plus rapidement.

#### Ethereum

Ethereum peut être considéré comme une plateforme logicielle programmable basée sur la blockchain. Il possède sa propre cryptomonnaie (Ether) qui alimente le déploiement de **_contrats intelligents_** sur sa blockchain.

Les contrats intelligents sont un morceau de code stocké sous forme de transaction unique dans la blockchain Ethereum. Pour exécuter le code, tout ce que vous avez à faire est d'émettre une transaction avec un contrat intelligent comme destination. Cela fait en sorte que les nœuds mineurs exécutent le code et les changements qu'il entraîne. Le code est exécuté à l'intérieur de la machine virtuelle Ethereum.

**_Solidity_**, le langage de programmation natif d'Ethereum, est ce qui est utilisé pour écrire des contrats intelligents. C'est un langage de programmation Turing-complet qui interface directement avec la blockchain Ethereum, vous permettant d'interroger l'état comme les soldes ou d'autres résultats de contrats intelligents. Pour prévenir les boucles infinies, l'exécution du code nécessite une certaine quantité d'Ether.

Comme la blockchain peut être interprétée comme une série de **_changements d'état_**, de nombreuses applications distribuées [(DApps)](https://medium.com/the-mission/2018-the-year-of-dapps-dbe108860bcb) ont été construites sur Ethereum et des plateformes similaires.

#### Autres usages des registres distribués

[**_Preuve d'existence_**](https://en.wikipedia.org/wiki/Proof_of_Existence) — Un service pour stocker de manière anonyme et sécurisée la preuve qu'un certain document numérique existait à un moment donné. Utile pour garantir l'intégrité des documents, la propriété et l'horodatage.

[**_Organisations autonomes décentralisées (DAO)_**](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization) — organisations qui utilisent la blockchain comme moyen d'atteindre un consensus sur les propositions d'amélioration de l'organisation. Des exemples sont [le système de gouvernance de Dash](https://www.dash.org/governance/), [le projet SmartCash](https://smartcash.cc/what-is-smartcash/)

**_Authentification décentralisée_** — Stockez votre identité sur la blockchain, vous permettant d'utiliser [l'authentification unique](https://en.wikipedia.org/wiki/Single_sign-on) (SSO) partout. [Sovrin](https://sovrin.org/), [Civic](https://www.civic.com/products/secure-identity-platform)

_Et bien d'autres. La technologie des registres distribués a vraiment ouvert des possibilités sans fin. Certaines sont probablement en train d'être inventées alors que nous parlons !_

### Résumé

Dans la courte durée de cet article, nous avons réussi à définir ce qu'est un système distribué, pourquoi vous en utiliseriez un et à passer en revue chaque catégorie un peu. Certaines choses importantes à retenir sont :

* Les systèmes distribués sont complexes
* Ils sont choisis par nécessité d'échelle et de prix
* Ils sont plus difficiles à travailler
* Théorème CAP — compromis Cohérence/Disponibilité
* Ils ont 6 catégories — stockages de données, calcul, systèmes de fichiers, systèmes de messagerie, registres, applications

Pour être franc, nous avons à peine effleuré la surface des systèmes distribués. Je n'ai pas eu l'occasion de traiter et d'expliquer en profondeur des problèmes fondamentaux comme le [consensus](https://www.cs.rutgers.edu/~pxk/417/notes/content/consensus.html), les [stratégies de réplication](http://www.cloudbus.org/papers/DataReplicationInDSChapter2006.pdf), [l'ordre des événements et le temps](https://swizec.com/blog/week-7-time-clocks-and-ordering-of-events-in-a-distributed-system/swizec/6444), [la tolérance aux pannes](http://blog.empathybox.com/post/19574936361/getting-real-about-distributed-system-reliability), [la diffusion d'un message à travers le réseau](https://www.distributed-systems.net/my-data/papers/2007.osr.pdf) et [d'autres](http://the-paper-trail.org/blog/distributed-systems-theory-for-the-distributed-systems-engineer/).

#### Avertissement

Permettez-moi de vous laisser avec un avertissement final :

Vous devez éviter les systèmes distribués autant que possible. La complexité qu'ils entraînent n'en vaut pas la peine si vous pouvez éviter le problème en le résolvant d'une autre manière ou par une autre solution clé en main.

**_[1]_**  
[Combattre la double dépense en utilisant des systèmes P2P coopératifs](https://ieeexplore.ieee.org/document/4268195/), 25–27 juin 2007 — une solution proposée dans laquelle chaque « pièce » peut expirer et est assignée à un témoin (validateur) pour sa dépense.

[_Bitgold_](http://web.archive.org/web/20060329122942/http://unenumerated.blogspot.com/2005/12/bit-gold.html), décembre 2005 — Un aperçu de haut niveau d'un protocole extrêmement similaire à celui de Bitcoin. On dit que c'est le précurseur de Bitcoin.

#### Lectures supplémentaires sur les systèmes distribués :

[_Designing Data-Intensive Applications, Martin Kleppmann_](https://dataintensive.net/) — Un excellent livre qui couvre tout sur les systèmes distribués et plus encore.

[_Spécialisation en Cloud Computing, Université de l'Illinois, Coursera_](https://www.coursera.org/specializations/cloud-computing) — Une longue série de cours (6) couvrant les concepts et applications des systèmes distribués

[_Jepsen_](https://aphyr.com/tags/Jepsen) — Blog expliquant de nombreuses technologies distribuées (ElasticSearch, Redis, MongoDB, etc)

Merci d'avoir pris le temps de lire cet article long (~5600 mots) !

Si, par quelque hasard, vous avez trouvé cela informatif ou pensez qu'il vous a apporté de la valeur, assurez-vous de lui donner autant d'applaudissements que vous pensez qu'il mérite et envisagez de le partager avec un ami qui pourrait utiliser une introduction à ce merveilleux domaine d'étude.

_~Stanislav Kozlovski_

#### Mise à jour

Je travaille actuellement chez [Confluent](http://confluent.io). Confluent est une entreprise de Big Data fondée par les créateurs d'[Apache Kafka](https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1) eux-mêmes ! Je suis immensément reconnaissant pour l'opportunité qu'ils m'ont donnée — je travaille actuellement sur Kafka lui-même, ce qui est au-delà de l'extraordinaire ! Chez Confluent, nous aidons à façonner tout l'écosystème open-source Kafka, y compris une nouvelle offre cloud Kafka-as-a-service gérée.

Nous recrutons pour de nombreux postes (surtout SRE/Ingénieurs Logiciels) en Europe et aux États-Unis ! Si vous êtes intéressé à travailler sur Kafka lui-même, à la recherche de nouvelles opportunités ou simplement curieux — assurez-vous de m'envoyer un message sur [Twitter](https://twitter.com/StanKozlovski) et je partagerai tous les grands avantages qui viennent du travail dans une entreprise de la baie.