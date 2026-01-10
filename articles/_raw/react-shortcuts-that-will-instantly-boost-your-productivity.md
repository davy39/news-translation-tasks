---
title: 5 React Shortcuts That Will Instantly Boost Your Productivity
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-19T14:55:08.000Z'
originalURL: https://freecodecamp.org/news/react-shortcuts-that-will-instantly-boost-your-productivity
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/5-react-shortcuts.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
seo_title: null
seo_desc: 'To become a better React developer, you don''t always have to learn an
  entirely new, challenging skill. You can instantly improve your React code in a
  few minutes by using the powerful features your development tools make available.

  Some of the bigges...'
---

To become a better React developer, you don't always have to learn an entirely new, challenging skill. You can instantly improve your React code in a few minutes by using the powerful features your development tools make available.

**Some of the biggest improvements in your work as React developer take the smallest amount of time to learn.** Make an effort today to apply these tips and I guarantee you'll save many hours of tedious work in your daily coding, plus you'll enjoy coding with React much more.

Here are five shortcuts that you can take advantage of right now to become a more productive React coder.

> These tips largely feature how to get more out of your code editor. The code editor I use is Visual Studio Code, which is very popular among React developers. If you want to use VSCode, you can download it for free at [code.visualstudio.com](https://code.visualstudio.com). Note that these features are available in virtually all code editors.

## 1. Tired of writing closing tags for every JSX element? Use Emmet.

As a React developer, you write a lot of JSX elements, most of which consist of an opening and closing tag.

If you don't have Emmet setup with React, you have to write both of these tags by hand for every element. A far better approach is to use a tool called **Emmet,** which automatically creates the closing tag whenever you create the opening one. 

**To setup Emmet with React in VSCode:**

1. Go to **Code** (at the top of your screen), then **Preferences**, then **Settings** in VSCode
2. In the options on the left, select **Extensions**, then **Emmet**
3. Scroll to the **Include Languages** section, add in the item input, _javascript_ and in the value input, _javascriptreact_ and hit **Add Item**

_And just like that, Emmet has sped up your coding by 100%:_

![Emmet Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/emmet.gif)

## 2. Tired of formatting your code by hand? Use Prettier.

Can you count the number of times your code hasn't been aligned probably so you tried to adjust the spacing yourself? I don't want to even think about how much time I've spent formatting my own code!

_If you're still trying to format your code manually, you need **Prettier**._

Prettier is aptly named: it turns your misaligned code into a much prettier, formatted version.

Prettier is available as a devDependency for individual JavaScript projects or you can use it across all of your projects with the Prettier VSCode extension. The benefit of using the VSCode extension is that you can automatically format your JavaScript code every time you hit save.

**Here's how to setup Prettier to use across all your projects in VSCode:**

1. Go to **Code**, then **Preferences**, then **Extensions**
2. Search for _prettier_ in the search input and hit enter (it should be the first one to come up)
3. Select the extension, then hit **Install** (and possibly **Reload** to apply the extension)
4. Go to **Code**, then **Preferences**, then **Settings**
5. Search for **Format on Save** and select the checkbox next to the format on save option

Now all of the code you write will be formatted perfectly, every time you save:

![Prettier for React Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/prettier.gif)

## 3. Do you write out every single component you make? Use React snippets.

Creating many things in React and in JavaScript projects in general requires a lot of boilerplate. Every time you write a component you have to type out every part of it – import React, create a function, and export it from your file.

_Do you get tired of having to do this?_ We all do. That's why snippets for React exist.

To avoid all the extra work of writing the same code again and again, use **React snippets**. Snippets allow you to use keyboard shortcuts to instantly write every part of your React code instead of having to type it all out manually.

For example, instead of writing `import React from 'react'` you can just write `imr` and hit the Tab key to instantly create the same thing. Snippets are a huge timesaver.

**Here's how to use React Snippets in VSCode:**

1. Go to **Code**, then **Settings**, then **Extensions**
2. Search for _React Snippets_. There are many good snippet extensions to choose from.
3. When you have a snippet extension installed, take a look at the shortcuts available and write the best ones down.
4. When you type a shortcut, wait for the suggestion to appear in your code editor and then hit **Tab** (you can arrow through the list if you want a different one)

You'll be shocked at how quickly you can make your components now:

![React snippets for VSCode Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/react-snippets.gif)

## 4. Do you import all your components manually? Use auto import instead.

One of the most tedious things to do in creating React apps is importing packages and components from other files. 

It's very repetitive and can take a significant amount of energy to import every single thing by hand (plus to correct when you make a typo).

Instead of having to remember, find, and manually import your components and packages, let your code editor do it for you. You can **auto import** whatever you like by selecting what you want to import by pressing the Tab key.

**Here's how to auto import packages and components in VSCode:**

1. Go to **Code**, then **Preferences**, then **Settings**
2. Search _auto import_ and make sure the **Enable Auto Import** checkbox is selected
3. Go back into your project, write the name of what you want to import, arrow through the options the editor suggests, and hit **Tab** to instantly create an import statement for it.

When you use auto import, it makes working with projects of any scale easier, because you no longer spend half of your time writing import statements.

![Auto import for React Demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/auto-import.gif)

## 5. Do you manually remove your unused imports? Use the organize imports shortcut.

Along with having Prettier for all of the code that we write, VSCode gives us a shortcut called **organize imports** that does just that. In fact, it does two things:

1. It alphabetically organizes our import statements
2. It removes unused import statements (instantly fixes linting warnings about unused imports)

And best of all, this shortcut requires no setup. **Here's how to use it:**

1. Go to **View**, then **Command Palette.**
2. Search for _organize imports_ and select it. 
3. Your imports should now be organized and any unused imports removed. 

Note that you can use the keyboard shortcut `command/control + shift + o` as well.

![Organize imports demo](https://reedbarger.nyc3.digitaloceanspaces.com/5-react-shortcuts-that-will-instantly-boost-your-productivity/organize-imports.gif)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

