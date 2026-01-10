---
title: Web Accessibility – Best Practices and a Checklist for Developers
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2022-11-30T18:40:47.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-best-practices-and-checklist
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/WebAccessibility.png
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "The World Health Organization reports that about 15% (1.2 billion) of the\
  \ world's population lives with some form of disability. \nThis means that as developers,\
  \ our focus on making websites and applications accessible helps more people use\
  \ these reso..."
---

The World Health Organization [reports](https://www.who.int/teams/noncommunicable-diseases/sensory-functions-disability-and-rehabilitation/world-report-on-disability) that about **15% (1.2 billion)** of the world's population lives with some form of disability. 

This means that as developers, our focus on making websites and applications accessible helps more people use these resources. 

In this article, I'll point out barriers to web accessibility, discuss the Web Content Accessibility Guidelines (WCAG), and share a basic checklist that all developers can use when building their websites and applications.

> “_The power of the Web is in its universality. Access by everyone regardless of disability is an essential aspect_.” – Tim Berners-Lee, W3C Director and inventor of the World Wide Web.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/a11y.png)
_Image credit: [Interactive Schools](https://blog.interactiveschools.com/)_

## What is Web Accessibility?

A person is said to be disabled when they’re faced with a condition – permanent or temporary – that makes it difficult or impossible for them to achieve a desired task. 

In effect, web accessibility involves removing all barriers that prevent any users from accessing the web equally.

## What are the Barriers to Accessibility?

The barriers to accessibility include **visual, auditory, cognitive** and **motor**. 

Visual barriers constitute conditions which make it difficult for people to view images, videos, and gifs. These conditions can include low vision, colour blindness, or even total vision loss. 

Auditory barriers constitute conditions which make it difficult or impossible for people to consume audio content. 

Those who have difficulty concentrating, learning or remembering new things are faced with cognitive barriers. 

And people who have partial or total loss of function in a body part and find it difficult to navigate websites using devices such as a mouse experience motor barriers.

To resolve these barriers of web or digital accessibility, the Web Accessibility Initiative (WAI) of World Wide Consortium (W3C) created the **Web Content Accessibility Guidelines** (WCAG). 

## What are Web Content Accessibility Guidelines? 

They are globally accepted standards that guide developers and organisations in building an accessible web.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/pour-accessibility.png)
_Image credit: [Site Improve](https://www.siteimprove.com/)_

Most of the barriers to web accessibility faced by people with disabilities can be put into four categories. The WCAG addresses each category to ensure accessibility is achieved.

**Perceivable:** It requires that users can identify content and interface elements using their senses. Most users rely primarily on visual senses, while others rely on sound.

**Operable:** It requires that users can use controls, buttons, navigation, and other interactive elements by themselves. It takes into consideration that disabled users will use assistive technology like voice recognition, keyboards, screen readers, and so on.

**Understandable:** It requires that users can comprehend the content and learn and remember how to use your site. The site should have a consistent format, predictable design and usage patterns, as well as an appropriate tone.

**Robust:** It requires that users of varying abilities and conditions can reliably interpret and interact with content using a technology or device of their choice.

## Web Accessibility Checklist

As developers, these are a few of the things to look out for when building websites or application in order to ensure that people of varying abilities can access them equally.  

### How to make images accessible

All images should have descriptive sentence-like alt texts instead of just a word or clause. For example, the image below should have an alt text as shown in the code beneath it.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/pizza.jpg)
_Photo by [Unsplash](https://unsplash.com/@hybridstorytellers?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Hybrid Storytellers</a> on <a href="https://unsplash.com/t/food-drink?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

```html
<img alt="a right hand removing a slice from a whole pizza" src="https://unsplash.com/photos/XYyUxXw_oQw"/>
```

The code above shows a sentence-like, descriptive alternative text for the image. The goal of the alt text should be to describe the image in such a way that people using screen readers feel like they can visualize or imagine exactly what image is being described.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/ImageAlt-1.png)
_Image Alt text output_

The next level of accessibility as seen in the above image, is to write alt texts so that users who may be encountering connectivity issues have an idea of the image before they see it.

### How to make links accessible

Links should be descriptive and suggestive, and you should label all links with exactly what they do. 

Avoid embedding your links in vague texts such as ‘here’. For instance, if we wanted to refer to my most recent article, for the sake of users who rely on screen readers, this is how to do it.

```html
<p>
Check out my most recent article on <a href="https://www.freecodecamp.org/news/web-layouts-use-css-grid-and-flex-to-create-responsive-webpages/">Web Layouts – How to Use CSS Grid and Flex to Create a Responsive Web Page</a>
</p>
```

In the code above, the link tag is wrapped around the whole title of the article instead of simply making the link text a vague 'here'. This way, everyone who sees, reads, or hears it knows exactly what resource will be found when the link is clicked.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AccessibilityLink.png)
_Link output image_

