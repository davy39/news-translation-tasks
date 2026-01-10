---
title: Tutoriel Spring Boot – Comment construire des applications Java rapides et
  modernes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-20T19:43:06.000Z'
originalURL: https://freecodecamp.org/news/spring-boot-tutorial-build-fast-modern-java-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-ramdas-ware-102896.jpg
tags:
- name: database
  slug: database
- name: Java
  slug: java
- name: spring-boot
  slug: spring-boot
- name: spring security
  slug: spring-security
seo_title: Tutoriel Spring Boot – Comment construire des applications Java rapides
  et modernes
seo_desc: "By Yiğit Kemal Erinç\nIn this article I am going to walk you through building\
  \ a prototype with Spring Boot. Think of it like building a project for a hackathon\
  \ or a prototype for your startup in limited time. \nIn other words, we are not\
  \ trying to buil..."
---

Par Yiğit Kemal Erinç

Dans cet article, je vais vous guider à travers la création d'un prototype avec Spring Boot. Imaginez que vous construisez un projet pour un hackathon ou un prototype pour votre startup en un temps limité. 

En d'autres termes, nous n'essayons pas de construire quelque chose de parfait – mais plutôt quelque chose qui fonctionne.

Si vous êtes bloqué à une partie de ce tutoriel ou si j'ai oublié de mentionner quelque chose, vous pouvez consulter le dépôt GitHub que j'ai inclus dans la **Conclusion**.

### Prérequis

* Fondamentaux de Java et de la POO
* Connaissance de base des bases de données relationnelles (un-à-plusieurs, plusieurs-à-plusieurs, etc.)
* Les bases de Spring seraient utiles
* Niveau de base en HTML

Assurez-vous également d'avoir ce qui suit :

