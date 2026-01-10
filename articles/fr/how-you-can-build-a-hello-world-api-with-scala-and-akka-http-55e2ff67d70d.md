---
title: Comment créer une API Hello World avec Scala et Akka HTTP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T16:27:50.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-build-a-hello-world-api-with-scala-and-akka-http-55e2ff67d70d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: Akka
  slug: akka
- name: api
  slug: api
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une API Hello World avec Scala et Akka HTTP
seo_desc: 'By Miguel Lopez

  Yes, it’s still a thing.


  _Photo by [Unsplash](https://unsplash.com/photos/B3l0g6HLxr8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Blake Connally on <a href="https://unsp...'
---

Par Miguel Lopez

#### _Oui, c'est toujours d'actualité._

![Image](https://cdn-media-1.freecodecamp.org/images/ws5H0lYzh1Kol7Aum0Up1pW9eiDRpXHoKkcT)
_Photo par [Unsplash](https://unsplash.com/photos/B3l0g6HLxr8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Blake Connally</a> sur <a href="https://unsplash.com/search/photos/code?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Akka est un outil populaire basé sur les acteurs pour construire des applications concurrentes et distribuées dans la JVM. Ces applications utilisent principalement Scala ou Java.

Il dispose de plusieurs modules qui aident à construire de telles applications, et Akka HTTP en fait partie.

Akka HTTP dispose d'utilitaires côté client et côté serveur. Nous nous concentrerons sur le serveur dans ce tutoriel.

Vous devriez être familier avec Scala, et vous devriez avoir SBT et IntelliJ configurés et installés. Si ce n'est pas le cas, consultez la [documentation officielle](https://docs.scala-lang.org/getting-started-intellij-track/getting-started-with-scala-in-intellij.html).

Sans plus attendre, construisons une API hello world en utilisant Scala et Akka HTTP !

### Installation du projet

N'hésitez pas à cloner le [dépôt](https://github.com/Codemunity/akkahttp-quickstart), assurez-vous d'utiliser la branche `2.1-review-project`.

Sinon, nous utiliserons sbt `1.1.6` et Scala `2.12.6`. Vérifiez vos fichiers `build.properties` et `build.sbt` pour vous assurer que les versions correspondent à celles-ci.

Commençons par ajouter les dépendances requises. Comme Akka HTTP dépend des acteurs et des flux, nous devrons également ajouter ces bibliothèques.

Ajoutez le snippet suivant à la fin de votre fichier `build.sbt` :

```
libraryDependencies ++= Seq(  "com.typesafe.akka" %% "akka-actor" % "2.5.13",  "com.typesafe.akka" %% "akka-stream" % "2.5.13",  "com.typesafe.akka" %% "akka-http" % "10.1.3",)
```

Si vous êtes invité à activer l'auto-import, faites-le. Sinon, vous pouvez ouvrir un terminal et vous déplacer dans le répertoire racine de votre projet. Ensuite, exécutez `sbt update` pour obtenir les dépendances.

L'auto-import veillera à mettre à jour votre projet chaque fois que certains fichiers sont mis à jour, y compris le fichier `build.sbt`.

### Instancier les dépendances

Créons un objet Scala sous "src/main/scala" nommé `Server`. Nous commencerons par instancier les dépendances requises pour créer un serveur avec Akka HTTP.

Tout d'abord, l'objet étendra le trait `App` :

```
object Server extends App {}
```

Cela permettra à notre objet `Server` d'être exécutable.

Nous aurons besoin d'un hôte et d'un port pour lier le serveur, alors ajoutons-les maintenant :

```
val host = "0.0.0.0"val port = 9000
```

Parce qu'Akka HTTP utilise des acteurs et des flux Akka en dessous, nous devrons également fournir leurs dépendances :

```
implicit val system: ActorSystem = ActorSystem("helloworld")implicit val executor: ExecutionContext = system.dispatcherimplicit val materializer: ActorMaterializer = ActorMaterializer()
```

Même si vous n'avez pas besoin de savoir ce qu'ils font pour commencer à développer des applications Akka HTTP, il est toujours bon d'être conscient de leur utilité.

Un `ActorSystem` est utilisé pour gérer les acteurs. Il est utilisé pour les créer et les rechercher. Les acteurs du même système partagent généralement la même configuration.

Le `ExecutionContext` est responsable de l'exécution des `Future`. Il sait où et comment il doit les exécuter, par exemple dans un pool de threads.

Et enfin, un `ActorMaterializer` est responsable de l'exécution des flux.

Avec cela fait, nous pouvons créer notre route hello !

### Créer la route

Pour créer notre route, nous utiliserons le DSL de routage d'Akka HTTP. Il est basé sur des "couches" de ce qu'on appelle une directive. Pour un aperçu, n'hésitez pas à parcourir leur [documentation officielle](https://doc.akka.io/docs/akka-http/current/routing-dsl/overview.html).

Ajoutez la route sous les dépendances :

```
def route = path("hello") {  get {    complete("Hello, World!")  }}
```

Nous avons une première couche, où nous essayons de faire correspondre le chemin de la requête entrante à "/hello". Si cela ne correspond pas, cela sera rejeté.

Si cela correspond, cela essaiera de faire correspondre les "[directives](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html)" internes. Dans notre cas, nous faisons correspondre les requêtes GET. Nous complétons le cycle requête/réponse avec un message "Hello, World".

### Démarrer le serveur

Avec notre route créée, tout ce que nous avons à faire est de démarrer le serveur :

```
Http().bindAndHandle(route, host, port)
```

Nous lions notre route à l'hôte et au port donnés en utilisant l'objet `Http` d'Akka HTTP.

Pour exécuter notre objet `Server`, vous pouvez faire un clic droit dessus et cliquer sur _Run 'Server'_.

Donnez-lui quelques secondes pour compiler, puis allez dans un navigateur. Accédez à `http://localhost:9000/hello` et vous devriez voir notre message "Hello, World !".

![Image](https://cdn-media-1.freecodecamp.org/images/EZYjgm5uULRp-qqC1upw4Q8kGcDad7q4BeXN)

Cool, n'est-ce pas ?

### Journalisation

Avant de conclure ce tutoriel, nous ajouterons une journalisation de base à notre serveur.

Vous avez peut-être remarqué qu'il n'y avait aucun retour lorsque nous avons exécuté notre objet `Server`. Nous n'avons aucune idée de savoir s'il a réussi ou échoué.

Nous pouvons seulement supposer qu'il a fonctionné parce que l'application n'a pas planté.

Ajoutons un peu de journalisation.

Si vous regardez la fonction `bindAndHandle` de l'objet `Http`, elle retourne un futur de `ServerBinding`. Nous pouvons accrocher quelques logs à la fonction `onComplete` du futur.

Faisons cela :

```
val bindingFuture = Http().bindAndHandle(route, host, port)bindingFuture.onComplete {  case Success(serverBinding) => println(s"écoute sur ${serverBinding.localAddress}")  case Failure(error) => println(s"erreur : ${error.getMessage}")}
```

Exécutez à nouveau le `Server`, et cette fois vous devriez voir :

```
écoute sur /0:0:0:0:0:0:0:0:9000
```

### Conclusion

Bien que l'utilisation de Scala et Akka HTTP ne soit pas la manière la plus rapide de développer des APIs, elle permet d'intégrer d'autres modules Akka, tels que les acteurs, les flux, les clusters, et plus encore, rendant plus facile le développement de systèmes résilients et scalables.

Cela dit, il est bon de garder à l'esprit que le développement d'une application utilisant Scala et/ou Akka ne signifie pas nécessairement qu'elle sera résiliente et scalable. Vous devrez toujours effectuer un travail pour y parvenir, mais c'est plus facile qu'avec d'autres technologies.

Si vous avez aimé Akka HTTP, nous avons un cours gratuit qui vous permettra de démarrer rapidement dans le développement d'APIs avec celui-ci. Vous construirez une API pour une application Todo, expliquée étape par étape. Allez-y ! 🚀

[**Akka HTTP Quickstart**](http://link.codemunity.io/hw-akka-http-quickstart-course)
[_Apprenez à créer des applications web et des APIs avec Akka HTTP dans ce cours gratuit !_link.codemunity.io](http://link.codemunity.io/hw-akka-http-quickstart-course)