---
title: An Introduction to Object-Oriented Programming with Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T03:29:08.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-object-oriented-programming-with-ruby-73531e2b8ddc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YCQfbNxV9hutPmznUcRA4Q.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nishant Mishra

  As a computer science student, I spend a lot of time learning and playing with new
  languages. Every new language has something unique to offer. Having said that, most
  beginners start off their programming journey with either procedu...'
---

By Nishant Mishra

As a computer science student, I spend a lot of time learning and playing with new languages. Every new language has something unique to offer. Having said that, most beginners start off their programming journey with either procedural languages like C or with object-oriented languages like JavaScript and C++.

Therefore, it makes sense to go through the basics of object-oriented programming so you can understand the concepts and apply them to the languages you learn easily. We’ll be using the Ruby programming language as an example.

You may be asking, why Ruby? Because it is “designed to make programmers happy” and also because almost everything in Ruby is an object.

### Getting a sense of the Object-Oriented Paradigm (OOP)

In OOP, we identify the “things” that our program handles. As humans, we think about things as objects with attributes and behaviors, and we interact with things based on these attributes and behaviors. A thing can be a car, a book, and so on. Such things become classes (the blueprints of objects), and we create objects out of these classes.

Each instance (object) contains instance variables which are the state of the object (attributes). Object behaviors are represented by methods.

Let’s take the example of a car. A car is a thing which would make it a **class**. A specific type of car, say BMW is an **object** of the class Car_._ The **attributes/properties** of a BMW such as the color and model number can be stored in instance variables. And if you want to perform an operation of the object, such as driving, then “drive” describes a behavior which is defined as a **method**.

### A Quick Syntax Lesson

* To end a line in a Ruby program, a semicolon(;) is optional (but is generally not used)
* 2-space indentation for each nested level is encouraged (not required, like it is in Python)
* No curly braces `{}` are used, and the **end** keyword is used to mark the end of a flow control block
* To comment, we use the `#` symbol

The way objects are created in Ruby is by calling a **new** method on a class, as in the example below:

```
class Car  def initialize(name, color)    @name = name    @color = color  end
```

```
  def get_info    "Name: #{@name}, and Color: #{@color}"  endend
```

```
my_car = Car.new("Fiat", "Red")puts my_car.get_info
```

To understand what’s going on in the code above:

* We have a class named `Car` with two methods, `initialize` and `get_info`.
* Instance variables in Ruby begin with `@` (For example `@name`). The interesting part is that the variables are not initially declared. They spring into existence when first used, and after that they are available to all instance methods of the class.
* Calling the `new` method causes the `initialize` method to invoke. `initialize` is a special method which is used as a constructor.

#### Accessing Data

Instance variables are private and can’t be accessed from outside the class. In order to access them, we need to create methods. Instance methods have public access by default. We can limit the access to these instance methods as we will see later in this article.

In order to get and modify the data, we need “getter” and “setter” methods, respectively. Let’s look at these methods taking the same example of a car.

```
class Car  def initialize(name, color) # "Constructor"    @name = name    @color = color  end
```

```
  def color    @color  end
```

```
  def color= (new_color)    @color = new_color  endend
```

```
my_car = Car.new("Fiat", "Red")puts my_car.color # Red
```

```
my_car.color = "White"puts my_car.color # White
```

In Ruby, the “getter” and the “setter” are defined with the same name as the instance variable that we are dealing with.

In the example above, when we say `my_car.color`, it actually calls the `color` method which in turn returns the name of the color.

_Note: Pay attention to how Ruby allows a space between the_ `color` _and **equals to sign** while using the setter, even though the method name is_ `color=`

Writing these getter/setter methods allow us to have more control. But most of the time, getting the existing value and setting a new value is simple. So, there should be an easier way instead of actually defining getter/setter methods.

#### The easier way

By using the `attr_*` form instead, we can get the existing value and set a new value.

