---
title: How to Create an Interactive Button Component in Figma
subtitle: ''
author: Faith Olohijere
co_authors: []
series: null
date: '2024-03-06T18:44:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-interactive-button-component-in-figma
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pexels-jess-bailey-designs-810079.jpg
tags:
- name: figma
  slug: figma
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'Designers are always searching for tools that help ease their workflow
  and create innovative solutions for their users. This ranges from components, style
  guides, and design systems, to plugins and extensions.

  In this article, we''re going to look at ...'
---

Designers are always searching for tools that help ease their workflow and create innovative solutions for their users. This ranges from components, style guides, and design systems, to plugins and extensions.

In this article, we're going to look at components as features which can help boost your efficiency as a designer. I'll show you how to create an interactive button component using Figma.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [What are Components?](#heading-what-are-components)  
– [Button components](#heading-button-components)
3. [How to Create an Interactive Button Component in Figma](#heading-how-to-create-an-interactive-button-component-in-figma)  
– [Build the button component](#heading-build-the-button-component)  
– [How to create variants](#heading-how-to-create-variants)  
– [How to create hover and active states](#heading-how-to-create-hover-and-active-states)  
– [How to create other button states](#heading-how-to-create-other-button-states)  
– [How to group buttons by states](#heading-how-to-group-buttons-by-states)  
– [How to make the button components interactive](#heading-how-to-make-the-button-components-interactive)
4. [Conclusion](#heading-conclusion)

## Prerequisites:

To get the most out of this article, it'll be helpful to have basic knowledge of how to use Figma and its features. But note that this is not necessary, as I wrote this article for everyone – irrespective of their individual level of knowledge.

This article is for everyone who is interested in learning more about components, reusable elements, Figma, and design in general.

## What are Components?

Components are reusable design elements that you can use multiple times within a project or across different projects. 

> Components are interactive building blocks for creating a user interface. They can be organized into categories based on their purpose: Action, containment, communication, navigation, selection, and text input. – Material Design 3

Components can range from simple elements like buttons or icons to more complex structures like navigation bars or entire UI modules. They help maintain consistency and uniformity in a design, they are scalable, and they're very helpful for collaboration.

### Button Components 

Buttons, sometimes called CTAs, are elements which allow a user to carry out a specific action like signing up, buying a product, subscribing to a newsletter, and so on. They come in different formats and sizes, and are very important elements in design.

Button components typically consist of visual attributes such as shape, size, color, and typography to convey their functionality and encourage user interaction. They can vary in style and appearance based on the design system, brand guidelines, or the context of their usage within an application or website. 

## How to Create an Interactive Button Component in Figma

Next, we're going to create an interactive button component in Figma. This button component will contain text only buttons, buttons with icons on either the left or right side of the text, and buttons with icons only. 

The button component will contain different button states (default, hover, and active), and will be interactive.

This is very helpful for when you're designing interfaces with different use cases. For instance, you could want a button in your design to carry text and an accompanying icon, for a particular screen. In another screen, you might want to use an icon only button. If you have already created these different components, you'll save a lot of time.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-30.png)
_Different button types (Icon only, Icon &amp; text, text only). Image from [Telerik](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fwww.telerik.com%2Fdesign-system%2Fdocs%2Fcomponents%2Fbutton%2F&amp;psig=AOvVaw2RdR4WQVKTp_y542hJlwaB&amp;ust=1709772173745000&amp;source=images&amp;cd=vfe&amp;opi=89978449&amp;ved=0CBYQ3YkBahcKEwjQnoXps96EAxUAAAAAHQAAAAAQBA)_

Let's get started!

### Build the Button Component

Open a new Figma file. If you don't have a Figma account, go ahead and create one at [figma.com](https://www.freecodecamp.org/news/p/3c725afb-cd49-490c-b122-0115d9b1780a/figma.com).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-1.png)
_Opening a new Figma file_

Next, click on the Text icon on the left hand panel, and type _Button_.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-2.png)
_Typing "button" in the search bar._

Next, add auto-layout (Shift + A). 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-3.png)
_Adding auto-layout_

Make the horizontal button padding to be 36px and the vertical padding 12px. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-4.png)
_Adding horizontal and vertical padding_

Also, give the button a border radius of 8px.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-5.png)
_Adding a border radius._

Add a fill to the button.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-6.png)
_Moving to the "fill" section._

I'll choose the color code #1C199, which is a shade of blue.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-7.png)
_Choosing a color code._

Next, I'll make the text a little bit bolder. To do that, click on the text, and move to the font section on your right panel.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-8.png)
_Moving to the font section._

I'll give the button a font size of 16px, and make the weight "medium".

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-10.png)
_Changing the font size to 16 px_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-11.png)
_Changing the font weight to medium._

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-9.png)
_Showing the edited text_

Next, I'll add any icon of my choice to the button frame. This will enable me easily create a button component with icons, and not just text when the time comes.

To add an icon, I'll use a Figma plugin called _Iconify_, which is one of the largest icon collections in Figma. To do this, right-click on your canva and a menu will pop-up. Go to the _Plugins_ tab.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-12.png)
_Opening Plugins_

A list of the recent plugins you have used will pop-up. You'll also see all the _Saved_ plugins you have. The first plugin on my list is Iconify (that's because I use it a lot, lol). Now, I'll just click on Iconify and search for the particular icon I want to use.

