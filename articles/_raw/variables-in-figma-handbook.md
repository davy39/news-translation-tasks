---
title: How to Use Variables in Figma – A Handbook for Beginners
subtitle: ''
author: Faith Olohijere
co_authors: []
series: null
date: '2023-12-15T22:11:10.000Z'
originalURL: https://freecodecamp.org/news/variables-in-figma-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/How-to-Use-Variables-in-Figma-cover--1-.png
tags:
- name: Design
  slug: design
- name: figma
  slug: figma
- name: handbook
  slug: handbook
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: "At Figma Config 2023, the Figma team unveiled a lot of new features – including\
  \ variables. The launch of variables in Figma offers designers a new approach that\
  \ helps them make their designs more flexible and adaptable. \nIn this tutorial,\
  \ you'll lear..."
---

At Figma Config 2023, the Figma team unveiled a lot of new features – including variables. The launch of variables in Figma offers designers a new approach that helps them make their designs more flexible and adaptable. 

In this tutorial, you'll learn what variables in Figma are, and how to create and implement different types of variables while designing in Figma.

## Prerequisites:

To get the most out of this handbook, it'll be helpful to have basic knowledge of how to use Figma and its features. But note that this is not necessary, as I wrote this handbook for everyone – irrespective of their individual level of knowledge. 

This handbook is for everyone who is interested in learning more about variables, Figma, and design in general.

## Table of Contents:

