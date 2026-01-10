---
title: How Inheritance Works in C# – with Code Examples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-11-29T20:04:11.000Z'
originalURL: https://freecodecamp.org/news/inheritance-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/caspar-camille-rubin-fPkvU7RDmCo-unsplash.jpg
tags:
- name: C
  slug: c
- name: inheritance
  slug: inheritance
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: "Inheritance is a branch of object-oriented programming that helps you write\
  \ reusable code. It allows you to extend the content of a class to another class.\
  \ \nOther pillars of object-oriented programming include encapsulation, polymorphism,\
  \ and abstrac..."
---

Inheritance is a branch of object-oriented programming that helps you write reusable code. It allows you to extend the content of a class to another class. 

[Other pillars of object-oriented programming](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/) include encapsulation, polymorphism, and abstraction. 

In this article, we will learn about inheritance in C# and the various types of inheritance we have in OOP.

## What is Inheritance?

Inheritance is one of the key features of object-oriented programming (OOP). It is simply the process by which one class (the child or derived class) acquires the properties, methods, and fields of another class (the base, parent, or super class).

Inheritance in object-oriented programming means that you're creating classes that can pass down their properties to other classes without having to explicitly define the properties in new classes. 

Inheritance does not only ensure the reusability of the codebase, but it also reduces your code’s complexity.

## Types of Inheritance in C#

Inheritance allows you to build families of related classes. The base/parent class defines the common data for the child class to inherit it. You use the colon operator (:) to show inheritance between two classes.

```cs
using System;

namespace LearningInheritance
{
    class ParentClass
    {
        //...
    }
    class ChildClass:ParentClass
    {
        //..
    }
}
 

```

There are different types of inheritance in C#. We'll discuss them now.

### Single Inheritance in C#

Single inheritance usually occurs between two classes – the base class, and the derived class. It occurs when a class is inherited from a single-parent class. 

Below is a code sample that shows single inheritance in C#:

```cs
using System;

namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        public void displayParentClassDetails()
        {
            Console.WriteLine($"I am {name}");
            Console.WriteLine($"ID : {Id}");
        }
    }

    class ChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine($"This is my ID : {Id}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //accessing the inherited members from the child class
            ChildClass child = new ChildClass();
            child.getIdFromParentClass();
        }
    }
}


```

In the above code, we derived a subclass (ChildClass) from a super class (ParentClass). The ChildClass now has access to the fields and properties of the ParentClass through inheritance. We could easily access the inherited members from the ChildClass as seen above.

### Hierarchical Inheritance in C#

Hierarchical inheritance occurs when more than one derived class is created from a single-parent class.

```cs
namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        public void displayParentClassDetails()
        {
            Console.WriteLine($"I am {name}");
            Console.WriteLine($"ID : {Id}");
        }
    }

    class ChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine("Displaying from my Child Class");
            Console.WriteLine($"This is my ID : {Id}.");
        }
    }

    class AnotherChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine("Displaying from my other Child Class");
            Console.WriteLine($"This is my ID : {Id}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //accessing the inherited members in the parent class (from the child class)
            ChildClass child = new ChildClass();
            child.getIdFromParentClass();

            //accessing the inherited members in the parent class (from the other child class)
            AnotherChildClass anotherChild = new AnotherChildClass();
            anotherChild.getIdFromParentClass();
        }
    }
}
```

In the above code, we showed that we can derive more than one child class from a single parent class. 

The ChildClass and AnotherChildClass both inherit the fields and methods of the base class, ParentClass. This is called Hierarchical inheritance. The two child classes can therefore access the fields and methods of the parent class.

### Multi-level Inheritance in C#

Multi-level inheritance occurs when a class is derived from another derived class. It is simply a situation where a derived class is created and used as a base class for another class.

```cs
namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        //...
    }

    class ChildClass : ParentClass
    {
        //...
        //The Child class is the derived class in this case
    }

    class ThirdClass : ChildClass
    {
        //...
        //The ChildClass is the base class for the ThirdClass
    }

    class Program
    {
        static void Main(string[] args)
        {
            //...
        }
    }
}
```

In the above code, we also derived a subclass (ChildClass) from a super class (ParentClass). The ChildClass then acts as a base class for a sub-child class which was named ThirdClass.

### Multiple Inheritances – Interfaces in C#

Multiple inheritances are not supported in C#. But you can achieve it by using _interfaces_. 

Multiple inheritances allow a derived class to be inherited from multiple parent classes. You can see an example of how a child class can inherit from multiple interfaces that act like a parent class below:

```cs
namespace LearningInheritance
{    
    class Program
    {
        interface InterfaceA
        {
            //...
        }

        interface InterfaceB
        {
            //...
        }     
        
        class NewClass: InterfaceA, InterfaceB
        {
            //...            
        }
        
        static void Main(string[] args)
        {
            //...
        }
    }
}
```

## Conclusion

Inheritance is important because it helps keep your code clean. It makes it easier to build families of related classes. The child class can inherit all the fields, properties, and methods that are contained in the parent class except those classes that are declared as a private class. 

Through this article, I hope you have gained some insight about inheritance in C#.

Happy Coding.

