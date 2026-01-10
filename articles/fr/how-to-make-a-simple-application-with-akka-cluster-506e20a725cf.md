---
title: Comment créer une application simple avec Akka Cluster
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T21:08:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-simple-application-with-akka-cluster-506e20a725cf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kbflVM9_tfKyfVOR1ldKAw.jpeg
tags:
- name: Akka
  slug: akka
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
seo_title: Comment créer une application simple avec Akka Cluster
seo_desc: 'By Luca Florio

  If you read my previous story about Scalachain, you probably noticed that it is
  far from being a distributed system. It lacks all the features to properly work
  with other nodes. Add to it that a blockchain composed by a single node is ...'
---

Par Luca Florio

Si vous avez lu mon histoire précédente sur [Scalachain](https://github.com/elleFlorio/scalachain), vous avez probablement remarqué qu'il est loin d'être un système distribué. Il manque toutes les fonctionnalités pour fonctionner correctement avec d'autres nœuds. Ajoutez à cela qu'une blockchain composée d'un seul nœud est inutile. Pour cette raison, j'ai décidé qu'il était temps de travailler sur le problème.

Puisque Scalachain est alimenté par Akka, pourquoi ne pas profiter de l'occasion pour jouer avec Akka Cluster ? J'ai créé un [projet simple](https://github.com/elleFlorio/akka-cluster-playground) pour bricoler un peu avec [Akka Cluster](https://doc.akka.io/docs/akka/2.5/index-cluster.html), et dans cette histoire, je vais partager mes apprentissages. Nous allons créer un cluster de trois nœuds, en utilisant [Cluster Aware Routers](https://doc.akka.io/docs/akka/2.5/cluster-routing.html#weakly-up) pour équilibrer la charge entre eux. Tout fonctionnera dans un conteneur Docker, et nous utiliserons docker-compose pour un déploiement facile.

D'accord, c'est parti ! ?

#### Introduction rapide à Akka Cluster

Akka Cluster offre un excellent support pour la création d'applications distribuées. Le meilleur cas d'utilisation est lorsque vous avez un nœud que vous souhaitez répliquer N fois dans un environnement distribué. Cela signifie que tous les N nœuds sont des pairs exécutant le même code. Akka Cluster vous offre la découverte des membres du même cluster. En utilisant Cluster Aware Routers, il est possible d'équilibrer les messages entre les acteurs de différents nœuds. Il est également possible de choisir la politique d'équilibrage, rendant l'équilibrage de charge un jeu d'enfant !

En fait, vous pouvez choisir entre deux types de routeurs :

**Group Router** — Les acteurs auxquels envoyer les messages — appelés routees — sont spécifiés en utilisant leur chemin d'acteur. Les routeurs partagent les routees créés dans le cluster. Nous utiliserons un Group Router dans cet exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aRVBb-_v2dBpTV8m97Pd3w.png)
_Group Router_

**Pool Router** — Les routees sont créés et déployés par le routeur, donc ils sont ses enfants dans la hiérarchie des acteurs. Les routees ne sont pas partagés entre les routeurs. Cela est idéal pour un scénario primaire-réplica, où chaque routeur est le primaire et ses routees les répliques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ofa_x3hkM_sMzH5Nzum_Gg.png)
_Pool Router_

Ce n'est que la partie émergée de l'iceberg, donc je vous invite à lire la [documentation officielle](https://doc.akka.io/docs/akka/2.5/index-cluster.html) pour plus d'informations.

#### Un Cluster pour les calculs mathématiques

Imaginons un scénario d'utilisation. Supposons concevoir un système pour exécuter des calculs mathématiques sur demande. Le système est déployé en ligne, donc il a besoin d'une API REST pour recevoir les demandes de calcul. Un processeur interne gère ces demandes, exécute le calcul et retourne le résultat.

Pour l'instant, le processeur ne peut calculer que le [nombre de Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number). Nous décidons d'utiliser un cluster de nœuds pour distribuer la charge parmi les nœuds et améliorer les performances. Akka Cluster gérera la dynamique du cluster et l'équilibrage de charge entre les nœuds. D'accord, cela semble bien !

#### Hiérarchie des acteurs

D'abord, nous devons définir notre hiérarchie d'acteurs. Le système peut être divisé en trois parties fonctionnelles : la **logique métier**, la **gestion du cluster**, et le **nœud** lui-même. Il y a aussi le **serveur**, mais ce n'est pas un acteur, et nous travaillerons dessus plus tard.

**Logique métier**

L'application doit effectuer des calculs mathématiques. Nous pouvons définir un simple acteur `Processor` pour gérer toutes les tâches de calcul. Chaque calcul que nous supportons peut être implémenté dans un acteur spécifique, qui sera un enfant de l'acteur `Processor`. De cette manière, l'application est modulaire et plus facile à étendre et à maintenir. Pour l'instant, le seul enfant de `Processor` sera l'acteur `ProcessorFibonacci`. Je suppose que vous pouvez deviner quelle est sa tâche. Cela devrait être suffisant pour commencer.

**Gestion du cluster**

Pour gérer le cluster, nous avons besoin d'un `ClusterManager`. Cela semble simple, n'est-ce pas ? Cet acteur gère tout ce qui est lié au cluster, comme retourner ses membres lorsqu'on le demande. Il serait utile de journaliser ce qui se passe à l'intérieur du cluster, donc nous définissons un acteur `ClusterListener`. Celui-ci est un enfant du `ClusterManager`, et s'abonne aux événements du cluster pour les journaliser.

**Nœud**

L'acteur `Node` est la racine de notre hiérarchie. C'est le point d'entrée de notre système qui communique avec l'API. Les acteurs `Processor` et `ClusterManager` sont ses enfants, ainsi que l'acteur `ProcessorRouter`. Celui-ci est l'équilibreur de charge du système, distribuant la charge parmi les `Processor`. Nous le configurerons comme un Cluster Aware Router, donc chaque `ProcessorRouter` peut envoyer des messages aux `Processor` de chaque nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sblmA495LlrJLLBaIpbYYg.png)
_Hiérarchie des acteurs_

#### Implémentation des acteurs

Il est temps d'implémenter nos acteurs ! D'abord, nous implémentons les acteurs liés à la logique métier du système. Ensuite, nous passons aux acteurs pour la gestion du cluster et enfin à l'acteur racine (`Node`).

**ProcessorFibonacci**

Cet acteur exécute le calcul du nombre de Fibonacci. Il reçoit un message `Compute` contenant le nombre à calculer et la référence de l'acteur auquel répondre. La référence est importante, car il peut y avoir différents acteurs demandeurs. N'oubliez pas que nous travaillons dans un environnement distribué !

Une fois le message `Compute` reçu, la fonction `fibonacci` calcule le résultat. Nous l'enveloppons dans un objet `ProcessorResponse` pour fournir des informations sur le nœud qui a exécuté le calcul. Cela sera utile plus tard pour voir la politique de round-robin en action.

Le résultat est ensuite envoyé à l'acteur auquel nous devons répondre. Facile comme bonjour.

```scala
object ProcessorFibonacci {
  sealed trait ProcessorFibonacciMessage
  case class Compute(n: Int, replyTo: ActorRef) extends ProcessorFibonacciMessage

  def props(nodeId: String) = Props(new ProcessorFibonacci(nodeId))

  def fibonacci(x: Int): BigInt = {
    @tailrec def fibHelper(x: Int, prev: BigInt = 0, next: BigInt = 1): BigInt = x match {
      case 0 => prev
      case 1 => next
      case _ => fibHelper(x - 1, next, next + prev)
    }
    fibHelper(x)
  }
}

class ProcessorFibonacci(nodeId: String) extends Actor {
  import ProcessorFibonacci._

  override def receive: Receive = {
    case Compute(value, replyTo) => {
      replyTo ! ProcessorResponse(nodeId, fibonacci(value))
    }
  }
}
```

**Processor**

L'acteur `Processor` gère les sous-processeurs spécifiques, comme celui de Fibonacci. Il doit instancier les sous-processeurs et transmettre les demandes à ceux-ci. Pour l'instant, nous n'avons qu'un seul sous-processeur, donc le `Processor` reçoit un type de message : `ComputeFibonacci`. Ce message contient le nombre de Fibonacci à calculer. Une fois reçu, le nombre à calculer est envoyé à un `FibonacciProcessor`, ainsi que la référence du `sender()`.

```scala
object Processor {

  sealed trait ProcessorMessage

  case class ComputeFibonacci(n: Int) extends ProcessorMessage

  def props(nodeId: String) = Props(new Processor(nodeId))
}

class Processor(nodeId: String) extends Actor {
  import Processor._

  val fibonacciProcessor: ActorRef = context.actorOf(ProcessorFibonacci.props(nodeId), "fibonacci")

  override def receive: Receive = {
    case ComputeFibonacci(value) => {
      val replyTo = sender()
      fibonacciProcessor ! Compute(value, replyTo)
    }
  }
}
```

**ClusterListener**

Nous aimerions journaliser des informations utiles sur ce qui se passe dans le cluster. Cela pourrait nous aider à déboguer le système si nécessaire. C'est le but de l'acteur `ClusterListener`. Avant de démarrer, il s'abonne lui-même aux messages d'événements du cluster. L'acteur réagit à des messages comme `MemberUp`, `UnreachableMember`, ou `MemberRemoved`, en journalisant l'événement correspondant. Lorsque `ClusterListener` est arrêté, il se désabonne des événements du cluster.

```scala
object ClusterListener {
  def props(nodeId: String, cluster: Cluster) = Props(new ClusterListener(nodeId, cluster))
}

class ClusterListener(nodeId: String, cluster: Cluster) extends Actor with ActorLogging {

  override def preStart(): Unit = {
    cluster.subscribe(self, initialStateMode = InitialStateAsEvents,
      classOf[MemberEvent], classOf[UnreachableMember])
  }

  override def postStop(): Unit = cluster.unsubscribe(self)

  def receive = {
    case MemberUp(member) =>
      log.info("Node {} - Member is Up: {}", nodeId, member.address)
    case UnreachableMember(member) =>
      log.info(s"Node {} - Member detected as unreachable: {}", nodeId, member)
    case MemberRemoved(member, previousStatus) =>
      log.info(s"Node {} - Member is Removed: {} after {}",
        nodeId, member.address, previousStatus)
    case _: MemberEvent => // ignore
  }
}
```

**ClusterManager**

L'acteur responsable de la gestion du cluster est `ClusterManager`. Il crée l'acteur `ClusterListener`, et fournit la liste des membres du cluster sur demande. Il pourrait être étendu pour ajouter plus de fonctionnalités, mais pour l'instant, cela suffit.

```scala
object ClusterManager {

  sealed trait ClusterMessage
  case object GetMembers extends ClusterMessage

  def props(nodeId: String) = Props(new ClusterManager(nodeId))
}

class ClusterManager(nodeId: String) extends Actor with ActorLogging {

  val cluster: Cluster = Cluster(context.system)
  val listener: ActorRef = context.actorOf(ClusterListener.props(nodeId, cluster), "clusterListener")

  override def receive: Receive = {
    case GetMembers => {
      sender() ! cluster.state.members.filter(_.status == MemberStatus.up)
        .map(_.address.toString)
        .toList
    }
  }
}
```

**ProcessorRouter**

L'équilibrage de charge parmi les processeurs est géré par le `ProcessorRouter`. Il est créé par l'acteur `Node`, mais cette fois toutes les informations requises sont fournies dans la configuration du système.

```scala
class Node(nodeId: String) extends Actor {

  //...
  
  val processorRouter: ActorRef = context.actorOf(FromConfig.props(Props.empty), "processorRouter")
  
  //...
}
```

Analysons la partie pertinente dans le fichier `application.conf`.

```
akka {
  actor {
    ...
    deployment {
      /node/processorRouter {
        router = round-robin-group
        routees.paths = ["/user/node/processor"]
        cluster {
          enabled = on
          allow-local-routees = on
        }
      }
    }
  }
  ...
}
```

La première chose est de spécifier le chemin vers l'acteur routeur, qui est `/node/processorRouter`. À l'intérieur de cette propriété, nous pouvons configurer le comportement du routeur :

* `router` : il s'agit de la politique pour l'équilibrage de charge des messages. J'ai choisi le `round-robin-group`, mais il en existe beaucoup d'autres.
* `routees.paths` : ce sont les chemins vers les acteurs qui recevront les messages gérés par le routeur. Nous disons : « Lorsque vous recevez un message, recherchez les acteurs correspondant à ces chemins. Choisissez-en un selon la politique et transférez le message à celui-ci. » Puisque nous utilisons des Cluster Aware Routers, les routees peuvent être sur n'importe quel nœud du cluster.
* `cluster.enabled` : fonctionnons-nous dans un cluster ? La réponse est `on`, bien sûr !
* `cluster.allow-local-routees` : ici, nous permettons au routeur de choisir un routee dans son nœud.

En utilisant cette configuration, nous pouvons créer un routeur pour équilibrer la charge de travail parmi nos processeurs.

**Node**

La racine de notre hiérarchie d'acteurs est le `Node`. Il crée les acteurs enfants — `ClusterManager`, `Processor`, et `ProcessorRouter` — et transmet les messages au bon acteur. Rien de complexe ici.

```scala
object Node {

  sealed trait NodeMessage

  case class GetFibonacci(n: Int)

  case object GetClusterMembers

  def props(nodeId: String) = Props(new Node(nodeId))
}

class Node(nodeId: String) extends Actor {

  val processor: ActorRef = context.actorOf(Processor.props(nodeId), "processor")
  val processorRouter: ActorRef = context.actorOf(FromConfig.props(Props.empty), "processorRouter")
  val clusterManager: ActorRef = context.actorOf(ClusterManager.props(nodeId), "clusterManager")

  override def receive: Receive = {
    case GetClusterMembers => clusterManager forward GetMembers
    case GetFibonacci(value) => processorRouter forward ComputeFibonacci(value)
  }
}
```

#### Serveur et API

Chaque nœud de notre cluster exécute un serveur capable de recevoir des requêtes. Le `Server` crée notre système d'acteurs et est configuré via le fichier `application.conf`.

```scala
object Server extends App with NodeRoutes {

  implicit val system: ActorSystem = ActorSystem("cluster-playground")
  implicit val materializer: ActorMaterializer = ActorMaterializer()

  val config: Config = ConfigFactory.load()
  val address = config.getString("http.ip")
  val port = config.getInt("http.port")
  val nodeId = config.getString("clustering.ip")

  val node: ActorRef = system.actorOf(Node.props(nodeId), "node")

  lazy val routes: Route = healthRoute ~ statusRoutes ~ processRoutes

  Http().bindAndHandle(routes, address, port)
  println(s"Node $nodeId is listening at http://$address:$port")

  Await.result(system.whenTerminated, Duration.Inf)

}
```

[Akka HTTP](https://doc.akka.io/docs/akka-http/current/index.html) alimente le serveur lui-même et l'API REST, exposant trois endpoints simples. Ces endpoints sont définis dans le trait `NodeRoutes`.

Le premier est `/health`, pour vérifier l'état de santé d'un nœud. Il répond avec un `200 OK` si le nœud est opérationnel.

```scala
lazy val healthRoute: Route = pathPrefix("health") {
    concat(
      pathEnd {
        concat(
          get {
            complete(StatusCodes.OK)
          }
        )
      }
    )
  }
```

L'endpoint `/status/members` répond avec les membres actifs actuels du cluster.

```scala
lazy val statusRoutes: Route = pathPrefix("status") {
    concat(
      pathPrefix("members") {
        concat(
          pathEnd {
            concat(
              get {
                val membersFuture: Future[List[String]] = (node ? GetClusterMembers).mapTo[List[String]]
                onSuccess(membersFuture) { members =>
                  complete(StatusCodes.OK, members)
                }
              }
            )
          }
        )
      }
    )
  }
```

Le dernier (mais non le moindre) est l'endpoint `/process/fibonacci/n`, utilisé pour demander le nombre de Fibonacci de `n`.

```scala
lazy val processRoutes: Route = pathPrefix("process") {
    concat(
      pathPrefix("fibonacci") {
        concat(
          path(IntNumber) { n =>
            pathEnd {
              concat(
                get {
                  val processFuture: Future[ProcessorResponse] = (node ? GetFibonacci(n)).mapTo[ProcessorResponse]
                  onSuccess(processFuture) { response =>
                    complete(StatusCodes.OK, response)
                  }
                }
              )
            }
          }
        )
      }
    )
  }
```

Il répond avec un `ProcessorResponse` contenant le résultat, ainsi que l'identifiant du nœud où le calcul a eu lieu.

#### Configuration du Cluster

Une fois que nous avons tous nos acteurs, nous devons configurer le système pour qu'il fonctionne comme un cluster ! Le fichier `application.conf` est l'endroit où la magie opère. Je vais le diviser en morceaux pour le présenter mieux, mais vous pouvez trouver le fichier complet [ici](https://github.com/elleFlorio/akka-cluster-playground/blob/master/src/main/resources/application.conf).

Commençons par définir quelques variables utiles.

```
clustering {
  ip = "127.0.0.1"
  ip = ${?CLUSTER_IP}

  port = 2552
  port = ${?CLUSTER_PORT}

  seed-ip = "127.0.0.1"
  seed-ip = ${?CLUSTER_SEED_IP}

  seed-port = 2552
  seed-port = ${?CLUSTER_SEED_PORT}

  cluster.name = "cluster-playground"
}
```

Ici, nous définissons simplement l'ip et le port des nœuds et du seed, ainsi que le nom du cluster. Nous définissons une valeur par défaut, puis nous la remplaçons si une nouvelle est spécifiée. La configuration du cluster est la suivante.

```
akka {
  actor {
    provider = "cluster"
    ...
    /* configuration du routeur */
    ...
  }
  remote {
    log-remote-lifecycle-events = on
    netty.tcp {
      hostname = ${clustering.ip}
      port = ${clustering.port}
    }
  }
  cluster {
    seed-nodes = [
      "akka.tcp://"${clustering.cluster.name}"@"${clustering.seed-ip}":"${clustering.seed-port}
    ]
    auto-down-unreachable-after = 10s
  }
}
...
/* variables du serveur */
...
/* variables du cluster */
}
```

Akka Cluster est construit sur Akka Remoting, donc nous devons le configurer correctement. Tout d'abord, nous spécifions que nous allons utiliser Akka Cluster en disant que `provider = "cluster"`. Ensuite, nous lions `cluster.ip` et `cluster.port` à l'`hostname` et au `port` du framework web `netty`.

Le cluster nécessite certains nœuds seeds comme points d'entrée. Nous les définissons dans le tableau `seed-nodes`, au format `akka.tcp://"{clustering.cluster.name}"@"{clustering.seed-ip}":${clustering.seed-port}`. Pour l'instant, nous avons un nœud seed, mais nous pourrions en ajouter plus tard.

La propriété `auto-down-unreachable-after` définit un membre comme hors service après qu'il soit inaccessible pendant une période de temps. Cela ne doit être utilisé que pendant le développement, comme expliqué dans la [documentation officielle](https://doc.akka.io/docs/akka/2.5/cluster-usage.html#auto-downing-do-not-use-).

D'accord, le cluster est configuré, nous pouvons passer à l'étape suivante : la Dockerisation et le déploiement !

#### Dockerisation et déploiement

Pour créer le conteneur Docker de notre nœud, nous pouvons utiliser [sbt-native-packager](https://www.scala-sbt.org/sbt-native-packager). Son installation est facile : ajoutez `addSbtPlugin("com.typesafe.sbt" % "sbt-native-packager" % "1.3.15")` au fichier `plugin.sbt` dans le dossier `project/`. Cet outil amazing possède un plugin pour la création de conteneurs Docker. Il nous permet de configurer les propriétés de notre Dockerfile dans le fichier `build.sbt`.

```
// autres propriétés de build.sbt

enablePlugins(JavaAppPackaging)
enablePlugins(DockerPlugin)
enablePlugins(AshScriptPlugin)

mainClass in Compile := Some("com.elleflorio.cluster.playground.Server")
dockerBaseImage := "java:8-jre-alpine"
version in Docker := "latest"
dockerExposedPorts := Seq(8000)
dockerRepository := Some("elleflorio")
```

Une fois que nous avons configuré le plugin, nous pouvons créer l'image docker en exécutant la commande `sbt docker:publishLocal`. Exécutez la commande et goûtez la magie… ?

Nous avons l'image Docker de notre nœud, maintenant nous devons la déployer et vérifier que tout fonctionne bien. La manière la plus simple est de créer un fichier `docker-compose` qui lancera un seed et un couple d'autres nœuds.

```yml
version: '3.5'

networks:
  cluster-network:

services:
  seed:
    networks:
      - cluster-network
    image: elleflorio/akka-cluster-playground
    ports:
      - '2552:2552'
      - '8000:8000'
    environment:
      SERVER_IP: 0.0.0.0
      CLUSTER_IP: seed
      CLUSTER_SEED_IP: seed

  node1:
    networks:
      - cluster-network
    image: elleflorio/akka-cluster-playground
    ports:
      - '8001:8000'
    environment:
      SERVER_IP: 0.0.0.0
      CLUSTER_IP: node1
      CLUSTER_PORT: 1600
      CLUSTER_SEED_IP: seed
      CLUSTER_SEED_PORT: 2552

  node2:
    networks:
      - cluster-network
    image: elleflorio/akka-cluster-playground
    ports:
      - '8002:8000'
    environment:
      SERVER_IP: 0.0.0.0
      CLUSTER_IP: node2
      CLUSTER_PORT: 1600
      CLUSTER_SEED_IP: seed
      CLUSTER_SEED_PORT: 2552
```

Je ne vais pas passer de temps à l'expliquer, car c'est assez simple.

#### Exécutons-le !

Il est temps de tester notre travail ! Une fois que nous exécutons la commande `docker-compose up`, nous aurons un cluster de trois nœuds opérationnel. Le `seed` répondra aux requêtes sur le port `:8000`, tandis que `node1` et `node2` sur les ports `:8001` et `:8002`. Jouez un peu avec les différents endpoints. Vous verrez que les requêtes pour un nombre de Fibonacci seront calculées par un nœud différent à chaque fois, suivant une politique de round-robin. C'est bien, nous sommes fiers de notre travail et pouvons sortir pour une bière pour célébrer ! ?

#### Conclusion

Nous avons terminé ici ! Nous avons appris beaucoup de choses en ces dix minutes :

* Ce qu'est Akka Cluster et ce qu'il peut faire pour nous.
* Comment créer une application distribuée avec lui.
* Comment configurer un Group Router pour l'équilibrage de charge dans le cluster.
* Comment Dockeriser le tout et le déployer en utilisant docker-compose.

Vous pouvez trouver l'application complète dans mon [dépôt GitHub](https://github.com/elleFlorio/akka-cluster-playground). N'hésitez pas à contribuer ou à jouer avec comme vous le souhaitez ! ?

À bientôt ! ?