---
title: How to Create a Contact Form with Netlify Forms and Next.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-26T17:13:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-contact-form-with-netlify-forms-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/netlify-forms.jpg
tags:
- name: Netlify
  slug: netlify
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: null
seo_desc: "If you want someone to be able to contact you or submit information on\
  \ a website, an HTML form is a pretty standard way to achieve that. \nBut accepting\
  \ form submissions usually requires an additional service or complex server-side\
  \ code. How can we ta..."
---

If you want someone to be able to contact you or submit information on a website, an HTML form is a pretty standard way to achieve that. 

But accepting form submissions usually requires an additional service or complex server-side code. How can we take advantage of Netlify to easily create new forms?

* [What is Netlify?](#heading-what-is-netlify)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [How much does this cost?](#heading-how-much-does-this-cost)
* [Part 1: Creating a contact form with HTML](#heading-part-1-creating-a-contact-form-with-html)
* [Part 2: Adding a custom Netlify form to a Next.js React app](#heading-part-2-adding-a-custom-netlify-form-to-a-nextjs-react-app)

%[https://www.youtube.com/watch?v=GLxgxnLTVLE]

## What is Netlify?

[Netlify](https://www.netlify.com/) is a web platform that lets you easily deploy new web projects with easy to configure workflows. This includes deploying a static website, lambda functions, and like we’ll talk about here, custom forms.

Their form service works as part of the build and deployment pipeline. When we include a form with a specific attribute to our page, Netlify will recognize that form and configure it to work.

## What are we going to build?

We’re going to build a contact form that will allow people to send you a note through your website.

The form itself will be pretty simple. Like a standard contact form, we'll ask for someone's name, email address, and a message.

We’re going to build this out using plain HTML to demonstrate how it works and then build it with [Next.js](https://nextjs.org/) for creating a form in a React app.

## How much does this cost?

Netlify forms are free to get started. This free tier is limited to 100 form submissions per website per month, so if you stay under that, it will always be free.

That said, if you exceed 100 form submission on any particular site, the first tier is going to be $19+ at the time of writing this. You can check out the [latest pricing plans on Netlify’s website](https://www.netlify.com/pricing/).

## Part 1: Creating a contact form with HTML

To get started, we’re going to create a basic form with pure HTML. It’s a quick win to demonstrate how this works.

### Step 1: Creating an HTML form

For our form, we can really use whatever we want. Contact forms can be as simple as an email address and a message field or it include a variety of options to help a business answer specific questions.

We’re going to start with something simple. We’ll create a form that asks for someone’s name, email address, and a message.

To get started, create a new HTML file in the root of your project. This HTML file should include the basic structure of an HTML document. Inside of the body, let’s add our new form:

```html
<form name="contact" method="POST" data-netlify="true">
    <p>
      <label for="name">Name</label>
      <input type="text" id="name" name="name" />
    </p>
    <p>
      <label for="email">Email</label>
      <input type="text" id="email" name="email" />
    </p>
    <p>
      <label for="message">Message</label>
      <textarea id="message" name="message"></textarea>
    </p>
    <p>
      <button type="submit">Send</button>
    </p>
  </form>

```

In the snippet above, we’re:

* Creating a new form
* The form has a name attribute, a method, and a `data-netlify` attribute set to `true`
* Creating 3 form fields with labels, each identified with a name attribute
* Creating a button to submit the form

The thing we want to take most notice of is the `data-netlify` attribute and the form `name`. When Netlify reads the site, it will see those fields and use those to turn your form into an actively working form.

I’m also going to add a little bit of CSS to make the labels look a little more consistent. You can optionally add this to the `<head>` of the document:

```html
<style>
  body {
    font-family: sans-serif;
  }
  label {
    display: block;
    margin-bottom: .2em;
  }
</style>

```

And at this point, we should have a basic form!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/basic-html-form-1.jpg)
_Basic HTML form_

You’ll now want to put this form on GitHub or your favorite Netlify-supported Git provider and we’ll be ready for the next step.

[Follow along with the commit!](https://github.com/colbyfayock/my-html-netlify-form/commit/482a4e14b3c8e10bc9ae29c2f233c3312dd1b89a)

### Step 2: Configuring a new form with Netlify

Once our form is pushed to our Git provider, we can now sync it up with Netlify.

First create an account or use an existing account with Netlify and click the **New site from Git** button.

Here, select whichever Git provider you used. I'm using **GitHub** in my example.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-connect-git-provider.jpg)
_Connecting a Git provider in Netlify_

Once selecting your Git provider, it will ask you to authorize access so that Netlify can find your Git repository.

After you successfully connect your account, you should now see a list of the repositories you provided access to. Find the repository you added your form to and select it.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/connecting-git-repo-netlify.jpg)
_Connecting a Git repository to Netlify_

If you’re following along with me, our form is pure HTML, meaning, there should be no build steps or no special directory it gets published to. But feel free to tweak these settings if you did something different.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/configuring-build-steps-netlify.jpg)
_Configuring the build steps in Netlify_

Now, click **Deploy site** which will open up a new page in Netlify and in no time your site will be successfully deployed.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-site-successfully-deployed.jpg)

Finally, click the URL at the top of the Netlify project dashboard that ends in netlify.app. Once it's loaded, you’ll see your form!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/html-form-netlify.jpg)

### Step 3: Viewing form submissions

Now that we have our form, we ultimately want to see responses.

To get started, add some information to your form and click submit.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-html-form.jpg)
_Testing HTML form_

Once you submit, you’ll notice you get taken to a Netlify page that says the form was successfully submitted.

You can now go back to your Netlify project dashboard and scroll down a little bit where you can now see a box with **Recent form submissions** as well as your new submission.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-form-submission.jpg)
_Netlify Form submission_

## Part 2: Adding a custom Netlify form to a Next.js React app

If the form is going to live by itself and not be part of a bigger site, there are a lot of advantages to leaving your form as pure HTML. But often, we want our contact form to be part of our website or app.

Here we’ll walk through adding a form to a [Next.js](https://nextjs.org/) app.

_Note: our demo of using Next.js is a statically rendered app. If you’re loading your form client side, meaning the underlying HTML doesn’t include the form, check out the notes at the bottom of this page for more information on solutions._

### Step 0: Creating a Next.js app

To start off, we need an app. We’re going to use Next.js since we can pretty easily spin up a new app from scratch.

To do this, you can navigate to where you want to create the app and run:

```
yarn create next-app [project-name]
# or
npx create-next-app [project-name]

```

I’m going to name my project `my-nextjs-netlify-form`.

Once Next.js finishes installing dependencies, it’ll give you instructions to navigate to your project directory and start your development server.

And after you run `yarn dev` or `npm run dev`, you should be ready to go with your Next.js app:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-1.jpg)
_New Next.js app_

[Follow along with the commit!](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/6f9fb6966b6c112a3ec934e305f2dd115e9d424e)

### Step 1: Adding an HTML form to a Next.js app

Our Step 1 is going to look very similar to Part 1.

Inside of `pages/index.js`, we want to find our grid wrapper and we’ll use that to add our form.

Find `<div className={styles.grid}>` and replace the entire block with the following:

```jsx
<div className={styles.grid}>
  <div className={styles.card}>
    <form name="contact" method="POST" data-netlify="true">
      <p>
        <label htmlFor="name">Name</label>
        <input type="text" id="name" name="name" />
      </p>
      <p>
        <label htmlFor="email">Email</label>
        <input type="text" id="email" name="email" />
      </p>
      <p>
        <label htmlFor="message">Message</label>
        <textarea id="message" name="message"></textarea>
      </p>
      <p>
        <button type="submit">Send</button>
      </p>
    </form>
  </div>
</div>

```

Here’s what we’re doing:

* We’re taking advantage of the existing grid from Next.js
* We’re also taking advantage of the existing card that we’ll include our form in
* Inside of the card, we’re pasting in the exact same HTML form as Part 1

If we reload the page, we can now see our form inside of a card, like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/form-nextjs-react-app.jpg)
_Adding a form to a Next.js app_

Now before we move on, we want to do 2 things.

First, because we’re creating this form in a JavaScript app, [Netlify recommends](https://www.netlify.com/blog/2017/07/20/how-to-integrate-netlifys-form-handling-in-a-react-app/#form-handling-with-static-site-generators) that we add a hidden input with our form name.

Inside of our form, add the following input at the top of the form element:

```
<input type="hidden" name="form-name" value="contact" />

```

Make sure the value of that input is the same as your form’s name.

Second, because the card that we’re reusing is intended for a list of links, Next.js includes some hover effects. This makes the form confusing to use, so let’s remove those

Remove the following from `styles/Home.module.css`:

```
.card:hover,
.card:focus,
.card:active {
  color: #0070f3;
  border-color: #0070f3;
}

```

For an extra bonus step, I’m going to update my page title to “Contact Me” and remove the description. Feel free to make this whatever you want.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-contact-form-title.jpg)
_Updating the form title_

And once you’re ready, similar to before, add this as a new repository to GitHub or your favorite Git provider.

[Follow along with the commit!](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/b9cac11411c6c71ee648c8631c35740735c599b7)

### Step 2: Setting up and deploying your Next.js app to Netlify

Deploying our app to Netlify will look pretty similar, but before we get there, we need to set up our Next.js app to be able to export on build.

In our Next.js app, inside of the `package.json` file, we want to update the `build` script to:

```json
"build": "next build && next export",

```

Now when you run the `build` script, it will compile the app to static HTML, CSS, and JS inside of the `out` directory. This will let us deploy it to Netlify. You can even try it locally on your machine if you want.

With that change, commit that and push it out to your Git provider.

Next, deploying the app will mostly look similar to Part 1. The only difference is because we have a Next.js app, we need to add our build steps.

To get started, we’ll want to connect our Git provider just like in Part 1.

Once we get to the Deploy Settings page, we want to configure our Build command and our Publish directory.

Our **Build command** will be `yarn build` or `npm run build` depending on what package manager you used and the **Publish directory** will be `out`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-deploy-settings-nextjs-app.jpg)
_Deploy settings for a static Next.js app_

