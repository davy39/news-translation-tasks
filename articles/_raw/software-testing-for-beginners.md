---
title: Software Testing – Beginner's Guide
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2022-03-07T23:14:46.000Z'
originalURL: https://freecodecamp.org/news/software-testing-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Talk2Her-Foundation--4-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
- name: user testing
  slug: user-testing
seo_title: null
seo_desc: "What is Software Testing?\nLet's say you're working on a coding project.\
  \ You have been writing a bunch of code and staying up late at night to fix bugs.\
  \ All this is part of the process before you release that software product. \nThen\
  \ you'll check your ..."
---

## What is Software Testing?

Let's say you're working on a coding project. You have been writing a bunch of code and staying up late at night to fix bugs. All this is part of the process before you release that software product. 

Then you'll check your code to verify that it actually performs what it's been programmed to do. This is where software testing comes in.

This article will discuss the categories of Software Testing and the different types of testing developers most commonly use. You'll see that some of the tests are named for their function. So, when I say API test, I am referring to the tests carried out on the APIs consumed in your source code. 

But before going further, let's make sure we know what we mean by Software Testing.

In simple terms, Software Testing is the process of checking the various aspects of a software product to validate the software’s specifications and make sure it's ready to use.

## Objectives of Software Testing

From a single line code to a block of code, and even to the finished product, you test software to:

* check for defects and ensure that the product performs as specified
* make sure that the product meets market standards
* resolve any loopholes at the production stage
* prevent future malfunctions of the product

## Characteristics of Software Testing

When you test your software, you want to make sure that your tests are:

* Practical
* Reliable
* Authentic
* Capable of finding errors
* Capable of checking the validity of your software

## When Should You Test Your Software? 

When you test your software will depend on what test you're wanting to perform.

You can test your software during the software development phase – that is, when writing the source code, as in the case of unit testing, API testing, and others. 

You can also test after the software has been developed such as in User Interface (UI) Testing.

## When Should Testing Stop?

You can stop testing your software when:

* All the necessary tests have been carried out efficiently
* Bugs in the source codes have been reduced to the barest minimum or eradicated
* Testers are done testing
* Product is fully secured against threats
* The product is released

## **Software Testing Methods**

Now that you know what Software Testing means, how exactly is it done? 

Software Testing is done based on two main methods:

1. Functional Testing
2. Non-functional Testing

The major difference between these categories of  Software Testing is that Functional Testing tests the functionality of a software product while non-functional testing concentrates on the performance of the software product.  

### **Functional Testing**

Functional testing is the process of testing software to validate its usefulness with regard to its specifications.

In simple terms, it consists of various tests carried out on the software generally to verify its functionalities.

Functional testing helps the software team know if the software is working as required. Mind you, Functional Testing doesn't mean testing unit functions or modules.

### Examples of Functional Testing

#### Unit Testing

In unit testing, you test individual units or functions of your software's source code. Unit testing can be done automatically or manually.

Automatic unit testing happens with human assistance while manual unit testing is actively done by humans.

The difference between these two methods is that the former is automated while the latter requires hard-coding.

The purpose of unit testing is to ensure that each unit component is working as expected.

#### API Testing

An application Programming Interface (or API) is a link between your program and an external source. So, if you want your program to do more than just what you code, you could employ the features of another program also. This is what consuming APIs is all about. 

For instance, let's say that I want my application to have a map feature. Instead of coding one from the scratch, I could save myself some time and stress by using one of the readily available map APIs.   

Using APIs, especially from external sources, comes with its pros and cons, though. And I bet you want to reduce the cons as much as possible. Well, this is why you need to test the API prior to product release. 

When you consume a public or private API, while developing your software, you should check for the API's reliability, security, and effectiveness in your product prior to release. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/API.png)
_Image representing API_

#### UI (User interface) Testing

The User Interface is the channel of communication between the user and the software. 

Every software product is developed with certain specifications for the User Interface. This means that the way the user interacts with the application is predetermined prior to developing the product.

 In order to make sure that these specifications are met according to design, you can carry out tests on the UI – and this is known as UI Testing.

The UI Testing involves things like checking if the Sign-Up page is correctly accepting inputs, checking to see if the submit button is functional, and a host of other UI features. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Signup-page3--1-.png)
_Image of a Payment Page_

#### Integration Testing

Putting components into groups for testing is known as integration testing. Integration testing involves checking how each separate component works together to achieve the common aim of the product. 

For instance, in an e-commerce application, the integration tests can check how the Home page connects to the Carts page when the Cart menu is clicked. 

The purpose of integration testing is to make sure that components are working in synchrony – that is, that component A works well with component B.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/LOGIN_SIGNUP-PAGE.png)
_Image of two UI pages_

#### Regression Testing 

Software Development involves iteration, which often happens because of bugs in the source code. 

After debugging your code, updating the software program, or making any other change to your code, you should test that software to validate its functionality. This testing is called Regression testing. 

Examples of regression testing are corrective regression testing, selective regression testing, progressive regression testing, and others.

### **Non-functional or Performance Testing**

Non-functional testing refers to the various tests carried out on a product to check its readiness for the market. Non-functional Tests go a step further to ensure the viability of a product and its worth.

### Examples of Non-functional Testing

#### Volume Testing

The strength of every product lies in its ability to handle different volumes of data. Some software may not function with a large database. To avoid such breakage, you can do volume tests. 

Volume test involves feeding a large database to the software to check its functionality based on the large volume of data. Testing your product on different volumes of data shows that your product can withstand more or fewer data at a given time.

#### Security Testing

In the world today, security is an important and much-discussed topic. Concerns range from physical security down to cyberspace – and everyone wants that assurance of safety when they are on the internet.

One of the issues you'll want to avoid as a software developer is threats to your application. You can perform security testing on your software product to check its level of vulnerability. 

Security tests include authentication, authorization confidentiality, and other measures required to protect your software from risks and threats.

## Where to put test files in a program folder

Your test files should be together in a test folder inside the root folder of your project. This is for easy navigation and integration into your project.

## **Conclusion**

Now that you know the importance of testing in software development, you should make sure to write code that is error and bug-free when tested.

This will reduce the time you waste fixing bugs and will in turn make the product release date more achievable.

Lastly, be careful to put your test files in the same folder, especially for tests other than unit testing.

 

  

