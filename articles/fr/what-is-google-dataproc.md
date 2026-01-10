---
title: Comment utiliser Google Dataproc – Exemple avec PySpark et Jupyter Notebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-03T15:14:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-google-dataproc
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/My-project.jpg
tags:
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: hadoop
  slug: hadoop
- name: Machine Learning
  slug: machine-learning
- name: spark
  slug: spark
seo_title: Comment utiliser Google Dataproc – Exemple avec PySpark et Jupyter Notebook
seo_desc: "By Sameer Shukla\nIn this article, I'll explain what Dataproc is and how\
  \ it works. \nDataproc is a Google Cloud Platform managed service for Spark and\
  \ Hadoop which helps you with Big Data Processing, ETL, and Machine Learning. It\
  \ provides a Hadoop clus..."
---

Par Sameer Shukla

Dans cet article, je vais expliquer ce qu'est Dataproc et comment il fonctionne. 

Dataproc est un service géré de la plateforme Google Cloud pour Spark et Hadoop qui vous aide avec le traitement des Big Data, l'ETL et le Machine Learning. Il fournit un cluster Hadoop et prend en charge les outils de l'écosystème Hadoop comme Flink, Hive, Presto, Pig et Spark.

Dataproc est un cluster auto-scalable qui gère la journalisation, la surveillance, la création de clusters de votre choix et l'orchestration des jobs. Vous devrez provisionner manuellement le cluster, mais une fois le cluster provisionné, vous pouvez soumettre des jobs à Spark, Flink, Presto et Hadoop.

Dataproc a une intégration implicite avec d'autres produits GCP comme Compute Engine, Cloud Storage, Bigtable, BigQuery, Cloud Monitoring, et ainsi de suite. Les jobs pris en charge par Dataproc sont MapReduce, Spark, PySpark, SparkSQL, SparkR, Hive et Pig.

En outre, Dataproc permet également une intégration native avec les Jupyter Notebooks, que nous aborderons plus tard dans cet article.

Dans cet article, nous allons couvrir :

1. Les types de clusters Dataproc et comment configurer Dataproc
2. Comment soumettre un job PySpark à Dataproc
3. Comment créer une instance de Notebook et exécuter des jobs PySpark via Jupyter Notebook.

## Comment créer un cluster Dataproc

Dataproc propose trois types de clusters :

1. Standard
2. Nœud unique
3. Haute disponibilité

Le cluster Standard peut se composer de 1 maître et de N nœuds travailleurs. Le Nœud unique n'a qu'un seul maître et 0 nœud travailleur. Pour des fins de production, vous devriez utiliser le cluster Haute disponibilité qui possède 3 maîtres et N nœuds travailleurs. 

Pour nos besoins d'apprentissage, un cluster à nœud unique est suffisant, avec seulement 1 nœud maître.

La création de clusters Dataproc dans GCP est simple. Tout d'abord, nous devons activer Dataproc, puis nous pourrons créer le cluster.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-185.png)
_Démarrer la création du cluster Dataproc_

Lorsque vous cliquez sur "Créer un cluster", GCP vous donne l'option de sélectionner le type de cluster, le nom du cluster, l'emplacement, les options de mise à l'échelle automatique, et plus encore.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-199.png)
_Paramètres requis pour le cluster_

Puisque nous avons sélectionné l'option Cluster à nœud unique, cela signifie que la mise à l'échelle automatique est désactivée car le cluster ne se compose que d'un seul nœud maître. 

L'option Configurer les nœuds nous permet de sélectionner le type de famille de machines comme Optimisé pour le calcul, GPU et Usage général. 

Dans ce tutoriel, nous utiliserons l'option de machine à usage général. Grâce à cela, vous pouvez sélectionner le type de machine, la taille du disque principal et les options de type de disque.

Le type de machine que nous allons sélectionner est n1-standard-2 qui possède 2 CPU et 7,5 Go de mémoire. La taille du disque principal est de 100 Go, ce qui est suffisant pour notre démonstration ici.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-200.png)
_Configuration du nœud maître_

Nous avons sélectionné le type de cluster à nœud unique, c'est pourquoi la configuration ne comprend qu'un nœud maître. Si vous sélectionnez un autre type de cluster, vous devrez également configurer le nœud maître et les nœuds travailleurs.

À partir de l'option Personnaliser le cluster, sélectionnez la configuration réseau par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-201.png)

