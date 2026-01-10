---
title: How To Use Prettier in Visual Studio Code
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-03-18T12:35:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-prettier-in-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Prettier.png
tags:
- name: Prettier
  slug: prettier
- name: Visual Studio Code
  slug: visual-studio-code
seo_title: null
seo_desc: "Nowadays, every tech company strives to build quality software fast. That's\
  \ why every developer must learn how to write clean and readable code. \nBut when\
  \ a project is managed by multiple developers, the focus shifts into consistency\
  \ especially in te..."
---

Nowadays, every tech company strives to build quality software fast. That's why every developer must learn how to write clean and readable code. 

But when a project is managed by multiple developers, the focus shifts into consistency especially in terms of written code. 

Keeping a consistent code style and formatting across many team members and project is a challenging task. It's almost impossible to do it manually, but that's where Prettier comes into play.

In this guide, you will learn how to install Prettier in Visual Studio Code and how to use it to format code.

## Prerequisites 

Before you follow this guide, you will need to download and install [Visual Studio Code](https://code.visualstudio.com/).

## What is Prettier?

Prettier is a powerful code formatter that automates this process from start to finish. It gives you confidence that your code adheres to defined coding standards without any manual actions (unless you want to have it manual).   
  
Prettier not only supports all JavaScript libraries and frameworks, such as Angular, React, Vue, and Svelte, but also works with TypeScript.

That's why it is used by many people in tech worldwide.

## How To Install Prettier in Visual Studio Code

To install Prettier in Visual Studio Code, you need to:

1. Open the Extensions tab.
2. Type prettier in the search box.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---1--2-.png)
_Visual Studio Code / Extensions_

At the top of the list you will find the Prettier - Code formatter extension. You need to open it, and click the Install button:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---2.png)
_Visual Studio Code / Extensions / Prettier - Code Formatter_

After the successful installation you will see the text saying "This extension is enabled globally"_:_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---2--1-.png)
_Visual Studio Code / Extensions / Prettier - Code Formatter (Installation completed)_

## How To Activate Prettier in Visual Studio Code

When your Prettier extension is installed, you need to configure Visual Studio Code to take advantage of it. You can do in the Settings tab. 

Side node: to open the Settings tab, you can use `COMMAND + ,` on macOS or `CTRL + ,` on Windows and Linux:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---4.png)
_Visual Studio Code / Main view_

At the top of the Settings tab you will find a search box. Now, you need to type formatter, and then Editor: Default Formatter will pop up on the settings list:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---5.png)
_Visual Studio Code / Settings_

Now, open the dropdown and select Prettier - Code formatter from the list:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---6.png)
_Visual Studio Code / Settings / Default Formatter_

Now, Prettier is your default code formatter, but you might want to enable Visual Studio Code to automatically format code when you save files. 

If you want to, just tick the checkbox in the Format On Save section:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---7.png)
_Visual Studio Code / Settings / Format On Save_

## How To Format Code with Prettier in Visual Studio Code

Let's take a look at one React component I created: 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---8--2-.png)
_Visual Studio Code / Unformatted React 18 Component_

As you can see, this code is completely misaligned, it misses semicolons, and it is very difficult to read. The code could formatted in a better way, right? Here's where Prettier comes into play.  

To format code, we need to open the command palette – you can use `COMMAND + SHIFT + P` on macOS or `CTRL + SHIFT + P` on Windows and Linux. 

Now, you need to find Format Document. Feel free to use the search box:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---9.png)
_Visual Studio Code / Format Document command_

After running Format Document your code becomes neat and clean:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---10.png)
_Visual Studio Code / Formatted React 18 Component (with Prettier)_

## Conclusion

Integrating Prettier into Visual Studio Code is a game-changer for developers striving to maintain a consistent and high-quality codebase. 

By automating the formatting process, you are not only adhering to coding standards but are also reducing the struggle that comes with manual code formatting. That's why every developer should use Prettier to ensure consistency in their codebase. 

I hope this article helped you a lot. It'd mean the world to me if you shared it on your social media.

If you have any questions you can reach me on [Twitter](https://twitter.com/msokola).

## Learn React

Looking for a practical course to learn React? 

🚀 **Join my [React 18 Course on Udemy](https://assets.mateu.sh/r/fcc-prettier-guide)**.

This course includes:

* 🎥 5.5 hours on-demand video
* 📱 Access on mobile and TV
* 🗓️ Full lifetime access
* 🎓 Certificate of completion

Click below to enroll.

[![React 18 on Udemy](https://assets.mateu.sh/assets/fcc-prettier-guide)](https://assets.mateu.sh/r/fcc-prettier-guide)  
_Click to get started_



