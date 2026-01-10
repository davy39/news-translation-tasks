---
title: Comment construire une API Rest avec Spring Boot en utilisant MySQL et JPA
subtitle: ''
author: Parathan Thiyagalingam
co_authors: []
series: null
date: '2019-03-15T16:25:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rest-api-with-spring-boot-using-mysql-and-jpa-f931e348734b
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca447740569d1a4ca6173.jpg
tags:
- name: Java
  slug: java
- name: MySQL
  slug: mysql
- name: General Programming
  slug: programming
- name: spring-boot
  slug: spring-boot
- name: 'tech '
  slug: tech
seo_title: Comment construire une API Rest avec Spring Boot en utilisant MySQL et
  JPA
seo_desc: 'Hi Everyone! For the past year, I have been learning JavaScript for full-stack
  web development. For a change, I started to master Java — the powerful Object Oriented
  Language.

  In that case, I found a very clean and elegant framework called Spring Boo...'
---

Bonjour à tous ! Au cours de l'année passée, j'ai appris JavaScript pour le développement web full-stack. Pour changer, j'ai commencé à maîtriser Java — le puissant langage orienté objet.

Dans ce cas, j'ai trouvé un framework très propre et élégant appelé Spring Boot pour construire un back-end.

Auparavant, dans le développement JavaScript, j'utilisais :

1. Mongoose — un ORM (Object Relational Mapping) pour Mongo DB
2. Sequelize — un ORM pour MySQL

Pour le développement lié à Java, il existe de nombreux ORM comme **Hibernate, JPA** (Java Persistence API) et **Java Object Oriented Querying**.

J'ai choisi de construire avec JPA qui est traditionnellement utilisé dans les applications Java.

C'était très intéressant, et cela a pris environ une semaine pour finir car j'ai dû apprendre Spring Boot (il y a beaucoup d'annotations « **@** » et d'autres choses cool à apprendre), JPA, et Hibernate en cours de route.

Toute cette magie est principalement réalisée par les **annotations** (symbole « **@** ») utilisées dans Spring Boot.

#### Création d'un projet Maven Spring Boot

