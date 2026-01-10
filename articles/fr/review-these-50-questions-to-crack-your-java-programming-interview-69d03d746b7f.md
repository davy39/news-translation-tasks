---
title: Passez en revue ces 50 questions pour réussir votre entretien de programmation
  Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T16:41:53.000Z'
originalURL: https://freecodecamp.org/news/review-these-50-questions-to-crack-your-java-programming-interview-69d03d746b7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s73cLB7vYz05f-aw_QAgFw.png
tags:
- name: coding
  slug: coding
- name: interview questions
  slug: interview-questions
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Passez en revue ces 50 questions pour réussir votre entretien de programmation
  Java
seo_desc: 'By javinpaul

  A list of frequently asked Java questions from programming job interviews.


  Hello, everybody! Over the past few years, I have been sharing a lot of Java Interview
  questions and discussion individually. Many of my readers have requested t...'
---

Par javinpaul

#### Une liste de questions Java fréquemment posées lors des entretiens d'embauche en programmation.

![Image](https://cdn-media-1.freecodecamp.org/images/cA9-wkkWif9KjVOo09g1D5s5OiE8KskLLfa-)

Bonjour à tous ! Au cours des dernières années, j'ai partagé beaucoup de [questions d'entretien Java](http://javarevisited.blogspot.sg/2015/10/133-java-interview-questions-answers-from-last-5-years.html) et de discussions individuellement. Beaucoup de mes lecteurs m'ont demandé de les rassembler afin qu'ils puissent les avoir au même endroit. Cet article est le résultat de cela.

Cet article contient plus de **50 questions d'entretien Java** couvrant tous les sujets importants comme les fondamentaux de Java Core, le [Framework de Collection Java](https://javarevisited.blogspot.com/2011/11/collection-interview-questions-answers.html), la [Programmation Multithread et la Concurrence en Java](https://javarevisited.blogspot.com/2014/07/top-50-java-multithreading-interview-questions-answers.html#axzz5ghebTpxm), les [Java IO](https://javarevisited.blogspot.com/2014/08/socket-programming-networking-interview-questions-answers-Java.html), [JDBC](https://javarevisited.blogspot.com/2012/12/top-10-jdbc-interview-questions-answers.html), les [Internes de la JVM](http://www.java67.com/2016/08/10-jvm-options-for-java-production-application.html), les [Problèmes de Codage](http://www.java67.com/2018/06/data-structure-and-algorithm-interview-questions-programmers.html), la [Programmation Orientée Objet](http://www.java67.com/2015/12/top-30-oops-concept-interview-questions-answers-java.html), etc.

Les questions sont également tirées de divers entretiens et ne sont, en aucun cas, très difficiles. Vous avez peut-être déjà vu certaines d'entre elles lors de vos entretiens téléphoniques ou en face à face.

Les questions sont également très utiles pour réviser des sujets importants comme le multithreading et les collections. J'ai également partagé quelques _ressources utiles pour un apprentissage et une amélioration supplémentaires_ comme [**The Complete Java MasterClass**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) pour vous rafraîchir la mémoire et combler les lacunes dans vos compétences Java.

Alors, qu'attendons-nous ? Voici la liste de certaines des questions Java les plus fréquemment posées lors des entretiens pour les développeurs Java débutants et expérimentés.

### 50+ Questions d'Entretien Java pour les Programmeurs Ayant 2 à 3 Ans d'Expérience

Alors, sans perdre plus de votre temps, voici ma liste de certaines des [Questions d'Entretien Java Core](http://www.java67.com/2018/03/top-50-core-java-interview-questions.html) les plus fréquemment posées pour les programmeurs débutants. Cette liste se concentre sur les débutants et les développeurs moins expérimentés, comme quelqu'un ayant 2 à 3 ans d'expérience en Java.

1) **Comment Java atteint-il l'indépendance de plateforme ?** ([réponse](http://www.java67.com/2012/08/how-java-achieves-platform-independence.html))  
indice : bytecode et Java Virtual Machine

2) **Qu'est-ce que `ClassLoader` en Java ?** ([réponse](http://javarevisited.blogspot.sg/2012/12/how-classloader-works-in-java.html#axzz59AWpr6cb))  
indice : fait partie de la JVM qui charge les bytecodes pour les classes. Vous pouvez écrire le vôtre.

