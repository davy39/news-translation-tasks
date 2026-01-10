---
title: Comment construire une blockchain simple basée sur des acteurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T20:32:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-actor-based-blockchain-aac1e996c177
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qrVfVF1nIjVO7ZvGs6q4UQ.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Functional Programming
  slug: functional-programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire une blockchain simple basée sur des acteurs
seo_desc: 'By Luca Florio

  Scalachain is a blockchain built using the Scala programming language and the actor
  model (Akka Framework).

  In this story I will show the development process to build this simple prototype
  of a blockchain. This means that the project i...'
---

Par Luca Florio

Scalachain est une blockchain construite en utilisant le langage de programmation Scala et le modèle d'acteur ([Akka Framework](https://akka.io/)).

Dans cette histoire, je vais montrer le processus de développement pour construire ce prototype simple d'une blockchain. Cela signifie que le projet n'est pas parfait, et qu'il peut y avoir de meilleures implémentations. Pour toutes ces raisons, toute contribution - qu'il s'agisse d'une suggestion ou d'une PR sur le dépôt GitHub [repository](https://github.com/elleFlorio/scalachain) - est la bienvenue ! :-)

Commençons par une petite introduction à la blockchain. Après cela, nous pouvons définir le modèle simplifié que nous allons implémenter.

#### **Introduction rapide à la blockchain**

Il existe de nombreux bons articles qui expliquent comment fonctionne une blockchain, donc je vais faire une introduction de haut niveau juste pour fournir un peu de contexte à ce projet.

La blockchain est un **grand livre distribué** : elle enregistre certaines transactions de valeurs (comme des pièces) entre un expéditeur et un destinataire. Ce qui distingue une blockchain d'une base de données traditionnelle est la nature décentralisée de la blockchain : elle est distribuée parmi plusieurs nœuds communicants qui garantissent la validité des transactions enregistrées.

La blockchain stocke les transactions dans des blocs, qui sont créés - nous disons **minés** - par des nœuds investissant de la puissance de calcul. Chaque bloc est créé en résolvant une énigme cryptographique qui est difficile à résoudre, mais facile à vérifier. De cette manière, chaque bloc représente le travail nécessaire pour résoudre une telle énigme. C'est la raison pour laquelle l'énigme cryptographique est appelée **Preuve de Travail** : la solution de l'énigme est la preuve qu'un nœud a dépensé une certaine quantité de travail pour la résoudre et miner le bloc.

Pourquoi les nœuds investissent-ils de la puissance de calcul pour miner un bloc ? Parce que la création d'un nouveau bloc est récompensée par un montant prédéfinis de pièces. De cette manière, les nœuds sont encouragés à miner de nouveaux blocs, contribuant à la croissance et à la force de la blockchain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IV05CUizMrIQCIXjqjaRKA.png)
_Blockchain simple_

La solution de la Preuve de Travail dépend des valeurs stockées dans le dernier bloc miné. De cette manière, chaque bloc est enchaîné au précédent. Cela signifie que, pour changer un bloc miné, un nœud devrait miner à nouveau tous les blocs au-dessus du bloc modifié. Puisque chaque bloc représente une quantité de travail, cette opération serait irréalisable une fois que plusieurs blocs sont minés sur le bloc modifié. C'est la fondation du **consensus distribué**, l'accord de tous les nœuds sur la validité des blocs (c'est-à-dire les transactions) stockés dans la blockchain.

Il peut arriver que différents nœuds minent un bloc en même temps, créant différentes "branches" à partir de la même blockchain - cela s'appelle un **fork** dans la blockchain. Cette situation est résolue lorsqu'une branche devient plus longue que les autres : la chaîne la plus longue l'emporte toujours, donc la branche gagnante devient la nouvelle blockchain.

#### **Le modèle de blockchain**

Scalachain est basé sur un modèle de blockchain qui est une simplification de celui de Bitcoin.

Les principaux composants de notre modèle de blockchain sont la Transaction, la Chaîne, l'algorithme de Preuve de Travail (PoW), et le Nœud. Les transactions sont stockées à l'intérieur des blocs de la chaîne, qui sont minés en utilisant le PoW. Le nœud est le serveur qui exécute la blockchain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jh1BNavGEHnHm0AWi2O-gA.png)
_Modèle Scalachain_

**Transaction**

Les transactions enregistrent le mouvement de pièces entre deux entités. Chaque transaction est composée d'un expéditeur, d'un destinataire et d'un montant de pièces. Les transactions seront enregistrées à l'intérieur des blocs de notre blockchain.

**Chaîne**

La chaîne est une liste liée de blocs contenant une liste de transactions. Chaque bloc de la chaîne a un index, la preuve qui le valide (plus sur cela plus tard), la liste des transactions, le hachage du bloc précédent, la liste des blocs précédents, et un horodatage. Chaque bloc est enchaîné au précédent par son hachage, qui est calculé en convertissant le bloc en une chaîne `JSON` puis en le hachant via une fonction de hachage `SHA-256`.

**PoW**

L'algorithme PoW est requis pour miner les blocs composant la blockchain. L'idée est de résoudre une énigme cryptographique qui est difficile à résoudre, mais facile à vérifier ayant la preuve. L'algorithme PoW qui est implémenté dans Scalachain est similaire à celui de Bitcoin (basé sur [Hashcash](https://en.wikipedia.org/wiki/Hashcash)). Il consiste à trouver un hachage avec N zéros en tête, qui est calculé à partir du hachage du dernier bloc et d'un nombre, qui est la preuve de notre algorithme.