If you have never used a plugin before, and so there are no plugins on your list, you can use the resources section to search for your plugin of choice and save it to your list.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-65.png)
_Going to the resources section_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-64.png)
_Searching for plugins_

I want to use the _forward arrow_ icon, so I'll just search for that using the search field on the plugin.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-13.png)
_Searching for the forward arrow icon._

A lot of forward arrow icons from different collections will pop-up so, I'll just choose any particular one that works best for me, in this case, a forward arrow icon from _IonIcons_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-14.png)
_Selecting a particular forward arrow icon_

I'll select the icon and click on the _Import icon_ button so it can appear on my Figma file.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-15.png)
_Importing the icon to your file_

Next, we'll reduce the size of the icon to whatever height and width we want it to be. It's currently on 48 x 48 and I want it to be 24 x 24.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-16.png)
_Icon size currently 48x48_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-17.png)
_Changing icon size to 24x24_

We'll also change the colour of the icon to match the text colour (white). To do this, make sure the icon is selected and then scroll down to _Selection colours_ to input the color code, which in this case is #FFFFFF.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-18.png)
_Changing icon colour to white (#FFFFFF)_

Next, we'll add the icon inside the button frame. To do this, just drag your icon inside the frame.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-19.png)
_Dragging arrow icon into the button frame_

You'll notice that the frame size increases to accommodate the icon added. 

Next, duplicate the icon and move it to the other side of the text. Duplicating the icon will help us easily create button components with icons on either sides of the text later.

To do this, simply use Ctrl + D, and move the duplicated icon to the other side.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-20.png)
_Using Ctrl + D to duplicate an icon_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-21.png)
_Moving the duplicated icon to the other side of the frame._

Next, I'll hide both icons because I want to create my first button component (text only button). I'll rename the frame to Button.

To hide both icons, move to the layers panel on your left, and click on the eye icon by the side of the assets you want to hide.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-22.png)
_Moving to the layers panel to hide the icons_

You'll notice that the frame resizes automatically once both icons are hidden.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-23.png)
_Button frame with hidden icons_

I'll then rename the frame to _Button_. To do that, double click on the heading of the frame, and rename.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-24.png)
_Double-clicking the frame_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-25.png)
_Renamed button frame_

### How to Create Variants

Next, we'll make the button frame a variant. 

Variants help you create multiple versions or states of a component. They're very useful when designing interfaces that have different states or variations, such as buttons with different sizes or designs, like we're creating here.

To make the button frame a variant, double-click on the component icon at the top of your screen.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-26.png)
_Moving to the component icon at the top of the screen and double-clicking_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-27.png)
_Variant of the button component_

Next, I'll add another variant because I want to have three states for the button (Default, Hover, and Active). To add another variant, click on the plus icon on any of the already existing variants.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-28.png)
_Clicking on the olus icon on a variant to add nother variant_

Automatically, a new variant will be added.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-29.png)
_Added third variant_