3) **Écrivez un programme Java pour vérifier si un nombre est pair ou impair ?** ([réponse](http://javarevisited.blogspot.sg/2013/04/how-to-check-if-number-is-even-or-odd.html#axzz59AWpr6cb))  
indice : vous pouvez utiliser l'opérateur bitwise, comme le bitwise AND, rappelez-vous, le nombre pair a zéro à la fin en format binaire et un nombre impair a 1 à la fin.

4) **Différence entre `ArrayList` et `HashSet` en Java ?** ([réponse](http://www.java67.com/2012/07/difference-between-arraylist-hashset-in-java.html))  
indice : toutes les différences entre `List` et `Set` sont applicables ici, par exemple, l'ordre, les doublons, la recherche aléatoire, etc. Voir [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) par Richard Warburton pour en savoir plus sur ArrayList, HashSet et autres Collections importantes en Java.

![Image](https://cdn-media-1.freecodecamp.org/images/ueOwMAd5GBdw4blCOpEBpOdMOtcs-et6nPYA)

5) **Qu'est-ce que le double checked locking dans Singleton ?** ([réponse](http://www.java67.com/2016/04/why-double-checked-locking-was-broken-before-java5.html))  
indice : vérification en deux temps si l'instance est initialisée ou non, d'abord sans verrouillage et ensuite avec verrouillage.

**6) Comment créez-vous un Singleton thread-safe en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/12/how-to-create-thread-safe-singleton-in-java-example.html))**  
indice : plusieurs façons, comme utiliser Enum ou en utilisant le motif double-checked locking ou en utilisant une classe statique imbriquée.