Nous pouvons le formaliser comme suit :

```
NzerosHash = SHA-256(previousNodeHash + proof)
```

Plus N est élevé, plus il est difficile de trouver la preuve. Dans Scalachain N=4 (il sera configurable éventuellement).

**Nœud**

Le Nœud est le serveur exécutant notre blockchain. Il fournit une API REST pour interagir avec lui et effectuer des opérations de base telles que l'envoi d'une nouvelle transaction, l'obtention de la liste des transactions en attente, le minage d'un bloc et l'obtention de l'état actuel de la blockchain.

#### Implémentation de la blockchain en Scala

Nous allons implémenter le modèle défini en utilisant le langage de programmation Scala. D'un point de vue de haut niveau, les choses dont nous avons besoin pour implémenter une blockchain sont :

* transactions
* la chaîne de blocs contenant des listes de transactions
* l'algorithme PoW pour miner de nouveaux blocs

Ces composants sont les parties essentielles d'une blockchain.

**Transaction**

La transaction est un objet très simple : elle a un expéditeur, un destinataire et une valeur. Nous pouvons l'implémenter comme une simple `case class`.

```scala
case class Transaction(sender: String, recipient: String, value: Long)
```

**Chaîne**

La chaîne est le cœur de notre blockchain : c'est une liste liée de blocs contenant des transactions.

```scala

sealed trait Chain {

  val index: Int
  val hash: String
  val values: List[Transaction]
  val proof: Long
  val timestamp: Long
}

```

