---
title: Image File Types – The .jpeg, .svg, and .png Picture Format Extensions Explained
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-09T22:26:12.000Z'
originalURL: https://freecodecamp.org/news/image-file-types-picture-format-extensions-jpeg-gif-png-svg-tiff
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/timon-klauser-3MAmj1ZKSZA-unsplash.jpg
tags:
- name: Image Compression
  slug: image-compression
seo_title: null
seo_desc: 'When you’re working with images, it’s important to understand the different
  file types. Which format is best for what application?

  In this tutorial, we’re going to explain the most common image file types, and when
  you should use them.

  Note that this...'
---

When you’re working with images, it’s important to understand the different file types. Which format is best for what application?

In this tutorial, we’re going to explain the most common image file types, and when you should use them.

Note that this is a short, non-technical article. If you want to go much deeper on the performance side of things, read these guides on [how to optimize your website's images for the web](https://www.freecodecamp.org/news/tag/image-optimization/).

First, a quick explanation of how image compression works.

## Lossless vs Lossy – What is the Difference Between These Two Compression Types?

Lossless compression is a class of data compression algorithms that allows the original data to be perfectly reconstructed from the compressed data.

There is only so much you can compress a file before you start throwing away _some_ of the information that file contains.

This is where "Lossy" compression comes in. Lossy in that it loses some of the information.

Lossy compression permits reconstruction only of an approximation of the original data (though usually with greatly improved compression rates).

You will see both the terms "Lossless" and "Lossy" appear below when we describe different image file formats.

## What is the JPEG Format? (.jpg and .jpeg file extension)

JPEG is the most common file type for images. It’s best used for photos and other images with lots of colors.

By the way, JPEG stands for Joint Photographic Experts Group – the team that developed the standard.

JPEG files are smaller than other file types, so they’re easy to download and share.

### Can JPEGs be transparent or have a transparent background?

No. Unlike GIFs, SVGs, and PNGs, JPEGs cannot have transparent backgrounds. You would need to convert your JPEG to a different file format.

### Are .jpeg and .jpg are the same? 

Yes – the only difference is that, traditionally, file extensions are only 3 characters long. ".jpg" is a shortened form of ".jpeg".

## What is a PNG? The PNG File Format (.png file extension)

PNG is a lossless compression format for digital images. PNG was created as an improved replacement for GIF. It has become the most widely-used lossless image compression format on the web.

PNG is a file type that’s best used for images with transparency, like logos. PNG files are usually larger than JPEGs, so they’re not ideal for large images.

PNGs can have a transparent background.

## What is a GIF? The GIF Image Format (.gif file extension)

The GIF format is another type of image file that is commonly used on the web. GIF files are typically smaller than other image file types, making them ideal for use on the web.

GIFs can be used for static images. But they are more commonly associated with animations – a series of images that auto-play. For example, here's a public domain GIF.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Globespin.gif)
_A public domain GIF of the spinning globe_

This is really just a series of a dozen or so images playing in a loop.

Note that GIFs can also have a transparent background.

### How do you pronounce GIF?

The creator of the GIF format, Stephen Wilhite, said that he pronounced "jif" as in "Jif" peanut butter.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/6398248857_42ff8de345_h-1.jpeg)
_Jif peanut butter. Creative Commons photo by Brian Cantoni._

This said, almost all the developers I know pronounce it "gif", as in "gift", and I think that will continue to be the most popular way to say it.

%[https://twitter.com/FallonTonight/status/1011823951167750144?s=20&t=hGaYcvhV9J8H5n9pv9Em_A]

## What is a TIFF? The TIFF Image Format (.tif file format)

TIFF is a file type that it's best to use for high-quality images that need to be edited. TIFF files are large, so they’re not ideal for sharing online.

You should use a TIFF when quality is more important than file size. In practice, a PNG is almost always a better option – especially when dealing with images on the web.

## What is an SVG? The SVG File Format (.svg file extension)

An SVG is a Scalable Vector Graphic. This means that the graphic can be scaled to any size without losing quality.

Unlike all the other file formats we're discussing in this article, SVG files are vector files. (JPEG, PNG, GIF, and TIFF are raster files.)

This means that SVG files can be scaled to any size without losing quality, while raster files will lose quality when they are scaled up.

You can edit SVG files using vector editing software (or just manually update the coordinates and colors of the graphics). You can only edit a PNG files using raster editing software.

Here is an example SVG file from the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Getting_Started). This is what SVG looks like in its native XML code form:

```xml
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="red" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>
```

And this simple code renders this image:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/example-svg-file.png)
_A red square with a green dot and the letters "SVG" on it._

SVG files are usually smaller than PNG files, because they only contain the data necessary to draw the image, while PNG files contain the data for the entire image.

You can also animate SVG files using a tool called SMIL. Thus, they can serve as extremely space-efficient GIF files. And if you're really adventurous, you can program SVGs.

## JPEGs VS PNGs – Which Image Format is Best for the Web?

The web may look very different in the future, as we roll out more and more fiberoptic cable, and high speed satellite internet becomes more common.

But for now, my recommendation is to use JPEGs for most of your images.

If you have a company logo or a very important photo where quality is vital, PNG is a good option.

For logos, I recommend using an SVG, as it will scale infinitely, and is very compact in size.

## I hope you learned a lot about Image File Types.

And I hope you've found this helpful. If you want to learn more about programming and technology, try [freeCodeCamp's core coding curriculum](https://www.freecodecamp.org/learn). It's free.

