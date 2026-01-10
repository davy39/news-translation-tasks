---
title: How to get started with Maven
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:51:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-maven-36851d8cfd96
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e-MWm5xnFFpeo9it
tags:
- name: beginner
  slug: beginner
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Aditya Sridhar

  Maven is used very often in the industry and I felt it would be good to cover the
  basics in this article so that it can be used efficiently.

  This article will cover things like maven basics, maven plugins, maven dependencies,
  and ma...'
---

By Aditya Sridhar

Maven is used very often in the industry and I felt it would be good to cover the basics in this article so that it can be used efficiently.

This article will cover things like maven basics, maven plugins, maven dependencies, and maven build lifecycle.

### What is Maven

Maven was created to provide a standard way in which Projects can be built. One of its powerful features is dependency management.

**Maven is commonly used for dependency management, but it is not the only thing it is capable of doing.**

If you do not know what dependency management means, don’t worry?. I will cover that in this article as well.

### Installing Maven

You can Install Maven from [https://maven.apache.org/](https://maven.apache.org/)

Also ensure Maven is set in the PATH so that `mvn` comands work.

You can verify if it is installed and can be accessed using the command

```bash
mvn -v
```

Also ensure [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/) is set.

By default, Maven will use the jdk you provided in JAVA_HOME. This can be overridden, but for this article we will use the jdk provided in JAVA_HOME.

### Create your Maven Project

Normally an IDE like eclipse can be used to easily create maven projects. But in this artice I will be running the commands from the command line so that the steps are clearly understood.

Run the following command to Create the project.

```bash
mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.first.app -DartifactId=first-maven-app

```

Archetype in the above command is nothing but a sample project template. **groupdId** tells what group your project comes under and **artifactId** is the project name.

Once you run the above command, it may take maven a minute or so to download the necessary plugins and create the project.

A folder called first-maven-app is now created. Open the folder and you will see a file called **pom.xml**

### pom.xml

POM stands for Project Object Model. pom.xml has all the details about your project, and this is where you will tell maven what it should do.

The contents of this file are shown below:

```xml
 <project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.first.app</groupId>
  <artifactId>first-maven-app</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>first-maven-app</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

**groupdId** and **artifactId** are the same values we gave in the command line.

**packaging** is the package format of the artifact. Default value is **jar**. It can have other values as well like ear, war, tar and so on.

**version** indicates the version number of the artifact. If **SNAPSHOT** is present, then it indicates the version is still in dev and may not be stable. If the version number does not have **SNAPSHOT,** then it’s the actual release version.

**name** is the project name.

I will explain about dependencies and plugins in Maven below.

### Super POM

pom.xml as you can see is pretty small. The reason for this is that a lot of the configuration is present in something called Super POM which is maintained internally by Maven.

pom.xml extends Super Pom to get all the config present in super Pom.

One of the config present in Super Pom indicates the following:

* All java source code is present inside **src/main/java**
* All java test code is present inside **src/test/java**

I mention only this config here, since we will be dealing with both source code as well as test code in this article.

### Code

The entire code discussed here is available in this repo: [https://github.com/aditya-sridhar/first-maven-app](https://github.com/aditya-sridhar/first-maven-app)

Let’s add some simple Java code. Create the following folder structure:

**src/main/java/com/test/app/App.java**

**App.java** is the Java code we will be adding.

Copy the following code into App.java:

```java
package com.first.app;

import java.util.List;
import java.util.ArrayList;

public class App 
{
    public static void main( String[] args )
    {
        List<Integer> items = new ArrayList<Integer>();
        items.add(1);
        items.add(2);
        items.add(3);
        printVals(items);
        System.out.println("Sum: "+getSum(items));
    }

    public static void printVals(List<Integer> items){
        items.forEach( item ->{
            System.out.println(item);
        });
    }

    public static int getSum(List<Integer> items){
        int sum = 0;
        for(int item:items){
            sum += item;
        }
        return sum;
    }
}

```

This is simple code which has 2 functions.

But one thing to observe is, the code is using lambda expressions inside the forEach loop in **printVals** function.

Lambda expressions need at minimum Java 8 to run. But by default Maven 3.8.0 runs using Java version 1.6.

So we need to tell maven to use Java 1.8 instead. In order to do this we will use Maven Plugins.

### Maven Plugins

We will use the Maven Compiler Plugin to indicate which Java version to use. Add the following lines to pom.xml:

```xml
<project>
...
<build>
  <plugins>
     <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.0</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
  <plugins>
</build>
...
</project>
```

You can see that the Java **source** and **target** versions are set to **1.8**.

**Plugins basically get some action done in maven. The compiler plugin compiles the source files.**

The full pom.xml is available [here](https://github.com/aditya-sridhar/first-maven-app/blob/master/pom.xml).

**There are a lot of maven plugins available. By knowing how to use plugins well, Maven can be used to do amazing things.** ?

### Maven Dependencies

Normally while writing code, we will be using a lot of existing libraries. These existing libraries are nothing but dependencies. Maven can be used to manage dependencies easily.

In the pom.xml of our project you can see the following dependency:

```xml
 <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
```

This dependency is telling that we will be needing **junit**. Junit is used to write Unit Tests for Java code. Similarly a lot of other dependencies can be added.

Let’s say you want to handle JSON in the code. Then you can add the **gson** dependency as shown below:

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
```

You can search for Maven artifacts in [https://search.maven.org](https://search.maven.org/)

### Transitive Dependencies

Let’s say you add a dependency **A** to the Project. Now **A** depends on a dependency called **B**. **B** depends on a dependency called **C**.

Since you are using **A** in the project, you will also need **B** and **C**.

But fortunately, it is enough if you add only **A** in pom.xml. Because Maven can figure out that A depends on B and that B depends on C. So internally Maven will automatically download **B** and **C**.

Here **B** and **C** are transitive dependencies.

### Custom Maven Repository

All these dependencies are available in a Public Maven Central Repository [http://repo.maven.apache.org/maven2](http://repo.maven.apache.org/maven2)

It is possible that there are some artifacts which are private to your company. In this case, you can maintain a private maven repository within your organization. I won’t be covering this portion in this tutorial.

### Adding the test class

Since the junit dependency is present in the project, we can add test Classes.

Create the following folder structure:

**src/test/java/com/test/app/AppTest.java**

**AppTest.java** is the Test Class.

Copy the following code into AppTest.java:

```java
package com.first.app;
import junit.framework.TestCase;
import java.util.List;
import java.util.ArrayList;

public class AppTest extends TestCase
{
    public AppTest( String testName )
    {
        super( testName );
    }

    public void testGetSum()
    {
        List<Integer> items = new ArrayList<Integer>();
        items.add(1);
        items.add(2);
        items.add(3);
        assertEquals( 6, App.getSum(items) );
    }
}
```

This class tests the getSum() function present in the App Class.

### Maven Build Lifecycle and Phases

Maven follows a build lifecycle to build and distribute artifacts. There are three main lifecycles:

1. **Default lifecycle**: This deals with building and deploying the artifact.
2. **Clean lifecycle**: This deals with project cleaning
3. **Site lifecycle**: This deals with Site documentation. **Will cover this in a different article.**

A Lifecycle is made up of phases. Here are some of the important phases in the **default lifecycle:**

* **validate**: Checks if all necessary information is available for the project
* **compile**: Used to compile the source files. Run the following command to compile:

```bash
mvn compile
```

* After running this command, a folder called target is created with all the compiled files.
* **test**: Used to run all the unit tests present in the project. This is why the Junit dependency was needed. Using Junit, unit tests can be written. Test classes can be run using the command

```bash
mvn test
```

* **package**: This will run all the above phases and then package the artifact. Here it will package it into a **jar** file since pom indicates a jar is needed. Run the following command for this:

```bash
mvn package
```

* The **jar** file is created inside the **target** folder
* **verify**: This will ensure that quality criteria is met in the project
* **install**: This will install the package in a local repository. The local repository location is usually **${user.home}/.m2/repository**. Use the following command for this:

```bash
mvn install
```

* **deploy**: This is used to deploy the package to a remote repository

One more command which is commonly used is the clean command which is given below:

```bash
mvn clean
```

This command cleans up everything inside the **target** folder

### References

Maven’s Offical Guide: [https://maven.apache.org/guides/getting-started/](https://maven.apache.org/guides/getting-started/)

More about POM : [https://maven.apache.org/guides/introduction/introduction-to-the-pom.html](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html)

More about Build Lifecycle : [https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)

### Congrats ?

You know how to use Maven now. This article covered just the basics of pom, plugins, dependencies and build lifecycle. To know more about Maven check the links I have given above.

Happy Coding ?

### About the author

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

_Originally published at [adityasridhar.com](https://adityasridhar.com/posts/how-to-get-started-with-maven)._

