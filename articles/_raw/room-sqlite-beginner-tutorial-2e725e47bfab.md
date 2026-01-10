---
title: A Beginner’s Guide to the Room Persistence Library
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
seo_title: null
seo_desc: 'By Ajin Augustine

  It’s not a difficult task for an Android developer to convert raw data into a structured
  database for internal storage. This is done using the most reliable language — SQL.
  The inbuilt SQLite core library is within the Android OS. I...'
---

By Ajin Augustine

It’s not a difficult task for an Android developer to convert raw data into a structured database for internal storage. This is done using the most reliable language — SQL. The inbuilt SQLite core library is within the Android OS. It will handle CRUD (Create, Read, Update and Delete) operations required for a database. Java classes and interfaces for SQLite are provided by the android.database. SQLite maintains an effective database management system. But this conventional method has its own disadvantages.

* You have to write long repetitive code, which will be time-consuming as well as prone to mistakes.
* It is very difficult to manage SQL queries for a complex relational database.

To overcome this, Google has introduced Room Persistence Library. This acts as an abstraction layer for the existing SQLite APIs. All the required packages, parameters, methods, and variables are imported into an Android project by using simple annotations.

![Image](https://cdn-media-1.freecodecamp.org/images/XoUsalA8v-rQhUsBaaYGQoRXkFtgxWDH-gI8)
_Annotations in Room Persistence Library_

Let’s have a look at how to implement this with an example.

1. Add the gradle dependencies in the build.gradle file.

```
implementation “android.arch.persistence.room:runtime:1.0.0”annotationProcessor “android.arch.persistence.room:compiler:1.0.0”
```

2. Create a data model class for the database table and annotate its table name and primary key.

```
@Entity public class Movies { @NonNull @PrimaryKey private String movieId; private String movieName;  public Movies() { }  public String getMovieId() { return movieId; } public void setMovieId(String movieId) { this.movieId = movieId; } public String getMovieName() { return movieName; } public void setMovieName (String movieName) { this.movieName = movieName; } }
```

3. Create an interface class for Database access. Create abstract methods for CRUD operations. Add custom SQL query as a method.

```
@Dao public interface DaoAccess {  @Insert void insertOnlySingleMovie (Movies movies); @Insert void insertMultipleMovies (List<Movies> moviesList); @Query (“SELECT * FROM Movies WHERE movieId = :movieId“) Movies fetchOneMoviesbyMovieId (int movieId); @Update void updateMovie (Movies movies); @Delete void deleteMovie (Movies movies); }
```

4. Create a Database class for database implementation.

```
@Database (entities = {Movies.class}, version = 1, exportSchema = false) public abstract class MovieDatabase extends RoomDatabase { public abstract DaoAccess daoAccess() ; }
```

5.Declare and initialize an object for the Database class in your Activity or Fragment class.

```
private static final String DATABASE_NAME = “movies_db”; private MovieDatabase movieDatabase; movieDatabase = Room.databaseBuilder(getApplicationContext(), MovieDatabase.class, DATABASE_NAME) .fallbackToDesctructiveMigration() .build();
```

The initial steps are done. By using the database object, you can do all functionalities for database management.

Sample Insert code:

```
new Thread(new Runnable() { @Override public void run() { Movies movie =new Movies(); movie.setMovieId( “2”); movie.setMovieName(“The Prestige”); movieDatabase.daoAccess () . insertOnlySingleMovie (movie); } }) .start();
```

Always use a Thread, AsyncTask, or any worker threads to perform database operations.

For further information, please check out:

[https://developer.android.com/training/data-storage/room/index.html](https://developer.android.com/training/data-storage/room/index.html)

Experience seamless coding now that there’s ROOM for improvement!

_Originally published at [thinkpalm.com](http://thinkpalm.com/blogs/beginners-guide-room-persistence-library/)._

