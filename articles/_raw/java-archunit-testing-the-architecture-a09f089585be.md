---
title: How to test your Java project’s architecture with ArchUnit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T16:33:05.000Z'
originalURL: https://freecodecamp.org/news/java-archunit-testing-the-architecture-a09f089585be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T1255atSpmUxEhV_n4t9Yw.png
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'By Emre Savcı

  In this post, I will show you an interesting library called ArchUnit that I met
  recently. It does not test your code flow or business logic. The library lets you
  test your “architecture” including class dependencies, cyclic dependencies...'
---

By Emre Savcı

In this post, I will show you an interesting library called ArchUnit that I met recently. It does not test your code flow or business logic. The library lets you test your “architecture” including class dependencies, cyclic dependencies, layer accesses, naming conventions, and inheritance checking.

Here is the list of tests which we will write in this post:

* Cyclic Dependency Test
* Layer Access Test
* Class Location Test
* Method Return Type Test
* Naming Convention Test

So let's imagine a project with the package structure shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/eRqPRYi8fcrjbBal2M9vIqopIPnJcfOz6SX3)

Before writing tests for our architecture, as a start point, we decide that our controllers should not be accessed from any other class or package. Also conceptually we accept that controller names should end with the “…Controller” suffix.

Now it is time to get our hands dirty. Below, we start writing our first test. It allows us to check our naming convention.

#### **Naming Convention Tests**

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test.controllers")public class NamingConventionTests {    @ArchTest    ArchRule controllers_should_be_suffixed = classes()            .that().resideInAPackage("..controllers..")            .should().haveSimpleNameEndingWith("Controller");    }
```

When we run the test we see that it passes:

![Image](https://cdn-media-1.freecodecamp.org/images/FVYRmI5KiWe5B5VFE53v4F3x0tsoi2Q5dceD)

There are two types of tests with arc unit. One of them is like the one shown above. If we want, we can write tests using JUnit's `Test` annotation. Change the `RunWith` parameter to `JUnit4.class` and remove the `AnalyzeClasses` annotation.

In this way, we specify the packages to import using `ClassFileImporter` within ArcUnit.

```
@RunWith(JUnit4.class)public class NamingConventionTests {    @Test    public void controllers_should_be_suffixed() {        JavaClasses importedClasses = new ClassFileImporter().importPackages("com.test.controllers");        ArchRule rule = classes()                .that().resideInAPackage("..controllers..")                .should().haveSimpleNameEndingWith("Controller");        rule.check(importedClasses);    }}
```

Now, let's see what happens if we have a different suffix. Change `("Controller") to ("Ctrl")` and run:

![Image](https://cdn-media-1.freecodecamp.org/images/bpiNudC8z7TTx19wNbeoEauM3s00fGstkKuL)

The exception says that: “java.lang.**AssertionError**: **Architecture Violation** [Priority: MEDIUM] — Rule ‘classes that reside in a package ‘..controllers..’ should have a simple name ending with ‘Ctrl’’ was violated (1 time):  
the simple name of com.test.controllers.**FirstController does not end with ‘Ctrl’** in (FirstController.java:0)”

So far so good. We wrote our first test and it correctly runs. Now it’s time to jump to other tests.

#### **Class Location Tests**

Let's write another rule that makes sure that classes which have annotation **repositories** should be located in the **infrastructure** package.

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test")public class RepositoryPackageTest {    @ArchTest    public ArchRule repositories_should_located_in_infrastructure = classes()            .that().areAnnotatedWith(Repository.class)            .should().resideInAPackage("..infrastructure..");}
```

If we annotate other classes than infrastructure packages, the test raises an AssertionError.

#### **Method Return Type Tests**

