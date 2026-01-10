---
title: How to hack your Mac and give it the gorgeous wallpapers it truly deserves
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-11T23:33:33.000Z'
originalURL: https://freecodecamp.org/news/this-is-the-wallpaper-your-mac-truly-deserves-with-a-bit-of-coding-f3149bbeb51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kEVDB5B2KX5_O69b0ccLPQ.jpeg
tags:
- name: Apple
  slug: apple
- name: Photography
  slug: photography
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Aakaash Jois

  Let’s face it. The default wallpapers on the Mac gets boring after a few weeks.
  And setting new wallpaper manually is tiresome. Well, what if I told you that I
  got my Mac greet me with a brand new, high resolution wallpaper every time...'
---

By Aakaash Jois

Let’s face it. The default wallpapers on the Mac gets boring after a few weeks. And setting new wallpaper manually is tiresome. Well, what if I told you that I got my Mac greet me with a brand new, high resolution wallpaper every time I flip it open?

If you’re a Chromecast user, you may be familiar with [Chromecast Backdrop](https://www.google.com/chromecast/backdrop/). Backdrop allows the Chromecast to display a slideshow of beautiful photos when it’s idle.

While most users default to Facebook to post photos, a lot of photographers use Google+ to publish their work. Google selects some of these best photos to create brilliant slideshows.

For a long time, this was exclusive to ChromeCast user. But a few months ago, Google released a nifty app for Mac called [Google Featured Photos](https://plus.google.com/featuredphotos).

You may be wondering why my title says “wallpaper” but then links to a “Screen Saver” app. Well, there’s the little trick. On a Mac, any screen saver can be made to run as a wallpaper with just one line of code.

First, you have to download and install the [Google Featured Photos Screen Saver](https://plus.google.com/featuredphotos). Next, go to _System Preferences_ → _Desktop & Screen Saver_ and set the _Google Featured Photos_ as the active screen saver. Now it’s time to run the magic code.

![Image](https://cdn-media-1.freecodecamp.org/images/6uI-dPJ4HxwPs-zEr6X2tOaLgd4cVCxJisDG)
_Set Google Featured Photos as Screen Saver_

#### Coding Time!

Fire up Terminal and paste the below line of code. It will set your screen saver as your wallpaper.

```
/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background &
```

#### EDIT: Apple decided to restructure a bit in High Sierra.

![Image](https://cdn-media-1.freecodecamp.org/images/PIf9ZPG2dnz2LDhSVwH8wkXipDvVITqT1J4K)

If you are using High Sierra (or later), the `ScreenSaverEngine.app` has been moved to a different location. Use the code below instead of the one above.

```
/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background &
```

Just replace all occurrences of `Frameworks/ScreenSaver.framework/Resources` with `CoreServices` and you will be good to go!

Cool, right?

The problem with running just that line of code is that if you close the Terminal window — or if your Mac goes to sleep — the screen saver closes and your wallpaper goes back to whatever it was by default. To handle this, we need to go a bit deeper.

To detect when the Mac sleeps and wakes up, we need a small piece of software called “Sleepwatcher.” You can download it [here](http://www.bernhard-baehr.de/sleepwatcher_2.2.tgz). Just open the file and your Mac will extract the downloaded file (sometimes it might have to be extracted twice). After extracting, you’ll get a “sleepwatcher_2.2” folder. Just move this folder to Desktop and run the following lines of code in the Terminal.

```
sudo mkdir -p /usr/local/sbin /usr/local/share/man/man8
```

You might need to enter your password after pasting this line. Next, run:

```
sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher /usr/local/sbin
```

Then run:

```
sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher.8 /usr/local/share/man/man8
```

Awesome! You have successfully installed Sleepwatcher.

Now let’s add the lines of code needed to make Sleepwatcher run the screen saver when your Mac wakes up, and kill the screen saver when your Mac goes to sleep.

Sleepwatcher searches for and runs two files, `.sleep` when the Mac sleeps, and `.wakeup` when the Mac wakes up. We just need to create these 2 files in the user’s Home Directory.

In the Terminal, type `nano ~/.wakeup` then paste the below code.

```
#!/bin/bashosascript -e 'do shell script "/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background & EOF"'
```

Now press **Control + X** to exit. When it asks if you want to save the file, press **Y** and then press the enter key to confirm the file name. This will create the `.wakeup` file. Now to create the `.sleep` file.

![Image](https://cdn-media-1.freecodecamp.org/images/bAhqA6gKmCsnH2MBP7bdHc4yEox2raRLTATj)
_The .wakeup file_

Just like above, type `nano ~/.sleep` and paste the below code.

```
#!/bin/bash
```

```
osascript -e 'do shell script "kill `ps -ax | grep [S]creenSaver | cut -c1-6` EOF"'
```

Again, press **Control + X** to exit, **Y** to save, and then the enter key to confirm the file name. Now the `.sleep` file will be created.

![Image](https://cdn-media-1.freecodecamp.org/images/oGnweS4gcVcIWtmisaePYhRDrlTgahBL3U6h)
_The .sleep file_

In Terminal, run the below line of code.

```
chmod 700 ~/.sleep ~/.wakeup
```

It changes the permissions for the newly created files so that it can be run by Sleepwatcher.

Now that you’ve created the scripts, you just need to add Sleepwatcher to `launchd` so that it can start when the system starts, then continue to run in the background. Paste the following code code into your Terminal.

```
cp ~/Desktop/sleepwatcher_2.2/config/de.bernhard-baehr.sleepwatcher-20compatibility-localuser.plist ~/Library/LaunchAgents
```

This will copy the Sleepwatcher property list file so that it can be added to `launchd`. Now just paste the code below into Terminal to add Sleepwatcher to `launchd`.

```
launchctl load ~/Library/LaunchAgents/de.bernhard-baehr.sleepwatcher-20compatibility-localuser.plist
```

Awesome! You can now restart your Mac and the `launchd` will run the Sleepwatcher scripts at the startup. Just put your Mac to sleep and wake it up. Then you’ll be welcomed with a beautiful wallpaper.

![Image](https://cdn-media-1.freecodecamp.org/images/SdQIhifPuCV8vx-vSgqLlgLHmNDTpM59Weqa)
_Example of the newly installed Wallpaper_

If you want to uninstall everything and go back to default, follow the link below.

[**To uninstall, run the following lines in Terminal one by one.**](https://medium.com/@aakaashjois/to-uninstall-run-the-following-lines-in-terminal-one-by-one-299916c8ff3b)  
[_After running these, you can uninstall the Google Screen Saver and restart your Mac. It should be removed. Let me know…_medium.com](https://medium.com/@aakaashjois/to-uninstall-run-the-following-lines-in-terminal-one-by-one-299916c8ff3b)

I hope you enjoyed this short tutorial, and enjoy these beautiful wallpaper photos. If you liked this, hit the ❤️ and stay tuned for more.

