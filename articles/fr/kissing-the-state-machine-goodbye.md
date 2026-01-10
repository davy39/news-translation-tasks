---
title: Dire adieu à la machine à états
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-27T21:05:06.000Z'
originalURL: https://freecodecamp.org/news/kissing-the-state-machine-goodbye
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Kissing.png
tags:
- name: coding
  slug: coding
- name: Event Sourcing
  slug: event-sourcing
- name: finite state machine
  slug: finite-state-machine
- name: Java
  slug: java
- name: Statecharts
  slug: statecharts
seo_title: Dire adieu à la machine à états
seo_desc: 'By Bertil Muth

  Recently, I have written about simplifying an event sourced application.

  The article starts with code from a talk by Jakub Pilimon and Kenny Bastani. And
  it ends with building a model  for events in the code: how they are applied, and
  ...'
---

Par Bertil Muth

Récemment, j'ai écrit un article sur la [simplification d'une application basée sur les événements](https://www.freecodecamp.org/news/simplifying-an-event-sourced-application/).

L'article commence avec du [code](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/) issu d'une [conférence](https://youtu.be/r7AGQsM7ncA) de Jakub Pilimon et Kenny Bastani. Et il se termine par la construction d'un modèle pour les événements dans le code : comment ils sont appliqués et sous quelles conditions.

L'application exemple concerne la gestion de cartes de crédit. Vous pouvez :

* **Attribuer une limite de crédit**. Mais une seule fois, sinon l'application lance une `IllegalStateException`.
* **Retirer de l'argent**. Mais vous ne pouvez pas effectuer plus de 45 retraits dans un certain cycle. Sinon, vous obtiendrez également une exception.
* **Rembourser de l'argent**

J'ai joué avec la classe `CreditCard`. J'avais l'impression que quelque chose n'allait pas avec la méthode `withdraw`. J'ai donc écrit un test pour vérifier le comportement correct.

```java
@Test(expected = IllegalStateException.class)
public void withdrawWithoutLimitAssignedThrowsIllegalStateException() {
    CreditCard card = new CreditCard(UUID.randomUUID());
    card.withdraw(BigDecimal.ZERO);
}
```

Le test tente de retirer un montant de zéro. Mais aucune limite de crédit n'a été attribuée auparavant. L'application devrait rejeter cela et lancer une `IllegalStateException`.
Au lieu de cela, l'application a lancé une `NullPointerException`.

L'application supposait que la limite avait été attribuée auparavant.
Maintenant : il s'agit d'une application exemple. Si elle couvrait tous les cas, elle ne serait probablement pas aussi compréhensible qu'elle ne l'est.

Prétendons que nous traitons une application réelle. Et si l'ordre requis des commandes/événements dépendait d'une multitude de conditions et d'états ?

Si vous avez déjà essayé de mettre cela en œuvre avec des instructions conditionnelles uniquement, vous savez probablement qu'il est facile de perdre la vue d'ensemble. Mais il existe une solution standard pour gérer les flux compliqués et les changements de comportement.

## La machine à états à la rescousse

En informatique, les machines à états existent depuis des décennies. Elles sont bien comprises en théorie. Elles sont éprouvées en pratique. Elles sont le standard de facto pour traiter le comportement dépendant de l'état.

J'ai donc décidé de créer un modèle de machine à états UML pour l'application exemple. Je me suis d'abord demandé : veux-je traiter les commandes ou les événements dans la machine à états ?

Les commandes concernent quelque chose que l'application doit faire à l'avenir.
Les événements concernent quelque chose qui s'est produit dans le passé.

Je voulais _empêcher_ les retraits sans attribution de limite de crédit.
Le modèle de machine à états devait donc traiter les commandes.

La syntaxe d'une transition dans le diagramme est `command[condition] / commandHandler()`. Cela signifie : lorsqu'un objet de commande a été reçu et que la condition est remplie si présente, traiter la commande et passer à l'état suivant.

![Machine à états](https://res.cloudinary.com/practicaldev/image/fetch/s--IsFVxafc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/3laq9tz8h82nwvjsmugv.png)

Le modèle fixe ce qui est autorisé à se produire et ce qui ne l'est pas. Par exemple : le remboursement n'est possible qu'après un retrait.

Mais cette précision a un prix. Si vous voulez que le modèle de machine à états soit exécuté et contrôle le comportement à l'exécution, vous devez modéliser chaque transition possible à partir de chaque état. Y compris sa condition, s'il y a deux transitions avec le même événement.

C'est pourquoi il y a beaucoup plus de répétitions dans la machine à états que dans le code original avec les instructions `if`. Une façon de réduire la quantité de répétitions est d'utiliser des _super états_ et des _sous-états_ :

![Machine à états avec sous-états](https://res.cloudinary.com/practicaldev/image/fetch/s--CCZSYf5s--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2cwl67ddaa64l2szlp4s.png)

Il est facile de définir un comportement dépendant de l'état dans un modèle de machine à états. Mais une règle indépendante de l'état comme _dans n'importe quel état (quand la condition X est remplie), faire Y_ conduit à plusieurs transitions. Par exemple, j'ai dû ajouter `requestToCloseCycle` à chaque super état.

Vous avez besoin de personnes avec les bonnes compétences pour créer les modèles. Et il n'est pas facile de communiquer sur les modèles avec des parties prenantes non techniques. Ce n'est pas la façon dont elles parlent normalement des parcours utilisateurs.

## Dire adieu

Il semble qu'il y ait deux options jusqu'à présent.

Dans le coin gauche : l'instruction `if`. Facile à démarrer. Peu de surcharge. Meilleur pour les applications qui n'ont pas de flux de comportement compliqués. Mais il est facile de perdre la vue d'ensemble lorsque le comportement devient compliqué.

Dans le coin droit : le modèle de machine à états exécutable. Puissant. Éprouvé. Précis. Donne une vue d'ensemble du comportement. Mais il est difficile de définir des règles indépendantes de l'état. Et les modèles de machines à états sont difficiles à communiquer avec des parties prenantes non techniques.

Je me tiens dans le troisième coin. J'ai trouvé une alternative aux machines à états.
Une solution qui

* permet de définir des conditions. Mais vous n'avez pas à le faire dans la plupart des cas.
* rend les règles dépendantes et indépendantes de l'état également faciles à spécifier.
* utilise un langage que toutes les parties prenantes peuvent comprendre.

Avant d'entrer dans les détails, voici le modèle de machine à états exemple réécrit en utilisant cette solution :

```java
Model model = Model.builder()
  .useCase(useCreditCard)
    .basicFlow()
    	.step(assigningLimit).user(requestsToAssignLimit).systemPublish(assignedLimit)
    	.step(withdrawingCard).user(requestsWithdrawingCard).systemPublish(withdrawnCard).reactWhile(accountIsOpen)
    	.step(repaying).user(requestsRepay).systemPublish(repay).reactWhile(accountIsOpen)
    	
    .flow("Withdraw again").after(repaying)
    	.step(withdrawingCardAgain).user(requestsWithdrawingCard).systemPublish(withdrawnCard)
    	.step(repeating).continuesAt(withdrawingCard)
    	
    .flow("Cycle is over").anytime()
    	.step(closingCycle).on(requestToCloseCycle).systemPublish(closedCycle)
    	
    .flow("Limit can only be assigned once").condition(limitAlreadyAssigned)
    	.step(assigningLimitTwice).user(requestsToAssignLimit).system(throwsAssignLimitException)
    	
    .flow("Too many withdrawals").condition(tooManyWithdrawalsInCycle) 
    	.step(withdrawingCardTooOften).user(requestsWithdrawingCard).system(throwsTooManyWithdrawalsException)
.build();
return model;
```

Comme vous pouvez le voir, le modèle est [dans le code](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCardAggregateRoot.java). Un exécuteur de modèle exécute ce modèle. L'exécuteur réagit aux commandes/événements, similaire à une machine à états.

Le flux de base est le "scénario de jour heureux". Les étapes d'un utilisateur pour atteindre son objectif. Les autres flux couvrent les scénarios alternatifs et d'erreur.

Un flux peut définir une _condition explicite_ pour que sa première étape s'exécute - par exemple `after(...)`, `anytime()` ou `condition()` dans l'exemple.
Si un flux a une condition explicite, le flux commence lorsque la condition est remplie et que l'exécuteur est actuellement dans un flux différent.
Si un flux n'a pas de condition explicite (par exemple, le flux de base dans l'exemple), la première étape s'exécute après que l'exécuteur a démarré, lorsqu'aucune étape n'a été exécutée jusqu'à présent.

À partir de la deuxième étape d'un flux, chaque étape a une _condition implicite_. Cette condition est : exécuter l'étape après l'étape précédente dans le même flux, sauf si un flux différent avec une condition explicite peut démarrer.
Ainsi, contrairement aux machines à états, vous n'avez pas besoin de spécifier les conditions après la première étape.

En interne, le comportement dépendant de l'état est réalisé en vérifiant une condition.
Chaque étape contient sa condition complète qui définit exactement quand l'étape peut s'exécuter. C'est ainsi que [requirements as code](https://github.com/bertilmuth/requirementsascode) peut traiter le comportement dépendant et indépendant de l'état de la même manière.

Jetez un coup d'œil à [d'autres exemples](https://github.com/bertilmuth/requirementsascode/tree/master/requirementsascodeexamples/helloworld) pour approfondir.

## Quand utiliser les exigences en tant que code

De nombreuses applications ont un comportement interne dynamique. Cela est particulièrement vrai pour les applications distribuées. Elles doivent traiter le fait que "l'autre partie" n'est pas disponible.

Mais du point de vue de l'utilisateur, ces applications semblent assez prévisibles et régulières. Lorsque je veux regarder une émission sur Netflix ou Amazon Prime, je suis les mêmes étapes exactes chaque fois jusqu'à ce que je puisse la regarder. Cela semble comme si une étape suivait simplement l'autre.

C'est le point idéal pour les exigences en tant que code, si utilisé comme alternative à une machine à états : définir le _comportement visible_ d'une application.

## Comment fonctionne l'application de carte de crédit maintenant

* Un [client](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/EventsourcingApplication.java) envoie une commande à `CreditCardAggregateRoot`
* Le [CreditCardAggregateRoot](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCardAggregateRoot.java) utilise le dépôt d'événements pour rejouer tous les événements de la carte de crédit, pour la restaurer
* Le `CreditCardAggregateRoot` utilise le modèle ci-dessus pour dispatcher la commande à une méthode de gestion de commande
* La méthode de gestion de commande produit un événement et l'applique à l'instance `CreditCard`.
* Le modèle de gestion d'événements de l'instance [CreditCard](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCard.java) dispatch l'événement à une méthode de changement d'état

## Conclusion

J'espère que vous avez apprécié mon article. Je souhaite également vous inviter à regarder [la bibliothèque](https://github.com/bertilmuth/requirementsascode) que j'ai utilisée tout au long de l'article. Essayez-la en pratique et faites-moi savoir le résultat.

_Si vous souhaitez suivre ce que je fais ou me laisser un mot, suivez-moi sur [LinkedIn](https://www.linkedin.com/in/bertilmuth/) ou [Twitter](https://twitter.com/BertilMuth). Pour en savoir plus sur le développement logiciel agile, visitez mon [cours en ligne](https://skl.sh/2Cq497P)._
_Dernière édition le 27 avril 2020 : processus de sourcing d'événements mis à jour_