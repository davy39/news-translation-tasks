---
title: How to Use Facades in Laravel
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-12-08T19:32:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-facades-in-laravel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95ff740569d1a4ca0f32.jpg
tags:
- name: framework
  slug: framework
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: null
seo_desc: 'Facades are one of the key things you should understand when learning Laravel.

  It took me a considerable amount of time to figure out how facades work, and I''m
  writing this to help anyone who is having trouble wrapping their heads around the
  concept....'
---

Facades are one of the key things you should understand when learning Laravel.

It took me a considerable amount of time to figure out how facades work, and I'm writing this to help anyone who is having trouble wrapping their heads around the concept.

In this article we'll cover what facades are, how they're used in Laravel, how you can build your own simple facade, and more.

## What is a facade? And what is a wrapper?

A facade in Laravel is a wrapper around a non-static function that turns it into a static function.

The word "wrapper" can also be used when describing design patterns. Wrapping an object to provide a simplified interface to it is often described as the "facade" pattern. 

So in short, the [wrapper](https://en.wikipedia.org/wiki/Wrapper_function) is the facade.

Before diving deeper into facades, it's important to understand what static and non-static functions are in PHP.

### Static Methods

In Static methods we're not required to create an instance of a class to reference it. Static methods use double colons (::) when accessing properties or methods of a class:

```php
<?php
class Calc {
    const GOLDEN_RATIO = '1.618';
}

echo Calc::GOLDEN_RATIO;  //1.618


```

Reserved keywords like `self` , `static` and `parents` is used to reference properties or methods within a class:

```php
<?php
class backend {
	private const language = "php";
	public static function language() {
    	echo self::language;
  	}
}

backend::language();  //php


```

### Non-static Methods

Non-static methods require that a given class be instantiated. In other words, they require an instance of the class to execute:

```php
<?php
class backend{

	public function language($name){
		
		echo $name;
	}

}


$test = new backend; //creating an instance of the class

$test->language('php'); //php
```

Now that we've gone over static and non-static methods, we can dive deeper into facades in Laravel.

## Laravel facades

In the `vendors > laravel  > framework > src > illuminate > support > Facades` directory, there's a list of files which are the various facades that ship with Laravel by default.

Here's a screenshot of what the directory structure actually looks like in our editor:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-26-at-01.06.09.png)

Let's use the working code from `Log.php` to examine facades in more detail – the same explanation should apply to all facades in any Laravel application.

### Laravel's Log facade

Here's the code for Laravel's `Log` facade:

```php
<?php

namespace Illuminate\Support\Facades;

class Log extends Facade
{
    /**
     * Get the registered name of the component.
     *
     * @return string
     */
    protected static function getFacadeAccessor()
    {
        return 'log';
    }
}

```

`Log` is a class that extends the base facade which is from the namespace above.

Within the `Log` class we have a protected access modifier, `getFacadeAccessor`, and what that method does is it just returns `log`. 

The name of this facade, `log`, is being returned so we can access the named facade anywhere within the Laravel application without initializing it. So we can do something like `Log::info('hello there');` anywhere really easily.

As you can see, facades make code easier to read, more organized, and make testing 10 times easier.

Since learning about `Log` from one of my co-workers, it's been my favorite debugging tool.

## How to create a facade in Laravel

In this section we'll implement our own facade. The main objective here is to help learners understand how Laravel facades work.

We'll do this by creating a StudentFacade which will extend properties from a base Facade that returns a name property after it has been resolved. This name property will be of type string and it will be returned each time we instantiate the class as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-05-at-21.13.39.png)

Curious how we will achieve this? Follow along as I'll be walking you through the steps.

We won't be creating our facade using the normal Laravel convention where we have a `.php file` in `app > facade` and then another in the `providers` before we end up registering it in the `config > app`. 

Instead, we will make do with the `web.php` inside the `routes` for this illustration since we're just trying to see how facades work under the hood in a typical Laravel application.

First, let's start with this in `web.php`:

```php
<?php 
class Student{
    public function students(){
        return 'Sean';
    }
}

 app()->bind('student', function(){
 	return new Student;   
 }); 
```

We've created a class `Student`, and inside it we have a non-static `students` method that returns an array of students.

Then we call the _bind_ method to make it always instantiate `new Student` so we don't need to do this manually anymore.

Next, let's create a base `Facade` class still within the same `web.php`:

```php
 class Facade{
    public static function __callStatic($name, $args){
        return app()->make(static::getFacadeAccessor())->$name();
    }
    
    protected static function getFacadeAccessor(){
        //override take place 
    }
}
```

Any facade we might create later will be extending the properties of this base facade.

Within the `Facade` class we have a `__callStatic` [magic method](https://www.php.net/manual/en/language.oop5.magic.php) that helps us resolve the `static::getFacadeAccessor()` from the container with `app()->make()`. And with those we're able to access the `$name` property.

```php
class StudentFacade extends Facade {
	protected static function getFacadeAccessor(){
    	return 'student';
    }
}
```

Here, `StudentFacade` inherits the properties of the base facade. Then we override `getFacadeAccessor()` and set the return value to be whatever we have each time we instantiate in the bind above `student`.

```php
StudentFacade::students(); //output "Sean"
```

When we try to call the facade which we created it returns "Sean" as expected. Now in the final step we have to put all these steps together:

```php
<?php

class Student{
    public function students(){
        return 'Sean';
    }
}

 app()->bind('student', function(){
    return new Student;   
 }); 
 
 
 class Facade{
    public static function __callStatic($name, $args){
        return app()->make(static::getFacadeAccessor())->$name();
    }
    
    protected static function getFacadeAccessor(){
        //override take place 
    }
}

class StudentFacade extends Facade {
    protected static function getFacadeAccessor(){
        return 'student';
    }
}

//log or die it to the output
dd(StudentFacade::students());
```



![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-05-at-21.13.39-1.png)

## Conclusion

I hope that by the end of this lesson you have been able to broaden your knowledge about facades work. If you have questions or wish to continue the conversation feel free to tweet at me.

### References

[Laravel Beginner tutorial](https://www.youtube.com/watch?v=zD2VJhOdI5c) - Bitfumes

[What is WRAPPER in programming, what does it help to do?](https://stackoverflow.com/questions/3293752/where-and-how-is-the-term-used-wrapper-in-programming-what-does-it-help-to-do) - Stackoverflow

