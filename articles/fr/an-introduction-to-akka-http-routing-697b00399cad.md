---
title: Une introduction au routage Akka HTTP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T19:17:41.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-akka-http-routing-697b00399cad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SLnwW0f177L3NOX0V88Z0g.png
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
seo_title: Une introduction au routage Akka HTTP
seo_desc: 'By Miguel Lopez

  Akka HTTP’s routing DSL might seem complicated at first, but once you get the hang
  of it you’ll see how powerful it is.

  In this tutorial we will focus on creating routes and their structure. We won’t
  cover parsing to and from JSON, we...'
---

Par Miguel Lopez

Le DSL de routage d'Akka HTTP peut sembler compliqué au premier abord, mais une fois que vous aurez compris, vous verrez à quel point il est puissant.

Dans ce tutoriel, nous nous concentrerons sur la création de routes et leur structure. Nous n'aborderons pas l'analyse vers et depuis JSON, nous avons [d'autres tutoriels](https://www.codemunity.io/tutorials/akka-http-json-circe/) qui couvrent ce sujet.

### Qu'est-ce que les directives ?

L'un des premiers concepts que nous rencontrerons lors de l'apprentissage d'Akka HTTP côté serveur (il existe également une bibliothèque côté client) est celui des _directives_.

Alors, qu'est-ce que c'est ?

Vous pouvez les considérer comme des blocs de construction, des pièces Lego si vous voulez, que vous pouvez utiliser pour construire vos routes. Elles sont composables, ce qui signifie que nous pouvons créer des directives sur la base d'autres directives.

Si vous souhaitez une lecture plus approfondie, n'hésitez pas à consulter [la documentation officielle d'Akka HTTP](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html).

Avant de continuer, discutons de ce que nous allons construire.

### API de type blog

Nous allons créer un exemple d'API publique pour un blog, où nous permettrons aux utilisateurs de :

* interroger une liste de tutoriels
* interroger un tutoriel unique par ID
* interroger la liste des commentaires dans un tutoriel
* ajouter des commentaires à un tutoriel

Les points de terminaison seront :

```
- Lister tous les tutoriels GET /tutorials 
```

```
- Créer un tutoriel GET /tutorials/:id 
```

```
- Obtenir tous les commentaires d'un tutoriel GET /tutorials/:id/comments 
```

```
- Ajouter un commentaire à un tutoriel POST /tutorials/:id/comments
```

Nous ne mettrons en œuvre que les points de terminaison, sans logique. De cette façon, nous apprendrons à créer cette structure et les pièges courants lors du démarrage avec Akka HTTP.

### Configuration du projet