- [What are variables?](#heading-what-are-variables)
- [Differences between Variables and Styles in Figma](#heading-differences-between-variables-and-styles-in-figma)
- [Why are Variables Important to the Design Process?](#heading-why-are-variables-important-to-the-design-process)
- [How to Create Variables in Figma](#heading-how-to-create-variables-in-figma)
    - [How to Create Colour Variables in Figma](#heading-how-to-create-colour-variables-in-figma)
        - [How to Create Colour Variables for Tokens](#heading-how-to-create-colour-variables-for-tokens)
        - [How to Implement Colour Variables in Your Designs](#heading-how-to-implement-colour-variables-in-your-designs)
        - [How to Create Different Modes with Variables](#heading-how-to-create-different-modes-with-variables)
    - [How to Create Number Variables in Figma](#heading-how-to-create-number-variables-in-figma)
    - [How to Create String Variables in Figma](#heading-how-to-create-string-variables-in-figma)
    - [How to Create Boolean Variable in Figma](#heading-how-to-create-boolean-variables-in-figma)
- [How to Use Variables for Advanced Prototyping](#heading-how-to-use-variables-for-advanced-prototyping)
   - [Advanced Prototyping with Number Variables](#heading-advanced-prototyping-with-number-variables)
   - [Advanced Prototyping with Boolean Variables](#heading-advanced-prototyping-with-boolean-variables)
- [How to Use Variables for Developers- Using APIs](#heading-how-to-use-variables-for-developers-using-apis) 
- [Conclusion](#heading-conclusion)

# What Are Variables?

The word "variable" has a lot of definitions. The Oxford Dictionary defines the word variable as "not consistent or having a fixed pattern; liable to change." Another definition says "an element, feature, or factor that is liable to vary or change." 

The definitions above simply tell us that variables are elements which are dynamic and prone to change. With these definitions, we can now define what a variable is in Figma. 

In Figma, a variable stores reusable values like colour and text values that you can apply to different kinds of design properties and prototypes.

## Differences between Variables and Styles in Figma

Given the definition of variables above, you might have begun to see some similarities between variables and style guides. Although both features exist to make your work better, there are a few key differences to keep in mind:

* Variables are a more advanced feature, and they allow you to define and reuse values like colours, text, and spacing across your designs. On the other hand, styles are predefined sets of design properties such as text styles, colour styles, and effect styles.
* Variables allow designs to change when used in various contexts, because of their dynamic nature, unlike styles. For example, you can change your designs from light mode to dark mode or have padding values change when designing for different devices. This makes variables useful for creating design systems with adaptable components.
* Variables offer a more flexible design process in creating flexible design components, especially where you want to change values like button text or color on different instances of the same component. Styles are typically used for maintaining consistent design elements like button styles, text headings, or colour palettes.
* Variables can store raw, single values, while styles store sets of values.

## Why are Variables Important to the Design Process?

Using variables is quite important for a number of reasons.

First, variables help maintain **consistency** across a design system. By defining variables for colors, typography, spacing, and other design elements, you ensure that these elements have a uniform appearance throughout your project. This consistency is crucial for branding and user experience.

Variables also make designs **adaptable**. Designers can quickly experiment with different values such as colour schemes or font sizes by adjusting the variables. This adaptability is valuable when creating designs for different platforms or devices.

Variables are also quite **efficient**. When a variable is updated, all instances of that variable in the design updates automatically. This saves time and effort, and eliminates the need to manually update every instance of a specific element.

Variables are particularly useful in large projects or design systems because of their **scalability** and **ease of maintenance**. They allow designers to scale their designs without losing control. 

Since projects grow and design systems evolve over time, variables can be adjusted globally to accommodate new requirements. Variables also provide a central place to update these changes, ensuring that all design elements are consistently modified.

And finally, variables can be beneficial to developers during the **hand-off process**. Designers can provide developers with precise values for design elements, reducing the chances of misinterpretation and streamlining the implementation process. 

# How to Create Variables in Figma

Variables are quite easy to create in Figma. Below, I'll walk you through the steps for creating different kinds of variables in Figma.

At the moment, we have four types of variables in Figma:

* Color: used for colour fills.
* Number: used for dimensions, corner radius, and auto layout properties.
* String: used for text layers and variant properties.
* Boolean: used to toggle layer visibility.

We'll create and implement each of these variables in Figma, and also use them for advanced prototyping.

## How to Create Colour Variables in Figma

The first type of variable we'll be creating is a colour variable. As a designer or developer, you have likely used colours in your projects. So, the concept of colour shouldn't be unfamiliar to you from a design standpoint.

### Step 1: Open a new Figma file

Let's assume that you want to create colour variables for a new design project you're going to start working on, like a magazine website for example. The first thing you need to do is open a new Figma file.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-1.png)
_Blank Figma file_

### Step 2: Choose a colour palette

The next step is to choose a colour palette for the project. Every design project has a set of colours used repeatedly to establish consistency – for example, for headers and backgrounds, to call attention to a primary button, and so on. 

You'll want to choose colours which complement each other for your design. If you need some help here, you can read my article on the [60-30-10 rule in design](https://www.freecodecamp.org/news/the-60-30-10-rule-in-design/). 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-3.png)
_Creating a colour palette_

### Step 3: Create variables for each colour

Next, we'll create variables for each colour code in the palette. Go to the panel on the right-hand side and click on _local variables_.

Local variables means all the variables located in the design file.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-4.png)
_Click on local variables_

Click on _create variable_ to create the first variable in the file. 

A dropdown will appear containing the four types of variables I explained earlier. Since we're trying to create colour variables in this section, we'll choose _color_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-5.png)
_Create a colour variable_

A created variable section will come up, with two columns: the title of the variable (_Color_), and the value of the variable (the colour code-FFFFFF).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-6.png)
_Choose colour variables_

Give your new variable a name – you can use the role of the colour, primary background for instance. In the next column, type the colour code or use a colour picker. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-7.png)
_Rename variable &amp; type in colour code_

And there you go – you just created your first colour variable!

To see more editing options, hover over the variable's row. An _edit variable_ icon will pop up.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-141.png)
_Edit variable_

Click on it to edit the colour variable to your taste.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-8.png)
_Edit the colour variable/add a description_

In the editing section, you can add a description on how to use the variable, hide from publishing, and so on.

Having done that, follow the steps above to create variables for the remaining colours in the colour palette.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-10.png)
_Create variables for other colours_

You can also organise your variables into groups. To do this, select the colour variables you want to group (hold down SHIFT key), and right-click.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-11.png)
_Group the colour variables_

This will bring out some options:

* New group with selection
* Edit variables
* Duplicate variables
* Delete variables

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-12.png)
_New group with selection_

Choose _New group with selection_, double-click on the group name, and rename it to _color/blue_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-14-1.png)
_Rename group_

You can group your colour variables anyway you'd like to – for example, background colours, header colours, different shades of a particular colour, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-15.png)
_Colour blue variables grouped._

Violà! You just created a colour variable group in Figma. Click on the collection drop-down and choose _rename collection_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-16.png)
_Rename collection_

You can rename this collection _primitives_. 

_Primitives_ means basic. Also, you can decide to rename your collections or not. The choice rests on you.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-39.png)
_Renamed primitives collection_

### How to Create Colour Variables for Tokens

Now, we'll create colour variables for the text, surfaces (such as backgrounds), and borders we need for the project. We want to assign different functions to the colour palette (variables) we created earlier.

Click on local variables and create a new collection. You can name this _tokens_. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-21.png)
_New collection_

Create a new colour variable and rename it "primary text". 

In order to save yourself time, and group your variables as you're naming them, rename the variable as _text/primary_. This will automatically form a group.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-24.png)
_Creating and grouping text variables_

Click on the fill box and go to _Libraries_ to see all colour variables created.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-26.png)
_Assigning colour from libraries_

We'll choose _Main Black_ which is under _color/greys_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-27.png)
_Choosing colour black_

We can go ahead and assign other colour variables for different text functions, as much as we want to. Remember to add _text/_ before the actual name of the variable, so it'll form a group automatically.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-28.png)
_Assigning colour variables for text_

Next, we'll create colour variables for surfaces such as backgrounds, and for borders as well.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-29.png)
_Colour variables for surfaces and borders_

Some of the colour variables might bear the same colour code, but they have different functions, so that's totally fine. For example, the colour code for button text is the same as the colour code for main background. 

### How to Implement Colour Variables in Your Designs

Next, we're going to implement these colour variables in our design. 

In the image below, there are four mobile wireframes with no colour and images (I created these previously). 

You can read about how to create wireframes in this article: [What is Wireframing? How to move from Paper Sketches to High Fidelity Wireframes](https://www.freecodecamp.org/news/what-is-wireframing/).

We'll use the colour variables we've created to add colour to the buttons and text, making sure all elements are consistent.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-30.png)
_Low-fidelity wireframes_

Starting with the first screen, let's add colour to the button. Click on the button, and go to to _Fill_ on the right-hand side of your screen. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-32-1.png)
_Click on button_

In the _Fill_ section, click on _style_ (the four dot icon by the side). Selecting _style_ will bring up a list of colours in your libraries. Select the colour you've assigned for the primary button in order to implement it.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-33-1.png)
_Select a fill colour from the colour variables in libraries_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-34-1.png)
_Implemented button colour_

Next, give the button text a white colour following the same steps.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-35-3.png)
_Implementing colour variable for button text_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-36-1.png)
_Implemented button text colour_

