---
title: The Best Java Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T00:31:00.000Z'
originalURL: https://freecodecamp.org/news/java-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f11740569d1a4ca40a6.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "What is Java?\nJava is a programming language developed by Sun Microsystems\
  \ in 1995, which later got acquired by Oracle. It’s now a full platform with lots\
  \ of standard APIs, open source APIs, tools, and a huge developer community. \n\
  It is used to build..."
---

## What is Java?

[Java](https://www.oracle.com/java/index.html) is a programming language developed by [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) in 1995, which later got acquired by [Oracle](http://www.oracle.com/index.html). It’s now a full platform with lots of standard APIs, open source APIs, tools, and a huge developer community. 

It is used to build the most trusted enterprise solutions by big and small companies alike. [Android](https://www.android.com/) application development is done fully with Java and its ecosystem. 

To learn more about Java basics, read [this](https://java.com/en/download/faq/whatis_java.xml) and [this](http://tutorials.jenkov.com/java/what-is-java.html).

## **Version**

The latest version is [Java 11](http://www.oracle.com/technetwork/java/javase/overview), which was released in 2018 with [various improvements](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html) over the previous version, Java 10. But for all intents and purposes, we will use Java 8 in this wiki for all tutorials.

Java is also divided into several “Editions” :

* [SE](http://www.oracle.com/technetwork/java/javase/overview/index.html) - Standard Edition - for desktop and standalone server applications
* [EE](http://www.oracle.com/technetwork/java/javaee/overview/index.html) - Enterprise Edition - for developing and executing Java components that run embedded in a Java server
* [ME](http://www.oracle.com/technetwork/java/embedded/javame/overview/index.html) - Micro Edition - for developing and executing Java applications on mobile phones and embedded devices

## **Installation : JDK or JRE ?**

Download the latest Java binaries from the [official website](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). Here you may face a question, which one to download, JDK or JRE? JRE stands for Java Runtime Environment, which is the platform dependent Java Virtual Machine to run Java codes, and JDK stands for Java Development Kit, which consists of most of the development tools, most importantly the compiler `javac`, and also the JRE. So, for an average user JRE would be sufficient, but since we would be developing with Java, we would download the JDK.

## **Platform specific installation instructions**

### **Windows**

* Download the relevant [.msi](https://en.wikipedia.org/wiki/Windows_Installer) file (x86 / i586 for 32bits, x64 for 64bits)
* Run the .msi file. Its a self extracting executable file which will install Java in your system!

### **Linux**

* Download the relevant [tar.gz](http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/) file for your system and install :

`bash $ tar zxvf jdk-8uversion-linux-x64.tar.gz`

* [RPM based Linux platforms](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) download the relevant [.rpm](https://en.wikipedia.org/wiki/RPM_Package_Manager) file and install :

`bash $ rpm -ivh jdk-8uversion-linux-x64.rpm`

* Users have the choice to install an open source version of Java, OpenJDK or the Oracle JDK. While OpenJDK is in active development and in sync with Oracle JDK, they just differ in [licensing](http://openjdk.java.net/faq/) stuff. However few developers complain of the stability of Open JDK.

### Instructions for **Ubuntu** :

Open JDK installation :  
`bash sudo apt-get install openjdk-8-jdk`

Oracle JDK installation :  
`bash sudo add-apt-repository ppa:webupd8team/java sudo apt-get update sudo apt-get install oracle-java8-installer`

### **Mac**

* Either download Mac OSX .dmg executable from Oracle Downloads
* Or use [Homebrew](http://brew.sh/) to [install](http://stackoverflow.com/a/28635465/2861269) :

```bash
brew tap caskroom/cask  
brew install brew-cask  
brew cask install java
```

### **Verify Installation**

Verify Java has been properly installed in your system by opening Command Prompt (Windows) / Windows Powershell / Terminal (Mac OS and *Unix) and checking the versions of Java runtime and compiler :

```text
$ java -version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)

$ javac -version
javac 1.8.0_66
```

**Tip** : If you get an error such as “Command Not Found” on either `java` or `javac` or both, dont panic, its just your system PATH is not properly set. For Windows, see [this StackOverflow answer](http://stackoverflow.com/questions/15796855/java-is-not-recognized-as-an-internal-or-external-command) or [this article](http://javaandme.com/) on how to do it. Also there are guides for [Ubuntu](http://stackoverflow.com/questions/9612941/how-to-set-java-environment-path-in-ubuntu) and [Mac](http://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/) as well. If you still can’t figure it out, dont worry, just ask us in our [Gitter room](https://gitter.im/FreeCodeCamp/java)!

## **JVM**

Ok now since we are done with the installations, let’s begin to understand first the nitty gritty of the Java ecosystem. Java is an [interpreted and compiled](http://stackoverflow.com/questions/1326071/is-java-a-compiled-or-an-interpreted-programming-language) language, that is the code we write gets compiled to bytecode and interpreted to run . We write the code in .java files, Java compiles them into [bytecodes](https://en.wikipedia.org/wiki/Java_bytecode) which are run on a Java Virtual Machine or JVM for execution. These bytecodes typically has a .class extension.

Java is a pretty secure language as it doesn’t let your program run directly on the machine. Instead, your program runs on a Virtual Machine called JVM. This Virtual Machine exposes several APIs for low level machine interactions you can make, but other than that you cannot play with machine instructions explicitely. This adds a huge bonus of security.

Also, once your bytecode is compiled it can run on any Java VM. This Virtual Machine is machine dependent, i.e it has different implementations for Windows, Linux and Mac. But your program is guranteed to run in any system thanks to this VM. This philosophy is called [“Write Once, Run Anywhere”](https://en.wikipedia.org/wiki/Write_once,_run_anywhere).

## **Hello World!**

Let’s write a sample Hello World application. Open any editor / IDE of choice and create a file `HelloWorld.java`.

```text
public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        System.out.println("Hello, World");
    }

}
```

**N.B.** Keep in mind in Java file name should be the **exact same name of the public class** in order to compile!

Now open the terminal / Command Prompt. Change your current directory in the terminal / Command Prompt to the directory where your file is located. And compile the file :

```text
$ javac HelloWorld.java
```

Now run the file using `java` command!

```text
$ java HelloWorld
Hello, World
```

Congrats! Your first Java program has run successfully. Here we are just printing a string passing it to the API `System.out.println`. We will cover all the concepts in the code, but you are welcome to take a [closer look](https://docs.oracle.com/javase/tutorial/getStarted/application/)! If you have any doubt or need additional help, feel free to contact us anytime in our [Gitter Chatroom](https://gitter.im/FreeCodeCamp/java)!

## **Documentation**

Java is heavily [documented](https://docs.oracle.com/javase/8/docs/), as it supports huge amounts of API’s. If you are using any major IDE such as Eclipse or IntelliJ IDEA, you would find the Java Documentation included within.

Also, here is a list of free IDEs for Java coding:

* [NetBeans](https://netbeans.org/)
* [Eclipse](https://eclipse.org/)
* [IntelliJ IDEA](https://www.jetbrains.com/idea/features/)
* [Android Studio](https://developer.android.com/studio/index.html)
* [BlueJ](https://www.bluej.org/)
* [jEdit](http://www.jedit.org/)
* [Oracle JDeveloper](http://www.oracle.com/technetwork/developer-tools/jdev/overview/index-094652.html)

## Basic Operations

Java supports the following operations on variables:

* **Arithmetic** : `Addition (+)`, `Subtraction (-)`, `Multiplication (*)`, `Division (/)`, `Modulus (%)`,`Increment (++)`,`Decrement (--)`.
* **String concatenation**: `+` can be used for String concatenation, but subtraction `-` on a String is not a valid operation.
* **Relational**: `Equal to (==)`, `Not Equal to (!=)`, `Greater than (>)`, `Less than (<)`, `Greater than or equal to (>=)`, `Less than or equal to (<=)`
* **Bitwise**: `Bitwise And (&)`, `Bitwise Or (|)`, `Bitwise XOR (^)`, `Bitwise Compliment (~)`, `Left shift (<<)`, `Right Shift (>>)`, `Zero fill right shift (>>>)`
* **Logical**: `Logical And (&&)`, `Logical Or (||)`, `Logical Not (!)`
* **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`
* **Others**: `Conditional/Ternary(?:)`, `instanceof`

While most of the operations are self-explanatory, the Conditional (Ternary) Operator works as follows:

`expression that results in boolean output ? return this value if true : return this value if false;`

Example: True Condition:

```java
    int x = 10;
    int y = (x == 10) ? 5 : 9; // y will equal 5 since the expression x == 10 evaluates to true
    
```

False Condition:

```java
    int x = 25;
    int y = (x == 10) ? 5 : 9; // y will equal 9 since the expression x == 10 evaluates to false
```

The instance of operator is used for type checking. It can be used to test if an object is an instance of a class, a subclass or an interface. General format- *object **instance** of class/subclass/interface*

Here is a program to illustrate instanceof operator:

```java
  Person obj1 = new Person();
        Person obj2 = new Boy();
 
        // As obj is of type person, it is not an
        // instance of Boy or interface
        System.out.println("obj1 instanceof Person: " +  (obj1 instanceof Person)); /*it returns true since obj1 is an instance of person */
                           
       
```

# Variable Examples

Variables store values. They are the most basic entity used to store data such as text, numbers, etc. in a program.

In Java, variables are strongly typed, which means you have to define the type for each variable whenever you declare it. Otherwise, the compiler will throw an error at compile time. Therefore, each variable has an associated ’data-type’ of one of the following:

Primitive Type: int, short, char, long, boolean, byte, float, double

Wrapper Type: Integer, Short, Char, Long, Boolean, Byte, Float, Double

Reference Type: String, StringBuilder, Calendar, ArrayList, etc.

You may have noticed that the Wrapper Type consists of types spelled exactly like the Primitive Type, except for the capitalised alphabet in the begining (like the Reference Type). This is because the Wrapper Types are actually a part of the more general Reference Types, but closely linked with their primitive counterparts via autoboxing and unboxing. For now, you just need to know that such a ‘Wrapper Type’ exists.

Typically, you can declare (i.e., create) variables as per the following syntax: <data-type> <variableName>;

```java
// Primitive Data Type
int i;

// Reference Data Type
Float myFloat;
```

You can assign a value to the variable either simultaneously when you are declaring it (which is called initialisation), or anywhere in the code after you have declared it. The symbol = is used for the same.

```java
// Initialise the variable of Primitive Data Type 'int' to store the value 10
int i = 10;
double amount = 10.0;
boolean isOpen = false;
char c = 'a'; // Note the single quotes

//Variables can also be declared in one statement, and assigned values later.
int j;
j = 10;

// initiates an Float object with value 1.0
// variable myFloat now points to the object
Float myFloat = new Float(1.0);

//Bytes are one of types in Java and can be
//represented with this code
int byteValue = 0B101;
byte anotherByte = (byte)0b00100001;
```

As evident from the above example, variables of Primitive type behave slightly differently from variables of Reference (& Wrapper) type - while Primitive variables store the actual value, Reference variables refer to an ‘object’ containing the actual value. You can find out more in the sections linked below.

# **Array**

An Array is a collection of values (or objects) of similar datatypes (primitive and reference both form of datatypes are allowed) held in sequencial memory addresses. An Array is used to store a collection of similar data types. Arrays always start with the index of 0 and are instantiated to a set number of indexes. All the variables in the array must be of the same type, declared at instantiation.

**Syntax:**

```java
dataType[] arrayName;   // preferred way
```

Here, `java datatype[]` describes that all the variables stated after it will be instantiated as arrays of the specified datatype. So, if we want to instantiate more arrays of the similar datatype, we just have to add them after the specified `java arrayName`(Don’t forget to separate them through commas only). An example is given below in the next section for reference.

```java
dataType arrayName[];  //  works but not preferred way
```

Here, `java datatype` describes only that the variables stated after it belong to that datatype. Besides, `java []` after the variable name describes that the variable is an array of the specified datatype (not just a value or object of that datatype). So, if we want to instantiate more arrays of the similar datatype, we will add the variables names just after the one already specified, separated by commas and each time we will have to add `java []` after the variable name otherwise the variable will be instantiated as an ordinary value-storing variable (not an array). For better understanding an example is given in the next section.

## **Code snippets of above syntax:**

```java
double[] list1, list2; // preferred way
```

Above code snippet instantiates 2 arrays of double type names list1 and list2.

```java
double list1[], list2; // works but not preferred way
```

Above code snippet an array of datatype double named list1 and a simple variable of datatype double named list2 (Don’t be confused with the name **list2**. Variables names have nothing to do with the type of variable).

Note: The style `double list[]` is not preferred as it comes from the C/C++ language and was adopted in Java to accommodate C/C++ programmers. Additionally it’s more readable: you can read that it’s a “double array named list” other than “a double called list that is an array”

## **Creating Arrays:**

```java
dataType[] arrayName = new dataType[arraySize];
```

## **Code snippets of the above syntax:**

```java
double[] List = new double[10];
```

## **Another way to create an Array:**

```java
dataType[] arrayName = {value_0, value_1, ..., value_k};
```

## **Code snippets of above syntax:**

```java
double[] list = {1, 2, 3, 4};

The code above is equivalent to:
double[] list = new double[4];
*IMPORTANT NOTE: Please note the difference between the types of brackets
that are used to represent arrays in two different ways.
```

## **Accessing Arrays:**

```java
arrayName[index]; // gives you the value at the specified index
```

## **Code snippets of above syntax:**

```java
System.out.println(list[1]);
```

Output:

```text
2.0
```

## **Modifying Arrays:**

```java
arrayName[index] = value; 
```

Note: You cannot change the size or type of an array after initialising it. Note: You can however reset the array like so

```java
arrayName = new dataType[] {value1, value2, value3};
```

## **Size of Arrays:**

It’s possible to find the number of elements in an array using the “length attribute”. It should be noticed here that `java length` is an **attribute** of every array i.e. a variable name storing the length of the variable. It must not be confused for a **method** of array since the name is same as the `java length()` method corresponding to String classes.

```java
int[] a = {4, 5, 6, 7, 8}; // declare array
System.out.println(a.length); //prints 5
```

## **Code snippets of above syntax:**

```java
list[1] = 3; // now, if you access the array like above, it will output 3 rather than 2
```

_Example of code:_

```java
int[] a = {4, 5, 6, 7, 8}; // declare array
for (int i = 0; i < a.length; i++){ // loop goes through each index
    System.out.println(a[i]); // prints the array
}
```

Output:

```java
    4
    5
    6
    7
    8
```

### **Multi-dimensional Arrays**

Two-dimensional arrays (2D arrays) can be thought of as a table with rows and columns. Though this representation is only a way to visualize the array for better problem-solving. The values are actually stored in sequential memory addresses only.

```java
int M = 5;
int N = 5;
double[][] a = new double [M][N]; //M = rows N = columns
for(int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
        //Do something here at index 
    }
}
```

This loop will execute M ^ N times and will build this:

[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[ 0 | 1 | 2 | 3 | 4 ]

Similarly a 3D array can also be made. It can be visualised as a cuboid instead of a rectangle(as above), divided into smaller cubes with each cube storing some value. It can be initialised follows:

```java
int a=2, b=3, c=4;
int[][][] a=new int[a][b][c];
```

In a similar manner, one can an array of as many dimensions as he/she wishes to but visualizing an array of more than 3 dimensions is difficult to visualize in a particular way.

### **Jagged Arrays**

Jagged arrays are multi-dimensional arrays that have a set number of rows but a varying number of columns. Jagged arrays are used to conserve memory use of the array. Here is a code example:

```java
int[][] array = new int[5][]; //initialize a 2D array with 5 rows
array[0] = new int[1]; //creates 1 column for first row
array[1] = new int[2]; //creates 2 columns for second row
array[2] = new int[5]; //creates 5 columns for third row
array[3] = new int[5]; //creates 5 columns for fourth row
array[4] = new int[5]; //creates 5 columns for fifth row
```

Output:

[0](https://guide.freecodecamp.org/java/arrays)   
[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[ 0 | 1 | 2 | 3 | 4 ]

# **Control Flow**

Control flow statements are exactly what the term means. They are statements that alter execution flow based on decisions, loops and branching so that the program can conditionally execute blocks of code.

Primarily, Java has the following constructs for flow control:

* `if`
* `if...else`

```java
if( <expression that results in a boolean> ){
    //code enters this block if the above expression is 'true'
}
```

```java
if( <expression that results in a boolean> ){
    //execute this block if the expression is 'true'
} else{
    //execute this block if the expression is 'false'
}
```

`switch`

Switch is an alternative for the `if...else` construct when there are multiple values and cases to check against.

```java
switch( <integer / String / Enum > ){
    case <int/String/Enum>: 
        <statements>
        break;
    case <int/String/Enum>:
        <statements>
        break;
    default:
        <statements>
}
```

Note: The program flow `falls through` the next `case` if the `break` statement is missing. e.g. Let’s say you say the standard ‘Hello’ to everyone at office, but you are extra nice to the girl who sits next to you and sound grumpy to your boss. The way to represent would be something like:

```java
switch(person){
    case 'boss': 
        soundGrumpy();
        break;
    case 'neighbour': 
        soundExtraNice();
        break;
    case 'colleague':
        soundNormal();
        break;
    default:
        soundNormal();
}
```

```text
Note: The `default` case runs when none of the `case` matches. Remember that when a case has no `break` statement, it `falls through` to the next case and will continue to the subsequent `cases` till a `break` is encountered. Because of this, make sure that each case has a `break` statement. The `default` case does not require a `break` statement. 
```

* `nested statements`

Any of the previous control flows can be nested. Which means you can have nested `if`,`if..else`and`switch..case`statements. i.e., you can have any combination of these statements within the other and there is no limitation to the depth of`nesting`.

For example, let’s consider the following scenario:

* If you have less than 25 bucks, you get yourself a cup of coffee.
* If you have more than 25 bucks but less than 60 bucks, you get yourself a decent meal.
* If you have more than 60 bucks but less than a 100, you get yourself a decent meal along with a glass of wine.
* However, when you have more than a 100 bucks, depending on who you are with, you either go for a candle lit dinner (with your wife) or you go to a sports bar (with your friends).

One of the ways to represent this will be:

```java
int cash = 150;
String company = "friends";

if( cash < 25 ){
    getCoffee();
} else if( cash < 60 ){
    getDecentMeal();
} else if( cash < 100 ){
    getDecentMeal();
    getGlassOfWine();
} else {
    switch(company){
        case "wife":
            candleLitDinner();
            break;
        case "friends": 
            meetFriendsAtSportsBar();
            break;
        default:
            getDecentMeal();
    }
}
```

In this example, `meetFriendsAtSportsBar()` will be executed.



# **Loops**

Whenever you need to execute a block of code multiple times, a loop will often come in handy.

Java has 4 types of loops:

# **While Loop**

The `while` loop repeatedly executes the block of statements until the condition specified within the parentheses evaluates to `false`. For instance:

```java
while (some_condition_is_true)
{
    // do something
}
```

  
Each ‘iteration’ (of executing the block of statements) is preceeded by the evaluation of the condition specified within the parentheses - The statements are executed only if the condition evaluates to `true`. If it evaluates to `false`, the execution of the program resumes from the the statement just after the `while`block.

**Note**: For the `while` loop to start executing, you’d require the condition to be `true` initially. However, to exit the loop, you must do something within the block of statements to eventually reach an iteration when the condition evaluates to `false` (as done below). Otherwise the loop will execute forever. (In practice, it will run until the [JVM](https://guide.freecodecamp.org/java/the-java-virtual-machine-jvm) runs out of memory.)

## **Example**

In the following example, the `expression` is given by `iter_While < 10`. We increment `iter_While` by `1`each time the loop is executed. The `while`loop breaks when`iter_While`value reaches `10`.

```java
int iter_While = 0;
while (iter_While < 10)
{
    System.out.print(iter_While + " ");
    // Increment the counter
    // Iterated 10 times, iter_While 0,1,2...9
    iter_While++;
}
System.out.println("iter_While Value: " + iter_While);
```

Output:

```
1 2 3 4 5 6 7 8 9
iter_While Value: 10
```


