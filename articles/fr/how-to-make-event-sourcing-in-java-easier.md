---
title: Comment faciliter l'Event Sourcing en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-21T16:23:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-event-sourcing-in-java-easier
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/thisisengineering-raeng-64YrPKiguAE-unsplash.jpg
tags:
- name: Event Sourcing
  slug: event-sourcing
seo_title: Comment faciliter l'Event Sourcing en Java
seo_desc: 'By Bertil Muth

  Event sourcing is about persisting events instead of just the current state. Event
  sourcing can be helpful for auditing purposes, and to analyze or rebuild previous
  system states for business analysis.

  Let''s look at it in a bit more de...'
---

Par Bertil Muth

L'Event Sourcing consiste à persister les événements plutôt que simplement l'état actuel. L'Event Sourcing peut être utile pour des fins d'audit, et pour analyser ou reconstruire des états précédents du système pour des analyses métiers.

Examinons cela un peu plus en détail : chaque fois que vous apportez une modification à l'état de l'application, vous enregistrez la modification sous forme d'événement.

Vous pouvez rejouer les événements depuis le début de l'enregistrement, jusqu'à un certain moment. Vous avez alors recréé l'état de l'application à ce moment-là. Et en fusionnant les événements dans une structure de données différente, vous pouvez fournir une vue spécifique de l'état pour l'utilisateur (un "modèle de requête").

Prenons l'exemple d'un panier d'achat : une application e-commerce typique ne stockerait que l'état du panier lorsque l'utilisateur passe à la caisse. Que faire si vous souhaitez savoir quels articles du panier ont été supprimés par l'utilisateur, afin d'optimiser le processus d'achat ? C'est là que le stockage de chaque événement devient utile, par exemple `ShoppingCartItemRemoved`.

## Exemple Hello World de l'Event Sourcing

Dans cet exemple, un utilisateur envoie une requête HTTP POST avec les données d'une commande `CreateGreeting` au backend. Cette commande contient le nom de la personne à saluer.

Le backend transforme la commande en un événement `GreetingCreated`. Cet événement contient le nom de la personne de la commande, et une salutation par défaut (`Hello,`) :

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--4PlWs_1a--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nwjsupcxesbrk288j279.PNG)

L'événement contient également l'id de l'entité que vous voyez au milieu : l'entité `Greeting` qui consomme les commandes et produit les événements. Ainsi, l'état de cette entité peut être reconstruit plus tard.

En produisant l'événement, l'entité `Greeting` a accepté la commande comme valide, et l'événement enregistre cela comme un fait. L'événement est maintenant stocké dans un journal, par exemple une base de données en mémoire, relationnelle ou NoSQL.

Jusqu'à présent, l'état de l'entité `Greeting` n'a pas encore changé. Pour changer l'état, `Greeting` prend l'événement et l'état actuel en entrée, et produit une nouvelle instance de la classe d'état :

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--gRyVptBX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uiy6jr5ipknxjpz5vqy6.png)

Les objets de `GreetingState` sont immutables. `Greeting` remplace l'ancien état par le nouvel état après avoir appliqué l'événement.

Que faire si vous souhaitez changer la salutation pour le message de Jill plus tard ? Cela peut être fait avec une commande `ChangeSalutation`. Si vous encodez l'id de l'entité `Greeting` de Jill dans l'URL de la requête, la gestion de la commande ressemble à ceci :

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--PB5bLgHr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a5sc976cdgdy3ff8cing.PNG)

Notez que l'événement capture uniquement les informations pertinentes pour le changement à venir. Il n'a pas besoin de capturer toutes les informations dans `GreetingState`.

L'application de l'événement `SalutationChanged` ressemble à ceci :

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--4yzt35Bt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9ujrmctd31vcdlebtejz.PNG)

L'intérêt est le suivant : `Greeting` prend la salutation de l'événement et la combine avec le `personName` de son état actuel, pour produire le nouvel état.

## Implémenter l'Event Sourcing est difficile

Le problème que j'ai vu dans ce domaine. Lors de la construction d'une application basée sur l'Event Sourcing, il y a une courbe d'apprentissage abrupte. Non seulement vous devez vous adapter à cette nouvelle façon de penser l'état, mais vous devez également apprendre les détails de la bibliothèque/du framework d'Event Sourcing.

Je veux changer cela. J'ai créé la bibliothèque Being. Elle vise à réduire la complexité technique autant que possible. Vous pouvez la trouver sur [GitHub](https://github.com/bertilmuth/being). Elle est à un stade précoce de développement, donc je suis très reconnaissant pour tout retour que vous pourriez avoir.

## Code de gestion des commandes et des événements

Lorsque vous utilisez Being, vous devez définir les gestionnaires de commandes : quels types de commandes l'entité consomme, et quel(s) événement(s) elle produit en réaction à chaque commande.

Vous devez également définir les gestionnaires d'événements : pour chaque type d'événement, quel nouvel état d'entité créer en réaction à celui-ci.

