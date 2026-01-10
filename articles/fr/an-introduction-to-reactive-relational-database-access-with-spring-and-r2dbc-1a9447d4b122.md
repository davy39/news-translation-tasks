---
title: Une introduction à l'accès réactif aux bases de données relationnelles avec
  Spring et R2DBC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-16T10:28:54.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-reactive-relational-database-access-with-spring-and-r2dbc-1a9447d4b122
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y5vRk0tztWvhhbWrvJrm-g.png
tags:
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: spring data
  slug: spring-data
- name: 'tech '
  slug: tech
seo_title: Une introduction à l'accès réactif aux bases de données relationnelles
  avec Spring et R2DBC
seo_desc: 'By Daniel Newton

  Not too long ago, a reactive variant of the JDBC driver was released, known as R2DBC.
  It allows data to be streamed asynchronously to any endpoints that have subscribed
  to it. Using a reactive driver like R2DBC together with Spring, ...'
---

Par Daniel Newton

Il n'y a pas si longtemps, une variante réactive du pilote JDBC a été publiée, connue sous le nom de R2DBC. Elle permet de diffuser des données de manière asynchrone vers tous les points de terminaison qui y sont abonnés. L'utilisation d'un pilote réactif comme R2DBC avec Spring et WebFlux vous permet d'écrire une application complète qui gère la réception et l'envoi de données de manière asynchrone.

Dans cet article, nous nous concentrerons sur la base de données, depuis la connexion à la base de données jusqu'à l'enregistrement et la récupération des données. Pour ce faire, nous utiliserons Spring Data. Comme tous les modules Spring Data, il nous fournit une configuration prête à l'emploi. Cela réduit la quantité de code standard que nous devons écrire pour configurer notre application. En plus de cela, il fournit une couche au-dessus du pilote de base de données qui facilite les tâches simples et rend les tâches plus difficiles un peu moins pénibles.

Pour le contenu de cet article, j'utilise une base de données Postgres. Au moment de l'écriture, seuls Postgres, H2 et Microsoft SQL Server ont leurs propres implémentations de pilotes R2DBC.

