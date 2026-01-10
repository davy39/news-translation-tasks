---
title: How to Improve Web Accessibility with Landmarks - Explained with Examples
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2025-08-05T20:51:05.799Z'
originalURL: https://freecodecamp.org/news/improve-web-accessibility-with-landmarks
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754425989581/1302898e-439b-4666-af27-cf1b091c6975.png
tags:
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: If you’re reading this article on the freeCodeCamp publication, you should
  see some visual clues in different sections of the page. The header is at the top
  of the page. If you scroll all the way to the bottom of the page, you can see the
  footer sect...
---

If you’re reading this article on the freeCodeCamp publication, you should see some visual clues in different sections of the page. The header is at the top of the page. If you scroll all the way to the bottom of the page, you can see the footer section in grey background, which is clearly separated from the body with a white background.

freecCodeCamp, like other websites, visually separates the sections of the page to give the user clues so they can easily navigate between sections.

While sighted users have visual clues about the sections, those who use assistive technology like a screen reader, rely on landmarks to navigate through the page.

Simply put, landmarks are semantic regions in a web page that define the purpose of its sections. Landmarks allow assistive technologies to jump between major parts of the page, just like sighted users visually scan headings or menus.

Common HTML landmarks include:

* `<header>` – Represents introductory content or a page header.
    
* `<nav>` – Identifies navigation links.
    
* `<main>` – Marks the main content area of the page.
    
* `<aside>` – Contains complementary or related information.
    
* `<footer>` – Represents page or section footer.
    

## Table of contents