* `attr_accessor`: for getter and setter both
* `attr_reader`: for getter only
* `attr_writer`: for setter only

Let’s look at this form taking the same example of a car.

```
class Car  attr_accessor :name, :colorend
```

```
car1 = Car.newputs car1.name # => nil
```

```
car1.name = "Suzuki"car1.color = "Gray"puts car1.color # =&gt; Gray
```

```
car1.name = "Fiat"puts car1.name # =&gt; Fiat
```

This way we can skip the getter/setter definitions altogether.

#### Talking about best practices

In the example above, we didn’t initialize the values for the `@name` and `@color` instance variables, which is not a good practice. Also, as the instance variables are set to nil, the object `car1` doesn’t make any sense. It’s always a good practice to set instance variables using a constructor as in the example below.

```
class Car  attr_accessor :name, :color    def initialize(name, color)    @name = name    @color = color  endend
```

```
car1 = Car.new("Suzuki", "Gray")puts car1.color # =&gt; Gray
```

```
car1.name = "Fiat"puts car1.name # =&gt; Fiat
```

### Class Methods and Class Variables

So class methods are invoked on a class, not on an instance of a class. These are similar to **static** methods in Java.

_Note: `self` outside of the method definition refers to the class object. Class variables begin with `@@`_

Now, there are actually three ways to define class methods in Ruby:

#### Inside the class definition

1. Using the keyword self with the name of the method:

```
class MathFunctions  def self.two_times(num)    num * 2  endend
```

```
# No instance createdputs MathFunctions.two_times(10) # =&gt; 20
```

2. Using `<<`; self

```
class MathFunctions  class << self    def two_times(num)      num * 2    end  endend
```

```
# No instance createdputs MathFunctions.two_times(10) # =&gt; 20
```

#### Outside the class definition

3. Using class name with the method name

```
class MathFunctionsend
```

```
def MathFunctions.two_times(num)  num * 2end
```

```
# No instance createdputs MathFunctions.two_times(10) # =&gt; 20
```

### Class Inheritance

In Ruby, every class implicitly inherits from the Object class. Let’s look at an example.

```
class Car  def to_s    "Car"  end
```

```
  def speed    "Top speed 100"  endend
```

```
class SuperCar < Car  def speed # Override    "Top speed 200"  endend
```

```
car = Car.newfast_car = SuperCar.new
```

```
puts "#{car}1 #{car.speed}" # =&gt; Car1 Top speed 100puts "#{fast_car}2 #{fast_car.speed}" # => Car2 Top speed 200
```

In the above example, the `SuperCar` class overrides the `speed` method which is inherited from the `Car` class. The symbol `&`lt; denotes inheritance.

_Note: Ruby doesn’t support multiple inheritance, and so mix-ins are used instead. We will discuss them later in this article._

### Modules in Ruby

A Ruby module is an important part of the Ruby programming language. It’s a major object-oriented feature of the language and supports multiple inheritance indirectly.

A module is a container for classes, methods, constants, or even other modules. Like a class, a module cannot be instantiated, but serves two main purposes:

* Namespace
* Mix-in

#### Modules as Namespace

A lot of languages like Java have the idea of the package structure, just to avoid collision between two classes. Let’s look into an example to understand how it works.

```
module Patterns  class Match    attr_accessor :matched  endend
```

```
module Sports  class Match    attr_accessor :score  endend
```

```
match1 = Patterns::Match.newmatch1.matched = "true"
```

```
match2 = Sports::Match.newmatch2.score = 210
```

In the example above, as we have two classes named `Match`, we can differentiate between them and prevent collision by simply encapsulating them into different modules.

#### Modules as Mix-in

In the object-oriented paradigm, we have the concept of Interfaces. Mix-in provides a way to share code between multiple classes. Not only that, we can also include the built-in modules like `Enumerable` and make our task much easier. Let’s see an example.

```
module PrintName  attr_accessor :name  def print_it    puts "Name: #{@name}"  endend
```

