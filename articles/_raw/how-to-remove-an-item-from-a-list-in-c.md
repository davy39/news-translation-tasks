---
title: How to Remove an Item from a List in C#
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-12-13T00:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-an-item-from-a-list-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/bernd-dittrich-d_3EKbSg1tg-unsplash.jpg
tags:
- name: C
  slug: c
- name: C#
  slug: csharp
seo_title: null
seo_desc: 'While building your application in C#, you might need to store and manipulate
  sets of data. The List class is a member of the System.Collections.Generic namespace
  and you use it to store multiple objects of the same datatype.

  The List class represent...'
---

While building your application in C#, you might need to store and manipulate sets of data. The **List<T>** class is a member of the **System.Collections.Generic** namespace and you use it to store multiple objects of the same datatype.

The **List<T>** class represents a collection of strongly typed lists of objects that can be accessed using an index. Its class contains various methods to search, sort, and manipulate lists. 

In this article, we are going to learn how to remove an item from a list in C#. There are different ways to remove an item from a list. Here you will learn how to remove an item from a **List<T>** class using the **Remove()** and the **RemoveAt()** method.

## How to Remove an Item From a List Using the Remove() Method

Let’s assume you already have an existing list of strings of first names.

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
        }
    }
}

```

You use the **Remove()** method to remove the first occurrence of the item in a list. It takes in a parameter as an item and removes the first occurrence of the item.

Below is a code snippet showing how to use the **Remove()** method to remove an item from a list:

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
            
            //Iterating through the list before calling the Remove() method
            foreach(string names in FirstName)
            {
                Console.WriteLine(names);                
            }

            //Remove method
            FirstName.Remove("John");            

            //Iterating through the list after calling the Remove() method
            foreach (string names in FirstName)
            {
                Console.WriteLine(names);
            }
        }
    }
}



```

In the code above, **FirstName.Remove(“John”)** removes the first item with the value **“John”**. We then looped through the list to see the content of our list before and after manipulation.

## How to Remove an Item From a List Using the RemoveAt() Method

Using the list we created, the **RemoveAt()** method takes an index as a parameter and removes the item at that index. Below is a code snippet showing how to use the **Remove()** method to remove an item from a list.

```program.cs
using System.Collections.Generic;

namespace Collections
{
    public class Program
    {
        static void Main(string[] args)
        {
            List<string> FirstName = new List<string>() { "John", "Jane", "Josh", "Debby", "Gilbert", "Joe" };
            
            //Iterating through the list before calling the RemoveAt() method
            foreach(string names in FirstName)
            {
                Console.WriteLine(names);                
            }

            //RemoveAt() method
            FirstName.RemoveAt(1);            

            //Iterating through the list after calling the RemoveAt() method
            foreach (string names in FirstName)
            {
                Console.WriteLine(names);
            }
        }
    }
}

```

In the code above, **FirstName.RemoveAt(1)** removes the item at index 1. It is necessary to know that the **RemoveAt()** method takes a zero-based index number (this means the positions/index starts at 0, not 1). We then looped through the list to see the content of our list before and after the list manipulation.

## Conclusion

In this article, we discussed how to remove an item from a **List<T>** class in C#. We also demonstrated two approaches with examples.  

I hope this article was helpful. **Happy coding!**

