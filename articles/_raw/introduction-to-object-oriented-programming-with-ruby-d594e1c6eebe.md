---
title: An introduction to Object-Oriented Programming with Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T22:49:30.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-object-oriented-programming-with-ruby-d594e1c6eebe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yk9cvq3T5pHUsObH3XiA1Q.png
tags:
- name: learning to code
  slug: learning-to-code
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Saul Costa

  Object-oriented programming (OOP) is a programming paradigm organized around objects.
  At a high level, OOP is all about being able to structure code so that its functionality
  can be shared throughout the application. If done properly, O...'
---

By Saul Costa

**Object-oriented programming** (**OOP**) is a programming paradigm organized around objects. At a high level, OOP is all about being able to structure code so that its functionality can be shared throughout the application. If done properly, OOP can lead to very elegantly written programs that have minimal code duplication.

This is opposed to procedural programming (PP), in which you build programs in sequential order and call methods when you want shared behavior between pages in the application. Common procedural programming languages include [C](https://en.wikipedia.org/wiki/C_(programming_language)) and [Go](https://en.wikipedia.org/wiki/Go_(programming_language)).

In this tutorial, you’ll learn the fundamental concepts of OOP for **Ruby**, an object-oriented programming language wherein everything is an object. We will be using Ruby since one of its defining attributes — in addition to its elegant syntax and readability — is how it implements OOP techniques. This makes it a great language to start learning OOP with.

We will cover:

* Creating classes
* Instantiating objects
* Initializing arguments
* Working with inheritance, and
* Private and public methods.

In learning these concepts, we will build out our own application: an API connector that communicates dynamically with an application that sends a text message. This will include walking through how to leverage concepts such as inheritance and object instantiation to make our code more scalable and reusable!

_This brief tutorial is adapted from Next Tech’s [Introduction to Ruby course](https://c.next.tech/2EyLhYk), which includes an in-browser sandboxed environment and auto-checked interactive tasks to complete._

_You can follow along with the code snippets in this tutorial using Next Tech’s sandbox which already has Ruby pre-installed. If you chose to use your own IDE, make sure Ruby is installed by following the instructions on the [installation page](https://www.ruby-lang.org/en/documentation/installation/)._

### Creating Classes

Before we begin, let’s define what an **object** is. At its core, an object is a self-contained piece of code that contains data (“attributes”) and behavior (“methods”) and can communicate with other objects. Objects of the same type are created from **classes**, which act as blueprints that define properties and behavior.

Creating a class in Ruby is fairly easy. To define a class, simply type the `class` word followed by the name of the class, and end it with the `end` word. Anything contained between `class` and `end` belongs to this class.

Class names in Ruby have a very specific style requirement. They need to start with a letter and if they represent multiple words, each new word needs also to be an uppercase letter — i.e. “CamelCase”.

We’ll start by creating a class called `ApiConnector`:

Classes in Ruby can store both data and methods. In many traditional OOP languages such as Java, you need to create two methods for each data element you want to be included in the class. One method, the **setter**, sets the value in the class. The other method, the **getter**, allows you to retrieve the value.

The process of creating setter and getter methods for every data attribute can be tiresome and leads to incredibly long class definitions. Thankfully Ruby has a set of tools called **attribute accessors**.

Let’s implement some setters and getters for some new data elements for our class. Since it’s an API connector, it would make sense to have data elements such as `title`, `description`, and `url`. We can add these elements with the following code:

When you merely create a class, it doesn’t do anything — it is simply a definition. In order to work with the class, we need to create an instance of it…we’ll cover that next!

### Instantiation

To understand what **instantiation** is, let’s consider a real-world analogy. Let’s imagine that you’re building a house. The first task is to build a blueprint for the house. This blueprint would contain attributes and features of the house, such as the dimensions for each room, how the plumbing will flow, and so on.

Is the blueprint of the house the actual house? Of course not, it simply lists out the attributes and design elements for how the home will be created. So after the blueprint is completed, the actual home can be built — or, “instantiated”.

As explained in the previous section, in OOP, a class is the blueprint for an object. It simply describes what an object will look like and how it will behave. Therefore, instantiation is the process of taking a class definition and creating an object that you can use in a program.

Let’s create a new instance of our `ApiConnector` class and store it in a variable called `api`:

Now that we have an object created, we can use the `api` variable to work with the class attributes. For example, we can run the code:

```
[Out:]https://next.tech
```

In addition to creating attributes, you can also create methods within a class:

To access this method, we can use the same syntax that we utilized with the attribute accessors:

Putting this all together, running the full class code below will result in the `url` and the `test_method` message to be printed:

```
[Out:]"https://next.tech""testing class call"
```

### Initializer Method

One thing you may find handy in Ruby development is the ability to create an **initializer** method. This is simply a method called `initialize` that will run every time when you create an instance of your class. In this method, you can give values to your variables, call other methods, and do just about anything that you think should happen when a new instance of that class is created.

Let’s update our `ApiConnector` to utilize an initializer method:

Within the `initialize` method, we created an instance variable for each of the parameters so that we can use these variables in other parts of the application as well.

We also removed the `attr_accessor` method since the new `initialize` method will take care of this for us. If you need the ability to call the data elements outside of the class, then you would still need to have the `attr_accessor` call in place.

To test if the `initialize` method is working, let’s create another method within the class that prints these values out:

Finally, we’ll instantiate the class and test the initialize method:

```
[Out:]"My title""My cool description""https://next.tech"
```

#### Working with optional values

Now, what happens when we want to make one of these values optional? For example, what if we want to give a default value to the URL? To do that, we can update our `initialize` method with the following syntax:

Now our program will have the same output even if we don’t pass the `url` value while creating a new instance of the class:

#### Using named arguments

Though this looks simple, passing arguments can get complex in real-world Ruby applications because some methods may take a large number of arguments. In such cases, it becomes difficult to know the order of arguments and what values to assign to them.

To avoid this confusion, you can utilize named arguments, like this:

You can enter the arguments without having to look at the order in the `initialize` method, and even change the order of the arguments without causing an error:

#### Overriding default values

What happens if we want to override a default value? We simply update our instantiation call like this:

This update will override our default value of `https://next.tech`, and calling `api.testing_initializer` will now print `https://next.xyz` as the URL.

### Inheritance

Now, we are going to learn about an important object-oriented principle called **inheritance**. Before going into how it is executed in Ruby, let’s see why it’s important for building applications.

To start with, inheritance means your classes can have a hierarchy. It is best used when different classes have some shared responsibilities, since it would be a poor practice to duplicate code in each class for identical or even similar behavior.

Take our `ApiConnector` class. Let's say we have different API classes for various platforms, but each class shares a number of common data or processes. Instead of duplicating code in each of the API connector classes, we can have one **parent class** with the shared data and methods. From there, we can create **child classes** from this parent class. With the way that inheritance works, each of the child classes will have access to the components provided from the parent class.

For example, say we have three APIs: `SmsConnector`, `PhoneConnector`, and `MailerConnector`. If we wrote code individually for each of these classes, it would look like this:

As you can see, we are simply repeating the same code across different classes. This is considered a poor programming practice that violates the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don’t Repeat Yourself) principle of development. Instead, we can make an `ApiConnector` parent class, and each of the other classes can inherit the common functionality from this class:

By leveraging inheritance, we were able to cut all of the duplicate code throughout our classes.

The syntax for using inheritance is to define the child class name, followed by the `&`lt; symbol, then the parent class name — i.e. o`ur SmsConnec`to`r, MailerConnec`tor, a`nd PhoneConnec`tor classes inherit from t`he ApiConnec`tor class .

Each of these child classes now has access to the full set of elements provided in the parent `ApiConnector` class. For example, if we create a new instance of `SmsConnector` with the following parameters, we can call the `send_sms` method:

```
[Out:]Sending SMS message with the title 'Hi there!' and description 'I'm an SMS message'.
```

A rule of thumb in OOP is to ensure that a class performs a single responsibility. For example, the `ApiConnector` class should not send SMS messages, make phone calls, or send emails since that would be three core responsibilities.

### Private and Public Methods

Before we dive into private and public methods, let’s first go back to our original `ApiConnector` class and create a `SmsConnector` class that inherits from `ApiConnector`. In this class, we will create a method called `send_sms` that will run a script that contacts an API:

This method will send a `title` and `url` to an API, which will in turn send an SMS message. Now we can instantiate the `SmsConnector` class and call the `send_sms` message:

Running this code will contact the SMS API and send the message. You can go to the bottom of [this page](http://edutechional-smsy.herokuapp.com/notifications) to see your message!

Now, using this example, let’s discuss the types of methods provided by classes.

The `send_sms` method is a **public method**. This means that anyone working on our class can communicate with this method. This may not seem like a big deal if you are working on an application that no one else is working on. However, if you build an API or code library that is open sourced for others to use, it's vital that your public methods represent elements of functionality that you actually want other developers to use.

Public methods should rarely, if ever, be altered. This is because other developers may be relying on your public methods to be consistent, and a change to a public method may break components of their programs.

So, if you can’t change public methods, how can you work on a production application? That’s where **private methods** come in. A private method is a method that is only accessed by the class that it is contained in. It should never be called by outside services. This means that you can alter their behavior, assuming that these changes don’t have a domino effect and alter the public methods that they may be called from.

Usually private methods are placed at the end of the file after all the public methods. To designate private methods, we use the `private` word above the list of methods. Let’s add a private method to our `ApiConnector` class:

Notice how we’re calling this method from the inside of the `initialize` method of the `ApiConnector` class? If we run this code, it will give the following output:

```
[Out:]A secret message from the parent class
```

Now child classes have access to methods in the parent class, right? Well, not always. Let’s remove the `secret_method` method from the `initialize` method in `ApiConnector` and try to call it from our `SmsConnector` child class, as shown here:

```
[Out:]Traceback (most recent call last):main.rb:29:in `<main>': private method `secret_method' called for #SmsConnector:0x000056188cfe19b0> (NoMethodError)
```

This is because the `SmsConnector` class only has access to the public methods from the parent class. The private methods are, by their nature, private. This means that they can only be accessed by the class that they are defined in.

So a good rule of thumb is to create private methods when they should not be used outside the class and public methods when they have to be available throughout the application or used by outside services.

#### Wrapping up

I hope you enjoyed this quick tutorial on the fundamental concepts of object-oriented programming in Ruby! We covered creating classes, attribute accessors, instantiation, initialization, inheritance, and private and public methods.

Ruby is a powerful object-oriented language used by popular applications, including our own here at Next Tech. With this foundational knowledge of OOP, you’re well on your way to developing your own Ruby apps!

_If you’re interested in learning more about programming with Ruby, check out our Introduction to Ruby course [here](https://c.next.tech/2EyLhYk)! In this course we cover core programming skills, such as variables, strings, loops, and conditionals, more advanced OOP topics, and error handling._

