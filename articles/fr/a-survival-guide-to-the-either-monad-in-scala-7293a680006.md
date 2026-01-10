---
title: Un guide de survie pour le monad Either en Scala
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T16:37:01.000Z'
originalURL: https://freecodecamp.org/news/a-survival-guide-to-the-either-monad-in-scala-7293a680006
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/either.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
seo_title: Un guide de survie pour le monad Either en Scala
seo_desc: 'By Luca Florio

  I started to work with Scala few months ago. One of the concepts that I had the
  most difficulties to understand is the Either monad. So, I decided to play around
  with it and better understand its power.

  In this story I share what I’ve ...'
---

Par Luca Florio

J'ai commencé à travailler avec Scala il y a quelques mois. L'un des concepts que j'ai eu le plus de difficultés à comprendre est le monad `Either`. J'ai donc décidé de m'amuser avec et de mieux comprendre sa puissance.

Dans cette histoire, je partage ce que j'ai appris, espérant aider les codeurs à aborder ce beau langage.

#### Le monad Either

`Either` est l'un des monads les plus utiles en Scala. [Si vous vous demandez ce qu'est un monad](https://medium.com/@sinisalouc/demystifying-the-monad-in-scala-cc716bb6f534), eh bien... Je ne peux pas entrer dans les détails ici, peut-être dans une future histoire !

Imaginez `Either` comme une boîte contenant un calcul. Vous travaillez à l'intérieur de cette boîte, jusqu'à ce que vous décidiez d'en sortir le résultat.

Dans ce cas spécifique, notre boîte `Either` peut avoir deux "formes". Elle peut être (soit) un `Left` ou un `Right`, selon le résultat du calcul à l'intérieur.

Je vous entends demander : "OK, et à quoi ça sert ?"

La réponse habituelle est : la gestion des erreurs.

Nous pouvons mettre un calcul dans le `Either`, et en faire un `Left` en cas d'erreur, ou un `Right` contenant un résultat en cas de succès. L'utilisation de `Left` pour les erreurs et de `Right` pour le succès est une convention. Comprenons cela avec un peu de code !

%[https://scalafiddle.io/sf/sgAxvBI/0]

Dans cet extrait, nous définissons uniquement une variable `Either`.

Nous pouvons la définir comme un `Right` contenant une valeur valide, ou comme un `Left` contenant une erreur. Nous avons également un calcul qui retourne un `Either`, ce qui signifie qu'il peut être un `Left` ou un `Right`. Simple, n'est-ce pas ?

#### Projection Right et Left

Une fois que nous avons le calcul dans la boîte, nous pouvons vouloir en extraire la valeur. Je suis sûr que vous vous attendez à appeler un `.get` sur le `Either` et à extraire votre résultat.

Ce n'est pas si simple.

Réfléchissez-y : vous mettez votre calcul dans le `Either`, mais vous ne savez pas s'il a abouti à un `Left` ou à un `Right`. Alors, que devrait retourner un appel `.get` ? L'erreur ou la valeur ?

C'est pourquoi, pour obtenir le résultat, vous devez faire une hypothèse sur le résultat du calcul.

C'est là que la **projection** entre en jeu.

À partir d'un `Either`, vous pouvez obtenir une `RightProjection` ou une `LeftProjection`. La première signifie que vous supposez que le calcul a abouti à un `Right`, la seconde à un `Left`.

Je sais, je sais... cela peut être un peu confus. Il est préférable de le comprendre avec un peu de code. Après tout, **le code dit toujours la vérité**.

%[https://scalafiddle.io/sf/8amYK4r]

C'est tout. Notez que lorsque vous essayez d'obtenir le résultat d'une `RightProjection`, mais qu'il s'agit d'un `Left`, vous obtenez une exception. Il en va de même pour une `LeftProjection` et vous avez un `Right`.

Le truc cool, c'est que vous pouvez mapper sur les projections. Cela signifie que vous pouvez dire : "supposez que c'est un Right : faites ceci avec", en laissant le `Left` inchangé (et vice versa).

#### De Option à Either

`Option` est une autre façon courante de gérer les valeurs invalides.

Un `Option` peut avoir une valeur ou être vide (sa valeur est `Nothing`). Je parie que vous avez remarqué une similitude avec `Either`... C'est encore mieux, car nous pouvons transformer un `Option` en un `Either` ! C'est l'heure du code !

%[https://scalafiddle.io/sf/KCtNRkL]

Il est possible de transformer un `Option` en un `Left` ou un `Right`. Le côté résultant du `Either` contiendra la valeur de l'`Option` si elle est définie. Cool. Attendez une minute... Que se passe-t-il si l'`Option` est vide ? Nous obtenons l'autre côté, mais nous devons spécifier ce que nous nous attendons à y trouver.

#### À l'envers

`Either` est magique, nous sommes tous d'accord sur ce point. Nous décidons donc de l'utiliser pour nos calculs incertains. Un scénario typique en programmation fonctionnelle est le mappage d'une fonction sur une `List` d'éléments, ou sur une `Map`. Faisons-le avec notre tout nouveau calcul alimenté par `Either`...

%[https://scalafiddle.io/sf/WozPbpV]

Huston, nous avons un "problème" (ok, ce n'est pas un GROS problème, mais c'est un peu inconfortable). Il serait préférable d'avoir la collection à l'intérieur du `Either` plutôt que beaucoup de `Either` à l'intérieur de la collection. Nous pouvons travailler là-dessus.

#### **List**

Commençons par `List`. D'abord, nous réfléchissons, puis nous pouvons jouer avec le code.

Nous devons extraire la valeur du `Either`, la mettre dans la `List`, et mettre la liste à l'intérieur d'un `Either`. Bien, j'aime ça.

Le point est que nous pouvons avoir un `Left` ou un `Right`, donc nous devons gérer les deux cas. Jusqu'à ce que nous trouvions un `Right`, nous pouvons mettre sa valeur à l'intérieur d'une nouvelle `List`. Nous procédons de cette manière en accumulant chaque valeur dans la nouvelle `List`.

Finalement, nous atteindrons la fin de la `List` de `Either`, ce qui signifie que nous avons une nouvelle `List` contenant toutes les valeurs. Nous pouvons l'emballer dans un `Right` et c'est fait. C'était le cas où notre calcul n'a pas retourné une `Error` à l'intérieur d'un `Left`.

Si cela se produit, cela signifie que quelque chose s'est mal passé dans notre calcul, donc nous pouvons retourner le `Left` avec l'`Error`. Nous avons la logique, maintenant nous avons besoin du code.

%[https://scalafiddle.io/sf/LjaXKPT]

#### **Map**

Le travail sur `Map` est assez simple une fois que nous avons fait le travail pour la `List` (malgré le besoin de le rendre générique) :

* Étape un : transformer la `Map` en une `List` de `Either` contenant le tuple (clé, valeur).
* Étape deux : passer le résultat à la fonction que nous avons définie sur `List`.
* Étape trois : transformer la `List` de tuples à l'intérieur du `Either` en une `Map`.

Facile comme bonjour.

%[https://scalafiddle.io/sf/vlY7xV0]

#### Soyons classe : un convertisseur implicite utile

Nous avons introduit `Either` et compris qu'il est utile pour la gestion des erreurs. Nous avons un peu joué avec les projections. Nous avons vu comment passer d'un `Option` à un `Either`. Nous avons également implémenté quelques fonctions utiles pour "extraire" `Either` de `List` et `Map`. Jusqu'à présent, tout va bien.

J'aimerais conclure notre voyage dans le monad `Either` en allant un peu plus loin. Les fonctions utilitaires que nous avons définies font leur travail, mais j'ai l'impression qu'il manque quelque chose...

Il serait incroyable de faire notre conversion directement sur la collection. Nous aurions quelque chose comme `myList.toEitherList` ou `myMap.toEitherMap`. Plus ou moins comme ce que nous faisons avec `Option.toRight` ou `Option.toLeft`.

Bonne nouvelle : nous pouvons le faire en utilisant des **classes implicites** !

%[https://scalafiddle.io/sf/j8Ixqz5]

L'utilisation de classes implicites en Scala nous permet d'étendre les capacités d'une autre classe.

Dans notre cas, nous étendons la capacité de `List` et `Map` pour "extraire" automatiquement le `Either`. L'implémentation de la conversion est la même que celle que nous avons définie précédemment. La seule différence est que maintenant nous la rendons générique. Scala n'est-il pas génial ?

Puisque cela peut être une classe utilitaire utile, j'ai préparé pour vous un gist que vous pouvez copier et coller facilement.

```scala
object EitherConverter {
  implicit class EitherList[E, A](le: List[Either[E, A]]){
    def toEitherList: Either[E, List[A]] = {
      def helper(list: List[Either[E, A]], acc: List[A]): Either[E, List[A]] = list match {
        case Nil => Right(acc)
        case x::xs => x match {
          case Left(e) => Left(e)
          case Right(v) => helper(xs, acc :+ v)
        }
      }

      helper(le, Nil)
    }
  }

  implicit class EitherMap[K, V, E](me: Map[K, Either[E, V]]) {
    def toEitherMap: Either[E, Map[K, V]] = me.map{
        case (k, Right(v)) => Right(k, v)
        case (_, e) => e
      }.toList.toEitherList.map(l => l.asInstanceOf[List[(K, V)]].toMap)
  }
}
```

#### Conclusion

C'est tout, les amis. J'espère que cette courte histoire pourra vous aider à mieux comprendre le monad `Either`.

Veuillez noter que mon implémentation est assez simple. Je parie qu'il existe des moyens plus complexes et élégants de faire la même chose. Je suis un débutant en Scala et j'aime [KISS](https://en.wikipedia.org/wiki/KISS_principle), donc je préfère la lisibilité à la complexité (élégante).

Si vous avez une meilleure solution, surtout pour la classe utilitaire, je serai ravi de la voir et d'apprendre quelque chose de nouveau ! :-)