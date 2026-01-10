---
title: PHP Tutorial – How to Setup PHP and XAMPP for Your Project
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-02T15:11:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-php
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/PHP.jpg
tags:
- name: PHP
  slug: php
seo_title: null
seo_desc: 'Hello and welcome to this tutorial, everyone. Today, we''ll look at how
  you can set up and use PHP in a project.

  But before we get started, we''ll need to understand what PHP is all about.

  What is PHP?

  PHP is an abbreviation or acronym for "Hypertext P...'
---

Hello and welcome to this tutorial, everyone. Today, we'll look at how you can set up and use PHP in a project.

But before we get started, we'll need to understand what PHP is all about.

## What is PHP?

PHP is an abbreviation or acronym for "Hypertext Preprocessor." It's a web-based open source server-side scripting language that's integrated in your HTML files.

You use it to make webpages that are both responsive and interactive with the database.

## Advantages of PHP

PHP has many benefits, and here are a few of them:

### PHP is Simple to Use

You don't need to study extensively to learn and use PHP because its syntax is sensible and well-organized. The command functions are also easy to work with because they help you understand exactly what they do.

### PHP is Flexible

Flexibility is a major benefit that every scripting language should have, and PHP is no exception. Even after a project has been launched, a PHP developer has the ability to make changes to the project.

### PHP Helps You Collect Data from Forms

You can use PHP to collect data from a form that has been created with HTML (like Name, E-mail, Phone Number, or Password). Many websites use this particular function of PHP.

### PHP Has Good Security

PHP does not outsource the data or information collected from forms. This is part of the reason why most most website and social media apps make use of it because it has a secure database system.

## How to Install and Setup PHP in your Project

To get started with PHP, you'll need three things: a code editor for writing your code, an installed version of PHP, and XAMPP.

We'll be using Visual Studio code in this example, and I'll teach you how to install a version of PHP and XAMPP on your PC.

Go to the [PHP website](https://www.php.net/) and click on download in the navigation bar. The current version should be at the top.

Click on "Windows downloads," and when it opens, scroll down a little and you should see a section that has "VS16 x64 Thread Safe (2022-May-11 09:29:42)." The section contains a "zip" file below it – click on it and wait for your download to finish.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_57_44-PM-1.png align="left")

*Click on the Download Button*

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_57_58-PM.png align="left")

*Click on Windows downloads*

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_58_42-PM.png align="left")

*Below Thread Safe click on the zip file to download*

When the download is complete, go to your computer's downloads folder and look for a PHP zip file. Right-click it and select extract file. It's important to save the file to your local drive.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-20-15-25-892-1.jpg align="left")

*Zip folder and the extracted folder*

Open the Local Disk and open the extracted PHP folder. Click once on the bar that shows the current directory then copy the name of the directory, which should be in this format: C:\\php-8.1.6.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-05-30-20-30-59-641.jpg align="left")

*Click the bar once and copy the Directory name*

In your windows bar, search for “Edit the systems environment property”. Click on the “environment variables” button, click on “Path”, and then click on the edit button below. It opens a space where you can create a new variable.

So click on the new button and then paste the name of the directory you copied earlier (which should be “C:\\php-8.1.6”) and click ok for all of them.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Environment.jpg align="left")

To test if PHP is now installed in your computer, search for the command prompt in Windows by using the search keyword `cmd`. Open it then type `php --version` and click enter. You should see something similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-20-46-16-280.jpg align="left")

*PHP version 8.1.6*

The current version of PHP is installed on our PC as seen in the image above. The next step is to get XAMPP.

## What is XAMPP?

The acronym XAMPP stands for cross-platform, Apache, MySQL, PHP, and Perl. XAMPP is a free and open source web server that allows you to develop, test, and build websites on a local server.

Unlike PHP, XAMPP installation is quite simple and uncomplicated. Search for "XAMPP Download" in your browser or go to their [website](https://www.apachefriends.org/index.html). You should see the current version of XAMPP for Windows, Linux, and OSX when it opens.

Because I'm using a Windows computer, I simply need to click on the one for Windows, and the download should begin.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-01-27-189.jpg align="left")

*Click the XAMPP for Windows if you are using Windows*

When its done downloading, go to your downloads, right click on the setup file and select “run as administrator”.

This will take you to the **Setup-xampp** wizard:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-14-620.jpg align="left")

*click next*

Click next, and you'll be able to select the components you want:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-22-682.jpg align="left")

***Select components and click next***

Then you'll come to the installation folder. You have to select a folder where you want to install XAMPP. I recommend creating a folder in your local disk to install XAMPP.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-29-806.jpg align="left")

*select an installation folder*

Then you'll select the language. You can select either English or Deutsch (your choice):

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-03-881.jpg align="left")

*select language*

Now you'll get Bitnami for XAMPP:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-08-433.jpg align="left")

*click next*

And you're ready to install:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-25-333.jpg align="left")

*click next*

Be patient while the installation process completes. When it's, done click ok.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-30-643.jpg align="left")

*wait for the installation to complete*

Once the installation process is finished, you can now use XAMPP in you project.

## Why Do You Need XAMPP?

To run PHP for the web, you will need to install a web server like Apache and a database like MySQL – and both are supported by XAMPP.

XAMPP is a local server that can run smoothly on our personal computer, and is accepted in both Windows and Linux. It also helps you test websites and see if they work before actually publishing them to a web server.

## How to Run PHP with XAMPP

To run PHP with XAMPP you will have to go through some steps, and I will break it down so you can understand.

First, open the local storage folder, go to the “xampp” folder and open it. You should see a folder named “htdocs”. Open it then create a new folder in it. In my case I named the folder I created “Demo” (so give your folder the name of your choice).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/1-2-3.jpg align="left")

Next, open your VS code, click on open folder, then go to the location where you saved the folder you created (which in my case I named “Demo”). Create a file with the extension `.php` – in my case I named mine `test.php`. The extension `.php` tells the code editor that we are working on a PHP code/project.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-06-01-22-08-09-094.jpg align="left")

*create a file with an extension of .php*

PHP is run with the `<?php (Code goes in here) ?>` tag. The opening tag is `<?php` then your PHP code goes next before the closing tag `?>`. For example:

```php
<?php
echo “<h1> My Name is Derek </h2>;
?>
```

The echo keyword tells the browser to display `My Name is Derek` while the `<h1></h1>` tells the web browser to format the text to be bold/bigger. Then save it.

After writing the code, open the XAMPP control panel, and start the Apache module by clicking on start under the action section.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/test.php---Demo---Visual-Studio-Code-6_2_2022-1_23_21-AM.png align="left")

Then go to your web browser and in the search bar type `localhost/Demo/test.php`, then enter. Your web browser should be display this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-06-01-22-07-50-039.jpg align="left")

*web display*

If your code was displayed on the web browser, congratulations! You're up and running.

## Conclusion

Thank you very much for following along with this tutorial. I hope you got some value out of this lesson and I hope you'll try using PHP and XAMPP.

Stay tuned for my next tutorial.

Have fun coding!
