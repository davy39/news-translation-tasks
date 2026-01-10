---
title: What is Tabnabbing and How to Prevent it
subtitle: ''
author: Juanita Washington
co_authors: []
series: null
date: '2023-10-16T22:56:14.000Z'
originalURL: https://freecodecamp.org/news/what-is-tabnabbing
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Tab-pg-6.png
tags:
- name: HTML
  slug: html
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'Sometimes when you''re building a website, you may need a link to open
  in a new tab. What you might not realize, though, is that doing so could leave your
  users vulnerable to malicious attacks via a practice called "tabnabbing".

  And while nothing is f...'
---

Sometimes when you're building a website, you may need a link to open in a new tab. What you might not realize, though, is that doing so could leave your users vulnerable to malicious attacks via a practice called "tabnabbing".

And while nothing is foolproof, there is a way to at least mitigate the effects: using the `noopener` and `noreferrer` attributes. And that's what you'll learn about in this quick tutorial.

## What is Tabnabbing?

Tabnabbing is a type of phishing attack that targets the inactive tabs in your browser. While you're focused on your current tab, the link to the previous one can be hijacked, and you'll be redirected from the intended site to a malicious one resembling the real thing.

Since the malicious site looks very similar to the original, the user is typically unaware that the page they're on isn't legit once they return to that tab. Because of this, the user puts in their personal information, not knowing someone's on the other side waiting to steal it.

Some ways attackers might compromise a well-known website include:

* malicious ads
    
* 3rd party widgets that the website has included, which were later compromised
    
* malicious user-generated content (like forum posts) that contain unsanitized JavaScript
    

### A Quick Example of Tabnabbing

Think of how a website with your personal details logs you out automatically when you're inactive for too long. Since that means your attention's elsewhere, the attacker can switch out the real page for a very convincing fake.

When you go back to that tab, you wouldn't know the difference, so you log back in, and the phisher now has access to your private details.

As is the case for phishing attacks, the purpose of this action is to deceive the unsuspecting user into entering sensitive information (usually login or financial info) on the phony site.

This is, of course, a problem you'll want to avoid for your site when visitors come! You'll want to make sure people are safe when clicking any of your links, right?

So now you're going to learn how to make your corner of the internet a little bit safer—starting with learning how to open a new tab to begin with.

## How to Open a Link in a New Tab in HTML

To open a link in a new tab, write out a link how you would in HTML, then just add the target attribute, setting the value to blank, like this: `target="_blank"`:

```html
<p>Learn to code for free at <a href ="https://www.freecodecamp.org/" target="_blank">freeCodeCamp.org!</a><p/>
```

On the page, it would look like this:

Learn to code for free at [freeCodeCamp.org!](https://www.freecodecamp.org/)

## How to Add a `Noopener`/`Noreferrer` Attribute

Unfortunately, the more tabs you have open (who doesn't multitask on their browser?), the more susceptible you are to tabnabbing. This is because the longer a tab stays inactive, the higher the chance a phisher can strike, swapping the real page with a fake.

So, how do you prevent this? By adding `rel="noopener noreferrer"` to your anchor, like this:

```html
<p>Learn to code for free at <a href ="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp.org!</a><p/>
```

### Why use `noopener` and `noreferrer`?

Using `noopener` prevents bad actors and links from accessing the previous tab or window that opened the current one. This is done by setting the `Window.opener()` property to null.

Adding `noreferrer` prevents external sites from knowing that you've linked to them, which means your traffic data won't be sent their way.

## Wrapping Up

You should now have an understanding of what tabnabbing is and how protect your links (and users) against it. Hope you found this helpful and best of luck to you!

If you have indeed found this helpful, I have more tech articles on my [blog](https://jwashingtondev.hashnode.dev/). If you want to connect, I'm on [linkedin](https://www.linkedin.com/in/juanita-washington-freelance-writer-web-developer-saas-tech/)!

If you want to read more about all this, here are some resources:

1. [EASYDMARC - What is Tabnabbing and how it works](https://easydmarc.com/blog/what-is-tabnabbing-and-how-it-works/)
    
2. [Elegant Themes - What is the "noopener noreferrer" tag and what does it mean?](https://www.elegantthemes.com/blog/wordpress/rel-noopener-noreferrer-nofollow)
    
3. [MDN - the Window.opener() property](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
