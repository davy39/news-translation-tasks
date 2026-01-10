---
title: Comment utiliser Thread.sleep sans bloquer sur la JVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-21T17:39:16.000Z'
originalURL: https://freecodecamp.org/news/non-blocking-thread-sleep-on-jvm
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/164b263b-0d10-452b-9bd0-b14c22adeb31-screen-shot-2019-11-15-at-122953-pm-4-1.png
tags:
- name: Java
  slug: java
- name: Scala
  slug: scala
seo_title: Comment utiliser Thread.sleep sans bloquer sur la JVM
seo_desc: 'By Daniel Sebban

  JVM Languages like Java and Scala have the ability to run concurrent code using
  the Thread  class. Threads are notoriously complex and very error prone, so having
  a solid understanding of how they work is essential.

  Let''s start with ...'
---

Par Daniel Sebban

Les langages JVM comme Java et Scala ont la capacité d'exécuter du code concurrent en utilisant la classe `Thread`. Les threads sont notoirement complexes et très sujets aux erreurs, donc avoir une solide compréhension de leur fonctionnement est essentiel.

Commençons par le Javadoc de `Thread.sleep`:

> Fait en sorte que le thread en cours d'exécution s'endorme (cesser temporairement l'exécution) pendant le nombre de millisecondes spécifié

Quelles sont les implications de « cesser l'exécution », également connu sous le nom de « blocage », et que signifie-t-il ? Est-ce mauvais ? Et si oui, pouvons-nous atteindre un « sommeil non bloquant » ?

### Ce que nous allons couvrir dans cet article

Cet article couvre beaucoup de terrain et, espérons-le, vous apprendrez beaucoup de choses intéressantes.

* Ce qui se passe au niveau du système d'exploitation lors de l'endormissement ?
* Le problème avec l'endormissement
* Project Loom et les threads virtuels
* La programmation fonctionnelle et la conception
* La bibliothèque ZIO Scala pour la concurrence

Oui, tout cela arrive ci-dessous.

Mais d'abord, commençons par ce simple extrait de code Scala que nous allons modifier tout au long de l'article pour atteindre ce que nous voulons :

```scala
println("a")
Thread.sleep(1000)
println("b")
```

C'est assez simple : il imprime « a » puis 10 secondes plus tard, il imprime « b »

Concentrons-nous sur `Thread.sleep` et essayons de comprendre COMMENT il parvient à endormir. Une fois que nous comprendrons le comment, nous pourrons voir le problème et le définir plus concrètement.

## Comment fonctionne l'endormissement au niveau du système d'exploitation ?

Voici ce qui se passe lorsque vous appelez `Thread.sleep` sous le capot.

* Il appelle l'API de thread du système d'exploitation sous-jacent
* Parce que la JVM utilise une correspondance un à un entre les threads Java et les threads du noyau, elle demande au système d'exploitation d'abandonner les « droits » du thread sur le CPU pendant le temps spécifié
* Lorsque le temps s'est écoulé, l'ordonnanceur du système d'exploitation réveillera le thread via une interruption (ce qui est efficace) et lui attribuera une tranche de temps CPU pour lui permettre de reprendre son exécution

Le point critique ici est que le thread en sommeil est complètement retiré et n'est pas réutilisable pendant son sommeil.

### Limitations des threads

Voici quelques limitations importantes qui accompagnent les threads :

* Il y a une limite au nombre de threads que vous pouvez créer. Après environ 30K, vous obtiendrez cette erreur :

```
java.lang.OutOfMemoryError : impossible de créer un nouveau thread natif
```

* Les threads JVM peuvent être coûteux en mémoire à créer, car ils viennent avec une pile dédiée
* Trop de threads JVM entraîneront des frais généraux en raison des changements de contexte coûteux et de la manière dont ils partagent les ressources matérielles finies

Maintenant que nous comprenons mieux ce qui se passe en coulisses, revenons au problème de l'endormissement.

## Le problème avec l'endormissement

Définissons le problème plus concrètement et exécutons un extrait pour montrer le problème auquel nous sommes confrontés. Nous utiliserons cette fonction pour illustrer le point :

```scala
def task(id: Int): Runnable = () =>
{
  println(s"${Thread.currentThread().getName()} start-$id")
  Thread.sleep(10000)
  println(s"${Thread.currentThread().getName()} end-$id")
}
```

Cette simple fonction va

* imprimer `**start**` suivi de l'identifiant du thread
* dormir pendant 10 secondes
* imprimer `**end**` suivi de l'identifiant du thread

### Votre mission, si vous l'acceptez, est d'exécuter 2 tâches simultanément avec 1 thread

Nous voulons exécuter 2 tâches simultanément, ce qui signifie que l'ensemble du programme devrait prendre un total de 10 secondes. Mais nous n'avons qu'un seul thread disponible.

Êtes-vous prêt pour ce défi ?

Jouons un peu avec le nombre de tâches et de threads pour avoir une idée de ce qu'est exactement le problème.

### `1 tâche -> 1 thread`

```scala
new Thread(task(1)).start()
```

```
12:11:08 INFO  Thread-0 start-1
12:11:18 INFO  Thread-0 end-1
```

Lançons `jvisualvm` pour voir ce que fait le thread :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vissualm_vm_1.png)

