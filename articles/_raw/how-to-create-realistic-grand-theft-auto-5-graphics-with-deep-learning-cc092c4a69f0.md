---
title: How to create realistic Grand Theft Auto 5 graphics with Deep Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-01T20:37:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-realistic-grand-theft-auto-5-graphics-with-deep-learning-cc092c4a69f0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BgjLO87og9PUnDNtU7Ip7Q.gif
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: gaming
  slug: gaming
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chintan Trivedi

  This project is a continuation of my previous article. In it, I explained how we
  can use CycleGANs for image style transfer, and apply it to convert Fortnite graphics
  and make it look like PUBG.

  CycleGAN is a type of Generative Adv...'
---

By Chintan Trivedi

This project is a continuation of my [previous article](https://towardsdatascience.com/turning-fortnite-into-pubg-with-deep-learning-cyclegan-2f9d339dcdb0). In it, I explained how we can use CycleGANs for image style transfer, and apply it to convert Fortnite graphics and make it look like PUBG.

CycleGAN is a type of Generative Adversarial Network that is capable of mimicking the visual style of one image and transfering it onto another. We can use it to make a game’s graphics look like that of another game or the real world.

In this article, I wanted to share some more results using the same [CycleGAN algorithm](https://junyanz.github.io/CycleGAN/) which I covered in my previous work. First, I’ll try to improve GTA 5 graphics by adapting them to look like the real world. Next, I’ll cover how we can achieve the same photo-realistic results, without having to render high-detailed GTA graphics in the first place.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EZ0j8XVuf30B-ar3GXCIzg.png)
_Both the datasets that I’ve used for this are available at [this link](https://junyanz.github.io/CycleGAN/" rel="noopener" target="_blank" title=") on the original author’s project page._

For the first task, I have taken screenshots of the game as our source domain which we want to convert into something photo-realistic. The target domain comes from the cityscapes dataset that represents the real world (which we aim to make our game resemble).

### CycleGAN results

![Image](https://cdn-media-1.freecodecamp.org/images/1*3ZD4OtDtLVqQWExjydt6OA.gif)

Based on about three days of training for about 100 epochs, the Cyclegan model seems to do a very nice job of adapting GTA to the real world domain. I really like how the smaller details are not lost in this translation and the image retains its sharpness even at such a low resolution.

The main downside is that this neural network turned out to be quite materialistic: it hallucinates a Mercedes logo everywhere, ruining the almost perfect conversion from GTA to real world. (It’s because the cityscapes dataset was collected by a Mercedes owner.)

### How to achieve the same photo-realistic graphics with less effort

While this approach may seem very promising in improving game graphics, I do not think the real potential lies in following this pipeline. By that I mean that it seems impractical to render such a highly detailed image and then convert it to something else.

Wouldn’t it be better to synthesize a similar quality image but with much less time and effort in designing the game in the first place? I think the real potential lies in rendering objects with low detail and letting the neural net synthesize the final image from this rendering.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1DZl_0oqSQzKhUuL5GUh5g.png)

So, based on the semantic labels available in the cityscapes dataset, I segmented objects in a screenshot of GTA giving us a representation of low detail graphics. Consider this as a game rendering of only a few objects, like the road, car, houses, sky, and so on without designing them in detail. This will act as the input to our image style transfer model instead of the highly detailed screenshot from the game.

Let’s see what quality of final images can be generated from such low detail semantic maps using CycleGANs.

### Results of image synthesis from semantic maps

![Image](https://cdn-media-1.freecodecamp.org/images/1*kNx9TrAXmaGHUeivjwQReg.gif)
_Recreating photo-realistic scenes from the semantic maps of GTA 5._

Here are a few examples of how it looks when we recreate GTA graphics from semantic maps. Note that I have not created these maps by hand. That seemed really tedious, so I simply let another CycleGAN model do it (it is trained to perform image segmentation using the cityscapes dataset).

It seems like a good conversion from far away, but looking closely its quite obvious that the image is fake and lacks any kind of details.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XqPMGvpKwd4U7uN93dk6yQ.png)

Now, these results are 256p and have been generated on a GPU with 8 GB of memory. However, the authors of the original paper have shown that it is possible to create a much more detailed 2048 x 1024p image using a GPU with over 24 GB of memory. It uses the supervised learning version of CycleGAN, called [pix2pixHD](https://github.com/NVIDIA/pix2pixHD), that is trained to perform the same task. And boy does the fake image look pretty darn convincing!

![Image](https://cdn-media-1.freecodecamp.org/images/1*SJ09ZfgwAUw52XoL07jDGA.png)
_[Here’s the full video](https://www.youtube.com/watch?v=3AIpPlzM_qs&amp;t=23s" rel="noopener" target="_blank" title=") uploaded by the authors of this paper._

### Conclusion

GANs have great potential to change how the entertainment industry will produce content going forward. They are capable of producing much better results than humans and in much less time.

The same is applicable to the gaming industry as well. I’m sure that in a few years, this will revolutionize how game graphics are generated. It will be much easier to simply mimic the real world than to recreate everything from scratch.

Once we attain that, rolling out new games will also be much faster. Exciting times ahead with these advancements in Deep Learning!

#### More results in video format

All the above results and more can be found on my [YouTube channel](https://www.youtube.com/c/DeepGamingAI) and in the video embedded below. If you liked it, feel free to [subscribe](http://www.youtube.com/subscription_center?add_user=DeepGamingAI) to my channel to follow more of my work.

Thank you for reading! If you liked this article, please follow me on [Medium](https://medium.com/@chintan.t93), [GitHub](https://github.com/ChintanTrivedi), or subscribe to my [YouTube channel](http://youtube.com/c/DeepGamingAI).

