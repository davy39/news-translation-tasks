---
title: How to dynamically theme your Ionic application and make your users happy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-10T16:35:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-dynamically-theme-your-ionic-application-and-make-your-users-happy-ffa17e15dbf7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FPTVBGFH--t0AHelBsBX2g.png
tags:
- name: Ionic Framework
  slug: ionic
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Ryan Gordon

  Designing a sleek color scheme for your mobile application can be time consuming.
  Why not let the user choose their own favourite theme?

  This is one of my favorite features in apps. It provides a great experience for
  users who don’t wa...'
---

By Ryan Gordon

Designing a sleek color scheme for your mobile application can be time consuming. Why not let the user choose their own favourite theme?

This is one of my favorite features in apps. It provides a great experience for users who don’t want to be tied down to one primary accent color scheme or want to personalize the theme to suit their own style.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mCKTtAbjsDbmijNnIQPI6Q.jpeg)
_A great example of dynamic themes in the ToDoist app_

In this Medium post, we will work through a project which will have a number of themes the user can select at run-time just like above. When a theme is selected by the user, ideally this change should happen in real-time rather than requiring the user to reopen the app.

### Installation and getting started

Ionic, if you haven’t used it before, is a mobile application framework which lets you write mobile apps in HTML, CSS, and Typescript. With one shared codebase, you can develop an application for iOS or Android or you can deploy it as a web app.

To install Ionic, open a terminal and enter :

`npm install -g ionic@latest`

