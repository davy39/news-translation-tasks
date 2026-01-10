---
title: Kissing the state machine goodbye
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
seo_title: null
seo_desc: 'By Bertil Muth

  Recently, I have written about simplifying an event sourced application.

  The article starts with code from a talk by Jakub Pilimon and Kenny Bastani. And
  it ends with building a model  for events in the code: how they are applied, and
  ...'
---

By Bertil Muth

Recently, I have written about [simplifying an event sourced application](https://www.freecodecamp.org/news/simplifying-an-event-sourced-application/).

The article starts with [code](https://gitlab.com/pilloPl/eventsourced-credit-cards/blob/4329a0aac283067f1376b3802e13f5a561f18753/src/main/java/io/pillopl/eventsourcing/) from a [talk](https://youtu.be/r7AGQsM7ncA) by Jakub Pilimon and Kenny Bastani. And it ends with building a model  for events in the code: how they are applied, and under which  conditions.

The sample application is about Credit Card management. You can:

* **Assign a credit limit**. But only once, otherwise the application throws an `IllegalStateException`.
* **Withdraw money**. But you can't make more than 45 withdrawals in a certain cycle. Or you'll get an exception as well.
* **Repay money**

I played around with the `CreditCard` class. I had a feeling that something might be wrong with the `withdraw` method. So I wrote a test that checks for the correct behavior.

```java
@Test(expected = IllegalStateException.class)
public void withdrawWithoutLimitAssignedThrowsIllegalStateException() {
    CreditCard card = new CreditCard(UUID.randomUUID());
    card.withdraw(BigDecimal.ZERO);
}
```

The test attempts to withdraw an amount of zero. But no credit limit  has been assigned before. The application should reject this, and throw  an `IllegalStateException`.   
Instead, the application threw a `NullPointerException`.

The application assumed that the limit had been assigned before.  
Now: this is a sample application. If it covered all cases it probably wouldn't be as understandable as it is.

Let's pretend we're dealing with a real world application. What if  the required order of commands/events depends on a multitude of  conditions and states?

If you have ever tried to implement this with conditional statements  only, you probably know it's easy to lose the overview. But there is a  standard solution for managing complicated flows and changes in  behavior.

## State machine to the rescue

In computer science, state machines have been around for decades.  They are well understood in theory. They are battle proven in practice.  They are the de facto standard for dealing with state dependent  behavior.

So I decided to create a UML state machine model for the sample  application. I asked myself first: Do I want to deal with commands or  events in the state machine?

Commands are about something the application should do in the future.  
Events are about something that has happened in the past.

I wanted to _prevent_ withdrawals without a credit limit assigned.  
So the state machine model needed to deal with commands. 

The syntax of a transition in the diagram is `command[condition] / commandHandler()`. It means: when a command object has been received, and the condition is  fulfilled if present, handle the command and go to the next state.

![State machine](https://res.cloudinary.com/practicaldev/image/fetch/s--IsFVxafc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/3laq9tz8h82nwvjsmugv.png)

The model fixes what is allowed to happen, and what not. For example: repaying is only possible after withdrawing.

But that precision has a price. If you want the state machine model  to be executed and to control the behavior at runtime, you need to model  every possible transition from every state. Including its condition, if  there are two transitions with the same event.

That's why there is a lot more repetition in the state machine than in the original code with the `if` statements. A way to reduce the amount of repetition is to use _super states_ and _sub states_:

![State machine with sub states](https://res.cloudinary.com/practicaldev/image/fetch/s--CCZSYf5s--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2cwl67ddaa64l2szlp4s.png)

It is easy to define state dependent behavior in a state machine model. But a state independent rule like _in any state (when condition X holds), do Y_ leads to several transitions. For example, I needed to add `requestToCloseCycle` to every super state.

You need people with the right skills to create the models. And it's  not easy to communicate about the models with non-technical  stakeholders. It's not the way they normally speak about user journeys.

## Saying goodbye

It seems there are two options so far.

In the left corner: the `if` statement. Easy to start  with. Low overhead. Best fit for applications that have no complicated  flows of behavior. But it's easy to lose the overview when the behavior  gets complicated.

In the right corner: the executable state machine model. Powerful.  Proven. Precise. Gives you an overview of the behavior. But it's hard to  define state independent rules. And state machine models are difficult  to communicate about with non-technical stakeholders.

I stand in the third corner. I have found an alternative to state machines.   
A solution that

* enables you to define conditions. But you don't have to in most cases.
* makes state dependent and independent rules equally easy to specify.
* uses language that all stakeholders can relate to.

Before I dig into the details, here's the sample state machine model rewritten using that solution:

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

As you can see, the model is [in the code](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCardAggregateRoot.java).  A model runner executes this model. The runner reacts to commands/events, similar to a state machine.

The basic flow is the "happy day scenario". The steps of a user to  reach her goal. The other flows cover alternative and error scenarios.

A flow can define an _explicit condition_ for its first step to run - e.g. `after(...)`, `anytime()` or `condition()` in the sample.  
If a flow has an explicit condition, the flow starts when the condition  is fulfilled and the runner is currently in a different flow.  
If a flow has no explicit condition (e.g. the basic flow in the sample),  the first step runs after the runner has started, when no step has been  run so far.

Starting with the second step of a flow, each step has an _implicit condition_.  That condition is: run the step after the previous step in the same  flow, unless a different flow with an explicit condition can start.   
So in contrast to state machines, you don't need to specify the conditions after the first step.

Internally, state depending behavior is realized by checking a condition.   
Every step contains its complete condition that defines exactly when the step can run. That's how [requirements as code](https://github.com/bertilmuth/requirementsascode) can treat state dependent and independent behavior alike.

Have a look at [further examples](https://github.com/bertilmuth/requirementsascode/tree/master/requirementsascodeexamples/helloworld) to dig deeper.

## When to use requirements as code

Many applications have dynamic internal behavior. This is true for  distributed applications in particular. They need to deal with the fact  that "the other party" is not available.

But from a user's perspective, these applications look quite  predictable and regular. When I want to watch a show on Netflix or  Amazon Prime, I follow the exact same steps each time until I can watch  it. It looks like one step just follows the other.

That's the sweet spot for requirements as code, if used as an alternative to a state machine: defining the _visible behavior_ of an application.

## How the Credit Card application works now

* A [client](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/EventsourcingApplication.java) sends a command to the `CreditCardAggregateRoot`
* The [CreditCardAggregateRoot](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCardAggregateRoot.java) uses the event repository to replay all the events for the credit card, to restore it
* The `CreditCardAggregateRoot` uses the above model to dispatch the command to a command handling method
* The command handling method produces an event and applies it to the `CreditCard` instance.
* The event handling model of the [CreditCard](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodeexamples/creditcard_eventsourcing/src/main/java/creditcard_eventsourcing/model/CreditCard.java) instance dispatches the event to a state changing method

## Conclusion

I hope you enjoyed my article. I also want to invite you to look at [the library](https://github.com/bertilmuth/requirementsascode) that I used throughout the article. Try it out in practice, and let me know the result.

_If you want to keep up with what I'm doing or drop me a note, follow me on [LinkedIn](https://www.linkedin.com/in/bertilmuth/) or [Twitter](https://twitter.com/BertilMuth). To learn about agile software development, visit my [online course](https://skl.sh/2Cq497P)._  
_Last edited April 27, 2020: updated event sourcing process_