```
class Person  include PrintNameend
```

```
class Organization  include PrintNameend
```

```
person = Person.newperson.name = "Nishant"puts person.print_it # =&gt; Name: Nishant
```

```
organization = Organization.neworganization.name = "freeCodeCamp"puts organization.print_it # =&gt; Name: freeCodeCamp 
```

Mix-ins are extremely powerful, as we only write the code once and can then include them anywhere as required.

### Scope in Ruby

We will see how scope works for:

* variables
* constants
* blocks

#### Scope of variables

Methods and classes define a new scope for variables, and outer scope variables are not carried over to the inner scope. Let’s see what this means.

```
name = "Nishant"
```

```
class MyClass  def my_fun    name = "John"    puts name # =&gt; John  end
```

```
puts name # =&gt; Nishant
```

The outer `name` variable and the inner `name` variable are not the same. The outer `name` variable doesn’t get carried over to the inner scope. That means if you try to print it in the inner scope without again defining it, an exception would be thrown — **no such variable exists**

#### Scope of constants

An inner scope can see constants defined in the outer scope and can also override the outer constants. But it’s important to remember that even after overriding the constant value in the inner scope, the value in the outer scope remains unchanged. Let’s see it in action.

```
module MyModule  PI = 3.14  class MyClass    def value_of_pi      puts PI # =&gt; 3.14      PI = "3.144444"      puts PI # => 3.144444    end  end  puts PI # =&gt; 3.14end
```

#### Scope of blocks

Blocks inherit the outer scope. Let’s understand it using a fantastic example I found on the internet.

```
class BankAccount  attr_accessor :id, :amount  def initialize(id, amount)    @id = id    @amount = amount  endend
```

```
acct1 = BankAccount.new(213, 300)acct2 = BankAccount.new(22, 100)acct3 = BankAccount.new(222, 500)
```

```
accts = [acct1, acct2, acct3]
```

```
total_sum = 0accts.each do |eachAcct|  total_sum = total_sum + eachAcct.amountend
```

```
puts total_sum # =&gt; 900
```

In the above example, if we use a method to calculate the `total_sum`, the `total_sum` variable would be a totally different variable inside the method. That’s why sometimes using blocks can save us a lot of time.

Having said that, a variable created inside the block is only available to the block.

### Access Control

When designing a class, it is important to think about how much of it you’ll be exposing to the world. This is known as **Encapsulation,** and typically means hiding the internal representation of the object.

There are three levels of access control in Ruby:

* **Public** - no access control is enforced. Anybody can call these methods.
* **Protected** - can be invoked by objects of the defining classes or its sub classes.
* **Private** - cannot be invoked except with an explicit receiver.

Let’s see an example of Encapsulation in action:

```
class Car  def initialize(speed, fuel_eco)    @rating = speed * comfort  end
```

```
  def rating    @rating  endend
```

```
puts Car.new(100, 5).rating # =&gt; 500
```

Now, as the details of how the rating is calculated are kept inside the class, we can change it at any point in time without any other change. Also, we cannot set the rating from outside.

Talking about the ways to specify access control, there are two of them:

1. Specifying public, protected, or private and everything until the next access control keyword will have that access control level.
2. Define the method regularly, and then specify public, private, and protected access levels and list the comma(,) separated methods under those levels using method symbols.

#### Example of the first way:

```
class MyClass  private    def func1      "private"    end  protected    def func2      "protected"    end  public    def func3      "Public"    endend
```

#### Example of the second way:

```
class MyClass  def func1    "private"  end  def func2    "protected"  end  def func3    "Public"  end  private :func1  protected :func2  public :func3end
```

_Note: The public and private access controls are used the most._

### Conclusion

These are the very basics of Object Oriented Programming in Ruby. Now, knowing these concepts you can go deeper and learn them by building cool stuff.

Don’t forget to clap and follow if you enjoyed! Keep up with me [here](https://www.instagram.com/nishantmishra02/).

