---
title: 'Multithreading en Java : Comment commencer avec les threads'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T13:45:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-multithreading-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/how-to-get-started-with-multithreading-in-java.jpg
tags:
- name: Backend Development
  slug: backend-development
- name: concurrency
  slug: concurrency
- name: Java
  slug: java
- name: Threading
  slug: threading
seo_title: 'Multithreading en Java : Comment commencer avec les threads'
seo_desc: 'By Aditya Sridhar

  What is a Thread?

  A thread is a lightweight process. Any process can have multiple threads running
  in it.

  For example in a web browser, we can have one thread which will load the user interface
  and another thread which will actually...'
---

Par Aditya Sridhar

# Qu'est-ce qu'un Thread ?

Un thread est un processus léger. Tout processus peut avoir plusieurs threads en cours d'exécution.

Par exemple, dans un navigateur web, nous pouvons avoir un thread qui charge l'interface utilisateur et un autre thread qui récupère toutes les données à afficher dans cette interface.

# Qu'est-ce que le Multithreading ?

Le multithreading nous permet d'exécuter plusieurs threads simultanément.

Par exemple, dans un navigateur web, nous pouvons avoir un thread qui gère l'interface utilisateur, et en parallèle, un autre thread qui récupère les données à afficher.

Ainsi, le multithreading améliore la réactivité d'un système.

# Qu'est-ce que la Concurrence ?

La concurrence dans le contexte des threads nous permet d'exécuter plusieurs threads en même temps.

Mais les threads s'exécutent-ils vraiment en même temps ?

## Systèmes à un seul cœur

Le **Thread Scheduler** fourni par la JVM décide quel thread s'exécute à un moment donné. Le planificateur donne un petit intervalle de temps à chaque thread.

Ainsi, à un moment donné, nous n'avons qu'un seul thread qui s'exécute réellement dans le processeur. Mais grâce au découpage temporel, nous avons l'impression que plusieurs threads s'exécutent en même temps.

## Systèmes multicœurs

Même dans les systèmes multicœurs, le planificateur de threads est impliqué. Mais comme nous avons plusieurs cœurs, nous pouvons avoir plusieurs threads s'exécutant exactement au même moment.

Par exemple, si nous avons un système à double cœur, nous pouvons avoir 2 threads s'exécutant exactement au même moment. Le premier thread s'exécutera dans le premier cœur, et le second thread s'exécutera dans le second cœur.

# Pourquoi le Multithreading est-il nécessaire ?

Le multithreading nous permet d'améliorer la réactivité d'un système.

Par exemple, dans un navigateur web, si tout s'exécutait dans un seul thread, le système serait complètement non réactif chaque fois que des données seraient récupérées pour être affichées. Par exemple, si cela prend 10 secondes pour récupérer les données, alors pendant ces 10 secondes, nous ne pourrons rien faire d'autre dans le navigateur web, comme ouvrir de nouveaux onglets ou même fermer le navigateur.

Ainsi, l'exécution de différentes parties d'un programme dans différents threads de manière concurrente aide à améliorer la réactivité d'un système.

# Comment écrire des programmes Multithread en Java

Nous pouvons créer des threads en Java en utilisant les méthodes suivantes :

* En étendant la classe Thread
* En implémentant l'interface Runnable
* En implémentant l'interface Callable
* En utilisant le framework Executor avec des tâches Runnable et Callable

Nous examinerons les Callables et le framework Executor dans un autre article de blog. Dans cet article, je me concentrerai principalement sur l'extension de la classe Thread et l'implémentation de l'interface Runnable.

## Étendre la classe Thread

Pour créer un morceau de code qui peut être exécuté dans un thread, nous créons une classe et étendons ensuite la classe **Thread**. La tâche effectuée par ce morceau de code doit être placée dans la fonction **run()**.

Dans le code ci-dessous, vous pouvez voir que **Worker** est une classe qui étend la classe **Thread**, et la tâche d'imprimer les nombres de 0 à 5 est effectuée à l'intérieur de la fonction **run()**.

```java
class Worker extends Thread {

	@Override
	public void run() {
		for (int i = 0; i <= 5; i++) {
			System.out.println(Thread.currentThread().getName() + ": " + i);
		}
	}

}

```

Dans le code ci-dessus, **Thread.currentThread().getName()** est utilisé pour obtenir le nom du thread actuel qui exécute le code.

Pour créer un **thread**, nous devons simplement créer une instance de la classe Worker. Ensuite, nous pouvons démarrer le thread en utilisant la fonction **start()**.

```java
public class ThreadClassDemo {
	public static void main(String[] args) {
		Thread t1 = new Worker();
		Thread t2 = new Worker();
		Thread t3 = new Worker();
		t1.start();
		t2.start();
		t3.start();

	}
}

```

Dans le code ci-dessus, nous créons 3 threads (t1, t2 et t3) à partir de la classe Worker. Ensuite, nous démarrons les threads en utilisant la fonction **start()**.

Voici le code final pour créer un thread en étendant une classe Thread :