Next, I'll increase the size of the component frame so it can accommodate other variants that will be added. To do this, simply select the whole component, and drag to your satisfied size.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-30.png)
_Selecting the component frame_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-31.png)
_Increasing the width of the component frame._

### How to Create Hover and Active States

Next, I'll tweak the last two buttons (hover and active states), so the difference between the three button states will be obvious. To do this, I'll make the hover state lighter, and the active state darker.

For the hover state, I'll change the color code to #392AE7, which is a lighter shade of blue. Make sure the particular button is selected so the changes take effect:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-32.png)
_Changing color code for the hover state_

For the active state, I'll change the color code to #19107A which is a slightly darker shade of blue.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-33.png)
_Changing the color code of the active state_

### How to Create Other Button States 

Next, we want to create other button states (buttons with icons on either side of the text, and with icons only).

To start with, I'll duplicate the three buttons. To do this, select the three buttons and duplicate using Ctrl + D.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-34.png)
_Duplicating the three buttons_

Next, we want to create button components with text and a left icon. To do this, click on the eye on the left icons on each of the icons to reveal them.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-35.png)
_Revealing the icons on the left side of the buttons_

Next, we want to create button components with text and a right icon.

To do this, duplicate the buttons again, and do the same for the right icons.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-36.png)
_Duplicating the buttons a second time_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-37.png)
_Revealing the icons on the right side_

Lastly, we want to create button components with icons only.

To do that, we'll duplicate the buttons one last time to hide the text.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-38.png)
_Duplicating the buttons a third time_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-39.png)
_Hiding the text_

I'll make the _icon only_ frames a square shape. To do that, select the three frames and drag to resize.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-40.png)
_Selecting the 'icons only' frames_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-41.png)
_Resizing the frames_

I'll now resize the component frame to fit its content.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-42.png)
_Resizing the component frame._

Next, we'll rename the different button states so it'll be easy to identify them. First, select the whole component frame. Then move to the section labelled _Properties_, and change _Property 1_ to _Button_ to show that this is a button component.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-43.png)
_Moving to properties section_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-44.png)
_Renaming the component frame_

Next, we'll rename the button frames by icons. Select the first three frames horizontally, and go over to the _Current variant_ section. Rename them _No icons_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-46.png)
_Selecting first three buttons and renaming them_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-47.png)
_Renamed no icons buttons_

We'll do same for the next three buttons, and name them _Left Icons_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-48.png)
_Renamed left icons' buttons_

We'll do the same thing for the next set, renaming them _Right Icons_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-49.png)
_Renamed right icons' buttons_

Finally, for the last set, we'll rename the buttons _Icons only_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-50.png)
_Renamed icons only buttons_

### How to Group Buttons by States

Next, we'll group the buttons by states and name them. We'll start with the first state: _Default_. Select all the button frames under default and move to the _Current variant section_ on the right hand panel. Click on the configure icon to edit the component configuration.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-51.png)
_Clicking on configure icon_

Click on the description box to add a description. In this case, I'll simply type _Default state_. 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-55.png)
_Adding a description_

Do the same for the other two states – hover and active.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-53.png)
_Adding a description for the hover state_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-54.png)
_Adding a description for the active state_

### How to Make the Button Components Interactive

To start, switch to the Prototype tab, located at the top of your screen, right-hand panel.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-56.png)
_Switching to prototype mode_

Next, add an interaction from the first to the second _no icon_ button frame. To do this, click on the first button frame and drag the plus icon to the second frame.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-57.png)
_Adding an interaction_

This will bring up a list of interaction options and settings  for the animation. 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-58.png)
_Bringing up interaction setting_

Change _On click_ to _While hovering_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-60.png)
_Changing interaction type to "while hovering"_

Do the same for the next button frame but, instead of _While hovering_, change to _While pressing_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-61.png)
_Animating the third button frame_

Now, repeat the same steps for the other sets.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-62.png)
_Repeating the animation steps for the other button sets._

Voilà, you just created an interactive button component. 

## Conclusion

Components help enhance your designs and make them more efficient. They also help you save time and they improve consistency across your designs. But they can only help when they're created the right way.

Practicing often will help improve your ability to create helpful reusable components. Remember, make every decision with your users in mind.

