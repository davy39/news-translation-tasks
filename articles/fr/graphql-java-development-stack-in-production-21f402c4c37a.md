---
title: Comment démarrer votre serveur GraphQL Java en un rien de temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T01:37:39.000Z'
originalURL: https://freecodecamp.org/news/graphql-java-development-stack-in-production-21f402c4c37a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*49DDRZhUWvVnH-QNHuSUSw.png
tags:
- name: GraphQL
  slug: graphql
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: 'tech '
  slug: tech
seo_title: Comment démarrer votre serveur GraphQL Java en un rien de temps
seo_desc: 'By Prithviraj Pawar

  GraphQL is a query language for fetching data over the internet. Since its public
  announcement by Facebook in 2015, it has sparked interest in many minds. GraphQL
  has primarily been used in JavaScript. In fact, Facebook released t...'
---

Par Prithviraj Pawar

GraphQL est un langage de requête pour récupérer des données sur Internet. Depuis son annonce publique par Facebook en 2015, il a suscité l'intérêt de nombreux esprits. [GraphQL](http://graphql.org/) a principalement été utilisé en JavaScript. En fait, Facebook a publié l'implémentation de référence pour celui-ci en JavaScript ([graphql-js](https://github.com/graphql/graphql-js)).

Mais cet article de blog se concentrera sur le développement du serveur GraphQL en Java. [**GraphQL-Java**](https://github.com/graphql-java/graphql-java) est l'implémentation correspondante de GraphQL en Java, et il reçoit des mises à jour et des améliorations de version presque tous les mois. Des fonctionnalités comme l'instrumentation, les appels asynchrones au backend, le dataloader, les directives, et bien d'autres en font un dépôt très intéressant et puissant en Java.

![Image](https://cdn-media-1.freecodecamp.org/images/1*49DDRZhUWvVnH-QNHuSUSw.png)
_GraphQL Java_

### Comment construire un serveur GraphQL Java dans Spring Boot

Prenons l'exemple d'une école de magie de l'**univers de Harry Potter**. Les données de l'école de magie sont les suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hXbJSrgal1fqUEvTl--Zlw.jpeg)

Ici, les DataStores peuvent être des serveurs backend, ou même des bases de données. Une récupération RESTful ressemblerait à ceci.

```
GET: /student?{parameters}GET: /House?{parameters}
```

En gros, exposez une interface pour un service. Ainsi, si des **Professeurs** sont ajoutés dans le modèle ci-dessus, alors un nouveau point de terminaison doit être ouvert et le client doit faire plusieurs allers-retours. De plus, si le client veut des données imbriquées comme **l'origine de la baguette de Harry** ou **la couleur de la maison de Ron**, alors le serveur API doit appeler le backend deux fois. Cela entraînera également certaines informations indésirables sur la maison et la baguette.

**Entrez GraphQL** : GraphQL est une approche basée sur un schéma pour récupérer des données. Il modélise les données sous forme de graphes, et vous devez émettre une requête pour récupérer les données. Il fonctionne comme SQL, mais pour les objets web. Ainsi, une requête graphQL pour **Harry** ressemble à ceci :

```
query{Magic School{Student{namewand{origin}}}}
```

Avant de passer à GraphQL, nous devons configurer un MVC Spring. La manière la plus simple de faire cela est [SpringBootStarter](https://start.spring.io/). Vous pouvez sélectionner votre outil d'automatisation de build souhaité. Cela donne un package de Tomcat intégré à Spring prêt à fonctionner sur le port 8080. Pour tester Tomcat, exécutez :

```
$gradle clean build$java -jar ./build/libs/graphql-demo-0.0.1-SNAPSHOT.jar
```

Par défaut, Gradle nomme votre JAR « project_name-version-SNAPSHOT.jar ». Vérifiez [_http:localhost:8080_](http://localhost:8080/) pour voir Tomcat fonctionner sur le port 8080.

Ajoutons maintenant une dépendance [GraphQL-Java](https://github.com/graphql-java/graphql-java) dans notre **build.gradle**_._

```
dependencies {compile('com.graphql-java:graphql-java:{version}')compile group: 'org.json', name: 'json', version: '20170516'}
```

Ajoutez la version actuelle comme trouvée dans le dépôt [mavenCentral](https://mvnrepository.com/artifact/com.graphql-java/graphql-java). Actuellement, la dernière version est 8.0. Ajoutez également **org.json**, qui est une bibliothèque pratique car GraphQL gère la requête-réponse en JSON.

Comme je l'ai mentionné précédemment, GraphQL est un langage basé sur un schéma. Il demande aux utilisateurs de sélectionner des objets dans la requête en fonction du schéma.

Plongeons directement dans le sujet :

Nous avons ouvert une interface **/graphql** pour les requêtes POST GraphQL_._ Nous devons créer un schéma pour représenter les données.

* **SchemaGenerator** analyse le schéma et crée un [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) avec les noms des champs comme nœuds enfants.
* Ensuite, les champs sont assignés à des types par **TypeDefinitionRegistry**, par exemple Int, String, etc. GraphQL a un système de [Type](http://graphql-java.readthedocs.io/en/latest/scalars.html) agréable où nous pouvons avoir des types personnalisés dans le schéma, y compris enum, interfaces, unions, listes, et plus encore.
* Jetez un œil à l'étape **RuntimeWiring()** où le champ « MagicSchool » est mappé à « Hogwarts » par un **StaticDataFetcher**_._
* Chaque champ est soutenu par un **datafetcher**, et c'est le travail du datafetcher de résoudre les données et de les retourner à GraphQL.
* Ensuite, GraphQL les relie aux noms de schéma définis, qu'il s'agisse d'une map imbriquée de listes ou d'une map générique. GraphQL le fait tant que vous définissez le schéma approprié.
* Après avoir envoyé ces données à **ExecutionInput**, le moteur GraphQL analyse-> valide-> récupère-> exécute la requête et vous retourne une sortie JSON de la réponse en utilisant .toSpeci**fiation()

Lançons une requête en utilisant [GraphiQL](https://github.com/graphql/graphiql). Ajoutez cette extension à votre navigateur et définissez le point de terminaison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CKJMKjvUEv4B4j-zjvc6XA.png)

Regardez comment la forme de votre requête détermine la forme de la réponse. Le schéma peut être visualisé proprement grâce à la nature introspective de GraphQL. Cela permet la validation et la vérification de la syntaxe du schéma automatiquement grâce à l'arbre de syntaxe abstraite créé lors de l'analyse du schéma.

Ajoutons quelques champs supplémentaires dans le schéma. Nous allons construire un [Schema Definition Language](http://graphql-java.readthedocs.io/en/latest/schema.html). Créez un fichier nommé **magicSchool.graphql.**

```
type Query{magicSchool:MagicSchool}type MagicSchool{name: StringHeadMaster:Stringstudent:Student}type Student{name:Stringwand:Wandhouse:House}type House{name:Stringcolor:Stringpoints:Int}type Wand{name:Stringorigin:String}
```

Modifiez la source du schéma dans le code et vérifiez le nouveau schéma dans GraphiQL

```
File schemaFile = loadSchema("magicSchool.graphql");TypeDefinitionRegistry typeRegistry=schemaParser.parse(schemaFile);
```

Le runtimeWiring pour le schéma et les fetchers change considérablement pour inclure les autres types. Chaque type a son DataFetcher indépendant.

Ici, nous avons **@Autowired** tous les fetchers pour obtenir les données. Chaque type GraphQL est soutenu par un résolveur de type (data fetcher). Ces résolveurs sont indépendants les uns des autres et peuvent avoir différentes sources. Chaque DataFetcher ici a un **DatafetchingEnvironment**, qui est une interface vers l'exécution de la requête GraphQL. Il contient les **arguments de la requête**_,_ **contexte**_,_ **executionId**_,_ **paramètres spécifiques au champ,** et ainsi de suite_._

Jetez un œil à StudentFetcher et à la sortie de notre requête (ignorez les Extensions) :

```
public DataFetcher getData() {    return environment -> {        Map<String, Object> student = new HashMap<>();        if ("1".equalsIgnoreCase(environment.getArgument("id"))) {            student.put("name", "Harry Potter");        }        return student;    };}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*IHNWKg07X-IssEV5Ixefbw.png)
_Sortie GraphiQL_

Cela vous rappelle SQL, n'est-ce pas ? Voyez également comment **Underfetching** et **Overfetching** sont éliminés, et le contrôle des données est entièrement entre les mains du client. Maintenant, nous pouvons obtenir les informations de Harry et Ron proprement et en un seul appel au serveur !

### **Stratégie d'exécution GraphQL et instrumentation**

Chaque exécution de requête est asynchrone dans graphql-java. Lorsque vous appelez **build.execute(executionInput)**_,_ il retourne un objet [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html) qui se complète lorsque la requête termine son flux d'exécution.

De plus, comme les champs sont résolus séparément, dans l'exemple ci-dessus, les informations **Wand** et **House** sont récupérées et exécutées en parallèle. La stratégie d'exécution par défaut utilise le fork-join pool de Java, mais vous pouvez ajouter votre propre threadpool en utilisant la classe Executor.

```
ExecutorService executorService = new ThreadPoolExecutor(            128, /* taille du pool principal 128 threads */            256, /* taille maximale du pool 256 threads */            10, TimeUnit.SECONDS,            new LinkedBlockingQueue<Runnable>(),            new ThreadPoolExecutor.CallerRunsPolicy());    return GraphQL.newGraphQL()            .instrumentation(new TracingInstrumentation ())             .queryExecutionStrategy(new ExecutorServiceExecutionStrategy(executorService))            .build();}
```

graphql-java vous permet d'instrumenter l'exécution de la requête à chaque point : **beforeExecution**_,_ **beforeParsing**_,_ et **beforeFetching**_._ Vous pouvez étendre la classe **Instrumentation** et fournir votre propre action à chaque étape — par exemple, journaliser les requêtes et retourner le temps de chaque étape.

La sortie de l'instrumentation fournit une carte d'extensions au [format Apollo Tracing](https://www.apollographql.com/engine/) par défaut. Cela peut ensuite être utilisé par un certain client pour visualiser les données d'exécution (par exemple, en utilisant elastic-search et Grafana). Maintenant, vous savez ce que signifient les extensions dans l'image ci-dessus !

Le code complet de l'exemple ci-dessus peut être consulté [ici](https://github.com/prithvi10/GraphQL-Java-Spring).

### Conclusion

Il existe de nombreuses autres fonctionnalités dans graphql-java, comme [**Dataloader**](http://graphql-java.readthedocs.io/en/latest/batching.html) (qui résout le problème de récupération N+1), **directives** (qui facilitent l'écriture de schémas), et ainsi de suite. GraphQL est une technologie émergente qui facilite la vie du client et peut changer la manière dont nous faisons les choses sur Internet. C'est pourquoi de nombreuses entreprises comme Facebook, Twitter, GitHub et Coursera l'ont déjà adopté.

J'adorerais entendre vos commentaires sur GraphQL. N'hésitez pas à partager vos opinions. De plus, si vous aimez l'article de blog, n'oubliez pas d'applaudir.