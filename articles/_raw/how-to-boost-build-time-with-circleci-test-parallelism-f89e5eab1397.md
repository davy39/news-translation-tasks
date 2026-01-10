---
title: How to boost build time with CircleCI test parallelism
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T17:21:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-build-time-with-circleci-test-parallelism-f89e5eab1397
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Xw31bEh4xGoWbmx_.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: gradle
  slug: gradle
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Karel Rochelt

  Providing an error-free API for a heavily developed project is not an easy task.
  Likely, the first things that come to mind are tests. For a mid-sized API, you may
  write hundreds or even thousands of end-to-end tests. These tests sig...'
---

By Karel Rochelt

Providing an error-free API for a heavily developed project is not an easy task. Likely, the first things that come to mind are tests. For a mid-sized API, you may write hundreds or even thousands of end-to-end tests. These tests significantly prolong build times.

In this post, we will explain how we solved long build times with CircleCI test parallelism and Gradle/Grails for [Amio](https://amio.io) main service.

### CircleCI setup

CircleCI’s [documentation](https://circleci.com/docs/2.0/parallelism-faster-jobs/) does a decent job of explaining how their [command line interface](https://circleci.com/docs/2.0/local-cli/) (CLI) tool should be used to enable test parallelism. When I started looking into it for the first time, it wasn’t entirely obvious what the returned result would look like. I was asking myself, “So, I’ll run this command and it will magically start splitting my tests?” Well, of course not! The result is a list of test files that should be executed on a particular container.

Does that sound complicated? Let me explain in an example.

The first thing we have to do is to set the parallelism key in the `.circleci/config.yml` file. From the CircleCI docs:

> The `_parallelism_` key specifies how many independent executors will be set up to run the steps of a job.

Any value greater than one will enable parallel execution, but for the sake of this example, let’s go with two. This way, every time a CircleCI job is started, it will spawn two containers which will both do the same tasks.

If we were to use the parallelism key with no additional configuration, it would just run all of our tests twice. That is not what we want. We want to split our tests between the containers.

That’s where the CircleCI CLI comes in. It offers two commands which, when used together, split our tests into equal portions across our two containers.

Let’s say these are the test files in our project:

```
src/integration-test/groovy/com/package1/Test1.groovysrc/integration-test/groovy/com/package1/Test2.groovysrc/integration-test/groovy/com/package2/Test3.groovysrc/integration-test/groovy/com/package2/Test4.groovysrc/integration-test/groovy/com/package2/Test5.groovy
```

Naturally, we will have other source files in our project; not just our tests. They may be located in the same `src/integration-test/…` directory. To achieve our goal of test splitting, we need to select only the test files for the project. That is done by using the [glob](https://circleci.com/docs/2.0/parallelism-faster-jobs/#globbing-test-files) command:

```
circleci tests glob "src/integration-test/**/*.groovy"
```

This command will output the list of our tests (all 5 of them). ? Now we use the split command to, well, s[plit](https://circleci.com/docs/2.0/parallelism-faster-jobs/#splitting-test-files) them between containers:

```
circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings
```

The `split` command offers several strategies to split the tests but `timings` is my favorite. It uses the timings data that is collected by CircleCI (this has to be enabled via the [store_test_results](https://circleci.com/docs/2.0/configuration-reference/#store_test_results) key) to split the tests into portions that take a similar time to execute. Container indexing is automatic. We can run the same command on every container. In our example, running the command on Container 0 might output:

```
src/integration-test/groovy/com/package1/Test1.groovysrc/integration-test/groovy/com/package2/Test3.groovy
```

And on Container 1:

```
src/integration-test/groovy/com/package1/Test2.groovysrc/integration-test/groovy/com/package2/Test4.groovysrc/integration-test/groovy/com/package2/Test5.groovy
```

I say “might” because the real result would depend on the timings data. As you can see, every container got its half of the tests.

### Gradle setup

Splitting the tests in CircleCI was the easy part. The hard part is getting Gradle to execute just the tests that are in the result of the split command. If we were using JavaScript and Mocha, it would be much easier. Mocha accepts a list of files which should be executed. With Gradle 3, I had been using this command to run tests: `./gradlew check -i`

Gradle’s [documentation](https://docs.gradle.org/current/userguide/gradle_wrapper.html) isn’t really helpful. Just figuring out what the check task does is a pain. Thankfully, it is possible to pass our test list as a parameter to the Gradle task.

```
./gradlew check -i -PtestFilter="`circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings`"
```

Now, when the `check` task is started, it has access to the `testFilter` parameter. To make everything work, we also need to add some code that can handle the parameter in our **build.gradle**:

```
integrationTest {  if (project.hasProperty("testFilter")) {    List<String> props = project.getProperties().get("testFilter").split("\\s+")    props.each {      include(it.replace("src/integration-test/groovy/com/", "**/").replace(".groovy", ".class"))    }  }}
```

Note that the parameter was passed to the task as a single string. In the code block above, Line 3 contains logic to split it back into rows. Calling include will tell Gradle to execute only the tests that we include. Now we can include all the rows, and we’re good, right?

Nope. Gradle doesn’t know how to work with source files. It only understands classes. We need to pass the compiled class files to it.

There are two problems with that. First, the compiled classes are not in the same directory. Second, the suffix is not .groovy but .class.

To overcome the first problem, we replaced the common prefix with **/. This says, “Look in the root directory and all its subdirectories.” Of course, you could replace it with something like `build/classes/integrationTest/com`. That is cleaner, but not necessary. This should be safe as long as the test classes names are unique. Line 5 in the code block above includes logic that solves both of these problems.

In the end, your `.circleci/config.yml` should look something like this (just the relevant part):

```
- run:    # This is just for debugging purposes, you can omit this step    name: test splitting output    command: circleci tests glob “src/integration-test/**/*.groovy” | circleci tests split --split-by=timings | xargs -n 1 echo
```

```
- run:    name: test    command: ./gradlew check -i -PtestFilter="`circleci tests glob “src/integration-test/**/*.groovy” | circleci tests split --split-by=timings`"
```

### Conclusion

And that’s it! Easy, right? Well, it was a bit more work than it should have been. Having our test times cut nearly in half was definitely worth it! Applying test parallelism, we’ve decreased the build time from around 15 minutes to 9 minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/5Pn6DOPH8BS02ki3faCRXcsui9ZE1x9jRnp4)

