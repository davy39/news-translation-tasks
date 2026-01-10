---
title: How to eliminate (or deal with) hidden dependencies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-05T08:44:39.000Z'
originalURL: https://freecodecamp.org/news/eliminating-hidden-dependencies-a95c7b03aa54
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Shalvah

  In software, a dependency occurs when one module in an application, A, depends on
  another module or environment, B. A hidden dependency happens when A depends on
  B in a way that’s not obvious.

  To discover a hidden dependency, you usually h...'
---

By Shalvah

In software, a dependency occurs when one module in an application, _A_, depends on another module or environment, _B_. A hidden dependency happens when _A_ depends on _B_ in a way that’s not obvious.

To discover a hidden dependency, you usually have to dig into the source code of the module. A module could refer to anything from an entire service to a class or function to just a few lines of code.

Here’s a small example of a dependency, comparing two ways it could be expressed:

```
let customer = Customer.find({id: 1});
```

```
// explicit — the customer has to be passed to the cartfunction Cart(customer) { this.customer = customer;}let cart = new Cart(customer);
```

```
// hidden — the cart still needs a customer,// but it doesn’t say so outrightfunction Cart() { this.customer = customer; // a global variable `customer`}let cart = new Cart();
```

Note the subtle difference? Both implementations of the Cart constructor depend on a customer object. But the first requires that you pass in this object, while the second expects that there’s already a customer object available in the environment.

A dev seeing `let cart = new Cart()` would have no way to tell that the cart object depends on a global customer variable, except if they took a look at the Cart constructor.

#### Hidden dependencies in the wild

I’ll share a few examples of hidden dependencies I’ve come across in real-world codebases.

* **PHP `include` files**

Let’s take a typical PHP backend app. In our `index.php`, the entry point of our app, we could have something like this:

```
include 'config.php';include 'loader.php';$app = new Application($config);
```

The code looks suspicious, doesn’t it? Where did the `$config` variable come from? Let’s see.

The `include` directive is similar to HTML `<scri`pt> tags. It tells the interpreter to grab the contents of the specified file, execute it and, if it has a return statement, pass the return value to the caller. It’s a way of splitting code across multiple files. L`ike a &l`t;scri`pt>` tag, include can also put variables into the global scope.

Let’s look at the files we’re including. The `config.php` file contains typical configuration settings for a backend app:

```
$config = [  'database' => [    'host' => '127.0.0.1',    'port' => '3306',    'name' => 'home',  ],  'redis' => [    'host' => '127.0.0.1',  ]];
```

The `loader.php` is basically a homemade class loader. Here’s a simplified version of its contents:

```
$loader = new Loader(__DIR__);$loader->configure($config);
```

See the problem? The code in `loader.php` (and the rest of the code in `index.php`) depends on some variable named `$config`, but it’s not obvious where `$config` is defined until you open up `config.php`. This coding pattern is actually not uncommon.

* **Including JavaScript files via `<scri`pt>**; tags

This is probably a more common example. Compare the follwing two code snippets (assume `cart-fx` and `cart-utils` are some random JS libraries):

Exhibit A:

```
<script src="//some-cdn/cart-fx.js"></script><script src="//some-cdn/cart-utils.js"></script>
```

```
/* lots and lots of code */
```

```
<script>var cart = new Cart(CartManager.default, new Customer());</script>
```

Exhibit B:

```
import Cart from ‘cart-fx’;import CartManager from ‘cart-utils’;
```

```
/* lots and lots of code */
```

```
const cart = new Cart(CartManager.default, new Customer());
```

In the second, it’s obvious that the `Cart` and `CartManager` variables were brought in (imported) from the `cart-fx` and `cart-utils` modules respectively. In the first, we’re left to guess as to which module owns the `Cart`, and which owns the `CartManager`. And don’t forget the `Customer` too! (Remember, our own code is also a module.)

* **Reading from the environment**

