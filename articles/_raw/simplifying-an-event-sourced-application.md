---
title: Simplifying an event sourced application
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
seo_title: null
seo_desc: 'By Bertil Muth

  Every time you make a change to the application state, you record the change as
  an event.You can replay the events since the beginning of the recording, up to a  certain
  time. Then you''ve recreated the state of the application at that ...'
---

By Bertil Muth

Every time you make a change to the application state, you record the change as an event.   
You can replay the events since the beginning of the recording, up to a  certain time. Then you've recreated the state of the application at that  time.

That's what [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) is about. It's like you can time travel to the past. I find it fascinating.

Event sourcing provides an audit trail when you need to meet  regulatory requirements. It can help with debugging. And you can even  explore alternate realities: what would have happened if...

I recently saw a [great talk](https://youtu.be/r7AGQsM7ncA) by [Jakub Pilimon](https://twitter.com/JakubPilimon) and [Kenny Bastani](https://twitter.com/kennybastani) about event sourcing.

The talk is a 1 hour session of life coding. The two speakers start with a simple application that is _not_ event sourced. Then they refactor it to use events.

They end up wiring the application up with Apache Kafka. I will skip  that part in this article and focus on the conceptual part of event  sourcing instead.

## A recap of the talk

As a user of a Credit Card management application, you can:

* Assign a limit to the credit card
* Withdraw money
* Repay money

For each of these commands, there is a method in the `CreditCard` class.  
Here's the original code of the `assignLimit` method:

```java
public void assignLimit(BigDecimal amount) { 
  if(limitAlreadyAssigned()) {  
    throw new IllegalStateException(); 
  }
  this.initialLimit = amount; 
}

```

Here's the `withdraw` method:

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

The `repay` method is similiar.

Remember that for event sourcing, you need to record an event   
any time the application changes its state?  
So the speakers extract each state change to its own method in the [CreditCard](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/model/CreditCard.java) class.

Here's the refactored `withdraw` method:

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

An instance of `CardWithdrawn` represents the event that a user has successfully withdrawn money. _After_ the state has changed, the event is added to the list of pending events.

You call the `save` method of the [CreditCardRepository](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/persistence/CreditCardRepository.java) class to flush the pending events to the event stream. Event listeners may handle the events then.

Apart from the payload, each event has its own unique identifier and timestamp. So you can sequence and replay the events later.  
To replay the events for a specific credit card, the repository calls the `recreateFrom` method of the [CreditCard](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/model/CreditCard.java) class, passing in the id of the card and the events stored for it:

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

This code uses the [vavr.io](http://www.vavr.io/) library to call the `handle` method for each event. The `handle` method dispatches the event object to the appropriate method.   
For example: for each `LimitAssigned` event, the `handle` method calls the `limitAssigned` method with the event as parameter.

## Simplifying the application

I used the [requirements as code](https://github.com/bertilmuth/requirementsascode) library for simplifying the code. First, I put all of the event classes and the handling methods in a model. Like this:

```java
this.eventHandlingModel = 
        Model.builder()
           .on(LimitAssigned.class).system(this::limitAssigned)
           .on(CardWithdrawn.class).system(this::cardWithdrawn)
           .on(CardRepaid.class).system(this::cardRepaid)
           .on(CycleClosed.class).system(this::cycleWasClosed)
       .build();

```

I had to change the return type of the handling methods (e.g. `limitAssigned`) to `void`. Apart from that, the conversion from [vavr.io](http://www.vavr.io/) was straight forward.

Then, I created a runner and started it for the model:

```java
this.modelRunner = new ModelRunner();
modelRunner.run(eventHandlingModel);

```

After that, I changed the `recreateFrom` and `handle` methods to this:

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

At that point, I could get rid of the dependency to [vavr.io](http://www.vavr.io/).   
Transition complete. Now I could get some more simplifying done.

I revisited the `withdraw` method:

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

The check `tooManyWithdrawalsInCycle()` didn't depend on the data of the event. It only depended on the state of the `CreditCard`.  
State checks like this can be represented in the model as `conditions`.

After I moved all state checks for all methods to the model, it looked like this:

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

For this to work, I needed to replace the direct calls to methods that change the state with the `handle` method. After that, the `assignLimit` and `withdraw` methods looked like this:

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

As you can see, most of the conditional logic has moved out of the  methods into the model. This makes the methods easier to understand.

One thing that bothered me is that you must not forget to add the  event to the pending events. Every time. Or your code won't work.

[Requirements as code](https://github.com/bertilmuth/requirementsascode) allows you to control how the system handles the events. So I extracted `pendingEvents.add(event)` from the methods as well:

```java
modelRunner.handleWith(this::addingPendingEvents);
...

public void addingPendingEvents(StepToBeRun stepToBeRun) {
    stepToBeRun.run();
    DomainEvent domainEvent = (DomainEvent) stepToBeRun.getEvent().get();
    pendingEvents.add(domainEvent);
}

```

I could have gone further and extract the validation logic as well.   
But I leave that as a thought exercise to you, dear reader.

## What's the point?

What I tried to achieve is a clear separation of concerns:

* The state dependent execution of methods is defined in the model
* The data validation and state changes are in the implementations of the methods
* The events are automatically added to the pending events. In  general: the infrastructure code is clearly separated from the business  logic.

Simplifying an example that is already very simple is good for explaining.  
But that's not the point I want to make.

The point is: having such a clear separation of concerns pays out in practice.   
Especially, if you work with multiple teams. On complicated problems.

Separation of concerns helps with changing different parts of code at  a different pace. You have simple rules where to find something. The  code is easier to understand. And it's easier to isolate units for  testing purposes.

## Conclusion

I hope you enjoyed my article. Please give me feedback.

Have you been working on event sourcing applications?   
What were your experiences like?   
Can you relate to what I wrote in this article?

I also want to invite you to look at [my library](https://github.com/bertilmuth/requirementsascode) that I used throughout the article. I would be thrilled if you try it out in practice, and tell me what you think.

_This article was first published on [dev.to](https://dev.to/bertilmuth/simplifying-an-event-sourced-application-1klp)_


