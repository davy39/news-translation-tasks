---
title: What are the SOLID Principles in C#? Explained With Code Examples
subtitle: ''
author: Danny
co_authors: []
series: null
date: '2024-10-24T15:07:34.502Z'
originalURL: https://freecodecamp.org/news/what-are-the-solid-principles-in-csharp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729777076695/7d956373-1835-4823-9a6a-d2d232cd64d5.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: C#
  slug: csharp
- name: software development
  slug: software-development
- name: design patterns
  slug: design-patterns
- name: Web Development
  slug: web-development
- name: Software Engineering
  slug: software-engineering
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: The SOLID Principles are five software design principles that help you to
  write high quality, flexible, maintainable, reusable, testable, and readable software.
  If you plan to work with object-oriented software, it is crucial to understand these
  five...
---

The SOLID Principles are five software design principles that help you to write high quality, flexible, maintainable, reusable, testable, and readable software. If you plan to work with object-oriented software, it is crucial to understand these five principles.

The SOLID Principles were introduced by a software engineer named Robert C. Martin (also known as "Uncle Bob") in the early 2000s. Uncle Bob’s goal was to promote good software design practices, particularly in object-oriented programming (OOP), by addressing common problems developers face as software systems grow in size and complexity.

Here are the five SOLID principles:

