---
title: How to Set Up reCAPTCHA v3 in a Laravel Project
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2021-09-20T22:26:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-recaptcha-v3-in-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-davis-sanchez-1727004.jpg
tags:
- name: Laravel
  slug: laravel
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: "In this article, you'll learn how to set up reCAPTCHA v3 in your Laravel\
  \ project. This can be a bit tricky, so I'll help you simplify the process here.\
  \ \nWhat is reCaptcha?\nreCaptcha is a Google service provided for free that helps\
  \ you protect your we..."
---

In this article, you'll learn how to set up reCAPTCHA v3 in your Laravel project. This can be a bit tricky, so I'll help you simplify the process here. 

## What is reCaptcha?

[reCaptcha](https://developers.google.com/recaptcha/) is a Google service provided for free that helps you protect your websites from spam and malicious attacks. 

The new version, V3, has many improvements over previous versions thanks to the new captcha challenges. It returns a score and analytics you can use to take appropriate action for your website.

Here's what the previous version of reCaptcha looks like – but as of the latest release (v3), reCaptcha has changed a lot and has a better user experience.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/newCaptchaAnchor.gif)
_Previous reCaptcha Version_

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-26-at-04.11.28.png)
_Previous reCaptcha Version_

## What you'll learn

By the end of this article, you'll have learned the following:

1. How to integrate the reCaptcha v3 into your Laravel project
2. How to setup a Google reCaptcha admin dashboard
3. How to view your website reCaptcha scores and analytics to help you make better security decisions

## How to Setup reCaptcha in a Laravel Project

You can follow these simple steps to get reCaptcha set up on your project.

1. Install this [laravel project](https://laravel.com/docs/8.x/installation) if you haven't done so yet
2. In the terminal, pull the open-source package into your project with composer.

```
composer require biscolab/laravel-recaptcha
```

3.  Publish the `recaptcha.php` with this command:

```php
php artisan vendor:publish --provider="Biscolab\ReCaptcha\ReCaptchaServiceProvider"
```

This will create a file in the config directory, called `config\recaptcha.php`, where we will add more reCaptcha configurations.

4.  [Visit this link](https://www.google.com/recaptcha/admin/create) to create a reCaptcha admin account for yourself.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-23-10-59-07.png)
_Register reCaptcha v3_

To create the reCaptcha admin, you can do the following:

* Add your site name to the label – `localhost`  or `examplesite.com`
* Select v3 as the reCaptcha type
* Include domains in the domain section (`localhost` or `examplesite.com`)
* Add the owner's email address to the owner's section
* Check the "accept terms and service" box 

Just a note – the localhost is for the sole purpose of developing locally. As such, it should be updated before moving to a production environment.

5.  Add the reCaptcha to your site

Click the submit button and save your secret keys. 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-23-11-16-17.png)
_Adding reCaptcha to your site within the .env_

6.  Add the site keys to the `.env` file of your project:

```php
RECAPTCHA_SITE_KEY=ADD_YOUR_SITE_KEY
RECAPTCHA_SECRET_KEY=ADD_YOUR_SECRET_KEY
RECAPTCHA_SITE=https://www.google.com/recaptcha/admin/
```

Since you have made changes to the `.env`, it's best to clear all cached configurations so that the new changes take effect. Use `php artisan optimize:clear` in your terminal.

7.  Within the `config > recaptcha.php` file, update the property of the version to V3. It's also important to note that the `api_site_key` and `api_secret_key` generated via the admin dashboard will be referenced from what we set in the .env file of the project.

```php
return [
	'version'                      => 'v3'
]
```

You can now head over to the analytics page of the reCaptcha admin to view how well your site is performing, view your scores, and make decisions when you're in a production environment.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-24-10-27-04-1.png)
_reCaptcha analytics page_

The below image shows that reCaptcha has been implemented.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-19-at-15.37.00.png)



## Conclusion

At the end of this article, I hope you'll find it easier to set up reCaptcha and that you'll have a better understanding of what it's all about. Now you should be able to set up the most recent version within your Laravel project.

### Resources

* What is [reCaptcha](https://developers.google.com/recaptcha/)?
* Laravel reCaptcha [repo](https://github.com/biscolab/laravel-recaptcha)
* Laravel reCaptcha [docs](https://laravel-recaptcha-docs.biscolab.com/docs/configuration) 


