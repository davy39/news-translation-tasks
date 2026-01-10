---
title: Things you need to know about working with SVG in VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-19T15:42:22.000Z'
originalURL: https://freecodecamp.org/news/things-you-need-to-know-about-working-with-svg-in-vs-code-63be593444dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LkyIv0Kk298yNUu2nHhSgg.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: SVG
  slug: svg
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Burke Holland

  Check out this VS Code release highlights video from Brian Clark. Towards the end,
  he shows how you can now zoom in on image previews in VS Code.

  https://youtu.be/MWz8y1D3PMQ

  I thought that was an interesting feature. I mean, let’s f...'
---

By Burke Holland

Check out this [VS Code release highlights video](https://code.visualstudio.com/updates/v1_20?WT.mc_id=vscoderelease-medium-buhollan) from [Brian Clark](https://twitter.com/_clarkio). Towards the end, he shows how you can now zoom in on image previews in VS Code.

%[https://youtu.be/MWz8y1D3PMQ]

I thought that was an interesting feature. I mean, let’s face it — there are only two types of people in the world: those who like to zoom in on images and those who won’t admit it. So I opened a project that I had to test it out and sure enough, it works as advertised.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cClUCHBbOIxPq5X5vHOPEg.png)

My next thought was to see if it worked on SVG images. Because I like to zoom in on SVG and watch it not degrade. At this point in my life, that is an enjoyable and fulfilling activity.

It turns out that VS Code does not provide a visual preview for SVG files from within the editor. Which makes sense. SVG is markup and VS Code treats SVG files like XML, which is only text. You would need [XSLT](https://en.wikipedia.org/wiki/XSLT) to render it into something you could _view_. I just triggered a bunch of you, and for that, I apologize.

Here is a great joke about XML to soothe your anxiety:

> “XML is like violence: If it isn’t working, you aren’t using enough of it”

> - Unknown

This got me wondering, if VS Code treats SVG like XML, what extensions are available to help me work with SVG in VS Code? It turns out that there are quite a few, and some work better than others. Here are a few of my favorite extensions for working with SVG in VS Code.

### SVG

The first extension is just called [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg&WT.mc_id=vscoderelease-medium-buhollan).

That’s right. This person was first to the game and got the coveted SVG name all to themselves. Like the person who registered the Twitter name “Burke.” What the heck, Sam! You haven’t tweeted in….YOU’VE NEVER TWEETED!

![Image](https://cdn-media-1.freecodecamp.org/images/1*le6FD4mNmlHMu7jTMlb2kA.png)
_Sam, if you’re reading this — tweet at me and let’s talk. Seriously. You don’t even want this account!_

As you can see from this GIF here, out the box Visual Studio Code has limited support for SVG because we know that it treats it like XML. It knows how to appropriately highlight the markup, but that’s about it. Notice that it literally has no suggestions for me here when I try and create this rectangle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XXkYkF9VkrjPjhopsqIw_Q.gif)

The primary thing the “SVG” extension does is add language support for SVG to Visual Studio Code. So now when I start typing `rect`, it gives me options for elements I may want to select and a description of what they are.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_782ezwZaplm7oTTT6TAQ.png)

Once it has the element, it now knows about all of the possible attributes as well.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n2coQIEQfmPGGGw31yWhGg.png)

And it even knows the values for some of these attributes if they are enumerations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NCML04UHivsnY5J0NhalWw.png)

#### Preview

This extension also provides a “Preview” function that shows a side-by-side preview with the markup and the rendered image. This is available from the Command Pallet (Ctrl/Cmd + Shift + P).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Y0488W57gQZhmTtaYcmOw.png)

The cool thing about this is that the preview updates live as you type your SVG. This makes for a pretty neat sandbox for building out SVG images by hand if that’s your jam.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-YsmT0Fp2pfuTjjrAVZumA.gif)

#### Minify

This extension also includes a minify command that will minify your SVG using SVGO. Take this beautiful image of a hillside created with Sketch. Yes, I made it all by myself.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U2XGkBcryp-WNyzjbemn0g.png)

This image is already pretty small. It comes in at around 9kb on disk. The SVG extension provides a “Minify” command in the Command Pallet (Ctrl/Cmd + Shift + P). Using that command reduces the size of the image to 5kb. That’s nearly half. Pretty impressive.

If we use the inline Git differentials in VS Code we can see some of what SVGO is doing. It’s removing things we don’t need like “id” or a parameter of 0 where the default is already 0. It also converted my `rect` to `path`. I have no idea why, but that’s super interesting! Whatever, SVGO. I trust you. Do your thing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2FIKY-LKJ4yF0DfFteHwdQ.png)

That’s most of what SVG for VS Code does. But there is another SVG extension that is also relevant here — **SVG Viewer**.

### SVG Viewer

[**SVG Viewer - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan)  
[_Extension for Visual Studio Code - SVG Viewer for Visual Studio Code._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan)

[SVG Viewer](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer&WT.mc_id=vscoderelease-medium-buhollan) provides the same side-by-side image preview that the SVG extension does. However, this one has two main advantages. First, you can auto-open the preview whenever you click on an `svg` file by adding the following line to your User Preferences file.

```
"svgviewer.enableautopreview": true,
```

AND, it shrinks the image to fit the window. I don’t know if I like this yet, but I think that I do. I think I prefer this over a giant image that I can’t see the entirety of.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhmcEToLx4stYr0P4tDtTA.png)

#### Convert To PNG

This extension also adds a convert command, so you can inline convert your SVG to PNG. Take this truck image. I exported it as SVG, but it’s just a data URI wrapped in an svg tag. There’s no point in that. I might as well take it back to a static image. With this extension, I don’t need to go back to Sketch to do that.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A07GtiA0XJ4holgAzKYG7A.gif)

This extension also allows you to copy the data URI scheme of any SVG. I guess that’s nice, but it’s not something that I ever do. I’m sure I will need to do it now that I have said that.

The last extension worth noting is the [SVG Editor](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan).

### SVG Editor

[**SVG Editor - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan)  
[_Extension for Visual Studio Code - Visual and literal SVG editor for VSCode._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan)

The [SVG Editor extension](https://marketplace.visualstudio.com/items?itemName=henoc.svgeditor&WT.mc_id=vscoderelease-medium-buhollan) is super aggressive. It attempts to create a complete SVG editing surface inside of VS Code, complete with drawing tools and the whole nine yards.

It’s important to note that this extension doesn’t work for me at all. Like it’s there, but it just doesn’t do anything as far as I can tell. Or maybe I’m doing it wrong. There is a high likelihood of that. My comprehensive testing approach consisted of “click around a bunch and see what happens.” Nothing ever did.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cvxmnb8Zp_w98wK5Vc-BEA.gif)

Yep — doesn’t work. But a tip of the hat for trying to build a graphics editor into Visual Studio Code. That’s no easy task, and the fact that someone even attempted to do it is highly impressive to me.

### Enjoy Your SVG

With extensions, VS Code has some pretty solid support for SVG. The two big things for me are the code completion and the preview. Although I should note that you cannot zoom in on any of the previews, so I still can’t satisfy my weird craving to watch the vector graphics scale.

You can grab the [latest version of VS Code today](https://code.visualstudio.com/?WT.mc_id=vscoderelease-medium-buhollan) and install these SVG extensions at your leisure.

