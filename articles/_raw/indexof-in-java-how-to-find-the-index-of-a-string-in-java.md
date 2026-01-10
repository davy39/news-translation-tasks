---
title: indexOf in Java – How to Find the Index of a String in Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-24T16:11:05.000Z'
originalURL: https://freecodecamp.org/news/indexof-in-java-how-to-find-the-index-of-a-string-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/index.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'A string is a collection of characters nested in double quotes. The indexOf
  method returns the index position of a specified character or substring in a string.

  In this article, we''ll see the syntax for the different indexOf methods. We''ll
  also look ...'
---

A string is a collection of characters nested in double quotes. The `indexOf` method returns the index position of a specified character or substring in a string.

In this article, we'll see the syntax for the different `indexOf` methods. We'll also look at some examples to help you understand and use them effectively to find the index of a character or substring in your Java code. 

## Syntax for the `indexOf` Method

The `indexOf` method has the following methods:

```java
public int indexOf(int char)
public int indexOf(int char, int fromIndex)
public int indexOf(String str)
public int indexOf(String str, int fromIndex)
```

Let's explain these parameters before seeing some examples:

* `char` represents a single character in a string.
* `fromIndex` signifies the position where the search for the index of a character or substring should begin. This is important where you have two characters/strings that have the same value in a string. With this parameter, you can tell the `indexOf` method where to start its operation from. 
* `str` represents a substring in a string. 

Don't worry if you don't yet understand how any of this works – the examples will make it all clear!

## How to Use the indexOf Method in Java

In the first example below, we'll find the index of a single character in a string. This example will help us understand the `public int indexOf(int char)` method.

### `indexOf(int Char)` Method Example

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    System.out.println(greetings.indexOf("o"));
    
    // 4
  }
}

```

In the code above, we got the index of the character "0" returned to us which is 4. We have two "o" characters but the index of the first one got returned. 

In the next example, we'll see how we can return the index of the second "o" in the next example.

If you're wondering how the index numbers are derived then you should note that the first character in a string has an index of zero, the second character has an index of one, and so on. 

### `indexOf(int Char, Int fromIndex)` Method Example

Here's an example that explains the `int indexOf(int char, int fromIndex)` method:

```
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    System.out.println(greetings.indexOf("o", 5));
    
    // 7
  }
}

```

In the example above, we are telling the `indexOf` method to begin its operation from the fifth index.

H => index 0

e => index 1

l => index 2

l => index 3

0 => index 4

Note that index 5 is not the character "W". The fifth index is the space between "Hello" and "World".

So from the code above, every other character that comes before the fifth index will be ignored. 7 is returned as the index of the second "o" character. 

### `Int indexOf(String Str)` Method Example

In the next example, we'll understand how the `public int indexOf(String str)` method which returns the index of a substring works.

```
public class Main {
  public static void main(String[] args) {
    String motivation = "Coding can be difficult but don't give up";
    
    System.out.println(motivation.indexOf("be"));
    
    // 11
  }
}

```

Wondering how we got 11 returned? You should check the last section to understand how indexes are counted and how spaces between substrings count as indexes as well. 

Note that when a substring is passed in as a parameter, the index returned is the index of the first character in the substring – 11 is the index of the "b" character.

### `indexOf(String Str, Int fromIndex)` Method Example

The last method – `public int indexOf(String str, int fromIndex)` – is the same as the `public int indexOf(int char, int fromIndex)` method. It returns an index from a specified position. 

Here is an example:

```java
public class Main {
  public static void main(String[] args) {
    String motivation = "The for loop is used for the following";
    
    System.out.println(motivation.indexOf("for", 5));
    
    // 21
  }
}

```

In the example above, we have specified that the method should start its operation from the fifth index which is the index that comes after the first "for" substring. 21 is the index of the second "for" substring.

Lastly, when we pass in a character or substring that doesn't exist in a string, the `indexOf` method will return a value of -1. Here is an example:

```java
public class Main {
  public static void main(String[] args) {
    String motivation = "The for loop is used for the following";
    
    System.out.println(motivation.indexOf("code"));
    
    // -1
  }
}

```

## Conclusion

In this article, we learned how to use the four `indexOf` methods with an example explaining each of the different methods. 

We also saw what the syntax for each of these methods looks like and how they are able to tell the index to return. 

We ended by showing what happens when a character or substring that doesn't exist is passed in as a parameter.

Happy coding!