You can go ahead and do the same for the other screens, following the steps above. Don't forget to update the text and colours as well. 

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-37-1.png)
_Updating colour variables for other screens_

You can also add some images or illustrations to complete the look.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-38-1.png)
_Adding illustrations to updated design_

Note: You can get your illustrations from plugins in Figma like Storyset by Freepik, Artify Illustrations, and so on, as well as from illustration libraries like [Freepik](https://www.freepik.com/), [Lapa Ninja](https://www.lapa.ninja/blog/free-illustrations-library-for-your-project/), and others.

### How to Create Different Modes with Variables

Next, we'll create different modes for our design. For instance, if you're working on a project that requires light and dark modes, instead of changing all the design elements manually to accommodate the modes, you can simply use variables to implement that.

To start with, click on _Local variables_ to create a new variable. A list of all variables in the file and their groups will come up:

color/blue:

* Primary Button
* Main Blue

color/greys:

* Main Black
* Main Background

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-142.png)
_Opening "Local variables"_

Next, I'll create a new collection so I can just focus on the modes I am about to create. To create a new collection, simply click on the menu icon on the variables header.

Note that creating a new collection isn't mandatory. It's just to help take your focus away from other variables you have already created.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-143.png)
_Creating a new collection_

Next, I'll rename the collection to _Modes._ To rename a collection, simply double-click on the title, and input your preferred title.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-144.png)
_Renaming a collection_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-145.png)
_Renamed collection "Modes"_

Next, click on _Create variable_ to create a new variable. I'll choose _Color_ because that's the variable we're working with.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-146.png)
_Creating a variable called Color_

The created colour variable will come up with a default colour code: FFFFFF.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-147.png)
_Created color variable with default colour code: FFFFFF_

Next, I'll rename the variable _Background_ because I'm trying to set the background colours for each mode (light and dark).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-148.png)
_Renamed color variable: Background_

Now, we've been working with only the name and value of the variables we've created, but we can add another column when we want to create modes. To do this, simply click on the plus icon on the header to add a new variable mode.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-149.png)
_Clicking on the plus icon_

The new mode will come with three columns: 

* Column 1 (the title of the variable – Background)
* Mode 1 (the first value of the variable – colour code FFFFFF)
* Mode 2 (the first value of the variable – colour code FFFFFF)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-150.png)
_Created new mode_