**7) Quand utiliser la variable volatile en Java ? ([réponse](http://www.java67.com/2012/08/what-is-volatile-variable-in-java-when.html))**  
indice : lorsque vous devez instruire la JVM qu'une variable peut être modifiée par plusieurs threads et donner un indice à la JVM pour ne pas mettre en cache sa valeur.

**8) Quand utiliser une variable transient en Java ? ([réponse](http://www.java67.com/2012/08/what-is-transient-variable-in-java.html))**  
indice : lorsque vous voulez rendre une variable non-sérialisable dans une classe, qui implémente l'interface Serializable. En d'autres termes, vous pouvez l'utiliser pour une variable dont la valeur vous ne voulez pas sauvegarder. Voir [**The Complete Java MasterClass**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) pour en savoir plus sur les variables transient en Java.

**9) Différence entre les variables transient et volatile en Java ? ([réponse](http://www.java67.com/2012/11/difference-between-transient-vs-volatile-modifier-variable-java.html))**  
indice : totalement différentes, l'une est utilisée dans le contexte de la sérialisation tandis que l'autre est utilisée dans la concurrence.

**10) Différence entre Serializable et Externalizable en Java ? ([réponse](http://www.java67.com/2012/10/difference-between-serializable-vs-externalizable-interface.html))**  
indice : Externalizable vous donne plus de contrôle sur le processus de sérialisation.

**11) Peut-on override une méthode private en Java ? ([réponse](http://www.java67.com/2013/08/can-we-override-private-method-in-java-inner-class.html))**  
indice : Non, car elle n'est pas visible dans la sous-classe, une exigence primaire pour override une méthode en Java.

**12) Différence entre `Hashtable` et `HashMap` en Java ? ([réponse](http://javarevisited.blogspot.sg/2010/10/difference-between-hashmap-and.html#axzz53B6SD769))**  
indice : plusieurs mais la plus importante est que `Hashtable` est synchronisé, tandis que `HashMap` ne l'est pas. C'est aussi une classe héritée et lente par rapport à `HashMap`.

**13) Différence entre `List` et `Set` en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/04/difference-between-list-and-set-in-java.html#axzz53n9YK0Mb))**  
indice : `List` est ordonnée et permet les doublons. `Set` est non ordonnée et n'autorise pas les éléments en double.

**14) Différence entre `ArrayList` et `Vector` en Java ([réponse](http://www.java67.com/2012/09/arraylist-vs-vector-in-java-interview.html))**  
indice : Beaucoup, mais la plus importante est que `ArrayList` est non synchronisé et rapide tandis que `Vector` est synchronisé et lent. C'est aussi une classe héritée comme `Hashtable`.

**15) Différence entre `Hashtable` et `ConcurrentHashMap` en Java ? ([réponse](http://javarevisited.blogspot.sg/2011/04/difference-between-concurrenthashmap.html#axzz4qw7RoNvw))**  
indice : plus scalable. Voir [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) par Richard Warburton pour en savoir plus.

**16) Comment `ConcurrentHashMap` atteint-il la scalabilité ? ([réponse](http://javarevisited.blogspot.sg/2017/08/top-10-java-concurrenthashmap-interview.html#axzz50U9xyqbo))**  
indice : en divisant la map en segments et en verrouillant uniquement pendant l'opération d'écriture.

**17) Quelles sont les deux méthodes à override pour qu'un `Object` soit utilisé comme `Key` dans `HashMap` ? ([réponse](http://www.java67.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html))**  
indice : equals et hashcode

**18) Différence entre wait et sleep en Java ? ([réponse](http://www.java67.com/2012/08/what-are-difference-between-wait-and.html))**  
indice : La méthode `wait()` libère le verrou ou le moniteur, tandis que sleep ne le fait pas.

**19) Différence entre `notify` et `notifyAll` en Java ? ([réponse](http://www.java67.com/2013/03/difference-between-wait-vs-notify-vs-notifyAll-java-thread.html))**  
indice : `notify` notifie un thread aléatoire en attente de ce verrou tandis que `notifyAll` informe tous les threads en attente d'un moniteur. Si vous êtes certain qu'un seul thread est en attente, utilisez `notify`, sinon `notifyAll` est meilleur. Voir [**Threading Essentials Mini-Course**](https://javaspecialists.teachable.com/p/threading-essentials/?product_id=539197&coupon_code=SLACK100?affcode=92815_johrd7r8) par Java Champion Heinz Kabutz pour en savoir plus sur les bases du threading.

**20) Pourquoi override hashcode avec `equals()` en Java ? ([réponse](http://javarevisited.blogspot.sg/2015/01/why-override-equals-hashcode-or-tostring-java.html#axzz55oDxm8vv))**  
indice : pour être conforme au contrat equals et hashcode, ce qui est requis si vous prévoyez de stocker votre objet dans des classes de collection, par exemple `HashMap` ou `ArrayList`.

**21) Que signifie le facteur de charge de `HashMap` ? ([réponse](http://www.java67.com/2017/08/top-10-java-hashmap-interview-questions.html))**  
indice : Le seuil qui déclenche le redimensionnement de `HashMap` est généralement de 0,75, ce qui signifie que `HashMap` se redimensionne s'il est rempli à 75 pour cent.

**22) Différence entre `ArrayList` et `LinkedList` en Java ? ([réponse](http://www.java67.com/2012/12/difference-between-arraylist-vs-LinkedList-java.html))**  
indice : même chose qu'un tableau et une liste chaînée, l'un permet la recherche aléatoire tandis que l'autre ne le permet pas. L'insertion et la suppression sont faciles sur la liste chaînée mais la recherche est facile sur un tableau. Voir [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections)**,** le cours de Richard Warburton sur Pluralsight, pour en savoir plus sur les structures de données Collection essentielles en Java.

**23) Différence entre `CountDownLatch` et `CyclicBarrier` en Java ? ([réponse](http://www.java67.com/2012/08/difference-between-countdownlatch-and-cyclicbarrier-java.html))**  
indice : Vous pouvez réutiliser `CyclicBarrier` après que la barrière soit brisée mais vous ne pouvez pas réutiliser `CountDownLatch` après que le compte atteigne zéro.

**24) Quand utiliser `Runnable` vs `Thread` en Java ? ([réponse](http://www.java67.com/2016/01/7-differences-between-extends-thread-vs-implements-Runnable-java.html))**  
indice : toujours

**25) Que signifie Enum étant type-safe en Java ? ([réponse](http://www.java67.com/2014/04/what-java-developer-should-know-about-Enumeration-type-in-Java.html))**  
indice : Cela signifie que vous ne pouvez pas assigner une instance d'un type Enum différent à une variable Enum. Par exemple, si vous avez une variable comme `DayOfWeek` day, vous ne pouvez pas lui assigner une valeur de l'énumération `DayOfMonth`.

**26) Comment fonctionne l'Autoboxing de Integer en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/07/auto-boxing-and-unboxing-in-java-be.html#axzz59AWpr6cb))**  
indice : En utilisant la méthode `valueOf()` en Java.

**27) Différence entre `PATH` et `Classpath` en Java ? ([réponse](http://www.java67.com/2012/08/what-is-path-and-classpath-in-java-difference.html))**  
indice : `PATH` est utilisé par le système d'exploitation tandis que `Classpath` est utilisé par la JVM pour localiser les binaires Java, par exemple les fichiers JAR ou les fichiers Class. Voir [Java Fundamentals: The Core Platform](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-core-platform) pour en savoir plus sur `PATH`, `Classpath`, et autres variables d'environnement Java.

![Image](https://cdn-media-1.freecodecamp.org/images/io-lPE67oMG1oBh204LvPm61t7kAcLFvp-B6)

**28) Différence entre la surcharge de méthode et le override en Java ? ([réponse](http://www.java67.com/2015/08/top-10-method-overloading-overriding-interview-questions-answers-java.html))**  
indice : Le override se produit dans la sous-classe tandis que la surcharge se produit dans la même classe. De plus, le override est une activité d'exécution tandis que la surcharge est résolue à la compilation.

**29) Comment empêcher une classe d'être sous-classée en Java ? ([réponse](http://www.java67.com/2017/06/10-points-about-final-modifier-in-java.html))**  
indice : rendez simplement son constructeur privé

**30) Comment restreindre l'utilisation de votre classe par votre client ? ([réponse](http://javarevisited.blogspot.sg/2016/01/why-jpa-entity-or-hibernate-persistence-should-not-be-final-in-java.html))**  
indice : rendez le constructeur privé ou lancez une exception depuis le constructeur

**31) Différence entre `StringBuilder` et `StringBuffer` en Java ? ([réponse](http://www.java67.com/2016/10/5-difference-between-stringbuffer.html))**  
indice : `StringBuilder` n'est pas synchronisé tandis que `StringBuffer` est synchronisé.

**32) Différence entre le Polymorphisme et l'Héritage en Java ? ([réponse](http://www.java67.com/2014/04/difference-between-polymorphism-and-Inheritance-java-oops.html))**  
indice : L'héritage permet la réutilisation du code et construit la relation entre les classes, ce qui est requis par le polymorphisme, qui fournit un comportement dynamique. Voir [**Java Fundamentals: Object-Oriented Design**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-object-oriented-design) pour en savoir plus sur les fonctionnalités OOP.

**33) Peut-on override une méthode statique en Java ? ([réponse](http://www.java67.com/2012/08/can-we-override-static-method-in-java.html))**  
indice : Non, car le override se résout à l'exécution tandis que l'appel de méthode statique est résolu à la compilation.

**34) Peut-on accéder à une méthode privée en Java ? ([réponse](http://www.java67.com/2012/08/can-we-override-private-method-in-java.html))**  
indice : oui, dans la même classe mais pas en dehors de la classe

**35) Différence entre une interface et une classe abstraite en Java ? ([réponse](http://www.java67.com/2017/08/difference-between-abstract-class-and-interface-in-java8.html))**  
indice : à partir de [Java 8](https://dzone.com/articles/5-courses-to-crack-java-certification-ocajp-1z0-80), la différence est floue. Cependant, une classe Java peut toujours implémenter plusieurs interfaces mais ne peut étendre qu'une seule classe.

**36) Différence entre les parseurs DOM et SAX en Java ? ([réponse](http://www.java67.com/2012/09/dom-vs-sax-parser-in-java-xml-parsing.html))**  
indice : DOM charge tout le fichier XML en mémoire tandis que SAX ne le fait pas. C'est un parseur basé sur les événements et peut être utilisé pour analyser un grand fichier, mais DOM est rapide et doit être préféré pour les petits fichiers.

**37) Différence entre les mots-clés throw et throws en Java ? ([réponse](http://www.java67.com/2012/10/difference-between-throw-vs-throws-in.html))**  
indice : throws déclare quelle exception une méthode peut lancer en cas d'erreur mais le mot-clé throw lance réellement une exception. Voir [**Java Fundamentals: Exception Handling**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-exception-handling) pour en savoir plus sur la gestion des exceptions en Java.

![Image](https://cdn-media-1.freecodecamp.org/images/QSqKD-b97Dr36kViV1eTdvqNVNgdZRp52D7n)

**38) Différence entre les itérateurs fail-safe et fail-fast en Java ? ([réponse](http://www.java67.com/2015/06/what-is-fail-safe-and-fail-fast-iterator-in-java.html))**  
indice : fail-safe ne lance pas `ConcurrentModificationException` tandis que `fail-fast` le fait chaque fois qu'ils détectent un changement externe sur la collection sous-jacente pendant l'itération.

**39) Différence entre Iterator et Enumeration en Java ? ([réponse](http://javarevisited.blogspot.sg/2010/10/what-is-difference-between-enumeration.html#axzz59AWpr6cb))**  
indice : Iterator vous donne également la possibilité de supprimer un élément pendant l'itération tandis qu'Enumeration ne le permet pas.

**40) Qu'est-ce que `IdentityHashMap` en Java ? ([réponse](http://www.java67.com/2016/09/difference-between-identityhashmap-weakhashmap-enummap-in-java.html))**  
indice : Une `Map`, qui utilise l'opérateur d'égalité `==` pour vérifier l'égalité au lieu de la méthode `equals()`.

**41) Qu'est-ce que le pool de `String` en Java ? ([réponse](http://javarevisited.blogspot.sg/2016/07/difference-in-string-pool-between-java6-java7.html#axzz4pGGwsyna))**  
indice : Un pool de littéraux `String`. Rappelez-vous qu'il a été déplacé du heap depuis l'espace perm gen dans JDK 7.

**42) Une classe `Serializable` peut-elle contenir un champ non-sérialisable en Java ? ([réponse](http://javarevisited.blogspot.sg/2016/09/how-to-serialize-object-in-java-serialization-example.html))**  
indice : Oui, mais vous devez le rendre soit statique soit transient.

**43) Différence entre this et super en Java ? ([réponse](http://www.java67.com/2013/06/difference-between-this-and-super-keyword-java.html))**  
indice : this fait référence à l'instance actuelle tandis que super fait référence à une instance de la superclasse.

**44) Différence entre `Comparator` et `Comparable` en Java ? ([réponse](http://www.java67.com/2013/08/difference-between-comparator-and-comparable-in-java-interface-sorting.html))**  
indice : `Comparator` définit un ordre personnalisé tandis que `Comparable` définit l'ordre naturel des objets, par exemple l'ordre alphabétique pour `String`. Voir [The Complete Java MasterClass](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) pour en savoir plus sur le tri en Java.

![Image](https://cdn-media-1.freecodecamp.org/images/DOCGFtdTMhjj3faRAiQ69ZSTxf2pffyroFfv)

**45) Différence entre `java.util.Date` et `java.sql.Date` en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/04/difference-between-javautildate-and.html))**  
indice : le premier contient à la fois la date et l'heure tandis que le second contient uniquement la partie date.

**46) Pourquoi les méthodes wait et notify sont-elles déclarées dans la classe `Object` en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/02/why-wait-notify-and-notifyall-is.html))**  
indice : car elles nécessitent un verrou qui n'est disponible que pour un objet.

**47) Pourquoi Java ne supporte-t-il pas l'héritage multiple ? ([réponse](http://javarevisited.blogspot.sg/2011/07/why-multiple-inheritances-are-not.html))**  
indice : Il ne le supporte pas à cause d'une mauvaise expérience avec C++, mais avec Java 8, il le fait dans une certaine mesure — seul l'héritage multiple de `Type` n'est pas supporté en Java maintenant.

**48) Différence entre les exceptions checked et unchecked en Java ? ([réponse](http://javarevisited.blogspot.sg/2011/12/checked-vs-unchecked-exception-in-java.html))**  
indice : Dans le cas des checked, vous devez gérer l'exception en utilisant un bloc catch, tandis que dans le cas des unchecked, c'est à vous de décider ; le compilateur ne vous dérangeras pas.

**49) Différence entre Error et Exception en Java ? ([réponse](http://www.java67.com/2012/12/difference-between-error-vs-exception.html))**  
indice : Je suis fatigué de taper, veuillez vérifier la réponse

**50) Différence entre Race condition et Deadlock en Java ? ([réponse](http://javarevisited.blogspot.sg/2012/02/what-is-race-condition-in.html#axzz59AbkWuk9))**  
indice : les deux sont des erreurs qui se produisent dans une application concurrente, l'une se produit à cause de l'ordonnancement des threads tandis que l'autre se produit à cause d'un mauvais codage. Voir [Multithreading and Parallel Computing in Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fmultithreading-and-parallel-computing-in-java%2F) pour en savoir plus sur les deadlocks, les Race Conditions et autres problèmes de multithreading.

### Remarques de Clôture

Merci, vous avez atteint la fin de l'article … Bonne chance avec votre entretien de programmation ! Cela ne sera certainement pas facile, mais en suivant cette feuille de route et ce guide, vous êtes un pas de plus vers devenir un [ingénieur DevOps](https://hackernoon.com/10-free-courses-to-learn-docker-for-programmers-and-devops-engineers-7ff2781fd6e0).

Si vous aimez cet article, alors veuillez le partager avec vos amis et collègues, et n'oubliez pas de suivre [javinpaul](https://twitter.com/javinpaul) sur Twitter !

#### Ressources Supplémentaires

* [Guide d'Entretien Java : 200+ Questions et Réponses d'Entretien](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-interview-questions-and-answers%2F)
* [Guide d'Entretien sur le Framework Spring — 200+ Questions & Réponses](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fspring-interview-questions-and-answers%2F)
* [Préparation à un Entretien d'Embauche par John Sonmez](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fdeveloper-job-interviews)
* [Java Programming Interview Exposed par Markham](http://www.amazon.com/Java-Programming-Interviews-Exposed-Markham/dp/1118722868?tag=javamysqlanta-20)
* [Cracking the Coding Interview — 189 Questions et Réponses](http://www.amazon.com/Cracking-Coding-Interview-6th-Edition/dp/0984782850/?tag=javamysqlanta-20)
* [Analyse des Structures de Données et des Algorithmes pour les Entretiens d'Embauche](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structure-and-algorithms-analysis%2F)
* [130+ Questions d'Entretien Java des 5 Dernières Années](http://javarevisited.blogspot.sg/2015/10/133-java-interview-questions-answers-from-last-5-years.html)

> **P.S. —** Si vous avez besoin de ressources GRATUITES pour apprendre Java, vous pouvez consulter cette liste de **cours Java gratuits** pour commencer votre préparation.  
>   
> **P. S. S. —** Je n'ai pas fourni la réponse à la question d'entretien partagée dans l'image « Combien d'objets String sont créés dans le code ? » pouvez-vous deviner et expliquer ?