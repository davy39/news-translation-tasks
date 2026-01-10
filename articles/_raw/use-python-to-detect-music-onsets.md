---
title: How to Use Python to Detect Music Onsets
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-07-22T16:56:17.000Z'
originalURL: https://freecodecamp.org/news/use-python-to-detect-music-onsets
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Python-Music-Onset-Detection.png
tags:
- name: music
  slug: music
- name: Python
  slug: python
seo_title: null
seo_desc: 'In music terminology, an onset refers to the beginning of a musical note
  or other sound. In this post, we will look at how to detect music onsets with Python''s
  audio signal processing libraries, Aubio and librosa.

  This tutorial is relevant even if yo...'
---

In music terminology, an **onset** refers to **the beginning of a musical note or other sound.** In this post, we will look at how to detect music onsets with Python's audio signal processing libraries, [Aubio](https://aubio.org/) and [librosa](https://librosa.org/doc/latest/index.html).

This tutorial is relevant even if your application doesn't use Python - for example, you are building a game in Unity and C# which doesn't have robust libraries for onset detection.

If that is the case, you may export the detected onset timestamps to a text file to read into your engine of choice.

If you prefer a video tutorial to an article, here's the video version of this tutorial.

%[https://youtu.be/aMMI0nAKgI0] 

## Applications of Music Onset Detection

I came across this music onset detection technique when I was building **a rhythm game** and wanted a way to **automatically** generate beat maps for any song.

Check out the end of this article for my [open-source rhythm game](https://github.com/RuolinZheng08/renpy-rhythm) and [my step-by-step course on how I built it.](https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973)

![Image of a rhythm game similar to Guitar Hero](https://www.freecodecamp.org/news/content/images/2021/07/ezgif.com-gif-maker.gif align="left")

*My rhythm game showcase*

Besides building a rhythm game, this technique has a lot of other applications.

For example, detecting onsets is usually the first step in **music information retrieval and analysis**.

Another example could be that we are building a game in which there are combat scenes. We may detect the onsets in the BGM and spawn an enemy at every onset. This can create a unique pacing in our game.

I'll demonstrate how to detect music onsets using two different Python packages for **audio signal processing**, [Aubio](https://aubio.org/) and [librosa](https://librosa.org/doc/latest/index.html). Both packages detect onsets pretty accurately. The small difference is that librosa works for the **OGG** format while Aubio doesn't.

## How to Set up the Development Environment

We will be installing our packages in a virtual environment.

In the command line, we create a virtual environment named `python-aubio-librosa` as follows. `-m` stands for `module`.

```pgsql
$ python3 -m venv python-aubio-librosa
```

Then we activate the virtual environment:

```pgsql
$ . python-aubio-librosa/bin/activate
```

Note that if you try to activate the environment using the following command, you will get an error:

```pgsql
$ ./python-aubio-librosa/bin/activate
-bash: ./python-aubio-librosa/bin/activate: Permission denied
```

Once your environment is activated, the name of the environment will show in parentheses:

```pgsql
(python-aubio-librosa) $ ...
```

We can check that if we invoke `python` or `pip`, the invoked programs will be those in our virtual environment instead of the system-level ones.

If we haven't activated our environment, the output will point to the system-level programs.

```pgsql
$ which python
/usr/bin/python
$ which pip
/usr/local/bin/pip
```

Once we have activated our environment, the output will point to the local ones.

```pgsql
(python-aubio-librosa) $ which python
/Users/USERNAME/Desktop/python-aubio-librosa/bin/python
(python-aubio-librosa) $ which pip
/Users/USERNAME/Desktop/python-aubio-librosa/bin/pip
```

## How to Install and Use Aubio

We will install Aubio via `pip`:

```pgsql
(python-aubio-librosa) $ pip install aubio
```

The function that we will use to generate a list of onset timestamps as floating point numbers in seconds is as follows. This function comes from Aubio's [official documentations](https://github.com/aubio/aubio/blob/master/python/demos/demo_onset.py), so we can just use it without learning about the nitty-gritty details (like FFT, Fast-Fourier Transformations) in audio signal processing.

```python
from aubio import source, onset

def get_onset_times(file_path):
    window_size = 1024 # FFT size
    hop_size = window_size // 4

    sample_rate = 0
    src_func = source(file_path, sample_rate, hop_size)
    sample_rate = src_func.samplerate
    onset_func = onset('default', window_size, hop_size)
    
    duration = float(src_func.duration) / src_func.samplerate

    onset_times = [] # seconds
    while True: # read frames
        samples, num_frames_read = src_func()
        if onset_func(samples):
            onset_time = onset_func.get_last_s()
            if onset_time < duration:
                onset_times.append(onset_time)
            else:
                break
        if num_frames_read < hop_size:
            break
    
    return onset_times
```

Then, we write a `main` function that takes in the path to an audio file, and outputs the onset timestamps to a file, keeping the first four decimal places in each float, one float per line.

```python
def main():
    file_path = '../game/audio/my-music.mp3'
    onset_times = get_onset_times(file_path)
    # remove extension, .mp3, .wav etc.
    file_name_no_extension, _ = os.path.splitext(file_path)
    output_name = file_name_no_extension + '.beatmap.txt'
    with open(output_name, 'wt') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
```

Let's invoke the script from the command line. Aubio might raise a warning about accuracy but my experimentation shows that Aubio is still pretty accurate.

```pgsql
(python-aubio-librosa) $ python generate_beatmap_aubio.py 
[mp3 @ 0x7fe671031e00] Estimating duration from bitrate, this may be inaccurate
```

An example output file would look like below. For a short 15-second music clip, Aubio detected 26 onsets. These are the timestamps that we can use for our application.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-13.54.18.png align="left")

*An example output file consisting of onset timestamps*

And that's it for Aubio.

## How to Install and Use Librosa

Similar to Aubio, we will install librosa also via `pip`:

```pgsql
(python-aubio-librosa) $ pip install librosa
```

Compared to Aubio, librosa's library methods are easier to use. `librosa.load` returns a NumPy array `x` and a sampling rate `sr`, which we pass to `librosa.onset.onset_detect` to get a list of onset frames.

Finally we convert onset frames into onset timestamps, and write each timestamp to an output file like we did for Aubio.

```python
import librosa

def main():
    file_path = '../game/audio/my-music.ogg'
    x, sr = librosa.load(file_path)
    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    # remove extension, .mp3, .wav etc.
    file_name_no_extension, _ = os.path.splitext(file_path)
    output_name = file_name_no_extension + '.beatmap.txt'
    with open(output_name, 'wt') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
```

The output file will be in the same format as shown above for Aubio.

## Conclusion

Thanks for reading and I hope you are ready to apply this onset detection technique to your next project. 🎶

As a recap of the differences between Aubio and Librosa, both detect onsets pretty accurately based on my experimentation.

Aubio is more restricted in terms of audio file formats: it raises a warning about accuracy for MP3 files and doesn't handle OGG files.

On the flip side, Librosa is able to handle most common audio file formats: MP3, OGG, FLAC, and M4A. Librosa's library interface is also easier to use than Aubio's, especially for those of us who aren't pros in signal processing.

Check out the resources below if you'd like to learn more or get inspired for your next project!

## Resources

You can check out the code used in this tutorial [on my GitHub](https://github.com/RuolinZheng08/renpy-minigames101/tree/master/generate_beatmap) or [watch the video version of this tutorial on YouTube.](https://youtu.be/aMMI0nAKgI0)

If you are interested in building a rhythm game, check out [my open-source one built in Python on GitHub](https://github.com/RuolinZheng08/renpy-rhythm) and my Udemy course in which we will build the game from the ground up.

%[https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973] 

If you'd like to know whether the course is for you, check out my course promotional video on YouTube and [free sample lectures on Udemy.](https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973)

%[https://youtu.be/_AaUKSjTNY8] 

My YouTube channel also features other fun project tutorials like [building a Discord AI Chatbot](https://youtu.be/UBwvFuTC1ZE), and, [a series of coding interview crash courses](https://youtu.be/H2gnD7Ixeao) I'm developing. Hope to see you there!

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]
