---
title: How to Build an Advice Generator Chrome Extension with Manifest V3
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2025-08-25T20:19:19.961Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-advice-generator-chrome-extension-with-manifest-v3
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756152220137/8717b809-1186-4a15-92f8-ea926177ef76.png
tags:
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
- name: chrome extension
  slug: chrome-extension
seo_title: null
seo_desc: 'In 2025, using Chrome without extensions is like using a smartphone without
  apps. It’s possible, but you’re missing out on a lot.

  And despite how essential extensions are, creating one is very simple – it’s just
  HTML, CSS, and JavaScript with browser...'
---

In 2025, using Chrome without extensions is like using a smartphone without apps. It’s possible, but you’re missing out on a lot.

And despite how essential extensions are, creating one is very simple – it’s just HTML, CSS, and JavaScript with browser APIs.

In this tutorial, we are going to learn about Chrome extensions by building an Advice Generator extension with Manifest V3 (MV3), the latest and most secure architecture for Chrome Extensions. You can move along to see what we'll build [here](#heading-what-were-going-to-build).

### Table of Contents

* [What are the Key Components of a Chrome Extension?](#heading-what-are-the-key-components-of-a-chrome-extension)
    
* [How to Build an Advice Generator Chrome Extension](#heading-how-to-build-an-advice-generator-chrome-extension)
    
* [The Benefits of Manifest V3](#heading-the-benefits-of-manifest-v3)
    
* [How to Debug Your Chrome Extension](#heading-how-to-debug-your-chrome-extension)
    
* [Conclusion](#heading-conclusion)
    

## What are the Key Components of a Chrome Extension?

Chrome extensions are incredibly powerful tools that can add custom functionality directly into your Browser experience to transform how you use the web.

Before we write any code, let's understand some key components:

* Every extension starts with a **manifest** file. This JSON file tells Chrome everything it needs to know about an extension: name, version, permissions, and files
    
* The **user interface** is built with HTML, CSS, and JavaScript. It's essentially a mini webpage that lives inside your browser
    
* Finally, there's the **service worker** which runs in the background and fetches data from external APIs. In Manifest V3, service workers have replaced background pages
    

## How to Build an Advice Generator Chrome Extension

Here’s a look at what we’re going to build:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1755718930961/381f422d-f83c-49a9-a007-051ddea6e8da.png align="center")

This design is by [Frontend Mentor](https://www.frontendmentor.io/?via=ophyboamah).

**Prerequisites:**

To follow along with this tutorial, you need:

* Basic understanding of HTML, CSS and JavaScript
    
* A Chrome browser
    
* A text editor
    

When structuring an extension project, the only prerequisite is to place the `manifest.json` file in the extension's root directory.

### **Testing Your Chrome Extension (Load Unpacked)**

Before we start building, you’ll want to see your progress after each file to catch any issues early. Here’s how to load your extension into Chrome for testing:

1. Go to `chrome://extensions` to open the Chrome Extensions page.
    
2. In the top right corner of the Extensions page, toggle the **Developer mode** on.
    
3. Click the **Load unpacked** button that appears.
    
4. In the file dialog, go to the **root folder of the extension** and click **Select Folder**.
    

Your extension should appear. If its icon does not appear in your browser's toolbar immediately, click the **puzzle** icon in your toolbar and pin it.

![A screenshot showing how to pin a Chrome extension from a browser's toolbar](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711497449/6c3f056c-322d-45a2-b1b3-15a62b7fad44.png align="center")

Now let's start by defining our extension's identity in the `manifest.json` file.

### The Benefits of Manifest V3

The `manifest.json` is the heart of a Chrome Extension. Written in JSON (JavaScript Object Notation), it provides Chrome with everything it needs to know about your extension.

Think of it like a passport with visas and Chrome as the immigration officer verifying identity and access.

![An image depicting the analogy of the Manifest file as a passport and visa and Chrome as the immigration officer that ensures the right permissions.](https://cdn.hashnode.com/res/hashnode/image/upload/v1755715844005/b1742fbf-fafa-4c36-b08c-1637d00d625d.png align="center")

Manifest V3 (MV3), brings better performance, security, and reliability to extensions. MV3 uses service workers that activate only when needed, improving battery life and preventing extensions from slowing down your browser.

Let's break down each important field:

* `manifest_version` is the most critical line. Give it a value of 3 to tell Chrome you're using Manifest V3.
    
* `name`**,** `version`**,** `description` define your extension's basic identity.
    
* `action` is a Manifest V3 field that controls what happens when someone clicks your extension's `default_icon` in the toolbar. The `default_popup` points to your HTML file, so clicking the icon opens that page in a small popup window.
    
* `permissions` tells Chrome what your extension needs access to. We're using host permission [https://api.adviceslip.com/\*](https://api.adviceslip.com/) so our extension can fetch advice from that API. Without it, the extension would be blocked from making those requests. This might seem overly cautious, but it's a security measure that protects users.
    
* `background` points to your service worker script. The `service_worker` field tells Chrome that `service-worker.js` should run in the background.
    

### Step 1: Create a Manifest 3 File

Going by the explanations of the various parts of the file above, here's what our `manifest.json` file would look like:

```json
{
  "name": "Advice Generator",
  "description": "Get a fresh piece of advice whenever you need it!",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "index.html",
    "default_icon": "/icons/icon-dice.png"
  },
  "permissions": [
    "activeTab"
  ],
  "host_permissions": [
    "https://api.adviceslip.com/*"
  ],
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

You might see `activeTab` in other extension examples. While we don't strictly need it for this, it's worth knowing about. It gives temporary access to whatever tab the user is on, but only when they click the extensions icon.

The image below will be the result of running our manifest code above:

![A screenshot showing the Advice Generator Chrome extension after running the Manifest.json](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711701772/49fa40e5-1c5b-4cd3-a6f2-a9100db8efcb.png align="center")

### Step 2: Create the HTML and CSS Pages

Now that our extension has its identity and permissions defined, let's move on to building the user interface starting with an `index.html` page.

```xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advice Generator</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;800&display=swap" rel="stylesheet">
</head>
<body>
    <main class="advice-card">
        <h1 class="advice-id">ADVICE #<span id="advice-id-number"></span></h1>
        <p class="advice-quote" id="advice-quote">
            “It is easy to sit up and take notice, what's difficult is getting up and taking action.”
        </p>
        <div class="divider">
            <img src="icons/pattern-divider.png" alt="Divider pattern">
        </div>
        <button class="dice-button" id="generate-advice-btn">
            <img src="icons/icon-dice.png" alt="Dice icon">
        </button>
    </main>
    <script src="index.js"></script>
</body>
</html>
```

Now, let's bring the design to life with a `style.css` file in your root directory. We'll set up the overall body styles, position the card, and style all the elements within it.

```css
:root {
    /* Define colors from the Frontend Mentor style guide */
    --clr-light-cyan: hsl(193, 38%, 86%);
    --clr-neon-green: hsl(150, 100%, 66%);
    --clr-grayish-blue: hsl(217, 19%, 35%);
    --clr-dark-grayish-blue: hsl(217, 19%, 25%);
    --clr-dark-blue: hsl(218, 23%, 16%); 
    /* Typography */
    --ff-manrope: 'Manrope', sans-serif;
    --fw-regular: 400;
    --fw-bold: 700;
}
body {
    margin: 0;
    padding: 0;
    font-family: var(--ff-manrope);
    background-color: var(--clr-dark-blue);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    min-width: 30rem;
    box-sizing: border-box;
}
.advice-card {
    background-color: var(--clr-dark-grayish-blue);
    border-radius: 0.5rem;
    padding: 1.5rem 1.5rem;
    width: 60%; 
    text-align: center;
    position: relative;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
    margin-bottom: 70px; 
}
.advice-id {
    color: var(--clr-neon-green);
    font-size: 0.8em;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.advice-quote {
    color: var(--clr-light-cyan);
    font-size: 1.75em; 
    font-weight: var(--fw-bold);
    line-height: 1.4;
    margin-bottom: 1.2rem;
    padding: 0 15px;
}
.divider {
    margin-bottom: 35px;
}
.divider img {
    max-width: 90%;
    height: auto;
}
.dice-button {
    background-color: var(--clr-neon-green);
    border: none;
    border-radius: 50%;
    width: 2rem;
    height: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    position: absolute;
    bottom: -1rem; 
    left: 50%;
    padding: 1rem;
    transform: translateX(-50%);
    transition: box-shadow 0.3s ease-in-out;
}
.dice-button:hover {
    box-shadow: 0 0 40px var(--clr-neon-green);
}
.dice-button img {
    width: 2rem;
    height: 2rem;
}
```

The image below will be the result of running our HTML and CSS code above plus the initial manifest:

![An image of the Advice Generator Chrome extension design](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711748813/c641535b-5bdf-4adc-a11c-6115b1f1a284.png align="center")

With the HTML and CSS done, our extension's visual aspect is complete. Next, let’s give it life by writing the JavaScript that handles fetching new advice and updating the display.

### Step 3: Add a Service Worker

In Manifest V3, the core background logic for an extension lives in its Service Worker. Unlike the persistent background pages of Manifest V2, in V3 Service Workers run only when needed, such as in response to a message from `index.js` or a browser event.

Our `service-worker.js` will have these roles:

* Listen for a request from `index.js` (when the user clicks the dice).
    
* Fetch a new piece of advice from the Advice Slip API.
    
* Send that advice back to `index.js` to be displayed.
    

Create a file named `service-worker.js` in your extension's root directory.

```javascript
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "fetchAdvice") {
    fetchAdvice().then(adviceData => {
      sendResponse({ advice: adviceData });
    }).catch(error => {
      console.error("Error fetching advice:", error);
      sendResponse({ error: "Failed to fetch advice" });
    });
    return true;
  }
});
// Function to fetch advice from the Advice Slip API
async function fetchAdvice() {
  try {
    const response = await fetch("https://api.adviceslip.com/advice");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.slip; 
  } catch (error) {
    console.error("Could not fetch advice:", error);
    throw error; 
  }
}
```

#### Message Handling in Service Workers

Since Service Workers don't have direct access to the DOM of your `index.html` page (and vice versa), they communicate using message passing. As you can see in the code above, the user clicks the dice in `index.html`, and `index.js` will send a message to `service-worker.js` asking for new advice. The Service Worker will then fetch the advice and send it back in another message.

`chrome.runtime.onMessage.addListener` listens for incoming messages and `sendResponse` replies.

Our Service Worker is now ready to fetch advice. The next step is to make our `index.js` interact with it.

### Step 4: Add App Functionality

First, we'll create our `index.js` file. This script is responsible for all the user-facing logic. It will handle the user's interaction (clicking the dice), send a message to our `service-worker.js` to get new advice, and then update the `index.html` with the fetched advice.

Our `index.js` will perform the following steps:

1. Reference the HTML elements where we'll display the advice ID, quote, and dice.
    
2. Set up an event listener for when the dice is clicked.
    
3. Send a message to the `service-worker.js` to request new advice.
    
4. Receive the advice back from `service-worker.js` and update the content on the `index.html` page.
    

```javascript
// Get references to our HTML elements
const adviceIdElement = document.getElementById('advice-id-number');
const adviceQuoteElement = document.getElementById('advice-quote');
const generateAdviceBtn = document.getElementById('generate-advice-btn');
// Function to request advice from the Service Worker
function requestNewAdvice() {
  chrome.runtime.sendMessage({ action: "fetchAdvice" }, (response) => {
    if (chrome.runtime.lastError) {
      console.error("Error sending message:", chrome.runtime.lastError);
      adviceQuoteElement.textContent = "Error: Could not get advice.";
      adviceIdElement.textContent = "---";
      return;
    }
    if (response && response.advice) {
      adviceIdElement.textContent = response.advice.id;
      adviceQuoteElement.textContent = `“${response.advice.advice}”`;
    } else if (response && response.error) {
      console.error("Service Worker error:", response.error);
      adviceQuoteElement.textContent = `Error: ${response.error}`;
      adviceIdElement.textContent = "---";
    }
  });
}
if (generateAdviceBtn) {
  generateAdviceBtn.addEventListener('click', requestNewAdvice);
} else {
  console.error("Generate advice button not found!");
}
document.addEventListener('DOMContentLoaded', requestNewAdvice);
```

With `index.js` in place, our Advice Generator is now ready as you can see in the GIF below:

![A GIF showing the finished Advice Generator Chrome extension](https://cdn.hashnode.com/res/hashnode/image/upload/v1755717163786/326dc332-bf3b-4a8a-ba3a-25bdc829cf68.gif align="center")

The next crucial step is to know how to debug your extension, should anything go wrong.

## How to Debug Your Chrome Extension

Chrome provides excellent debugging tools to help troubleshoot extensions. Always follow these essential steps:

* Reload your extension after making changes (especially to `manifest.json` or `service-worker.js`) by clicking the refresh icon on `chrome://extensions`.
    
* Check your `manifest.json` for typos – missing commas or brackets will break everything.
    
* Verify your API URL and make sure you have the right permissions listed in `manifest.json`.
    

### Debugging the Main HTML and JS Pages

This is likely where you'll encounter most of your initial JavaScript or HTML/CSS issues.

1. Open the extension and right-click anywhere in the popup to Inspect.
    
2. Check the Console tab for JavaScript errors from your `index.js` file.
    
3. Use the Elements tab to inspect your HTML and tweak CSS styles in real-time.
    

![A GIF showing how to inspect the Elements and Console tabs of a Chrome extension](https://cdn.hashnode.com/res/hashnode/image/upload/v1755714931805/f03dc46c-b78b-44b6-bc67-bb7fe02499a9.gif align="center")

### **Debugging the Service Worker – Crucial for MV3**

The Service Worker runs in the background and has its own separate DevTools.

1. Go to `chrome://extensions`.
    
2. Click the **Service worker** link underneath your extension or the Errors button.
    
3. Check the Console and Network tabs for service worker and API errors respectively.
    

![A screenshot showing a Chrome extension with the service worker link and errors button](https://cdn.hashnode.com/res/hashnode/image/upload/v1755715410580/2c03c56c-affe-4a0a-939f-72ca866eecd3.png align="center")

## **Conclusion**

Congratulations, you've just built a Chrome extension using Manifest V3. You've created a user interface, implemented background processing with a service worker, and established communication between different parts of your extension. These skills are the building blocks for any Chrome extension, no matter how simple or complex.

Here are some helpful resources:

* [MDN on Browser Extensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/What_are_WebExtensions)
    
* [Chrome Devs on Chrome Extensions](https://developer.chrome.com/docs/extensions/get-started?hl=en)
