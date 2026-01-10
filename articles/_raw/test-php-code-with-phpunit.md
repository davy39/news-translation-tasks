---
title: How to Test PHP Code With PHPUnit
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2022-03-09T01:15:45.000Z'
originalURL: https://freecodecamp.org/news/test-php-code-with-phpunit
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/120480919-metal-bolts-nuts-group-drawing-technical-drafting-steel-screws-threaded-parts-with-hexagonal-head-bl--1-.png
tags:
- name: PHP
  slug: php
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'There are many different ways to test your software application, and unit
  testing is an important one.

  So what is unit testing and how can you do it? You''ll learn that and more in this
  article.

  What is Unit Testing?


  Unit testing is a software develo...'
---

There are many different ways to test your software application, and unit testing is an important one.

So what is unit testing and how can you do it? You'll learn that and more in this article.

## What is Unit Testing?

> Unit testing is a software development process in which the smallest testable parts of an application, called units, are individually and independently scrutinised for process operation. - [SearchSoftwareQuality](https://searchsoftwarequality.techtarget.com/definition/unit-testing#:~:text=Unit%20testing%20is%20a%20software,developers%20and%20sometimes%20QA%20staff.)

In basic terms, unit testing means that you break your application down to its simplest pieces and test these small pieces to ensure that each part is error free (and secure). 

This testing is automated and written by software engineers as part of their development process. This is a very important step during development as it helps developers build better applications with fewer bugs.

## What is PHPUnit?

You can perform unit testing in PHP with [PHPUnit](https://phpunit.de), a programmer-oriented testing framework for PHP. PHPUnit is an instance of the xUnit architecture for unit testing frameworks. It is very easy to install and get started with.

## PHPUnit Installation

You can install PHPUnit globally on your server. You can also install it locally, on a per-project, development-time basis as a dependency to your project using composer. This article will explain how to use it on a per project basis.

To get started, create and initiate a new project with composer using these commands:

```bash
$ mkdir test-project
$ cd test-project
$ composer init
```

The first command creates a folder in your current directory, `test-project` and the second command moves into it. The last command starts an interactive shell.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-11.08.39.png)
_Composer init prompt_

Follow the prompt, filling in the details as required (the default values are fine). You can set the project description, author name (or contributors' names), minimum stability for dependencies, project type, license, and define your dependencies.

You can skip the dependencies part, as we are not installing any dependencies. PHPUnit is supposed to be a `dev-dependency` because testing as a whole should only happen during development.

Now, when the prompt asks `Would you like to define your dev dependencies (require-dev) interactively [yes]?`, press enter to accept. Then type in `phpunit/phpunit` to install PHPUnit as a `dev-dependency`.

Accept the other defaults and proceed to generating the `composer.json` file. The generated file should look like this currently:

```json
{
    "name": "zubair/test-project",
    "require-dev": {
        "phpunit/phpunit": "^9.5"
    },
    "autoload": {
        "psr-4": {
            "Zubair\\TestProject\\": "src/"
        }
    },
    "authors": [
        {
            "name": "Idris Aweda Zubair",
            "email": "zubairidrisaweda@gmail.com"
        }
    ],
    "require": {}
}
```

To learn how to install PHPUnit globally on your server, read [here](https://phpunit.readthedocs.io/en/9.5/installation.html#).

## How to Write Tests in PHPUnit

Writing tests in PHPUnit is quite simple. Here are a few conventions to get you started:

* To test a class in PHP, you'll create a test class named after that class. For example, if I had some sort of `User` class, the test class would be named `UserTest`.
* The test class, `UserTest`, will usually inherit the `PHPUnit\Framework\TestCase` class.
* Individual tests on the class are public methods named with `test` as a prefix. For example, to test a `sayHello` method on the `User` class, the method will be named `testSayHello`.
* Inside the test method, say `testSayHello`, you use PHPUnit's method like `assertSame` to see that some method returns some expected value.

A popular convention is to have all tests in a `tests` directory, and all source code in the `src` directory. 

## PHPUnit Testing Example

To help understand this article, here's a sample `User` class with simple methods that will be tested:

```php
<?php

namespace Zubair\TestProject;

use InvalidArgumentException;

class User
{
    public int $age;
    public array $favorite_movies = [];
    public string $name;

    /**
     * @param int $age
     * @param string $name
     */
    public function __construct(int $age, string $name)
    {
        $this->age = $age;
        $this->name = $name;
    }

    public function tellName(): string
    {
        return "My name is " . $this->name . ".";
    }

    public function tellAge(): string
    {
        return "I am " . $this->age . " years old.";
    }

    public function addFavoriteMovie(string $movie): bool
    {
        $this->favorite_movies[] = $movie;

        return true;
    }

    public function removeFavoriteMovie(string $movie): bool
    {
        if (!in_array($movie, $this->favorite_movies)) throw new InvalidArgumentException("Unknown movie: " . $movie);

        unset($this->favorite_movies[array_search($movie, $this->favorite_movies)]);

        return true;
    }
}

```

This user class could be the `User` class in your movie streaming application. The user has a name, age, and a list of favourite movies that can be updated. For the rest of the article we will test that all these features work as they're expected to.

Create a `UserTest` class in the `tests` folder. Paste this in to start:

```php
<?php

namespace Zubair\TestProject;

use PHPUnit\Framework\TestCase;

final class UserTest extends TestCase
{
    // Tests will go here
}
```

### Test Constructor

Normally, you wouldn't be testing the `__construct` method. However, since we're setting values in it, it only makes sense to be sure that the values are being set correctly. 

This seems like a very small thing to test, but that's the whole point of unit tests – to ensure that the smallest parts of your application function as expected.

Create a `testClassConstructor` method to test the constructor:

```php
public function testClassConstructor()
{
    $user = new User(18, 'John');

    $this->assertSame('John', $user->name);
    $this->assertSame(18, $user->age);
    $this->assertEmpty($user->favorite_movies);
}
```

Let's take a quick break now, to see how to run the tests.

## How to Run Tests in PHPUnit

You can run all the tests in a directory using the PHPUnit binary installed in your vendor folder.

```bash
$ ./vendor/bin/phpunit --verbose tests
```

You can also run a single test by providing the path to the test file.

```bash
$ ./vendor/bin/phpunit --verbose tests/UserTest.php
```

You use the `--verbose` flag to get more information on the test status.

Now, we can run the test and see the output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-13.17.54.png)
_Test Output_

The output shows that we ran 1 test, and made 3 assertions in it. We also see how long it took to run the test, as well as how much memory was used in running the test.

These assertions are what PHPUnit uses to compare values returned from the methods to their expected value. 

This example uses `assertSame` to check if the `name` and `age` properties on the user object match the entered values. It also uses `assertEmpty` to check that the `favorite_movies` array is empty. 

To see a list of all these assertions, you can check out PHPUnit's docs [here](https://phpunit.readthedocs.io/en/9.5/assertions.html#appendixes-assertions).

Edit the code to check if the user age is the same as _21_.

```php
public function testClassConstructor()
{
    $user = new User(18, 'John');

    $this->assertSame('John', $user->name);
    $this->assertSame(21, $user->age);
    $this->assertEmpty($user->favorite_movies);
} 
```

Running the test again this time gives this output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-13.24.20.png)
_Failed Assertion Output_

The output now shows that we ran 1 test, with 2 successful assertions, and also a failed one. We can see some explanation of the failure, showing the expected value, the gotten value, and the line where the error is from.

### Test testName and tellAge

Next, we can test the `testName` method. This method tells the name of a user as a sentence. So, we can write the test to check:

* If the returned value is a string.
* If the returned string has the user's name in it (with or without case sensitivity).

```php
public function testTellName()
{
    $user = new User(18, 'John');

    $this->assertIsString($user->tellName());
    $this->assertStringContainsStringIgnoringCase('John', $user->tellName());
}
```

The test uses the assertions `assertIsString`  and `assertStringContainsStringIgnoringCase` to check that the return value is a string and that it contains the string _John_, respectively.

The `testAge` method is very similar to `testName` and uses the same logic. Its test will be similar to the previous one:

```php
public function testTellAge()
{
    $user = new User(18, 'John');

    $this->assertIsString($user->tellAge());
    $this->assertStringContainsStringIgnoringCase('18', $user->tellAge());
}
```

### Test addFavoriteMovie

We can test this method, too. This method adds a movie to the list of movies. To test it, we can check if the newly added movie is in the list, and that the number of items in the list actually increased. 

The latter is for confirming that items are not being displaced. Also, since the function returns some value at the end, we can check that this value is correct too.

```php
public function testAddFavoriteMovie()
{
    $user = new User(18, 'John');

    $this->assertTrue($user->addFavoriteMovie('Avengers'));
    $this->assertContains('Avengers', $user->favorite_movies);
    $this->assertCount(1, $user->favorite_movies);
}
```

Here, we use a few new assertions – `assertTrue`, `assertContains`, and `assertCount` – to check that the returned value is true, that it contains the newly added string, and that the array now has one item in it.

### Test removeFavoriteMovie

Finally, we can test that the method to remove a movie works. 

```php
public function testRemoveFavoriteMovie()
{
    $user = new User(18, 'John');

    $this->assertTrue($user->addFavoriteMovie('Avengers'));
    $this->assertTrue($user->addFavoriteMovie('Justice League'));

    $this->assertTrue($user->removeFavoriteMovie('Avengers'));
    $this->assertNotContains('Avengers', $user->favorite_movies);
    $this->assertCount(1, $user->favorite_movies);
}
```

Here, we're adding some movies to the list. Then, we remove one of them, and confirm that the function returned true. Next, we confirm the removal by checking that the value is no longer in the list. Finally, we confirm that we have only one movie in the list, instead of two.

## Conclusion

Now you know how to set up PHPUnit in your projects and how to test and ensure that you're building world class software. You can find all the code for this article [here](https://github.com/Zubs/php-testing).

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

