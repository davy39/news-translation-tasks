---
title: How to Write Accessible Technical Documentation – Best Practices with Examples
subtitle: ''
author: EZINNE ANNE EMILIA
co_authors: []
series: null
date: '2024-04-11T23:03:04.000Z'
originalURL: https://freecodecamp.org/news/best-practices-for-writing-accessible-technical-documentation
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/20240401_161256_0000.png
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: best practices
  slug: best-practices
- name: documentation
  slug: documentation
seo_title: null
seo_desc: 'When you''re writing technical documentation for a project or a tool you''re
  working on, you''ll want it to be accessible. This means that it will cater to and
  be usable by the diverse global audience on the web.

  Web accessibility aims to make it possib...'
---

When you're writing technical documentation for a project or a tool you're working on, you'll want it to be accessible. This means that it will cater to and be usable by the diverse global audience on the web.

Web accessibility aims to make it possible for anyone to access web content. There are common accessibility best practices for designers, developers, and writers. This article will cover some best practices for creating technical content.‌

## What is Web Accessibility?

[Web accessibility](https://www.freecodecamp.org/news/web-accessibility-for-devs/) is the practice of making it possible for anyone to consume or create content on the web, regardless of any health, economic, geographic, or language challenges they may have.

## Why is Web Accessibility Important?

It is important to apply web accessibility best practices in your projects for a number of reasons.

First, it'll help you reach a wider audience. When a person who may have different abilities comes across some data on the web – say on your website – they'll want to learn more or use the data. But if they are not able to access it, you will not be happy or have a good experience.

Imagine how many people are unable to utilize the web because they are not considered when devs and designers are making decisions about how the product, website, or tool will be built.

Another important thing about accessibility is that it improves your brand's quality. Letting people know you are an accessibility-oriented person or company by implementing it in your work shows that you want your information to be available t everyone. It also displays your versatility in your craft and your ability to improve and adapt with changing times and trends.

Also, as an individual, applying accessibility best practices benefits you as well. There are possible employment opportunities for developers and designers with great accessibility skills.

Good accessibility practices mean good SEO practices too, which can result in more visibility for your work.

Finally, accessibility is enforced by law in certain countries around the world, and web accessibility strategies are implemented by certain countries. There could be legal consequences if you overlook accessibility on your websites and apps.

## How to Write Accessible Technical Documentation

Software engineers have a key role in making the web accessible. But when it comes to writing documentation, technical writers also have a role to play in improving web accessibility.

Technical writers help write various types of content, like user guides, tutorials, API references, code documentation, and so on.

Now, let's look at some of the best practices for implementing web accessibility in technical writing. These strategies will help improve your documentation and make it more user-friendly and accessible to everyone.

### Use clear headings and paragraphs

When writing content, you should make sure to use headings – along with the proper heading hierarchy (H1 for the title of the page/article, H2 for major headings, H3 for subheadings, and so on).

Also, make sure to break your content up into paragraphs so it's easier to read and understand.

When you introduce a new topic, use a heading to call that out. When you talk about smaller topics within that section, use subheadings to alert the reader.

Headings are also important to help screen readers understand a page's contents and how to navigate through them. So use headings to help guide readers through the text in a logical manner.

You denote headings in markdown with hashes. Here's an example of headings in hierarchical order.‌

```css
# Use H1 for the page title

## Use H2 for major headings 
This heading is a main heading for the main section content. 

### Use H3 for subheadings 
This heading is a subheading that goes deeper into one of the main section's points.
```

### Make your content clear and concise

Overall, try to keep your sentences quite short in your docs. This makes them easier to read and understand (for everyone). You can also use images or videos to provide more details if needed.

Make sure you give the full meanings of any acronyms you are using for the first time. Also, always use simple sentences, and try not to use ambiguous words.

Here's an example of an overly complex, long sentence with difficult vocabulary:

```css
The web3 running on the Blockchain structure which is transparent, secure, immutable, decentralized would require the processes of artificial intelligence, where it would read data, process, and store information.
```

This is better:

```css
Web3 is built on the transparent, secure, unchangable, and decentralized structure of the blockchain. It uses artificial intelligence processes to read, process, and store information.
```

Your content should contain the main points you're trying to make, removing all forms of ambiguity.‌ ‌

### Use informative link text

All your in-line links should use clear, detailed, and descriptive text. You can describe the link's purpose or the company's name if it is a brand, for example.

Links are important for improving the ranking of a page. And using links like "Click here" or "Read More" is not all that helpful, as they don't tell the reader much about what they'll find at that link.

For instance, if I wanted to link a W3C (World Wide Web Consortium) accessibility tutorial to this article, I could use the following format: Check out [these resources for content writers by W3C](https://www.w3.org/WAI/roles/writers/).

### Add alt text and captions to media content

#### Images

Adding descriptive text to the alt text attribute allows screen readers to be able to read out the alt text associated with an image. Alt text also helps search engine bots that crawl the page know how to classify that content.

When you're adding alt text, describe the purpose of the image and not what the image is. For instance, let's say you're using an image that shows some shipping containers in a section that is about containerization.‌

![Various containers on a ship in motion to illustrate the packaging structure and process of a digital container.](https://www.freecodecamp.org/news/content/images/2024/04/containers-1.jpeg align="left")

*Various containers on a ship in motion to illustrate the packaging structure and process of a digital container.*

Instead of writing alt text like "various containers on a ship in motion", you could write "various containers on a ship in motion to illustrate the packaging structure and process of a digital container."

While alt text serves as an alternative for the image, captions give more details about the image. You can use HTML to insert image captions. Markdown does not support image captions, but markdown documentation sites usually have a way around it (for example, through plugins – ReadTheDocs, MkDocs – or inserting HTML via a custom component –Docusaurus).

As an example, I'll show you how to add image captions in Docusaurus.

**How to add image captions in a Docusaurus .md file:**

* Create a folder `components` in the `src` folder.
    
* Create a file named `figure.jsx`.
    
* Add this line of code to it:
    

```css
import React from "react"; 
import useBaseUrl from "@docusaurus/useBaseUrl"; 
export default function Figure({ src, caption }) {
  return ( 
  <figure> <img src={useBaseUrl(src)} alt={caption} /> 
  <figcaption>{`Figure: ${caption}`}</figcaption> </figure> 
  ); 
}
```

* Go to the `.md` file where you have the image and import the code.
    

```css
import Figure from '@site/src/components/figure'; 
import figure1 from 'path-to-image';
```

* Add it to the file.
    

```css
<Figure caption="This is a caption for the image" alt="This is alt text" src={figure1} />
```

The image will now display with a caption.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_13-3.png align="left")

*A screenshot example of image caption*

#### ‌Videos

To caption videos, HTML is a great option. But if you are using markdown, you can embed videos from YouTube and Vimeo using the `<iframe>` tag. These apps offer in-built caption support so you can enable captions before adding the embed code.

You could also install third-party plugins for this purpose.

Here's another tip: avoid flashing content in your videos as it could lead to seizure triggers. If your video has flashing bright colours, ensure that it does not exceed two times within a second.

### Add transcripts to audios and videos

It's a good idea to add transcripts to your audio and video content. Not everyone will want to watch or listen to the content. But they may be curious to know what it is about.

By adding a transcript, you make it easier for anyone to navigate through the content and get the information that they need.

#### Transcript for audio

For audio content, you can insert transcripts using HTML. Here's an example:

```html
<audio controls muted><!--Always set your audios to muted--> 
    <source src="ringtone.mp3" type="audio/mpeg"></source> 
</audio> 
<code> 
    <p>Here is a transcription of the text</p> 
    00:03 = I am going to be productive today<br><br> 
    00:05 = I am going to be productive today<br><br> 
    00:08 = I am going to be productive today<br><br> 
    00:10 = I need to be productive today<br><br> 
    00:11 = I have to be productive today<br><br> 
    00:13 = I should be productive today<br><br> 
    00:16 = I am going to be productive today<br><br> 
    00:18 = I ought to be productive today<br><br> 
    00:21 = I have to be productive today<br><br> 
    00:23 = Productivity matters to me <br><br> 
</code>
```

For markdown documentation sites like Docusaurus, you can create a custom component.‌

* In your `src/components` folder, create a file named `transcript.jsx`.
    
* Insert this code:
    

```javascript
import React, { useState } from 'react'; 
export default function Transcript({ }) { 
  const [showTranscript, setShowTranscript] = useState(false); 
  const toggleTranscript = () => { 
    setShowTranscript(!showTranscript); 
  }; 
  return ( 
    <div> <a href="#" onClick={toggleTranscript}> { 
    showTranscript ? 'Hide transcript' : 'View transcript'
    } 
    </a> {showTranscript && ( <div id="transcriptText"> (insert your transcript text here) </div> )} 
    </div> 
  ); 
}
```

* Go to your markdown file and import it.
    

```css
import Transcript from '@site/src/components/transcript'; 

<Transcript />
```

‌

![A screenshot of the audio transcript output on a documentation site](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_17-6.png align="left")

*A screenshot of the audio transcript output*

‌**Note:** I added some tweaks to the code to make transcript display optional. You can edit it if you want the transcript to show as the page loads.

#### Transcript for video

Now for videos, YouTube is a great option. It provides inbuilt transcripts for your videos. So, you can always embed YouTube videos in your docs.

The transcript is in the video description after the main details. The transcript will display with the timestamps when you click the "Show Transcript" button.

### Add code snippets and use the colour contrast technique

#### How to add code snippets

Use code blocks within the text to explain code instead of images. You could also use code snippets to showcase the output of your code. Unless it is necessary to add an image, you should use code snippets.

For instance,

`index.html`

```html
<!DOCTYPE html> 
<html> 
    <head> 
        <meta http-equiv="content-type" content="text/html; charset=utf-8" /> <title>A calculator app</title> 
        <link rel="stylesheet" href="styles.css"/> 
    </head> 
    <body> 
    </body> 
</html>
```

This will allow screen readers to read through the code, which they are not able to do with screenshots.

![A screenshot of the above code](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_14-2.png align="left")

*A screenshot of the above code*

#### Colour contrast technique

The colour contrast technique implies using colours that are opposite or heavily contrasting.

For example, using black text on a white background has a high contrast, as opposed to using light brown text on a brown background.

When combining colours, you could use an [accessible colour palette like Color Safe](http://colorsafe.co/).‌

![Using a pale white colour on a green background gotten from Color Safe](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_15-4.png align="left")

*Using a pale white colour on a green background gotten from Color Safe*

### Add translation options

There are documentation sites that provide translation options where you can build your docs in multiple languages, websites like Jekyll. [This is an example](https://leo3418.github.io/collections/multilingual-jekyll-site/add-language-switcher.html).

Docusaurus is also another doc site that provides multilingual options using Crowdin or Git.

* [Follow through this guide](https://docusaurus.io/docs/i18n/git) to set up translation and localization on Docusaurus using Git.
    
* [Follow through this guide](https://docusaurus.io/docs/i18n/crowdin) to set up translation and localization on Docusaurus using Crowdin.‌
    

### Use accessibility testing tools

There are tools you can use to check for errors in accessibility in your docs. Some examples are [WAVE (Web Accessibility Evaluation Tool)](https://wave.webaim.org/) and [AXE (Accessibility Engine)](https://www.deque.com/axe/).

Also, you can get the [NVDA(NonVisual Desktop Access) screen reader](https://www.nvaccess.org/download/) to test out your content. This software will let you know how the content of your documentation will be perceived by a user using a screen reader.‌

### Set up an improvement or suggestion box

Finally, it may not be possible to cover the needs of every user. So you could add a suggestion or improvement box, allowing users to send feedback about how you could further improve the content. Hearing firsthand from users can help you know how best to make the docs accessible for them.

To add an improvement box, you could use an external form link that stores the users' inputs or you could set up the suggestion box in the docs.

#### How to add an external form link in Docusaurus

You would need to create a custom component for that.

* Go to `src/components` folder and create a file `feedback.jsx`.
    
* Add this code:
    

```css
import React from 'react'; 

export default function FeedbackButton({ href }) {
  return ( <a href={href} target="_blank" rel="noopener noreferrer" > Give Feedback </a> ); 
};
```

* In your markdown file import it:
    

```css
import FeedbackButton from '@site/src/components/feedbackbutton';
```

* Insert the link
    

```css
<FeedbackButton href="https://forms.google.com" />
```

When you run it on your docs, it should showcase a link to Google forms. Google Forms is an example, you could add the link to your company website or server. Here's what it'll look like:

![A feedback link that states "Give feedback" for suggestion or improvement on a docusaurus docs site that leads users to an external site which is Google Forms](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_18-3.png align="left")

*A feedback link for suggestion in a docs site*

## Summary

To follow and implement these accessibility best practices, you can consider creating or using an already made style guide. This can help you consistently implement these practices and make it easier for you and other technical writers on your team.

There are style guides focused on accessibility for technical writers, such as the following:

1. [Accessibility style guide by Heyawhite](https://github.com/heyawhite/tech-writing-tools/blob/main/accessibility/style.md)
    
2. [Write accessible documentation by Google for developers](https://developers.google.com/style/accessibility)
    
3. [Writing for Accessibility by MailChimp content style guide](https://styleguide.mailchimp.com/writing-for-accessibility/)
    

That sums up my tips about web accessibility practices in writing. I'm a technical writer, and you can reach out to me on [Instagram](https://www.instagram.com/ezinneanneemilia/) or hire me via [Upwork](https://www.upwork.com/freelancers/~013e195fa64f8b3456?mp_source=share). Thank you for reading.‌
