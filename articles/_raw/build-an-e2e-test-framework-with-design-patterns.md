---
title: How to Build an E2E Testing Framework Using Design Patterns
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-09T17:14:49.000Z'
originalURL: https://freecodecamp.org/news/build-an-e2e-test-framework-with-design-patterns
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa818ca49c47664ed81b9ed.jpg
tags:
- name: automation
  slug: automation
- name: design patterns
  slug: design-patterns
- name: Testing
  slug: testing
seo_title: null
seo_desc: "By Jose J. Rodríguez\nEnd to End or E2E testing is about simulating the\
  \ user's experience. It doesn't deal with functions, variables, classes, or databases.\
  \ Instead, it deals with buttons, clicks, expected messages, links, and so on. \n\
  You might say th..."
---

By Jose J. Rodríguez

End to End or E2E testing is about simulating the user's experience. It doesn't deal with functions, variables, classes, or databases. Instead, it deals with buttons, clicks, expected messages, links, and so on. 

You might say that E2E testing is the "ultimate" testing since it checks whether the product as a whole behaves as expected.

In general, E2E testing is difficult to automate. First of all, you need tools that can interact with the application that is being tested – fill out forms, wait for a page to load completely, that kind of stuff.

You also need to get the results from the user interface. You don't have functions returning objects but HTML elements containing the information. Mocking a real user can be challenging and might require a lot of maintenance.

In this article, I will talk about my own experience building an E2E testing framework. I applied some cool Design Patterns so I think this could be interesting for you even if you have nothing to do with E2E testing automation.

This post is _language and tool agnostic_. This means that I won't refer to a specific programming language or a specific E2E tool like Selenium, Puppeteer, or Playwright. By the way, those are great tools for automatizing E2E tests. Also, this post focuses on E2E testing for websites.

## The problem I had to solve

I had to design a framework to perform different E2E tests on different websites. More precisely, I needed to make some tests over specific React components inside those websites. 

Every component had the same structure and CSS selectors no matter the website and just changed slightly from one site to another. I needed to make tests for every possible viewport (mobile, tablet, and desktop), and the components had to change their structure when the viewport changed.

In this scenario, I knew nothing about the developers. So I needed to be prepared to manage some unforeseen changes in the interface relatively easy. In other words, it was critical that the framework be easy to maintain.

So how was I supposed to make an E2E testing framework that didn't care too much whether the developers changed the id attribute of some button that was clicked in some test? How could I write tests for some component that was not created yet? And how could I make every test easy to read and understand?

I was able to achieve all those goals by applying some abstractions and design patterns. So let's see how I did it.

## The Page Object Model

The first thing we need to do is to create an abstraction for a page. This is important for several reasons. 

First, it will increase readability. For example, you don't want to have a line in your test that reads ```tool.getByCssSelector("button.btn.btn-submit").click()```. Instead you want to have a line like this one: ```page.clickSubmitLoginFormButton()``` or something similar. 

You also need to keep all the CSS selectors and DOM-related stuff in a single place. This way, when something in the interface changes you only need to modify one single file (or maybe two, but not more ;-) ).

That abstraction is called the **Page Object Model**. You make a class that represents only the elements that you are interested in from the page. You put all the DOM-related stuff in those classes.

In my case, I did it slightly differently. I created two classes for every page, a **PageModel** and a **Page Object**. 

In the first one, I put the elements of the page. For example, suppose we are testing a login page, then my **LoginPageModel** would be like this:

```pseudocode

class LoginPageModel

    constructor(tool)

        this.tool = tool


    loginUsernameInput()

        return this.tool.getById('username-input')


    loginPasswordInput()

        return this.tool.getById('password-input)


    loginSubmitButton()

        return this.tool.getById('submit-login-button')

```

If any of those elements change in the future we only need to modify the corresponding **PageModel** class.

In the **PageObject** class, I add the actions that you can perform on the page. An example of a **LoginPageObject** class would be:

```pseudocode

class LoginPageObject

    constructor(pageModel)

        this.model = pageModel


    typeUsername(username)

        this.model.loginUsernameInput().type(username)


    typePassword(password)

        this.model.loginPasswordInput().type(password)


    clickLoginSubmitButton()

        this.model.loginSubmitButton().click()

```

Here we can take advantage of a statically typed language that can get all the methods of the model class in compilation time. That way some IntelliSense tool can remind us the name of every method that represents a page element. 

We also get more compilation errors and fewer runtime errors, which is very good for us and our mental health.

Why do we need to separate page elements from page actions? A single class that contains both the elements and the actions can be very large. 

