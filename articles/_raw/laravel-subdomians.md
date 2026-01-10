---
title: Laravel Subdomains – How to Create and Manage Subdomains in Your Apps
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2021-09-16T17:19:06.000Z'
originalURL: https://freecodecamp.org/news/laravel-subdomians
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/subdomain-structure.png
tags:
- name: Laravel
  slug: laravel
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: "Modern web applications usually perform more than one function. They often\
  \ have more than one section, offer more than one service, and have a couple of\
  \ clients.\nBut the more functionality the app has, the clumsier your route paths\
  \ will get. \nWhat if..."
---

Modern web applications usually perform more than one function. They often have more than one section, offer more than one service, and have a couple of clients.

But the more functionality the app has, the clumsier your route paths will get. 

What if there was a way to separate all these parts into smaller components with better and cleaner routes? Something that users could easily access and use independently, under the same website?

Fortunately, there is such a way: **Subdomains**.

## What is a Subdomain?

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-75.png)
_Credit: [Electroica Blog](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fblog.electroica.com%2Fgoogles-top-searches-india-2019%2F&amp;psig=AOvVaw2bx9ZwYjA8ldb4CuGhccN-&amp;ust=1631749915996000&amp;source=images&amp;cd=vfe&amp;ved=0CAwQjhxqFwoTCMiBuKbU__ICFQAAAAAdAAAAABAh)_

Here's a [basic definition of a subdomain](https://www.domain.com/blog/subdomain/):

> A subdomain is, as the name would suggest, an additional section of your main **domain name**. You create subdomains to help organize and navigate to different sections of your main website. Within your main domain, you can have as many subdomains as necessary to get to all of the different pages of your website.

So let's say you have a website called mysite.com. You have a blog section, a store section, and a general website section for about and contact pages. The website could have subdomains like blog.mysite.com and store.mysite.com, where the main website would use the main domain.

## Why Should You Use Subdomains?

Subdomains are pretty useful, and here are some of their main advantages:

* Users can easily remember you website domains, which means they'll likely use your site more.
* You'd be able to split your large application into smaller groups, so it will be easier to manage, debug, and update or upgrade.
* Subdomains also allow for personalisation – for example, a blog app could give each user their own subdomain (like _username.domain.com_).
* Subdomains also let developers test version of their application before pushing to production. You could have a _beta.site.com_ to preview changes before deploying them to the main site.

Let's see how all this works by building an actual project and testing it out.

## How to Create New Laravel Project

I have [Docker](https://www.docker.com/) setup on my laptop, so I'll be using the [Sail](https://laravel.com/docs/8.x/sail) setup that [Laravel](https://laravel.com/docs/8.x/) ships with.

```bash
curl -s "https://laravel.build/example-app" | bash
```

> _You can use any other method you feel comfortable with. See the [docs](https://laravel.com/docs/8.x/installation) for help._

### Start the Laravel Server

```bash
./vendor/bin/sail up -d

```

## How to Configure the Route Files

In your `web.php` file, you can define individual routes with their domain (or subdomain) like this:

```php
Route::get('/', function () {
    return 'First sub domain';
})->domain('blog.' . env('APP_URL'));
```

Now you can access the page at _blog.domain.com_.

But more often than not, you'll have more than one path in an application, like a domain and subdomains. So, it's a good idea to use a route group to cover all the routes in the same domain or subdomain.

```php
Route::domain('blog.' . env('APP_URL'))->group(function () {
    Route::get('posts', function () {
        return 'Second subdomain landing page';
    });
    Route::get('post/{id}', function ($id) {
        return 'Post ' . $id . ' in second subdomain';
    });
});
```

Now, all the routes for the domain can be handled in one place.

## How to Make Subdomains Dynamic

As I mentioned earlier, you can use subdomains to allow personalisation in web applications, so they need to be dynamic. For example, [Medium](https://medium.com) gives authors domains like _username.domain.com_.

You can do this easily in Laravel as subdomains may be assigned route parameters just like route URIs. This allows you to capture a portion of the subdomain for usage in your route closure or controller.

```php
Route::domain('{username}.' . env('APP_URL'))->group(function () {
    Route::get('post/{id}', function ($username, $id) {
        return 'User ' . $username . ' is trying to read post ' . $id;
    });
});
```

In this example, you could have a domain like _zubair.domain.com_ with route parameters, too_._

## Route Service Providers

For very large applications, the `web.php` could get a bit messy if the routes keep increasing. It is best to split the routes into different files, preferably by subdomain.

In your `RouteServiceProvider.php` file, you'll see this code in the `boot` method:

```php
public function boot()
    {
        $this->configureRateLimiting();

        $this->routes(function () {
            Route::prefix('api')
                ->middleware('api')
                ->namespace($this->namespace)
                ->group(base_path('routes/api.php'));

            Route::middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/web.php'));
        });
    }
```

This is Laravel's default route configuration to separate API routes from web routes. We'll use this same file to separate subdomains.

Add the following to the method:

```php
Route::domain('blog.' . env('APP_URL'))
                ->middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/blog.php'));
```

This is telling Laravel that whenever someone hits the _blog.domain.com_ endpoint, look for the route in the blog.php (that we are yet to create).

We can go on to create the `blog.php` file in the `routes` folder, and add the following content:

```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return 'Route using separate file';
});

```

At this point, you're done with all the code! All that's left is some server configuration.

## Server Configuration

If you're using a service such as [Laravel Valet](https://laravel.com/docs/8.x/valet), it is way easier to setup.

In the root directory of your project, run:

```bash
valet link domain
valet link blog.domain
```

And if you're not using Laravel Valet, you can add this to your `/etc/hosts/` file:

```
127.0.0.1       domain.test
127.0.0.1       blog.domain.test
```

This is basically just mapping the domain to the IP.

## **Summary**

Now you know how to set up and manage subdomains in your Laravel apps. You can find all the code for this article [here](https://github.com/Zubs/subdomain-test).

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

