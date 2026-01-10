---
title: How to Set Up Laravel 8 on Your Android Phone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-11T16:34:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-laravel-8-on-android-phone
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-lisa-1092644--1-.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Laravel
  slug: laravel
- name: mobile app development
  slug: mobile-app-development
- name: PHP
  slug: php
seo_title: null
seo_desc: "By Precious Oladele\nHey, how are you doing? In this article, I'm going\
  \ to show you how you can install Laravel 8 on your phone. \nTo get the most out\
  \ of this guide, you should have some knowledge of PHP and you should know what\
  \ Laravel is. But if you ..."
---

By Precious Oladele

Hey, how are you doing? In this article, I'm going to show you how you can install Laravel 8 on your phone. 

To get the most out of this guide, you should have some knowledge of PHP and you should know what Laravel is. But if you don't, don't worry – I will explain the basics so you can get started.

## What Is Laravel?

Laravel is a web application framework with expressive, elegant syntax. It's built on PHP, which means that Laravel is PHP but it makes things easier to work with.

It comes with lots of packages for various features, like authentication, so we don't need to write authentication ourselves. To learn more about what Laravel can do, you can visit the site at [laravel.com](https://www.freecodecamp.org/news/p/8cc4755b-3b0b-4751-991c-a7b4997c0335/laravel.com).

## Why I wrote this tutorial

I created this tutorial because I want people interested in programming who don't have a laptop or pc to be able to build things on their phones. 

