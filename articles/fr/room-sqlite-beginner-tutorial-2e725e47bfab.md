---
title: Un guide pour débutants sur la bibliothèque Room Persistence
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T11:15:01.000Z'
originalURL: https://freecodecamp.org/news/room-sqlite-beginner-tutorial-2e725e47bfab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vy2KApBboWCZQoxLSgsWhQ.jpeg
tags:
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide pour débutants sur la bibliothèque Room Persistence
seo_desc: 'By Ajin Augustine

  It’s not a difficult task for an Android developer to convert raw data into a structured
  database for internal storage. This is done using the most reliable language — SQL.
  The inbuilt SQLite core library is within the Android OS. I...'
---

Par Ajin Augustine

Ce n'est pas une tâche difficile pour un développeur Android de convertir des données brutes en une base de données structurée pour le stockage interne. Cela se fait en utilisant le langage le plus fiable — SQL. La bibliothèque principale SQLite intégrée se trouve dans le système d'exploitation Android. Elle gérera les opérations CRUD (Create, Read, Update et Delete) requises pour une base de données. Les classes et interfaces Java pour SQLite sont fournies par android.database. SQLite maintient un système de gestion de base de données efficace. Mais cette méthode conventionnelle a ses propres inconvénients.

* Vous devez écrire un long code répétitif, ce qui sera chronophage ainsi que sujet à des erreurs.
* Il est très difficile de gérer les requêtes SQL pour une base de données relationnelle complexe.

Pour surmonter cela, Google a introduit la bibliothèque Room Persistence. Celle-ci agit comme une couche d'abstraction pour les API SQLite existantes. Tous les packages, paramètres, méthodes et variables requis sont importés dans un projet Android en utilisant des annotations simples.

![Image](https://cdn-media-1.freecodecamp.org/images/XoUsalA8v-rQhUsBaaYGQoRXkFtgxWDH-gI8)
_Annotations dans la bibliothèque Room Persistence_

Examinons comment implémenter cela avec un exemple.

1. Ajoutez les dépendances gradle dans le fichier build.gradle.

```
implementation "android.arch.persistence.room:runtime:1.0.0"
annotationProcessor "android.arch.persistence.room:compiler:1.0.0"
```

2. Créez une classe de modèle de données pour la table de la base de données et annotez son nom de table et sa clé primaire.

```
@Entity public class Movies { @NonNull @PrimaryKey private String movieId; private String movieName;  public Movies() { }  public String getMovieId() { return movieId; } public void setMovieId(String movieId) { this.movieId = movieId; } public String getMovieName() { return movieName; } public void setMovieName (String movieName) { this.movieName = movieName; } }
```

3. Créez une classe d'interface pour l'accès à la base de données. Créez des méthodes abstraites pour les opérations CRUD. Ajoutez une requête SQL personnalisée en tant que méthode.

```
@Dao public interface DaoAccess {  @Insert void insertOnlySingleMovie (Movies movies); @Insert void insertMultipleMovies (List<Movies> moviesList); @Query ("SELECT * FROM Movies WHERE movieId = :movieId") Movies fetchOneMoviesbyMovieId (int movieId); @Update void updateMovie (Movies movies); @Delete void deleteMovie (Movies movies); }
```

4. Créez une classe de base de données pour l'implémentation de la base de données.

```
@Database (entities = {Movies.class}, version = 1, exportSchema = false) public abstract class MovieDatabase extends RoomDatabase { public abstract DaoAccess daoAccess() ; }
```

5. Déclarez et initialisez un objet pour la classe de base de données dans votre classe Activity ou Fragment.

```
private static final String DATABASE_NAME = "movies_db"; private MovieDatabase movieDatabase; movieDatabase = Room.databaseBuilder(getApplicationContext(), MovieDatabase.class, DATABASE_NAME) .fallbackToDesctructiveMigration() .build();
```

Les étapes initiales sont terminées. En utilisant l'objet de base de données, vous pouvez effectuer toutes les fonctionnalités pour la gestion de la base de données.

Exemple de code d'insertion :

```
new Thread(new Runnable() { @Override public void run() { Movies movie =new Movies(); movie.setMovieId( "2"); movie.setMovieName("The Prestige"); movieDatabase.daoAccess () . insertOnlySingleMovie (movie); } }) .start();
```

Utilisez toujours un Thread, AsyncTask ou tout autre thread de travail pour effectuer des opérations sur la base de données.

Pour plus d'informations, veuillez consulter :

[https://developer.android.com/training/data-storage/room/index.html](https://developer.android.com/training/data-storage/room/index.html)

Expérimentez un codage fluide maintenant qu'il y a de la PLACE pour l'amélioration !

_Publié à l'origine sur [thinkpalm.com](http://thinkpalm.com/blogs/beginners-guide-room-persistence-library/)._