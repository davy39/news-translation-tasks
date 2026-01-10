---
title: 'Au-delà des tests unitaires : une introduction aux tests de propriété et de
  loi en Scala'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T15:42:57.000Z'
originalURL: https://freecodecamp.org/news/beyond-unit-tests-an-intro-to-property-and-law-testing-in-scala-dd6a15898a19
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QcyFEloaC2fG_naIOEYXbQ.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: Scala
  slug: scala
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: 'Au-delà des tests unitaires : une introduction aux tests de propriété
  et de loi en Scala'
seo_desc: 'By Daniel Sebban

  Taking your unit tests to the next level.

  I have been using ScalaCheck testing library for at least 2 years now. It allows
  you to take your unit tests to the next level.


  You can do Property-based testing by generating a lot of tests...'
---

Par Daniel Sebban

#### Passer vos tests unitaires au niveau supérieur.

J'utilise la bibliothèque de test ScalaCheck depuis au moins 2 ans. Elle permet de passer vos tests unitaires au niveau supérieur.

*   
Vous pouvez faire des **tests basés sur les propriétés** en générant un grand nombre de tests avec des données aléatoires et en assertant des propriétés sur vos fonctions. Un simple exemple de code est décrit ci-dessous.
* Vous pouvez faire des **tests de loi** qui sont encore plus puissants et permettent de vérifier des propriétés mathématiques sur vos types.

# Tests basés sur les propriétés

Voici notre type de données `User` bien-aimé :

```scala
case class User(name: String, age: Int)
```

Et un générateur de `User` aléatoire :

```scala
import org.scalacheck.{ Gen, Arbitrary }
import Arbitrary.arbitrary
implicit val randomUser: Arbitrary[User] = Arbitrary(for {
  randomName <- Gen.alphaStr
  randomAge  <- Gen.choose(0,80)
  } yield User(randomName, randomAge))
```

Nous pouvons maintenant générer un `User` comme ceci :

```scala
scala> randomUser.arbitrary.sample
res0: Option[User] = Some(User(OtwlaaxGbmdhuorlmgvXitbmGfbgetm,22))
```

Définissons quelques fonctions sur le `User` :

```scala
def isAdult: User => Boolean = _.age >= 18
def isAllowedToDrink : User => Boolean = _.age >= 21
```

Affirmons que :

**Tous les adultes sont autorisés à boire.**

**Pouvons-nous somehow prouver cela ? Est-ce correct pour tous les utilisateurs ?**

C'est là que les tests de propriété viennent à la rescousse. Ils nous permettent de ne pas écrire de tests unitaires spécifiques. Voici ce qu'ils seraient :

* Les 18 ans ne sont pas autorisés à boire
* Les 19 ans ne sont pas autorisés à boire
* Les 20 ans ne sont pas autorisés à boire

Toutes ces déclarations peuvent être remplacées par une seule vérification de propriété :

```scala
import org.scalacheck.Prop.forAll
val allAdultsCanDrink = forAll { u: User =>
    if(isAdult(u)) isAllowedToDrink(u) else true }
```

Lançons-le :

```scala
scala> allAdultsCanDrink.check()
! Falsified after 0 passed tests.
> ARG_0: User(,19)
```

Il échoue comme prévu pour un jeune de 19 ans.

Les tests de propriété sont géniaux pour plusieurs raisons :

* Gain de temps en écrivant moins de tests spécifiques
* Découverte de nouveaux cas d'utilisation générés par ScalaCheck que vous avez oublié de gérer
* Vous force à penser de manière plus générale
* Vous donne plus de confiance pour le refactoring que les tests unitaires conventionnels

# Tests de loi

Cela devient encore mieux : passons au niveau supérieur et définissons un ordre entre les utilisateurs :

```scala
import scala.math.Ordering
implicit val userOrdering: Ordering[User] = Ordering.by(_.age)
```

