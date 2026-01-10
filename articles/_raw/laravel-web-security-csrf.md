---
title: What is Cross-Site Request Forgery (CSRF)? Laravel Web Security Tutorial
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2022-10-04T21:40:49.000Z'
originalURL: https://freecodecamp.org/news/laravel-web-security-csrf
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Dark-Neon-Simple-Futuristic-UIUX-Designer-LinkedIn-Banner--7---1-.png
tags:
- name: Laravel
  slug: laravel
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'In this tutorial, you''ll learn about Laravel web security and how to secure
  your web applications and protect them from Cross-Site Request Forgery, or CSRF
  attacks.

  CSRF is a malicious activity that involves an attacker performing actions on behalf
  o...'
---

In this tutorial, you'll learn about Laravel web security and how to secure your web applications and protect them from Cross-Site Request Forgery, or CSRF attacks.

CSRF is a malicious activity that involves an attacker performing actions on behalf of an authenticated user. Fortunately, Laravel provides out-of-the-box measures to prevent this type of vulnerability.

**In this tutorial, you'll learn:**

* What is CSRF?
* How to prevent a CSRF request
* How and where CSRF verification happens

## What is CSRF?

CSRF attacks hijack user sessions. They do this by tricking a user into sending a request through hidden form tags or malicious URLs (images or links) without the user's knowledge. 

This attack leads to a change in the state of the user session, data leaks, and attackers can sometimes manipulate end-users data in an application.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-03-at-14.59.14-1.png)
_CSRF Explainer_

The image above illustrates this scenario where an Actor (User) sends a request from **malicious.xyz** through the **webserver** to **application.xyz**. They then realize that their information has been manipulated by **updating** their **password**.

## How to Prevent CSRF Requests

For each user session, Laravel generates secured tokens that it uses to ensure that the authenticated user is the one requesting the application. 

Since this token changes each time a user session is regenerated, a malicious attacker can not access it. 

Each time there’s a request to modify user information on the server-side (back end) like `POST`, `PUT`, `PATCH`, and `DELETE`, you need to include a `@csrf` in the HTML form request. The `@csrf` is thus a Blade directive used to generate a hidden token validated by the application. 

**Blade directive** is the syntax used within the Laravel templating engine called **Blade**. To create a blade file you give it a name – in our case form – followed by the blade extension. This means that the file will have the name `form.blade.php`.

You use the blade file to render views to users on the webpage. There are a couple of default directives or blade shorthand syntaxes you can use. For example, `@if` checks if a condition is met, `@empty` checks if records are not empty, `@auth` checks if a user is authenticated, and so on. 

But here we are more interested with the `@csrf` directive. Here's how you use it:

```php
<form method="POST" action="{{route('pay')}}">

    @csrf
    
</form>
```

Earlier Laravel releases used to look somewhat like this – both work and do the same thing behind the scenes.

```php
<form method="POST" action="{{route('pay')}}">
    
    <input type="hidden" name="_token" value="{{ csrf_token() }}" />
    
</form>
```

When the CSRF token is not present in the form request that gets sent or if it appears invalid, Laravel throws an error message "Page Expired" with a status code 419.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-03-at-15.11.43-1.png)
_Laravel 419 Page Expired_

## How and Where CSRF Verification Happens

The `VerifyCsrfToken` middleware handles CSRF verification within the Laravel application. The middleware is registered in the Kernel.php, and found within the application's web route middleware group. This means the middleware is triggered for requests within the Web, not related to APIs.

```php
protected $middlewareGroups = [
        'web' => [
           .
           .
           .
           .
           .
            \App\Http\Middleware\VerifyCsrfToken::class,
        ],
    ];
```

The VerifyCsrfToken middleware extends the `Illuminate\Foundation\Http\Middleware\VerifyCsrfToken` class. This means that the CSRF verification is housed within the class. 

Let's dive deeper to learn how Laravel handles the CSRF verification. 

Within the class, we have the `tokensMatch` function.

```php
protected function tokensMatch($request)
    {
        $token = $this->getTokenFromRequest($request);

        return is_string($request->session()->token()) &&
               is_string($token) &&
               hash_equals($request->session()->token(), $token);
    }
```

The function does two things:

1. `$this->getTokenFromRequest` gets the token from the incoming request attached via a hidden field or the request's header. The token is decrypted and then returned to the token variable.

```php
protected function getTokenFromRequest($request)
    {
        $token = $request->input('_token') ?: $request->header('X-CSRF-TOKEN');

        if (! $token && $header = $request->header('X-XSRF-TOKEN')) {
            try {
                $token = CookieValuePrefix::remove($this->encrypter->decrypt($header, static::serialized()));
            } catch (DecryptException $e) {
                $token = '';
            }
        }

        return $token;
    }
```

2. Cast both request token and session to a string and then use the PHP built-in hash_equals to compare if both strings are equal using the same time. The result of this operation is always a **bool (true) or (false)**.

## Wrapping up

In this article, you have learned about CSRF, how to handle and protect against it, and the behind-the-scenes of how Laravel does the verification.

You can read more about this in the [Laravel documentation](https://laravel.com/docs/9.x/csrf). And you can read more about [PHP hash equals in the docs here](https://www.php.net/manual/en/function.hash-equals.php).

Happy Coding!

