---
title: 'Au-delà d''Android : comment Kotlin fonctionne sur le Backend'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-06T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/going-beyond-android-kotlin-on-the-backend-2a75eef2582b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6K5vmzalJUxn44v3cm6wBw.jpeg
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Au-delà d''Android : comment Kotlin fonctionne sur le Backend'
seo_desc: 'By Adam Arold

  This article is part of a series.

  While most developers use Kotlin on Android, it is also a viable option on other
  platforms. In this article, we’ll look at how it works on the backend.

  As I have written about this before, I think that ...'
---

Par Adam Arold

Cet article fait partie d'une [série](http://the-cogitator.com/2017/12/21/beyond-android-exploring-kotlin-areas-of-application.html).

Alors que la plupart des développeurs utilisent Kotlin sur Android, c'est également une option viable sur d'autres plateformes. Dans cet article, nous allons voir comment il fonctionne sur le backend.

Comme [je l'ai déjà écrit](http://the-cogitator.com/2017/05/19/kotlin-is-the-new-java.html), je pense que l'interopérabilité entre Java et Kotlin est assez transparente. Cela signifie également que l'utilisation de Kotlin à la place de Java sur le backend est plutôt facile. À part quelques nuisances, vous pouvez commencer à écrire vos nouvelles fonctionnalités en Kotlin dans votre projet Java. Ou si vous voulez simplement l'essayer, vous pouvez commencer par écrire vos tests avec.

Si vous regardez autour de vous, il semble que les entreprises avec une grande part du marché du backend aient la même pensée : la nouvelle version de Spring a des fonctionnalités [dédiées à Kotlin](https://tech.io/playgrounds/8594/spring-5---dedicated-kotlin-features), et vous pouvez même utiliser Kotlin pour écrire vos scripts Gradle en utilisant le [kotlin-dsl](https://github.com/gradle/kotlin-dsl).

Ce qui est intéressant à noter ici, c'est que **vous n'avez pas besoin de support Kotlin pour aucune de ces bibliothèques**, car les fonctionnalités d'interopérabilité Java de Kotlin sont si bonnes.

### Décisions

Lorsque vous commencez à travailler avec Kotlin sur le backend, vous avez plusieurs options à votre disposition.

Si vous choisissez d'utiliser une bibliothèque écrite en Kotlin, vous obtenez certains avantages majeurs : il n'y aura pas de problèmes de compatibilité liés à la langue que vous utilisez puisque tout est écrit en Kotlin. Une autre chose à mentionner est qu'il y a certaines choses qui ne sont présentes que dans Kotlin, comme les coroutines et les génériques réifiés.

Le compromis est que la plupart de ces bibliothèques ne sont pas très anciennes et pourraient avoir les problèmes typiques des nouveaux projets : manque de documentation et éventuels bugs ou problèmes de conception.

Si vous avez besoin de quelque chose qui est testé en conditions réelles, vous ne pouvez pas vous tromper avec des outils comme [Spring](https://docs.spring.io/spring/docs/5.0.2.RELEASE/spring-framework-reference/) ou [Mockito](http://site.mockito.org/). Ce que vous obtenez avec ceux-ci, c'est que la plupart des problèmes sont bien documentés, et vous obtiendrez des réponses à vos questions assez rapidement. Ce que vous perdez, cependant, c'est certaines des bonnes choses à propos de Kotlin : ils n'ont pas de [Kotlin DSL](https://kotlinlang.org/docs/reference/type-safe-builders.html), et le code sera assez Java-ish.

Une autre option est de choisir une bibliothèque qui a un support intégré pour Kotlin. [RxKotlin](https://github.com/ReactiveX/RxKotlin) et [vert.x](https://github.com/vert-x3/vertx-lang-kotlin) sont de bons exemples de cela. Je vais appeler ces projets des _hybrides_ à partir de maintenant. Avec eux, vous obtenez le meilleur des deux mondes : vous aurez généralement une bonne API qui est idiomatique d'un point de vue Kotlin, et derrière elle, il y aura quelque chose qui est bien connu et testé en conditions réelles.

Regardons quelques bibliothèques que vous pourriez vouloir essayer.

Notez que ce qui suit sont juste mes opinions, et à ce titre, elles sont subjectives.

#### Ktor

[**Ktor**](http://ktor.io/) est l'un des nouveaux frameworks web écrits en Kotlin. Il est livré avec Netty intégré et un joli DSL. Ce qui est intéressant ici, c'est qu'il tire parti du support des [Coroutines](https://kotlinlang.org/docs/reference/coroutines.html) de Kotlin. Voici à quoi cela ressemble en pratique :

J'étais préoccupé lorsque je l'ai essayé que la documentation est [plutôt manquante](http://ktor.io/servers/structure.html). Lorsque vous tombez sur un problème, vous êtes plus susceptible de rester bloqué. Il ne [performant pas bien](https://www.techempower.com/benchmarks/#section=data-r14&hw=ph&test=plaintext), et l'interopérabilité avec Java est un peu douteuse.

#### Javalin

[Javalin](https://javalin.io/) est un autre framework web qui a une API très simple, fluide et lisible. Il peut également fonctionner avec plusieurs serveurs web intégrés comme Netty ou Undertow. Ce que j'ai le plus aimé, c'est qu'il trouve un équilibre entre l'approche minimaliste de [Spark](http://sparkjava.com/) (à ne pas confondre avec [Apache Spark](https://spark.apache.org/)) et la nature de bas niveau de [vert.x](http://vertx.io/). La [documentation](https://javalin.io/documentation) est également très bonne, donc vous pouvez commencer en un rien de temps :

J'aime que l'API soit un peu plus Java-ish que celle de Ktor, donc si vous venez d'un milieu Java, il pourrait être plus facile de commencer avec.

#### Hexagon

[Hexagon](http://hexagonkt.com/) est un choix intéressant pour écrire des applications web. Le choix du nom n'est pas aléatoire : il encourage l'utilisation de l'[architecture hexagonale](http://alistair.cockburn.us/Hexagonal+architecture) (plus communément connue sous le nom d'[architecture propre](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)), et il est également [plus performant](https://www.techempower.com/benchmarks/#section=data-r14&hw=ph&test=plaintext) que ktor ou même le framework Spring ! Le DSL que vous obtenez est également assez descriptif :

#### Hors du web

Il est intéressant de noter qu'il existe de [nombreux outils](https://kotlin.link/) écrits en Kotlin parmi lesquels vous pouvez choisir. Kotlin dispose d'un framework de spécification très utile [specification framework](https://github.com/spekframework/spek). Si vous n'aimez pas le fait qu'il n'y ait pas de bons clients HTTP pour Java, vous pouvez maintenant profiter de [Fuel](https://github.com/kittinunf/Fuel), qui est un outil très pratique pour interagir avec des endpoints REST et au-delà. Vous avez même des outils pour [écrire des jeux](https://github.com/Hexworks/zircon) en Kotlin.

### Frameworks Java

#### vert.x

[vert.x](http://vertx.io/) est un framework web multi-module similaire à [Spring](https://docs.spring.io/spring/docs/5.0.2.RELEASE/spring-framework-reference/). Ce qui est important à noter ici, c'est qu'il existe une [section de documentation](http://vertx.io/docs/vertx-core/kotlin/) dédiée à Kotlin. vert.x pourrait être votre choix pour écrire des applications web si la performance est primordiale pour vous : vert.x a [de très bons scores de benchmark](https://www.techempower.com/benchmarks/#section=data-r14&hw=ph&test=plaintext). Cela ne devrait pas être une surprise, car il implémente le [modèle multi réacteur](http://vertx.io/docs/vertx-core/java/#_reactor_and_multi_reactor) (le modèle réacteur pourrait vous être familier à partir de [node.js](https://www.packtpub.com/mapt/book/web_development/9781783287314/1/ch01lvl1sec09/the-reactor-pattern)).

Il est intéressant de noter qu'il existe de très bons [exemples Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/kotlin-examples) pour vert.x. Vous en aurez besoin car il a certains concepts qui ne sont pas présents ailleurs et sa configuration est également un peu plus impliquée :

#### Spring

Pour de nombreux développeurs Java, [Spring](https://docs.spring.io/spring/docs/5.0.2.RELEASE/spring-framework-reference/) est l'outil de facto pour écrire des applications Java. La bonne nouvelle est que depuis la version _5.0_, Spring a un [support intégré](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0) pour Kotlin. Il existe une multitude de [projets Spring](https://spring.io/projects) parmi lesquels vous pouvez choisir. Si vous êtes intéressé, il existe un simple [tutoriel](https://kotlinlang.org/docs/tutorials/spring-boot-restful.html) qui vous permettra de commencer à utiliser Spring avec Kotlin. Voici à quoi ressemble Hello World avec :

#### Sparkjava

[Sparkjava](http://sparkjava.com/) est un framework web (micro) minimaliste. Vous pouvez commencer à l'utiliser avec pratiquement zéro investissement de temps, et si vous venez de node.js, c'est également un très bon choix. Vous ne pouvez pas non plus être plus minimaliste que cela :

### Options hybrides

Alors que l'interfaçage avec les outils Java est généralement assez pratique, certains des outils ci-dessus ont un support d'outillage écrit pour Kotlin :

[**Spark-kotlin**](https://github.com/perwendel/spark-kotlin) offre une expérience plus rationalisée pour les utilisateurs de Kotlin, et il est également intéressant de noter qu'il est écrit par [perwendel](https://github.com/perwendel), l'auteur original de Sparkjava.

[**vertx-lang-kotlin**](https://github.com/vert-x3/vertx-lang-kotlin) fournit des options spécifiques à Kotlin utiles pour vert.x comme les coroutines, les workers one-shot ou les flux réactifs.

Alors qu'utiliser Mockito depuis Kotlin est principalement agréable, [**mockito-kotlin**](https://github.com/nhaarman/mockito-kotlin) améliore cela en vous donnant un joli DSL et en prenant soin de certains problèmes.

[**Hamkrest**](https://github.com/npryce/hamkrest) est une réimplémentation de [Hamcrest](http://hamcrest.org/) avec des sucres syntaxiques, de l'extensibilité et plus.

[**RxKotlin**](https://github.com/ReactiveX/RxKotlin) ajoute des [fonctions d'extension](https://kotlinlang.org/docs/reference/extensions.html) pratiques, des aides SAM, et plus à [RxJava](https://github.com/ReactiveX/RxJava). Le seul problème est que la documentation est derrière un [paywall](https://www.packtpub.com/application-development/learning-rxjava).

### Un exemple fonctionnel

Maintenant, regardons un exemple étape par étape. Nous allons utiliser Spring Boot avec [Spring Initializr](https://start.spring.io/).

Le code source de ce tutoriel peut être trouvé [ici](https://github.com/AppCraft-Projects/spring-boot-kotlin-demo).

### Getting started

Spring Boot est livré avec [Spring Initializr](https://start.spring.io/), qui est un outil pratique avec lequel vous pouvez rapidement lancer votre projet. Je recommande de sélectionner _Gradle Project_ avec _Kotlin_ et Spring Boot _2.0.0_ pour cet exemple, car avec **2.0.0**, vous obtiendrez les fonctionnalités de _Spring 5.0_.

Si vous cliquez sur "Switch to full version", vous pourrez également assembler un squelette finement granulaire. Il y a une cornucope de sujets parmi lesquels vous pouvez choisir des outils allant du Web à AWS et plus. Pour cet exercice, j'ai choisi uniquement le Web.

Après avoir configuré Initializr, cliquez sur "Generate Project" et ouvrez-le dans votre IDE. Vous pourriez remarquer que, par rapport à un simple projet Java, vous n'avez pas besoin d'ajouter beaucoup de choses à votre `build.gradle` qui sont spécifiques à Kotlin. Je les ai extraites dans cet exemple :

### Ajout d'un simple Controller

Si vous regardez le point d'entrée de l'application, il est plutôt minimaliste :

Maintenant, la seule chose dont nous avons besoin pour un Hello World fonctionnel est d'ajouter un `RestController` à notre projet :

et **Bam !** vous avez terminé ! Vous pouvez aller voir le résultat à l'adresse `[http://localhost:8080/](http://localhost:8080/)` après l'avoir démarré avec `./gradlew bootRun` :

Vous pouvez en apprendre plus sur le fonctionnement de cela [dans ce tutoriel](https://spring.io/guides/gs/spring-boot/). Ou si vous voulez voir à quoi ressemblent les API Kotlin et la manière fonctionnelle, il y a un bon tutoriel [ici](https://spring.io/blog/2017/08/01/spring-framework-5-kotlin-apis-the-functional-way).

### Conclusion

Dans cet article, nous avons exploré certaines des options les plus connues pour le développement backend avec Kotlin. Nous avons également vu que les acteurs majeurs du marché ont _adopté Kotlin_, et que le développement backend peut être beaucoup plus simple avec lui par rapport à Java pur.

Dans le prochain article, nous explorerons comment Kotlin peut être utilisé dans votre projet à la place de Javascript !

_Merci d'avoir lu ! Vous pouvez lire plus de mes articles sur [mon blog](http://the-cogitator.com/2018/01/06/going-beyond-android-kotlin-on-the-backend.html)._