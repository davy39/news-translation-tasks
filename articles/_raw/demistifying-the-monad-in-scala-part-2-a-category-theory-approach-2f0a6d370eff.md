---
title: 'Further demistifying the Monad in Scala: a Category Theory approach'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-25T18:14:51.000Z'
originalURL: https://freecodecamp.org/news/demistifying-the-monad-in-scala-part-2-a-category-theory-approach-2f0a6d370eff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OU9A2GD6x7ben-VtJogDIQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sinisa Louc

  Some of you may have read my article on monads. This time I want to talk about monads
  from a different, more theoretical point of view. It is not mandatory to read the
  previous article first (in case you haven’t), but if you don’t know...'
---

By Sinisa Louc

Some of you may have read my [article](https://www.freecodecamp.org/news/demystifying-the-monad-in-scala-cc716bb6f534/) on monads. This time I want to talk about monads from a different, more theoretical point of view. It is not mandatory to read the previous article first (in case you haven’t), but if you don’t know anything about the topic, I guess it wouldn’t hurt to become familiar with it before jumping on this one.

Let’s start. Some of you may have heard the popular quote:

> A monad is just a monoid in the category of endofunctors, what’s the problem?

Original statement is from _Categories for the Working Mathematician_ by Saunders Mac Lane, but it has been quoted and rephrased numerous times. I took this statement as a reference point; a teaching objective, if you will. So I will attempt to explain monads from the category theory point of view by explaining that particular sentence.

Important note: A lot of stuff written here is simplified and may not be 100% mathematically accurate. Category theory is a very complex field of mathematics (sometimes even jokingly referred to as “[abstract nonsense](https://en.wikipedia.org/wiki/Abstract_nonsense)”).   
This is not a math article. This is simply my attempt of creating an introductory, easy-to-follow text that should serve as a starting point to get you all excited about category theory and continue the exploration on your own.

#### Algebraic structures

What is a category? A category is an _algebraic structure_. OK, but what is an algebraic structure? Algebraic structure is basically a **set** (when used in this context of being an algebraic structure’s set, it is commonly referred to as _underlying_ _set_) of one or more **elements** with one or more **operations** on them.

There are two main things that differentiate algebraic structures from one another:

* laws that need to hold for operations on set elements
* existence of identity element

Here are some laws that appear across different algebraic structures (operation in an algebraic structure is denoted as ○):

* _Closure_: For all _a_, _b_ in algebraic structure _M_, the result of operation _a_ ○ _b_ is also in _M_
* _Invertibility_: For each element _a_ in _M_ there is an element _b_ where _a_ ○ _b_ = _b_ ○ _a_ = _e_ , where _e_ is the identity
* _Commutativity_: for all _a, b_ in _M_: _a ○ b = b ○ a_
* _Associativity_: for all _a, b, c_ in _M: (a ○ b) ○ c = a ○ (b ○ c)_

Identity element is an element which (quoting the [wiki](https://en.wikipedia.org/wiki/Identity_element)) “leaves other elements unchanged when combined with them”. It’s the element that doesn’t affect the result when used in operation ○. We can formulate that into a law too:

* _Identity_: for any _a_ in _M_ there is an element _e_ where _e_ ○ _a = a_ ○ _e = a_

So, starting from a simple set with one or more operations and by adding a certain combination of the laws that are required, we can end up with various algebraic structures. Here are some:

![Image](https://cdn-media-1.freecodecamp.org/images/AnBwokE21gCnz0Wzr8Oky6Pa27hKwFirLFEt)

#### Category

Category is an algebraic structure that consists of objects with defined mappings between some of them. Those mappings are called _morphisms_ or _arrows_. Arrows go from one object to another. Some pairs of objects have an arrow between them defined, some don’t.

Categories have an important feature: if there is some arrow _f_: A → B and an arrow _g_: B → C, there is also automatically a _composition_ of arrows _f_ and _g_ which forms an arrow A → C. We write the composition as _g ○ f_. Recall that algebraic structure is defined as a set with some operation(s) on its elements; in case of category, those elements are arrows and the operation is arrow composition.

Categories are completely abstract and this is quite tricky to wrap your mind around. “Give me an example of a category”, you ask. OK, here’s one — _Set_. _Set_ is the [category of sets](https://en.wikipedia.org/wiki/Category_of_sets). Which sets? Does it include the set of integers, set of letters in english alphabet, set of all animals with four legs? Yes, it includes any and every set there is.

It’s not easy, but try not to think in completely concrete terms. Don’t try to materialise those sets. We don’t care how many sets are inside the category or which elements are inside those sets. We just care about the fact that objects in the Set category are sets and arrows are functions between sets that can be composed. I mean, that’s not all, there is a [whole science](https://www.jstor.org/stable/72513) behind category of sets with lots of axioms and laws. But we have all we need for now.

Regarding our algebraic structure laws, category obeys two: **identity** and **associativity**. Since category is an algebraic structure with arrows as its elements and arrow composition as the operation between the elements, following those laws means that we have an identity arrow and that composition of arrows is associative.

Identity arrow is an arrow that goes from an object to itself. Composition of any arrow _f_ with identity arrow _e_ is arrow _f:_

_e ○ f_ = _f_ = _f_ _○ e_

Given arrows _f_, _g_, _h_ and their composition _○_, the associativity law is:

_h ○ (g ○ f) = (h ○ g) ○ f_

Functions in your favourite programming language are another example of a category. Objects in this category are types and morphisms are functions that take a type and return a type. For any type there exists a function that returns that same type (identity) and functions compose easily, obeying associativity law. Note that functions of two or more arguments can be [curried](https://en.wikipedia.org/wiki/Currying) and therefore viewed as functions of one argument that return a higher-order function.

That’s it for now regarding categories. Objects, arrows, composition, identity, associativity. Good. We’ll get back to them shortly.

#### Monoid

Getting warmer. What is a monoid?

Monoid can be defined as a:

- single set _S_   
- with an associative binary operation _○_  
- and an identity element _e_  
_-_ following two laws:  
 _(a ○ b) ○ c = a ○ (b ○ c)_  
 _a ○ e = e ○ a = a_

Note how similar this looks to a category. We will soon see what this means.

But first an example for a monoid. OK, so we need a set with an associative binary operation and with some identity element. We could take addition on the set of integers Z. Alright, we have an identity element (it’s zero) and we have the associativity, because (x + y) + z= x + (y + z). If you take another look at that table of laws for various algebraic structures, you’ll notice that addition in Z is in fact a group, because it also has an inverse (subtraction).

But here’s something cool and possibly a bit disturbing at the same time — monoid is actually a **category**, just a bit of a special one: **it has only one object**.

If you scroll back to the table we saw earlier you’ll see that monoid is actually pretty similar to a category, only difference being the closure law. Recall that closure says “for all _a_, _b_ in algebraic structure _M_, the result of operation _a_ ○ _b_ is also in _M_”. It’s pretty logical we got the closure property in a monoid since we always start from and end up in the same object (the only one we have). Categories don’t have closure because not all arrows can necessarily be composed (e.g. you can’t compose _a → b_ and _c → d_) so the property “combine any two elements and you’ll arrive at something that’s also a part of the set” doesn’t hold. Other two laws (identity and associativity) are the same.

When switching the viewpoint from _monoid as a set_ to _monoid as a category_, elements of the set become arrows of the category, identity element becomes the identity arrow, and binary operation becomes arrow composition. And yes, as soon as we enter the twilight zone also known as category theory, stuff gets weird. But with a bit of mindset shifting, our addition-in-Z example can be seen as a category.

First of all, numbers are now arrows. Think of an arrow as an “add X” function. These functions compose quite nicely, since adding 3 to a number and adding 5 to the result is the same as adding 8 to the original number. Furthermore, composing add3 with add5 followed by composing with add7 is the same as composing add3 with the composition of add5 and add7:

_(add3 ○ add5) ○ add7 = add3 ○ (add5 ○ add7)_

To cite a particular [great source](http://bartoszmilewski.com/2014/12/05/categories-great-and-small/) on category theory from which I took the adders example:

> Instead of giving you the traditional rules of addition, I could as well give you the rules of composing adders, without any loss of information.

So, by shifting our viewpoint a little, we were able to see the monoid both as a set (on the left) and a single-object category (on the right).

![Image](https://cdn-media-1.freecodecamp.org/images/b3uWNx07IXLiBE21ysOYyAeBiDsDF5rH29vr)
_(I took the photo from [here](https://en.wikiversity.org/wiki/Introduction_to_Category_Theory/Monoids#From_Binary_Operators_to_Arrows" rel="noopener" target="_blank" title="))_

Also, all the laws that we had in the first case are also present in the second case. Nothing more, nothing less.

OK, so we no longer have numbers; we have add-arrows which represent single-parameter adding functions. Second operand of adding operation is “hardcoded” (operation is now unary, not binary) so we have one function for each natural number. Total count of natural numbers and total count of arrows in our category are the same. Finally, arrows all share the same starting and ending object.

This object is completely irrelevant; think of it as a massless blob of nothingness. If you want, we could rename arrows from “addX’ to simply “x” and then the whole thing becomes really similar to our normal good old set Z with addition, just instead of “adding two and two equals four” we would say “composing two and two equals four”.

Here are the wikis for both viewpoints, perhaps you’ll find them useful:

* [monoid as a set](https://en.wikipedia.org/wiki/Monoid)
* [monoid as a category](https://en.wikipedia.org/wiki/Monoid_(category_theory)).

#### Functor

Alright, now we know what algebraic structures are and how they are defined, and we also took a closer look into two of them — category and monoid. We saw that monoid is a category too, just with only one object.

What we need now is a _functor_ (by the way, I already [wrote a bit about functors](https://hackernoon.com/functors-and-applicatives-b9af535b1440#.zabfpezi1) too).

Compared to monoids and categories, functor is a bit different. It is not really an algebraic structure; it’s more of a function that _maps_ from algebraic structures to algebraic structures. But not just any algebraic structures: functor is a **mapping between categories.**

Category, as we know by now, is a set of objects with arrows between them. Well, functor knows how to map the category to another category. It will map all the objects and all the arrows, and it will preserve the connections between objects (if there is an arrow between _a_ and _b_ in original category, there will be one between _Fa_ and _Fb_ in the resulting category). Given some object _a_ or some arrow _f: a → b_ from the original category, corresponding object (the one functor maps into) is denoted as _F(a)_ and corresponding arrow is denoted as _F(f): F(a) → F(b)_.

Functor that maps a category back to that same category is called an _endofunctor._ Quick detour from the category theory into the real world — in programming, we deal with functors in category of types, and they are all endofunctors. They map a category of types back to category of types. Whenever you mapped something (_map_ in Scala, _fmap_ in Haskell) you had an endofunctor in your hands. For example, Option, List and Future are all valid endofunctors. Basically anything that has a map() function is an endofunctor.

Don’t take this for granted though; it’s merely a convention. Some library may provide you with an object whose map() doesn’t obey the functor laws (see the [old article](https://hackernoon.com/functors-and-applicatives-b9af535b1440#.zabfpezi1)) which would mean that the object itself cannot be considered a functor.

Example: in Scala we can map from List[Int] to List[String] (in other words, to map all elements of a List from Int to String):

```scala
List(1, 2, 3).map((x: Int) => x.toString)
```

We can have all kinds of mappings: from Int to String, from String to List[String], from List[String] to Banana etc. All of them are Scala types. This means we always map from a category of Scala types back to the category of Scala types. Hence the “endo” part.

Now let’s “rip out” the map() method from some functor F and view it as a function of two arguments — a functor object and a function which we map it with. For example, List(1, 2, 3).map(f) becomes map(f, List(1, 2, 3)).

If we curry that, it’s easy to see that signature of _map_ is:

_(a → b) → F[a] → F[b]_

Function which we map with is denoted as _a → b_, starting functor object is _F[a]_ and result functor is _F[b]._ Note that instead of providing both arguments, function _a → b_ (e.g. _(x: Int) => _.toStrin_g()) and a functor instan_ce F[_a] (e._g. List(1, 2,_ 3)), we can provide only the functi_on_ f, in which case we get back a functi_on F[a] → F_[b] (if this is not something you’re comfortable with, do a quick research on currying and partially applied functio_n_s). So yeah, instead of providing both arguments of type A and B and getting back a value of type C, we can provide only parameter of type A and get back a function B → C. Providing only number 4 to a function which sums two numbers gives us back a function that takes some numb_er_ n and retur_ns_ n+4.

Let’s take another look at this interesting function _(a → b) → F[a] → F[b]_. It’s a function from _(a → b)_ to _F[a] → F[b]._ To put it in category theory terms — it maps a category to another category, where objects of destination category carry the F symbol. Remember what we said earlier? “Given some object _a_ or some arrow _a → b_ from the original category, corresponding object (the one functor maps into) is denoted as _F(a)_ and corresponding arrow is denoted as _F(a) → F(b)_.” That’s exactly what map does.

But we are missing something. We saw just one half of being a functor: the one that maps morphisms. A **function on functions**. It takes a function and returns the “lifted” version of that function, that is, one that instead of taking _a_ and returning _b_ now takes _F[a]_ and returns _F[b]_. By the way, in practice we often don’t just lift functions and save them for later. Instead we immediately apply them to a functor instance. For example, instead of lifting a function _Int → String_ to _List[Int] → List[String]_, we usually pass in an instance of _List[Int]_ right away (or, in case of Scala, we invoke map() as a method on an instance of _List[Int]_)).

However, we know that functor not only maps all source arrows to destination arrows, but also maps all source objects to destination objects, right? But we only saw the mapping of arrows, when we lifted _a → b_ to _F(a) → F(b)_. How to map _a_ itself (and _b_, for that matter)? This is another side of a functor: apart from the function on functions, there is also a (somewhat implicit) **function on types**. Functor’s mapping of arrows is represented by the function-on-functions part, while mapping of objects is represented by the function-on-types part.

What is this function on types? It’s a _unary type constructor_. This means that, given some type, functor produces another new type. So if we take List functor as an example, given a String it gives us a List[String]. Given some type A, it gives us a List[A]. Type constructor for functors can be described in a more general way as * → * (takes one type as a parameter and produces a new type from it). [Here’s](http://blogs.atlassian.com/2013/09/scala-types-of-a-higher-kind/) some more useful reading on type constructors.

Quick wrap-up of functors. Each functor is a mapping of categories. It maps some source category C to destination category F by mapping objects in C to objects in F and morphisms in C to morphisms in F. We say that (quoting myself) “given some object _a_ or some arrow _f: a → b_ from the original category, corresponding object (the one functor maps into) is denoted as _F(a)_ and corresponding arrow is denoted as _F(f): F(a) → F(b)_”.

As (Scala?) programmers, we are working with the category of types in Scala (category of types in Haskell is called _Hask_, so I guess the Scala one could be called _Sca_ or something). Here objects are Scala types and morphisms are functions between those types. Each functor in _Sca_ maps the objects (Scala types) via the _type constructor_, and morphisms (functions on Scala types) via function _map_. If we take Option as an example, it maps every object in _Sca_ (that is, every Scala type) into Option(thatObject), and every morphism between objects in Scala (that is, function between Scala types) into Option(thatFunction).

And since it’s a functor _Sca → Sca_, it’s more specifically an _endofunctor_.

#### Monad

Now that we know what category, monoid and endofunctor are, we can imagine a category of endofunctors and try to find a monoid in that category. As the famous statement by mr. Mac Lane tells us, monoid in the category of endofunctors is in fact a monad.

What does it mean to be a monoid in some category? For example, a monoid in the category Set (remember, that’s the category of all sets). What is it? Well, take a look at the category; it contains all imaginable sets. Now pick out those that satisfy monoid laws, that is, pick out all those sets for whose elements we can find an _identity element_ and define an _associative binary operation_.

One such set is the set of integers with identity element being zero and binary operation being addition. Note that monoidal binary operation on set S must operate on two operands, both from S, and return something that is also an element of S.

Cool, so a monoid in the category Set is any set that has those properties, that is, those two operations (for example, the set of natural numbers with addition). [Here](https://en.wikipedia.org/wiki/Monoid_%28category_theory%29#Examples) are some more examples of monoids in the category of X.

Let’s now see about “monoid in the category of endofunctors”. In this category, **objects are endofunctors** and **arrows are mappings between those functors**. An extra bit of terminology before we continue: mappings between functors are called [natural transformations](https://en.wikipedia.org/wiki/Natural_transformation). They operate on a yet higher level of abstraction:

* _arrows_ map objects within a category from one to another
* _functors_ map categories from one to another
* _natural transformations_ map functors from one to another

We could also say that a natural transformation is an “arrow between functors”, and that’s exactly what we have here — we have a category of endofunctors, which means that objects are endofunctors themselves, and arrows between those endofunctors are by definition natural transformations.

Back to our search for monads. So what we are doing is reaching into the category of endofunctors and looking for such objects of that category for which two particular arrows are defined — identity and associative binary operation. When we have those two arrows, we have a monoid (in the category of endofunctors).

So we need an endofunctor F for which the following operations are defined:

* _η_: _I → F_
* _μ_: _F x F → F_

where I is the identity endofunctor, _η_ (eta) is the fancy math name for _identity_ on endofunctors, and _μ_ (mu) is the fancy math name for _associative binary operation_ on endofunctors. If you’re unsure where these two came from all of a sudden, remember that when we talked about monoid as a set, I showed you a [wiki link](https://en.wikipedia.org/wiki/Monoid_%28category_theory%29) which, as you can see, uses those exact two operations (more precisely, arrows in the monoidal category) to define a monoid (in the monoidal category).

Let’s examine those two operations in the context of category of endofunctors and see what they become in that case:

* _Identity_ is a natural transformation mapping from an identity endofunctor (a functor which maps a category to itself) to another endofunctor.
* _Asssociative binary operation_ is some operation x that knows how to take two endofunctors and turn them into one. Keep in mind that this operation must be associative, so (F x F) x F must yield the same result as F x (F x F).

Now let’s see how each of these two operations materialize in the Scala world.

First, _η_: _I → F._ What identity functor _I_ does is it maps any category back to itself. That means its “type constructor” doesn’t actually create any new type _F(value)_. It just leaves the value as it is. So what nat. transformation _η_ really does is — it takes an identity functor and wraps it into a functor _F_ context. In category of Scala types, identity functor maps a type back to itself, so we can view this whole transformation as lifting a Scala type into some F context, where F can be any functor.

What about _μ_: _F x F → F_? It’s a composition of two identical functors which results in just one. It’s a way to turn F[F[T]] into F[T].

Based on what we just said, it’s pretty logical to have **_apply_** as _η_ and **_flatten_** as _μ._ Method _apply_ constructs a type F[x] from x , while _flatten_ “flattens” the composition F[F[x]] into F[x].

So whenever you see an endofunctor in Scala (in practice this is almost any object with method _map_, but remember to check the functor laws before you declare something a functor; for example, there’s a way to break those laws for Set) that also has _flatten_ and _unit_, you are in fact dealing with a monad.

#### Three monad definitions and monad laws

We saw that monad is an endofunctor (remember, any functor in a programming language is actually an endofunctor because it maps from the category of types back to category of types) with two natural transformations:

* identity/unit implemented as _apply,_ and
* associative binary operation implemented as _flatten_ (note that terms _unit_ and _identity_ are used interchangeably; I tend to use unit when talking from a practical, programming viewpoint, and identity when talking about category theory, but sometimes I may mix them up; they’re the same thing).

Also, since we are talking about an (endo)functor, we know that there is a _map_ method available too.

You may have heard about monad consisting of _unit_ and _flatMap_. Yep, that’s correct; we can simply “squash” the _flatten_ (coming from _μ_) and _map_ (coming from its functor nature) methods into a single _flatMap_ method. Our monad would still retain the same properties, it’s just that its associative binary operation would no longer be _flatten_, but _flatMap_. Monad laws (explained later) are not harmed.

So there are two valid definitions of a monad? One that involves _unit_ and _flatMap_ and one that involves _unit_, _flatten_ and _map?_

Yes. And not just that — there’s also a third one. **Monads can be expressed in three different ways.** All three definitions are equivalent and we can easily transform one into another. Here they are:

* unit + flatMap
* unit + flatten + map
* unit + compose

All three are equally powerful and each one can be expressed by using one of the other two. We’ll talk more about them later.

Now, every monad implementation (e.g. List, Option etc.) needs to obey the **monad laws**. Monad laws can be expressed in three different ways, depending on which monad definition you are using, but they all resemble the same core concept.

Here are the monad laws presented using the _unit + flatMap_ definition:

* **left-identity law**:   
_unit(x).flatMap(f) == f(x)_
* **right-identity law**:   
_m.flatMap(unit) == m_
* **associativity law**:  
_m.flatMap(f).flatMap(g) == m.flatMap(x ⇒ f(x).flatMap(g))_

It is obvious that _unit + flatMap_ definition is easily transformed to _unit + flatten + map_ and vice versa because _flatMap = flatten + map._ I will now show the connection between _unit_ + _flatMap_ and _unit_ + _compose_. I like the _unit + compose_ definition because it makes the laws easier to express.

Let’s see the _compose_ function:

```scala
def compose: (A => F[B]) => (B => F[C]) => A => F[C]
```

This is a two-parameter function where both parameters are functions of type _A → F[B]_, and the result is also a function of the same type. Note that types A and B are completely free and may represent any concrete types in Scala (_A→F[B]_ could be e.g. _Int → List[String]_ or _Int → Set[Int]_). We use the letters simply to denote that the parameter of the first function is the same type as the parameter of the result function (here denoted as “A”).

By the way, functions of type A _→_ F[B] are called _Kleisli arrows_, just in case you stumble upon the term somewhere. We say that the function we just defined has Kleisli arrows as parameters and also as return type. It’s a _composition of Kleisli arrows_.

Now let’s also define “unit”:

```scala
def unit: A => F[A]
```

We can easily check that this is indeed unit: it’s a neutral element that, when composed with, gives back the original element. Just take the signature and replace F[C] with F[B] so that the second parameter becomes an identity function:

```scala
(A => F[B]) => (B => F[B]) => A => F[B]
```

Again, types A, B and C are not fixed and can represent any concrete type so _A → F[A]_ from the first identity expression is the same function as _B → F[B]_ in this expression. You can think of identity function not as A _→_ F[A], but as Whatever _→_ F[Whatever] if you wish:

```scala
(A => F[Whatever]) => (Whatever => F[Whatever]) => A => F[Whatever]
```

So if we apply identity function as a second operand to _compose,_ we will arrive back at our first operand. Good, composing identity with some function results in the same function. Identity holds. Associativity is pretty clear too; I will leave it to you to try and prove it by yourself.

What I wanted to show you is that _compose_ can be expressed by using _flatMap_. Same goes in the other direction too; _flatMap_ can be expressed by using _compose_.

Here it is:

```scala
trait Monad[F[_]] {

  def flatMap[A, B](fa: F[A], f: A => F[B]): F[B] = ???
  
  def compose[A, B, C](f1: A => F[B], f2: B => F[C]): A => F[C] = {
    a => flatMap[B, C](f1(a), f2)
  }
}
```

And the other direction:

```scala
trait Monad[F[_]] {

  def compose[A, B, C](f1: A => F[B], f2: B => F[C]): A => F[C] = ???

  def flatMap[A, B](fa: F[A], f: A => F[B]): F[B] = {
    compose[Unit, A, B]((u: Unit) => fa, f)()
  }
}
```

As I said earlier, _unit_ + _compose_ is particularly great for one specific purpose, and that is expressing monad laws. They become simpler to read and understand. Here they are again, this time using _compose_ instead of _flatMap_:

* **left-identity law**:   
_unit.compose(f) == f_
* **right-identity law**:   
_f.compose(unit) == f_
* **associativity law**:  
_f.compose(g.compose(h)) == (f.compose(g)).compose(h)_

Remember that all three definitions are equally “good”, that is, all three are minimal sets of operations needed to define a monad and each one can be expressed by using one of the other two.

Always remember that monad laws are the essence of what makes monads what they are. Having monad operations (e.g. _unit_ + _flatMap_) is not enough if the laws are not satisfied.

#### Summary

Our initial objective is complete. We now understand that famous sentence. **Monoid in the category of endofunctors is any endofunctor with operations _η_ and _μ_, and we call such endofunctor a _monad_** (reminder: objects of that category are endofunctors and arrows are natural transformations).

So, monad can be defined in many ways, such as:

* monoid in the category of endofunctors
* object in the category of endofunctors with arrows _η_ and _μ_
* endofunctor with natural transformations _η_ and _μ_

In Scala, _η_ is implemented as _apply_ and _μ_ is implemented as _flatten_, which means that monad is any functor (that is, a construct with _map_ method) that is additionally equipped with _apply_ and _flatten_. There are two more completely equally valid ways of defining a monad in terms of its operations: _unit_ + _flatMap_ and _unit_ + _compose_. They are completely equal and there is nothing one can do that others can’t. We saw how _flatMap_ can be expressed using _compose_ and vice versa; this is possible for all combinations.

And don’t forget about the monad laws.

#### Final word

Hopefully this article helped you gain some perception as to how certain category theory constructs fit together and, more specifically, what our old friends monads “really are” — monoids in the category of endofunctors.

By the way, the name monad comes from “monoid” and “triad”; monoid because it’s a monoid in the category of endofunctors, and triad because it’s a package of three things: an endofunctor equipped with two natural transformations.

That’s all for now. As usual, if you find any mistakes please do let me know via email (sinisalouc[at]gmail[dot]com). You can also find me on [Twitter](http://twitter.com/sinisalouc).

Cheers!

