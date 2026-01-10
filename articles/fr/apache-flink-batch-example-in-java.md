---
title: Exemple de traitement par lots Apache Flink en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-09T23:27:00.000Z'
originalURL: https://freecodecamp.org/news/apache-flink-batch-example-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca8740569d1a4ca3379.jpg
tags:
- name: apache
  slug: apache
- name: Data Science
  slug: data-science
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Exemple de traitement par lots Apache Flink en Java
seo_desc: 'Flink Batch Example JAVA

  Apache Flink is an open source stream processing framework with powerful stream-
  and batch-processing capabilities.

  Prerequisites


  Unix-like environment (Linux, Mac OS X, Cygwin)

  git

  Maven (we recommend version 3.0.4)

  Java 7 ...'
---

## **Exemple Flink Batch JAVA**

Apache Flink est un framework de traitement de flux open source avec des capacités puissantes de traitement de flux et de lots.

### **Prérequis**

* Environnement de type Unix (Linux, Mac OS X, Cygwin)
* git
* Maven (nous recommandons la version 3.0.4)
* Java 7 ou 8
* IntelliJ IDEA ou Eclipse IDE

```text
git clone https://github.com/apache/flink.git
cd flink
mvn clean package -DskipTests # cela peut prendre jusqu'à 10 minutes
```

## Jeux de données

Pour les données de traitement par lots, nous utiliserons les jeux de données disponibles ici : [datasets](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip). Dans cet exemple, nous utiliserons les fichiers movies.csv et ratings.csv. Créez un nouveau projet Java et placez-les dans un dossier à la base de l'application.

## Exemple

Nous allons créer une exécution où nous récupérons la note moyenne par genre de film de l'ensemble des données que nous avons.

### Environnement et jeux de données

Tout d'abord, créez un nouveau fichier Java, je vais le nommer AverageRating.java.

La première chose que nous allons faire est de créer l'environnement d'exécution et de charger les fichiers CSV dans un jeu de données. Comme ceci :

```text
ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
DataSet<Tuple3<Long, String, String>> movies = env.readCsvFile("ml-latest-small/movies.csv")
  .ignoreFirstLine()
  .parseQuotedStrings('"')
  .ignoreInvalidLines()
  .types(Long.class, String.class, String.class);

DataSet<Tuple2<Long, Double>> ratings = env.readCsvFile("ml-latest-small/ratings.csv")
  .ignoreFirstLine()
  .includeFields(false, true, true, false)
  .types(Long.class, Double.class);
```

Ici, nous créons un jeu de données avec un <Long, String, String> pour les films, en ignorant les erreurs, les guillemets et la ligne d'en-tête, et un jeu de données avec <Long, Double> pour les notes de films, en ignorant également l'en-tête, les lignes invalides et les guillemets.

### Traitement Flink

Ici, nous allons traiter le jeu de données avec Flink. Le résultat sera dans une liste de tuples String, Double, où le genre sera dans la String et la note moyenne sera dans le double.

Tout d'abord, nous allons joindre le jeu de données des notes avec le jeu de données des films par l'ID des films présent dans chaque jeu de données. Avec cela, nous allons créer un nouveau Tuple avec le nom du film, le genre et le score. Ensuite, nous regroupons ce tuple par genre et ajoutons le score de tous les genres égaux, enfin nous divisons le score par le nombre total de résultats et nous avons notre résultat souhaité.

```text
List<Tuple2<String, Double>> distribution = movies.join(ratings)
  .where(0)
  .equalTo(0)
  .with(new JoinFunction<Tuple3<Long, String, String>,Tuple2<Long, Double>, Tuple3<StringValue, StringValue, DoubleValue>>() {
    private StringValue name = new StringValue();
    private StringValue genre = new StringValue();
    private DoubleValue score = new DoubleValue();
    private Tuple3<StringValue, StringValue, DoubleValue> result = new Tuple3<>(name,genre,score);

    @Override
    public Tuple3<StringValue, StringValue, DoubleValue> join(Tuple3<Long, String, String> movie,Tuple2<Long, Double> rating) throws Exception {
      name.setValue(movie.f1);
      genre.setValue(movie.f2.split("\\|")[0]);
      score.setValue(rating.f1);
      return result;
    }
})
  .groupBy(1)
  .reduceGroup(new GroupReduceFunction<Tuple3<StringValue,StringValue,DoubleValue>, Tuple2<String, Double>>() {
    @Override
    public void reduce(Iterable<Tuple3<StringValue,StringValue,DoubleValue>> iterable, Collector<Tuple2<String, Double>> collector) throws Exception {
      StringValue genre = null;
      int count = 0;
      double totalScore = 0;
      for(Tuple3<StringValue,StringValue,DoubleValue> movie: iterable){
        genre = movie.f1;
        totalScore += movie.f2.getValue();
        count++;
      }

      collector.collect(new Tuple2<>(genre.getValue(), totalScore/count));
    }
})
  .collect();
```

Avec cela, vous aurez une application Flink de traitement par lots fonctionnelle. Profitez-en !