---
title: Une introduction aux tests de lois en Scala
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T16:48:22.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-law-testing-in-scala-4243d72272f9
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca2eb740569d1a4ca57e8.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Une introduction aux tests de lois en Scala
seo_desc: 'By dor sever

  Property-based law testing is one of the most powerful tools in the scala ecosystem.
  In this post, I’ll explain how to use law testing and the value it’ll give you using
  in-depth code examples.

  This post is aimed for Scala developers who...'
---

Par dor sever

Les tests basés sur les propriétés des lois sont l'un des outils les plus puissants de l'écosystème Scala. Dans cet article, je vais expliquer comment utiliser les tests de lois et la valeur qu'ils vous apporteront en utilisant des exemples de code approfondis.

Cet article s'adresse aux développeurs Scala qui souhaitent améliorer leurs connaissances et compétences en matière de tests. Il suppose une certaine connaissance de Scala, de cats et d'autres bibliothèques fonctionnelles.

![Image](https://cdn-media-1.freecodecamp.org/images/GpUIRfAe79BTz8JGTvk0oOD376oxjBxj4CiS)

#### **Introduction**

* Vous êtes peut-être familier avec les types qui sont un ensemble de valeurs (par exemple, les valeurs Int sont : `1,2,3`… Les valeurs String sont : `John Doe` etc).
* Vous êtes peut-être également familier avec les fonctions qui sont un mappage d'un type d'entrée vers un type de sortie.
* Une propriété est définie sur un type ou une fonction et décrit son comportement souhaité.

Alors, qu'est-ce qu'une Loi ? **Continuez à lire !**

#### **Un exemple concret**

Voici notre type de données bien-aimé `_Person_` :

```
case class Person(name: String, age: Int)
```

Et le code de sérialisation utilisant `Play-Json`, une bibliothèque qui permet de transformer votre type `Person` en `JSON` :

```scala
val personFormat: OFormat[Person] = new OFormat[Person] {
  override def reads(json: JsValue): JsResult[Person] = {
    val name = (json \ "name").as[String]
    val age = (json \ "age").as[Int]
    JsSuccess(Person(name, age))
  }
  override def writes(o: Person): JsObject =
    JsObject(Seq("name" -> JsString(o.name), 
                 "age" -> JsNumber(o.age)))
}
```

Nous pouvons maintenant tester cette fonction de sérialisation sur une entrée spécifique comme ceci :

```scala
import org.scalatest._
class PersonSerdeSpec extends WordSpecLike with Matchers {
  "should serialize and deserialize a person" in {
    val person = Person("John Doe", 32)
    val actualPerson =
      personFormat.reads(personFormat.writes(person))
    actualPerson.asOpt.shouldEqual(Some(person))
  }
}
```

Mais nous devons maintenant nous demander si toutes les personnes seront sérialisées avec succès ? Qu'en est-il d'une personne avec des données invalides (comme un âge négatif) ? Voudrons-nous répéter ce processus de réflexion pour trouver des cas limites pour toutes nos données de test ?

Et surtout, ce code restera-t-il lisible dans le temps ? (par exemple : changer le type de données `person` [ajouter un champ `LastName`], répéter les tests pour d'autres types de données, etc)

> « Nous pouvons résoudre n'importe quel problème en introduisant un niveau supplémentaire d'indirection ».

### Tests basés sur les propriétés

La première arme à notre disposition est le test basé sur les propriétés (PBT). Le PBT fonctionne en définissant une propriété, qui est une spécification de haut niveau du comportement qui doit être valable pour toutes les valeurs du type spécifique.

Dans notre exemple, la **propriété** sera :

* Pour chaque personne p, si nous la sérialisons et la désérialisons, nous devrions obtenir la même personne.

Écrire cette propriété en utilisant ScalaCheck ressemble à ceci :

```scala
object PersonSerdeSpec extends org.scalacheck.Properties("PersonCodec") {
  property("round trip consistency") = 
    org.scalacheck.Prop.forAll { a: Person =>
      personFormat.reads(personFormat.writes(a)).asOpt.contains(a)
    }
}
```

La vérification de la propriété nécessite un moyen de générer des personnes. Cela se fait en utilisant un `Arbitrary[Person]` qui peut être défini comme ceci :

```scala
implicit val personArb: Arbitrary[Person] = Arbitrary {
  for {
    name <- Gen.alphaStr
    age  <- Gen.chooseNum(0, 120)
  } yield Person(name, age)
}
```

De plus, nous pouvons utiliser `scalacheck-shapeless` - une bibliothèque incroyable qui élimine (presque) tous les besoins pour la définition de type arbitraire verbeuse (plutôt désordonnée et très sujette aux bugs) en la générant pour nous !

![Image](https://cdn-media-1.freecodecamp.org/images/XgoIxileqrYUmSnMMkzuGFJJCkxvy6-Ryj-Q)

Cela peut être fait en ajoutant :

```
libraryDependencies += "com.github.alexarchambault" %% "scalacheck-shapeless_1.14" % "1.2.0"
```

et en important ce qui suit dans notre code :

```
import org.scalacheck.ScalacheckShapeless._
```

Et ensuite, nous pouvons supprimer l'instance `_personArb_` que nous avons définie précédemment.

### La loi du Codec

Essayons d'abstraire davantage en définissant les **lois** de notre type de données :

```scala
trait CodecLaws[A, B] {
  def serialize: A => B
  def deserialize: B => A
  def codecRoundTrip(a: A): Boolean = serialize.
andThen(deserialize)(a) == a
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/De-BSLaDLDfZvMXrdBFzwvufzCyHVTONXTTg)

Cela signifie que, étant donné :

* Les types `A, B`
* Une fonction de `A` vers `B`
* Une fonction de `B` vers `A`

Nous définissons une fonction appelée `codecRoundTrip` qui prend un `a: A` et le fait passer à travers les fonctions et s'assure que nous obtenons la même valeur de type A en retour.

Cette loi stipule (sans révéler **aucun détail d'implémentation**) que le voyage aller-retour que nous effectuons sur l'entrée donnée ne perd aucune information.

> Une autre façon de dire cela est de prétendre que nos types A et B sont isomorphes.

Nous pouvons abstraire encore plus en utilisant la bibliothèque cats-laws avec la classe de cas `IsEq` pour définir une description d'égalité.

```scala
import cats.laws._
trait CodecLaws[A, B] {
  def serialize: A => B
  def deserialize: B => A
  def codecRoundTrip(a: A): cats.laws.IsEq[A] = serialize.andThen(deserialize)(a) <-> a
}
/** Représente deux valeurs du même type qui sont censées être égales. */
final case class IsEq[A](lhs: A, rhs: A)
```

Ce que nous obtenons de ce type et de cette syntaxe est une **description** **de l'égalité** entre les deux valeurs au lieu du résultat de l'égalité comme avant.

### Le test du Codec

Il est temps de tester les lois que nous venons de définir. Pour ce faire, nous utiliserons la bibliothèque [discipline](https://github.com/typelevel/discipline).

```
import cats.laws.discipline._
import org.scalacheck.{ Arbitrary, Prop }
trait CodecTests[A, B] extends org.typelevel.discipline.Laws {
  def laws: CodecLaws[A, B]
  def tests(
    implicit
    arbitrary: Arbitrary[A],
    eqA: cats.Eq[A]
  ): RuleSet =
    new DefaultRuleSet(
      name   = name,
      parent = None,
      "roundTrip" -> Prop.forAll { a: A =>
        laws.codecRoundTrip(a)
      }
    )
}
```

Nous définissons un trait CodecTest qui prend 2 paramètres de type `A` et `B`, qui dans notre exemple seront `Person` et `JsResult`.

Le trait contient une instance des lois et définit une méthode de test qui prend un `Arbitrary[A]` et un vérificateur d'égalité (de type `Eq[A]`) et retourne un `rule-set` pour que `scalacheck` l'exécute.

Notez que aucun test ne s'exécute réellement ici. Cela nous donne le pouvoir d'exécuter ces tests qui sont définis une seule fois pour tous les types que nous voulons.

Nous pouvons maintenant nous engager sur un type et une implémentation spécifiques (comme la sérialisation `Play-Json`) en instantiant un `CodecTest` avec les types appropriés.

```scala
object JsonCodecTests {
  def apply[A: Arbitrary](implicit format: Format[A]): CodecTests[A, JsValue] =
    new CodecTests[A, JsValue] {
      override def laws: CodecLaws[A, JsValue] =
        CodecLaws[A, JsValue](format.reads, format.writes)
    }
}
```

#### Une (type) digression

Mais maintenant nous obtenons l'erreur :

```scala
Error:(11, 38) type mismatch;
 found   : play.api.libs.json.JsResult[A]
 required: A
```

Nous nous attendions à ce que les types circulent de :

```
  A  =>  B  =>  A
```

Mais les types Play-Json vont de :

```
 A  =>  JsValue  =>  JsResult[A]
```

Cela signifie que notre fonction de désérialisation peut réussir ou échouer et ne retournera pas toujours un A, mais plutôt un conteneur de A.

Pour abstraire les types, nous devons maintenant utiliser la syntaxe du constructeur de type `F[_]` :

```scala
trait CodecLaws[F[_],A, B] {
  def serialize: A => B
  def deserialize: B => F[A]
  def codecRoundTrip(a: A)(implicit app:Applicative[F]): IsEq[F[A]] =
    serialize.andThen(deserialize)(a) <-> app.pure(a)
}
```

L'instance `Applicative` est utilisée pour prendre une valeur simple de type A et la lever dans le contexte `Applicative` qui retourne une valeur de type `F[A]`.

> Ce processus est similaire à prendre une valeur `x` et la lever dans un contexte `Option` en utilisant `Some(x)`, ou dans notre exemple concret, prendre une valeur `a:A` et la lever dans le type `JsResult` en utilisant `[JsSuccess](https://www.playframework.com/documentation/2.7.0/api/scala/play/api/libs/json/JsSuccess.html)(a)`.

Nous pouvons maintenant terminer l'implémentation pour `CodecTests` et `JsonCodecTests` comme ceci :

```scala
trait CodecTests[F[_], A, B] extends org.typelevel.discipline.Laws {
  def laws: CodecLaws[F, A, B]
  def tests(
    implicit
    arbitrary: Arbitrary[A],
    eqA: cats.Eq[F[A]],
    applicative: Applicative[F]
  ): RuleSet =
    new DefaultRuleSet(
      name   = name,
      parent = None,
      "roundTrip" -> Prop.forAll { a: A =>
        laws.codecRoundTrip(a)
      }
    )
}
object JsonCodecTests {
  def apply[A: Arbitrary](implicit format: Format[A]): CodecTests[JsResult, A, JsValue] =
    new CodecTests[JsResult, A, JsValue] {
      override def laws: CodecLaws[JsResult, A, JsValue] =
        CodecLaws[JsResult, A, JsValue](format.reads, format.writes)
    }
}
```

Et pour définir un test de sérialisation `Person` fonctionnel en **1 ligne de code** :

```scala
import JsonCodecSpec.Person
import play.api.libs.json._
import org.scalacheck.ScalacheckShapeless._
import org.scalatest.FunSuiteLike
import org.scalatest.prop.Checkers
import org.typelevel.discipline.scalatest.Discipline
class JsonCodecSpec extends Checkers with FunSuiteLike with Discipline { 
  checkAll("PersonSerdeTests", JsonCodecTests[Person].tests)
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/imdSWbMKWX8xBSGWLXuMy-iB04TAGBkgqg5l)

### Le pouvoir de l'abstraction

Nous avons pu définir nos tests et lois sans révéler aucun détail d'implémentation. Cela signifie que nous pouvons passer à l'utilisation d'une bibliothèque différente pour la sérialisation demain et toutes nos lois et tests seront toujours valables.

#### Un autre exemple

Nous pouvons tester cette théorie en ajoutant la prise en charge de la sérialisation BSON en utilisant la bibliothèque `reactive-mongo` :

```scala
import cats.Id
import io.bigpanda.laws.serde.{ CodecLaws, CodecTests }
import org.scalacheck.Arbitrary
import reactivemongo.bson.{ BSONDocument, BSONReader, BSONWriter }
object BsonCodecTests {
  def apply[A: Arbitrary](
    implicit
    reader: BSONReader[BSONDocument, A],
    writer: BSONWriter[A, BSONDocument]
  ): CodecTests[Id, A, BSONDocument] =
    new CodecTests[Id, A, BSONDocument] {
      override def laws: CodecLaws[Id, A, BSONDocument] =
        CodecLaws[Id, A, BSONDocument](reader.read, writer.write)
      override def name: String = "BSON serde tests"
    }
}
```

Les types ici circulent de :

```
A => BsonDocument => A
```

et non `F[A]` comme nous l'avions prévu. Heureusement pour nous, nous avons une solution et utilisons le type Id pour représenter cela.

Et étant donné la définition (très longue) du sérialiseur :

```scala
implicit val personBsonFormat
  : BSONReader[BSONDocument, Person] with BSONWriter[Person, BSONDocument] =
  new BSONReader[BSONDocument, Person] with BSONWriter[Person, BSONDocument] {
    override def read(bson: BSONDocument): Person =
      Person(bson.getAs[String]("name").get, bson.getAs[Int]("age").get)
    override def write(t: Person): BSONDocument =
      BSONDocument("name" -> t.name, "age" -> t.age)
  }
```

nous pouvons maintenant définir BsonCodecTests dans toute sa **1** ligne de logique gloire.

```scala
class BsonCodecSpec extends Checkers with FunSuiteLike with Discipline {
    checkAll("PersonSerdeTests", BsonCodecTests[Person].tests)
}
```

### Une perspective de logique du premier ordre sur notre code

Notre première tentative de test peut être décrite comme suit :

```
∃p:Person,s:OFormat qui tient : s.read(s.write(p)) <-> p
```

Cela signifie, `pour la personne spécifique p(John Doe,32)` et `pour le format **s**`, l'énoncé suivant est vrai : `decode(encode(p)) <-`> p.

La deuxième tentative (en utilisant `PBT`) peut être :

```
∃s:OFormat, ∀p:Person ce qui suit doit tenir : s.read(s.write(p)) <-> p
```

Ce qui signifie, **pour toutes** les personnes p et `pour le format spécifique **s**`, ce qui suit est vrai : `decode(encode(p))<`->p.

La troisième (et la plus puissante à ce jour) en utilisant `law testing` :

```
∀s:Encoder, ∀p:Person ce qui suit doit tenir : s.read(s.write(p)) <-> p
```

Ce qui signifie, `pour tous` `les formats s`, et `**pour toutes** les personnes p`, ce qui suit est vrai : `decode(encode(p))<`->p.

#### **Résumé**

* Les tests de lois vous permettent de raisonner sur vos types de données et fonctions de manière mathématique et concise et fournissent un paradigme totalement nouveau pour tester votre code !
* La plupart des bibliothèques de niveau de type que vous utilisez (comme `cats`, `circe` et bien d'autres) utilisent les tests de lois en interne pour tester leurs types de données.
* Évitez d'écrire des cas de test spécifiques pour vos types de données et fonctions et essayez de les généraliser en utilisant des tests de lois basés sur les propriétés.

Merci d'être arrivé jusqu'ici ! Je suis super excité à l'idée de trouver des lois plus abstraites et utiles que je peux utiliser dans mon code ! Veuillez me faire savoir celles que vous avez utilisées ou auxquelles vous pouvez penser.

Plus de contenu inspirant et détaillé peut être trouvé sur le site [cats-laws](https://typelevel.org/cats/typeclasses/lawtesting.html) ou [circe](https://github.com/circe/circe/blob/master/modules/testing/shared/src/main/scala/io/circe/testing/CodecTests.scala).

Les exemples de code complets peuvent être trouvés [ici](https://gist.github.com/dorsev/0fdd8315228d7ef6914b27650f817ae6).