After that, click **Deploy site**, and it will kick off just like before.

Once it’s finished deploying, we’ll now be ready to open the app.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/successfully-deployed-nextjs-app-netlify.jpg)
_Successfully deployed Next.js app on Netlify_

And once we open up our app we can test our form by filling it out and hitting submit.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-nextjs-contact-form.jpg)

Similar to before, we’ll land on a Netlify success page. But if we go back and look inside of our Netlify dashboard, we’ll now see our submission!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/successful-nextjs-form-submission-netlify-form.jpg)
_Succesful Next.js form submission on Netlify_

[Follow along with the commit!](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/3a4516a706af550a37372a9aa2bbaf54b9d7d691)

### Bonus: Keep people on your website with a success message

Another cool feature with Netlify forms is that it allows you to set up your form to keep people on your website by configuring the form right on the page.

You have a lot of options here, whether it’s redirecting someone to a new page or configuring messaging on the page they submitted from.

For this demo, we’re going to set up a URL parameter that we can detect to show a success message if we see that parameter.

To do this, on your HTML form, add the following attribute:

```
action="/?success=true"

```

This will tell Netlify we want to stay on the homepage (since we only have one page) but apply the URL parameter so we can detect it in our app.

Next, we can use the `useState` and `useEffect` hooks to see this parameter and update the page.