Nous commençons par créer un `sealed trait` qui représente le bloc de notre chaîne. La `Chain` peut avoir deux types : elle peut être une `EmptyChain` ou une `ChainLink`. La première est notre bloc zéro (le _bloc genesis_), et elle est implémentée comme un singleton (c'est un `case object`), tandis que la seconde est un bloc miné régulier.

```scala
case class ChainLink(index: Int, proof: Long, values: List[Transaction], previousHash: String = "", tail: Chain = EmptyChain, timestamp: Long = System.currentTimeMillis()) extends Chain {
  val hash = Crypto.sha256Hash(this.toJson.toString)
}

case object EmptyChain extends Chain {
  val index = 0
  val hash = "1"
  val values = Nil
  val proof = 100L
  val timestamp = System.currentTimeMillis()
}
```

Regardons plus en détail notre chaîne. Elle fournit un index, qui est la hauteur actuelle de la blockchain. Il y a la liste des `Transaction`, la preuve qui a validé le bloc, et l'horodatage de la création du bloc. La valeur de hachage est définie sur une valeur par défaut dans `EmptyChain`, tandis que dans `ChainLink`, elle est calculée en convertissant l'objet en sa représentation `JSON` et en le hachant avec une fonction utilitaire (voir le package `crypto` dans le [repository](https://github.com/elleFlorio/scalachain)). Le `ChainLink` fournit également le hachage du bloc précédent dans la chaîne (notre lien entre les blocs). Le champ tail est une référence aux blocs précédemment minés. Cela peut ne pas être la solution la plus efficace, mais c'est utile pour voir comment la blockchain grandit dans notre implémentation simplifiée.

Nous pouvons améliorer notre `Chain` avec quelques utilitaires. Nous pouvons lui ajouter un _companion object_ qui définit une méthode `apply` pour créer une nouvelle chaîne en lui passant une liste de blocs. Un companion object est comme un "ensemble de méthodes statiques" - en faisant une analogie avec Java - qui a des droits d'accès complets sur les champs et méthodes de la classe/trait.

```scala
object Chain {
  def apply[T](b: Chain*): Chain = {
    if (b.isEmpty) EmptyChain
    else {
      val link = b.head.asInstanceOf[ChainLink]
      ChainLink(link.index, link.proof, link.values, link.previousHash, apply(b.tail: _*))
    }
  }
}
```

Si la liste des blocs est vide, nous initialisons simplement notre blockchain avec un `EmptyChain`. Sinon, nous créons un nouveau `ChainLink` en ajoutant comme queue le résultat de la méthode apply sur les blocs restants de la liste. De cette manière, la liste des blocs est ajoutée en suivant l'ordre de la liste.

Il serait bien d'avoir la possibilité d'ajouter un nouveau bloc à notre chaîne en utilisant un simple opérateur d'addition, comme celui que nous avons sur `List`. Nous pouvons définir notre propre opérateur d'addition `::` à l'intérieur du trait `Chain`.

```scala
sealed trait Chain {

  val index: Int
  val hash: String
  val values: List[Transaction]
  val proof: Long
  val timestamp: Long

  def ::(link: Chain): Chain = link match {
    case l:ChainLink => ChainLink(l.index, l.proof, l.values, this.hash, this)
    case _ => throw new InvalidParameterException("Cannot add invalid link to chain")
  }
}
```

Nous faisons correspondre le motif sur le bloc qui est passé comme argument : si c'est un objet `ChainLink` valide, nous l'ajoutons comme tête de notre chaîne, en mettant la chaîne comme queue du nouveau bloc, sinon nous lançons une exception.

**PoW**

L'algorithme PoW est fondamental pour le minage de nouveaux blocs. Nous l'implémentons comme un simple algorithme :

1. Prendre le hachage du dernier bloc et un nombre représentant la preuve.

2. Concaténer le hachage et la preuve dans une chaîne.

3. Hacher la chaîne résultante en utilisant l'algorithme `SHA-256`.

4. Vérifier les 4 premiers caractères du hachage : s'ils sont quatre zéros, retourner la preuve.

5. Sinon, répéter l'algorithme en augmentant la preuve de un.

Ceci est une simplification de l'algorithme [HashCash](https://en.wikipedia.org/wiki/Hashcash) utilisé dans la blockchain Bitcoin.

Puisqu'il s'agit d'une fonction récursive, nous pouvons l'implémenter comme une fonction récursive terminale pour améliorer l'utilisation des ressources.

```scala
object ProofOfWork {

  def proofOfWork(lastHash: String): Long = {
    @tailrec
    def powHelper(lastHash: String, proof: Long): Long = {
      if (validProof(lastHash, proof))
        proof
      else
        powHelper(lastHash, proof + 1)
    }

    val proof = 0
    powHelper(lastHash, proof)
  }

  def validProof(lastHash: String, proof: Long): Boolean = {
    val guess = (lastHash ++ proof.toString).toJson.toString
    val guessHash = Crypto.sha256Hash(guess)
    (guessHash take 4) == "0000"
  }
}
```

La fonction `validProof` est utilisée pour vérifier si la preuve que nous testons est la bonne. La fonction `powHelper` est une fonction auxiliaire qui exécute notre boucle en utilisant la récursion terminale, en augmentant la preuve à chaque étape. La fonction `proofOfWork` enveloppe tout cela et est exposée par l'objet `ProofOfWork`.

#### Le modèle d'acteur

Le modèle d'acteur est un modèle de programmation conçu pour le **traitement concurrent**, la **scalabilité** et la **tolérance aux pannes**. Le modèle définit les éléments atomiques qui composent les systèmes logiciels - les **acteurs** - et la manière dont ces éléments interagissent entre eux. Dans ce projet, nous utiliserons le modèle d'acteur implémenté en Scala par le framework Akka.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6jDNPwSi80yxej_swJ5kfg.png)
_Modèle d'acteur_

**Acteur**

L'acteur est l'unité atomique du modèle d'acteur. C'est une unité de calcul qui peut envoyer et recevoir des messages. Chaque acteur a un état interne **privé** et une boîte aux lettres. Lorsqu'un acteur reçoit et traite un message, il peut réagir de 3 manières :

* Envoyer un message à un autre acteur.
* Changer son état interne.
* Créer un autre acteur.

La communication est **asynchrone**, et les messages sont retirés de la boîte aux lettres et traités en série. Pour permettre le calcul parallèle des messages, vous devez créer plusieurs acteurs. De nombreux acteurs ensemble créent un **système d'acteurs**. Le comportement de l'application émerge de l'interaction entre les acteurs fournissant différentes fonctionnalités.

**Les acteurs sont indépendants**

Les acteurs sont indépendants les uns des autres et ne partagent pas leur état interne. Ce fait a un couple de conséquences importantes :

1. Les acteurs peuvent traiter les messages **sans effets secondaires** les uns des autres.

2. Il n'est pas important où se trouve un acteur - qu'il soit sur votre ordinateur portable, un serveur ou dans le cloud - une fois que nous connaissons son adresse, nous pouvons demander ses services en lui envoyant un message.

Le premier point rend le calcul concurrent très facile. Nous pouvons être sûrs que le traitement d'un message n'interférera pas avec le traitement d'un autre. Pour atteindre le **traitement concurrent**, nous pouvons déployer plusieurs acteurs capables de traiter le même type de message.

Le deuxième point concerne la **scalabilité** : nous avons besoin de plus de puissance de calcul ? Pas de problème : nous pouvons démarrer une nouvelle machine et déployer de nouveaux acteurs qui rejoindront le système d'acteurs existant. Leurs adresses de boîte aux lettres seront découvrables par les acteurs existants, qui commenceront à communiquer avec eux.

**Les acteurs sont supervisés**

Comme nous l'avons dit dans la description de l'acteur, l'une des réactions possibles à un message est la création d'autres acteurs. Lorsque cela se produit, le père devient le _superviseur_ de ses enfants. Si un enfant échoue, le superviseur peut décider de l'action à prendre, qu'il s'agisse de créer un nouvel acteur, d'ignorer l'échec ou de le transmettre à son propre superviseur. De cette manière, le système d'acteurs devient un arbre hiérarchique, chaque nœud supervisant ses enfants. C'est ainsi que le modèle d'acteur fournit la **tolérance aux pannes**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GMV9z5B_00Kwjx8b2Kolxg.png)
_Hiérarchie des acteurs_

#### Broker, un acteur simple

Le premier acteur que nous allons implémenter est le Broker Actor : c'est le gestionnaire des transactions de notre blockchain. Ses responsabilités sont l'ajout de nouvelles transactions et la récupération de celles en attente.

Le Broker Actor réagit à trois types de messages, définis dans le `companion object` de la classe Broker :

```scala

object Broker {
  sealed trait BrokerMessage
  case class AddTransaction(transaction: Transaction) extends BrokerMessage
  case object GetTransactions extends BrokerMessage
  case object Clear extends BrokerMessage

  val props: Props = Props(new Broker)
}
```

Nous créons un trait `BrokerMessage` pour identifier les messages du Broker Actor. Chaque autre message étendra ce trait. `AddTransaction` ajoute une nouvelle transaction à la liste des transactions en attente. `GetTransaction` récupère les transactions en attente, et `Clear` vide la liste. La valeur `props` est utilisée pour initialiser l'acteur lorsqu'il sera créé.

```scala
class Broker extends Actor with ActorLogging {
  import Broker._

  var pending: List[Transaction] = List()

  override def receive: Receive = {
    case AddTransaction(transaction) => {
      pending = transaction :: pending
      log.info(s"Added $transaction to pending Transaction")
    }
    case GetTransactions => {
      log.info(s"Getting pending transactions")
      sender() ! pending
    }
    case Clear => {
      pending = List()
      log.info("Clear pending transaction List")
    }
  }
}
```

La classe `Broker` contient la logique métier pour réagir aux différents messages. Je ne vais pas entrer dans les détails car c'est trivial. La chose la plus intéressante est la manière dont nous répondons à une demande des transactions en attente. Nous les envoyons au `sender()` du message `GetTransaction` en utilisant l'opérateur `tell` (`!`). Cet opérateur signifie "envoyer le message et ne pas attendre de réponse" - aka fire-and-forget.

#### Miner, un acteur avec différents états

Le Miner Actor est celui qui mine de nouveaux blocs pour notre blockchain. Puisque nous ne voulons pas miner un nouveau bloc alors que nous en minons un autre, le Miner Actor aura deux états : `ready`, lorsqu'il est prêt à miner un nouveau bloc, et `busy`, lorsqu'il est en train de miner un bloc.

Commençons par définir le `companion object` avec les messages du Miner Actor. Le motif est le même, avec un trait scellé - `MinerMessage` - utilisé pour définir le type de messages auxquels cet acteur réagit.

```scala
object Miner {
  sealed trait MinerMessage
  case class Validate(hash: String, proof: Long) extends MinerMessage
  case class Mine(hash: String) extends MinerMessage
  case object Ready extends MinerMessage

  val props: Props = Props(new Miner)
}
```

Le message `Validate` demande une validation d'une preuve, et transmet au Miner le hachage et la preuve à vérifier. Puisque ce composant est celui qui interagit avec l'algorithme PoW, c'est à lui d'exécuter cette vérification. Le message `Mine` demande le minage à partir d'un hachage spécifié. Le dernier message, `Ready`, déclenche une transition d'état.

**Même acteur, différents états**

La particularité de cet acteur est qu'il réagit aux messages en fonction de son état : `busy` ou `ready`. Analysons la différence de comportement :

* **busy** : le Miner est occupé à miner un bloc. Si une nouvelle demande de minage arrive, il doit la refuser. S'il est demandé d'être prêt, le Miner doit changer son état en prêt.
* **ready** : le Miner est inactif. Si une demande de minage arrive, il doit commencer à miner un nouveau bloc. S'il est demandé d'être prêt, il doit dire : "OK, je suis prêt !"
* **les deux** : le Miner doit toujours être disponible pour vérifier l'exactitude d'une preuve, que ce soit dans un état prêt ou occupé.

Il est temps de voir comment nous pouvons implémenter cette logique dans notre code. Nous commençons par définir le comportement commun, la validation d'une preuve.

Nous définissons une fonction `validate` qui réagit au message `Validate` : si la preuve est valide, nous répondons à l'expéditeur avec un succès, sinon avec un échec. Les états `ready` et `busy` sont définis comme des fonctions qui "étendent" la fonction `validate`, puisque c'est un comportement que nous voulons dans les deux états.

```scala
def validate: Receive = {
    case Validate(hash, proof) => {
      log.info(s"Validating proof $proof")
      if (ProofOfWork.validProof(hash, proof)){
        log.info("proof is valid!")
        sender() ! Success
      }
      else{
        log.info("proof is not valid")
        sender() ! Failure(new InvalidProofException(hash, proof))
      }
    }
  }
```

Un couple de choses à souligner ici.

1. La transition d'état est déclenchée en utilisant la fonction `become`, fournie par le framework Akka. Cela prend comme argument une fonction qui retourne un objet `Receive`, comme ceux que nous avons définis pour la `validation`, les états `busy` et `ready`.

2. Lorsqu'une demande de minage est reçue par le Miner, il répond avec un `Future` contenant l'exécution de l'algorithme PoW. De cette manière, nous pouvons travailler de manière asynchrone, rendant le Miner libre de faire d'autres tâches, telles que la validation.

3. Le **superviseur** de cet acteur contrôle la transition d'état. La raison de ce choix est que le Miner est agnostique quant à l'état du système. Il ne sait pas quand le calcul de minage dans le `Future` sera terminé, et il ne peut pas savoir si le bloc qu'il est en train de miner a déjà été miné par un autre nœud. Cela nécessiterait d'arrêter le minage du hachage actuel et de commencer le minage du hachage du nouveau bloc.

La dernière chose à faire est de fournir un état initial en remplaçant la fonction `receive`.

```scala
override def receive: Receive = {
    case Ready => become(ready)
  }
```

Nous commençons par attendre un message `Ready`. Lorsqu'il arrive, nous démarrons notre Miner.

#### Blockchain, un acteur persistant

Le Blockchain Actor interagit avec la logique métier de la blockchain. Il peut ajouter un nouveau bloc à la blockchain et il peut récupérer des informations sur l'état de la blockchain. Cet acteur a un autre superpouvoir : il peut **persister** et récupérer l'état de la blockchain. Cela est possible en implémentant le trait `PersistentActor` fourni par le framework Akka.

```scala
object Blockchain {
  sealed trait BlockchainEvent
  case class AddBlockEvent(transactions: List[Transaction], proof: Long) extends BlockchainEvent

  sealed trait BlockchainCommand
  case class AddBlockCommand(transactions: List[Transaction], proof: Long) extends BlockchainCommand
  case object GetChain extends BlockchainCommand
  case object GetLastHash extends BlockchainCommand
  case object GetLastIndex extends BlockchainCommand

  case class State(chain: Chain)

  def props(chain: Chain, nodeId: String): Props = Props(new Blockchain(chain, nodeId))
}
view raw
```

Nous pouvons voir que le `companion object` de cet acteur a plus d'éléments que les autres. La classe `State` est l'endroit où nous stockons l'état de notre blockchain, c'est-à-dire sa `Chain`. L'idée est de mettre à jour l'état chaque fois qu'un nouveau bloc est créé.

À cette fin, il existe deux traits différents : `BlockchainEvent` et `BlockchainCommand`. Le premier est utilisé pour gérer les événements qui déclencheront la logique de persistance, le second est utilisé pour envoyer des commandes directes à l'acteur. Le message `AddBlockEvent` est l'événement qui mettra à jour notre état. Les commandes `AddBlockCommand`, `GetChain`, `GetLastHash` et `LastIndex` sont celles utilisées pour interagir avec la blockchain sous-jacente.

La fonction `props` habituelle initialise le Blockchain Actor avec la `Chain` initiale et le `nodeId` du nœud Scalachain.

```scala
class Blockchain(chain: Chain, nodeId: String) extends PersistentActor with ActorLogging{
  import Blockchain._

  var state = State(chain)

  override def persistenceId: String = s"chainer-$nodeId"
  
  //Code...
}
```

Le Blockchain Actor étend le trait `PersistentActor` fourni par le framework Akka. De cette manière, nous avons tout le nécessaire pour persister et récupérer notre état.

Nous initialisons l'état en utilisant la `Chain` fournie comme argument lors de la création. Le `nodeId` fait partie de la `persistenceId` que nous remplaçons. La logique de persistance l'utilisera pour identifier l'état persistant. Puisque nous pouvons avoir plusieurs nœuds Scalachain en cours d'exécution sur la même machine, nous avons besoin de cette valeur pour persister et récupérer correctement l'état de chaque nœud.

```scala
def updateState(event: BlockchainEvent) = event match {
    case AddBlockEvent(transactions, proof) =>
      {
        state = State(ChainLink(state.chain.index + 1, proof, transactions) :: state.chain)
        log.info(s"Added block ${state.chain.index} containing ${transactions.size} transactions")
      }
  }
```

La fonction `updateState` exécute la mise à jour de l'état de l'acteur lorsque l'événement `AddBlockEvent` est reçu.

```scala
override def receiveRecover: Receive = {
    case SnapshotOffer(metadata, snapshot: State) => {
      log.info(s"Recovering from snapshot ${metadata.sequenceNr} at block ${snapshot.chain.index}")
      state = snapshot
    }
    case RecoveryCompleted => log.info("Recovery completed")
    case evt: AddBlockEvent => updateState(evt)
  }
```

La fonction `receiveRecover` réagit aux messages de récupération envoyés par la logique de persistance. Lors de la création d'un acteur, un état persistant (**snapshot**) peut lui être offert en utilisant le message `SnapshotOffer`. Dans ce cas, l'état actuel devient celui fourni par le snapshot.

Le message `RecoveryCompleted` nous informe que le processus de récupération s'est terminé avec succès. L'événement `AddBlockEvent` déclenche la fonction `updateState` en passant l'événement lui-même.

```scala
override def receiveCommand: Receive = {
    case SaveSnapshotSuccess(metadata) => log.info(s"Snapshot ${metadata.sequenceNr} saved successfully")
    case SaveSnapshotFailure(metadata, reason) => log.error(s"Error saving snapshot ${metadata.sequenceNr}: ${reason.getMessage}")
    case AddBlockCommand(transactions : List[Transaction], proof: Long) => {
      persist(AddBlockEvent(transactions, proof)) {event =>
        updateState(event)
      }

      // This is a workaround to wait until the state is persisted
      deferAsync(Nil) { _ =>
        saveSnapshot(state)
        sender() ! state.chain.index
      }
    }
    case AddBlockCommand(_, _) => log.error("invalid add block command")
    case GetChain => sender() ! state.chain
    case GetLastHash => sender() ! state.chain.hash
    case GetLastIndex => sender() ! state.chain.index
  }
```

La fonction `receiveCommand` est utilisée pour réagir aux commandes directes envoyées à l'acteur. Passons les commandes `GetChain`, `GetLastHash` et `GetLastIndex`, car elles sont triviales. La commande `AddBlockCommand` est la partie intéressante : elle crée et déclenche un événement `AddBlock`, qui est persistant dans le journal des événements de l'acteur. De cette manière, les événements peuvent être rejoués en cas de récupération.

La fonction `deferAsync` attend que l'état soit mis à jour après le traitement de l'événement. Une fois l'événement exécuté, l'acteur peut sauvegarder le snapshot de l'état et informer l'expéditeur du message avec l'index mis à jour de la `Chain`. Les messages `SaveSnapshotSucces` et `SaveSnapshotFailure` nous aident à suivre les éventuels échecs.

#### Node, un acteur pour les régner tous

Le Node Actor est l'épine dorsale de notre nœud Scalachain. C'est le **superviseur** de tous les autres acteurs (Broker, Miner et Blockchain), et celui qui communique avec le monde extérieur via l'API REST.

```scala
object Node {

  sealed trait NodeMessage

  case class AddTransaction(transaction: Transaction) extends NodeMessage

  case class CheckPowSolution(solution: Long) extends NodeMessage

  case class AddBlock(proof: Long) extends NodeMessage

  case object GetTransactions extends NodeMessage

  case object Mine extends NodeMessage

  case object StopMining extends NodeMessage

  case object GetStatus extends NodeMessage

  case object GetLastBlockIndex extends NodeMessage

  case object GetLastBlockHash extends NodeMessage

  def props(nodeId: String): Props = Props(new Node(nodeId))

  def createCoinbaseTransaction(nodeId: String) = Transaction("coinbase", nodeId, 100)
}
```

Le Node Actor doit gérer tous les messages de haut niveau provenant de l'API REST. C'est la raison pour laquelle nous trouvons dans le `companion object` plus ou moins les mêmes messages que nous avons implémentés dans les acteurs enfants. La fonction props prend un nodeId comme argument pour créer notre Node Actor. Ce sera celui utilisé pour l'initialisation de l'acteur Blockchain. La fonction `createCoinbaseTransaction` crée simplement une transaction attribuant un montant de pièces prédéfinis au nœud lui-même. Ce sera la **récompense** pour le minage réussi d'un nouveau bloc de la blockchain.

```scala
class Node(nodeId: String) extends Actor with ActorLogging {

  import Node._

  implicit lazy val timeout = Timeout(5.seconds)

  val broker = context.actorOf(Broker.props)
  val miner = context.actorOf(Miner.props)
  val blockchain = context.actorOf(Blockchain.props(EmptyChain, nodeId))

  miner ! Ready
  
  //Code...
}
```

Regardons l'initialisation du Node Actor. La valeur timeout est utilisée par l'opérateur `ask` (`?`) (cela sera expliqué bientôt). Tous nos acteurs sont créés dans le contexte de l'acteur, en utilisant la fonction `props` que nous avons définie dans chaque acteur.

L'acteur Blockchain est initialisé avec `EmptyChain` et le `nodeId` du Node. Une fois tout créé, nous informons le Miner Actor d'être prêt à miner en lui envoyant un message `Ready`. D'accord, nous sommes maintenant prêts à recevoir des messages et à réagir à ceux-ci.

```scala
override def receive: Receive = {
    case AddTransaction(transaction) => {
      //Code...
    }
    case CheckPowSolution(solution) => {
      //Code...
    }
    case AddBlock(proof) => {
      //Code...
    }
    case Mine => {
      //Code...
    }
    case GetTransactions => broker forward Broker.GetTransactions
    case GetStatus => blockchain forward GetChain
    case GetLastBlockIndex => blockchain forward GetLastIndex
    case GetLastBlockHash => blockchain forward GetLastHash
  }
```

Voici un aperçu de la fonction `receive` habituelle que nous devons remplacer. Je vais analyser la logique des `case` les plus complexes plus tard, regardons maintenant les quatre derniers. Ici, nous transférons les messages à l'acteur Blockchain, puisque aucun traitement n'est requis. En utilisant l'opérateur `forward`, le `sender()` du message sera celui qui a originé le message, et non le Node Actor. De cette manière, le Blockchain Actor répondra à l'expéditeur original du message (la couche API REST).

```scala
override def receive: Receive = {
    case AddTransaction(transaction) => {
      val node = sender()
      broker ! Broker.AddTransaction(transaction)
      (blockchain ? GetLastIndex).mapTo[Int] onComplete {
        case Success(index) => node ! (index + 1)
        case Failure(e) => node ! akka.actor.Status.Failure(e)
      }
    }
  
  //Code...
}
```

Le message `AddTransaction` déclenche la logique pour stocker une nouvelle transaction dans la liste des transactions en attente de notre blockchain. Le Node Actor répond avec l'`index` du bloc qui contiendra la transaction.

Tout d'abord, nous stockons l'« adresse » du `sender()` du message dans une valeur `node` pour l'utiliser plus tard. Nous envoyons à l'acteur Broker un message pour ajouter une nouvelle transaction, puis nous `demandons` à l'acteur Blockchain le dernier index de la chaîne. L'opérateur `ask` - celui exprimé avec `?` - est utilisé pour envoyer un message à un acteur et attendre une réponse. La réponse (mappée à une valeur `Int`) peut être un `Success` ou un `Failure`.

Dans le premier cas, nous renvoyons à l'expéditeur (`node`) l'`index+1`, puisque ce sera l'index du prochain bloc miné. En cas d'échec, nous répondons à l'expéditeur avec un `Failure` contenant la raison de l'échec. Rappelez-vous ce motif :

**ask → wait for a response → handle success/failure**

parce que nous le reverrons.

```scala
override def receive: Receive = {
    //Code...
  
    case CheckPowSolution(solution) => {
      val node = sender()
      (blockchain ? GetLastHash).mapTo[String] onComplete {
        case Success(hash: String) => miner.tell(Validate(hash, solution), node)
        case Failure(e) => node ! akka.actor.Status.Failure(e)
      }
    }
  
  //Code...
}
view raw
```

Cette fois, nous devons vérifier si une solution à l'algorithme PoW est correcte. Nous demandons à l'acteur Blockchain le hachage du dernier bloc, et nous disons à l'acteur Miner de valider la solution par rapport au hachage. Dans la fonction `tell`, nous passons au Miner le message `Validate` ainsi que l'adresse de l'expéditeur, afin que le mineur puisse répondre directement à celui-ci. C'est une autre approche, comme celle du `forward` que nous avons vue précédemment.

```scala
override def receive: Receive = {
    //Code...
  
    case AddBlock(proof) => {
      val node = sender()
      (self ? CheckPowSolution(proof)) onComplete {
        case Success(_) => {
          (broker ? Broker.GetTransactions).mapTo[List[Transaction]] onComplete {
            case Success(transactions) => blockchain.tell(AddBlockCommand(transactions, proof), node)
            case Failure(e) => node ! akka.actor.Status.Failure(e)
          }
          broker ! Clear
        }
        case Failure(e) => node ! akka.actor.Status.Failure(e)
      }
    }
  
    //Code...
}
```

D'autres nœuds peuvent miner des blocs, donc nous pouvons recevoir une demande pour ajouter un bloc que nous n'avons pas miné. La preuve est suffisante pour ajouter le nouveau bloc, puisque nous supposons que tous les nœuds partagent la même liste de transactions en attente.

```scala
override def receive: Receive = {
    //Code...
  
    case Mine => {
      val node = sender()
      (blockchain ? GetLastHash).mapTo[String] onComplete {
        case Success(hash) => (miner ? Miner.Mine(hash)).mapTo[Future[Long]] onComplete {
          case Success(solution) => waitForSolution(solution)
          case Failure(e) => log.error(s"Error finding PoW solution: ${e.getMessage}")
        }
        case Failure(e) => node ! akka.actor.Status.Failure(e)
      }
    }
  
    //Code...
  }

  def waitForSolution(solution: Future[Long]) = Future {
    solution onComplete {
      case Success(proof) => {
        broker ! Broker.AddTransaction(createCoinbaseTransaction(nodeId))
        self ! AddBlock(proof)
        miner ! Ready
      }
      case Failure(e) => log.error(s"Error finding PoW solution: ${e.getMessage}")
    }
  }
```

Ceci est une simplification, dans le réseau Bitcoin, il ne peut pas y avoir une telle hypothèse. Tout d'abord, nous devons vérifier si la solution est valide. Nous faisons cela en envoyant un message au nœud lui-même : `self ? CheckPowSolution(proof)`. Si la preuve est valide, nous obtenons la liste des transactions en attente de l'acteur Broker, puis nous `disons` à l'acteur Blockchain d'ajouter à la chaîne un nouveau bloc contenant les transactions et la preuve validée. La dernière chose à faire est de commander à l'acteur Broker de vider la liste des transactions en attente.

Le dernier message est la demande de commencer le minage d'un nouveau bloc. Nous avons besoin du hachage du dernier bloc de la chaîne, donc nous le demandons à l'acteur Blockchain. Une fois que nous avons le hachage, nous pouvons commencer à miner un nouveau bloc.

L'algorithme PoW est une opération de longue durée, donc l'acteur Miner répond immédiatement avec un `Future` contenant le calcul. La fonction `waitForSolution` attend que le calcul soit terminé, tandis que le Node Actor continue à faire ses affaires.

Lorsque nous avons une solution, nous nous récompensons en ajoutant la **transaction coinbase** à la liste des transactions en attente. Ensuite, nous ajoutons le nouveau bloc à la chaîne et disons à l'acteur Miner d'être prêt à miner un autre bloc.

#### API REST avec Akka HTTP

Cette dernière section décrit le serveur et l'API REST. C'est la partie la plus "externe" de notre application, celle qui connecte le monde extérieur au nœud Scalachain. Nous allons utiliser la bibliothèque Akka HTTP, qui fait partie du framework Akka. Commençons par regarder le serveur, le point d'entrée de notre application.

```scala
object Server extends App with NodeRoutes {

  val address = if (args.length > 0) args(0) else "localhost"
  val port = if (args.length > 1) args(1).toInt else 8080

  implicit val system: ActorSystem = ActorSystem("scalachain")

  implicit val materializer: ActorMaterializer = ActorMaterializer()

  val node: ActorRef = system.actorOf(Node.props("scalaChainNode0"))

  lazy val routes: Route = statusRoutes ~ transactionRoutes ~ mineRoutes

  Http().bindAndHandle(routes, address, port)

  println(s"Server online at http://$address:$port/")

  Await.result(system.whenTerminated, Duration.Inf)

}
```

Puisque le `Server` est notre point d'entrée, il doit étendre le trait `App`. Il étend également `NodeRoutes`, un trait qui contient toutes les routes http vers les différents endpoints du nœud.

La valeur `system` est l'endroit où nous stockons notre `ActorSystem`. Chaque acteur créé dans ce système sera capable de parler aux autres à l'intérieur de celui-ci. Akka HTTP nécessite également la définition d'une autre valeur, le `ActorMaterializer`. Cela est lié au module Akka Streams, mais puisque Akka HTTP est construit sur celui-ci, nous avons toujours besoin de cet objet pour être initialisé dans notre serveur (si vous voulez approfondir la relation avec les streams, regardez [ici](https://doc.akka.io/docs/akka-http/current/implications-of-streaming-http-entity.html)).

Le Node Actor est créé avec les routes HTTP du nœud, qui sont enchaînées en utilisant l'opérateur `~`. Ne vous inquiétez pas des routes pour l'instant, nous y reviendrons dans un moment.

La dernière chose à faire est de démarrer notre serveur en utilisant la fonction `Http().bindHandle`, qui liera également les routes que nous lui passons comme argument. La fonction `Await.result` attendra le signal de terminaison pour arrêter le serveur.

Le serveur sera inutile sans les routes pour déclencher la logique métier de l'application. Nous définissons les routes dans le trait `NodeRoutes`, en les différenciant selon la logique différente qu'elles déclenchent :

* `statusRoutes` contient les endpoints pour demander au nœud Scalachain son statut.
* `transactionRoutes` gère tout ce qui est lié aux transactions.
* `mineRoutes` a l'endpoint pour démarrer le processus de minage

Remarquez que cette différenciation est logique, juste pour garder les choses ordonnées et lisibles. Les trois routes seront enchaînées en une seule après leur initialisation dans le serveur.

```scala
//Imports...
import com.elleflorio.scalachain.utils.JsonSupport._
// Imports...

trait NodeRoutes extends SprayJsonSupport {

  implicit def system: ActorSystem

  def node: ActorRef

  implicit lazy val timeout = Timeout(5.seconds)

  //Code...
}
```

Le trait `NodeRoutes` étend `SprayJsonSupport` pour ajouter la sérialisation/désérialisation `JSON`. [SprayJson](https://github.com/spray/spray-json) est une bibliothèque Scala analogue à Jackson en Java, et elle est fournie gratuitement avec Akka HTTP.

Pour convertir nos objets en une chaîne JSON, nous importons la classe `JsonSupport` définie dans le package `utils`, qui contient des lecteurs/écrivains personnalisés pour chaque objet. Je ne vais pas entrer dans les détails, vous pouvez trouver la [classe](https://github.com/elleFlorio/scalachain/blob/master/src/main/scala/com/elleflorio/scalachain/utils/JsonSupport.scala) dans le dépôt si vous voulez regarder l'implémentation.

Nous avons quelques valeurs implicites. Le `ActorSystem` est utilisé pour définir le système d'acteurs, tandis que le `Timeout` est utilisé par la fonction `OnSuccess` qui attend une réponse des acteurs. Le `ActorRef` est défini en le remplaçant dans l'implémentation du serveur.

```scala
//Code...

lazy val statusRoutes: Route = pathPrefix("status") {
    concat(
      pathEnd {
        concat(
          get {
            val statusFuture: Future[Chain] = (node ? GetStatus).mapTo[Chain]
            onSuccess(statusFuture) { status =>
              complete(StatusCodes.OK, status)
            }
          }
        )
      }
    )
  }

//Code...
```

L'endpoint pour obtenir le statut de la blockchain est défini dans les statusRoutes. Nous définissons le pathPrefix comme "status" donc le nœud répondra au chemin ` http://<address>:<port/status. Après cela, il y a la définition des actions HTTP que nous voulons activer sur le chemin. Ici, nous voulons obtenir le statut de la blockchain, donc nous définissons seulement l'action get. À l'intérieur, nous demandons à l'acteur Node d'obtenir la Chain actuelle. Lorsque l'acteur répond, la Chain est envoyée sous forme de JSON avec un statut ok dans la méthode complete.

```scala
//Code...

lazy val transactionRoutes: Route = pathPrefix("transactions") {
    concat(
      pathEnd {
        concat(
          get {
            val transactionsRetrieved: Future[List[Transaction]] =
              (node ? GetTransactions).mapTo[List[Transaction]]
            onSuccess(transactionsRetrieved) { transactions =>
              complete(transactions.toList)
            }
          },
          post {
            entity(as[Transaction]) { transaction =>
              val transactionCreated: Future[Int] =
                (node ? AddTransaction(transaction)).mapTo[Int]
              onSuccess(transactionCreated) { done =>
                complete((StatusCodes.Created, done.toString))
              }
            }
          }
        )
      }
    )
  }

//Code...
```

Les `transactionRoutes` permettent l'interaction avec les transactions en attente du nœud. Nous définissons l'action HTTP `get` pour récupérer la liste des transactions en attente. Cette fois, nous définissons également l'action HTTP `post` pour ajouter une nouvelle transaction à la liste des transactions en attente. La fonction `entity(as[Transaction])` est utilisée pour désérialiser le corps `JSON` en un objet `Transaction`.

```scala
//Code...
lazy val mineRoutes: Route = pathPrefix("mine") {
    concat(
      pathEnd {
        concat(
          get {
            node ! Mine
            complete(StatusCodes.OK)
          }
        )
      }
    )
  }

//Code...
```

La dernière route est la `MineRoutes`. C'est une route très simple, utilisée uniquement pour demander au nœud Scalachain de commencer à miner un nouveau bloc. Nous définissons une action `get` puisque nous n'avons pas besoin d'envoyer quoi que ce soit pour démarrer le processus de minage. Il n'est pas nécessaire d'attendre une réponse, car cela peut prendre un certain temps, donc nous répondons immédiatement avec un statut `Ok`.

L'API pour interagir avec le nœud Scalachain est documentée [ici](https://documenter.getpostman.com/view/4636741/RWaHw8yx).

#### Conclusion

Avec la dernière section, nous avons conclu notre visite à l'intérieur de Scalachain. Ce prototype de blockchain est loin d'une implémentation réelle, mais nous avons appris beaucoup de choses intéressantes :

* Comment fonctionne une blockchain, au moins d'un point de vue de haut niveau.
* Comment utiliser la programmation fonctionnelle (Scala) pour construire une blockchain.
* Comment fonctionne le modèle d'acteur et son application à notre cas d'utilisation en utilisant le framework Akka.
* Comment utiliser la bibliothèque Akka HTTP pour créer un serveur pour exécuter notre blockchain, ainsi que les API pour interagir avec celle-ci.

Le code n'est pas parfait, et certaines choses peuvent être implémentées de manière meilleure. Pour cette raison, **n'hésitez pas à contribuer au projet !** ;-)