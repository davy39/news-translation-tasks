---
title: How to Handle NullPointerException in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T17:09:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-nullpointerexception-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99be740569d1a4ca2181.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'By Aditya Sridhar

  If you have spent some time developing programs in Java, at some point you have
  definitely seen the following exception:

  java.lang.NullPointerException


  Some major production issues arise due to NullPointerException. In this article...'
---

By Aditya Sridhar

If you have spent some time developing programs in Java, at some point you have definitely seen the following exception:

```java
java.lang.NullPointerException
```

Some major production issues arise due to `NullPointerException`. In this article, we'll go over some ways to handle `NullPointerException` in Java.

## Simple Null Check

Consider the following piece of code:

```java
public static void main(String args[]) {
    String input1 = null;
    simpleNullCheck(input1);
}

private static void simpleNullCheck(String str1) {
    System.out.println(str1.length());
}
```

If you run this code as is, you will get the following exception:

```java
Exception in thread "main" java.lang.NullPointerException
```

The reason you are getting this error is because we are trying to perform the `length()` operation on `str1` which is `null`.

An easy fix for this is to add a null check on `str1` as shown below:

```java
private static void simpleNullCheck(String str1) {
    if (str1 != null) {
        System.out.println(str1.length());
    }
}
```

This will ensure that, when `str1` is `null`, you do not run the `length()` function on it.

But you may have the following question. 

### What if str1 is an important variable?

In that case you can try something like this:

```java
 private static void simpleNullCheck(String str1) {
    if (str1 != null) {
        System.out.println(str1.length());
    } else {
        // Perform an alternate action when str1 is null
        // Print a message saying that this particular field is null and hence the program has to stop and cannot continue further.
    }
}
```

The idea is that, when you expect a value to be `null`, its better to put a `null` check on that variable. And if the value does turn out to be `null`, take an alternative action.

This is applicable not only to strings, but to any other object in Java.

## Lombok Null Check

Now take the following example:

```java
public static void main(String args[]) {
    String input2 = "test";
    List<String> inputList = null;
    lombokNullCheck(input2, inputList, input2);
}

public static void lombokNullCheck(String str1, List<String> strList, String str2) {
    System.out.println(str1.length() + strList.size() + str2.length());
}
```

Here we have a function that accepts three arguments: `str1`, `strList`, and `str2`.

If any of these values turn out to be `null`, we do not want to execute the logic in this function at all.

### How do you achieve this?

This is where Lombok comes handy. In order to add the Lombok library in your code, include the following Maven dependency:

```xml
 <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.12</version>
            <scope>provided</scope>
 </dependency>
```

To learn more about Maven, check out [this article](https://adityasridhar.com/posts/how-to-get-started-with-maven).

Here's what the code would look like with the Lombok `null` check:

```java
public static void main(String args[]) {
    String input2 = "test";
    List<String> inputList = null;
    try {
        lombokNullCheck(input2, inputList, input2);
    } catch (NullPointerException e) {
        System.out.println(e);
    }

}

public static void lombokNullCheck(@NonNull String str1, @NonNull List<String> strList, @NonNull String str2) {
    System.out.println(str1.length() + strList.size() + str2.length());
}
```

Before every argument of the function we add `@NonNull` annotation.

Also when we call this function, we put a `try-catch` block around the function call to catch `NullPointerException`.

If any of the arguments given in the function turn out to be `null`, the function would throw a `NullPointerException`. This would then be caught by the `try-catch` block.

This ensures that, if any of the function arguments turn out to be `null`, then the logic in the function is not executed and we know the code won't behave unusually.

This can be done with a bunch of `null` check statements as well. But using Lombok helps us avoid writing multiple `null` check statements and makes the code look much cleaner. 

## Lists and Nulls

Say that you have a list and you want to print all elements in the list:

```java
List<String> stringList = new ArrayList<>();
stringList.add("ele1");
stringList.add("ele2");
if (stringList != null) {
    for (String element : stringList)
        System.out.println(element);
}
```

Before looping over the list, we need to put a `null` check on the list. 

If the `null` check is not present, then trying to loop over a `null` list will throw a `NullPointerException`.

## Maps and Nulls

Let's take the scenario where you need to access the value for a particular key in a map:

```java
Map<String, String> testMap = new HashMap<>();
testMap.put("first_key", "first_val");
if (testMap != null && testMap.containsKey("first_key")) {
    System.out.println(testMap.get("first_key"));
}
```

First we need to do a null check on the map object itself. If this is not done, and the map is `null`, then a `NullPointerException` is thrown. This is done using `testMap!=null`

Once that is done, check if a particular key is present before accessing it. You can check the presence of the key using `testMap.containsKey("first_key")`. If this is not done and the particular key is absent, then you will get the value as `null`. 

## Is it necessary to always add a Null Check?

If you know for certain that a particular variable can never be `null`, then you can avoid adding the `null` check. This maybe applicable in private functions where you can control the data going into function. 

But if you are not really certain about the nullability of an object, it is best to add a `null` check.

## **Code**

All the code discussed in this article can be found [in this Github repo](https://github.com/aditya-sridhar/java-handling-nulls-example).

## **Congrats **?****

You now know how handle `NullPointerException` in Java!

## **About the author**

I love technology and follow advancements in the field. I also like helping others with my knowledge of tech.

Feel free to read more of my articles on [my blog](https://adityasridhar.com/), connect with me on [LinkedIn](https://www.linkedin.com/in/aditya1811/), or follow me on [Twitter](https://twitter.com/adityasridhar18).