Nous voulons nous assurer que nous n'avons **pas oublié de cas limites** et que nous avons défini notre ordre correctement. Cette propriété a un nom, et elle s'appelle un **ordre total**. Il doit être valide pour les propriétés suivantes :

* **Totalité**
* **Antisymétrie**
* **Transitivité**

**Pouvons-nous somehow prouver cela ? Est-ce correct pour tous les utilisateurs ?**

Cela est possible sans écrire un seul test !

Nous utilisons la bibliothèque `cats-laws` pour définir les lois que nous voulons tester sur l'ordre que nous avons défini :

```scala
import cats.kernel.laws.discipline.OrderTests
import cats._
import org.scalatest.FunSuite
import org.typelevel.discipline.scalatest.Discipline
import org.scalacheck.ScalacheckShapeless._
class UserOrderSpec extends FunSuite with Discipline  {
//code standard nécessaire pour satisfaire les dépendances du framework
  implicit def eqUser[A: Eq]: Eq[Option[User]] = Eq.fromUniversalEquals
//convertir notre ordre standard en un ordre `cats`
  implicit val catsUserOrder: Order[User] = Order.fromOrdering(userOrdering)
  
//vérifier toutes les propriétés mathématiques sur notre ordre
  checkAll("User", OrderTests[User].order)
}
```

Lançons-le :

```scala
scala> new UserOrderSpec().execute()
UserOrderSpec:
- User.order.antisymmetry *** FAILED ***
  GeneratorDrivenPropertyCheckFailedException was thrown during property evaluation.
   (Discipline.scala:14)
    Falsified after 1 successful property evaluations.
    Location: (Discipline.scala:14)
    Occurred when passed generated values (
      arg0 = User(h,17),
      arg1 = User(edsb,17),
      arg2 = org.scalacheck.GenArities$$Lambda$2739/1277317528@41d7b4cf
    )
    Label of failing property:
      Expected: true
  Received: false
- User.order.compare
- User.order.gt
- User.order.gteqv
- User.order.lt
- User.order.max
- User.order.min
- User.order.partialCompare
- User.order.pmax
- User.order.pmin
- User.order.reflexitivity
- User.order.reflexitivity gt
- User.order.reflexitivity lt
- User.order.symmetry
- User.order.totality
- User.order.transitivity
```

Comme prévu, il échoue sur la loi d'antisymétrie ! Le même âge et des noms différents ne sont pas censés être égaux. Nous avons oublié d'utiliser le nom dans notre `Ordering` original, alors corrigeons-le et relançons les lois :

```scala
implicit val userOrdering: Ordering[User] = Ordering.by( u => (u.age, u.name))
scala> new UserOrderSpec().execute()
UserOrderSpec:
- User.order.antisymmetry
- User.order.compare
- User.order.gt
- User.order.gteqv
- User.order.lt
- User.order.max
- User.order.min
- User.order.partialCompare
- User.order.pmax
- User.order.pmin
- User.order.reflexitivity
- User.order.reflexitivity gt
- User.order.reflexitivity lt
- User.order.symmetry
- User.order.totality
- User.order.transitivity
```

Et maintenant, cela passe :)

Si vous vous demandez ce que vous pouvez tester en plus des `Order`s, allez consulter la documentation ici : [https://typelevel.org/cats/typeclasses/lawtesting.html](https://typelevel.org/cats/typeclasses/lawtesting.html)

# Résumé

* Les tests de propriété sont plus puissants que les tests unitaires. Ils nous permettent de définir des propriétés sur les fonctions et de générer un grand nombre de tests en utilisant des générateurs de données aléatoires.
* Les tests de loi passent au niveau supérieur et utilisent les propriétés mathématiques des structures comme `Order` pour générer les propriétés et les tests.
* La prochaine fois que vous définissez un ordre et que vous vous demandez s'il est bien défini, allez-y et exécutez les lois dessus !