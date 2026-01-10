---
title: Wav File Format – How to Open a Wav and Convert Wavs to MP3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T18:46:16.000Z'
originalURL: https://freecodecamp.org/news/wav-file-format-how-to-open-a-wav-and-convert-wavs-to-mp3
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Untitled-design.jpg
tags:
- name: audio
  slug: audio
- name: how-to
  slug: how-to
seo_title: null
seo_desc: 'By Vaibhav Kandwal

  Audio is a very important part of any digital media. Since audio or sound is a wave
  (a literal, continuous wave) it is analog in nature. This means that it cannot be
  stored and processed by the computer directly, as a computer only...'
---

By Vaibhav Kandwal

Audio is a very important part of any digital media. Since audio or sound is a wave (a literal, continuous wave) it is analog in nature. This means that it cannot be stored and processed by the computer directly, as a computer only understands digital signals. 

So naturally, engineers found a way to convert these analog signals into digital signals. They've also developed a method to save them in digital format. I'm talking about audio codecs.

Audio codecs, in simpler terms, are just encoders and decoders (_co_ - coders, _dec_ - decoders, or _co_ - compressor, _dec_ - decompressor). They can be implemented as hardware codecs, which encode analog audio to digital audio and vice versa. 

An example of such codecs are sound cards in your computer, which have built-in analog-to-digital (ADC) and digital-to-analog (DAC) circuits.

 The software counterpart is an algorithm that compresses and decompresses digital audio. Some examples of such codecs are MP3, FLAC, WAV, and AAC.  
  
Today, we'll be looking at software encoders and we'll focus our attention on the WAV format.

## What compression means in audio codecs

Audio compression algorithms are divided into two categories: _Lossless_ and _Lossy_. So what's the difference between these two?

### Lossless algorithms

These algorithms may perform some kind of compression on the audio, but it doesn't remove any audio data, thus nothing is lost. The tradeoff is that you have very large file sizes.

### Lossy algorithms

In this type of compression, some part of audio fidelity, deemed inaudible/indistinguishable to human ears, is removed or has its fidelity (or accuracy or loudness) reduced. Compression is also performed after this step. [You can read more about it here](https://en.wikipedia.org/wiki/Data_compression#Lossy_audio_compression).

Unless you have a very good HI-FI sound system that can reproduce those extra fidelity sounds, you should go for lossy. It will save space and remove extra data that you might never even hear.

Now that you understand audio compression, let's move on to the main topic of this article.

## What is WAV?

WAV (or WAVE) stands for Waveform Audio File Format. It was developed by IBM and Microsoft. The file extension is `.wav` or `.wave`. 

The WAV format is widely used where you would want uncompressed audio. For example, sound engineers use it a lot – and due to its lossless form, it can be used for early production samples. 

The large file size means that it's usually not suitable for transmission over the internet. Other formats like MP3 and AAC offer much smaller file sizes, as they are lossy.

### Limitations of the WAV format

WAV files are limited to 4GB in size as they have a 32bit file size header. W64 is a successor which has a 64bit header, allowing even larger file sizes.  
  
Apart from that, since the audio is uncompressed, its file size is large. So if the audio is stored on a slow disk drive, it can cause buffering issues (as audio needs to be loaded from disk to RAM before the music player can decode and play the file). 

This might not be an issue, however, on modern computers, as they have much faster disks drives.

## How to open a WAV file

Since WAV is quite a popular format, almost all devices today support it using built-in media players. 

* On Windows, the Windows Media Player is capable of playing WAV files.
* On MacOS, iTunes or QuickTime can play WAV files.
* On Linux, your basic ALSA system can play these files.

Other solutions also exist which can help you play WAV files, such as the VLC media player or any other music players.

### How to Play a WAV file on Windows using Windows Media Player

1. Open Windows Media Player using Search

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-140.png)
_step 1: windows search_

2.  Drag and drop your WAV audio file from explorer to Windows Media Player

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc.gif)
_step 2: drag and drop your audio_

3. Click Play!

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-1.jpg)
_step 3: click play_

### How to Play a WAV file on any OS with VLC Media Player

VLC media player is an open-source media player that can play most of your file formats without needing to download external codecs. It is cross platform, too, so you'll get the same features and interface across all operating systems, whether you use Linux, Windows, or MacOS (also supports Android and iOS). 

Here are the steps to play an WAV file with VLC on your PC.

1. Download VLC from the official website [here](https://www.videolan.org/)
2. Open VLC
3. Click on Media, then select Open File

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-2-1.jpg)
_step 3: click on 'media', then click 'open file'_

4.  In the file picker dialog, choose your audio, click `Open` and the WAV file should start playing automatically!

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-3.jpg)
_step 4: select your file and click 'open'_

 Or if you prefer a GIF:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc2.gif)
_Step 1-4 for VLC :D_

## How to convert WAV file**s** to MP3

Depending on the end device, you might want to convert WAV to other formats, for example to save disk space or if you're listening on a low end device.

MP3 is quite a good format for storing audio. It gives you 50-75% smaller file sizes, while retaining almost the same listening experience. Let's see how you can convert these files.

### Online Convertors

If you only convert audio on rare occasions, I would suggest that you to use an online convertor such as [CloudConvert](https://cloudconvert.com/wav-converter). And Google is your friend here. 

Do keep in mind that these online convertors can store your files for some time (even forever), so read their policy if you want to convert something mission critical.

### Offline Convertors

Another option is to convert these files locally. This will help you if you want to convert frequently or have something that you don't want to expose to the internet.  
  
There are two ways to do this:

**[Audacity](https://www.audacityteam.org/)**: Audacity is a free, open-source cross-platform application that allows you to edit and convert audio. 

The only con is you have to do some initial setup first (installing LAME). Also you have to convert files one by one. 

**[FFmpeg](https://ffmpeg.org/)**: FFmpeg is a cross-platform command line tool to convert audio and video files. You can run the following command to convert a wav file to mp3:  
`ffmpeg -i input.wav output.mp3`

You can dig around FFmpeg's docs to figure out how to customize some parameters and pass a list of files for batch conversions.

The main con is that FFmpeg is not user friendly. You need to know how to use command line tools. Though stuff like a FFmpeg GUI exists, it is out of the scope of our discussion here.

### Thanks for reading!

I hope this article gave you some insights into audio compression, as well as how to play around with and convert WAV files. 

For any questions or comments, you can find me on Twitter [@vaibhav_kandwal](https://twitter.com/vaibhav_kandwal). Thank you for reading.

