---
title: Asynchronous-IO vs Traitement Asynchrone des Requêtes en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T17:24:24.000Z'
originalURL: https://freecodecamp.org/news/java-async-io-async-request-processing-in-http-request-1a04f395d8c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5htxZQ3yUYwLMuoHND11ug.png
tags:
- name: asynchronous
  slug: asynchronous
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: Sockets
  slug: sockets
- name: 'tech '
  slug: tech
seo_title: Asynchronous-IO vs Traitement Asynchrone des Requêtes en Java
seo_desc: 'By Bhuvan Gupta

  In this article, I am trying to explain the difference between Async-IO and Async-Request
  processing in the HTTP request in the Java world.

  In the pre-Java 1.4 world, Java provides an API to send/receive data over the network
  socket. ...'
---

Par Bhuvan Gupta

Dans cet article, je tente d'expliquer la différence entre Async-IO et le traitement asynchrone des requêtes dans le monde Java.

Dans le monde pré-Java **_1.4_**, Java fournit une API pour envoyer/recevoir des données via une socket réseau. Les auteurs originaux de la JVM ont mappé ce comportement d'API à l'API de socket du système d'exploitation, presque un à un.

Alors, quel est le comportement des sockets du système d'exploitation ? Le système d'exploitation fournit une [API de programmation de socket](https://www.csd.uoc.gr/~hy556/material/tutorials/cs556-3rd-tutorial.pdf), qui possède des appels send/recv **bloquants**. Puisque Java est simplement un processus s'exécutant sur Linux (système d'exploitation), ce programme Java doit donc utiliser cette API bloquante fournie par le système d'exploitation.

Le monde était heureux et les développeurs Java ont commencé à utiliser l'API pour envoyer/recevoir des données. Mais ils devaient garder un thread Java pour chaque socket (client).

Chacun écrivait sa propre version de serveurs HTTP. Le partage de code devenait difficile, le monde Java exigeait une standardisation. 
**Entrez la spécification des servlets Java.**

Avant de continuer, définissons quelques termes :

**Développeur de serveurs Java** : Les personnes qui utilisent l'API de socket Java et implémentent le protocole HTTP comme Tomcat.

**Développeur d'applications Java** : Les personnes qui construisent des applications métier sur Tomcat.

REVENONS AU SUJET

Une fois la spécification des servlets Java entrée dans le monde, elle a dit :

_Chers développeurs de serveurs Java,_ veuillez fournir une méthode comme ci-dessous :

```
doGet(inputReq, OutPutRes)
```

afin que le _développeur d'applications Java_ puisse implémenter `doGet` et écrire leur logique métier. Une fois que le _"développeur d'applications"_ souhaite envoyer la `réponse`, il peut appeler `OutPutRes.write()`.

**Une chose à noter :** Puisque l'API de socket est bloquante, `OutPutRes.write()` est également bloquant. De plus, une limitation supplémentaire était que l'objet de réponse était validé à la **sortie de la méthode doGet**.

En raison de ces limitations, les gens devaient utiliser un thread pour traiter une requête.

Le temps a passé et Internet a pris le dessus sur le monde. [_Un thread par requête_](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request) a commencé à montrer ses limites.

### Problème 1 :

Le modèle [thread-par-requête](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request) échoue lorsqu'il y a de longues pauses pendant le traitement de chaque requête.

> _Par exemple : la récupération de données depuis un sous-service prend beaucoup de temps._

Dans une telle situation, le thread est principalement inactif et la JVM peut facilement manquer de threads.

### Problème 2 :

Les choses se sont aggravées avec les [connexions persistantes http1.1](https://en.wikipedia.org/wiki/HTTP_persistent_connection). Avec une connexion persistante, la connexion TCP sous-jacente reste active et le serveur doit bloquer _un thread par connexion_.

> _Mais pourquoi le serveur doit-il bloquer_ un thread par connexion ? 
> _Puisque le système d'exploitation fournit une API de socket bloquante Recv, la JVM doit appeler la méthode Recv bloquante du système d'exploitation afin d'écouter d'autres requêtes sur la même connexion TCP depuis le client._

### **Le monde exigeait une solution !**

**La première solution** est venue des créateurs de la JVM. Ils ont introduit [NIO(**ASYNC-IO**)](https://en.wikipedia.org/wiki/Non-blocking_I/O_(Java)). Nio est l'API non bloquante pour envoyer/recevoir des données via une socket.

**Un peu de contexte :** le système d'exploitation, en plus de l'API de socket bloquante, fournit également une version non bloquante de l'API de socket.

Mais comment le système d'exploitation fournit-il cela... Crée-t-il un thread en interne et ce thread se bloque ???

La RÉPONSE est non... le système d'exploitation demande au matériel d'interrompre lorsqu'il y a des données à lire ou à écrire.

NIO a permis au _"développeur de serveurs Java"_ de résoudre le **problème 2** de blocage _d'un thread par connexion TCP_. Avec NIO étant une connexion persistante HTTP, le thread n'a pas besoin de se bloquer sur l'appel _recv_. Au lieu de cela, il peut maintenant le traiter uniquement lorsqu'il y a des données à traiter. Cela a permis à un thread de surveiller/gérer un grand nombre de connexions persistantes.

**La deuxième solution** est venue de la spécification des servlets. La spécification des servlets a été mise à niveau et ils ont introduit le [**support asynchrone**](https://docs.oracle.com/javaee/7/tutorial/servlets012.htm) **(Traitement Asynchrone des Requêtes).**

```
AsyncContext acontext = req.startAsync();
```

> **_IMPORTANT:_** _Cette mise à niveau a supprimé la limitation de validation de l'objet de réponse à la **fin de la méthode doGet**._

Cela a permis au _"développeur d'applications Java"_ de résoudre le **problème 1**, en déléguant le travail à des threads en arrière-plan. Maintenant, au lieu de garder le thread en attente pendant la longue pause, le thread peut être utilisé pour traiter d'autres requêtes.

### CONCLUSION :

_Async-IO_ en Java consiste essentiellement à utiliser la version non bloquante de l'API de socket du système d'exploitation.

Le _traitement asynchrone des requêtes_ est essentiellement la standardisation par la spécification des servlets de la manière de traiter plus de requêtes avec un seul thread.

### RÉFÉRENCES :

[https://www.scottklement.com/rpg/socktut/tutorial.pdf](https://www.scottklement.com/rpg/socktut/tutorial.pdf)  
[https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request](https://stackoverflow.com/questions/15217524/what-is-the-difference-between-thread-per-connection-vs-thread-per-request)

> _Motivation de l'article : Apprentissage d'équipe/Partage des connaissances_