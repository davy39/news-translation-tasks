---
title: How to Set Up VSCode for Your React Projects
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-17T16:54:36.000Z'
originalURL: https://freecodecamp.org/news/vscode-react-setup
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/setup-vscode-for-react-projects.png
tags:
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'The ultimate tool you have when you''re developing your projects is your
  code editor. Which is why it''s so important to set it up properly.

  In this step-by-step guide, we will go from a completely new VSCode installation
  to a code editor perfectly pre...'
---

The ultimate tool you have when you're developing your projects is your code editor. Which is why it's so important to set it up properly.

In this step-by-step guide, we will go from a completely new VSCode installation to a code editor perfectly prepared for your next React project.

Let's get started!

## How to Install VSCode

The first step to setting up Visual Studio Code (VSCode for short) is to install it for your computer.

Head to [code.visualstudio.com](https://code.visualstudio.com) and download the right version for your computer (it's 100% free).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.08.06-AM.png)
_Install the right version for your operating system_

Once your installation is done and you open the VSCode app, you should be greeted with a home screen that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.19.32-AM.png)
_VSCode Home Screen (After Install)_

## Choose a color theme you like

Although the default theme that ships with VSCode is very nice and legible, I prefer to use a third-party theme that I find easier on my eyes.

It might seem like a trivial thing to spend time picking a theme. But since you will be spending hours reading text on your editor, you want to choose colors that you like and that do not strain your eyes.

I personally use and highly recommend the Material Theme for all of my installations of VSCode.

To install the Material Theme, go to (at the top of the screen):

**View** > **Extensions** (or use the shortcut ⇧ + ⌘ (Ctrl) + X)

Then search for "Material Theme" in the sidebar and install the first result that comes up. 

It should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.36.24-AM.png)
_Material Theme Installation_

Once it has been installed it will give you a dropdown to choose between a bunch of different variants.

The default option is great, but I personally find the "Material Theme Ocean High Contrast" variant to be the best looking.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.37.38-AM.png)
_Material Theme for VSCode_

## Make your text easy to read

Now is a good time to add some basic settings that make the code that you write comfortable to read.

Settings that will improve the readability of your code are your font size, tab size, and font family.

You can change your VSCode preferences by going to (at the top of your screen):

**Code** > **Preferences** > **Settings** (or use the shortcut: ⌘ (Ctrl) + ,)

The settings I have found to most comfortable over the years for both desktop and laptop development are font size of 18 and a tab size set to 2.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.27.06-AM.png)
_Text Settings for VSCode_

Additionally, to get your text looking just right, I find text looks better when you increase the default zoom level of the editor.

To increase the zoom level, go to preferences (⌘ (Ctrl) + ,) and type in "**zoom level**".

I recommend changing the zoom level from 0 to 1.

And finally, as a matter of preference, I like to remove the default breadcrumb links that are at the top of the editor.

You can remove breadcrumbs by going to:

**View** > **Show Breadcrumbs** (and making sure it is unchecked).

Here is what our code editor looks like with a sample component file I added to my Desktop:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.49.42-AM.png)
_React component appearance in VSCode_

## Format your code with the Prettier extension

You might have noticed in the example above that the code isn't very nicely formatted.

Fortunately, you can automatically format every .js file you write using the Prettier extension for VSCode.

To be able to instantly format our code every time we save a .js file, we can again go to the extensions tab (⇧ + ⌘ (Ctrl) + X), type in "**prettier**" and install it:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.51.35-AM.png)
_Prettier extension for VSCode_

Next, we can go back to preferences (⌘ (Ctrl) + ,) and search for "**format on save**" and make sure it is checked:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.53.36-AM.png)
_Format on Save setting_

And again in preferences, search for the "**default formatter**" setting and set it to Prettier.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.55.30-AM.png)
_Default formatter setting_

Now if we go back to an unformatted file and hit save, it will instantly be formatted for us!

Here is what our dummy component now looks like after we hit save:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-10.57.23-AM.png)
_Formatted React component (with Prettier)_

Check out the Prettier extension documentation to see how you can further configure it according to your formatting preferences. Still, I personally recommend using the default options

## How to Quickly type JSX with Emmet

VSCode comes with built-in support for an amazing tool called Emmet that allows you to write HTML tags very quickly.

However, Emmet is not configured by default to be used with JSX, which React uses instead of HTML.

To write your JSX more quickly, you can use Emmet with React by going to:

**Code** > **Preferences** > **Settings** (⌘ (Ctrl) + ,)

And then typing in the search bar, "**emmet include languages**".

After that, click the "Add Item" button and add the following setting:

item: **javascript**, value: **javascriptreact** (and then hit ok)

Your added setting should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-17-at-11.10.32-AM.png)
_Emmet Include Languages setting_

Now that we have included React as a language for Emmet, we can start writing our JSX much more quickly.

Here is quick demo of how productive you can be with Emmet:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/emmet-react.gif)
_Quick demo of Emmet shortcuts_

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

