---
title: Comment développer une application CRUD avec Spring Boot, Neon Postgres et
  Azure App Service
subtitle: ''
author: Abhinav Pandey
co_authors: []
series: null
date: '2024-07-26T19:14:36.000Z'
originalURL: https://freecodecamp.org/news/build-a-crud-app-spring-boot-neon-postgres
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/neon-banner.png
tags:
- name: Azure
  slug: azure
- name: crud
  slug: crud
- name: postgres
  slug: postgres
- name: spring-boot
  slug: spring-boot
seo_title: Comment développer une application CRUD avec Spring Boot, Neon Postgres
  et Azure App Service
seo_desc: 'In this article, we''ll explore how to develop a CRUD (Create, Read, Update,
  Delete) application using Spring Boot and Neon Postgres.

  We''ll also deploy the application on Azure App Service and make it production-ready
  by setting up features like autos...'
---

Dans cet article, nous allons explorer comment développer une application CRUD (Create, Read, Update, Delete) en utilisant Spring Boot et [Neon Postgres](https://neon.tech/).

Nous allons également déployer l'application sur [Azure App Service](https://azure.microsoft.com/fr-fr/products/app-service) et la rendre prête pour la production en configurant des fonctionnalités comme le scaling automatique et plusieurs environnements.

Vous apprendrez comment Neon Postgres peut faciliter vos processus de développement et de déploiement.

## Voici ce que nous allons couvrir :

* Configuration d'une base de données Neon Postgres et exploration de ses fonctionnalités
* Construction d'une application CRUD utilisant Spring Boot et déploiement de l'application sur Azure App Service
* Pourquoi Neon est adapté pour une infrastructure auto-scalable
* Le branchement de base de données dans Neon Postgres et comment il peut faciliter le flux de développement

## Prérequis
- Connaissance pratique de Java, Maven et Spring Boot
- Bases des bases de données SQL
- Compréhension des services serverless et cloud
- Familiarité avec les processus de test et de déploiement

## Table des matières
- [Qu'est-ce que Neon Postgres ?](#heading-quest-ce-que-neon-postgres)
- [Comment configurer la base de données](#heading-comment-configurer-la-base-de-donnees)
    - [Créer la base de données](#heading-creer-la-base-de-donnees)
- [Comment construire l'application CRUD Spring Boot](#heading-comment-construire-lapplication-crud-spring-boot)
    - [Créer une classe d'entité](#heading-creer-une-classe-dentite)
    - [Créer un dépôt](#heading-creer-un-depot)
    - [Créer un contrôleur REST](#heading-creer-un-controleur-rest)
    - [Configurer la base de données](#heading-configurer-la-base-de-donnees)
- [Comment déployer sur Azure App Service](#heading-comment-deployer-sur-azure-app-service)
    - [Créer une nouvelle application Web](#heading-creer-une-nouvelle-application-web)
    - [Déployer l'application](#heading-deployer-lapplication)
    - [Accéder à l'application](#heading-acceder-a-lapplication)
- [Comment configurer le scaling automatique](#heading-comment-configurer-le-scaling-automatique)
    - [Scaling automatique dans Azure](#heading-scaling-automatique-dans-azure)
    - [Scaling automatique dans Neon](#heading-scaling-automatique-dans-neon)
- [Comment configurer les branches de base de données dans Neon](#heading-comment-configurer-les-branches-de-base-de-donnees-dans-neon)
- [Résumé](#heading-resume)

## Qu'est-ce que Neon Postgres ?

Neon est une plateforme de base de données Postgres serverless entièrement gérée. Elle offre des fonctionnalités telles que la haute disponibilité, les sauvegardes automatiques et des options de scaling pour gérer différents niveaux de trafic.

Neon est conçu pour être économique et convivial pour les développeurs, et il se concentre sur la fourniture d'une expérience transparente pour les développeurs.

En plus des fonctionnalités standard de Postgres, il fournit des capacités comme le branchement de base de données, vous permettant de créer des branches de type Git de la base de données pour différents usages.

## Comment configurer la base de données

Pour commencer, explorons comment vous pouvez configurer une base de données Neon pour votre application.

Tout d'abord, vous devrez [créer un compte](https://console.neon.tech/signup) sur le site web de Neon. Il n'est pas nécessaire de fournir une carte de crédit pour s'inscrire, et vous êtes automatiquement configuré avec le niveau gratuit pour commencer.

Voici une [comparaison des prix et des fonctionnalités](https://neon.tech/pricing) des plans Neon :

![Une capture d'écran des plans tarifaires de Neon listant les fonctionnalités gratuites et payantes](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Finxumg46sf92ffre6l2q.png)
_Plans tarifaires de Neon_

Dans le niveau gratuit, nous obtenons 0,5 Go de stockage avec un calcul de base, ce qui est suffisant pour jouer avec la base de données et construire de petites applications.

### Créer la base de données

Une fois inscrit, vous pouvez accéder au tableau de bord et créer un nouveau projet.

Commencez par remplir les options de nom de projet, de région et de version de Postgres. En plus de cela, nous pouvons choisir deux options supplémentaires :

* **taille du calcul** – Vous pouvez choisir une taille de calcul minimale et maximale pour la base de données. Cela est utile pour le scaling automatique de la base de données en fonction de la charge.
* **temps de suspension** – Vous pouvez définir un temps après lequel la base de données sera suspendue si elle n'est pas utilisée. Cela est utile pour économiser des coûts lorsque la base de données n'est pas utilisée.

![Formulaire avec les spécifications requises lors de la création d'une base de données](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fggwuvqtb8ydl3mxd1dak.png)
_Création d'un projet de base de données dans Neon_

Une fois que vous avez soumis le formulaire, Neon créera la base de données et fournira les détails de connexion.

![Tableau de bord Neon montrant que le projet est prêt. Affiche également les détails de connexion.](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwe2x5d81euphg2owgxhd.png)
_Tableau de bord Neon_

Comme vous pouvez le voir, la base de données a été configurée en 3,3 secondes (contre des heures d'installation et de configuration de votre propre infrastructure). Vous pouvez choisir plusieurs façons de vous connecter à la base de données. Pour ce tutoriel, sélectionnez Java comme langage de programmation et obtenez la chaîne de connexion JDBC.

## Comment construire l'application CRUD Spring Boot

Ensuite, configurons notre application CRUD. Nous utiliserons Spring Boot, car il fournit un démarrage et une configuration faciles pour la construction d'applications web.

Nous pouvons utiliser [Spring Initializr](https://start.spring.io/) pour générer un nouveau projet Spring Boot avec les dépendances nécessaires :

* Spring Web – pour construire des applications web
* Spring Data JPA – pour travailler avec des bases de données en utilisant JPA
* Pilote PostGres – pour se connecter à la base de données Postgres

![Formulaire du site web Spring Initializer pour sélectionner les spécifications et les dépendances du projet Spring Boot](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffifv17tc5d3swothe3zf.png)
_Création d'un projet Spring Boot en utilisant Spring Initializer_

Vous pouvez générer, télécharger et importer le projet dans votre IDE préféré.

### Créer une classe d'entité

Créons une classe d'entité pour représenter les données dans l'application. Tout d'abord, créez une classe `User` :

```java
@Entity(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;

    // Constructeurs, Getters et Setters
}
```

Le nom de l'entité `users` est le nom de la table que vous souhaitez utiliser dans votre base de données.

### Créer un dépôt

Ensuite, créez une interface de dépôt pour interagir avec la base de données. Vous allez étendre l'interface `JpaRepository` fournie par Spring Data JPA :

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
```

Vous devez annoter l'interface avec `@Repository` pour la marquer comme un bean Spring. L'interface `JpaRepository` fournit des méthodes pour les opérations CRUD comme `save`, `findAll`, `findById`, `delete`, etc., donc vous n'avez pas besoin d'écrire les requêtes manuellement.

Vous fournirez votre classe d'entité `User` et le type de la clé primaire `Long` comme arguments de type à l'interface `JpaRepository`.

### Créer un contrôleur REST

Enfin, créez un contrôleur REST pour gérer les opérations CRUD. Vous allez injecter le `UserRepository` dans le contrôleur et implémenter les endpoints nécessaires :

```java
@RestController
@RequestMapping("/users")
public class UserController {
    private final UserRepository userRepository;

    public UserController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @GetMapping
    public List<User> getUsers() {
        return userRepository.findAll();
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userRepository.save(user);
    }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return userRepository.save(user);
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userRepository.deleteById(id);
    }
}
```

Voici quelques points à noter :

* Vous utilisez l'annotation `@RestController` pour marquer la classe comme un contrôleur qui gère les requêtes REST.
* L'annotation `@RequestMapping` spécifie l'URL de base pour les endpoints.
* Vous injectez le `UserRepository` dans le contrôleur en utilisant l'injection par constructeur.
* Enfin, vous implémentez vos endpoints d'API pour les opérations CRUD en utilisant les annotations `@GetMapping`, `@PostMapping`, `@PutMapping`, et `@DeleteMapping`.

### Configurer la base de données

Pour connecter votre application Spring Boot à la base de données Neon Postgres, vous devez configurer l'URL de la base de données, le nom d'utilisateur et le mot de passe dans le fichier `application.properties` :

```
spring.datasource.url=jdbc:postgresql://<db-url>/<db-name>?sslmode=require
spring.datasource.username=<username>
spring.datasource.password=<password>
spring.jpa.hibernate.ddl-auto=update
```

Ici, vous avez configuré l'URL de la base de données, le nom d'utilisateur et le mot de passe fournis par Neon lorsque vous avez créé la base de données. La propriété `spring.jpa.hibernate.ddl-auto=update` indique à Spring Boot de créer automatiquement les tables ou colonnes nécessaires en fonction des classes d'entités lorsque l'application démarre.

## Comment déployer sur Azure App Service

Maintenant que votre application Spring Boot est prête, il est temps de la déployer sur Azure App Service.

### Créer une nouvelle application Web

Pour déployer votre application Spring Boot sur Azure App Service, vous allez d'abord créer une nouvelle `Application Web`. Vous pouvez le faire via le portail Azure en suivant ces étapes :

* Connectez-vous au [portail Azure](https://portal.azure.com/).
* Cliquez sur le bouton `Créer une ressource`.
* Recherchez `Application Web` et sélectionnez l'option `Créer`.
* Remplissez les détails nécessaires comme le groupe de ressources, le nom de l'application, la pile d'exécution et la région.
* Cliquez sur le bouton `Vérifier + créer`.

![Formulaire pour créer une application web dans Azure](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flf2kmh12t8eucd1qa1pg.png)
_Création d'une application Web dans Azure_

### Déployer l'application

La création de l'application Web prend quelques minutes. Une fois terminée, vous pouvez déployer votre application Spring Boot sur Azure App Service.

L'une des façons les plus simples de déployer est de packager votre application Spring Boot sous forme de fichier JAR et de la déployer sur Azure App Service en utilisant l'interface de ligne de commande Azure.

Pour ce faire, exécutez les commandes suivantes :

```
mvn package
az webapp deploy --src-path neon-demo-0.0.1-SNAPSHOT.jar --resource-group learn-ba1a439c-71ca-4cab-9bb1-f5b1331bab04 --name neon-app
```

Ici, vous packagez votre application Spring Boot en utilisant Maven et déployez le fichier JAR sur Azure App Service en utilisant l'interface de ligne de commande Azure. Vous avez fourni le chemin vers le fichier JAR, le groupe de ressources et le nom de l'application que vous avez précédemment configurés.

### Accéder à l'application

Une fois le déploiement terminé, vous pouvez accéder à votre application Spring Boot sur Azure App Service en naviguant vers l'URL de l'application Web. Votre application est disponible à l'adresse neon-app.azurewebsites.net

Utilisons _curl_ pour tester les endpoints.

#### Créer un utilisateur

```
curl -X POST -d '{"name":"John Doe","email":"john@gmail.com"}' https://neon-app.azurewebsites.net/users
```

Ici, vous fournissez les données de l'utilisateur au format JSON pour créer un nouvel utilisateur.

#### Obtenir les utilisateurs

Vous pouvez également tester que l'utilisateur a été créé en récupérant tous les utilisateurs :

```
curl -X GET https://neon-app.azurewebsites.net/users
```

## Comment configurer le scaling automatique

Une application de production peut connaître des niveaux de trafic variables, et il est important de scaler l'application dynamiquement en fonction de la charge.

Explorons comment vous pouvez auto-scaler votre application lorsque cela est nécessaire.

### Scaling automatique dans Azure

Azure App Service fournit des [options de scaling automatique](https://learn.microsoft.com/fr-fr/azure/azure-functions/functions-premium-plan?tabs=portal#plan-and-sku-settings) qui vous permettent d'ajuster automatiquement le nombre d'instances selon les besoins.

Vous pouvez configurer les règles de scaling automatique dans le portail Azure en suivant ces étapes :

* Accédez à l'application Web dans le portail Azure.
* Cliquez sur l'option `Scaler (Plan App Service)` dans le menu de gauche.
* Configurez les règles de scaling automatique – vous pouvez choisir des règles prédéfinies comme le trafic ou créer des règles personnalisées basées sur des métriques comme l'utilisation du CPU, l'utilisation de la mémoire ou des métriques personnalisées.
* Enregistrez.

Azure scalera automatiquement l'application en fonction des règles configurées.

### Scaling automatique dans Neon

Puisque votre application est automatiquement scalée en fonction de la charge, vous voudrez vous assurer que la base de données peut gérer le trafic accru.

Neon fournit des [options de scaling automatique](https://neon.tech/docs/introduction/autoscaling) pour scaler la base de données dynamiquement en fonction de la charge. Vous pouvez configurer des règles de scaling automatique dans le tableau de bord Neon pour vous assurer que la base de données peut gérer la charge accrue.

Suivez les étapes ci-dessous pour configurer le scaling automatique dans Neon :

1. Accédez au tableau de bord Neon et sélectionnez la base de données. Ensuite, sélectionnez la branche pour configurer le scaling automatique.

![Tableau de bord du projet Neon avec la section des branches mise en évidence](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl6s84pqhk2avflpjbgrf.png)
_Sélection d'une branche à partir du tableau de bord du projet Neon_

2. Cliquez sur le bouton `Modifier` à côté de la section `Compute`. Configurez les règles de scaling automatique en fonction des métriques comme l'utilisation du CPU, l'utilisation de la mémoire ou des métriques personnalisées.

![Vue des détails de la branche dans Neon avec le bouton de modification dans la section des computes mis en évidence](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffkn11nop1zz9xxbfamsr.png)
_Vue des détails de la branche dans Neon_

3. Configurez la taille minimale et maximale du compute et enregistrez. Neon scalera automatiquement la base de données en fonction des règles configurées lorsque cela sera nécessaire.

![Formulaire pour activer le scaling automatique et sélectionner la taille minimale et maximale du compute](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdmuow8zvndz0dibv2kxt.png)
_Configuration du scaling automatique pour le compute_

Assurer que l'application et la base de données peuvent scaler dynamiquement en fonction de la charge vous aidera à gérer efficacement les niveaux de trafic variables.

## Comment configurer les branches de base de données dans Neon

Dans un flux de travail de développement typique, plusieurs bases de données peuvent être utilisées pour différents usages comme le développement, les tests et la production.

Neon Postgres fournit le [branchement de base de données](https://neon.tech/docs/introduction/autoscaling) pour créer plusieurs branches à différentes fins. Chaque branche est une instance de la base de données que vous pouvez utiliser indépendamment.

Cette fonctionnalité de type Git aide à configurer une copie de la base de données pour différents environnements comme le développement, la pré-production et la production. Elle aide également à préserver les données pour différentes versions de l'application.

Explorons comment vous pouvez créer et gérer des branches dans Neon Postgres :

* Accédez au tableau de bord Neon et sélectionnez la base de données.
* Dans la section `Branches`, cliquez sur le bouton `Voir tout`.
* Vous pouvez créer une nouvelle branche à partir d'une branche existante en cliquant sur le bouton `Créer une branche`. Vous devrez fournir le nom de la branche et les données à copier depuis la branche parente.

![Vue des branches avec l'option Créer une branche visible](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9ncdgdrj32etd3gbqurf.png)
_Option Créer une branche_

* Vous pouvez soit copier toutes les données, soit copier jusqu'à un point dans le temps ou un enregistrement spécifique. Cela est utile pour plusieurs usages comme la restauration de données, la création d'un nouvel environnement ou le test de nouvelles fonctionnalités.

![Création d'une nouvelle branche à partir d'une branche existante](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fw7gchucru5qw294icqw3.png)
_Création d'une nouvelle branche_

* Neon créera une nouvelle branche de la base de données qui peut être utilisée indépendamment. Vous pouvez trouver l'URL, le nom d'utilisateur et le mot de passe pour la nouvelle branche dans le tableau de bord. Et cela se fait en temps réel sans aucun temps d'arrêt ni délai.

![Détails de connexion spécifiques à la branche](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fji79akuf193gtv94yaag.png)
_Détails de connexion spécifiques à la branche_

Maintenant, vous pouvez utiliser votre branche `dev` pour le développement et les tests locaux, et la branche `main` pour la production. Cela aide à garder les données séparées et garantit que les changements dans une branche n'affectent pas les autres branches.

## Résumé

Dans cet article, nous avons construit une application CRUD en utilisant Spring Boot, Neon Postgres et Azure App Service.

Nous avons exploré comment configurer la base de données Neon Postgres, construire une application CRUD basique en utilisant Spring Boot, déployer l'application sur Azure App Service et configurer le scaling automatique pour l'application et la base de données.

Nous avons également appris comment la fonctionnalité de branchement de base de données dans Neon Postgres vous aide à créer des branches de la base de données pour différents environnements et usages.