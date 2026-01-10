---
title: Qu'est-ce que les Threads en Java ? Comment créer un Thread avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-28T22:23:36.000Z'
originalURL: https://freecodecamp.org/news/what-are-threads-in-java-how-to-create-one
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Copy-of-Copy-of-How-Encapsulation-is-Achieved-in-Python--1-.png
tags:
- name: Java
  slug: java
- name: multithreading
  slug: multithreading
seo_title: Qu'est-ce que les Threads en Java ? Comment créer un Thread avec des exemples
seo_desc: "By Bikash Daga (Jain)\nThreads in Java are pre-defined classes that are\
  \ available in the java.package when you write your programs. Generally, every program\
  \ has one thread which is provided from the java.package. \nAll of these threads\
  \ use the same mem..."
---

Par Bikash Daga (Jain)

Les threads en Java sont des classes prédéfinies disponibles dans le package java lorsque vous écrivez vos programmes. Généralement, chaque programme dispose d'un thread fourni par le package java.

Tous ces threads utilisent la même mémoire, mais ils sont indépendants. Cela signifie qu'une exception dans un thread n'affectera pas le fonctionnement des autres threads, malgré le partage de la même mémoire.

## Ce que vous allez apprendre :

* Dans cet article, nous apprendrons à créer un thread
* Nous apprendrons le concept de multitâche.
* Nous apprendrons le cycle de vie des threads ainsi que la classe thread.

## Qu'est-ce qu'un Thread en Java ?

Les threads nous permettent de faire les choses plus rapidement en Java. C'est-à-dire qu'ils nous aident à effectuer plusieurs choses à la fois.

Vous utilisez des threads pour effectuer des opérations complexes sans perturber le programme principal.

Lorsque divers threads sont exécutés simultanément, ce processus est connu sous le nom de multithreading.

