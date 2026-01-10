---
title: Ce qu'il faut considérer pour une intégration sans douleur d'Apache Kafka
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T18:04:27.000Z'
originalURL: https://freecodecamp.org/news/what-to-consider-for-painless-apache-kafka-integration-df559e828876
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca635740569d1a4ca6eb0.jpg
tags:
- name: Apache Kafka
  slug: apache-kafka
- name: architecture
  slug: architecture
- name: big data
  slug: big-data
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Ce qu'il faut considérer pour une intégration sans douleur d'Apache Kafka
seo_desc: 'By Adi Polak

  Apache Kafka’s real-world adoption is exploding, and it claims to dominate the world
  of stream data. It has a huge developer community all over the world that keeps
  on growing. But, it can be painful too. So, just before jumping head fir...'
---

Par Adi Polak

L'adoption d'Apache Kafka dans le monde réel explose, et il prétend dominer le monde des données en flux continu. Il dispose d'une énorme communauté de développeurs à travers le monde qui ne cesse de croître. Mais cela peut aussi être douloureux. Alors, juste avant de sauter à pieds joints et de s'intégrer pleinement à Apache Kafka, vérifions l'eau et planifions à l'avance pour une intégration sans douleur.

![Image](https://cdn-media-1.freecodecamp.org/images/DdJhig6V7tsyyPxWQThFzKGd6R-8dbmw3-nw)
_nPhoto par [Unsplash](https://unsplash.com/photos/5fNmWej4tAA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Helloquence</a> sur <a href="https://unsplash.com/search/photos/computer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Qu'est-ce que c'est ?

Apache Kafka est un framework open source pour la messagerie asynchrone et c'est une plateforme de streaming distribuée. Il est basé sur TCP. Les messages sont persistés dans des topics. Les producteurs de messages sont appelés _publishers_ et les consommateurs de messages sont appelés _subscribers_.

Les consommateurs peuvent s'abonner à **un ou plusieurs topics** et consommer tous les messages de ce topic. Les messages sont écrits dans les partitions de topics.

Les _topics_ sont toujours multi-abonnés, ils peuvent avoir zéro, un ou plusieurs consommateurs qui s'abonnent aux données écrites. Pour chaque topic, Kafka maintient un journal de partition. Les métadonnées des journaux de partition et des topics sont généralement gérées par Zookeeper.

Si vous souhaitez en savoir plus sur la sémantique de livraison des messages Kafka — comme _au plus une fois_, _au moins une fois_ et _exactement une fois_ — lisez [ici](http://bit.ly/2Shu9L5).

De nombreuses entreprises technologiques ont déjà intégré Apache Kafka dans leur production en tant que **broker de messages, pipeline de suivi des activités des utilisateurs, collecteur de métriques, mécanisme d'agrégation de logs, dispositif de traitement de flux** et bien plus encore. Apache Kafka est écrit en Scala et Java.

#### Pourquoi Kafka ?

* _Kafka offre une **haute disponibilité** et une **tolérance aux pannes** des journaux de messages._ Les clusters Kafka conservent tous les enregistrements publiés. Il est par défaut **persistant** — Si vous ne définissez pas de limite pour Kafka, il conservera les enregistrements jusqu'à ce qu'il manque d'espace disque. Lorsque la **perte de données** signifie un échec catastrophique pour le produit, cela est essentiel pour la récupération.
* **Plusieurs consommateurs de topics** — lors de la configuration des consommateurs sous plusieurs groupes de consommateurs, cela aide à réduire l'ancien goulot d'étranglement de l'envoi des données à plusieurs applications pour le traitement. Kafka est distribué, donc il peut envoyer des informations aux consommateurs à partir de diverses machines physiques/instances de services. La réplication des topics vers un cluster secondaire est également relativement facile en utilisant la fonctionnalité de miroir d'Apache Kafka, MirrorMaker — voir un [exemple](http://bit.ly/2CsENsU) de miroir de données entre deux clusters HDInsight. **Souvenez-vous simplement**, si plusieurs consommateurs sont définis dans le cadre du même groupe (définis par le group.id), les données seront équilibrées sur tous les consommateurs du groupe.
* Kafka est **polyglotte** — il existe de nombreux clients en C#, Java, C, Python et plus encore. L'écosystème fournit également un proxy REST qui permet une intégration facile via HTTP et JSON.
* **Traitement en temps réel** — Kafka peut gérer des pipelines de données en temps réel pour la messagerie en temps réel des applications.
* **Scalable** — grâce à l'architecture distribuée, Kafka peut s'étendre sans entraîner de temps d'arrêt.
* et plus encore...

### Rendre l'intégration avec Kafka sans douleur

![Image](https://cdn-media-1.freecodecamp.org/images/ltseK3C8ZbvxjNtH95aPcVfZhWGx1wCqoapf)

#### Voici 6 choses à savoir avant de s'intégrer :

**1 — Apache Zookeeper peut devenir un point de douleur avec un cluster Kafka**

Dans le passé (versions < 0.81), Kafka utilisait Zookeeper pour maintenir les offsets de chaque topic et partition. Zookeeper participait au chemin de lecture, où des commits trop fréquents et trop de consommateurs entraînaient des problèmes de performance et de stabilité sévères.

En plus de cela, il est préférable d'utiliser des commits manuels avec les anciens consommateurs basés sur Zookeeper, car des auto-commits négligents pourraient entraîner une perte de données.

Les nouvelles versions de Kafka offrent leur propre gestion, où le consommateur peut utiliser Kafka lui-même pour gérer les offsets. Cela signifie qu'il existe un topic spécifique qui gère les offsets de lecture au lieu de Zookeeper.

Cependant, Kafka a toujours besoin d'un cluster avec Zookeeper, même dans les versions ultérieures 2.+. Zookeeper est utilisé pour stocker les configurations Kafka (réattribution de partitions si nécessaire) et l'API des topics Kafka, comme créer un topic, ajouter une partition, etc.

La charge sur Kafka est strictement liée au nombre de consommateurs, de brokers, de partitions et à la fréquence des commits du consommateur.

![Image](https://cdn-media-1.freecodecamp.org/images/YHjRwjTTwgWD4nilJIADm7GF9KkNyZPWG4NG)

**2 — Vous ne devriez pas envoyer de grands messages ou charges utiles via Kafka**

Selon Apache Kafka, pour un meilleur débit, la taille maximale des messages doit être de **10 Ko**. Si les messages sont plus grands que cela, il est préférable de vérifier les alternatives ou de trouver un moyen de découper le message en parties plus petites avant de l'écrire dans Kafka. La meilleure pratique consiste à utiliser une clé de message pour s'assurer que tous les messages découpés seront écrits dans la même partition.

**3 — Apache Kafka ne peut pas transformer les données**

De nombreux développeurs se trompent et pensent qu'ils peuvent créer des analyseurs Kafka ou effectuer une transformation de données via Kafka. Cependant, Kafka ne permet pas la transformation des données. Si vous utilisez les services Azure, il existe une excellente liste de [services de data factories](http://bit.ly/2Sk8rpS) que vous pouvez utiliser pour transformer les données comme [Azure Databricks](http://bit.ly/2Lv6uEm), [HDInsights Spark](http://bit.ly/2EK5EDp) et d'autres qui se connectent à Kafka.

Une autre solution consiste à utiliser [Apache Kafka Stream](https://kafka.apache.org/documentation/streams/). Il s'agit en fait d'une nouvelle API construite sur les clients producteurs et consommateurs de Kafka. Elle est significativement plus puissante et également plus expressive que le client consommateur Kafka.

Le client `[KafkaStreams](https://kafka.apache.org/10/javadoc/org/apache/kafka/streams/KafkaStreams.html)` nous permet d'effectuer des calculs continus sur les entrées provenant d'un ou plusieurs topics d'entrée et envoie la sortie à zéro, un ou plusieurs topics de sortie. En interne, une instance `KafkaStreams` contient un `[KafkaProducer](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html)` et une instance `[KafkaConsumer](https://kafka.apache.org/10/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)` normale qui est utilisée pour lire les entrées et écrire les sorties.

Une autre option consiste à utiliser Flink, consultez-le [ici](https://www.baeldung.com/kafka-flink-data-pipeline).

**4 — Apache Kafka prend en charge un protocole binaire sur TCP**

Le protocole de communication d'Apache Kafka est basé sur TCP. Il ne prend pas en charge MQTT ou JMS ou d'autres protocoles non basés sur TCP hors de la boîte. Cependant, de nombreux utilisateurs ont écrit des adaptateurs pour lire des données à partir de ces protocoles et écrire dans Apache Kafka. Par exemple [kafka-jms-client](https://github.com/adispennette/apache-kafka-jms).

![Image](https://cdn-media-1.freecodecamp.org/images/ScLTW1xegqrB9bKdZwmPrT0WUgzsmRzycyFV)
_Poignée de main TCP simple_

**5 — Gestion / support d'Apache Kafka et la courbe d'apprentissage abrupte**

À ce jour, il existe des systèmes de gestion basés sur l'UI _gratuits_ limités pour Apache Kafka, et la plupart des DevOps avec lesquels j'ai travaillé utilisent des outils de script. Cependant, cela peut être fastidieux pour un débutant de se lancer dans les outils de script Apache Kafka sans prendre le temps de se former. La courbe d'apprentissage est abrupte et prend un certain temps pour avancer et s'intégrer dans de grands systèmes en cours d'exécution.

Pour les DevOps/développeurs expérimentés, cela peut prendre quelques mois (2+) pour comprendre pleinement comment intégrer, supporter et travailler avec Apache Kafka. Il est important d'apprendre comment Kafka fonctionne afin d'utiliser la configuration de la manière qui conviendra le mieux aux besoins du système.

Voici une liste d'outils de gestion que vous pouvez utiliser pour **presque gratuit** (certains sont restreints à un usage personnel/communautaire) :

* [KafkaTool](http://www.kafkatool.com/) — Application GUI pour gérer et utiliser les clusters **Apache Kafka**.
* [Confluent Platform](https://www.confluent.io/product/confluent-platform/) — Solution complète de plateforme de streaming d'entreprise.
* [KafDrop](https://github.com/HomeAdvisor/Kafdrop) — Outil pour afficher des informations telles que les brokers, les topics, les partitions, et même vous permet de voir les messages. Il s'agit d'une application légère qui fonctionne sur Spring Boot et nécessite très peu de configuration.
* [Yahoo Kafka Manager](https://github.com/yahoo/kafka-manager) — Un autre outil pour surveiller Kafka, mais il offre beaucoup moins que les autres.

**Support de Kafka géré sur le cloud**

Aujourd'hui, presque tous les clouds supportent Kafka, qu'il soit entièrement géré ou en utilisant une intégration avec Confluent depuis le magasin cloud jusqu'à l'achat de machines Kafka :

* [Confluent Cloud - Kafka en tant que Service](https://www.confluent.io/confluent-cloud/)
* [Azure Event Hub](http://bit.ly/2Ah5MGo) - Kafka entièrement géré
* [Kafka géré sur HDInsight — Azure](http://bit.ly/2BEpPyp)
* [Machine Kafka sur Google Cloud](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/kafka?pli=1)
* [Kafka sur AWS en utilisant la solution Confluent](https://aws.amazon.com/quickstart/architecture/confluent-platform/)
* ... et bien d'autres

**6 — Kafka n'est pas magique — Il existe toujours une possibilité de perte de données**

Apache Kafka est probablement l'outil le plus populaire pour la messagerie asynchrone distribuée. Cela est principalement dû à ses capacités de **haut débit, faible latence, scalabilité, centralisation et temps réel**. La plupart de cela est dû à l'utilisation de réplicas de données qui dans Kafka sont appelés partitions.

Cependant, avec une mauvaise configuration, il existe une forte probabilité de **perte de données** lorsque les machines/processus tombent en panne, et ils tomberont en panne. Par conséquent, il est important de comprendre comment Kafka fonctionne et quelles sont les exigences du produit/système.

**7 — Cadre de test de défaillance intégré de Kafka Trogdor**

Pour vous aider à trouver la bonne configuration, l'équipe Kafka a créé [Trogdor](https://cwiki.apache.org/confluence/display/KAFKA/Fault+Injection). Trogdor est un cadre de test de défaillance.

**Comment cela fonctionne**

* Configurez Kafka comme vous le feriez en production
* Créez un producteur qui génère des messages avec une séquence de 1...X million.
* Exécutez le producteur
* Exécutez le consommateur
* Créez une défaillance en écrasant et/ou en suspendant le broker.
* Testez et vérifiez que chaque événement produit a été consommé.
* ... si ce n'est pas le cas, il est préférable de revenir en arrière et de mettre à jour la configuration en conséquence !

#### En plus de cela, il est important de se rappeler qu'Apache Kafka...

* N'est **pas un RPC** — Apache Kafka est un système de messagerie. Pour RPC, le service X doit être conscient du service Y et de la signature de l'appel. Par exemple, dans Kafka, si vous envoyez un message, cela ne signifie pas que quelqu'un le consommera, jamais. Dans RPC, il y a toujours un consommateur puisque le service lui-même est conscient du consommateur Y et crée un appel à sa signature/fonction.
* Ce n'est **pas une base de données** — ce n'est pas un bon endroit pour sauvegarder des messages puisque vous ne pouvez pas sauter entre eux ou créer une recherche sans un scan complet coûteux.

#### Juste un mot sur KSQL

Une bibliothèque intéressante apportée par la communauté Confluent est [KSQL](https://github.com/confluentinc/ksql). Elle est construite sur Kafka Stream. KSQL est une interface SQL complètement interactive. Vous pouvez l'utiliser sans écrire de code. KSQL est sous licence Confluent Community.

### TL;DR

Apache Kafka a de nombreux avantages, mais avant de l'ajouter en production, il faut être conscient que :

* Il a une courbe d'apprentissage abrupte — prenez le temps d'apprendre les détails de Kafka
* Vous devez gérer les ressources du cluster — soyez conscient des exigences comme Zookeeper
* Vous pouvez encore perdre des données avec Apache Kafka
* La plupart des clouds fournissent Kafka géré
* Il ne transformera pas les données
* Ce n'est pas une base de données
* Il prend en charge le protocole binaire sur le protocole TCP
* Pour le moment, vous ne pouvez pas envoyer de grands messages en utilisant Kafka
* Vous devriez utiliser Trogdor pour les tests de défaillance de votre système

Tout cela étant dit, Apache Kafka est probablement le meilleur outil pour les tâches de messagerie et de streaming.

Merci à [Gwen Shapira](https://www.freecodecamp.org/news/what-to-consider-for-painless-apache-kafka-integration-df559e828876/undefined) pour vos contributions et conseils tout au long du chemin.

Si vous avez aimé cette histoire, veuillez cliquer sur le bouton ?. N'hésitez pas à laisser un commentaire ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/aPn5w0kq5WP9lvUQ2a7dF1Yx-bUxVfvMDO1i)

[Suivez-moi](https://medium.com/@adipolak) ici, ou [ici](https://twitter.com/adipolak) pour plus de publications sur Scala, Kotlin, Big Data, le code propre et les absurdités des ingénieurs logiciels. Santé !