Next, I'll rename the modes to light and dark. To do this, simply double-click on the title and edit the name.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-151.png)
_Renamed modes: Light &amp; Dark_

Now, we'll assign a value to the background for dark mode. To do this, simply input the colour code/value you prefer for the background. I'll use #0C3272 as my background colour for dark mode.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-152.png)
_Changed value for dark mode background_

Next, we'll create other colour variables for other elements like, text, button colour, button text colour, and so on for the two modes. I''ll list out the specifications to make it easier:

**Light/Dark:**

* Body text: 1A1A1A/FFFFFF
* Button: 0C3272/FFFFFF
* Button text: FFFFFF/0C3272
* iPhone header: 1A1A1A/FFFFFF

Next, we'll go ahead to create the variables. Just follow the steps we followed earlier to create the variables and assign values for each of the modes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-154.png)
_Created variables for other elements_

Next, we make sure the design is connected to the variables we created. To do this, simply hold the element and use _Fill_ to tie it to the colour variable. 

For the Button text for instance, select the text, and click on the style icon in _Fill_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-155.png)
_Clicking on style icon in the "FFill" section_

Next, scroll down the list that comes up, to the specific variable you want to tie the variable to (in this case Body text).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-156.png)
_Selecting Body text variable._

Do the same for the other elements in the design, including the background.

Note that I'll be leaving the illustrations the way they are.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-157.png)
_Screens connected to the variable modes._

To check if the modes actually work, click on the _change variable mode_ icon on the _Layer_ section on the right-hand panel of your screen. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-158.png)
_Clicking on the "change variable mode" icon_

A list of all modes (Light & Dark) will come up and you can switch the screen to whatever mode you choose.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-159.png)
_Switching modes_

A section named _Modes_ will appear on the _Layer_ section, indicating that one of the screens is in dark mode.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-160.png)
_One dark mode &amp; one light mode screen._

## How to Create Number Variables in Figma

Next, I'll show you how to create number variables in Figma. 

Number variables are defined by number values, and they can be applied to corner radius, width or height padding, and so on. Here are the steps to follow to create your own:

### Step 1: Choose a variable

Just like we did when creating color variables, click on the local variables panel to select the kind of variable you're trying to create. Here, you'll select _number._ 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/variable-40.png)
_Choosing variable to create_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Variable-41.png)
_Selecting "number"_

When you select _number_, it appears on the list of variables with a value, in this case 0. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-43.png)
_Number variable showing Number with a default value of 0_

Now, you can rename the number variable to whatever you decide. To rename the variable, double click on _number_, and change it to whatever name you want.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-44.png)
_Renaming number variable_

I'll rename mine to _OrderCount,_ because I'm trying to implement a function that allows a user to increase the number of portions of food they're trying to order.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-45.png)
_Renamed number variable_

Next, we'll set the default number value to _1_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-46.png)
_Setting default number value_

Now we'll tie the number on the design to the number variable (_OrderCount)._ To do this, click on the number in the design.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-47.png)
_Implementing the number variable_

Then go to _Text_ on the left hand side of your screen. Click on the _Apply variable_ icon to apply the variable.

Note: The _apply variable_ icon will only appear on the _Text_ section when a variable has been created.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-49.png)
_Clicking on the "appy variable" icon_

Clicking on the icon will bring up a list of all number variables available in the file. Next, you'll select the variable you're trying to implement. I'll choose _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-50.png)
_Selecting a number variable_

When the variable has been implemented (tied to the number), it'll appear on the text section, indicating that a number variable has been implemented.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-51.png)
_Implemented number variable_

Now, we'll also need two more number variables for the other number values in the design (cost of food and total cost). This is so that these values will also change when a user increases the number of portions they're ordering. 

We won't include delivery fee, because it remains the same way irrespective of the number of portions a user orders.

Next, we'll follow the same process as we did above to create number variables for these.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-52.png)
_Creating other number variables_

Next, we'll tie the numbers in the design to their respective number variables, just as we also did earlier. 

Note: In the main design, I gave the actual number (25) a different frame from the dollar sign (which is in text). This is because when creating the number variable, the dollar sign will not be attached, because it's a word, not a number. 

Consequently, when I tie the number variable to the design, I'll be applying it to the frame containing the number alone.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-53.png)
_Give the number a different frame from the dollar sign_

So, when I tied the first number to the number variable I created (Cost-Portion), something interesting happened. The number in the design took on the value of the variable. Instead of 25.00 which was in the screen earlier, it changed to just 25 because that's what the number variable was set to. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-55.png)
_Number variable changing the number in the design_