* **S**: [Single Responsibility Principle (SRP)](#heading-single-responsibility-principle-srp)
    
* **O**: [Open-closed Principle (OCP)](#heading-open-closed-principle-ocp)
    
* **L**: [Liskov Substitution Principle (LSP)](#heading-liskov-substitution-principle-lsp)
    
* **I**: [Interface Segregation Principle (ISP)](#heading-interface-segregation-principle-isp)
    
* **D**: [Dependency Inversion Principle (DIP)](#heading-dependency-inversion-principle-dip)
    

By following these principles, you can create software designs that are easier to understand, maintain, and extend, leading to higher-quality software that is more robust and adaptable to change.

In this article, to demonstrate each principle, I’ll first show you a bad code example in C# that violates the principle. We will then discuss the issues this bad code causes, and then solve those issues by refactoring the code to satisfy the principle.

First up we have the…

## Single Responsibility Principle (SRP) in C#

> A class should have only one reason to change, meaning that it should have only one responsibility or purpose.

This principle encourages you to create classes that are more focussed and perform one single well-defined task, rather than multiple tasks. Breaking up classes into smaller, more focused units makes code easier to understand, maintain, and test.

**An example that violates the SRP:**

```csharp
public class User
{
 public string Username { get; set; }
 public string Email { get; set; }

 public void Register()
 {
   // Register user logic, e.g. save to database...

   // Send email notification
   EmailSender emailSender = new EmailSender();
   emailSender.SendEmail("Welcome to our platform!", Email);
 }
}
```

```csharp
public class EmailSender
{
 public void SendEmail(string message, string recipient)
 {
   // Email sending logic
   Console.WriteLine($"Sending email to {recipient}: {message}");
 }
}
```

In this example, the `User` class manages user data (username and email), and contains logic for registering a user. This violates the SRP because the class has more than one reason to change. It could change due to:

* Modifications in user data management – for example adding more fields, such as `firstName`, `gender`, `hobbies`.
    
* Modifications to the logic of registering a user, for example we may choose to fetch a user from the database by their username rather than their email.
    

To adhere to the Single Responsibility Principle, we should separate these responsibilities into separate classes. 

**Refactoring the code to satisfy the SRP**:

```csharp
public class User
{
 public string Username { get; set; }
 public string Email { get; set; }
}
```

```csharp
public class EmailSender
{
 public void SendEmail(string message, string recipient)
 {
   // Email sending logic
   Console.WriteLine($"Sending email to {recipient}: {message}");
 }
}
```

```csharp
public class UserService
{
 public void RegisterUser(User user)
 {
   // Register user logic...

   EmailSender emailSender = new EmailSender();
   emailSender.SendEmail("Welcome to our platform!", user.Email);
 }
}
```

In the refactored code, the `User` class is responsible solely for representing user data. The `UserService` class now handles user registration, separating concerns related to user data management from user registration logic. The `UserService` class is responsible only for the business logic of registering a user.

This separation of responsibilities adheres to the Single Responsibility Principle, making the code easier to understand, maintain, and extend.

## Open/Closed Principle (OCP) in C#

> Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

This principle promotes the idea that existing code should be able to be extended with new functionality without modifying its source code. It encourages the use of abstraction and polymorphism to achieve this goal, allowing for code to be easily extended through inheritance or composition.

(By the way, if you don’t understand these fundamental OOP concepts, such as abstraction, polymorphism, inheritance and composition — then check out my book, [Mastering Design Patterns in C#: A Beginner-Friendly Guide, Including OOP and SOLID Principles on Amazon](https://www.amazon.com/Mastering-Design-Patterns-Beginner-Friendly-Principles/dp/B0DB6MLYYZ) or [Gumroad](https://doabledanny.gumroad.com/l/ennyj?layout=profile).)

Let's consider an example of a `Shape` class hierarchy that calculates the area of different geometric shapes. Initially, this violates the Open/Closed Principle because adding a new shape requires modifying the existing code:

```csharp
public enum ShapeType
{
 Circle,
 Rectangle
}
```

```csharp
public class Shape
{
 public ShapeType Type { get; set; }
 public double Radius { get; set; }
 public double Length { get; set; }
 public double Width { get; set; }

 public double CalculateArea()
 {
   switch (Type)
   {
     case ShapeType.Circle:
       return Math.PI * Math.Pow(Radius, 2);
     case ShapeType.Rectangle:
       return Length * Width;
     default:
       throw new InvalidOperationException("Unsupported shape type.");
   }
 }
}
```

In this example, the `Shape` class has a method, `CalculateArea()`, that calculates the area based on the type of shape. Adding a new shape, such as a triangle, would require modifying the existing `Shape` class, violating the OCP.

To adhere to the Open/Closed Principle, we should design the system in a way that allows for extension without modification. Let's refactor the code using inheritance and polymorphism:

```csharp
public abstract class Shape
{
 public abstract double CalculateArea();
}
```

```csharp
public class Circle : Shape
{
 public double Radius { get; set; }

 public override double CalculateArea()
 {
   return Math.PI * Math.Pow(Radius, 2);
 }
}
```

```csharp
public class Rectangle : Shape
{
 public double Length { get; set; }
 public double Width { get; set; }

 public override double CalculateArea()
 {
   return Length * Width;
 }
}
```

In this refactored code, we define an abstract `Shape` class with an abstract `CalculateArea()` method. Concrete shape classes (`Circle` and `Rectangle`) inherit from the `Shape` class and provide their own implementations of `CalculateArea()`.

Adding a new shape, such as a triangle, would involve creating a new class – *extending* the codebase – that inherits from `Shape` and implements `CalculateArea()`, without *modifying* existing code. This adheres to the OCP by allowing for extension without modification.

Being able to add functionality without modifying existing code means that we don’t have to worry as much about breaking existing working code and introducing bugs.

Following the OCP encourages us to design our software so that we add new features only by adding new code. This helps us to build loosely-coupled, maintainable software.

## Liskov Substitution Principle (LSP) in C#

> Objects of a superclass should be replaceable with objects of its subclass without affecting the correctness of the program.

This principle ensures that inheritance hierarchies are well-designed and that subclasses adhere to the contracts defined by their superclasses.

Violations of the LSP can lead to unexpected behavior or errors when substituting objects, making code harder to reason about and maintain.

Let's consider an example involving a `Rectangle` class and a `Square` class, which inherit from a common `Shape` class. Initially, we'll violate the LSP by not adhering to the behavior expected from these classes. Then, we'll fix it to ensure that the principle is respected.

```csharp
public abstract class Shape
{
 public abstract double Area { get; }
}
```

```csharp
public class Rectangle : Shape
{
 public virtual double Width { get; set; }

 public virtual double Height { get; set; }

 public override double Area => Width * Height;
}
```

```csharp
public class Square : Rectangle
{
 public override double Width
 {
   get => base.Width;
   set => base.Width = base.Height = value;
 }

 public override double Height
 {
   get => base.Height;
   set => base.Height = base.Width = value;
 }
}
```

Now, let’s test out if `Rectangle` calculates its area correctly:

```csharp
// Program.cs

var rect = new Rectangle();
rect.Height = 10;
rect.Width = 5;

System.Console.WriteLine("Expected area = 10 * 5 = 50.");

System.Console.WriteLine("Calculated area = " + rect.Area);
```

Running the program:

```plaintext
Expected area = 10 * 5 = 50.

Calculated area = 50
```

Perfect!

Now, in our program, the `Square` class inherits from, or extends, the `Rectangle` class, because, mathematically, a square is just a special type of rectangle, where its height equals its width. Because of this, we decided that `Square` should extend `Rectangle` – it’s like saying “a square *is a* (special type of) rectangle”.

But look what happens if we substitute the `Rectangle` class for the `Square` class:

```csharp
var rect = new Square();
rect.Height = 10;
rect.Width = 5;

System.Console.WriteLine("Expected area = 10 * 5 = 50.");

System.Console.WriteLine("Calculated area = " + rect.Area);
```

```plaintext
Expected area = 10 * 5 = 50.

Calculated area = 25
```

Oh dear, LSP has been violated: we replaced the object of a superclass (`Rectangle`) with an object of its subclass (`Square`), and it affected the correctness of our program. By modeling `Square` as a subclass of `Rectangle`, and allowing width and height to be independently set, we violate the LSP. When setting the width and height of a `Square`, it should retain its squareness, but our implementation allows for inconsistency.

Let’s fix this to satisfy LSP:

```csharp
public abstract class Shape
{
 public abstract double Area { get; }
}
```

```csharp
public class Rectangle : Shape
{
 public double Width { get; set; }

 public double Height { get; set; }

 public override double Area => Width * Height;
}
```

```csharp
public class Square : Shape
{
 private double sideLength;

 public double SideLength
 {
   get => sideLength;
   set
   {
     sideLength = value;
   }
 }

 public override double Area => sideLength * sideLength;
}
```

```csharp
// Program.cs

Shape rectangle = new Rectangle { Width = 5, Height = 4 };

Console.WriteLine($"Area of the rectangle: {rectangle.Area}");

Shape square = new Square { SideLength = 5 };

Console.WriteLine($"Area of the square: {square.Area}");
```

In this corrected example, we redesign the `Square` class to directly set the side length. Now, a `Square` is correctly modeled as a subclass of `Shape`, and it adheres to the Liskov Substitution Principle.

How does this satisfy LSP? Well, we have a superclass, `Shape`, and subclasses `Rectangle` and `Square`. Both `Rectangle` and `Square` maintain the correct expected behavior of a `Shape` — we can substitute a square for a rectangle and the area will still be calculated correctly.

## Interface Segregation Principle (ISP) in C#

> Clients should not be forced to depend on interfaces they do not use.

This principle encourages the creation of fine-grained interfaces that contain only the methods required by the clients that use them. It helps to prevent the creation of "fat" interfaces that force clients to implement unnecessary methods, leading to cleaner and more maintainable code.

Let's consider an example involving 2D and 3D shapes, initially violating the ISP.

**Violating ISP:**

```csharp
public interface IShape
{
 double Area();
 double Volume(); // problem: 2D shapes don't have volume!
}
```

```csharp
public class Circle : IShape
{
 public double Radius { get; set; }

 public double Area()
 {
   return Math.PI * Math.Pow(Radius, 2);
 }

 public double Volume()
 {
   throw new InvalidOperationException("Volume not applicable for 2D shapes.");
 }
}
```

```csharp
public class Sphere : IShape
{
 public double Radius { get; set; }

 public double Area()
 {
   return 4 * Math.PI * Math.Pow(Radius, 2);
 }

 public double Volume()
 {
   return (4.0 / 3.0) * Math.PI * Math.Pow(Radius, 3);
 }
}
```

In this example, we have an `IShape` interface representing both 2D and 3D shapes. However, the `Volume()` method is problematic for 2D shapes, like `Circle` and `Rectangle`, because they don't have volume. This violates the ISP because clients (classes using the `IShape` interface) may be forced to depend on methods they do not need.

```csharp
var circle = new Circle();
circle.Radius = 10;

System.Console.WriteLine(circle.Area());
System.Console.WriteLine(circle.Volume()); // My text editor doesn't flag a problem...

var sphere = new Sphere();
sphere.Radius = 10;

System.Console.WriteLine(sphere.Area());
System.Console.WriteLine(sphere.Volume());
```

Usually, if I try to call a method on an object that doesn’t exist, VS Code will tell me that I’m making a mistake. But above, when I call `circle.Volume()`, VS code is like “no problem”. And VS code is correct, because the `IShape` interface forces `Circle` to implement a `Volume()` method, even though circles don’t have volume.

It’s easy to see how violating ISP can introduce bugs into a program – above, everything looks fine, until we run the program and an exception gets thrown.

**Fixing ISP**

```csharp
public interface IShape2D
{
 double Area();
}
```

```csharp
public interface IShape3D
{
 double Area();
 double Volume();
}
```

```csharp
public class Circle : IShape2D
{
 public double Radius { get; set; }

 public double Area()
 {
   return Math.PI * Math.Pow(Radius, 2);
 }
}
```

```csharp
public class Sphere : IShape3D
{
 public double Radius { get; set; }

 public double Area()
 {
   return 4 * Math.PI * Math.Pow(Radius, 2);
 }

 public double Volume()
 {
   return (4.0 / 3.0) * Math.PI * Math.Pow(Radius, 3);
 }
}
```

In the fixed example, we've *segregated* the `IShape` interface into two smaller, more focused interfaces: `IShape2D` and `IShape3D`. Each shape class now implements only the interface that is relevant to its functionality.

This adheres to the Interface Segregation Principle by ensuring that clients are not forced to depend on methods that they do not use. Clients can now depend only on the interfaces that they need, promoting better code reuse and flexibility.

Next up, the fifth and final SOLID principle…

## Dependency Inversion Principle (DIP) in C#

> High-level modules should not depend on low-level modules. Both should depend on abstractions.

Dependency Inversion is the strategy of depending upon interfaces or abstract classes rather than upon concrete classes. This principle promotes decoupling between modules and promotes the use of interfaces or abstract classes to define dependencies, allowing for more flexible and testable code.

Let's start with an example violating the DIP and then we’ll correct it.

```csharp
public class Engine // Engine is our "low-level" module
{
 public void Start()
 {
   System.Console.WriteLine("Engine started.");
 }
}
```

```csharp
public class Car // Car is our "high-level" module
{
 private Engine engine;

 public Car()
 {
   this.engine = new Engine(); // Direct dependency on concrete Engine class
 }

 public void StartCar()
 {
   engine.Start();
   System.Console.WriteLine("Car started.");
 }
}
```

In this example:

* The `Car` class directly creates an instance of the `Engine` class, leading to a tight coupling between Car and Engine.
    
* If the `Engine` class changes, it may affect the `Car` class, violating the Dependency Inversion Principle.
    

The UML diagram below shows that `Car` depends on `Engine`:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbd6IZ4TfDmGCPIjsJJHTtEw7_WBxCP-H1cSme78Ze7qJq0fG6tQzNo7A-IbgnnruAZwMBhjuJoozA0rzA9RM35Pu9vWpk4I2Hp6Szk7Ns_kTFbu2oIIfHQa9ceBembsjN8EUlZLkQuB863NyzeeSn7qY?key=p75tPpeumlH4kqsSJuxz6w align="left")

But what do we mean by “high level” and “low level” classes?

**High-Level Class**: The high-level class is typically the one that represents the main functionality or business logic of the application. It orchestrates the interaction between various components and is often more abstract in nature.

In this example, the `Car` class can be considered the high-level class. It represents the main functionality related to starting the car and driving it. The `Car` class is concerned with the overall behavior of the car, such as controlling its movement.

**Low-Level Class**: The low-level class is usually one that provides specific functionality or services that are used by the high-level class. It typically deals with implementation details and is more concrete in nature.

In this example, the `Engine` class can be considered the low-level class. It provides the specific functionality related to starting the engine. The `Engine` class encapsulates the details of how the engine operates, such as ignition and combustion.

So in summary, the `Car` class is the high-level class, representing the main functionality of the application related to the car's behavior.

The `Engine` class is the low-level class, providing specific functionality related to the operation of the engine, which is used by the Car class.

**Fixing DIP:**

To adhere to the Dependency Inversion Principle, we introduce an abstraction (interface) between `Car` and `Engine`, allowing `Car` to depend on an abstraction instead of a concrete implementation.

```csharp
public interface IEngine
{
 void Start();
}
```

```csharp
public class Engine : IEngine
{
 public void Start()
 {
   System.Console.WriteLine("Engine started.");
 }
}
```

```csharp
public class Car
{
 private IEngine engine;

 public Car(IEngine engine)
 {
   this.engine = engine;
 }

 public void StartCar()
 {
   engine.Start();
   System.Console.WriteLine("Car started.");
 }
}
```

We can now *inject* any type of engine into `Car` implementations:

```csharp
var engine = new Engine(); // concrete implementation to be "injected" into the car

var car = new Car(engine);

car.StartCar();
```

From the UML diagram below, we can see that both objects now depend on the abstraction level of the interface. `Engine` has inverted its dependency on `Car`.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf2Wes5g5HoeLNGoo4weo-gO6AVdVJ1WbRZxUfTEXIFROup8qCeUiQ8l5CsrwXkC5I1_0i3Q5DyzN5wpXSgjol2_RNFysFKpjMyj4SdEI2lFOplOs-uCUxZGEWE9fI4sFzMKfQOvOx33HKViFcXoqTVmi2s2FcLvCobCCZAvA?key=hfr-bV5v9p97pXexBFuY1A align="left")

In this corrected example:

1. We define an interface `IEngine` representing the behavior of an engine.
    
2. The `Engine` class implements the `IEngine` interface.
    
3. The `Car` class now depends on the `IEngine` interface instead of the concrete `Engine` class.
    
4. Dependency injection is used to inject the `IEngine` implementation into the `Car` class, promoting loose coupling. Now, if we want to give a car a different type of engine, for example a `FastEngine`, we can inject that in instead. 
    
5. Now, if the implementation of the engine changes, it won't affect the `Car` class as long as it adheres to the `IEngine` interface.
    

Dependency Injection (DI) offers several advantages in software development:

* **Decoupling**: DI promotes loose coupling between components by removing direct dependencies. Components rely on abstractions rather than concrete implementations, making them more independent and easier to maintain.
    
* **Testability**: Dependency injection simplifies unit testing by allowing components to be easily replaced with mock or stub implementations during testing. This enables isolated testing of individual components without relying on their dependencies.
    
* **Flexibility**: DI provides flexibility in configuring and swapping dependencies at runtime. It allows different implementations of dependencies to be used interchangeably without modifying the client code, facilitating runtime customization and extensibility.
    
* **Readability and Maintainability**: By explicitly specifying dependencies in the constructor or method parameters, DI improves code readability and makes the codebase easier to understand. It also reduces the risk of hidden dependencies, leading to more maintainable and understandable code.
    
* **Reusability**: DI promotes component reusability by decoupling them from their specific contexts or environments. Components can be designed to be independent of the application framework or platform, making them more portable and reusable in different projects or scenarios.
    
* **Scalability**: DI simplifies the management of dependencies in large-scale applications by providing a standardised approach for dependency resolution. It helps prevent dependency hell and makes it easier to manage and scale complex systems.
    

Overall, dependency injection enhances modularity, testability, and maintainability of software systems, contributing to improved software quality and developer productivity.

## Conclusion

Congratulations – you now understand the extremely important SOLID principles. These principles are going to save you a lot of headaches during your software development career, and guide you towards creating beautiful, maintainable, flexible, testable software.

If you’d like to take your software development skills to the next level and learn:

* OOP principles: encapsulation, abstraction, inheritance, polymorphism, coupling, composition, composition vs inheritance, fragile base class problem.
    
* All 23 design patterns (“The Gang of Four Design Patterns”) with real world examples.
    
* Unified Modeling Language (UML): the standard way to model classes and the relationships between them.
    

Then check out my book:

[Mastering Design Patterns in C#: A Beginner-Friendly Guide, Including OOP and SOLID Principles on Amazon](https://www.amazon.com/Mastering-Design-Patterns-Beginner-Friendly-Principles/dp/B0DBZGQZMZ) (also available on [Gumroad](https://doabledanny.gumroad.com/l/ennyj)).

Hopefully this article helps you to become a better OOP software developer!

Thanks for reading,

[Danny](https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA) 😎
