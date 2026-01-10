---
title: Plongée approfondie dans les internes et l'architecture de Spark
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-14T20:18:53.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-spark-internals-and-architecture-f6e32045393b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EzZs4uEuO30lV51KV07_RA.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: spark
  slug: spark
- name: technology
  slug: technology
seo_title: Plongée approfondie dans les internes et l'architecture de Spark
seo_desc: 'By Jayvardhan Reddy

  Apache Spark is an open-source distributed general-purpose cluster-computing framework.
  A spark application is a JVM process that’s running a user code using the spark
  as a 3rd party library.

  As part of this blog, I will be showin...'
---

Par Jayvardhan Reddy

**_Apache Spark_** est un framework de calcul en cluster distribué, généraliste et open-source. Une application Spark est un processus JVM qui exécute un code utilisateur en utilisant Spark comme une bibliothèque tierce.

Dans le cadre de cet article, je vais montrer comment Spark fonctionne sur l'architecture Yarn avec un exemple et les divers processus sous-jacents impliqués tels que :

* Contexte Spark
* Yarn Resource Manager, Application Master et lancement des exécutants (conteneurs).
* Configuration des variables d'environnement, des ressources de travail.
* CoarseGrainedExecutorBackend et RPC basé sur Netty.
* SparkListeners.
* Exécution d'un travail (plan logique, plan physique).
* Spark-WebUI.

#### **Contexte Spark**

Le contexte Spark est le premier niveau de point d'entrée et le cœur de toute application Spark. **_Spark-shell_** n'est rien d'autre qu'un REPL basé sur Scala avec des binaires Spark qui créera un objet sc appelé contexte Spark.

Nous pouvons lancer le shell Spark comme montré ci-dessous :

```
spark-shell --master yarn \ --conf spark.ui.port=12345 \ --num-executors 3 \ --executor-cores 2 \ --executor-memory 500M
```

Dans le cadre du spark-shell, nous avons mentionné le nombre d'exécutants. Ils indiquent le nombre de nœuds travailleurs à utiliser et le nombre de cœurs pour chacun de ces nœuds travailleurs pour exécuter des tâches en parallèle.

Ou vous pouvez lancer le shell Spark en utilisant la configuration par défaut.

```
spark-shell --master yarn
```

Les configurations sont présentes dans **spark-env.sh**

