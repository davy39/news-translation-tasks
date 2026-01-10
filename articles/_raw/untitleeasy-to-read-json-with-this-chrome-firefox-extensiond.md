---
title: How to get easy-to-read JSON trees with this free Chrome Extension (or Firefox
  Plugin)
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2019-08-14T11:29:54.000Z'
originalURL: https://freecodecamp.org/news/untitleeasy-to-read-json-with-this-chrome-firefox-extensiond
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/0_9FUbCPtz2dGrBmIi.png
tags:
- name: chrome extension
  slug: chrome-extension
- name: json
  slug: json
seo_title: null
seo_desc: 'JSON is a very popular file format. Sometimes we may have a JSON object
  inside a browser tab that we need to read and this can be difficult.

  We may need to go and search for an online tool that turns it into an easy-to-read
  format so we can understan...'
---

[JSON](https://www.json.org/) is a very popular file format. Sometimes we may have a JSON object inside a browser tab that we need to read and this can be difficult.

We may need to go and search for an online tool that turns it into an easy-to-read format so we can understand it.

Now, here is a Chrome and Firefox extension that does the formatting and makes your JSONs instantly pretty inside your browser, without having to perform many unnecessary steps.

It comes with support for JSON and JSONP and highlights the syntax so that you can differentiate different attributes and values accordingly. It also comes with the option to collapse nodes, clickable URLs that you can open in new tabs, and you see the raw, unformatted JSON.

It works with any JSON page, regardless of the URL you opened. It also works with local files, after you enable it in `chrome://extensions`. You can inspect the JSON by typing `json` into the console.

You can install the extension by going [here for Chrome](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en) and [here for Firefox](https://addons.mozilla.org/en-US/firefox/addon/basic-json-formatter/) and then test it, for example, by visiting this [API response](https://efa.mvv-muenchen.de/ng/XSLT_DM_REQUEST?outputFormat=JSON&language=en&stateless=1&coordOutputFormat=MRCV&useRealtime=1&zope_command=enquiry&type_dm=stop&name_dm=Zugspitzstra%C3%9Fe&itOptionsActive=1&ptOptionsActive=1&mergeDep=1&useAllStops=1&mode=direct&anyMaxSizeHitList=10000&useAllStops=1).

This is what it looks like, before formatting:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-134.png align="left")

Now, take a look at the beautiful JSON response you get with [JSON Formatter](https://github.com/callumlocke/json-formatter):

![Image](https://cdn-images-1.medium.com/max/1600/1*c_9u3i-WVKnhGZsd5UZ6Rw.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-135.png align="left")

Here is a pro tip: Hold down CTRL (or CMD on Mac) while collapsing a tree, if you want to collapse all its siblings too.

It is an open-source project, so you can view its [source code on GitHub](https://github.com/callumlocke/json-formatter).

Thanks for reading.
