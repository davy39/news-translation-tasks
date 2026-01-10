---
title: File Directories Explained by Getting Dressed in the Morning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-24T21:37:44.000Z'
originalURL: https://freecodecamp.org/news/file-directories-explained-by-getting-dressed-in-the-morning-2f5d0a69cdde
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ST1cC7voeyDyuOWGubNMgw.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you get dressed for work or school in the morning, then you can understand file
  directories.

  When you are building your first website with HTML, CSS and JavaScript, you only
  need a very simple file directory.

  You have one folder...'
---

By Kevin Kononenko

**If you get dressed for work or school in the morning, then you can understand file directories.**

When you are building your first website with HTML, CSS and JavaScript, you only need a very simple file directory.

You have one folder with three total files, and perhaps an image file or two if you are using a background image or a logo.

But, as your site grows, you will need to start using multiple folders to organize your different files. And, if you write your own back-end using a language like Node.js or Ruby on Rails, then you will need to be even more focused on organization.

Here’s the issue: you must use prefixes like “/” and “../” to refer to different folders within your directory. Those brief prefixes give you absolutely no clue as to what they actually do!

File directories are actually pretty similar to the way that a bedroom is organized. So, if you are used to checking multiple places every day before work to assemble an outfit, then you can understand how to navigate file directories.

So let’s get into it! In order to understand this guide, you just need to know the difference between HTML, CSS and JavaScript. [You can check out our guide here](https://blog.codeanalogies.com/2018/05/09/the-relationship-between-html-css-and-javascript-explained/).

### The Setup of A File Directory

Let’s imagine that you have a bedroom with a closet and drawers to hold your clothing. You wake up every day at 7AM, and you need to put together an outfit for work.

In this case, the clothes are like individual files, while the different parts of your room are like folders, since they contain the clothes. Let’s call the top-level folder “/bedroom”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4tREPBNuyL6ADG0FIUI25A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tCzVTBq2cFAc4gYdAgLcPg.jpeg)

Let’s say that you wear a suit to work. Your suit hangs in the closet, while your shirts are in the drawers. Your suit is like an HTML file, while your shirts are like CSS files.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0brd9T7rlUzB2-GJ1dw6eQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EoK-fLFWf9nkClyi7Ei8FQ.jpeg)

In this case, “/bedroom” is the entire **directory**, while “/closet” and “/drawers” are **subdirectories**. And the files themselves are contained in the subdirectory. “/bedroom” is the **top-level** or **root** directory here since it contains our entire project.

Let’s think about how you might get dressed.

1. Wake up
2. Go to closet and pick out an outfit
3. Leave closet
4. Go to drawers
5. Get other clothes that will complete the outfit, like a collared shirt and socks

Similarly, when you create an HTML file, you need to find a way to connect your CSS file to add the stylings.

1. Start at HTML file
2. Leave the folder (if necessary)
3. Access the folder that contains CSS files
4. Reference the specific HTML file you will be using

Here’s one important note. When you want to connect an HTML file to a CSS file, you start your navigation of the file directory at the HTML file itself. Just like picking out an outfit, you navigate from one piece of clothing to another. You **don’t** start at the root directory.

Here’s the code to link your workoutfit.html file to your white shirt file.

```
<link rel="stylesheet" type="text/css" href="/drawers/whiteshirt.css">
```

Here are the steps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RDfVmxOgweTNS7C1)

So, it might be wiser to split up that path into three distinct parts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ESCTx-EdCRBBxVs482f0pg.jpeg)

1. **/** — sends us back to the root folder
2. **drawers**– we open up the drawers folder within the root folder
3. **/whiteshirt.css** — this is the actual file we want to connect, within the drawers folder

### How To Access Files in the Same Folder

Most of the time, you will be trying to access files from other folders in your directory. As your project grows, this will be especially important for keeping track of all the different files in use.

But sometimes, you will access files from the same subdirectory. This is common when your project is at an early stage — one HTML File, one CSS file, and one JavaScript file (plus images).

In this case, the path is much simpler. Let’s return to our bedroom example, and imagine that you also must pick out a tie for your outfit. That tie is stored in the closet too.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ws2QYEzv7VD5beK7)

So, we now want to link two separate stylesheets to our HTML file. One in the same folder, one in a separate folder. This is common practice when you have one general stylesheet that is shared among many HTML files.

```
<link rel="stylesheet" type="text/css" href="tie.css"> <link rel="stylesheet" type="text/css" href="/drawers/whiteshirt.css">
```

Notice how _tie.css_ has no prefix whatsoever. The file path is simply the filename and suffix. That means that the file is in the same subdirectory as the HTML file. It’s just like searching through your closet and grabbing two items that are right next to each other.

### One Last Way To Navigate Your Directory

Once your app gets larger, you may need multiple levels of subdirectories to store all the different types of scripts, stylesheets and images. So far, we have covered only one way to navigate this: by going all the way back to the root directory, and accessing files from there.

But, this can create long file paths, and that introduces the opportunity for confusion and bugs when another person looks over your code.

Sometimes, it’s easier to work backwards one subdirectory at a time. This is where the “../” prefix comes into play.

Let’s reorganize our closet to see how multiple tiers of folders can be used. Now, within our closet, there will be a _tierack_ folder to hold the _tie.css_ file, and a _hangars_ folder to hold _workoutfit.html._

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zx0mKUlQqivPDUUY)

We still want to connect our tie.css file to workoutfit.html. But it doesn’t make a lot of sense to return to the root directory and then navigate all the way back down to the _tierack_ folder.

Instead, we can use the ../ prefix to go backwards by one folder, then navigate to tiereack.

![Image](https://cdn-media-1.freecodecamp.org/images/0*I0wmgDIWCB6WPe2Y)

And here is the code.

```
<link rel="stylesheet" type="text/css" href="../tierack/tie.css">
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*O3cj8DVh78w_YMBo)

This makes our code a little more maintainable. For example, what if we changed a part of the directory structure at a higher level? Then all of our file paths would break, and we would be forced to go on a scavenger hunt to find all the broken paths. This makes it more likely that we will be able to maintain our code. You can even string more than one together. “../../” means that you should go **two** levels higher in your directory.

### Using the Chrome Inspector To View Live Sites

Once your site goes live, those files will be hosted using the same structure on a server. That means that if the structure works locally… it should work live as well.

You can use the Chrome Inspector (or the dev tools in the browser of your choice) to verify this. For example, if you head to codeanalogies.com and inspect the logo in the top left, here is what you will see:

![Image](https://cdn-media-1.freecodecamp.org/images/0*LIQgu_fn1Mc93xj0)

This means that I am storing my main site logo in a folder called _img_. It is located one level below the root folder.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GDPpDuOgAEvUAlVq)

Other sites may use a CDN to store static assets. [You can read more about that here](https://blog.codeanalogies.com/2018/06/11/web-caching-explained-by-buying-milk-at-the-supermarket/).

### Get More Visual Tutorials

Did you enjoy this guide? Give it a “clap”, or sign up here to get my latest visual explanations of web development topics:

