---
title: 5 Mistakes Beginner Web Developers Make – And How to Fix Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-05T16:48:42.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-beginning-web-development-students-make
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/varvara-grabova-NCSARCecw4U-unsplash-1.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: coding
  slug: coding
- name: lessons learned
  slug: lessons-learned
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  This list is made up of the most common mistakes I''ve witnessed during nearly a
  decade of teaching beginning web development students.

  My idea for writing this article is not to make fun of beginner mistakes or embarrass
  anyone who is be...'
---

By Dave Gray

This list is made up of the most common mistakes I've witnessed during nearly a decade of teaching beginning web development students.

My idea for writing this article is not to make fun of beginner mistakes or embarrass anyone who is beginner.

Rather, my goal is to educate beginners and hopefully save them from some of these common mistakes.

## We Were All Beginners

If you aren't a beginner, you may think the mistakes listed below are obvious... but remember, obviousness is relative to experience.

Once upon a time, those of us with experience struggled with some of these mistakes, too.

If you are a beginner, I hope this list saves you some time and anxiety in the near future.

Let the countdown begin!

## Mistake #5: Adding Spaces in File Names

You may save your HTML file with the name "my cool page.html", but those spaces between words are a mistake.

Web addresses (aka URLs) cannot have spaces.

If you load this file into your browser, you are going to see "my%20cool%20page.html" in the browser address bar. Spaces must be encoded because they are not allowed in URLs.

If you want to see separation between the words in your file names, use an underscore (my_cool_page.html) or a hyphen (my-cool-page.html).

As a beginner, you probably aren't too worried about search engine optimization (SEO), but [Google has noted they prefer hyphens](https://developers.google.com/search/docs/advanced/guidelines/url-structure) in file names over underscores.

## Mistake #4: Ignoring cAsE sEnSiTiViTy

If you are using Windows for your development environment, you might not notice a problem when you inconsistently use lowercase and capital letters. This is a mistake.

Let's say you created a CSS folder named "Css" and a file within it named "Main.css". But in your code, you link to it like this:

```
<link rel="stylesheet" href="css/main.css">

```

While you're working on your project, there is no problem.

But when you load your project to a web server...**Boom!** No CSS is applied.

Many web servers have some version of Linux or Unix running instead of Windows. You may have heard of the LAMP stack. Linux is the L in LAMP.

These systems are case sensitive.

Therefore, it is best to use lowercase file names and directory names all the time unless there is a specific naming convention that uses a capital letter. At that point, the file names will still always be consistent. And consistency is what will prevent this mistake.

## Mistake #3: Not Understanding File Paths

Students that do not understand how to link files within different directories often dump all their files in the root directory in order to access them. This is a mistake that leads to an unorganized file tree.

Not long after you start learning HTML, you start learning how to link to other HTML and CSS files.

This is fairly straightforward when the files are in the same directory. Even in the example above, we just looked inside the CSS directory for the main.css file.

It starts to get more complicated when we need to go up a directory instead of (or before) going down into one.

In the example below, we are setting the background-image for a web page in our main.css file. The main.css file is in the CSS directory. We are linking to an image in the img directory.

```
body {
     background-image: url("../img/moon.png");
}

```

Both of these directories (aka folders) are in the root directory. Therefore, we need to go up and out of the CSS directory and then down into the img directory.

We go up one directory with two dots: ".."

From there, we go down into the img directory to link to the moon.png file.

If we needed to go up two directories, the file path would start like this: "../../"

Remember, one dot indicates the directory you are in. Two dots indicates the directory above where you currently are.

## Mistake #2: Not Naming Your Default Page Index

Naming your default page something other than "index" is a mistake.

Web servers look for an index file.

When you're working with HTML, you should have an index.html file.

This file will load by default without showing the file name at the end of the URL.

That's why you can go to your favorite dot com or other web address and not see "/index.html" after their ".com". The index file loads by default.

Granted, your favorite website may use more than just HTML, but this concept carries over to other technologies like PHP (index.php), React (index.js), and more.

As you continue to learn, you will find some developers choose other file names when utilizing other technologies, but as a beginner, stick with index.

## Mistake #1: Not Taking A Break!

I receive emails when students are frustrated.

They have poured over their project for hours and cannot find the error.

Often, the problem is a misspelled tag or variable, a missing semi-colon, or other small syntax error.

_This happens to us all._

After staring at code for an extended time period, our vision blurs, our brains fizzle, and what would have been easy to see with fresh eyes becomes impossible.

Don't feel bad. Don't blame yourself. Just get up!

Take a walk. Get some coffee. Take a nap. Whatever snaps you out of the haziness and gives you fresh eyes and a clear head again.

Really, this mistake isn't just for beginners. It can happen to anyone.

I must remind myself to take breaks, too.

Come back to the code when you are refreshed and that error you couldn't find will often be obvious!

## Conclusion

As you gain experience, you will quickly move past these common mistakes.

What was once difficult to understand will become clear.

If these common mistakes were obvious to you, congrats! You've already got some experience.

If you're just starting out, I hope this review of common beginner mistakes saves you both time and frustration in the near future.

I'll leave you with a video from my YouTube Channel that counts down the Top 10 Biggest Beginner Mistakes. Watch to see examples of the 5 mistakes I discussed in this article plus 5 additional common beginner mistakes:

%[https://youtu.be/5xkztyg12FU]