Now, to avoid any unpleasantness, I'll change the values of the other numbers, and realign them.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-56.png)
_Changed and realigned number values in the design_

We've just created number variables for our design. In the section for advanced prototyping, we'll check to see if these number variables actually work.

## How to Create String Variables in Figma

Next, you'll learn how to create string variables in Figma.  

As I wrote earlier, string variables are used for text layers and variant properties. With string variables, you can change the headings in your design, flip text on different screens, change language modes, and so on.

For this article, we'll use string variables to change the headings on the screens for each mode we created earlier (light and dark). 

As usual, our first step is to click on _Local variables_ and select the type of variable we want to create.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-161.png)
_Going to local variables to create a new variable_

I'll choose _String_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-163.png)
_Choosing "String" out of a list of all variables_

When I do that, the string variable I just created will appear on the list of variables.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-164.png)
_Created String variable_

If you noticed, the string variable has two columns for "string value", because I created the variable in the _Modes_ collection. Following that, let's see if we can change the headings for each mode. 

Note: The string value is the actual text you're trying to change. 

So, for the first screen whose heading is "Transactions Made Easy", I want it to change to "Easy Transactions, Less Stress" for dark mode. For the second screen whose heading is "Pay Bills with Ease", I want it to change to  "Paid Bills, Easier Life" for dark mode.

Since we're changing the headings for two different screens, we'll create another string variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-165-1.png)
_Creating another string variable_

Next, we'll input the different values for the different modes. To do this, just input the different texts for the two screens in both modes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-166-1.png)
_Inputing string value_

Next, we'll tie the headings to the string variables we just created. To do this, click on the particular heading, and go to the _Apply variable_ icon on the _Text_ section.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-167-3.png)
_Applying string variable_

Next, scroll down and choose the string you're applying it to.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-168-1.png)
_Choosing string variable_

Once you're done, a string icon will come up, indicating that a string variable was applied to the text.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-169-1.png)
_Applied string variable_

Do the same for the second string:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-170-1.png)
_Applying string variable to the second screen_

Next, let's test to see if the string variable works. Select the screens which have the applied variable, go to _Layers,_ and change the mode from light to dark.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-171-1.png)
_Selecting screens which have the applied variables_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-172-1.png)
_Selecting dark mode_

Mine works:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-173-1.png)
_Screens changed to dark mode_

## How to Create Boolean Variables in Figma

Next up, we'll learn how to create Boolean variables. 

Generally, boolean variables are variables that can only have two possible values – true or false. In Figma, boolean variables have the same function: they are used for variant properties or components with two values: true or false. 

Remember the toggle in the design above? 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-110.png)
_Toggle in the design used for implementing number variables_

I'll change that to a checkbox and use boolean variables to make it work. 

To do this, I'll copy out the component and paste it on another frame. I'll then add the checkbox (and replace it in the main design screen later).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-111.png)
_Checkbox on a blank frame._

Next, we'll make the selection a variant. To do this, double-click on the _Create component_ icon on your Figma file header.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-113.png)
_Double-clicking on "create component" icon_

A variant will automatically appear:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-114.png)
_Variant of the component_

Next, I'll create different states for the checkboxes: default, hover, and filled.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-116.png)
_Different states for the chechboxes: Default, hover and filled._

Now, we'll create the boolean variable. 

To do this, go to _Local variables_ as usual and select _Boolean_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-118.png)
_Opening local variables_

Click on _Create variable_. 

Next, we'll choose _Boolean_ from the list.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-117.png)
_Choosing "boolean" from the list_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-119.png)
_Created boolean variable_

Next, we'll rename the boolean variable _SaveFood_ since we're trying to create a function for saving a food choice for subsequent orders.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-120.png)
_Renamied boolean variable_

Next, we'll make the variable _True_ by default. To do this, just click on the toggle icon by the side of the variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-121.png)

You've created a boolean variable!

We'll create an interaction for this boolean variable in the advanced prototyping section and check if it works. 

## How to Use Variables for Advanced Prototyping

In this section, we'll learn how to use variables for advanced prototyping in Figma, using the colour, number, string, and boolean variables we implemented earlier in the design.

N.B: You can only use advanced prototyping features on Figma if your file is on a paid team file. If you don't have a paid team version, you can apply for the _[Figma for Education](https://www.figma.com/education/)_ plan. It's a way Figma helps learners and educators by giving them access to resources, and all benefits of a paid version, for free.