At the top of the file, let’s import these hooks:

```
import { useState, useEffect } from 'react';

```

Inside of our Home component at the top, let’s add our state:

```
const [success, setSuccess] = useState(false);

```

And to detect the URL parameter, we can use the `useEffect` hook:

```jsx
useEffect(() => {
  if ( window.location.search.includes('success=true') ) {
    setSuccess(true);
  }
}, []);

```

_Note: this is a simple way of achieving this result for the demo. If you have a more complicated app, you might want to name the parameter something more logical and properly parse the URL parameters for the value._

What this is doing, is when the component renders, it will fire this `useEffect` hook, checking the parameters in the URL, and looking for `success=true`. If it finds it, it will update our `success` state variable to `true`!

Next, under our page title (`<h1>`), let’s add the following snippet:

```jsx
{success && (
  <p style={{ color: 'green'}}>
    Successfully submitted form!
  </p>
)}

```

Here we’re looking to see if `success` is true, and if it its, we include a line of text that says the form was successfully submitted.

While you can’t submit your form locally, you can test this out by visiting your app running locally with the `?success=true` URL parameter like:

```
http://localhost:3000/?success=true

```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-success-message-locally.jpg)
_Testing success message locally_

Finally, you can push these changes out to your Git provider and Netlify will automatically rebuild your site.

And once it’s finished, you can submit your form like before and see the success message.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-success-redirect.jpg)
_Successful form redirect on Netlify_

And see that our form is still submitting!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/form-submission-success-netlify.jpg)
_Successful form submission on Netlify_

[Follow along with the commit!](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/25378cd6b17ad6bb48dc7281220ab48eba74f478)

## Netlify forms and client-side code

One thing to take note of with Netlify’s solution is this only works this “simply” for static HTML pages. 

If your page uses JavaScript to manage the content of that page, such as not adding a form until after the page loads, you’ll need to check out Netlify’s documentation on how you can make this work [with an additional form attribute](https://docs.netlify.com/forms/setup/#javascript-forms).

Netlify also gives an example on how you can [submit your form dynamically with JavaScript](https://docs.netlify.com/forms/setup/#submit-forms-via-ajax) so you can create a custom experience in your app.

## What else can you do?

### Setting up advanced workflows with other tools

Netlify lets you integrate with other tools to allow you to wrangle your form submissions. Notably, [Netlify works with Zapier](https://zapier.com/apps/netlify/integrations), meaning you can accept incoming submissions and do whatever you want with them.

[https://docs.netlify.com/forms/notifications/](https://docs.netlify.com/forms/notifications/)

### Preventing spam with reCAPTCHA

Spam is also a real thing. You don’t want your inbox flooded with spam, so you can take advantage of Netlify’s built-in Honeypot field or they walk you through how to add reCAPTCHA 2.

[https://docs.netlify.com/forms/spam-filters/](https://docs.netlify.com/forms/spam-filters/)

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>

