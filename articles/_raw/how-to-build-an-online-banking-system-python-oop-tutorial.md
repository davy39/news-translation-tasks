---
title: How to Build an Online Banking System – Python Object-Oriented Programming
  Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-20T18:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-online-banking-system-python-oop-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/OOP_in_Python.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: null
seo_desc: "By Jacob Isah \nObject-Oriented Programming (OOP) is a fundamental concept\
  \ in software engineering that allows software engineers to structure code in a\
  \ more organized and modular way. \nPython, with its clear and concise syntax, is\
  \ an excellent langua..."
---

By Jacob Isah 

Object-Oriented Programming (OOP) is a fundamental concept in software engineering that allows software engineers to structure code in a more organized and modular way. 

Python, with its clear and concise syntax, is an excellent language for learning and implementing OOP principles. 

In this article, we'll  look at the basics of OOP in Python by building a simple online banking system.

## An Overview of OOP Concepts

Before we start coding, let's understand the key concepts of OOP:

* **Classes**: Classes are blueprints for creating objects. They define the attributes (data) and methods (functions) that objects of that class will have.
* **Objects**: Objects are instances of classes. They represent real-world entities and encapsulate data and behavior.
* **Inheritance**: Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reuse and supports hierarchical relationships between classes.
* **Constructor:** A constructor ( `__init__()` ) is a special type of method that is automatically called when an object of a class is created. Its primary purpose is to initialize the newly created object, setting initial values for its attributes or performing any necessary setup tasks.

## How to Build An Online Banking System

Let's start by creating the basic structure for our online banking system using OOP principles.

### How to Create A Class and Constructor

Let's create a class and initiate the class with the constructor:

```python
class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
```

In the example above:

* The `class` keyword declares an `Account` class.
* The `__init__()` method is the constructor, defined with the special double underscore notation at the beginning and end.
* `self` is a reference to the instance of the class. It is the first parameter of all instance methods in Python.
* `name` is the name of the account holder.
*  `account_number`  is a unique identifier for the savings account, and `balance` are parameters passed to the constructor.
* Inside the constructor `self.name`, `self.account_number`, and `self.balance` are attributes of the class `Account` that are initialized with the values of `name`, `account_number` and `balance`, respectively.

Constructors can perform various tasks such as initializing attributes, opening connections, loading data, and more. They are essential for ensuring that objects are properly set up and ready for use as soon as they are created.

### How to Create Methods (functions)

The next thing to do is to write the different methods for our `Account` class. Users should be able to deposit and withdraw.

#### How to create a deposit method

```python
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} Deposited {amount} $. Current balance is: {self.balance}")
```

In the example above:

* The `deposit` method allows users to add funds to their account.
* The method takes an additional parameter `amount`, which is the amount to be deposited.
* Inside the method, the `amount` is added to the current balance using `self.balance += amount`.
* A message is printed showing the depositor name and the amount deposited and the balance is updated.

#### How to create a withdraw method

```python
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} Withdrew {amount} $. Current balance is: {self.balance}")
        else:
            print("You don't have enough funds to withdraw.")
```

In the example above:

* The `withdraw` method allows users to withdraw funds from their account.
* The method also takes an `amount` parameter which is the amount our user wants to withdraw.
* The method checks if the account balance (`self.balance`) is greater than or equal to the amount our user wants to withdraw.
* If the balance is enough, the withdrawal amount is removed from the balance using `self.balance -= amount`.
* If the balance is not enough, a message stating “You don't have enough funds to withdraw.” is printed to the user.

### How Inheritance Works

Having explained inheritance above, let's see how it works in code. We are going to create a class that inherits the `Account` class. 

Note that the `Account` class is the supper class, while the `Savings_Account` class is a subclass, also known as a child class.

```python
class Savings_Account(Account):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate
```

In the above code:

* The `__init__` method is the constructor for the `Savings_Account` class.
* It accepts four parameters: `name` which is the name of the account holder,  `account_number`, which is a unique identifier for the savings account, `balance`, which is the initial balance of the account, and `interest_rate`, which is the annual interest rate (expressed as a decimal) for the account.
* The `super().__init__(name, account_number, balance)` line calls the constructor of the parent class (`Account`) to initialize the account number and balance.
* The `self.interest_rate = interest_rate` line sets the interest rate specific to the savings account. it is not inherited

### How to Create An `add_interest`  Method 

```python
def add_interest(self):
    interest = self.balance * self.interest_rate
    self.deposit(interest)
```

In the example above:

* The `add_interest` method calculates and adds interest to the account balance.
* The method calculates the interest by multiplying the current balance (`self.balance`) with the interest rate (`self.interest_rate`).
* The result is stored in the `interest` variable.
* Finally, the `self.deposit(interest)` line calls the `deposit` method (defined in the parent `Account` class) to add the interest amount to the account balance.

### How to Create and Use Objects

Your class is just a template. You need to create an object for your class to work.

Now, let's create objects from our classes and interact with them.

```python
account1 = Account("John Doe", "123456", 1000)
account1.deposit(500)
account1.withdraw(200)
print()

savings_account = Savings_Account("John Doe", "789012", 2000, 0.05)
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)
savings_account.withdraw(1000)
```

In the above code:

* We created an instance `account1` of the `Account` class and performed deposit and withdrawal operations.
* Similarly, we created an instance `savings_account` of the `Savings_Account` class and demonstrated deposit, interest addition, and withdrawal operations.

## Conclusion

Object-Oriented Programming is a powerful paradigm that allows software engineers to write code that is reusable, maintainable, and can scale. 

Python's simplicity makes it an excellent choice for learning and implementing OOP concepts. 

By building a simple online banking system, I've show you the basic concepts of classes, objects, and inheritance in Python. 

Happy coding!