You can use advanced prototyping when you have a lot of screens to work on, and to simply make prototyping easier.

### Advanced Prototyping with Number Variables

Starting with the number variables we created above, let's try to check if it actually works. But before we do that, we'll have to actually prototype the design. 

Note that you can prototype number variables for designs where your user can increase or decrease the number of an item on the screen. Prototyping helps to show the functionality and how that particular feature would work. 

To start with, I'll make the frame where the order count is a component. To do this, select the frame, and click on the component icon on your Figma file header.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-57.png)
_Selecting the order count frame_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-58.png)
_Clicking on the component icon_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-59.png)
_The order count component_

Click on the component icon again to make it a variant.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-60.png)
_Making the order count component a variant_

I'll make a frame outside the screen and drag the variant there, so I'll be able to work on the interactions well.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-61.png)
_Making a frame outside the screen_

Remember that we want to implement a function where the number of portions increases when the user clicks on the plus icon. 

We'll start prototyping from here. 

Now, click on the plus icon in the default variant and move to the prototype tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-62.png)
_Clicking on the plus icon in the default variant_

Next, click on the plus icon in the interactions area to add an interaction.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-63.png)
_Adding an interaction_

A tab will come up showing interactions. In this case, it's set to default _On click_, and no interaction has been added yet (None).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-64.png)
_Adding an interaction_

Now, click on the dropdown icon that says _None._

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-65.png)
_Clicking on the dropdown icon_

It'll bring up a list:

* Navigate to
* Change to
* Back
* Set variable
* Conditional
* Scroll to
* Open link
* Open overlay
* Swap overlay
* Close overlay

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-66.png)
_List following the dropdown_

Choose _Set variable_. 

A list of all variables in the file will come up, and you can then select the particular variable you want to implement. I'll click on _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-67.png)
_Choosing "set variable"_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-68.png)
_Clicking on Order Count (the first time)_

Next, I'll click on _OrderCount_ again to write a mathematical expression, and all the available mathematical expressions will appear:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-69.png)
_Clicking on Order Count (the second time) and showing all mathematical expressions_

I'll select _Addition_, because that's what we're trying to do.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-70.png)
_Choosing the "addition" expression_

You'll notice that an addition icon popped up to signify that the addition expression was given. 

Next, I'll input _1_ by the side of the addition icon to show that it's plus 1.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-71.png)
_Adding number 1 to the expression_

Done! 

Now, we'll follow the same steps to do the same for the minus icon, making the expression subtraction instead of addition.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-72.png)
_Added interactions for the minus icon_

Done!

Note: We don't really need the variant we created earlier. You might only use the variant in cases where you want to create a hover state. I just wanted to show you how easy it would be to create a variant while doing this. 

Next, we'll just copy the prototyped component and put it back in the main design.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-73.png)
_Frame containing the prototyped variable_

To put the prototyped component in the main design, click on _Assets_ at the top of the left hand panel.

This section will show all the assets in the page you're currently on.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-74.png)
_Showing all assets on the page_

Next, I'll drag the frame to the design. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-75.png)
_Dragged asset to main design_

Note: If you don't want to follow the process above to place the prototyped component in the design, simply copy the component (CTRL + C), and _paste to replace_ the frame on the main design.

Now, let's check our prototype out. To do this, you don't need to open the prototype on another tab. You can simply click on the asset and press SHIFT + space bar.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-76.png)
_Clicked asset_

Another frame will appear on your screen. It's interactive and you can test your prototype on it.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-77.png)
_Interactive frame on your Figma screen._

Try clicking on the minus and plus icons on the frame to see if it carries out its function. 

After checking the prototype, I'd like to implement some logic. 

We don't want a scenario where the clicking on the minus icon continues till after 0 and now gives us a negative sign like -1 as you can see in the image below.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-78.png)
_Minus icon giving us negative values_

That wouldn't make sense, so we'll add a _conditional_. 

A conditional is simply a condition that sets rules about how the interaction should work.

To do this, I'll move to the frame containing the component I made earlier. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-79.png)
_Frame containing prototyped component_

I'll be adding the conditional to the minus icon since that's the area that would give us negative values. So, I want the values to stop at 1 since that's the least a user can order (they can't order half or 0, for example). 

So, we'll just zoom into the component to add our conditional. Make sure you're on the prototype tab as well.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-80.png)
_Moving to prototype tab and zooming in on the prototyped component_