Vous pouvez voir que Thread-0 est dans l'état violet `sleeping`.

En cliquant sur le bouton de vidage de thread, cela imprimera :

```
"Thread-0" #13 prio=5 os_prio=31 tid=0x00007f9a3e0e2000 nid=0x5b03 waiting on condition [0x0000700004ac8000]
  java.lang.Thread.State: TIMED_WAITING (sleeping)
  at java.lang.Thread.sleep(Native Method)
  at example.Blog$.$anonfun$task$1(Blog.scala:7)
  at example.Blog$$$Lambda$2/1359484306.run(Unknown Source)
  at java.lang.Thread.run(Thread.java:748)
  Locked ownable synchronizers:        - None
```

Clairement, ce thread n'est plus utilisable jusqu'à ce qu'il termine son sommeil.

### `2 tâches -> 1 thread`

Illustrons le problème en exécutant 2 tâches avec seulement un thread disponible :

```scala
import java.util.concurrent.Executors

// un exécutant avec seulement 1 thread disponible
val oneThreadExecutor = Executors.newFixedThreadPool(1)

// envoyer 2 tâches à l'exécutant
(1 to 2).foreach(id =>
   oneThreadExecutor.execute(task(id)))
```

Nous obtenons cette sortie :

```
2020.09.28 21:49:56 INFO  pool-1-thread-1 start-1
2020.09.28 21:50:07 INFO  pool-1-thread-1 end-1
2020.09.28 21:50:07 INFO  pool-1-thread-1 start-2
2020.09.28 21:50:17 INFO  pool-1-thread-1 end-2
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/visualvm_3.png)

Vous pouvez voir la couleur violette (état de sommeil) pour `pool-1-thread-1`. Les tâches n'ont pas d'autre choix que de s'exécuter l'une après l'autre car le thread est retiré chaque fois que `Thread.sleep` est utilisé.

### `2 tâches -> 2 threads`

Exécutons le même code avec 2 threads disponibles. Nous obtenons ceci :

```scala
// un exécutant avec 2 threads disponibles
val oneThreadExecutor = Executors.newFixedThreadPool(2)

// envoyer 2 tâches à l'exécutant
(1 to 2).foreach(id =>
   oneThreadExecutor.execute(task(id)))
