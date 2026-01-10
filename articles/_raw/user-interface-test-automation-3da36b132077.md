---
title: User Interface Test Automation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-22T22:28:56.000Z'
originalURL: https://freecodecamp.org/news/user-interface-test-automation-3da36b132077
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MAoFtzMOZQV7fGIcvizZDg.jpeg
tags:
- name: automation
  slug: automation
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Aditya Parab

  Test Automation has become one of the important aspects in the Software development
  world. Everyone in this community must be aware of the below Agile Test Automation
  Pyramid. It is concept developed my Mike Cohn.

  Unit tests should fo...'
---

By Aditya Parab

Test Automation has become one of the important aspects in the Software development world. Everyone in this community must be aware of the below Agile Test Automation Pyramid. It is concept developed my Mike Cohn.

Unit tests should form the base of this pyramid. The Service level tests form the next layer and finally the User Interface (UI) tests form the apex.

![Image](https://cdn-media-1.freecodecamp.org/images/91E5LbriJvgfm9TWbyaMUnpYN0hXgKrU4CEp)
_Agile Test Automation Pyramid_

Traditionally automated testing meant testing the end to end execution flow on the UI level. But with the above concept and the implementation of agile, this has changed. Unit and service level tests form the major part of the automation strategy. UI tests are a small part.

There are valid reasons for having less UI automation tests as part of your automation strategy. Below I have listed a few:

* These tests are **slow**.
* These tests are **brittle** and can give a false positive or false negative.
* UI based hence need a lot of **changes** and **maintenance**.

Having said this, UI Test Automation is still important as it tests the part which your user will be navigating through. Feedback about this surely helps improve the user experience while using the application.

Below are a few cases in which UI test automation is valuable:

* Regression Testing. Automation can free human testers of the boring and repeated process of regression testing.
* Testing applications which do not have unit tests developed. This helps to introduce automated testing in legacy applications.
* Cross-browser and Cross-platform testing. This is mostly executing the same tests on different versions. This is also the case for mobile applications for testing different OS versions and device models.
* Performance Testing as it requires a higher load than that manual testing cannot generate.

With a proper strategy, UI Test Automation can form a very useful part of your Test Automation suite. Some pointers in developing an efficient test strategy

### Identify the right cases to automate

The most important aspect of any testing is the identification of the right test cases. The same is true for automated testing.

Following are some criteria for selecting test cases for automation:

1. Test cases which are frequently executed as part of smoke and regression
2. Test cases which implement complex logic and calculations
3. Test cases which need to be executed across multiple platforms
4. Test cases where the manual execution can be difficult eg. Performance

### Prepare from the beginning

The preparation for automating any functionality begins in the design phase. Involve test engineers in this phase along with the developers. Create a strategy for automation testing. Decide what tests are covered in the unit and service level so that there is no duplication in UI tests.

In case of an application built from scratch, design the code to make it easy to automate once the application is stable. It can be small things. For example, following specific naming conventions for the UI elements. As well as naming similar elements on different pages similarly. This also helps to keep the automation scripts consistent.

In case of changes in an existing application, start automation together with the development. As the changes made are incremental, execute testing as soon as they are available. This is beneficial for agile and continuous delivery. Therein, small increments are required to be ready for implementation continuously.

### Continuous and parallel execution

Schedule automated test execution frequently. At least once per day. This provides a continuous feedback about the changes made. It also gives a good idea of the stability of the test environment.

Execution is slower as these tests are executed on the UI. But with continuous testing, we want faster feedback. Parallel execution is one of the ways to solve this problem. Also with parallel executions testing across platforms can be achieved.

### Refactoring and Maintenance

UI Automated Test scripts should be considered same as application code. This provides required focus and attention. Same as the application code, these scripts also need continuous refactoring and maintenance.

With proper maintenance test execution becomes consistent. Also, it will help improve the performance of test execution and make future changes easier.

With a proper design and execution strategy, UI Test Automation can prove to be a useful step towards improving the quality and speeding up continuous delivery.