When screen readers get to a link that is as descriptive as what we have in the image above, it makes it very easy for visually impaired users to know what the link does and, in effect, decide whether or not to visit it. 

### **How to make forms accessible**

When creating web forms, you should consider users with visual or motor limitations. Make it easy for users who can't use the mouse to navigate your form with the keyboard and users relying on screen readers to know the exact information needed for each input.

Ensure that your forms are accessible by using `<label>` or `aria-label` to communicate the purpose of an input or what information it requires to screen readers. 

`<fieldset>` tags tell the form that groups of inputs belong together and `<legend>` tags act as labels for groups of inputs. These become especially necessary when dealing with questions that involve checkboxes or radio buttons.

```html
<fieldset class="first-section">
      <legend>Contact Details</legend>
      <label for="name">Name</label>
      <input type="text" id="name" name="name" autofocus placeholder="Ophy Boamah" autocomplete="on" required> <br><br>
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="ob2@hotmail.com"> <br><br>
      <label for="tel">Phone</label>
      <input type="tel" id="tel" placeholder="+233 200001212"> <br><br>
</fieldset>
```

In the code above, I implement all the form best practices I mentioned. The fieldset tag creates an initial "first-section" group. The legend tag contains text that provides a description for the group of elements. Finally, the label tag identifies each of the inputs and their purpose.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Fieldset.png)
_Accessible form output_

The image above is the output of the code. To learn more about creating modern and accessible forms, check out my previous article on [How To Create and Validate Modern Web Forms With HTML5](https://www.freecodecamp.org/news/create-and-validate-modern-web-forms-html5/). 

### Video and audio accessibility

All videos should have subtitles and captions. Similarly, all audio should have transcripts, so that people with hearing challenges can still follow along and understand.

```html
 <video id="video" controls preload="metadata">
     <source src="assets/samplevideo.mp4" type="video/mp4" />
     <track
     label="English"
     kind="subtitles"
     srclang="en"
     src="assets/samplevideo-en.srt"
     default />
 </video>
```

The code above shows a video element that introduces the track tag for adding subtitles so that users who are not able to hear the accompanying audio can read to follow along.

%[https://vimeo.com/776769878#t=0]

### How to select colours for accessibility 

When selecting colours for your websites, consider people who are colour-blind and those who have issues with sight. 

When we use colours with poor contrast, it makes it difficult for users to read or navigate content on a web page. This means that we must always ensure that even in bad lighting conditions, our foreground and background colours have enough contrast between them for button, links, images, icons, texts and so on. 

If you're unsure whether two colours complement each other in an accessible way, check using this [online colour checker tool](https://accessibleweb.com/color-contrast-checker/).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/wcagcolorcheceker.png)
_Use a color checker tool to check color contrast_

You can also add this [Web Accessibility Checker Chrome Extension](https://chrome.google.com/webstore/detail/accessible-web-helper/gdnpkbipbholkoaggmlblpbmgemddbgb) to your browser for onsite accessibility checks.

### How to make transitions and animations accessible

Use transitions and animations sparingly and only when extremely necessary in order not to trigger some users. 

There are those who get dizzy or experience seizures when they encounter elements that move rapidly. Provide a way for such users to pause, hide, or stop the animation by making those controls available. 

### How to create accessible page structure and navigation

Use the appropriate HTML tags to semantically structure websites. Your site should be easy to navigate especially with assistive technology. 

Page titles should be descriptive so users can easily differentiate between tabs.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Web Accessibility Site | Checklist for Developers</title>
</head>
<body>
  <header>
  <nav>
    <ul>
      <li>Home</li>
      <li>About</li>
      <li>Contact</li>
    </ul>
  </nav>
  </header>
  <main>
    <section>
      <div>
        <h1>
          Welcome to Web Accessibility
        </h1>
        <p>
          This is semantic structuring with HTML tag
        </p>
      </div>
    </section>
  </main>
  <footer>
    <a href="https://codehemaa.com">My website</a>
  </footer>
</body>
</html>
```

The code above shows a web page with a descriptive title. I've used the right semantic tags to properly structure the page by distinguishing the header from the main body and footer. 

I've also properly labelled sections, divs, and headings. This helps screen recorders to properly spell out exactly what element and content is present on the page.

## Conclusion

If the inventor of the web stated emphatically “_access by everyone regardless of disability is an essential aspect_” of the web, then as developers we must strive to achieve just that. Plus, it's just the right thing to do.

You should consider accessibility even before you start to build your sites – not done after as damage control. Going forward, we ought to strive for inclusion by contributing to build a more a11y-conscious and a11y-friendly web. 

Thanks for reading 👋🏾. I hope you found it helpful.

  

