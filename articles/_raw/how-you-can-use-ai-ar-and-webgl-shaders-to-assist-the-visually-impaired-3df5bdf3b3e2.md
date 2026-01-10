---
title: How you can use AI, AR, and WebGL shaders to assist the visually impaired
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T21:25:37.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-ai-ar-and-webgl-shaders-to-assist-the-visually-impaired-3df5bdf3b3e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Vg0Gku4F-8K6sFtQiOZFQ.png
tags:
- name: Accessibility
  slug: accessibility
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dan Ruta

  Today, about 4% of the world’s population is visually impaired. Tasks like simple
  navigation across a room, or walking down a street pose real dangers they have to
  face every day. Current technology based solutions are too inaccessible, o...'
---

By Dan Ruta

Today, about 4% of the world’s population is visually impaired. Tasks like simple navigation across a room, or walking down a street pose real dangers they have to face every day. Current technology based solutions are too inaccessible, or difficult to use.

As part of a university assignment, we ([myself](https://twitter.com/Dan_Ruta), [Louis](https://twitter.com/LouisJordan), and [Tom](https://www.instagram.com/thomas.j.fox96/)) devised and implemented a new solution. We used configurable WebGL shaders to augment a video feed of a user’s surroundings in real-time. We rendered the output in a AR/VR format, with effects such as edge detection and color adjustments. Later, we also added color blindness simulation, for designers to use. We also added some AI experiments.

We did a more in-depth literature review in our original research paper. ACM published a shorter, two page version [here](https://dl.acm.org/citation.cfm?id=3196319&dl=ACM&coll=DL&preflayout=flat). This article focuses more on the technologies used, as well as some of the further uses, and experiments such as AI integration.

A popular approach we found in our studies of existing solutions was the use of edge detection for detecting obstacles in the environment. Most solutions fell short in terms of usability, or hardware accessibility and portability.

The most intuitive approach we could think of as feedback to the user was through the use of a VR headset. While this meant that the system would not be of help to very severely visually impaired people, it would be a much more intuitive system for those with partial sight, especially for those with blurry vision.

#### Edge detection

Feature detection, such as edges, are best done using 2D convolutions, and are even used in deep learning ([convolutional neural networks](http://cs231n.github.io/convolutional-networks/)). Simply put, these are dot products of a grid of image data (pixels) against weights in a kernel/filter. In edge detection, the output is higher (more white) when the pixel values line up with the filter values, representing an edge.

![Image](https://cdn-media-1.freecodecamp.org/images/mSstLIsZsNZK2vz-UaV3bLTnpiyQpoKTzNmk)
_This is done for every pixel. - [Image credit](http://jeanvitor.com/convolution-parallel-algorithm-python/" rel="noopener" target="_blank" title=")_

There are a few available options for edge detection filters. The ones we included as configurations are Frei-chen, and the 3x3 and 5x5 variants of [Sobel](https://en.wikipedia.org/wiki/Sobel_operator). They each achieved the same goal, but with slight differences. For example, the 3x3 Sobel filter was sharper than the 5x5 filter, but included more noise, from textures such as fabric:

![Image](https://cdn-media-1.freecodecamp.org/images/St0sndi1cpWo4e9GcpCu9p6yRITP8PVv1pTR)
_Left: 3x3, Right: 5x5_

#### The web platform

The primary reason we chose the web as a platform was its wide availability, and compatibility across almost all mobile devices. It also benefits from easier access, compared to native apps. However, this trade-off came with a few issues, mostly in terms of necessary set-up steps that a user would need to take:

1. Ensure network connectivity
2. Navigate to the web page
3. Turn the device to landscape mode
4. Configure the effect
5. Enable VR mode
6. Activate full screen mode (by tapping the screen)
7. Slot the phone into a VR headset

To avoid confusing a non-technical user, we created the website as a PWA ([progressive web app](https://developers.google.com/web/progressive-web-apps/)), allowing the user to save it to their Android home screen. This ensures it always starts on the correct page, landscape mode is forced on, the app is always full screen, and not reliant on a network connection.

#### Performance

Early JavaScript prototypes ran nowhere near our 60fps target, due to the very expensive convolution operations. We suspected that the bottleneck was JavaScript itself. We attempted a WebAssembly version. The resulting prototype ran even slower. This was most likely due to the overhead in passing the video frame data to the WebAssembly code, and back.

So instead, we turned to WebGL shaders. Shaders are awesome because of their extreme parallelization of a bit of code (the shader) across the texture (video feed) pixels. To maintain high performance, while keeping a high level of customization, the shader code had to be spliced together and re-compiled at run-time, as configurations changed, but with this, we managed to stay within the 16.7ms frame budget needed for 60fps.

#### Feedback

We carried out some user testing. We tested some basic tasks like navigation, and collected some qualitative feedback. This included adjustments to the UI, a suggestion to add an option to configure the colors of the edges and surfaces, and a remark that the field of view (FoV) was too low.

Both software improvement suggestions were applied. The FoV was not something which could have been fixed through software, due to camera hardware limitations. However, we managed to find a solution for this in the form of cheaply available phone-camera fish-eye lenses. The lenses expanded the FoV optically, instead of digitally.

![Image](https://cdn-media-1.freecodecamp.org/images/4jBuDXQcVSRCIW10boRa-Tl5rtdoEYHqerGM)
_Fish-eye lens_

![Image](https://cdn-media-1.freecodecamp.org/images/SDASEK6w5TFLXm7eXYzjYRQD1Ld7uWWTzofn)
_Left: no lens, Right: with lens_

Other than that, the system surpassed initial expectations, but fell short on reading text. This was due to there being two sets of edges for each character. Low light performance was also usable, despite the introduction of more noise.

![Image](https://cdn-media-1.freecodecamp.org/images/XUnEmgZYZn2cj5iSAEQvnXLHE0JlclqFWhXm)
_Some shader effect configuration examples_

Some other configurations we included was the radius of the effect, its intensity, and color inversion.

![Image](https://cdn-media-1.freecodecamp.org/images/5jvE831AtBsKj7eFSXr0hzCwmJTkfsmdzPsA)
_The options menu_

#### Other use cases

An idea we had was to add shader effects to simulate various types of color blindness, providing an easy way for designers to detect color blindness related accessibility issues in their products, be they software or otherwise.

Using RGB ratio values found [here](http://web.archive.org/web/20081014161121/http://www.colorjack.com/labs/colormatrix/), and turning off edge detection, we were able to add basic simulations of all major types of color blindness through extra, toggle-able components in the shaders.

![Image](https://cdn-media-1.freecodecamp.org/images/YflPhnWBrDuIrMI2w-WeOjQ122D-Vhz9E60J)
_Ishihara test - [Image Credit](http://www.colour-blindness.com/colour-blindness-tests/ishihara-colour-test-plates/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/BGBmXtHVuvC7WeWoFPubBOMCRZjevjccC3VP)
_**(Left)** Normal **(Right)** Deuteranopia filter_

![Image](https://cdn-media-1.freecodecamp.org/images/b4ZsxdfjfGFJAL2WxJ7EpBIaighVoALhJqOp)
_**(Left)** Normal **(Right)** Protanopia filter_

#### AI and future work

Although it’s an experiment, still in its very early stages, higher level object detection can be done using [tensorflowjs](https://js.tensorflow.org/) and [tfjs-yolo-tiny](https://github.com/ModelDepot/tfjs-yolo-tiny), a tensorflowjs port of [tiny-yolo](https://pjreddie.com/darknet/yolo/), a smaller and faster version of the YOLO object detection model.

![Image](https://cdn-media-1.freecodecamp.org/images/J6bwH0h0HQXONQaDapoimg6aUDcAr5jjJ2c6)
_The current categories_

![Image](https://cdn-media-1.freecodecamp.org/images/YGBVsqdO0WC9HizjlwNVoWOfh2I-XRHuqeMK)
_Example inference, using a laptop. Requires a decent GPU, to work._

The next step is to get instance segmentation working in a browser, with something similar to [mask rcnn](https://github.com/matterport/Mask_RCNN) (though, it may need to be smaller, like tiny-yolo), and add it to WebSight, to highlight items with a color mask, instead of boxes with labels.

![Image](https://cdn-media-1.freecodecamp.org/images/fs-OeTSPqBXdyLhBL8oU7gqIAQknnb3tDyr5)
_Goals — [Source](https://github.com/matterport/Mask_RCNN#4k-video-demo-by-karol-majek" rel="noopener" target="_blank" title=")_

The GitHub repo is [here](https://github.com/DanRuta/WebSight), and a live demo can be found at [https://websight.danruta.co.uk](https://websight.danruta.co.uk). Do note that until Apple provides support for the camera API in browsers, it might not work on Apple phones.

Of course, I had some extra fun with this as well. Being able to edit what you can see around you in real time opens up a world of opportunities.

For example, using a [Matrix shader](https://websight.danruta.co.uk/#matrix), you can feel like The One.

![Image](https://cdn-media-1.freecodecamp.org/images/PGMyqHkLVWBECPfmIxvEqpAGD7uz8e6pcPWf)
_Everything is drawn using green digits, not lines_

Or maybe you just enjoy watching the world [burn](https://websight.danruta.co.uk/#fire).

![Image](https://cdn-media-1.freecodecamp.org/images/3rZoIwLMDtceBYESlehqZWPecrbUdCjN8lLu)
_Playing: [Billy Joel — We Didn’t Start the Fire](https://www.youtube.com/watch?v=eFTLKWw542g" rel="noopener" target="_blank" title=")_

You can tweet more shader ideas at me here: @DanRuta

