---
title: Comment configurer Vertx dans Spring
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T01:43:36.000Z'
originalURL: https://freecodecamp.org/news/vertx-in-spring-39c2dd7bc2a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zOLXCXhrX_NgyWJf3KGmrQ.jpeg
tags:
- name: Java
  slug: java
- name: MySQL
  slug: mysql
- name: spring-boot
  slug: spring-boot
- name: 'tech '
  slug: tech
- name: vertx
  slug: vertx
seo_title: Comment configurer Vertx dans Spring
seo_desc: 'By Rick Lee

  Spring is probably the most popular framework in the Java space. We all love its
  dependency injection and all that autowired/configuration magic. It makes unit testing
  a piece of cake.

  On the other hand, Vertx.io, which is a newer toolkit...'
---

Par Rick Lee

[Spring](https://spring.io/) est probablement le framework le plus populaire dans l'espace Java. Nous aimons tous son injection de dépendances et toute cette magie autowired/configuration. Cela rend les tests unitaires très simples.

D'autre part, [Vertx.io](https://vertx.io/), qui est un nouvel outil/ framework, gagne en popularité ces dernières années. Il est léger et supporte la programmation entièrement asynchrone via une boucle d'événements comme Node.js et la messagerie eventbus comme Akka. De plus, la communauté a créé de nombreux outils/clients de base de données asynchrones comme [Async MySQL / PostgreSQL Client](https://vertx.io/docs/vertx-mysql-postgresql-client/java/), ce qui en fait un autre choix tendance à côté de Spring.

Il semble difficile de choisir entre Vertx et Spring pour de nouveaux projets, mais la bonne nouvelle est qu'ils ne sont pas mutuellement exclusifs ! Voici un exemple simple pour illustrer la configuration.

Ce projet d'exemple concerne le déploiement d'un Vertical dans une application Springboot. Le Vertical fournit une fonction pour interroger MySQL en utilisant un client MySQL asynchrone. La fonction peut être appelée directement ou via vertx.eventbus.

Tout d'abord, créez une simple application Springboot avec Maven. Vous pouvez la créer via [Spring Initializer](https://start.spring.io/). Ensuite, ajoutez ce qui suit au fichier pom.xml :

Comme nous allons interroger MySQL en utilisant [Async MySQL / PostgreSQL Client](https://vertx.io/docs/vertx-mysql-postgresql-client/java/), un MysqlClient.java très primitif est créé et la configuration MySQL est mise dans le fichier application.yaml.

Créez une table utilisateur factice avec 2 champs et insérez quelques données :

Optionnellement, créez une classe de dépôt pour accéder à la table utilisateur :

Maintenant, nous pouvons créer le vertical, qui a une seule méthode pour gérer les requêtes MySQL.

Enfin, créez l'application Spring et ajoutez une méthode deployVerticle avec l'annotation @PostConstruct.

Si vous exécutez l'application Spring, vous verrez l'impression système suivante de « dbVerticle deployed » et cela signifie que le Verticle est en cours d'exécution sur l'application Spring.

```
2019-02-11 08:56:27.110  INFO 29444 --- [ntloop-thread-0] i.v.ext.asyncsql.impl.MYSQLClientImpl    : Creating configuration for localhost:33062019-02-11 08:56:27.442  INFO 29444 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'dbVerticle deployed2019-02-11 08:56:27.848  INFO 29444 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''2019-02-11 08:56:27.853  INFO 29444 --- [           main] n.r.s.SpringVertxExampleApplication      : Started SpringVertxExampleApplication in 5.393 seconds (JVM running for 6.671)
```

Pour le tester, nous pouvons simplement ajouter une requête de base de données juste après le déploiement du Verticle.

La console imprime ce qui suit :

```
dbVerticle deployedsuccess[{"id":10466,"username":"ricklee"}][{"id":10468,"username":"maryjohnson"}]
```

Cet exemple a illustré comment vous pouvez profiter des facilités des mondes Spring et Vertx avec une configuration simple.

Code source ici : [https://github.com/rickcodetalk/spring-vertx-example](https://github.com/rickcodetalk/spring-vertx-example)