I’m the culprit in this one. I built a PHP package some time ago to interact with an API. The package allowed you to pass your API keys to the constructor. Unfortunately, it also allowed you to instead specify your keys as environment variables, and the package would automatically make use of them. [Take a peek, and don’t laugh at me](https://github.com/Hng-X/moneywave-php/blob/ef4d491c9a23f084d7a13e7279219213e8d4f87f/README.md#configuration).

When I did that, I believed I was making the developer’s life easier. In reality, though, I was making assumptions about the environment the code was running in, and tying the package’s functionality to certain conditions being met in the environment.

#### So, why are hidden dependencies dangerous?

I can think of two main reasons:

* **It’s easy to unintentionally remove the module depended upon without removing the dependency**. For instance, take the case of my package above. Imagine a developer setting up an app which uses the package in a new environment. While deciding what environment variables to carry over from the old environment, the dev might neglect to add the ones needed by the package, _because they can’t find them used anywhere in the codebase_.
* **A small change to the dependent code could break the entire application, or make it buggy.** Take the case of our `index.php` file above — swapping the first two lines might seem like a harmless change, but it would break the app, because line 2 depends on a variable set in line 1. An even more serious case of this would be something like this:

```
$config = […];include 'bootstrap.php';$app = new Application($config);
```

Suppose our `bootstrap.php` file makes some important changes to `$config`. If, for some reason, the second line is moved to the bottom, the app would run without throwing any errors, but the crucial configuration changes that `bootstrap.php` makes would be unseen by the app.

#### Getting Rid of Hidden Dependencies

Like much of software engineering, there are no hard rules for dealing with hidden dependencies, but I’ve found a few basic principles that work for me:

1. _Write code that’s truly modular_, not just split across multiple files. An ideal module aims to be self-contained and have minimal dependence on shared global state. A module should also explicitly state its dependencies.
2. _Reduce the number of assumptions a module needs to make_ about its environment or other modules.
3. _Expose a clear interface._ Ideally, beyond things like function/class signatures, a user of your module should not have to look at the source code to figure out what the module’s dependencies are.
4. _Avoid littering the environment._ Resist the temptation to add variables to the parent scope. As often as possible, prefer explicitly returning or exporting variables to the caller.

I’ll demonstrate how we could refactor the first example above using these principles. The first thing to do is make the config file **return** the configuration array, so the caller can explicitly save that in a variable:

```
// config.phpreturn [  'database' => [    'host' => '127.0.0.1',    'port' => '3306',    'name' => 'home',  ],  'redis' => [    'host' => '127.0.0.1',  ]];
```

The next thing we can do is change the loader file to return a function. This function will take a config parameter. In this way, we’re making it clear that the process of loading files depends on some preset configuration.

```
// loader.php
```

```
return function (array $config){  $loader = new Loader(__DIR__);  $loader->configure($config);}
```

Putting these together, we end up with our `index.php` file looking like this:

```
$config = include 'config.php';(include 'loader.php')($config);
```

```
$app = new Application($config);
```

We can even go a bit further by saving the returned function in a variable before calling it:

```
$config = include 'config.php';
```

```
$loadClasses = include 'loader.php';$loadClasses($config);
```

```
$app = new Application($config);
```

Now, anyone looking at `index.php` can tell at a glance that:

1. The file `config.php` returns **_something_** (we can guess this is some sort of configuration, but that’s not important now).
2. Both the loader file and the `Application` depend on that **_something_** in order to do their work.

Much better, isn’t it?

Let’s take a dig at our second example. We could refactor this in a couple of ways: switch to `import`/`require` for supported browsers, or use build tools that would provide polyfills for that. But there’s a small change we could make that would make things somewhat better:

```
<script src="//some-cdn/cart-fx.js"></script><script src="//some-cdn/cart-utils.js"></script>
```

```
/* lots and lots of code */
```

```
<script>var cart = new CartFx.Cart(CartUtils.CartManager.default, new Customer());</script>
```

By attaching the `CartManager` and `Cart` objects onto the global `CartFx` and `CartUtils` objects, we’ve effectively moved them into namespaces. We would do the same for any other variables those libraries want to make available, reducing the number of potentially hidden dependencies to just one per module.

#### Sometimes, you just can’t help it

There are times where you might be constrained by available tools, limited resources and whatnot. It’s important, though, to keep in mind that what seems so obvious to you, the author of the code, might not be so to a newcomer. Look for little optimizations you can make to improve this.

Have any experiences with hidden dependencies or techniques for handling them? Do share in the comments.