Let's write some method checks. Suppose we decide that our controller methods should return a type BaseResponse.

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test.controllers")public class ControllerMethodReturnTypeTest {    @ArchTest    public ArchRule controller_public_methods_should_return = methods()            .that().areDeclaredInClassesThat().resideInAPackage("..controllers..")            .and().arePublic()            .should().haveRawReturnType(BaseResponse.class)            .because("here is the explanation");}
```

#### **Cyclic Dependency Tests**

In this day and age, cyclic dependency issues are handled by most of the IOC containers. It is a good thing to have some tool that tests it for us.

Now first create classes that have cyclic complexity:

![Image](https://cdn-media-1.freecodecamp.org/images/vRxbd6lmK0eHHl4s4UKELLZs1ldF4ir9yMV9)

```
package com.test.services.slice1;import com.test.services.slice2.SecondService;public class FirstService {    private SecondService secondService;    public FirstService() {        this.secondService = new SecondService();    }}
```

```
package com.test.services.slice2;import com.test.services.slice1.FirstService;public class SecondService {    private FirstService firstService;    public SecondService() {        this.firstService = new FirstService();    }}
```

FirstService and SecondService depend on each other, and it creates the cycle.

Now write a test for it:

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test")public class CyclicDependencyTest {    @ArchTest    public static final ArchRule rule = slices().matching("..services.(*)..")            .should().beFreeOfCycles();}
```

Running this test gives the below result:

![Image](https://cdn-media-1.freecodecamp.org/images/ltAIwJP2j1vgpYj79u9GtZIIi-rJWmJSvnpW)

Also, the result is the same as constructor injection.

#### **Layer Tests**

Now it is time to write a layer test which covers our layers.

```
@RunWith(JUnit4.class)public class LayeredArchitectureTests {    @Test    public void layer_dependencies_are_respected() {        JavaClasses importedClasses = new ClassFileImporter().importPackages("..com.test..");        ArchRule myRule = layeredArchitecture()                .layer("Controllers").definedBy("..com.test.controllers..")                .layer("Services").definedBy("..com.test.services..")                .layer("Infrastructure").definedBy("..com.test.infrastructure..")                .whereLayer("Controllers").mayNotBeAccessedByAnyLayer()                .whereLayer("Services").mayOnlyBeAccessedByLayers("Controllers")                .whereLayer("Infrastructure").mayOnlyBeAccessedByLayers("Services");        myRule.check(importedClasses);    }}
```

We make a violation of the above rules to see that our test fails — we inject a service into the repository.

```
package com.test.infrastructure;import com.test.services.SecondService;public class FirstRepository {    SecondService secondService;    public FirstRepository(SecondService secondService) {        this.secondService = secondService;    }}
```

When we run the test we will see that our repository violates the rules:

![Image](https://cdn-media-1.freecodecamp.org/images/ThVQipnz3IR6On5lGpClwNOZ0kTgnzg3q6WP)

#### Wrapping up

ArchUnit, as you see, ensures that your project has the right architecture. It helps you to keep the project structure clean and prevents developers from making breaking changes.

We have done a brief overview of the library. Besides all of its features, I think it would be great if ArchUnit would have some rules to test [hexagonal architecture](https://blog.octo.com/en/hexagonal-architecture-three-principles-and-an-implementation-example/), [cqrs](https://docs.microsoft.com/tr-tr/azure/architecture/guide/architecture-styles/cqrs) and some DDD concepts like aggregates, value objects, etc.

For curious ones, here is the code on Github:

[**mstrYoda/java-archunit-examples**](https://github.com/mstrYoda/java-archunit-examples)  
[_Contribute to mstrYoda/java-archunit-examples development by creating an account on GitHub._github.com](https://github.com/mstrYoda/java-archunit-examples)[**TNG/ArchUnit**](https://github.com/TNG/ArchUnit)  
[_A Java architecture test library, to specify and assert architecture rules in plain Java - TNG/ArchUnit_github.com](https://github.com/TNG/ArchUnit)[**Unit test your Java architecture**](https://www.archunit.org/)  
[_Start enforcing your architecture within 30 minutes using the test setup you already have._www.archunit.org](https://www.archunit.org/)

