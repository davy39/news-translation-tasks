---
title: How to Use Object-Oriented Programming in Python – Explained With Examples
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2024-04-24T14:39:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-oop-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/WhatsApp-Image-2024-04-24-at-8.25.07-AM.jpeg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: null
seo_desc: 'Object-oriented programming (OOP) is a style of programming that heavily
  relies on objects. These objects can have attributes and methods. While attributes
  store data, methods define behavior.

  Like many other programming languages, Python supports bo...'
---

Object-oriented programming (OOP) is a style of programming that heavily relies on objects. These objects can have attributes and methods. While attributes store data, methods define behavior.

Like many other programming languages, Python supports both OOP and functional programming. However, OOP becomes valuable when writing large-sized and complex programs.

In this article, you will learn the benefits of OOP in Python, how to define a class, class and instance attributes, and instance methods. You will also learn the concept of encapsulation and how to implement inheritance between classes in Python.

To fully understand this article, you should have the following prerequisites:

* Basic knowledge of the Python programming language.
    
* Familiarity with the concepts of functions and objects in programming.
    
* Experience working with a code editor or integrated development environment (IDE).
    
* Basic understanding of how to use a command-line terminal or console.
    

Now let's dive in.

## Why Use Object-Oriented Programming?

Object-oriented programming (OOP) offers several benefits when organizing and managing code. By grouping related data and functions into logical classes, OOP promotes code structure and simplifies maintenance, especially as programs grow in size and complexity. The [modular approach](https://en.wikipedia.org/wiki/Modular_programming) makes it easier to understand, modify, and reuse code, thereby reducing development time.

Another benefit of OOP is its ability to provide a clear and relatable programming style, which can be more helpful for developers. The use of objects and the relationships between them mirror real-world concepts. This makes it easier to reason about code and design complex systems.

Finally, OOP's concepts such as encapsulation and inheritance, contribute to code robustness by promoting data protection and code reusability.

## What is a Class in Python?

OOP in Python heavily relies on the concept of `class`. You can think of a class as a blueprint that is used to create objects. To illustrate this, imagine that you have a blueprint for a speaker. You can use this blueprint to build multiple speakers. Each speaker that is created using the blueprint is an instance of the blueprint. Also, each created speaker has its attributes such as color, model, and name. They will also have their methods showing a certain kind of behavior such as volume up and volume down.

## How to Define a Class in Python

To define a class, you have to use the `class` keyword, provided by Python, then followed by the name of the class and a colon:

```python
class ClassName:
    pass
```

Now using our earlier illustration, let’s create a class named `Speaker`. In your code editor, create a file named `classes.py` and copy the following lines of code into it:

```python
class Speaker:
    pass

speaker_one = Speaker()
print(speaker_one)
```

In the preceding code, you defined a class named `Speaker` without any attributes or methods. You used the keyword `pass` in the class body. In Python, the `pass` keyword does nothing and is usually used as a placeholder.

In line four of the code, you created an instance of the `Speaker` class and assigned it to the variable `speaker_one`. This process is also known as instantiating an object from a class. You then printed `speaker_one` in line five.

Now run the code by running the command `python classes.py` in your terminal. You will get an output similar to this in your terminal:

```bash
<__main__.Speaker object at 0x10087f8e0>
```

The output shows that `speaker_one` is an object. `0x10087f8e0` in the output shows the memory address where Python stores the object on your computer.

The memory address in your terminal output will be different.

You can create several more instances from the `Speaker` class and they will all be different from one another. To verify this, let’s use the equality comparison (**\==**) operator. In your `classes.py` file, delete `print(speaker_one)` and add the following to the bottom of your code:

```python
speaker_two = Speaker()

if speaker_one == speaker_two:
    print("speaker one is the same as speaker two")
else:
    print("speaker one is different from speaker two")
```

Now run `python classes.py` in your terminal. You will get the following output:

```bash
speaker one is different from speaker two
```

## Class and Instance Attributes

In this section, you'll add attributes to your `Speaker` class. You can see attributes as data stored within an object. While class attributes are common to all instances created from your class, instance attributes are unique to each instance.

Now modify your `classes.py` file by replacing your code with the following:

```python
class Speaker:
    brand = "Beatpill" # class attribute

    def __init__(self, color, model):
        self.color = color # instance attribute
        self.model = model # instance attribute
```

You should already be familiar with line one of your new code. In line two, you defined a class attribute, named `brand`, and assigned it the value `Beatpill`. Class attributes are variables that belong to the class itself, rather than to individual instances of the class. The effect of class attributes is that all instances you create from your class will inherit and share that class attribute and its value. In this case, every instance you create from your `Speaker` class will share the same `brand` value.

Line four of your code defines an `__init__` method, which takes in three parameters—`self`, `color`, and `model`. This method will be called anytime you create a new instance from your `Speaker` class. The `self` parameter is a reference to the `Speaker` class and it's a convention in Python to always have it as the first parameter in a `__init__` method. Line five and six set instance attributes, `color`, and `model` to your `Speaker` class.

So, every time you create a new instance from your class, you have to provide arguments for your `color` and `model` attributes. Not doing this will result in an error.

Now add the following to the bottom of your code:

```python
speaker_one = Speaker("black", "85XB5")
speaker_two = Speaker("red", "Y8F33")

print(f"speaker one is {speaker_one.color} while speaker two is {speaker_two.color}")
```

By adding the preceding code, you created two instances of the `Speaker` class—`speaker_one` and `speaker_two`. The arguments in each instance represent the values of their `color` and `model` attributes. You then printed a message that displays the color attribute of each object. Now, if you run the command `python classes.py` in your terminal, you will get the output:

```bash
speaker one is black while speaker two is red
```

To see that both instances share the same `brand` class attribute, modify your `print()` function like this:

```python
print(
    f"speaker one is {speaker_one.color} while speaker two is {speaker_two.color}",
    speaker_one.brand,
    speaker_two.brand,
    sep="\n",
)
```

Now run `python classes.py` and you will get the following output:

```bash
speaker one is black and speaker two is red
Beatpill
Beatpill
```

## Instance Methods

In addition to class and instance attributes, classes can also have methods, known as instance methods. Instance methods are functions defined within a class that operate on instances of the class. They use the class and instance attributes to provide behavior and functionality to the objects.

To add instance methods, modify your code file as follows:

```python
class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def power_on(self):
        print(f"Powering on {self.color} {self.model} speaker.")

    def power_off(self):
        print(f"Powering off {self.color} {self.model} speaker.")


speaker_one = Speaker("black", "85XB5")
speaker_two = Speaker("red", "Y8F33")
```

In the example above, we've added two instance methods—`power_on()` and `power_off()`. These methods, just like the `__init__` method, take `self` as the first argument.

The `power_on()` method prints a message indicating that the speaker of the given color and model is being powered on. Similarly, the `power_off()` method prints a message about powering off the speaker.

To call these methods, add the following to the bottom of your file:

```python
speaker_one.power_on()
speaker_two.power_off()
```

Now run `python classes.py` in your terminal and you will get the following output:

```bash
Powering on black 85XB5 speaker.
Powering off red Y8F33 speaker.
```

## Encapsulation in Python

Encapsulation is one of the core concepts of OOP. It refers to the bundling of data (attributes) and methods within a class. Encapsulation provides data protection and control over how the code interacts with an object's internal state.

You can achieve encapsulation in Python by defining private attributes and methods within a class. By convention, private attributes and methods are prefixed with a single underscore (\_). While Python does not have strict private modifiers like some other languages, the underscore prefix serves as a warning to other developers not to access or modify the attributes and methods directly from outside the class.

Here's an example of encapsulation in Python:

```python
class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self._color = color  # Private attribute
        self._model = model  # Private attribute

    def power_on(self):
        print(f"Powering on {self._color} {self._model} speaker.")

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker.")

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


speaker_one = Speaker("black", "85XB5")
speaker_one.power_on()

# Accessing a private attribute directly (not recommended)
print(speaker_one._color)

# Accessing a private attribute using the getter method (recommended)
print(speaker_one.get_color())

# Modifying a private attribute using the setter method (recommended)
speaker_one.set_color("white")
print(speaker_one.get_color())
```

In the preceding example, the `color` and `model` attributes are private attributes of the `Speaker` class. Although it is possible to access and modify these attributes directly from outside the class by using, for example, `print(speaker_one._color)`, this practice is discouraged. Doing so violates encapsulation and can lead to unintended behavior or data corruption.

Instead, the class provides getter `get_color()` and setter `set_color()` methods to access and modify the private attributes in a controlled manner. These methods act as an interface for interacting with the object's internal state, ensuring data integrity and enabling additional validation.

Encapsulation promotes code modularity, maintainability, and data protection by separating the internal state from the public interface (methods). It allows you to change the internal state without affecting the code that uses the class, as long as the public interface remains the same.

## Inheritance in Python

Inheritance is another core concept of OOP. It allows classes to inherit attributes and methods from other classes. The new class inherits attributes and methods from the existing class, known as the parent or base class. The new class is called the child or derived class.

Inheritance promotes code reuse by allowing the child class to inherit and extend the functionality of the parent class. This helps in creating hierarchical relationships between classes and organizing code in a more structured and logical manner.

In Python, inheritance is implemented using the following syntax:

```python
class DerivedClass(BaseClass):
    # Derived class methods and attributes
```

To see how inheritance works, modify your code as follows:

```python
class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self._color = color
        self._model = model

    def power_on(self):
        print(f"Powering on {self._color} {self._model} speaker.")

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker.")

# Add a SmartSpeaker class and make it inherit from the Speaker class
class SmartSpeaker(Speaker):
    def __init__(self, color, model, voice_assistant):
        super().__init__(color, model)
        self._voice_assistant = voice_assistant

    def say_hello(self):
        print(f"Hello, I am {self._voice_assistant}")


# Create an instance of the SmartSpeaker class
smart_speaker = SmartSpeaker("black", "XYZ123", "Alexa")
smart_speaker.power_on()  # Inherited from Speaker
smart_speaker.say_hello()
```

In the preceding code, the `SmartSpeaker` class is derived from the `Speaker` class. The `SmartSpeaker` class inherits the attributes and methods of the `Speaker` class.

The `__init__` method of the `SmartSpeaker` class calls the `__init__` method of the `Speaker` class using `super().__init__(color, model)`. This ensures that the inherited `_color` and `_model` attributes are properly initialized. Also, the `SmartSpeaker` class has its own attribute `_voice_assistant`, and a new method `say_hello`.

Now run `python classes.py` in your terminal and you will get the following output:

```bash
Powering on black XYZ123 speaker.
Hello, I am Alexa
```

## Conclusion

Throughout this article, we highlighted the benefits of Object-Oriented Programming (OOP) and demonstrated how to define classes, create and use instance attributes and methods. We provided practical examples to illustrate the implementation of classes in Python, as well as key OOP concepts such as encapsulation and inheritance.

Applying the lessons covered in this article will help you improve your Python programming experience and increase the efficiency and maintainability of your code.

## References and Further Reading

* https://en.wikipedia.org/wiki/Object-oriented\_programming
    
* https://realpython.com/python3-object-oriented-programming/
    
* https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented\_programming
    
* https://docs.python.org/3/tutorial/classes.html
    
* https://realpython.com/python-classes/
    
* https://realpython.com/python-double-underscore/
