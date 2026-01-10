---
title: How to Use the Print Function in Java
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-10-04T21:16:25.000Z'
originalURL: https://freecodecamp.org/news/how-does-print-work-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Print-Statement.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'Often, you''ll need to print something to the console output when you''re
  coding in Java. And the first thing that likely comes to your mind is the print
  function or print statement.

  But very few people know about the three different print functions/st...'
---

Often, you'll need to print something to the console output when you're coding in Java. And the first thing that likely comes to your mind is the print function or print statement.

But very few people know about the three different print functions/statements in Java. In this article, I am going to tell you about them and show you how they work, with examples.

## How to Use the `println()` Function in Java

The `println()` function adds a new line after printing the value/data inside it. Here, the suffix `ln` works as the newline character, `\n`. If you consider the following example:

```java
public class Main{
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

You might not figure out exactly what is happening under the hood as you are printing only one line, and you get the following output:

```
Hello World!
```

But if you try to print several different expressions using the `println()` then you'll see the difference clearly!

```java
public class Main{
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("Welcome to freeCodeCamp");
    }
}
```

Here, you can see that after executing the first print statement, it is adding one new line character ( `\n` ). So you are getting the second print statement, `Welcome to freeCodeCamp`, in the next line.

The whole output will be like below:

```
Hello World!
Welcome to freeCodeCamp
```

You can check out this video of mine where I talk about this `println()` function in detail.

%[https://youtu.be/_jfnI7yyaPo]

But, isn't there a way of avoiding the automatically generated newline character in the print function?

YES! There is. In that case, you'll want to use the `print()` statement.

## How to Use the `print()` Function in Java

For this function, let me use the example I have used just now. You should be able to see the difference right away:

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!");
        System.out.print("Welcome to freeCodeCamp");
    }
}
```

Here, you see that I used `print` instead of using `println` like I did earlier. The `print` doesn't add the additional `\n` (new line character) after executing the task in it. This means that you will not get any new line after executing any `print` statement like above.

The output will be like this:

```
Hello World!Welcome to freeCodeCamp
```

If you want, then you can also solve this issue using `\n` like below:

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!\n");
        System.out.print("Welcome to freeCodeCamp");
    }
}
```

This time, the `\n` will work as the new line character and you will get the second string in a new line. The output is like below:

```
Hello World!
Welcome to freeCodeCamp
```

You can also print the two strings using only one print statement like below:

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!\nWelcome to freeCodeCamp");
    }
}
```

The output will be the same this time:

```
Hello World!
Welcome to freeCodeCamp
```

## How to Use the `printf()` Function in Java

This `printf()` function works as a **formatted print function**. Think about the two scenarios given below:

Scenario 1: Your friend Tommy wants you to provide him your notebook's PDF via an email. You can simply compose an email, provide a subject as you like (such as, hey Tommy, it's Fahim). You can also avoid writing anything to the body part of the email and send that email after attaching the PDF with the email. As simple as that – you don't need to maintain any courtesy with your friend, right?

Scenario 2: You couldn't come to your class yesterday. Your professor asked you to provide the valid reasons with proof and submit the documents via an email. 

Here, you can't mail your professor like you did for you friend, Tommy. In this case, you need to maintain formality and proper etiquette. You have to provide a formal and legit subject and write the necessary information in the body part. Last but not least, you have to attach your medical records with your email after renaming them with the proper naming convention. Here, you formatted your email as the authority wants!

In the `printf()`function, we follow the second scenario. If we want to specify any specific printing format/style, we use the `printf()`function.

Let me give you a short example of how this works: 

```java
public class Main{
    public static void main(String[] args) {
        double value = 2.3897;
        System.out.println(value);
        System.out.printf("%.2f" , value);
    }
}
```

Here, I am declaring a double type variable named `value` and I am assigning `2.3897` to it. Now when I use the `println()` function, it prints the whole value with the 4 digits after the radix point.

This is the output:

```
2.3897
2.39
```

But after that, when I am using the `printf()` function, I can modify the output stream of how I want the function to print the value. Here, I am telling the function that I want exactly 2 digits to be printed after the radix point. So the function prints the rounded value up to 2 digits after the radix point.

In this type of scenario, we normally use the `printf()` function. But keep in mind that it has a wide variety of uses in the Java programming language. I will try to write a detailed article later based on that. 😄

## Conclusion

In this article, I have given you a very basic idea about the difference between three print functions in Java. 

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

