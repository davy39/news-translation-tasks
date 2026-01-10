---
title: Test JUnit avec Maven dans VSCode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-18T23:16:06.000Z'
originalURL: https://freecodecamp.org/news/cjn-junit-test-with-maven-in-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_8zPHl_wSifWv_DBOkYGEzQ.png
tags: []
seo_title: Test JUnit avec Maven dans VSCode
seo_desc: 'By Clark Jason Ngo

  Install VSCode

  Setup here: https://code.visualstudio.com/docs/setup/setup-overview

  Install and create a Maven project

  Full Installation Guide here: https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

  If you h...'
---

Par Clark Jason Ngo

### **Installer VSCode**

Installation ici : [https://code.visualstudio.com/docs/setup/setup-overview](https://code.visualstudio.com/docs/setup/setup-overview)

### Installer et créer un projet Maven

Guide d'installation complet ici : [https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)

Si vous avez Maven installé, suivez ces étapes :

**Générer le projet**

```
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```

**Se déplacer dans le répertoire du projet**

```
cd my-app
```

**Construire le projet**

```
mvn package
```

**Tester et compiler le projet**

```
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

**Vous devriez obtenir une sortie avec :** Hello World!

### Modifier notre projet

Commençons par créer des fonctions mathématiques simples

Recherchez le fichier `App.java` et remplacez son contenu par ce code :

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

Recherchez `AppTest.java` et remplacez son contenu par ce code :

```java
package com.mycompany.app;

import static org.junit.Assert.assertTrue;

import org.junit.Assert;
import org.junit.Test;

/**
 * Test unitaire pour une simple App.
 */
public class AppTest 
{
    /**
     * Test rigoureux :-)
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

Vous pouvez continuer à créer des tests tels que :

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

**Construire le projet**

```
mvn package
```

Sortie :

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

**Tester et compiler le projet**

```java
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

Sortie :

```
6
Hello World!
```

Une autre façon d'exécuter les tests est de cliquer sur _Run Test_ dans `AppTest.java`

Dans l'exemple ci-dessous, _Run Test_ est situé juste en dessous de la ligne de code 44.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TFBgactTWvK7ColY1YgxEw.png)

**Voir les tests et le rapport de test**

![Image](https://cdn-media-1.freecodecamp.org/images/1*uNAouJG881s3iP0rX2zeVw.png)

### Migration de JUnit 4 vers JUnit 5

Modifiez les dépendances de votre `pom.xml` pour :

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

Modifiez votre `AppTest.java` en :

```java
package com.mycompany.app;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * Test unitaire pour une simple App.
 */
public class AppTest 
{
    /**
     * Test rigoureux :-)
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

**Ajout de la couverture de test**

**Vérifier le rapport de couverture de test**

Dans VSCode, ouvrez le MarketPlace des extensions et recherchez Coverage Gutters

![Image](https://cdn-media-1.freecodecamp.org/images/1*OjkwUa9oX9s8MNgTMG6WdQ.png)

Cliquez sur le bouton installer

Ouvrez le fichier pom.xml sous votre dossier racine et remplacez le contenu par [http://bit.ly/2Df1Oj2](http://bit.ly/2Df1Oj2) pour ajouter la prise en charge d'un plugin.

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

Ouvrez le terminal dans VSCode et exécutez

```
mvn install
mvn clean jacoco:prepare-agent install jacoco:report
```

Ouvrez votre fichier `App.java` sous le dossier `main/java/com/mycompany/app` et cliquez sur le bouton Watch pour vérifier le rapport

![Image](https://cdn-media-1.freecodecamp.org/images/1*eRmrtwQ23Gp6IGXRwphLvA.png)

Barre rouge : le code de test n'est pas couvert

Barre jaune : la condition n'est pas couverte

Barre verte : le code est couvert

Ouvrez le fichier `index.html` sous votre dossier racine/target/site/jacoco.

Pour ouvrir :

Collez (Ctrl et V pour Windows, Command et V pour MacOS) le chemin dans votre navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jj1o8eqXMZ27xK9crCng9w.png)

Vous pouvez voir un rapport de couverture de test très détaillé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LIgnn-CgO6vR9hBhZZGvug.png)

Merci d'avoir lu ! =)

Vous voulez apprendre les différents types de tests logiciels ? [https://medium.com/@clarkjasonngo/easy-examples-for-black-white-and-gray-box-testings-fdceb2a8b664](https://medium.com/@clarkjasonngo/easy-examples-for-black-white-and-gray-box-testings-fdceb2a8b664)[**Clark Jason Ngo - Graduate Teaching Assistant - Technology Institute - City University of Seattle |…**](https://www.linkedin.com/in/clarkngo/)  
[_View Clark Jason Ngo's profile on LinkedIn, the world's largest professional community. Clark Jason has 9 jobs listed…_www.linkedin.com](https://www.linkedin.com/in/clarkngo/)

Contributeur de la section Couverture de Test : [**Kevin Wang - Full Stack Software Engineer - Resonance Path Institute | LinkedIn**](https://www.linkedin.com/in/kevin-pwang/)  
[_Join LinkedIn Kevin is a master student in computer science who loves technologies and programming. He has a great…_www.linkedin.com](https://www.linkedin.com/in/kevin-pwang/)