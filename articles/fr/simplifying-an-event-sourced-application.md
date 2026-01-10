---
title: Simplifier une application basée sur l'event sourcing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-21T12:43:28.000Z'
originalURL: https://freecodecamp.org/news/simplifying-an-event-sourced-application
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/EventSourcing.jpg
tags:
- name: coding
  slug: coding
- name: Event Sourcing
  slug: event-sourcing
- name: events
  slug: events
- name: Java
  slug: java
seo_title: Simplifier une application basée sur l'event sourcing
seo_desc: 'By Bertil Muth

  Every time you make a change to the application state, you record the change as
  an event.You can replay the events since the beginning of the recording, up to a  certain
  time. Then you''ve recreated the state of the application at that ...'
---

Par Bertil Muth

Chaque fois que vous apportez une modification à l'état de l'application, vous enregistrez la modification sous forme d'événement. 
Vous pouvez rejouer les événements depuis le début de l'enregistrement, jusqu'à un certain moment. Vous avez alors recréé l'état de l'application à ce moment-là.

C'est ce qu'est [l'Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html). C'est comme si vous pouviez voyager dans le temps vers le passé. Je trouve cela fascinant.

L'event sourcing fournit une piste d'audit lorsque vous devez répondre à des exigences réglementaires. Il peut aider au débogage. Et vous pouvez même explorer des réalités alternatives : qu'aurait-il arrivé si...

J'ai récemment vu une [excellente conférence](https://youtu.be/r7AGQsM7ncA) de [Jakub Pilimon](https://twitter.com/JakubPilimon) et [Kenny Bastani](https://twitter.com/kennybastani) sur l'event sourcing.

La conférence est une session de codage en direct d'une heure. Les deux intervenants commencent avec une application simple qui n'est pas basée sur l'event sourcing. Ensuite, ils la refactorisent pour utiliser des événements.

Ils finissent par connecter l'application avec Apache Kafka. Je vais sauter cette partie dans cet article et me concentrer sur la partie conceptuelle de l'event sourcing.

## Un résumé de la conférence

En tant qu'utilisateur d'une application de gestion de cartes de crédit, vous pouvez :

* Attribuer une limite à la carte de crédit
* Retirer de l'argent
* Rembourser de l'argent

Pour chacune de ces commandes, il y a une méthode dans la classe `CreditCard`. 
Voici le code original de la méthode `assignLimit` :

```java
public void assignLimit(BigDecimal amount) { 
  if(limitAlreadyAssigned()) {  
    throw new IllegalStateException(); 
  }
  this.initialLimit = amount; 
}

```

Voici la méthode `withdraw` :

```java
    public void withdraw(BigDecimal amount) {
        if(notEnoughMoneyToWithdraw(amount)) {
            throw new IllegalStateException();
        }
        if(tooManyWithdrawalsInCycle()) {
            throw new IllegalStateException();
        }
        this.usedLimit = usedLimit.add(amount);
        withdrawals++;
    }

```

La méthode `repay` est similaire.

Rappelez-vous que pour l'event sourcing, vous devez enregistrer un événement chaque fois que l'application change d'état ? 
Ainsi, les intervenants extraient chaque changement d'état dans sa propre méthode dans la classe [CreditCard](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/model/CreditCard.java).

Voici la méthode `withdraw` refactorisée :

```java
   public void withdraw(BigDecimal amount) {
        if(notEnoughMoneyToWithdraw(amount)) {
            throw new IllegalStateException();
        }
        if(tooManyWithdrawalsInCycle()) {
            throw new IllegalStateException();
        }
        cardWithdrawn(new CardWithdrawn(uuid, amount, Instant.now()));
    }

    private CreditCard cardWithdrawn(CardWithdrawn event) {
        this.usedLimit = usedLimit.add(event.getAmount());
        withdrawals++;
        pendingEvents.add(event);
        return this;
    }

```

Une instance de `CardWithdrawn` représente l'événement qu'un utilisateur a retiré de l'argent avec succès. _Après_ que l'état a changé, l'événement est ajouté à la liste des événements en attente.

Vous appelez la méthode `save` de la classe [CreditCardRepository](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/persistence/CreditCardRepository.java) pour vider les événements en attente vers le flux d'événements. Les auditeurs d'événements peuvent alors traiter les événements.

Outre la charge utile, chaque événement a son propre identifiant unique et un horodatage. Vous pouvez donc séquencer et rejouer les événements plus tard. 
Pour rejouer les événements pour une carte de crédit spécifique, le dépôt appelle la méthode `recreateFrom` de la classe [CreditCard](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/model/CreditCard.java), en passant l'identifiant de la carte et les événements stockés pour celle-ci :

```java
    public static CreditCard recreateFrom(UUID uuid, List<DomainEvent> events) {
        return ofAll(events).foldLeft(new CreditCard(uuid), CreditCard::handle);
    }

    private CreditCard handle(DomainEvent event) {
        return Match(event).of(
                Case($(Predicates.instanceOf(LimitAssigned.class)), this::limitAssigned),
                Case($(Predicates.instanceOf(CardWithdrawn.class)), this::cardWithdrawn),
                Case($(Predicates.instanceOf(CardRepaid.class)), this::cardRepaid),
                Case($(Predicates.instanceOf(CycleClosed.class)), this::cycleWasClosed)
        );
    }
```

Ce code utilise la bibliothèque [vavr.io](http://www.vavr.io/) pour appeler la méthode `handle` pour chaque événement. La méthode `handle` envoie l'objet événement à la méthode appropriée. 
Par exemple : pour chaque événement `LimitAssigned`, la méthode `handle` appelle la méthode `limitAssigned` avec l'événement comme paramètre.

## Simplifier l'application

J'ai utilisé la bibliothèque [requirements as code](https://github.com/bertilmuth/requirementsascode) pour simplifier le code. Tout d'abord, j'ai placé toutes les classes d'événements et les méthodes de gestion dans un modèle. Comme ceci :

```java
this.eventHandlingModel = 
        Model.builder()
           .on(LimitAssigned.class).system(this::limitAssigned)
           .on(CardWithdrawn.class).system(this::cardWithdrawn)
           .on(CardRepaid.class).system(this::cardRepaid)
           .on(CycleClosed.class).system(this::cycleWasClosed)
       .build();

```

J'ai dû changer le type de retour des méthodes de gestion (par exemple, `limitAssigned`) en `void`. À part cela, la conversion depuis [vavr.io](http://www.vavr.io/) était directe.

Ensuite, j'ai créé un runner et je l'ai démarré pour le modèle :

```java
this.modelRunner = new ModelRunner();
modelRunner.run(eventHandlingModel);

```

Après cela, j'ai modifié les méthodes `recreateFrom` et `handle` comme suit :

```java
public static CreditCard recreateFrom(UUID uuid, List<DomainEvent> events) {
    CreditCard creditCard = new CreditCard(uuid);
    events.forEach(ev -> creditCard.handle(ev));
    return creditCard;
}

private void handle(DomainEvent event) {
    modelRunner.reactTo(event);
}

```

À ce stade, j'ai pu me débarrasser de la dépendance à [vavr.io](http://www.vavr.io/). 
Transition terminée. Maintenant, je pouvais faire quelques simplifications supplémentaires.

J'ai revisité la méthode `withdraw` :

```java
public void withdraw(BigDecimal amount) {
    if(notEnoughMoneyToWithdraw(amount)) {
        throw new IllegalStateException();
    }
    if(tooManyWithdrawalsInCycle()) {
        throw new IllegalStateException();
    }
    cardWithdrawn(new CardWithdrawn(uuid, amount, Instant.now()));
}

```

La vérification `tooManyWithdrawalsInCycle()` ne dépendait pas des données de l'événement. Elle ne dépendait que de l'état de la `CreditCard`. 
Les vérifications d'état comme celle-ci peuvent être représentées dans le modèle en tant que `conditions`.

Après avoir déplacé toutes les vérifications d'état pour toutes les méthodes vers le modèle, cela ressemblait à ceci :

```java
this.eventHandlingModel = 
  Model.builder()
    .condition(this::limitNotAssigned)
        .on(LimitAssigned.class).system(this::limitAssigned)
    .condition(this::limitAlreadyAssigned)
        .on(LimitAssigned.class).system(this::throwsException)
    .condition(this::notTooManyWithdrawalsInCycle)
        .on(CardWithdrawn.class).system(this::cardWithdrawn)
    .condition(this::tooManyWithdrawalsInCycle)
        .on(CardWithdrawn.class).system(this::throwsException)
    .on(CardRepaid.class).system(this::cardRepaid)
    .on(CycleClosed.class).system(this::cycleWasClosed)
.build();

```

Pour que cela fonctionne, j'ai dû remplacer les appels directs aux méthodes qui changent l'état par la méthode `handle`. Après cela, les méthodes `assignLimit` et `withdraw` ressemblaient à ceci :

```java
public void assignLimit(BigDecimal amount) { 
    handle(new LimitAssigned(uuid, amount, Instant.now()));
}

private void limitAssigned(LimitAssigned event) {
    this.initialLimit = event.getAmount(); 
    pendingEvents.add(event);
}

public void withdraw(BigDecimal amount) {
    if(notEnoughMoneyToWithdraw(amount)) {
        throw new IllegalStateException();
    }
    handle(new CardWithdrawn(uuid, amount, Instant.now()));
}

private void cardWithdrawn(CardWithdrawn event) {
    this.usedLimit = usedLimit.add(event.getAmount());
    withdrawals++;
    pendingEvents.add(event);
}

```

Comme vous pouvez le voir, la plupart de la logique conditionnelle a été déplacée des méthodes vers le modèle. Cela rend les méthodes plus faciles à comprendre.

Une chose qui me dérangeait est que vous ne devez pas oublier d'ajouter l'événement aux événements en attente. À chaque fois. Sinon, votre code ne fonctionnera pas.

[Requirements as code](https://github.com/bertilmuth/requirementsascode) vous permet de contrôler la manière dont le système gère les événements. J'ai donc extrait `pendingEvents.add(event)` des méthodes également :

```java
modelRunner.handleWith(this::addingPendingEvents);
...

public void addingPendingEvents(StepToBeRun stepToBeRun) {
    stepToBeRun.run();
    DomainEvent domainEvent = (DomainEvent) stepToBeRun.getEvent().get();
    pendingEvents.add(domainEvent);
}

```

J'aurais pu aller plus loin et extraire également la logique de validation. 
Mais je vous laisse cela comme exercice de réflexion, cher lecteur.

## Quel est l'intérêt ?

Ce que j'ai essayé d'atteindre est une séparation claire des préoccupations :

* L'exécution dépendante de l'état des méthodes est définie dans le modèle
* La validation des données et les changements d'état sont dans les implémentations des méthodes
* Les événements sont automatiquement ajoutés aux événements en attente. En général : le code d'infrastructure est clairement séparé de la logique métier.

Simplifier un exemple qui est déjà très simple est bon pour expliquer. 
Mais ce n'est pas le point que je veux faire.

Le point est : avoir une telle séparation claire des préoccupations est payant en pratique. 
Surtout si vous travaillez avec plusieurs équipes. Sur des problèmes compliqués.

La séparation des préoccupations aide à changer différentes parties du code à un rythme différent. Vous avez des règles simples pour trouver quelque chose. Le code est plus facile à comprendre. Et il est plus facile d'isoler des unités à des fins de test.

## Conclusion

J'espère que vous avez apprécié mon article. Veuillez me donner votre avis.

Avez-vous travaillé sur des applications basées sur l'event sourcing ? 
Quelles ont été vos expériences ? 
Pouvez-vous vous identifier à ce que j'ai écrit dans cet article ?

Je veux également vous inviter à regarder [ma bibliothèque](https://github.com/bertilmuth/requirementsascode) que j'ai utilisée tout au long de l'article. Je serais ravi si vous l'essayez en pratique et me dites ce que vous en pensez.

_Cet article a été publié pour la première fois sur [dev.to](https://dev.to/bertilmuth/simplifying-an-event-sourced-application-1klp)_