Nous avons créé un [dépôt](https://github.com/Codemunity/akka-http-routing-primer) pour ce tutoriel, dans lequel vous trouverez une branche pour chaque section nécessitant du codage. N'hésitez pas à le cloner et à l'utiliser comme projet de base ou même à changer de branche pour voir les différences.

Sinon, créez un nouveau projet SBT, puis ajoutez les dépendances dans le fichier `build.sbt` :

```
name := "akkahttp-routing-dsl" 
```

```
version := "0.1" 
```

```
scalaVersion := "2.12.7" 
```

```
val akkaVersion = "2.5.17" val akkaHttpVersion = "10.1.5" 
```

```
libraryDependencies ++= Seq(   "com.typesafe.akka" %% "akka-actor" % akkaVersion,   "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,  "com.typesafe.akka" %% "akka-stream" % akkaVersion,   "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,   "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,   "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,      "org.scalatest" %% "scalatest" % "3.0.5" % Test )
```

Nous avons ajouté Akka HTTP et ses dépendances, Akka Actor et Streams. Et nous utiliserons également Scalatest pour les tests.

### Lister tous les tutoriels

Nous adopterons une approche TDD pour construire notre hiérarchie de directives, en créant d'abord les tests pour nous assurer de ne pas casser nos routes lors de l'ajout d'autres. Adopter cette approche est très utile lorsque l'on commence avec Akka HTTP.

Commençons par notre route pour lister tous les tutoriels. Créez un nouveau fichier sous `src/test/scala` (si les dossiers n'existent pas, créez-les) nommé `RouterSpec` :

```
import akka.http.scaladsl.testkit.ScalatestRouteTest import org.scalatest.{Matchers, WordSpec} 
```

```
class RouterSpec extends WordSpec with Matchers with ScalatestRouteTest { 
```

```
}
```

`WordSpec` et `Matchers` sont fournis par Scalatest, et nous les utiliserons pour structurer nos tests et assertions. `ScalatestRouteTest` est un trait fourni par le kit de test d'Akka HTTP, il nous permettra de tester nos routes de manière pratique. Voyons comment nous pouvons y parvenir.

Puisque nous utilisons [Scalatest's WordSpec](http://www.scalatest.org/at_a_glance/WordSpec), nous commencerons par créer une portée pour notre objet `Router` que nous créerons bientôt et le premier test :

```
"A Router" should {   "list all tutorials" in {   } }
```

Ensuite, nous voulons nous assurer de pouvoir envoyer une requête GET au chemin `/tutorials` et obtenir la réponse attendue, voyons comment nous pouvons y parvenir :

```
Get("/tutorials") ~> Router.route ~> check {   status shouldBe StatusCodes.OK   responseAs[String] shouldBe "all tutorials" }
```

Cela ne compilera même pas car nous n'avons pas créé notre objet `Router`. Faisons cela maintenant.

Créez un nouvel objet Scala sous `src/main/scala` nommé `Router`. Dans celui-ci, nous créerons une méthode qui retournera une `Route` :

```
import akka.http.scaladsl.server.Route 
```

```
object Router {
```

```
  def route: Route = ???
```

```
}
```

Ne vous inquiétez pas trop pour le `???`, c'est juste un espace réservé pour éviter les erreurs de compilation temporairement. Cependant, si ce code est exécuté, il lancera une `NotImplementedError` comme nous le verrons bientôt.

Maintenant que nos tests et notre projet compilent, exécutons les tests (clic droit sur la spécification et "Exécuter 'RouterSpec'").

Le test a échoué avec l'exception attendue, nous n'avons pas implémenté nos routes. Commençons !

### Création de la route de liste

En consultant [la documentation officielle](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html#composing-directives), nous voyons que la route commence par la directive `path`. Imions ce qu'ils font et construisons notre route :

```
import akka.http.scaladsl.server.{Directives, Route}
```

```
object Router extends Directives {
```

```
  def route: Route = path("tutorials") {    get {      complete("all tutorials")    }  }}
```

Cela semble raisonnable, exécutons notre spécification. Et cela passe, super !

Pour référence, notre `RouterSpec` complet ressemble maintenant à :

```
import akka.http.scaladsl.model.StatusCodesimport akka.http.scaladsl.testkit.ScalatestRouteTestimport org.scalatest.{Matchers, WordSpec}class RouterSpec extends WordSpec with Matchers with ScalatestRouteTest {  "A Router" should {    "list all tutorials" in {      Get("/tutorials") ~> Router.route ~> check {        status shouldBe StatusCodes.OK        responseAs[String] shouldBe "all tutorials"      }    }  }}
```

### Obtenir un tutoriel unique par ID

Ensuite, nous permettrons à nos utilisateurs de récupérer un tutoriel unique.

Ajoutons un test pour notre nouvelle route :

```
"return a single tutorial by id" in {  Get("/tutorials/hello-world") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "tutorial hello-world"  }}
```

Nous nous attendons à recevoir un message qui inclut l'ID du tutoriel.

Le test échouera car nous n'avons pas créé notre route, faisons cela maintenant.

À partir de la même [ressource](https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/index.html#composing-directives) que nous avons utilisée précédemment pour baser notre route, nous pouvons voir comment nous pouvons placer plusieurs directives au même niveau dans la hiérarchie en utilisant la directive `~`.

Nous devrons imbriquer les directives `path` car nous avons besoin d'un autre segment après la route `/tutorials` pour l'ID du tutoriel. Dans la documentation, ils utilisent `IntNumber` pour extraire un nombre du chemin, mais nous utiliserons une chaîne et pour cela, nous pouvons utiliser `Segment` à la place.

Notre route ressemble à :

```
def route: Route = path("tutorials") {  get {    complete("all tutorials")  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Exécutons les tests. Et vous devriez obtenir une erreur similaire :

```
Request was rejectedScalaTestFailureLocation: RouterSpec at (RouterSpec.scala:17)org.scalatest.exceptions.TestFailedException: Request was rejected
```

Qu'est-ce qui se passe ?!

Eh bien, une requête est rejetée lorsqu'elle ne correspond pas à notre hiérarchie de directives. C'est l'une des choses qui m'a posé problème au début.

Maintenant est probablement le bon moment pour examiner comment ces directives correspondent à la requête entrante lorsqu'elle traverse la hiérarchie.

Différentes directives correspondront à différents aspects d'une requête entrante, nous avons vu `path` et `get`, l'une correspond à l'URL de la requête et l'autre à la méthode. Si une requête correspond à une directive, elle entrera à l'intérieur, sinon elle passera à la suivante. Cela nous indique également que l'ordre compte. Si elle ne correspond à aucune directive, la requête est rejetée.

Maintenant que nous savons que notre requête ne correspond pas à nos directives, commençons à examiner pourquoi.

Si nous consultons la documentation pour la directive `path` (Cmd + Clic sur Mac), nous trouverons :

```
/** * Applies the given [[PathMatcher]] to the remaining unmatched path after consuming a leading slash. * The matcher has to match the remaining path completely. * If matched the value extracted by the [[PathMatcher]] is extracted on the directive level. * * @group path */
```

Ainsi, la directive `path` doit correspondre exactement au chemin, ce qui signifie que notre première directive `path` ne correspondra qu'à `/tutorials` et jamais à `/tutorials/:id`.

Dans le même trait `PathDirectives` qui contient la directive `path`, nous pouvons voir une autre directive nommée `pathPrefix` :

```
/** * Applies the given [[PathMatcher]] to a prefix of the remaining unmatched path after consuming a leading slash. * The matcher has to match a prefix of the remaining path. * If matched the value extracted by the PathMatcher is extracted on the directive level. * * @group path */
```

`pathPrefix` ne correspond qu'à un préfixe et le supprime. Cela semble être ce que nous cherchons, mettons à jour nos routes :

```
def route: Route = pathPrefix("tutorials") {  get {    complete("all tutorials")  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Exécutons les tests, et... nous obtenons une autre erreur. ?

```
"[all tutorials]" was not equal to "[tutorial hello-world]"ScalaTestFailureLocation: RouterSpec at (RouterSpec.scala:18)Expected :"[tutorial hello-world]"Actual   :"[all tutorials]"
```

Il semble que notre requête a correspondu à la première directive `get`. Elle correspond maintenant à `pathPrefix`, et parce qu'il s'agit également d'une requête GET, elle correspondra à la première directive `get`. L'ordre compte.

Il y a plusieurs choses que nous pouvons faire. La solution la plus simple serait de déplacer la première requête `get` à la fin de la hiérarchie, cependant, nous devrions nous en souvenir ou le documenter. Pas idéal.

Personnellement, je préfère éviter de telles solutions et rendre l'intention claire à travers le code. Si nous regardons dans le trait `PathDirectives` de tout à l'heure, nous trouverons une directive appelée `pathEnd` :

```
/** * Rejects the request if the unmatchedPath of the [[RequestContext]] is non-empty, * or said differently: only passes on the request to its inner route if the request path * has been matched completely. * * @group path */
```

C'est exactement ce que nous voulons, alors enveloppons notre première directive `get` avec `pathEnd` :

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ path(Segment) { id =>    get {      complete(s"tutorial $id")    }  }}
```

Exécutons les tests à nouveau, et... enfin, les tests passent ! ?

### Lister tous les commentaires d'un tutoriel

Mettons en pratique ce que nous avons appris sur l'imbrication des routes en allant un peu plus loin.

D'abord le test :

```
"list all comments of a given tutorial" in {  Get("/tutorials/hello-world/comments") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "comments for the hello-world tutorial"  }}
```

C'est un cas similaire à celui d'avant : nous savons que nous devrons placer une route à côté d'une autre, ce qui signifie que nous devons :

* changer le `path(Segmenter)` en `pathPrefix(Segmenter)`
* envelopper le premier `get` avec la directive `pathEnd`
* placer la nouvelle route à côté du `pathEnd`

Nos routes finissent par ressembler à :

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ pathPrefix(Segment) { id =>    pathEnd {      get {        complete(s"tutorial $id")      }    } ~ path("comments") {      get {        complete(s"comments for the $id tutorial")      }    }  }}
```

Exécutons les tests, et ils devraient passer ! ?

### Ajouter des commentaires à un tutoriel

Notre dernier point de terminaison est similaire au précédent, mais il correspondra aux requêtes POST. Nous utiliserons cet exemple pour voir la différence entre la mise en œuvre et le test d'une requête GET et d'une requête POST.

Le test :

```
"add comments to a tutorial" in {  Post("/tutorials/hello-world/comments", "new comment") ~> Router.route ~> check {    status shouldBe StatusCodes.OK    responseAs[String] shouldBe "added the comment 'new comment' to the hello-world tutorial"  }}
```

Nous utilisons la méthode `Post` au lieu du `Get` que nous avons utilisé, et nous lui donnons un paramètre supplémentaire qui est le corps de la requête. Le reste nous est familier maintenant.

Pour implémenter notre dernière route, nous pouvons nous référer à [la documentation](https://doc.akka.io/docs/akka-http/current/routing-dsl/index.html#longer-example) et voir comment cela se fait habituellement.

Nous avons une directive `post` tout comme nous avons une directive `get`. Pour extraire le corps de la requête, nous avons besoin de deux directives, `entity` et `as`, auxquelles nous fournissons le type que nous attendons. Dans notre cas, c'est une chaîne.

Essayons cela :

```
post {  entity(as[String]) { comment =>    complete(s"added the comment '$comment' to the $id tutorial")  }}
```

Cela semble raisonnable. Nous extrayons le corps de la requête sous forme de chaîne et l'utilisons dans notre réponse. Ajoutons cela à notre méthode `route` à côté de la route précédente sur laquelle nous avons travaillé :

```
def route: Route = pathPrefix("tutorials") {  pathEnd {    get {      complete("all tutorials")    }  } ~ pathPrefix(Segment) { id =>    pathEnd {      get {        complete(s"tutorial $id")      }    } ~ path("comments") {      get {        complete(s"comments for the $id tutorial")      } ~ post {        entity(as[String]) { comment =>          complete(s"added the comment '$comment' to the $id tutorial")        }      }    }  }}
```

*Si vous souhaitez apprendre à analyser des classes Scala vers et depuis JSON [nous avons des tutoriels pour cela également](https://www.codemunity.io/tutorials/akka-http-json-circe/).*

Exécutez les tests, et ils devraient tous passer.

### Conclusion

Le DSL de routage d'Akka HTTP peut sembler déroutant au premier abord, mais après avoir surmonté quelques obstacles, cela devient clair. Après un certain temps, cela deviendra naturel et peut être très puissant.

Nous avons appris à structurer nos routes, mais plus important encore, nous avons appris à créer cette structure guidée par des tests qui nous assureront de ne pas les casser à un moment donné dans le futur.

Même si nous n'avons travaillé que sur quatre points de terminaison, nous avons abouti à une structure quelque peu compliquée et profonde. Restez à l'écoute et nous explorerons différentes façons de simplifier nos routes et de les rendre plus gérables !

[Apprenez à construire des API REST avec Scala et Akka HTTP avec ce cours gratuit étape par étape !](http://link.codemunity.io/website-akka-http-quickstart)

*Initialement publié sur [www.codemunity.io](https://www.codemunity.io/tutorials/akka-http-routing-primer/).*