---
title: HTML File Text Editor – How to Open Web Page Code in Windows Notepad
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-16T15:08:00.000Z'
originalURL: https://freecodecamp.org/news/html-file-text-editor-how-to-open-web-page-code-in-windows-notepad
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/notepad.png
tags:
- name: editor
  slug: editor
- name: HTML
  slug: html
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'Notepad is a built-in text editor that comes pre-installed on Windows machines
  of all versions – XP, Windows 7, Windows 8, Windows 10, and so on.

  It is the default Windows text editor. You can think of Notepad as your VS Code
  or favorite text editor ...'
---

Notepad is a built-in text editor that comes pre-installed on Windows machines of all versions – XP, Windows 7, Windows 8, Windows 10, and so on.

It is the default Windows text editor. You can think of Notepad as your VS Code or favorite text editor with fewer capabilities. 

Coding with Notepad is great for beginners, because you have no access to syntax highlighting, formatting, and other such automated features. 

Without these aides, you'll learn attention to detail, perseverance, resilience, and how to format your code yourself, before you start coding with other text editors like VS Code, Sublime Text, or Atom.

So, in this article, I will walk you through how to use Windows Notepad, and how to open any web page code with it by making a simple website with HTML, a little bit of CSS, and JavaScript.

## How to Code a Simple Website in Notepad

You can use Notepad to code in two ways: launch Notepad directly from your Windows machine and start coding and then save the code later, or create the file and open it with Notepad.

In this tutorial, I will focus on the second method, so I’m going to create the files first, then open them with Notepad.

**Step** 1: Create a folder anywhere on your computer 
**Step 2**: On the main menu section of the folder, click on the "View" tab and make sure "file name extensions" is ticked. This will give you access to creating a file and specifying the extension as well.

