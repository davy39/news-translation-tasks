---
title: Démystifier la Monade en Scala
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-04T21:50:48.000Z'
originalURL: https://freecodecamp.org/news/demystifying-the-monad-in-scala-cc716bb6f534
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CRR3Lql_Mk2aTO54G-JQxg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: monads
  slug: monads
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: software development
  slug: software-development
seo_title: Démystifier la Monade en Scala
seo_desc: 'By Sinisa Louc

  In my previous post I mentioned how I decided to write about variance despite the
  fact that there are already several dozen articles about the topic. This is a similar
  situation. I am aware that this is a drop in the sea. I feel the se...'
---

Par Sinisa Louc

Dans mon [précédent article](https://medium.com/@sinisalouc/variance-in-java-and-scala-63af925d21dc#.xvhs1zq7p), j'ai mentionné comment j'ai décidé d'écrire sur la variance malgré le fait qu'il existe déjà plusieurs dizaines d'articles sur le sujet. C'est une situation similaire. Je suis conscient que cela ne représente qu'une goutte dans l'océan. Je pense que l'océan est pollué par des explications mathématiques complexes impliquant la théorie des catégories. Des explications ennuyeuses qui alignent une définition après l'autre sans fournir l'essentiel des choses.

Je ne vais pas entrer dans les détails techniques, et par techniques, je veux dire mathématiques. Stephen Hawking a dit qu'on lui avait conseillé que chaque équation qu'il mettait dans « Une brève histoire du temps » (un excellent livre, soit dit en passant) réduirait les ventes de moitié. Je vais suivre le même principe ici. Mais je vais aussi essayer de ne pas être trop simpliste, et par simpliste, je veux dire vague. Nous devons nous salir les mains. Enfin, mais pas des moindres, je vais fournir des exemples comme moyen principal d'explication. Les exemples sont plus un complément à l'explication principale.

#### Introduction

Alors, qu'est-ce qu'une monade ?

Vous pouvez penser aux monades comme à des **emballages**. Vous prenez simplement un objet et vous l'emballez avec une monade. C'est comme emballer un cadeau ; vous prenez une écharpe, un bon livre ou une montre élégante, et vous l'emballez avec du papier brillant et un ruban rouge. Nous emballons les cadeaux avec du papier brillant parce qu'ils ont l'air jolis. Nous emballons les objets avec des monades parce que les monades nous fournissent les deux opérations suivantes :

* **identité** (_return_ en Haskell, _unit_ en Scala)
* **bind** (_>>= en Haskell, flatMap en Scala)

Scala ne vient pas avec un type de monade intégré comme Haskell, donc nous allons modéliser la monade nous-mêmes. Si vous regardez certaines bibliothèques de programmation fonctionnelle cool comme [Scalaz](https://github.com/scalaz/scalaz), vous y trouverez des monades. Vous y trouverez également le reste de la famille de la théorie des catégories (functeurs, applicatifs, monoïdes, etc.). En Scala pur, il n'y a rien de tel prêt à l'emploi.

Nous allons modéliser une monade avec un trait générique qui fournit les méthodes unit() et flatMap(). Nous pouvons l'appeler M au lieu de Monad simplement pour être plus concis. La voici :

```
trait M[A] {
  def flatMap[B](f: A => M[B]): M[B]
}
  
def unit[A](x: A): M[A]
```

Vous voyez, elle fournit les deux fonctions mentionnées précédemment, _unit_ et _flatMap_. Ne vous inquiétez pas de leurs signatures, de ce qu'elles font pour l'instant ou de pourquoi la méthode unit() est à l'extérieur du corps du trait. Nous y viendrons dans un instant.

Maintenant, notez une chose très importante ici — il y a un **concept de monade** (que nous avons modélisé en Scala il y a une demi-minute). Il y a des **monades concrètes** de chair et de sang qui implémentent ces deux fonctions et font réellement quelque chose (par exemple, la monade IO). Parfois, les gens se réfèrent à une chose et parfois à l'autre, alors soyez prudent. Nous rencontrerons quelques monades concrètes plus tard dans cet article. Vous pouvez penser à une monade générique comme une interface et aux monades concrètes comme des implémentations.

Il y a une autre chose à laquelle vous devez prêter attention — les monades prennent un paramètre de type. Nous n'avons pas simplement écrit M ; nous avons écrit M[A]. Le paramètre de type est comme une étiquette collante sur notre emballage cadeau, indiquant quel type d'objet nous avons à l'intérieur (dans la vie réelle, cela gâcherait la surprise, mais en programmation, nous n'aimons pas les surprises). Donc, si nous voulons emballer un objet avec notre emballage monade, nous devons paramétrer la monade avec le type de l'objet sous-jacent, par exemple M[Int], M[String], M[MyClass], etc.

Maintenant, examinons de plus près ces deux fonctions.

#### Fonctions de la monade

Au cas où vous nous auriez rejoints, laissez-moi répéter que les monades viennent avec deux opérations, _unit_ (également connu sous le nom d'_identity_ ou _return_) et _flatMap_ (également connu sous le nom de _bind_). D'ailleurs, la littérature et les sources en ligne regorgent de toutes sortes de noms. J'ai simplement mentionné les plus courants. Attendez, j'en ai oublié un — unit est aussi souvent appelé _pure_. Mais ne vous inquiétez pas, il est toujours assez simple de savoir à quelle fonction on fait référence, peu importe le nom utilisé. Oh, ils utilisent aussi _zero_ pour unit parfois. Bon, passons à autre chose.

Unit effectue la partie emballage. Donc, dans le cas de notre analogie avec l'emballage cadeau, nous pouvons passer un livre à unit(). Il nous retournera notre livre emballé dans ce super papier brillant coloré, avec une étiquette « livre » dessus. Et dans le cas de notre trait monade, si nous lui donnons une valeur de type A, il nous retournera une valeur de type M[A]. C'est une sorte de constructeur de monade, si vous voulez.

Il devrait être clair à ce stade pourquoi nous avons défini la méthode unit() à l'extérieur du corps du trait. Parce que nous ne voulons pas l'invoquer sur l'objet monadique existant (par exemple, myMonad.unit("myBook")). Cela n'aurait pas beaucoup de sens. Nous la voulons comme une méthode statique autonome (par exemple, unit("myBook")). En passant notre livre à unit(), nous le récupérons emballé dans une monade.

Maintenant, à propos de flatMap. Vous êtes peut-être déjà familier avec lui ; c'est le même flatMap que vous pouvez rencontrer dans d'autres endroits en Scala, comme les collections. Voici sa signature :

```
def flatMap[B](f: (A) => U[B]): U[B]
```

Disons que U est une List. Cela fonctionne pour divers autres types, mais nous utiliserons List pour cet exemple. Maintenant, ce que fait flatMap, c'est qu'il prend une fonction avec la signature A _→_ List[B] et il utilise cette fonction pour transformer l'objet sous-jacent de type A en un List[B]. Cette opération est connue sous le nom de _map_. Puisque nous avons transformé notre A sous-jacent en un List[B], cela nous laisse avec un List[List[B]]. Mais nous n'avons pas utilisé map() ordinaire — nous avons utilisé flatMap(). Cela signifie que le travail n'est pas encore terminé ; flatMap va maintenant « aplatir » notre List[List[B]] en List[B].

Regardons un exemple concret. Si A est Int, et que notre fonction _f_ est

```
val f = (i: Int) => List(i - 1, i, i + 1)
```

alors nous pouvons flatMap une liste d'entiers avec _f_ comme suit :

```
val list = List(5, 6, 7)
println(list.flatMap(f))
// imprime List(4, 5, 6, 5, 6, 7, 6, 7, 8)
```

Notez que map() régulier prendrait chaque nombre _i_ et l'étendrait à une mini-liste _(prédécesseur, nombre original, successeur)_ ce qui nous donnerait la liste de mini-listes suivante : List((4, 5, 6), (5, 6, 7), (6, 7, 8)). FlatMap va plus loin ; il aplatit cela en une longue liste, résultant en 
List(4, 5, 6, 5, 6, 7, 6, 7, 8).

Maintenant, disons que nous avons une classe M avec un type sous-jacent A, écrite comme M[A]. Si nous voulons [flatMap that sh*t](http://1.bp.blogspot.com/-f5T38j9evCk/VZ54cIBwUeI/AAAAAAAABLY/3bvMZaQ4HCY/s640/nzfiq.jpg) (je n'ai pas inventé cette phrase ; essayez de la googler), nous devons fournir une fonction A _→_ M[B]. FlatMap utilisera alors cette fonction pour transformer notre A sous-jacent en M[B], résultant en un M[M[B]], puis il aplatira le tout en M[B].

```
         map avec A => M[B]                  flatten
M[A]  ------------------------->  M[M[B]]  -----------> M[B]
```

Remarquez comment flatMap ne nécessite pas une fonction A _→_ M[A], mais une plus flexible, A _→_ M[B]. Donc si M est une List et A est un Int, nous pouvons alimenter le flatMap avec des fonctions telles que Int _→_ List[String], Int _→_ List[MyClass] et ainsi de suite. Cela n'a pas besoin d'être Int _→_ List[Int]. Par exemple, nous aurions pu définir _f_ comme :

```
val f = (i: Int) => List("pred=" + (i - 1), "succ=" + (i + 1))
```

et ensuite nous aurions pu flatMap une liste d'entiers avec elle comme ceci :

```
val list = List(5, 6, 7)
println(list.flatMap(f))
// imprime List(pred=4, succ=6, pred=5, succ=7, pred=6, succ=8)
```

FlatMap est bien plus puissant que map. Il nous donne la capacité de chaîner des opérations ensemble, comme vous le verrez dans la section des exemples. La fonctionnalité de map est juste un sous-ensemble de la fonctionnalité de flatMap. Si vous voulez avoir map() disponible dans votre monade, vous pouvez l'exprimer en utilisant les méthodes existantes de la monade flatMap() et unit() comme ceci (notez que _g_ est une fonction _Int → Something_, pas _Int → List[Something]_) :

```
  m map g = flatMap(x => unit(g(x)))
```

Si tout ce que nous avions était map et unit, nous ne serions pas capables de définir flatMap car ni l'un ni l'autre n'a la moindre idée de l'aplatissement. Flatten (également connu sous le nom de _join_ en Haskell) est une partie très importante du processus dans notre machine monade. Si nous avions un map, mais aucune capacité à aplatir (et donc pas de flatMap), alors nous nous retrouverions avec ce qui est connu dans la théorie des catégories sous le nom de _functor_. Les foncteurs sont assez cool aussi, mais les monades sont la star de notre spectacle, alors ne digressons pas.

D'ailleurs, si nous décomposons _flatMap_ en _map_ (_fmap_) et _flatten_ (_join_), nous créerons une [définition complètement équivalente](https://en.wikipedia.org/wiki/Monad_%28functional_programming%29#fmap_and_join) et valide de la monade. Cette définition ressemblerait alors à ceci :

* def unit: A → F[A]
* def map: F[A] → (A → B) → F[B]
* def flatten: F[F[A]] → F[A]

Notez que j'ai écrit la signature de _map_ comme une fonction complètement autonome, « neutre ». Ce qui signifie qu'elle est définie sans aucun contexte supplémentaire au lieu d'être une méthode sur F[A].

Un tel _map_ prend d'abord une instance de F[A] (par exemple, List(42)), puis une fonction A → B (comme a → a + 1) et ensuite nous donne une instance de F[B] (dans notre cas List(43)). Je l'ai écrit de cette manière seulement pour pouvoir écrire la signature correspondante de _flatten_ également. Si j'avais écrit map simplement comme A → B, en supposant qu'il est défini comme une méthode sur F[A], alors j'aurais eu du mal à écrire la signature pour _flatten_. Il aurait fallu que ce soit une fonction Unit → F[A], définie uniquement sur les instances de F[F[A]], ce qui rend les choses maladroites. En écrivant les signatures « neutres », les choses devraient être claires.

Quoi qu'il en soit, nous allons nous en tenir à la version flatMap, et nous allons continuer à voir la signature de _map_ comme A → B au lieu de F[A] → A → B, ce qui signifie que F[A] est déjà connu au moment de l'invocation (c'est l'instance sur laquelle nous invoquons la méthode map()).

#### Exposer la monade

Comme je l'ai dit plus tôt, il n'y a pas de classe de type monade en Scala. Mais _cela ne signifie pas qu'il n'y a pas de monades en Scala_. La monade n'est pas une classe ou un trait ; la monade est un concept. Chaque « emballage » qui nous fournit nos deux opérations chéries, _unit_ et _flatMap_, est essentiellement une monade (bien, ce n'est pas vraiment suffisant de simplement fournir des méthodes avec ces noms, elles doivent, bien sûr, suivre certaines lois, mais nous y viendrons).

Je pense que nous pouvons maintenant enfin mettre les deux et deux ensemble et réaliser que **List est une monade** ! Laissez cela couler. Quel rebondissement, hein ? C'est comme dans ce film où vous réalisez que c'était *lui* tout le temps. Mais attendez — il y en a d'autres ! Set ? Monade. Option ? Monade. Future ? Monade !(*)

D'accord, c'est un film de conspiration de masse. Les monades sont partout !

_(*): Il y a une légère controverse sur le fait que Future soit vraiment une monade ou non. Puisque c'est un texte pour débutants, je vais simplement dire que c'est une monade et en rester là._

_Au cas où quelqu'un du camp Future-n'est-pas-une-vraie-monade lit ceci, je suis sûr que vous serez d'accord pour dire que ce n'est pas le lieu pour ce débat. Peut-être que j'écrirai même un article là-dessus aussi un jour._

_Je suis d'accord pour dire que leur rupture de certains principes fondamentaux de la programmation fonctionnelle comme la transparence référentielle ne devrait pas passer inaperçue. Mais laissons cela pour une autre fois._

Lorsque vous les regardez de près, vous pouvez voir que chacune d'entre elles a effectivement une méthode flatMap. Et unit ? Eh bien, rappelez-vous que unit est une opération qui crée une monade M[A] à partir d'un objet de type A. Cela signifie qu'un simple apply() sert de unit parfaitement bon. Donc si nous avons un objet appelé x, voici à quoi ressemble l'opération unit dans diverses monades (rappelons qu'il y a une syntaxe sucrée qui nous permet d'invoquer par exemple List.apply(3) comme List(3)) :

```
List:          Set:          Option:                 Future:
------------------------------------------------------------------
List(x)        Set(x)        Some(x) ou Option(x)    Future(x)
```

De plus, comme je l'ai dit plus tôt, il n'y a pas de classe de type monade réelle en Scala pur. Des constructions comme List, Option, Future, etc., n'étendent aucun trait Monad spécial (il n'existe pas). Cela signifie qu'elles ne sont pas obligées de nous fournir des méthodes appelées _unit_ et _flatMap_. C'est en les observant et en voyant qu'elles ont des méthodes unit() et flatMap() avec des signatures et un comportement corrects que nous pouvons déduire qu'elles sont, en fait, des monades.

Je vous entends dire « mais s'il n'y a pas de méthode unit() réelle en Scala (puisque nous avons dit que apply() dans l'objet compagnon de la monade sert de unit), que vouliez-vous dire par _return_ en Haskell, _unit_ en Scala ? Quoi, _unit_ est un nom pour une fonction qui n'existe pas ? »

C'est une bonne observation, et oui, vous avez tout à fait raison. « Unit » est simplement une convention pour référencer l'opération d'identité de la monade en Scala. Vous pouvez créer une monade personnalisée parfaitement bonne et appeler ses méthodes _galvanize_ et _dropTheBass_ au lieu de _unit_ et _flatMap_ si vous le souhaitez. Tant qu'elles ont des signatures appropriées et font ce qu'elles sont censées faire, ce sera conceptuellement une monade. Mais la convention est une bonne chose, et la communauté Scala a adopté les termes _flatMap_ (comme vu dans List, Option, Future) pour l'opération de liaison et _unit_ (par convention implémenté comme apply()) pour l'opération d'identité.

J'ai dit, « tant qu'elles ont des signatures appropriées et font ce qu'elles sont censées faire ». D'accord, nous avons couvert la partie des signatures, mais nous n'avons jamais vraiment spécifié ce que ces méthodes doivent faire exactement. Je veux dire, nous avons _discuté_ de la manière dont elles devraient se comporter, mais ce n'est pas vraiment suffisant pour définir leurs exigences en termes plus concrets. C'est là que les **lois des monades** entrent en jeu. Ces lois doivent être respectées par _unit_ et _flatMap_ si notre monade doit être une vraie monade.

Puisque c'est un texte pour débutants, je ne vais pas entrer dans trop de détails sur la théorie derrière les lois ou même démontrer leur exactitude. Pour l'instant, il est important que vous sachiez qu'elles existent. Ce n'est pas grave si vous reportez leur étude jusqu'à ce que vous ayez un peu de pratique.

Donc, si nous avons une valeur de base _x_, une instance de monade _m_ (contenant une certaine valeur) et des fonctions _f_ et _g_ de type _Int → M[Int]_, nous pouvons écrire les lois comme suit :

* **loi d'identité à gauche** :   
_unit(x).flatMap(f) == f(x)_
* **loi d'identité à droite** :   
_m.flatMap(unit) == m_
* **loi d'associativité** :  
_m.flatMap(f).flatMap(g) == m.flatMap(x → f(x).flatMap(g))_

Très bien. Jusqu'à présent, nous avons atteint deux des trois objectifs que je visais dans cet article. Nous avons expliqué le concept de monade et nous avons établi un parallèle avec certaines monades de la vie réelle en Scala. D'ailleurs, au début, je n'ai mentionné que la monade IO comme exemple de monade concrète. Je voulais reporter la mention des autres jusqu'à ce que vous ayez une idée du concept général.

Au cas où vous vous demandez ce que diantre est une monade IO, c'est une petite chose assez complexe utilisée pour les opérations d'E/S dans les langages purement fonctionnels comme Haskell. Ce n'est ni le moment ni l'endroit pour approfondir celle-ci.

Il est temps pour le troisième objectif — pourquoi les monades sont-elles utiles ?

#### Monades en pratique : Option

Dans cette section, je vais montrer deux monades, Option et Future.

Nous commençons par Option. Comme vous le savez probablement, Option est une construction qui nous permet d'éviter les pointeurs nuls en Scala (en Haskell, c'est appelé Maybe). Nous l'utilisons pour des choses qui peuvent ou non avoir une valeur définie. Si une valeur est définie, option est égale à Some(value), et si elle n'est pas définie, elle est égale à None.

Disons que nous avons un tas d'utilisateurs stockés dans une base de données. Nous avons également un service qui peut charger un utilisateur à partir de cette base de données avec une méthode loadUser(). Il prend un nom et nous fournit un Option[User] car l'utilisateur avec ce nom peut ou non exister.

Chaque utilisateur peut ou non avoir un enfant (pour les besoins de l'exemple, disons qu'il y a une loi appliquée dans l'état qui permet un maximum d'un enfant). Notez que l'enfant est également de type User, donc il peut avoir un enfant aussi.

Enfin, mais pas des moindres — nous avons une fonction simple _getChild_ qui retourne l'enfant pour un utilisateur donné.

```
trait User {
  val child: Option[User]
}

object UserService {
  def loadUser(name: String): Option[User] = { /** get user **/ }
}

val getChild = (user: User) => user.child
```

Maintenant, disons que nous voulons charger un utilisateur à partir de la base de données et, s'ils existent, nous voulons voir s'ils ont un petit-enfant. Nous devons invoquer ces trois fonctions :

String _→_ Option[User] // charger depuis la base de données  
User _→_ Option[User] // obtenir l'enfant  
User _→_ Option[User] // obtenir l'enfant de l'enfant

Et voici le code.

```
val result = UserService.loadUser("mike")
  .flatMap(getChild)
  .flatMap(getChild)
```

Si vous ne saviez pas comment flatMap une monade, vous auriez probablement écrit quelques branches if-then-else imbriquées, vérifiant si l'option est définie. Rien de mal à cela, mais ceci est bien plus élégant, concis et dans l'esprit de la programmation fonctionnelle.

D'accord, examinons de plus près notre monade « utilisateur optionnel ». Rappelez-vous ce que nous avons appris plus tôt. Voici l'analogie.

```
generic monad:
--------------
unit:     A => M[A]           
flatMap: (A => M[B]) => M[B]

our monad:
-------------- 
unit:     User => Option[User]
flatMap: (User => Option[User]) => Option[User]
```

D'ailleurs, vous pouvez également écrire ces fonctions sous forme de fonctions lambda en place au lieu de les définir a priori. Ensuite, le code devient ceci :

```
val result = UserService.loadUser("mike")
  .flatMap(user => user.child)
  .flatMap(user => user.child)
```

ou même plus concis :

```
val result = UserService.loadUser("mike")
  .flatMap(_.child)
  .flatMap(_.child)
```

Vous pouvez également utiliser une compréhension for qui est essentiellement du sucre syntaxique pour mapper, flatMapper et filtrer. Je ne veux pas trop m'égarer, donc je ne vais pas l'expliquer ici, vous pouvez le chercher ; je vais simplement vous montrer le code.

```
val result = for {
  user             <- UserService.loadUser("mike)
  usersChild       <- user.child
  usersGrandChild  <- usersChild.child
} yield usersGrandChild
```

Si vous trouvez tout cela un peu confus, bidouiller avec votre propre code aide beaucoup. Vous pouvez créer des utilisateurs factices, ajouter une implémentation de base à UserService.loadUser() pour qu'elle retourne l'un d'eux. Faites-leur avoir une tonne d'enfants et de petits-enfants et flatMappez-les sans relâche.

#### Monades en pratique : Future

Future est un wrapper autour d'une opération asynchrone. Une fois que le future a été complété, vous pouvez faire ce que vous devez faire avec son résultat.

Il y a deux principales façons d'utiliser un future :

* utiliser future.onComplete() pour définir un callback qui travaillera avec le résultat du future (pas très cool)
* utiliser future.flatMap() pour simplement dire quelles opérations doivent être effectuées sur le résultat une fois que le future est complet (plus propre et plus puissant puisque vous pouvez retourner le résultat de la dernière opération)

Passons à notre exemple. Nous avons une boutique en ligne et des clients qui ont passé des milliers de commandes. Pour chaque client, nous devons maintenant obtenir sa commande, vérifier quel article la commande concerne, obtenir l'article correspondant de la base de données, effectuer l'achat et écrire le résultat de l'opération d'achat dans le journal. Voyons cela en code.

```
// nécessaire pour que les Futures fonctionnent
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

trait Order
trait Item
trait PurchaseResult
trait LogResult
object OrderService {  
  def loadOrder(username: String): Future[Order] 
}

object ItemService {  
  def loadItem(order: Order): Future[Item] 
}

object PurchasingService { 
  def purchaseItem(item: Item): Future[PurchaseResult]
  def logPurchase(purchaseResult: PurchaseResult): Future[LogResult] 
}
```

D'ailleurs, ne vous souciez pas de choses comme référencer des objets globaux depuis l'intérieur des fonctions. Je sais que ce n'est pas la meilleure pratique. Mais cela est complètement à côté de la question ici. De plus, notez que le code ci-dessus ne compile pas car j'ai omis les implémentations des méthodes de service pour plus de clarté. Encore une fois, si vous voulez jouer avec l'exemple vous-même (et je le recommande), vous pouvez créer des implémentations factices vous-même. Par exemple, def loadItem(order: Order) = Future(new Item{}).

Maintenant, de manière similaire à l'exemple Option, il y a quelques fonctions que nous allons utiliser. Elles sont assez triviales car chacune invoque simplement une méthode du service correspondant.

```
val loadItem: Order => Future[Item] = {
  order => ItemService.loadItem(order)
}

val purchaseItem: Item => Future[PurchaseResult] = {
  item => PurchasingService.purchaseItem(item)
}

val logPurchase: PurchaseResult => Future[LogResult] = {
  purchaseResult => PurchasingService.logPurchase(purchaseResult)
}
```

Nous devons charger la commande pour un client donné, obtenir l'article en question, effectuer l'achat de cet article et journaliser le résultat. C'est aussi simple que :

```
val result = 
  OrderService.loadOrder("customerUsername")
  .flatMap(loadItem)
  .flatMap(purchaseItem)
  .flatMap(logPurchase)
```

Voici l'alternative tout aussi agréable de la compréhension for, utilisant des invocations directes de méthodes de service au lieu des fonctions qui ont été utilisées ci-dessus :

```
val result =
  for {
    loadedOrder    <- orderService.loadOrder("customerUsername")
    loadedItem     <- itemService.loadItem(loadedOrder)
    purchaseResult <- purchasingService.purchaseItem(loadedItem)
    logResult      <- purchasingService.logPurchase(purchaseResult)
  } yield logResult
```

C'est tout. J'espère avoir réussi à éclairer le mystère des monades.

#### Conclusion

La monade avec ses deux armes, unit et flatMap, est un gars assez puissant. Bien sûr, elles ne sont pas la solution à _tous_ vos problèmes. Mais penser de cette manière (enchaîner des opérations et manipuler des données en utilisant map, flatMap, filter, etc., accompagnés d'autres constructions de programmation fonctionnelle comme le pattern matching) améliore vraiment votre raisonnement sur le code et réduit le nombre de bugs.

Et étant donné que le code est beaucoup plus souvent lu qu'écrit, la lisibilité et la clarté d'un tel code sont un grand plus. Par exemple, voici un extrait du code que j'ai écrit au travail aujourd'hui (j'ai changé les noms) :

```
itemService.loadItems(order).flatMap {

  case Success(items) =>
    val updateResults = items.map { item =>
      itemService.purchase(item, order.owner)
    }
    Future.sequence(updateResults)
      .map(toPurchaseResults(_))
      .map(mergeResults(_))
      
  case RepositoryFailure(failure) =>
    Future(Failure(Json.obj(Failed -> FailureLoadingItems)))
    
}
```

Oubliez les branches if emmêlées, les boucles imbriquées avec leurs erreurs de décalage et [l'enfer des callbacks](http://callbackhell.com/). Ce code est plus simple, plus joli et, avec un peu d'aide du compilateur Scala, _fonctionne la première fois que vous l'exécutez_.

Vous pouvez apercevoir quelques autres constructions de la théorie des catégories [ici](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html) ou opter pour une lecture plus détaillée [ici](http://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/).

En ce qui concerne la programmation fonctionnelle en général, si vous aimez Scala, vous pourriez commencer par [ici](https://www.manning.com/books/functional-programming-in-scala).

Il y a aussi quelques bibliothèques sympas qui fournissent des constructions de programmation fonctionnelle, comme [Scalaz](https://github.com/scalaz/scalaz) (qui a déjà été mentionné plus tôt) et [Cats](https://github.com/non/cats) (le nouveau venu sur le bloc), alors essayez de jouer avec elles ; vous pouvez trouver quelques tutoriels [ici](http://eed3si9n.com/).

Et si vous voulez vous impliquer sérieusement dans la programmation fonctionnelle, vous devrez [apprendre Haskell](http://learnyouahaskell.com/chapters) tôt ou tard (au cas où vous ne le connaissez pas déjà).

Voici mon email : sinisalouc[at]gmail[dot]com. Si vous trouvez des erreurs, pensez qu'une partie spécifique a besoin d'amélioration ou souhaitez simplement entrer en contact, n'hésitez pas à me contacter.