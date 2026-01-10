---
title: How to Create Links in HTML – Tutorial with Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-02T07:59:34.000Z'
originalURL: https://freecodecamp.org/news/html-links-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/White-Soft-Brown-Professional-Elegant-Marketing-Strategy-Presentation-169.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: null
seo_desc: "Links are an essential part of the web because they connect web pages,\
  \ documents, and resources across the internet. \nIn HTML (which is short for Hypertext\
  \ Markup Language), links play a crucial role in creating a web of interconnected\
  \ content, allow..."
---

Links are an essential part of the web because they connect web pages, documents, and resources across the internet. 

In HTML (which is short for Hypertext Markup Language), links play a crucial role in creating a web of interconnected content, allowing users to navigate seamlessly between different web pages and websites. 

In this article, we will explore the fundamentals of links in HTML, including their types, attributes, and best practices.

## What Are Links in HTML?

In HTML, a link, also known as a hyperlink, is an element that lets users navigate from one web page to another. They also allow users to navigate to external resources such as documents, images, videos, and more.

HTML offers several types of links, each serving a specific purpose. Let's see some of them in action in the following sections.

### How to create text links

Text links are the most common type of links. They are created by wrapping text with an anchor (`<a>`) element. When users click on the linked text, they are directed to the URL specified in the link's `href` attribute:

```html
<a href="https://www.example.com">Visit Example.com</a>

```

Text links are versatile and can be used for various purposes, such as linking to other web pages, external websites, or even specific sections within a page using anchor tags.

### How to create image links

You can turn images into clickable links by wrapping them in an anchor element. This is useful for creating an image-based navigation or linking to larger versions of images:

```html
<a href="https://www.example.com">
  <img src="image.jpg" alt="Example Image">
</a>

```

Image links are visually engaging and are often used for elements like logos, banners, or thumbnail images that, when clicked, lead users to a related web page or resource.

### How to create email links

To create links that open an email client with a pre-filled recipient address, use the `mailto` scheme:

```html
<a href="mailto:contact@example.com">Send an Email</a>

```

Email links are convenient for enabling users to initiate email communication with a simple click. They are commonly used for contact information on websites.

### How to create external links

External links point to resources on other websites. It's essential to indicate that a link is external by using the `target="_blank"` attribute to open the linked page in a new browser tab or window. This ensures that your website remains open in the user's current tab while the linked content appears in a separate tab or window:

```html
<a href="https://www.external-site.com" target="_blank">Visit External Site</a>

```

External links are a way to provide additional resources, references, or sources to your content while allowing users to return to your site easily.

### How to create internal links

Internal links are used to navigate within the same website. They typically reference other pages within the site using relative URLs:

```html
<a href="/about">Learn More About Us</a>

```

Internal links are essential for site navigation, helping users find related content or move between different sections of your website.

## Link Attributes Explained

To create functional and user-friendly links, it's crucial to understand the key attributes that can be used with anchor (`<a>`) elements.

### How to use the `href` attribute

The `href` attribute specifies the destination URL or resource that the link points to. It can be an absolute URL (starting with "http://" or "https://") or a relative URL (relative to the current page).

Here is how you create absolute URLs:

```html
<a href="https://www.example.com">Visit Example.com</a>

```

And here is how you create relative URLs:

```html
<a href="/about">Learn More About Us</a>

```

Using relative URLs is often preferred when linking within the same website because it makes your links more adaptable to changes in the domain structure.

### How to use the `target` attribute

The `target` attribute defines how the linked resource should be displayed when clicked. Common values include:

* `_self` (default): Opens the link in the same browser tab or window.
* `_blank`: Opens the link in a new browser tab or window.
* `_parent`: Opens the link in the parent frame or window.
* `_top`: Opens the link in the full body of the window, replacing any frames.

```html
<a href="https://www.external-site.com" target="_blank">Visit External Site</a>

```

The use of the `_blank` target is common for external links to prevent users from navigating away from your site entirely.

### How to use the `rel` attribute

The `rel` attribute specifies the relationship between the current document and the linked resource. For example, `rel="noopener"` is often used for security reasons when opening links in a new tab:

```html
<a href="https://www.example.com" rel="noopener">Visit Example.com</a>

```

The `noopener` value helps protect against potential security vulnerabilities associated with opening new tabs or windows.

## HTML Link Best Practices

To ensure an excellent user experience and maintain web accessibility and SEO (Search Engine Optimization) standards, you can follow certain best practices when working with links in HTML.

### Use descriptive text

The text used for link anchors should be descriptive and convey the purpose of the link to users. Avoid generic phrases like "click here."

Not Recommended: `<a href="https://www.example.com">Click here</a>`

Recommended: `<a href="https://www.example.com">Visit Example.com</a>`

Descriptive link text improves the user experience and helps users understand where the link will take them.

### Provide context

When linking to external resources, consider adding a brief description or title attribute to inform users about the linked content:

```html
<a href="https://www.example.com" title="Visit Example.com">Example.com</a>

```

Providing context enhances usability and accessibility, especially for users with disabilities who rely on assistive technologies.

### Test links

Regularly test all links on your website to ensure they are working correctly. Broken links can frustrate users and harm your website's reputation.

Consider using automated link-checking tools to scan your site for broken links and address them promptly.

### Optimize for accessibility

Use semantic HTML and provide alt text for images within links to make your content accessible to users with disabilities.

```html
<a href="/about">
  <img src="about-image.jpg" alt="About Us">
</a>

```

Accessible links ensure that all users, regardless of their abilities, can navigate and interact with your content.

### Consider SEO

When linking to internal pages, use meaningful anchor text that includes relevant keywords. This can improve your website's search engine ranking.

Not recommended: `<a href="/product123">Click here for more info</a>`

Recommended: `<a href="/product123">Learn more about Product XYZ</a>`

Keyword-rich anchor text helps search engines understand the content and context of your links, which can boost your site's visibility in search results.

### Use relative URLs

When linking within your own website, prefer relative URLs over absolute ones. This makes your website more maintainable and adaptable to changes in the domain structure.

```html
<a href="/about">Learn More About Us</a>

```

Relative URLs are less prone to breaking when you make changes to your website's structure or migrate it to a different domain.

### Use external link indicators

When linking to external websites, make it clear to users that they are leaving your site. This can help build trust and transparency.

Consider using an icon or text such as "External Link" next to external links to provide this indication.

## Conclusion

In conclusion, links are the backbone of the web, enabling seamless navigation and exploration of online content. By understanding the types of links available in HTML, their attributes, and best practices for their usage, you can create a user-friendly and accessible web experience while enhancing your website's visibility and credibility on the internet.

With proper link usage, you can connect your audience with valuable resources, provide a smooth user experience, and contribute to the overall success of your website.