![file-extension_LI](https://www.freecodecamp.org/news/content/images/2021/09/file-extension_LI.jpg)

**Step 3**: Inside the folder, create an HTML file called `index.html`, a CSS file called `styles.css`, and a JavaScript file called `app.js`.

![file-creation](https://www.freecodecamp.org/news/content/images/2021/09/file-creation.png)

These names are due to convention. You can name the files whatever you want if you don’t want to follow the conventions.

**Step 4**: Right-click on the `index.html` and hover on the “open with” option. This will show apps with which you can open the file. Choose Notepad.

![file-openinig](https://www.freecodecamp.org/news/content/images/2021/09/file-openinig.jpg)

By default, the index.html file will be opened by your default browser, so make sure you don’t double-click the file.

If Notepad is not shown within the options, click “Choose another app”, select “More apps” in the next popup, and you will see Notepad within the apps listed.

![file-opening-alternative](https://www.freecodecamp.org/news/content/images/2021/09/file-opening-alternative.jpg)

Now, you should have opened the HTML file with Notepad. You will see something like this (if you get things right):

![blank-notepad](https://www.freecodecamp.org/news/content/images/2021/09/blank-notepad.png)

**Step 5**: Paste in the following HTML Code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Notepad Website</title>
  </head>
  <body>
    <h1 class="page-heading"></h1>

    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>

    <p>
      This is a paragraph with some placeholder texts: Lorem ipsum dolor sit
      amet, consectetur adipisicing elit. Beatae, mollitia quo quasi voluptatum
      quam soluta debitis praesentium molestias nam magnam aperiam deserunt eos
      modi odit incidunt ut vitae cum maiores.
    </p>

    <strong>This is a bolded sentence</strong> <br>

    <em>This is an italicised text</em>

    <p>
      This is a link to <a href="https://freecodecamp.org">freeCodeCamp</a>, a
      platform where you can learn to code for free
    </p>

    <p>Below is freeCodeCamp logo:</p>

    <img
      src="https://popsql.com/static/external-logos/freecodecamp.png"
      alt="freecodecamp-logo"
    />
  </body>
</html>
```

Your Notepad app should now be filled with code:
![html-notepad-1](https://www.freecodecamp.org/news/content/images/2021/09/html-notepad-1.png)

Save the file by pressing Ctrl + S, or go to File and click “Save”.

If your code isn't indented like mine, don’t worry. Notepad doesn’t do it for you automatically, so you have to do it manually.

**Step 6**: Now the HTML file is ready. Go back to the folder in which you created the HTML, CSS, and JavaScript files in Step 3. Double-click the HTML file to open it in your default browser.

The website should now look like this:
![html-page-1](https://www.freecodecamp.org/news/content/images/2021/09/html-page-1.png)

Open the CSS file you created in **Step 3** and paste in the following code: 

```css
.page-heading {
  color: #2ecc71;
}
```

If you reload the page, you will see there are no changes. Don’t worry at all. This is because the `h1` tag with the class of `page-heading` in the HTML file is empty.

Now, you can insert some text into that `h1` tag dynamically with JavaScript.

Open the JavaScript file created in **Step 3** and paste in the following code: 

```js
const pageHeadingText = "This is a Simple Website coded with Windows Notepad";
const pageHeading = document.querySelector(".page-heading");

pageHeading.innerHTML = pageHeadingText;
```

What is the JavaScript code above doing?

I declared a variable called `pageHeadingText` and set it to a string, `“This is a Simple Website coded with Windows Notepad”`.

I declared another variable called `pageHeading` to select the empty h1 tag in the HTML. I did this with the DOM (Document Object Model) `querySelector` method.

In the third line of the JavaScript code, I used the DOM’s `innerHTML` method to set the text content of the `h1` to the value of the `pageHeadingText` variable, which I set to `“This is a Simple Website coded with Windows Notepad”`.

Now, go back to the website and reload it. There’s still no difference. Don’t worry once again. This is because you have to link the CSS and JavaScript files. 

To link the CSS file, paste the following code in the head section of the HTML: 

```html
<link rel="stylesheet" href="styles.css" />
```

To link the JavaScript file, paste in the code below right before the closing body tag in the HTML: 

```html
<script src="app.js"></script>
```

The HTML file should now have the CSS and JavaScript files linked like this: 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Notepad Website</title>

    <!-- CSS Link -->
    <link rel="stylesheet" href="styles.css" />

  </head>
  <body>
    <h1 class="page-heading"></h1>

    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>

    <p>
      This is a paragraph with some placeholder texts: Lorem ipsum dolor sit
      amet, consectetur adipisicing elit. Beatae, mollitia quo quasi voluptatum
      quam soluta debitis praesentium molestias nam magnam aperiam deserunt eos
      modi odit incidunt ut vitae cum maiores.
    </p>

    <strong>This is a bolded sentence</strong>

    <em>This is an italicised text</em>

    <p>
      This is a link to <a href="https://freecodecamp.org">freeCodeCamp</a>, a
      platform where you can learn to code for free
    </p>

    <p>Below is freeCodeCamp logo:</p>

    <img
      src="https://popsql.com/static/external-logos/freecodecamp.png"
      alt="freecodecamp-logo"
    />

    <!-- JavaScript Link -->
    <script src="app.js"></script>

  </body>
</html>
```

If you now reload the page, you should see a difference:

![html-page-2](https://www.freecodecamp.org/news/content/images/2021/09/html-page-2.png)

The code in the CSS and JavaScript files is now working.

## Conclusion

The Windows Notepad is a text editor just like S Code, Atom, Sublime Text, and others. It just does not have the features of other more advanced text editors like syntax highlighting, text formatting, built-in terminal, and so on. But it still performs all the functions of a text editor as you can code in any programming language with it.

To get more comfortable coding, you can download and install a more feature-rich text editor like VS Code (it's free!). It gives you syntax highlighting, text formatting, and pretty much any functionality you want through a rich library of extensions available in the VS Code marketplace. 

Apart from VS Code, other text editors you can use are Atom, Sublime Text, Vim, and Notepad++, a hybrid version of Windows Notepad.

Thank you for reading this article. If you find it helpful, share it with your friends and family.



