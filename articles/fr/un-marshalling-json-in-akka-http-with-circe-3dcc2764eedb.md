---
title: Comment (dés)érialiser du JSON dans Akka HTTP avec Circe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T08:38:53.000Z'
originalURL: https://freecodecamp.org/news/un-marshalling-json-in-akka-http-with-circe-3dcc2764eedb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RtFazsYIcVhn1w1cr4CyeQ.png
tags:
- name: api
  slug: api
- name: json
  slug: json
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment (dés)érialiser du JSON dans Akka HTTP avec Circe
seo_desc: 'By Miguel Lopez

  Even though the usual library to (un)marshal JSON in Akka HTTP applications is spray-json,
  I decided to give circe a try. I use it in the Akka HTTP beginners course I’m working
  on. cough it’s free ? c**_ough_**

  In this post I’d like t...'
---

Par Miguel Lopez

Bien que la bibliothèque habituelle pour (dés)érialiser du JSON dans les applications Akka HTTP soit spray-json, j'ai décidé d'essayer circe. Je l'utilise dans le cours pour débutants sur Akka HTTP sur lequel je travaille. ***_toux_*** [il est gratuit](http://link.codemunity.io/circe-akka-http-quickstart-course) ? *c**_toux_***

Dans cet article, je voudrais vous montrer pourquoi je l'ai essayé.