```java
class Worker extends Thread {

	@Override
	public void run() {
		for (int i = 0; i <= 5; i++) {
			System.out.println(Thread.currentThread().getName() + ": " + i);
		}
	}

}

public class ThreadClassDemo {
	public static void main(String[] args) {
		Thread t1 = new Worker();
		Thread t2 = new Worker();
		Thread t3 = new Worker();
		t1.start();
		t2.start();
		t3.start();

	}
}

```

Voici le résultat que nous obtenons en exécutant le code ci-dessus :

![Sortie de la classe Thread](https://adityasridhar.com/assets/img/posts/how-to-get-started-with-multithreading-in-java/thread-class-output.png)

Vous pouvez voir que les 3 threads ont imprimé les nombres de 0 à 5.

**Vous pouvez également voir clairement à partir de la sortie que les 3 threads ne s'exécutent pas dans un ordre particulier.**

## Implémenter l'interface Runnable

Pour créer un morceau de code qui peut être exécuté dans un thread, nous créons une classe et implémentons ensuite l'interface **Runnable**. La tâche effectuée par ce morceau de code doit être placée dans la fonction **run()**.

Dans le code ci-dessous, vous pouvez voir que **RunnableWorker** est une classe qui implémente l'interface **Runnable**, et la tâche d'imprimer les nombres de 0 à 4 est effectuée à l'intérieur de la fonction **run()**.

```java
class RunnableWorker implements Runnable{

	@Override
	public void run() {
		for (int i = 0; i <= 4; i++) {
			System.out.println(Thread.currentThread().getName() + ": " + i);
		}
	}
	
}

```

Pour créer un thread, nous devons d'abord créer une instance de **RunnableWorker** qui implémente l'interface **Runnable**.

Ensuite, nous pouvons créer un nouveau thread en créant une instance de la classe **Thread** et en passant l'instance de **RunnableWorker** comme argument. Cela est montré dans le code ci-dessous :

```java
public class RunnableInterfaceDemo {

	public static void main(String[] args) {
		Runnable r = new RunnableWorker();
		Thread t1 = new Thread(r);
		Thread t2 = new Thread(r);
		Thread t3 = new Thread(r);
		
		t1.start();
		t2.start();
		t3.start();

	}

}

```

Le code ci-dessus crée une instance Runnable r. Ensuite, il crée 3 threads (t1, t2 et t3) et passe **r** comme argument aux 3 threads. Ensuite, la fonction **start()** est utilisée pour démarrer les 3 threads.

Voici le code complet pour créer un thread en implémentant l'interface Runnable :

```java
class RunnableWorker implements Runnable{

	@Override
	public void run() {
		for (int i = 0; i <= 4; i++) {
			System.out.println(Thread.currentThread().getName() + ": " + i);
		}
	}
	
}

public class RunnableInterfaceDemo {

	public static void main(String[] args) {
		Runnable r = new RunnableWorker();
		Thread t1 = new Thread(r);
		Thread t2 = new Thread(r);
		Thread t3 = new Thread(r);
		
		t1.start();
		t2.start();
		t3.start();

	}

}

```

En exécutant le code ci-dessus, nous obtiendrons le résultat suivant. La séquence de la sortie changera à chaque exécution du code.

![Sortie de l'interface Runnable](https://adityasridhar.com/assets/img/posts/how-to-get-started-with-multithreading-in-java/runnable-interface-output.png)

**Implémenter l'interface Runnable est une meilleure option que d'étendre la classe Thread, car nous ne pouvons étendre qu'une seule classe, mais nous pouvons implémenter plusieurs interfaces en Java.**

## Interface Runnable en Java 8

En Java 8, l'interface Runnable devient une **FunctionalInterface** car elle n'a qu'une seule fonction, **run()**.

Le code ci-dessous montre comment nous pouvons créer une instance Runnable en Java 8.

```java
public class RunnableFunctionalInterfaceDemo {

	public static void main(String[] args) {
		
		Runnable r = () -> {
			for (int i = 0; i <= 4; i++) {
				System.out.println(Thread.currentThread().getName() + ": " + i);
			}
		};
		
		Thread t1 = new Thread(r);
		Thread t2 = new Thread(r);
		Thread t3 = new Thread(r);
		
		t1.start();
		t2.start();
		t3.start();
	}

}

```

Ici, au lieu de créer une classe et d'implémenter ensuite l'interface Runnable, nous pouvons directement utiliser une expression lambda pour créer une instance Runnable comme montré ci-dessous :

```java
Runnable r = () -> {
        for (int i = 0; i <= 4; i++) {
            System.out.println(Thread.currentThread().getName() + ": " + i);
        }
    };

```

# Code

Le code de cet article est disponible dans le dépôt GitHub suivant : [https://github.com/aditya-sridhar/basic-threads-demo](https://github.com/aditya-sridhar/basic-threads-demo)

# Félicitations 🎉

Vous savez maintenant comment créer des threads en étendant la classe Thread et en implémentant l'interface Runnable.

Je discuterai du cycle de vie des threads et des défis liés à l'utilisation des threads dans mon prochain article de blog.

**Mon site web** : [https://adityasridhar.com/](https://adityasridhar.com/)

N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/aditya1811) ou à me suivre sur [Twitter](https://www.twitter.com/adityasridhar18)