![Image](https://cdn-media-1.freecodecamp.org/images/-6BLEYtF8novhDmJFdm5jOcRIcU2BnIeIMSY)

Notre programme Driver est exécuté sur le nœud Gateway qui n'est rien d'autre qu'un spark-shell. Il créera un contexte Spark et lancera une application.

![Image](https://cdn-media-1.freecodecamp.org/images/AfCWOl6WV-LTqqOBZhu1vmZgAdxTuEUO0NXm)

L'objet contexte Spark peut être accédé en utilisant **sc.**

![Image](https://cdn-media-1.freecodecamp.org/images/XddrUMFGYv0CZtW0KVYll8t6gH0B-vsdJrZJ)

Après la création du contexte Spark, il attend les ressources. Une fois les ressources disponibles, le contexte Spark configure les services internes et établit une connexion à un environnement d'exécution Spark.

#### **Yarn Resource Manager, Application Master et lancement des exécutants (conteneurs).**

Une fois le contexte Spark créé, il vérifie avec le **_Cluster Manager_** et lance le **_Application Master_**, c'est-à-dire, lance un conteneur et enregistre les gestionnaires de signaux**_._**

![Image](https://cdn-media-1.freecodecamp.org/images/cjo3Db6Bu6YAfbynbMqAnUeZwq7b2gyDktzI)

![Image](https://cdn-media-1.freecodecamp.org/images/oPN9axnzYJYOD4uVrgnAFHavgelG7PU6qcxC)

Une fois l'Application Master démarré, il établit une connexion avec le Driver.

![Image](https://cdn-media-1.freecodecamp.org/images/HNXgewZ5xbv1rnAtlAkrVX8cIpM57MEAPUUF)

Ensuite, l'ApplicationMasterEndPoint déclenche une application proxy pour se connecter au gestionnaire de ressources.

![Image](https://cdn-media-1.freecodecamp.org/images/qYP4KcyLx47l13m2rK7DmHz1v3HjjvOvfCfc)

Maintenant, le conteneur Yarn effectuera les opérations suivantes comme montré dans le diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/Nn-uzm4KF38fk3GEP46x6nHaRY4qEiF0OKZv)
_Crédits Image : [jaceklaskowski.gitbooks.io](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/yarn/spark-yarn-applicationmaster.html" rel="noopener" target="_blank" title=")_

ii) YarnRMClient s'enregistrera avec l'Application Master.

![Image](https://cdn-media-1.freecodecamp.org/images/L-1dKAks3zKzEG-3LQjUb59y87o32NwCm0CH)

iii) YarnAllocator : Demandera 3 conteneurs d'exécutants, chacun avec 2 cœurs et 884 Mo de mémoire incluant 384 Mo de surcharge

![Image](https://cdn-media-1.freecodecamp.org/images/k8JzuqdtEIr30S2i9FDqjLfuCU0fdx1V7hJ9)

iv) AM démarre le Reporter Thread

![Image](https://cdn-media-1.freecodecamp.org/images/0ivLtRFO8U-sXl9auRRFgjaIiCRl7ggf5gEU)

Maintenant, l'allocateur Yarn reçoit des jetons du Driver pour lancer les nœuds Executor et démarrer les conteneurs.

![Image](https://cdn-media-1.freecodecamp.org/images/ISQkVVySYyDsBWkE5i3OEi-JI602MXyd1SpG)

#### **Configuration des variables d'environnement, des ressources de travail et lancement des conteneurs.**

Chaque fois qu'un conteneur est lancé, il effectue les 3 choses suivantes dans chacun d'eux.

* Configuration des variables d'environnement

L'environnement d'exécution Spark (SparkEnv) est l'environnement d'exécution avec les services de Spark qui sont utilisés pour interagir les uns avec les autres afin d'établir une plateforme de calcul distribué pour une application Spark.

![Image](https://cdn-media-1.freecodecamp.org/images/IuLu5w5LZBGd3LNj5HMD7hUA8M0f9KpdQO4T)

![Image](https://cdn-media-1.freecodecamp.org/images/WvPtwOF6swG4mdHfNdA7SNiaoW1WSAu5b16C)

* Configuration des ressources de travail

![Image](https://cdn-media-1.freecodecamp.org/images/-4Kq6oTpBIzxXxJslrnyja9NvEYOVK0fN8Eo)

* Lancement du conteneur

![Image](https://cdn-media-1.freecodecamp.org/images/eovWnCKboFLKrabJTkQeheqlSEL1pjvYzyIQ)

Le contexte de lancement de l'exécutant YARN attribue à chaque exécutant un identifiant d'exécutant pour identifier l'exécutant correspondant (via Spark WebUI) et démarre un CoarseGrainedExecutorBackend.

![Image](https://cdn-media-1.freecodecamp.org/images/HwkvxgUxXrbP-sSlod7ww2ON730xBNoCD5OL)

#### **CoarseGrainedExecutorBackend et RPC basé sur Netty.**

Après avoir obtenu des ressources du Resource Manager, nous verrons le démarrage de l'exécutant

![Image](https://cdn-media-1.freecodecamp.org/images/JV2n4sSeorLmRQeqYV5qnX0VipHO7UDpOTDs)

**_CoarseGrainedExecutorBackend_** est un ExecutorBackend qui contrôle le cycle de vie d'un seul exécutant. Il envoie le statut de l'exécutant au driver.

Lorsque ExecutorRunnable est démarré, CoarseGrainedExecutorBackend enregistre le point de terminaison RPC de l'exécutant et les gestionnaires de signaux pour communiquer avec le driver (c'est-à-dire avec le point de terminaison RPC de CoarseGrainedScheduler) et pour informer qu'il est prêt à lancer des tâches.

![Image](https://cdn-media-1.freecodecamp.org/images/eCIDgTM7qIHET63gN0hT3bURjLreHK0clFvD)

**_Netty-based RPC -_** Il est utilisé pour communiquer entre les nœuds travailleurs, le contexte spark, les exécutants.

![Image](https://cdn-media-1.freecodecamp.org/images/enybOZ6oQRaFwrbnQIbxdcEYf4taktLy8-vO)

NettyRPCEndPoint est utilisé pour suivre le statut du résultat du nœud travailleur.

RpcEndpointAddress est l'adresse logique pour un point de terminaison enregistré à un environnement RPC, avec RpcAddress et nom.

Il est au format comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/kLkRsIqy4YhYzRXyUuDroQHeNgxu7Vozk1Gp)

C'est le premier moment où CoarseGrainedExecutorBackend initie la communication avec le driver disponible à driverUrl via RpcEnv.

![Image](https://cdn-media-1.freecodecamp.org/images/de85dQifuBDHqUZdqmXrl14e3LYMJuHvQZKP)

#### **SparkListeners**

![Image](https://cdn-media-1.freecodecamp.org/images/AIHRmLNMZpTUpgYFqylC0FeveeYLmLjbnZbo)
_Crédits Image : [jaceklaskowski.gitbooks.io](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-scheduler-LiveListenerBus.html" rel="noopener" target="_blank" title=")_

SparkListener (écouteur de planificateur) est une classe qui écoute les événements d'exécution du DAGScheduler de Spark et journalise toutes les informations d'événement d'une application telles que l'exécutant, les détails d'allocation du driver ainsi que les travaux, les étapes et les tâches et d'autres changements de propriétés d'environnement.

SparkContext démarre le LiveListenerBus qui réside à l'intérieur du driver. Il enregistre JobProgressListener avec LiveListenerBus qui collecte toutes les données pour montrer les statistiques dans l'interface utilisateur Spark.

Par défaut, seul l'écouteur pour WebUI serait activé, mais si nous voulons ajouter d'autres écouteurs, nous pouvons utiliser **spark.extraListeners.**

Spark est livré avec deux écouteurs qui montrent la plupart des activités

i) StatsReportListener

ii) EventLoggingListener

**_EventLoggingListener:_** Si vous souhaitez analyser davantage les performances de vos applications au-delà de ce qui est disponible dans le serveur d'historique Spark, vous pouvez traiter les données de journal des événements. Le journal des événements Spark enregistre les informations sur les travaux/étapes/tâches traités. Il peut être activé comme montré ci-dessous...

![Image](https://cdn-media-1.freecodecamp.org/images/haTAg5LO0bzKsjjXZbpE26AkR2Is2nLBbOzF)

Le fichier de journal des événements peut être lu comme montré ci-dessous

* Le driver Spark journalise la charge de travail/les métriques de performance dans le répertoire spark.evenLog.dir sous forme de fichiers JSON.
* Il y a un fichier par application, les noms de fichiers contiennent l'identifiant de l'application (comprenant donc un horodatage) application_1540458187951_38909.

![Image](https://cdn-media-1.freecodecamp.org/images/ecY6tTy-i4s3mmYZoAhraM2KENWWtVgJD8wY)

Il montre le type d'événements et le nombre d'entrées pour chacun.

![Image](https://cdn-media-1.freecodecamp.org/images/ANujSUpy0IQexpkoae-HfMFckmOPwCLV1-ve)

Maintenant, ajoutons **_StatsReportListener_** à spark.extraListeners et vérifions le statut du travail.

Activez le niveau de journalisation INFO pour le logger org.apache.spark.scheduler.StatsReportListener pour voir les événements Spark.

![Image](https://cdn-media-1.freecodecamp.org/images/B7HGuBTSYxAa6Ep8B47LncJicPMXZiT6bkPP)

Pour activer l'écouteur, vous l'enregistrez dans SparkContext. Cela peut être fait de deux manières.

i) En utilisant la méthode SparkContext.addSparkListener(listener: SparkListener) à l'intérieur de votre application Spark.

Cliquez sur le lien pour implémenter des écouteurs personnalisés - [**CustomListener**](https://stackoverflow.com/questions/24463055/how-to-implement-custom-job-listener-tracker-in-spark)

ii) En utilisant l'option de ligne de commande conf

![Image](https://cdn-media-1.freecodecamp.org/images/eOkpNJ380lOHphroPJjCYtKcBTrnwCMncM7G)

Lisons un fichier exemple et effectuons une opération de comptage pour voir le StatsReportListener.

![Image](https://cdn-media-1.freecodecamp.org/images/C5Aro1tHenM1CulhoUqtcvbg487-4TfhrNfR)

#### **Exécution d'un travail (plan logique, plan physique).**

Dans Spark, RDD (_jeu de données distribué résilient_) est le premier niveau de la couche d'abstraction. Il s'agit d'une collection d'éléments partitionnés sur les nœuds du cluster qui peuvent être exploités en parallèle. Les RDD peuvent être créés de 2 manières.

**i) _Parallélisation_ d'une collection existante dans votre programme driver**

![Image](https://cdn-media-1.freecodecamp.org/images/URNJDr-DZdPfXLVbiWQrEe2-PEX0-p67g1mw)

**ii) Référencement d'un jeu de données dans un système de stockage externe**

![Image](https://cdn-media-1.freecodecamp.org/images/mFYIkS67sITmSz7SV1MOfFDaMVh-jWQB4ARv)

Les RDD sont créés soit en utilisant un fichier dans le système de fichiers Hadoop, soit une collection Scala existante dans le programme driver, et en le transformant.

Prenons un extrait de code comme montré ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/H4qJqN74iIRbDBWx6qhi9Uuqr7EFNTKYT2Df)

L'exécution de l'extrait de code ci-dessus se déroule en 2 phases.

**_6.1 Plan Logique:_** Dans cette phase, un RDD est créé en utilisant un ensemble de transformations. Il garde une trace de ces transformations dans le programme driver en construisant une chaîne de calcul (une série de RDD) sous forme de graphe de transformations pour produire un RDD appelé **_Graphe de Lignée_**. 

Les transformations peuvent être divisées en 2 types

* **Transformation étroite :** Un pipeline d'opérations qui peut être exécuté en une seule étape et ne nécessite pas que les données soient mélangées entre les partitions — par exemple, Map, filter, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/y0iv0YErJYvRwvm8BEEqw9KhIVM5IM54FLJZ)

Maintenant, les données seront lues dans le driver en utilisant la variable de diffusion.

![Image](https://cdn-media-1.freecodecamp.org/images/LpuhSTa3XXdggW9J4e52QXTSNGKIbBzwOYdY)

* **Transformation large :** Ici, chaque opération nécessite que les données soient mélangées, par conséquent, pour chaque transformation large, une nouvelle étape sera créée — par exemple, reduceByKey, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/8Wzx99ex1SXX0WUPWTVPjzUTLbjS1j0QawFG)

Nous pouvons voir le graphe de lignée en utilisant **_toDebugString_**

![Image](https://cdn-media-1.freecodecamp.org/images/Tiz7zB4BUl8KhLcyE9LFZMKzwt3RWt1Symj9)

**_6.2 Plan Physique:_** Dans cette phase, une fois que nous déclenchons une action sur le RDD, le **_DAG Scheduler_** examine la lignée RDD et élabore le meilleur plan d'exécution avec des étapes et des tâches ainsi que TaskSchedulerImpl et exécute le travail en un ensemble de tâches parallèles.

![Image](https://cdn-media-1.freecodecamp.org/images/YYUBKfaYaYQiE7zrsdUOCNwSkcs8fll7FhyF)

Une fois que nous effectuons une opération d'action, le SparkContext déclenche un travail et enregistre le RDD jusqu'à la première étape (c'est-à-dire, avant toute transformation large) dans le cadre du DAGScheduler.

![Image](https://cdn-media-1.freecodecamp.org/images/5zSZlLhIownDYA1xRAuMjyG4waHL4M654lNn)

Maintenant, avant de passer à l'étape suivante (transformations larges), il vérifie s'il y a des données de partition à mélanger et s'il manque des résultats d'opérations parentales dont il dépend. Si une telle étape est manquante, il réexécute cette partie de l'opération en utilisant le DAG (graphe acyclique dirigé) qui le rend tolérant aux pannes.

![Image](https://cdn-media-1.freecodecamp.org/images/RbSQEIy9nbRolwQPc0lygIxhCa9odYAgaaP0)

En cas de tâches manquantes, il attribue des tâches aux exécutants.

![Image](https://cdn-media-1.freecodecamp.org/images/q2UCiTrCdl1D4Jr7uM47IbdStmXvOSW2LrNc)

Chaque tâche est attribuée au CoarseGrainedExecutorBackend de l'exécutant.

![Image](https://cdn-media-1.freecodecamp.org/images/QcoWEHGMvmiF5lBbmAN4oT1y5cOUt6kEZ0OB)

Il obtient les informations de bloc du Namenode.

![Image](https://cdn-media-1.freecodecamp.org/images/smtnxaTQw1B5rzIQ0aoDgfcpZh4PL5GPhcrH)

Maintenant, il effectue le calcul et retourne le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/pSG-NIrRKOV-LxRxXGLgbi2pizwgx2wiCZtB)

Ensuite, le DAGScheduler recherche les nouvelles étapes exécutables et déclenche l'opération de l'étape suivante (reduceByKey).

![Image](https://cdn-media-1.freecodecamp.org/images/o5SPhS1d8o1fG5klmiupU--BEc52ZvmaWbbA)

Le ShuffleBlockFetcherIterator obtient les blocs à mélanger.

![Image](https://cdn-media-1.freecodecamp.org/images/aUU1-Z-0bbW8vZRS43DhJrwffkR6V0pHos2z)

Maintenant, l'opération de réduction est divisée en 2 tâches et exécutée.

![Image](https://cdn-media-1.freecodecamp.org/images/U4WfZPLsoa76XL9bTz2xadadQD5cpZAVrTpq)

À la fin de chaque tâche, l'exécutant retourne le résultat au driver.

![Image](https://cdn-media-1.freecodecamp.org/images/-8Pwz7cMv3GLJwRJSCZ42Bm-NeD98E91Zf1r)

Une fois le travail terminé, le résultat est affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/m3KpbqF4utduxP0wHb634aOREZf2LXehYoyu)

#### **Spark-WebUI**

Spark-UI aide à comprendre le flux d'exécution du code et le temps nécessaire pour compléter un travail particulier. La visualisation aide à découvrir les problèmes sous-jacents qui se produisent pendant l'exécution et à optimiser davantage l'application Spark.

Nous verrons la visualisation Spark-UI dans le cadre de l'**étape 6** précédente.

Une fois le travail terminé, vous pouvez voir les détails du travail tels que le nombre d'étapes, le nombre de tâches qui ont été planifiées pendant l'exécution d'un travail.

![Image](https://cdn-media-1.freecodecamp.org/images/oMGL38wBVkMpbyBwDz8oUjn4J8HgUa6FkQcy)

En cliquant sur les travaux terminés, nous pouvons voir la visualisation DAG, c'est-à-dire les différentes transformations larges et étroites qui en font partie.

![Image](https://cdn-media-1.freecodecamp.org/images/QbHRUFsfBCmjW5Wjx-iwl1RKFG181TPvsso2)

Vous pouvez voir le temps d'exécution pris par chaque étape.

![Image](https://cdn-media-1.freecodecamp.org/images/EnqEsKsm7oOpyCmYjJUVJ78V6dP0tZwDYfr6)

En cliquant sur une étape particulière dans le cadre du travail, il montrera les détails complets concernant l'emplacement des blocs de données, la taille des données, l'exécutant utilisé, la mémoire utilisée et le temps nécessaire pour compléter une tâche particulière. Il montre également le nombre de mélanges qui ont lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/XABdREC97TPKB3l1tDHuvBT9fUo9oGnjFLm4)

De plus, nous pouvons cliquer sur l'onglet Executors pour voir l'exécutant et le driver utilisés.

![Image](https://cdn-media-1.freecodecamp.org/images/VAWPvAI4Jst5MN4Z60ed29qgrhAgs2fy5Yd0)

Maintenant que nous avons vu comment Spark fonctionne en interne, vous pouvez déterminer le flux d'exécution en utilisant l'interface utilisateur Spark, les journaux et en ajustant les Spark EventListeners pour déterminer la solution optimale lors de la soumission d'un travail Spark.

**Note_** : Les commandes exécutées liées à cet article sont ajoutées dans mon compte [GIT](https://github.com/Jayvardhan-Reddy/BigData-Ecosystem-Architecture).

De même, vous pouvez également lire plus ici :

* [Architecture de Sqoop en profondeur](https://medium.freecodecamp.org/an-in-depth-introduction-to-sqoop-architecture-ad4ae0532583) avec **code.**
* [Architecture HDFS en profondeur](https://medium.com/plumbersofdatascience/hdfs-architecture-in-depth-1edb822b95fa) avec **code**.
* [Architecture Hive en profondeur](https://medium.com/plumbersofdatascience/hive-architecture-in-depth-ba44e8946cbc) avec **code**.

Si vous le souhaitez, vous pouvez me contacter sur LinkedIn — [Jayvardhan Reddy](https://www.linkedin.com/in/jayvardhan-reddy-vanchireddy).

Si vous avez aimé lire cet article, vous pouvez cliquer sur l'applaudissement et faire savoir aux autres. Si vous souhaitez que j'ajoute autre chose, n'hésitez pas à laisser une réponse ?