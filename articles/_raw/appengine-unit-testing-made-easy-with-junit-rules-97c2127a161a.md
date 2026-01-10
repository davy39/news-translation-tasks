---
title: AppEngine unit testing made easy with JUnit Rules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T11:50:44.000Z'
originalURL: https://freecodecamp.org/news/appengine-unit-testing-made-easy-with-junit-rules-97c2127a161a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V2EDFPlZSdQQSVyKn6I68w.png
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Ramesh Lingappa

  Hello there! If you are using AppEngine for hosting your application, then you will
  be using one or more of their services like Datastore, Memcache, TaskQueues, UserService,
  etc.

  And you will be needing to write unit tests to make ...'
---

By Ramesh Lingappa

Hello there! If you are using AppEngine for hosting your application, then you will be using one or more of their services like Datastore, Memcache, TaskQueues, UserService, etc.

And you will be needing to write unit tests to make sure your application functionality is working as expected with these services. For that, you need to set up some configurations to test these services in your local environment.

If you are new to AppEngine service testing, Google has great documentation on how to set up this configuration with sample codes. Take a look at [Local Unit Testing for Java](https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting).

For example, here is a sample code from Google to perform datastore testing:

This is great. Most of the time, our services will be making use of multiple AppEngine services like Memcache for entities (Objectify), queueing tasks after saving an entity. The real pain point comes when we try to set up multiple configurations.

Okay, that’s the lot of configuration, but guess what — it’s not all. What if you need to change specific settings for some test like _High Replication_, _Queue XML Path_, or _Current User_ ? Then your set up will be even more complex. And you need to repeat all these for each of your unit test classes.

Oh, by the way, did you forgot [Objectify](https://github.com/objectify/objectify) test setup? Take a look at [Objectify Unit Testing](https://stackoverflow.com/questions/32628124/how-to-use-objectifyservice-in-junit-testing).

You might be thinking,

> “Let’s set up all of these configurations in the parent class and every unit testing class will extend this one”

We can do that, but there is another problem with it:

**Each of these services is expensive to create. You need to configure the environment _using only the services you need._**

So unnecessarily configuring all services will probably slow down the test execution time.

#### Okay, is there a rescuer?

Yes, [Junit Rules](https://github.com/junit-team/junit4/wiki/rules) comes to the rescue!

> “Rules allow very flexible addition or redefinition of the behavior of each test method in a test class. Testers can reuse or extend one of the provided Rules below, or write their own”

There are so many great articles out there about Junit Rules — please check them out.

So with JUnit rules, we are able to setup external dependencies before test execution in an easy way. With a few tweaks, we can setup AppEngine related services per class in the way we wanted. Here is a sample:

Here **AppEngineRule** is a simple class that extends **ExternalResource** and was created using a builder pattern. We can set up services which we need, and if you see in the **_SampleTestClass_**, we can do all the setup in one line.

```
@Rule    public final AppEngineRule rule = AppEngineRule.builder()             .withDatastore()             .withQueue()             .build();
```

And _AppEngineRule_ class overrides `before` and `after` methods to setup AppEngine setup and tearDown functionalities. You can also configure similarly for each Test classes with only the required services.

#### Is that all? Can we do any better?

Of course we can! To make this setup easy you need to write something similar to _AppEngineRule_ class with all the boilerplate setup code.

Here is good news: you don’t need to write any. I made a small library with all the necessary setup implementation for all the services and with even more configurable options.

[**ramesh-dev/gae-test-util-java**](https://github.com/ramesh-dev/gae-test-util-java)  
[_Google AppEngine Java Utility Library. Contribute to ramesh-dev/gae-test-util-java development by creating an account…_github.com](https://github.com/ramesh-dev/gae-test-util-java)

In your build script, simply add the dependency, for example in gradle:

```
testCompile 'com.github.ramesh-dev:gae-test-util-java:0.3'
```

With this, we can have flexible configurations like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PEm-JvZu6NKFKq_AY7VoPA.png)
_Image downloaded from the internet_

### Conclusion

So Junit Rules is a handy option to easily configure our external dependencies, even for complex one like AppEngine services. You can also have other Rules and chain them in a specific order using [Rule Chain](https://github.com/junit-team/junit4/wiki/rules#rulechain)

Thank you for reading and this time, and **Happy Testing…**

#### References

* [https://github.com/junit-team/junit4/wiki/rules](https://github.com/junit-team/junit4/wiki/rules)
* [https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting](https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting)
* [https://github.com/ramesh-dev/gae-test-util-java](https://github.com/ramesh-dev/gae-test-util-java)

