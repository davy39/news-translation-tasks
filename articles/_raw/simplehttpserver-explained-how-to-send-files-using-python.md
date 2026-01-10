---
title: 'SimpleHTTPServer Explained: How to Send Files Using Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T23:14:00.000Z'
originalURL: https://freecodecamp.org/news/simplehttpserver-explained-how-to-send-files-using-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e01740569d1a4ca3ad4.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "As a web developer, there will be a point when you need to create your\
  \ own local web server. \nMaybe it's because you'll be on a flight and want to work\
  \ on your project, far from internet service. Or perhaps you just want a quick way\
  \ to access files f..."
---

As a web developer, there will be a point when you need to create your own local web server. 

Maybe it's because you'll be on a flight and want to work on your project, far from internet service. Or perhaps you just want a quick way to access files from another computer on your home network. 

Whenever and however the need arises, setting up a local HTTP server is a useful skill to have.

### What is an HTTP server?

Simply put, an HTTP server or web server is a process running on a machine that listens for incoming requests and serves web pages. 

For example, when you type in `https://www.freecodecamp.org/news/` into your browser, there's a server somewhere listening for that request. In response, it sends back data so your browser can render the freeCodeCamp Developer News page.

Of course there's a lot more happening behind the scenes, but for the purposes of this tutorial, that's all you really need to know.

### How to set up a local HTTP server

1. [Install Python](https://www.freecodecamp.org/news/best-python-tutorial/#installation)
2. Open your command prompt or terminal and run `python -V`
3. Go to your project's directory with `cd` on *nix or MacOS systems or `CD` for Windows
4. Run the following commands to start a local HTTP server:

```
# If python -V returned 2.X.X
python -m SimpleHTTPServer

# If python -V returned 3.X.X
python3 -m http.server

# Note that on Windows you may need to run python -m http.server instead of python3 -m http.server
```

You'll notice that both commands look very different – one calls `SimpleHTTPServer` and the other `http.server`. This is just because the `SimpleHTTPServer` module was rolled into Python's `http.server` in Python 3. They both work the same way.

Now when you go to [`http://localhost:8000/`](http://localhost:8000/) you should see a list of all the files in your directory. Then you can just click on the HTML file you want to view.

Just keep in mind that `SimpleHTTPServer` and `http.server` are only for testing things locally. They only do very basic security checks and shouldn't be used in production.

### How to send files locally

To set up a sort of quick and dirty NAS (Network Attached Storage) system:

1. Make sure both computers are connected through same network via LAN or WiFi
2. Open your command prompt or terminal and run `python -V` to make sure Python is installed
3. Go to the directory whose file you want to share by using cd (change directory) command.
4. Go to the directory with the file you want to share using `cd` on *nix or MacOS systems or `CD` for Windows
5. Start your HTTP server with either `python -m SimpleHTTPServer` or `python3 -m http.server`
6. Open new terminal and type `ifconfig` on *nix or MacOS or `ipconfig` on Windows to find your IP address

Now on the second computer or device:

1. Open browser and type in the IP address of the first machine, along with port 8000: `http://[ip address]:8000`

A page will open showing all the files in the directory being shared from the first computer. If the page is taking too long to load, you may need to adjust the firewall settings on the first computer.

