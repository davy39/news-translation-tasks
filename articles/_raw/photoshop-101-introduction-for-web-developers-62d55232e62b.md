---
title: 'Photoshop 101: an introduction for web developers'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T21:19:02.000Z'
originalURL: https://freecodecamp.org/news/photoshop-101-introduction-for-web-developers-62d55232e62b
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cabbc740569d1a4ca93a0.jpg
tags:
- name: Design
  slug: design
- name: photoshop
  slug: photoshop
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vincent Humeau

  Introduction

  Often, when working as web developer, we need to integrate templates. They can be
  from Photoshop or other software. In this article, we will have a look at the basics
  of Photoshop for web developers.

  This content was in...'
---

By Vincent Humeau

### Introduction

Often, when working as web developer, we need to integrate templates. They can be from Photoshop or other software. In this article, we will have a look at the basics of Photoshop for web developers.

This content was initially written for a workshop for [DAMDigital London](http://damdigital.com/).

Adobe Photoshop is a raster graphics editor software, meaning it is a program that allows users to create and edit images.

![Image](https://cdn-media-1.freecodecamp.org/images/Hn9dRTjo6YkUp5YZ5bnr1oIGxXjjMm9G1j2V)
_Image [source](https://www.adobe.com/products/photoshop.html#hero-featured-video" rel="noopener" target="_blank" title=")_

It was released in 1988 and has grown to be the industry standard for graphics software.

You can download a free trial version of Photoshop on the [Adobe website](https://www.adobe.com/products/photoshop/free-trial-download.html).

### Workspace

Photoshop’s workspace is modular, so you can adapt it depending on the work you are doing. Some default workspaces are already set up in Photoshop. In this article, I’m using the `Graphic and Web` one. To change to this workspace, go into `Window/workspace/Graphic and Web`.

Let’s have a look at our workspace:

![Image](https://cdn-media-1.freecodecamp.org/images/GrHsceHchCL77wzBJVYovMnh6Wumhltg6ikN)
_Photoshop_

* **A — Menu bar**: This is where you’ll find most photoshop options.
* **B — Options bar**: This bar will give you all the options for the currently selected tool.
* **C — Toolbox**: This panel contains all the available tools from photoshop. Related tools are grouped together, and you can long click on one of them to see all the tools.
* **D — Panels**: It is the area where you have your basic panels open, such as `Layers`, `History`, and so on. To open a panel, just go into `Window/(Panel that you want to open)`

### Create a new file

When creating a new file in Photoshop, you first need to know for what medium the design is going to be used — meaning, is it going to be used for a screen (web, film, or video) or for print?

Depending on the answer to this question, you will need to change the PPI (Pixels Per Inch) value.

> _Pixels per inch (PPI) is a measurement used to define the resolution of a computer display. This metric evaluates the picture/image quality that a particular computing or output display device is able to display. Pixels per inch is also known as pixel density._ [Techopedia](https://www.techopedia.com/definition/2741/pixels-per-inch-ppi)

For print, you normally need 300PPI, but it actually depends on the printer and the size of the printed document. You should change your colour to CMYK as well, but again that depends on how you print your document. If you want to learn more about RGB and CMYK colours, check out this [article](https://printaura.com/difference-between-RGB-and-CMYK).

For screens and web ?, you need 72PPI and RGB colour. Then you need to specify your screen size. I would recommend designing first for mobile, then tablet and desktop.

As a web developer, you might not need to create a new file. Chances are that you will need to work with a design provided by web designers.

We are now going to look at an existing `.psd`template and work with it to have a look around Photoshop.

You can download and open this [PSD template](https://shibbythemes.com/psd-freebies/surfersco-psd-template/) from [Luis Costa](http://lucaal.co/).

### Layers

One of the core features of Photoshop is **layers**. Layers are like a stack of sheets, and you can see through transparent areas or area with low opacity (partially transparent).

You can open the layer panel in `Window/Layers`.

![Image](https://cdn-media-1.freecodecamp.org/images/tQQjIui8Q7xS3jxXIdyvWHDHNIVirFY8A93N)

The top layer in this panel will be placed over all the other layers underneath. Layers can be organized as well in folders. It is important to correctly name layers and folders. That will help during integration.

Next to each folder and layer, you have an eye icon. This allows you to toggle their visibility.

Your PSD might have a lot of layers and documents. One way to quickly find a layer is to select the `move tool (v)`. Right click on the canvas where you want to find your layer. You will get all the layers in the area where you have right clicked. By clicking on one, it will select this layer in your layer panel.

![Image](https://cdn-media-1.freecodecamp.org/images/G6F2Tk5n4XnwyY2X3J8cdswbGb-EWxZcIglZ)

### Toolbox

Photoshop comes with a load of tools. I’m going to show you a few useful ones that will help you ?.

First, if you just install Photoshop CC 2018, you will need to restore all tools. So go to `Edit > Tool`bar and click on the Restore Defaults button.

![Image](https://cdn-media-1.freecodecamp.org/images/UMkamoH1ixOjCLaOS6Z9bM-NVc1QReFOByyK)
_[Image from Adobe](https://helpx.adobe.com/photoshop/using/tools.html" rel="noopener" target="_blank" title="https://helpx.adobe.com/photoshop/using/tools.html)_

We are going to see some of the most useful tools you’d use to integrate a template:

#### A — Selection tools

* **Move**: Allows the user to move a layer around the canvas. As we saw earlier, it can be used as well to find a layer if you right click on your canvas.
* **Rectangular Marquee**: This tool is used to select an area of the canvas to copy and paste, fill it in, and so on. It can be used as well to measure. When your selection is done, you can find the size of the selected area in `Window/Info`. You might need to change the default unit in photoshop `Edit/preferences/general/Unit & Rulers` then set your units to pixels.

![Image](https://cdn-media-1.freecodecamp.org/images/RNWaDP1kVGLAyGz3DrKZXT-TCHYLFNYjazj8)

#### B — Crop and Slice tools

* **Crop**: This tool can… crop an image ?. In the tool settings (Options Bar), you can set an aspect ratio that you want to keep.

#### C — Measuring tools

* **Eyedropper**: The eyedropper allows you to quickly get a color reference in your design. Just click where you want the color. Then at the bottom of your toolbox, the foreground color will change to the selected color. If you click on the foreground color, it will open the `color picker window`. From there you can get the value of your color.
* **Color Sampler**: When integrating your design, you might need to select multiple colors. We are going to use the info window again `Window/Info`. This tool allows us to create a color sampler. Just click on the area of the image you want to get the colors from. You will get each color in the info panel. You can change the color type to web by clicking on the Eyedropper icon under the number.

![Image](https://cdn-media-1.freecodecamp.org/images/-r5ub2UTHKZWsnsIUtm4SdjRBEbGODTwmwHw)

* **Ruler**: helps you to measure your template. All the info will appear in your info window. Maintain `Shift`when measuring, so your ruler stays straight. You can get angles also.

#### G — Navigation tool

* **Hand**: This tool helps you to get around the canvas. You can access this tool at any time by holding the spacebar and dragging it with your mouse.
* **Zoom**: Allows you to zoom in and out (you can you `Ctrl` + `+`, or `Ctrl` + `-` too).

### Guides

As you might have noticed when opening our PSD file, we have some green lines on our template. They are guides. They are basically helpers that will help you build or measure things around your canvas.

You can move existing guides using the `move tool`(v).

To create new guides, you will need to open your ruler: `View/Ruler` or `Ctrl` + `R`. The ruler will appear in your workspace. Then from the ruler, you can drag a new guide into your canvas.

To remove a guide, use the `move tool`(v) and put the guide back in the ruler.

To hide and show all your guides, you can just use `Ctrl` + `H`, or go to `View/Extras`.

### Smart objects

What are smart objects?

> _Smart Objects are layers that contain image data from raster or vector images, such as Photoshop or Illustrator files. Smart Objects preserve an image’s source content with all its original characteristics, enabling you to perform nondestructive editing to the layer._ [Adobe](https://helpx.adobe.com/photoshop/using/create-smart-objects.html)

Smart objects can be recognized in your layers when they have the following icon in their thumbnails:

![Image](https://cdn-media-1.freecodecamp.org/images/QyPI1W-pNwBcjwv8oz4WAY8oAorz4TbhcNHk)

Smart objects are really handy if you work with vector-type images (SVG, EPS, AI), but are also useful with other complex raster files.

Let’s try to import a smart object into our PSD. Download an SVG file from [flaticon](https://www.flaticon.com/free-icon/surfboard_930944#term=surf&page=1&position=10). To import our SVG in our canvas, just drag the file into the canvas. We can now edit our SVG in illustrator, or any other vector software, by double-clicking on the thumbnail or our smart object. Changes will appear in our PSD.

Smart objects can do way more than that, though. If you want to learn more about them, check out [10 Things You Need to Know About Smart Objects in Photoshop](https://design.tutsplus.com/tutorials/10-things-you-need-to-know-about-smart-objects-in-photoshop--cms-20268).

### Export assets

First, just a reminder that photoshop is a **raster** software, not a **vector** software. This means we “can’t” export SVG files from photoshop. To do so, you will need to export these kinds of files from Illustrator or Inkscape, for example.

On the web, we want to have light image files. For photography, we would use a compressed `.jpg` file. If you need to use transparency (Alpha channel) we would use `.png` file. For an animated image, we would use a `.gif`. If you need a vector image (icons, for example) the best is to export your file as `.svg`. If you want to have more information about all the files available in Photoshop, you can check out ["file formats" in the Adobe's website](https://helpx.adobe.com/photoshop/using/file-formats.html).

#### Export our canvas

To export the canvas, just follow these steps:

1. Go to `File/Export/Save for Web`
2. Pick file format
3. Pick image size
4. Pick quality
5. Save

#### Export only an asset from the canvas

You will probably need to export some assets of your template.

Let’s export the left arrow in the product carousel:

![Image](https://cdn-media-1.freecodecamp.org/images/rK3w29prW1my7q8LEhDrTfHTURlhqj9CIKh6)

Using the move tool, we are going to find our layer. Right click on the arrow and select the layer `Arrow Left`. Now just right click on this layer in the layer panel. Select `export as` and select the type of file you need.

We can also export folders.

### Actions

What’s an action in Photoshop?

> _An action is a series of tasks that you playback on a single file or a batch of files — menu commands, panel options, tool actions, and so on. For example, you can create an action that changes the size of an image, applies an effect to the image, and then saves the file in the desired format._ [Adobe](https://helpx.adobe.com/photoshop/using/actions-actions-panel.html)

This feature is really convenient if you want to resize a batch of images for the web!

Let’s create a new action to crop an image and export this one:

1. Download a bunch of images from [https://unsplash.com/](https://unsplash.com/)
2. Open one of those images
3. Open the `Actions` panel, `Window/Actions`,
4. Create a new action by clicking on the icon **Create a new action** (The one on the left of the bin icon). Let’s name this action **Export for web — client name.**
5. We are now recording our action. The record button will be red, and you can stop recording by clicking on the stop icon (square icon on the left)/
6. Select the crop icon and set the ratio to 1x1 and crop the image/
7. Now we want to export our image, `File/Export/Save for Web`, select `JPG`, quality 50% and width 500px.
8. Click save and pick your destination folder.
9. Close your image without saving it.
10. To stop recording click on the stop icon (square icon on the left).

We now have our action, so we can open an image and just “play” our action by clicking on the play button.

If we want to apply our action to a batch of images, just follow these steps:

1. Go to `File/Automate/Batch`
2. Select the `Source` folder.
3. Select our action
4. Click on `Ok`

And voilà! All your images are in the export folder.

I hope you’ve enjoyed this small Photoshop 101 introduction for web developers ?. If you want to have a 102 version, let me know what you would like to know or to read more about ?.

* [@vince_umo](https://twitter.com/vince_umo)
* [vincent-humeau.com](http://vincent-humeau.com/)

