---
title: A hands-on session with Google Guice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T16:50:05.000Z'
originalURL: https://freecodecamp.org/news/a-hands-on-session-with-google-guice-5f25ce588774
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TUa3fApD5vZpVB7-d7mTaw.jpeg
tags:
- name: dependency injection
  slug: dependency-injection
- name: Google
  slug: google
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sankalp Bhatia

  A few months ago, I wrote an article explaining dependency injection. I had mentioned
  of a follow-up article with a hands-on session of Google Guice. While I am disappointed
  in being so late in writing this, part of me is happy that...'
---

By Sankalp Bhatia

A few months ago, I wrote [an article](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536) explaining dependency injection. I had mentioned of a follow-up article with a hands-on session of Google Guice. While I am disappointed in being so late in writing this, part of me is happy that I was able to write a second article.

This article assumes that you are familiar with what dependency injection is. I would recommend you to glance through [my previous article](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536) as we will be building upon the examples we used there. If you are hearing the term for the first time, it will be worth it. If you are familiar with it, reading it won’t take much time :)

If you haven’t worked much with Guice, please check it out on GitHub [here](https://github.com/google/guice).

We will need to set up a few things before we start

1. **JDK**: We will be using Java for this task. So you will need to have a working JDK to be able to run Java code in your computer. To check if it’s already installed, run ‘java -version’ on the command line. If the version is 1.6 or greater, we are good. Just a note: I don’t think it would make much sense to attempt this if you don’t have experience with Java_._
2. **Maven**: We will be using maven as a build tool. To install maven, follow the instructions here [https://maven.apache.org/install.html](https://maven.apache.org/install.html) (Quite easy). To check if you already have maven, run ‘mvn -v’ on the command line.
3. **git** (optional): [https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
4. **clone the hands on repository (FreshGuice)**: Run commands mentioned below

```
cd folder/to/clone-into/ git clone https://github.com/sankalpbhatia/FreshGuice.git
```

### Bindings and Binding Annotations

We are ready now. Let me start by introducing two crucial terms in the Guice framework: **Bindings and Binding Annotations.**

**Bindings:** being the core concept of Guice, in literal terms, means an agreement or promise involving an obligation that cannot be broken. Now let’s map it in the context of Dependency Injection. When we make Guice _bind_ an instance with a class, we make an agreement with Guice that “When I ask for an instance of X.java, give me this instance”. And this agreement can’t be broken.

**Binding Annotations:** Occasionally you’ll want multiple bindings for the same type. The annotation and (class) type together uniquely identify a binding. For example, in some cases, you might need two separate instances of the same class/ implementation of the same interface. To identify those, we use binding annotations. We will see some examples when we explain bindings.

#### **How to create bindings**

The user guide section of Guice explains it perfectly. So I will just be copying it here:

> To create bindings, extend `AbstractModule` and override its `configure` method. In the method body, call `bind()` to specify each binding. These methods are type checked so the compiler can report errors if you use the wrong types. Once you've created your modules, pass them as arguments to `Guice.createInjector()` to build an injector.

There are a number of types of bindings: Linked, Instance, @Provides annotation, Provider bindings, Constructor bindings, and Un-targeted bindings.

For this article, I will only be covering Linked Bindings, Instance Bindings, @Provides annotation, and a special annotation @Inject. I very rarely use any other means to bind, but more information can be found at [https://github.com/google/guice/wiki/Bindings](https://github.com/google/guice/wiki/Bindings).

1. **Linked Binding:** a Linked binding maps a type/interface to its implementation. This example maps the interface MessageService to its implementation EmailService.

In plain terms: When I ask Guice to give me an instance of MessageService, it will give me an instance of EmailService.

_But, how will it know to create an instance of EmailService_? We’ll see that later.

```
public class MessagingModule extends AbstractModule {  @Override   protected void configure() {    bind(MessageService.class).to(EmailService.class);  }}
```

Maybe we want more than one instance of MessageService in our project. At some places, we would want a SMSService to be associated with a MessageService, rather than an EmailService. In such cases, we use a binding annotation. To create a binding annotation, you will have to create two annotations like so:

```
@BindingAnnotation @Target({ FIELD, PARAMETER, METHOD }) @Retention(RUNTIME)public @interface Email {}
```

```
@BindingAnnotation @Target({ FIELD, PARAMETER, METHOD }) @Retention(RUNTIME)public @interface SMS {}
```

You need not know about the metadata annotations (@Target, @ Retention). If interested, please read this: [https://github.com/google/guice/wiki/BindingAnnotations](https://github.com/google/guice/wiki/BindingAnnotations)

Once we have the annotations with us, we can create two separate bindings which instruct Guice to create different instances of MessageService based on the BindingAnnotation (I think of it as a qualifier).

```
public class MessagingModule extends AbstractModule {  @Override   protected void configure() {   bind(MessageService.class).annotatedWith(Email.class)                             .to(EmailService.class);
```

```
   bind(MessageService.class).annotatedWith(SMS.class)                             .to(SMSService.class);  }}
```

2. **Instance Binding:** Binds a type to a specific instance

```
 bind(Integer.class) .annotatedWith(Names.named(“login timeout seconds”)) .toInstance(10);
```

One should avoid using .toInstance with objects that are complicated to create, since it can slow down application startup. You can use an @Provides method instead. In fact, you can even forget that we mentioned anything about Instance binding right now.

3. **@ Provides annotation**:

This is straight from Guice’s wiki, as it is fairly simple:

> When you need code to create an object, use an `@Provides` method. The method must be defined within a module, and it must have an `@Provides` annotation. The method's return type is the bound type. Whenever the injector needs an instance of that type, it will invoke the method.

```
bind(MessageService.class)
```

```
.annotatedWith(Email.class)
```

```
.to(EmailService.class);
```

is same as

```
@Provides@Emailpublic MessageService provideMessageService() {  return new EmailService();}
```

where Email.java is a Binding annotation.

Dependencies can be passed to a method with this annotation which makes it extremely useful in real life projects. For example, for the code mentioned below, the injector will exercise the binding for the string parameter **_apiKey_** before invoking the method.

```
@Provides @PayPalCreditCardProcessor providePayPalCreditCardProcessor(      @Named("PayPal API key") String apiKey) {  PayPalCCProcessor processor = new PaypalCCProcessor();  processor.setApiKey(apiKey);  return processor;  }
```

4. **@ Inject annotation** (Just in Time binding): Whatever we covered up until now are called _explicit bindings._ If Guice, when trying to create an instance, does not find an explicit binding, it tries to create one using a Just-in-time binding.

Guice can create these bindings by using the class’s _injectable constructor_. This is either a non-private, no-arguments constructor or a constructor with the `@Inject`annotation.

### Task

Now let’s move to the project we cloned from Github.

Like the examples in the [previous article](https://medium.freecodecamp.org/demystifying-dependency-injection-49d4b6fe6536), this maven project implements a BillingService which charges a PizzaOrder using a credit card and generates a Receipt.

The project structure is as follows:

**Interfaces**

* BillingService — charges an order using a credit card
* CreditCardProcessor — debits some amount from a credit card
* TransactionLog — logs results

**Classes**

src

* CreditCard — entity representing a Credit Card
* PizzaOrder — entity representing a Pizza order
* Receipt — entity representing a receipt
* RealBillingService implements BillingService
* PaypalCreditCardProcessor implements CreditCardProcessor
* BankCreditCardProcessor implements CreditCardProcessor
* InMemoryTransactionLog implements TransactionLog
* GuiceTest — Main class which uses BillingService
* BillingModule — All Guice bindings go here
* GuiceInjectionTest : Unit tests to check binding constraints

The task here is to create Guice Bindings in the BillingModule such that the following constraints are satisfied:

1. All implementations of BillingService should be bound to RealBillingService.
2. CreditCardProcessor interface annotated with @Paypal should be bound to PaypalCreditCardProcessor class.
3. CreditCardProcessor interface named with string “Bank” should be bound to BankCreditCardProcessor class.
4. BillingService instances returned by injector should have an instance of BankCreditCardProcessor as their dependency.
5. All implementations of TransactionLog should be bound to InMemoryTransactionLog.

All five unit tests in GuiceInjectionTests should pass if the above conditions are satisfied. You should also be able to run the main method in GuiceTest.

To test correctness:

1. run unit tests

```
mvn test
```

This should run the test file GuiceInjectionTests.java.

2. run the main file

```
mvn exec:java -Dexec.mainClass="GuiceTest"
```

This should execute the main class of the project, which does the end to end work of creating an order, processes payment using a credit card and generates a receipt.

You can comment if you have any questions and I will try answering them. Please note that there is no single correct answer for this exercise. DM me your solutions and I will add the answers to the repository. Or better still, send me a pull request :)

