---
title: Steganography Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/steganography-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d28740569d1a4ca3637.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: Steganography is the concept of concealing text, images, files, or videos
  within other text, images, files or videos. An offline example of this is using
  “invisible ink” to conceal a message between the lines of a letter. Lemon juice
  is a popular can...
---

Steganography is the concept of concealing text, images, files, or videos within other text, images, files or videos. An offline example of this is using “invisible ink” to conceal a message between the lines of a letter. Lemon juice is a popular candidate for invisible ink: [lemon juice invisible ink](https://www.youtube.com/embed/poCnU_crpjQ)  
  
Here is a very basic formula for the steganographic process:

> cover_medium + hidden_data + stego_key = stego_medium  
>   
> _In this context, the cover_medium is the file in which we will hide the hidden_data, which may also be encrypted using the stego_key. The resultant file is the stego_medium (which will, of course be the same type of file as the cover_medium).  
>   
> Source: [Steganography and Its Applications in Security](http://www.ijmer.com/papers/Vol2_Issue6/EN2646344638.pdf)_

## Steganography in images

On computers, images are stored as binary files. They contain a binary representation of the color or light intensity of each picture element (pixel) comprising the image. For example, this image of a dog:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/American_Eskimo_Dog.jpg)

might start out with something like:

```text
10010101   00001101   11001001
10010110   00001111   11001010
10011111   00010000   11001011
...
```

The simplest approach to hide data within the file is called least significant bit (LSB) insertion. With it, you can take the binary representation of the image and overwrite the LSB of each byte so that the change is minimal to the point where it can't be seen by the human eye.

While JPEG can be used for steganographic applications, it is more common to embed data in GIF or BMP files. GIF and 8-bit BMP files employ what is known as lossless compression, a scheme that allows the software to exactly reconstruct the original image. JPEG, on the other hand, uses lossy compression, which means that the expanded image is very nearly the same as the original but not an exact duplicate.

