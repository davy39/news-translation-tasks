---
title: Demystify Dependency Injection and see it in action with this quick intro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T17:42:44.000Z'
originalURL: https://freecodecamp.org/news/demystifying-dependency-injection-49d4b6fe6536
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hnStARpFrN-7liCbeUKXRw.jpeg
tags:
- name: dependency injection
  slug: dependency-injection
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sankalp Bhatia

  Dependency Injection (DI) is a topic which I found a little difficult to grasp during
  my initial days as a software developer. I just could not find a good definition
  of the term.

  In this article, I’ve tried to put my understandings...'
---

By Sankalp Bhatia

Dependency Injection (DI) is a topic which I found a little difficult to grasp during my initial days as a software developer. I just could not find a good definition of the term.

In this article, I’ve tried to put my understandings of it in fairly simple language. It is intended for people starting out with DI, or those who just want to get a little more insight.

### **What is Dependency Injection?**

First things first: what is it? Dependency Injection, like so much other software development jargon, is a fancy term for a rather simple concept.

The definition which I found most useful is:

**_Dependency injection means giving an object its instance variables._**

That’s it. Providing (injecting) dependencies for a class. Simple right? Indeed.

Now, there are three ways of providing a class its dependencies in Java. All of them achieve…(coughs) Dependency Injection.

They are:

* Constructors
* Setters
* Directly setting public fields

### Let’s see Dependency Injection in action

I have an application class named MyMessagePublisher which has a dependency on a certain EmailService class.

#### **Dependency Injection using Constructor:**

```
public class MyMessagePublisher {    private EmailService emailService = null;        public MyMessagePublisher(EmailService emailService){        this.emailService = emailService;    }}
```

See what the constructor is doing there? It is telling MyMessagePublisher to use the EmailService provided by it. The class instantiating MyMessagePublisher should provide (inject) an EmailService instance (using the constructor) to be used by MyMessagePublisher. Something like this:

```
EmailService emailService = new EmailService();MyMessagePublisher myMessagePublisher =                            new MyMessagePublisher(emailService);
```

Good job, Constructor!

#### **Dependency Injection using Setter:**

```
public class MyMessagePublisher {    private EmailService emailService = null;    public MyMessagePublisher() {    }    public setEmailService(EmailService emailService) {        this.emailService = emailService;    }}
```

What’s going on here? The class using MyMessagePublisher can now set the EmailService which they want to use. Something like this:

```
MyMessagePublisher myMessagePublisher = new MyMessagePublisher();myMessagePublisher.setEmailService(new EmailService());
```

Good job, Setter!

#### **Dependency Injection by directly setting public fields**

Never do this!! If you have reached this far reading this article, I believe you know that this approach is evil.

### **Benefits of Dependency Injection**

I’ll start this section by explaining what we miss out on if we do not use DI.

Consider this code. I have defined the EmailService and MyMessagePublisher classes. MyMessagePublisher itself instantiates an EmailService object instead of using the DI techniques mentioned above.

```
public class EmailService {        public void sendEmail(String message, String receiver){        System.out.println("Email sent to " + receiver);    }}
```

```
public class MyMessagePublisher {    private EmailService emailService = new EmailService();    public void processMessages(String message, String receiver){        this.emailService.sendEmail(message, receiver);    }}
```

The above code has some limitations:

1. If EmailService initialization logic changes (it takes a constructor parameter to initialize), we would need to make changes to MyMessagePublisher class along with everywhere else in the codebase where we are using EmailService without DI.
2. It has tight coupling. Let’s say we want to move away from sending emails and instead start sending SMSs. We will then have to write a new publisher class.
3. This code is not testable. We will be sending emails to everyone while unit testing MyMessagePublisher class.

This is the solution I propose:

```
public class EmailService implements MessageService {    @Override    public void sendMessage(String message, String receiver) {        //logic to send email    }}
```

```
public class SMSService implements MessageService {    @Override    public void sendMessage(String message, String receiver) {        //logic to send SMS    }
```

```
public interface MessageService {    void sendMessage(String message, String receiver);}
```

```
public class MyMessagePublisher {    private MessageService messageService;        public MyMessagePublisher(MessageService messageService){        this.messageService = messageService;    }        @Override    public void processMessages(String msg, String rec){        this.service.sendMessage(msg, rec);    }}
```

This implementation overcomes all three limitations mentioned above.

* EmailService (or MessageService) initialization logic moves to the module initializing MyMessagePublisher
* We can move to a different implementation of MessageService which sends SMS without changing code in MyMessagePublisher
* The code is testable. We can use a dummy implementation of MessageService while unit testing MyMessagePublisher

Sweet. We have achieved DI using Constructors of our classes. Easy right? But there are some shortcomings here as well.

### Issues with Vanilla Dependency Injection

When does this become a problem? **When the code grows**.

So what are the alternatives? **Dependency Injection Containers** (Spring, Guice, Dagger, and so on).

Let’s try to answer the questions above in more detail.

Consider the code below. We are designing an AllInOneApp which offers multiple services like booking movie tickets, recharging prepaid connections, transferring money, and online shopping.

```
public class BookingService {    private SlotsManager slotsManager;    private MyMessagePublisher myMessagePublisher; //Looks familiar?}
```

```
public class AllInOneApp  {    BookingService bookingService; // Class above    RechargeService rechargeService;    MoneyTransferService moneyTransferService;    ShoppingService shoppingService;}
```

AllInOneApp needs four dependencies to be initialized. Let’s use vanilla Dependency Injection using Constructor here and instantiate the AllInOneApp class.

```
public static void main(String[] args) {
```

```
AllInOneApp allInOneApp = new AllInOneApp(                new BookingService(new SlotsManager(),                                   new MyMessagePublisher(                                              new EmailService())),                 new RechargeService(...),                 new MoneyTransferService(..),                new ShoppingService(...));
```

```
}
```

This looks messy. Can we identify the problems here? A couple of them are:

* The class initializing AllInOneApp needs to know the logic to construct all the dependency classes as well. This is cumbersome when writing code in any decent sized project. Managing all these instances by ourselves is not what we want to do while writing business specific code.
* Although I have seen people prefer this kind of DI, I personally believe this code is less readable as compared to this:

```
AllInOneApp myApp = SomeDIContainer.getInstance(AllInOneApp.class);
```

If all the components use DI, somewhere in the system some class or factory must know what to inject into all these components (AllInOneApp, BookingService, MessageService etc).

**This is where Dependency Injection containers come into picture**. It is called a container and not a factory because the container often takes on more responsibility than just instantiating objects and injecting dependencies.

DI containers let us define what components are to be initiated and what dependencies to be injected in those components. We can also configure other instantiation features, like the object being a singleton or getting created every time it is requested.

I will be writing another article explaining the usage of one of the popularly used DI Containers, Google Guice, which will have a hands on practice section as well. I will update this story with it’s link soon. I will now leave you with this [user guide](https://github.com/google/guice/wiki/GettingStarted) which is a good place to start.

Thank you for reading :)

