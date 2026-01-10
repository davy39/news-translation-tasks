---
title: Web Accessibility Tips for Developers – A11y Principles Explained
subtitle: ''
author: Adeola Ajiboso
co_authors: []
series: null
date: '2023-11-02T14:17:51.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-for-devs
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/51314.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Accessibility isn't just something you check off as done when you're building\
  \ websites and web apps. It's a basic part of making the online world a better and\
  \ fairer place for everyone. \nIn this article, you'll learn what accessibility\
  \ means, and why..."
---

Accessibility isn't just something you check off as done when you're building websites and web apps. It's a basic part of making the online world a better and fairer place for everyone. 

In this article, you'll learn what accessibility means, and why it's important to make accessibility a part of your regular workflow. I'll also give you practical tips with examples to make your websites more accessible. 

Let's explore the key parts of web accessibility together and help you make a website that includes everyone.

## What is Web Accessibility?

[Web accessibility](https://www.freecodecamp.org/news/accessibility-best-practices-to-make-web-apps-accessible/) refers to the practice of designing and developing websites, applications, and digital content in a way that ensures people with disabilities can perceive, understand, navigate, and interact with them effectively.

## Principles of Web Accessibility

To effectively enhance the accessibility of your websites and apps, you'll want to follow these fundamental principles outlined by the Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0)):

### Is it Perceivable?

Content should be displayed in a manner that all users can understand, regardless of their sensory abilities. Here are some ways you can make your content more perceivable:

First, you can provide captions for audio and video materials. Adding captions to your website or application allows those with hearing disabilities to understand the information being shared, and make the content more accessible to everyone.

You can see an example of adding captions to a video in the image below: 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/img.jpg)
_Image of a video illustrating the use of captions._

Next, make sure you use proper color contrast for text and background elements.

Colors are an important part of a website, and we can describe them in terms of hue, lightness, and saturation.  
  
There are several categories of colors which include warm colors, cool colors, and neutral colors

**Warm Colors:** Warm colors include red, orange, and yellow, and variations of  
those three colors. These are the colors of fire, fall leaves, sunsets, and sunrises, and are generally energizing, passionate, and positive. 

**Cool Colors:** Cool colors include green, blue, and purple, are often more  
subdued than warm colors. They are the colors of night, water, of nature, and are usually calming, relaxing, and somewhat reserved.

**Neutral Colors:** Neutral colors often serve as the backdrop in design. They’re  
commonly combined with brighter accent colors. But they can also be used on their own in designs and can create very sophisticated layouts. Neutral colors include black, white, gray, cream, and beige.  
  
Examples of colors that will make good contrast are white and blue, purple and white, yellow and white, light purple and black, green and white, black and white, and so on – basically any colors that are different enough from each other to create that contrast.  
  
Examples of colors that will make a bad contrast are gray and white, brown and orange, red and purple, and so on.

Here is an example that shows good color contrast that's easy to read:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/1.png)
_Image illustrating good contrast using a dark blue background with white text_

And here's an image with poor color contrast that's hard to read:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/2.png)
_Image Illustrating bad contrast using a white background with light grey text_

Also, it's a good idea to include descriptive alternative text (alt text) for images, explaining what they depict and their purpose.

So for example, when you want to add an image to your website, you can add alt text to it explaining what it depicts. 

Here is a markup description of how to add alt text to an image:

```HTML
    <img src="Dog.png" alt="Image of a dog">
```

Here is an example that shows an image of two (2) dogs:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/dog.jpg)
_Image of two dogs_

And here's an example of an image that illustrates the use of alt text:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/dog1-1.jpg)
_Image of dog with alt text displayed_

You should also describe your icon buttons.

Icons can be easily understood most of the time. It's widely recognized that an x symbol, like this ❌, typically closes a window, a check mark ✅ signifies completion, a forward arrow ▶ signifies send (or play), and a plus sign ➕ represents addition. 

But this is clear only for individuals with visual capabilities. For people who aren't able to see the buttons, you'll need to provide a description so they know what that button does.

Let's take a look at this HTML and CSS code that shows how to make buttons access:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
     integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" 
     crossorigin="anonymous" referrerpolicy="no-referrer" />
    <title>Document</title>
</head>

<style>
    button{
        border: none;
        outline: none;
        color: #fff;
        padding: 12px 12px;
        margin: 10px;
        border-radius: 10px;
        background-color: red;
        cursor: pointer;
    }
</style>
<body>
    <button><i class="fa-solid fa-trash"> Delete </i></button>
    <button style="background-color:green;"><i class="fa-solid fa-check"> Check </i></button>
    <button style="background-color:green;"><i class="fa-solid fa-play"> Send</i></button>
    <button style="background-color:blue;"><i class="fa-solid fa-plus"> Add</i></button>