Utilisez l'option "Suppression planifiée" au cas où aucun cluster ne serait nécessaire à un moment précis dans le futur (ou disons après quelques heures, jours ou minutes).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/5_ml_resize_x2_colored_toned_light_ai-1.jpg)
_Paramètre de suppression planifiée_

Ici, nous avons défini le "Timeout" à 2 heures, donc le cluster sera automatiquement supprimé après 2 heures.

Nous utiliserons l'option de sécurité par défaut qui est une clé de chiffrement gérée par Google. Lorsque vous cliquez sur "Créer", il commencera à créer le cluster. 

Vous pouvez également créer le cluster en utilisant la commande 'gcloud' que vous trouverez dans l'option 'EQUIVALENT COMMAND LINE' comme montré dans l'image ci-dessous. 

Et vous pouvez créer un cluster en utilisant une requête POST que vous trouverez dans l'option 'Equivalent REST'.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-203.png)
_Option gcloud et REST pour la création de cluster_

Après quelques minutes, le cluster avec 1 nœud maître sera prêt à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-204.png)
_Cluster opérationnel_

Vous pouvez trouver des détails sur les instances de VM si vous cliquez sur "Nom du cluster" :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-205.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-206.png)

## Comment soumettre un job PySpark

Comprenons brièvement comment fonctionne un job PySpark avant d'en soumettre un à Dataproc. C'est un job simple qui consiste à identifier les éléments distincts d'une liste contenant des éléments dupliqués. 

```python
#! /usr/bin/python

import pyspark

#Créer une liste
numbers = [1,2,1,2,3,4,4,6]

#SparkContext
sc = pyspark.SparkContext()

# Création d'un RDD en utilisant la méthode parallelize de SparkContext
rdd = sc.parallelize(numbers)

# Retourne les éléments distincts du RDD
distinct_numbers = rdd.distinct().collect()

#Imprimer
print('Nombres distincts :', distinct_numbers)
```

Téléchargez le fichier .py dans le bucket GCS, et nous aurons besoin de sa référence lors de la configuration du job PySpark.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-21.png)
_Emplacement du job GCS_

Soumettre des jobs dans Dataproc est simple. Vous devez simplement sélectionner l'option "Soumettre un job" :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-209.png)
_Soumission de job_

Pour soumettre un job, vous devrez fournir l'ID du job qui est le nom du job, la région, le nom du cluster (qui sera le nom du cluster, "first-data-proc-cluster"), et le type de job qui sera PySpark.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-223.png)
_Paramètres requis pour la soumission de job_

Vous pouvez obtenir l'emplacement du fichier Python à partir du bucket GCS où le fichier Python est téléchargé – vous le trouverez à l'URI gsutil.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-24.png)

Aucun autre paramètre supplémentaire n'est requis, et nous pouvons maintenant soumettre le job :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-224.png)

Après l'exécution, vous devriez pouvoir trouver les nombres distincts dans les logs :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-213.png)
_Logs_

## Comment créer une instance de Jupyter Notebook

Vous pouvez associer une instance de notebook à Dataproc Hub. Pour ce faire, GCP provisionne un cluster pour chaque instance de Notebook. Nous pouvons exécuter des jobs de type PySpark et SparkR à partir du notebook. 

Pour créer un notebook, utilisez l'option "Workbench" comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-26.png)

Assurez-vous de passer par les configurations habituelles comme le nom du Notebook, la région, l'environnement (Dataproc Hub) et la configuration de la machine (nous utilisons 2 vCPU avec 7,5 Go de RAM). Nous utilisons les paramètres réseau par défaut, et dans la section Autorisations, sélectionnez l'option "Compte de service".

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-225.png)
_Paramètres requis pour la création du cluster Notebook_

Cliquez sur Créer :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-216.png)
_Cluster Notebook opérationnel_

L'option "OUVRIR JUPYTERLAB" permet aux utilisateurs de spécifier les options de cluster et la zone pour leur notebook.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-226.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-227.png)

Une fois le provisionnement terminé, le Notebook vous propose quelques options de noyau :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-27.png)

Cliquez sur PySpark, ce qui vous permettra d'exécuter des jobs via le Notebook.

Une instance SparkContext sera déjà disponible, vous n'avez donc pas besoin de créer explicitement SparkContext. À part cela, le programme reste le même.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-220.png)
_Extrait de code sur le Notebook_

## Conclusion

Travailler sur Spark et Hadoop devient beaucoup plus facile lorsque vous utilisez GCP Dataproc. Le meilleur aspect est que vous pouvez créer un cluster de notebook, ce qui simplifie le développement.