* [How to Navigate Landmarks in Any Browser](#heading-how-to-navigate-landmarks-in-any-browser)
    
* [How to Navigate Through Landmarks on a Mac Voice Over](#heading-how-to-navigate-through-landmarks-on-a-mac-voice-over)
    
* [Why Landmarks Matter for Accessibility](#heading-why-landmarks-matter-for-accessibility)
    
* [How to Use Landmarks](#heading-how-to-use-landmarks)
    
* [Concrete Examples of Each Landmark](#heading-concrete-examples-of-each-landmark)
    
* [Final Thoughts](#heading-final-thoughts)
    

## How to Navigate Landmarks in Any Browser

### General Browser Support

Most screen readers support landmark navigation with shortcut keys. Here's a basic overview:

| Screen Reader | OS | Shortcut |
| --- | --- | --- |
| VoiceOver | macOS | `Control + Option + U` (to open Rotor), then arrow keys to navigate |
| NVDA | Windows | `D` to move to the next landmark |
| JAWS | Windows | `R` to cycle through regions |
| Narrator | Windows | `Caps Lock + Right Arrow` to move by landmark |
| ChromeVox | Chrome OS | `Search + Left/Right Arrow` to move between landmarks |

These shortcuts let users jump between regions—for example, from the `<main>` content directly to the `<footer>`—without tabbing through every interactive element.

## **How to Navigate Through Landmarks on a Mac Voice Over**

1. **Turn on VoiceOver:** You can easily turn VoiceOver by opening Finder and typing VoiceOver. Toggle VoiceOver on.
    
    ![Finder searching the word, "voiceOver" Underneath is a VoiceOver with a toggle to turn on. Underneath that is VoiceOver Utility](https://cdn.hashnode.com/res/hashnode/image/upload/v1753898345534/2fba73d7-b102-41ce-8731-f865a71631e6.png align="center")
    
2. **Open rotor:** Once you turned on voiceOver, press Control+Option+U on your keyboard. This will open the VoiceOver rotor. You can press right and left arrow to switch through different rotor items which include navigating with all headings, links and landmarks. Screenshot below is the accessibility rotor’s landmark item option on freeCodeCamp article. The article is divided up into navigation, search, main, article and footer elements.
    

![Landmarks title followed up by navigation, search, main, article and footer](https://cdn.hashnode.com/res/hashnode/image/upload/v1753897939501/ddef4a40-047d-469c-80e3-add29ff8f297.png align="center")

3. **Press down and up arrow to navigate through landmarks:** Once you are on accessibility rotor’s landmark items, you can press down and up arrow to navigate to different sections of the page. If you want to go to the footer, press the down arrow until you reach footer and then press enter.
    

## **Why Landmarks Matter for Accessibility**

### **1\. Easier Navigation for Screen Reader Users**

Screen readers provide shortcuts to navigate through landmarks. Without landmarks, users must tab through every single link or element, which is frustrating and time-consuming. In the freeCodeCamp article example, the user might want to skip to the footer in order to find and click on the donation link. Without landmarks, the user will need to tab through the entire article to reach the footer. This is time consuming and exhausting. Landmarks provide easy navigation to users that rely on screen readers.

### **2\. Consistent Structure Across Pages**

When every page uses the same landmark structure, users can predict where navigation menus, main content, and sidebars are located. This predictability reduces cognitive load. With organizing the page into sections, you can easily figure out where to go next.

### **3\. Clear Context and Orientation**

Landmarks communicate the **role** of content. For instance:

* The `main` landmark signals: *“This is the core content of the page.”*
    
* The `aside` landmark signals: *“This is supplementary or related content.”*
    

This helps users decide which areas to skip or focus on.

## How to Use Landmarks

### ✅ **Basic Landmark Structure**

Here’s an example of a page using HTML5 landmarks:

```plaintext
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Accessible Landmark Example</title>
</head>
<body>

  <header>
    <h1>Website Logo</h1>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h2>Main Content Area</h2>
    <p>This is the primary content of the page.</p>
  </main>

  <aside>
    <h3>Related Links</h3>
    <ul>
      <li><a href="#resource1">Resource 1</a></li>
    </ul>
  </aside>

  <footer>
    <p>2025 Example Company</p>
  </footer>

</body>
</html>
```

The HTML is divided into 5 landmark sections which are header, navigation, main, aside and footer. If the screen reader wants to skip the header and go direct to the main content, they can do so by turning the accessibility rotor and clicking on the main landmark. Landmarks allow screen reader users to easily navigate through the page.

Here’s a breakdown of what each landmark is and how it's typically used:

### `<nav>` – Navigation Section

Used for menus, site-wide links, or breadcrumbs.

```plaintext
<nav>
  <ul>
    <li><a href="/about">About</a></li>
    <li><a href="/courses">Courses</a></li>
  </ul>
</nav>
```

**Real-world use**: Jump straight to the navigation to find the “Contact” page without browsing through all the content.

### `<main>` – Primary Page Content

Used once per page to wrap the most important content.

```plaintext
<main>
  <h1>Learn Accessibility</h1>
  <p>This article explains how to use landmarks...</p>
</main>
```

**Real-world use**: Skip past the header and sidebar to dive into the tutorial or article.

### `<aside>` – Complementary Information

Used for sidebars, ads, related links, or pull quotes.

```plaintext
<aside>
  <h3>Related Tutorials</h3>
  <ul>
    <li><a href="/accessibility/forms">Accessible Forms</a></li>
  </ul>
</aside>
```

**Real-world use**: Users can skip the aside if they don’t want extra content, or jump to it for helpful resources.

### `<footer>` – Page Footer

Used for closing content like copyright.

```plaintext
<footer>
  <p>&copy; 2025 FreeCodeCamp. All rights reserved.</p>
</footer>
```

**Real-world use**: Quickly navigate to support links, licensing info, or a newsletter sign-up.

### `<header>` – Top-of-Page or Section Header

Used for introductory content, such as logos or search bars.

```plaintext
<header>
  <img src="logo.png" alt="Site Logo" />
  <form role="search">
    <input type="text" aria-label="Search site" />
  </form>
</header>
```

**Real-world use**: Quickly access the search input or return to the homepage.

## **Final Thoughts**

Landmarks aren’t just an accessibility bonus—they’re a fundamental part of good UX. By implementing landmarks properly, you make your site easier to navigate for users with disabilities, comply with WCAG, and create a more predictable structure for everyone.
