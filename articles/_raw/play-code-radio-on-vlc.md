---
title: How to listen to Code Radio in VLC Media Player in just 2 simple steps
subtitle: ''
author: Akarsh Seggemu
co_authors: []
series: null
date: '2019-07-29T21:07:12.000Z'
originalURL: https://freecodecamp.org/news/play-code-radio-on-vlc
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca12d740569d1a4ca4d23.jpg
tags: []
seo_title: null
seo_desc: "I enjoy listening to Code Radio while I'm working. The music helps me focus\
  \ and block out the noise of the surrounding office. \nBut when one of my co-workers\
  \ interrupts my flow to ask a question, I have to switch Code Radio off. \nIt's\
  \ kind of time co..."
---

I enjoy listening to [Code Radio](https://coderadio.freecodecamp.org/) while I'm working. The music helps me focus and block out the noise of the surrounding office. 

But when one of my co-workers interrupts my flow to ask a question, I have to switch Code Radio off. 

It's kind of time consuming to switch over to the Code Radio site to pause the music. You have to figure out which tab Code Radio is playing in so you can pause it.

To overcome this situation, I started opening a separate browser that I only used for playing Code Radio. This made it easier for me since I could just alt+tab back to that browser icon and press Code Radio's spacebar hotkey to pause the music.

But running a separate browser only for playing music felt like a drain on my computer resources. I thought there would be a better solution that wasn't so taxing. 

Since, I started listening to [Code Radio](https://coderadio.freecodecamp.org/), I had largely abandoned Spotify and uninstalled the app. But I remembered how when I used to use Spotify, I was could use the media controls on my keyboard to pause and play the music. This got me thinking.

# A more elegant solution

What if you could play and pause Code Radio with a single hotkey on your keyboard - even if you were in your terminal or your code editor?

Well you can't do that with a browser app. But you can do that with a native app running on your computer. And you may already have this app installed on your computer. It's called VLC, and it's one of the most common media players.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/IMG_20190726_173455644-1.jpg)
_media player buttons on my keyboard_

During my lunch break, I kept thinking on how to make it easy for myself to listen to music and have the ability to play/pause music from my keyboard with the click of a single button i.e. play/pause button. So, I searched in the internet and found out that media players can stream content from any network. 

[This article](https://www.vlchelp.com/access-media-upnp-dlna/) helped me understand how to stream content from any network in VLC.

In order to have the flexibility of using the play/pause button from my keyboard I had to use a media player. I found the [VLC media player](https://www.videolan.org/vlc/index.html) a reliable media player that is available in all platforms and it is open source and free to download.

In my first attempt, I tried to open the Code Radio website page URL: _[https://radio.freecodecamp.org](https://radio.freecodecamp.org)_ in VLC media player.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.02.22.png)
_trying to open code radio from VLC media player._

And VLC media player could not play it. I tried pressing the play button multiple times, but it did not nothing.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.02.40.png)
_unable to play on VLC media player_

After multiple trials, I found that VLC media player requires a music format file (e.g. mp3) and cannot parse the html website :/. the URL needs to be the location of the music format file.

So I went back to the [Code Radio](https://coderadio.freecodecamp.org/) music website page and inspected the website page. I searched for "_mp3_" keyword and found nothing. 

Then I noticed i did not hit the play button for the website to request for the mp3 file to be played. I just tried it (on Firefox), and I don't have to click enter to find the URL of those mp3s.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.01.05.png)
_mp3 file location via inspecting the Code Radio music website page_

There are two [bitrate](https://en.wikipedia.org/wiki/MP3#Bit_rate) options available on [Code Radio](https://coderadio.freecodecamp.org/) music website page.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-29-at-22.05.28.png)
_several mp3 bitrate options_

The mp3 files I saw in the inspect correspond to the [bitrate](https://www.freecodecamp.org/news/play-code-radio-on-vlc/Code%20Radio%20music%20website%20page) option button.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-29-at-22.05.47.png)
_mp3 file locations with their bit rate_

The two bitrates and their file names:

1. 64kbps - low.mp3
2. 128kbps - radio.mp3

In my second attempt, I used the mp3 file location URL: [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326) which I found in the Code Radio music page in the VLC media player. It started to play the music :).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.03.35.png)
_VLC media player playing the mp3 file_

I noticed the unique number at the end of the mp3 file "[?1564340326](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326)". This seem to be unique values created by the back-end server. When I opened the VLC media player in the next day. It was unable to play the Code Radio music. I tried to delete the last values at the end of the mp3 file and it started to play again :).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.23.48.png)

## Steps to play [Code Radio](https://coderadio.freecodecamp.org/) music from [VLC media player](https://www.videolan.org/vlc/index.html)

**Step 1.** Open VLC media player. Then, click on **File**->**Open Network**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-26-at-18.34.07.png)
_Open Network in VLC media player_

**Step 2.** In the **URL** field,  paste this URL: [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3) . Then Click on the **Open** button.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.25.43.png)
_openning the URL from the Network in VLC media player_

Then, [VLC media player](https://www.videolan.org/vlc/index.html) will open the Code Radio network and start playing the music.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.23.48-1.png)

Note: You can use the URL: [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3) in any media player that supports streaming via Network. I tried to play on Quick Time player and it works!

### Other option: Playing via playlist file,

Code radio is powered by AzuraCast and its public player has a "Download PLS" link that will produce a PLS playlist file and it contains all the different bitrates. The playlist file can be played in VLC media player and in other players. 

You can open the playlist file - [https://coderadio-admin.freecodecamp.org/public/coderadio/playlist/pls](https://coderadio-admin.freecodecamp.org/public/coderadio/playlist/pls) in VLC media player and choose the bitrate and start playing the music.

Enjoy listening to [Code Radio](https://coderadio.freecodecamp.org/) music.

Credits: I thank [Quincy Larson](https://twitter.com/ossia), [Buster Neece](https://twitter.com/SlvrEagle23) and [Louis Tsai](https://twitter.com/louis993546) for reviewing this article.