```

```
2020.09.28 22:42:04 INFO  pool-1-thread-2 start-2
2020.09.28 22:42:04 INFO  pool-1-thread-1 start-1
2020.09.28 22:42:14 INFO  pool-1-thread-1 end-1
2020.09.28 22:42:14 INFO  pool-1-thread-2 end-2
```

Chaque thread peut exécuter une tâche à la fois. Nous avons enfin accompli ce que nous voulions, exécuter 2 tâches simultanément, et l'ensemble du programme s'est terminé en 10 secondes.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/visulavm_4.png)

C'était facile car nous avons utilisé 2 threads (pool-1-thread-1 et pool-1-thread-2), mais nous voulons faire la même chose avec un seul thread.

Identifions le problème puis trouvons une solution.

### Le problème : `Thread.sleep est bloquant`

Nous comprenons maintenant que nous ne pouvons pas utiliser `Thread.sleep` – il bloque le thread.

Cela le rend inutilisable jusqu'à ce qu'il reprenne, nous empêchant d'exécuter 2 tâches simultanément.

Heureusement, il existe des solutions, que nous allons discuter ensuite.

## Première solution : Mettre à jour votre JVM avec Project Loom

J'ai mentionné précédemment que les threads JVM mappent un à un aux threads du système d'exploitation. Et cette erreur de conception fatale nous amène ici.

[Project Loom](https://wiki.openjdk.java.net/display/loom/Main) vise à corriger cela en ajoutant des threads virtuels.

Voici notre code réécrit en utilisant des threads virtuels de Loom :

```scala
Thread.startVirtualThread(() -> {
  System.out.println("a")
  Thread.sleep(1000)
  System.out.println("b")
});
```

L'incroyable chose est que le `Thread.sleep` ne bloquera plus ! Il est entièrement asynchrone. Et en plus de cela, les threads virtuels sont super bon marché. Vous pourriez en créer des centaines de milliers sans frais généraux ni limitations.

Tous nos problèmes sont résolus maintenant – à part le fait que Project Loom ne sera pas disponible avant au moins JDK 17 (prévu pour septembre 2021).

Oh bien, revenons en arrière et essayons de résoudre le problème de l'endormissement avec ce que la JVM nous donne actuellement.

### Idée clé : Vous pouvez exprimer l'endormissement en termes de planification d'une tâche dans le futur

Si vous dites à votre patron que vous êtes occupé et que vous reprenez votre travail dans 10 minutes, votre patron ne sait pas que vous êtes sur le point de faire une sieste. Ils voient seulement que vous avez commencé votre travail le matin, puis avez fait une pause de 10 minutes avant de reprendre.

Ceci :

```
start
sleep(10)
end
```

est équivalent de l'extérieur à ceci :

```
start
resumeIn(10s, end)
```

Ce que nous avons fait ci-dessus est de PLANIFIER la tâche pour qu'elle se termine dans 10 secondes.

C'est tout, nous n'avons plus besoin de dormir. Nous devons simplement être capables de planifier des choses dans le futur à la place.

Nous avons réduit un problème avec un autre, qui est plus facile et a une solution plus simple.

### Le problème de la planification

Heureusement pour nous, la planification des tâches est très simple à faire. Nous devons simplement changer l'exécutant comme suit :

```
val oneThreadScheduleExecutor = Executors.newScheduledThreadPool(1)
```

Nous pouvons maintenant utiliser la fonction `schedule` au lieu de `execute` :

```scala
oneThreadScheduleExecutor.schedule
(task(1),10, TimeUnit.SECONDS)
```

Ce n'est pas exactement ce que nous voulons. Nous voulons séparer l'impression de début et de fin par 10 secondes, alors modifions notre fonction de tâche comme suit :

```scala
def nonBlockingTask(id: Int): Runnable = () => {
  println(s"${Thread.currentThread().getName()} start-$id")
  val endTask: Runnable = () =>
  {
    println(s"${Thread.currentThread().getName()} end-$id")
  }
  //au lieu de Thread.sleep pendant 10s, nous le planifions dans le futur, plus de blocage !
  oneThreadScheduleExecutor.schedule(endTask, 10, TimeUnit.SECONDS)
}
```

```
2020.09.28 23:35:45 INFO  pool-1-thread-1 start-1
2020.09.28 23:35:45 INFO  pool-1-thread-1 start-2
2020.09.28 23:35:56 INFO  pool-1-thread-1 end-1
2020.09.28 23:35:56 INFO  pool-1-thread-1 end-2
```

Oui ! Nous l'avons fait ! Un seul thread et 2 tâches concurrentes qui « dorment » 10 secondes chacune.

D'accord, c'est super, mais vous ne pouvez pas vraiment écrire du code comme ça. Et si vous voulez une autre tâche au milieu comme suit :

```
00:00:00 start
00:00:10 middle
00:00:20 end
```

Vous devriez changer l'implémentation de la `nonBlockingTask` et ajouter un autre appel à `schedule` là-dedans. Et cela va devenir très désordonné très rapidement.

## Comment utiliser la programmation fonctionnelle pour écrire un DSL avec un sommeil non bloquant

La programmation fonctionnelle en Scala est un plaisir, et écrire un DSL (langage spécifique à un domaine) en utilisant les principes de la PF est assez facile.

Commençons par la fin. Nous aimerions que notre programme final ressemble à quelque chose comme ceci :

```scala
def nonBlockingFunctionalTask(id: Int) = {
  Print(id,"start") andThen 
  Print(id,"middle").sleep(1000) andThen
  Print(id,"end").sleep(1000)
}
```

Ce mini-langage atteindra exactement le même comportement que notre solution précédente mais sans exposer toutes les vilaines internes de l'exécutant planifié et des threads.

### Le modèle

Définissons nos types de données :

```scala
object Task {
sealed trait Task { self =>
  def andThen(other: Task) = AndThen(self,other)
  def sleep(millis: Long) = Sleep(self,millis)
}
  
case class AndThen(t1: Task, t2: Task) extends Task
case class Print(id: Int, value: String) extends Task 
case class Sleep(t1: Task, millis: Long) extends Task
```

En PF, les types de données ne contiennent que des données et aucun comportement. Donc ce code entier ne fait « rien » – il capture simplement la structure du langage et les informations que nous voulons.

Nous avons besoin de 2 fonctions :

* `sleep` pour faire dormir une tâche
* `andThen` pour enchaîner les tâches

Remarquez que leur implémentation ne fait rien. Il l'enveloppe simplement dans la bonne classe et c'est tout.

Utilisons notre fonction `nonBlockingFunctionalTask` :

```scala
import Task._
//créer 2 tâches, cela ne les exécute pas, aucun thread impliqué ici
(1 to 2).toList.map(nonBlockingFunctionalTask)
```

C'est une description du problème. Cela ne fait rien, il construit simplement une liste avec 2 tâches, chacune décrivant ce qu'il faut faire.

Si nous imprimons le résultat dans le REPL, nous obtenons ceci :

```scala
res3: List[Task] = List(
//première tâche
AndThen(AndThen(Print(1,start),Sleep(Print(1,middle),10000)),Sleep(Print(1,end),10000)), 
//deuxième tâche
AndThen(AndThen(Print(2,start),Sleep(Print(2,middle),10000)),Sleep(Print(2,end),10000))
)
```

Écrivons l'`interprète` qui transformera cet arbre en un arbre qui exécute réellement les tâches.

### L'interprète

En PF, la fonction qui transforme une description en un programme exécutable est appelée l'`interprète`. Il prend la description du programme, le modèle, et l'interprète en une forme exécutable. Ici, il exécutera et planifiera les tâches directement.

Nous avons d'abord besoin d'une `Stack` qui nous permettra d'encoder les dépendances entre les tâches. Pensez que `start >>= middle >>= end` sera poussé dans la pile puis retiré dans l'ordre d'exécution. Cela sera évident dans l'implémentation.

Et maintenant l'interprète (ne vous inquiétez pas si vous ne comprenez pas ce code, il est un peu compliqué, une solution plus simple arrive) :

```scala
def interpret(task: Task, executor: ScheduledExecutorService): Unit = {
  def loop(current: Task, stack: Stack[Task]): Unit =
  current match {
    case AndThen(t1, t2) =>
      loop(t1,stack.push(t2))
    case Print(id, value) =>
      stack.pop match {
        case Some((t2, b)) =>
          executor.execute(() => {
          println(s"${Thread.currentThread().getName()} $value-$id")
          })
        loop(t2,b)
        case None =>
          executor.execute(() => {
          println(s"${Thread.currentThread().getName()} $value-$id")
          })
    case Sleep(t1,millis) =>
      val r: Runnable = () =>{loop(t1,stack)}
      executor.schedule(r, millis, TimeUnit.MILLISECONDS)
}
loop(task,Nil)
}
```

Et la sortie est ce que nous voulons :

```
2020.09.29 00:06:39 INFO  pool-1-thread-1 start-1
2020.09.29 00:06:39 INFO  pool-1-thread-1 start-2
2020.09.29 00:06:50 INFO  pool-1-thread-1 middle-1
2020.09.29 00:06:50 INFO  pool-1-thread-1 middle-2
2020.09.29 00:07:00 INFO  pool-1-thread-1 end-1
2020.09.29 00:07:00 INFO  pool-1-thread-1 end-2
```

Un thread exécutant 2 tâches de sommeil concurrentes. C'est beaucoup de code et beaucoup de travail. Comme d'habitude, vous devriez toujours vous demander s'il existe une bibliothèque qui résout déjà ce problème. Il s'avère qu'il y en a une : ZIO.

## Sommeil non bloquant dans ZIO

`**[ZIO](https://zio.dev/)**` est une bibliothèque fonctionnelle pour la programmation asynchrone et concurrente. Elle fonctionne de manière similaire à notre petit DSL, car elle vous donne quelques types que vous pouvez mélanger et assortir pour décrire votre programme et rien de plus.

Et ensuite, elle nous donne un interprète qui vous permet d'exécuter un programme ZIO.

Comme je l'ai dit, ce modèle d'interprète est omniprésent dans le monde de la PF. Une fois que vous l'avez compris, un nouveau monde s'ouvre à vous.

### `ZIO.sleep` – une meilleure version de `Thread.sleep`

`ZIO` nous donne la fonction `ZIO.sleep`, une version non bloquante de `Thread.sleep`. Voici notre fonction écrite en utilisant `ZIO` :

```scala
import zio._
import zio.console._
import zio.duration._
object ZIOApp extends zio.App {
def zioTask(id: Int) =
  for {
  _ <- putStrLn(s"${Thread.currentThread().getName()} start-$id")
  _ <- ZIO.sleep(10.seconds)
  _ <- putStrLn(s"${Thread.currentThread().getName()} end-$id")
} yield ()
```

C'est frappant de similitude avec le premier extrait :

```scala
def task(id: Int): Runnable = () =>
{
  println(s"${Thread.currentThread().getName()} start-$id")
  Thread.sleep(10000)
  println(s"${Thread.currentThread().getName()} end-$id")
}
```

La différence claire est la syntaxe `for` qui nous permet d'enchaîner des instructions avec le type `ZIO`. C'est très similaire à la fonction `andThen` de notre précédent mini-langage.

Comme avant avec notre mini-langage, ce programme est juste une description. C'est des données pures, et cela ne fait rien. Pour faire quelque chose, nous avons besoin de l'interprète.

### L'interprète ZIO

Pour interpréter un programme ZIO, vous devez simplement étendre l'interface `ZIO.App` et le mettre dans la méthode `run` et `ZIO` se chargera de l'exécuter, comme ceci :

```scala
object ZIOApp extends zio.App
{
 override def run(args: List[String]) = {
  ZIO
  //démarrer 2 tâches ZIO en parallèle
  .foreachPar((1 to 2))(zioTasks)
  //programme complet lorsqu'il est terminé
  .as(ExitCode.success)
}
```

Et nous obtenons cette sortie – les tâches se terminent correctement en 10 secondes :

```
2020.09.29 00:45:12 INFO  zio-default-async-3-1594199808 start-2
2020.09.29 00:45:12 INFO  zio-default-async-2-1594199808 start-1
2020.09.29 00:45:33 INFO  zio-default-async-7-1594199808 end-1
2020.09.29 00:45:33 INFO  zio-default-async-8-1594199808 end-2
```

## Points clés

* Chaque thread JVM correspond à un thread du système d'exploitation, de manière **un à un**. Et c'est la racine de beaucoup de problèmes.
* `Thread.sleep` est mauvais ! Il **bloque le thread actuel** et le rend inutilisable pour un travail ultérieur.
* **Project Loom** (qui sera disponible dans JDK 17) résoudra beaucoup de problèmes. [Voici une conférence intéressante à ce sujet](https://www.youtube.com/watch?v=SJeAb-XEIe8).
* Vous pouvez utiliser `ScheduledExecutorService` pour atteindre un **sommeil non bloquant**.
* Vous pouvez utiliser la **programmation fonctionnelle pour modéliser un langage** où faire dormir est non bloquant.
* La **bibliothèque ZIO** fournit un sommeil non bloquant dès la sortie de la boîte.