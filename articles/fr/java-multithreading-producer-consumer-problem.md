---
title: Comment résoudre le problème producteur-consommateur en Java en utilisant le
  multithreading
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-03-04T17:48:32.000Z'
originalURL: https://freecodecamp.org/news/java-multithreading-producer-consumer-problem
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/producer-consumer-problem-image.jpeg
tags:
- name: Java
  slug: java
- name: multithreading
  slug: multithreading
seo_title: Comment résoudre le problème producteur-consommateur en Java en utilisant
  le multithreading
seo_desc: 'Concurrency is an important part of Java applications. Each application
  has multiple processes running at the same time. This helps utilize resources efficiently
  and improve performance.

  Multithreading is a method of achieving concurrency. It uses th...'
---

La concurrence est une partie importante des applications Java. Chaque application a plusieurs processus qui s'exécutent en même temps. Cela permet d'utiliser les ressources de manière efficace et d'améliorer les performances.

Le multithreading est une méthode pour atteindre la concurrence. Il utilise le concept de threads - des processus légers - pour exécuter plusieurs tâches en parallèle. Une application très populaire du multithreading est le problème producteur-consommateur.

Dans ce tutoriel, nous allons comprendre ce qu'est le problème producteur-consommateur et aborder brièvement les threads et le multithreading. Ensuite, nous allons comprendre comment résoudre le problème producteur-consommateur en Java en utilisant des threads.

Maintenant, je suppose que vous avez une connaissance de base de Java. Si ce n'est pas le cas, consultez les ressources suivantes.

