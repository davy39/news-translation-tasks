---
title: Un aperçu rapide du Framework Apache Hadoop
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-quick-overview-of-the-apache-hadoop-framework
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d24740569d1a4ca3622.jpg
tags:
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: hadoop
  slug: hadoop
- name: toothbrush
  slug: toothbrush
seo_title: Un aperçu rapide du Framework Apache Hadoop
seo_desc: Hadoop, now known as Apache Hadoop, was named after a toy elephant that
  belonged to co-founder Doug Cutting’s son. Doug chose the name for the open-source
  project as it was easy to spell, pronounce, and find in search results. The original
  yellow stu...
---

Hadoop, maintenant connu sous le nom d'Apache Hadoop, a été nommé d'après un éléphant en peluche qui appartenait au fils du co-fondateur Doug Cutting. Doug a choisi ce nom pour le projet open-source car il était facile à épeler, à prononcer et à trouver dans les résultats de recherche. L'éléphant en peluche jaune original qui a inspiré le nom apparaît dans le logo de Hadoop.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1200px-Hadoop_logo_new.svg.png)

## Qu'est-ce qu'Apache Hadoop ?

> La bibliothèque logicielle Apache Hadoop est un framework qui permet le traitement distribué de grands ensembles de données sur des clusters d'ordinateurs en utilisant des modèles de programmation simples. Il est conçu pour évoluer de serveurs uniques à des milliers de machines, chacune offrant un calcul et un stockage locaux. Plutôt que de compter sur le matériel pour fournir une haute disponibilité, la bibliothèque elle-même est conçue pour détecter et gérer les défaillances au niveau de l'application, offrant ainsi un service hautement disponible sur un cluster d'ordinateurs, chacun pouvant être sujet à des défaillances.  
>   
> Source : [Apache Hadoop](https://hadoop.apache.org/)

En 2003, Google a publié son article sur le Google File System (GFS). Il détaillait un système de fichiers distribué propriétaire destiné à fournir un accès efficace à de grandes quantités de données en utilisant du matériel standard. Un an plus tard, Google a publié un autre article intitulé « MapReduce : Simplified Data Processing on Large Clusters ». À l'époque, Doug travaillait chez Yahoo. Ces articles ont été l'inspiration pour son projet open-source Apache Nutch. En 2006, les composants du projet alors connus sous le nom de Hadoop ont été séparés d'Apache Nutch et ont été publiés.

## Pourquoi Hadoop est-il utile ?

Chaque jour, des milliards de gigaoctets de données sont créés sous diverses formes. Voici quelques exemples de données fréquemment créées :

* Métadonnées d'utilisation de téléphone
* Journaux de sites web
* Transactions d'achat par carte de crédit
* Publications sur les réseaux sociaux
* Vidéos
* Informations recueillies à partir de dispositifs médicaux

Les « big data » désignent des ensembles de données trop volumineux ou trop complexes pour être traités avec des applications logicielles traditionnelles. Les facteurs qui contribuent à la complexité des données sont la taille de l'ensemble de données, la vitesse des processeurs disponibles et le format des données.

Au moment de sa sortie, Hadoop était capable de traiter des données à une échelle plus grande que les logiciels traditionnels.

### **Core Hadoop**

Les données sont stockées dans le Hadoop Distributed File System (HDFS). En utilisant map reduce, Hadoop traite les données en morceaux parallèles (traitement de plusieurs parties en même temps) plutôt que dans une seule file d'attente. Cela réduit le temps nécessaire pour traiter de grands ensembles de données.

HDFS fonctionne en stockant de grands fichiers divisés en morceaux et en les répliquant sur de nombreux serveurs. Avoir plusieurs copies de fichiers crée une redondance, ce qui protège contre la perte de données.

### **Écosystème Hadoop**

De nombreux autres logiciels existent pour compléter Hadoop. Ces programmes constituent l'écosystème Hadoop. Certains programmes facilitent le chargement des données dans le cluster Hadoop, tandis que d'autres rendent Hadoop plus facile à utiliser.

L'écosystème Hadoop comprend :

* Apache Hive
* Apache Pig
* Apache HBase
* Apache Phoenix
* Apache Spark
* Apache ZooKeeper
* Cloudera Impala
* Apache Flume
* Apache Sqoop
* Apache Oozie

## Plus d'informations :

* [Apache Hadoop](http://hadoop.apache.org/)