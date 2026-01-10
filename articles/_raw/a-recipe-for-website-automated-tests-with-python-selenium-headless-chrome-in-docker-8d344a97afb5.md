---
title: A recipe for website automated tests with Python Selenium & Headless Chrome
  in Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T10:58:19.000Z'
originalURL: https://freecodecamp.org/news/a-recipe-for-website-automated-tests-with-python-selenium-headless-chrome-in-docker-8d344a97afb5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LFMkcmJNOOgGK1qyKYebLw.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Joyz

  The QA team leads bug catching, but manual testing is not scalable when your company
  takes on more projects. Since my company sends builds every two weeks, the QA team
  wants to test every build before we pass them to our clients.

  To improve Q...'
---

By Joyz

The QA team leads bug catching, but manual testing is not scalable when your company takes on more projects. Since my company sends builds every two weeks, the QA team wants to test every build before we pass them to our clients.

To improve QA, I’ve helped modify project management processes, recruited a team of exploratory testers, and built automated testing tools for continuous integration as a QA Engineer. Most of the tools I build use open-source or free libraries.

Below is a guide for my open-source [Github repo](https://hub.docker.com/r/joyzoursky/python-chromedriver/) with 100,000+ docker image pulls to help development teams and freelance developers set up their own automated tests.

### Our Task

We will go through the process step-by-step to see how to set up a test with [Selenium](https://www.seleniumhq.org/), which automates browsers to perform tests. In this example, we will use headless Chrome to load our website and perform a simple click on the button we want to test on the site.

### Setting up the Headless chrome

Starting up a Chrome browser in Docker to run a Selenium test takes just a minute. Once it works, it works with any automated CI builds.  
   
 Here is an example:  
   
 First, open your terminal and go to your working directory.

```
$ cd [your working directory]
```

Then pull and run this docker image from [joyzoursky/python-chromedriver](https://hub.docker.com/r/joyzoursky/python-chromedriver/). We will run the Selenium test inside the Docker container.

```
$ docker run -it -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.6-alpine3.7-selenium shUnable to find image 'joyzoursky/python-chromedriver:3.6-alpine3.7-selenium' locally3.6-alpine3.7-selenium: Pulling from joyzoursky/python-chromedriverff3a5c916c92: Pull complete471170bb1257: Pull completed487cc70216e: Pull complete9358b3ca3321: Pull complete78b9945f52f1: Pull complete66eb40d9fb29: Pull complete36cb996dbd54: Pull complete8e6f0ca23b1a: Pull completed5a3895f190c: Pull completeDigest: sha256:c51c240f1a472b0f252e96cd39678c7d039b757b83e46bf8ed182e95caaf02e7Status: Downloaded newer image for joyzoursky/python-chromedriver:3.6-alpine3.7-selenium
```

Now the container is ready. Let’s move to the workspace and try out the code.

```
/ # cd /usr/workspace/
```

### Now, we can script our test

Let’s start Python.

```
/usr/workspace # pythonPython 3.6.4 (default, Jan 10 2018, 05:20:21)[GCC 6.4.0] on linuxType "help", "copyright", "credits" or "license" for more information.>>>
```

Before trying the code, import the Selenium webdriver from the pre-installed package.

```
>>> from selenium import webdriver
```

Then let’s start the headless Chrome. Some options are required to pass to the driver to avoid crashing during startup.

```
>>> chrome_options = webdriver.ChromeOptions()>>> chrome_options.add_argument('--no-sandbox')>>> chrome_options.add_argument('--window-size=1420,1080')>>> chrome_options.add_argument('--headless')>>> chrome_options.add_argument('--disable-gpu')>>> driver = webdriver.Chrome(chrome_options=chrome_options)
```

Now the browser is already opened in the container, but we cannot see it. Let’s try to go to this website and check the inner text of the top right button.

![Image](https://cdn-media-1.freecodecamp.org/images/d8pHoiJdyENTGuhTRqyEMGsJ2NufawIOAFfQ)

```
>>> driver.get('https://www.oursky.com/')>>> el = driver.find_element_by_class_name('btn-header')>>> el.text'START YOUR PROJECT'
```

Let's find the element we wish to interact with, for example the button in the header “btn-header”.  
   
 Got it! Now, let's try to trigger a click on the button.

```
>>> el.click()>>> driver.current_url'https://oursky.com/enquiry/general/'
```

Success! The driver goes to the expected URL after clicking the button.  
   
You can now run your scripts in the container, or use the image in a CI build script. You can also build your own image with more pip packages installed, so you can automate more powerful tests.  
   
 Enjoy!  
   
 You may find the [GitHub repository of the docker image](https://github.com/joyzoursky/docker-python-chromedriver) here with the testing environment set up.

Also take a look at the full [Python Selenium script example](https://github.com/joyzoursky/selenium-template), so you can customize it into your own test.

![Image](https://cdn-media-1.freecodecamp.org/images/0pEr4VFOcP6iQEO9cTpQjFwcPGq2Jq4Qlzyr)

_I work for the Hong Kong and Taiwan-based software development company [Oursky](https://oursky.com). We build digital products for clients and [developer tools](https://oursky.com/products/) like our opensource BaaS,_ _Skygear,_ _which helps developers build apps faster._

