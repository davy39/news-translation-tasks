---
title: How to Fix Broken Audio in Headphones and Speakers in Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-16T15:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-broken-audio-in-headphones-and-speakers-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--10-.jpg
tags:
- name: audio
  slug: audio
- name: Linux
  slug: linux
seo_title: null
seo_desc: "If you are using the Linux operating system on your desktop, you might\
  \ have faced some audio issues before. Like when you're trying to get sound in your\
  \ speakers when your headphones are connected to the audio jack. \nIf so, no worries!\
  \ It is a pretty..."
---

If you are using the Linux operating system on your desktop, you might have faced some audio issues before. Like when you're trying to get sound in your speakers when your headphones are connected to the audio jack. 

If so, no worries! It is a pretty common issue that you can resolve quickly. In this article, I am going to help you solve the issue completely. I'll be using a well known distro called [Manjaro Linux](https://manjaro.org/), but I believe that the same method is applicable for all Linux distributions.

### Step 1 – Open the terminal / console


![Image](https://www.freecodecamp.org/news/content/images/2022/02/2.png)

### Step 2 – Open Alsamixer
We will use alsamixer to tweak the audio settings. Type `alsamixer` and press the **Enter** key on your keyboard.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/3.png)

Alsamixer will open in your terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/4.png)

### Step 3 – Set Preferred Sound Card

Now you need to select your preferred sound card. For that, simply press the `F6` key on your keyboard. Select the sound card appropriate for you. 

If you are not sure, then you can simply select one of them at a time (press the **Enter** key after selecting the sound card) and try the rest of the methods to see whether that sound card was appropriate or not. For me, it is **default:1 HD-Audio Generic**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/5.png)

The AlsaMixer window will change depending on your selected sound card.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/6.png)

Then press the right arrow (`➜`) key until you find **Auto-Mute Mode**. 

You will see that it is currently **ENABLED**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/7.png)

We need to change it back to **DISABLED**. You have to press the down arrow (`↓`) key to disable it.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/8.png)

Then press the `Esc` key to exit AlsaMixer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/10.png)

### Step 4 – Save Settings

Now we need to save the settings that we just tweaked in AlsaMixer. For that, type `sudo alsactl store`. Now press the **Enter** key.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/11.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/12.png)

Now you are good to go!

If you want to check whether the audio is working in your speakers or not, then you can go to **Settings**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/13.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/14.png)

Then go to **Sound**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/15.png)

If you change your **Output Device**, then you should see that the speaker audio is working perfectly. I am using the **Line Out** option here for my workstation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/16.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/17.png)

Now you should see that the audio issue has been fixed!

**BONUS**: I have also made a complete video tutorial about this and published the [video](https://youtu.be/zCaJ6lcaSOg) on my new YouTube channel.

%[https://youtu.be/zCaJ6lcaSOg]

## Conclusion

I hope this trick helps you if you also face this kind of audio issue in your speakers. Thanks a lot for reading the entire article till now. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

