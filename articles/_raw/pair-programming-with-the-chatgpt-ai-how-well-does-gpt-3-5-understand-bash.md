---
title: Pair Programming with the ChatGPT AI – Does GPT-3.5 Understand Bash?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2022-12-16T17:51:07.000Z'
originalURL: https://freecodecamp.org/news/pair-programming-with-the-chatgpt-ai-how-well-does-gpt-3-5-understand-bash
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-pavel-danilyuk-8438951.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Bash
  slug: bash
- name: Chat
  slug: chat
seo_title: null
seo_desc: "We've been hearing a lot about artificial intelligence and natural language\
  \ processing – and in particular about the latest version of OpenAI's GPT – for\
  \ weeks. \nThe recent release of GPT 3.5, and specifically the very new ChatGPT\
  \ tool, is definitely..."
---

We've been hearing a lot about artificial intelligence and natural language processing – and in particular about the latest version of OpenAI's GPT – for weeks. 

The recent release of GPT 3.5, and specifically the very new ChatGPT tool, is definitely a huge leap forward.

You may have read about people asking the AI to draw up real estate contracts and wills, and even generate programming code. This article approaches the tool from a slightly different perspective. 

You can watch a video version of this article here if you'd like to use it to supplement your learning:

%[https://www.youtube.com/watch?v=GxJKuINwPSw]

## Experimenting with ChatGPT and Bash Scripting

I decided to see how ChatGPT handles Linux Bash scripting. But (spoiler alert!) as I worked through the tool's suggestions - both good code and bad code - I began to realize that there was an even more powerful benefit staring me in the face: an opportunity to pair-program with an eminently helpful partner.

The AI ultimately failed to solve my problem, but the _way_ it failed was absolutely fascinating. And watching the AI searching for new answers was absolutely crazy.

### First Attempt – ChatGPT Tries to Solve the Problem

So let's see how it all happened. Here, more or less, is the initial prompt I provided to the AI:

> Write me a Bash script that prompts for the URL of a YouTube video and then uses the yt-dlp program to download from that URL. The script should then change the file name to "myvideo.mp4"

After a few seconds, the ChatGPT told me that a script was coming. Here's how that code looked:

```
#!/bin/bash

# Prompt user for YouTube video URL
read -p "Enter YouTube video URL: " url

# Download video from YouTube using yt-dlp
yt-dlp $url

# Get the name of the downloaded video file
yt-dlp $url

# Change the downloaded video filename to "myvideo.mkv"
mv video-filename.mp4 myvideo.mp4
```

The AI obviously knows what Bash scripts are and how to present code. It even did a great job commenting each line of code. The AI knows how to properly prompt the user for input and then how to import the input string into a variable called `url`. 

It also knows about the yt-dlp program and how it works, appropriately feeding it the URL that was provided. Then it at least attempted to rename the downloaded video file to myvideo.mp4. But everything kind of broke down when it assumed that the download filename would be video-filename.mp4. Whoops.

At any rate, the AI helpfully showed me how to create the script from its code and then run it.

### Second Attempt – ChatGPT Corrects Itself

My first follow-up prompt pointed out the obvious mistake and, after a few seconds, ChatGPT admitted it was wrong and offered an improvement. 

> You're right, the script I provided would not work as expected because it assumes that the downloaded video will be saved to a file with the name `video-filename.mp4`. However, this is not guaranteed to be the case. To fix this...

It's just mind-blowing how the AI is completely engaged in the process here. It remembers its first code, listens to and understands my complaint, and thinks through a solution. Here's that second attempt:

```
#!/bin/bash

# Prompt user for YouTube video URL
read -p "Enter YouTube video URL: " url

# Download video from YouTube using yt-dlp
yt-dlp $url

# Get the name of the downloaded video file
filename=$(basename $url)

# Change the downloaded video filename to "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

Ok, so I can see how the solution kind of looked right. `basename` is a Linux tool that can strip out file system directories and leave nothing but the actual filename.

The problem is that the variable `url` doesn't contain a local filename, but an internet address. This one definitely isn't going to work.

### Third Attempt – ChatGPT Tries Again

So I tried again, explaining how that wasn't the right tool for the job. And ChatGPT gives it another try. 

```
#!/bin/bash

# Prompt user for YouTube video URL
read -p "Enter YouTube video URL: " url

# Extract the filename from the URL
filename=$(basename $url)

# Download the video using the yt-dlp tool and specify the filename
yt-dlp -o $filename $url

# Change the downloaded video filename to "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

This time, it shows that it had familiarized itself with the yt-dlp documentation, suggesting that we use the `-o` argument to give the downloading video a name, against which `basename` should now work. With each iteration, the AI gives me this updated code for my cutting and pasting pleasure.

Of course, that wasn't going to work either. With the next attempt, I get the feeling that the AI is a bit desperate. 

### If At First You Don't Succeed...At Least You'll Learn Something

I'm going to skip past the next attempt or two, as we ran into a side problem: Videos coming from YouTube aren't always MP4s, they're sometimes MKVs or even WEBMs. That uncertainty could mess with the filenames we're working with, so I asked ChatGPT to work that into the code. 

```
#!/bin/bash

# Prompt user for YouTube video URL
read -p "Enter YouTube video URL: " url

# Extract the filename from the URL
filename=$(basename $url)

# Download the video using the yt-dlp tool and specify the filename
yt-dlp -F mp4 -O $filename $url

# Change the downloaded video filename to "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

When I reported how that, too, wouldn't work, the AI started to get confused. First it told me that the `-F` option was expecting a valid video format, but that "mp4" wasn't valid. Then it gives me valid options, including "mp4".

When nothing the AI suggested worked, it gave up, advising me to make sure that yt-dlp was actually installed on my machine and showing me how to do that. 

I figured that was a good time to give up. It was a surprisingly good effort and, even if it didn't solve the problem, it did show me some useful syntax and got me thinking.

In case you're interested, by the way, here's how an actual working script would look. 

```
#!/bin/bash

# Prompt user for YouTube video URL
read -p "Enter YouTube video URL: " url

# Download video from YouTube using yt-dlp
yt-dlp $url

# Get the name of the downloaded video file
original_filename=$(ls | awk '/mp4/ || /webm/ || /mkv/')

# Change the downloaded video filename to "myvideo.mkv"
mv "$original_filename" /home/ubuntu/vids/myvideo.mp4
```

The first two lines of code are just the way ChatGPT suggested. But I then isolate the filename by listing all the files in the current directory and using `awk` to filter for only filenames containing either mp4, webm, or mkv. (This assumes that there will never be more than one video file in the directory at a time.) 

The filename will then be written to the `original_filename` variable. I'll then use that variable as part of a `move` command to rename the file `myvideo.mp4` As far as I can tell, that'll work no matter what format was actually sent.

## Wrapping Up

Artificial intelligence might not be quite ready for real-world programming tasks today, but I wouldn't want to bet against it getting there tomorrow...or some time next year. 

In the meantime though, I would absolutely recommend engaging with tools like ChatGPT whenever you're faced with a challenging programming task. 

Two minds are (almost) always better than one.

_Besides my [my YouTube channel](https://www.youtube.com/@davidbclinton) (to which you can subscribe), [my website](https://bootstrap-it.com) links to all kinds of technology goodness available as articles, books, and courses._