My [last post on freeCodeCamp](https://www.freecodecamp.org/news/how-to-code-on-your-phone-python-pydroid-android-app-tutorial/) made me realize that people are interested in learning how the tech works, so that's why I'm making more guides like this.

So let's dive into it. In this tutorial I am going to show you how you can install composer.php and use it to set up Laravel 8 on your phone 🔥🔥. 

I am Precious Oladele, and I'm almost 19 this month 🥴. I'm from Nigeria and I will be taking you through this process. And if you're wondering how I know so much about this, it's because I also don't have a laptop so I explore with my phone instead 😎.

## Requirements

To go through this tutorial, you'll need an Android phone with V6.0+.

## Set up

We need to head over to the Play Store and download **Termux:**

![Image](https://lh6.googleusercontent.com/cQlgYSj1hH3487jHevQn4eKEjC51xAn5vm0fo6tL8yfNV-nwTeLFW2kv480G5i-OjxtaKXCNQ2c5q36ywH5nqjitwKBjieL7NC4ZXmw7K3WbsuxrsKgAaQBslE9uFg_xnSOFdXc)

**Termux** is a Linux-based system which we can use on our phones. It's as simple as using your regular Linux – you can install anything, even Kali, Ubuntu, or whatever you want. But for this tutorial we will be using it to set up Laravel 8 on our mobile phone.

## Download composer

Before we download composer, we need to open up our **Termux** app and type in this command:

```
termux-setup-storage
```

It'll ask you for storage permissions, so go ahead and click accept. Once you're done head over to [https://getcomposer.org/download/](https://getcomposer.org/download/).

![Image](https://lh4.googleusercontent.com/6DrBqRU9swO3NdA0iEKhzhvK7bQtH3dLdKdx69YrCQboxPLIi-seYv84u_5I4dTAcAqAayNRv6wxlMxxLkivcLYi0N5-iLLYAwB9nzVKvxdMFRaY44ECp5duQLcX7j685RyK-K0)

We need to grab everything there. But before that we need to install **PHP** so we can use it in our app. To do that in your **Termux**, type in the following command:

```
apt install php 
```

and click enter. You should see this:

![Image](https://lh6.googleusercontent.com/jamAoOq-pWlvWz9FfouVQVagFh1stoz-qvrCf4k_Aywd9pabMiDj8ygNR9lqCiXDmwF8M2nzHyrJoDlvrBoPAUSO4w7WY40vQlQqTWzdkDAvK8dlR9XMn19qVhLAu1iwv0E7R24)

Once that is done head over to the composer page and grab the code. We need to do this because Termux is Linux-based. If it was Windows there would be a simple button to download composer.exe there. 

Copy the whole code and head over to Termux where you can paste it in. Then click enter.

When composer is installed you should see something like this:

![Image](https://lh3.googleusercontent.com/Ou_2eDdSX0ZuA0KW29MF2xNMi0YHh3f159-w7ujzGeQtIUEtEZ4mFaq4WYJLFxeGeox7lHmxMswxJcRm1fY6a2C4fZSd0329DnjPcHJvaiUs-vKerof13s2qYMCEi650q-X_qqU)

## How to Install Laravel 8

Before we install Laravel 8, let's check to see if we have a **composer.phar** file. In your **Termux** type this command:

```php
ls
```

and hit enter. You will see the available files there.

![Image](https://lh4.googleusercontent.com/wNOLq4c37i9ccupbMQm64jvOibFEEN2ZuPi_Lez_HO6PZZalo0eI1Lp_XWwvpZK8fWgRedfNsUqo2tYsC4lN54w7TDjjFB4C3k0yR2NVcXiKRY4sFOk6tpCGjVk8X3GaIuMIJEw)

You can see the **composer.phar** file and a **storage** folder. The storage folder grants access to your file manager. Remember the **termux-setup-storage** command you wrote first.

Now let's install Laravel 8. To do so we can either create a project or just install it globally. But it's a bit of a long process when installing it globally on your phone because you need to set a path and so on, and it can be pretty confusing. So in this guide we will create a project instead. 

In your **Termux** go ahead and type this:

```php
php composer.phar create-project laravel/laravel myapp
```

`myapp` is just the project name – you can change it to whatever you want. Then hit enter and wait for the magic to happen.

When you see the below, it means that Laravel has been installed:

![Image](https://lh5.googleusercontent.com/e1T64FywzWaz7amrgF0E5aXE6YqJdjMqCm2ZbAMeVyq2GBJ3wPXpAIxevqulsoPa2LOyqfWTtb6PjbqK48-IcWAssx6Hk3cPHyd5-N6Lw2fFWFdWEM0qhbA6ivKHjt5GH_ED5aI)

Easy as pie. Now to test it, you can cd into `myapp` by typing **`cd myapp`**. Then you can run the Laravel server with **`php artisan serve`.**

Voilà – development has started 🔥

![Image](https://lh5.googleusercontent.com/OmM_BEGUNTploSBEIItrnkn6S_yotTKJPo_q60PP7mx93Uo9V4Tb9p_ucHIiaHAOPbFGL36CWT-zWcGwc-a2FsiNbfyFpbnWu6IjT-MsS2X5TQhI1vAbhU3bGMgbM_tLC_nu3oU)

Now you can open [http://127.0](about:blank).0.1:8000 in your browser and see that Laravel is running:

![Image](https://lh5.googleusercontent.com/iG_uPbC4lzleqSPETYM6pRFsZ1BAj5PbAeTwSDNVWL2_r6V-AxpWk5iYpS-Gs2iBQUmvPZMnVoCjIk9ZtcOJj6QeCOi32dFJ-2zVJC420MIiFyN9pSKUb5sUGI2iSaJ0ITf9Wr4)

 Also make sure you do this so your **Termux** app won't force close when you are coding: 😎

![Image](https://lh5.googleusercontent.com/P6s9dGlmoHGeo2_vAmImYFSXrFgRZTUUlunlOwegzVw8QdLGKoigMhbm5lPlxsE-K5PraWkGlN6VYwzwk16FLi_A4GOGRJdCkPWB3rlc6bbZuJQN7d7s0WKkJTSu1QFTeGXABDM)

## That's it!

Thanks for reading. I hope you learned something from this tutorial. You should now be able to install Laravel on your Android phone and start using it to build apps.

If you want more content from me, you can subscribe to my YouTube channel 🙏😁  
[DevStack](https://youtube.com/channel/UCLcHGKxbEO1XGVETXqzYXLA)

%[https://www.youtube.com/watch?v=VAh6A1SpZfo&t=490s]


