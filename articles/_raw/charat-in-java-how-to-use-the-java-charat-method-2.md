---
title: charAt() in Java – How to Use the Java charAt() Method
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-31T16:10:26.000Z'
originalURL: https://freecodecamp.org/news/charat-in-java-how-to-use-the-java-charat-method-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/charAt.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "The charAt() method in Java returns the char value of a character in a\
  \ string at a given or specified index.\nIn this article, we'll see how to use the\
  \ charAt() method starting with it's syntax and then through a few examples/use\
  \ cases. \nHow to Use th..."
---

The `charAt()` method in Java returns the `char` value of a character in a string at a given or specified index.

In this article, we'll see how to use the `charAt()` method starting with it's syntax and then through a few examples/use cases. 

## How to Use the Java charAt() Method

Here is what the syntax for the `charAt()` method looks like: 

```java
public char charAt(int index)
```

Note that the characters returned from a string using the `charAt()` method have a `char` data type. We'll see how this affects concatenation of the returned values later in the article.

Now let's see some examples.

```java
public class Main {
  public static void main(String[] args) {
  
    String greetings = "Hello World";
    
    System.out.println(greetings.charAt(0));
    // H
  }
}
```

In the code above, our string – stored in a variable called `greetings` – says "Hello World". We used the `charAt()` method to get the character at index 0 which is H.

The first character will always have an index of 0, the second an index of 1, and so on. The space between substrings also counts as an index.

In the next example, we'll see what happens when we try to concatenate the different characters returned. Concatenation means joining two or more values together (in most cases, this term is used for joining characters or substrings in a string).

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    char ch1 = greetings.charAt(0); // H
    char ch2 = greetings.charAt(4); // o
    char ch3 = greetings.charAt(9); // l
    char ch4 = greetings.charAt(10); // d
    
    System.out.println(ch1 + ch2 + ch3 + ch4);
    // 391
  }
}
```

Using the `charAt()` method, we got the characters at index 0, 4, 9 and 10 which are H, o, l and d, respectively.

We then tried to print and concatenate these characters: `System.out.println(ch1 + ch2 + ch3 + ch4);`. 

But instead of getting "Hold" returned to us, we got 391. This happened because the returned values are no longer strings but have a data type of `char`. So when we concatenate them, the interpreter adds their [ASCII](https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html) value instead.

H has an ASCII value of 72, o has a value of 111, l has a value of 108, and d has a value of 100. When we add them together, we get 391 which was returned in the last example.

## StringIndexOutOfBoundsException Error

When we pass in an index number that exceeds the number of characters in our string, we'd get the StringIndexOutOfBoundsException error in the console. 

This error also applies to using negative indexing which is not supported in Java. In programming languages like Python that have support for negative indexing, passing in -1 will give you the last character or value in a data set, similar to how 0 always returns the first character.

Here is an example:

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    char ch1 = greetings.charAt(20); 
    
    System.out.println(ch1);
    
    /* Exception in thread "main" java.lang.StringIndexOutOfBoundsException: String index out of range: 20 
    */
  }
}



```

In the code above, we passed in an index of 20: `char ch1 = greetings.charAt(20);` which exceeds the number of characters in our `greetings` variable – so we got an error thrown at us. You can see the error message commented out in the code block above.

Similarly, if we pass in a negative value like this: `char ch1 = greetings.charAt(-1);`, we would get a similar error.

## Conclusion

In this article, we learned how to use the `charAt()` method in Java. We saw how to return characters in a string based on their index number and what happens when we concatenate these characters.

Lastly, we talked about some of the instances where we would get an error response while using the `charAt()` method in Java.

Happy coding!