</body>
</html>

Here's the result of the code implemented above:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/code1.jpg)

### Is it Operable?

Users should be able to navigate and interact with the interface quickly. Consider the following factors:

First, make sure you use clear and consistent headings.

This is what clear and consistent headings look like:

# I am a Title

## I am a Subtitle

### This is heading 3

#### This is Heading 4

##### This is Heading 5

###### This is heading 6



As you can see, these headings go from largest to smallest in order. We have an H1 heading first, followed by H2, H3, and so on.

Here are some headings that don't follow the proper hierarchy: 


###### This is heading 6

##### This is Heading 5

#### This is Heading 4

### This is heading 3

## I am a Subtitle

# I am a Title

In this example, the headings go in reverse order, starting from H6 and moving up through H5, H4, and so on. 

Just remember to use proper heading hierarchy – don't use an H2 and then jump straight to H4 for a subheading, for example, as this is visually jarring and doesn't convey the proper importance or hierarchy of the text.

Here's why heading hierarchy is important:

* A clear heading hierarchy helps readers easily navigate and understand the content of a document.
* Heading hierarchy is crucial for accessibility, as it helps screen readers and assistive technologies interpret the structure of the content. This is important for individuals with visual impairments who rely on such tools to access information.
* A well-organized heading hierarchy implement a logical flow of information, ensuring that topics are presented in a coherent order.

Also, refrain from using elements that might trigger physical discomfort, like bright flashing lights.

And make sure you think about [keyboard accessibility](https://www.freecodecamp.org/news/designing-keyboard-accessibility-for-complex-react-experiences/) so users can navigate and communicate using the keyboard, and not exclusively using a mouse.

### Is it Understandable?

Content and functionality should be presented clearly and understandably. Consider the following factors:

* Organize content using headings, subheadings, and bullet points to enhance readability.
* Provide instructions and error messages that are easy to understand.
* Use simple and concise language, avoid complex terms.

### Is it Robust?

Websites should be built using robust and widely supported technologies to enable compatibility across devices and assistive technologies. 

You'll want to maximize compatibility with current and future user agents, including assistive technologies.

Here are some of the ways you can maximize compatibility with current and future agents, including assistive tools:

* Use [HTML5 semantic elements](https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/) like `<header>`, `<nav>`, `<main>`, and `<footer>` to enhance the document's structure.
* Ensure that your [JavaScript code is efficient](https://www.freecodecamp.org/news/javascript-performance-async-defer/) and doesn't block the rendering process.
* Utilize [browser developer tools](https://www.freecodecamp.org/news/learn-how-to-use-the-chrome-devtools-to-troubleshoot-websites/) and online testing services to identify and fix compatibility issues.
* Conduct [usability testing](https://www.freecodecamp.org/news/10-best-ux-testing-software-tools/) with a diverse group of users, including those who rely on assistive technologies, to gather feedback and make improvements.
* Optimize your website for fast loading times and low data usage using techniques like [caching](https://www.freecodecamp.org/news/a-detailed-guide-to-pre-caching/) and [tools like CDNs](https://www.freecodecamp.org/news/cdns-speed-up-performance-by-reducing-latency/) to reduce latency. This benefits both accessibility and user experience.
* Document your code and accessibility features for future maintainers.
* Test [website compatibility across various browsers](https://www.freecodecamp.org/news/cross-browser-compatibility-testing-best-practices-for-web-developers/). Testing website compatibility involves ensuring that your website functions correctly and looks good on a variety of devices, browsers, and assistive technologies. 

Here are the steps you can follow to test website compatibility effectively:

1. **Device Testing**: Test your website on various devices, such as desktop computers, laptops, tablets, and smartphones. This includes both iOS and Android devices.
2. **Browser Testing**: Check your website's performance and appearance on multiple browsers, including but not limited to Google Chrome, Mozilla Firefox, Apple Safari, and  Microsoft Edge.
3. **User Testing**: Conduct usability testing with real users. Ask them to use your website on different devices and browsers and collect feedback on compatibility issues.
4. **Performance Testing**: Assess website loading times, and optimize for speed using tools like Google PageSpeed Insights, GTmetrix, or Lighthouse. Check for compatibility with slow internet connections.

## Conclusion

Understanding web accessibility can enhance the user experience by creating a smooth and seamless interaction with websites and web applications.

Implementing these tips can improve the overall user-friendliness and navigability of your app. It'll help create a more enjoyable experience for all users, and will also allow people with disabilities to perceive, understand, navigate, and interact with your sites effectively.

