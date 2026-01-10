---
title: How to create themes for your Angular 7 apps using CSS Variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:22:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-themes-for-your-angular-7-apps-using-css-variables-69251690e9c5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_r2HnHAK7lak_Fee
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Stephen McLean

  In this post, we will build a super simple cryptocurrency listing app using Angular
  7 and CSS variables.

  Table of Contents


  Design

  Project Setup

  Code

  Conclusion, Repo, and Further Reading



  What we’re aiming for

  Design

  Feel free to ...'
---

By Stephen McLean

In this post, we will build a super simple cryptocurrency listing app using Angular 7 and CSS variables.

### Table of Contents

* [Design](#42d3)
* [Project Setup](#868f)
* [Code](#8b88)
* [Conclusion, Repo, and Further Reading](#5106)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qQjQUQCwg_mhbeMtwXg3Q.gif)
_What we’re aiming for_

### Design

Feel free to [skip this section](#868f) if you’re only here for the code.

I designed this simple app using [Figma](https://www.figma.com/).

#### Color Scheme

Our color scheme is made up of _foreground_, _background_, _primary_, and _error_ colors. Each color group has several lighter and darker variants of the base color.

For our light/dark themes, the foreground and background colors will simply swap.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A4&scaling=min-zoom&redirected=1]

#### Components

Next up is to create the components. Since our app is pretty small, we only have a couple of components.

The _nav_ component, which will let our user toggle the theme.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A2&scaling=min-zoom&redirected=1]

The _tile_ component which will display coin info.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=2%3A60&scaling=min-zoom&redirected=1]

Putting it all together, we get our target designs.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A3&scaling=min-zoom&redirected=1]

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=2%3A53&scaling=min-zoom&redirected=1]

#### Project Setup

We are going to scaffold our app using the Angular CLI. First, we need to install it.

```
npm install -g @angular/cli
```

Then create our app.

```
ng new project-crypto
```

And finally, generate a module to hold our theming logic.

```
cd project-crypto 
```

```
ng generate module theme 
```

### Code

Alright, time for the good stuff.

#### Define CSS Variables

Let’s start by defining out initial CSS variables. We can set them initially to reflect our light theme. Since we want our theme to be global, I have defined it using the `:root` selector, which will match the `html` element. You could use the `body` or some other high-level element here if you wish.

```js
@import url("https://fonts.googleapis.com/css?family=PT+Sans:400,700");
@import url("https://fonts.googleapis.com/css?family=Inconsolata:400,700");

:root {
  /* Colors */
  --foreground-default: #08090a;
  --foreground-secondary: #41474d;
  --foreground-tertiary: #797c80;
  --foreground-quaternary: #f4faff;
  --foreground-light: #41474d;

  --background-default: #f4faff;
  --background-secondary: #a3b9cc;
  --background-tertiary: #5c7d99;
  --background-light: #ffffff;

  --primary-default: #5dfdcb;
  --primary-dark: #24b286;
  --primary-light: #b2ffe7;

  --error-default: #ef3e36;
  --error-dark: #800600;
  --error-light: #ffcecc;

  /* Shadows */
  --background-tertiary-shadow: 0 1px 3px 0 rgba(92, 125, 153, 0.5);
}

body {
  background: var(--background-default);
}

html,
body {
  margin: 0;
  padding: 0;
  font-family: "PT Sans", sans-serif;
}
```

#### Define the themes

Next, let’s define our themes in TypeScript. These will later be used to toggle the theme by an Angular service.

Under our newly created `theme` module, create a new file: `theme.ts`

```js
export interface Theme {
  name: string;
  properties: any;
}

export const light: Theme = {
  name: "light",
  properties: {
    "--foreground-default": "#08090A",
    "--foreground-secondary": "#41474D",
    "--foreground-tertiary": "#797C80",
    "--foreground-quaternary": "#F4FAFF",
    "--foreground-light": "#41474D",

    "--background-default": "#F4FAFF",
    "--background-secondary": "#A3B9CC",
    "--background-tertiary": "#5C7D99",
    "--background-light": "#FFFFFF",

    "--primary-default": "#5DFDCB",
    "--primary-dark": "#24B286",
    "--primary-light": "#B2FFE7",

    "--error-default": "#EF3E36",
    "--error-dark": "#800600",
    "--error-light": "#FFCECC",

    "--background-tertiary-shadow": "0 1px 3px 0 rgba(92, 125, 153, 0.5)"
  }
};

export const dark: Theme = {
  name: "dark",
  properties: {
    "--foreground-default": "#5C7D99",
    "--foreground-secondary": "#A3B9CC",
    "--foreground-tertiary": "#F4FAFF",
    "--foreground-quaternary": "#E5E5E5",
    "--foreground-light": "#FFFFFF",

    "--background-default": "#797C80",
    "--background-secondary": "#41474D",
    "--background-tertiary": "#08090A",
    "--background-light": "#41474D",

    "--primary-default": "#5DFDCB",
    "--primary-dark": "#24B286",
    "--primary-light": "#B2FFE7",

    "--error-default": "#EF3E36",
    "--error-dark": "#800600",
    "--error-light": "#FFCECC",

    "--background-tertiary-shadow": "0 1px 3px 0 rgba(8, 9, 10, 0.5)"
  }
};
```

We can add as many themes as we like here. For now, let’s just stick with light and dark themes.

#### Create the theme service

Our service will be responsible for: **tracking the active theme**, and **updating the CSS variables** based on the active theme.

We can use the CLI to generate our new service. Under `/src/app/theme` run

```
ng generate service theme
```

```
import { Injectable } from "@angular/core";
import { Theme, light, dark } from "./theme";

@Injectable({
  providedIn: "root"
})
export class ThemeService {
  private active: Theme = light;
  private availableThemes: Theme[] = [light, dark];

  getAvailableThemes(): Theme[] {
    return this.availableThemes;
  }

  getActiveTheme(): Theme {
    return this.active;
  }

  isDarkTheme(): boolean {
    return this.active.name === dark.name;
  }

  setDarkTheme(): void {
    this.setActiveTheme(dark);
  }

  setLightTheme(): void {
    this.setActiveTheme(light);
  }

  setActiveTheme(theme: Theme): void {
    this.active = theme;

    Object.keys(this.active.properties).forEach(property => {
      document.documentElement.style.setProperty(
        property,
        this.active.properties[property]
      );
    });
  }
}
```

Some things to note here:

1. We import our theme definitions that we just created, on line 2.
2. Lines 34–39 update our CSS variables defined in the theme. This is essentially where the magic is happening.
3. Since, in this example app, we only have two themes, I have added some convenience functions to set the theme to light and dark directly. You can use the `getAvailableThemes` and `setActiveTheme` functions to change the theme dynamically based on user input instead.

#### Components

The hard work is done. Now we just need to put our building blocks together. Well, actually, first we need to create the building blocks ?. Let’s create the components.

We will start with the **nav** component. Again, we can use the Angular CLI to give us a head start.

```
ng generate component nav
```

```js
import { Component, OnInit } from "@angular/core";
import {
  faLightbulb as faSolidLightbulb,
  faDollarSign,
  IconDefinition
} from "@fortawesome/free-solid-svg-icons";
import { faLightbulb as faRegularLightbulb } from "@fortawesome/free-regular-svg-icons";
import { ThemeService } from "src/app/theme/theme.service";

@Component({
  selector: "app-nav",
  templateUrl: "./nav.component.html",
  styleUrls: ["./nav.component.css"]
})
export class NavComponent implements OnInit {
  faLightbulb: IconDefinition;
  faDollarSign = faDollarSign;

  constructor(
    private themeService: ThemeService
  ) {}

  ngOnInit() {
    this.setLightbulb();
  }

  setLightbulb() {
    if (this.themeService.isDarkTheme()) {
      this.faLightbulb = faRegularLightbulb;
    } else {
      this.faLightbulb = faSolidLightbulb;
    }
  }

  toggleTheme() {
    if (this.themeService.isDarkTheme()) {
      this.themeService.setLightTheme();
    } else {
      this.themeService.setDarkTheme();
    }

    this.setLightbulb();
  }
}
```

**Note:** I have used Font Awesome for the icons on the nav bar. If you want to do the same, you will need to [install Font Awesome for Angular](https://fontawesome.com/how-to-use/on-the-web/using-with/angular).

The logic for our nav component is pretty straight forward. We set our icon depending on the theme on initialization (line 22). Then we set up an event handler to toggle the theme. You can see it’s usage in the HTML below.

```js
<nav>
  <fa-icon [icon]="faDollarSign"></fa-icon>
  <h5 class="title secondary-font">ProjectCrypto</h5>
  <fa-icon [icon]="faLightbulb" (click)="toggleTheme()"></fa-icon>
</nav>
```

```css
nav {
  height: 4rem;
  display: flex;
  align-items: center;
  padding-left: 1rem;
  padding-right: 1rem;
  background-color: var(--background-tertiary);
  color: var(--foreground-quaternary);
  font-size: 1rem;
}

nav .title {
  margin-left: auto;
  margin-right: auto;
}
```

Notes on the nav component CSS:

1. Line 7, and 8 are the important ones here. These are the two lines that use our previously defined CSS variables, and make this component themeable.

Next, the **tile** component.

```
<div class="container">
  <h5 class="name">{{ name }}</h5>
  <h5 class="price">
    <fa-icon [icon]="currencyIcon"></fa-icon>
    {{ price | number }}
  </h5>
  <fa-icon
    [icon]="faHeart"
    (click)="onToggleFavourite()"
    class="favouriteIcon icon"
    [ngClass]="{ isFavourite: isFavourite }"
  ></fa-icon>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 0.5fr 1fr 0.5fr;
  align-items: center;
  border-radius: 0.5rem;
  background: var(--background-light);
  color: var(--foreground-tertiary);
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  margin-bottom: 1rem;
  min-height: 8rem;
  box-shadow: var(--background-tertiary-shadow);
}

.container .name {
  justify-self: start;
}

.container .price {
  justify-self: center;
}

.container .icon {
  justify-self: end;
}

.favouriteIcon {
  font-size: 1.5rem;
}

.isFavourite {
  color: var(--primary-default);
}
```

Notes:

1. The TypeScript for our tile component doesn’t have any theming logic, so I have omitted it here.
2. Lines 6, 7, 12, and 32 are what enable our tile component to be themeable.

### Conclusion, Repo, and Further Reading

And that’s it! You now have the components and theme created. You can add the components to your base app component to wire everything up with some test data.

You can find the repo [here](https://github.com/stephan-mclean/project-crypto).

Learn more about CSS Variables [here](https://medium.freecodecamp.org/everything-you-need-to-know-about-css-variables-c74d922ea855).

Thanks for reading!

