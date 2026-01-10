---
title: JUnit Test with Maven in VSCode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-18T23:16:06.000Z'
originalURL: https://freecodecamp.org/news/cjn-junit-test-with-maven-in-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_8zPHl_wSifWv_DBOkYGEzQ.png
tags: []
seo_title: null
seo_desc: 'By Clark Jason Ngo

  Install VSCode

  Setup here: https://code.visualstudio.com/docs/setup/setup-overview

  Install and create a Maven project

  Full Installation Guide here: https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

  If you h...'
---

By Clark Jason Ngo

### **Install VSCode**

Setup here: [https://code.visualstudio.com/docs/setup/setup-overview](https://code.visualstudio.com/docs/setup/setup-overview)

### Install and create a Maven project

Full Installation Guide here: [https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)

If you have Maven installed, follow these steps:

**Generate the project**

```
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```

**Change into project directory**

```
cd my-app
```

**Build the project**

```
mvn package
```

**Test and compile the project**

```
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

**You should get an output with:**Hello World!

### Modify our project

Let’s start creating simple math functions

Search for `App.java` file and replace the contents with this code:

```java
package com.mycompany.app;

public class App 
{
  public static int add(int firstNumber, int secondNumber) {
    return firstNumber + secondNumber;
  }

  public static int multiply(int multiplicand, int multiplier) {
    return multiplicand * multiplier;
  }

  public static int divide(int dividend, int divisor) {
    if (divisor == 0)
      throw new IllegalArgumentException("Cannot divide by zero (0).");

    return dividend / divisor;
  }
  public static void main( String[] args )
  {
    System.out.println(App.add(3, 3)); 
  }
}
```

Search for `AppTest.java` and replace the contents with this code:

```java
package com.mycompany.app;

import static org.junit.Assert.assertTrue;

import org.junit.Assert;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );
    }
    @Test
    public void add_TwoPlusTwo_ReturnsFour() {
      // Arrange
      final int expected = 4;
  
      // Act
      final int actual = App.add(2, 2);
  
      // Assert
      Assert.assertEquals(expected, actual);
    }    
    @Test
    public void multiply_FourTimesTwo_ReturnsEight() {
      // Arrange
      final int expected = 8;
  
      // Act
      final int actual = App.multiply(4, 2);
  
      // Assert
      Assert.assertEquals(expected, actual);
    }        

    @Test
    public void divide_TenDividedTwo_ReturnsFive() {
      // Arrange
      final int expected = 5;
  
      // Act
      final int actual = App.divide(10, 2);
  
      // Assert
      Assert.assertEquals(expected, actual);
    }           
}
```

You can keep creating tests such as:

```java
@Test    
public void multiply_FiftyTimesTwo_ReturnsOneHundred() 
{      
  // Arrange      
  final int expected = 100;        
  // Act      
  final int actual = App.multiply(50, 2);        
  // Assert      
  Assert.assertEquals(actual, expected);    
}
```

**Build the project**

```
mvn package
```

Output:

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.mycompany.app.AppTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.026 s - in com.mycompany.app.AppTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
```

**Test and compile the project**

```java
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

Output:

```
6
Hello World!
```

An alternative way to run tests is by click _Run Test_ inside `AppTest.java`

In the example below, _Run Test_ is located just below code line 44.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TFBgactTWvK7ColY1YgxEw.png)

**View Tests and Test Report**

![Image](https://cdn-media-1.freecodecamp.org/images/1*uNAouJG881s3iP0rX2zeVw.png)

### Migrating JUnit 4 to JUnit 5

Change your `pom.xml` dependencies to:

```xml
  <dependencies>
      <dependency>
          <groupId>org.junit.jupiter</groupId>
          <artifactId>junit-jupiter-api</artifactId>
          <version>5.4.2</version>
          <scope>test</scope>
      </dependency>
      <dependency>
          <groupId>org.junit.jupiter</groupId>
          <artifactId>junit-jupiter-engine</artifactId>
          <version>5.4.2</version>
          <scope>test</scope>
      </dependency>
  </dependencies>
