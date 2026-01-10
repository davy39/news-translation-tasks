---
title: How to Blur a Picture in Photoshop - Blur Faces, Backgrounds, and More
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-09T17:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-blur-a-picture-in-photoshop-blur-faces-backgrounds-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/blur-face.png
tags:
- name: photoshop
  slug: photoshop
seo_title: null
seo_desc: 'This tutorial will show you how to blur faces, backgrounds, text, and more
  using Photoshop CC.

  We''ll be making use of the Gaussian blur effect. The first step is to open the
  image you want to modify in Photoshop CC.


  How to blur an entire image in Ph...'
---

This tutorial will show you how to blur faces, backgrounds, text, and more using Photoshop CC.

We'll be making use of the Gaussian blur effect. The first step is to open the image you want to modify in Photoshop CC.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-151.png)

### How to blur an entire image in Photoshop

If you want to blur the entire image choose **Filter > Blur > Gaussian Blur...**

Adjust the radius to add more or less blur to the image. Then click "OK".

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-155.png)

You're done!

### How to blur faces in Photoshop (easy method)

If you want to blur a face in Photoshop, here is an easy way to do it. You can also use this method to blur text, logos, backgrounds, and anything else you want to blur. 

First, use the selection tools to select the area you want to blur. In the following example, the face is selected using the Elliptical Marquee Tool.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-156.png)

Next, apply a Gaussian Blur just like before (**Filter > Blur > Gaussian Blur...**). Select the radius and click "OK". Finally, choose **Select > Deselect**.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-157.png)

You're done!

### How to blur faces in Photoshop (advanced method)

In the easy method above, there is a hard line between the blurred section and the unblurred section. If you want to make a soft transition between the sections, use this advanced method. This method will also keep the unblurred version on a separate layer so it will be easy to revert if necessary.

First, duplicate the layer by right clicking on the layer and selecting "Duplicate layer...".

Next, apply a Gaussian Blur just like before (**Filter > Blur > Gaussian Blur...**) with your desired radius.

Add a layer mask to the duplicated layer by clicking the "Add vector mask" button. Make sure to hold OPTION on Mac or ALT on Windows while clicking the button to conceal the entire layer behind the mask. You will no longer see the blurred layer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-159.png)

The next step is to use a brush tool to paint the areas that you want to be blurred. Make sure the brush tool has a soft edge (consider setting the hardness to 0%) and use white as the foreground color.

When you paint white on the mask the areas you paint will become blurred because the blurred layer is revealed.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-160.png)

You can see in the image above that the original unblurred layer is still available.

You can continue to paint any section you want blurred.

You're done!

