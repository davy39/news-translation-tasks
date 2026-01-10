---
title: Java for Beginners – How to Create Your First "Hello World" Program
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-06T16:08:13.000Z'
originalURL: https://freecodecamp.org/news/hello-world-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/altumcode-XMFZqrGyV-Q-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: Java
  slug: java
seo_title: null
seo_desc: "If you are learning a programming language, the first thing you do is print\
  \ something in the terminal/command prompt. \nAnd that first thing is likely printing\
  \ \"Hello World\" in the terminal. So that's what I'll show you how to do here if\
  \ you are learn..."
---

If you are learning a programming language, the first thing you do is print something in the terminal/command prompt. 

And that first thing is likely printing "Hello World" in the terminal. So that's what I'll show you how to do here if you are learning Java for the first time.

## 🫵 What You Need to Know First

Before you start writing Java code, there are a few things you should know.

First of all, Java source files have the extension `.java`. An extension is something that is appended at the end of the file name, and it indicates which type of file it really is. 

Different programming languages have different file extensions which help the compilers/interpreters identify which type of programming data the file contains. These extensions also help identify whether that specific compiler/interpreter can support that file format or not.

Second, you have to ensure that you have properly installed the Java compiler (JDK) on your computer. If you do not know anything about that, then simply check out [this article](https://www.freecodecamp.org/news/how-to-install-java-on-windows/) (if you are a Windows user).

Also, when we compile the Java source code ( `.java` file), it generates a `.class` file. Later we run the `.class` file. Since Java is a platform-independent language (which means you can run the Java program from any operating system if you have installed the necessary components there), you can simply run this `.class` file from any operating system you want!

You can use any text editors / IDEs you want. But I prefer [Visual Studio Code](https://code.visualstudio.com/) or [IntelliJ IDEA IDE](https://www.jetbrains.com/idea/).

And finally, the Java file name and the public class name should be identical.

## ✍️ How to Create Your First Java File

Now you'll learn how to create a Java file. In this example, I am going to create a file named `Main.java`.

You can write the following code in that file:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

Then simply run the code. If you use the `Code Runner` extension to run this code using VS Code, it will compile the code first and then create the `Main.class` file. Later it will run the `Main.class` file. 

As it does this automatically, you almost won't see any time delays. But if you want to become a better programmer and run the code from your terminal, then [make sure to check out this article](https://www.freecodecamp.org/news/how-to-execute-and-run-java-code/). 

### 😉 Code Explanation

In the code above, we used the public class, and the public class name needs to be identical to the `.java` filename. If you used a different file name, then the public class name will also need to be different. 

For example, if you are using `MyJavaFile.java`, then the public class would be like this: `public class MyJavaFile`. Java is a case-sensitive language, so make sure to check that the uppercase-lowercase letters are also identical.

Then we need the main method. The Java compiler always starts compiling from the main method. The main method is `public static void main(String[] args)`. 

For printing something in the terminal, we use the `print` method. Here the print method is `System.out.println("")`. You have to provide the thing that you want to print in the terminal in the double quotations. 

We use the semicolon ( `;` ) to specify the end of a statement. So we use the semicolon after each statement's end.

There you go! I'll discuss more tweaks and advanced cool topics in other articles. 😁

## 📹 Video Walkthrough

If you're the type of person who enjoys learning from videos, then I have also created a video just for you! Make sure to check it out: 

%[https://youtu.be/U__ljdoYDYY]

Also, I am putting together a playlist where I am publishing all Java-related content. Make sure to check the [playlist from here](https://www.youtube.com/playlist?list=PL7ZCWbO2Dbl44-HqGWnRl7u28Qb1ac-Jk) and get all the code from [this GitHub repository](https://github.com/FahimFBA/everything-of-java).

## 😀 Conclusion

Thanks for reading this entire article. I hope this helps you get started on your Java programming journey.

You can follow me on:

* GitHub: [FahimFBA](https://github.com/FahimFBA)
* LinkedIn: [fahimfba](https://www.linkedin.com/in/fahimfba/)
* Twitter: [Fahim_FBA](https://twitter.com/Fahim_FBA)
* YouTube: [Code With FahimFBA](https://www.youtube.com/@FahimAmin?sub_confirmation=1)
* Website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

If you want to support me, then [you can also buy me a coffee!](https://www.buymeacoffee.com/fahimbinamin)

Cover: Photo by [AltumCode](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/XMFZqrGyV-Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

