---
title: Comment implémenter l'autorisation fine en Java et Spring Boot
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-10-24T17:37:31.841Z'
originalURL: https://freecodecamp.org/news/fine-grained-authorization-in-java-and-springboot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729783227124/9725e8cf-553d-42c3-a823-5215e8d4d0e9.png
tags:
- name: Java
  slug: java
- name: Springboot
  slug: springboot
- name: authorization
  slug: authorization
- name: Web Development
  slug: web-development
- name: software development
  slug: software-development
- name: Docker
  slug: docker
- name: Developer
  slug: developer
- name: Developer Tools
  slug: developer-tools
seo_title: Comment implémenter l'autorisation fine en Java et Spring Boot
seo_desc: 'Securing your application goes beyond simply granting or denying access
  at the surface level. As a developer, you need to implement fine-grained authorization
  (FGA) to manage permissions at a more detailed, granular level.

  FGA allows you to set up de...'
---

Sécuriser votre application va au-delà du simple fait d'accorder ou de refuser l'accès au niveau de surface. En tant que développeur, vous devez implémenter une `autorisation fine` (FGA) pour gérer les permissions à un niveau plus détaillé et granulaire.

La FGA vous permet de configurer des contrôles d'accès détaillés qui spécifient qui peut faire quoi et sous quelles conditions.