* [JDK (Java Development Kit)](https://www.oracle.com/java/technologies/javase-downloads.html) dernier
* [IntelliJ IDEA](https://www.jetbrains.com/idea/) ou un autre IDE Java

## Que construisons-nous ?

Nous allons construire un système de réservation d'équipements où les utilisateurs se connecteront et réserveront un créneau pour utiliser un service tel que centre de fitness, piscine ou sauna. 

Chaque équipement aura une certaine capacité (nombre de personnes pouvant utiliser le service en même temps) afin que les gens puissent utiliser les équipements en toute sécurité pendant la pandémie de Covid-19.

### Liste des fonctionnalités de l'application

Nous pouvons considérer notre application comme le système de réservation pour un complexe d'appartements. 

* Les utilisateurs doivent pouvoir se connecter.
* Nous supposerons que les comptes des résidents sont pré-créés et qu'il n'y aura pas de fonctionnalité d'inscription.
* Les utilisateurs doivent pouvoir consulter leurs réservations. 
* Les utilisateurs doivent pouvoir créer de nouvelles réservations en sélectionnant le type d'équipement, la date et l'heure.
* **Seuls les utilisateurs connectés** doivent pouvoir voir la page des réservations et créer des réservations.
* Nous devons vérifier la capacité et ne créer de nouvelles réservations que si le nombre actuel de réservations ne dépasse pas la capacité.

### Technologies que nous utiliserons

Nous allons apprendre beaucoup de technologies utiles qui vous rendront plus efficace en tant que développeur Spring Boot. Je vais brièvement mentionner ce qu'elles sont et à quoi elles servent, puis nous les verrons en action.

* Bootify
* Hibernate
* Spring Boot
* Maven
* JPA
* Swagger
* Base de données H2 In-Memory
* Thymeleaf
* Bootstrap
* Spring Security

## Pourquoi Spring Boot ?

Le framework Spring est généralement utilisé pour des travaux de niveau entreprise/à grande échelle. Ce n'est pas généralement la première option qui vient à l'esprit pour des projets plus petits – mais je vais argumenter qu'il peut être assez rapide pour le prototypage. 

Il présente les avantages suivants :

* Le développement basé sur les annotations génère beaucoup de code pour vous en coulisses. Et surtout avec la disponibilité de bibliothèques comme Lombok, il est devenu beaucoup plus facile de se concentrer sur la logique métier.
* Il a un bon support pour les bases de données en mémoire, donc nous n'avons pas besoin de créer une vraie base de données et de nous y connecter. (H2)
* Il a un écosystème mature, donc vous pouvez facilement trouver des réponses à la plupart des questions.
* Presque "aucune configuration" n'est requise. Avec l'aide de Spring Boot, nous nous débarrassons des configurations XML laides du côté Spring des choses et la configuration de votre application est vraiment facile.
* Il se passe beaucoup de choses en coulisses. Spring fournit tellement de magie et fait tant de choses pour faire avancer les choses. Donc vous n'avez généralement pas besoin de vous soucier de ces trucs et pouvez simplement laisser le framework gérer les choses.
* Nous avons [Spring Security.](https://github.com/spring-projects/spring-security) Avoir l'un des frameworks de sécurité les plus complets et testés en combat de votre côté vous donne plus de confiance dans la sécurité de votre application. Il prend également en charge une bonne partie du travail difficile pour vous.

## Comment créer le projet avec Bootify

Pour créer le projet, vous utiliserez [**Bootify**](https://bootify.io/). C'est un service freemium qui rend le développement Spring Boot plus rapide en générant beaucoup de code standard pour vous et en vous permettant de vous concentrer sur la logique métier.

**Bootify** nous permet de spécifier nos préférences et importe automatiquement les dépendances similaires à **Spring Initializr**. 

Mais il y a plus que cela. Vous pouvez également spécifier vos entités et il générera les classes de modèle et DTO correspondantes. Il peut même générer le code de service et de contrôleur pour les opérations **CRUD** courantes.

Je pense que c'est un outil plus pratique pour le développement d'API que pour les applications MVC, car il génère du code d'API REST par défaut. Mais il facilitera toujours notre vie même avec une application Spring Boot MVC qui contient des vues. Nous devrons simplement apporter quelques ajustements au code généré.

Ouvrons le site web **Bootify** et cliquons sur le bouton "Start Project" en haut à droite.

Vous devez sélectionner :

* **Maven** comme type de build
* Version de Java : 14
* Cochez activer **Lombok**
* SGBD : base de données **H2**
* Cochez **ajouter** **dateCreated/lastUpdated** aux entités
* Packages : Technique
* Activer **OpenAPI/Swagger UI**
* Ajoutez **org.springframework.boot:spring-boot-devtools** aux dépendances supplémentaires

Une fois que vous avez terminé, vous devriez voir ceci :

![Image](https://erinc.io/wp-content/uploads/2021/04/screencapture-bootify-io-app-8U9U2BBTLEAX-2021-04-09-16_06_29-1024x754.png)

Maintenant, spécifions nos entités. Commencez par cliquer sur l'onglet **Entités** dans le menu de gauche.

Nous aurons les entités et relations suivantes :

1. **Réservation** qui contient les données liées à chaque réservation telles que la date de réservation, l'heure de début de réservation, l'heure de fin et l'utilisateur qui possède cette réservation.
2. L'entité **Utilisateur** qui contient notre modèle d'utilisateur et aura des relations avec **Réservation**.
3. L'entité **Équipement** pour stocker le type d'équipement et sa capacité (nombre maximum de réservations pour un certain temps, par exemple 2 personnes peuvent utiliser et réserver le Sauna pour le même temps).

Définissons notre entité **Réservation** comme suit et gardons "Ajouter des points de terminaison REST" coché (même si nous modifierons la sortie). Ensuite, cliquez sur le bouton Enregistrer.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-1-1024x577.png)

Nous spécifierons les relations plus tard, donc le seul champ que notre entité utilisateur possède est le champ id.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-1024x445.png)

Nous pourrions créer une entité pour les équipements afin de stocker les données du nom de l'équipement et de sa capacité, puis nous pourrions y faire référence depuis la **Réservation**. Mais la relation entre Équipement et Réservation serait un-à-un. 

Donc, pour simplifier, nous allons créer une énumération appelée **AmenityType** et stocker le **AmenityType** à l'intérieur de **Réservation**.

Maintenant, créons une relation entre les entités **Utilisateur** et **Réservation** en cliquant sur le bouton + à côté du menu **Relations**.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-2.png)
_Menu pour créer des relations_

Ce sera une relation **Plusieurs-à-un** puisque un utilisateur peut avoir plusieurs réservations mais une réservation doit avoir un et un seul utilisateur. Nous nous assurerons que c'est le cas en cochant la case requise.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-3-1024x507.png)
_Relation Utilisateur-Réservation_

Nous cliquons sur "Enregistrer les modifications" et c'est terminé. Votre modèle final devrait ressembler à ceci :

![Image](https://erinc.io/wp-content/uploads/2021/04/image-4-1024x481.png)

Maintenant, cliquez sur le bouton de téléchargement dans le menu de gauche pour télécharger le code du projet généré afin que nous puissions commencer à travailler dessus. Vous pouvez voir le premier commit sur le dépôt du projet pour comparer avec le vôtre si vous avez des problèmes.

Après avoir téléchargé le projet, ouvrez-le dans un IDE – j'utiliserai **IntelliJ IDEA**. Votre structure de fichiers devrait ressembler à ceci :

```
├── amenity-reservation-system.iml
├── mvnw
├── mvnw.cmd
├── pom.xml
├── src
│   └── main
│       ├── java
│       │   └── com
│       │       └── amenity_reservation_system
│       │           ├── AmenityReservationSystemApplication.java
│       │           ├── HomeController.java
│       │           ├── config
│       │           │   ├── DomainConfig.java
│       │           │   ├── JacksonConfig.java
│       │           │   └── RestExceptionHandler.java
│       │           ├── domain
│       │           │   ├── Reservation.java
│       │           │   └── User.java
│       │           ├── model
│       │           │   ├── ErrorResponse.java
│       │           │   ├── FieldError.java
│       │           │   ├── ReservationDTO.java
│       │           │   └── UserDTO.java
│       │           ├── repos
│       │           │   ├── ReservationRepository.java
│       │           │   └── UserRepository.java
│       │           ├── rest
│       │           │   ├── ReservationController.java
│       │           │   └── UserController.java
│       │           └── service
│       │               ├── ReservationService.java
│       │               └── UserService.java
│       └── resources
│           └── application.yml
└── target
    ├── classes
    │   ├── application.yml
    │   └── com
    │       └── amenity_reservation_system
    │           ├── AmenityReservationSystemApplication.class
    │           ├── HomeController.class
    │           ├── config
    │           │   ├── DomainConfig.class
    │           │   ├── JacksonConfig.class
    │           │   └── RestExceptionHandler.class
    │           ├── domain
    │           │   ├── Reservation.class
    │           │   └── User.class
    │           ├── model
    │           │   ├── ErrorResponse.class
    │           │   ├── FieldError.class
    │           │   ├── ReservationDTO.class
    │           │   └── UserDTO.class
    │           ├── repos
    │           │   ├── ReservationRepository.class
    │           │   └── UserRepository.class
    │           ├── rest
    │           │   ├── ReservationController.class
    │           │   └── UserController.class
    │           └── service
    │               ├── ReservationService.class
    │               └── UserService.class
    └── generated-sources
        └── annotations
```

## Comment tester et explorer le code généré

Prenons notre temps pour expérimenter avec le code généré et le comprendre couche par couche.

Le dossier **Repos** contient le code pour la couche d'accès aux données, à savoir nos dépôts. Nous utiliserons les méthodes **JPA** pour récupérer nos données, qui sont des méthodes de requête pré-faites que vous pouvez utiliser en les définissant à l'intérieur de l'interface de dépôt. 

Remarquez que nos classes de dépôt étendent l'interface **JpaRepository**. C'est l'interface qui nous permet d'utiliser les méthodes mentionnées. 

Les requêtes JPA suivent une certaine convention, et lorsque nous créons la méthode qui obéit aux conventions, elle saura automatiquement quelles données vous souhaitez récupérer, en coulisses. Si vous ne comprenez pas encore, ne vous inquiétez pas, nous verrons des exemples.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-5-1024x719.png)
_Mots-clés d'exemple, phrases d'exemple et leurs extraits JPQL correspondants (requêtes)_

Les classes **Model** présentent notre modèle de données, et quelles classes auront quels champs. 

Chaque classe de modèle correspond à une table de base de données avec le même nom et les champs dans la classe de modèle seront des colonnes dans la table correspondante. 

Remarquez l'annotation **@Entity** en haut de nos classes de modèle. Cette annotation est gérée par [**Hibernate**](https://hibernate.org/) et chaque fois qu'Hibernate voit **@Entity**, il créera une table en utilisant le nom de notre classe comme nom de table. 

Si vous vous demandez, "Qu'est-ce qu'Hibernate au fait ?", c'est un outil de **mappage objet-relationnel** (ORM) pour Java qui nous permet de mapper les **POJOs** (Plain Old Java Object) aux tables de base de données. Il peut également fournir des fonctionnalités telles que des contraintes de validation de données, mais nous n'approfondirons pas Hibernate dans cet article car c'est un sujet vaste en soi. 

Une fonctionnalité géniale d'Hibernate est qu'il gère toutes les opérations de création et de suppression de tables, donc vous n'avez pas besoin d'utiliser des scripts **SQL** supplémentaires.

Nous représentons également les relations entre les objets dans les classes de modèle. Pour voir un exemple, jetez un œil à notre classe **User** :

```java
    @OneToMany(mappedBy = "user")
    private Set<Reservation> userReservations;
```

Elle a un objet **userReservations** qui contient un ensemble de références qui ressemble aux réservations de cet utilisateur particulier. Dans la classe **Reservation**, nous avons la relation inverse comme :

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

Avoir des références des deux côtés permet d'accéder à l'autre côté de la relation (objet utilisateur à réservation et vice versa).

Les **Contrôleurs** géreront les requêtes qui sont passées à ce contrôleur par le gestionnaire de requêtes et retourneront les vues correspondantes, dans ce cas. 

Les contrôleurs qui ont été générés par Bootify sont configurés pour retourner des réponses JSON, et nous les modifierons dans la section suivante pour retourner nos vues.

Les **Services** contiendront la logique de notre application. La meilleure pratique est de garder les contrôleurs minces en gardant la logique métier dans un endroit séparé, les classes de service. 

Les contrôleurs ne doivent pas interagir directement avec les dépôts, mais plutôt appeler le service qui interagira avec le dépôt, effectuera toute opération supplémentaire et retournera le résultat au contrôleur.

### Essayons l'API

Maintenant, passons à la partie amusante et essayons notre API pour la voir en action. Exécutez l'application Spring sur votre IDE préféré. Ouvrez votre navigateur et allez à cette adresse :

```
http://localhost:8080/swagger-ui/index.html?configUrl=/v3/api-docs/swagger-config#/
```

Swagger documente automatiquement notre code et vous permet d'envoyer des requêtes facilement. Vous devriez voir ceci :

![Image](https://erinc.io/wp-content/uploads/2021/04/screencapture-localhost-8080-swagger-ui-index-html-2021-04-17-21_27_48-1024x914.png)

Créons d'abord un utilisateur en envoyant une requête **POST** à **UserController**. Nous le ferons en cliquant sur la dernière case (la verte) sous la liste user-controller.

![Image](https://erinc.io/wp-content/uploads/2021/04/Screen-Shot-2021-04-17-at-21.30.41-1024x565.png)

**Swagger** nous montre les paramètres que ce point de terminaison attend – seulement l'id pour l'instant – et aussi les réponses que l'API retourne. 

Cliquez sur le bouton "Try it out" en haut à droite. Il vous demande d'entrer un id. Je sais que c'est absurde et que le code n'utilisera même pas cet id que vous entrez, mais nous corrigerons cela dans la section suivante (c'est juste un problème avec le code généré). 

Pour l'expérience, entrez n'importe quel nombre, comme 1 pour l'id, et cliquez sur le bouton exécuter.

![Image](https://erinc.io/wp-content/uploads/2021/04/screencapture-localhost-8080-swagger-ui-index-html-2021-04-17-21_39_32-547x1024.png)

Le corps de la réponse contient l'id de l'objet créé. Nous pouvons confirmer qu'il est créé sur la base de données en vérifiant la console H2. 

Mais avant de faire cela, nous devons apporter une légère modification au fichier **application.yml** qui contient les paramètres et la configuration de l'application. Ouvrez votre fichier **application.yml** et collez le code suivant :

```
spring:
  datasource:
    url: ${JDBC_DATABASE_URL:jdbc:h2:mem:amenity-reservation-system}
    username: ${JDBC_DATABASE_USERNAME:sa}
    password: ${JDBC_DATABASE_PASSWORD:}
  dbcp2:
    max-wait-millis: 30000
    validation-query: "SELECT 1"
    validation-query-timeout: 30
  jpa:
    hibernate:
      ddl-auto: update
    open-in-view: false
    properties:
      hibernate:
        jdbc:
          lob:
            non_contextual_creation: true
        id:
          new_generator_mappings: true
springdoc:
  pathsToMatch: /api/**
```

Ensuite, nous devrions pouvoir accéder à la console H2 en allant à cette adresse :

```
http://localhost:8080/h2-console/
```

![Image](https://erinc.io/wp-content/uploads/2021/04/image-6-1024x724.png)

Ici, vous devez vérifier que le nom d'utilisateur est "sa" et cliquer sur le bouton Connecter.

Cliquez sur la table USER dans le menu de gauche et la console écrira la requête select all pour vous.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-7-1024x573.png)
_Panneau d'administration H2_

Cliquons sur le bouton **Exécuter** qui se trouve au-dessus de la requête.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-8-1024x466.png)

Nous pouvons voir que l'objet **User** est effectivement créé – super !

Nous avons déjà une API fonctionnelle à ce stade et nous n'avons pas écrit une seule ligne de code.

### Comment ajuster le code pour notre cas d'utilisation

Comme je l'ai mentionné précédemment, le code généré ne convient pas entièrement à notre cas d'utilisation et nous devons y apporter quelques ajustements. 

Supprimons le dossier model qui contient les DTO et autres éléments que nous n'utiliserons pas. Nous afficherons les données à l'intérieur des vues à la place.

```
cd src/main/java/com/amenity_reservation_system/ 
rm -rf model
```

Nous aurons beaucoup d'erreurs maintenant puisque le code utilise les classes DTO, mais nous nous en débarrasserons après avoir supprimé les classes de contrôleur. 

Nous allons supprimer les contrôleurs car nous ne voulons plus exposer la fonctionnalité de modification de nos données. Nos utilisateurs doivent pouvoir le faire en interagissant avec notre interface utilisateur, et nous créerons de nouveaux contrôleurs pour retourner les composants de vue dans la section suivante.

```
rm -rf rest
```

Enfin, nous devons faire un peu de refactoring de nos classes de service puisque les classes DTO ne sont plus présentes :

```java
package com.amenity_reservation_system.service;

import com.amenity_reservation_system.domain.User;
import com.amenity_reservation_system.repos.UserRepository;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;


@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(final UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> findAll() {
        return userRepository.findAll();
    }

    public User get(final Long id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
    }

    public Long create(final User user) {
        return userRepository.save(user).getId();
    }

    public void update(final Long id, final User user) {
        final User existingUser = userRepository.findById(id)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
        
        userRepository.save(user);
    }

    public void delete(final Long id) {
        userRepository.deleteById(id);
    }
}
```

Nous avons essentiellement supprimé le code lié aux DTO de la classe **UserService** et remplacé les types de retour par **User**. Faisons de même pour **ReservationService**.

```java
package com.amenity_reservation_system.service;

import com.amenity_reservation_system.domain.Reservation;
import com.amenity_reservation_system.domain.User;
import com.amenity_reservation_system.repos.ReservationRepository;
import com.amenity_reservation_system.repos.UserRepository;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;


@Service
public class ReservationService {

    private final ReservationRepository reservationRepository;
    private final UserRepository userRepository;

    public ReservationService(final ReservationRepository reservationRepository,
            final UserRepository userRepository) {
        this.reservationRepository = reservationRepository;
        this.userRepository = userRepository;
    }

    public List<Reservation> findAll() {
        return reservationRepository.findAll();
    }

    public Reservation get(final Long id) {
        return reservationRepository.findById(id)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
    }

    public Long create(final Reservation reservation) {
        return reservationRepository.save(reservation).getId();
    }

    public void update(final Long id, final Reservation reservation) {
        final Reservation existingReservation = reservationRepository.findById(id)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
        reservationRepository.save(reservation);
    }

    public void delete(final Long id) {
        reservationRepository.deleteById(id);
    }

}
```

Supprimons également les classes de configuration :

```
rm -rf config
```

Et renommons le dossier domain en model. Si vous utilisez un IDE, je vous conseille fortement d'utiliser la fonctionnalité de renommage de votre IDE pour renommer ce dossier, car il renommera automatiquement les imports pour correspondre au nouveau nom de package.

```
mv domain model
```

Assurez-vous également que vos classes de modèle (**User** et **Reservation**) ont le bon nom de package après cette opération. La première ligne de ces deux fichiers doit être :

```
package com.amenity_reservation_system.model;
```

Si elle reste en tant que package domain, vous pouvez avoir des erreurs.

À ce stade, vous devriez pouvoir compiler et exécuter le projet sans aucun problème.

## Comment créer les contrôleurs et les fichiers de vue pour afficher les données

**Thymeleaf** est un moteur de template pour Spring qui nous permet de créer des interfaces utilisateur et d'afficher nos données de modèle aux utilisateurs. 

Nous pouvons accéder aux objets Java à l'intérieur du template Thymeleaf, et nous pouvons également utiliser le bon vieux HTML, CSS et JavaScript. Si vous connaissez les JSP, c'est JSP en version améliorée.

Créons quelques templates Thymeleaf qui ne feront rien d'autre qu'afficher les données pour l'instant. Nous les styliserons dans la section suivante. Nous créerons également les contrôleurs qui retourneront ces vues.

Avant de commencer avec les templates Thymeleaf, nous devons ajouter une dépendance Maven pour Spring Boot Thymeleaf. Vos dépendances doivent ressembler à ceci dans votre fichier **pom.xml** :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.4.4</version>
        <relativePath /><!-- lookup parent from repository -->
    </parent>
    <groupId>com</groupId>
    <artifactId>amenity-reservation-system</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>amenity-reservation-system</name>

    <properties>
        <java.version>14</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-ui</artifactId>
            <version>1.5.2</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.20</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>

```

Vous pouvez simplement copier et coller le contenu interne de la balise dependencies. Maintenant, demandons à Maven d'installer les dépendances :

```
mvn clean install
```

Nous sommes maintenant prêts à créer nos vues. Créons un répertoire sous resources pour contenir nos fichiers de modèles de vue comme ceci :

```
cd ../../../resources
mkdir templates
```

Et créons un fichier de vue :

```
cd templates
touch index.html
```

Copiez et collez le fragment suivant. Ce fichier sera notre page d'accueil à l'avenir.

```
<!DOCTYPE HTML>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8"/>
    <title>Amenities Reservation App</title>

    <link th:rel="stylesheet" th:href="@{/webjars/bootstrap/4.0.0-2/css/bootstrap.min.css} "/>
</head>
<body>

<div>
hello world!
</div>

<script th:src="@{/webjars/jquery/3.0.0/jquery.min.js}"></script>
<script th:src="@{/webjars/popper.js/1.12.9-1/umd/popper.min.js}"></script>
<script th:src="@{/webjars/bootstrap/4.0.0-2/js/bootstrap.min.js}"></script>

</body>
</html>
```

Nous devons également créer un contrôleur qui nous retournera cette vue afin que nous puissions la voir dans le navigateur.

```
cd ../java/com/amenity_reservation_system
mkdir controller && cd controller
touch HomeController
```

Collez ce code dans le HomeController :

```
package com.amenity_reservation_system.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class HomeController {

    @GetMapping("/")
    public String index(Model model) {

        return "index";
    }
}

```

Remarquez comment nous annotons notre méthode avec **@Controller** au lieu de **@RestController** cette fois. L'annotation @RestController implique que le contrôleur retournera une réponse REST alors qu'un **@Controller** peut retourner des vues/HTML pré-rendus (SSR).

Lorsque qu'une requête arrive dans notre application, Spring exécutera automatiquement cette méthode de contrôleur. Ensuite, il trouvera le fichier **index.html** que nous avons précédemment créé sous les ressources et enverra ce fichier au client.

Confirmons que cela fonctionne en envoyant une requête à notre application. N'oubliez pas de redémarrer d'abord, puis envoyez cette requête :

```
GET localhost:8080
```

Vous devriez pouvoir voir le message Hello World sur le navigateur.

## Comment définir différents types d'équipements

Nous avons la classe **Réservation** mais nous n'avons pas créé de moyen de spécifier quel type d'équipement est réservé (la piscine, le sauna ou la salle de sport).

Il existe plusieurs façons de faire cela. L'une d'entre elles serait de créer une entité appelée Équipement pour stocker les données partagées entre les entités. Ensuite, nous créerions les classes **PoolAmenity**, **SaunaAmenity** et **GymAmenity** qui étendraient alors la classe Amenity. 

C'est une solution agréable et extensible, mais cela semble un peu excessif pour notre application simple, car nous n'avons pas beaucoup de données spécifiques au type d'équipement. Nous n'aurons qu'une capacité pour chaque type d'équipement.

Pour garder les choses simples et ne pas nous embêter avec l'héritage de table et d'autres choses compliquées, créons simplement une énumération pour indiquer le type d'équipement sous forme de chaîne et laissons chaque réservation avoir l'un de ceux-ci.

Passons du répertoire du contrôleur au répertoire du modèle et créons l'énumération pour **AmenityType** :

```
cd ../model
touch AmenityType.java
```

```
public enum AmenityType {
    POOL("POOL"), SAUNA("SAUNA"), GYM("GYM");

    private final String name;

    private AmenityType(String value) {
        name = value;
    }

    @Override
    public String toString() {
        return name;
    }
}
```

Dans cette énumération, nous définissons une variable de nom pour contenir le nom de l'énumération et créons un constructeur privé pour n'autoriser qu'un ensemble limité de types. Remarquez que les déclarations de type appellent le constructeur depuis la classe avec leurs valeurs de nom.

Maintenant, nous devons modifier la classe Reservation pour contenir une référence à **AmenityType** :

```java
@Enumerated(EnumType.STRING)
@Column(nullable = false)
private AmenityType amenityType;
```

Nous utilisons l'annotation **@Enumerated** pour décrire comment nous voulons stocker l'énumération dans notre base de données. Nous allons également la rendre non nullable car chaque **Réservation** doit avoir un **AmenityType**.

## Comment afficher les réservations d'un utilisateur

Quelle est la fonctionnalité la plus cruciale pour notre application ? Créer des réservations et afficher les réservations d'un utilisateur. 

Nous n'avons pas encore de moyen d'authentifier les utilisateurs, donc nous ne pouvons pas vraiment demander à l'utilisateur de se connecter puis afficher leurs réservations. Mais nous voulons toujours implémenter et tester la fonctionnalité pour réserver un équipement et afficher les réservations.

À cette fin, nous pouvons demander à Spring de mettre certaines données initiales dans notre base de données chaque fois que l'application s'exécute. Ensuite, nous pouvons interroger ces données pour tester si nos requêtes fonctionnent réellement. Nous pouvons ensuite procéder à l'appel de ces services depuis nos **Vues** et ajouter l'authentification à notre application dans les sections suivantes.

Nous utiliserons un bean **CommandLineRunner** pour exécuter le code initial. Chaque fois que le conteneur Spring trouve un bean de type CommandLineRunner, il exécutera le code à l'intérieur. Avant cette étape, ajoutons quelques méthodes à nos classes de modèle pour faciliter et rendre moins verbeuse la création d'objets.

Jetez un œil aux annotations des classes de modèle et vous devriez voir des annotations comme **@Getter** et **@Setter**. Ce sont des annotations **Lombok**. 

Lombok est un processeur d'annotations que nous pouvons utiliser pour améliorer notre expérience de codage en le laissant générer du code pour nous. Lorsque nous annotons une classe avec **@Getter** et **@Setter**, il génère les getters et setters pour chaque champ de cette classe. 

Spring utilise les méthodes getter et setter pour de nombreuses opérations triviales en coulisses, donc celles-ci sont presque toujours requises. Et les créer pour chaque entité devient facilement une corvée sans l'aide de Lombok. 

Lombok peut faire plus que cela cependant. Nous ajouterons également les annotations suivantes à nos classes **Réservation** et **Utilisateur** :

```
@Builder
@NoArgsConstructor
@AllArgsConstructor
```

Avec ces annotations, Lombok implémente le modèle de création builder pour cette classe et crée également 2 constructeurs : l'un sans arguments (constructeur par défaut) et un autre avec tous les arguments. Je pense que c'est génial que nous puissions faire autant en ajoutant simplement quelques annotations. 

Nous sommes maintenant prêts à ajouter quelques données initiales. Allez dans votre classe principale (**AmenityReservationSystemApplication.java**) et ajoutez cette méthode :

```java
package com.amenity_reservation_system;

import com.amenity_reservation_system.model.AmenityType;
import com.amenity_reservation_system.model.Reservation;
import com.amenity_reservation_system.model.User;
import com.amenity_reservation_system.repos.ReservationRepository;
import com.amenity_reservation_system.repos.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZoneId;
import java.util.Date;


@SpringBootApplication
public class AmenityReservationSystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(AmenityReservationSystemApplication.class, args);
    }

    @Bean
    public CommandLineRunner loadData(UserRepository userRepository,
                                      ReservationRepository reservationRepository) {
        return (args) -> {
            User user = userRepository.save(new User());
            DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
            Date date = new Date();
            LocalDate localDate = date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
            Reservation reservation = Reservation.builder()
                    .reservationDate(localDate)
                    .startTime(LocalTime.of(12, 00))
                    .endTime(LocalTime.of(13, 00))
                    .user(user)
                    .amenityType(AmenityType.POOL)
                    .build();

            reservationRepository.save(reservation);
        };
    }
}

```

Si vous obtenez une erreur concernant les opérations d'enregistrement telles que "Le type déduit 'S' pour le paramètre ... ne correspond pas", c'est parce que nous avons renommé le répertoire domain en model. Allez dans les classes de dépôt et corrigez les chemins des imports vers **model.User** et **model.Reservation**.

Remarquez comment nous avons utilisé le **modèle de construction** pour créer facilement l'objet de réservation. Lorsque la création d'objet devient complexe et qu'un constructeur nécessite tant de paramètres, il est facile d'oublier l'ordre des paramètres ou de simplement mélanger l'ordre. 

Sans le modèle de construction, nous devrions soit appeler un constructeur avec tant de paramètres, soit appeler le constructeur par défaut et écrire du code #properties pour appeler les setters.

Une fois que vous avez terminé, exécutez à nouveau votre application pour insérer les données initiales et connectez-vous à la **console H2** comme nous l'avons appris précédemment pour confirmer que notre date est effectivement insérée. Si vous n'avez pas d'erreurs, vous devriez pouvoir voir que l'utilisateur et la réservation sont insérés avec succès.

![Image](https://erinc.io/wp-content/uploads/2021/04/image-9-1024x325.png)

Nous avons inséré une réservation pour pouvoir tester la fonctionnalité de liste des réservations, mais nos vues n'ont actuellement aucun moyen d'afficher les réservations et d'ajouter des réservations. Nous devons créer l'interface utilisateur pour cela. 

Nous n'avons pas encore de mécanisme d'authentification ou d'inscription, alors agissez comme si l'utilisateur avec l'ID 10001 était connecté. Plus tard, nous améliorerons cela en vérifiant dynamiquement qui est connecté et en affichant une page différente si l'utilisateur n'est pas connecté.

### Comment créer des vues avec Thymeleaf

Commençons par créer une simple page d'accueil et une barre de navigation pour nous-mêmes. Nous utiliserons les fragments Thymeleaf pour le code de la barre de navigation. 

Les fragments Thymeleaf nous permettent de créer des structures réutilisables similaires à des composants, comme les composants React/Vue si vous les connaissez. Créons un dossier pour nos fragments sous les templates et appelons-le fragments.

```
mkdir fragments
touch nav.html
```

Nous mettrons notre barre de navigation dans le fichier **nav.html**. Copiez et collez le code suivant :

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<body>
<nav th:fragment="nav" class="navbar navbar-expand navbar-dark bg-primary">
    <div class="navbar-nav w-100">
        <a class="navbar-brand text-color" href="/">Amenities Reservation System</a>
    </div>
</nav>
</body>
</html>
```

Dans son état actuel, il ne fait pas grand-chose, mais nous pourrions ajouter un bouton de connexion ou quelques liens à l'avenir. 

Maintenant, créons une simple page d'accueil qui servira les utilisateurs qui ne sont pas connectés. Nous aurons notre fragment de barre de navigation en haut et un bouton de connexion pour demander à l'utilisateur de se connecter avant d'utiliser l'application.

```html
<!DOCTYPE HTML>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8"/>
    <title>Amenities Reservation App</title>

    <link th:rel="stylesheet" th:href="@{/webjars/bootstrap/4.0.0-2/css/bootstrap.min.css} "/>
</head>
<body>

<div>
    <div th:insert="fragments/nav :: nav"></div>
    <div class="text-light" style="background-image: url('https://source.unsplash.com/1920x1080/?nature');
                                   position: absolute;
                                   left: 0;
                                   top: 0;
                                   opacity: 0.6;
                                   z-index: -1;
                                   min-height: 100vh;
                                   min-width: 100vw;">
    </div>

    <div class="container" style="padding-top: 20vh; display: flex; flex-direction: column; align-items: center;">
        <h1 class="display-3">Reservation management made easy.</h1>
        <p class="lead">Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Numquam in quia natus magnam ducimus quas molestias velit vero maiores.
            Eaque sunt laudantium voluptas. Fugiat molestiae ipsa delectus iusto vel quod.</p>
        <a href="/reservations" class="btn btn-success btn-lg my-2">Reserve an Amenity</a>
    </div>
</div>

<script th:src="@{/webjars/jquery/3.0.0/jquery.min.js}"></script>
<script th:src="@{/webjars/popper.js/1.12.9-1/umd/popper.min.js}"></script>
<script th:src="@{/webjars/bootstrap/4.0.0-2/js/bootstrap.min.js}"></script>

</body>
</html>
```

Cela devrait ressembler à ceci :

![Image](https://erinc.io/wp-content/uploads/2021/05/image-1024x533.png)

Nous allons créer une autre page à afficher si l'utilisateur est déjà connecté. Pour garder cela simple, nous la traiterons également comme une page d'accueil, et si l'utilisateur est connecté, il pourra voir ses réservations sur la page d'accueil. 

C'est également bon en termes de praticité pour l'utilisateur, car cela réduit les étapes qu'il doit suivre pour voir ses réservations. 

Nous allons maintenant créer cette page comme un autre point de terminaison. Mais après avoir ajouté la connexion à notre application, nous afficherons cette page précédente si l'utilisateur n'est pas connecté et la page suivante s'il est connecté, de manière dynamique.

Avant de commencer à travailler sur notre nouvelle page, ajoutons un autre mappage à **HomeController** qui retournera notre nouvelle page. Nous fusionnerons ensuite ces deux contrôleurs :

```java
package com.amenity_reservation_system;

import com.amenity_reservation_system.domain.User;
import com.amenity_reservation_system.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class HomeController {

    final UserService userService;

    public HomeController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/")
    public String index(Model model) {
        return "index";
    }

    @GetMapping("/reservations")
    public String reservations(Model model) {
        User user = userService.get(10000L);
        model.addAttribute("user", user);

        return "reservations";
    }
}
```

Si une requête est reçue à "/reservations", ce code appellera notre userService et demandera l'utilisateur avec l'id 10000L. Ensuite, il ajoutera cet utilisateur au **Model**. 

La vue accédera à ce modèle et présentera les informations sur les réservations de cet utilisateur. Nous avons également injecté le service utilisateur pour l'utiliser.

Naviguez vers le dossier templates si vous n'y êtes pas déjà et créez un autre fichier appelé "reservations.html" :

```
touch reservations.html
```

Copiez et collez le code suivant :

```html
<!DOCTYPE HTML>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8"/>
    <title>Reservations</title>

    <link th:rel="stylesheet" th:href="@{/webjars/bootstrap/4.0.0-2/css/bootstrap.min.css} "/>
</head>
<body>

<div>
    <div th:insert="fragments/nav :: nav"></div>
    <div class="container" style="padding-top: 10vh; display: flex; flex-direction: column; align-items: center;">
        <h3>Welcome <span th:text=" ${user.getFullName()}"></span></h3>
        <br>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Amenity</th>
                    <th scope="col">Date</th>
                    <th scope="col">Start Time</th>
                    <th scope="col">End Time</th>
                </tr>
            </thead>
            <tbody>
                <tr th:each="reservation : ${user.getReservations()}">
                    <td th:text="${reservation.getAmenityType()}"></td>
                    <td th:text="${reservation.getReservationDate()}"></td>
                    <td th:text="${reservation.getStartTime()}"></td>
                    <td th:text="${reservation.getEndTime()}"></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<script th:src="@{/webjars/jquery/3.0.0/jquery.min.js}"></script>
<script th:src="@{/webjars/popper.js/1.12.9-1/umd/popper.min.js}"></script>
<script th:src="@{/webjars/bootstrap/4.0.0-2/js/bootstrap.min.js}"></script>

</body>
</html>
```

Dans ce modèle **Thymeleaf**, nous importons **Bootstrap** et **Thymeleaf** comme avant et nous accédons à la variable utilisateur qui a été ajoutée au modèle dans notre contrôleur en utilisant la syntaxe ${}. 

Pour accéder aux données, Thymeleaf utilise les méthodes getter de l'objet et nous pouvons imprimer ces informations en utilisant l'attribut `th:text`. Thymeleaf prend également en charge les boucles. Dans le `tbody`, nous avons une boucle `th:each`, que nous pouvons considérer comme une boucle foreach sur les réservations d'un utilisateur. Nous parcourons donc les réservations et les affichons dans un tableau.

Vous pouvez avoir une erreur qui dit quelque chose comme "Impossible d'initialiser le proxy, ... chargement paresseux". Cela est dû au fait que la vue essaie d'accéder à l'objet des réservations alors qu'il n'existe pas encore. Pour nous en débarrasser, nous pouvons modifier les lignes suivantes dans **User.java** :

```java
    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private Set<Reservation> reservations = new HashSet<>();
```

Nous ajoutons une déclaration pour dire à Java de récupérer cet objet de manière proactive.

Maintenant, vous devriez pouvoir voir la page des réservations :

![Image](https://erinc.io/wp-content/uploads/2021/05/image-1-1024x488.png)

### Comment créer une réservation

Nous avons également besoin d'un moyen de créer de nouvelles réservations, alors construisons ce mécanisme pour notre utilisateur pré-créé comme nous l'avons fait avec l'affichage des réservations. Ensuite, nous pourrons l'altérer pour montrer les réservations de l'utilisateur actuellement connecté.

Avant de continuer, nous devons mettre à jour les formats de date dans notre fichier **Reservation.java** pour éviter tout problème de non-correspondance de format. Assurez-vous que vos formats pour ces variables sont les mêmes :

```java
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    @Column(nullable = false)
    private LocalDate reservationDate;

    @DateTimeFormat(pattern = "HH:mm")
    @Column
    private LocalTime startTime;

    @DateTimeFormat(pattern = "HH:mm")
    @Column
    private LocalTime endTime;
```

Dans la section précédente, nous avons créé notre contrôleur **reservations**. Maintenant, nous devons le modifier un peu pour ajouter un autre attribut au modèle. 

Nous avons appris comment nous pouvons accéder aux objets qui sont ajoutés au modèle en utilisant la syntaxe ${}. Maintenant, nous allons faire quelque chose de similaire :

```java
@GetMapping("/reservations")
    public String reservations(Model model, HttpSession session) {
        User user = userService.get(10000L);
        session.setAttribute("user", user);
        Reservation reservation = new Reservation();
        model.addAttribute("reservation", reservation);

        return "reservations";
    }
```

Nous mettons à jour notre contrôleur de réservations pour déplacer l'objet utilisateur vers la session car nous voulons qu'il soit accessible depuis une autre méthode de contrôleur et pas seulement depuis un modèle. 

Pensez-y de cette manière : une fois qu'un utilisateur est connecté, ce compte utilisateur sera responsable de chaque action entreprise après ce point. Vous pouvez considérer la Session comme une variable globale accessible de partout. 

Nous créons également un objet **Réservation** et l'ajoutons au modèle. **Thymeleaf** accédera à cet objet nouvellement créé dans notre modèle de vue de modèle et il appellera les setters pour définir ses champs.

Maintenant, créons la vue pour créer la réservation. Nous allons utiliser [Bootstrap Modal](https://getbootstrap.com/docs/4.0/components/modal/) pour afficher un formulaire modal après qu'un bouton a été cliqué.

Nous pouvons d'abord gérer le code pour appeler le modal que nous allons créer à l'étape suivante, passer au fichier reservations.html et ajouter ce fragment après la balise de tableau que nous avons ajoutée précédemment :

```html
<button
  type="button"
  class="btn btn-primary"
  data-toggle="modal"
  data-target="#createReservationModal"
>
  Create Reservation
</button>

<!-- Modal -->
<div
  th:insert="fragments/modal :: modal"
  th:with="reservation=${reservation}"
></div>
```

Ce bouton déclenchera notre modal. Dans la div, nous insérons ce modal que nous allons créer et nous utilisons la balise `th:with` pour passer l'objet de réservation qui a été mis dans le modèle dans notre contrôleur. Si nous ne faisons pas cela, le fragment ne connaîtra pas l'objet de réservation.

Nous devons également changer la façon dont nous accédons à l'utilisateur pour imprimer son nom car nous ne le stockons plus dans le modal mais dans la session :

```html
<h3>Welcome <span th:text=" ${session.user.getFullName()}"></span></h3>

```

Ainsi, votre fichier final **reservations.html** devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
  <head>
    <meta charset="UTF-8" />
    <title>Reservations</title>

    <link
      th:rel="stylesheet"
      th:href="@{/webjars/bootstrap/4.0.0-2/css/bootstrap.min.css} "
    />
  </head>
  <body>
    <div>
      <div th:insert="fragments/nav :: nav"></div>
      <div
        class="container"
        style="padding-top: 10vh; display: flex; flex-direction: column; align-items: center;"
      >
        <h3>Welcome <span th:text=" ${session.user.getFullName()}"></span></h3>
        <br />
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Amenity</th>
              <th scope="col">Date</th>
              <th scope="col">Start Time</th>
              <th scope="col">End Time</th>
            </tr>
          </thead>
          <tbody>
            <tr th:each="reservation : ${session.user.getReservations()}">
              <td th:text="${reservation.getAmenityType()}"></td>
              <td th:text="${reservation.getReservationDate()}"></td>
              <td th:text="${reservation.getStartTime()}"></td>
              <td th:text="${reservation.getEndTime()}"></td>
            </tr>
          </tbody>
        </table>

        <button
          type="button"
          class="btn btn-primary"
          data-toggle="modal"
          data-target="#createReservationModal"
        >
          Create Reservation
        </button>

        <!-- Modal -->
        <div
          th:insert="fragments/modal :: modal"
          th:with="reservation=${reservation}"
        ></div>
      </div>
    </div>

    <script th:src="@{/webjars/jquery/3.0.0/jquery.min.js}"></script>
    <script th:src="@{/webjars/popper.js/1.12.9-1/umd/popper.min.js}"></script>
    <script th:src="@{/webjars/bootstrap/4.0.0-2/js/bootstrap.min.js}"></script>
  </body>
</html>
```

Nous sommes maintenant prêts à créer le fragment modal. Nous pouvons créer un fragment pour le modal comme nous l'avons fait avec la barre de navigation :

```bash
pwd
/src/main/resources
cd templates/fragments
touch modal.html

```

Et collez le code de modèle suivant :

```html
<html lang="en" xmlns:th="http://www.thymeleaf.org">
  <body>
    <div
      class="modal fade"
      th:fragment="modal"
      id="createReservationModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="createReservationModalTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="createReservationModalTitle">
              Create Reservation
            </h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <div class="modal-body">
            <form
              action="#"
              th:action="@{/reservations-submit}"
              th:object="${reservation}"
              method="post"
            >
              <div class="form-group row">
                <label for="type-select" class="col-2 col-form-label"
                  >Amenity</label
                >
                <div class="col-10">
                  <select
                    class="form-control"
                    id="type-select"
                    th:field="*{amenityType}"
                  >
                    <option value="POOL">POOL</option>
                    <option value="SAUNA">SAUNA</option>
                    <option value="GYM">GYM</option>
                  </select>
                </div>
              </div>
              <div class="form-group row">
                <label for="start-date" class="col-2 col-form-label"
                  >Date</label
                >
                <div class="col-10">
                  <input
                    class="form-control"
                    type="date"
                    id="start-date"
                    name="trip-start"
                    th:field="*{reservationDate}"
                    value="2018-07-22"
                    min="2021-05-01"
                    max="2021-12-31"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="start-time" class="col-2 col-form-label"
                  >From</label
                >
                <div class="col-10">
                  <input
                    class="form-control"
                    type="time"
                    id="start-time"
                    name="time"
                    th:field="*{startTime}"
                    min="08:00"
                    max="19:30"
                    required
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="end-time" class="col-2 col-form-label">To</label>
                <div class="col-10">
                  <input
                    class="form-control"
                    type="time"
                    id="end-time"
                    name="time"
                    th:field="*{endTime}"
                    min="08:30"
                    max="20:00"
                    required
                  />
                  <small>Amenities are available from 8 am to 8 pm</small>
                </div>
              </div>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-dismiss="modal"
                >
                  Close
                </button>
                <button type="submit" class="btn btn-primary" value="Submit">
                  Save changes
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
```

Il y a quelques points importants que vous devez noter ici.

Remarquez comment nous accédons à l'objet de réservation dans la balise de formulaire :

```html
<form
  action="#"
  th:action="@{/reservations-submit}"
  th:object="${reservation}"
  method="post"
></form>
```

La balise **`th:object`** associe ce formulaire à l'objet de réservation que nous avons créé précédemment. **`th:action`** détermine où cet objet sera envoyé lorsque le formulaire est soumis, et notre méthode de soumission sera **POST**. Nous créerons ce contrôleur avec le mappage vers **/reservations-submit** après cette étape.

Nous utilisons la balise **`th:field`** pour lier les entrées aux champs de notre objet de réservation. Thymeleaf appelle les setters de l'objet de réservation chaque fois que la valeur du champ d'entrée change.

Maintenant, créons le contrôleur qui recevra ce formulaire. Allez dans **HomeController** et ajoutez la méthode suivante :

```java
@PostMapping("/reservations-submit")
    public String reservationsSubmit(@ModelAttribute Reservation reservation,
                                     @SessionAttribute("user") User user) {

        // Save to DB after updating
        assert user != null;
        reservation.setUser(user);
        reservationService.create(reservation);
        Set<Reservation> userReservations = user.getReservations();
        userReservations.add(reservation);
        user.setReservations(userReservations);
        userService.update(user.getId(), user);
        return "redirect:/reservations";
    }
```

Et ajoutez également le **ReservationService** à nos dépendances :

```java
    final UserService userService;
    final ReservationService reservationService;

    public HomeController(UserService userService, ReservationService reservationService) {
        this.userService = userService;
        this.reservationService = reservationService;
    }
```

Après que notre fragment modal a posté l'objet de réservation à ce contrôleur, cet objet sera lié avec l'annotation **@ModelAttribute**. Nous avons également besoin de l'utilisateur, donc nous utilisons **@SessionAttribute** pour obtenir une référence à celui-ci.

Les champs de l'objet de réservation doivent tous être définis par le formulaire. Maintenant, nous devons simplement l'enregistrer dans la base de données. 

Nous le faisons en appelant la méthode **create**. Ensuite, nous ajoutons la nouvelle Réservation à la liste des réservations de l'utilisateur et mettons à jour l'utilisateur pour refléter ces changements. Nous redirigeons ensuite l'utilisateur vers la page des réservations pour montrer la liste des réservations mise à jour.

Votre page de réservations devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/LFJE0Ad---Imgur.png)

Et lorsque vous cliquez sur le bouton, la modal de création de réservation devrait s'afficher.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-42.png)

## Comment ajouter l'authentification et l'autorisation à l'application

Nous allons utiliser **Spring Security** pour ajouter l'authentification et l'autorisation à notre application. Nous voulons nous assurer que personne ne peut voir les réservations des autres et que les utilisateurs doivent être connectés pour créer des réservations. 

Si vous souhaitez en savoir plus, j'ai écrit un article qui fournit un aperçu de [Spring Security](https://auth0.com/blog/spring-security-overview/). 

Nous allons garder cela simple et utiliser principalement les paramètres par défaut car c'est un sujet difficile en soi. Si vous souhaitez apprendre à configurer correctement l'authentification et l'autorisation Spring Security, vous pouvez consulter mon [article](https://www.freecodecamp.org/news/how-to-setup-jwt-authorization-and-authentication-in-spring/) à ce sujet. 

Nous devons ajouter "Spring Security" et "Thymeleaf Spring Security" à nos dépendances, alors ouvrez votre pom.xml et ajoutez ce qui suit à votre liste de dépendances :

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<dependency>
    <groupId>org.thymeleaf.extras</groupId>
    <artifactId>thymeleaf-extras-springsecurity5</artifactId>
    <version>3.0.4.RELEASE</version>
</dependency>
```

Maintenant, par défaut, Spring Security rend tous les points de terminaison protégés, donc nous devons le configurer pour permettre de voir la page d'accueil. 

Créons un dossier de configuration pour contenir notre fichier **WebSecurityConfig**. En supposant que vous êtes dans le dossier racine :

```bash
cd /src/main/java/com/amenity_reservation_system
mkdir config && cd config
touch WebSecurityConfig.java
```

Voici le contenu de votre fichier de configuration :

```java
package com.amenity_reservation_system.config;

import com.amenity_reservation_system.service.UserDetailsServiceImpl;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    private final UserDetailsServiceImpl userDetailsService;

    private final BCryptPasswordEncoder bCryptPasswordEncoder;

    public WebSecurityConfig(UserDetailsServiceImpl userDetailsService, BCryptPasswordEncoder bCryptPasswordEncoder) {
        this.userDetailsService = userDetailsService;
        this.bCryptPasswordEncoder = bCryptPasswordEncoder;
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .authorizeRequests()
                .antMatchers("/", "/webjars/**").permitAll()
                .anyRequest().authenticated()
                .and()
                .formLogin()
                .permitAll()
                .and()
                .logout()
                .permitAll()
                .logoutSuccessUrl("/");
    }

    public void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService).passwordEncoder(bCryptPasswordEncoder);
    }

}
```

Je ne vais pas entrer dans les détails, mais voici un résumé de ce qui s'est passé ici : 

* nous avons configuré Spring Security pour permettre toutes les requêtes faites à la page d'accueil ("/")
* nous avons configuré nos styles ("/webjars/**")
* nous lui avons demandé de nous fournir des formulaires de connexion et de déconnexion 
* et nous lui avons demandé de permettre également les requêtes à ceux-ci et de rediriger vers la page d'accueil après que la déconnexion soit réussie

N'est-ce pas incroyable ce que vous pouvez accomplir avec seulement quelques déclarations ?

Nous avons également configuré notre **AuthenticationManagerBuilder** pour utiliser bCryptPasswordEncoder et userDetailsService. Mais attendez, nous n'avons ni l'un ni l'autre pour l'instant, et votre IDE peut déjà se plaindre de cela. Alors créons-les.

Avant de continuer, il peut être judicieux d'ajouter les champs **username** et passwordHash à notre classe **User**. Nous les utiliserons pour authentifier l'utilisateur au lieu d'utiliser leur nom complet. Ensuite, nous les ajouterons au constructeur.

```java
package com.amenity_reservation_system.model;

import java.time.OffsetDateTime;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.*;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class User {

    @Id
    @Column(nullable = false, updatable = false)
    @SequenceGenerator(
            name = "primary_sequence",
            sequenceName = "primary_sequence",
            allocationSize = 1,
            initialValue = 10000
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "primary_sequence"
    )
    private Long id;

    @Column(nullable = false, unique = true)
    private String fullName;

    @Column(nullable = false, unique = true)
    private String username;

    @Column
    private String passwordHash;

    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private Set<Reservation> reservations = new HashSet<>();

    @Column(nullable = false, updatable = false)
    private OffsetDateTime dateCreated;

    @Column(nullable = false)
    private OffsetDateTime lastUpdated;

    @PrePersist
    public void prePersist() {
        dateCreated = OffsetDateTime.now();
        lastUpdated = dateCreated;
    }

    @PreUpdate
    public void preUpdate() {
        lastUpdated = OffsetDateTime.now();
    }

    public User(String fullName, String username, String passwordHash) {
        this.fullName = fullName;
        this.username = username;
        this.passwordHash = passwordHash;
    }
}
```

Créez un fichier appelé **UserDetailsServiceImpl** sous le dossier des services :

```bash
cd service
touch UserDetailsServiceImpl.java
```

```java
package com.amenity_reservation_system.service;

import com.amenity_reservation_system.model.User;
import com.amenity_reservation_system.repos.UserRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {

    private UserRepository userRepository;

    public UserDetailsServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        final User user = userRepository.findUserByUsername(username);

        if (user == null) {
            throw new UsernameNotFoundException(username);
        }

        UserDetails userDetails = org.springframework.security.core.userdetails.User.withUsername(
                user.getUsername()).password(user.getPwHash()).roles("USER").build();

        return userDetails;
    }
}

```

Cela indique essentiellement à Spring Security que nous voulons utiliser l'entité **User** que nous avons créée précédemment en obtenant l'objet **User** de notre base de données et en utilisant la méthode JPA sur notre dépôt. Mais encore une fois, nous n'avons pas la méthode **findUserByUsername** sur notre **UserRepository**. Vous pouvez essayer de corriger cela par vous-même comme un défi, c'est vraiment simple.

Rappelez-vous, nous n'avons pas besoin d'écrire des requêtes. Il suffit de fournir la signature et de laisser JPA faire le travail.

```java
package com.amenity_reservation_system.repos;

import com.amenity_reservation_system.model.User;
import org.springframework.data.jpa.repository.JpaRepository;


public interface UserRepository extends JpaRepository<User, Long> {

    User findUserByUsername(String username);
}

```

Nous avons également besoin d'un bean **BCryptPasswordEncoder** pour satisfaire cette dépendance dans **WebSecurityConfig** et pour le faire fonctionner. Modifions notre classe principale pour ajouter un bean et changer les paramètres du constructeur pour donner à notre **User** prédéfini un nom d'utilisateur.

```java
package com.amenity_reservation_system;

import com.amenity_reservation_system.model.AmenityType;
import com.amenity_reservation_system.model.Reservation;
import com.amenity_reservation_system.model.User;
import com.amenity_reservation_system.repos.ReservationRepository;
import com.amenity_reservation_system.repos.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZoneId;
import java.util.Date;


@SpringBootApplication
public class AmenityReservationSystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(AmenityReservationSystemApplication.class, args);
    }


    @Bean
    public CommandLineRunner loadData(UserRepository userRepository,
                                      ReservationRepository reservationRepository) {
    return (args) -> {
      User user =
          userRepository.save(
              new User("Yigit Kemal Erinc",
                      "yigiterinc",
                      bCryptPasswordEncoder().encode("12345")));
      DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
      Date date = new Date();
      LocalDate localDate = date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
      Reservation reservation =
          Reservation.builder()
              .reservationDate(localDate)
              .startTime(LocalTime.of(12, 00))
              .endTime(LocalTime.of(13, 00))
              .user(user)
              .amenityType(AmenityType.POOL)
              .build();

      reservationRepository.save(reservation);
    };
    }

    @Bean
    public BCryptPasswordEncoder bCryptPasswordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

Votre application devrait être prête à compiler maintenant et elle devrait déjà vous rediriger vers la page de connexion si vous envoyez une requête à "/reservations". 

Il serait bien d'avoir des boutons de connexion et de déconnexion sur la barre de navigation, et nous voulons montrer la connexion si l'utilisateur n'est pas authentifié et la déconnexion sinon. Nous pouvons le faire de cette manière dans **nav.html** :

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org" xmlns:sec="http://www.w3.org/1999/xhtml">
<body>
<nav th:fragment="nav" class="navbar navbar-expand navbar-dark bg-primary">
    <div class="navbar-nav w-100">
        <a class="navbar-brand text-color" href="/">Amenities Reservation System</a>
    </div>
        <a sec:authorize="isAnonymous()"
           class="navbar-brand text-color" th:href="@{/login}">Log in</a>
        <a sec:authorize="isAuthenticated()"
               class="navbar-brand text-color" th:href="@{/logout}">Log out</a>
</nav>
</body>
</html>
```

Le lien de connexion devrait maintenant être visible sur la barre de navigation.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-10-at-02.19.09.png)
_Page d'accueil lorsque vous n'êtes pas connecté_

## Comment afficher les réservations d'un utilisateur connecté

Notre page de réservations affiche actuellement les réservations d'un utilisateur codé en dur et non les réservations de l'utilisateur connecté. 

```java
    @GetMapping("/reservations")
    public String reservations(Model model, HttpSession session) {
        User user = userService.get(10000L);
        session.setAttribute("user", user);
        Reservation reservation = new Reservation();
        model.addAttribute("reservation", reservation);

        return "reservations";
    }

```

Nous devons afficher les réservations de l'utilisateur actuellement connecté. Pour y parvenir, nous devons utiliser Spring Security.

Allez dans la classe **HomeController** (je sais, ce nom est un peu problématique pour l'instant) et remplacez-la par le code suivant :

```java
@GetMapping("/reservations")
    public String reservations(Model model, HttpSession session) {
        UserDetails principal = (UserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        String name = principal.getUsername();
        User user = userService.getUserByUsername(name);

        // This should always be the case 
        if (user != null) {
            session.setAttribute("user", user);

            // Empty reservation object in case the user creates a new reservation
            Reservation reservation = new Reservation();
            model.addAttribute("reservation", reservation);

            return "reservations";
        }

        return "index";    
        }
```

Puisque nous avons ajouté Spring Security au projet, il crée automatiquement l'objet **Authentication** en coulisses – nous l'obtenons à partir de **SecurityContextHolder**. 

Nous récupérons l'objet **[UserDetails](https://docs.spring.io/spring-security/site/docs/current/api/org/springframework/security/core/userdetails/UserDetails.html#:~:text=Interface%20UserDetails&text=Provides%20core%20user%20information.,later%20encapsulated%20into%20Authentication%20objects.)** qui stocke les informations relatives à l'utilisateur. Ensuite, nous vérifions si l'objet utilisateur est null. Cela devrait toujours être le cas puisque _reservations_ est un point de terminaison protégé et l'utilisateur doit être connecté pour voir cette page – mais il est toujours bon de s'assurer que tout est comme prévu.

Ensuite, nous appelons la classe **UserService** pour obtenir l'objet **User** qui a ce nom d'utilisateur – mais nous n'avons pas encore ajouté la méthode **getUserByUsername**. Alors, passons à **UserService** et ajoutons cette méthode simple.

```java
    public User getUserByUsername(String username) {
        return userRepository.findUserByUsername(username);
    }
```

Maintenant, vous devriez pouvoir voir les réservations de l'utilisateur connecté. Vous pouvez essayer cela en ajoutant un autre utilisateur et en créant des réservations pour cet utilisateur également. 

### Comment vérifier la capacité 

Nous n'avons actuellement aucun mécanisme pour stocker la capacité de chaque type d'équipement. Nous devons stocker celles-ci d'une manière ou d'une autre et également vérifier qu'il y a suffisamment de capacité avant d'approuver une réservation. 

À cette fin, créons une classe appelée **Capacité** sous notre dossier de modèle.

```java
package com.amenity_reservation_system.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Capacity {

    @Id
    @Column(nullable = false, updatable = false)
    @SequenceGenerator(
            name = "primary_sequence",
            sequenceName = "primary_sequence",
            allocationSize = 1,
            initialValue = 10000
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "primary_sequence"
    )
    private Long id;

    @Column(nullable = false, unique = true)
    @Enumerated(EnumType.STRING)
    private AmenityType amenityType;

    @Column(nullable = false)
    private int capacity;

    public Capacity(AmenityType amenityType, int capacity) {
        this.amenityType = amenityType;
        this.capacity = capacity;
    }
}
```

C'est l'entité qui représentera notre construct logique à stocker dans notre base de données. C'est essentiellement une entrée de carte avec un AmenityType et sa capacité correspondante.

Nous avons également besoin d'un dépôt pour stocker les entrées de **Capacité**, alors créons le CapacityRepository sous le dossier **repos**.

```java
package com.amenity_reservation_system.repos;

import com.amenity_reservation_system.model.Capacity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CapacityRepository extends JpaRepository<Capacity, Long> {
}

```

Nous devons remplir cette nouvelle table avec les capacités initiales. Nous pourrions lire les capacités initiales à partir d'un fichier de configuration ou autre chose, mais gardons cela simple et codons-le en dur en utilisant loadData dans notre méthode principale.

```java
package com.amenity_reservation_system;

import com.amenity_reservation_system.model.AmenityType;
import com.amenity_reservation_system.model.Capacity;
import com.amenity_reservation_system.model.Reservation;
import com.amenity_reservation_system.model.User;
import com.amenity_reservation_system.repos.CapacityRepository;
import com.amenity_reservation_system.repos.ReservationRepository;
import com.amenity_reservation_system.repos.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZoneId;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class AmenityReservationSystemApplication {

  private Map<AmenityType, Integer> initialCapacities =
      new HashMap<>() {
        {
          put(AmenityType.GYM, 20);
          put(AmenityType.POOL, 4);
          put(AmenityType.SAUNA, 1);
        }
      };

  public static void main(String[] args) {
    SpringApplication.run(AmenityReservationSystemApplication.class, args);
  }

  @Bean
  public CommandLineRunner loadData(
      UserRepository userRepository,
      CapacityRepository capacityRepository) {
    return (args) -> {
      userRepository.save(
          new User("Yigit Kemal Erinc", "yigiterinc", bCryptPasswordEncoder().encode("12345")));

      for (AmenityType amenityType : initialCapacities.keySet()) {
        capacityRepository.save(new Capacity(amenityType, initialCapacities.get(amenityType)));
      }
    };
  }

  @Bean
  public BCryptPasswordEncoder bCryptPasswordEncoder() {
    return new BCryptPasswordEncoder();
  }
}

```

J'ai simplement ajouté les capacités à l'intérieur de la carte **initialCapacities**, puis enregistré celles-ci dans le **CapacityRepository** à l'intérieur de la méthode **loadData**.

Nous pouvons maintenant vérifier si le nombre de réservations à l'heure demandée dépasse la capacité et rejeter la demande de réservation si c'est le cas.

Voici la logique : nous devons récupérer le nombre de réservations qui sont le même jour et qui se chevauchent avec cette demande actuelle. Ensuite, nous devons récupérer la capacité pour ce type d'équipement, et si la capacité est dépassée, nous pouvons lancer une exception. 

Par conséquent, nous avons besoin d'une requête pour obtenir le nombre de réservations potentiellement chevauchantes. Ce n'est pas la requête la plus facile à écrire, mais JPA est très pratique et nous pouvons accéder à cette requête à l'intérieur de notre **ReservationRepository** sans avoir besoin d'écrire de SQL ou de HQL (Hibernate Query Language). 

Je vous encourage à essayer par vous-même avant de continuer, car c'est la seule raison pour laquelle j'ai inclus ce concept de capacité dans ce tutoriel (pour montrer un exemple de requête JPA plus avancée).

Voici à quoi ressemble la méthode create de **ReservationService**. Vous devez remplacer le 0 par un appel à reservationRepository pour obtenir le nombre de réservations chevauchantes. 

Si le nombre actuel de réservations chevauchantes est égal à la capacité, cela signifie que la suivante la dépassera, donc nous lançons l'exception.

```java
public Long create(final Reservation reservation) {
        int capacity = capacityRepository.findByAmenityType(reservation.getAmenityType()).getCapacity();
        int overlappingReservations = 0; // TODO

        if (overlappingReservations >= capacity) {
            // Throw a custom exception
        }

        return reservationRepository.save(reservation).getId();
    }
```

Pour trouver les réservations chevauchantes, il y a quelques conditions que nous devons vérifier :

Tout d'abord, la date de réservation doit être la même que la date dans la demande.

1. L'heure de début peut être avant l'heure de début d'une nouvelle demande. Dans ce cas, l'heure de fin doit être plus tardive que notre demande, afin de chevaucher. (startTimeBeforeAndEndTimeAfter)
2. Ou, endTime peut être après mais startTime peut en fait être entre startTime et endTime de la demande. (endTimeAfterOrStartTimeBetween)

Donc notre requête finale doit retourner toutes les réservations qui correspondent à l'une de ces 2 possibilités.

Nous pouvons l'exprimer comme ceci : 

```java
List<Reservation> findReservationsByReservationDateAndStartTimeBeforeAndEndTimeAfterOrStartTimeBetween
            (LocalDate reservationDate, LocalTime startTime, LocalTime endTime, LocalTime betweenStart, LocalTime betweenEnd);

```

Et la méthode create finale ressemble à ceci :

```java
 public Long create(final Reservation reservation) {
        int capacity = capacityRepository.findByAmenityType(reservation.getAmenityType()).getCapacity();
        int overlappingReservations = reservationRepository
                .findReservationsByReservationDateAndStartTimeBeforeAndEndTimeAfterOrStartTimeBetween(
                        reservation.getReservationDate(),
                        reservation.getStartTime(), reservation.getEndTime(),
                        reservation.getStartTime(), reservation.getEndTime()).size();

        if (overlappingReservations >= capacity) {
            throw new CapacityFullException("This amenity's capacity is full at desired time");
        }

        return reservationRepository.save(reservation).getId();
    }
```

Vous n'avez pas besoin de vous soucier de l'exception personnalisée, mais si vous êtes intéressé par cela, voici le code :

```java
package com.amenity_reservation_system.exception;

public class CapacityFullException extends RuntimeException {
    public CapacityFullException(String message) {
        super(message);
    }
}
```

Nous devrions normalement afficher une modale d'erreur si la capacité est dépassée, mais je vais sauter cela pour éviter les répétitions d'interface utilisateur. Vous pouvez essayer cela comme un défi si vous le souhaitez.

## Conclusion

Dans ce tutoriel, nous avons appris beaucoup de technologies qui rendent le développement avec Spring Boot plus facile et plus rapide. 

Je pense que beaucoup de gens sous-estiment le framework en termes de vitesse de développement et de la qualité du travail résultant. 

En supposant que vous êtes à l'aise avec la technologie, je dirais que Spring Boot n'est pas plus lent (en développement) que n'importe quel autre framework backend si vous faites tout de manière moderne. 

Vous pouvez trouver le code complet dans ce dépôt :

[https://github.com/yigiterinc/amenity-reservation-system.git](https://github.com/yigiterinc/amenity-reservation-system.git)

Si vous êtes intéressé à lire plus de contenu comme celui-ci, n'hésitez pas à vous abonner à mon blog à [https://erinc.io](https://erinc.io/) pour être informé de mes nouveaux articles.