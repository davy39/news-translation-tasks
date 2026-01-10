---
title: Object Oriented Programming in Python – Full Crash Course
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-10-20T22:24:35.000Z'
originalURL: https://freecodecamp.org/news/crash-course-object-oriented-programming-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/udaXTUR.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: null
seo_desc: "Object Oriented programming, or \"OOP\" for short, is a way of writing\
  \ code that relies on the concepts of classes and objects. \nThe main benefit of\
  \ writing your code in an object-oriented way is to structure your program into\
  \ simple, reusable pieces o..."
---

Object Oriented programming, or "OOP" for short, is a way of writing code that relies on the concepts of classes and objects. 

The main benefit of writing your code in an object-oriented way is to structure your program into simple, reusable pieces of code.

Stick with me through this article and you'll have a full understanding of the core tenets of OOP by the end. All the coding examples will be in [Python](https://boot.dev/learn/learn-python), but the concepts apply generally to all coding languages.

I've included all the learning material you'll need here in this article. But if you would like to go more in-depth with live coding exercises and quizzes, you can find those [here](https://boot.dev/learn/learn-object-oriented-programming) on [Boot.dev](https://boot.dev/).

## Table of Contents

1. [The Goal of Object Oriented Programming](#heading-the-goal-of-oop-is-cleaner-code)
2. [Classes in OOP](#heading-classes-allow-for-even-more-reusability)
3. [OOP Pillar #1 –Encapsulation](#heading-oop-pillar-1-encapsulation)
4. [OOP Pillar #2 –Abstraction](https://www.freecodecamp.org/news/p/463de7a5-749b-49da-96e9-223a08fc983b/oop-pillar-2-abstraction)
5. [OOP Pillar #3 –Inheritance](#heading-oop-pillar-3-inheritance)
6. [OOP Pillar #4 –Polymorphism](#heading-oop-pillar-4-polymorphism)

## The Goal of OOP is Cleaner Code

Object oriented programming and other paradigms like [functional programming](https://boot.dev/learn/learn-functional-programming) are all about making code easier to work with and understand. We call code that is easy to work with "clean code".

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler

### Clean code is not:

* A way to make your programs run faster
* A way to make your program use less memory
* Necessary to create certain kinds of programs
* Strictly better than non-OOP code

### Clean code is:

* Designed to make code easier to work with in many situations
* Something that helps humans model and simulate the real world
* A way to make finding and fixing bugs easier
* A way to make new feature development faster
* The best way to stay sane as a software engineer

A couple of examples of "clean code" practices include [writing good comments](https://blog.boot.dev/clean-code/code-comments/), using [DRY code](https://blog.boot.dev/clean-code/dry-code/), and [naming variables well](https://blog.boot.dev/clean-code/naming-variables/), just to name a few.

## OOP is a Way to Write DRY Code

Let's pretend we have some code that looks like this:

```python
soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]

soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
```

We can use a function to refactor the code a bit:

```python
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
    
soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)
```

We don't want too much of our code doing the exact same thing. When code is duplicated, it leads to many potential problems. In our example, let's pretend the `soldier` dictionary changed, and now the key that stores the "damage" value is called `dmg`.

In the first example, we would need to update two lines of code. In the second example, we only need to make the change in one place.

It's not a big deal when two lines are the same and exist right next to each other. However, imagine if we had done this hundreds of times in ten or twenty different code files! All of sudden, it makes a lot sense to stop repeating yourself and write more reusable functions. We call that [DRY (don't repeat yourself) code](https://blog.boot.dev/clean-code/dry-code/).

## Classes Allow for Even More Reusability

A [class](https://boot.dev/course/f9a48bbc-d1ff-4388-bf0c-23c6e3c60ae0/46f1f86f-9b7c-4a8b-8883-4b407c0e675b) is a special type of value in an object-oriented programming language like Python. Just like a string, integer, or float, a class is a _custom_ type that has some special properties.

An object is just an instance of a class type. "Instance" is just a big word for "one of a thing". For example, here, `health` is an instance of an integer type.

```python
health = 50
```

### How do I create a class?

In Python you just need to use the `class` keyword, and you can set custom properties in the following way.

```python
class Soldier:
    health = 5
```

Then to create an instance of a `Soldier` we simply call the class. Notice that a class isn't a function, and it doesn't take input parameters directly.

```python
first_soldier = Soldier()
print(first_soldier.health)
# prints "5"
```

### Methods on a class

You might be wondering why classes are useful – they seem like regular Python dictionaries but worse! 

What makes classes really cool is that they allow us to define custom [methods](https://en.wikipedia.org/wiki/Method_(computer_programming)) on them. A method is a function that is associated with a class, and it has access to all the properties of the object.

```python
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"
```

### The special "self" value

As you can see, methods are nested within the `class` declaration. Methods always take a special parameter as their first argument called `self`. The `self` variable is a reference to the object itself, so by using it you can read and update the properties of the object.

Notice that methods are called directly on an object using the dot operator.

```python
object.method()
```

### How to return values from a method

If a regular function doesn't return anything, it's typically not a very useful function. But methods often don't return anything explicitly because they often mutate the properties of the object instead.

However, they _can_ return values as well!

```python
class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"
```

### Methods vs Functions

A function is a piece of code that is called by a name. You can pass it data to operate on via parameters and it can optionally return data. All data that is passed to a function is explicitly passed through parameters.

A method is a piece of code that is called by a name _that is associated with an object_. Methods and functions are similar but have two key differences.

1. A method is _implicitly_ passed the object on which it was called. In other words, you won't see all the inputs in the parameter list
2. A method is able to operate on data that is contained within the class. In other words, you won't see all the outputs in the `return` statement.

## The OOP Debate

Because functions are more explicit, some developers argue that [functional programming](https://blog.boot.dev/clean-code/benefits-of-functional-programming/) is better than object oriented programming. In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.

For example, while methods are more implicit and often make code more difficult to read, they also make it easier to group a program's data and behavior together in one place. This can lead to a codebase that's more organized. The tradeoff is one of readability at the file level for readability at the project level.

## Constructors in Python

It's quite rare in the real-world to see a class that defines properties in the way we've been doing it so far.

```python
class Soldier:
    armor = 2
    num_weapons = 2
```

It's much more practical to use a [constructor](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)). In Python, a constructor is made with the [__init__() method](https://docs.python.org/3/reference/datamodel.html#object.__init__), and it is automatically called when a new object is created. So, with a constructor the code would look like this.

```python
class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2
```

However, because the constructor is a method, we can now make the starting armor and number of weapons configurable with some parameters.

```python
class Soldier:
    def __init__(self, armor, num_weapons):
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier(5, 10)
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"
```

## Class Variables vs Instance Variables

So far we've worked with both class variables and instance variables, but we haven't really talked about the difference yet.

### Instance variables

Instance variables vary from object to object and are declared in the constructor.

```python
class Wall():
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"
```

### Class variables

Class variables remain the same between instances of the same class and are declared at the top-level of a class.

```python
class Wall():
    height = 10

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height)
# prints "20"
```

### **Class vs instance variables – which should I use?**

Generally speaking, _stay away from class variables_. Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making data updates. 

However, it is important to understand how they work because you may see them out in the wild.

# The Four Pillars of OOP

## OOP Pillar #1 – Encapsulation

[Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) is one of the strongest tools in your tool belt as a software engineer. Like we covered in the beginning of this tutorial, writing code that machines understand is easy. But writing code that humans can understand is very difficult.

Encapsulation is the practice of hiding information inside of a "[black box](https://en.wikipedia.org/wiki/Black_box)" so that other developers working with the code don't have to worry about it. 

A basic example of encapsulation would be a function. The caller of a function doesn't need to worry too much about what happens inside – they just need to understand the inputs and outputs.

```python
pythonacceleration = calc_acceleration(initial_speed, final_speed, time)
```

In the example above, to use the `calc_acceleration` function, we don't really need to understand what goes on inside. That's the goal of encapsulation: it makes our lives easier as developers and helps us write cleaner code.

### Encapsulation in OOP

In the context of object-oriented programming, we can practice good encapsulation by using private and public members. 

The idea is that if we want the users of our class to interact with something directly, we make it _public_. If they don't need to use a certain method or property, we make that _private_ in order to keep the usage instructions for our class simple.

### Encapsulation in Python

In order to enforce encapsulation in Python, developers prefix properties and classes that they intend to be private with a double underscore.

```python
class Wall():
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall
        self.__height = height

    def get_height(self):
        return self.__height
```

In the example above, we don't want users of the `Wall` class to be able to change its height. We make the `__height` property private and expose a public `get_height` method so that users can still read the height of a wall without being tempted to update it. 

This will stop developers from being able to do something like:

```python
# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error
```

### Encapsulation does NOT make systems more secure

Like we talked about earlier, encapsulation is the practice of hiding some code complexity inside a "[black box](https://en.wikipedia.org/wiki/Black_box)" so that other developers working with the code don't have to worry about it. Adding encapsulation to our programs through "public" and "private" members makes our code easier to work with. It makes it "cleaner".

To be clear, encapsulation doesn't make the code more secure in the [cryptographic](https://boot.dev/learn/learn-cryptography) or cyber-security sense of the word. That's a point I was personally confused about when I was first learning about private and public class members in school. 

Things like [SHA-256](https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/) hashes, [JWTs for authentication](https://blog.boot.dev/cryptography/hmac-and-macs-in-jwts/), and [ciphers](https://blog.boot.dev/cryptography/aes-256-cipher-python-cryptography-examples/) are a completely separate topic that have nothing to do with classes or encapsulation.

Encapsulation is a mechanism for making code easier to work with and less buggy. We stop _ourselves_ from accessing private data because we've decided it doesn't make sense to be used outside from outside of the class.

## OOP Pillar #2 – Abstraction

Abstraction is one of the key concepts of object-oriented programming. The goal of abstraction is to handle complexity by hiding unnecessary details. 

Abstraction and encapsulation typically go hand in hand, and if we aren't careful with our definitions, they can seem like the same thing.

### Abstraction vs encapsulation

While definitions are always changing, I like to think about abstraction and encapsulation in the following way.

* Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
* Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.

If you want a longer read on the topic, check out [this essay](https://web.archive.org/web/20210513154547/https://www.tonymarston.net/php-mysql/abstraction.txt).

### So are we _encapsulating_ or _abstracting_ our code when we make things private?

Both. We are almost always doing both. The process of using the double underscore is a form of encapsulation. The process of _deciding_ which data _deserves_ to be hidden behind the double underscore is abstraction. 

Let's look at a concrete example.

```python
import random

my_random_number = random.randrange(5)
```

In this example we're using the `random` library to generate a random number. As it turns out, [generating random numbers](https://blog.boot.dev/cryptography/what-is-entropy-in-cryptography/) is a _*really hard*_ problem. 

The operating system actually uses the physical hardware state of the computer as an input to seed the randomness. 

However, the developers of the `random` library have _abstracted_ that complexity away and _encapsulated_ a lot of that data and behavior so we don't need to worry about it. We just say "I want a random number less or equal to than 5" and the library takes care of it for us.

The decision to take a single number as input to the `randrange` function was a decision of abstraction. When writing production-level software, getting the abstractions right is crucial, because they are the hardest things to change later. 

Think about the consequences of the `random` package maintainers changing the input parameters to the `randrange` function! It would break code all over the world.

## How OOP Developers Think

Methods can actually be private as well. In other words, we can encapsulate _behavior_ as well as _data_.

### **Grouping data and behavior**

Classes in object-oriented programming are all about grouping data and behavior together in one place: an object. 

Object oriented programmers tend to think about programming as a modeling problem. They think, "how can I write a `Human` class that simulates the data and behavior of a real human?"

We aren't focusing on [functional programming](https://boot.dev/learn/learn-functional-programming) in this course. But to provide some contrast, functional programmers tend to think of their code as inputs and outputs. "When a human performs an action, what are the inputs to that action, and how do the outputs affect my program state?"

### **Both paradigms are valuable**

While OOP isn't the only paradigm in programming, it's a tried and true one that is useful in a variety of circumstances. 

In any event, if you personally have an understanding of multiple ways of thinking about code, you'll be a much better developer over all.

## OOP Pillar #3 – Inheritance

We've made it to the Holy-grail of object-oriented programming: [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)). Inheritance is really the defining trait of object oriented languages. 

Languages without classes like [Go](https://boot.dev/learn/learn-golang)lang and [Rust](https://www.freecodecamp.org/news/rust-in-replit/) provide encapsulation and abstraction features. In fact, almost _every_ language does. Inheritance, on the other hand, tends to be unique to class-based languages like [Python](https://boot.dev/learn/learn-python), [JavaScript](https://www.freecodecamp.org/news/learn-javascript-by-coding-7-games/), [Java](https://www.freecodecamp.org/news/the-java-handbook/), and Ruby.

### What is inheritance?

Inheritance allows one class (aka "the child class") to _inherit_ the properties and methods of another class (aka "the parent class").

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to [DRY (don't repeat yourself)](https://blog.boot.dev/clean-code/dry-code/) up our code.

### Inheritance in Python – Syntax

In Python, one class can inherit from another using the following syntax:

```python
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
```

In order to use the constructor of the parent class, we can use Python's built in `super()` method.

```python
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)
```

### When should I use inheritance?

Inheritance is a powerful tool, but it is a _really_ bad idea to try to overuse it. You should only use inheritance when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits _everything_. If you only want to share _some_ functionality, inheritance probably is not the best answer. In that case you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from.

### All cats are animals but not all animals are cats

![Image](https://www.freecodecamp.org/news/content/images/2022/10/LwZVCId.png)

### Inheritance hierarchy

There is no limit to how deeply we can nest an inheritance tree. For example, a `Cat` can inherit from `Animal` which inherits from `LivingThing`. 

That said, we should always be careful that each time we inherit from a base class that the child is a _*strict*_ subset of the parent. You should never think to yourself "my child class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

### Multiple children

So far we've worked with linear class inheritance. In reality, inheritance structures often form trees, not lines. A class can have as many direct child classes as the programmer wants.

You'll often find in production software that it's more likely that an inheritance tree is wide than deep. In other words, instead of a deep tree like:

`Organism -> Animal -> Mammal -> Feline -> Cat`

You will more often see a wide tree:

```
Dragon -> Drake
       -> Wyvern
       -> Hydra
       -> Druk
```

### Why are **inheritance** trees often wide instead of deep?

Like we talked about earlier, in good software a child class is a strict subset of its parent class. 

In a deep tree, that means the children need to be perfect members of all the parent class "types". That simply doesn't happen very often in the real world. It's much more likely that you'll have a base class that simply has many sibling classes that are slightly different variations of the base.

```
Vehicle -> Truck
        -> Car
        -> Boat
        -> Train
```

## OOP Pillar #4 – Polymorphism

While inheritance is the most unique trait that object-oriented languages make claim to, polymorphism is probably the most powerful.

Polymorphism is the ability of a variable, function, or object to take on multiple forms. For example, in a programming language that supports inheritance, classes in the same hierarchical tree may have methods with the same name but _different_ behaviors.

### Polymorphism with shapes

Let's look at a simple example:

```python
class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims
```

In this example the child classes, `Dragon` and `Kraken` are **overriding** the behavior of their parent class's `move()` method.

### Polymorphisms Roots

Take a look at the Greek roots of "polymorphism".

* "poly" means "many"
* "morph" means "to change" or "form"

Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).

A classic example is a `Shape` class that `Rectangle`, `Circle`, and `Triangle` can inherit from. 

With polymorphism, each of these classes will have different underlying data. The circle needs a center and radius. The rectangle needs two co-ordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

By making each class responsible for its data **and** its code, you can achieve polymorphism. 

In this example, each class would have its own `Draw()` method. This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the **same** even though they are **different**. It hides the complexities of the difference behind a clean abstraction.

```python
shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
for shape in shapes:
    print(shape.Draw())
```

This is in contrast to the functional way of doing things where you would have had separate functions that have **different** function signatures, like `draw_rectangle(x1, y1, x2, y2)` and `draw_circle(center, radius)`.

### Wait, what is a "function signature"?

A function signature includes the name, inputs, and outputs of a function or method. For example, these two classes have the same method signatures.

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
```

Both methods have the same name, take `0` inputs, and return integers. If _any_ of those things are different, they would have different function signatures.

Here is an example of different signatures.

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
```

### When overriding methods, use the same function signature

If you change the function signature of a parent class when overriding a method, it could be a disaster. 

The whole point of overriding a method is so that the caller of your code _doesn't have to worry_ about what different things are going on inside the methods of different object types.

### Operator overloading

Another kind of built-in polymorphism in Python is the ability to override an operator in Python depending upon the operands used.

Arithmetic operators work for built-in types like integers and strings.

```python
print(3 + 4)
# prints "7"

print("three " + "four")
# prints "three four"
```

Custom classes, on the other hand, don't have any built-in support for those operators:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

However, we can add our own support! The `__add__` method is used by the Python interpreter when instances of a class are being added with the `+` operator.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
```

When you call `p1 + p2` under the hood the interpreter just calls `p1.__add__(p2)`.

Here's a list of how the operators translate into method names. If you're not familiar with logical and bitwise operators in Python, you can check out [this video](https://www.youtube.com/watch?v=1rUzblmGHzk).

| Operation           | Operator | Method       |
| ------------------- | -------- | ------------ |
| Addition            | +        | __add__      |
| Subtraction         | -        | __sub__      |
| Multiplication      | *        | __mul__      |
| Power               | **       | __pow__      |
| Division            | /        | __truediv__  |
| Floor Division      | //       | __floordiv__ |
| Remainder (modulo)  | %        | __mod__      |
| Bitwise Left Shift  | <<       | __lshift__   |
| Bitwise Right Shift | >>       | __rshift__   |
| Bitwise AND         | &        | __and__      |
| Bitwise OR          | \|       | __or__       |
| Bitwise XOR         | ^        | __xor__      |
| Bitwise NOT         | ~        | __invert__   |

### How to overload built-in methods

Last but not least, let's take a look at some of the built-in methods we can overload in Python. While there isn't a default behavior for the arithmetic operators like we just saw, there _is_ a default behavior for **printing** a class.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# prints "<Point object at 0xa0acf8>"
```

That's not super useful! Let's teach instances of our `Point` object to print themselves. The `__repr__` method (short for "represent") lets us do just that. It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's `print()` function.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"
```

## Great Job Making it to the End!

Thanks for joining me in this written course about object oriented programming. 

If you're interested in doing the live coding assignments and quizzes for this course you can do so on the [Learn OOP course](https://boot.dev/learn/learn-object-oriented-programming) over on [Boot.dev](https://boot.dev/). 

Alternatively, if you'd like to check out the next course in the [back-end developer career path](https://boot.dev/tracks/computer-science) you can start the [Learn Algorithms](https://boot.dev/learn/learn-algorithms) course here.