Créons une application de projet Maven Spring Boot en utilisant ce [lien](https://start.spring.io/).

« **Maven** » est un outil de gestion de projet utilisé pour gérer la gestion des dépendances. C'est comme Node Package Manager (**NPM**) dans l'environnement de développement JS.

![Image](https://cdn-media-1.freecodecamp.org/images/YsUiOp9T6nTFMyBPE2ZaGPQbMnmzddx2v3sU)

Nous avons **package.json dans NodeJS** pour la gestion des dépendances et **pom.xml dans Spring Boot** pour la gestion des dépendances.

Dans Group, écrivez le nom que vous voulez. Habituellement, le nom de domaine de l'organisation est écrit de droite à gauche.

Par exemple, notre nom de domaine est [www.javaAPI.com](http://www.javaAPI.com), donc le nom du groupe pourrait être **com.javaAPI.www**

Ensuite, dans Artifact, tapez le **nom du dossier que vous voulez**.

Sur le côté droit, ajoutez les dépendances suivantes :

1. WEB — Pour utiliser les dépendances de Spring (l'ancien framework de Spring Boot utilisé pour développer des applications web)
2. JPA — Java Persistence API
3. MYSQL

Ensuite, cliquez sur « Generate Project ». Vous trouverez un fichier rar — extrayez-le. Puis ouvrez ce dossier dans votre IDE préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/u3sdwjDkrp1ua8vM4vRVFLbX545YJ9IPbABj)

Cliquez sur **com.rest.API** et vous trouverez un fichier **ApiApplication.java** comme suit :

```java
package com.rest.API;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class ApiApplication {
public static void main(String[] args) {
      SpringApplication.run(ApiApplication.class, args);
   }
}
```

Ce code est suffisant pour démarrer votre serveur. Normalement, Spring Boot s'exécute sur **localhost:8080**.

Tapez dans votre terminal comme suit :

> **mvn spring-boot:run**

Voir votre localhost en cours d'exécution dans le navigateur web au port 8080. Il semble vide car nous n'avons encore rien fait.

#### Explorons les fichiers et leurs balises

Si vous regardez le fichier pom.xml, vous remarquerez que les dépendances que vous avez ajoutées lors de la création de l'application dans Spring Initialize comme MySQL, JPA et Web seront à l'intérieur d'une balise **<dependen**cy>.

![Image](https://cdn-media-1.freecodecamp.org/images/zHV02AMHLVCjin9mlAZh4lbwigWVk98mYeFF)

Les dépendances de démarrage et de test sont essentielles pour créer l'application Spring Boot pour servir sur le serveur.

Maintenant, passons à APIApplication.java qui est le fichier principal.

```java
package com.rest.API;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class ApiApplication {
public static void main(String[] args) {
      SpringApplication.run(ApiApplication.class, args);
   }
}
```

Ici, le nom du package est sur la première ligne du code. En utilisant ce nom de package, vous pouvez importer n'importe quelle classe, méthode ou instances dans un autre fichier de package.

Après cela, deux modules sont importés du package « org.springframework.boot ».

1. SpringApplication
2. SpringBootApplication

Puisque Spring Boot est le dernier framework de développement d'applications de Spring, il a besoin des packages de Spring Application ainsi que de ses packages spécifiques.

Après cela, l'annotation **@SpringBootApplication** est utilisée. Cette annotation consiste en des annotations qui sont utilisées dans Spring :

1. **@Component** — Indique au compilateur que la classe suivante est un composant qui doit être inclus lors de la compilation de l'application entière.
2. **@ComponentScan** — Celui-ci effectue le scan des packages que nous allons utiliser dans la classe Java suivante.
3. **@EnableAutoConfiguration** — active le mécanisme d'autoconfiguration de Spring Boot pour importer des modules importants pour que Spring Boot s'exécute.

Ce sont les annotations utilisées pour démarrer l'application Spring Boot pour qu'elle s'exécute sur un serveur.

Voici un article que j'ai écrit sur [Annotation & leurs utilisations en Java](https://medium.com/@parathanlive123/annotation-their-uses-in-java-4285c9413365).

### Créons un modèle pour nos données

Créons une classe de modèle pour sauvegarder, récupérer, mettre à jour et supprimer les détails d'un livre.

Pour cela, je dois créer un nouveau package nommé **model** et à l'intérieur de celui-ci, créer une classe **Book.java** pour mettre mon code.

```java
package com.rest.API.model;
import javax.persistence.*;
import javax.validation.constraints.NotBlank;
@Entity
@Table(name = "books")
public class Book {
    @Id
    @GeneratedValue
    private Long id;
@NotBlank
    private String book_name;
@NotBlank
    private String author_name;
@NotBlank
    private String isbn;
public Book(){
        super();
    }
public Book(Long id, String book_name, String author_name, String isbn) {
        super();
        this.id = id;
        this.book_name = book_name;
        this.author_name = author_name;
        this.isbn=isbn;
    }
public Long getId() {
        return id;
    }
public void setId(Long id) {
        this.id = id;
    }
public String getBook_name() {
        return book_name;
    }
public void setBook_name(String book_name) {
        this.book_name = book_name;
    }
public String getAuthor_name() {
        return author_name;
    }
public void setAuthor_name(String author_name) {
        this.author_name = author_name;
    }
public String getIsbn() {
        return isbn;
    }
public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
}
```

Ici, j'utilise JPA (Java Persistence API) qui est une collection de classes et de méthodes pour stocker continuellement des données dans une base de données.

**@Entity** — utilisé pour indiquer que cette classe va être une entité dans la base de données.

**@Table** — qui prend certaines valeurs comme le nom que vous allez donner à votre table

**@Id** — indique que l'id est la clé primaire / clé d'identification pour cette table

**@NotBlank** — est utilisé pour dire que ces attributs ne doivent pas être vides.

Autre que cela, il y a un constructeur vide qui a une méthode super pour satisfaire les coutumes de JPA. Les méthodes getter et setter sont généralement dans une classe POJO (**Plain old Java object**).

### Création du dépôt

Ensuite, nous allons créer un package **repository** pour gérer la gestion de la base de données en Java.

Créez une interface appelée **BookRepository.java** à l'intérieur du package **repository**.

```java
package com.rest.API.repository;
import com.rest.API.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
@Repository
public interface BookRepository extends JpaRepository<Book, Long> {
}
```

J'ai importé le package **JpaRepository** pour utiliser ce dépôt dans l'interface **BookRepository** en connectant mon modèle de livre récemment codé pour effectuer des opérations **CRUD**.

Il y a déjà des méthodes intégrées dans ces dépôts pour effectuer des opérations CRUD.

Exemple :

```java
.findAll() - pour obtenir toutes les données
.save()    - pour sauvegarder les données obtenues
.delete()  - pour supprimer les données
```

À l'intérieur de la balise <> nous prenons le nom du modèle que nous allons utiliser et le type de données de la clé primaire.

**@Repository** : Annotation utilisée pour indiquer le composant DAO (**Data Access Object**) dans la couche de persistance.

Il indique au compilateur que l'interface va utiliser le dépôt pour effectuer des activités de base de données.

#### Création du contrôleur et gestion des exceptions

Créez un nouveau package appelé **controller**, et à l'intérieur de celui-ci, créez un fichier **BookController.java** qui contient les endpoints.

```java
package com.rest.API.controller;

import com.rest.API.exception.BookNotFoundException;
import com.rest.API.model.Book;
import com.rest.API.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import javax.validation.Valid;
import java.util.List;

@RestController
public class BookController {

@Autowired
    BookRepository bookRepository;

// Obtenir toutes les notes
    @GetMapping("/books")
    public List<Book> getAllNotes() {
        return bookRepository.findAll();
    }

// Créer une nouvelle note
    @PostMapping("/books")
    public Book createNote(@Valid @RequestBody Book book) {
        return bookRepository.save(book);
    }

// Obtenir une seule note
    @GetMapping("/books/{id}")
    public Book getNoteById(@PathVariable(value = "id") Long bookId) throws BookNotFoundException {
        return bookRepository.findById(bookId)
                .orElseThrow(() -> new BookNotFoundException(bookId));
    }

// Mettre à jour une note
    @PutMapping("/books/{id}")
    public Book updateNote(@PathVariable(value = "id") Long bookId,
                           @Valid @RequestBody Book bookDetails) throws BookNotFoundException {

Book book = bookRepository.findById(bookId)
                .orElseThrow(() -> new BookNotFoundException(bookId));

book.setBook_name(bookDetails.getBook_name());
        book.setAuthor_name(bookDetails.getAuthor_name());
        book.setIsbn(bookDetails.getIsbn());

Book updatedBook = bookRepository.save(book);

return updatedBook;
    }

// Supprimer une note
    @DeleteMapping("/books/{id}")
    public ResponseEntity<?> deleteBook(@PathVariable(value = "id") Long bookId) throws BookNotFoundException {
        Book book = bookRepository.findById(bookId)
                .orElseThrow(() -> new BookNotFoundException(bookId));

bookRepository.delete(book);

return ResponseEntity.ok().build();
    }
}
```

Le premier package importé est pour l'exception Book Not Found (pour laquelle nous allons créer un fichier dans un instant).

**Explication des annotations que nous avons utilisées ici :**

1. **RestController** : Cette annotation est utilisée pour désigner chaque méthode dans la classe annotée comme Objet de Domaine.

Alors, qu'est-ce qu'un Objet de Domaine...

Il dit simplement que Objet de Domaine == Objet d'Affaires.

Ils sont généralement représentés par des entités et des objets de valeur liés à l'endpoint que nous donnons pour obtenir les données de la base de données.

2. **Autowired** : Cette annotation est utilisée pour connecter automatiquement les classes de beans.

Pour cela, vous devez savoir « **Qu'est-ce qu'une classe Bean..?** »

En gros, une classe Java Bean est une classe simple qui encapsule de nombreux objets en elle.

C'est un article que j'ai écrit sur [Java Bean Classes](https://medium.com/@parathantl/java-bean-class-804c6431a57f).

Les annotations de mappage suivantes sont pour les endpoints afin d'effectuer des opérations CRUD.

3. **GetMapping** : Il s'agit d'une **interface** qui contient le chemin de l'endpoint pour effectuer une méthode Get. Cette interface GetMapping utilise l'interface RequestMapping qui peut avoir la méthode « path, value, params, headers » pour effectuer la méthode Get dans les versions précédentes de Spring.

Maintenant, c'est simplifié en utilisant **GetMapping**.

4. **PostMapping** : Il s'agit d'une **interface** qui contient le chemin de l'endpoint pour effectuer la méthode Post.

5. **PutMapping** : Il s'agit d'une **interface** qui contient le chemin de l'endpoint pour effectuer la méthode Put pour la mise à jour.

6. **DeleteMapping** : Il s'agit d'une **interface** qui contient le chemin de l'endpoint pour effectuer la méthode Delete.

Dans les dernières lignes, vous avez probablement remarqué le mot-clé « **ResponseEntity** ».

Qu'est-ce que **c'est**...

C'est une classe Java qui hérite de la classe **HttpEntity** pour manipuler les réponses HTTP. Que la demande de connexion soit « **OK** » ou s'il y a des problèmes, lancez une **exception** à partir de la classe **HttpEntity**.

**orElseThrow()** : Il s'agit d'une méthode trouvée dans la **classe Optional de Java8** qui a été introduite pour gérer les exceptions. La classe optional fournit diverses méthodes utilitaires pour vérifier la présence ou l'absence d'un objet, ce qui aide à traiter NullPointerException.

**orElseThrow** est une méthode qui retourne la valeur si présente, sinon invoque une exception.

#### Création d'une NotFoundException s'il n'y a pas de book_id

Comme la méthode orElseThrow lance une exception NotFound. Voici la partie de gestion des exceptions. Créez un fichier **BookNotFoundException.java** à l'intérieur du package exception.

```java
package com.rest.API.exception;
public class BookNotFoundException extends Exception {
private long book_id;
public BookNotFoundException(long book_id) {
        super(String.format("Book is not found with id : '%s'", book_id));
        }
}
```

La classe créée étend la superclasse de Exception. Dans le constructeur, je passe le book_id et imprime l'exception.

Donc, c'est tout...

Nous avons terminé la partie API REST. Maintenant, vous pouvez construire l'application (qui a été expliquée dans la partie 1) et faire quelques tests avec Postman.

#### Connexion avec la base de données MySql

À l'intérieur du fichier **application.properties** de votre dossier **resources**, ajoutez ce qui suit :

```java
## Spring DATASOURCE (DataSourceAutoConfiguration & DataSourceProperties)
spring.datasource.url = jdbc:mysql://localhost:3306/library
spring.datasource.username = root // normalement mettez votre nom d'utilisateur MySQL 
spring.datasource.password = VOTRE_MOT_DE_PASSE_MYSQL
## Hibernate Properties
# The SQL dialect makes Hibernate generate better SQL for the chosen database
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL5InnoDBDialect
# Hibernate ddl auto (create, create-drop, validate, update)
spring.jpa.hibernate.ddl-auto = update
```

C'est tout.

Nous avons construit une API REST de base dans Spring Boot. Félicitations !

Si quelque chose ne va pas ou doit être corrigé, faites-le moi savoir dans la section des commentaires.

Restez en contact avec moi sur [twitter](https://twitter.com/Parathantl).

Bon codage !