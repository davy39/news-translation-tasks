---
title: How to Add a "Skip to Main Content" Link to Your Website
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2022-07-20T16:30:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-skip-to-main-content-links-to-a-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/man-sitting-infront-of-conputer.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: best practices
  slug: best-practices
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Websites and web applications have increasingly become more complex. But
  it''s still our responsibility, as web developers, to strive for the highest level
  of accessibility we possibly can.

  This isn''t always easy, as the range of user accessibility ne...'
---

Websites and web applications have increasingly become more complex. But it's still our responsibility, as web developers, to strive for the highest level of accessibility we possibly can.

This isn't always easy, as the range of user accessibility needs can complicate things even further.

Thankfully, various guidelines exist for designing and building more accessible websites and web applications. This article will look at the seemingly mundane, lesser-known, and often overlooked web accessibility feature: the "skip to main content" link.

Because they are invisible by default, many users navigating a website using the usual point-and-click method won't even notice skip-to-main-content links. But these links are critical, as they make navigating complex and large websites simpler for keyboard-only and some screen reader users.

In the section below, we shall have a detailed look at "skip to main content" links and why you should consider implementing them in your website or web application.

## What are "Skip to Main Content" Links?

Most websites usually come with navigation menus to make navigation easier. But although they make your website or web application navigable for the point-and-click users, navigation menus can also cause a poor user experience for keyboard-only and some screen reader users.

It is not uncommon for a typical website to have a navigation menu with up to ten menu items at the top of each web page. So a keyboard-only user will needlessly tab through all the navigation links before accessing the main content on pages they visit.

Some screen reader users may undergo a similar experience by traversing all the menu items before reaching the main content.

This creates a negative experience for your users. Adding skip-to-content links can make navigating such complex sites easier and less laborious for keyboard-only and some screen reader users.

A "skip to content" link is an ordinary link, usually before the main navigation menu at the top, linking to the main content on the web page. Since a point-and-click user doesn't need it, a "skip to main content link" is usually hidden and made visible when it is in focus.

It helps keyboard-only and screen reader users skip to the main content instead of traversing all the menu items. And this greatly improves their browsing experience.

The image below shows the skip-to-main-content link for the [a11y project](https://www.a11yproject.com/). As mentioned above, the skip-to-main-content link is visible only after being focused on.

To test it, navigate to [a11yproject.com](https://www.a11yproject.com/) and hit the Tab key. The skip-to-main-content link immediately becomes visible. After that, you can hit the Enter key to skip the navigation menu.

![Skip to main content link on a11y project website](https://www.freecodecamp.org/news/content/images/2022/07/skip-to-main-content-link.png align="left")

*Skip to main content link on a11y project website*

In the next section, we shall implement a simple skip-to-main-content link.

## How to Add a Skip to Main Content Link to Your Site

Now that we know what "skip to main content" links are, let's look at how to implement them and some best practices when using them.

As already mentioned in the introduction, skip-to-main-content links are ordinary links.

But again, they are usually not visible to an ordinary point-and-click user. You can change the visibility of the skip-to-main-content link for the keyboard user when it is in focus.

The code below shows the markup for a typical navigation menu. A real-world application may be more complex with nested menu items in addition to the top-level menu items. But I have kept it simple in the example below.

```html
  <body>
    <a href="#main" class="skip-to-main-content-link">Skip to main content</a>
    <nav>
      <ul>
        <li>
          <a href="/">Home</a>
        </li>
        <li>
          <a href="/about.html">About</a>
        </li>
        <li>
          <a href="/blog.html">Blog</a>
        </li>
        <li>
          <a href="/contact.html">Contact</a>
        </li>
        <li>
          <a href="/portfolio.html">Portfolio</a>
        </li>
      </ul>
    </nav>
    <main id="main">
      <h1>Your sweet heading</h1>

      <!-- Page content goes here! -->
    </main>
  </body>
```

The first element of the `<body>` tag in the above example is the skip-to-main-content link. Its `href` attribute points to the `main` element via its `id` attribute. Clicking or pressing the Enter key when the skip-to-main-content link is in focus will scroll the main content into view in the viewport.

As pointed out in the previous section, the skip-to-main-content link is primarily for keyboard-only and some screen reader users. So we need to apply some styling to hide it from view when out of focus and display it when it receives focus.

So we select it using the given class and apply the styling below. You can hide and display the skip link with different styling. It doesn't have to be the same code as below.

```css
.skip-to-main-content-link {
  position: absolute;
  left: -9999px;
  z-index: 999;
  padding: 1em;
  background-color: black;
  color: white;
  opacity: 0;
}
.skip-to-main-content-link:focus {
  left: 50%;
  transform: translateX(-50%);
  opacity: 1;
}
```

You can also apply transition animation to your skip-to-main-content link, though I haven't included it in the example above.

## Good Practices When Adding a Skip to Main Content Link

Though skip-to-main-content links are easy to implement, there are some potential problems that can easily slip by you.

Follow what I consider good practices below when implementing skip-to-main-content links. I have picked them up from the [WCAG techniques](https://www.w3.org/TR/WCAG20-TECHS/G1.html).

* If the skip to main content link is for skipping the main navigation menu at the top of a web page, it should be the first focusable element on the web page.
    
* The text of the skip link should describe the intent. The text "Skip to main content" will usually suffice.
    
* It is a requirement that the skip-to-content link is either always visible or visible when in focus. Since our skip-to-content link is for keyboard-only and some screen reader users, you can hide it and make it visible as we did in the example above.
    
* The focus should shift to the main content after activating the skip link.
    

It is worth pointing out that using skip links is not only limited to navigation menus. You can also implement links to help users skip focusable elements that are difficult or laborious to navigate with the keyboard.

## Conclusion

A navigation menu is a handy feature for navigating to different sections or pages of a website. And although it's meant to provide a better user experience, a navigation menu can become an accessibility obstacle for some users who only use the keyboard or who use a screen reader.

This is why it's a good idea to add skip-to-main-content links on each page. When users need to traverse the navigation menu items, they can use that link to bypass the navigation menu.

The skip-to-main-content link is an ordinary link that's invisible to the point-and-click user. It is visible to screen reader users and when in focus. Clicking it will shift focus to the main content on the web page.

Hopefully, this article has given you insights on skip-to-main-content links and how to implement them in your website or web application.

Accessibility is a journey. Every step you take in the right direction makes your site or web application more accessible. Implementing skip-to-main-content links is one such step. Take that step and make the web more accessible if you haven't. By doing so, you are enriching the digital experience for your clients.
