---
title: Comment (dés)érialiser du JSON dans Akka HTTP avec spray-json
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T00:37:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-un-marshal-json-in-akka-http-with-spray-json-1407876373a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HS08mMqwO6HTlYIA_xtmVw.png
tags:
- name: api
  slug: api
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment (dés)érialiser du JSON dans Akka HTTP avec spray-json
seo_desc: 'By Miguel Lopez

  In the previous post, we added JSON support to our Akka HTTP API using circe.

  This time we’ll do the same but using spray-json. Akka HTTP supports it by providing
  an official library — we don’t need a third-party party one like we did...'
---

Par Miguel Lopez

Dans le [précédent article](https://www.codemunity.io/tutorials/akka-http-json-circe), nous avons ajouté la prise en charge du JSON à notre API Akka HTTP en utilisant circe.

Cette fois, nous ferons la même chose mais en utilisant spray-json. Akka HTTP le supporte en fournissant une bibliothèque officielle — nous n'avons pas besoin d'une bibliothèque tierce comme nous l'avons fait avec circe.

### Installation du projet

Nous allons suivre les mêmes étapes que dans le tutoriel précédent pour configurer le projet.

Clonez le [dépôt](https://github.com/Codemunity/akkahttp-quickstart), et vérifiez la branche `3.3-repository-implementation`.

Nous allons également apporter les modifications que nous avons faites dans le tutoriel précédent.

Tout d'abord, nous allons remplacer les dépendances circe par la dépendance spray-json puisque nous n'en aurons pas besoin pour ce tutoriel. Mettez à jour le fichier `build.sbt` avec le contenu suivant :

```
name := "akkahttp-quickstart"
version := "0.1"
scalaVersion := "2.12.6"
val akkaVersion = "2.5.13"
val akkaHttpVersion = "10.1.3"
libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % akkaVersion,
  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,
  "com.typesafe.akka" %% "akka-stream" % akkaVersion,
  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,
  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,
  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,
  "com.typesafe.akka" %% "akka-http-spray-json" % akkaHttpVersion,
  "org.scalatest" %% "scalatest" % "3.0.5" % Test
)
```

Ensuite, nous allons ajouter une fonction `save` au `TodoRepository` et son implémentation :

```
import scala.concurrent.{ExecutionContext, Future}
trait TodoRepository {
  def all(): Future[Seq[Todo]]
  def done(): Future[Seq[Todo]]
  def pending(): Future[Seq[Todo]]
  def save(todo: Todo): Future[Todo]}
class InMemoryTodoRepository(initialTodos: Seq[Todo] = Seq.empty)(implicit ec: ExecutionContext) extends TodoRepository {
  private var todos: Vector[Todo] = initialTodos.toVector
  override def all(): Future[Seq[Todo]] = Future.successful(todos)
  override def done(): Future[Seq[Todo]] = Future.successful(todos.filter(_.done))
  override def pending(): Future[Seq[Todo]] = Future.successful(todos.filterNot(_.done))
  override def save(todo: Todo): Future[Todo] = Future.successful {
    todos = todos :+ todo
    todo
  }
}
```

Cela nous permettra de créer une requête POST pour créer de nouvelles tâches.

Et enfin, mettez à jour l'objet `Main` pour créer une liste de tâches à des fins de test, et avec les routes appropriées :

```
import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.stream.ActorMaterializer
import scala.concurrent.Await
import scala.util.{Failure, Success}
object Main extends App {
  val host = "0.0.0.0"
  val port = 9000
  implicit val system: ActorSystem = ActorSystem(name = "todoapi")
  implicit val materializer: ActorMaterializer = ActorMaterializer()
  import system.dispatcher
  val todos = Seq(
    Todo("1", "Enregistrer des gifs incroyables pour les tutoriels", "", done = false),
    Todo("2", "Terminer le tutoriel spray-json", "", done = true),
  )
  val todoRepository = new InMemoryTodoRepository(todos)
  import akka.http.scaladsl.server.Directives._
  def route = path("todos") {
    get {
      complete(todoRepository.all())
    } ~ post {
      entity(as[Todo]) { todo =>
        complete(todoRepository.save(todo))
      }
    }
  }
  val binding = Http().bindAndHandle(route, host, port)
  binding.onComplete {
    case Success(_) => println("Succès !")
    case Failure(error) => println(s"Échec : ${error.getMessage}")
  }
  import scala.concurrent.duration._
  Await.result(binding, 3.seconds)
}
```

Avec cela en place, nous pouvons maintenant passer à la prise en charge de l'analyse JSON.

### Création du format

Le projet ne devrait pas compiler pour l'instant car Akka HTTP ne sait pas comment convertir le JSON en nos modèles et vice versa.

Ajouter la prise en charge du JSON avec circe était assez simple. Cela ne nécessitait que l'ajout de quelques instructions d'importation.

Malheureusement, avec spray-json, ce n'est pas le cas. L'effort n'est pas non plus si grand.

Alors, commençons.

Parce que nous voulons utiliser spray-json avec Akka HTTP, nous pouvons consulter la [documentation officielle d'Akka HTTP](https://doc.akka.io/docs/akka-http/current/common/json-support.html) pour savoir comment accomplir ce que nous voulons.

Nous devons étendre le trait `SprayJsonSupport` pour permettre à Akka HTTP de savoir comment analyser nos modèles vers et depuis JSON (via le `FromEntityUnmarshaller` et `ToEntityMarshaller` fournis par le trait).

Et pour créer le _format_ réel, nous utiliserons le trait `DefaultJsonProtocol` de spray-json.

Ajoutez l'objet suivant sous le modèle `Todo` :

```
object TodoFormat extends SprayJsonSupport with DefaultJsonProtocol {
  implicit val todoFormat = jsonFormat4(Todo)
}
```

C'est l'étape supplémentaire dont nous avons besoin lorsque nous utilisons spray-json. Cela doit être fait pour chaque modèle que nous avons.

Pour faire fonctionner notre projet, nous devons importer `TodoFormat` dans notre objet `Main` :

```
import TodoFormat._
import akka.http.scaladsl.server.Directives._
def route = path("todos") {
  get {
    complete(todoRepository.all())
  } ~ post {
    entity(as[Todo]) { todo =>
      complete(todoRepository.save(todo))
    }
  }
}
```

Exécutez l'application et elle devrait fonctionner correctement.

Faisons quelques tests !

### Test de notre API

Nous devons nous assurer que notre API fonctionne comme prévu. Alors, interrogeons-la comme nous l'avons fait dans le tutoriel précédent pour vérifier que la fonctionnalité est la même.

Envoyer une requête GET à `localhost:9000/todos` devrait nous donner les tâches initiales :

![Image](https://cdn-media-1.freecodecamp.org/images/97TXx4zg12xaNIhdDcxZys0figQgN06hFTdI)

Super, cela fonctionne de la même manière.

Voyons si l'envoi d'un JSON invalide nous donne quelque chose de similaire :

![Image](https://cdn-media-1.freecodecamp.org/images/SeH1uiH0xzKy12LYxYIglHDS8TmWIlZ8kifl)

C'est le cas. Le message d'erreur est différent, mais nous obtenons le même `400 Bad Request`, ce qui est la partie importante.

Créons une nouvelle tâche avec un JSON valide :

![Image](https://cdn-media-1.freecodecamp.org/images/o3ItlFqvXdih41ioeLPP7p9VI1F3ZpXu23fm)

Et pour terminer, interrogeons à nouveau les tâches pour nous assurer qu'elle a été enregistrée :

![Image](https://cdn-media-1.freecodecamp.org/images/q9BNV8IqdeXQ-FMBp1q6rtaD9Ef9M2sZKVbG)

Nous y voilà. Nous avons une application fonctionnelle avec spray-json.

Cool, n'est-ce pas ?

### Conclusion

Même si travailler avec spray-json implique un peu plus de travail manuel, vous n'avez pas besoin d'une dépendance tierce supplémentaire pour le faire fonctionner avec Akka HTTP.

C'est vraiment une question de préférence.

À l'avenir, nous explorerons comment accomplir différents cas d'utilisation avec les deux pour les comparer. Alors, restez à l'écoute !

Si vous avez aimé ce tutoriel et que vous souhaitez apprendre à créer une API pour une application de tâches, consultez notre nouveau cours **gratuit** ! 🎉

[**Akka HTTP Quickstart**](http://link.codemunity.io/website-akka-http-quickstart)
[_Apprenez à créer des applications web et des API avec Akka HTTP dans ce cours gratuit !_link.codemunity.io](http://link.codemunity.io/website-akka-http-quickstart)

_Publié à l'origine sur [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-spray-json/)._