I'll click on the variable icon by the minus frame.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-81.png)
_Selecting the variable icon close to the minus icon frame_

This will bring up the already set interactions:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-82.png)
_Already made interactions on the minus frame_

Next, I'll click on the plus icon by the 'x' on the interactions header.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-83.png)
_Clicking on the plus icon in the interaction header_

I'll choose _conditional_ from the list of options which will appear:

* Navigate to
* Change to
* Back
* Set variable
* Conditional
* Scroll to
* Open link
* Open overlay
* Swap overlay
* Close overlay

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-84.png)
_Choosing conditional from the list of options_

We'll then write the condition. To do this, click on _Write condition_ by the _if else_ statement_._ 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-86.png)
_Writing a condition for the interaction_

When we click on _Write condition_, a list of all number variables will come up. I'll choose _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-87.png)
_Selecting ordercount_

This will bring up a list of all available conditions:

* Equal to
* Not equal to
* Greater than
* Greater than or equal to
* Less than
* Less than or equal to

I'll choose _Not equal to_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-88.png)
_Choosing "Not equal to" condition_

Next, the icon for the condition I chose will appear on the input field for writing the condition.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-89.png)
_Condition appearing on the input field_

Next, I'll input 0, which means the interaction is not equal to 0.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-90.png)
_Inputing 0 (zero)_

Next, I'll close the frame and try moving the _Set variable_ section under the _conditional section_ in the interaction. To close the Set variable section, click on the little dropdown icon.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-91.png)
_Clicking on the dropdown icon to close set variable_

When you click on the little dropdown icon, the _Set variable_ section will be minimized, allowing you move the section under the _Conditional_ section.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-92.png)
_Closed set variable section_

Next, I'll drag the _set variable_ section under the _conditional_ section. To do this, just hover on the _set variable_ section and use your trackpad or mouse to drag it.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-93.png)
_Dragging set variable under conditional_

We just added a conditional to our interaction! The icon for the minus frame will change to a condition icon, showing that a conditional has been added.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-94.png)
_Added a conditional to minus interaction_

Now, you can test this new interaction to see how it works. 

Mine certainly does! It doesn't go lower than 0 anymore.

### How to implement cost per portion variable

Now, we want the other number values (cost per portion and total cost) to increase in response to the number of portions a user orders.

We'll start with the Plus icon frame:

Going back to the component we've been working on...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-95.png)
_Frame with prototyped component_

I'll click on the plus frame and go ahead to _set variable_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-96.png)
_Opening the interactions for plus frame_

I'll click on the plus icon on the interactions header.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-97.png)
_Clicking on the plus icon on the interactions header_

Next, I'll select _set variable_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-98.png)
_Selecting set variable_

A list of all variables that have been created in the file will come up:

* The color variables for text, buttons, headings, and so on.
* Number variables – _OrderCount_, _Cost-Portion_, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-99.png)
_A list of all variables in the file_

I'll scroll down to choose _cost-portion,_ which is the cost per food portion a user orders.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-100.png)
_Choosing "Cost-portion" (the first time)_

An input field to write an expression for the variable will come up.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-101.png)
_Write expression input filed_

To write an expression, click on Cost-Portion again and select _Addition_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-102.png)
_Choosing cost-portion (the second time) and selecting addition_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-104.png)
_Addition icon coming up on input field_

Next, I'll input 25, meaning that +25 should be added for every portion of food a user orders.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-103.png)
_Inputing 25_

Having added the interaction for the plus frame, we'll follow the same process for the minus frame. When you're done, the _Set variable_ section should be under the _Conditional_ section.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-105.png)
_Adding interaction for the minus frame_

Remember there's a conditional for the minus frame, so I'll just drag the new interaction inside the conditional.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-106.png)
_Dragging the new "set variable" interaction inside the conditiona;_

Now, try testing the new interaction you just added. Mine certainly works!

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-107.png)
_Testing the new interaction_

Next, we still have one last variable to add (Total Cost). 

Follow the steps above to recreate this interaction. Starting with the plus frame, implement the variable to make sure $25 adds when the order increases. It should show a placeholder – _Total Cost + 25_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-108.png)
_Implementing Total Cost variable_

Now, do the same for the minus frame and test the interaction. Don't forget to add the new interaction inside the conditional.

Mine works!

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-109.png)
_Testing the interactions_

You just learnt how to implement number variables with advanced prototyping in Figma. Congrats!

### Advanced Prototyping with Boolean Variables

Next, we'll create an interaction for the boolean variable we created earlier in the article. 

