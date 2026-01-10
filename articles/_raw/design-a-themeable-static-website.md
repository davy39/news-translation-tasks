---
title: How to Create a Theme-able Static Website
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-02-08T21:00:38.000Z'
originalURL: https://freecodecamp.org/news/design-a-themeable-static-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/20210207_172754_0000-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Static Site Generators
  slug: static-site-generators
- name: ux design
  slug: ux-design
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'A while ago I wanted to create a dark theme for my personal site. So I
  did some clicking around to find out the most suitable and clean way to do this.

  I read Max Bock''s article on creating a custom theme, where he explained the process
  quite clearly...'
---

A while ago I wanted to create a dark theme for my [personal site](https://spruce.com.ng). So I did some clicking around to find out the most suitable and **clean** way to do this.

I read [Max Bock's article on creating a custom theme](https://mxb.dev/blog/color-theme-switcher), where he explained the process quite clearly. He also really went super pro (with TEN different color schemes).

But for my case I wanted more. I wanted users to be able to change the color scheme to the different options provided.

I also wanted them to be able to change the font size. This is because I had a fixed header on my site which was kind of great, but on small mobile devices it took up quiet a lot of space – not great for UX design, right? So I also gave users the ability to turn off that fixed header.

![spruce.com.ng customizable static website preview with dark theme](https://www.freecodecamp.org/news/content/images/2021/02/spruce-theme.png align="left")

*Spruce.com.ng Theme-able static site*

You can find a live preview of this on my personal site [spruce.com.ng](https://spruce.com.ng). You can also copy the source code [here](#not-much-of-a-tutorial-person-you-can-copy-the-complete-source-code-here) to save you some read time.

## What I Wanted to Do

1. Ask users their preferred color scheme, font size, and header type (fixed or static)
    
2. Collect user choices
    
3. Save them in localStorage
    
4. Get them from localStorage and show them to the user immediately on page reload, if they switch tabs and come back, and if they close their browser and come back after a week or month, until they clear their browser storage
    

## How I Created the Theme

In 11ty (the static site generator I'm using) you can create a JSON file in the `_data` folder. You can access the data globally in your template (Jekyll does this too). It's likely that your preferred static site generator (SSG) can do the same.

```json
_data/themes.json file

[
    {
        "id": "default",
        "colors": {
            "text": "#222126",
            "text-dark": "#777;",
            "border": "rgba(0,0,0,.1)",
            "primary": "#665df5",
            "secondary": "#6ad1e0",
            "primary-dark": "#382cf1",
            "bg": "#ffffff",
            "bg-alt": "#f8f8f8",
            "overlay": "rgba(255, 255, 255, .4)"
        }
                }, 
    ... other color schemes
]
```

## How to Generate the CSS

To use the data file, create a file called `theme.css.liquid` and give it a permalink where you want the CSS file to output to.

```css
css/theme.css.liquid file
---
permalink: /css/theme.css
---
// when no theme is selected
// use default theme
:root {
    --text: {{ themes[0].colors.text }};
    --text-dark: {{ themes[0].colors.text-dark }};
    --border: {{ themes[0].colors.border }};
    --primary: {{ themes[0].colors.primary }};
    --secondary: {{ themes[0].colors.secondary }};
    --primary-dark: {{ themes[0].colors.primary-dark }};
    --bg: {{ themes[0].colors.bg }};
    --bg-alt: {{ themes[0].colors.bg-alt }};
}  
// if user preferred color scheme is dark
// use the dark theme

@media(prefers-color-scheme: dark) {
    :root {
    --text: {{ themes[1].colors.text }};
    --text-dark: {{ themes[1].colors.text-dark }};
    --border: {{ themes[1].colors.border }};
    --primary: {{ themes[1].colors.primary }};
    --secondary: {{ themes[1].colors.secondary }};
    --primary-dark: {{ themes[1].colors.primary-dark }};
    --bg: {{ themes[1].colors.bg }};
    --bg-alt: {{ themes[1].colors.bg-alt }};
    }
}
// generate the theme css from the data file
// here we use a for loop
// to iterate over all the themes in our _data/themes.json
// and output them as plain css


{% for theme in themes %}
 [data-theme="{{ theme.id }}"] {
    --text: {{ theme.colors.text }};
    --text-dark: {{ theme.colors.text-dark }};
    --border: {{ theme.colors.border }};
    --primary: {{ theme.colors.primary }};
    --secondary: {{ theme.colors.secondary }};
    --primary-dark: {{ theme.colors.primary-dark }};
    --bg: {{ theme.colors.bg }};
    --bg-alt: {{ theme.colors.bg-alt }};
 }
{% endfor %}
```

Notice that I'm using **themes\[0\].colors.text** because my default theme is the first one on the list. It has an index of 0, so also my dark theme has an index of 1.

In **Jekyll** you can output liquid in CSS by just adding empty front matter at the top of the file.

```css
css/theme.css file
---
---

// your liquid in css goes here
```

I'm sure your favourite static site generator provides a similar way to output liquid in a CSS file. You can also handcode all this if you are just writing plain HTML and CSS without a SSG.

## How to Use the CSS in Your Site

If you are reading this, then I assume that you already know how to work with CSS custom properties. So I won't go in depth into that here.

```css
// css custom properties are declared using the keyword **var**
// color: var(--text);
body {
    background: var(--bg);
    color: var(--text);
}
h1,h2 {
    color: var(--text-dark)
}
// i also had default font-size and margin-top properties set
// i added this to the :root in css
:root {
    --font-size: 18px;
    --position: fixed;
    --top-margin: 96px;
}
```

You just have to change every bit of color on your site to the custom properties you have generated.

## How to Generate the HTML

Now let's provide a UI to allow users to change the font size, header type, and color scheme of our site. Mine is a bit simple, but you can take yours further. I'm just explaining the concept here.

```html
theme.html file
// create the font buttons
// I gave each button a value
// I want to get the value and save it in local storage 

<section class="theme-section">
    <div class="theme-btn-wrapper">
        <button class="btn btn--small btn--border js-font-btn" value="16">16px</button>
        <button class="btn btn--small btn--border js-font-btn" value="18">18px</button>
        <button class="btn btn--small btn--border js-font-btn" value="20">20px</button>
        <button class="btn btn--small btn--border js-font-btn" value="22">22px</button>
    </div>
</section>

// Create the toggle button
// To turn On & Off
// The fixed header
// The **sr-only** is used to hide the text visually 
// while keeping accessibilty in mind
// note the **role="switch"** nd aria-checked
// they are what turns the button to a On and Off switch
<div class="check-wrapper">
    <span id="btn-label" class="sr-only">Fixed or static header</span>
   <button role="switch" type="button" aria-checked="true" aria-labelledby="btn-label" class="js-theme-toggle btn btn--border btn--rounded btn--toggle">
       <span>On</span>
       <span>Off</span>
   </button>
</div>
```

That's pretty much the HTML for my use case. Again you can do more if you want, and there is some CSS styling involved (which would be left out in our case).

## The Fun Part: How to Create the JavaScript

```js
/assets/js/theme.js file
class CustomTheme {
    constructor() {
        // part A: check if localStorage works
        this.islocalStorage = function() {
            try {
                localStorage.setItem("test", "testing");
                localStorage.removeItem("test");
                return true;
            } catch (error) {
                return false
            }
           
        };
        // part B: Get the value from the buttons
        this.schemeBtns = document.querySelectorAll('.js-theme-color');
        this.schemeBtns.forEach((btn) => {
            const btnVal = btn.value;
            btn.addEventListener('click', () => this.themeScheme(btnVal))
        });

        this.fontBtns = document.querySelectorAll('.js-font-btn');
        this.fontBtns.forEach((btn) => {
            const btnVal = btn.value;
            const btnTag = btn;
            btn.addEventListener('click', () => this.themeFont(btnVal, btnTag))
        });

        // part C: get the html button element
        this.switchBtn = document.querySelector('.js-theme-toggle');
        const clicked = this.switchBtn;
        this.switchBtn.addEventListener('click', () => this.themePosition(clicked))
    }

    // part D: Save the data in localStorage
    themeScheme(btnVal) {
        document.documentElement.setAttribute('data-theme', btnVal);
        if (this.islocalStorage) {
            localStorage.setItem('theme-name', btnVal);
        }
    };
    
    themeFont(btnVal,btnTag) {
        document.documentElement.style.setProperty('--font-size', `${btnVal}px`);
        if (this.islocalStorage) {
            localStorage.setItem('font-size', btnVal);
        }
        ;
        if (btnVal == localStorage.getItem('font-size')) {
            removeActive();
            btnTag.classList.add('active');
    }
};

    themePosition(clicked) {
    if (clicked.getAttribute('aria-checked') == 'true') {
        clicked.setAttribute('aria-checked', 'false');
        document.documentElement.style.setProperty('--position', 'static');
        document.documentElement.style.setProperty('--top-margin', '0px');
        if (this.islocalStorage) {
            localStorage.setItem('position', 'static');
        }

    } else {
        clicked.setAttribute('aria-checked', 'true');
        document.documentElement.style.setProperty('--position', 'fixed');
        document.documentElement.style.setProperty('--top-margin', '96px');
        if (this.islocalStorage) {
            localStorage.setItem('position', 'fixed');
        }
    }

    }
}

function removeActive() {
    const btns = document.querySelectorAll('.js-font-btn');
    btns.forEach((btn) => {
        btn.classList.remove('active');
    })
}

// part E: Only use our class if css custom properties are supported
if (window.CSS && CSS.supports('color', 'var(--i-support')) {
    new CustomTheme()
};

// part E: Add an active class to selected font size button

window.addEventListener('load', () => {
    const fontBtns = document.querySelectorAll('.js-font-btn');
    fontBtns.forEach((btn) => {
        const btnVal = btn.value;
        const btnTag = btn;
        if (btnVal == localStorage.getItem('font-size')) {
            btnTag.classList.add('active');
    }
    });   
})
```

I know that's a big chunk of JavaScript code, but it basically only does a few things:

* it collects and checks if localStorage is supported
    
* then it saves the data in localStorage
    

Also notice that I used **Javascript Classes**, but you could use functions as well.

### Checking for local storage

A lot of browsers support localStorage these days, but why do we still need to check?

Some users may be browsing your site in **incognito mode (private browsing mode)**. And sometimes localStorage is turned off by default so it doesn't save anything on the users device.

So instead of saving it directly and sometimes getting an error on browsers that don't support it, we can check if the browser does support it. If it does, great – and if it doesn't then we're also cool.

Now if you notice, everything seems to work just fine. But if you change the theme or font size and you reload your browser, everything is going to revert to default. This is because we haven't used the data we stored in **localStorage**

So go ahead and add this piece of code to the top of your head file before any CSS files. We're doing this to eliminate the flash you get when you reload your browser.

```js
<script>
    const scheme = localStorage.getItem('theme-name');
      document.documentElement.setAttribute('data-theme', scheme);

      const fontSize = localStorage.getItem('font-size');
    document.documentElement.style.setProperty('--font-size',  `${fontSize}px`);
    

    const position = localStorage.getItem('position');
    if (position == 'fixed') {
        document.documentElement.style.setProperty('--position', 'fixed');
        document.documentElement.style.setProperty('--top-margin', '96px');

    } else {
        document.documentElement.style.setProperty('--position', 'static');
        document.documentElement.style.setProperty('--top-margin', '0px');

    }    
    
  </script>
```

## Wrapping up

And that's it! You now have a simple and customizable static site.

The main purpose of this guide was to show you the endless possibilities of creating a user-customizable website. So go ahead and play around with it – there are a lot of things you can do, like:

1. Show users specific content based on their choices
    
2. Display notification messages based on user's visits
    
3. Display ads in the least annoying way by showing users ads based on user choices
    

You can do these things and a lot more with our SSG's. Just imagine the endless possibilities.

Not much of a tutorial person? You can copy the complete source code [here](https://spruce.com.ng/blog/on-designing-a-themeable-static-website).