> Note: you must have [Node JS and npm](https://nodejs.org/en/download/) installed. If you get an error with code ‘EACCES,’ then you may need sudo or admin privileges.

For this tutorial, the sidemenu template provides a good starting point. To generate a project with this template, enter this command into the terminal:

`ionic start <name of your app> si`demenu

![Image](https://cdn-media-1.freecodecamp.org/images/1*mLFWCTj1IhdMdMiXSI7OVg.png)
_Example terminal output from the CLI_

After the project has generated, change into the directory with:

`cd <name of your a`pp>

Now you have an Ionic project with a sidemenu and two pages ready to go! To see your creation, enter `ionic serve` in your terminal.

#### Setting up the first 2 themes: Todoist Red vs Noir

In order to set up the first two themes, we’ll need to complete a number of steps. Pretty much all of these steps need to be followed in order to get the themes working.

First, we need to denote an SCSS file which will be used when the theme is applied. In the `src/theme` directory of your project, you’ll find a `variables.scss` . The respective theme files are located here, too. Create a new file called:

```
red.theme.scss
```

This file will be used to apply the first theme. From this file, any of the default Ionic styling can be overridden. There are two options for how we can apply the themes:

Option 1: Styling just the navbar and certain elements

Option 2: Applying the theme to all background content

Here is an example of both options applied. The code has a checkpoint halfway down. If you don’t want to style the whole app, comment out the rest of the code below it:

That’s the first SCSS file created! Next will be for dark mode. Create another new file called:

```
noir.theme.scss
```

This file will be used to apply the second theme. We won’t need to change much for the second theme to work other than changing the hexcode values to a colour such as `#33333` .

It’s important to note, though, that **we will need to rename** **the SCSS class from `theme-red` to something unique** for this theme. I’ll call mine `theme-noir` .

The next step is to import the SCSS files into the app itself. This is important, otherwise the theme won’t be loaded into the app. Head to the `app.scss` file located at `src/app/app.scss` where you can import the theme like so:

```
@import '../theme/red.theme';@import '../theme/noir.theme';
```

Now that we’ve created and imported the theme files into the project, the SCSS side of things is taken care of! Now onto the Typescript and HTML.

### Programmatically changing the theme

Changing the theme itself will only require three more steps for a simple setup:

* a wrapper around the app
* a function to change the theme at run-time
* something to hold the state of the current theme

#### The AppState class

The AppState class will be an injectable Angular component that holds what the current theme, and that can also be used to update the theme.

There isn’t much to how it works, other than that it has an internal state variable. When a Get operation is called, a clone of the state is returned. When a Set happens, a property of the state is updated with a new value, in this case the theme.

The AppState will hold the current theme and allow modification, but it will need to be imported into the component you want to use it with.

When an Ionic app is first setup using the CLI, you’ll find the following code in the `app.component.ts` :

```
// used for an example of ngFor and navigation
```

```
this.pages = [
```

```
{ title: 'Default Red Theme', component: HomePage },
```

```
{ title: 'List', component: ListPage }
```

```
];
```

The array that’s displayed is used to provide content for the sidemenu. This sidemenu will serve as our theme switcher in this project rather than a navigation menu.

Change the values in **this.pages** to reflect the names of the themes you want the user to see (like the theme file that will be applied, and any other assets like images files).

In this example, the ‘theme file’ is going to be the name of the CSS class that we want to use. We’ve already imported the SCSS files by the time the app is running. So rather than accessing the file itself, we access the root class in that file. In the case of the red theme, the ‘theme-noir’ class will be applied.

#### Displaying available themes and applying the wrapper

The last step we need to take will be to add a wrapper div. This will be the top level element in the `app.html` file. This wrapper will have the chosen theme applied to it, allowing children elements to receive style updates also. An example of this in `app.html` would look like this:

```
<!-- Wrapper over the app which will use the theming-->
```

```
<div class="{{global.state['theme']}}">
```

```
    //in here you will have the rest of app.html 
```

```
</div>
```

In terms of display, if you followed above and renamed the `this.pages` array to `this.themes` so it holds your available themes, then you don’t need to change anything else to display!

The sidemenu originally was used to push to available pages in the app, but now it’s a great theme switcher. The names of each available theme are displayed using NgFor and some databinding with the `this.themes` array. The result will be a very simple list which will have the name of the theme for each entry. When an entry is clicked, that theme will be applied.

On the [Github repo](https://github.com/Ryan-Gordon/ionic-dynamic-themes) you can find a better example with a color indicator next to each entry.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-QxmagEFaYE8JMn5w9RHA.png)

### Recap

Okay time for a quick review of what we have done here. So far we have implemented the following changes to get the theming working:

* Created theme SCSS files for each desired theme
* Imported the created theme files in the main Sass file located at `src/app/app.scss`
* Setup an AppState class to hold which theme is currently applied
* Setup a very small changeTheme function which will set a new theme into AppState
* Added a wrapper element over the `app.html` which will have the theme applied to it

To create more themes from here, copy one of the theme files you already created, rename it, and change the hex colour values in this new file. You can make as many as you want! Just make sure that you also import this new theme file in `app.scss` like you did with the first ones, otherwise it won’t work.

With these five steps you can have dynamic theming in any Ionic application. The beauty of the solution is that it works well on all platforms since it uses no native plugins — everything is in HTML,CSS and TS.

As a bonus, on the [GitHub repo](https://github.com/Ryan-Gordon/ionic-dynamic-themes), I have implemented two other ways to present the available themes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FPTVBGFH--t0AHelBsBX2g.png)
_Option 2 on the left and a model option on the right_

### Conclusion:

Dynamic theming saves us from worrying whether our chosen colour scheme will suit all audiences. Instead of doing numerous mockups with different schemes to evaluate, we can simply implement all of the colour schemes and let the user choose which one they prefer at runtime.

A hidden benefit of this is that we can collect analytics from our users on which theme suits them best. In the `changeTheme` function discussed, a webhook or some event could be sent specifying the user’s choice. Through this, developers could gather real user feedback on which themes ‘work’ and which don’t.

All the source code for this tutorial can be found in this [Github repo](https://github.com/Ryan-Gordon/ionic-dynamic-themes).

![Image](https://cdn-media-1.freecodecamp.org/images/1*LGQFvGWTml9dQTsUJO-s8g.png)
_One last look_

Please consider leaving a star on the repo. I welcome any and all additions.