Note that you can prototype your boolean variables in designs where you have features like checkboxes and toggles. The prototype would show how the checkbox is supposed to function.

To create the interaction, move to the prototype tab and focus on the frame containing the boolean components.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-122.png)
_Frame containing boolean components_

Now, our main interaction will start from the hover state because that's when a user tries to click on the checkbox. But we still need to add an action that will take the user from the default state to the hover state. 

To do this, I'll just click on the first variant and drag it to the second variant.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-132.png)
_Connecting first variant to the second variant_

I'll change _On-click_ to _While Hovering_. To do this, just click on the _On-click_ dropdown and select from the list that pops up:

* On click
* On drag
* While hovering
* While pressing
* Key/Gamepad
* Mouse enter
* Mouse leave
* Mouse down
* Mouse up
* After delay

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-133.png)
_Clicking on the on-click dropdown_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-134.png)
_Selecting "while hovering" from the list_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-135.png)
_Selected "while hovering"_

I also want to change _Instant_ to _Smart Animate_, so I'll click on the dropdown icon by _Instant_, and select from the list that appears:

* Instant
* Dissolve
* Smart animate

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-136.png)
_Changing "Instant" to "Smart Animate"_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-137.png)
_How the interaction looks_

So, we're done with the first interaction and we'll get started on connecting the second variant to the third variant (Hover - Filled).

Just as we did earlier, we'll just drag the second variant to the third variant.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-124.png)
_Connecting the second to the third variant_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-125-1.png)
_How the interaction looks_

Like I said earlier, the main interaction starts from the second variant so we'll not be following the same steps we took to add the first interaction.

To continue, I'll click on the plus icon on the interaction header to add an action, and select _Set variable_ from the list that pops up:

* Navigate to
* Change to
* Back
* Set variable
* Conditional
* Scroll to
* Open link
* Open overlay
* Swap overlay
* Close overlay

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-126.png)
_Clicking on the plus icon on the interaction_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-127.png)
_Choosing "set variable" from the list_

Next, I'll click on _Pick target variable_ to select the boolean variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-128.png)
_Clicking on "pick target variable"_

I'll scroll down the list of variables to choose the variable I want: SaveFood.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-129.png)
_Selecting "SaveFood" variable_

Now, to write the expression for this variable, we're going to say the value will be equal to true. So, I'll select _True_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-130.png)
_Writing the expression and selecting "true"_

Having selected _True_, the expression (_true_) will go under the _SaveFood_ variable, indicating that an expression was applied.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-131.png)
_How the interaction looks_

Next, we'll just copy the original component and paste it in our design so it can sync when we're checking the prototype.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-138.png)
_Pasting the default component in the main design_

To check the prototype directly on your Figma page, click on Shift + space bar.

Mine works!

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-139.png)

But I noticed something; I can't un-check the checkbox. No interaction was provided for that. Now, we'll quickly add that interaction so our component works perfectly. 

To do this, we'll go back to our components, making sure we're in prototype mode, and drag the connection from filled all the way back to default.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-140.png)
_Dragging the connection from filled state to default state_

Now, it's works perfectly!

## How to Use Variables for Developers – Using APIs

Variables are very helpful for teams consisting of developers and/or designers. 

> Variables are now supported in Figma’s Plugin API—for building plugins and widgets—and in the REST API. Since variables is currently in open beta, features and functions may change as we respond to feedback. – Figma Docs

There are three documentations which contain support for variables for developers on Figma: 

* For the [REST API](https://www.figma.com/developers/api#variables): 

> This API includes endpoints for querying, creating, updating, and deleting variables. – Figma docs

To be able to use this API, you must be a member of an enterprise.

* For the [plugin API](https://www.figma.com/plugin-docs/working-with-variables/): 

> This API provides support for creating and reading variables, and binding variables to components. – Figma docs

* For the [widget API](https://www.figma.com/widget-docs/working-with-variables/): This API is connected to the plugin API. It is available to widgets by using the Plugin API the widget contains. 

Widgets are interactive elements that can be used to create interactive prototypes. Widgets extend the functionality of design files and FigJam boards and are often part of the larger design system, which is a collection of reusable components.

## Conclusion

Variables exist in Figma to make your designs better. They are easy to use and create, and are helpful in every design project. In order to save yourself time, make sure to incorporate variables into your design process. 

The key is to practice and explore, and you'll get better as you go. 

Thank you for reading this article, I hope you enjoyed it! 

