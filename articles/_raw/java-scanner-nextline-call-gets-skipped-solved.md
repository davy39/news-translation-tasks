---
title: Java scanner.nextLine() Method Call Gets Skipped Error [SOLVED]
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-08-26T21:01:37.000Z'
originalURL: https://freecodecamp.org/news/java-scanner-nextline-call-gets-skipped-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/java-scanner-nextline-call-gets-skipped-solved.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Java
  slug: java
seo_title: null
seo_desc: 'There''s a common error that tends to stump new Java programmers. It happens
  when you group together a bunch of input prompts and one of the scanner.nextLine()
  method calls gets skipped – without any signs of failure or error.

  Take a look at the follo...'
---

There's a common error that tends to stump new Java programmers. It happens when you group together a bunch of input prompts and one of the `scanner.nextLine()` method calls gets skipped – without any signs of failure or error.

Take a look at the following code snippet, for example:

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.nextLine();

        System.out.printf("So %s. How old are you? ", name);
        int age = scanner.nextInt();

        System.out.printf("Cool! %d is a good age to start programming. \nWhat language would you prefer? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah! %s is a solid programming language.", language);

        scanner.close();

    }

}

```

The first `scanner.nextLine()` call prompts the user for their name. Then the `scanner.nextInt()` call prompts the user for their age. The last `scanner.nextLine()` call prompts the user for their preferred programming language. Finally, you close the scanner object and call it a day.

It's very basic Java code involving a `scanner` object to take input from the user, right? Let's try to run the program and see what happens.

If you did run the program, you may have noticed that the program asks for the name, then the age, and then skips the last prompt for the preferred programming language and abruptly ends. That's what we're going to solve today.

## Why Does the `scanner.nextLine()` Call Get Skipped After the `scanner.nextInt()` Call?

This behavior is not exclusive to just the `scanner.nextInt()` method. If you call the `scanner.nextLine()` method after any of the other `scanner.nextWhatever()` methods, the program will skip that call.

Well, this has to do with how the two methods work. The first `scanner.nextLine()` prompts the user for their name.

When the user inputs the name and presses enter, `scanner.nextLine()` consumes the name and the enter or the newline character at the end. 

Which means the input buffer is now empty. Then the `scanner.nextInt()` prompts the user for their age. The user inputs the age and presses enter.

Unlike the `scanner.nextLine()` method, the `scanner.nextInt()` method only consumes the integer part and leaves the enter or newline character in the input buffer.

When the third `scanner.nextLine()` is called, it finds the enter or newline character still existing in the input buffer, mistakes it as the input from the user, and returns immediately.

As you can see, like many real life problems, this is caused by misunderstanding between the user and the programmer.

There are two ways to solve this problem. You can either consume the newline character after the `scanner.nextInt()` call takes place, or you can take all the inputs as strings and parse them to the correct data type later on.

## How to Clear the Input Buffer After the `scanner.nextInt()` Call Takes Place

It's easier than you think. All you have to do is put an additional `scanner.nextLine()` call after the `scanner.nextInt()` call takes place.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.nextLine();

        System.out.printf("So %s. How old are you? ", name);
        int age = scanner.nextInt();

        // consumes the dangling newline character
        scanner.nextLine();

        System.out.printf("Cool! %d is a good age to start programming. \nWhat language would you prefer? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah! %s is a solid programming language.", language);

        scanner.close();

    }

}

```

Although this solution works, you'll have to add additional `scanner.nextLine()` calls whenever you call any of the other methods. It's fine for smaller programs but in larger ones, this can get very ugly very quick.

## How to Parse Inputs Taken Using the `scanner.nextLine()` Method

All the wrapper classes in Java contain methods for parsing string values. For example, the `Integer.parseInt()` method can parse an integer value from a given string.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.nextLine();

        System.out.printf("So %s. How old are you? ", name);
        // parse the integer from the string
        int age = Integer.parseInt(scanner.nextLine());

        System.out.printf("Cool! %d is a good age to start programming. \nWhat language would you prefer? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah! %s is a solid programming language.", language);

        scanner.close();

    }

}

```

This is a cleaner way of mixing multiple types of input prompts in Java. As long as you're being careful about what the user is putting in, the parsing should be alright.

## **Conclusion**

I'd like to thank you from the bottom of my heart for taking interest in my writing. I hope it has helped you in one way or another. 

If it did, feel free to share with your connections. If you want to get in touch, I'm available on [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

