---
title: How To Publish Your Chrome Extension
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-11-30T18:08:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-your-chrome-extension-dd8400a3d53
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6SBGxnrpx8yGjo5S
tags:
- name: chrome extension
  slug: chrome-extension
- name: coding
  slug: coding
- name: development
  slug: development
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'In my previous article I wrote, I talked about the building blocks of a
  Chrome extension. Now, I would like to focus on the other part of building a Chrome
  extension: what to do when you are done building it. The process in itself is not
  long nor har...'
---

In my previous [article](https://medium.freecodecamp.org/how-to-implement-a-chrome-extension-3802d63b5376) I wrote, I talked about the building blocks of a Chrome extension. Now, I would like to focus on the other part of building a Chrome extension: **what to do when you are done building it**. The process in itself is not long nor hard, but there are some things you should pay attention to.

Every Chrome extension is published on the [Chrome Web Store](https://chrome.google.com/webstore/category/extensions). Think of it as the equivalent to Google’s Play Store or Apple’s App Store, but only for Chrome extensions and themes.

### Steps

If you haven’t created one already, you will need to create a Developer account. In it, you will have a Developer Dashboard.

> As I stated in the previous article, there is a $5 one time signup fee if you want to be able to publish Chrome extensions. This will give you the ability to publish up to 20 extensions

Once you are the proud owner of a Developer account, the next step is to upload your Chrome extension to your account. To do this, create a ZIP file with all the files associated with your extension. **The only file Google requires you to upload is the manifest.json file**. But you will want to add the JavaScript files you have as well.

After that, the next step is to publish our extension. Login to your developer account and go to your Developer Dashboard.

![Image](https://cdn-media-1.freecodecamp.org/images/u6LZm6jafoX5k2lVN-j1m64kWSJuCm658oBK)

There you will see an **Add New Item** button.

![Image](https://cdn-media-1.freecodecamp.org/images/Y5aNZVWVXR4nIZFiLm8yblYJVnv5dGVBEZ95)
_Click Me_

> **_⚠️ Be aware that once you add an extension to your Developer Dashboard you cannot delete it. As long as it is not published, it will not count towards your extension limit._**

This will direct you to a page where you can upload the ZIP file we created earlier:

![Image](https://cdn-media-1.freecodecamp.org/images/0kFfxuPAmDDtuVIZhzbxq29DXK9dUjvVmUbY)
_Click choose file and press upload_

Assuming everything went fine, you will be directed to the next page:

![Image](https://cdn-media-1.freecodecamp.org/images/w6sFu56M9LcBHekEYrid8oSWKC3ZN6XyfE8o)
_Here you can provide a description of your extension_

> If you are planning to make changes to your extension, you can use the Upload Updated Package button to re-upload your ZIP file.

On this page, you can add an icon that will be shown on the toolbar:

![Image](https://cdn-media-1.freecodecamp.org/images/TypgvFz8T8rYSBC5--KHPZm-7pzJSJnJn9hQ)

Add screenshots of your extension (these will be used when a user looks at your extension):

![Image](https://cdn-media-1.freecodecamp.org/images/33NG7giJ5X3U2Jkzc-1tm1EGkbdJBEJl47Y1)

And various other features like choosing a Category for the extension (I.E. Fun), choosing the regions where your extension will be available, the pricing of your extension, and other categories which I suggest you take a look at.

When you are done fine tuning the details of your extension, you will arrive at the end of the page and see the following buttons:

![Image](https://cdn-media-1.freecodecamp.org/images/-T9LN7NxeYyk8gqb4nuFe2p0J-P9zH9TvkKq)

The two left buttons allow you to save the work you have done so far configuring your extension (or discarding it), and the two right ones are for when you are ready to publish. To see how everything you configured will look on the Chrome Web Store, press the **Preview Changes** button. When you are satisfied with what you have, click **Publish Changes**.

![Image](https://cdn-media-1.freecodecamp.org/images/i0xLibubdSwSbK0BDVOsPv3WTdfKFWSoGhrN)
_Photo by [Unsplash](https://unsplash.com/@adspedia?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Val Vesa</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Congratulations! You have just published your first Chrome Extension!

In your Developer Dashboard you will now see this:

![Image](https://cdn-media-1.freecodecamp.org/images/oBMLsvN4hlBDyUy0ZGwfVKOHFrJwi6Aa3Qso)

Clicking the _Stats_ link will give you analytics regarding your extension (how many impressions, installs and active users). I’m looking forward to seeing your published Chrome extensions.

