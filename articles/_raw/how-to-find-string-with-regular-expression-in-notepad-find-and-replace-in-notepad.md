---
title: Find and Replace in Notepad++ – How to Find String with Regular Expression
  in Notepad++
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-05T13:21:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-string-with-regular-expression-in-notepad-find-and-replace-in-notepad
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/findAndReplacewithRe.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: "Notepad++ has a Find feature with which you can search for any text in\
  \ a file. But it doesn’t end there. \nYou can also use Notepad++'s Find and Replace\
  \ feature to search for a text and replace it with a specified replacement.\nThe\
  \ Find and Find and Re..."
---

Notepad++ has a **Find** feature with which you can search for any text in a file. But it doesn’t end there. 

You can also use Notepad++'s **Find and Replace** feature to search for a text and replace it with a specified replacement.

The **Find** and **Find and Replace** features accept regular text, but they both also accept regular expressions.

Let's see how the **Find** and **Find and Replace** feature of Notepad++ works by using regular expressions instead of regular text.


## How to Find a String with Regular Expressions in Notepad++
This is the code I'll use for this demo:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Find String with RegEx in Notepad++</title>
  </head>
  <body>
    <h1>Find String with RegEx in Notepad++</h1>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius beatae
      dignissimos alias quo odit aperiam laborum accusamus ea maxime dolores?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae voluptatem
      perferendis iure laborum inventore ducimus harum saepe voluptatibus neque
      earum?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam
      accusantium placeat dolore illo, quidem suscipit. Recusandae corrupti
      assumenda soluta libero!
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate
      officia rerum id inventore sunt deleniti quaerat quibusdam libero vero
      non?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>
  </body>
</html>
```

Once you've opened your file in Notepad++, press `CTRL + H` to open the **Find** popup. Make sure you're in the **Find** tab because the **Replace** tab is what opens by default. 

After that, select **Regular expression**:

![ss1-3](https://www.freecodecamp.org/news/content/images/2023/05/ss1-3.png) 

Next, enter your regular expression in the search input. I want to search for all Heading elements, so I'll enter the regex `<h(1|2|3|4|5|6)>`

After entering the regex, click the Find Next button. It may also appear as "Find":

![ss2-1](https://www.freecodecamp.org/news/content/images/2023/05/ss2-1.png) 

To keep seeing the matches, you have to keep clicking the "Find Next" button. However, you can click the "Count" button to see all your matches:

![ss3-1](https://www.freecodecamp.org/news/content/images/2023/05/ss3-1.png) 


## How to Find and Replace a String with Regular Expressions in Notepad++
You can perform find and replace almost the same way. The only difference is that you select the "Replace" tab instead of "Find":

![ss4-1](https://www.freecodecamp.org/news/content/images/2023/05/ss4-1.png)

The search regex gets automatically populated, so what you need to do here is specify what to replace the matches with and the click **Replace**. 

Let's say I want to replace all headings with a `p` tag:

![ss5-2](https://www.freecodecamp.org/news/content/images/2023/05/ss5-2.png) 

Instead of clicking "Replace" repeatedly to replace the matches, you can click the "Replace All" button:

![ss6-1](https://www.freecodecamp.org/news/content/images/2023/05/ss6-1.png) 

I'm also going to find all the closing heading tags with this regex ` <\/h(1|2|3|4|5|6)>` and replace them with closing `p` tags.

Now, this is what the code looks like:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Find String with RegEx in Notepad++</title>
  </head>
  <body>
    <p>Find String with RegEx in Notepad++</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius beatae
      dignissimos alias quo odit aperiam laborum accusamus ea maxime dolores?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae voluptatem
      perferendis iure laborum inventore ducimus harum saepe voluptatibus neque
      earum?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam
      accusantium placeat dolore illo, quidem suscipit. Recusandae corrupti
      assumenda soluta libero!
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate
      officia rerum id inventore sunt deleniti quaerat quibusdam libero vero
      non?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>
  </body>
</html>
```


## Conclusion
Find and Replace is a great feature that saves you a ton of time in Notepad++, especially if you have to replace text in a large file.

Since VS Code is the most popular code editor these days, it also has its own find and replaces feature you can access by pressing `CTRL + H`. And if you want to search with regex, you can press the `.*` button:

![ss7-1](https://www.freecodecamp.org/news/content/images/2023/05/ss7-1.png)

Thank you for reading. 