We can say that by doing this we are applying the Single Responsibility Principle and that would be cool. But in this case, that doesn't have much practical significance beyond readability and keeping classes simple.

With the **Page Object** abstraction we can make tests that only depend on page objects instead of writing some tricky CSS selectors in the middle of the test code. 

We keep all the DOM-related stuff in a single place and our tests can be more expressive and easy to understand.

## Writing tests – the Facade Pattern

Now we have many classes that contain all the elements and actions of several pages. What we need to do now is to build our tests. 

These tests will provide a simple interface that exposes the ```run``` functionality to the client. This functionality returns a test result. 

The client doesn't have to worry about accessing any element or doing any action, it just needs to instantiate the test and run it.

When we provide a simple interface that hides a more complex infrastructure we are applying the Facade Pattern. I know that's only a fancy name for something it's clear that we needed to do. 

Continuing with our Login Page test example, the **LoginTest** would be something like this:

```pseudocode

class LoginTest


    constructor(loginPageObject)

        this.pageObject = loginPageObject


    run()

        this.pageObject.typeUsername("TestUser")

        this.pageObject.typePassword("TestPassword")

        this.pageObject.clickLoginSubmitButton()

        assert that the login was successful
```

The last line of the ```run``` method is an assertion. Depending on the complexity of the assertions you use, you can either define them separately or inside the Page Object. 

By choosing the first option you can reuse and extend assertions. But if your assertions are very specific for each case and simple enough, the first option can be overkill and you will probably be good with the second one.

We are also injecting the Page Object dependency in the test. We are not doing ```this.pageObject = new LoginPageObject()``` but receiving the dependency as an argument in the constructor. This is called _Dependency Injection_. That way, we can instantiate the same test for another page. 

We also inject the Page Model in Page Object instances. Then, we can have the same Page Object with another model (Example: same LoginPageObject instance with a LoginMobilePageModel instead of a regular LoginPageModel).

But now, to instantiate a test, we need to instantiate one or more Page Models, then one or more Page Objects, and finally the test. This seems like too much work. That's precisely one of the drawbacks of using Dependency Injection – but the problem is solvable!

## The Factory Pattern

Let's delegate the responsibility to another abstraction. In this case, we'll make some factories. 

Factories are classes that are used to instantiate other classes. Every factory class will be responsible for instantiating a specific test. That's the Factory Pattern in action.

So we can create a **LoginTestFactory** for our LoginTest:

```pseudocode

import tool

class LoginTestFactory


    create(config)

        if config.viewport == 'mobile'
            then return new LoginTest(new LoginPageObject(new LoginMobilePageModel(tool)))
        else
            return new LoginTest(new LoginPageObject(new LoginPageModel(tool)))
```

Here with ```tool``` we are representing any possible technology you could use to get the elements of a page and interact with them. 

Maybe you don't pass the imported tool as is, but you create some objects using that tool and then pass those objects as parameters. 

But the idea is that all the relatively complex logic to make an instance of a test is encapsulated in a factory object.

To run our test we only need to do something like this:

```pseudocode

runLoginTestDesktop()

    factory = new LoginTestFactory()

    config = new ConfigObject(viewport = 'desktop')

    test = factory.create(config)

    test.run()



runLoginTestMobile()

    factory = new LoginTestFactory()

    config = new ConfigObject(viewport = 'mobile')

    test = factory.create(config)

    test.run()
```

Now, in the conclusions section, we'll check whether we have accomplished our initial goals

## Conclusion

Building your testing framework like this can dramatically decrease the cost of changes in a user interface. All the code that depends on the user interface is isolated in specific classes that abstract the concept of a page.

That abstraction also allows you to write your tests for the next week. (I mean the tests for components that have not been created yet.) You just make the required new PageModels and PageObjects to mock the elements on the page that will be created and you can build the rest of the process in the same way we have seen so far. 

When you have specific elements on the interface you can change the page models and verify whether the application behaves as expected.

You also have tests that are very easy to read and understand since you make expressive actions like ```this.pageObject.clickLoginSubmitButton()```. Thus, your tests can describe the requirements of your application and can be easily maintained.

E2E testing automation is difficult because it's hard to keep it simple. And a complex test is not a test. 

In this post, I have shown some design patterns and good practices you can use to make it smoother. I have tried to make it language and tool agnostic so you can apply these practices in your project no matter what language or technology you are using. I only assumed an Object-Oriented programming language.

Whether or not you're making an E2E testing framework, I think this article can still be of use to you. Some of these tricks can be applied in a relatively wide variety of problems.

You can visit my [personal blog](https://jj.hashnode.dev) and follow me on [Twitter](https://twitter.com/josejorgexl) for more Computer Science related content.



