---
title: How to Execute and Run Java Code from the Terminal
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-10T19:20:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-execute-and-run-java-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Run-Java-Using-The-Terminal---freeCodeCamp-Cover-image.jpg
tags:
- name: Java
  slug: java
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "If you work with Java, you've probably used one of the well known text\
  \ editors like Sublime Text, VS Code, Brackets, Atom, and Notepad++ as well as IDEs\
  \ like Apache NetBeans and IntelliJ IDEA. \nRunning code in your IDE is straightforward,\
  \ but you don..."
---

If you work with Java, you've probably used one of the well known text editors like Sublime Text, VS Code, Brackets, Atom, and Notepad++ as well as IDEs like Apache NetBeans and IntelliJ IDEA. 

Running code in your IDE is straightforward, but you don't often get to see how it executes your code (even though you can check the command in the terminal of course!). 

However, it is good practice to know how your code actually executes and provides the output it gives you. 

Many of you might have heard that experienced professional programmers also use the terminal to execute the programs. This gives them better clarity and helps them understand how the code is working, where it is returning the desired value, where the bug might be, and so on.

Whatever your purpose may be, executing Java code directly from the terminal is a very easy task. 

In this article, I will show you how you can execute Java directly from your favorite terminal window. Fear not! The procedure is quite easy, and after reading the entire article you should be able to run your own Java code in the terminal.

## How to Run Java Code in the Terminal

The process I am going to show you in this article is applicable to any operating system whether that is Windows, MacOS, or Linux.

I will be using the following Java code in the next step.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

## 📦 Step 1 – Go to the directory where your source code is

If you have already written your Java code in an editor, then simply go into that directory. You can go straight into the directory through your file manager if you want.

### How to go into the directory where the source code is: for Windows 🪟

Suppose I have the source code ( `Main.java` ) inside  `This PC` > `Documents` folder. I can simply go there through my file explorer.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Untitled.png)

Or, if I want, I can also go there using my terminal. I need to use `cd` to indicate that I want to **change directory**. 

In this case, I can use `cd "C:\Users\Md. Fahim Bin Amin\Documents"`. As my user name contains white spaces, I have used `"` `"` to enclose them. 

Then if I check all the files under that directory, then I will get the `Main.java` file as well.

I placed the `Main.java` file under my **D** drive this time. So I went in that directory using the `cd` command.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-022040.png)

I get my Java file in the terminal as well.

### How to go into the directory where the source code is: for Linux 🐧

You can go into the directory where you have kept your source code either by following the typical GUI way or from the terminal using the `cd` command as well.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124200.png)
_using the typical GUI way_

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124317.png)
_Using the `cd` command_

## 🧑‍💻How to Compile the Java Code

Before running our Java code, we need to compile it first. To compile a Java code/program, we get the class file. Then we need to execute/run the class file.

### How to compile Java code using the terminal

We need to use the command `javac file_name_with_the_extension`. For example, as I want to compile my `Main.java`, I will use the command `javac Main.java`. The `c` in `javac` indicates compile.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122312.png)

If the compilation process is successful, then we will not get any errors.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122345.png)

This will create the class file we need under the same directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122628.png)

Keep in mind that we run the **class** file, not the `.java` file.

The same process is applicable for all of the operating systems out there.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124951.png)
_in Linux OS_

## 🖥️ How to Run the Java Code

We run the `.class` file to execute the Java programs. For that, we use the command `java class_file_name_without_the_extension`. Like, as our `.class` file for this is `Main.class`, our command will be `java Main`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-125223.png)

The Java program has been executed successfully!

The exact same procedure is also applicable for the other operating systems as well.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-125317.png)
_in Linux OS_

## 🏅Bonus: How to Run a Java Program with Packages

A package basically means a folder. Earlier, I showed you how to use any regular Java code using the terminal. There, I did not use any packages inside the Java code. 

Now I will show you how you can run any Java code that has packages declared within it. This time, I will be using the following Java code.

```java
package myJavaProgram.Source;
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

In the first line, I have written the package as `package myJavaProgram.Source`. This indicates that I want to create a folder named `myJavaProgram`. Then, I want to create another folder under that named `Source`. Finally, I want to create the class file of my Java code inside the `Source` folder. 

The directory tree looks like this: **myJavaProgram > Source.** 

For compiling this type of Java code with the packages, we use the command `javac -d . file_name_with_the_extension`. 

As for now, I am using the `Main.java` file, so I will apply the command `javac -d . Main.java`. This will create a folder named **myJavaProgram**, then create another folder named **Source** under the **myJavaProgram** folder under the directory where my source file is now.

- The_Directory_Where_I_Have_Kept_My_Source_Code
	- `myJavaProgram` folder
		- `Source` folder

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134626.png)

It instantly creates the **myJavaProgram** folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134710.png)

Within the folder, it creates the **Source** folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134806.png)

Inside the Source folder, it creates our `.class` file. We need this file to run the Java program.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134853.png)

Now if we want to run the `.class` file, then we need to change the command a little, as we need to provide the directory of the `.class` file in the terminal window.

We use the command to run the Java program with packages, `java directory_of_the_class_file.the_class_file_name_without_the_extension`. 

As I am using `Main.java` and I need to run the `Main.class` file, my command will be `java myJavaProgram.Source.Main`. It will run the Java code like below. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-135226.png)

If you're wondering why we are changing the command now, it's because earlier, we did not declare any packages. So the Java compiler created the `.class` file within the directory where our source code was. So, we could get the `.class` file directly from there and execute the class file as well.

But if we declare packages inside the source code like this, then we are telling the compiler to create the `.class` file in another place (not within the directory where our source code currently is). This means that we do not get the class file directly there. 

As we want to run the class file, we need to tell the compiler explicitly where the class file currently is so that it can get the class file and execute it.

If you think that you might mess up this step, then you can copy the directory directly from your Java code.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-135404.png)

In line 1, we have declared the package directory (where we want the class file to be generated). So if we simply copy the directory and add the `.class` file name without the extension ( `.class` ) later with a period ( `.` ), then it satisfies the condition for executing any Java code that has packages declared in the source code.

The same process is also applicable for the other operating systems as well. I am providing screenshots from a Linux OS here:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-140017.png)
_Running Java codes having packages within a Linux Machine_

Great job! 👏 You can now run any Java code/programs directly using a terminal. 🥳

I have also created a video where I have shown all the processes mentioned above. You can check that out [here](https://www.youtube.com/watch?v=e_lmKSCH9YE). 😁

## 💁‍♂️ Conclusion

I hope this article helps you run your Java programs just using the terminal. 

➡️	If you want to know how to install a Java compiler for your Windows operating system, [then you can check out this article](https://www.freecodecamp.org/news/how-to-install-java-on-windows/).

➡️	If you want to know how to install C and C++ compilers for your Windows operating system, [then you can check out this article](https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/).

➡️	If you want to know how to install Python on your Windows OS, [then you can check out this article](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/).

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