J'ai précédemment écrit deux articles sur les bibliothèques Spring Data réactives, l'un sur [Mongo](https://lankydanblog.com/2017/07/16/a-quick-look-into-reactive-streams-with-spring-data-and-mongodb/) et un autre sur [Cassandra](https://lankydanblog.com/2017/12/11/reactive-streams-with-spring-data-cassandra/). Vous avez peut-être remarqué que aucune de ces bases de données n'est une base de données RDBMS. Il existe d'autres pilotes réactifs disponibles depuis longtemps (j'ai écrit l'article sur Mongo il y a près de 2 ans), mais au moment de l'écriture, un pilote réactif pour une base de données RDBMS est encore une chose assez nouvelle. Cet article suivra un format similaire à ceux-ci.

De plus, j'ai également écrit un article sur l'utilisation de [Spring WebFlux](https://lankydanblog.com/2018/03/15/doing-stuff-with-spring-webflux/) que j'ai mentionné dans l'introduction. N'hésitez pas à y jeter un coup d'œil si vous êtes intéressé par la création d'une application web entièrement réactive.

### Dépendances

Il y a quelques points à souligner ici.

Plus vous utilisez Spring Boot, plus vous vous habituerez à importer une seule dépendance `spring-boot-starter` pour la chose cool que vous voulez faire. Par exemple, j'espérais qu'il y aurait une dépendance `spring-boot-starter-r2dbc`, mais malheureusement, il n'y en a pas. Pas encore.

Simplement dit, cette bibliothèque est du côté des plus récentes et, au moment de l'écriture, ne dispose pas de son propre module Spring Boot qui contient toutes les dépendances dont elle a besoin, ainsi qu'une configuration plus rapide via l'auto-configuration. Je suis sûr que ces choses viendront à un moment donné et rendront la configuration d'un pilote R2DBC encore plus facile.

Pour l'instant, nous devrons remplir quelques dépendances supplémentaires manuellement.

De plus, les bibliothèques R2DBC n'ont que des versions Milestone (preuve supplémentaire de leur nouveauté), nous devons donc nous assurer d'inclure le dépôt Milestone de Spring. Je devrai probablement mettre à jour cet article à l'avenir lorsqu'une version sera publiée.

### Connexion à la base de données

Grâce à Spring Data qui fait beaucoup de travail pour nous, le seul Bean qui doit être créé manuellement est le `ConnectionFactory` qui contient les détails de connexion de la base de données :

La première chose à remarquer ici est l'extension de `AbstractR2dbcConfiguration`. Cette classe contient un ensemble de Beans que nous n'avons plus besoin de créer manuellement. La mise en œuvre de `connectionFactory` est la seule exigence de la classe, car elle est nécessaire pour créer le Bean `DatabaseClient`. Ce type de structure est typique des modules Spring Data, il est donc assez familier lorsque vous essayez un module différent. De plus, je m'attends à ce que cette configuration manuelle soit supprimée une fois que l'auto-configuration sera disponible et soit entièrement pilotée via le fichier `application.properties`.

J'ai inclus la propriété `port` ici, mais si vous n'avez pas modifié la configuration de votre Postgres, vous pouvez vous fier à la valeur par défaut de `5432`.

Les quatre propriétés : `host`, `database`, `username` et `password` définies par `PostgresqlConnectionFactory` sont le minimum requis pour qu'elle fonctionne. Moins que cela et vous rencontrerez des exceptions lors du démarrage.

En utilisant cette configuration, Spring est capable de se connecter à une instance Postgres en cours d'exécution.

Le dernier élément d'information notable de cet exemple est l'utilisation de `@EnableR2dbcRepositories`. Cette annotation indique à Spring de trouver toutes les interfaces de dépôt qui étendent l'interface `Repository` de Spring. Cela est utilisé comme interface de base pour instrumenter les dépôts Spring Data. Nous examinerons cela de plus près dans la section suivante. Le principal élément d'information à retenir ici est que vous devez utiliser l'annotation `@EnableR2dbcRepositories` pour tirer pleinement parti des capacités de Spring Data.

### Création d'un dépôt Spring Data

Comme mentionné précédemment, dans cette section, nous examinerons l'ajout d'un dépôt Spring Data. Ces dépôts sont une fonctionnalité intéressante de Spring Data, ce qui signifie que vous n'avez pas besoin d'écrire beaucoup de code supplémentaire pour simplement écrire une requête.

Malheureusement, au moins pour l'instant, Spring R2DBC ne peut pas inférer les requêtes de la même manière que les autres modules Spring Data le font actuellement (je suis sûr que cela sera ajouté à un moment donné). Cela signifie que vous devrez utiliser l'annotation `@Query` et écrire le SQL à la main. Regardons cela :

Cette interface étend `R2dbcRepository`. Cela étend à son tour `ReactiveCrudRepository` et ensuite `Repository`. `ReactiveCrudRepository` fournit les fonctions CRUD standard et, d'après ce que je comprends, `R2dbcRepository` ne fournit aucune fonction supplémentaire et est plutôt une interface créée pour une meilleure dénomination situationnelle.

`R2dbcRepository` prend deux paramètres génériques, l'un étant la classe d'entité qu'il prend en entrée et produit en sortie. Le second étant le type de la clé primaire. Par conséquent, dans cette situation, la classe `Person` est gérée par le `PersonRepository` (ce qui est logique) et le champ de la clé primaire à l'intérieur de `Person` est un `Int`.

Les types de retour des fonctions de cette classe et celles fournies par `ReactiveCrudRepository` sont `Flux` et `Mono` (non vu ici). Ce sont des types Project Reactor que Spring utilise comme types de flux réactifs par défaut. `Flux` représente un flux de plusieurs éléments tandis qu'un `Mono` est un résultat unique.

Enfin, comme je l'ai mentionné avant l'exemple, chaque fonction est annotée avec `@Query`. La syntaxe est assez simple, avec la requête SQL étant une chaîne à l'intérieur de l'annotation. Le `$1` (`$2`, `$3`, etc. pour plus d'entrées) représente la valeur d'entrée de la fonction. Une fois que vous avez fait cela, Spring gérera le reste et passera les entrées dans leurs paramètres d'entrée respectifs, recueillera les résultats et les mappers à la classe d'entité désignée du dépôt.

### Un très rapide coup d'œil à l'entité

Je ne vais pas dire grand-chose ici, mais simplement montrer la classe `Person` utilisée par le `PersonRepository`.

En fait, il y a un point à faire ici. `id` a été rendu nullable et une valeur par défaut de `null` a été fournie pour permettre à Postgres de générer lui-même la valeur suivante appropriée. Si cela n'est pas nullable et qu'une valeur `id` est fournie, Spring essaiera en fait d'exécuter une mise à jour au lieu d'une insertion lors de l'enregistrement. Il existe d'autres moyens de contourner cela, mais je pense que cela est suffisant.

Cette entité sera mappée à la table `people` définie ci-dessous :

### Voir tout cela en action

Maintenant, regardons cela en action. Ci-dessous se trouve du code qui insère quelques enregistrements et les récupère de différentes manières :

Une chose que je mentionnerai à propos de ce code. Il y a une possibilité très réelle qu'il s'exécute sans réellement insérer ou lire certains des enregistrements. Mais, lorsque vous y pensez, cela a du sens. Les applications réactives sont censées faire des choses de manière asynchrone et, par conséquent, cette application a commencé à traiter les appels de fonction dans différents threads. Sans bloquer le thread principal, ces processus asynchrones pourraient ne jamais s'exécuter complètement. Pour cette raison, il y a quelques appels `Thread.sleep` dans ce code, mais je les ai supprimés de l'exemple pour garder tout propre.

La sortie de l'exécution du code ci-dessus ressemblerait à quelque chose comme ceci :

```
[ main] onSubscribe(FluxConcatMap.ConcatMapImmediate)[ main] request(unbounded)[actor-tcp-nio-1] onNext(Person(id=35, name=Dan Newton, age=25))[actor-tcp-nio-1] onNext(Person(id=36, name=Laura So, age=23))[actor-tcp-nio-1] onComplete()[actor-tcp-nio-2] findAll - Person(id=35, name=Dan Newton, age=25)[actor-tcp-nio-2] findAll - Person(id=36, name=Laura So, age=23)[actor-tcp-nio-4] findAllByName - Person(id=36, name=Laura So, age=23)[actor-tcp-nio-5] findAllByAge - Person(id=35, name=Dan Newton, age=25)
```

Quelques points à retenir ici :

* `onSubscribe` et `request` se produisent sur le thread principal où le `Flux` a été appelé. Seule la méthode `saveAll` produit cela puisqu'elle inclut la fonction `log`. L'ajout de cela aux autres appels aurait conduit au même résultat de journalisation sur le thread principal.
* L'exécution contenue dans la fonction subscribe et les étapes internes du `Flux` sont exécutées sur des threads séparés.

Cela n'est en aucun cas une représentation réelle de la manière dont vous utiliseriez les flux réactifs dans une application réelle, mais cela démontre, je l'espère, comment les utiliser et donne un peu d'information sur la manière dont ils s'exécutent.

### Conclusion

En conclusion, les flux réactifs sont arrivés sur certaines bases de données RDBMS grâce au pilote R2DBC et à Spring Data qui construit une couche par-dessus pour rendre tout un peu plus propre. En utilisant Spring Data R2DBC, nous sommes capables de créer une connexion à une base de données et de commencer à l'interroger sans avoir besoin de trop de code.

Bien que Spring fasse déjà beaucoup pour nous, il pourrait en faire plus. Actuellement, il ne dispose pas du support d'auto-configuration de Spring Boot. Ce qui est un peu ennuyeux. Mais, je suis sûr que quelqu'un s'en occupera bientôt et rendra tout encore meilleur que ce n'est déjà le cas.

Le code utilisé dans cet article peut être trouvé sur mon [GitHub](https://github.com/lankydan/spring-data-r2dbc).

Si vous avez trouvé cet article utile, vous pouvez me suivre sur Twitter à [@LankyDanDev](https://twitter.com/LankyDanDev) pour rester informé de mes nouveaux articles.

[Voir tous les articles de Dan Newton](https://lankydanblog.com/author/danknewton/)

_Publié à l'origine sur [lankydanblog.com](https://lankydanblog.com/2019/02/16/asynchronous-rdbms-access-with-spring-data-r2dbc/) le 16 février 2019._