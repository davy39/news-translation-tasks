---
title: The HTML a href Attribute Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/the-a-href-attribute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d6a740569d1a4ca37a6.jpg
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: "The <a href> attribute refers to a destination provided by a link. The\
  \ a (anchor) tag is dead without the <href> attribute. \nHow to use the  tag\nSometimes\
  \ in your workflow, you don’t want a live link or you won’t know the link destination\
  \ yet. In thi..."
---

The `<a href>` attribute refers to a destination provided by a link. The `a` (anchor) tag is dead without the `<href>` attribute. 

## How to use the <a href> tag

Sometimes in your workflow, you don’t want a live link or you won’t know the link destination yet. In this case, it’s useful to set the `href` attribute to `"#"` to create a dead link. 

The `href` attribute can be used to link to local files or files on the internet.

For instance:

```html
<html>
  <head>
    <title>Href Attribute Example</title>
  </head>
  <body>
    <h1>Href Attribute Example</h1>
      <p>
        <a href="https://www.freecodecamp.org/contribute/">The freeCodeCamp Contribution Page</a> shows you how and where you can contribute to freeCodeCamp's community and growth.
      </p>
    </h1>
  </body>
</html>
```

The `<a href>` attribute is supported by all browsers.

## More HTML attributes:

`hreflang` : Specifies the language of the linked resource. 

`target` : Specifies the context in which the linked resource will open. 

`title` : Defines the title of a link, which appears to the user as a tooltip.

### **Examples**

```html
<a href="#">This is a dead link</a>
<a href="https://www.freecodecamp.org">This is a live link to freeCodeCamp</a>
<a href="https://html.com/attributes/a-href/">more with a href attribute</a>
```

### **In-page anchors**

It’s also possible to set an anchor to certain place of the page. To do this you should first place a tab at location on the page with tag and necessary attribute “name” with any keyword description in it, like this:

```html
<a name="top"></a>
```

Any description between tags is not required. After that you can place a link leading to this anchor at any palce on same page. To do this you should use tag with necessary attribute “href” with symbol # (sharp) and key-word description of the anchor, like this:

```html
<a href="#top">Go to Top</a>
```

### **Image Links**

The `<a href="#">` may also be applied to images and other HTML elements.

### **Example**

```html
<a href="#"><img itemprop="image" style="height: 90px;" src="http://www.chatbot.chat/assets/images/header-bg_y.jpg" alt="picture">  </a>
```

### **Some more examples of href**

```html
<base href="https://www.freecodecamp.org/a-href/">This gives a base url for all further urls on the page</a>
<link href="style.css">This is a live link to an external stylesheet</a>
```

## What else can you do with <a href>? 

More customization! Let's see a specific use case:

A mailto link is a kind of hyperlink (`<a href=""></a>`) with special parameters that lets you specify additional recipients, a subject line, and/or a body text.

### **The basic syntax with a recipient is:**

```html
<a href="mailto:friend@something.com">Some text</a>
```

### Adding a subject to that mail:

If you want to add a specific subject to that mail, be careful to add `%20` or `+` everywhere there’s a space in the subject line. An easy way to ensure that it is properly formatted is to use a [URL Decoder / Encoder](https://meyerweb.com/eric/tools/dencoder/).

### Adding body text:

Similarly, you can add a specific message in the body portion of the email: Again, spaces have to be replaced by `%20` or `+`. After the subject paramater, any additional parameter must be preceded by `&`

Example: Say you want users to send an email to their friends about their progress at Free Code Camp:

Address: empty

Subject: Great news

Body: I am becoming a developer

Your html link now:

```html
<a href="mailto:?subject=Great%20news&body=I%20am%20becoming%20a%20developer">Send mail!</a>
```

Here, we’ve left mailto empty (mailto:?). This will open the user’s email client and the user will add the recipient address themselves.

### Adding more recipients:

In the same manner, you can add CC and bcc parameters. Seperate each address by a comma!

Additional parameters must be preceded by `&`.

```html
<a href="mailto:firstfriend@something.com?subject=Great%20news&cc=secondfriend@something.com,thirdfriend@something.com&bcc=fourthfriend@something.com">Send mail!</a>
```

#### **More Information:**

[MDN - E-mail links](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#E-mail_links)

