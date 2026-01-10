---
title: An introduction to Law Testing in Scala
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
seo_title: null
seo_desc: 'By dor sever

  Property-based law testing is one of the most powerful tools in the scala ecosystem.
  In this post, I’ll explain how to use law testing and the value it’ll give you using
  in-depth code examples.

  This post is aimed for Scala developers who...'
---

By dor sever

Property-based law testing is one of the most powerful tools in the scala ecosystem. In this post, I’ll explain how to use law testing and the value it’ll give you using in-depth code examples.

This post is aimed for Scala developers who want to improve their testing knowledge and skills. It assumes some knowledge of Scala, cats, and other functional libraries.

![Image](https://cdn-media-1.freecodecamp.org/images/GpUIRfAe79BTz8JGTvk0oOD376oxjBxj4CiS)

#### **Introduction**

* You might be familiar with types which are a set of values (for example Int values are : `1,2,3`… String values are : `“John Doe”` etc).
* You also might be familiar with functions which is a mapping from Input type to Output type.
* A property is defined on a type or a function and describes its desired behavior.

So what is a Law? **Keep on reading!**

#### **A concrete example**

Here is our beloved `_Person_` data type:

```
case class Person(name: String, age: Int)
```

And serialization code using the `Play-Json` , a library that allows transforming your `Person` type into `JSON :`

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

We can now test this serialization function on a specific input like this:

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

But, we now need to ask ourselves, whether all people will serialize successfully? What about a person with invalid data (such as negative age)? Will we want to repeat this thought process of finding edge-cases for all our test data?

And most importantly, will this code remain readable over time? (e.g.: changing the `person` data type [adding a `LastName` field], repeated tests for other data types, etc)

> “ We can solve any problem by introducing an extra level of indirection”.

### Property-based testing

The first weapon in our disposal is Property-based testing (PBT). PBT works by defining a property, which is a high-level specification of behavior that should hold for all values of the specific type.

In our example, the **property** will be:

* For every person p, if we serialize and deserialize them, we should get back the same person.

Writing this property using scala check looks like this:

```scala
object PersonSerdeSpec extends org.scalacheck.Properties("PersonCodec") {
  property("round trip consistency") = 
org.scalacheck.Prop.forAll { a: Person =>
    personFormat.reads(personFormat.writes(a)).asOpt.contains(a)
  }
}
```

The property check requires a way to generate Persons. This is done by using an `Arbitrary[Person]` which can be defined like this:

```scala
implicit val personArb: Arbitrary[Person] = Arbitrary {
  for {
    name <- Gen.alphaStr
    age  <- Gen.chooseNum(0, 120)
  } yield Person(name, age)
}
```

Furthermore, we can use `“scalacheck-shapeless”`- an amazing library which eliminates (almost) all needs for the verbose (quite messy and highly bug-prone) arbitrary type definition by generating it for us!

![Image](https://cdn-media-1.freecodecamp.org/images/XgoIxileqrYUmSnMMkzuGFJJCkxvy6-Ryj-Q)

This can be done by adding:

```
libraryDependencies += "com.github.alexarchambault" %% "scalacheck-shapeless_1.14" % "1.2.0"
```

and importing the following in our code:

```
import org.scalacheck.ScalacheckShapeless._
```

And then we can remove the `_personArb_` instance we defined earlier.

### The Codec Law

Let’s try to abstract further, by defining the **laws** of our data type:

```scala
trait CodecLaws[A, B] {
  def serialize: A => B
  def deserialize: B => A
  def codecRoundTrip(a: A): Boolean = serialize.
andThen(deserialize)(a) == a
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/De-BSLaDLDfZvMXrdBFzwvufzCyHVTONXTTg)

This means That given

* The types `A, B`
* A function from `A to B`
* A function from `B to A`

We define a function called “`codecRoundTrip`” which takes an `“a: A”` and takes it through the functions and makes sure we get the same value of type A back.

This Law states (without giving away **any implementation details**), that the roundtrip we do on the given input does not “lose” any information.

> Another way of saying just that is by claiming that our types A and B are isomorphic.

We can abstract even more, by using the cats-laws library with the `IsEq` case-class for defining an Equality description.

```scala
import cats.laws._
trait CodecLaws[A, B] {
  def serialize: A => B
  def deserialize: B => A
  def codecRoundTrip(a: A): cats.laws.IsEq[A] = serialize.andThen(deserialize)(a) <-> a
}
/** Represents two values of the same type that are expected to be equal. */
final case class IsEq[A](lhs: A, rhs: A)
```

What we get from this type and syntax is a **description** **of equality** between the two values instead of the equality result like before.

### The Codec Test

It is time to test the laws we just defined. In order to do that, we will use the “[discipline](https://github.com/typelevel/discipline)” library.

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

We define a CodecTest trait that takes 2 type parameters `A and B`, which in our example will be `Person` and `JsResult`.

The trait holds an instance of the laws and defines a test method that takes an `Arbitrary[A]` and an equality checker (of type `Eq[A]`) and returns a `rule-set` for `scalacheck` to run.

Note that no tests actually run here. This gives us the power to run these tests which are defined just once for all the types we want

We can now commit to a specific type and implementation (like `Play-Json` serialization) by instantiating a `CodecTest` with the proper types.

```scala
object JsonCodecTests {
  def apply[A: Arbitrary](implicit format: Format[A]): CodecTests[A, JsValue] =
    new CodecTests[A, JsValue] {
      override def laws: CodecLaws[A, JsValue] =
        CodecLaws[A, JsValue](format.reads, format.writes)
    }
}
```

#### A (type) detour

But now we get the error:

```scala
Error:(11, 38) type mismatch;
 found   : play.api.libs.json.JsResult[A]
 required: A
```

We expected the types to flow from:

```
  A  =>  B  =>  A
```

But Play-Json types go from:

```
 A  =>  JsValue  =>  JsResult[A]
```

This means that our deserialize function can succeed or fail and will not always return an A, but rather a container of A.

In order to abstract over the types, we now need to use the `F[_]` type constructor syntax:

```scala
trait CodecLaws[F[_],A, B] {
  def serialize: A => B
  def deserialize: B => F[A]
  def codecRoundTrip(a: A)(implicit app:Applicative[F]): IsEq[F[A]] =
    serialize.andThen(deserialize)(a) <-> app.pure(a)
}
```

The `Applicative` instance is used to take a simple value of type A and lift it into the `Applicative` context which returns a value of type `F[A]`.

> This process is similar to taking some value `x` and lifting it to an `Option` context using `Some(x)`, or in our concrete example taking a value `a:A` and lifting it to the `JsResult` type using `[JsSuccess](https://www.playframework.com/documentation/2.7.0/api/scala/play/api/libs/json/JsSuccess.html)(a)`.

We can now finish the implementation for `CodecTests` and `JsonCodecTests` like this:

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

And to define a working `Person` serialization test in **1 line of code:**

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

### The power of abstraction

We were able to define our tests and laws without giving away any implementation details. This means we can switch to using a different library for serialization tomorrow and all our laws and tests will still hold.

#### Another example

We can test this theory by adding support to BSON serialization using the `reactive-mongo` library:

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

The types here flow from

```
A => BsonDocument => A
```

and not `F[A]` as we had expected. Luckily for us, we have a solution and use the Id-type to represent just that.

And given the (very long) serializer definition:

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

we can now define BsonCodecTests in all its **1** line of logic glory.

```scala
class BsonCodecSpec extends Checkers with FunSuiteLike with Discipline {
    checkAll("PersonSerdeTests", BsonCodecTests[Person].tests)
}
```

### A (First-order) logic perspective on our code

Our first test attempt can be described as follows:

```
∃p:Person,s:OFormat that holds : s.read(s.write(p)) <-> p
```

Meaning, `for the specific person p(“John Doe”,32)` and `for the format **s**`, the following statement is true: `decode(encode(p)) <-`> p.

The second attempt (using `PBT`) can be:

```
∃s:OFormat, ∀p:Person the following should hold :  s.read(s.write(p)) <-> p
```

Which means, **for all** persons p and `for the specific format **s**`, the following is true: `decode(encode(p))<`->p.

The third (and most powerful statement thus far) using `law testing`:

```
∀s:Encoder, ∀p:Person the the following should hold :  s.read(s.write(p)) <-> p
```

Which means, `for all` `formats s`, and `**for all** persons p`, the following is true: `decode(encode(p))<`->p.

#### **Summary**

* Law testing allows you to reason about your data-types and functions in a mathematical and concise way and provides a totally new paradigm for testing your code!
* Most of the type level libraries you use (like `cats`, `circe` and many more) use law testing internally to test their data-types.
* Avoid writing specific test-cases for your data-types and functions and try to generalize them using property-based law tests.

Thank you for reaching this far! I am super excited about finding more abstract and useful laws that I can use in my code! Please let me know about any you’ve used or can think of.

More inspiring and detailed content can be found in the [cats-laws](https://typelevel.org/cats/typeclasses/lawtesting.html) site or [circe](https://github.com/circe/circe/blob/master/modules/testing/shared/src/main/scala/io/circe/testing/CodecTests.scala).

The complete code examples can be found [here](https://gist.github.com/dorsev/0fdd8315228d7ef6914b27650f817ae6).