* [Cours gratuits de Java pour débutants](https://www.freecodecamp.org/news/learn-java-free-java-courses-for-beginners/)

* [Bases de la programmation Java](https://www.freecodecamp.org/news/learn-the-basics-of-java-programming/)

## Table des matières

* [Qu'est-ce que le problème producteur-consommateur ?](#heading-quest-ce-que-le-probleme-producteur-consommateur)

* [Solution utilisant les threads producteur et consommateur et problème avec la synchronisation](#heading-solution-utilisant-les-threads-producteur-et-consommateur)

* [Introduction de la synchronisation dans la classe de file d'attente de messages](#heading-introduction-de-la-synchronisation-dans-la-classe-de-file-dattente-de-messages)

* [Producteur avec plusieurs consommateurs](#heading-producteur-avec-plusieurs-consommateurs)

* [Solution utilisant la classe BlockingQueue de la concurrence Java](#heading-solution-utilisant-la-classe-blockingqueue-de-la-concurrence-java)

## Qu'est-ce que le problème producteur-consommateur ?

Le problème producteur-consommateur est un problème de synchronisation entre différents processus. Il y a trois entités dans ce problème : un producteur, un consommateur et un tampon mémoire. Le producteur et le consommateur partagent le même tampon mémoire.

Le producteur produit des éléments et les pousse dans le tampon mémoire. Un consommateur consomme ensuite ces éléments en les retirant du tampon. Si le tampon est vide, le consommateur attend que le producteur pousse un élément, qu'il consomme après que le producteur l'ait poussé.

Le tampon mémoire est de taille fixe. S'il est plein, le producteur attend que le consommateur consomme un élément avant d'en pousser un nouveau. Le producteur et le consommateur ne peuvent pas accéder au tampon en même temps - c'est-à-dire qu'il est mutuellement exclusif. Chaque processus doit attendre que l'autre termine son travail sur le tampon avant de pouvoir y accéder.

Les systèmes d'exploitation rencontrent souvent ce problème où plusieurs processus accèdent au même espace mémoire pour effectuer leurs tâches.

Nous allons résoudre ce problème en utilisant le multithreading, donc je suppose que vous avez une idée de base de ce qu'est le multithreading et de son fonctionnement. Si ce n'est pas le cas, vous pouvez [lire ce tutoriel](https://www.freecodecamp.org/news/how-to-get-started-with-multithreading-in-java/).

Nous commencerons par une tentative de le résoudre simplement en utilisant des threads et une classe séparée pour la file d'attente de messages. Ensuite, nous comprendrons ses problèmes et comment les surmonter dans l'approche suivante. Nous verrons également d'autres approches du problème. Assurez-vous de rester jusqu'à la fin.

## Solution utilisant les threads producteur et consommateur

Passons d'abord en revue nos exigences.

* Les tâches du producteur et du consommateur s'exécutent dans des threads séparés

* Bus de données commun, généralement une file d'attente de messages, utilisé par le producteur et le consommateur.

* Si la file n'est pas pleine, le producteur pousse les données dans la file, ou attend qu'elles soient consommées

* Si la file n'est pas vide, le consommateur prend les données de la file, ou attend que le producteur publie.

Ce sont les choses que nous devons implémenter pour résoudre ce problème. Créons d'abord la file d'attente de messages.

### File d'attente de messages

Pour configurer une file d'attente de messages, nous utiliserons une classe qui contient la file et des méthodes pour publier et consommer des messages.

```java
class Data { 
	Queue<String> q; 
    int capacity; 
    
    Data(int cap) { 
    	q = new LinkedList<>(); 
        capacity=cap; 
    } 
    // autres méthodes 
}
```

Ici, nous avons utilisé la classe `Queue` de Java pour stocker nos messages. Chaque message est de type `String`. Mais dans les applications plus grandes, le message ou la charge utile pourrait être de n'importe quel type d'objet. Nous définissons également la capacité de la file d'attente de messages.

Ensuite, nous allons implémenter la méthode `publish()`. La méthode accepte un nouveau message à publier.

```java
public void publish(String msg) { // publier le message dans la file }
```

Tout d'abord, nous vérifions si la file est pleine. Nous ne pouvons pas publier un nouveau message si la file a atteint sa capacité.

```java
if(q.size() == capacity){ 
	return; 
}
```

Si la file n'est pas pleine, alors ajoutez le message à la file.

```java
q.add(msg);
```

Nous allons ajouter des instructions d'impression pour mieux comprendre le flux de travail.

```java
public void publish(String msg) { 
	String name=Thread.currentThread().getName(); 
    if(q.size() == capacity){ 
    	System.out.println("File pleine !"+name+" en attente de consommation de message..."); 
        return; 
    } 
    q.add(msg); 
    System.out.println("Message publié :: "+msg); 
    System.out.println("File : "+ q); 
    System.out.println(); 
}
```

Ici, nous imprimons simplement le thread qui est dans la méthode, le message publié et la file résultante.

Implémentons maintenant la méthode `consume()`. Cette méthode ne prend aucun argument et fonctionne de manière similaire à la méthode `publish()`. Nous vérifions d'abord si la file est vide avant de retirer quoi que ce soit de la file.

```java
if(q.size()==0){ 
	return; 
}
```

Ensuite, nous retirons le message.

```java
q.poll();
```

Encore une fois, nous allons ajouter des instructions d'impression pour mieux comprendre le flux de travail.

```java
public void consume()  { 
	String name=Thread.currentThread().getName(); 
	if(q.size()==0){ 
		System.out.println(name+" en attente de nouveau message..."); 
		return; 
	} 
    String msg = q.poll(); 
    System.out.println(name+" a consommé le message :: "+msg); 
    System.out.println("File : "+ q); 
    System.out.println(); 
}
```

### Thread Producteur

Écrivons maintenant la logique du producteur. Nous allons créer une classe `Producer` qui s'exécutera dans un thread. Il existe [plusieurs façons de créer des threads](https://www.javatpoint.com/how-to-create-a-thread-in-java) en Java. Nous allons utiliser l'interface `Runnable` pour créer notre thread, car c'est l'approche la plus préférée.

```java
class Producer implements Runnable{ 
	Data data; 
    public Producer(Data data) { 
    	this.data = data; 
	} 
    
    @Override public void run() { } 
}
```

Le producteur a accès à l'objet de bus de données qui lui est passé via le constructeur. La logique du producteur va à l'intérieur de la méthode `run()`. En remplaçant la méthode run, vous écrivez une fonctionnalité qui s'exécute dans un thread.

Maintenant, les moyens de production et de publication de données d'un producteur diffèrent dans chaque application. Pour ce post, nous allons simuler une fonctionnalité où le producteur continue de publier des messages toutes les quelques secondes.

Nous allons définir une liste de messages que le producteur peut utiliser.

```java
final String[] messages={"Salut !!", "Comment ça va !!", "Je t'aime !", "Quoi de neuf ?!!", "C'est vraiment drôle !!"};
```

Voici la logique du producteur à l'intérieur de la méthode `run()`:

```java
public void run() { 
	int i=0; 
    try { 
    	while(true){ 
        	Thread.sleep(1000); 
            data.publish(messages[i]); 
            i=(i+1)%messages.length; 
		} 
	} catch (InterruptedException e) {} 
}
```

Dans ce code, le producteur publie un message de la liste des messages toutes les 1000 ms. `Thread.sleep(_un_certain_délai_)` pause l'exécution du thread pendant une certaine période. Comme il lance une exception, nous entourons le code d'un bloc try-catch.

Ceci est juste à des fins de démonstration - ne vous inquiétez pas de la logique. Notre implémentation fonctionne indépendamment de la logique du producteur ou du consommateur.

### Thread Consommateur

Similaire au thread producteur, simulons la logique du consommateur.

```java
class Consumer implements Runnable{ 
	Data data; 
    public Consumer(Data data) { 
    	this.data = data; 
	} 
    @Override public void run() { 
    	try { 
        	while(true){ 
            	Thread.sleep(2000); 
                data.consume(); 
            } 
        } catch (InterruptedException e) {} 
    } 
}
```

Ici, le consommateur essaie de consommer un message toutes les 2000 ms.

### Mettre le tout ensemble

Maintenant, nous avons notre file d'attente de messages ainsi que les classes producteur et consommateur. Créons un thread producteur et un thread consommateur et démarrons-les.

Nous allons créer un objet `Data` avec une capacité de 5 messages et créer nos threads producteur et consommateur avec les objets des classes `Producer` et `Consumer`.

```java
public class Main { 
	public static void main(String[] args) { 
    	Data data = new Data(5); 
        Thread producer=new Thread(new Producer(data), "producer"); 
        Thread consumer=new Thread(new Consumer(data), "consumer");
        producer.start(); 
        consumer.start(); 
	} 
}
```

La méthode `run()` s'exécute dans un thread séparé lorsque `start()` est appelé.

### Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-23-211626-1.png align="left")

*Sortie incohérente*

Ici, la sortie est incohérente avec le flux de travail souhaité. Même après la publication du premier message, le consommateur attend toujours. Ensuite, un consommateur a consommé un message `Salut !!` qui n'existe pas. L'état de la file est également incohérent.

Vous obtiendrez probablement une sortie différente, puisque l'exécution des threads dépend du système d'exploitation central. Mais le problème persiste. Pourquoi cela se produit-il ?

### Problème de synchronisation avec la classe Data

Les threads producteur et consommateur s'exécutent simultanément, travaillant sur la même ressource. Ils accèdent à la file d'attente de messages exactement au même moment. Les deux threads peuvent commencer avec une version de la ressource et au moment où ils effectuent une opération, ils travaillent sur une version différente.

Cela conduit à une condition de [course](https://www.javatpoint.com/race-condition-in-operating-system). Les deux threads finissent par rivaliser pour la même ressource et donnent des résultats incohérents. Le thread producteur essaie d'ajouter un message à la file, tandis qu'au même moment un consommateur essaie de consommer un message. Il n'y a aucun moyen de contrôler quel message le consommateur pourrait obtenir.

Pour résoudre ce problème, nous avons besoin d'un mécanisme pour garantir qu'un seul thread peut opérer sur une ressource partagée à la fois. Dans ce cas, nous allons utiliser le concept de [synchronisation](https://www.geeksforgeeks.org/synchronization-in-java/).

À première vue, une fonction ou un bloc synchronisé ne peut être exécuté que par un seul thread à la fois. Un thread entrant dans un tel bloc acquiert un "verrou" sur l'objet et tout autre thread doit attendre jusqu'à ce que le thread libère ce verrou - c'est-à-dire jusqu'à ce qu'il termine son travail sur la ressource partagée.

Nous allons utiliser une méthode similaire pour résoudre notre problème.

## Introduction de la synchronisation dans la file d'attente de messages

Pour garantir que la file d'attente de messages n'est accessible que par un seul thread (producteur ou consommateur) à la fois, un thread doit sécuriser un verrou sur l'objet `Data` avant d'effectuer des opérations.

### Comment utiliser le mot-clé `synchronized`

Un objet peut être rendu mutuellement exclusif en utilisant le mot-clé synchronized. Nous allons utiliser le mot-clé `synchronized` avec les méthodes `publish()` et `consume()`.

```java
public synchronized void publish(String msg)
```

```java
public synchronized void consume()
```

Maintenant, un thread doit acquérir un verrou sur l'objet avant d'entrer dans ces méthodes.

### Que sont les méthodes `wait()` et `notify()` ?

Nous avons atteint la synchronisation - un seul thread peut accéder à une ressource partagée à la fois pour garantir la cohérence. Maintenant, nous devons établir une communication entre les threads producteur et consommateur.

Comprenons d'abord ce dont nous avons besoin. Si la file est pleine, le producteur doit attendre qu'un consommateur consomme un élément. De même, si la file est vide, le consommateur doit attendre que le producteur pousse un élément.

De plus, lorsqu'un producteur pousse un élément, il doit notifier tous les threads consommateurs en attente de l'action. Cela est également vrai lorsque le consommateur consomme un élément. Alors, comment établir cette communication ?

Nous pouvons le faire en utilisant les méthodes `wait()` et `notify()`. Lorsque la méthode `wait()` est appelée, le thread libère le verrou sur l'objet et entre dans un état d'attente jusqu'à ce qu'un autre thread appelle la méthode `notify()` ou `notifyAll()`.

`notify()` réveille un thread qui est dans l'état d'attente, tandis que `notifyAll()` réveille tous les threads en attente. Lorsqu'un thread se réveille à nouveau, il doit réacquérir le verrou sur l'objet. Si un autre thread a le verrou, alors ce thread doit attendre jusqu'à ce que l'autre thread libère le verrou.

Vous pouvez en apprendre davantage sur les méthodes `wait()` et `notify()` [ici](https://www.baeldung.com/java-wait-notify).

### Comment communiquer entre les threads en utilisant wait() et notify()

Utilisons les méthodes ci-dessus. Un producteur doit attendre avant de pousser un élément si la file est pleine. Donc, invoquez la méthode `wait()` si la file est à capacité. De même, le consommateur doit attendre si la file est vide.

Pour réveiller les threads de l'état d'attente, appelez `notifyAll()` après que le producteur publie un message et que le consommateur consomme un message. Cela notifiera tous les threads en attente.

Voici la méthode `publish()` mise à jour :

```java
public synchronized void publish(String msg) throws InterruptedException { 
	String name=Thread.currentThread().getName(); 
    if(q.size() == capacity){ 
    	System.out.println("File pleine !"+name+" en attente de consommation de message..."); 
        wait(); 
	} 
    q.add(msg); 
    System.out.println("Message publié :: "+msg); 
    System.out.println("File : "+ q); 
    System.out.println(); 
    notifyAll(); 
}
```

Et voici la méthode `consume()` mise à jour :

```java
public synchronized void consume() throws InterruptedException { 
	String name=Thread.currentThread().getName(); 
    if(q.size()==0){ 
    	System.out.println(name+" en attente de nouveau message..."); 
        wait(); 
 	} 
    String msg = q.poll(); 
    System.out.println(name+" a consommé le message :: "+msg);
    System.out.println("File : "+ q); 
    System.out.println(); 
    notifyAll(); 
}
```

`wait()` et `notify()` peuvent lancer `InterruptedException`, donc nous ajoutons une déclaration `throws` aux méthodes.

### Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-132435-1.png align="left")

*Sortie avec synchronisation*

Cette fois, la sortie est plus cohérente et nous obtenons le comportement attendu. Le producteur continue de publier des messages et le consommateur consomme ces messages.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-134924-1.png align="left")

*Producteur en attente*

Ici, la file est pleine et le producteur attend que le consommateur consomme un message. Ce n'est qu'après cela que le producteur publie un nouveau message.

## Producteur avec plusieurs consommateurs

Jusqu'à présent, nous avons abordé le problème avec un producteur et un consommateur. Dans une application réelle, il pourrait y avoir plusieurs producteurs et consommateurs, tous s'exécutant dans des threads séparés.

Ajoutons plus de threads consommateurs pour voir comment nous pourrions gérer ce scénario :

```python
for(int i=1;i<=5;i++){ 
	new Thread(new Consumer(data), "Consumer "+i).start();
}
```

Ici, nous avons créé 5 threads consommateurs, nous les avons étiquetés et nous les avons démarrés un par un. Mais cela ne suffit pas. Il y a un problème avec l'approche existante.

Réduisons le temps d'attente du consommateur et exécutons le code :

```java
Thread.sleep(500);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-203117.png align="left")

*Problème avec plusieurs consommateurs*

Ici, après que le consommateur 5 a consommé un message, les autres consommateurs peuvent consommer même si la file est vide.

Le problème réside dans la condition suivante :

```java
if(q.size()==0){
	wait();
}
```

Comprenons d'abord le flux de travail. Considérons le consommateur 5 (C5) et le consommateur 1 (C1). C5 sécurise le verrou sur la méthode et y entre. La file est initialement vide, donc il libère le verrou et attend le producteur. En même temps, C1 sécurise le verrou et entre dans la méthode. Il attend également le producteur.

Donc, C5 et C1 attendent. Le producteur publie un message. C5 et C1 sont notifiés et se réveillent. C5 réacquiert le verrou et procède à la consommation du message, tandis que C1 attend que C5 libère le verrou. Ici, C1 n'attend pas à cause de `wait()` - il s'est réveillé et maintenant il attend à la ligne suivante.

Après que C5 a consommé le message et libéré le verrou, C1 continue et essaie de consommer le message. Mais la file est vide maintenant, donc il reçoit null ou lance une exception. Cela arrive également avec les autres threads.

Pour éviter cela, nous devons vérifier si la file est vide une fois de plus. Donc, au lieu d'utiliser une condition `if`, nous utilisons une boucle `while` comme ceci :

```python
while(q.size()==0){
            wait();
        }
```

Cela vérifie si la file est vide chaque fois qu'un thread se réveille. Donc, si plusieurs threads se réveillent en même temps, il doit vérifier si un autre thread a vidé la file.

Nous faisons de même pour vérifier si la file est pleine.

```java
while(q.size() == capacity){
            wait();
        }
```

Cette fois, le code s'exécute sans aucun problème.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-26-204943.png align="left")

*Sortie correcte avec plusieurs consommateurs*

Voici le code complet pour la classe `Data` :

```java
class Data {
    Queue<String> q;
    int capacity;
    Data(int cap) {
        q = new LinkedList<>();
        capacity=cap;
    }

    public synchronized void publish(String msg) throws InterruptedException {
        String name=Thread.currentThread().getName();
        while(q.size() == capacity){
            System.out.println("File pleine !"+name+" en attente de consommation de message...");
            wait();
        }
        q.add(msg);
        System.out.println("Message publié :: "+msg);
        System.out.println("File : "+ q);
        System.out.println();
        notifyAll(); 
    }

    public synchronized void consume() throws InterruptedException {
        String name=Thread.currentThread().getName();
        while(q.size()==0){
            System.out.println(name+" en attente de nouveau message...");
            wait();
        }
        String msg = q.poll();
        System.out.println(name+" a consommé le message :: "+msg);
        System.out.println("File : "+ q);
        System.out.println();
        notifyAll();
    }
}
```

Vous pouvez créer n'importe quel nombre de producteurs et de consommateurs et tester ce code dans plusieurs scénarios.

## Solution utilisant la classe BlockingQueue de la concurrence Java

Jusqu'à présent, vous avez appris ce qu'est le problème producteur-consommateur et comment il peut être résolu. Mais, en travaillant sur des applications en temps réel, nous ne mettrons probablement pas en œuvre la synchronisation manuellement.

Au lieu de cela, nous pouvons utiliser la classe `BlockingQueue` du package `java.util.concurrent`. La différence entre `Queue` et `BlockingQueue` est qu'elle attend que la file devienne non vide avant qu'un message puisse être consommé. De même, elle attend que la file ait de l'espace avant de publier un nouveau message.

Nous pouvons initialiser la file bloquante de la manière suivante :

```java
BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
```

Cela crée une file bloquante de capacité 10. Pour publier un élément, nous utilisons la méthode `put()`, et pour retirer un élément, nous utilisons la méthode `take()`.

Utilisons d'abord cela dans notre classe Producer :

```java
class Producer implements Runnable{
    BlockingQueue<String> q;
    final String[] messages={"Salut !!", "Comment ça va !!", "Je t'aime !", "Quoi de neuf ?!!", "C'est vraiment drôle !!"};
    public Producer(BlockingQueue<String> q) {
        this.q = q;
    }

    @Override
    public void run() {
        int i=0;
        try {
            while(true){
                Thread.sleep(500);
                
                q.put(messages[i]);
                
                System.out.println("Message publié :: "+messages[i]);
                i=(i+1)%messages.length;
            }
        } catch (InterruptedException e) {}
    }
    
}
```

Ici, nous n'utilisons pas une classe `Data` séparée avec des méthodes synchronisées, puisque les méthodes `put()` et `take()` de `BlockingQueue` sont synchronisées. Ici, si la file est pleine, la méthode `put()` attend qu'un consommateur consomme un message.

De même, mettons à jour notre classe Consumer :

```java
class Consumer implements Runnable{
    BlockingQueue<String> q;

    public Consumer(BlockingQueue<String> q) {
        this.q = q;
    }

    @Override
    public void run() {
        try {
            while(true){
                Thread.sleep(1500);
                
                String msg=q.take();

                String name=Thread.currentThread().getName();
                System.out.println(name+" a consommé le message :: "+msg);
            }
        } catch (InterruptedException e) {}
    }    
}
```

Ici, si la file est vide, la méthode `take()` attend que le producteur publie un message.

Créons notre objet `BlockingQueue` et démarrons ces threads :

```java
public class Main {
    public static void main(String[] args) {
        BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
        Thread producer = new Thread(new Producer(q));
        producer.start();
        for(int i=1;i<=5;i++){
            new Thread(new Consumer(q), "Consumer "+i).start();
        }
    }
    
}
```

Ici, nous avons un thread producteur et 5 threads consommateurs. Regardons la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-28-115531.png align="left")

*Sortie pour l'implémentation de BlockingQueue*

Dans la sortie, vous pouvez voir qu'après que les consommateurs 1, 3 et 2 ont consommé un message, les autres consommateurs attendent qu'un message soit publié avant de le consommer.

Il pourrait y avoir quelques incohérences lors de l'impression de ces messages puisque le thread ne s'arrête qu'aux méthodes `put()` ou `take()` et non aux instructions `println()`. Mais le code s'exécute correctement. Encore une fois, la sortie sera différente à chaque fois que vous exécuterez le code.

Donc, en travaillant sur de grands projets, vous pouvez utiliser la classe `BlockingQueue`. Mais il est important de comprendre comment gérer le problème producteur-consommateur à partir de zéro. Cela est vraiment utile, surtout lors des entretiens, puisque vous ne serez généralement pas autorisé à utiliser la classe `BlockingQueue`.

## Conclusion

Dans ce tutoriel, vous avez appris un problème important en matière de concurrence, le problème producteur-consommateur. Et vous avez appris comment vous pouvez le résoudre en utilisant le multithreading en Java.

Au total, nous avons implémenté quatre approches différentes :

Tout d'abord, j'ai commencé par une implémentation très basique et directe. L'exécution du producteur et du consommateur dans des threads séparés a permis d'atteindre la concurrence. Mais comme ils utilisaient la même file d'attente de messages, il y avait un problème de synchronisation.

Par conséquent, dans l'approche suivante, nous avons ajouté la synchronisation pour corriger le problème. Ensuite, nous avons ajouté plus de consommateurs qui attendraient tous le producteur. Là, nous avons appris pourquoi il est important de vérifier les conditions de pleine et vide chaque fois qu'un thread se réveille.

Après avoir parcouru toute l'implémentation à partir de zéro, nous avons vu une manière simple de résoudre le problème producteur-consommateur en Java en utilisant BlockingQueue. En comprenant différentes approches et leurs problèmes, vous pouvez vous faire une meilleure idée de la manière d'aborder un problème. J'espère que ce guide vous aidera dans vos futures entreprises.

Si vous ne comprenez pas le contenu ou trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !