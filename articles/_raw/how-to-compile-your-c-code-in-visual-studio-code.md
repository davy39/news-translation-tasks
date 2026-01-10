---
title: How to compile your C++ code in Visual Studio Code
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-10-07T05:14:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/banner-1.png
tags:
- name: C++
  slug: c-2
- name: compilers
  slug: compilers
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'C++ is a statically-typed, free-form, (usually) compiled, multi-paradigm,
  intermediate-level general-purpose middle-level programming language.

  In simple terms, C++ is a sophisticated, efficient, general-purpose programming
  language based on C.

  It wa...'
---

C++ is a statically-typed, free-form, (usually) compiled, multi-paradigm, intermediate-level general-purpose middle-level programming language.

In simple terms, C++ is a sophisticated, efficient, general-purpose programming language based on C.

It was developed by [Bjarne Stroustrup](http://www.stroustrup.com/) in 1979.

One of C++'s main features is the compiler. This is used to compile and run C++ code.

> A compiler is a special program that processes statements written in a particular programming language like C++ and turns them into machine language or "code" that a computer's processor uses. ([Source](https://en.wikipedia.org/wiki/Compiler))

I actually wrote this article because I had a C++ assignment which required using a compiler. As usual, everyone was using the [CodeBlocks IDE](http://www.codeblocks.org/) and [Visual Studio IDE](https://visualstudio.microsoft.com/). But I was already used to Visual Studio Code for all my programming stuff.

I then set out to find a way of compiling C++ directly inside my own VsCode Editor, hence this article :).

In this article, I'll show you how to set up your compiler in VsCode and give you some links to some of the best C++ resources.

![Image](https://media0.giphy.com/media/3o7TKUM3IgJBX2as9O/giphy.gif align="left")

# Prerequisites

* Prior knowledge of C++  
    (I assume you're learning C++, about to start learning, or just reading this for fun. This article is not a C++ 101 tutorial – some understanding of C++ is needed.)
    
* Visual Studio Code Editor  
    Download [here](https://code.visualstudio.com/#alt-downloads) and read the setup docs for [Windows](https://code.visualstudio.com/docs/?dv=win), [Linux](https://code.visualstudio.com/docs/?dv=linux64_deb) and [Mac](https://code.visualstudio.com/docs/?dv=osx)
    
* **Internet connection (!important)**
    

### **Disclaimer!**

I will be using a Windows OS throughout this article, but I'll provide links to resources that will help those using other operating systems.

Now let's get started!

# Download and install a C++ compiler

* Head to www.mingw.org and click the “Download/Installer” link to download the MinGW setup file, or click [here](https://osdn.net/projects/mingw/downloads/68260/mingw-get-setup.exe/) for Windows, [here](http://www.mingw.org/wiki/LinuxCrossMinGW) for Linux, and [here](https://brewinstall.org/Install-mingw-w64-on-Mac-with-Brew/) for Mac
    

> MinGW, a contraction of "Minimalist GNU for Windows", is a minimalist development environment for native Microsoft Windows applications. ([Source](https://mingw.osdn.io/))

* After downloading, install MinGW and wait for the “MinGW Installation Manager” to show up.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture1.png align="left")

* When the “MinGW Installation Manager” shows up, click on `mingw32-gcc-g++` then select “Mark for Installation”
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture2.png align="left")

* In the menu at the top left corner, click on “Installation &gt; Apply Changes”
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture3.png align="left")

* Wait and allow to install completely. Ensure you have a stable internet connection during this process.
    

# Edit your PATH environment variable to include the directory where the C++ compiler is located

> PATH is an environment variable on Unix-like operating systems, DOS, OS/2, and Microsoft Windows, specifying a set of directories where executable programs are located. In general, each executing process or user session has its own PATH setting. - [Wikipedia](https://en.wikipedia.org/wiki/PATH_(variable))

After installing MinGW, it can be found in `C:\MinGW\bin`. Now you have to include this directory in your environment variable PATH. If you've been using computers for a while now you should know how to do this already, but if you don't, here are a few resources:

* Click [here](https://www.computerhope.com/issues/ch000549.htm) for a Windows OS guide
    
* Click [here](https://www.cyberciti.biz/faq/unix-linux-adding-path/) for Linux
    
* Click [here](https://hathaway.cc/2008/06/how-to-edit-your-path-environment-variables-on-mac/) for a Mac OS guide
    

# Install Code Runner extension in VS Code

Now we have our compiler set up, let's install Code Runner

Code Runner allows you to Run code snippet or code file for multiple languages:

> C, C++, Java, JavaScript, PHP, Python, Perl, Perl 6, Ruby, Go, Lua, Groovy, PowerShell, BAT/CMD, BASH/SH, F# Script, F# (.NET Core), C# Script, C# (.NET Core), VBScript, TypeScript, CoffeeScript, Scala, Swift, Julia, Crystal, OCaml Script, R, AppleScript, Elixir, Visual Basic .NET, Clojure, Haxe, Objective-C, Rust, Racket, AutoHotkey, AutoIt, Kotlin, Dart, Free Pascal, Haskell, Nim, D, Lisp, Kit, and custom command.

* Click [here](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) to download
    
* Or search in VsCode marketplace tab
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture4.png align="left")

* After installing restart VsCode
    
* Open your C++ file in Vscode. Here's a basic hello world program below:
    

```c++
#include <iostream>
using namespace std;
int main() 
{
    cout << "Hello world!";
    return 0;
}
```

Save this file as `test.cpp`

# Run your code using Code Runner

* Use the shortcut `Ctrl+Alt+N`
    
* Or press F1 and then select/type Run Code
    
* Or right-click the Text Editor and then click Run Code in the editor context menu
    

The code will run and the output will be shown in the Output Window. Open the output window with \`Ctrl+ shortcut.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture5.png align="left")

# To stop the running code

* Use the shortcut `Ctrl+Alt+M`
    
* Or press F1 and then select/type Stop Code Run
    
* Or right-click the Output Channel and then click Stop Code Run in the context menu
    

Hurray, you just successfully set up your C++ environment in VsCode!

# Conclusion

Here's a quick hint: By default, VsCode's output terminal is read-only. If you're running code that requires user input like:

```c++
#include <iostream>
using namespace std;

const double pi = 3.14159; 

void calculate()
{
  double area; 
  double radius;

  cout<<"Enter Radius: "<<endl; 
  cin>>radius;

  area = pi * radius * radius; 

  cout<<"area is: "<<area<<endl;
 }
 
int main()
{
  calculate(); 
  return 0;
}
```

you won't be able to type into the terminal, `Cannot edit in read-only terminal`.  
To fix this, you need to manually enable read-write.

* In VsCode, Go to File &gt; Preference &gt; Setting.
    
* In the User tab on the left panel, find the extensions section
    
* Scroll and find 'Run Code Configuration'
    
* Scroll and find a checkbox `Run in Terminal` (Whether to run code in Integrated Terminal) Check the box.
    

OR

* In your `setting.json` file, add:
    

```python
"code-runner.runInTerminal": true
```

Hurray, you're done and ready to roll :).

# C++ resources

Here are some C++ resources you can use to get started with learning C++

* [https://www.learncpp.com/](https://www.learncpp.com/)
    
* [https://www.codecademy.com/learn/learn-c-plus-plus](https://www.codecademy.com/learn/learn-c-plus-plus)
    
* [https://www.udemy.com/free-learn-c-tutorial-beginners/](https://www.udemy.com/free-learn-c-tutorial-beginners/)
    
* [https://www.sololearn.com/Course/CPlusPlus/](https://www.sololearn.com/Course/CPlusPlus/)
    
* [https://www.youtube.com/watch?v=vLnPwxZdW4Y](https://www.youtube.com/watch?v=vLnPwxZdW4Y)
    
* [https://www.tutorialspoint.com/cplusplus/cpp\_useful\_resources.htm](https://www.tutorialspoint.com/cplusplus/cpp_useful_resources.htm)
    
* [https://makeawebsitehub.com/learning-c/](https://www.tutorialspoint.com/cplusplus/cpp_useful_resources.htm)
    

# Credits

* [MinGW Project](http://www.mingw.org/)
    
* [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) by [Jun Han](https://marketplace.visualstudio.com/publishers/formulahendry)
    

Thank you for reading!
