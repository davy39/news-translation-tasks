---
title: My favorite Java debugging techniques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-06T11:18:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-java-code-4a28442e0959
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E5604TZJQHsu3Yn6jXYPFA.jpeg
tags:
- name: debugging
  slug: debugging
- name: Java
  slug: java
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Bhuvan Gupta

  This article is about techniques which I have used to debug codeBases of various
  kinds, such as:


  CodeBase with high concurrent nature.

  CodeBase with a lot of proprietary (unsupported) libraries.

  CodeBase with a lot of deprecated/unwa...'
---

By Bhuvan Gupta

This article is about techniques which I have used to debug codeBases of various kinds, such as:

1. CodeBase with high concurrent nature.
2. CodeBase with a lot of proprietary (unsupported) libraries.
3. CodeBase with a lot of deprecated/unwanted code.
4. CodeBase with memory leaks.
5. CodeBase where every JVM can talk to every other JVM.

So let’s look at them one by one.

#### **CodeBase with high concurrent nature.**

It may happen that for serving a request, JVM uses many threads for eg:

```
Req -> tomcatThread-1 -> executorThread-2 -> BizThread-3->…`
```

Let say, we find that exception is coming in BizThread-3. Now as a debugger, we want to understand the Request flow. But the stacktrace will not be able to provide the complete request flow (for example, what happened in **executorThread-2** and what happened in **tomcatThread-1** and so on).

**Technique 1.1:** Write a [**custom java-agent**](https://www.baeldung.com/java-instrumentation) which will be used to effectively add `log.debug()` to the start and end of every method of certain java packages. This will give us some insight into what all is getting called.

**Technique 1.2:** In certain frameworks, if supported, use [**AOP**](https://www.journaldev.com/2583/spring-aop-example-tutorial-aspect-advice-pointcut-joinpoint-annotations) to proxy all methods and effectively add `log.debug()`.

#### **CodeBase with a lot of proprietary (unsupported) libraries.**

Sometimes we find ourself in a situation where, after hours of debugging, we nail the problem that _xyz-gov-secret_ library is misbehaving and this library is now unsupported.

**Technique 2.1:** Roll up your sleeves and install [**eclipse-decompiler**](https://marketplace.eclipse.org/content/enhanced-class-decompiler) and dive into the code base.

#### **CodeBase with a lot of deprecated/unwanted code.**

This is a classic one: we sometimes find ourselves in a method of 500+ lines with tons of deprecated if-else. Now, how do we figure out what is the code flow for a particular call, which if-else are going to use, and which is the dead code?

**Technique 3.1:** We can use a tool called [**jacoco agent**](https://www.eclemma.org/jacoco/trunk/doc/agent.html). It collects the execution details during runtime and can color-code the code in eclipse.  
Basically, it is the same tool, generally used in analyzing code coverage by JUnit Test.

#### **CodeBase with memory leaks.**

Every developer has a day when, in their local system, all goes good, in production OutOfMemory :(

**_Technique 4.1:_** JVM provides techniques to capture heap dumps in case of outOfMemory.

Add the following as an argument while starting the JVM   
[_-XX:+HeapDumpOnOutOfMemoryError_](https://docs.oracle.com/javase/7/docs/webnotes/tsg/TSG-VM/html/clopts.html) _._ This will capture the heap dump and put it in a file, which can be used to analyze what is eating up the memory.

**Technique 4.2:** You can also take the heap dump/thread dump of a running JVM using [jProfiler](https://www.ej-technologies.com/products/jprofiler/overview.html)/[Jvisiualvm](https://visualvm.github.io/).

#### **CodeBase where every JVM can talk to every other JVM.**

When you are thrown into a spaghetti distributed environment, it becomes difficult to track down the request flow.

**Technique 5.1:** You can use tools like [**Wireshark**](https://www.wireshark.org/). Wireshark captures the network data and represents it in a nice UI. You can then view the HTTP request/response flowing through the system

#### **Honorable mentions**

**Technique 6.1:** In a single-threaded environment, intentionally insert   
`try catch` in order to quickly know the stacktrace.

```java
try {
	throw new RuntimeException(); 
} catch(Exception e){
  e.printStackTrace();
}
```

**Technique 6.2:** Using eclipse breakpoint or using conditional breakpoint.

**Technique 6.3:** [https://en.wikipedia.org/wiki/Rubber_duck_debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)

> Motivation of article: Team Learning/Knowledge Sharing.

