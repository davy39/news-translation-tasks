---
title: Print Methods in Java – How to Print to the Terminal
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-19T14:28:53.000Z'
originalURL: https://freecodecamp.org/news/print-methods-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/tracy-adams-TEemXOpR3cQ-unsplash.jpg
tags:
- name: Java
  slug: java
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'If you''re learning Java, you probably started your coding journey by printing
  the "Hello World" program in the console. And that''s a great way to begin – but
  after that, you need to learn how print methods and functions actually work.

  Well, this arti...'
---

If you're learning Java, you probably started your coding journey by printing the "Hello World" program in the console. And that's a great way to begin – but after that, you need to learn how print methods and functions actually work.

Well, this article will show you how those print functions/methods actually work. You'll also learn the differences between the **`println`** and the **`print`** methods.

In Java, methods work like functions in other programming languages. But since Java developers typically prefer the term "Function", I am going to use that terminology as well for all of my Java-related articles. 

If you want to print something in the terminal, you need to use one of the print methods. There are actually three different print methods in Java. They are the **`print`**, **`printf`,** and **`println`** methods. We'll see how each of them works now.

## How to Use the `print` Method in Java

This is the most generic print method in Java, but developers only use it if they do not want to get any new line characters after printing the statement inside it. For example:

```java
System.out.print("Fahim");
System.out.print("Bin Amin");
```

The output would be like below:

```
FahimBin Amin
```

I have not specified any newline character explicitly here, so it will not generate any new line explicitly. So, we will not get any new lines after printing the first statement. 

If you do not know what escape sequences are and how they actually work, I have prepared this video for you. Make sure to watch it if you need a refresher.

### 🎥 Video Tutorial

%[https://youtu.be/QqtYTnNxkoM]

If you want to add any spaces between the two statements even though you want to print them on the same line, then you can simply add a trailing space in the first statement or a leading space in the second statement.

```java
System.out.print("Fahim ");
System.out.print("Bin Amin");
```

The output will be:

```
Fahim Bin Amin
```

So, the **print** method is the most basic print method that doesn't add any specific thing other than simply printing the statement inside the method.

## How to Use the `printf` Method in Java

You use the `printf` method to organize a statement differently. For example:

```java
double value = 5.984;
System.out.println(value);
System.out.printf("%.2f" , value);
```

The output is `5.98` because we have specified that we want to print exactly 2 digits after the radix (.) point. In those cases, we use the `printf` method. 

## How to Use the `println` Method in Java

This method is the most widely used print method in Java. Whenever we want to print a newline after printing the statement inside of the method, we use this **`println`** method. 

If you are using the "Extensions for Java" extension in the Visual Studio Code or if you are using the well known IntelliJ IDEA IDE, then you can get the full `println` method ( `System.out.println("")` ) in the editor by simply using the shortcut "sout".

Now, it is time for an example:

```java
System.out.println("Fahim");
System.out.println("Bin Amin");
```

The output is:

```
Fahim
Bin Amin
```

As I used the `println` methods in both statements, each statement provides a newline character after printing the statement inside of it. So, after printing `Fahim`, I am getting a new line – in that new line, I am getting `Bin Amin`.

### 🎥 Video Tutorial

You can watch the video I made for you to help you understand these print methods better:

%[https://youtu.be/_jfnI7yyaPo]

## Conclusion

Thanks for reading this entire article. I hope this helps you get started on your Java programming journey.

You can follow me on:

* GitHub: [FahimFBA](https://github.com/FahimFBA)
* LinkedIn: [fahimfba](https://www.linkedin.com/in/fahimfba/)
* Twitter: [Fahim_FBA](https://twitter.com/Fahim_FBA)
* YouTube: [Code With FahimFBA](https://www.youtube.com/@FahimAmin?sub_confirmation=1)
* Website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

If you want to support me, then [you can also buy me a coffee!](https://www.buymeacoffee.com/fahimbinamin)

Cover: Photo by [Tracy Adams](https://unsplash.com/@tracycodes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/java?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