Pour utiliser circe avec Akka HTTP — et d'autres bibliothèques JSON d'ailleurs — nous devons créer les marshalers et unmarshalers manuellement. Heureusement, il existe une [bibliothèque supplémentaire](https://github.com/hseeberger/akka-http-json) qui le fait déjà pour nous.

### Installation et vue d'ensemble du projet

Clonez le [dépôt du projet](https://github.com/Codemunity/akkahttp-quickstart), et basculez sur la branche `3.3-repository-implementation`.

Sous `src/main/scala`, vous trouverez les fichiers suivants :

```
$ tree srcsrc main     scala         Main.scala         Todo.scala         TodoRepository.scala2 directories, 3 files
```

L'objet `Main` est le point d'entrée de l'application. Jusqu'à présent, il a une route hello world et la lie à un hôte et une route donnés.

`Todo` est le modèle de notre application. Et le `TodoRepository` est responsable de la persistance et de l'accès aux todos. Jusqu'à présent, il n'a qu'une implémentation en mémoire pour garder les choses simples et ciblées.

### Lister tous les todos

Nous allons modifier la route de l'objet `Main` pour lister tous les todos dans un dépôt. Nous ajouterons également quelques todos initiaux pour les tests :

```
import akka.actor.ActorSystemimport akka.http.scaladsl.Httpimport akka.stream.ActorMaterializerimport scala.concurrent.Awaitimport scala.util.{Failure, Success}object Main extends App {  val host = "0.0.0.0"  val port = 9000  implicit val system: ActorSystem = ActorSystem(name = "todoapi")  implicit val materializer: ActorMaterializer = ActorMaterializer()  import system.dispatcher  val todos = Seq(    Todo("1", "Nettoyer la maison", "", done = false),    Todo("2", "Apprendre Scala", "", done = true),  )  val todoRepository = new InMemoryTodoRepository(todos)  import akka.http.scaladsl.server.Directives._  def route = path("todos") {    get {      complete(todoRepository.all())    }  }  val binding = Http().bindAndHandle(route, host, port)  binding.onComplete {    case Success(_) => println("Succès !")    case Failure(error) => println(s"Échec : ${error.getMessage}")  }  import scala.concurrent.duration._  Await.result(binding, 3.seconds)}
```

Maintenant, nous écoutons les requêtes sous `/todos` et nous répondons avec tous les todos que nous avons dans notre `todoRepository`.

Cependant, si nous essayons de l'exécuter, cela ne compilera pas :

```
Error:(26, 34) type mismatch; found   : scala.concurrent.Future[Seq[Todo]] required: akka.http.scaladsl.marshalling.ToResponseMarshallable      complete(todoRepository.all())
```

L'erreur de compilation nous indique qu'il ne sait pas comment marshaler nos todos en JSON.

Nous devons importer circe et la bibliothèque de support :

```
import akka.http.scaladsl.server.Directives._import de.heikoseeberger.akkahttpcirce.FailFastCirceSupport._import io.circe.generic.auto._def route = path("todos") {  get {    complete(todoRepository.all())  }}
```

Avec ces deux lignes supplémentaires, nous pouvons maintenant exécuter notre objet `Main` et tester notre nouvelle route.

Faites une requête GET à `http://localhost:9000/todos` :

![Image](https://cdn-media-1.freecodecamp.org/images/xuRxZ8giASz62AEFcSr0SZRIVRlXXOEoMZqL)

Et nous obtenons nos todos en retour ! ?

### Créer des todos

Il s'avère que la désérialisation de JSON dans nos modèles ne demande pas beaucoup d'efforts non plus. Mais notre `TodoRepository` ne supporte pas encore l'enregistrement des todos. Ajoutons d'abord cette fonctionnalité :

```
import scala.concurrent.{ExecutionContext, Future}trait TodoRepository {  def all(): Future[Seq[Todo]]  def done(): Future[Seq[Todo]]  def pending(): Future[Seq[Todo]]  def save(todo: Todo): Future[Todo]}class InMemoryTodoRepository(initialTodos: Seq[Todo] = Seq.empty)(implicit ec: ExecutionContext) extends TodoRepository {  private var todos: Vector[Todo] = initialTodos.toVector  override def all(): Future[Seq[Todo]] = Future.successful(todos)  override def done(): Future[Seq[Todo]] = Future.successful(todos.filter(_.done))  override def pending(): Future[Seq[Todo]] = Future.successful(todos.filterNot(_.done))  override def save(todo: Todo): Future[Todo] = Future.successful {    todos = todos :+ todo    todo  }}
```

Nous avons ajouté une méthode `save` au trait et à l'implémentation. Comme nous utilisons un `Vector`, notre implémentation de `save` stockera des todos en double. Cela convient pour les besoins de ce tutoriel.

Ajoutons une nouvelle route qui écoutera les requêtes POST. Cette route reçoit un `Todo` comme corps de la requête et l'enregistre dans notre dépôt :

```
def route = path("todos") {  get {    complete(todoRepository.all())  } ~ post {    entity(as[Todo]) { todo =>      complete(todoRepository.save(todo))    }  }}
```

En utilisant la directive `entity`, nous pouvons construire une route qui analyse automatiquement le JSON entrant vers notre modèle. Elle rejette également les requêtes avec un JSON invalide :

![Image](https://cdn-media-1.freecodecamp.org/images/ew2sqvGf4H8BuBFuDM5iVG-RQsHTV5DVd9yx)

Nous avons envoyé le champ `done` comme une chaîne, alors qu'il aurait dû être un booléen, ce à quoi notre API a répondu par une mauvaise requête.

Faisons une requête valide pour créer un nouveau todo :

![Image](https://cdn-media-1.freecodecamp.org/images/qqLEGI-7ia2pcDesaClXCoTW7D21h5DOC7v1)

Cette fois, nous avons envoyé la propriété comme `done := false`, ce qui indique à HTTPie d'envoyer la valeur comme `Boolean` au lieu de `String`.

Nous obtenons notre todo en retour et un code de statut 200, ce qui signifie que tout s'est bien passé. Nous pouvons confirmer que cela a fonctionné en interrogeant à nouveau les todos :

![Image](https://cdn-media-1.freecodecamp.org/images/bHQixnuljInXUXX7QaKPjX6JfX-9rm-Yxtln)

Nous obtenons trois todos, ceux codés en dur et le nouveau que nous avons créé.

### Conclusion

Nous avons ajouté la sérialisation et la désérialisation JSON à notre application en ajoutant les dépendances (c'était déjà fait dans le projet) et en important les deux bibliothèques.

Circe comprend comment gérer nos modèles sans beaucoup d'intervention de notre part.

Dans un prochain article, nous explorerons comment accomplir la même fonctionnalité avec spray-json à la place.

Restez à l'écoute !

Si vous avez aimé ce tutoriel et que vous souhaitez apprendre à construire une API pour une application de todos, consultez notre nouveau cours **gratuit** ! ???

[**Akka HTTP Quickstart**](http://link.codemunity.io/circe-akka-http-quickstart-course)  
[_Apprenez à créer des applications web et des API avec Akka HTTP dans ce cours gratuit !_link.codemunity.io](http://link.codemunity.io/circe-akka-http-quickstart-course)

_Publié à l'origine sur [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-json-circe/)._