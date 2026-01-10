---
title: Java String to Int – How to Convert a String to an Integer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-23T20:30:55.000Z'
originalURL: https://freecodecamp.org/news/java-string-to-int-how-to-convert-a-string-to-an-integer
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Untitled-design.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "By Thanoshan MV\nString objects are represented as a string of characters.\
  \ \nIf you have worked in Java Swing, it has components such as JTextField and JTextArea\
  \ which we use to get our input from the GUI. It takes our input as a string. \n\
  If we want to..."
---

By Thanoshan MV

String objects are represented as a string of characters. 

If you have worked in Java Swing, it has components such as JTextField and JTextArea which we use to get our input from the GUI. It takes our input as a string. 

If we want to make a simple calculator using Swing, we need to figure out how to convert a string to an integer. This leads us to the question – how can we convert a string to an integer?

In Java, we can use `Integer.valueOf()` and `Integer.parseInt()` to convert a string to an integer. 

## 1. Use Integer.parseInt() to Convert a String to an Integer

This method returns the string as a **primitive type int**. If the string does not contain a valid integer then it will throw a [NumberFormatException](https://docs.oracle.com/javase/7/docs/api/java/lang/NumberFormatException.html). 

So, every time we convert a string to an int, we need to take care of this exception by placing the code inside the try-catch block. 

Let's consider an example of converting a string to an int using `Integer.parseInt()`:

```java
        String str = "25";
        try{
            int number = Integer.parseInt(str);
            System.out.println(number); // output = 25
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Let's try to break this code by inputting an invalid integer:

```java
     	String str = "25T";
        try{
            int number = Integer.parseInt(str);
            System.out.println(number);
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

As you can see in the above code, we have tried to convert `25T` to an integer. This is not a valid input. Therefore, it must throw a NumberFormatException. 

Here's the output of the above code:

```java
java.lang.NumberFormatException: For input string: "25T"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.parseInt(Integer.java:615)
	at OOP.StringTest.main(StringTest.java:51)
```

Next, we will consider how to convert a string to an integer using the `Integer.valueOf()` method. 

## 2. Use Integer.valueOf() to Convert a String to an Integer

This method returns the string as an **integer object**. If you look at the [Java documentation](https://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#valueOf(java.lang.String)), `Integer.valueOf()` returns an integer object which is equivalent to a `new Integer(Integer.parseInt(s))`. 

We will place our code inside the try-catch block when using this method. Let us consider an example using the `Integer.valueOf()` method:

```java
        String str = "25";
        try{
            Integer number = Integer.valueOf(str);
            System.out.println(number); // output = 25
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Now, let's try to break the above code by inputting an invalid integer number:

```java
        String str = "25TA";
        try{
            Integer number = Integer.valueOf(str);
            System.out.println(number); 
        }
        catch (NumberFormatException ex){
            ex.printStackTrace();
        }
```

Similar to the previous example, the above code will throw an exception. 

Here's the output of the above code:

```java
java.lang.NumberFormatException: For input string: "25TA"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.valueOf(Integer.java:766)
	at OOP.StringTest.main(StringTest.java:42)
```

We can also create a method to check if the passed-in string is numeric or not before using the above mentioned methods. 

I have created a simple method for checking whether the passed-in string is numeric or not. 

```java
public class StringTest {
    public static void main(String[] args) {
        String str = "25";
        String str1 = "25.06";
        System.out.println(isNumeric(str));
        System.out.println(isNumeric(str1));
    }

    private static boolean isNumeric(String str){
        return str != null && str.matches("[0-9.]+");
    }
}
```

The output is:

```java
true
true
```

The `isNumeric()` method takes a string as an argument. First it checks if it is `null` or not. After that we use the `matches()` method to check if it contains digits 0 to 9 and a period character. 

This is a simple way to check numeric values. You can write or search Google for more advanced regular expressions to capture numerics depending on your use case. 

It is a best practice to check if the passed-in string is numeric or not before trying to convert it to integer. 

Thank you for reading. 

Post image by [🇸🇮 Janko Ferlič](https://unsplash.com/@itfeelslikefilm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/collections/139346/soul-care?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

You can connect with me on [Medium](https://mvthanoshan.medium.com/).

**Happy Coding!**

