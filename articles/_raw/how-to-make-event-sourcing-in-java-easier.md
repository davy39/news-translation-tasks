---
title: How to Make Event Sourcing in Java Easier
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
seo_title: null
seo_desc: 'By Bertil Muth

  Event sourcing is about persisting events instead of just the current state. Event
  sourcing can be helpful for auditing purposes, and to analyze or rebuild previous
  system states for business analysis.

  Let''s look at it in a bit more de...'
---

By Bertil Muth

Event sourcing is about persisting events instead of just the current state. Event sourcing can be helpful for auditing purposes, and to analyze or rebuild previous system states for business analysis.

Let's look at it in a bit more detail: every time you make a change to the application state, you record the change as an event.

You can replay the events since the beginning of the recording, up to a certain time. Then you've recreated the state of the application at that time. And by merging the events into a different data structure, you can provide a user specific view of the state (a "query model").

Think of a shopping cart: a typical e-commerce application would only store the state of the cart when the user proceeds to checkout. What if you want to know which shopping cart items have been removed by the user, to optimize the purchasing flow? That's when storing each event becomes helpful, for example `ShoppingCartItemRemoved`.

## Event Sourcing Hello World Example

In this example, a user sends a POST HTTP request with the data of a `CreateGreeting` command to the backend. This command contains the name of the person to greet. 

The backend transforms the command into a `GreetingCreated` event. This event contains the person's name from the command, and a default salutation (`Hello,`):

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--4PlWs_1a--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nwjsupcxesbrk288j279.PNG)

The event also contains the id of the entity you see in the middle: the `Greeting` entity that consumes the commands, and produces the events. That way, the state of this entity can later be reconstructed.

By producing the event, the `Greeting` entity has accepted the command as valid, and the event records this as a fact. The event is now stored in a journal, for example an in-memory, relational, or NoSQL database.

So far, the state of the `Greeting` entity hasn't changed yet. To change the state, `Greeting` takes the event and current state as input, and produces a new instance of the state class:

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--gRyVptBX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uiy6jr5ipknxjpz5vqy6.png)

Objects of `GreetingState` are immutable. `Greeting` replaces the old state with the new state after applying the event.

What if you want to change the salutation for Jill's greeting later on? This can be done with a `ChangeSalutation` command. If you encode the id of Jill's `Greeting` entity in the request URL, the command handling looks like this:

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--PB5bLgHr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a5sc976cdgdy3ff8cing.PNG)

Note that the event captures only the information that is relevant for the change about to happen. It doesn't need to capture all information in `GreetingState`.

Applying the `SalutationChanged` event looks like this:

![Image description](https://res.cloudinary.com/practicaldev/image/fetch/s--4yzt35Bt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9ujrmctd31vcdlebtejz.PNG)

The interesting thing is this: `Greeting` takes the salutation from the event, and combines it with the `personName` from its current state, to produce the new state.

## Implementing Event Sourcing is Hard

The problem I've seen in this. When building an event-sourced application, there is a steep learning curve. Not only do you need to get adjusted to this new way of thinking about state – you also need to learn the event sourcing library/framework details.

I want to change that. I created the Being library. It aims to cut down the technical complexity as far as possible. You can find it on [GitHub](https://github.com/bertilmuth/being). It's in an early stage of development, so I'm very thankful for any feedback you might have.

## Command and event handling code

When you use Being, you need to define the command handlers: which types of commands the entity consumes, and which event(s) it produces as a reaction to each command.

You also need to define the event handlers: for each of the event types, which new entity state to create as a reaction to it.

The behavior of the `Greeting` entity shown below has the following [code](https://github.com/bertilmuth/being-samples/blob/main/greetings/src/main/java/org/requirementsascode/being/samples/greeting/model/Greeting.java):

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

Apart from the `initialState()` method that defines the starting state of `Greeting`, this should look pretty familiar.

The first command handler consumes a `CreateGreeting` command that contains the name of the person to greet, and produces a `GreetingCreated` event.

But a user can also change the salutation via a `ChangeSalutation` command. This command contains only the new text for the salutation, not the person's name. The person is identified by the entity's id, `state.id`.

Both the command handlers and the event handlers can use the current state of the entity. So when a `SalutationChanged` event is applied, the person name is not taken from the event, but from the current state of the entity: `(event,state) -> new GreetingState(event.id, event.salutation, state.personName)`.

## Code for the Greeting entity's state

Here's the code for the `GreetingState` class that represents the state of the entity:

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
    
    // hashCode() and equals() omitted for brevity
}

```

As you can see, objects of the state class are immutable.

## Code for commands and events

Commands are simple POJOs, as you can see in the following example:

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

Commands of an entity implement a common interface, like `GreetingCommand` in the example, which may be empty:

```java
public interface GreetingCommand {
}
```

The reason for having a common interface for the commands is type safety. Use this command interface as the first type parameter of the entity class, as shown above.

Each event class must be a subclass of `IdentifiedDomainEvent`:

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

Being is based on the powerful [VLINGO XOOM](https://docs.vlingo.io/) platform that defines the `IdentifiedDomainEvent` super class.

## Conclusion

Apart from what I've shown above, you also need to define the HTTP request handlers. The [Being](https://github.com/bertilmuth/being) website explains how to do that.

I want to invite you to have a look at it, if you find this topic interesting. And I'm very grateful for feedback.

To drop me a note, visit the [Gitter community](https://gitter.im/requirementsascode/community) or contact [me](https://twitter.com/BertilMuth) on Twitter.

