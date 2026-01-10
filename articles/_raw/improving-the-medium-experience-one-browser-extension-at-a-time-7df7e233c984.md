---
title: Improving the Medium Experience
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T09:45:06.000Z'
originalURL: https://freecodecamp.org/news/improving-the-medium-experience-one-browser-extension-at-a-time-7df7e233c984
coverImage: https://cdn-media-1.freecodecamp.org/images/0*x-bORZmgzqDVzW-g.
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By cedric amaya

  One browser extension at a time.


  _Photo by [Unsplash](https://unsplash.com/@barnimages?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Barn Images on <a href="https://unsplash.com?utm_source=medium&utm_...'
---

By cedric amaya

#### One browser extension at a time.

![Image](https://cdn-media-1.freecodecamp.org/images/5ykRlwzkzFJzHOky-2arac3AWBNCySxbrPAD)
_Photo by [Unsplash](https://unsplash.com/@barnimages?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Barn Images</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

I love Medium. As a consumer, it has provided me with countless articles that have helped me to better myself both personally and professionally. And as a producer, it has provided me a platform on which I can express myself as genuinely as possible through the written word.

Since using Medium, however, I have noticed some things about the publishing platform that I either found lacking or that have room for improvement. And as a web developer and tinkerer, I like to come up with the solutions for these problems myself. Here are a couple extensions I created to make your Medium experience even better.

### Medium Bookmarklets ?

The first occasion of me trying to improve the Medium experience was with my Firefox WebExtension, [Medium Bookmarklets](https://medium-bookmarklets.com/) (which, I found out after naming the product, aren’t actually bookmarklets).

This aimed to bring true bookmarking functionality, in the sense that you could save your spot in an article for later without the need to remember or scroll to that section. This solved a problem I constantly faced and thought others might as well.

#### How it Works

Since I knew that HTML elements in Medium articles contain a unique `id` attribute, I developed a solution that added a marker / highlighter on the selected element. This would correspond to a paragraph, heading, or quote in the article where the user wanted to save their spot which in turn saved that element’s `id`.

Navigating directly to that spot in the article is performed by using a fragment identifier of the saved `id`. For example, if this paragraph had an `id` of “3b75”, then to open this article with this specific paragraph at the top of the page, the URL would look something like `https://blog.cedricamaya.me/improving-medium-experience-7df7e233c678**#3b75**` **.** Note the fragment identifier (`#3b75`) at the end.

This same functionality is usually used by writers / editors to include a table of contents in their articles on Medium. [Here’s a great explanation and how-to guide that goes more into detail.](https://medium.freecodecamp.org/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549)

With that functionality in mind, I coded a Firefox add-on that created a sidebar of clickable cards which represented the user’s saved _bookmarklets,_ as I called them. The click event handler on each card would navigate the current page to the _bookmarklet’s_ URL. So if you placed a _bookmarklet_ halfway in a long article, the need to scroll to that section where you last left off was completely eliminated.

![Image](https://cdn-media-1.freecodecamp.org/images/zBx9xbR2vlqxbauf-L4tmKI7yLpTkrqgf5d-)
_Promo image showcasing the Medium Bookmarklets sidebar and a bookmarklet highlight in an article._

There is more functionality included in Medium Bookmarklets, such as the need to whitelist the publications you’d like to save _bookmarklets_ from (due to security reasons), as well as notifications when a _bookmarklet_ it added or deleted. Other than that, it’s a pretty simple extension that aims to improve your bookmarking capabilities.

_Check out [**Medium Bookmarklets**](https://addons.mozilla.org/en-US/firefox/addon/medium-bookmarklets/) from Mozilla Addons._

### Signature ✍️

If Medium Bookmarklets was developed with the consumers of Medium in mind, then [Signature](https://chrome.google.com/webstore/detail/signature/hgabbjfneihcmbbcnbnfdnfdcbpodnhp) was developed for those creating content on Medium.

Signature’s purpose is simple: provide writers and editors the ability to instantly add their blog’s signature / sign off with the click of a button—eliminating the need to copy and paste or retype it every time.

The idea for Signature originated after coming across numerous articles in a specific publication that all ended with the same text / copy. It was usually a call-to-action with hyperlinks, and was styled using bold or italicized text to make it stand out.

I thought to myself, “do people type that signature or copy and paste it from a previous article every time they’re writing a new blog post?” Regardless, retyping or copying and pasting takes time, and wanting to simplify the process, I developed another browser extension (this time for both Chrome and Firefox) to solve this problem.

#### How it Works

With Signature installed, users simply fill out their blog’s signature in the editor found in the extension’s settings page. This editor, an instance of [Quill](https://quilljs.com/), is a rich text editor, meaning any formatting of text (i.e. bold, italics, quote, heading, code, and so on) can easily be transferred and applied to a Medium blog post draft, which also utilizes rich text capability.

Once a signature has been defined in the settings page, users will then be able to click the “signature” button (with the nib icon) located in the inline-tooltip, as shown below. Clicking that button then pastes the signature that was defined in the settings page in the draft.

![Image](https://cdn-media-1.freecodecamp.org/images/h8kqbC09qw8J2Bu96z0DXb5rcC8wwEniR1sK)
_“Signature” button, on the far right._

Enough talking about how it works, though — let’s see it in action!

![Image](https://cdn-media-1.freecodecamp.org/images/R48SQUC-Qy8E5kJOQFanlP2zVzDYhvN8diZ5)
_Signature added in settings page, then “signature” button used to add signature in Medium draft._

_Check out **Signature** from [Mozilla Addons](https://addons.mozilla.org/en-US/firefox/addon/medium-signature/) and from the [Chrome Webstore](https://chrome.google.com/webstore/detail/signature/hgabbjfneihcmbbcnbnfdnfdcbpodnhp)._

#### Takeaways

Like all products out there, Medium has its flaws. However, with the creative use of your imagination and a do-it-yourself attitude, you can greatly improve these issues with a little programming.

I now encourage _you_ to improve the Medium experience in your own way and share the result using #MediumExperience. If you can’t think of your own idea or are just getting started with programming, feel free to implement a new feature or fix a bug in either Medium Bookmarklets or Signature — both are open-source and can be found on GitHub.

[**cedricium/medium-bookmarklets**](https://github.com/cedricium/medium-bookmarklets)  
[_? medium-bookmarklets - Easy way to save your place in Medium articles and return to them later.g_ithub.com](https://github.com/cedricium/medium-bookmarklets) [**cedricium/signature**](https://github.com/cedricium/signature)  
[_✍️ Signature - Medium signatures, simplified._github.com](https://github.com/cedricium/signature)

Thanks for reading and I look forward to seeing how you choose to improve the Medium experience!

**~ cedric amaya**  
? wielder who loves to create things with code  
G[itHub](https://github.com/cedricium) | L[inkedIn](https://www.linkedin.com/in/cedricamaya) | T[witter](https://twitter.com/cedricamaya)

