---
title: Comment lire et écrire des fichiers profondément partitionnés avec Apache Spark
subtitle: ''
author: Arun Shanmugam Kumar
co_authors: []
series: null
date: '2025-08-31T21:23:23.426Z'
originalURL: https://freecodecamp.org/news/how-to-read-and-write-deeply-partitioned-files-using-apache-spark
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756671369152/1e620925-6fb6-47fa-8344-86b9d3c7cd02.png
tags:
- name: '#apache-spark'
  slug: apache-spark
- name: Scala
  slug: scala
- name: big data
  slug: big-data
seo_title: Comment lire et écrire des fichiers profondément partitionnés avec Apache
  Spark
seo_desc: 'If you use Apache Spark to write your data pipeline, you might need to
  export or copy data from a source to destination while preserving the partition
  folders between the source and destination.

  When I researched online on how to do this in Spark, I ...'
---

Si vous utilisez Apache Spark pour construire votre pipeline de données, vous pourriez avoir besoin d'exporter ou de copier des données d'une source vers une destination tout en préservant les dossiers de partition entre la source et la destination.

Quand j'ai fait des recherches en ligne sur la manière de faire cela dans Spark, j'ai trouvé très peu de tutoriels proposant une solution de bout en bout qui fonctionnait – surtout quand les partitions sont profondément imbriquées et que vous ne connaissez pas à l'avance les valeurs que prendront ces noms de dossiers (par exemple `year=*/month=*/day=*/hour=*/*.csv`).

Dans ce tutoriel, j'ai fourni une telle implémentation utilisant Spark.

### Voici ce que nous allons aborder :

* [Prérequis](#heading-prerequis)
    
* [Installation](#heading-installation)
    
* [Fausses pistes](#heading-fausses-pistes)
    
* [Ma solution](#heading-ma-solution)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce tutoriel, vous devez avoir une compréhension de base de l'informatique distribuée utilisant des Frameworks comme Hadoop et Spark, ainsi que du code programmé dans des langages orientés objet comme Scala/Java. Le code est testé avec les dépendances ci-dessous :

* Scala 2.12+
    
* Java 17 (des versions antérieures pourraient fonctionner)
    
* Sbt
    

## Installation

Je suppose que vous avez des dossiers de partition créés à la source avec le modèle ci-dessous (qui est un format de colonne de partition standard impliquant la date et l'heure) :

`year/month/day/hour`

Crucialement, comme je l'ai mentionné plus haut, je suppose que vous ne connaissez pas le nom complet des dossiers – sauf qu'ils contiennent un certain motif de préfixe constant.

## Fausses pistes

1. Si vous envisagez d'utiliser les options `recursiveFileLookup` et `pathGlobFilter` lors de la lecture et de l'écriture, cela ne fonctionne pas vraiment, car les fonctions ci-dessus ne sont disponibles que sur l'API de lecture.
    
2. Si vous envisagez de paramétrer la lecture et l'écriture en fonction de toutes les combinaisons possibles année/mois/jour/heure et d'ignorer l'exportation si le dossier de partition correspondant n'est pas trouvé, cela pourrait fonctionner mais ne serait pas très efficace.
    

## Ma solution

Après quelques essais et erreurs et des recherches sur Stack Overflow et dans la documentation Spark, j'ai eu l'idée d'utiliser une combinaison des API `input_file_name()`, `regexp_extract()`, et `partitionBy()` du côté de l'écriture pour atteindre l'objectif final. Vous trouverez ci-dessous un exemple de code basé sur Scala :

```scala
package main.scala.blog

/**
*  Exemple de code Spark stream pour lire et écrire depuis un dossier partitionné
*  vers un dossier partitionné sans date-heure explicitement connue.
*/

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.StringType
import org.apache.spark.sql.functions.{udf, input_file_name, col, lit, regexp_extract}

object PartitionedReaderWriter {

    def main(args: Array[String]) {
        // 1.
        val spark = SparkSession
                    .builder
                    .appName("PartitionedReaderWriterApp")
                    .getOrCreate()

        val sourceBasePath = "data/partitioned_files_source/user"
        // 2.
        val sourceDf = spark.read
                            .format("csv")
                            .schema("State STRING, Color STRING, Count INT")
                            .option("header", "true")
                            .option("pathGlobFilter", "*.csv")
                            .option("recursiveFileLookup", "true")
                            .load(sourceBasePath)

        val destinationBasePath = "data/partitioned_files_destination/user"
        // 3.
        val writeDf = sourceDf
                        .withColumn("year", regexp_extract(input_file_name(), "year=(\\d{4})", 1))
                        .withColumn("month", regexp_extract(input_file_name(), "month=(\\d{2})", 1))
                        .withColumn("day", regexp_extract(input_file_name(), "day=(\\d{2})", 1))
                        .withColumn("hour", regexp_extract(input_file_name(), "hour=(\\d{2})", 1))

        // 4.
        writeDf.write
                .format("csv")
                .option("header", "true")
                .mode("overwrite")
                .partitionBy("year", "month", "day", "hour")
                .save(destinationBasePath)

        // 5.
        spark.stop()        
    }
}  
```

Voici ce qui se passe dans le code ci-dessus :

1. À l'intérieur de la méthode main, vous commencez par ajouter le code d'initialisation de Spark pour créer une session Spark.
    
2. Vous lisez les données depuis `sourceBasePath` en utilisant l'API Spark `read()` avec le format `csv` (vous pouvez également fournir le schéma en option). Les options `recursiveFileLookup` et `pathGlobFilter` sont nécessaires respectivement pour lire récursivement à travers les dossiers imbriqués et pour spécifier n'importe quel fichier `csv`.
    
3. La section suivante contient la logique principale où vous pouvez utiliser `input_file_name()` pour renvoyer le chemin complet du fichier et `regexp_extract()` pour extraire `year`, `month`, `day`, et `hour` des sous-dossiers correspondants dans le chemin et les stocker en tant que colonnes auxiliaires dans le dataframe.
    
4. Enfin, vous écrivez le dataframe en utilisant à nouveau le format `csv` et, surtout, vous utilisez `partitionBy` pour spécifier les colonnes auxiliaires précédemment créées comme colonnes de partition. Ensuite, enregistrez le dataframe dans le `destinationBasePath`.
    
5. Une fois la copie terminée, vous arrêtez la session Spark en appelant l'API `stop()`.
    

## Conclusion

Dans cet article, je vous ai montré comment exporter / copier des fichiers de données profondément imbriqués d'une source vers une destination en utilisant Apache Spark de manière efficace. J'espère que vous le trouverez utile !

Vous pouvez lire mes autres articles sur [https://www.beyonddream.me.](https://www.beyonddream.me/post-1/)