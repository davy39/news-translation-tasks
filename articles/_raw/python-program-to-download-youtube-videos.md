---
title: How to Build a Python Program to Download YouTube Videos
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2022-11-14T15:56:27.000Z'
originalURL: https://freecodecamp.org/news/python-program-to-download-youtube-videos
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-christina-morillo-1181671.jpg
tags:
- name: Python
  slug: python
- name: Script
  slug: script
- name: youtube
  slug: youtube
seo_title: null
seo_desc: "YouTube is a well-known internet video streaming service. There are millions\
  \ of videos in categories such as education, entertainment, and travel. \nYou can\
  \ quickly watch videos with a few mouse clicks, but downloading videos is difficult.\
  \ But in a re..."
---

YouTube is a well-known internet video streaming service. There are millions of videos in categories such as education, entertainment, and travel. 

You can quickly watch videos with a few mouse clicks, but downloading videos is difficult. But in a recent upgrade, YouTube now allows you to save videos in its download folder for offline viewing. Still, you are unable to save them locally.

In this tutorial, you will learn how to use Python code to download YouTube videos. As you may know, one of Python's great strengths is its huge number of modules and libraries. We will write the Python script using the popular pytube package.

## Prerequisites

Below are the basic requirements to proceed with this tutorial:

* Understanding of the Python Programming language
* You must have Python 3+ installed on your computer
* You must have installed the Python library Pytube
* You should have a Python code editor such as Pycharm, Vscode, and so on.

## Pytube Overview and Installation

Pytube is a small, dependency-free Python module for accessing videos from the internet.

The native library is not pytube – you must first install it to be able to use it. When you have pip, installation is simple.

To install Pytube using pip, you will need to open your command prompt CLI as an administrator and enter the following command:

```
pip install pytube


```

The pytube library improves video downloads. Build the YouTube module's object by supplying the URL as a parameter. Then, obtain the video's proper extension and resolution. You can change the name of the file at your leisure – otherwise, the original name will be retained.

Now let's get to the main aspect of writing and implementing the code to download our favorite videos from YouTube.

```
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

```

You use the `from pytube import YouTube` function to import the Python Pytube library before continuing with the other aspects. Then you define the function download link.

The `youtubeObject = youtubeObject.streams.get_highest_resolution()` command will automatically download the highest resolution available.  
Then I implemented the Try and Except to return an error message if the download fails – else it will print out that the download is completed successfully.

The Link function will ask for the preferred YouTube video link to download, then immediately after you hit the enter button, the video downloading will commence.

### The Output:

![Image](https://paper-attachments.dropboxusercontent.com/s_2A6E5F7B9EF3D136021C2A8815B8956B830A35B9A863E60136A6FD8F4C45E374_1666119447422_pytube.PNG)

The video I downloaded was successful. You can see the video in the same Python folder where the file you are working on is located. But if you wish, you can then move the video to your preferred storage location. In my case the video name is "Ronaldo celebrates with Antony.mp4."

However, it would be preferable if you had a reliable internet connection. 

This library also has numerous sophisticated features, but we have covered all of the major ones. You can learn more about the pytube library by visiting its official [well-written documentation](https://pytube.io/en/latest/).

## Conclusion

We have successfully built a YouTube video downloader script of our own in Python. This helps you avoid the stress of looking for an external website or application to get your preferred video to your local storage. 

It also saves you from having to expose your data on a third-party website or phishing link – all in the name of getting a video from YouTube to your local storage.

Hopefully after going through this article, you will understand the process required to download videos from YouTube without the need to download an external application or visit any website you don't trust.

