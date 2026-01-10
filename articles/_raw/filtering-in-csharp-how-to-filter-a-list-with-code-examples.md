---
title: Filtering in C# – How to Filter a List with Code Examples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-12-21T21:45:12.000Z'
originalURL: https://freecodecamp.org/news/filtering-in-csharp-how-to-filter-a-list-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/ferenc-almasi-tvHtIGbbjMo-unsplash.jpg
tags:
- name: C
  slug: c
seo_title: null
seo_desc: "Filtering through a data set is one of the most basic operations a developer\
  \ should know how to perform. \nFiltering refers to the process of restricting the\
  \ result set to contain only those elements that satisfy a specified condition.\
  \ It is also know..."
---

Filtering through a data set is one of the most basic operations a developer should know how to perform. 

[Filtering](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/filtering-data) refers to the process of restricting the result set to contain only those elements that satisfy a specified condition. It is also known as selection. 

To be practical, imagine trying to search and collect oranges from a basket of fruits. That is **filtering**. 

In this article, we will see different ways to filter through a List<T> class.

Before we start filtering the List collection, we will create a public class called **Employee** that holds the employee details. 

The Employee class is like a blueprint that holds the details for each employee. It has private fields for the _name_, _id_, and _department_ of each employee. 

The **Employee** class also has _getter_ and _setter_ methods to be able to set and get the value of each of the private field. 

Here is the code that demonstrates what I was just explaining above:

```cs
    public class Employee
    {
        private string _name;
        private int _id;
        private string _department;
         
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public int Id
        {
            get { return _id; }
            set { _id = value; }
        }

        public string Department
        {
            get { return _department; }
            set { _department = value; }
        }
    }

```

Inside the Program class, let's create a method that will house a list using the **Employee** class already created above. Each employee will have an ID, a name, and a department.

```program.cs
 public static void ListOperations()
 {
 	List<Employee> employees = new List<Employee>()
    {
		new Employee(){ Id=1, Name="John Doe", Department="Software"},
        new Employee(){ Id=2, Name="Angela Su", Department="Sales"},
        new Employee(){ Id=3, Name="Frank Kelvin", Department="Marketing"},
        new Employee(){ Id=4, Name="Joe Dustin", Department="Sales"},
        new Employee(){ Id=5, Name="Glory GG", Department="Software"},
        new Employee(){ Id=6, Name="Antonella Cruz", Department="Marketing"},
        new Employee(){ Id=5, Name="Andrew Logan", Department="Software"},
        new Employee(){ Id=6, Name="Billy Cruz", Department="Marketing"},
        new Employee(){ Id=5, Name="Sally Jane", Department="Software"},
        new Employee(){ Id=4, Name="Jon Snow", Department="Sales"},
    };
}

```

The above code is the declaration of a list of employees in the **ListOperations method**. Our goal is to filter through the list to get the employees that work in the software department.

There are several ways to filter through a list in C#. Let's look at them now:

## How to filter through a list using the iterative method

In this method, you loop through a list and search for the member of each iteration that passes the condition. Below is a code sample that uses the iterative method:

```program.cs
Console.WriteLine("Filtering through the Employee list using the " +
                    "Iterative method");
//goal: Filter through the list to get employees in the company’s software //department
           
foreach (var employee in employees)
{
	if(employee.Department == "Software")
    {
    	Console.WriteLine(employee.Name);
    }
}

```

## How to filter through a list using the LINQ query syntax (Where clause)

Language-Integrated Query (LINQ) is a powerful way to retrieve data from data sources in C#. This method filters the list collection and returns a new collection based on a given criterion.

```program.cs
Console.WriteLine("\nWhere clause - LINQ query syntax ");
var filteredResults = from employee in employees
						where employee.Department == "Software"
                        select employee.Name;
            
//Looping through your filtered results
foreach(var result in filteredResults)
{
	Console.WriteLine(result);
}

```

In the above code, the **LINQ query syntax** uses the **where** operator to filter the employees who are working in the **Software** department from the **employees** list. We then loop through the filtered results to print our results to the console. 

## How to filter through a list using the LINQ method syntax (Where clause)  

Unlike the query syntax above, the **LINQ extension method** uses the lambda expression. The lambda expression is passed as a predicate. It is indeed a shortcut to the LINQ query syntax above. 

Below is a code sample that uses the **LINQ method syntax.**

```program.cs
Console.WriteLine("\nWhere clause - LINQ method syntax ");

var filteredResultsTwo = employees.Where(employee => employee.Department == "Software");

//Looping through your filtered results
foreach(var employee in filteredResultsTwo)
{
	Console.WriteLine(employee.Name);
}
```

In the above code, the **LINQ method syntax** is used to filter the **employees** list and return a new list of employees who are working in the **Software** department. It uses a lambda expression as a predicate function. We then loop through the filtered results to print our results to the console.         

The complete code for various methods of filtering a list is provided below:

```program.cs
namespace Linq
{
    public class Employee
    {
        private string _name;
        private int _id;
        private string _department;
         
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public int Id
        {
            get { return _id; }
            set { _id = value; }
        }

        public string Department
        {
            get { return _department; }
            set { _department = value; }
        }
    }


    internal class Program
    {
        //GOAL: Our goal is to filter through the list to get the employees
        //that work in the software department.

        public static void ListOperations()
        {
           List<Employee> employees = new List<Employee>()
           {
            new Employee(){ Id=1, Name="John Doe", Department="Software"},
            new Employee(){ Id=2, Name="Angela Su", Department="Sales"},
            new Employee(){ Id=3, Name="Frank Kelvin", Department="Marketing"},
           new Employee(){ Id=4, Name="Joe Dustin", Department="Sales"},
           new Employee(){ Id=5, Name="Glory GG", Department="Software"},
           new Employee(){ Id=6, Name="Antonella Cruz", Department="Marketing"},
           new Employee(){ Id=5, Name="Andrew Logan", Department="Software"},
           new Employee(){ Id=6, Name="Billy Cruz", Department="Marketing"},
           new Employee(){ Id=5, Name="Sally Jane", Department="Software"},
           new Employee(){ Id=4, Name="Jon Snow", Department="Sales"},
           };
            

         //1: Iterative method
       Console.WriteLine("Filtering through the Employee list using the " +
                    "Iterative method");            
            foreach (var employee in employees)
            {
                if(employee.Department == "Software")
                {
                    Console.WriteLine(employee.Name);
                }
            }


       //2: LINQ query syntax (using the Where clause)            
          Console.WriteLine("\nWhere clause - LINQ query syntax ");
            var filteredResults = from employee in employees
                                  where employee.Department == "Software"
                                  select employee.Name;
                    
            foreach(var result in filteredResults)
            {
                Console.WriteLine(result);
            }


       //3: LINQ method syntax (using the Where clause)            
         Console.WriteLine("\nWhere clause - LINQ method syntax ");
         var filteredResultsTwo = employees.Where(employee => employee.Department == "Software");
            foreach(var employee in filteredResultsTwo)
            {
                Console.WriteLine(employee.Name);
            }

        }

        static void Main(string[] args)
        {
            ListOperations();           
        }

    }
}


```

## Conclusion

Filtering allows you to select only those elements that meet a particular condition. In this article, we showed how to filter a list in C# using various methods.

I hope this article has given you enough information to filter the List<T> collections easily. 

**Happy coding!**

  

