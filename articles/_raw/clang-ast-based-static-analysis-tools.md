---
title: How to Build a Clang AST-Based C++ Static Analysis Tool
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-11-30T19:01:21.000Z'
originalURL: https://freecodecamp.org/news/clang-ast-based-static-analysis-tools
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/ClangCover-2.jpg
tags:
- name: C++
  slug: c-2
- name: compilers
  slug: compilers
seo_title: null
seo_desc: 'Clang is a set of tools and projects that provides infrastructure for languages
  in the C family like C, C++, OpenCL, and CUDA. It is a part of the LLVM project.

  This article will show you how to use Clang''s front end libraries to build a simple
  stati...'
---

Clang is a set of tools and projects that provides infrastructure for languages in the C family like C, C++, OpenCL, and CUDA. It is a part of the [LLVM](https://www.llvm.org/) project.

This article will show you how to use Clang's front end libraries to build a simple static analysis tool which will operate on C++ source / header files. It will use the power of AST (Abstract Syntax Tree) traversal. 

An abstract syntax tree is a tree structure representing the syntactical structure of code. [Here](https://en.wikipedia.org/wiki/Abstract_syntax_tree) is a good explanation of how it works, and [here](https://astexplorer.net/) is a tool to help you explore the AST for a given piece of code. 

Here, I will teach you how you can use the Clang AST to find information about the code given to it to show you how powerful it is.

This article goes through everything step by step, and I’ll explain the terminology I'm using briefly at each step.

In the first section, you'll learn how to get the open source Clang project. Then, we'll explore how you can build a static analysis tool with a simple goal: to check if each `Class` defined in a source / header file starts with an uppercase character. We'll do this using Clang's frontend libraries which will analyze the C++ source AST. 

So go ahead and grab your favorite coding beverage, get comfortable, and read on!

Here's what we'll cover:

* [Prerequisites](#heading-prerequisites)
* [How to Get the Clang Project and Access the Front-end Libraries](#how-to-get-the-clang-project-and-access-front-end-libraries)
* [How to Create the Scaffolding for the Static Analysis Tool](#heading-how-to-create-the-scaffolding-for-the-static-analysis-tool)
* [Putting it All Together in Code](#heading-putting-it-all-together-in-code)
* [Summary](#heading-summary)

## Prerequisites

Before getting started, it would be beneficial to have a basic understanding of the following:

* Compilers: [this](https://en.wikipedia.org/wiki/Compiler#:~:text=In%20computing%2C%20a%20compiler%20is,language%20(the%20target%20language).) page is a good primer for beginners.
* C++ : For readers not familiar with C++, [Learn C++ Programming for Beginners – Free 31-Hour Course](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) is a helpful resource.
* Git: [Git Best Practices – A Guide to Version Control for Beginners](https://www.freecodecamp.org/news/how-to-use-git-best-practices-for-beginners/) is an excellent starting point.

## How to Get the Clang Project and Access the Front-end Libraries

Since `clang` and `llvm` are open source projects, they have very comprehensive documentation around how to get started with getting the code and building tools using them. 

You can check out the [Getting Started](https://llvm.org/docs/GettingStarted.html) page of the `llvm` project to get more information about this. I've referenced that in this article as well.

###1. Get the Clang project 

On a UNIX like terminal, clone the `llvm` Git project into your own directory. I'll call it `ast-anaylzer`.


1. `mkdir -p  ~/ast-analyzer; cd ~/ast-analyzer`
2. `git clone https://github.com/llvm/llvm-project.git` #Clone the llvm project source 


###2. Get the CMake build system and Ninja build tool

[CMake](https://cmake.org/) and [ninja](https://ninja-build.org/) work in conjunction to form a build system. `CMake` generates `build.ninja` files, which contain commands that tell `ninja` how to generate output targets. We’ll get into this more a little later.

####2.1 Get and install Ninja


Here are the steps you can follow to install Ninja:

1. `cd ~/ast-analyzer`
2. Clone the ninja source project with this command: `git clone https://github.com/martine/ninja.git` 
3. `cd ninja`
4. Checkout the release branch - this is the stable branch - with this command: `git checkout release`
5. `python3 configure.py –bootstrap` This prepares and creates a Ninja binary (`configure.py –help` will give you more information).
6. Install ninja with this command: `sudo cp ninja /usr/local/bin`. After this step, as a basic validity check, do `which ninja` to make sure it says /usr/local/bin/ninja.

####2.2. Get and install CMake

Here are the steps you can follow to install cmake:

1. `cd ~/ast-analyzer`
2. Clone the cmake project source code: `git clone git://cmake.org/stage/cmake.git`
3. `cd cmake`
4. Checkout the release branch - this is the stable branch - with this command: `git checkout release`.
5. Run the bootstrap script: `./bootstrap`. This prepares cmake to be built and installed on your host machine.
6. Build cmake from source with this command: `make`.
7. Then finally install cmake: `sudo make install`.



Once we’ve gotten Clang, we’ll build it and configure it so we can build Clang-based tools as well.

###3. Build Clang and configure it

Create a ‘build’ directory. This is where our build.ninja/ output binaries and so on will get created:

```
cd ~/ast-analyzer; mkdir -p build; cd build
```

Now we need to generate the `build.ninja file` in order to build Clang and also the tools in the directory from the project cloned earlier (`llvm/clang-tools-extra`). You can do this using `CMake` like this:

```
cmake -G Ninja ../llvm-project/llvm -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra" # Enable the clang-tools projects in our build as well
```

This should generate a build.ninja file, which I encourage you to open and check out the contents. You will see that it contains a list of targets followed by dependencies. For example, one of the targets may look something like this: 

```
#############################################
# Utility command for install-llvm-headers

build install-llvm-headers: phony CMakeFiles/install-llvm-headers llvm-headers
```

 We’ll also do this for the custom static analysis tool we build in the next steps.

###4. Build and install all targets specified in the build.ninja file

`   ninja; ninja install`

Okay, the setup is done and now we get to the fun part!

## How to Create the Scaffolding for the Static Analysis Tool

We’ll be building our tool as a part of the `clang-tools-extra` directory in `llvm-project/clang-tools-extra`. Let's go ahead and create that directory. We’ll call our tool `class-analyzer`.

```
mkdir ~/ast-analyzer/llvm-project/clang-tools-extra/class-analyzer
cd ~/ast-analyzer/llvm-project/clang-tools-extra/class-analyzer
```

Now we need to create a `CMakeLists.txt`. This is basically a file that tells the `CMake` build system to add the source files in this tool to the `build.ninja` file it will generate. This lets `ninja` know how to build our tool.

Our `CMakeLists.txt` file will look like this:

CMakeLists.txt

```
set(LLVM_LINK_COMPONENTS support)
set(CMAKE_CXX_COMPILER /usr/bin/clang++)  


add_clang_executable(class-analyzer
  ClassAnalzyer.cpp
  MyFrontendActionFactory.cpp
  MyFrontendAction.cpp
  MyASTConsumer.cpp
  )
target_link_libraries(class-analyzer
  PRIVATE
  clangAST
  clangFrontend
  clangTooling
  )
```

The first couple lines tell the build system that the compiler should be `/usr/local/bin/clang++` (the one just built in the previous steps).

The next `add_clang_executable` section tells the build system which source files to build as a part of our executable. We'll get more into the details of what each source file does soon. It also tells defines the name of the executable for the build system. Here it is called `class-analyzer` since it analyzes class names. 

The `target_link_libraries` section informs the build system about the Clang front end libraries we should be linking against. These are the libraries which really expose the power of Clang’s AST to the tool we'll build.

Clang's API documentation is a good place to start looking for hints on how we should start writing the `class-analyzer` tool. Another good place to start is by scanning the source code of the Clang project we cloned earlier, for other tools! `[clang-tools-extra](https://github.com/llvm/llvm-project/tree/main/clang-tools-extra)` has multiple examples – these have been a source of inspiration for the code written here.

So now, let's start with the code for our very first source file. This file is contains the `main()` function of the executable. It looks something like this:

```cpp

#include "clang/Tooling/CommonOptionsParser.h"
#include "clang/Tooling/Tooling.h"

#include "MyFrontendActionFactory.h"

#include <memory>

using namespace clang::tooling;
using namespace llvm;

static llvm::cl::OptionCategory toolCategory("class-analyzer <options>");

int main(int argc, const char** argv)
{
    // Use clang's argument parser infrastructure
    // This is used for giving clang tooling the path
    // to the source files passed in to the tool.
    // It also gets the compilation database - a collection
    // of the compiler options used in the invocation of the tool
    auto argsParser = CommonOptionsParser::create(
        argc, argv, toolCategory);
    if (!expectedArgsParser) {
        llvm::errs() << argsParser.takeError();
        return -1;
    }
    CommonOptionsParser& optionsParser
        = argsParser.get();
    ClangTool tool(optionsParser.getCompilations(),
                   optionsParser.getSourcePathList());
    auto myActionFactory
        = std::make_unique<MyFrontendActionFactory>();
   
    return tool.run(myActionFactory.get());
} 

```

This source file essentially creates a tool which runs a `clang` [`FrontendActionFactory`](https://clang.llvm.org/doxygen/classclang_1_1tooling_1_1FrontendActionFactory.html). Now to understand what `FrontendActionFactory` does, let's take a look at Clang's documentation for it. 

We see that it has a pure virtual method, 

```cpp
virtual std::unique_ptr<FrontendAction> create () = 0;
```

which returns an [`std::unique_ptr`](https://en.cppreference.com/w/cpp/memory/unique_ptr) to a `[FrontendAction](https://clang.llvm.org/doxygen/classclang_1_1FrontendAction.html)` object. `FrontendAction` is, in its essence, a class which allows callers to perform custom actions as Clang parses the AST of a translation unit given to it. A [translation unit](https://en.wikipedia.org/wiki/Translation_unit_(programming)) in simple words is the combined code given to the compiler to create an object file. It contains code included through all the header files + code in a C / C++ source file

 This will become clearer as we get further along in the article.

Now we come to writing our own `FrontendActionFactory` which you can call `MyFrontendActionFactory`. This is a very simple class which just overrides the `create()` virtual method. It looks like this:

```cpp
// Header file MyFrontendActionFactory.h
#pragma once

include<clang/Tooling/Tooling.h>


class MyFrontendActionFactory : public clang::tooling::FrontendActionFactory{
    public:
    MyFrontendActionFactory();
    std::unique_ptr<clang::FrontendAction> create() override;
};                                                         

// Source file MyFrontendActionFactory.cpp

#include "MyFrontendActionFactory.h"
#include "MyFrontendAction.h"

MyFrontendActionFactory::MyFrontendActionFactory() {

}

std::unique_ptr<clang::FrontendAction> MyFrontendActionFactory::create() {
    return std::make_unique<MyFrontendAction>();
}

```

Since `MyFrontendActionFactory::create()` needs to return an `std::unique_ptr` to `clang::FrontendAction`, we'll need to create a `clang::FrontendAction` object. 

If we look at the Clang documentation for [`FrontendAction`](https://clang.llvm.org/doxygen/classclang_1_1FrontendAction.html), we'll be particularly interested in looking at what we can do with the AST (Abstract Syntax Tree) of the source. 

We might spot the following method:

```cpp
virtual std::unique_ptr< ASTConsumer >
CreateASTConsumer (CompilerInstance &CI, StringRef InFile) = 0;
```

This is a virtual method that a class which inherits from FrontendAction can implement. It returns an [`ASTConsumer`](https://clang.llvm.org/doxygen/classclang_1_1ASTConsumer.html#details) which according to the documentation,

>  _"...is an abstract interface that should be implemented by clients that read ASTs."_

So, this method looks really promising if we want to create something that will let us read the Clang generated AST!

If we look at the `FrontendAction` documentation again, it shows us that `ASTFrontend` is a class that inherits from `FrontendAction`. We also learn that it is:

> "The Abstract base class to use for AST consumer-based frontend actions."

It only has one pure virtual method: `CreateASTConsumer()`. This seems promising, since...we might be able to create our own `ASTConsumer` object.

So, we start by reading through `ASTConsumer`'s [documentation](https://clang.llvm.org/doxygen/classclang_1_1ASTConsumer.html). We see that it has a virtual method

```cpp
virtual void
clang::ASTConsumer::HandleTranslationUnit(ASTContext &Ctx)
```

where the documentation states:

>  "`HandleTranslationUnit` - This method is called when the ASTs for entire translation unit have been parsed". 

This is exactly what we want. We can override this method to do interesting things with the parsed AST.

You might now be wondering – how exactly can we use the parameter passed to this function `ASTContext` to actually go through the AST? 

There's a class in the Clang front end API which can help us here: [`RecursiveASTVisitor`](https://clang.llvm.org/doxygen/classclang_1_1RecursiveASTVisitor.html). This is a class that does a depth-first traversal of the Clang AST and visits each node. It has methods such as `VisitDecl()`, `VisitStmt()` and so on which can help us go through virtually the whole source file's AST. 

It also has a method which is particularly interesting: [`TraverseDecl()`](https://clang.llvm.org/doxygen/classclang_1_1RecursiveASTVisitor.html#a99a9e941a07a015bc18d3613c5aa0914). This method recursively traverses through all the declarations starting from the root declaration given to it.

## Putting it All Together in Code

So now what we need to do is give `TraverseDecl()` the root declaration of our translation unit and it will traverse the entirety of it. We can define special 'hooks' which will get called as this traversal happens. One such hook is:

```cpp
bool VisitRecordDecl(const clang::RecordDecl *record);
```

This is called each time the `RecursiveASTVisitor` traverses through a `CXXRecordDecl` – which is Clang speak for a C++ class. We'll overload this method with our own version to do something interesting: getting the C++ Class' name and seeing if it starts with an upper-case character. 

Putting all this together, here's what we get:

```cpp
// MyFrontendAction.h header file
#pragma once

#include <clang/Frontend/FrontendAction.h>

class MyFrontendAction : public clang::ASTFrontendAction {
    protected:
        std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) override;
};    

// MyFrontendAction.cpp source file
#include "MyFrontendAction.h"
#include "MyASTConsumer.h"

std::unique_ptr<clang::ASTConsumer> MyFrontendAction::CreateASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) {
    return std::make_unique<MyASTConsumer>(ci, file);
}
```

```cpp

//MyASTConsumer.h header file

#pragma once

#include<clang/AST/ASTConsumer.h>
#include<clang/Frontend/CompilerInstance.h>

class MyASTConsumer : public clang::ASTConsumer {

public:
    MyASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) {}
    void HandleTranslationUnit(clang::ASTContext &context) override;
};

// MyASTConsumer.cpp source file

#include <clang/AST/RecursiveASTVisitor.h>
#include "MyASTConsumer.h"

#include <iostream>

static bool isFirstLetterUpperCase(const std::string &str) {
    return str.size() != 0 && std::isupper(str[0]);
}
class MyASTVisitor : public clang::RecursiveASTVisitor<MyASTVisitor> {
    public:
    bool VisitCXXRecordDecl(const clang::RecordDecl *record) {
        std::string name = record->getNameAsString();

        if (!isFirstLetterUpperCase(name)) {
            std::cout << "Record Decl : " << name
                      <<" doesn't start with uppercase! \n";
        }

        return true;
    }
    bool TraverseDecl(clang::Decl *decl)  {
        return
           clang::RecursiveASTVisitor<MyASTVisitor>::TraverseDecl(decl);
    }
};

void MyASTConsumer::HandleTranslationUnit(clang::ASTContext &ctx) {
    clang::TranslationUnitDecl *tuDecl = ctx.getTranslationUnitDecl();
    MyASTVisitor visitor;
    visitor.TraverseDecl(tuDecl);
}

```

Now to build, we just do:

`cd ~/ast-analyzer/build/;  ninja class-analyzer`

This builds the `class-analyzer` executable in the `build/bin` directory.

Now to test out the analyzer, we create a test.cpp source file:

```cpp
// test.cpp
class Test {
public:
 int a;
};

class testLower {
public:
 int b;
};

int main() {
        return 0;
}
```

Run `class-analyzer` on it:

```
bin/class-analyzer test.cpp
```

The output of this command is :

```
Record Decl : testLower doesn't start with uppercase!
```

We can use a multitude of such `Visit*` methods such as `VisitEnumDecl`, `VisitFunctionDecl`, `VisitVarDecl`, and so on to get valuable information about the source file and create our own tools. Just think about any tool which runs and performs actions on code or gives suggestions to the user. 

You may think that this seems like a lot of work for a small task. But think about the potential. For example, you could write a tool which automatically gives a user suggestions to improve their code style. Or you could create a tool which analyses C++ code and finds lines of code where there might be security vulnerabilities. 

The possibilities are endless. Clang's front-end libraries are extremely powerful and you can build many cool projects and tools with them.

## Summary

In this article, you learned how to get and use the rich collection of Clang's Front-end libraries to parse a C++ source AST. You can use these libraries to write interesting static code analysis tools. 

As this article showed, one of the most important parts of the journey of exploring Clang's libraries is the art of reading the API documentation and applying it to the problems your tools aim to solve. I hope you enjoyed the article! 