Le comportement de l'entité `Greeting` montré ci-dessous a le [code](https://github.com/bertilmuth/being-samples/blob/main/greetings/src/main/java/org/requirementsascode/being/samples/greeting/model/Greeting.java) suivant :

```java
public class Greeting implements AggregateBehavior<GreetingCommand, GreetingState> {
	@Override
	public GreetingState initialState(final String id) {
		return GreetingState.identifiedBy(id);
	}

	@Override
	public CommandHandlers<GreetingCommand, GreetingState> commandHandlers() {
		return CommandHandlers.handle(
			commandsOf(CreateGreeting.class).with((cmd, state) -> new GreetingCreated(state.id, "Hello,", cmd.personName)),
			commandsOf(ChangeSalutation.class).with((cmd, state) -> new SalutationChanged(state.id, cmd.salutation)));
	}

	@Override
	public EventHandlers<GreetingState> eventHandlers() {
		return EventHandlers.handle(
			eventsOf(GreetingCreated.class)
				.with((event, state) -> new GreetingState(event.id, event.salutation, event.personName)),
			eventsOf(SalutationChanged.class)
				.with((event, state) -> new GreetingState(event.id, event.salutation, state.personName)));
	}
}
```

À part la méthode `initialState()` qui définit l'état initial de `Greeting`, cela devrait vous sembler assez familier.

Le premier gestionnaire de commandes consomme une commande `CreateGreeting` qui contient le nom de la personne à saluer, et produit un événement `GreetingCreated`.

Mais un utilisateur peut également changer la salutation via une commande `ChangeSalutation`. Cette commande contient uniquement le nouveau texte pour la salutation, et non le nom de la personne. La personne est identifiée par l'id de l'entité, `state.id`.

Les gestionnaires de commandes et les gestionnaires d'événements peuvent utiliser l'état actuel de l'entité. Ainsi, lorsqu'un événement `SalutationChanged` est appliqué, le nom de la personne n'est pas pris de l'événement, mais de l'état actuel de l'entité : `(event,state) -> new GreetingState(event.id, event.salutation, state.personName)`.

## Code pour l'état de l'entité Greeting

Voici le code pour la classe `GreetingState` qui représente l'état de l'entité :

```java
public final class GreetingState {
    public final String id;
    public final String salutation;
    public final String personName;

    public static GreetingState identifiedBy(final String id) {
        return new GreetingState(id, "", "");
    }

    public GreetingState(final String id, final String salutation, final String personName) {
        this.id = id;
        this.salutation = salutation;
        this.personName = personName;
    }

    @Override
    public String toString() {
        return "GreetingState [id=" + id + ", salutation=" + salutation + ", personName=" + personName + "]";
    }
    
    // hashCode() et equals() omis pour plus de concision
}

```

Comme vous pouvez le voir, les objets de la classe d'état sont immutables.

## Code pour les commandes et les événements

Les commandes sont des POJOs simples, comme vous pouvez le voir dans l'exemple suivant :

```java
public class CreateGreeting implements GreetingCommand{
    public final String personName;

    public CreateGreeting(String personName) {
        this.personName = personName;
    }

    @Override
    public String toString() {
        return "CreateGreeting [personName=" + personName + "]";
    }
}

```

Les commandes d'une entité implémentent une interface commune, comme `GreetingCommand` dans l'exemple, qui peut être vide :

```java
public interface GreetingCommand {
}
```

La raison d'avoir une interface commune pour les commandes est la sécurité des types. Utilisez cette interface de commande comme premier paramètre de type de la classe d'entité, comme montré ci-dessus.

Chaque classe d'événement doit être une sous-classe de `IdentifiedDomainEvent` :

```java
public final class GreetingCreated extends IdentifiedDomainEvent {
    public final String id;
    public final String salutation;
    public final String personName;

    public GreetingCreated(final String id, final String salutation, String personName) {
        super(SemanticVersion.from("1.0.0").toValue());
        this.id = id;
        this.salutation = salutation;
        this.personName = personName;
    }

    @Override
    public String identity() {
        return id;
    }

    @Override
    public String toString() {
        return "GreetingCreated [id=" + id + ", salutation=" + salutation + ", personName=" + personName + "]";
    }
}

```

Being est basé sur la puissante plateforme [VLINGO XOOM](https://docs.vlingo.io/) qui définit la super classe `IdentifiedDomainEvent`.

## Conclusion

En plus de ce que j'ai montré ci-dessus, vous devez également définir les gestionnaires de requêtes HTTP. Le site [Being](https://github.com/bertilmuth/being) explique comment faire cela.

Je vous invite à y jeter un coup d'œil si vous trouvez ce sujet intéressant. Et je suis très reconnaissant pour tout retour.

Pour me laisser un mot, visitez la [communauté Gitter](https://gitter.im/requirementsascode/community) ou contactez-[moi](https://twitter.com/BertilMuth) sur Twitter.