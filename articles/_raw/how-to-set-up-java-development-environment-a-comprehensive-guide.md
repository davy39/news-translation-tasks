---
title: How to Set Up Your Java Development Environment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-08T20:14:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-java-development-environment-a-comprehensive-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/How-To-Set-Up-Java-Development-Environment--A-Comprehensive-Guide-1.png
tags:
- name: ide
  slug: ide
- name: Java
  slug: java
seo_title: null
seo_desc: "By Jacob Isah \nSetting up an efficient Java development environment is\
  \ key if you're a Java dev. It helps streamline your coding process and makes you\
  \ more productive. \nIn this article, I will walk you through the important steps\
  \ you need to set up a..."
---

By Jacob Isah 

Setting up an efficient Java development environment is key if you're a Java dev. It helps streamline your coding process and makes you more productive. 

In this article, I will walk you through the important steps you need to set up a Java development environment. We'll cover how to install the Java Development Kit (JDK), the Integrated Development Environment (IDE), and configure the necessary tools and libraries. Let's dive in!

## How to Install the Java Development Kit (JDK)

To begin, you need to install the JDK, which includes the Java Runtime Environment (JRE) as well as development tools, like the Java compiler and debugger. 

Follow these steps below:

1. Visit the [official Oracle website](https://www.oracle.com/java/technologies/downloads/).
2. Download the latest version of the JDK that matches your operating system.
3. Run the installer and follow the on-screen instructions.
4. After installation, set the `JAVA_HOME` environment variable to the JDK installation directory.

### How to Set the `JAVA_HOME` Environment Variable 

#### Know the JDK Installation Directory

The first step you need to take before setting the `JAVA_HOME` environment variable, is to know the installation directory of the JDK. Take note of the path where the JDK is installed on your machine.

#### How to Access Environment Variables

To access the environment variables on your machine, follow the steps below:

1. On Windows: Right-click on the "This PC" or "My Computer" icon on your desktop or File Explorer and select "Properties." In the System window, click on "Advanced system settings" on the left-hand side. You can now copy the environment variables.
2. On macOS: Go to "System Preferences" and click on "Security & Privacy." Then, click on the "Privacy" tab and select "Full Disk Access" from the left-hand side. Click on the lock icon at the bottom left and enter your password to make changes. Now, you can copy the environment variables.

#### Set the `JAVA_HOME` Environment Variable

Depending on your operating system, follow the instructions below:

**Windows:**

1. In the System Properties window, click on the "Environment Variables" button.
2. In the "System Variables" section, click on the "New" button.
3. Set the "Variable name" as `JAVA_HOME`.
4. In the "Variable value" field, enter the path to the JDK installation directory. For example, if the JDK is installed in "C:\Program Files\Java\jdk1.8.0_XXX" (where XXX represents the specific update number), enter that path.
5. Click "OK" to save the changes.

**macOS:**

1. In the System Preferences window, click on "Security & Privacy" and navigate to the "Privacy" tab.
2. Scroll down and select "Full Disk Access" from the left-hand side.
3. Click on the "+" button and navigate to the Applications > Utilities folder.
4. Open the "Terminal" application and click "Open."
5. In the Terminal, enter the following command:

```java
echo export JAVA_HOME=/Library/Java/JavaVirtualMachines/{JDK_VERSION}/Contents/Home >> ~/.bash_profile
```

Replace `{JDK_VERSION}` with the actual version number of the installed JDK without the curly braces {}.

Then you can close the Terminal and you should be all set.

#### Verify the `JAVA_HOME`  Environment Variable

To ensure that the `JAVA_HOME` environment variable is set correctly, open a new terminal or command prompt window and enter the following command:

**For Windows:**

```java
echo %JAVA_HOME%
```

**For macOS:**

```java
echo $JAVA_HOME
```

The command above should display the path to the JDK installation directory that you previously set.

Congratulations! You have successfully set the `JAVA_HOME` environment variable to the JDK installation directory. This variable is now accessible to Java applications and tools on your system.

## Choose an Integrated Development Environment (IDE)

An IDE makes coding simple and gives you various features like code editing, debugging, and project management. 

There are many popular IDEs for Java development. I recommend IntelliJ because of its advanced refactoring tools.

You can download IntelliJ IDEA Community Edition or Ultimate Edition, depending on your requirements. Install it, and you will be guided through the setup process, including selecting key plugins and themes. If you are a student of any university, you can get the [Github Student Pack](https://education.github.com/students).

### How to Configure Your IDE

Once you have downloaded IntelliJ as your chosen IDE, you need to configure it to suit your needs. 

The following configurations are some of the things you can do once you have downloaded the IntelliJ IDE.

#### Set the JDK

You'll need to point your IntelliJ to the JDK installation directory so that it uses the correct Java version for compilation and execution.

Open IntelliJ IDEA and go to "File" in the menu bar, I am using Ubuntu to demonstrate this.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-14-13-13.png)

then select "Project Structure":

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-14-14-25.png)

In the Project Structure dialog, navigate to the "SDKs" section (under "Platform Settings") on the left-hand side.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-14-17-33.png)

Click the "+" button on the top  right-hand side to add a new JDK. You can see what this looks like from the screenshot above.

In the "Add JDK" dialog, locate and select the directory where your JDK is installed. I am on Ubuntu. 

```java
/usr/lib/jvm/java-11-openjdk-amd64
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-14-48-59.png)

The JDK installation directory typically has a structure like this: 

**Windows**

`C:\Program Files\Java\jdk1.x.x_xx`  

**macOS**

`/Library/Java/JavaVirtualMachines/jdk1.x.x_xx.jdk/Contents/Home`

Click "OK" to add the JDK.

After adding the JDK, go to the "Project" section (under "Project Settings") on the left-hand side of the Project Structure dialog.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-21-25-33.png)

In the "SDK" dropdown, select the JDK you just added.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-21-27-35.png)

If you want to set the JDK for a specific module, go to the "Modules" section (under "Project Settings") on the left-hand side, select the module, and then choose the JDK from the "Module SDK" dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-07-21-29-59.png)

Click "OK" to apply the changes and close the Project Structure dialog.

IntelliJ IDEA should now be configured to use the JDK you selected for compilation and execution of your Java projects.

#### Customize Editor Preferences

Adjust the code editor's font, indentation, and code style settings to match your coding style. This enhances readability and consistency.

#### Install Plugins

IntelliJ offers a wide range of plugins to extend functionality. Install plugins for version control systems (for example, Git), build tools (for example, Maven), icons, and any other tools you frequently use.

## Explore Additional Tools and Libraries

Java offers a vast ecosystem of tools and libraries that can enhance your development experience. 

Some popular options include:

1. JUnit: A unit testing framework for Java that helps write and execute tests to ensure code quality.
2. Apache Commons: A library containing reusable components and utilities, such as handling file operations, collections, and string manipulation.
3. Log4j: A logging framework that assists in generating log statements during runtime.

# Conclusion

In this article, you learned how to set up Java development environment that is tailored to your needs. 

Specifically, you learned how to install the JDK, select an IDE, configure it appropriately, and leverage build tools and libraries that will empower you to write efficient, high-quality Java code. 

Thanks for reading.

