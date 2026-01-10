---
title: C# Coding Best Practices – Coding Conventions with Examples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-13T16:31:30.000Z'
originalURL: https://freecodecamp.org/news/coding-best-practices-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kevin-ku-w7ZyuGYNpRQ-unsplash.jpg
tags:
- name: best practices
  slug: best-practices
- name: C
  slug: c
seo_title: null
seo_desc: "Coding conventions ensure that your code is consistent, readable, understandable,\
  \ and maintainable. \nWhen it comes to writing clean and quality code, there are\
  \ conventions developers should follow to make this possible. \nThere are a few\
  \ things you sh..."
---

Coding conventions ensure that your code is consistent, readable, understandable, and maintainable. 

When it comes to writing clean and quality code, there are conventions developers should follow to make this possible. 

There are a few things you should keep in mind while writing your code. In this article, we will learn about the best coding practices every C# developer should know.

## C# Naming Conventions

There are various naming conventions you should use when following best coding practices in C#. 

Using consistent naming conventions across a codebase can make it easier for developers to understand and navigate the code, and can help prevent naming conflicts and confusion. 

The following naming conventions are usually observed in C# programming.

### When to use Pascal case

When naming a **class**, **struct, method**, **property,** or **constant field**, Pascal casing is usually preferred.

```cs
namespace ExampleApp
{

    class ClassNamingConvention
    {
        public const string ConstantFieldNamingConvention = "C#";
        public string PropertiesNamingConvention { get; set; }

        public void MethodNamingConvention()
        {
            //type something here
        }
    }
}
```

When naming an interface, it is usually prefixed with the capital letter **I**. You can also use Pascal case when naming an interface.

```cs
public interface IInterfaceNamingConvention
{
        //type something here
}
```

### When to use Camel case

Camel cases are used when naming **method arguments, private fields,** and **local variables.** Private fields are usually prefixed with _.

```cs
private string _fieldsNamingConvention;

public void MethodNamingConvention(string methodArgsNamingConvention)
{
     string localVariables = "string here ...";            
}

```

### Use meaningful names for classes, methods, and properties

Always use meaningful and self-explanatory names for your classes, methods, and properties. It is good practice to name properties, methods, and classes with what they do. This way, just by reading the name, you can easily know what exactly it does.

```cs
class AppNotification
    {
        private string _appStatus;
        public string AppStatus
        {
            get { return _appStatus; }
            set { _appStatus = value; }
        }

        public static void SendNotification()
        {
            //type something here . . .
        }
    }

```

### Use meaningful names for LINQ query variables

Always use meaningful and self-explanatory names for your LINQ query variables, as seen in the example below.

```cs
public void QueryRacers()
{
     var racersInItaly = from racer in racers
                         where racer.City == "Lazio"
                         select racer.Name;
}

```

##   
C# Code Layouts and Comments

### How to declare member variables and fields

Always declare all your member variables and fields at the top of a class. When fields are declared at the top of a class, it is easy to see all the variables that the class is using and understand the class's overall state. 

It's also important to declare fields at the top of a class in C# because it makes the code more organized and readable, especially when working with large classes or when working with a team. This makes it easier for others to understand the code and make changes.

```cs
    class Car
    {
        private int _carSpeed;
        public int CarSpeed
        {
            get { return _carSpeed; }
            set { _carSpeed = value; }
        }

        public static void GetMaxSpeed()
        {
            //...
        }

        public static void GetMaxAcceleration()
        {
            //...
        }
    }

```

### Format and indent your code properly

When it comes to code layout, it is important to format and properly indent your code for readability and clean code organization. 

It is good practice to write only one statement per line. For example:

```cs
public void Numbers(int number)
{
       //Good practice
      if (number > 0)
      {
           Console.WriteLine(number);
       }

       //Bad practice
      if (
            number 
              < 0
          )
          {
              Console.WriteLine(number);
          }
  }

```

### How to write comments

It is good practice to start your comments with uppercase text and end with a period. 

Writing comments is helpful to the whole team. It makes code more readable, maintainable, and understandable. It is good practice to place comments on a new line, not at the end of your code. For example:

```cs
    class Car
    {
        public string Name { get; set; }
        //We place comments here.       
        //And end with a period.

        public void Move()
        {
            //...
        }
    }

```

## General C# Coding Best Practices

### How to compare a value to an empty string

Instead of " ", try `String.Empty` when comparing a value to an empty string. Using String.Empty improves code readability and makes it clear that the comparison is intended to be with an empty string. This makes it easier to understand and maintain the code in the future.

```cs
public void NameCheck(string name)
{
     if(name == String.Empty)
     {

      }
 }

```

### Use exception handling

Use exception handling to gracefully handle errors and exceptions. This helps prevent your code from crashing and makes it more robust. It is good practice to use a try-catch statement for most exception handling.

```cs
  public void NameCheck(string name)
    {
        try
        {
            //type code here
        }
        catch (Exception exception) { }
        {
            //type code here
        }
    }
```

### Use `&&` and `||` for better performance

To increase the performance of your application, it is good practice to use **&&** instead of **&** and **||** instead of **|** when you perform comparisons, as shown in the following example.

```cs
public void Numbers(int number)
{
   if (number > 2 && number < 4)
   {
       Console.WriteLine(number);
   }   
}
```

This is because the `&&` and `||` operators are known as "**short-circuit**" operators. This means that if the first operand of an `&&` operation is false, the second operand will not be evaluated because the overall expression must be false.

Similarly, if the first operand of an `||` operation is true, the second operand will not be evaluated because the overall expression must be true. 

This in turn increase the performance of your program.

### Limit methods to a single functionality

It is best to limit your methods to a single functionality. Do not try to combine multiple functionalities of a class into a single method. This ensures code readability and helps you avoid writing "spaghetti code".

```cs
    class AppNotification
    {        
        public void SendNotification()
        {
            //. . .
        }

        public void ReceiveNotification()
        {
            //. . .
        }

        public void MuteNotification()
        {
            //. . .
        }
    }

```

### Use enums for discrete values

Use [enums](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum) instead of using numbers and strings to indicate discrete values. Enums provide a way to improve the quality of your code by making it more readable, type-safe, and efficient. They also provide a way to define a set of named integral constants.

```cs
 class Car
    {
        public enum LoggerType
        {
            NewCars,
            UsedCars,
            Database
        }
        public void DisplayException(string message, LoggerType loggerType)
        {
            switch (loggerType)
            {
                case LoggerType.NewCars:
                    Console.WriteLine(LoggerType.NewCars);
                    break;

                case LoggerType.UsedCars:
                    Console.WriteLine(LoggerType.UsedCars);
                    break;

                case LoggerType.Database:
                    Console.WriteLine(LoggerType.Database);
                    break;

                default:
                    Console.WriteLine(message);
                    break;
            }
        }
    }

```

### How to compare string variables with user input

It is good practice to always convert string variables into uppercase or lowercase before comparing them with user input. 

This ensures that the comparison is case-insensitive. This makes your code more readable and maintainable as it eliminates the need for case-handling logic.

```cs
  class Car
    {
        public void DisplayTransactions()
        {
            string name = Console.ReadLine();

            if(name.ToLower() == "Joe")
            {
                //...
            }

            //Or.

            if (name.ToUpper() == "Joe")
            {
                //...
            }
        }
    }

```

## Conclusion

Coding conventions ensure readability and consistency within the team's and company’s codebase.

There are a lot of coding conventions in C# that help to ensure code quality. You can check the Microsoft .NET [documentation](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) to read more about coding conventions.

I hope you learnt a lot through this tutorial.

Happy Coding!

  


  

