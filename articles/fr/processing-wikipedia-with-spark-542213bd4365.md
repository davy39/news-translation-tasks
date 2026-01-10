---
title: Leçons apprises lors du traitement de Wikipedia avec Apache Spark
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-15T05:54:52.000Z'
originalURL: https://freecodecamp.org/news/processing-wikipedia-with-spark-542213bd4365
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KVxCfnROdLEWVwI3NLecFA.jpeg
tags:
- name: '#apache-spark'
  slug: apache-spark
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: technology
  slug: technology
- name: Wikipedia
  slug: wikipedia
seo_title: Leçons apprises lors du traitement de Wikipedia avec Apache Spark
seo_desc: 'By Siddhesh Rane

  Apache Spark is an open-source fault-tolerant cluster-computing framework that also
  supports SQL analytics, machine learning, and graph processing.

  It works by splitting your data into partitions, and then processing those partitions...'
---

Par Siddhesh Rane

[Apache Spark](http://spark.apache.org) est un framework de calcul en cluster tolérant aux pannes, open-source, qui supporte également l'analyse SQL, le machine learning et le traitement de graphes.

Il fonctionne en divisant vos données en partitions, puis en traitant ces partitions en parallèle sur tous les nœuds du cluster. Si un nœud tombe en panne, il réassigne la tâche de ce nœud à un autre nœud et assure ainsi la tolérance aux pannes.

Être 100 fois plus rapide que Hadoop l'a rendu [extêmement populaire pour le traitement des Big Data](http://fortune.com/2015/09/25/apache-spark-survey/). Spark est écrit en Scala et s'exécute sur la JVM, mais la bonne nouvelle est qu'il fournit également des API pour Python et R ainsi que pour C#. Il est bien [documenté](http://spark.apache.org/docs/latest/) avec des [exemples](http://spark.apache.org/examples.html) que vous devriez consulter.

Lorsque vous êtes prêt à l'essayer, cet article vous guidera du téléchargement et de l'installation jusqu'à l'optimisation des performances. Mon petit cluster Spark a effectué 100 millions de correspondances de chaînes sur tous les articles de Wikipedia — en moins de deux heures.

C'est lorsque vous dépassez les tutoriels et que vous faites un travail sérieux que vous réalisez tous les tracas de la pile technologique que vous utilisez. Apprendre par ses erreurs est la meilleure façon d'apprendre. Mais parfois, vous manquez simplement de temps et vous souhaitez connaître toutes les choses possibles qui pourraient mal tourner.

Ici, je décris certains des problèmes auxquels j'ai été confronté lorsque j'ai commencé avec Spark, et comment vous pouvez les éviter.

### Comment commencer

#### Téléchargez le binaire Spark qui inclut les dépendances Hadoop packagées

Si vous vous lancez dans le téléchargement de Spark, vous remarquerez qu'il existe diverses versions binaires disponibles pour la même version. Spark annonce qu'il n'a pas besoin de Hadoop, donc vous pourriez télécharger la version user-provided-hadoop qui est plus petite en taille. **Ne faites pas cela**.

Bien que Spark n'utilise pas le framework MapReduce de Hadoop, il a des dépendances sur d'autres bibliothèques Hadoop comme HDFS et YARN. La version sans Hadoop est pour lorsque vous avez déjà des bibliothèques Hadoop fournies ailleurs.

#### **Utilisez le mode cluster autonome, pas Mesos ou YARN**

Une fois que vous avez testé les exemples intégrés sur le cluster `local`, et que vous avez vérifié que tout est installé et fonctionne correctement, procédez à la configuration de votre cluster.

Spark vous offre trois options : Mesos, YARN et autonome.

Les deux premières sont des allocateurs de ressources qui contrôlent vos nœuds réplicats. Spark doit leur demander d'allouer ses propres instances. En tant que débutant, n'augmentez pas votre complexité en allant dans cette voie.

Le cluster autonome est le plus facile à configurer. Il vient avec des paramètres par défaut sensés, comme l'utilisation de tous vos cœurs pour les exécutants. Il fait partie de la distribution Spark elle-même et dispose d'un script `sbin/start-all.sh` qui peut démarrer le primaire ainsi que tous vos réplicats listés dans `conf/slaves` en utilisant ssh.

Mesos/YARN sont des programmes séparés qui sont utilisés lorsque votre cluster n'est pas seulement un cluster Spark. De plus, ils ne viennent pas avec des paramètres par défaut sensés : les exécutants n'utilisent pas tous les cœurs sur les réplicats sauf si cela est explicitement spécifié.

Vous avez également l'option d'un mode de haute disponibilité utilisant Zookeeper, qui maintient une liste de primaires de secours au cas où un primaire tomberait en panne. Si vous êtes un débutant, il est peu probable que vous gériez un cluster de mille nœuds où le risque de panne de nœud est significatif. Il est plus probable que vous configuriez un cluster sur une plateforme cloud gérée comme celle d'Amazon ou de Google, qui prend déjà en charge les pannes de nœuds.

#### Vous n'avez pas besoin de haute disponibilité avec une infrastructure cloud ou un petit cluster

J'avais mon cluster configuré dans un environnement hostile où des facteurs humains étaient responsables des pannes de courant et des nœuds hors réseau. (En gros, le laboratoire informatique de mon collège où des étudiants diligents éteignent la machine et des étudiants négligents débranchent les câbles LAN). Je pouvais encore m'en sortir sans haute disponibilité en choisissant soigneusement le nœud primaire. Vous n'auriez pas à vous en soucier.

#### Vérifiez la version de Java que vous utilisez pour exécuter Spark

Un aspect très important est la version de Java que vous utilisez pour exécuter Spark. Normalement, une version ultérieure de Java fonctionne avec quelque chose compilé pour des versions plus anciennes.

Mais avec le projet Jigsaw, la modularité a introduit une isolation et des frontières plus strictes dans Java 9, ce qui brise certaines choses qui utilisent la réflexion. Sur Spark 2.3.0 s'exécutant sur Java 9, j'ai obtenu un accès à la réflexion illégal. Java 8 n'avait aucun problème.

Cela changera certainement dans un avenir proche, mais gardez cela à l'esprit jusqu'à ce moment-là.

#### Spécifiez l'URL du primaire exactement telle quelle. Ne résolvez pas les noms de domaine en adresses IP, ou vice-versa

Le cluster autonome est très sensible aux URL utilisées pour résoudre les nœuds primaires et réplicats. Supposons que vous démarriez le nœud primaire comme ci-dessous :

```
> sbin/start-master.sh 
```

et votre primaire est disponible à `localhost:8080`

![Image](https://cdn-media-1.freecodecamp.org/images/0*_dPwEaOa1Sf6C5sB.png)

Par défaut, le nom d'hôte de votre PC est choisi comme adresse URL du primaire. `x360` se résout en `localhost`, mais démarrer un réplicat comme ci-dessous **ne fonctionnera pas**.

```
# ne fonctionne pas > sbin/start-slave.sh spark://localhost:7077 
```

```
# fonctionne > sbin/start-slave.sh spark://x360:7077
```

Cela fonctionne, et notre réplicat a été ajouté au cluster :

![Image](https://cdn-media-1.freecodecamp.org/images/0*rPOG-Z-x_sAhSDRB.png)

Notre réplicat a une adresse IP dans le sous-domaine 172.17.x.x, qui est en fait le sous-domaine configuré par Docker sur ma machine.

Le primaire peut communiquer avec ce réplicat car les deux sont sur la même machine. Mais le réplicat ne peut pas communiquer avec d'autres réplicats sur le réseau, ou un primaire sur une machine différente, car son adresse IP n'est pas routable.

Comme dans le cas du primaire ci-dessus, un réplicat sur une machine sans primaire prendra le nom d'hôte de la machine. Lorsque vous avez des machines identiques, elles finissent toutes par utiliser le même nom d'hôte comme adresse. Cela crée un véritable désordre et personne ne peut communiquer avec l'autre.

Donc les commandes ci-dessus changeraient en :

```
# démarrer le maître > sbin/start-master.sh -h $myIP # démarrer l'esclave > sbin/start-slave.sh -h $myIP spark://<masterIP>:7077 # soumettre un travail > SPARK_LOCAL_IP=$myIP bin/spark-submit ...
```

où `myIP` est l'adresse IP de la machine qui est routable entre les nœuds du cluster. Il est plus probable que tous les nœuds soient sur le même réseau, donc vous pouvez écrire un script qui définira `myIP` sur chaque machine.

```
# supposer que tous les nœuds sont dans le sous-domaine 10.1.26.x siddhesh@master:~$ myIP=`hostname -I | tr " " "\n" | grep 10.1.26. | head`
```

### Flux du code

Jusqu'à présent, nous avons configuré notre cluster et vu qu'il est fonctionnel. Maintenant, il est temps de coder. Spark est assez bien documenté et vient avec de nombreux exemples, donc il est très facile de commencer à coder. Ce qui est moins évident, c'est comment tout cela fonctionne, ce qui entraîne des erreurs très difficiles à déboguer pendant l'exécution. Supposons que vous avez codé quelque chose comme ceci :

```
class SomeClass {  static SparkSession spark;  static LongAccumulator numSentences; 
```

```
 public static void main(String[] args) {    spark = SparkSession.builder()                        .appName("Sparkl")                       .getOrCreate(); (1)    numSentences = spark.sparkContext()                       .longAccumulator("sentences"); (2)    spark.read()        .textFile(args[0])        .foreach(SomeClass::countSentences); (3)  }  static void countSentences(String s) { numSentences.add(1); } (4) }
```

**1** créer une session spark

**2** créer un compteur long pour suivre la progression du travail

**3** parcourir un fichier ligne par ligne en appelant countSentences pour chaque ligne

**4** ajouter 1 à l'accumulateur pour chaque phrase

Le code ci-dessus fonctionne sur un cluster `local` mais échouera avec une exception de pointeur nul lorsqu'il est exécuté sur un cluster multinœud. `spark` ainsi que `numSentences` seront nuls sur la machine réplicat.

Pour résoudre ce problème, encapsulez tous les états initialisés dans des champs non statiques d'un objet. Utilisez `main` pour créer l'objet et reportez le traitement ultérieur à celui-ci.

Ce que vous devez comprendre, c'est que le code que vous écrivez est exécuté par le nœud pilote tel quel, mais ce que les nœuds réplicats exécutent est un travail sérialisé que Spark leur donne. Vos classes seront chargées par la JVM sur le réplicat.

Les initialisateurs statiques s'exécuteront comme prévu, mais des fonctions comme `main` ne le feront pas, donc les valeurs statiques initialisées dans le pilote ne seront pas vues dans le réplicat. Je ne suis pas sûr de savoir comment tout cela fonctionne, et je ne fais que déduire de l'expérience, donc prenez mon explication avec des pincettes. Votre code ressemble maintenant à ceci :

```
class SomeClass {  SparkSession spark; (1)  LongAccumulator numSentences;  String[] args;   SomeClass(String[] args) { this.args = args; }   public static void main(String[] args){    new SomeClass(args).process(); (2)  }   void process() {    spark = SparkSession.builder().appName("Sparkl").getOrCreate();   numSentences = spark.sparkContext().longAccumulator("sentences");   spark.read().textFile(args[0]).foreach(this::countSentences); (3) }  void countSentences(String s) { numSentences.add(1); }}
```

**1** Rendre les champs non statiques

**2** créer une instance de la classe puis exécuter les travaux spark

**3** la référence à `this` dans la lambda foreach amène l'objet dans la fermeture des objets accessibles et est ainsi sérialisé et envoyé à tous les réplicats.

Ceux d'entre vous qui programmez en Scala pourraient utiliser des objets Scala qui sont des classes singleton et n'auront donc peut-être jamais ce problème. Néanmoins, c'est quelque chose que vous devriez savoir.

### Soumettre l'application et les dépendances

Il y a plus à coder ci-dessus, mais avant cela, vous devez soumettre votre application au cluster. À moins que votre application ne soit extrêmement triviale, il est probable que vous utilisiez des bibliothèques externes.

Lorsque vous soumettez votre jar d'application, vous devez également indiquer à Spark les bibliothèques dépendantes que vous utilisez, afin qu'il les rende disponibles sur tous les nœuds. C'est assez simple. La syntaxe est :

```
bin/spark-submit --packages groupId:artifactId:version,...
```

Je n'ai eu aucun problème avec ce schéma. Cela fonctionne sans faille. Je développe généralement sur mon ordinateur portable, puis je soumets des travaux à partir d'un nœud du cluster. Donc, je dois transférer l'application et ses dépendances vers le nœud auquel je me connecte via ssh.

Spark recherche les dépendances dans le dépôt maven local, puis dans le dépôt central et dans les dépôts que vous spécifiez à l'aide de l'option `--repositories`. Il est un peu fastidieux de synchroniser tout cela sur le pilote, puis de taper toutes ces dépendances sur la ligne de commande. Je préfère donc que toutes les dépendances soient packagées dans un seul jar, appelé un uber jar.

#### **Utilisez le plugin Maven shade pour générer un uber jar avec toutes les dépendances afin de faciliter la soumission des travaux**

Il suffit d'inclure les lignes suivantes dans votre `pom.xml`

```
<build> <plugins>  <plugin>   <groupId>org.apache.maven.plugins</groupId>   <artifactId>maven-shade-plugin</artifactId   <version>3.0.0</version>   <configuration>    <artifactSet>     <excludes>      <exclude>org.apache.spark:*</exclude>     </excludes>    </artifactSet>   </configuration>   <executions>    <execution>     <phase>package</phase>     <goals>      <goal>shade</goal>     </goals>    </execution>   </executions>  </plugin> </plugins> </build>
```

Lorsque vous construisez et packagez votre projet, le jar de distribution par défaut inclura toutes les dépendances.

Lorsque vous soumettez des travaux, les jars d'application s'accumulent dans le répertoire `work` et se remplissent avec le temps.

Définissez `spark.worker.cleanup.enabled` sur true dans `conf/spark-defaults.conf`

Cette option est false par défaut et s'applique au mode autonome.

### Fichiers d'entrée et de sortie

C'était la partie la plus confuse et difficile à diagnostiquer.

Spark supporte la lecture/écriture de diverses sources telles que `hdfs`, `ftp`, `jdbc` ou des fichiers locaux sur le système lorsque le protocole est `file://` ou manquant. Ma première tentative était de lire à partir d'un fichier sur mon pilote. J'ai supposé que le pilote lirait le fichier, le transformerait en partitions, puis les distribuerait dans le cluster. Il s'avère que cela ne fonctionne pas de cette manière.

Lorsque vous lisez un fichier depuis le système de fichiers local, assurez-vous que le fichier est présent sur tous les nœuds travailleurs exactement au même endroit. Spark ne distribue pas implicitement les fichiers du pilote aux travailleurs.

J'ai donc dû copier le fichier sur chaque travailleur au même endroit. L'emplacement du fichier était passé en argument à mon application. Comme le fichier était situé dans le dossier parent, j'ai spécifié son chemin comme `../wikiArticles.txt`. Cela n'a pas fonctionné sur les nœuds travailleurs.

#### Passez toujours des chemins de fichiers absolus pour la lecture

Cela pourrait être une erreur de ma part, mais je sais que le chemin du fichier est arrivé tel quel dans la fonction `textFile` et cela a causé des erreurs de "fichier non trouvé".

Spark supporte les schémas de compression courants, donc la plupart des fichiers texte gzippés ou bzippés seront décompressés avant utilisation. Il pourrait sembler que les fichiers compressés soient plus efficaces, mais ne tombez pas dans ce piège.

#### Ne lisez pas à partir de fichiers texte compressés, surtout `gzip`. Les fichiers non compressés sont plus rapides à traiter.

Gzip ne peut pas être décompressé en parallèle comme bzip2, donc les nœuds passent la majeure partie de leur temps à décompresser de grands fichiers.

Il est fastidieux de rendre les fichiers d'entrée disponibles sur tous les travailleurs. Vous pouvez plutôt utiliser le mécanisme de diffusion de fichiers de Spark. Lorsque vous soumettez un travail, spécifiez une liste séparée par des virgules de fichiers d'entrée avec l'option `--files`. L'accès à ces fichiers nécessite `SparkFiles.get(filename)`. Je n'ai pas trouvé suffisamment de documentation sur cette fonctionnalité.

Pour lire un fichier diffusé avec l'option `--files`, utilisez `SparkFiles.get(<onlyFileNameNotFullPath>`) comme chemin dans les fonctions de lecture.

Ainsi, un fichier soumis comme `--files /opt/data/wikiAbstracts.txt` serait accessible via `SparkFiles.get("wikiAbstracts.txt")`. Cela retourne une chaîne que vous pouvez utiliser dans toute fonction de lecture qui attend un chemin. Encore une fois, n'oubliez pas de spécifier des chemins absolus.

Comme mon fichier d'entrée faisait 5 Go compressé, et que mon réseau était assez lent à 12 Mo/s, j'ai essayé d'utiliser la fonction de diffusion de fichiers de Spark. Mais la décompression elle-même prenait tellement de temps que j'ai copié manuellement le fichier sur chaque travailleur. Si votre réseau est suffisamment rapide, vous pouvez utiliser des fichiers non compressés. Ou alternativement, utilisez HDFS ou un serveur FTP.

L'écriture de fichiers suit également les sémantiques de la lecture. J'enregistrais mon DataFrame dans un fichier csv sur le système local. Encore une fois, j'avais l'hypothèse que les résultats seraient renvoyés au nœud pilote. Cela n'a pas fonctionné pour moi.

#### Lorsqu'un DataFrame est enregistré dans un chemin de fichier local, chaque travailleur enregistre ses partitions calculées sur son propre disque. Aucune donnée n'est renvoyée au pilote

Je n'obtenais qu'une fraction des résultats que j'attendais. Initialement, j'avais mal diagnostiqué ce problème comme une erreur dans mon code. Plus tard, j'ai découvert que chaque travailleur stockait ses résultats calculés sur son propre disque.

### Partitions

Le nombre de partitions que vous créez affecte les performances. Par défaut, Spark créera autant de partitions qu'il y a de cœurs dans le cluster. Ce n'est pas toujours optimal.

Surveillez le nombre de travailleurs qui traitent activement les tâches. S'il y en a trop peu, augmentez le nombre de partitions.

Si vous lisez à partir d'un fichier gzippé, Spark crée une seule partition qui sera traitée par un seul travailleur. C'est aussi une raison pour laquelle les fichiers gzippés sont lents à traiter. J'ai observé des performances plus lentes avec un petit nombre de grandes partitions par rapport à un grand nombre de petites partitions.

Il est préférable de définir explicitement le nombre de partitions lors de la lecture des données.

Vous n'aurez peut-être pas à faire cela lors de la lecture à partir de HDFS, car les fichiers Hadoop sont déjà partitionnés.

### Wikipedia et DBpedia

Il n'y a pas de _pièges_ ici, mais j'ai pensé qu'il serait bon de vous faire connaître les alternatives. Le dump XML complet de Wikipedia fait 14 Go compressé et 65 Go non compressé. La plupart du temps, vous ne voulez que le texte brut de l'article, mais le dump est au format MediaWiki, donc il nécessite un certain prétraitement. Il existe de nombreux outils disponibles pour cela dans divers langages. Bien que je ne les aie pas utilisés personnellement, je suis presque sûr que cela doit être une tâche chronophage. Mais il existe des alternatives.

Si tout ce que vous voulez est le texte brut des articles de Wikipedia, principalement pour le NLP, alors téléchargez le jeu de données mis à disposition par DBpedia.

J'ai utilisé le dump complet des articles (`NIF Context`) disponible sur [DBpedia](http://wiki.dbpedia.org/downloads-2016-10) (téléchargement direct depuis [ici](http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_context_en.ttl.bz2)). Ce jeu de données se débarrasse des éléments indésirables comme les tables, les infoboxes et les références. Le téléchargement compressé fait 4,3 Go au format `turtle`. Vous pouvez le convertir en `tsv` comme suit

Des jeux de données similaires sont disponibles pour d'autres propriétés comme les liens de page, les textes d'ancrage, etc. Consultez [DBpedia](https://dbpedia.org).

### Un mot sur les bases de données

Je n'ai jamais vraiment compris pourquoi il existe une pléthore de bases de données, toutes si similaires, et en plus de cela, les gens achètent des licences de bases de données. Jusqu'à ce projet, je n'avais pas sérieusement utilisé de bases de données. Je n'ai jamais utilisé que MySQL et Apache Derby.

Pour mon projet, j'ai utilisé une base de données de triples SPARQL, Apache Jena TDB, accessible via une API REST servie par Jena Fuseki. Cette base de données me fournirait des URL RDF, des étiquettes et des prédicats pour toutes les ressources mentionnées dans l'article fourni. Chaque nœud effectuerait un appel à la base de données et ne procéderait au traitement ultérieur qu'après cela.

Ma charge de travail était devenue liée aux E/S, car je pouvais voir une utilisation du CPU proche de 0 % sur les nœuds travailleurs. Chaque partition des données entraînerait deux requêtes SPARQL. Dans le pire des cas, l'une des deux requêtes prenait 500 à 1000 secondes à traiter. Heureusement, la base de données TDB repose sur la cartographie mémoire de Linux. Je pouvais mapper toute la base de données en RAM et améliorer considérablement les performances.

#### Si vous êtes limité par les E/S et que votre base de données peut tenir dans la RAM, exécutez-la en mémoire.

J'ai trouvé un outil appelé [vmtouch](https://hoytech.com/vmtouch/) qui montre quel pourcentage du répertoire de la base de données a été mappé en mémoire. Cet outil permet également de mapper explicitement des fichiers/répertoires en RAM et de les verrouiller éventuellement pour qu'ils ne soient pas paginés.

Ma base de données de 16 Go pouvait facilement tenir dans mon serveur de 32 Go de RAM. Cela a boosté les performances des requêtes de plusieurs ordres de grandeur à 1-2 secondes par requête. En utilisant une forme rudimentaire d'équilibrage de charge de la base de données basée sur le numéro de partition, j'ai pu réduire mon temps d'exécution de moitié en utilisant 2 serveurs SPARQL au lieu d'un.

### Conclusion

J'ai vraiment apprécié le calcul distribué sur Spark. Sans cela, je n'aurais pas pu terminer mon projet. Il était assez facile de prendre mon application existante et de la faire fonctionner sur Spark. Je recommanderais définitivement à quiconque de l'essayer.

_Publié à l'origine sur [siddheshrane.github.io](https://siddheshrane.github.io/processing-wikipedia-with-spark/index.html).