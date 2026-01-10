---
title: Si vous utilisez toujours Synchronized, vous devriez essayer Akka Actor à la
  place — voici pourquoi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T06:15:28.000Z'
originalURL: https://freecodecamp.org/news/still-using-synchronized-try-akka-actor-instead-ac2f2b22a9ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qep0tBNdjhQzyunssu4jvw.jpeg
tags:
- name: Akka
  slug: akka
- name: Java
  slug: java
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Si vous utilisez toujours Synchronized, vous devriez essayer Akka Actor
  à la place — voici pourquoi
seo_desc: 'By Martin Budi

  Synchronized is Java’s traditional concurrency mechanism. Although it is probably
  not something we see often these days, it is still fueling many libraries. The problem
  is, synchronized is both blocking and complicated. In this article...'
---

Par Martin Budi

_Synchronized_ est le mécanisme de concurrency traditionnel de Java. Bien qu'il ne soit probablement pas quelque chose que nous voyons souvent ces jours-ci, il alimente encore de nombreuses bibliothèques. Le problème est que synchronized est à la fois bloquant et compliqué. Dans cet article, je souhaite illustrer le problème de manière simple et expliquer mon raisonnement pour passer à Akka Actor pour une meilleure et plus facile concurrency.

Considérez ce simple code :

```java
  int x; 
 
 if (x > 0) {
   return true;
 } else {
   return false;
 }
```

Donc, retourne true si _x_ est positif. Simple.

Ensuite, considérez ce code encore plus simple :

```java
x++;
```

Oui, un compteur. Très simple, n'est-ce pas ?

Cependant, tous ces codes peuvent exploser de manière spectaculaire dans un environnement multi-thread.

Dans le premier exemple, true ou false n'est pas déterminé par la valeur de x. Il est en fait déterminé par le test if. Donc, si un autre thread change x en négatif juste après que le premier thread a passé le test if, nous obtiendrions toujours true même si x n'est plus positif.

Le deuxième exemple est assez trompeur. Bien qu'il ne s'agisse que d'une seule ligne, il y a en fait trois opérations : lire _x_, l'incrémenter et remettre la valeur mise à jour. Si deux threads s'exécutent exactement au même moment, la mise à jour peut être perdue.

Lorsque nous avons différents threads accédant et modifiant simultanément une variable, nous avons une condition de course. Si nous voulons simplement construire un compteur, Java fournit des variables atomiques thread-safe, parmi lesquelles Atomic Integer que nous pouvons utiliser à cette fin. Atomic Integer, cependant, ne fonctionne que sur des variables simples. Comment rendre plusieurs opérations atomiques ?

En utilisant un bloc _synchronized_. Tout d'abord, examinons un exemple plus élaboré.

```java
int x; 
public int withdraw(int deduct){
    int balance = x - deduct; 
    if (balance > 0) {
      x = balance;
      return deduct;
    } else {
      return 0;
    }
}
```

Ceci est une méthode de retrait d'argent très basique. Elle se trouve également être dangereuse. Deux threads s'exécutant en même temps peuvent amener la banque à effectuer deux retraits même si le solde n'est plus suffisant. Maintenant, voyons comment cela fonctionne avec un bloc synchronized :

```java
volatile int x;
public int withdraw(int deduct){
  synchronized(this){
    int balance = x - deduct; 
    if (balance > 0) {
      x = balance;
      return deduct;
    } else {
      return 0;
    }
  }
}
```

L'idée du bloc synchronized est simple. Un thread y entre et le verrouille, tandis que les autres threads attendent à l'extérieur. Le verrou est un objet, dans notre cas _this_. Une fois terminé, le verrou est libéré et passé à un autre thread qui fait alors la même chose. Notez également le mot-clé ésotérique _volatile_ qui est nécessaire pour empêcher le thread d'utiliser le cache CPU local de _x_.

Maintenant que les threads sont démêlés, la banque n'effectuera pas accidentellement de retraits non financés. Cependant, cette structure tend à devenir complexe avec plus de blocs et plus de verrous. Travailler avec plusieurs verrous est particulièrement risqué. Les blocs peuvent involontairement détenir la clé l'un de l'autre et finir par verrouiller toute l'application. Et en plus de cela, nous avons un problème d'efficacité. Rappelez-vous que pendant qu'un thread travaille à l'intérieur, tous les autres threads attendent à l'extérieur. Et les threads en attente sont bien... en attente. Ils ne font rien d'autre qu'attendre.

Alors, au lieu de faire un tel mécanisme, pourquoi ne pas simplement déposer le travail dans une file d'attente ? Pour mieux le visualiser, imaginez un système de messagerie. Lorsque vous envoyez un email, vous déposez l'email dans la boîte de réception du destinataire. Vous n'attendez pas jusqu'à ce que la personne le lise.

Ce sont les bases du modèle Actor et du framework Akka en général.

Actor encapsule l'état et le comportement. Contrairement à l'encapsulation de la POO, cependant, les acteurs n'exposent pas du tout leur état et leur comportement. La seule façon pour un acteur de communiquer avec un autre est d'échanger des messages. Les messages entrants sont déposés dans une boîte aux lettres et traités dans l'ordre premier entré, premier sorti. Voici un exemple retravaillé en Akka et Scala.

```scala
case class Withdraw(deduct: Int)
class ReplicaActor extends Actor {
  var x = 10;
  def receive: Receive = {
    case Withdraw(deduct) => val r = withdraw(deduct)
  }
}
class BossActor extends Actor {
  var replica = context.actorOf(Props[ReplicaActor])
  replica ! Withdraw(6)
  replica ! Withdraw(9)   
}
```

Nous avons un ReplicaActor qui fait le travail et un BossActor qui donne des ordres au replica. Tout d'abord, remarquez le signe ! ou _tell_. C'est l'une des deux méthodes (l'autre est _ask_) pour qu'un acteur envoie un message à un autre acteur de manière asynchrone. _tell_ en particulier le fait sans attendre de réponse. Donc le boss dit au replica d'effectuer deux ordres de retrait et quitte immédiatement. Ces messages arrivent dans le _receive_ du replica où chacun est extrait et associé au gestionnaire correspondant. Dans ce cas, _Withdraw_ exécute la méthode _withdraw_ de l'exemple précédent et déduit le montant demandé de l'état x. Une fois terminé, l'acteur passe au message suivant dans la file d'attente.

Alors, qu'obtenons-nous ici ? Pour commencer, nous n'avons plus à nous soucier du verrouillage et du travail avec des types atomiques/concurrents. L'encapsulation et le mécanisme de file d'attente de l'acteur garantissent déjà la sécurité des threads. Et il n'y a plus d'attente puisque les threads déposent simplement le message et reviennent. Les résultats peuvent être livrés plus tard avec _ask_ ou _tell_. C'est simple et sain.

Akka est basé sur la JVM et est disponible en Scala et en Java. Bien que cet article ne débatte pas de Java vs Scala, la correspondance de motifs et la programmation fonctionnelle de Scala seraient très utiles pour gérer la messagerie de données de l'acteur. À tout le moins, cela peut vous aider à écrire un code plus court en évitant les accolades et les points-virgules de Java.