```

Change your `AppTest.java` into:

```java
package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );
    }
    @Test
    public void add_TwoPlusTwo_ReturnsFour() {
      // Arrange
      final int expected = 4;
  
      // Act
      final int actual = App.add(2, 2);
  
      // Assert
      assertEquals(expected, actual);
    }    
    @Test
    public void multiply_FourTimesTwo_ReturnsEight() {
      // Arrange
      final int expected = 8;
  
      // Act
      final int actual = App.multiply(4, 2);
  
      // Assert
      assertEquals(expected, actual);
    }        

    @Test
    public void divide_TenDividedTwo_ReturnsFive() {
      // Arrange
      final int expected = 5;
  
      // Act
      final int actual = App.divide(10, 2);
  
      // Assert
      assertEquals(expected, actual);
    }           
}
```

**Adding test coverage**

**Check the test coverage report**

In the VSCode open the Extension MarketPlace and search Coverage Gutters

![Image](https://cdn-media-1.freecodecamp.org/images/1*OjkwUa9oX9s8MNgTMG6WdQ.png)

Click install button

Open the pom.xml file under your root folder and replace the content with [http://bit.ly/2Df1Oj2](http://bit.ly/2Df1Oj2) to add one plugin support.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>

  <name>my-app</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.4.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.4.2</version>
        <scope>test</scope>
    </dependency>
  </dependencies>


  <build>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.2</version>
          <executions>
              <execution>
                  <goals>
                      <goal>prepare-agent</goal>
                  </goals>
              </execution>
              <execution>
                  <id>report</id>
                  <phase>prepare-package</phase>
                  <goals>
                      <goal>report</goal>
                  </goals>
              </execution>
          </executions>
        </plugin>
        <!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>
        <!-- default lifecycle, jar packaging: see https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_jar_packaging -->
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.8.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.22.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.5.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.8.2</version>
        </plugin>
        <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->
        <plugin>
          <artifactId>maven-site-plugin</artifactId>
          <version>3.7.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-project-info-reports-plugin</artifactId>
          <version>3.0.0</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

Open the terminal in the VSCode and run

```
mvn install
mvn clean jacoco:prepare-agent install jacoco:report
```

Open your `App.java` file under `main/java/com/mycompany/app` folder and click the Watch button to check the report

![Image](https://cdn-media-1.freecodecamp.org/images/1*eRmrtwQ23Gp6IGXRwphLvA.png)

Red bar: test code is not covered

Yellow bar: condition is not covered

Green bar: code is covered

Open the `index.html` file under your root folder/target/site/jacoco.

To open:

Then paste (Ctrl and V for Windows, Command and V for MacOS) the path in your browser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jj1o8eqXMZ27xK9crCng9w.png)

You can see a very detailed test coverage report:

![Image](https://cdn-media-1.freecodecamp.org/images/1*LIgnn-CgO6vR9hBhZZGvug.png)

Thanks for reading! =)

Want to learn the different types of software testing? [https://medium.com/@clarkjasonngo/easy-examples-for-black-white-and-gray-box-testings-fdceb2a8b664](https://medium.com/@clarkjasonngo/easy-examples-for-black-white-and-gray-box-testings-fdceb2a8b664)[**Clark Jason Ngo - Graduate Teaching Assistant - Technology Institute - City University of Seattle |…**](https://www.linkedin.com/in/clarkngo/)  
[_View Clark Jason Ngo's profile on LinkedIn, the world's largest professional community. Clark Jason has 9 jobs listed…_www.linkedin.com](https://www.linkedin.com/in/clarkngo/)

Test Coverage section contributor:[**Kevin Wang - Full Stack Software Engineer - Resonance Path Institute | LinkedIn**](https://www.linkedin.com/in/kevin-pwang/)  
[_Join LinkedIn Kevin is a master student in computer science who loves technologies and programming. He has a great…_www.linkedin.com](https://www.linkedin.com/in/kevin-pwang/)

