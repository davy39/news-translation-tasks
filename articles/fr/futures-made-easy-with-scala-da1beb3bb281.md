---
title: Les Futures Simplifiés avec Scala
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-26T22:06:18.000Z'
originalURL: https://freecodecamp.org/news/futures-made-easy-with-scala-da1beb3bb281
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DBWep0oc9Om-9DzWoasoZQ.jpeg
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: Les Futures Simplifiés avec Scala
seo_desc: 'By Martin Budi

  Future is an abstraction to represent the completion of an asynchronous operation.
  Today it is commonly used in popular languages from Java to Dart. However, as modern
  applications are becoming more complex, composing them is also beco...'
---

Par Martin Budi

Future est une abstraction pour représenter l'achèvement d'une opération asynchrone. Aujourd'hui, il est couramment utilisé dans des langues populaires allant de Java à Dart. Cependant, à mesure que les applications modernes deviennent plus complexes, leur composition devient également plus difficile. Scala utilise une approche fonctionnelle qui facilite la visualisation et la construction de la composition des Futures.

Cet article vise à expliquer les bases de manière pragmatique. Pas de jargon, pas de terminologie étrangère. Vous n'avez même pas besoin d'être un programmeur Scala (pour l'instant). Tout ce dont vous avez besoin, c'est de comprendre quelques fonctions d'ordre supérieur : map et foreach. Alors, commençons.

En Scala, un future peut être créé aussi simplement que ceci :

```scala
Future {"Hi"} 
```

Maintenant, exécutons-le et faisons un "Hi World".

```scala
Future {"Hi"} .foreach (z => println(z + " World"))
```

C'est tout. Nous venons d'exécuter un future en utilisant `foreach`, nous avons manipulé le résultat un peu et nous l'avons imprimé sur la console.

Mais comment est-ce possible ? Nous associons normalement foreach et map aux collections : nous déballons le contenu et nous le manipulons. Si vous regardez, c'est conceptuellement similaire à un future dans la manière dont nous voulons déballer la sortie de `Future{}` et la manipuler. Pour que cela se produise, le future doit d'abord être complété, d'où le fait de l'exécuter. C'est le raisonnement derrière la composition fonctionnelle de Scala Future.

Dans les applications réalistes, nous voulons coordonner non pas un mais plusieurs futures à la fois. Un défi particulier est de savoir comment les organiser pour qu'ils s'exécutent **séquentiellement** ou **simultanément**.

#### **Exécution séquentielle**

Lorsque plusieurs futures commencent les uns après les autres comme une course de relais, nous appelons cela une exécution séquentielle. Une solution typique consisterait simplement à placer une tâche dans le callback de la tâche précédente, une technique connue sous le nom de chaînage. Le concept est correct mais ce n'est pas très joli.

En Scala, nous pouvons utiliser la compréhension for pour nous aider à l'abstraire. Pour voir à quoi cela ressemble, passons directement à un exemple.

```scala
import scala.concurrent.ExecutionContext.Implicits.global

object Main extends App {

  def job(n: Int) = Future {
    Thread.sleep(1000)
    println(n) // pour la démonstration uniquement car cela a des effets secondaires 
    n + 1
  }

  val f = for {
    f1 <- job(1)
    f2 <- job(f1)
    f3 <- job(f2)
    f4 <- job(f3)
    f5 <- job(f4)
  } yield List(f1, f2, f3, f4, f5)
  f.map(z => println(s"Terminé. ${z.size} jobs exécutés"))
  Thread.sleep(6000) // nécessaire pour empêcher le thread principal de quitter 
                     // trop tôt 
}
```

La première chose à faire est d'importer _ExecutionContext_ dont le rôle est de gérer le pool de threads. Sans cela, notre future ne s'exécutera pas.

Ensuite, nous définissons notre "gros travail" qui attend simplement une seconde et retourne son entrée incrémentée de un.

Ensuite, nous avons notre bloc de compréhension for. Dans cette structure, chaque ligne à l'intérieur attribue le résultat d'un travail à une valeur avec `<-` qui sera ensuite disponible pour tous les futures suivants. Nous avons organisé nos travaux de sorte que, sauf pour le premier, chacun prend la sortie du travail précédent.

De plus, notez que le résultat d'une compréhension for est également un future avec une sortie déterminée par **yield**. Après l'exécution, le résultat sera disponible à l'intérieur de `map`. Pour notre objectif, nous mettons simplement toutes les sorties des travaux dans une liste et prenons sa taille.

Exécutons-le.

![Image](https://cdn-media-1.freecodecamp.org/images/dzz5CXOB2TXLAzGnPcxQJpjjlgjaz-VomVBW)
_Exécution séquentielle_

Nous pouvons voir les cinq futures déclenchés un par un. Il est important de noter que cet arrangement ne doit être utilisé que lorsque le future dépend du future précédent.

#### **Exécution simultanée ou parallèle**

Si les futures sont indépendants les uns des autres, ils doivent être déclenchés simultanément. À cette fin, nous allons utiliser _Future.sequence_. Le nom est un peu déroutant, mais en principe, il prend simplement une liste de futures et la transforme en un future de liste. L'évaluation, cependant, est faite de manière asynchrone.

Créons un exemple de futures séquentiels et parallèles mixtes.

```scala
val f = for {
  f1 <- job(1)
  f2 <- Future.sequence(List(job(f1), job(f1)))
  f3 <- job(f2.head)
  f4 <- Future.sequence(List(job(f3), job(f3)))
  f5 <- job(f4.head)
} yield f2.size + f4.size
f.foreach(z => println(s"Terminé. $z jobs exécutés en parallèle"))
```

Future.sequence prend une liste de futures que nous souhaitons exécuter simultanément. Donc ici, nous avons f2 et f4 contenant deux jobs parallèles. Comme l'argument alimenté dans Future.sequence est une liste, le résultat est également une liste. Dans une application réaliste, les résultats peuvent être combinés pour un calcul ultérieur. Ici, nous allons prendre le premier élément de chaque liste avec `.head` puis le passer à f3 et f5 respectivement.

Voyons cela en action :

![Image](https://cdn-media-1.freecodecamp.org/images/9yDEuET5UU-nSsW8VyNKMY4rkBP9igBs8w7s)
_Exécution parallèle_

Nous pouvons voir les jobs dans 2 et 4 déclenchés simultanément, indiquant un parallélisme réussi. Il est intéressant de noter que l'exécution parallèle n'est pas toujours garantie car elle dépend des threads disponibles. S'il n'y a pas assez de threads, seuls certains des jobs s'exécuteront en parallèle. Les autres, cependant, attendront jusqu'à ce que davantage de threads soient libérés.

#### **Récupération des erreurs**

Scala Future incorpore **recover** qui agit comme un future de secours lorsqu'une erreur se produit. Cela permet à la composition des futures de se terminer même en cas d'échecs. Pour illustrer, considérons ce code :

```scala
Future {"abc".toInt}
.map(z => z + 1)
```

Bien sûr, cela ne fonctionnera pas, car "abc" n'est pas un int. Avec **recover**, nous pouvons le sauver en passant une valeur par défaut. Essayons de passer un zéro :

```scala
Future {"abc".toInt}
.recover {case e => 0}
.map(z => z + 1)
```

Maintenant, le code s'exécutera et produira un comme résultat. Dans la composition, nous pouvons ajuster chaque future comme ceci pour nous assurer que le processus nechouera pas.

Cependant, il arrive aussi que nous voulions rejeter explicitement les erreurs. À cette fin, nous pouvons utiliser _Future.successful_ et _Future.failed_ pour signaler le résultat de la validation. Et si nous ne nous soucions pas des échecs individuels, nous pouvons positionner recover pour attraper _n'importe quelle_ erreur à l'intérieur de la composition.

Travaillons un autre peu de code en utilisant la compréhension for qui vérifie si l'entrée est un int valide et inférieur à 100. Future.failed et Future.successful sont tous deux des futures, donc nous n'avons pas besoin de les envelopper dans un. Future.failed en particulier nécessite un _Throwable_, donc nous allons créer un personnalisé pour une entrée supérieure à 100. Après avoir tout assemblé, nous aurions ce qui suit :

```scala
val input = "5" // essayons "5", "200", et "abc"
case class NumberTooLarge() extends Throwable()
val f = for {
   f1 <- Future{ input.toInt }
   f2 <- if (f1 > 100) {
            Future.failed(NumberTooLarge())
          } else {
            Future.successful(f1)
          }
} yield f2
f map(println) recover {case e => e.printStackTrace()}
```

Remarquez le positionnement de recover. Avec cette configuration, il intercepta simplement toute erreur survenant à l'intérieur du bloc. Testons-le avec plusieurs entrées différentes "5", "200", et "abc" :

```
"5"   -> 5
"200" -> NumberTooLarge stacktrace
"abc" -> NumberFormatException stacktrace 
```

"5" a atteint la fin sans problème. "200" et "abc" sont arrivés dans recover. Maintenant, que se passe-t-il si nous voulons gérer chaque erreur séparément ? C'est là que la correspondance de motifs entre en jeu. En développant le bloc recover, nous pouvons avoir quelque chose comme ceci :

```scala
case e => 
  e match {
    case t: NumberTooLarge => // traiter le nombre > 100
    case t: NumberFormatException => // traiter le fait que ce n'est pas un nombre
    case _ => // traiter toute autre erreur
  }
}
```

Vous l'aurez probablement deviné, mais un scénario tout ou rien comme celui-ci est couramment utilisé dans les API publiques. Un tel service ne traiterait pas les entrées invalides mais devrait retourner un message pour informer le client de ce qu'il a fait de mal. En séparant les exceptions, nous pouvons passer un message personnalisé pour chaque erreur. Si vous souhaitez construire un tel service (avec un framework web très rapide), rendez-vous sur mon [article Vert.x](https://medium.freecodecamp.org/an-introduction-to-vert-x-the-fastest-java-framework-today-27d8661ceb14).

#### **Le monde en dehors de Scala**

Nous avons beaucoup parlé de la facilité d'utilisation des Futures de Scala. Mais est-ce vraiment le cas ? Pour y répondre, nous devons voir comment cela se fait dans d'autres langues. Arguablement, la langue la plus proche de Scala est Java, car les deux fonctionnent sur JVM. De plus, Java 8 a introduit l'API Concurrency avec _CompletableFuture_ qui est également capable de chaîner les futures. Retravaillons le premier exemple de séquence avec celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/LDS0WqYRsLYNTCV4gnEh0U6DsDn8HOUGi6lb)
_Exécution séquentielle en Java_

C'est sûr que c'est beaucoup de choses. Et pour coder cela, j'ai dû chercher _supplyAsync_ et _thenApply_ parmi tant de méthodes dans la documentation. Et même si je connais toutes ces méthodes, elles ne peuvent être utilisées que dans le contexte de l'API.

D'autre part, Scala Future n'est pas basé sur une API ou des bibliothèques externes mais sur un concept de programmation fonctionnelle qui est également utilisé dans d'autres aspects de Scala. Donc, avec un investissement initial dans la couverture des fondamentaux, vous pouvez récolter la récompense de moins de surcharge et de plus de flexibilité.

#### **Conclusion**

C'est tout pour les bases. Il y a plus à Scala Future, mais ce que nous avons ici a couvert suffisamment de terrain pour construire des applications réelles. Si vous souhaitez en savoir plus sur Future ou Scala en général, je recommande les [tutoriels d'Alvin Alexander](https://alvinalexander.com/scala/how-use-multiple-scala-futures-in-for-comprehension-loop), [AllAboutScala](http://allaboutscala.com/tutorials/chapter-9-beginner-tutorial-using-scala-futures/), et [l'article de Sujit Kamthe](https://medium.com/beingprofessional/understanding-functor-and-monad-with-a-bag-of-peanuts-8fa702b3f69e) qui offre des explications faciles à comprendre.