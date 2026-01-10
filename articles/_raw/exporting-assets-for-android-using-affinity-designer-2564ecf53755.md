---
title: Exporting assets for Android using Affinity Designer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T06:46:52.000Z'
originalURL: https://freecodecamp.org/news/exporting-assets-for-android-using-affinity-designer-2564ecf53755
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UH2YFK41CVHsBQM1r8qABQ.png
tags:
- name: Android
  slug: android
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dixita Ganatra

  Affinity Designer has a rich feature, Export Persona. I was wondering if it could
  ease the process of exporting assets for an Android project. Here’s what I found
  after delving into it.

  Preface

  This article assumes that you are fami...'
---

By Dixita Ganatra

[Affinity Designer](https://affinity.serif.com/en-gb/designer/) has a rich feature, **Export Persona**. I was wondering if it could ease the process of exporting assets for an Android project. Here’s what I found after delving into it.

#### Preface

This article assumes that you are familiar with navigating around in Affinity Designer. I am going to use an example mockup of a fitness app called **Watch Your Steps**. This app counts your daily footsteps, the time you were active, the calories you burned, and the distance you walked.

![Image](https://cdn-media-1.freecodecamp.org/images/QGOWZjfU8z54IHq4YGZIOymi1GSI38eHOlQE)
_“Watch Your Steps”_

To use these icons in an Android app, we need to export them. Since this application is going to run on Android devices with various screen sizes, we need to export them for various resolutions.

#### The Footsteps

**Step 1:** When your design is ready, switch to **Export Persona**.

![Image](https://cdn-media-1.freecodecamp.org/images/PhNCxNMRb2vf1HT8kr9wYSn1rEfZ3CW47kp9)
_Export Persona_

**Step 2:** Go to the **Slices** panel in the right pane.

![Image](https://cdn-media-1.freecodecamp.org/images/cH24SAa8xefhaadpih6sQfSmYAvfieVoy6LB)
_**Slices** panel_

To export icons, we need to slice them. Affinity creates a slice for our artwork by default. Now we need to slice the icons from our artwork. We will create slices from layers directly. We could use **Slice Tool** to create slices manually as well.

**Step 3:** Go to the Layers panel. Select the layers you want to export and click **Create Slice**.

![Image](https://cdn-media-1.freecodecamp.org/images/Aick0-inYuaP8QFArocDwh1p27VkOaAt7wNR)
_Layers to be sliced_

These are the layers which were created in **Draw Persona**. We are going to export the layers highlighted above. You should now be able to see blue borders around the sliced layers in your artwork indicating the slices created.

![Image](https://cdn-media-1.freecodecamp.org/images/tgJgk-HVZyTkxpgu3GOI8wBJSSIJfrpEYUjm)
_Slices_

**Step 4:** Go to the **Slices** panel and uncheck the default slice (the app slice in this example) and any other slice(s) that you don’t want to export.

![Image](https://cdn-media-1.freecodecamp.org/images/H3jruZ80r1eiHUhesv8Hkg61LZ2mpxRctsmW)
_Sliced layers_

**Step 5:** Expand a slice by clicking an arrow in the left side and set the file path.

![Image](https://cdn-media-1.freecodecamp.org/images/HPQFVDufWe4lZX4Kuh9auAdiWpaNxFf0T1R5)

It shows the details of a slice. The highlighted area shows the file path of the expanded slice. Since we gave our layers proper names, we can reuse them for file paths.

By default, the size of the png will be **1x** (same as of the icon). We need this size for **drawable-mdpi** in an Android project. Click on the file path, and perform the following steps to set it.

Remove **Scale suffix (1x)** from the filename and prepend `drawable-mdpi/` to our file path (do not forget the trailing /). Because we want our asset to be in the folder `drawable-mdpi/`, named `back_button.png`.

![Image](https://cdn-media-1.freecodecamp.org/images/f6idoX0cUSIO5yLeBVBEc4SrMjIsC8A5Fyil)
_drawable-mdpi/back_button.png_

**Step 6:** Follow the previous step for **drawable-hdpi — 1.5x, drawable-xhdpi — 2x, drawable-xxhdpi — 3x** and **drawable-xxxhdpi — 4x**.

After completing **Step 6**, the slice will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/iJfP5g7SzU0mpKoVYHsC6wKS-CElCaffEF73)
_All sizes with respective folders_

We don’t have to repeat this procedure for all the following icons. Affinity provides a feature to save this as a preset.

**Step 7:** Click on the menu icon from the top-right side of the Slices panel and select **Create export setup preset**. Then name it **Android** (or whatever you prefer).

![Image](https://cdn-media-1.freecodecamp.org/images/2FZxwSyVMNWwKrqekZA7S9B00SyjHcv94w7j)
_Create **Android** preset_

Now we are ready to select the rest of the slices and apply the **Android** preset on them. ?

![Image](https://cdn-media-1.freecodecamp.org/images/GAxwMzX3bQ35iwA-C5xHDXdjrZN8dgI9sJ3n)
_Apply Android preset to rest of the slices_

As you can see, once you create a preset it is extremely easy to apply on others.

**Step 8:** Click **Export Slices** placed in the bottom-right. The icons will be exported within their respective folders. After exporting them, the folder structure will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/BurQKOsSbedJfJP2StkliLRrGgDGB8uucJvn)
_Exported icons just like we wanted ?_

What if we change the icons later? Do we have to export them again ??

No, we don’t.

#### Bonus

Just check the highlighted option, **Continuous**.

![Image](https://cdn-media-1.freecodecamp.org/images/cg83sJ1q6zO8hQDr0QoPSoBCuW3LNuxtIoV5)
_Check continuous_

Now whenever you save your changes, exported assets will be updated continuously. Isn’t it cool ??

![Image](https://cdn-media-1.freecodecamp.org/images/vsm2ijONxrMgOziFPy1ymQfBc5M1TfA-gahF)
_Live update on saving the artwork_

That’s all folks. Contact me if you have any ideas worth sharing. I would love to hear from you on twitter [@dixita0607](https://twitter.com/dixita0607).

#### Application Mockup

You can download the mockup file used in this tutorial here ?.

[**watch-your-steps.afdesign**](https://drive.google.com/file/d/1XMIWRoeKHryH2B7i3CMLb30usCDJo3p2/view?usp=sharing)  
 drive.google.com

#### References

[**Android Icon Reference Chart | The Icon Handbook**](http://iconhandbook.co.uk/reference/chart/android/)  
[_The Icon Handbook is a reference manual, how-to guide and coffee table 'showcase' in one. learn how to design icons for…_iconhandbook.co.uk](http://iconhandbook.co.uk/reference/chart/android/)[**A Designers Guide for naming Android Assets**](https://medium.com/@AkhilDad/a-designers-guide-for-naming-android-assets-f790359d11e5)  
[_This article is mainly intended for Curious Designers and it will also help newbie developers but experienced…_medium.com](https://medium.com/@AkhilDad/a-designers-guide-for-naming-android-assets-f790359d11e5)

