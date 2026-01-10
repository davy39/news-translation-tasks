---
title: Python Automation Scripts You Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-03T18:36:39.000Z'
originalURL: https://freecodecamp.org/news/python-automation-scripts
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Python-Automation-Scripts-You-Should-Know.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  We all have those same old boring tasks that we do over and over again. Fortunately,
  we can automate some of these processes so that we can focus on doing other things
  that really need our energy and attention.

  In this article, we w...'
---

By Shittu Olumide

We all have those same old boring tasks that we do over and over again. Fortunately, we can automate some of these processes so that we can focus on doing other things that really need our energy and attention.

In this article, we will talk about some Python automation scripts that you can easily use to perform automation tasks. It's important to understand that they are all ready-made codes which can help us take care of many of our daily repetitive tasks.

I strongly recommend that you have some prior experience with the Python programming language before continuing with this article. 

Shall we begin?

%[https://tenor.com/bTCas.gif]

## How to Automate Python Proofreading

The first on the list is proofreading. Whenever you want to eliminate grammar and spelling mistakes from your writing, you can try this project that uses the `Lmproof` module.

```python
# Python Proofreading
# pip install lmproof
import lmproof
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))
    
proofread("Your Text")
```

First, you'll need to install the `lmproof` library for this automation. Then you can use the function `proofread()` which takes in `text` as a parameter. The function runs and prints the original text that was passed into the function as well as the corrected text. You can use it to quickly proofread an essay or a short article.

## How to Automate Playing Random Music

While working, many devs love listening to music. So for music lovers (like me), this script randomly picks a song from a folder containing songs and plays it with the help of the `OS` and `random` modules in Python.

```python
import random, os
music_dir = 'E:\\music diretory'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[0])) 
```

The code goes to the music directory containing all the songs you want to play, and puts them all in a list. Then it randomly plays each song one after the other. The `os.startfile` plays the song. 

## Automatic PDF to CSV Converter

Sometimes you'll need to convert `pdf` data to `CSV` (comma separated value) data so you can use it for further analysis. In those cases, this script can come in handy.

```python
import tabula

filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')

df.to_csv('output.csv')
```

You'll need to install the `tabula` library using `pip` in order to run this code. After installation you can pass the file into your project. 

The library comes with a function `read_pdf()` which takes the file and reads it. You finish the automation by using the `to_csv()` function to convert the output into CSV.

## Automatic Photo Compressor

You can also decrease the size of a picture by compressing it – while still keeping its quality. 

```python
import PIL
from PIL import Image
from tkinter.filedialog import *

fl=askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality = 10)
```

You can use the PIL (Python Imaging Library) to manipulate images, add filters, blurring, sharpening, smoothing, edge detection, compressing images and doing a lot to images.

## Automatic YouTube Video Downloader

Here's an easy automated script for downloading YouTube videos. Simply use the code below to download any video without the need for any websites or apps.

```python
import pytube

link = input('Youtube Video URL')
video_download = pytube.Youtube(link)
video_download.streams.first().download()
print('Video Downloaded', link)
```

The pytube library is a very easy and simple library you can use to download YouTube videos to your local computer. All you need to do is input the link to the video and then the `download()` method downloads it to your computer.

## Automatic Text to Speech

We will make use of the Google Text to Speech API for this script. The API is up to date and works with many languages, pitches, and voices, that you can select from.

```python
from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('Like This Article')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()
```

## How to Automatically Convert Images to PDF

This is a very common task that you may perform often. You may want to convert a single image or multiple images into a PDF. 

How to convert a single image to a PDF:

```python
import os
import img2pdf
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))
```

How to convert multiple images to PDF:

```python
from fpdf import FPDF
Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("result.pdf", "F")
```

Here we're using the `image2pdf` library in Python to convert our image to a PDF. We can also convert multiple images to PDFs with just a few lines of code.

## Automatic Plagiarism Checker

Plagiarism is the act of representing another person's words or ideas as your own, with or without that person's permission, by integrating them into your work without giving the original author due credit. 

This script can be quite helpful when you want to check for plagiarism between two files.

```python
from difflib import SequenceMatcher
def plagiarism_checker(f1,f2):
    with open(f1,errors="ignore") as file1,open(f2,errors="ignore") as file2:
        f1_data=file1.read()
        f2_data=file2.read()
        res=SequenceMatcher(None, f1_data, f2_data).ratio()
        
print(f"These files are {res*100} % similar")
f1=input("Enter file_1 path: ")
f2=input("Enter file_2 path: ")
plagiarism_checker(f1, f2)
```

## How to Make URLs Shorter

Large URLs can be quite annoying to read and share. To shorten the URLs, this script makes use of a third-party API.

```python
from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import sys

def make_tiny(url):
	request_url = ('http://tinyurl.com/app-index.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()
    

'''

-----------------------------OUTPUT------------------------
python url_shortener.py https://www.wikipedia.org/
https://tinyurl.com/bif4t9

'''
    
```

## Internet Speed Tester

The OOKLA speed test API allows you to check the ping and internet speed. In addition to measuring the ping, this little automated project will measure the download and upload speeds.

```python
# Internet Speed tester
# pip install speedtest-cli
import speedtest as st

# Set Best Server
server = st.Speedtest()
server.get_best_server()

# Test Download Speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {down} Mb/s")

# Test Upload Speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {up} Mb/s")

# Test Ping
ping = server.results.ping
print(f"Ping Speed: {ping}")

```

Although there are alternatives like [fast.com](https://www.freecodecamp.org/news/p/596c046e-0ba5-4a99-bf4d-eb3e0bebe75c/www.fast.com), with this script you can quickly check for the internet speed using a Python script.

## Conclusion

We have talked about ten Python automation scripts in this article, and I hope you've found it useful. You can also go the extra mile to check out the libraries used and expand your knowledge.

Lets connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.freecodecamp.org/news/p/596c046e-0ba5-4a99-bf4d-eb3e0bebe75c/linkedin.com/in/olumide-shittu).

Happy Coding!

