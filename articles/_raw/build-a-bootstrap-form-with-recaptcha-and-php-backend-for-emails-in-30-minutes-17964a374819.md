---
title: How to build a Bootstrap email form with ReCaptcha and PHP in 30 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T08:38:25.000Z'
originalURL: https://freecodecamp.org/news/build-a-bootstrap-form-with-recaptcha-and-php-backend-for-emails-in-30-minutes-17964a374819
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-rFtK5Bs2Y2Ugvib.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ondrej Svestka

  In this tutorial, I will show you how to easily and quickly add a captcha to your
  Bootstrap form to prevent spam. We will be using Google’s ReCaptcha, the most popular
  Captcha solution today.

  As a base, I will be using an HTML conta...'
---

By Ondrej Svestka

In this tutorial, I will show you how to easily and quickly **add a captcha to your Bootstrap form to prevent spam**. We will be using Google’s **ReCaptcha,** the most popular Captcha solution today.

As a base, I will be using [**an HTML contact form**](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form) with the PHP backend **from one my previous tutorials. Y**ou can use it with any other Bootstrap form that you have.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-rFtK5Bs2Y2Ugvib.png)

Our form will be using **HTML5** syntax sprinkled with some **Bootstrap scaffolding** and a **JavaScript validator**.

**We will submit it via AJAX** (the page will not reload), and then process the form values with PHP.

And finally, we will send an email with PHP and return a response to the original page that will be shown in a status message above the form.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Lm6jtqIQlaFNeeXU.gif)
_This will be the result. See it also live [in the demo](https://bootstrapious.com/tutorial/recaptcha/" rel="noopener" target="_blank" title=")._

As I mentioned before, I will mostly focus on **working with ReCaptcha** today and not on the Bootstrap form itself too much. So, in case you have missed it, have at least [a quick look at my Bootstrap form tutorial](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form).

#### Demo & Links

* [See the demo](https://bootstrapious.com/tutorial/recaptcha/)
* or [download the files](https://bootstrapious.com/p/bootstrap-recaptcha#demo-and-links) for the tutorial

**Ok, let’s do it!**

### 1. Register your site

To be able to use ReCaptcha, you will need to **register your website** on [ReCaptcha’s website](https://www.google.com/recaptcha/admin) first.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GRk4rP9nglbHOw7V.png)

After successful registration, you will get **a pair of keys** to use with your ReCaptcha. Leave the page open or copy the keys to a text file, we will need them soon.

![Image](https://cdn-media-1.freecodecamp.org/images/0*G0dDkucp15TJJFNa.png)

### 2. HTML

We will use the contact form’s template from the [previous tutorial](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form) + we will add a reCAPTCHA element and a hidden input next to it to help us with the JavaScript validation.

**Let’s explain the HTML code a bit:**

* we have an HTML contact form ready written with the Bootstrap markup
* the main 3rd party scripts & stylesheets that will be used are: jQuery, Bootstrap 4, CSS, and JavaScript

**To add a ReCaptcha to your form, you just need:**

* to include `<div class="g-recaptcha" data-sitekey="6LfKURIUAAAAAO50vlwWZkyK_G2ywqE52NU7YO0S">`</div>on a place you need it i_n your form (replace the site key with your own key from the_ first step)
* Include the ReCaptcha JS to initialize ReCaptcha on the page — `<script src='https://www.google.com/recaptcha/api.js'><`;/script>
* I also use `data-callback` and `data-expired-callback` attributes on the `g-recaptcha` div — these are optional and I will use them to make ReCaptcha cooperate with the validator

**Here’s the full code of the form**

### 3. PHP

In the PHP, we will be using [Google’s client library](https://github.com/google/recaptcha) that will take care of the verification.

You can use Composer to install it in your project, download it from GitHub or simply use the version I included in the [Download package](https://bootstrapious.com/tutorial/files/recaptcha.zip).

The major part of the code is also from my previous tutorial, so I will try to recap it just briefly.

**Let’s name the file** `contact.php` **and see what we’ll do in it:**

* in the beginning, we need to require the ReCaptcha PHP library — `require('recaptcha-master/src/autoload.php');`
* and do some configuration stuff, for example entering your Secret Key — `$recaptchaSecret = 'YOUR_SECRET_KEY';`
* We also set the additional variables as the emails to send the email to, subject and the success/error messages
* then, you’ll need to initialize the class with your Secret Key - `$recaptcha = new \ReCaptcha\ReCaptcha($recaptchaSecret)`;
* send a call to validate the ReCaptcha — `$response = $recaptcha->verify($_POST['g-recaptcha-response'], $_SERVER['REMOTE_ADDR'`]);
* throw an exception if the validation fails — `if (!$response->isSuccess()) {.`..}
* the script then composes the email message, sends it, and returns a JSON response. _(The form is submitted by AJAX in default.)_

### 4. JavaScript

Our JavaScript file `contact.js` will take care of:

* **validating the inputs** with [Bootstrap validator](http://1000hz.github.io/bootstrap-validator/)
* handling the **JS callbacks from ReCaptcha** _(we will fill in the hidden_ `input[data-recaptcha]` _based on the ReCaptcha’s response. If successful, we fill this input in = the validator will consider the form being valid.)_
* **AJAX sending the form**
* and lastly, **displaying the success or error message** and also emptying the form.

**Here’s the code:**

### 5. Result

This is it!

You should have a working contact Bootstrap contact form with ReCaptcha and PHP background now.

#### Thanks for the 50 clap ? if you enjoyed this article! A**lso, check out my other B[ootstrap tutorials](https://bootstrapious.com/tutorials) or my B[ootstrap templates.](https://bootstrapious.com/free-templates)**

_Originally published on [Bootstrapious blog](https://bootstrapious.com/p/bootstrap-recaptcha)._

### About The Author

Ondrej Svestka is a Bootstrap and front-end enthusiast and founder of [Boostrapious](https://bootstrapious.com/).

