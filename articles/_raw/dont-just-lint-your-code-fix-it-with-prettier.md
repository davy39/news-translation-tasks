---
title: Don’t just lint your code - fix it with Prettier
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-11-06T15:45:00.000Z'
originalURL: https://freecodecamp.org/news/dont-just-lint-your-code-fix-it-with-prettier
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/formatting-1.jpg
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: eslint
  slug: eslint
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: Prettier
  slug: prettier
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Linting makes our lives easier because it tells us what’s wrong with our
  code. But how can we avoid doing the actual work that goes into fixing it?

  Previously I wrote about linting, what it is, and how it makes your life easier.
  At the end, I actuall...'
---

Linting makes our lives easier because it tells us what’s wrong with our code. But how can we avoid doing the actual work that goes into fixing it?

[Previously I wrote about linting](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/), what it is, and how it makes your life easier. At the end, I actually included a way that you could automatically fix your code. So why am I writing this?

## **What do you mean fix it?**

Before we roll into it, let’s hit this quick. Linters are powerful and provide an easy way to scan your code for syntax errors that could lead to bugs. Or they can simply help keep a codebase clean, healthy, and consistent. When run, it will show all the issues and let you go through each one individually to fix them.

Taking that to the next level, some linters will actually allow you to pass in an argument to the command running the linter that allows it to fix it for you automagically. This means you don’t have to manually go through and make all of those little whitespace and semicolon (add them! ?) tweaks yourself!

![Image](https://www.freecodecamp.org/news/content/images/2019/11/ron-swanson-happy.gif)
_Ron Swanson happy_

## **So what more can I do to fix things?**

If you already use the fix option, thats a good start. But there are tools out there that have been developed specifically to tackle this problem beyond just a flag into your command. The one I’m going to cover is Prettier.

## **What is Prettier?**

[Prettier](https://prettier.io/) pegs itself as “an opinionated code formatter." It takes an input of your code and outputs it in a consistent format stripping any of the original code style. It actually converts your code to a [syntax tree](https://github.com/benjamn/recast), then rewrites it using the styles and rules you and Prettier provide together via your ESLint config and Prettier’s default rules.

You can easily use Prettier alone just to format your code, which works just fine. But if you combine this with an underlying ESLint process, you get both a powerful linter and a powerful fixer. I’m going to show you how to make those work together.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/voltron.gif)
_Voltron_

## **Getting started with Prettier**

For this walkthrough, I’m going to assume that you have ESLint set up and configured in an application. Particularly, I’m going to pick up where I left off in my previous walkthrough where [we installed ESLint to a React application](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/).

Additionally of note, Prettier tells us right from the start that it's an opinionated code formatter. You should expect that it will format your code in a consistent way, but maybe a different way than you currently have it configured. But don’t fret! You can tweak this configuration.

So what are we starting off with? We already:

* Have installed [ESLint](https://github.com/eslint/eslint)
* Have added [Babel](https://github.com/babel/babel-eslint) as our parser
* Have added a [plugin](https://github.com/yannickcr/eslint-plugin-react) that includes React configurations

Next, let’s get started by installing a few packages:

```shell
yarn add prettier prettier-eslint prettier-eslint-cli -D
```

_Note: the command above is similar to using `npm`. If your project doesn't use `yarn`, swap out to `npm` as appropriate._

Above, we’re installing:

* [prettier](https://github.com/prettier/prettier): core Prettier package and engine
* [prettier-lint](https://github.com/prettier/prettier-eslint): passes the Prettier result to ESLint to fix using your ESLint config
* [prettier-eslint-cli](https://github.com/prettier/prettier-eslint-cli): helps Prettier and ESLint work together on various files across your project

And we’re installing them as a dev dependency, as we don’t need it outside development.

## **Configuring your new formatter**

Now that our packages are installed, we can set up `yarn` to run this command for us.

Previously, we set up a `lint` script to look like this in our `package.json`:

```json
"scripts": {
  ...
  "lint": "eslint . --ext .js"
  ...
}
```

We’re going to leave that as it is, but we’ll do something similar and create a new script right next to it called `format` for our formatter Prettier:

```json
"scripts": {
  ...
  "format": "prettier-eslint --eslint-config-path ./.eslintrc.js --write '**/*.js'",
  "lint": "eslint . --ext .js"
  ...
}
```

So what’s going on there? We’re:

* Adding a new script called `format`, that we can run as `yarn format`
* We’re utilizing our `prettier-eslint-cli` package to run the formatting for us
* We’re passing in our ESLint config located next to our `package.json` in the root of the project (change this if it’s in a different location)
* And finally, we’re telling prettier to write all files matching `**/*.js`, or any JS files it finds recursively through our project

The beauty here is that we're passing in our ESLint config to Prettier. This means we only have to maintain 1 config for both tools, but we still leverage the linting power of ESLint along with the formatting power of Prettier.

## **Run your formatter!**

Now that we’re all set up, let’s run it! Run this following:

```
yarn format

```

and immediately, we see that it works:

![Image](https://www.freecodecamp.org/news/content/images/2019/11/prettier-command-line-success.png)
_Successfully running Prettier_

## **Hey, my code looks different!**

![Image](https://www.freecodecamp.org/news/content/images/2019/11/spongebob-pitchforks.gif)
_Angry mob with pitchforks_

As I mentioned earlier, Prettier tells us straight up, it’s an opinionated formatter. It ships with its own rules, sort of like its own ESLint config, so it will go through and make those changes as well.

Don’t abandon your code! Instead, you can review the changes, see if maybe it makes sense to keep it that way (it will be very consistent) or you can update your ESLint config (`.eslintrc.js`) to overwrite the rules you don’t like. This is also a good way to maybe learn some new things that you might not have expected to get caught before.

## **So where does this leave us?**

If you’ve followed along so far, we now have two commands:

* `lint`: which will check your code for you and tell you what's wrong
* `format`: will automatically try to fix the problems for you

When using these in practice, your best bet is to always run `format` first to let it try to automatically fix anything it can. Then immediately run `lint` to catch anything Prettier wasn’t able to fix automatically.

## **What’s next?**

Now that we can format our code automatically, we should be able to fix our code automatically!

![Image](https://www.freecodecamp.org/news/content/images/2019/11/fresh-off-the-boat-mind-blown.gif)
_Eddie from Fresh Off the Boat's mind blown_

Next time we’ll take this a step further and set up a `git` hook that will allow this to run before you commit. This means you won't ever have to worry about forgetting to run this again!

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originally published at [https://www.colbyfayock.com/2019/11/dont-just-lint-your-code-fix-it-with-prettier/](https://www.colbyfayock.com/2019/11/dont-just-lint-your-code-fix-it-with-prettier/)_