Dans ce tutoriel, vous apprendrez à implémenter une `autorisation fine` en Java et Spring Boot en utilisant [Permit.io](https://permit.io/).

Voici le [code source](https://github.com/tyaga001/java-spring-fine-grained-auth) (n'oubliez pas de lui donner une étoile ⭐).

J'espère que vous avez apprécié mon précédent [blog](https://www.freecodecamp.org/news/how-i-built-a-custom-video-conferencing-app-with-stream-and-nextjs/) sur la création d'une application de visioconférence personnalisée avec Stream et Next.js. Ces blogs reflètent mon parcours dans la création de DevTools Academy, une plateforme conçue pour aider les développeurs à découvrir des outils de développement incroyables.

Ce tutoriel est un autre effort pour vous présenter un outil de développement super utile que j'ai récemment exploré.

## **Table des matières :**

* [Qu'est-ce que Permit](#heading-quest-ce-que-permit) ?
    
* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que l'autorisation fine](#heading-quest-ce-que-lautorisation-fine) ?
    
    * [Contrôle d'accès basé sur les rôles (RBAC)](#heading-controle-dacces-base-sur-les-roles-rbac)
        
    * [Contrôle d'accès basé sur les attributs (ABAC)](#heading-controle-dacces-base-sur-les-attributs-abac)
        
    * [Contrôle d'accès basé sur les relations (ReBAC)](#heading-controle-dacces-base-sur-les-relations-rebac)
        
* [Comment implémenter l'autorisation fine](#heading-comment-implementer-lautorisation-fine)
    
    * [Implémentation du contrôle d'accès basé sur les rôles](#heading-implementation-du-controle-dacces-base-sur-les-roles)
        
    * [Implémentation du contrôle d'accès basé sur les attributs](#heading-implementation-du-controle-dacces-base-sur-les-attributs)
        
    * [Implémentation du contrôle d'accès basé sur les relations](#heading-implementation-du-controle-dacces-base-sur-les-relations)
        
* [Comment implémenter la FGA en Java et Spring Boot](#heading-comment-implementer-la-fga-en-java-et-springboot)
    
    * [Étape 1 : Configuration de l'application e-commerce](#heading-etape-1-configuration-de-lapplication-e-commerce)
        
    * [Étape 2 : Obtenir votre clé API d'environnement](#heading-etape-2-obtenir-votre-cle-api-denvironnement)
        
    * [Étape 3 : Déployer le Point de Décision de Politique (PDP)](#heading-etape-3-deployer-le-point-de-decision-de-politique-pdp)
        
    * [Étape 4 : Exécution de l'application](#heading-etape-4-execution-de-lapplication)
        
* [Prochaines étapes](#heading-prochaines-etapes)
    
    * [Avant de terminer...](#heading-avant-de-terminer)
        

## **Qu'est-ce que** Permit ?

> [Permit.io](https://www.permit.io) est une solution d'autorisation au niveau de l'application, complète et prête à l'emploi, qui vous permet d'implémenter une couche d'`autorisation` `sécurisée` et `flexible` en quelques minutes, afin que vous puissiez vous concentrer sur ce qui compte le plus.

[![qu'est-ce que permit - capture d'écran de la page d'accueil](https://cdn.hashnode.com/res/hashnode/image/upload/v1729499767197/6e2b4312-8986-493e-9453-3b67e6aad155.png align="center")](https://www.permit.io)

## **Prérequis**

Pour comprendre pleinement ce tutoriel, vous devez avoir une compréhension de base de `Java` et de `Spring Boot`. Vous aurez également besoin des éléments suivants :

* [**Permit.io**](http://Permit.io) : Un outil de développement qui simplifie l'implémentation de la FGA.
    
* **Spring Boot Starter Web** : Fournit des composants essentiels pour construire des applications web, y compris des API RESTful.
    
* **Gradle** : Un outil de construction pour gérer les dépendances.
    
* **JDK 11 ou ultérieur** : La version du kit de développement Java requise pour compiler et exécuter votre application Spring Boot.
    
* **Postman ou cURL** : Outils pour tester vos points de terminaison `API`.
    

## **Qu'est-ce que l'autorisation fine ?**

L'[autorisation fine](https://www.permit.io/blog/what-is-fine-grained-authorization-fga) offre un contrôle d'accès aux ressources en déterminant qui peut y accéder, dans quelle mesure et sous quelles conditions.

Contrairement à l'autorisation grossière (qui gère l'accès en fonction de catégories comme les `rôles utilisateur` tels que "`admin`" ou "`user`"), l'autorisation fine vous donne la flexibilité de définir l'accès à un niveau granulaire, pour des ressources ou des actions spécifiques et même des attributs.

Dans l'`autorisation fine`, il existe 3 types de modèles de politique pour gérer l'autorisation : **Contrôle d'accès basé sur les rôles (RBAC)**, **Contrôle d'accès basé sur les attributs (ABAC)**, et **Contrôle d'accès basé sur les relations (ReBAC)**.

Examinons chacun de ces approches et voyons comment vous pouvez les implémenter dans votre application.

### **Contrôle d'accès basé sur les rôles (RBAC)**

Le [RBAC](https://www.permit.io/blog/what-is-rebac) est une approche de sécurité qui contrôle l'accès aux ressources en fonction des rôles des utilisateurs au sein d'une organisation. Ce modèle rationalise les permissions en organisant les utilisateurs en rôles et en gérant le contrôle d'accès selon ces rôles définis.

**Concepts clés du RBAC :**

**Utilisateurs :** Personnes qui utilisent le système, telles que les employés ou les clients.

**Rôles :** Ensemble de permissions ou de privilèges d'accès attribués à un groupe d'utilisateurs en fonction de leurs responsabilités ou tâches, tels que admin, manager ou client.

**Permissions :** Les droits accordés aux utilisateurs pour interagir avec les ressources, tels que lire, écrire ou supprimer.

### **Contrôle d'accès basé sur les attributs (ABAC)**

L'[ABAC](https://www.permit.io/blog/what-is-abac) est un modèle de contrôle d'accès polyvalent et adaptatif qui décide qui peut ou ne peut pas accéder aux ressources en fonction des attributs, comme les détails de l'utilisateur. Le modèle ABAC vous permet de définir une autorisation fine basée sur les attributs de l'utilisateur.

**Concepts clés de l'ABAC :**

**Attributs :** Caractéristiques ou propriétés utilisées pour prendre des décisions de contrôle d'accès. Les attributs sont généralement catégorisés en :

* **Attributs de l'utilisateur :** Informations sur l'utilisateur (par exemple, rôle, département, titre de poste, âge, etc.).
    
* **Attributs de la ressource :** Caractéristiques de la ressource (par exemple, type de fichier, niveau de classification des données, date de création, propriétaire).
    
* **Attributs d'action :** L'action que l'utilisateur tente d'effectuer (par exemple, lire, écrire, supprimer, approuver).
    
* **Attributs environnementaux :** Informations contextuelles sur la demande d'accès (par exemple, heure de la journée, lieu, type de périphérique, adresse IP).
    

### **Contrôle d'accès basé sur les relations (ReBAC)**

Le ReBAC est un système de contrôle d'accès qui accorde des permissions pour accéder aux ressources en fonction de la relation entre les entités au sein d'un système. Cette approche met l'accent sur la définition et la gestion du contrôle d'accès en cartographiant comment les utilisateurs se rapportent aux ressources et à d'autres entités telles que les organisations ou les groupes.

**Concepts clés du ReBAC :**

**Entités :** Utilisateurs, ressources (telles que fichiers et documents), et autres entités, telles que groupes ou unités organisationnelles.

**Relations :** Les connexions qui spécifient la relation entre deux entités. Un utilisateur peut être le "propriétaire" d'un document ou un "membre" d'une équipe, par exemple.

**Politiques :** Règles qui utilisent les relations pour déterminer les droits d'accès. Un utilisateur peut accéder à une ressource ou exécuter une action sur celle-ci s'il a une relation particulière avec elle.

## **Comment implémenter l'autorisation fine**

Maintenant que vous avez une compréhension de base du `RBAC`, de l'`ABAC` et du `ReBAC`, voyons comment nous pouvons implémenter ces modèles dans une application e-commerce.

### **Implémentation du contrôle d'accès basé sur les rôles**

**Étape 1 :** Accédez à [Permit.io](http://Permit.io), puis créez un compte et votre espace de travail.

![Permit.io - créer votre espace de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1729494514537/a49035e8-1eb2-495f-acee-6ac212d0076e.png align="center")

Par défaut, vous devriez voir un projet qui inclut deux environnements : `Développement` et `Production`.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text"><strong><em>Remarque :</em></strong><em> Vous devez définir et tester vos politiques dans l'environnement de développement avant de les déployer en production.</em></div>
</div>

![Permit.io - tableau de bord du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1729494835226/8d0e6841-09e7-44e2-89fb-1ec3bacb316d.png align="center")

**Étape 2 :** Créez une ressource nommée **Produits**. Pour créer la ressource, ouvrez l'onglet **Politique** dans la barre latérale de gauche, puis ouvrez l'onglet **Ressources** en haut. Après cela, cliquez sur le bouton **Créer une ressource** et créez une ressource appelée **Produits** avec les actions `lire`, `créer`, `mettre à jour` et `supprimer`.

![Permit.io - comment ajouter une nouvelle ressource](https://cdn.hashnode.com/res/hashnode/image/upload/v1729495042599/91660d3d-eafe-4874-aeb2-50bf88c5a291.png align="center")

**Étape 3 :** Créez une autre ressource appelée **Avis** avec les actions `lire`, `créer`, `mettre à jour` et `supprimer`.

**Étape 4 :** Ouvrez l'onglet **Éditeur de politique**. Vous verrez que 3 rôles nommés `admin`, `éditeur` et `lecteur` ont été créés.

* Le rôle admin a la permission de `créer`, `supprimer`, `lire` ou `mettre à jour` un produit ou un avis.
    
* Le rôle `éditeur` a la permission de `créer`, `lire` ou `mettre à jour` un `produit` ou un `avis` mais pas de `supprimer` aucun.
    
* Le rôle `lecteur` a la permission de `créer` et `lire` un produit ou un `avis` mais pas de `supprimer` ou `mettre à jour` aucun.
    

![Permit.io - Éditeur de politique](https://cdn.hashnode.com/res/hashnode/image/upload/v1729495227714/38553c90-5cc0-4fa0-a116-2f5051b5ebb8.png align="center")

### **Implémentation du contrôle d'accès basé sur les attributs**

**Étape 1 :** Ouvrez l'onglet **Ressources**, puis cliquez sur le bouton **Ajouter des attributs**.

* Ajoutez un attribut appelé **fournisseur**
    
* Ajoutez un attribut appelé **client**
    

![Permit.io - modifier la ressource](https://cdn.hashnode.com/res/hashnode/image/upload/v1729495417262/94a09532-83b3-496c-8fef-6ee7c836a211.png align="center")

**Étape 2 :** Ouvrez l'onglet Règles ABAC, puis créez un nouvel ensemble de ressources ABAC appelé **Produits propres** qui dépend de la ressource Produits. Après cela, ajoutez une condition qui donne des permissions uniquement à l'utilisateur qui a créé un produit en fonction de l'attribut fournisseur.

![Permit.io - créer votre ensemble de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1729495597939/d528f47f-710a-4bd6-b13a-1cf3a3c49031.png align="center")

**Étape 3 :** Créez un autre ensemble de ressources ABAC appelé **Avis propres** qui dépend de la ressource Avis.

### **Implémentation du contrôle d'accès basé sur les relations**

**Étape 1 :** Ouvrez l'onglet Ressources et modifiez la ressource Produits. Ajoutez le rôle `fournisseur` dans la section des options `ReBAC`. Ensuite, définissez les produits comme parent des avis dans la section des relations.

**Étape 2 :** Modifiez la ressource Avis en ajoutant le rôle client dans la section des options `ReBAC`, comme montré ci-dessous :

![Permit.io - modifier la ressource ABAC](https://cdn.hashnode.com/res/hashnode/image/upload/v1729497355241/4f1a6235-7181-468a-82ce-c727df517604.png align="center")

**Étape 3 :** Allez dans l'onglet `Politique` `Éditeur` et ajoutez :

* rôle `fournisseur` permission de mettre à jour et supprimer ses propres produits.
    
* rôle `client` permission de mettre à jour et supprimer ses propres avis sur les produits.
    

![Permit.io - Éditeur de politique](https://cdn.hashnode.com/res/hashnode/image/upload/v1729497438508/935f79b7-3789-4047-b7b5-73e82654b617.png align="center")

## **Comment implémenter la FGA en Java et Spring Boot**

Maintenant que nous avons défini les politiques `RBAC`, `ABAC` et `ReBAC` dans l'interface web de Permit.io, apprenons à les appliquer dans une application de système de gestion e-commerce en utilisant l'API de Permit.io.

Il y a beaucoup de code à venir, alors assurez-vous de lire les commentaires détaillés que j'ai laissés dans chaque bloc de code. Ceux-ci vous aideront à comprendre plus pleinement ce qui se passe dans ce code.

### **Étape 1 : Configuration de l'application e-commerce**

Pour configurer l'application e-commerce et cloner le code source git.

```powershell
git clone https://github.com/tyaga001/java-spring-fine-grained-auth.git
```

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Ouvrez ensuite le code dans votre IDE Java. J'ai utilisé <a target="_blank" rel="noopener noreferrer nofollow" href="https://www.jetbrains.com/idea/" style="pointer-events: none">JetBrains</a> pour tout mon travail.</div>
</div>

#### **Installation du SDK Permit**

Pour installer le SDK Permit, vous ajoutez le SDK dans le bloc des dépendances dans le fichier `build.gradle`.

````java
## Dépendances

Pour configurer les dépendances nécessaires pour votre projet Spring Boot, incluez ce qui suit dans votre fichier `build.gradle` :

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springdoc:springdoc-openapi-starter-webmvc-ui:2.3.0'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'

    // Ajoutez cette ligne pour installer le SDK Java de Permit.io dans votre projet
    implementation 'io.permit:permit-sdk-java:2.0.0'
}
````

#### **Initialisation du SDK Permit**

Vous pouvez initialiser le client SDK `Permit` en utilisant le code ci-dessous :

```java
package com.boostmytool.store.config;

import io.permit.sdk.Permit;
import io.permit.sdk.PermitConfig;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration  // Marque cette classe comme une classe de configuration pour Spring IoC
public class PermitClientConfig {

    @Value("${permit.api-key}")  // Injecte la clé API Permit depuis les propriétés de l'application
    private String apiKey;

    @Value("${permit.pdp-url}")  // Injecte l'URL PDP (Policy Decision Point) Permit depuis les propriétés de l'application
    private String pdpUrl;

    /**
     * Crée une instance de client Permit avec une configuration personnalisée
     * @return Instance de client Permit
     */
    @Bean
    public Permit permit() {
        return new Permit(
                new PermitConfig.Builder(apiKey)  // Initialise PermitConfig avec la clé API
                        .withPdpAddress(pdpUrl)   // Définit l'adresse PDP
                        .withDebugMode(true)      // Active le mode débogage pour un journal détaillé
                        .build()                  // Construit l'objet PermitConfig
        );
    }
}
```

#### **Synchronisation des utilisateurs avec le SDK**

Pour commencer à appliquer les permissions, vous devez d'abord synchroniser un utilisateur avec Permit, puis lui attribuer un rôle.

Dans le code ci-dessous, la classe **UserService** fournit des méthodes pour la connexion de l'utilisateur, l'inscription, l'attribution de rôle et l'autorisation, avec une gestion des exceptions pour les erreurs possibles lors de l'interaction avec l'API Permit.

```java
package com.boostmytool.store.service;

import com.boostmytool.store.exception.ForbiddenAccessException;
import com.boostmytool.store.exception.UnauthorizedException;
import io.permit.sdk.Permit;
import io.permit.sdk.api.PermitApiError;
import io.permit.sdk.api.PermitContextError;
import io.permit.sdk.enforcement.Resource;
import io.permit.sdk.enforcement.User;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service  // Marque cette classe comme un service Spring, la rendant éligible pour le balayage des composants
public class UserService {
    private final Permit permit;

    // Injection de dépendance pour le SDK Permit
    public UserService(Permit permit) {
        this.permit = permit;
    }

    /**
     * Simule la connexion de l'utilisateur en créant et en retournant un objet Utilisateur Permit.
     * 
     * @param key Clé unique de l'utilisateur
     * @return Objet Utilisateur
     */
    public Object login(String key) {
        return new User.Builder(key).build();
    }

    /**
     * Gère l'inscription de l'utilisateur en créant et en synchronisant un nouvel Utilisateur Permit.
     * 
     * @param key Clé unique de l'utilisateur
     * @return Objet Utilisateur créé et synchronisé
     */
    public User signup(String key) {
        var user = new User.Builder(key).build();
        try {
            permit.api.users.sync(user);  // Synchronise le nouvel utilisateur avec le service Permit
        } catch (PermitContextError | PermitApiError | IOException e) {
            throw new RuntimeException("Échec de la création de l'utilisateur", e);  // Gère les exceptions lors de la création de l'utilisateur
        }
        return user;
    }

    /**
     * Attribue un rôle à l'utilisateur dans l'environnement "default".
     * 
     * @param user Objet Utilisateur auquel attribuer le rôle
     * @param role Rôle à attribuer
     */
    public void assignRole(User user, String role) {
        try {
            permit.api.users.assignRole(user.getKey(), role, "default");  // Attribue le rôle dans l'environnement "default"
        } catch (PermitApiError | PermitContextError | IOException e) {
            throw new RuntimeException("Échec de l'attribution du rôle à l'utilisateur", e);  // Gère les exceptions lors de l'attribution du rôle
        }
    }

    /**
     * Vérifie si l'utilisateur est autorisé à effectuer une action spécifique sur une ressource.
     * 
     * @param user Objet Utilisateur demandant l'autorisation
     * @param action Action à autoriser
     * @param resource Ressource sur laquelle l'action sera effectuée
     * @throws UnauthorizedException si l'utilisateur n'est pas connecté
     * @throws ForbiddenAccessException si l'accès est refusé à l'utilisateur
     */
    public void authorize(User user, String action, Resource resource) {
        if (user == null) {
            throw new UnauthorizedException("Non connecté");  // Lance une exception si l'utilisateur n'est pas connecté
        }
        try {
            var permitted = permit.check(user, action, resource);  // Effectue la vérification d'autorisation
            if (!permitted) {
                throw new ForbiddenAccessException("Accès refusé");  // Lance une exception si l'accès est refusé
            }
        } catch (PermitApiError | IOException e) {
            throw new RuntimeException("Échec de l'autorisation de l'utilisateur", e);  // Gère les exceptions lors de l'autorisation
        }
    }
}
```

Ensuite, dans le code ci-dessous, la classe **UserController** expose des points de terminaison d'API REST pour l'inscription des utilisateurs et l'attribution de rôles. Elle interagit avec la classe UserService pour gérer la logique métier liée aux utilisateurs et fournit des réponses HTTP appropriées.

```java
package com.boostmytool.store.controllers;

import com.boostmytool.store.exception.UnauthorizedException;
import com.boostmytool.store.service.UserService;
import io.permit.sdk.enforcement.User;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController  // Indique que cette classe gère les requêtes HTTP et retourne des réponses JSON
@RequestMapping("/api/users")  // Chemin de base de l'URL pour toutes les opérations liées aux utilisateurs
public class UserController {
    private final UserService userService;

    // Injection de dépendance de UserService, contenant la logique métier pour les opérations utilisateur
    public UserController(UserService userService) {
        this.userService = userService;
    }

    /**
     * Gère les requêtes d'inscription des utilisateurs.
     * Point de terminaison : POST /api/users/signup
     * 
     * @param key Clé unique pour le nouvel utilisateur
     * @return Objet Utilisateur créé
     */
    @PostMapping("/signup")
    public User signup(@RequestBody String key) {
        return userService.signup(key);  // Appelle la méthode signup dans UserService pour créer un nouvel utilisateur
    }

    /**
     * Gère l'attribution d'un rôle à l'utilisateur connecté.
     * Point de terminaison : POST /api/users/assign-role
     * 
     * @param request Requête HTTP, utilisée pour récupérer l'utilisateur actuel
     * @param role Rôle à attribuer à l'utilisateur actuel
     */
    @PostMapping("/assign-role")
    public void assignRole(HttpServletRequest request, @RequestBody String role) {
        // Récupère l'utilisateur actuel à partir des attributs de la requête
        User currentUser = (User) request.getAttribute("user");
        
        // Lance une exception si l'utilisateur n'est pas connecté
        if (currentUser == null) {
            throw new UnauthorizedException("Non connecté");
        }

        // Attribue le rôle spécifié à l'utilisateur actuel
        userService.assignRole(currentUser, role);
    }
}
```

#### **Création de points d'application des politiques RBAC, ABAC et ReBAC**

Dans le code ci-dessous, la classe **ProductService** gère les opérations CRUD pour les produits et les avis, en gérant les permissions et les rôles via l'API Permit.

Chaque opération inclut des vérifications d'`autorisation` de l'utilisateur, avec une gestion appropriée des exceptions pour les erreurs de l'API Permit et les scénarios de ressource introuvable.

```java
package com.boostmytool.store.service;

import com.boostmytool.store.exception.ResourceNotFoundException;
import com.boostmytool.store.model.Product;
import com.boostmytool.store.model.Review;
import io.permit.sdk.Permit;
import io.permit.sdk.api.PermitApiError;
import io.permit.sdk.api.PermitContextError;
import io.permit.sdk.enforcement.Resource;
import io.permit.sdk.enforcement.User;
import io.permit.sdk.openapi.models.RelationshipTupleCreate;
import io.permit.sdk.openapi.models.ResourceInstanceCreate;
import io.permit.sdk.openapi.models.RoleAssignmentCreate;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

@Service  // Marque cette classe comme un service Spring
public class ProductService {

    private final List<Product> products = new ArrayList<>();  // Liste en mémoire pour stocker les produits
    private final AtomicInteger productIdCounter = new AtomicInteger();  // Compteur pour générer des identifiants de produit uniques
    private final AtomicInteger reviewIdCounter = new AtomicInteger();   // Compteur pour générer des identifiants d'avis uniques

    // Constructeurs pour les instances de ressources Permit (produit et avis)
    private final Resource.Builder productResourceBuilder = new Resource.Builder("product");
    private final Resource.Builder reviewResourceBuilder = new Resource.Builder("review");

    private final UserService userService;  // Service pour gérer les opérations liées aux utilisateurs
    private final Permit permit;  // Instance du SDK Permit pour gérer l'autorisation et la gestion des ressources

    // Constructeur pour l'injection de dépendances
    public ProductService(UserService userService, Permit permit) {
        this.userService = userService;
        this.permit = permit;
    }

    // Méthode pour autoriser un utilisateur à effectuer une action sur une ressource
    private void authorize(User user, String action, Resource resource) {
        userService.authorize(user, action, resource);
    }

    // Autorise un utilisateur à effectuer une action sur un produit spécifique
    private void authorize(User user, String action, Product product) {
        var attributes = new HashMap<String, Object>();
        attributes.put("vendor", product.getVendor());  // Ajoute l'attribut fournisseur au produit
        userService.authorize(user, action, productResourceBuilder.withKey(product.getId().toString()).withAttributes(attributes).build());
    }

    // Autorise un utilisateur à effectuer une action sur un avis spécifique
    private void authorize(User user, String action, Review review) {
        var attributes = new HashMap<String, Object>();
        attributes.put("customer", review.getCustomer());  // Ajoute l'attribut client à l'avis
        userService.authorize(user, action, reviewResourceBuilder.withKey(review.getId().toString()).withAttributes(attributes).build());
    }

    // Récupère un produit par son identifiant, lance une exception s'il n'est pas trouvé
    private Product getProductById(int id) {
        return products.stream().filter(product -> product.getId().equals(id))
                .findFirst().orElseThrow(() -> new ResourceNotFoundException("Produit avec l'identifiant " + id + " non trouvé"));
    }

    // Récupère tous les produits, vérifie si l'utilisateur est autorisé à "lire" les produits
    public List<Product> getAllProducts(User user) {
        authorize(user, "read", productResourceBuilder.build());  // L'utilisateur doit avoir la permission "read"
        return new ArrayList<>(products);  // Retourne une copie de la liste des produits
    }

    // Récupère un produit par son identifiant, vérifie si l'utilisateur est autorisé à "lire" le produit
    public Product getProduct(User user, int id) {
        authorize(user, "read", productResourceBuilder.build());
        return getProductById(id);
    }

    // Ajoute un nouveau produit, autorise l'utilisateur et crée des instances de ressources et des attributions de rôles dans Permit
    public Product addProduct(User user, String content) {
        authorize(user, "create", productResourceBuilder.build());  // Vérifie si l'utilisateur peut créer un produit
        Product product = new Product(productIdCounter.incrementAndGet(), user.getKey(), content);  // Crée un nouveau produit

        try {
            // Crée une instance de ressource dans Permit et attribue le rôle "vendor" à l'utilisateur pour ce produit
            permit.api.resourceInstances.create(new ResourceInstanceCreate(product.getId().toString(), "product").withTenant("default"));
            permit.api.roleAssignments.assign(new RoleAssignmentCreate("vendor", user.getKey()).withResourceInstance("product:" + product.getId()).withTenant("default"));
        } catch (IOException | PermitApiError | PermitContextError e) {
            throw new RuntimeException("Échec de la création de l'instance de ressource ou de l'attribution de rôle : " + e.getMessage());
        }

        products.add(product);  // Ajoute le produit à la liste en mémoire
        return product;
    }

    // Met à jour le contenu d'un produit, vérifie si l'utilisateur est autorisé à "mettre à jour" le produit
    public Product updateProduct(User user, int id, String content) {
        Product product = getProductById(id);  // Récupère le produit par son identifiant
        authorize(user, "update", product);  // Vérifie si l'utilisateur peut mettre à jour le produit
        product.setContent(content);  // Met à jour le contenu du produit
        return product;
    }

    // Supprime un produit, vérifie si l'utilisateur est autorisé à "supprimer" le produit
    public void deleteProduct(User user, int id) {
        boolean isDeleted = products.removeIf(product -> {
            if (product.getId().equals(id)) {
                authorize(user, "delete", product);  // Vérifie si l'utilisateur peut supprimer le produit
                return true;
            } else {
                return false;
            }
        });
        
        if (!isDeleted) {
            throw new ResourceNotFoundException("Produit avec l'identifiant " + id + " non trouvé");
        }

        try {
            permit.api.resourceInstances.delete("product:" + id);  // Supprime l'instance de ressource produit de Permit
        } catch (IOException | PermitApiError | PermitContextError e) {
            throw new RuntimeException(e);
        }
    }

    // Ajoute un avis à un produit, crée une instance de ressource et une relation dans Permit
    public Review addReview(User user, int productId, String content) {
        authorize(user, "create", reviewResourceBuilder.build());  // Vérifie si l'utilisateur peut créer un avis
        Product product = getProductById(productId);  // Récupère le produit par son identifiant
        Review review = new Review(reviewIdCounter.incrementAndGet(), user.getKey(), content);  // Crée un nouvel avis

        try {
            // Crée une instance de ressource pour l'avis et définit la relation avec le produit
            permit.api.resourceInstances.create(new ResourceInstanceCreate(review.getId().toString(), "review").withTenant("default"));
            permit.api.relationshipTuples.create(new RelationshipTupleCreate("product:" + productId, "parent", "review:" + review.getId()));
        } catch (IOException | PermitApiError | PermitContextError e) {
            throw new RuntimeException(e);
        }

        product.addReview(review);  // Ajoute l'avis au produit
        return review;
    }

    // Met à jour le contenu d'un avis, vérifie si l'utilisateur est autorisé à "mettre à jour" l'avis
    public Review updateReview(User user, int productId, int reviewId, String content) {
        Product product = getProductById(productId);  // Récupère le produit par son identifiant
        Review review = product.getReviews().stream().filter(c -> c.getId().equals(reviewId))
                .findFirst().orElseThrow(() -> new ResourceNotFoundException("Avis avec l'identifiant " + reviewId + " non trouvé"));
        
        authorize(user, "update", review);  // Vérifie si l'utilisateur peut mettre à jour l'avis
        review.setContent(content);  // Met à jour le contenu de l'avis
        return review;
    }

    // Supprime un avis, vérifie si l'utilisateur est autorisé à "supprimer" l'avis
    public void deleteReview(User user, int productId, int reviewId) {
        Product product = getProductById(productId);  // Récupère le produit par son identifiant
        boolean isDeleted = product.getReviews().removeIf(review -> {
            if (review.getId().equals(reviewId)) {
                authorize(user, "delete", review);  // Vérifie si l'utilisateur peut supprimer l'avis
                return true;
            } else {
                return false;
            }
        });

        if (!isDeleted) {
            throw new ResourceNotFoundException("Avis avec l'identifiant " + reviewId + " non trouvé");
        }

        try {
            permit.api.resourceInstances.delete("review:" + reviewId);  // Supprime l'instance de ressource avis de Permit
        } catch (IOException | PermitApiError | PermitContextError e) {
            throw new RuntimeException(e);
        }
    }
}
```

Ensuite, dans le code ci-dessous, la classe **ProductController** gère les requêtes HTTP liées aux produits et à leurs avis. Elle expose des points de terminaison pour gérer les produits (comme la `création`, la `mise à jour`, la `suppression` et la `récupération`) et pour gérer les avis sur les produits.

```java
package com.boostmytool.store.controllers;

import com.boostmytool.store.model.Product;
import com.boostmytool.store.model.Review;
import com.boostmytool.store.service.ProductService;
import io.permit.sdk.enforcement.User;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController  // Indique que cette classe est un contrôleur REST Spring
@RequestMapping("/api/products")  // URL de base pour tous les points de terminaison de ce contrôleur
public class ProductController {

    private final ProductService productService;  // Instance de ProductService pour gérer les opérations liées aux produits

    @Autowired  // Injection automatique du bean ProductService
    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    // Requête GET pour récupérer tous les produits
    @GetMapping
    public List<Product> getAllProducts(HttpServletRequest request) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.getAllProducts(currentUser);  // Appelle ProductService pour obtenir tous les produits pour l'utilisateur
    }

    // Requête GET pour récupérer un produit par son identifiant
    @GetMapping("/{id}")
    public Product getProductById(HttpServletRequest request, @PathVariable("id") int id) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.getProduct(currentUser, id);  // Appelle ProductService pour obtenir le produit par identifiant pour l'utilisateur
    }

    // Requête POST pour ajouter un nouveau produit
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)  // Définit le statut de la réponse à 201 (Créé)
    public Product addProduct(HttpServletRequest request, @RequestBody String content) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.addProduct(currentUser, content);  // Appelle ProductService pour ajouter un nouveau produit
    }

    // Requête PUT pour mettre à jour un produit existant par son identifiant
    @PutMapping("/{id}")
    public Product updateProduct(HttpServletRequest request, @PathVariable("id") int id, @RequestBody String content) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.updateProduct(currentUser, id, content);  // Appelle ProductService pour mettre à jour le produit par identifiant
    }

    // Requête DELETE pour supprimer un produit par son identifiant
    @DeleteMapping("/{id}")
    public String deleteProduct(HttpServletRequest request, @PathVariable("id") int id) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        productService.deleteProduct(currentUser, id);  // Appelle ProductService pour supprimer le produit par identifiant
        return "Produit supprimé avec l'identifiant " + id;  // Retourne un message de succès après la suppression
    }

    // Requête POST pour ajouter un nouvel avis à un produit par identifiant de produit
    @PostMapping("/{id}/review")
    public Review addReview(HttpServletRequest request, @PathVariable("id") int id, @RequestBody String content) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.addReview(currentUser, id, content);  // Appelle ProductService pour ajouter un avis au produit
    }

    // Requête PUT pour mettre à jour un avis existant par identifiant de produit et d'avis
    @PutMapping("/{id}/review/{reviewId}")
    public Review updateReview(HttpServletRequest request, @PathVariable("id") int id, @PathVariable("reviewId") int reviewId, @RequestBody String content) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        return productService.updateReview(currentUser, id, reviewId, content);  // Appelle ProductService pour mettre à jour l'avis
    }

    // Requête DELETE pour supprimer un avis par identifiant de produit et d'avis
    @DeleteMapping("/{id}/review/{reviewId}")
    public String deleteReview(HttpServletRequest request, @PathVariable("id") int id, @PathVariable("reviewId") int reviewId) {
        User currentUser = (User) request.getAttribute("user");  // Récupère l'utilisateur authentifié de la requête
        productService.deleteReview(currentUser, id, reviewId);  // Appelle ProductService pour supprimer l'avis
        return "Avis supprimé avec l'identifiant " + reviewId + " du produit " + id;  // Retourne un message de succès après la suppression
    }
}
```

### **Étape 2 : Obtenir votre clé API d'environnement**

Dans le tableau de bord de l'interface utilisateur, copiez la clé `API` de l'environnement actif.

![Permit.io - copier la clé d'environnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1729498343969/2bbbd4a0-512f-4b46-a82a-ca41ecb67a4c.png align="center")

Ensuite, ajoutez la clé `API` de l'environnement et l'`URL PDP` dans le fichier `application.yaml`.

```plaintext
permit:
  pdpUrl: 'http://localhost:7766'
  apiKey: "Votre clé API d'environnement Permit"
```

### **Étape 3 : Déployer le Point de Décision de Politique (PDP)**

Le Point de Décision de Politique (PDP) est déployé dans votre VPC et est responsable de l'évaluation de vos requêtes d'autorisation. Le PDP garantira une latence nulle, de grandes performances, une haute disponibilité et une sécurité améliorée.

Utilisez la commande ci-dessous pour tirer le conteneur PDP de [Permit.io](http://Permit.io) depuis le `Docker` Hub.

```dockerfile
docker pull permitio/pdp-v2:latest
```

Ensuite, exécutez le conteneur.

```dockerfile
docker run -it -p 7766:7000 --env PDP_DEBUG=True --env PDP_API_KEY=<VOTRE_CLE_API> permitio/pdp-v2:latest
```

![Permit.io - test local](https://cdn.hashnode.com/res/hashnode/image/upload/v1729515246656/6bed08e3-6109-4643-a724-f55641d7c974.png align="center")

### **Étape 4 : Exécution de l'application**

Vous pouvez exécuter l'application en utilisant la commande `Gradle` suivante :

```dockerfile
./gradlew bootRun
```

![Permit.io - comment exécuter l'application en local](https://cdn.hashnode.com/res/hashnode/image/upload/v1729515837209/41556843-b8d5-4433-a2f3-93371562d27d.png align="center")

#### **Visualisation et création de produits**

Interagissons maintenant avec les points de terminaison de l'application en utilisant [REQBIN](https://reqbin.com/curl).

Tout d'abord, créez un nouvel utilisateur en utilisant le point de terminaison `/api/users/signup`.

```dockerfile
curl -X POST "http://localhost:8080/api/users/signup" -H "Content-Type: application/json" -d 'johndoe'
```

Vous devriez pouvoir voir l'utilisateur dans votre projet Permit, sous Directory > All Tenants.

Initialement, l'utilisateur n'a aucun rôle, donc il ne peut pas faire grand-chose. Par exemple, essayer de lister les produits entraînera une réponse 403 Forbidden, comme montré ci-dessous. Le code d'erreur 403 signifie que l'utilisateur n'a pas les permissions pour accéder à la ressource demandée, qui dans ce cas est les produits. Vous pouvez en apprendre plus sur [la différence entre les codes d'erreur 401 et 403 ici](https://www.permit.io/blog/401-vs-403-error-whats-the-difference).

![Permit.io - points de terminaison](https://cdn.hashnode.com/res/hashnode/image/upload/v1729498632123/aaf26b76-a89f-4e6b-9324-85d082b8061d.png align="center")

Pour que l'utilisateur puisse voir une liste de produits, attribuez-lui un rôle de lecteur en utilisant la commande ci-dessous :

```dockerfile
curl -X POST "http://localhost:8080/api/users/assign-role" \
-H "Authorization: Bearer johndoe" \
-H "Content-Type: application/json" \
-d 'viewer'
```

Vous devriez voir que l'utilisateur `johndoe` s'est vu attribuer le rôle de lecteur, comme montré ci-dessous :

![Permit.io - utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1729498710784/ebd789fd-ec52-4146-bb94-6f300edb9d7e.png align="center")

Puisqu'un lecteur peut créer un produit, utilisez la commande ci-dessous pour créer un produit avec l'utilisateur `johndoe`.

```dockerfile
curl -X POST "http://localhost:8080/api/products" -H "Authorization: Bearer johndoe" -H "Content-Type: application/json" -d 'MacBook'
```

Vous devriez voir qu'un nouveau produit est créé avec l'identifiant 1 et que l'utilisateur `johndoe` a été ajouté en tant que fournisseur.

![Permit.io - points de terminaison de l'API](https://cdn.hashnode.com/res/hashnode/image/upload/v1729498758160/c14169f0-d720-465e-9bc1-f7096e6da31a.png align="center")

#### **Ajout d'avis aux produits**

Pour ajouter des avis aux produits, créez un autre utilisateur appelé `jane`.

```dockerfile
curl -X POST "http://localhost:8080/api/users/signup" -H "Content-Type: application/json" -d 'jane'
```

Pour que l'utilisateur puisse ajouter un avis aux produits, attribuez-lui un rôle de `lecteur` en utilisant la commande ci-dessous :

```dockerfile
curl -X POST "http://localhost:8080/api/users/assign-role" \
-H "Authorization: Bearer jane" \
-H "Content-Type: application/json" \
-d 'viewer'
```

Ensuite, vous pouvez ajouter un avis au produit ajouté par `johndoe` en utilisant la commande ci-dessous :

```dockerfile
curl -X POST "http://localhost:8080/api/products/1/review" -H "Authorization: Bearer jane" -H "Content-Type: application/json" -d 'Le produit était de bonne qualité'
```

Félicitations ! Vous avez terminé le projet pour ce tutoriel.

## **Prochaines étapes**

Maintenant que vous avez appris à implémenter l'autorisation fine dans vos applications Java et Spring Boot en utilisant [Permit.io](http://Permit.io), vous pourriez vouloir explorer davantage.

Voici quelques ressources précieuses :

* [Documentation Permit.io](https://docs.permit.io/)
    
* [RBAC VS ABAC : Choisir le bon modèle de politique d'autorisation](https://www.permit.io/blog/rbac-vs-abac)
    

### **Avant de terminer**

J'espère que vous avez trouvé ce tutoriel instructif.

Voici quelques-uns de mes autres articles de blog récents que vous pourriez apprécier :

* [Apprendre React – Un guide des concepts clés](https://www.freecodecamp.org/news/learn-react-key-concepts/)
    
* [**Neon Postgres vs Supabase**](https://www.devtoolsacademy.com/blog/neon-vs-supabase)
    
* [Développement Full Stack avec Next.js, Clerk et Neon Postgres](https://www.freecodecamp.org/news/nextjs-clerk-neon-fullstack-development/)
    

Pour plus de tutoriels sur des outils de développement incroyables, assurez-vous de consulter mon blog [DTA](https://www.devtoolsacademy.com/).

Suivez-moi sur [Twitter](https://x.com/TheAnkurTyagi) pour obtenir des mises à jour en direct sur mes autres projets.

Bonne programmation.