Le [multithreading](https://www.freecodecamp.org/news/how-to-get-started-with-multithreading-in-java/) est principalement utilisé dans les jeux et programmes similaires. Maintenant que nous en savons un peu sur le multithreading, apprenons également le concept de multitâche.

## Qu'est-ce que le Multitâche en Java ?

Le [multitâche](https://www.techtarget.com/whatis/definition/multitasking) est le processus qui permet aux utilisateurs d'effectuer plusieurs tâches en même temps. Il existe deux façons d'activer le multitâche en Java :

1. **Multitâche basé sur les processus** : Les processus dans ce type de multitâche sont lourds et consomment beaucoup de temps. Cela est dû au fait que le programme met longtemps à basculer entre différents processus.
2. **Multitâche basé sur les threads** : Les threads sont légers par rapport au multitâche basé sur les processus, et le temps nécessaire pour basculer entre eux est plus court.

Maintenant, apprenons le modèle de fonctionnement d'un thread.

## Cycle de vie d'un Thread en Java

### Qu'est-ce qu'un cycle de vie de thread en Java ?

En Java, un thread restera toujours dans l'un des quelques états différents (que nous allons lire ci-dessous).

Le thread passe par diverses étapes dans son cycle de vie. Par exemple, un thread est d'abord né, puis il est démarré, et traverse ces diverses étapes jusqu'à ce qu'il meure.

Le modèle de thread se compose de divers états. Apprenons chacun d'eux en détail :

1. **Nouveau** : le modèle est dans l'état nouveau lorsque le code n'est pas encore en cours d'exécution.
2. **État d'exécution ou stade actif** : c'est l'état lorsque le programme est en cours d'exécution ou est prêt à être exécuté.
3. **État suspendu** : vous pouvez utiliser cet état si vous souhaitez mettre en pause l'activité lorsqu'un événement spécifique se produit (et vous permet d'arrêter temporairement l'exécution).
4. **État bloqué** : un thread est dans l'état bloqué lorsqu'il attend des ressources. Dans l'état bloqué, l'ordonnanceur de threads efface la file d'attente en rejetant les threads indésirables qui sont présents.
5. **État terminé** : cet état arrête l'exécution d'un thread immédiatement. Un thread terminé signifie qu'il est mort et n'est plus disponible pour une utilisation.

## Méthodes de Thread

### Quelles sont les méthodes de thread en Java ?

Les méthodes de thread en Java sont très importantes lorsque vous travaillez avec une application multithread. La classe thread possède certaines méthodes importantes qui sont décrites par le thread lui-même.

Maintenant, apprenons chacune de ces méthodes :

1. **public void start()** : vous utilisez cette méthode pour démarrer le thread dans un chemin d'exécution séparé. Ensuite, elle appelle la méthode run() sur l'objet thread.
2. **public void run()** : cette méthode est le point de départ du thread. L'exécution du thread commence à partir de ce processus.
3. **public final void setName()** : cette méthode change le nom de l'objet thread. Il existe également une méthode `getName()` pour récupérer le nom du contexte actuel.
4. **public final void setPriority()** : vous utilisez cette méthode pour définir les valeurs de l'objet thread.
5. **public void sleep()** : vous utilisez cette méthode pour suspendre le thread pendant une durée particulière.
6. **public void interrupt()** : vous utilisez cette méthode pour interrompre un thread particulier. Elle permet également de continuer l'exécution s'il était bloqué pour une raison quelconque.
7. **public final boolean isAlive()** : cette méthode retourne vrai si le thread est vivant.

Maintenant, apprenons à créer un thread.

## Comment créer un Thread en Java

Il existe deux façons de créer un thread :

Premièrement, vous pouvez créer un thread en utilisant la classe thread (syntaxe extend). Cela vous fournit des constructeurs et des méthodes pour créer et opérer sur des threads.

La classe thread étend la classe objet et implémente une interface runnable. La classe thread en Java est la classe principale sur laquelle repose le système multithread de Java.

Deuxièmement, vous pouvez créer un thread en utilisant une interface runnable. Vous pouvez utiliser cette méthode lorsque vous savez que la classe avec l'instance est destinée à être exécutée par le thread lui-même.

L'interface runnable est une interface en Java qui est utilisée pour exécuter un thread concurrent. L'interface runnable n'a qu'une seule méthode qui est `run()`.

Maintenant, voyons la syntaxe des deux :

#### Comment utiliser la syntaxe extend :

```
public class Main extends thread {
  public void test() {
    System.out.println("Les threads sont très utiles en java");
  }
}

```

Voici un exemple de la méthode `extend` :

```
public class Main extends test {
  public static void main(String[] args) {
    Main test = new Main();
    test.start();
    System.out.println("Les threads sont très utiles en java");
  }
  public void run() {
    System.out.println("Les threads sont très utiles en java");
  }
}

```

En utilisant la syntaxe de la classe étendue, nous venons de l'implémenter dans cet exemple. Exécutez le code ci-dessus dans votre éditeur pour voir comment il fonctionne.

#### Comment utiliser une interface runnable :

```
public class Main implements runnable {
  public void test() {
    System.out.println("Les threads sont très utiles en java");
  }
}
```

Et voici un exemple d'utilisation d'une [interface runnable](https://docs.oracle.com/javase/7/docs/api/java/lang/Runnable.html) :

```
public class cal implements test {
  public static void main(String[] args) {
    cal obj = new cal();
    Thread thread = new Thread(obj);
    thread.start();
    System.out.println("Les threads sont très utiles en java");
  }
  public void run() {
    System.out.println("Les threads sont très utiles en java");
  }
}

```

Puisque nous avons étendu la classe thread, notre objet de classe ne sera pas traité comme un objet thread. Exécutez le code ci-dessus dans votre compilateur pour voir comment il fonctionne.

## Comment implémenter des Threads en Java – Exemples

Voyons quelques exemples supplémentaires d'implémentation de [threads en Java](https://www.scaler.com/topics/thread-in-java/) :

```
class First
{
public static void main (String [ ]args) throws IOException
{
Thread t =Thread.currentThread( );
System.out.println("CURRENTTHREAD = " + t);
t.setName("NewThread");
t.setPriority(t.getPriority( ) - 1);
System.out.println("CURRENTTHREAD = " + t);
System.out.println("NAME = " + t.getName( ));
}
}

```

#### Sortie

```
CURRENTTHREAD =THREAD [main, 5, main]
CURRENTTHREAD =THREAD [New Thread, 4, main]
NAME = New Thread

```

Ici, nous avons créé un thread puis imprimé le thread actuel. Ensuite, nous avons défini le nom du thread comme un nouveau thread et enfin nous avons imprimé le nom du thread. Exécutez le code ci-dessus dans votre éditeur pour voir comment il fonctionne.

Voici un autre exemple :

```
class First implements Runnable
{
Thread t;
First( ){
t = new Thread(this,"NEW");
System.out.println("CHILD :" + t);
t.start();
}
public void run( ) {
try{ for(int i = 5; i>0, i- -) {
System.out.println("CHILD :" + i);
Thread.sleep(500); }
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING CHILD");
} }
class Second
{
public static void main(String [ ]args) throws IOException
{
new First();
try{
for(int i = 5; i>0, i- -)
{
System.out.println("MAIN :"  + i);
Thread.sleep(1000);
}
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("Exiting man");
}
}

```

#### Sortie

```
CHILD = THREAD [NEW, 5, main]
MAIN : 5
CHILD : 5
CHILD : 4
MAIN : 4
CHILD : 3
CHILD : 2
MAIN : 3
CHILD : 1
EXITING CHILD
MAIN : 2
MAIN : 1
EXITING MAIN

```

Ici, nous avons créé un thread puis imprimé le thread enfant. Ensuite, nous avons exécuté la boucle for à l'intérieur de la fonction run et imprimé l'enfant. Exécutez le code dans votre éditeur pour voir comment il fonctionne.

Maintenant, apprenons-en plus sur le multithreading.

## Multithreading en Java

Comme je l'ai brièvement expliqué ci-dessus, le multithreading en Java fait référence à l'exécution de plusieurs threads en même temps.

Le multithreading est utile car les threads sont indépendants – et dans le multithreading, nous pouvons effectuer l'exécution de plusieurs threads en même temps sans bloquer l'utilisateur.

Cela nous aide également à gagner du temps car nous pouvons effectuer plusieurs opérations en même temps. Un bon exemple en temps réel de multithreading en Java est le traitement de texte. Ce programme vérifie l'orthographe de ce que nous tapons pendant que nous écrivons un document. Dans ce cas, chaque tâche sera fournie par un thread différent.

### Cas d'utilisation du multithreading en Java

Maintenant que vous savez comment le multithreading économise du temps en vous permettant d'effectuer plusieurs opérations ensemble, apprenons quelques cas d'utilisation pratiques du multithreading :

1. Le traitement de texte, dont nous avons discuté ci-dessus.
2. Les jeux.
3. Améliorer la réactivité d'un serveur.
4. Utiliser des fonctions de synchronisation de threads pour fournir des processus améliorés à la communication de processus.

Maintenant, regardons un exemple de programme pour apprendre à implémenter le multithreading :

```
class First implements Runnable
{
Thread t; String S;
First(String Name){
S=Name;
t = new Thread(this,S);
System.out.println("CHILD :" + t);
t.start();
}
public void run( ) {
try{ for(int i = 5; i>0, i- -) {
System.out.println(S + " :" + i);
Thread.sleep(1000); }
} //END OF TRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING " + S);
} 
}
class Second
{
public static void main(String [ ]args) throws IOException
{
new First("ONE");
new First("TWO");
new First("THREE");
try{
Thread.sleep(20000);
} //END OFTRY BLOCK
catch(InterruptedException e){ }
System.out.println("EXITING MAIN");

```

#### Sortie

```
CHILD =THREAD [ONE, 5, main]
CHILD =THREAD [TWO, 5, main]
CHILD =THREAD [THREE, 5, main]
ONE : 5 ONE : 2
TWO : 5 TWO : 2
THREE : 5 THREE:2
ONE : 4 ONE : 1
TWO : 4 TWO : 1
THREE : 4 THREE : 1
ONE : 3 EXITING ONE
TWO : 3 EXITINGTWO
THREE : 3 EXITINGTHREE
EXITING MAIN

```

Dans le code ci-dessus, nous avons implémenté le multithreading en utilisant la méthode run. Ensuite, nous avons initié un thread en utilisant le constructeur, puisque le thread est créé à partir de celui-ci. Ensuite, nous pouvons commencer en appelant la méthode start(). Exécutez le code dans votre éditeur pour voir comment il fonctionne.

## Conclusion

Un thread est un processus léger en Java. C'est un chemin d'exécution au sein d'un processus. Il n'existe que deux méthodes pour créer des threads en Java.

Dans un navigateur, plusieurs onglets peuvent être plusieurs threads. Une fois qu'un thread est créé, il peut être présent dans l'un des états que nous avons discutés ci-dessus.

Merci d'avoir lu.